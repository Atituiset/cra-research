# 产品形态与技术栈调研日志（06-product-forms-and-tech-stacks）

抓取基准日：2026-09-20

## 检索记录

1. `Dependency-Track architecture storage Alpine ORM PostgreSQL database backend`
   - 采纳：Backbase 工程博客（2026-04-14，Aurora PostgreSQL 生产部署）、官方 configuration 文档。
   - 弃用：GitHub discussion #3955（安装问答，信息密度低）、wisesec.nl（2022 教程）。

2. `Black Duck snippet matching fingerprint code identification how it works`
   - 采纳：Synopsys Detect 9.6.0 官方手册 PDF（四种 snippet 模式）、SecureSECO 学术分析（2MB/5–7 行细节）。
   - 弃用：skilljar 课程页（营销）、securityboulevard 软文。

3. `Anchore grype vulnerability matching distro backport RHEL Debian NVD version fix data`
   - 采纳：docs.anchore.com《How It Works》（2026-06-16，GrypeDB 共用匹配）、Discourse 维护者回复（distro feed 清单）、GitHub issue #1541（backport 误报一手反证）。
   - 冲突注意：issue #1541 是 2023 年 SUSE 场景，现 Grype 对主流发行版 feed 已覆盖，但"NVD CPE 版本比较路径上 backport 失效"的机制判断仍成立。

4. `Oligo Security eBPF runtime reachability how it works library profiling`
   - 采纳：Oligo 官方工程博客（2025-06-10，eBPF 信号回溯到函数/库粒度）、VentureBeat（2023-02，$28M 融资背景）。
   - 弃用：appsecsanta 评测（二手转述，仅交叉验证）、Coana 白皮书 PDF（竞品）。

5. `Aqua Security tracee eBPF runtime detection open source`
   - 采纳：Tracee 官方文档与仓库；arXiv 2026-09 文献（Tracee/Falco 并列为 eBPF 运行时事实标准）。
   - 弃用：Gitee 镜像、YouTube 视频、第三方教程。

6. `Wiz runtime sensor eBPF agentless workload scanning architecture`
   - 采纳：Wiz 官方博客 FAQ（2026-07-06）+ runtime sensor 产品页；ARMO 竞品文（交叉验证"agentless 打底 + sensor 加深"架构）。
   - 弃用：Techclick/TechBag 聚合站（AI 生成痕迹重）。

7. `Snyk vulnerability database Snyk Intel security research team curation hand triage`
   - 采纳：Snyk 官方《Human + AI》策展博客（2025-07-14）、security-intelligence 平台页、NVD delays 博客。
   - 弃用：businessmodelcanvastemplate（推测性财务数据）、Safeguard 二手拆解。

8. `Sonatype vulnerability data curation research team automated vs NVD`
   - 采纳：help.sonatype.com《Sonatype Vulnerability Data》（"we create the precise data"原文）。
   - 弃用：各中文博客转述、学位论文（内容对但层级低）。

9. `Mend vulnerability database research team WhiteSource`
   - 采纳：Mend 官方博客（2026-07-09）+ WhiteSource Vulnerability Database 白皮书 PDF；顺带获得 Checkmarx Zero 团队证据（Checkmarx SCA FAQ 官方文档，合入 Mend note）。
   - 注意：白皮书中"消除 70–85% 告警"为厂商声称，报告已标注。

10. `CRACI startup CRA compliance`
    - 采纳：ArcticStartup、Tech Funding News、CRACI 官网（2026-05-19，€1.4M pre-seed、CI/CD 嵌入形态）。
    - 弃用：TAMradar/Due Diligence Hub（纯转载）。

11. `ArmorCode Apiiro ASPM aggregation platform`
    - 采纳：ArmorCode 官方 ASPM 页（"doesn't run its own scanner"原文）+ appsecsanta 双评测；guptadeepak 对比表（Apiiro/ArmorCode/Cycode 内部分化）。
    - 弃用：Heeler/Aikido 竞品对比页（立场鲜明，仅作存在性参考）。

12. `Snyk MCP server Endor Socket MCP AI agent integration`
    - 采纳：Snyk 官方 MCP 两篇（2025-05/2025-12）+ oodle.ai 对 Snyk MCP server 的第三方核验（13 tools、本地扫描）。
    - 弃用：各类"MCP 服务器清单"软文。
    - 说明：Endor/Socket 的 MCP 也有公开信号但本次未取到足够一手材料，报告正文只做定性表述，未单独成 note。

13. `NetRise binary analysis CPE generation firmware SBOM`
    - 采纳：NetRise 官方 BCA glossary + Turbine 产品页、Manifest-NetRise 合作新闻稿（能力组件化信号）。
    - 弃用：RunSafe 博客（竞品视角）。

14. `VulnDB Flashpoint independently researched`
    - 采纳：Flashpoint 官方两篇（400k 里程碑 2025-04、NVD slowdown 2026-04）。
    - 注意：所有覆盖数字均为厂商声称，报告已标注；Cybersecurity Dive 2024-04 佐证 NVD 积压行业背景。

15. `Finite State binary analysis reverse engineering firmware how it works`
    - 采纳：Finite State 官方博客（2026-03-15）+ mdu.se 论文（同方法学术描述）+ MDPI 2026-08 固件逆向综述（二进制相似性检测方法族）。
    - 弃用：coddykit 教程、grammatech（另一家，仅方法参照）。

16. `Semgrep engine architecture tree-sitter OCaml`
    - 采纳：Semgrep 官方 grammar 升级文档（tree-sitter→ocaml-tree-sitter→generic AST）、官方 OpenGrep 对比页（LGPL-2.1 确认）、appsecsanta（分叉时间线）。
    - 冲突注意：pixee.ai 称"Semgrep 把核心引擎从宽松许可改为 LGPL"——表述不准（引擎自始 LGPL-2.1，变的是规则仓库许可），以 Semgrep 官方为准。

17. 定价/交付类检索（Snyk/Wiz/Endor/Chainguard/Mend/Veracode/Black Duck/JFrog/ONEKEY）
    - 采纳：AWS Marketplace Wiz 上架页（官方渠道公开价）、Endor 官方 docs licenses、Chainguard 官方 edu 定价页 + RFP.wiki/Sacra 交叉、TrustRadius Mend 交付字段、Black Duck 官方 air-gapped KB 文档、ToolsInfo ONEKEY 条目 + 官方 Swisscom 案例、appsecsanta JFrog Xray 评测 + ALMtoolbox 自管环境 Curation 博客。
    - 通用注意：企业档真实合同价均不公开，报告一律标注"公开标价/第三方汇编"层级，询价制厂商不做数字断言。

18. `Socket behavioral analysis package`
    - 采纳：Socket 官方 FAQ + 创始人 HN 首发帖。
    - 弃用：xygeni/systemsarchitect 清单文。

## 总体弃用原则

- 营销落地页仅在涉及"厂商自身交付/定价/架构陈述"时采纳并标注厂商声称；
- AI 生成聚合站（TechBag、Techclick 等）一律弃用；
- 竞品互评文仅在双方对"架构事实"无分歧时作交叉验证用。

## 与既有报告的边界执行

- 04 已覆盖的理论方法（govulncheck/Joern/CPG/GUAC Postgres/Wiz graph/AIxCC/Agent Fix/CCR 架构）一律引用，未重新取证（见 sources/internal-cross-references.md）；
- 03 的厂商×能力明细未重抄，06 只取"形态/交付/定价/栈"四维度。
