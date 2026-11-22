import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 221 INDIA · Bulk vegetable supplier to hotels · SINGLE · Archivo Black + Source Sans 3 · tomato red / leaf green / crate wood
# New technique: digital weighing scale with a 7-segment-style LCD readout as the hero, order lines checked against weight.
lines221 = [("Onion", "40 kg", "40.0 kg", "ok"), ("Tomato", "25 kg", "25.2 kg", "ok"), ("Potato", "30 kg", "30.0 kg", "ok"), ("Coriander", "3 kg", "2.0 kg", "sh"), ("Green chilli", "4 kg", "4.1 kg", "ok"), ("Capsicum", "8 kg", "—", "na")]
P["p221_veg"] = page("""
body{--f:'Source Sans 3';--h:'Archivo Black';background:#f4efe4;color:#2a2018}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#d2402d;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.22} h1 span{color:#2f7a3a}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.sc{width:400px;flex:none;display:flex;flex-direction:column;gap:12px}
.scale{flex:1;background:#c9ccd1;border-radius:28px;padding:18px;display:flex;flex-direction:column;gap:12px;box-shadow:inset 0 -10px 0 rgba(0,0,0,.12)}
.plat{flex:1;background:linear-gradient(#e9ebee,#cfd3d8);border-radius:18px;border:3px solid #9aa0a8;display:flex;align-items:center;justify-content:center;padding:14px}
.crate{width:340px;height:240px;background:repeating-linear-gradient(90deg,#b98a52 0 40px,#a67843 40px 46px);border:5px solid #7b5530;border-radius:8px;position:relative;display:flex;align-items:flex-start;justify-content:center;gap:4px;padding-top:0}
.crate i{width:74px;height:74px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#ff7a62,#d2402d 60%,#9e2a1c);margin-top:-30px;border:3px solid #7a2014}
.crate b{position:absolute;bottom:10px;left:50%;transform:translateX(-50%);background:#fff;border-radius:8px;padding:4px 12px;font:700 18px 'Source Sans 3';white-space:nowrap}
.lcd{background:#1d2a22;border-radius:16px;padding:12px 18px;display:flex;justify-content:space-between;align-items:center}
.lcd small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7fa58c}
.lcd b{font:700 54px/1.3 'DejaVu Sans Mono',monospace;color:#9dff9a;letter-spacing:2px;text-shadow:0 0 12px rgba(157,255,154,.5)}
.ord{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(42,32,24,.08)}
.oh{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:10px;border-bottom:2px solid #efe7d8}
.oh small{display:block;font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#857766}.oh b{font:400 26px/1.3 'Archivo Black'}
.cols{display:grid;grid-template-columns:1fr 80px 92px 34px;gap:8px;font:700 13px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#857766;padding:8px 0 4px}
.ln{flex:1;display:grid;grid-template-columns:1fr 80px 92px 34px;gap:8px;align-items:center;border-bottom:1px solid #f3ece0;font:600 21px 'Source Sans 3'}.ln:last-child{border:0}
.ln b{font:700 22px 'Source Sans 3'}.ln em{font-style:normal;color:#5d5347}
.ln i{width:32px;height:32px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff}
.ok i{background:#2f7a3a}.sh i{background:#d2402d}.na i{background:#c9b99f}
.sh em,.sh b{color:#d2402d}
.nt{background:#2a2018;color:#fff;border-radius:22px;padding:14px 20px;font:500 20px/1.4 'Source Sans 3'}.nt b{color:#ffb4a6}
""", "<div class=kk>VEGETABLE SUPPLY TO HOTELS · DAILY ORDERS</div><h1>Hotel order on a voice note?<br><span>Weigh it against the list.</span></h1>",
f'''<div class=vw><div class=sc><div class=scale><div class=plat><div class=crate><i class=free></i><i class=free></i><i class=free></i><i class=free></i><b>Tomato · crate 2</b></div></div>
<div class=lcd><small>WEIGHT</small><b>25.2 kg</b></div></div>
<div class=nt>Short items go on tomorrow's sheet: <b>coriander 1 kg</b>, <b>capsicum 8 kg</b>.</div></div>
<div class=ord><div class=oh><div><small>SAMPLE HOTEL · TUE 24 NOV · 6 AM</small><b>Order O-221</b></div></div>
<div class=cols><span>ITEM</span><span>ASKED</span><span>WEIGHED</span><span></span></div>
{"".join(f'<div class="ln {k}"><b>{a}</b><em>{q}</em><span>{w}</span><i>{ic("check",18,w=3) if k=="ok" else ("!" if k=="sh" else "–")}</i></div>' for a,q,w,k in lines221)}</div></div>''',
"#2a2018", "Supply hotels? DM us", "background:#2f7a3a;color:#fff")

# ───────── 222 INDIA · Kitchen chimney cleaning · SINGLE · Poppins + Fira Sans · brushed steel / ink blue / lime · PHONE
# New technique: drawn chimney hood front with baffle filter grid where each filter cell shows grease level; phone booking with AMC visit count.
grease = [0.9, 0.8, 0.95, 0.7, 0.85, 0.6]
P["p222_chimney"] = page("""
body{--f:'Fira Sans';--h:'Poppins';background:#e6e9ec;color:#1b2a4a}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#5b8f00;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#1b2a4a;background:linear-gradient(transparent 60%,#c6f04a 60%)}
.vw{flex:1;display:flex;gap:18px;min-height:0;align-items:stretch}
.lf{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.hood{flex:1;min-height:0;background:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:10px}.hood .lgd{font-size:19px}
.hood>small{align-self:flex-start;font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#6b7891}
.hw{width:100%;display:flex;flex-direction:column;align-items:center}.duct{width:150px;height:90px;background:linear-gradient(90deg,#aab3bd,#e3e7eb,#aab3bd);border:3px solid #1b2a4a;border-bottom:0}
.hd{width:100%;background:linear-gradient(#dde2e7,#b9c1ca);border:3px solid #1b2a4a;border-radius:8px 8px 18px 18px;clip-path:polygon(16% 0,84% 0,100% 100%,0 100%);padding:28px 40px 18px}
.fg{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.fc{height:118px;border:3px solid #1b2a4a;border-radius:6px;background:repeating-linear-gradient(135deg,#8d969f 0 6px,#c3c9d0 6px 12px);position:relative;overflow:hidden}
.fc i{position:absolute;left:0;right:0;bottom:0;background:rgba(122,74,20,.78)}
.lgd{display:flex;gap:18px;font:600 17px 'Fira Sans';color:#4a5770}.lgd span{display:flex;align-items:center;gap:8px}.lgd i{width:18px;height:18px;border-radius:4px;background:rgba(122,74,20,.78)}
.vs{background:#1b2a4a;color:#fff;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;gap:6px}
.vs small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#c6f04a}
.dots{display:flex;gap:8px;align-items:center;font:600 18px 'Fira Sans'}.dots i{width:34px;height:34px;border-radius:50%;border:3px solid #c6f04a;display:flex;align-items:center;justify-content:center;color:#1b2a4a}.dots i.d{background:#c6f04a}.dots em{font-style:normal;margin-left:8px;color:#d7deea}
.ap{flex:1;padding:8px 18px 18px;display:flex;flex-direction:column;gap:11px}
.ap h4{font:700 22px/1.3 Poppins}.ap small{font:700 12px/1.4 'Fira Sans';letter-spacing:1.5px;color:#6b7891}
.rw{border:2px solid #e1e5ea;border-radius:12px;padding:9px 12px;font:600 15px 'Fira Sans';display:flex;justify-content:space-between}.rw em{font-style:normal;color:#5b8f00}
.ch{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ch span{text-align:center;border:2px solid #e1e5ea;border-radius:10px;padding:8px 0;font:600 15px 'Fira Sans'}.ch .on{background:#1b2a4a;border-color:#1b2a4a;color:#fff}.ch .x{color:#b3bac6;text-decoration:line-through}
.bt{margin-top:auto;background:#c6f04a;color:#1b2a4a;border-radius:12px;padding:13px;text-align:center;font:700 16px Poppins}
""", "<div class=kk>CHIMNEY CLEANING · AMC VISITS</div><h1>Chimney service<br>booked on calls?<br><span>Let them pick a slot.</span></h1>",
f'''<div class=vw><div class=lf><div class=hood><small>FILTERS AT LAST VISIT · SAMPLE HOME</small><div class=hw><div class=duct></div><div class=hd><div class=fg>{"".join(f'<div class=fc><i style="height:{g*100:.0f}%"></i></div>' for g in grease)}</div></div></div>
<div class=lgd><span><i></i>Oil and grease found</span><span>6 of 6 filters cleaned</span></div></div>
<div class=vs><small>AMC · 3 VISITS A YEAR · SAMPLE</small><div class=dots><i class=d>{ic("check",16,w=3)}</i><i class=d>{ic("check",16,w=3)}</i><i></i><em>Visit 3 due in March</em></div></div></div>
{phone(f"""<div class=ap><h4>Book chimney cleaning</h4><small>SAMPLE BOOKING PAGE</small>
<div class=rw><span>Chimney type</span><b>Wall, 90 cm</b></div><div class=rw><span>Filters</span><b>Baffle</b></div><div class=rw><span>AMC</span><em>Visit 3 of 3</em></div>
<div class=ch><span class=x>Sat 10 AM</span><span class=on>Sat 2 PM</span><span>Sun 11 AM</span><span>Sun 4 PM</span></div>
<div class=rw><span>Before photos</span><b>Yes</b></div><div class=rw><span>After photos</span><b>Yes</b></div><div class=rw><span>Address</span><b>Sample home</b></div><div class=bt>Confirm Sat 2 PM</div></div>""", w=340, h=720)}</div>''',
"#1b2a4a", "Clean chimneys? DM us", "background:#1b2a4a;color:#fff")

# ───────── 223 USA · Dog daycare · SINGLE · TeX Gyre Adventor + Roboto · grass green / sunny yellow / charcoal
# New technique: top-down play yard plan split into fenced group zones with dog dots (paw markers) = live capacity per group.
random.seed(223)
zones = [("Small dogs", 8, 10, 40, 40, 350, 300), ("Medium dogs", 12, 12, 410, 40, 450, 300), ("Large dogs", 6, 8, 40, 360, 820, 220)]
yard = '<svg viewBox="0 0 900 620" class=yd><rect width="900" height="620" rx="30" fill="#7cbf5a"/>'
for name, n, cap, x, y, w, h in zones:
    yard += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="18" fill="#94d06f" stroke="#2b2b2b" stroke-width="5" stroke-dasharray="14 8"/>'
    cols = math.ceil(cap / 2) if w < 500 else 10
    for i in range(cap):
        cx = x + 50 + (i % cols) * ((w - 100) / (cols - 1)); cy = y + h / 2 if cap <= cols else y + 95 + (i // cols) * 110
        if cap > cols: cy = y + 90 + (i // cols) * 110
        on = i < n
        yard += f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="25" fill="{"#ffd23f" if on else "none"}" stroke="#2b2b2b" stroke-width="4" {"" if on else "stroke-dasharray=\"6 6\""}/>'
        if on:
            yard += f'<g fill="#2b2b2b"><ellipse cx="{cx:.0f}" cy="{cy+6:.0f}" rx="10" ry="8"/><circle cx="{cx-11:.0f}" cy="{cy-6:.0f}" r="4.5"/><circle cx="{cx-4:.0f}" cy="{cy-12:.0f}" r="4.5"/><circle cx="{cx+4:.0f}" cy="{cy-12:.0f}" r="4.5"/><circle cx="{cx+11:.0f}" cy="{cy-6:.0f}" r="4.5"/></g>'
yard += '<rect x="420" y="596" width="60" height="24" fill="#c98a4b"/></svg>'
P["p223_daycare"] = page("""
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#fdf6d8;color:#2b2b2b}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#3f8a2a;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#3f8a2a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ydw{flex:1;min-height:0;background:#fff;border-radius:28px;padding:14px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(43,43,43,.08)}
.ydw>small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6c6c5e}
.yd{width:100%;flex:1;min-height:0;display:block}
.gz{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.gz div{background:#fff;border-radius:20px;padding:14px 18px;border-top:8px solid #ffd23f}
.gz small{display:block;font:700 14px/1.4 'Roboto';letter-spacing:1.5px;color:#6c6c5e}.gz b{display:block;font:700 34px/1.3 'TeX Gyre Adventor'}.gz span{font:600 17px 'Roboto';color:#3f8a2a}
.gz .fu{border-top-color:#2b2b2b}.gz .fu span{color:#c0392b}
.nt{display:flex;gap:14px;align-items:center;background:#2b2b2b;color:#fff;border-radius:20px;padding:14px 20px;font:500 20px/1.4 'Roboto'}.nt .ib{width:50px;height:50px;border-radius:14px;background:#ffd23f;color:#2b2b2b}
""", "<div class=kk>DOG DAYCARE · TODAY'S PLAY GROUPS</div><h1>“Do you have room today?”<br><span>Show live spots by group.</span></h1>",
f'''<div class=vw><div class=ydw><small>PLAY YARD · TODAY · SAMPLE</small>{yard}</div>
<div class=gz><div><small>SMALL DOGS</small><b>8 of 10</b><span>2 spots open</span></div><div class=fu><small>MEDIUM DOGS</small><b>12 of 12</b><span>Full, waitlist on</span></div><div><small>LARGE DOGS</small><b>6 of 8</b><span>2 spots open</span></div></div>
<div class=nt><span class=ib>{ic("cal",26)}</span><span>Owners book a spot online. When a group is full, the app offers the waitlist.</span></div></div>''',
"#2b2b2b", "Run a dog daycare? DM us", "background:#3f8a2a;color:#fff")

# ───────── 224 INDIA · Terrace garden setup service · CAROUSEL 5 · Crimson Text + Inter · sage white / basil green / sunset coral
# New techniques: top-down terrace plan with sun-hour shading and planter boxes to scale, plant list cards with drawn leaves, visit calendar with photo report.
TB = """
body{--f:'Inter';--h:'Crimson Text';background:#eef2ea;color:#1f3a2a}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#e0684b;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:68px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#3d7a45}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(31,58,42,.07)}
"""
def tb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f3a2a;color:#fff"):
    return page(TB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f3a2a", cta, ctacss, tagline=f"{n} / 5")
# terrace 30 ft x 20 ft, scale 26 px/ft -> 780 x 520
def terrace(boxes=True, sun=True, big=False):
    s = '<svg viewBox="-20 -40 840 620" class=tr><rect x="0" y="0" width="780" height="520" fill="#e9e4d8" stroke="#1f3a2a" stroke-width="6"/>'
    s += "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="520" stroke="#d8d1c0" stroke-width="2"/>' for x in range(52, 780, 52))
    s += "".join(f'<line x1="0" y1="{y}" x2="780" y2="{y}" stroke="#d8d1c0" stroke-width="2"/>' for y in range(52, 520, 52))
    if sun:
        s += '<rect x="0" y="0" width="780" height="156" fill="#f6c26b" fill-opacity=".45"/><rect x="0" y="156" width="390" height="364" fill="#f6c26b" fill-opacity=".25"/><rect x="390" y="156" width="390" height="364" fill="#8fb3c9" fill-opacity=".3"/>'
    s += '<rect x="560" y="330" width="220" height="190" fill="#c9c2b2" stroke="#1f3a2a" stroke-width="4"/><text x="670" y="432" text-anchor="middle" font-family="Inter" font-weight="700" font-size="22" fill="#1f3a2a"><tspan>Water tank</tspan></text>'
    s += '<rect x="0" y="420" width="104" height="100" fill="#fff" stroke="#1f3a2a" stroke-width="4"/><text x="52" y="476" text-anchor="middle" font-family="Inter" font-weight="700" font-size="20" fill="#1f3a2a"><tspan>Stairs</tspan></text>'
    if boxes:
        for i, (x, y, w, h, c, t) in enumerate([(26, 26, 312, 78, "#3d7a45", "A"), (364, 26, 390, 78, "#3d7a45", "B"), (26, 182, 78, 208, "#7fb069", "C"), (182, 260, 156, 156, "#e0684b", "D")]):
            s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}" stroke="#1f3a2a" stroke-width="4"/><circle cx="{x+w/2}" cy="{y+h/2}" r="22" fill="#fff"/><text x="{x+w/2}" y="{y+h/2+8}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#1f3a2a"><tspan>{t}</tspan></text>'
    s += '<g font-family="Inter" font-weight="700" font-size="22" fill="#e0684b"><text x="390" y="-12" text-anchor="middle"><tspan>30 ft</tspan></text><text x="800" y="270" text-anchor="middle" transform="rotate(90 800 270)"><tspan>20 ft</tspan></text></g></svg>'
    return s
P["p224_terrace_s1"] = tb(1, "TERRACE GARDEN SETUP · ENQUIRIES", "“How much for<br>my terrace?”<br><span>Measure it first.</span>",
f'''<div class=w1><div class="cd pl">{terrace(False, False)}<div class=qs>{"".join(f'<span>{q}</span>' for q in ["Size?","Sun or shade?","Tank space?","Weight on roof?"])}</div></div>
<div class=nb><span class=ib>{ic("chat",26)}</span><span>Every enquiry starts with a photo of an empty terrace and the same 4 unknowns.</span></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pl{flex:1;min-height:0;padding:20px;display:flex;flex-direction:column;gap:14px;align-items:center}
.tr{width:100%;flex:1;min-height:0;display:block}.qs{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;width:100%}.qs span{background:#fde8e1;color:#b5432a;border-radius:14px;padding:12px 0;text-align:center;font:700 21px Inter}
.nb{display:flex;align-items:center;gap:14px;background:#1f3a2a;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Inter}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e0684b}""")

P["p224_terrace_s2"] = tb(2, "PART 1 · SITE VISIT ON A TABLET", "Sun, shade and size,<br><span>marked on the plan.</span>",
f'''<div class=w2><div class="cd pl2">{terrace(True, True)}</div>
<div class=lg2><div><i style="background:#f6c26b"></i><b>6+ hours sun</b><span>Vegetables</span></div><div><i style="background:#f8dfb0"></i><b>3 to 6 hours</b><span>Herbs, flowers</span></div><div><i style="background:#c7d8e2"></i><b>Shade</b><span>Leafy plants</span></div><div class=sz2><b>600 sq ft</b><span>30 x 20 ft · sample</span></div></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pl2{flex:1;min-height:0;padding:20px;display:flex}.pl2 .tr{width:100%;height:100%;display:block}
.lg2{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.lg2 div{background:#fff;border-radius:18px;padding:12px 16px;display:flex;flex-direction:column;gap:2px}.lg2 i{width:28px;height:14px;border-radius:4px;margin-bottom:4px;border:1px solid #c9c2b2}
.lg2 b{font:700 22px/1.3 'Crimson Text'}.lg2 span{font:500 16px Inter;color:#5a6b5f}.lg2 .sz2{background:#1f3a2a;color:#fff}.lg2 .sz2 span{color:#c9dccc}.lg2 .sz2 b{font-size:28px}""")

def leaf(c):
    return f'<svg viewBox="0 0 60 60" width="96" height="96"><path d="M30 54 C10 40 8 18 30 6 C52 18 50 40 30 54 Z" fill="{c}" stroke="#1f3a2a" stroke-width="3"/><path d="M30 50 V14" stroke="#1f3a2a" stroke-width="2.5"/></svg>'
plants = [("A", "Tomato, chilli, brinjal", "Box A · 12 x 3 ft", "Full sun", "#3d7a45"), ("B", "Okra, beans, gourd climber", "Box B · 15 x 3 ft", "Full sun", "#3d7a45"), ("C", "Mint, coriander, basil", "Box C · 3 x 8 ft", "Part sun", "#7fb069"), ("D", "Spinach, lettuce, fenugreek", "Box D · 6 x 6 ft", "Part sun", "#e0684b")]
P["p224_terrace_s3"] = tb(3, "PART 2 · PLAN AND QUOTE", "Planter boxes,<br><span>plants and materials.</span>",
f'''<div class=w3><div class=pg3>{"".join(f'<div class="cd pc"><div class=lt style="background:{c}">{t}</div><div class=tx><b>{a}</b><span>{b}</span></div><div class=lf3>{leaf(c)}</div><em>{d}</em></div>' for t,a,b,d,c in plants)}</div>
<div class=ml><div><small>MATERIALS · SAMPLE</small><b>4 planter boxes</b></div><div><small>SOIL MIX</small><b>Worked out by box size</b></div><div class=dr><small>DRIP LINE</small><b>Tank to all 4 boxes</b></div></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pg3{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px}
.pc{padding:18px 20px;display:grid;grid-template-columns:auto 1fr auto;grid-template-rows:1fr auto;gap:10px 14px;align-items:center}
.lt{width:60px;height:60px;border-radius:16px;color:#fff;display:flex;align-items:center;justify-content:center;font:800 28px Inter}
.tx b{display:block;font:700 30px/1.25 'Crimson Text'}.tx span{font:500 19px Inter;color:#5a6b5f}
.pc em{grid-column:span 3;justify-self:start;font-style:normal;font:700 16px Inter;background:#eef2ea;border-radius:10px;padding:6px 12px}
.ml{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.ml div{background:#1f3a2a;color:#fff;border-radius:20px;padding:14px 18px}.ml small{display:block;font:700 13px/1.4 Inter;letter-spacing:1.5px;color:#c9dccc}.ml b{font:700 24px/1.3 'Crimson Text'}
.ml .dr{background:#e0684b}.ml .dr small{color:#ffe0d6}""")

visits = {3: "d", 17: "d", 31: "n"}
P["p224_terrace_s4"] = tb(4, "PART 3 · CARE VISITS", "Every visit planned,<br><span>with a photo report.</span>",
f'''<div class=w4><div class="cd cal"><div class=ch4><b>December · sample</b><span><i class=d></i>Done <i class=n></i>Next</span></div><div class=dw>{"".join(f"<span>{d}</span>" for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])}</div>
<div class=gd>{"".join('<div></div>' for _ in range(1))}{"".join(f'<div class="dc {visits.get(d,"")}">{d}</div>' for d in range(1,32))}</div></div>
<div class=rp><div class="cd ph"><small>VISIT REPORT · 17 DEC · SAMPLE</small><div class=pp>{"".join(f'<div style="background:linear-gradient(135deg,{a},{b})"><span>{t}</span></div>' for a,b,t in [("#7fb069","#3d7a45","Box A"),("#9cc77f","#5d9a55","Box C"),("#e9a08b","#e0684b","Box D")])}</div>
<p>Pruned tomato, added compost to Box D, drip line checked.</p></div><div class=nx><small>NEXT VISIT</small><b>Thu 31 Dec</b><span>Reminder sent to the owner</span></div></div></div>''',
css=""".w4{flex:1;display:flex;gap:14px;min-height:0}.cal{width:470px;flex:none;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.ch4{display:flex;justify-content:space-between;align-items:center}.ch4 b{font:700 28px/1.3 'Crimson Text'}.ch4 span{display:flex;gap:6px;align-items:center;font:600 15px Inter}.ch4 i{width:14px;height:14px;border-radius:4px;margin-left:6px}
.d{background:#3d7a45}.n{background:#e0684b}
.dw{display:grid;grid-template-columns:repeat(7,1fr);font:700 14px Inter;color:#5a6b5f;text-align:center}
.gd{flex:1;display:grid;grid-template-columns:repeat(7,1fr);grid-auto-rows:1fr;gap:6px}
.dc{border-radius:10px;background:#f2f5ef;display:flex;align-items:center;justify-content:center;font:600 18px Inter}.dc.d{background:#3d7a45;color:#fff}.dc.n{background:#e0684b;color:#fff;box-shadow:0 0 0 4px rgba(224,104,75,.25)}
.rp{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}.ph{flex:1;padding:16px 18px;display:flex;flex-direction:column;gap:12px}
.ph small,.nx small{font:700 14px/1.4 Inter;letter-spacing:1.5px;color:#5a6b5f}.pp{flex:1;display:grid;grid-template-columns:1fr;gap:8px}.pp div{border-radius:14px;display:flex;align-items:flex-end;padding:10px}.pp span{background:rgba(255,255,255,.9);border-radius:8px;padding:3px 10px;font:700 15px Inter}
.ph p{font:500 19px/1.45 Inter}.nx{background:#e0684b;color:#fff;border-radius:22px;padding:16px 20px}.nx small{color:#ffe0d6}.nx b{display:block;font:700 32px/1.3 'Crimson Text'}.nx span{font:500 17px Inter}""")

P["p224_terrace_s5"] = tb(5, "YOUR TURN", "Set up terrace gardens?<br><span>Let's build your site app.</span>",
f'''<div class=w5><div class="cd pl5">{terrace(True, False)}</div><div class=t5>{"".join(f'<div><span class=ib>{ic(i,32)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("map","Site plan","Size, sun and tank"),("leaf","Plant list","Box by box"),("doc","Quote","From the plan"),("cal","Care visits","With photo reports")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#e0684b;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pl5{flex:1;min-height:0;padding:16px;display:flex}.pl5 .tr{width:100%;height:100%;display:block}
.t5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.t5 div{background:#1f3a2a;color:#fff;border-radius:22px;padding:14px 18px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:14px;align-content:center}
.t5 div:nth-child(2),.t5 div:nth-child(3){background:#3d7a45}.t5 .ib{grid-row:span 2;width:64px;height:64px;border-radius:16px;background:rgba(255,255,255,.14)}.t5 b{font:700 30px/1.3 'Crimson Text'}.t5 small{font:400 18px/1.35 Inter;color:#dbe8dc}""")

# ───────── 225 INDIA · Sewing machine repair (home visits) · SINGLE · Bitter + Open Sans · mint / cherry red / black
# New technique: side-view sewing machine SVG with numbered problem hotspots chosen by the customer → visit card with parts used.
mach = '''<svg viewBox="0 0 520 380" class=mc><rect x="20" y="320" width="480" height="40" rx="10" fill="#2a2a2a"/>
<path d="M60 320 V120 Q60 70 110 70 H420 Q460 70 460 110 V160 H400 V130 H130 V320 Z" fill="#9fdcc8" stroke="#1d1d1d" stroke-width="6" stroke-linejoin="round"/>
<rect x="390" y="150" width="80" height="70" rx="10" fill="#9fdcc8" stroke="#1d1d1d" stroke-width="6"/>
<rect x="418" y="220" width="10" height="58" fill="#1d1d1d"/><path d="M423 278 L423 300" stroke="#9aa" stroke-width="4"/>
<rect x="380" y="296" width="100" height="24" rx="4" fill="#cfd6d6" stroke="#1d1d1d" stroke-width="4"/>
<circle cx="110" cy="150" r="46" fill="#e9f7f1" stroke="#1d1d1d" stroke-width="6"/><circle cx="110" cy="150" r="10" fill="#1d1d1d"/>
<rect x="250" y="40" width="22" height="34" rx="4" fill="#d43d51" stroke="#1d1d1d" stroke-width="4"/><path d="M261 40 V20" stroke="#1d1d1d" stroke-width="4"/>
<path d="M261 74 Q300 110 423 222" stroke="#d43d51" stroke-width="3" fill="none" stroke-dasharray="6 5"/>
<rect x="160" y="200" width="200" height="60" rx="10" fill="#e9f7f1" stroke="#1d1d1d" stroke-width="4"/><circle cx="200" cy="230" r="14" fill="#1d1d1d"/><rect x="230" y="220" width="100" height="20" rx="10" fill="#1d1d1d"/>'''
for n, (x, y) in enumerate([(423, 258), (110, 150), (261, 30)], 1):
    mach += f'<circle cx="{x}" cy="{y}" r="24" fill="#d43d51" stroke="#fff" stroke-width="5"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Open Sans" font-weight="800" font-size="22" fill="#fff"><tspan>{n}</tspan></text>'
mach += '</svg>'
probs = [("1", "Needle breaks", "Picked by customer"), ("2", "Wheel feels stuck", "Picked by customer"), ("3", "Thread keeps cutting", "Picked by customer")]
parts = [("Needle set", "Replaced"), ("Belt", "Replaced"), ("Tension spring", "Adjusted")]
P["p225_sewing"] = page("""
body{--f:'Open Sans';--h:'Bitter';background:#dff3ec;color:#1d1d1d}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#d43d51;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.2} h1 span{color:#d43d51}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp{flex:1;min-height:0;display:grid;grid-template-columns:1.25fr 1fr;gap:14px}
.mw{background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.mw>small,.pb small,.vc small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#5f6f6a}
.mc{width:100%;flex:1;min-height:0;display:block}
.pb{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}
.pr{flex:1;display:flex;gap:12px;align-items:center;border-top:1px solid #edf3f0}
.pr i{font-style:normal;width:40px;height:40px;border-radius:50%;background:#d43d51;color:#fff;display:flex;align-items:center;justify-content:center;font:800 19px 'Open Sans';flex:none}
.pr b{display:block;font:700 23px/1.3 Bitter}.pr span{font:500 16px 'Open Sans';color:#5f6f6a}
.vc{background:#1d1d1d;color:#fff;border-radius:26px;padding:16px 22px;display:grid;grid-template-columns:1fr 1.3fr;gap:18px}
.vc small{color:#9fdcc8}.vc b{display:block;font:700 30px/1.3 Bitter}.vc span{font:500 17px 'Open Sans';color:#c7d4d0}
.pt{display:flex;flex-direction:column;gap:8px}.pt p{display:flex;justify-content:space-between;border-bottom:1px solid #3a3a3a;padding-bottom:6px;font:500 19px 'Open Sans'}.pt em{font-style:normal;color:#9fdcc8;font-weight:700}
""", "<div class=kk>SEWING MACHINE REPAIR · HOME VISITS</div><h1>“Machine not working”<br>is all you hear?<br><span>Let them point to it.</span></h1>",
f'''<div class=vw><div class=tp><div class=mw><small>BOOKING PAGE · TAP THE PROBLEM · SAMPLE</small>{mach}</div>
<div class=pb><small>PROBLEMS PICKED</small>{"".join(f'<div class=pr><i>{n}</i><div><b>{a}</b><span>{b}</span></div></div>' for n,a,b in probs)}</div></div>
<div class=vc><div><small>VISIT V-225 · SAMPLE HOME</small><b>Wed 25 Nov, 11 AM</b><span>Mechanic carries needles, belt and springs.</span></div>
<div class=pt><small>PARTS USED · LOGGED ON SITE</small>{"".join(f'<p><span>{a}</span><em>{b}</em></p>' for a,b in parts)}</div></div></div>''',
"#1d1d1d", "Repair machines? DM us", "background:#d43d51;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
