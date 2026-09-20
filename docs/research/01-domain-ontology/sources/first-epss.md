# Source Note: EPSS 官方页面（FIRST）

- **URL**: https://www.first.org/epss/
- **标题**: Exploit Prediction Scoring System (EPSS)
- **发布方**: FIRST.org（EPSS Special Interest Group；分数由 Empirical Security 生成并免费发布）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方

## 关键摘录 / 事实点

1. 定义原文："a data-driven machine-learning model that estimates the **probability** that a published CVE will be exploited in the wild in the **next 30 days**."
2. 每天为**每个已发布 CVE** 发布 0–1 的概率值和 percentile 排名，数据免费公开（CSV + API + GitHub repo）。
3. 定位：用观测到的利用活动等经验信号替代主观判断，把有限的修复精力集中到最可能被攻击的漏洞上。
4. 数据源合作伙伴包括 VulnCheck KEV、Shadow Server Foundation、LevelBlue 等（exploitation activity 数据）。
5. 治理：EPSS SIG 挂靠 FIRST，实践者社区每两周例会。

## 支撑报告中的结论

- §8 EPSS 定义：probability ≠ severity，时间窗口 30 天
- §8 EPSS 与 CVSS 的本质区别（机器学习预测模型 vs 静态特征度量公式）
- §8 信号链中 EPSS → likelihood 的位置
