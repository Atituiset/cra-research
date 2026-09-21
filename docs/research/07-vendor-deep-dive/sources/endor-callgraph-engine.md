# Source Note: Endor Labs call graph 引擎实现（2022 技术博客 + 官方文档 + JS 工程博客）

- URL（一组）:
  - https://www.endorlabs.com/learn/what-is-reachability-based-dependency-analysis （2022-12-21，技术博客，疑为 Georgios Gousios 署名体系）
  - https://docs.endorlabs.com/scan/sca/call-graphs （官方文档）
  - https://www.endorlabs.com/learn/why-reachability-analysis-for-javascript-is-hard-and-how-we-fixed-it （2024-12-17，工程博客）
  - https://scholar.google.com/citations?user=sl1ofC0AAAAJ （Duc-Ly Vu 学术主页，显示 Henrik Plate = "Security Researcher, Endor Labs，Verified email at endor.ai"）
  - https://docs.endorlabs.com/developers-api/cli/commands/scan （endorctl scan `--languages` 官方清单）
- 发布方： Endor Labs 官方（前三条、第五条）+ Google Scholar（人员佐证）
- 抓取日期： 2026-09-21
- 来源层级： 厂商技术博客/官方文档为主；学术主页为独立佐证

## 关键事实点

### 引擎架构（2022 博客，迄今最完整的自曝）

1. **选 static 不选 dynamic 的明确论证**：dynamic call graph "de facto precise"但"not complete"（单次执行）；static 是 over-approximation。"we chose static analysis… because **completeness is an absolute must for any downstream security analysis tasks**"。
2. **生态级扩展架构**："we create a call graph **per package version**, store those call graphs and then, given a client dependency set, we **stitch them on the fly**"——预计算 + 存储 + 按需拼接，是 reachability 可扩展性的核心设计。
3. **动态图做内部基准**："We also use dynamic call graphs internally to form benchmarks against which our call graphs are being measured and optimized."
4. **学统渊源**：文末致谢 "Much of the initial work described here was done at the first author's Software Analytics lab at the TU Delft and then, at a larger scale, by the **FASTEN project**"，引用 Boldi & Gousios "Fine-Grained Network Analysis for Modern Software Ecosystems"（ACM TOIT 2021）。
5. **自认不精确**："computing the call graphs is complex and inherently imprecise so there is always a risk of false positives… and false negatives… for security risk, false negatives can be problematic"；reachability 应被消费为"优先级"而非绝对结论。
6. Reachability = 从客户端出发的**前向**遍历；Impact analysis（升级影响）= 从目标函数出发的**后向**遍历——同一图数据支撑两个方向的产品功能。

### 官方文档 call-graphs 页

7. 数据源混合："uses both **source code and binary artifacts** to enrich the analysis… without a heavy reliance on test coverage"。
8. 规模声明：分析范围含 client + 依赖，"often comprising over 100 packages"；为"each project release **and all its dependencies**"生成 call graph。
9. call path 支持语言官方清单：Java、Python、Rust、JavaScript、Golang、.NET (C#)、Kotlin、Scala、Ruby（9 语言）。
10. **口径不一致**：endorctl scan 文档 `--languages`（call graph 生成）列出 "C#, Go, Java, JavaScript, Kotlin, Python, Rust, Scala, and TypeScript"——无 Ruby、拆出 TypeScript；两处官方文档语言清单存在出入（Ruby 的实际支持度存疑）。

### JS 工程博客（自曝实现难点）

11. **JS call graph 生成器为自研**："Through the development of Endor Labs' JavaScript call graph generator, Endor Labs has made some observations…"
12. 自曝三类丢边来源：
    - **匿名函数**：无名字，只能用"行号+offset"做映射，而"line numbers of offsets (oftentimes just white space) can change between dependency versions"——跨版本函数身份不稳定；
    - **函数指针/回调**："tracking function pointers statically is complex and requires a level of data flow tracking… leads to some **missed edges** in static call graphs compared to dynamic ones"；
    - **动态 import**：import 名可以是运行时值，"impossible to know statically"；module-level code 在 import 时即执行（JS 特有语义）。
    - NodeJS 嵌套 node_modules 解析逻辑须精确模拟才能定位"代码实际使用的依赖版本"，否则 phantom dependency 误判。
13. 降噪数字（厂商声称）：示例项目 124 findings → function-level reachability 过滤后 11（约 91%）；再叠加 EPSS(1%)+fix available+in production → 2。

### 人员佐证

14. **Henrik Plate**（Eclipse Steady / SAP 系 function-level reachability 学术血统，"Identifying Challenges for OSS Vulnerability Scanners" TSE 2022 作者之一）Google Scholar 显示 "Security Researcher, Endor Labs"，endor.ai 验证邮箱。结合 FASTEN 致谢，Endor reachability 栈的学术谱系清晰：FASTEN（生态级调用图）+ Steady（漏洞函数级可达性）。

## 支撑报告结论

- 维度 2：reachability 引擎**自研**（非基于 CodeQL/Soot 等现成底座的公开证据），核心架构 = per-package-version 预计算 + stitch-on-the-fly；证据输出 = UI 中逐跳 call path + CallGraphDataService API。
- 维度 10：JS 丢边、匿名函数跨版本映射、静态过近似/假阴性风险均为官方自认。
