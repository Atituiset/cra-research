# 02 · CRA 法规与能力映射（Know the Regulation）

> 对应 mvp.md §十八 #2/#3/#14。本章把 Regulation (EU) 2024/2847（Cyber Resilience Act, CRA）拆成**义务清单**，再把每条义务映射到**产品能力**，形成 Article→Obligation→Activity→Capability 表（mvp.md 明确要求的交付物）。
> 来源：R3#1-#7 + EUR-Lex 官方全文（CELEX:32024R2847，本轮已存盘 grep 提取）。引用 `[EUR-Lex Art.X]` / `[EUR-Lex Annex I]` 为原文级证据。

## 1. CRA 是什么、管什么

- **法律地位**：EU 法规（Regulation），直接适用于所有成员国，无需国内立法转化。2024-12-10 生效 [R3#1]。
- **管辖对象**：投放欧盟市场的**含数字元素的产品**（products with digital elements）——从智能冰箱到工业控制器、从操作系统到**独立软件**（含 SaaS 中的产品组件，但纯 SaaS/纯服务有边界讨论，见 §2.3）[R3#1]。
- **核心逻辑**：把"网络安全"变成产品**基本要求**（essential requirements, Annex I），走 CE 标志路径——与玩具安全、CE 机械指令同一套**新框架立法**（New Legislative Framework）逻辑：制造商自评估/第三方评估 + 技术文档 + 符合性声明（DoC）+ CE 标志，市场监管（market surveillance）事后执法 [R3#6]。

### 1.1 结构速览
| 章/附件 | 内容 | 对产品设计的影响 |
|---|---|---|
| Art.1-4 | 目标、范围、定义 | 角色判定 |
| Art.5-11 | 义务主体（制造商/授权代表/进口商/分销商/OSS stewards）| 供应链责任传导 |
| **Art.13** | **制造商义务（产品网络安全风险管理、设计、SBOM、漏洞处理）** | **产品主功能区** |
| **Art.14** | **事件报告义务（24h/72h/final）** | **事件报告工作流** |
| Art.15-16 | CE 合格评定 / 符合性推定（协调标准）| 认证路径 |
| Art.17-18 | DoC、CE 标志 | 产物生成 |
| Art.19-21 | 授权代表、进口分销义务 | 谁替谁合规 |
| Art.24 | **开源软件 steward 义务** | OSS 项目风险 |
| Art.25-29 | 公告机构 / 市场监管 / 不合规产品 | 执法面 |
| **Annex I** | **Essential requirements**（Part I 安全默认/无已知漏洞/最小攻击面/机密性；**Part II 生命周期：漏洞处理、安全更新、SBOM、事件处理、披露、支持期**）| **能力设计的法条原文来源** |
| Annex II | 技术文档内容清单 | 导出/归档功能 |
| Annex III | 符合性评估程序 | 评估路径 |
| **Annex IV** | **需第三方公告机构评估的产品（critical/important 类）** | 目标客群筛选 |

### 1.2 时间线（今天 = 2026-09-19，已越过的线加粗）
| 日期 | 事件 | 状态 |
|---|---|---|
| 2024-12-10 | CRA 生效 | ✅ |
| **2026-09-11** | **Art.14 事件报告义务开始适用（24h/72h/final）** | **✅ 已生效 8 天** |
| 2026-06-11 | 部分条款（Art.7(2)-11、19-21、58-65 等，含部分角色义务）适用 | ✅ |
| 2027-12-11 | **主要义务全面适用**（Art.13、CE、Annex I 要求） | ⏳ 15 个月 |
| 2028-06-11 | 第三方合格评定的型式证书（Annex IV 路径）截止衔接 | ⏳ |
- 关键事实（对销售话术很重要）：**报告义务适用于 2027 年之前已投放市场的产品**——不是"2027 后新卖的产品才合规" [R3#1, R3#4]。存量产品线现在就该有事件报告能力。

## 2. 角色与责任（谁必须做什么）

| 角色 | 定义要点 | 义务摘要 | 法条 |
|---|---|---|---|
| **制造商** | 以自己名义开发/生产/销售，含**对已投放产品做实质修改的（含远程）主体** | 风险管理、Annex I 要求、SBOM、漏洞处理、报告、技术文档、CE | Art.13-14 |
| **授权代表** | 欧盟境内、制造商书面授权 | 存技术文档/DoC、配合监管 | Art.19 |
| **进口商/分销商** | 引入/供应产品 | 尽职核查 CE、不得供应不合规产品 | Art.20-21 |
| **OSS steward** | 以非商业活动维护开源组件的自然人/法人 | 市场实践文档（open-source software process map）、**协调披露、参与 ENISA SRP** | **Art.24** |
| **重要/关键产品类制造商** | Annex IV 列表（工业、医疗、基础等重要类 + 云计算/智能卡等关键类）| **强制公告机构（third-party conformity assessment）** | Art.15 + Annex IV |

### 2.1 两个对产品定位至关重要的边界
1. **OSS steward 不对下游产品贴 CE，且不能因开源义务被罚**（Art.64(10)/Art.64 exemption 框架下，steward 违反 Art.24 不处罚则到"制造商级"罚款；steward 走 ENISA SRP 模型报告漏洞情报）[R3#5, R3#7]——**开源项目不是我们的付费客户**；客户是需要"消费+证明"steward 信息的**制造商**。
2. **"实质修改"回流**：云服务商若对其托管的可配置产品做实质修改，可能变成"制造商" [基于公开资料；本轮未重抓 recital 原文]——SaaS 边界是客户尽调时的高频问题，产品可做"角色判定助手"（小而粘的功能）。

## 3. Annex I 原文：CRA 对漏洞管理的全部要求（能力设计母本）

> 以下为 EUR-Lex 原文级证据的义务拆解（英文原文 + 中文要点），逐条接产品能力。

### Part I — 安全基本要求（设计层）
| 原文要点 | 中文义务 | 产品能力 |
|---|---|---|
| designed, developed, produced… free from **known exploitable vulnerabilities** | 交付时不得含已知可利用漏洞 | 发布门禁：扫描+已知漏洞清零证明 |
| **default secure**, minimal attack surface | 默认安全配置、最小攻击面 | 配置基线+攻击面报告 |
| **confidentiality** (encryption at rest/in transit using state-of-the-art) | 机密性保护 | 密钥/加密盘点（可从 SBOM 关联） |
| integrity of essential functions; **software updates integrity** | 关键功能与更新的完整性 | 签名/更新链审计 |

### Part II — 生命周期要求（本产品主战场，逐条）
| 原文/结构 | 义务 | 对应产品能力（→ Capability 表用语） |
|---|---|---|
| **(1) vulnerability handling process**：identify, document, report, remediate; **share/deliver corrections & mitigations across supply chain**；**SBOM: "commonly used and machine-readable format covering at the very least the top-level dependencies"** [EUR-Lex Annex I Part II(1)] | 漏洞处理流程 + 供应链内协同 + **SBOM（顶层依赖起步）**；Commission implementing acts **可规定 SBOM 格式** | **SCA 摄取 + 多源情报 + SBOM 生成/校验/导出（SPDX+CDX）** |
| **(2) security updates without delay**；without **negative effects on functionality**；**pre-release transparency** to coordinated disclosure participants；**timely & effective information**；**automatic updates as default**（可用户暂缓，但严重风险须自动且用户可重启生效） | 安全更新时效+预发布透明+自动更新 | **修复建议→PR→灰度→验证→发布** 的自动化管道；更新策略配置 |
| **(3) free of charge / defined support period**（默认 **≥5 年**，除非产品寿命更短）；至少告知消费者支持期 | 公开支持期、免费安全更新 | **支持期作为产品一等属性**（客群=需声明 5 年支持期的厂商） |
| **(4) 单个漏洞的处理**：发布修复、**全供应链告知、无歧视地提供给受影响客户** | 单漏洞修复的分发与通知 | 修复公告/通知工作流 + 与 VEX/CSAF 发布联动 |
| **(5) vulnerable fix releases + 对 exploited vuln 的"active monitoring"** | 持续监控在野利用 | **KEV/在野利用 feed 接入 → 触发优先处理 + 报告** |
| **(6) events 处理与记录；记录至少 10 年** | 事件记录 10 年 | **证据库/审计留痕（Evidence Graph 即为此设计）** |
| **(7) 及时告知用户 remediation 建议**；文档引导安全配置/数据保护 | 用户侧安全指导 | 报告模板+客户通知 |

### 3.1 事件报告义务（Art.14）— 时间表就是产品规格
| 阶段 | 时限 | 内容 | 触发条件 |
|---|---|---|---|
| **早期预警** | **知悉后 24h 内** | 初步影响评估、是否恶意、严重程度、缓解措施 | **已被主动利用（actively exploited）或严重事件** |
| **正式通知** | **知悉后 72h 内** | Annex I(II)(7)-(9) 详细信息：根因、利用方式、严重度与影响评估、缓解、**受影响产品清单** | 同上 |
| **纠正措施报告** | 纠正措施实施后 **≤14 天** | final report（根因、严重度、影响、跨成员国影响、缓解与修复） | 已提交前两报 |
| **被要求补充** | 监管要求时 | 补充信息 | 监管问询 |
| **对最终用户** | 无迟延 | 公告受影响产品、风险、缓解、作者/发布方身份、CE | 已提供缓解 |
- **报告去向**：ENISA 运营的 **Single Reporting Platform (SRP)**，成员国 CSIRT/CB 与 ENISA 消费，**不用逐国重复报告** [R3#5, EUR-Lex Art.14]。
- **"严重事件"定义**（Art.3/Annex 语境）[R3#4]：涉及利用可能导致国家级公共安全严重后果的有害影响（生命、健康、人身安全、关键基础设施、数据保护/GDPR 级敏感数据、经济重大损失、系统可用性关键服务）。**产品含义**：需要"严重度→是否触发 24h"的**判定辅助**（而非让工程师自己猜）。
- **产品能力映射**：事件时间线管理器（0→24h→72h→14d 状态机）、受影响产品/SBOM 快照冻结、预填 SRP 报告字段、披露草稿（AI 起草+人工审批）。

## 4. 符合性、标准与处罚（客户为什么急）

### 4.1 符合性路径
- **默认路径**：内部生产控制（Module A）+ 技术文档（Annex II）+ 自我声明（DoC）+ CE 标志 [R3#6]。
- **强制第三方**：Annex IV 重要/关键类 → 公告机构介入（Module B/C 或 D/E/H 组合）[R3#6]。
- **符合性推定**：遵循**已 harmonise 的协调标准**（列出引用于 OJ 的标准）即可推定满足 Annex I [R3#6]。
- **标准化在途**：CEN/CENELEC/ETSI 收到 Commission 请求 **M/606**（C(2025)618），**41 项（w）标准工作项**覆盖 Art.7(4) 所需安全要求 [R3#6]——**标准未全落地前，产品的"证据完备度"就是客户对不确定性的替代品**。

### 4.2 处罚（为什么要现在买）
- **违反 Art.13（产品义务）/ Art.14（报告义务）等**：行政罚款上限 **€15,000,000 或全球年营业额 2.5%（取高者）** [EUR-Lex Art.罚则条]。
- 对比 GDPR：7.5M/2%——**CRA 罚则上限更高**，且市场监管可采取产品下架/召回式措施。
- 低层义务/提供误导信息有较低档罚款（€5M/1% 量级）[基于公开资料，具体档位以 EUR-Lex 罚则条为准]。

### 4.3 一张"时间压力"图（给销售/路演用）
```
2026-09-11 ──报告义务已生效（存量产品也适用）
     │  15 个月
2027-12-11 ──Annex I 全面适用（SBOM、漏洞处理、支持期、CE）
     │  6 个月
2028-06-11 ──第三方路径衔接完成
今天买 = 提前 15 个月建立证据链；2027 下半年买 = 挤在合规恐慌窗口（价格不敏感、交付容易翻车）
```

## 5. 法规强制 vs 官方解释 vs 行业最佳实践（mvp.md §十七 的合规口径纪律）

> **这张表直接决定营销材料的措辞。** 把"最佳实践"说成"法规要求"= 被合规团队一票否决；把"强制"说成"建议"= 丢掉紧迫感卖点。

| 主张 | 分类 | 证据 | 营销措辞（正确姿势）|
|---|---|---|---|
| 24h/72h/14d 事件报告 | **法规强制** | EUR-Lex Art.14（2026-09-11 起适用）| "CRA Art.14 强制" ✅ |
| SBOM（至少顶层依赖、机器可读） | **法规强制** | EUR-Lex Annex I Part II(1) | "CRA Annex I 强制" ✅ |
| 支持期 ≥5 年（默认） | **法规强制** | EUR-Lex Annex I Part II(3) | "CRA 默认要求 5 年" ✅ |
| 漏洞处理流程 + 记录 ≥10 年 | **法规强制** | EUR-Lex Annex I Part II(1)(6) | "CRA 强制" ✅ |
| 事件记录 10 年 | **法规强制** | EUR-Lex Annex I Part II(6) | "10 年留存" ✅ |
| OSS steward 非商业义务/免罚 | **法规强制（豁免）** | Art.24 + Art.64(10) | "CRA 对开源维护者的责任限定" ✅ |
| 必须用 SPDX/CycloneDX | **非强制（措辞是"常用机器可读格式"+授权 implementing acts）** | Annex I Part II(1) | "CRA 要求机器可读 SBOM；SPDX/CDX 是主流选择" ✅（不能说"强制 SPDX"）|
| 必须用 VEX / CSAF | **非强制（CRA 未点名）** | EUR-Lex 全文无 VEX | "行业实践+供应链传导事实" ✅（不能说"CRA 要求 VEX"）|
| 必须 reachability 分析 | **非强制（推导）** | "exploitable vulnerabilities" + VEX justification 词汇 | "判定 not_affected 的常见证据路径" ✅ |
| 必须 EPSS/KEV 打分 | **非强制（KEV 用于判定"actively exploited"触发报告有强关联）** | Art.14 触发条件 | "KEV 是 24h 判定的参考源之一" ✅ |
| 协调标准（M/606 在途）带来的具体技术参数 | **未来强制（通过符合性推定）** | C(2025)618 [R3#6] | "标准落地前，完备证据是最佳替代" ✅ |
| CISA 2026 SBOM Minimum Elements | **美国政策指引，非 EU 法** | R2#16 | "对齐国际 SBOM 实践" ✅（不能说 CRA 引用它）|
| 厂商"我们通过 CRA 认证" | **营销话术** | CRA 无"认证"一说，只有符合性声明+可能的公告机构 | 对客户应纠正为"支持符合性声明与技术文档准备" ✅ |
| recital 21：委员会可设 FOSS 自愿安全认证 | **官方意图/未来政策** | EUR-Lex recital | "官方预留了开源安全认证空间" ✅ |

> 纪律：本报告任何"必须"字样，必须能指回 EUR-Lex 条文号；否则写"实践上/推荐"。

## 6. Article/Annex → 义务 → 安全活动 → 产品能力 映射表（§十八 #14 交付物）

> 读法：左侧是法条，右侧是我们产品可售卖的能力单元。**Product Capabilities 列 = MVP 范围的候选池**（08 章从这里选 Phase 0-1）。

| 法条/附件 | 义务（Obligation）| 安全活动（Security Activity）| 产品能力（Product Capability）| MVP 优先级 |
|---|---|---|---|---|
| Annex I Pt II(1) | SBOM（顶层依赖起步，机器可读）| 物料清单生成与持续更新 | **SBOM Importer/Generator**（SPDX+CDX 双格式，质量评分）| **P0** |
| Annex I Pt II(1) | 识别并记录产品内漏洞与组件 | SCA 扫描 + 漏洞关联 | **多源情报归一引擎**（NVD/OSV/GHSA/advisory 别名消解+区间对齐）| **P0** |
| Annex I Pt II(1) | 漏洞处理流程（发现→记录→报告→修复）| 漏洞生命周期管理 | **Vulnerability Lifecycle 状态机**（含 SLA）| **P0** |
| Annex I Pt II(1) | 跨供应链分享修复/缓解 | 上下游协同 | 供应链通告工作流（v1 可仅导出 CSAF/VEX）| P1 |
| Annex I Pt II(2) | 安全更新无延迟、默认自动、预发布透明 | 修复发布管道 | 修复建议+PR 草稿+发布状态追踪（接 agent，见 06）| P1 |
| Annex I Pt II(3) | 支持期（默认≥5 年）声明 | 产品生命周期登记 | **产品×版本×支持期台账**（产品级模型的一等公民）| **P0** |
| Annex I Pt II(4)(5) | 单漏洞修复分发、对抗利用监控 | 修复验证 + KEV 监控 | KEV/在野利用触发器 + 复扫验证 | **P0**（KEV 触发）|
| Annex I Pt II(6) | 事件处理与**记录≥10 年** | 审计留痕 | **Evidence Graph / 审计事件库**（10 年留存设计）| **P0** |
| Annex I Pt II(7) | 及时告知用户 remediation | 披露沟通 | 披露/客户通知草稿（AI 起草）| P2 |
| Annex I Pt I | 无已知可利用漏洞、默认安全、最小攻击面 | 发布门禁 | 发布前扫描+配置基线 | P1 |
| **Art.14** | 24h/72h/14d 报告至 SRP | 事件响应 | **事件报告工作流**（时间线状态机+SRP 字段预填+受影响产品快照）| **P0**（义务已生效）|
| Art.14 | 判定"actively exploited / severe" | 可利用性研判 | **Exploitability 判定辅助**（KEV/EPSS/暴露面证据，输出判定+理由）| P0/P1 |
| Art.13 | 风险管理过程制度化 | 流程文档化 | 合规中心（policy→evidence 映射看板）| P1 |
| Art.15+Annex IV | 重要/关键类强制公告机构 | 第三方评估材料准备 | 技术文档（Annex II）自动汇编 | P2（高价值窄客群）|
| Art.17-18 | DoC + CE 标志 | 合规文书 | DoC 生成器 | P2 |
| Art.24 | OSS steward 市场实践文档/披露 | 下游消费 steward 信息 | **上游 advisory/CSAF 摄取器**（吃 Red Hat/上游 CSAF/VEX）| P1 |
| Art.25-29 | 配合市场监管 | 证据调取 | "一键导出监管应答包"（证据图→文档）| P1 |
| Annex II | 技术文档 10 年 | 文档归档 | 证据→Annex II 文档装配 | P1 |
| —（推导）| 判定受影响/不受影响的举证 | Reachability/Exploitability | **Reachability 分析器 + VEX 判定引擎**（详见 05）| **P0（差异化）** |
| —（推导）| 修复有效性举证 | 修复验证 | 复扫 + 调用链验证 | P1（详见 06）|

### 6.1 从映射表读出的 4 条产品结论
1. **P0 能力 = 8 项**：SBOM、多源归一、生命周期状态机、支持期台账、KEV 触发、证据图、事件报告、Reachability+VEX——这 8 项就是 MVP 边界（08 章将收敛到 3-5 个 PoC）。
2. **CRA 义务里"报告"和"证据"是硬到期项**（2026-09-11 已生效），"SBOM/CE"是 2027 项——**销售叙事按此分两波**。
3. **VEX/Reachability 不出现在法条字面**，但通过 "exploitable" + justification 举证成为**事实必需**——这是"合规解释层"产品的空间，也是最容易被竞品扭曲话术的地方（回到 §5 口径纪律）。
4. **产品级模型（产品×版本×支持期）vs 组件级模型（包×CVE）**：CRA 义务全部挂在"产品"上（报告受影响产品、支持期、CE），而传统 SCA 数据模型挂在组件上——**模型鸿沟是架构级机会**（03/04 章展开）。

---
*来源：R3#1-#7、EUR-Lex CELEX:32024R2847 原文。时间线以官方公告页为准 [R3#1]。*
