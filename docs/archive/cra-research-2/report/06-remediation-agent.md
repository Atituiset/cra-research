# 06 · 修复自动化 / AI Agent 架构 / Evidence Graph

> 对应 mvp.md §十八 #11/#12/#13。三件事：① 修复自动化的现状与"上游修复≠我修了"链条；② Agent 九个架构问题的产品化回答（基于已验证的行业范式）；③ Evidence Graph 的数据模型——本报告论证的核心壁垒。
> 来源：R6（GUAC/MCP/Prophet/OpenRewrite/Dependabot/学术 agent）、R5（Snyk/GitLab/Endor）、R2（CycloneDX citations）、EUR-Lex（10 年记录义务）。

## 1. 修复链条：Mitigation vs Remediation vs Fix（概念先行）

| 概念 | 定义 | 例子 | CRA 语境 |
|---|---|---|---|
| **Fix（上游修复）** | 开发者改代码消除了缺陷 | log4j 2.16 去掉 JndiLookup | 我只是"消费了消息" |
| **Remediation（我的处置）** | 我的**产品**消除了漏洞 | 升级到 2.16 / backport 补丁 / 移除依赖 / 加配置拦截 | Annex I Pt II(2)(4) 的义务对象 |
| **Mitigation（缓解）** | 未 fix 但降低可利用性（隔离、WAF、关闭特性） | 网络分段、禁用 jndi | 可作为 VEX=affected 的处置记录+报告缓解措施 |
| **Verification（验证）** | 证明 remediation 生效 | 复扫+复测+证据 | "已修复"声明的举证基础 |
- **关键断链（01 §13 心智模型的一环）**：*上游 fixed ≠ 我依赖的包 fixed（backport 窗口）≠ 我产品里 fixed（版本矩阵/构建）≠ fixed 被验证（复扫+运行证据）*——传统 SCA 把"Dependabot 显示 fixed"当终点，**本产品把 verification 当终点**。
- 修复建议必须是**四选一菜单**（升级/backport/缓解/暂不可修→VEX+SLA），对应 04 J4；"暂不可修"是一等出口（硬件发版周期现实，03 §3.1 痛点 3）。

## 2. AI 修复现状：产品级证据（学术"autonomous repair"检索为 0，见 R6#6）

| 厂商/平台 | 已验证能力（来源） | 范式 |
|---|---|---|
| **GitHub Dependabot** | 告警可**指派给 AI agent**（Copilot 内置 + Codex/Claude 第三方），agent 自动开会话、**开草稿 PR**；修不了保持 assignee 并留会话日志；auto-triage 自动关低风险；assignees_changed webhook [R6#5 官方文档] | **草稿 PR + 人工审阅 + 会话日志** = 平台级安全范式 |
| **GitLab** | SBOM 依赖扫描 + Continuous Scanning + **Duo 自动解决依赖升级 breaking change** + libbehave + agentic breaking-change 分析 [R5#3] | agent 解决"升级不敢升"的阻塞 |
| **Snyk** | Risk Score（reachability+EPSS+exploit maturity）+ **Snyk Evo**（AI agent 治理）[R5#2，部分营销] | agent 治理层 |
| **Semgrep** | Autofix + **Agentic Workflows** [R4#3] | 确定性 autofix + agent 编排并存 |
| **Endor Labs** | agentic remediation + **Endor Patches**（预构建补丁）[R5#1，营销] | 修复包预生成 |
| **OpenRewrite** | LST（无损语法树）重构 + 安全 fix recipes + Moderne 多仓 mass-commit [R6#4] | **确定性 recipe**（非生成式）——对 backport/版本迁移尤其重要 |
| **学术侧** | arXiv 检索：VulnBot/xOffense/Red-MIRROR 均为**渗透测试 agent**（攻侧基准竞赛），"autonomous vulnerability repair" 0 结果 [R6#6] | 修复侧证据以产品发布为主，成熟度判断**依赖厂商口径，需标注** |

**结论**：① Agentic remediation **已 GA、不再是概念验证**；② 行业收敛到同一安全范式：**草稿/预构建 → 人工审阅 → 可回放的会话日志**；③ 因此"有没有 agent"不是差异化，**"agent 的结论/改动挂不挂证据、能不能进 VEX/报告闭环"才是**（引出 §3/§4）。

## 3. Agent 架构：九个问题的参考答案（mvp.md §八 十类问题的收敛）

> 原则：**Agent 是编排层，不是判定权威**（05 §3.4 的人机分工延伸）。每条建议后标 [决策]（MVP 采纳）/ [权衡]（待 PoC）。

1. **自治程度**：分级 A0 建议只读 → A1 起草（PR/报告草稿）→ A2 条件执行（低风险类自动，高风险需批）→ A3 全自动。**[决策] MVP 只做 A1+A2 白名单**（A2 仅限"明确 fix version 存在+CI 绿+无 breaking change 信号"的升级）；参照 Prophet scoped actions（自主或需用户批准 [R6#3]）与 Dependabot 草稿范式 [R6#5]。
2. **工具边界**：只读代码/SBOM/情报 = 自由调用；写操作（PR、状态迁移、报告提交）= 白名单+审批钩子。**[决策]** 工具清单：read repo、run scan、propose fix、open draft PR、propose VEX change、draft report；**永不直接** merge、publish VEX、submit to SRP。
3. **上下文组装**：判定上下文 = 产品/版本快照 + 漏洞多源情报 + reachability 证据 + 历史判定 + 修复尝试史。**[决策]** 每次会话以**证据快照 ID** 为锚（不是实时查询），保证可回放。
4. **验证回路**：agent 声称"修好了"必须过 CI 复扫+复核 L2 结果（04 J4）。**[决策]** verification 是状态机强制迁移条件，不可跳过。
5. **人类审批点**：VEX 状态变更（尤其 not_affected/affected）、事件报告提交、A2 自动升级的合并。**[决策]** 与 04 J2/J3 UI 一致。
6. **失败与降级**：agent 超时/低置信 → 回 `under_investigation` + SLA 升级（05 §5 表）。**[决策]** 无静默失败；失败本身进证据图。
7. **多 agent 协作**：分类器/定位/修复起草/验证 四角色可拆（学术 multi-agent 渗透框架同构 [R6#6]）。**[权衡]** MVP 单 agent 流水线足够，架构留 role 接口。
8. **观测性**：会话日志、工具调用、token 成本、成功率。**[决策]** 依赖 MCP 式标准化工具接口（R6#2：MCP 是 AI 应用与外部系统的事实标准——**我们的 agent 工具层直接按 MCP server 暴露，未来客户可把自己的工具接进来**，生态杠杆）。
9. **安全**：提示注入（仓库内恶意 README）、权限最小化、密钥不入上下文。**[决策]** 代码内容按不可信数据处理（分隔/过滤）、A2 权限与仓库权限解耦、审计全量。

## 4. Evidence Graph（核心壁垒章）

### 4.1 为什么需要图：CRA 的"记录 10 年"与"随时可提交"是图查询问题
- EUR-Lex 要求：事件处理**记录至少 10 年**、技术文档（Annex II）随监管问询可提交、每次判定的**尽职过程可举证** [EUR-Lex Annex I Pt II(6), Annex II]。
- 若证据散落在扫描日志/工单/邮件里，10 年后=考古。**结构化做法：所有判定与动作作为带版本的图节点，按产品实体收敛。**
- 开源锚点 **GUAC**（OpenSSF 孵化，Google/Kusari/Red Hat/Purdue/Citi）验证了"SBOM/工件元数据 → 图 → 可行动洞察"的可行性 [R6#1]——但 GUAC 面向**软件供应链资产图**，**没有人把它做成"CRA 判定证据图"**：我们的差异 = 图的边是**合规判定链**（谁、何时、基于哪些证据、得出什么状态、触发了什么动作），且按产品×版本组织。

### 4.2 图模型（MVP 可落地的最小 schema）
```
实体（按产品级模型，03 §5）：
  Product → Release(version, support_period) → Deployment(客户/批次, 可选)
  Component(PURL, 版本)  ←— contains —← Release
  Vulnerability(CVE/OSV/GHSA 别名归一)
  Advisory(情报源+版本区间+发布时间)   ReachabilityRun(分析器版本, 结果, call path)
  ExploitSignal(KEV/EPSS快照/厂商标注)
  Judgment(VEX 状态+justification+判定人+时间)
  Remediation(升级/backport/缓解, PR/commit)
  Verification(复扫结果+runtime 快照)
  Incident(Art.14 时间线事件)
  Report(24h/72h/final, 提交状态)
  SBOMSnapshot(hash, 格式, 生成时间)
  AgentSession(工具调用轨迹, prompt 版本, 产出物)

边（判定链——图的灵魂）：
  SBOMSnapshot --captured_from--> Release
  ReachabilityRun --analyzes--> Component@Release  --for--> Vulnerability
  ReachabilityRun --evidence_of--> Judgment
  ExploitSignal --evidence_of--> Judgment / --triggers--> Incident
  Judgment --resolved_by--> Remediation --verified_by--> Verification
  Verification --supports--> Judgment(fixed)  --exports_as--> VEX/CSAF 导出物
  Incident --attaches--> SBOMSnapshot(冻结)  --produces--> Report
  AgentSession --proposes--> Judgment/Remediation/Report  --requires_approval--> Human(actor)
  所有节点: timestamp + actor + input_snapshot_refs（可回放）
```
- **CycloneDX 的 `citations`（证据溯源字段）与 `declarations`（合规即代码）** 是导出侧的近亲 [R2#3]——图是内部真源，CycloneDX/SPDX 是序列化出口（01 §5.2 立场一致）。

### 4.3 三个杀手级查询（把图卖成能力）
1. **监管应答（Annex II）**："给产品 P 在日期 D 的完整证据链" → 冻结快照→导出技术文档附录（04 J5 升级版）。
2. **时间旅行复盘**："当时为什么判定 not_affected？" → Judgment 节点回放当时的 reachability run + 情报版本（回答审计/事故归因）。
3. **报告完备度**："Art.14 三份报告各自还缺哪些字段/证据" → Incident→Report 缺口查询（04 J3 的倒计时看板数据源）。

### 4.4 与事件报告、VEX 的闭环（一张图收束全报告）
```
情报到达 → [Associate] 归一关联 → [Assess] reachability/exploitability 证据
 → Judgment(VEX) ←——人审——→ [Act] Remediation → Verification → Judgment(fixed)
        │ KEV/严重信号
        ▼
   Incident 状态机(24h/72h/14d) → Report 草稿预填 → 提交标记
        │
        ▼
   Evidence Graph 全程冻结快照 ──导出──> SBOM/VEX/CSAF/Annex II/客户应答包
                                        （10 年留存，EUR-Lex Annex I Pt II(6)）
```
- **一句话给董事会**：扫描器卖"发现"，我们卖"**可采信的结论**"——发现会同质化，证据随客户合规历史增值。

## 5. 本章 → 08 章的接口
- PoC-3（VEX 工作流）直接以 §4.2 schema 的子集（Judgment+ReachabilityRun+SBOMSnapshot+导出）实现。
- PoC-1（多源归一）产出 Advisory/Vulnerability 别名与区间节点，是图的左侧入口。
- Agent 运行时（§3）在 Phase 1 才进 MVP，但 **schema Day 1 就按图设计**（避免 alert 表二次迁移，03 §5 教训）。

---
*Dependabot agent assignment、GitLab Duo、OpenRewrite recipes、GUAC、MCP、Prophet 均为本轮官方源/厂商页核实 [R6, R5]；Endor Patches/Snyk Evo 营销标记不变。*
