# Source Note: Snyk Evo 生产指标新闻稿（2026-09-17，含修复合并率与规模数据）

- URL: https://snyk.io/news/agentic-ai-security-moves-into-production/
- 标题: As AI Risk Scales and Vulnerabilities Compound, Evo by Snyk Reaches 60% of New Deal Volume
- 发布方: Snyk 官方新闻稿
- 发布日期: 2026-09-17（抓取日 4 天前，最新）
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方新闻稿（商业数据为厂商声称；技术指标可交叉验证到 VulnBench 论文与 Golden Test 博客）

## 关键事实点

1. **Evo 商业牵引**（厂商声称）：占新单额 60%；平均合同额 +30%；首个能力 GA（2026-03）以来月环比客户增长 81.5%；76% 客户在购买的当季即上生产。
2. **运行规模**（厂商声称）：每月 **240 万次 agent 供应链扫描**、每天 **420 万次 agent 行为检查**、**41.7 万台已纳管机器**；某美国大行集中管理约 1,000 个内部 agent skills、服务 50,000 名用 Claude Code 的开发者（7 月起上线）。
3. **修复合并率数据（本轮最重要发现之一）**："Open source issues remediated through Snyk's independent validation layer **merge at a 94% higher rate** than fixes produced by a frontier model working alone." —— 全行业首个公开的 AI 修复合并率对比声明（相对值，未给绝对基线与样本量）。
4. **架构信条**（原文）："the generator cannot be the validator"；"Every Evo solution places an **independent, deterministic security layer beneath the model**"；多模型设计（multi-model by design）。
5. **VulnBench 引用**（原文）："when the same code and the same prompt were run five identical times, **nearly half of the issues flagged by an LLM alone appeared in only one of the five runs**; the best-performing model scored **75.4%** against Snyk's reference set"。
6. **三环产品表述（官方最新口径）**：Evo Agentic AppSec（Secrets GA / Remediation Agent **open preview** / Agentic AppSec Agent private preview，编排成 continuous autonomous triage-and-remediation loop）、Evo Agentic Development Security（2026-06 GA）、Evo AI-SPM（2026-03 GA）、Evo COS（2026-08 GA，验证防御架构在对抗压力下是否成立）；四环叙事 discover→remediate→validate→prevent 在文中以 "continuous security model" 复述。
7. **需求侧数据**（厂商声称）：4,800+ 客户的新引入 issue 数 Q4 2025→Q1 2026 涨 108%。

## 对本轮深挖的支撑

- 维度 3：94% merge-rate lift 是 Agent Fix/Remediation 合并率的唯一公开数字（注意是相对声明）。
- 维度 4：Evo 四环的最新官方表述与产品化状态。
- 维度 8：平台运行规模的可引用数字。
