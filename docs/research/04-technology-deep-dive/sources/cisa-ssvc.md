# Source Note: CISA — Stakeholder-Specific Vulnerability Categorization (SSVC)

- URL: https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc
- 标题: Stakeholder-Specific Vulnerability Categorization (SSVC)
- 发布方: CISA（政府机构，一手）
- 抓取日期: 2026-09-18
- 来源层级: 标准/方法论（政府机构官方）

## 关键摘录 / 技术要点

- SSVC 由 CMU SEI 与 CISA 于 2019 年创建；2020 年 CISA 定制了自己的 decision tree（面向 USG/SLTT/关键基础设施）。
- CISA SSVC 输出四个决策：**Track / Track\* / Attend / Act**（每个带明确的响应动作与时限建议）。
- 决策基于 5 个 decision point：Exploitation status、Technical impact、Automatable、Mission prevalence、Public well-being impact。
- SEI 白皮书 "Prioritizing Vulnerability Response: A Stakeholder-Specific Vulnerability Categorization (Version 2.0)" 定义了 Supplier / Deployer / Coordinator 等不同角色的树。
- CISA 提供 SSVC Calculator（可导出 PDF/JSON）。
- 另：CISA 通过 Vulnrichment 以 CVE ADP container 发布 SSVC decision points（Exploitation/Automatable/Technical Impact），见 OpenCTI connectors issue #7068；2026 年 BOD 26-04 要求联邦机构以 SSVC 为优先级方法（待一手核实）。

## 支撑报告结论

- 第二部分：SSVC 是 exploitability/prioritization 决策框架的成熟先例——决策树（规则化、可解释、可审计）优于打分混合，是本报告"决策模型应规则+证据而非黑盒打分"的关键依据。
- SSVC 的 decision points（Exploitation/Automatable/Technical Impact）大部分可由威胁情报数据机械填充（CISA Vulnrichment 已在做），但 Mission/Well-being 与部署上下文仍需组织侧输入。
