# Source Note: Endor Labs 部署形态与数据流（Outpost / Trust & Compliance）

- URL（一组，均官方文档）:
  - https://docs.endorlabs.com/setup-deployment/outpost
  - https://docs.endorlabs.com/trust-compliance
- 发布方： Endor Labs（官方文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

### Trust & Compliance 页（部署模型与数据流）

1. **两种主部署模型**：
   - **Hybrid scanning**：endorctl CLI 在客户 CI/CD 环境内运行，"analysis of your software is performed inside your environment"，仅扫描**元数据**回传 Endor 云租户。
   - **Cloud scanning**：GitHub App 等云端方案，Endor 获得源码访问权；repo 被克隆进"dedicated ephemeral container"，扫描完成后容器与全部数据删除，"The source code is removed after each scan, and only the metadata related to the scan is retained"。
2. **数据留存**：finding 数据、finding 位置（repo 名/文件名/行号）、集成配置、身份 claims、用户遥测。SCA 扫描会"Assesses the source code or final artifact to create and identify a call graph for the specific version of your code"。
3. **AI 模型发现功能**：可能把代码片段发往 **Azure OpenAI Service** 以识别使用中的模型名。
4. **EU 数据驻留**：独立 EU 环境，"all your organization's data is stored and processed on **Azure** infrastructure in the EU region"；非个人 OSS 包元数据（包名/版本/漏洞信息）从**共享的美国 OSS 集群**拉取；"No EU customer data transits to the US"。→ 佐证主云为 Azure，且存在一个所有客户共享的 OSS 数据集群。
5. 信任材料外链：Drata Trust Center、subprocessors 页、DPA。

### Outpost 页（on-prem 扫描调度）

6. **Outpost = "deployable on-prem instance of the Endor Labs scheduler"**，部署在客户私有 Kubernetes 集群上，页面标题自称面向 "air-gapped environments"。
7. 扫描调度与扫描本身在客户防火墙内运行，**"After the scans are completed, only the scan results are sent to Endor Labs"**——即结果仍须出网到 Endor 云，不是控制面整体离线。
8. **全租户二选一**："you cannot use the cloud-based Endor Labs scheduler… All monitoring scans in your Endor Labs tenant will be carried out on your Kubernetes cluster"——不可按项目混用。
9. 声称"full feature parity with regular cloud-based Endor Labs scans"。
10. 典型动机：源码不得出网、防火墙限制、CI 集成复杂、需扫私有 artifact registry。

## 支撑报告结论

- 维度 1（架构与交付）：Endor 是 **SaaS 优先 + 扫描执行可下沉**（hybrid CLI / Outpost on K8s），**没有证据表明存在完全自托管/真 air-gapped 的控制面**（Outpost 仍需把结果传回 Endor 云）。
- 维度 8（数据底座）：Azure 为主云 + 共享 OSS 集群（美区）为跨客户数据底座的直接证据。
