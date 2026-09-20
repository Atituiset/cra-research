# Source Note: NetRise Binary Composition Analysis（官方）

- URL: https://www.netrise.io/glossary/software-supply-chain-security/binary-composition-analysis-bca ；https://www.netrise.io/products/turbine
- 标题: What Is Binary Composition Analysis (BCA)? / NetRise Turbine
- 发布方: NetRise 官方
- 发布日期: 2026-06-30；2025-10-16
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方

## 关键事实点

- BCA 定义：直接检查编译后软件、无源码识别"实际运行的东西里有什么"——SBOM 从当前 build 产物（产品/固件）生成而非从 manifest 推导。
- 交付为 SaaS 平台（Turbine），分析对象包括二进制、容器镜像、设备固件。
- 生态信号：Manifest（SBOM 管理商）与 NetRise 合作把固件 SBOM 能力嵌入其平台（2025-11 官方新闻稿）——二进制识别能力开始被作为**上游组件**嵌入聚合型产品。

## 支撑报告结论

- 二进制识别能力正在"组件化"：专业厂商的分析引擎通过合作/API 进入 SBOM 管理平台，印证该层是技术壁垒、非每个平台都自建。
