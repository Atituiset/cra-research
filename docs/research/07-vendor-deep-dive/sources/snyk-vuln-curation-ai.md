# Source Note: Snyk 漏洞库 Human+AI 策展（官方博客深挖）

- URL: https://snyk.io/blog/human-ai-the-next-era-of-snyks-vulnerability-curation/
- 标题: Human + AI: The Next Era of Snyk's Vulnerability Curation
- 发布方: Snyk 官方博客（Security R&D Group 自述）
- 发布日期: 2025-07-14
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方（一手陈述自身数据管道内部机制）

## 关键事实点

1. **使命与四支柱**（原文）："curate and organize every open source vulnerability on the planet"；衡量标准四柱 = **Timeliness / Completeness / Accuracy / Actionability**。
2. **起点形态**：分析师团队"在一个大 JSON 文件里手工策展漏洞"；后建内部工具自动化，但关键决策保留给人工：是否真漏洞 vs 质量问题、受影响包、受影响版本区间、是否有 fix、CVSS vector、是否有已知 exploit、CVE ID、最准确 CWE。
3. **AI Agent 在策展管线的五个角色**（原文）：
   - Lead generation：搜网找新漏洞早期信号；
   - Code analysis：监控 commit、比对代码变更，用 Snyk 私有静态分析引擎识别潜在问题（目标：在漏洞被利用前就把可疑 commit 标记入库）；
   - Prioritization：帮分析师按严重性×影响面排序；
   - Data enrichment：**RAG** 从既有"人工验证过的"数据库检索，向分析师建议漏洞元数据；
   - Post-publication monitoring：发布后持续扫描 fix、backport、新 exploit。
4. **HITL + RLHF**（原文）：分析师 validate/approve AI 建议，高调漏洞尤其如此；反馈闭环"formally known as **Reinforcement Learning from Human Feedback (RLHF)**"。
5. **工程质量机制**（原文）：**Eval-driven development**（分析师为 LLM/prompt 写 eval，"basically unit tests"）+ **LLM-as-a-Judge**（模型当裁判打分，评估 accuracy 与 hallucination）；用 Model System Cards 与 LMArena 跟踪选型；prompt/context engineering；自训分类模型（判断 commit 是否含潜在漏洞）。
6. **内部 MCP Server**（原文，值得注意）："building a **centralized MCP Server** to act as a unified orchestration layer. This server wraps our entire suite of security tools, from code scanners to internal and external APIs"，分析师用自然语言交叉比对 repo commit 与数据库、直接更新漏洞记录。——MCP 在 Snyk 内部先用于策展团队自身提效。
7. **下一步（前瞻声明）**：预测性分析（按历史漏洞、开发模式、代码复杂度、AI agent 采用度预测哪些项目会产生弱点）；在官方 fix 出现前自动生成安全补丁建议。

## 口径注意

- 未给出人工 vs AI 的定量比例；"比例"只可定性描述为"AI 做 lead/富化/排序，人做判定"（Interpretation）。
- "训练 AI agent 大规模发现可疑 commit 并抢在利用前入库"是进行式（"we are now training"），非已完成能力。

## 对本轮深挖的支撑

- 维度 1：策展流程、人机分工、RLHF/eval 机制均有官方一手表述。
