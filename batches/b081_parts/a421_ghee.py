
# ───────── 421 INDIA · Desi ghee maker · SINGLE · Lora + Inter · ghee gold / cream / brass brown
# New technique: batch-to-jar allocation — one batch is split into three SVG jar sizes (glass with gold fill + lid + label
# band) with count badges, every order is allocated from it in code, and "left" counts are derived; phone = repeat order.
GO1 = "#d9a21b"; CR1 = "#fbf4e4"; BR1 = "#5b3a12"; TL1 = "#1f6f6a"
BATCH1 = {"1 kg": 10, "500 g": 8, "200 g": 10}
GR1 = {"1 kg": 1000, "500 g": 500, "200 g": 200}
GHEE1 = sum(BATCH1[k] * GR1[k] for k in BATCH1) / 1000
BUT1 = 20
ORD1 = [("Sample Sweet Shop", {"1 kg": 6}, "Picked up today"), ("Online · 4 orders", {"500 g": 4}, "Courier Tue 24 Nov"), ("Sample Store", {"200 g": 10}, "Van round Tue"), ("Sample Home (app)", {"1 kg": 2, "500 g": 1}, "Deliver Wed 25 Nov")]
USED1 = {k: sum(o.get(k, 0) for _, o, _ in ORD1) for k in BATCH1}
LEFT1 = {k: BATCH1[k] - USED1[k] for k in BATCH1}
def jar1(size, w):
    h = {"1 kg": 150, "500 g": 118, "200 g": 88}[size]
    return f'''<svg viewBox="0 0 100 {h + 30}" width="{w}" style="display:block"><rect x="14" y="6" width="72" height="18" rx="5" fill="{BR1}"/><rect x="10" y="22" width="80" height="{h}" rx="16" fill="#f3e9d2" stroke="#c9b48a" stroke-width="2"/>
<rect x="14" y="{22 + h * .18:.0f}" width="72" height="{h * .78:.0f}" rx="12" fill="{GO1}"/><rect x="18" y="{22 + h * .2:.0f}" width="12" height="{h * .6:.0f}" rx="6" fill="#fff" opacity=".35"/>
<rect x="10" y="{22 + h * .42:.0f}" width="80" height="{max(26, h * .26):.0f}" fill="#fffaf0" stroke="{BR1}" stroke-width="1.5"/><rect x="10" y="{22 + h * .42:.0f}" width="80" height="6" fill="{TL1}"/><text x="50" y="{22 + h * .42 + max(26, h * .26) * .5 + 9:.0f}" text-anchor="middle" font-family="Lora" font-weight="700" font-size="{15 if size == "200 g" else 17}" fill="{BR1}"><tspan>B-118</tspan></text></svg>'''
PH1 = f'''<div class=pp1><div class=h1x>Order again</div><div class=cl1>Sample Home · last order 26 Oct</div><span class=rp1>Same as last month</span>
{"".join(f'<div class=r><span>Desi ghee · {k}</span><div class=st><i>−</i><b>{q}</b><i>+</i></div></div>' for k, q in [("1 kg", 2), ("500 g", 1), ("200 g", 0)])}
<div class=f1><span>Deliver on</span><b>Wed 25 Nov · evening</b></div><div class=f1><span>Address</span><b>Flat 4B, Sample Society</b></div><div class=f1><span>Pay</span><b>UPI on delivery</b></div><div class=f1><span>Note</span><b>Leave with the guard if we are out</b></div><div class=bt1>Place order</div></div>'''
P["p421_ghee"] = page(f"""
body{{--f:'Inter';--h:'Lora';background:{CR1};color:{BR1};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{TL1};margin-top:22px}}
h1{{font-family:'Lora';font-weight:700;font-size:62px;line-height:1.22;letter-spacing:-1px;margin-top:20px}} h1 span{{color:#b07d0c}}
.vw1{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:20px;min-height:0}}
.lf1{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm1{{font:700 13px/1.4 Inter;letter-spacing:2px;color:#8a7458}}
.cd1{{background:#fffdf7;border-radius:24px;box-shadow:0 14px 30px rgba(90,60,10,.09);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.eq1{{display:flex;align-items:center;gap:10px}}.eq1 div{{flex:1;background:#f6ead0;border-radius:14px;padding:8px 14px}}.eq1 b{{display:block;font:700 30px/1.35 Lora}}.eq1 span{{font:600 14px/1.3 Inter;color:#8a7458}}.eq1 i{{font:700 26px/1 Inter;font-style:normal;color:{GO1}}}
.jr1{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:10px;align-items:end}}.jr1>div{{display:flex;flex-direction:column;align-items:center;gap:6px}}.jr1 b{{font:700 24px/1.35 Lora}}.jr1 span{{font:600 15px/1.3 Inter;color:#8a7458}}
.lb1{{display:flex;justify-content:space-between;align-items:center;background:{TL1};color:#fff;border-radius:12px;padding:9px 14px;font:600 15px/1.3 Inter}}.lb1 b{{font-weight:800}}
.or1{{flex:1}}.or1 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid #efe3c8}}.or1 .r b{{display:block;font:700 20px/1.3 Inter}}.or1 .r em{{display:inline-block;margin-top:6px;font:700 13px/1.2 Inter;font-style:normal;background:#e1efed;color:{TL1};border-radius:8px;padding:5px 9px}}.or1 .r>span{{font-size:19px!important;color:{BR1}!important;font-weight:700!important}}.or1 .r span{{font:600 17px/1.3 Inter;color:#8a7458;text-align:right}}
.lt1{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.lt1 div{{background:{BR1};color:#fff;border-radius:16px;padding:10px 14px}}.lt1 b{{display:block;font:700 32px/1.35 Lora;color:#f2c94c}}.lt1 span{{font:600 14px/1.3 Inter;color:#e6d5b5}}
.ph1{{display:flex;align-items:center}}.pp1{{flex:1;display:flex;flex-direction:column;gap:11px;padding:8px 16px 18px;background:#fffdf7}}.h1x{{font:700 22px/1.3 Lora}}.cl1{{font:600 14px/1.3 Inter;color:#8a7458;margin-top:-6px}}
.rp1{{align-self:flex-start;font:700 14px/1.2 Inter;background:#e1efed;color:{TL1};border-radius:10px;padding:8px 11px}}
.pp1 .r{{background:#fff;border:1.5px solid #ecdcbc;border-radius:14px;padding:12px;display:flex;justify-content:space-between;align-items:center}}.pp1 .r span{{font:700 15px/1.3 Inter}}
.st{{display:flex;align-items:center;gap:7px}}.st i{{width:28px;height:28px;border-radius:9px;background:{BR1};color:#fff;font:800 17px/28px Inter;font-style:normal;text-align:center}}.st b{{font:700 19px/1.2 Lora;width:28px;text-align:center}}
.f1{{display:flex;flex-direction:column;gap:3px;background:#fff;border:1.5px solid #ecdcbc;border-radius:14px;padding:9px 12px}}.f1 span{{font:700 12px/1.3 Inter;letter-spacing:1px;color:#8a7458;text-transform:uppercase}}.f1 b{{font:700 15px/1.35 Inter}}
.bt1{{margin-top:auto;background:{GO1};color:{BR1};border-radius:14px;padding:13px;text-align:center;font:800 16px/1.2 Inter}}
""", "<div class=kk>DESI GHEE MAKER · JARS AND TINS</div><h1>Ghee orders in a diary?<br><span>Every jar, batch and order.</span></h1>",
f'''<div class=vw1><div class=lf1><div class=cd1 style="flex:1.25"><span class=sm1>TODAY'S BATCH · B-118 · SAMPLE</span>
<div class=eq1><div><b>{BUT1} kg</b><span>butter in</span></div><i>→</i><div><b>{GHEE1:g} kg</b><span>ghee out</span></div><i>→</i><div><b>{sum(BATCH1.values())}</b><span>jars and tins</span></div></div>
<div class=jr1>{"".join(f'<div>{jar1(k, {"1 kg": 120, "500 g": 104, "200 g": 88}[k])}<b>{q} × {k}</b><span>{LEFT1[k]} left after orders</span></div>' for k, q in BATCH1.items())}</div>
<div class=lb1><span>Every label: <b>Batch B-118</b></span><span>Packed Mon 23 Nov 2026</span></div></div>
<div class="cd1 or1"><span class=sm1>ORDERS FROM B-118</span>{"".join(f'<div class=r><div><b>{n}</b><em>{st}</em></div><span>{" + ".join(f"{q} × {k}" for k, q in o.items())}</span></div>' for n, o, st in ORD1)}</div></div>
<div class=ph1>{phone(PH1, w=330, h=720)}</div></div>''',
BR1, "Make ghee? DM us", f"background:{BR1};color:#f2c94c")
