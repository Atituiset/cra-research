# Source Note: Regulation (EU) 2024/2847 (CRA) 全文原文

- **URL**: https://eur-lex.europa.eu/eli/reg/2024/2847/oj (CELEX 32024R2847)
- **标题**: Regulation (EU) 2024/2847 of the European Parliament and of the Council of 23 October 2024 on horizontal cybersecurity requirements for products with digital elements... (Cyber Resilience Act)
- **发布方**: European Parliament & Council;Official Journal of the EU (EUR-Lex)
- **发布日期**: 2024-10-23 签署;2024-11-20 OJ 公布
- **抓取日期**: 2026-09-18
- **来源层级**: 法规原文(一手)
- **抓取方式备注**: eur-lex.europa.eu 直连被 AWS WAF challenge 拦截(curl 与 FetchURL 均失败)。改用 Wayback Machine 存档快照 `web.archive.org/web/20250118003947/https://eur-lex.europa.eu/eli/reg/2024/2847/oj`(英文全文,973KB)下载并提取为纯文本,存于 `raw/reg-2024-2847-en.txt`(353,962 chars,含全部 71 条 Articles + Annex I–VIII + 全部 recitals)。引用页 URL 仍以 EUR-Lex ELI 官方地址为准。

## 关键摘录/条文要点(报告中引用以本条为准)

### 定义(Art 3)
- (1) 'product with digital elements' = a software or hardware product **and its remote data processing solutions**, including software or hardware components being placed on the market separately.
- (2) 'remote data processing' = data processing at a distance, designed/developed by or under the responsibility of the manufacturer, the absence of which would prevent the product from performing one of its functions.
- (13) 'manufacturer' — 开发/制造或委托开发制造并以自己名义/商标上市的自然人或法人,**whether for payment, monetisation or free of charge**。
- (14) 'open-source software steward' = 非制造商的法人,系统性地、持续地支持特定 FOSS 产品(且该产品 intended for commercial activities)的开发并确保其 viability。
- (20) 'support period' = 制造商须按 Annex I Part II 有效处理产品漏洞的期间。
- (22) 'making available on the market' = 在商业活动过程中向欧盟市场供应用于分销或使用,whether in return for payment or free of charge。
- (39) 'software bill of materials' = a formal record containing details and supply chain relationships of components included in the software elements。
- (40)(41)(42) vulnerability / exploitable vulnerability / **actively exploited vulnerability**(有可靠证据表明恶意行为者已在未经系统所有者许可的情况下利用)。
- (44) 'incident having an impact on the security of the product with digital elements'。
- (51) 'CSIRT designated as coordinator' 按 NIS2 Art 12(1) 指定。

### 范围(Art 2)
- Art 2(1): 适用于 intended purpose 或 reasonably foreseeable use 包含**直接或间接**逻辑或物理数据连接到设备或网络的 products with digital elements。
- Art 2(2): 排除已适用 Regulation (EU) 2017/745(医疗器械)、2017/746(IVD)、2019/2144(机动车)的产品;2(3) 航空 2018/1139 认证产品;2(4) 船用设备 Directive 2014/90/EU;2(7) 国家安全/防务专用;2(6) 同规格备件。
- Recital(见 raw 文本 line 143):**SaaS/PaaS/IaaS 云服务属于 NIS2 管辖,不属于 CRA**;CRA 只管"构成产品 remote data processing"的云功能(如智能家居厂商提供的远程控制云)。

### Manufacturer 义务(Art 13)
- 13(1)(2)(3)(4): 按 Annex I Part I 设计开发生产;网络安全风险评估并文档化、在 support period 内更新;纳入技术文档(Annex VII)。
- 13(5): 集成第三方组件(含未商业化上市的 FOSS 组件)的 **due diligence** 义务。
- 13(6): 发现所集成组件(含开源组件)的漏洞时,应**上报组件维护者**、按 Annex I Part II 修复;如已开发修复代码/文档,应与组件维护者共享(适当时机读格式)。
- 13(7): 系统记录已知漏洞与第三方提供的信息,并更新风险评估。
- 13(8): 在上市时及整个 **support period** 内按 Annex I Part II 有效处理漏洞;**support period 至少 5 年**,若产品预期使用不足 5 年则等于预期使用时间;确定依据须写入技术文档;Commission 可通过 delegated act 规定特定类别的最低 support period。
- 13(9): 每个安全更新发布后须保持可用至少 **10 年**或 support period 剩余期,取较长者。
- 13(10): 对实质性修改后的后续版本,只对最后上市版本承担 Annex I Part II(2) 修复义务,前提是旧版用户可**免费**升级到最新版且不产生额外软硬件环境成本。
- 13(17): 指定 **single point of contact**,用户可报告漏洞,且不得仅限自动化工具。
- 13(18): 随附 Annex II 用户信息与说明,保留 10 年或 support period(取长)。
- 13(19): 购买时清晰标明 support period **结束日期**(至少到月/年);技术可行时在产品上显示 EoL 通知。
- 13(21): 知悉不合规时立即采取纠正措施、撤回或召回。
- 13(22): 应 market surveillance authority 合理请求提供全部合规信息与文档。
- 13(24): Commission 可通过 implementing acts 规定 SBOM 的格式与要素。
- 13(25): ADCO 可决定全欧盟依赖评估,market surveillance authorities 可据此**要求制造商提供 SBOM**;向 ADCO 提交时须匿名化聚合。

### 报告义务(Art 14,2026-09-11 起适用)
- 14(1)(2) **actively exploited vulnerability**: 同时报给 CSIRT designated as coordinator + ENISA,经 Art 16 single reporting platform:
  - (a) early warning:知悉后 24h 内;
  - (b) vulnerability notification:72h 内(产品一般信息、exploit 与漏洞性质、已采取/用户可采取的缓解措施、信息敏感度);
  - (c) final report:纠正/缓解措施可用后 **14 天**内(漏洞描述+严重性+影响;恶意行为者信息(如有);安全更新/纠正措施详情)。
- 14(3)(4)(5) **severe incident having an impact on the security of the product**: 同一平台、同一接收方;24h early warning / 72h incident notification / **1 个月**内 final report(在提交 incident notification 之后)。severe 判定标准见 14(5)(a)(b)。
- 14(6): CSIRT 可要求 intermediate report。
- 14(7): 通过制造商**欧盟主要机构所在地**成员国 CSIRT 的 end-point 提交;无主要机构时按授权代表→进口商→分销商→用户最多成员国顺序确定。
- 14(8): 制造商还须**通知受影响用户**(必要时结构化、机读格式);制造商不及时通知时 CSIRT 可直接通知用户。
- 14(9): 2025-12-11 前 Commission 应通过 delegated act 规定延迟传播的 cybersecurity grounds 细则。
- Art 16: ENISA 建立并运营 single reporting platform;CSIRT 接收后无延迟分发给相关成员国 CSIRT;特殊情形可延迟分发(14(2)(a) 敏感度);极端情形下 ENISA 仅同步获得有限信息。
- Art 17(4): 报告行为本身不加重责任;17(5): 修复措施可用后 ENISA 经与制造商协商将漏洞纳入 NIS2 Art 12(2) 的 European vulnerability database;17(6): CSIRT 为中小微企业提供 helpdesk。
- Art 15: 自愿报告(其他漏洞、cyber threats、incidents、near misses)。

### Importer / Distributor(Art 19, 20)
- Importer: 只能上市合规产品;上市前核实 conformity assessment、技术文档、CE、DoC、标识与 support period 标注;发现漏洞**无延迟通知制造商**,产品有 significant cybersecurity risk 时立即通知 MSA;保留 DoC 副本 10 年或 support period。
- Distributor: due care;核实 CE 与相关义务;发现漏洞通知制造商,significant risk 时通知 MSA。
- Art 21/22: 进口商/分销商或第三方以自己名义上市或进行 **substantial modification** 者,视为 manufacturer,适用 Art 13/14。

### Open-Source Software Steward(Art 24)
- 24(1): 以可验证方式制定并文档化 cybersecurity policy(促进安全开发与漏洞有效处理、鼓励自愿报告、促进开源社区内信息共享)。
- 24(2): 与 MSA 合作,应请求提供上述文档。
- 24(3): **Art 14(1) 报告义务仅在其参与产品开发的范围内适用**;Art 14(3)(8) 仅在 severe incident 影响 steward 自有开发基础设施时适用。
- 不贴 CE(Recital, line 199);不受罚款(Art 64(10)(b))。
- Art 25: 自愿性 FOSS security attestation 计划(delegated acts)。
- Art 32(5): FOSS 制造商即使属 Annex III 类别,只要**公开技术文档**,仍可用 Module A 内部控制自评。

### FOSS 豁免边界(Recitals,raw 文本 line 191/183)
- 只有在"商业活动过程中供应"(making available on the market)的 FOSS 才落入 CRA;**未 monetised 的 FOSS 供应不算商业活动**;接受资助/捐助、定期发布本身不构成商业性;非营利组织开发 FOSS 在收入用于非营利目标时不算商业活动;**向他人负责的 FOSS 项目贡献源代码的个人不适用 CRA**。
- 只有当组件被其原始制造商 monetise 时,FOSS 组件供应才算 making available on the market。

### Annex I Part I(产品属性,13 项)
(1) 基于风险的适当网络安全水平;(2)(a) 上市时**无已知可利用漏洞**;(b) **secure by default** 配置(可与企业用户就定制产品另行约定)+ 可重置出厂;(c) 可通过安全更新修复漏洞,默认启用自动更新+清晰 opt-out+可暂缓;(d) 防未授权访问(认证/访问控制)并报告可疑未授权访问;(e) 机密性(静态/传输加密,SOTA);(f) 完整性防篡改并报告损坏;(g) 数据最小化;(h) 基本功能可用性、抗 DoS;(i) 最小化对其他设备/网络可用性的负面影响;(j) 限制攻击面;(k) 漏洞利用缓解技术降低事件影响;(l) 记录监控内部活动(带用户 opt-out);(m) 用户可安全彻底删除数据与设置。

### Annex I Part II(漏洞处理,8 项)
(1) 识别并记录漏洞与组件,**包括以常用机读格式绘制 SBOM,至少覆盖顶层依赖**;(2) 无延迟处理与修复漏洞、提供安全更新;技术可行时**安全更新与功能更新分开**;(3) 定期有效的安全测试与评审;(4) 安全更新发布后**公开披露已修复漏洞信息**(描述、受影响产品识别、影响、严重性、修复指引;有正当理由时可延迟公开至用户有机会打补丁后);(5) 制定并执行 **coordinated vulnerability disclosure policy**;(6) 便利漏洞信息共享,包括**提供漏洞报告联系地址**(含第三方组件);(7) 安全分发更新的机制,及时修复,适用时自动分发;(8) 安全更新**免费**、无延迟分发,附 advisory messages(定制产品可与企业用户另行约定)。

### Annex II(用户须知)
含:制造商联系方式;single point of contact 与 CVD policy 获取地址;产品标识;预期用途与安全属性;已知重大风险情形;EU DoC 网址;技术支持类型与 **support period 结束日期**;安全安装/更新/退役说明;**第 9 项:若制造商决定向用户提供 SBOM,说明获取途径**(即 SBOM 公开是可选的)。

### 重要/关键产品分类
- Art 7 + **Annex III**:important products 分 Class I(19 类:身份管理/PAM、浏览器、密码管理器、杀毒软件、VPN、网络管理、SIEM、boot manager、PKI/证书签发、网络接口、**操作系统**、路由器/调制解调器/交换机、安全微处理器/微控制器/ASIC/FPGA、智能家居虚拟助手、带安全功能的智能家居产品、联网玩具、可穿戴健康/儿童设备)与 Class II(4 类:hypervisor 与容器运行时、防火墙与 IDS/IPS、防篡改微处理器、防篡改微控制器)。
- Art 8 + **Annex IV**:critical products(3 类:hardware devices with security boxes、smart meter gateways 等高级安全设备、智能卡/secure elements),Commission 可通过 delegated act 强制其获得至少 'substantial' 级 European cybersecurity certificate;否则适用 Art 32(3)。
- Art 7(4): 2025-12-11 前 Commission 应通过 implementing act 给出 Annex III/IV 类别的技术描述。
- **符合性评估路径(Art 32)**: 默认产品 → Module A 内部控制自评(或自愿选更严路径);Class I → 若完整适用 harmonised standards/common specs/EUCC 认证可自评,否则须第三方(Module B+C 或 H);Class II → **始终须第三方**(B+C、H 或 EUCC substantial+);Critical(Annex IV)→ EUCC 认证或 Art 32(3) 路径。
- Art 27: presumption of conformity(harmonised standards / common specifications / EU cybersecurity certification schemes);Commission 应向 ESO 发出标准化请求。

### 技术文档与合规证据
- Art 31 + **Annex VII**:技术文档至少含产品总体描述(预期用途、影响合规的软件版本)、设计开发生产与漏洞处理过程信息(含 **SBOM、CVD policy、漏洞报告联系地址证据、安全更新分发技术方案**)、网络安全风险评估(Art 13)、support period 确定依据、所适用 harmonised standards/共同规范/认证方案清单、测试报告、EU DoC 副本、以及 **Annex VII 第 8 项:SBOM 仅在市场监管机构合理请求且为核查合规所必需时提供**。
- Art 13(13)/18(3)/19(6):技术文档与 EU DoC 保留 **10 年或 support period,取较长者**。
- Art 28: EU declaration of conformity;Art 30: CE marking。
- Art 69(2): 2027-12-11 前已上市产品仅在进行 substantial modification 后才适用 CRA;**69(3) 例外:Art 14 报告义务适用于所有在 2027-12-11 前已上市的产品**。

### 罚则(Art 64)
- 64(2): 违反 **Annex I 基本要求、Art 13、Art 14** → 最高 €15M 或全球年营业额 2.5%(取高)。
- 64(3): 违反 Art 18–23、28、30(1)-(4)、31(1)-(4)、32(1)-(3)、33(5)、39、41、47、49、53 → 最高 €10M 或 2%。
- 64(4): 向 notified body/MSA 提供错误、不完整或误导性信息 → 最高 €5M 或 1%。
- 64(10): 豁免 — (a) 小微企业在 Art 14 24h early warning 时限上的失误不罚款;(b) **open-source software stewards 的任何违反不罚款**。
- 非罚款风险:Art 52-59 市场监管措施(召回、撤回、市场禁入);Art 59 Commission 在例外情形下可要求全欧盟层面召回/撤回(Recital line 943);Art 65 集体诉讼(Directive 2020/1828)。

### 时间线(Art 71, 69, 70)
- 2024-11-20 OJ 公布;**2024-12-10 生效**(Art 71(1),公布后第 20 天;delegated powers 自 2024-12-10 起,Recital line 983)。
- **2026-06-11**:Chapter IV(Art 35-51,notifying authorities / notified bodies 等)适用。
- **2026-09-11**:**Art 14 报告义务适用**(Art 71(2))。
- **2027-12-11**:其余全部适用(Art 71(2));2027-12-11 前上市产品原则上不适用,除非 substantial modification(Art 69(2)),但 Art 14 例外适用(Art 69(3))。
- 2028-06-11: 其他欧盟法规下已发 EU type-examination 证书过渡期届满(Art 69(1))。
- 2028-09-11 前:Commission 提交 single reporting platform 有效性评估报告(Art 70(2))。
- 2030-12-11: 首次评估审查报告(Art 70(1))。
- 2025-12-11 前(多个节点):Annex III/IV 技术描述 implementing act(Art 7(4));Art 14(9) 延迟分发 delegated act。

## 支撑的报告结论
适用对象与定义(#1)、四类角色(#2)、Annex I 逐条(#3)、SBOM/漏洞处理(#4)、CVD(#5)、Art 14 报告机制(#6)、Support Period(#7)、上市后监控(#8)、更新与通知(#9)、技术文档(#10)、时间线(#11)、罚则(#12)、产品分类与符合性评估(#13) —— 本来源是全部 13 项的一级依据。
