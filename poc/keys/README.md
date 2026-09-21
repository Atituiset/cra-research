# keys/ — 开发用演示签名密钥

**仅限开发 / DEV ONLY。** 这里的 ed25519 私钥随仓库提交，唯一目的是让 PoC
端到端可复现。任何真实部署都必须：

1. 立即轮换此密钥（它已公开，不具备任何信任价值）
2. 改用 KMS/HSM 托管的 signer（securesystemslib 支持 `azurekms:`、`gcpkms:`、
   `hsmsigner:` 等 signer URI，[attest.py](../pipeline/attest.py) 的签名接口无需改动）
3. 公钥通过带外渠道分发，验证方固定 keyid

文件：
- [dev-ed25519.pem](dev-ed25519.pem) — 私钥（PKCS#8，未加密）
- [dev-ed25519.pub.json](dev-ed25519.pub.json) — 公钥（securesystemslib key dict，含 keyid）
