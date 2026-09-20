# Source Note: GitHub — Copilot code review 新 public preview（agentic tool calling + CodeQL/ESLint）

- URL: https://github.blog/changelog/2025-10-28-new-public-preview-features-in-copilot-code-review-ai-reviews-that-see-the-full-picture/
- 标题: New public preview features in Copilot code review: AI reviews that see the full picture
- 发布方: GitHub Blog（官方 changelog，一手）
- 日期: 2025-10-28（编者注更新 2025-10-31）；抓取日期 2026-09-18
- 来源层级: 官方文档（厂商 changelog）

## 关键摘录 / 技术要点

- Copilot code review (CCR) 将 **LLM 检测 + agentic tool calling**（主动收集项目上下文：代码、目录结构、引用）与 **deterministic 工具（CodeQL、ESLint）** 结合。官方原话定位："This fusion of LLM intelligence and deterministic precision"。
- 修复路径：CCR 建议可直接 handoff 给 **Copilot coding agent**（@copilot 提及后自动在 stacked PR 中应用修复）。
- 二手来源（AI-LLM/Controversy 仓库引述）称 GitHub 公布 Autofix 2025 年修复 100 万+ 漏洞、修复速度约 3 倍于人工（SQL 注入 12 倍）——这两个数字需以 GitHub 官方材料为准（不确定，未在一手页面核实到原文）。

## 支撑报告结论

- 第三部分：主流平台级厂商的 remediation agent 架构实践 = "LLM 负责上下文聚合与补丁生成，deterministic engine（CodeQL/linter）负责检测与校验，human review merge"——正是本报告推荐的 agent 分工模式的一线证据。
