# Source Note: Snyk Evo Continuous Offensive Security GA（官方新闻稿）

- URL: https://snyk.io/news/snyk-launches-evo-continuous-offensive-security/
- 标题: Snyk Launches Evo Continuous Offensive Security to Protect Enterprises Against Autonomous AI Attacks
- 发布方: Snyk 官方新闻稿
- 发布日期: 2026-08-04
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方新闻稿（营销声明为主，能力表述需标注厂商声称）

## 关键事实点

- Evo COS GA：自主 AI 渗透测试 + Agent Red Teaming，随应用变化持续攻击，返回"攻击者实际可利用"的验证证据（厂商声称）。
- 四环叙事：Discover（AI-SPM：模型/agent/MCP server/skills 清单，入 AI-BOM）→ Remediate（Evo Agentic AppSec 修复 agent，public preview，CLI/ADE 入口）→ Validate（COS：AI pentest + DAST，消费 Snyk Code/Open Source/API&Web 的存量发现作为上下文）→ Prevent（Snyk Secrets GA、prevention gates、恶意代码防御 private preview）。
- 关键差异化（厂商声称）：COS 以静态扫描结果作为 AI pentest 的上下文输入，专注架构/业务逻辑缺陷；批评竞品 benchmark "100% 通过率用纯黑盒非 SOTA 模型刷的"，自称在建基于真实客户环境的新一代 benchmark。
- 客户：Emburse、Yalo 引言。4800+ 全球客户。
- 配套时间线：Evo 首发 2025-10-22（experimental preview，"world's first agentic security orchestration system"，厂商声称）；Evo Agentic Development Security 2026-06-23（对 AI 编码 agent 的全生命周期治理）。

## 支撑报告结论

- Snyk 已从 copilot 式 AI 转向**多 agent 编排**（Discover/Remediate/Validate/Prevent 四个防御环），属"真 agent 编排"阵营的头部。
- "Validate"环（持续验证可利用性）是 exploitability 决策方向最激进的产品化尝试。
- 但 Evo 的对象仍是"应用/repo/agent 资产"，未见 Product→Version 维度的漏洞生命周期对象 → 定位空白论据。
