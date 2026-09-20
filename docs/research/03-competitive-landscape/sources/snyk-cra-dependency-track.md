# Source Note: Snyk CRA 内容 + Dependency-Track（OSS 基线）

## Snyk CRA 内容
- URL: https://snyk.io/blog/understanding-the-eus-cyber-resilience-act-cra/（2025-01-22）；https://snyk.io/blog/understanding-cra-compliance/（2025-06-25）；https://snyk.io/es/lp/what-you-need-to-know-about-cra/（LP + cheat sheet）
- 层级: 厂商官方博客 + 营销 LP
- 事实点: Snyk 有持续 CRA 内容营销（解读+合规方法+cheat sheet 下载），主张"把安全测试集成进开发工作流以满足 CRA"；产品映射为扫描+SBOM 生成+合规报告（厂商声称）。未见专门的 CRA 产品模块或产品版本生命周期功能。
- 支撑结论: Snyk 的 CRA 策略 = 内容营销 + 现有能力映射，介于"真方案"与"蹭概念"之间偏前者。

## OWASP Dependency-Track（开源基线）
- URL: https://owasp.org/blog/2023/02/07/vdr-vex-comparison（OWASP 官方 VDR/VEX 博文）；https://devsecopsschool.com/blog/owasp-dependency-check-vs-owasp-dependency-track-features-differences-evolution-milestones-and-best-use-cases/（2026-07，第三方）
- 层级: OWASP 官方 + 第三方分析
- 事实点:
  - Dependency-Track 以 **project（含版本）为一级对象**组织 SBOM 组合（portfolio），持续监控组件风险、支持 VEX 消费/分析、策略管理——是开源世界最接近"Product→Version 漏洞管理"的实现。
  - 4.13（2025-12）接受 CycloneDX 1.7 摄入。
  - 局限（第三方）：不生成 SBOM（只摄入）；无 reachability；UI/工作流面向安全运营而非开发闭环；无 CRA 证据模型。
- 另注：独立 OSS 项目 sbom-sentinel（GitHub，2026）自称"为每个出货产品保持最新 SBOM、监控新漏洞、判断可利用性、路由给开发者、保留 EU 监管所需证据"——说明个体开发者已在拼这个闭环，但无商业产品完整覆盖。
- 支撑结论: Product→Version 维度在开源侧有雏形（D-T 的 project/portfolio 模型），商业 AppSec 平台反而缺 → B 分析核心证据。
