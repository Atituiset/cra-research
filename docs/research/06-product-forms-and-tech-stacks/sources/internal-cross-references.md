# Source Note: [04 报告](../../04-technology-deep-dive.md)既有技术栈证据（内部引用汇总）

- 说明: 本 note 非外部来源，而是 [06 报告](../../06-product-forms-and-tech-stacks.md)对项目内 [01](../../01-domain-ontology.md)/[03](../../03-competitive-landscape.md)/[04](../../04-technology-deep-dive.md) 报告已核实来源的引用登记，避免重复落盘。[06 报告](../../06-product-forms-and-tech-stacks.md)在正文中标注"[见 04](../../04-technology-deep-dive.md) / [见 03](../../03-competitive-landscape.md)"处对应以下 source notes。

## 引用的 [04 报告](../../04-technology-deep-dive.md) sources（[docs/research/04-technology-deep-dive/sources/](../../04-technology-deep-dive/sources/)）

- [govulncheck-docs.md](../../04-technology-deep-dive/sources/govulncheck-docs.md) — Go 官方 govulncheck：基于调用分析的漏洞检测，单语言 reachability 被生态"国有化"的标杆。
- [joern-cpg.md](../../04-technology-deep-dive/sources/joern-cpg.md) — Joern Code Property Graph：CPG 作为多语言（含 C/C++）静态分析底座的开源现实。
- [endor-js-reachability-blog.md](../../04-technology-deep-dive/sources/endor-js-reachability-blog.md) / [endor-labs-reachability-docs.md](../../04-technology-deep-dive/sources/endor-labs-reachability-docs.md) — Endor Labs reachability 实现与 CVE→函数映射库（自研程序分析 + 策展数据集）。
- [snyk-agent-fix.md](../../04-technology-deep-dive/sources/snyk-agent-fix.md) — Snyk Agent Fix 架构：前沿模型 + few-shot 修复样本 + SAST re-scan 预筛选。
- [github-copilot-code-review-agentic.md](../../04-technology-deep-dive/sources/github-copilot-code-review-agentic.md) / [github-dependabot-vulnerable-function-calls.md](../../04-technology-deep-dive/sources/github-dependabot-vulnerable-function-calls.md) — GitHub CCR "LLM + deterministic precision"、Dependabot vulnerable function call 检测。
- [semgrep-reachability-whitepaper.md](../../04-technology-deep-dive/sources/semgrep-reachability-whitepaper.md) — Semgrep Supply Chain reachability 白皮书。
- [openssf-guac-readme.md](../../04-technology-deep-dive/sources/openssf-guac-readme.md) — GUAC 生产后端推荐 PostgreSQL/内存 KV，Neo4j 后端 unsupported。
- [wiz-security-graph.md](../../04-technology-deep-dive/sources/wiz-security-graph.md) — Wiz Security Graph 叙事 vs 关系库可复刻证据。
- [darpa-aixcc.md](../../04-technology-deep-dive/sources/darpa-aixcc.md) — AIxCC：确定性工具层 + LLM 编排层的架构实证。

## 引用的 [01](../../01-domain-ontology.md)/[03](../../03-competitive-landscape.md) 报告 sources

- 01: [osv-schema-spec.md](../../01-domain-ontology/sources/osv-schema-spec.md)、[github-advisory-database.md](../../01-domain-ontology/sources/github-advisory-database.md)（OSV/GHSA 数据格式与免费聚合层）。
- [03](../../03-competitive-landscape.md): 各厂商分节（JFrog/Sonatype/Black Duck/Veracode/Checkmarx/Endor/Socket/Arnica/Finite State/ONEKEY 等能力明细）——[06 报告](../../06-product-forms-and-tech-stacks.md)不重复摘录，仅引用其结论。

## 支撑报告结论

- [06 报告](../../06-product-forms-and-tech-stacks.md)聚焦"形态"与"业界实际技术栈"两新维度；凡 [04](../../04-technology-deep-dive.md) 已论证的理论/方法层结论直接引用，不重复取证。
