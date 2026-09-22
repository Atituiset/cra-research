"""Target architecture figures, explicitly separated from measured observations."""
from matplotlib.patches import Rectangle
from .notebook_figures import canvas, label, edge, node, INK, MUTED, LINE, BLUE, TEAL, AMBER, RED, PURPLE


def band(ax,x,y,w,h,color):
    ax.add_patch(Rectangle((x,y),w,h,facecolor=color,edgecolor='none',zorder=0))


def architecture(case):
    fig,ax=canvas('A1 / TARGET ARCHITECTURE','评估引擎居中，CRA 与 VEX 位于消费端',
        '目标设计 · 来自 chat-history §2、§10–17；不表示三层已全部实现',
        '现有实现提供部分工具接入、历史证据和工作台。VA-IR / Claim Engine / 动态 Pass Manager 仍待建设。',height=9)
    for y,h,c in [(73,26,'#eef4fc'),(32,32,'#edf6f3'),(1,23,'#f6f1fb')]:band(ax,0,y,74,h,c)
    label(ax,2,95,'FACT PROVIDERS  /  事实来源',11,BLUE)
    for x,t,d in [(12,'SCA / 情报','组件、版本、漏洞'),(37,'Static Frontend','产出 CodeGraph'),(62,'Runtime / Config','观测与环境条件')]:
        label(ax,x,85,t,12,INK,ha='center');label(ax,x,77,d,10,MUTED,ha='center')
    edge(ax,(37,72),(37,64),BLUE,2)
    label(ax,2,59,'ASSESSMENT CORE  /  评估核心',11,TEAL)
    for x,t,d in [(12,'Evidence','事实 + 来源 + 边界'),(37,'Claim / VA-IR','支持 / 反证 / unknown'),(62,'Decision','策略 + 理由 + 复核')]:
        node(ax,x,47,t,TEAL,400);label(ax,x,35,d,9,MUTED,ha='center')
    edge(ax,(15,47),(33,47),TEAL,2);edge(ax,(41,47),(58,47),TEAL,2)
    edge(ax,(62,31),(62,24),PURPLE,2)
    label(ax,2,19,'CONSUMERS  /  评估结果投影',11,PURPLE)
    for x,t in [(9,'VEX'),(25,'CRA'),(43,'CSAF'),(63,'CI / Assurance')]:label(ax,x,8,t,12,PURPLE,ha='center')
    ax.plot([77,77],[1,99],color=LINE,ls=':')
    label(ax,89,92,'CONTROL PLANE',10,AMBER,ha='center')
    node(ax,89,78,'Agent / Planner',AMBER,650)
    label(ax,89,59,'读当前 VA-IR\n识别证据缺口\n选择 Analysis Pass',11,INK,ha='center')
    edge(ax,(89,49),(89,38),AMBER,2)
    node(ax,89,31,'Pass Executor',AMBER,380)
    label(ax,89,13,'工具执行 / 预算\n权限 / 停止条件',10,MUTED,ha='center')
    edge(ax,(74,50),(84,76),AMBER,1.5,rad=-.2,style='--')
    edge(ax,(85,32),(70,78),AMBER,1.5,rad=-.3,style='--')
    return fig


def localization(case):
    obs=case['observations']; loc=obs['localization']; reach=obs['reachability']
    fig,ax=canvas('A2 / LOCALIZATION BRIDGE','CVE 如何从组件世界，连接到程序世界？',
        '实际材料对照 · C 样例 / 人工策展定位 / 已签名 Joern 调用路径',
        '实线为材料中已有关系；虚线为策展引用。源码当前 hash 已记录，但与历史制品的完整构建绑定仍待验证。',height=9)
    band(ax,0,65,100,34,'#eef4fc');band(ax,0,3,100,36,'#edf6f3')
    label(ax,2,95,'SUPPLY CHAIN  /  产品与组件',11,BLUE)
    node(ax,10,80,case['subject']['product'],BLUE,540,detail='发布物 0.1.0')
    node(ax,34,80,'zlib '+obs['component']['version'],BLUE,540,detail='SBOM 人工增补')
    node(ax,61,80,case['subject']['vulnerability'],RED,540)
    edge(ax,(13,80),(31,80),BLUE,2);edge(ax,(37,80),(58,80),BLUE,2)
    label(ax,87,83,'Fix commit 引用',11,PURPLE,ha='center')
    label(ax,87,75,loc['fix_commit_references'][-1][:12]+'…',10,MUTED,ha='center')
    edge(ax,(64,80),(77,80),PURPLE,1.5,style='--')
    edge(ax,(61,73),(61,27),AMBER,3,style='--')
    label(ax,58,54,'Localization',14,AMBER,ha='right')
    label(ax,58,46,'人工映射 → 文件 / 符号',10,MUTED,ha='right')
    label(ax,83,55,'已知：函数级定位\n未知：漏洞分支是否执行',10,AMBER,ha='center')
    label(ax,2,34,'PROGRAM FACTS  /  历史调用图',11,TEAL)
    for x,name,location in zip([10,34,61],reach['path'],reach['locations']):
        node(ax,x,21,name,RED if x==61 else TEAL,460)
        label(ax,x,5,location.replace('third_party/zlib/',''),9,MUTED,ha='center')
    edge(ax,(13,21),(31,21),TEAL,2);edge(ax,(37,21),(58,21),TEAL,2)
    label(ax,85,22,'EXTRA 分支\nFEXTRA 前提\n尚无路径敏感证据',10,AMBER,ha='center')
    return fig


def claims(case):
    fig,ax=canvas('A3 / EVIDENCE → CLAIM → DECISION','一条调用路径，能支持多强的结论？',
        '设计投影 · 将现有材料整理为 Claim 示例；没有运行生产 Claim 或 Decision Engine',
        'Reachability 与 Exploitability 分开；unknown 是分析结果，needs_review 是流程状态，stale 是有效性。',height=8.8)
    for x,t in [(1,'已有材料'),(39,'分层 Claim'),(79,'决策与消费')]:label(ax,x,96,t,12,MUTED)
    for y,title,detail in [(79,'人工定位映射','CVE → inflate / 文件与修复引用'),(54,'已签名 call path','main → gunzip_file → inflate'),(23,'上下文缺口','输入控制 / 分支条件 / 缓解措施')]:
        color=AMBER if y==23 else BLUE
        node(ax,9,y,title,color,430)
        label(ax,0,y-16,detail,9,MUTED)
    band(ax,37,61,34,26,'#edf6f3')
    label(ax,40,80,'StructuralReachabilityClaim',12,TEAL)
    label(ax,40,70,'reachable_in_recorded_graph',11,TEAL)
    label(ax,40,63,'只对所记录图快照成立',10,MUTED)
    band(ax,37,14,34,30,'#fff6e9')
    label(ax,40,37,'ExploitabilityClaim',12,AMBER)
    label(ax,40,27,'UNKNOWN',17,AMBER)
    label(ax,40,17,'证据不足；反证也未穷尽',10,MUTED)
    edge(ax,(16,79),(36,77),BLUE,2);edge(ax,(16,54),(36,70),BLUE,2)
    edge(ax,(16,23),(36,27),AMBER,2,style='--')
    edge(ax,(71,73),(87,54),TEAL,2);edge(ax,(71,28),(87,48),AMBER,2,style='--')
    node(ax,88,51,'Decision Policy',PURPLE,600)
    label(ax,88,32,'本例未运行\n需要策略 + 复核',11,MUTED,ha='center')
    label(ax,88,12,'VEX / CRA / CI\n只消费明确的决策投影',10,PURPLE,ha='center')
    return fig


def planner(case):
    fig,ax=canvas('A4 / DYNAMIC PASS MANAGER','Agent 的价值，体现在“下一步为什么查这个”',
        '脚本化设计推演 · 三轮预设教学步骤；不是实际 Agent 调用轨迹',
        '执行器仍需校验权限、前置条件与预算。无工具支持或没有新证据时，应停止并保留 unknown。',height=9)
    cols=[2,28,53,82]
    for x,t in zip(cols,['Evidence gap','选择 Pass','获得 / 仍缺的证据','下一步']):label(ax,x,95,t,12,MUTED)
    rows=[('01  缺少代码定位','Localization','人工映射指向 inflate\n来源与基线随结果保存','继续',BLUE),
          ('02  缺少结构路径','Reachability','读取历史 Joern 结果\n得到函数调用路径','继续',TEAL),
          ('03  利用前提不明','Dataflow / Runtime','本演示无此类提供方\n输入 / 分支证据未解决','停止',AMBER)]
    for y,(gap,pass_name,result,next_action,c) in zip([75,47,19],rows):
        band(ax,0,y-11,100,24,'#f6f8fb' if y!=19 else '#fff6e9')
        label(ax,2,y,gap,12,c);label(ax,28,y,pass_name,12,c)
        label(ax,53,y,result,11,INK);label(ax,86,y,next_action,14,c)
        edge(ax,(22,y),(27,y),c,1.8);edge(ax,(46,y),(51,y),c,1.8);edge(ax,(77,y),(83,y),c,1.8)
    edge(ax,(97,75),(97,47),BLUE,1.5,style='--');edge(ax,(97,47),(97,19),TEAL,1.5,style='--')
    return fig


def invalidation(example):
    fig,ax=canvas('A5 / CONTINUOUS ASSESSMENT','输入变了，哪些结论需要重新计算？',
        '合成依赖示例 · 仅更换源码快照，SBOM 与 advisory 在本例中保持不变',
        '红色 = 依赖失效待重算；蓝色 = 本例不受影响。失效不等于结论反转，旧修订仍保留。',height=9)
    deps=example['dependencies']
    positions={'component_inventory':(8,88),'advisory_snapshot':(8,59),'source_snapshot':(8,19),
        'association_claim':(37,86),'localization_claim':(37,49),'codegraph_snapshot':(37,15),
        'reachability_claim':(61,35),'decision':(80,69),'vex_projection':(95,25)}
    titles={'component_inventory':'SBOM','advisory_snapshot':'Advisory','source_snapshot':'Source v2',
        'association_claim':'Association','localization_claim':'Localization','codegraph_snapshot':'CodeGraph',
        'reachability_claim':'Reachability','decision':'Decision','vex_projection':'VEX projection'}
    stale=set(example['stale'])|{example['changed']}
    for name,inputs in deps.items():
        for source in inputs:edge(ax,positions[source],positions[name],RED if source in stale else BLUE,2,style='--' if source in stale else '-')
    for name,(x,y) in positions.items():
        node(ax,x,y,titles[name],RED if name in stale else BLUE,550 if name==example['changed'] else 390,
             detail='changed' if name==example['changed'] else 'stale' if name in stale else '保留')
    return fig


FIGURES={'architecture':architecture,'localization':localization,'claims':claims,
         'planner':planner,'invalidation':invalidation}


def build_assessment_figure(data,name):
    return FIGURES[name](data)
