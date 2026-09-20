# Source Note: CycloneDX 规范概览

- **URL**: https://cyclonedx.org/specification/overview/
- **标题**: The CycloneDX Object Model（Specification Overview）
- **发布方**: OWASP Foundation（CycloneDX 项目）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方

## 关键摘录 / 事实点

1. 定位原文："a structured framework for representing information relevant for software and system transparency"，覆盖 vulnerability management、license compliance、cryptographic transparency、operational assurance。
2. 对象模型组成：**BOM Metadata**（supplier、manufacturer、target component、创建工具）→ **Components**（软件、硬件设备、ML 模型、源码、配置，含 license/copyright、pedigree/provenance）→ **Services**（外部 API、认证要求、信任边界、数据流）→ **Dependencies**（直接+传递依赖图，服务也可入图）→ **Compositions**（完整性声明：complete / incomplete / incomplete_first_party_only / incomplete_third_party_only / unknown）→ **Vulnerabilities**（内嵌已知漏洞及其 exploitability 声明，"making it ideal for both vulnerability disclosure and VEX use cases"）→ Formulation / Annotations（可签名）/ Definitions / **Declarations**（compliance-as-code：attestations、claims、evidence、签名）/ Citations / Extensions。
3. IANA 注册媒体类型：`application/vnd.cyclonedx+json`、+xml、protobuf；可带 `version=1.7` 参数。
4. 约定文件名：`bom.json` / `bom.xml` / `*.cdx.json` / `*.cdx.xml`。
5. OWASP 认定 `https://cyclonedx.org/bom` 为 in-toto 等 attestation 框架中 CycloneDX BOM 的官方 predicate type。
6. 支持多种 BOM 变体：SBOM、SaaSBOM、HBOM 等。

## 支撑报告中的结论

- §10 CycloneDX 对象模型结构拆解（含 vulnerabilities/VEX 内嵌能力）
- §10 SPDX vs CycloneDX 场景对比中 CycloneDX 一侧
- §11 CycloneDX VEX 实现方式（vulnerabilities 数组 + analysis.state/justification）
- §10 SBOM 内容清单（supplier/hash/license/relationship 等字段的出处）
