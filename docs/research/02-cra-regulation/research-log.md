# Research Log — 02-cra-regulation(CRA 法规调研)

任务:系统研究 Regulation (EU) 2024/2847(CRA)与软件漏洞全生命周期管理相关的要求。
抓取日期均为 2026-09-18。

## 时间线

### 2026-09-18

1. **建立目录** `docs/research/02-cra-regulation/sources/`(及 `raw/` 子目录存原始抓取件)。
2. **直连 EUR-Lex 失败**:`curl` 请求 `eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ:L_202402847` 返回 HTTP 202 + `x-amzn-waf-action: challenge`(AWS WAF 人机验证);FetchURL 报"may require JavaScript"。**决策**:不硬磕,改走 Wayback Machine 存档。
3. **Cellar 试探**:`publications.europa.eu/resource/celex/32024R2847` 返回 RDF 元数据(可达),但未找到直接 HTML 全文端点(`.eng` 404)。弃用此路径。
4. **Wayback CDX 查询** `eur-lex.europa.eu/eli/reg/2024/2847/oj` 有多个 200 快照。下载 `20241122090643id_` 快照 → 1MB,但为**法语版**。改下 `20250118003947id_` 快照 → 973KB,**英文全文版**(标题 "Regulation - 2024/2847 - EN - EUR-Lex")。✅ 采纳。
   - 注意:archive.org 期间多次返回 "Temporarily Offline",重试后成功。
5. **文本提取**:pip 装 bs4 失败(PyPI 镜像 403),改用 Python 标准库 html.parser 提取纯文本 → `raw/reg-2024-2847-en.txt`(353,962 字符,71 条 Article + Annex I–VIII + recitals 齐全,grep 验证)。
6. **精读条文**:Art 1–3(范围与定义)、Art 13(制造商义务 25 款)、Art 14–17(报告机制)、Art 18–25(importer/distributor/steward/attestation)、Art 26–32(guidance、presumption of conformity、符合性评估)、Art 64(罚则)、Art 69–71(过渡与生效)、Annex I/II/III/IV/VII、以及关键 recitals(SaaS 分工、FOSS 商业性边界、SBOM 不强制公开、support period 细则)。逐段核对行号。
7. 写 source note `eur-lex-reg-2024-2847-fulltext.md`(法规原文层)。

## 来源采纳/弃用记录

| 来源 | 状态 | 原因 |
|---|---|---|
| EUR-Lex 直连 | 弃用(直连) | AWS WAF challenge;改用其 Wayback 存档快照,内容同一官方文本 |
| lexparency.org 镜像 | 弃用 | DNS 被污染(解析到 198.18.1.15),TLS 握手失败 |
| Cellar RDF 端点 | 弃用 | 只拿到元数据,无便捷全文 HTML |
| Wayback 2024-11-22 快照 | 弃用(语言) | 法语版;改用 2025-01-18 英文版 |

8. **Commission 官方页**:`digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act`(FetchURL 成功)——确认时间线官方口径、2026-07-27 guidance 发布。写 note `commission-cra-page.md`。
9. **ENISA SRP FAQ**(WebSearch 发现,FetchURL 成功):SRP 已于 2026-09-11 上线、无 API、steward 报告义务 2027-12-11 起、PEC delegated act 2025-12-11 通过、不追溯规则等。写 note `enisa-cra-srp-faq.md`。✅ 高价值采纳。
10. **Commission "FAQs on the CRA Implementation" v1.0**(2025-12-03):library 页 FetchURL 只给 "Download" 文字,用 curl 抓页面 HTML 找到 newsroom 文档 ID(122331=PDF,123307=Markdown),下载成功并存入 `raw/`。全文通读 Scope / Annex I / 漏洞处理 / support period / 报告 / 标准章节。写 note `commission-faqs-cra-implementation.md`。✅ 最高价值官方解释来源。
11. **标准化状态**:Commission `cra-standardisation` 页(FetchURL)确认 M/606=C(2025)618(2025-02-03)、41 个标准、2025-04-03 ESO 接受。写 note `commission-cra-standardisation.md`。
12. **二手对照**:Regara / cyberresilienceact.eu / disclose.io / spilma(WebSearch 摘要,未全文抓取)——"截至 2026-07 无任何 CRA 协调标准获 OJ 引用"、"M/606 期限拟顺延 2 个月"。合并写 note `secondary-standards-status.md`,全部标二手。
13. **撰写最终报告** `docs/research/02-cra-regulation.md`(13 个问题 + 时限表 + 46 行映射表 + 关键发现)。✅ 完成。

## 来源间冲突记录

1. **M/606 标准交付期限**:Commission FAQ v1.0(2025-12,官方解释)记 horizontal vulnerability-handling 标准 2026-08-30、vertical 2026-10-30;二手来源(cyberresilienceact.eu 2026-07-30、disclose.io 2026-09-01)称 Commission 已发修订草案顺延约 2 个月。**处理**:报告以官方原文日期为准,顺延标(不确定)。
2. **"是否要求主动监控"**:部分厂商营销材料暗示 CRA 要求持续威胁监控;Commission FAQ 5.1 明确不要求(知悉渠道仅为举例)。报告 §8 已纠正。
3. **"是否必须修补所有漏洞"**:常见于二手解读的夸大;FAQ 4.3.1 明确按风险定补救形式。报告 §15 已列为关键发现。
4. **"SBOM 公开"**:大量二手文章称 CRA "要求 SBOM";法规只要求绘制+向监管提供,明确不强制公开(Recital)。已纠正。

## 未完成/后续建议
- 未读 C(2026) 5252 guidance 全文(仅新闻稿+ENISA FAQ 转述);§15 的第 218 段(第三方组件 AEV 分工)细节可补充。
- 二手来源未全文抓取,仅基于搜索摘要。
- EUR-Lex 文本取自 Wayback 存档;正式引用前建议在可直连 EUR-Lex 的网络复核。
