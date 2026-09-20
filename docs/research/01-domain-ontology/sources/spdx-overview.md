# Source Note: SPDX 官方概览

- **URL**: https://spdx.dev/learn/overview/
- **标题**: SPDX Overview（SPDX 3.0）
- **发布方**: Linux Foundation（SPDX 项目）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方

## 关键摘录 / 事实点

1. SPDX = System Package Data Exchange（3.0 起改名，原为 Software Package Data Exchange），开放标准，用于跨域交换 BOM 信息（软件、AI、数据集、系统组件）。
2. "Originally focused on software licensing, security, and composition" —— **license compliance 是 SPDX 的历史起点**（SPDX License List 至今是其最广泛使用的部分）。
3. SPDX 2.2.1 即 **ISO/IEC 5962:2021**（免费公开的国际标准）；SPDX 3.0 是对 2.2.1 的重大修订。
4. 3.0 扩展领域：软件组成（Package/File/Snippet 三级粒度）、构建信息、AI 模型、数据集、Creator/Supplier/Distributor 身份、Provenance 与完整性（checksum/hash）、License 表达式、**Security Vulnerabilities 数据集成**、显式 Relationships、生命周期、Annotations。
5. 序列化：JSON-LD / Turtle / N-Triples / RDF/XML（3.0 转向 RDF/Linked Data 模型；2.x 时代还有 tag-value、spreadsheet 等）。
6. 明确声明不覆盖：无法通过检查包得出的信息、数据接收方如何使用、专利、license 法律解释。
7. 对齐 NIST SBOM 要求、ISO/IEC 标准、OpenSSF，获 OMG 背书。

## 支撑报告中的结论

- §10 SPDX 起源（license compliance）与 ISO 5962 地位
- §10 SPDX 3.0 能力范围（含 vulnerability 数据集成，但 VEX 表达弱于 CycloneDX）
- §10 SPDX vs CycloneDX 场景对比
