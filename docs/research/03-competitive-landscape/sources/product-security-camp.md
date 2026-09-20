# Source Note: Finite State & ONEKEY——产品安全/PSIRT 阵营（官方页面）

- URL:
  - https://finitestate.io/cra（Managed CRA Compliance Services，2026-03-27）
  - https://finitestate.io/use-cases/psirt-rapid-vulnerability-response（2026-02-06）
  - https://www.onekey.com/resource/cyber-resilience-act-sbom（2026-04-01）
  - https://www.onekey.com/role/psirt-manager
  - https://www.onekey.com/resource/onekey-webinar-psirt---start-small-but-start-cra-implications-on-notification-obligations（2026-08-17）
  - https://www.cyberresilienceact.eu/analysis.html（2026-09-11，"SBOM is a living artefact"）
- 发布方: Finite State / ONEKEY / cyberresilienceact.eu（社区站点）
- 抓取日期: 2026-09-18
- 来源层级: 厂商营销材料 + 第三方社区分析

## 关键事实点

- Finite State：定位"Product Security Automation Platform / Product Security OS"（厂商声称）；CRA 托管服务：从出货物生成 SBOM & VEX、运行网络安全风险评估、持续漏洞监控、起草披露与 CVD 策略；PSIRT 用例页明确"快速判定哪些**产品和 build** 受影响"。
- ONEKEY：Product Cybersecurity & Compliance Platform (OCP)，从**二进制镜像**生成/导入 SBOM、漏洞扫描、事件响应；PSIRT Manager 角色页："在**完整产品生命周期**中监控 SBOM 并接收更新"；威胁建模/自定义分析 profile/可接受风险定义。
- cyberresilienceact.eu（2026-09-11，即 Article 14 生效日）："SBOM 是活文档，在产品受支持生命周期内持续更新"。
- 共同特征：以**产品（product line/build/固件二进制）**为核心对象，面向设备/嵌入式/OT 制造商，CRA 是其主要需求驱动力。

## 支撑报告结论

- 定位空白判断的关键反方证据：Finite State/ONEKEY 已占据"以 Product 为核心对象 + CRA 证据"的位置，但集中在**嵌入式/IoT/固件**领域，技术路线是二进制分析而非源码 SCA，且无 function-level reachability / agentic remediation / 现代开发者工作流。
- 支撑 B 分析：空白在"现代化（源码+云原生技术栈）的 Product→Version 漏洞生命周期闭环"——两个阵营（AppSec 厂商 repo 中心 vs 产品安全厂商二进制/固件中心）中间存在断层。
