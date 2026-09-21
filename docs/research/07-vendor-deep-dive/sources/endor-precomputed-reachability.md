# Source Note: Endor Labs Pre-computed Reachability（官方文档，2026-09 快照）

- URL: https://docs.endorlabs.com/scan/sca/reachability-analysis/pre-computed-reachability
- 发布方： Endor Labs（官方文档）
- 抓取日期： 2026-09-21（页面快照日期 2026-09-08）
- 来源层级： 厂商官方文档

## 关键事实点

1. **定位**：manifest 级、无需构建的 reachability，两个用途——(a) full scan 构建失败/call graph 无法生成时的**默认自动 fallback**；(b) quick scan 的可选增强（`ENDOR_SCAN_ENABLE_PRECOMPUTED_CALLGRAPHS=true`）。
2. **算法（官方原文级描述）**：
   - 从 manifest（package.json/go.mod/pom.xml/build.gradle/Gemfile 等）解析完整依赖图；"Dependency resolution is required… but no build or compilation is necessary"；
   - **假设直接依赖全部可达**（"assumes that all functions and code in your direct dependencies are reachable"，含私有非 OSS 一方库）——保守近似；
   - 用 Endor **预计算的 OSS 包间调用图**判断直接依赖能否调到传递依赖中的漏洞函数；调不到则标 unreachable。
3. **分层精度体系（官方对比表述）**：function-level reachability = "the most precise… the primary and preferred method when builds succeed"；pre-computed = "pragmatic" 兜底。"Endor Labs automatically uses the best available analysis method for your situation."
4. **支持语言**：java、javascript、typescript、kotlin、python、scala、C#（7 个，少于 function-level 的 9 个）。
5. **自认局限**：
   - 不分析应用代码对传递依赖的**直接调用**（"does not analyze direct calls to transitive dependencies from your application code"）；
   - 聚焦传递依赖漏洞（理由：约 95% 漏洞在传递依赖中——引 Endor 自家 State of Dependency Management 报告）；
   - reachable 判定给出依赖内可能触发漏洞的函数调用列表，但证据粒度弱于 full call graph 的逐步 call chain。
6. 哲学自述："don't let perfect get in the way of better."

## 支撑报告结论

- 维度 2/10：Endor 的 reachability 是**三级降级体系**（function-level full call graph → pre-computed manifest 级 → dependency-level），构建失败不再是分析盲区；pre-computed 的精度代价 = 直接依赖全可达假设（系统性过近似）。
- 该设计间接证实：per-package-version 预计算 call graph 库存于服务端（OSS 集群），客户端构建失败时仍可查询——与 2022 博客"store + stitch"架构互证。
