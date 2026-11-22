import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 256 INDIA · Mobile screen guard kiosk · SINGLE · Anton + Poppins · pegboard tan / electric violet / black
# New technique: a pegboard (radial-gradient holes) with hanging guard packets per screen size, count badges, and a token queue.
pk = [("6.1 in", "Glass", 14, False), ("6.5 in", "Glass", 3, True), ("6.7 in", "Glass", 9, False), ("6.1 in", "Matte", 2, True), ("6.5 in", "Matte", 11, False), ("6.7 in", "Privacy", 6, False)]
queue = [("T-21", "6.5 in glass", "Fitting now", "n"), ("T-22", "6.7 in privacy", "Next · 4 min", "x"), ("T-23", "6.1 in matte", "Waiting", "w"), ("T-24", "6.5 in glass", "Waiting", "w")]
P["p256_guard"] = page("""
body{--f:'Poppins';--h:'Anton';background:#f1ece4;color:#17131f}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#6b3df5;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:70px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#6b3df5}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.pb{flex:1;min-width:0;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;background:radial-gradient(circle,#8a6a45 0 4px,transparent 5px) 0 0/30px 30px,#c9a578;box-shadow:inset 0 0 0 8px #b38d5c}
.pb>small{align-self:flex-start;font:600 14px/1.4 'Poppins';letter-spacing:2px;background:#17131f;color:#fff;padding:6px 12px;border-radius:8px}
.pg2{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:14px 18px}
.pc{display:flex;flex-direction:column;align-items:center}
.pc i{width:10px;height:24px;background:#5b5b5b;border-radius:5px 5px 0 0}
.pt{flex:1;width:100%;background:#fff;border-radius:12px;position:relative;padding:22px 14px 10px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:0 8px 16px rgba(23,19,31,.2)}
.pt:before{content:"";position:absolute;top:8px;left:50%;width:34px;height:8px;margin-left:-17px;border-radius:5px;background:#c9a578}
.pt b{font:400 52px/1.3 'Anton';letter-spacing:.5px}.pt span{font:600 20px 'Poppins';color:#6b647a}.pt u{position:absolute;right:22px;top:26px;width:46px;height:84px;border:4px solid #17131f;border-radius:10px;background:linear-gradient(160deg,#ebe5ff,#fff)}.pt u:after{content:'';position:absolute;top:5px;left:50%;width:12px;height:4px;margin-left:-6px;border-radius:2px;background:#17131f}
.pt em{position:absolute;right:10px;bottom:10px;font:700 18px Poppins;font-style:normal;background:#ebe5ff;color:#6b3df5;padding:4px 12px;border-radius:10px}
.pt.lo em{background:#ffe1e1;color:#d43b3b}
.rc{width:350px;flex:none;display:flex;flex-direction:column;gap:12px}
.qq{flex:1;background:#17131f;color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}
.qq small,.lw small{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#b9a6ff}
.qr{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #2c2638}
.qr b{font:400 34px/1.3 'Anton';letter-spacing:.5px;width:84px}.qr div{flex:1;font:600 21px/1.35 Poppins}.qr div span{display:block;font:500 17px Poppins;color:#a79fb8}
.qr.n b{color:#c9b8ff}.qr.n div span{color:#c9b8ff}
.lw{background:#6b3df5;color:#fff;border-radius:24px;padding:16px 18px}.lw small{color:#e3dbff}.lw p{font:500 19px/1.45 Poppins;margin-top:4px}.lw p b{font-weight:700}
""", "<div class=kk>SCREEN GUARD AND MOBILE ACCESSORIES KIOSK</div><h1>“Size 6.5 is over?”<br><span>See it before the customer asks.</span></h1>",
f'''<div class=vw><div class=pb><small>WALL STOCK · BY SCREEN SIZE · SAMPLE</small><div class=pg2>{"".join(f'<div class=pc><i></i><div class="pt{" lo" if lo else ""}"><u></u><b>{a}</b><span>{t}</span><em>{n} left</em></div></div>' for a,t,n,lo in pk)}</div></div>
<div class=rc><div class=qq><small>FITTING QUEUE · TOKENS</small>{"".join(f'<div class="qr {c}"><b>{t}</b><div>{a}<span>{s}</span></div></div>' for t,a,s,c in queue)}</div>
<div class=lw><small>LOW STOCK · ORDER TODAY</small><p><b>6.5 in glass</b> and <b>6.1 in matte</b> are under 5. Added to your supplier list.</p></div></div></div>''',
"#17131f", "Run a mobile kiosk? DM us", "background:#6b3df5;color:#fff")

# ───────── 257 USA · Piano tuner · CAROUSEL 5 · Gelasio + DM Sans · ebony / ivory / brass
# New technique: a drawn piano keyboard band that runs through every slide; client cards with "last tuned" ribbons; route by town.
def keys(n=21, hl=()):
    w = 100 / n
    whites = "".join(f'<i class="wk{" hl" if i in hl else ""}" style="left:{i*w:.3f}%;width:{w:.3f}%"></i>' for i in range(n))
    blacks = "".join(f'<i class=bk style="left:{(i+1)*w - w*0.3:.3f}%;width:{w*0.6:.3f}%"></i>' for i in range(n-1) if i % 7 not in (2, 6))
    return f'<div class=kbd>{whites}{blacks}</div>'
PT = """
body{--f:'DM Sans';--h:'Gelasio';background:#f7f1e3;color:#141210}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#a77b2c;margin-top:22px;align-self:flex-start}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#a77b2c}
.kbd{position:relative;height:110px;border-radius:0 0 10px 10px;overflow:hidden;background:#141210;border:6px solid #141210;border-top-width:14px;flex:none}
.wk{position:absolute;top:0;bottom:0;background:#fffaf0;border-right:2px solid #141210;border-radius:0 0 4px 4px}.wk.hl{background:#e8c477}
.bk{position:absolute;top:0;height:62%;background:#141210;border-radius:0 0 4px 4px;z-index:2}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(20,18,16,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#857b6a}
.nb{display:flex;align-items:center;gap:14px;background:#141210;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#a77b2c}.nb b{color:#e8c477}
"""
def pt(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#141210;color:#fff"):
    return page(PT + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#141210", cta, ctacss, tagline=f"{n} / 5")
P["p257_piano_s1"] = pt(1, "PIANO TUNING · HOME VISITS", "“When was it last tuned?”<br><span>Nobody remembers.</span>",
f'''<div class=w1><div class="cd pn"><small class=cap>A CLIENT'S UPRIGHT PIANO · SAMPLE</small>{keys(21, (9,))}<div class=ns><div class=nt>“Maybe two years ago? Or was it before we moved?”</div><div class=nt2>Your notebook: <b>a phone number</b> and the word <b>“upright”</b>.</div></div></div>
<div class=pr>{"".join(f'<div class=px><b>{a}</b><span>{b}</span></div>' for a,b in [("No date","Of the last visit"),("No reminder","So they forget"),("No route","Visits all over town")])}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pn{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:14px}.pn .kbd{height:220px}
.ns{flex:1;display:grid;grid-template-columns:1.2fr 1fr;gap:12px}.nt{background:#f7f1e3;border-radius:18px;padding:20px 22px;font:italic 700 30px/1.4 Gelasio;display:flex;align-items:center}.nt2{background:#141210;color:#fff;border-radius:18px;padding:20px 22px;font:500 23px/1.45 'DM Sans';display:flex;align-items:center}.nt2 b{color:#e8c477;display:contents}
.pr{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.px{background:#fff;border-radius:20px;padding:16px 20px;border-top:6px solid #a77b2c}.px b{display:block;font:700 30px/1.35 Gelasio}.px span{font:500 18px 'DM Sans';color:#5f574a}""")

clients = [("Sample home 1", "Upright", "Last tuned 14 Nov 2025", "Due now", "d"), ("Sample school hall", "Grand", "Last tuned 3 Jun 2026", "Due Dec 2026", "s"), ("Sample home 2", "Upright", "Last tuned 22 Aug 2026", "Due Feb 2027", "o"), ("Sample studio", "Baby grand", "Last tuned 10 Oct 2026", "Due Apr 2027", "o")]
P["p257_piano_s2"] = pt(2, "STEP 1 · EVERY PIANO ON FILE", "Each piano keeps<br><span>its own history.</span>",
f'''<div class=w2>{"".join(f'<div class="cd cc"><div class=pi>{keys(10)}</div><div class=ct><b>{a}</b><span>{t} · {l}</span></div><em class="{c}">{d}</em></div>' for a,t,l,d,c in clients)}
<div class=nb><span class=ib>{ic("bell",26)}</span><span>Your rule: every 6 or 12 months. <b>The reminder goes out on its own.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.cc{flex:1;display:flex;align-items:center;gap:20px;padding:14px 22px}
.pi{width:170px;flex:none}.pi .kbd{height:96px;border-width:4px;border-top-width:10px}
.ct{flex:1}.ct b{display:block;font:700 32px/1.35 Gelasio}.ct span{font:500 20px 'DM Sans';color:#5f574a}
.cc em{font:700 18px 'DM Sans';font-style:normal;padding:10px 16px;border-radius:12px;width:170px;text-align:center}.cc em.d{background:#a77b2c;color:#fff}.cc em.s{background:#f6e6c4;color:#7a5718}.cc em.o{background:#eef0ea;color:#4f6a4a}""")

route = [("9:00 AM", "Sample home 1", "Upright · North side"), ("11:00 AM", "Sample home 4", "Upright · North side"), ("1:30 PM", "Sample studio 2", "Baby grand · North side"), ("3:30 PM", "Sample home 7", "Upright · North side")]
mp = '''<svg viewBox="0 0 420 860" class=mp><rect width="420" height="860" rx="18" fill="#efe7d4"/>
<path d="M0 170 H420 M0 350 H420 M0 520 H420 M0 690 H420 M140 0 V860 M290 0 V860" stroke="#fffaf0" stroke-width="16"/><path d="M60 0 Q120 420 40 860" stroke="#cfe0e6" stroke-width="22" fill="none"/>
<rect x="150" y="20" width="250" height="140" rx="14" fill="#e8c477" fill-opacity=".45" stroke="#a77b2c" stroke-width="3" stroke-dasharray="10 8"/>
<text x="275" y="62" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="22" fill="#7a5718">NORTH SIDE · TUE</text>
<path d="M190 130 L250 100 L320 130 L360 95" stroke="#141210" stroke-width="5" fill="none" stroke-dasharray="2 10" stroke-linecap="round"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="19" fill="#141210"/><text x="{x}" y="{y+7}" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="19" fill="#e8c477">{i}</text>' for i,(x,y) in enumerate([(190,130),(250,100),(320,130),(360,95)],1)) + '''
<circle cx="210" cy="430" r="14" fill="#c8bda6"/><circle cx="350" cy="590" r="14" fill="#c8bda6"/><circle cx="210" cy="590" r="14" fill="#c8bda6"/><circle cx="80" cy="770" r="14" fill="#c8bda6"/><circle cx="360" cy="780" r="14" fill="#c8bda6"/><circle cx="330" cy="260" r="14" fill="#c8bda6"/><circle cx="90" cy="300" r="14" fill="#c8bda6"/>
<text x="210" y="480" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#857b6a">Other days</text></svg>'''
P["p257_piano_s3"] = pt(3, "STEP 2 · ONE AREA PER DAY", "Due pianos grouped<br><span>by part of town.</span>",
f'''<div class=w3><div class="cd mc"><small class=cap>TUESDAY · SAMPLE MAP</small>{mp}</div><div class="cd rl">{"".join(f'<div class=rs><em>{i}</em><div><b>{t}</b><span>{a}</span><small>{b}</small></div></div>' for i,(t,a,b) in enumerate(route,1))}</div></div>''',
css=""".w3{flex:1;display:flex;gap:14px;min-height:0}.mc{width:440px;flex:none;padding:16px;display:flex;flex-direction:column;gap:10px}.mp{flex:1;min-height:0;width:100%;display:block}
.rl{flex:1;min-width:0;padding:12px 22px;display:flex;flex-direction:column}.rs{flex:1;display:flex;align-items:center;gap:18px;border-bottom:1px solid #eee7d8}.rs:last-child{border:0}
.rs em{width:52px;height:52px;border-radius:50%;background:#141210;color:#e8c477;font:800 22px 'DM Sans';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.rs b{display:block;font:700 22px 'DM Sans';color:#a77b2c}.rs span{display:block;font:700 28px/1.35 Gelasio}.rs small{font:500 18px 'DM Sans';color:#5f574a}""")

book = f'''<div class=bp><div class=bh><b>Book a tuning</b><span>Sample Piano Care</span></div>
{"".join(f'<div class=bf><span>{a}</span><b>{b}</b></div>' for a,b in [("Piano type","Upright"),("ZIP code","Sample 00000"),("Last tuned","About 1 year ago"),("Floor","Ground floor"),("Notes","Park in the driveway")])}
<div class=bs><span>Open slots · North side</span><div>{"".join(f'<i class="{"on" if j==1 else ""}">{t}</i>' for j,t in enumerate(["Tue 9 AM","Tue 11 AM","Tue 3:30 PM"]))}</div></div>
<div class=bb>Book Tue 11 AM</div></div>'''
P["p257_piano_s4"] = pt(4, "STEP 3 · CLIENTS BOOK THE OPEN SLOTS", "They pick a time<br><span>on your route day.</span>",
f'''<div class=w4>{phone(book, w=380, h=760)}<div class=sd>{"".join(f'<div class="cd sx"><span class=ib>{ic(i,28)}</span><b>{a}</b><span>{b}</span></div>' for i,a,b in [("pin","By ZIP code","Shows only your day for that area"),("clock","Two-hour slots","Room for the drive"),("bell","Day-before text","With your arrival window")])}</div></div>''',
css=""".w4{flex:1;display:flex;gap:18px;min-height:0;align-items:center}
.bp{flex:1;padding:6px 18px 18px;display:flex;flex-direction:column;gap:10px;font-family:'DM Sans'}.bh b{display:block;font:700 26px Gelasio;color:#141210}.bh span{font:500 14px 'DM Sans';color:#857b6a}
.bf{display:flex;justify-content:space-between;align-items:center;padding:13px 14px;border-radius:12px;background:#f7f1e3;font:500 15px 'DM Sans';color:#5f574a}.bf b{font:700 16px 'DM Sans';color:#141210}
.bs span{display:block;font:700 13px 'DM Sans';letter-spacing:1px;color:#857b6a;margin:4px 0 8px}.bs div{display:flex;flex-direction:column;gap:8px}.bs i{font:700 16px 'DM Sans';font-style:normal;padding:12px;border-radius:12px;border:2px solid #e3d8c0;text-align:center;color:#141210}.bs i.on{background:#141210;color:#e8c477;border-color:#141210}
.bb{margin-top:auto;background:#a77b2c;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 16px 'DM Sans'}
.sd{flex:1;min-width:0;align-self:stretch;display:flex;flex-direction:column;gap:12px}.sx{flex:1;padding:18px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px}
.sx .ib{width:60px;height:60px;border-radius:18px;background:#f6e6c4;color:#a77b2c}.sx b{font:700 32px/1.35 Gelasio}.sx>span:last-child{font:500 20px/1.4 'DM Sans';color:#5f574a}""")

P["p257_piano_s5"] = pt(5, "YOUR TURN", "Tune pianos for a living?<br><span>Let's build your app.</span>",
f'''<div class=w5><div class="cd hk">{keys(28, (4, 11, 18))}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Piano history","Every visit saved"),("bell","Reminders","On your own rule"),("map","Route days","One area a day"),("cal","Online booking","Open slots only")])}</div>
<div class=q>How do your clients remember their next tuning today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#a77b2c;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hk{flex:1;padding:22px;display:flex;align-items:center}.hk .kbd{width:100%;height:360px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(20,18,16,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#f6e6c4;color:#a77b2c}.ti b{display:block;font:700 30px/1.4 Gelasio;margin-bottom:2px}.ti div span{font:500 19px/1.35 'DM Sans';color:#5f574a}
.q{background:#141210;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'DM Sans'}""")

# ───────── 258 INDIA · Granite and marble cutter · SINGLE · Bitter + Inter · marble white / granite black / copper
# New technique: top-down slab with a nested cut plan (pieces as rectangles to scale, offcut hatched) next to a slab stock rack.
SW, SH = 10, 6  # slab 10 x 6 ft
cuts = [("A", 0, 0, 7, 2, "Kitchen top 7 × 2"), ("B", 7, 0, 3, 2, "Side top 3 × 2"), ("C", 0, 2, 4, 2, "Sill 4 × 2 · 1 of 2"), ("D", 4, 2, 4, 2, "Sill 4 × 2 · 2 of 2"), ("E", 0, 4, 6, 1.5, "Step 6 × 1.5")]
sc = 70
slab = f'<svg viewBox="-20 -20 {SW*sc+40} {SH*sc+70}" class=sb><defs><pattern id="ht" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="14" height="14" fill="#f3efe9"/><rect width="5" height="14" fill="#d9cfc3"/></pattern>'
slab += '<linearGradient id="mb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fbfaf7"/><stop offset=".5" stop-color="#ece8e1"/><stop offset="1" stop-color="#f8f6f2"/></linearGradient></defs>'
slab += f'<rect width="{SW*sc}" height="{SH*sc}" fill="url(#ht)" stroke="#232323" stroke-width="4"/>'
slab += "".join(f'<rect x="{x*sc}" y="{y*sc}" width="{w*sc}" height="{h*sc}" fill="url(#mb)" stroke="#b5642c" stroke-width="4"/><path d="M{x*sc+20} {y*sc+h*sc-18} Q{x*sc+w*sc*0.5} {y*sc+10} {x*sc+w*sc-20} {y*sc+h*sc*0.6}" stroke="#c9c2b6" stroke-width="2" fill="none"/><circle cx="{x*sc+34}" cy="{y*sc+34}" r="22" fill="#b5642c"/><text x="{x*sc+34}" y="{y*sc+42}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="22" fill="#fff">{k}</text>' for k,x,y,w,h,_ in cuts)
slab += f'<rect x="{6*sc+40}" y="{4*sc+22}" width="250" height="42" rx="10" fill="#fff" stroke="#232323" stroke-width="2"/><text x="{6*sc+165}" y="{4*sc+50}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="20" fill="#232323">Offcut 4 × 2 + strip</text>'
slab += f'<text x="{SW*sc/2}" y="{SH*sc+42}" text-anchor="middle" font-family="Bitter" font-weight="700" font-size="22" fill="#232323">Slab S-14 · 10 × 6 ft · white marble · sample</text></svg>'
P["p258_stone"] = page("""
body{--f:'Inter';--h:'Bitter';background:#ecebe8;color:#232323}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#b5642c;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#b5642c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sc{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(35,35,35,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#7b776f}
.sb{width:100%;display:block}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.cl{flex:1;min-width:0;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(35,35,35,.08)}
.cr{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #eeece8;font:600 22px Inter}.cr i{width:34px;height:34px;border-radius:50%;background:#b5642c;color:#fff;font:800 16px Inter;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.cr span{flex:1}.cr em{font:600 16px Inter;font-style:normal;color:#7b776f}
.rk{width:330px;flex:none;background:#232323;color:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column}
.rk small{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#e7a978}
.rr{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #3a3a3a}.rr i{width:46px;height:30px;border-radius:4px;flex:none}
.rr div{flex:1;font:700 19px/1.25 Inter}.rr div span{display:block;font:500 15px Inter;color:#bdb8b0}.rr em{font:700 16px Inter;font-style:normal;color:#e7a978}
""", "<div class=kk>GRANITE AND MARBLE CUTTING</div><h1>Plan every cut<br><span>before the blade touches the slab.</span></h1>",
f'''<div class=vw><div class=sc><small class=cap>CUT PLAN · ORDER 258 · SAMPLE</small>{slab}</div>
<div class=bt><div class=cl><small class=cap>PIECES FROM THIS SLAB</small>{"".join(f'<div class=cr><i>{k}</i><span>{t} ft</span></div>' for k,x,y,w,h,t in cuts)}</div>
<div class=rk><small>SLAB RACK · SAMPLE</small>{"".join(f'<div class=rr><i style="background:{c}"></i><div>{a}<span>{b}</span></div><em>{e}</em></div>' for a,b,c,e in [("S-14 White marble","10 × 6 ft","linear-gradient(135deg,#fbfaf7,#dcd6cc)","In use"),("S-15 Black granite","9 × 5.5 ft","linear-gradient(135deg,#2e2e2e,#555)","Free"),("S-16 Beige granite","10 × 5 ft","linear-gradient(135deg,#e6d3b3,#c9ad80)","Free"),("Offcuts","3 pieces","repeating-linear-gradient(45deg,#d9cfc3 0 5px,#f3efe9 5px 12px)","Listed")])}</div></div></div>''',
"#232323", "Cut stone slabs? DM us", "background:#b5642c;color:#fff")

# ───────── 259 INDIA · Electric motor rewinding shop · SINGLE · Montserrat + Fira Sans · copper orange / workshop blue / steel grey
# New technique: paper job tags hanging on hooks (string hole + tied string) with motor details and a status punch.
tags = [("J-101", "Water pump motor", "1 HP · burnt winding", "Ready", "r"), ("J-102", "Flour mill motor", "3 HP · bearing noise", "Winding", "w"), ("J-103", "Ceiling fan", "Not running", "Waiting for part", "p"), ("J-104", "Borewell motor", "1.5 HP · trips switch", "Testing", "t"), ("J-105", "Cooler motor", "Slow speed", "Received", "n"), ("J-106", "Lathe motor", "2 HP · burnt smell", "Winding", "w")]
P["p259_rewind"] = page("""
body{--f:'Fira Sans';--h:'Montserrat';background:#e9eef4;color:#1d2f4a}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#c4621d;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#c4621d}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bd{flex:1;min-height:0;background:#1d2f4a;border-radius:26px;padding:16px 22px 22px;display:flex;flex-direction:column;gap:6px}
.bd>small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#9fb6d6}
.rail{height:12px;border-radius:6px;background:linear-gradient(#c7d0db,#8c98a8);margin-top:8px}
.tg3{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:18px 18px;min-height:0}
.tc{display:flex;flex-direction:column;align-items:center;min-height:0}
.tc s{width:3px;height:26px;background:#e8d9b8;text-decoration:none;display:block}
.tt{flex:1;width:100%;background:#f6ecd6;clip-path:polygon(18% 0,82% 0,100% 12%,100% 100%,0 100%,0 12%);padding:34px 18px 14px;display:flex;flex-direction:column;gap:6px;position:relative}
.tt:before{content:"";position:absolute;top:12px;left:50%;width:16px;height:16px;margin-left:-8px;border-radius:50%;background:#1d2f4a;box-shadow:0 0 0 4px #c4621d}
.tt em{font:700 16px 'Fira Sans';font-style:normal;color:#8a7a5a;letter-spacing:1px}
.tt b{font:800 25px/1.3 Montserrat}.tt>span{font:500 19px/1.35 'Fira Sans';color:#5a5040}.tp{margin-top:10px;border-top:2px dashed #d8c9a6;padding-top:8px}.tp span{display:block;font:700 13px 'Fira Sans';letter-spacing:2px;color:#8a7a5a;text-transform:uppercase}.tp strong{font:800 22px Montserrat}
.tt i{margin-top:auto;font:700 16px 'Fira Sans';font-style:normal;text-align:center;padding:8px 0;border-radius:10px}
.tt i.r{background:#2f8f5b;color:#fff}.tt i.w{background:#c4621d;color:#fff}.tt i.p{background:#e2b23a;color:#1d2f4a}.tt i.t{background:#3f6fb0;color:#fff}.tt i.n{background:#d5dde7;color:#1d2f4a}
.ms{display:flex;gap:14px;align-items:center;background:#fff;border-radius:22px;padding:16px 20px;box-shadow:0 14px 30px rgba(29,47,74,.08)}.ms .ib{width:54px;height:54px;border-radius:16px;background:#fbe6d6;color:#c4621d}
.ms p{flex:1;font:500 21px/1.45 'Fira Sans'}.ms p b{color:#c4621d}
""", "<div class=kk>ELECTRIC MOTOR REWINDING SHOP</div><h1>“Is my motor ready?”<br><span>Every tag answers it.</span></h1>",
f'''<div class=vw><div class=bd><small>JOB TAGS · TODAY · SAMPLE</small><div class=rail></div><div class=tg3>{"".join(f'<div class=tc><s></s><div class=tt><em>{j}</em><b>{a}</b><span>{d}</span><p class=tp><span>Promised</span><strong>{pr}</strong></p><i class={c}>{st}</i></div></div>' for (j,a,d,st,c),pr in zip(tags,["Today","Wed 25 Nov","Thu 26 Nov","Today","Fri 27 Nov","Thu 26 Nov"]))}</div></div>
<div class=ms><span class=ib>{ic("bell",26)}</span><p>Change a tag to <b>Ready</b> and the customer gets a message with the job number, sample.</p></div></div>''',
"#1d2f4a", "Run a rewinding shop? DM us", "background:#c4621d;color:#fff")

# ───────── 260 CANADA · Deck builder · SINGLE · Archivo Black + Open Sans · lake blue / cedar / pine green
# New technique: top-down deck plan with board grain (repeating gradient), measured sides, and the customer's picks as swatch chips.
deck = '''<svg viewBox="0 0 640 820" class=dk><defs><pattern id="bd" width="640" height="22" patternUnits="userSpaceOnUse"><rect width="640" height="22" fill="#b9784a"/><rect y="19" width="640" height="3" fill="#8a5330"/><path d="M0 9 Q160 5 320 10 T640 8" stroke="#a8693d" stroke-width="2" fill="none"/></pattern></defs>
<rect width="640" height="820" rx="14" fill="#cfe6d6"/><path d="M0 600 Q160 570 320 595 T640 585 V806 Q640 820 626 820 H14 Q0 820 0 806 Z" fill="#7fb6d9"/><path d="M60 680 q30 -10 60 0 M400 720 q30 -10 60 0 M200 760 q30 -10 60 0" stroke="#d6ecf7" stroke-width="4" fill="none"/><rect x="430" y="560" width="70" height="200" fill="url(#bd)" stroke="#5a3218" stroke-width="4"/><rect x="250" y="642" width="168" height="40" rx="10" fill="#fff"/><text x="334" y="669" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="18" fill="#163a4f">Dock 4 × 12 ft</text><text x="80" y="790" font-family="Archivo Black" font-size="22" fill="#fff">LAKE</text><circle cx="580" cy="470" r="34" fill="#4f9a6f"/><circle cx="600" cy="520" r="26" fill="#3f8a60"/><rect x="0" y="0" width="640" height="80" fill="#e3e6ea"/><text x="320" y="50" text-anchor="middle" font-family="Archivo Black" font-size="24" fill="#5b6470">HOUSE WALL</text>
<rect x="80" y="80" width="400" height="300" fill="url(#bd)" stroke="#5a3218" stroke-width="5"/><rect x="110" y="380" width="100" height="66" fill="url(#bd)" stroke="#5a3218" stroke-width="4"/>
<path d="M110 402 H210 M110 424 H210" stroke="#5a3218" stroke-width="3"/>
<path d="M110 380 H80 V80 M480 80 V380 H210" stroke="#1f5f4a" stroke-width="9" fill="none"/>
<g stroke="#1f6fa8" stroke-width="3" fill="#1f6fa8"><line x1="515" y1="80" x2="515" y2="380"/><path d="M515 80 l-8 14 h16z"/><path d="M515 380 l-8 -14 h16z"/><line x1="80" y1="478" x2="480" y2="478"/><path d="M80 478 l14 -8 v16z"/><path d="M480 478 l-14 -8 v16z"/></g>
<rect x="320" y="460" width="100" height="36" rx="8" fill="#fff" stroke="#1f6fa8" stroke-width="3"/><text x="370" y="485" text-anchor="middle" font-family="Archivo Black" font-size="19" fill="#1f6fa8">16 FT</text>
<rect x="528" y="212" width="84" height="36" rx="8" fill="#fff" stroke="#1f6fa8" stroke-width="3"/><text x="570" y="237" text-anchor="middle" font-family="Archivo Black" font-size="19" fill="#1f6fa8">12 FT</text>
<rect x="178" y="200" width="204" height="60" rx="12" fill="#fff" fill-opacity=".92"/><text x="280" y="238" text-anchor="middle" font-family="Archivo Black" font-size="22" fill="#5a3218">192 SQ FT</text>
<text x="260" y="420" font-family="Open Sans" font-weight="700" font-size="18" fill="#1f5f4a">3 steps to the lawn</text></svg>'''
picks = [("Boards", "Cedar brown", "linear-gradient(#b9784a,#9a5f37)"), ("Railing", "Black metal", "repeating-linear-gradient(90deg,#222 0 5px,#e9eef2 5px 18px)"), ("Steps", "3, to the lawn", "linear-gradient(#a8693d,#8a5330)")]
P["p260_deck"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#e6f0f5;color:#163a4f}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#1f6fa8;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.22;margin-top:16px} h1 span{color:#1f5f4a}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.pc{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(22,58,79,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#6a7f8c}
.dk{width:100%;flex:1;min-height:0;display:block}
.lg2{display:flex;gap:16px;font:600 17px 'Open Sans';color:#4d6170}.lg2 span{display:flex;align-items:center;gap:8px}.lg2 i{width:28px;height:8px;border-radius:4px;background:#1f5f4a}.lg2 i.b{background:#1f6fa8;height:4px}
.rc{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.pk2{flex:1;background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(22,58,79,.08)}
.pr2{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #e8eef2}.pr2 i{width:58px;height:58px;border-radius:14px;flex:none;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}
.pr2 i{width:72px!important;height:72px!important}.pr2 small{display:block;font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#6a7f8c}.pr2 b{font:700 25px/1.35 'Open Sans'}
.bk2{background:#163a4f;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.bk2 small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#9fd0ef}
.bk2 .r{display:flex;justify-content:space-between;font:500 20px 'Open Sans'}.bk2 .r b{font-weight:700}
.bk2 .bb{background:#7bc4a4;color:#163a4f;border-radius:12px;padding:12px;text-align:center;font:700 18px 'Open Sans'}
""", "<div class=kk>DECK AND DOCK BUILDERS · DESIGN REQUESTS</div><h1>Size, boards and railing,<br><span>picked before your site visit.</span></h1>",
f'''<div class=vw><div class=pc><small class=cap>CUSTOMER'S DECK REQUEST · SAMPLE BACKYARD</small>{deck}<div class=lg2><span><i></i>Railing</span><span><i class=b></i>Measured by customer</span></div></div>
<div class=rc><div class=pk2><small class=cap>PICKED ON YOUR WEBSITE</small>{"".join(f'<div class=pr2><i style="background:{bg}"></i><div><small>{a.upper()}</small><b>{b}</b></div></div>' for a,b,bg in picks)}</div>
<div class=bk2><small>SITE VISIT · SAMPLE</small><div class=r><span>Date</span><b>Thu 3 Dec</b></div><div class=r><span>Time</span><b>10 AM</b></div><div class=r><span>Photos</span><b>4 attached</b></div><div class=bb>Confirm visit</div></div></div></div>''',
"#163a4f", "Build decks or docks? DM us", "background:#1f5f4a;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
