# Research Log: Endor Labs 厂商深挖（第二轮 Competitive Deep Dive）

- 日期： 2026-09-21
- 执行： 子代理调研（research skill 流程，主 agent 委派的第二轮厂商深挖）
- 范围： 10 个深挖维度（架构/交付、reachability 引擎、漏洞库策展、C/C++/二进制、Upgrade Impact Analysis、exploitability 信号、AI/Agent 架构、数据底座/对象模型、定价部署、自曝局限）
- 基线： docs/research/03-competitive-landscape.md §1.10 与 §6（不重复，本轮只加深）

## 过程时间线

1. **读基线**：03 报告 Endor 节 + §6 闭环核实 + 已有两份 endor source notes（endor-lifecycle-chain.md、endor-reachability-framework.md）。确认已核实项：9 语言 function-level reachability、call chain 证据、Upgrade Impact "program analysis"、SBOM/VEX 三通道导出。
2. **检索部署形态**（WebSearch）→ 命中 docs.endorlabs.com/setup-deployment/outpost 与 trust-compliance；FetchURL 两页全文。确认：SaaS 优先 + hybrid/Outpost 下沉扫描执行，无全自托管控制面；Azure 主云 + EU 租户 + 美国共享 OSS 集群。
3. **检索 reachability 实现** → 命中 2022 技术博客（what-is-reachability-based-dependency-analysis，含 FASTEN/Gousios 致谢与 store+stitch 架构）、call-graphs docs、JS 难点工程博客（2024-12）。全部 FetchURL 全文。确认自研引擎、动态图做内部基准、JS 丢边自曝。
4. **检索 MCP/AI** → 命中 MCP 发布博客、github.com/endorlabs/skills-ideas（完整 MCP Tools Reference + 26 个 Claude Code skills + 8 hooks）、AURI 新闻稿（2026-03-03）、docs agentic-ui。全部抓取。确认"确定性引擎+agentic 层"架构与数据 grounding 硬限制。
5. **检索漏洞库策展** → docs vulnerability-db 页（CVE/GHSA/PySEC/MAL + impacted classes + fix commit + affected call paths）；DroidGPT 2023 发布转载（定位为 ChatGPT 问答前端而非策展流水线）；命中 DIMVA 2024 论文 PDF 并全文抓取（enck.org）——**核实作者单位为 NC State + Chainguard（Trevor Dunlap 在 Chainguard），不是 Endor**，故仅作行业方法参照，不作为 Endor 实现证据。Henrik Plate 任职 Endor 经 Google Scholar 验证邮箱佐证。
6. **检索 C/C++** → 命中官网 CDN 白皮书 PDF（2025-06-18）并全文抓取 + docs C/C++ 页。确认 segment+hash+embedding（Azure OpenAI）路线、reachability 缺失、`.so`/`.a` 不支持、动态库不在范围。
7. **检索 Upgrade Impact / 排序** → docs upgrade-impact-analysis 全文（四要素输入、四档选项、三档风险、六类 breaking change、Low≠保证）+ OSS overview 优先级漏斗（test 排除→fix available→reachable→EPSS>1%）。
8. **检索数据底座** → docs llms.txt 索引（277+313 页、OpenAPI v3 spec、*Service 分组）、data-model/common-fields 与 resource-kinds 全文。确认 K8s 风格资源模型、context 扫描隔离、`oss` 共享租户、CallGraphDataService、AIProviderKey BYOK。
9. **检索定价** → docs licenses 全文（per contributor/year、8 个 SKU、scan credit 池）+ Microsoft Learn FAQ 交叉确认。价格点无公开数字。
10. **检索 JD 佐证技术栈** → Greenhouse Program Analysis Engineer JD 全文：自研 static analysis 套件（call graph/data-flow/taint/语言分析器）+ ML-for-code 实验；要求 Java/Python/Go。佐证引擎自研与工程语言栈。

## 弃用/降级来源记录

- **appsecsanta.com / ssojet.com / rightaichoice.com / coruzant.com / pricingsaas.com / softwr.com / pixee.ai / heeler.com / safeguard.sh**：二手测评/竞品页，仅用于旁证定价未公开与市场定位，不作为技术事实来源。Safeguard 提到 "station deployment model"，官方文档未见此名词（疑指 Outpost 或过时叫法），标（不确定）未采信。
- **DIMVA 2024 论文**：高质量一手学术来源，但**非 Endor 成果**，仅作"CVE→函数映射 LLM 化是行业公开路线"的参照，正文明确标注归属（NC State/Chainguard）。
- **venturebeat.com AURI 报道**：抓取受限未读全文，仅用搜索快照中"code context graph"引语并与 PR Newswire 官方稿互证。
- **免费层细节**（softwr 称 "Developer tier… read-only"）：未经官方文档核实，未采信具体限制描述。
- **KEV 集成**：文档与 release notes 检索未见，标（不确定），不断言有无。

## 产出

- 主文档： docs/research/07-vendor-deep-dive/endor-labs.md
- 来源 notes： docs/research/07-vendor-deep-dive/sources/ 下 9 份（endor- 前缀）：
  - endor-deployment-models.md（维度 1）
  - endor-callgraph-engine.md（维度 2、10）
  - endor-precomputed-reachability.md（维度 2、10）
  - endor-ccxx-whitepaper.md（维度 4）
  - endor-upgrade-impact.md（维度 5、6）
  - endor-mcp-auri.md（维度 7）
  - endor-data-model-api.md（维度 8）
  - endor-vulndb-curation.md（维度 3）
  - endor-licensing-pricing.md（维度 9）

## 遗留问题（供后续轮次）

1. Endor 的 CVE→函数映射策展流水线细节（LLM 参与度、人工复核比例）无公开信息。
2. 存储/图数据库选型无公开证据（API 风格暗示 K8s 式资源存储，但无数据库层证据）。
3. KEV 是否进入排序因子未见文档证据。
4. Ruby 支持口径不一致（call-graphs 页有、CLI `--languages` 无）。
5. AURI 的 "specialized agents" 编排实现细节（是否多 agent 框架、确定性校验点位置）仅有新闻稿级描述。
