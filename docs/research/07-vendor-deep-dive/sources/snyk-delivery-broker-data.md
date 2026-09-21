# Source Note: Snyk 交付形态与数据处理（Broker + 部署选项 + 数据留存）

- URL:
  - https://docs.snyk.io/snyk-data-and-governance/how-snyk-handles-your-data （2026-07-27 更新）
  - https://docs.snyk.io/platform-administration/snyk-broker/snyk-broker （2026-09-15 更新）
  - https://github.com/Snyk/broker （开源仓库）
- 发布方: Snyk 官方文档 / GitHub
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方文档（一手）

## 关键事实点

### 部署形态（How Snyk handles your data，原文）
1. 三档："**Multi-Tenant SaaS**（最常用）/ **Single-Tenant SaaS: Private Cloud**（隔离、全托管实例）/ **Snyk Broker**（装在客户私有基础设施的 client 代理）"。区域：US、EU、AU。
2. **无 self-hosted/on-prem 平台形态**——Broker 只是把私有网络内的 SCM/Jira/registry 桥接到 Snyk SaaS（multi- 或 single-tenant），扫描与数据平台始终在 Snyk 侧。
3. Broker 仅 **Enterprise plan** 可用；Broker 本身开源（github.com/Snyk/broker）。
4. **Broker 架构**（Broker 文档原文）：Server 在 Snyk SaaS 侧（无需安装）；Client 在客户网络内；连接由 client 主动出向发起（无需开入向端口），建立后 WebSocket 双向；凭证留在客户网络边界内；访问收敛到 **approved data list**（最小权限请求白名单）。**Universal Broker** 目标完全取代 Classic：云端连接参数配置、单 connection 多类型复用、Org↔connection 映射、`snyk-broker-config` 工具/API。覆盖 SCM（GitHub/GHE/GitLab/Bitbucket/Azure Repos）+ Jira + 私有制品库（Artifactory/Nexus）+ 全部主流容器 registry（经 Container Registry Agent）。
5. **源码处理与留存**（数据文档原文，隐私关键）：
   - Snyk Open Source 常规只读 manifest/lock 文件；`--unmanaged` 只存文件哈希+文件名；
   - **Reachability**："Snyk will access and store the contents of your Git repository to facilitate the building of a call graph. **When the analysis completes, your code is deleted from the Snyk system. Only the call graph and function names are maintained.**"
   - Snyk Code：一次性分析，源码按云厂商最短缓存期缓存（AWS S3：24–48h）后删除，只留 issue 位置（file/line/column）+ ID + 解释；"**Snyk Code does not use any customer code for engine training purposes or to extract examples to show possible fixes**"；Fix Suggestions 的 AI 模型只用宽松许可证公开仓库训练。
   - Container：不经 Broker 时会短期存镜像副本，分析后删除。
6. 合规：SOC 2 Type II、ISO 27001:2022 + ISO 27017:2015（Schellman 认证）；GDPR/CCPA DPA。
7. contributing developer 计数会读取被监控仓库**最近 90 天 commit** 的 author email（应请求可提供未哈希版）——定价机制的数据副作用，值得注意。

## 对本轮深挖的支撑

- 维度 7：SaaS-only 判定成立（multi/single-tenant + Broker 桥接，无 on-prem 平台）；Broker 是"出向 WebSocket + 白名单请求"模式，不是数据本地化方案。
- 维度 8：reachability/SAST 的云端短暂存代码、只留 call graph+函数名，是数据底座与隐私边界的一手证据。
