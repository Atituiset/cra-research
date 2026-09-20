# Source Note: OSV API — GHSA-jfh8-c2jp-5v3q（Log4Shell 的 OSV 条目）

- **URL**: https://api.osv.dev/v1/vulns/GHSA-jfh8-c2jp-5v3q
- **标题**: OSV entry GHSA-jfh8-c2jp-5v3q "Remote code injection in Log4j"
- **发布方**: GitHub Advisory Database 导出，经 osv.dev 聚合（Google 运营）
- **记录时间线**: published 2021-12-10T00:40:56Z / modified 2025-10-22
- **抓取日期**: 2026-09-18
- **来源层级**: 官方文档（一手 API 数据）

## 关键摘录 / 事实点

1. `id: GHSA-jfh8-c2jp-5v3q`，`aliases: ["CVE-2021-44228"]` —— OSV/GHSA 通过 aliases 与 CVE 互认。
2. `affected[].package` = `{ ecosystem: "Maven", name: "org.apache.logging.log4j:log4j-core", purl: "pkg:maven/org.apache.logging.log4j/log4j-core" }` —— **直接用 Maven 坐标 + PURL 标识组件**。
3. 受影响范围用多段 range 表达（ECOSYSTEM 类型事件序列 + 显式 versions 枚举）：
   - `[2.13.0, 2.15.0)` — versions: 2.13.0 … 2.14.1
   - `[2.0-beta9, 2.3.1)` — versions: 2.0 … 2.3
   - `[2.4, 2.12.2)` — versions: 2.4 … 2.12.1
   这精确表达了"2.12.2/2.3.1 等 backport 修复版本不受影响"。
4. 还列出了**换名重发布**的包 `com.guicedee.services:log4j-core`（`introduced: 0`, `last_affected: 1.2.1.2-jre17`）——同名不同 groupId 的 shaded/fork 包也被单独建模，这是 CPE 很难做到的。
5. `severity: [{"type": "CVSS_V3", "score": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H/E:H"}]`（带 E:H 的 Temporal 度量）。
6. `database_specific` 含 `cwe_ids: [CWE-20, CWE-400, CWE-502, CWE-917]`、`github_reviewed: true`、源文件指向 github/advisory-database 仓库中的 JSON。
7. details 中写明修复版本 2.16.0 移除 message lookup、2.15.0 只是部分修复（引出 CVE-2021-45046）、backport 版本 2.3.1/2.12.2/2.12.3、workaround（移除 JndiLookup 类）。

## 支撑报告中的结论

- §5 OSV Schema 真实条目拆解（ecosystem/package/purl/ranges/versions）
- §5 "OSV 为什么适合 SCA"：Maven 坐标 + 版本区间可直接与依赖树匹配
- §6 GHSA 条目与 CVE 的 alias 关系、github_reviewed 机制
- §15 backport / fix version / workaround 的真实样例
