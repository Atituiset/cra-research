# Source Note: GitHub Advisory Database 官方文档

- **URL**: https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database
- **标题**: About the GitHub Advisory Database
- **发布方**: GitHub Docs
- **抓取日期**: 2026-09-18
- **来源层级**: 厂商官方（文档）

## 关键摘录 / 事实点

1. Advisory 以 **OSV 格式的 JSON 文件**发布（GitHub Advisory Database 本身就是 OSV 生态的一个数据库）。
2. Advisory 三类：vulnerability（有 fixed version 概念）、malware（无 safe version，只能移除）、GitHub-reviewed vs unreviewed 分层。
3. **GitHub-reviewed** advisory：来自 GitHub 上报告的 advisory、NVD、npm、FriendsOfPHP、Go Vulncheck、Python Packaging Advisory DB、RubySec、RustSec、社区 PR 贡献；由 GitHub Security Lab curation team 人工审核有效性、补全 description/ecosystem/package 信息；覆盖 Composer/Erlang/Go/GitHub Actions/Maven/npm/NuGet/Pip/Pub/RubyGems/Rust/Swift 等生态。
4. **Unreviewed** advisory：直接从 NVD feed 自动导入，**Dependabot 不会为 unreviewed advisory 产生告警**。
5. **GHSA ID**：每条 advisory（无论类型）在创建或导入时分配 `GHSA-xxxx-xxxx-xxxx`，字符集 `23456789cfghjmpqrvwx`（去掉易混淆字符），正则 `/GHSA(-[23456789cfghjmpqrvwx]{4}){3}/`。GHSA ID 与 CVE 无关——无 CVE 的漏洞也能有 GHSA。
6. Advisory 包含：description、severity（Low/Moderate/High/Critical）、affected package、ecosystem、affected versions、patched versions、references、workarounds、credits。
7. GitHub 同步 FIRST 的 EPSS 分数（每日同步），并展示 percentile；EPSS 数据不可被社区 PR 修改。
8. 支持 CVSS 3.1 和 4.0；若 CVE 由 maintainer 提供分数则沿用 maintainer 的。
9. Dependabot alerts 基于 GitHub-reviewed advisory 与 dependency graph 的匹配。

## 支撑报告中的结论

- §6 GHSA 定义、GHSA ID 结构、GHSA 与 CVE 的关系（可独立存在，经 alias 关联）
- §6 GitHub-reviewed vs unreviewed 分层 → 为什么 GHSA 数据质量高于纯 NVD 导入
- §6 Dependabot 如何使用 advisory（只告警 reviewed）
- §5 OSV 格式作为事实上的开源 advisory 交换格式
