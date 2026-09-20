# Source Note: Semgrep — Reachability Analysis 白皮书（厂商白皮书，含竞品粒度批评）

- URL: https://semgrep.dev/assets/content/whitepapers/semgrep-reachabilityanalysis-whitepaper-1225.pdf
- 标题: Semgrep Reachability Analysis whitepaper (12/25)
- 发布方: Semgrep
- 抓取日期: 2026-09-18（未 fetch 全文 PDF，内容来自搜索引擎索引摘录，细节以原文为准——不确定）
- 来源层级: 厂商白皮书（立场性来源）

## 关键摘录 / 技术要点

- 核心论点："reachability analysis" 无标准定义；把 **package 级过滤称为 reachability 是过度包装**（"a generous interpretation"），只能筛掉最明显的发现。
- Function-level reachability 需要 dependency resolution + call graph 生成；full scan 慢、会延迟 PR merge——指出 Endor 类全量 call graph 方案的成本。
- 批评竞品的 "噪声减少" 数字基于完整应用扫描（慢）。
- Semgrep Supply Chain 自身提供 direct dependency 的 reachability（Java/JS/Ruby 等），基于其 SAST 引擎的跨文件数据流。

## 支撑报告结论

- 第一部分：粒度定义混乱是行业现状——"reachability" 从 package 级到 branch 级都被叫同一名字，评估壁垒必须先统一粒度口径。
- 反面证据来源：厂商互相揭短的文章恰好暴露了各自方案的工程限制（构建要求、扫描时长、覆盖语言）。
