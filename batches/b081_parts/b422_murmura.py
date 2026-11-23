
# ───────── 422 INDIA · Puffed rice (murmura) maker · CAROUSEL 5 · TeX Gyre Adventor + Roboto · rice white / turmeric / indigo
# New technique: clear plastic bags filled with seeded puffed-rice grains (SVG clipPath), a shop × day standing-order
# matrix whose Tuesday column drives the roast plan (rice needed, batches on a time ribbon) and the delivery round.
TU2 = "#e0a526"; IN2 = "#2d3a7a"; BG2 = "#f7f4ec"; K2 = "#1e2233"
SH2 = ["Sample Kirana A", "Sample Bhel Cart B", "Sample Snack Shop C", "Sample Kirana D", "Sample Hotel E"]
DY2 = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
MX2 = [[6, 6, 6, 6, 8, 8], [4, 4, 4, 4, 6, 6], [3, 3, 0, 3, 3, 4], [5, 5, 5, 5, 5, 6], [2, 2, 2, 2, 3, 3]]
TUE2 = sum(r[1] for r in MX2); BAG2 = 5; KG2 = TUE2 * BAG2
RICE2 = math.ceil(KG2 / 0.9); BSZ2 = 25; NB2 = math.ceil(RICE2 / BSZ2)
def bag2(seed, w=200, lab="5 kg"):
    rnd = random.Random(seed)
    gr = "".join(f'<ellipse cx="{rnd.uniform(26, 154):.1f}" cy="{rnd.uniform(70, 236):.1f}" rx="{rnd.uniform(5, 7):.1f}" ry="{rnd.uniform(2.6, 3.6):.1f}" transform="rotate({rnd.randint(0, 180)} {rnd.uniform(26, 154):.0f} {rnd.uniform(70, 236):.0f})" fill="{rnd.choice(["#fffdf6", "#f4ead2", "#efe1c0"])}" stroke="#d6c39a" stroke-width=".8"/>' for _ in range(420))
    return f'''<svg viewBox="0 0 180 260" width="{w}" style="display:block"><defs><clipPath id="bg2{seed}"><path d="M20 60 Q20 50 30 48 L150 48 Q160 50 160 60 L164 238 Q164 252 150 252 L30 252 Q16 252 16 238 Z"/></clipPath></defs>
<path d="M58 48 Q70 18 90 14 Q110 18 122 48 Z" fill="#e9eef7" stroke="#b8c2d6" stroke-width="2"/><rect x="74" y="22" width="32" height="10" rx="4" fill="{IN2}"/>
<path d="M20 60 Q20 50 30 48 L150 48 Q160 50 160 60 L164 238 Q164 252 150 252 L30 252 Q16 252 16 238 Z" fill="#fbf7ec"/><g clip-path="url(#bg2{seed})">{gr}</g>
<path d="M20 60 Q20 50 30 48 L150 48 Q160 50 160 60 L164 238 Q164 252 150 252 L30 252 Q16 252 16 238 Z" fill="#dfe8f5" fill-opacity=".18" stroke="#b8c2d6" stroke-width="2.5"/><rect x="30" y="70" width="14" height="150" rx="7" fill="#fff" opacity=".45"/>
<rect x="56" y="134" width="68" height="40" rx="8" fill="{TU2}"/><text x="90" y="161" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="20" fill="{K2}"><tspan>{lab}</tspan></text></svg>'''
B2 = f"""
body{{--f:'Roboto';--h:'TeX Gyre Adventor';background:{BG2};color:{K2}}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{IN2};margin-top:22px;align-self:flex-start}}
h1{{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;line-height:1.22;letter-spacing:-1.5px;margin-top:18px}} h1 span{{color:#b07f0e}}
.sm2{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#6d6a5e}}
.cd2{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(30,34,51,.08)}}
.dk2{{background:{IN2};color:#fff;border-radius:24px}}.dk2 .sm2{{color:#c3cbec}}
"""
def t2(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{IN2};color:#fff"):
    return page(B2 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, K2, cta, ctacss, tagline=f"{n} / 5")

QT2 = [("“Same as last week.”", "How many bags?"), ("“Send 2 extra on Friday.”", "Big bags or small?"), ("“The last bag was soft.”", "Which batch was it?")]
P["p422_puff_s1"] = t2(1, "MURMURA MAKER · SHOP AND CART ORDERS", "Murmura orders by memory?<br><span>Bags and rounds, on record.</span>",
f'''<div class=w21><div class=tp21><div class="cd2 bg21"><span class=sm2>TOMORROW · {TUE2} BAGS OF 5 KG · SAMPLE</span><div class=bs21>{"".join(bag2(s, 190) for s in (3, 8, 13, 21))}</div></div>
<div class=qs21>{"".join(f'<div class="cd2 q"><p>{a}</p><em>{b}</em></div>' for a, b in QT2)}</div></div>
<div class="dk2 bt21"><b>{len(SH2)} shops × {len(DY2)} days</b><span>= {len(SH2) * len(DY2)} standing orders, all kept in one person's head.</span></div></div>''',
css=f""".w21{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tp21{{flex:1;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:16px;min-height:0}}
.bg21{{padding:18px 20px;display:flex;flex-direction:column;gap:10px}}.bs21{{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:6px 18px;align-items:center;justify-items:center}}.bs21 svg{{width:auto!important;height:100%!important;max-height:330px;max-width:100%}}
.qs21{{display:flex;flex-direction:column;gap:14px}}.qs21 .q{{flex:1;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:12px}}.qs21 p{{font:700 30px/1.35 'TeX Gyre Adventor'}}
.qs21 em{{align-self:flex-start;font:700 19px/1.2 Roboto;font-style:normal;border:2px dashed {TU2};color:#8a620a;border-radius:10px;padding:8px 12px}}
.bt21{{padding:20px 26px;display:flex;align-items:baseline;gap:14px;flex-wrap:wrap}}.bt21 b{{font:700 34px/1.3 'TeX Gyre Adventor';color:{TU2}}}.bt21 span{{font:500 22px/1.4 Roboto}}""")

P["p422_puff_s2"] = t2(2, "1 · ORDER BOOK", "Every shop, every day.<br><span>One standing order book.</span>",
f'''<div class=w22><div class="cd2 mx22"><div class="r hd"><span>5 KG BAGS · SAMPLE</span>{"".join(f'<span class="{"tu" if d == "Tue" else ""}">{d}</span>' for d in DY2)}<span>Week</span></div>
{"".join(f'<div class=r><b>{s}</b>{"".join(f"<i class={chr(34)}{chr(32).join(c for c in ['tu' if j == 1 else '', 'z' if v == 0 else ''] if c)}{chr(34)}>{v if v else '—'}</i>" for j, v in enumerate(r))}<strong>{sum(r)}</strong></div>' for s, r in zip(SH2, MX2))}
<div class="r ft2"><b>Bags a day</b>{"".join(f"<i class={chr(34)}{'tu' if j == 1 else ''}{chr(34)}>{sum(r[j] for r in MX2)}</i>" for j in range(6))}<strong>{sum(map(sum, MX2))}</strong></div></div>
<div class=nt22><div class="cd2 n"><span class=sm2>A SHOP CALLS</span><p>“No murmura on Wednesday.” Snack Shop C's Wednesday is set to zero. Everyone sees it.</p></div><div class="dk2 n"><span class=sm2>TOMORROW · TUE 24 NOV</span><b>{TUE2} bags</b><span>{KG2} kg to make tonight</span></div></div></div>''',
css=f""".w22{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.mx22{{flex:1;padding:14px 20px;display:flex;flex-direction:column;min-height:0}}
.mx22 .r{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) repeat(6,62px) 70px;gap:6px;align-items:center;border-top:1px solid #ece6d6}}.mx22 .r.hd{{flex:none;border:0;padding-bottom:6px}}.mx22 .r.hd span{{font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#6d6a5e;text-align:center}}.mx22 .r.hd span:first-child{{text-align:left}}
.mx22 .r.hd span.tu{{background:{TU2};color:{K2};border-radius:8px;padding:4px 0}}.mx22 b{{font:700 19px/1.3 Roboto}}
.mx22 i{{font:700 24px/1.4 'TeX Gyre Adventor';font-style:normal;text-align:center;border-radius:10px;padding:6px 0}}.mx22 i.tu{{background:#fbecc4}}.mx22 i.z{{color:#b8b2a0}}.mx22 strong{{font:700 22px/1.4 'TeX Gyre Adventor';text-align:center;color:{IN2}}}
.mx22 .r.ft2{{background:{IN2};border-radius:14px;border:0;margin-top:6px;padding:0 10px;color:#fff}}.mx22 .ft2 i.tu{{background:{TU2};color:{K2}}}.mx22 .ft2 strong{{color:{TU2}}}
.nt22{{display:grid;grid-template-columns:1.2fr .8fr;gap:16px}}.nt22 .n{{padding:18px 22px;display:flex;flex-direction:column;gap:6px}}.nt22 p{{font:600 22px/1.4 Roboto;text-wrap:pretty}}.nt22 b{{font:700 46px/1.3 'TeX Gyre Adventor';color:{TU2}}}.nt22 .dk2>span:last-child{{font:500 18px/1.3 Roboto}}""")

BT2 = []
t = 4 * 60
for k in range(NB2):
    kg = min(BSZ2, RICE2 - k * BSZ2); d = round(45 * kg / BSZ2)
    BT2.append((k + 1, kg, t, t + d)); t += d
def hm2(m): return f"{m // 60}:{m % 60:02d}"
S0, S1 = 4 * 60, 8 * 60
P["p422_puff_s3"] = t2(3, "2 · ROAST PLAN", "How much rice tonight?<br><span>The plan works it out.</span>",
f'''<div class=w23><div class=eq23>{"".join(f'<div class="cd2{" hi" if i == 3 else ""}"><b>{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([(f"{TUE2} bags", "for Tuesday"), (f"{KG2} kg", f"murmura ({BAG2} kg a bag)"), (f"{RICE2} kg", "rice (10 kg rice → 9 kg murmura)"), (f"{NB2} batches", f"of up to {BSZ2} kg rice")]))}</div>
<div class="cd2 rb23"><span class=sm2>ROASTER · TUE 24 NOV · 4 AM TO 8 AM · SAMPLE</span><div class=rbx>{"".join(f'<div class=bk style="left:{(a - S0) / (S1 - S0) * 100:.2f}%;width:{(b - a) / (S1 - S0) * 100:.2f}%"><b>B{n}</b></div>' for n, kg, a, b in BT2)}<div class="bk pk" style="left:{(BT2[-1][3] + 5 - S0) / (S1 - S0) * 100:.2f}%;width:{(S1 - BT2[-1][3] - 5) / (S1 - S0) * 100:.2f}%"><b>Pack</b></div></div>
<div class=ax>{"".join(f'<span style="left:{(h * 60 - S0) / (S1 - S0) * 100:.2f}%">{h} AM</span>' for h in (4, 5, 6, 7, 8))}</div></div>
<div class="cd2 bl23"><div class="r hd"><span>BATCH</span><span>RICE</span><span>TIME</span><span>MURMURA</span></div>{"".join(f'<div class=r><b>B{n}</b><span>{kg} kg</span><span>{hm2(a)} to {hm2(b)} AM</span><span>≈ {kg * 0.9:g} kg</span></div>' for n, kg, a, b in BT2)}</div></div>''',
css=f""".w23{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.eq23{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}.eq23>div{{padding:14px 16px;display:flex;flex-direction:column;gap:4px}}.eq23 b{{font:700 32px/1.3 'TeX Gyre Adventor';color:{IN2}}}.eq23 span{{font:500 16px/1.35 Roboto;color:#6d6a5e}}.eq23 .hi{{background:{IN2}}}.eq23 .hi b{{color:{TU2}}}.eq23 .hi span{{color:#dfe3f5}}
.rb23{{padding:16px 20px 10px;display:flex;flex-direction:column;gap:10px}}.rbx{{position:relative;height:74px;background:#f1ede2;border-radius:12px;overflow:hidden}}.rbx .bk{{position:absolute;top:0;bottom:0;background:{TU2};border-right:3px solid #fff;display:flex;align-items:center;justify-content:center}}.rbx .bk b{{font:700 20px/1.3 'TeX Gyre Adventor'}}.rbx .bk.pk{{background:{IN2};color:#fff}}
.ax{{position:relative;height:22px}}.ax span{{position:absolute;top:0;transform:translateX(-50%);font:600 14px/1.4 Roboto;color:#6d6a5e;white-space:nowrap}}.ax span:first-child{{transform:none}}.ax span:last-child{{transform:translateX(-100%)}}
.bl23{{flex:1;padding:14px 20px;display:flex;flex-direction:column}}.bl23 .r{{flex:1;display:grid;grid-template-columns:110px 110px 1fr 160px;gap:10px;align-items:center;border-top:1px solid #ece6d6}}.bl23 .r.hd{{flex:none;border:0;padding-bottom:6px}}.bl23 .r.hd span{{font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#6d6a5e}}
.bl23 b{{font:700 26px/1.3 'TeX Gyre Adventor';color:{IN2}}}.bl23 .r span{{font:600 20px/1.3 Roboto}}""")

ST2 = [("8:50", "Sample Kirana A", 0, "Paid · UPI"), ("9:10", "Sample Snack Shop C", 2, "Weekly bill · Sat"), ("9:25", "Sample Bhel Cart B", 1, "Paid · UPI"), ("9:45", "Sample Kirana D", 3, "Paid · UPI"), ("10:05", "Sample Hotel E", 4, "Weekly bill · Sat")]
PAID2 = sum(1 for s in ST2 if s[3].startswith("Paid"))
P["p422_puff_s4"] = t2(4, "3 · DELIVERY ROUND", "One van, five stops.<br><span>Every bag counted out.</span>",
f'''<div class=w24><div class="cd2 rt24"><div class="st first"><i></i><b>8:30</b><span>Van leaves with {TUE2} bags</span></div>
{"".join(f'<div class=st><i></i><b>{tm}</b><span>{nm}</span><strong>{MX2[ix][1]} bags</strong><em class="{"pd" if s.startswith("Paid") else ""}">{s}</em></div>' for tm, nm, ix, s in ST2)}</div>
<div class=sm24>{"".join(f'<div class="{c}"><b>{a}</b><span>{b}</span></div>' for c, a, b in [("cd2", str(sum(MX2[ix][1] for _, _, ix, _ in ST2)), "bags delivered"), ("cd2", str(PAID2), "paid on the spot"), ("dk2", str(len(ST2) - PAID2), "on the Saturday bill")])}</div></div>''',
css=f""".w24{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.rt24{{flex:1;padding:16px 24px;display:flex;flex-direction:column;position:relative}}
.rt24 .st{{flex:1;display:grid;grid-template-columns:40px 90px 1fr 110px 190px;gap:12px;align-items:center;position:relative}}
.rt24 .st i{{width:22px;height:22px;border-radius:50%;background:{TU2};border:4px solid #fff;box-shadow:0 0 0 3px {TU2};justify-self:center;z-index:1}}.rt24 .st.first i{{background:{IN2};box-shadow:0 0 0 3px {IN2}}}
.rt24 .st:not(:last-child)::after{{content:"";position:absolute;left:19px;top:50%;height:100%;width:3px;background:repeating-linear-gradient(180deg,#d9cfb4 0 8px,transparent 8px 14px)}}
.rt24 .st b{{font:700 24px/1.3 'TeX Gyre Adventor';color:{IN2}}}.rt24 .st span{{font:600 21px/1.3 Roboto}}.rt24 .st strong{{font:700 22px/1.3 'TeX Gyre Adventor';text-align:right}}
.rt24 .st em{{font:700 15px/1.2 Roboto;font-style:normal;text-align:center;border-radius:10px;padding:9px 6px;background:#fbecc4;color:#8a620a}}.rt24 .st em.pd{{background:#e3e7f6;color:{IN2}}}
.sm24{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.sm24>div{{padding:16px 20px;display:flex;flex-direction:column;gap:2px}}.sm24 b{{font:700 46px/1.3 'TeX Gyre Adventor';color:{IN2}}}.sm24 .dk2 b{{color:{TU2}}}.sm24 span{{font:500 18px/1.3 Roboto}}""")

P["p422_puff_s5"] = t2(5, "MURMURA ORDER APP", "Make murmura or poha?<br><span>Let's build your order app.</span>",
f'''<div class=w25><div class=tl25>{"".join(f'<div class=cd2><span class=ib>{ic(i, 38)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("grid", "Order book", "Shops × days"), ("clock", "Roast plan", "Rice and batches"), ("truck", "Van round", "Stops in order"), ("rupee", "Paid or bill", "Per shop, per week")])}</div>
<div class="dk2 q25"><span class=sm2>A QUESTION FOR MURMURA MAKERS</span><p>How do you remember which shop wants how many bags on which day? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{TU2};color:{K2}",
css=f""".w25{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl25{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl25>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl25 .ib{{width:84px;height:84px;border-radius:24px;background:{TU2};color:{K2}}}.tl25 b{{font:700 40px/1.3 'TeX Gyre Adventor'}}.tl25>div>span:last-child{{font:500 23px/1.4 Roboto;color:#6d6a5e}}
.q25{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q25 p{{font:700 31px/1.4 'TeX Gyre Adventor';text-wrap:pretty}}""")
