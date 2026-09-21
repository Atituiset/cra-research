# 07. 第二轮厂商深度技术调研：横向汇总（2026-09-21）

> 本目录是第二轮 Competitive Deep Dive：对 [03 报告](../03-competitive-landscape.md) §6 闭环核实过的五家厂商（Endor Labs / JFrog / Snyk / Sonatype / Black Duck）做技术实现级深挖。本 README 是横向汇总；各厂商主文档自带 sources/ source notes 与 research-log（过程记录）。
>
> 分级约定：**Fact** = 有一手来源（官方文档/官方代码/官方工程博客）；**（厂商声称）** = 营销页/新闻稿；**Interpretation** = 基于 Fact 的推断；**Hypothesis** = 方向性猜测。本汇总只引用各厂商文档中已分级核实的内容，不新增未核实表述。

## 0. 五家一句话技术画像

- **Endor Labs**（[endor-labs.md](endor-labs.md)）：自研确定性程序分析引擎（FASTEN/Eclipse Steady 学术谱系）+ 服务端 per-package-version 预计算调用图资产 + 上层 agentic 编排层（MCP/AURI）的三层结构；C/C++ 走与主引擎完全隔离的"哈希+embedding 相似度"路线。
- **JFrog**（[jfrog.md](jfrog.md)）：checksum 组件图（PostgreSQL）寄生在 Artifactory 之上；exploitability 判定靠人工策展的 per-CVE scanner 规则库（1,600+ CVE）；五家中唯一把判定证据做成密码学对象（DSSE/in-toto Evidence）、唯一把对象模型推进到 application 一级（AppTrust）。
- **Snyk**（[snyk.md](snyk.md)）：护城河是三份互相喂数据的资产——Human+AI 策展漏洞库（35,000+ 专家修复样本）、DeepCode 血统程序分析引擎、"generator ≠ validator"独立验证层；reachability 已引入 agentic 欠近似决策并官方自认假阴性与结论漂移。
- **Sonatype**（[sonatype.md](sonatype.md)）：registry 代理位（Firewall/Nexus）× 策展队列（Fast-Track <24h / Deep Dive ≤3 天可回改）× 细粒度策略引擎三件套互相咬合；已有 method 级 reachability（修正 03 旧口径）；SBOM Manager 的版本级持续监控+VEX 跨版本复制是最有 CRA 相性的现成骨架。
- **Black Duck**（[black-duck.md](black-duck.md)）：900 万+组件 KB + snippet"高召回+人工确认闸门"+ C/C++/固件（Build Capture/BitBake/BDBA）最完整覆盖；LTS Project Version 是"已发布产品持续监控"的最接近实现；Signal 是 7-agent LLM 流水线但 SCA agent 仅覆盖 Python。

## 1. 五家 × 关键技术维度对比表

每格一句话，链接指向对应厂商文档章节（分级与一手来源见各文档）。

| 维度 | Endor Labs | JFrog | Snyk | Sonatype | Black Duck |
|---|---|---|---|---|---|
| **Reachability 引擎实现** | 自研（FASTEN/Steady 谱系），per-package-version 预计算调用图+客户端 stitch；三级降级（full call graph→pre-computed→dependency）构建失败自动 fallback（[§2](endor-labs.md#2-reachability-引擎实现)） | 无通用 call graph 引擎；Contextual Analysis = 人工策展 per-CVE scanner（1,600+），约 1/3 scanner 故意不用 reachability（配置/CLI/运行时信号）（[§2](jfrog.md#2-contextual-analysis-scanner-的工程实现)） | DeepCode 自研（ETH 血统）符号分析，2026 引入 agentic 欠近似决策；官方自认假阴性与结论漂移（[§2](snyk.md#2-reachability-实现)） | method 级 reachability（Java/JS/.NET，.NET 为 IQ 203 新增）+ Reachability Evidence（仅 Java）——03"无 function 级"口径已过时（[§0](sonatype.md#0-对-03-报告的两条重要修正)） | Detect 生成 Java 调用图→SHA-1→KB Function Signature Match，仅 Java 且限带方法名元数据的 BDSA；**非** Coverity 引擎（修正 03 口径）（[§0](black-duck.md#0-本轮要点tldr)） |
| **漏洞数据策展** | 多源聚合+自有策展层，CVE→漏洞函数映射自称程序分析自建；策展流水线细节无公开证据（[§3](endor-labs.md#3-漏洞数据库自建还是聚合策展流程)） | 研究团队对高危 CVE 披露同日人工建 scanner，客户可点单；Catalog 集中式元数据底座（[§2](jfrog.md#2-contextual-analysis-scanner-的工程实现)） | Human+AI 五角色分工（lead gen/代码分析/排序/富化/监控），HITL+RLHF+eval-driven+LLM-as-judge；内部 MCP 先行（[§1](snyk.md#1-漏洞数据库策展)） | Fast-Track（<24h 占位）/Deep Dive（≤3 天源码级、可推翻前者）两级队列+disputed 自纠；自曝 92% 公开数据需修正（[§1](sonatype.md#1-漏洞数据策展流程证据进产品方式)） | CyRC 人工策展 BDSA（含否定性确认、embargo Under Review）+ ASA/Rapid Review AI 批量扩面（验证收窄到版本区间）（[§1](black-duck.md#1-knowledgebasekb规模策展离线分发)） |
| **VEX 实现** | 仅导出动作（CycloneDX/SPDX/VEX）；机器判定不落 VEX statement（[§11](endor-labs.md#11-对我们产品的启示)） | SBOM 富化 VEX（厂商声称）；判定 justification 绑 scanner 版本而非独立证据对象，与 Evidence（DSSE/in-toto）是两条未打通的线（[§4](jfrog.md#4-apptrust-证据链模型evidence-的密码学实现)） | 无 VEX 产品；reachability 只作为 Risk Score"只加不减"的上下文因子（[§5](snyk.md#5-risk-score-组成因子)） | SBOM Manager 注释（CycloneDX analysis 块），逐条从最近前版本 Copy；"VEX 自动化规则"存在但语义未公开（[§4](sonatype.md#4-sbomvex-工作流工程细节)） | 11 态状态机+CSAF 2.0 profile 5+NOT_AFFECTED 强制 justification（2025.1.0 引入）；但属展示层状态机——无失效触发器、无状态历史、Revision 硬编码 draft/v1（[§4](black-duck.md#4-vex-状态机与-csaf-映射加深)） |
| **AI/Agent 架构** | 确定性引擎在下+薄结构化 MCP 工具面（返回 finding UUID，LLM 不判漏洞）+Agentic UI 数据域硬限制；hooks 锚入 agent 生命周期；双向战略（对外 MCP+对内 Coding Agent Governance）（[§7](endor-labs.md#7-ai--agent-架构)） | 不做 LLM 判定；把平台能力 MCP 化卖给别人的 agent（MCP Server 含 waiver 审批/Evidence 创建等治理动作；Fly=agentic repository；Agent Guard 治理 agent 资产）（[§7](jfrog.md#7-ai--agent-叙事)） | "generator ≠ validator"独立验证层叙事；Agent Fix=前沿 LLM+35k 专家修复 dynamic few-shot+SAST 重扫闸门；MCP 纯本地 12 工具三档 profile（[§3](snyk.md#3-agent-fix-架构)、[§4](snyk.md#4-evo--ai-trust-platform-与-mcp)） | 刻意不做 LLM 修复闭环：Guide（MCP 数据 grounding）+Golden PR（规则驱动、仅 Maven）+Automated Waivers；叙事把 LLM 建议定位为风险源（[§7](sonatype.md#7-ai--agent)） | Signal 七 agent 流水线（5 chat+2 embedding），oversight-agent FP 复核+实验性 synthesis/PoCKit 主动利用验证；sca-agent 仅 Python；BYOLLM 支持断网内网 LLM（[§5](black-duck.md#5-signalagentic-修复架构深拆)） |
| **对象模型** | K8s 风格资源模型（UUID+Meta+TenantMeta+Spec+Context），根=Project(git repo URL)，Context 隔离扫描代际；无 product/version（[§8](endor-labs.md#8-数据底座与对象模型)） | checksum 组件图（PostgreSQL）→**AppTrust application 一等实体**：maturity_level（含 end_of_life）+criticality+owners，application version 三态（PRE_RELEASE/RELEASED/TRUSTED_RELEASE）（[§5](jfrog.md#5-对象模型artifactpackagebuild--application-的跃迁)） | Tenant→Group→Org→**Target（repo/K8s workload/可扫资源）**→Project（manifest×扫描类型）；无版本语义，距 product/version 一整层（[§6](snyk.md#6-对象模型project--target--org离-productversion-有多远)） | Root Org→Org→Application；SBOM Manager：Application→Application Version→SBOM 双件；version evaluation window 是运维参数非支持期对象（[§5](sonatype.md#5-对象模型applicationorganization-vs-productversion)） | Project→Project Version（phase 状态机：In Planning…Released…Archived）→BOM；**LTS version**=已发布产品持续监控骨架（转换即出 SBOM、不可逆、剥开发期数据、集中式 catalog），但通知"Coming soon"（[§3](black-duck.md#3-projectversion-对象模型与-cra-粒度的距离)） |
| **交付形态** | SaaS 优先（hybrid/cloud scanning 两种），无自托管控制面；API-first（3 份 OpenAPI spec 公开）（[§1](endor-labs.md#1-产品架构与交付形态)） | SaaS+self-hosted 双形态全功能；self-hosted Enterprise X 起价 $51,000/年（[§9](jfrog.md#9-定价--部署形态fact官方定价页2026-09-02-抓取)） | SaaS-only（多租户/单租户 Private Cloud）+Broker 桥接；无 self-hosted（[§7](snyk.md#7-交付形态saas-only--broker-桥接)） | Cloud/self-hosted/SAGE 三形态；RPM/Docker/Helm，自备 MySQL+PostgreSQL（[§8](sonatype.md#8-交付形态self-hosted-传统air-gapped)） | hosted/self-hosted（K8s Helm 为主力）/air-gapped KB/BDBA 虚拟 appliance（OVA/qcow2）；Signature Scanner 支持完全离线扫描（[§9](black-duck.md#9-交付形态self-hosted-与离线能力总览)） |
| **Air-gapped** | Outpost 把扫描下沉到客户 K8s 但结果仍回传云——"air-gapped"名实有缝（[§1](endor-labs.md#1-产品架构与交付形态)） | DBSync v3 流式离线数据包成熟；但 scanner 执行体须升级 Xray 本体、Smart Remediation 需 Catalog 连通（[§3](jfrog.md#3-air-gapped-知识库分发fact)） | 无；替代回答是 Broker 数据最小化（分析完即删源码、只留 call graph）（[§7](snyk.md#7-交付形态saas-only--broker-桥接)） | SAGE 正式产品：离线数据每日打包摆渡灌库，部分客户已全自动（[§8](sonatype.md#8-交付形态self-hosted-传统air-gapped)） | 最重但最完整：月度 5TB 整库搬运、64 核/256GB/35TB 门槛；代价是功能阉割（无 fuzzy/MaaS/correlation/自动 BOM 重算）（[§1.3](black-duck.md#13-air-gapped-离线分发机制重点)） |
| **CRA 叙事** | 非核心战场（FedRAMP 为主线）；EU 租户+元数据出网是对数据主权的折中（[§1](endor-labs.md#1-产品架构与交付形态)） | 唯一有专门 CRA Compliance Brief；AppTrust 已有 pre-built CRA policy templates 一键化（厂商声称）（[§5](jfrog.md#5-对象模型artifactpackagebuild--application-的跃迁)） | 内容营销映射，无专门模块；SaaS-only 形态结构性接不住 CRA 高敏行业（制造业/OT）（[§11](snyk.md#11-对我们产品的启示)） | SAGE 页合规框架清单唯一显式挂 CRA（营销页级，非专项方案）（[§8](sonatype.md#8-交付形态self-hosted-传统air-gapped)） | "SCA alone won't get you to CRA compliance"组合套装叙事+STMicro 半导体头部案例背书；无 CRA 专门模块（[§7](black-duck.md#7-制造业嵌入式-cra-叙事)） |

## 2. 五家共同的架构收敛点（Fact 级，逐条可在上表对应章节核实）

1. **"确定性引擎在下、LLM 编排/叙述在上"的分层架构全员收敛**。Endor（"agentic AI layer above that"，MCP 只返回 finding UUID）、Snyk（"the generator cannot be the validator"，SAST 重扫闸门）、Black Duck（oversight-agent FP 复核+PoCKit 主动验证）、JFrog（判定仍是人工规则，LLM 只做平台能力 MCP 化）、Sonatype（直接把 LLM 建议定位为风险源）——没有一家让 LLM 独立产出漏洞判定。这加固了 [00 报告](../00-final-report.md) §1.2 判断 5 的架构结论。
2. **MCP 化全员完成**。Endor MCP（11 客户端）、Snyk `snyk mcp`（本地 stdio、12 工具、三档 profile）、JFrog MCP Server（覆盖 Evidence/AppTrust/Curation 治理动作）、Sonatype Guide（MCP 接入 IDE）、Black Duck `@black-duck/mcp-server`——MCP 已是安全能力接入编码 agent 的标准接口（印证 [06 报告](../06-product-forms-and-tech-stacks.md) 技术栈要点④）；JFrog/Snyk 已把**治理动作**（waiver 审批、evidence 创建）开放给 agent 调用，是 MCP 化的下一步。
3. **Reachability 保守度/局限声明成为官方文档标配**。Endor 三级降级各自带保守度假设明示（"直接依赖全可达"）、Snyk 自认假阴性与"NO PATH FOUND 可漂移为 Reachable"、JFrog 自承"刻意偏好假阳性"、Black Duck 声明"reachable ≠ 必然受影响，未标 ≠ 安全"——"降噪率"营销数字背后，厂商都在文档里给自己留了保守性免责。买方尽调应以这些自述为准而非营销页。
4. **情报策展全部转向"AI 扩面+人工终审"双层结构**。Snyk 五角色+HITL/RLHF、Black Duck ASA/Rapid Review（验证收窄到版本区间）、Sonatype Fast-Track/Deep Dive 可回改队列、JFrog 人工 per-CVE（自承无法自动化）、Endor 程序分析自建（声称）——纯人工策展已无人声称可行。
5. **存储层无一家用专门图数据库**。JFrog 组件图存 PostgreSQL、Sonatype IQ 是 Java 单体+MySQL/PostgreSQL、Black Duck 是 Tomcat+PostgreSQL+Solr——"图数据库是叙事、图数据模型才是实质"（[04 报告](../04-technology-deep-dive.md) §5.2）样本再扩大。
6. **修复后状态闭环开始出现但形态割裂**。JFrog Patched（限 Zero-Touch 场景）+Rescan Required、Sonatype auto-waiver（reachability→waiver 链路已产品化，但有失效 bug 记录）、Black Duck remediation status 跨 BOM 延续——无一家实现"修复→重扫→VEX status→fixed"自动流转（03 §6.2 发现 2 本轮维持）。

## 3. 五家共同的空白（汇总后再次确认）

03 §6.2/§6.3 的三条主空白本轮深挖后**全部维持且证据更硬**，另有一条从"薄弱"升级为"确认空白"：

1. **机器判定→VEX statement 自动化：五家均无，且看清了各自的断点位置**。Endor 有 call chain 证据但 VEX 只是导出动作；JFrog 有机器 justification 但绑 scanner 版本、且与 Evidence 密码学证据线在对象模型上未合一；Snyk 无 VEX 产品；Sonatype/Black Duck 的 VEX 状态靠人工标注（Black Duck 强制 justification 但只是枚举+自由文本）。断点不在格式层（CSAF/OpenVEX 都支持），在**判定对象化**这一层。
2. **判定失效重估：五家均无，且拿到对手自曝的最硬证据**。Black Duck KB 更新作业官方自认：score/severity 变化**静默生效无通知无审计日志**、BDSA↔CVE 标识符切换**重置 remediation status 与 comments**（[black-duck.md §10](black-duck.md#10-工程博客文档自曝的局限汇总)）；Sonatype waiver 是 zero-tolerance 失效但静默、无自动重估通知（CLM-38947 显示链路仍有 bug）；Snyk reachability 结论漂移但无 statement 失效机制。"新情报推翻旧判定"在每家内部都是断点。
3. **Product/Version/支持期一等对象：全员仍缺，但两家已到"加字段"距离**。JFrog application version 有 maturity_level=end_of_life 枚举但无支持期日期/监管义务字段；Black Duck LTS version 是持续监控骨架但无支持期语义且通知 Coming soon；Sonatype version evaluation window 是运维参数；Snyk/Endor 对象模型无版本概念。CRA 的"支持期承诺+24h/72h 报告义务"语义没有任何一家落成对象。
4. **纯二进制/固件 reachability：全行业确认空白**。Endor 官方自认"Reachability is not available for C/C++"、`.so`/`.a` 出界；Black Duck BDBA 只有组件级匹配无函数级 reachability；JFrog Contextual Analysis 不扫 third-party 代码（部分因许可限制）；Sonatype/Snyk 无二进制 reachability。C/C++ 方向只有 snippet/指纹级"成分识别"，没有"可利用性判定"——CRA 制造业主战场的最深技术缺口（加固 [00 报告](../00-final-report.md) §1.2 判断 3 的 C/C++ 押注）。
5. **（附加确认）修复可信度遥测仍全行业空白**。Snyk 的"94% 更高合并率"是全行业首个公开数字但只是相对值（无基线、无样本量、无回归率）；其余四家无任何公开数字（[snyk.md §3.3](snyk.md#33-合并率回归率)）。

## 4. 五家各自对我们最有威胁的动向（Interpretation）

1. **JFrog：application 对象模型跃迁（最高威胁）**。AppTrust 把 application 做成一等实体（ownership/criticality/maturity_level 含 `end_of_life`），application version 有 PRE_RELEASE/RELEASED/TRUSTED_RELEASE 三态+OPA gate+签名 evidence 绑定，且 CRA policy templates 已一键化（厂商声称）——距"产品线+版本+支持期"只差加字段，不是架构重写。[03 §4](../03-competitive-landscape.md) 风险①正在兑现中。其短板（判定线与证据线未合一、支持期无日期语义）正是我们的差异化落点，但这个短板是"产品 backlog"级别而非"架构"级别。（[jfrog.md §5/§11](jfrog.md#11-对我们产品的启示)）
2. **Black Duck：LTS Project Version**。已为"已发布、不再重扫、只需持续漏洞监控"的软件设计了专门对象（转换即出 SBOM、集中式 catalog 撑海量版本、单向不可逆），官方承认通知/告警"Coming soon; top priority"——补上通知+把 VEX 绑定 LTS 持续重生成，就是现成的 CRA 上市后监控产品。制造业（STMicro）渠道与 air-gapped 能力是其兑现该路线的现成底座。（[black-duck.md §3/§11](black-duck.md#3-projectversion-对象模型与-cra-粒度的距离)）
3. **Sonatype：SAGE 挂 CRA + 版本级持续监控工程化**。SAGE 是目前 Sonatype 唯一显式挂 CRA 的着陆点（营销页级）；更实质的是 SBOM Manager 的评估队列架构（producer/consumer、version evaluation window、监控所有历史版本）已是"支持期内重评估"的最小可行架构，且 "Create rules to scale and automate the VEX process" 若属实则比 03 的"VEX 纯人工"结论走得更远（规则语义未公开，待验证）。（[sonatype.md §4/§8/§11](sonatype.md#11-综合判断)）
4. **Snyk：AI-SPM 资产对象 + Evo 商业验证**。AI-SPM 的"模型/agent/skill 清单"是 Snyk 对象模型中第一个非 repo 锚点的资产对象——若它向"应用/产品版本"演化，是 Snyk 填补 product/version 空白的唯一可能路径（Hypothesis）；Evo 已获商业验证（新单额 60%，厂商声称），平台叙事一旦加 CRA 维度，品牌势能最大。（[snyk.md §6](snyk.md#6-对象模型project--target--org离-productversion-有多远)）
5. **Endor：reachability 基础设施化 + MCP 免费层 PLG**。预计算调用图存成全客户共享的 `oss` 租户 API 资源（GetCallGraphData），MCP/CLI/IDE 免费层（2026-03 起）把 reachability 证据变成开发者随手可得的公共品——威胁的不是某个功能，而是我们"证据化 reachability"差异化叙事的时间价值：它商品化得越快，我们的窗口越短。（[endor-labs.md §2/§9](endor-labs.md#2-reachability-引擎实现)）

## 5. 时间线判断更新：12–18 个月窗口是否需要调整？

**结论（Interpretation）：维持 12–18 个月不变，但压力明显偏向下限（12 个月侧）；窗口关闭的触发器从"是否发生"变为"何时发生"，建议设立两个可监控的领先指标。**

收窄压力上升的证据（本轮新增，均为 Fact 级）：

- **JFrog 风险①已在兑现**：03 §4 风险提示"若其把对象模型升级为产品线+版本+支持期则空白快速收窄"——AppTrust 的 application 一等实体+maturity_level 枚举+version 三态+CRA templates 说明该升级**已经开始**，完成度约一半（缺支持期日期与监管报告对象）。
- **Black Duck 的 LTS 比 03 评估的更接近 CRA 语义**：03 时只知道 Project+Version 模型；本轮确认 LTS 就是"投放市场的产品版本持续监控"的工程实现，且官方把通知列为 top priority——距离从"缺一层语义"缩到"缺一个产品化包装"。
- **Sonatype/Snyk/Endor 三家对空白无实质动作**：Sonatype 的窗口是运维参数、Snyk 距 product/version 仍隔一整层、Endor 明确 git-centric 无 release 语义——空白的中段（现代开发者工作流×产品版本对象）暂无第三家入场。

反向（支持窗口不进一步收窄）的证据：

- 四条共同空白（§3）**没有一家有任何 roadmap 信号**；JFrog 的判定线与证据线未合一是对象模型级问题；Black Duck LTS 转换会**丢弃 triage 信息与 comments**（方向与"判定延续"相反）；Black Duck KB 更新作业连"preserving remediation status across identifier transitions"都还在 roadmap 上——离"新情报触发判定失效重估"都很远。
- CRA 执法实践未定型、证据粒度监管期望不确定（03 §4 风险②）这一根本不确定性本轮无任何变化。

**领先指标建议**（出现任一即应重估窗口为 ≤12 个月）：① JFrog AppTrust application version 增加支持期/EOL 日期字段或 CRA 报告义务对象；② Black Duck LTS 通知/告警 GA 或 VEX 绑定 LTS version 自动重生成。

## 6. 文档索引

| 文档 | 内容 |
|---|---|
| [endor-labs.md](endor-labs.md) | Endor Labs 深挖（引擎/预计算图/三级降级/C++ 路线/MCP 双向战略） |
| [jfrog.md](jfrog.md) | JFrog 深挖（checksum 组件图/Contextual Analysis 规则库/Evidence DSSE/AppTrust 对象跃迁/ZTR） |
| [snyk.md](snyk.md) | Snyk 深挖（策展五角色/DeepCode+agentic 混合/Agent Fix 验证层/Risk Score 因子/对象模型字段级确认） |
| [sonatype.md](sonatype.md) | Sonatype 深挖（reachability 口径修正/两级策展队列/策略引擎/SBOM Manager 持续监控/SAGE） |
| [black-duck.md](black-duck.md) | Black Duck 深挖（KB 与 air-gapped/snippet 机制/LTS version/VEX 状态机/Signal 七 agent） |
| [research-log-endor.md](research-log-endor.md) / [research-log-jfrog.md](research-log-jfrog.md) / [research-log-snyk.md](research-log-snyk.md) / [research-log-sonatype.md](research-log-sonatype.md) / [research-log-blackduck.md](research-log-blackduck.md) | 各厂商调研过程记录 |
| [sources/](sources/) | 全部 source notes（一手来源摘录与 URL） |

> 对 03 报告的口径修正汇总见 [03 §6.5](../03-competitive-landscape.md#65-第二轮深挖修正索引2026-09-21)；对 00 报告的影响见 [00 §9.6](../00-final-report.md#96-第二轮厂商技术深挖摘要2026-09-21)。
