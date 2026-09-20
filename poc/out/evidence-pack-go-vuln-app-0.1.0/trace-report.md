# Traceability report — go-vuln-app 0.1.0

- exported_at: 2026-09-18T16:53:56Z
- product artifact: `go-vuln-app` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- signer: `a57a061281f93b3a264fed8cf655523c0c3e7a087078e30224afa2cf19e00ff0` (dev key, keys/dev-ed25519.pub.json)
- conclusions: 152

Each section: conclusion → evidence → tool → artifact hash → timestamp → signer.

## reachability: GO-2023-2402 — **affected**

- conclusion_id: `b3ef9f33-82de-489b-a5eb-ad6b39195bf0`
- justification: `—`
- attestation: `attestations/reachability-GO-2023-2402-216d8e946c36.json` sha256:`216d8e946c3610a7fe87cfae00f9b5fee1e86780e57cb50255127caf89a8d100`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2024-2687 — **not_affected**

- conclusion_id: `1186445c-794c-4a5f-93e6-3720aab40892`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2024-2687-7715737404be.json` sha256:`7715737404bea95d3c831d4b6cb7a189b218665a53d2b61bacc9b37d68a60aeb`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2024-3321 — **not_affected**

- conclusion_id: `7dab835d-f67e-4bfa-91f8-095b6887388a`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2024-3321-ee1d19766b60.json` sha256:`ee1d19766b60342b6b64cf7d37f191abaa6ba5328e0f32d7d92053b6c536847d`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2024-3333 — **not_affected**

- conclusion_id: `43871ce2-ac8e-4803-8764-00cd8b9c76e0`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2024-3333-820c5321d777.json` sha256:`820c5321d7774bf3f3c5466e24b4336f35fcb0d2b3e53533a4e7737a4f517cef`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2025-3487 — **affected**

- conclusion_id: `843be6ed-b62a-4651-9a68-db358211aa67`
- justification: `—`
- attestation: `attestations/reachability-GO-2025-3487-c40fdd7a952f.json` sha256:`c40fdd7a952f6b2bae84bd21d2f6159a46dd7b33cf3318024967576537661d4d`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2025-3503 — **not_affected**

- conclusion_id: `65766adb-c978-4a63-ae39-a40d2a28fc71`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2025-3503-6f34e5b2ad01.json` sha256:`6f34e5b2ad01fd14e5c72179456fc6208f4d2639fb65362e667ee1c108421398`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2025-3595 — **not_affected**

- conclusion_id: `85856858-90e5-4c5f-9b1a-28fdf74f094c`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2025-3595-8e8324c907d1.json` sha256:`8e8324c907d19667135e13bd409ebe55729f0bb8d81fc532f61b92d4c8726cd2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2025-4116 — **not_affected**

- conclusion_id: `beceb76f-a4e2-4dde-8e04-c7f2591f0ae5`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2025-4116-8abbfaf3d05b.json` sha256:`8abbfaf3d05be3ce8bbd0855c7404d7b4b3268f1fe200b10fed84423cec957ed`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2025-4134 — **not_affected**

- conclusion_id: `bb4cef23-4fff-489a-bcfe-d64dcee355ab`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2025-4134-81d282e92d8f.json` sha256:`81d282e92d8f422b9f1db76465a1b4910626f91f491bdadb0a422aa0584461fb`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2025-4135 — **not_affected**

- conclusion_id: `e516429e-90ff-4e19-a0a7-e2721fbb0d87`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2025-4135-82f236974ecf.json` sha256:`82f236974ecf5c61bd621e999e7bfd3200e52a5f9546a8e833eb2a05e660fe3f`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4440 — **not_affected**

- conclusion_id: `4dbce262-20e0-4a73-ab7b-30989fa17a01`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4440-3e64376f2c1d.json` sha256:`3e64376f2c1db6a71238a19cf30e305caf60f203ed64afb665e662402f2c0293`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4441 — **not_affected**

- conclusion_id: `df07480b-e70f-4114-9c3b-962c2ed13235`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4441-6613ac4fee58.json` sha256:`6613ac4fee586ea5bb0532dc2c77aa824a5ef1aef2a81dfeba68f5ad9393f7e9`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4864 — **not_affected**

- conclusion_id: `f7c8031e-17dc-4e62-b6c7-d91a406ed57a`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-4864-f8f4585afaeb.json` sha256:`f8f4585afaebadc08cbd3e584a238b88ac89059c478aa1eb86d471960e06aa1b`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4865 — **not_affected**

- conclusion_id: `0f349f52-ea9a-4ad9-a4eb-1ba7bab03e8a`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4865-a4b1080b8e65.json` sha256:`a4b1080b8e656bbc7a81c21143e6b721c413dce0475077e1f05374f1e508859b`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4866 — **not_affected**

- conclusion_id: `68d2c90a-bf74-4719-90d4-35f3335179a1`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-4866-44a16279abb5.json` sha256:`44a16279abb5acea34b3cd1f058a0cca14f501d2f9944f4310ff6a4974d9c224`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4869 — **not_affected**

- conclusion_id: `7c7f3028-0a28-4d2b-857a-1734ec62eb8d`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4869-9f1c57278a94.json` sha256:`9f1c57278a9434fb78b15173824dd7d908054793609aa2c0724428da712d4ac8`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4870 — **not_affected**

- conclusion_id: `f4f80e27-cf0d-44cc-881d-ab7e9f2abeea`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4870-9d45d63f67f2.json` sha256:`9d45d63f67f27a92d3936bde42588be864235810ef736b3e2d17f17d44267fea`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4918 — **not_affected**

- conclusion_id: `03a02c64-979a-418e-99cd-c2d50e0a1c14`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4918-5bb8c51249cf.json` sha256:`5bb8c51249cf5871858f6ba43585ede98a3edae8814c41f0d8729854223e2fbd`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4946 — **not_affected**

- conclusion_id: `216e928f-c944-426b-b8d5-233b7da4757b`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-4946-d147b9441d21.json` sha256:`d147b9441d219fccc6cb082c545eb9eb73f8f0939bb78ac335380f049072da0c`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4947 — **not_affected**

- conclusion_id: `00e5ef7a-0928-40c9-990c-843903d44c0b`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-4947-f87d8b71492c.json` sha256:`f87d8b71492c083eeae060d1bd629b9699717ce6d2a0bb2bb7b83f9480da40d8`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4970 — **not_affected**

- conclusion_id: `62672a75-62a8-4024-9cb7-7041c9868633`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-4970-d33330d91834.json` sha256:`d33330d91834a8e0d61f00ea306078810359a2d297d64a76a7e88375969e469f`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4971 — **affected**

- conclusion_id: `d0c8e182-4c73-4bdb-bd4d-b4fc03c7cee7`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-4971-e4d6a4e9070a.json` sha256:`e4d6a4e9070a91604c49befad148563de9941693e1ff76675369f4cdefb0c7ff`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `DialTimeout` (net)
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-4976 — **not_affected**

- conclusion_id: `6c2c08e2-068b-4769-a1a7-4550dbd73986`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4976-744d15b2a775.json` sha256:`744d15b2a775eefc9f892e4e05abcdc3b957957a334e8ead5f3b790d81fc6a56`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4977 — **not_affected**

- conclusion_id: `b6d69e01-814b-40ee-920b-6d2e23767880`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4977-2a19d055f095.json` sha256:`2a19d055f095b4b1e5b75bc99e20529dd0128cced555c228977526eb0ab3c743`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4980 — **not_affected**

- conclusion_id: `26cbabfd-c28e-4a04-a788-532ba1ac78db`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4980-680a4b242cf8.json` sha256:`680a4b242cf85dcaee2b67bdb9f32f998ee23cfc0e294a3f3585cb2529c10346`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4981 — **not_affected**

- conclusion_id: `dede0b44-43fe-43e0-b791-f315dfc040af`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-4981-5d7bf3f93843.json` sha256:`5d7bf3f93843e6ab05377d8f934cf56e944e336acbe352eab823651e330c3397`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4982 — **not_affected**

- conclusion_id: `d527bba1-6e33-4718-8433-2cc2ea3c7f3f`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4982-8d53e9dc9087.json` sha256:`8d53e9dc908714292ae1315807308d68d7957a04817cbb43a761b6420a45f43b`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-4986 — **not_affected**

- conclusion_id: `873ff1c5-5654-4c33-91c0-50bd8fb04638`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-4986-e38d81356468.json` sha256:`e38d81356468cc0ecad5ea9698d5bda2917f54d78c9dfeb7a9dcf506b3da670a`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5005 — **not_affected**

- conclusion_id: `3159d91d-3f8b-43c2-bcbf-a08aaba0758d`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5005-9ea0385bd7cb.json` sha256:`9ea0385bd7cb96a8e02ec3f8b622bb9865ced99970bb962152682989af08f9f3`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5006 — **not_affected**

- conclusion_id: `f9ab1e11-e079-435c-9fba-cbcd4fc71452`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5006-b10284782632.json` sha256:`b10284782632539554c43dae9ec0a9bcf5a4c7f6fd47203bcfc22e7fe18519b5`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5013 — **affected**

- conclusion_id: `ef2b3dcd-a199-4588-bcb4-74ea22fd3c10`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5013-02b4538e9977.json` sha256:`02b4538e99777a1c5b045dc75b76c636d2fea70cace99fb20dff70c66c2b0782`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5014 — **not_affected**

- conclusion_id: `5efb03b6-f06e-43dd-81f7-94ef1e217732`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5014-94d59a6809fc.json` sha256:`94d59a6809fc0f43387698fd63fdc984b63048775abaadfd9316e90001023939`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5015 — **not_affected**

- conclusion_id: `32d59263-ea98-4ce5-bf11-78f44d2cbdc0`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5015-53e1ffb04824.json` sha256:`53e1ffb04824588f632fc1e2df7a1180e5ce7df3f83ede58641236d2ca755bcc`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5016 — **not_affected**

- conclusion_id: `1c68b56d-85f1-4f07-9896-142771ecb3ee`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5016-af95ad9a2ece.json` sha256:`af95ad9a2ece351a57c09f2ff4bba0b24d38d830db0683a46c10990d49b0e180`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5017 — **affected**

- conclusion_id: `1919536c-f7bc-40c7-a170-507de7843a97`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5017-6d26c4bd9f62.json` sha256:`6d26c4bd9f623f81258f0f404fe8500cdf61303c3e1209389f83d6779d8d855a`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5018 — **affected**

- conclusion_id: `4491b81d-181c-4f97-9bd5-fe55aefdd591`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5018-e6d6e593ef39.json` sha256:`e6d6e593ef39de9a311d4bd3bead3dfd095a9fc49c0077c93a9043f22b87507d`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5019 — **affected**

- conclusion_id: `f546af1b-2214-471c-af0e-02eff5baf5e2`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5019-a57e27fbdfc9.json` sha256:`a57e27fbdfc9d203b98f13afdf9051a1ce7ae7b043511ae240796cab4f4ddce0`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5020 — **affected**

- conclusion_id: `65e46589-e940-4a62-a25b-337b47cad59d`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5020-92521ea87517.json` sha256:`92521ea87517d47cf42604e6ed2ad6c689ac36d786a7438d6985007ebb52f348`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5021 — **not_affected**

- conclusion_id: `b630da6f-fa59-4d1f-b216-46b915aeb9c6`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5021-f9121e81cd60.json` sha256:`f9121e81cd6042379a609a79b2fa5ca9a511668912afae244d22fe281e380249`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5023 — **not_affected**

- conclusion_id: `7b3e1c82-2006-48bc-97f3-eb1e2704e0c7`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5023-328bad3bfc57.json` sha256:`328bad3bfc57582e1e576c442643e2960b80ca8847a4e4d2060fea237c3b1918`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5025 — **not_affected**

- conclusion_id: `91f7ae10-8050-47e8-893b-5e1e51f2d7a4`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5025-15cd8232945e.json` sha256:`15cd8232945ee277e77bf70b45868071f3ccad34d7fc2a7f74fb700f1be52549`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5026 — **affected**

- conclusion_id: `c1aae4dc-6eb3-47af-90be-bc184975c2f0`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5026-e6452ac2c5f9.json` sha256:`e6452ac2c5f98f6e58b73c158a5176f9ba6c06d930370a7573dcfcb6eea9f446`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `ToASCII` (golang.org/x/net/idna)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5027 — **not_affected**

- conclusion_id: `61c3122c-94ba-4edb-b860-3093fa8e7b15`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5027-956185052fb8.json` sha256:`956185052fb860195e647588497fa843db642063b96f14c8695163c878c94176`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5028 — **not_affected**

- conclusion_id: `5a4cba94-ec86-4b65-af1f-7603387239aa`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5028-040fd9d2b126.json` sha256:`040fd9d2b12630f57a1fa157a0726bd95603c71c872c0c4e74b495f2ca0b6c74`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5029 — **not_affected**

- conclusion_id: `78f3013f-be5d-4702-8a1d-b5f7faf5eba4`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5029-e5ebcb14dd11.json` sha256:`e5ebcb14dd11df5949210bc946314c62d95d009279aa76de70abd43bea525545`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5030 — **not_affected**

- conclusion_id: `4bdf3d36-0c3a-4375-8d40-90a046111233`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5030-344b5bd56e06.json` sha256:`344b5bd56e0648fccaed76c8c676e20e86e3a7c517c4d1081dfe43b438efd11f`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5033 — **not_affected**

- conclusion_id: `4d495907-45be-4e8d-92b1-b75de055e19e`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5033-e50ac5f35266.json` sha256:`e50ac5f35266e4d0a833c3c8a20010a6fface442d990cfd2a2cd47969a9e27ae`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5037 — **not_affected**

- conclusion_id: `98de370c-cfaf-46dd-ad7f-61ec1efd6a92`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5037-15ebdab878b0.json` sha256:`15ebdab878b02f6f609a9c2a573e6a80301052a4210034ff329cc525aeeb9445`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5038 — **not_affected**

- conclusion_id: `4457c0ba-8c64-499f-a2e4-9492ba0beae6`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5038-eb6b9a58e324.json` sha256:`eb6b9a58e3246ed0c1197e78f484614928c83b15b23091bdfde7d605ef811b00`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5039 — **not_affected**

- conclusion_id: `8534a89b-6e72-4c90-a293-5275ec669a73`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5039-d30b57c796d9.json` sha256:`d30b57c796d95da6889923c3581a59b88d411bcd37690974be7317ce09877c60`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5856 — **not_affected**

- conclusion_id: `a117a258-6f3a-499c-a491-385db5035ea9`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5856-3fd9eb7ee7aa.json` sha256:`3fd9eb7ee7aa015143d2936a14899270253a14719f47d164fe7cdd898394c197`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5932 — **not_affected**

- conclusion_id: `b6197330-5ee2-4672-8cf5-9298ba7c77d9`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-5932-da441aa50beb.json` sha256:`da441aa50beba92907d2b469ab948a973f507aafa87a8f9bcca9ee6055b92114`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5942 — **not_affected**

- conclusion_id: `c34aadc0-ed3c-4e01-965d-baeceaae85f0`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5942-e3b147680981.json` sha256:`e3b1476809819ff425182a0c69735e1d7b68ab6c0665390607f4a833b651a7d0`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-5970 — **affected**

- conclusion_id: `0fe8a7f7-c2ce-4d1e-8fa2-c68ef0782ce2`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-5970-82be537a7658.json` sha256:`82be537a765888b814fccd00393f8dab15ef5536dcaf81ec00b7a5f30c5dccdb`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `IsNormalString` (golang.org/x/text/unicode/norm)
  - trace: `validateRegistration` (golang.org/x/net/idna)
  - trace: `process` (golang.org/x/net/idna)
  - trace: `ToASCII` (golang.org/x/net/idna)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-5972 — **not_affected**

- conclusion_id: `cb7b8056-f7ab-46a6-b8ca-7c72058b8451`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-5972-7870449eb984.json` sha256:`7870449eb9840e0d73577be3a0a20d85a037273b4cf94ad69d245918c8e77d75`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6088 — **not_affected**

- conclusion_id: `388e959f-ea6a-4253-8ca3-e3152adf024f`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-6088-bab42719f70b.json` sha256:`bab42719f70b7149da345eacb858be572379154fdccc75b84143dc575f8874c7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6089 — **not_affected**

- conclusion_id: `f1ae9984-6500-4c78-bc31-6632408145c0`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-6089-0d04f2ec08ad.json` sha256:`0d04f2ec08adb3a71ce5f0227d54b7d0d04b7a11951cb739abe99535be01c519`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6090 — **not_affected**

- conclusion_id: `e7e54b3b-dc7c-4fd4-a2d8-1f3e88cda06d`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-6090-e413cfffcded.json` sha256:`e413cfffcded61108ec01a70981a8d3f9613cc63364b7dbb0b2008e74a040f2d`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6091 — **not_affected**

- conclusion_id: `8d9c6f3c-a1c9-4adf-85be-183f8fa3227a`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/reachability-GO-2026-6091-5a1246ead061.json` sha256:`5a1246ead061633c721adab8b19fd703cc7bb12d5503fd0d0b3ab6990af028d8`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6218 — **not_affected**

- conclusion_id: `1ca1f206-9184-4343-bc37-660a93e95be7`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-6218-f1e77e4dd874.json` sha256:`f1e77e4dd874a88430d8e13389199d7fc363649a411ce65af8cba07de9d2f994`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6303 — **not_affected**

- conclusion_id: `2f7a9ea0-8686-4e77-8c4d-ffb2487ba1fd`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/reachability-GO-2026-6303-02e5b738b3ba.json` sha256:`02e5b738b3ba0c1b074767ad3588579988c81323add51cdeabf83d34409b4626`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`

## reachability: GO-2026-6354 — **affected**

- conclusion_id: `2ec70c5e-390d-44b7-b0e1-bf02d66101b0`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-6354-f6e044be84f1.json` sha256:`f6e044be84f174c489cacd61a65af024c3a7f70251a2f3ca8f74a4e23dd634fd`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## reachability: GO-2026-6355 — **affected**

- conclusion_id: `2d4dc044-efef-46b5-8671-74c545d47b06`
- justification: `—`
- attestation: `attestations/reachability-GO-2026-6355-ada8a34f9433.json` sha256:`ada8a34f9433d5f37feda2f286b80ce56edc9efb455b71b44ae42472c0f5fff2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:json` `out/go-vuln-app/govulncheck.json` sha256:`598bf24f6ecd130cc7c33f80cb5b13323a365a958093ebfd6fe0f8bdf6e14cd3`
  - `tool-output:openvex` `out/go-vuln-app/govulncheck.openvex.json` sha256:`fd7b676ef51a3b2b5a980d331e0ba2020d51e74de1a0036c7b97953aba65b556`
  - trace: `Dial` (golang.org/x/crypto/ssh)
  - trace: `connectSSH` (cra-research.dev/poc/go-vuln-app)
  - trace: `main` (cra-research.dev/poc/go-vuln-app)

## verification: GO-2023-2402 — **fixed**

- conclusion_id: `75abc5c5-c261-42eb-b66e-bb01f4da483e`
- justification: `—`
- attestation: `attestations/verification-GO-2023-2402-8fa8f6bba2da.json` sha256:`8fa8f6bba2da567bbbfad01c7e40b6e876839cb47122116c1e092ae9330d2c86`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2025-3487 — **fixed**

- conclusion_id: `572913ba-ca12-4763-aea6-ba4d00ea9312`
- justification: `—`
- attestation: `attestations/verification-GO-2025-3487-e2eb58ea7707.json` sha256:`e2eb58ea77070778ce9eee39782b54be2e0f3ea733580f306870df175673ea25`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-4971 — **still_present**

- conclusion_id: `050fac08-f56e-4dda-b3b9-a86fe9f68c61`
- justification: `vulnerable_code_present`
- attestation: `attestations/verification-GO-2026-4971-b655fa5f5a37.json` sha256:`b655fa5f5a3726a63f066a52c0cbff9d7d8df0bcb1f718b025b33ea02685e743`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5013 — **fixed**

- conclusion_id: `f018f12b-7f51-4c49-9c0a-e53898580465`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5013-61af13391c16.json` sha256:`61af13391c168393b69f309f9a231d8f3b5bd52d463ac2e959ce90d91d941e7b`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5017 — **fixed**

- conclusion_id: `32198bb6-609c-4fe8-979c-80b6e462ce30`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5017-7df9a02f59ab.json` sha256:`7df9a02f59ab1789f3a41d94eaae724135e222b46a3a22f684b6f4e2be390404`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5018 — **fixed**

- conclusion_id: `154fbc23-e3ba-4a65-9758-f6994ffea322`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5018-5210510116b2.json` sha256:`5210510116b2544f708027178428a4818ff709ed3a4ea1ccef6bd3355d59da26`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5019 — **fixed**

- conclusion_id: `20784408-5af2-4ee9-918e-d2994375ceb1`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5019-825793c8bfc6.json` sha256:`825793c8bfc64f92b38bfdf1f88b44c543b65107f9c431404976304767a18136`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5020 — **fixed**

- conclusion_id: `05a227c1-9006-4b38-b220-67deef3fe33d`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5020-d23596766488.json` sha256:`d23596766488254820f981f60b31503e6ed1751068d0788d1657e521a384bbcf`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5026 — **fixed**

- conclusion_id: `7ab44468-8ab5-4c4c-9d15-f048745a284f`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5026-a04651633d1b.json` sha256:`a04651633d1b4996bc0c26fb837bf5362e4d2ef1289fcd5b6e7ace5de8405afa`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-5970 — **fixed**

- conclusion_id: `7bb2f558-6e51-43ae-8678-3ef8961a5d1a`
- justification: `—`
- attestation: `attestations/verification-GO-2026-5970-2b2f75077a0d.json` sha256:`2b2f75077a0d6afb9c76b5dc05e5d6c1d1c9e6d29c8ba08a691b352e68912c71`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-6354 — **fixed**

- conclusion_id: `95a6e120-181e-464f-a58c-08f289c5ca0d`
- justification: `—`
- attestation: `attestations/verification-GO-2026-6354-63339b6db395.json` sha256:`63339b6db39593477f413b30083c6a91f30cf293c0c68f94d60438cc1369f860`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## verification: GO-2026-6355 — **fixed**

- conclusion_id: `cbebe032-1808-4bb6-aab8-df7022ddb53f`
- justification: `—`
- attestation: `attestations/verification-GO-2026-6355-5da2f9a8f0f2.json` sha256:`5da2f9a8f0f2e6119ea6fa6baac891c2fa69a1607394932176ac09eddb286ea1`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `govulncheck` — govulncheck@v1.8.0
  - command: `govulncheck -format openvex ./... && govulncheck -format json ./...`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:fixed-openvex` `out/go-vuln-app/govulncheck-fixed.openvex.json` sha256:`ce7df23ea07aab2afad3ce755c4d15866a80639c55e5026fd61b228638efb133`

## vex: GHSA-45gg-vh54-h5m9 — **under_investigation**

- conclusion_id: `cddeb89d-4696-4349-bf45-e5304ec66ad5`
- justification: `—`
- attestation: `attestations/vex-GHSA-45gg-vh54-h5m9-6d65bcdbb1e9.json` sha256:`6d65bcdbb1e946fc313f19f8f1133911011f52f0562fcb80f76b97d25f7a77d2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-5cv4-jp36-h3mw — **under_investigation**

- conclusion_id: `19589882-901e-4171-8468-6a38e10bd424`
- justification: `—`
- attestation: `attestations/vex-GHSA-5cv4-jp36-h3mw-64b6f99e2623.json` sha256:`64b6f99e2623146442326d754281623511a12895c583f699feb72a16bc797434`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-78mq-xcr3-xm33 — **under_investigation**

- conclusion_id: `9f9fc48a-60f3-4fc6-a665-3d31d4b420dd`
- justification: `—`
- attestation: `attestations/vex-GHSA-78mq-xcr3-xm33-3227899ff539.json` sha256:`3227899ff53912d6acbf6e0c1eea9b3880146e5828b4639d6c916182ef992ea2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-89gr-r52h-f8rx — **under_investigation**

- conclusion_id: `3dcc9ce2-022e-48e5-b889-7d0cfbfff8fe`
- justification: `—`
- attestation: `attestations/vex-GHSA-89gr-r52h-f8rx-1a2d1415ef2f.json` sha256:`1a2d1415ef2f16546d5ccf773037706cce2bd5319d5b85f00f30a9e442d86de7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-9m57-25v3-79x9 — **under_investigation**

- conclusion_id: `ef075b90-3f5d-4d0a-8a55-7ad6ae359055`
- justification: `—`
- attestation: `attestations/vex-GHSA-9m57-25v3-79x9-8e5170a6ccbb.json` sha256:`8e5170a6ccbb1e9a631c7dde194643dbb6bc995095d260af0585998334e1e30d`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-hcg3-q754-cr77 — **under_investigation**

- conclusion_id: `1c48b6fd-502a-400e-ab19-b3f166716b1c`
- justification: `—`
- attestation: `attestations/vex-GHSA-hcg3-q754-cr77-6104425a5842.json` sha256:`6104425a584214b24cd056fbaf44080e03f88aba7950921acecbe8db40e645af`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-q4h4-gmj2-qvw2 — **under_investigation**

- conclusion_id: `d145a40e-346e-4ddb-8aa1-573fbe5706b6`
- justification: `—`
- attestation: `attestations/vex-GHSA-q4h4-gmj2-qvw2-2e25d882bb0f.json` sha256:`2e25d882bb0fa0258859ad58843b491c460f00eaffeea0052089d7d3ec34a21e`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-qpw4-5x99-6vjp — **under_investigation**

- conclusion_id: `beeb648c-83e6-427d-8474-f74a69ba5773`
- justification: `—`
- attestation: `attestations/vex-GHSA-qpw4-5x99-6vjp-afcae6c4877c.json` sha256:`afcae6c4877c4a6755209bb445f7b2c6c359ac585ad51cc60cf086203dbe17fe`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-rm3j-f69w-wqmq — **under_investigation**

- conclusion_id: `3c93596f-cbc4-4b6d-acc6-45f8bf5bef32`
- justification: `—`
- attestation: `attestations/vex-GHSA-rm3j-f69w-wqmq-fb4ed10cfef7.json` sha256:`fb4ed10cfef722b0085266803c0e6c982350536a98c3605dcd892062cdefbf0f`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-vgwf-h737-ff37 — **under_investigation**

- conclusion_id: `e4d4d1eb-8b41-479b-bae5-001305f2bea1`
- justification: `—`
- attestation: `attestations/vex-GHSA-vgwf-h737-ff37-9825a9042842.json` sha256:`9825a9042842ab28e7880dbc91433a66aa15c6163eb2fcc441c4f04845e14c3b`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-vvgc-356p-c3xw — **under_investigation**

- conclusion_id: `364d55f5-aba6-4083-acd5-df93cc45ad35`
- justification: `—`
- attestation: `attestations/vex-GHSA-vvgc-356p-c3xw-9a53cc173cba.json` sha256:`9a53cc173cba70b1493b7debaf874aa240586feeb9a2dc5ecc00a83030be12bd`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-w879-237q-wc7r — **under_investigation**

- conclusion_id: `e92dc144-f330-4181-8f5d-253cd5e4d058`
- justification: `—`
- attestation: `attestations/vex-GHSA-w879-237q-wc7r-676cbaf2862d.json` sha256:`676cbaf2862d8fccf2ac0e293b07e67ec53309a86673bbb7731699e55668e35c`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GHSA-x527-x647-q7gg — **under_investigation**

- conclusion_id: `273297a5-094b-4b5b-8943-a1d7495c4187`
- justification: `—`
- attestation: `attestations/vex-GHSA-x527-x647-q7gg-a4bbce335a96.json` sha256:`a4bbce335a967fd33001417c5a502840e1188ef63ccf7e23bf99f21e68a350d2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2023-2402 — **affected**

- conclusion_id: `4585f332-a41b-481b-9bb9-284f37ead5d3`
- justification: `—`
- attestation: `attestations/vex-GO-2023-2402-54f839152f32.json` sha256:`54f839152f32d2548086931c258f2effd5bd34e325dd587b15bd2d3953fbac15`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2024-2687 — **not_affected**

- conclusion_id: `6ed06149-0ad6-4bb5-a487-89f4b1cd5585`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2024-2687-4c4afe9f5943.json` sha256:`4c4afe9f594338b789cc4f5061bd1e3982a1d765b07ff055082fb9a0d0ca8803`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2024-3321 — **not_affected**

- conclusion_id: `934781a8-8963-4743-aeea-9662f9fc7dec`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2024-3321-22232b49997a.json` sha256:`22232b49997a1cd0d061a1e8ac925cc28062fe19bf1aebbdf13902703be87b07`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2024-3333 — **not_affected**

- conclusion_id: `d8b27c40-92e2-46f9-b345-b4d36a7d4494`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2024-3333-07a59484a47f.json` sha256:`07a59484a47fd811e9669dc226c8d0452c5f52897724fc623537c2c0473246d6`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2025-3487 — **affected**

- conclusion_id: `a29bbd1d-8d69-4f20-a1f5-03fcc6896738`
- justification: `—`
- attestation: `attestations/vex-GO-2025-3487-c7d91d46e812.json` sha256:`c7d91d46e812987a8463e43decd2c739b35e0adad3b2f0420b15439842068c38`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2025-3503 — **not_affected**

- conclusion_id: `79890b2c-6015-4127-a887-0ae22c5a29ce`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2025-3503-621e79cce577.json` sha256:`621e79cce5777f313ae643e4e39ca08d561d36725ed0e2f76556a29e955e53e5`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2025-3595 — **not_affected**

- conclusion_id: `2839cc3a-8bdb-411b-9148-7e0bebbd7b1f`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2025-3595-eeb5d82fae72.json` sha256:`eeb5d82fae72a30fc55d165739bb810904acc55bb6ef436a421d18df97d19cb7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2025-4116 — **not_affected**

- conclusion_id: `e75ade53-5f33-4d8c-8e35-83278b90f694`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2025-4116-d222d1c7b36c.json` sha256:`d222d1c7b36ccc2bab347117b317c7a27adf72c84d2170b1deafe7ee6addec35`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2025-4134 — **not_affected**

- conclusion_id: `7062ea15-ff88-4493-b81b-96234b9193fd`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2025-4134-6745dc6acd13.json` sha256:`6745dc6acd13df2a8f2ce045429302e414dcf009b6558a23bc9a38d7a45718c4`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2025-4135 — **not_affected**

- conclusion_id: `c1e11659-11e3-4d3f-961f-043a03c47427`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2025-4135-14b928be0ebd.json` sha256:`14b928be0ebda5600034e3e55f7db8462e9f29afabe2dcb3bf91ef68d4bd121f`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4440 — **not_affected**

- conclusion_id: `8b7a7887-067c-4186-b730-1184e3301cc6`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4440-3007075d5ec5.json` sha256:`3007075d5ec5d0369bc93795927af6a8c1f6afe0a93f098cae8b01ffd41ad7e9`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4441 — **not_affected**

- conclusion_id: `ae03442d-7568-48da-a9b8-f0ac57ca1aba`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4441-e62c5ae31bc6.json` sha256:`e62c5ae31bc6271951731062a9b6a2ce2e39f1881558a375e2090254a2633be9`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4864 — **not_affected**

- conclusion_id: `2575761c-9cdc-4e21-a8da-749907ed0733`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-4864-269fd008b191.json` sha256:`269fd008b191252f2116539857e6334a2d81ee87cb6d137f08fc1a3c55155422`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4865 — **not_affected**

- conclusion_id: `471d50bd-6a27-4789-b657-259b7e5c20ff`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4865-eb525159a7e3.json` sha256:`eb525159a7e30bf933a1ce02c6e98d91d3a668be5dc73b32859d5aedc34bf482`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4866 — **not_affected**

- conclusion_id: `7d7f0672-c564-480b-86a1-722213d8b3c9`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-4866-ecc604cca9ca.json` sha256:`ecc604cca9cabc13fdd9d46955b158988ec5d897f690da9c55b44ca0a582f46b`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4869 — **not_affected**

- conclusion_id: `b2199415-5091-4b84-809c-b302882ffd76`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4869-430b7a9d99ce.json` sha256:`430b7a9d99ce2c2df8883103358f00eef3b9986401bfd1151e78929fffa94008`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4870 — **not_affected**

- conclusion_id: `716ef79b-871e-48f6-9c1a-d152ca992248`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4870-0d974ba5f48d.json` sha256:`0d974ba5f48dfa0cda38776d979e8d184d51d581671d676bb078d21291820b16`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4918 — **not_affected**

- conclusion_id: `6afd9c39-19ed-4e8b-b5b5-5a3a63064258`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4918-8640d5db5387.json` sha256:`8640d5db538786121f7ae8d2f1f13d24092db0628ec613ce4edb462ff27ca3e2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4946 — **not_affected**

- conclusion_id: `c39fea7a-94be-4459-9cdd-5a7906bb8ddf`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-4946-87320416a519.json` sha256:`87320416a51902c31be4129be4a35a32ee1118b7606cef2767ffb333e4863206`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4947 — **not_affected**

- conclusion_id: `c15b7de0-19c1-4170-81aa-cecc25785e74`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-4947-59a8b34cc5ad.json` sha256:`59a8b34cc5ad686f2c55fd0c46b167ef983bde099d549317c331bcf0f444d341`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4970 — **not_affected**

- conclusion_id: `02275358-6360-4df5-9ee6-41a69c50baf3`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-4970-6cda62858d39.json` sha256:`6cda62858d3903c1549575f00df5001359893bcd13a01acde65cd68fd35b18bd`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4971 — **affected**

- conclusion_id: `502ad458-1172-4420-b969-10922e610a31`
- justification: `—`
- attestation: `attestations/vex-GO-2026-4971-f5414c997fdb.json` sha256:`f5414c997fdb5cbe0091f96167929413f4584342d26f92dc4a426a0af18c7b73`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4976 — **not_affected**

- conclusion_id: `3ee386b4-681c-4ee4-94d9-6e302f7fc4f2`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4976-1a1dfb0539c3.json` sha256:`1a1dfb0539c359a9bc428615decc8118118a1252039244e8153b5ca68da1ee28`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4977 — **not_affected**

- conclusion_id: `5ddc17bd-d1b9-46ec-b8d8-75de0c8e4797`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4977-808935de5d1d.json` sha256:`808935de5d1d9de5e1c11b3281b377e8fdfba0e8e3f99e680378f06a7d53c9f4`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4980 — **not_affected**

- conclusion_id: `b7465364-d88c-4352-9641-a151d83bf67c`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4980-45f567cb8044.json` sha256:`45f567cb804403f660d70eccde617bdeb88674972ed5f5323895ad2224af1fdb`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4981 — **not_affected**

- conclusion_id: `aea621fa-f563-472c-a96f-e5ef4e7f9649`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-4981-dc4a5edfc1c3.json` sha256:`dc4a5edfc1c3d248868e1e472914283bf1de1189f4544f8f654295c54ea0f3e2`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4982 — **not_affected**

- conclusion_id: `39e2c10f-b431-48a9-935a-da33d59df3bd`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4982-9cc4f17601c4.json` sha256:`9cc4f17601c454ed1344c1420549d088ea6e537f34d032adb51071a37e879691`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-4986 — **not_affected**

- conclusion_id: `628ee62b-7f1e-44b1-a613-0969815ef8f4`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-4986-fb2ab4c096cb.json` sha256:`fb2ab4c096cbd58d0674356017b26ca1129079932656ff1ad6f1db87dc8e51c6`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5005 — **not_affected**

- conclusion_id: `b8702d27-0f1e-435d-a050-50cac3dda283`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5005-289b7ab0bef9.json` sha256:`289b7ab0bef9588efffc4b04e6e03cf89ad79bc12c25dd17f462c3d5b48c4396`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5006 — **not_affected**

- conclusion_id: `66de7c04-dd3e-4f07-8b63-a7c4080dbe90`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5006-8893bc41c217.json` sha256:`8893bc41c217511526777bedf3c5fd44173d968f8968079a080e90e3bd1f97a7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5013 — **affected**

- conclusion_id: `ac8bf1a7-827b-4e4f-bbb4-5beac36a1e77`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5013-cc72284291a7.json` sha256:`cc72284291a78a7258a9e3b96be940aee45fd090f8330a0eefe20b1a29bd27fd`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5014 — **not_affected**

- conclusion_id: `1dd14a28-222f-44b3-aca5-4d29e50d1126`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5014-9397e8cf6f64.json` sha256:`9397e8cf6f649ee266b9c5ef88be37edba7da370800ed8e4c76fd7aae44e8d75`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5015 — **not_affected**

- conclusion_id: `cc600ac9-57fc-45c8-8ce9-b2e7f8904af4`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5015-df02ec3e24bc.json` sha256:`df02ec3e24bc4b1f57c66b917b2d8175cbb6e358b704cec8e873d3d7fb550344`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5016 — **not_affected**

- conclusion_id: `06e4bc94-f469-4781-9df5-51024cf261ee`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5016-06ec5fe3dfee.json` sha256:`06ec5fe3dfee16b7a802937ab263ef21c84e6b29aeeef128fdd739f7c35e64cb`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5017 — **affected**

- conclusion_id: `7fb2eb6d-1f38-49d3-9c1a-43ac5e264a59`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5017-470d57623f48.json` sha256:`470d57623f48605ead3a52ce1fad46857ee124945a64bc4e1a667860722f0bb3`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5018 — **affected**

- conclusion_id: `02d949a9-a3b2-4263-aacd-046b97032682`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5018-94e54b9692e4.json` sha256:`94e54b9692e472ab89d6376ce6822bde1f8cb3135828e6479385b0a20886a7e8`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5019 — **affected**

- conclusion_id: `3261db35-a1a6-4c9d-a3a8-ab4f7aeced63`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5019-f31023d17a27.json` sha256:`f31023d17a27377b2e191c0c33e47c838afbeafd1b3da27680ad9ee94ce5f808`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5020 — **affected**

- conclusion_id: `4f7f7500-fdea-40df-9a5c-406100cb3f67`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5020-2be56a358066.json` sha256:`2be56a358066f06a78bcdfb097831f9e1d96b5e718c5a537047153360751a89e`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5021 — **not_affected**

- conclusion_id: `c417d0f8-13cb-44a2-8f51-bed55d6f287e`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5021-6bd8f444653e.json` sha256:`6bd8f444653e9c4364ccf334316a2af81e43277f171446a8454bce9684ee4251`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5023 — **not_affected**

- conclusion_id: `5b5ccd33-9539-4d65-a790-1b3944900bfe`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5023-02ef59037a18.json` sha256:`02ef59037a18a9ec2d9fb976b9a0179589bc19938ee74bcb40779ec9fda39b02`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5024 — **under_investigation**

- conclusion_id: `9f7a18d7-f3ad-4e1c-a8ce-f5fcc555a62b`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5024-e8f9d56e7123.json` sha256:`e8f9d56e71235118431f1a302572aec53c7cf741d8f43a96049ac2fd6cd08af0`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5025 — **not_affected**

- conclusion_id: `6269d603-dcf3-43d1-a2c9-c8ad2101e6db`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5025-cce51f419e3b.json` sha256:`cce51f419e3b5289c58928a7a5b5290e3af80d4ef4764f25b65a3d14594967d4`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5026 — **affected**

- conclusion_id: `e250cff2-eae6-4d36-9ef2-f709450aae37`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5026-4c433dbb223c.json` sha256:`4c433dbb223c747a913264df3f620aa39572278a973fce0b4dbfd1b4132f38fe`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5027 — **not_affected**

- conclusion_id: `73e448bd-1fbd-420c-8987-3bd4e3c8355c`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5027-3f08cb6903d0.json` sha256:`3f08cb6903d0ddb474be235d13f7f3fc1b5c1a5ae9d6a30a9441d13f5dc9ac7e`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5028 — **not_affected**

- conclusion_id: `dcf5d3a7-40ae-419b-ad03-852c4c33af31`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5028-6df193db0409.json` sha256:`6df193db04095de987e6bdfc1fc825e7e714f47da825f7de3920c5bad2390e46`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5029 — **not_affected**

- conclusion_id: `6b7cfcad-d73f-438d-b99a-57218e0da5af`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5029-3a70db89ba5e.json` sha256:`3a70db89ba5ec3a89e99138527a1a3198e28282cdd055acf17cf8f159ae54c7a`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5030 — **not_affected**

- conclusion_id: `3e42af4f-645a-4348-98c7-83b30b6a523f`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5030-2fd2066e5fd3.json` sha256:`2fd2066e5fd3dd3a6c4e91487f3ad6226f916c680450f6818e4ab8590e8480f9`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5033 — **not_affected**

- conclusion_id: `79332e0f-2faf-4122-9287-7e0ce4ba38c1`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5033-bc41bab2eac5.json` sha256:`bc41bab2eac5be6920c5ea5604e51997bc278a23114a2595b72cd168bd6d9be4`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5037 — **not_affected**

- conclusion_id: `ae1a6ba6-4e40-4e09-a209-b99fb9ae0226`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5037-003a59ac9073.json` sha256:`003a59ac90738b1b48b720ccaab9682061553cbb3569359783684b0044946231`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5038 — **not_affected**

- conclusion_id: `edcb1d3c-7fa7-4c5f-bd3e-6857ecd946ec`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5038-c2d020028928.json` sha256:`c2d020028928640636cd532f36db34102bac916ded0fb0480edd03b795971f06`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5039 — **not_affected**

- conclusion_id: `59b9e574-bc17-4c8b-a8be-7f02d2fc42b6`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5039-e87fe4627113.json` sha256:`e87fe462711351417af6ec35873afd9edc8b51ae26415a3f2ea2805fc302ebca`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5856 — **not_affected**

- conclusion_id: `2d0f5d33-4361-4ffa-be2d-1c0928c72a0c`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5856-429f1dd7ade6.json` sha256:`429f1dd7ade61c01a78fc3c8824c113039227c3a055abc49d085b068d9e3bfe4`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5932 — **not_affected**

- conclusion_id: `653c3c04-83a4-4134-8b95-2711ee6813a4`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-5932-354d16ee57f5.json` sha256:`354d16ee57f58e5f34ab872ab52d4ed93a9f425968b08deda7f5a9a040fa6b79`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5942 — **not_affected**

- conclusion_id: `01ae32fb-4355-48d5-b850-222bbdb4c7a0`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5942-ff8dd930c4d8.json` sha256:`ff8dd930c4d836a9463ab3d369b6c19115723e5757a2e7e6090e544dd208d9cb`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5970 — **affected**

- conclusion_id: `d1035e18-24f5-4ca2-96a6-0c0276d5b592`
- justification: `—`
- attestation: `attestations/vex-GO-2026-5970-c9e65b9e3a23.json` sha256:`c9e65b9e3a236041b32ff33adcfbe4301e6d452860e6d258df3839f46f43d2b7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-5972 — **not_affected**

- conclusion_id: `454c7eec-609f-47c0-bd10-628798c4b831`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-5972-41d6e69adf9b.json` sha256:`41d6e69adf9b016eb5be1816340e093795e8bb5340d0e36365ad669ed7c142bf`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6088 — **not_affected**

- conclusion_id: `faebcedd-ca2a-47ab-8e4c-6149d158b405`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-6088-f74078347bbf.json` sha256:`f74078347bbf40349f74dd370fe18f140da070512df8eafe0902a4e4a0b33709`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6089 — **not_affected**

- conclusion_id: `ff67cfd4-0829-44be-8246-79d4b4acd6d9`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-6089-139aa934edf6.json` sha256:`139aa934edf65393710ca7be2f8d7d46c53c67e7c5be673c35b37da2aa0cce71`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6090 — **not_affected**

- conclusion_id: `11598b27-2025-4bb0-9b83-7c4a60b7f7fc`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-6090-744c2cd8253c.json` sha256:`744c2cd8253ca67c6711882ed67fc6db969596ed6b3c5b84ab4eed2655e6ded6`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6091 — **not_affected**

- conclusion_id: `b3ed41f7-1817-4941-a822-16194ee8c6e2`
- justification: `vulnerable_code_not_present`
- attestation: `attestations/vex-GO-2026-6091-c3a01d8fb4ae.json` sha256:`c3a01d8fb4ae28e2a77605bc808ee90795c26ebd2a6abf60c8ed8c85de6693db`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6218 — **not_affected**

- conclusion_id: `a5c718c3-d6f7-4370-b3c8-1cfa94c4be78`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-6218-9c35f0d9107e.json` sha256:`9c35f0d9107e63d1cfad99b471e64ad862418e9e1257c347daff6146a1a750fd`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6303 — **not_affected**

- conclusion_id: `5e7ab755-509c-4b5e-b74a-ad2e84bae5a1`
- justification: `vulnerable_code_not_in_execute_path`
- attestation: `attestations/vex-GO-2026-6303-2bf26ebd755e.json` sha256:`2bf26ebd755e35d2cac618e0969726132a23e9af744017d6626248275423e1b7`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6354 — **affected**

- conclusion_id: `53f3426f-8cff-4898-927d-da8978831a48`
- justification: `—`
- attestation: `attestations/vex-GO-2026-6354-a024aaf27a3c.json` sha256:`a024aaf27a3c42d8a39cff0276676879592585516b0a92160cb565f01e73a329`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`

## vex: GO-2026-6355 — **affected**

- conclusion_id: `ff9f2849-f63e-48cf-9a1a-078b95da6118`
- justification: `—`
- attestation: `attestations/vex-GO-2026-6355-4c4476136781.json` sha256:`4c447613678187f50f19abe189ec3f9a2330137c633a855f4a8f4eead205aaa3`
- signature: **verified ✓** (keyid `a57a061281f93b3a…`, signer `cra-research-poc-dev-key`)
- subject: `go-vuln-app-0.1.0` sha256:`1719ae6a81ee6bd84d754e2183dce398864c161af570a60964db60a2da564e43`
- tool: `vex.py` — 0.1.0
  - command: `pipeline/attest.py --product go-vuln-app --version 0.1.0 --artifact examples/go-vuln-app/go-vuln-app --sbom out/go-vuln-app/sbom.cdx.json --associations out/go-vuln-app/associations.json --reachability out/go-vuln-app/reachability.json --vex out/go-vuln-app/vex.openvex.json --keys keys --outdir out/go-vuln-app`
- timestamp: 2026-09-18T16:53:55Z
- evidence:
  - `tool-output:openvex` `/home/atituiset/Projects/cra-research/poc/out/go-vuln-app/vex.openvex.json` sha256:`da9656526f49651b820c82f84cebc7a8c07626e7248fdc15512bbc50acd2aad6`
