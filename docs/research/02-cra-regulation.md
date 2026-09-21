# 02 — EU Cyber Resilience Act(Regulation (EU) 2024/2847)法规研究:软件漏洞全生命周期视角

> 研究日期:2026-09-18 | 研究者:法规调研子任务
> **重要时间背景**:CRA Art 14 漏洞/事件报告义务已于 **2026-09-11(7 天前)开始适用**;ENISA Single Reporting Platform(SRP)同日上线。主体义务(Annex I、Art 13 等)2027-12-11 才适用。
> 配套材料:每条重要结论对应 [sources/](02-cra-regulation/sources/) 下一条 source note;检索过程见 [research-log.md](02-cra-regulation/research-log.md)。

## 阅读指南:四层标注体系

本报告严格区分四个层次,引用时用标签注明:

| 标签 | 含义 | 主要来源 |
|---|---|---|
| **【法规】** | Regulation (EU) 2024/2847 条文/Annex/Recital 原文要求(有法律强制力) | [sources/eur-lex-reg-2024-2847-fulltext.md](02-cra-regulation/sources/eur-lex-reg-2024-2847-fulltext.md)(EUR-Lex 官方文本的 Wayback 存档快照,2025-01-18 抓取件) |
| **【官方解释】** | 欧盟委员会 / ENISA 官方页面、FAQ、guidance(有权威性但**无法律强制力**,Commission FAQ 自称 working document) | [sources/commission-faqs-cra-implementation.md](02-cra-regulation/sources/commission-faqs-cra-implementation.md)、[sources/enisa-cra-srp-faq.md](02-cra-regulation/sources/enisa-cra-srp-faq.md)、[sources/commission-cra-page.md](02-cra-regulation/sources/commission-cra-page.md)、[sources/commission-cra-standardisation.md](02-cra-regulation/sources/commission-cra-standardisation.md) |
| **【标准/实践】** | 协调标准(harmonised standards)、行业最佳实践 | M/606 标准化体系;目前**无任何 CRA 协调标准在 OJ 获得引用** |
| **【厂商实现】** | 安全厂商/工具商的产品化方式 | 本报告末尾映射表的"Product Capability"列属此类推论 |

事实确定性标注:**Fact**(条文/官方页直接载明)/**Interpretation**(基于文本的合理推论)/ **Hypothesis**(假设,需进一步核实)/ **(不确定)**。

⚠️ 抓取限制说明:eur-lex.europa.eu 直连被 AWS WAF 拦截,法规文本取自 EUR-Lex 官方页面在 Wayback Machine 的 2025-01-18 英文全文存档(见 [research-log](02-cra-regulation/research-log.md))。条文编号与措辞以该文本为准;正式引用时建议在可访问 EUR-Lex 的网络下复核。

---

## 1. 适用对象与 "product with digital elements" 的定义

### 1.1 核心定义(【法规】Fact)

- **Art 3(1)**:"product with digital elements" = **a software or hardware product and its remote data processing solutions**,including software or hardware components being placed on the market separately。
- **Art 3(2)**:"remote data processing" = 由制造商或在其责任下设计开发的远程数据处理,**缺了它产品就无法实现其功能之一**。
- **Art 2(1)** 范围闸门:适用于 made available on the market、且其 intended purpose 或 reasonably foreseeable use 包含**直接或间接的逻辑或物理数据连接**到设备或网络的产品。

### 1.2 各类形态如何适用

| 形态 | 是否适用 | 依据 |
|---|---|---|
| 独立软件(app、可下载程序) | ✅ 适用 | 【官方解释】Commission FAQ 1.2:standalone software 明确在内(Fact) |
| 嵌入式软件/固件 | ✅ 适用(单独上市的嵌入式组件也是独立产品) | Art 3(1);FAQ 1.2(Fact) |
| 硬件(从芯片到 IoT 设备) | ✅ 适用 | Art 3(1)、FAQ 1.2(Fact) |
| **SaaS / 云服务** | ❌ **原则上不适用** | 【法规】Recital 12:**SaaS/PaaS/IaaS 由 NIS2(Directive 2022/2555)管辖**;只有构成某产品 Art 3(2)"remote data processing"的云功能(如智能家居厂商的远程控制云)才随产品落入 CRA。不支持产品功能的纯网站也不在范围内。(Fact) |
| 完全离线、无任何连接能力的产品(如基础计算器、无联网洗碗机) | ❌ 不适用 | 【官方解释】FAQ 1.3(Fact);注意:**经操作系统间接联网的离线软件(如文本编辑器)仍在范围内** |
| 组件供应商(单独上市的软/硬件组件) | ✅ 作为独立产品适用全部义务 | Art 3(1) "components being placed on the market separately";Art 13 全部(Fact) |
| 被集成的组件(未单独商业化上市,如多数 FOSS 库) | ❌ 组件本身不适用,但**集成它的制造商对整体产品负全责** | Art 13(5) due diligence;Recital 34(Fact) |
| 医疗器械、机动车、航空、船用设备 | ❌ 排除(各有部门法) | Art 2(2)(3)(4)(Fact) |
| 国家安全/防务专用 | ❌ 排除 | Art 2(7)(Fact) |
| 自产自用(不上市) | ❌ 不适用 | 【官方解释】FAQ 1.5 引 Blue Guide(Fact) |
| 测试版(alpha/beta/RC) | 豁免,须限时+可见标识 | Art 4(3)、Recital 37(Fact) |

---

## 2. 四类角色的责任

### 2.1 Manufacturer(Art 13,25 款)——义务核心

全部义务见 §3–§10 展开。要点:【法规】确保产品符合 Annex I Part I、其**流程**符合 Part II;风险评估文档化;组件 due diligence;漏洞处理覆盖 support period;Art 14 报告;技术文档 + EU DoC + CE;纠正/召回义务。**manufacturer 定义(Art 3(13))包含"whether for payment, monetisation or free of charge"**——免费发布商业产品(如免费商用软件)不豁免。

### 2.2 Importer(Art 19)

只能上市合规产品;上市前核实符合性评估、技术文档、CE、DoC、标识、support period 标注;**发现漏洞须无延迟通知制造商**,产品有 significant cybersecurity risk 时立即通知 market surveillance authority(MSA);保留 DoC 副本 10 年或 support period(取长)。(Fact)

### 2.3 Distributor(Art 20)

due care;核实 CE 与相关文件;发现漏洞通知制造商;significant risk 时通知 MSA。(Fact)

### 2.4 Open-Source Software Steward(Art 24)

- 定义(Art 3(14)):非制造商的**法人**,系统性、持续地支持特定 FOSS 产品(且该产品 intended for commercial activities)的开发并确保其存续。典型如开源基金会。(Fact)
- 义务是**轻量、定制化的**(Recital 18 / raw line 199):
  - Art 24(1):制定并**以可验证方式文档化 cybersecurity policy**(促进安全开发、漏洞处理、自愿报告、社区内信息共享);
  - Art 24(2):与 MSA 合作、应请求提供该文档;
  - Art 24(3):**Art 14(1) 漏洞报告义务仅在其参与开发的范围内适用**;Art 14(3)(8) 仅当 severe incident 影响 steward 自有开发基础设施时适用;
  - **不得贴 CE**(Recital);**不受任何罚款**(Art 64(10)(b))。
  - 【官方解释】steward 的 Art 24(3) 报告义务 **2027-12-11 才适用**(Art 71(2)),即目前(2026-09)steward 无报告义务(ENISA SRP FAQ #4/#29,Fact)。

### 2.5 Steward 与商业 manufacturer 的关键差异

| 维度 | Manufacturer | OSS Steward |
|---|---|---|
| Annex I Part I/II 产品要求 | ✅ 全部 | ❌ 不适用 |
| CE marking / EU DoC / 技术文档 | ✅ | ❌(且禁止贴 CE) |
| Art 14 报告 | ✅ 全量(2026-09-11 起) | 有限范围,且 2027-12-11 才起算 |
| 罚款风险 | 最高 €15M / 2.5% | **明确豁免**(Art 64(10)(b)) |
| 核心义务 | 产品+流程合规 | 一份可验证的 cybersecurity policy + 配合监管 |

### 2.6 免费开源开发者的豁免边界(【法规】Recital,raw line 191 —— Fact)

CRA 只管辖"在商业活动过程中供应"的 FOSS:
- **未被 monetise 的 FOSS 供应不算商业活动**;
- 接受捐赠/资助、厂商参与贡献、定期发版,**本身都不构成商业性**;
- 非营利组织开发 FOSS,只要收益全部用于非营利目标,不算商业活动;
- **向他人负责的 FOSS 项目贡献源代码的个人不适用 CRA**;
- FOSS **组件**只有当其原始制造商将其 monetise 时,供应才算 making available on the market。

→ 边界不在"是否开源",而在"**是否在商业活动中供应/被 monetise**"。(Interpretation 的固化:recital 列举了判断要素,最终个案判断留给 Commission guidance,见 Art 26(2)(a))

---

## 3. Annex I 逐条梳理(全生命周期 cybersecurity risk management)

### Part I — 产品属性要求(13 项,【法规】Fact)

| # | 要求 | 漏洞生命周期相关性 |
|---|---|---|
| (1) | 基于风险确保适当网络安全水平(设计/开发/生产) | 总纲 |
| (2)(a) | **上市时无已知可利用漏洞**(known exploitable vulnerabilities) | 上市门禁;【官方解释】FAQ 4.2.1:不要求"无所有漏洞",只要求无"已知+可利用"(可利用性逐案判断)(Fact) |
| (2)(b) | **secure by default** 配置 + 可重置出厂;定制产品可与企业用户另行约定 | 默认配置基线 |
| (2)(c) | 漏洞可通过安全更新修复;**默认启用自动更新**+清晰 opt-out+更新通知+可暂缓 | 更新机制设计要求;Recital 56:专业 ICT/工业环境可豁免自动更新(Fact) |
| (2)(d) | 防未授权访问(认证/访问管理)并报告可疑未授权访问 | — |
| (2)(e) | 数据机密性(静态/传输加密,SOTA) | — |
| (2)(f) | 完整性防篡改并报告损坏 | — |
| (2)(g) | 数据最小化 | — |
| (2)(h) | 基本功能可用性、抗 DoS | — |
| (2)(i) | 最小化对其他设备/网络可用性的负面影响 | — |
| (2)(j) | 限制攻击面(含外部接口) | 攻击面管理 |
| (2)(k) | 漏洞利用缓解机制降低事件影响 | exploit mitigation |
| (2)(l) | 记录监控内部安全相关活动(带用户 opt-out) | 日志/审计 |
| (2)(m) | 用户可安全彻底删除数据与设置 | — |

注意:Part I 各项是 "where applicable",由 Art 13(2) 风险评估决定哪些适用、如何落实(Art 13(3) 要求在技术文档中写明)。【官方解释】FAQ 4.1.3。(Fact)

### Part II — Vulnerability handling 要求(8 项,【法规】Fact)

1. **identify and document vulnerabilities and components**,包括以**常用机读格式绘制 SBOM,至少覆盖顶层依赖(top-level dependencies)**;
2. **无延迟处理与修复漏洞**,包括提供安全更新;**技术可行时安全更新与功能更新分开**;
3. 定期有效的安全测试与评审(tests and reviews);
4. 安全更新发布后**公开披露已修复漏洞信息**(描述、受影响产品、影响、严重性、修复指引;有正当理由时可延迟公开);
5. **制定并执行 coordinated vulnerability disclosure policy**;
6. 便利漏洞信息共享,**包括提供漏洞报告联系地址**(覆盖自身产品和第三方组件);
7. **安全分发更新的机制**,及时修复/缓解,适用时自动分发;
8. 安全更新**无延迟、免费**分发,附 advisory messages(定制产品可与企业用户另行约定)。

### 3.3 CIA 三性在 CRA 中的体现(2026-09-19 补充)

CRA 全文不使用 "CIA"(Confidentiality/Integrity/Availability)框架——**CIA 被拆散为 Annex I Part I 的具体产品属性条款,而非组织框架**。法规的组织轴是漏洞全生命周期(Part II)+ 风险评估(Art 13(2)),CIA 只是风险评估要论证的属性集合。三层体现:

**① 法规层:CIA → Annex I Part I 条款映射(【法规】Fact)**

| CIA | 条款 | 要求内容 |
|---|---|---|
| C 机密性 | (2)(e) | 数据机密性:静态/传输加密,SOTA 水准 |
| | (2)(d) | 防未授权访问(认证/访问管理)+ 报告可疑未授权访问 |
| | (2)(g) | 数据最小化(辅助 C) |
| I 完整性 | (2)(f) | 完整性防篡改 + 损坏时报告 |
| | Part II(7) | 更新安全分发机制(供应链完整性) |
| A 可用性 | (2)(h) | 基本功能可用性、抗 DoS |
| | (2)(i) | 最小化对其他设备/网络可用性的负面影响 |
| | Art 13(9) | 安全更新发布后保持可用 ≥10 年或剩余支持期("修复的可用性"亦被立法) |

注意:Part I 全部 13 项均为 "where applicable",由 Art 13(2) 风险评估决定适用性并写入 Annex VII 技术文档——CIA 在 CRA 下的法律形态是"经风险评估论证的适用属性",不是一刀切清单(【法规】Fact)。

旁证:RED 2022/30 的三类要求(网络保护/隐私/防欺诈)本质是 CIA 切片;EU 2026/339 Recital (3) 确认 CRA Annex I "includes all the elements"——废止 RED 授权法规的法律依据正是这个覆盖关系(见 [05 报告](05-eu-compliance-landscape.md))。

**② 评估层:CIA 是漏洞影响(impact)维度(Interpretation)**

漏洞优先级 = 可能性 × 影响,"影响"即 CIA:CVSS 向量内建 C/I/A 三个 impact metric(H/L/N),每条 CVE 的 severity 本质是对 CIA 损害程度的打分;CISA SSVC 同样把 technical impact 作为独立决策点。EPSS/KEV/Reachability/Exploitability 回答"会不会被打"(likelihood 侧),CIA 回答"打中了损失什么"(impact 侧)。产品 Risk Engine 的 CIA 影响应结合产品上下文而非照抄 CVSS——同一 CVE 在数据存储产品中 C 权重高,在工控网关中 A 权重高,这是 Art 13(2) 风险评估在产品内的直接对应物。

**③ 产品能力层:CIA 对平台设计的要求(Recommendation)**

- **C**:SBOM 本身是敏感资产——MSA 向 ADCO 提交时须匿名聚合以保护 SBOM 机密性(Recital,raw line 223);平台的证据导出需考虑 SBOM 分级披露。
- **I**:证据链本身是完整性机制——结论级 attestation 签名 + 工件 sha256 锚定,用密码学完整性证明合规证据未被篡改(已在 PoC 中验证篡改拒绝,见 [poc/](../../poc/));10 年留存期(Art 31)下这是证据可信度根基。
- **A**:Art 13(9)"更新 10 年可用"与 Part II(8)"免费无延迟分发"意味着客户需要更新归档与分发基础设施——已纳入 §13 映射表第 28 行(更新归档库与可用性监控),是纯 SCA 视角容易漏掉的能力。

---

## 4. Vulnerability handling 与 SBOM 细节

### 4.1 SBOM:要求什么、给谁、是否公开

| 问题 | 答案 | 依据 |
|---|---|---|
| 是否要求识别记录组件? | ✅ 明确要求 | Annex I Part II(1)(【法规】Fact) |
| 是否要求绘制 SBOM? | ✅,"including by drawing up a SBOM in a commonly used and machine-readable format covering **at the very least the top-level dependencies**" | 同上(Fact);格式与要素由 Commission implementing act 细化(Art 13(24)) |
| **是否要求公开 SBOM?** | ❌ **不要求公开**。"Manufacturers should not be obliged to make the SBOM public." | 【法规】Recital(raw line 663)(Fact) |
| 是否可选向用户提供? | ✅ 可选;若提供须在用户说明中写明获取途径 | Annex II 第 9 项(Fact) |
| 谁有权获取? | ① 技术文档中包含 SBOM(Annex VII 2(b));② **MSA 提出合理请求且为核查合规所必需时,必须提供**(Annex VII 第 8 项);③ ADCO 全欧依赖评估时 MSA 可要求提供(Art 13(25),提交 ADCO 须匿名化聚合) | 【法规】Fact |
| SBOM 保密性 | Recital(raw line 223):MSA 向 ADCO 提交时须匿名聚合以保护 SBOM 机密性 | Fact |

### 4.2 其他漏洞处理要点

- **及时修复**:Annex I Part II(2) "without delay";但【官方解释】FAQ 4.3.1:**不要求对所有发现的漏洞都打补丁**——按风险定补救形式(立即补丁/变通 advisory/手册更新/禁用功能),低风险可仅记录(Fact,官方解释层)。
- **上市后才发现的已知可利用漏洞**:上市时点合规即可,但 support period 内的 Part II(2) 义务要求在用户启用时尽快提供安全更新(FAQ 4.2.2)。
- **组件漏洞上报上游**:Art 13(6) —— 发现集成组件(含开源组件)漏洞时须报告组件维护者、按 Part II 修复;自研补丁须与组件维护者共享(适当时机读格式)。(【法规】Fact)
- **组件自身失支(EOL)**:制造商仍须自行补救(换组件/自研补丁/禁用功能)(FAQ 4.3.7)。
- **默认安全配置**:Annex I Part I(2)(b);组件制造商只对组件交付时的默认配置负责,不对集成商的修改负责(FAQ 4.2.4)。

---

## 5. Vulnerability Disclosure(协调披露)

【法规】Fact:
- **Annex I Part II(5)**:必须 put in place **and enforce** a policy on coordinated vulnerability disclosure(CVD)。
- **Annex I Part II(6)**:须**提供漏洞报告联系地址**(覆盖产品及第三方组件)。
- **Art 13(17)**:指定 **single point of contact**,用户可直接快速沟通(含报告漏洞),**不得仅限自动化工具**;须在 Annex II 用户说明中公开(Annex II 第 2 项:CVD policy 的获取地址也要给用户)。
- **Annex VII 2(b)**:CVD policy 与联系地址证据须纳入技术文档。
- Recital(raw line 655):CVD 应支持直接或经 CSIRT 间接、可匿名报告;鼓励机器可读的安全策略(如 security.txt);**鼓励但非强制 bug bounty**。
- **Annex I Part II(4)**:修复后须公开披露漏洞信息(这是"修复后公开"义务,与 CVD 接收义务互补)。

---

## 6. Art 14 报告机制(2026-09-11 起已生效)

### 6.1 两条报告线与时限表(【法规】Fact,Art 14(1)–(5);【官方解释】ENISA SRP FAQ #7)

**接收方(两条线相同)**:同时报给 ① **CSIRT designated as coordinator**(按 Art 14(7):欧盟主要机构所在地成员国;无主要机构时按 授权代表→进口商→分销商→用户最多成员国 顺序)和 ② **ENISA**;通过 **Art 16 single reporting platform(SRP)** 提交,一次提交即完成两方报送。

| 阶段 | A线:Actively Exploited Vulnerability(Art 14(2)) | B线:Severe Incident(Art 14(4)) |
|---|---|---|
| 触发 | 知悉"有可靠证据已被恶意利用"的漏洞(Art 3(42)) | 知悉对产品安全有严重影响的 incident(严重标准见 Art 14(5):影响敏感/重要数据或功能的 AIC,或导致恶意代码植入/执行) |
| ① Early warning | **知悉后 24h 内**(不得无故拖延);注明产品在哪些成员国上市 | **24h 内**;至少说明是否疑似非法/恶意行为所致 |
| ② Notification | **72h 内**:产品一般信息、exploit 与漏洞性质、已采取/用户可采取的缓解措施、信息敏感度 | **72h 内**:事件性质、初步评估、已采取/用户可采取的措施、敏感度 |
| ③ Final report | **纠正/缓解措施可用后 14 天内**:漏洞描述+严重性+影响;恶意行为者信息(如有);安全更新/纠正措施详情 | **72h 通知后 1 个月内**:事件详述+严重性+影响;威胁类型/根因;已实施与进行中的缓解措施 |
| 中间报告 | CSIRT 可要求 intermediate report(Art 14(6)) | 同左 |
| 用户通知 | Art 14(8):通知受影响用户(必要时全体),适当结构化机读格式;不及时通知时 CSIRT 可直接通知用户 | 同左 |

### 6.2 关键操作细节(【官方解释】ENISA SRP FAQ,Fact 级,2026-09-12 更新)

- **SRP 已上线**(portal.cra-srp.enisa.europa.eu),初期仅英文、**无 API**,须网页手工提交;Art 15 自愿报告功能尚未上线。
- 注册:Assigned Representative 制,EU Login + MFA;验证与提交并行,未验证前可先提交最多 20 条。
- **不追溯**:2026-09-11 前已知悉的 AEV 不需补报;此后知悉的,即使漏洞早已存在也要报(FAQ #13 + Commission FAQ 5.1/5.3)。
- **零日 ≠ 须报告**:只有已被恶意利用才触发;善意研究/bug bounty 发现的未利用零日不触发(可自愿报告)(Commission FAQ 5.2,引 Recital 68)。
- **第三方组件中的 AEV**:集成商须报;组件制造商(若组件已上市)也须分别报;若组件漏洞在本产品不可利用则无需强制报告(Commission FAQ 5.4)。
- **延迟分发(PEC)**:Art 16(2) 特殊情形下接收 CSIRT 可延迟向其他 CSIRT/ENISA 分发;Commission 已于 **2025-12-11 通过 Delegated Act** 细化(Art 14(9) 授权的落地)。
- 报告本身不加重责任(Art 17(4));修复后 ENISA 经制造商同意将漏洞纳入 **EUVD**(NIS2 Art 12(2) 欧洲漏洞库)(Art 17(5))。
- **小微企业豁免 24h 时限罚款**(Art 64(10)(a))——但义务本身仍在。

---

## 7. Support Period

【法规】Fact:
- 定义(Art 3(20)):制造商须按 Annex I Part II 有效处理漏洞的期间。
- **下限(Art 13(8)):至少 5 年**;产品预期使用不足 5 年的,support period = 预期使用时间;预期使用超 5 年的应相应更长(Recital 60 举例:主板、路由器、操作系统、工业控制系统)。
- 确定依据须写入技术文档(Annex VII 第 4 项);Commission 可对特定类别规定最低 support period(delegated act,Art 13(8) 第四项)。
- **结束日期通知义务(Art 13(19))**:购买时以易获取方式清晰标明结束日期(至少到月/年);技术可行时在产品上显示 EoL 通知;Annex II 第 7 项也要求向用户说明支持类型与结束日期。
- 支持期结束后:可继续卖库存,但新生产批次须各自设定 support period(【官方解释】FAQ 4.5.3);鼓励开放源码以便第三方延续漏洞处理(Recital 61,**非强制**)。
- 订阅制产品的特例:support period 可等于活跃订阅期(FAQ 4.5.2)。

---

## 8. 上市后持续漏洞监控义务

- 【法规】Art 13(7):**系统性记录**与其风险相称的产品网络安全信息,**包括其知悉的漏洞及第三方提供的任何相关信息**,并更新风险评估。(Fact)
- 【法规】Annex I Part II(3):定期安全测试与评审。(Fact)
- 【法规】Art 13(8):support period 内持续按 Part II 处理漏洞。(Fact)
- ⚠️ 边界(【官方解释】Fact):Commission FAQ 5.1 明确——CRA **不强制制造商为履行报告义务而主动开展威胁监控**(遥测、蜜罐、暗网监控只是"可能的知悉渠道"示例)。→ "CRA 要求 7×24 威胁情报监控"是**过度解读**(常见误区)。

---

## 9. 安全更新与用户通知义务

【法规】Fact:
- **免费**:Annex I Part II(8) 安全更新 free of charge(定制产品可与企业用户另行约定;Recital 64 限定 tailor-made 场景)。
- **与功能更新分开**:Part II(2) "where technically feasible";【官方解释】FAQ 4.3.4:技术不可分时可合并。
- **无延迟分发** + advisory messages(Part II(8));安全分发机制(Part II(7));默认自动更新+opt-out(Part I(2)(c))。
- **更新长期可用**:Art 13(9) —— 每个安全更新发布后保持可用至少 **10 年或 support period 剩余期,取较长者**。
- **版本策略**:Art 13(10) —— 实质性修改的后续版本,只对最后上市版本修复,前提是老用户免费升级且无额外环境成本。
- **用户通知**:Art 14(8)(AEV/SI 时);Part II(4)(修复后公开披露);Annex II(随附说明)。
- 用户不安装更新,制造商不担责(FAQ 4.3.3,官方解释)。

---

## 10. 技术文档与合规证据

| 项 | 要求 | 依据(【法规】Fact) |
|---|---|---|
| 技术文档内容 | Annex VII:产品总体描述(预期用途、影响合规的软件版本、Annex II 用户说明);设计开发与**漏洞处理过程**(含 **SBOM、CVD policy、漏洞报告联系地址证据、安全更新分发技术方案**);生产与监控过程;网络安全风险评估(Art 13(3));support period 确定依据;所用 harmonised standards/共同规范/认证方案清单(未用须说明替代方案);**测试报告**;EU DoC 副本;SBOM(MSA 合理请求时提供) | Art 31 + Annex VII |
| 编制与更新 | 上市前编制,support period 内持续更新 | Art 31(2) |
| EU declaration of conformity | 符合性评估通过后签署,随产品提供副本或简化版(含全文网址) | Art 28、13(20) |
| CE marking | 表明产品与制造商流程符合 Annex I | Art 30、Art 3(31) |
| 保留期限 | 技术文档 + EU DoC:**上市后至少 10 年或 support period,取较长者**;用户说明同样 10 年/支持期;进口商留 DoC 副本同期 | Art 13(13)(18)、18(3)、19(6) |
| FOSS 特例 | FOSS 的 Annex III 产品走 Module A 自评的前提:**技术文档向公众公开** | Art 32(5) |

---

## 11. 实施时间线

| 日期 | 事件 | 依据 |
|---|---|---|
| 2024-10-23 | 签署 | 文本落款(Fact) |
| 2024-11-20 | OJ 公布 | OJ L, 2024/2847(Fact) |
| **2024-12-10** | **生效**(Art 71(1));delegated powers 起算 | 【法规】 |
| 2025-02-03 | M/606 标准化请求(C(2025)618,41 个标准) | 【官方解释】Commission 标准页 |
| 2025-04-03 | CEN/CENELEC/ETSI 接受 M/606 | 【标准/实践】CEN-CENELEC 新闻 |
| 2025-12-03 | Commission "FAQs on the CRA Implementation" v1.0 | 【官方解释】 |
| 2025-12-11 | Art 7(4) Annex III/IV 技术描述 implementing act 截止;Art 14(9) PEC delegated act 通过(已落地) | 【法规】+【官方解释】ENISA FAQ #21 |
| 2026-06-11 | Chapter IV(Art 35–51,notified body 体系)适用 | 【法规】Art 71(2) |
| 2026-07-27 | Commission 实施 guidance C(2026) 5252 发布 | 【官方解释】 |
| **2026-09-11** | **Art 14 报告义务适用;ENISA SRP 上线** | 【法规】Art 71(2)+【官方解释】 |
| 2026-08-30 / 10-30 | M/606 原定:horizontal(含 vulnerability handling)/ vertical 标准交付(二手来源称已顺延约 2 个月,(不确定)) | 【官方解释】FAQ 6.8 /【标准/实践】 |
| 2027-10-30 | M/606:Annex I Part I 产品属性标准 | 同上 |
| **2027-12-11** | **主体义务全部适用**(Annex I、Art 13 等);OSS steward 报告义务起算;此前上市产品原则上不适用(除非 substantial modification),**但 Art 14 例外覆盖存量产品**(Art 69(3)) | 【法规】 |
| 2028-06-11 | 其他欧盟法规下已发 EU type-examination 证书过渡期满 | Art 69(1) |
| 2028-09-11 前 | Commission 评估 SRP 有效性报告 | Art 70(2) |
| 2030-12-11 | 首次全面评估审查报告 | Art 70(1) |

**Presumption of conformity 现状**:Art 27 机制本身已在,但【标准/实践】截至 2026-07 无任何 CRA harmonised standard 获 OJ 引用, presumption 通道实际不可用(二手,见 [sources/secondary-standards-status.md](02-cra-regulation/sources/secondary-standards-status.md),(不确定但以官方 OJ 公告为准前按此理解))。

---

## 12. 罚则(Art 64)

| 违反对象 | 罚款上限 | 条款 |
|---|---|---|
| **Annex I 基本要求、Art 13(制造商义务)、Art 14(报告义务)** | **€15M 或全球年营业额 2.5%(取高)** | Art 64(2) |
| Art 18–23(授权代表/进口商/分销商等)、28(DoC)、30(1)-(4)(CE)、31(1)-(4)(技术文档)、32(1)-(3)(符合性评估)、33(5)、39、41、47、49、53 | €10M 或 2% | Art 64(3) |
| 向 notified body/MSA 提供错误、不完整、误导性信息 | €5M 或 1% | Art 64(4) |

豁免(Art 64(10)):① 小微企业未赶上 Art 14 **24h early warning** 时限不罚款(72h 等其他时限不在豁免内);② **OSS steward 的任何违反不罚款**。

非罚款类风险(【法规】Fact):
- MSA 措施(Art 52–58):要求整改、**召回(recall)、撤回(withdrawal)、限制/禁止上市**(Art 54;Art 57 对"合规但仍有重大风险"产品也可要求措施);
- 委员会层面:Art 56(9) 例外情形下可通过 implementing act 在全欧盟要求撤回/召回;
- 集体诉讼:Art 65 适用 Directive 2020/1828;
- 罚款可与其他纠正/限制措施叠加(Art 64(9))。

### 12.1 执法架构:不存在"CRA 机构审计",是三条独立的线(2026-09-19 补充)

CRA 是 NLF 产品法,**没有中央"CRA 局"做定期审计**,执法由三条线构成(【法规】Fact + Interpretation):

**线一:Market Surveillance Authorities(MSA)——真正的执法者。** 各成员国指定的国家级市场监管机构(非欧盟层面机构),依据 Regulation 2019/1020 行使权力:要求提供技术文档/SBOM/证据(Annex VII 第 8 项)→ 评估 → 要求纠正 → 不合规则罚款(成员国执行,Art 64)、召回/禁售(Art 52–58)。触发方式是**被动**的:Art 14 报告、ADCO 协调抽查、投诉、公开漏洞事件。**大多数自我评估(Module A)产品不会"被审计",直到 MSA 敲门。**

**线二:Notified Bodies——第三方存在,但性质是"上市前合格评定"而非"受委托审计"。** 仅对 Annex III/IV(important/critical)产品强制(Art 32(2)(3));由制造商**自行聘请**做上市前评估(Module B+C / H),不是监管机构委托的事后检查。注意现实问题:协调标准至今无 OJ 引用(§11),Class I 产品的标准自评路径不可用,实务上可能被动推向第三方评估;notified body 的成员国指定也仍在进行中。

**线三:ENISA / CSIRT——只收报告,不审计。** Art 14 报告经 ENISA single reporting platform 送达指定 CSIRT + ENISA(§6),角色是事件通报与态势感知;不评判合规性,但报告记录会成为 MSA 的线索来源。

```text
上市前:Notified Body 第三方评估 —— 仅 Annex III/IV,厂商自聘,一次性大考
          ↓ 产品上市
上市后:MSA(成员国) —— 被动触发、调证据、罚款/召回,10 年留存期内随时可能来
          ↑ 线索来自
事件通报:ENISA SRP + CSIRT —— Art 14 报告(已生效) + 投诉/抽查/ADCO
```

**推论:"能力弱 → 审计预警"的理解需要修正(Interpretation)。** CRA 的义务结构是流程义务 + 事件触发,没有"能力考试":Part II(3) 的"定期有效的安全测试"是相对企业自身风险评估的要求(Art 13(2)),不是绝对能力标准;Part I(2)(a) 只要求无"**已知**"可利用漏洞。真实风险链条是:工具/团队能力弱(本身不违法)→ 漏洞发现不了/处理没记录/修复没验证 → 漏洞被在野利用或被公开 → Art 14 的 24h 时钟启动 + MSA 调证 → **"拿不出流程在运行的证据"才是罚款落点**。CRA 罚的不是能力弱,是出事后无可辩护的流程证据——这正是"可辩护性优先于扫描覆盖率"产品定位的法规依据(见 [00-final-report](00-final-report.md) §1.2)。

**对产品的含义(Recommendation):** 平台要服务两种形态截然不同的"审计场景":① 上市前向 notified body 举证(Annex III/IV 客户,一次性大考,重文档完整性);② 上市后随时应对 MSA 调证(所有客户,10 年留存期,重证据可追溯与快速导出)。Evidence Graph 的导出形态需同时覆盖两者。

---

## 13. 重要/关键产品分类与符合性评估路径

### 13.1 分类(【法规】Fact)

- **Important products(Art 7 + Annex III)**:
  - **Class I(19 类)**:身份管理与 PAM、独立与嵌入式浏览器、密码管理器、**杀毒/恶意软件查杀软件**、VPN、网络管理系统、**SIEM**、boot manager、PKI/证书签发、物理与虚拟网络接口、**操作系统**、路由器/调制解调器/交换机、安全微处理器/微控制器/ASIC/FPGA、智能家居虚拟助手、带安全功能的智能家居产品(智能门锁、安防摄像头、婴儿监控、报警系统)、联网玩具、健康监测/儿童可穿戴。
  - **Class II(4 类)**:hypervisor 与容器运行时、**防火墙与 IDS/IPS**、防篡改微处理器、防篡改微控制器。
  - 集成一个 important 产品**不会**使集成产品自动变为 important(Art 7(1) 第二句)。
- **Critical products(Art 8 + Annex IV,3 类)**:hardware devices with security boxes;smart meter gateways 等高级安全/加密处理设备;智能卡/secure elements。Commission 可通过 delegated act 强制其获得 EUCC 等认证方案至少 'substantial' 级证书。

### 13.2 符合性评估路径(Art 32,【法规】Fact)

| 产品类别 | 默认路径 | 说明 |
|---|---|---|
| 默认产品(不在 Annex III/IV) | **Module A 内部控制自评** | 可选更严路径;即使不用标准也可自评 |
| Important Class I | 完整适用 harmonised standards/共同规范/EUCC(substantial+)→ 仍可自评;**未(完整)适用 → 须第三方**(Module B+C 或 H) | Art 32(2) |
| Important Class II | **始终须第三方**(B+C / H / EUCC substantial+) | Art 32(3) |
| Critical(Annex IV) | EUCC 认证(Art 8(1) 触发时);否则按 Art 32(3) | Art 32(4) |
| FOSS 且属 Annex III | **可用 Module A 自评**,前提:技术文档上市时向公众公开 | Art 32(5) |

**对"安全厂商的客户是谁"的含义**(Interpretation):杀毒软件、SIEM、防火墙/IDS/IPS、VPN、操作系统、密码管理器等**安全产品本身就在 Annex III 里**——安全厂商自身首先是 CRA 的合规对象(且多在 Class I/II,可能需第三方评估);同时所有制造商都需要漏洞全生命周期能力来满足 Annex I Part II 与 Art 14——两条需求线并存。

---

## 14. 核心交付:CRA Article/Annex → Obligation → Security Activity → Product Capability 映射表

> 用途:从法规义务反推"CRA + SCA 漏洞全生命周期产品"的能力清单。Security Activity 是制造商必须做的安全动作;Product Capability 是我们产品可承接的能力(属【厂商实现】层推论,非法律要求)。共 **46 行**。

| # | Article/Annex | Obligation(法规要求) | Security Activity(安全活动) | Product Capability(产品能力) |
|---|---|---|---|---|
| 1 | Art 2(1), 3(1)(2) | 判定产品是否在 CRA 范围 | 适用范围判定(含 remote data processing 判定) | 范围评估问卷/判定器(SaaS vs 产品组件分流) |
| 2 | Art 7, 8, Annex III/IV | 判定产品分类(默认/Class I/II/Critical) | 产品分类判定 | Annex III/IV 分类器 → 决定评估路径 |
| 3 | Art 32 | 选择并执行符合性评估路径 | 自评(Module A)或第三方评估管理 | 合规路径向导、评估证据包生成 |
| 4 | Art 13(2)(3) | 网络安全风险评估并文档化、支持期内更新 | 威胁建模、风险评估、适用范围裁剪(Part I 哪些适用) | 风险评估模块、Annex I 适用性裁剪工作流 |
| 5 | Art 13(4), 31, Annex VII | 编制并持续更新技术文档 | 合规文档编制与版本化 | 技术文档自动生成(模板+证据聚合) |
| 6 | Annex VII 2(b) | 文档中含 SBOM、CVD policy、联系地址证据、更新分发方案 | 证据归集 | 证据库(SBOM/策略/记录统一存档) |
| 7 | Annex VII 6 | 测试报告入档 | 安全测试执行与报告归档 | SAST/DAST/渗透测试集成与报告导出 |
| 8 | Art 28, 30 | 签署 EU DoC、加贴 CE | 声明签署流程、CE 标识管理 | DoC 生成器、签署工作流 |
| 9 | Art 13(13), 18(3), 19(6) | 文档与 DoC 保留 10 年或支持期(取长) | 长期归档与检索 | 合规档案库(保留期策略自动化) |
| 10 | Art 13(22), Annex VII 8 | 应 MSA 合理请求提供全部合规信息与 SBOM | 监管请求响应 | 一键导出监管证据包(含 SBOM) |
| 11 | Annex I Part II(1) | 识别并记录组件与漏洞;绘制机读 SBOM(至少顶层依赖) | 组件识别、依赖分析、SBOM 生成与维护 | **SCA 引擎、SBOM 生成器(CycloneDX/SPDX)、SBOM 版本化** |
| 12 | Annex I Part II(1) + Art 13(24) | SBOM 采用 Commission 规定的格式与要素 | 跟踪 SBOM 格式 implementing act | SBOM 格式合规校验器(随法案更新) |
| 13 | Art 13(5), Recital 34 | 第三方/FOSS 组件 due diligence | 组件准入审查(CE、更新历史、EUVD/CVE 查询、附加测试) | 组件准入评估引擎(更新活跃度、已知漏洞、许可证) |
| 14 | Art 13(6) | 组件漏洞上报维护者并共享补丁 | 上游协调披露、补丁回流 | 上游报告工作流(自动生成组件方报告)、补丁共享记录 |
| 15 | Art 13(7) | 系统记录已知漏洞与第三方通报,更新风险评估 | 漏洞台账、风险重估 | 漏洞知识库(产品维度)、风险登记册联动 |
| 16 | Annex I Part I(2)(a) | 上市时无已知可利用漏洞 | 发布前漏洞扫描 + 可利用性判定 | 发布门禁(release gate):SCA 扫描 + KEV/EPSS 可利用性分级 |
| 17 | Annex I Part I(2)(b) | secure by default + 可重置 | 默认配置基线设计 | 安全基线库、配置漂移扫描 |
| 18 | Annex I Part I(2)(c) | 默认自动更新 + opt-out + 通知 + 暂缓 | 更新机制设计验证 | 更新机制合规检查清单/验证工具 |
| 19 | Annex I Part I(2)(j)(k) | 限制攻击面、exploit 缓解 | 攻击面分析、缓解措施验证 | 攻击面盘点工具、二进制缓解 flag 检查 |
| 20 | Annex I Part I(2)(l) | 安全相关内部活动记录监控(opt-out) | 日志与审计功能 | 日志能力合规检查 |
| 21 | Annex I Part II(2) | 无延迟处理修复漏洞;安全/功能更新分离(可行时) | 漏洞分流、修复 SLA、更新通道管理 | 漏洞修复工作流(SLA 计时)、更新包分类标记 |
| 22 | Annex I Part II(3) | 定期有效安全测试与评审 | 周期性安全测试计划 | 持续测试调度与合规记录 |
| 23 | Annex I Part II(4) | 修复后公开披露漏洞信息(可延迟) | 安全公告编写与发布、CVE 申请 | Advisory 生成器、CVE/CNA 对接、披露时间管理 |
| 24 | Annex I Part II(5), Art 13(8) 末段 | 制定并执行 CVD policy | 协调披露流程运营 | VDP 平台/security.txt 生成、披露时间线跟踪 |
| 25 | Annex I Part II(6), Art 13(17) | 漏洞报告联系地址 + SPOC(不限于自动化工具) | 漏洞接收渠道运营 | 漏洞收件箱(intake)、人工响应 SLA 跟踪 |
| 26 | Annex I Part II(7) | 安全分发更新机制 | 更新签名与分发安全 | 更新签名/验证机制审计 |
| 27 | Annex I Part II(8) | 安全更新免费、无延迟、附 advisory | 更新发布管理 | 更新发布流水线合规检查(免费性、及时性) |
| 28 | Art 13(9) | 安全更新发布后可用 ≥10 年或剩余支持期(取长) | 更新长期归档 | 更新归档库与可用性监控 |
| 29 | Art 13(10), Recital 40 | 只对最新版本修复的前提:老用户免费升级 | 版本支持策略管理 | 版本支持矩阵管理 |
| 30 | Art 13(8), Annex VII 4 | 确定 support period(≥5 年或预期使用期)并记录依据 | EOL/EOS 策略制定 | Support period 计算与文档化工具 |
| 31 | Art 13(19), Annex II 7 | 购买时标明支持期结束日期;到期通知用户 | EOL 通知运营 | EOL 日期登记、自动到期通知 |
| 32 | Art 13(21) | 知悉不合规立即纠正/撤回/召回 | 纠正措施管理(CAPA) | 纠正措施跟踪、召回决策支持 |
| 33 | Art 14(1)(2) | AEV:24h early warning → 72h notification → 修复后 14 天 final report | 24/72h 应急响应、监管报告撰写 | **CRA 报告工作台:awareness 时间戳、倒计时、分阶段表单(SRP 字段映射)** |
| 34 | Art 14(3)(4)(5) | Severe incident:24h → 72h → 1 个月 final report | 事件分级(是否符合 Art 14(5) 严重标准) | 事件分级向导、incident 报告工作台 |
| 35 | Art 3(42), Recital 68 | 判定"actively exploited"(可靠恶意利用证据) | 在野利用确认 | 威胁情报集成(CISA KEV、EUVD、厂商情报)辅助判定 |
| 36 | Art 14(7) | 选对 CSIRT(主要机构所在地/备选顺序) | 报告管辖区判定 | CSIRT 选择器、SRP 提交指引 |
| 37 | Art 14(8) | 通知受影响用户(结构化机读) | 受影响用户识别与通知 | 受影响版本/用户范围分析(SBOM 反查)、通知模板 |
| 38 | Art 15 | 自愿报告(漏洞/威胁/事件/near miss) | 自愿情报共享 | 自愿报告通道(SRP 上线后) |
| 39 | Art 16(2), Art 14(2) 敏感度标注 | 标注信息敏感度;PEC 延迟分发请求 | 分发敏感性评估 | 敏感度标记与 PEC 请求工作流 |
| 40 | Art 17(5) | 修复后漏洞纳入 EUVD(经制造商同意) | EUVD 对接 | EUVD/CVE 编号映射管理 |
| 41 | Art 19(5), 20(4) | 进口商/分销商发现漏洞通知制造商;重大风险通知 MSA | 渠道漏洞通报 | 供应链协同门户(进口商/分销商上报入口) |
| 42 | Art 24(1) | (steward)可验证的 cybersecurity policy | 开源项目安全治理 | Steward policy 文档生成与验证(基金会客户) |
| 43 | Art 24(3)(2027-12-11 起) | (steward)有限范围 Art 14 报告 | steward 报告流程 | steward 报告模式(与制造商不同入口) |
| 44 | Art 13(5) + Art 25 | 利用自愿性 FOSS security attestation 简化 due diligence | attestation 结果采信 | attestation 注册表查询集成 |
| 45 | Art 69(2)(3) | 存量产品:仅 Art 14 适用;substantial modification 触发全面适用 | 存量产品台账、实质性修改判定 | 存量产品登记、修改性质判定向导 |
| 46 | Art 26(2), 27, M/606 | 跟踪 guidance、harmonised standards、presumption of conformity | 法规与标准动态跟踪 | 法规雷达(标准引用/法案更新推送) |

---

## 15. 与大众理解有出入的关键发现

1. **SaaS 基本不适用 CRA**。CRA 只管"产品+其 remote data processing";独立 SaaS/PaaS/IaaS 由 NIS2 管辖(Recital 12)。市面上"CRA 覆盖所有软件服务"的说法是错的——只有缺了它产品功能就残缺的厂商自有云后端才随产品落入 CRA。
2. **SBOM 不要求公开**。法规要求"识别记录组件+绘制机读 SBOM(至少顶层依赖)",但 Recital 明确"不应强制公开 SBOM";只有 MSA 合理请求核查合规、或 ADCO 依赖评估时才须向监管提供。对用户公开是可选项(Annex II 9)。
3. **开源豁免的真实边界是"商业活动中的供应",不是"是否收钱"那么简单**:未 monetise 的 FOSS 供应(哪怕接受捐赠、有厂商参与、定期发版)不算商业活动;但一旦被 monetise(含卖订阅支持),同一项目可能瞬间落入 manufacturer 义务。而 steward(基金会等)是独立轻量角色:不贴 CE、不罚款、报告义务 2027 年底才开始。
4. **Art 14 报告义务对存量产品也适用**(Art 69(3))——2027-12-11 前上市的老产品虽不需满足 Annex I,但从 2026-09-11 起其 actively exploited vulnerability / severe incident 一样要 24h/72h 报告。同时 Commission 明确:**未被恶意利用的零日不触发报告**,CRA 也**不强制主动威胁监控**("知悉即报"而非"必须去发现")。
5. **不要求修补所有漏洞,也不要求产品无漏洞**:上市门禁只针对"已知+可利用"漏洞;支持期内按风险决定补救形式(可以是 advisory、禁用功能,甚至仅记录)。"CRA = 所有 CVE 都必须打补丁"是过度解读(Commission FAQ 4.2.1/4.3.1)。
6. (附加)**Class II 安全产品永远需要第三方评估**:防火墙、IDS/IPS、hypervisor、容器运行时——没有"用了标准就能自评"的通道(Art 32(3))。而 Class I(操作系统、杀毒、SIEM、VPN、密码管理器)只有在完整采用协调标准/认证时才能自评;目前 OJ 尚无标准引用,意味着实务上 Class I 当前也走第三方(二手,(不确定))。

---

## 附:来源清单(对应 [sources/](02-cra-regulation/sources/) 目录)

| Note | 层级 | 支撑章节 |
|---|---|---|
| [eur-lex-reg-2024-2847-fulltext.md](02-cra-regulation/sources/eur-lex-reg-2024-2847-fulltext.md) | 法规原文 | §1–§13 全部 |
| [commission-faqs-cra-implementation.md](02-cra-regulation/sources/commission-faqs-cra-implementation.md) | 官方解释 | §1、§3–§9、§11、§13、§15 |
| [enisa-cra-srp-faq.md](02-cra-regulation/sources/enisa-cra-srp-faq.md) | 官方解释 | §2、§6、§11 |
| [commission-cra-page.md](02-cra-regulation/sources/commission-cra-page.md) | 官方解释 | §1、§11 |
| [commission-cra-standardisation.md](02-cra-regulation/sources/commission-cra-standardisation.md) | 官方解释/标准组织 | §11、§13 |
| [secondary-standards-status.md](02-cra-regulation/sources/secondary-standards-status.md) | 二手解读 ⚠️ | §11、§13、§15(均已标注) |

原始抓取件:[sources/raw/](02-cra-regulation/sources/raw/)(EUR-Lex 英文全文 txt/html、Commission FAQ md/pdf)。
