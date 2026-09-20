# Source Note: GitHub (GHAS/Dependabot) 与 Veracode 汇编

## GitHub
- URL:
  - https://docs.github.com/code-security/supply-chain-security/understanding-your-software-supply-chain/exporting-a-software-bill-of-materials-for-your-repository（SBOM 导出）
  - https://docs.github.com/en/code-security/concepts/code-scanning/autofix-for-code-scanning（Copilot Autofix）
  - https://druce.ai/governance/wiki/vendors/github-advanced-security（2026-08 汇编：2025 年 GHAS 拆分为 Secret Protection + Code Security 两个 SKU）
  - 检索证据：搜索 "GitHub Cyber Resilience Act github.blog" 无官方 CRA 页面命中，结果均为第三方仓库（zealience 等）
- 抓取日期: 2026-09-18
- 层级: 厂商官方文档 + 第三方汇编
- 事实点:
  - SBOM：从 dependency graph 导出（SPDX），repo 粒度；无 SBOM 导入/管理产品。
  - Copilot Autofix：为 code scanning（CodeQL）告警自动生成修复建议，PR 内呈现；第三方（Heeler 对比，竞品视角）指出"不在沙箱中构建验证修复"（需谨慎）。
  - Dependabot：自动升级 PR 的鼻祖（商品化标杆）；第三方对比（Safeguard 2026-05）确认 Dependabot **无 reachability**。
  - 无专门 CRA 方案/页面；合规叙事靠 SBOM 导出 + 通用安全功能。
- 支撑结论: GitHub 代表"够用就好"的平台内置基线——SCA 扫描/升级 PR/SBOM 导出免费或捆绑化，加速商品化；但 reachability/VEX/Product 维度缺位。

## Veracode
- URL:
  - https://www.businesswire.com/news/home/20260128773416/en/Veracode-Releases-Platform-Enhancements-as-Software-Supply-Chain-Attacks-Surge（2026-01-28）
  - https://docs.veracode.com/updates/r/c_all_sca（SCA 更新页，2026-08-20 快照）
  - https://docs.veracode.com/updates（2026-08-31 快照：Fix for SCA Limited Availability；Package Firewall 2026-07-07 更新）
  - https://community.veracode.com/s/question/0D5Uf000003VxISKA0/（2023-12：SCA API 已含 KEV/EPSS）
- 抓取日期: 2026-09-18
- 层级: 厂商官方新闻稿/文档 + 媒体报道
- 事实点:
  - Package Firewall（2025-06 首发、2026 持续更新）：在包进入供应链前阻断——"prevention"环节代表。
  - 2025-01 收购 Phylum 获得恶意包行为检测（typosquatting/dependency confusion）。
  - SCA agent v3.8.120（2026）修复 JavaScript "vulnerable method scans" → 证实 Veracode 有 vulnerable-method（function 级）扫描，主打 Java/.NET 生态。
  - SBOM：SCA agent 扫描时生成 CycloneDX SBOM（2025-06-03）；SBOM API 支持 upload scans（2026）。
  - Veracode Fix for SCA：Limited Availability（2026 年中）；Fix 主打 SAST 自动修复。
  - EPSS/KEV 2023 年已集成。
  - 未见专门 CRA 产品页。
- 支撑结论: Veracode 传统企业市场、合规报告强，但 CRA/产品版本维度无专门动作；Fix for SCA 仍 LA 说明 agentic 修复成熟度参差。
