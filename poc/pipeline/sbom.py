#!/usr/bin/env python3
"""Stage 1 — artifact extraction: syft -> CycloneDX SBOM + artifact sha256.

We do NOT build our own SBOM tooling (commoditized per research conclusions);
we shell out to syft and post-process the CycloneDX JSON:
  * stamp the product artifact (binary) sha256 into metadata
  * optionally merge an augmentation fragment (C/C++ vendored deps that syft's
    binary classifier cannot see — see sbom-augment.cdx.json)
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from util import run, sha256_file, write_json, now_iso


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--product", required=True)
    ap.add_argument("--version", required=True)
    ap.add_argument("--scan", required=True, help="dir or binary for syft to scan")
    ap.add_argument("--artifact", required=True, help="product binary (hashed + registered)")
    ap.add_argument("--augment", help="CycloneDX fragment whose components get merged in")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    artifact_sha = sha256_file(args.artifact)
    rc, out, err = run(["syft", args.scan, "-o", "cyclonedx-json"], check=True)
    sbom = json.loads(out)

    components = sbom.get("components", [])
    if args.augment:
        with open(args.augment) as f:
            frag = json.load(f)
        existing = {c.get("purl") for c in components}
        for c in frag.get("components", []):
            if c.get("purl") not in existing:
                components.append(c)
        sbom["components"] = components

    sbom.setdefault("metadata", {}).setdefault("properties", []).extend([
        {"name": "cra-research:product", "value": args.product},
        {"name": "cra-research:product-version", "value": args.version},
        {"name": "cra-research:artifact-sha256", "value": artifact_sha},
        {"name": "cra-research:artifact-path", "value": os.path.abspath(args.artifact)},
        {"name": "cra-research:extracted-at", "value": now_iso()},
    ])
    write_json(args.out, sbom)

    purls = sorted({c.get("purl") for c in components if c.get("purl")})
    print(json.dumps({
        "product": args.product,
        "artifact_sha256": artifact_sha,
        "sbom": args.out,
        "components": len(components),
        "purls": len(purls),
    }, indent=2))


if __name__ == "__main__":
    main()
