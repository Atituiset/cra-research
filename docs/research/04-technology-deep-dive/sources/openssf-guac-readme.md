# Source Note: OpenSSF GUAC README（开源项目一手）

- URL: https://github.com/guacsec/guac/blob/main/README.md
- 标题: GUAC: Graph for Understanding Artifact Composition
- 发布方: guacsec / OpenSSF（孵化项目，Supply Chain Integrity WG）
- 抓取日期: 2026-09-18
- 来源层级: 开源项目（一手）

## 关键摘录 / 技术要点

- 定位："aggregates software security metadata into a high fidelity **graph database**——normalizing entity identities and mapping standard relationships"，支撑 audit/policy/risk management/developer assistance。处于供应链透明度模型的 "aggregation and synthesis" 层。
- 支持的输入文档：CycloneDX、SPDX、SLSA、in-toto ITE6、CSAF/CSAF VEX、OpenVEX、OSV、Deps.dev、OpenSSF Scorecard、Dead Simple Signing Envelope。
- 诚实声明："identifiers are not always available and **heuristics need to be used** to link them…may be unhandled edge cases and errors"——实体解析是图落地的真实难点。
- 架构：Collectors → (NATS) → Ingestor → GraphQL API，后端可插拔。
- **值得注意**：被项目承诺维护的、完整且优化过的后端只有 keyvalue（内存）和 ent+PostgreSQL；**Neo4j/openCypher 后端是 unsupported + incomplete**，arangoDB unsupported。即"供应链安全图"的旗舰开源项目在生产上并不依赖图数据库。

## 支撑报告结论

- 第四部分：GUAC 是"供应链元数据知识图谱"的最权威先例，证明图谱模型可行；但其后端现状说明"图"的价值在于**数据模型与查询语义（GraphQL 本体）**，而非图数据库技术本身——支撑"Evidence Graph 是数据模型壁垒而非数据库技术壁垒"。
- 启发式实体链接问题支撑"identifier/实体解析是工程难点"。
