# Source Note: Apiiro Guardian Agent / AutoFix（官方+第三方）

- URL:
  - https://apiiro.com/platform/（Context Graph 平台页）
  - https://apiiro.com/blog/confidence-in-agentic-code-fixes-is-rising-but-not-without-a-strong-aspm-program/（2025-10-30）
  - https://www.devopsdigest.com/apiiro-releases-autofix-agent（2025-08-04）
  - https://awards.thehackernews.com/winners/2026/apiiro-agentic-application-security-platform/（2026）
  - https://appsecsanta.com/apiiro（2026-07-14 第三方评测）
- 发布方: Apiiro 官方 + DEVOPSdigest + The Hacker News + AppSec Santa
- 抓取日期: 2026-09-18
- 来源层级: 厂商营销材料 + 第三方分析

## 关键事实点

- 定位：Agentic Application Security Platform；底座是 Deep Code Analysis（专利）+ 实时软件图谱（Risk Graph / Context Graph）：连接代码仓库、函数、数据流、构建管道、部署目标、运行时。
- Guardian Agent：拦截发往 Copilot/Cursor 等编码 agent 的 prompt，注入安全上下文/威胁模型/合规策略，在 prompt 层阻断不安全模式（第三方评测描述）；向 Athena 社区贡献新发现漏洞（厂商招聘信息转述）。
- AutoFix AI Agent（2025-08-04 发布）：生成上下文感知修复、自动化测试验证、产出 review-ready PR；官方博客承认"agentic code fix 的信心依赖持续上下文"，即强 ASPM 程序是前提。
- 集成 Chainguard 的修复状态入 Risk Graph。
- 客户：USAA、BlackRock、Shell、SoFi（第三方评测）。

## 支撑报告结论

- Apiiro 是"图谱+多 agent"路线代表：真 agent 编排而非 chatbot；其"prompt 层预防"是差异化。
- 但对象仍是应用/仓库/运行时风险，不是 Product→Version 的合规生命周期 → 定位空白论据。
