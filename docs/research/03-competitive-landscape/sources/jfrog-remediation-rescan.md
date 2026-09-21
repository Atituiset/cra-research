# Source Note: JFrog Xray Remediation（Smart Remediation + Patched 状态回扫）（本 note 供 03 报告 §6 使用）

- URL:
  - https://docs.jfrog.com/security/docs/smart-remediation
  - https://docs.jfrog.com/security/docs/interpret-remediation-in-scan-results
- 发布方： JFrog（官方文档；后者页面显示 "Updated 14 days ago"，即约 2026-09-07）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

### Smart Remediation（CVE-based + component-based）

- 原文："You can remediate in two ways: **CVE-based remediation** — find the best fix for a specific vulnerability, including whether to upgrade a direct dependency or override a transitive one. **Component-based remediation** — identify package upgrades that reduce the most overall risk, even when you are not targeting a single CVE."
- CVE-based 修复基于 SBOM impact path 分析，区分直接升级 vs 传递依赖 in-lock override；生态支持矩阵：Maven/NPM/PyPI 支持 In-Lock+Direct，Go/NuGet/Conan 仅 In-Lock。
- 三种版本选择策略：Quickest Fix（最小版本跳）/ Least Vulnerable（最低风险分）/ Best Version（Coming Soon，policy+non-breaking 四层优先级）；候选版本按 severity 加权评分（Low=1 … Critical=10,000）。
- 文档免责："Remediation suggestions represent best-effort recommendations and may not be complete or fully accurate in all cases."
- 徽章体系含 **Non-Breaking**（遵守 semver 约束）——breaking change 判断是 semver 启发式，非 Endor 式程序分析。

### 修复后 re-scan 带回 Patched 状态

- 原文："Xray adds a **Patched** status to the contextual analysis vocabulary alongside Applicable, Not Applicable, Not Scanned, and other existing values."
- **限定条件**（重要）：Patched 状态仅在 **Zero-Touch Remediation** 场景生效——"A CVE on a remediated component displays as Patched when: JFrog Catalog identifies the served version as a patched rebuild, and Catalog data confirms the CVE is resolved on that exact rebuilt version."（Catalog 提供的 vendor patched rebuild 或注册的 local patch）
- 目的四条（原文）：Evidence of value / Scanner reconciliation / **Auditability**（"Governance, risk, and compliance teams can prove a finding was present and remediated, with lineage and timestamps"）/ Developer trust。

## 支撑报告结论

- 二手声明 ③（Smart Remediation 支持 CVE-based 与 component-based 两条路径）**成立**。
- 二手声明 ④（修复后 re-scan 把 remediation 状态 patched 带回扫描结果）**部分成立**：机制存在且逐字属实，但仅限 Zero-Touch Remediation（patched rebuild/local patch）场景，不是通用的"任意修复后重扫自动标注"；二手声明把它泛化了。
- 对 03 §1.5 的补强：JFrog 在"验证重扫"环节有行业少见的明确产品化（Patched 状态 + Catalog 对齐的 CVE 过滤），但绑定其制品仓库/Catalog 生态。
