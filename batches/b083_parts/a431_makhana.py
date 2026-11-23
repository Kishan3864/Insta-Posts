
# ───────── 431 INDIA · Makhana (fox nut) processor and grader · CAROUSEL 5 · Lora + DM Sans · pond green / makhana ivory / lotus pink
# New technique: seeded SVG makhana pops in round sieve trays sized by grade (sutta), a lot-split bar computed from each
# lot's grade shares, sack isotype stock per grade, and FIFO matching of buyer orders to grade stock.
PG1 = "#24564a"; IV1 = "#f6f0e2"; LP1 = "#d9718f"; INK1 = "#1f2a26"; MU1 = "#62706a"; BR1 = "#8a6a45"
GR1 = [("6+ sutta", 6, "#24564a"), ("5 sutta", 5, "#3f8a77"), ("4 sutta", 4, "#8fbfa9"), ("Broken", 0, "#d9c7a2")]
LOT1 = [("L-21", "Sample Farmer A", "Mon 16 Nov", 400, (30, 40, 22, 8)), ("L-22", "Sample Farmer B", "Wed 18 Nov", 250, (24, 42, 26, 8)),
        ("L-23", "Sample Farmer C", "Fri 20 Nov", 350, (34, 38, 20, 8))]
def split1(kg, sh): return [round(kg * p / 100) for p in sh]
STK1 = [sum(split1(l[3], l[4])[i] for l in LOT1) for i in range(4)]
ORD1 = [("Sample Snack Brand A", 0, 150), ("Sample Wholesaler B", 1, 220), ("Sample Retail Chain C", 2, 120), ("Sample Exporter D", 0, 200), ("Sample Shop E", 1, 60)]
NEED1 = [sum(o[2] for o in ORD1 if o[1] == i) for i in range(4)]
def pops1(seed, n, rr, w=260, h=170, fill=True):
    rnd = random.Random(seed); out = ""
    for _ in range(n):
        x, y = rnd.uniform(rr + 4, w - rr - 4), rnd.uniform(rr + 4, h - rr - 4); r = rr * rnd.uniform(.85, 1.1)
        out += f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r:.1f}" ry="{r * .9:.1f}" fill="#fbf7ec" stroke="#cdbb93" stroke-width="1.2"/>'
        out += "".join(f'<circle cx="{x + rnd.uniform(-r * .6, r * .6):.1f}" cy="{y + rnd.uniform(-r * .6, r * .6):.1f}" r="{rnd.uniform(.8, 1.8):.1f}" fill="{BR1}" opacity=".7"/>' for _ in range(3))
    return out
def tray1(i, seed):
    name, s, col = GR1[i]; rr = 6 + s * 2.2 if s else 5
    n = {6: 26, 5: 34, 4: 46, 0: 60}[s]
    inner = pops1(seed, n, rr, 240, 240) if s else "".join(f'<path d="M{x} {y} a14 14 0 0 1 26 0 Z" fill="#fbf7ec" stroke="#cdbb93" stroke-width="1.2"/>' for x, y in [(random.Random(seed + k).uniform(30, 196), random.Random(seed * 7 + k).uniform(40, 200)) for k in range(60)])
    return f'''<svg viewBox="0 0 260 260" style="display:block;width:100%;height:auto"><defs><clipPath id="tr1{seed}"><circle cx="130" cy="130" r="112"/></clipPath></defs>
<circle cx="130" cy="130" r="126" fill="#c9a87a"/><circle cx="130" cy="130" r="114" fill="#e9dcc0"/><g clip-path="url(#tr1{seed})" transform="translate(10 10)">{inner}</g>
<circle cx="130" cy="130" r="114" fill="none" stroke="{col}" stroke-width="5"/></svg>'''
B1 = f"""
body{{--f:'DM Sans';--h:'Lora';background:{IV1};color:{INK1};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{LP1};margin-top:22px}}
h1{{font-family:'Lora';font-weight:700;font-size:60px;line-height:1.2;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{PG1}}}
.sm1{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:{MU1}}}
.cd1{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(36,86,74,.08)}}
.dk1{{background:{PG1};color:#fff;border-radius:24px}}.dk1 .sm1{{color:#b9d6cc}}
.gs1.gs1{{display:inline-block;width:18px;height:18px;border-radius:5px;flex:none}}
"""
def t1(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{PG1};color:#fff"):
    return page(B1 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, INK1, cta, ctacss, tagline=f"{n} / 5")
gs1 = lambda i: f'<i class=gs1 style="background:{GR1[i][2]}"></i>'
L0 = LOT1[0]; S0 = split1(L0[3], L0[4])
QS1 = [("“Which farmer's lot was this?”", "No lot number on the sack"), ("“How much 6+ is left?”", "Count the sacks again"), ("“Send the same grade as last time.”", "Which one was it?")]
P["p431_makhana_s1"] = t1(1, "MAKHANA PROCESSING · GRADING AND SALES", "Makhana by guesswork?<br><span>Every lot graded, every kg known.</span>",
f'''<div class=w11><div class="cd1 tr11"><span class=sm1>ONE LOT, FOUR GRADES AFTER THE SIEVE · SAMPLE</span><div class=g>{"".join(f'<div class=t>{tray1(i, 11 + i)}<b>{GR1[i][0]}</b><strong>{S0[i]} kg</strong><div class=bb><i style="height:{L0[4][i] / max(L0[4]) * 100:.0f}%;background:{GR1[i][2]}"></i></div></div>' for i in range(4))}</div><div class=lt><b>{L0[0]}</b><span>{L0[1]} · {L0[3]} kg popped makhana in · {L0[2]}</span></div></div>
<div class=qs11>{"".join(f'<div class="cd1 q"><p>{a}</p><em>{b}</em></div>' for a, b in QS1)}</div></div>''',
css=f""".w11{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tr11{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:12px;min-height:0}}
.tr11 .g{{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:16px;align-items:center}}.tr11 .t{{display:flex;flex-direction:column;align-items:center;gap:10px}}.tr11 .t b{{font:700 24px/1.3 Lora}}.tr11 .t strong{{font:700 34px/1.2 Lora;color:{PG1}}}.tr11 .bb{{width:70%;height:150px;background:#f3ecdd;border-radius:10px;display:flex;align-items:flex-end;overflow:hidden}}.tr11 .bb i{{width:100%;border-radius:10px 10px 0 0}}.tr11 .lt{{display:flex;align-items:baseline;gap:14px;background:#f3ecdd;border-radius:14px;padding:12px 18px}}.tr11 .lt b{{font:700 26px/1.3 Lora;color:{PG1}}}.tr11 .lt span{{font:600 19px/1.3 'DM Sans'}}
.qs11{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.qs11 .q{{padding:20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.qs11 p{{font:700 25px/1.35 Lora}}
.qs11 em{{align-self:flex-start;font:700 16px/1.25 'DM Sans';font-style:normal;border:2px dashed {LP1};color:#a3445f;border-radius:10px;padding:8px 10px}}""")

P["p431_makhana_s2"] = t1(2, "1 · LOT CARD", "Every lot gets a number<br><span>and its own grade split.</span>",
f'''<div class=w12><div class="dk1 lc"><div><span class=sm1>LOT CARD · SAMPLE</span><b>{L0[0]}</b></div>{"".join(f'<div class=r><span>{a}</span><strong>{b}</strong></div>' for a, b in [("Farmer", L0[1]), ("Came in", L0[2]), ("Popped makhana", f"{L0[3]} kg"), ("Sacks", f"{L0[3] // 10} of 10 kg")])}</div>
<div class="cd1 sp"><span class=sm1>GRADE SPLIT FOR {L0[0]} · {L0[3]} KG</span><div class=bar>{"".join(f'<div style="flex:{p};background:{GR1[i][2]}"><b>{p}%</b></div>' for i, p in enumerate(L0[4]))}</div>
{"".join(f'<div class=r>{gs1(i)}<b>{GR1[i][0]}</b><span>{L0[4][i]}% of {L0[3]} kg</span><strong>{S0[i]} kg</strong></div>' for i in range(4))}</div>
<div class="cd1 al"><span class=sm1>ALL LOTS THIS WEEK</span><div class=hd><span>Lot</span>{"".join(f'<span>{g[0]}</span>' for g in GR1)}</div>{"".join(f'<div class=rw><b>{l[0]}</b>{"".join(f"<span>{v} kg</span>" for v in split1(l[3], l[4]))}</div>' for l in LOT1)}</div></div>''',
css=f""".w12{{flex:1;display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);grid-template-rows:auto 1fr;gap:16px;min-height:0}}
.lc{{grid-row:1 / 3;padding:24px;display:flex;flex-direction:column;gap:6px;justify-content:space-between}}.lc b{{display:block;margin-top:10px;font:700 64px/1.2 Lora;color:#f3c9d5}}.lc .r{{display:flex;flex-direction:column;padding:12px 0;border-top:1px solid rgba(255,255,255,.18)}}.lc .r span{{font:500 17px/1.3 'DM Sans';color:#b9d6cc}}.lc .r strong{{font:700 25px/1.3 'DM Sans'}}
.sp{{padding:20px 24px;display:flex;flex-direction:column;gap:10px}}.sp .bar{{display:flex;height:64px;border-radius:14px;overflow:hidden;margin-bottom:6px}}.sp .bar div{{display:flex;align-items:center;justify-content:center}}.sp .bar b{{font:700 19px/1.2 'DM Sans';color:#fff}}.sp .bar div:nth-child(4) b,.sp .bar div:nth-child(3) b{{color:{INK1}}}
.sp .r{{display:grid;grid-template-columns:18px 1fr 150px 90px;gap:12px;align-items:center;padding:6px 0;border-top:1px solid #eee6d6}}.sp .r b{{font:700 20px/1.3 'DM Sans'}}.sp .r span{{font:500 17px/1.3 'DM Sans';color:{MU1}}}.sp .r strong{{font:700 22px/1.3 Lora;text-align:right}}
.al{{padding:20px 24px;display:flex;flex-direction:column;gap:6px}}.al .hd,.al .rw{{flex:1;display:grid;grid-template-columns:70px repeat(4,1fr);gap:8px;align-items:center}}.al .hd{{flex:none;padding-bottom:6px}}.al .hd span{{font:700 14px/1.3 'DM Sans';color:{MU1}}}.al .rw{{border-top:1px solid #eee6d6}}.al .rw b{{font:700 23px/1.3 'DM Sans';color:{PG1}}}.al .rw span{{font:600 22px/1.3 'DM Sans'}}""")

def sacks1(kg, col):
    n = math.ceil(kg / 25)
    return "".join(f'<i style="background:{col}"></i>' for _ in range(n))
P["p431_makhana_s3"] = t1(3, "2 · GRADE STOCK", "Stock by grade,<br><span>not by sack count.</span>",
f'''<div class=w13><div class="cd1 st"><span class=sm1>IN STOCK FROM {", ".join(l[0] for l in LOT1)} · 1 SACK = 25 KG · SAMPLE</span>{"".join(f"""<div class=r><div class=nm>{gs1(i)}<b>{GR1[i][0]}</b></div><div class=sk>{sacks1(STK1[i], GR1[i][2])}</div><strong>{STK1[i]} kg</strong></div>""" for i in range(4))}</div>
<div class=bt13>{"".join(f"""<div class="{'dk1' if STK1[i] - NEED1[i] < 0 else 'cd1'} m"><span class=sm1>{GR1[i][0].upper()}</span><div class=nn><div><span>Stock</span><b>{STK1[i]}</b></div><div><span>Orders</span><b>{NEED1[i]}</b></div></div><em class="{'no' if STK1[i] < NEED1[i] else 'ok'}">{f'Short {NEED1[i] - STK1[i]} kg' if STK1[i] < NEED1[i] else f'{STK1[i] - NEED1[i]} kg free'}</em></div>""" for i in range(3))}</div></div>''',
css=f""".w13{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.st{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:6px}}
.st .r{{flex:1;display:grid;grid-template-columns:170px 1fr 110px;gap:16px;align-items:center;border-top:1px solid #eee6d6}}.st .nm{{display:flex;align-items:center;gap:10px}}.st .nm b{{font:700 22px/1.3 Lora}}.st strong{{font:700 26px/1.3 Lora;text-align:right}}
.st .sk{{display:flex;flex-wrap:wrap;gap:7px}}.st .sk i{{width:28px;height:46px;border-radius:9px 9px 6px 6px;box-shadow:inset 0 6px 0 rgba(255,255,255,.25),inset 0 -4px 0 rgba(0,0,0,.12)}}
.bt13{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.bt13 .m{{padding:18px 20px;display:flex;flex-direction:column;gap:10px}}.bt13 .nn{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}.bt13 .nn span{{display:block;margin-bottom:6px;font:500 15px/1.3 'DM Sans';color:{MU1}}}.bt13 .dk1 .nn span{{color:#b9d6cc}}.bt13 .nn b{{font:700 36px/1.2 Lora}}
.bt13 em{{font:700 17px/1.3 'DM Sans';font-style:normal;border-radius:10px;padding:9px 10px;text-align:center}}.bt13 em.ok{{background:#dcefe6;color:{PG1}}}.bt13 em.no{{background:{LP1};color:#fff}}""")

def alloc1():
    left = STK1[:]; out = []
    for b, g, kg in ORD1:
        give = min(kg, left[g]); left[g] -= give; out.append((b, g, kg, give))
    return out, left
AL1, LEFT1 = alloc1()
P["p431_makhana_s4"] = t1(4, "3 · BUYER ORDERS", "Each buyer gets the grade<br><span>they asked for.</span>",
f'''<div class=w14><div class="cd1 ol"><span class=sm1>ORDERS · FILLED IN ORDER OF BOOKING · SAMPLE</span>{"".join(f"""<div class=r><b>{b}</b><span class=g>{gs1(g)}{GR1[g][0]}</span><span>{kg} kg</span><em class="{'ok' if give == kg else 'pt'}">{'Packed' if give == kg else f'{give} kg now'}</em></div>""" for b, g, kg, give in AL1)}</div>
<div class=bt14><div class="dk1 ms"><span class=sm1>MESSAGE TO SAMPLE EXPORTER D</span><p>{AL1[3][3]} kg of 6+ sutta is packed today. The other {AL1[3][2] - AL1[3][3]} kg comes from the next lot, by Sat 28 Nov.</p></div>
<div class="cd1 lf"><span class=sm1>LEFT AFTER ORDERS</span>{"".join(f'<div class=r>{gs1(i)}<span>{GR1[i][0]}</span><b>{LEFT1[i]} kg</b></div>' for i in range(4))}</div></div></div>''',
css=f""".w14{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.ol{{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:4px}}
.ol .r{{flex:1;display:grid;grid-template-columns:1fr 150px 90px 130px;gap:12px;align-items:center;border-top:1px solid #eee6d6}}.ol .r b{{font:700 21px/1.3 'DM Sans'}}.ol .r .g{{display:flex;align-items:center;gap:8px;font:600 18px/1.3 'DM Sans'}}.ol .r>span:nth-child(3){{font:700 21px/1.3 Lora;text-align:right}}
.ol em{{font:700 15px/1.2 'DM Sans';font-style:normal;border-radius:10px;padding:9px 8px;text-align:center}}.ol em.ok{{background:#dcefe6;color:{PG1}}}.ol em.pt{{background:{LP1};color:#fff}}
.bt14{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:16px}}.bt14 .ms{{padding:20px 24px;display:flex;flex-direction:column;gap:10px}}.bt14 .ms p{{font:600 22px/1.45 'DM Sans'}}
.bt14 .lf{{padding:18px 22px;display:flex;flex-direction:column;gap:4px}}.bt14 .lf .r{{display:grid;grid-template-columns:18px 1fr auto;gap:10px;align-items:center;padding:5px 0}}.bt14 .lf span{{font:600 17px/1.3 'DM Sans'}}.bt14 .lf b{{font:700 20px/1.3 Lora}}""")

P["p431_makhana_s5"] = t1(5, "MAKHANA LOT APP", "Process makhana?<br><span>Let's build your lot app.</span>",
f'''<div class=w15><div class=tl15>{"".join(f'<div class=cd1><span class=ib>{ic(i, 38)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("tag", "Lot cards", "Farmer, date, kg"), ("chart", "Grade split", "Per lot, per week"), ("box", "Grade stock", "Kg free after orders"), ("truck", "Buyer orders", "Right grade, on time")])}</div>
<div class="dk1 q15"><span class=sm1>A QUESTION FOR PROCESSORS</span><p>How do you keep track of which lot each grade came from? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{LP1};color:#fff",
css=f""".w15{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl15{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl15>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl15 .ib{{width:84px;height:84px;border-radius:24px;background:#f3d6df;color:{PG1}}}.tl15 b{{font:700 38px/1.25 Lora}}.tl15>div>span:last-child{{font:500 23px/1.4 'DM Sans';color:{MU1}}}
.q15{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q15 p{{font:700 29px/1.4 Lora;text-wrap:pretty}}""")
