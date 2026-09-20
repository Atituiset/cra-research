# Source Note: Checkmarx One SCA / Developer Assist / Mend SCA（官方+第三方）

## Checkmarx
- URL:
  - https://checkmarx.com/cxsca-open-source-scanning/（SCA 产品页，2026-09-03 快照）
  - https://checkmarx.com/product/triage-and-remediation/（Triage & Remediation Assist，2025-04-23）
  - https://checkmarx.com/blog/ai-llm-tools-in-application-security/revolutionizing-sca-with-agentic-ai-how-checkmarx-developer-assist-transforms-open-source-security-within-the-ide/（2025-11-19）
  - https://www.pixee.ai/blog/checkmarx-vs-veracode（2026-05，第三方）
- 抓取日期: 2026-09-18
- 层级: 厂商营销材料 + 第三方对比
- 事实点:
  - SCA 差异化："exploitable path analysis"——判定漏洞类/函数是否被调用（厂商声称）；强调比 reachability 更精确的"可利用路径"。
  - Developer Assist（2025-11 官方博客）：agentic AI 在 IDE 内实时 SCA——即时发现恶意包、自动化安全修复，"plan, execute, and validate"（厂商声称）。
  - Triage & Remediation Assist：风险优先级 + review-ready 修复建议。
  - 第三方（pixee.ai）指出：Checkmarx 与 Snyk/Veracode 均**未公布 AI 修复合并率（merge rate）**；Pixee 自称 76% 合并率（竞品声称，仅作"可信度指标缺失"论据）。
  - Checkmarx One 为 9 引擎 ASPM 平台（SAST/SCA/DAST/IaC/容器/API/secrets 等，第三方评测）。
  - 未见专门 CRA 页面（检索未命中）。
- 支撑结论: 传统 AST 厂商的 agentic 化速度；"merge rate 等可信度指标全行业缺失"支撑 agentic remediation 可信度创新空间。

## Mend
- URL: https://www.mend.io/sca/（2026-09-02 快照）；https://docs.mend.io/legacy-sca/latest/sca-reachability（2025-02-19）；https://www.mend.io/compliance/（2026-09-04）
- 层级: 厂商营销页 + 官方文档
- 事实点:
  - Mend SCA 宣称覆盖 200+ 语言（检测面）、reachability 降噪、"修复时间降 80%"（厂商声称）。
  - Reachability 为 Mend 传统强项（业内最早一批做 SCA reachability 的厂商；文档有专门章节）。
  - 合规页覆盖 EU AI Act/NIST/CRA + AI-BOM + red teaming（代码层+AI 层双层合规叙事）。
  - Renovate（开源依赖更新工具）归属 Mend——自动升级 PR 生态位。
  - 未找到 Mend 官方 CRA 产品模块；CRA 指南见 mend-cra-guide.md。
- 支撑结论: Mend = "SCA 老牌 + reachability + Renovate + AI-BOM"组合；CRA 靠内容营销映射。
