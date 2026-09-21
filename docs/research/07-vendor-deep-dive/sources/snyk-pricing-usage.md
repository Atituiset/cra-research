# Source Note: Snyk 定价与 contributing developer 计费（官方页 + 官方文档）

- URL:
  - https://snyk.io/plans/ （抓取时点页面）
  - https://docs.snyk.io/platform-administration/snyk-hierarchy/usage-settings （2026-09-18 更新）
- 发布方: Snyk 官方
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方定价页 + 用户文档（一手）

## 关键事实点

1. **计费单位官方定义**（两来源一致，原文）："developers who have made a **commit to a private repo monitored by Snyk in the last 90 days**"；公开（开源）仓库不计；按 git author email 去重（"recognized through the author email field, set in the local Git settings"）；跨集成/跨仓库只计一次（Group/Org 两级 Usage 页可见总数与按集成 breakdown）。
2. **价格档**（plans 页抓取时点）：
   - Free：$0/月/contributing developer；限 Projects 5 个；Free 测试配额：Open Source 400 次、Code 100 次、IaC 300 次、Container 100 次（Usage 文档）。
   - Team：$25/月/contributing developer 起（年付）；100 Projects。
   - **Ignite（新档，2026 出现）**：$1,260/年/contributing developer 起（≈$105/月），面向 <50 开发者组织的"Enterprise-grade"档。
   - Enterprise：询价。
   - 脚注："products are available for individual purchase. **All products must be purchased within the same plan.** Plan price varies per product."（逐产品计价，plan 内打包）
3. **新计费体系**：Usage 文档出现 **Snyk Credits plan** 与 **Snyk Platform Access plan**（Tenant 级 Billing and Usage 仪表盘、credits 消耗、billable events log）——Snyk 正在从纯 seat 计费向 credits/平台用量计费并行演进（新客登记不适用旧口径）。具体 credit 换算率在 Policies 页，本轮未展开（待补）。
4. 计数机制的实现细节：Snyk 为计数需读取被监控仓库最近 90 天的 commit 记录（见 snyk-delivery-broker-data.md #7）。

## 口径注意

- "90 天窗口 + git email 去重"意味着：离职/转岗者 90 天后自然释放席位；用不同 email 提交会被重复计数（第三方社区 Reddit r/devsecops 有对应讨论，非官方）。
- Ignite 档的"每年 $1,260"折算月价高于 Team 4 倍，买的是 Enterprise 功能下放。

## 对本轮深挖的支撑

- 维度 9：contributing developer 定义、去重机制、四档价格、credits 新体系。
