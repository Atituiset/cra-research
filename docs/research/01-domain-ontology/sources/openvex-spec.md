# Source Note: OpenVEX 规范仓库 README

- **URL**: https://github.com/openvex/spec
- **标题**: OpenVEX Specification（draft）
- **发布方**: OpenVEX 社区（起源于 Chainguard 等，OpenSSF 沙箱项目）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方（社区规范，draft 状态）

## 关键摘录 / 事实点

1. OpenVEX 定位："an implementation of the Vulnerability Exploitability eXchange (VEX) that is designed to be **minimal, compliant, interoperable, and embeddable**"。
2. 设计原则：满足 CISA SBOM/VEX 工作组定义的 VEX 最小要求；**SBOM Agnostic**（VEX 应独立于任何 SBOM 格式，且没有 SBOM 时也有用）；Minimal。
3. VEX 定义原文："a vulnerability document designed to complement a Software Bill of Materials (SBOM) that informs users of a software product about the **applicability** of one or more vulnerability findings."
4. 动机原文：扫描器会标记含漏洞组件，但软件"未必真的受影响"（已打补丁 / 代码不存在 / 无法执行）；供应商用 VEX 数据让扫描器关掉这类误报；SBOM 带来的透明度会使这类误报增多，"Hence VEX"。
5. 文档形态：JSON-LD，含文档元数据（@id、author、role、timestamp、version）+ `statements[]`；每条 statement = `{ vulnerability: {name: CVE-...}, products: [purl...], status: "..." }`。
6. 与 CSAF 对比：OpenVEX 更轻量、易于存入 Sigstore / 嵌入 in-toto attestation；CSAF 有丰富的 product tree 机制，OpenVEX 直接用 **PURL** 作软件标识。
7. 与 CycloneDX VEX 对比：OpenVEX 主张 VEX 元数据与 SBOM 分离；且指出 CycloneDX VEX 的 status/justification 标签集与 CISA VEX 工作组定义**不一致**，需要做标签翻译。
8. 工具链：go-vex 库、vexctl CLI（create/merge/attest）。

## 支撑报告中的结论

- §11 VEX 为什么出现（官方动机原文）
- §11 OpenVEX 文档结构真实示例
- §11 三种 VEX 实现（CycloneDX/CSAF/OpenVEX）的关系与差异
- §11 "VEX 是判断结果还是文件格式"：status label 集合（CISA 定义）+ 三种序列化实现
