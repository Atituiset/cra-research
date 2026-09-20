#!/usr/bin/env python3
"""Stage 2 — vulnerability association: SBOM PURLs -> OSV querybatch.

For Go modules the PURL (pkg:golang/...) maps 1:1 onto the OSV "Go" ecosystem.
For C/C++ there is no standardized package ecosystem in OSV: the zlib entry for
CVE-2022-37434 is a bare GIT range with no package name, so a PURL query finds
nothing. We therefore *additionally* cross-check components against the curated
vuln->function map (curation/vuln-function-map.json) and record such matches
with match_source="curation-crosscheck" — the curation step bridging the
C/C++ association gap is itself a research finding, and is logged honestly.
"""
import argparse
import json
import os
import sys
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import read_json, write_json, now_iso

OSV_QUERYBATCH = "https://api.osv.dev/v1/querybatch"
OSV_VULN = "https://api.osv.dev/v1/vulns/"


def purl_to_osv_query(purl: str):
    """Translate a Package URL into an OSV query dict, or None if unsupported."""
    if not purl.startswith("pkg:"):
        return None
    body = purl[4:]
    body, _, _version = body.partition("@") if "@" in body else (body, "", "")
    parts = body.split("/")
    ptype = parts[0]
    name = parts[-1].split("?")[0]
    version = purl.split("@", 1)[1].split("?")[0] if "@" in purl else None
    eco = {"golang": "Go", "npm": "npm", "pypi": "PyPI", "cargo": "crates.io",
           "deb": "Debian", "gem": "RubyGems", "maven": "Maven"}.get(ptype)
    if not eco or not version:
        return None
    if ptype == "golang":
        name = "/".join(p.split("?")[0] for p in parts[1:]) or name
    return {"package": {"name": name, "ecosystem": eco}, "version": version}


def osv_post(url, payload):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--sbom", required=True)
    ap.add_argument("--curation", help="curated vuln->function map for cross-check")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    sbom = read_json(args.sbom)
    components = sbom.get("components", [])

    queries, comp_of = [], []
    for c in components:
        q = purl_to_osv_query(c.get("purl", ""))
        if q:
            queries.append(q)
            comp_of.append(c)

    resp = osv_post(OSV_QUERYBATCH, {"queries": queries}) if queries else {"results": []}

    associations = []
    for comp, res in zip(comp_of, resp.get("results", [])):
        for v in res.get("vulns", []):
            associations.append({
                "vuln_id": v["id"],
                "aliases": v.get("aliases", []),
                "package_purl": comp.get("purl"),
                "package_name": comp.get("name"),
                "package_version": comp.get("version"),
                "match_source": "osv-purl-query",
            })

    # C/C++ gap: cross-check all components against curated mappings.
    curated = []
    if args.curation:
        cur = read_json(args.curation)
        for m in cur.get("mappings", []):
            for c in components:
                if c.get("name", "").lower() == m["package"].lower():
                    req = urllib.request.Request(OSV_VULN + m["vuln_id"])
                    with urllib.request.urlopen(req, timeout=60) as r:
                        detail = json.load(r)
                    associations.append({
                        "vuln_id": m["vuln_id"],
                        "aliases": detail.get("aliases", []),
                        "package_purl": c.get("purl"),
                        "package_name": c.get("name"),
                        "package_version": c.get("version"),
                        "match_source": "curation-crosscheck",
                        "note": "OSV has no package-ecosystem entry for this C library "
                                "(bare GIT range); matched via curated mapping. See curation/README.md.",
                    })
                    curated.append(m["vuln_id"])

    result = {
        "product": args.product,
        "generated_at": now_iso(),
        "osv_api": OSV_QUERYBATCH,
        "purls_queried": len(queries),
        "associations": associations,
    }
    write_json(args.out, result)
    print(json.dumps({
        "product": args.product,
        "purls_queried": len(queries),
        "associations": len(associations),
        "via_curation": len(curated),
    }, indent=2))


if __name__ == "__main__":
    main()
