# Source Note: JFrog AI/Agent 叙事与 MCP Server 能力面

- 来源层级：厂商官方文档（MCP 工具、AI Catalog）+ 官方新闻稿 + 媒体报道（标注）
- 抓取日期：2026-09-21

## URL 清单

1. JFrog MCP Server Tools（2026-07-30 更新）: https://docs.jfrog.com/integrations/docs/jfrog-mcp-server-tools
2. Business Wire：Self-Healing Software Supply Chain / agentic remediation（swampUP 2025，2025-09-09）: https://www.businesswire.com/news/home/20250909861213/en/DevSecOps-in-the-AI-Era-JFrog-Powers-Agentic-Remediation-with-Self-Healing-Software-Supply-Chain
3. Business Wire：JFrog Fly agentic repository（2025-09-09）: https://finance.yahoo.com/news/jfrog-unveils-industry-first-agentic-131500776.html
4. SiliconANGLE 报道 swampUP 2025 一批发布: https://siliconangle.com/2025/09/09/jfrog-unveils-ai-era-platform-upgrades-software-supply-chains/
5. devops.com：swampUP 2026 Agent Guard / ZTR（2026-09-02）: https://devops.com/jfrog-moves-to-secure-agentic-engineering-workflows/
6. JFrog AI Catalog Overview 文档: https://docs.jfrog.com/ai-ml/docs/jfrog-ai-catalog-overview
7. Pricing（Multi-agent Support、Policy-as-Code Playground、agent evidence）: https://jfrog.com/pricing/

## 关键事实点

1. **官方 MCP Server 工具面**（URL 1）：toolset 覆盖 Access（Tokens/OIDC/Projects/Roles）/ Artifactory（Repos/Packages/Builds/Federation/Storage）/ Security（Catalog 漏洞查询、Xray 摘要、impacted resources 搜索）/ **Curation（含 waiver 审批 approve/reject，强制 justification）** / Distribution / Workers / **OneModel（统一 GraphQL，Beta）** / Event（webhook）/ **Evidence（创建、验签、检索、Markdown 渲染）** / **AppTrust（application 生命周期、promotion、release、activity log）**。→ agent 可执行的不只是查询，还有治理动作。
2. **swampUP 2025（2025-09-09）**（URL 2/3/4，厂商声称）：JFrog Fly（"行业首个 agentic repository"，MCP 对接 GitHub Copilot/Claude Code/Cursor）；Self-Healing Software Supply Chain（agentic remediation，MCP + Copilot 集成）；AI Catalog；AppTrust；Evidence Ecosystem。
3. **swampUP 2026（2026-09）**（URL 5，媒体报道）：**Agent Guard**（把 Artifactory 治理延伸到 AI agent 的插件与资产）；ZTR 的 "Compliant Version Replacement"。
4. **Multi-agent Support**（URL 7）：Claude/Codex/Cursor/Devin/VS Code/IntelliJ/Copilot/OpenCode/Kiro，agent 在平台策略内走可信解析路径。
5. **Policy-as-Code Playground**（URL 7）：自然语言 → Rego 策略，AI 辅助工作台，可对真实 application version 预验证。
6. **Agent 行为证据化**（URL 7 原文）："Automatically capture **agent interactions** and generating a **signed evidence chain** from commits, PRs, and Jira tickets, attached to every application version."
7. **AI Catalog**（URL 6）：AI 资产（模型、MCP server、agent skills、插件）的发现/治理/安全枢纽。

## 解读（Interpretation）

- JFrog 的 AI 路线 = 平台能力 MCP 化卖给别家 agent（Fly=agent 的仓库、MCP Server=工具箱、Agent Guard=治理），而非用 LLM 做漏洞判定；Contextual Analysis 仍是人工规则库。两条路线在哲学上一致：判定要保守可控，自动化留给分发与治理。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §7 全部。
- 修正 03 §1.5 第 10 条（"AI/Agent：弱；MCP 生态集成在演进"）——2025-09 起 MCP Server 官方化、工具面完整，评级应上调。
