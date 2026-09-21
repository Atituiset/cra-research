# Source Note: JFrog Contextual Analysis 官方文档（本 note 供 03 报告 §6 使用）

- URL: https://docs.jfrog.com/security/docs/contextual-analysis-of-cves-1
- 标题： Contextual Analysis of CVEs（JFrog Security / Advanced Security 文档）
- 发布方： JFrog（官方文档，页面显示 "Updated 13 days ago"，即约 2026-09-08）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

1. **不同 CVE 使用不同 scanner、多信号融合**（原文）："It runs a set of automated scanners, built and maintained by the JFrog Security Research team, that inspect multiple facets of your artifact to determine whether a CVE is truly exploitable: **first-party code usage of the library, binary compilation, configuration, invocation, and runtime environment**." 且 "A single scanner may combine several of the following techniques: Reachability / Binary symbols and strings / Configuration parsing / Command-line flags / Runtime environment"——每个技术附具体 CVE 示例（Jackson-Databind CVE-2019-14892、BusyBox CVE-2018-1000500、Apache HTTP Server CVE-2024-27316、curl CVE-2022-42915、glibc CVE-2020-1751 等）。
2. **"约三分之一 scanner 不依赖 reachability"（原文逐字）**："**Approximately one-third of JFrog's contextual analysis scanners deliberately don't rely on reachability**, because for many CVEs the evidence of exploitability never appears in source or binary code. It lives in configuration files, command-line flags, or properties of the host." FAQ 复现同一表述。
3. **每个结果带 justification**："The analysis produces a **justification** for every result, including which signals the scanner looked for, so you can learn and verify the finding against your code and environment."
4. **状态机**：Not Scanned / Applicable / Not Applicable / Undetermined / **Rescan Required**（"A new scanner for this CVE is available. You need to rescan to retrieve applicability results"）/ Not Covered / Technology Unsupported / Missing Context / Upgrade Required。
5. **Call chain 证据展示**（Transitive Dependency Analysis）：对每个 CVE 展示 direct/transitive call chain、call graph 可视化按钮、高亮函数与文件路径、**可复制函数名/文件路径/行号作为证据**（"A copy-to-clipboard option for evidence"）。
6. **覆盖规模**："already more than **1,600 high-profile CVEs**"有 contextual analysis scanner；优先 high/critical（CVSS ≥ 7.5）与在野利用 CVE。
7. **形态覆盖**：源码 + 编译二进制（Docker/OCI 镜像、Uber/Fat JAR）；Docker 中 Rust 二进制需 Xray 3.79.x+、.NET 需 3.95.4+。

## 支撑报告结论

- 二手声明 ①（不同 CVE 不同 scanner、五维信号）与 ②（约三分之一不依赖 reachability）**逐字成立**。
- **修正 03 §1.5 第 6 条**：原口径"非公开 call graph 粒度的 function 级证据"不准确——官方文档显示 Contextual Analysis 对覆盖的 CVE 展示 function 级 call chain 证据（含 transitive 视图与证据复制）。同时解决 00 报告 §18.2 的"粒度不可验证"口径差异。
- JFrog 是五家中唯一在官方文档层面承诺"每个判定带机器 justification（列出 scanner 检测信号）"的厂商——最接近 Evidence 层的产品化。
