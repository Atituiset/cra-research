# Research Log — 01 Domain Ontology

研究日期：2026-09-18。按时间顺序记录查询、采纳/弃用来源及理由、来源冲突。

## 查阅时间线（2026-09-18）

| # | 动作 | URL / Query | 结果 | 处置 |
|---|---|---|---|---|
| 1 | FetchURL | cveawg.mitre.org/api/cve/CVE-2021-44228 | CVE JSON 5.1 完整记录；CNA=apache；CVSS/SSVC/KEV 来自 CISA-ADP 容器 | 采纳 → sources/cve-record-api-cve-2021-44228.md |
| 2 | FetchURL | api.osv.dev/v1/vulns/CVE-2021-44228 | 失败：JSON 无法被正文提取器解析 | 弃用该途径，改用 Bash curl |
| 3 | FetchURL | ossf.github.io/osv-schema | OSV Schema 1.9.0（2026-08-06）规范全文 | 采纳 → sources/osv-schema-spec.md |
| 4 | Bash curl | api.osv.dev/v1/vulns/GHSA-jfh8-c2jp-5v3q | Log4Shell OSV 条目：Maven 坐标 + PURL + 三段 ECOSYSTEM range + versions 枚举 + 换名 fork 包建模 | 采纳 → sources/osv-api-ghsa-log4shell.md |
| 5 | Bash curl | services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2021-44228 | NVD 视图：NVD Primary CVSS 3.1=10.0、NVD 补 CWE-917、CPE configurations（AND/OR 树）、103 references、内嵌 KEV 字段 | 采纳 → sources/nvd-api-20-cve-2021-44228.md |
| 6 | FetchURL | github.com/package-url/purl-spec/.../PURL-SPECIFICATION.rst | 发现规范已迁移；PURL 已成为 ECMA-427 | 采纳（重定向事实）→ sources/purl-spec-location.md |
| 7 | FetchURL | first.org/epss | EPSS 官方定义：未来 30 天被野外利用的概率，每日更新，FIRST SIG 维护 | 采纳 → sources/first-epss.md |
| 8 | FetchURL | packageurl.org/docs/purl/introduction | PURL/VERS 官方介绍；ECMA-427 2025-12-10 批准；VERS 计划 2026 提交 Ecma | 采纳 → sources/purl-intro.md |
| 9 | FetchURL | cisa.gov/known-exploited-vulnerabilities-catalog | KEV 目录（1713 条）；字段含 Due Date、Ransomware known/unknown；现行 BOD 26-04 | 采纳 → sources/cisa-kev-catalog.md |
| 10 | FetchURL | first.org/cvss/v4-0/specification-document | CVSS v4.0 规范全文（74K 字符存档）；Base/Threat/Environmental/Supplemental 四组 + CVSS-B/BT/BE/BTE nomenclature | 采纳 → sources/first-cvss-v40-spec.md |
| 11 | WebSearch | "NVD enrichment slowdown 2024 NIST announcement CVE analysis backlog" | 发现 2026-04-15 NIST 官方公告：放弃全量 enrichment，KEV/联邦软件/EO14028 critical software 优先，2026-03-01 前积压整体转 "Not Scheduled" | 追踪一手来源（#12） |
| 12 | FetchURL | nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth | 官方公告全文：263% 增长、2025 年 enrich 42,000 条仍不够、不再重复 CNA 已给的评分 | 采纳 → sources/nist-nvd-operations-2026.md |
| 13 | FetchURL | docs.github.com/.../about-the-github-advisory-database | GHSA ID 结构、reviewed/unreviewed 分层、OSV 格式发布、Dependabot 只对 reviewed 告警、EPSS 每日同步 | 采纳 → sources/github-advisory-database.md |
| 14 | FetchURL | cyclonedx.org/specification/overview | CycloneDX 对象模型全结构（含 Vulnerabilities/Declarations/Compositions）；IANA 媒体类型 | 采纳 → sources/cyclonedx-overview.md |
| 15 | FetchURL | spdx.dev/learn/overview | SPDX 3.0：license 起源、ISO/IEC 5962:2021、RDF 序列化、明确不覆盖范围 | 采纳 → sources/spdx-overview.md |
| 16 | FetchURL | github.com/openvex/spec | OpenVEX README：SBOM-agnostic、与 CSAF/CycloneDX VEX 的差异声明（标签集不一致） | 采纳 → sources/openvex-spec.md |
| 17 | FetchURL | csaf.io / oasis-open.github.io/csaf-documentation | 正文提取过薄（只有一句话） | 弃用，改抓 OASIS 标准原文（#19） |
| 18 | FetchURL | cve.org/ProgramOrganization/CNAs | CNA 定义与规模：517 家 CNA（514+3 CNA-LR）、43 国 | 采纳 → sources/cve-program-cna.md |
| 19 | FetchURL | docs.oasis-open.org/csaf/csaf/v2.0/os/csaf-v2.0-os.html | CSAF 2.0 OASIS 标准全文（295K 字符存档）；5 个 Profile；VEX profile 要求；引用 CISA VEX Status Justifications | 采纳 → sources/csaf-v20-oasis-standard.md |
| 20 | FetchURL | cwe.mitre.org/about/index.html | CWE 官方定义：weakness = 可能导致漏洞的条件 | 采纳 → sources/cwe-about.md |
| 21 | FetchURL | raw.githubusercontent.com/openvex/spec/main/OPENVEX-SPEC.md | OpenVEX v0.2.0 全文：statement 模型、四 status、五 justification、Spring Boot/Log4Shell 真实示例、CISA Minimum Requirements for VEX (2023-04) 出处 | 采纳 → sources/openvex-spec-v020.md |
| 22 | FetchURL | cve.org/About/Overview | CVE mission："identify, define, and catalog"；官方辟谣"CVE 不负责打分" | 采纳 → sources/cve-program-overview.md |
| 23 | FetchURL | federalregister.gov EO 14028 | 被反爬 CAPTCHA 拦截 | 弃用；改用 NIST EO 14028 任务页佐证 |
| 24 | FetchURL | nist.gov/itl/executive-order-14028-improving-nations-cybersecurity | EO 14028 Section 4、critical software 定义时间线 | 采纳 → sources/nist-eo-14028.md |
| 25 | FetchURL | slsa.dev | SLSA 定位：artifact integrity/防篡改框架，OpenSSF 项目 | 采纳 → sources/slsa-dev.md |
| 26 | FetchURL | csrc.nist.gov/pubs/sp/800/218/final | SSDF v1.1（2022-02）官方出版物页 | 采纳 → sources/ssdf-sp800-218.md |
| 27 | FetchURL | ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom | NTIA SBOM 最小要素报告（2021-07-12），EO 14028 指令链、SBOM 定义原文 | 采纳 → sources/ntia-sbom-minimum-elements.md |
| 28 | FetchURL | nvd.nist.gov/developers/vulnerabilities | NVD API 2.0 官方文档：CVE API + Change History API；pre-2015 记录保真度低 | 采纳 → sources/nvd-api-developers.md |
| 29 | WebSearch | "Cyber Resilience Act Regulation (EU) 2024/2847 EUR-Lex ..." | 确认 CRA = Regulation (EU) 2024/2847；2024-12-10 生效；Article 14 报告义务 2026-09-11 起适用（24h/72h/14d）；全面适用 2027-12-11 | 采纳（时间点经多源交叉）→ sources/cra-regulation-2024-2847.md |

## 弃用来源及原因

- api.osv.dev 经 FetchURL：JSON 响应无法正文提取 → 改用 curl（数据本身采纳）。
- federalregister.gov：CAPTCHA 反爬 → EO 14028 内容改以 NIST/NTIA 官方页面佐证。
- csaf.io / oasis-open.github.io/csaf-documentation：正文提取内容过薄 → 直接采用 OASIS 标准原文。
- 二手博客（Socket、Safeguard、The Record、dtvss.io 等关于 NVD 2024 backlog 的文章）：仅用于发现线索，事实均以 NIST 2026-04-15 官方公告为准。

## 来源间冲突 / 注意事项

1. **Log4Shell 受影响版本的三源表述不完全一致**：CVE Record（Apache CNA）用 version+changes 表达（2.15.0 标记 unaffected 后又引出 CVE-2021-45046）；OSV/GHSA 条目拆成三段区间（[2.0-beta9,2.3.1) / [2.4,2.12.2) / [2.13.0,2.15.0)）；NVD 用 CPE configurations 表达。三者语义相同但模型不同——这正是 SCA 需要多源归一化的实证。
2. **CVSS 10.0 的归属**：CVE Record 中 CNA 容器只有非标准的 "critical" 文本；正式 CVSS 3.1 向量来自 CISA-ADP；NVD 视图中另有 NVD Primary 评分。报告中必须区分"谁打的分"。
3. **KEV 的 binding directive 版本**：早期为 BOD 22-01，2026 年目录条目引用 BOD 26-04（含 forensic triage 字段）。报告以现行状态为准并注明演进。
4. **CRA 报告时间点**（24h/72h/14d/1mo）来自多源交叉核实；EUR-Lex 原文页未直接抓取，报告中已注明以法规原文为准。
