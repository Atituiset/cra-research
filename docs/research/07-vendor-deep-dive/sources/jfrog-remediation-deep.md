# Source Note: Smart Remediation 与 Zero-Touch Remediation 实现细节

- 来源层级：厂商官方文档 + 合作方（Chainguard）官方 changelog 交叉印证
- 抓取日期：2026-09-21

## URL 清单

1. Smart Remediation（2026-08-13 更新）: https://docs.jfrog.com/security/docs/smart-remediation
2. Zero-Touch Remediation Overview（2026-09-06 更新）: https://docs.jfrog.com/security/docs/zero-touch-remediation-overview
3. Interpreting Remediation in Scan Results（2026-09-06 更新）: https://docs.jfrog.com/security/docs/interpret-remediation-in-scan-results
4. Register Local Patches（2026-09-07 更新）: https://docs.jfrog.com/security/docs/register-local-patches
5. Chainguard products changelog（"Chainguard Libraries in JFrog"，2026-09-02 上线）: https://edu.chainguard.dev/chainguard/changelog/
6. swampUP 2026 live blog（Compliant Version Replacement）: https://jfrog.com/blog/jfrog-swampup-2026-live-updates/

## 关键事实点

### A. Smart Remediation（URL 1，原文要点）

- 输入是 SBOM（self-hosted 需 `sbom.enabled: true` + `sbom.dependenciesEnabled: true`），且必须能访问 **JFrog Catalog**。
- 三策略：**Quickest Fix**（最近安全版本）/ **Least Vulnerable**（最低风险分）/ **Best Version**（四级优先级：policy-approved non-breaking → approved breaking → 非 approved non-breaking → 非 approved breaking，每层取最低风险分）。
- 风险权重：**Critical=10,000 / High=100 / Medium=10 / Low=1**。
- 两条路径：**In-Lock override**（Maven/npm/PyPI/Go/NuGet/Conan）与 direct 升级；容器侧 **base image upgrade**（给 Dockerfile `FROM` 行；不跨发行版推荐；要求 base image 与本镜像在同一 JFrog Platform 都被扫过）。
- 自曝上限："only selects the latest **500 versions** to prioritize from…partial results may happen"；全局免责 "best-effort recommendations and **may not be complete or fully accurate**"；`Curation Approved`/`Policy Approved` badge 标 **Coming Soon**。

### B. Zero-Touch Remediation（URL 2/3/4，原文要点）

- **Maven：下载时拦截**。build 请求原坐标 → Artifactory 问 Xray → Xray 查 Catalog patched 候选（clearing-house vendor rebuild + virtual repo 内注册的 local patch）→ **Least Vulnerable** 选择（权重 **Critical×1,000,000 / High×10,000 / Medium×100 / Low×1**；同分 local patch 优先于 vendor rebuild；再平手按 automation vendor priority）→ 候选能降低 CVE 暴露才替换，否则**给原始 artifact（不阻断）**。
- **npm：lockfile healing**，不拦截 tarball。JFrog CLI 把 `package-lock.json` 发给 Xray → 返回改写 lockfile（patched 版本 + 指向同一 virtual repo 的 `resolved` URL + Artifactory 内 artifact 算出的 integrity）→ npm install 装 patched tarball。**标准 `npm install` 不触发**；`package.json` 声明不变。local patch 不适用 npm。
- **vendor 生态**：Chainguard（仅 Maven）/ Echo / TuxCare / Seal Security；vendor 参与前提 = 其 remote repo 挂在被覆盖的 virtual repo 下。
- **local patch 注册**（URL 4）：`POST /xray/api/v1/ztr/patches` + **CycloneDX 1.6 声明**；仅 Maven；无 UI；需 Manage Data 权限。
- **Patched 状态判定**（URL 3）："JFrog Catalog identifies the served version as a patched rebuild, **and** Catalog data confirms the CVE is resolved on that exact rebuilt version"；local patch 时 Catalog 存 CycloneDX 声明并重打分。审计三分：**Healed / Skipped / Not required**。
- 官方给出 Patched 展示的四条设计理由：evidence of value / **scanner reconciliation**（承认第三方扫描器按原坐标会报出差异）/ auditability / developer trust。
- URL 5（对侧印证）："JFrog Catalog now recognizes Chainguard-built packages…**This is what underpins JFrog's Zero-Touch Remediation**"。
- URL 6：swampUP 2026 演进叙事 "**Compliant Version Replacement**（a bad version swapped out with a patched one, mid-pipeline）"。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §6 全部；§10-5/6；§11-2。
- 加深 03 §6③④：③双路径机制补全（策略/权重/上限）；④Patched 状态的判定前提与审计设计补全——确认其仅限 ZTR 场景，且依赖 Catalog 数据而非通用重扫。
