# Source Note: Endor Labs C/C++ SCA（官方白皮书 2025-06 + docs C/C++ 页）

- URL（一组）:
  - https://cdn.prod.website-files.com/6574c9e538a34feac8cec013/6852cc3d94c65acb990c5e47_Endor%20Labs%20SCA%20for%20C%20Languages%20Whitepaper.pdf （《Solving the Challenges of C/C++ Software Composition Analysis》，Published 2025-06-18）
  - https://docs.endorlabs.com/scan/sca/c （官方文档 C/C++ 页）
  - https://www.endorlabs.com/learn/introducing-accurate-sca-for-c-c-applications （2025-06-11 发布公告，未深读）
  - https://docs.endorlabs.com/releasenotes/previous-releases/march-2025 （C/C++ Beta 起始）
- 发布方： Endor Labs（官方白皮书 + 官方文档）
- 抓取日期： 2026-09-21
- 来源层级： 厂商官方技术白皮书（含实现细节与自认局限；精度数字为厂商声称）

## 关键事实点（白皮书）

1. **技术路线完全不同于主产品线**：不做 call graph，而是 **代码分段 + 哈希 + embedding 向量相似度**：
   - 专有语言相关分段算法把代码切成分段（"this step has the most significant impact on the quality of results and has required extensive development effort"）；
   - 每个文件/分段算哈希做精确匹配；分段再生成 embedding 进**向量数据库**做模糊匹配（余弦/欧氏距离），识别"复制、修改过、无显式声明"的第三方代码；
   - Endor 自建"comprehensive vector databases"装 C/C++ 依赖的分段 embedding；新增依赖入库"fast and efficient"。
2. **embedding 走 Azure OpenAI**："code segments will be sent to an Endor Labs dedicated **Microsoft Azure OpenAI** deployment to generate embeddings"，可用 opt-out flag 关闭。
3. **扫描流程**（endorctl 本地发起）：遍历目录 → 文件哈希比对包哈希库 → 分段哈希模糊匹配（置信度够则停）→ 未匹配分段送 Azure OpenAI 生成 embedding → 向量库相似度搜索。哈希与 embedding 缓存支持每周差分扫描。
4. **精度声明（厂商声称）**：内部对比测试 "143% more true positives and 81% fewer false negatives than legacy tools"；白皮书自认"hard to quantify how much each of the proprietary source database, segmenting algorithms, and matching methodology contributes"。
5. **自认局限（Implementation Considerations，原文）**：
   - 所有源码须在分析目录树内（不构建、不解析 manifest）；
   - **"Dynamic libraries are not in scope"**；
   - 依赖库未入库则检测不到（"dependencies not included, however, will not be detected"）；
   - **"Reachability is not available for C/C++, although it is a possible future roadmap item"**。
6. 版本识别粒度可细到"Git commit times"；头文件与源文件不论扩展名都分析。

## 关键事实点（docs C/C++ 页，2026-07 快照）

7. 两种模式并存：**Conan package manager scan**（解析 conanfile）+ **segment-based scanning**（`endorctl scan --segment-match-languages=c`）。
8. **embedding 默认关闭**：需 "Endor Labs **AI license**"，在 Settings → Data Privacy 勾选 "Code Segment Embeddings and LLM Processing"；可用 `ENDOR_SCAN_EMBEDDINGS=false` 单次覆盖。→ 数据隐私上把"代码片段出送给 LLM"做成显式 opt-in。
9. **明确不支持二进制库**："Scanning binary library files such as `.so` and `.a` files is **not supported**."
10. 结果含 "Dependency File Locations"（依赖在代码库中的文件路径树）。

## 支撑报告结论

- 维度 4：C/C++ **不是空白但路线隔离**——2025-03 Beta、2025-06 白皮书，用 embedding 相似度而非程序分析；**无 reachability、无二进制/动态库扫描**，嵌入式/固件场景仍是空白。
- 维度 3：佐证漏洞库为"multi-source + 自有研究团队策展"（"A Multi-Source Vulnerability Database… including our world-class research team"）。
- 维度 7/8：Azure OpenAI dedicated deployment + AI license + opt-in 数据隐私开关，是 Endor AI 数据流的硬证据。
