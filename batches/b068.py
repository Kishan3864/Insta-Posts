import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 356 INDIA · Biryani handi orders · SINGLE · Lora + Roboto · saffron / handi copper / mint
# New technique: top-down SVG handis (copper rim, dough seal ring, saffron rice) sized by kg (area ∝ kg) standing on
# a wooden pickup counter in time order; the kitchen totals and advance chips come from the same order list.
ORD = [("O-1", "Office lunch", "Chicken", 5, "11:30 AM", True), ("O-2", "Family lunch", "Veg", 2, "12:00 PM", True),
       ("O-3", "Birthday party", "Chicken", 10, "12:30 PM", False), ("O-4", "Flat 302", "Mutton", 2, "1:00 PM", True),
       ("O-5", "Team lunch", "Veg", 3, "1:30 PM", True), ("O-6", "Get-together", "Chicken", 4, "2:00 PM", False)]
TC = {"Chicken": "#e07b1a", "Veg": "#2f8f6a", "Mutton": "#a5532a"}
def handi(kg, c):
    r = 34 * math.sqrt(kg); W = 2 * r + 20
    return (f'<svg viewBox="0 0 {W:.0f} {W:.0f}" style="width:{W*0.62:.0f}px;display:block">'
            f'<circle cx="{W/2}" cy="{W/2}" r="{r+6}" fill="#7a3b1c"/><circle cx="{W/2}" cy="{W/2}" r="{r}" fill="#c06a35"/>'
            f'<circle cx="{W/2}" cy="{W/2}" r="{r*0.82}" fill="#f2dcb0" stroke="#e6c48a" stroke-width="5" stroke-dasharray="7 5"/>'
            f'<circle cx="{W/2}" cy="{W/2}" r="{r*0.6}" fill="{c}" opacity=".9"/><circle cx="{W/2-r*0.18}" cy="{W/2-r*0.2}" r="{r*0.16}" fill="#fff4dc" opacity=".55"/></svg>')
TOT = {t: sum(o[3] for o in ORD if o[2] == t) for t in TC}
PEND = [o for o in ORD if not o[5]]
from collections import Counter; HS = Counter(o[3] for o in ORD)
P["p356_biryani"] = page("""
body{--f:'Roboto';--h:'Lora';background:#fff4e6;color:#2d1d12}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#c4600d;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:64px;line-height:1.22;letter-spacing:-1px} h1 span{color:#2f8f6a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ct6{background:#fff;border-radius:26px;padding:16px 22px 0;box-shadow:0 12px 28px rgba(45,29,18,.08);display:flex;flex-direction:column}
.ct6>small,.ol6>small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#8a6f5a}
.hl6{display:flex;justify-content:space-between;align-items:flex-end;padding:10px 6px 0;min-height:200px}
.hd6{display:flex;flex-direction:column;align-items:center;gap:6px}
.hd6 b{font:700 22px/1.3 Lora}.hd6 em{font:600 14px/1.3 Roboto;font-style:normal;color:#6e5747}
.cn6{height:24px;margin:8px -22px 0;border-radius:0 0 26px 26px;background:repeating-linear-gradient(90deg,#b07a4a 0 46px,#a16d40 46px 50px)}
.bt6{flex:1;display:grid;grid-template-columns:1.45fr 1fr;gap:14px;min-height:0}
.ol6{background:#fff;border-radius:26px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 12px 28px rgba(45,29,18,.08)}
.or6{flex:1;display:grid;grid-template-columns:84px 1fr 66px 118px;gap:10px;align-items:center;border-bottom:1px solid #f3e7da}.or6:last-child{border:0}
.or6>strong{font:700 17px/1.3 Roboto;color:#6e5747}.or6 div b{display:block;font:700 22px/1.3 Lora}.or6 div span{font:500 16px/1.35 Roboto;color:#6e5747}
.or6>em{font:700 20px/1.3 Roboto;font-style:normal;text-align:right}
.or6>i{font:700 15px/1.3 Roboto;font-style:normal;text-align:center;border-radius:8px;padding:6px 4px;background:#e2f3ea;color:#1f6b4d}.or6>i.pn{background:#fde6cf;color:#9a4a08}
.kt6{background:#2d1d12;color:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.kt6 small{margin-top:4px;font:700 13px/1.4 Roboto;letter-spacing:2px;color:#f6c48b}
.tr6{display:flex;align-items:center;gap:12px;background:rgba(255,255,255,.08);border-radius:14px;padding:10px 14px}.tr6 i{width:18px;height:18px;border-radius:50%;flex:none}.tr6 span{flex:1;font:500 18px/1.3 Roboto}.tr6 b{font:700 28px/1.3 Lora}
.sz6{display:flex;flex-wrap:wrap;gap:8px}.sz6 i{font:700 17px/1.3 Roboto;font-style:normal;border:2px solid #6e5240;border-radius:10px;padding:6px 10px}.sz6 i.op{border:2px dashed #f6c48b;color:#f6c48b}
.kt6 p{margin-top:auto;background:#c4600d;border-radius:14px;padding:12px 14px;font:500 16px/1.45 Roboto}
""", "<div class=kk>BIRYANI · SUNDAY HANDI ORDERS</div><h1>Handi orders on WhatsApp?<br><span>See every kg before you cook.</span></h1>",
f'''<div class=vw><div class=ct6><small>SUNDAY PICKUP COUNTER · SIZE = KG · SAMPLE</small><div class=hl6>{"".join(f'<div class=hd6>{handi(o[3], TC[o[2]])}<b>{o[3]} kg</b><em>{o[4]}</em></div>' for o in ORD)}</div><div class=cn6></div></div>
<div class=bt6><div class=ol6><small>ORDERS · SUN 29 NOV</small>{"".join(f'<div class=or6><strong>{o[4]}</strong><div><b>{o[1]}</b><span>{o[0]} · {o[2]}</span></div><em>{o[3]} kg</em><i class="{"" if o[5] else "pn"}">{"Advance paid" if o[5] else "Advance due"}</i></div>' for o in ORD)}</div>
<div class=kt6><small>KITCHEN SHEET · {sum(TOT.values())} KG</small>{"".join(f'<div class=tr6><i style="background:{TC[t]}"></i><span>{t}</span><b>{v} kg</b></div>' for t,v in TOT.items())}
<small>HANDIS TO PREP</small><div class=sz6>{"".join(f"<i>{k} kg × {v}</i>" for k,v in sorted(HS.items(), reverse=True))}</div>
<small>OPEN PICKUP SLOTS</small><div class=sz6><i class=op>2:30 PM</i><i class=op>3:00 PM</i></div>
<p>Advance due: {" and ".join(o[0] for o in PEND)}. The UPI link goes out on Friday.</p></div></div></div>''',
"#2d1d12", "Take biryani orders? DM us", "background:#2f8f6a;color:#fff")


# ───────── 357 INDIA · Agri input shop (fertilizer + seed) · CAROUSEL 5 · Montserrat + Source Sans 3 · loam brown / sprout green / sack cream
# New techniques: isometric SVG godown stacks (cuboids with one line per 10 bags, height ∝ bags) and a round
# double-ring "CLEARED" stamp (SVG textPath) in its own cell beside the slip. Ledger, stock and reminders share data.
LED = [("3 Nov", "Wheat seed, 40 kg bag", 1, "UPI"), ("10 Nov", "DAP, 50 kg bag", 2, "Credit"),
       ("17 Nov", "Urea, 45 kg bag", 2, "Credit"), ("21 Nov", "Zinc, 5 kg pack", 1, "UPI")]
TAKEN = sum(e[2] for e in LED); CRED = sum(e[2] for e in LED if e[3] == "Credit"); PAIDN = TAKEN - CRED
CRED_TXT = ", ".join(f"{e[1].split(',')[0]} {e[2]}" for e in LED if e[3] == "Credit")
STK = [("Urea", "45 kg bags", 120, 70, "#e9e4d6"), ("DAP", "50 kg bags", 64, 40, "#d8c3a0"), ("Wheat seed", "40 kg bags", 38, 20, "#c9d9a8"),
       ("Potash", "50 kg bags", 14, 18, "#e3b9a4"), ("Zinc", "5 kg packs", 46, 10, "#cfd6dc")]
LOW = [x for x in STK if x[2] < x[3] * 1.2]
VIL = [("Village A", 18, 61), ("Village B", 11, 37), ("Village C", 9, 28)]
NF = sum(v[1] for v in VIL)
def iso(stk, H=330, unit=2.1, w=86, d=34, gap=150):
    W = 40 + gap * (len(stk) - 1) + w + d + 30
    s = f'<svg viewBox="0 0 {W} {H}" class=iso style="width:100%;display:block"><path d="M10 {H-40} L{W-10} {H-40} L{W-10-d} {H-6} L{10+d*0} {H-6} Z" fill="#e6dcc7"/>'
    for i, (n, u, b, bk, c) in enumerate(stk):
        x = 30 + i * gap; y0 = H - 42; h = b * unit; top = y0 - h
        lo = b < bk * 1.2
        s += f'<path d="M{x} {y0} L{x} {top} L{x+w} {top} L{x+w} {y0} Z" fill="{c}" stroke="#6b4a2f" stroke-width="2.5"/>'
        s += f'<path d="M{x+w} {y0} L{x+w} {top} L{x+w+d} {top-d*0.6} L{x+w+d} {y0-d*0.6} Z" fill="{c}" stroke="#6b4a2f" stroke-width="2.5" style="filter:brightness(.82)"/>'
        s += f'<path d="M{x} {top} L{x+d} {top-d*0.6} L{x+w+d} {top-d*0.6} L{x+w} {top} Z" fill="{c}" stroke="#6b4a2f" stroke-width="2.5" style="filter:brightness(1.07)"/>'
        for k in range(1, math.ceil(b / 10)):
            yy = y0 - k * 10 * unit
            s += f'<path d="M{x} {yy} L{x+w} {yy} L{x+w+d} {yy-d*0.6}" fill="none" stroke="#6b4a2f" stroke-width="1.4" opacity=".55"/>'
        s += f'<text x="{x+(w+d)/2}" y="{top-d*0.6-12}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="24" fill="{"#c0392b" if lo else "#2d2a1f"}">{b}</text>'
    return s + "</svg>"
def stamp(txt="CLEARED", sub="20 NOV 2026", c="#2f7d32", sz=210):
    return (f'<svg viewBox="0 0 200 200" style="width:{sz}px;display:block"><defs><path id="sc" d="M26 100 A74 74 0 0 1 174 100"/></defs>'
            f'<circle cx="100" cy="100" r="94" fill="none" stroke="{c}" stroke-width="6"/><circle cx="100" cy="100" r="66" fill="none" stroke="{c}" stroke-width="3"/>'
            f'<text font-family="Montserrat" font-weight="800" font-size="13" letter-spacing="1.5" fill="{c}" text-anchor="middle"><textPath href="#sc" startOffset="50%">SAMPLE AGRI SHOP</textPath></text>'
            f'<rect x="14" y="80" width="172" height="40" rx="4" fill="#fffdf6" stroke="{c}" stroke-width="4"/><text x="100" y="109" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="26" fill="{c}">{txt}</text>'
            f'<text x="100" y="142" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="13" fill="{c}">{sub}</text></svg>')
AG = """
body{--f:'Source Sans 3';--h:'Montserrat';background:#f4efe3;color:#2d2a1f}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#4f8a1f;margin-top:22px;margin-bottom:4px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#8a5a33}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(45,42,31,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7a715e}
.nb{display:flex;align-items:center;gap:14px;background:#2d2a1f;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 'Source Sans 3'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#8cc63f;color:#2d2a1f}.nb b{color:#b9e07a}
"""
def ag(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2d2a1f;color:#b9e07a"):
    return page(AG + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2d2a1f", cta, ctacss, tagline=f"{n} / 5")
NBK = [("KHARIF 2026", "#b5543c", ["DAP 2 bags", "Urea 3 → 5?", "paid half"]), ("RABI", "#3f6e8c", ["Seed 1 bag", "Urea 2", "cash or credit?"]),
       ("VILLAGE B", "#5d7d2a", ["Potash 1", "DAP 2 ✓", "Urea 4 → 3?"]), ("LOOSE PAGES", "#8a6a2f", ["Zinc 1 pack", "who took 2?", "page torn"])]
P["p357_agri_s1"] = ag(1, "FERTILIZER AND SEED SHOP · FARMER CREDIT", "Credit till harvest?<br><span>4 notebooks, no answer.</span>",
f'''<div class=w1>{"".join(f'<div class=nk1 style="--c:{c};transform:rotate({r}deg)"><div class=lb1>{l}</div>{"".join(f"<p class={chr(34)}{"q" if "?" in t else ""}{chr(34)}>{t}</p>" for t in ts)}</div>' for (l,c,ts),r in zip(NBK,[-3,2,2.5,-2]))}
<div class=bb1><span class=vn>{ic("chat",22)} A farmer at the counter</span><p>“I took 3 bags of urea, not 5. Check your book again.”</p></div></div>''',
css=""".w1{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr auto;gap:26px 30px;min-height:0;padding:10px 12px 0}
.nk1{background:#fffdf6;border-radius:10px 18px 18px 10px;border-left:22px solid var(--c);padding:16px 22px;box-shadow:0 12px 24px rgba(45,42,31,.12);display:flex;flex-direction:column;justify-content:space-around;background-image:repeating-linear-gradient(180deg,transparent 0 46px,#dfe6ef 46px 48px)}
.lb1{align-self:flex-start;background:var(--c);color:#fff;font:800 16px/1.3 Montserrat;letter-spacing:1.5px;border-radius:6px;padding:5px 10px}
.nk1 p{font:italic 600 27px/1.35 'Source Sans 3';color:#3a3a50}.nk1 p.q{color:#c0392b;text-decoration:underline wavy;text-decoration-thickness:2px;text-underline-offset:6px}
.bb1{grid-column:1 / 3;background:#2d2a1f;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 'Source Sans 3';color:#b9e07a;margin-bottom:6px}.bb1 p{font:500 25px/1.4 'Source Sans 3'}""")

P["p357_agri_s2"] = ag(2, "STEP 1 · ONE LEDGER FOR EACH FARMER", "Every bag written once,<br><span>paid or on credit.</span>",
f'''<div class=w2><div class="cd lg2"><div class=hh2><div><b>Farmer 12</b><span>Village A · wheat, 2 acres · sample</span></div><small class=cap>RABI 2026</small></div>
<div class="rr2 hd2"><span>DATE</span><span>ITEM</span><span>QTY</span><span>PAID BY</span></div>
{"".join(f'<div class=rr2><strong>{d}</strong><b>{it}</b><em>{q}</em><i class="{"cr" if pb=="Credit" else ""}">{pb}</i></div>' for d,it,q,pb in LED)}
<div class=tl2><div><small>TAKEN</small><b>{TAKEN}</b></div><div><small>PAID BY UPI</small><b>{PAIDN}</b></div><div class=cr><small>ON CREDIT · DUE AT HARVEST</small><b>{CRED}</b></div></div></div>
<div class=nb><span class=ib>{ic("send",26)}</span><span>Each entry goes to the farmer on WhatsApp the same day. <b>No more “3 or 5 bags?”</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.lg2{flex:1;padding:18px 26px;display:flex;flex-direction:column;gap:6px}
.hh2{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:8px}.hh2 b{display:block;font:800 34px/1.3 Montserrat}.hh2 span{font:500 19px/1.4 'Source Sans 3';color:#7a715e}
.rr2{flex:1;display:grid;grid-template-columns:110px 1fr 70px 130px;gap:14px;align-items:center;border-bottom:1px solid #efe9dc}
.hd2{flex:none;font:700 14px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#7a715e;border-bottom:2px solid #2d2a1f;padding-bottom:6px}
.rr2 strong{font:600 22px/1.3 'Source Sans 3';color:#7a715e}.rr2 b{font:700 28px/1.3 'Source Sans 3'}.rr2 em{font:800 32px/1.3 Montserrat;font-style:normal}
.rr2 i{font:700 18px/1.3 'Source Sans 3';font-style:normal;text-align:center;border-radius:10px;padding:8px 0;background:#e6f2d6;color:#3d6f14}.rr2 i.cr{background:#f7e1d3;color:#9a4a1c}
.tl2{display:grid;grid-template-columns:1fr 1fr 1.6fr;gap:12px;margin-top:8px}.tl2 div{background:#f4efe3;border-radius:16px;padding:12px 16px}.tl2 small{display:block;font:700 13px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#7a715e}.tl2 b{font:800 40px/1.3 Montserrat}
.tl2 .cr{background:#8a5a33;color:#fff}.tl2 .cr small{color:#f3d9c2}""")

P["p357_agri_s3"] = ag(3, "STEP 2 · GODOWN STOCK VS BOOKINGS", "Know what runs out<br><span>before farmers ask.</span>",
f'''<div class=w3><div class="cd gd3"><small class=cap>GODOWN · BAGS IN STOCK · SAMPLE</small>{iso(STK, H=400, unit=2.3)}
<div class=lb3>{"".join(f'<div><b>{n}</b><span>{u}</span></div>' for n,u,b,bk,c in STK)}</div></div>
<div class=bk3>{"".join(f'<div class="{"lo" if (n,u,b,bk,c) in LOW else ""}"><small>BOOKED THIS WEEK</small><b>{bk}</b><span>{n}</span></div>' for n,u,b,bk,c in STK)}</div>
<div class=nb><span class=ib>{ic("box",26)}</span><span>{LOW[0][0]}: {LOW[0][2]} in stock, {LOW[0][3]} booked. <b>Reorder goes to the supplier today.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.gd3{flex:1;padding:16px 22px;display:flex;flex-direction:column;justify-content:space-evenly}
.lb3{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;text-align:center}.lb3 b{display:block;font:800 21px/1.3 Montserrat}.lb3 span{font:500 16px/1.4 'Source Sans 3';color:#7a715e}
.bk3{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.bk3 div{background:#fff;border-radius:16px;padding:10px 12px;box-shadow:0 8px 18px rgba(45,42,31,.06)}
.bk3 small{display:block;font:700 11px/1.4 'Source Sans 3';letter-spacing:1px;color:#7a715e}.bk3 b{display:block;font:800 32px/1.3 Montserrat}.bk3 span{font:600 16px/1.4 'Source Sans 3'}
.bk3 .lo{background:#c0392b;color:#fff}.bk3 .lo small{color:#ffd6cf}""")

P["p357_agri_s4"] = ag(4, "STEP 3 · HARVEST TIME REMINDERS", "Harvest comes,<br><span>the reminder goes by itself.</span>",
f'''<div class=w4><div class="cd vl4"><small class=cap>ON CREDIT · DUE AT HARVEST · SAMPLE</small>{"".join(f'<div class=vr4><b>{v}</b><span>{f} farmers</span><strong>{bg} bags</strong><i>{ic("check",16,w=3)} Reminder ready</i></div>' for v,f,bg in VIL)}</div>
<div class="cd ms4"><small class=cap>WHATSAPP TO FARMER 12 · APRIL</small><p>Namaste. Your wheat harvest is near. On credit: {CRED} bags ({CRED_TXT}). Please pay at the shop or by UPI.</p></div>
<div class="cd sl4"><div class=tx4><small class=cap>SLIP · FARMER 07 · VILLAGE B</small><b>All 5 credit bags paid</b><span>Paid by UPI on 20 Nov. The account is clear for the next season.</span></div><div class=st4>{stamp()}</div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.vl4{flex:1;padding:16px 24px;display:flex;flex-direction:column}
.vr4{flex:1;display:grid;grid-template-columns:1fr 150px 130px 200px;gap:12px;align-items:center;border-bottom:1px solid #efe9dc}.vr4:last-child{border:0}
.vr4 b{font:800 26px/1.3 Montserrat}.vr4 span{font:500 20px/1.4 'Source Sans 3';color:#7a715e}.vr4 strong{font:800 24px/1.3 Montserrat;color:#8a5a33}
.vr4 i{display:flex;align-items:center;gap:6px;justify-content:center;font:700 16px/1.3 'Source Sans 3';font-style:normal;background:#e6f2d6;color:#3d6f14;border-radius:10px;padding:8px}
.ms4{background:#dff3c6;border-radius:22px 22px 6px 22px;padding:16px 22px;display:flex;flex-direction:column;gap:6px}.ms4 p{font:500 25px/1.45 'Source Sans 3'}
.sl4{flex:none;display:grid;grid-template-columns:1fr 230px;gap:16px;align-items:center;padding:14px 24px;background:#fffdf6;border:2px dashed #cbbd9f;box-shadow:none}
.tx4 b{display:block;font:800 28px/1.3 Montserrat;margin:4px 0}.tx4 span{font:500 19px/1.45 'Source Sans 3';color:#5e5645}.st4{display:flex;justify-content:center;align-items:center;padding:6px}""")

P["p357_agri_s5"] = ag(5, "YOUR TURN", "Run an agri input shop?<br><span>Let's build your app.</span>",
f'''<div class=w5><div class="cd c5">{iso(STK[:3], H=440, unit=2.7, w=110, d=40, gap=150)}<div class=st5>{stamp(sz=170)}<span>Every farmer account,<br>clear for next season.</span></div></div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Farmer ledger","Every bag, paid or credit"),("box","Godown stock","Stock vs bookings"),("bell","Harvest reminders","Sent by village"),("send","WhatsApp slips","Same day, every entry")])}</div>
<div class=q>How do you keep farmer credit today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#4f8a1f;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1.05fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{display:flex;flex-direction:column;justify-content:space-evenly;padding:20px}.st5{display:flex;align-items:center;gap:16px}.st5 span{font:700 20px/1.4 Montserrat;color:#2f7d32}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(45,42,31,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#e6f2d6;color:#2d2a1f}.ti b{display:block;font:800 23px/1.4 Montserrat;margin-bottom:2px}.ti div span{font:500 18px/1.4 'Source Sans 3';color:#5e5645}
.q{background:#2d2a1f;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Source Sans 3'}""")


# ───────── 358 USA · Septic pumping · SINGLE · TeX Gyre Adventor + Inter · slate navy / heat orange ramp / paper
# New technique: hexbin heat map of service zones (pointy-top hex grid, fill by tanks due) — the route days and
# the text reminder are picked from the hottest zones in code.
ZD = [2, 5, 1, 7, 3, 0, 6, 2, 4, 1, 3, 0]
RAMP = ["#f3ece2", "#fbd9bd", "#f6b07a", "#e8743b", "#b9400f"]
def heat(v): return RAMP[0] if v == 0 else RAMP[min(4, 1 + (v - 1) // 2)]
def hexmap(r=64):
    w = math.sqrt(3) * r; W = 4 * w + w / 2 + 24; H = 2 * r + 2 * 1.5 * r + 24
    s = f'<svg viewBox="0 0 {W:.0f} {H:.0f}" class=hx8>'
    for i, v in enumerate(ZD):
        row, col = i // 4, i % 4
        cx = 12 + w / 2 + col * w + (w / 2 if row % 2 else 0); cy = 12 + r + row * 1.5 * r
        pts = " ".join(f"{cx + (r-3) * math.cos(math.radians(60*k-30)):.1f},{cy + (r-3) * math.sin(math.radians(60*k-30)):.1f}" for k in range(6))
        tc = "#fff" if v >= 5 else "#1f2d3d"
        s += f'<polygon points="{pts}" fill="{heat(v)}" stroke="#fff" stroke-width="5"/>'
        s += f'<text x="{cx:.1f}" y="{cy-8:.1f}" text-anchor="middle" font-family="Inter" font-weight="600" font-size="16" fill="{tc}" opacity=".85">Zone {i+1}</text>'
        s += f'<text x="{cx:.1f}" y="{cy+24:.1f}" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="30" fill="{tc}">{v}</text>'
    return s + "</svg>"
TOP = sorted(range(12), key=lambda i: -ZD[i])[:3]
DAYS = ["Tue, Dec 8", "Wed, Dec 9", "Thu, Dec 10"]
P["p358_septic"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#f3f0ea;color:#1f2d3d}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#c2531a;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#c2531a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.mp8{background:#fff;border-radius:26px;padding:16px 22px;display:grid;grid-template-columns:1fr 210px;gap:18px;align-items:center;box-shadow:0 12px 28px rgba(31,45,61,.08)}
.mp8 small,.rt8>small{display:block;font:700 13px/1.4 Inter;letter-spacing:2px;color:#6b7684}.hx8{width:100%;display:block;margin-top:6px}
.lg8{display:flex;flex-direction:column;gap:12px}.lg8 .rp{display:flex;height:20px;border-radius:6px;overflow:hidden}.lg8 .rp i{flex:1}
.lg8 .rl{display:flex;justify-content:space-between;font:600 14px/1.3 Inter;color:#6b7684}
.lg8 .tt{background:#1f2d3d;color:#fff;border-radius:18px;padding:14px 16px}.lg8 .tt b{display:block;font:700 46px/1.2 'TeX Gyre Adventor';color:#f6b07a}.lg8 .tt span{font:500 16px/1.4 Inter}
.lg8 p{font:500 15px/1.45 Inter;color:#4b5868}
.bt8{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px;min-height:0}
.rt8{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 12px 28px rgba(31,45,61,.08)}
.rr8{flex:1;display:grid;grid-template-columns:16px 1fr auto;gap:12px;align-items:center;border-radius:16px;background:#f7f4ef;padding:10px 14px}
.rr8 i{width:16px;height:16px;border-radius:4px}.rr8 b{display:block;font:700 20px/1.3 'TeX Gyre Adventor'}.rr8 span{font:500 15px/1.4 Inter;color:#6b7684}.rr8 strong{font:700 24px/1.3 'TeX Gyre Adventor'}
.sm8{background:#1f2d3d;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;color:#fff}
.sm8>small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#f6b07a}
.bu8{background:#fff;color:#1f2d3d;border-radius:18px 18px 18px 6px;padding:12px 14px;font:500 17px/1.45 Inter;max-width:92%;text-wrap:pretty}
.bu8.me{align-self:flex-end;background:#e8743b;color:#fff;border-radius:18px 18px 6px 18px;font-weight:700}
.sm8 em{margin-top:auto;display:flex;align-items:center;gap:8px;font:500 15px/1.4 Inter;font-style:normal;color:#c9d2dc}
""", "<div class=kk>SEPTIC PUMPING · SERVICE REMINDERS</div><h1>Who's due for a pump-out?<br><span>See it on a map.</span></h1>",
f'''<div class=vw><div class=mp8><div><small>TANKS DUE IN DECEMBER, BY ZONE · SAMPLE</small>{hexmap()}</div>
<div class=lg8><div class=rp>{"".join(f'<i style="background:{c}"></i>' for c in RAMP)}</div><div class=rl><span>0</span><span>7+</span></div>
<div class=tt><b>{sum(ZD)}</b><span>tanks past the cycle you set for each home</span></div><p>Each home keeps its tank size and last pump-out date.</p></div></div>
<div class=bt8><div class=rt8><small>ROUTE DAYS · HOTTEST ZONES FIRST</small>{"".join(f'<div class=rr8><i style="background:{heat(ZD[z])}"></i><div><b>Zone {z+1}</b><span>{d}</span></div><strong>{ZD[z]} tanks</strong></div>' for z,d in zip(TOP,DAYS))}</div>
<div class=sm8><small>TEXT REMINDER · ZONE {TOP[0]+1}</small><div class=bu8>Hi, this is Sample Septic Co. Your tank at 18 Birch Ln was last pumped in October 2023. Our truck is in your area on {DAYS[0]}. Reply&nbsp;1 to book a&nbsp;time.</div><div class="bu8 me">1</div><div class=bu8>Thanks! You are booked for {DAYS[0]} at 10&nbsp;AM. We will text you when the truck is on the&nbsp;way.</div><em>{ic("check",16,w=3)} Added to the {DAYS[0]} route automatically.</em></div></div></div>''',
"#1f2d3d", "Run a septic service? DM us", "background:#c2531a;color:#fff")


# ───────── 359 INDIA · Centering + scaffolding rental · SINGLE · Archivo Black + Open Sans · galvanized grey / rust orange / sky blue · PHONE
# New techniques: CSS telescopic steel props (base plate, outer tube, pin, inner tube, U-head) as an isotype (1 = 50),
# a 30-day rent strip per site, and a phone return slip with an SVG signature pad. Missing counts are computed.
from datetime import date
TODAY = date(2026, 11, 23)
SITES9 = [("Site 1", "4-storey building", date(2026, 11, 2), {"Props": 400, "Plates": 600, "Spans": 120}, None),
          ("Site 2", "Bungalow slab", date(2026, 10, 26), {"Props": 300, "Plates": 450, "Spans": 80}, {"Props": 300, "Plates": 422, "Spans": 77}),
          ("Site 3", "Shop row roof", date(2026, 11, 16), {"Props": 200, "Plates": 250, "Spans": 60}, None)]
def prop9(): return '<div class=pr9><i class=u></i><i class=in></i><i class=pn></i><i class=ot></i><i class=bs></i></div>'
S2 = SITES9[1]; MISS = {k: S2[3][k] - S2[4][k] for k in S2[3]}
ph9 = phone(f'''<div class=ap9><div class=ah9><small>SAMPLE CENTERING CO.</small><b>Return slip · {S2[0]}</b><span>{S2[1]} · Mon 23 Nov</span></div>
<div class=tb9><div class="tr9 th"><span>ITEM</span><span>SENT</span><span>BACK</span><span>SHORT</span></div>
{"".join(f'<div class=tr9><b>{k}</b><span>{S2[3][k]}</span><span>{S2[4][k]}</span><strong class="{"z" if not MISS[k] else ""}">{MISS[k]}</strong></div>' for k in S2[3])}</div>
<div class=dy9><small>ON RENT</small><b>{(TODAY - S2[2]).days} days</b><span>since {S2[2].day} Oct</span></div>
<div class=sg9><small>SITE SUPERVISOR SIGNS HERE</small><svg viewBox="0 0 280 70" style="width:100%;display:block"><path d="M10 50 C30 10,45 10,50 40 S70 60,85 30 S110 10,120 45 C125 60,140 20,160 35 S200 55,230 28 L262 40" fill="none" stroke="#1f2429" stroke-width="3" stroke-linecap="round"/></svg></div>
<div class=ph9><small>PHOTOS AT THE GATE</small><div>{"".join('<i class=pl></i>' for _ in range(2))}</div></div>
<div class=sh9>{MISS["Plates"]} plates and {MISS["Spans"]} spans stay on rent until they come back.</div><div class=bk9>Send slip on WhatsApp</div></div>''', 360, 830)
P["p359_props"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#e7ecef;color:#1f2429}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#c4581f;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.25;letter-spacing:-1px} h1 span{color:#2f75b5}
.vw{flex:1;display:flex;gap:20px;min-height:0;align-items:center}
.lf9{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:12px;min-width:0}
.sc9{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(31,36,41,.08)}
.sc9.hi{box-shadow:0 0 0 4px #c4581f,0 12px 26px rgba(31,36,41,.08)}
.hd9{display:flex;justify-content:space-between;align-items:baseline}.hd9 b{font:400 24px/1.3 'Archivo Black'}.hd9 span{font:600 15px/1.4 'Open Sans';color:#66717a}
.ps9{display:flex;gap:10px;align-items:flex-end;flex:1;min-height:0}
.pr9{width:18px;height:100%;max-height:170px;display:flex;flex-direction:column;align-items:center}
.pr9 .u{width:22px;height:8px;border:3px solid #6f7c86;border-top:0;border-radius:0 0 4px 4px}.pr9 .in{width:6px;flex:1;background:#9aa6af}
.pr9 .pn{width:14px;height:4px;background:#c4581f;border-radius:2px}.pr9 .ot{width:10px;height:44px;background:linear-gradient(90deg,#7d8a94,#b7c1c8,#7d8a94);border-radius:2px}.pr9 .bs{width:22px;height:5px;background:#4f5a62;border-radius:2px}
.it9{margin-left:auto;display:flex;gap:6px}.it9 i{font:700 14px/1.3 'Open Sans';font-style:normal;background:#eef2f5;border-radius:8px;padding:6px 8px;text-align:center}.it9 i b{display:block;font:400 18px/1.3 'Archivo Black'}
.st9{display:grid;grid-template-columns:repeat(30,1fr);gap:3px}.st9 i{height:12px;border-radius:2px;background:#e3e8ec}.st9 i.on{background:#2f75b5}.st9 i.ov{background:#c4581f}
.dl9{display:flex;justify-content:space-between;font:600 14px/1.3 'Open Sans';color:#66717a}
.ap9{display:flex;flex-direction:column;gap:10px;padding:8px 18px 18px;flex:1}
.ah9 small{display:block;font:700 11px/1.4 'Open Sans';letter-spacing:2px;color:#66717a}.ah9 b{display:block;font:400 21px/1.35 'Archivo Black'}.ah9 span{font:500 14px/1.4 'Open Sans';color:#66717a}
.tb9{background:#f3f6f8;border-radius:12px;padding:6px 12px}.tr9{display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:6px;align-items:center;padding:8px 0;border-bottom:1px solid #e1e7ec;font:600 15px/1.3 'Open Sans'}.tr9:last-child{border:0}
.tr9.th{font:700 11px/1.3 'Open Sans';letter-spacing:1px;color:#66717a}.tr9 b{font:700 15px/1.3 'Open Sans'}.tr9 strong{font:700 15px/1.3 'Open Sans';color:#fff;background:#c4581f;border-radius:6px;text-align:center;padding:2px 0}.tr9 strong.z{background:#dbe9f5;color:#2f75b5}
.dy9{display:flex;align-items:baseline;gap:8px;background:#1f2429;color:#fff;border-radius:12px;padding:10px 12px}.dy9 small{font:700 11px/1.4 'Open Sans';letter-spacing:1.5px;color:#9fc6ea}.dy9 b{font:400 22px/1.3 'Archivo Black'}.dy9 span{font:500 13px/1.4 'Open Sans';color:#c5ced5}
.sg9{border:2px dashed #b9c4cc;border-radius:12px;padding:8px 10px}.sg9 small{font:700 11px/1.4 'Open Sans';letter-spacing:1.5px;color:#66717a}
.ph9 small{display:block;font:700 11px/1.4 'Open Sans';letter-spacing:1.5px;color:#66717a;margin-bottom:6px}.ph9 div{display:grid;grid-template-columns:1fr 1fr;gap:8px}
.ph9 .pl{height:84px;border-radius:10px;background:repeating-linear-gradient(180deg,#8e9aa3 0 7px,#c3ccd2 7px 10px) 50% 70%/76% 56% no-repeat,linear-gradient(#cfe3f3 60%,#b9a68f 60%)}
.sh9{background:#fdebe0;color:#8a3a10;border-radius:12px;padding:10px 12px;font:600 14px/1.45 'Open Sans'}
.bk9{margin-top:auto;background:#c4581f;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 16px 'Open Sans'}
.nt9{background:#1f2429;color:#fff;border-radius:20px;padding:14px 18px;font:500 17px/1.45 'Open Sans'}.nt9 b{color:#ffb48a}
""", "<div class=kk>CENTERING AND SCAFFOLDING RENTAL</div><h1>Plates missing on return?<br><span>Count them on the slip.</span></h1>",
f'''<div class=vw><div class=lf9>{"".join(f"""<div class="sc9 {'hi' if r else ''}"><div class=hd9><b>{n}</b><span>{d} · sample</span></div>
<div class=ps9>{"".join(prop9() for _ in range(it["Props"]//50))}<div class=it9>{"".join(f"<i><b>{v}</b>{k}</i>" for k,v in it.items())}</div></div>
<div class=st9>{"".join(f'<i class={chr(34)}{"ov" if i>=21 and i<(TODAY-s).days else ("on" if i<(TODAY-s).days else "")}{chr(34)}></i>' for i in range(30))}</div>
<div class=dl9><span>Sent {s.day} {s.strftime("%b")}</span><span>{(TODAY-s).days} days on rent{" · returning today" if r else ""}</span></div></div>""" for n,d,s,it,r in SITES9)}
<div class=nt9>1 prop drawn = 50 props. Orange days = past the 3 weeks agreed. <b>Short items are on the slip before the truck leaves.</b></div></div>{ph9}</div>''',
"#1f2429", "Rent out centering? DM us", "background:#2f75b5;color:#fff")


# ───────── 360 CANADA · Farrier (hoof care visits) · CAROUSEL 5 · Crimson Text + Roboto · saddle tan / forest green / hay cream
# New techniques: SVG horseshoe isotype (filled = due, pale = not due) per barn, weeks-since bars with a cycle tick,
# and a country-road SVG map whose route stops are the barns with the most horses due. All slides share one horse list.
_r = random.Random(422)
BARN_N = [6, 4, 5, 3, 6, 4, 5, 3, 4]
NAMES = ["Ginger", "Scout", "Willow", "Duke", "Pepper", "Maple", "Ranger", "Clover", "Dusty", "Hazel", "Copper", "Misty", "Rusty", "Daisy", "Jasper", "Sage", "Blaze", "Penny", "Bandit", "Honey",
         "Shadow", "Biscuit", "Comet", "Rosie", "Tango", "Cider", "Ollie", "Nutmeg", "Storm", "Poppy", "Buddy", "Fern", "Ace", "Lulu", "Moose", "Bella", "Ziggy", "Peaches", "Chief", "Toffee"]
WORK = ["Trim", "Front shoes", "Full set"]
HR = []; k = 0
for b, n in enumerate(BARN_N, 1):
    for j in range(n):
        cyc = _r.choice([6, 7, 8]); wk = _r.randint(2, 9)
        HR.append(dict(name=NAMES[k], barn=b, cyc=cyc, wk=wk, work=_r.choice(WORK))); k += 1
for h in HR: h["due"] = h["wk"] >= h["cyc"]
DUEB = {b: sum(1 for h in HR if h["barn"] == b and h["due"]) for b in range(1, 10)}
NDUE = sum(DUEB.values())
ROUTE = sorted(DUEB, key=lambda b: -DUEB[b])[:3]
def shoe(due, w=60):
    c = "#a8693a" if due else "#e4d8bf"
    return (f'<svg viewBox="0 0 60 62" style="width:{w}px;display:block"><path d="M12 8 C8 36,18 54,30 54 C42 54,52 36,48 8" fill="none" stroke="{c}" stroke-width="11" stroke-linecap="round"/>'
            + "".join(f'<circle cx="{x}" cy="{y}" r="1.8" fill="{"#fff6e6" if due else "#f7efd9"}"/>' for x, y in [(11, 20), (13, 34), (19, 46), (49, 20), (47, 34), (41, 46)]) + "</svg>")
FR = """
body{--f:'Roboto';--h:'Crimson Text';background:#f7efd9;color:#2a2a22}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#2f5d46;margin-top:22px;margin-bottom:4px}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;line-height:1.18;letter-spacing:-.5px} h1 span{color:#a8693a}
.cd{background:#fffaf0;border-radius:24px;box-shadow:0 12px 28px rgba(42,42,34,.08)}
.cap{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#7b7560}
.nb{display:flex;align-items:center;gap:14px;background:#2f5d46;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 Roboto}.nb .ib{width:50px;height:50px;border-radius:14px;background:#f2c98f;color:#2a2a22}.nb b{color:#f2c98f}
"""
def fr(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2f5d46;color:#fff"):
    return page(FR + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2a2a22", cta, ctacss, tagline=f"{n} / 5")
P["p360_farrier_s1"] = fr(1, "FARRIER · HOOF CARE VISITS", f"{len(HR)} horses, 9 barns.<br><span>Who is due this week?</span>",
f'''<div class=w1>{"".join(f"""<div class="cd bn1 {'hot' if b in ROUTE else ''}"><div class=hh1><b>Barn {b}</b><span>{DUEB[b]} due</span></div><div class=sh1>{"".join(shoe(h["due"]) for h in HR if h["barn"]==b)}</div></div>""" for b in range(1,10))}</div>
<div class=lg1><span>{shoe(True,30)} Due now</span><span>{shoe(False,30)} Not yet</span><em>Sample data · {NDUE} of {len(HR)} due</em></div>''',
css=""".w1{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:14px;min-height:0}.vis{flex-direction:column;gap:14px}
.bn1{padding:14px 18px;display:flex;flex-direction:column;gap:10px}.bn1.hot{box-shadow:0 0 0 4px #a8693a,0 12px 28px rgba(42,42,34,.08)}
.hh1{display:flex;justify-content:space-between;align-items:baseline}.hh1 b{font:700 30px/1.25 'Crimson Text'}.hh1 span{font:700 17px/1.3 Roboto;color:#a8693a}
.sh1{flex:1;display:flex;flex-wrap:wrap;gap:8px 12px;align-content:center}
.lg1{display:flex;gap:24px;align-items:center;font:600 18px/1.4 Roboto}.lg1 span{display:flex;align-items:center;gap:8px}.lg1 em{margin-left:auto;font-style:normal;color:#7b7560}""")

SHOW = [h for h in HR if h["due"]][:4] + [h for h in HR if not h["due"]][:3]
P["p360_farrier_s2"] = fr(2, "STEP 1 · EVERY HORSE ON ITS OWN CYCLE", "Weeks since the last visit,<br><span>for every horse.</span>",
f'''<div class=w2><div class="cd bd2"><div class="r2 h2"><span>HORSE</span><span>WORK</span><span>WEEKS SINCE LAST VISIT · TICK = CYCLE</span></div>
{"".join(f'<div class=r2><div><b>{h["name"]}</b><em>Barn {h["barn"]}</em></div><i>{h["work"]}</i><div class=tk2><div class="br2 {"d" if h["due"] else ""}" style="width:{h["wk"]/10*100:.0f}%"><span>{h["wk"]} wk</span></div><s style="left:{h["cyc"]/10*100:.0f}%"></s></div></div>' for h in SHOW)}
<div class=ax2><span></span><span></span><div>{"".join(f"<i>{w}</i>" for w in range(0,11,2))}</div></div></div>
<div class=nb><span class=ib>{ic("cal",26)}</span><span>Each horse keeps its own cycle, 6 to 8 weeks. <b>Due horses turn tan on their own.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.bd2{flex:1;padding:16px 24px;display:flex;flex-direction:column}
.r2{flex:1;display:grid;grid-template-columns:170px 150px 1fr;gap:16px;align-items:center;border-bottom:1px solid #efe6d0}
.h2{flex:none;font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#7b7560;border-bottom:2px solid #2a2a22;padding-bottom:6px}
.r2 b{display:block;font:700 30px/1.2 'Crimson Text'}.r2 em{font:500 16px/1.4 Roboto;font-style:normal;color:#7b7560}
.r2>i{font:600 17px/1.3 Roboto;font-style:normal;background:#efe6d0;border-radius:8px;padding:6px 10px;text-align:center}
.tk2{position:relative;height:40px;background:#f1e9d6;border-radius:10px}.br2{height:100%;border-radius:10px;background:#cdd9cf;display:flex;align-items:center;justify-content:flex-end;padding-right:10px}.br2.d{background:#a8693a;color:#fff}
.br2 span{font:700 17px/1.3 Roboto}.tk2 s{position:absolute;top:0;bottom:0;width:5px;margin-left:-2.5px;background:#2f5d46;border-radius:2px}
.ax2{display:grid;grid-template-columns:170px 150px 1fr;gap:16px;padding-top:6px}.ax2 div{display:flex;justify-content:space-between;font:600 14px/1.3 Roboto;color:#7b7560}.ax2 i{font-style:normal}""")

BP = {b: (x, round(y * 1.2)) for b, (x, y) in {1: (90, 110), 2: (300, 80), 3: (520, 130), 4: (740, 90), 5: (170, 300), 6: (420, 280), 7: (680, 320), 8: (270, 470), 9: (600, 480)}.items()}
_o = []; _c = (40, 640); _left = list(ROUTE)
while _left:
    _n = min(_left, key=lambda b: (BP[b][0]-_c[0])**2 + (BP[b][1]-_c[1])**2); _o.append(_n); _left.remove(_n); _c = BP[_n]
ROUTE = _o
TIMES = ["8:00 AM", "11:30 AM", "2:30 PM"]
def rmap(W=880, H=680):
    s = f'<svg viewBox="0 0 {W} {H}" class=mp3><rect width="{W}" height="{H}" rx="18" fill="#e4ead9"/>'
    s += "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="#d6dfc6"/>' for x, y, w, h in [(30, 230, 200, 80), (560, 250, 220, 80), (380, 470, 160, 140), (40, 460, 150, 150)])
    s += '<path d="M0 240 C200 205,320 275,480 240 S760 205,880 250" fill="none" stroke="#c9bfa6" stroke-width="16"/><path d="M450 0 C430 190,470 430,430 680" fill="none" stroke="#c9bfa6" stroke-width="16"/>'
    pts = [BP[b] for b in ROUTE]
    s += '<path d="M' + " L".join(f"{x} {y}" for x, y in [(40, 640)] + pts) + '" fill="none" stroke="#a8693a" stroke-width="6" stroke-dasharray="14 10" stroke-linecap="round"/>'
    s += '<rect x="20" y="626" width="92" height="34" rx="8" fill="#2a2a22"/><text x="66" y="649" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="15" fill="#fff">START</text>'
    for b, (x, y) in BP.items():
        on = b in ROUTE
        s += f'<circle cx="{x}" cy="{y}" r="{28 if on else 22}" fill="{"#a8693a" if on else "#fffaf0"}" stroke="#2a2a22" stroke-width="3"/>'
        s += f'<text x="{x}" y="{y+8}" text-anchor="middle" font-family="Crimson Text" font-weight="700" font-size="{24 if on else 20}" fill="{"#fff" if on else "#2a2a22"}">{b}</text>'
    for i, b in enumerate(ROUTE):
        x, y = BP[b]
        lx = x + 34 if x + 140 < W else x - 130
        s += f'<rect x="{lx}" y="{y-16}" width="96" height="32" rx="8" fill="#2f5d46"/><text x="{lx+48}" y="{y+6}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="15" fill="#fff">Stop {i+1}</text>'
    return s + "</svg>"
P["p360_farrier_s3"] = fr(3, "STEP 2 · ONE ROUTE A DAY", "Visit the barns<br><span>with the most horses due.</span>",
f'''<div class=w3><div class="cd mc3">{rmap()}</div>
<div class=st3>{"".join(f'<div class="cd sp3"><small class=cap>STOP {i+1} · {t}</small><b>Barn {b}</b><span>{DUEB[b]} horses due</span></div>' for i,(b,t) in enumerate(zip(ROUTE,TIMES)))}
<div class=tt3><small>TUESDAY, NOV 24</small><b>{sum(DUEB[b] for b in ROUTE)} horses</b><span>3 barns, one loop</span></div></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.mc3{flex:1;padding:14px;display:flex;align-items:center;min-height:0}.mp3{width:100%;height:100%;display:block}
.st3{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.sp3{padding:12px 16px}.sp3 b{display:block;font:700 30px/1.2 'Crimson Text'}.sp3 span{font:600 17px/1.4 Roboto;color:#a8693a}
.tt3{background:#2f5d46;color:#fff;border-radius:24px;padding:12px 16px}.tt3 small{display:block;font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#cfe3d6}.tt3 b{display:block;font:700 32px/1.2 'Crimson Text';color:#f2c98f}.tt3 span{font:500 16px/1.4 Roboto}""")

B4 = ROUTE[0]; H4 = [h for h in HR if h["barn"] == B4]
br4 = browser(f'''<div class=bw4><div class=bh4><div><small>SAMPLE HOOF CARE · BARN PORTAL</small><b>Barn {B4} · your horses</b></div><span>Next visit: Tue, Nov 24 · 8 AM</span></div>
{"".join(f'<div class=hr4><b>{h["name"]}</b><span>{h["work"]}</span><em class="{"d" if h["due"] else ""}">{"Due now" if h["due"] else f"Due in {h[chr(99)+chr(121)+chr(99)]-h[chr(119)+chr(107)]} wk"}</em><i>Every {h["cyc"]} wk</i></div>' for h in H4)}
<div class=nt4><small>NOTE AFTER LAST VISIT · {H4[0]["name"].upper()}</small><p>{H4[0]["work"]} done. Hooves look even. Next visit in {H4[0]["cyc"]} weeks. Photos added.</p></div></div>''', url="yourfarrier.ca/barn")
P["p360_farrier_s4"] = fr(4, "STEP 3 · OWNERS SEE EVERY HORSE", "Owners stop texting<br><span>“When are you coming?”</span>",
f'''<div class=w4>{br4}</div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;min-height:0}.w4 .browser{flex:1}
.bw4{flex:1;padding:18px 24px;display:flex;flex-direction:column;gap:8px}.bh4{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:8px;border-bottom:2px solid #2a2a22}
.bh4 small{display:block;font:700 12px/1.4 Roboto;letter-spacing:2px;color:#7b7560}.bh4 b{font:700 34px/1.2 'Crimson Text'}.bh4>span{font:700 17px/1.3 Roboto;background:#2f5d46;color:#fff;border-radius:10px;padding:8px 12px}
.hr4{flex:1;display:grid;grid-template-columns:1fr 160px 150px 130px;gap:12px;align-items:center;border-bottom:1px solid #efe6d0}
.hr4 b{font:700 34px/1.2 'Crimson Text'}.hr4 span{font:500 20px/1.4 Roboto;color:#5a5646}.hr4 i{font:500 16px/1.4 Roboto;font-style:normal;color:#7b7560;text-align:right}
.hr4 em{font:700 16px/1.3 Roboto;font-style:normal;text-align:center;border-radius:8px;padding:7px 8px;background:#e2ece5;color:#2f5d46}.hr4 em.d{background:#a8693a;color:#fff}
.nt4{background:#f7efd9;border-radius:16px;padding:14px 18px;margin-top:6px}.nt4 small{font:700 12px/1.4 Roboto;letter-spacing:2px;color:#7b7560}.nt4 p{font:500 20px/1.45 Roboto}""")

P["p360_farrier_s5"] = fr(5, "YOUR TURN", "Are you a farrier?<br><span>Let's build your app.</span>",
f'''<div class=w5><div class="cd c5">{"".join(shoe(i % 3 != 1, 96) for i in range(12))}</div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("cal","Horse cycles","Due dates by themselves"),("map","Daily route","Barns with most due"),("globe","Barn portal","Owners see every horse"),("camera","Visit notes","Work done and photos")])}</div>
<div class=q>How do you plan your barn visits today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#a8693a;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1.05fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{display:grid;grid-template-columns:repeat(3,1fr);align-content:center;justify-items:center;gap:30px 10px;padding:20px}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fffaf0;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(42,42,34,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#efe6d0;color:#2a2a22}.ti b{display:block;font:700 27px/1.3 'Crimson Text';margin-bottom:2px}.ti div span{font:500 18px/1.4 Roboto;color:#5a5646}
.q{background:#2f5d46;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Roboto}""")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
