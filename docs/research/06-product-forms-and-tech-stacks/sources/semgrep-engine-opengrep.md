# Source Note: Semgrep 引擎架构与 OpenGrep 分叉（官方文档 + 第三方）

- URL: https://docs.semgrep.dev/contributing/updating-a-grammar ；https://docs.semgrep.dev/faq/comparisons/opengrep ；https://appsecsanta.com/sast-tools/semgrep-vs-snyk
- 标题: How to upgrade the grammar for a language / Compare Semgrep to Opengrep / Semgrep vs Snyk
- 发布方: Semgrep 官方文档；AppSec Santa（第三方）
- 发布日期: 官方文档页 2026-09-14 更新；第三方 2026-05-10
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档 + 第三方交叉

## 关键事实点

- 引擎架构：核心模式匹配引擎 **OCaml** 编写；语言解析基于 **tree-sitter** 语法，经 `ocaml-tree-sitter` 代码生成器产出 OCaml 解析代码，再映射 CST → **generic AST**（跨语言统一中间表示），模式匹配在 generic AST 上进行——这是"一套引擎 30+ 语言"的关键设计。
- 许可与分叉（官方确认）：引擎自 2020 年起 **LGPL-2.1**；2024-12 规则仓库改 proprietary Semgrep Rules License（引擎许可证未变）；2025-01 多家厂商联盟 fork 出 **OpenGrep**（LGPL-2.1，Endor Labs 等参与维护），恢复被商业化的跨函数 taint 等能力。
- "引擎开源、规则与平台收费"是 Semgrep 的明确商业结构。

## 支撑报告结论

- 静态分析底座的业界实际栈：tree-sitter（CST）→ 语言无关 generic AST → OCaml 匹配内核，是"多语言 SAST 引擎"的被验证最省事路线；OpenGrep 事件说明"开源核心 + 商业平台"模式存在许可张力，新入场者可直接站在 OpenGrep/Semgrep CE 上。
