import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 406 INDIA · Cricket bat maker · CAROUSEL 5 · Archivo Black + Open Sans · willow cream / leather red / pitch green
# New technique: SVG bat drawings (front with grain lines, side profile with spine + sweet-spot bracket), willow cleft
# isotypes where reserved vs free clefts come from the same order list, and an LED scale readout over a weight-check log.
R6 = "#b3262e"; G6 = "#2f5d3a"; K6 = "#1e1b16"; C6 = "#f3ead6"
def batf(w=120, h=470, grains=8, grip="#2f5d3a", seed=1):
    rr = random.Random(seed)
    hx = w / 2; bw = w - 20; by = h * .36
    gl = "".join(f'<line x1="{10 + bw * (i + .5) / grains + rr.uniform(-2, 2):.1f}" y1="{by + 14}" x2="{10 + bw * (i + .5) / grains + rr.uniform(-3, 3):.1f}" y2="{h - 16}" stroke="#c9a76b" stroke-width="1.6"/>' for i in range(grains))
    gr = "".join(f'<rect x="{hx - 13}" y="{10 + k * 15}" width="26" height="9" rx="3" fill="{grip}" opacity="{.75 + .25 * (k % 2)}"/>' for k in range(int((by - 30) / 15)))
    return f'''<svg viewBox="0 0 {w} {h}" width="{w}" style="display:block;width:100%;height:auto"><rect x="{hx - 14}" y="6" width="28" height="{by}" rx="10" fill="#e8d3a4"/>{gr}
<path d="M{hx - 14} {by - 10} Q{hx - 14} {by + 6} 10 {by + 18} L10 {h - 20} Q10 {h - 4} 26 {h - 4} L{w - 26} {h - 4} Q{w - 10} {h - 4} {w - 10} {h - 20} L{w - 10} {by + 18} Q{hx + 14} {by + 6} {hx + 14} {by - 10} Z" fill="#f1dcae" stroke="#b9925a" stroke-width="2"/>{gl}
<rect x="22" y="{by + 46}" width="{w - 44}" height="34" rx="6" fill="{K6}"/><text x="{hx}" y="{by + 68}" text-anchor="middle" font-family="Archivo Black" font-size="12" fill="#f3ead6" letter-spacing="1">SAMPLE</text></svg>'''

B6 = f"""
body{{--f:'Open Sans';--h:'Archivo Black';background:{C6};color:{K6};font-variant-numeric:lining-nums}}
.kk{{font:800 16px/1.4 'Open Sans';letter-spacing:3px;color:{R6};margin-top:22px;align-self:flex-start}}
h1{{font-family:'Archivo Black';font-weight:400;font-size:58px;line-height:1.24;letter-spacing:-.8px;margin-top:22px}} h1 span{{color:{G6}}}
.sm6{{font:800 13px/1.4 'Open Sans';letter-spacing:2px;color:#7a6f5c}}
.cd6{{background:#fffaf0;border-radius:24px;box-shadow:0 14px 30px rgba(60,40,10,.09)}}
.dk6{{background:{K6};color:#fff;border-radius:24px}}
"""
def t6(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{K6};color:{C6}"):
    return page(B6 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, K6, cta, ctacss, tagline=f"{n} / 5")

Q6 = [("“Same as last time, but lighter.”", "How many grams?", 7, "#2f5d3a"), ("“Use the good willow.”", "Which grade?", 10, "#b3262e"), ("“Thick edges, short handle.”", "Edges in mm?", 6, "#1e4f7a")]
P["p406_bat_s1"] = t6(1, "CRICKET BAT MAKER · BULK ORDERS", "Bat orders lost in voice notes?<br><span>Put it all in one order card.</span>",
f'''<div class=w61><div class=bt61>{"".join(f'<div class="cd6 bc61"><p class=vn61><i>{ic("chat", 22)}</i>{q}</p><div class=bw61>{batf(150, 470, g, c, i + 3)}</div><span class=qq61>{a}</span></div>' for i, (q, a, g, c) in enumerate(Q6))}</div>
<div class="dk6 pb61"><span class=sm6>WHAT GOES WRONG</span>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [("Wrong weight", "Bats come back from the shop"), ("Wrong grade", "Good willow used on a cheap order"), ("No count", "“How many are ready?” all day")])}</div></div>''',
css=f""".w61{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.bt61{{flex:1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;min-height:0}}
.bc61{{padding:16px 16px 18px;display:flex;flex-direction:column;align-items:center;gap:12px;min-height:0}}
.vn61{{align-self:stretch;background:#efe4cc;border-radius:16px 16px 16px 4px;padding:10px 12px;font:600 17px/1.4 'Open Sans';display:flex;gap:8px;align-items:flex-start;text-wrap:pretty}}.vn61 i{{color:{R6};flex:none;margin-top:1px}}
.bw61{{flex:1;min-height:0;width:150px;display:flex;align-items:center}}.bw61 svg{{max-height:100%}}
.qq61{{font:800 20px/1.3 'Open Sans';background:{R6};color:#fff;border-radius:12px;padding:8px 14px}}
.pb61{{padding:16px 22px;display:grid;grid-template-columns:auto repeat(3,1fr);gap:18px;align-items:center}}.pb61 .sm6{{color:#d8c9a8;width:96px}}
.pb61 b{{display:block;font:400 20px/1.3 'Archivo Black';color:#f0c36a}}.pb61 span{{font:500 15px/1.4 'Open Sans';color:#e8dfcd}}""")

def batside():
    W, H = 760, 170
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto">
<rect x="20" y="66" width="230" height="30" rx="12" fill="#e8d3a4"/>{"".join(f'<rect x="{30 + k * 22}" y="66" width="14" height="30" rx="4" fill="{G6}"/>' for k in range(10))}
<path d="M250 62 Q285 58 305 56 L722 56 Q742 58 742 76 L742 112 Q742 126 724 128 L690 128 Q640 158 560 158 Q470 158 410 128 L305 128 Q285 122 250 100 Z" fill="#f1dcae" stroke="#b9925a" stroke-width="2.5"/>
<line x1="305" y1="72" x2="722" y2="72" stroke="#c9a76b" stroke-width="1.5"/><line x1="305" y1="90" x2="722" y2="90" stroke="#c9a76b" stroke-width="1.5"/><line x1="305" y1="108" x2="722" y2="108" stroke="#c9a76b" stroke-width="1.5"/>
<rect x="480" y="20" width="160" height="10" rx="5" fill="{R6}"/><rect x="478" y="16" width="4" height="18" fill="{R6}"/><rect x="638" y="16" width="4" height="18" fill="{R6}"/></svg>'''
SP6 = [("Order", "B-112 · Sample Sports Shop"), ("Willow", "English · grade 2"), ("Weight", "1160–1200 g"), ("Handle", "Short · round"), ("Edges", "38–40 mm"), ("Grip · sticker", "Navy · shop's own"), ("Bats", "24 · due Fri 4 Dec")]
P["p406_bat_s2"] = t6(2, "1 · ONE ORDER CARD", "Every detail, written once.<br><span>The workshop sees it too.</span>",
f'''<div class=w62><div class="cd6 sv62"><div class=hd62><span class=sm6>SIDE PROFILE · B-112 · SAMPLE</span><span class=ok62>Sweet spot: mid</span></div>{batside()}
<div class=lb62><span><i style="background:{G6}"></i>Short handle, round</span><span><i style="background:{R6}"></i>Sweet spot: middle of the blade</span><span><i style="background:#c9a76b"></i>Edges 38–40 mm</span></div></div>
<div class=bt62><div class="dk6 sp62"><span class=sm6>ORDER CARD · SAMPLE</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in SP6)}</div>
<div class=ch62>{"".join(f'<div class="cd6 cg62"><span class=sm6>{t}</span><div>{"".join(f"<i class={chr(39)}{'on' if o == s else ''}{chr(39)}>{o}</i>" for o in opts)}</div></div>' for t, opts, s in [("WILLOW GRADE", ["1", "2", "3", "4"], "2"), ("SWEET SPOT", ["Low", "Mid", "High"], "Mid"), ("HANDLE", ["Short", "Long"], "Short"), ("HANDLE SHAPE", ["Round", "Oval"], "Round")])}</div></div></div>''',
css=f""".w62{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.sv62{{padding:18px 22px;display:flex;flex-direction:column;gap:10px}}
.hd62{{display:flex;justify-content:space-between;align-items:center}}.ok62{{font:700 15px/1.2 'Open Sans';background:#f6dcdc;color:{R6};border-radius:10px;padding:7px 12px}}
.lb62{{display:flex;justify-content:space-between;gap:10px}}.lb62 span{{display:flex;gap:8px;align-items:center;font:600 16px/1.3 'Open Sans'}}.lb62 i{{width:16px;height:16px;border-radius:4px;flex:none}}
.bt62{{flex:1;display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,1fr);gap:16px;min-height:0}}
.sp62{{padding:18px 22px;display:flex;flex-direction:column;gap:2px}}.sp62 .sm6{{color:#d8c9a8;margin-bottom:4px}}.sp62 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:12px;border-top:1px solid rgba(255,255,255,.12)}}
.sp62 .r span{{font:500 17px/1.3 'Open Sans';color:#d8cdb8}}.sp62 .r b{{font:700 19px/1.3 'Open Sans';text-align:right}}
.ch62{{display:flex;flex-direction:column;gap:12px}}.cg62{{flex:1;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:8px}}.cg62>div{{display:flex;gap:8px}}
.cg62 i{{flex:1;font:700 17px/1.2 'Open Sans';font-style:normal;text-align:center;padding:9px 4px;border-radius:10px;background:#efe4cc;color:#6d624f}}.cg62 i.on{{background:{G6};color:#fff}}""")

UNIT6 = 2
GR6 = [("Grade 1", 16, 0), ("Grade 2", 40, 32), ("Grade 3", 48, 20), ("Grade 4", 28, 0)]
NEW6 = 30
FREE6 = GR6[1][1] - GR6[1][2]
def cleft(c):
    return f'<svg viewBox="0 0 22 56" width="22" height="62" preserveAspectRatio="none" style="display:block"><path d="M3 2 L19 2 L19 54 L3 54 Z" fill="{c}" stroke="#8a6a3a" stroke-width="1.4"/><line x1="8" y1="6" x2="8" y2="50" stroke="#8a6a3a" stroke-width=".8" opacity=".6"/><line x1="14" y1="6" x2="14" y2="50" stroke="#8a6a3a" stroke-width=".8" opacity=".6"/></svg>'
RES6 = [("B-112", "Sample Sports Shop", "24 bats", "Grade 2"), ("B-115", "Sample Club", "8 bats", "Grade 2"), ("B-116", "Sample Store", "20 bats", "Grade 3")]
P["p406_bat_s3"] = t6(3, "2 · WILLOW STOCK BY GRADE", "Which clefts are free?<br><span>See what's already booked.</span>",
f'''<div class=w63><div class="cd6 st63"><div class=hd63><span class=sm6>WILLOW CLEFTS IN STOCK · 1 ICON = {UNIT6} CLEFTS · SAMPLE</span><div class=lg63><span><i style="background:{R6}"></i>Booked</span><span><i style="background:#f1dcae"></i>Free</span></div></div>
{"".join(f'<div class=r63><b>{g}</b><div class=ic63>{"".join(cleft(R6 if k < r // UNIT6 else "#f1dcae") for k in range(n // UNIT6))}</div><em>{n - r} free</em></div>' for g, n, r in GR6)}</div>
<div class=bt63><div class="cd6 rs63"><span class=sm6>BOOKED FOR ORDERS</span>{"".join(f'<div class=r><div><b>{o}</b><span>{c}</span></div><em>{q} · {g}</em></div>' for o, c, q, g in RES6)}</div>
<div class="dk6 nw63"><span class=sm6>NEW ORDER · B-118</span><p>Wants {NEW6} bats in grade 2. Only {FREE6} grade 2 clefts are free.</p><div class=ans63>Tell the buyer: {FREE6} now, {NEW6 - FREE6} after the next willow lot.</div></div></div></div>''',
css=f""".w63{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.st63{{padding:18px 22px;display:flex;flex-direction:column;gap:6px}}
.hd63{{display:flex;justify-content:space-between;align-items:center;gap:10px;margin-bottom:4px}}.lg63{{display:flex;gap:14px}}.lg63 span{{display:flex;gap:6px;align-items:center;font:600 15px/1.2 'Open Sans'}}.lg63 i{{width:16px;height:16px;border-radius:4px;border:1.4px solid #8a6a3a}}
.r63{{display:grid;grid-template-columns:104px 1fr 86px;gap:10px;align-items:center;border-top:1px solid #efe4cc;padding:12px 0}}.r63 b{{font:400 19px/1.3 'Archivo Black'}}.ic63{{display:flex;gap:5px;flex-wrap:wrap}}
.r63 em{{font:700 17px/1.2 'Open Sans';font-style:normal;text-align:right;color:{G6}}}
.bt63{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.rs63{{padding:16px 20px;display:flex;flex-direction:column;gap:4px}}.rs63 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid #efe4cc}}.rs63 b{{display:block;font:400 19px/1.3 'Archivo Black'}}.rs63 span{{font:500 15px/1.3 'Open Sans';color:#7a6f5c}}
.rs63 em{{font:700 15px/1.2 'Open Sans';font-style:normal;background:#f6dcdc;color:{R6};border-radius:10px;padding:7px 10px;white-space:nowrap}}
.nw63{{padding:18px 22px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.nw63 .sm6{{color:#f0c36a}}.nw63 p{{font:600 26px/1.45 'Open Sans';text-wrap:pretty}}
.ans63{{background:{G6};border-radius:16px;padding:16px 18px;font:700 22px/1.4 'Open Sans';text-wrap:pretty}}""")

ST6 = [("Cleft cut", 24), ("Pressed", 24), ("Handle fitted", 20), ("Shaped", 16), ("Sanded", 12), ("Grip + sticker", 8), ("Packed", 6)]
WT6 = [("Bat 1", 1182), ("Bat 2", 1176), ("Bat 3", 1206), ("Bat 4", 1164), ("Bat 5", 1191), ("Bat 6", 1158)]
def wst(g):
    if g > 1200: return ("Over · sand a little more", "ov")
    if g < 1160: return ("Light · move to another order", "lt")
    return ("In range", "ok")
OKN6 = sum(1 for _, g in WT6 if wst(g)[1] == "ok")
P["p406_bat_s4"] = t6(4, "3 · STAGES AND WEIGHT CHECK", "“How many are ready?”<br><span>Count stages, weigh bats.</span>",
f'''<div class=w64><div class="cd6 sg64"><span class=sm6>B-112 · 24 BATS · STAGE COUNT · SAMPLE</span>{"".join(f'<div class=r><span>{a}</span><div class=br><i style="width:{n / 24 * 100:.1f}%"></i></div><b>{n} / 24</b></div>' for a, n in ST6)}</div>
<div class=bt64><div class="dk6 sc64"><span class=sm6>WEIGHT CHECK · TARGET 1160–1200 g</span><div class=led64>1182<small>g</small></div><p>{OKN6} of {len(WT6)} bats weighed today are in range.</p></div>
<div class="cd6 wl64"><span class=sm6>TODAY'S WEIGHT LOG</span>{"".join(f'<div class=r><b>{a}</b><span>{g} g</span><em class={wst(g)[1]}>{wst(g)[0]}</em></div>' for a, g in WT6)}</div></div></div>''',
css=f""".w64{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.sg64{{padding:16px 22px;display:flex;flex-direction:column;gap:2px}}
.sg64 .r{{display:grid;grid-template-columns:150px 1fr 76px;gap:12px;align-items:center;height:38px}}.sg64 .r span{{font:600 17px/1.3 'Open Sans'}}.sg64 .r b{{font:700 17px/1.3 'Open Sans';text-align:right}}
.sg64 .br{{height:18px;border-radius:9px;background:#efe4cc;overflow:hidden}}.sg64 .br i{{display:block;height:100%;background:{G6};border-radius:9px}}
.bt64{{flex:1;display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr);gap:16px;min-height:0}}
.sc64{{padding:18px 22px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.sc64 .sm6{{color:#d8c9a8}}.sc64 p{{font:600 23px/1.45 'Open Sans';text-wrap:pretty}}
.led64{{background:#0d1a10;border:3px solid #3a4a3c;border-radius:16px;padding:12px 18px;font:700 76px/1.2 'DejaVu Sans Mono';color:#7dff9a;text-align:right;letter-spacing:2px}}.led64 small{{font-size:28px;margin-left:8px}}
.wl64{{padding:14px 20px;display:flex;flex-direction:column;gap:2px}}.wl64 .r{{flex:1;display:grid;grid-template-columns:64px 76px 1fr;gap:10px;align-items:center;border-top:1px solid #efe4cc}}
.wl64 b{{font:700 16px/1.3 'Open Sans'}}.wl64 span{{font:600 16px/1.3 'DejaVu Sans Mono'}}.wl64 em{{font:700 14px/1.25 'Open Sans';font-style:normal;border-radius:9px;padding:6px 9px;text-align:center}}
.wl64 em.ok{{background:#dfeee2;color:{G6}}}.wl64 em.ov{{background:#f6dcdc;color:{R6}}}.wl64 em.lt{{background:#f7ead0;color:#7a5800}}""")

P["p406_bat_s5"] = t6(5, "CRICKET BAT ORDER APP", "Make cricket bats?<br><span>Let's build your order app.</span>",
f'''<div class=w65><div class=tl65>{"".join(f'<div class=cd6><span class=ib>{ic(i, 36)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("doc", "Order cards", "Grade, weight, handle"), ("box", "Willow stock", "Booked and free clefts"), ("chart", "Stage counts", "Cut to packed"), ("check", "Weight check", "Every bat logged")])}</div>
<div class="dk6 q65"><span class=sm6>A QUESTION FOR BAT MAKERS</span><p>How do bat orders reach your workshop today: voice notes, a diary or a sheet? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{R6};color:#fff",
css=f""".w65{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl65{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl65>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl65 .ib{{width:80px;height:80px;border-radius:22px;background:{G6};color:#f0c36a}}.tl65 b{{font:400 32px/1.3 'Archivo Black'}}.tl65 span{{font:500 22px/1.4 'Open Sans';color:#7a6f5c}}
.q65{{padding:26px 30px;display:flex;flex-direction:column;gap:12px}}.q65 .sm6{{color:#f0c36a}}.q65 p{{font:700 29px/1.45 'Open Sans';text-wrap:pretty}}""")


# ───────── 407 CANADA · Backyard ice rink installer · SINGLE · Bitter + Roboto · ice blue / midnight navy / board orange
# New technique: top-down backyard lots drawn to scale in feet (house, fence, trees) with the rink placed to scale and a
# fit check (rink + 4 ft clearance inside the open yard) that picks the suggested size on the booking bar.
N7 = "#142a44"; O7 = "#e8742c"
LOTS7 = [("Sample Yard A", 50, 70, 20, 40, "Installed · Sat 21 Nov", "dn"), ("Sample Yard B", 45, 80, 24, 48, "Install · Sat 28 Nov", "bk"), ("Sample Yard C", 60, 90, 30, 60, "Site check · Tue 24 Nov", "sc")]
def fits7(yw, yd, rw, rl, house=16): return rw + 8 <= yw and rl + 8 <= yd - house
for _l in LOTS7: assert fits7(_l[1], _l[2], _l[3], _l[4]), _l
def lot7(yw, yd, rw, rl, seed):
    s = 3.0; W = 60 * s + 20; H = 90 * s + 20
    ox = 10 + (60 - yw) * s / 2; oy = 10 + (90 - yd) * s / 2
    rr = random.Random(seed)
    trees = "".join(f'<circle cx="{ox + rr.choice([8, yw * s - 8]):.0f}" cy="{oy + 70 + k * 46:.0f}" r="{rr.randint(7, 10)}" fill="#3d6b5a"/>' for k in range(int((yd * s - 90) / 46)))
    rx = ox + (yw - rw) * s / 2; ry = oy + 16 * s + (yd * s - 16 * s - rl * s) / 2
    return f'''<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" style="display:block;width:100%;height:auto"><rect x="{ox:.0f}" y="{oy:.0f}" width="{yw * s:.0f}" height="{yd * s:.0f}" rx="6" fill="#f7fafc" stroke="#8a9bb0" stroke-width="2.5" stroke-dasharray="7 5"/>
<rect x="{ox + 10:.0f}" y="{oy + 6:.0f}" width="{yw * s - 20:.0f}" height="{16 * s - 14:.0f}" rx="4" fill="#5b6f88"/><rect x="{ox + 10:.0f}" y="{oy + 6:.0f}" width="{yw * s - 20:.0f}" height="{(16 * s - 14) / 2:.0f}" rx="4" fill="#4a5d75"/>{trees}
<rect x="{rx:.0f}" y="{ry:.0f}" width="{rw * s:.0f}" height="{rl * s:.0f}" rx="12" fill="#cfe8f6" stroke="{O7}" stroke-width="5"/><line x1="{rx + 6:.0f}" y1="{ry + rl * s / 2:.0f}" x2="{rx + rw * s - 6:.0f}" y2="{ry + rl * s / 2:.0f}" stroke="#d9442b" stroke-width="2"/>
<circle cx="{rx + rw * s / 2:.0f}" cy="{ry + rl * s / 2:.0f}" r="{min(rw, rl) * s / 5:.0f}" fill="none" stroke="#3b78c4" stroke-width="2"/></svg>'''
WK7 = [("Tue 24", [("Site check", "Yard C", "sc")]), ("Wed 25", [("Install", "Yard D", "bk")]), ("Thu 26", [("Boards", "Yard E", "bk"), ("Site check", "Yard F", "sc")]), ("Fri 27", [("Install", "Yard G", "bk")]), ("Sat 28", [("Install", "Yard B", "bk"), ("Liner", "Yard H", "bk")])]
P["p407_rink"] = page(f"""
body{{--f:'Roboto';--h:'Bitter';background:#e6f1f8;color:{N7}}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{O7};margin-top:22px}}
h1{{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1px}} h1 span{{color:#2f6fae}}
.vw{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm7{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#5f7389}}
.ls7{{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}}
.lc7{{background:#fff;border-radius:22px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 28px rgba(20,42,68,.09)}}
.lc7 .t{{display:flex;justify-content:space-between;align-items:baseline;gap:8px}}.lc7 b{{font:800 19px/1.3 Bitter}}.lc7 .z{{font:500 14px/1.3 Roboto;color:#5f7389}}
.lc7 .sv{{flex:1;min-height:0;width:100%;display:flex;align-items:center;justify-content:center}}.lc7 .sv svg{{max-height:100%;width:auto!important;height:100%!important}}.lc7 .rk{{font:700 17px/1.3 Roboto;text-align:center}}
.st7{{font:700 14px/1.2 Roboto;border-radius:10px;padding:8px 10px;text-align:center}}.k-dn{{background:#e0f1e6;color:#1f6b3a}}.k-bk{{background:#fde8da;color:#a34a12}}.k-sc{{background:#e1ecf8;color:#24558f}}
.wk7{{flex:none;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 28px rgba(20,42,68,.09);min-height:0}}
.dg7{{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}}.dg7>div{{background:#f2f7fb;border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:8px}}
.dg7 h4{{font:800 17px/1.3 Bitter}}.dg7 .j{{border-radius:10px;padding:8px 10px;min-height:62px;display:flex;flex-direction:column;justify-content:center}}.dg7 .j b{{display:block;font:700 15px/1.3 Roboto}}.dg7 .j span{{font:500 14px/1.3 Roboto}}
.bf7{{background:{N7};color:#fff;border-radius:22px;padding:16px 20px;display:grid;grid-template-columns:repeat(4,minmax(0,1fr)) auto;gap:14px;align-items:center}}
.bf7 small{{display:block;font:500 13px/1.3 Roboto;color:#a9bdd3}}.bf7 b{{font:700 17px/1.3 Roboto}}.bf7 .bt{{background:{O7};color:#fff;border-radius:12px;padding:13px 16px;font:800 16px/1.2 Bitter;white-space:nowrap}}
""", "<div class=kk>BACKYARD RINK INSTALLS · BOOKINGS</div><h1>Rink requests by email?<br><span>Size, yard and date in one app.</span></h1>",
f'''<div class=vw><div class=ls7>{"".join(f'<div class=lc7><div class=t><b>{n}</b><span class=z>{yw} × {yd} ft yard</span></div><div class=sv>{lot7(yw, yd, rw, rl, i + 7)}</div><span class=rk>Rink {rw} × {rl} ft</span><span class="st7 k-{k}">{s}</span></div>' for i, (n, yw, yd, rw, rl, s, k) in enumerate(LOTS7))}</div>
<div class=wk7><span class=sm7>CREW WEEK · SAMPLE · YARDS ABOVE DRAWN TO SCALE</span><div class=dg7>{"".join(f'<div><h4>{d}</h4>' + "".join(f'<div class="j k-{k}"><b>{a}</b><span>{y}</span></div>' for a, y, k in js) + '</div>' for d, js in WK7)}</div></div>
<div class=bf7>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a, b in [("Yard (measured)", "45 × 80 ft"), ("Slope", "4 in end to end"), ("Water", "Outdoor tap"), ("Suggested rink", "24 × 48 ft")])}<span class=bt>Book install</span></div></div>''',
N7, "Build backyard rinks? DM us", f"background:{O7};color:#fff")


# ───────── 408 INDIA · Gym equipment dealer (install + service) · SINGLE · Montserrat + Fira Sans · rubber black / chrome / volt lime
# New technique: receipt-style thermal service slip (monospace, dotted rules, zigzag torn bottom via clip-path) beside a
# machine "passport" with an SVG treadmill and a service timeline; the due list comes from the same machine list.
K8 = "#17181a"; L8 = "#c6f04a"
def tread8():
    return '''<svg viewBox="0 0 300 150" width="300" style="display:block;width:100%;height:auto"><rect x="20" y="112" width="250" height="22" rx="11" fill="#2a2c30"/><rect x="34" y="104" width="222" height="10" rx="5" fill="#55585e"/>
<circle cx="44" cy="123" r="8" fill="#8d9198"/><circle cx="246" cy="123" r="8" fill="#8d9198"/><path d="M236 108 L262 22" stroke="#c9cdd3" stroke-width="9" stroke-linecap="round"/><rect x="226" y="10" width="56" height="26" rx="6" fill="#2a2c30"/><rect x="232" y="15" width="30" height="12" rx="3" fill="#c6f04a"/>
<path d="M248 40 L196 46" stroke="#c9cdd3" stroke-width="7" stroke-linecap="round"/></svg>'''
HIST8 = [("Mon 24 Aug", "Installed", "dn"), ("Mon 23 Nov", "3-month service done", "nw"), ("Tue 23 Feb 2027", "Next service", "nx")]
DUE8 = [("Sample Gym A", "6 machines", "Wed 25 Nov"), ("Sample Society Gym", "4 machines", "Thu 26 Nov"), ("Sample Home", "1 treadmill", "Fri 27 Nov"), ("Sample Hotel Gym", "3 machines", "Sat 28 Nov")]
CK8 = ["Belt centred", "Belt lubricated", "Motor and brushes checked", "Emergency stop tested", "Console and speed OK"]
P["p408_gymeq"] = page(f"""
body{{--f:'Fira Sans';--h:'Montserrat';background:#eef0ea;color:{K8}}}
.kk{{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#5d7a12;margin-top:22px}}
h1{{font-family:'Montserrat';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.5px}} h1 span{{background:{L8};padding:0 10px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.vw{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm8{{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#6b6f66}}
.ps8{{background:{K8};color:#fff;border-radius:24px;padding:16px 22px;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:20px;align-items:center}}.ps8 .sm8{{color:#a9ada3}}
.ps8 .id{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}.ps8 .id b{{font:800 22px/1.3 Montserrat;color:{L8}}}
.tl8{{display:flex;flex-direction:column;gap:10px}}.tl8 .r{{display:flex;gap:12px;align-items:center}}.tl8 i{{width:18px;height:18px;border-radius:50%;flex:none;border:3px solid #c9cdd3}}.tl8 i.dn{{background:#c9cdd3}}.tl8 i.nw{{background:{L8};border-color:{L8}}}
.tl8 b{{display:block;font:700 18px/1.3 'Fira Sans'}}.tl8 span{{font:500 15px/1.3 'Fira Sans';color:#a9ada3}}
.bt8{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.rc8{{background:#fbfbf7;padding:20px 22px 34px;display:flex;flex-direction:column;gap:6px;font-family:'DejaVu Sans Mono';box-shadow:0 18px 36px rgba(0,0,0,.12);
clip-path:polygon(0 0,100% 0,100% calc(100% - 14px),95% 100%,90% calc(100% - 14px),85% 100%,80% calc(100% - 14px),75% 100%,70% calc(100% - 14px),65% 100%,60% calc(100% - 14px),55% 100%,50% calc(100% - 14px),45% 100%,40% calc(100% - 14px),35% 100%,30% calc(100% - 14px),25% 100%,20% calc(100% - 14px),15% 100%,10% calc(100% - 14px),5% 100%,0 calc(100% - 14px))}}
.rc8 h3{{font:700 20px/1.3 'DejaVu Sans Mono';text-align:center}}.rc8 .c{{text-align:center;font:400 14px/1.4 'DejaVu Sans Mono';color:#55585e}}
.rc8 hr{{border:0;border-top:2px dotted #9a9d95;margin:4px 0}}.rc8 .l{{display:flex;justify-content:space-between;gap:8px;font:400 15px/1.45 'DejaVu Sans Mono'}}.rc8 .l b{{font-weight:700}}
.rc8 .k{{flex:1;display:flex;align-items:center;gap:10px;font:400 15px/1.35 'DejaVu Sans Mono'}}.rc8 .k i{{font-style:normal;font-weight:700;color:#3f6b00}}
.du8{{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 28px rgba(0,0,0,.07)}}
.du8 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid #ecede7}}.du8 b{{display:block;font:700 19px/1.3 'Fira Sans'}}.du8 span{{font:500 15px/1.3 'Fira Sans';color:#6b6f66}}
.du8 em{{font:700 15px/1.2 'Fira Sans';font-style:normal;background:#eef7d2;color:#3f5a00;border-radius:10px;padding:8px 10px;white-space:nowrap}}
.du8 .msg{{background:{K8};color:#fff;border-radius:14px;padding:12px 14px;font:500 16px/1.45 'Fira Sans';text-wrap:pretty}}
""", "<div class=kk>GYM EQUIPMENT DEALER · INSTALL AND SERVICE</div><h1>Service calls lost in chats?<br><span>Track every machine you sold.</span></h1>",
f'''<div class=vw><div class=ps8><div><div class=id><span class=sm8>MACHINE CARD · SAMPLE</span><b>T-204</b></div>{tread8()}</div>
<div class=tl8><span class=sm8>TREADMILL T-204 · SAMPLE GYM A</span>{"".join(f'<div class=r><i class={k}></i><div><b>{b}</b><span>{a}</span></div></div>' for a, b, k in HIST8)}</div></div>
<div class=bt8><div class=rc8><h3>SERVICE REPORT</h3><div class=c>SAMPLE · NO PRICES</div><hr><div class=l><span>Machine</span><b>T-204</b></div><div class=l><span>Date</span><b>Mon 23 Nov</b></div><div class=l><span>Site</span><b>Sample Gym A</b></div><hr>
{"".join(f'<div class=k><i>[✓]</i>{c}</div>' for c in CK8)}<hr><div class=l><span>Next service</span><b>Tue 23 Feb</b></div><div class=l><span>Owner OK</span><b>By OTP</b></div></div>
<div class=du8><span class=sm8>SERVICE DUE THIS WEEK</span>{"".join(f'<div class=r><div><b>{a}</b><span>{b}</span></div><em>{d}</em></div>' for a, b, d in DUE8)}<div class=msg>Owner gets a reminder 2 days before, and the report by message after the visit.</div></div></div></div>''',
K8, "Sell gym equipment? DM us", f"background:{K8};color:{L8}")


# ───────── 410 USA · Mobile RV repair · SINGLE · Poppins + Source Sans 3 · desert sand / RV teal / rust
# Side-view SVG travel trailer with numbered pins aimed at real parts, matching the numbered problem list in the phone form.
T0 = "#1f7a7a"; U0 = "#b5512a"; K0 = "#22201d"
def rv0():
    return f'''<svg viewBox="0 0 520 230" width="520" style="display:block;width:100%;height:auto"><rect x="0" y="206" width="520" height="8" rx="4" fill="#cdb99a"/>
<path d="M60 40 Q60 22 80 22 L440 22 Q478 22 486 60 L494 170 Q494 186 478 186 L76 186 Q60 186 60 170 Z" fill="#fbf7f0" stroke="#8c7a63" stroke-width="3"/>
<rect x="60" y="120" width="434" height="16" fill="{T0}"/><rect x="60" y="140" width="434" height="6" fill="{U0}"/>
<rect x="140" y="6" width="90" height="18" rx="4" fill="#d9d2c6" stroke="#8c7a63" stroke-width="2"/>
<rect x="84" y="50" width="70" height="46" rx="8" fill="#9fc5cc" stroke="#55707a" stroke-width="2"/><rect x="300" y="50" width="120" height="46" rx="8" fill="#9fc5cc" stroke="#55707a" stroke-width="2"/>
<rect x="196" y="48" width="56" height="128" rx="6" fill="#efe6d8" stroke="#8c7a63" stroke-width="2.5"/><circle cx="240" cy="116" r="4" fill="#8c7a63"/>
<rect x="292" y="40" width="190" height="10" rx="4" fill="#8c7a63"/>
<rect x="432" y="146" width="40" height="30" rx="4" fill="#e8dccb" stroke="#8c7a63" stroke-width="2"/>
<path d="M300 50 L300 186" stroke="#8c7a63" stroke-width="2" stroke-dasharray="6 5"/>
<circle cx="160" cy="190" r="22" fill="#2b2926"/><circle cx="160" cy="190" r="9" fill="#a19a90"/><circle cx="214" cy="190" r="22" fill="#2b2926"/><circle cx="214" cy="190" r="9" fill="#a19a90"/>
<path d="M60 168 L14 176" stroke="#5c544a" stroke-width="6" stroke-linecap="round"/><circle cx="12" cy="176" r="7" fill="#5c544a"/></svg>'''
PINS0 = [(1, 35, 0), (2, 58, 26), (3, 87, 62), (4, 74, 4)]
ISS0 = ["Roof AC not cooling", "Slide-out stuck", "Water heater not lighting", "Awning won't close"]
RT0 = [("8:30 AM", "Sample RV Park · Site 14", "Slide-out stuck", "now"), ("11:00 AM", "Sample Campground · Site 3", "Water heater", ""), ("1:30 PM", "Storage lot · Space 22", "Roof AC check", ""), ("4:00 PM", "Driveway · ZIP 00000", "Awning motor", "")]
FORM0 = f'''<div class=pf0><div class=ph0>Book a mobile RV tech</div>
<div class=f0><small>RV type</small><div class=ch0><i class=on>Travel trailer</i><i>Fifth wheel</i><i>Motorhome</i></div></div>
<div class=f0><small>What's wrong? (match the pins)</small>{"".join(f'<div class="is0{" on" if k == 1 else ""}"><u>{k + 1}</u>{t}</div>' for k, t in enumerate(ISS0))}</div>
<div class=f0><small>Photos</small><div class=pt0><i></i><i></i><span>+ Add</span></div></div>
<div class=f0><small>Where is it parked?</small><b>Sample RV Park · Site 14</b></div>
<div class=f0><small>Notes</small><b class=nt0>Slide won't move in or out since this morning.</b></div>
<div class=f0><small>Day</small><div class=ch0><i>Today</i><i class=on>Tue 24 Nov</i><i>Wed 25</i></div></div>
<div class=f0><small>Time window</small><div class=ch0><i class=on>8 AM–12 PM</i><i>12–4 PM</i><i>4–7 PM</i></div></div>
<div class=bt0>Request visit</div></div>'''
P["p410_rv"] = page(f"""
body{{--f:'Source Sans 3';--h:'Poppins';background:#f2e6d3;color:{K0}}}
.kk{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{U0};margin-top:22px}}
h1{{font-family:'Poppins';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.5px}} h1 span{{color:{T0}}}
.vw{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 372px;gap:22px;min-height:0;align-items:stretch}}
.lf0{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm0{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#7b6d5a}}
.rc0{{background:#fffaf2;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 12px 28px rgba(60,40,10,.09)}}
.rw0{{position:relative}}.pin0{{position:absolute;width:34px;height:34px;border-radius:50%;background:{U0};color:#fff;font:800 17px/1 Poppins;display:flex;align-items:center;justify-content:center;border:3px solid #fff;box-shadow:0 4px 10px rgba(0,0,0,.25)}}
.lg0{{display:grid;grid-template-columns:1fr 1fr;gap:6px 14px}}.lg0 span{{display:flex;gap:8px;align-items:center;font:600 16px/1.3 'Source Sans 3'}}.lg0 u{{text-decoration:none;width:24px;height:24px;border-radius:50%;background:{U0};color:#fff;font:800 13px/1 Poppins;display:flex;align-items:center;justify-content:center;flex:none}}
.rt0{{flex:1;background:{K0};color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:6px;min-height:0}}.rt0 .sm0{{color:#cbbda8}}
.rt0 .r{{flex:1;display:grid;grid-template-columns:86px 1fr;gap:12px;align-items:center;border-top:1px solid rgba(255,255,255,.12)}}.rt0 .r>b{{font:700 17px/1.3 Poppins;color:#f0b48f}}
.rt0 .r div b{{display:block;font:700 18px/1.3 'Source Sans 3'}}.rt0 .r div span{{font:500 15px/1.3 'Source Sans 3';color:#cbbda8}}.rt0 .r.now{{background:rgba(31,122,122,.35);border-radius:12px;padding:0 10px;border-top:0}}
.ph0wrap{{display:flex;align-items:center;justify-content:center}}
.pf0{{flex:1;display:flex;flex-direction:column;gap:14px;padding:6px 16px 16px;background:#fbf7f0}}.ph0{{font:800 19px/1.3 Poppins;color:{T0}}}
.f0{{display:flex;flex-direction:column;gap:5px}}.f0 small{{font:700 12px/1.3 'Source Sans 3';letter-spacing:1px;color:#7b6d5a;text-transform:uppercase}}.f0>b{{font:700 15px/1.3 'Source Sans 3';background:#fff;border:1.5px solid #e2d6c4;border-radius:10px;padding:8px 10px}}
.ch0{{display:flex;gap:5px}}.ch0 i{{font:600 13px/1.2 'Source Sans 3';font-style:normal;border:1.5px solid #e2d6c4;background:#fff;border-radius:9px;padding:7px 7px;white-space:nowrap}}.ch0 i.on{{background:{T0};border-color:{T0};color:#fff}}
.is0{{display:flex;gap:8px;align-items:center;font:600 15px/1.25 'Source Sans 3';background:#fff;border:1.5px solid #e2d6c4;border-radius:10px;padding:8px 9px}}.is0 u{{text-decoration:none;width:22px;height:22px;border-radius:50%;background:#e2d6c4;color:{K0};font:800 12px/1 Poppins;display:flex;align-items:center;justify-content:center;flex:none}}
.is0.on{{border-color:{U0};background:#fbe9df}}.is0.on u{{background:{U0};color:#fff}}
.pt0{{display:flex;gap:8px;align-items:center}}.pt0 i{{width:54px;height:42px;border-radius:8px;background:linear-gradient(160deg,#9fc5cc,#5b8a8f 60%,#cdb99a 60%)}}.pt0 span{{font:700 13px/1.2 'Source Sans 3';color:{T0}}}
.nt0{{font-weight:500!important;line-height:1.4!important}}.bt0{{margin-top:auto;background:{U0};color:#fff;border-radius:12px;padding:12px;text-align:center;font:800 16px/1.2 Poppins}}
""", "<div class=kk>MOBILE RV REPAIR · BOOKINGS</div><h1>RV trouble at the campsite?<br><span>Let owners book a mobile tech.</span></h1>",
f'''<div class=vw><div class=lf0><div class=rc0><span class=sm0>TRAVEL TRAILER · SAMPLE · PINS MATCH THE FORM</span><div class=rw0>{rv0()}{"".join(f'<span class=pin0 style="left:{x}%;top:{y}%">{n}</span>' for n, x, y in PINS0)}</div>
<div class=lg0>{"".join(f'<span><u>{k + 1}</u>{t}</span>' for k, t in enumerate(ISS0))}</div></div>
<div class=rt0><span class=sm0>TECH ROUTE · TUE 24 NOV · SAMPLE</span>{"".join(f'<div class="r {c}"><b>{t}</b><div><b>{w}</b><span>{i}</span></div></div>' for t, w, i, c in RT0)}</div></div>
<div class=ph0wrap>{phone(FORM0, w=372, h=850)}</div></div>''',
K0, "Fix RVs on site? DM us", f"background:{T0};color:#fff")


# ───────── 409 INDIA · Bedsheet and home furnishing maker (Panipat-style unit) · CAROUSEL 5 · Lora + Roboto · teal cotton / rose print / ivory
# New technique: CSS folded-sheet stack where each sheet wears its own CSS print (stripes, checks, dots, florets, diamonds) and a
# code tag; the same design list drives the online catalogue tiles, the design x size order matrix and the carton packing plan.
T9 = "#1f6f6b"; R9 = "#d9667a"; K9 = "#23262b"; I9 = "#f7f2e8"
DS9 = {
 "PB-101": ("Blue stripe", "repeating-linear-gradient(90deg,#3d6fb6 0 14px,#e8eef8 14px 30px)"),
 "PB-104": ("Blue check", "repeating-linear-gradient(90deg,rgba(43,84,150,.55) 0 12px,transparent 12px 26px),repeating-linear-gradient(0deg,rgba(43,84,150,.55) 0 12px,#eef3fa 12px 26px)"),
 "PB-109": ("Blue dots", "radial-gradient(circle,#2c5aa0 5px,transparent 6px) 0 0/26px 26px,#dfe9f7"),
 "PB-112": ("Navy floret", "radial-gradient(circle,#f3d9a4 4px,transparent 5px) 0 0/34px 34px,radial-gradient(circle,#f3d9a4 9px,transparent 10px) 17px 17px/34px 34px,#1f3260"),
 "PB-118": ("Rose diamond", "linear-gradient(45deg,transparent 42%,#d9667a 42% 58%,transparent 58%) 0 0/30px 30px,linear-gradient(-45deg,transparent 42%,#d9667a 42% 58%,transparent 58%) 0 0/30px 30px,#fbeef0"),
 "PB-121": ("Teal leaf", "radial-gradient(ellipse 7px 12px,#1f6f6b 80%,transparent 90%) 0 0/28px 32px,radial-gradient(ellipse 7px 12px,#7fb7a9 80%,transparent 90%) 14px 16px/28px 32px,#eaf4f1"),
}
def sheet9(code, w=380, h=86):
    return f'<div class=sh9 style="width:{w}px;height:{h}px;background:{DS9[code][1]}"><span class=fd9></span><b>{code}</b></div>'
B9 = f"""
body{{--f:'Roboto';--h:'Lora';background:{I9};color:{K9};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{R9};margin-top:22px;align-self:flex-start}}
h1{{font-family:'Lora';font-weight:700;font-size:60px;line-height:1.22;letter-spacing:-.8px;margin-top:22px}} h1 span{{color:{T9}}}
.sm9{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#7c7466}}
.cd9{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(60,40,10,.08)}}
.dk9{{background:{T9};color:#fff;border-radius:24px}}
.sh9{{position:relative;border-radius:10px 10px 14px 14px;box-shadow:0 6px 0 rgba(0,0,0,.08),0 10px 18px rgba(0,0,0,.12);overflow:hidden}}
.sh9 .fd9{{position:absolute;left:0;right:0;bottom:0;height:22px;background:linear-gradient(180deg,rgba(0,0,0,.18),rgba(0,0,0,.04))}}
.sh9 b{{position:absolute;right:12px;top:50%;transform:translateY(-50%);font:700 16px/1 Roboto;background:#fff;color:{K9};border-radius:8px;padding:7px 9px}}
"""
def t9(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{K9};color:#fff"):
    return page(B9 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, K9, cta, ctacss, tagline=f"{n} / 5")

BLUES9 = [c for c in DS9 if "Blue" in DS9[c][0]]
P["p409_sheet_s1"] = t9(1, "BEDSHEET AND HOME FURNISHING MAKER", "Buyer wants “that blue one”?<br><span>Give every design a code.</span>",
f'''<div class=w91><div class="cd9 stk91"><span class=sm9>DESIGNS IN STOCK · SAMPLE</span><div class=pile91>{"".join(sheet9(c, 400 - (k % 2) * 24, 78) for k, c in enumerate(DS9))}</div></div>
<div class=ch91><div class="cd9 bb91"><span class=sm9>BUYER'S MESSAGE</span><p class=in91>“Send 40 sets of the blue one from last time. Double size.”</p></div>
<div class="cd9 bb91"><span class=sm9>WHICH BLUE?</span><div class=bl91>{"".join(f'<div><i style="background:{DS9[c][1]}"></i><span>{c}<br><small>{DS9[c][0]}</small></span></div>' for c in BLUES9)}</div></div>
<div class="dk9 ok91"><span class=sm9>WITH A CODE</span><p>“40 sets of PB-104, double.” Done in one message.</p></div></div></div>''',
css=f""".w91{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.stk91{{padding:18px 20px;display:flex;flex-direction:column;gap:12px}}.pile91{{flex:1;display:flex;flex-direction:column;justify-content:space-evenly;align-items:center}}
.ch91{{display:flex;flex-direction:column;gap:14px}}.bb91{{padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.in91{{background:#eef6f4;border-radius:16px 16px 16px 4px;padding:14px 16px;font:500 21px/1.45 Roboto;text-wrap:pretty}}
.bl91{{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}}.bl91>div{{display:flex;flex-direction:column;gap:8px;align-items:center;text-align:center}}.bl91 i{{width:100%;height:84px;border-radius:12px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}}
.bl91 span{{font:700 17px/1.3 Roboto}}.bl91 small{{font:500 14px/1.3 Roboto;color:#7c7466}}
.ok91{{flex:1;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:10px}}.ok91 .sm9{{color:#cfe6e2}}.ok91 p{{font:600 34px/1.4 Lora;text-wrap:pretty}}""")

SZ9 = ["Single", "Double", "King"]
AV9 = {"PB-101": "SDK", "PB-104": "SDK", "PB-109": "DK", "PB-112": "DK", "PB-118": "SD", "PB-121": "SDK"}
P["p409_sheet_s2"] = t9(2, "1 · AN ONLINE CATALOGUE", "Buyers see codes and sizes.<br><span>No more photo dumps.</span>",
browser(f'''<div class=bw92><div class=fl92>{"".join(f"<i class={'on' if k == 0 else ''}>{f}</i>" for k, f in enumerate(["All designs", "Blue", "Floral", "Double", "King"]))}</div>
<div class=gd92>{"".join(f'<div class=tl92><div class=sw92 style="background:{DS9[c][1]}"></div><div class=tx92><b>{c}</b><span>{DS9[c][0]}</span><div class=sz92>{"".join(f"<u class={chr(39)}{'on' if s[0] in AV9[c] else 'no'}{chr(39)}>{s}</u>" for s in SZ9)}</div></div></div>' for c in DS9)}</div>
<div class=ft92><span>Prices are shared with each buyer directly. Sample catalogue.</span><b>Add to order</b></div></div>''', url="yourcompany.com/catalogue", style="flex:1"),
css=f""".bw92{{flex:1;display:flex;flex-direction:column;gap:14px;padding:18px 20px;background:#fbf8f2;min-height:0}}
.fl92{{display:flex;gap:8px}}.fl92 i{{font:600 15px/1.2 Roboto;font-style:normal;border:1.5px solid #e4dccd;border-radius:20px;padding:8px 14px;background:#fff}}.fl92 i.on{{background:{T9};border-color:{T9};color:#fff}}
.gd92{{flex:1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:1fr 1fr;gap:14px;min-height:0}}
.tl92{{background:#fff;border-radius:16px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 6px 16px rgba(0,0,0,.06)}}.sw92{{flex:1;min-height:0}}
.tx92{{padding:10px 12px;display:flex;flex-direction:column;gap:4px}}.tx92 b{{font:700 19px/1.3 Lora}}.tx92 span{{font:500 15px/1.3 Roboto;color:#7c7466}}
.sz92{{display:flex;gap:5px;margin-top:4px}}.sz92 u{{text-decoration:none;font:700 13px/1.2 Roboto;border-radius:8px;padding:5px 7px}}.sz92 u.on{{background:#e3f0ed;color:{T9}}}.sz92 u.no{{background:#f3f0ea;color:#b9b2a5;text-decoration:line-through}}
.ft92{{display:flex;justify-content:space-between;align-items:center;gap:12px}}.ft92 span{{font:500 15px/1.3 Roboto;color:#7c7466}}.ft92 b{{background:{R9};color:#fff;border-radius:12px;padding:12px 18px;font:700 17px/1.2 Roboto;white-space:nowrap}}""")

ORD9 = {"PB-104": {"Double": 40, "King": 20}, "PB-112": {"Double": 30}, "PB-118": {"Single": 24, "Double": 16}}
PER9 = 20
def cartons9():
    out = []
    for c, d in ORD9.items():
        for s, q in d.items():
            k = 0
            while q > 0:
                n = min(PER9, q); q -= n; k += 1; out.append((c, s, n))
    return out
CT9 = cartons9()
TOT9 = sum(sum(d.values()) for d in ORD9.values())
for _c, _d in ORD9.items():
    for _s in _d: assert _s[0] in AV9[_c], (_c, _s)
P["p409_sheet_s3"] = t9(3, "2 · ORDER BY DESIGN AND SIZE", "One clear order.<br><span>Cartons planned from it.</span>",
f'''<div class=w93><div class="cd9 mx93"><div class=hd93><span class=sm9>ORDER H-56 · SAMPLE HOME STORE · SETS</span><span class=tt93>{TOT9} sets</span></div>
<div class=mr93 style="font-weight:700"><span></span>{"".join(f"<span class=ch>{s}</span>" for s in SZ9)}<span class=ch>Total</span></div>
{"".join(f'<div class=mr93><span class=dn><i style="background:{DS9[c][1]}"></i><b>{c}</b></span>' + "".join(f"<span class='{'q' if d.get(s) else ('na' if s[0] not in AV9[c] else 'z')}'>{d.get(s, '—' if s[0] not in AV9[c] else 0)}</span>" for s in SZ9) + f'<span class=q2>{sum(d.values())}</span></div>' for c, d in ORD9.items())}</div>
<div class="cd9 cp93"><span class=sm9>CARTON PLAN · {PER9} SETS PER CARTON · {len(CT9)} CARTONS</span><div class=cg93>{"".join(f'<div class=bx93><div class=tp93></div><div class=lb93><b>C-{k + 1}</b><i style="background:{DS9[c][1]}"></i><span>{c}<br>{s} × {n}</span></div></div>' for k, (c, s, n) in enumerate(CT9))}</div></div></div>''',
css=f""".w93{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.mx93{{padding:16px 22px;display:flex;flex-direction:column;gap:2px}}
.hd93{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}.tt93{{font:700 17px/1.2 Roboto;background:{T9};color:#fff;border-radius:10px;padding:8px 12px}}
.mr93{{display:grid;grid-template-columns:1.6fr repeat(4,1fr);gap:10px;align-items:center;border-top:1px solid #eee7da;height:62px}}.mr93 .ch{{font:700 15px/1.2 Roboto;color:#7c7466;text-align:center}}
.mr93 .dn{{display:flex;gap:12px;align-items:center}}.mr93 .dn i{{width:46px;height:38px;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}}.mr93 .dn b{{font:700 20px/1.3 Lora}}
.mr93>span{{text-align:center;font:700 20px/1.3 Roboto}}.mr93 .z{{color:#c9c1b2}}.mr93 .na{{color:#c9c1b2;font-weight:500}}.mr93 .q{{background:#e3f0ed;color:{T9};border-radius:10px;padding:6px 0}}.mr93 .q2{{color:{R9}}}
.cp93{{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:12px;min-height:0}}.cg93{{flex:1;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}}
.bx93{{background:#c99a62;border-radius:8px;position:relative;display:flex;flex-direction:column;overflow:hidden;box-shadow:inset 0 -10px 0 rgba(0,0,0,.08)}}.tp93{{height:16px;background:linear-gradient(90deg,transparent 44%,#e3c48f 44% 56%,transparent 56%),#b98a52}}
.lb93{{margin:auto 12px 14px;background:#fff;border-radius:10px;padding:12px;display:grid;grid-template-columns:auto 1fr;gap:4px 8px;align-items:center}}.lb93 b{{font:700 22px/1.2 Lora;grid-column:1/3}}
.lb93 i{{width:46px;height:46px;border-radius:6px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}}.lb93 span{{font:600 17px/1.35 Roboto;color:#4b4f55}}""")

TL9 = [("Order confirmed", "Mon 23 Nov", "dn"), ("Stitched and packed", "Thu 26 Nov", "nw"), ("Loaded · LR no. shared", "Fri 27 Nov", ""), ("Delivered", "Mon 30 Nov", "")]
P["p409_sheet_s4"] = t9(4, "3 · DISPATCH WITH UPDATES", "“Has my order left?”<br><span>The buyer can see it.</span>",
f'''<div class=w94><div class="cd9 tl94"><span class=sm9>ORDER H-56 · {TOT9} SETS · {len(CT9)} CARTONS · SAMPLE</span>{"".join(f'<div class="r {k}"><i></i><div><b>{a}</b><span>{d}</span></div></div>' for a, d, k in TL9)}</div>
<div class=rt94><div class="dk9 ms94"><span class=sm9>MESSAGE TO BUYER · THU 26 NOV</span><p>Order H-56: all {len(CT9)} cartons are packed. Loading tomorrow. The transport receipt number will come in the next message.</p><div class=dt94>{''.join(f'<div><span>{x}</span><b>{y}</b></div>' for x, y in [('Cartons', str(len(CT9))), ('Loading', 'Fri 27 Nov'), ('Delivery plan', 'Mon 30 Nov')])}</div></div>
<div class="cd9 ck94"><span class=sm9>PACKED TODAY</span><div class=cb94>{"".join(f'<div><i style="background:{DS9[c][1]}"></i><b>C-{k + 1}</b></div>' for k, (c, s, n) in enumerate(CT9))}</div></div></div></div>''',
css=f""".w94{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.tl94{{padding:20px 24px;display:flex;flex-direction:column;gap:4px}}.tl94 .r{{flex:1;display:flex;gap:16px;align-items:center;position:relative}}
.tl94 .r i{{width:28px;height:28px;border-radius:50%;border:4px solid #d9d1c2;background:#fff;flex:none;z-index:1}}.tl94 .r.dn i{{background:{T9};border-color:{T9}}}.tl94 .r.nw i{{background:{R9};border-color:{R9}}}
.tl94 .r:not(:last-child)::after{{content:"";position:absolute;left:12px;top:calc(50% + 14px);height:calc(100% - 28px);width:4px;background:#e6dfd2}}
.tl94 b{{display:block;font:700 28px/1.3 Lora}}.tl94 .r span{{font:500 20px/1.3 Roboto;color:#7c7466}}
.rt94{{display:flex;flex-direction:column;gap:16px}}.ms94{{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:12px}}.ms94 .sm9{{color:#cfe6e2}}.dt94{{margin-top:auto;background:rgba(255,255,255,.12);border-radius:16px;padding:8px 16px;display:flex;flex-direction:column}}.dt94>div{{display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid rgba(255,255,255,.14)}}.dt94>div:first-child{{border-top:0}}.dt94 span{{font:500 18px/1.3 Roboto;color:#cfe6e2}}.dt94 b{{font:700 19px/1.3 Roboto}}.ms94 p{{font:500 29px/1.5 Roboto;text-wrap:pretty}}
.ck94{{padding:16px 20px;display:flex;flex-direction:column;gap:12px}}.cb94{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.cb94>div{{background:#f6f1e7;border-radius:12px;padding:10px;display:flex;flex-direction:column;align-items:center;gap:6px}}
.cb94 i{{width:100%;height:60px;border-radius:8px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.08)}}.cb94 b{{font:700 15px/1.2 Roboto}}""")

P["p409_sheet_s5"] = t9(5, "HOME FURNISHING ORDER APP", "Make bedsheets or cushions?<br><span>Let's build your order app.</span>",
f'''<div class=w95><div class=tl95>{"".join(f'<div class=cd9><span class=ib>{ic(i, 36)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("tag", "Design codes", "One code per print"), ("globe", "Online catalogue", "Sizes for each design"), ("box", "Carton plans", "Made from the order"), ("truck", "Dispatch updates", "Buyers can see them")])}</div>
<div class="dk9 q95"><span class=sm9>A QUESTION FOR MAKERS</span><p>How do buyers pick designs today: photos on chat, printed books or samples? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{R9};color:#fff",
css=f""".w95{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl95{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl95>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl95 .ib{{width:80px;height:80px;border-radius:22px;background:{T9};color:#fff}}.tl95 b{{font:700 36px/1.3 Lora}}.tl95 span{{font:500 22px/1.4 Roboto;color:#7c7466}}
.q95{{padding:26px 30px;display:flex;flex-direction:column;gap:12px}}.q95 .sm9{{color:#cfe6e2}}.q95 p{{font:600 30px/1.45 Lora;text-wrap:pretty}}""")



if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
