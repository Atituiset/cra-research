# Source Note: Dependency-Track 存储底座（企业工程博客 + 官方文档）

- URL: https://engineering.backbase.com/2026/04/14/dependency-track/ ；https://docs.dependencytrack.org/getting-started/configuration/
- 标题: Dependency-Track (Backbase 工程博客) / Configuration (官方文档)
- 发布方: Backbase Engineering；OWASP Dependency-Track 官方文档
- 发布日期: 2026-04-14；官方文档页更新 2026-09-14
- 抓取日期: 2026-09-20
- 来源层级: 用户方工程博客（一线落地）+ 厂商官方文档

## 关键事实点

- Backbase 生产部署：API Server + Frontend 容器 + **高可用 Aurora PostgreSQL** 作为 projects/findings/metrics 的持久存储。
- Dependency-Track 架构为 Java 单体（Alpine 框架/ORM），默认内嵌 H2，生产推荐外接 PostgreSQL——**纯关系模型，无图数据库层**；其"项目→组件→漏洞→VEX"的 portfolio 语义完全建在关系表上。
- 官方文档确认机密数据 AES256 加密后入库等企业部署细节。

## 支撑报告结论

- 业界存储底座判断的关键证据：连"供应链安全平台"中最接近图语义的 Dependency-Track 也跑在 PostgreSQL 上——与 [04 报告](../../04-technology-deep-dive.md) GUAC 用 Postgres 的发现互证，"图数据模型 ≠ 图数据库"在业界是普遍现实。
