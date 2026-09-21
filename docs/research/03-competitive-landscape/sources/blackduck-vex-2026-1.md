# Source Note: Black Duck 2026.1 VEX 官方文档（本 note 供 03 报告 §6 使用）

- URL:
  - https://docs.blackduck.com/r/blackduck/2026.1/black-duck-documentation/vulnerability-exploitability-exchange-vex-.html （正文经 Fluid Topics API 抓取：map `WIl3UIBXQXtRO_8dfbLjxA` = bd-hub-2026.1_en-US，topic `GYoNOujKPWF7dBq1tK0ssQ`/`tW5nTvzD09QTmoolW9DC~w`）
  - https://docs.blackduck.com/r/blackduck/2026.1/black-duck-documentation/remediating-security-vulnerabilities.html （topic `gr0jFNpx7bDaECBh8k~9FQ`）
  - https://abb.app.blackduck.com/doc/ReleaseNotes/2025.1.x/newAndChangedFeatures_2025_1_0.html （2025.1.0 Release Notes，佐证状态引入时间）
- 发布方： Black Duck（官方文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

1. **VEX 围绕 project version 持续更新、SBOM 不变（原文逐字）**："An SBOM serves as a static declaration of components in a product release. After release, it's important to determine the exploitability of any vulnerabilities, and VEX reports facilitate this process. **While the SBOM content remains unchanged, VEX allows for on-demand updates regarding the status of vulnerabilities for specific project versions.**"
2. **状态集**：VEX 报告收录具有以下 BD 状态的 CVE/BDSA 条目：Under Investigation / Needs Review / Known Affected / **Known Not Affected** / Remediation Required / Remediation Complete。
3. **NOT_AFFECTED 强制 justification（原文）**："Known Not Affected — No [不计入风险计算]. **A justification must be provided to ensure that the decision is properly documented.**"（2026.1 Remediating security vulnerabilities 页；同一表述最早见于 **2025.1.0 Release Notes**——即该状态体系 2025.1.0 引入，2026.1 文档继承。）
4. **VEX 报告格式为 CSAF 2.0 profile 5（csaf_vex）**，JSON、仅实现 CSAF v2 最小必需元素；分 Project Version VEX 与 Global VEX 两种；VEX 为独立 license（"must have VEX enabled on your product registration key"）。
5. **BD 状态 → CSAF VEX 映射表（原文）**：AFFECTED→known_affected；NOT_AFFECTED→known_not_affected；MITIGATED→known_not_affected + justification `inline_mitigations_already_exist`；PATCHED / REMEDIATION_COMPLETE→fixed；UNDER_INVESTIGATION / NEEDS_REVIEW / NEW→under_investigation；Duplicate/Ignored 不入报告。
6. **Global remediation**：可对漏洞设全局 remediation status，"applies to new instances of that vulnerability when that component appears on new BOMs"（跨版本/跨项目的判定延续）。
7. 文档局限：Revision History 硬编码 version=1、status=draft（final/interim 为 future support）。

## 支撑报告结论

- 二手声明 ⑤（2026.1 VEX 支持 affected/not affected/under investigation、NOT_AFFECTED 强制 justification、VEX 围绕产品版本持续更新而 SBOM 不变）**成立**；一处口径修正：状态体系实际 **2025.1.0 引入**，2026.1 文档为继承。
- 补强 03 §1.3：VEX 独立 license 模块在 2026.1 文档获确认（registration key 启用）；VEX 报告格式 = CSAF 2.0 profile 5（03 此前未记录格式）；Black Duck 是五家中唯一在官方文档层面明确"SBOM 静态 + VEX 按项目版本持续更新"语义的厂商，支撑其"次近占位者"判断。
