# Research Log — 04 Technology Deep Dive

调研日期：2026-09-18。按时间顺序记录 query、采纳/弃用来源及原因、来源间冲突。

## 2026-09-18

### Query: "Endor Labs reachability analysis function-level call graph technical blog how it works"
- 采纳: docs.endorlabs.com/scan/sca/reachability-analysis（官方文档，已 fetch，note: `endor-labs-reachability-docs.md`）
- 采纳: endorlabs.com/learn/why-reachability-analysis-for-javascript-is-hard-and-how-we-fixed-it（厂商工程博客，待 fetch）
- 采纳: semgrep.dev reachability whitepaper PDF（厂商白皮书，含对竞品粒度定义的批评，注意其立场偏向自家产品）
- 弃用: reddit r/devsecops 帖（二手、 anecdotal，仅作旁证）；safeguard.sh / konvu.com / pixee.ai 对比文（二手解读/竞品营销，只用于发现线索不作事实引用）

### Query: "Snyk reachability analysis supported languages Java JavaScript technical documentation"
- 发现冲突线索：konvu.com 对比称 "Snyk reachability GA 覆盖 Java/JS/TS/Python、C# EA，但其自家 Risk Score 页只写 Java/JS"——需以 Snyk 官方文档为准核实。
- 采纳计划: docs.snyk.io reachability 官方页（待 fetch）

### Query: "GitHub Dependabot reachability call graph public beta vulnerable function calls 2025"
- 采纳: github.blog changelog 2022-04-14 "Dependabot alerts show vulnerable function calls (Python Beta)"（一手官方 changelog；说明 GitHub 2022 年即上线基于 precise code navigation 的 vulnerable function call 检测）
- 注：搜索未发现 2025 年 GitHub 对 Dependabot call graph 的新 GA 公告；GitHub 的依赖可达性能力长期停留在"是否调用 vulnerable function"提示层面。

### Query: "vulnerability reachability analysis function level academic paper arxiv call graph dependency Java soundness"
- 采纳: arXiv 2506.17798 "Savant: Vulnerability Detection in Application Dependencies through Semantic-Guided Reachability Analysis"（学术论文）
- 采纳: arXiv 2408.02846 "Less Is More: ... Security-Sensitive API Calls in Java"（学术论文，其中提到开源 Java call graph 工具无法累积依赖可达 API，需用私有工具）
- 采纳: TOSEM-2025 ReachCheck（call graph reachability 用于依赖冲突与 CVE 风险检测）
- 采纳: snyk.io/blog/reachable-vulnerabilities (2020)（厂商博客，Snyk 2020 年即公开 call graph reachability 思路）

### Query: "CISA SSVC ... decision tree"
- 采纳: CISA SSVC 官方页面（待 fetch）；GitHub OpenCTI connectors issue #7068（佐证 CISA 通过 Vulnrichment ADP 发布 SSVC decision points：Exploitation/Automatable/Technical Impact）；BOD 26-04 强制联邦机构使用 SSVC（待核实一手来源）
- 采纳: VulnCheck blog "automating SSVC"（厂商博客，SSVC 自动化实践）

### Query: "OpenSSF GUAC ..."
- 采纳: github.com/guacsec/guac README（开源项目一手）；docs.guac.sh/guac/guac-components（官方文档：Collectors/Ingestor/本体，支持 SPDX/CycloneDX/SLSA/in-toto/CSAF VEX/OSV，GraphQL 查询，后端可用 Neo4j/arangodb/ent 等——以 docs 为准）

### Query: "EPSS FIRST model documentation ..."
- 采纳计划: first.org/epss 官方页（待 fetch）。多个二手来源一致称 EPSS v4 于 2025-03-17 发布、ROC AUC 0.838、估计未来 30 天被利用概率——需以 FIRST 官方核实。
- 新线索: NIST 2025-05 发布 "Likely Exploited Vulnerabilities (LEV)" 白皮书，基于 EPSS——待核实一手来源。

### Query: "VEX not_affected justification ... automation"
- 采纳: docs.anchore.com vuln annotations（官方文档，列出 CISA 五种 justification 的机器可读值）
- 采纳: SPDX 3.0.1 spec PDF 8.3.4 VexJustificationType（标准组织一手）
- 采纳: provenvex.com "Evidence-backed VEX"（厂商/项目博客，主张"exploitation proof"支撑 VEX；立场性来源，用作观点）
- 采纳: devguard.org blog（CRA 场景 VEX 实践，二手）

### Query: "govulncheck ... how it works"
- 采纳: pkg.go.dev 官方文档（已 fetch，note: `govulncheck-docs.md`）——含官方自述 limitations，是 Go 可达性边界的一手证据。

### Query: "agentic AI vulnerability remediation 2025 2026 ..."
- 采纳: github.blog changelog 2025-10-28（Copilot code review / Autofix：称 2025 年 Autofix 修复 100 万+ 漏洞；待 fetch 一手）
- 采纳: corgea.com/learn/auto-remediation-tools、pixee.ai 对比页（竞品厂商，用于确认 Snyk Agent Fix 更名自 DeepCode AI Fix 等事实线索，最终引用以 Snyk 官方为准）
- 采纳: CSA research note PDF（labs.cloudsecurityalliance.org，2026-03，AI 漏洞扫描市场研究，引用 Snyk Labs "Copilot amplifies insecure codebases" 与 Pillar Security SWE agents 风险研究——作为反面证据线索）

### Query: "Oligo Security runtime reachability eBPF ..."
- 采纳: oligo.security/blog/loaded-vs-executed-libraries（note: `oligo-runtime-reachability.md`）
- 发现: Coana 白皮书（module/function/network 三层 reachability 定义，值得引用分层口径）；Datadog State of DevSecOps 2025 "18%" 数据线索。

### Query: "breaking change detection API compatibility tools ..."
- 采纳: docs.renovatebot.com/merge-confidence（官方）、github.com/obi1kenobi/cargo-semver-checks（开源）（note: `breaking-change-tools.md`）
- 补充（常识级核实）: japicmp/revapi（Java）、gorelease（Go）、griffe（Python）真实存在。

### Query: "Datadog State of DevSecOps 2025 ..."
- 采纳: datadoghq.com 官方新闻稿 + 报告页（note: `datadog-state-of-devsecops-2025.md`）。注意：18% 数字来自厂商自有算法与遥测，非独立研究。

### Query: "Endor Labs Endor Patches backport ..."
- 采纳: github.com/endorlabs/endor-patches（开源）+ 官方博客（note: `endor-patches.md`）

### Query: "Joern code property graph ..."
- 采纳: github.com/joernio/joern、docs.joern.io（note: `joern-cpg.md`）；发现 arXiv 2603.24837 codebadger（Joern CPG 封装为 MCP server）。

### Query: "LLM AI agent vulnerability triage accuracy study hallucination ..."
- 采纳: simbian.ai AI SOC benchmark（61–67%，厂商立场，note: `simbian-ai-soc-benchmark.md`）；线索：Ghost Security 91% SAST 误报、arXiv 2407.12241 76% 告警无关（未独立核实，标不确定）。

### Query: "DARPA AIxCC final 2025 Team Atlanta ..."
- 采纳: arXiv 2602.07666 SoK、Team-Atlanta/aixcc-afc-atlantis、Fuzzing Brain 论文（note: `darpa-aixcc.md`）

### Query: "Snyk AppContext ..."
- 结果: Snyk 侧对应物为 AppRisk application context（2024 起，与 Orca runtime context 集成）；未找到名为 "AppContext" 的独立图产品——用户任务中的 "Snyk AppContext" 说法存疑，报告中如实标注。Aptori 有 "Application Context Graph"（厂商）。

### Fetch: docs.snyk.io reachability-analysis
- 首次 URL 404，经 site: 搜索定位正确 URL 后 fetch 成功（note: `snyk-reachability-docs.md`）。页面确认 GA 语言 = Java/JS/TS/Python，C# EA；含 FP/FN 权衡与 "NO PATH FOUND ≠ unreachable" 的官方声明。

### Fetch: endorlabs.com JS reachability blog
- 成功（note: `endor-js-reachability-blog.md`）。92% 降噪为厂商营销数字。

### Fetch: first.org/epss、cisa.gov SSVC、github.com/guacsec/guac、in-toto.io、pkg.go.dev govulncheck、github.blog 两条 changelog
- 均成功，均已写 note。

### Fetch: CISA VEX minimum requirements 着陆页
- 404；通过 arXiv 2503.14388 参考文献拿到 PDF 直链（2023-04）。五种 justification 枚举经 Anchore 官方文档与 SPDX 3.0.1 spec §8.3.4 交叉印证。

### Query: "Snyk Agent Fix site:snyk.io"
- 采纳: snyk.io 三篇官方博客 + docs（note: `snyk-agent-fix.md`）。确认 2026 年 Snyk 已上线 agentic Agent Fix 架构 + CLI Remediation Agent；Golden Test benchmark 数据为厂商自述。

### 来源冲突记录
1. Snyk reachability 语言覆盖：konvu.com 称文档自相矛盾（Risk Score 页只写 Java/JS）；以 2026-09-15 更新的官方 reachability 页为准：GA = Java/JS/TS/Python。
2. arXiv 2506.17798 标题在 v3 从 "Savant" 改为 "CognixShield"——引用时注意版本。
3. Endor "95% 漏洞在 transitive 依赖"与其营销口径一致但属厂商自研报告；Snyk/Endor/Semgrep 的降噪百分比（91%/92%/…）分母各不相同，不可横向比较。
4. GUAC README 的 "graph database" 叙事 vs 其后端实际（Neo4j 后端 unsupported/incomplete，生产推荐 keyvalue/ent+PostgreSQL）——"图"是数据模型而非存储技术。
