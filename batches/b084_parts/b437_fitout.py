
# ───────── 437 INDIA · Shop interior fit-out (racks, counters for small shops) · CAROUSEL 5 · Poppins + DM Sans · ply beige / laminate teal / charcoal
# New technique: isometric shop floor drawn from one item list in feet (iso projection, painter's order by x + y), the
# same items as a to-scale top-down plan with computed walkway gaps, an item list and an 8-day job Gantt.
PB7 = "#e9d8b8"; LT7 = "#1f7a78"; CH7 = "#2b2d31"; BG7b = "#f4efe6"; MU7 = "#6b6d72"; AC7 = "#e07a3f"
SW7b, SD7 = 12, 20
IT7 = [("Back rack", 2, 0, 8, 1.5, 7, "#cfe3e2"), ("Left wall rack", 0, 2, 1.5, 14, 7, "#cfe3e2"), ("Right low rack", 10.5, 2, 1.5, 14, 4, "#cfe3e2"),
       ("Centre display", 4.5, 6, 3, 6, 4, "#f2c98a"), ("Counter", 7, 16, 4, 2.5, 3.5, "#9fd0c9")]
C30, S30 = math.cos(math.pi / 6), .5
def iso7(x, y, z, S=17):
    return ((x - y) * C30 * S + SD7 * C30 * S + 20, (x + y) * S30 * S - z * S + 9 * S + 20)
def poly7(pts, fill, stroke="#5d5f63", sw=1.5):
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
def shade7(c, f):
    c = c.lstrip("#"); r, g, b = (int(c[i:i + 2], 16) for i in (0, 2, 4)); return f"#{int(r * f):02x}{int(g * f):02x}{int(b * f):02x}"
def isoshop7(labels=True):
    P_ = iso7; out = poly7([P_(0, 0, 0), P_(SW7b, 0, 0), P_(SW7b, SD7, 0), P_(0, SD7, 0)], "#efe6d6")
    out += "".join(f'<line x1="{P_(0, k, 0)[0]:.1f}" y1="{P_(0, k, 0)[1]:.1f}" x2="{P_(SW7b, k, 0)[0]:.1f}" y2="{P_(SW7b, k, 0)[1]:.1f}" stroke="#e0d4bf" stroke-width="1"/>' for k in range(2, SD7, 2))
    out += poly7([P_(0, 0, 0), P_(SW7b, 0, 0), P_(SW7b, 0, 9), P_(0, 0, 9)], "#f7f1e6") + poly7([P_(0, 0, 0), P_(0, SD7, 0), P_(0, SD7, 9), P_(0, 0, 9)], "#ece3d2")
    for n, x, y, w, d, h, col in sorted(IT7, key=lambda t: t[1] + t[2]):
        out += poly7([P_(x + w, y, 0), P_(x + w, y + d, 0), P_(x + w, y + d, h), P_(x + w, y, h)], shade7(col, .82))
        out += poly7([P_(x, y + d, 0), P_(x + w, y + d, 0), P_(x + w, y + d, h), P_(x, y + d, h)], shade7(col, .7))
        out += poly7([P_(x, y, h), P_(x + w, y, h), P_(x + w, y + d, h), P_(x, y + d, h)], col)
        if n != "Centre display" and n != "Counter":
            for z in ((1.75, 3.5, 5.25) if h >= 7 else (2,)):
                if w < d: a, b = P_(x + w, y, z), P_(x + w, y + d, z)
                else: a, b = P_(x, y + d, z), P_(x + w, y + d, z)
                out += f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#5d5f63" stroke-width="1.5"/>'
    if labels:
        LP = {"Back rack": (6, 0.7, 9.6), "Left wall rack": (0.7, 6, 9.2), "Right low rack": (11.2, 7, 4.9), "Centre display": (6, 9, 5.4), "Counter": (9, 17.2, 4.6)}
        for n, (x, y, z) in LP.items():
            cx, cy = iso7(x, y, z); wdt = len(n) * 9 + 20
            out += f'<rect x="{cx - wdt / 2:.1f}" y="{cy - 17:.1f}" width="{wdt}" height="28" rx="8" fill="{CH7}"/><text x="{cx:.1f}" y="{cy + 2:.1f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#fff"><tspan>{n}</tspan></text>'
        ex, ey = iso7(3, SD7, 0)
        out += f'<rect x="{ex - 50:.1f}" y="{ey + 6:.1f}" width="100" height="26" rx="8" fill="{AC7}"/><text x="{ex:.1f}" y="{ey + 24:.1f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#fff"><tspan>Shop door</tspan></text>'
    W = (SW7b + SD7) * C30 * 17 + 40; H = (SW7b + SD7) * S30 * 17 + 9 * 17 + 80
    return f'<svg viewBox="0 0 {W:.0f} {H:.0f}" style="position:absolute;inset:0;width:100%;height:100%">{out}</svg>'
def plan7():
    S = 22; o = 14; out = f'<rect x="{o}" y="{o}" width="{SW7b * S}" height="{SD7 * S}" fill="#fbf7ef" stroke="{CH7}" stroke-width="5"/>'
    out += f'<rect x="{o + 2 * S}" y="{o + SD7 * S - 3}" width="{3 * S}" height="6" fill="{AC7}"/>'
    for n, x, y, w, d, h, col in IT7:
        out += f'<rect x="{o + x * S}" y="{o + y * S}" width="{w * S}" height="{d * S}" fill="{col}" stroke="#5d5f63" stroke-width="1.5"/>'
    gaps = [((1.5, 9), (4.5, 9)), ((7.5, 9), (10.5, 9))]
    for (x1, y1), (x2, y2) in gaps:
        out += f'<path d="M{o + x1 * S} {o + y1 * S} H{o + x2 * S}" stroke="{AC7}" stroke-width="2.5" marker-start="url(#ar7)" marker-end="url(#ar7)"/><text x="{o + (x1 + x2) / 2 * S}" y="{o + y1 * S - 8}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="15" fill="{AC7}"><tspan>{x2 - x1:g} ft</tspan></text>'
    out += f'<text x="{o + SW7b * S / 2}" y="{o + SD7 * S + 34}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="{MU7}"><tspan>{SW7b} ft wide · door</tspan></text>'
    return f'<svg viewBox="0 0 {SW7b * 22 + 28} {SD7 * 22 + 52}" style="position:absolute;inset:0;width:100%;height:100%"><defs><marker id="ar7" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 Z" fill="{AC7}"/></marker></defs>{out}</svg>'
B7 = f"""
body{{--f:'DM Sans';--h:'Poppins';background:{BG7b};color:{CH7}}}
.kk{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{LT7};margin-top:22px}}
h1{{font-family:'Poppins';font-weight:800;font-size:56px;line-height:1.2;letter-spacing:-1.5px;margin-top:14px}} h1 span{{color:{LT7}}}
.sm7{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:{MU7}}}
.cd7b{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(43,45,49,.08)}}
.dk7b{{background:{CH7};color:#fff;border-radius:24px}}.dk7b .sm7{{color:#b9bcc2}}
.im7{{flex:1;min-height:0;position:relative}}
"""
def t7(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{LT7};color:#fff"):
    return page(B7 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, CH7, cta, ctacss, tagline=f"{n} / 5")
P["p437_fit_s1"] = t7(1, "SHOP FIT-OUT · RACKS AND COUNTERS", "Shop fit-out on a rough sketch?<br><span>Show the whole shop first.</span>",
f'''<div class=w71><div class="cd7b sh"><span class=sm7>SAMPLE SHOP · {SW7b} × {SD7} FT · RACKS, DISPLAY AND COUNTER</span><div class=im7>{isoshop7()}</div></div>
<div class=qs>{"".join(f'<div class="cd7b q"><p>{a}</p><em>{b}</em></div>' for a, b in [("“Will the counter block the door?”", "Hard to see on paper"), ("“Can two people pass here?”", "Nobody measured it"), ("“How high is the top shelf?”", "Owner finds out on day 7")])}</div></div>''',
css=f""".w71{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.sh{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px;min-height:0}}
.qs{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.qs .q{{padding:20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.qs p{{font:700 22px/1.35 Poppins}}.qs em{{align-self:flex-start;font:700 15px/1.25 'DM Sans';font-style:normal;border:2px dashed {AC7};color:#a4491b;border-radius:10px;padding:8px 10px}}""")

P["p437_fit_s2"] = t7(2, "1 · MEASURE AND PLAN", "Every item to scale,<br><span>every walkway checked.</span>",
f'''<div class=w72><div class="cd7b pl"><span class=sm7>TOP VIEW · 1 SQUARE = 1 FT · SAMPLE</span><div class=im7>{plan7()}</div></div>
<div class=rt>{"".join(f'<div class="cd7b r"><i style="background:{c}"></i><div><b>{n}</b><span>{w:g} × {d:g} ft · {h:g} ft high</span></div></div>' for n, x, y, w, d, h, c in IT7)}
<div class="dk7b ck"><span class=sm7>WALKWAY CHECK</span><p>{ic("check", 22, "#7fd3c9", 3)}Left rack to display: 3 ft</p><p>{ic("check", 22, "#7fd3c9", 3)}Display to right rack: 3 ft</p><p>{ic("check", 22, "#7fd3c9", 3)}Door clear of the counter</p></div></div></div>''',
css=f""".w72{{flex:1;display:grid;grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);gap:16px;min-height:0}}.pl{{padding:20px 22px;display:flex;flex-direction:column;gap:10px}}
.rt{{display:flex;flex-direction:column;gap:10px}}.rt .r{{flex:1;padding:10px 18px;display:flex;align-items:center;gap:14px}}.rt .r i{{width:30px;height:30px;border-radius:8px;border:2px solid #5d5f63;flex:none}}.rt .r b{{display:block;font:700 20px/1.3 Poppins}}.rt .r span{{font:500 17px/1.3 'DM Sans';color:{MU7}}}
.rt .ck{{padding:16px 20px;display:flex;flex-direction:column;gap:6px}}.rt .ck p{{display:flex;align-items:center;gap:10px;font:600 18px/1.35 'DM Sans'}}""")

RK7 = [i for i in IT7 if "rack" in i[0]]; LED7 = sum(max(i[3], i[4]) for i in RK7)
BOQ7 = [("Left wall rack", "1", "1.5 × 14 ft, 7 ft high, 4 shelves"), ("Right low rack", "1", "1.5 × 14 ft, 4 ft high, 2 shelves"), ("Back rack", "1", "8 × 1.5 ft, 7 ft high, 4 shelves"), ("Centre display", "1", "3 × 6 ft, 4 ft high, both sides open"),
        ("Counter", "1", "4 × 2.5 ft, glass top, 2 drawers"), ("LED strip under shelves", f"{LED7:g} ft", "Length of all 3 racks added up"), ("Laminate", "Teal + light oak", "Owner picked from swatches")]
P["p437_fit_s3"] = t7(3, "2 · ITEM LIST", "One clear item list<br><span>the owner signs off.</span>",
f'''<div class=w73><div class="cd7b bq"><div class="r h"><span>ITEM</span><span>QTY</span><span>DETAIL</span></div>{"".join(f'<div class=r><b>{a}</b><strong>{q}</strong><span>{d}</span></div>' for a, q, d in BOQ7)}</div>
<div class=bt><div class="dk7b"><span class=sm7>APPROVED BY OWNER</span><b>Wed 25 Nov</b><p>Signed on the phone with the 3D view attached.</p></div><div class="cd7b sw"><span class=sm7>LAMINATE PICKED</span><div class=s>{"".join(f'<div><i style="background:{c}"></i><span>{t}</span></div>' for c, t in [(LT7, "Teal gloss"), ("#d8b98c", "Light oak"), ("#f4f1ea", "Frosty white"), ("#3b3d42", "Charcoal")])}</div></div></div></div>''',
css=f""".w73{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.bq{{flex:1;padding:18px 24px;display:flex;flex-direction:column}}.bq .r{{flex:1;display:grid;grid-template-columns:260px 160px 1fr;gap:14px;align-items:center;border-top:1px solid #eee7da}}.bq .h{{flex:none;border:0;padding-bottom:8px}}.bq .h span{{font:700 13px/1.3 'DM Sans';letter-spacing:1px;color:{MU7}}}
.bq .r b{{font:700 21px/1.3 Poppins}}.bq .r strong{{font:800 20px/1.3 'DM Sans';color:{LT7}}}.bq .r>span{{font:500 18px/1.35 'DM Sans';color:{MU7}}}
.bt{{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:16px}}.bt>div{{padding:18px 22px;display:flex;flex-direction:column;gap:6px}}.bt .dk7b b{{font:800 34px/1.25 Poppins;color:#7fd3c9}}.bt .dk7b p{{font:500 17px/1.4 'DM Sans';color:#dfe1e5}}
.bt .s{{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;align-items:center}}.bt .s div{{display:flex;flex-direction:column;align-items:center;gap:6px}}.bt .s i{{width:64px;height:64px;border-radius:14px;border:2px solid #d8d2c6}}.bt .s span{{font:600 15px/1.3 'DM Sans';text-align:center}}""")

GT7 = [("Measure and 3D view", 1, 2, LT7), ("Owner approval", 3, 3, AC7), ("Racks made in workshop", 4, 6, "#8b6f4e"), ("Fitting at the shop", 7, 7, LT7), ("Lights, cleaning, handover", 8, 8, CH7)]
DAY7 = ["Mon 23", "Tue 24", "Wed 25", "Thu 26", "Fri 27", "Sat 28", "Mon 30", "Tue 1"]
P["p437_fit_s4"] = t7(4, "3 · JOB PLAN", "8 working days,<br><span>and the owner sees each one.</span>",
f'''<div class=w74><div class="cd7b gt"><div class="r h"><span></span>{"".join(f'<span>{d}</span>' for d in DAY7)}</div>{"".join(f'<div class=r><b>{n}</b><div class=tr><i style="grid-column:{a} / {b + 1};background:{c}"></i></div></div>' for n, a, b, c in GT7)}
<div class=nt>Sun 29 Nov is a day off · today is Mon 23 Nov</div></div>
<div class=bt4b><div class="dk7b"><span class=sm7>PHOTO UPDATE · FRI 27 NOV · SAMPLE</span><p>Wall racks are ready in the workshop. Fitting at your shop on Mon 30 Nov, 9 AM. The shop can stay open.</p></div><div class="cd7b ph">{"".join(f'<div class=t><svg viewBox="0 0 120 90" style="width:100%;height:100%;display:block"><rect width="120" height="90" fill="#efe6d6"/><rect x="{20 + k * 6}" y="14" width="{50 - k * 8}" height="66" fill="#cfe3e2" stroke="#5d5f63" stroke-width="2"/>{"".join(f"<line x1={chr(34)}{20 + k * 6}{chr(34)} y1={chr(34)}{14 + z * 16}{chr(34)} x2={chr(34)}{70 - k * 2}{chr(34)} y2={chr(34)}{14 + z * 16}{chr(34)} stroke={chr(34)}#5d5f63{chr(34)} stroke-width={chr(34)}2{chr(34)}/>" for z in range(1, 4))}<rect x="78" y="40" width="28" height="40" fill="#f2c98a" stroke="#5d5f63" stroke-width="2"/></svg></div>' for k in range(3))}</div></div></div>''',
css=f""".w74{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.gt{{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:4px}}.gt .r{{flex:1;display:grid;grid-template-columns:230px 1fr;gap:12px;align-items:center;border-top:1px solid #eee7da}}
.gt .h{{flex:none;border:0;grid-template-columns:230px repeat(8,1fr);gap:12px 0}}.gt .h span{{font:700 13px/1.3 'DM Sans';color:{MU7};text-align:center}}.gt .r b{{font:700 18px/1.3 Poppins}}
.gt .tr{{display:grid;grid-template-columns:repeat(8,1fr);height:44px;background:repeating-linear-gradient(90deg,#f6f1e8 0 calc(12.5% - 2px),#fff calc(12.5% - 2px) 12.5%);border-radius:10px}}.gt .tr i{{border-radius:10px}}
.gt .nt{{font:600 15px/1.3 'DM Sans';color:{MU7};padding-top:8px}}
.bt4b{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}}.bt4b .dk7b{{padding:18px 22px;display:flex;flex-direction:column;gap:8px}}.bt4b .dk7b p{{font:600 19px/1.45 'DM Sans'}}.bt4b .ph{{padding:14px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.bt4b .t{{border-radius:12px;overflow:hidden}}""")

P["p437_fit_s5"] = t7(5, "SHOP FIT-OUT APP", "Do shop fit-outs?<br><span>Let's build your job app.</span>",
f'''<div class=w75><div class=tl>{"".join(f'<div class=cd7b><span class=ib>{ic(i, 38)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("grid", "3D shop view", "From your measurements"), ("check", "Walkway check", "Before anything is cut"), ("doc", "Item list", "Signed by the owner"), ("camera", "Photo updates", "Day by day")])}</div>
<div class="dk7b q"><span class=sm7>A QUESTION FOR FIT-OUT CONTRACTORS</span><p>How do you show a shop owner what the racks will look like before you build them? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{AC7};color:#fff",
css=f""".w75{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl .ib{{width:84px;height:84px;border-radius:24px;background:#d5ebe9;color:{LT7}}}.tl b{{font:800 34px/1.25 Poppins}}.tl>div>span:last-child{{font:500 23px/1.4 'DM Sans';color:{MU7}}}
.q{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q p{{font:700 27px/1.4 Poppins;text-wrap:pretty}}""")
