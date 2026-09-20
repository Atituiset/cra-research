# curation/ — 手工策展的 vuln → function 映射

**为什么手工策展在本 PoC 中是合法做法**：研究结论已确认 vuln→function 映射数据策展是公认的
成本中心（上游没有覆盖 C/C++ 的成熟映射数据源；Go 侧由 govulncheck 内置数据库解决）。
Phase 0 的目标是验证管道闭环，不是验证策展自动化，因此示例 CVE 的映射由人工根据
NVD / upstream fix commit 策展，并在每条映射里记录策展依据（fix commit、参考链接）。

## 当前内容

| CVE | 包 | 漏洞函数 | 依据 |
|---|---|---|---|
| CVE-2022-37434 | zlib ≤ 1.2.12 | `inflate()`（EXTRA state）@ `inflate.c` | madler/zlib commit `eff308a` + NVD |

## 生产化展望

真实产品需要把这一步产品化：从 fix commit diff 提取函数级映射（GitHub Advisory /
OSV 的 GIT range + commit diff 是主要原料），人工复核长尾。这部分的成本结构是
Phase 1 的研究对象。
