# 竞争格局调研日志（03-competitive-landscape）

抓取基准日：2026-09-18

## 2026-09-18

### 检索记录

1. `Snyk Cyber Resilience Act CRA compliance solution 2025`
   - 采纳：Snyk 官方博客两篇（CRA 解读 + CRA compliance 方案）、Snyk LP "What you need to know about CRA"（营销材料）。第三方：AppDevANGLE(YouTube)、Linux Foundation CRA 认知报告 PDF（可引用其行业认知数据）。
   - 弃用：Microchip 硬件厂商 brochure（与本主题相关性低）、Aikido 第三方软文（仅作补充参考）。

2. `Mend CRA SCA reachability 2025`
   - 采纳：Mend.io 官方博客《EU CRA explained: requirements, timeline, and compliance》(2026-07-30 更新）、Mend 合规页（2026-09-04）、Mend docs 的 SCA Reachability 页、Endor Labs "Understanding the CRA"（厂商营销但内容详实）。
   - 弃用：ioimalaysia（无关）、CSL Group IoT 文章（垂直行业）。

3. `Snyk reachability function-level Evo agentic AI 2026 release`
   - 采纳：Snyk 官方新闻稿三篇：Evo 首发（2025-10-22)、Evo Agentic Development Security(2026-06-23)、Evo Continuous Offensive Security(2026-08-04)；Snyk docs《Reachability analysis》（已抓取全文，含支持语言矩阵：Java/JS/Python GA、.NET EA）。
   - 弃用：substack 二手解读（仅背景）、各类对比软文。

4. `Black Duck SCA VEX SBOM CRA 2025 2026`
   - 采纳：Black Duck 社区《Black Duck SCA 2026.7.0 is now available!》——确认 VEX Templates 功能（仿照 SBOM Templates）；herodevs 文章确认 CRA 报告义务 2026-09-11 生效时间点。
   - 弃用：ipros、HuggingFace 数据集。

5. `Sonatype Lifecycle CRA SBOM VEX release notes 2025`
   - 采纳：Sonatype 官方 docs（SBOM 页、IQ Server 2025 release notes、IQ 2024 release notes 中"VEX annotations 可从旧 SBOM 复制到新 SBOM"一条）。
   - 弃用：Safeguard 买家指南（第三方，仅交叉验证）。

6. `JFrog Xray Curation SBOM VEX CRA 2025 2026`
   - 采纳：JFrog 官方 solution sheet《Cyber Resilience Act (CRA) JFrog Platform Compliance Brief》（已抓取全文）；JFrog docs 关于 Xray 部分能力迁移至 Curation 的 deprecation 公告（2026-04-01 起分阶段）。
   - 冲突/注意：JFrog 宣称"the CRA regulates the product you ship: the binary"——营销话术，需标注厂商声称。

7. `GitHub Copilot Autofix Dependabot SBOM export reachability 2025 2026`
   - 采纳：GitHub Docs（SBOM export 页、Autofix for code scanning 页）；druce.ai 汇编指出 2025 年 GHAS 拆分为 Secret Protection + Code Security 两个 SKU（第三方汇编，可信度中等）。
   - 弃用：Heeler 对比软文（竞品视角）。

8. `GitLab Duo vulnerability resolution SBOM dependency scanning reachability 2025 2026`
   - 采纳：GitLab Docs 三篇（Dependency scanning、Static reachability 分析——已抓取全文，含支持语言矩阵 Beta: Python/JS-TS/Java；SBOM-based dependency scanning）。
   - 关键事实：GitLab 的 static reachability 是 package 粒度（import 层面），非 function 粒度；文档明确写了 Java 动态加载/Spring DI 会导致假阴性。

9. `Veracode SCA agentic fix package firewall SBOM 2025 2026`
   - 采纳：BusinessWire/Help Net Security(2026-01-28)Veracode 平台增强新闻；Veracode docs SCA updates 页（2025-06-03 SCA agent 生成 SBOM；2026-07-07 Package Firewall 更新；Fix for SCA Limited Availability）。
   - 注意：Veracode 2025-01 收购 Phylum（恶意包检测）——来自 Aikido 博客转述，需二次核实。

10. `Checkmarx One SCA reachability AI remediation agent 2026`
    - 采纳：Checkmarx 官方 SCA 页（"exploitable path analysis"）、官方 Triage & Remediation Assist 页（2025-04-23）、官方博客《Revolutionizing SCA With Agentic AI》(2025-11-19, Developer Assist)。
    - 采纳（第三方）：pixee.ai 对比文章指出 Checkmarx/Snyk 均未公布 AI 修复合并率（merge rate)——可用于"agentic remediation 可信度"论点。

11. `Endor Labs agentic AI remediation reachability call graph SBOM VEX 2026`
    - 采纳：Endor Labs 官网多篇（reachability、best SCA、FedRAMP use case 页提到 SBOM/VEX）；Microsoft Learn 的 Endor Labs-Defender for Cloud 集成 FAQ（2026-06-16）确认 call graph 能力；F6S 条目确认 Endor Patches、Upgrade Impact Analysis。
    - 弃用：ssojet、appsecsanta 评测（仅交叉验证 97% 降噪等厂商声称数字）。

12. `Semgrep Assistant reachability Supply Chain 2025 2026`
    - 采纳：Semgrep 官方：Spring 2025 release、官方博客（Assistant 承担 60% triage 工作，2025-09-10；zero-false-positive SAST 文章）、Product Updates 页（2025-06-24 PHP reachability 业界首个）。

13. `Chainguard Libraries Containers CVE remediation SBOM CRA 2025 2026`
    - 采纳：Chainguard 官方：Libraries for Java GA(2026-06-23，含 CVE remediation)、Libraries for Python GA(2025-10-22)、CRA 文章(2026-01-14)；The New Stack(2026-06-24)；The Hacker News(2026-01-08，"Critical CVE 平均 20 小时内修复"——厂商声称经媒体转述）。
    - 采纳：Anchore 博客(2025-12-04)Anchore+Chainguard Libraries 集成——交叉验证 CVE 修复库的存在。

14. `Anchore Enterprise VEX SBOM grype syft 2025`
    - 采纳：Safeguard 两篇（Syft v1.20、CycloneDX 1.7/ECMA-424 认证 2025-12，含 Syft 1.18/Trivy 0.59/Grype 支持 1.7 的细节）、Minimus 买家指南（Grype 读 VEX 文档 `--vex-documents`）。
    - 弃用：arXiv 论文（学术，仅背景）。

15. `Aqua Security SCA reachability runtime context Trivy 2025 2026`
    - 采纳：Aqua 官网 container vulnerability scanning 页（runtime context 降噪）；AppSec Santa 评测确认 Trivy 归属 Aqua。
    - 信息缺口：Aqua 的 SCA 细节、CRA 专门材料未找到，待补。

16. `Wiz Code SCA reachability runtime exploitability SBOM 2026`
    - 采纳：Wiz Academy 多篇（SCA、reachability 定义页）；latio.tech(James Berthoty, 2024-10)评测指出 Wiz Code SCA 无静态 reachability、有 SBOM 生成——第三方评测，注意时间较早。
    - 待核实：2025-2026 Wiz Code 是否已加 reachability。

17. `Socket Arnica Oligo Apiiro agentic remediation AI SCA 2026`
    - 采纳：Apiiro 官网与官方博客（AutoFix AI Agent, 2025-10-30）；The Hacker News 奖项页（Apiiro agentic ASPM）；Arnica 官方对比页（pipelineless 架构、Arnie AI）；CM-Alliance 文章。
    - 信息缺口：Socket、Oligo 官方资料待专门检索。

### 待补检索（第二轮执行结果）
- Socket：已补。官方 docs/blog 确认 2025-04 收购 Coana、precomputed/static reachability；竞品指出其应用侧 call path 不完整（已标注竞品立场）。
- Oligo：已补。官方博客《Proving Compliance at Runtime》(2026-05-28) 全文抓取：DAI、runtime SBOM & VEX、FedRAMP SLA 72h→180d 论据；**未见 CRA 专门映射**（聚焦 FedRAMP/PCI/SOC2）。
- Black Duck CRA：未找到独立 CRA 产品页；找到 STMicroelectronics CRA 案例 PR（2025-03）、OSSRA 2026 提及 CRA、Signal（2025-12 发布/2026-03 GA）、2026.7.0 VEX Templates（官方 docs 确认）。Black Duck 社区页 JS 渲染无法抓取，改用 docs.blackduck.com 文档页佐证。
- GitHub CRA：**确认无官方 CRA 页面**（搜索仅命中第三方仓库 zealience 等）——作为"平台内置基线不重视 CRA"的论据。
- GitLab agentic：IR 新闻稿（2026-04-16）Agentic SAST Vulnerability Resolution GA；19.2（2026-07-16）governed agentic automation 修复依赖。
- Mend reachability 语言：官网宣称 200+ 语言检测、reachability 降噪（营销页）；docs 有专门章节但抓取受限，报告中按"厂商声称+文档存在"处理。
- Aqua/Wiz：Aqua SCA 非主战场（第三方一致），无 CRA 材料；Wiz Code 无静态 reachability（2024-10 与 2026-05 两个第三方来源一致）；Google $32B 收购 2026-03-11 交割（Reuters/PitchBook/多源）。
- CRA 时间线：Mend/JFrog/Orbiq/herodevs 四源一致（2026-09-11 Article 14 生效；2027-12-11 全面适用）。
- 新增阵营发现：**Finite State / ONEKEY**（产品安全/PSIRT/嵌入式二进制分析阵营）已占据"Product 对象+CRA 证据"位置，但技术栈是固件/二进制，与现代源码 SCA 阵营存在断层——B 分析关键证据。
- 新增 OSS 基线：Dependency-Track（project/portfolio+VEX）；sbom-sentinel（个人项目拼 CRA 闭环）。
- Checkmarx/Apiiro/Arnica/Semgrep/Veracode/Chainguard 均已补官方或准官方来源。

### 弃用/降权记录
- 所有竞品对比软文（pixee/heeler/aikido/appsecsanta 等）仅用于交叉验证，不单独作为事实来源；厂商自称数字（降噪 %、合并率、修复时长）一律标注"厂商声称"。
- arXiv 论文、韩语/日语聚合博客仅作背景，未采纳为证据。

### 收尾（2026-09-18）
- 全部 22 条 source note 落盘于 [sources/](sources/)；最终报告写入 [docs/research/03-competitive-landscape.md](../03-competitive-landscape.md)（含 15 主厂商 + 6 补充厂商分节、横向对比大表、A/B 分析、来源索引）。
- 已知局限：Mend reachability 语言矩阵、Endor 语言清单、Checkmarx exploitable path 支持语言未能拿到文档级明细（营销页仅有声称），报告中已按"厂商声称"标注；Black Duck 社区页 JS 渲染无法抓取，以 docs.blackduck.com 文档页替代。

## 2026-09-21（闭环视角补充核实，五家逐项）

触发：一份二手分析（来源疑似 AI 生成，链接带 `utm_source=chatgpt.com`）对 Endor Labs/JFrog/Snyk/Sonatype/Black Duck 五家的"漏洞生命周期闭环"能力做出具体声明，逐条一手核实后入库（报告 §6）。

### 检索记录

18. `Endor Labs reachability / upgrade impact / SBOM VEX 官方文档`
    - 采纳：docs.endorlabs.com 五页（reachability-analysis、call-graphs、upgrade-impact-analysis、automated-pull-requests、exporting-sboms）+ 官网 use-case/sca-with-reachability（营销页，排序因子组合标"厂商声称"）。
    - 结论：声明 1 成立。call path 官方语言清单 9 个（Java/Python/Rust/JS/Go/.NET/Kotlin/Scala/Ruby）——修正 03 §1.10 "覆盖广（声称）"口径。
    - 弃用：Safeguard 评测、thectoclub/xygeni 软文（仅交叉验证）；NIST NCCoE 附录中的 Endor 条目（厂商供稿性质）。

19. `JFrog contextual analysis / smart remediation / interpret remediation in scan results`
    - 采纳：docs.jfrog.com 三页（contextual-analysis-of-cves-1、smart-remediation、interpret-remediation-in-scan-results），全部拿到原文。
    - 结论：声明 2 ①②③成立（②"Approximately one-third…deliberately don't rely on reachability"逐字命中）；④部分成立——Patched 状态仅限 Zero-Touch Remediation（Catalog patched rebuild/local patch）场景，非通用修复后重扫标注。
    - 修正：03 §1.5 "非公开 call graph 粒度的 function 级证据"不准确——官方文档显示 Contextual Analysis 有 direct/transitive call chain 展示与证据复制；00 报告 §18.2 的"粒度不可验证"口径随之解决。

20. `Snyk reachability call path Risk Score / snyk monitor`
    - 采纳：docs.snyk.io 两页（reachable-vulnerabilities、monitor-your-projects-at-regular-intervals）。
    - 结论：声明 3 成立。注意 monitor 的"状态变化"语义 = "patch/upgrade path 从无到有"；旧路径页语言矩阵（Java GA + JS/TS EA）落后于新路径页，以 snyk-reachability-docs.md 为准。

21. `Sonatype SBOM VEX workflow`
    - 采纳：help.sonatype.com/en/sbom-vex-workflow.html 全文。
    - 结论：声明 4 部分成立——五步主干（Analyze→Review→Annotate→Share→Audit）属实，但 "Reachability" 不是编号步骤（二手声明把引言描述误植为产品步骤）；justification 为 "should" 建议性非强制；Share 的是 annotated SBOM。VEX 注释跨版本复制获官方文档直接确认（此前仅有 IQ release notes）。

22. `Black Duck 2026.1 VEX 文档`
    - 采纳：docs.blackduck.com 2026.1 两页（VEX、Remediating security vulnerabilities）。docs.blackduck.com 为 Fluid Topics JS 渲染，FetchURL 只拿到 shell；改用其公开 API（`/api/khub/maps`、`/api/khub/maps/{mapId}/topics/{topicId}/content`）抓取 2026.1 英文 map（WIl3UIBXQXtRO_8dfbLjxA = bd-hub-2026.1_en-US）正文。
    - 采纳：abb.app.blackduck.com 2025.1.0 Release Notes（佐证 AFFECTED/NOT_AFFECTED/UNDER_INVESTIGATION 状态体系 2025.1.0 引入）。
    - 结论：声明 5 成立；"SBOM 不变、VEX 按 project version 持续更新"为原文逐字；口径修正：状态体系引入时间是 2025.1.0 而非 2026.1。

### 弃用记录（本轮）

- **触发用的二手分析本身不采信为来源**：其五家声明经一手核实后入库，但该文中无法核实的表述一律弃用——包括各家"内部肯定有 Evidence Graph 类似东西"的推测、对厂商的星级评分、以及任何无官方出处的架构断言。该文仅作为待核实声明清单使用，不进入 sources/。
- pixee/heeler/appsecsanta/dynamicbusiness 等对比软文：仅交叉验证，不作事实来源（沿用既有规则）。

