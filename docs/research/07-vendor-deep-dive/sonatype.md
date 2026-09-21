# Sonatype 厂商深度技术调研（第二轮 Competitive Deep Dive）

- 调研日期：2026-09-21
- 前置基础：`docs/research/03-competitive-landscape.md` §1.4 / §6（本文件不重复已有结论，只加深与修正）
- 事实分级：【事实】=有一手来源；【厂商声称】=营销/PR 口径；【解读】=基于事实的推断；【假设】=推测，待验证
- 过程记录：[research-log-sonatype.md](research-log-sonatype.md)

## 0. 对 03 报告的两条重要修正

1. **Reachability 结论需要更新**。03 §1.4 记"Sonatype 无 function 级 reachability"——**已过时**。Sonatype Lifecycle 现有 Reachability Analysis：method 粒度（"应用代码是否调用了含已知漏洞的具体方法"），支持 **Java/JVM、JavaScript/Node.js、.NET**（.NET 为 IQ 203，2026-05 新增）；另有 **Reachability Evidence**（压缩调用路径展示，stacktrace 风格，**仅 Java**）。【事实】〔[help: Reachability Analysis](https://help.sonatype.com/en/reachability-analysis.html)；[sources/sonatype-reachability-analysis.md](sources/sonatype-reachability-analysis.md)〕
2. **AI 能力结论需要更新**。03 记"AI/Agent 弱"——需要细化：Sonatype 2025-2026 推出了 Sonatype Guide（AI-first，MCP Server 接入 Claude/Cursor 等 IDE）、Golden Pull Requests（策略驱动的自动修复 PR）、Automated Waivers（规则化自动豁免）。方向是"数据+策略驱动的自动化"，**不是** LLM agentic 修复闭环（区别于 Black Duck Signal / GitLab Duo）。【事实】〔[help: Sonatype Guide](https://help.sonatype.com/en/sonatype-guide.html)；[blog: Golden PR](https://www.sonatype.com/blog/golden-pull-requests-automating-trusted-remediation-without-breaking-builds)〕

## 1. 漏洞数据策展：流程、证据、进产品方式

### 1.1 研究流程（官方文档级）

Sonatype 官方"Sonatype Vulnerability Data"页披露了完整的数据生产流水线 【事实】〔[help: Sonatype Vulnerability Data](https://help.sonatype.com/en/sonatype-vulnerability-data.html)；[sources/sonatype-vulnerability-data.md](sources/sonatype-vulnerability-data.md)〕：

- **输入源**：NVD、GHSA、OSV、Friends of PHP、RustSec、HackerOne、ExploitDB、18+ Apache 项目、GitHub events、X/Twitter、博客、客户上报等；明确说"评估过付费数据源，认为质量/精度价值有限，因此自建"。
- **两级研究队列**：
  - **Fast-Track**：自动化系统每日处理各数据源；发现新漏洞后由研究员核实组件归属、一句话摘要、受影响版本区间；**一般 <24h 上线**（视严重性）。数据较薄。
  - **Deep Dive**：按优先级队列选取，做**源码级分析**，产出准确版本区间+详细解释+检测方法+修复建议；**一般 24h，离群最多 3 天**。Deep Dive **可能推翻** Fast-Track 的组件归属/CVSS/版本区间。
  - 另两类：Public Research（直接 ingest NIST CPE 标识）、Vendor Research（SBOM 中第三方 CPE 漏洞，需开启 Public Data Sources）。
- **进产品方式**：Data Services 持续更新，"研究完成即对后续 Lifecycle 扫描可见，无 refresh 延迟"；研究类型会作为**策略条件**暴露（Security Research Type 条件可按 Fast Track / Deep-Dive / Public / Vendor 过滤），漏洞详情面板有 Vulnerability Research Metadata（IQ 193+）。
- **自我纠偏机制**：NVD 标记 disputed/rejected 的漏洞，Sonatype 研究员复核后更新状态，**不再触发新扫描的策略违规**（旧报告保留可见）；持续重评旧数据，"删除不再相关的以减少假阳性"。

### 1.2 "比 NVD 更快更准"的可考证据

- **速度**："publishes detailed information on new vulnerabilities 10X faster than NVD"【厂商声称】〔[Sonatype Intelligence 产品页](https://www.sonatype.com/products/intelligence)〕。可独立佐证的结构性证据：2026 SSCR 发现 **2025 年 65% 的 OSS 相关 CVE 没有 NVD 评分**；Sonatype 用自有评分把可用 CVSS 覆盖从 35% 拉到 91%（第三方转述报告数据）〔[CyberDesserts 转述](https://blog.cyberdesserts.com/npm-security/)〕。
- **精度**：官方自曝"**92% 的众包/公开漏洞数据在深入研究后需要修正**"；Sonatype 研究员用 CVSS v4 自行打分（SONATYPE- 前缀 ID），并明说"与 NVD 分数不同是常见且预期的"【事实，官方文档】。2026 SSCR 量化：与 Sonatype 相比，NVD 的 CVSS 分数精确匹配率仅 4.4%，严重性分桶一致率 55.7%（44% 的 CVE 落在不同桶；61.3% NVD 偏高）【厂商报告数据】〔[SSCR 2026 PDF 镜像](https://www.wokb.cz/Report2/SSCR_2026_final.pdf)〕。产品页话术："1 in 7 CVEs scored by NVD differ from Sonatype by 3+ CVSS points"【厂商声称】〔[Lifecycle 产品页](https://www.sonatype.com/products/open-source-security-dependency-management)〕。
- 【解读】Sonatype 的"快"本质是**不等 NVD enrichment**：先用 Fast-Track 占位+自评分，Deep Dive 再修正。这套"先覆盖、后精修、可回改"的队列模型是策展工程化的核心资产，且修正历史通过"报告漏洞变少"的官方解释页间接可见。

### 1.3 ATML / 恶意包检测

系统名 **Release Integrity**（2019 起），60+ 信号（包年龄、作者历史、包内代码/bytecode 模式、命名相似度/仿冒、攻击者签名），ML/NLP 模型打分，可疑包进 quarantine 队列由 65+ 人研究团队人工复核，复核期间 Firewall 用户已被默认保护【事实，官方博客】〔[Meet the Developers (2021)](https://www.sonatype.com/blog/meet-the-developers-behind-sonatypes-automated-malware-detection-system-securing-open-source-supply-chains)；[AI/ML Insights (2023)](https://www.sonatype.com/blog/protecting-software-developers-with-ai-ml)；[sources/sonatype-malware-detection.md](sources/sonatype-malware-detection.md)〕。恶意包数据见 §6。

## 2. Lifecycle/IQ 策略引擎

### 2.1 Policy 模型（官方语义）

【事实】〔[help: Policy Constraints](https://help.sonatype.com/en/policy-constraints.html)；[sources/sonatype-policy-engine.md](sources/sonatype-policy-engine.md)〕

- 三层结构：**Policy → Constraint（OR 组合）→ Condition（ANY/ALL 组合）**。"policy 违规 = 任一 constraint 为 true"。
- Condition 目录极厚：CVSS（默认 v4 回落 v3/v2）、漏洞 Category（九值分类法：Data/Operational/Functional/Configuration/Test Code/Sample Code/Privileged/Malicious Code/Other）、CWE、**KEV 状态**、**EPSS 分数**（IQ 199 起 Firewall 也可评估 EPSS/KEV）、**Security Research Type**（按策展队列分级做策略！）、**Detection Type**（Primary/Secondary/AST/CPE Match/Unshaded/Other——可按"检测来源可信度"做策略）、License Threat Group、Relative Popularity（仅 Maven Central）、Age（按 Sonatype catalog 时间滚动 24h 计）、Hygiene/Integrity Rating、EOL（Maven/npm/NuGet/PyPI）、坐标/PURL、Dependency Type（Direct/Transitive/InnerSource）、**Derivative AI Model / AI Content**（AI 模型治理已进入策略引擎）。
- 策略类型自动归类（Security > License > Quality > Other 优先级）。
- 作用点分 stage：proxy（Firewall quarantine）/ develop / source / build / stage-release / release / operate；proxy 阶段动作 = Fail（隔离）/ Warn（邮件）/ No Action（仅审计）。

### 2.2 Quarantine 与 Waive 机制

【事实】〔[help: Firewall Quarantine](https://help.sonatype.com/en/firewall-quarantine.html)；[help: Waivers](https://help.sonatype.com/en/waivers.html)；[sources/sonatype-firewall-quarantine.md](sources/sonatype-firewall-quarantine.md)；[sources/sonatype-waivers.md](sources/sonatype-waivers.md)〕

- **Quarantine**：proxy 阶段 Fail → 新请求组件进隔离区，HTTP 403（NuGet 特例 409，因 NuGet 客户端把 403 硬编码为认证失败；Pub 用 451）。**只隔离新请求组件**——已在 proxy 缓存中的组件只审计不隔离（避免打断构建）；重新拉取才可能被隔离。
- **Fail-closed**：Firewall 服务不可用且 quarantine 开启时，新组件请求一律进隔离直到评估完成（官方明确"fail closed to limit risk"）。
- **Waiver 模型**：scoped 到 constraint/condition 单一组合（一个 waiver 不一定消除组件所有违规）；可挂层级（Application / Organization / Root Organization）+ 组件范围（单版本/全版本/全部组件）+ **过期时间**；八种 reason 枚举（含 **Not Reachable**——reachability 结论进入豁免理由）；Stale waiver 概念（scope 内当前无组件但仍激活，新组件落入即生效）。
- **Zero-tolerance 失效**：策略任一元素（条件/约束/数据，如 CVSS 从 6.5 变 5.8）变化 → 既有 waiver 自动失效需重建。这是 Sonatype 对"waiver 防漂移"的回答。
- **时序漏洞（官方自曝）**：time-based waiver 过期后组件重新违规，但**因已在仓库中不会被重新隔离**——要重新隔离需先删缓存。这是"前门拦截"模型的固有边界。
- **Auto Waivers / Automated Waivers**：规则化自动豁免低危/不可利用违规（2025-05 build-safe automation）【厂商声称 MTTR 提升 30%】；IQ 203 修复了一个 bug：CM 重评估曾丢失 reachability 标记导致 "Not Reachable" auto-waiver 失效（CLM-38947）——说明 reachability→auto-waiver 链路已产品化。

## 3. Firewall（registry 代理拦截）实现

【事实】〔[help: Repository Firewall](https://help.sonatype.com/en/repository-firewall.html)；[sources/sonatype-firewall-quarantine.md](sources/sonatype-firewall-quarantine.md)〕

- **架构**：IQ Server 驱动，挂在 proxy repository 层；支持 Nexus Repository Pro（3.38.1+）**和 JFrog Artifactory**（7.2.6+，SaaS 不支持）——即 Firewall 可与竞品仓库组合。**协议依赖 HTTP/1.1 的 human-readable errorPhrase，不支持 HTTP/2**（少见的硬实现细节披露）。
- **拦截语义**：见 §2.2。防 dependency confusion 有专门策略（Proprietary Name Conflict 条件：proxy 包名撞 hosted 私有包名即违规）。
- **生态覆盖**：npm/PyPI/Maven/NuGet/Go/RubyGems/Cargo/Conda/CocoaPods/Composer/Conan/CRAN/Pub/Swift/Docker/**Hugging Face 模型**（IQ 191+，按 .bin/.safetensors/.pkl 等扩展名拦截）/Raw 任意静态站点。
- **事件化**：IQ 203 起支持 **Webhook**（quarantine/block 实时通知，区分新隔离与重复尝试）+ Bulk Waivers。
- 【解读】Firewall 的本质是"把 SCA 评估前移到包管理器解析时刻"，它不要求改 CI、不依赖开发者装插件——这是 Sonatype 相对 Snyk/Endor 的结构性差异，也是它敢声称"发布即保护"的原因：检测在 Sonatype 侧完成，阻断在 registry 代理层完成，客户侧零集成。

## 4. SBOM/VEX 工作流工程细节

### 4.1 Annotated SBOM 的存储模型

【事实】〔[help: SBOM Manager](https://help.sonatype.com/en/sonatype-sbom-manager.html)；[help: SBOM Component Details](https://help.sonatype.com/en/sbom-component-details-view.html)；[sources/sonatype-sbom-storage-audit.md](sources/sonatype-sbom-storage-audit.md)〕

- **双件存储**：original SBOM（导入原文，只读，逐组件可检索的 Original BOM 视图）+ augmented SBOM（Sonatype 富化后），均**按 application version 归档**。"retaining the original SBOMs for compliance"。
- **漏洞三分区**：Disclosed（SBOM 自带但 Sonatype 不认识的组件漏洞）/ Sonatype Identified（Sonatype 数据命中，随 Continuous Monitoring 更新）/ Verification 状态（Sonatype Verified vs Unverified——承认"我们没有数据核实 SBOM 声明的漏洞"）。
- **VEX 注释 = CycloneDX analysis 块内嵌于 SBOM**（03 已确认），UI 级操作：Add/Edit/**Copy**/Delete Annotation。
- **Copy Annotation 的精确规则**（本轮新增）："copy the annotation for this component vulnerability **from the closest previous application version** where this vulnerability has been annotated"——**逐 component-vulnerability 粒度、从最近的已注释前版本拉取**；无前版本注释时 Copy 按钮不出现。即不是整份 SBOM 批量继承，而是逐条可选复制。【事实】
- "Create rules to scale and automate the VEX process"（SBOM Manager 能力清单语）——存在 VEX 自动化规则，但公开文档未见规则语法细节（不确定：规则能表达到什么程度）。
- SBOM 导入限制：某导入路径"only imports the components section…may not be VEX annotated"【事实，官方文档自曝】。

### 4.2 Audit 的持续监控机制（工程细节，本轮核心新增）

【事实】〔[help: SBOM Continuous Monitoring](https://help.sonatype.com/en/sbom-continuous-monitoring.html)；[help: Continuous Monitoring Best Practices](https://help.sonatype.com/en/continuous-monitoring-best-practices.html)；[sources/sonatype-sbom-storage-audit.md](sources/sonatype-sbom-storage-audit.md)〕

- **机制**：SBOM 初次分析后漏洞快照静态；Continuous Monitoring **每晚**（默认午夜，hosting server 时间）重评估，新违规触发通知。
- **SBOM Manager 版用独立 `Compliance` stage**，与 Lifecycle 的 CM 配置解耦；**监控所有 SBOM 版本，不限最新版**（CRA 意义上"历史在售版本"的正确方向）。
- **评估队列架构（完全公开）**：producer/consumer 异步队列，可跨实例分布。默认参数：producer 每 10min、最多排 1000 条；cycle 24h；每 tenant 1 个 consumer 线程、每 cycle 处理 30 条、排队条目 100min 过期重排。可通过 Configuration REST API 调参；每 consumer 线程约 +0.5–1GB heap。
- **Version Evaluation Window**：`maxVersions` / `maxAgeInDays`（如最近 5 个版本或 90 天内）限制评估范围——**这是"支持期"语义的雏形，但是通用窗口而非产品级支持期对象**。
- **吞吐上限（官方自曝）**：Lifecycle CM "约 2500 应用/天，一次扫一个应用，99% <2min，大组合可能需多天"；建议 CM 数据保留 ≤30 天。IQ 203 给 SBOM CM 加了"最新版本优先"排序以保证 24h 窗口内最重要的先出结果。

## 5. 对象模型：application/organization vs product/version

【事实+解读】〔[help: Organization Management](https://help.sonatype.com/en/organization-management.html)；SBOM Component Details〕

- IQ/Lifecycle 层级：**Root Organization → Organization（可嵌套）→ Application**；Application Category 作为横切标签做策略作用域（官方最佳实践：策略挂 Root，用 category 圈例外）。Application 是"团队正在开发的应用"的一一映射（CLM 文档），评估/报告挂在 application 的某次 scan/stage 上。
- SBOM Manager 层级：**Organization → Application → Application Version → SBOM（original + augmented）**——SBOM 绑定应用版本，组件详情面包屑为 org/application/file/import date。"closest previous application version" 表明版本有序。
- **离 CRA 粒度的距离**：版本是一级对象（SBOM 按版本存、CM 可按版本窗口监控、VEX 按版本间复制），比"repo/分支"模型（Snyk/Endor）更接近 CRA 的 product-version。但缺：产品线（product line）聚合、**支持期/EOS 语义**（version evaluation window 是运维参数不是合规声明）、上市状态、监管报告对象。Application ≈ 产品，但语义是"被扫描的软件"而非"投放市场的产品"。【解读】
- 【解读】Sonatype 的对象模型在"版本存续期漏洞重评估"上已具备 CRA 所需骨架（多版本监控+跨版本注释复制），缺的是把版本包装成"带支持期承诺的产品版本"这一层合规语义——恰是我们产品的空档机会。

## 6. 恶意包检测（2025–2026 数据）

【事实，均官方来源】〔[Q2 2025 Malware Index](https://www.sonatype.com/blog/open-source-malware-index-q2-2025)；[2026 SSCR 新闻稿](https://www.globenewswire.com/news-release/2026/01/28/3227372/0/en/Sonatype-Research-Reveals-OSS-Malware-Grows-75-as-Yearly-Open-Source-Downloads-Surpass-9-8-Trillion.html)；[sources/sonatype-malware-detection.md](sources/sonatype-malware-detection.md)〕

- 累计发现恶意包 **>123.3 万**（2026-01 SSCR 口径；Q2 2025 时为 845,204）。Q2 2025 单季 16,279 个（同比 +188%）；55% 为数据窃取型。
- **Firewall 拦截侧**：Q2 2025 单季阻断 88,150 次恶意包攻击（49% 指向政府/公共部门，31% 金融）；2024-04 声称累计避免 >$1.5B 损失【厂商声称】。
- 归因能力实例：107 个包归因 Lazarus Group（>30,050 下载）；Yeshen-Asia 活动在 Safety/OSV 公开 60 个之外**多发现 35 个**（基础设施关联：IP/邮箱域）——自有情报超出公共披露的可考案例。
- 检测方法：Release Integrity 60+ 信号+ML 打分→人工复核队列；"恶意包常被下架，无永久样本库，所以必须持续主动捕获"（自曝数据飞轮的原料逻辑）。2019-2023 确认恶意包 108,232 个→2026 达 123 万，飞轮效应明显。
- SSCR 2026 披露 AI 相关发现：分析 37K 条升级建议，**GPT-5 在无实时情报时有 27.8% 组件版本幻觉、并会推荐真实存在的恶意包**【厂商研究，含营销动机】；Sonatype Hybrid 策略升级成本比 latest-version 低 2.1×、比 LLM 推荐低 2.7×【厂商声称】。

## 7. AI / Agent

【事实】〔[help: Sonatype Guide](https://help.sonatype.com/en/sonatype-guide.html)；[Golden PR blog](https://www.sonatype.com/blog/golden-pull-requests-automating-trusted-remediation-without-breaking-builds)；[IQ 203 release notes](https://help.sonatype.com/en/sonatype-iq-server-203-release-notes.html)；[sources/sonatype-ai-golden-pr.md](sources/sonatype-ai-golden-pr.md)〕

- **Sonatype Guide**：AI-first 产品，MCP Server 接入 MCP-aware IDE/编码助手（Claude、Cursor 等），提供组件/漏洞搜索、实时扫描、版本指导、合规检查；另有 Guide API。定位：把策展数据喂给 AI 编码时刻（"grounding AI"），**不是修复 agent**。
- **Golden Pull Requests**：Golden Version = 解决该组件+传递依赖全部策略违规、无破坏性变更、符合组织策略的升级版本；自动开 PR（GitHub/GitLab/Bitbucket/Azure DevOps）。**关键限制：Golden Version 目前仅 Maven 生态**（IQ 203 起自动 PR 默认只为 Golden Version 生成=默认只覆盖 Maven；非 Maven 需 Source Control API 重新开启）。这是"规则+数据驱动"而非 LLM 生成 diff。
- **Automated Waivers / Build-Safe Automation**：规则化自动豁免。
- **策展中的 AI**：恶意检测 ML/NLP（§1.3）；漏洞发现用 ML 聚合关联公开源（§1.1）。
- 【解读】Sonatype 的 AI 路线是"**数据底座+策略引擎的自动化**"，刻意（或暂时）不做 LLM 代码改写；其叙事直接把 LLM 建议定位为风险源（幻觉/推恶意包），自家产品是"给 AI 纠偏的实时情报层"。对 agentic 修复浪潮是差异化对冲而非跟随。

## 8. 交付形态（self-hosted 传统、air-gapped）

【事实】〔[SAGE 页](https://www.sonatype.com/sonatype-air-gapped-environment-overview)；[help: Repository Firewall](https://help.sonatype.com/en/repository-firewall.html)；[sources/sonatype-sage-air-gapped.md](sources/sonatype-sage-air-gapped.md)〕

- 三种形态：Sonatype Cloud（托管）、self-hosted（单节点到多区域 HA）、**SAGE（Sonatype Air-Gapped Environment）**。
- **SAGE 官方页明确把 EU CRA 列入合规框架清单**（与 DoD RMF、CMMC 2.0、NIS2、DORA、ISO 27001、MOSA、NATO DPAP 并列）——03 报告记"未见专门 CRA 页面"，SAGE 是目前 Sonatype 唯一显式挂 CRA 的着陆点（注意：这是营销页级提及，非 CRA 专项方案）【厂商声称】。
- 部署细节：IQ Server + Nexus Repository + Data Service 以 **RPM / Docker / Helm chart** 安装；需自备 MySQL+PostgreSQL、NFS/S3 共享存储。**离线数据更新**：联网机器上用 Update Tools 每日下载数据包，摆渡进隔离网后用官方工具灌库（"有些客户已全自动此流程"）。
- 单体证据：IQ Server 从 H2 到 PostgreSQL 迁移、HA（ClusterLock、连接池调参 bug 修复）等 release notes 痕迹显示典型企业级 Java 单体+关系库架构【解读】。

## 9. 数据底座可考证据

【事实】

- **Maven Central 运营者**身份：86% 的 Maven Central 2025 流量来自 CSP（构建自动化），9.8T 年下载（四大 registry，+67% YoY）——遥测数据独家性成立〔[2026 SSCR 新闻稿](https://www.globenewswire.com/news-release/2026/01/28/3227372/0/en/Sonatype-Research-Reveals-OSS-Malware-Grows-75-as-Yearly-Open-Source-Downloads-Surpass-9-8-Trillion.html)〕。
- 组件情报规模：第三方口径 140M+ 组件追踪（AppSec Santa，未官方核实）；恶意包库 123 万+；漏洞记录研究样本 1.7 千/报告（SSCR 2026 方法节）。
- ABF（Advanced Binary Fingerprinting）：cryptographic hash + structural similarity + derived coordinate + file name，可识别改名/修改过的未声明组件（"as deployed" vs "as declared" 的差异化叙事）【厂商声称】〔[Intelligence 页](https://www.sonatype.com/products/intelligence)〕。
- 研究团队：65+ 研究员（2023 口径）。
- OSS Index / AuditJS 免费工具作为数据入口与社区漏斗。

## 10. 工程博客/官方文档自曝的局限

全部一手来源【事实】：

1. **Firewall 协议限制**：依赖 HTTP/1.1 errorPhrase，不支持 HTTP/2〔repository-firewall.html〕。
2. **Quarantine 只挡新增**：已缓存组件不隔离；time-based waiver 过期后组件留在仓库内不会重新隔离（要删缓存才行）——前门模型的覆盖缝隙由官方自己写明〔firewall-quarantine.html / waivers.html〕。
3. **NuGet/Pub 客户端怪癖**：NuGet 把 403 当认证失败，只能返回 409；Pub 返回 451〔firewall-quarantine.html〕。
4. **Reachability 边界**：仅 Java/JS/.NET；**Evidence 仅 Java**；容器 target 不支持；六种 Unknown 状态明示（含"漏洞无法映射到可调用方法"）；不配 namespace 时"每个方法都被当入口，调用路径又长又噪"〔reachability-analysis.html〕。
5. **Golden Version 仅 Maven**；自动 PR 默认因此只覆盖 Maven〔IQ 203 release notes〕。
6. **CM 吞吐**：~2500 应用/天、单应用串行、大组合多天扫完；SBOM CM 默认每 cycle 仅 30 条×1 线程，官方建议调参/限窗〔continuous-monitoring-best-practices.html / sbom-continuous-monitoring.html〕。
7. **数据自纠**：Fast-Track 数据会被 Deep Dive 推翻（组件归属/CVSS/版本区间可变），"报告里漏洞变少"需要官方 FAQ 解释；92% 公开数据需修正——既是卖点也暴露上游数据脏乱〔sonatype-vulnerability-data.html〕。
8. **SBOM 导入不保 VEX**：某导入路径只导 components 节、注释丢失〔sbom-import.html〕。
9. **Release notes 中的工程债痕迹**（IQ 203）：策略评估在连接池耗尽时死锁（CLM-39913）；CM 重评估丢失 reachability 标记致 auto-waiver 失效（CLM-38947）；CycloneDX 导入导出曾产出不合规格 SBOM（CLM-39030）；大负载下 OOM（EI-1273）〔IQ 203 release notes〕。
10. **CVE 搜索非通用**：只覆盖已 ingest 组件，"不是 NVD 通用查询"——数据底座覆盖边界自认〔sonatype-vulnerability-data.html〕。

## 11. 综合判断

- 【解读】Sonatype 的护城河结构：**registry 代理位（Firewall/Nexus）× 策展数据（Fast-Track/Deep-Dive/Release Integrity）× 策略引擎（细粒度 condition 目录）**三者互相咬合；SBOM Manager 是这套底座向"合规/审计"场景的延展，VEX 跨版本复制+多版本持续监控是其中最有 CRA 相性的部分。
- 【解读】对我们最有参考价值的三点：
  1. **版本级持续监控的工程化范式**：评估队列（producer/consumer、可调参、version evaluation window）是"CRA 支持期内漏洞重评估"的最小可行架构蓝本；但其 window 是运维参数——把窗口升级为一等产品语义（支持期承诺、EOS、监管报告）即差异化。
  2. **策展队列的"先覆盖后精修"模型**（Fast-Track 24h → Deep Dive 3 天 → 可回改+disputed 处理）值得借鉴；且 Sonatype 把 research type/detection type 暴露为策略条件，"按数据可信度做策略"是个被低估的设计。
  3. **Waiver 的 zero-tolerance 失效**（策略/数据一变 waiver 即失效）是防判定漂移的硬机制，比"建议定期复核"强；但其失效即静默，无"自动重估并通知"闭环（IQ 203 的 CLM-38947 显示这条链仍有 bug）——自动失效重估的行业空档（03 §3.3.6）在 Sonatype 处依然成立。
- 【假设】SBOM Manager 的 "Create rules to scale and automate the VEX process" 若实质是"按条件自动套注释"，则 Sonatype 比 03 报告的"VEX 纯人工标注"结论走得更远；公开文档未披露规则语义，待（Demo/试用）验证。
