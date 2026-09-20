# Source Note: Renovate Merge Confidence + cargo-semver-checks（breaking change 检测的真实工具）

- URL 1: https://docs.renovatebot.com/merge-confidence/ （Renovate 官方文档）
- URL 2: https://github.com/obi1kenobi/cargo-semver-checks （开源项目）
- 抓取日期: 2026-09-18
- 来源层级: 官方文档 + 开源项目（一手）

## 关键摘录 / 技术要点

- **Renovate Merge Confidence**：通过分析 Mend Renovate 用户群的测试与发布采纳数据，标记"未声明的 breaking release"（undeclared breaking releases），给 PR 附 confidence 等级——用**群体采纳数据**而非静态分析来评估升级风险。
- **cargo-semver-checks**：扫描 Rust crate 的 semver 违规（基于 rustdoc JSON 的 API 差异 + 规则库，lint 式查询）。
- 同生态已知工具（常识级、真实存在）：Java 的 japicmp / revapi（二进制与源码 API 兼容）；Go 的 gorelease / go-apidiff；Python 的 griffe（API breaking 检测）； Rust 官方 Cargo 书有 SemVer Compatibility 章节定义何为 breaking。
- 已知局限线索：release-plz issue #2294 显示 cargo-semver-checks 对 rustdoc 格式版本敏感，失败可被误判为"API compatible"——工具链脆弱性的实例。

## 支撑报告结论

- 第三部分：breaking change / API compatibility 分析是"自动升级 PR"能否规模化的关键环节；现状 = 规则化 API diff 工具（确定性强但覆盖有限、对动态语言弱）+ 采纳数据驱动的 confidence（启发式）。语义级 breaking change（行为变化而非签名变化）基本无工具覆盖——适合 LLM 辅助但不可独立下结论。
