# Source Note: Snyk Agent Fix / Remediation Agent（agentic 修复的产品化现状）

- URL: https://snyk.io/blog/snyk-agent-fix-agentic-architecture/ (2026-04-27)；https://snyk.io/blog/snyk-remediation-agent-in-the-cli/ (2026-05-29)；https://snyk.io/jp/blog/snyk-agent-fix-remediation-benchmark/ (2026-08-18)；https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-code/manage-code-vulnerabilities/fix-code-vulnerabilities-automatically
- 发布方: Snyk（厂商官方博客/文档）
- 抓取日期: 2026-09-18
- 来源层级: 厂商工程博客 + 官方文档（基准数据为厂商自述）

## 关键摘录 / 技术要点

- Agent Fix（前身 DeepCode AI Fix）：为 Snyk Code 发现的漏洞生成修复；2026-04 宣布新 **agentic 架构**（前沿模型 + "Snyk Intelligence"：fix 时注入该弱点类别的专家撰写修复样本做 dynamic few-shot）。
- 关键工程机制——**pre-screening**：所有生成的 auto-fix 先过一遍 Snyk Code SAST 扫描，验证可读、确实解决原问题、不引入新漏洞，"agentically in seconds"，只把高质量修复推给开发者。
- Golden Test benchmark（厂商自述）：Agent Fix 架构比裸前沿模型（Gemini 3.1 Pro / Claude Sonnet 4.6 / Opus 4.6）修复率提升 14%+；同时评估 "secure AND functional"（不仅修掉还要不破坏功能）。
- Remediation Agent in CLI（2026-05）：SCA 侧修复 agent；官方明确分层——Fix PRs 是 deterministic 规则化升级（每年数百万个），Agent Fix 处理 SAST 修复，Remediation Agent 处理 SCA 批量修复编排。

## 支撑报告结论

- 第三部分：头部厂商的修复 agent 架构 = **LLM 生成 + 确定性 SAST 校验 + 专家数据增强 + 人工 merge**，与本报告推荐的职责划分完全一致；"secure and functional" 双目标验证是修复验证的现实标准。
- 幻觉防护先例：不让 LLM 结论直接落地，必须经过 deterministic re-scan。
