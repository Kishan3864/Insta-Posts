import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 251 INDIA · Mosquito net / window mesh fitter · SINGLE · Archivo Black + Source Sans 3 · slate blue / mint / coral
# New technique: a drawn window with an SVG mesh pattern inside the frame + dimension arrows, tied to a site list of every window.
wins = [("Hall", "60 × 48 in", "Sliding", False), ("Bedroom 1", "48 × 36 in", "Fixed", True), ("Bedroom 2", "48 × 36 in", "Fixed", False), ("Kitchen", "36 × 30 in", "Openable", False), ("Balcony door", "36 × 84 in", "Pleated", False)]
winsvg = '''<svg viewBox="0 0 560 470" class=wsv><defs><pattern id="msh" width="9" height="9" patternUnits="userSpaceOnUse"><path d="M9 0H0V9" fill="none" stroke="#2c3e57" stroke-opacity=".55" stroke-width="1.2"/></pattern>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#cfe9f7"/><stop offset="1" stop-color="#eaf6ef"/></linearGradient></defs>
<rect x="70" y="70" width="400" height="300" rx="6" fill="#3d5170"/><rect x="88" y="88" width="364" height="264" fill="url(#sky)"/>
<path d="M88 300 Q170 250 250 290 T452 270 V352 H88 Z" fill="#9fd8b8"/><circle cx="380" cy="150" r="30" fill="#fff3c9"/>
<rect x="88" y="88" width="364" height="264" fill="url(#msh)"/><rect x="268" y="88" width="6" height="264" fill="#3d5170"/>
<rect x="50" y="370" width="440" height="22" rx="4" fill="#d9e1ea"/>
<g stroke="#e8604c" stroke-width="4" fill="#e8604c"><line x1="70" y1="38" x2="470" y2="38"/><path d="M70 38 l16 -9 v18 z"/><path d="M470 38 l-16 -9 v18 z"/>
<line x1="510" y1="70" x2="510" y2="370"/><path d="M510 70 l-9 16 h18 z"/><path d="M510 370 l-9 -16 h18 z"/></g>
<rect x="210" y="18" width="120" height="40" rx="10" fill="#fff" stroke="#e8604c" stroke-width="3"/><text x="270" y="47" text-anchor="middle" font-family="Archivo Black" font-size="22" fill="#e8604c">48 in</text>
<rect x="466" y="200" width="88" height="40" rx="10" fill="#fff" stroke="#e8604c" stroke-width="3"/><text x="510" y="229" text-anchor="middle" font-family="Archivo Black" font-size="22" fill="#e8604c">36 in</text>
<text x="270" y="440" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="26" fill="#2c3e57">Bedroom 1 · Window 2 · fixed frame</text></svg>'''
P["p251_mesh"] = page("""
body{--f:'Source Sans 3';--h:'Archivo Black';background:#eef3f7;color:#2c3e57}
.kk{font:700 17px/1.4 'Source Sans 3';letter-spacing:3px;color:#e8604c;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.22;margin-top:16px} h1 span{color:#2f9e74}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp{flex:1;min-height:0;display:flex;gap:14px}
.wc{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(44,62,87,.08)}
.cap{font:700 15px/1.4 'Source Sans 3';letter-spacing:2px;color:#6d7d92}
.wsv{width:100%;flex:1;min-height:0;display:block}
.it4{display:grid;grid-template-columns:1fr 1fr;gap:10px}.it4 div{background:#e3f4ec;border-radius:14px;padding:12px 16px}.it4 small{display:block;font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#2f7d5e}.it4 b{font:700 23px/1.35 'Source Sans 3';color:#2c3e57}
.sl{width:380px;flex:none;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(44,62,87,.08)}
.wr{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:1px solid #e6ebf1;padding:0 6px}
.wr b{font:700 24px/1.4 'Source Sans 3';display:flex;justify-content:space-between;margin-bottom:3px}.wr b em{font-style:normal;color:#2c3e57}
.wr span{font:600 18px/1.4 'Source Sans 3';color:#6d7d92}
.wr.on{background:#fdece9;border-radius:14px;border-top-color:transparent}.wr.on b em{color:#e8604c}
.fc{display:grid;grid-template-columns:1fr 1.25fr 1.25fr;gap:12px}
.fx{background:#2c3e57;color:#fff;border-radius:22px;padding:16px 20px}.fx small{display:block;font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#a9e3c8}
.fx b{display:block;font:400 30px/1.35 'Archivo Black';margin-top:4px}.fx span{font:600 18px/1.4 'Source Sans 3';color:#d3dde9}
""", "<div class=kk>MOSQUITO NET AND WINDOW MESH FITTING</div><h1>Every window measured once.<br><span>Every mesh cut right.</span></h1>",
f'''<div class=vw><div class=tp><div class=wc><small class=cap>SITE VISIT · SAMPLE FLAT 302</small>{winsvg}<div class=it4>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a,b in [("OPENS","Fixed, no handle"),("MESH","Grey fibre"),("FRAME","Aluminium"),("PHOTO","Saved with size")])}</div></div>
<div class=sl><small class=cap>ALL WINDOWS · 5 FRAMES</small>{"".join(f'<div class="wr{" on" if o else ""}"><b>{a}<em>{b}</em></b><span>{c} · mesh grey</span></div>' for a,b,c,o in wins)}</div></div>
<div class=fc><div class=fx><small>CUT LIST</small><b>5 frames</b><span>Sent to the workshop</span></div><div class=fx><small>FITTING SLOT</small><b>Wed 25 Nov</b><span>11 AM · 2 fitters</span></div><div class=fx><small>CUSTOMER GETS</small><b>Sizes + slot</b><span>In one message, sample</span></div></div></div>''',
"#2c3e57", "Fit window mesh? DM us", "background:#e8604c;color:#fff")

# ───────── 252 INDIA · Texture wall painting · CAROUSEL 6 · Cardo + Open Sans · terracotta / sand / charcoal
# New technique: CSS-generated wall textures as swatches (comb lines, sand, stone, brush arcs, wash, plaster) reused across slides.
TX = {
 "Comb lines": "repeating-linear-gradient(90deg,#c8643f 0 6px,#d97a52 6px 10px,#b9583a 10px 14px)",
 "Sand finish": "radial-gradient(circle at 20% 30%,rgba(255,255,255,.35) 0 1.5px,transparent 2px) 0 0/9px 9px,radial-gradient(circle at 70% 60%,rgba(0,0,0,.18) 0 1.5px,transparent 2px) 0 0/11px 11px,#d8b98c",
 "Stone look": "radial-gradient(ellipse 40px 26px at 30% 30%,#8f8a82 0 60%,transparent 62%) 0 0/70px 54px,radial-gradient(ellipse 34px 22px at 70% 75%,#a6a198 0 60%,transparent 62%) 0 0/70px 54px,#7b766e",
 "Brush arcs": "repeating-radial-gradient(circle at 0 100%,#e7c9a6 0 8px,#d6b088 8px 12px) 0 0/60px 60px",
 "Soft wash": "radial-gradient(120px 80px at 30% 40%,#f2d9c4,transparent),radial-gradient(140px 90px at 75% 70%,#e6b99a,transparent),#ecc9ad",
 "Rough plaster": "repeating-conic-gradient(from 10deg at 50% 50%,#bdb3a6 0 8deg,#cfc6ba 8deg 20deg) 0 0/26px 26px",
}
TC = """
body{--f:'Open Sans';--h:'Cardo';background:#f4ece1;color:#2b2622}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#c8643f;margin-top:22px;align-self:flex-start}
h1{font-family:'Cardo';font-weight:700;font-size:66px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#c8643f}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(43,38,34,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#857a6e}
.sw{border-radius:16px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.06)}
.nb{display:flex;align-items:center;gap:14px;background:#2b2622;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Open Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#c8643f}.nb b{color:#f3c9a8}
"""
def tc(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2b2622;color:#fff"):
    return page(TC + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2b2622", cta, ctacss, tagline=f"{n} / 6")
P["p252_texture_s1"] = tc(1, "TEXTURE WALL PAINTING · CUSTOMER CHOICE", "“Like the wall in that photo”?<br><span>Show six, get a clear yes.</span>",
f'''<div class=w1><div class=g6>{"".join(f'<div class=t6><div class=sw style="background:{v}"></div><b>{k}</b></div>' for k,v in TX.items())}</div>
<div class=qq><div class=qb>“Not this one… the one with lines, but softer.”</div><div class=qa>A catalogue with names stops the guessing on site.</div></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.g6{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px}
.t6{background:#fff;border-radius:22px;padding:12px;display:flex;flex-direction:column;gap:10px;box-shadow:0 12px 28px rgba(43,38,34,.08)}.t6 .sw{flex:1}.t6 b{font:700 27px/1.4 Cardo;padding:0 6px}
.qq{display:flex;gap:12px}.qb{flex:1.2;background:#fff;border-radius:22px;padding:18px 22px;font:italic 700 27px/1.35 Cardo;border-left:8px solid #c8643f}.qa{flex:1;background:#2b2622;color:#f3c9a8;border-radius:22px;padding:18px 22px;font:600 21px/1.4 'Open Sans'}""")

pick = "Comb lines"
tab = f'''<div class=tb><div class=scr><div class=th><b>Texture catalogue</b><span>Sample studio</span></div><div class=tg>{"".join(f'<div class="ti{" on" if k==pick else ""}"><div class=sw style="background:{v}"></div><span>{k}</span></div>' for k,v in TX.items())}</div>
<div class=pk><span>Picked</span><b>Comb lines · terracotta</b><em>Send to painter</em></div></div></div>'''
P["p252_texture_s2"] = tc(2, "STEP 1 · CATALOGUE ON A TABLET", "They pick by name,<br><span>not by “that one”.</span>",
f'''<div class=w2>{tab}<div class=sd>{"".join(f'<div class=sx><span class=ib>{ic(i,26)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("img","Photo of each texture","From your own past sites"),("tag","Clear names","Comb lines, sand finish…"),("send","Choice saved","Your painter sees it too")])}</div></div>''',
css=""".w2{flex:1;display:flex;gap:16px;min-height:0;align-items:stretch}
.tb{flex:1;min-width:0;background:#2b2622;border-radius:34px;padding:18px;box-shadow:0 24px 44px rgba(43,38,34,.25)}
.scr{height:100%;background:#fbf7f1;border-radius:20px;padding:18px;display:flex;flex-direction:column;gap:12px}
.th{display:flex;justify-content:space-between;align-items:baseline}.th b{font:700 28px Cardo}.th span{font:600 16px 'Open Sans';color:#857a6e}
.tg{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:10px}
.ti{background:#fff;border-radius:16px;padding:8px;display:flex;flex-direction:column;gap:6px;border:3px solid transparent}.ti .sw{flex:1;border-radius:10px}.ti span{font:700 17px 'Open Sans';padding:0 4px}.ti.on{border-color:#c8643f}
.pk{display:flex;align-items:center;gap:12px;background:#f6e3d6;border-radius:14px;padding:12px 14px}.pk span{font:600 15px 'Open Sans';color:#857a6e}.pk b{flex:1;font:700 19px 'Open Sans'}.pk em{font:700 15px 'Open Sans';font-style:normal;background:#c8643f;color:#fff;padding:8px 12px;border-radius:10px}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}.sx{flex:1;background:#fff;border-radius:22px;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:12px;box-shadow:0 12px 28px rgba(43,38,34,.08)}
.sx .ib{width:70px;height:70px;border-radius:20px;background:#f6e3d6;color:#c8643f}.sx b{display:block;font:700 34px/1.4 Cardo;margin-bottom:3px}.sx div span{font:500 21px/1.4 'Open Sans';color:#6b6157}""")

wall = f'''<svg viewBox="0 0 640 460" class=wl><defs><pattern id="cmb" width="14" height="14" patternUnits="userSpaceOnUse"><rect width="14" height="14" fill="#d97a52"/><rect width="5" height="14" fill="#c8643f"/></pattern></defs>
<rect x="60" y="60" width="520" height="340" fill="url(#cmb)"/><rect x="380" y="130" width="140" height="140" fill="#cfe4ee" stroke="#2b2622" stroke-width="5"/><line x1="450" y1="130" x2="450" y2="270" stroke="#2b2622" stroke-width="4"/>
<rect x="30" y="400" width="580" height="14" fill="#8a7e72"/>
<g stroke="#2b2622" stroke-width="3" fill="#2b2622"><line x1="60" y1="30" x2="580" y2="30"/><path d="M60 30 l14 -8 v16z"/><path d="M580 30 l-14 -8 v16z"/><line x1="610" y1="60" x2="610" y2="400"/><path d="M610 60 l-8 14 h16z"/><path d="M610 400 l-8 -14 h16z"/></g>
<rect x="265" y="12" width="110" height="36" rx="8" fill="#fff" stroke="#2b2622" stroke-width="3"/><text x="320" y="38" text-anchor="middle" font-family="Open Sans" font-weight="800" font-size="21" fill="#2b2622">14 ft</text>
<rect x="566" y="212" width="88" height="36" rx="8" fill="#fff" stroke="#2b2622" stroke-width="3"/><text x="610" y="238" text-anchor="middle" font-family="Open Sans" font-weight="800" font-size="21" fill="#2b2622">10 ft</text>
<rect x="392" y="282" width="116" height="36" rx="8" fill="#2b2622"/><text x="450" y="307" text-anchor="middle" font-family="Open Sans" font-weight="800" font-size="19" fill="#fff">4 × 4 ft</text></svg>'''
P["p252_texture_s3"] = tc(3, "STEP 2 · MEASURE THE WALL", "Wall minus window,<br><span>worked out for you.</span>",
f'''<div class=w3><div class="cd wc"><small class=cap>LIVING ROOM · FEATURE WALL · SAMPLE</small>{wall}</div>
<div class=mt>{"".join(f'<div class="mx{" t" if t else ""}"><span>{a}</span><b>{b}</b></div>' for a,b,t in [("Wall 14 × 10 ft","140 sq ft",False),("Window 4 × 4 ft","− 16 sq ft",False),("To texture","124 sq ft",True)])}</div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.wc{flex:1;min-height:0;padding:18px 22px;display:flex;flex-direction:column;gap:8px}.wl{flex:1;min-height:0;width:100%;display:block}
.mt{display:grid;grid-template-columns:1fr 1fr 1.1fr;gap:12px}.mx{background:#fff;border-radius:22px;padding:16px 20px;box-shadow:0 12px 28px rgba(43,38,34,.08)}.mx span{display:block;font:600 19px/1.4 'Open Sans';color:#6b6157;margin-bottom:4px}.mx b{display:block;font:700 44px/1.4 Cardo}
.mx.t{background:#c8643f;color:#fff}.mx.t span{color:#ffe2d0}""")

qrows = [("Living room wall", "124 sq ft", "Comb lines", "2 days"), ("Bedroom, bed wall", "96 sq ft", "Sand finish", "1 day"), ("Passage wall", "60 sq ft", "Soft wash", "1 day"), ("Balcony wall", "70 sq ft", "Rough plaster", "1 day")]
P["p252_texture_s4"] = tc(4, "STEP 3 · QUOTE, WALL BY WALL", "A clear quote<br><span>they can say yes to.</span>",
f'''<div class=w4><div class=dq><div class=dh><div><b>Quote · Q-252</b><span>Sample home · Mon 23 Nov · sample</span></div><em>Texture work</em></div>
<div class=qh><span>WALL</span><span>AREA</span><span>TEXTURE</span><span>DAYS</span></div>
{"".join(f'<div class=qr><b>{a}</b><em>{b}</em><span><i class=sw style="background:{TX[c]}"></i>{c}</span><em>{d}</em></div>' for a,b,c,d in qrows)}
<div class="qr tt"><b>Total</b><em>350 sq ft</em><span>4 textures</span><em>5 days</em></div>
<div class=rt>Your own rate per sq ft is added for each texture. Accept online, and the start date is booked.</div></div></div>''',
css=""".w4{flex:1;display:flex;min-height:0}.dq{flex:1;background:#fffdf9;border-radius:14px;padding:24px 28px;display:flex;flex-direction:column;box-shadow:0 22px 44px rgba(43,38,34,.14);border-top:12px solid #c8643f}
.dh{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:14px;border-bottom:2px solid #2b2622}.dh b{display:block;font:700 36px/1.4 Cardo;margin-bottom:4px}.dh span{font:600 17px 'Open Sans';color:#857a6e}.dh em{font:700 16px 'Open Sans';font-style:normal;background:#f6e3d6;color:#c8643f;padding:8px 14px;border-radius:10px}
.qh,.qr{display:grid;grid-template-columns:1.35fr 140px 1.2fr 90px;gap:12px;align-items:center}.qh{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#857a6e;padding:14px 0 8px}
.qr{flex:1;border-bottom:1px solid #eee5da}.qr b{font:700 25px/1.3 Cardo}.qr em{font:700 21px 'Open Sans';font-style:normal}.qr span{display:flex;align-items:center;gap:10px;font:600 19px 'Open Sans'}.qr .sw{width:40px;height:40px;border-radius:10px;flex:none}
.qr.tt{border:0;background:#f6e3d6;border-radius:14px;padding:0 14px;margin-top:8px}
.rt{margin-top:14px;font:500 19px/1.45 'Open Sans';color:#6b6157}""")

days = [("Mon 30 Nov", "Comb lines", "Living room, day 1", 1), ("Tue 1 Dec", "Comb lines", "Living room, finish", 1), ("Wed 2 Dec", "Sand finish", "Bedroom, bed wall", 3), ("Thu 3 Dec", "Soft wash", "Passage wall", 0), ("Fri 4 Dec", "Rough plaster", "Balcony wall", 0)]
P["p252_texture_s5"] = tc(5, "STEP 4 · SITE DAYS AND PHOTOS", "Customer sees each day<br><span>without calling you.</span>",
f'''<div class=w5><div class="cd dl">{"".join(f'<div class=dr><em>{d}</em><i class=sw style="background:{TX[t]}"></i><div><b>{t}</b><span>{w}</span></div><s class="p{s}">{["Next","Photo sent","","Today"][s]}</s></div>' for d,t,w,s in days)}</div>
<div class=nb><span class=ib>{ic("camera",26)}</span><span>Every evening, the painter adds one photo. <b>The customer gets it with tomorrow's plan.</b></span></div></div>''',
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.dl{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.dr{flex:1;display:grid;grid-template-columns:150px 70px 1fr 150px;gap:16px;align-items:center;border-bottom:1px solid #eee5da}.dr:last-child{border:0}
.dr em{font:700 20px 'Open Sans';font-style:normal;color:#857a6e}.dr .sw{width:66px;height:66px;border-radius:14px}.dr b{display:block;font:700 30px/1.4 Cardo;margin-bottom:3px}.dr div span{font:500 19px 'Open Sans';color:#6b6157}
.dr s{text-decoration:none;font:700 16px 'Open Sans';text-align:center;padding:8px 0;border-radius:10px}.dr s.p1,.dr s.p2{background:#e4efe2;color:#3f7a3a}.dr s.p3{background:#c8643f;color:#fff}.dr s.p0{background:#f4ece1;color:#857a6e}""")
days_fix = None

P["p252_texture_s6"] = tc(6, "YOUR TURN", "Do texture painting?<br><span>Let's build your quote app.</span>",
f'''<div class=w6><div class=hw>{"".join(f'<div class=sw style="background:{TX[k]}"></div>' for k in ["Comb lines","Sand finish","Stone look","Brush arcs"])}</div>
<div class=tl>{"".join(f'<div class=tt2><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("img","Catalogue","Textures by name"),("grid","Wall sizes","Minus doors, windows"),("doc","Quote","Wall by wall"),("camera","Site days","A photo each evening")])}</div>
<div class=q>How do customers choose a texture with you today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#c8643f;color:#fff",
css=""".w6{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hw{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;background:#fff;border-radius:24px;padding:14px;box-shadow:0 12px 28px rgba(43,38,34,.08)}.hw .sw{border-radius:14px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.tt2{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(43,38,34,.07)}
.tt2 .ib{width:72px;height:72px;border-radius:20px;background:#f6e3d6;color:#c8643f}.tt2 b{display:block;font:700 32px/1.4 Cardo;margin-bottom:3px}.tt2 div span{font:500 19px/1.35 'Open Sans';color:#6b6157}
.q{background:#2b2622;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Open Sans'}""")

# ───────── 253 USA · Moving labor only (load / unload crews) · SINGLE · TeX Gyre Adventor + Roboto · kraft tan / forest green / white
# New technique: room-by-room item counter with drawn box tallies + a crew time bar split into load / drive / unload.
rooms = [("Living room", [("Couch", 1), ("TV + stand", 1), ("Boxes", 8)]), ("Bedroom", [("Queen bed", 1), ("Dresser", 1), ("Boxes", 10)]), ("Kitchen", [("Table + 4 chairs", 1), ("Boxes", 9)])]
P["p253_movers"] = page("""
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#efe4d2;color:#1e3b2c}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#2f6b45;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#2f6b45}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.il{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(30,59,44,.08)}
.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#7c7060}
.rm{font:700 22px/1.3 'TeX Gyre Adventor';color:#2f6b45;padding:12px 0 4px}
.it{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #efe8dc}
.it span{flex:1;font:500 21px 'Roboto'}
.bx{display:flex;gap:4px;flex-wrap:wrap;width:150px;justify-content:flex-end}.bx i{width:14px;height:14px;background:#c9a46c;border:2px solid #8a6a3a;border-radius:2px}
.st{display:flex;align-items:center;gap:8px}.st em{width:34px;height:34px;border-radius:10px;background:#efe4d2;font:700 20px/34px Roboto;font-style:normal;text-align:center}.st b{width:34px;text-align:center;font:700 22px Roboto}
.rc{width:380px;flex:none;display:flex;flex-direction:column;gap:12px}
.cr{flex:1;background:#1e3b2c;color:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.cr small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#b9dcc5}
.cr .bg{font:700 46px/1.25 'TeX Gyre Adventor'}.cr .bg span{display:block;font:500 19px/1.4 Roboto;color:#cfe3d6}
.dl{flex:1;display:flex;flex-direction:column}.dl div{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:1px solid #34584a}.dl span{font:600 15px/1.4 Roboto;letter-spacing:1px;color:#b9dcc5;text-transform:uppercase}.dl b{font:600 21px/1.35 Roboto}
.tb{display:flex;height:56px;border-radius:12px;overflow:hidden;font:700 16px Roboto}.tb span{display:flex;align-items:center;justify-content:center;color:#1e3b2c}
.tl{display:flex;justify-content:space-between;font:600 15px Roboto;color:#b9dcc5}
.rl{background:#fff;border-radius:22px;padding:14px 20px;font:500 19px/1.45 Roboto;box-shadow:0 14px 30px rgba(30,59,44,.08)}.rl b{color:#2f6b45}
.cf{background:#f4b860;color:#1e3b2c;border-radius:14px;padding:14px;text-align:center;font:700 19px Roboto}
""", "<div class=kk>LOADING AND UNLOADING CREWS · BOOKINGS</div><h1>“How many movers do I need?”<br><span>Their item list answers it.</span></h1>",
f'''<div class=vw><div class=il><small class=cap>CUSTOMER'S ITEM LIST · SAMPLE</small>{"".join(f'<div class=rm>{r}</div>' + "".join(f'<div class=it><span>{a}</span><div class=bx>{"".join("<i></i>" for _ in range(n)) if a=="Boxes" else ""}</div><div class=st><em>−</em><b>{n}</b><em>+</em></div></div>' for a,n in its) for r,its in rooms)}</div>
<div class=rc><div class=cr><small>CREW PLAN · SAT 28 NOV</small><div class=bg>2 movers<span>From 32 items + 2nd floor stairs, using your own rule</span></div>
<div class=dl>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [("Stairs","2nd floor, no lift"),("Heavy items","Couch, dresser"),("Your rule","1 mover per 40 items, +1 for stairs")])}</div>
<div class=tb><span style="flex:3;background:#f4b860">Load</span><span style="flex:1;background:#cfe3d6">Drive</span><span style="flex:2;background:#9fcfb0">Unload</span></div><div class=tl><span>9 AM</span><span>about 3 hours</span><span>12 PM</span></div>
<div class=cf>Book 9 AM slot</div></div>
<div class=rl>Truck: <b>customer's own rental</b>. Your crew only loads and unloads.</div></div></div>''',
"#1e3b2c", "Run a moving crew? DM us", "background:#2f6b45;color:#fff")

# ───────── 254 INDIA · Computer classes for seniors · SINGLE · Crimson Text + Poppins · chalk green / cream / tomato
# New technique: a CSS keyboard with today's lesson keys lit up, plus batch seats and a printed practice sheet.
rowsK = [list("QWERTYUIOP"), list("ASDFGHJKL"), list("ZXCVBNM")]
lit = {"C", "V"}
kb = '<div class=kb>' + "".join(f'<div class=kr>{"<span class=\"k w\">Ctrl</span>" if i==2 else ""}{"".join(f"<span class=\"k{" on" if c in lit else ""}\">{c}</span>" for c in r)}</div>' for i,r in enumerate(rowsK)) + '<div class=kr><span class="k on w">Ctrl</span><span class="k sp">Space</span><span class="k w">Enter</span></div></div>'
P["p254_seniors"] = page("""
body{--f:'Poppins';--h:'Crimson Text';background:#f6f0e2;color:#22382f}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#d1493a;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#2d6a55}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ls{flex:1;min-height:0;background:#22382f;color:#fff;border-radius:28px;padding:18px 24px;display:flex;flex-direction:column;gap:12px}
.ls small{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#a9d5c2}
.lt{display:flex;justify-content:space-between;align-items:flex-end}.lt b{font:700 40px/1.25 'Crimson Text'}.lt em{font:600 17px Poppins;font-style:normal;background:#d1493a;padding:8px 14px;border-radius:10px}
.kb{flex:1;display:flex;flex-direction:column;gap:12px;justify-content:center;background:#2f4a3f;border-radius:18px;padding:14px}
.kr{display:flex;gap:8px;justify-content:center}
.k{width:78px;height:76px;border-radius:12px;background:#f6f0e2;color:#22382f;font:600 26px/76px Poppins;text-align:center;box-shadow:0 5px 0 #b9b19f}
.k.w{width:118px;font-size:21px}.k.sp{width:420px;font-size:21px}.k.on{background:#ffd15c;box-shadow:0 5px 0 #c99a1e}
.sp2{display:flex;gap:14px;font:500 20px/1.4 Poppins;color:#e6efe9}.sp2 b{color:#ffd15c}
.bt{display:flex;gap:14px}
.bs{flex:1.3;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(34,56,47,.08)}
.cap{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#7b7464}
.br{display:flex;align-items:center;gap:12px;border-top:1px solid #efe8d8;padding:10px 0}.br b{flex:1;font:700 26px/1.25 'Crimson Text'}.br b span{display:block;font:500 16px Poppins;color:#7b7464}
.seat{display:flex;gap:5px}.seat i{width:20px;height:20px;border-radius:6px;background:#2d6a55}.seat i.f{background:#e7e0cf}
.br em{font:600 16px Poppins;font-style:normal;width:90px;text-align:right;color:#2d6a55}
.ps{flex:1;background:#fffdf6 repeating-linear-gradient(transparent 0 33px,#e7dfcb 33px 34px);border-radius:8px;padding:16px 20px;box-shadow:0 14px 30px rgba(34,56,47,.12);border-left:6px solid #d1493a}
.ps small{color:#d1493a}.ps p{font:500 19px/34px Poppins;margin-top:6px}.ps p b{font-weight:700}
""", "<div class=kk>COMPUTER CLASSES FOR SENIORS</div><h1>One small skill a day,<br><span>at their own pace.</span></h1>",
f'''<div class=vw><div class=ls><small>TODAY'S LESSON · TUE 24 NOV · SAMPLE</small><div class=lt><b>Copy a photo into a message</b><em>Lesson 6 of 20</em></div>{kb}
<div class=sp2><span>Keys today: <b>Ctrl + C</b> to copy, <b>Ctrl + V</b> to paste.</span></div></div>
<div class=bt><div class=bs><small class=cap>BATCHES · SEATS · SAMPLE</small>{"".join(f'<div class=br><b>{a}<span>{b}</span></b><div class=seat>{"".join("<i></i>" for _ in range(t)) + "".join("<i class=f></i>" for _ in range(8-t))}</div><em>{8-t} left</em></div>' for a,b,t in [("Morning batch","Mon, Wed, Fri · 11 AM",6),("Evening batch","Tue, Thu · 4 PM",3)])}</div>
<div class=ps><small class=cap>PRACTICE SHEET · TAKE HOME</small><p>1. Open the photo.<br>2. Press <b>Ctrl + C</b>.<br>3. Open the chat. Press <b>Ctrl + V</b>.</p></div></div></div>''',
"#22382f", "Teach computers to seniors? DM us", "background:#d1493a;color:#fff")

# ───────── 255 INDIA · Sofa and curtain fabric store · SINGLE · Lora + Montserrat · plum velvet / mustard / linen
# New technique: hanging swatch cards on a brass rail, each with a CSS weave (velvet sheen, herringbone, linen slub, chenille stripe).
FAB = [
 ("V-12", "Plum velvet", "Sofa", "linear-gradient(115deg,#4a1d3f 0%,#7a3566 45%,#4a1d3f 60%,#5e2750 100%)"),
 ("Z-07", "Grey chevron", "Sofa", "linear-gradient(135deg,#a6aab0 25%,transparent 25%) -12px 0/24px 24px,linear-gradient(225deg,#a6aab0 25%,transparent 25%) -12px 0/24px 24px,linear-gradient(315deg,#a6aab0 25%,transparent 25%) 0 0/24px 24px,linear-gradient(45deg,#a6aab0 25%,transparent 25%) 0 0/24px 24px,#8b8f96"),
 ("L-04", "Natural linen", "Curtain", "repeating-linear-gradient(0deg,rgba(120,100,70,.18) 0 1px,transparent 1px 4px),repeating-linear-gradient(90deg,rgba(120,100,70,.14) 0 1px,transparent 1px 5px),#e8dcc4"),
 ("C-21", "Mustard chenille", "Sofa", "repeating-linear-gradient(90deg,#d79f1f 0 10px,#c18a12 10px 13px),#d79f1f"),
 ("S-09", "Sheer white", "Curtain", "repeating-linear-gradient(90deg,rgba(255,255,255,.9) 0 14px,rgba(235,232,226,.9) 14px 22px),#f4f1ea"),
]
ordr = [("Sofa 3 + 1 + 1", "V-12 Plum velvet", "18 m"), ("Cushions × 4", "C-21 Mustard", "2 m"), ("Curtains · 2 windows", "L-04 Linen", "14 m"), ("Sheer layer", "S-09 Sheer white", "14 m")]
P["p255_fabric"] = page("""
body{--f:'Montserrat';--h:'Lora';background:#f3ece2;color:#3a1631}
.kk{font:700 16px/1.4 'Montserrat';letter-spacing:3px;color:#b37f0e;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:60px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#7a3566}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.rl{position:relative;background:#fff;border-radius:26px;padding:16px 20px 18px;box-shadow:0 14px 30px rgba(58,22,49,.08);flex:1.15;min-height:0;display:flex;flex-direction:column}
.cap{font:700 14px/1.4 'Montserrat';letter-spacing:2px;color:#86707f}
.bar{height:14px;border-radius:7px;background:linear-gradient(#e7c46a,#a37a1b);margin:12px 0 0}
.sws{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:12px;min-height:0}
.sc{display:flex;flex-direction:column;align-items:center;min-height:0}
.hk{width:4px;height:22px;background:#a37a1b}
.cl{flex:1;width:100%;border-radius:10px 10px 14px 14px;box-shadow:0 10px 18px rgba(58,22,49,.18);border:1px solid rgba(0,0,0,.08)}
.tg{margin-top:-30px;background:#fff;border-radius:10px;padding:7px 10px;text-align:center;box-shadow:0 6px 12px rgba(0,0,0,.12);width:86%}
.tg b{display:block;font:700 19px/1.3 Montserrat}.tg span{font:600 14px Montserrat;color:#86707f}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.od{flex:1;min-width:0;background:#3a1631;color:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column}
.od small{font:700 14px/1.4 'Montserrat';letter-spacing:2px;color:#e7c46a}
.orw{flex:1;display:grid;grid-template-columns:1fr 1fr 80px;gap:10px;align-items:center;border-top:1px solid #57304d}
.orw b{font:700 22px/1.3 Lora}.orw span{font:500 17px/1.35 Montserrat;color:#e4cfdd}.orw em{font:700 22px Montserrat;font-style:normal;text-align:right;color:#e7c46a}
.ln{width:300px;flex:none;display:flex;flex-direction:column;gap:12px}
.lb{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 14px 30px rgba(58,22,49,.08)}
.lb b{font:700 30px/1.3 Lora;color:#7a3566}.lb span{font:500 18px/1.4 Montserrat;color:#5d4656}
.lb.y{background:#d79f1f;color:#3a1631}.lb.y b{color:#3a1631}.lb.y span{color:#3a1631}
""", "<div class=kk>SOFA AND CURTAIN FABRIC STORE</div><h1>“Send me photos of the fabrics”?<br><span>Send your catalogue link.</span></h1>",
f'''<div class=vw><div class=rl><small class=cap>SWATCH CATALOGUE · SAMPLE CODES</small><div class=bar></div><div class=sws>{"".join(f'<div class=sc><i class=hk></i><div class=cl style="background:{bg}"></div><div class=tg><b>{c}</b><span>{n}</span></div></div>' for c,n,u,bg in FAB)}</div></div>
<div class=bt><div class=od><small>MEASUREMENT ORDER · SAMPLE HOME</small>{"".join(f'<div class=orw><b>{a}</b><span>{b}</span><em>{m}</em></div>' for a,b,m in ordr)}</div>
<div class=ln><div class=lb><b>48 m</b><span>total cloth, worked out from the sizes</span></div><div class="lb y"><b>Sat 28 Nov</b><span>tailor visit to fit curtains</span></div></div></div></div>''',
"#3a1631", "Sell sofa fabrics? DM us", "background:#7a3566;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
