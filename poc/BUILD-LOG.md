# BUILD-LOG — Phase 0 PoC 构建过程实录

时间：2026-09-18 → 2026-09-19。机器：Linux x86_64（Ubuntu 24.04 系），go1.26.1 /
gcc 13.3 / python3.12.3 / docker 29.3.1 / cmake 3.x，无 java、无 sudo。

## 1. 工具安装

| 工具 | 方式 | 结果 |
|---|---|---|
| syft 1.52.0 | 官方 install script → `/usr/local/bin` 失败（无 sudo，tar+install permission denied）；script 改 `-b ~/bin` 又遇 github releases 下载 HTTP 000（瞬时网络/代理抖动） | 最终直接 `curl -sSfL https://github.com/anchore/syft/releases/download/v1.52.0/syft_1.52.0_linux_amd64.tar.gz` 解到 `~/bin/syft` ✅ |
| govulncheck v1.8.0 | `go install golang.org/x/vuln/cmd/govulncheck@latest` → `~/go/bin` ✅ | 一次成功 |
| in-toto 3.1.0 + securesystemslib 1.5.1 | `pip3 install --break-system-packages in-toto securesystemslib` ✅ | Ubuntu 24.04 PEP668 需 `--break-system-packages` |
| Joern | **docker `ghcr.io/joernio/joern:latest` → 404（tag 已被官方移除，见 joernio/joern#6192，ghcr 只剩 `master`/`nightly`）**；`nightly`（2.44GB）经代理拉取极慢（约 20 分钟，一度疑似 stalled）但最终成功 ✅；期间并行装了 host 备选：Temurin JRE 21（`~/tools/jre`）+ joern-cli v4.0.630 linux-x86_64 zip（1.86GB，`~/tools/joern-cli`，首次下载中断，curl `-C -` 断点续传完成） | **管道实际用 docker 镜像**；host 直装留作 fallback |
| sqlite3 CLI | 未装 | 按既定方案用 Python sqlite3 模块 ✅ |
| bear | 未装 | cmake `CMAKE_EXPORT_COMPILE_COMMANDS=ON` 生成 compile_commands.json ✅ |

## 2. CVE 选型验证过程

**Go 侧**：OSV querybatch 实测 `golang.org/x/crypto@0.16.0` → 42 条（含
GO-2023-2402 / CVE-2023-48795 Terrapin）；`golang.org/x/net@0.19.0` → 18 条（含
GO-2024-2687 / CVE-2023-45288 http2 CONTINUATION flood）。govulncheck 实测：
app 用 `ssh.Dial` → Terrapin 握手路径 **affected**；只 import `x/net/idna` →
http2 全部 **not_affected**。一个示例同时产出两类判定 ✅。

**C 侧候选**：先查 OSV——`OSS-Fuzz/zlib@1.2.12` 与 `OSS-Fuzz/cjson@1.7.15`
querybatch 均返回空；直接 `GET /v1/vulns/CVE-2022-37434` 有条目（madler/zlib
GIT range，last_affected 1.2.12，fix commits 1eb7682f / eff308af）。选
**zlib 1.2.12 + CVE-2022-37434**（漏洞点在 `inflate()` 的 gzip EXTRA 字段处理）。
示例 app 用 `inflateInit2(47)` + `inflate()` 解一个带 FEXTRA 头的 gzip 样本
（gen_sample.py 程序化生成，避免手编字节出错），运行时确实走 EXTRA 状态。

## 3. 关键决策与坑

1. **syft 检不出静态链接的 vendored zlib**：binary 里明明有
   `inflate 1.2.12 Copyright…` 字符串，`--override-default-catalogers
   binary-classifier-cataloger` 也试过了，0 组件。→ C 侧 SBOM 用
   `sbom-augment.cdx.json` 片段增补，如实记录（C/C++ vendored 依赖的 SBOM
   本来就应走 manifest 声明）。
2. **OSV 对 C 库无包生态条目**：CVE-2022-37434 只有裸 GIT range，PURL 查询
   必然为空 → associate.py 加 curation-crosscheck 回退，关联结果标注
   `match_source: curation-crosscheck`。这是 H3 在 C 侧的实证结论。
3. **govulncheck openvex 输出**：`-format openvex` 直接产出 affected /
   not_affected + justification，含 63 条 statement（vuln DB 截至 2026-09-16，
   因此有一大批 2026 新条目）。`-format json` 的同一 OSV 有多条 finding 消息，
   第一条常只有 module 帧——提取 call trace 时要跳过无 function 帧的 finding
   （reach_go.py first_trace 的 fallback 逻辑）。
4. **OSV/GHSA 与 GO-id 双条目去重**：querybatch 对同一问题同时返回 GHSA-* 和
   GO-* 条目，vex.py 按 govulncheck finding 的 aliases 归并，canonical id 一个
   漏洞只出一条 statement；归并不了的（14 条）置 `under_investigation`，
   不静默丢弃——OSV 与 Go vuln DB 的覆盖差如实暴露。
5. **in-toto python 库（3.1.0）没有现成 Statement 模型**：自行构造 Statement v1
   JSON，用 `in_toto.models.metadata.Envelope` 做 DSSE 信封 + `CryptoSigner`
   ed25519 签名。坑：`SSlibKey.from_dict(keyid, dict)` 是双参（公钥 json 里
   要自存 keyid）；私钥 URI 格式是 `file2:`（PKCS8 PEM），不是 `file:`；
   **`Envelope.from_dict` 会原地 pop 掉传入 dict 的字段**——export.py 最初把
   验签后的同一个 dict 写盘，导致导出的 attestation 签名变 `[{}]`（DB 原件
   完好），深拷贝后修复。这类"验签通过但落盘损坏"的问题靠带外抽查
   （篡改 payload / 换错公钥应拒绝）抓出来。
6. **验证（verification）类结论的来源**：复制 go-vuln-app → go-vuln-app-fixed。
   第一版只升到 x/crypto v0.31.0：Terrapin 消失但 11 条 2025/2026 新漏洞仍
   affected——结论本身没错但演示效果差；改升到 latest（x/crypto v0.57.0 /
   x/net v0.59.0）后 12 条原 affected 中 11 条 fixed，剩下 1 条 GO-2026-4971
   是 Go 1.26.1 **标准库自身**的漏洞，升依赖修不掉（要升 toolchain）——
   这是比"全部修好"更有信息量的结果，如实保留。
7. **attestation 内容寻址**：DSSE 信封 canonical JSON 的 sha256 作为 attestation
   id，VEX statement 的 `evidence_refs` 回填 **reachability** attestation 的 hash
   （run.sh 里 vex.py 跑两遍，第二遍带 --attestation-map；attest.py 里
   attestation_map 只记录 reachability 类，避免被同漏洞的 vex attestation 覆盖）。
8. **Joern docker 内运行**：需 `--user $(id -u):$(id -g)`（否则 /out 落下 root
   文件）+ `-e HOME=/tmp -w /tmp`（非 root 时默认 workspace `/app/workspace`
   不可写）；`joern --script` 退出时 save-on-exit 抛 NPE 使 exit code=1，但
   脚本输出已完整——reach_c.py 以"是否拿到 CALL 行"判定成败而非退出码。
   CPG 规模：463 个函数定义、32223 条调用边。

## 4. 实测数字

见 README.md「成功判据与实测结果」。原始输出全部在 `out/`。

## 5. 已知未解

- Joern docker `latest` tag 已不存在（上游 2026-08 的已知 issue），只有
  `master`/`nightly`；镜像 2.44GB，代理环境下拉取约 20 分钟。生产环境应推送
  固定 digest 的镜像到内网 registry。
- syft 对静态链接 C 库的 binary classification 覆盖不足（上游已知问题类别）。
- govulncheck 版本行解析：`-version` 输出多行，Scanner 行才是工具版本
  （reach_go.py 已处理）。
- go-vuln-app-fixed 里剩下的 GO-2026-4971 是标准库漏洞，需要升级 Go toolchain
  才能闭环——超出了本 PoC 的"依赖升级"演示范围。
