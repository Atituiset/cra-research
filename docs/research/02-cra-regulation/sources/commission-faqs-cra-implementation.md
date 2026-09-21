# Source Note: European Commission — FAQs on the CRA Implementation (v1.0)

- **URL**: 页面 https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-implementation-frequently-asked-questions ;Markdown 下载 https://ec.europa.eu/newsroom/dae/redirection/document/123307 ;PDF https://ec.europa.eu/newsroom/dae/redirection/document/122331
- **标题**: FAQs on the CRA Implementation(Version 1.0)
- **发布方**: European Commission services(官方工作文件)
- **发布日期**: 2025-12-03
- **抓取日期**: 2026-09-18;原始件存 [raw/commission-faqs-cra-implementation-v1.md](raw/commission-faqs-cra-implementation-v1.md) 与 [.pdf](raw/commission-faqs-cra-implementation-v1.pdf)
- **来源层级**: 官方解释(Commission services 工作文件,非立法;FAQ 自称 preliminary、供实施参考)

## 关键摘录/要点

### 范围
- 三要素判断是否在 CRA 范围内:符合 Art 3(1) 定义 + made available on the market + 预期/可预见用途含直接或间接数据连接(Art 2(1))。
- **standalone SaaS/云服务(非产品制造商责任范围内)不是 product with digital elements**;只有构成 Art 3(2) "remote data processing" 的服务才落入 CRA(引 Recital 12)。网站不支持产品功能时不在范围内。
- 间接连接例子:离线文本编辑器/计算器经操作系统间接联网,**仍在范围内**;无任何连接能力的洗碗机、基础计算器、电动牙刷等不在范围。
- 2027-12-11 前上市的产品仅在 substantial modification 后才全面适用(Art 69(2));但 **Art 14 报告义务对存量产品也适用**(Art 69(3));对老产品,制造商"须通知漏洞/事件,但 CRA 不要求其履行其他义务(如 vulnerability handling)",因为老版本工具链可能已不存在。
- 自产自用(own use)不在范围(Blue Guide 2.3);测试版(alpha/beta/RC)可依 Art 4(3) 豁免,须有可见标识且限时。

### 漏洞处理(Annex I Part II)
- **CRA 不要求产品"没有任何漏洞"**:只要求上市时基于风险评估无"已知可利用漏洞"(known exploitable vulnerabilities);可利用性须逐案判断(代码是否被调用、所需访问权限、补偿控制等)。
- **不要求对 support period 内发现的所有漏洞都打补丁**:按风险决定补救形式——立即补丁、变通 advisory、手册更新、禁用受影响功能等;风险低时可仅记录并在下个常规版本中移除受影响组件。
- 安全更新与功能更新分离是"where technically feasible";技术上不可分(如替换解析器必然改变行为)时可合并。
- 集成组件漏洞:整产品责任在集成制造商;组件本身已上市时组件制造商也有义务;组件未上市(或 CRA 前上市)时,集成商须自行补救(禁用功能、换组件、自己写补丁——开源组件场景);依 Art 13(6) 补丁须分享给组件维护者。
- **用户不装更新,制造商不负责**(只要已提供自动更新机制与通知;用户 opt-out 除外)。

### Support period
- 至少 5 年;预期使用超过 5 年的(主板、路由器、操作系统、工业控制系统)应更长;少于 5 年仅限产品预期使用确实不足 5 年(如订阅到期即不可用的 SaaS 化杀毒软件、订阅制 FOSS 支持服务——support period 等于活跃订阅期)。
- 支持期结束不等于停售:已上市库存可继续卖;新生产的每批须各自设定 support period。

### 报告(Art 14)
- "知悉"渠道举例:客户通报、威胁情报、政府机构通知、内部遥测/蜜罐、暗网监控——但 **CRA 不强制要求制造商主动开展这些监控活动** 来满足报告义务(重要边界!与"持续监控义务"的读法有关)。
- **Zero-day 未被恶意利用时不需报告**:只有有可靠证据已被恶意利用才触发强制报告;善意研究/bug bounty 发现的不算(Recital 68);可自愿报告(Art 15)。
- 第三方组件中的 actively exploited vulnerability:**集成该组件的产品制造商须报告;组件制造商(若组件已上市)也须报告**——同一漏洞可能被多方分别报告,以便 CSIRT/ENISA 评估市场渗透率。若组件漏洞在该产品中不可利用,则无需强制报告。
- **OSS steward 的 Art 24(3) 报告义务自 2027-12-11 起适用**(Art 71(2))。

### 符合性评估与标准
- Module A 自评适用对象含:FOSS 的 Class I/II important products(前提:技术文档公开,Art 32(5))。
- M/606 标准化请求:15 个 horizontal standards 聚成 3 个 deliverables —— 基于风险的设计开发生产标准(2026-08-30)、Annex I Part I 产品属性标准(2027-10-30)、**vulnerability handling 标准(2026-08-30)**;26 个 vertical standards(31 个 deliverables,覆盖 Annex III/IV 类别)2026-10-30。标准被 ESO 采纳后 Commission 依 Regulation 1025/2012 评估并在 OJ 公布引用后才产生 presumption of conformity。

## 支撑的报告结论
#1(SaaS 边界、standalone software 在内)、#3(Annex I 逐项的操作化解释)、#4(不必修补所有漏洞、组件漏洞分工)、#6(零日不触发报告、第三方组件双方报告)、#7(support period 细节)、#8("不强制主动监控"边界)、#11(标准时间表)。
