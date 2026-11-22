import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 216 USA · Alterations and tailoring shop · CAROUSEL 5 · Gelasio + DM Sans · chalk pink / thread navy / pin silver
# New techniques: garment rack with hanging tickets, garment drawing with numbered pin marks, ready-date kanban, pickup rack slot grid.
def g_pants(c):
    return f'<path d="M30 10 H110 L118 200 H82 L70 70 L58 200 H22 Z" fill="{c}" stroke="#1f2747" stroke-width="4" stroke-linejoin="round"/><path d="M30 26 H110" stroke="#1f2747" stroke-width="3"/>'
def g_dress(c):
    return f'<path d="M50 10 H90 L96 50 L130 200 H10 L44 50 Z" fill="{c}" stroke="#1f2747" stroke-width="4" stroke-linejoin="round"/><path d="M44 60 H96" stroke="#1f2747" stroke-width="3"/>'
def g_jacket(c):
    return f'<path d="M40 10 L70 24 L100 10 L134 30 L130 150 L110 150 L108 200 H32 L30 150 L10 150 L6 30 Z" fill="{c}" stroke="#1f2747" stroke-width="4" stroke-linejoin="round"/><path d="M70 24 V200" stroke="#1f2747" stroke-width="3"/><circle cx="78" cy="90" r="4" fill="#1f2747"/><circle cx="78" cy="130" r="4" fill="#1f2747"/>'
def g_shirt(c):
    return f'<path d="M46 10 L70 22 L94 10 L130 34 L118 70 L104 62 L104 200 H36 L36 62 L22 70 L10 34 Z" fill="{c}" stroke="#1f2747" stroke-width="4" stroke-linejoin="round"/><path d="M70 22 V200" stroke="#1f2747" stroke-width="3"/>'
GAR = {"pants": g_pants, "dress": g_dress, "jacket": g_jacket, "shirt": g_shirt}
def garment(kind, c, w=140):
    return f'<svg viewBox="0 0 140 210" width="{w}" height="{w*1.5:.0f}" class=gm>{GAR[kind](c)}</svg>'
AB = """
body{--f:'DM Sans';--h:'Gelasio';background:#f6e6e4;color:#1f2747}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b2475b;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b2475b}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(31,39,71,.07)}
.tk{background:#fffdf7;border:2px solid #1f2747;border-radius:10px;padding:6px 10px 7px;text-align:center;position:relative}
.tk b{display:block;font:700 22px/1.3 'DM Sans'}.tk span{font:600 15px/1.3 'DM Sans';color:#5a6180}
.tk:before{content:"";position:absolute;top:-9px;left:50%;margin-left:-6px;width:12px;height:12px;border-radius:50%;background:#f6e6e4;border:2px solid #1f2747}
.q{border-color:#b2475b;background:#fbe3e6}.q b{color:#b2475b}
"""
def ab(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f2747;color:#fff"):
    return page(AB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f2747", cta, ctacss, tagline=f"{n} / 5")
rack = [("pants", "#3d4a7a", "A-101", "Thu"), ("dress", "#d98a96", "A-102", "Fri"), ("jacket", "#6b5b4a", None, None), ("shirt", "#9fb7d6", "A-104", "Thu"), ("pants", "#2b2b2b", "A-105", "Sat")]
P["p216_alter_s1"] = ab(1, "ALTERATIONS SHOPS · TICKETS", "“Which one was mine?”<br><span>Tag every piece with a ticket.</span>",
f'''<div class=w1><div class=rk><div class=rod></div><div class=hg>{"".join(f'<div class=it><i class=hk></i>{garment(k,c,172)}<div class="tk {"q" if t is None else ""}"><b>{t or "No tag"}</b><span>{("Ready "+d) if d else "Whose is this?"}</span></div></div>' for k,c,t,d in rack)}</div><div class=fl1><span>5 pieces on the rack</span><span>4 tagged</span><span class=bd>1 unknown</span></div></div>
<div class=cs><div><small>AT THE COUNTER · SAMPLE</small><b>“I dropped off a brown jacket last week.”</b></div><div class=al><small>ON THE RACK</small><b>1 brown jacket, no tag, no name</b></div></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.rk{flex:none;background:#fff;border-radius:28px;padding:24px 22px 20px;gap:16px;display:flex;flex-direction:column;position:relative}
.rod{height:12px;border-radius:6px;background:linear-gradient(#c9ccd6,#8d92a3);margin:0 6px}
.hg{flex:1;display:flex;justify-content:space-between;align-items:flex-start;padding-top:4px}.fl1{display:flex;gap:10px;justify-content:center;font:600 19px 'DM Sans';color:#5a6180}.fl1 span{background:#f6e6e4;border-radius:12px;padding:8px 14px}.fl1 .bd{background:#b2475b;color:#fff}
.it{display:flex;flex-direction:column;align-items:center;gap:14px;width:176px}.it .tk{padding:10px 14px}.it .tk b{font-size:27px}.it .tk span{font-size:17px}
.hk{display:block;width:26px;height:30px;border:4px solid #8d92a3;border-bottom:0;border-radius:14px 14px 0 0;margin-top:-6px;margin-bottom:-4px}
.gm{display:block}
.cs{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}.cs div{background:#1f2747;color:#fff;border-radius:22px;padding:20px 24px;display:flex;flex-direction:column;justify-content:center}
.cs small{display:block;font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#c3c8dc}.cs b{font:700 34px/1.35 Gelasio;margin-top:6px}.cs .al{background:#b2475b}.cs .al small{color:#f6d3d9}""")

pins = [("1", "Hem 1 in shorter", "Both legs, keep the cuff"), ("2", "Take in waist 1 in", "Back seam"), ("3", "Fix back pocket", "Loose stitch")]
P["p216_alter_s2"] = ab(2, "PART 1 · TICKET AT DROP-OFF", "Every job written once,<br><span>with a ready date.</span>",
f'''<div class=w2><div class="cd gp"><svg viewBox="-20 -10 180 230" class=bp>{g_pants("#2b2b2b")}
<g fill="#b2475b" stroke="#fff" stroke-width="3"><circle cx="40" cy="196" r="13"/><circle cx="70" cy="22" r="13"/><circle cx="104" cy="60" r="13"/></g>
<g font-family="DM Sans" font-weight="700" font-size="15" fill="#fff" text-anchor="middle"><text x="40" y="201"><tspan>1</tspan></text><text x="70" y="27"><tspan>2</tspan></text><text x="104" y="65"><tspan>3</tspan></text></g></svg>
<span class=nt>Black pants · sample customer</span></div>
<div class=tc><div class=th><div><small>TICKET</small><b>A-105</b></div><span>Ready Sat, Dec 5</span></div>
{"".join(f'<div class=pr><i>{n}</i><div><b>{a}</b><span>{b}</span></div></div>' for n,a,b in pins)}
<div class=tx>{ic("chat",22)}Text sent: “Ticket A-105, ready Sat, Dec 5.”</div></div></div>''',
css=""".w2{flex:1;display:flex;gap:16px;min-height:0}
.gp{width:380px;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px}
.bp{width:340px;height:auto;display:block}.nt{font:600 18px 'DM Sans';color:#5a6180}
.tc{flex:1;background:#fffdf7;border:3px solid #1f2747;border-radius:24px;padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.th{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:3px dashed #1f2747;padding-bottom:12px}.th small{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#5a6180}.th b{display:block;font:700 52px/1.3 Gelasio}
.th span{background:#1f2747;color:#fff;border-radius:12px;padding:8px 12px;font:700 17px 'DM Sans'}
.pr{flex:1;display:flex;gap:14px;align-items:center}.pr i{font-style:normal;width:42px;height:42px;border-radius:50%;background:#b2475b;color:#fff;display:flex;align-items:center;justify-content:center;font:700 20px 'DM Sans';flex:none}
.pr b{display:block;font:700 25px/1.3 Gelasio}.pr span{font:500 18px 'DM Sans';color:#5a6180}
.tx{display:flex;gap:10px;align-items:center;background:#f6e6e4;border-radius:14px;padding:12px 14px;font:600 18px/1.35 'DM Sans'}""")

kb = {"Thu, Dec 3": [("A-101", "Pants · hem"), ("A-104", "Shirt · sleeves"), ("A-106", "Skirt · zipper")],
      "Fri, Dec 4": [("A-102", "Dress · take in"), ("A-107", "Coat · buttons")],
      "Sat, Dec 5": [("A-105", "Pants · hem, waist"), ("A-108", "Jeans · hem"), ("A-109", "Blazer · sleeves")]}
P["p216_alter_s3"] = ab(3, "PART 2 · WORK BY READY DATE", "The bench sees<br><span>what is due first.</span>",
f'''<div class=w3><div class=kb>{"".join(f'<div class=col><div class=ch><small>READY</small><b>{d}</b><span>{len(v)} tickets</span></div>' + "".join(f'<div class=kc><b>{t}</b><span>{x}</span></div>' for t,x in v) + '<div class=op3>Open for new tickets</div></div>' for d,v in kb.items())}</div>
<div class=bar3><span class=ib>{ic("clock",26)}</span><span>Tickets move left to right. Nothing due tomorrow gets missed.</span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.kb{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.col{background:#fff;border-radius:24px;padding:14px;display:flex;flex-direction:column;gap:10px}
.ch{background:#1f2747;color:#fff;border-radius:16px;padding:12px 16px}.ch small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#c3c8dc}.ch b{display:block;font:700 26px/1.3 Gelasio}.ch span{font:500 16px 'DM Sans';color:#c3c8dc}
.col:first-child .ch{background:#b2475b}.col:first-child .ch small,.col:first-child .ch span{color:#f6d3d9}
.kc{flex:none;height:150px;border:2px solid #e8dfe5;border-left:8px solid #1f2747;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;justify-content:center;gap:2px}
.kc b{font:700 32px/1.3 Gelasio}.kc span{font:500 20px 'DM Sans';color:#5a6180}
.op3{flex:1;border:2px dashed #e0d3da;border-radius:14px;display:flex;align-items:center;justify-content:center;font:600 17px 'DM Sans';color:#a49aa8;text-align:center;padding:8px}.bar3{display:flex;gap:14px;align-items:center;background:#1f2747;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'DM Sans'}.bar3 .ib{width:50px;height:50px;border-radius:14px;background:#b2475b}""")

slots = [(r + str(c)) for r in "ABC" for c in range(1, 6)]
filled = {"A1": "A-098", "A3": "A-099", "B2": "A-100", "B4": "A-105", "C1": "A-097", "C5": "A-101"}
P["p216_alter_s4"] = ab(4, "PART 3 · PICKUP", "Ready? Text the slot,<br><span>find it in seconds.</span>",
f'''<div class=w4><div class=ms><small>TEXT TO SAMPLE CUSTOMER · SAT, DEC 5 · 11:40 AM</small><p>Your pants (ticket A-105) are ready. Pickup at the counter till 7 PM.</p></div>
<div class="cd sg"><div class=sh><small>PICKUP RACK · SAMPLE</small><span><i></i>Ready</span></div><div class=gr>{"".join(f'<div class="sl {"on" if s=="B4" else ("f" if s in filled else "")}"><small>{s}</small><b>{filled.get(s,"")}</b></div>' for s in slots)}</div></div>
<div class=pk><div><small>STAFF SEES</small><b>A-105 → Slot B4</b></div><div class=pd><small>PAID AT PICKUP</small><b>Ticket closed</b></div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ms{background:#1f2747;color:#fff;border-radius:24px;padding:18px 22px}.ms small{font:700 14px/1.4 'DM Sans';letter-spacing:1.5px;color:#c3c8dc}.ms p{font:500 24px/1.45 'DM Sans';margin-top:4px}
.sg{flex:1;min-height:0;padding:16px 20px;display:flex;flex-direction:column;gap:12px}
.sh{display:flex;justify-content:space-between;align-items:center}.sh small{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#5a6180}.sh span{display:flex;gap:8px;align-items:center;font:600 16px 'DM Sans'}.sh i{width:16px;height:16px;border-radius:4px;background:#d7dbe8}
.gr{flex:1;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(3,1fr);gap:10px}
.sl{border:2px dashed #d7dbe8;border-radius:14px;padding:10px 12px;display:flex;flex-direction:column;justify-content:space-between}
.sl small{font:700 15px/1.4 'DM Sans';color:#9aa0b8}.sl b{font:700 21px/1.3 'DM Sans'}
.sl.f{border:2px solid #d7dbe8;background:#eef0f6}.sl.on{background:#b2475b;border-color:#b2475b;color:#fff;box-shadow:0 0 0 5px rgba(178,71,91,.25)}.sl.on small{color:#f6d3d9}
.pk{display:grid;grid-template-columns:1fr 1fr;gap:14px}.pk div{background:#fff;border-radius:20px;padding:14px 20px}.pk small{display:block;font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#5a6180}.pk b{font:700 28px/1.3 Gelasio}
.pk .pd{background:#b2475b;color:#fff}.pk .pd small{color:#f6d3d9}""")

P["p216_alter_s5"] = ab(5, "YOUR TURN", "Run an alterations shop?<br><span>Let's build your ticket app.</span>",
f'''<div class=w5><div class=rk5><div class=rod></div><div class=hg5>{garment("jacket","#6b5b4a",160)}{garment("dress","#d98a96",160)}</div><div class=tk><b>A-110</b><span>Ready Mon</span></div></div>
<div class=t5>{"".join(f'<div><span class=ib>{ic(i,32)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("tag","Tickets","Every piece tagged"),("cal","Ready dates","Work by due day"),("chat","Ready texts","Sent for you"),("grid","Rack slots","Found in seconds")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#b2475b;color:#fff",
css=""".w5{flex:1;display:flex;gap:16px;min-height:0}
.rk5{width:380px;flex:none;background:#fff;border-radius:28px;padding:28px 22px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px}
.rk5 .rod{align-self:stretch;height:12px;border-radius:6px;background:linear-gradient(#c9ccd6,#8d92a3)}.hg5{display:flex;gap:16px}
.t5{flex:1;display:grid;grid-template-rows:repeat(4,1fr);gap:12px}.t5 div{background:#1f2747;color:#fff;border-radius:22px;padding:14px 20px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:16px;align-content:center}
.t5 div:nth-child(2n){background:#b2475b}.t5 .ib{grid-row:span 2;width:76px;height:76px;border-radius:16px;background:rgba(255,255,255,.14)}.t5 b{font:700 34px/1.3 Gelasio}.t5 small{font:400 20px/1.35 'DM Sans';color:#e9e2ea}""")

# ───────── 217 INDIA · Cattle feed dealer · SINGLE · Fira Sans (Black) + Open Sans · straw yellow / field green / soil brown
# New technique: top-down tractor trolley load plan — sack grid coloured by village drop, unloading order by row.
vil = [("Village 1", 18, "#2f6b3a"), ("Village 2", 12, "#c98a1b"), ("Village 3", 15, "#7a4b2a"), ("Village 4", 9, "#6f8f9a")]
sacks = []
for v, n, c in vil: sacks += [c] * n
cells = "".join(f'<i style="background:{c}"></i>' for c in sacks)  # 54 sacks → 9 x 6 grid
P["p217_feed"] = page("""
body{--f:'Open Sans';--h:'Fira Sans';background:#f3e7c2;color:#2c2416}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#2f6b3a;margin-top:22px}
h1{font-family:'Fira Sans';font-weight:900;font-size:64px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#2f6b3a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp{flex:1;min-height:0;background:#fffaf0;border-radius:28px;padding:18px 24px;display:flex;flex-direction:column;gap:12px;box-shadow:0 14px 30px rgba(44,36,22,.08)}
.tp>small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#7a6c50}
.tr{flex:1;min-height:0;display:flex;align-items:center;gap:0}
.cab{width:150px;height:200px;background:#2f6b3a;border-radius:30px 12px 12px 30px;position:relative;flex:none}
.cab:before,.cab:after{content:"";position:absolute;left:24px;width:66px;height:26px;border-radius:8px;background:#1f2a1c}.cab:before{top:-14px}.cab:after{bottom:-14px}
.cab b{position:absolute;inset:60px 20px;background:#cfe0d2;border-radius:10px}
.hitch{width:46px;height:12px;background:#5a4a33;flex:none}
.trl{flex:1;border:8px solid #5a4a33;border-radius:14px;background:#d9c79b;padding:10px;display:grid;grid-template-columns:repeat(9,1fr);grid-template-rows:repeat(6,1fr);gap:6px;height:300px;position:relative}
.trl i{border-radius:8px;box-shadow:inset 0 -6px 0 rgba(0,0,0,.18),inset 0 3px 0 rgba(255,255,255,.18)}
.vg{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.vg div{border-radius:16px;padding:12px 14px;color:#fff;display:flex;flex-direction:column}
.vg small{font:700 13px/1.4 'Open Sans';letter-spacing:1.5px;opacity:.9}.vg b{font:900 30px/1.3 'Fira Sans'}.vg span{font:600 15px/1.35 'Open Sans';opacity:.92}
.bt{display:grid;grid-template-columns:1.1fr 1fr;gap:14px}
.bt div{background:#2c2416;color:#fff;border-radius:22px;padding:16px 20px}
.bt small{display:block;font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#e8d79f}.bt b{display:block;font:800 28px/1.3 'Fira Sans'}.bt span{font:500 17px/1.4 'Open Sans';color:#d9cfb6}
.bt .cr{background:#2f6b3a}.bt .cr small{color:#cfe8c9}
""", "<div class=kk>CATTLE FEED DEALERS · TODAY'S TRIP</div><h1>54 sacks, 4 villages,<br>one trolley?<br><span>Load it in drop order.</span></h1>",
f'''<div class=vw><div class=tp><small>TROLLEY LOAD PLAN · SAMPLE · TOP VIEW</small><div class=tr><div class=cab><b></b></div><div class=hitch></div><div class=trl>{cells}</div></div>
<div class=vg>{"".join(f'<div style="background:{c}"><small>DROP {i}</small><b>{n} sacks</b><span>{v}</span></div>' for i,(v,n,c) in enumerate(vil,1))}</div></div>
<div class=bt><div><small>ORDERS FROM THE APP</small><b>4 village orders</b><span>Farmers and dairies order by phone link.</span></div><div class=cr><small>ON CREDIT</small><b>Village 3 · due Sat</b><span>Reminder goes by itself.</span></div></div></div>''',
"#2c2416", "Sell cattle feed? DM us", "background:#2f6b3a;color:#fff")

# ───────── 218 INDIA · Sofa and mattress cleaning at home · SINGLE · Poppins + Source Sans 3 · foam aqua / deep navy / white
# New technique: booked items drawn as objects (sofa seats split into numbered cushions, mattresses by size) = price-free job card; slot rail.
def sofa(seats, w):
    sw = (w - 40) / seats
    cush = "".join(f'<rect x="{20 + i*sw + 4:.1f}" y="40" width="{sw-8:.1f}" height="50" rx="10" fill="#e8f6f5" stroke="#163049" stroke-width="3"/>' for i in range(seats))
    return f'<svg viewBox="0 0 {w} 120" width="{w*1.4:.0f}" height="168"><rect x="0" y="10" width="{w}" height="40" rx="16" fill="#3fb3ad" stroke="#163049" stroke-width="3"/><rect x="0" y="36" width="22" height="70" rx="10" fill="#3fb3ad" stroke="#163049" stroke-width="3"/><rect x="{w-22}" y="36" width="22" height="70" rx="10" fill="#3fb3ad" stroke="#163049" stroke-width="3"/>{cush}<rect x="20" y="88" width="{w-40}" height="18" rx="6" fill="#2a8f8a" stroke="#163049" stroke-width="3"/></svg>'
def mattress(w, h, lbl):
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect x="2" y="2" width="{w-4}" height="{h-4}" rx="14" fill="#e8f6f5" stroke="#163049" stroke-width="3"/><rect x="14" y="14" width="{w-28}" height="{h-28}" rx="8" fill="none" stroke="#3fb3ad" stroke-width="3" stroke-dasharray="8 6"/><text x="{w/2}" y="{h/2+8}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="22" fill="#163049"><tspan>{lbl}</tspan></text></svg>'
P["p218_sofa"] = page("""
body{--f:'Source Sans 3';--h:'Poppins';background:#dff3f1;color:#163049}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#2a8f8a;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#2a8f8a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.jb{flex:1;min-height:0;background:#fff;border-radius:28px;padding:18px 24px;display:flex;flex-direction:column;gap:12px;box-shadow:0 14px 30px rgba(22,48,73,.08)}
.jh{display:flex;justify-content:space-between;align-items:center}.jh small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#5c7286}.jh b{font:700 17px 'Source Sans 3';background:#163049;color:#fff;border-radius:10px;padding:5px 12px}
.ob{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:12px;min-height:0}
.ob>div{background:#f2faf9;border-radius:20px;padding:14px 16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.ob small{align-self:flex-start;font:700 14px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#2a8f8a}
.ob p{font:700 28px/1.3 Poppins}.ob span{font:500 19px 'Source Sans 3';color:#5c7286}
.mt{flex-direction:row!important;flex-wrap:wrap}
.sr{display:flex;gap:8px}
.sr div{flex:1;border:2px solid #cfe6e4;border-radius:14px;padding:10px 0;text-align:center;font:600 19px 'Source Sans 3';background:#fff}
.sr .x{color:#a8b6c2;text-decoration:line-through}.sr .on{background:#163049;border-color:#163049;color:#fff}
.bt{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.bt div{background:#163049;color:#fff;border-radius:20px;padding:14px 18px}.bt small{display:block;font:700 13px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#9fd8d4}.bt b{font:700 24px/1.3 Poppins}
.bt .a{background:#2a8f8a}.bt .a small{color:#d6f2ef}
""", "<div class=kk>SOFA AND MATTRESS CLEANING · HOME VISITS</div><h1>“How many seats?”<br>on every call?<br><span>Let them book by item.</span></h1>",
f'''<div class=vw><div class=jb><div class=jh><small>BOOKING B-218 · SAMPLE HOME</small><b>6 items</b></div>
<div class=ob><div><small>SOFA · 3 + 2 SEATER</small>{sofa(3, 300)}{sofa(2, 210)}<p>5 seats</p></div>
<div><small>MATTRESS</small>{mattress(300, 190, "Queen")}<p>1 mattress</p><span>Customer photo added</span></div></div>
<div class=sr><div class=x>9 AM</div><div class=on>12 PM</div><div>3 PM</div><div class=x>6 PM</div></div></div>
<div class=bt><div><small>DAY</small><b>Sun 29 Nov</b></div><div><small>CREW</small><b>Team 2 · 2 people</b></div><div class=a><small>TIME ON SITE</small><b>About 3 hours</b></div></div></div>''',
"#163049", "Clean sofas? DM us", "background:#2a8f8a;color:#fff")

# ───────── 219 CANADA · Small manufacturer (custom metal parts) · SINGLE · TeX Gyre Adventor + Open Sans · blueprint blue / white / signal yellow
# New technique: top-down production line (stations as machine blocks on a conveyor) with order boxes at their current station + portal row.
stations = [("Cut", "#ffffff"), ("Bend", "#ffffff"), ("Weld", "#ffffff"), ("Paint", "#ffffff"), ("Pack", "#ffffff")]
orders219 = {"Cut": ["PO-58"], "Bend": ["PO-55", "PO-57"], "Weld": [], "Paint": ["PO-52"], "Pack": ["PO-50"]}
P["p219_factory"] = page("""
body{--f:'Open Sans';--h:'TeX Gyre Adventor';background:#173a6b;color:#fff}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#ffd23f;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#ffd23f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.fl{background-color:#1d4580;background-image:linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px);background-size:28px 28px;border:2px solid rgba(255,255,255,.25);border-radius:26px;padding:16px 20px 18px;display:flex;flex-direction:column;gap:12px}
.fl>small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#a9c3e6}
.ln{position:relative;display:grid;grid-template-columns:repeat(5,1fr);gap:14px;padding:0}
.ln:before{content:"";position:absolute;left:0;right:0;top:72px;height:26px;background:repeating-linear-gradient(90deg,#7f97b8 0 10px,#5f789c 10px 20px);border-radius:6px}
.st{position:relative;display:flex;flex-direction:column;align-items:center;gap:10px}
.mc{width:100%;height:170px;border:3px solid #fff;border-radius:14px;background:#173a6b;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;position:relative;z-index:1}
.mc b{font:700 24px/1.3 'TeX Gyre Adventor'}.mc span{font:600 15px 'Open Sans';color:#a9c3e6}
.bx{display:flex;flex-direction:column;gap:6px;width:100%;min-height:96px}.bx i{font-size:20px!important;padding:8px 0!important}
.bx i{font-style:normal;background:#ffd23f;color:#173a6b;border-radius:8px;padding:6px 0;text-align:center;font:700 18px/1.3 'Open Sans';box-shadow:inset 0 -4px 0 rgba(0,0,0,.15)}
.bx i.me{background:#fff;outline:3px solid #ffd23f}
.bx em{font-style:normal;text-align:center;font:600 15px 'Open Sans';color:#7f97b8;padding-top:8px}
.pt{flex:1;min-height:0;background:#fff;color:#173a6b;border-radius:26px;overflow:hidden;display:flex;flex-direction:column}
.pb{background:#eef3fa;display:flex;align-items:center;gap:8px;padding:10px 16px;font:600 15px 'Open Sans';color:#5d7392}.pb i{width:11px;height:11px;border-radius:50%;background:#c9d4e3}
.pb span{margin-left:10px;background:#fff;border-radius:10px;padding:3px 12px;flex:1}
.pc{flex:1;padding:14px 22px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.pc small{font:700 15px/1.4 'Open Sans';letter-spacing:2px;color:#5d7392}.pc h3{font:700 40px/1.3 'TeX Gyre Adventor'}.up{display:flex;gap:10px;align-items:center;background:#eef3fa;border-radius:12px;padding:10px 14px;font:600 19px 'Open Sans'}
.sp{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}.sp div{height:20px;border-radius:7px;background:#dfe7f2}.sp .d{background:#173a6b}.sp .n{background:#ffd23f}
.sl{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;font:600 18px 'Open Sans';color:#5d7392}.sl span:nth-child(2){color:#173a6b;font-weight:800}
.ft2{display:flex;justify-content:space-between;align-items:center;font:600 21px 'Open Sans'}.ft2 b{font:700 26px 'TeX Gyre Adventor'}
""", "<div class=kk>SMALL MANUFACTURERS · ORDER PORTAL</div><h1>“Where's my order?”<br>emails all day?<br><span>Give buyers a live portal.</span></h1>",
f'''<div class=vw><div class=fl><small>SHOP FLOOR · LIVE · SAMPLE</small><div class=ln>{"".join(f'<div class=st><div class=mc><b>{s}</b><span>Station {i}</span></div><div class=bx>{"".join(f"<i class={chr(39)+(chr(109)+chr(101) if o=="PO-57" else "")+chr(39)}>{o}</i>" for o in orders219[s]) or "<em>Free</em>"}</div></div>' for i,(s,_) in enumerate(stations,1))}</div></div>
<div class=pt><div class=pb><i></i><i></i><i></i><span>portal.yourshop.ca/PO-57</span></div><div class=pc><small>SAMPLE BUYER · ORDER PO-57 · 40 BRACKETS</small><h3>Now at station 2 · Bend</h3>
<div class=sp><div class=d></div><div class=n></div><div></div><div></div><div></div></div><div class=sl><span>Cut</span><span>Bend</span><span>Weld</span><span>Paint</span><span>Pack</span></div>
<div class=up>{ic('clock',22)}Last update: Bend started Tue, Dec 8 · 9:20 AM</div><div class=ft2><span>Ship date</span><b>Fri, Dec 11</b></div></div></div></div>''',
"#fff", "Make parts? DM us", "background:#ffd23f;color:#173a6b", logo_color="#ffffff")

# ───────── 220 INDIA · Home pickle (achaar) business · CAROUSEL 5 · Lora + Roboto · mustard / chilli red / jar green
# New techniques: glass jar SVG with fill level (batch plan from orders), order page with jar size steppers, courier parcel labels by PIN zone.
def jar(fill, col, w=150, label="", lid="#b23a2a"):
    H = 200; top = 46; inner = H - top - 14
    fy = top + inner * (1 - fill)
    return f'''<svg viewBox="0 0 150 210" width="{w}" height="{w*1.4:.0f}" class=jr><rect x="38" y="6" width="74" height="26" rx="6" fill="{lid}" stroke="#3a2a12" stroke-width="3"/>
<path d="M30 34 H120 Q134 40 134 60 V188 Q134 202 118 202 H32 Q16 202 16 188 V60 Q16 40 30 34 Z" fill="#eef6e6" fill-opacity=".7" stroke="#3a2a12" stroke-width="3"/>
<clipPath id="jc{label}{int(fill*100)}"><path d="M30 34 H120 Q134 40 134 60 V188 Q134 202 118 202 H32 Q16 202 16 188 V60 Q16 40 30 34 Z"/></clipPath>
<g clip-path="url(#jc{label}{int(fill*100)})"><rect x="0" y="{fy:.0f}" width="150" height="210" fill="{col}"/>''' + "".join(f'<circle cx="{random.randint(28,122)}" cy="{random.randint(int(fy)+8, 194)}" r="{random.randint(4,8)}" fill="#fff" fill-opacity=".22"/>' for _ in range(int(10*fill)+1)) + f'''</g>
<rect x="34" y="96" width="82" height="46" rx="6" fill="#fffdf3" stroke="#3a2a12" stroke-width="2"/><text x="75" y="125" text-anchor="middle" font-family="Lora" font-weight="700" font-size="16" fill="#3a2a12"><tspan>{label}</tspan></text></svg>'''
random.seed(220)
PB = """
body{--f:'Roboto';--h:'Lora';background:#f7e7b4;color:#3a2a12}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#b23a2a;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b23a2a}
.cd{background:#fffdf3;border-radius:24px;box-shadow:0 12px 28px rgba(58,42,18,.08)}
.jr{display:block}
"""
def pb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3a2a12;color:#fff"):
    return page(PB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3a2a12", cta, ctacss, tagline=f"{n} / 5")
chats = [("Customer 1", "2 mango, 1 lemon, 500 g each?"), ("Customer 2", "Same as last month, please."), ("Customer 3", "Can you send to another city?"), ("Customer 4", "Mixed one, 1 kg. When?")]
P["p220_pickle_s1"] = pb(1, "HOME PICKLE BUSINESS · ORDERS", "Pickle orders in<br>40 different chats?<br><span>Put them on one page.</span>",
f'''<div class=w1><div class="cd js">{jar(.8,"#e0a21b",290,"Mango")}<span class=jl>Mango pickle · 500 g jars</span></div>
<div class=ch>{"".join(f'<div class="bb {"r" if i%2 else ""}"><small>{a} · SAMPLE</small><p>“{b}”</p></div>' for i,(a,b) in enumerate(chats))}</div>
<div class=nb><b>40</b><span>chats this week, no one list of who wants what and where to send it.</span></div></div>''',
css=""".w1{flex:1;display:grid;grid-template-columns:400px 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}
.js{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px 14px}.jl{font:600 19px Roboto;color:#6b5a3a}
.ch{display:flex;flex-direction:column;gap:10px;justify-content:center}.bb{background:#fff;border-radius:20px 20px 20px 6px;padding:12px 18px;max-width:92%;box-shadow:0 8px 18px rgba(58,42,18,.07)}
.bb.r{align-self:flex-end;background:#fdf3d0;border-radius:20px 20px 6px 20px}.bb{padding:14px 20px!important}.bb small{font:700 14px/1.4 Roboto;letter-spacing:1.5px;color:#8a7650}.bb p{font:500 24px/1.4 Roboto}
.nb{grid-column:span 2;display:flex;align-items:center;gap:18px;background:#3a2a12;color:#fff;border-radius:22px;padding:14px 22px}.nb b{font:700 54px/1.3 Lora;color:#f2b632}.nb span{font:500 21px/1.4 Roboto}""")

menu = [("Mango pickle", "#e0a21b", [("250 g", 0), ("500 g", 2), ("1 kg", 0)]), ("Lemon pickle", "#c8b23a", [("250 g", 0), ("500 g", 1), ("1 kg", 0)]), ("Green chilli", "#3f7a3a", [("250 g", 0), ("500 g", 0), ("1 kg", 0)]), ("Mixed pickle", "#b23a2a", [("250 g", 0), ("500 g", 0), ("1 kg", 1)])]
P["p220_pickle_s2"] = pb(2, "PART 1 · ONE ORDER PAGE", "Customers pick jar size<br><span>and add the address.</span>",
f'''<div class=w2>{browser(f"""<div class=op><div class=oh><b>Your Pickle Kitchen</b><span>SAMPLE MENU</span></div>
{"".join(f'<div class=mr><i style="background:{c}"></i><b>{n}</b><div class=sz>' + "".join(f'<div class="{"on" if q else ""}"><span>{s}</span><em>− {q} +</em></div>' for s,q in sz) + '</div></div>' for n,c,sz in menu)}
<div class=ad><div><label>Deliver to</label><p>Sample address, your city</p></div><div><label>Pay</label><p>UPI on order</p></div></div>
<div class=bt>Place order · 4 jars</div></div>""", url="yourpicklekitchen.in/order", style="flex:1")}</div>''',
css=""".w2{flex:1;display:flex;min-height:0}
.op{flex:1;padding:20px 26px;display:flex;flex-direction:column;gap:12px}
.oh{display:flex;justify-content:space-between;align-items:center}.oh b{font:700 32px/1.3 Lora}.oh span{font:700 14px Roboto;letter-spacing:2px;color:#8a7650}
.mr{flex:1;display:flex;align-items:center;gap:14px;border-bottom:1px solid #f0e6cc}.mr>i{width:22px;height:22px;border-radius:50%;flex:none}.mr>b{width:200px;flex:none;font:700 24px/1.3 Lora}
.sz{flex:1;display:flex;gap:8px}.sz div{flex:1;border:2px solid #eadfc2;border-radius:12px;padding:12px 10px;display:flex;justify-content:space-between;align-items:center;font:600 19px Roboto}
.sz em{font-style:normal;color:#8a7650}.sz .on{border-color:#b23a2a;background:#fbeae6}.sz .on em{color:#b23a2a;font-weight:800}
.ad{display:grid;grid-template-columns:1.4fr 1fr;gap:10px}.ad div{background:#fbf3dc;border-radius:12px;padding:10px 14px}.ad label{font:700 13px Roboto;letter-spacing:1.5px;color:#8a7650;text-transform:uppercase}.ad p{font:600 19px/1.35 Roboto}
.bt{background:#b23a2a;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 21px Roboto}""")

# batch plan: kg needed from all week's orders (sample)
plan = [("Mango", "#e0a21b", 9.5, 12), ("Lemon", "#c8b23a", 4, 12), ("Chilli", "#3f7a3a", 2.5, 12), ("Mixed", "#b23a2a", 6, 12)]
P["p220_pickle_s3"] = pb(3, "PART 2 · WEEK'S BATCH PLAN", "Know how much<br><span>to make this week.</span>",
f'''<div class=w3><div class="cd bp"><div class=bh><small>BATCH PLAN · WEEK OF 23 NOV · SAMPLE</small><span>Each jar shows the kg needed out of one 12 kg pot.</span></div>{"".join(f'<div class=jc>{jar(kg/cap, c, 215, nm)}<b>{kg:g} kg</b><span>{nm} pickle</span></div>' for nm,c,kg,cap in plan)}</div>
<div class=rw3><div><small>ORDERS THIS WEEK</small><b>28 orders</b><span>All added up by jar size</span></div><div class=hl><small>MAKE FIRST</small><b>Mango, 9.5 kg</b><span>Most asked this week</span></div></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bh{grid-column:span 4;align-self:start;display:flex;flex-direction:column;gap:6px;border-bottom:2px solid #efe2bd;padding-bottom:14px}.bh small{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#8a7650}.bh span{font:600 24px/1.4 Lora}.bp{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:auto 1fr;gap:8px;padding:20px 18px 26px;align-items:end;background:linear-gradient(transparent calc(100% - 128px),#ead8a6 calc(100% - 128px),#ead8a6 calc(100% - 118px),transparent calc(100% - 118px)),#fffdf3}
.jc{display:flex;flex-direction:column;align-items:center;gap:4px}.jc b{font:700 34px/1.35 Lora;margin-top:8px}.jc span{font:500 18px Roboto;color:#6b5a3a}
.rw3{display:grid;grid-template-columns:1fr 1fr;gap:14px}.rw3 div{background:#3a2a12;color:#fff;border-radius:22px;padding:16px 20px}
.rw3 small{display:block;font:700 14px/1.4 Roboto;letter-spacing:2px;color:#f2d68a}.rw3 b{display:block;font:700 30px/1.3 Lora}.rw3 span{font:500 17px Roboto;color:#e6dcc5}
.rw3 .hl{background:#b23a2a}.rw3 .hl small{color:#ffd9cf}""")

parcels = [("P-301", "Customer 1", "Same city", "1 day", "Packed", "pk"), ("P-302", "Customer 2", "Nearby city", "2 days", "Picked up", "pu"), ("P-303", "Customer 3", "Other state", "4 days", "Picked up", "pu"), ("P-304", "Customer 4", "Same city", "1 day", "Delivered", "dl")]
P["p220_pickle_s4"] = pb(4, "PART 3 · PACK AND SEND", "Every parcel tracked,<br><span>every customer told.</span>",
f'''<div class=w4><div class=lb>{"".join(f'<div class="cd pl"><div class=tp><b>{a}</b><span class="s {k}">{s}</span></div><p>{b} · sample</p><div class=pn><span>{pin}</span><em>{z}</em></div><div class=bc>{"".join(f"<i style=width:{random.choice([2,3,4,6])}px></i>" for _ in range(30))}</div></div>' for a,b,pin,z,s,k in parcels)}</div>
<div class=ms4><small>TEXT TO CUSTOMER 2 · SAMPLE</small><p>Your pickle parcel P-302 is picked up. Track it here: yourpicklekitchen.in/P-302</p></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.lb{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px}
.pl{padding:16px 20px;display:flex;flex-direction:column;justify-content:space-between;border:2px dashed #d9c48a}
.tp{display:flex;justify-content:space-between;align-items:center}.tp b{font:700 34px/1.3 Lora}
.s{font:700 16px Roboto;border-radius:10px;padding:5px 11px}.pk{background:#f2d68a}.pu{background:#3a2a12;color:#fff}.dl{background:#3f7a3a;color:#fff}
.pl p{font:600 25px Roboto}.pn{display:flex;gap:10px;align-items:center}.pn span{font:700 22px Roboto;background:#fbf3dc;border-radius:8px;padding:6px 12px}.pn em{font-style:normal;font:500 21px Roboto;color:#6b5a3a}.bc{height:44px!important}
.bc{display:flex;gap:3px;height:34px}.bc i{display:block;height:100%;background:#3a2a12}
.ms4{background:#b23a2a;color:#fff;border-radius:22px;padding:16px 22px}.ms4 small{font:700 14px/1.4 Roboto;letter-spacing:1.5px;color:#ffd9cf}.ms4 p{font:500 22px/1.45 Roboto;margin-top:4px}""")

P["p220_pickle_s5"] = pb(5, "YOUR TURN", "Sell homemade pickles?<br><span>Let's build your order page.</span>",
f'''<div class=w5><div class="cd j5">{jar(.8,"#e0a21b",280,"Mango")}</div><div class=t5>{"".join(f'<div><span class=ib>{ic(i,32)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("cart","Order page","Jar sizes and address"),("chart","Batch plan","Kg to make this week"),("box","Parcel labels","By delivery zone"),("bell","Tracking texts","Customers told")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#b23a2a;color:#fff",
css=""".w5{flex:1;display:flex;gap:16px;min-height:0}.j5{width:380px;flex:none;display:flex;align-items:center;justify-content:center;gap:10px}
.t5{flex:1;display:grid;grid-template-rows:repeat(4,1fr);gap:12px}.t5 div{background:#3a2a12;color:#fff;border-radius:22px;padding:14px 20px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:16px;align-content:center}
.t5 div:nth-child(2n){background:#b23a2a}.t5 .ib{grid-row:span 2;width:76px;height:76px;border-radius:16px;background:rgba(255,255,255,.14)}.t5 b{font:700 34px/1.3 Lora}.t5 small{font:400 20px/1.35 Roboto;color:#f3e6cf}""")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
