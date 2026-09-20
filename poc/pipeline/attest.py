#!/usr/bin/env python3
"""Stage 5 — sign conclusions into in-toto attestations and store them.

Each conclusion (reachability / vex / verification) becomes an in-toto
Statement v1 with predicateType https://cra-research.dev/attestation/conclusion/v0.1,
DSSE-enveloped and ed25519-signed with the dev key (keys/). The envelope bytes
are content-addressed (sha256) into SQLite; the signed JSON is also written to
<outdir>/attestations/ for the evidence pack.

Chain of traceability per conclusion:
  conclusion -> predicate.evidence (call path / tool output hashes / OSV ids)
             -> predicate.tool{name,version,command}
             -> subject digest (product artifact sha256)
             -> predicate.timestamp
             -> envelope signature keyid -> signer
"""
import argparse
import json
import os
import sys
import uuid

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import (PREDICATE_TYPE, SIGNER_NAME, STATEMENT_TYPE, read_json,
                  sha256_bytes, sha256_file, write_json, now_iso)
from store import connect

from in_toto.models.metadata import Envelope
from securesystemslib.signer import CryptoSigner, SSlibKey


def load_signer(keys_dir):
    with open(os.path.join(keys_dir, "dev-ed25519.pem"), "rb") as f:
        priv = f.read()
    with open(os.path.join(keys_dir, "dev-ed25519.pub.json")) as f:
        pub_dict = json.load(f)
    pub = SSlibKey.from_dict(pub_dict["keyid"],
                             {k: v for k, v in pub_dict.items() if k != "keyid"})
    priv_path = os.path.abspath(os.path.join(keys_dir, "dev-ed25519.pem"))
    return CryptoSigner.from_priv_key_uri("file2:" + priv_path, pub), pub


def build_statement(subject_name, subject_sha, predicate):
    return {
        "_type": STATEMENT_TYPE,
        "subject": [{"name": subject_name, "digest": {"sha256": subject_sha}}],
        "predicateType": PREDICATE_TYPE,
        "predicate": predicate,
    }


def sign_statement(stmt, signer):
    payload = json.dumps(stmt, sort_keys=True).encode("utf-8")
    env = Envelope(payload=payload, payload_type="application/vnd.in-toto+json",
                   signatures={})
    sig = env.create_signature(signer)
    env.signatures = {sig.keyid: sig}
    env_bytes = json.dumps(env.to_dict(), sort_keys=True).encode("utf-8")
    return env, env_bytes


def evidence_for_finding(f, reach):
    ev = []
    for k, meta in reach.get("raw_outputs", {}).items():
        ev.append({"kind": f"tool-output:{k}", "path": meta["path"],
                   "sha256": meta["sha256"]})
    if f.get("call_path"):
        ev.append({"kind": "call-path",
                   "path": " -> ".join(h["function"] for h in f["call_path"]),
                   "hops": f["call_path"],
                   "path_length": f["call_path_length"]})
    if f.get("call_trace"):
        ev.append({"kind": "call-trace", "frames": f["call_trace"][:12]})
    return ev


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--artifact", required=True)
    ap.add_argument("--sbom", required=True)
    ap.add_argument("--associations", required=True)
    ap.add_argument("--reachability", required=True)
    ap.add_argument("--vex", required=True)
    ap.add_argument("--keys", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--db", default=None)
    args = ap.parse_args()

    signer, pub = load_signer(args.keys)
    conn = connect(args.db) if args.db else connect()

    artifact_sha = sha256_file(args.artifact)
    for name, path, typ in [
        ("binary", args.artifact, "application/octet-stream"),
        ("sbom", args.sbom, "application/vnd.cyclonedx+json"),
        ("vex", args.vex, "application/vnd.openvex+json"),
    ]:
        conn.execute(
            "INSERT OR REPLACE INTO artifacts(product,version,name,path,sha256,type,created_at)"
            " VALUES (?,?,?,?,?,?,?)",
            (args.product, args.version, name, os.path.abspath(path),
             sha256_file(path), typ, now_iso()))

    reach = read_json(args.reachability)
    assoc = read_json(args.associations)
    vex = read_json(args.vex)
    vex_by_vuln = {}
    for s in vex.get("statements", []):
        vex_by_vuln[s["vulnerability"]["name"]] = s
        for al in s["vulnerability"].get("aliases", []):
            vex_by_vuln.setdefault(al, s)

    att_dir = os.path.join(args.outdir, "attestations")
    os.makedirs(att_dir, exist_ok=True)
    attestation_map = {}

    def record(conclusion_type, vuln_id, status, justification, tool, evidence,
               extra=None):
        cid = str(uuid.uuid4())
        predicate = {
            "conclusion_type": conclusion_type,
            "conclusion_id": cid,
            "product": args.product,
            "product_version": args.version,
            "vulnerability": {"id": vuln_id},
            "status": status,
            "justification": justification,
            "evidence": evidence,
            "tool": tool,
            "timestamp": now_iso(),
            "signer": SIGNER_NAME,
        }
        if extra:
            predicate.update(extra)
        for ev in evidence:
            if ev.get("sha256"):
                conn.execute(
                    "INSERT OR IGNORE INTO evidence(sha256,kind,path,inline_json,created_at)"
                    " VALUES (?,?,?,?,?)",
                    (ev["sha256"], ev["kind"], ev.get("path"),
                     json.dumps(ev) if not ev.get("path") else None, now_iso()))
        stmt = build_statement(f"{args.product}-{args.version}", artifact_sha, predicate)
        env, env_bytes = sign_statement(stmt, signer)
        sha = sha256_bytes(env_bytes)
        fname = os.path.join(att_dir, f"{conclusion_type}-{vuln_id}-{sha[:12]}.json")
        with open(fname, "w") as fh:
            fh.write(json.dumps(env.to_dict(), indent=2, sort_keys=True))
        conn.execute(
            "INSERT INTO conclusions(id,product,version,conclusion_type,vuln_id,status,"
            "justification,tool_name,tool_version,tool_command,evidence_json,"
            "attestation_sha256,created_at) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (cid, args.product, args.version, conclusion_type, vuln_id, status,
             justification, tool["name"], tool["version"], tool["command"],
             json.dumps(evidence), sha, now_iso()))
        conn.execute(
            "INSERT OR REPLACE INTO attestations(sha256,conclusion_id,envelope_json,"
            "signer,keyid,created_at) VALUES (?,?,?,?,?,?)",
            (sha, cid, json.dumps(env.to_dict(), sort_keys=True), SIGNER_NAME,
             pub.keyid, now_iso()))
        if conclusion_type == "reachability":
            attestation_map[vuln_id] = sha
        return sha

    # 1) reachability conclusions
    for f in reach.get("findings", []):
        record("reachability", f["vuln_id"], f["status"], f.get("justification"),
               reach["tool"], evidence_for_finding(f, reach))

    # 2) vex conclusions (one per OpenVEX statement)
    for s in vex.get("statements", []):
        vid = s["vulnerability"]["name"]
        record("vex", vid, s["status"], s.get("justification"),
               {"name": "vex.py", "version": "0.1.0",
                "command": " ".join(sys.argv)},
               [{"kind": "tool-output:openvex",
                 "path": os.path.abspath(args.vex),
                 "sha256": sha256_file(args.vex)}],
               extra={"openvex_statement_status": s["status"],
                      "aliases": s["vulnerability"].get("aliases", [])})

    # 3) fix verification conclusions (Go flow only, when a fixed build was scanned)
    fv = reach.get("fix_verification")
    if fv:
        still = set(fv["vulns_still_present"])
        for f in reach.get("findings", []):
            if f["status"] != "affected":
                continue
            fixed = f["vuln_id"] not in still
            record("verification", f["vuln_id"],
                   "fixed" if fixed else "still_present",
                   None if fixed else "vulnerable_code_present",
                   reach["tool"],
                   [{"kind": "tool-output:fixed-openvex",
                     "path": fv["raw_outputs"]["openvex"]["path"],
                     "sha256": fv["raw_outputs"]["openvex"]["sha256"]}],
                   extra={"fixed_variant": fv["fixed_appdir"]})

    conn.commit()
    write_json(os.path.join(args.outdir, "attestation-map.json"), attestation_map)
    print(json.dumps({"product": args.product,
                      "attestations": len(attestation_map) and
                      conn.execute("SELECT COUNT(*) FROM attestations").fetchone()[0],
                      "keyid": pub.keyid}, indent=2))


if __name__ == "__main__":
    main()
