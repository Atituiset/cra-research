# Vendor Deep Dive: Snyk（第二轮 Competitive Deep Dive）

- 调研日期: 2026-09-21
- 调研人: 研究子代理（Kimi Code CLI）
- 前置文档: [03-competitive-landscape.md §1.1/§6](../03-competitive-landscape.md)、[04-technology-deep-dive.md](../04-technology-deep-dive.md)、[06-product-forms-and-tech-stacks.md](../06-product-forms-and-tech-stacks.md)
- 范围: 不重复基线结论，只做技术实现与深度挖掘；每条重要事实附 URL 与来源层级。
- 分级约定: **[F]**=Fact（一手来源可核）／**[I]**=Interpretation（基于事实的解读）／**[H]**=Hypothesis（推测，待验证）；营销页声明标"（厂商声称）"；无法核实标（不确定）。

---

## 0. 摘要

Snyk 的技术护城河不在任何单个扫描器，而在三个互相喂数据的资产：**人工+AI 策展的漏洞库（含 35,000+ 专家修复样本）、DeepCode 血统的程序分析引擎、"generator ≠ validator"的确定性验证层叙事**。2026 年的 Snyk 已经把这三者打包成 Evo 平台并拿到商业验证（新单额 60%，厂商声称）。对我们最关键的参照系：它的 reachability 引擎是**自研符号分析 + agentic 决策混合**、结论会随引擎升级漂移且官方自认假阴性；它的 Risk Score 因子全公开且 reachability "只加不减"；它的对象模型距 product/version 仍隔一整层；它的修复合并率首次有了公开数字（94% 相对提升），但绝对合并率/回归率全行业仍无人公布。

---

## 1. 漏洞数据库策展

### 1.1 策展管线与人机分工 [F]

Snyk Security R&D Group 自述（[Human + AI: The Next Era of Snyk's Vulnerability Curation, 2025-07-14](https://snyk.io/blog/human-ai-the-next-era-of-snyks-vulnerability-curation/)）：

- 起点是"分析师在一个大 JSON 文件里手工策展"；现在 AI agent 承担五类角色：**lead generation（全网找早期信号）、code analysis（监控 commit 比对代码变更，用私有静态引擎识别可疑修复）、prioritization、data enrichment（RAG 从人工验证过的库检索建议元数据）、post-publication monitoring（追踪 fix/backport/新 exploit）**。
- 人工保留的判定清单（原文）：是否真漏洞、受影响包、版本区间、fix 可用性、CVSS vector、已知 exploit、CVE ID、CWE。
- 人机闭环官方表述为 **HITL + RLHF**；工程质量机制为 **eval-driven development（分析师给 LLM 写 eval）+ LLM-as-a-judge（模型互评 accuracy/hallucination）**；自训 commit 分类模型。
- **内部已建集中式 MCP Server** 包裹"全部安全工具、内外部 API"，分析师用自然语言交叉比对 commit 与漏洞库、直接更新记录——MCP 先在策展团队内部落地（2025-07），早于对外 Snyk Studio 产品化。[F]
- 人工 vs AI 的**定量比例未披露**（不确定；只能定性为"AI 做线索/富化/排序，人做最终判定"）[I]。

### 1.2 与 NVD 的差异策略 [F]

（[Snyk users don't have to worry about NVD delays, 2024-03-13](https://snyk.io/blog/snyk-users-dont-have-to-worry-about-nvd-delays/)）

- 每条开源 advisory 自带包坐标、漏洞版本区间、CVSS vector，"regardless of what other sources provide"；CLI 输出可见 `cvssSources` 中 **Snyk=primary、NVD=secondary**（[reachability 文档 JSON 示例](https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis)）。
- **收录不等 CVE 分配**："NVD only analyzes vulnerabilities with CVE IDs; the Snyk Security Team analyzes vulnerabilities regardless of their CVE ID assignment status."
- 数据源五类：结构化社区库（RubySec 等）、官方库（NVD）、ML 挖掘未编目漏洞、社区/学术披露协作、自有研究（Leaky Vessels 等）；Snyk 是 CNA，有公开披露流程（[labs.snyk.io/vulnerability-disclosure](https://labs.snyk.io/vulnerability-disclosure/)）。

### 1.3 披露时间优势的可考证据

- [F] 官方定量声明（2024-03-12 时点）：2023–2024 年 Snyk 库中 **500+ 个 CVE 在 NVD 尚未分析**；举例 CVE-2024-22243、CVE-2024-1597 已入库并分析 **3 周**而 NVD 未动。
- （厂商声称）营销页三指标：**3x** 于"下一个最大公开库"的漏洞量；**92%** 的 JavaScript 漏洞 Snyk 先于 NVD 报告；平均快 **47 天**（[security-intelligence 平台页](https://snyk.io/platform/security-intelligence/)）。无方法学披露，第三方广泛转述。
- [F] 边界自认：容器 advisory 的 severity/CVSS 以 Linux 发行版自评为主；发行版自己透传 NVD 时，**Snyk 也会延迟**——"NVD 免疫"叙事只覆盖开源包侧。

---

## 2. Reachability 实现

### 2.1 引擎底座：DeepCode 自研血统，非 CodeQL [F]

- [reachability 官方文档](https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis)（2026-09-18 更新）五步管线：fix commit 富化（策展流程）→ **DeepCode AI program analysis** 找相关 code elements → DeepCode AI + **NLP** 排根因概率 → 扫描时 **DeepCode program analysis engine** 比对应用 call graph 与依赖间 call graph → 安全专家人工校验回灌。
- 所有官方文档未出现 CodeQL；底座为 2020-09 收购的 DeepCode（ETH Zurich spin-off，symbolic AI 语义分析）。[F]（收购公开记录；[演进汇编](sources/snyk-reachability-evolution.md)）
- 时序细节：Reachable Vulnerabilities **2020-08 首发于 Java**（[首发博客](https://snyk.io/blog/reachable-vulnerabilities/)），早于 DeepCode 收购官宣一个月——reachability 最初是 Snyk 自研的 call-graph 功能，收购后并入 DeepCode 引擎统一演进。[I]

### 2.2 语言与粒度演进 [F]

- 语言：Java（Maven/Gradle）、JS/TS（npm/Yarn/pnpm）、Python（pip/poetry/pipenv）**GA**；.NET（NuGet/paket）**EA**（2026-09 文档）。Python EA 阶段官方称覆盖率已达 "over 99% of applicable vulnerabilities"（[updates.snyk.io 2025-10](https://updates.snyk.io/improvements-to-reachability-for-snyk-open-source/)）。
- 粒度词演进：2020 "vulnerable function" → 2024 "function related to the vulnerability" → 2026-09 "**code element** (functions, classes, modules, and more)"。[F]（文档原文；粒度的实际放宽深度无第三方验证，[I]）
- CLI 化：CLI 1.1301.0+ 支持 `--reachability=true` / `--source-dir` / `--reachability-filter`，但**走新 findings schema（破坏式变更）且 CLI/CI/CD 路径仍 EA**。[F]

### 2.3 2026 年的架构变化：静态 + agentic 混合 [F][I]

- 文档新增表述：DeepCode 分析 "applies **real-time decision-making** to determine whether to under-approximate the set of reachable elements"；"The **agentic capability** of Snyk analysis optimizes..."——reachability 引擎已引入 agentic 成分做欠近似/召回权衡。[F]
- [I] 这解释了为什么 Snyk 敢在官方文档承认假阴性（见 §10）：它把"判不准"从产品缺陷重新定位为"agentic 权衡的设计选择"。

---

## 3. Agent Fix 架构

### 3.1 分工（LLM vs 确定性层）[F]

- 生成侧：前沿 LLM（生产环境 **Claude Opus 4.7**）+ **Snyk Intelligence** = **dynamic few-shot prompting**：修复时按弱点类别注入专家撰写修复样本，来源是 "**more than 35,000 vulnerabilities**" 的 Snyk 库（[Golden Test 基准博客, 2026-08-18](https://snyk.io/blog/snyk-agent-fix-remediation-benchmark/)）。
- 验证侧：所有 auto-fix 先过 **Snyk Code SAST re-scan**（验证可读、修掉原问题、不引入新漏洞）再推给开发者（[04 报告已录](../04-technology-deep-dive/sources/snyk-agent-fix.md)）；基准层用 **secure AND functional 双门**（隐藏单测、首试通过才算）。
- 核心架构声明（原文）："The durable asset is the 35,000-plus expert fixes; **the model is a component we can swap**." [F]

### 3.2 量化结果 [F]（厂商自述基准）

- 裸前沿模型收敛在 72–75%（secure+functional 修复率）；+Snyk Intelligence：Sonnet 4.6 → **82.5%**，Opus 4.6 → **85.4%**（+10.8pt / +14.48% 样本）；Python 提升最大（64%→88%）。
- 上一代内部 StarCoder 模型：支持规则子集 72.4%，**全规则集仅 54.9%**（自曝，说明老模型覆盖面窄）。

### 3.3 合并率/回归率

- [F] 全行业首个公开合并率声明（[2026-09-17 新闻稿](https://snyk.io/news/agentic-ai-security-moves-into-production/)）："Open source issues remediated through Snyk's independent validation layer **merge at a 94% higher rate** than fixes produced by a frontier model working alone."——**相对值，无绝对基线、无样本量、无回归率**。（厂商声称）
- [I] 基准博客的 Limitations 自曝（样本 ~150、snippet 级、只 3 语言、两轮方差）说明 Snyk 自己知道这些数字离"生产可信度遥测"还很远；绝对 merge/regression rate 全行业仍空白（与 03 报告 §3.2 判断一致，本轮加固）。

---

## 4. Evo / AI Trust Platform 与 MCP

### 4.1 四环官方表述 [F]

- 平台页总叙事：Snyk AI Security Platform = "**independent validation layer** for AI-built software"，信条 "the generator cannot be the validator"，"deterministic engines paired with frontier-model reasoning"（[snyk.io/platform](https://snyk.io/platform/)）。
- 四环（[COS GA 新闻稿 2026-08-04](https://snyk.io/news/snyk-launches-evo-continuous-offensive-security/) + [2026-09-17 新闻稿](https://snyk.io/news/agentic-ai-security-moves-into-production/)复述为 continuous security model）：**Discover**（AI-SPM，2026-03 GA）→ **Remediate**（Agentic AppSec：Secrets GA / Remediation Agent **open preview** / 编排 agent private preview）→ **Validate**（COS：AI pentest + agent red teaming，2026-08 GA，消费存量静态发现作上下文）→ **Prevent**（secure at inception gates）。
- 运行规模（厂商声称）：240 万 agent 供应链扫描/月、420 万 agent 行为检查/天、41.7 万纳管机器。

### 4.2 MCP server 实现 [F]

（[Snyk Studio 官方文档](https://docs.snyk.io/agent-security/agentic-security-with-snyk-studio/getting-started-with-snyk-studio)，2026-09-10 更新）

- **形态**：`snyk mcp` 是 CLI 子命令（v1.1296.2+，stdio），**纯本地 MCP server**——"Snyk does not offer a hosted remote MCP server"。扫描在本地执行，LLM 只拿结果。
- **tool 集**：12 个（`snyk_auth / snyk_code_scan / snyk_sca_scan / snyk_container_scan / snyk_iac_scan / snyk_sbom_scan / snyk_aibom / snyk_package_health_check / snyk_version / snyk_logout / snyk_trust / snyk_send_feedback`）。
- **profile 三档**（lite/full/experimental， `--profile` 或 `SNYK_MCP_PROFILE`）——官方承认 MCP tool 消耗 token/context，需要裁剪面。[F][I]
- **双路径落地**：支持 hooks 的 ADE（Claude Code/Cursor/Codex CLI/Gemini CLI/Copilot）走 **hooks-based "secure at inception"**（installer 脚本，repo snyk/studio-recipes 开源可自托管）；其余走 rules-based MCP + directives（Secure at inception / Remediation 两类指令）。
- [I] 内部先行：策展团队的内部 MCP server（§1.1）证明 Snyk 把 MCP 当作自家工具的通用编排层，对外产品化是同一思路的外溢。

---

## 5. Risk Score 组成因子

（[Risk Score 官方文档](https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/risk-score)，2026-09-15 更新；全清单见 [source note](sources/snyk-risk-score-docs.md)）

- [F] 结构：0–1000 = Impact × Likelihood 双子分。Impact = CVSS impact 指标 + Provider Urgency（容器）+ **Business criticality**（Project attribute，默认 high 不影响）；Likelihood 客观因子 = **Exploit Maturity（Snyk 自评四档）/ EPSS（每日更新，恶意包强制置 1，缺省 0.01055）/ advisory 年龄（>1 年降一次）/ CVSS exploitability 指标 / Social Trends / Malicious Package / Package popularity**；上下文因子 = **Transitive depth**（间接依赖降分）与 **Reachability**。
- [F] **Reachability 只加不减**：`Reachable` 升分且 transitive depth 不再计入；`No path found` **不降分**；未启用则不出现。[I] 这意味着 reachability 在 Snyk 里是"升级器"而非"过滤器"——降噪要靠人工看 `NO PATH FOUND`，分数不会替你降。
- [F] 成熟度口径：Risk Score 自 2023-08 公开至 2026-09 **仍 Early Access**；CLI 不可用；API 字段名仍叫 `priority`；Snyk Code/IaC 仍用旧 Priority Score。文档间口径不同步（Risk Score 页写 reachability "supported for Java and JavaScript"，滞后于专页的三语言 GA）。

---

## 6. 对象模型：Project / Target / Org——离 product/version 有多远

（[Snyk Projects 官方文档](https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-projects)，2026-09-15 更新；[source note](sources/snyk-object-model.md)）

- [F] 官方定义：**Target** = "an external resource Snyk has scanned: a code repository, a Kubernetes workload, or another scannable resource"；**Project** = Target 下按 **manifest 文件（Targetfile）× 扫描类型（Type）** 划分的扫描单元；层级 Tenant → Group → Org → Target → Project；Origin 枚举 30+ 来源生态。
- [F] 一个 monorepo 多 manifest → 多 Project；官方为"hundreds of thousands of Projects"规模设计分页。Business criticality 等上下文 attribute 挂在 **Project** 上。
- [I] **距 product/version 的距离 = 一整层映射**：Project 无版本语义（monitor 快照原地覆盖）、无产品线/支持期概念；"哪个产品版本的哪个漏洞"需要用户在 Project 集合之上自建聚合，且 Project↔manifest 的多对一使该映射不平凡。03 报告 §6 的判断本轮获官方文档级加固。
- [H] Evo 的 AI-SPM 在建立"模型/agent/skill 资产清单"对象——这是 Snyk 对象模型里第一次出现"非 repo 锚点"的资产对象；若它向"产品/应用版本"演化，是 Snyk 填补该空白的唯一可能路径。

---

## 7. 交付形态：SaaS-only + Broker 桥接

（[How Snyk handles your data](https://docs.snyk.io/snyk-data-and-governance/how-snyk-handles-your-data) + [Snyk Broker 文档](https://docs.snyk.io/platform-administration/snyk-broker/snyk-broker) + [github.com/Snyk/broker](https://github.com/Snyk/broker)；[source note](sources/snyk-delivery-broker-data.md)）

- [F] 三档部署：Multi-Tenant SaaS / Single-Tenant SaaS（Private Cloud，全托管隔离实例）/ Snyk Broker；区域 US/EU/AU。**无 self-hosted/on-prem 平台形态**。
- [F] Broker 仅 Enterprise plan；本身开源（Apache 系仓库公开）。架构：Server 在 Snyk SaaS 侧，Client 装客户网络内，**client 主动出向发起 WebSocket**（无需开入向端口），凭证不出边界，访问收敛到 **approved data list** 白名单。Universal Broker（云端配置、单 connection 多类型、Org 映射、API 管理）目标是完全取代 Classic。
- [F] 数据留存边界（隐私设计的一手证据）：reachability/SAST 分析时短暂上传源码，**分析完即删，只留 call graph + 函数名**（SAST 留 issue 位置/ID/解释）；源码缓存受云厂商最短生命周期限制（AWS S3 24–48h）；Snyk Code **不用客户代码训练引擎**；容器镜像副本分析后删除。SOC 2 Type II + ISO 27001/27017。
- [I] 对私有部署需求（CRA 下的制造业/OT 客户尤其敏感）Snyk 的答案是"数据最小化上传 + 单租户"，而不是"平台下沉"——这对我们是机会窗口（见 §11）。

---

## 8. 数据底座可考证据

- [F] 漏洞库规模与更新：35,000+ 漏洞（修复样本库口径，基准博客）；营销页称 3x 于次大公开库（厂商声称）；第三方转述 Snyk 年报称 2024 年新增 24,000+ 条（厂商声称经转述，（不确定）原文）。
- [F] 数据资产互相喂的流程证据：fix commit → reachability 根因标注（§2）；人工验证漏洞库 → RAG 富化新 advisory（§1）；35k 专家修复 → Agent Fix few-shot（§3）；静态发现 → COS pentest 上下文（§4）。
- [F] 平台运行遥测（厂商声称，2026-09-17）：2.4M agent 供应链扫描/月、4.2M 行为检查/天、417k 机器、4,800+ 客户。
- [F] 研究产出产品化：VulnBench JS 1.0（[arXiv:2606.15762](https://arxiv.org/abs/2606.15762)，数据集公开于 vulnbench.com）——把"LLM 检测不可重复"做成公开学术资产来支撑自家架构叙事。
- （不确定）Snyk 内部存储/图数据库栈（Postgres? 图库?）未见工程博客披露；数据底座的"基础设施层"无一手证据。

---

## 9. 定价模型：contributing developer 计费细节

（[plans 页](https://snyk.io/plans/) + [Usage settings 文档](https://docs.snyk.io/platform-administration/snyk-hierarchy/usage-settings)；[source note](sources/snyk-pricing-usage.md)）

- [F] 定义（官方双来源一致）："developers who have made a **commit to a private repo monitored by Snyk in the last 90 days**"；公开仓库不计；按 **git author email** 去重，跨集成/仓库只计一次。
- [F] 档位：Free $0（5 Projects；测试配额 OS 400/Code 100/IaC 300/Container 100 次每月）→ Team $25/月/dev（100 Projects）→ **Ignite $1,260/年/dev**（<50 人组织的 Enterprise 下放档，2026 新设）→ Enterprise 询价。产品可单买但须同 plan。
- [F] 新计费体系并行出现：**Snyk Credits / Platform Access plan**（Tenant 级 credits 消耗 + billable events log）——从纯 seat 向平台用量计费演进中。（credits 换算率未展开，待补）
- [I] 90 天窗口设计的副作用：席位随人员流动自然释放，但也意味着"只在发版季活跃的开发者"仍计费 3 个月；git email 去重对多邮箱开发者会虚高（社区已知问题，非官方承认）。
- [I] 计费计数本身需要读 90 天 commit 元数据——定价机制与数据访问深度绑定，是私有部署客户的摩擦点。

---

## 10. 工程博客/官方文档自曝的局限

1. [F] **Reachability 假阴性**（官方文档原文）："just because there is no evidence of this does not mean that the element cannot be reached... incomplete information, control flow issues, **potential dynamic behaviors**, or overlooked edge cases"；反射场景无法精确回答，引擎实时决定欠近似程度；`NO PATH FOUND` ≠ 不可达不可利用。
2. [F] **结论漂移**："vulnerabilities labeled as Not path found **can change to Reachable over time**"；Java Reachability Engine 升级公告自认会把存量漏洞改判 reachable 并提醒"may affect your triage workflows"（[updates.snyk.io](https://updates.snyk.io/improvements-to-reachability-for-snyk-open-source/)）。规模上限：≤300k 文件 / ≤3GB。
3. [F] **Risk Score 长期 EA**：2023-08 发布至今未 GA；CLI 不可用；API 字段名遗留 `priority`；文档间语言覆盖口径不同步。
4. [F] **老 Agent Fix 模型覆盖窄**：StarCoder 全规则集修复率仅 54.9%（基准博客自曝）。
5. [F] **LLM 检测不可重复**（自家 VulnBench 论文）：~50% 的 LLM-only findings 在 5 次相同运行中只出现 1 次；最佳模型对 Snyk 参考集 75.4%；且作者自注参考集取自 Snyk Code 有**循环性风险**。
6. [F] **容器 advisory 的 NVD 透传延迟**（§1.3）；CLI reachability 的新 findings schema 是破坏式变更（官方提醒检查自动化）。
7. [I] 汇总：Snyk 的透明度策略是"把局限写进文档和论文，换取架构叙事的可信度"——这在买方尽调中是加分项，也说明这些局限（假阴性、漂移、LLM 不确定性）是行业结构性问题而非 Snyk 独有。

---

## 11. 对我们产品的启示

1. **"判定证据"是 Snyk 留出的最大空档**。Snyk 有 call path、有 Risk Score 因子、有 94% 合并率声明，但：reachability 结论会漂移且官方承认、Risk Score 对 no-path 不降分、判定不落 VEX、对象模型无 product/version。**我们应把"判定"做成一等对象（Assessment = Claim + Evidence + Decision，可版本化、可被新情报触发失效重估、自动落 VEX statement），锚定在 Product/Version 上**——这正是 03 报告 §4/§6 定位空白的深挖加固，Snyk 本轮证据让空白更硬而非更软。
2. **"模型可换、资产不可换"的资产观值得直接借用**。Snyk 明说 35k 专家修复库是 durable asset、模型是可换组件；我们的等价物应是**策展后的漏洞-证据-判定知识库**（含 fix commit 富化、根因标注、判定历史），所有 LLM 功能（修复、triaging、报告生成）都应设计为"从该库检索增强 + 确定性校验"，并积累自己的 eval 集（Snyk 的 eval-driven development + LLM-as-judge 是可复制的工程机制）。
3. **交付形态差异化**：Snyk SaaS-only + Broker（数据最小化上传）在 CRA 高敏行业（制造业/OT/国防供应链）留出自托管缺口；我们若以"可私有化部署 + 本地证据库"为形态，配合 product/version 对象模型，可以接住 Snyk 结构性地接不住的客群。同时注意 Snyk 的隐私话术（"分析完即删、只留 call graph"、不用客户代码训练）已是买方尽调基线，我们的数据处理文档需达到同等颗粒度。

---

## 12. 无法核实项清单

1. 策展管线中人工 vs AI 的**定量比例**（官方只有定性分工）。（不确定）
2. "3x 漏洞量 / 92% 先于 NVD / 47 天更快"的**方法学**（营销页无披露）。（厂商声称）
3. 94% 合并率提升的**绝对基线、样本量、统计口径**；Agent Fix 生产环境绝对 merge rate / regression rate。（厂商声称，全行业空白）
4. Snyk 内部数据基础设施栈（存储/图引擎选型）——无工程博客披露。（不确定）
5. Snyk Credits 计费体系的**credit 换算率与 billable event 目录**（在 Policies 页，本轮未展开）。（待补）
6. reachability "code element" 粒度放宽后，类/模块级根因的**实际覆盖深度**——无第三方验证。（不确定）
7. Evo COS 的 AI pentest 误报率/覆盖率——只有厂商叙事与客户引言，无独立评测。（厂商声称）
8. Java Reachability Engine 升级的具体技术变更内容（changelog 只告知影响，不披露细节）。（不确定）

---

## 附：本轮 source notes 索引

| Note | 内容 |
|---|---|
| [sources/snyk-reachability-analysis-docs.md](sources/snyk-reachability-analysis-docs.md) | reachability 官方文档深挖（五步管线/agentic 欠近似/CLI/限制/假阴性） |
| [sources/snyk-risk-score-docs.md](sources/snyk-risk-score-docs.md) | Risk Score 因子全清单 + EA 口径 |
| [sources/snyk-vuln-curation-ai.md](sources/snyk-vuln-curation-ai.md) | Human+AI 策展（五角色/RLHF/eval/内部 MCP） |
| [sources/snyk-nvd-independence.md](sources/snyk-nvd-independence.md) | NVD 差异策略与时差证据（500 CVE/3 周/92%/47 天） |
| [sources/snyk-studio-mcp.md](sources/snyk-studio-mcp.md) | Snyk Studio / MCP server 实现（local-only/12 tool/profile） |
| [sources/snyk-evo-production-metrics.md](sources/snyk-evo-production-metrics.md) | Evo 生产指标新闻稿（94% 合并率/规模遥测/四环最新口径） |
| [sources/snyk-agent-fix-benchmark.md](sources/snyk-agent-fix-benchmark.md) | Golden Test 基准全文要点 + Limitations |
| [sources/snyk-vulnbench-arxiv.md](sources/snyk-vulnbench-arxiv.md) | VulnBench arXiv 论文要点 + 循环性自注 |
| [sources/snyk-delivery-broker-data.md](sources/snyk-delivery-broker-data.md) | 部署形态/Broker 架构/数据留存边界 |
| [sources/snyk-pricing-usage.md](sources/snyk-pricing-usage.md) | 定价四档 + contributing developer 机制 + Credits |
| [sources/snyk-object-model.md](sources/snyk-object-model.md) | Project/Target/Org 官方定义 + product/version 差距分析 |
| [sources/snyk-reachability-evolution.md](sources/snyk-reachability-evolution.md) | reachability 时间线 + DeepCode 血统 + 结论漂移公告 |
