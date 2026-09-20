# Source Note: Wiz Runtime Sensor 与 agentless 双轨架构（官方 + 第三方对比）

- URL: https://www.wiz.io/blog/is-wiz-a-runtime-security-tool ；https://www.wiz.io/solutions/runtime-sensor ；https://www.armosec.io/blog/armo-vs-wiz-cloud-runtime-security/
- 标题: FAQs from the Field: Is Wiz a Runtime Security Tool / Wiz Runtime Sensor / ARMO vs Wiz
- 发布方: Wiz 官方博客/产品页；ARMO（竞品，带立场）
- 发布日期: 2026-07-06；2026-08-19；2026-07-06
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方 + 竞品视角（用于交叉验证架构事实）

## 关键事实点

- Wiz 基础架构 = **agentless**：通过云厂商 API 读取磁盘快照、云配置、API 数据，不在工作负载内装软件（新账号 15 分钟出首批发现，厂商声称）。
- 运行时补位 = **Wiz Runtime Sensor（eBPF）**：观测容器/K8s/VM/serverless 上"实际在执行什么"，用于 CDR/取证/威胁狩猎；官方自述模型为"agentless 打底 + 对值得加深观测的工作负载叠加 sensor"（竞品 ARMO 亦确认此架构，仅对深度有异议）。
- Sensor 强调 kernel-safe 架构与可忽略性能影响（厂商声称）。

## 支撑报告结论

- 运行时/云原生形态的业界收敛架构：**agentless 快照扫描（无代理、快覆盖）+ eBPF 探针（按需加深）双轨**；"装不装 agent"已从路线之争变成分层组合。
