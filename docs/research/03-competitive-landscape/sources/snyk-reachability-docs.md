# Source Note: Snyk Reachability analysis（官方文档）

- URL: https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis
- 标题: Reachability analysis | Scan, fix, and prevent
- 发布方: Snyk（官方用户文档）
- 发布/更新: 页面检索日期显示 2026-09-15 更新
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方文档

## 关键事实点

- Snyk reachability = 判断应用是否调用了与漏洞相关的"代码元素"（function/class/module 粒度），支持显示 call path。
- 方法：修复 commit 提取 → DeepCode AI 程序分析识别相关代码元素 → NLP 排名 root cause → 应用侧 call graph 与依赖 call graph 比对 → 安全专家人工校验。
- 支持语言/包管理器（文档原表）:
  - Java (Maven, Gradle) — GA
  - JavaScript (npm, Yarn, pnpm) — GA
  - Python (pip, poetry, pipenv) — GA
  - .NET (NuGet, paket) — Early Access
- 状态值：`REACHABLE` / `NO PATH FOUND` / `NOT APPLICABLE`；文档明确警示 NO PATH FOUND 不等于不可利用（静态分析局限）。
- CLI 支持 `--reachability=true`（CLI ≥1.1301.0），JSON 输出含 `reachability` 字段；CLI/CI/CD 集成仍为 Early Access。
- Reachability 是 Snyk Risk Score 的上下文因子之一；JSON 输出同时含 EPSS(`epssDetails`)、exploit maturity、CVSSv4 等字段。
- 技术限制：30 万文件 / 3GB 上限；反射等动态行为会导致欠近似（文档明确承认 trade-off）。

## 支撑报告结论

- Snyk 的 reachability 为 function/code-element 粒度 + call path，属行业第一梯队；但语言覆盖仅 4 个（.NET 仍 EA）。
- Reachability + EPSS + exploit maturity + Risk Score = 商品化的风险优先级组合。
- 文档自身承认静态 reachability 的欠近似问题 → 支撑"跨语言/动态语言的 function-level reachability 仍是技术难点"。
