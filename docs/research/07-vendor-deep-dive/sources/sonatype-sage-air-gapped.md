# Source Note: Sonatype Air-Gapped Environment（SAGE）与交付形态

- URL: https://www.sonatype.com/sonatype-air-gapped-environment-overview ；https://help.sonatype.com/en/repository-firewall.html
- 发布方： Sonatype（产品页=营销层；FAQ 部署细节具体）
- 抓取日期： 2026-09-21
- 来源层级： 厂商营销页（部署/数据更新机制描述具体可信；合规框架罗列属厂商声称）

## 关键事实点

1. **SAGE 合规框架清单明确包含 EU CRA**："operationalizes compliance of air-gapped development environments with the DoD RMF/CSRMC, the EU's Cyber Resilience Act (CRA), CMMC 2.0, NIS2, DORA, ISO 27001, MOSA, NATO DPAP"——03 报告"未见专门 CRA 页面"的修正点：CRA 出现在 SAGE 着陆点（营销页级，非专项方案）。
2. **目标市场**：国防/情报（NATO 及盟国）、关键基础设施、航空/半导体。
3. **部署形态（FAQ 原文）**：IQ Server + Nexus Repository + Data Service 以 RPM / Docker / Helm charts 安装；需自备 **MySQL 和 PostgreSQL**、NFS 或 S3 共享存储。
4. **离线数据更新（FAQ 原文）**："Administrators use Sonatype's Update Tools on an internet-connected machine to download data bundles **on a daily basis**. These files are transferred to the air-gapped network, then updates are applied to the databases using Sonatype provided utilities. Some customers have automated this entire process."
5. **三形态**：Sonatype Cloud（Firewall Cloud 自动更新）/ self-hosted（单节点至多区域 HA，"Built on the same platform as Lifecycle and SBOM Manager"）/ SAGE。
6. 侧面证据（release notes）：H2→PostgreSQL 迁移工具链、HA ClusterLock/连接池修复、air-gapped telemetry 缓存回退（NEXUS-53373）——企业级 Java 单体+关系库架构痕迹。

## 支撑报告结论

- 主文档 §8（交付形态）；CRA 营销策略的更新点（03 §1.4 第 2 条需补注）。
