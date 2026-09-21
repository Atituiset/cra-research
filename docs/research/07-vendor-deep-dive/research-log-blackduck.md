# Research Log — Black Duck Deep Dive（07-vendor-deep-dive）

- 调研日期：2026-09-21
- 执行方式：docs.blackduck.com khub API 批量抓取 + WebSearch/FetchURL 核实网页一手来源
- 前序：03-competitive-landscape §1.3 / §6；khub 方法沿用 research-log #22

## 检索与抓取记录（按序）

1. `GET https://docs.blackduck.com/api/khub/maps` → 117 个 map 全清单落 `/tmp/bd_maps.json`，定位关键 map：
   - `YsDtm_HKwGM6efkx~2HVvQ` = Black Duck Air-gapped KnowledgeBase（15 主题，全部抓取）
   - `1WqD3iF0wWDzpOGfy2mr8Q` = Black Duck Documentation latest en-US（940 行 TOC 落 `/tmp/toc_hub_latest.txt`，按维度选点抓取）
   - `xmDr3Yryk7OYDGb__OGKlg` = Black Duck Signal（31 主题，抓 14 个核心主题）
   - `3we1j4a_j1FLyNb0zozX4g` = BDBA Installation Guide 2026.9.0（6 主题抓 4）
   - `834deLimBke9_ockudDDwg` = Black Duck Detect latest（抓 BitBake/Clang/Conan/detector accuracy）
   - `6dyNreOMuOAenymg0Owm8A` = Software Risk Manager latest（抓 correlation 6 主题）
   - `n97xWy6PqPKE~KNHCQD_3w` = Sigma 2026.9.0（只取 TOC 证实 AI-augmented SAST checker plug-in 存在，未抓正文）
2. khub API 路径修正：map 详情在 `/api/khub/maps/{id}`，TOC 在 `/api/khub/maps/{id}/topics`，正文在 `.../topics/{topicId}/content`（返回 JSON，取 content/html 字段后 strip HTML）。辅助脚本 `/tmp/bd.py` + `/tmp/batch_fetch.py`。
3. 空主题记录：`About Signature Scanning`、`About project version BOMs`、`Architecture and Network Communications` 三个主题为容器页（content 为空），不影响结论（子主题均有正文）。
4. Web 核实：
   - 剥离交易：SEC EDGAR（Synopsys 10-Q R11 / 10-K Note 3）——2024-05-05 签约、2024-09-30 交割、$1.65B、Clearlake+Francisco Partners。
   - Signal 时间线：news.blackduck.com 2025-12-10 发布 PR；blackduck.com 博客 2026-03-23 GA 公告；docs release notes 记 2026-04 GA 版本 → 主文档 §5.3 做了口径修正。
   - Seeker：blackduck.com/interactive-application-security-testing.html（/seeker 路径 403，换 canonical 路径成功）——确认 Seeker 集成 BDBA + Hub KB 统一视图。
   - CRA：blackduck.com 2025-07-17 CRA 博客 + 2026-07-01 "SCA alone won't get you to CRA compliance" 方案页（Tim Mackey 引语）；STMicro 侧用 ST 官方社区贴（community.st.com，2025-03-06）补客户视角。
   - KB 规模：blackduck.com KB 页（8.7M 组件/57,700 forges/3,000 license）vs hub 文档（9M/50,000 站点/260K/2,900）vs 2025-10 datasheet（317K 漏洞/426K 版本）——口径冲突列入无法核实项。
   - CyRC：blackduck.com/resources/cybersecurity-research-center.html（披露清单 + ContextAI 定位）。
5. 未走通/放弃：
   - `https://www.blackduck.com/seeker` 403（Cloudflare 类拦截）；canonical 产品页替代成功。
   - docs.blackduck.com 无独立 Seeker 文档 map（Seeker 文档不在该站），Seeker↔SCA 联动以产品页 + SRM 文档佐证。
   - Sigma AI-augmented checker 只取 TOC 标题，未抓正文（与 SCA 主线距离较远）。
   - Coverity 文档未翻检（体量大且偏 SAST）；由此留下"Coverity reachability 是否另有实现"的无法核实项。

## 对 03 报告的修正点（已在主文档标注）

1. Signal GA 口径：03 写"2026-03 GA"；细化=2025-12-10 发布（受限开放）→ 2026-03-23 GA 公告 → 2026-04 首个 GA 版本（release notes）。
2. Reachability 口径：03 写"Coverity 引擎支撑的可利用路径分析"；本轮官方文档只支持 Detect 调用图 + KB Function Signature Match Service（仅 Java、仅带方法名元数据的 BDSA）。已列入无法核实项 #9。
3. KB 规模：03 引用"400 万+组件"为旧口径；当前官方口径 8.7M–9M+（两组数字冲突，见无法核实项 #2）。

## 证据强度自评

- 文档级（最强）：检测引擎、VEX 状态机、对象模型/LTS、air-gapped 机制、部署形态、自曝局限、Signal 架构（7-agent/BYOLLM/preflight）。
- 厂商声称（营销级）：KB 规模数字、Signal "no false positives"/"significantly better findings"、exploitation window 数字、Gartner MQ。
- 无法核实：见主文档 §12 九条。
