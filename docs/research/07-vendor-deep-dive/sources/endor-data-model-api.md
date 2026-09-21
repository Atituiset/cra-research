# Source Note: Endor Labs 数据底座与对象模型（REST API data model 官方文档）

- URL（一组，均官方文档）:
  - https://docs.endorlabs.com/developers-api/rest-api/using-the-rest-api/data-model/common-fields
  - https://docs.endorlabs.com/developers-api/rest-api/using-the-rest-api/data-model/resource-kinds
  - https://docs.endorlabs.com/llms.txt （含 OpenAPI specs: /api-reference/openapi.v3.json、openapi.full.v3.json、topapi.v3.json；API reference 按 *Service 分组）
- 发布方： Endor Labs（官方文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

### 对象模型（common-fields 页）

1. **Kubernetes 风格资源模型**：所有对象 = UUID + **Meta**（name/description/**kind**/version/**parent_uuid/parent_kind**/create_time/update_time/upsert_time/created_by/updated_by/tags/annotations）+ **TenantMeta**（namespace，层级式全限定名，如 `endor.prod.app`）+ **Spec**（资源本体）+ **Context**。
2. **Context 区分扫描来源**（同一项目的不同扫描产出互不污染）：
   - `CONTEXT_TYPE_MAIN`（默认分支，id=default）；
   - `CONTEXT_TYPE_REF`（分支扫描）；
   - `CONTEXT_TYPE_CI_RUN`（PR 扫描，id=PR UUID，**三周后自动删除**，`will_be_deleted_at`）；
   - `CONTEXT_TYPE_SBOM`（SBOM 导入，id=SBOM serial number）；
   - `CONTEXT_TYPE_EXTERNAL`（同租户跨项目依赖/vendor 目录的副本，**只算 call graph 不做其他操作**）。
3. **共享 OSS 租户**："There is a common tenant for all OSS projects called `oss`, to which **customers have read access**"——所有客户共享的 OSS 包/漏洞数据面，佐证"预计算 call graph 库存于服务端"。
4. **ProcessingStatus**（Project/PackageVersion 对象）：scan_state 状态机（NOT_PROCESSED/IDLE/INGESTING/ANALYTIC/UNREACHABLE/REQUEST_FULL_RESCAN/REQUEST_INCREMENTAL_RESCAN）；GitHub App 项目每 24h 扫描、每 24h 自动 analytics。
5. **Project 对象示例**：`meta.name` = git repo URL；`spec.git` 含 clone URL/organization/platform_source——**对象模型的根是 repo（Project），无 product/产品线/版本发布对象**。
6. **服务身份痕迹**：`created_by` 示例 `ewok@endor.ai@google@api-key`、`vulnerabilityingestor@endor.ai@x509`——内部用 endor.ai 域 + x509/API-key 身份体系的微服务（ingestor 等）在写对象。

### Resource kinds / API 面

7. API reference 按 **\*Service** 分组（ProjectService、PackageVersionService、VulnerabilityService、FindingService、**CallGraphDataService**、NamespaceService、OnPremSchedulerService、MalwareService、MalwareExposureService、HuggingFaceModelService、AIProviderKeyService、VersionUpgradeService、SBOM/VEX AsyncJobService（签名下载 URL，5 分钟 TTL + object-store file_path）等数十个）。
8. **CallGraphDataService.GetCallGraphData**："Fetches the call graph for a given **package version**"——call graph 以 PackageVersion 为粒度作为一等资源存储、可 API 读取（证据输出的机器可读形态）。
9. **AIProviderKeyService**：客户可在 root namespace 配置自有 AI provider key，"credential is validated, encrypted with a server-side key and stored; read APIs never return it"——支持 **BYOK 式自带模型 key**（暗示 AI 功能可走客户自己的模型账户）。
10. API 提供 OpenAPI v3 spec 下载（3 个规格文件），API 为 REST/JSON。

## 支撑报告结论

- 维度 8：对象模型 = repo（Project）为中心的资源图，namespace 层级多租户 + context 隔离扫描代际；**无 CRA 意义上的 product/version/support-window 语义**（与 03 报告 §7 结论一致并补强到字段级）。存储技术（数据库选型）无公开证据（不确定）；可确认的证据是 Azure 托管 + 向量数据库（C/C++ embedding）+ 对象存储（SBOM/VEX 签名 URL）。
