# Source Note: Endor Labs 漏洞生命周期全链路官方文档核实（本 note 供 03 报告 §6 使用）

- URL（一组，均为 docs.endorlabs.com 官方文档 + 官网 use case 页）:
  - https://docs.endorlabs.com/scan/sca/reachability-analysis
  - https://docs.endorlabs.com/scan/sca/call-graphs
  - https://docs.endorlabs.com/risk-remediation/upgrade-impact-analysis
  - https://docs.endorlabs.com/risk-remediation/automated-pull-requests
  - https://docs.endorlabs.com/inventory-insights/sbom/exporting-sboms
  - https://www.endorlabs.com/use-case/sca-with-reachability （营销页）
- 发布方： Endor Labs（官方）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档（前 5 条）+ 厂商营销页（最后 1 条，相关声明标注"厂商声称"）

## 关键事实点（逐环节）

1. **Dependency Inventory**：SCA 以源码为 ground truth 扫描，覆盖 direct/transitive/**phantom dependencies**（代码用到但未在 manifest 声明的包）与 AI models，输出 SBOM（营销页 + reachability 文档 phantom dependencies 节）。
2. **Function-level Reachability（可追踪到具体 vulnerable function）**：官方文档定义三档标签——`Reachable Function`（"there is a path from the developer-written code to a vulnerable function… demonstrated by a call graph that illustrates each step between the source code and the vulnerable library"）、`Unreachable Function`、`Potentially Reachable Function`（call graph 不支持该语言/包管理器时的兜底）。另有 dependency-level reachability 与 pre-computed reachability（manifest 级、无需构建，作为构建失败时的 fallback）。
3. **Call path 证据**：call-graphs 文档确认 UI 展示 call path（"the sequence of function calls that connects your code to a specific function in a dependency"），**官方支持语言清单：Java、Python、Rust、JavaScript、Golang、.NET (C#)、Kotlin、Scala、Ruby（9 语言）**。
4. **Exploitability/Context**：文档表述 function-level reachability "is the most accurate way to determine exploitability in the context of your application"。
5. **优先级排序（EPSS + fix availability + production context）**：仅见于营销页（"Combine reachability with EPSS, fix availability, and production context to rank what to fix first"）——**厂商声称**，docs 中未见同等粒度的排序因子列表。
6. **Safe upgrade（含 breaking change 分析）**：Upgrade Impact Analysis 文档确认——升级建议评估"heuristic factors… + **program analysis to directly identify breaking changes**"；三档 remediation risk（High/Medium/Low）；breaking change 类别枚举（API/行为/传递依赖/deprecation/配置/平台支持变化）；文档明示局限（仅 OSS 包、不降级、不含容器/GHA 依赖等）。
7. **自动 PR**：docs 有专门页《Automated Pull Requests》（remediation PR 配置）；营销页称"automated pull requests that bundle related fixes"。
8. **SBOM/VEX 输出**：导出文档确认 CycloneDX/SPDX SBOM + VEX 三种格式，UI/REST API/endorctl 三通道；"A VEX export adds vulnerability exploitability status for those components"；CycloneDX SBOM 对 Endor Patches 组件带 **pedigree patch 数据**（上游版本、patch diff、resolves 的 GHSA 列表）。
9. 另一修复路径：Endor Patches——不升级时对传递依赖在构建期打补丁（营销页 "Patch transitive dependencies at build time when an upgrade is not practical"）。

## 支撑报告结论

- 二手声明所述 Endor 链路（Inventory→SCA→function-level reachability→context→EPSS/fix availability/production context 排序→safe upgrade→自动 PR→SBOM/VEX）**各环节均有官方材料支撑，整体成立**；唯一降级项是排序因子组合仅见营销页。
- 修正/补强 03 §1.10：reachability 语言覆盖从"覆盖广（厂商声称）"升级为官方文档 9 语言清单；SBOM 导出含 patch pedigree 是 Chainguard 之外的另一种"修复证据入 SBOM"实现。
