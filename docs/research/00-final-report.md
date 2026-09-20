# 00 — 最终汇总研究报告：CRA + SCA 漏洞全生命周期产品

> **汇总日期**：2026-09-18 | **汇总对象**：四份分报告的浓缩、交叉核对与决策化重写
>
> **分报告**（均为本报告的事实基础，本文引用时简写为"01/02/03/04 报告 §x"）：
>
> 1. `docs/research/01-domain-ontology.md` — 领域知识体系（CVE/CWE/NVD/OSV/GHSA/CVSS/EPSS/KEV/CPE/PURL/SBOM/VEX/CSAF/Reachability/Exploitability/修复/披露）
> 2. `docs/research/02-cra-regulation.md` — CRA Regulation (EU) 2024/2847 法规研究（13 组必答问题 + 46 行义务映射表）
> 3. `docs/research/03-competitive-landscape.md` — 21 家厂商竞争格局
> 4. `docs/research/04-technology-deep-dive.md` — Reachability / Exploitability / Evidence Graph / Agentic 技术深挖
>
> **关键时间背景**（Fact）：CRA **Article 14 漏洞/事件报告义务已于 2026-09-11（7 天前）起适用**，ENISA Single Reporting Platform（SRP）同日上线；主体义务（Annex I、Art 13 等）**2027-12-11** 全面适用。
>
> **标注约定**：**（Fact）**= 有一手来源支撑；**（Interpretation）**= 基于事实的推理；**（Hypothesis）**= 待验证假设；**（Recommendation）**= 行动建议。引用格式："见 0x 报告 §y"。
>
> **引用限制**：02 报告的法规全文取自 EUR-Lex 官方页面在 Wayback Machine 的 2025-01-18 英文存档（eur-lex.europa.eu 直连被 WAF 拦截）。条文编号与措辞以该存档为准，正式对外引用前建议在可访问 EUR-Lex 的网络下复核（见 02 报告 §阅读指南）。

---

## 目录

1. Executive Summary
2. 领域知识地图（Know the Domain）
3. CRA 法规要求（Know the Regulation）
4. CRA → Product Capability Mapping
5. 核心问题：为什么传统 "Component→CVE" SCA 不足以应对 CRA（Know the Problem）
6. 产品定位分析
7. 产品形态与信息架构
8. 技术架构参考
9. 竞争格局浓缩
10. 技术壁垒判断（Find the Moat）
11. AI/Agent 角色
12. Evidence Graph 数据底座
13. 五个 User Journey
14. MVP 与路线图
15. 关键战略问题 Q1–Q10
16. 主要技术风险与 Open Questions
17. 三张浓缩图表
18. 交叉核对说明

---

## 1. Executive Summary

### 1.1 一句话结论

CRA 把漏洞管理从"开发期的 repo 级告警"变成了"对**投放市场的产品版本**负法律责任的、带小时级时钟和十年留存期的全生命周期义务"。现有 AppSec/SCA 厂商的对象模型（repo/应用/工作负载）与监管提问的粒度（"哪个产品版本的哪个漏洞、判定了什么、修没修、证据在哪"）之间存在**结构性错配**，这是真实存在但正在收窄的产品定位空白（见 03 报告 §4）。对一家已有 SCA/SAST 能力的厂商，正确的战略不是"给 SCA 加一个 CRA 报表"，而是**以 CRA 为切入口，把核心对象从 Component/CVE 升级为 Product/Version/Lifecycle，并围绕 Evidence Graph 建立可辩护性壁垒**（Recommendation；支撑证据见 §5、§6、§10、§15）。

### 1.2 最重要的 5 个判断

**判断 1：定位空白存在，但窗口约 12–18 个月。** "以 Product/Version 为核心对象、覆盖完整漏洞生命周期闭环、面向 CRA 证据"的现代化产品，目前没有厂商完整占据（Fact 级观察，见 03 报告 §4）：AppSec 阵营（Snyk/Mend/Endor/GitLab 等）全部是 repo 对象模型；PSIRT 阵营（Finite State/ONEKEY）以产品为对象但技术栈停留在嵌入式二进制分析；JFrog（AppTrust 证据链 + CRA Compliance Brief）与 Black Duck（制造业案例 + VEX Templates + Project+Version 对象）是距离最近的两个占位者。若二者把对象模型升级为"产品线+版本+支持期"，空白将快速收窄（03 报告 §4 风险提示）。

**判断 2：CRA 义务的实质是"可辩护性（defensibility）"，不是"扫描覆盖率"。** 法规明确要求的是：SBOM 至少覆盖顶层依赖且**不要求公开**、上市时无**已知可利用**漏洞（不要求无所有漏洞）、按风险决定补救形式（不要求全修）、Art 14 知悉即报（**不强制主动威胁监控**）（Fact，见 02 报告 §4、§8、§15）。但每一项义务都要求**留痕**：技术文档与 EU DoC 保留 10 年或 support period（取长）、风险评估文档化、MSA 合理请求时必须能出示 SBOM 与证据（Art 31 + Annex VII）。违反 Annex I / Art 13 / Art 14 的罚款上限 €15M 或全球营业额 2.5%（Art 64(2)）。产品价值的核心是把"做了"变成"能证明"（Interpretation）。

**判断 3：Reachability 是工程壁垒而非技术壁垒，且其降噪叙事被高估——必须诚实定价。** 方法全部公开、govulncheck/CodeQL/Joern 等开源底座成熟，Snyk/Semgrep/Endor/GitLab 均已产品化（Fact，见 04 报告 §1、§6.1）。三条反面证据必须纳入决策：① "reachable" 是强证据但 "unreachable" 是弱证据（Snyk/govulncheck 官方承认静态分析无法证明不可达），因此 `not_affected + vulnerable_code_not_in_execute_path` 不能全自动签出；② Endor "降噪 92%" 等数字的分母是全部 findings，而 Datadog 用廉价得多的 runtime context（生产标记+互联网暴露）就把 82% 的 CVSS-critical 降级——reachability 的增量价值须与 context 过滤对比衡量而非与"什么都不做"对比（Fact，04 报告 §5）；③ package 级 reachability 已商品化，function 级正在快速商品化（03 报告 §3）。差异化机会在 **C/C++/嵌入式**（CRA 主战场语言、产品化最薄弱、无官方免费工具）（Interpretation，04 报告 §6.1）。

**判断 4：Evidence Graph 是三个候选方向中唯一的"真壁垒"候选，但它是 Hypothesis 而非 Fact。** in-toto/SLSA/GUAC 证明了 attestation 范式与图模型的可行性，但没有人在"安全结论级证据链"（reachability 判定、VEX status、修复验证）上建立标准（Fact + Hypothesis，见 04 报告 §4.3、§6.3）。壁垒来源是数据模型卡位 + 证据数据积累 + 信任位，不是任何单点技术。风险：若 CRA 执法强度与审计需求不及预期，它退化为"不错的平台架构"而非商业壁垒（04 报告 §6.3 明示）。同时注意：GUAC 的生产后端是 PostgreSQL/KV 而非 Neo4j——**"图数据库"是叙事，图数据模型+实体解析+证据链才是实质**（Fact，04 报告 §5.2）。

**判断 5：Agentic Vulnerability Management 可行，但唯一诚实的形态是"LLM 编排 + 确定性引擎出证据 + 人工签核"。** DARPA AIxCC 已实证该模式（冠军 ATLANTIS：确定性工具层产代码事实 → LLM agent 层做推理编排）；GitHub（CCR = "LLM intelligence + deterministic precision"）、Snyk（Agent Fix + SAST pre-screening）收敛到同一架构（Fact，04 报告 §3）。裸 LLM 安全 triage 准确率仅 61–67%（Simbian benchmark，厂商来源），没有任何严肃厂商让 LLM 结论未经确定性校验直接落地（Fact，04 报告 §5.3）。在 CRA 制造商担责的场景下，"全自动修复"短期不成立；卖点应是"agent 产出带证据的修复建议 + 确定性验证 + 人工一键签核"（Recommendation）。

### 1.3 核心结论速览

| 维度 | 结论 |
|---|---|
| 市场时机 | Art 14 已于 2026-09-11 生效且覆盖存量产品；2027-12-11 全面适用前是建设窗口（Fact） |
| 产品定位 | CRA-native Product Security Platform（第五种定位）为终局，以"CRA Foundation + 现有 SCA 复用"切入（Recommendation，§6） |
| 核心对象 | Product → Version → Release → SBOM → Vulnerability → Decision → Evidence（不是 repo/CVE）（§5、§15 Q2） |
| 技术壁垒 | Evidence Graph（潜在真壁垒，Hypothesis）> Reachability 多语言引擎 + vuln→function 数据策展（工程壁垒）> Exploitability 决策框架（无壁垒，产品功能）（§10） |
| AI 角色 | 编排层而非 copilot；结论证据必须来自确定性引擎；VEX/advisory 对外发布必须人工签核（§11） |
| 近期行动 | 未来 1–2 个月做 3–5 个技术 PoC 验证关键假设，首选 C/C++ function-level reachability 精度验证与结论级 in-toto attestation Evidence Graph 原型（§14） |
| 最大风险 | 定位窗口收窄（JFrog/Black Duck/平台厂商）；Evidence Graph 壁垒依赖 CRA 执法兑现；reachability 商品化速度（§16） |

---

## 2. 领域知识地图（Know the Domain）

> 本节为 01 报告（848 行、18 章）的浓缩。完整概念释义、真实 API 数据拆解（CVE-2021-44228 等）与逐条来源索引见 01 报告；此处只保留建立 mental model 所必需的骨架。

### 2.1 分层概念图：先分清层次，再谈概念

初学者最易犯的错是把 CVE、NVD、CVSS、SBOM、VEX 当作同类并列记忆。它们处在**完全不同的抽象层次**（01 报告 §1）：

| 层次 | 回答的问题 | 代表概念 |
|---|---|---|
| Identifier（标识符） | 这个东西叫什么？ | CVE ID、CWE ID、GHSA ID、CPE、PURL |
| Taxonomy（分类法） | 属于哪类问题？ | CWE |
| Scoring System（评分） | 多严重/多可能被利用？ | CVSS（severity）、EPSS（likelihood） |
| Database（数据库） | 去哪查结构化记录？ | NVD、GitHub Advisory Database |
| Data Source / Feed（数据源） | 原始信息从哪来？ | CNA 的 CVE Record、Vendor Advisory、CISA KEV、Exploit-DB |
| Data Format（数据格式） | 怎么序列化交换？ | CVE JSON 5.x、OSV Schema、CSAF、OpenVEX、SPDX/CycloneDX |
| Standard（标准） | 按什么规则做事？ | CVSS（FIRST）、CSAF（OASIS）、SPDX（ISO/IEC 5962）、PURL（ECMA-427）、SSDF、SLSA |
| Threat Intelligence | 攻击者在干什么？ | CISA KEV、EPSS、勒索软件标注 |
| Analysis Result（分析结论） | 对我的产品意味着什么？ | Vulnerability Association、Reachability、Exploitability、VEX statement |
| Compliance Artifact（合规工件） | 拿什么证明/通报？ | SBOM、VEX 文档、CSAF advisory、CRA 报告、Evidence/Audit Trail |

同一名字可能跨层：VEX 既是判断模型（Analysis Result）又有三种文件格式实现（CycloneDX VEX / CSAF VEX Profile / OpenVEX）；SBOM 既是 Compliance Artifact，其载体 SPDX/CycloneDX 又是 Data Format/Standard。读任何材料先问"它此刻指哪一层"（01 报告 §1）。

### 2.2 领域关系图（从资产到合规的流向）

```text
Software Product（CRA 的责任对象）
        │ contains
        ▼
Component ─── Package Identity: PURL（主轨道，包生态）/ CPE（辅轨道，OS/固件/COTS）
        │ 被记录在
        ▼
SBOM（SPDX / CycloneDX）—— "我有什么"
        │ 与漏洞情报做关联匹配（Vulnerability Association：误报/漏报第一发源地）
        ▼
Vulnerability Intelligence：NVD / OSV / GHSA / Vendor Advisory
        └── 全部锚定 CVE Record（CVE ID = 跨库 join key；CWE = 弱点类别）
        │ 附带优先级信号
        ▼
CVSS（多坏）/ EPSS（多可能）/ KEV（是否已被真实利用）
        │ 结合私有资产做判断
        ▼
Association → Reachability（走不走得到）→ Exploitability（在我的上下文能否被利用）
        │ 形成正式结论
        ▼
VEX（status + justification；not_affected 必须带机器可读 justification）
        ▼
Remediation / Verification（修 + 证明修好了）
        ▼
Security Advisory（CSAF）→ CRA Evidence / Reporting（合规闭环）
```

### 2.3 关键事实卡（每张卡一句话，详见 01 报告对应章节）

- **CVE ≠ NVD**（01 §2/§4）：CVE 是标识编目系统（MITRE 秘书处 + CISA 资助 + 517 家 CNA 联邦签发），不打分；NVD 是 NIST 在 CVE 之上的增强库（追加 CVSS/CPE/CWE/references）。著名的 Log4Shell "CVSS 10.0" 实际来自 CISA-ADP 的 Vulnrichment 追加容器，不是 Apache CNA 给的。
- **NVD 2026 政策转向**（01 §4，Fact）：CVE 提交量 2020→2025 增长 263%，NVD 积压无法清空；**2026-04-15 起 NVD 放弃全量 enrichment**，只对 KEV/联邦软件/critical software 即时处理，2026-03-01 前积压整体转 "Not Scheduled"。→ 只靠 NVD 的 SCA 会在最危险的窗口期失明；"多源融合"已从最佳实践变成生存必需。
- **OSV/GHSA 是开源匹配的主轨道**（01 §5/§6）：OSV 以 ecosystem+name+PURL+版本区间事件序列建模，与 SCA 输入（lockfile 坐标）形状一致，匹配近乎无损；GHSA 的 GitHub-reviewed 层人工策展、patched versions 为一等字段。Vendor advisory 掌握 backport 真相（版本号老≠没修），是版本范围的最终裁决者（01 §7）。
- **三个信号回答三个问题**（01 §8）：CVSS=severity（且 CVSS-B 明确"环境化是消费方责任"）、EPSS=未来 30 天利用概率（ML 预测，每日更新）、KEV=已观测利用的事实（1713 条，截至 2026-09）。加上两个私有信号 Reachability/Exploitability，构成从公共知识到私有结论的漏斗。
- **PURL vs CPE 双轨身份**（01 §9）：PURL（2025-12 成为 ECMA-427）对齐包管理器坐标，匹配是精确比较；CPE 是 NVD 的产品字典，包名→CPE 靠猜测映射，是误报/漏报最大来源。正确架构是双轨 + 显式映射关系，而非强行翻译。
- **SBOM ≠ SCA**（01 §10）：SBOM 是"记录"，SCA 是"分析"；SBOM 生成已商品化，差异化在准确性/新鲜度/可信度。
- **VEX 是判断结果而非文件格式**（01 §11）：statement = product + vulnerability + status + timestamp；四 status（affected/not_affected/fixed/under_investigation）；not_affected 必须带五种机器可读 justification 之一。产品应把 VEX statement 当数据库一等对象（可版本化、可追溯、可签名），导出格式只是适配层。
- **Reachable ≠ Exploitable**（01 §13/§14）：可达只说"代码能走到"，不说"攻击者能控制输入"。完全自动的 Exploitability 判定在多数语言下仍是研究级难题，诚实定位是"证据聚合 + 半自动裁决"。
- **Fix 的链条每环都可能断裂**（01 §15）：Fixed upstream ≠ Fixed in dependency ≠ Fixed in my product ≠ Fix verified。CRA 语境下"修好了吗"需要可出示的证据（新 SBOM、重扫记录、VEX status→fixed），不是 CI 绿灯。

### 2.4 14 步 Mental Model 故事线（01 报告 §18 浓缩版）

```text
 1. 我有什么软件？        → Product Inventory（产品注册，Product/Version 管理）
 2. 软件里有什么？        → SBOM（SPDX/CycloneDX；CRA Annex I 要求）
 3. 这些组件是谁？        → PURL / CPE 双轨身份归一化
 4. 世界上有哪些漏洞？    → CVE + NVD + OSV + GHSA + Vendor Advisory 多源情报管道
 5. 漏洞严重吗？          → CVSS（severity ≠ probability）
 6. 现实中会被攻击吗？    → EPSS / KEV / TI（KEV 命中 = 触发 CRA Art 14 时钟评估）
 7. 和我有关吗？          → Vulnerability Association（PURL/CPE 匹配 + 版本区间）
 8. 漏洞代码走得到吗？    → Reachability（justification: not_in_execute_path 的证据源）
 9. 我的环境能利用吗？    → Exploitability（部署/配置/输入可控性合取判断）
10. 我的正式判断是什么？  → VEX statement（not_affected 必须带 justification + 证据）
11. 怎么修？             → Remediation（fix version/backport 映射 + 兼容性分析）
12. 真修好了吗？          → Verification（重扫/回归/利用复现 → SBOM/VEX 自动更新）
13. 怎么告诉客户与监管？  → CSAF advisory / CRA Art 14 报告（24h/72h/14d 时钟）
14. 怎么证明整个过程？    → Evidence / Audit Trail（VEX 版本史 + SBOM 存档 + 签名 attestation）
```

**三句话总结**（01 报告 §18，Interpretation）：① 领域数据流本质是"公共知识 × 私有上下文 → 私有结论 → 公共输出"；② 传统 SCA 只做到第 7 步，第 8–10 步是当前竞争主战场，第 12–14 步是 CRA 把"做了"变成"证明了"之后的新刚需；③ 任何单一数据源都不可靠，**多源融合 + 证据链是立身之本**。

---

## 3. CRA 法规要求（Know the Regulation）

> 本节为 02 报告（387 行）的浓缩。完整条文引用、FAQ 细节与来源清单见 02 报告。02 报告采用四层标注：【法规】（条文原文，有强制力）/【官方解释】（Commission/ENISA 页面与 FAQ，权威但无法律强制力）/【标准·实践】/【厂商实现】。本节保留这一区分——**不要把最佳实践描述成法律强制要求**。
>
> ⚠️ 条文引用基于 EUR-Lex 的 Wayback 存档快照（2025-01-18），正式引用前需复核（见 02 报告 §阅读指南）。

### 3.1 适用范围与核心定义（【法规】Fact，02 报告 §1）

- **Art 3(1)**："product with digital elements" = 软件或硬件产品**及其 remote data processing solutions**（缺了它产品功能就残缺的厂商自有云后端随产品落入范围），含单独上市的软/硬件组件。
- **Art 2(1)** 范围闸门：投放市场 + intended purpose / 合理可预见用途包含**直接或间接数据连接**。
- 关键边界：
  - **SaaS/PaaS/IaaS 原则上不适用**（Recital 12，由 NIS2 管辖）——"CRA 覆盖所有软件服务"是错误说法；
  - 纯离线产品不适用，但**经 OS 间接联网的离线软件（如文本编辑器）仍在范围内**；
  - 医疗/机动车/航空/船用、国防专用、自产自用排除；
  - 被集成的 FOSS 组件本身不适用，但**集成它的制造商对整体负全责**（Art 13(5) due diligence）；
  - 免费开源豁免边界不在"是否开源"，而在"**是否在商业活动中供应/被 monetise**"（捐赠、厂商参与、定期发版本身都不构成商业性）。

### 3.2 四类角色（02 报告 §2，【法规】Fact）

| 角色 | 核心义务 | 关键点 |
|---|---|---|
| **Manufacturer**（Art 13，25 款） | 义务核心：Annex I Part I 产品 + Part II 流程、风险评估文档化、组件 due diligence、Art 14 报告、技术文档+DoC+CE、纠正/召回 | 定义含"无论收费、变现或免费"；罚款上限 €15M/2.5% |
| **Importer**（Art 19） | 上市前核实符合性；发现漏洞**无延迟通知制造商**；重大风险通知 MSA；留 DoC 副本 10 年 | — |
| **Distributor**（Art 20） | due care；核实 CE；漏洞通知制造商 | — |
| **OSS Steward**（Art 24） | 轻量定制义务：可验证文档化的 cybersecurity policy + 配合监管；**不贴 CE、不受任何罚款**（Art 64(10)(b)）；Art 14 报告义务仅在其参与开发范围内且 **2027-12-11 才起算**（目前无报告义务） | 典型如开源基金会 |

### 3.3 Annex I 义务（【法规】Fact，02 报告 §3）

**Part I — 产品属性要求（13 项）**，与漏洞生命周期最相关的：

- (2)(a) **上市时无已知可利用漏洞**——【官方解释】FAQ 4.2.1：不要求"无所有漏洞"，只要求"已知+可利用"，可利用性逐案判断；
- (2)(b) secure by default + 可重置出厂；(2)(c) 漏洞可经安全更新修复、**默认启用自动更新** + opt-out（专业 ICT/工业环境可豁免）；(2)(j) 限制攻击面；(2)(k) exploit 缓解；(2)(l) 内部安全活动记录监控。
- Part I 各项是 "where applicable"，由 Art 13(2) 风险评估决定裁剪，裁剪依据须写入技术文档（Art 13(3)）。

**Part II — Vulnerability handling 要求（8 项）**：

1. **识别并记录漏洞与组件，以常用机读格式绘制 SBOM，至少覆盖顶层依赖**（格式由 Commission implementing act 细化，Art 13(24)）；
2. **无延迟处理与修复漏洞**；技术可行时安全更新与功能更新分开；
3. 定期有效的安全测试与评审；
4. 安全更新发布后**公开披露已修复漏洞信息**（可延迟）；
5. 制定并执行 **coordinated vulnerability disclosure policy**；
6. 提供漏洞报告联系地址（覆盖自身产品和第三方组件）；
7. 安全分发更新的机制；
8. 安全更新**无延迟、免费**分发，附 advisory messages。

### 3.4 SBOM 的精确要求（02 报告 §4.1）

| 问题 | 答案 |
|---|---|
| 是否要求 SBOM？ | ✅ 机读、至少顶层依赖（【法规】Annex I Part II(1)） |
| **是否要求公开？** | ❌ **明确不要求公开**（Recital："Manufacturers should not be obliged to make the SBOM public"）；对用户公开是可选项（Annex II 9） |
| 谁有权获取？ | 技术文档包含；**MSA 合理请求且核查必需时必须提供**（Annex VII 8）；ADCO 依赖评估时可要求（匿名聚合） |

### 3.5 Art 14 报告机制（已于 2026-09-11 生效，【法规】Fact +【官方解释】，02 报告 §6）

两条报告线，经 ENISA SRP 一次提交即同时报送协调 CSIRT 与 ENISA：

| 阶段 | A 线：Actively Exploited Vulnerability（Art 14(2)） | B 线：Severe Incident（Art 14(4)） |
|---|---|---|
| 触发 | 知悉"有可靠证据已被恶意利用"的漏洞（Art 3(42)） | 知悉对产品安全有严重影响的 incident |
| ① Early warning | **知悉后 24h 内**，注明产品上市成员国 | 24h 内 |
| ② Notification | **72h 内**：产品信息、exploit 与漏洞性质、缓解措施、敏感度 | 72h 内 |
| ③ Final report | **纠正/缓解措施可用后 14 天内** | **72h 通知后 1 个月内** |
| 用户通知 | Art 14(8)：结构化机读格式通知受影响用户 | 同左 |

关键操作细节（【官方解释】ENISA SRP FAQ / Commission FAQ，Fact 级）：

- **SRP 已上线但无 API**，初期仅英文、网页手工提交；未验证身份前可先提交最多 20 条；
- **不追溯**：2026-09-11 前已知悉的 AEV 不需补报；此后知悉的即使漏洞早已存在也要报；
- **零日 ≠ 须报告**：只有已被恶意利用才触发；
- **第三方组件中的 AEV**：集成商须报；若组件漏洞在本产品不可利用则无需强制报告（→ Exploitability 结论直接决定报告义务）；
- 小微企业豁免 24h 时限罚款（义务仍在）；报告本身不加重责任（Art 17(4)）；
- ⚠️ 边界：Commission FAQ 5.1 明确 **CRA 不强制主动威胁监控**（遥测/蜜罐/暗网只是"可能的知悉渠道"）——"CRA 要求 7×24 威胁监控"是过度解读。但【厂商实现】层，监听 KEV/EUVD/vendor advisory 并在命中时触发报告时钟评估，是合理的最佳实践（01 报告 §16，Interpretation）。

### 3.6 Support Period 与上市后义务（02 报告 §7/§8/§9，【法规】Fact）

- Support period **至少 5 年**（Art 13(8)）；预期使用更长则相应更长；结束日期须在购买时标明并到期通知（Art 13(19)）；
- Art 13(7)：**系统性记录**产品网络安全信息（含知悉的漏洞及第三方通报）并更新风险评估；
- 安全更新发布后**保持可用至少 10 年或剩余支持期（取长）**（Art 13(9)）；免费、无延迟、可行时与功能更新分离；
- Art 13(6)：发现集成组件（含开源）漏洞须**上报组件维护者**，自研补丁须共享。

### 3.7 技术文档、时间线与罚则（02 报告 §10/§11/§12）

- **技术文档**（Art 31 + Annex VII）：产品描述、设计开发与漏洞处理过程（含 SBOM、CVD policy、联系地址证据、更新分发方案）、风险评估、support period 依据、测试报告、EU DoC；**保留至少 10 年或 support period（取长）**，support period 内持续更新。
- **时间线**：2024-12-10 生效 → 2026-06-11 notified body 体系适用 → **2026-09-11 Art 14 + SRP 上线（当前）** → **2027-12-11 主体义务全面适用**（存量产品原则上不适用，但 Art 14 例外覆盖存量，Art 69(3)）→ 2030-12-11 首次全面评估。Presumption of conformity 现状：截至 2026-07 **无任何 CRA 协调标准获 OJ 引用**（二手来源，（不确定）），Class I 产品实务上当前也须走第三方评估。
- **罚则**（Art 64）：违反 Annex I / Art 13 / Art 14 → **€15M 或全球营业额 2.5%（取高）**；技术文档/DoC/CE 等 → €10M 或 2%；误导性信息 → €5M 或 1%。另有非罚款风险：召回/撤回/禁售（Art 52–58）、集体诉讼（Art 65 + Directive 2020/1828）。
- **产品分类**（Art 7/8 + Annex III/IV）：Important Class I（19 类，含操作系统、杀毒、SIEM、VPN、密码管理器）、Class II（4 类：hypervisor/容器运行时、防火墙/IDS/IPS 等，**永远须第三方评估**）、Critical（3 类）。**安全产品本身就在 Annex III 里**——安全厂商自身首先是合规对象（Interpretation，02 报告 §13.2）。

### 3.8 与大众理解有出入的关键发现（02 报告 §15，浓缩）

1. SaaS 基本不适用 CRA；
2. SBOM 不要求公开；
3. 开源豁免边界是"商业活动中的供应"而非"是否收钱"；steward 是独立轻量角色（不罚款、报告义务 2027 年底起算）；
4. Art 14 覆盖存量产品；未被利用的零日不触发；不强制主动威胁监控；
5. 不要求修补所有漏洞、不要求产品无漏洞——"CRA = 所有 CVE 必须打补丁"是过度解读；
6. Class II 安全产品永远需要第三方评估。

### 3.9 与既有欧盟产品合规体系的关系(05 报告,2026-09-19 补充)

CRA 不是孤立的网络安全立法,而是欧盟 New Legislative Framework(NLF)产品法家族的第 29 部对齐立法:CE marking 是制造商声明产品满足所有适用协调法规的标志(非政府批文),NLF 三件套(Regulation 765/2008、Decision 768/2008/EC、Regulation 2019/1020)提供横向工具箱,CRA 沿用标准路径:技术文档(Art 31/Annex VII)→ 合格评定(Art 32,默认 Module A 自评;Annex III/IV 强制第三方)→ EU DoC(Art 28)→ CE(Art 29/30)→ 上市后义务 → MSA 市场监督(Art 52/53)。

最重要的新事实:Commission Delegated Regulation (EU) **2026/339**(2026-02-16 通过,一手 EUR-Lex 核实成立)自 **2027-12-11** 起废止 RED 网络安全授权法规 EU 2022/30——理由是其 Recital (3) 确认 CRA Annex I 已包含 RED Art 3(3)(d)(e)(f) 全部要素,避免双重监管;RED 本体(频谱/安全/EMC)不受影响,2025-08-01 至 2027-12-10 上市设备的 RED 网络安全市场监督继续有效。边界上:SaaS 归 NIS2(CRA Recital 12);MDR/IVDR/机动车/民航/船用设备经 Art 2(2)–(4) 排除;Art 2(5) 是 Commission 限制/排除 CRA 适用的通用阀门;Machinery Regulation 2023/1230(2027-01-20 适用)与 CRA **叠加适用**而非互斥。核心论点:RED 2022/30 是"产品属性 + 一次性评估"导向,CRA Annex I 是"属性 + 全生命周期漏洞处理义务"的双层结构——合规资产从一次性证书变为持续证据流,这正是漏洞全生命周期平台的嵌入点(详见 [05 报告](05-eu-compliance-landscape.md),含平台边界内/外分析)。

### 3.10 CIA 三性在 CRA 中的体现(2026-09-19 补充)

CRA 不以 CIA(Confidentiality/Integrity/Availability)为组织框架——**CIA 被拆散为 Annex I Part I 的产品属性条款**:C → (2)(e) 数据机密性/(2)(d) 防未授权访问/(2)(g) 数据最小化;I → (2)(f) 完整性防篡改 + Part II(7) 更新安全分发;A → (2)(h) 抗 DoS/(2)(i) 不损害他方可用性/Art 13(9) 更新 10 年可用。全部经 Art 13(2) 风险评估决定适用性——CIA 的法律形态是"经风险评估论证的适用属性",而非一刀切清单。对产品设计的两层含义:① Risk Engine 中 CIA 是 impact 侧维度(CVSS 的 C/I/A metric、SSVC technical impact),应结合产品上下文定权重而非照抄 CVSS——这是 Art 13(2) 风险评估的产品对应物;② CIA 反向定义平台能力:SBOM 分级披露(C,Recital 的匿名聚合要求)、证据链密码学完整性(I,attestation 签名 + 工件 hash 锚定,PoC 已验证)、更新归档与可用性监控(A,Art 13(9))。详见 [02 报告 §3.3](02-cra-regulation.md)。

### 3.11 执法架构:谁来"审计"(2026-09-19 补充)

CRA 没有中央"CRA 局"做定期审计,执法是三条独立的线:① **MSA(成员国市场监管机构)**——真正的执法者,被动触发(Art 14 报告/ADCO 抽查/投诉/公开事件),可调技术文档与 SBOM、罚款(成员国执行,上限 €15M/2.5%)、召回禁售;多数 Module A 自评产品直到 MSA 敲门才会"被审计"。② **Notified Bodies**——第三方但性质是**上市前合格评定**(仅 Annex III/IV,厂商自聘,Module B+C/H),非监管委托的事后审计;因协调标准仍无 OJ 引用,Class I 实务上可能也被推向第三方。③ **ENISA/CSIRT**——只收 Art 14 报告做态势感知,不评判合规,但报告记录是 MSA 线索来源。重要推论:CRA 罚的不是"安全能力弱"(Part II(3)"有效测试"是相对自身风险评估的要求,Part I(2)(a) 只管"已知"可利用漏洞),而是**出事后拿不出流程在运行的可辩护证据**——能力弱厂商正是平台的目标客户。平台需同时服务两种审计形态:上市前 notified body 举证(一次性大考)与上市后 MSA 调证(10 年留存期随时触发)。详见 [02 报告 §12.1](02-cra-regulation.md)。

---

## 4. CRA → Product Capability Mapping

> 基于 02 报告 §14 的 46 行"Article/Annex → Obligation → Security Activity → Product Capability"映射表提炼。46 行原表见 02 报告；此处重组为能力地图（Capability Map）。Product Capability 列属【厂商实现】层推论，非法律要求。

### 4.1 CRA Vulnerability Lifecycle Capability Map（六大能力域）

**能力域 A：范围与合规治理（Governance）**——对应映射表 #1–3、#45–46

| 能力 | CRA 依据 | 说明 |
|---|---|---|
| 范围评估判定器 | Art 2(1), 3(1)(2) | SaaS vs 产品组件分流问卷 |
| 产品分类器（Annex III/IV） | Art 7/8 | 决定符合性评估路径（自评 vs 第三方） |
| 合规路径向导 + 评估证据包 | Art 32 | Module A 自评 / B+C / H / EUCC |
| 存量产品登记 + 实质性修改判定 | Art 69(2)(3) | 存量仅 Art 14 适用 |
| 法规雷达 | Art 26/27, M/606 | 标准引用/法案更新推送（当前无 OJ 引用，正是需要跟踪期） |

**能力域 B：产品清单与 SBOM（Inventory）**——#11–13、#28–31

| 能力 | CRA 依据 | 说明 |
|---|---|---|
| **SCA 引擎 + SBOM 生成/版本化**（CycloneDX/SPDX） | Annex I Part II(1) | 至少顶层依赖；每次构建重新生成 |
| SBOM 格式合规校验器 | Art 13(24) | 随 implementing act 更新 |
| 组件准入 due diligence 引擎 | Art 13(5) | 更新活跃度、已知漏洞、EUVD/CVE 查询 |
| Support period 计算与文档化 | Art 13(8), Annex VII 4 | ≥5 年或预期使用期 |
| EOL 登记与到期通知 | Art 13(19) | 购买时标明 + 到期通知 |
| 更新归档库（≥10 年可用） | Art 13(9) | 长期归档 + 可用性监控 |

**能力域 C：漏洞情报与评估（Intelligence & Assessment）**——#15–16、#35

| 能力 | CRA 依据 | 说明 |
|---|---|---|
| 多源漏洞情报管道（NVD+OSV+GHSA+vendor CSAF+KEV/EPSS） | Annex I Part II(1), Art 13(7) | NVD 盲区弥补是卖点（01 报告 §4） |
| 漏洞知识库（产品维度台账）+ 风险登记册联动 | Art 13(7) | 系统性记录已知漏洞与第三方通报 |
| 发布门禁（release gate） | Annex I Part I(2)(a) | SCA 扫描 + KEV/EPSS/reachability 可利用性分级 |
| AEV 判定辅助（威胁情报集成） | Art 3(42), Recital 68 | KEV/EUVD/厂商情报辅助"actively exploited"判定 |

**能力域 D：漏洞处置与修复（Remediation）**——#14、#21–22、#27、#29、#32

| 能力 | CRA 依据 | 说明 |
|---|---|---|
| 漏洞修复工作流（SLA 计时、按风险定补救形式） | Annex I Part II(2) | 官方解释：低风险可仅记录，不要求全修 |
| 上游报告工作流 + 补丁共享记录 | Art 13(6) | 组件漏洞上报维护者 |
| 持续测试调度与合规记录 | Annex I Part II(3) | 周期性安全测试 |
| 更新发布流水线合规检查 | Part II(7)(8) | 免费性、及时性、安全分发 |
| 版本支持矩阵管理 | Art 13(10) | 只对最新版修复的前提管理 |
| 纠正措施跟踪（CAPA）/召回决策支持 | Art 13(21) | — |

**能力域 E：披露与报告（Disclosure & Reporting）**——#23–26、#33–41

| 能力 | CRA 依据 | 说明 |
|---|---|---|
| **CRA 报告工作台**：awareness 时间戳、24h/72h/14d 倒计时、分阶段表单（SRP 字段映射） | Art 14(1)–(5) | SRP 无 API，需生成可手工粘贴的结构化内容 |
| 事件分级向导 | Art 14(5) | 是否构成 severe incident |
| CSIRT 选择器 + 敏感度标记/PEC 请求 | Art 14(7), 16(2) | 管辖区判定 |
| 受影响用户范围分析（SBOM 反查）+ 通知模板 | Art 14(8) | 结构化机读通知 |
| Advisory 生成器（CSAF）+ CVE/CNA 对接 + 披露时间管理 | Part II(4) | 修复后公开披露 |
| VDP 平台/security.txt + 漏洞收件箱 + 人工响应 SLA | Part II(5)(6), Art 13(17) | SPOC 不得仅限自动化工具 |
| 进口商/分销商协同上报门户 | Art 19(5), 20(4) | 渠道漏洞通报 |

**能力域 F：证据与文档（Evidence & Documentation）**——#4–10、#42–44

| 能力 | CRA 依据 | 说明 |
|---|---|---|
| 风险评估模块 + Annex I 适用性裁剪工作流 | Art 13(2)(3) | 文档化 + 支持期内更新 |
| 技术文档自动生成（模板 + 证据聚合） | Art 31, Annex VII | 含 SBOM/CVD policy/更新分发方案/测试报告 |
| **证据库（SBOM/策略/记录统一存档）** | Annex VII 2(b) | 见 §12 Evidence Graph |
| 合规档案库（10 年/支持期保留策略自动化） | Art 13(13), 18(3) | — |
| 一键导出监管证据包（含 SBOM） | Art 13(22), Annex VII 8 | MSA 合理请求响应 |
| SAST/DAST/渗透测试集成与报告导出 | Annex VII 6 | 测试报告入档 |
| DoC 生成器 + 签署工作流 | Art 28/30 | — |
| Steward policy 生成与验证 / steward 报告模式 | Art 24 | 基金会客户（2027-12-11 起） |
| FOSS security attestation 注册表集成 | Art 13(5)+25 | 简化 due diligence |

### 4.2 从映射表看到的两个结构性结论（Interpretation）

1. **46 项义务中约 2/3 是"流程 + 证据"类而非"检测"类**。传统 SCA 只覆盖能力域 B/C 的一小部分；CRA 产品的本体是工作流 + 证据管理，检测引擎是输入之一而非全部。
2. **能力域 F（证据）是其余五个域的共同汇流点**——每个域的产出都必须落到可留存、可导出、可审计的证据对象上。这直接支撑 §12 的 Evidence Graph 作为底层数据模型的论证。

---

## 5. 核心问题：为什么传统 "Component→CVE" SCA 不足以应对 CRA（Know the Problem）

传统 SCA 的模式是：扫描 lockfile/制品 → 得到组件清单 → `组件+版本 → CVE` 匹配 → 告警列表。CRA 时代这个模式在五个环节系统性失效（综合 01/02/04 报告）：

### 5.1 情报层：NVD 失明窗口（Fact，01 报告 §4）

NVD 2026-04-15 起放弃全量 enrichment：一个 CVE 可能已公开、已有 exploit、已进 KEV，但在 NVD 里仍是 "Awaiting Analysis"/"Not Scheduled"，没有 CPE 和 CVSS。只挂 NVD 的 SCA 在最危险的窗口期（漏洞公开后到 enrichment 前）完全失明。而 CRA Art 14 的 24h 时钟从"知悉"起算——**失明窗口直接转化为合规风险敞口**。

### 5.2 关联层：身份错配与 backport 误报（Fact，01 报告 §7/§9）

- CPE 字典与包管理器坐标无系统对应，"包名→CPE"猜测映射直接产出误报/漏报；
- RHEL/Debian 等把安全补丁 backport 到老版本，版本号不变但漏洞已修——按上游版本号匹配必然误报，**只有 vendor advisory 知道真相**；
- 反向也成立：换名 fork 包（同代码不同坐标）在 CPE 模型里几乎无法表达，OSV 的显式建模才能覆盖。

### 5.3 判断层：成分级告警 ≠ 产品级结论（Fact，01 报告 §11/§13/§14）

SBOM 说"产品含 log4j-core 2.14.1"、NVD 说"该版本受影响"，但"产品是否真的受影响"需要 Reachability（漏洞代码可达吗）+ Exploitability（在我的部署上下文可利用吗）两级私有判断。OpenVEX 规范自述动机：SBOM 带来的极致透明会**增加**成分级误报，"Hence VEX"。CRA Annex I Part I(2)(a) 的上市门禁恰好是"已知+**可利用**"漏洞——**可利用性判定是法规概念的直接对应物**，传统 SCA 完全没有这一层。

### 5.4 降噪层：告警量与监管问题粒度双重错配（Fact + Interpretation）

- 告警量：reachability 厂商声称降噪 80–99%（03 报告 §1.10），但 04 报告 §5.1 的反面证据表明该数字被高估——"unreachable" 是弱证据（静态不可达不可证明），且 Datadog 数据显示仅靠 runtime context 就能把 82% 的 CVSS-critical 降级。真实结论：**降噪需要 reachability + runtime context + exploitability 裁决的组合**，单靠任何一层都不够。
- 粒度：监管问的是"哪个产品版本的哪个漏洞、判定了什么、修没修、证据在哪"，传统 SCA 答的是"这个 repo 有多少 CVE"（03 报告 §4.5 的"结构性错配"）。

### 5.5 证据层：修了 ≠ 能证明修了（Fact，01 报告 §15；02 报告 §10）

CRA 要求技术文档留存 10 年、MSA 请求时出示 SBOM、Art 14 报告带 awareness 时间戳。"Fixed upstream ≠ Fixed in dependency ≠ Fixed in my product ≠ Fix verified"——每一环都需要可出示的证据（新 SBOM、重扫记录、VEX status 流转）。传统 SCA 的告警列表没有证据对象模型，审计时无法重建"当时为什么这么判断"。

### 5.6 一句话

**传统 SCA 是"成分发现工具"，CRA 需要的是"产品级漏洞生命周期管理系统"**——差距不在扫描精度，而在对象模型（Product/Version vs repo）、判断深度（Exploitability vs Presence）、证据能力（可辩护 vs 告警列表）三个维度（Interpretation）。

---

## 6. 产品定位分析

> 五种定位的对比基于 03 报告（厂商现状）与 02 报告（义务结构）。结论见 6.3。

### 6.1 五种定位对比

| 维度 | ① CRA Compliance 产品 | ② 增强 SCA | ③ Vulnerability Management | ④ ASPM | ⑤ CRA-native Product Security Platform |
|---|---|---|---|---|---|
| **Target User** | 合规官、法务、产品经理 | 开发者、AppSec 工程师 | 安全运营、VM 团队 | AppSec 团队、安全架构师 | PSIRT、产品安全负责人、合规官、工程负责人 |
| **Buyer** | 合规/法务预算 | 工程/DevSecOps 预算 | 安全运营预算 | 安全部门平台预算 | CISO + 首席产品官/CTO 联合（法规驱动的高管预算） |
| **核心价值** | "帮我满足 CRA 条文" | "更准的告警 + 修复建议" | "统一漏洞台账与 SLA" | "多引擎关联与治理" | "对某个产品版本，从发现到证据的完整闭环 + 可辩护性" |
| **产品边界** | 文档、报告、流程 | 代码/依赖扫描 | 漏洞聚合与工单 | 应用安全全域 | 产品清单→SBOM→漏洞→判定→修复→证据→报告 |
| **技术边界** | 浅（不碰分析引擎） | 深（引擎为核心） | 中（聚合为主） | 深而广 | 深（引擎）+ 广（生命周期）+ 新（证据模型） |
| **商业优势** | 需求刚性、卖点清晰、销售周期短 | 复用现有资产、进入市场快 | 概念成熟、 buyer 现成 | 平台客单价高 | 空白定位（03 §4）、法规护城河、证据数据粘性 |
| **商业风险** | 天花板低、易被平台厂商"一个模块"吃掉；CRA 执法不及预期则需求萎缩 | 红海（21 家厂商）、商品化严重（03 §3）、CRA 只是营销话术（Snyk/Mend 现状） | 与现有 VM/ASPM 正面竞争（Wiz/Checkmarx） | 对象模型错配未解决，只是更大而不是更对 | 建设周期长；证据粒度监管期望未定型（03 §4 风险②）；需同时说服工程与合规两条线 |
| **与现有 SCA/SAST 关系** | 消费其输出 | 就是其升级 | 并列集成 | 包含之 | **以其为数据源之一，在其上重建对象模型** |

### 6.2 定位空白证据（03 报告 §4，Fact 级观察）

1. AppSec/SCA 阵营（Snyk、Mend、Endor、Checkmarx、GitLab、GitHub、Veracode、Semgrep、Socket、Arnica、Apiiro、Aqua、Wiz）**全部是 repo/应用/工作负载对象模型**；21 家对比表中 Product→Version 维度仅 Black Duck（Project+Version）、Sonatype（SBOM 绑版本 + VEX 跨版本延续）、JFrog（release 制品证据链）达到"部分"，且三家都缺 CRA 的产品线/支持期/监管报告语义；
2. 产品安全/PSIRT 阵营（Finite State、ONEKEY）以产品/build 为对象且 CRA 原生，但技术栈是嵌入式二进制分析，无 function reachability/agentic 修复/开发者工作流——现代软件厂商不会买；
3. Oligo 证明 runtime 证据可改变合规结论（FedRAMP SLA 72h→180d，厂商声称），但框架映射停在 FedRAMP/PCI/SOC 2，未接 CRA；
4. 开源雏形（Dependency-Track 的 project/portfolio+VEX）与个人项目（sbom-sentinel 自述目标几乎逐字是目标闭环）证明对象模型可行、市场感知已到；CRA 原生初创（CRACI，2026-05 种子轮 €1.4M）开始出现，**供给未到**。

### 6.3 定位判断（Recommendation）

**终局定位选 ⑤（CRA-native Product Security Platform），切入口是"①的合规刚需 × ②的现有资产"组合**：

- 纯 ① 天花板低且易被吞并；纯 ② 是红海且 CRA 只是话术；③④ 与巨头正面碰撞且不解决对象模型错配；
- ⑤ 的价值主张不是"发现了多少 CVE"，而是"针对某个具体产品和版本，从漏洞发现到风险判断、修复、验证以及最终合规证据的完整闭环"——这恰好是 CRA 义务的镜像；
- 路径依赖的现实约束：不要重建已有 SCA/SAST 引擎，而是把核心对象模型换成 Product/Version/Lifecycle，把引擎能力作为数据源接入（§8 架构）；
- 窗口风险明示：JFrog 与 Black Duck 距离最近，窗口估计 12–18 个月（Hypothesis，基于 03 §4 反方提示）。

---

## 7. 产品形态与信息架构

> 主线：**Product → Version → Release → SBOM → Vulnerabilities → Risk → Remediation → Compliance Status**。三个核心工作台共享同一个 Evidence Graph 数据底座（§12），视图不同、对象相同。（Recommendation 层设计，对象模型依据见 §5/§6）

### 7.1 全局对象模型（先于页面设计）

```text
Product（产品线，CRA 责任主体；含 Annex III/IV 分类、support period 策略）
  └─ Version（投放市场的版本；含上市日期、support period 起止、EoL 通知状态）
       └─ Release（一次具体发布/构建；绑定制品 hash、SBOM、证据包）
            └─ SBOM（组件清单，版本化存档）
                 └─ Component（PURL/CPE 双轨身份）
                      └─ Vulnerability Association（CVE/GHSA/OSV 关联）
                           └─ Risk Decision（reachability + exploitability + TI → VEX statement）
                                └─ Remediation（任务/PR/补丁）→ Verification（重扫/回归证据）
                                     └─ Compliance Status（Annex I 裁剪、Art 14 时钟、技术文档就绪度）
```

### 7.2 工作台一：Product Security Dashboard（产品组合视角）

**用户**：产品安全负责人、工程负责人、合规官。**主问题**："我所有产品线的合规与风险水位如何？"

- **L1 组合层**：Product 卡片墙——每个产品显示：CRA 分类（默认/Class I/II/Critical）、当前在 support period 内的 Version 数、未闭环漏洞数（按风险分级）、Art 14 活跃报告时钟数、合规就绪度评分；
- **L2 产品层**：Product → Versions 时间线（上市日期、support period 终止日、EoL 通知状态）；每个 Version 挂最新 Release 的 SBOM 指纹与漏洞热力图；
- **L3 版本层**：Version → Release 列表 → 每个 Release 的 SBOM/Components/Vulnerabilities/Risk/Remediation Status/Compliance Status 六联视图；版本间 diff（新增组件、新增漏洞、VEX 继承状态）；
- **告警入水口**：新 CVE 命中、KEV 命中（AEV 时钟评估）、support period 临近到期、监管请求待响应。

### 7.3 工作台二：Vulnerability Workbench（单漏洞裁决视角）

**用户**：安全分析师、PSIRT。**主问题**："这个漏洞对我的每个产品版本到底意味着什么，我的正式判断是什么？"

围绕单个漏洞的一页式裁决界面：

```text
CVE/GHSA/OSV 聚合视图（多源字段对照：NVD vs OSV vs vendor advisory 的版本范围差异）
  → Affected Components（PURL/CPE）
  → 受影响 Product × Version 矩阵（SBOM 反查，跨产品线影响面）
  → Dependency Path（传递依赖链）
  → Vulnerable Symbol/Function（vuln→function 映射数据）
  → Reachability 证据（call chain，标注"强证据/弱证据/不可构建降级"）
  → Exploitability 上下文（网络暴露、认证、输入可控性、feature flag、缓解措施）
  → Threat Intelligence（CVSS/EPSS/KEV/exploit 成熟度，时间序列）
  → SSVC 决策点取值建议（机器预填 + 人工确认）
  → VEX Status 编辑（status + justification + impact/action statement）
      —— not_affected 强制挂证据引用，execute_path 类 justification 强制人工签核标记
  → Fix 方案（fix version / backport patch / workaround；breaking change 预判）
  → Verification 状态（重扫/回归/复现证据）
  → Evidence 链（结论→证据→工具→工件 hash→时间戳→决策者，§12）
```

### 7.4 工作台三：CRA Compliance Center（监管义务视角）

**用户**：合规官、法务、被签发的报告人。**主问题**："我对监管负什么责、时钟走到哪里、证据拿不拿得出？"

- **义务总览**：46 项映射（§4）按产品覆盖度着色（已覆盖/部分/缺口）；
- **Art 14 报告工作台**：活跃报告列表——awareness 时间戳、24h/72h/14d 倒计时、三阶段表单（字段映射 SRP 结构，因 SRP 无 API 生成可复制粘贴的结构化文本+附件包）、CSIRT 选择器、敏感度标记/PEC 请求、受影响用户通知记录；
- **技术文档生成器**：Annex VII 模板 + 证据自动聚合（SBOM、CVD policy、测试报告、风险评估、support period 依据），版本化留存（10 年/支持期策略）；
- **披露管理**：CVD policy 状态、漏洞收件箱（SPOC 人工响应 SLA）、修复后披露（CSAF 生成）、CVE 申请对接；
- **Support Period 监控**：各版本 EoL 日历、到期通知发送记录、更新归档可用性（10 年义务）；
- **监管请求响应**：一键导出证据包（MSA 请求场景）；
- **Audit Trail**：全量决策日志检索（谁在什么时间基于什么证据做了什么判断）。

### 7.5 三个工作台的关系（Interpretation）

Dashboard 回答"哪个产品有问题"，Workbench 回答"这个漏洞怎么办"，Compliance Center 回答"如何向监管证明"。三者是同一 Evidence Graph 的三个投影——**这是该设计与"SCA + 报表模块"的本质区别**：报表不是事后生成物，而是证据图的一个查询视图。

---

## 8. 技术架构参考

> 17 层架构，标注每层与已有 SCA/SAST 资产的关系：**【复用】**= 现有能力直接接入；**【改造】**= 现有能力需包装/扩展；**【新建】**= 需从零建设。依据：01 报告（数据流）、03 报告（业界实现现状）、04 报告（技术可行性）。

```text
┌─────────────────────────────────────────────────────────────────┐
│ Integration Layer          【改造】Jira/GitHub/GitLab/CI/CD/SIEM/ │
│                            ITSM/MCP tool 暴露                     │
├─────────────────────────────────────────────────────────────────┤
│ Reporting Engine             【新建】CSAF/OpenVEX 导出、SRP 表单、 │
│                            技术文档/证据包生成                      │
│ CRA Compliance Engine        【新建】义务映射、Art 14 时钟、披露工作 │
│                            流、support period 监控                  │
├─────────────────────────────────────────────────────────────────┤
│ Workflow Engine              【改造】工单/SLA/签核流                │
│ Remediation Engine           【改造】升级 PR/补丁/兼容性分析          │
│ Agent Runtime                【新建】Agent 编排 + tool 注册 + trace │
│                            落证据                                  │
├─────────────────────────────────────────────────────────────────┤
│ Risk Engine                  【新建】SSVC 决策树 + CVSS/EPSS/KEV/   │
│                            context 融合（不融合成单一分数）           │
│ Exploitability Engine        【新建】上下文因子聚合 + 半自动裁决      │
│ Reachability Engine          【新建】多语言 call graph（PoC 先行）   │
│ Static Analysis Engine       【复用】已有 SAST（CodeQL/自研）        │
├─────────────────────────────────────────────────────────────────┤
│ Evidence Graph / Evidence Store 【新建】结论级 attestation 图底座    │
│ Product Inventory            【新建】Product/Version/Release 注册表 │
├─────────────────────────────────────────────────────────────────┤
│ Vulnerability Intelligence   【新建】多源融合管道（NVD+OSV+GHSA+    │
│                            CSAF+KEV/EPSS，实体对齐以 CVE ID 为键）   │
│ SBOM Engine                  【复用/改造】Syft/cdxgen 或现有生成器， │
│                            补版本化存档与 diff                     │
│ SCA Engine                   【复用】现有 SCA（检测/关联）           │
├─────────────────────────────────────────────────────────────────┤
│ Data Ingestion Layer         【改造】feed 拉取、webhook、变更驱动    │
│                            增量同步（NVD change history API 等）    │
└─────────────────────────────────────────────────────────────────┘
```

### 8.1 各层要点与复用判断

| 层 | 要点 | 复用判断 |
|---|---|---|
| **Data Ingestion** | NVD API 2.0 + change history 驱动增量（01 §4 工程实践）；OSV/GHSA feed；vendor CSAF 聚合；KEV/EPSS 每日同步 | 【改造】feed 框架可复用，多源实体对齐逻辑新建 |
| **SCA Engine** | 组件识别（声明/二进制/代码片段）、PURL/CPE 双轨归一化 | 【复用】现有 SCA 核心；补双轨身份映射表（01 §9） |
| **SBOM Engine** | 生成已是商品（Syft/cdxgen 事实标准）；差异化在准确性（传递依赖/二进制/重打包）与**版本化存档** | 【复用+改造】生成复用，存档/diff/新鲜度策略新建 |
| **Vulnerability Intelligence** | CVE ID 为 join key 的实体对齐；vuln→function 映射策展（reachability 的成本中心，04 §1.5）；fix commit↔fix version↔backport 映射表（01 §15） | 【新建】这是数据资产层，无现成资产 |
| **Product Inventory** | Product/Version/Release 注册 + support period 状态机；与 CMDB/制品库/CI 对接 | 【新建】对象模型是本产品的根基（§5） |
| **Evidence Graph / Evidence Store** | 见 §12；关系库即可起步（GUAC 先例：PostgreSQL/KV，勿押注图数据库） | 【新建】核心差异化资产 |
| **Static Analysis** | SAST 复用；为 reachability 提供 call graph 底座（CodeQL/Joern） | 【复用】 |
| **Reachability** | 分语言分粒度建设；Go/Java 有开源底座，C/C++ 是差异化方向（04 §1.3/§6.1）；必须输出证据对象而非布尔值 | 【新建】工程壁垒所在 |
| **Exploitability** | SSVC 决策树（周级实现）+ context 数据采集（部署拓扑/暴露面/feature flag）；定位为"证据聚合+半自动裁决" | 【新建】框架无壁垒，集成工程是工作量 |
| **Risk Engine** | KEV 命中→立即行动+AEV 时钟评估；EPSS 高+CVSS 高→本周期修复；reachability/exploitability 降级路径；**不融合成单一分数**（FIRST 官方建议组合使用，04 §2.2） | 【新建】 |
| **Agent Runtime** | MCP tool 封装（SCA/reachability/SAST/CI）；Skill 资产（SSVC 树、CRA 条款映射、修复 playbook）；**每次运行的 tool call 序列 + 输入输出 hash 落 Evidence Store**（04 §3.3） | 【新建】 |
| **Remediation** | 升级 PR（Dependabot/Renovate 模式商品化）；差异化在 breaking change 预判（04 §3.1 L2 工具链）与 backport（Endor Patches 模式 L3） | 【改造】 |
| **Workflow** | SLA 计时、多级签核（not_affected/对外 advisory 强制人工） | 【改造】 |
| **CRA Compliance** | §7.4 工作台的后端：义务映射表（§4 的 46 行数据化）、Art 14 时钟状态机、Annex VII 文档组装 | 【新建】 |
| **Evidence Store** | 10 年留存策略、不可变存储、签名 attestation | 【新建】 |
| **Reporting** | CSAF VEX Profile / OpenVEX / CycloneDX VEX 三格式导出（01 §11 三种实现）；SRP 手工提交辅助 | 【新建】 |
| **Integration** | 研发工具链双向集成；对外暴露 MCP tool 供客户 AI 生态调用 | 【改造】 |

### 8.2 架构判断（Interpretation）

1. **新建集中在"对象模型层 + 证据层 + 判断层"**（Product Inventory / Evidence Graph / Reachability / Exploitability / Risk / CRA Compliance / Agent Runtime）——这七层恰好是传统 SCA 没有的三层差距（§5.6）的工程对应物；
2. **复用集中在检测层**（SCA/SAST/SBOM 生成）——验证"不重建引擎、重建对象模型"的定位路径（§6.3）；
3. Evidence Graph 是中枢而非边缘组件：Agent trace、VEX 决策、修复验证、CRA 报告全部读写它（§12）。

---

## 9. 竞争格局浓缩

> 完整 21 家厂商分节与 12 维对比表见 03 报告；本节只保留决策所需的商品化判断与定位空白证据。

### 9.1 能力商品化光谱（03 报告 §3）

**已高度商品化**（2026 年做成不再是差异化）：

1. 基础 SCA 扫描与依赖告警（Trivy/Grype/Dependency-Track 免费 + GitHub/GitLab 内置，基线压到零成本）；
2. SBOM 生成（Syft/Trivy 事实标准，CycloneDX 1.7 已 ECMA 标准化）；
3. EPSS/KEV 信号集成（全员标配）；
4. 自动升级 PR（Dependabot/Renovate 普及）；
5. dependency/package 级 reachability（GitLab Beta、Socket、Arnica 已上线；Endor 自述 reachability 已成 table stakes）；
6. AI triage/降噪 copilot（Semgrep Assistant 声称承担 60% triage）；
7. VEX 格式层（Grype 消费、Black Duck VEX Templates、Sonatype VEX 注释）。

**正在快速商品化**（半年到一年窗口）：

1. function 级静态 reachability（主流语言）：Snyk Java/JS/Py GA、Semgrep 10+ 语言、Endor/Arnica/Socket 到位；但语言长尾参差（Snyk .NET 仍 EA，GitLab 仅 package 级，**C/C++ 全行业薄弱**）；
2. 单点 agentic 修复：GitLab 18.11 GA（2026-04）、Snyk Agent Fix GA（2026-09）、Checkmarx Developer Assist、Black Duck Signal GA（2026-03）——头部全部交卷，但**可信度指标全行业缺失**（无一家公布 AI 修复合并率/回归率）；
3. 恶意包/行为检测（Socket、Veracode-Phylum、Checkmarx、Snyk 均已补齐）。

**仍有明显创新空间**：

1. 跨语言含动态行为的 function-level reachability 的**证据化**（"可达判定→可审计 call chain"几乎无人做好；反射/DI 假阴性是公认难点，Snyk/GitLab 文档自认）；
2. Exploitability 决策层：代码级（Snyk/Endor）、运行时级（Oligo）、网络级（Wiz）三个阵营各占一块，**无人统一成可辩护判定并自动写入 VEX**；
3. Evidence graph/合规证据链：JFrog AppTrust 最接近（证据与二进制加密绑定+OPA gate）但绑在制品仓库生态，全链路无人完整实现；
4. Agentic remediation 的可信度基础设施（验证闭环、合并率遥测、升级影响预判——Endor Upgrade Impact Analysis 是唯一明确产品化的）；
5. 修复即服务/制品级修复（Chainguard backport 重建：EOL 依赖如 Spring Boot 2.7 的 143 个无补丁 CVE，干净版本号+VEX feed+扫描器互认）；
6. VEX 生命周期自动化（Sonatype 跨版本复制是唯一产品化；"新情报触发 VEX 失效重估"无人做）。

### 9.2 关键厂商态势速览（决策相关者）

| 厂商 | 与本产品定位的关系 | 要点（详见 03 报告对应节） |
|---|---|---|
| **JFrog** | **最接近的占位者，窗口收窄主风险** | 唯一有专门 CRA Compliance Brief；AppTrust 证据链（不可变 release bundle+OPA gate）最接近 Evidence Graph 思想；但对象是"制品"非"带支持期语义的产品线"，reachability/修复深度弱 |
| **Black Duck** | 次近占位者 | 制造业 CRA 真实案例（STMicro）；Project+Version 对象模型 + 2026.7 VEX Templates + 审计级证据是行业最强档；缺 reachability 深度与 agentic 闭环 |
| **Sonatype** | 对象模型启示来源 | SBOM Manager 独立产品 + VEX 注释跨版本延续（全行业唯一）；无 reachability/修复闭环 |
| **Endor Labs** | reachability 标杆与叙事对手 | function 级+call chain 证据+CVE→函数映射库；Upgrade Impact + Patches 差异化修复；但其降噪数字须打折（§10.2 反面证据） |
| **Snyk** | 功能广度标杆 | Evo 四环真 agent 编排（Discover/Remediate/Validate/Prevent）；reachability GA 三语言；无 Product→Version、CRA 仅内容营销 |
| **GitLab** | agentic 修复水位参照 | Agentic 修复 GA 最早（18.11, 2026-04）+ governed automation（19.2）；reachability 仅 package 级 Beta |
| **Chainguard** | 范式启示 | "不修代码、换制品"——证明修复→验证→SBOM/VEX 更新闭环可在制品供应链层完整实现 |
| **Oligo** | runtime 证据标杆 | 运行时函数执行观测→runtime SBOM&VEX→FedRAMP SLA 改变（72h→180d，厂商声称）；未接 CRA |
| **Finite State / ONEKEY** | PSIRT 阵营（半个占位者） | 产品/build 为对象、CRA 原生、托管合规服务；但技术栈是嵌入式二进制分析，无现代开发者工作流 |
| **Dependency-Track（OSS）** | 开源基线 | project/portfolio+VEX，开源世界最接近目标对象模型；无 reachability/修复/CRA 证据 |

### 9.3 定位空白判断（引用 03 报告 §4 结论）

> **空白存在但正在收窄**——"以 Product/Version 为核心对象、覆盖完整漏洞生命周期闭环、面向 CRA 证据"的现代化产品定位，目前没有厂商完整占据；两端各有半个占位者（JFrog/Black Duck 从 AppSec 侧、Finite State/ONEKEY 从 PSIRT 侧），中间断层明显。

反方风险（03 §4 明示，必须纳入决策）：① JFrog/Black Duck 升级对象模型则空白快速收窄；② CRA 执法实践未定型，证据粒度的监管期望有不确定性；③ GitHub/GitLab 若以 release 为轴重组 SBOM/漏洞数据，可从下往上吃掉该空间。

### 9.4 业内产品形态与技术栈格局（06 报告，2026-09-20 补充）

> 03 是"厂商×功能"视角；06 补齐形态分类学与技术栈两层。**供给收敛为十个物种，计费单位即物种指纹**：开发者平台型（Snyk/Endor，per dev）、运行时型（Wiz，per workload）、制品仓库型（JFrog/Sonatype，per server，air-gapped 齐备）与新子物种重建发行商（Chainguard，镜像目录订阅+CVE SLA）、企业 SCA 套件（Black Duck 有 air-gapped KB）、二进制固件型（ONEKEY 等，per image）、ASPM 聚合层（ArmorCode 明示"不自产扫描器"）、CLI 开源核心+商业 SaaS（Trivy/Semgrep）、漏洞情报供应（VulnDB 纯数据订阅）、CRA 原生初创（CRACI，pre-seed 体量）、开源自建派（Dependency-Track/GUAC 压价基线）。

**形态学二次确认 §9.3 空白**：以 Product→Version 为对象的生命周期平台在十个物种中无对应物——企业套件有对象模型无现代闭环，固件型有产品对象无开发者闭环；且新物种几乎全 SaaS-only，而 CRA 高相关行业（军工/汽车/医疗）要求 on-prem/air-gapped。

**技术栈五要点**：① 识别/匹配/SBOM/PR bot/runtime 探针五层已开源商品化（Trivy fanal、GrypeDB 离线库、Semgrep/OpenGrep 的 tree-sitter 路线、Tracee/Falco），自研=浪费；② 存储层 PostgreSQL 一统（Dependency-Track 生产实证），"图数据库是叙事"样本扩大（印证 §10.2 反叙事 2）；③ 漏洞策展收敛为"AI 加速+人类终审+风险优先队列"（GitHub 官方承认纯人工撑不住），backport 误报上限=发行版 feed 覆盖率而非算法；④ AI 修复架构趋同"确定性校验+LLM"，MCP tool 化（Snyk 模式）成为安全能力接入 agent 的标准接口；⑤ 自研差异化只在三处：产品/版本对象模型与证据链数据模型、垂直薄策展与 backport 数据质量、C/C++/二进制 reachability 证据化（详见 06 Part C）。

---

## 10. 技术壁垒判断（Find the Moat）

> 完整论证见 04 报告（TL;DR 表 + 第六章）。本节浓缩三个方向的壁垒定性 + 三条反叙事证据 + PoC 建议。这是本研究中"反面证据最集中"的一章，结论刻意保守。

### 10.1 三个方向的壁垒定性（04 报告 §6，Interpretation）

| 方向 | 壁垒判断 | 依据（浓缩） |
|---|---|---|
| **Reachability** | **工程壁垒（非技术壁垒）** | 方法全公开（call graph/CFG/taint）、工具链成熟（govulncheck 官方免费、CodeQL/Joern 开源）、多家已产品化→无算法壁垒。真护城河成分：① 多语言引擎持续投入（约 2–3 人年/语言，估计值）；② **vulnerability→function 标注数据集**（Snyk/Endor/Go 团队都在策展，这才是成本中心）；③ 不可构建项目的 fallback 工程。风险：govulncheck 的存在说明单语言 reachability 可被生态"国有化"。差异化机会：**C/C++/嵌入式与二进制 reachability**（CRA 覆盖的嵌入式/IoT 主战场语言、产品化最薄弱、竞争最少） |
| **Exploitability** | **仅产品功能（框架层）；其中"证据化 VEX"含工程壁垒成分** | SSVC/EPSS/KEV/CVSS 全公开，决策树实现以周计→零壁垒。有价值的成分：① 组织侧 context 数据采集治理（集成工程）；② not_affected justification 的机器证据链（deterministic 部分可自动，execute_path 类必须保守+人工）；③ 决策过程固化为可审计记录（与 Evidence Graph 合流）。**应作为 Evidence Graph 上的杀手级应用，而非独立技术方向** |
| **Evidence Graph + Agentic** | **Evidence Graph 是潜在真壁垒候选；Agentic 编排是工程壁垒且窗口期短** | 见 §12 与 §11。Agentic 修复模式已被 GitHub/Snyk/AIxCC 公开验证、追赶者众，壁垒成分=修复验证闭环工程化+失败率数据积累；"纯套 MCP 编排 LLM"无壁垒 |

### 10.2 三条反叙事证据（04 报告 §5，必须如实纳入结论）

**反叙事 1："Reachability 降噪 90%+"被高估。** Endor "up to 92%"的分母是全部 findings；且 unreachable 判定官方承认 unsound（Snyk："NO PATH FOUND ≠ 不可达"；govulncheck 列举 reflect/unsafe 漏报）。真正的对照基线：Datadog 基于数万应用遥测，仅 18% 的 CVSS-critical 依赖漏洞在叠加 runtime context（生产/互联网暴露）后仍为 critical——**廉价的 context 过滤拿走了大部分降噪价值，reachability 的增量须与之对比衡量**（Fact + Interpretation）。→ 产品含义：reachability 的定位是"VEX 证据源 + 精准排序"，不是"降噪神器"；优先级排序上 context（exposure/生产标记）应先于 call graph。

**反叙事 2："图数据库"是叙事，图数据模型才是实质。** GUAC（供应链图旗舰开源项目）生产后端推荐 PostgreSQL/内存 KV，Neo4j 后端官方明示 unsupported/incomplete；Wiz 式图可在关系库上复刻（PuppyGraph 演示）（Fact）。→ 押注"图数据库技术"没有壁垒；押注"安全本体+实体解析+证据链数据"才有。

**反叙事 3："Agentic 全自动修复/裸 LLM 判定"超出实测水位。** 裸 LLM 安全 triage 准确率 61–67%（Simbian benchmark，厂商来源）；所有严肃实现都靠确定性校验兜底；CRA 下制造商担责，全自动（无人签核）修复短期不成立（Fact + Interpretation）。另：arXiv 2503.14388（"Vexed by VEX tools"）实证容器扫描器+VEX 工具链对同一漏洞判定不一致——**VEX 自动化远未标准化**，`not_in_execute_path` 依赖的静态不可达证据本身是弱证据。

### 10.3 建议 PoC（详见 §14.3）

1. **C/C++ function-level reachability 精度验证**（04 §6.1 Hypothesis）：Joern/CodeQL + compilation database，测精度上限与假阴性率；
2. **结论级 in-toto attestation Evidence Graph 原型**（04 §3.3/§4.3 Hypothesis）：把 reachability 判定/VEX status 做成签名 attestation 入图。

---

## 11. AI/Agent 角色：Agentic Vulnerability Management 的可行性

> 依据 04 报告 §3。核心判断：可行，但只有唯一诚实的架构形态。

### 11.1 可行性已被实证（Fact）

DARPA AIxCC（2025 决赛）是最大规模实证：7 支队伍的全自动 Cyber Reasoning System 在 >5400 万行真实开源代码上发现+修复漏洞，冠军 ATLANTIS 的架构正是"**确定性工具层产出精确代码事实 → LLM agent 层做推理与编排**"。业界一线收敛到同一模式：GitHub CCR = "LLM intelligence + deterministic precision"（CodeQL/ESLint 兜底）；Snyk Agent Fix = 前沿模型 + 专家修复样本 few-shot + SAST re-scan pre-screening。**没有任何严肃厂商让 LLM 结论未经确定性校验直接落地。**

### 11.2 分工架构（Interpretation，04 报告 §3.2/§3.3）

```text
┌──────────────────────────────────────────────┐
│  Agent 层（reasoning + orchestration + 解释） │
│  · 高上下文、低可形式化任务                    │
│  · backport 冲突消解、无上游修复的补丁起草      │
│  · 跨步骤编排（CVE→哪个 repo→哪个版本线→几个 PR）│
│  · changelog/迁移指南的语义判读                │
│  · 把确定性信号汇总成人可读 decision rationale  │
│  · SSVC 决策点的建议值（人确认后生效）           │
├──────────────────────────────────────────────┤
│  Deterministic Engine 层（出证据，Agent 不可替代）│
│  · 版本解析与升级图、API diff、cherry-pick     │
│  · call graph / reachability 路径             │
│  · 构建/测试/re-scan/PoC 执行                  │
│  · SBOM diff                                  │
│  输出必须是可复现、可审计的事实                  │
├──────────────────────────────────────────────┤
│  Human-in-the-loop（签核点）                   │
│  · not_affected 断言、豁免                     │
│  · 对外发布的 VEX/CSAF advisory               │
│  · Art 14 报告的提交                           │
└──────────────────────────────────────────────┘
```

依据：裸 LLM triage 61–67% 不满足"事实产出"要求；Agent 是调度员与分析师，不是测量仪器（04 §3.3）。

### 11.3 六类 Agent 的组织方式（Recommendation）

| Agent | 职责 | 确定性依赖 | 签核点 |
|---|---|---|---|
| **Triage Agent** | 新 CVE 影响面初判（哪些 Product×Version 受影响）、情报摘要 | SCA 关联结果、SBOM 反查 | 低危可自动，高危人审 |
| **Reachability Agent** | 调度 call graph 分析、解读路径、标注证据强度（强/弱/降级） | Reachability Engine 输出 | unreachable→not_affected 必须人签 |
| **Exploitability Agent** | 聚合 context 因子、预填 SSVC 决策点、生成 rationale | context 数据、TI 信号 | VEX status 变更人签 |
| **Remediation Agent** | 选修复路径（升级/backport/workaround）、起草补丁与 PR、语义级 breaking change 判读 | 构建/测试/API diff/re-scan | PR 合入按客户既有评审流 |
| **Verification Agent** | 修复后验证编排（重扫、回归、利用复现）、SBOM/VEX 联动更新建议 | 验证证据对象 | status→fixed 流转人签 |
| **Compliance Agent** | Art 14 时钟监控、报告表单预填（SRP 字段映射）、技术文档组装 | 义务映射数据、Evidence Store | 报告提交必须人签 |

工具组织（Fact/Interpretation，04 §3.3）：MCP 已成 2025–2026 事实标准接口；SCA/reachability/SAST/CI 各封装为 MCP tool；领域知识（SSVC 决策树、CRA 条款映射、修复 playbook）编码为 Skill/prompt 资产；学术侧已有 Joern CPG 封装为 MCP server 的先例（codebadger）。

### 11.4 幻觉防控三层机制（Interpretation，有先例支撑，04 §3.3）

1. **Evidence-based agent**：agent 的每个结论必须携带 tool call 产物引用（AIxCC 的 PoV、Snyk 的 pre-screening 为先例）；
2. **Machine-verifiable evidence**：结论以结构化证据对象（调用栈、测试日志、SARIF）而非自然语言陈述存储；
3. **Human-in-the-loop 位置**：not_affected 断言、豁免、对外 VEX/CSAF、监管报告必须人工签核（与 CISA VEX justification 的"可辩护性"要求对齐）。

外加一条架构性要求：**每次 agent 运行记录为 attestation 风格的 trace**（步骤、工具版本、输入输出 hash、模型版本、时间戳）落 Evidence Store——使 AI 参与的安全决策具备 CRA 审计所需的可辩护性（Hypothesis，04 §3.3：目前未见厂商公开实现，是差异化点）。

---

## 12. Evidence Graph 数据底座

> 依据 04 报告 §4。本节回答：为什么它是数据底座、为什么比 Knowledge Graph 更适合合规、壁垒何在、风险何在。

### 12.1 节点/关系模型

```text
节点：Product · Version · Release · Repo · Artifact · Component · Package ·
     File · Symbol · Function · CVE · CWE · Exploit · Patch · Commit · PR ·
     SBOM · VEX Statement · Advisory · CRA Obligation · Evidence · Tool · Agent/Analyst

关系：contains · depends_on · affected_by · reachable_from · exploitable_via ·
     fixed_by · verified_by · reported_by · satisfies · evidenced_by · decided_by
```

可行性（Fact，04 §4.1）：该本体与 GUAC 高度同构——GUAC 已证明能统一 SPDX/CycloneDX/SLSA/in-toto/CSAF VEX/OpenVEX/OSV/deps.dev。但 GUAC 的诚实声明同样关键：实体标识符不总是可得，须靠启发式链接——**图的最大工程难点不是存储而是实体解析（identity resolution）**。这与 01 报告 §9 的"PURL↔CPE 显式映射 + 置信度"判断一致。

### 12.2 追溯链：结论→证据→工具→工件→时间戳→决策者

每个安全结论（Conclusion）挂完整证据链：

```text
Conclusion（如 VEX statement: Product X v2.3 × CVE-2026-YYYY = not_affected）
  → Evidence（call graph "no path found" 结果对象 / SBOM diff / 配置快照）
    → Tool（引擎名称 + 版本 + 参数；或 Agent trace id + 模型版本）
      → Artifact（输入工件 hash：SBOM、二进制、源码 commit）
        → Timestamp（分析时间）
          → Decision（决策者：人/Agent；签核记录；理由）
```

### 12.3 先例（Fact，04 §4.3）

- **in-toto**（CNCF graduated）："make it transparent what steps were performed, by whom and in what order"——供应链每步签名 attestation + 验证；
- **SLSA provenance**：以 in-toto attestation 为载体记录构建出处；
- **GUAC**：直接消费 in-toto ITE6/CSAF VEX/OpenVEX，证明"证据文档→图"管线可行。

**但现有先例的证据链覆盖的是构建过程；没有人把 attestation 范式系统性应用到安全结论**（reachability 判定、VEX status、修复验证）。Evidence Graph = in-toto 思想 × 漏洞生命周期（Hypothesis，04 §4.3：在 CRA 强制审计留痕背景下是真实空白点）。

### 12.4 为什么比纯 Knowledge Graph 更适合合规场景（Interpretation，04 §4.3）

- Knowledge Graph 回答"什么与什么相关"；**Evidence Graph 回答"这个结论凭什么成立"**；
- CRA 场景下买方（制造商）面对的是监管调取（MSA 合理请求须出示）、10 年留存义务、€15M/2.5% 罚款风险——需要的是**可辩护性（defensibility）**，纯关联图不携带证明力；
- 技术实现上不需要图数据库（GUAC 先例：PostgreSQL/KV 即可，见 §10.2 反叙事 2）——壁垒在**数据模型标准卡位 + 证据数据积累 + 信任位**（客户敢把合规证据托管给你），这恰是"真壁垒"的构造方式（04 §6.3）；
- 风险提示（Hypothesis）：壁垒依赖 CRA 执法强度与客户审计需求的实际兑现；若不及预期，退化为"不错的平台架构"。

---

## 13. 五个 User Journey

> 每个 Journey 标注使用的架构层（§8）与法规依据（§3）。均为 Recommendation 层设计，事实依据散见各分报告。

### Journey 1：新 CVE 发布 → 全生命周期闭环

```text
T+0h   Vulnerability Intelligence 管道捕获新 CVE（OSV/GHSA/vendor CSAF 先到，
       NVD 可能仍在 "Not Scheduled"——多源融合的价值点，01 §4）
  ↓    实体对齐（CVE ID/GHSA/alias）→ Vulnerability Association
T+1h   受影响 Product × Version 矩阵自动生成（SBOM 反查，Evidence Graph 查询）
  ↓    Triage Agent 初判 + 分析师确认
T+1d   Reachability Engine 出 call chain 证据（标注强/弱证据）
  ↓    Exploitability 聚合（context + CVSS/EPSS/KEV）
  ↓    Exploitability Agent 预填 SSVC 决策点 → 分析师签核 VEX statement
       （not_affected 强制挂 justification + 证据引用）
T+3d   Remediation：fix version 升级 PR（或 backport/workaround 决策）
       → CI 构建+测试+re-scan（确定性验证）
T+5d   Verification 通过 → SBOM 重新生成存档 → VEX status 流转 fixed
  ↓    全链路证据（关联→判定→修复→验证）落 Evidence Store
输出：每个受影响 Product Version 的完整证据链；技术文档自动更新
```

### Journey 2：Actively Exploited Vulnerability → CRA 24h/72h/14d 报告工作流

法规依据：Art 14(1)(2)(8)，02 报告 §6。触发说明：CRA 不强制主动监控（02 §8），但监听 KEV/EUVD/TI 是合理最佳实践（01 §16）。

```text
T+0    KEV 收录命中 / 内部发现恶意利用证据 / 外部研究者报告（漏洞收件箱）
  ↓    Compliance Agent 检测到 KEV 命中 → 启动 AEV 判定评估
       （Art 3(42)："可靠恶意利用证据"；未利用零日不触发，Commission FAQ 5.2）
T+0.5h 分析师确认构成 AEV → **awareness 时间戳落 Evidence Store（24h 时钟起算）**
  ↓    SBOM 反查受影响产品版本与上市成员国
T+2h   24h Early warning 表单自动预填（SRP 字段映射；SRP 无 API，
       生成可粘贴的结构化内容）→ 指定报告人签核 → 人工提交 SRP
T+24h  ⚠️ 时钟 1 截止（小微企业此时限豁免罚款，义务仍在）
  ↓    并行：Exploitability 判定（若组件漏洞在本产品不可利用→FAQ 5.4 可免于
       强制报告——判定结论与证据必须存档）+ 缓解措施落地
T+48h  72h Notification：exploit 与漏洞性质、已采取/用户可采取措施、敏感度标记
       （PEC 延迟分发请求如适用，Art 16(2)）→ 签核提交
T+72h  ⚠️ 时钟 2 截止；同步触发 Art 14(8) 受影响用户通知（结构化机读）
  ↓    修复 → 验证（同 Journey 1 的 Remediation/Verification 链）
修复可用后 14 天内 Final report：漏洞描述+严重性+影响、恶意行为者信息、
       安全更新详情 → 签核提交
全程：每次提交、每个决策、每份证据带时间戳入 Evidence Store（10 年留存）
```

### Journey 3：新产品 Release 合规门禁

法规依据：Annex I Part I(2)(a)（上市时无已知可利用漏洞）、Art 13(2)(3)、Art 31。

```text
Release 候选构建完成
  → SBOM 自动生成 + 版本化存档（与上一 Release diff）
  → SCA 关联 + KEV/EPSS/reachability 分级
  → 门禁规则（Policy as Code，JFrog AppTrust 已证明此模式，03 §1.5）：
      · KEV 命中且可利用 → block
      · 已知可利用漏洞未处置（无 VEX statement）→ block
      · 有 not_affected 结论但缺证据/签核 → block（证据完整性检查是差异化点）
  → 门禁通过 → Annex I 适用性裁剪确认 → 技术文档增量更新 → DoC 状态检查
  → Release 发布，证据包归档（SBOM+扫描报告+VEX 集+门禁决策记录）
```

### Journey 4：老版本 Support Period 监控

法规依据：Art 13(8)(9)(19)、Art 13(7)，02 报告 §7/§8。

```text
持续后台流程：
  · 每个在 support period 内的 Version 持续关联新漏洞（SBOM 不变、情报在变
    ——无需重扫，Anchore 模式，03 §1.13）
  · 新命中 → Journey 1 流程（按版本线分别评估：老版本可能需 backport 而非升级，
    Art 13(10) 版本策略前提检查：老用户免费升级？）
  · Support period 到期前 N 月 → EoL 通知任务（Art 13(19)）
  · 到期后 → 转入存量台账（Art 69(3)：仍受 Art 14 约束，AEV 报告流程不退役）
  · 安全更新归档可用性巡检（Art 13(9)：10 年或剩余支持期）
```

### Journey 5：第三方组件供应商发布安全更新

法规依据：Art 13(5)(6)、Annex I Part II(2)。

```text
Vendor advisory（优先 CSAF 机器可读通道，01 §12）发布组件安全更新
  → 情报管道识别：这是 fix version 发布 / backport 发布 / 仅 workaround
  → 匹配我方哪些 Product Version 使用该组件的受影响版本
  → 校验现有 VEX statement 是否失效（"新情报触发 VEX 重估"是无人做的创新点，03 §3.3.6）
  → 升级路径评估：fix version 有无 breaking change（API diff 工具链，04 §3.1 L2）；
    无兼容升级路径时 → backport patch 评估（Endor Patches 模式 L3）
    或制品替换评估（Chainguard 模式）
  → Remediation 任务按产品版本线分发 → 验证 → SBOM/VEX 联动更新
  → 若我方曾就该组件漏洞上报上游（Art 13(6)），核对上游修复与我方补丁一致性，闭环记录
```

---

## 14. MVP 与路线图

> 原则：不做大而全。每阶段给出 Goal / User Story / Feature / Dependency / PoC / Success Metric / Risk。时间框以 2026-09 为起点，对齐 CRA 时间线（主体义务 2027-12-11 全面适用——**Phase 1 必须在 2027 年中前可用**，Hypothesis 级排期）。

### 14.1 Phase 0 — 关键假设验证（1–2 个月）

**Goal**：用 PoC 验证/证伪决定架构走向的关键假设，不建产品。

| # | 假设 | 验证方式 | 判据 |
|---|---|---|---|
| H1 | C/C++ function-level reachability 精度可支撑产品化（04 §6.1 Hypothesis） | PoC-1（§14.3） | 在已知 CVE 测试集上 P/R 达到可用水位（目标值 PoC 设计时定） |
| H2 | 结论级 attestation Evidence Graph 可统一承载 reachability/VEX/修复验证证据（04 §4.3 Hypothesis） | PoC-2 | 三种结论类型可建模、可签名、可查询追溯 |
| H3 | 多源情报融合的实体对齐准确率足够高（01 §4/§7） | PoC-3 | NVD 盲区命中率可度量；PURL 匹配误报率 < 现有 SCA 基线 |
| H4 | SSVC+context 的 exploitability 裁决能显著降噪且可辩护（04 §2.2） | PoC-4 | 样本数据上复现 Datadog 式降级效果，且每条结论可溯源 |
| H5 | 目标客户（EU 市场制造商）对"Product→Version+证据"定位有付费意愿（03 §4 的空白判断是市场假设） | 5–10 家设计伙伴访谈 | ≥3 家愿意参与 Phase 1 试点 |

**Risk**：H5 是商业假设，PoC 无法纯技术验证；H1 若证伪，Phase 2 降级为 context-first 降噪。

### 14.2 Phase 1 — CRA Foundation（最小合规闭环，约 2 个季度）

- **Goal**：产品对象模型 + 情报管道 + SBOM 生命周期 + Art 14 报告工作流 + 证据留存——**不做 reachability/agentic**。
- **User Story**："作为 EU 市场制造商的产品安全负责人，我能注册我的产品版本、维护其 SBOM、在新漏洞发布当天知道哪些版本受影响、在 KEV 命中时启动带时钟的 Art 14 报告、并随时导出监管证据包。"
- **Feature**：Product Inventory（Product/Version/Release 注册 + support period 状态机）；多源情报管道 + 关联（PoC-3 产品化）；SBOM 生成/版本化/diff（复用 Syft/cdxgen 或现有 SCA）；Art 14 报告工作台（awareness 时间戳、倒计时、SRP 字段映射表单）；Evidence Store v1（关联结论+SBOM 存档+报告记录）；技术文档生成器 v1（Annex VII 模板）。
- **Dependency**：现有 SCA 引擎接入；EU 指定报告人试点客户。
- **Success Metric**：试点客户完成 ≥1 次真实或演练的 Art 14 报告全流程；新 CVE→受影响版本矩阵产出 < 4h；证据包一键导出通过合规官验收。
- **Risk**：SRP 无 API 使报告提交流程体验受限（缓解：结构化粘贴+浏览器辅助）；SBOM 格式 implementing act 未定（Art 13(24)）→ 格式校验器须可配置。

### 14.3 Phase 2 — Intelligent Triage（约 2 个季度，依赖 Phase 0 的 H1/H4 结论）

- **Goal**：Reachability + Exploitability + SSVC 风险裁决 + 证据化 VEX。
- **User Story**："作为安全分析师，每个漏洞告警自带可达性证据与上下文裁决建议，我签核的不是'感觉'而是证据链；not_affected 自动带 justification 与证据引用。"
- **Feature**：Reachability Engine（按 H1 结果定语言优先级：若 C/C++ 可行则主打差异化，否则 Java/Go/Python 跟随）；Exploitability context 聚合（暴露面/生产标记/feature flag）；Risk Engine（SSVC 决策树，不融合单一分数）；VEX Workbench（四 status + justification + 证据强制挂接 + 跨版本延续）；Agent Runtime v1（Triage/Exploitability Agent）。
- **Dependency**：vuln→function 映射数据策展启动（这是持续投入，04 §1.5 成本中心）；客户 context 数据接入（部署标记）。
- **Success Metric**：告警降噪率（与"context-only 基线"对比报告，诚实呈现，见 §10.2）；VEX statement 证据挂接率 100%；分析师单漏洞裁决时间下降 ≥50%。
- **Risk**：reachability 商品化速度（03 §3）——若 12 个月内主流语言全部沦为标配，差异化仅剩 C/C++ 与证据化；unreachable 弱证据引发的误判风险（缓解：execute_path 类 justification 强制人工签核）。

### 14.4 Phase 3 — Agentic Remediation（约 2 个季度）

- **Goal**：修复闭环——升级/backport/AI 补丁 + 确定性验证 + 证据留存。
- **User Story**："作为开发者，修复 PR 自动开好且带验证证据（构建通过、测试通过、漏洞不再触发的 re-scan 记录），我只需评审合入；升级会不会 break 有预判。"
- **Feature**：Remediation Engine（升级 PR + breaking change 预判 + backport 评估）；Remediation/Verification Agent（补丁起草、冲突消解、验证编排）；修复可信度遥测（合并率/回归率——**全行业缺失的指标，先建先赢**，03 §3.2）；验证通过后 SBOM/VEX 自动联动。
- **Dependency**：CI/CD 集成深度；AI Coding 工具链对接（Copilot/Cursor 生态或自建）。
- **Success Metric**：修复 PR 合并率与回归率遥测上线并对外公布（信任差异化）；median time-to-remediate（KEV 命中）显著低于客户基线。
- **Risk**：全自动修复叙事过度承诺（04 §5.3）——营销口径必须锁定"带证据的建议+确定性验证+人工签核"；修复质量问题损害信任位（Evidence Graph 壁垒的根基）。

### 14.5 Phase 4 — Product Security Platform（持续）

- **Goal**：完整平台化——PSIRT 工作流、组件供应商协同、steward 模式、披露自动化、Evidence Graph 开放。
- **Feature**：漏洞收件箱 + CVD 运营（Part II(5)(6)）；CSAF advisory 生产器（Part II(4)）；进口商/分销商协同门户（Art 19/20）；steward 报告模式（Art 24，2027-12-11 起有真实需求）；上游报告工作流（Art 13(6)）；EUVD 对接（Art 17(5)）；Evidence Graph 的 attestation 格式开源/标准化尝试（卡位策略，Hypothesis）。
- **Success Metric**：平台承载客户完整漏洞生命周期（Journey 1–5 全部在线）；Evidence 数据网络效应初显（跨客户 anonymized 情报价值）。
- **Risk**：与平台巨头（GitHub/GitLab/JFrog）正面碰撞；CRA 执法不及预期导致证据价值缩水（§10.2/§12.4 的明示风险）。

### 14.6 未来 1–2 个月最值得做的 3–5 个技术 PoC（Recommendation）

1. **C/C++ function-level reachability 精度验证**（04 §6.1 建议）：Joern/CodeQL + compilation database，选 20–30 个有明确 fix commit 的 C/C++ CVE，测 vuln→function 标注 + call graph 可达性的精度/召回/假阴性率；含"不可构建项目 fallback"与二进制场景抽样。**目的**：决定 Phase 2 的差异化押注是否成立（H1）。
2. **结论级 in-toto attestation Evidence Graph 原型**（04 §3.3/§4.3 建议）：PostgreSQL 后端（勿用图数据库，§10.2），把一条 reachability 判定 + 一条 VEX statement + 一条修复验证做成签名 attestation，实现"结论→证据→工具→工件 hash→时间戳→决策者"全链查询与导出。**目的**：验证统一承载力与审计演示价值（H2），这是最接近真壁垒方向的低成本试探。
3. **多源情报融合管道 + NVD 盲区度量**（01 §4/§7）：NVD+OSV+GHSA+KEV 每日同步，以 CVE ID/alias 实体对齐；抽 100 个近期 CVE 度量"NVD 未 enrichment 但 OSV/GHSA 已可匹配"的盲区比例与时长。**目的**：H3 + 为 Phase 1 情报层奠基，盲区数据本身即营销素材。
4. **SSVC + context exploitability 裁决原型**（04 §2.2）：决策树实现（周级）+ 两个 context 因子（生产标记、互联网暴露），在样本漏洞集上对比"CVSS-only 排序"与"SSVC+context 排序"的降噪与可解释性。**目的**：H4，验证廉价 context 的真实杠杆（Datadog 数据的内部复现）。
5. （可选）**Art 14 报告工作流纸上演练**：与 1–2 家设计伙伴用真实历史 AEV（如某 KEV 条目）走一遍 24h/72h 表单填写，验证 SRP 字段映射与 evidence 需求。**目的**：Phase 1 需求校准（非技术 PoC，H5 的组成部分）。

---

## 15. 关键战略问题 Q1–Q10

> 每题给出基于证据的回答；证据不足或有两面性时如实说明。详细证据散见前述各章，此处标注出处。

**Q1：CRA 是一个单独 Compliance Feature，还是重新定义 SCA 产品的机会？**
**答：两面皆有，但战略上应按后者下注、战术上按前者交付。** 证据：46 项义务映射中约 2/3 是流程+证据类（§4.2），超出任何"SCA 加一个报表"能覆盖的范围；主流厂商（Snyk/Mend）当前确实只做了"现有能力映射"的内容营销（03 §1.1/§1.2），说明"当 feature 做"是行业默认——这正是空白存在的原因（03 §4）。但按后者下注的风险是 CRA 执法不及预期（03 §4 风险②）。→ 以 CRA 义务为骨架重建对象模型，但第一阶段交付物必须是能独立卖的最小合规闭环（Phase 1），而非只有叙事。（Recommendation）

**Q2：核心对象应该是 Component/CVE 还是 Product/Version/Lifecycle？**
**答：Product/Version/Lifecycle。** 证据：CRA 的监管对象是"投放市场的产品"而非代码仓库（03 §0）；监管提问粒度是"哪个产品版本、判定了什么、修没修、证据在哪"（03 §4.5）；21 家厂商中无一家以该对象模型完整实现（03 §2 对比表第 12 列）；开源 Dependency-Track 与 sbom-sentinel 证明对象模型可行（03 §4.4）。注意：Component/CVE 仍是**分析的原子单位**——Product/Version 是组织与责任维度，二者不互斥，是投影关系（§7.1）。（Interpretation，证据充分）

**Q3：Reachability 是否值得成为核心技术壁垒？**
**答：不值得作为唯一壁垒；值得作为工程壁垒组合的一部分，差异化押注在 C/C++/嵌入式。** 证据：方法公开、开源底座成熟、多家已产品化，且 package 级已商品化、function 级快速商品化（03 §3）；Go 有官方免费工具说明可被生态国有化（04 §6.1）；"unreachable" 是弱证据限制了其合规断言用途（04 §5.1）；真正的成本中心是 vuln→function 数据策展而非引擎（04 §1.5）。C/C++ 方向是 Hypothesis 级机会（CRA 主战场语言+产品化最薄弱），须 PoC-1 验证后再下注。（04 §6.1）

**Q4：Exploitability 能否显著解决告警噪声？**
**答：能显著降噪，但"全自动 exploitability 判定"不成立；且廉价 context 过滤拿走大部分价值，reachability 增量须诚实定价。** 证据：Datadog 数据——仅 runtime context 就把 82% 的 CVSS-critical 降级（04 §2.2）；判定链越靠右自动化越低，无单一引擎能走完（04 §2.1）；SSVC 式"决策点+人工校准"比端到端 AI 判定现实（04 §2.2）；完全自动判定是研究级难题（01 §14）。→ 产品形态应为"证据聚合+半自动裁决+可审计决策记录"。（Fact + Interpretation）

**Q5：VEX 应该只是输出格式，还是 vulnerability decision 的正式结果？**
**答：是决策结果的语义模型，格式只是承载。** 证据：VEX 本质是 CISA 工作组定义的 statement 模型（product+vulnerability+status+timestamp），有三种序列化实现且语义同源、可互转（01 §11）；statement 可版本化演进（under_investigation→affected→fixed）；not_affected 必须带 justification，而 justification 与 reachability/exploitability 证据一一对应（01 §11）。→ 产品应把 VEX statement 当数据库一等对象（可版本化、可追溯、可签名），导出格式是适配层（01 §11 的产品建议）。"新情报触发 VEX 失效重估"的自动化无人做（03 §3.3.6），是产品化空间。（Interpretation，规范依据充分）

**Q6：Evidence Graph 是否值得成为底层核心数据模型？**
**答：值得，是三个候选方向中唯一的真壁垒候选——但这是 Hypothesis，且壁垒兑现依赖 CRA 执法强度。** 证据：in-toto/SLSA/GUAC 先例证明可行（04 §4.3）；无人把 attestation 范式应用于安全结论（空白）；CRA 的 10 年留存/MSA 调取/Art 14 时钟使可辩护性成为买方刚需（02 §10/§12）；它天然统一其余所有能力的产出（§4.2 结论 2）。反方：GUAC 后端是 PostgreSQL 而非图数据库——数据模型是实质、图数据库是叙事（04 §5.2）；若 CRA 市场不及预期则退化为平台架构（04 §6.3）。→ 以 PoC-2 低成本验证，架构上从现在起按"结论+证据"建模，但不对外承诺壁垒叙事。（Hypothesis + Recommendation）

**Q7：Agent 应该是 UI Copilot，还是整个 Vulnerability Lifecycle 的执行与编排层？**
**答：编排层，但带两个硬约束：事实产出委托确定性引擎，对外结论人工签核。** 证据：AIxCC/GitHub/Snyk 的严肃实现全部是"LLM 编排+确定性工具出证据"（04 §3.2/§3.3）；裸 LLM triage 61–67% 不配独立产出结论（04 §5.3）；纯 copilot 形态（GitHub Copilot Autofix、Mend）已商品化且无壁垒（03 §3.1.6）；Snyk Evo 四环证明编排层是头部厂商的演进方向（03 §1.1）。→ Agent = 调度员与分析师，不是测量仪器（04 §3.3）。（Interpretation，实证充分）

**Q8：Remediation 是否应该进入 AI Coding workflow？**
**答：应该，行业已在 GA，但进入方式必须是"确定性闸门后的落地"，且可信度遥测是差异化空档。** 证据：GitLab 18.11（2026-04）、Snyk Agent Fix（2026-09）、Checkmarx Developer Assist、Black Duck Signal 全部 GA（03 §3.2）；GitHub Copilot Autofix 是 CodeQL+LLM+coding agent 的确定性联动（04 §3.1 L4）；**无一家公布 AI 修复合并率/回归率**（03 §3.2）——先建可信度基础设施者建立信任差异化。（Fact + Recommendation）

**Q9：安全能力是否应从 Security after Coding 演进为 Security during Coding？**
**答：对漏洞预防环节是趋势，但本产品的主战场仍在 after/post-release——两面性。** 证据：during-coding 侧已有强占位者（Black Duck Signal 编码时 agent、Apiiro Guardian 在 prompt 层拦截、IDE 内 agentic 修复）（03 §1.3/§1.16）；而 CRA 义务的主体在上市门禁与上市后 support period（≥5 年）全周期（02 §3/§7），这是"after coding"的法律固化；Agentic 修复 PR 工作流本身横跨两者。→ 本产品应通过 Integration/AI Coding 对接进入 during-coding 环节（修复动作落在开发者工作流），但对象模型与证据锚点保持在产品版本侧。（Interpretation）

**Q10：CRA 是否可能成为 SCA → Product Security Platform → Agentic Security Platform 演进的商业切入口？**
**答：是，当前证据支持；窗口 12–18 个月（估计）。** 证据：Art 14 已生效且覆盖存量产品（2026-09-11），制造了即时刚需（02 §6/§11）；定位空白被四路独立证据确认（AppSec 阵营对象模型错配、PSIRT 阵营技术栈断层、运行时阵营未接 CRA、开源雏形无人产品化，03 §4）；CRA 原生初创已获融资（CRACI €1.4M 种子轮，2026-05）说明市场感知已到。反方风险：JFrog/Black Duck 升级对象模型、平台厂商自上而下重组、执法实践不确定（03 §4 风险提示）。→ 切入口成立，但"切入口"三个字意味着必须按 §14 路线图向平台演进，停在合规工具会被吞并。（Interpretation）

---

## 16. 主要技术风险与 Open Questions

### 16.1 技术风险

| # | 风险 | 等级 | 依据与缓解 |
|---|---|---|---|
| R1 | **Reachability 商品化 + "unreachable" 弱证据**限制差异化与合规用途 | 高 | 04 §5.1/§6.1；缓解：证据强度分级、execute_path 类强制人签、押注 C/C++（待 PoC-1） |
| R2 | **实体解析质量**（PURL↔CPE 映射、fork/重打包识别）决定关联准确率，而它是误差的第一发源地 | 高 | 01 §9、04 §4.1（GUAC 诚实声明）；缓解：建测试集与回归基准，关联准确率作为第一质量指标 |
| R3 | **vuln→function 数据策展是持续成本中心**，无捷径 | 中高 | 04 §1.5；缓解：优先覆盖客户语言栈 + KEV/高 EPSS CVE 优先策展 |
| R4 | **Evidence Graph 壁垒依赖 CRA 执法兑现**，若市场不及预期退化为架构优点 | 中高 | 04 §6.3；缓解：PostgreSQL 低成本实现、不押注图数据库、PoC-2 先行 |
| R5 | **AI 修复质量事故损害信任位**（Evidence Graph 壁垒的根基） | 中 | 04 §5.3；缓解：确定性闸门 + 人签 + 遥测公开 |
| R6 | **SRP 无 API**（初期仅英文网页手工提交）限制报告自动化体验 | 低 | 02 §6.2；缓解：结构化粘贴辅助，跟踪 ENISA API 计划 |
| R7 | **C/C++ reachability 精度可能不达标**（预处理/函数指针/剥离二进制） | 中 | 04 §1.3；缓解：PoC-1 证伪机制，备选 context-first 路线 |
| R8 | **VEX 工具链判定不一致**（arXiv 2503.14388 实证）损害机器生成 VEX 的公信力 | 中 | 04 §2.3/§5.4；缓解：本产品内部一致性 + 证据挂接本身就是差异化 |

### 16.2 Open Questions

1. **SBOM 格式 implementing act**（Art 13(24)）何时发布、要素细则是什么？——影响 SBOM 引擎合规校验器设计（02 §4.1）。
2. **协调标准 OJ 引用时间表**：M/606 原定 2026-08/10 交付已传顺延（二手，（不确定））；presumption of conformity 通道何时真正可用？（02 §11）
3. **监管对"证据粒度"的期望**：MSA 核查时 accept 什么粒度的 reachability/exploitability 证据？执法实践定型前 Evidence Graph 的深度设计存在不确定性（03 §4 风险②）。
4. **EUVD 的演进**（Art 17(5)）：欧洲漏洞库与 CVE/GHSA 生态的实体对齐规则。
5. **C/C++ reachability 的精度上限**（PoC-1 待回答）。
6. **结论级 attestation 的标准化机会**：是否存在或应否发起"安全结论 attestation"的开放规范（in-toto 扩展？OpenVEX 扩展？）（Hypothesis，04 §4.3 延伸）。
7. **存量产品的实质修改判定**（Art 69(2)(3)）边界在执法中如何解释——影响 Journey 4 的台账逻辑（02 §15.4）。
8. **买方预算归属**：PSIRT/合规/工程三条线谁为主 buyer，影响定价与 GTM（03 §4 未覆盖的商业问题，（不确定））。
9. **Agent trace 的监管可接受性**：AI 参与的安全决策在 CRA 审计中如何被看待，无先例（04 §3.3 Hypothesis）。

---

## 17. 三张浓缩图表

### 图 A：CRA → Capability → Product → Technology Map

```text
CRA 义务（02 §14 的 46 行 → 六能力域）
│
├─ A. 治理（范围/分类/路径）──→ 范围判定器·分类器·路径向导 ──→ 规则引擎+法规数据库
├─ B. 清单与 SBOM（Part II(1)）──→ SCA/SBOM 引擎·版本化·准入评估 ──→ Syft/cdxgen【复用】+PURL/CPE 双轨+存档 diff【新建】
├─ C. 情报与评估（Art 13(7)、Part I(2)(a)）──→ 多源情报·发布门禁·AEV 判定 ──→ NVD+OSV+GHSA+CSAF+KEV/EPSS 融合管道【新建】
├─ D. 处置与修复（Part II(2)(3)(7)(8)）──→ 修复工作流·SLA·更新管理 ──→ 升级 PR/backport/breaking-change 工具链【改造】+验证闭环
├─ E. 披露与报告（Art 14、Part II(4)(5)(6)）──→ 报告工作台·VDP·advisory ──→ SRP 字段映射+CSAF/OpenVEX 生成+时钟状态机【新建】
└─ F. 证据与文档（Art 31、Annex VII）──→ 证据库·技术文档·监管导出 ──→ Evidence Graph（in-toto attestation 式）【新建·壁垒候选】

横向公共层：Product Inventory（Product/Version/Release 对象模型）· Risk Engine（SSVC）·
           Reachability/Exploitability 引擎 · Agent Runtime（MCP+trace 落证据）
```

### 图 B：End-to-End Vulnerability Lifecycle

```text
Discover          多源情报管道捕获 CVE/GHSA/vendor advisory/KEV（NVD 盲区由 OSV/GHSA 补）
   │
Associate         PURL/CPE 双轨匹配 + 版本区间（VERS/OSV range）→ 受影响 Product×Version 矩阵
   │
Reachability      call graph / call path 证据（强证据=有路径；弱证据=无路径）
   │
Exploitability    + context（暴露面/认证/输入可控/feature flag/缓解）→ SSVC 决策点
   │
Decide            VEX statement（status+justification+证据引用；not_affected/对外结论人签）
   │
Remediate         升级 PR / backport patch / workaround / 制品替换（breaking change 预判）
   │
Verify            构建+测试+re-scan+利用复现（确定性验证，证据对象化）
   │
SBOM/VEX          SBOM 重新生成存档；VEX status 流转（→fixed）；跨版本延续
   │
Report            CSAF advisory 发布；AEV/SI 时 Art 14 三阶段报告（24h/72h/14d-1m）
   │
Evidence          全链路结论→证据→工具→工件→时间戳→决策者 落 Evidence Store（10 年留存）
   └────────────────── 反馈：新情报触发既有 VEX statement 失效重估 ──────────────┐
                  ↑────────────────────────────────────────────────────────────┘
```

### 图 C：产品演进路线

```text
SCA（现状资产）
  │  +对象模型升级：Product/Version/Release
  ▼
Intelligent SCA（+多源情报融合、+reachability/exploitability 降噪、+SSVC 裁决）
  │  +生命周期闭环：修复→验证→SBOM/VEX 联动
  ▼
Vulnerability Lifecycle Management（+工作流、+VEX 一等对象、+证据留存）
  │  +CRA 义务映射：Art 14 时钟、技术文档、监管导出
  ▼
CRA-native Product Security Platform（Evidence Graph 底座、46 项义务覆盖、PSIRT 协同）
  │  +Agent 编排层：六类 Agent、确定性闸门、attestation trace
  ▼
Agentic Product Security（结论级证据标准卡位、跨客户证据网络效应）
```

---

## 18. 交叉核对说明

> 对四份分报告做了相互比对。大部分事实一致；以下为发现的口径差异与矛盾点，按严重度排列。

### 18.1 实质矛盾：Art 14 终报时限表述不一致（03 vs 02/01）⚠️ 需以 02 为准

- **03 报告 §0** 写："2026-09-11 Article 14 漏洞/事件强制报告义务已生效（24h 预警 / 72h 通知 / **1 个月终报**）"。
- **02 报告 §6.1**（有条文依据）：**漏洞线（AEV）终报 = 纠正/缓解措施可用后 14 天内**；**事件线（severe incident）终报 = 72h 通知后 1 个月内**。01 报告 §16 的表述（"14 天（漏洞）/1 个月（事件）"）与 02 一致。
- 结论：03 的"1 个月终报"对 severe incident 正确、对 actively exploited vulnerability **不正确**（应为 14 天）。本报告 §3.5 采用 02 的双线表。03 报告该处属概括性压缩导致的失真，建议回改 03 §0 加双时限。

### 18.2 口径差异：JFrog reachability 能力描述（03 vs 04）

- **03 报告 §1.5**：JFrog Contextual Analysis"判断 CVE 在制品/代码上下文中是否真正可利用（厂商声称）；非公开 call graph 粒度的 function 级证据"，对比表标 ◐。
- **04 报告 §1.4**："Mend/JFrog：均有 reachability 功能宣称（**本次未核实到官方技术细节，不确定粒度**）"。
- 结论：不矛盾但口径不同——03 依据的是 JFrog CRA Compliance Brief 的营销表述，04 承认未核实。两报告共同点是"粒度不可验证"。本报告采用"厂商声称、粒度未验证"口径。

### 18.3 口径差异：Wiz 收购时间点（03 vs 04，实为互补）

- **03 报告 §1.15**："2026-03-11 被 Google 以 $32B **完成收购**（EU 批准后交割）"。
- **04 报告 §4.2**："Google 以约 320 亿美元收购 Wiz（**2025-03 宣布**）"。
- 结论：二者互补（2025-03 宣布、2026-03 交割），非矛盾。引用时注意区分"宣布"与"交割"。

### 18.4 粒度差异：Snyk reachability 语言支持（03 vs 04，互补）

- 03 §1.1：GA 支持 Java/JS/Python，.NET Early Access；04 §1.3 单独确认 Python GA。无矛盾；04 未覆盖 .NET 状态。

### 18.5 潜在张力（非矛盾，但叙事权重不同）：reachability 价值评估

- **01 报告 §13** 称 reachability 是"把 SCA 告警量降一到两个数量级的最现实杠杆"；**03 报告 §1.10** 引厂商声称降噪 80–99%；**04 报告 §5.1** 则系统性质疑该数字（分母问题 + unreachable unsound + Datadog context 基线对比）。
- 结论：01/03 反映行业主流叙事，04 是刻意的反叙事校验。本报告采用 04 的保守口径（§10.2 反叙事 1），并把"降噪数字"类产品声明一律标注"厂商声称"。三份报告无须修改——它们是"叙事 vs 校验"关系，但读者（尤其是做产品定价与营销口径的人）必须以 04 为准。

### 18.6 其余一致性确认

- KEV 条目数（01 §8：1713 条，2026-09）、CVE 增长 263%（01 §4）、CNA 数量 517 家（01 §2）、EPSS v4 发布时间（04 §2.2：2025-03）等关键数字在各报告间无冲突；
- SBOM"不要求公开"、Art 14 覆盖存量产品、steward 2027-12-11 起算等法规事实在 01/02/03 中一致；
- Black Duck VEX Templates（2026.7.0）、Sonatype VEX 跨版本延续、GitLab package 级 reachability Beta 等厂商事实仅在 03 出现，无交叉冲突。

---

## 附录：分报告索引

| 分报告 | 路径 | 过程材料 |
|---|---|---|
| 01 领域知识体系 | `docs/research/01-domain-ontology.md` | `01-domain-ontology/sources/`（20+ source notes）、`research-log.md` |
| 02 CRA 法规 | `docs/research/02-cra-regulation.md` | `02-cra-regulation/sources/`（含 EUR-Lex Wayback 全文存档）、`research-log.md` |
| 03 竞争格局 | `docs/research/03-competitive-landscape.md` | `03-competitive-landscape/sources/`（22 条 notes）、`research-log.md` |
| 04 技术深挖 | `docs/research/04-technology-deep-dive.md` | `04-technology-deep-dive/sources/`（23 条 notes）、`research-log.md` |
| 05 欧盟产品合规体系（2026-09-19 补充） | `docs/research/05-eu-compliance-landscape.md` | `05-eu-compliance-landscape/sources/`（9 条 notes，EUR-Lex 一手直连核实 EU 2026/339）、`research-log.md` |
| 06 产品形态与技术栈（2026-09-20 补充） | `docs/research/06-product-forms-and-tech-stacks.md` | `06-product-forms-and-tech-stacks/sources/`（28 条 notes）、`research-log.md` |

> 本报告所有 Fact 的最终出处以各分报告的 source notes 为准；本报告不重复列 URL。

### 修订记录

- **2026-09-19**：新增 §3.9"与既有欧盟产品合规体系的关系"（05 报告摘要），附录索引增补 05 报告。核心增量：一手核实 Commission Delegated Regulation (EU) 2026/339 成立（2027-12-11 起废止 RED 网络安全授权法规 EU 2022/30）；CRA 的 NLF 产品法定位；CRA 与 NIS2/MR/RED 的边界条文。其余章节未改动。
- **2026-09-19**：新增 §3.10"CIA 三性在 CRA 中的体现"（摘要），02 报告新增 §3.3 完整分析。核心论点：CRA 不以 CIA 为组织框架，CIA 被拆散为 Annex I Part I 产品属性条款（C→(2)(e)/(2)(d)/(2)(g)，I→(2)(f)/Part II(7)，A→(2)(h)/(2)(i)/Art 13(9)），经 Art 13(2) 风险评估决定适用性；对产品设计的含义是 Risk Engine 的 impact 侧建模与 SBOM 分级披露/证据链完整性/更新归档三项平台能力。
- **2026-09-19**：新增 §3.11"执法架构：谁来'审计'"（摘要），02 报告新增 §12.1 完整分析。核心论点：CRA 无中央审计机构，执法为三线结构——MSA（成员国、被动触发、可调证罚款召回）、Notified Body（仅 Annex III/IV 上市前合格评定、厂商自聘、非委托审计）、ENISA/CSIRT（只收 Art 14 报告不审计）；CRA 罚的不是能力弱而是出事后无可辩护流程证据；平台需同时服务 notified body 上市前举证与 MSA 上市后调证两种形态。
- **2026-09-20**：新增 §9.4"业内产品形态与技术栈格局"（06 报告摘要），附录索引增补 06 报告。核心增量：十物种产品形态分类学（计费单位即物种指纹）；形态学二次确认 Product→Version 定位空白；技术栈入场底线（识别/匹配/SBOM/PR bot/runtime 五层复用开源，PostgreSQL 存储一统）与三处自研差异化（产品对象模型与证据链、垂直薄策展与 backport 数据质量、C/C++/二进制 reachability 证据化）。其余章节未改动。
