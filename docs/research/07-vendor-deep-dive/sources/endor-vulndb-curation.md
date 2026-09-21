# Source Note: Endor Labs 漏洞数据库与策展（官方 vuln DB 文档 + DroidGPT 史料 + DIMVA'24 论文上下文）

- URL（一组）:
  - https://docs.endorlabs.com/discover/vulnerability-db （官方文档）
  - https://www.globalsecuritymag.fr/Introducing-DroidGPT-AI-that-helps-you-select-better-open-source-software.html （DroidGPT 发布转载，2023-04-07）
  - https://www.devopsdigest.com/endor-labs-introduces-droidgpt （2023-04-10）
  - https://www.enck.org/pubs/dunlap-dimva24.pdf （Dunlap et al., "Pairing Security Advisories with Vulnerable Functions Using Open-Source LLMs", DIMVA 2024；**非 Endor 成果**，作者单位 NC State + Chainguard）
  - https://scholar.google.com/citations?user=sl1ofC0AAAAJ （Henrik Plate 现任 Endor Labs Security Researcher 佐证）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方文档 + 厂商新闻稿转载 + 同行评审论文（独立学术来源）

## 关键事实点

### Endor 漏洞库形态（官方文档）

1. 支持检索的标识符：**CVE / GHSA / PySEC / MAL**（MAL 恶意包条目注明 "OSV supplies the data"——恶意包情报至少部分来自 OSV 聚合）。
2. 漏洞条目结构：Affected Packages（含 introduced/fixed 版本与**数据来源标注**）；Overview 含 "available patches, **impacted classes**, and a link to the **fix commit**"；**Endor Details** 页展示 "**affected call paths and file paths**"；Impact 页展示每个受影响包版本的 findings 数、使用项目数、被依赖数（blast radius）。
3. → 漏洞条目自带**函数/类级映射**（impacted classes + affected call paths），这是 function-level reachability 的数据前提。

### CVE→函数映射的策展方法（证据分级）

4. **厂商声称**：Endor learn 页称通过程序分析自建 CVE→受影响函数（跨版本）映射数据库（见 03 报告 sources/endor-reachability-framework.md）。**本轮未找到官方文档对该策展流水线（是否 LLM 辅助、人工复核比例、覆盖语言）的进一步公开描述（不确定）**。
5. **行业参照（非 Endor）**：DIMVA 2024 论文（Dunlap/Meyers/Reaves/Enck，NC State + Chainguard）量化了该问题的难度：
   - naive 方法（patch link 中所有改动函数都算漏洞函数）precision 仅 **0.22**（78% 改动与漏洞无关）；recall 0.90；
   - 用开源 LLM（CodeLlama 7B/13B/34B、Mixtral 8x7B 等）+ zero/few-shot + CoT 提示，precision 提升至 0.60（**+173%**），recall 降至 0.74（-18%）；
   - ground truth 用 GoVulnDB（Google Go 安全团队人工标注 symbols + govulncheck 自动 derived symbols）；
   - 工具链：PatchParser 解析 commit、Tree-sitter 定位函数边界、CodeT5+ embedding + Faiss 检索 few-shot 示例、LangChain 编排；
   - CoT 慢 13 倍；few-shot 示例顺序会影响 precision/recall 偏向。
   - **注意**：Trevor Dunlap 署名单位为 Chainguard，非 Endor；此论文说明"CVE→函数映射可用 LLM 半自动化"是行业公开技术路线，不能直接当作 Endor 实现的证据。
6. **人员佐证**：Henrik Plate（Eclipse Steady 核心作者，Steady 即 SAP 系函数级可达性 + 人工/程序分析漏洞函数标注系统）现任 Endor Labs Security Researcher（Google Scholar 验证邮箱 endor.ai）——Endor 的漏洞函数策展能力有该领域最直接的人才储备（Interpretation）。

### DroidGPT 史实（定位澄清）

7. DroidGPT（2023-04 发布）= **ChatGPT 套壳的 OSS 选型问答机器人**："combines the power of ChatGPT with Endor Labs' proprietary risk data"，回答包的安全/质量/活跃度/流行度问题。**它是消费策展数据的前端，不是策展流水线本身**。2026 年产品线中其角色已被 MCP server / Agentic UI / AURI 取代（演进脉络见 endor-mcp-auri.md）。

## 支撑报告结论

- 维度 3：漏洞库 = 多源聚合（NVD/GHSA/PySEC/OSV-MAL）+ 自有研究团队策展 + 函数级标注（impacted classes/call paths/fix commit）；"DroidGPT 式 AI 策展"无公开证据，DroidGPT 本体是问答前端；LLM 辅助 CVE→函数映射是行业公开方法（DIMVA'24），Endor 是否采用未公开（不确定）。
