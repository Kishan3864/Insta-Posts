
# ───────── 428 USA · Home inspection company · CAROUSEL 6 · Anton + Inter · slate blue / clipboard tan / flag red
# New technique: SVG house cross-section (roof, attic, two floors, basement, deck) with numbered finding pins from one
# findings list that also drives a CSS tablet checklist, photo cards, a report summary page and the counts.
SL8 = "#34506b"; TN8 = "#e8dcc4"; RD8 = "#d1495b"; BG8 = "#f3f1ec"; INK8 = "#1e2a36"; MU8 = "#66727e"; GN8 = "#3c8d6e"; AM8 = "#d99a2b"
TY8 = {"Safety": RD8, "Repair": AM8, "Monitor": SL8}
FD8 = [(1, "Roof", "Flashing gap at the chimney", "Repair", 410, 112), (2, "Attic", "Thin insulation over the hall", "Monitor", 220, 118),
       (3, "Bathroom", "Slow drain in the tub", "Repair", 384, 236), (4, "Kitchen", "Water stain under the sink", "Repair", 176, 366),
       (5, "Laundry", "Missing outlet cover", "Safety", 452, 352), (6, "Deck", "Loose deck railing", "Safety", 566, 352),
       (7, "Basement", "Hairline crack in a wall", "Monitor", 150, 462)]
CNT8 = {t: sum(1 for f in FD8 if f[3] == t) for t in TY8}
AR8 = [("Roof", 6), ("Attic", 4), ("Bathroom", 5), ("Kitchen", 7), ("Laundry", 3), ("Electrical panel", 4), ("Deck", 5), ("Basement", 6)]
def house8(pins=True):
    g = f'''<rect x="0" y="400" width="620" height="120" fill="#d9cdb4"/><rect x="0" y="392" width="620" height="10" fill="#7fae6e"/>
<path d="M56 144 L300 40 L544 144 Z" fill="#8a5a44"/><path d="M84 144 L300 58 L516 144 Z" fill="#efe6d2"/>
<rect x="396" y="56" width="34" height="80" fill="#9a6f58"/><rect x="390" y="50" width="46" height="10" fill="#6b4a3a"/>
<rect x="100" y="132" width="400" height="12" fill="#f4d89a" opacity=".9"/><rect x="180" y="126" width="80" height="18" fill="#f4d89a" opacity=".5"/>
<rect x="84" y="144" width="432" height="256" fill="#fbf9f4" stroke="{INK8}" stroke-width="6"/><path d="M84 268 H516" stroke="{INK8}" stroke-width="6"/><path d="M300 150 V262 M300 274 V396" stroke="{INK8}" stroke-width="3"/>
<rect x="84" y="400" width="432" height="104" fill="#e9e2d2" stroke="{INK8}" stroke-width="6"/>
<rect x="330" y="214" width="120" height="40" rx="18" fill="#cfe0ea" stroke="{INK8}" stroke-width="2"/><rect x="120" y="340" width="120" height="56" fill="#d8cbb0" stroke="{INK8}" stroke-width="2"/><rect x="150" y="330" width="60" height="12" fill="#9aa8b3"/>
<rect x="420" y="330" width="60" height="66" fill="#c9d3da" stroke="{INK8}" stroke-width="2"/><circle cx="450" cy="362" r="18" fill="#fff" stroke="{INK8}" stroke-width="2"/>
<rect x="516" y="372" width="88" height="10" fill="#8a5a44"/><path d="M524 372 V330 M548 372 V330 M572 372 V330 M596 372 V330 M520 330 H600" stroke="#8a5a44" stroke-width="5"/>
<path d="M140 430 l10 14 l-6 10 l12 16 l-4 12" stroke="{INK8}" stroke-width="2" fill="none"/>
<rect x="110" y="190" width="70" height="50" fill="#cfe0ea" stroke="{INK8}" stroke-width="2"/><rect x="410" y="290" width="56" height="30" fill="#cfe0ea" stroke="{INK8}" stroke-width="2"/>'''
    if pins:
        g += "".join(f'<circle cx="{x}" cy="{y}" r="17" fill="{TY8[t]}" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y + 7}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="19" fill="#fff"><tspan>{n}</tspan></text>' for n, a, d, t, x, y in FD8)
    return f'<svg viewBox="0 30 620 482" style="display:block;width:100%;height:auto">{g}</svg>'
B8 = f"""
body{{--f:'Inter';--h:'Anton';background:{BG8};color:{INK8}}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{RD8};margin-top:22px}}
h1{{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.2;letter-spacing:.3px;margin-top:14px;text-transform:uppercase}} h1 span{{color:{SL8}}}
.sm8{{font:700 13px/1.4 Inter;letter-spacing:2px;color:{MU8}}}
.cd8{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(30,42,54,.08)}}
.dk8{{background:{SL8};color:#fff;border-radius:22px}}.dk8 .sm8{{color:#bccbd9}}
.ty8{{font:700 14px/1.2 Inter;font-style:normal;color:#fff;border-radius:9px;padding:7px 10px;text-align:center;white-space:nowrap}}
.pn8.pn8.pn8{{display:inline-flex;align-items:center;justify-content:center;width:34px;height:34px;border-radius:50%;color:#fff!important;font:800 17px/1 Inter!important;flex:none;text-align:center!important}}
"""
def t8(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{SL8};color:#fff"):
    return page(B8 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, INK8, cta, ctacss, tagline=f"{n} / 6")
ty8 = lambda t: f'<em class=ty8 style="background:{TY8[t]}">{t}</em>'
pn8 = lambda n, t: f'<span class=pn8 style="background:{TY8[t]}">{n}</span>'

NOTE8 = ["roof - chimney ??", "attic thin? hall", "tub slow - check", "stain undr sink", "<s>laundry</s> outlet cvr", "deck rail LOOSE", "bsmt crack - photo?"]
P["p428_insp_s1"] = t8(1, "HOME INSPECTORS · USA AND CANADA", "Notes on a clipboard?<br><span>Send the report on site.</span>",
f'''<div class=w81><div class=tp81><div class=cb81><i class=clip></i><div class=pa><span class=sm8>SAMPLE HOME · TUE 24 NOV</span>{"".join(f'<p>{x}</p>' for x in NOTE8)}</div></div>
<div class="cd8 hs81"><span class=sm8>THE SAME 7 FINDINGS, PINNED ON THE HOUSE · SAMPLE</span>{house8()}<div class=lg>{"".join(f'<div><i style="background:{c}"></i>{t}</div>' for t, c in TY8.items())}</div></div></div>
<div class="dk8 bt81"><b>Clipboard:</b><span>type it all up at night, send it tomorrow.</span><b class=y>App:</b><span>the report is ready before you leave.</span></div></div>''',
css=f""".w81{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tp81{{flex:1;display:grid;grid-template-columns:minmax(0,.62fr) minmax(0,1.38fr);gap:16px;min-height:0}}
.cb81{{background:#b98a5e;border-radius:18px;padding:34px 14px 14px;position:relative;display:flex}}.cb81 .clip{{position:absolute;top:10px;left:50%;transform:translateX(-50%);width:110px;height:34px;border-radius:10px;background:linear-gradient(#c9ced3,#8e959c)}}
.cb81 .pa{{flex:1;background:#fffdf7 repeating-linear-gradient(transparent 0 55px,#d6e2ea 55px 57px);border-radius:6px;padding:16px 16px;display:flex;flex-direction:column;justify-content:space-around}}.cb81 p{{font:italic 500 23px/1.3 'Inter';color:#3c4a57;transform:rotate(-1deg)}}.cb81 s{{color:{RD8}}}
.hs81{{padding:18px 20px;display:flex;flex-direction:column;justify-content:space-between;gap:10px}}.hs81 .lg{{display:flex;gap:20px}}.hs81 .lg div{{display:flex;align-items:center;gap:8px;font:600 17px/1.3 Inter}}.hs81 .lg i{{width:20px;height:20px;border-radius:50%}}
.bt81{{padding:18px 24px;display:grid;grid-template-columns:auto 1fr;gap:4px 14px;align-items:baseline}}.bt81 b{{font:400 30px/1.3 Anton;letter-spacing:.5px;color:#f0c9cf}}.bt81 b.y{{color:#bfe7d6}}.bt81 span{{font:600 23px/1.35 Inter}}""")

P["p428_insp_s2"] = t8(2, "1 · AREA BY AREA", "Check it off<br><span>room by room.</span>",
f'''<div class=tb82><div class=sc><div class=hd><b>Sample Home · ZIP 12345</b><span>Tue 24 Nov · 9:00 AM · 1,850 sq ft · built 1998</span></div>
<div class=gr>{"".join(f"""<div class=r><b>{a}</b><span>{c} items checked</span><div class=fs>{"".join(pn8(f[0], f[3]) for f in FD8 if f[1] == a) or '<em class=ok>All OK</em>'}</div><u>{ic("camera", 20)} {sum(2 for f in FD8 if f[1] == a) + 1}</u></div>""" for a, c in AR8)}</div>
<div class=ft><span>{sum(c for _, c in AR8)} items checked · {len(FD8)} findings · photos saved to each finding</span><b>Next: findings</b></div></div></div>''',
css=f""".tb82{{flex:1;background:#1c2229;border-radius:40px;padding:22px;box-shadow:0 30px 60px rgba(30,42,54,.25);display:flex}}
.tb82 .sc{{flex:1;background:#fff;border-radius:22px;padding:22px 26px;display:flex;flex-direction:column;gap:10px}}.tb82 .hd{{display:flex;flex-direction:column;gap:2px;border-bottom:3px solid {INK8};padding-bottom:12px}}.tb82 .hd b{{font:400 34px/1.25 Anton;letter-spacing:.3px}}.tb82 .hd span{{font:500 18px/1.4 Inter;color:{MU8}}}
.tb82 .gr{{flex:1;display:flex;flex-direction:column}}.tb82 .r{{flex:1;display:grid;grid-template-columns:200px 170px 1fr 70px;gap:12px;align-items:center;border-bottom:1px solid #e7e4dc}}.tb82 .r b{{font:700 21px/1.3 Inter}}.tb82 .r>span{{font:500 17px/1.3 Inter;color:{MU8}}}.tb82 .fs{{display:flex;gap:8px}}
.tb82 em.ok{{font:700 15px/1.2 Inter;font-style:normal;background:#dcefe6;color:{GN8};border-radius:9px;padding:7px 12px}}.tb82 u{{text-decoration:none;display:flex;align-items:center;gap:6px;font:700 17px/1 Inter;color:{MU8};justify-content:flex-end}}
.tb82 .ft{{display:flex;justify-content:space-between;align-items:center;gap:12px;background:#f1efe9;border-radius:14px;padding:12px 16px}}.tb82 .ft span{{font:600 16px/1.35 Inter}}.tb82 .ft b{{font:700 16px/1.2 Inter;background:{SL8};color:#fff;border-radius:10px;padding:9px 14px;white-space:nowrap}}""")

def ph8(kind):
    if kind == 6:
        art = f'<rect width="300" height="170" fill="#9cc0d8"/><rect y="120" width="300" height="50" fill="#b08a62"/>' + "".join(f'<rect x="{30 + i * 60}" y="40" width="10" height="80" fill="#7a5a3c" transform="rotate({8 if i == 2 else 0} {35 + i * 60} 120)"/>' for i in range(5)) + '<rect x="20" y="34" width="260" height="12" fill="#7a5a3c" transform="rotate(3 150 40)"/>'
    elif kind == 5:
        art = '<rect width="300" height="170" fill="#e8e1d2"/><rect x="110" y="40" width="80" height="96" rx="6" fill="#f7f5ef" stroke="#9aa3ab" stroke-width="3"/><rect x="132" y="62" width="12" height="22" rx="3" fill="#2a2f35"/><rect x="156" y="62" width="12" height="22" rx="3" fill="#2a2f35"/><circle cx="150" cy="108" r="7" fill="#2a2f35"/>'
    else:
        art = '<rect width="300" height="170" fill="#efe7d6"/><rect x="40" y="30" width="220" height="110" fill="#d9c9a9"/><ellipse cx="160" cy="98" rx="56" ry="30" fill="#a07c4a" opacity=".55"/><ellipse cx="150" cy="94" rx="30" ry="16" fill="#7d5c33" opacity=".5"/><rect x="60" y="20" width="16" height="60" fill="#9aa3ab"/>'
    return f'<svg viewBox="0 0 300 170" style="display:block;width:100%;height:100%" preserveAspectRatio="xMidYMid slice">{art}</svg>'
SEL8 = [FD8[5], FD8[4], FD8[3]]
P["p428_insp_s3"] = t8(3, "2 · FINDINGS WITH PHOTOS", "Every finding gets<br><span>a photo and a label.</span>",
f'''<div class=w83>{"".join(f"""<div class="cd8 fc"><div class=im>{ph8(f[0])}<span class=pin>{pn8(f[0], f[3])}</span></div><div class=tx><div class=tp><span class=sm8>{f[1].upper()}</span>{ty8(f[3])}</div><b>{f[2]}</b><p>{n}</p></div></div>""" for f, n in zip(SEL8, ["Railing moves when pushed. Have a deck builder fix the posts.", "No cover plate on the outlet by the dryer. Fit a cover.", "Dry stain on the cabinet floor. Watch the drain pipe joint."]))}
<div class="dk8 sm83">{"".join(f'<div><b>{CNT8[t]}</b><span>{t}</span></div>' for t in TY8)}<div><b>{len(FD8)}</b><span>Findings in all</span></div></div></div>''',
css=f""".w83{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.w83 .fc{{flex:1;display:grid;grid-template-columns:300px 1fr;gap:20px;padding:14px;min-height:0}}
.w83 .im{{position:relative;border-radius:14px;overflow:hidden}}.w83 .im .pin{{position:absolute;left:10px;top:10px;display:flex}}
.w83 .tx{{display:flex;flex-direction:column;justify-content:center;gap:8px;padding-right:10px}}.w83 .tp{{display:flex;justify-content:space-between;align-items:center}}.w83 .tx b{{font:800 27px/1.3 Inter}}.w83 .tx p{{font:500 19px/1.45 Inter;color:{MU8}}}
.sm83{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;padding:16px 22px}}.sm83 div{{display:flex;align-items:baseline;gap:10px}}.sm83 b{{font:400 40px/1.2 Anton}}.sm83 span{{font:600 18px/1.3 Inter;color:#dfe7ef}}""")

P["p428_insp_s4"] = t8(4, "3 · THE REPORT", "The report is done<br><span>before you drive off.</span>",
f'''<div class=w84><div class=dc><div class=hd><div><span class=sm8>HOME INSPECTION REPORT · SAMPLE</span><b>Sample Home · ZIP 12345</b><small>Tue 24 Nov 2026 · Inspector: Your Name</small></div><div class=mini>{house8()}</div></div>
<div class=sm>{"".join(f'<div style="border-color:{c}"><b style="color:{c}">{CNT8[t]}</b><span>{t}</span></div>' for t, c in TY8.items())}</div>
<div class=ls>{"".join(f'<div class=r>{pn8(n, t)}<b>{d}</b><span>{a}</span><span>Page {i + 3}</span></div>' for i, (n, a, d, t, x, y) in enumerate(FD8))}</div></div>
<div class=sd><div class="dk8 sn"><span class=sm8>SENT · TUE 24 NOV · 12:40 PM</span>{"".join(f'<div class=r>{ic("send", 22)}<span>{a}</span><b>{b}</b></div>' for a, b in [("Buyer", "Report + photos"), ("Agent", "Report + photos")])}</div>
<div class="cd8 nx"><span class=sm8>BUILT IN</span>{"".join(f'<p>{ic("check", 22, GN8, 3)}{x}</p>' for x in ["Photos sit next to each finding", "Same layout for every home", "Old reports easy to find"])}</div></div></div>''',
css=f""".w84{{flex:1;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:16px;min-height:0}}
.w84 .dc{{background:#fff;border-radius:6px;box-shadow:0 20px 40px rgba(30,42,54,.14);padding:26px 26px;display:flex;flex-direction:column;gap:14px;border-top:10px solid {SL8}}}
.w84 .dc .hd{{display:flex;justify-content:space-between;gap:12px;align-items:center}}.w84 .dc .hd b{{display:block;font:400 30px/1.3 Anton;letter-spacing:.3px;margin-top:4px}}.w84 .dc .hd small{{display:block;margin-top:6px;font:500 15px/1.4 Inter;color:{MU8}}}.w84 .mini{{width:150px;flex:none}}
.w84 .dc .sm{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.w84 .dc .sm div{{border:3px solid;border-radius:14px;padding:8px 12px;display:flex;align-items:baseline;gap:8px}}.w84 .dc .sm b{{font:400 36px/1.2 Anton}}.w84 .dc .sm span{{font:700 16px/1.3 Inter}}
.w84 .ls{{flex:1;display:flex;flex-direction:column}}.w84 .ls .r{{flex:1;display:grid;grid-template-columns:34px 1fr 92px 64px;gap:10px;align-items:center;border-bottom:1px solid #ebe8e0}}.w84 .ls .r b{{font:700 17px/1.3 Inter}}.w84 .ls .r span{{font:500 15px/1.3 Inter;color:{MU8}}}.w84 .ls .r span:last-child{{text-align:right}}
.w84 .sd{{display:flex;flex-direction:column;gap:16px}}.w84 .sn{{padding:20px;display:flex;flex-direction:column;gap:10px}}.w84 .sn .r{{display:grid;grid-template-columns:24px 1fr;gap:4px 10px;align-items:center;background:rgba(255,255,255,.1);border-radius:14px;padding:12px 14px}}.w84 .sn .r span{{font:700 20px/1.3 Inter}}.w84 .sn .r b{{grid-column:2;font:500 16px/1.3 Inter;color:#dfe7ef}}
.w84 .nx{{flex:1;padding:20px;display:flex;flex-direction:column;justify-content:space-around;gap:10px}}.w84 .nx p{{display:flex;gap:10px;align-items:flex-start;font:700 23px/1.4 Inter}}.w84 .nx svg{{flex:none;margin-top:2px}}""")

DY8 = [("Mon", 23), ("Tue", 24), ("Wed", 25), ("Thu", 26), ("Fri", 27), ("Sat", 28)]
BK8 = {"Mon": [(9, "12345"), (13, "12350")], "Tue": [(9, "12345"), (13, "12347")], "Wed": [(10, "12352")],
       "Thu": [(9, "12346"), (13, "12346")], "Fri": [(11, "12349")], "Sat": []}
P["p428_insp_s5"] = t8(5, "4 · BOOKING", "Buyers book online.<br><span>You see the whole week.</span>",
f'''<div class=w85><div class="cd8 wk"><span class=sm8>THIS WEEK · BY ZIP CODE · SAMPLE</span><div class=gd><div class=ax>{"".join(f'<span style="top:{(h - 8) / 9 * 100:.2f}%">{(h - 1) % 12 + 1} {"AM" if h < 12 else "PM"}</span>' for h in range(8, 17, 2))}</div>{"".join(f"""<div class=dc><b>{d} {n}</b><div class=tg>{"".join(f'<div class=bk style="top:{(h - 8) / 9 * 100:.2f}%;height:{3 / 9 * 100:.2f}%"><span>{(h - 1) % 12 + 1}&nbsp;{"AM" if h < 12 else "PM"} to {(h + 2) % 12 + 1}&nbsp;{"PM" if h + 3 >= 12 else "AM"}</span><em>ZIP {z}</em></div>' for h, z in BK8[d]) or '<div class=fr>Open</div>'}</div></div>""" for d, n in DY8)}</div></div>
<div class=bt85><div class="cd8 fm"><span class=sm8>BOOKING FORM ON YOUR WEBSITE</span>{"".join(f'<div class=f><span>{a}</span><b>{b}</b></div>' for a, b in [("Address", "Sample St, ZIP 12352"), ("Size", "2,100 sq ft"), ("Built", "1985"), ("Add-ons", "Sewer scope")])}</div>
<div class="dk8 cf"><span class=sm8>BOOKED · WED 25 NOV</span><b>10 AM to 1 PM</b><p>Buyer and agent get the time, the address and a reminder the day before.</p></div></div></div>''',
css=f""".w85{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.w85 .wk{{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:12px;min-height:0}}
.w85 .gd{{flex:1;display:grid;grid-template-columns:56px repeat(6,1fr);gap:8px;position:relative}}.w85 .ax{{position:relative;margin-top:44px;margin-bottom:8px}}.w85 .ax span{{position:absolute;right:0;font:700 13px/1 Inter;color:{MU8};white-space:nowrap}}.w85 .dc{{background:#f4f2ec;border-radius:14px;padding:8px;display:flex;flex-direction:column;gap:8px}}.w85 .tg{{flex:1;position:relative;background:repeating-linear-gradient(180deg,transparent 0 calc(22.22% - 1px),#ddd8cc calc(22.22% - 1px) 22.22%)}}.w85 .bk{{position:absolute;left:0;right:0}}.w85 .dc>b{{font:400 22px/1.3 Anton;letter-spacing:.4px;text-align:center}}
.w85 .bk.bk{{background:{SL8};color:#fff;border-radius:10px;padding:10px 8px;display:flex;flex-direction:column;gap:4px;border:2px solid #f4f2ec}}.w85 .bk span{{font:800 16px/1.3 Inter}}.w85 .bk em{{font:600 14px/1.3 Inter;font-style:normal;color:#dfe7ef}}.w85 .fr{{position:absolute;inset:0;border:2px dashed #c9c4b6;border-radius:10px;display:flex;align-items:center;justify-content:center;font:700 16px/1.2 Inter;color:{MU8}}}
.bt85{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:16px}}.bt85 .fm{{padding:18px 20px;display:flex;flex-direction:column;gap:6px}}.bt85 .f{{display:flex;justify-content:space-between;gap:10px;padding:9px 0;border-bottom:1px solid #ebe8e0}}.bt85 .f span{{font:500 18px/1.3 Inter;color:{MU8}}}.bt85 .f b{{font:700 18px/1.3 Inter}}
.bt85 .cf{{padding:20px 22px;display:flex;flex-direction:column;gap:8px;justify-content:center}}.bt85 .cf b{{font:400 40px/1.2 Anton;letter-spacing:.4px}}.bt85 .cf p{{font:500 19px/1.45 Inter;color:#dfe7ef}}""")

P["p428_insp_s6"] = t8(6, "HOME INSPECTION APP", "Run home inspections?<br><span>Let's build your app.</span>",
f'''<div class=w86><div class=tl86>{"".join(f'<div class=cd8><span class=ib>{ic(i, 38)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("check", "Area checklist", "Room by room"), ("camera", "Photo findings", "Pinned and labelled"), ("file", "Report on site", "Sent to buyer and agent"), ("cal", "Online booking", "The week by ZIP")])}</div>
<div class="dk8 q86"><span class=sm8>A QUESTION FOR INSPECTORS</span><p>How long does it take you to turn your notes and photos into a report? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{RD8};color:#fff",
css=f""".w86{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl86{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl86>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl86 .ib{{width:84px;height:84px;border-radius:24px;background:{TN8};color:{INK8}}}.tl86 b{{font:400 38px/1.25 Anton;letter-spacing:.4px}}.tl86>div>span:last-child{{font:500 23px/1.4 Inter;color:{MU8}}}
.q86{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q86 p{{font:700 29px/1.4 Inter;text-wrap:pretty}}""")
