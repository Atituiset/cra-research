# Research Log — 05 CRA 与既有欧盟产品合规体系的关系

> 研究日期:2026-09-19 | 目标:核实 EU 2026/339;梳理 CE/NLF 体系、CRA 与 RED/NIS2/MR 等边界、对产品边界的影响。

## 检索过程(按时间)

1. **WebSearch "Delegated Regulation (EU) 2026/339"** → 命中 EUR-Lex 官方 OJ 页、EUR-Lex 2026-04-29 OJ 日报、EFTA EEA-Lex factsheet、TÜV、Omnilex、ANACOM、cutuil.dev 等多方,编号/标题/日期一致 → 初步判断线索可信。
2. **FetchURL EUR-Lex ELI(reg_del/2026/339)直连** → **成功**,取得 OJ 全文(此前 [02 报告](../02-cra-regulation.md)时 EUR-Lex 直连被 AWS WAF 拦截,本次未拦截,不再需要 Wayback)。逐点核实:通过 2026-02-16、OJ 2026-04-29、Art 1 废止生效 2027-12-11、Recital (3)(4) 废止理由、Recital (5) 过渡期市场监督保全 → **线索成立**。
3. **FetchURL EUR-Lex ELI(reg_del/2022/30)直连** → 成功,取得全文:Art 1 三类要求与设备类别、Art 2 部门法豁免、原适用日 2024-08-01。
4. **FetchURL EUR-Lex ELI(reg_del/2023/2444)直连** → 成功:适用日延至 2025-08-01(理由:EN 18031 标准未及就绪),并更正 Art 1(2) 表述。
5. **本地复核 CRA 全文存档**([02 报告](../02-cra-regulation.md) [raw/reg-2024-2847-en.txt](../02-cra-regulation/sources/raw/reg-2024-2847-en.txt))→ Art 2 排除条款、Art 2(5) 弹性阀门、Art 27–32/52/53 条文编号、Recital 12(NIS2/SaaS)、RED recital(行 287,预见 2022/30 废止)、MR recital(行 471,叠加适用)。
6. **Commission CE marking 页**:旧路径 404 → 找到当前有效路径 /single-market/ce-marking_en → 取得制造商四步责任与"CE 非政府批文"官方表述。
7. **Commission NLF 页**(/single-market/goods/new-legislative-framework_en)→ NLF 三件套、31 部对齐立法清单(RED #14、MR #26、AI Act #28、CRA #29)、NLF 现代化评估。
8. **Machinery Regulation 适用日冲突**:EUR-Lex 抓取文本 Art 54 印为 2027-01-14,但 Commission NLF 页写 20/1/2027 → WebSearch 确认系 OJ corrigendum(OJ L 169, 4.7.2023)更正为 **2027-01-20**;EUR-Lex 默认页未合并 corrigendum → 采纳 2027-01-20,并在 source note 记录教训。
9. **M/606 OJ 引用进展**:WebSearch → Greenbone(2026-08-25)、Regara(2026-07-27)、CVD Portal(2026-07-29)、cybercertlabs(2026-09-07)四源一致:截至 2026-08 下旬无任何 CRA 协调标准获 OJ 引用;ETSI 2026-08-13 对 17 个 vertical 标准启动批准程序。
10. **EN 18031 OJ 引用**:WebSearch → TÜV SÜD(2025-01-30)、VDMA、西班牙政府指南一致:Implementing Decision (EU) 2025/138,2025-01-30 引用,带限制。

## 采纳 / 弃用

- **采纳**:EUR-Lex 一手文本(2026/339、2022/30、2023/2444、2023/1230);Commission CE/NLF 官方页;[02 报告](../02-cra-regulation.md)本地 CRA 全文存档;多源一致的二手(标准进展、EN 18031、MR corrigendum)。
- **弃用/降级**:cutuil.dev、ce-copilot.de、omnilex.ai 等对 2026/339 的转述仅作旁证,结论以 EUR-Lex 一手文本为准;线索自带的 utm_source=chatgpt.com 链接未直接使用(AI 转述风险),改从官方域名重新检索定位。
- **未深入**:EN 18031 引用限制条款细节(2025/138 对密码策略的限制等)——非本章重点,记为遗留项。

## 冲突记录

| 冲突 | 处理 |
|---|---|
| Machinery Regulation 适用日:EUR-Lex 文本 2027-01-14 vs Commission 页面/行业来源 2027-01-20 | 查明系 OJ corrigendum(2023-07-04)更正;采纳 **2027-01-20**;教训:EUR-Lex 默认页可能未合并 corrigendum |
| [02 报告](../02-cra-regulation.md)称"EUR-Lex 直连被 AWS WAF 拦截,须用 Wayback" | 本次直连成功,环境已变化;[05 报告](../05-eu-compliance-landscape.md)及 source notes 如实注明抓取路径,未沿用 Wayback |
| 线索链接带 utm_source=chatgpt.com(疑似 AI 转述) | 不采信转述文本,以官方一手来源重新核实;结论:内容属实 |
| CRA 协调标准状态:[02 报告](../02-cra-regulation.md)(2026-09-18)"无任何 OJ 引用" vs 本章检索 | 一致,且获得 2026-08 下旬多源确认 + ETSI 批准程序新进展,属更新而非冲突 |
