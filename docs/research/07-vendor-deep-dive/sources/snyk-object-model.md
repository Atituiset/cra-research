# Source Note: Snyk 对象模型（Projects / Target / Origin）官方文档

- URL: https://docs.snyk.io/scan-fix-and-prevent/scan-with-snyk/snyk-projects （2026-09-15 更新）；Error Catalog 中 SNYK-TARGET-0002 佐证 Target 是一等资源
- 发布方: Snyk 官方用户文档
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方文档（一手）

## 关键事实点（原文定义）

1. **Target**："represents an external resource Snyk has scanned: a code repository, a Kubernetes workload, or another scannable resource external to Snyk"；import 或 CLI 扫描时创建；import 失败/无发现则 Target 为空。
2. **Project**："defines the items, such as **manifest files**, that Snyk scans for a given Target, with configuration information defining how to run that scan"；一个 Target 含多个 Project；属性含 **Targetfile**（具体扫描对象，如 repo 里的 pom.xml）与 **Type**（扫描方法：SAST / Maven / npm …）。
   - 含义：一个 monorepo 会因多个 manifest 生成多个 Project（第三方实测：单 repo 可生成 5+ 个 Snyk projects）。
3. **Origin**：Target 的属性，定义来源生态（cli/github/gitlab/kubernetes/ecr/artifactory-cr 等 30+ 枚举值）。
4. 层级：Tenant → Group → Organization → (Target → Project)。Business criticality 等 attribute 挂在 **Project** 上（Risk Score 的 contextual 因子来源）。
5. 测试频率按 Project 类型：Open Source 默认每日、Code 默认每周（每日需向 support 申请）、Container 每日、IaC 每周。
6. 规模表述：官方提到"hundreds of thousands of Projects"场景的分页与过滤——对象模型面向海量小对象设计。

## 分析（Interpretation）

- 对象锚点是 **repo/manifest/registry 制品**，而非"产品/产品线/版本"：没有"某产品的 v2.3 在支持期内"的概念；Project 无版本语义（快照靠 monitor 重测覆盖同一 Project）。
- Business criticality 挂 Project 而非产品——CRA 语境下"按产品版本评估风险"需要用户在 Project 层面手工建模，且 Project↔manifest 的多对一使"产品级视图"需要自行聚合。
- 与 03 报告 §6 结论一致并加固：Snyk 距 product/version 对象模型的距离 = 需要在其上自建"产品线→版本→Project 集合"映射层。

## 对本轮深挖的支撑

- 维度 6：Project/Target/Org 官方定义与层级，无 product/version 语义的一手确认。
