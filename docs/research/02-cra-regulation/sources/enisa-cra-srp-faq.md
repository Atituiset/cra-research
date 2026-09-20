# Source Note: ENISA — CRA Single Reporting Platform FAQ

- **URL**: https://www.enisa.europa.eu/topics/product-security/single-reporting-platform-srp/frequently-asked-questions
- **标题**: Frequently Asked Questions — CRA Single Reporting Platform (CRA SRP)
- **发布方**: ENISA(欧盟网络安全局,官方)
- **更新日期**: 2026-09-12(页面标注 "Updated: 12 September 2026")
- **抓取日期**: 2026-09-18
- **来源层级**: 官方解释(ENISA 对 CRA Art 14–16 的操作化说明;非法律文本本身)

## 关键摘录/要点

1. **SRP 已于 2026-09-11 上线**,与 Art 14 报告义务生效同日;入口 `https://portal.cra-srp.enisa.europa.eu`,初期仅英文、**无 API**(须走网页界面),自愿报告(Art 15)功能后续阶段才上线。
2. **OSS steward 的 Art 24(3) 报告义务从 2027-12-11 才适用**(依 Art 71(2))——即 steward 目前(2026-09)还不需要报告,尽管 Art 14 已对 manufacturer 生效。
3. 报告时限复述(与法规一致):Early Warning 24h;72h Notification;AEV Final Report = 缓解措施可用后 14 天;SI Final Report = 72h 通知后 1 个月。
4. **接收方**:一次提交,同时给 CSIRT designated as coordinator(按 Art 14(7) 选定,通常为主要机构所在地)+ ENISA;接收 CSIRT 无延迟分发给其他相关 CSIRT,并向本国 market surveillance authority 共享。
5. **注册机制**:Assigned Representative(AR)制,需 EU Login + MFA;每制造商 1 个 Primary AR + 最多 20 个 Secondary AR;CSIRT 验证 AR-制造商关联,**验证与报告并行,未验证前可先提交最多 20 条通知**;建议需要报告时才注册。
6. **不追溯**:2026-09-11 之前已经知悉的 actively exploited vulnerability 不需补报(引 Commission "FAQs on the CRA Implementation" 5.1/5.3);之后知悉的,即使漏洞早已存在也要报。
7. 第三方组件中的 AEV 报告责任:指向 Commission FAQ 5.4 与 C(2026) 5252 附件第 218 段(集成组件的制造商 vs 组件制造商的分工——需进一步读 Commission guidance)。
8. **延迟分发(PEC)**:Commission 于 **2025-12-11 通过 Delegated Act** 细化 Art 16(2) 的 cybersecurity grounds;PEC 仅适用于 Art 16(2)(a)–(c) 情形,PEC 下 ENISA 只收到部分信息。
9. 平台计时器提示:72h 计数器当前按"early warning 提交后 48h"显示到期(已知 UI 逻辑问题,未来版本改为按"知悉时间"计算);AEV 无 final report 计数器(因取决于补丁可用时间)。
10. ENISA 职责:运营平台、每 24 个月出趋势报告(首份在报告义务生效后 24 个月内)、对修复后的漏洞经制造商同意纳入 EUVD(NIS2 Art 12(2))、为 SME 提供 helpdesk。
11. SRP 故障时:等平台恢复后仍需经 SRP 补交;紧急可先直接联系 CSIRT,但不替代 SRP 提交。

## 支撑的报告结论
#6(报告机制细节、时限表、接收方、SRP 现状)、#11(2026-09-11 节点实际生效情况)、#2(steward 义务起始时间差异)。
