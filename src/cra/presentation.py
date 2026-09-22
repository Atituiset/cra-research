"""Read-only presentation: no independent status or risk calculation."""
from html import escape
import json


def render(snapshot):
    def e(value):
        return escape(str(value))

    release_names = {r['id']: f"{r['product']} {r['version']}" for r in snapshot['releases']}
    rows = ''.join(f"<tr><td>{e(release_names[j['release_id']])}</td>"
        f"<td>{e(j['vulnerability'])}</td><td>{e(j['proposed_status'])}</td>"
        f"<td>{e(j['effective_status'])}</td><td>{e(j['review']['decision'] if j['review'] else '待复核')}</td>"
        f"<td><details><summary>判定与证据</summary><pre>{e(json.dumps(j,ensure_ascii=False,indent=2))}</pre></details></td></tr>"
        for j in snapshot['judgments'])
    evidence = ''.join(f"<details><summary>{e(v['predicate']['vulnerability']['id'])} · "
        f"{e(v['predicate']['conclusion_type'])} · measured</summary>"
        f"<pre>{e(json.dumps(v,ensure_ascii=False,indent=2))}</pre></details>" for v in snapshot['evidence'])
    incidents = ''.join(f"<details open><summary>{e(i['event_type'])} · 草稿</summary>"
        f"<pre>{e(json.dumps(i,ensure_ascii=False,indent=2))}</pre></details>" for i in snapshot['incidents'])
    reports = ''.join(f"<details><summary>外部报送记录 · {e(r['stage'])}</summary>"
        f"<pre>{e(json.dumps(r,ensure_ascii=False,indent=2))}</pre></details>"
        for r in snapshot.get('report_records', []))
    verifications = ''.join(f"<details><summary>跨发布物修复复核</summary>"
        f"<pre>{e(json.dumps(v,ensure_ascii=False,indent=2))}</pre></details>"
        for v in snapshot.get('verifications', []))
    releases = ''.join(f"<li>{e(r['product'])} {e(r['version'])}<br><code>{e(r['artifact_sha256'])}</code></li>"
                       for r in snapshot['releases'])
    return f'''<!doctype html><html lang="zh-CN"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>CRA 产品漏洞证据工作台</title>
<style>body{{font:16px/1.6 system-ui,sans-serif;background:#f4f7fb;color:#17263c;margin:0}}
header,main{{max-width:1250px;margin:auto;padding:32px}}header{{background:#142a46;color:white}}
nav{{display:flex;gap:20px;flex-wrap:wrap}}nav a{{color:#bbdcff}}section{{background:white;border:1px solid #dbe3ef;padding:24px;margin:20px 0;border-radius:12px}}
table{{width:100%;border-collapse:collapse}}td,th{{text-align:left;padding:10px;border-bottom:1px solid #ddd;vertical-align:top}}
pre{{white-space:pre-wrap;overflow-wrap:anywhere;max-height:420px;overflow:auto;background:#f0f4f9;padding:14px}}code{{overflow-wrap:anywhere}}
.stats{{display:flex;gap:24px;flex-wrap:wrap}}.stats b{{font-size:28px}}details{{margin:12px 0}}.table{{overflow:auto}}
</style><header><p>CRA · 统一核心 / 真实证据回放</p><h1>产品漏洞证据工作台</h1>
<p>历史工具结果 → 待复核判定 → 处置证据 → 事件草稿 → 内部应答包</p>
<nav><a href="#products">产品</a><a href="#judgments">判定</a><a href="#evidence">证据</a><a href="#incidents">事件</a><a href="workbench.json">数据快照</a></nav></header>
<main><section class="stats"><span><b>{len(snapshot['releases'])}</b> 发布物</span><span><b>{len(snapshot['judgments'])}</b> 当前判定</span><span><b>{len(snapshot['evidence'])}</b> 实测记录</span><span><b>{len(snapshot['reviews'])}</b> 复核记录</span></section>
<section id="products"><h2>① 产品与发布物</h2><ul>{releases}</ul><p>同版本不同构建以制品 hash 区分。这里展示既有 PoC 的实测快照，并非实时漏洞监测。</p></section>
<section id="judgments"><h2>② 关联、分析与判定</h2><p>建议状态与当前有效状态分开。未复核或被拒绝的建议保持调查中；无路径结论需审查分析范围与证据。</p><div class="table"><table><thead><tr><th>发布物</th><th>漏洞</th><th>历史建议</th><th>有效状态</th><th>复核</th><th>详情</th></tr></thead><tbody>{rows}</tbody></table></div></section>
<section id="evidence"><h2>③ 分析与修复验证证据</h2><p>导入和导出时重新验签；签名不代表技术判断必然正确。保留历史 verification，不据此直接改写旧发布物。</p>{verifications}{evidence}</section>
<section id="incidents"><h2>④ 事件与报告草稿</h2><p>KEV 是核查信号。事件需记录知悉时间和适用依据；本地记录不会向监管平台报送。</p>{incidents or '<p>暂无事件。真实漏洞样例不会自动生成虚构的在野利用事件。</p>'}{reports}</section>
<section><h2>⑤ 客户应答与证据导出</h2><p>本目录为内部复核包：原始签名文件位于 sources/，当前统一数据位于 workbench.json，manifest.json 列出文件 hash。</p><p>当前判定尚未重新签发为标准 VEX；本地复核人名称不是认证身份。外部交付前仍需正式身份、签发与标准校验。</p></section></main></html>'''
