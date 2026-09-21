# Source Note: Endor Labs AI/Agent 架构（MCP Server、AURI、Claude Code Skills、Agentic UI）

- URL（一组）:
  - https://www.endorlabs.com/learn/fix-first-security-for-the-vibe-coding-era （MCP Server 发布博客，2025-04-23）
  - https://github.com/endorlabs/skills-ideas （官方 GitHub：Claude Code skills/hooks/rules + MCP Tools Reference）
  - https://www.prnewswire.com/news-releases/endor-labs-introduces-auri-security-intelligence-for-agentic-software-development-302701739.html （AURI 发布稿，2026-03-03）
  - https://docs.endorlabs.com/secure-ai-coding/agentic-ui （Agentic UI / AppSec Assistant 官方文档）
  - https://docs.endorlabs.com/setup-deployment/mcp/ （MCP 部署文档族：Cursor/Claude Code/Codex/VS Code/Devin/Gemini CLI/Augment/IntelliJ/Antigravity/OpenCode/GitHub AgentHQ）
- 发布方： Endor Labs 官方（GitHub/博客/文档）+ PR Newswire 官方新闻稿
- 抓取日期： 2026-09-21
- 来源层级： 官方 GitHub 仓库与文档（事实性强）；新闻稿含厂商声称

## 关键事实点

### MCP Server 形态

1. **分发方式**：`npx -y endorctl ai-tools mcp-server`——MCP server 内嵌在 endorctl 中，无独立安装；通过 `ENDOR_API=https://api.endorlabs.com` 指向 SaaS。
2. **MCP tools 清单（skills-ideas 仓库 README 的 MCP Tools Reference）**：
   - `scan`（path + scan_types: vulnerabilities/secrets/dependencies/sast/ghactions；quick_scan/pr_incremental/pr_baseline 选项；**返回按严重性排序的 finding UUID 列表**）；
   - `check_dependency_for_vulnerabilities`（ecosystem/name/version → CVE、严重性、推荐升级版本）；
   - `check_dependency_for_risks`（前者超集，加恶意包检测）；
   - `security_review`（AI 驱动的 diff 安全审查，**需 Enterprise Edition 且启用 AI security code review**）；
   - `get_endor_vulnerability`（按 CVE/GHSA 取漏洞详情）；
   - `get_resource`（按 UUID/name 取任意资源：Project/PackageVersion/Vulnerability/Finding/Metric/ScanRequest/ScanResult/Policy）。
3. **架构特征**：LLM agent 拿到的是**确定性引擎产出的结构化结果**（finding UUID、CVE 详情、升级版本），LLM 只做编排与叙述——"get a meaningful answer that isn't LLM guesswork or hallucination"（官方定位语）。
4. 认证：浏览器 OAuth（google/github/gitlab/sso/email）或 CI 用 API key（`ENDOR_API_CREDENTIALS_KEY/SECRET`）。
5. 免费层：AURI 发布稿确认 "free developer tier of its MCP server"。

### Claude Code Skills 仓库（endor-solutions-claude-skills）

6. 官方维护 26 个 slash-command skills（/endor-scan、/endor-scan-full "Deep scan with reachability analysis"、/endor-upgrade-impact、/endor-fix、/endor-sbom 等）+ 8 个 **hooks**（依赖安装后触发 /endor-check、manifest 编辑后触发、MCP 错误恢复、会话结束提醒 /endor-review 等）+ always-on rules。
7. Hook 分级语义：Block (exit 2) / Warn / Suggest——把安全拦截嵌入 agent 生命周期事件。

### AURI（2026-03-03 发布稿，厂商声称为主）

8. 定位："combining **agentic reasoning with deterministic static analysis**"；能力是 "deep code reasoning"（multi-file call graphs + dataflow 检测业务逻辑缺陷）、"full-stack reachability"（一方代码+依赖+容器层）、"ecosystem monitoring"（持续扫 OSS 项目与 AI 模型）、"**agent orchestration**（specialized agents work together to detect, triage, and remediate）"。
9. "code context graph"：连接一方代码、OSS 依赖、容器镜像、AI 模型的统一视图（VentureBeat 同日报道佐证此术语）。
10. 客户引语：Cursor 安全团队 "Over 97% of vulnerabilities flagged by our previous tool weren't reachable in our application"。
11. 分发：MCP + CLI + Skills，进 Cursor/VS Code/Windsurf 等 IDE；OpenHands 产品负责人背书（agent 生态合作信号）。

### Agentic UI（AppSec Assistant，官方文档）

12. 应用内 AI Chat，**数据范围硬限制**："generate answers based **solely** on specific data available within the Endor Labs platform: Findings / Scan results / Vulnerabilities / Package versions"——超出范围则不回答。这是确定性的 grounding/防幻觉设计。
13. 前提：需开启 "Code Segment Embeddings and LLM Processing"（与 C/C++ embedding 同一数据隐私开关）。

## 支撑报告结论

- 维度 7：Endor 的 AI 架构是"**确定性引擎在下、agentic 编排层在上**"（官方原话 "we've built a new agentic AI layer above that"）；MCP 是主要 agent 接口且工具面薄而结构化；防幻觉靠 (a) 工具返回引擎结构化结果、(b) chat 数据范围硬限制。有 MCP server（自家工具暴露给外部 agent），同时 Coding Agent Governance 是治理**别人**的 agent/MCP（hooks 采集 + 策略），两个方向都有产品。
