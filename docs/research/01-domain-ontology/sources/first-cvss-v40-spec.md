# Source Note: CVSS v4.0 Specification（FIRST）

- **URL**: https://www.first.org/cvss/v4-0/specification-document
- **标题**: CVSS v4.0 Specification Document（Document Version 1.2, 2024-06-18；v1.0 初始发布 2023-11-01）
- **发布方**: FIRST.Org, Inc.（CVSS 由 FIRST 拥有和管理，免费授权公众使用）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方（规范原文）

## 关键摘录 / 事实点

1. 定义原文："an open framework for communicating the **characteristics and severity** of software vulnerabilities" —— 注意官方定位是 severity（严重性），不是 exploitation probability。
2. v4.0 由**四个** metric group 组成：**Base / Threat / Environmental / Supplemental**（v3.x 是 Base/Temporal/Environmental 三组；v4.0 把 Temporal 改名为 Threat，并新增 Supplemental）。
3. Base = 漏洞固有特征，跨时间跨环境不变；Threat = 随时间变化的特征（如 PoC 可用性、active exploitation）；Environmental = 用户环境特有特征（缓解措施、资产关键性）；Supplemental = 不改变分数的补充上下文。
4. **Nomenclature**（v4.0 新增强制标注）：CVSS-B（仅 Base）/ CVSS-BT（+Threat）/ CVSS-BE（+Environmental）/ CVSS-BTE（全量）。规范明确："numerical CVSS scores should be labeled using nomenclature that communicates the metrics used in its generation."
5. Base 分 Exploitability metrics（AV/AC/AT/PR/UI）和 Impact metrics（VC/VI/VA + SC/SI/SA，v4.0 区分 vulnerable system 与 subsequent system）。
6. "Base Metrics, and optionally Supplemental Metrics, are provided by the organization maintaining the vulnerable system... Threat and Environmental information is available to only the end consumer." —— 即 **评分公布者通常只给 CVSS-B，环境化评分是消费方的责任**。
7. 评估 Base 时假定攻击者对目标有先验知识且目标带默认防护；目标特定缓解措施应体现在 Environmental 而非 Base。

## 支撑报告中的结论

- §8 CVSS 定位（severity 度量，不是概率）
- §8 v3.1 vs v4.0 差异（4 metric groups、Supplemental、nomenclature、subsequent system）
- §8 "CVSS 9.8 不一定先修"：公布的多为 CVSS-B，未含 Threat/Environmental，消费方应自行环境化
- §14 Exploitability 与 CVSS Exploitability metrics 的区别（规范假定 worst-case 环境）
