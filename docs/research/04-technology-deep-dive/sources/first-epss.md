# Source Note: FIRST — Exploit Prediction Scoring System (EPSS)

- URL: https://www.first.org/epss
- 标题: Exploit Prediction Scoring System (EPSS)
- 发布方: FIRST.org / EPSS SIG（标准组织，一手）
- 抓取日期: 2026-09-18
- 来源层级: 标准组织官方文档

## 关键摘录 / 技术要点

- EPSS 是数据驱动的机器学习模型，估计一个已公开 CVE 在未来 30 天内被在野利用的概率（0–1，附 percentile），每日发布，CSV/API/GitHub 免费开放。
- 由 FIRST 的 EPSS SIG 维护，打分由 Empirical Security 生成。
- 利用活动数据来自 VulnCheck KEV、Shadow Server Foundation、LevelBlue 等合作伙伴。
- 官方建议：EPSS 与 CVSS、KEV 组合使用，设阈值而非替代影响分析（Using EPSS 页）。
- 版本沿革（多个二手来源一致，需以 FIRST research 页为准）：v1 2019 Black Hat 发布 logistic regression 16 变量；v2 2022-02 全量 ML 1000+ 变量；v3 2023-03；v4 2025-03-17 发布，自称 ROC AUC 0.838。
- 相关：NIST 2025-05 发布 "Likely Exploited Vulnerabilities (LEV)" 白皮书，基于 EPSS 概率估计 KEV 收录不完整度（待一手核实）。

## 支撑报告结论

- 第二部分：EPSS 是"全局/群体级" exploit likelihood 信号，与"本产品内 exploitability"是不同层次——决策模型中只能作为外部先验，不能回答 context-specific exploitability。
- 数据开放性意味着 EPSS 不构成任何厂商的壁垒。
