# Source Note: JFrog 交付模式与 Curation 封闭环境部署（第三方评测 + 集成商博客）

- URL: https://appsecsanta.com/jfrog-xray ；https://portersfiveforce.com/blogs/how-it-works/jfrog ；https://www.almtoolbox.com/blog/jfrog-curation-self-managed/
- 标题: JFrog Xray Review 2026 / How Does JFrog Company Work / JFrog Curation for Closed Environments
- 发布方: AppSec Santa（第三方评测）；Porter's Five Forces；ALMtoolbox（JFrog 集成合作伙伴）
- 发布日期: 2026-07-14 / 2025-12-06 / 2026-03-29
- 抓取日期: 2026-09-20
- 来源层级: 第三方评测与生态伙伴（与官方口径一致，无冲突）

## 关键事实点

- Xray 不单独售卖/部署，**作为 JFrog Platform 的安全层运行，依赖 Artifactory**；部署选项：JFrog SaaS（Cloud）、Self-Hosted（Docker/K8s）；Artifactory 支持 hybrid SaaS / self-hosted / **air-gapped**（面向受监管环境）。
- Self-managed 环境下 Curation 的工作模型：开发者经 Artifactory 拉包 → Curation 按策略判定 → 放行或阻断（registry 代理拦截点）。
- 定价按服务器/订阅：self-managed Enterprise X 约 $51,000/年起（3 节点，第三方挂牌价，2026-09 核）；SaaS Enterprise X $950/月起 + 计量消耗。

## 支撑报告结论

- "制品仓库/Registry 代理型"物种：检测能力寄生在 repository 上，策略执行点在"拉包"路径；air-gapped 交付是既有能力而非新增。
