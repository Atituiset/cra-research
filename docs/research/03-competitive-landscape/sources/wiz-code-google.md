# Source Note: Wiz Code 与 Google 收购（官方博客+第三方+媒体）

- URL:
  - https://www.wiz.io/blog/introducing-wiz-code（2024-09-10）
  - https://www.wiz.io/blog/introducing-wiz-sast-where-code-risk-meets-cloud-context（2025-12-02）
  - https://www.wiz.io/blog/the-missing-link-in-code-to-cloud-visibility-is-finally-here（2025-10-17，Security Graph 打通代码层）
  - https://roboticsandautomationnews.com/2026/05/26/wiz-alternatives-in-2026-7-tools-compared-best-for-cloud-and-code-security/101861/（2026-05，第三方）
  - https://pitchbook.com/profiles/company/431717-23 与多家媒体报道：Google 以 $32B 收购 Wiz，2026-03-11 完成交割
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方博客 + 第三方分析 + 财经媒体

## 关键事实点

- Google 2025-03-18 宣布 $32B 全现金收购 Wiz，2026-03-11 完成交割（EU 批准后），Wiz 并入 Google Cloud 但保留品牌与多云承诺（Reuters/PitchBook 及多家媒体一致）。
- Wiz Code（2024-09 发布）：SAST/SCA/IaC/secrets/容器扫描，核心价值是与 Wiz Security Graph 的 code-to-cloud 关联（把云端攻击路径回溯到 Dockerfile/Terraform/代码与负责人）。
- Wiz SAST（2025-12）："exposure-aware prioritization"，代码分析+运行时/云上下文。
- 第三方评测（2026-05，roboticsandautomationnews）：Wiz Code 仍落后于专门 AppSec 工具——无静态 reachability、无 AI AutoTriage、AutoFix 仅限主分支、DAST 覆盖有限（第三方评价，需注意竞品文章立场）。
- latio.tech（2024-10，James Berthoty）：Wiz Code SCA 无静态 reachability、有 SBOM 生成——与 2026 评测一致。

## 支撑报告结论

- CNAPP 阵营的 exploitability 优势在**运行时/网络暴露上下文**（互联网可达、工作负载在跑），不在代码级 call graph；Wiz 的 SCA 代码深度是公认短板。
- Google 收购后 Wiz 资源倾斜云安全，CRA/产品合规不是其叙事重点（未见 CRA 专门材料）→ 定位空白论据。
