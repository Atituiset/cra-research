# 厂商深度调研：JFrog（第二轮 Competitive Deep Dive）

- 调研日期：2026-09-21
- 定位：**加深**而非重复。基础事实（CRA Compliance Brief、Contextual Analysis 五维信号与"1/3 不依赖 reachability"逐字命中、Smart Remediation 双路径、Patched 状态、AppTrust 概览）见 `docs/research/03-competitive-landscape.md` §1.5 与 §6，本文不再复述，只记录**新增/加深/修正**的发现。
- 证据分级：**Fact**（官方文档/代码/工程博客可核实）｜**（厂商声称）**（营销页/新闻稿）｜**Interpretation**（基于 Fact 的推断）｜**Hypothesis**（待验证猜测）｜**（不确定）**。
- 每条重要事实的 URL 同时收录于 `sources/jfrog-*.md` source notes。

---

## 0. 一页结论

JFrog 是五家深度调研对象中**唯一把"判定证据"做成密码学对象**（DSSE/in-toto evidence）且**唯一把对象模型推进到 application 一级**（AppTrust 的 application/application version 实体，含 maturity_level 枚举值 `end_of_life`）的厂商。但其 exploitability 判定引擎（Contextual Analysis）本质上是**人工策展的 per-CVE 规则库**（1,600+ CVE，厂商自承"无法自动生成规则"），判定 justification 绑定 scanner 版本而非独立证据对象；证据链（Evidence）与漏洞判定（Contextual Analysis justification）在对象模型上**仍是两条未打通的线**。

---

## 1. Xray 架构：寄生关系、触发点、组件识别引擎

### 1.1 微服务与数据流【Fact】

Xray 由六个微服务组成，职责划分清晰（[Xray Service 官方文档](https://docs.jfrog.com/installation/docs/jfrog-xray-service)）：

| 微服务 | 职责 |
|---|---|
| Indexer | 递归解包 artifact/build、收集元数据、构建组件图表示 |
| Persist | 把组件图与公共组件信息匹配、补全组件命名、**把图数据与组件元数据写入 PostgreSQL** |
| Analysis | 富化组件元数据（漏洞、许可证、版本） |
| Server | API/UI 端点、**DBSync 定时任务**、通知 |
| Policy Enforcer | 把分析结果与 Watch/Policy 匹配生成 violation |
| SBOM | 管理、存储、富化 Xray 及 JFrog Security 其他产品的扫描结果 |

第三方依赖只有三个：**PostgreSQL（存组件图）+ RabbitMQ（队列，HA 用 Quorum Queue 镜像/复制）+ Erlang**（[Database and Third-Party Applications in Xray](https://docs.jfrog.com/installation/docs/database-and-third-party-applications-in-xray_xray-system-requirements-and-platform-support)）。

### 1.2 与 Artifactory 的寄生关系【Fact】

Xray 不能独立运行：部署在 JFrog Platform 内，**要求 Artifactory 存在**（初始化时 router 需先连 Artifactory 完成 join 流程，第三方部署记录与官方安装文档一致）。Xray 的扫描对象（repository/build/release bundle）全部是 Artifactory 资源——这既是它的天然数据源优势，也是它的生态锁定点。

### 1.3 扫描触发点【Fact】

- **索引是扫描的前提，且是显式 opt-in**："Xray does not automatically index all resources—you must enable indexing for a specific resource"（[Index Xray Resources](https://docs.jfrog.com/security/docs/index-xray-resources)）。三个可索引资源层级：Repositories / Builds / Release Bundles。
- **上传即扫**："Indexed repositories allow Xray to scan artifacts **as they are uploaded or modified**"（同上）——事件驱动，不是轮询。
- **新 CVE 反向冲击分析**：新漏洞入库后，Xray 自动在**保留期内的已索引 artifact** 中定位所有受影响者（同上）——这是 checksum 组件图带来的核心收益。
- **Watch/Policy 是 violation 生成器**：Policy Enforcer 微服务把扫描结果与 watch 规则匹配后才产生 violation 和阻断动作；扫描（识别+富化）与执法（watch 匹配）是两个独立阶段。

### 1.4 组件识别引擎：checksum 组件图，不是包管理器解析【Fact】

官方安装文档明确："Every artifact and build indexed by Xray is broken down into multiple components. These components and their interrelationships are represented in a **checksum-based components graph**. Xray uses **PostgreSQL** to store and query this component's graph."（[Database and Third-Party Applications in Xray](https://docs.jfrog.com/installation/docs/database-and-third-party-applications-in-xray_xray-system-requirements-and-platform-support)）

官方 KB 进一步确认匹配机制："Xray extracts the components inside the artifact and performs **checksum-based analysis against JFrog's vulnerability database**"（[JFrog KB: different scan results](https://jfrog.com/help/r/xray-why-am-i-seeing-different-scan-results-between-jfrog-xray-scans)）。

**Interpretation**：这意味着 JFrog 的组件识别**不靠解析 manifest/lockfile**（那是 CLI 侧 `jf audit` 做的事），而是把二进制递归解包后按文件 checksum 对照 JFrog 维护的"公共组件指纹库"做匹配。这正是它能扫 Docker 镜像任意层、Fat JAR、无 manifest 的裸二进制的原因；也是它对**重新编译/重新打包过的组件**（校验和变了）需要 Catalog/CPE 启发式兜底的原因——这一点未找到官方明文，**（不确定）**。

---

## 2. Contextual Analysis scanner 的工程实现

### 2.1 scanner 是人工策展的 per-CVE 规则，厂商自承无法自动化【Fact，工程博客自曝】

技术血统：Contextual Analysis 源自 2021 年收购的 **Vdoo**（设备/二进制安全公司），2022-02 作为收购整合的首个落地能力发布（[JFrog Q2 2021 财报电话会](https://www.fool.com/earnings/call-transcripts/2021/08/06/jfrog-ltd-frog-q2-2021-earnings-call-transcript/)；[DEVOPSdigest 2022-02](https://www.devopsdigest.com/jfrog-xray-adds-advanced-contextual-analysis-security-capabilities)）——这解释了其"从二进制/配置/运行时看问题"的视角与传统 SCA 厂商（从源码/依赖清单看问题）的差异。

2022 年 JFrog Security Research 官方工程博客（[78% 研究](https://jfrog.com/blog/turns-out-78-of-reported-cves-on-top-dockerhub-images-are-not-really-exploitable/)，该文是 Contextual Analysis 上线时附带的方法论文）直说：

- "**it is still impossible to automatically define the needed rules** for performing precise contextual analysis. Almost all vulnerability advisories do not contain formatted fields…that provide the information needed…what are the vulnerable functions or the vulnerable configuration of the affected component."
- "generic techniques…**will never give the needed accuracy that's possible only with a per-CVE contextual scanner**."
- "JFrog's contextual analysis is based on the **daily work of JFrog's security research team**, which analyzes each new vulnerability **on the same day it is disclosed**."

官方文档侧印证策展优先级机制（[Contextual Analysis of CVEs](https://docs.jfrog.com/security/docs/contextual-analysis-of-cves-1)，2026-09-03 更新）：

- 选 CVE 建 scanner 的三个因子：**JFrog 客户常用技术**、severity（主要 CVSS ≥ 7.5，无 CVSS 的用 ML 预测 severity）、**在野利用/媒体热度**。
- 覆盖量 "already more than **1,600 high-profile CVEs**"。
- **客户可以点单**："With a JFrog Advanced Security subscription, you can **request research** from the dedicated team. If a CVE lacks a contextual analysis scanner, the team prioritizes building support for it."

**Interpretation（策展成本估算）**：1,600+ scanner ÷ 2022-02 上线至今约 55 个月 ≈ 平均每月 ~29 个 scanner 的产能；相对每年 ~40k 个新 CVE，覆盖率天然只能瞄准头部高危 CVE。这是"规则库"路线的结构性上限，与我们产品若走"自动证据提取"路线的差异化空间。

### 2.2 scanner 的分发与版本化【Fact】

官方文档的状态机暴露了分发机制：

- **self-managed**：scanner 随 Xray 版本发布——"**Upgrade Required**: For self-managed environments, the **Xray version needs to be updated to receive a new scanner** for this CVE. A rescan is required after the upgrade."（[Contextual Analysis docs](https://docs.jfrog.com/security/docs/contextual-analysis-of-cves-1)）
- **SaaS**：scanner 自动部署，用户可能短暂看到 Upgrade Required 但无需动作。
- **Rescan Required**：新 scanner 可用后旧结果失效，需重扫拉取新判定——判定结果**绑定 scanner 版本**而非独立证据对象（03 §6 的结论在此得到机制层面的解释）。
- Xray self-managed release notes 可观察到 scanner 的迭代节奏，如 "Updated Contextual Analysis applicability scanners to support the Python 3.14 runtime"、"Java Contextual Analysis to detect call sites on generic types"（[Security Self-Managed Releases](https://docs.jfrog.com/releases/docs/security-self-managed-releases)）。
- DBSync v3 有独立的 `contextual_analysis` 流（见 §3），分发的是 CVE→scanner 的**元数据/覆盖清单**；scanner 执行体本身随 Xray 版本走。**（Interpretation：元数据走 DBSync、引擎走版本发布，这个二分由两个一手来源拼出，官方未一句话明说）**
- **CLI/IDE 侧**：`jf scan`/`jf audit` 首次运行自动下载 **Xray Indexer + Analyzer Manager 二进制（合计约 100MB）**（[CLI Command Summaries](https://docs.jfrog.com/integrations/docs/cli-command-summaries)；GitHub issue [jfrog-cli-security#592](https://github.com/jfrog/jfrog-cli-security/issues/592) 可见 analyzerManager 缺失报错路径）。即本地源码扫描的 scanner 引擎是**可独立下载分发的二进制**，不依赖服务端 Xray。

### 2.3 "不依赖 reachability"的那 1/3 用什么信号【Fact】

03 报告已记录五维信号框架；本次补上**每个技术的官方 CVE 示例**（docs 原文），它们精确展示了非 reachability 信号的形态：

- **Binary symbols/strings（编译时选项）**：CVE-2018-1000500 BusyBox `wget` 仅在以非默认 `FEATURE_WGET_OPENSSL` 编译时可利用。
- **Configuration parsing**：CVE-2024-27316 Apache httpd 仅在 `httpd.conf` 里 `LoadModule http2_module` 时可利用——官方原话点明 "**no amount of source-code or binary reachability analysis can determine exploitability, because Apache exposes no API to enable HTTP/2**"。
- **Command-line flags**：CVE-2022-42915 curl 仅在带 `--proxy` 且 scheme 为 `gopher://` 时可利用。
- **Runtime environment**：CVE-2024-3219（Python 仅 Windows）、CVE-2020-1751（glibc 仅 PowerPC）、CVE-2022-28321（PAM 仅 openSUSE Tumbleweed）、CVE-2024-45492（libExpat 仅 32 位二进制）、CVE-2022-4883（libXpm 要求 SUID 可执行文件调用）。

### 2.4 分析深度与自我声明的局限【Fact，工程博客自曝】

78% 博文罕见地坦白了实现取舍：

1. **保守偏好假阳性**："Prefer scanners that tend to show false positives…In the opposite case…[it] will be left vulnerable, which is a much more severe scenario." → Contextual Analysis 的 Not Applicable 判定**刻意保守**，其"降噪率"（78%）是保守设定下的数字。
2. **data-flow 分析只覆盖部分 scanner**：判断是否 attacker-controlled 只对"较容易"的 CVE 做数据流分析（如 CVE-2022-30630 `fs.Glob` non-constant input）；对文件类输入（CVE-2022-30631 gzip）放弃数据流、退化为"只要调用即报"。
3. **性能硬约束**：最精确的 scanner 需要"infinite call depth + inter-module calls"，"greatly increase the scanner's runtime"，在高吞吐（每分钟大量 artifact）场景下必须权衡——即**服务端 scanner 不是全程序分析**。
4. **只扫 first-party 代码**，理由有三：CPE 已覆盖 3rd-party 间调用、3rd-party 代码量远大于 1st-party、**专有 3rd-party 组件的许可限制**（"the 1st-party vendor may not have the approval to analyze the proprietary 3rd-party component"）。1st/3rd-party 区分借助 Xray SCA 能力做**文件级粒度**。
5. 文档状态机中 `Undetermined`（如需用户交互）、`Missing Context`（需放到 Docker 仓库里重扫才能定）坦承了静态判定的边界。

---

## 3. Air-gapped 知识库分发【Fact】

- 离线更新走 **DBSync v3**，按**流（stream）分包**下载：`public_data` / `exposures` / `contextual_analysis`，另有 `--periodic` 的周期性整包（[Xray Offline Database Sync](https://docs.jfrog.com/security/docs/xray-offline-database-sync)）。
- 工具是 JFrog CLI 的 `xr offline-update`（alias `xr ou`），**必须提供 Xray license ID**；Xray UI 可辅助生成命令结构。v1 支持按日期范围增量，v3 改为流+周期包模型。
- 存在官方迁移指南 "Upgrading from DBSync V1 to V3"（2026-09 更新，建议 off-peak 执行），说明 v3 是现役机制。
- **注意短板（Interpretation）**：scanner 执行体随 Xray 版本分发（§2.2），air-gapped 环境想拿新 scanner 必须**升级 Xray 本体**，DBSync 离线包只更新数据流。离线环境的 Contextual Analysis 覆盖永远滞后于 Xray 升级节奏。
- Smart Remediation 在 self-hosted 上还**额外要求能访问 JFrog Catalog**（见 §6.1），完全离线部署下该能力受限——官方前提条款明文列出 "To use Xray Remediation, you must have access to the JFrog Catalog"（[Smart Remediation docs](https://docs.jfrog.com/security/docs/smart-remediation)）。

---

## 4. AppTrust 证据链模型：evidence 的密码学实现

### 4.1 Evidence = DSSE 信封包裹的 in-toto statement【Fact】

`jf evd create` 的参数结构（[Create Evidence CLI](https://docs.jfrog.com/governance/docs/create-evidence-cli)，2026-05 更新）完整暴露了格式栈：

- predicate 是任意 JSON，**predicate-type 是 in-toto URI**，官方示例：`https://in-toto.io/attestation/link/v0.3`、`…/scai/attribute-report`、`…/runtime-trace/v0.1`、`…/test-result/v0.1`、`…/vulns`。
- 签名密钥支持 `rsa` / `ed25519` / `ecdsa`，PEM 与 SSH 格式；公钥以 `--key-alias` 注册在 Artifactory，创建时即做 **DSSE 验证**（缺公钥则 "created but not verified"）。
- **直接支持 Sigstore bundle 上传**（`--sigstore-bundle`，与自带密钥互斥），subject 可从 DSSE envelope 自动解析。
- MCP Server 的 Evidence 工具把这点说得更白：存在 "**Prepare a ready-to-sign in-toto statement** for a JFrog subject" 和 "Upload an already-signed **DSSE envelope** as evidence" 两个工具，且支持返回 **DSSE PAE（Pre-Authentication Encoding）字节**与 Markdown 渲染（[JFrog MCP Server Tools](https://docs.jfrog.com/integrations/docs/jfrog-mcp-server-tools)，Evidence 7.277+）。
- JFrog 还开源了 DSSE 相关组件：Go 包 `github.com/jfrog/jfrog-cli-artifactory/evidence/dsse`（EnvelopeSigner/Verifier/PAE）和免费的 [dsse.io 在线解码器](https://github.com/jfrog/evidence-extractor)（evidence-extractor 仓库）。

**Interpretation**：JFrog Evidence 在格式层**就是 in-toto/DSSE 生态的原生实现**，不是私造格式；其差异化不在格式，而在**存储与生命周期**（evidence 作为对象跟着 subject 走）。

### 4.2 Evidence 的组织与流转【Fact】

- subject 粒度五种：**artifact / package / build / Release Bundle v2 / application version**（[Create Evidence CLI](https://docs.jfrog.com/governance/docs/create-evidence-cli)）。
- **evidence 跟随 subject 穿越 promotion**：GitHub Actions 集成文档明确 "If you move your image from a 'dev' repo to a 'prod' repo within JFrog, **the Evidence follows the artifact automatically**"（[GitHub attestation to JFrog evidence](https://docs.jfrog.com/integrations/docs/github-actions-github-attestation-to-jfrog-evidence)）。Distribution 的 RBv2 分发也有 `include_evidence` 选项（MCP Distribution 工具）。
- **Evidence Graph**：Release Bundle 维度可视化 evidence/subject/关系图，可导出（[Evidence Solution Sheet, PDF](https://media.jfrog.com/wp-content/uploads/2024/12/23184548/JFrog-Evidence-Solution-Sheet.pdf)，（厂商声称））。
- **Evidence Ecosystem**：2025-09-09 起与 GitHub（build attestation）、ServiceNow、SonarQube、Anchore（Syft&Grype 参考实现）等十余家 partner 互通（[Business Wire](https://www.businesswire.com/news/home/20250909201600/en/JFrog-Extends-its-System-of-Record-Solution-Empowering-Application-Delivery-Governance-with-Evidence-from-World-Leading-Companies)；[Evidence Partners docs](https://docs.jfrog.com/governance/docs/evidence-partners)，含第三方工具 reference designs 的 GitHub 仓库）。
- 一个工程细节暴露缓存架构：**公钥从 Artifactory 删除后，Evidence 服务缓存最长 4 小时仍可用该密钥签名验证**（Create Evidence CLI FAQ）。

### 4.3 Trusted Release 与 gate【Fact（官方文档），部分（厂商声称）】

- AppTrust 文档：版本通过全部 policy gate 发布到生产后获得 **Trusted Release badge——"a cryptographically signed attestation stored in Artifactory that travels with the release as an immutable audit record"**（[AppTrust Overview](https://docs.jfrog.com/governance/docs/jfrog-apptrust)）。
- gate 用 **OPA/Rego** 实现，可按 application/project/组织全局定义，warn 或 block；每个事件（版本创建、promotion、policy 评估、release）记 timestamp+actor 入 Activity Log。
- "Immutable System of Record" 的不可变性具体靠什么（仅签名绑定还是 WORM 存储）文档未说明，**（不确定）**。

---

## 5. 对象模型：artifact/package/build → application 的跃迁

### 5.1 AppTrust 引入了 application 作为一等实体【Fact——相对 03 报告的重要更新】

[AppTrust Overview](https://docs.jfrog.com/governance/docs/jfrog-apptrust)（2026-06 更新）原文："AppTrust introduces the **application** as a **first-class entity** in the JFrog Platform. An application groups your packages, container images, and build artifacts under a single object with **defined ownership, business criticality, and maturity level**."

MCP Server 的 AppTrust 工具（[MCP Tools docs](https://docs.jfrog.com/integrations/docs/jfrog-mcp-server-tools)）暴露了精确的对象字段：

- **application**：`application_key`、`maturity_level`（枚举：`unspecified / experimental / production / end_of_life`）、`criticality`（`low/medium/high/critical`）、owners（user/group）、labels。
- **application version**：语义化版本号、sources（可来自 builds/packages/artifacts/release bundles/AQL/其他 app version）、`sign_key_name`；**release_status 三态：`PRE_RELEASE / RELEASED / TRUSTED_RELEASE`**。
- 生命周期：stage 间 promotion（move/copy/keep/dry_run）、rollback、release 到 PROD、Activity Log 全程审计。

**Interpretation**：这是 03 报告 §1.5"对象仍是'制品'"判断的**实质性演进**——AppTrust 的 application version 已有 owner/关键性/成熟度（含 `end_of_life`）三字段，**距离 CRA 的"产品线 + 支持期"语义只差一步**：`maturity_level=end_of_life` 是枚举状态而非带日期的支持期对象，没有"支持截止日、监管报告义务时间线"字段。但若 JFrog 加字段即可覆盖 03 §7 风险①（"若其把对象模型升级为产品线+版本+支持期则空白快速收窄"）——**该风险正在兑现中**。

### 5.2 CRA Brief 映射的粒度【Fact + Interpretation】

CRA Compliance Brief（03 已记录）把义务映射到 Curation/Xray/AppTrust 三件套；定价页显示 AppTrust 已有 **"pre-built CRA and NIST policy templates…one click…real-time compliance scoring"**（[pricing](https://jfrog.com/pricing/)，（厂商声称））。映射的对象粒度= **application version 的证据与 gate**，比 03 时的"release bundle"粒度又上移了一层。

---

## 6. Smart Remediation 与 Zero-Touch Remediation 的实现

### 6.1 Smart Remediation（Xray Remediation）算法细节【Fact】

[Smart Remediation docs](https://docs.jfrog.com/security/docs/smart-remediation)（2026-08 更新）比 03 记录的"双路径"丰富得多：

- **输入是 SBOM**：self-hosted 要求 `sbom.enabled: true` + `sbom.dependenciesEnabled: true`（Xray `system.yaml`），且**必须能访问 JFrog Catalog**。
- **三种选版本策略**：Quickest Fix（最小版本跳）、Least Vulnerable（最低风险分）、Best Version（四级优先级：policy-approved non-breaking → policy-approved breaking → 非 approved non-breaking → 非 approved breaking，每层内取最低风险分）。
- **风险打分权重**：Critical=10,000 / High=100 / Medium=10 / Low=1（ severity 间 100 倍级差）。
- **两条修复路径**：In-Lock override（传递依赖强制安全版本，Maven/npm/PyPI/Go/NuGet/Conan）与 direct 升级；容器侧是 **base image upgrade**（给 Dockerfile `FROM` 行；**不跨发行版推荐**，不会建议 Debian→Alpine；要求 base image 与本镜像在**同一 JFrog Platform**上都被扫过）。
- **明确的工程上限自曝**："only selects the **latest 500 versions** to prioritize from…partial results may happen"；全局免责 "Remediation suggestions represent **best-effort** recommendations and **may not be complete or fully accurate**"；`Curation Approved` / `Policy Approved` badge 标注 **Coming Soon**（策略联动尚未闭环）。

### 6.2 Zero-Touch Remediation：解析时替换，不是重建流水线【Fact】

[Zero-Touch Remediation Overview](https://docs.jfrog.com/security/docs/zero-touch-remediation-overview)（2026-09-06 更新）+ [Interpreting Remediation in Scan Results](https://docs.jfrog.com/security/docs/interpret-remediation-in-scan-results) 给出了完整机制，比 03 的"Catalog patched rebuild"一句话深入得多：

**Maven 路径（下载时拦截）**：build 请求原坐标 → Artifactory 问 Xray → Xray 查 Catalog 的 patched 候选（clearing-house vendor rebuild + 该 virtual repo 内注册的 local patch）→ **Least Vulnerable 策略**选最低分（权重 Critical×1,000,000 / High×10,000 / Medium×100 / Low×1；同分 **local patch 优先于 vendor rebuild**，再平手按 automation 的 vendor priority）→ 从同一 virtual repo 给出 patched 版本 → Xray 记审计。找不到合适候选则给原始 artifact（**不阻断**——阻断仍是 Xray/Curation 的职责）。

**npm 路径（lockfile 改写，非 tarball 拦截）**：JFrog CLI 把 `package-lock.json` 发给 Xray → Xray 返回改写后的 lockfile（patched 版本 + 指向同一 virtual repo 的 `resolved` URL + 按 Artifactory 内 artifact 计算的 integrity）→ npm install 装 patched tarball。**标准 `npm install` 不触发 healing，必须走新版 JFrog CLI**；`package.json` 里声明的仍是原版本。

**fix 来源生态（clearing-house vendors）**：Chainguard（仅 Maven）/ Echo / TuxCare / Seal Security；vendor 参与的前提是其 remote repo 挂在被覆盖的 virtual repo 下。Chainguard 官方 changelog（2026-09-02 上线，"Chainguard Libraries in JFrog…**this is what underpins JFrog's Zero-Touch Remediation**"）从对侧印证了这个 OEM 关系（[Chainguard changelog](https://edu.chainguard.dev/chainguard/changelog/)）。

**local patch 注册**：`POST /xray/api/v1/ztr/patches` + **CycloneDX 1.6 声明**；仅 Maven；无 UI，需 Manage Data 权限；要求 artifact 已在 Xray 索引的 local repo 中。

**Patched 状态闭环（加深 03 §6④）**：Patched 显示的前提是"Catalog 识别该 served 版本为 patched rebuild 且 Catalog 数据确认该 CVE 在该确切版本已修复"；local patch 时 Catalog 存注册时的 CycloneDX 声明并对自定义版本重打分。审计视图把事件分 **Healed / Skipped / Not required** 三类。官方文档罕见地给出设计理由四条（evidence of value / scanner reconciliation / auditability / developer trust）——其中 "scanner reconciliation" 一条承认**第三方扫描器会对同一坐标报出与 Xray 不同的 CVE 数**，JFrog 选择用 Patched 状态"reframe 差异"而不是隐藏。

**Interpretation**：ZTR 的本质是**把修复动作从"改源码仓库"（PR 路线：Snyk/Dependabot/Endor）搬到"改制品解析结果"（仓库代理路线）**——只有掌握解析层（Artifactory virtual repo）的厂商能这么做，这是 JFrog 寄生架构的护城河兑现。代价：修复发生在构建解析时，**源码仓库里的依赖声明不变**，离开 JFrog 仓库的环境（开发机直连公网、部署到其他 registry）不享受该保护。

---

## 7. AI / Agent 叙事

【Fact（官方文档/代码）与（厂商声称）混合，逐条标注】

1. **官方 MCP Server 已成体系**（[MCP Tools docs](https://docs.jfrog.com/integrations/docs/jfrog-mcp-server-tools)）：工具集覆盖 Access/Artifactory/Security/Curation/Distribution/Workers/OneModel/Event/**Evidence/AppTrust**；值得注意的是 **Curation waiver 审批**（approve/reject，强制 justification）和 **Evidence 创建/验签**都开放了 agent 可调用接口——即 agent 不只是读数据，还能执行治理动作。`OneModel` 工具暴露统一 GraphQL 端点供 agent 自由查询（Beta）。
2. **Multi-agent 支持**（[pricing](https://jfrog.com/pricing/)）：Claude、Codex、Cursor、Devin、VS Code、IntelliJ、Copilot、OpenCode、Kiro——agent 在 JFrog 策略内走"可信解析路径"。
3. **swampUP 2025（2025-09-09）一批发布**（[Business Wire: agentic remediation](https://www.businesswire.com/news/home/20250909861213/en/DevSecOps-in-the-AI-Era-JFrog-Powers-Agentic-Remediation-with-Self-Healing-Software-Supply-Chain)；[SiliconANGLE](https://siliconangle.com/2025/09/09/jfrog-unveils-ai-era-platform-upgrades-software-supply-chains/)）：**JFrog Fly**（"行业首个 agentic repository"，零配置，MCP 对接 Copilot/Claude Code/Cursor）、**Self-Healing Software Supply Chain**（agentic remediation，MCP+GitHub Copilot 直连修复工作流）、AI Catalog、AppTrust、Evidence Ecosystem。（厂商声称，新闻稿）
4. **swampUP 2026（2026-09）续作**：ZTR 演进为 "**Compliant Version Replacement**（坏版本流水线中途换掉）"；**Agent Guard**——把 Artifactory 治理延伸到 AI agent 的插件/资产（[devops.com](https://devops.com/jfrog-moves-to-secure-agentic-engineering-workflows/)）。（厂商声称/媒体报道）
5. **Policy-as-Code Playground**：自然语言 → Rego 策略的 AI 辅助工作台，定义后可对真实 application version 预验证（[pricing](https://jfrog.com/pricing/)）。（厂商声称）
6. **Agent 行为证据化**：AppTrust "Automatically capture agent interactions and generating a **signed evidence chain** from commits, PRs, and Jira tickets, attached to every application version"（pricing 页）。**Interpretation**：这是把 AI agent 的开发行为本身纳入证据链——CRA 语境下"谁/什么写了这段代码"的可审计性，全行业罕见。

**Interpretation（AI 叙事总评）**：JFrog 的 AI 路线不是"用大模型做判定"（Contextual Analysis 依然是人工规则），而是**把平台能力 MCP 化卖给别人的 agent**（Fly = agent 的制品仓库；MCP Server = agent 的工具箱；Agent Guard = agent 的治理）。与其判定引擎的保守哲学一致。

---

## 8. 数据底座【Fact + Interpretation】

- **组件图存 PostgreSQL**（§1.4，官方明文 "checksum-based components graph…PostgreSQL"）；队列 RabbitMQ；无公开的专用图数据库证据。**Interpretation**：所谓"组件图"是关系库里的图模型，不是 Neo4j 类图库——亿级边规模下的递归查询性能由 checksum 索引与物化结构承担，具体模式未公开（不确定）。
- **JFrog Catalog**：集中式 OSS 包+CVE 元数据服务（JFrog Security Research 持续富化），是所有安全产品（Curation 评估、Remediation 候选、ZTR patched 识别）的数据底座，暴露 GraphQL API（[Catalog docs](https://docs.jfrog.com/security/docs/catalog)）。
- **OneModel**：平台级统一 GraphQL 数据端点（MCP 工具，Beta）——**Hypothesis**：OneModel 是 JFrog 把 Artifactory/Xray/AppTrust 各服务数据模型统一的进行中项目，长期可能成为其 evidence graph 的查询层。

---

## 9. 定价 / 部署形态【Fact（官方定价页，2026-09-02 抓取）】

| 层 | SaaS | Self-hosted |
|---|---|---|
| Pro（纯 Artifactory DevOps） | $150/月（限时 $50） | — |
| Enterprise X（HA + Advanced Security 含 Contextual Analysis） | 起价 $950/月 | — |
| Pro X（self-hosted 入门） | — | **起价 $27,000/年，1 server** |
| Enterprise X（self-hosted） | — | **起价 $51,000/年，3 servers（HA）** |
| Enterprise+ | 联系销售 | 联系销售（多年合同可选） |

- 安全能力打包成 **Security Bundles：Unified / Ultimate**；**AppTrust（DevGovOps）只在 Ultimate**；Zero-Touch Remediation 两档都有（[pricing](https://jfrog.com/pricing/)）。
- Self-hosted 最低一年合同。
- **Interpretation**：Contextual Analysis / AppTrust / ZTR 全部收在付费高层级——JFrog 的免费/低价层没有 CRA 叙事所需的任何差异化能力，其 CRA 方案是典型 enterprise upsell。Self-hosted 传统强项仍在（air-gapped DBSync + self-managed 全功能），但 ZTR 依赖 vendor remote repo、Smart Remediation 依赖 Catalog 访问，**离线场景两者都打折扣**。

---

## 10. 工程博客/文档自曝的局限（汇总）

1. Contextual Analysis **规则无法自动生成**，靠研究团队逐 CVE 人工策展（§2.1）。【Fact】
2. **刻意偏好假阳性**，"applicable" 判定保守膨胀（§2.4-1）。【Fact】
3. 数据流分析有限覆盖；无 infinite call depth / 跨模块分析（§2.4-2,3）。【Fact】
4. 不扫 3rd-party 代码的调用，部分因**许可限制**（§2.4-4）。【Fact】
5. Smart Remediation：500 版本截断、best-effort 免责、策略联动 badge Coming Soon（§6.1）。【Fact】
6. ZTR：不阻断、仅 Maven/npm、npm 必须走 JFrog CLI、源码声明不变（§6.2）。【Fact】
7. Evidence：公钥删除后 4 小时缓存窗口仍可验签通过（§4.2）。【Fact】
8. Air-gapped：scanner 更新必须升级 Xray 本体；Smart Remediation 需要 Catalog 连通（§3）。【Fact】

---

## 11. 对我们产品的启示

1. **"判定证据对象化"是 JFrog 也没做完的事**：JFrog 有两套证据——Evidence（in-toto/DSSE 签名对象，绑 artifact/application version）与 Contextual Analysis justification（scanner 输出文本，绑 scanner 版本），二者在对象模型上未合一。我们的 Evidence Graph 若把 exploitability 判定**本身**做成可签名、可版本延续、可挂到 VEX statement 的 claim-evidence 对象，恰好落在 JFrog 两条线之间的空档。
2. **解析时修复（ZTR）证明了"不改源码的修复路径"有真实市场**，但它的前提是拥有仓库代理层。我们若不掌握解析层，可复制其**状态设计**而非机制：Patched 状态 + Healed/Skipped/Not required 审计三分 + "第三方扫描器对账"叙事，是修复后验证环节的产品化模板（也印证了 03 §6 结论：修复→重扫→VEX 自动流转全行业没人闭环）。
3. **CRA 对象粒度竞赛已经开始**：AppTrust 的 application/application version（ownership、criticality、maturity 含 end_of_life、TRUSTED_RELEASE 三态）把 03 报告 §7 的风险①兑现了一半。我们的窗口在于带**支持期时间轴、监管报告义务、判定证据链**的产品版本语义——JFrog 目前是"成熟度枚举"，不是"支持期对象"；但它加字段的速度会很快，且其 CRA policy templates 已一键化。

## 12. 无法核实项清单

1. checksum 组件图对**重编译/重打包组件**（checksum 变化）的识别兜底机制——官方无说明。
2. AppTrust "immutable audit record" 的不可变实现方式（签名绑定 vs WORM/append-only 存储）。
3. PostgreSQL 组件图的具体 schema/规模数据（多少边、递归查询优化方式）。
4. Contextual Analysis scanner 的编写语言/规则 DSL——只知产物是 analyzerManager 二进制+随 Xray 版本分发的规则，规则格式未公开。
5. DBSync v3 离线包的签名/完整性校验机制（是否有 GPG 验签）未在文档见到。
6. ZTR vendor rebuild 的"verified"具体含义（JFrog 是否对 Chainguard/Echo 等 rebuild 做独立校验，还是信任 vendor 签名）。
7. AppTrust pre-built CRA policy templates 的具体 Rego 内容（定价页声称存在，模板本身未公开获取）。
