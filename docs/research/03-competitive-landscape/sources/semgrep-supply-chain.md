# Source Note: Semgrep Supply Chain / Assistant（官方+第三方）

- URL:
  - https://github.com/semgrep/semgrep（README：Supply Chain 支持 12 语言 15 包管理器）
  - https://semgrep.dev/blog/2024/semgrep-supply-chain-announces-dataflow-reachability-support-for-10-languages（2024-12-03：Scala/Swift 后达 10 语言 dataflow reachability）
  - https://semgrep.dev/products/product-updates/page/2（2025-06-24：业界首个 PHP reachability）
  - https://docs.semgrep.dev/semgrep-supply-chain/requirements-and-feature-support（2026-07-07）
  - https://semgrep.dev/blog/2025/semgrep-is-confidently-handling-60-of-all-triage-for-users-without-reducing-coverage（2025-09-10：Assistant 承担 60% triage）
  - https://safeguard.sh/resources/blog/semgrep-supply-chain-april-2026-update（2026-05：Guardian 自动升级 PR、dependency path 数据）
- 抓取日期: 2026-09-18
- 层级: 厂商官方文档/博客 + 第三方分析

## 关键事实点

- Semgrep Supply Chain：12 语言/15 包管理器；dataflow（函数级）reachability 2024-12 已达 10 语言，2025-06 新增 PHP（厂商声称业界首个）——**reachability 语言覆盖广度行业领先**。
- Semgrep Assistant：AI triage 与研究者决策一致率 95%+（厂商声称）；承担客户 60% SAST triage 工作（2025-09，厂商声称）；Memories 机制学习组织 triage 习惯。
- Guardian：依赖升级自动 PR（第三方评测）；2026-04 新增 dependency path 数据；Java/Kotlin 无 lockfile 支持 public beta（2026）。
- 模式：规则透明可编辑（YAML），与 ML 黑盒区分；CE 开源版免费。

## 支撑结论

- Semgrep 证明"跨语言 function/dataflow reachability"可做（10+ 语言），但它是 SAST 引擎复用路线的特例 → 创新空间不在"能不能做"，而在"证据化、产品化、与 VEX/合规打通"。
- Assistant 的 triage 自动化率是 AI 降噪商品化的标杆数据（厂商声称）。
