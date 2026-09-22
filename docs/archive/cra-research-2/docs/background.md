对。上一版更偏“产品战略 + 技术架构研究”，但你现在是准备真正接手 CRA/SCA 这个课题，那么 Deep Research 还应该承担一个任务：**帮你快速补齐这个领域的知识地图**。

也就是说报告前半部分应该先回答“这个领域到底有哪些概念、标准、组织、数据源，它们之间是什么关系”，然后再进入产品设计。否则直接看到 VEX、CSAF、PURL、CPE、EPSS、KEV、NVD、OSV，很容易知道它们“有用”，但不知道分别处在漏洞生命周期哪一层。

我建议把下面这一大章插到刚才提示词的 **CRA 法规背景之后、产品能力分析之前**。

# 补充要求：建立完整的 SCA / Vulnerability Management / CRA 背景知识体系

在进入产品定位、技术架构和产品能力设计之前，请先用较大篇幅建立本课题所需的背景知识体系。

假设读者：

* 有软件研发和安全工程背景；
* 理解基本的 CVE、软件依赖、静态分析概念；
* 但没有系统研究过 SCA、SBOM、VEX、漏洞情报和 CRA 生态。

目标不是简单制作“术语表”，而是帮助读者建立完整的：

**Software Supply Chain Security / Vulnerability Management Mental Model**

要求解释：

> 每个概念是什么 → 为什么产生 → 解决什么问题 → 谁维护 → 数据长什么样 → 在漏洞生命周期哪个阶段使用 → 与其他概念是什么关系 → 对 CRA/SCA 产品有什么意义。

---

# 一、首先建立整个领域的知识地图

请先画出一张完整关系图，至少覆盖：

```text
Software Product
        │
        ↓
     Component
        │
        ↓
   Package Identity
   PURL / CPE
        │
        ↓
       SBOM
   SPDX / CycloneDX
        │
        ↓
Vulnerability Intelligence
        │
 ┌──────┼─────────┐
 ↓      ↓         ↓
NVD    OSV      Vendor Advisory
 │
CVE / CWE
 │
CVSS / EPSS / KEV
 │
 ↓
Vulnerability Association
 │
 ↓
Reachability
 │
 ↓
Exploitability
 │
 ↓
VEX
 │
 ↓
Remediation
 │
 ↓
Security Advisory / CSAF
 │
 ↓
CRA Evidence / Reporting
```

说明这些对象不是同一个层次：

* Identifier
* Database
* Data Source
* Data Format
* Standard
* Scoring System
* Threat Intelligence
* Analysis Result
* Compliance Artifact

必须帮助读者避免把这些概念混在一起。

---

# 二、漏洞基础体系

系统解释以下概念。

## CVE

解释：

* CVE 是什么；
* 谁维护；
* CVE Numbering Authority（CNA）是什么；
* CVE Record 包含什么；
* CVE ID 解决什么问题；
* CVE 本身是不是漏洞数据库；
* CVE 和 NVD 有什么区别。

给一个真实 CVE 示例拆解。

## CWE

解释：

* CWE 是什么；
* CWE 与 CVE 的区别；
* 一个是 weakness taxonomy，一个是具体 vulnerability，这句话具体是什么意思；
* CVE 如何映射 CWE；
* CWE 对 SAST/SCA 分别有什么价值。

例如解释：

```text
CWE-79
   ↓
Cross-site Scripting weakness class

CVE-XXXX-XXXX
   ↓
某个具体产品中的具体 XSS 漏洞
```

---

# 三、NVD：重点解释

系统研究 NVD（National Vulnerability Database）。

必须回答：

* NVD 是什么；
* 谁维护；
* NVD 与 CVE Program 的关系；
* CVE 是不是 NVD 创建的；
* NVD 在 CVE 数据基础上增加了什么；
* CVSS、CWE、CPE、Reference 等信息如何进入 NVD；
* NVD API / Data Feed 如何使用；
* SCA 厂商为什么会使用 NVD；
* 只依赖 NVD 为什么不够；
* NVD 数据延迟、质量和 enrichment 问题；
* Vendor Advisory / GitHub Advisory / OSV 等为什么可以补充 NVD。

重点建立：

```text
Vulnerability discovered
        ↓
CNA assigns CVE
        ↓
CVE Record
        ↓
NVD enrichment
        ↓
CPE / CVSS / CWE / References
        ↓
SCA vulnerability database
```

同时说明现实世界不一定严格按照这一线性流程发生。

---

# 四、OSV / GHSA / Vendor Advisory

分别解释：

### OSV

* Open Source Vulnerabilities 是什么；
* 为什么 Google 要建立 OSV；
* OSV Schema；
* ecosystem/package/version 如何描述；
* 与 NVD/CPE 模型相比有什么特点；
* 为什么它特别适合 SCA。

### GitHub Security Advisory / GHSA

解释：

* GHSA ID；
* GitHub Advisory Database；
* 与 CVE 的关系；
* 一个 GHSA 是否一定有 CVE；
* Dependency Graph / Dependabot 如何利用这些数据。

### Vendor Advisory

解释：

为什么：

Microsoft / Red Hat / Debian / Ubuntu / Apache / GitHub / 各开源项目

自己的 advisory 在很多情况下可能比 NVD 更准确。

最后比较：

```text
CVE
NVD
OSV
GHSA
Vendor Advisory
```

它们分别是什么、谁维护、解决什么问题、SCA 如何组合使用。

---

# 五、CVSS / EPSS / KEV

这是漏洞优先级判断的重要背景知识，必须深入解释。

## CVSS

解释：

* CVSS 是什么；
* Base / Temporal / Environmental 等思想；
* CVSS v3.x 与 v4.0；
* CVSS 衡量的是 severity 还是真实 exploitation probability；
* 为什么 CVSS 9.8 不意味着必须第一个修。

## EPSS

解释：

* Exploit Prediction Scoring System；
* 谁维护；
* probability 的含义；
* EPSS 与 CVSS 最大区别；
* 如何用于漏洞 prioritization。

## CISA KEV

解释：

* Known Exploited Vulnerabilities Catalog；
* 什么叫 known exploited；
* KEV 与“存在 PoC”有什么区别；
* 为什么 KEV 是很强的风险信号。

形成：

```text
CVSS
    → How severe could it be?

EPSS
    → How likely is exploitation?

KEV
    → Has exploitation been observed?

Reachability
    → Can my software reach it?

Exploitability
    → Can it actually be exploited
       in MY product context?
```

并讨论这些信号如何共同形成 Risk Decision。

---

# 六、Package Identity：CPE 与 PURL

重点解释这是 SCA 很基础但非常容易被忽略的问题：

> “我扫描出来的组件”和“漏洞数据库里的组件”到底怎么关联？

## CPE

解释：

* Common Platform Enumeration；
* CPE URI；
* vendor/product/version；
* NVD 为什么大量使用 CPE；
* CPE mapping 为什么容易出现误匹配。

## PURL

解释：

Package URL，例如：

```text
pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1
```

拆解：

* type
* namespace
* name
* version
* qualifiers

说明 PURL 为什么更适合现代 package ecosystem。

比较：

```text
CPE
vs
PURL
```

以及它们对 Vulnerability Association 的影响。

---

# 七、SBOM：重点背景知识

系统解释 Software Bill of Materials。

不要只说“软件物料清单”。

回答：

* SBOM 为什么出现；
* 一个 SBOM 到底包含什么；
* Component；
* Version；
* Dependency；
* Hash；
* License；
* Supplier；
* Relationship。

给出一个小型 SBOM 示例。

解释两个主要标准：

## SPDX

* 谁维护；
* 最初解决什么问题；
* license compliance 背景；
* 后来如何扩展到 SBOM。

## CycloneDX

* 谁维护；
* 为什么 security use case 很强；
* Components；
* Dependencies；
* Vulnerabilities；
* Services；
* VEX。

比较：

SPDX vs CycloneDX

但不要简单判断哪个“更好”，而要分析不同使用场景。

重点解释：

```text
Source Code
    ↓
SCA
    ↓
Component Inventory
    ↓
SBOM
```

以及：

SBOM ≠ SCA

为什么？

---

# 八、VEX：必须重点解释

这是整个研究中的核心背景知识之一。

系统解释：

**Vulnerability Exploitability eXchange**

首先解释它为什么出现。

例如：

```text
SBOM says:

Product A
  contains
log4j-core 2.14.1

NVD says:

log4j-core 2.14.1
  affected by
CVE-2021-44228
```

但：

```text
Does Product A actually suffer from this vulnerability?
```

SBOM 本身回答不了。

因此需要：

```text
SBOM
    ↓
What components exist?

VEX
    ↓
What is the vulnerability status
of those components in THIS product?
```

深入解释典型 VEX status：

```text
affected
not_affected
fixed
under_investigation
```

尤其解释：

`not_affected`

为什么必须有 justification / evidence。

例如：

```text
not_affected

reason:
vulnerable_code_not_present
```

或者：

```text
not_affected

reason:
vulnerable_code_not_in_execute_path
```

研究：

* CycloneDX VEX；
* CSAF VEX；
* OpenVEX；
* 不同实现之间的关系。

重点回答：

> VEX 是一种“文件格式”，还是一种“漏洞判断结果”？

从产品设计角度进一步讨论：

```text
Reachability
       +
Exploitability
       +
Runtime Context
       +
Security Expert / Agent Decision
       ↓
     VEX
```

这种模型是否合理。

---

# 九、CSAF

解释：

Common Security Advisory Framework。

说明：

* CSAF 是什么；
* 谁维护；
* Security Advisory 为什么需要机器可读；
* CSAF 与传统 PDF/网页 Security Advisory 的区别；
* CSAF 与 VEX 的关系；
* CSAF VEX Profile 是什么。

建立：

```text
Vendor
   ↓
Security Advisory
   ↓
CSAF
   ↓
Machine-readable
vulnerability information
```

并分析它与 CRA vulnerability disclosure / communication 的关系。

---

# 十、Reachability

从初学者可以理解的方式开始，然后深入技术。

例如：

```text
Application
   ↓
depends on
Library A
   ↓
contains
vulnerable_function()
```

Presence Analysis 只能证明：

```text
vulnerable component exists
```

Reachability 要回答：

```text
Application entrypoint
       ↓
foo()
       ↓
bar()
       ↓
vulnerable_function()
```

这条路径是否存在。

区分：

* Package Reachability
* Module Reachability
* Symbol Reachability
* Function Reachability
* Call Path Reachability
* Vulnerable Branch Reachability
* Runtime Reachability

解释：

为什么 Reachability 能减少 SCA false positive。

同时说明：

**Reachable ≠ Exploitable**

---

# 十一、Exploitability

建立：

```text
Present
   ↓
Affected
   ↓
Reachable
   ↓
Input Controllable
   ↓
Precondition Satisfied
   ↓
Exploitable
```

解释：

为什么漏洞存在、代码可达，仍然不一定可利用。

考虑：

* network exposure；
* authentication；
* attacker-controlled input；
* runtime configuration；
* feature flags；
* privilege；
* sandbox；
* mitigations；
* operating environment。

进一步说明：

Exploitability Analysis

与：

CVSS / EPSS / KEV / Reachability

之间的区别。

---

# 十二、漏洞修复相关概念

解释：

* Fix Version
* Patch
* Fix Commit
* Backport
* Workaround
* Mitigation
* Upgrade
* Dependency Update
* Breaking Change
* Remediation
* Verification

特别区分：

```text
Mitigation
vs
Remediation
vs
Fix
```

以及：

```text
Fixed upstream
≠
Fixed in dependency
≠
Fixed in my product
≠
Fix verified
```

---

# 十三、漏洞披露体系

解释：

* Vulnerability Disclosure
* Coordinated Vulnerability Disclosure
* Responsible Disclosure
* Security Advisory
* PSIRT
* CNA

研究一个漏洞从研究人员发现开始：

```text
Researcher
    ↓
Vendor / PSIRT
    ↓
Triage
    ↓
CNA
    ↓
CVE
    ↓
Patch
    ↓
Security Advisory
    ↓
NVD / OSV / GHSA
    ↓
Downstream SCA
```

解释现实世界中实际流程可能有哪些变化。

再将 CRA reporting obligation 放入这张图中。

---

# 十四、标准和组织知识地图

最终制作一个表格，至少覆盖：

| 名称        | 类型                | 维护组织             | 解决的问题                | 生命周期位置       |
| --------- | ----------------- | ---------------- | -------------------- | ------------ |
| CVE       | Identifier/System | CVE Program      | 漏洞统一标识               | Discover     |
| CWE       | Taxonomy          | MITRE            | 弱点分类                 | Analyze      |
| NVD       | Database          | NIST             | 漏洞 enrichment        | Intelligence |
| CVSS      | Scoring           | FIRST            | Severity             | Prioritize   |
| EPSS      | Prediction        | FIRST            | Exploit probability  | Prioritize   |
| KEV       | Catalog           | CISA             | Known exploitation   | Prioritize   |
| CPE       | Identifier        | NIST             | Product identity     | Association  |
| PURL      | Identifier        | Package URL spec | Package identity     | Association  |
| SBOM      | Artifact          | 多标准              | 软件组成                 | Inventory    |
| SPDX      | Standard          | Linux Foundation | SBOM/license         | Inventory    |
| CycloneDX | Standard          | OWASP            | SBOM/security        | Inventory    |
| VEX       | Artifact/Model    | 多生态              | Vulnerability status | Assess       |
| CSAF      | Standard          | OASIS            | Security advisory    | Communicate  |

要求进一步补充遗漏的重要概念。

---

# 十五、最后建立一张“我应该如何理解整个领域”的 Mental Model

最终不要让读者记几十个缩写。

把它们重新组织成一条完整故事：

```text
我有什么软件？
        ↓
Product Inventory

软件里有什么？
        ↓
SBOM
SPDX / CycloneDX

这些组件是谁？
        ↓
PURL / CPE

世界上有哪些漏洞？
        ↓
CVE
NVD / OSV / GHSA
Vendor Advisory

漏洞严重吗？
        ↓
CVSS

现实中可能被攻击吗？
        ↓
EPSS / KEV
Threat Intelligence

这个漏洞和我的产品有关吗？
        ↓
Vulnerability Association

漏洞代码真的能走到吗？
        ↓
Reachability

在我的运行环境真的能利用吗？
        ↓
Exploitability

我对这个漏洞的正式判断是什么？
        ↓
VEX

怎么解决？
        ↓
Remediation

真的修掉了吗？
        ↓
Verification

怎么告诉客户/上下游？
        ↓
Security Advisory / CSAF

怎么证明整个过程？
        ↓
Evidence / Audit Trail

CRA 要求我承担什么责任？
        ↓
Compliance Workflow / Reporting
```

对于每一层同时说明：

**Concept → Standard → Data Source → Tool → Product Capability → CRA Relevance**

完成背景知识体系后，再继续进行原提示词中的：

* CRA Capability Mapping
* 产品定位
* 产品形态
* Reachability
* Exploitability
* Remediation
* Agent
* Evidence Graph
* 竞争分析
* 技术架构
* MVP
* Roadmap

等研究。

最终报告应做到：

> 一个熟悉软件研发但此前没有系统研究 SCA/漏洞管理的人，看完前 20%～30% 的报告以后，能够建立完整的领域知识地图，并理解后续产品和技术方案为什么这样设计。

不要把背景知识写成百科全书式术语罗列。所有概念都应该放到“漏洞全生命周期”中解释其位置和作用。

这样改以后，我觉得这个 Research 的结构就比较完整了：

**第一层：Know the Domain**——CVE、CWE、NVD、OSV、CVSS、EPSS、KEV、CPE、PURL、SBOM、SPDX、CycloneDX、VEX、CSAF……到底是什么。

**第二层：Know the Regulation**——CRA 到底要求企业承担什么责任。

**第三层：Know the Problem**——为什么传统 `Component → CVE` SCA 不足以解决 CRA 下的漏洞生命周期问题。

**第四层：Design the Product**——`Product → SBOM → Association → Reachability → Exploitability → VEX → Remediation → Verification → Evidence → CRA`。

**第五层：Find the Moat**——Reachability、Exploitability、Evidence Graph、Agentic Remediation 哪些真能形成壁垒，哪些只是产品功能。

这样你周日开会的时候，就不仅是在讨论“开发哪些 feature”，而是你自己先把**这个领域的 ontology（概念体系）和 capability map（能力地图）建立起来了**。后面不管和 SCA 专家、产品经理还是 CTO 聊，大家说 NVD、VEX、CSAF、KEV、PURL 时，你脑子里都有它在整个系统中的坐标。
