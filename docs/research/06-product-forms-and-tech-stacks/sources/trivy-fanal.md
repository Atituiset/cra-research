# Source Note: Trivy 检测架构（fanal 分析器注册表）

- URL: https://pkg.go.dev/github.com/aquasecurity/trivy@v0.56.2/pkg/fanal/analyzer ；https://factory.ai/open-source-wikis/trivy?page=systems%2Ffanal.md ；https://blog.csdn.net/guoguangwu/article/details/129027523
- 标题: fanal/analyzer package (pkg.go.dev) / fanal — Trivy wiki / trivy os 软件包扫描原理分析
- 发布方: Go 官方包文档（源码生成）；Factory.ai 仓库 wiki（源码走读）；CSDN 源码分析
- 发布日期: 2025–2026 各页
- 抓取日期: 2026-09-20
- 来源层级: 开源仓库一手（源码/文档）+ 源码走读二手

## 关键事实点

- Trivy 核心子系统 `pkg/fanal/`（file analyzer）：把容器镜像/文件系统/仓库/VM 镜像/SBOM 归一化为 `BlobInfo`；架构为**分析器注册表**（`RegisterAnalyzer`），每个 analyzer 认领一类文件（apk/dpkg/rpm 包数据库、各语言 lockfile 等），含 post-analyzer 与 handler 机制。
- OS 包识别 = 解析发行版包管理数据库（apk installed db、dpkg status、rpm db）；镜像按层解包逐层分析，能处理"后续层删除的包不计入最终镜像"。
- 语言栈：**Go** 单体 CLI；配置扫描为 Rego 引擎（Trivy Checks，AVD-* 规则）。

## 支撑报告结论

- CLI/CI 原生扫描器的业界实际栈：Go 单二进制 + 分析器插件注册表 + 逐层镜像分析；这类"识别层"已完全开源商品化，自研无意义（入场底线论据）。
