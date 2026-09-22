# 04 — 技术路线深挖：Reachability / Exploitability / Agentic Remediation / Evidence Graph

> **2026-09-23 许可口径修正：** CodeQL 的查询与库开源，不等于 CLI 分析引擎开源或可无条件用于私有代码。见 [CodeQL 官方仓库](https://github.com/github/codeql) 与 [CLI 使用条件](https://docs.github.com/en/code-security/concepts/code-scanning/codeql/codeql-cli)。

> **开源选型专题已独立成篇：** [08 — 开源生态与集成选型](08-open-source-ecosystem.md)。按当前评估引擎架构查看项目能力、输入输出、许可边界与本仓库验证状态；本文保留方法分析及原研究背景。

> 调研日期：2026-09-18。标注约定：**[Fact]** 有一手来源支撑；**[Interpretation]** 基于事实的推断；**[Hypothesis]** 待验证假设；不确定处显式标注"（不确定）"。
> 每个重要引用对应 [04-technology-deep-dive/sources/](04-technology-deep-dive/sources/) 下一条 source note；调研过程见 [research-log.md](04-technology-deep-dive/research-log.md)。

## TL;DR：三个方向的壁垒判断（详细论证见第六章）

| 方向 | 壁垒判断 | 一句话依据 |
|---|---|---|
| Reachability | **工程壁垒（非技术壁垒）** | 方法全部公开、工具链成熟（govulncheck、Joern 提供开源底座；CodeQL CLI 有独立授权条件），Endor/Snyk/GitHub/Semgrep 均已产品化；难在每语言 2–3 人年的引擎工程与漏洞→函数映射数据策展，不在算法新颖性 |
| Exploitability | **仅产品功能（决策框架层），但其中"证据化 VEX"有工程壁垒成分** | SSVC/EPSS/KEV/CVSS 全是公开框架与开放数据；真正的难点是 context 数据的获取与可信度，而非决策模型本身 |
| Evidence Graph + Agentic Remediation | **Evidence Graph 是潜在真壁垒（数据资产+信任位），Agentic 编排是工程壁垒** | GUAC/in-toto/SLSA 证明了模型可行但没有人在"安全结论级证据链"上建立标准；CRA 合规场景下"可审计证据"是买方的付费点。Agent 本身（AIxCC、Copilot、Snyk Agent Fix 已验证模式）会被快速追平 |

---

## 一、Reachability 实现技术深挖

### 1.1 粒度层级：先统一口径

厂商营销中 "reachability" 一词覆盖了差异巨大的多个粒度 [Fact，见 Semgrep 白皮书对粒度混淆的批评](https://semgrep.dev/assets/content/whitepapers/semgrep-reachabilityanalysis-whitepaper-1225.pdf)：

1. **Package/Dependency Reachability**：依赖包是否被 import/use（Endor 称其为 dependency-level，默认全语言支持 [Fact](https://docs.endorlabs.com/scan/sca/reachability-analysis)）。
2. **Module/File Reachability**：漏洞所在模块是否被加载（运行时视角，Oligo/Coana 的 module-level）。
3. **Symbol/Function Reachability**：从应用代码到 vulnerable function 是否存在调用路径——业界主流宣称的 "function-level"。
4. **Call Path Reachability**：给出完整的 entrypoint→…→vulnerable function 调用链（govulncheck `-show traces`、Snyk call path 展示均支持 [Fact](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck)）。
5. **Vulnerable Branch/Condition Reachability**：不仅函数可达，且触发漏洞的具体分支/前置条件可达（需要 path-sensitive 分析，工业界基本没有规模化产品；学术上 CognixShield 用 PoV 编码触发条件 [Fact](https://arxiv.org/abs/2506.17798)）。
6. **Runtime Reachability**：生产环境中函数**实际被执行**（Oligo eBPF 区分 loaded vs executed [Fact](https://www.oligo.security/blog/loaded-vs-executed-libraries)）。

### 1.2 方法谱系：每种方法能支撑到什么粒度

| 方法 | 可支撑粒度 | 说明与代表工具 |
|---|---|---|
| Manifest/lockfile 解析 | Package | 传统 SCA 基线；Endor "pre-computed reachability" 用 manifest + direct→transitive 使用关系做无构建近似 [Fact](https://docs.endorlabs.com/scan/sca/reachability-analysis) |
| AST 模式匹配 | Symbol（弱） | 只回答"import 了没有"，Semgrep 基础能力 |
| Call Graph | Function / Call Path | 主力方法。Java: Soot/WALA/OPAL；多语言: CodeQL、Joern(CPG)；Go: golang.org/x/tools callgraph（govulncheck 底座）[Fact] |
| CFG + path-sensitive 分析 | Vulnerable Branch | 学术工具（Joern CPG 可查 CFG/PDG [Fact](https://github.com/joernio/joern)）；规模化昂贵 |
| Data Flow / Taint Analysis | Branch + input-controllable | 回答"攻击者输入能否到达 sink"，已属 exploitability 范畴；CodeQL/Joern/Semgrep 支持 |
| Pointer Analysis | 提升 call graph 精度 | Java 反射/函数指针/虚调用解析的关键；成本随精度指数上升（学术界 soundiness 争论的核心） |
| 动态分析 / Runtime Telemetry (eBPF, IAST) | Runtime | Oligo(eBPF)、Datadog ASM、Contrast IAST；观测窗口有限，"未执行≠不可执行"（不确定各产品的具体误报率） |
| Binary Analysis | Symbol（粗）→ Function（难） | govulncheck `-mode binary` 用符号表匹配但**无 call stack** [Fact](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck)；剥离符号的 C/C++ 二进制需二进制相似度/反汇编重建调用图（Joern 支持二进制前端），精度显著下降 |
| Build System / Compilation Database | Module/File（C/C++ 必需） | compile_commands.json 提供预处理后的真实编译单元，是 C/C++ 分析的前提；也用于确定"哪个版本/哪个配置真正进入产物"（支撑 `vulnerable_code_not_present` 判定） |

### 1.3 语言差异：技术挑战与现有工具（均已核实真实存在）

- **Go — 最可行 [Fact]**：静态编译、反射少、官方数据标注到 symbol。`govulncheck` 用 call graph 做 function-level 分析并输出调用栈，且可直接输出 **OpenVEX**。官方自述局限：函数指针/interface 保守分析可能 FP；`reflect`/`unsafe` 导致 FN；二进制模式无调用栈。([govulncheck docs](https://pkg.go.dev/golang.org/x/vuln/cmd/govulncheck))
- **Java — 可行但数据贵**：字节码规整，Soot/WALA/Doop 成熟；难点在反射、动态代理、ClassLoader、ServiceLoader。学术界的痛点是**跨依赖的可达 API 累积没有开源工具直接支持**（arXiv 2408.02846 只能用私有工具 [Fact](https://arxiv.org/pdf/2408.02846)）。Snyk/Endor 的 Java reachability 均为 GA。Endor 2022 年博客即公开其 Java 分析栈思路 [Fact](https://www.endorlabs.com/learn/what-is-reachability-based-dependency-analysis)。
- **JavaScript/TypeScript — 最难的主流语言 [Fact]**：Endor 工程博客详述四大难点——NodeJS 嵌套 node_modules 多版本解析、模块顶层代码 import 即执行、匿名函数无稳定符号名（版本间行号漂移）、回调/函数指针丢边（[Endor JS blog](https://www.endorlabs.com/learn/why-reachability-analysis-for-javascript-is-hard-and-how-we-fixed-it)）。另有打包器（webpack/rollup）把依赖内联进 bundle，源码与运行时代码形态断裂。
- **Python — 中等偏难**：动态类型 + monkey patching + `getattr`，静态 call graph 天然不精确。GitHub 2022 年用 precise code navigation（stack graphs）做了 Dependabot vulnerable function calls（Python beta）[Fact](https://github.blog/changelog/2022-04-14-dependabot-alerts-show-vulnerable-function-calls-python-beta/)；Snyk Python reachability 已 GA（pip/poetry/pipenv）[Fact](https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis)。
- **C/C++ — 最难且最缺产品**：预处理宏使源码形态≠编译形态（必须先有 compilation database）；函数指针/虚函数需 pointer analysis；交付物常为**剥离符号的二进制**，call graph 要靠反汇编重建；嵌入式/固件场景甚至拿不到完整构建。可用底座：Joern CPG（源码/字节码/二进制）[Fact](https://github.com/joernio/joern)、CodeQL（需要可构建）、商业 Coverity/CodeSonar。没有 govulncheck 式的官方免费工具。模糊测试侧 OSS-Fuzz 的 Fuzz Introspector 用编译时插桩做函数可达性（真实存在，作为"instrumentation 路线"参照）。
- **Rust — 工具链刚起步**：`cargo-geiger` 只做 unsafe 统计（不是 reachability）；`cargo-audit` 只做 advisory 匹配（无 reachability）；`cargo-semver-checks` 做 API 兼容而非漏洞可达（[GitHub](https://github.com/obi1kenobi/cargo-semver-checks)）。Rust 的 trait 单态化对 call graph 友好，但缺漏洞→symbol 标注数据（不确定 2026 年是否有官方 reachability 计划）。

### 1.4 学术与工业现状：soundness/precision 权衡与真实水位

- **学术界 [Fact/Interpretation]**：reachability = call graph 可达性是标准基线（VAScanner、ReachCheck/TOSEM-2025 用于依赖冲突与 CVE 风险检测）；前沿已转向 branch/condition 级与 LLM 混合（CognixShield：AST 分片 + 多 agent RAG + PoV-guided 推理，57 个 Java 应用上 P84/R95，预印本自述 [Fact](https://arxiv.org/abs/2506.17798)）。Java call graph 的 soundiness 问题（反射等动态特性下"基本 sound"）在学术界是公开结论。
- **工业界 [Fact]**：
  - Endor Labs：三档分级（function/dependency/pre-computed），function-level 要求**可成功构建**；构建失败退化为 manifest 近似。([docs](https://docs.endorlabs.com/scan/sca/reachability-analysis))
  - Snyk：fix commit→DeepCode AI 找 root cause 元素→双 call graph 路径匹配→安全专家抽检；**无需构建**；官方明确 "NO PATH FOUND ≠ 不可达/不可利用"，并对特定环境做 **under-approximation**。([docs](https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis))
  - GitHub：2022 年起 Dependabot 提示"是否直接调用 vulnerable function"（Python beta 起步）。
  - Semgrep Supply Chain：direct dependency reachability（基于自家 SAST 引擎），并在白皮书中批评把 package 级过滤称作 reachability 是过度包装。
  - Mend/JFrog：均有 reachability 功能宣称（本次未核实到官方技术细节，不确定粒度）。
- **已知误报/漏报共识 [Fact]**：Snyk 官方文档承认静态分析只能在"找到至少一条路径"时证明可达，**无法证明不可达**（reflection、动态行为、控制流缺口）；govulncheck 官方列举 reflect/unsafe 漏报。即：**"reachable" 是强证据，"unreachable" 是弱证据**——这对下游 VEX 自动化是结构性约束（见第二章）。

### 1.5 关键问题回答

**function-level reachability 在各语言上是否工程可行？**
- Go/Java：已验证可行且产品化（官方工具或多家 GA）。[Fact]
- Python/JS：可行但精度打折，需要厂商自研引擎 + 人工校验兜底（Snyk/Endor/GitHub 均已落地）。[Fact]
- C/C++/Rust：技术上可行（Joern/CodeQL 底座在），工程上昂贵，产品化最薄弱——**这恰是 CRA 覆盖的嵌入式/IoT 产品的主要语言，供需错位明显**。[Interpretation]

**最大的落地障碍是什么？[Interpretation，按重要性排序]**
1. **漏洞→函数映射数据**：reachability 引擎本身不难，难的是每条 CVE 要标注"哪个函数/版本区间引入、哪个 commit 修"——这是持续的数据策展投入（Snyk 用 fix commit enrichment + 安全专家；Go 团队人工策展 vuln.go.dev）。这是 reachability 真正的成本中心。
2. **可构建性要求**：全量 call graph 通常要求项目可构建（Endor full scan）；企业客户的构建环境千差万别。
3. **多语言引擎矩阵**：每语言一套 frontend + 持续跟进语言演进，2–3 人年/语言量级（估计值，不确定）。
4. **"unreachable" 的证明力不足**：不能用于强结论，只能用于降噪排序，限制了其在合规断言中的用法。

---

## 二、Exploitability 决策模型

### 2.1 判定链的工程化 [Interpretation]

```
Present（SBOM/SCA 可判定，deterministic）
  → Affected（version range 匹配，deterministic，但 CPE/PURL 映射有 FP）
    → Reachable（call graph；reachable=强证据，unreachable=弱证据）
      → Input-controllable（taint analysis；部分 deterministic）
        → Precondition satisfied（配置/feature flag/分支条件；需上下文数据 + 人工/LLM）
          → Exploitable（PoC/运行时观测/攻击路径；证据最强但最贵）
```

工程化的核心洞察：**判定链上越靠右，证据成本越高、可自动化程度越低，且没有任何单一引擎能走完**——这正是 SSVC 式"决策点 + 人工校准"框架比"端到端 AI 判定"更现实的原因。

### 2.2 决策因子如何组合：规则 > 打分 > 裸 LLM [Interpretation]

三类机制的实证依据：

- **规则/决策树（推荐主框架）**：CISA SSVC 用 5 个 decision point（Exploitation status / Technical Impact / Automatable / Mission Prevalence / Public Well-being Impact）输出 Track/Track\*/Attend/Act 四级动作 [Fact](https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc)。SSVC 的价值在于**每个决策点可独立溯源**、决策路径可解释可审计——天然契合 CRA 证据要求。CISA 已通过 Vulnrichment 把 Exploitation/Automatable/Technical Impact 三个点以 CVE ADP 形式机器化发布 [Fact，OpenCTI connectors #7068 佐证](https://github.com/OpenCTI-Platform/connectors/issues/7068)。
- **打分（辅助排序，不可直接做结论）**：CVSS 是 severity；EPSS v4（2025-03 发布）是"未来 30 天在野利用概率"的 ML 模型，每日更新、数据全开放 [Fact](https://www.first.org/epss)；KEV 是已观测利用的布尔事实。三者回答三个不同问题，**不应融合成一个分数**（FIRST 官方建议组合使用而非替代）。Snyk 的 Risk Score、Endor 的多因子过滤是产品化打分先例。
- **LLM 判断（只可做建议层）**：裸 LLM 安全告警 triage 准确率 61–67%（Simbian benchmark，厂商来源 [Fact](https://simbian.ai/blog/the-first-ai-soc-llm-benchmark)）——不够格独立产出 exploitability 结论；适合做的是：把各确定性信号汇总成人可读的 decision rationale，或填充 SSVC 决策点的**建议值**由人确认。

**部署上下文的杠杆最大**：Datadog 基于数万应用遥测发现，仅 18% 的 CVSS-critical 依赖漏洞在叠加 runtime context（生产环境/互联网暴露）后仍为 critical [Fact](https://www.datadoghq.com/about/latest-news/press-releases/datadog-state-of-devops-2025/)。[Interpretation] 这意味着对多数客户，"exposure + 生产标记"的性价比高于 function-level call graph——reachability 叙事的优先级应排在 context 之后。

### 2.3 VEX 四状态如何由机器证据支撑

- 标准基础 [Fact]：CISA《Minimum Requirements for VEX》定义四 status + `not_affected` 必须附 justification，五种机器可读 justification（`component_not_present` / `vulnerable_code_not_present` / `vulnerable_code_not_in_execute_path` / `vulnerable_code_cannot_be_controlled_by_adversary` / `inline_mitigations_already_exist`）见 [CISA PDF（2023-04）](https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf)、[Anchore docs](https://docs.anchore.com/current/docs/vulnerability_management/vuln_annotations/)、[SPDX 3.0.1 §8.3.4](https://spdx.dev/wp-content/uploads/sites/31/2024/12/SPDX-3.0.1-1.pdf)。
- justification 与证据类型的映射 [Interpretation]：

| Justification | 可由什么机器证据支撑 | 可信度 |
|---|---|---|
| component_not_present | SBOM diff / binary 成分分析 | 高，deterministic |
| vulnerable_code_not_present | 编译配置/构建记录证明文件未进产物；patch hunk 定位 + 文件存在性 | 高，deterministic |
| vulnerable_code_not_in_execute_path | call graph "no path found" | **中低**——静态不可达不可证明（Snyk/govulncheck 官方局限），应降级为 `under_investigation` + 人工确认，或叠加 runtime telemetry 加强 |
| cannot_be_controlled_by_adversary | taint analysis 无路径 + 网络暴露面数据 | 中，需保守 |
| inline_mitigations_already_exist | 配置核查/WAF 规则/mitigation 检测 | 中，依赖环境数据 |

- 自动化先例 [Fact]：govulncheck 原生输出 OpenVEX；VulnCheck 等已做 SSVC 决策自动化。但反证同样存在：arXiv 2503.14388 "Vexed by VEX tools"（2025）实证发现容器扫描器 + VEX 工具链对同一漏洞的判定**不一致** [Fact](https://arxiv.org/html/2503.14388v1)——机器生成 VEX 的可靠性远未标准化。
- [Interpretation] 结论：`not_affected` 自动化的可行路径是"**deterministic 证据能支撑的两个 justification 全自动；execute_path 类降级为半自动 + 证据附件 + 人工签核**"。把不可达的弱证据包装成强结论，是合规场景的实质性风险。

### 2.4 可参考的公开方法论清单 [Fact]

- **CISA SSVC**（决策树框架，首推）：https://www.cisa.gov/stakeholder-specific-vulnerability-categorization-ssvc ；SEI 白皮书 v2.0 含 Supplier/Deployer/Coordinator 角色树。
- **FIRST EPSS**（利用概率先验）：https://www.first.org/epss
- **CISA KEV**（已观测利用事实）：https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **NIST LEV**（Likely Exploited Vulnerabilities，2025-05 白皮书，基于 EPSS 估计 KEV 漏收程度；本次未读一手原文，不确定细节）
- **CVSS v4.0**（severity，含 Threat/Environmental 分组）：https://www.first.org/cvss/

---

## 三、Remediation 自动化与 Agent

### 3.1 能力阶梯（从"告诉用户怎么修"到"自动修"）

| 阶梯 | 能力 | 代表实现（已核实） | 确定性? |
|---|---|---|---|
| L0 | Fix version 推荐 | 所有 SCA（OSV 数据自带 fixed version） | 确定性 |
| L1 | 自动 dependency upgrade PR | Dependabot / Renovate（Renovate **Merge Confidence** 用群体采纳数据标记 undeclared breaking release [Fact](https://docs.renovatebot.com/merge-confidence/)） | 确定性 + 数据启发式 |
| L2 | 升级风险评估（breaking change / API compatibility） | cargo-semver-checks（Rust）、japicmp/revapi（Java）、gorelease（Go）、griffe（Python）；局限：只查 API 签名，行为级 breaking 基本无工具覆盖 [Fact/Interpretation](https://github.com/obi1kenobi/cargo-semver-checks) | 确定性（覆盖有限） |
| L3 | Patch backport（不升级版本直接打补丁） | Endor Patches：定位 fix commit → backport 到当前版本 → 兼容性/安全测试 [Fact](https://github.com/endorlabs/endor-patches)；Seal Security、Chainguard 同类（技术细节未核实） | 半确定性：cherry-pick 确定性，冲突解决与验证需工程 |
| L4 | AI coding agent 生成补丁（无上游修复时改代码） | GitHub Copilot Autofix（CodeQL 检测 + LLM 修复 + coding agent 落地 stacked PR [Fact](https://github.blog/changelog/2025-10-28-new-public-preview-features-in-copilot-code-review-ai-reviews-that-see-the-full-picture/)）；Snyk Agent Fix agentic 架构 [Fact](https://snyk.io/blog/snyk-agent-fix-agentic-architecture/) | LLM 生成 + 确定性校验 |
| L5 | 修复验证（证明漏洞真的修掉） | PoV/回归测试驱动：AIxCC 冠军系统 ATLANTIS 用 fuzzer/程序分析产出可执行证据闭环 [Fact](https://arxiv.org/html/2602.07666v1)；Snyk 对生成的 fix 先跑 Snyk Code re-scan（pre-screening）[Fact](https://snyk.io/de/blog/building-ai-trust-with-snyk-code-and-snyk-agent-fix/) | 确定性验证是底线 |

### 3.2 确定性工具 vs LLM/Agent 的分工依据 [Interpretation]

- **确定性工具**：版本解析与升级图计算、API diff、补丁 cherry-pick、构建与测试、修复后 re-scan、PoC/PoV 执行。依据：这些步骤的输出**必须是可复现、可审计的事实**，LLM 的 61–67% 裸 triage 准确率说明其不满足。
- **LLM/Agent**：修复冲突消解（backport 冲突）、无上游修复时的补丁起草、变更影响的自然语言解释、跨步骤编排（"这个 CVE → 哪个 repo → 哪个版本线 → 开几个 PR"）、breaking change 的语义级判读（changelog/迁移指南理解）。依据：这些是**高上下文、低可形式化**任务，且其产出都经过确定性闸门（编译、测试、re-scan）后才落地。
- 业界一线实践已收敛到同一模式 [Fact]：GitHub 官方称 CCR = "LLM intelligence + deterministic precision"（CodeQL/ESLint）；Snyk = 前沿模型 + 专家修复样本 few-shot + SAST pre-screening；AIxCC 冠军 = LLM 编排 + fuzzer/程序分析出证据。**没有任何严肃厂商让 LLM 结论未经确定性校验直接落地。**

### 3.3 Agentic Vulnerability Management 架构可行性

- **可行性已被验证 [Fact]**：DARPA AIxCC（2025 决赛）是最大规模实证——7 支队伍的 CRS 全自动发现+修复真实开源项目（>5400 万行）漏洞，冠军 ATLANTIS 的架构正是"**Code Retriever 等确定性工具层产出精确代码事实 → LLM agent 层做推理与编排**"；第四名队伍自主发现 28 个漏洞含 6 个 0day。([SoK](https://arxiv.org/html/2602.07666v1)、[ATLANTIS 开源](https://github.com/Team-Atlanta/aixcc-afc-atlantis))
- **Agent 负责 reasoning 还是 execution？[Interpretation]** Agent 负责 **orchestration + reasoning + 解释**；execution 中的"事实产出"（扫描、call graph、测试执行）必须委托给 deterministic 工具。即 Agent = 调度员与分析师，不是测量仪器。
- **必须 deterministic 出证据的结论**：reachability 路径、version range 匹配、补丁是否编译通过/测试通过/漏洞不再触发、SBOM diff。LLM 可对这些证据做**解读**，不可**替代**。
- **幻觉防护的三层机制 [Interpretation，有先例支撑]**：
  1. Evidence-based agent：agent 的每个结论必须携带 tool call 产物引用（AIxCC 的 PoV、Snyk 的 pre-screening、GitHub 的 CodeQL 联动）；
  2. Machine-verifiable evidence：结论以结构化证据对象（调用栈、测试日志、扫描 SARIF）而非自然语言陈述存储；
  3. Human-in-the-loop 位置：`not_affected` 断言、豁免、对外发布的 VEX/CSAF 必须人工签核（与 CISA VEX justification 的"可辩护性"要求对齐）。
- **MCP/Tool/Skill 组织 [Fact/Interpretation]**：MCP 已成 2025-2026 事实标准接口；学术侧已有把 Joern CPG 封装为 MCP server 供 LLM 做程序分析的开源先例（codebadger, [arXiv 2603.24837](https://arxiv.org/html/2603.24837v1)）。合理组织方式：SCA/reachability/SAST/CI 各封装为 MCP tool；领域知识（SSVC 决策树、CRA 条款映射、修复 playbook）编码为 Skill/prompt 资产；agent trace（tool call 序列 + 输入输出 hash）落 Evidence Store 供审计。
- **审计可追踪的 agent execution trace [Hypothesis]**：把每次 agent 运行记录为 in-toto 风格的 attestation（步骤、工具版本、输入输出摘要、时间戳、模型版本），可使 AI 参与的安全决策具备 CRA 审计所需的可辩护性——目前未见厂商公开实现（不确定）。

---

## 四、Knowledge Graph vs Evidence Graph 数据底座

### 4.1 节点/关系模型的可行性

任务书给出的节点（Product/Version/Repo/Artifact/Component/Package/File/Symbol/Function/CVE/CWE/Exploit/Patch/Commit/PR/SBOM/VEX/Advisory/CRA Obligation）与关系（contains/depends_on/affected_by/reachable_from/exploitable_via/fixed_by/verified_by/reported_by/satisfies）与 GUAC 的本体高度同构——GUAC 已证明该模型能统一 SPDX/CycloneDX/SLSA/in-toto/CSAF VEX/OpenVEX/OSV/deps.dev [Fact](https://github.com/guacsec/guac/blob/main/README.md)。**但 GUAC 的诚实声明同样重要：实体标识符不总是可得，必须靠启发式链接，存在未处理的边界情况**——即图的最大工程难点不是存储而是**实体解析（identity resolution）**。

### 4.2 业界谁在用图 [Fact]

- **OpenSSF GUAC**：供应链元数据聚合图的事实标准开源项目（OpenSSF incubating）。注意：其"graph database"是数据模型与 GraphQL 语义层面的概念——**官方维护的生产后端是 keyvalue/ent+PostgreSQL，Neo4j 后端反而是 unsupported/incomplete**（README 明示）。佐证：PuppyGraph 演示在关系库上复刻 Wiz Security Graph。
- **Wiz Security Graph**：code-to-cloud 资产/发现/身份关联图，attack path analysis 的核心；Google 以约 320 亿美元收购 Wiz（2025-03 宣布）[Fact](https://www.wiz.io/lp/wiz-security-graph)——安全关联图的商业价值获最高级别验证。但 Wiz 图粒度是云资产级，不到 function/CVE/commit。
- **Endor Labs**：依赖+调用图是其产品底座；Snyk 侧对应物是 AppRisk application context（2024 起，含 Orca runtime context 集成 [Fact](https://snyk.io/blog/announcing-new-snyk-apprisk-integration-orca/)）；任务书中 "Snyk AppContext" 一名未核到独立产品（不确定，可能指 AppRisk 的 context 能力）。Aptori 有 "Application Context Graph"（厂商宣称）。
- [Interpretation] 图作为 SCA+SAST+Reachability+Exploitability+Remediation+合规的共同底座是成立的——但**壁垒在数据（实体解析质量 + vulnerability→function 标注 + 客户环境上下文），不在图技术**。

### 4.3 Evidence Graph：为什么比纯 Knowledge Graph 更适合审计/合规 [Interpretation]

- Knowledge Graph 回答"什么与什么相关"；Evidence Graph 回答"**这个结论凭什么成立**"——每个 Conclusion 挂 Evidence→Tool（含版本）→Artifact（hash）→Timestamp→Analyst/Agent→Decision 的链。CRA 场景下买方（制造商）需要的是面对监管与客户的**可辩护性（defensibility）**，纯关联图不携带证明力。
- 先例充分 [Fact]：
  - **in-toto**（CNCF graduated）："make it transparent what steps were performed, by whom and in what order"——供应链每步的签名 attestation + 验证（[in-toto.io](https://in-toto.io)）；
  - **SLSA provenance**：以 in-toto attestation 为载体记录构建出处；
  - **GUAC**：直接消费 in-toto ITE6/CSAF VEX/OpenVEX，证明"证据文档→图"的管线可行。
- [Hypothesis] 差异化机会：现有先例的证据链覆盖**构建过程**，没有人把同样的 attestation 范式系统性地应用到**安全结论**（reachability 判定、VEX status、修复验证）。Evidence Graph = in-toto 思想 × 漏洞生命周期，这在 CRA 强制审计留痕的背景下是真实的空白点。

---

## 五、反面证据汇总（哪些叙事可能被高估）

1. **"Reachability 降噪 90%+" 的厂商数字不可直接采信 [Fact/Interpretation]**：Endor "up to 92%"、示例 124→11→2 的分母是"全部 findings"；且 unreachable 判定官方承认 unsound（Snyk：NO PATH FOUND ≠ 不可达）。真正的对照基线是：Datadog 用**廉价得多的 runtime context** 就把 82% 的 critical 降级——reachability 的增量价值需要与 context 过滤对比衡量，而不是与"什么都不做"对比。
2. **"图数据库"是叙事，图数据模型才是实质 [Fact]**：GUAC（供应链图旗舰项目）生产后端推荐 PostgreSQL/内存 KV，Neo4j 后端 unsupported/incomplete；Wiz 式图可在关系库上复刻。押注"图数据库技术"没有壁垒，押注"安全本体 + 实体解析 + 证据链数据"才有。
3. **"Agentic 全自动修复"叙事超出实测水位 [Fact]**：公开 benchmark 显示裸 LLM triage 准确率 61–67%；所有严肃实现（GitHub/Snyk/AIxCC）都靠 deterministic 校验兜底。全自动（无人签核）修复在合规场景（CRA 下制造商担责）短期内不成立——卖点应是"agent 产出带证据的修复建议 + 确定性验证 + 人工一键签核"，而非"AI 自动修"。
4. **VEX 自动化已解决的叙事为时过早 [Fact]**：arXiv 2503.14388 实证工具间判定不一致；CISA justification 枚举虽机器可读，但 `not_in_execute_path` 依赖的静态不可达证据本身是弱证据。

---

## 六、结论：三个方向的壁垒判断

### 6.1 Reachability —— 工程壁垒 [Interpretation]

- 方法（call graph/CFG/taint/binary）全部公开，不同语言有可复用工具（govulncheck/Joern/Soot；CodeQL CLI 须另核授权），Endor/Snyk/GitHub/Semgrep 已产品化 → **不构成技术（算法）壁垒**。
- 真正的护城河成分是：(a) 多语言引擎的持续工程投入（每语言 2–3 人年量级，估计）；(b) **vulnerability→function/symbol 的标注数据集**（Snyk/Endor/Go 团队都在策展，这是数据资产）；(c) 不可构建项目的 fallback 工程。
- 对一家已有 SCA/SAST 的厂商：自建 Java/Go/Python 的 function-level reachability 是 1–2 年可追平的工程；**差异化机会在 C/C++/嵌入式（CRA 主战场、产品化最薄弱）与二进制 reachability**——那里竞争最少、客户最痛。[Hypothesis：值得做 PoC 验证 C/C++ 可达性精度上限]
- 风险：Go 官方免费工具的存在说明单语言 reachability 可被生态"国有化"，长期商品化压力大。

### 6.2 Exploitability —— 仅产品功能（框架层）；证据化 VEX 含工程壁垒成分 [Interpretation]

- SSVC/EPSS/KEV/CVSS 全公开、数据全开放，决策树实现成本以周计 → 决策模型本身零壁垒。
- 有价值的成分：(a) **组织侧 context 数据的采集与治理**（部署拓扑、暴露面、feature flag 状态）——这是集成工程；(b) `not_affected` justification 的机器证据链（见 2.3 映射表）——deterministic 部分可自动化，execute_path 类必须保守处理；(c) 把决策过程固化为**可审计的决策记录**（SSVC 决策点取值 + 证据引用 + 签核人）——这与 Evidence Graph 合流。
- 判断：Exploitability 单独做不成壁垒，但它是 Evidence Graph 上最有价值的"结论类型"，应作为图的杀手级应用而非独立技术方向。

### 6.3 Evidence Graph + Agentic Remediation —— 分两半看 [Interpretation]

- **Agentic Remediation（编排层）= 工程壁垒，且窗口期短**：模式已被 GitHub/Snyk/AIxCC 公开验证，追赶者众。壁垒成分 = 修复验证闭环（PoV/回归/SAST re-scan 的工程化）+ 失败率数据积累。纯"套 MCP 编排 LLM"无任何壁垒。
- **Evidence Graph = 三方向中最接近"真壁垒"的候选**：
  - 它有先例验证可行性（in-toto/SLSA/GUAC），但没有人在"安全结论级证据链"上建立标准或数据网络效应；
  - 它把 SCA/SAST/Reachability/Exploitability/Remediation/CRA 合规全部统一为"结论+证据"的存储与查询问题，是天然的共同底座；
  - CRA 的审计/报告义务（24h/72h 报告、技术文档留存）使"可辩护证据"成为买方刚需，而非锦上添花；
  - 壁垒来源是**数据模型标准卡位 + 证据数据积累 + 信任位（客户敢把合规证据托管给你）**，而非任何单点技术——这恰恰是"真壁垒"的构造方式。
- 风险提示 [Hypothesis]：Evidence Graph 的壁垒依赖 CRA 执法强度与客户审计需求的实际兑现；若 CRA 合规市场不及预期，它退化为"不错的平台架构"而非商业壁垒。

---

## 七、来源索引

所有来源 note 位于 [docs/research/04-technology-deep-dive/sources/](04-technology-deep-dive/sources/)：

| Note | 来源 | 层级 |
|---|---|---|
| [endor-labs-reachability-docs.md](04-technology-deep-dive/sources/endor-labs-reachability-docs.md) | docs.endorlabs.com | 厂商官方文档 |
| [snyk-reachability-docs.md](04-technology-deep-dive/sources/snyk-reachability-docs.md) | docs.snyk.io | 厂商官方文档 |
| [endor-js-reachability-blog.md](04-technology-deep-dive/sources/endor-js-reachability-blog.md) | endorlabs.com/learn | 厂商工程博客 |
| [govulncheck-docs.md](04-technology-deep-dive/sources/govulncheck-docs.md) | pkg.go.dev | 官方文档 |
| [github-dependabot-vulnerable-function-calls.md](04-technology-deep-dive/sources/github-dependabot-vulnerable-function-calls.md) | github.blog | 官方 changelog |
| [joern-cpg.md](04-technology-deep-dive/sources/joern-cpg.md) | github.com/joernio | 开源项目 |
| [semgrep-reachability-whitepaper.md](04-technology-deep-dive/sources/semgrep-reachability-whitepaper.md) | semgrep.dev | 厂商白皮书（立场性） |
| [cognixshield-savant-arxiv.md](04-technology-deep-dive/sources/cognixshield-savant-arxiv.md) | arXiv 2506.17798 | 学术论文（预印本） |
| [cisa-ssvc.md](04-technology-deep-dive/sources/cisa-ssvc.md) | cisa.gov | 政府/标准 |
| [first-epss.md](04-technology-deep-dive/sources/first-epss.md) | first.org | 标准组织 |
| [cisa-vex-minimum-requirements.md](04-technology-deep-dive/sources/cisa-vex-minimum-requirements.md) | cisa.gov PDF + Anchore/SPDX 印证 | 政府/标准 |
| [datadog-state-of-devsecops-2025.md](04-technology-deep-dive/sources/datadog-state-of-devsecops-2025.md) | datadoghq.com | 厂商研究（一手数据） |
| [oligo-runtime-reachability.md](04-technology-deep-dive/sources/oligo-runtime-reachability.md) | oligo.security | 厂商工程博客 |
| [breaking-change-tools.md](04-technology-deep-dive/sources/breaking-change-tools.md) | docs.renovatebot.com + GitHub | 官方文档/开源 |
| [endor-patches.md](04-technology-deep-dive/sources/endor-patches.md) | github.com/endorlabs | 开源 + 厂商博客 |
| [snyk-agent-fix.md](04-technology-deep-dive/sources/snyk-agent-fix.md) | snyk.io | 厂商官方（数据自述） |
| [github-copilot-code-review-agentic.md](04-technology-deep-dive/sources/github-copilot-code-review-agentic.md) | github.blog | 官方 changelog |
| [darpa-aixcc.md](04-technology-deep-dive/sources/darpa-aixcc.md) | arXiv 2602.07666 + GitHub | 学术/政府 |
| [simbian-ai-soc-benchmark.md](04-technology-deep-dive/sources/simbian-ai-soc-benchmark.md) | simbian.ai | 厂商（立场性） |
| [openssf-guac-readme.md](04-technology-deep-dive/sources/openssf-guac-readme.md) | github.com/guacsec | 开源项目 |
| [in-toto-framework.md](04-technology-deep-dive/sources/in-toto-framework.md) | in-toto.io | 标准/开源 |
| [wiz-security-graph.md](04-technology-deep-dive/sources/wiz-security-graph.md) | wiz.io + 第三方佐证 | 厂商官方 + 新闻 |

调研过程与来源冲突记录见 [docs/research/04-technology-deep-dive/research-log.md](04-technology-deep-dive/research-log.md)。
