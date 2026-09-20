# Source Note: DARPA AIxCC 决赛（2025）— 自动化漏洞发现与修复的最高水位线

- URL: https://arxiv.org/html/2602.07666v1 （SoK: DARPA's AI Cyber Challenge, 2026-02）；决赛系统开源：https://github.com/Team-Atlanta/aixcc-afc-atlantis ；https://huggingface.co/papers（"All You Need Is A Fuzzing Brain"）
- 发布方: DARPA / arXiv / 各参赛队（学术+政府一手）
- 抓取日期: 2026-09-18
- 来源层级: 学术论文 / 开源项目

## 关键摘录 / 技术要点

- AIxCC（2023–2025）是迄今最大规模的全自动 Cyber Reasoning System（CRS）竞赛：对真实开源 C/Java 项目（>5400 万行代码，含从未公开的合成注入漏洞）做自主漏洞发现 + 补丁生成；2025-08 决赛 7 支队伍的 CRS 全部开源。
- 冠军 Team Atlanta 的 ATLANTIS：多 agent 架构 + "Code Retriever" 工具层——**由确定性工具（fuzzer、程序分析）产出精确代码事实，供上层 LLM agent 推理**（技术报告 TR-Team-Atlanta）。
- 第四名 "All You Need Is A Fuzzing Brain"：自主发现 28 个漏洞，含 6 个真实 0day。
- 与 2016 年 CGC 对比：从 binary analysis/符号执行演进为 LLM 编排 + fuzzing + 程序分析 + 补丁证明生成（Jamf 综述）。

## 支撑报告结论

- 第三部分："Agent 做 orchestration/reasoning、确定性引擎做证据产出"不是设想，而是 AIxCC 冠军系统的实际架构——是 Agentic Vulnerability Management 可行性的最强公开证据。
- 同时是边界证据：CRS 的补丁正确性依赖**可执行的 PoV（proof of vulnerability）与功能测试**做闭环验证，没有验证闭环的 LLM 补丁不可信。
