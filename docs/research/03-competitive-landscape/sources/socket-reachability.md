# Source Note: Socket 收购 Coana 与 Reachability（官方文档+博客）

- URL:
  - https://socket.dev/blog/socket-acquires-coana-reachability-analysis（2025-04-23）
  - https://socket.dev/blog/announcing-precomputed-reachability-analysis-in-socket（2025-07-30）
  - https://docs.socket.dev/docs/reachability-analysis（2026-08-17 更新）
  - https://docs.socket.dev/docs/precomputed-reachability（2026-06-29 更新）
  - https://docs.socket.dev/docs/static-reachability-analysis（2026-07-01 更新）
- 发布方: Socket 官方
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方文档 + 官方博客

## 关键事实点

- 2025-04 收购 Coana（丹麦 reachability 分析初创），将 reachability 引入 Socket SCA。
- "Precomputed reachability"：预计算 CVE 影响函数 vs 传递依赖中从未被调用的函数，过滤不可达 CVE；可安全忽略不可达漏洞（厂商声称）。
- Static reachability 可识别直接依赖与传递依赖（含依赖的依赖）中的漏洞可达性。
- Socket 核心差异化仍是包行为分析（恶意包、typosquatting、供应链攻击，在 CVE 出现前检测）——第三方评测（AppSec Santa 2026-05）交叉确认。
- 竞品批评（Aikido 博客，竞品视角，需谨慎）：Socket precomputed reachability"止步于依赖内部函数级过滤，不判断你自己的代码是否真正调用该依赖"——即应用侧 call path 可能不完整。

## 支撑报告结论

- Reachability 能力在 2025-2026 快速扩散（连 Socket 这类恶意包检测厂商都通过收购补齐）→ 支撑"package/dependency 级 reachability 正在商品化"。
- "precomputed reachability"是成本优化的工程创新点，但应用侧 call path 完整度存疑 → 支撑"跨语言 function-level + 应用侧全链路 reachability 仍有创新空间"。
