# Source Note: Xray air-gapped 知识库分发（DBSync v3 / offline-update）

- 来源层级：厂商官方文档
- 抓取日期：2026-09-21

## URL 清单

1. Xray Offline Database Sync（2026-08-17 更新）: https://docs.jfrog.com/security/docs/xray-offline-database-sync
2. Migration Guide: Upgrading from DBSync V1 to V3（2026-09-06 更新）: https://docs.jfrog.com/security/docs/migration-guide-for-self-hosted-customers-upgrading-from-dbsync-v1-to-v3
3. Smart Remediation（self-hosted Catalog 前提）: https://docs.jfrog.com/security/docs/smart-remediation

## 关键事实点

1. **命令与机制**（URL 1 原文）：JFrog CLI `xr offline-update`（alias `xr ou`）下载漏洞库更新；**`--license-id` 必填**（Xray license ID）；Xray UI 可辅助构建命令。
2. **DBSync v3 按流分包**（URL 1 参数表原文）：`--stream` 可取值 **`public_data` / `exposures` / `contextual_analysis`**；`--periodic`（默认 false）下载 "DBSync V3 Periodic Package"（须与 `--stream` 同用）。DBSync v1 才有 `--from`/`--to` 日期区间增量。
3. **v3 是现役机制**（URL 2）：存在官方 V1→V3 迁移指南（建议 off-peak 执行，"the migration process takes…"）。
4. **离线环境的能力短板**（URL 2 无，来自交叉来源）：
   - Contextual Analysis 的 **scanner 执行体不随 DBSync 分发**——官方文档 "Upgrade Required" 状态明确 self-managed 需升级 Xray 版本才能获得新 scanner（见 jfrog-contextual-analysis-engineering.md §B）；DBSync 的 `contextual_analysis` 流只更新数据。
   - Smart Remediation 在 self-hosted 明文要求 "you must have access to the **JFrog Catalog**"（URL 3），完全离线部署受限。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §3（air-gapped 分发）；§9（离线场景 ZTR/Remediation 折扣）；§10-8；§12-5（离线包完整性校验未核实）。
