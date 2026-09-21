# Source Note: Snyk reachability 演进时间线与 DeepCode 血统（多源汇编）

- URL:
  - https://snyk.io/blog/reachable-vulnerabilities/ （2020-08-18，Reachable Vulnerabilities 首发博客，Java）
  - https://snyk.io/blog/optimizing-prioritization-with-deep-application-level-context/ （2020-07-28）
  - https://updates.snyk.io/early-access-of-reachability-for-javascript-typescript-298264/ （JS/TS EA）
  - https://updates.snyk.io/reachability-for-python-is-now-available-in-ea-306203/ （Python EA）
  - https://updates.snyk.io/improvements-to-reachability-for-snyk-open-source/ （2025-10-16：Group 级批量开启 + Python EA 覆盖率"over 99% of applicable vulnerabilities"）
  - https://headwayapp.co/snyk-io-updates（Java Reachability Engine 升级公告："may see changes to existing vulnerabilities marking them as reachable"）
  - DeepCode 收购：2020-09-23 官宣（多家财经媒体转 Business Wire 稿；DeepCode 为 ETH Zurich spin-off，创始人 Boris Paskalev/Martin Vechev 团队）
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方博客/changelog（一手）；收购事实为公开记录

## 关键事实点

1. **时间线**：
   - 2020-07/08：Reachable Vulnerabilities 首发（Java，基于 call graph 判断 vulnerable function 是否被调用）——**先于 DeepCode 收购官宣**（2020-09-23）。首发博客强调"无需构建、静态 call graph"。
   - 2020-09：收购 DeepCode（ETH Zurich spin-off，symbolic AI / ML 语义代码分析），成为 Snyk Code 引擎底座；此后 reachability 文档统一表述为 "DeepCode program analysis engine"。
   - 之后：JS/TS EA → GA；Python EA（pip/poetry/pipenv）→ GA（2026 文档）；.NET（NuGet/paket）EA（2026-09 文档仍 EA）。
   - 2025-10：Group 级批量开启 + Python 覆盖率 >99%（applicable vulnerabilities 口径）。
   - Java Reachability Engine 升级公告自认：**引擎升级会把存量漏洞从 no-path 改判 reachable**，官方提示"may affect your triage and prioritization workflows"。
2. **底座判定**：官方文档明确用 "DeepCode AI program analysis / DeepCode program analysis engine"；**未见任何基于 CodeQL 的表述**（CodeQL 是 GitHub 系，竞品对比文章也只把 CodeQL 与 Snyk Code 对列）。结合 2026-09 文档新增的 "agentic capability... real-time decision-making"，引擎已从纯静态符号分析演进为"静态 + AI/agentic 决策"混合。
3. **粒度演进**：2020 年 "vulnerable function" → 2024 文档 "function related to the vulnerability" → 2026-09 文档 "**code element** (functions, classes, modules, and more)"——粒度词放宽意味着引擎对非函数级根因（类/模块级）也有覆盖（Interpretation）。
4. **语言覆盖口径注意**：Risk Score 文档（同期）仍写 reachability "supported for Java and JavaScript"，滞后于 reachability 专页（Java/JS/Py GA）——Snyk 文档内部存在更新不同步（自曝口径差）。

## 对本轮深挖的支撑

- 维度 2：自研（DeepCode 血统）而非 CodeQL；语言与粒度演进时间线；引擎升级导致结论漂移的官方确认。
