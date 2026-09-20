# Source Note: Endor Labs — Reachability Analysis（产品文档）

- URL: https://docs.endorlabs.com/scan/sca/reachability-analysis
- 标题: Reachability analysis
- 发布方: Endor Labs（厂商官方文档）
- 抓取日期: 2026-09-18（页面标注更新 2026-09-08）
- 来源层级: 官方文档（厂商）

## 关键摘录 / 技术要点

- 提供三档 reachability：Function-level、Dependency-level、Pre-computed reachability。
- Function-level：full scan 要求**项目可成功构建**，生成完整 call graph；给出 Reachable / Unreachable / Potentially Reachable 三种标签。Potentially Reachable 的含义是"该语言或包管理器不支持 call graph 分析"——即承认覆盖有限。
- Pre-computed reachability：manifest-based，无需编译/构建，分析 direct dependency 如何使用 transitive dependency，作为构建失败时的 fallback。引用其 State of Dependency Management 报告：约 95% 漏洞存在于 transitive dependencies。
- Dependency-level：默认所有语言支持，粗粒度（包是否被使用）。
- Phantom dependencies：代码使用但 manifest 未声明的依赖，通过扫描实际代码使用情况识别。

## 支撑报告结论

- 第一部分：工业界 function-level reachability 依赖"可构建 + 全量 call graph"，构建失败时退化为 manifest 级近似（工程障碍证据）。
- 结论部分：reachability 是"工程壁垒"而非不可复制技术壁垒的证据之一（多厂商已实现并文档化分级）。
- 95% 漏洞在 transitive 依赖中 —— 支撑"为什么需要跨依赖 call graph 拼接"。
