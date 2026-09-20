# Source Note: Datadog — State of DevSecOps 2025（runtime context 对优先级的影响）

- URL: https://www.datadoghq.com/about/latest-news/press-releases/datadog-state-of-devops-2025/ （报告页 https://www.datadoghq.com/state-of-devsecops/）
- 标题: Datadog's State of DevSecOps 2025 Report Finds Only 18% of Critical Vulnerabilities Are Truly Worth Prioritizing
- 发布方: Datadog（厂商报告/新闻稿，基于其数万客户应用的遥测数据）
- 日期: 2025-04-23；抓取日期 2026-09-18
- 来源层级: 厂商研究报告（一手数据，但有厂商立场）

## 关键摘录 / 技术要点

- 核心数字：**仅 18% 的 CVSS-critical 依赖漏洞在加入 runtime context（是否生产环境、是否暴露到互联网等）后仍保持 critical**；2026 年版报告称该数字与去年持平。
- 方法：Datadog 自研 prioritization 算法，把 runtime context 因子叠加到 CVSS base score 上。
- 其他发现：Java 应用的 exploitable 漏洞比例尤其高；部署频率低的服务依赖陈旧度高 47%。

## 支撑报告结论

- 第二部分：deployment/runtime context 是当前业界**最大的降噪杠杆**之一（82% 的 critical 被降级），且实现成本低（无需 call graph）——这是"reachability 叙事可能被高估"的关键反证：runtime context + 曝光面过滤可能比 function-level call graph 性价比更高。
- 第二部分决策模型：runtime context 作为独立决策因子的实证支持。
