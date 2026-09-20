# Source Note: Oligo Security — Runtime reachability（eBPF，loaded vs executed）

- URL: https://www.oligo.security/blog/loaded-vs-executed-libraries ；产品页 https://www.oligo.security/runtime-platform/runtime-vulnerability-management
- 标题: On Loaded vs. Executed Libraries During Runtime / Runtime Vulnerability Management
- 发布方: Oligo Security（厂商工程博客）
- 日期: 2024-02-28 等；抓取日期 2026-09-18
- 来源层级: 厂商工程博客

## 关键摘录 / 技术要点

- Oligo 用 **eBPF sensor** 观测 Linux workload 实际执行的 library function，区分 "loaded"（库被加载进内存）vs "executed"（函数真正被执行），以此证明漏洞是否真正可达/可利用，并可在 function/syscall 级阻断利用。
- 对 SCA 的批评：静态扫描对"依赖出现即告警"，无论库是否被加载、函数是否被执行。
- 层级化 reachability（引自 Coana 白皮书）：module-level（模块是否加载）→ function-level（函数是否调用）→ network-level（是否暴露到网络）。

## 支撑报告结论

- 第一部分：Runtime Telemetry / eBPF 是 reachability 方法谱系中的独立分支，可给出静态分析给不出的"实际执行"证据；但只覆盖已部署运行的工作负载，且观测窗口有限（未执行≠不可执行——与静态 unreachable 的对称局限）。
- 结论：runtime reachability 是真实存在的差异化能力（Oligo、Datadog、Contrast/Seeker IAST 类），但需要 agent 部署，CRA 制造商侧场景未必适用。
