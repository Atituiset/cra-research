# Traceability report — c-vuln-app 0.1.0

- exported_at: 2026-09-18T16:53:56Z
- product artifact: `c-vuln-app` sha256:`4332f06c17d5ef7e97061a8b0433331ad74ddd5d6474f89fd6fbe0f5d7ba82d7`
- signer: `a57a061281f93b3a264fed8cf655523c0c3e7a087078e30224afa2cf19e00ff0` (dev key, keys/dev-ed25519.pub.json)
- conclusions: 2

Each section: conclusion → evidence → tool → artifact hash → timestamp → signer.

## reachability: CVE-2022-37434 — **affected**

- conclusion_id: `287da101-b2bc-4382-956c-e970b1394b74`
- justification: `—`
- attestation: `attestations/reachability-CVE-2022-37434-742cc0c764ac.json` sha256:`742cc0c764acd50123fbaaffc5fc212043dff66e53202f21710c4d3a9ccf8ac7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `c-vuln-app-0.1.0` sha256:`4332f06c17d5ef7e97061a8b0433331ad74ddd5d6474f89fd6fbe0f5d7ba82d7`
- tool: `joern` — docker ghcr.io/joernio/joern:nightly
  - command: `docker run ... joern-parse --language newc --output /out/cpg.bin /src; docker run ... joern --script callpath.sc --param cpgFile=/out/cpg.bin`
- timestamp: 2026-09-18T16:53:56Z
- evidence:
  - `tool-output:cpg_dump` `/home/atituiset/Projects/cra-research/poc/out/c-vuln-app/joern-cpg-dump.tsv` sha256:`9e21b9703ee64251a2c6af1a68f956185cf8f4638b7dbdf908331ca3e6ec99fa`
  - call-path (len 3): `main -> gunzip_file -> inflate`
    - `main` (main.c:37)
    - `gunzip_file` (main.c:19) called at main.c:58
    - `inflate` (third_party/zlib/inflate.c:623) called at main.c:32

## vex: CVE-2022-37434 — **affected**

- conclusion_id: `0ea8e733-0f47-40d0-9c67-056b206dedf2`
- justification: `—`
- attestation: `attestations/vex-CVE-2022-37434-f12214f90130.json` sha256:`f12214f901304f549234ca3def260fc024ffb12248539e5015fb221831344884`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `c-vuln-app-0.1.0` sha256:`4332f06c17d5ef7e97061a8b0433331ad74ddd5d6474f89fd6fbe0f5d7ba82d7`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product c-vuln-app --version 0.1.0 --artifact examples/c-vuln-app/build/c-vuln-app --sbom out/c-vuln-app/sbom.cdx.json --associations out/c-vuln-app/associations.json --reachability out/c-vuln-app/reachability.json --vex out/c-vuln-app/vex.openvex.json --keys keys --outdir out/c-vuln-app`
- timestamp: 2026-09-18T16:53:56Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/c-vuln-app/vex.openvex.json` sha256:`56a1d21cee9149eb52f3a0df6726b33d46cf6a8269ac2603a278799d16044a17`
