# Source Note: JFrog Catalog 与数据底座（Catalog / OneModel / PostgreSQL 组件图）

- 来源层级：厂商官方文档
- 抓取日期：2026-09-21

## URL 清单

1. JFrog Catalog（2026-05-28 更新）: https://docs.jfrog.com/security/docs/catalog
2. Database and Third-Party Applications in Xray（2026-08-03）: https://docs.jfrog.com/installation/docs/database-and-third-party-applications-in-xray_xray-system-requirements-and-platform-support
3. JFrog MCP Server Tools（OneModel 工具）: https://docs.jfrog.com/integrations/docs/jfrog-mcp-server-tools

## 关键事实点

1. **Catalog 定位**（URL 1 原文）："JFrog Catalog acts as the **foundation for JFrog's security products**, providing enriched OSS metadata, vulnerabilities, dependencies, and license insights **before software is ingested** into a development pipeline"；数据由 JFrog Security Research 持续富化；集成 OpenSSF Scorecards；暴露 **Catalog GraphQL** 供批量自动化。
   - 下游消费方（交叉来源）：Curation 评估、Smart Remediation 候选版本、Zero-Touch Remediation 的 patched rebuild 识别与 CVE 对账。
2. **组件图存储**（URL 2 原文）：checksum-based components graph 存 **PostgreSQL**；队列 RabbitMQ。无公开专用图数据库证据——"图"是关系库中的图模型（Interpretation）。
3. **OneModel**（URL 3，Beta）："Build and execute GraphQL queries against the **JFrog OneModel unified data endpoint**"——平台级统一数据查询层的雏形（Hypothesis：长期可能成为跨 Artifactory/Xray/AppTrust 的 evidence graph 查询层）。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §8（数据底座）；§12-3（图 schema/规模未核实）。
