# Source Note: Aqua Tracee（开源 eBPF 运行时检测底座）

- URL: https://aquasecurity.github.io/tracee/v0.8.3/ ；https://github.com/aquasecurity/tracee
- 标题: Tracee: Runtime Security and Forensics using eBPF
- 发布方: Aqua Security 开源项目官方文档/仓库
- 抓取日期: 2026-09-20
- 来源层级: 开源项目一手

## 关键事实点

- Tracee = Aqua 开源的 Linux 运行时安全/取证工具：eBPF 采集 syscall、进程、文件、网络等内核事件，检测引擎把底层事件组合成 security event（如 fileless execution），可 K8s DaemonSet 部署。
- 三层模型：event（事实）→ security event（派生检测语义）→ policy scope；学术文献（arXiv 2026-09）将其与 Falco（CNCF graduated）并列为 eBPF 运行时安全事实标准。
- Aqua 商业 CNAPP 的运行时能力建立在 Tracee 之上（与 Trivy 对应扫描侧同构：开源核心 + 商业平台）。

## 支撑报告结论

- 运行时层的"开源底座 + 商业平台"范式与扫描层完全同构：Tracee/Falco/Tetragon 是公共底座，商业产品差异化在事件→安全语义的规则与上下文关联。
