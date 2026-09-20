#!/usr/bin/env bash
# One-shot end-to-end run of the CRA PoC pipeline.
# Stages: build -> SBOM -> OSV association -> reachability -> VEX -> attest -> export.
set -euo pipefail
cd "$(dirname "$0")/.."
POC=$PWD
PY=${PYTHON:-python3}
export PATH="$PATH:$HOME/bin:$HOME/go/bin"

GO_APP=examples/go-vuln-app
GO_FIXED=examples/go-vuln-app-fixed
C_APP=examples/c-vuln-app
GO_VER=0.1.0
C_VER=0.1.0

echo "==> 0/7 keys + store"
$PY pipeline/gen_keys.py
$PY pipeline/store.py

echo "==> 1/7 build products"
(cd $GO_APP && go build -o go-vuln-app .)
(cd $C_APP && python3 gen_sample.py && cmake -S . -B build -DCMAKE_BUILD_TYPE=Release >/dev/null && cmake --build build -j >/dev/null)

echo "==> 2/7 SBOM (syft)"
$PY pipeline/sbom.py --product go-vuln-app --version $GO_VER \
  --scan $GO_APP --artifact $GO_APP/go-vuln-app \
  --out out/go-vuln-app/sbom.cdx.json
$PY pipeline/sbom.py --product c-vuln-app --version $C_VER \
  --scan $C_APP --artifact $C_APP/build/c-vuln-app \
  --augment $C_APP/sbom-augment.cdx.json \
  --out out/c-vuln-app/sbom.cdx.json

echo "==> 3/7 associate (OSV)"
$PY pipeline/associate.py --product go-vuln-app \
  --sbom out/go-vuln-app/sbom.cdx.json --out out/go-vuln-app/associations.json
$PY pipeline/associate.py --product c-vuln-app \
  --sbom out/c-vuln-app/sbom.cdx.json --curation curation/vuln-function-map.json \
  --out out/c-vuln-app/associations.json

echo "==> 4/7 reachability"
$PY pipeline/reach_go.py --product go-vuln-app --appdir $GO_APP \
  --fixed-appdir $GO_FIXED \
  --outdir out/go-vuln-app --out out/go-vuln-app/reachability.json
$PY pipeline/reach_c.py --product c-vuln-app --appdir $C_APP \
  --curation curation/vuln-function-map.json \
  --outdir out/c-vuln-app --out out/c-vuln-app/reachability.json

echo "==> 5/7 VEX"
$PY pipeline/vex.py --product go-vuln-app --version $GO_VER \
  --sbom out/go-vuln-app/sbom.cdx.json \
  --associations out/go-vuln-app/associations.json \
  --reachability out/go-vuln-app/reachability.json \
  --out out/go-vuln-app/vex.openvex.json
$PY pipeline/vex.py --product c-vuln-app --version $C_VER \
  --sbom out/c-vuln-app/sbom.cdx.json \
  --associations out/c-vuln-app/associations.json \
  --reachability out/c-vuln-app/reachability.json \
  --out out/c-vuln-app/vex.openvex.json

echo "==> 6/7 attest + store"
$PY pipeline/attest.py --product go-vuln-app --version $GO_VER \
  --artifact $GO_APP/go-vuln-app \
  --sbom out/go-vuln-app/sbom.cdx.json \
  --associations out/go-vuln-app/associations.json \
  --reachability out/go-vuln-app/reachability.json \
  --vex out/go-vuln-app/vex.openvex.json \
  --keys keys --outdir out/go-vuln-app
$PY pipeline/attest.py --product c-vuln-app --version $C_VER \
  --artifact $C_APP/build/c-vuln-app \
  --sbom out/c-vuln-app/sbom.cdx.json \
  --associations out/c-vuln-app/associations.json \
  --reachability out/c-vuln-app/reachability.json \
  --vex out/c-vuln-app/vex.openvex.json \
  --keys keys --outdir out/c-vuln-app

echo "==> 7/7 back-fill attestation refs into VEX + export evidence packs"
$PY pipeline/vex.py --product go-vuln-app --version $GO_VER \
  --sbom out/go-vuln-app/sbom.cdx.json \
  --associations out/go-vuln-app/associations.json \
  --reachability out/go-vuln-app/reachability.json \
  --attestation-map out/go-vuln-app/attestation-map.json \
  --out out/go-vuln-app/vex.openvex.json
$PY pipeline/vex.py --product c-vuln-app --version $C_VER \
  --sbom out/c-vuln-app/sbom.cdx.json \
  --associations out/c-vuln-app/associations.json \
  --reachability out/c-vuln-app/reachability.json \
  --attestation-map out/c-vuln-app/attestation-map.json \
  --out out/c-vuln-app/vex.openvex.json
$PY pipeline/export.py --product go-vuln-app --version $GO_VER \
  --sbom out/go-vuln-app/sbom.cdx.json --vex out/go-vuln-app/vex.openvex.json \
  --keys keys --outroot out
$PY pipeline/export.py --product c-vuln-app --version $C_VER \
  --sbom out/c-vuln-app/sbom.cdx.json --vex out/c-vuln-app/vex.openvex.json \
  --keys keys --outroot out

echo "==> store stats"
$PY pipeline/store.py --stats
echo "DONE. Evidence packs under out/evidence-pack-*/"
