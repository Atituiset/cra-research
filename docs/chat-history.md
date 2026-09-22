可以。去掉所有公司、人物和具体组织背景后，这个会话实际上逐步收敛出了一套比较完整的 **“面向 CRA 的漏洞全生命周期智能分析架构”**。下面按“问题 → 核心判断 → 架构 → 数据流 → Agent → IR → 落地路线”整体整理。

# 面向 CRA 的 Vulnerability Assessment Engine 架构总结

## 1. 最初的问题

起点是 CRA 场景下的软件漏洞全生命周期：

```text
发现
  ↓
评估
  ↓
决策
  ↓
修复
  ↓
验证 / 记录
  ↓
持续监控
  └────────→ 重新评估
```

具体包括：

```text
发现                    评估
────────────────       ─────────────────────
SBOM                    Reachability
资产盘点                 Exploitability
SCA                     Threat Intelligence
漏洞匹配

决策                    修复
────────────────       ─────────────────────
优先级排序               Remediation
风险接受 / 例外           Dependency Upgrade
策略选择                 Patch / Code Fix
                        Build / Test

验证 / 记录
─────────────────────────────
Re-scan
Verification
VEX 更新
SBOM 更新
审计记录
Issue / Ticket Closure

        ↑
        │
持续监控 CVE / KEV / Advisory / Product Change
        │
        └───────────────重新进入 Assessment
```

讨论过程中逐渐发现：

> **真正值得构建的并不是一个 CRA 工具，而是一套通用 Vulnerability Assessment Engine。**

CRA 是重要业务入口和 Consumer，而不是架构中心。

---

# 2. 最终核心判断

整个架构最终收敛为一句话：

> **以 SCA 为漏洞入口，以静态/动态分析、CodeGraph、Runtime 和 Threat Intelligence 为事实证据源，以 Vulnerability Assessment IR + Evidence Graph 为统一中间表示，以 Agent/Pass Manager 进行证据驱动的动态编排，完成 Localization、Reachability、Exploitability、Decision、Remediation 和 Verification，再由 VEX、CRA、CSAF、CI/CD 和其他 Assurance/Compliance 系统消费。**

因此整体分成三层。

```text
┌──────────────────────────────────────────┐
│              Consumer Layer              │
│                                          │
│ CRA │ VEX │ CSAF │ CI │ Certification   │
└────────────────────┬─────────────────────┘
                     │
                     ▲
┌────────────────────┴─────────────────────┐
│            Assessment Layer              │
│                                          │
│ Localization → Reachability              │
│              → Exploitability            │
│              → Decision                  │
│              → Remediation               │
│              → Verification              │
│                                          │
│        Agent / Dynamic Pass Manager      │
└────────────────────┬─────────────────────┘
                     │
                     ▲
┌────────────────────┴─────────────────────┐
│                Fact Layer                │
│                                          │
│ SCA │ Static Analysis │ Dynamic/Runtime  │
│ Binary │ Threat Intelligence             │
└──────────────────────────────────────────┘
```

三层分别回答：

**事实层：**

> 事实是什么？

**判定层：**

> 这个漏洞对这个 Product / Version 究竟意味着什么？

**消费层：**

> 这个安全结论拿来做什么？

---

# 3. SCA 的角色：漏洞分析入口

SCA 不应该只是：

```text
package + version
       ↓
      CVE
```

在整个系统里，它承担的是 **Assessment Target Discovery**。

主链是：

```text
Product
   ↓
Release
   ↓
Artifact
   ↓
SCA
   ↓
SBOM
   ↓
Component
   ↓
Version
   ↓
Dependency Graph
   ↓
Vulnerability Intelligence
   ↓
CVE / Advisory
   ↓
Vulnerability Association
```

得到：

```text
Product A
   │
 contains
   ↓
Component X@1.2.3
   │
affected_by
   ↓
CVE-XXXX
```

所以：

> **SCA 告诉后面的系统“应该分析谁”。**

---

# 4. 最关键的桥梁：Vulnerability Localization

这是整个架构讨论中逐渐明确出来的核心能力之一。

CVE 本身不能直接交给 CallGraph：

```text
CVE-XXXX
    ↓
CallGraph
```

中间缺了一大段语义映射。

正确过程应该是：

```text
CVE
 ↓
Affected Component
 ↓
Affected Version
 ↓
Affected Source
 ↓
File
 ↓
Symbol
 ↓
Function
 ↓
Vulnerable Code Region
 ↓
Fix Commit / Patch
```

即：

> **Vulnerability Localization**

它真正把两个世界连接起来：

```text
      SCA / Supply Chain World

Component
    ↓
Version
    ↓
CVE
    ↓

──── Vulnerability Localization ────

    ↓
Symbol
    ↓
Function
    ↓
Code Region

       Static Analysis World
```

因此 Localization 不是附属功能，而应该成为一级原子能力。

---

# 5. CodeGraph 到底是什么

讨论过程中进一步修正了一个重要抽象：

**CodeGraph 不应该和 SAST/Static Analysis 并列成一级数据源。**

更准确的是：

```text
Source Code
    ↓
Static Analysis Frontend
    ↓
AST / Symbol / Type
    ↓
CodeGraph
    │
    ├── Symbol Graph
    ├── Reference Graph
    ├── Call Graph
    ├── CFG
    ├── DFG
    └── Taint Flow
```

传统 SAST 可以理解为：

```text
Source
 ↓
Static Analysis
 ↓
CodeGraph / Program Representation
 ↓
Security Analysis Pass
 ↓
Finding
```

因此：

> **CodeGraph 是静态程序分析产生的程序事实表示；SAST Finding、Reachability、DataFlow/Taint 等能力是在这些程序事实之上的 Analysis。**

这和编译器非常类似：

```text
Source
 ↓
Frontend
 ↓
IR
 ↓
Analysis Pass
 ↓
Result
```

---

# 6. Component Graph 和 CodeGraph 必须连接

SCA 世界有一张图：

```text
Product
 ↓
Component A
 ↓
Component B
 ↓
Component C
 ↓
CVE
```

静态分析世界有另一张图：

```text
EntryPoint
 ↓
Function A
 ↓
Function B
 ↓
Function C
 ↓
VulnerableFunction
```

真正有价值的是建立 Bridge：

```text
Product
   ↓
Component
   ↓
CVE
   ↓
Affected Symbol
   │
   │ Bridge
   ▼
Symbol
   ↓
Function
   ↓
CallGraph
```

最终形成：

```text
Product
   │
 contains
   ▼
Component
   │
 affected_by
   ▼
CVE
   │
 affects
   ▼
VulnerableFunction
   ▲
 called_by
   │
Function B
   ▲
 called_by
   │
Function A
   ▲
 reachable_from
   │
EntryPoint
```

于是 Supply Chain Graph 和 CodeGraph 开始融合。

---

# 7. 最终需要的是 Vulnerability Evidence Graph

继续往前推，真正的平台核心 Graph 不应该只是 CodeGraph。

而应该覆盖：

```text
Product
  │
  ├── contains ───────→ Component
  │                       │
  │                  affected_by
  │                       ↓
  │                      CVE
  │                       │
  │                    affects
  │                       ↓
  │                VulnerableSymbol
  │                       ↑
  │                    calls
  │                       │
  └── EntryPoint → A → B → C
                       │
                    dataflow
                       │
                       ↓
                 ExternalInput

CVE ── fixed_by ───────→ Patch

Patch ── applied_to ───→ Product Version

Product ── verified_by ─→ Test / Scan Evidence
```

也就是：

> **Vulnerability Evidence Graph**

CodeGraph 是其中的代码事实子图。

Component Graph 是供应链子图。

Runtime、Threat Intelligence、Remediation、Verification 都可以继续进入 Evidence Graph。

---

# 8. Reachability 和 Exploitability 必须严格区分

这也是讨论中的一个重要结论。

## Structural Reachability

最简单：

```text
EntryPoint
 ↓
A
 ↓
B
 ↓
VulnerableFunction
```

它证明：

> 存在结构上的调用路径。

但：

```text
Reachable ≠ Exploitable
```

Exploitability 至少还可能涉及：

```text
Reachability
     +
Input Controllability
     +
Data Flow
     +
Vulnerable Branch
     +
Runtime Preconditions
     +
Configuration
     +
Permissions
     +
Mitigation
     +
Threat Intelligence
```

形成：

```text
Present?
   ↓
Affected?
   ↓
Reachable?
   ↓
Attacker Controlled?
   ↓
Vulnerable Branch Reachable?
   ↓
Preconditions Satisfied?
   ↓
Mitigation Effective?
   ↓
Exploitable?
```

所以第一阶段即使只完成：

> **Structural Reachability**

也是一个合理 PoC。

不要过早把 CallGraph Path 宣称成 Exploitability。

---

# 9. 原子能力不能按照扫描器划分

不建议：

```text
SCA Agent
SAST Agent
DAST Agent
```

因为这是按照工具分类，而不是按照问题分类。

更合理的原子能力是：

```text
1. Component Resolution

2. Vulnerability Association

3. Vulnerability Localization

4. Reachability Analysis

5. Exploitability Analysis

6. Remediation

7. Verification
```

每个能力内部可以调用不同 Tool。

例如：

```text
ExploitabilityAnalysis
       │
       ├── SCA
       ├── CodeGraph
       ├── CFG
       ├── DFG
       ├── Taint
       ├── Runtime
       ├── DAST
       ├── Config Analyzer
       └── Threat Intelligence
```

因此：

> **Tool 是能力实现手段，而不是系统能力边界。**

---

# 10. Agent 到底在哪里

这是讨论中进一步澄清的另一个关键问题。

Agent 不应该和 SCA/SAST/DAST 并列：

```text
SCA
SAST
DAST
Agent
```

Agent 应该位于 **Assessment Control Plane**。

```text
                 Agent
          Assessment Control Plane
                    │
                    ▼
              Current VA-IR
                    │
                    ▼
              Evidence Graph
                    │
                    ▼
             Evidence Gap?
                    │
      ┌─────────────┼─────────────┐
      ▼             ▼             ▼
 Localization   Reachability   DataFlow
      │             │             │
      ▼             ▼             ▼
   Tools          Tools          Tools
      │             │             │
      └─────────────┼─────────────┘
                    ▼
              New Evidence
                    │
                    ▼
               Update Claim
                    │
                    ▼
             Evidence Enough?
              │           │
             NO          YES
              │           │
              └──Agent    ▼
                       Decision
```

Agent 的职责可以概括为：

> **Planner + Evidence Gap Resolver + Dynamic Pass Manager + Reasoner**

它不应该主要负责：

> “读代码然后觉得这里存在漏洞。”

而应该：

```text
Current Evidence
       ↓
缺什么？
       ↓
选择 Analysis Pass / Tool
       ↓
获取新 Evidence
       ↓
更新 Assessment
       ↓
判断是否还缺 Evidence
```

---

# 11. Agent 和确定性工具的边界

这一条是架构不变量。

确定性工具负责：

```text
Component Detection
Symbol Resolution
CallGraph
CFG
DataFlow
Taint
Binary Analysis
Runtime Observation
Build/Test
```

它们产生：

> **Facts / Evidence**

Agent 负责：

```text
证据编排
证据关联
证据缺口发现
冲突处理
工具选择
推理
解释
```

所以：

```text
Analyzer
   ↓
Evidence
   ↓
Agent
   ↓
Claim
```

而不是：

```text
Source Code
   ↓
LLM
   ↓
"我认为不受影响"
```

---

# 12. VA-IR：统一 Vulnerability Assessment 中间表示

整个系统需要一个类似 Compiler IR 的中间层。

暂时可以称为：

> **VA-IR — Vulnerability Assessment Intermediate Representation**

核心结构：

```text
VulnerabilityAssessment

Subject
 ├── Product
 ├── Version
 ├── Artifact
 └── Component

Vulnerability
 ├── CVE
 ├── CWE
 └── AffectedRange

Presence
 ├── Status
 └── Evidence

Localization
 ├── File
 ├── Symbol
 ├── Function
 ├── CodeRegion
 └── FixCommit

Reachability
 ├── Status
 ├── Paths
 └── Evidence

Exploitability
 ├── Status
 ├── Preconditions
 ├── DataFlow
 └── Evidence

Remediation
 ├── FixVersion
 ├── FixCommit
 ├── Patch
 └── Status

Verification
 ├── Status
 └── Evidence

Decision
 ├── Status
 ├── Reason
 └── Confidence

Provenance
 ├── Tool
 ├── ToolVersion
 ├── Rule
 ├── Agent
 └── Timestamp
```

---

# 13. Claim 可能是比 VA-IR 更基础的核心抽象

讨论后进一步认为，每个判断不能只是：

```text
reachable = false
```

而应该是：

```text
Claim<T>

subject
assertion
status

evidence[]
counter_evidence[]
unknowns[]

policy
confidence

provenance
```

例如：

```text
ReachabilityClaim

Subject:
    Product-A:v3.2 / CVE-XXXX

Assertion:
    vulnerable_function is NOT_REACHABLE

Evidence:
    E01
    E02
    E03

CounterEvidence:
    none

Unknowns:
    dynamic reflection path unresolved

Policy:
    reachability-policy-v1

Provenance:
    analyzer/version/time
```

这样才能真正支持：

```text
Evidence
   ↓
Claim
   ↓
Decision
```

---

# 14. UNKNOWN 必须是一等公民

安全分析不能强制二值化。

建议：

```text
AFFECTED
NOT_AFFECTED
FIXED
UNDER_INVESTIGATION
UNKNOWN
HUMAN_REVIEW
```

Reachability：

```text
REACHABLE
NOT_REACHABLE
UNKNOWN
```

Exploitability：

```text
EXPLOITABLE
NOT_EXPLOITABLE
UNKNOWN
```

因为：

> **“当前证据不足”本身就是一个合法、可审计的 Assessment 状态。**

Agent 遇到 UNKNOWN，可以继续寻找 Evidence；无法消除不确定性时进入 Human Review。

---

# 15. Evidence 必须具有 Provenance

CRA、VEX、认证最终需要的不是一个模型回答，而是可复现证据。

每条 Evidence 至少应该记录：

```text
Evidence

id
type

source
tool
tool_version
rule_version

input
source_commit
artifact_hash
sbom_version

configuration
parameters
environment

timestamp
producer

raw_result
normalized_result
```

这样未来才能回答：

> 为什么当时做出这个判断？

以及：

> 现在输入发生变化，这个判断是否仍然成立？

---

# 16. VEX 的正确位置

不要：

```text
SCA
 ↓
VEX
```

而应该：

```text
Evidence
   ↓
Assessment
   ↓
Claim
   ↓
Decision
   ↓
VEX Adapter
   ↓
VEX
```

所以：

> **VEX 是 Assessment 的标准化 Projection / Consumer，不是内部数据模型。**

同一个 Assessment：

```text
Assessment
   ├──→ CycloneDX VEX
   ├──→ OpenVEX
   ├──→ CSAF
   ├──→ CRA Evidence
   ├──→ CI Gate
   └──→ Security Advisory
```

---

# 17. CRA 的正确位置

同理：

```text
Vulnerability Assessment
        +
SBOM
        +
Risk Assessment
        +
Remediation Records
        +
Verification
        +
Disclosure
        +
Audit Trail
        ↓
CRA Workflow / Evidence
```

所以：

> **CRA 是 Consumer / Policy / Workflow Layer，而不是底层漏洞分析模型。**

这也是为什么底层设计不应该叫：

```text
CRA Vulnerability Model
```

而应该是：

```text
Vulnerability Assessment Model
```

---

# 18. CRA 场景下最终形成四条数据流

### ① Supply Chain Flow

```text
Product
 ↓
Artifact
 ↓
SCA
 ↓
SBOM
 ↓
Component
 ↓
Version
 ↓
CVE
```

### ② Vulnerability Assessment Flow

```text
CVE
 ↓
Localization
 ↓
CodeGraph
 ↓
Reachability
 ↓
Exploitability
 ↓
Claim
 ↓
Decision
```

### ③ Remediation Flow

```text
Decision
 ↓
Fix Strategy
 ↓
Dependency Upgrade / Patch / Code Fix
 ↓
Build
 ↓
Test
 ↓
Re-scan
 ↓
Re-Assessment
 ↓
Verification
```

### ④ Compliance Flow

```text
Assessment
 +
SBOM
 +
Remediation
 +
Verification
 +
Audit Trail
 ↓
VEX / CSAF
 ↓
CRA Evidence
 ↓
Technical Documentation
 ↓
Compliance / Conformity Workflow
```

---

# 19. 最关键的是最后那个 Feedback Loop

最初画的闭环里，最有价值的其实是最后这一根箭头：

```text
Verification
     │
     ▼
Evidence / VEX / SBOM
     │
     ▼
Continuous Monitoring
     │
     ├── New CVE
     ├── New KEV
     ├── New Advisory
     ├── New EPSS
     ├── New Product Version
     ├── New SBOM
     ├── New Runtime Config
     └── New Patch
             │
             ▼
        Evidence Changed
             │
             ▼
       Claim Invalidated
             │
             ▼
          Agent
             │
             ▼
       Re-Assessment
```

这使系统从：

> Vulnerability Scanner

变成：

> **Continuous Vulnerability Assessment System**

这是非常重要的产品边界变化。

---

# 20. 从 Finding-centric 转向 Assessment-centric

传统系统中心通常是：

```text
Finding

CVE = XXX
Severity = Critical
Status = Open
Fix = Upgrade
```

而这套架构的中心变成：

```text
Assessment
(
    Product,
    Version,
    Component,
    Vulnerability,
    Context
)
```

里面包含：

```text
Presence
Localization
Reachability
Exploitability
Evidence
CounterEvidence
Unknowns
Decision
Remediation
Verification
Provenance
```

所以系统思维发生了变化：

```text
Scanner
  ↓
Finding
```

变成：

```text
Vulnerability
      ↓
Evidence Collection
      ↓
Assessment
      ↓
Claim
      ↓
Decision
      ↓
Action
      ↓
Verification
      ↓
Re-Assessment
```

---

# 21. “Security Analysis Compiler” 是一个很好的技术隐喻

整个系统实际上越来越像编译器：

```text
                 Frontend

 SCA    Static    Dynamic    Binary    Runtime
  │       │          │         │         │
  └───────┴──────────┴─────────┴─────────┘
                      │
                   Lowering
                      │
                      ▼
                    VA-IR
                      │
                      ▼
                Evidence Graph
                      │
                Analysis Passes
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
 Localization   Reachability   Exploitability
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                   Decision
                      │
                   Backend
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
       VEX           CRA           CSAF
```

而：

> **Agent = Dynamic Pass Manager**

传统 Pass Manager：

```text
Pass A
 ↓
Pass B
 ↓
Pass C
 ↓
Pass D
```

Agentic Pass Manager：

```text
Current VA-IR
     ↓
Evidence Gap
     ↓
Agent
     ↓
选择下一 Analysis Pass
     ↓
New Evidence
     ↓
Update Claim
     ↓
重新判断 Evidence Gap
```

因此 Agent 不是装饰层，而是整个 Assessment Engine 的 **Control Plane**。

---

# 22. CodeGraph 开源项目在这里的位置

我们还讨论了使用现有 CodeGraph 基础设施。

正确定位不是：

> 完整 SAST / Exploitability Engine

而是：

> **Code Fact Provider / Structural Program Graph**

它适合提供：

```text
Symbol
Definition
Reference
Caller
Callee
Import
Inheritance
Impact
Structural Call Path
```

可以直接支持第一阶段：

```text
CVE
 ↓
Localization
 ↓
Vulnerable Symbol
 ↓
CodeGraph
 ↓
Caller / Callee
 ↓
Structural Reachability
 ↓
Evidence
```

但不能把：

```text
A → B → vulnerable_func
```

直接解释成：

```text
EXPLOITABLE
```

后续仍需要：

```text
CFG
DFG
Taint
Alias
Points-to
Path Sensitivity
Runtime
Config
```

因此技术路线可以逐层升级：

```text
Structural Reachability
        ↓
CFG Reachability
        ↓
DataFlow Reachability
        ↓
Taint Reachability
        ↓
Runtime Reachability
        ↓
Exploitability
```

---

# 23. 行业现状带来的结论

讨论过程中也对比了当前安全产品的大致能力。

行业已经普遍具备相当多零件：

```text
SBOM                ✓ 成熟
SCA                 ✓ 成熟
CVE Matching        ✓ 成熟
Threat Intelligence ✓ 成熟
Reachability        ✓ 已产品化
Prioritization      ✓ 成熟
Remediation Advice  ✓ 成熟
Automated PR        ✓ 已出现
Re-scan             ✓ 成熟
VEX                 ✓ 已产品化
Continuous Monitor  ✓ 成熟
```

所以如果新产品只定义为：

> **SCA + Reachability + LLM**

差异化并不强。

真正值得进一步验证和沉淀的是：

```text
Unified VA-IR
       +
Evidence Graph
       +
Claim Model
       +
Evidence Provenance
       +
Agent Dynamic Evidence Acquisition
       +
Decision Policy
       +
Remediation
       +
Verification
       +
Continuous Re-Assessment
```

尤其是：

> **统一 Evidence → Claim → Decision → Action → Verification → Re-Assessment 模型。**

---

# 24. 最适合的第一版 PoC

不要一开始追求完整 CRA 平台。

第一阶段只证明最核心的假设：

```text
Real Repository
      ↓
     SCA
      ↓
Component + Version
      ↓
Real CVE
      ↓
Localization
      ↓
Vulnerable Symbol
      ↓
CodeGraph
      ↓
Structural Call Path
      ↓
Reachability Evidence
      ↓
Reachability Claim
      ↓
VA-IR
      ↓
Decision
      ↓
VEX
```

同时 Agent 参与：

```text
Current Assessment
       ↓
Agent
       ↓
发现缺少 Localization Evidence
       ↓
Localization Skill
       ↓
发现缺少 Reachability Evidence
       ↓
CodeGraph Skill
       ↓
Evidence Complete
       ↓
Decision
```

这就已经能够验证四个最核心的技术假设：

**VA-IR 是否成立、Evidence Graph 是否成立、Agent Dynamic Pass Manager 是否成立、Consumer Adapter 是否成立。**

---

# 25. 后续演进路线

第一阶段：

```text
SCA
→ Localization
→ Structural Reachability
→ Claim
→ VA-IR
→ VEX
```

第二阶段：

```text
+ CFG
+ DFG
+ Taint
+ Exploitability
```

第三阶段：

```text
+ Remediation Agent
+ Dependency Upgrade
+ Patch
+ Build
+ Test
+ Verification
```

第四阶段：

```text
+ Runtime
+ DAST
+ Config
+ Threat Intelligence
+ Continuous Re-Assessment
```

第五阶段：

```text
+ CRA Workflow
+ CSAF
+ CI/CD
+ Assurance / Certification Profiles
```

---

# 26. 最后冻结成几条“架构不变量”

我认为整个会话最终最值得保留下来的其实是这几条：

**第一，CRA 是 Consumer，不是 Architecture Core。**

**第二，SCA 是 Vulnerability Assessment 的入口，而不是终点。**

**第三，Vulnerability Localization 是连接 Supply Chain Analysis 与 Program Analysis 的关键桥梁。**

**第四，CodeGraph 是 Static Analysis 产生的代码事实表示，不应与 Static Analysis 本身混为同一抽象层。**

**第五，Reachability ≠ Exploitability。后者需要 DataFlow、Runtime、Config、Precondition、Mitigation 等更丰富证据。**

**第六，确定性工具产生 Evidence；Agent 编排 Evidence，而不是替代分析器产生“感觉式结论”。**

**第七，Agent 是 Assessment Control Plane / Dynamic Pass Manager。**

**第八，Evidence → Claim → Decision 是核心判定链；UNKNOWN/HUMAN_REVIEW 必须是一等状态。**

**第九，所有 Evidence 必须带 Provenance，保证可解释、可复现、可审计。**

**第十，VEX/CRA/CSAF 都应该是 VA-IR 的 Consumer / Adapter，而不是内部核心数据模型。**

**第十一，真正的平台核心资产是 `VA-IR + Evidence Graph + Claim/Decision Engine + Agent Orchestration`。**

**第十二，闭环不是以 Fix 结束，而是以 Verification → Continuous Monitoring → Claim Invalidation → Re-Assessment 重新开始。**

最终整套思想可以压缩成这一张图：

```text
                         Vulnerability Event
                                  │
                                  ▼
                     ┌──────────────────────┐
                     │        Agent         │
                     │ Assessment Control   │
                     │       Plane          │
                     └──────────┬───────────┘
                                │
                         Evidence Gap
                                │
          ┌─────────────────────┼────────────────────┐
          ▼                     ▼                    ▼
         SCA              Static Analysis       Dynamic/Runtime
          │                     │                    │
          ▼                     ▼                    ▼
 Component Graph            CodeGraph          Runtime Evidence
          │              CG / CFG / DFG              │
          │                     │                    │
          └─────────────────────┼────────────────────┘
                                ▼
                         Evidence Graph
                                │
                                ▼
                              VA-IR
                                │
                                ▼
                              Claim
                                │
                                ▼
                            Decision
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
           NOT_AFFECTED                     AFFECTED
                 │                             │
                 ▼                             ▼
                VEX                       Remediation
                                               │
                                               ▼
                                          Build/Test
                                               │
                                               ▼
                                          Verification
                                               │
                                               ▼
                                         New Evidence
                                               │
                                               ▼
                                       Re-Assessment
                                               │
             ┌─────────────────────────────────┼───────────────┐
             ▼                                 ▼               ▼
            VEX                               CRA             CSAF
```

一句话收尾：

> **这不是“用 AI 做 SCA”，也不是“用 LLM 做 CRA”；它更接近构建一个以 Evidence 为事实基础、以 VA-IR 为中间表示、以 Agent 为动态 Pass Manager 的 Vulnerability Assessment Engine，再把 CRA/VEX/CSAF/CI/CD/认证体系做成它的不同 Backend。**

这应该就是本会话最终形成的最核心技术思想。
