# 01 — Software Supply Chain Security / Vulnerability Management 领域知识体系（Domain Ontology）

> **读者假设**：有软件研发和安全工程背景，理解 CVE/依赖/静态分析的基础概念，但没有系统研究过 SCA、SBOM、VEX、漏洞情报与 CRA 生态。
>
> **写作约定**：中文为主，技术术语保留英文。每个概念按统一线索展开：**是什么 → 为什么产生 → 解决什么问题 → 谁维护 → 数据长什么样 → 在漏洞生命周期哪个阶段使用 → 与其他概念的关系 → 对 SCA/合规产品的意义**。
>
> **证据规范**：文中标记 **（Fact）** 表示有一手来源支撑，标记 **（Interpretation）** 表示本文作者的推理与归纳，无法核实的标记 **（不确定）**。每条一手来源在 [docs/research/01-domain-ontology/sources/](01-domain-ontology/sources/) 下有对应 source note，研究过程见 [research-log.md](01-domain-ontology/research-log.md)。
>
> 调研执行日：2026-09-18。需要特别注意的时代背景：**欧盟 CRA（Regulation (EU) 2024/2847）Article 14 漏洞报告义务已于 2026-09-11 起适用**（24h/72h 报告时钟已开始走动），其余主体义务 2027-12-11 全面适用（Fact，见 [sources/cra-regulation-2024-2847.md](01-domain-ontology/sources/cra-regulation-2024-2847.md)）。这不是遥远的合规议题，而是正在发生的事实。

---

## 1. 领域知识地图：先分清层次，再谈概念

初学者最容易犯的错，是把 CVE、NVD、CVSS、SBOM、VEX 当成"同一类东西"并列记忆。它们其实处在**完全不同的抽象层次**上。先建立这张分层表：

| 层次（Layer） | 回答的问题 | 代表概念 |
|---|---|---|
| **Identifier（标识符）** | 这个东西叫什么？ | CVE ID、CWE ID、GHSA ID、CPE、PURL |
| **Taxonomy（分类法）** | 它属于哪一类问题？ | CWE |
| **Scoring System（评分体系）** | 它有多严重/多可能被利用？ | CVSS、EPSS |
| **Database（数据库）** | 去哪里查结构化记录？ | NVD、GitHub Advisory Database、各 Linux 发行版 tracker |
| **Data Source / Feed（数据源）** | 原始信息从哪来？ | CNA 发布的 CVE Record、Vendor Advisory、CISA KEV、Exploit-DB |
| **Data Format（数据格式）** | 数据怎么序列化交换？ | CVE JSON 5.x、OSV Schema、CSAF、OpenVEX、SPDX/CycloneDX 文档格式 |
| **Standard（标准/规范）** | 大家按什么规则做事？ | CVSS（FIRST）、CSAF（OASIS）、SPDX（ISO/IEC 5962）、PURL（ECMA-427）、SSDF、SLSA |
| **Threat Intelligence（威胁情报）** | 现实中攻击者在干什么？ | CISA KEV、EPSS、勒索软件关联标注、商业 TI feed |
| **Analysis Result（分析结论）** | 对我的产品意味着什么？ | Vulnerability Association、Reachability、Exploitability、VEX statement |
| **Compliance Artifact（合规工件）** | 拿什么证明/通报？ | SBOM、VEX 文档、CSAF advisory、CRA 报告、Evidence/Audit Trail |

同一名字可能跨层：例如 "VEX" 既是一种**判断模型**（Analysis Result 层），又有三种**文件格式实现**（Data Format 层）；"SBOM" 既是 Compliance Artifact，其载体 SPDX/CycloneDX 又是 Data Format/Standard。读任何材料时先问"它此刻指哪一层"，大部分困惑会消失。

整个领域的关系图（自上而下是"从资产到合规"的流向）：

```text
Software Product（我发布的产品，CRA 的责任对象）
        │  contains
        ▼
Component（第三方/开源组件）─── Package Identity: PURL / CPE（Identifier 层）
        │  被记录在
        ▼
SBOM（SPDX / CycloneDX）（Compliance Artifact 层：我有什么）
        │  与漏洞情报做关联匹配
        ▼
Vulnerability Intelligence（Data Source 层：世界上有什么漏洞）
   ┌────┼─────────┬──────────┐
   ▼    ▼         ▼          ▼
  NVD  OSV      GHSA     Vendor Advisory
   └──全部锚定──┴── CVE Record（Identifier: CVE ID；Taxonomy: CWE）
        │  附带优先级信号
        ▼
CVSS（severity）/ EPSS（likelihood）/ KEV（observed exploitation）（Scoring + TI 层）
        │  结合我的资产做判断
        ▼
Vulnerability Association → Reachability → Exploitability（Analysis Result 层）
        │  形成正式结论
        ▼
VEX（status + justification）（Analysis Result → Compliance Artifact）
        │
        ▼
Remediation / Verification（行动层）
        │
        ▼
Security Advisory（CSAF，机器可读通报）→ CRA Evidence / Reporting（合规闭环）
```

---

## 2. CVE：漏洞世界的"身份证"系统

### 是什么

CVE（Common Vulnerabilities and Exposures）是一个**给公开披露的漏洞分配唯一标识符并编目**的计划。CVE Program 的官方使命是 "identify, define, and catalog publicly disclosed cybersecurity vulnerabilities. There is one CVE Record for each vulnerability in the catalog."（Fact，[cve.org About](https://www.cve.org/About/Overview)，见 [sources/cve-program-overview.md](01-domain-ontology/sources/cve-program-overview.md)）

关键理解：**CVE 的核心交付物是"一个漏洞 ↔ 一个 ID ↔ 一条 Record"的对应关系**，解决的是"大家说的是不是同一个漏洞"的通信问题。在 CVE 出现（1999 年）之前，同一个漏洞在不同厂商公告、不同扫描器里各有名字，安全团队无法对齐讨论对象。

### 谁维护：CNA 联邦机制

CVE Program 由 MITRE 运营秘书处、CISA 资助，但**漏洞不由 MITRE 集中录入**。分配权下放给 CNA（CVE Numbering Authorities）——被授权"在自己覆盖范围内分配 CVE ID 并发布 CVE Record"的组织，包括厂商、开源基金会、CERT、bug bounty 平台等。截至 2026-09 有 **517 家 CNA（514 CNA + 3 CNA-LR），来自 43 个国家**；加入无费用、无合同（Fact，[cve.org CNAs](https://www.cve.org/ProgramOrganization/CNAs)，见 [sources/cve-program-cna.md](01-domain-ontology/sources/cve-program-cna.md)）。不在任何 CNA 范围内的漏洞由 CNA-LR（Last Resort，如 MITRE、CISA）兜底。

治理结构：Top-Level Root → Root → CNA 三级，外加若干 Working Group。**这意味着 CVE 数据质量天然是异构的**——Apache CNA 的记录详尽程度和一个小型 CNA 可能完全不同（Interpretation）。

### CVE Record 长什么样：CVE-2021-44228 真实拆解

通过 CVE 官方 API（`cveawg.mitre.org/api/cve/CVE-2021-44228`，CVE JSON 5.1 格式）拿到的真实记录，结构如下（Fact，完整摘录见 [sources/cve-record-api-cve-2021-44228.md](01-domain-ontology/sources/cve-record-api-cve-2021-44228.md)）：

```json
{
  "dataType": "CVE_RECORD", "dataVersion": "5.1",
  "cveMetadata": {
    "cveId": "CVE-2021-44228",
    "assignerShortName": "apache",          // ← Apache 软件基金会作为 CNA 签发
    "dateReserved": "2021-11-26",           // ← 先占位预留
    "datePublished": "2021-12-10"           // ← 协调披露日
  },
  "containers": {
    "cna": {                                 // ← CNA 必填容器：一手事实
      "title": "Apache Log4j2 JNDI features do not protect against attacker controlled LDAP...",
      "descriptions": [{"lang": "en", "value": "Apache Log4j2 2.0-beta9 through 2.15.0 (excluding security releases 2.12.2, 2.12.3, and 2.3.1) ... this vulnerability is specific to log4j-core and does not affect log4net, log4cxx..."}],
      "affected": [{"vendor": "Apache Software Foundation", "product": "Apache Log4j2",
                     "versions": [{"version": "2.0-beta9", "status": "affected",
                                   "changes": [{"at": "2.3.1", "status": "unaffected"}, ...]}]}],
      "problemTypes": [{"descriptions": [{"cweId": "CWE-502", ...}]}, ...],   // ← CNA 给的 CWE 映射
      "credits": [{"value": "discovered by Chen Zhaojun of Alibaba Cloud Security Team"}],
      "metrics": [{"other": {"content": {"other": "critical"}}}]             // ← 注意：CNA 没给标准 CVSS！
    },
    "adp": [                                 // ← 授权数据发布者追加容器
      {"providerMetadata": {"shortName": "CISA-ADP"}, "title": "CISA ADP Vulnrichment",
       "metrics": [
         {"cvssV3_1": {"baseScore": 10, "vectorString": "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H", ...}},
         {"other": {"type": "ssvc", "content": {"options": [{"Exploitation": "active"}, ...]}}},
         {"other": {"type": "kev", "content": {"dateAdded": "2021-12-10"}}}
       ]}
    ]
  }
}
```

这条记录教给我们四件事：

1. **日期链条**（reserved 11-26 → published 12-10）就是协调披露（CVD）过程的化石记录。
2. **CNA 容器是"一手事实层"**：受影响的 vendor/product/version、CWE 分类、致谢、参考链接。Log4Shell 的描述甚至明确排除了 log4net/log4cxx。
3. **CVE Record 可以没有 CVSS 分数**。著名的 "CVSS 10.0" 实际来自 CISA-ADP 的 Vulnrichment 追加容器，不是 Apache CNA 给的。CVE Program 官方也明确辟谣："CVE Program is **not** responsible for assigning vulnerability severity scores"（Fact，[cve.org Overview](https://www.cve.org/About/Overview)）。ADP（Authorized Data Publisher）机制允许授权第三方向记录追加数据。
4. **references 是生态指针**：同一条记录挂出 Cisco、Debian DSA-5020、Fedora、Microsoft MSRC 等几十条带 `vendor-advisory` tag 的链接——CVE Record 是枢纽，不是终点。

### CVE 不是数据库；CVE ≠ NVD

这是最容易混淆的一点：

- **CVE 是标识与编目系统**：每条 Record 只承诺"这个漏洞存在、影响谁、描述是什么"。它不打分、不做产品字典映射、不提供检索引擎。
- **NVD 是美国政府建立在 CVE 之上的增强数据库**（详见 §4）：拿 CVE Record 做底料，追加 CVSS、CPE、CWE 修订、参考链接分类。
- 类比（Interpretation）：CVE 之于 NVD，如同 DOI 之于 Web of Science——前者解决"唯一标识"，后者解决"可检索、可度量、可关联"。

**生命周期位置**：Disclosure（披露时刻的命名与编目）。**对 SCA/合规产品的意义**：CVE ID 是跨数据库、跨工具、跨厂商的 join key；任何漏洞数据管道的第一步都是围绕 CVE ID 做实体对齐（entity resolution）。没有 CVE ID 的漏洞（很多 GHSA、内部发现）是关联的难点。

---

## 3. CWE：弱点的分类法，不是漏洞清单

### 是什么 / 与 CVE 的本质区别

CWE（Common Weakness Enumeration）是 MITRE 维护的**社区共建的软硬件弱点分类清单**。官方定义："a 'weakness' is a condition in a software, firmware, hardware, or service component that, **under certain circumstances, could contribute to the introduction of vulnerabilities**"（Fact，[cwe.mitre.org/about](https://cwe.mitre.org/about/index.html)，见 [sources/cwe-about.md](01-domain-ontology/sources/cwe-about.md)）。

一句话区分（Fact 的推论）：

```text
CWE-79（Improper Neutralization of Input During Web Page Generation）
   = 一类弱点："输入没净化就进网页"这个模式
CVE-2024-XXXX
   = 某个具体产品 vX.Y 里的一次具体 XSS 漏洞实例
```

CWE 是**类别（class）**，CVE 是**实例（instance）**。一个 CWE 类别对应无数个 CVE；一个 CVE 通常映射到一个或多个 CWE。CWE List 每年更新 3–4 次，以多种 Views 组织（软件开发视图、硬件设计视图、研究概念视图），并有 CWE Top 25、OWASP Top 10 映射等衍生榜单。

### CVE 如何映射 CWE

两条路径（Fact，来自 §2 的实例）：① CNA 在 CVE Record 的 `problemTypes` 中声明（Apache 给 Log4Shell 标了 CWE-502/400/20）；② NVD 分析师在 enrichment 时补充或修订（NVD 给同一条补了 CWE-917）。**两个来源可能不一致**——CWE 映射本身是需要治理的数据质量问题（Interpretation）。

### 对 SAST / SCA 的价值

- **对 SAST**：SAST 工具检测的本来就是弱点类别（"这里有个可能的 SQL 注入模式"），CWE 是 SAST 规则集的通用编目语言；OWASP Top 10、CERT 编码规范都以 CWE 为锚。
- **对 SCA**：SCA 不检测弱点，但 CWE 给 CVE 提供"这是什么类型的问题"的横向聚合维度——按 CWE 聚类可以做系统性风险分析（"我们产品线上 CWE-502 反序列化类漏洞占比"）、驱动安全需求（禁用某类 API）、支持 CRA 所要求的风险管理文档化。

**生命周期位置**：Analyze/Classify（分析归类）。**对产品意义**：CWE 是从"处理一个个 CVE"走向"管理一类类风险"的抽象阶梯，也是 SAST 结果与 SCA 结果能放进同一张图的共同维度。

---

## 4. NVD 深挖：美国政府建的"增强版"漏洞数据库

### 是什么 / 谁维护 / 与 CVE Program 的关系

NVD（National Vulnerability Database）由 **NIST**（美国国家标准与技术研究院）运营，1999 年起以某种形式存在。它**不创建 CVE**——CVE 由 CVE Program 的 CNA 体系发布；NVD 是 CVE 数据的**下游消费者 + 增强者**：把所有 CVE Record 拉进来，由分析师追加结构化信息后再发布（Fact，综合 [NVD API 数据](https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228) 与 [NIST 公告](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth)，见 [sources/nvd-api-20-cve-2021-44228.md](01-domain-ontology/sources/nvd-api-20-cve-2021-44228.md)、[sources/nist-nvd-operations-2026.md](01-domain-ontology/sources/nist-nvd-operations-2026.md)）。

理想化流程（现实常不严格遵守，见下文）：

```text
漏洞被发现 → CNA 分配 CVE ID → CVE Record 发布
     → NVD 拉取并 enrichment（CPE / CVSS / CWE / References 分类）
     → 各类 SCA 漏洞库 / 扫描器 / 合规平台消费 NVD
```

### NVD 在 CVE 之上 enrichment 了什么

用 CVE-2021-44228 的 NVD API 2.0 响应实测对比（Fact，见 [sources/nvd-api-20-cve-2021-44228.md](01-domain-ontology/sources/nvd-api-20-cve-2021-44228.md)）：

| 字段 | CVE Record（CNA 层） | NVD 视图（enrichment 后） |
|---|---|---|
| CVSS | CNA 只有 "critical" 文本；CISA-ADP 补了 v3.1 10.0 | **NVD Primary 评分** `cvssMetricV31`（source: nvd@nist.gov），另存 cvssMetricV2、CISA SSVC |
| CWE | CNA: CWE-20/400/502 | 保留 CNA 的 + **NVD 追加 CWE-917** |
| 受影响产品 | vendor/product 字符串 + 版本 changes | **`configurations`：CPE Applicability Language 树**（AND/OR 节点 + `cpeMatch`，如 `cpe:2.3:o:siemens:6bk1602-0aa12-0tp0_firmware:*` 配 `versionEndExcluding`） |
| References | CNA 挂的几十条 | 扩展到 **103 条**并打 tag |
| 利用状态 | CISA-ADP 容器 | 内嵌一等字段：`cisaExploitAdd: 2021-12-10`、`cisaActionDue: 2021-12-24`、`cisaRequiredAction` |

其中最关键也最有争议的是 **CPE configurations**：NVD 分析师把"Apache Log4j2 2.0-beta9–2.15.0"这样的人话翻译成机器可匹配的 CPE 表达式树，包括"某固件运行在某硬件上才受影响"这类复合条件。SCA 工具传统的匹配方式就是把扫描到的组件映射成 CPE，再与这些 configurations 求交（详见 §9）。

### API 2.0 / Data Feed 使用方式

（Fact，[nvd.nist.gov/developers/vulnerabilities](https://nvd.nist.gov/developers/vulnerabilities)，见 [sources/nvd-api-developers.md](01-domain-ontology/sources/nvd-api-developers.md)）

- **CVE API**：`https://services.nvd.nist.gov/rest/json/cves/2.0`，按 CVE ID 或条件检索，offset 分页（`startIndex`/`resultsPerPage`）。
- **CVE Change History API**：`.../cvehistory/2.0`，追踪记录何时因何被改——对增量同步至关重要。
- 另有 CPE API / CPE Match Criteria API。官方提醒：**2015 年之前的记录字段保真度明显较低**。
- 工程实践（Interpretation）：生产级消费方应使用 API key 提高 rate limit，并以 change history 驱动增量更新，而非全量轮询。

### 数据延迟与质量问题：2024 slowdown → 2026 政策转向

这是整个领域近年最重要的事件，必须知道（Fact，[NIST 2026-04-15 官方公告](https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth)，见 [sources/nist-nvd-operations-2026.md](01-domain-ontology/sources/nist-nvd-operations-2026.md)）：

- **2024 年初起**（社区观察到 2024-02-12 速率骤降），NVD 形成大量未 enrichment 的 CVE 积压；NIST 官方承认"unable to clear that backlog"。
- 背景：CVE 提交量 2020→2025 增长 **263%**；NVD 2025 年 enrich 了约 42,000 条（创纪录）仍跟不上；2026 Q1 提交量又同比高约 1/3。
- **2026-04-15 起 NVD 放弃"全量 enrichment"目标**，改为风险优先：只对 ① CISA KEV 目录内 CVE（目标 1 个工作日）、② 联邦政府使用软件的 CVE、③ EO 14028 定义的 critical software 的 CVE 做即时 enrichment；其余标记 "Lowest Priority - not scheduled for immediate enrichment"；**2026-03-01 前的积压整体转入 "Not Scheduled"**。
- 同时 NVD **不再对 CNA 已给分的 CVE 重复打分**。

### 为什么只依赖 NVD 不够

1. **延迟与覆盖断层**（Fact，上文）：一个 CVE 可能已经公开、已有 exploit、已进 KEV，但在 NVD 里仍是 "Awaiting Analysis"/"Not Scheduled"，没有 CPE 和分数——只靠 NVD 的 SCA 会在最危险的窗口期失明。
2. **CPE 模型对现代包生态不适配**：CPE 以 vendor/product 字典描述"产品"，对 Maven/npm/PyPI 坐标映射质量参差（§9）。
3. **单点视角**：NVD 的分析是"美国政府视角"，vendor advisory / GHSA / OSV 常有更准的版本范围、更快的修复信息（§7）。
4. **记录会滞后变更**：NVD 2026 年起也不再对修改过的 CVE 例行重分析。

**对 SCA/合规产品的意义**（Interpretation）：NVD 仍是覆盖面最广的基准数据源和合规语境下的"权威引用"，但 2026 年之后，**"NVD + OSV + GHSA + vendor advisory 多源融合、以 CVE ID 为 join key"已经不是最佳实践，而是生存必需**。产品卖点之一就是弥补 NVD 的官方盲区。

---

## 5. OSV：为开源生态而生的漏洞交换格式与聚合库

### 为什么 Google 建 OSV

OSV（Open Source Vulnerabilities）由 Google 发起（2021），规范现由 OpenSSF 托管，作者为 Google 的 Oliver Chang 和 Russ Cox。规范开篇写明动机："define a standard interchange format for describing vulnerabilities in open source packages … enable **automated, accurate, and distributed** management of vulnerabilities in open source dependencies"（Fact，[OSV Schema 1.9.0](https://ossf.github.io/osv-schema/)，见 [sources/osv-schema-spec.md](01-domain-ontology/sources/osv-schema-spec.md)）。

要理解动机，先看 NVD/CPE 模型在开源世界的痛点（Interpretation）：开源组件的身份是**生态坐标**（Maven 的 `groupId:artifactId:version`、npm 的 `name@version`），不是 CPE 的 vendor/product；开源漏洞的受影响范围是**版本区间**，与具体 commit 强相关。OSV 把这两点变成一等公民。

### OSV Schema 拆解与真实条目

OSV 条目顶层字段：`id`（`<DB>-<ENTRYID>` 格式，如 `GHSA-jfh8-c2jp-5v3q`）、`aliases`（如指向 CVE-2021-44228）、`affected[]`、`severity[]`、`references[]` 等。核心是 `affected`（Fact，以下取自 [GHSA-jfh8-c2jp-5v3q 的真实 OSV 条目](https://api.osv.dev/v1/vulns/GHSA-jfh8-c2jp-5v3q)，见 [sources/osv-api-ghsa-log4shell.md](01-domain-ontology/sources/osv-api-ghsa-log4shell.md)）：

```json
"affected": [{
  "package": {
    "ecosystem": "Maven",
    "name": "org.apache.logging.log4j:log4j-core",
    "purl": "pkg:maven/org.apache.logging.log4j/log4j-core"
  },
  "ranges": [{
    "type": "ECOSYSTEM",
    "events": [{"introduced": "2.13.0"}, {"fixed": "2.15.0"}]
  }],
  "versions": ["2.13.0", "2.13.1", "2.13.2", "2.13.3", "2.14.0", "2.14.1"]
}, ... ]
```

要点：

- **组件身份 = ecosystem + name + purl**，三段式直击包管理器坐标。
- **版本范围 = 事件序列**：`introduced`/`fixed`/`last_affected`/`limit` 构成区间，类型可以是 `SEMVER`、`ECOSYSTEM`（生态原生版本序）或 `GIT`（commit 粒度）。Log4Shell 条目用三段区间精确表达了 "2.12.2/2.3.1 等 backport 安全版本不受影响"。
- 同一条目还建模了**换名 fork 包** `com.guicedee.services:log4j-core`（`introduced: 0`）——这种"同代码不同坐标"情形在 CPE 模型里几乎无法表达。
- `severity` 直接内嵌 CVSS 向量字符串。

### 与 CPE 模型对比 / 为什么适合 SCA

| 维度 | CPE 模型（NVD） | OSV 模型 |
|---|---|---|
| 身份表达 | vendor:product:version 字典 | ecosystem:name:version + PURL |
| 版本范围 | CPE 表达式 + start/end excluding | 事件序列区间 / 显式枚举 |
| 与依赖树的匹配 | 需要"包名→CPE"猜测映射 | **坐标直接相等比较** |
| 数据来源 | 中央分析师录入 | 各数据库分布式发布、osv.dev 聚合 |
| commit 粒度 | 无 | GIT range 原生支持 |

**OSV 适合 SCA 的根本原因**（Interpretation + Fact 支撑）：SCA 的输入是 lockfile/依赖树，输出需要"这个坐标这个版本是否受影响"。OSV 的数据模型与这个问题的形状完全一致——匹配几乎是无损的字符串/版本比较，不需要经过 CPE 这个易错中间层。OSV 同时是**格式**（任何漏洞库都可导出）和**服务**（osv.dev 聚合了 GHSA、PyPA、RustSec、Go vuln DB 等数十个数据库），是事实上的开源漏洞交换层。

**生命周期位置**：Intelligence（情报源）。**对产品意义**：OSV 应作为 SCA 漏洞库的第一优先数据源；`aliases` 字段提供与 CVE/GHSA 的免费实体对齐。

---

## 6. GHSA：GitHub Advisory Database 与生态策展

### 是什么 / 谁维护

GHSA（GitHub Security Advisory）ID 是 GitHub Advisory Database 中每条 advisory 的唯一标识，格式 `GHSA-xxxx-xxxx-xxxx`（字符集去掉了易混淆字符，可用 `/GHSA(-[23456789cfghjmpqrvwx]{4}){3}/` 校验）（Fact，[GitHub Docs](https://docs.github.com/en/code-security/security-advisories/working-with-global-security-advisories-from-the-github-advisory-database/about-the-github-advisory-database)，见 [sources/github-advisory-database.md](01-domain-ontology/sources/github-advisory-database.md)）。

### GHSA 与 CVE 的关系：GHSA 不一定有 CVE

- GHSA ID 在 advisory 创建或导入时**无条件分配**——一个漏洞没有 CVE 也可以有 GHSA（例如维护者在 GitHub 上直接发 advisory、或 CVE 申请还在排队）。
- 多数 GitHub-reviewed advisory 会关联 CVE（OSV 的 `aliases` 字段表达互认，如 GHSA-jfh8-c2jp-5v3q ↔ CVE-2021-44228）。
- GitHub 本身也是 CNA，可以给托管项目直接签发 CVE。

### 数据从哪来：分层策展是核心价值

GitHub Advisory Database 的来源：GitHub 站内报告、NVD、npm、FriendsOfPHP、Go Vulncheck、Python Packaging Advisory DB、RubySec、RustSec、社区 PR。关键分层（Fact）：

- **GitHub-reviewed**：GitHub Security Lab curation team 人工审核有效性、补全生态/包/版本信息；以 OSV 格式 JSON 发布（github/advisory-database 仓库即源头）。
- **Unreviewed**：从 NVD feed 自动导入，**不保证质量**。
- **Dependabot 只对 GitHub-reviewed advisory 告警**——这条产品决策本身就是"策展 > 聚合"的宣言。

Advisory 内容：description、severity 四级、**affected versions 与 patched versions**（修复版本是一等字段）、workarounds、references，且 GitHub 每日同步 FIRST 的 EPSS 分数及 percentile 展示。

### Dependabot 如何使用

Dependency Graph 解析仓库依赖 → 与 GitHub-reviewed advisory 的 ecosystem/package/affected range 匹配 → 产生 Dependabot alert → Dependabot security updates 自动开升级 PR。这是"advisory → 开发者工作流"最短链路的工业样板。

**生命周期位置**：Intelligence + Remediation 触发。**对产品意义**：GHSA 是开源生态中**时效性和版本准确度通常最高**的来源之一，且免费、机器可读、带修复版本；SCA 产品应原生消费 advisory-database 仓库而非仅依赖其 NVD 镜像层。

---

## 7. Vendor Advisory 与五源对比

### 为什么厂商自己的 advisory 常常比 NVD 更准

Vendor Advisory（Microsoft MSRC、Red Hat RHSA、Debian DSA、Ubuntu USN、Apache 项目安全页、Cisco 等）是**发布软件的当事方**对漏洞的一手陈述。它们更准的原因（Interpretation，有 Fact 支撑）：

1. **版本范围以实际发布产物为准**：Debian DSA-5020 针对的是 Debian 打包的 log4j，其修复版本号（含 Debian revision）与上游 Maven 版本号完全不同——只有发行版自己知道"我们 backport 了补丁到哪个包版本"。
2. **backport 信息只有 vendor 知道**：RHEL/Ubuntu 常年把安全补丁 backport 到老版本，版本号不变但漏洞已修——按上游版本号匹配必然误报。
3. **时效**：CNA 发布 CVE 与 vendor advisory 通常同日（Log4Shell 当天 MSRC、Cisco、Debian 全部跟进，见 §2 references），NVD enrichment 则可能滞后数天到永不（2026 政策后）。
4. **上下文**：默认配置是否受影响、哪个组件实际受影响（如 log4j-api vs log4j-core）通常只有 vendor 写得清。

代价是：格式各异（网页/PDF/API/CSAF）、覆盖仅限自家产品、无统一标识——聚合成本高。这正是 CSAF（§12）要解决的。

### 五者对比表

| | CVE（Program/Record） | NVD | OSV | GHSA（GitHub Advisory DB） | Vendor Advisory |
|---|---|---|---|---|---|
| **本质层次** | Identifier + 编目 | Database（增强） | Data Format + 聚合服务 | Database（策展） | Data Source（一手公告） |
| **谁维护** | CVE Program/MITRE + 517 家 CNA | NIST | OpenSSF 规范 + Google 运营 osv.dev | GitHub Security Lab | 各厂商/项目 PSIRT |
| **解决什么** | "同一个漏洞同一个名字" | 美国政府视角的可检索增强库 | 开源漏洞的机器可读交换与聚合 | 开源生态的策展 advisory + 开发者工作流 | 厂商产品的权威影响与修复声明 |
| **组件标识** | vendor/product 字符串 | CPE | ecosystem+name+PURL | 生态坐标 | 厂商自有产品/包名 |
| **CVSS 来源** | CNA 可选；ADP 可补 | NVD Primary + 多来源 | 内嵌向量 | 沿用 maintainer/CVE | 厂商自评 |
| **时效** | 披露即发布 | 2026 起风险优先，有盲区 | 快（源库同步） | 快（reviewed 层策展） | 最快（当事方） |
| **主要短板** | 无评分/无检索/质量异构 | 积压与覆盖断层、CPE 模型老旧 | 仅限开源包 | 生态覆盖有限、unreviewed 层噪声 | 格式不一、聚合难 |

**SCA 组合策略**（Interpretation）：以 CVE ID/GHSA/alias 做实体对齐；**开源依赖匹配以 OSV/GHSA 为主**（坐标精确、带 fixed version），**商业/OS/固件组件以 NVD CPE + vendor advisory 为主**，vendor advisory（优先机器可读 CSAF）做版本范围与修复状态的最终裁决，KEV/EPSS 叠加为优先级信号。

---

## 8. CVSS / EPSS / KEV：三个回答不同问题的优先级信号

### CVSS：度量 severity，不是概率

CVSS（Common Vulnerability Scoring System）由 **FIRST** 拥有和管理，官方定位是 "an open framework for communicating the **characteristics and severity** of software vulnerabilities"（Fact，[CVSS v4.0 规范](https://www.first.org/cvss/v4-0/specification-document)，见 [sources/first-cvss-v40-spec.md](01-domain-ontology/sources/first-cvss-v40-spec.md)）。

**v3.1 vs v4.0**（Fact）：

| | v3.1（2019） | v4.0（2023-11） |
|---|---|---|
| Metric groups | Base / Temporal / Environmental | **Base / Threat / Environmental / Supplemental**（Temporal 改名 Threat，新增 Supplemental） |
| Base 结构 | Exploitability（AV/AC/PR/UI）+ Impact（C/I/A）+ Scope | Exploitability（AV/AC/AT/PR/UI）+ Impact 拆分为 vulnerable system（VC/VI/VA）与 **subsequent system**（SC/SI/SA），含 Safety |
| 标注 | 无强制 | **Nomenclature 强制**：CVSS-B / CVSS-BT / CVSS-BE / CVSS-BTE，标明用了哪些组 |
| 粒度 | 较粗 | 更细（Attack Requirements、Subsequent impacts、Supplemental 的 Automatable/Recovery 等） |

Base/Temporal(Threat)/Environmental 的思想：Base 是漏洞固有属性（跨环境不变）；Threat 随时间变化（PoC 是否公开、是否被 actively exploited）；Environmental 是**你的环境**特有（缓解措施、资产关键性）。规范明确："Threat and Environmental information is available to **only the end consumer**"——公布方（CNA/NVD）通常只给 CVSS-B，**把分数环境化是消费方的责任**。

**为什么 CVSS 9.8 不一定先修**（Interpretation，有规范依据）：

1. CVSS-B 假定"攻击者对目标有先验知识、目标仅默认防护"的最坏情形；你的部署若有关键缓解，Environmental 修正后实际风险可能低得多。
2. CVSS 不含**利用概率**维度。一个 CVSS 9.8 但无人开发 exploit 的漏洞，历史经验上很可能不如一个 CVSS 7.5 但已在勒索软件中使用的漏洞紧迫。
3. 大量 CVE 都是 9.8（Log4Shell 时代尤其），按分数排序无法区分——这就是 EPSS 存在的理由。

### EPSS：度量未来 30 天的利用概率

EPSS（Exploit Prediction Scoring System）由 FIRST 旗下 EPSS SIG 维护，分数由 Empirical Security 生成并免费发布。官方定义："a data-driven **machine-learning model** that estimates the **probability** that a published CVE will be exploited in the wild in the **next 30 days**"（Fact，[first.org/epss](https://www.first.org/epss/)，见 [sources/first-epss.md](01-domain-ontology/sources/first-epss.md)）。每日为每个已发布 CVE 产出 0–1 概率值 + percentile（"比百分之多少的 CVE 更可能被利用"），CSV/API 开放。数据合作方包括 VulnCheck KEV、Shadow Server、LevelBlue 等利用观测源。

**与 CVSS 的本质区别**：CVSS 是**确定性的特征度量公式**（输入向量属性，输出分数，可手工计算）；EPSS 是**经验性的统计预测**（输入全网利用观测、漏洞特征，输出概率，每天会变）。一个回答"最坏能多坏"，一个回答"多可能真的发生"。GitHub Advisory Database 已内嵌 EPSS 分数及 percentile 并每日同步（Fact，GitHub Docs）。

### CISA KEV：已被观测到真实利用的目录

KEV（Known Exploited Vulnerabilities Catalog）由 CISA 维护，截至 2026-09 收录 1713 条。入录门槛：已分配 CVE、**有可靠证据表明在野外被积极利用**、存在明确补救措施。条目含 Date Added、**Due Date**、Required Action、"Known To Be Used in Ransomware Campaigns?"等字段；2026 年起条目行动要求引用 BOD 26-04（早期为 BOD 22-01），对联邦机构是具有约束力的修复期限指令（Fact，[cisa.gov KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)，见 [sources/cisa-kev-catalog.md](01-domain-ontology/sources/cisa-kev-catalog.md)）。

**KEV 与"存在 PoC"的区别**（关键认知）：GitHub 上有 PoC 只说明"理论上可利用、代码公开了"；KEV 要求"**真实攻击者已经在真实目标上用了**"。前者是能力信号，后者是**事实信号**。Log4Shell 在 CVE 发布**当天**（2021-12-10）即入录 KEV，Due Date 2021-12-24——这种速度是 KEV 作为最高优先级信号的直观体现（Fact，见 [sources/nvd-api-20-cve-2021-44228.md](01-domain-ontology/sources/nvd-api-20-cve-2021-44228.md) 的 cisaExploitAdd 字段）。

### 信号链：五种信号回答五个不同的问题

```text
CVSS   → How severe could it be?          （严重性：最坏情况有多坏）
EPSS   → How likely is exploitation?      （可能性：未来 30 天被利用的概率）
KEV    → Has exploitation been observed?  （事实：是否已被真实利用）
Reachability    → Can my software reach it?         （我的代码能否走到漏洞代码，§13）
Exploitability  → Can it be exploited in MY context?（在我的部署上下文能否被利用，§14）
```

**组合使用**（Interpretation）：这五者不冗余、不互相替代，构成从"公共知识"到"私有上下文"的漏斗。一个合理的优先级模型：KEV 命中 = 立即行动（且触发 CRA Article 14 的 24h 时钟评估）；EPSS 高 percentile + CVSS 高 = 本周期修复；Reachability/Exploitability 分析结果用于把"理论高危但不可达"的告警降级，并为 VEX not_affected 提供证据。单靠任何一个信号做排序，都会系统性误排。

**生命周期位置**：Prioritize。**对产品意义**：这三个公共信号是"免费午餐"，产品应自动聚合；真正的差异化在后两个私有信号——它们需要分析客户自己的代码与部署，是传统 SCA 做不到、CRA 时代必须做的部分。

---

## 9. Package Identity：CPE vs PURL——漏洞关联的根基

SCA 的一切始于一个看似简单的问题：**"我扫描出来的组件"和"漏洞数据库里的组件"是不是同一个东西？** 这是 Vulnerability Association 的根基，也是误报/漏报的最大来源。

### CPE：为"产品清点"设计的字典

CPE（Common Platform Enumeration）是 NIST 体系的平台/产品命名标准（2.3 版为 NIST IR 7695）。NVD 用 CPE 2.3 的 formatted string 标识受影响产品，真实样例（Fact，来自 CVE-2021-44228 的 NVD configurations）：

```text
cpe:2.3:o:siemens:6bk1602-0aa12-0tp0_firmware:*:*:*:*:*:*:*:*
       │  │ │       │                                  │
       │  │ │       │                                  └─ version 等后续字段（update/edition/language/...）
       │  │ │       └─ product
       │  │ └─ vendor
       │  └─ part: a=application, o=OS, h=hardware
       └─ CPE 2.3
```

NVD 用 CPE 的原因：它需要一个**跨越所有软件种类的统一产品字典**（应用、操作系统、硬件、固件），才能支撑政府级的资产清点与漏洞匹配（CPE 出身是 SCAP/资产盘点体系）。

**误匹配问题**（Interpretation，业界共识）：CPE 字典里的 vendor/product 名由 NVD 分析师手工指定，与包管理器坐标**没有系统性对应关系**。SCA 工具要匹配就得猜测"`org.apache.logging.log4j:log4j-core` ≈ `cpe:2.3:a:apache:log4j:*`"——同名不同物（fork、重打包）、同物不同名（vendor 别名、产品改名）、一产品多 CPE、CPE 缺失，都直接转化为误报或漏报。NVD enrichment 收缩后新 CVE 缺 CPE 的问题进一步放大。

### PURL：为"包"设计的 URL

PURL（Package URL）是生态无关的包标识语法："a standard URL-based syntax to identify software packages, **independent from their ecosystem or distribution channel**"（Fact，[packageurl.org](https://www.packageurl.org/docs/purl/introduction)，见 [sources/purl-intro.md](01-domain-ontology/sources/purl-intro.md)）。2025-12-10 获批为 **ECMA-427** 国际标准，正走 ISO 快速通道（Fact）。

```text
pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1?type=jar
 │    │            │                    │          └─ qualifiers（key=value，如 arch、distro）
 │    │            │                    └─ version
 │    │            └─ namespace（Maven groupId）
 │    └─ type（生态：maven/npm/pypi/golang/deb/apk/...，有注册表）
 └─ scheme（固定 pkg:）
```

**为什么更适合现代生态**（Fact + Interpretation）：PURL 的每个 type 直接对齐一个包管理器的原生坐标系——SCA 从 lockfile 里读到的就是它，**匹配是精确的字符串比较而非字典猜测**。配套标准 **VERS**（Version Range Specifier，计划 2026 年提交 Ecma）统一版本区间表达，解决"各生态版本范围记号不一致"问题；PURL 还可用 `vers` qualifier 携带区间。CycloneDX、OpenVEX、OSV、GitHub Advisory DB、各大扫描器都已以 PURL 为一等标识。

### 对漏洞关联准确率的影响

| | CPE | PURL |
|---|---|---|
| 适用对象 | 产品/平台/固件/硬件 | 包管理器生态的包 |
| 与 SCA 输入的天然对齐 | 差（需映射层） | 好（直接相等） |
| 主要风险 | 字典猜测 → 误报/漏报 | 生态外（COTS、固件、系统包）覆盖弱 |
| 权威数据源 | NVD configurations | OSV/GHSA/CycloneDX/OpenVEX |

**产品意义**（Interpretation）：现代 SCA 的正确架构是**双轨身份**：包级组件用 PURL（主匹配轨道），OS/固件/COTS 用 CPE（辅轨道），并在知识图谱中维护 PURL↔CPE 的显式映射关系及置信度——而不是把一方强行翻译成另一方。关联准确率是 SCA 产品的第一质量指标，值得为它建测试集和回归基准。

---

## 10. SBOM：软件的"成分表"，合规时代的通行证

### 为什么出现

SBOM 的政策引爆点是美国 **EO 14028**（2021-05-12）：其 Section 4 指令商务部/NTIA 发布 SBOM 的"minimum elements"，NIST 牵头制定供应链安全标准并约束联邦采购（Fact，[NIST EO 14028 页](https://www.nist.gov/itl/executive-order-14028-improving-nations-cybersecurity)，见 [sources/nist-eo-14028.md](01-domain-ontology/sources/nist-eo-14028.md)）。NTIA 于 2021-07-12 发布报告，定义 SBOM 为 "a **formal record** containing the details and **supply chain relationships** of various components used in building software"（Fact，[NTIA](https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom)，见 [sources/ntia-sbom-minimum-elements.md](01-domain-ontology/sources/ntia-sbom-minimum-elements.md)）。深层动因是 SolarWinds（2020）与 Log4Shell（2021）暴露的现实：**大多数组织答不上"我的软件里到底有什么"**——Log4Shell 应急响应的第一周，大量企业的时间花在找 log4j 而不是修 log4j。欧盟 CRA 随后把 SBOM 纳入 Annex I 基本安全要求体系（2027-12-11 全面适用）（Fact，见 [sources/cra-regulation-2024-2847.md](01-domain-ontology/sources/cra-regulation-2024-2847.md)）。

### 一个 SBOM 到底包含什么

按 NTIA 最小要素 + 主流标准实践：每个 component 的 **名称、版本、唯一标识（PURL/CPE/hash）、supplier、license、依赖关系（direct/transitive、dependency graph）**；文档级的作者、时间戳、工具信息。小型 CycloneDX 示例（Format: CycloneDX，字段结构 Fact 依据 [cyclonedx.org](https://cyclonedx.org/specification/overview/)）：

```json
{
  "bomFormat": "CycloneDX", "specVersion": "1.6",
  "metadata": {
    "timestamp": "2026-09-18T08:00:00Z",
    "tools": [{"name": "my-sca-tool", "version": "1.0"}],
    "component": {"type": "application", "name": "payment-service", "version": "3.2.0"}
  },
  "components": [
    {"type": "library", "group": "org.apache.logging.log4j", "name": "log4j-core",
     "version": "2.14.1", "purl": "pkg:maven/org.apache.logging.log4j/log4j-core@2.14.1",
     "hashes": [{"alg": "SHA-256", "content": "abc123..."}],
     "licenses": [{"license": {"id": "Apache-2.0"}}],
     "supplier": {"name": "Apache Software Foundation"}, "bom-ref": "cmp-1"}
  ],
  "dependencies": [
    {"ref": "payment-service-3.2.0", "dependsOn": ["cmp-1"]}
  ]
}
```

### SPDX vs CycloneDX：按场景而非优劣

| | SPDX | CycloneDX |
|---|---|---|
| **维护方** | Linux Foundation | OWASP Foundation |
| **起源动机** | **License compliance**（开源许可证清单与表达）；SPDX License List 至今是使用最广的部分（Fact，[spdx.dev](https://spdx.dev/learn/overview/)） | **安全导向**的 SBOM（2017 年起于 OWASP），对象模型为漏洞管理、服务依赖、密码学透明度设计（Fact，[cyclonedx.org](https://cyclonedx.org/specification/overview/)） |
| **标准化** | 2.2.1 即 **ISO/IEC 5962:2021**；3.0 扩展到 AI/数据集/构建信息，序列化转向 JSON-LD/RDF | IANA 注册媒体类型（`application/vnd.cyclonedx+json/xml`，protobuf）；版本化演进快（1.6/1.7） |
| **安全能力** | 3.0 起集成漏洞数据引用，但非原生强项 | **原生内嵌 `vulnerabilities[]`**（含 VEX 语义）、services、compositions（完整性声明）、declarations（compliance-as-code、可签名） |
| **典型场景** | 许可证审计、法务合规、ISO 采信场景、开源治理 | 安全运营、漏洞/VEX 交换、CRA 证据、供应链安全工具链 |

（Interpretation）不是二选一：很多企业 SPDX 用于 license/法务链路，CycloneDX 用于安全链路，两者有官方/社区转换工具。NTIA 最小要素对两种格式都认可。

### SBOM ≠ SCA

（Interpretation，依据 NTIA 定义的 Fact）**SBOM 是"记录"，SCA 是"分析"**：

```text
Source Code / Binary / Lockfile
     │  被分析（identification、解析、指纹）
     ▼
   SCA 引擎 ──→ Component Inventory（内部数据）
     │  被导出为
     ▼
   SBOM（标准化的交换文档）
```

- SBOM 是 SCA 结果的**一种序列化产物**；SBOM 也可以由构建系统、手工、供应商直接产出，不经过 SCA。
- SBOM 本身**不含漏洞信息**（CycloneDX 的 vulnerabilities 是可选扩展）；"给你一份 SBOM"不等于"告诉你哪里有风险"——漏洞结论需要 SBOM × 漏洞情报的关联计算。
- 反向也成立：SCA 的内部清单比 SBOM 更丰富（文件级证据、检测置信度、license 文本匹配位置等），导出 SBOM 是有损投影。

**生命周期位置**：Inventory。**对产品意义**：SBOM 生成已是商品化能力；差异化在于 SBOM 的**准确性**（传递依赖、二进制组件、重打包识别）、**新鲜度**（每次构建重新生成）以及它作为下游关联/VEX/证据计算输入的**可信度**。

---

## 11. VEX：从"含有漏洞组件"到"我的产品是否受影响"的正式判断

### 为什么出现：SBOM 回答不了的问题

```text
SBOM 说：Product A 包含 log4j-core 2.14.1
NVD 说：log4j-core 2.14.1 受 CVE-2021-44228 影响
问题：Product A 真的受这个漏洞影响吗？
```

SBOM 本身回答不了——它只说成分，不说可达性与可利用性。于是扫描器产生海量"成分级"告警，其中大量是误报（组件已打补丁、漏洞代码不存在、不可执行、不可被攻击者控制）。OpenVEX 规范原文直陈动机："software is not necessarily affected as signaled by security scanners … The extreme transparency brought by SBOMs will most likely increase the number of these kind of false positives, requiring an automated solution … **Hence VEX**"（Fact，[OpenVEX spec](https://raw.githubusercontent.com/openvex/spec/main/OPENVEX-SPEC.md)，见 [sources/openvex-spec-v020.md](01-domain-ontology/sources/openvex-spec-v020.md)）。

VEX（Vulnerability Exploitability eXchange）的官方定义："a vulnerability document designed to **complement a SBOM** that informs users of a software product about the **applicability** of one or more vulnerability findings"（Fact，OpenVEX spec 引 CISA VEX 工作组定义）。最小要素由 CISA《Minimum Requirements for VEX》（2023-04）定义。

### 核心模型：statement = product + vulnerability + status + timestamp

（Fact，OpenVEX v0.2.0）VEX 的基本单位是 **statement**：对"某产品 × 某漏洞"在**某个时间点**的判断声明。VEX 文档是 statement 的序列，**同对象的后续 statement 覆盖前者**——status 可以随认知演进：

```text
T1: under_investigation（看到 CVE 了，正在查）
T2: affected（确认受影响，附 action_statement：缓解措施）
T3: fixed（已修复）
```

四个 status label（CISA 工作组统一定义）：

| Status | 含义 | 附加要求 |
|---|---|---|
| `affected` | 受影响，建议采取行动 | **必须**带 `action_statement`（怎么修/缓解） |
| `not_affected` | 不受影响，无需行动 | **必须**带机器可读 `justification` 或 `impact_statement` |
| `fixed` | 该产品版本已含修复 | — |
| `under_investigation` | 尚不确定，后续更新 | — |

### not_affected 为什么必须有 justification

"不受影响"是一个**强断言**，消费方要据此关闭告警——没有理由的 not_affected 等于让别人盲信供应商。因此 CISA《VEX Status Justifications》（2022-07）定义了五个机器可读标签（Fact，OpenVEX spec 收录全文）：

| Justification | 含义 | 对应的分析证据 |
|---|---|---|
| `component_not_present` | 组件根本不在产品中 | SBOM/成分分析 |
| `vulnerable_code_not_present` | 组件在但漏洞代码不在（构建裁剪等） | 二进制/源码级分析 |
| `vulnerable_code_not_in_execute_path` | 漏洞代码在产品使用方式下**不可达** | **Reachability 分析（§13）** |
| `vulnerable_code_cannot_be_controlled_by_adversary` | 攻击者无法控制漏洞代码的输入 | **Exploitability 分析（§14）** |
| `inline_mitigations_already_exist` | 内置防护完全阻止利用 | 防护机制验证 |

规范同时警告后两者"could be difficult to prove conclusively"——这正是把它们做成**证据驱动的产品能力**（而非人工下拉框）的价值所在（Interpretation）。

真实示例（Fact，OpenVEX spec 附录）：Spring Boot 2.6.0-M3 含受影响范围内的 log4j 依赖，但项目方可发布：

```json
{"status": "not_affected",
 "justification": "vulnerable_code_not_in_execute_path",
 "impact_statement": "The log4j-to-slf4j and log4j-api jars that we include ... cannot be exploited on their own. Only applications using log4j-core and including user input in log messages are vulnerable."}
```

### 三种实现及关系：VEX 是判断结果，不是文件格式

**VEX 本身是 CISA 工作组定义的"最小数据集/判断模型"**——一种语义约定；它有三个主流序列化实现（Fact）：

| 实现 | 载体 | 特点 |
|---|---|---|
| **CycloneDX VEX** | CycloneDX BOM 的 `vulnerabilities[]`（可独立成文） | 与 SBOM 同格式，analysis.state/justification 内嵌；标签集与 CISA 定义**有出入**，需翻译（OpenVEX 官方指出） |
| **CSAF VEX Profile** | CSAF 文档（Profile 5） | OASIS 标准通道；product tree 表达力最强，适合厂商发布正式 advisory（§12） |
| **OpenVEX** | 独立 JSON-LD 文档 | 最小化、SBOM 无关、PURL 为一等标识、易嵌入 in-toto attestation / Sigstore 签名；规范仍为 draft |

三者表达同一组语义（status + justification + product + vulnerability + timestamp），工具链（如 OpenVEX 的 vexctl/go-vex）支持互相转换合并、生成完整 impact 历史。所以回答那个关键问题：**VEX 是"漏洞判断结果"的语义模型，文件格式只是它的承载方式**；产品应该把 VEX statement 当作数据库里的一等对象（可版本化、可追溯、可签名），导出格式是适配层（Interpretation）。

### 产品视角：VEX 是分析流水线的终点也是合规证据的起点

```text
Reachability + Exploitability + Runtime Context + 专家/Agent 裁决
     ↓
VEX statement（附证据引用：call graph、配置快照、测试记录）
     ↓
对消费者：扫描器按 status 收敛告警
对监管：CRA 下的漏洞处置证明（"为什么这个 CVE 不修"的正式答案）
```

这个模型完全合理，且就是 VEX 设计的本意（Interpretation）：justification 标签与 Reachability/Exploitability 分析结论一一对应。产品的核心壁垒在于**让每个 not_affected 都有可审计的机器证据链**，而不是让人拍脑袋选标签——这正是 CRA 时代"证明你履行了漏洞管理义务"的落点。

**生命周期位置**：Assess/Decide + Communicate。

---

## 12. CSAF：机器可读的 Security Advisory 标准

### 是什么 / 谁维护

CSAF（Common Security Advisory Framework）2.0 是 **OASIS** 标准（2022-11-18 批准，TC 主席来自 Cisco，编辑来自 Red Hat、德国 BSI），取代 XML 时代的 CVRF 1.2。官方定位："the definitive reference for the language which supports creation, update, and interoperable exchange of **security advisories as structured information** on products, vulnerabilities and the status of impact and remediation"（Fact，[OASIS CSAF 2.0](https://docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html)，见 [sources/csaf-v20-oasis-standard.md](01-domain-ontology/sources/csaf-v20-oasis-standard.md)）。

### 为什么需要机器可读 / 与 PDF 公告的区别

传统 vendor advisory 是给人读的网页/PDF：版本范围藏在散文里，无法自动化消费。CSAF 把 advisory 变成 JSON 文档 + JSON Schema 校验 + 明确的分发生态（**CSAF provider** 发布、**aggregator** 聚合、**viewer** 消费），使"订阅所有供应商的 advisory 并自动匹配我的资产"成为可能。它强制结构化字段：`/document`（tracking、revision history、distribution）、`/product_tree`（产品家族/分支/版本树）、`/vulnerabilities[]`（CVE、CWE、scores、**remediations**、product status）。

### Profile 体系与 VEX Profile

CSAF 定义 5 个 profile（Fact）：1 CSAF Base、2 Security incident response、3 Informational Advisory、4 **Security Advisory**（标准漏洞公告）、5 **VEX**。Profile 5 要求：`/product_tree` 列出全部被引用产品 + `/vulnerabilities` + 至少一个 product status 组——即"在完整 advisory 文档框架内表达 VEX 判断"。与 OpenVEX 的关系：CSAF VEX 更重（完整文档框架、product tree），OpenVEX 更轻（statement 为中心、PURL 标识、易签名嵌入）；CSAF 规范自己引用了 NTIA/CISA 的 VEX 定义文档，三者语义同源。

### 与 CRA 漏洞披露义务的关系

（Interpretation，时间点为 Fact）CRA Article 14 自 2026-09-11 起要求制造商就 actively exploited vulnerability 在 24h/72h 内向 ENISA SRP 与协调 CSIRT 报告；Article 13 及配套体系要求制造商建立协调披露政策、向用户通报风险与修复。当披露义务进入"小时级"时钟，**手工写 PDF 公告的模式在操作上是不可持续的**；CSAF（含其 VEX profile）是目前唯一国际标准化、且已被主要厂商（Microsoft、Red Hat、Cisco、Siemens、Oracle 等）实际采用的机器可读 advisory 通道。对下游：消费 CSAF feed 是获取 vendor 一手影响判断的最佳自动化途径。

**生命周期位置**：Communicate/Disclose。**对产品意义**：SCA/合规平台应同时是 CSAF 的**消费者**（聚合 vendor advisory 做多源裁决）和潜在**生产者**（帮客户生成自己的 advisory/VEX 输出）。

---

## 13. Reachability：漏洞代码"走不走得到"

### 从 Presence 讲起

传统 SCA 做的是 **Presence Analysis**：依赖树里有 `log4j-core@2.14.1` → 告警。它只能证明"vulnerable component exists"。但组件存在 ≠ 漏洞会被触发——你可能只调用了这个库里完全不相干的类。Reachability 要回答的是调用路径是否存在：

```text
Application entrypoint → foo() → bar() → JndiLookup.lookup()  ← 存在这条路径才可被触发
```

### 层次谱系

由粗到细（Interpretation 的行业通用划分）：

| 层次 | 判定内容 | 典型技术 | 精度/成本 |
|---|---|---|---|
| Package reachability | 依赖是否被打进产物/被 import | 依赖解析、构建产物分析 | 低精度低成本 |
| Module/Class reachability | 含漏洞的模块/类是否被加载或引用 | import 分析、类加载图 | ↑ |
| Symbol/Function reachability | 漏洞函数是否被调用 | 静态 call graph | ↑ |
| Call Path reachability | 从入口到漏洞函数的完整路径是否存在 | call graph 路径可达性、CHA/PTA | ↑ |
| Vulnerable Branch reachability | 路径能否走到函数内**触发漏洞的具体分支**（特定参数/条件） | CFG + 数据流/污点分析 | ↑ |
| Runtime reachability | 真实运行中是否被执行到 | 运行时探针、eBPF、覆盖率遥测 | 最接近事实，需部署插桩 |

语言差异显著（Interpretation）：Java/Go/Rust 的静态调用图相对可行；JavaScript/Python 的动态特性使静态分析欠近似严重；C/C++ 需要 compilation database 且函数指针/虚调用使精度受限。这也是为什么" Reachability 支持哪些语言到什么深度"是 SCA 产品的真实分水岭。

### 为什么能降误报；为什么 Reachable ≠ Exploitable

VEX 的 justification `vulnerable_code_not_in_execute_path` 就是 reachability 结论的官方语义出口——有了不可达证据，not_affected 才立得住（Fact 关联，§11）。但反过来必须克制：**可达只说明"代码能走到"，不说明"攻击者能控制走到这里时的输入"**。漏洞函数被执行，但参数全部来自内部常量，仍然不可利用。把 Reachable 当成 Exploitable 是新一代 SCA 营销中常见的过度承诺（Interpretation）。

**生命周期位置**：Analyze（Association 之后）。**对产品意义**：Reachability 是把 SCA 告警量降一到两个数量级的最现实杠杆，也是 VEX not_affected 的主要证据源；其实现深度（语言覆盖、分支级精度、运行时验证）构成技术壁垒。

---

## 14. Exploitability：在我的上下文里"能不能真被打"

### 判定链条

```text
Present（组件存在）
  → Affected（我的版本落在受影响区间内）
    → Reachable（漏洞代码可达）
      → Input Controllable（攻击者能控制到达漏洞点的输入）
        → Precondition Satisfied（漏洞触发的前置条件成立）
          → Exploitable（在此部署上下文中可利用）
```

每一层都可能断链。典型影响因素（Interpretation，对照 VEX justification 与 CVSS Environmental 思想）：

- **Network exposure**：服务是否监听公网/可被攻击者触达的网段；
- **Authentication/Authorization**：触发路径是否需要认证、什么权限；
- **Attacker-controlled input**：污点分析能否证明外部输入到达漏洞点（Log4Shell 的关键就是"用户输入是否进日志"）；
- **Runtime configuration / feature flags**：漏洞功能是否启用（如 JNDI lookup 在 2.15.0+ 默认关闭；某 feature flag 默认关）；
- **Privilege / sandbox / mitigations**：进程权限、沙箱、ASLR/CFG 等缓解是否使利用失效；
- **Operating environment**：OS、容器、编排策略。

### 与 CVSS / EPSS / KEV / Reachability 的区别

（Interpretation，有规范依据）**四者都是"外部公共信号"，Exploitability 是"内部私有结论"**：

- CVSS-B 明确假定最坏环境、声明环境化是消费方责任——它**故意不回答**你的上下文问题；
- EPSS/KEV 描述"全世界"的利用情况，不知道你的部署；
- Reachability 只看代码结构，不看输入来源与运行环境；
- Exploitability 是以上一切在你具体产品/版本/配置/部署下的**合取判断**。

**生命周期位置**：Decide（VEX 之前最后的分析层）。**对产品意义**：这是告警噪声治理的终局能力，也是 CRA 下"基于风险的漏洞处置"主张能否成立的证据基础；现实产品是"静态可达性 + 部署/配置上下文 + 威胁情报"的组合裁决，并把结论固化为 VEX statement。完全的自动 Exploitability 判定在多数语言/框架下仍是研究级难题——诚实的定位是"证据聚合 + 半自动裁决"，而非全自动定论（Interpretation）。

---

## 15. 修复概念：Fix 不是一个词能说清的事

| 概念 | 含义 | 关键点 |
|---|---|---|
| **Fix Commit** | 上游修复漏洞的具体提交 | 漏洞级最精确的"修复事实"；可做 patch 存在性检测与 commit 级受影响分析（OSV GIT range 的基础） |
| **Fix Version / Patched Version** | 首个包含修复的发布版本 | GHSA/OSV advisory 的一等字段；SCA 升级建议的来源 |
| **Patch** | 修复的代码变更本身 | 可独立于版本发布存在（如临时补丁） |
| **Backport** | 把修复移植到旧维护分支 | Log4Shell 的 2.12.2/2.12.3/2.3.1 就是 backport 安全版本（Fact，§5 数据）；"版本号老 ≠ 没修" |
| **Workaround** | 不改代码的临时规避（改配置、删类、加 WAF 规则） | 如 Log4Shell 的移除 JndiLookup 类；不消除漏洞本身 |
| **Mitigation** | 降低可利用性或影响的措施 | 不消除根因；可被绕过（CISA 对 inline_mitigations 的警告） |
| **Remediation** | 彻底消除漏洞的处置（升级/打补丁/移除组件） | KEV 条目 required action 的语义层次 |
| **Upgrade / Dependency Update** | 升级依赖到修复版本 | 依赖场景的主要 remediation 手段 |
| **Breaking Change** | 升级引入的不兼容变更 | 修复的真实成本所在；决定"能不能升" |
| **Verification** | 证明修复确实生效 | 重扫、回归测试、利用复现失败、运行时确认 |

**最重要的区分**（Interpretation）：

```text
Mitigation（风险变小了）≠ Remediation（根因消除了）≠ Fix（代码改了）
Fixed upstream（上游修了）≠ Fixed in dependency（你依赖的版本修了）
  ≠ Fixed in my product（你的产品实际升级并发布了）≠ Fix verified（验证过修好了）
```

每一环都可能断裂：上游发布了 2.17.0 修好，但你的产品钉在 2.14.1；你升了版本但 shaded jar 里还藏着旧的；部署了但没验证。CRA 语境下，"修好了吗"需要的是**可出示的证据**（新 SBOM、重扫记录、VEX status 流转到 fixed），不是 CI 绿灯。

**生命周期位置**：Remediate + Verify。**对产品意义**：remediation 引擎的核心数据就是 fix commit ↔ fix version ↔ backport 版本 ↔ 发行版包版本的映射表（多源 advisory 融合的最大价值点之一），再加兼容性分析（breaking change 检测）决定"自动升还是人工修"。

---

## 16. 漏洞披露体系：一个 CVE 的诞生之旅

### 角色词汇

- **Vulnerability Disclosure**：把漏洞信息公开的行为总称。
- **Coordinated Vulnerability Disclosure（CVD，旧称 Responsible Disclosure）**：研究者与厂商协调，先修复后公开的披露模式（ISO/IEC 29147/30111 标准化）。
- **PSIRT**（Product Security Incident Response Team）：厂商侧接收、分流、处置漏洞报告的专职团队。
- **CNA**：签发 CVE ID 并发布 Record 的授权组织（§2）。

### 理想流程与现实变体

```text
Researcher 发现 → 报告给 Vendor/PSIRT（或 CNA、CERT/CC）
  → Triage（确认、定级、定范围）
  → CNA 预留 CVE ID（dateReserved）
  → 开发 Patch + 准备 Advisory
  → 协调披露日：CVE Record 发布（datePublished）+ Patch/Advisory 上线
  → NVD enrichment / OSV 收录 / GHSA 策展
  → 下游 SCA/扫描器/合规平台消费
```

CVE-2021-44228 的时间线完美印证：reserved 2021-11-26 → 阿里云 Chen Zhaojun 报告 → 协调披露 2021-12-10，同日进 KEV（Fact，§2/§8）。但现实变体极多（Interpretation）：研究者直接公开（full disclosure）倒逼流程；厂商自己发现内部漏洞走 CNA 直发；漏洞先在 GHSA/OSV 出现、CVE 后补；CNA 覆盖真空由 CNA-LR 兜底；厂商拖延导致 0day 窗口。**对产品的含义：漏洞情报管道不能只挂"CVE 发布"这一个钩子，必须同时监听 vendor advisory、OSV feed、GHSA、KEV、邮件列表与 exploit 源。**

### CRA 接入点

（Fact：时间点；Interpretation：流程映射）CRA 把披露体系变成法定义务：制造商须建立协调披露政策（接收外部报告的通道，类 PSIRT 职能）；发现 **actively exploited vulnerability** 或 severe incident 时，24h early warning → 72h notification → 14 天（漏洞）/1 个月（事件）final report，经 ENISA SRP 并行通报协调 CSIRT（Article 14，2026-09-11 起适用）。这把上图的"披露"环节从最佳实践变成了带时钟的法律流程——**情报管道发现 KEV 命中/活跃利用迹象的那一刻，就应当触发报告时钟评估工作流**，这是合规产品的直接功能点。

---

## 17. 标准与组织总表

| 名称 | 类型（层次） | 维护组织 | 解决的问题 | 生命周期位置 |
|---|---|---|---|---|
| CVE | Identifier / 编目系统 | CVE Program（MITRE 运营，CISA 资助，517 家 CNA 联邦签发） | 漏洞统一标识与编目 | Discover/Disclose |
| CWE | Taxonomy | MITRE（社区共建） | 弱点分类、横向聚合 | Analyze |
| NVD | Database（enrichment） | NIST | CVE 的结构化增强（CPE/CVSS/CWE/References） | Intelligence |
| CVSS | Scoring System（severity） | FIRST | 严重性度量与沟通（v4.0: Base/Threat/Env/Suppl） | Prioritize |
| EPSS | Scoring/Prediction（likelihood） | FIRST EPSS SIG（Empirical Security 生成） | 30 天利用概率预测 | Prioritize |
| KEV | Threat Intelligence Catalog | CISA | 已观测利用的事实清单 + 联邦修复时限 | Prioritize |
| CPE | Identifier（产品字典） | NIST | OS/固件/COTS 统一产品标识（SCAP 体系） | Association |
| PURL / VERS | Identifier / 版本区间语法 | package-url 社区 / Ecma（**ECMA-427**，ISO 快速通道中） | 生态原生包标识与版本区间 | Association |
| OSV | Data Format + 聚合服务 | OpenSSF（规范）/ Google（osv.dev） | 开源漏洞的机器可读交换与聚合 | Intelligence |
| GHSA | Identifier + Database | GitHub（Security Lab 策展） | 开源 advisory 策展 + 开发者工作流 | Intelligence |
| SBOM（概念） | Compliance Artifact | 多标准（NTIA 定义最小要素，EO 14028 引爆） | "软件里有什么"的正式记录 | Inventory |
| SPDX | Data Format / Standard | Linux Foundation（2.2.1 = ISO/IEC 5962） | license 合规起源的 BOM 交换 | Inventory |
| CycloneDX | Data Format / Standard | OWASP | 安全导向 BOM，内嵌 vulnerabilities/VEX | Inventory/Assess |
| VEX（模型） | Analysis Result 语义模型 | CISA VEX 工作组（最小要素 2023） | "我的产品是否受影响"的正式判断 | Assess/Decide |
| OpenVEX | Data Format（VEX 实现） | OpenVEX 社区（OpenSSF） | 轻量、SBOM 无关、可签名的 VEX 交换 | Assess/Communicate |
| CSAF | Data Format / Standard（含 VEX Profile） | OASIS | 机器可读 security advisory 与分发 | Communicate/Disclose |
| SSDF（SP 800-218） | 开发流程框架 | NIST | 安全开发实践共同语言（EO 14028 交付物） | Build/Prevent |
| SLSA | 供应链完整性框架 | OpenSSF | 构建/分发防篡改与 provenance 分级 | Build/Provenance |
| OpenSSF | 组织（非标准） | Linux Foundation | 开源安全生态的伞组织（OSV/SLSA/OpenVEX/scorecard 等） | 全周期 |
| EO 14028 / CRA | 法规 | 美国政府 / 欧盟 | 把上述实践变为采购/市场准入要求 | Compliance |

（补充说明：OpenSSF 是组织而非标准，列入表中是因为它在生态定位中极易被误当作标准；SWID tag 是 NTIA 认可的第三种 SBOM 格式但生态份额很小，（不确定）当前活跃度低。）

---

## 18. Mental Model：一条故事线串起整个领域

不要记缩写，记这条故事线。每一层标注 **Concept → Standard → Data Source → Tool → Product Capability**：

```text
1. 我有什么软件？
   Product Inventory → （内部模型）→ CMDB/代码仓/制品库 → 产品注册 → Product/Version 管理

2. 软件里有什么？
   SBOM → SPDX / CycloneDX → 构建时/扫描时生成 → Syft、cdxgen、SCA 引擎 → 成分清单能力
   （CRA Annex I 要求；EO 14028 溯源）

3. 这些组件是谁？
   Package Identity → PURL（ECMA-427）/ CPE → 包元数据 + NVD CPE 字典 → 识别与归一化引擎 → 组件识别准确率

4. 世界上有哪些漏洞？
   CVE → CVE Record Format 5.x → CNA 发布 + NVD + OSV + GHSA + Vendor Advisory → 多源情报管道 → 漏洞情报库
   （NVD 2026 起风险优先，多源融合是刚需）

5. 漏洞严重吗？
   CVSS → v4.0（FIRST）→ NVD/CNA/ADP 评分 → 评分聚合 → severity 视图
   （记住：severity ≠ probability）

6. 现实中会被攻击吗？
   EPSS / KEV / TI → FIRST EPSS、CISA KEV → 每日 feed → 威胁情报聚合 → 优先级引擎
   （KEV 命中 = 触发 CRA Article 14 时钟评估）

7. 这个漏洞和我有关吗？
   Vulnerability Association → PURL/CPE 匹配 + 版本区间（VERS/OSV range）→ OSV/NVD/GHSA → 关联引擎 → 告警生成
   （误报/漏报的第一发源地）

8. 漏洞代码真的能走到吗？
   Reachability → （无标准，产品级技术）→ 调用图/污点/运行时遥测 → 静态+动态分析引擎 → 可达性判定
   （justification: vulnerable_code_not_in_execute_path 的证据源）

9. 我的环境里能利用吗？
   Exploitability → （无标准，产品级技术）→ 部署/配置/输入可控性/缓解措施 → 上下文分析 + 专家/Agent 裁决 → 可利用性结论

10. 我对这个漏洞的正式判断是什么？
    VEX → CISA 最小要素；OpenVEX / CycloneDX VEX / CSAF VEX Profile → statement 管理 → VEX 工作台 → 可审计的漏洞裁决
    （not_affected 必须带 justification 和证据）

11. 怎么修？
    Remediation → advisory 的 fixed version / fix commit / backport 映射 → GHSA/OSV/vendor advisory → 升级建议、自动 PR、兼容性分析 → 修复引擎

12. 真的修好了吗？
    Verification → （内部流程）→ 重扫 + 回归 + 利用复现 → CI/CD 集成 → 修复验证 + SBOM/VEX 自动更新（status → fixed）

13. 怎么告诉客户/上下游/监管？
    Security Advisory → CSAF（OASIS）→ vendor feed / ENISA SRP → advisory 生成与发布 → 通报能力
    （CRA Article 14: 24h / 72h / 14d 时钟）

14. 怎么证明整个过程？
    Evidence / Audit Trail → （VEX 版本历史 + SBOM 存档 + 签名 attestation）→ 证据存储 → 证据图谱 → CRA 合规档案

CRA 要求我承担什么责任？→ 以上每一环的闭环与留痕。
```

**给读者的最后三句话**（Interpretation）：

1. 这个领域的数据流本质是"**公共知识（CVE/NVD/OSV/GHSA/CVSS/EPSS/KEV）× 私有上下文（SBOM/代码/部署）→ 私有结论（Association/Reachability/Exploitability/VEX）→ 公共输出（Advisory/CRA 报告）**"。
2. 传统 SCA 只做到第 7 步；第 8–10 步（Reachability/Exploitability/VEX）是当前产品竞争的主战场；第 12–14 步（Verification/Advisory/Evidence）是 CRA 把"做了"变成"证明了"之后的新刚需。
3. 任何单一数据源都不可靠：NVD 有官方盲区、CVE 不带分数、GHSA 只覆盖开源、vendor advisory 格式散乱——**多源融合 + 证据链**是这个领域产品的立身之本。

---

## 附录：来源索引

所有一手来源的详细摘录见 [docs/research/01-domain-ontology/sources/](01-domain-ontology/sources/)：

| Source Note | 支撑章节 |
|---|---|
| [cve-record-api-cve-2021-44228.md](01-domain-ontology/sources/cve-record-api-cve-2021-44228.md) | §2, §4, §8, §16 |
| [cve-program-overview.md](01-domain-ontology/sources/cve-program-overview.md) / [cve-program-cna.md](01-domain-ontology/sources/cve-program-cna.md) | §2, §16 |
| [cwe-about.md](01-domain-ontology/sources/cwe-about.md) | §3 |
| [nvd-api-20-cve-2021-44228.md](01-domain-ontology/sources/nvd-api-20-cve-2021-44228.md) / [nvd-api-developers.md](01-domain-ontology/sources/nvd-api-developers.md) | §4, §9 |
| [nist-nvd-operations-2026.md](01-domain-ontology/sources/nist-nvd-operations-2026.md) | §4 |
| [osv-schema-spec.md](01-domain-ontology/sources/osv-schema-spec.md) / [osv-api-ghsa-log4shell.md](01-domain-ontology/sources/osv-api-ghsa-log4shell.md) | §5, §15 |
| [github-advisory-database.md](01-domain-ontology/sources/github-advisory-database.md) | §6 |
| [first-cvss-v40-spec.md](01-domain-ontology/sources/first-cvss-v40-spec.md) / [first-epss.md](01-domain-ontology/sources/first-epss.md) / [cisa-kev-catalog.md](01-domain-ontology/sources/cisa-kev-catalog.md) | §8 |
| [purl-intro.md](01-domain-ontology/sources/purl-intro.md) / [purl-spec-location.md](01-domain-ontology/sources/purl-spec-location.md) | §9 |
| [ntia-sbom-minimum-elements.md](01-domain-ontology/sources/ntia-sbom-minimum-elements.md) / [nist-eo-14028.md](01-domain-ontology/sources/nist-eo-14028.md) | §10 |
| [spdx-overview.md](01-domain-ontology/sources/spdx-overview.md) / [cyclonedx-overview.md](01-domain-ontology/sources/cyclonedx-overview.md) | §10, §11 |
| [openvex-spec.md](01-domain-ontology/sources/openvex-spec.md) / [openvex-spec-v020.md](01-domain-ontology/sources/openvex-spec-v020.md) | §11, §13 |
| [csaf-v20-oasis-standard.md](01-domain-ontology/sources/csaf-v20-oasis-standard.md) | §11, §12 |
| [cra-regulation-2024-2847.md](01-domain-ontology/sources/cra-regulation-2024-2847.md) | §0, §10, §12, §16 |
| [ssdf-sp800-218.md](01-domain-ontology/sources/ssdf-sp800-218.md) / [slsa-dev.md](01-domain-ontology/sources/slsa-dev.md) | §17 |

研究过程记录：[docs/research/01-domain-ontology/research-log.md](01-domain-ontology/research-log.md)（含弃用来源与来源间冲突说明）。
