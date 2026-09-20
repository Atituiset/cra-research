# Source Note: Black Duck air-gapped KnowledgeBase（官方文档）

- URL: https://docs.blackduck.com/r/blackduck-onprem/latest/black-duck-air-gapped-knowledgebase/using-black-duck-sca-with-air-gapped-kb-deployed-with-kubernetes.html
- 标题: Using Black Duck SCA with Air-gapped KB deployed with Kubernetes
- 发布方: Black Duck（Synopsys 软件事业部剥离后）官方文档
- 抓取日期: 2026-09-20
- 来源层级: 厂商官方文档

## 关键事实点

- Black Duck 支持 **on-prem（Kubernetes 部署）+ air-gapped KnowledgeBase**：漏洞知识库以本地 KB 节点形式部署在隔离网内，扫描结果在完全断网环境内完成匹配。
- 第三方对比（Konvu 2026-04-28）称 Black Duck 是其对比组合中"最强的 air-gapped 选项"。

## 支撑报告结论

- 企业 SCA 套件物种的交付特征：on-prem/air-gapped 是一等公民，知识库本地化是断网交付的核心工程（KB 数据必须可打包下发）。
