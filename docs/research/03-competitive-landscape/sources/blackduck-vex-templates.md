# Source Note: Black Duck SCA 2026.7.0 VEX Templates（官方文档）

- URL:
  - https://docs.blackduck.com/r/1WqD3iF0wWDzpOGfy2mr8Q/NOZwr25uOY7i9Ea8~FscOg（VEX 文档页）
  - https://docs.blackduck.com/r/1WqD3iF0wWDzpOGfy2mr8Q/EbXg6uAReZsBzl___DF5EA（Managing SBOM and VEX Templates）
  - https://community.blackduck.com/s/black-duck-software-composition-analysis（2026-08-31 检索快照）
- 标题: Black Duck SCA 2026.7.0 release / Vulnerability Exploitability eXchange (VEX)
- 发布方: Black Duck（Synopsys 软件业务剥离后独立公司，官方文档）
- 发布/更新: 2026.7.0 版本，2026-08 发布
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方文档 / release notes

## 关键事实点

- Black Duck SCA 2026.7.0 新增 **VEX Templates**：仿照既有 SBOM Templates 能力，允许安全与合规团队定义 VEX 文档中包含哪些漏洞字段/内容（模板化生成）。
- 模板在统一入口 "SBOM and VEX Templates"（Manage 菜单）管理；VEX Templates 标签页需 license 启用 VEX 模块才可见（VEX 为独立付费模块）。
- Black Duck 文档体系中有专门的 VEX 章节（生成/管理）。
- 第三方交叉验证（Docker-Black Duck LinkedIn 文章）：Black Duck 支持导出"以 VEX exploitability status 富化的 SBOM"。

## 支撑报告结论

- VEX 生成能力已进入主流 SCA 厂商的标准版本发布节奏（2026 年中）→ VEX 生成商品化。
- 但 VEX 仍是"模板/导出"形态，按 license 单独售卖 → VEX 的**自动生成依据**（reachability/exploitability 结论自动写入 VEX statement）仍有空间。
