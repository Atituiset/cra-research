# Source Note: Oligo eBPF 深度应用观测（官方工程博客 + 媒体）

- URL: https://www.oligo.security/blog/not-all-ebpf-sensors-are-created-equal-why-depth-matters-in-runtime-security ；https://venturebeat.com/security/how-monitoring-libraries-rather-than-containers-is-key-to-open-source-security
- 标题: Not All eBPF Sensors Are Equal / Oligo Security raises $28M (VentureBeat)
- 发布方: Oligo Security 官方博客；VentureBeat
- 发布日期: 2025-06-10；2023-02-15
- 抓取日期: 2026-09-20
- 来源层级: 厂商工程博客 + 科技媒体

## 关键事实点

- Oligo 的 eBPF 探针不是只做 syscall/网络流式遥测，而是**把内核信号回溯到具体的函数/库粒度**（"traces each kernel signal back to the exact function, library"）——按库画像（library-level profiling）观测应用实际加载/执行了哪些库函数。
- 借此实现"证明哪些漏洞真实"：观测到 vulnerable function 被执行 ≠ reachability 推断，而是运行时实证（厂商叙事，[04 报告](../../04-technology-deep-dive.md) 已标注其合规声明为厂商声称）。
- 传感器为 eBPF-based engine，面向 Linux workload，强调 kernel-safe 与低开销（厂商声称）。

## 支撑报告结论

- 运行时层的业界实际栈：eBPF 是云原生 runtime 观测的统一底座，差异化在于**探针解读深度**（syscall 级 vs 库函数级 vs 应用语义级），而非是否用 eBPF。
