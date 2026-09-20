# Source Note: Simbian — AI SOC LLM Benchmark（LLM 告警 triage 能力边界的证据）

- URL: https://simbian.ai/blog/the-first-ai-soc-llm-benchmark
- 标题: AI SOC LLM Benchmark: Can LLMs Automate Alert Triage?
- 发布方: Simbian（SOC 自动化厂商，立场性来源）
- 日期: 2025-06-12；抓取日期 2026-09-18
- 来源层级: 厂商博客（二手/立场性，但其 benchmark 方法公开）

## 关键摘录 / 技术要点

- 100 个真实网络安全场景的 LLM triage benchmark：**顶级模型准确率 61–67%**。
- 含义：裸 LLM 做安全告警 triage 的准确率远低于可接受阈值；需要工具调用、检索与确定性校验增强。

## 支撑报告结论

- 第三部分：防止 LLM 幻觉污染安全结论的定量依据——裸模型 triage 准确率 ~2/3，安全结论必须由 deterministic engine 出证据，LLM 只做编排与解释。
- 相关旁证（未独立核实，标注不确定）：Ghost Security 2025-04 称 ~3000 个开源 repo 上 91% 的 SAST 标记为误报；arXiv 2407.12241 称 76% 的告警与漏洞代码变更无关。
