# Source Note: GitHub — Dependabot alerts show vulnerable function calls (Python Beta)

- URL: https://github.blog/changelog/2022-04-14-dependabot-alerts-show-vulnerable-function-calls-python-beta/
- 标题: Dependabot alerts show vulnerable function calls (Python Beta)
- 发布方: GitHub Blog（官方 changelog，一手）
- 日期: 2022-04-14；抓取日期 2026-09-18
- 来源层级: 官方文档（厂商 changelog）

## 关键摘录 / 技术要点

- Dependabot alerts 使用 GitHub 的 "precise code navigation engine"（基于 stack graphs 的精确代码导航）判断仓库代码是否**直接调用**了漏洞相关的 vulnerable function，并在 alert 上展示。
- 2022 年 4 月以 Python Beta 上线。

## 支撑报告结论

- 第一部分：function-call 级 reachability 在主流平台上 2022 年已落地（GitHub 规模化 infra），说明其非稀缺技术；但 GitHub 方案只覆盖"直接调用 vulnerable function"提示，且多年未扩展到全语言（不确定最新覆盖范围，文档以 Python beta 为起点）。
- 结论：reachability 商品化证据之一。
