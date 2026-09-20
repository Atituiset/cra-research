#!/usr/bin/env python3
"""Stage 4 — VEX generation (OpenVEX).

Merges association results (SBOM<->OSV) with reachability conclusions into an
OpenVEX document. Rules:

  reachability affected     -> status affected
  reachability not_affected -> status not_affected; justification from the tool
                               (govulncheck emits vulnerable_code_not_present /
                               vulnerable_code_not_in_execute_path; Joern-based
                               conclusions use vulnerable_code_not_in_execute_path)
  associated but no reachability verdict -> under_investigation (never silently
                               dropped)

Every statement carries an `evidence_refs` extension property pointing at the
signed reachability attestation hashes once attestation has run (attest.py
back-fills them into this file via --attestation-map; until then the field
references the raw tool-output hashes).
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import read_json, write_json, now_iso

OPEN_VEX_CONTEXT = "https://openvex.dev/ns/v0.2.0"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--sbom", required=True)
    ap.add_argument("--associations", required=True)
    ap.add_argument("--reachability", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--attestation-map", help="json: vuln_id -> attestation sha256")
    args = ap.parse_args()

    sbom = read_json(args.sbom)
    meta = {p["name"]: p["value"] for p in sbom.get("metadata", {}).get("properties", [])}
    artifact_sha = meta.get("cra-research:artifact-sha256", "unknown")
    product_id = f"pkg:generic/{args.product}@{args.version}"

    assoc = read_json(args.associations)
    reach = read_json(args.reachability)
    att_map = read_json(args.attestation_map) if args.attestation_map else {}

    findings = {f["vuln_id"]: f for f in reach.get("findings", [])}
    # alias index: CVE/GHSA <-> GO-id (canonical = the finding's own id)
    alias_of = {}
    for f in reach.get("findings", []):
        for a in f.get("aliases", []):
            alias_of[a] = f["vuln_id"]

    # OSV returns GHSA-* and GO-* as separate entries for the same issue;
    # group associations by canonical finding so each vuln yields one statement.
    grouped = {}
    for a in assoc["associations"]:
        canon = alias_of.get(a["vuln_id"], a["vuln_id"])
        g = grouped.setdefault(canon, {"ids": [], "aliases": set(), "assoc": a})
        g["ids"].append(a["vuln_id"])
        g["aliases"].update(a.get("aliases", []))

    statements = []
    for canon, g in grouped.items():
        a = g["assoc"]
        vid = canon
        all_ids = sorted(set(g["ids"]))
        f = findings.get(canon)
        evidence = [{
            "kind": "tool-output",
            "tool": reach["tool"]["name"],
            "path": reach["raw_outputs"][k]["path"],
            "sha256": reach["raw_outputs"][k]["sha256"],
        } for k in reach.get("raw_outputs", {})]
        if vid in att_map:
            evidence.append({
                "kind": "attestation",
                "sha256": att_map[vid],
                "predicateType": "https://cra-research.dev/attestation/conclusion/v0.1",
            })
        merged_aliases = sorted(g["aliases"] | {i for i in all_ids if i != vid})
        if f:
            status = f["status"]
            stmt = {
                "vulnerability": {"name": vid, "aliases": merged_aliases},
                "products": [{"@id": product_id,
                              "identifiers": {"sha256": artifact_sha}}],
                "status": status,
            }
            if status == "not_affected":
                stmt["justification"] = f.get("justification") or "vulnerable_code_not_in_execute_path"
                stmt["impact_statement"] = (
                    f.get("impact_statement")
                    or "Reachability analysis found no execution path from the product "
                       "entry point to the vulnerable code; see evidence_refs.")
            elif status == "affected":
                stmt["action_statement"] = ("Upgrade the affected dependency; see "
                                            "reachability evidence for the exposed call path.")
            if f.get("call_path"):
                evidence.append({"kind": "call-path", "hops": f["call_path"],
                                 "path_length": f["call_path_length"]})
            if f.get("call_trace"):
                evidence.append({"kind": "call-trace", "frames": f["call_trace"][:12]})
            stmt["evidence_refs"] = evidence
        else:
            stmt = {
                "vulnerability": {"name": vid, "aliases": merged_aliases},
                "products": [{"@id": product_id,
                              "identifiers": {"sha256": artifact_sha}}],
                "status": "under_investigation",
                "impact_statement": "Associated via SBOM<->OSV but no reachability "
                                    "verdict was produced for this component.",
                "evidence_refs": evidence,
            }
        statements.append(stmt)

    vex = {
        "@context": OPEN_VEX_CONTEXT,
        "@id": f"https://cra-research.dev/vex/{args.product}-{args.version}",
        "author": "cra-research poc pipeline",
        "timestamp": now_iso(),
        "version": 1,
        "statements": statements,
    }
    write_json(args.out, vex)
    from collections import Counter
    print(json.dumps({"product": args.product,
                      "statements": dict(Counter(s["status"] for s in statements))},
                     indent=2))


if __name__ == "__main__":
    main()
