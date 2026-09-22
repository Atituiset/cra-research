# 01 · 领域知识地图（Know the Domain）

> 对应 `docs/mvp.md` §十八 的 #2/#4/#7/#8。本章目标：把"漏洞数据体系 → 供应链物料 → 判定 → 修复"的所有概念串成一张可复用的心智模型，后续章节（问题定义、reachability、remediation、竞争）都挂在这张图上。
> 证据标记：`[R1#n]` 等指 `research/0X-sources.md` 行号；`[EUR-Lex]` 指 Regulation (EU) 2024/2847 官方文本。

## 0. 一张图看全链路

```
软件供应链上游                          漏洞管理决策下游
────────────────────────────────────────────────────────────────
源码仓库 ──> SBOM（组件+版本+PURL/CPE）
                │
CVE / OSV / GHSA / 厂商 advisory ──> 多源情报归一（别名消解、区间对齐）
                │
NVD / CPE ──────────────┘         EPSS（概率）/ KEV（已被利用事实）
                │                        │
        组件匹配（版本区间 / backport）   │
                │                        │
        Reachability（这段代码会被执行吗）
                │                        │
        Exploitability（真实环境可被利用吗）
                │                        │
        VEX 判定（affected / not_affected / fixed / under_investigation）
                │                        │
   ┌────────────┴────────────┐           │
修复（升级 / backport / 配置 / 缓解）  事件响应（24h/72h 报告义务）[EUR-Lex Art.14]
   │
验证（复扫 / 单测 / runtime 观测）
   │
审计留痕（Evidence Graph：每个结论挂证据）
   │
CRA 合规产物（SBOM、处理记录、技术文档 10 年）[EUR-Lex Annex I/III]
```

**读图要点**：左边是传统 SCA 的地盘（组件→CVE 匹配），中间两条判定层（Reachability / Exploitability）是 2024-2026 的技术主战场，右边 VEX/事件响应/证据留痕是 CRA 带来的合规增量。竞品大多集中在"匹配+优先级"，而 **VEX 判定 + 修复验证 + 证据留痕** 是本报告论证的空位。

## 1. 概念分类：先别把名词混在一起

背景材料（`docs/background.md` §十四）要求区分 9 类对象。产品与文档中必须严格分开：

| 类别 | 定义 | 例子 | 常见混淆 |
|------|------|------|----------|
| **Identifier** | 单条记录的稳定 ID | CVE-2021-44228, GHSA-xxxx, OSV-2020-xxx | CVE 是 ID 不是数据库 |
| **Database / Source** | 存放记录的仓库 | NVD, OSV, GHSA, 厂商 advisory DB | NVD ≠ CVE Program |
| **Data format / Schema** | 记录的序列化格式 | CVE JSON 5.x, OSV schema, CVSS JSON | OSV 既是格式也是事实库 |
| **Standard / Spec** | 被组织背书的规范 | SPDX(ISO 5962), CycloneDX(ECMA-424), CSAF(OASIS) | 标准 ≠ 强制 |
| **Scoring** | 给漏洞打分的方法 | CVSS v3.1/v4.0, EPSS | CVSS 是严重度不是概率 |
| **Threat intel** | 是否已被利用的情报 | CISA KEV, 真实利用日志 | KEV 是事实清单不是打分 |
| **Analysis result** | 厂商/研究者的判断 | Reachable? Exploitable? 暴露面 | 判断要挂证据 |
| **Compliance artifact** | 交付给监管/客户的物料 | SBOM, VEX, 事件报告 | SBOM 不是 SCA 结果 |
| **Framework** | 体系性方法 | SSDF, SLSA, CISA Secure by Design | 框架不含具体数据 |

> [来源: docs/background.md §十四] 本表直接复用背景材料的分类法，报告后续所有名词均按此归类。

## 2. 漏洞标识与记录层（Identifier + Database）

### 2.1 CVE — 事实上的全球编号系统
- 由 **CVE Program** 运作（The MITRE Corporation 任秘书处，CVE Board 治理，全球 CNAs 分布式编号）[基于公开资料]。
- CVE 是**一条漏洞的编号+描述记录**，不是可查询的漏洞数据库——查询、打分、匹配要靠 NVD/厂商库。
- **Log4Shell（CVE-2021-44228）** 常被用作教学案例：受影响产品数百个、上游 log4j 2.14.1 修复、各发行版 backport、下游嵌入式/云服务层层传递——**一个 CVE 对应"产品×版本"的多状态**，这正是单一 CVE→组件匹配模型失真的根源。
- 记录格式为 **CVE JSON Record Format 5.x**（现在是 5.2.0），其中 **2025 年已把 PURL 纳入 CVE 记录字段**（见 §6）。[R1#3]

### 2.2 CWE — 病因分类学
- CWE 是 MITRE 维护的**软件/硬件弱点分类**（对应"是什么类型的代码缺陷"），CVE 是"某个具体实例被谁发现"。
- 对本产品的意义：CWE 决定 **修复建议的泛化能力**（按 CWE-89 给 SQL 注入的通用 recipe），也是 SAST 规则映射的主键；SCA 场景下 CWE 粒度较粗（依赖漏洞通常映射到若干顶层 CWE）。
- 量级：CWE 列表 ~944 条（v4.x 量级）[基于公开资料；本轮未重抓 MITRE 列表页]。

### 2.3 NVD — 官方"增强层"，以及它的 2024-2026 危机
NVD 由 NIST 运营，在 CVE 记录之上补充：CPE 平台匹配、CVSS 打分、CWE 映射、引用链接、KEV 关联。**SCA 工具的版本匹配长期依赖 NVD 的 CPE + 版本区间。**

关键时间线（本轮从 NVD 官方 news 核实）[R1#7]：
| 时间 | 事件 | 对产品的影响 |
|------|------|-------------|
| 2024 年 | NVD 漏洞 enrichment 积压危机（响应变慢、补全滞后）| SCA 厂商开始被迫自建打分/匹配 |
| 2025-03-01 | 恢复 backlog 清零计划 | 阶段性恢复 |
| **2026-04-15** | **改为 risk-based enrichment**：只有 KEV 列表内、联邦政府软件、关键软件才做全量补全 | **大量 CVE 不再有官方 CPE/CVSS/CWE 补全** |
| 2026 年 | 2026-03-01 前未补全的存量 CVE 转入 "Not Scheduled" | 下游若只信 NVD，会出现"无数据的漏洞"黑洞 |

**产品含义（本报告核心论断之一）**：单一 NVD 依赖已不可行。产品的"多源情报归一"能力（NVD + OSV + GHSA + 厂商 CSAF/advisory + 自有研究）从"锦上添花"变成**结构性必需**，也是新进入者相对 NVD 依赖者的护城河。[R1#7]

### 2.4 OSV / GHSA / 厂商 Advisory — 生态原生的第二套体系
- **OSV**：开源漏洞格式（Google 主导，schema 定义 `affected[].ranges` 语义化版本区间、`database_specific` 扩展），本身就是**事实数据库**（聚合 OSS-Fuzz、各生态、GHSA 等）[R1#2]。其 `ECOSYSTEM`/`SEMVER`/`GIT` 三种 range 语义比 CPE 更贴近包管理器现实。
- **GHSA**（GitHub Security Advisories）：GitHub 自有 advisory 库，**Dependabot 的告警数据源**（只对 GitHub 审核过的 advisory 触发告警）[R6#5]，覆盖 npm/pip/maven/go 等生态最全的一手来源之一。
- **厂商 advisory**：Red Hat（CSAF/VEX/每 CVE 一页）[R2#12]、Debian（按 suite 标注 vulnerable/fixed）[R1#11]、Ubuntu（按 release 状态）[R1#13]、Microsoft、各上游项目。**backport 现象**（见 §4.2）使"版本号比较"失效，必须读发行版状态。
- 三者与 NVD 的关系：**同一漏洞多 ID、多区间、多状态**，产品必须做别名消解（alias resolution）+ 区间对齐 + 状态合并——这是 "关联（Associate）" 环节的技术难点。

## 3. 打分与情报层（Scoring + Threat intel）

### 3.1 CVSS — 严重度，不是被利用概率
- 现行 **CVSS v4.0**（FIRST 维护），引入 base/threat/environmental 三组，**新增 Exploit Maturity、Automatable、Recovery、Provider Urgency 等轴** [R1#4]。
- v4.0 的 `ExploitMaturity=Attacked` 与 KEV/实战利用直接挂钩——这是 CVSS 官方承认"利用情报应进入打分"的信号。
- **产品要点**：CVSS 9.8 ≠ 该修的第 1 名。只按 CVSS 排队是传统 SCA 噪声的来源之一。

### 3.2 EPSS — 被利用的概率（量化概率，非分数通胀）
- FIRST 的 **Exploit Prediction Scoring System**：给出未来 30 天被利用的**概率**（0-1），每日更新，模型基于真实利用数据训练 [R1#5, R1#12]。
- 使用要点（来自 FIRST 官方 use-cases 文档 [R1#12]）：
  - EPSS 阈值应与 CVSS 联用（例如 "CVSS≥9 且 EPSS>0.1" 作为 patch 窗口）；
  - 语义是**概率**，不能当"风险分"线性加到 CVSS 上；
  - 与 KEV 的关系：KEV 是**已发生**的事实，EPSS 是**未来**的概率——两者互补而非替代。
- EPSS 聚合公式（多漏洞组合暴露）：`组合风险 ≈ 1 - Π(1-p_i)`，用于"一次升级消掉多个 CVE"的收益量化。

### 3.3 CISA KEV — "已被利用"的事实清单
- CISA **Known Exploited Vulnerabilities** catalog：权威、免费（CSV/JSON）、字段含 due date、勒索软件关联、**BOD-26-04 新增 forensic triage 要求**；2026-09 时点约 **1,716 条** [R1#8]。
- **KEV 的产品含义**：CRA 场景下（详见 02 章），"actively exploited" 触发 **24h/72h 报告义务** [EUR-Lex Art.14]——KEV 不只是优先级信号，是**合规触发器**。
- **组合模型（本报告推荐的优先级栈）**：
  `最终优先级 = f(组件在产品中存在, 版本匹配可信, Reachable, EPSS, KEV/已观测利用, CVSS/严重度, 资产关键度, 网络暴露)`
  ——四家 reachability 厂商（Endor/Semgrep/Snyk/Oligo）与 FIRST 都强调这是一组**证据加权的决策**，不存在单一分值。[R4#1, R1#12]

## 4. 组件识别与匹配层（Identifier 规格）

### 4.1 CPE vs PURL — 两套坐标系，必须共存
| | CPE (NIST) | PURL (package URL) |
|---|---|---|
| 目标粒度 | 平台/产品/包（面向"软件"） | 包管理器坐标（面向"包"） |
| 表达 | `cpe:2.3:a:apache:log4j:2.14.0:...` [R2#8] | `pkg:maven/org.apache.logging.log4j/log4j-core@2.14.0` [R2#7] |
| 权威 | NVD/CVE 体系默认 | SBOM/SCA 生态事实默认，**2025 已进 CVE 记录 5.2.0** [R2#7] |
| 短板 | 无法精确表达语言包生态（groupId/artifactId 丢失）| 需回译到产品语境才能对上 NVD CPE |
- **产品含义**：归一化必须做 **PURL ↔ CPE 双向映射** + 生态别名，否则在 NVD risk-based enrichment 后会出现"有 PURL 无 CPE 数据"的断档。

### 4.2 版本匹配的三个坑（问题定义的证据）
1. **语义化区间 vs 字符串比较**：各生态版本规则不同（Debian `1.2.3-4+deb12u1`），必须用生态原生比较器。
2. **Backport**：Debian/Ubuntu/RHEL 常把安全修复回移到**不改版本号**的构建里 [R1#11, R1#13]——"版本在受影响区间"≠"真的受影响"。发行版状态（vulnerable/fixed per suite/release）才是真相。
3. **区间数据源打架**：同一 CVE 在 NVD/OSV/厂商处的受影响区间不一致；NVD 收缩补全后（§2.3）不一致会加剧。产品必须展示**区间来源与置信度**，而不是静默选一个。

> 结论（挂到 03 章问题定义）：**"组件→CVE"匹配看似简单，实际是五层不确定性叠乘**：数据源完整性 × 区间正确性 × backport 处理 × 别名消解 × 及时性。传统 SCA 的"高误报"不是玄学，是这五层的乘积。

## 5. 物料清单层（Compliance artifact：SBOM）

### 5.1 SBOM 是什么（以及它不是什么）
- SBOM = **给定时刻、单个软件工件的组件清单 + 层级关系 + 许可证 + 安全属性**的机器可读快照 [R2#13]。
- **SBOM ≠ SCA**：SBOM 是"我里面有什么"（声明），SCA 是"里面有什么漏洞"（分析+判定+修复）。SBOM 是 SCA 的**输入之一**与**输出之一**，但不包含判定逻辑。[R2#13, 背景材料 §十]
- CRA 官方措辞（**CRA 对 SBOM 的法律锚点，必须原样引用**）[EUR-Lex Annex I Part II]：
  > "…identify and document vulnerabilities and components contained in the product … including by drawing up **an SBOM in a commonly used and machine-readable format covering at the very least the top-level dependencies**…"
  - 关键点：**至少顶层依赖**（top-level dependencies）是法定底线；"常用且机器可读的格式"未点名 SPDX/CycloneDX；Commission implementing acts 可进一步规定格式（Annex I 与授权条款）——**格式选择是合规风险敞口，不是自由**。

### 5.2 两大格式与"格式之争"的现状
| | SPDX | CycloneDX |
|---|---|---|
| 背书 | **ISO/IEC 5962**（ISO 标准）[R2#4] | **ECMA-424**（ECMA 标准，OWASP 孵化起家）[R2#3] |
| 定位 | 许可证/合规出身，3.0 补安全模型 | 安全出身，vulnerabilities/VEX/声明/组合/formulation 原生 |
| 安全扩展 | SPDX 3.0 security profile | `vulnerabilities` 字段 + **VEX 内嵌** + declarations（合规即代码）+ citations（证据溯源）[R2#3] |
- **产品立场建议**（供 04/09 章决策）：**内部统一图模型，导出双格式**（SPDX 合规出口 + CycloneDX 安全出口）。格式只是序列化，证据图（§8）才是产品资产。CRA 未指定格式，押注单一格式有押错风险。
- CISA 最小要素：2021 NTIA 七要素已由 **2026-07-29 CISA/NSB "Minimum Elements"** 接替 [R2#16]——设计产品时按 2026 版要素对齐，别再引用 NTIA 2021。

### 5.3 SBOM 质量 = 产品的隐藏卖点
- 常见缺陷：缺版本、缺 PURL、依赖关系不全、license 错误、构建/交付时点陈旧 [R2#13]。
- **产品机会**：SBOM 质量评分 + 差异对比（两版 SBOM diff = 变更审计），可直接服务 CRA 的"持续更新 + 10 年技术文档"义务。

## 6. 判定与状态层（Analysis result + Compliance artifact：VEX / CSAF）

### 6.1 为什么需要 VEX —— SBOM∩Advisory 的天真模型会爆炸
- 天真模型："把 SBOM 和 CVE 流做笛卡尔积，命中的都算受影响" → 一个严重 CVE 命中数千组件，全量告警不可执行 [R2#17, R4#1]。
- VEX 回答的唯一问题：**"这个产品，在这个版本，对这个漏洞，到底什么状态，为什么"**。
- CISA 官方定义（**VEX 是一种 attestation / advisory 形态**）[R2#16]：
  > "a statement that reflects whether a vulnerability in a product could or could not be exploited… **at minimum a status of affected, not affected, fixed, or under investigation**… **justification** for that status."

### 6.2 四状态 × 四 justification —— 判定词汇表
| Status | 语义 | 典型 justification（CISA/规格定义） |
|---|---|---|
| `affected` | 确实受影响，未修复 | —（常附已知利用情报） |
| `not_affected` | 不受影响 | **vulnerable_code_not_present** / **vulnerable_code_not_in_execute_path**（≈ reachability 不可达）/ **cannot_be_controlled_by_adversary** / **inline_mitigations_already_exist** |
| `fixed` | 已修复 | 指向 fix 版本/commit |
| `under_investigation` | 调查中 | 证据不足的默认态 |
- **战略含义（04/06 章的核心论点）**：`vulnerable_code_not_in_execute_path` 就是 Reachability 分析的**合规化表达**。也就是说——**reachability 技术在 VEX 语义里有了官方词汇表**，"可达性分析→VEX 状态"是天然产品闭环，而不是两个割裂功能。

### 6.3 四种 VEX 实现 = 一个抽象，四种序列化
| 实现 | 宿主规范 | 归属组织 | 要点 |
|---|---|---|---|
| CycloneDX VEX | CycloneDX（ECMA-424）[R2#3] | OWASP→ECMA | 内嵌在 SBOM 的 `vulnerabilities[]`，交付一体 |
| CSAF 2.0 + VEX Profile | CSAF 2.0（OASIS 标准）[R2#9] | OASIS | 企业公告/协调流原生，profile 化表达 VEX |
| OpenVEX | 独立极简规范 | vexdevrokta/vex[营销]，中立 | 极简 JSON，主打跨工具可移植 |
| SPDX 3.0 security profile | SPDX 3.0 [R2#4] | Linux Foundation | 与 ISO 认证的 SBOM 绑定 |
- **"VEX 是格式还是结果？"（背景 §十）**——结论（本报告采用）：
  - **VEX 的本质是"带理由的状态判定（analysis result）"**；上表四种只是它的**运输格式**。
  - 产品必须把 **VEX 判定的生成（证据驱动）** 与 **VEX 的导出（多格式）** 分层——判定引擎是差异化，格式导出是兼容性。
  - 2026-09 时点无强制 VEX 格式；但 CRA 的"可提交给市场监管机构的文档"事实要求 + 供应链传导（客户要 VEX 文件）已在市场制造事实标准压力 [基于公开资料推断]。

### 6.4 CSAF — 协调公告的容器
- OASIS **CSAF 2.0** 标准（CVRF 的继任者），定义 provider/aggregator 分发、`/.well-known/csaf`、CSAID 标识、**VEX profile** [R2#9]；Red Hat 的每 CVE CSAF/VEX 文件是事实参考实现 [R2#12]。
- 与本产品关系：**CSAF 是"厂商如何向下游发布 VEX"的通道**；我们的产品既要**摄取**下游厂商 CSAF/VEX，也要**产出**自己的 VEX（选格式见 §6.3）。

### 6.5 官方 VEX 指南（判定流程的产品化模板）
- CISA **When to Issue a VEX**（2023-11-06，HTTPS-only 发布）[R2#17] 给出何时必须更新状态、何时可以 not_affected、如何传播——这几乎就是我们 VEX 工作流的需求文档雏形。
- **产品化**：把"调查中→判定→发布→再评估（新证据/新版本触发）"做成**有 SLA 的状态机**，每次迁移挂证据（见 06 章 Evidence Graph）。

## 7. 标准与框架总表（备查）

| 名称 | 类型 | 权威 | 与本产品关系 |
|---|---|---|---|
| SPDX | SBOM 格式标准 | ISO/IEC 5962 + Linux Foundation [R2#4] | 合规导出 A 面 |
| CycloneDX | SBOM+安全格式标准 | ECMA-424 [R2#3] | 合规导出 B 面，VEX/安全字段更全 |
| CSAF 2.0 | 公告/交换标准 | OASIS [R2#9] | 下游 VEX 摄取通道 |
| OpenVEX | VEX 极简格式 | 社区 [R2#5] | 可移植导出 |
| PURL | 组件坐标 | ECMA（2025 进 CVE 5.2.0）[R2#7] | 归一化主键之一 |
| CPE | 产品坐标 | NIST [R2#8] | NVD 匹配桥 |
| CVSS v4.0 | 打分 | FIRST [R1#4] | 严重度轴 |
| EPSS | 概率预测 | FIRST [R1#5] | 概率轴 |
| KEV | 利用事实 | CISA [R1#8] | 合规触发 + 概率轴校准 |
| SSDF (SP 800-218) | 流程框架 | NIST [基于公开资料] | 客户能力审计框架 |
| SLSA | 供应链完整性等级 | Google→OpenSSF [基于公开资料] | 构建侧信任（与产品弱相关）|
| Secure by Design / CISA 2026 SBOM 最小要素 | 政策指引 | CISA [R2#16] | 对齐客户合规话术 |
| IEC 62443 / ENISA SBOM guidance | OT/SBOM 指引 | ENISA [基于公开资料] | 欧盟客户背书引用 |

## 8. 心智模型：一段话串起来（背景 §十五 的产品化版本）

> 我是一家欧盟制造商，卖出的产品里**装着什么**由 SBOM（PURL 坐标）说清楚；外面的世界每天冒出**新的坏消息**（CVE/OSV/GHSA/厂商 advisory，经别名消解归一）；我必须判断**这个坏消息是否击中我的产品版本**（区间匹配 + backport + NVD risk-based 数据缺口）；命中之后，还要判断**代码路径是否可达、环境是否可利用**（Reachability/Exploitability）；据此作出**带理由的正式判定**（VEX 四状态），该修的走**修复→验证**闭环，涉主动利用/严重事件的走 **24h/72h 报告义务**（ENISA SRP）；全程每个结论**挂可审计证据**（Evidence Graph），最终沉淀为 **CRA 10 年可提交的技术文档**。
> **产品就是把这段话变成一个工作流系统。** [EUR-Lex; R2#16; R2#17; R1#7; R6#1]

---
*本章引用来源：R1（漏洞情报）、R2（标准/SBOM/VEX）、R3+EUR-Lex（CRA）、R4（reachability）、R6（agent/证据图）。逐源笔记见 `research/0X-sources.md`。*
