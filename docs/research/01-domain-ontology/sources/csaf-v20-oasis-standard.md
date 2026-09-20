# Source Note: CSAF 2.0 OASIS 标准原文

- **URL**: https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html
- **标题**: Common Security Advisory Framework Version 2.0（OASIS Standard, 18 November 2022）
- **发布方**: OASIS CSAF Technical Committee（Chair: Omar Santos/Cisco；编辑来自 Red Hat、德国 BSI 等）
- **发布日期**: 2022-11-18（取代 CSAF CVRF 1.2）
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方（标准原文）

## 关键摘录 / 事实点

1. Abstract 原文："the definitive reference for the language which supports creation, update, and interoperable exchange of **security advisories as structured information** on products, vulnerabilities and the status of impact and remediation among interested parties."
2. CSAF 是纯 JSON 格式（取代 XML 的 CVRF 1.1/1.2），配套 JSON Schema：csaf_json_schema / provider_json_schema / aggregator_json_schema。
3. **5 个 Profile**：1 CSAF Base、2 Security incident response、3 Informational Advisory、4 **Security Advisory**、5 **VEX**。
4. Profile 5 (VEX) 原文："The main purpose of the VEX format is to state that and **why** a certain product is, or is not, affected by a vulnerability." 要求：满足 CSAF Base + `/product_tree`（列出所有被引用产品）+ `/vulnerabilities` + 至少一个 product status 组。
5. 规范中 VEX 定义："enables a supplier or other party to assert whether or not a particular product is affected by a specific vulnerability, especially helpful in efficiently consuming SBOM data."
6. 规范性引用 NTIA VEX one-pager（2021-09-27）和 **CISA《VEX Status Justifications》（2022-05/06）** PDF。
7. 文档结构：`/document`（tracking、revision_history、distribution…）、`/product_tree`、`/vulnerabilities[]`（含 scores/cvss_v3、remediations、threats、flags、involvements、discovery_date 等）。
8. 生态角色：CSAF provider / CSAF aggregator / CSAF viewer —— 厂商以 provider 身份发布机器可读 advisory，aggregator 聚合。

## 支撑报告中的结论

- §12 CSAF 定义、维护方、profile 体系、与 PDF 公告的区别
- §12 CSAF VEX Profile 的结构要求
- §11 CISA VEX Status Justifications 的存在与出处（justification label 的官方来源）
- §16 披露/通报环节中 CSAF provider/aggregator 模型
