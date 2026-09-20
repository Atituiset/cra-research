# Source Note: Snyk MCP 支持（官方）

- URL: https://snyk.io/articles/secure-ai-coding-with-snyk-now-supporting-model-context-protocol-mcp/ ；https://snyk.io/blog/run-automcp-libraries-mcp-servers/
- 标题: Now Supporting Model Context Protocol (MCP) / Run AutoMCP…
- 发布方: Snyk 官方
- 发布日期: 2025-05-15；2025-12-03
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方

## 关键事实点

- Snyk 把扫描能力封装为 **MCP server**（随 CLI 分发，第三方核验 2026-09：13 个 tool、本地执行扫描），让 IDE 内的 AI agent（Copilot/Cursor 等）在生成代码时自主触发 Snyk 扫描并修复。
- 配套发布 **mcp-scan** 工具（扫描 MCP endpoint 暴露面）——厂商自身也在把 MCP 当作新的攻击面治理对象。

## 支撑报告结论

- AI/Agent 层的业界收敛点：**MCP 成为"安全工具 → AI 编码 agent"的标准接口**（2025 年中起头部厂商集中跟进）；安全能力以 tool 形态被 agent 编排，而非安全厂商自造 agent 闭环。
