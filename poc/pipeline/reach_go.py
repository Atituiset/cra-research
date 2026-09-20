#!/usr/bin/env python3
"""Stage 3a — Go reachability via govulncheck.

govulncheck does symbol-level reachability against the Go vuln database and can
emit OpenVEX directly (-format openvex), which we parse into normalized
reachability conclusions. Raw tool outputs (openvex + json) are kept and hashed
as evidence. With --verify-fixed it additionally scans the patched variant to
produce fix-verification evidence.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import run, sha256_file, write_json, now_iso


def scan(appdir, outdir, tag):
    rc, ovx, err = run(["govulncheck", "-format", "openvex", "./..."], cwd=appdir, check=False)
    ovx_path = os.path.join(outdir, f"govulncheck{tag}.openvex.json")
    with open(ovx_path, "w") as f:
        f.write(ovx)
    rc, js, err = run(["govulncheck", "-format", "json", "./..."], cwd=appdir, check=False)
    json_path = os.path.join(outdir, f"govulncheck{tag}.json")
    with open(json_path, "w") as f:
        f.write(js)
    doc = json.loads(ovx)
    return doc, ovx_path, json_path


def first_trace(json_path, osv_id):
    """Extract the best call trace for an OSV id from govulncheck JSON output.

    govulncheck emits several finding messages per OSV; the first often carries
    only the module-level frame. Prefer a trace that contains function frames.
    """
    try:
        buf = open(json_path).read()
    except OSError:
        return None
    dec = json.JSONDecoder()
    idx = 0
    fallback = None
    while idx < len(buf):
        while idx < len(buf) and buf[idx] in " \r\n\t":
            idx += 1
        if idx >= len(buf):
            break
        obj, end = dec.raw_decode(buf, idx)
        idx = end
        finding = obj.get("finding") if isinstance(obj, dict) else None
        if finding and finding.get("osv") == osv_id and finding.get("trace"):
            frames = [{
                "function": fr.get("function"),
                "package": fr.get("package"),
                "module": fr.get("module"),
                "position": fr.get("position"),
            } for fr in finding["trace"]]
            if any(fr["function"] for fr in frames):
                return frames
            fallback = fallback or frames
    return fallback


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--appdir", required=True)
    ap.add_argument("--outdir", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--fixed-appdir", help="patched variant; emits fix verification")
    args = ap.parse_args()

    os.makedirs(args.outdir, exist_ok=True)
    doc, ovx_path, json_path = scan(args.appdir, args.outdir, "")

    findings = []
    for st in doc.get("statements", []):
        vuln = st.get("vulnerability", {})
        vid = vuln.get("name")
        finding = {
            "vuln_id": vid,
            "aliases": vuln.get("aliases", []),
            "status": st["status"],
            "justification": st.get("justification"),
            "impact_statement": st.get("impact_statement"),
        }
        if st["status"] == "affected":
            trace = first_trace(json_path, vid)
            if trace:
                finding["call_trace"] = trace
        findings.append(finding)

    rc, ver, _ = run(["govulncheck", "-version"], check=False)
    scanner = next((l.split(":", 1)[1].strip() for l in ver.splitlines()
                    if l.startswith("Scanner:")), ver.strip().splitlines()[0] if ver else "unknown")
    result = {
        "product": args.product,
        "generated_at": now_iso(),
        "tool": {
            "name": "govulncheck",
            "version": scanner,
            "command": "govulncheck -format openvex ./... && govulncheck -format json ./...",
        },
        "raw_outputs": {
            "openvex": {"path": ovx_path, "sha256": sha256_file(ovx_path)},
            "json": {"path": json_path, "sha256": sha256_file(json_path)},
        },
        "findings": findings,
    }

    if args.fixed_appdir:
        fdoc, fp_ovx, fp_json = scan(args.fixed_appdir, args.outdir, "-fixed")
        present = {s.get("vulnerability", {}).get("name")
                   for s in fdoc.get("statements", [])
                   if s.get("status") == "affected"}
        result["fix_verification"] = {
            "fixed_appdir": args.fixed_appdir,
            "raw_outputs": {
                "openvex": {"path": fp_ovx, "sha256": sha256_file(fp_ovx)},
                "json": {"path": fp_json, "sha256": sha256_file(fp_json)},
            },
            "vulns_still_present": sorted(v for v in present),
        }

    write_json(args.out, result)
    from collections import Counter
    c = Counter(f["status"] for f in findings)
    print(json.dumps({"product": args.product, "statuses": dict(c),
                      "total": len(findings)}, indent=2))


if __name__ == "__main__":
    main()
