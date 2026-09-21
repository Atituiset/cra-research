# Source Note: Contextual Analysis scanner 工程实现（编写/分发/版本化/自曝局限）

- 来源层级：厂商官方工程博客（JFrog Security Research）+ 厂商官方文档 + 官方 GitHub
- 抓取日期：2026-09-21

## URL 清单

1. 78% 研究博文（2022-11-15，JFrog Security Research 方法论自曝）: https://jfrog.com/blog/turns-out-78-of-reported-cves-on-top-dockerhub-images-are-not-really-exploitable/
2. Contextual Analysis of CVEs 官方文档（2026-09-03 更新）: https://docs.jfrog.com/security/docs/contextual-analysis-of-cves-1
3. CLI Command Summaries（analyzerManager 下载）: https://docs.jfrog.com/integrations/docs/cli-command-summaries
4. GitHub jfrog/jfrog-cli-security issue #592（analyzerManager 缺失报错）: https://github.com/jfrog/jfrog-cli-security/issues/592
5. Security Self-Managed Releases（scanner 随版本迭代记录）: https://docs.jfrog.com/releases/docs/security-self-managed-releases

## 关键事实点

### A. 策展性质（URL 1，原文逐字要点）

- "**it is still impossible to automatically define the needed rules** for performing precise contextual analysis"；通用技术 "**will never give the needed accuracy that's possible only with a per-CVE contextual scanner**"。
- "based on the **daily work of JFrog's security research team**, which analyzes each new vulnerability **on the same day it is disclosed**"。
- URL 2 补充策展优先级三因子：客户常用技术 / CVSS≥7.5（无 CVSS 用 ML 预测 severity）/ 在野利用与媒体热度；覆盖 "more than 1,600 high-profile CVEs"；JAS 订阅客户可 **request research** 点单新 scanner。

### B. 分发与版本化（URL 2/3/5）

- **Upgrade Required 状态原文**："For self-managed environments, the **Xray version needs to be updated to receive a new scanner** for this CVE. A rescan is required after the upgrade is complete. For SaaS…the scanner operates automatically once the update is available." → scanner 执行体随 Xray 版本分发；DBSync v3 的 `contextual_analysis` 流只带元数据（见 jfrog-offline-dbsync.md）。
- Rescan Required："A new scanner for this CVE is available. You need to rescan to retrieve applicability results" → 判定绑定 scanner 版本。
- CLI 侧首次运行自动下载 **Xray Indexer + Analyzer Manager 二进制（约 100MB）**（URL 3 原文）；URL 4 显示 analyzerManager 是独立 fork/exec 的二进制依赖。
- URL 5 可见 scanner 持续迭代条目（如 "Updated Contextual Analysis applicability scanners to support the Python 3.14 runtime"）。

### C. 非 reachability 信号的官方 CVE 示例（URL 2 原文）

- 编译选项：CVE-2018-1000500 BusyBox（`FEATURE_WGET_OPENSSL` 非默认编译 flag）。
- 配置解析：CVE-2024-27316 Apache httpd（`httpd.conf` 的 `LoadModule http2_module`）；官方点明 "**no amount of source-code or binary reachability analysis can determine exploitability, because Apache exposes no API to enable HTTP/2**"。
- CLI flags：CVE-2022-42915 curl（`--proxy` + `gopher://`）。
- 运行时环境：CVE-2024-3219（Python/Windows）、CVE-2020-1751（glibc/PowerPC）、CVE-2022-28321（PAM/openSUSE Tumbleweed）、CVE-2024-45492（libExpat/32-bit）、CVE-2022-4883（libXpm/SUID）。

### D. 自曝的实现局限（URL 1，原文要点）

1. **保守偏好假阳性**："Prefer scanners that tend to show false positives…the opposite case…will be left vulnerable, which is a much more severe scenario."（78% 降噪率是保守设定下的数字）
2. **数据流分析部分覆盖**：CVE-2022-30630 做了 data-flow（non-constant input），CVE-2022-30631（gzip 文件输入）放弃——"guaranteeing whether a file is attacker-controlled is a very hard task"。
3. **性能硬约束**：最精确 scanner 需 "infinite call depth" 与 "inter-module calls"，"greatly increase the scanner's runtime"，高吞吐场景必须取舍。
4. **只扫 first-party 代码**（文件级粒度区分，借 Xray SCA）：理由含 CPE 冗余、3rd-party 代码量、**专有组件许可限制**（"may not have the approval to analyze the proprietary 3rd-party component"）。

## 支撑主文档

- 07-vendor-deep-dive/jfrog.md §2 全部；§10 局限清单 1-4。
- 加深 03 §6①②：03 核实了"五维信号/1/3 不依赖 reachability"的表述存在，本 note 补上 scanner 的工程属性（人工策展、版本分发、性能/许可取舍）。
