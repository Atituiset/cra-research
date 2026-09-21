# Source Note: Snyk 不依赖 NVD 的时差证据（官方博客）

- URL: https://snyk.io/blog/snyk-users-dont-have-to-worry-about-nvd-delays/
- 标题: Snyk users don't have to worry about NVD delays
- 发布方: Snyk 官方博客
- 发布日期: 2024-03-13（NVD 2024-02 停摆事件后）
- 抓取日期: 2026-09-21
- 来源层级: 厂商官方（含可核对的定量声明）

## 关键事实点

1. **数据源五类**（原文）：结构化社区生态库（如 RubySec Advisory DB）；官方库与 advisory（如 NVD）；**用机器学习从未编目的公开论坛/源码仓库挖掘未公开漏洞**；社区与学术披露协作；自有研究（如 Leaky Vessels runc 逃逸）。
2. **与 NVD 的差异策略**（原文）：
   - "every open source advisory added to the Snyk Vulnerability Database is accompanied by precise package coordinates, vulnerable version ranges, CVSS vectors... **regardless of what other sources provide**"；
   - "while NVD only analyzes vulnerabilities with CVE IDs, the Snyk Security Team **analyzes vulnerabilities regardless of their CVE ID assignment status**"——无 CVE 的漏洞也入库；
   - NVD 数据作为 secondary 并列展示（与 CLI JSON 示例中 `cvssSources` Snyk=primary / NVD=secondary 一致）。
3. **时差定量证据**（原文）："As of March 12, 2024, **more than 500 unique CVEs** published in the Snyk Vulnerability Database in 2023 and 2024 have **not yet been analyzed by NVD**"，举例 CVE-2024-22243（Spring open redirect，High）与 CVE-2024-1597（PostgreSQL SQL injection，Critical），"both of which were already published and analyzed **3 weeks ago** in the Snyk Vulnerability Database"。
4. **容器 advisory 的边界自认**：容器侧走半自动流程，**severity/CVSS 以 Linux 发行版自评为主**；"Advisories in which the Linux distribution does not provide their own CVSS assessment... and relies on (or passes through) NVD's instead, **will see delays in CVSS assessment** as a result of this incident"——即容器 advisories 并非完全免疫 NVD 延迟。
5. Snyk 是 CVE **CNA**（其披露流程官方页与 cve.org 名录一致；labs.snyk.io/vulnerability-disclosure 接受 JS/Java/Python/.NET/Go/Ruby/PHP 包的上报）。

## 营销页配套声称（厂商声称，注意口径）

- https://snyk.io/platform/security-intelligence/ ："covers **3x more vulnerabilities** than the next largest public database"；"**92% of JavaScript vulnerabilities** were reported by Snyk before the NVD"；"Detect and remediate issues **47 days faster** (on average) than with the next largest vulnerability database"。——无方法学披露，标注为厂商声称；"47 days"被多家第三方引用转述。

## 对本轮深挖的支撑

- 维度 1：差异策略（无 CVE 也收录、自评 CVSS primary）+ 时差可考证据（500 CVEs / 3 周 / 92% / 47 天）。
- 维度 10：容器 advisory 依赖发行版→NVD 透传链条的自认延迟。
