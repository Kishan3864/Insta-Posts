
# ───────── 448 INDIA · Industrial gas cylinder supplier (welding gases) · CAROUSEL 5 · Archivo Black + Fira Sans · steel grey / valve brass / maroon
# New technique: one cylinder list (40 IDs) drives every slide: SVG cylinders coloured by gas grouped by where they are,
# days-held bars with a 60-day line, and a refill truck loaded with the exact empties.
INK8 = "#1e2730"; BR8 = "#c9962e"; BG8 = "#e3e7eb"; MU8 = "#5f6a74"; RED8 = "#d2452f"
GAS8 = {"Oxygen": "#26323d", "Argon": "#2f8f8a", "CO2": "#8f99a3", "Acetylene": "#8e2b3a"}
LOC8 = [("Yard · full", None), ("Yard · empty", None), ("Sample Fabricator A", 6), ("Sample Workshop B", 5), ("Sample Garage C", 4), ("Sample Factory D", 5)]
rnd8 = random.Random(448)
GASSEQ8 = ["Oxygen"] * 16 + ["Argon"] * 8 + ["CO2"] * 8 + ["Acetylene"] * 8
rnd8.shuffle(GASSEQ8)
CYL8 = []
cnt = {"Yard · full": 12, "Yard · empty": 8, "Sample Fabricator A": 6, "Sample Workshop B": 5, "Sample Garage C": 4, "Sample Factory D": 5}
i8 = 0
DAYS8 = {"Sample Fabricator A": [12, 19, 25, 33, 8, 41], "Sample Workshop B": [5, 0, 22, 37, 14], "Sample Garage C": [29, 45, 52, 18], "Sample Factory D": [91, 74, 68, 40, 26]}
for loc, n in cnt.items():
    for k in range(n):
        d = DAYS8[loc][k] if loc in DAYS8 else None
        CYL8.append(dict(id=f"C-{101 + i8}", gas=GASSEQ8[i8], loc=loc, days=d)); i8 += 1
OVER8 = [c for c in CYL8 if c["days"] and c["days"] > 60]
FULL8 = [c for c in CYL8 if c["loc"] == "Yard · full"]; EMPTY8 = [c for c in CYL8 if c["loc"] == "Yard · empty"]
AT8 = [c for c in CYL8 if c["days"] is not None]
SCAN8 = [c for c in CYL8 if c["loc"] == "Sample Workshop B" and c["days"] == 0][0]
def cyl8(gas, w=30, empty=False, over=False):
    col = GAS8[gas]
    body = f'<rect x="3" y="22" width="34" height="86" rx="12" fill="{"#fff" if empty else col}" stroke="{col}" stroke-width="{4 if empty else 0}" {"stroke-dasharray=\"6 4\"" if empty else ""}/>'
    return f'''<svg viewBox="0 0 40 112" style="width:{w}px;height:auto;display:block;flex:none{";filter:drop-shadow(0 0 0 #000)" if over else ""}"><rect x="13" y="2" width="14" height="10" rx="3" fill="{BR8}"/><path d="M9 22 Q9 12 20 12 Q31 12 31 22 Z" fill="{"#fff" if empty else col}" stroke="{col}" stroke-width="{3 if empty else 0}"/>{body}{f'<rect x="3" y="52" width="34" height="8" fill="{RED8}"/>' if over else ""}</svg>'''
def pl8(n, w): return f"{n} {w if n == 1 else w + 's'}"
B8 = f"""
body{{--f:'Fira Sans';--h:'Archivo Black';background:{BG8};color:{INK8}}}
.kk8{{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:{MU8};margin-top:22px;display:flex;gap:10px;align-items:center}}.kk8 i{{width:14px;height:24px;border-radius:5px 5px 3px 3px;background:{BR8}}}
h1{{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.25;letter-spacing:-.5px;margin-top:16px}} h1 span{{color:{RED8}}}
.sm8{{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:{MU8}}}
.cd8{{background:#fff;border-radius:20px;box-shadow:0 14px 30px rgba(30,39,48,.08)}}
.dk8{{background:{INK8};color:#fff;border-radius:20px}}.dk8 .sm8{{color:#a8b3bd}}
.lgd8{{display:flex;gap:16px;flex-wrap:wrap}}.lgd8 span{{display:flex;align-items:center;gap:7px;font:600 16px/1.3 'Fira Sans'}}.lgd8 i{{width:16px;height:16px;border-radius:4px}}
"""
LG8 = '<div class=lgd8>' + "".join(f'<span><i style="background:{c}"></i>{g}</span>' for g, c in GAS8.items()) + f'<span><i style="background:{RED8}"></i>Over 60 days</span></div>'
def t8(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{INK8};color:#fff"):
    return page(B8 + css, f"<div class=kk8><i></i>{kick}</div><h1>{head}</h1>", vis, INK8, cta, ctacss, tagline=f"{n} / 5")

def zone8(loc):
    cs = [c for c in CYL8 if c["loc"] == loc]
    return f'''<div class="cd8 zn{" dz" if loc.startswith("Yard") else ""}"><div class=hd><b>{loc}</b><strong>{len(cs)}</strong></div><div class=cy{' style="grid-template-columns:repeat(4,auto)"' if loc == "Yard · empty" else ""}>{"".join(cyl8(c["gas"], 32 if loc.startswith("Yard") else 38, loc == "Yard · empty", bool(c["days"] and c["days"] > 60)) for c in cs)}</div></div>'''
QS8 = [("“Who has my argon cylinder?”", "Call five customers"), ("“How many empties to send?”", "Walk the yard and count"), ("“That one is out for months.”", "Nobody knows which")]
P["p448_gas_s1"] = t8(1, "INDUSTRIAL GAS CYLINDERS · SUPPLIER", f"Where are my {len(CYL8)} cylinders?<br><span>Every cylinder, every customer.</span>",
f'''<div class=w81><div class=zs>{"".join(zone8(l) for l, _ in LOC8)}</div>{LG8}<div class=qs>{"".join(f'<div class="cd8 q"><p>{a}</p><em>{b}</em></div>' for a, b in QS8)}</div></div>''',
css=f""".w81{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.zs{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px;min-height:0}}
.zn{{padding:14px 16px;display:flex;flex-direction:column;gap:10px}}.zn.dz{{background:#f4f1e8}}.zn .hd{{display:flex;justify-content:space-between;align-items:baseline;gap:8px}}.zn .hd b{{font:700 17px/1.3 'Fira Sans'}}.zn .hd strong{{font:400 34px/1.4 'Archivo Black';color:{BR8}}}
.zn .cy{{flex:1;display:flex;flex-wrap:wrap;gap:10px 10px;align-content:center;justify-content:center}}
.zn.dz .cy{{display:grid;grid-template-columns:repeat(6,auto);gap:12px 8px}}.zn:not(.dz) .cy{{flex-wrap:nowrap;gap:6px}}.qs{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.qs .q{{padding:16px 18px;display:flex;flex-direction:column;gap:10px;justify-content:space-between}}.qs p{{font:700 21px/1.35 'Fira Sans'}}.qs em{{align-self:flex-start;font:700 15px/1.3 'Fira Sans';font-style:normal;background:{BG8};border-radius:8px;padding:6px 10px;color:{MU8}}}""")

REG8 = [c for c in CYL8 if c["loc"] == "Sample Factory D"][:3] + [SCAN8] + FULL8[:3] + EMPTY8[:2] + [c for c in CYL8 if c["loc"] == "Sample Garage C"][:1]
P["p448_gas_s2"] = t8(2, "1 · CYLINDER REGISTER", "Scan at the gate,<br><span>the register fills itself.</span>",
f'''<div class=w82><div class="cd8 tb"><div class="r h"><span>NO.</span><span>GAS</span><span>WHERE</span><span>DAYS</span></div>{"".join(f'<div class="r{" ov" if c["days"] and c["days"] > 60 else ""}"><b>{c["id"]}</b><span><i style="background:{GAS8[c["gas"]]}"></i>{c["gas"]}</span><span>{c["loc"].replace("Sample ", "")}</span><strong>{"—" if c["days"] is None else c["days"]}</strong></div>' for c in REG8)}</div>
<div class=sd><div class="dk8 sc"><span class=sm8>GATE SCAN · MON 23 NOV · 10:20 AM</span><div class=row>{cyl8(SCAN8["gas"], 54)}<div><b>{SCAN8["id"]} · {SCAN8["gas"]}</b><p>Out to Sample Workshop B. Full, sealed.</p></div></div></div>
<div class="cd8 tt"><span class=sm8>ALL {len(CYL8)} CYLINDERS · SAMPLE</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("In the yard, full", len(FULL8)), ("In the yard, empty", len(EMPTY8)), ("With customers", len(AT8)), ("Over 60 days", len(OVER8))])}</div>
<div class="cd8 gb"><span class=sm8>BY GAS</span><div class=bar>{"".join(f'<i style="flex:{GASSEQ8.count(g)};background:{c}"></i>' for g, c in GAS8.items())}</div><div class=gl>{"".join(f'<span><b>{GASSEQ8.count(g)}</b> {g}</span>' for g in GAS8)}</div></div></div></div>''',
css=f""".w82{{flex:1;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:16px;min-height:0}}
.tb{{padding:14px 18px;display:flex;flex-direction:column}}.tb .r{{flex:1;display:grid;grid-template-columns:70px 120px 1fr 54px;gap:8px;align-items:center;border-top:1px solid #eceff2;padding:0 6px}}.tb .h{{flex:none;border:0;padding-bottom:8px}}.tb .h span{{font:700 13px/1.4 'Fira Sans';letter-spacing:1px;color:{MU8}}}
.tb .r b{{font:700 18px/1.3 'Fira Sans'}}.tb .r span{{font:500 18px/1.3 'Fira Sans';display:flex;align-items:center;gap:7px}}.tb .r span i{{width:14px;height:14px;border-radius:4px;flex:none}}.tb .r strong{{font:700 19px/1.3 'Fira Sans';text-align:right}}.tb .r.ov{{background:#fbe4df;border-radius:10px}}.tb .r.ov strong{{color:{RED8}}}
.sd{{display:flex;flex-direction:column;gap:14px}}.sc{{padding:16px 18px;display:flex;flex-direction:column;gap:10px}}.sc .row{{display:flex;gap:14px;align-items:center}}.sc b{{font:700 23px/1.3 'Fira Sans';color:{BR8}}}.sc p{{font:500 20px/1.45 'Fira Sans';margin-top:4px}}
.tt{{flex:1;padding:14px 18px;display:flex;flex-direction:column;gap:2px;justify-content:space-between}}.tt .r{{display:flex;justify-content:space-between;border-top:1px solid #eceff2;padding:7px 0;font:500 21px/1.35 'Fira Sans'}}.tt .r b{{font:700 24px/1.35 'Fira Sans'}}.tt .r:last-child b{{color:{RED8}}}
.gb{{padding:14px 18px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.gb .bar{{display:flex;height:30px;border-radius:8px;overflow:hidden;gap:2px}}.gb .gl{{display:grid;grid-template-columns:1fr 1fr;gap:4px 10px}}.gb .gl span{{font:500 16px/1.35 'Fira Sans'}}.gb .gl b{{font-weight:700}}""")

CUS8 = [l for l, n in LOC8 if n]
MSG8 = [c for c in OVER8]
P["p448_gas_s3"] = t8(3, "2 · WHO HOLDS WHAT", "Days held, per cylinder.<br><span>Old ones show up in red.</span>",
f'''<div class=w83><div class="cd8 hl">{"".join(f"""<div class=cu><div class=hd><b>{cu}</b><span>{pl8(len([c for c in AT8 if c["loc"] == cu]), "cylinder")}</span></div>{"".join(f'<div class=br><em>{c["id"]}</em><div class=tr><i style="width:{min(c["days"], 100)}%;background:{RED8 if c["days"] > 60 else GAS8[c["gas"]]}"></i><u></u></div><strong class="{"ov" if c["days"] > 60 else ""}">{c["days"]} d</strong></div>' for c in sorted([c for c in AT8 if c["loc"] == cu], key=lambda c: -c["days"]))}</div>""" for cu in CUS8)}
<div class=ax><span>0</span><span class=l60>60 days</span><span>100</span></div></div>
<div class=sd><div class="dk8 ms"><span class=sm8>REMINDER · SAMPLE FACTORY D</span><div class=bb>{len(MSG8)} cylinders are with you for over 60 days: {", ".join(f'{c["id"]} ({c["days"]} days)' for c in MSG8)}. Please send back the empty ones on our Tuesday round.<small>Your message · Mon 23 Nov</small></div><div class="bb cu2">Two are empty, we will send them on Tuesday. We still use {MSG8[2]["id"]}.<small>Sample Factory D · 11:40 AM</small></div><div class=bb>Noted, {MSG8[2]["id"]} stays with you. Pickup Tue 24 Nov.<small>Your message · 11:45 AM</small></div></div>
<div class="cd8 nt"><span class=sm8>THE RULE YOU SET</span><p>Over <b>60 days</b> with a customer: red on the board and a reminder on the next round.</p></div></div></div>''',
css=f""".w83{{flex:1;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:16px;min-height:0}}
.hl{{padding:14px 18px;display:flex;flex-direction:column;gap:8px}}.cu{{flex:1;display:flex;flex-direction:column;gap:3px}}.cu .hd{{display:flex;justify-content:space-between;font:700 18px/1.3 'Fira Sans'}}.cu .hd span{{color:{MU8};font-weight:600}}
.br{{flex:1;display:grid;grid-template-columns:58px 1fr 50px;gap:8px;align-items:center}}.br em{{font:600 15px/1.2 'Fira Sans';font-style:normal;color:{MU8}}}.br .tr{{height:13px;background:#eef1f4;border-radius:6px;position:relative}}.br .tr i{{position:absolute;left:0;top:0;bottom:0;border-radius:6px}}.br .tr u{{position:absolute;left:60%;top:0;bottom:0;width:2px;background:{RED8}}}.br strong{{font:700 16px/1.2 'Fira Sans';text-align:right}}.br strong.ov{{color:{RED8}}}
.ax{{display:grid;grid-template-columns:60px 1fr 54px;font:600 13px/1.3 'Fira Sans';color:{MU8};position:relative;height:18px}}.ax span:first-child{{position:absolute;left:60px}}.ax .l60{{position:absolute;left:calc(60px + (100% - 114px) * .6);transform:translateX(-50%);color:{RED8}}}.ax span:last-child{{position:absolute;right:54px;transform:translateX(50%)}}
.sd{{display:flex;flex-direction:column;gap:14px}}.ms{{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.bb.cu2{{background:#4a5866;border-radius:16px 16px 4px 16px;margin-left:24px}}.bb{{background:#33414f;border-radius:16px 16px 16px 4px;padding:14px 16px;font:500 18px/1.45 'Fira Sans';display:flex;flex-direction:column;gap:8px}}.bb small{{font:500 14px/1.3 'Fira Sans';color:#a8b3bd}}
.nt{{padding:18px 20px;display:flex;flex-direction:column;gap:8px}}.nt p{{font:500 20px/1.45 'Fira Sans'}}.nt b{{color:{RED8}}}""")

ORD8 = [("Sample Fabricator A", "Oxygen", 3, "Wed 25 Nov"), ("Sample Workshop B", "Argon", 2, "Thu 26 Nov"), ("Sample Garage C", "CO2", 2, "Thu 26 Nov"), ("Sample Factory D", "Acetylene", 2, "Fri 27 Nov")]
NEED8 = sum(o[2] for o in ORD8)
AFTER8 = len(FULL8) + len(EMPTY8)
for o in ORD8: assert sum(1 for c in FULL8 + EMPTY8 if c["gas"] == o[1]) >= o[2], o
def truck8():
    cyls = "".join(f'<g transform="translate({150 + i * 44},{38})"><rect x="0" y="16" width="34" height="96" rx="12" fill="#fff" stroke="{GAS8[c["gas"]]}" stroke-width="4" stroke-dasharray="6 4"/><rect x="10" y="4" width="14" height="12" rx="3" fill="{BR8}"/></g>' for i, c in enumerate(EMPTY8))
    return f'''<svg viewBox="0 0 560 210" style="display:block;width:100%;height:auto"><rect x="130" y="140" width="380" height="18" fill="{INK8}"/><rect x="130" y="30" width="6" height="110" fill="{INK8}"/><rect x="504" y="30" width="6" height="110" fill="{INK8}"/>{cyls}
<path d="M20 158 V92 Q20 76 36 76 H96 L126 112 V158 Z" fill="{BR8}"/><rect x="36" y="88" width="50" height="26" rx="4" fill="#cfe0ea"/><circle cx="66" cy="168" r="22" fill="{INK8}"/><circle cx="66" cy="168" r="9" fill="#9aa4ad"/><circle cx="400" cy="168" r="22" fill="{INK8}"/><circle cx="400" cy="168" r="9" fill="#9aa4ad"/><circle cx="460" cy="168" r="22" fill="{INK8}"/><circle cx="460" cy="168" r="9" fill="#9aa4ad"/></svg>'''
P["p448_gas_s4"] = t8(4, "3 · REFILL ROUND", "Send the right empties,<br><span>fill this week's orders.</span>",
f'''<div class=w84><div class="cd8 tk"><span class=sm8>TUE 24 NOV · 9 AM · TO THE REFILL PLANT · {len(EMPTY8)} EMPTIES</span>{truck8()}<div class=ids>{"".join(f'<span><i style="background:{GAS8[c["gas"]]}"></i>{c["id"]}</span>' for c in EMPTY8)}</div></div>
<div class=bt><div class="cd8 od"><span class=sm8>ORDERS THIS WEEK · SAMPLE</span>{"".join(f'<div class=r><div><b>{a}</b><span>{d}</span></div><em><i style="background:{GAS8[g]}"></i>{n} {g}</em></div>' for a, g, n, d in ORD8)}</div>
<div class=tl>{"".join(f'<div class="{"dk8" if k == 2 else "cd8"} t"><span class=sm8>{a}</span><b>{b}</b></div>' for k, (a, b) in enumerate([("FULL IN THE YARD NOW", len(FULL8)), ("NEEDED FOR ORDERS", NEED8), ("FULL ON WED, AFTER REFILL", AFTER8)]))}</div></div></div>''',
css=f""".w84{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tk{{padding:16px 20px;display:flex;flex-direction:column;gap:10px}}.tk svg{{max-height:300px}}.tk .ids{{display:flex;flex-wrap:wrap;gap:8px}}.tk .ids span{{display:flex;align-items:center;gap:6px;font:700 16px/1.3 'Fira Sans';background:{BG8};border-radius:8px;padding:5px 10px}}.tk .ids i{{width:12px;height:12px;border-radius:3px}}
.bt{{flex:1;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:16px;min-height:0}}.od{{padding:16px 20px;display:flex;flex-direction:column}}.od .r{{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #eceff2}}.od .r b{{display:block;font:700 21px/1.3 'Fira Sans'}}.od .r span{{font:500 18px/1.3 'Fira Sans';color:{MU8}}}.od em{{display:flex;align-items:center;gap:8px;font:700 20px/1.3 'Fira Sans';font-style:normal}}.od em i{{width:14px;height:14px;border-radius:4px}}
.tl{{display:flex;flex-direction:column;gap:14px}}.tl .t{{flex:1;padding:14px 18px;display:flex;flex-direction:column;justify-content:center}}.tl .t b{{font:400 46px/1.4 'Archivo Black';color:{BR8}}}""")

P["p448_gas_s5"] = t8(5, "CYLINDER TRACKING APP", "Supply gas cylinders?<br><span>Let's build your app.</span>",
f'''<div class=w85><div class=tl>{"".join(f'<div class=cd8><span class=ib>{ic(i, 40)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("qr", "Gate scan", "In and out, by code"), ("users", "Who holds what", "Days held, per cylinder"), ("bell", "Old cylinder alert", "Red after 60 days"), ("truck", "Refill round", "Right empties, right day")])}</div>
<div class="dk8 q"><span class=sm8>A QUESTION FOR GAS SUPPLIERS</span><p>How many of your cylinders are with customers right now? Do you know without calling? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{BR8};color:{INK8}",
css=f""".w85{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.w85 .tl{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.w85 .tl>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.w85 .ib{{width:86px;height:86px;border-radius:22px;background:{INK8};color:{BR8}}}.w85 .tl b{{font:400 32px/1.4 'Archivo Black'}}.w85 .tl>div>span:last-child{{font:500 22px/1.4 'Fira Sans';color:{MU8}}}
.q{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q p{{font:700 28px/1.4 'Fira Sans';text-wrap:pretty}}""")
