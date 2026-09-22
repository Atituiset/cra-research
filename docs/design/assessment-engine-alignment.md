# 对照聊天记录：从 CRA 工作台回到漏洞评估引擎

依据：[架构讨论记录](../chat-history.md)，重点为 §4、§10–17、§19–26。对照：[当前原型设计](unified-workbench.md)、[共享核心](../../src/cra/core.py)、[原始 PoC](../../poc/README.md)。

本文是方向与差距评估，以及下一步设计建议；不代表 VA-IR、Claim Engine 或 Agent 已经实现，也不改变历史证据。

## 1. 最重要的修正

聊天记录的中心是 **Vulnerability Assessment Engine**：对特定产品、发布物、组件、漏洞和上下文持续开展评估。CRA 是业务入口及消费方之一；VEX、CSAF、CI Gate 等复用同一评估结果。

之前的合并实现主要验证了“证据导入 → 判定候选 → 人签 → 历史 → 报告/导出”。这部分有价值，但只是证据存储与消费端原型，还没有验证“漏洞如何定位到代码、证据缺口如何驱动下一步分析、如何形成有条件的 Claim”。

因此，演示欠缺的不仅是美术表现，而是缺少了最关键的计算过程。换几种图形无法补上这一点。

## 2. 对照已有资产

| 讨论中的要求 | 当前资产及差距 | 建议 |
|---|---|---|
| SCA 是分析目标发现入口 | PoC 有 SBOM/OSV 关联；新核心从已签名包导入，未形成独立 AssessmentTarget | 保留工具，归一为产品×发布物×组件实例×漏洞×上下文的目标 |
| Localization 是一级能力 | [C 策展映射](../../poc/curation/vuln-function-map.json) 已有 CVE、函数、文件、修复提交；[reach_c.py](../../poc/pipeline/reach_c.py) 直接消费它 | 提取 LocalizationResult，记录来源、基线、候选符号、定位粒度和未解决项 |
| CodeGraph 提供代码事实 | Joern CPG/BFS 与 Go call trace 已跑通理想样例 | 归入 ProgramFactProvider；明确源码/构建、入口与图覆盖范围 |
| Evidence → Claim → Decision | `import_pack()` 将旧 VEX 状态转成 Judgment，没有独立的 Presence/Localization/Reachability Claim | 保留旧记录，新增结构化 Claim；不能给 Judgment 改名就称其为 VA-IR |
| VA-IR 统一分析状态 | 当前 `cra-workbench/v1` 是工作台快照，存的是原始 predicate 与业务对象 | 新建 assessment schema，与导出快照分开 |
| Agent 是动态 Pass Manager | 当前无 Planner、Pass 契约或证据缺口调度 | 优先实现可记录、可回放的调度协议；模型只提下一步建议，不直接签发结论 |
| 连续重估 | `reassess()` 追加调查中修订，未执行分析，也没有依赖传播 | 增加证据/Claim 依赖，依据变更精确标 stale，再调度受影响 Pass |
| CRA/VEX 是消费者 | 当前 Store 同时负责状态、事件期限、报送记录和 HTML 导出 | 渐进分离 assessment core 与 consumers；保留现有工作台作为消费者 |

已有图中的签名、证据记录数量证明了记录与校验链路；不能据此宣称已经具备语义完整的 Evidence Graph 或动态分析引擎。

## 3. 应统一成什么架构

```text
事实提供方
  SCA / advisory / static frontend / runtime / config / build-test
                           │
                    原始输出 + Provenance
                           ▼
评估核心
  AssessmentTarget + Evidence + Claim + 依赖关系（VA-IR）
                           ▲
                           │ 读取当前状态 / 写入新证据
  Evidence Gap → Planner → 有边界的 Pass 执行 → Claim 更新
       ▲                                              │
       └──────── 未完成、存在冲突或需要更多证据 ────────┘
                           │
                 Decision Policy + Review
                           ▼
消费端
  VEX adapter / CRA workflow / CSAF / CI Gate / 人类报告
                           │
                修复动作 → 验证 → 新证据
                           └──→ 依赖失效与重新评估
```

CodeGraph 位于静态前端的程序表示中。Component Graph、程序事实、运行事实与判定事实通过有类型的引用连接；无需为了“Graph”引入独立图数据库。

VA-IR 是可序列化的评估契约，Evidence Graph 是事实、Claim 和决策之间的关系及依赖语义。两者共用对象身份与修订号，不能维护两份独立真源。

## 4. 聊天记录仍需收紧的抽象

### 状态拆成不同维度

聊天记录 §14 并列列出了 AFFECTED、UNKNOWN、HUMAN_REVIEW。这表达了保留不确定性的正确意图，但不宜实现为一个枚举。

| 维度 | 例子 |
|---|---|
| 分析结论 | reachable / no_path_found / unknown；每种 Claim 定义自己的值域 |
| 证据充分性 | supported / insufficient / conflicting |
| 有效性 | current / stale / superseded |
| 审批流程 | proposed / approved / rejected / needs_review |
| 对外影响状态 | affected / not_affected / fixed / under_investigation，经消费适配器映射 |

一个 Claim 可以同时是“有可达证据、未批准、后来因构建变化而过期”。把它们压成单一 status 会丢信息。

### 工具证据也有边界

确定性工具可以重复产生某个结果，不代表结果一定完整或适用于当前制品。来源必须附带 source/build/artifact、配置、入口、工具与规则版本，以及未解析反射/间接调用等限制。

“没有路径”首先是某次分析的观察。只有分析边界足以支撑时，策略才可以得出范围明确的不受影响结论。

### Agent 的协议提前，模型能力逐步接入

应修正之前把 Agent 整体后置的说法：**证据缺口与动态调度是核心架构边界，第一版就要验证。** 但可先用确定性 Planner 建立可回放基线，再让 LLM 在相同协议下提出 Pass 选择和理由。

Pass 至少声明 requires、produces、支持范围、预算、失败结果与副作用。执行器校验权限和前置条件；达到预算、反复无新证据或工具不支持时停止，形成 unknown/needs_review。规则调度试验不能标成“Agent 已验证”。

### “Security Analysis Compiler” 是组织方式

Frontend / IR / Pass / Backend 很适合解释边界，但漏洞评估还存在不完整事实、冲突、外部时间变化与人为责任，不能假设一趟编译必然产出确定结论。评估过程应当允许部分结果和持续失效重算。

## 5. 下一轮最小切片

**目标：证明一次证据驱动评估，而非继续扩展报告页面。**

建议沿用 C 样例做 Localization 桥接试验：现有策展表显式连接 CVE-2022-37434、zlib、源码文件与 inflate；Go 样例用于适配器对照。策展是人工证据来源，不能包装成自动定位能力。

| 步骤 | 输入与产出 | 演示必须展示 |
|---|---|---|
| 1 发现目标 | 组件/版本与漏洞关联 → AssessmentTarget | 关联来源、版本范围、制品与源码绑定 |
| 2 发现缺口 | 当前无 Localization Claim | Planner 为什么选择定位 Pass |
| 3 定位 | 策展映射 + 实际源码基线 → LocalizationResult | 文件/符号/修复引用及匹配是否唯一；歧义则保留 unknown |
| 4 求路径 | 确定的符号 + 图快照 + 入口集 → ReachabilityEvidence | main → gunzip_file → inflate，注明仅结构可达 |
| 5 形成 Claim | 证据 + 限制 → ReachabilityClaim | supporting evidence、counter-evidence、unknowns、policy |
| 6 决策与消费 | Claim + policy + review → Decision → VEX 草稿 | 为什么这样判断；Exploitability 无证据时仍为 unknown |
| 7 变更回放 | 更换输入快照或规则 → 依赖失效 | 哪些 Claim 变 stale、哪些 Pass 重跑、历史为何仍可查 |

验收重点：不预填最终状态；缺少映射会停在定位缺口；缺少路径不自动判安全；输入变更使依赖 Claim 失效；换 VEX/CI 消费方不需要重写分析核心；每一步都能说明“为什么选这个 Pass”。

第一版数据契约可以从四个对象起步：

- `AssessmentTarget`：product/release/artifact/component/vulnerability/context 的版本化身份。
- `Evidence`：raw/normalized result、输入快照、工具与策略来源、范围限制。
- `Claim`：typed assertion、支持/反对证据、unknowns、适用范围、依赖、有效性。
- `Decision`：消费哪些 Claim 修订、采用什么策略、结果/理由/审批；外部格式另行投影。

不要要求每项证据都必须有精确 confidence 数字。若无校准依据，用明确的证据限制和充分性状态更可解释。

## 6. 文档和 notebook 应如何调整

首页先讲通用评估引擎，随后说明 CRA 是首个业务场景。研究报告继续作为行业与法规依据；当前工作台如实保留为现有实现状态。

演示应突出五种关系：

1. **系统层次**：事实提供方、评估核心、消费者；Agent 画在控制侧。
2. **跨域桥接**：组件/版本/CVE 如何通过 Localization 连到具体 Symbol/CodeRegion。
3. **证据推导**：Evidence 支持或反驳什么 Claim，哪些 unknown 尚未解决。
4. **动态执行**：每轮 evidence gap、被选 Pass、新证据与停止原因。
5. **变更影响**：某输入变了，哪些 Claim/Decision 失效，如何重算和重新投影。

当前 notebook 能支撑真实调用与历史记录的回放，却不能真实演示尚未实现的动态调度。后续图必须标注“设计示意”或“实际执行”，避免又用漂亮的流程图遮住工程缺口。

本次结论：复用已有工具与证据基础，将下一轮重点前移到 **Localization → Claim/VA-IR → 证据缺口调度 → Decision/Adapter**。CRA 事件与应答包继续作为消费端保留。
