# Source Note: Wiz Security Graph（+ Google 320 亿美元收购）

- URL: https://www.wiz.io/lp/wiz-security-graph ；https://www.wiz.io/academy/detection-and-response/attack-path-analysis ；佐证：https://www.tigergraph.com/blog/google-32b-cybersecurity-bet-validates-graph/ （第三方）
- 标题: Wiz Security Graph / What is Attack Path Analysis
- 发布方: Wiz（厂商）；Google 收购为公开新闻事实
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方 + 新闻（收购为事实）

## 关键摘录 / 技术要点

- Wiz Security Graph：持续映射云资源及其关系，把 code→cloud→runtime 的资产与发现（findings/vulnerabilities/identities/network exposure）连成图，用于 **attack path analysis**（攻击路径 = 多个弱点的组合路径，而非单点 finding）。官方称已从"静态图"演进为 code-to-cloud-to-runtime 闭环。
- Google 以约 320 亿美元收购 Wiz（2025-03 宣布，TigerGraph 2026-06 文章称 "Google's recent agreement to acquire Wiz for $32 billion"）——图方法在云安全商业化上获得最高级别市场验证。
- 旁证：PuppyGraph 等公司发文"用现有关系数据复刻 Wiz Security Graph"，说明图查询层可在关系库上实现，图的价值在**建模与关联**而非专用图数据库（与 GUAC 后端现状互证）。

## 支撑报告结论

- 第四部分：安全知识图谱（资产+发现+上下文的关联图）已被云安全头部厂商验证为平台级底座；但注意 Wiz 的图节点是"云资产/配置/身份"，本课题的图要细到 function/CVE/commit 粒度——粒度更深、数据更难，但也更稀缺。
