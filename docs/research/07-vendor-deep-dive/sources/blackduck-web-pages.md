# Source Note: Black Duck 官方网页（营销/博客/PR）抓取记录

- 抓取日期: 2026-09-21
- 来源层级: 厂商官方营销页/博客/新闻稿（厂商声称）、客户社区贴（STMicro 官方社区）
- 用途: 07-vendor-deep-dive/black-duck.md 的营销口径与 CRA 叙事部分

## 抓取清单

1. **Signal 发布 PR（2025-12-10）** — https://news.blackduck.com/2025-12-10-Introducing-Black-Duck-Signal-TM-Agentic-AI-Application-Security-for-Modern-Development
   - "agentic AI solution engineered to secure software at the speed of AI-powered development"；CEO Jason Schmitt 引语："the first programming language-agnostic security analysis product to combine the power of LLM-based code analysis with petabytes of human-labeled security data"（厂商声称）。
   - Key features：real-time incremental analysis、MCP 集成 AI coding assistants、role/task-based AI agents、universal language support、"Automated remediation with verified code fixes and library patching"、supply chain/license compliance、business logic flaw 检测。
   - 发布时只对既有客户与 design partners 开放，"broader availability in early 2026"。
   - 公司自称 "the leader in applied AI for application security"；品牌主张 "True Scale Application Security"。

2. **Signal GA 博客（2026-03-23）** — https://www.blackduck.com/blog/black-duck-signal-security-that-moves-at-the-speed-of-ai.html
   - "I'm proud to announce the general availability of Black Duck Signal"。
   - ContextAI 定义（厂商声称）："purpose-built application security model containing petabytes of human-vetted security intelligence… 20+ years of security ground truth… coding rule sets exercised over billions of lines of code across 40+ languages… tens of thousands of BSIMM assessments, Black Duck Audits, dynamic scans"。
   - "Signal deploys multiple specialized AI security agents that work together to analyze vulnerabilities, validate exploitability, prioritize risk, and recommend or apply fixes"。

3. **CRA 合规博客（2025-07-17）** — https://www.blackduck.com/blog/eu-cyber-resilience-act-compliance.html
   - 泛 CRA 科普 + Black Duck 能力映射（SBOM 生成 SPDX/CycloneDX、依赖分析、漏洞管理）。把 CRA "no known exploitable vulnerabilities" 作为售前扫描卖点。无专门 CRA 模块。

4. **CRA 分层测试方案页（2026-07-01）** — https://www.blackduck.com/solutions/eu-cyber-resilience-act-compliance/eu-cra-security-testing-sca-sast-dast.html
   - 核心叙事："SCA alone won't get you to CRA compliance" → SCA+SAST+DAST 三层。Tim Mackey（head of software supply chain risk strategy）引语：供应商 SBOM 导入并持续监控；Linux 固件组件级粒度重要性；Docker 镜像"可自动化大部分 CRA 义务"。
   - 声称"2018 年漏洞披露到利用平均 2 年，2026 年 <24 小时，2028 年预测 1 分钟"（厂商引用，未给出处）。
   - 提及 September 2026 为 CRA 漏洞报告义务生效节点。

5. **CyRC 页** — https://www.blackduck.com/resources/cybersecurity-research-center.html
   - CyRC 使命与 CVE/BDSA 披露列表（含 Heartbleed 时代 BDSA-2014-0028；Zephyr、Mediatek/Realtek/Atheros 芯片组、IKEA TRÅDFRI 等嵌入式/IoT CVE，多由 Defensics 团队产出）。
   - "Human-verified intelligence for ContextAI"：CyRC 研究反哺 ContextAI。

6. **Seeker IAST 产品页** — https://www.blackduck.com/interactive-application-security-testing.html
   - 关键句："Seeker integrates Black Duck Binary Analysis, which analyzes target binaries for open source security vulnerabilities… and matches them against the knowledgebase in Black Duck Hub. You get a unified view of all identified vulnerabilities found in custom code and component libraries."
   - "patented active verification technology"（自动重测验证可利用性）；sensitive-data tracking；API 发现（REST/SOAP/GraphQL/gRPC）；"near-zero false positives"（厂商声称）。

7. **KB 营销页（2026-08 快照）** — https://www.blackduck.com/software-composition-analysis-tools/knowledgebase.html
   - "8.7 million open source components from over 57,700 forges and repositories"、"3,000+ unique licenses"，"sourced and curated by the Cybersecurity Research Center (CyRC)"（厂商声称）。

8. **Black Duck SCA 产品页（2026-08-12 快照）** — https://www.blackduck.com/software-composition-analysis-tools/black-duck-sca.html
   - "Combine dependency, binary, and snippet analysis to build an accurate SBOM"；Gartner 2026 MQ for Software Supply Chain Security Leader（厂商引用）。

9. **STMicro 官方社区贴（2025-03-06）** — https://community.st.com/compliance-and-regulations-168/stm32cube-software-is-ready-for-automated-sbom-security-processes-with-black-duck-tools-147708
   - STM32Cube 生态用 Black Duck 工具生成 CycloneDX（ECMA-424）机读 SBOM；首个包 STM32CubeU3，后续 STM32CubeH7RS/N6；动机明确为 CRA（2027-12 生效）+ 航空/医疗/汽车既有监管。
   - 客户原话视角：SBOM 是静态文档、漏洞随产品生命周期出现，需要定期自动化分析。

## 备注

- Synopsys 剥离 Software Integrity Group 给 Clearlake Capital / Francisco Partners：2024-05-05 签协议，2024-09-30 完成交割，对价 $1.65B（Synopsys 10-K, SEC EDGAR: https://companiesmarketcap.com/synopsys/sec-reports/10k/ 引 10-K Note 3 Discontinued Operations；另见 https://www.sec.gov/Archives/edgar/data/883241/000088324124000021/R11.htm）。剥离后品牌为独立公司 "Black Duck Software, Inc."。
- Gartner 报告口径变化：Black Duck 现引用 "2026 Gartner Magic Quadrant for Software Supply Chain Security" Leader（原 Application Security Testing MQ 口径已换）。
