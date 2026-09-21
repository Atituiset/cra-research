# 05 — CRA 与既有欧盟产品合规体系的关系:CE/NLF 全景、RED 衔接与法规边界

> 研究日期:2026-09-19 | 研究者:补充调研子任务
> 配套材料:每条重要结论对应 [05-eu-compliance-landscape/sources/](05-eu-compliance-landscape/sources/) 下一条 source note;检索过程见 [05-eu-compliance-landscape/research-log.md](05-eu-compliance-landscape/research-log.md)。
> 标注体系沿用 [02 报告](02-cra-regulation.md):**Fact**(条文/官方页直接载明)/**Interpretation**(基于文本的合理推论)/**Hypothesis**(假设,需进一步核实)。
>
> ⚠️ 抓取说明:与 [02 报告](02-cra-regulation.md)不同,本次 eur-lex.europa.eu 直连**未被 AWS WAF 拦截**,所有 EUR-Lex 法规文本均为 2026-09-19 直连一手抓取,不再需要 Wayback 存档。此前"带 utm_source=chatgpt.com 的 EUR-Lex 链接疑似 AI 转述"的存疑点,已通过官方一手来源逐条核实(见 §1)。

---

## 0. 头条结论:Delegated Regulation (EU) 2026/339 核实结果——**成立**

线索声称:欧盟已通过 Delegated Regulation (EU) 2026/339,自 2027-12-11 起废止 RED 网络安全授权法规 EU 2022/30,理由是 CRA 全面适用后 Annex I 已覆盖其网络安全要求。

**核实结论:成立。** 该法规真实存在,已通过 EUR-Lex 官方一手文本逐点核实(抓取日期 2026-09-19):

| 线索要素 | 核实结果 | 证据 |
|---|---|---|
| Delegated Regulation (EU) 2026/339 存在 | ✅ 成立 | EUR-Lex ELI 官方页:OJ L, 2026/339, 29.4.2026 |
| 标题为废止 EU 2022/30 | ✅ 成立 | 标题原文:"Commission Delegated Regulation (EU) 2026/339 of 16 February 2026 **repealing Delegated Regulation (EU) 2022/30**" |
| 通过日期 | ✅ 2026-02-16(布鲁塞尔,Von der Leyen 签署);OJ 公布 2026-04-29;依 Art 2 于公布后第 20 日(**2026-05-19**)生效 | 法规落款与 Art 2 |
| 废止生效日 2027-12-11 | ✅ 成立 | Art 1 原文:"Delegated Regulation (EU) 2022/30 is repealed **with effect from 11 December 2027**"——即 CRA(Regulation (EU) 2024/2847)全面适用之日 |
| 理由:CRA Annex I 覆盖 RED 网络安全要求、避免重复监管 | ✅ 成立 | Recital (3):CRA Annex I "include **all the elements** of the essential requirements referred to in Article 3(3), points (d), (e) and (f), of Directive 2014/53/EU";Recital (4):为避免无线电设备"simultaneously subject to requirements also concerning cybersecurity",须自 CRA 全面适用之日起废止 2022/30 |

独立佐证:EFTA EEA-Lex factsheet(32026R0339)、TÜV、Omnilex、ANACOM(葡萄牙通信管理局)等多方转载同一文本,编号/日期/措辞一致。线索链接虽带 `utm_source=chatgpt.com`(说明检索者经 AI 转述获得链接),但链接指向的法规本身**真实且内容吻合**。

来源:[sources/eur-lex-reg-del-2026-339.md](05-eu-compliance-landscape/sources/eur-lex-reg-del-2026-339.md)(一手,EUR-Lex 直连)

---

## 1. 被废止的是什么:EU 2022/30 的准确内容与 RED 边界

### 1.1 EU 2022/30 事实卡(【一手法规】Fact)

- **全称**:Commission Delegated Regulation (EU) 2022/30 of 29 October 2021,supplementing Directive 2014/53/EU(RED)with regard to the application of the essential requirements referred to in Article 3(3), points (d), (e) and (f)。
- **法律机制**:RED Art 3(3) 自 2014 年起就载有三项"dormant"essential requirements,须由 Commission 以 delegated act 激活;2022/30 即该激活法案。
- **适用日期变迁**:原 Art 3 定 2024-08-01 适用;因协调标准(EN 18031 系列)未及就绪,由 Delegated Regulation (EU) **2023/2444**(2023-07-20)修正为 **2025-08-01** 适用,并更正了 Art 1(2) 的数据表述错误。
- **三类要求与适用设备类别**(Art 1):
  - **Art 3(3)(d) 网络保护**——"radio equipment does not harm the network or its functioning nor misuse network resources, thereby causing an unacceptable degradation of service"→ 适用于一切 **internet-connected radio equipment**(直接或经中间设备联网);
  - **Art 3(3)(e) 个人数据与隐私保护**→ 适用于能处理 GDPR 个人数据或 ePrivacy 流量/位置数据的:internet-connected 设备、**childcare 专用设备、玩具指令(2009/48/EC)覆盖设备、wearable 设备**(后三类即使不联网也适用);
  - **Art 3(3)(f) 防欺诈**→ 适用于 internet-connected 且**支持转账/货币价值/虚拟货币转移**的设备。
- **部门法豁免**(Art 2):适用 MDR(2017/745)/IVDR(2017/746)的无线电设备**完全豁免**;适用民航(2018/1139)、机动车(2019/2144)、电子道路收费(2019/520)的设备仅豁免 (e)(f) 两项。
- **协调标准**:EN 18031-1/2/3:2024 由 Implementing Decision (EU) 2025/138 于 **2025-01-30 在 OJ 引用(带限制)**,覆盖 (d)/(e)/(f) 三项。

来源:[sources/eur-lex-reg-del-2022-30.md](05-eu-compliance-landscape/sources/eur-lex-reg-del-2022-30.md)、[sources/eur-lex-reg-del-2023-2444.md](05-eu-compliance-landscape/sources/eur-lex-reg-del-2023-2444.md)、[sources/red-en-18031-oj-citation.md](05-eu-compliance-landscape/sources/red-en-18031-oj-citation.md)

### 1.2 废止的边界:RED 本体不受影响(【一手法规】Fact)

2026/339 废止的**只是 RED 下的网络安全 delegated act(2022/30)**。RED 2014/53/EU 本体的其余 essential requirements——Art 3(1)(a) 健康与安全(承接 LVD)、Art 3(1)(b) EMC、Art 3(2) 频谱有效利用——不在 2022/30 范围内,自然也不受 2026/339 影响。无线电设备 2027-12-11 之后:频谱/安全/EMC 仍走 RED 合规,网络安全改走 CRA。一台联网无线电设备将同时持有两套法规下的合规义务(可合并为单一 EU DoC,见 §3.3)。

### 1.3 过渡期衔接(2026/339 Recital (5),Fact)

废止**不溯及既往**:对 2025-08-01 至 2027-12-10 之间上市、受 2022/30 约束的无线电设备,成员国仍可依 RED 就其是否符合 Art 3(3)(d)(e)(f) 开展市场监督。即 RED 网络安全义务在其存续期内(约 2 年 4 个月)完整执法,与 CRA 无缝接力。

---

## 2. 欧盟产品合规体系全景:CE marking 与 New Legislative Framework

### 2.1 CE marking 的法律本质(【官方】Fact)

CE marking **不是单一法规的认证标志**,而是制造商声明产品满足**所有适用 EU 协调法规**全部要求的标志;加贴 CE 后即可在整个 EEA 自由流通。官方明确:"a CE marking does not indicate that a product have been approved as safe by the EU or by another authority"——CE 是**制造商自我声明**(必要时含第三方评估),不是政府批文。

### 2.2 New Legislative Framework(NLF)三件套(【官方】Fact)

2008 年通过的 NLF 是 EU 产品法的横向"操作系统":

- **Regulation (EC) No 765/2008**:accreditation(合格评定机构认可)与 market surveillance 的要求;
- **Decision No 768/2008/EC**:产品立法的**共同工具箱与模板**(reference provisions),统一定义、经营者义务、合格评定程序(Modules)、EU DoC、CE marking 规则——后续产品法逐部对齐;
- **Regulation (EU) 2019/1020**:市场监督与产品合规(含 Union Product Compliance Network、ADCO 合作机制)。

Commission 官方 NLF 对齐立法清单共 31 部,**RED(2014/53/EU)为第 14 项,Machinery Regulation(2023/1230)第 26 项,AI Act 第 28 项,CRA(2024/2847)第 29 项**。即 CRA 不是孤立的网络安全立法,而是标准 NLF 产品法家族的最新成员——这决定了它采用 NLF 的标准流程(技术文档 → 合格评定 → EU DoC → CE → 市场监督)。

来源:[sources/commission-nlf-page.md](05-eu-compliance-landscape/sources/commission-nlf-page.md)、[sources/commission-ce-marking-page.md](05-eu-compliance-landscape/sources/commission-ce-marking-page.md)

### 2.3 Harmonised standards → presumption of conformity(【法规】Fact)

NLF 机制的核心激励:制造商不必自己证明符合 essential requirements,只需遵循已在 OJ 引用(harmonised)的标准,即获得 **presumption of conformity**(CRA **Art 27**;一般机制由 Regulation (EU) No 1025/2012 第 10 条支撑:Commission 向 CEN/CENELEC/ETSI 发出标准化请求,ESO 制定标准,Commission 评估后在 OJ 公布引用方生效)。

CRA 下的进展(更新 [02 报告](02-cra-regulation.md) §11,截至 2026-09):

- M/606(C(2025)618,2025-02-03)41 个标准,ESO 已于 2025-04 接受([02 报告](02-cra-regulation.md)已述);
- **截至 2026-08 下旬,仍无任何 CRA 协调标准在 OJ 获得引用**,presumption of conformity 对所有产品类别暂不可用(多个独立二手来源一致);
- 新进展:ETSI 于 **2026-08-13 对 17 个 vertical 标准启动批准程序**(enquiry,2026-09 中至 11 月中截止);首批标准交付预期 2026 下半年,OJ 引用时间表 Commission 仍未公布。
- 对照 RED:2022/30 也因标准延迟被迫延期一年(见 §1.1),EN 18031 在适用前 6 个月才获 OJ 引用——**CRA 极可能重演"义务先行、标准后到"的窗口期**(Interpretation)。

来源:[sources/cra-standards-status-2026.md](05-eu-compliance-landscape/sources/cra-standards-status-2026.md)

### 2.4 标准合规流程(【官方】Fact)

NLF 家族产品的标准路径:**识别适用法规与 essential requirements → 编制 technical documentation → conformity assessment(默认 Module A 内部生产控制自评;高风险类别强制第三方 notified body)→ 签署 EU Declaration of Conformity → 加贴 CE marking → 上市**。CRA 完全沿用此路径:Art 31(技术文档,Annex VII)、Art 32(合格评定程序)、Art 28(EU DoC,Annex V)、Art 29/30(CE 一般原则与加贴规则)。

---

## 3. CRA 与其他 EU 法规的边界(Art 2 及 recitals)

### 3.1 CRA vs NIS2:SaaS/云的分工(【法规】Fact,补充 [02 报告](02-cra-regulation.md) §1.2 的条文依据)

CRA Recital 12(即 [02 报告](02-cra-regulation.md)已引)明确:"Directive (EU) 2022/2555 applies to cloud computing services and cloud service models, such as **SaaS, PaaS or IaaS**"。接口规则:

- 独立 SaaS/云服务 → **NIS2**(中型及以上实体);
- 只有构成产品功能的 **remote data processing**(CRA Art 3(2),如智能家居厂商的远程控制云)才随产品落入 CRA;
- 不支持产品功能的纯网站、制造商责任范围之外开发的云服务 → 均不在 CRA 范围。

两法分工的逻辑:**NIS2 管"实体/服务运营"(entity-based),CRA 管"产品上市"(product-based)**(Interpretation)。CRA 还通过修订 Regulation (EU) 2019/1020 接入 NLF 市场监督体系(见 CRA 标题"amending Regulations (EU) No 168/2013 and (EU) No 2019/1020")。

### 3.2 Lex specialis 排除与限制条款(CRA Art 2,【法规】Fact)

| 条款 | 排除对象 | 依据 |
|---|---|---|
| Art 2(2) | 适用 **MDR 2017/745、IVDR 2017/746、机动车 2019/2144** 的产品 | 部门法已含网络安全要求 |
| Art 2(3) | 经 **民航 2018/1139** 认证的产品 | 同上 |
| Art 2(4) | 适用**船用设备 Directive 2014/90/EU** 的设备 | 同上 |
| Art 2(6) | 同规格替换用 spare parts | 避免对备件重复评定 |
| Art 2(7) | 专为国家安全/防务开发或处理涉密信息的产品 | 安全豁免 |

**关键弹性条款 Art 2(5)**:对"被其他 EU 规则覆盖、且该规则能达到 CRA **同等或更高保护水平**"的产品,Commission 可依 Art 61 以 delegated act **限制或排除** CRA 的适用。这是 CRA 预留的通用防重复监管阀门——2026/339 废止 RED 2022/30 即同一逻辑的 RED 侧实现(Interpretation)。

### 3.3 Machinery Regulation (EU) 2023/1230:不排除,而是叠加(【法规】Fact)

- MR **2027-01-20 全面适用**(原 OJ 文本误印 2027-01-14,经 2023-07-04 OJ L 169 corrigendum 更正),同日废止 Directive 2006/42/EC,无过渡期(已在市场上的存量不受影响)。
- **同时落入 MR 与 CRA 的机械产品须同时符合两法**(CRA recital,见 [sources](05-eu-compliance-landscape/sources/)):MR Annex III 1.1.9(防控制系统篡改/protection against corruption)与 1.2.1(控制系统安全可靠)与 CRA Annex I 可能覆盖相似网络安全风险;CRA 合规可**facilitate** MR 合规,但协同须由制造商举证(如借助协调标准),并须分别走完两法的合格评定程序。Commission 承诺发布专项 guidance。
- 交叠处理(Interpretation):2027 年出现一个紧凑窗口——MR 2027-01-20 适用,CRA 2027-12-11 全面适用,期间上市的联网机械产品先满足 MR 网络安全相关条款,年底再叠加 CRA 全套义务;两法标准化进程被要求相互对齐。

来源:[sources/eur-lex-machinery-reg-2023-1230.md](05-eu-compliance-landscape/sources/eur-lex-machinery-reg-2023-1230.md)、[sources/cra-art2-art27-recitals.md](05-eu-compliance-landscape/sources/cra-art2-art27-recitals.md)

### 3.4 RED 设备在 CRA 下的地位与监管衔接(【法规】Fact + Interpretation)

- 无线电设备**本身完全落入 CRA 范围**(CRA 无任何条款排除 radio equipment);CRA recital 明确预见 2022/30 将被废止,并要求 CRA 协调标准吸收 RED 标准化请求 C(2022)5637(即 EN 18031 的技术成果)。
- 衔接时间线:**2025-08-01** RED 网络安全义务适用(2022/30)→ **2026-05-19** 2026/339 生效(废止决定本身)→ **2027-12-11** 2022/30 废止生效 = CRA 全面适用,同日 RED 网络安全义务退场。
- 2025-08-01 至 2027-12-10 期间上市的设备:RED (d)(e)(f) 义务存续且可被市场监督追溯(2026/339 Recital (5));**2027-12-11 起新上市设备只按 CRA 做网络安全合规**。

### 3.5 核心论点:从"产品属性"到"全生命周期"的义务演进(Interpretation,本章结论)

RED 2022/30(经 EN 18031)是**产品属性导向**:设备须具备网络保护、数据隐私、防欺诈三类静态特性,证明方式是一次性的合格评定(自评或 notified body)。CRA Annex I 则是**属性 + 流程的双层结构**:Part I 是产品属性要求(覆盖并超出 RED 三类要素),Part II 是**贯穿 support period 的漏洞处理流程义务**(vulnerability handling、安全更新、Art 14 主动报告、Annex VII 技术文档中的 SBOM 与证据留存)。2026/339 的废止逻辑(recital (3)"Annex I includes all the elements")在法律上确认:**CRA 不是 RED 网络安全义务的平移,而是将其吸收进一个以漏洞全生命周期为中心的更宽义务框架**。对产品设计的意义:合规资产从"上市时的一次性证书"变为"持续产生的证据流"——这正是漏洞全生命周期平台的机会所在。

---

## 4. 对产品边界的影响:证据链如何嵌入 conformity assessment

### 4.1 完整合规链条(【法规】Fact)

```
technical documentation (Art 31, Annex VII:产品描述/设计开发/SBOM/漏洞处理流程/测试报告)
  → conformity assessment (Art 32):
      默认产品        → Module A 内部控制自评(可用协调标准获 presumption of conformity)
      Annex III Class I important → 标准/认证自评,否则第三方
      Annex III Class II important / Annex IV critical → 强制第三方(notified body 或 EUCC 认证)
      FOSS Annex III 特例:技术文档公开可走 Module A(Art 32(5))
  → EU Declaration of Conformity (Art 28, Annex V;多法规可单一 DoC, Art 28(3))
  → CE marking (Art 29/30)
  → 上市后义务:support period 内漏洞处理(Annex I Part II)+ Art 14 主动利用漏洞/事件报告(已 2026-09-11 起适用)
  → 市场监督:MSA 依 Art 52 检查、Art 53 调取数据与文档、Art 54 处置 significant cybersecurity risk 产品
```

### 4.2 平台边界分析(Interpretation)

**边界内(证据生产/留存/导出)**——CRA 支撑平台可以且应该嵌入的环节:

1. **技术文档(Annex VII)的持续生产**:SBOM、漏洞处置记录、风险评估、更新记录本质上是"活文档",平台的漏洞全生命周期数据就是技术文档的数据源;导出能力须对齐 Annex VII 结构与 MSA 调取(Art 53)的粒度。
2. **conformity assessment 的举证支撑**:无论 Module A 自评还是第三方评估,制造商都要向(自己或 notified body)证明 Annex I Part II 流程在运行——平台输出"流程合规证据包"(漏洞处理时效、support period 覆盖、安全更新记录)是直接卖点。
3. **上市后义务的履约载体**:Art 14 报告(24h 预警/72h 通报/14d 终报,经 ENISA SRP)、support period 管理、纠正措施记录。
4. **EU DoC 前的自检**:Annex V 要求声明符合的法规与标准清单,平台可做 DoC 数据预填与一致性校验。

**边界外**——平台不应承诺替代的环节:

1. **Notified Body 第三方评估本身**(Annex III Class II / Annex IV):法定第三方行为,平台只能做"被评估对象"侧的准备工作;
2. **EU DoC 的签署**:制造商的法律责任行为,平台只能辅助生成草稿;
3. **CE 加贴与市场监督应对的决定权**:均在制造商;
4. ** presumption of conformity 的取得**:取决于 OJ 引用标准(截至 2026-09 尚无),平台不能以"用了我们的工具"暗示合规推定。

**结构性判断**:RED→CRA 的演进把竞争点从"帮助通过一次性评估"移向"支撑持续义务的证据基础设施";平台价值与 support period(≥5 年)同生命周期,天然订阅制。这与 [04 报告](04-technology-deep-dive.md)对证据层壁垒的判断一致(见 [00 报告](00-final-report.md) §5.5)。

---

## 5. 遗留不确定项

1. **CRA 协调标准 OJ 引用时间表**:截至 2026-08 下旬无任何引用;ETSI 17 个 vertical 标准在批准程序中(2026-11 中截止),但 Commission 引用节奏未知。若 2027 年仍无引用,Annex III Class I 产品的"标准路径自评"将不可用,第三方评估需求被动放大(影响平台对评估机构生态的接入策略)。
2. **Art 2(5) delegated act 的后续使用**:2026/339 处理了 RED,但其他部门法(如 EHDS 下 EHR 软件、汽车行业软件部件)是否会有类似限制/排除法案,值得持续监控 EUR-Lex。
3. **MR-CRA 联合 guidance**:Commission 承诺发布,截至本次检索未见落地文本。
4. **EN 18031 引用限制对 RED 存续期合规的实际影响**(2025/138 对密码策略等的限制条款),非本章重点,未展开核实。
