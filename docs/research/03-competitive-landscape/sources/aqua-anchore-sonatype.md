# Source Note: Aqua Security / Anchore Enterprise / Sonatype SBOM Manager（官方+第三方汇编）

## Aqua Security
- URL: https://www.aquasec.com/products/container-vulnerability-scanning/；https://appsecsanta.com/aqua-security（2026-07）；https://safeguard.sh/resources/blog/aqua-security-platform-buyer-review-2026（2026-03）
- 层级: 厂商营销页 + 第三方评测
- 事实点:
  - CNAPP 五支柱（镜像扫描/CWPP/KSPM/CSPM/IaC），eBPF 运行时（Tracee）；Trivy 是其开源扫描器（36k+ stars，2026 年最主流 OSS SCA/容器扫描器）。
  - 漏洞管理卖点："deep runtime context 降噪"；SCA 属供应链模块但**非 Aqua 主战场**（第三方评测一致）。
  - 未见 CRA 专门页面/方案（检索未命中）。
- 支撑结论: CNAPP 阵营以运行时上下文见长；Trivy 的存在使"基础扫描"彻底免费化（商品化最底层）。

## Anchore Enterprise
- URL: https://anchore.com/blog/anchore-enterprise-v6-announcement/（2026-05-18）；https://anchore.com/blog/anchore-enterprise-5-26/（2026-04-21）；https://docs.anchore.com/current/docs/compliance_management/（2026-08-11）；Q4 2025 release webinar（SlideShare, 2025-12-17）；https://appsecsanta.com/anchore（2026-06）
- 层级: 厂商官方博客/文档 + 第三方评测
- 事实点:
  - v6（2026-05）定位"统一 SBOM-powered 合规方案"，消除工具碎片化（厂商声称）。
  - 核心机制：存储 pipeline 生成的所有 SBOM，持续与漏洞 feed 匹配——新 advisory 发布即定位受影响制品，**无需重新扫描**（第三方评测确认这是与 CI 内跑 Grype 的本质区别）。
  - Q4 2025：非容器资产扫描（文件系统/VM/Git repo），SBOM 类型覆盖 application/container/device/filesystem/firmware/library/module/VMDK。
  - Grype 支持消费 VEX 文档（`--vex-documents`）；Syft 1.18+ 输出 CycloneDX 1.7（ECMA-424 第 2 版，2025-12 批准）。
  - Policy-as-code 合规管理（官方文档）。
- 支撑结论: "SBOM 库存储+持续重匹配"是 SBOM 管理商品化的标准形态；SBOM 类型枚举（device/firmware…）显示其向产品级对象扩展但未形成漏洞生命周期闭环。

## Sonatype
- URL: https://help.sonatype.com/en/software-bill-of-materials-sbom.html；https://help.sonatype.com/en/iq-2024-release-notes.html；https://safeguard.sh/resources/blog/sonatype-sbom-manager-overview（2026-06）；https://www.merito.com/vendors/sonatype/sbom-manager（2026-04）
- 层级: 厂商官方文档 + 第三方买家指南
- 事实点:
  - SBOM Manager（2023 年推出的独立产品）：SPDX/CycloneDX，SBOM 生成/校验/存储/分发全生命周期，1000+ 组织（厂商声称）。
  - **VEX 注释可从旧版本 SBOM 复制到新版本 SBOM**（IQ 2024 release notes）——极少数明确处理"版本间 VEX 延续"的功能。
  - Lifecycle（IQ Server）2025 release：Security Vulnerability Detection Type 策略约束等；数据源为自建 Sonatype 漏洞情报（"proprietary vulnerability intelligence"，202.1 release notes）。
  - 未见专门 CRA 产品页（检索未命中；SBOM Manager 营销以 EO 14028/NIS2 为主）。
- 支撑结论: Sonatype 是"SBOM 作为一等管理对象"最成熟者；VEX 跨版本延续功能直接呼应 Product→Version 维度，但对象是 application/SBOM 而非 CRA 意义上的"产品+版本+证据链"。
