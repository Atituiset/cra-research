# Source Note: NVD Developers — Vulnerabilities API 2.0 文档

- **URL**: https://nvd.nist.gov/developers/vulnerabilities
- **标题**: NVD API Documentation — Vulnerabilities
- **发布方**: NIST NVD
- **抓取日期**: 2026-09-18
- **来源层级**: 官方文档

## 关键摘录 / 事实点

1. 两个核心 API：
   - **CVE API** `https://services.nvd.nist.gov/rest/json/cves/2.0`：按单个或集合检索 CVE；offset 分页（`startIndex` + `resultsPerPage`）。
   - **CVE Change History API** `https://services.nvd.nist.gov/rest/json/cvehistory/2.0`：检索 CVE 变更历史（何时、为何被修改）。
2. 官方提醒：NVD 自 1999 年存在，**2015 年之前的记录字段保真度明显较低**。
3. （配合 sources/nvd-api-20-cve-2021-44228.md）API 2.0 的 JSON schema 中 CVE 记录包含：id、sourceIdentifier、published/lastModified、vulnStatus、descriptions、metrics（cvssMetricV31/V40/V2、SSVC）、weaknesses、configurations（CPE applicability）、references、CISA KEV 内嵌字段。
4. 另有 CPE API、CPE Match Criteria API（未本次抓取）；传统 1.1 JSON data feeds 已退役，API 2.0 是现行官方接口（（不确定）旧 feed 退役具体时间未核实，但 2.0 API 是当前文档唯一推荐途径）。

## 支撑报告中的结论

- §4 NVD API 2.0 / data feed 使用方式
- §4 NVD 数据质量的历史遗留问题（pre-2015 记录）
