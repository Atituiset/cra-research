# Source Note: AppTrust 与 Evidence 证据链（DSSE/in-toto 实现、subject 粒度、流转）

- 来源层级：厂商官方文档 + 官方开源仓库 + 官方新闻稿（Business Wire）
- 抓取日期：2026-09-21

## URL 清单

1. AppTrust Overview（2026-06-25 更新）: https://docs.jfrog.com/governance/docs/jfrog-apptrust
2. Create Evidence CLI（2026-05-28 更新）: https://docs.jfrog.com/governance/docs/create-evidence-cli
3. JFrog MCP Server Tools（2026-07-30 更新，Evidence/AppTrust 工具）: https://docs.jfrog.com/integrations/docs/jfrog-mcp-server-tools
4. GitHub Actions: GitHub attestation to JFrog evidence（2026-09-10 更新）: https://docs.jfrog.com/integrations/docs/github-actions-github-attestation-to-jfrog-evidence
5. JFrog AppTrust Evidence Partners（2026-07-07 更新）: https://docs.jfrog.com/governance/docs/evidence-partners
6. Evidence Ecosystem 扩展新闻稿（2025-09-09）: https://www.businesswire.com/news/home/20250909201600/en/JFrog-Extends-its-System-of-Record-Solution-Empowering-Application-Delivery-Governance-with-Evidence-from-World-Leading-Companies
7. 开源 DSSE 组件: https://github.com/jfrog/evidence-extractor （dsse.io 解码器）；Go 包 https://pkg.go.dev/github.com/jfrog/jfrog-cli-artifactory/evidence/dsse
8. Evidence Solution Sheet（PDF，营销材料）: https://media.jfrog.com/wp-content/uploads/2024/12/23184548/JFrog-Evidence-Solution-Sheet.pdf

## 关键事实点

### A. Evidence 格式栈（URL 2，原文）

- predicate = 任意 JSON；**predicate-type 用 in-toto URI**，官方示例：`in-toto.io/attestation/link/v0.3`、`/scai/attribute-report`、`/runtime-trace/v0.1`、`/test-result/v0.1`、`/vulns`。
- 签名密钥 `rsa`/`ed25519`/`ecdsa`（PEM/SSH）；公钥以 `--key-alias` 注册在 Artifactory，创建时做 **DSSE 验证**（缺公钥输出 "created but not verified"）。
- **`--sigstore-bundle`** 支持直接上传 Sigstore 预签 DSSE envelope；subject 可从 envelope 自动解析（解析失败 exit code 2）。
- 公钥删除后 **Evidence 服务缓存最长 4 小时**仍可验签（官方 Note）。

### B. MCP 层佐证（URL 3，Evidence 7.277+）

- 工具原文："Prepare a **ready-to-sign in-toto statement** for a JFrog subject"（支持返回 **DSSE PAE** 字节）、"Upload an already-signed **DSSE envelope** as evidence"、按 repo/path/sha256 检索 evidence、Markdown 渲染（7.289+）。
- → Evidence 在格式层是 in-toto statement + DSSE envelope 的原生实现。

### C. subject 粒度与流转（URL 1/2/3/4）

- evidence 可挂五种 subject：**artifact / package / build / Release Bundle v2 / application version**。
- **evidence 跟随 subject 穿越 promotion**（URL 4 原文）："If you move your image from a 'dev' repo to a 'prod' repo within JFrog, the Evidence follows the artifact automatically." Distribution 分发 RBv2 时有 `include_evidence` 选项（URL 3）。
- Trusted Release badge（URL 1 原文）："a **cryptographically signed attestation** stored in Artifactory that travels with the release as an immutable audit record"。不可变实现方式未说明（不确定）。
- gate = **OPA/Rego**，可按 application/project/组织定义，warn 或 block；Activity Log 记每个事件的 timestamp+actor。
- Evidence Graph 可视化 + 导出（URL 8，厂商声称）。

### D. AppTrust 对象模型（URL 1/3）

- "**application** as a first-class entity"：ownership、business criticality、maturity level。
- MCP 暴露精确字段：`maturity_level` 枚举 `unspecified/experimental/production/end_of_life`；`criticality` 枚举 `low/medium/high/critical`；application version 有 `sign_key_name`，`release_status` 三态 **`PRE_RELEASE/RELEASED/TRUSTED_RELEASE`**；promotion 支持 move/copy/keep/dry_run + rollback。

### E. 生态（URL 5/6）

- 2025-09-09 宣布 Evidence Ecosystem（GitHub build attestation、ServiceNow、SonarQube、NVIDIA 等十余家）；第三方工具可经 reference designs（GitHub 仓库）接入，示例 Anchore（Syft 签 SBOM + Grype 扫描结果）。
- URL 7：JFrog 开源 DSSE 工具链（evidence-extractor / dsse.io / jfrog-cli-artifactory 的 dsse Go 包含 PAE/EnvelopeSigner/Verifier）。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §4（证据链）、§5（对象模型）；§12-2/7（不可变实现、CRA Rego 模板未核实）。
- 相对 03 §1.5 第 11 条（"证据与二进制加密绑定，厂商声称"）：证据格式与签名机制现已升级为**官方文档可核实**；不可变性实现仍未核实。
