# Source Note: CISA Known Exploited Vulnerabilities Catalog

- **URL**: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **标题**: Known Exploited Vulnerabilities (KEV) Catalog
- **发布方**: CISA（美国网络安全与基础设施安全局）
- **抓取日期**: 2026-09-18（当时目录共 1713 条记录）
- **来源层级**: 官方文档（政府一手数据）

## 关键摘录 / 事实点

1. 目录条目字段：CVE ID、Vendor、Product、Vulnerability Name、Date Added、**Due Date**、Required Action、"Known To Be Used in Ransomware Campaigns?"（Known/Unknown）。
2. 截至 2026-09，条目行动要求引用 **BOD 26-04 "Prioritizing Security Updates Based on Risk"**（取代早期 BOD 22-01 的新版 Binding Operational Directive），并新增 "Forensic triage required per BOD-26-04: Yes/No" 字段。
3. 典型 Due Date 为加入后 3 天至 3 周不等（如 2026-09-16 加入、2026-09-19 到期）。
4. CVE-2021-44228 (Log4Shell) 于 2021-12-10 加入（与 CVE 发布同日），Due Date 2021-12-24（见 sources/nvd-api-20-cve-2021-44228.md 中的 cisaExploitAdd 字段）。
5. 入录标准（CISA 官方定义，见 https://www.cisa.gov/known-exploited-vulnerabilities-catalog 页面说明区）：CVE 已被分配、存在可靠证据表明该漏洞在野外被积极利用（active exploitation）、有明确的补救措施。注意：**入录依据是"已观测到利用"，不是"存在 PoC"**。

## 支撑报告中的结论

- §8 KEV 定义与 "known exploited" 的判定门槛
- §8 KEV 与 PoC 存在的区别
- §8 信号链 KEV → observed exploitation
- §14 Exploitability 讨论中 KEV 作为外部证据信号
