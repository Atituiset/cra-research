# Source Note: JFrog Xray 架构（微服务、数据流、组件识别、触发点）

- 来源层级：厂商官方文档 + 官方 KB
- 抓取日期：2026-09-21

## URL 清单

1. Xray Service（六个微服务职责）: https://docs.jfrog.com/installation/docs/jfrog-xray-service （页面显示 Updated 4 months ago）
2. Database and Third-Party Applications in Xray: https://docs.jfrog.com/installation/docs/database-and-third-party-applications-in-xray_xray-system-requirements-and-platform-support （2026-08-03）
3. Index Xray Resources: https://docs.jfrog.com/security/docs/index-xray-resources （Updated 4 months ago）
4. KB - Why am I Seeing Different Scan Results Between JFrog Xray Scans: https://jfrog.com/help/r/xray-why-am-i-seeing-different-scan-results-between-jfrog-xray-scans （2025-12-02）

## 关键事实点

1. **六个微服务**（URL 1 原文）：Indexer（递归解包 artifact/build、收集元数据、构建组件图）、Persist（组件图与公共组件信息匹配、补全组件命名、**写入 PostgreSQL**）、Analysis（富化漏洞/许可证/版本元数据）、Server（API/UI、**DBSync 定时任务**、通知）、Policy Enforcer（扫描结果 × Watch/Policy → violation）、SBOM（管理/存储/富化 Xray 与 JFrog Security 其他产品的扫描结果）。
2. **第三方依赖仅三个**（URL 2）：PostgreSQL + RabbitMQ（HA 用 Quorum Queues，Classic Queue mirroring 将弃用）+ Erlang。
3. **组件识别是 checksum-based**（URL 2 原文）："Every artifact and build indexed by Xray is broken down into multiple components. These components and their interrelationships are represented in a **checksum-based components graph**. Xray uses PostgreSQL to store and query this component's graph." URL 4 印证："Xray extracts the components inside the artifact and performs **checksum-based analysis** against JFrog's vulnerability database."
4. **索引是扫描前提且显式 opt-in**（URL 3 原文）："Xray does not automatically scan all repositories, builds, or artifacts unless they are explicitly indexed." 三个可索引层级：Repositories / Builds / Release Bundles。
5. **上传即扫 + 新 CVE 反向定位**（URL 3 原文）："Indexed repositories allow Xray to scan artifacts **as they are uploaded or modified**"；"If a new CVE is discovered, Xray automatically identifies all indexed artifacts (within the defined retention period) that contain the vulnerable package."
6. **寄生关系**：Xray 部署于 JFrog Platform 内、要求 Artifactory（安装文档与第三方部署记录一致；router 初始化需先连 Artifactory 完成 join）。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §1（Xray 架构全部小节）。
- 与 03 报告的关系：03 只记录"依托制品仓库的天然覆盖"，本 note 给出机制层细节（checksum 图、opt-in 索引、事件驱动触发、扫描与执法分离）。
