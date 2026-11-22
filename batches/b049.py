import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 261 INDIA · False ceiling contractor · SINGLE · Lora + Fira Sans · ceiling white / cove amber / graphite
# New technique: reflected ceiling plan (top-down) with a glowing cove band, light points and a dropped panel, to scale with the room.
rcp = '''<svg viewBox="0 0 660 520" class=rc2><defs><filter id="gl" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="7"/></filter>
<pattern id="gd" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="#e6e2da" stroke-width="1"/></pattern></defs><g transform="translate(40,0)">
<rect x="30" y="40" width="560" height="420" fill="url(#gd)" stroke="#2a2a2e" stroke-width="8"/>
<rect x="100" y="110" width="420" height="280" fill="none" stroke="#f0a43a" stroke-width="16" filter="url(#gl)"/>
<rect x="100" y="110" width="420" height="280" fill="#fbf7ef" stroke="#2a2a2e" stroke-width="3" stroke-dasharray="10 7"/>
<rect x="210" y="190" width="200" height="120" rx="10" fill="#f3e6cf" stroke="#2a2a2e" stroke-width="3"/>
<circle cx="310" cy="250" r="26" fill="#fff" stroke="#2a2a2e" stroke-width="3"/><circle cx="310" cy="250" r="10" fill="#f0a43a"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="11" fill="#fff" stroke="#2a2a2e" stroke-width="3"/><circle cx="{x}" cy="{y}" r="4" fill="#f0a43a"/>' for x,y in [(65,75),(310,75),(555,75),(65,425),(310,425),(555,425),(65,250),(555,250)]) + '''
<g stroke="#2a2a2e" stroke-width="2.5" fill="#2a2a2e"><line x1="30" y1="490" x2="590" y2="490"/><path d="M30 490 l12 -7 v14z"/><path d="M590 490 l-12 -7 v14z"/><line x1="10" y1="40" x2="10" y2="460"/><path d="M10 40 l-7 12 h14z"/><path d="M10 460 l-7 -12 h14z"/></g>
<rect x="262" y="474" width="96" height="32" rx="8" fill="#fff" stroke="#2a2a2e" stroke-width="2"/><text x="310" y="497" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="22" fill="#2a2a2e">14 ft</text>
<rect x="-16" y="234" width="72" height="32" rx="8" fill="#fff" stroke="#2a2a2e" stroke-width="2"/><text x="20" y="257" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="19" fill="#2a2a2e">12 ft</text>
<text x="310" y="166" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="22" fill="#a86a12">COVE LIGHT ALL ROUND</text>
<text x="310" y="345" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="20" fill="#6b655b">Dropped panel + fan point</text></g></svg>'''
mat = [("Gypsum boards", "12 sheets"), ("Channels and studs", "38 pieces"), ("Cove LED strip", "44 ft"), ("Spot lights", "8 points"), ("Fan hook point", "1")]
P["p261_ceiling"] = page("""
body{--f:'Fira Sans';--h:'Lora';background:#f2efe9;color:#2a2a2e}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#c27a12;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#c27a12}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.pl{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(42,42,46,.08)}
.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#79746b}
.rc2{width:100%;flex:1;min-height:0;display:block}
.vw2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pl{flex-direction:row!important;gap:16px!important}.pv{flex:1;min-width:0;display:flex;flex-direction:column;gap:8px}.dz{width:250px;flex:none;display:flex;flex-direction:column;gap:10px}.dz span{flex:1;display:flex;align-items:center;justify-content:center;border-radius:14px;padding:10px 12px;font:700 21px/1.3 'Fira Sans';background:#f5efe4;border:3px solid transparent;text-align:center}.dz .ok{flex:none}.dz span.on{border-color:#f0a43a;background:#fff4e2}
.sd{width:340px;flex:none;display:flex;flex-direction:column;gap:12px}
.mg{display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:8px}.ml{background:#2a2a2e;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column}
.ml small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#f6c27a}
.mr{display:flex;flex-direction:column;justify-content:center;border-left:3px solid #f0a43a;padding:4px 0 4px 12px}.mr span{font:500 17px 'Fira Sans';color:#c9c5bd}.mr b{font:700 26px/1.35 Lora}
.ok{background:#f0a43a;color:#2a2a2e;border-radius:22px;padding:16px 20px;font:500 19px/1.45 'Fira Sans'}.ok b{font-weight:700}
""", "<div class=kk>FALSE CEILING CONTRACTOR</div><h1>Show the ceiling plan,<br><span>then the material list.</span></h1>",
f'''<div class=vw2><div class=pl><div class=pv><small class=cap>CEILING PLAN · LIVING ROOM 14 × 12 FT · SAMPLE</small>{rcp}</div>
<div class=dz><small class=cap>DESIGN PICKED</small><span>Plain flat</span><span class=on>Cove + panel</span><span>Two levels</span><span>Light: warm white</span><div class=ok>Customer approves on their phone. <b>Your team gets the same list.</b></div></div></div>
<div class=ml><small>MATERIAL LIST · FROM THE PLAN</small><div class=mg>{"".join(f'<div class=mr><span>{a}</span><b>{b}</b></div>' for a,b in mat)}</div></div></div>''',
"#2a2a2e", "Do false ceilings? DM us", "background:#2a2a2e;color:#fff")

# ───────── 262 INDIA · Paneer and dairy products maker · CAROUSEL 5 · Bitter + Source Sans 3 · milk white / cobalt blue / butter yellow
# New technique: CSS 3D paneer blocks (three faces via transforms-free gradients), reused as the unit across slides.
def blk(s=1.0, lbl=""):
    w = int(120*s); h = int(70*s); d = int(36*s)
    return f'<div class=pb style="width:{w+d}px;height:{h+d}px"><i class=tp2 style="width:{w}px;height:{d}px;left:0;top:0;transform:skewX(-45deg);transform-origin:0 100%"></i><i class=fr style="width:{w}px;height:{h}px;left:0;top:{d}px">{lbl}</i><i class=sd2 style="width:{d}px;height:{h}px;left:{w}px;top:{d}px;transform:skewY(-45deg);transform-origin:0 0"></i></div>'
PN = """
body{--f:'Source Sans 3';--h:'Bitter';background:#eef3fb;color:#14306b}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#c28a00;margin-top:22px;align-self:flex-start}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#2d5bd7}
.pb{position:relative;flex:none}.pb i{position:absolute;display:flex;align-items:center;justify-content:center;font:700 18px 'Source Sans 3';font-style:normal;color:#14306b}
.tp2{background:#fffdf4;border:2px solid #14306b}.fr{background:#fff7dc;border:2px solid #14306b}.sd2{background:#f1e2ad;border:2px solid #14306b}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(20,48,107,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b7894}
.nb{display:flex;align-items:center;gap:14px;background:#14306b;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Source Sans 3'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#2d5bd7}.nb b{color:#ffd95a}
"""
def pn(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#14306b;color:#fff"):
    return page(PN + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#14306b", cta, ctacss, tagline=f"{n} / 5")
P["p262_paneer_s1"] = pn(1, "PANEER AND DAIRY PRODUCTS · SHOP SUPPLY", "Paneer orders on calls?<br><span>Put them on one sheet.</span>",
f'''<div class=w1><div class="cd st1"><small class=cap>6 AM · CALLS AND MESSAGES · SAMPLE</small><div class=ms1>{"".join(f'<div class=m1><b>{a}</b><span>{b}</span></div>' for a,b in [("Shop 1","“Same as yesterday”"),("Shop 2","“3 kg… no, make it 4”"),("Shop 3","Missed call"),("Sweet shop","“Paneer and curd, usual”")])}</div></div>
<div class="cd bl1"><div class=bks>{blk(1.7,"? kg")}{blk(1.7,"? kg")}{blk(1.7,"? kg")}</div><p>How much to make tomorrow? <b>Nobody has the total.</b></p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.st1{padding:16px 22px;display:flex;flex-direction:column;gap:10px}
.ms1{display:grid;grid-template-columns:1fr 1fr;gap:10px}.m1{background:#eef3fb;border-radius:16px;padding:14px 18px;border-left:6px solid #2d5bd7}.m1 b{display:block;font:700 24px/1.35 Bitter}.m1 span{font:italic 500 21px 'Source Sans 3';color:#44527a}
.bl1{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:20px}.bks{display:flex;gap:40px;align-items:flex-end}.bks .fr{font-size:30px}
.bl1 p{font:500 26px/1.4 'Source Sans 3'}.bl1 p b{color:#2d5bd7}""")

orders = [("Shop 1 · Market", 4, 20, 0), ("Shop 2 · Colony", 4, 12, 2), ("Shop 3 · Station", 2, 10, 0), ("Sweet shop", 8, 0, 4), ("Hotel", 6, 30, 2)]
P["p262_paneer_s2"] = pn(2, "STEP 1 · ORDERS BY 8 PM", "Each shop orders<br><span>in kg, cups and jars.</span>",
f'''<div class=w2><div class="cd os"><div class=oh><span>SHOP</span><span>PANEER KG</span><span>CURD CUPS</span><span>GHEE JARS</span></div>{"".join(f'<div class=orr><b>{s}</b><em>{a}</em><em>{b or "—"}</em><em>{c or "—"}</em></div>' for s,a,b,c in orders)}
<div class="orr tt"><b>Make tonight</b><em>{sum(o[1] for o in orders)} kg</em><em>{sum(o[2] for o in orders)}</em><em>{sum(o[3] for o in orders)}</em></div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>Shops order on a link. <b>The totals add up by themselves.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.os{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.oh,.orr{display:grid;grid-template-columns:1fr 150px 150px 150px;gap:10px;align-items:center}.oh{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b7894;padding-bottom:10px;border-bottom:2px solid #14306b}.oh span:not(:first-child){text-align:center}
.orr{flex:1;border-bottom:1px solid #e3e9f4}.orr b{font:700 25px/1.35 Bitter}.orr em{font:700 28px 'Source Sans 3';font-style:normal;text-align:center}
.tt{border:0;background:#fff3c4;border-radius:14px;padding:0 12px}.tt em{color:#14306b}""")

P["p262_paneer_s3"] = pn(3, "STEP 2 · MILK NEEDED FOR TOMORROW", "24 kg of paneer.<br><span>How much milk?</span>",
f'''<div class=w3><div class="cd cv"><div class=cvl><small class=cap>PANEER ORDERED</small><div class=bk3>{"".join(blk(0.9) for _ in range(6))}</div><b>24 kg</b></div>
<div class=ar>{ic("arrow",54,w=3)}<span>Your own yield rule<br><b>5 litres = 1 kg</b></span></div>
<div class=cvl><small class=cap>MILK TO KEEP</small><div class=cn>{"".join('<i class=can></i>' for _ in range(3))}</div><b>120 litres</b></div></div>
<div class=sx3>{"".join(f'<div class="cd x3"><span>{a}</span><b>{b}</b></div>' for a,b in [("Curd cups","72 cups · from your cup rule"),("Ghee jars","8 jars · from stock"),("Milk order","Sent to your milk supplier")])}</div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.cv{flex:1;display:flex;align-items:center;justify-content:space-around;padding:20px}
.cvl{display:flex;flex-direction:column;align-items:center;gap:16px}.cvl b{font:800 52px/1.3 Bitter;color:#2d5bd7}
.bk3{display:grid;grid-template-columns:repeat(2,auto);gap:10px 14px}
.ar{display:flex;flex-direction:column;align-items:center;gap:10px;color:#c28a00;text-align:center}.ar span{font:500 20px/1.4 'Source Sans 3';color:#44527a}.ar b{color:#14306b;font-size:24px}
.cn{display:flex;gap:16px;align-items:flex-end}.can{width:84px;height:150px;border:4px solid #14306b;border-radius:18px 18px 10px 10px;background:linear-gradient(#fff 0 18%,#dbe6fb 18%);position:relative}.can:before{content:"";position:absolute;top:-22px;left:22px;width:32px;height:18px;border:4px solid #14306b;border-bottom:0;border-radius:8px 8px 0 0;background:#fff}
.sx3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.x3{padding:16px 20px}.x3 span{display:block;font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b7894;text-transform:uppercase}.x3 b{font:700 23px/1.35 Bitter}""")

crates = [("Shop 1 · Market", "4 kg paneer · 20 curd", "6:15 AM"), ("Shop 2 · Colony", "4 kg · 12 curd · 2 ghee", "6:35 AM"), ("Shop 3 · Station", "2 kg · 10 curd", "6:50 AM"), ("Sweet shop", "8 kg · 4 ghee", "7:10 AM"), ("Hotel", "6 kg · 30 curd · 2 ghee", "7:30 AM")]
P["p262_paneer_s4"] = pn(4, "STEP 3 · CRATE LABELS AND ROUTE", "Every crate packed<br><span>to the right shop.</span>",
f'''<div class=w4><div class=cg>{"".join(f'<div class=cr4><div class=lb4><em>{t}</em><b>{s}</b><span>{d}</span></div></div>' for s,d,t in crates)}<div class="cr4 e"><div class=lb4><b>Printed at 5:30 AM</b><span>One label per crate, sample</span></div></div></div></div>''',
css=""".w4{flex:1;display:flex;min-height:0}.cg{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:14px}
.cr4{border-radius:18px;background:repeating-linear-gradient(90deg,#2d5bd7 0 18px,#2650c2 18px 22px);padding:18px;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 -12px 0 rgba(0,0,0,.18)}
.cr4.e{background:#14306b}
.lb4{background:#fff;border-radius:12px;padding:12px 18px;width:100%;box-shadow:0 6px 12px rgba(0,0,0,.2)}.lb4 em{float:right;font:700 18px 'Source Sans 3';font-style:normal;background:#fff3c4;padding:4px 10px;border-radius:8px}
.lb4{padding:16px 20px!important}.lb4 b{display:block;font:700 30px/1.35 Bitter}.lb4 span{font:500 21px 'Source Sans 3';color:#44527a}""")

P["p262_paneer_s5"] = pn(5, "YOUR TURN", "Make paneer for shops?<br><span>Let's build your order app.</span>",
f'''<div class=w5><div class="cd hp">{blk(2.0,"Paneer")}{blk(1.45,"Curd")}{blk(1.45,"Ghee")}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Order link","Shops order by 8 PM"),("drop","Milk needed","From your yield rule"),("tag","Crate labels","One per shop"),("truck","Morning route","With times")])}</div>
<div class=q>How do shops send you their paneer order today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#2d5bd7;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;justify-content:center;align-items:center;gap:50px}.hp .fr{font-size:26px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(20,48,107,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#fff3c4;color:#c28a00}.ti b{display:block;font:700 30px/1.35 Bitter}.ti div span{font:500 19px/1.35 'Source Sans 3';color:#44527a}
.q{background:#14306b;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Source Sans 3'}""")

# ───────── 263 USA · Mobile locksmith · SINGLE · Anton + DM Sans · brass / charcoal / signal red
# New technique: service-area rings around the van on a street grid, ZIP chips inside/outside, and a lockout call form.
rings = '''<svg viewBox="0 -100 520 760" class=ar2><rect y="-100" width="520" height="760" rx="18" fill="#2b2d31"/>
<path d="M0 -20 H520 M0 120 H520 M0 260 H520 M0 400 H520 M0 540 H520 M110 -100 V660 M250 -100 V660 M390 -100 V660" stroke="#3a3d43" stroke-width="12"/>
<circle cx="250" cy="290" r="230" fill="#d8a63a" fill-opacity=".08" stroke="#d8a63a" stroke-width="3" stroke-dasharray="10 8"/>
<circle cx="250" cy="290" r="140" fill="#d8a63a" fill-opacity=".16" stroke="#d8a63a" stroke-width="3"/>
<rect x="212" y="270" width="76" height="40" rx="10" fill="#d8a63a"/><circle cx="230" cy="314" r="9" fill="#111"/><circle cx="272" cy="314" r="9" fill="#111"/>
<text x="250" y="140" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#f3d58c">ABOUT 20 MIN</text>
<text x="250" y="52" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#cfb57a">ABOUT 40 MIN</text>
<circle cx="340" cy="210" r="15" fill="#e2483d" stroke="#fff" stroke-width="4"/><text x="340" y="250" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="18" fill="#fff">Caller</text></svg>'''
P["p263_locksmith"] = page("""
body{--f:'DM Sans';--h:'Anton';background:#f4f1ea;color:#1e1f22}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#e2483d;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:70px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#b5841c}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.mpc{width:460px;flex:none;background:#1e1f22;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:10px}
.mpc small{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#cfb57a;padding:2px 6px}
.ar2{width:100%;flex:1;min-height:0;display:block}
.zp{display:flex;flex-wrap:wrap;gap:8px}.zp span{font:700 16px 'DM Sans';padding:8px 12px;border-radius:10px;background:#3a3420;color:#f3d58c}.zp span.o{background:#3a2422;color:#f2a19a}
.fm{flex:1;min-width:0;background:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(30,31,34,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7d776b}
.fh{font:400 34px/1.3 'Anton';letter-spacing:.5px}
.ch{display:grid;grid-template-columns:1fr 1fr;gap:8px}.ch span{border:3px solid #e8e2d6;border-radius:14px;padding:14px 10px;text-align:center;font:700 19px 'DM Sans'}.ch span.on{border-color:#e2483d;background:#fdeceb;color:#b3302a}
.ff{flex:1;display:flex;justify-content:space-between;align-items:center;border-radius:14px;background:#f4f1ea;padding:0 16px;font:500 19px 'DM Sans';color:#6a655b}.ff b{color:#1e1f22;font-weight:700}
.go{background:#e2483d;color:#fff;border-radius:16px;padding:16px;text-align:center;font:700 21px 'DM Sans'}
""", "<div class=kk>MOBILE LOCKSMITH · 24/7 CALLS</div><h1>“Locked out. How soon?”<br><span>Answer before they call.</span></h1>",
f'''<div class=vw><div class=mpc><small>SERVICE AREA · SAMPLE CITY</small>{rings}<div class=zp>{"".join(f'<span>{z}</span>' for z in ["ZIP 10001","ZIP 10002","ZIP 10003"])}<span class=o>ZIP 10009 · call first</span></div></div>
<div class=fm><small class=cap>LOCKOUT REQUEST · SAMPLE</small><div class=fh>What's locked?</div>
<div class=ch>{"".join(f'<span class="{"on" if i==1 else ""}">{t}</span>' for i,t in enumerate(["House","Car","Office","Storage unit"]))}</div>
{"".join(f'<div class=ff><span>{a}</span><b>{b}</b></div>' for a,b in [("ZIP code","10002 · in area"),("Where now","Outside, by the car"),("Key type","Push-to-start fob"),("Call back on","Sample number")])}
<div class=go>Send · we call you back</div></div></div>''',
"#1e1f22", "Run a locksmith service? DM us", "background:#1e1f22;color:#f3d58c")

# ───────── 264 INDIA · Bicycle shop · SINGLE · Montserrat + Open Sans · cycle red / asphalt / mint
# New technique: drawn bicycle SVG with numbered service points tied to a checklist and a pickup slot.
bike = '''<svg viewBox="0 0 700 400" class=bk5><g fill="none" stroke="#24282e" stroke-width="10" stroke-linecap="round" stroke-linejoin="round">
<circle cx="160" cy="270" r="105"/><circle cx="540" cy="270" r="105"/></g>
<g fill="none" stroke="#e23b3b" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"><path d="M160 270 L300 270 L250 140 Z"/><path d="M300 270 L450 140 L250 140"/><path d="M450 140 L540 270"/></g>
<g stroke="#24282e" stroke-width="10" stroke-linecap="round"><line x1="250" y1="140" x2="235" y2="100"/><line x1="205" y1="98" x2="270" y2="98"/><line x1="450" y1="140" x2="470" y2="80"/><path d="M445 80 Q480 70 510 90" fill="none"/></g>
<circle cx="300" cy="270" r="26" fill="#fff" stroke="#24282e" stroke-width="8"/>
<path d="M160 270 L300 270" stroke="#9aa3ad" stroke-width="5" stroke-dasharray="3 6"/>''' + "".join(f'<circle cx="{x}" cy="{y}" r="24" fill="#2fb98a" stroke="#fff" stroke-width="5"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="22" fill="#fff">{n}</text>' for n,x,y in [(1,230,295),(2,525,90),(3,640,215),(4,60,215),(5,235,60)]) + '</svg>'
chk = [("Chain clean and oil", True), ("Brake pads, front and back", True), ("Tyre pressure and tubes", True), ("Rear tyre check", False), ("Seat height set", True)]
P["p264_bicycle"] = page("""
body{--f:'Open Sans';--h:'Montserrat';background:#eef6f2;color:#24282e}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#e23b3b;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#1f8f69}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bc{background:#fff;border-radius:26px;padding:14px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(36,40,46,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#707883}
.bk5{width:100%;display:block}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.cl{flex:1;min-width:0;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(36,40,46,.08)}
.cr{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #e9eef0;font:600 20px 'Open Sans'}.cr i{width:32px;height:32px;border-radius:50%;background:#2fb98a;color:#fff;font:800 15px Montserrat;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.cr span{flex:1}.cr em{font:700 15px 'Open Sans';font-style:normal;padding:5px 10px;border-radius:8px;background:#e3f6ee;color:#1f8f69}.cr em.x{background:#fde6e6;color:#c22b2b}
.sl{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.pt{flex:1;background:#24282e;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.pt small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#9fe3c8}.pt b{font:800 34px/1.3 Montserrat}.pt span{font:500 18px/1.4 'Open Sans';color:#c9ced4}
.pt.r{background:#e23b3b}.pt.r small{color:#ffd6d6}.pt.r span{color:#ffe3e3}
""", "<div class=kk>BICYCLE SHOP · SERVICE BOOKINGS</div><h1>Every cycle service,<br><span>point by point.</span></h1>",
f'''<div class=vw><div class=bc><small class=cap>JOB C-264 · SAMPLE CYCLE · SAT 28 NOV</small>{bike}</div>
<div class=bt><div class=cl><small class=cap>SERVICE CHECKLIST</small>{"".join(f'<div class=cr><i>{i+1}</i><span>{a}</span><em class="{"" if ok else "x"}">{"Done" if ok else "Needs new tyre"}</em></div>' for i,(a,ok) in enumerate(chk))}</div>
<div class=sl><div class="pt r"><small>ASK THE CUSTOMER</small><b>Rear tyre</b><span>Photo sent. They reply yes or no.</span></div><div class=pt><small>PICKUP</small><b>Sat 5 PM</b><span>Message goes out when it is ready</span></div></div></div></div>''',
"#24282e", "Run a cycle shop? DM us", "background:#e23b3b;color:#fff")

# ───────── 265 INDIA · Farm honey seller · SINGLE · Gelasio + Poppins · honey amber / hive black / cream
# New technique: hexagon (clip-path) honeycomb as a jar stock grid by batch, with filled vs empty cells.
batches = [("Batch B-11", "Mustard flower", "500 g", 9, 12), ("Batch B-12", "Multi-flower", "250 g", 5, 12), ("Batch B-13", "Forest flower", "1 kg", 11, 12)]
def comb(f, t):
    return "".join(f'<i class="hx{" f" if k < f else ""}"></i>' for k in range(t))
P["p265_honey"] = page("""
body{--f:'Poppins';--h:'Gelasio';background:#fbf3e0;color:#2a1f0e}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#b36b00;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#c98200}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bs{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.bc{background:#fff;border-radius:24px;padding:16px 16px 14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(42,31,14,.08)}
.bc small{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#8a7a5c}
.bc b{font:700 30px/1.3 Gelasio}.bc>span{font:500 18px Poppins;color:#6b5c40}
.cb{flex:1;display:flex;flex-wrap:wrap;align-content:center;justify-content:flex-start;padding:4px 0 0 0;width:270px;align-self:center}
.hx{width:74px;height:84px;margin:0 2px -17px;clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);background:#f1e6cc}
.hx.f{background:linear-gradient(160deg,#ffc94a,#e39a12)}
.cb .hx:nth-child(n+4):nth-child(-n+6),.cb .hx:nth-child(n+10):nth-child(-n+12){transform:translateX(38px)}
.lf{font:700 19px Poppins;text-align:center;border-radius:12px;padding:8px 0;background:#fff4d8;color:#9a5c00;margin-top:12px}
.lf.l{background:#2a1f0e;color:#ffc94a}
.od{display:flex;gap:14px;align-items:center;background:#2a1f0e;color:#fff;border-radius:22px;padding:16px 20px}.od .ib{width:56px;height:56px;border-radius:16px;background:#e39a12;color:#2a1f0e}
.od p{flex:1;font:500 20px/1.45 Poppins}.od p b{color:#ffc94a}
""", "<div class=kk>FARM HONEY · ONLINE ORDERS</div><h1>Which batch, which jar size,<br><span>how many left?</span></h1>",
f'''<div class=vw><div class=bs>{"".join(f'<div class=bc><small>{bn} · SAMPLE</small><b>{fl}</b><span>{sz} jars · 1 cell = 1 jar</span><div class=cb>{comb(f,t)}</div><div class="lf{" l" if f<6 else ""}">{f} of {t} left{" · low" if f<6 else ""}</div></div>' for bn,fl,sz,f,t in batches)}</div>
<div class=od><span class=ib>{ic("cart",28)}</span><p>A customer orders 2 jars of multi-flower 250 g. <b>The comb updates, and the batch number goes on the bill.</b></p></div></div>''',
"#2a1f0e", "Sell farm honey? DM us", "background:#e39a12;color:#2a1f0e")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
