# 06 — 业内产品形态分类学与各能力层实际技术栈

> 研究日期：2026-09-20 | 研究者：补充调研子任务
> 配套材料：每条重要结论对应 [06-product-forms-and-tech-stacks/sources/](06-product-forms-and-tech-stacks/sources/) 下一条 source note；检索过程见 [06-product-forms-and-tech-stacks/research-log.md](06-product-forms-and-tech-stacks/research-log.md)。
> 标注体系沿用 [02](02-cra-regulation.md)–[05](05-eu-compliance-landscape.md) 报告：**Fact**（一手来源直接载明）/**Interpretation**（基于事实的合理推论）/**Hypothesis**（假设，需进一步核实）。厂商营销口径一律标注"（厂商声称）"。
> 与 [03](03-competitive-landscape.md)/[04](04-technology-deep-dive.md) 的分工：[03](03-competitive-landscape.md) 回答"谁家有什么能力"（厂商×功能矩阵），[04](04-technology-deep-dive.md) 回答"理论上怎么做、壁垒在哪"（方法层）；**06 回答两个新问题——这些产品实际是什么"物种"、怎么交付、怎么收费（Part A）；各能力层业界实际在用什么技术组件（Part B，只要工程现实，不重复理论）**。凡 [03](03-competitive-landscape.md)/[04](04-technology-deep-dive.md) 已覆盖的内容一律标注"见 [03](03-competitive-landscape.md) / 见 [04](04-technology-deep-dive.md)"，不重抄。

---

## 0. TL;DR

1. **供给收敛为十个物种**，且每个物种有稳定的"核心对象 × 交付模式 × 计费单位"三元组：开发者平台型按席位（per-dev）、云原生/运行时型按工作负载（per-workload）、制品仓库型按服务器/订阅、二进制固件型按产品镜像（per-image/per-product）、重建发行商按镜像目录订阅。**计费单位即物种指纹**——它定义了产品对谁的价值负责。
2. **技术栈层面的"公共底座"已经形成**：识别层 = Trivy(fanal)/Syft/Semgrep CE(OpenGrep)/govulncheck 开源四件套；运行时层 = eBPF（Tracee/Falco/Tetragon）；数据层 = NVD+OSV/GHSA 免费聚合 + 商业策展库；修复层 = PR bot（Dependabot/Renovate）+ "确定性校验 + LLM 生成"修复架构；存储层 = **PostgreSQL 关系库一统天下**（Dependency-Track、GUAC、Backbase 生产实证），图数据库仍是叙事。
3. **三层趋同**：漏洞策展收敛到"AI 加速 + 人类终审 + 风险优先队列"（GitHub 官方承认纯人工已撑不住）；AI 修复收敛到"LLM 生成 + 确定性校验兜底"（见 [04](04-technology-deep-dive.md)）；AI 接入收敛到 MCP tool 化（Snyk 等把扫描器封装成 MCP server 供编码 agent 调用）。
4. **形态红海**：开发者平台型 SSCS、ASPM 聚合层、CLI 扫描器。**结构性机会**（结合 [03](03-competitive-landscape.md) 的 Product→Version 空白）：CRA 语境下"以产品/版本为对象的生命周期平台"在物种分类学上尚无对应物——它介于企业 SCA 套件（有对象模型、无现代工作流）与二进制固件型（有产品对象、无开发者闭环）之间；air-gapped/on-prem 交付是 CRA 覆盖的军工/汽车/医疗客户的硬门槛，恰好是新物种普遍放弃、老物种守着的能力。
5. **入场底线**：识别、匹配、SBOM、PR bot、runtime 探针五层必须复用成熟开源（自研=浪费）；自研差异化只在三处——**产品/版本对象模型与证据链数据模型、策展数据与 backport 处理的质量、C/C++/二进制侧的 reachability**（见 [04](04-technology-deep-dive.md) 壁垒判断）。

---

## Part A. 产品形态分类学（Product Form Taxonomy）

### A.0 总览表

| # | 物种 | 代表玩家 | 核心对象 | 交付模式 | 典型计费单位 | 拥挤度 |
|---|---|---|---|---|---|---|
| 1 | CLI/CI 原生扫描器（OSS 核心+商业 SaaS） | Trivy/Aqua、Grype+Syft/Anchore、osv-scanner/Google、Semgrep | repo / 镜像 / 文件系统 | OSS CLI 先行 + SaaS 平台；引擎开源 | 平台席位/用量（扫描本身免费） | 🔴 红海 |
| 2 | 开发者平台型 SSCS | Snyk、Endor Labs、Socket、Arnica | repo / 依赖图 | SaaS 控制台 + CLI/IDE 插件（扫描可在客户 runner 内） | per contributing dev（×产品线） | 🔴 红海 |
| 3 | 制品仓库/Registry 代理型 | JFrog Artifactory+Xray、Sonatype Nexus/Lifecycle、Chainguard（重建发行） | artifact / 镜像 / 包 | SaaS / self-hosted / air-gapped 全形态 | per server 订阅 / per image / 目录订阅 | 🟡 中高（重建子物种新） |
| 4 | 企业 SCA 套件 | Black Duck、Mend、Veracode | project+version / application | SaaS + on-prem + air-gapped KB | 企业订阅（per app/全包询价） | 🟡 存量稳固 |
| 5 | ASPM 聚合层 | ArmorCode（纯聚合）、Apiiro、Cycode | finding / asset 归一化视图 | 多租户 SaaS | 企业订阅（按集成资产/规模询价） | 🔴 红海（品类已整合） |
| 6 | 二进制/固件分析型 | Finite State、ONEKEY、NetRise | product / 固件镜像 | SaaS + on-prem + 离线 | per image / per product（订阅+服务） | 🟢 竞争少 |
| 7 | 运行时/云原生型 | Wiz、Aqua、Oligo | runtime workload | SaaS + agentless 快照 + eBPF sensor（可选 on-prem） | per cloud workload | 🟡 头部集中 |
| 8 | 漏洞数据/情报供应型 | Flashpoint VulnDB、Sonatype Data Services、Snyk Intel、Mend 库 | 漏洞记录/策展数据 | API/feed 订阅；随套件内嵌 | 数据订阅 | 🟢 少数寡头 |
| 9 | CRA 原生初创 | CRACI（赫尔辛基）等 | product 合规档案 | SaaS，CI/CD 嵌入 | 早期未定形 | 🟢 极早期 |
| 10 | 开源平台自建派 | Dependency-Track、GUAC | project / portfolio（SBOM-first） | 自托管 OSS（容器/二进制分发） | 免费（自付运维） | —（基线，非市场） |

一句话/类：

1. **CLI/CI 原生扫描器**：开源引擎把扫描做成免费公共设施，商业收入全靠上面的平台层。
2. **开发者平台型 SSCS**：把安全嵌进开发者工作流，按人头卖席位，产品线逐条加购。
3. **制品仓库/Registry 代理型**：守着"包的必经之路"，在拉包/入库点上做策略执行与检测。
4. **企业 SCA 套件**：以 project+version 为对象的审计级合规重型装备，on-prem/air-gapped 是祖传护城河。
5. **ASPM 聚合层**：自己不产检测，把别人扫描器的告警归一化成风险工单流。
6. **二进制/固件分析型**：没有源码也能从编译产物还原成分与漏洞，服务设备制造商 PSIRT。
7. **运行时/云原生型**：看"实际在跑什么"，agentless 快照打底、eBPF 按需加深。
8. **漏洞数据/情报供应型**：不做扫描器，只卖比 NVD 更快更全的策展数据。
9. **CRA 原生初创**：法规窗口期创业者，把 CRA 合规做成 CI/CD 里的自动化文档流。
10. **开源平台自建派**：企业用 Dependency-Track/GUAC 自组装零许可费基线，压低全行业的起步价。

### A.1 CLI/CI 原生扫描器：开源核心 + 商业 SaaS

- **模式（Fact）**：引擎 OSS（Trivy/Syft/Grype/osv-scanner/Semgrep CE 均 Apache-2.0 或 LGPL），扫描本身免费、本地执行、CI 嵌入零摩擦；商业化全部发生在平台层（Aqua Platform、Anchore Enterprise、Semgrep AppSec Platform）。来源：[trivy-fanal](06-product-forms-and-tech-stacks/sources/trivy-fanal.md)、[semgrep-engine-opengrep](06-product-forms-and-tech-stacks/sources/semgrep-engine-opengrep.md)。
- **许可张力（Fact）**：Semgrep 2024-12 将**规则仓库**改 proprietary Semgrep Rules License（引擎维持 LGPL-2.1，官方确认），2025-01 厂商联盟 fork 出 OpenGrep——"引擎开源、规则/生态控制收费"的结构矛盾已经公开爆过一次。来源：[semgrep-engine-opengrep](06-product-forms-and-tech-stacks/sources/semgrep-engine-opengrep.md)。
- **Interpretation**：该物种已完成历史使命——把"检测"打成零价。新入场者在检测层与它们竞争没有意义；它们是**供应商**（检测能力上游），不是对手。

### A.2 开发者平台型 SSCS

- **交付（Fact）**：SaaS 控制台为体，CLI/IDE 插件/SCM 集成为用；扫描可在客户 CI runner 内执行、仅结果回传（Endor 官方明确此选项 + Outpost 定时监测），缓解源码出域顾虑。来源：[endor-pricing-docs](06-product-forms-and-tech-stacks/sources/endor-pricing-docs.md)。
- **定价（Fact）**：全部收敛 per contributing developer——Snyk $25/席/月（Team）起、$105/席/月（Ignite）、Enterprise 询价且**按产品线分别计价**；Endor per contributor/年 + scan credit 配额；Socket 约 $25/席/月起（第三方目录）。来源：[snyk-pricing-outmano](06-product-forms-and-tech-stacks/sources/snyk-pricing-outmano.md)、[endor-pricing-docs](06-product-forms-and-tech-stacks/sources/endor-pricing-docs.md)。
- **能力明细见 [03](03-competitive-landscape.md)**（Snyk/Endor/Socket/Arnica 各节），此处不重复。
- **Interpretation**：per-dev 计费使该类产品的价值主张锚定在"开发者人数"上，天然难以覆盖 CRA 语境下"产品上市后 5–10 年支持期"的 PSIRT/合规场景——买方（工程效能）与 CRA 买方（合规/产品安全）错位。

### A.3 制品仓库/Registry 代理型

- **传统两强（Fact）**：JFrog Xray 不单独售卖，寄生在 Artifactory 上（SaaS/self-hosted/air-gapped 全形态；self-managed Enterprise X 公开挂牌约 $51k/年起，第三方挂牌价）；Sonatype 同构（IQ Server on-prem + Nexus Repository 拦截点）。策略执行点在"拉包"路径（Curation/Firewall 模型）。来源：[jfrog-xray-delivery](06-product-forms-and-tech-stacks/sources/jfrog-xray-delivery.md)；能力明细见 [03](03-competitive-landscape.md)。
- **新子物种：重建发行商（Fact）**：Chainguard 不扫描、直接**重建并发行干净制品**（Containers per-image/目录订阅 $19k/年起 + CVE 修复 SLA；Libraries 按语言×人头）——卖的是"替换用制品+SLA"而非检测。来源：[chainguard-catalog-pricing](06-product-forms-and-tech-stacks/sources/chainguard-catalog-pricing.md)；范式意义见 [03](03-competitive-landscape.md)/[00-final](00-final-report.md) §9.2。
- **Interpretation**：该物种拥有全行业最强的"执行点"（阻断/替换），但对象止步于 artifact——离 CRA 的"product with digital elements + 支持期"语义最近却又差一层（与 [00-final](00-final-report.md) §9.2 对 JFrog 的判断一致）。

### A.4 企业 SCA 套件

- **交付（Fact）**：on-prem/air-gapped 是一等公民——Black Duck 提供 K8s on-prem + **air-gapped KnowledgeBase**（漏洞库本地节点，断网匹配）；Mend 保留 On-Premise+SaaS 双形态；Veracode 为纯多租户 SaaS（品类内部分化点）。来源：[blackduck-airgap-kb](06-product-forms-and-tech-stacks/sources/blackduck-airgap-kb.md)、[mend-veracode-delivery](06-product-forms-and-tech-stacks/sources/mend-veracode-delivery.md)。
- **对象模型（见 [03](03-competitive-landscape.md)）**：Black Duck Project+Version 是全行业最接近 CRA Product→Version 语义的现存模型。
- **定价（Fact/Interpretation）**：企业订阅询价制；第三方口径 Mend 约 $1,000+/dev/年且通常比 Black Duck 低 30–50%（第三方汇编，未官方证实）。
- **Interpretation**：套件型物种的技术栈老龄化（扫描引擎、BOM 匹配逻辑均有十年以上积累）但**证据/审计能力与断网交付**恰好是 CRA 监管场景的硬通货——这是"旧物种在 CRA 下回春"的结构原因。

### A.5 ASPM 聚合层

- **定义性特征（Fact）**：ArmorCode 官方明示"doesn't run its own scanner"，以中立聚合为卖点；Apiiro/Cycode 则叠加部分自有检测（code-to-runtime 风险图、管道姿态）——ASPM 内部按"是否自产检测"再分化。来源：[armorcode-scannerless](06-product-forms-and-tech-stacks/sources/armorcode-scannerless.md)。
- **Interpretation**：该物种的护城河是集成广度 + finding/asset 归一化数据模型 + 工作流粘性，进入门槛低；2026 年品类已被平台型玩家（Snyk AppRisk、Wiz 等）上下挤压，独立 ASPM 空间收窄（第三方对比口径，Hypothesis 级趋势判断）。对 CRA 的意义：ASPM 的归一化数据模型是"多源证据入图"的现成参照，但它没有产品/支持期对象。

### A.6 二进制/固件分析型

- **对象与计量（Fact）**：核心对象是产品/固件镜像——ONEKEY 案例计量口径即"每年分析约 80 个固件镜像"（Swisscom），交付 SaaS+on-prem+离线，主打 IEC 62443/欧盟监管场景。来源：[onekey-delivery](06-product-forms-and-tech-stacks/sources/onekey-delivery.md)。
- **技术范式（Fact）**：解包 → 成分还原 → 特征库比对（见 Part B.1），与源码侧完全不同的识别栈。来源：[finite-state-binary](06-product-forms-and-tech-stacks/sources/finite-state-binary.md)、[netrise-bca](06-product-forms-and-tech-stacks/sources/netrise-bca.md)。
- **Interpretation**：这是 CRA 覆盖的嵌入式/IoT 主战场的"半个占位者"（[00-final](00-final-report.md) §9.2 已判），其短板不是技术而是**没有开发者侧闭环与现代工作流**——形态上停留在"上传镜像→出报告"的 PSIRT 工具。

### A.7 运行时/云原生型

- **架构收敛（Fact）**：agentless（云 API+磁盘快照，快覆盖）打底 + eBPF sensor（按需加深）双轨——Wiz 官方自述即此模型，竞品 ARMO 亦确认；Oligo 纯 eBPF 探针路线、按库函数粒度画像；Aqua 建立在开源 Tracee 上。来源：[wiz-runtime-sensor](06-product-forms-and-tech-stacks/sources/wiz-runtime-sensor.md)、[oligo-ebpf](06-product-forms-and-tech-stacks/sources/oligo-ebpf.md)、[aqua-tracee](06-product-forms-and-tech-stacks/sources/aqua-tracee.md)。
- **定价（Fact）**：per cloud workload——Wiz AWS Marketplace 公开价 100 workloads $24k/年（Essential）/$38k/年（Advanced）。来源：[wiz-aws-marketplace-pricing](06-product-forms-and-tech-stacks/sources/wiz-aws-marketplace-pricing.md)。
- **Interpretation**：per-workload 计费锚定"云上资产"，与 CRA 的"产品"对象同样错位；但其 runtime 证据（函数实际执行观测）是 CRA 漏洞处置论证的优质输入（见 [04](04-technology-deep-dive.md) Oligo 节）。

### A.8 漏洞数据/情报供应型

- **三种模式（Fact）**：① 独立情报商——Flashpoint VulnDB 自称 400k+ 记录、100k+ non-CVE、不依赖 NVD（厂商声称），纯 API/feed 订阅；② 套件内嵌数据服务——Sonatype"we create the precise data we use"（官方原文，自动化系统+人工研究团队）、Snyk Intel（人工策展+AI 辅助）、Mend/Checkmarx Zero 同理；③ 免费公共层——NVD/OSV/GHSA（[01](01-domain-ontology.md) 已覆盖）。来源：[flashpoint-vulndb](06-product-forms-and-tech-stacks/sources/flashpoint-vulndb.md)、[sonatype-vuln-data](06-product-forms-and-tech-stacks/sources/sonatype-vuln-data.md)、[snyk-vuln-curation](06-product-forms-and-tech-stacks/sources/snyk-vuln-curation.md)、[mend-vuln-research](06-product-forms-and-tech-stacks/sources/mend-vuln-research.md)。
- **Interpretation**：数据是少数仍具"寡头"结构的层——策展团队是重资产，新入场者短中期只能"消费+薄策展"，不可能复制全量自建。

### A.9 CRA 原生初创

- **现状（Fact）**：CRACI（赫尔辛基，2025 创立）2026-05 获 €1.4M pre-seed，形态 = CI/CD 嵌入的 CRA 合规自动化（成分跟踪+漏洞监控+SBOM+EU 文档，目标 CE marking readiness）。来源：[craci-preseed](06-product-forms-and-tech-stacks/sources/craci-preseed.md)。
- **Interpretation**：窗口期创业潮真实存在但体量极小（pre-seed 级），且切入点选择了"开发者工作流"而非"PSIRT 套件"——与 [03](03-competitive-landscape.md) 对 CRA 营销热度的观察一致：叙事很满，产品很浅。这既是空白证据也是需求未验证的警示。

### A.10 开源平台自建派

- **Fact**：Dependency-Track（OWASP 旗舰，SBOM-first，project/portfolio 对象，免费自托管）与 GUAC（OpenSSF，供应链图）构成企业自组装基线；生产部署普遍 PostgreSQL（Backbase 实证 Aurora PG）。来源：[dependency-track-storage](06-product-forms-and-tech-stacks/sources/dependency-track-storage.md)；GUAC 细节见 [04](04-technology-deep-dive.md)。
- **Interpretation**：该派的存在把"SBOM 管理+VEX+portfolio 监控"的市场价格压到零——任何商业产品在这些能力上的收费都必须回答"为什么不用 Dependency-Track"。

---

## Part B. 各能力层的"业界实际技术栈"

> 原则：只写"业界实际在用什么"，注明谁在用；理论方法一律指向 [04](04-technology-deep-dive.md)。

### B.1 组件检测/识别

| 技术 | 实际在用者 | 事实与出处 |
|---|---|---|
| manifest/lockfile 解析 + 分析器注册表 | Trivy（Go，`pkg/fanal`，analyzer 插件注册，解析 apk/dpkg/rpm 包数据库与各语言 lockfile，镜像逐层分析） | Fact，[trivy-fanal](06-product-forms-and-tech-stacks/sources/trivy-fanal.md)；Syft/Grype 同构（见 [03](03-competitive-landscape.md)/[04](04-technology-deep-dive.md)） |
| 文件/目录哈希签名（signature scan） | Black Duck Signature Scanner | Fact，[blackduck-snippet-matching](06-product-forms-and-tech-stacks/sources/blackduck-snippet-matching.md) |
| 代码片段指纹（snippet matching） | Black Duck：取文件前 2MB（1–16MB 可调），5–7 行可成匹配，专抓无声明的拷贝粘贴复用 | Fact（官方手册+学术分析），同上 |
| 二进制指纹/相似度匹配 | Finite State（解包→归一化→组件特征库比对）；学术界同族方法 BinaryAI/jTrans/VoteSim | Fact，[finite-state-binary](06-product-forms-and-tech-stacks/sources/finite-state-binary.md) |
| Binary Composition Analysis（BCA） | NetRise Turbine：直接从编译产物生成 SBOM；能力正被作为组件嵌入聚合平台（Manifest 合作） | Fact，[netrise-bca](06-product-forms-and-tech-stacks/sources/netrise-bca.md) |
| 包行为静态刻画 | Socket：检测新引入的 network/shell/filesystem/env 等风险 API 使用，不等 CVE | Fact，[socket-behavioral](06-product-forms-and-tech-stacks/sources/socket-behavioral.md) |
| CPE 匹配 | Dependency-Track、各扫描器在发行版 feed 缺失时的 fallback；公认误报源（见 B.3） | Fact，[anchore-grype-matching](06-product-forms-and-tech-stacks/sources/anchore-grype-matching.md) |
| PURL 归一化 | 全行业事实标准标识符（[01](01-domain-ontology.md) 已覆盖 spec）；各平台内部实体解析的统一键 | Fact，见 [01](01-domain-ontology.md) |

**Interpretation**：识别层是"三条范式并存"——声明解析（源码侧）、哈希/指纹（二进制侧）、行为刻画（恶意包侧）。三条都有成熟开源或寡头供应商，**自研价值为零**；值得做的是三条范式结果的**实体解析归一**（同一个 log4j 在 manifest、二进制指纹、SBOM 里认作同一组件）——这恰是 Evidence Graph 的地基（与 [04 §4](04-technology-deep-dive.md) 合流）。

### B.2 漏洞数据管道

- **公共免费层（Fact）**：NVD + OSV/GHSA 聚合，Dependency-Track 直接消费；GHSA 本身开源免费（见 [01](01-domain-ontology.md)）。
- **商业策展层（Fact）**：
  - Snyk：专职研究团队人工策展，2025 起公开 human-in-the-loop + AI 辅助（官方自述 RLHF 式闭环）；以"不受 NVD 延迟影响"为卖点。来源：[snyk-vuln-curation](06-product-forms-and-tech-stacks/sources/snyk-vuln-curation.md)。
  - Sonatype："自有自动化漏洞检测系统 + Data Research 团队"，官方强调"不只是聚合，是造数"（精确版本区间/组件坐标）。来源：[sonatype-vuln-data](06-product-forms-and-tech-stacks/sources/sonatype-vuln-data.md)。
  - Mend（WS-* 自有 ID）、Checkmarx Zero 同构。来源：[mend-vuln-research](06-product-forms-and-tech-stacks/sources/mend-vuln-research.md)。
  - Flashpoint VulnDB：独立研究团队、100k+ non-CVE、平均快约两周（厂商声称）。来源：[flashpoint-vulndb](06-product-forms-and-tech-stacks/sources/flashpoint-vulndb.md)。
- **策展吞吐危机（Fact）**：GitHub 官方承认漏洞报告速度已超人工审核能力（2026-05 单月 1,560 条 reviewed 仍积压），对策 = AI 辅助研究 + 自动化上游抽取 + **风险优先审核队列**（包使用量/在野利用/生态影响信号），人类保留最终判定。来源：[github-advisory-curation](06-product-forms-and-tech-stacks/sources/github-advisory-curation.md)。
- **Interpretation**：2026 年的行业拐点——**"AI 加速 + 人类终审 + 风险分层队列"成为策展标准模式**，纯人工与全自动都被证伪。新入场者的可行路径：消费公共层 + 商业 API（VulnDB/Snyk Intel 类），把有限的策展人力只投在**自家客户产品组合相关的组件**上（垂直薄策展），而不是横向建库。
- **Backport 感知的数据处理（Fact）**：体现在数据源选择而非算法——Grype/Anchore 以发行版 maintainer 安全 feed（Debian/RHEL/SUSE/Ubuntu 等 10 家）作为 OS 包匹配的权威源，NVD 仅用于语言包与 fallback。来源：[anchore-grype-matching](06-product-forms-and-tech-stacks/sources/anchore-grype-matching.md)。

### B.3 匹配引擎

- **实际架构（Fact）**：预加工漏洞 DB（GrypeDB ≈1GB SQLite，客户端离线匹配）+ 按生态实现的 matcher（OS 包走发行版 feed 的 fix 版本比较；语言包走 NVD/GHSA 版本区间）。来源：[anchore-grype-matching](06-product-forms-and-tech-stacks/sources/anchore-grype-matching.md)。
- **Backport 处理的边界（Fact）**：一手 issue（grype #1541）证明——落入 NVD CPE 版本比较路径时发行版 backport 必然误报；**误报控制的上限 = 发行版 feed 的覆盖率与质量**，不是匹配算法。Chainguard 的解法是另一条路：让自己的重建制品带干净版本号 + VEX feed，从数据源头消除（见 [03](03-competitive-landscape.md)）。
- **Interpretation**：匹配引擎是完全商品化的工程问题（version range 库、semver/distro 版本比较器均开源）；差异化在**匹配证据的可解释性**（"为什么判 affected"的版本区间推导链可审计）——这与 CRA 证据需求直接相关，是免费工具不做的事。

### B.4 静态分析 / Reachability 底座

| 引擎 | 谁在用 | 备注 |
|---|---|---|
| Semgrep CE/OpenGrep（OCaml 内核 + tree-sitter→generic AST） | Semgrep 自家 Supply Chain reachability（见 [04](04-technology-deep-dive.md) 白皮书）；OpenGrep 联盟厂商（Endor 等参与维护） | Fact，[semgrep-engine-opengrep](06-product-forms-and-tech-stacks/sources/semgrep-engine-opengrep.md)；"一套引擎 30+ 语言"的最省事被验证路线 |
| CodeQL | GitHub（GHAS/Copilot Autofix 的确定性底座，见 [04](04-technology-deep-dive.md)）；学术与自定义查询生态 | Fact，见 [04](04-technology-deep-dive.md) |
| Joern（CPG） | 学术界与 C/C++ 场景（见 [04](04-technology-deep-dive.md)）；商业化产品化少 | Fact，见 [04](04-technology-deep-dive.md) |
| govulncheck | Go 官方，单语言 reachability 被生态"国有化"的标杆 | Fact，见 [04](04-technology-deep-dive.md) |
| 自研程序分析 + 策展函数映射库 | Snyk（reachability GA 三语言）、Endor（CVE→函数映射库） | Fact，见 [03](03-competitive-landscape.md)/[04](04-technology-deep-dive.md)；**真正的成本中心是标注数据集不是引擎**（[04](04-technology-deep-dive.md) 已判） |
| Semgrep 引擎寄生 | GitLab SAST analyzer 基于 Semgrep（其 static reachability 为 package 级，见 [03](03-competitive-landscape.md)） | Fact，见 [03](03-competitive-landscape.md) |

**Interpretation**：底座引擎开源充足（tree-sitter 路线已被 Semgrep 验证为最经济的语言扩展方式）；各家差异在引擎之上的**规则/数据集/降噪工程**。新入场者若做 reachability，站在 OpenGrep/CodeQL/Joern 上、把投入集中在 C/C++ 与 CVE→函数数据集（[04 §6.1](04-technology-deep-dive.md) 结论的技术栈翻译）。

### B.5 运行时

- **统一底座 = eBPF（Fact）**：开源侧 Tracee（Aqua）、Falco（CNCF graduated）、Tetragon 三足鼎立；商业侧 Wiz Sensor、Oligo、Sysdig 均为 eBPF。来源：[aqua-tracee](06-product-forms-and-tech-stacks/sources/aqua-tracee.md)、[wiz-runtime-sensor](06-product-forms-and-tech-stacks/sources/wiz-runtime-sensor.md)、[oligo-ebpf](06-product-forms-and-tech-stacks/sources/oligo-ebpf.md)。
- **差异化维度（Fact/Interpretation）**：不是"是否 eBPF"而是**探针解读深度**——syscall/网络流（Tracee/Falco 层）→ 库函数画像（Oligo 层）→ 应用语义关联（Wiz Security Graph 层）；"agentless 快照 + agent 按需"双轨成为部署标准模式。
- **Interpretation**：对我们的含义——runtime 层不必自建探针，消费 Tracee/Falco 事件流或与 Oligo 类产品集成即可获得 runtime 证据；自建差异化只在"runtime 证据 → VEX/产品漏洞处置记录"的转化层（无人做好，见 [00-final](00-final-report.md) §9.1 创新空间 2）。

### B.6 Remediation

- **升级 PR bot（Fact）**：Dependabot（GHSA reviewed 条目驱动，只有经策展映射的 advisory 才产生告警——见 B.2）与 Renovate（OSS、可自托管）已普及，完全商品化。来源：[github-advisory-curation](06-product-forms-and-tech-stacks/sources/github-advisory-curation.md)；见 [04](04-technology-deep-dive.md)。
- **Patch backport / 重建修复（Fact）**：Chainguard CVE remediation（backport+重建制品+干净版本号+VEX feed）；Endor Patches（见 [03](03-competitive-landscape.md)/[04](04-technology-deep-dive.md)）。
- **LLM 修复 agent 的架构趋同点（Fact，[04](04-technology-deep-dive.md) 已证）**：GitHub CCR、Snyk Agent Fix、AIxCC 冠军系统全部 = "确定性工具产出精确代码事实 → LLM 生成 → 确定性校验（re-scan/编译/测试）兜底"。本报告补充：**该架构已商品化到"修复建议"环节，但验证闭环的深实现（构建/测试/回归证据入档）无人产品化**——与 [00-final](00-final-report.md) §9.1 创新空间 4 一致。
- **Interpretation**：修复层的可复用件 = Renovate bot 机制 + MCP 化的 LLM 修复调用；自研点 = 修复决策与产品版本/支持期策略的绑定（"这个版本修不修、怎么修、证据怎么留"），这正是 PR bot 不懂的部分。

### B.7 存储与数据底座

- **Fact（多源互证）**：
  - Dependency-Track：Java 单体 + 关系库（内嵌 H2，生产 PostgreSQL；Backbase 用 Aurora PG）——project/component/finding/VEX 全在关系表。来源：[dependency-track-storage](06-product-forms-and-tech-stacks/sources/dependency-track-storage.md)。
  - GUAC：生产推荐 PostgreSQL/内存 KV，Neo4j 后端官方 unsupported（[04](04-technology-deep-dive.md) 已证）。
  - Wiz Security Graph：营销叙事为图，第三方演示可在关系库上复刻（[04](04-technology-deep-dive.md) 已证）。
  - Artifactory：Derby/MySQL/PostgreSQL/Oracle/MSSQL 关系库 + 文件/S3 块存储（第三方迁移文档）。
- **Interpretation**：**"图数据模型、关系库实现"是业界普遍现实**，与 [04](04-technology-deep-dive.md) 反叙事 2 完全一致且样本扩大。工程推论：证据图产品的存储选型应是 PostgreSQL（JSONB+递归 CTE 足够）+ 对象存储（SBOM/证据 blob）+ 列存/搜索（OLAP 报表与全文检索），图数据库仅在前端探索可视化层出现。

### B.8 AI/Agent 层

- **copilot vs 编排层（Fact/见 [04](04-technology-deep-dive.md)）**：copilot（triage/降噪/问答）已商品化（Semgrep Assistant 等，见 [03](03-competitive-landscape.md)）；编排层（Snyk Evo 四环、GitHub agentic workflows）是 2026 年的主战场，但 [04](04-technology-deep-dive.md) 已判"纯 MCP 编排无壁垒"。
- **MCP 采用（Fact）**：Snyk 2025-05 起把扫描能力封装为 MCP server（随 CLI 分发，第三方核验 13 tools、本地执行），让 IDE 编码 agent 自主调用；并发布 mcp-scan 治理 MCP 攻击面。来源：[snyk-mcp](06-product-forms-and-tech-stacks/sources/snyk-mcp.md)。
- **Interpretation**：业界收敛方向 = **安全能力以 MCP tool 形态"被编排"，而非安全厂商自造封闭 agent 闭环**。真实产品里的 agent 架构三件套：确定性工具层（扫描/reachability/匹配）+ LLM 编排层（计划/生成/解释）+ 人类签核门（CRA 责任场景必需，见 [04](04-technology-deep-dive.md) 反叙事 3）。

### B.9 交付与部署

- **光谱（Fact）**：纯多租户 SaaS（Veracode、Apiiro、Wiz 主体）→ SaaS+客户侧执行混合（Endor：扫描在客户 runner、结果上云；Snyk MCP 本地扫描）→ SaaS+self-hosted 双形态（JFrog、Sonatype、Mend、Semgrep）→ on-prem+air-gapped 一等公民（Black Duck air-gapped KB、ONEKEY 离线模式、JFrog self-managed air-gapped）。来源：对应 source notes。
- **CLI 先行策略（Fact/Interpretation）**：开发者向物种（Snyk/Endor/Semgrep/Trivy 系）全部 CLI/IDE 先行、平台变现；PSIRT 向物种（Finite State/ONEKEY）全部平台先行（上传镜像→报告）——**入口选择即物种选择**。
- **Interpretation**：军工/汽车/医疗（CRA 高相关且采购力强的行业）的硬需求是 on-prem/air-gapped + 知识库可打包下发；SaaS-only 玩家在这些行业结构性缺席。Black Duck 的 air-gapped KB 证明"漏洞库本地化"是成熟工程问题，新入场者必须第一天就按"数据可离线分发"设计数据管道。

---

## Part C. 格局判断

### C.1 红海 vs 结构性机会

**已拥挤（红海）**：

1. CLI 扫描器（检测零价化完成，开源四件套垄断）；
2. 开发者平台型 SSCS（Snyk/Endor/Socket/Arnica + GitHub/GitLab 内置挤压，per-dev 价格战开始）；
3. ASPM 聚合层（品类被平台上下夹击，独立空间收窄，Hypothesis 级趋势）；
4. 运行时 CNAPP（Wiz 一家独大 + Google 整合，见 [03](03-competitive-landscape.md)）。

**CRA 语境下的结构性机会**：

1. **物种分类学上的缺失物种（Interpretation，呼应 [03 §4](03-competitive-landscape.md)）**：以 Product→Version 为核心对象、覆盖支持期漏洞生命周期的平台，在十个物种中**没有对应物**。两端最近者——企业 SCA 套件（有对象模型、无现代开发者闭环与 reachability）和二进制固件型（有产品对象、无闭环）——都被各自的物种基因锁死（per-dev/审计套件基因 vs 上传报告工具基因）。[03](03-competitive-landscape.md) 的"中间断层"在形态学上得到二次确认。
2. **交付形态差（Fact+Interpretation）**：CRA 高相关采购行业（军工/汽车/医疗/工业设备）要求 on-prem/air-gapped，而 2018 年后创立的新物种几乎全部 SaaS-only——**"现代能力 × 断网交付"的组合无人提供**，老物种有交付无现代能力，新物种有能力无交付。
3. **CRA 原生初创尚浅（Fact）**：窗口期创业者（CRACI 等）在 pre-seed 体量、CI/CD 文档自动化切入——验证空白存在，也提示需求侧付费意愿仍待监管执法催化（与 [03 §4](03-competitive-landscape.md) 反方风险②一致）。

### C.2 技术栈"入场底线"：哪些层必须复用、哪些层自研

**必须复用成熟开源（自研=浪费）**：

| 层 | 复用什么 | 理由 |
|---|---|---|
| 组件识别 | Trivy(fanal)/Syft 直接嵌入或兼容其输出 | 分析器注册表生态成熟，逐语言 lockfile/OS 包解析是纯工程量 |
| SBOM 生成/格式 | Syft/CycloneDX/SPDX/PURL（[01](01-domain-ontology.md) 已证标准化完成） | 已 ECMA 标准化，零差异化 |
| 漏洞匹配 | Grype 式生态 matcher + GrypeDB 模式（预加工 SQLite 离线库） | 匹配算法商品化；离线库模式天然解决 air-gapped |
| 公共漏洞数据 | NVD+OSV/GHSA 聚合，商业 API（VulnDB 类）补 non-CVE | 横向建库是千万级/年投入，寡头格局已定 |
| 静态分析底座 | OpenGrep/Semgrep CE（tree-sitter→generic AST 路线）、CodeQL、Joern（C/C++）、govulncheck（Go） | 引擎开源充足，[04](04-technology-deep-dive.md) 已证无算法壁垒 |
| 运行时探针 | Tracee/Falco 事件流；不自建 eBPF | 底座统一，差异化在语义层 |
| 修复 PR 机制 | Renovate（可自托管、可定制） | 机制商品化 |
| 存储 | PostgreSQL + 对象存储（+ 搜索/OLAP） | [04](04-technology-deep-dive.md)+[06](06-product-forms-and-tech-stacks.md) 双证：图数据库是叙事 |

**自研差异化所在（护城河成分）**：

1. **产品/版本/支持期对象模型与证据链数据模型**（Evidence Graph 本体：实体解析、跨源归一、结论级 attestation）——十个物种都没有，是 [04](04-technology-deep-dive.md) 判定的"潜在真壁垒候选"；
2. **垂直薄策展 + backport 数据质量**（只策展客户产品组合相关组件；发行版 feed 之外的长尾生态 backport 处理）——匹配误报控制的实际上限；
3. **C/C++/二进制 reachability 与其证据化**（[04 §6.1](04-technology-deep-dive.md)：产品化最薄弱、竞争最少、CRA 主战场语言）；
4. **air-gapped 数据管道工程**（知识库可打包下发 + 断网增量更新）——不是高科技但是硬门槛，老物种之外无人做；
5. **修复→验证→证据闭环**（构建/测试回归证据入档、VEX 自动重估）——[00-final](00-final-report.md) §9.1 创新空间 4/6 的技术栈落点。

### C.3 对我们（已有 SCA/SAST 能力的厂商）的技术栈复用建议

1. **存量能力映射**：自有 SCA（识别+匹配）可保留引擎但数据管道改造为"可离线分发"结构（GrypeDB 模式的启示）；自有 SAST 若是自研引擎，评估逐步向 OpenGrep/CodeQL 迁移语言长尾，把人力释放到规则与 reachability 数据集（[04](04-technology-deep-dive.md)：数据集才是成本中心）。
2. **缺口按 C.2 自研清单补**：优先产品/版本对象模型 + PostgreSQL 证据图底座（复用 Dependency-Track 的对象语义教训——它的 project/portfolio 模型已验证了关系库足够，见 B.7）。
3. **集成熟于自研的外部层**：runtime 证据（Oligo/Wiz/Tracee 消费）、non-CVE 情报（VulnDB API）、二进制分析（NetRise 式组件化采购，Manifest-NetRise 合作证明该层可被 API 化嵌入——来源：[netrise-bca](06-product-forms-and-tech-stacks/sources/netrise-bca.md)）。
4. **AI 层姿态**：把自有扫描/reachability 能力 MCP tool 化（Snyk 模式），让编码 agent 与合规 agent 都能编排；不建封闭 agent 闭环（[04](04-technology-deep-dive.md) 反叙事 3 + B.8 趋同判断）。
5. **交付策略**：第一天按 SaaS + on-prem/air-gapped 双轨设计（数据可离线分发是架构约束，后补代价高）；CLI/agent 先行获取开发者入口，平台承载 PSIRT/合规工作流。

---

## 附：与 [03](03-competitive-landscape.md)/[04](04-technology-deep-dive.md) 报告的交叉引用边界

- 厂商能力明细（reachability 语言矩阵、VEX 功能点、CRA 营销动作）：见 [03](03-competitive-landscape.md) 各厂商分节，本报告未重抄。
- Reachability/Exploitability/Evidence Graph 的理论方法与壁垒论证、GUAC/Wiz 存储反叙事、AIxCC/Agent Fix/CCR 架构实证：见 [04](04-technology-deep-dive.md)；本报告仅在"业界实际组件"层面新增证据（Trivy fanal、Semgrep 引擎、Tracee、GrypeDB、DT-Postgres、air-gapped KB 等）。
- 凡数字类声明（降噪率、覆盖量、修复时效）均为厂商声称，以 [04](04-technology-deep-dive.md) 的保守口径为准。
