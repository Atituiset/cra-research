# Source Note: JFrog CRA Compliance Brief（官方 solution sheet）

- URL: https://jfrog.com/solution-sheet/cyber-resilience-act-jfrog-platform-compliance-brief/
- 标题: Cyber Resilience Act (CRA) JFrog Platform Compliance Brief
- 发布方: JFrog
- 抓取日期: 2026-09-18
- 来源层级: 厂商营销材料（solution sheet，含具体产品映射）

## 关键事实点

- CRA 时间线表述：Regulation EU 2024/2847，2024-12 生效；强制 24 小时报告义务 2026-09-11 生效；全面合规 2027-12-11；罚款上限 €15M 或全球营业额 2.5%。
- JFrog 定位映射（厂商声称）:
  - Curation/Catalog/IDE 插件 → "front door" 阻断不安全开源包，满足安全设计义务。
  - Xray/Advanced Security/Runtime → 自动化 SBOM + VEX（机器可读），支撑"每个 release 至少 5 年漏洞跟踪义务"；Contextual Analysis 识别"真正被利用的 CVE"以满足 ENISA 24h/72h/1 月三级报告时限。
  - AppTrust → Release Lifecycle Management（不可变 bundle 分级 promotion）、自动化证据收集（与二进制加密绑定、防篡改 chain of custody）、Policy as Code（OPA）做合规 release gate。
- 营销话术："Scanners check code, but the CRA regulates the product you ship: the binary"（厂商声称）——体现 JFrog 以制品/二进制为中心而非 repo 为中心的差异化叙事。

## 支撑报告结论

- JFrog 是最明确把 CRA 义务逐条映射到产品能力的厂商之一，且以 **release/二进制制品** 为核心对象（最接近 Product→Version 维度），但对象仍是"二进制制品/release bundle"而非"产品+版本+漏洞生命周期闭环"。
- 支撑"SBOM+VEX 生成已商品化"；AppTrust 证据收集是 evidence 方向的现有占位者。
