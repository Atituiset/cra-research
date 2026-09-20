# Source Note: Oligo《Proving Compliance at Runtime》（官方博客）

- URL: https://www.oligo.security/blog/proving-compliance-at-runtime
- 标题: Proving Compliance at Runtime
- 发布方: Oligo Security 官方博客
- 发布/更新: 2026-05-28
- 抓取日期: 2026-09-18
- 来源层级: 厂商官方博客（营销+技术混合；客户数字为厂商声称）

## 关键事实点

- 核心论点："build-time theory vs runtime truth"——静态 SBOM 是"化石记录"，90–99% 静态扫描发现的库/函数在运行时从不执行（厂商声称）。
- Deep Application Inspection (DAI)：运行时观测应用执行行为，回答三个问题：漏洞库是否被加载？漏洞函数是否被执行？是否有异常行为？
- 合规价值（厂商声称）：runtime 非执行证据可作为 FedRAMP "reduced likelihood" 条款的风险调整依据，把 critical CVE 修复 SLA 从 72 小时延至 180 天；支持 PCI DSS 4.0（6.3.1/6.3.2/11.3.1）、SOC 2 CC6/CC7。
- 客户效果（厂商声称）：Sage 漏洞积压降 90%、Cato Networks 降 70%。
- 产品功能：自动化 **Runtime SBOM & VEX**（基于实际运行时风险生成）；内核安全传感器 <0.5% CPU。
- 引用 Cloud Security Alliance 数据：攻击者 10–15 分钟即可为已知 CVE 生成 exploit（第三方数据经厂商引用）。

## 支撑报告结论

- "Runtime 证据 → 合规证据"是 exploitability 维度最前沿的叙事；Oligo 把 runtime reachability（函数执行观测）直接转成 VEX/审计证据——这正是 CRA 证据链方向的雏形。
- 但 Oligo 的框架映射仍聚焦美国体系（FedRAMP/PCI/SOC 2），未见到 CRA 专门映射 → 定位空白论据之一。
- 支撑"静态 SBOM 商品化、runtime 动态证据未商品化"。
