# Vendor Deep Dive: Endor Labs（第二轮 Competitive Deep Dive）

> 调研日期：2026-09-21 ｜ 基线：[03-competitive-landscape.md §1.10/§6](../03-competitive-landscape.md)（已核实项不重复，本文只做加深）
> 分级约定：**Fact** = 有一手来源（官方文档/官方 GitHub/官方新闻稿/学术论文）；**（厂商声称）** = 营销页或新闻稿表述；**Interpretation** = 基于 Fact 的推断；**Hypothesis** = 方向性猜测；**（不确定）** = 无法核实。
> 来源明细见 [sources/](sources/) 下 9 份 endor- 前缀 notes；过程见 [research-log-endor.md](research-log-endor.md)。

## 0. 一句话定位

Endor Labs 是"**确定性程序分析引擎 + 服务端预计算调用图资产 + 上层 agentic 编排层**"三层结构的 SCA 起家厂商：引擎自研（学术谱系 FASTEN + Eclipse Steady），数据面是所有客户共享的 OSS 预计算集群，2025–2026 年把确定性引擎的产出通过 MCP 暴露给外部 AI agent（AURI），同时把 C/C++ 这类无主语言用 embedding 相似度路线单独补齐。

---

## 1. 产品架构与交付形态

**Fact**（[endor-deployment-models.md](sources/endor-deployment-models.md)）：

- **SaaS 优先，无完全自托管控制面**。官方只承认两种部署模型：
  - **Hybrid scanning**：endorctl 在客户 CI 内完成分析，只有元数据回传 Endor 云；
  - **Cloud scanning**：GitHub App 等，repo 克隆进一次性隔离容器，扫描完即销毁，只留元数据。
- **Outpost**（[docs](https://docs.endorlabs.com/setup-deployment/outpost)）：把 **scheduler** 部署到客户私有 Kubernetes 集群，页面标题称面向 "air-gapped environments"，但**扫描结果仍须回传 Endor 云**——是"扫描执行下沉"，不是控制面离线。且全租户二选一，不能按项目混用云/本地调度。
- **API 优先程度高**：REST API 有 3 份 OpenAPI v3 spec 公开下载，API reference 按数十个 `*Service` 资源服务分组；endorctl 本身即 API 客户端（含 `endorctl api` 裸调用命令）；文档站 Developers & API 部分 313 页，另有一个 **docs 专用 MCP server**。
- 入口面：GitHub/Azure DevOps App、endorctl（Linux/macOS/Windows）、REST API、MCP server、IDE 插件系（经 MCP）。

**Interpretation**：对"源码不出网"的合规客户，Endor 的答案是 Outpost/hybrid 而非私有部署——这对 CRA 场景下的欧盟受监管企业是既够用（元数据出网）又有缺口（控制面与漏洞库更新仍依赖厂商云）的形态。EU 租户（Azure EU + 美国共享 OSS 集群只读元数据）是其对数据主权的折中。

## 2. Reachability 引擎实现

**Fact**（[endor-callgraph-engine.md](sources/endor-callgraph-engine.md)、[endor-precomputed-reachability.md](sources/endor-precomputed-reachability.md)）：

- **自研，且有清晰学术谱系**。2022 技术博客致谢 TU Delft Software Analytics lab 与欧盟 **FASTEN** 项目（Gousios 一派，生态级细粒度调用图）；JS call graph 生成器博客自述 "through the development of Endor Labs' JavaScript call graph generator"；Greenhouse JD 明确岗位职责是"our existing suite of static analysis tools… call graph construction, data-flow and taint analysis, and language-specific analyzers"。无任何基于 CodeQL/Soot/WALA 等现成底座的公开证据。**Henrik Plate**（Eclipse Steady 核心作者）现任其 Security Researcher（Google Scholar 验证邮箱）。
- **核心架构：per-package-version 预计算 + stitch on the fly**。原话："we create a call graph per package version, store those call graphs and then, given a client dependency set, we stitch them on the fly"。API 侧佐证：`CallGraphDataService.GetCallGraphData` 以 PackageVersion 为粒度取调用图；`oss` 共享租户所有客户可读。
- **static 为主、dynamic 做基准**：选 static 是因为"completeness is an absolute must for security analysis"；dynamic call graph 只在内部用于给 static 图做 benchmark 与回归。
- **数据源混合**：源码 + 二进制 artifacts 都用于富化分析（docs 原话），"without a heavy reliance on test coverage"。
- **三级精度降级体系**（本轮新发现的最重要工程事实）：
  1. **Function-level full call graph**（构建成功时的首选，9 语言）；
  2. **Pre-computed reachability**（manifest 级，无需构建；**假设直接依赖全可达**，用服务端预计算的 OSS 包间调用图判断传递依赖漏洞可达性；full scan 构建失败时**默认自动 fallback**；7 语言）；
  3. Dependency-level / 无分析兜底（`Potentially Reachable` 标签）。
- **证据输出形态**：UI 逐跳 call path + API 可读 call graph 资源 + finding 三档标签（Reachable / Potentially Reachable / Unreachable Function）。
- **精度声明**：降噪 80–99%、示例 124→11→2（厂商声称）；**无公开 benchmark 数据集**。
- **口径不一致**：call-graphs 页列 9 语言含 Ruby；endorctl `--languages` 文档列 C#/Go/Java/JS/Kotlin/Python/Rust/Scala/TypeScript **无 Ruby**（不确定——Ruby 实际支持度存疑）。

**自曝局限**（维度 10 交叉）：JS 匿名函数只能靠行号+offset 映射且跨版本漂移；函数指针需要 dataflow tracking 导致 **missed edges**；动态 import 的运行时名静态不可知。

## 3. 漏洞数据库：自建还是聚合？策展流程

**Fact**（[endor-vulndb-curation.md](sources/endor-vulndb-curation.md)）：

- **多源聚合 + 自有策展层**：支持 CVE/GHSA/PySEC/MAL 检索；恶意包（MAL）数据注明来自 **OSV**；漏洞条目含 introduced/fixed 版本、**impacted classes**、**fix commit 链接**、"affected call paths and file paths"、blast radius（多少项目用、多少包依赖）。
- 白皮书自述 "A Multi-Source Vulnerability Database… including our world-class research team… scored by exploitability and severity"。
- **CVE→漏洞函数映射**是 function-level reachability 的数据前提；Endor 自称用程序分析自建跨版本映射（厂商声称，03 报告已录）。**本轮未找到策展流水线（LLM 参与度、人工复核比例、覆盖率）的任何公开技术细节（不确定）**。
- **DroidGPT 定位澄清**：2023 年发布的 DroidGPT 只是 **ChatGPT + Endor 私有风险数据的问答前端**（"combines the power of ChatGPT with Endor Labs' proprietary risk data"），不是策展管线；其角色在 2025–2026 已被 MCP server / Agentic UI / AURI 吸收。

**Interpretation**：行业参照显示 CVE→函数映射的 LLM 半自动化是公开技术路线——DIMVA 2024（Dunlap 等，**NC State + Chainguard**，非 Endor）证明 naive "patch 改动函数即漏洞函数" precision 仅 0.22，LLM 可提到 0.60。Endor 有 Henrik Plate 这种做过人工函数标注系统（Steady）的人，其策展大概率是"程序分析 + 人工 + 可能的 LLM 辅助"混合，但公开证据只到"程序分析自建"这句厂商声称。

## 4. C/C++ 与二进制支持

**Fact**（[endor-ccxx-whitepaper.md](sources/endor-ccxx-whitepaper.md)）：**不是空白，但是一条与主产品线完全隔离的技术路线**。

- 2025-03 Beta、2025-06 白皮书 GA 级发布。方法 = **专有分段算法 → 文件/分段哈希（精确匹配）→ 代码 embedding + 向量数据库（模糊匹配）**，识别复制/修改/无声明的三方代码；embedding 送 **Endor 专属 Azure OpenAI deployment** 生成，默认关闭、需 AI license、显式 opt-in（Data Privacy 开关）。
- 同时支持 **Conan** manifest 扫描。
- 自认局限（原文）：**"Dynamic libraries are not in scope"**；**`.so`/`.a` 二进制扫描不支持**（docs）；依赖未入库则漏报；**"Reachability is not available for C/C++"**（可能 roadmap）；不构建、所有源码须在目录树内。
- 精度声称 143% more TP / 81% fewer FN vs legacy（厂商声称，无公开测试集；白皮书承认无法归因各组件贡献）。

**Interpretation**：C/C++ 走的是"代码指纹 + 语义相似度"的 snippet 匹配路线（对标 Black Duck Protex 式 snippet scan 的 LLM 时代重做），与函数级 reachability 引擎没有交集；**纯二进制/固件 SCA 是真空白**。CRA 覆盖嵌入式设备场景的买方会撞上这两道墙。

## 5. Upgrade Impact Analysis 实现原理

**Fact**（[endor-upgrade-impact.md](sources/endor-upgrade-impact.md)）：

- 输入 = 漏洞差分（当前版 vs 新版及其传递依赖）+ **启发式因子** + **"program analysis to directly identify breaking changes"**。
- 输出 = 四档升级选项（latest / latest vuln-free / most-impactful-moderate-evidence / most-impactful-low-evidence）× 三档 **Remediation Risk**（High/Medium/Low，带 "breaking change confidence" 与逐条 **Remediation Risk Drivers**）。
- Breaking change 六类枚举：API / Behavioral / Transitive dependency / Deprecation-removal / Configuration / Supported platform。另有依赖图 major/minor **版本冲突**分析（Potential Conflicts 面板）。
- 官方明示：**"The absence of evidence does NOT guarantee that it will not break your application"**（Low 档免责）。
- 已知边界（03 已录）：仅 OSS 包、不降级、不含容器/GHA 依赖。付费墙：**OSS Pro**。

**Hypothesis**：结合 2022 博客"Impact = call graph 后向遍历"与 per-package-version 图库存储，其程序分析很可能是**相邻版本函数级 API diff × 本项目实际调用面**的交集——即只报"你真实调用的函数"发生的签名/行为变化。这解释了为什么它能给出"confidence"而非二元判定，但官方未公开 diff 技术细节（不确定）。

## 6. Exploitability / Context 信号采集

**Fact**（[endor-upgrade-impact.md](sources/endor-upgrade-impact.md) 漏斗部分）：

- 官方 **Vulnerability Prioritization Funnel** 固定五级：Total open → **Not in test**（排除测试代码）→ **Fix available** → **Reachable**（可选 Reachable / Potentially Reachable Function）→ **Exploitable likelihood（EPSS > 1%）**。
- 信号来源全部可考：测试代码排除与 fix availability 来自自有扫描与漏洞库；reachability 来自 §2 引擎；**EPSS** 来自 FIRST 公开数据（Findings 页有 EPSS 分数区间过滤器，release notes 佐证）。
- "in production / production context" 信号对应其**容器扫描 + container reachability + instrumented container reachability（Beta）**产品线——即通过容器内包的实际使用来近似运行时上下文（docs 目录佐证）。
- **KEV（CISA）集成未见任何文档证据（不确定）**——排序因子比 Snyk 等少一块公开威胁情报拼图。

**Interpretation**：Endor 的 context 是"**代码上下文重、威胁情报轻**"——把筹码全压在自有程序分析产出的信号上，外部情报只接 EPSS。这与它"evidence over feeds"的叙事一致，但也意味着 KEV 类"已被在野利用"信号需要客户自行补齐。

## 7. AI / Agent 架构

**Fact**（[endor-mcp-auri.md](sources/endor-mcp-auri.md)）：

- **分层架构（官方原话）**："we've built a new **agentic AI layer above that**"——that 指确定性引擎与数据。AURI 新闻稿定位语："combining **agentic reasoning with deterministic static analysis**"。
- **MCP server 是主要 agent 接口**：内嵌于 endorctl（`npx -y endorctl ai-tools mcp-server`），免费开发者层；官方支持 Cursor/Claude Code/Codex/VS Code/Devin/Gemini CLI/Augment/IntelliJ/Antigravity/OpenCode/GitHub AgentHQ **11 个客户端**。
- **工具面薄而结构化**：`scan`（返回 **finding UUID 列表**）、`check_dependency_for_vulnerabilities/risks`（后者含恶意包检测）、`get_endor_vulnerability`、`get_resource`（8 种资源类型）、`security_review`（AI diff 审查，Enterprise 付费墙）。**LLM 拿到的是引擎的结构化产出，不让 LLM 自己判断漏洞**——官方话术 "isn't LLM guesswork or hallucination"。
- **Claude Code Skills 官方仓库**（github.com/endorlabs/skills-ideas）：26 个 slash-command skills + **8 个生命周期 hooks**（装依赖后自动 /endor-check、MCP 错误恢复、会话末提醒 /endor-review，分级 Block/Warn/Suggest）+ always-on rules——把安全动作锚进 agent 的事件流而非靠提示词自觉。
- **确定性校验/防幻觉的两个明确位置**：
  1. MCP tools 只返回确定性引擎结果（finding UUID、CVE 详情、推荐版本）；
  2. Agentic UI（AppSec Assistant）**数据范围硬限制**——"answers based solely on Findings / Scan results / Vulnerabilities / Package versions"，超范围不回答。
- **双向 agent 战略**：对外暴露自家 MCP（被别人的 agent 调用）；对内做 **Coding Agent Governance**（开发者机器上的 hooks 采集 agent/MCP/skills/model 清单 + 策略执行）——治理别人的 agent。
- AURI 的 "specialized agents work together to detect, triage, and remediate"（agent orchestration）与 "code context graph"（一方代码+依赖+容器+AI 模型）目前只有新闻稿级描述（厂商声称），编排实现细节（多 agent 框架、校验点）未公开（不确定）。

## 8. 数据底座与对象模型

**Fact**（[endor-data-model-api.md](sources/endor-data-model-api.md)）：

- **Kubernetes 风格资源模型**：所有对象 = UUID + Meta（kind/parent_uuid/parent_kind/tags/annotations/created_by）+ TenantMeta（**层级 namespace**，`endor.prod.app`）+ Spec + **Context**。
- **Context 隔离扫描代际**：main（默认分支）/ ref（分支）/ ci_run（PR 扫描，**3 周 TTL 自动删**）/ sbom（导入）/ external（同租户跨项目 vendor 依赖，只算 call graph）。同一 repo 的不同扫描产出是不同 context 下的对象集合——**git-centric 的版本观，没有 release/产品版本对象**。
- **共享 `oss` 租户**：所有客户可读——OSS 包元数据、漏洞库、预计算 call graph 的公共服务层（与 trust-compliance 的"美国共享 OSS 集群"互证）。
- **对象模型根是 Project（= git repo URL）**。无 product / 产品线 / 支持期 / 版本发布语义（字段级确认，补强 03 报告 §7 结论）。
- 基础设施可考证据：Azure 托管（EU 租户明示）；向量数据库（C/C++ embedding）；对象存储 + 签名 URL（SBOM/VEX AsyncJob，5 分钟 TTL）；**AIProviderKeyService 支持客户自带 AI provider key（BYOK）**，服务端加密存储。
- 服务身份痕迹：`vulnerabilityingestor@endor.ai@x509`——微服务以 x509 身份写库（与创始人 Aporeto 背景一致的零信任控制面风格，Interpretation）。
- **存储/图数据库选型无任何公开证据（不确定）**。

## 9. 定价与部署模式

**Fact**（[endor-licensing-pricing.md](sources/endor-licensing-pricing.md)）：

- **Per Code Contributor per year**（90 天内有 commit 的人），Microsoft Defender for Cloud FAQ 交叉确认。
- 8 个 SKU 独立售卖：OSS Core/Pro、Code Core/Pro、Package Firewall、Endor Patches、SBOM Hub、Coding Agent Governance。**差异化能力全在付费墙后**：Upgrade Impact / container reachability = OSS Pro；agentic SAST = Code Pro；C/C++ embedding 与 AI chat = AI license。
- **Scan credit 池**（fair usage）：每席位每日 1–1.5 credit 合同期 pooling；5 repo/席位的默认分支无限扫；PR/非默认分支扫描计费；超量 10,000 扫/桶加购，不硬阻断。
- **免费层** = AURI MCP/CLI/IDE（PLG 入口，2026-03 起）。
- 具体价格点**未公开**（不确定）；二手来源称对标 Snyk per-developer（仅参考）。

**Interpretation**：计费模型与"扫描是引擎成本中心"的事实自洽——call graph 构建贵，所以用 credit 池把 PR 级高频扫描变成可计量资源；把"修复类智能"（upgrade impact、patches）而非"检测"放进 Pro，说明其认定商品化的是检测、溢价在修复。

## 10. 工程自曝的局限与坑（汇总）

全部为官方材料自认（各 source note 有原文）：

1. **静态调用图固有不精确**：over-approximation 带来 FP；"for security risk, false negatives can be problematic"（2022 博客）——官方立场是 reachability 用于**优先级排序**而非判定清零。
2. **JS 三类丢边**：匿名函数跨版本身份漂移、函数指针需 dataflow、动态 import 运行时名（JS 工程博客）。
3. **依赖构建成功**：full call graph 需要构建；构建失败率靠 pre-computed reachability 兜，但代价是"直接依赖全可达"的系统性过近似 + 不分析应用对传递依赖的直接调用（pre-computed 文档）。
4. **Upgrade Impact 的 Low ≠ 保证**；仅 OSS 包、不降级、不含容器/GHA。
5. **C/C++**：无 reachability、动态库出界、二进制不支持、库未入库即漏报。
6. **Outpost 全租户二选一**，且结果仍须出网——"air-gapped" 名实之间有缝。
7. **语言口径不一致**（Ruby 在/不在两个官方清单）。

---

## 11. 对我们产品的启示

1. **"预计算 + stitch"是 reachability 规模化的答案，且图资产应是一等 API 资源**。Endor 把 per-package-version call graph 存成可 `GetCallGraphData` 的资源，客户端构建失败时还能降级成 manifest 级查询。我们的 evidence graph 设计可借鉴：图资产服务端化、分粒度缓存、证据链作为独立对象可检索——并比 Endor 多走一步：**把机器判定（含 call chain）落成 VEX justification 对象**（03 §7 已确认 Endor 也没做这一步，仍是全行业断裂点）。
2. **三级降级体系（full call graph → pre-computed → dependency）是企业落地的必修课，不是可选项**。构建失败率决定 reachability 的真实覆盖率；每级都要有自己的证据标签与保守度假设声明（Endor 的"直接依赖全可达"明示是范本），否则"reachability 覆盖广"就是营销数字。我们的覆盖度披露应按这三档分别计量。
3. **AI 层的可信模式 = 确定性引擎在下 + 薄结构化 MCP 工具面 + 数据范围硬 grounding**。Endor 不让 LLM 判漏洞，只让 LLM 编排与叙述，并把回答数据域写死在平台对象内；hooks 把安全动作锚进 agent 生命周期事件（Block/Warn/Suggest 分级）。这直接回应 03 报告"agentic remediation 可信度基础设施"的缺口判断：校验器必须独立于生成器，且校验输入来自确定性引擎。

## 12. 无法核实项清单

| 项 | 状态 |
| --- | --- |
| CVE→漏洞函数策展流水线细节（LLM 参与度、人工复核比例、语言覆盖） | （不确定）——仅"程序分析自建"厂商声称 |
| 存储/图数据库选型 | （不确定）——无任何公开证据 |
| CISA KEV 是否进入排序因子 | （不确定）——文档仅见 EPSS |
| Ruby call path 实际支持度 | （不确定）——两处官方文档口径不一致 |
| AURI "specialized agents" 编排实现与确定性校验点细节 | （不确定）——新闻稿级描述 |
| 具体价格点 | （不确定）——无公开价目 |
| 二进制/固件 SCA | 已确认**不支持**（`.so`/`.a` 明确出界），无 roadmap 证据 |
| DroidGPT 是否仍在维护 / 与 AURI 的关系 | （不确定）——2023 年后无官方更新 |
