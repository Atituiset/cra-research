# Research Log: Snyk 厂商深挖（第二轮）

- 日期: 2026-09-21
- 产出: [snyk.md](snyk.md) + sources/ 下 12 个 snyk- 前缀 source notes
- 方法: 全部一手来源优先（docs.snyk.io / snyk.io 官方博客·新闻稿 / arXiv / github.com/Snyk）；营销页与新闻稿商业数据标"厂商声称"；第三方来源仅用于线索发现，不进正文证据链。

## 过程记录（按序）

1. **基线重读**：03 §1.1/§6（call path/Risk Score/monitor 三点已核实）、04（Agent Fix GA、Evo 四环、pre-screening）、06（MCP 13 tool 第三方核验、策展博客）。确定本轮只做增量深挖。
2. **reachability 新路径文档**（docs.snyk.io/scan-fix-and-prevent/...，2026-09-18 更新）拿到比 03 轮更深的表述：五步管线原文、"agentic capability / real-time decision-making / under-approximate"新增措辞、CLI `--reachability` EA 与新 findings schema、300k 文件/3GB 上限、"NO PATH FOUND can change to Reachable" 自认。
3. **Risk Score 文档**（2026-09-15 更新）拿到因子全清单与逐因子分数影响表；发现三个口径点：仍 EA（2023-08 至今）、CLI 不可用、该页 reachability 语言覆盖滞后于专页（文档内部不同步）。
4. **策展博客**（2025-07-14）全文：AI 五角色、RLHF、eval-driven + LLM-as-judge、内部 MCP server（策展团队先用）。人工/AI 定量比例未披露 → 列入无法核实。
5. **NVD delays 博客**（2024-03-13）：500+ CVE 未分析、两个 CVE 3 周时差、无 CVE 也收录、容器 advisory 透传延迟自认。营销页 3x/92%/47 天为厂商声称。
6. **Snyk Studio 文档**（2026-09-10）：MCP = CLI 子命令 `snyk mcp -t stdio`、local-only（无 hosted server）、12 tool 清单、lite/full/experimental profile、hooks vs rules 双路径、installer 开源可自托管。
7. **Evo 2026-09-17 新闻稿**（抓取前 4 天发布）：94% 合并率相对提升（本轮最重要新数据点）、VulnBench 引用、运行规模遥测、三环产品+四环叙事最新口径、AI-SPM 2026-03 GA / ADS 2026-06 GA / COS 2026-08 GA / Remediation Agent open preview。
8. **VulnBench arXiv:2606.15762**（2026-06-14）：300 次重复扫描、80/161 一次性 findings、134/158 匹配项稳定、作者自注 Snyk Code 参考集循环性。
9. **Golden Test 基准博客英文版**（2026-08-18）：数值表、35k 修复库、"model is a component we can swap"、四条 Limitations（含 StarCoder 全规则 54.9% 自曝）。
10. **数据治理 + Broker 文档**：三档部署（无 on-prem 平台）、Broker 出向 WebSocket + approved data list + Enterprise-only + Universal 取代 Classic、reachability/SAST 源码"分析完即删只留 call graph+函数名"、AWS 缓存 24–48h、不用客户代码训练。
11. **定价**：plans 页四档（含新 Ignite $1,260/年档）+ Usage 文档的 contributing developer 官方定义（90 天 commit、git email 去重、公开仓库不计）+ Snyk Credits/Platform Access 新计费体系出现（换算率未展开 → 待补）。
12. **对象模型**：Snyk Projects 文档（Target=外部可扫描资源、Project=Targetfile×Type、30+ Origin 枚举）；monorepo 多 Project 由第三方实测佐证；product/version 语义缺席获官方文档级确认。
13. **演进时间线**：2020-08 Reachable Vulnerabilities 首发博客（Java）早于 DeepCode 收购官宣（2020-09-23）一个月 → reachability 起源自研、后并入 DeepCode 引擎；updates.snyk.io 的 Python >99% 覆盖、Java 引擎升级改判公告。

## 放弃/未采信的来源

- 大量第三方对比站（AppSec Santa、Safeguard、cipherssecurity 等）：仅用于线索（如 "47 天" 的流传、"24,000+ 新增/年" 转述 Snyk 年报），不作为事实来源；其中 "24,000+" 未找到 Snyk 年报原文 → 正文标（厂商声称经转述，不确定）。
- aitoolsdevpro.com 等疑似 AI 生成内容站：弃用。
- Headway 聚合的 updates.snyk.io 条目：用于发现线索，关键条目回溯 updates.snyk.io 原页。

## 遗留问题（供下一轮）

- Snyk Credits 计费细节（Policies 页）。
- Snyk 内部数据基础设施栈（无公开披露，或需会议演讲/招聘 JD 侧写）。
- Evo COS 的独立第三方评测（目前只有厂商叙事）。
- Agent Fix 在 PR 工作流 GA（2026-09）的官方文档页本轮未单独抓取（04 报告已由第三方报道记录）；如需要可补 docs.snyk.io 对应页。
