
# ───────── 436 INDIA · Village milk collection centre · CAROUSEL 5 · Bitter + Open Sans · cooler steel / pasture green / cream
# New technique: SVG aluminium milk cans whose fill line is drawn from each farmer's litres, a 10-day × 2-shift litre
# strip for one farmer, and a cooler tank gauge filled from the same shift totals.
ST6b = "#5c6f7b"; PG6 = "#3d7a4f"; CM6 = "#faf6ec"; INK6b = "#1f2a30"; MU6b = "#66737a"; BL6 = "#2f6fa8"
FM6 = [("F-01", "Sample Farmer A", 12.0, 4.2, 8.6), ("F-02", "Sample Farmer B", 8.5, 3.8, 8.4), ("F-03", "Sample Farmer C", 15.0, 4.5, 8.7), ("F-04", "Sample Farmer D", 6.0, 3.6, 8.3),
       ("F-05", "Sample Farmer E", 10.5, 4.0, 8.5), ("F-06", "Sample Farmer F", 12.0, 4.8, 8.8), ("F-07", "Sample Farmer G", 7.5, 3.9, 8.4), ("F-08", "Sample Farmer H", 9.0, 4.1, 8.5)]
TL6 = sum(f[2] for f in FM6); FAT6 = sum(f[2] * f[3] for f in FM6) / TL6
CYC6 = [(16, 12.0, 10.5), (17, 11.5, 10.0), (18, 12.5, 10.5), (19, 12.0, 9.5), (20, 0, 0), (21, 11.0, 10.0), (22, 12.0, 10.5), (23, 12.0, 0), (24, 0, 0), (25, 0, 0)]
CT6 = sum(a + b for _, a, b in CYC6)
TANK6 = 250; EVE6 = 92.5
def can6(L, cap=20, w=150):
    fy = 160 - (L / cap) * 116
    return f'''<svg viewBox="0 0 120 190" style="display:block;width:{w}px;height:auto"><defs><clipPath id="cn6{int(L * 10)}"><path d="M22 52 Q22 40 34 38 H86 Q98 40 98 52 V170 Q98 180 88 180 H32 Q22 180 22 170 Z"/></clipPath></defs>
<rect x="40" y="10" width="40" height="18" rx="5" fill="#9aa7ae"/><path d="M34 28 H86 L92 38 H28 Z" fill="#b8c3c9"/>
<path d="M22 52 Q22 40 34 38 H86 Q98 40 98 52 V170 Q98 180 88 180 H32 Q22 180 22 170 Z" fill="#d7dee2"/><rect x="22" y="{fy:.1f}" width="76" height="{180 - fy:.1f}" fill="#fffdf6" clip-path="url(#cn6{int(L * 10)})"/>
<path d="M22 {fy:.1f} H98" stroke="{BL6}" stroke-width="2" stroke-dasharray="4 3"/><path d="M22 52 Q22 40 34 38 H86 Q98 40 98 52 V170 Q98 180 88 180 H32 Q22 180 22 170 Z" fill="none" stroke="#7f8d95" stroke-width="3"/><rect x="30" y="60" width="8" height="100" rx="4" fill="#fff" opacity=".55"/></svg>'''
B6b = f"""
body{{--f:'Open Sans';--h:'Bitter';background:{CM6};color:{INK6b};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:{PG6};margin-top:22px}}
h1{{font-family:'Bitter';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1px;margin-top:14px}} h1 span{{color:{BL6}}}
.sm6b{{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:{MU6b}}}
.cd6b{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(31,42,48,.08)}}
.dk6b{{background:{ST6b};color:#fff;border-radius:24px}}.dk6b .sm6b{{color:#d2dce1}}
"""
def t6b(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{PG6};color:#fff"):
    return page(B6b + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, INK6b, cta, ctacss, tagline=f"{n} / 5")
QS6b = [("“How many litres did I give on the 18th?”", "Turn back 20 pages"), ("“My fat was higher last time.”", "Which day? Which shift?"), ("“Is my slip ready?”", "Add it all by hand")]
P["p436_milk_s1"] = t6b(1, "MILK COLLECTION CENTRE · VILLAGE", "Milk register by hand?<br><span>Every can, both shifts, logged.</span>",
f'''<div class=w61b><div class="cd6b cn"><span class=sm6b>MORNING SHIFT · MON 23 NOV · 8 CANS · SAMPLE</span><div class=g>{"".join(f'<div class=c>{can6(f[2])}<b>{f[2]:g} L</b><span>{f[0]}</span></div>' for f in FM6)}</div></div>
<div class=qs>{"".join(f'<div class="cd6b q"><p>{a}</p><em>{b}</em></div>' for a, b in QS6b)}</div></div>''',
css=f""".w61b{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.cn{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:12px}}.cn .g{{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;align-items:center;justify-items:center}}
.cn .c{{display:flex;flex-direction:column;align-items:center;gap:4px}}.cn .c b{{font:800 24px/1.3 Bitter;color:{BL6}}}.cn .c span{{font:700 15px/1.3 'Open Sans';color:{MU6b}}}
.qs{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.qs .q{{padding:20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.qs p{{font:700 23px/1.35 Bitter}}.qs em{{align-self:flex-start;font:700 15px/1.25 'Open Sans';font-style:normal;border:2px dashed {PG6};color:#2b5a39;border-radius:10px;padding:8px 10px}}""")

P["p436_milk_s2"] = t6b(2, "1 · SHIFT LOG", "Litres and fat for each can,<br><span>saved as you test.</span>",
f'''<div class=w62b><div class="cd6b tb"><div class="r h"><span>FARMER</span><span>LITRES</span><span>FAT %</span><span>SNF %</span></div>{"".join(f'<div class=r><div><b>{f[0]}</b><small>{f[1]}</small></div><strong>{f[2]:g}</strong><span>{f[3]:.1f}</span><span>{f[4]:.1f}</span></div>' for f in FM6)}</div>
<div class=sd><div class="dk6b k"><span class=sm6b>MORNING TOTAL</span><b>{TL6:g} L</b><span>from {len(FM6)} farmers</span></div><div class="dk6b k" style="background:{PG6}"><span class=sm6b>AVERAGE FAT</span><b>{FAT6:.2f}%</b><span>weighted by litres</span></div>
<div class="cd6b n"><span class=sm6b>EACH FARMER GETS</span><p>A message right after testing:</p><div class=bb><b>F-06 · Mon 23 Nov · morning</b>12 L · fat 4.8% · SNF 8.8%<small>Sample message</small></div></div></div></div>''',
css=f""".w62b{{flex:1;display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,.65fr);gap:16px;min-height:0}}
.tb{{padding:16px 22px;display:flex;flex-direction:column}}.tb .r{{flex:1;display:grid;grid-template-columns:1fr 90px 80px 80px;gap:10px;align-items:center;border-top:1px solid #efe9dc}}.tb .h{{flex:none;border:0;padding-bottom:8px}}.tb .h span{{font:700 13px/1.3 'Open Sans';letter-spacing:1px;color:{MU6b};text-align:right}}.tb .h span:first-child{{text-align:left}}
.tb .r b{{display:block;font:700 20px/1.3 'Open Sans';color:{PG6}}}.tb .r small{{font:500 17px/1.3 'Open Sans';color:{MU6b}}}.tb .r strong{{font:800 22px/1.3 Bitter;text-align:right;color:{BL6}}}.tb .r>span{{font:600 19px/1.3 'Open Sans';text-align:right}}
.sd{{display:flex;flex-direction:column;gap:16px}}.sd .k{{padding:18px 20px;display:flex;flex-direction:column;gap:4px}}.sd .k b{{font:800 44px/1.2 Bitter}}.sd .k>span:last-child{{font:500 16px/1.3 'Open Sans';color:#e6eef2}}.sd .n{{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:14px;justify-content:center}}.sd .n p{{font:600 19px/1.45 'Open Sans'}}.sd .bb{{background:#e3f0e6;border-radius:16px 16px 16px 4px;padding:14px 16px;font:600 18px/1.45 'Open Sans';display:flex;flex-direction:column;gap:4px}}.sd .bb b{{font:700 15px/1.3 'Open Sans';color:{PG6}}}.sd .bb small{{font:500 13px/1.3 'Open Sans';color:{MU6b}}}""")

MX6 = max(max(a, b) for _, a, b in CYC6)
P["p436_milk_s3"] = t6b(3, "2 · 10-DAY CYCLE", "One farmer's 10 days,<br><span>both shifts, one screen.</span>",
f'''<div class=w63b><div class="cd6b ch"><span class=sm6b>SAMPLE FARMER F · 16 TO 25 NOV · LITRES PER SHIFT</span><div class=bs>{"".join(f"""<div class=d><div class=pr><i class=m style="height:{a / MX6 * 100:.0f}%"></i><i class=e style="height:{b / MX6 * 100:.0f}%"></i></div><b>{dd}</b><span>{'today' if dd == 23 else ('no milk' if a == 0 and dd < 23 else ('' if dd < 23 else 'to come'))}</span></div>""" for dd, a, b in CYC6)}</div>
<div class=lg><span><i class=m></i>Morning</span><span><i class=e></i>Evening</span><span>Fri 20 Nov: no milk given</span></div></div>
<div class=bt><div class="dk6b"><span class=sm6b>SO FAR THIS CYCLE</span><b>{CT6:g} L</b></div><div class="cd6b"><span class=sm6b>SLIP ON THU 26 NOV</span><p>Litres and fat for every shift, worked out with your own rate chart, sent to the farmer's phone.</p></div></div></div>''',
css=f""".w63b{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.ch{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:12px}}
.ch .bs{{flex:1;display:grid;grid-template-columns:repeat(10,1fr);gap:10px}}.ch .d{{display:flex;flex-direction:column;align-items:center;gap:4px}}.ch .pr{{flex:1;width:100%;display:flex;gap:4px;align-items:flex-end;background:#f6f2e8;border-radius:10px;padding:4px}}.ch .pr i{{flex:1;border-radius:6px 6px 3px 3px}}.ch i.m{{background:{BL6}}}.ch i.e{{background:{PG6}}}
.ch .d b{{font:800 20px/1.3 Bitter}}.ch .d span{{font:600 12px/1.3 'Open Sans';color:{MU6b};height:16px}}.ch .lg{{display:flex;gap:20px;font:600 16px/1.3 'Open Sans'}}.ch .lg span{{display:flex;align-items:center;gap:8px}}.ch .lg i{{width:18px;height:18px;border-radius:5px}}.ch .lg span:last-child{{color:{MU6b}}}
.bt{{display:grid;grid-template-columns:minmax(0,.7fr) minmax(0,1.3fr);gap:16px}}.bt>div{{padding:18px 22px;display:flex;flex-direction:column;gap:6px}}.bt b{{font:800 48px/1.2 Bitter}}.bt p{{font:600 20px/1.45 'Open Sans'}}""")

TOTD6 = TL6 + EVE6
def tank6():
    fy = 300 - TOTD6 / TANK6 * 250
    return f'''<svg viewBox="30 10 200 316" style="position:absolute;inset:0;width:100%;height:100%"><rect x="40" y="40" width="180" height="262" rx="30" fill="#dfe6ea" stroke="#7f8d95" stroke-width="4"/>
<clipPath id="tk6"><rect x="42" y="42" width="176" height="258" rx="28"/></clipPath><rect x="40" y="{fy:.0f}" width="180" height="{302 - fy:.0f}" fill="#fffdf6" clip-path="url(#tk6)"/><path d="M42 {fy:.0f} H218" stroke="{BL6}" stroke-width="3" stroke-dasharray="6 4"/>
<rect x="100" y="16" width="60" height="26" rx="6" fill="#9aa7ae"/><rect x="60" y="302" width="16" height="20" fill="#7f8d95"/><rect x="184" y="302" width="16" height="20" fill="#7f8d95"/>
<rect x="64" y="{fy - 44:.0f}" width="132" height="34" rx="8" fill="{BL6}"/><text x="130" y="{fy - 20:.0f}" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="20" fill="#fff"><tspan>{TOTD6:g} L</tspan></text></svg>'''
P["p436_milk_s4"] = t6b(4, "3 · COOLER AND TANKER", "Know what's in the cooler<br><span>before the tanker comes.</span>",
f'''<div class=w64b><div class="cd6b tk"><span class=sm6b>BULK COOLER · {TANK6} L · SAMPLE</span><div class=im>{tank6()}</div></div>
<div class=rt>{"".join(f'<div class="cd6b r"><span>{a}</span><b>{b}</b></div>' for a, b in [("Morning shift", f"{TL6:g} L"), ("Evening shift", f"{EVE6:g} L"), ("In the cooler now", f"{TOTD6:g} L"), ("Space left", f"{TANK6 - TOTD6:g} L")])}
<div class="dk6b tn"><span class=sm6b>TANKER PICKUP · TUE 24 NOV · 7 AM</span><p>Driver sees the litres and the average fat before he leaves the plant. Both sides sign on the app.</p></div></div></div>''',
css=f""".w64b{{flex:1;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:16px;min-height:0}}.tk{{padding:20px 22px;display:flex;flex-direction:column;gap:10px}}.tk .im{{flex:1;min-height:0;position:relative}}
.rt{{display:flex;flex-direction:column;gap:12px}}.rt .r{{flex:1;padding:12px 22px;display:flex;justify-content:space-between;align-items:center}}.rt .r span{{font:600 20px/1.3 'Open Sans'}}.rt .r b{{font:800 30px/1.3 Bitter;color:{BL6}}}.rt .tn{{padding:18px 22px;display:flex;flex-direction:column;gap:8px}}.rt .tn p{{font:600 19px/1.45 'Open Sans'}}""")

P["p436_milk_s5"] = t6b(5, "MILK COLLECTION APP", "Run a milk centre?<br><span>Let's build your app.</span>",
f'''<div class=w65b><div class=tl>{"".join(f'<div class=cd6b><span class=ib>{ic(i, 38)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("drop", "Shift log", "Litres, fat, SNF"), ("cal", "10-day cycle", "Per farmer"), ("doc", "Farmer slips", "Sent to the phone"), ("truck", "Cooler and tanker", "Litres before pickup")])}</div>
<div class="dk6b q"><span class=sm6b>A QUESTION FOR MILK CENTRES</span><p>How long does it take you to make the slips at the end of every cycle? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{BL6};color:#fff",
css=f""".w65b{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl .ib{{width:84px;height:84px;border-radius:24px;background:#dbe8f3;color:{BL6}}}.tl b{{font:800 36px/1.25 Bitter}}.tl>div>span:last-child{{font:500 23px/1.4 'Open Sans';color:{MU6b}}}
.q{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q p{{font:700 29px/1.4 Bitter;text-wrap:pretty}}""")
