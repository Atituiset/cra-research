# Source Note: Snyk Reachability（call path + Risk Score）与持续 monitor（本 note 供 03 报告 §6 使用）

- URL:
  - https://docs.snyk.io/manage-risk/prioritize-issues-for-fixing/reachable-vulnerabilities （Reachable vulnerabilities 页）
  - https://docs.snyk.io/developer-tools/snyk-cli/scan-and-maintain-projects-using-the-cli/monitor-your-projects-at-regular-intervals （snyk monitor 页）
- 发布方： Snyk（官方用户文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

1. **Reachability 提供 call path**（原文）："**Call path** - Allows you to see the path from your code to the vulnerable function to validate the result."（Project 页三要素：Filters / Reachability badge / Call path）
2. **Reachability 进入 Risk Score**（原文）："Risk Score helps you apply holistic Risk-Based prioritization that combines multiple factors, associated with either the vulnerability or the context of your application. **Reachability is such a contextual factor that will significantly increase the overall score.**" Risk Score 经 Projects 页、API、Reports 可得；legacy Priority Score 也计入 reachability。
3. **持续 monitor 在新 CVE 或状态变化时重新评估**（原文）：snyk monitor 上传依赖快照，"so Snyk can **notify you about newly disclosed vulnerabilities** in those dependencies, **or when a previously unavailable patch or upgrade path is created**"；同一 Project 多次快照只提示最新快照的新信息。
4. 该页同时确认分析管线五步（fix commit 富化 → DeepCode 相关元素分析 → NLP root cause 排名 → 应用 call graph 比对 → 安全专家校验），与既有 note [snyk-reachability-docs.md](snyk-reachability-docs.md) 一致。
5. **口径注意**：此页（manage-risk 旧路径）语言矩阵为 Java GA + JS/TS Early Access，比新路径页（scan-fix-and-prevent，2026-09-15 更新：Java/JS/Python GA、.NET EA）旧——以新页为准，本 note 仅取 call path/Risk Score/monitor 三个机制性表述。

## 支撑报告结论

- 二手声明 ③（Snyk Reachability 提供 call path 且进入 Risk Score；持续 monitor 在新 CVE 或状态变化时重新评估）**成立**，三点均有官方文档原文。
- "状态变化"的官方语义是"patch/upgrade path 从无到有"（fix availability 变化），不是漏洞状态机迁移——引用时注意。
