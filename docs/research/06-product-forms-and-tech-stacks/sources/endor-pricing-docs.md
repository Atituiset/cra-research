# Source Note: Endor Labs 许可模式（官方 docs）

- URL: https://docs.endorlabs.com/introduction/licenses （另见 https://www.endorlabs.com/pricing ）
- 标题: Endor Labs licenses / Pricing
- 发布方: Endor Labs 官方文档
- 发布日期: 页面最近更新 2026-09-11
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档

## 关键事实点

- 定价为 **seat-based，按 contributing developer 计**（"a developer who has made one or more commits"），按 **per contributor per year** 授权；每席位附带每日 scan credit 配额。
- 交付形态：SaaS 控制台；扫描可在客户 CI runner 内执行（代码不出边界，仅结果回传）；另有 **Endor Outpost** 可在 CI 之外定时跑 monitoring 扫描。
- 官方 pricing FAQ 明确 seat 定义因 SKU 略有差异（Endor Code / Endor Open Source）。

## 支撑报告结论

- 开发者平台型 SSCS 的"扫描在客户侧、结果上 SaaS"混合交付范式（降低源码出域顾虑）——CLI/agent 先行 + SaaS 控制台的标配组合。
