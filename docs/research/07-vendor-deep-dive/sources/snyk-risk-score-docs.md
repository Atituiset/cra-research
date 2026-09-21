# Source Note: Snyk Risk Score 官方文档（组成因子全清单）

- URL: https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/risk-score
- 发布方: Snyk（官方用户文档，页面 2026-09-15 前后更新）
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方文档（一手）

## 关键事实点

1. **模型结构**：0–1000 分 = Impact subscore × Likelihood subscore 思路；模型由 Snyk Security Data Science 团队与安全研究员研发，"draws on expertise gained over the years in developing the Snyk Vulnerability Database"。License issue 不支持。
2. **Objective impact 因子**：CVSS impact 指标（Confidentiality/Integrity/Availability/Scope，按 CVSS impact subscore 计算）；Container issue 另加 **Provider Urgency**（Linux 发行版安全团队的 urgency 评级）。
3. **Contextual impact 因子**：**Business criticality**（用户自定义 Project attribute；未配置时默认 `high`，即不影响 subscore；改属性后需 retest 才生效）。
4. **Objective likelihood 因子**（官方列全）：
   - Exploit Maturity（Snyk 检索并验证的公开 exploit；四档 No Known Exploit / PoC / Functional / High，分数影响从"显著降低"到"显著增加"）；
   - **EPSS**（FIRST 模型，**每日更新**；恶意包时 EPSS 强制置 1；无数据时默认 0.01055）；
   - Age of advisory（发布时间 >1 年 likelihood 降一次——这是 score 随时间自发变化的唯一机制）；
   - CVSS exploitability 指标（Attack Vector / Attack Complexity / Privileges Required / User Interaction / Scope）；
   - **Social Trends**（社媒流量，Snyk 研究称可预测未来 exploitation；Trending 则升分）；
   - **Malicious Package**（True 则显著升分）；
   - Provider Urgency（Container，同时影响 Impact 与 Likelihood）；
   - **Package popularity**（Open Source；生态内相对流行度 High 升 / Low 降）。
5. **Contextual likelihood 因子**：
   - **Transitive depth**（间接依赖降分；依据"Snyk research"：传递引入的漏洞更不可能存在可利用函数路径）；
   - **Reachability**（Reachable → 升分且 **transitive depth 不再计入**；No path found → 不变；未启用 reachability 则因子不出现）。
6. **发布状态（重要口径）**：Risk Score 截至该文档仍为 **Early Access**（Open Source + Container，所有 plan 可开），需 Snyk Preview 开关替换 Priority Score；**CLI 中不可用**；API 字段名仍是 `priority`（EA 阶段复用旧字段装新模型）；Snyk Code 与 Snyk IaC 仍用旧 Priority Score。启用后需 retest（Open Source 每日自动、Container 每周）才生效。
7. Risk Score 自 2023-08 公开（博客 "Introducing Snyk's new Risk Score"），到 2026-09 仍未 GA——3 年 EA。

## 对本轮深挖的支撑

- 维度 5：Risk Score 组成因子完整官方清单到手；reachability 仅在 Reachable 时单向升分（No path found 不降分）——"只加不减"设计值得注意。
- 维度 10：Risk Score 长期 EA、CLI 不可用、API 字段名遗留，均为官方自曝的成熟度局限。
