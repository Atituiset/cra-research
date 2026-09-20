# Source Note: Joern — Code Property Graph 开源平台

- URL: https://github.com/joernio/joern ；https://docs.joern.io/ ；https://joern.io/impact/
- 标题: Joern — The Bug Hunter's Workbench
- 发布方: Joern.io / Qwiet AI（开源，Apache 2.0）
- 抓取日期: 2026-09-18
- 来源层级: 开源项目（一手）

## 关键摘录 / 技术要点

- Joern 是 Code Property Graph（CPG）的原始实现（Yamaguchi et al. 2014 学术概念），把 AST + CFG + PDG 融合成单一图表示，支持源码、字节码与二进制可执行文件的跨语言分析（C/C++、Java/JVM 字节码、JS、Python、Go、Kotlin 等前端），CPG 存储于自定义图数据库，用 Scala-based 查询语言做跨过程数据流/调用图查询。
- 相关：arXiv 2603.24837 "codebadger"（2026-03）把 Joern CPG 封装为 **MCP server** 供 LLM 做程序分析——"deterministic engine 出图，LLM 负责查询与推理"的开源先例。

## 支撑报告结论

- 第一部分：C/C++ 侧 reachability 的可用开源底座（CPG/call graph/data flow）；同时说明 C/C++ 没有像 govulncheck 那样的官方免费 function-level 工具。
- 第三部分：Joern+MCP 是"Agent 调确定性分析引擎"架构的现实参照。
