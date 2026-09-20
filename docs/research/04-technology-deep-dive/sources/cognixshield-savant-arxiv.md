# Source Note: CognixShield（原 Savant）— LLM 驱动 vulnerable API 使用检测（arXiv 2506.17798）

- URL: https://arxiv.org/abs/2506.17798
- 标题: CognixShield（v1/v2 标题为 "Savant: Vulnerability Detection in Application Dependencies through Semantic-Guided Reachability Analysis"，v3 2026-08 更名；标题沿革以 arXiv 版本历史为准，改名原因不确定）
- 发布方: 学术论文（arXiv 预印本）
- 日期: v1 2025-06-21，v3 2026-08-09；抓取日期 2026-09-18
- 来源层级: 学术论文（预印本，未经同行评审）

## 关键摘录 / 技术要点

- 问题定义：Java 开源库的 vulnerable API 使用检测；指出纯程序分析与深度学习工具难以在规模上捕获 inter-procedural 漏洞语义；**通用 LLM 因上下文窗口限制与缺乏漏洞专门知识无法直接判定 exploitability**。
- 架构三组件：语义保持的 AST 分片（适配上下文窗口）→ vulnerability-aware 多 agent RAG（跨分片组装安全相关上下文）→ **PoV-guided 语义推理**（用编码了精确触发条件的 Proof-of-Vulnerability 测试来支撑漏洞判定）。
- 结果：57 个真实 Java 应用上 precision 84% / recall 95% / F1 89%（作者自述，预印本未评审）。
- 相关工作确认 VAScanner 等用 call graph 追踪从库到应用的 vulnerable API 调用——说明"call-graph reachability"在学术界已是标准基线而非新壁垒。

## 支撑报告结论

- 第二、三部分：学术前沿同样收敛到"LLM 推理 + 确定性证据（PoV/程序分析）"混合架构；单独 LLM 判定 exploitability 不可行的论断有论文支持。
- 第一部分：学术界 reachability 研究仍在解决 soundness/precision（如 Java 反射、inter-procedural 语义），且开源 Java call graph 工具无法跨依赖累积可达 API（arXiv 2408.02846 同样提及只能用私有工具）。
