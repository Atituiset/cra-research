# 客户应答包 · Acme IoT Gateway v3.2.1
生成: 2026-09-22T16:00:00+08:00（证据链可点验）

## 1. 支持期声明（Annex I Pt II(3)）
- 支持至 **2031-06-30**（≥5 年）

## 2. SBOM 快照
- snapshot: `snap-f07fc15cbc73` · 组件 4 个 · 质量分 100/100
- 格式: CycloneDX-1.7（另附 SPDX 见 out/）

## 3. 漏洞判定（VEX 摘要）
| CVE | 状态 | 理由 | 证据 |
|-----|------|------|------|
| CVE-2021-44228 | **fixed** | 升级 2.14.0→2.17.1，复扫不再命中；PR acme/gateway# | `snap-659b48bed5ac` |
| CVE-2021-45046 | **not_affected** | vulnerable_code_not_in_execute_path | `snap-0b19d3dfdc57` |
| CVE-2021-4034 | **not_affected** | vulnerable_code_not_present | `snap-112203d2b247` |
| CVE-2026-42424 | **under_investigation** | 等待 L2 reachability 分析（SLA 24h） | `snap-92047b266cb1` |

## 4. 事件状态（Art.14）
- INC-2026-0922-001: 24h 预警 **已产出**（2026-09-22T16:00:00+08:00，限期内）；72h 预填；final 模板就绪

## 5. 修复
- log4j-core 2.14.0 → 2.17.1（PR acme/gateway#4721，复扫证据 `snap-4cb376a69180`）

> 本包由 Evidence Graph 装配；每个 snapshot 可在 10 年留存期内回放校验。