# Source Note: SLSA 官方站点

- **URL**: https://slsa.dev/
- **标题**: SLSA — Supply-chain Levels for Software Artifacts
- **发布方**: OpenSSF（Open Source Security Foundation）项目，跨组织厂商中立指导组
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方

## 关键摘录 / 事实点

1. 定义："a security framework, a checklist of standards and controls to **prevent tampering, improve integrity, and secure packages and infrastructure**."
2. 核心是 artifact **integrity/provenance**（保证你用的代码就是你以为的代码），分级 assurance levels，面向 producer/consumer/build platform。
3. 注意区分：SLSA 管"供应链防篡改与构建完整性"，**不管已知漏洞管理**——与 SBOM/CVE 体系是互补关系而非替代关系。

## 支撑报告中的结论

- §17 标准总表 SLSA 行（类型：供应链安全框架；生命周期位置：Build/Provenance）
- §1 知识地图中"供应链安全框架"与"漏洞管理"两条线的区分
