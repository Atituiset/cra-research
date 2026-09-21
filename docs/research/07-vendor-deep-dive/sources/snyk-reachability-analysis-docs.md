# Source Note: Snyk Reachability analysis 官方文档（2026-09 最新路径，深挖版）

- URL: https://docs.snyk.io/scan-fix-and-prevent/fix/prioritize-issues-for-fixing/reachability-analysis
- 发布方: Snyk（官方用户文档，页面显示 2026-09-18 前后更新）
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方文档（一手）

## 关键事实点（均为原文/近原文）

1. **分析管线五步**（原文标题 "How reachable vulnerability analysis works"）：
   - fix commit 富化：策展流程中引用 maintainer 的 fix commit；
   - Related elements analysis：基于 fix commit，用 **DeepCode AI program analysis** 分析与漏洞相关的 code elements 与参数；
   - Root Cause analysis：DeepCode AI + **NLP** 按"成为漏洞根因的可能性"给相关 code elements 自动排名；
   - Reachability analysis：扫描发现 issue 时，**DeepCode program analysis engine** 分析应用 call graph 与开源依赖间 call graph 的关系，存在到 root-cause code element 的路径即判 "Reachable"；
   - Security experts supervision：安全专家人工校验/标记根因，"make the entire analysis more accurate over time"。
2. **粒度表述升级**：2024 年文档说 "calling a function"；2026-09 版为 "calling a **code element** (for example, functions, classes, modules, and more)"。
3. **语言矩阵**（GA/EA 表）：Maven/Gradle GA；npm/Yarn/pnpm GA；pip/poetry/pipenv GA；**NuGet/paket Early Access**。
4. **CLI 支持（新）**：CLI `1.1301.0+` 支持 `--reachability=true`，返回**新的 findings schema**（legacy 字段可能缺失，官方提示检查自动化兼容性）；`--source-dir` 指定源码目录；`--reachability-filter=reachable` 过滤。**CLI/CI/CD 集成的 reachability 仍是 Early Access**（经 Snyk Preview toggle 开启）。默认上传当前工作目录源码做分析。
5. **Broker 场景**：brokered 连接需配置 Broker 授权访问源码文件。
6. **假阴性自认（原文）**："just because there is no evidence of this does not mean that the element cannot be reached... due to incomplete information, control flow issues, **potential dynamic behaviors**, or overlooked edge cases." 状态三档：`REACHABLE` / `NO PATH FOUND`（明确 ≠ 不可达不可利用）/ `NOT APPLICABLE`。
7. **欠近似与"agentic"权衡（原文，新增表述）**：DeepCode 分析 "applies real-time decision-making to determine whether to **under-approximate** the set of reachable elements"；反射场景无法精确回答；"The **agentic capability** of Snyk analysis optimizes in order to retrieve the most accurate and complete result possible"——即 reachability 引擎已引入 agentic/实时决策成分，不再是纯静态。
8. **结果可变性自认**："vulnerabilities labeled as **Not path found** can change to **Reachable** over time"（first-party 代码变化、漏洞分析变化、SAST 引擎增强都会影响结果）。
9. **技术限制**：文件总数 ≤300,000；总大小 ≤3 GB；文件名 ≤256 字符。
10. **进入 Risk Score**：reachability 是 contextual factor，"will significantly increase the overall score"；经 Projects 页/API（Get issues by Group ID）/Issues Detail report 可得。CLI 端 `--reachability` 输出 JSON 示例含 `reachability: "reachable"` 字段及 EPSS details、exploit maturity、Snyk vs NVD 双 CVSS 来源（Snyk 标 primary、NVD 标 secondary——Snyk 自评分为主）。
11. 无需构建即可分析（"without requiring the application to be built prior to the scan"）。

## 对本轮深挖的支撑

- 维度 2：引擎底座明确为 **DeepCode program analysis engine**（自研/收购血统，非 CodeQL）；2026 年引入 agentic 实时决策。
- 维度 10：假阴性、结果可变性、CLI schema 破坏式变更均为官方自曝。
