# Source Note: Snyk Studio / MCP Server 官方文档（实现细节）

- URL: https://docs.snyk.io/agent-security/agentic-security-with-snyk-studio/getting-started-with-snyk-studio （2026-09-10 更新）；配套 quickstart（Codex CLI 等）
- 发布方: Snyk 官方用户文档
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方文档（一手）

## 关键事实点

1. **Snyk Studio 是 2026 年的 agent 安全产品线名**；两种落地路径：
   - **hooks-based "secure at inception" (SAI)**：对支持 hooks 的 ADE（Claude Code、Cursor、Codex CLI、Gemini CLI、GitHub Copilot CLI/VS Code）用 installer 脚本（snyk/studio-recipes GitHub 仓库分发，可自行 build/审计/内部托管）；
   - **rules-based**：不支持 hooks 的 ADE 走 MCP server + directives。
2. **MCP server 实现**（原文）：
   - "The Snyk MCP Server is designed as a **local MCP server**, running on your system using the Snyk CLI to ensure local file access. **Snyk does not offer a hosted remote MCP server.**"
   - 启动方式：`npx -y snyk@latest mcp -t stdio`（MCP server 是 CLI 的子命令，CLI v1.1296.2+ 内置，无额外依赖）。
   - **tool profiles 三档**：`lite`（最小集，控 token/context 成本）/ `full`（默认，全部稳定 tool）/ `experimental`；用 `--profile` 或 `SNYK_MCP_PROFILE` 配置。profile 的存在说明官方承认 MCP tool 数量有 token 成本问题。
   - **12 个 tool**（文档表格）：`snyk_auth`、`snyk_code_scan`、`snyk_sca_scan`、`snyk_version`、`snyk_logout`、`snyk_trust`、`snyk_send_feedback`、`snyk_container_scan`、`snyk_iac_scan`、`snyk_sbom_scan`、`snyk_aibom`、`snyk_package_health_check`。
   - **directives 两类**：Secure at inception directives（引导 agent 在代码生成时即测安全）+ Remediation directives（加速存量问题修复）。
3. 架构含义：Snyk 把扫描器包成 MCP tool 的方式 = **CLI 内嵌 stdio server + 本地执行 + profile 控面**，而非云端托管 API 化；安全判定仍在本地 CLI/引擎，LLM 只拿结果。

## 对本轮深挖的支撑

- 维度 4：MCP 实现细节（local-only、stdio、12 tool、三档 profile、hooks vs rules 双路径）。
