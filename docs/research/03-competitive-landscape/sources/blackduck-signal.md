# Source Note: Black Duck Signal + CRA 案例（官方新闻稿/PR）

- URL:
  - https://www.prnewswire.com/news-releases/introducing-black-duck-signal-agentic-ai-application-security-for-modern-development-302637175.html（2025-12-10）
  - https://www.helpnetsecurity.com/2026/03/23/black-duck-signal-secures-ai-generated-code-with-agentic-application-security/（2026-03-23，GA）
  - https://www.blackduck.com/signal-ai-appsec.html（产品页）
  - https://www.prnewswire.com/news-releases/stmicroelectronics-integrates-black-duck-sca-and-coverity-for-automated-sbom-generation-and-enhanced-software-security-302392021.html（2025-03-06）
- 发布方: Black Duck 官方 / PR Newswire / Help Net Security
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方新闻稿 + 媒体转载

## 关键事实点

- Black Duck Signal：2025-12-10 发布、2026-03 GA 的 agentic AI AppSec 产品，由 ContextAI 驱动（声称结合"20+ 年人工策划情报"），直接集成进 AI 编码工具工作流，"自动发现并修复安全缺陷、无假阳性"（厂商声称）；覆盖代码、二进制、供应链。
- 公司背景：Synopsys 软件完整性业务剥离为独立公司 Black Duck；Gartner AST MQ 八连冠（2025，厂商引用）；Forrester SCA Wave 四连冠（厂商引用）。
- CRA 证据点：STMicroelectronics 集成 Black Duck SCA + Coverity 自动化 SBOM 生成用于 CRA 合规（2025-03 官方 PR，CEO Jason Schmitt 背书）——Black Duck 在**制造业/半导体产品** CRA 场景有实际客户案例。
- 2026 OSSRA 报告页提及 CRA/DORA；Black Duck 有 Signal/SBOM/VEX 组合但未见专门的"CRA 产品模块"。

## 支撑报告结论

- Black Duck 的双层策略：传统 SCA（审计级 SBOM/VEX，面向制造业客户 CRA）+ Signal（agentic AI 修复，面向 AI 代码）。
- 支撑"agentic remediation 成为 2025-12 起所有头部厂商的标配发布"。
