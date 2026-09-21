# CRA 漏洞全生命周期 — Phase 0 垂直切片 PoC

对一个最小 C 产品和一个最小 Go 产品，跑通完整闭环：

```
产物提取(SBOM) → 漏洞关联(OSV) → Reachability 分析 → VEX 判定
→ 签名证据链(in-toto attestation) → 证据包导出
```

## 验证的三个假设

- **H1** — C/C++ function-level reachability 的工程可行性（精度上限是开放问题，
  证伪也是高价值结论）
- **H2** — 结论级 in-toto attestation 能统一承载 reachability 判定 / VEX statement /
  修复验证三类证据，并可从结论追溯回 工具 → 工件 hash → 时间戳 → 签名者
- **H3** — 基于 PURL + OSV 的漏洞关联管道可用

## 架构

```
examples/go-vuln-app     examples/c-vuln-app
  (x/crypto v0.16.0        (vendored zlib 1.2.12
   x/net v0.19.0)           CVE-2022-37434)
        │                         │ cmake → compile_commands.json
        ▼                         ▼
   ┌───────────────── pipeline ─────────────────┐
   │ sbom.py      syft → CycloneDX + sha256     │  （C 侧合入 sbom-augment 片段，
   │ associate.py PURL → OSV querybatch          │   vendored C 依赖 syft 看不到）
   │              C 侧回退：curation 交叉核对     │
   │ reach_go.py  govulncheck(openvex+json)      │
   │ reach_c.py   Joern(docker) CPG call path    │
   │ vex.py       OpenVEX statements             │
   │ attest.py    in-toto Statement v1, ed25519  │
   │ store.py     SQLite（生产目标 PostgreSQL）  │
   │ export.py    证据包 + trace-report.md       │
   └─────────────────────────────────────────────┘
        │
        ▼
   out/evidence-pack-<product>-<version>/
     sbom.cdx.json · vex.openvex.json · attestations/ · manifest.json · trace-report.md
```

**刻意的技术选择**（来自研究结论）：证据存储用 SQLite（Python 3.12 标准库），README
注明生产目标是 PostgreSQL；**刻意不用任何图数据库**——壁垒在数据模型不在图存储。
**不自研 SBOM 工具**（已商品化），用 syft。vuln→function 映射是公认成本中心，示例 CVE
的映射在 [curation/](curation/) 手工策展（合法做法，见 [curation/README.md](curation/README.md)）。

## 如何运行

前置：go、gcc+cmake、python3.12+pip、docker、网络。工具安装见 [BUILD-LOG.md](BUILD-LOG.md)
（syft → `~/bin`，govulncheck → `~/go/bin`，`pip3 install in-toto securesystemslib`，
Joern 用 docker 镜像 `ghcr.io/joernio/joern:nightly`）。

```bash
cd poc
bash pipeline/run.sh          # 一键端到端
python3 pipeline/store.py --stats
```

产物在 [poc/out/](out/)：[evidence-pack-go-vuln-app-0.1.0/](out/evidence-pack-go-vuln-app-0.1.0/) 与
[evidence-pack-c-vuln-app-0.1.0/](out/evidence-pack-c-vuln-app-0.1.0/)，每个包含 sbom / vex / 签名 attestations /
manifest（全文件 sha256 索引）/ 人类可读追溯报告。

## 成功判据与实测结果

| 判据 | 结果 |
|---|---|
| Go 示例同时产出 affected + not_affected | ✅ 见下 |
| C 示例拿到 main→漏洞函数 call path 作为证据 | ✅ 见下 |
| 每条结论都有 ed25519 签名的 in-toto Statement v1，导出时验签 | ✅ 全部 `signature verified ✓` |
| not_affected 带机器可读 justification + 证据引用 | ✅ |

实测数字（2026-09-18 跑出，原始数据在 [out/](out/)）：

- **go-vuln-app 0.1.0**：SBOM 13 个组件 / 7 个 PURL；OSV 关联 149 条（去重按
  规范 ID 归并后 77 个规范漏洞）；govulncheck 判定 **12 affected / 51 not_affected**，
  14 条 OSV 条目 govulncheck 未覆盖 → `under_investigation`（管道不静默丢弃）。
  关键样例：GO-2023-2402 / CVE-2023-48795（Terrapin，ssh.Dial 可达）= **affected**，
  证据含 call trace `main → connectSSH → ssh.Dial`；
  GO-2024-2687 / CVE-2023-45288（x/net/http2 未引入）= **not_affected**，
  justification `vulnerable_code_not_present`；GO-2024-3321（serverAuthenticate，
  包在二进制中但未被调用）= **not_affected**，
  justification `vulnerable_code_not_in_execute_path`。
  修复验证：[go-vuln-app-fixed](examples/go-vuln-app-fixed) 升级到 x/crypto v0.57.0 / x/net v0.59.0 后重扫，
  12 条原 affected 中 **11 条消失（verification/fixed）**，剩 1 条 GO-2026-4971
  是 Go 1.26.1 标准库自身的漏洞，升依赖修不掉（verification/still_present）——
  如实记录。
- **c-vuln-app 0.1.0**：SBOM = syft 扫描 + 策展增补 zlib 1.2.12；OSV PURL 查询对
  C 库无条目（如实记录），经策展交叉核对关联 CVE-2022-37434；Joern CPG 上找到
  call path `main → gunzip_file → inflate`（长度 3，含 file:line：
  `main.c:37 → main.c:19 (call@main.c:58) → inflate.c:623 (call@main.c:32)`）
  → **affected**。
- 合计签名 attestation **154 条**（Go：reachability 63 + vex 77 + verification 12；
  C：reachability 1 + vex 1），导出时逐条验签全部通过；另做了带外抽查：
  原始 attestation 验签 OK、篡改 payload 后验签拒绝、换错公钥拒绝。

## H1/H2/H3 初步结论

- **H1（C function-level reachability）**：**成立（证据强度：中）**。Joern 从
  compilation database / 源码建 CPG、dump 调用边、BFS 出 main→inflate 最短路径
  的工程链路完全可行。但本例路径长度仅 3、无函数指针/间接调用/宏遮蔽，属于
  理想条件；静态调用图在真实 C 代码库上的精度上限（虚调用、回调、条件编译）
  仍未验证——这正是 H1 说的开放问题。
- **H2（in-toto 统一证据链）**：**成立（证据强度：较强）**。一个自定义
  predicateType 承载了三类结论（reachability/vex/verification），每条含
  evidence（call path、工具输出 sha256、OSV id）、tool{name,version,command}、
  timestamp、signer，DSSE 信封 sha256 内容寻址入库，导出时逐条验签。
  trace-report.md 可从任一结论点查全链。
- **H3（PURL+OSV 关联）**：**Go 侧成立（强）；C 侧不成立（如实证伪）**。
  pkg:golang PURL 与 OSV Go 生态一一对应；而 CVE-2022-37434 在 OSV 只有裸
  GIT range（无包名），pkg:generic/zlib 查询返回空——C/C++ 侧必须靠策展映射
  桥接，这本身是一个研究结论。

## 局限性

- C reachability 只验证了直接调用 + 唯一符号名的理想情况；未覆盖函数指针、
  动态链接、宏生成代码。
- C SBOM 依赖手工增补片段（syft binary classifier 检不出静态链接的 vendored
  zlib——2026-09-18 实测）；生产上应走包管理 manifest（conan/vcpkg）。
- OSV 与 Go vuln DB 存在覆盖差（14 条 under_investigation），关联层需要冲突裁决策略，
  本 PoC 只记录不裁决。
- 签名密钥是随仓库提交的开发密钥（[keys/README.md](keys/README.md)）；生产需 KMS/HSM 与密钥轮换。
- 证据存储是单文件 SQLite；生产目标 PostgreSQL，同 schema 平移。
- Rust 本次砍掉：cargo 生态无成熟 function-level reachability 工具，第一批只验证管道。

## 边界（不做）

UI、CRA Art 14 报告流、多产品/多租户、Agent、SSVC 裁决、Rust。
