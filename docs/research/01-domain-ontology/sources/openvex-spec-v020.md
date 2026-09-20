# Source Note: OpenVEX Specification v0.2.0 全文

- **URL**: https://raw.githubusercontent.com/openvex/spec/main/OPENVEX-SPEC.md
- **标题**: OpenVEX Specification v0.2.0
- **发布方**: OpenVEX 社区
- **抓取日期**: 2026-09-18
- **来源层级**: 标准组织官方（社区规范）

## 关键摘录 / 事实点

1. VEX statement 核心模型：`statement = product(s) + vulnerability + status(+timestamp)`；VEX 是**带时间戳的 statement 序列**，后发的 statement 覆盖/补充先发者（under_investigation → affected → fixed 的演进示例）。
2. 四个 status label（来自 CISA VEX 工作组）：`not_affected`（必须带 justification 或 impact_statement）、`affected`（必须带 action_statement）、`fixed`、`under_investigation`。
3. 五个 justification label（CISA《VEX Status Justifications》2022-07 定义）：
   - `component_not_present` — 组件根本不在产品里
   - `vulnerable_code_not_present` — 组件在但漏洞代码不在（如构建时裁剪）
   - `vulnerable_code_not_in_execute_path` — 漏洞代码在产品使用方式下不可达
   - `vulnerable_code_cannot_be_controlled_by_adversary` — 攻击者无法控制漏洞代码输入（难以确证）
   - `inline_mitigations_already_exist` — 内置防护完全阻止利用（难以确证，历史上有大量绕过案例）
4. `not_affected` 必须提供机器可读 justification；自由文本 impact_statement 被"highly discouraged"（破坏自动化）。
5. 产品标识：推荐 **PURL**（也接受 cpe22/cpe23、hash）；vulnerability 用 ID + aliases 数组（CVE/GHSA/SNYK-/DSA/USN 混排的真实示例）。
6. 真实示例：Spring Boot 2.6.0-M3 对 CVE-2021-44228 声明 `not_affected` + `vulnerable_code_not_in_execute_path`，impact_statement 解释默认日志系统不是 log4j-core。
7. 规范性来源：CISA《Minimum Requirements for VEX》（2023-04, https://www.cisa.gov/sites/default/files/2023-04/minimum-requirements-for-vex-508c.pdf）和《VEX Status Justifications》（2022, https://www.cisa.gov/sites/default/files/publications/VEX_Status_Justification_Jun22.pdf）。

## 支撑报告中的结论

- §11 VEX 四 status / 五 justification 的权威定义（全文引用基础）
- §11 "VEX 是判断结果还是格式"：VEX 是 CISA 定义的**最小数据集/模型**，OpenVEX/CSAF/CycloneDX 是三种序列化实现
- §11 VEX 时间序列语义（同一 product+vulnerability 的 status 随时间演进）
- §13 Reachability 与 justification `vulnerable_code_not_in_execute_path` 的直接对应关系
