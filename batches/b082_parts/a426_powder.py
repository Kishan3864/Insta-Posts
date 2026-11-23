
# ───────── 426 INDIA · Powder coating job work unit · CAROUSEL 6 · Archivo Black + Inter · graphite / powder mint / hanger yellow
# New technique: overhead conveyor SVG with raw parts hanging on hooks + chalk tags; arrival-order vs grouped-by-shade
# powder-change strip computed from the job list; oven Gantt with hatched powder-change gaps; powder boxes with fill windows.
GR6 = "#1f2528"; CD6 = "#2b3337"; MN6 = "#6fd1b5"; YL6 = "#f2c14e"; TX6 = "#eef2f0"; MU6 = "#a9b5b8"; PA6 = "#f5f2ea"; INK6 = "#1f2528"
SH6 = {"B": ("S‑12 Black matt", "#1a1d1f"), "G": ("S‑07 Grey matt", "#8f979c"), "W": ("S‑21 White gloss", "#f7f7f2")}
JB6 = [("J-31", "Sample Fabricator A", "brackets and gates", 58, "B"), ("J-32", "Sample Furniture B", "chair frames", 24, "W"),
       ("J-33", "Sample Gate Works C", "gate panels", 8, "G"), ("J-34", "Sample Panel Maker D", "panel doors", 30, "B"),
       ("J-35", "Sample Rack Maker E", "rack frames", 20, "G"), ("J-36", "Sample Shop F", "shelves", 16, "W")]
NP6 = sum(j[3] for j in JB6)
ARR6 = [j[4] for j in JB6]
CH_ARR6 = sum(1 for a, b in zip(ARR6, ARR6[1:]) if a != b)
ORD6 = []
for s in ARR6:
    if s not in ORD6: ORD6.append(s)
CH_GRP6 = len(ORD6) - 1
def hm6(m): h, mm = divmod(m, 60); return f"{(h - 1) % 12 + 1}:{mm:02d}"
LD6 = []; t = 9 * 60
for i, s in enumerate(ORD6):
    js = [j for j in JB6 if j[4] == s]; parts = sum(j[3] for j in js)
    mins = math.ceil((40 + parts) / 15) * 15
    LD6.append(dict(n=i + 1, s=s, jobs=js, parts=parts, a=t, b=t + mins)); t += mins + 30
KGP6 = 0.1
STK6 = {"B": 18, "G": 4, "W": 2}
NEED6 = {L["s"]: math.ceil(L["parts"] * KGP6) for L in LD6}
NOW6 = 14 * 60 + 30
def part6(kind, x, col="#9aa3a8"):
    if kind == "br":
        return f'<path d="M{x - 30} 150 h60 v18 h-42 v62 h-18 Z" fill="{col}" stroke="#6b7478" stroke-width="2"/>'
    if kind == "gate":
        bars = "".join(f'<rect x="{x - 44 + k * 88 / 6 - 3:.1f}" y="150" width="6" height="110" fill="{col}"/>' for k in range(1, 6))
        return f'<rect x="{x - 48}" y="146" width="96" height="118" rx="3" fill="none" stroke="{col}" stroke-width="8"/>{bars}'
    if kind == "chair":
        return f'<path d="M{x - 30} 150 v120 M{x + 30} 150 v120 M{x - 30} 150 h60 M{x - 30} 210 h60 M{x - 30} 240 h60" stroke="{col}" stroke-width="8" fill="none" stroke-linecap="round"/>'
    if kind == "shelf":
        return f'<rect x="{x - 46}" y="150" width="92" height="16" rx="3" fill="{col}"/><rect x="{x - 46}" y="200" width="92" height="16" rx="3" fill="{col}"/><rect x="{x - 46}" y="250" width="92" height="16" rx="3" fill="{col}"/><path d="M{x - 40} 150 v116 M{x + 40} 150 v116" stroke="{col}" stroke-width="6"/>'
    return f'<rect x="{x - 40}" y="150" width="80" height="120" rx="4" fill="{col}"/><rect x="{x - 28}" y="164" width="56" height="40" rx="3" fill="#7f888d"/>'
def conveyor6():
    items = [("br", "A? black"), ("chair", "matt or gloss?"), ("gate", "C · grey"), ("panel", "whose?"), ("shelf", "F · white?")]
    g = '<rect x="0" y="34" width="900" height="14" rx="7" fill="#58646a"/>'
    for i, (k, tag) in enumerate(items):
        x = 90 + i * 180
        g += f'<rect x="{x - 16}" y="26" width="32" height="30" rx="6" fill="#3d474c" stroke="#6b7478" stroke-width="2"/><path d="M{x} 56 V132 q0 14 -12 14" stroke="#c8cfd2" stroke-width="4" fill="none" stroke-linecap="round"/>'
        g += part6(k, x)
        g += f'<rect x="{x - 72}" y="292" width="144" height="40" rx="8" fill="#1a2023" stroke="#e9ecea" stroke-width="1.5" stroke-dasharray="4 4"/><text x="{x}" y="318" text-anchor="middle" font-family="Inter" font-style="italic" font-weight="600" font-size="18" fill="#e9ecea"><tspan>{tag}</tspan></text>'
    return f'<svg viewBox="0 0 900 350" style="display:block;width:100%;height:auto">{g}</svg>'
B6 = f"""
body{{--f:'Inter';--h:'Archivo Black';background:radial-gradient(800px 500px at 100% 0%,rgba(111,209,181,.13),rgba(111,209,181,0) 70%),{GR6};color:{TX6}}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{MN6};margin-top:22px}}
h1{{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.22;letter-spacing:-.5px;margin-top:16px}} h1 span{{color:{YL6}}}
.sm6{{font:700 13px/1.4 Inter;letter-spacing:2px;color:{MU6}}}
.cd6{{background:{CD6};border-radius:24px;border:1px solid #3a4448}}
.pp6{{background:{PA6};color:{INK6};border-radius:24px}}.pp6 .sm6{{color:#6c726f}}
.sw6{{display:inline-block;width:26px;height:26px;border-radius:8px;border:2px solid #59656a;flex:none}}
"""
def t6(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{MN6};color:{INK6}"):
    return page(B6 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, TX6, cta, ctacss, tagline=f"{n} / 6", logo_color=TX6)
sw6 = lambda s: f'<i class=sw6 style="background:{SH6[s][1]}"></i>'

CB6 = ["A · 40 br + 18 gates · black?", "B · chairs · <s>grey</s> white gloss", "C · gates · grey · tomorrow??", "D · 30 doors · <u>call back</u>", "E, F · racks, shelves · ask shade"]
QS6 = [("“Whose brackets are these?”", "Tag says only “A?”"), ("“Matt or gloss black?”", "Nobody wrote it down"), ("“Are my gates ready today?”", "Call and wait")]
P["p426_powder_s1"] = t6(1, "POWDER COATING · JOB WORK UNIT", "Powder coating jobs on chalk?<br><span>Every part, shade and load.</span>",
f'''<div class=w61><div class="cd6 cv61"><span class=sm6>THE CHALKBOARD · MON 23 NOV · SAMPLE</span><div class=cb61>{"".join(f'<p>{x}</p>' for x in CB6)}</div><span class=sm6>TODAY'S LINE · RAW PARTS WITH CHALK TAGS</span>{conveyor6()}</div>
<div class=qs61>{"".join(f'<div class="pp6 q"><p>{a}</p><em>{b}</em></div>' for a, b in QS6)}</div>
<div class=bt61><b>{len(JB6)} customers · {NP6} parts · {len(SH6)} shades</b><span>and one chalk tag on each part.</span></div></div>''',
css=f""".w61{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.cv61{{flex:1;padding:20px 24px;display:flex;flex-direction:column;justify-content:space-between;gap:10px}}
.cb61{{flex:1;background:#2f4a3e;border:10px solid #8a6a44;border-radius:14px;padding:14px 22px;display:flex;flex-direction:column;justify-content:space-around}}.cb61 p{{font:italic 500 25px/1.3 Inter;color:#e9f0ea;opacity:.92}}.cb61 s{{opacity:.6}}.cb61 u{{text-decoration:none;color:#ffd77a}}
.qs61{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.qs61 .q{{padding:18px 18px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.qs61 p{{font:800 23px/1.35 Inter}}
.qs61 em{{align-self:flex-start;font:700 15px/1.2 Inter;font-style:normal;border:2px dashed #c9572e;color:#a3401c;border-radius:10px;padding:7px 10px}}
.bt61{{background:{YL6};color:{INK6};border-radius:22px;padding:18px 24px;display:flex;align-items:baseline;gap:12px;flex-wrap:wrap}}.bt61 b{{font:400 28px/1.3 'Archivo Black'}}.bt61 span{{font:600 21px/1.35 Inter}}""")

J1 = JB6[0]
P["p426_powder_s2"] = t6(2, "1 · JOB CARD AT THE GATE", "Tag every part<br><span>the day it comes in.</span>",
f'''<div class=w62><div class="pp6 jc62"><div class=hd><div><span class=sm6>JOB CARD · SAMPLE</span><b>{J1[0]}</b></div><em>Due Wed 25 Nov · 5 PM</em></div>
{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Customer", J1[1]), ("In", "Mon 23 Nov · 10:15 AM"), ("Brackets", "40"), ("Gate panels", "18"), ("Shade", SH6[J1[4]][0]), ("Tags", f"T-201 to T-{200 + J1[3]}")])}
<div class=ph><span class=sm6>PHOTOS AT ARRIVAL</span><div class=th>{"".join(f'<div class=t><svg viewBox="34 140 112 136" style="width:100%;height:100%;display:block">{part6(k, 90, "#8d969b")}</svg></div>' for k in ("br", "gate", "br"))}</div></div></div>
<div class="cd6 ls62"><span class=sm6>ALL JOBS IN TODAY · {NP6} PARTS</span>{"".join(f'<div class=r><b>{j}</b><div><strong>{c}</strong><span>{n} {w}</span></div>{sw6(s)}</div>' for j, c, w, n, s in JB6)}</div></div>''',
css=f""".w62{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.jc62{{padding:22px 24px;display:flex;flex-direction:column;gap:6px;justify-content:space-between}}.jc62 .hd{{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;border-bottom:3px solid {INK6};padding-bottom:12px}}.jc62 .hd b{{display:block;font:400 44px/1.2 'Archivo Black'}}.jc62 .hd em{{font:700 15px/1.3 Inter;font-style:normal;background:{YL6};border-radius:10px;padding:8px 10px;text-align:center;max-width:140px}}
.jc62 .r{{display:flex;justify-content:space-between;gap:10px;padding:8px 0;border-bottom:1px dashed #cfc9ba}}.jc62 .r span{{font:500 21px/1.3 Inter;color:#5b605d}}.jc62 .r b{{font:700 21px/1.3 Inter;text-align:right}}
.jc62 .ph{{display:flex;flex-direction:column;gap:8px;margin-top:4px}}.jc62 .th{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.jc62 .t{{height:104px;border-radius:12px;background:#dfe3e2;overflow:hidden;padding:6px}}
.ls62{{padding:22px 22px;display:flex;flex-direction:column;gap:4px}}.ls62 .r{{flex:1;display:grid;grid-template-columns:62px 1fr 30px;gap:12px;align-items:center;border-top:1px solid #3a4448}}.ls62 .r b{{font:700 20px/1.3 Inter;color:{MN6}}}.ls62 .r strong{{display:block;font:700 20px/1.3 Inter}}.ls62 .r span{{display:block;font:500 18px/1.35 Inter;color:{MU6}}}""")

def strip6(seq, label, n):
    cells = ""
    for i, s in enumerate(seq):
        if i and seq[i - 1] != s: cells += '<u>⟲</u>'
        cells += f'<i style="background:{SH6[s][1]}"></i>'
    return f'<div class=sq><span class=sm6>{label}</span><div class=cl>{cells}</div><b>{pl(n, "powder change")}</b></div>'
GS6 = [s for s in ORD6 for _ in [j for j in JB6 if j[4] == s]]
P["p426_powder_s3"] = t6(3, "2 · OVEN LOADS", "Same shade, same load.<br><span>Fewer powder changes.</span>",
f'''<div class=w63><div class="cd6 cp63">{strip6(ARR6, "IN ARRIVAL ORDER", CH_ARR6)}{strip6(GS6, "GROUPED BY SHADE", CH_GRP6)}</div>
<div class="pp6 gt63"><span class=sm6>OVEN PLAN · MON 23 NOV · SAMPLE RULE: 40 MIN + 1 MIN PER PART, ROUNDED UP</span>
<div class=ax>{"".join(f'<span style="left:{(h * 60 - 540) / 420 * 100:.2f}%">{hm6(h * 60)}</span>' for h in range(9, 17))}</div>
<div class=tr>{"".join(f'<div class="ld s{L["s"]}" style="left:{(L["a"] - 540) / 420 * 100:.2f}%;width:{(L["b"] - L["a"]) / 420 * 100:.2f}%"><b>Load {L["n"]}</b><span>{pl(L["parts"], "part")}</span></div>' for L in LD6)}{"".join(f'<div class=cg style="left:{(L["b"] - 540) / 420 * 100:.2f}%;width:{30 / 420 * 100:.2f}%"></div>' for L in LD6[:-1])}</div>
{"".join(f'<div class=rw>{sw6(L["s"])}<b>Load {L["n"]} · {SH6[L["s"]][0]}</b><span>{" + ".join(j[0] for j in L["jobs"])}</span><strong>{hm6(L["a"])} to {hm6(L["b"])}</strong></div>' for L in LD6)}
<div class=lg><i></i>Hatched: booth cleaning for the next shade</div></div></div>''',
css=f""".w63{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.cp63{{padding:20px 24px;display:flex;flex-direction:column;gap:14px}}.sq{{display:grid;grid-template-columns:150px 1fr 190px;gap:14px;align-items:center}}.sq .cl{{display:flex;align-items:center;gap:5px;min-width:0}}.sq .cl i{{width:44px;height:40px;border-radius:10px;border:2px solid #59656a}}.sq .cl u{{text-decoration:none;font:700 22px/1 Inter;color:{YL6};width:22px;text-align:center}}.sq>b{{font:700 20px/1.3 Inter;text-align:right}}.sq:last-child>b{{color:{MN6}}}
.gt63{{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:10px}}.gt63 .ax{{position:relative;height:22px;margin:4px 30px 0 0}}.gt63 .ax span{{position:absolute;transform:translateX(-50%);font:600 14px/1.4 Inter;color:#6c726f}}.gt63 .ax span:first-child{{transform:none}}
.gt63 .tr{{position:relative;height:150px;background:#e7e3d8;border-radius:14px;margin-right:30px}}.gt63 .ld{{position:absolute;top:8px;bottom:8px;border-radius:10px;padding:10px 12px;display:flex;flex-direction:column;justify-content:center;overflow:hidden}}.gt63 .ld b{{font:700 22px/1.3 Inter}}.gt63 .ld span{{font:500 18px/1.3 Inter}}
.gt63 .sB{{background:#1a1d1f;color:#fff}}.gt63 .sG{{background:#8f979c;color:#fff}}.gt63 .sW{{background:#fff;border:2px solid #b9bdb7;color:{INK6}}}
.gt63 .cg{{position:absolute;top:8px;bottom:8px;border-radius:8px;background:repeating-linear-gradient(45deg,#c9572e 0 5px,transparent 5px 11px);opacity:.6}}
.gt63 .rw{{flex:1;display:grid;grid-template-columns:30px 1fr 150px 160px;gap:12px;align-items:center;border-top:1px dashed #cfc9ba}}.gt63 .rw .sw6{{border-color:#b9bdb7}}.gt63 .rw b{{font:700 22px/1.3 Inter}}.gt63 .rw span{{font:600 20px/1.3 Inter;color:#5b605d}}.gt63 .rw strong{{font:700 22px/1.3 Inter;text-align:right}}
.gt63 .lg{{display:flex;align-items:center;gap:10px;font:600 16px/1.3 Inter;color:#5b605d}}.gt63 .lg i{{width:34px;height:18px;border-radius:5px;background:repeating-linear-gradient(45deg,#c9572e 0 5px,transparent 5px 11px);opacity:.6}}""")

def box6(s, left, need):
    cap = 25; lv = min(left / cap, 1); col = SH6[s][1]
    return f'''<svg viewBox="0 0 200 220" preserveAspectRatio="xMidYMid meet"><path d="M30 44 L52 20 H192 L170 44 Z" fill="#d9c8a6" stroke="#8c7a58" stroke-width="2"/><path d="M170 44 L192 20 V180 L170 204 Z" fill="#b8a27a" stroke="#8c7a58" stroke-width="2"/>
<rect x="30" y="44" width="140" height="160" fill="#c9b48c" stroke="#8c7a58" stroke-width="2"/><rect x="46" y="60" width="44" height="128" rx="4" fill="#efe9dc" stroke="#5e5038" stroke-width="2"/>
<rect x="48" y="{62 + 124 * (1 - lv):.1f}" width="40" height="{124 * lv:.1f}" fill="{col}" stroke="#59656a" stroke-width="1"/>
<rect x="102" y="72" width="56" height="40" rx="6" fill="#fff"/><text x="130" y="99" text-anchor="middle" font-family="Inter" font-weight="800" font-size="17" fill="{INK6}"><tspan>{SH6[s][0][:4]}</tspan></text>
<text x="130" y="140" text-anchor="middle" font-family="Inter" font-weight="700" font-size="13" fill="#5e5038"><tspan>25 kg box</tspan></text></svg>'''
P["p426_powder_s4"] = t6(4, "3 · POWDER STOCK", "Enough powder for today?<br><span>Know before the load.</span>",
f'''<div class=w64><div class=bx64>{"".join(f"""<div class="pp6 b"><span class=sm6>{SH6[s][0].upper()}</span><div class=im>{box6(s, STK6[s], NEED6[s])}</div>
<div class=nm><div><span>In stock</span><b>{STK6[s]} kg</b></div><div><span>Today</span><b>{NEED6[s]} kg</b></div></div>
<div class=br><i style="width:{min(NEED6[s] / max(STK6[s], NEED6[s]), 1) * 100:.0f}%" class="{'ov' if NEED6[s] > STK6[s] else ''}"></i></div>
<em class="{'no' if NEED6[s] > STK6[s] else ('lo' if STK6[s] - NEED6[s] < 3 else 'ok')}">{'Short by ' + str(NEED6[s] - STK6[s]) + ' kg' if NEED6[s] > STK6[s] else ('Only ' + str(STK6[s] - NEED6[s]) + ' kg left after' if STK6[s] - NEED6[s] < 3 else str(STK6[s] - NEED6[s]) + ' kg left after')}</em></div>""" for s in ORD6)}</div>
<div class=bt64><div class="cd6 ru"><span class=sm6>HOW “TODAY” IS WORKED OUT</span><p>Parts in each load × {KGP6:g} kg a part (your own sample rule), rounded up.</p></div>
<div class="cd6 ms"><span class=sm6>ORDER SENT · 9:00 AM</span><p>To Sample Powder Supplier: 20 kg of <span style="white-space:nowrap">{SH6["W"][0]}</span>, needed by 11:30 AM for Load 2.</p><em>Delivered 11:05 AM · stock updated</em></div></div></div>''',
css=f""".w64{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.bx64{{flex:1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px;min-height:0}}
.bx64 .b{{padding:20px 20px;display:flex;flex-direction:column;gap:12px}}.bx64 .im{{flex:1;min-height:0;position:relative}}.bx64 .im svg{{position:absolute;inset:0;width:100%!important;height:100%!important}}
.bx64 .nm{{display:grid;grid-template-columns:1fr 1fr;gap:10px}}.bx64 .nm span{{display:block;font:600 15px/1.3 Inter;color:#6c726f}}.bx64 .nm b{{font:400 34px/1.25 'Archivo Black'}}
.bx64 .br{{height:14px;border-radius:7px;background:#e2ddd0;overflow:hidden}}.bx64 .br i{{display:block;height:100%;background:#2f8f76;border-radius:7px}}.bx64 .br i.ov{{background:#c9572e}}
.bx64 em{{font:700 16px/1.3 Inter;font-style:normal;border-radius:10px;padding:9px 10px;text-align:center}}.bx64 em.ok{{background:#d8f0e8;color:#1f6b57}}.bx64 em.lo{{background:#fbecc4;color:#7a5a08}}.bx64 em.no{{background:#f7d9cd;color:#9b3515}}
.bt64{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:14px}}.bt64>div{{padding:20px 22px;display:flex;flex-direction:column;gap:8px}}.bt64 p{{font:600 20px/1.4 Inter}}.bt64 em{{font:700 16px/1.3 Inter;font-style:normal;color:{MN6}}}""")

def st6(j):
    L = next(L for L in LD6 if L["s"] == j[4])
    return ("Ready", "rd") if L["b"] <= NOW6 else ("In oven", "ov") if L["a"] <= NOW6 else ("Waiting", "wt")
RDY6 = [j for j in JB6 if st6(j)[0] == "Ready"]
P["p426_powder_s5"] = t6(5, "4 · READY AND OUT", "Customers get a message,<br><span>not a “come and check”.</span>",
f'''<div class=w65><div class="cd6 bd65"><span class=sm6>ALL JOBS · NOW {hm6(NOW6)} PM</span>{"".join(f'<div class=r><b>{j[0]}</b><span>{j[1]}</span>{sw6(j[4])}<em class={st6(j)[1]}>{st6(j)[0]}</em></div>' for j in JB6)}
<div class=tt><span>Ready now</span><b>{len(RDY6)} of {len(JB6)} jobs</b></div></div>
<div class=rt65><div class="pp6 ms"><span class=sm6>MESSAGE TO {J1[1].upper()}</span><p>{J1[0]} is ready: 40 brackets and 18 gate panels in S‑12 black matt. Pickup any time after 4 PM.</p><div class=th>{"".join(f'<div class=t><svg viewBox="34 140 112 136" style="width:100%;height:100%;display:block">{part6(k, 90, "#1a1d1f")}</svg></div>' for k in ("br", "gate"))}</div></div>
<div class="pp6 gp"><span class=sm6>GATE PASS OUT · {J1[0]}</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Parts in", J1[3]), ("Coated", J1[3]), ("Going out", J1[3])])}<em>Counts match · signed by driver</em></div></div></div>''',
css=f""".w65{{flex:1;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:16px;min-height:0}}
.bd65{{padding:22px 22px;display:flex;flex-direction:column;gap:4px}}.bd65 .r{{flex:1;display:grid;grid-template-columns:58px 1fr 28px 92px;gap:10px;align-items:center;border-top:1px solid #3a4448}}.bd65 .r b{{font:700 20px/1.3 Inter;color:{MN6}}}.bd65 .r span{{font:600 19px/1.3 Inter}}
.bd65 em{{font:700 14px/1.2 Inter;font-style:normal;border-radius:9px;padding:8px 4px;text-align:center}}.bd65 em.rd{{background:{MN6};color:{INK6}}}.bd65 em.ov{{background:{YL6};color:{INK6}}}.bd65 em.wt{{background:#3a4448;color:{TX6}}}
.bd65 .tt{{display:flex;justify-content:space-between;align-items:center;background:{YL6};color:{INK6};border-radius:14px;padding:12px 16px;margin-top:6px}}.bd65 .tt span{{font:700 18px/1.3 Inter}}.bd65 .tt b{{font:400 26px/1.3 'Archivo Black'}}
.rt65{{display:flex;flex-direction:column;gap:16px}}.rt65 .ms{{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:10px}}.rt65 .ms p{{font:600 24px/1.45 Inter}}.rt65 .th{{display:grid;grid-template-columns:1fr 1fr;gap:10px;flex:1;min-height:150px}}.rt65 .t{{border-radius:12px;background:#dfe3e2;padding:6px;overflow:hidden}}
.rt65 .gp{{padding:20px 22px;display:flex;flex-direction:column;gap:4px}}.rt65 .gp .r{{display:flex;justify-content:space-between;padding:7px 0;border-bottom:1px dashed #cfc9ba}}.rt65 .gp .r span{{font:500 18px/1.3 Inter;color:#5b605d}}.rt65 .gp .r b{{font:700 19px/1.3 Inter}}.rt65 .gp em{{margin-top:8px;font:700 16px/1.3 Inter;font-style:normal;background:#d8f0e8;color:#1f6b57;border-radius:10px;padding:9px 12px;text-align:center}}""")

P["p426_powder_s6"] = t6(6, "POWDER COATING JOB APP", "Run a coating unit?<br><span>Let's build your job app.</span>",
f'''<div class=w66><div class=tl66>{"".join(f'<div class=cd6><span class=ib>{ic(i, 38)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("tag", "Job cards", "Tags and photos"), ("clock", "Oven loads", "Grouped by shade"), ("box", "Powder stock", "Know before the load"), ("bell", "Ready alerts", "And a gate pass out")])}</div>
<div class="pp6 q66"><span class=sm6>A QUESTION FOR COATING UNITS</span><p>How do you keep track of whose parts are whose once they are all on the line? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{YL6};color:{INK6}",
css=f""".w66{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl66{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl66>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl66 .ib{{width:84px;height:84px;border-radius:24px;background:{MN6};color:{INK6}}}.tl66 b{{font:400 36px/1.3 'Archivo Black'}}.tl66>div>span:last-child{{font:500 23px/1.4 Inter;color:{MU6}}}
.q66{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q66 p{{font:700 29px/1.4 Inter;text-wrap:pretty}}""")
