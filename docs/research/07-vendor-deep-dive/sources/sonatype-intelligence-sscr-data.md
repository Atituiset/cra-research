# Source Note: Sonatype Intelligence 产品页 + SSCR 2026 NVD 对比数据

- URL: https://www.sonatype.com/products/intelligence ；https://www.sonatype.com/products/open-source-security-dependency-management ；https://www.wokb.cz/Report2/SSCR_2026_final.pdf （2026 State of the Software Supply Chain 报告镜像）；https://blog.cyberdesserts.com/npm-security/ （第三方转述）
- 发布方： Sonatype（营销页/年度报告）；wokb.cz 镜像 PDF；CyberDesserts 第三方
- 抓取日期： 2026-09-21
- 来源层级： 厂商声称（营销页）；厂商研究报告（SSCR，方法论披露但数据不可独立复算）；第三方转述

## 关键事实点

1. **"publishes detailed information on new vulnerabilities 10X faster than NVD"**（Intelligence 页）【厂商声称】。
2. **ABF（Advanced Binary Fingerprinting）**：cryptographic hash + structural similarity + derived coordinate + file name；识别改名/修改/未声明组件；"as deployed" vs "as declared" 叙事；Octopus Scanner 为例证【厂商声称】。
3. **恶意包累计检测 >870K**（Intelligence 页口径，2026 年中）；含 AI 模型伪装。
4. **SSCR 2026 NVD 对比数据**（报告 Figure 3.2 等，镜像 PDF）：与 Sonatype 评分相比，NVD CVSS 精确匹配率 **4.4%**、严重性分桶一致率 **55.7%**；61.3% NVD 偏高 / 34.3% 偏低。
5. **65% OSS CVE 无 NVD 评分（2025）**；Sonatype 富化把可用 CVSS 覆盖 35%→91%（CyberDesserts 转述报告数据）；**1 in 7 CVEs scored by NVD differ from Sonatype by 3+ CVSS points**（Lifecycle 产品页）。
6. 95% 有漏洞组件下载时已有修复版可用；~0.5% 为无上游路径的真边缘案例；Log4j 四个组件 2025 年合计近 18 亿次"可避免的有漏洞下载"。
7. 报告方法节：point-in-time 快照、聚合匿名遥测——**数据不可独立复算，引用时须标厂商报告**。

## 支撑报告结论

- 主文档 §1.2（比 NVD 快/准的证据分级）、§9（数据底座）。
