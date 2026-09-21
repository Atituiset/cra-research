# Source Note: Sonatype SBOM Manager 官方 SBOM/VEX 工作流（本 note 供 03 报告 §6 使用）

- URL: https://help.sonatype.com/en/sbom-vex-workflow.html
- 标题： SBOM VEX Workflow（Sonatype SBOM Manager Help）
- 发布方： Sonatype（官方帮助文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档

## 关键事实点

1. **官方五步工作流（原文编号列表）**："1. **Analyze** the application SBOM for vulnerabilities → 2. **Review** the vulnerabilities from the Bill of Materials → 3. **Annotate** the status of vulnerabilities → 4. **Share** annotated SBOM with stakeholders → 5. **Audit** SBOMs for newly discovered vulnerabilities"。
2. **Reachability 不是编号步骤**：引言段称 "Using reachability analysis, developers determine when their applications are at risk of discovered vulnerabilities and use SBOM Manager to annotate…"——reachability 是**用户在产品外自行做的分析**，SBOM Manager 承接其结论（annotate），产品本身不做 reachability。
3. **VEX 注释体系**（CycloneDX analysis 词表）：status = In triage / Exploitable / False positive / **Not affected** / Resolved / Resolved with pedigree；**"Justification should be specified for all not_affected cases"——是 should（建议），非强制**。justification 九值（code not present / code not reachable / protected at perimeter / at runtime / by compiler / by mitigating control / requires configuration / dependency / environment）。另有 response 字段（update/rollback/workaround 等）。
4. **VEX 跨版本延续（官方文档直接确认）**："Copy VEX Annotations from Previous Versions — When the previous version of the application has been annotated with a VEX status and justification, those annotations may be copied to the current version's vulnerabilities to reduce the time your team spends on vulnerability management."（此前 03 §1.4 的依据是 IQ 2024 release notes，现在有 SBOM Manager 官方文档级确认。）
5. Share 的对象是 **annotated SBOM**（VEX 注释内嵌于 SBOM），非独立 VEX 文档。

## 支撑报告结论

- 二手声明 ④（Analyze → Review → Reachability → Annotate status → Share VEX/SBOM → Audit）**部分成立**：主干五步与"Audit 回到分析"闭环成立；但 "Reachability" 不是官方工作流的编号步骤（系二手声明把引言描述误植为产品步骤），且 Share 的是 annotated SBOM、justification 为建议性而非强制。
- 补强 03 §1.4/§3.3.6：VEX 跨版本复制获官方文档确认；但 justification 非强制 + 无自动失效重估，VEX 生命周期自动化空档判断维持。
