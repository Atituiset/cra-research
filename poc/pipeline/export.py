#!/usr/bin/env python3
"""Stage 6 — export the evidence pack.

Writes out/evidence-pack-<product>-<version>/ with:
  sbom.cdx.json      — the CycloneDX SBOM
  vex.openvex.json   — the OpenVEX document (attestation refs back-filled)
  attestations/      — every signed in-toto Statement v1 envelope
  manifest.json      — content-addressed index of everything in the pack
  trace-report.md    — human-readable traceability report, one section per
                       conclusion: conclusion -> evidence -> tool -> artifact
                       sha256 -> timestamp -> signer, signature re-verified
                       at export time
"""
import argparse
import base64
import hashlib
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import read_json, sha256_file, write_json, now_iso
from store import connect


def verify_envelope(env_dict, pub_dict):
    # Envelope.from_dict mutates its argument (pops fields) — verify a copy.
    import copy
    from in_toto.models.metadata import Envelope
    env = Envelope.from_dict(copy.deepcopy(env_dict))
    try:
        env.verify_signature(pub_dict)
        return True
    except Exception as e:  # noqa: BLE001 — report, don't crash the export
        return f"FAILED: {e}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--sbom", required=True)
    ap.add_argument("--vex", required=True)
    ap.add_argument("--keys", required=True)
    ap.add_argument("--outroot", required=True)
    ap.add_argument("--db", default=None)
    args = ap.parse_args()

    from securesystemslib.signer import SSlibKey
    with open(os.path.join(args.keys, "dev-ed25519.pub.json")) as f:
        pub_dict = json.load(f)
    pub = SSlibKey.from_dict(pub_dict["keyid"],
                             {k: v for k, v in pub_dict.items() if k != "keyid"})

    conn = connect(args.db) if args.db else connect()
    outdir = os.path.join(args.outroot, f"evidence-pack-{args.product}-{args.version}")
    if os.path.exists(outdir):
        shutil.rmtree(outdir)
    os.makedirs(os.path.join(outdir, "attestations"))

    shutil.copy(args.sbom, os.path.join(outdir, "sbom.cdx.json"))
    shutil.copy(args.vex, os.path.join(outdir, "vex.openvex.json"))

    rows = conn.execute(
        "SELECT c.*, a.envelope_json, a.keyid FROM conclusions c "
        "JOIN attestations a ON a.sha256 = c.attestation_sha256 "
        "WHERE c.product=? AND c.version=? ORDER BY c.conclusion_type, c.vuln_id",
        (args.product, args.version)).fetchall()

    artifact = conn.execute(
        "SELECT * FROM artifacts WHERE product=? AND version=? AND name='binary'",
        (args.product, args.version)).fetchone()

    lines = [
        f"# Traceability report — {args.product} {args.version}",
        "",
        f"- exported_at: {now_iso()}",
        f"- product artifact: `{os.path.basename(artifact['path'])}` "
        f"sha256:`{artifact['sha256']}`",
        f"- signer: `{rows[0]['keyid'] if rows else 'n/a'}` "
        f"(dev key, keys/dev-ed25519.pub.json)",
        f"- conclusions: {len(rows)}",
        "",
        "Each section: conclusion → evidence → tool → artifact hash → timestamp → signer.",
        "",
    ]
    manifest = {"product": args.product, "version": args.version,
                "exported_at": now_iso(), "files": {}, "conclusions": []}

    for r in rows:
        env = json.loads(r["envelope_json"])
        payload = json.loads(base64.b64decode(env["payload"]).decode())
        pred = payload["predicate"]
        verified = verify_envelope(env, pub_dict)
        fname = f"{r['conclusion_type']}-{r['vuln_id']}-{r['attestation_sha256'][:12]}.json"
        with open(os.path.join(outdir, "attestations", fname), "w") as f:
            json.dump(env, f, indent=2, sort_keys=True)

        lines += [
            f"## {r['conclusion_type']}: {r['vuln_id']} — **{r['status']}**",
            "",
            f"- conclusion_id: `{r['id']}`",
            f"- justification: `{r['justification'] or '—'}`",
            f"- attestation: `attestations/{fname}` sha256:`{r['attestation_sha256']}`",
            f"- signature: **{'verified ✓' if verified is True else verified}** "
            f"(keyid `{r['keyid'][:16]}…`, signer `{pred.get('signer')}`)",
            f"- subject: `{payload['subject'][0]['name']}` "
            f"sha256:`{payload['subject'][0]['digest']['sha256']}`",
            f"- tool: `{pred['tool']['name']}` — {pred['tool']['version']}",
            f"  - command: `{pred['tool']['command']}`",
            f"- timestamp: {pred['timestamp']}",
            "- evidence:",
        ]
        for ev in pred.get("evidence", []):
            if ev["kind"].startswith("tool-output"):
                lines.append(f"  - `{ev['kind']}` `{ev.get('path')}` sha256:`{ev.get('sha256')}`")
            elif ev["kind"] == "call-path":
                lines.append(f"  - call-path (len {ev.get('path_length')}): `{ev.get('path')}`")
                for h in ev.get("hops", []):
                    loc = f"{h.get('defined_in')}:{h.get('defined_line')}"
                    call = (f" called at {h['called_in_file']}:{h['called_at_line']}"
                            if h.get("called_at_line") else "")
                    lines.append(f"    - `{h['function']}` ({loc}){call}")
            elif ev["kind"] == "call-trace":
                for fr in ev.get("frames", [])[:6]:
                    lines.append(f"  - trace: `{fr.get('function')}` ({fr.get('package')})")
            else:
                lines.append(f"  - {json.dumps(ev)[:200]}")
        lines.append("")
        manifest["conclusions"].append({
            "id": r["id"], "type": r["conclusion_type"], "vuln": r["vuln_id"],
            "status": r["status"], "attestation_sha256": r["attestation_sha256"],
            "signature_verified": verified is True,
        })

    with open(os.path.join(outdir, "trace-report.md"), "w") as f:
        f.write("\n".join(lines))

    for root, _, files in os.walk(outdir):
        for fn in files:
            p = os.path.join(root, fn)
            rel = os.path.relpath(p, outdir)
            if rel != "manifest.json":
                manifest["files"][rel] = sha256_file(p)
    write_json(os.path.join(outdir, "manifest.json"), manifest)
    print(json.dumps({"pack": outdir, "conclusions": len(rows),
                      "all_signatures_verified": all(
                          c["signature_verified"] for c in manifest["conclusions"])},
                     indent=2))


if __name__ == "__main__":
    main()
