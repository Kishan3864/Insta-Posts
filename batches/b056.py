import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 296 INDIA · Watch repair shop · SINGLE · Cardo + DM Sans · racing green / champagne / ivory
# New technique: CSS analog watch faces whose hands point to the promised ready time; status ring around each face.
def watch(h, m, ring, strap="#3a2a1f", size=150):
    ha = (h % 12) * 30 + m * 0.5; ma = m * 6
    ticks = "".join(f'<i class=tk2 style="transform:rotate({a}deg)"></i>' for a in range(0, 360, 30))
    return f'''<div class=wt style="width:{size}px"><div class=sp style="background:{strap}"></div><div class=fc2 style="width:{size}px;height:{size}px;box-shadow:0 0 0 8px {ring},0 10px 18px rgba(0,0,0,.18)">{ticks}
<i class=hh style="transform:rotate({ha}deg)"></i><i class=mh style="transform:rotate({ma}deg)"></i><i class=pn></i></div><div class=sp style="background:{strap}"></div></div>'''
jobs = [("W-31", "Battery change", "Ready 12:30 PM", 12, 30, "#3f8f5a", "Ready"), ("W-32", "Strap change", "Ready 4 PM", 4, 0, "#d9a441", "Today"), ("W-33", "Glass change", "Ready Tue 5 PM", 5, 0, "#d9a441", "Tue"),
        ("W-34", "Full service", "Ready Sat 11 AM", 11, 0, "#8b8f99", "Sat"), ("W-35", "Crown repair", "Part ordered", 9, 0, "#c2573b", "Waiting"), ("W-36", "Battery change", "Ready 1 PM", 1, 0, "#3f8f5a", "Ready")]
P["p296_watch"] = page("""
body{--f:'DM Sans';--h:'Cardo';background:#f5f1e6;color:#173528}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#a88838;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:68px;line-height:1.25} h1 span{color:#2a6a4a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ty{flex:1;min-height:0;background:#173528;border-radius:26px;padding:20px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px;box-shadow:inset 0 0 0 6px #22473a}
.jb{background:#204638;border-radius:18px;padding:12px;display:flex;flex-direction:column;align-items:center;gap:8px}
.wt{display:flex;flex-direction:column;align-items:center}.sp{width:56px;height:22px;border-radius:6px}
.fc2{border-radius:50%;background:radial-gradient(circle,#fffdf6,#efe8d6);position:relative;flex:none}
.tk2{position:absolute;left:50%;top:6px;width:3px;height:12px;margin-left:-1.5px;background:#173528;transform-origin:50% 69px}
.hh,.mh{position:absolute;left:50%;bottom:50%;border-radius:4px;background:#173528;transform-origin:50% 100%}
.hh{width:7px;height:38px;margin-left:-3.5px}.mh{width:4px;height:56px;margin-left:-2px;background:#a88838}
.pn{position:absolute;left:50%;top:50%;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;background:#173528}
.jt{text-align:center}.jt b{display:block;font:700 24px/1.3 Cardo;color:#fff}.jt span{font:600 16px/1.4 'DM Sans';color:#cfe0d6}
.jb em{font:700 15px 'DM Sans';font-style:normal;padding:4px 12px;border-radius:8px;color:#173528}
.bt{display:grid;grid-template-columns:1.4fr 1fr;gap:12px}
.ms{background:#fff;border-radius:22px;padding:16px 20px;box-shadow:0 14px 30px rgba(23,53,40,.08)}.ms small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7a7562;margin-bottom:6px}.ms p{font:500 20px/1.45 'DM Sans';background:#eef4ef;border-radius:14px 14px 14px 4px;padding:12px 14px}.ms b{color:#2a6a4a}
.lg8{background:#fff;border-radius:22px;padding:14px 18px;display:grid;grid-template-columns:1fr 1fr;gap:8px;align-content:center;box-shadow:0 14px 30px rgba(23,53,40,.08)}.lg8 span{display:flex;align-items:center;gap:8px;font:600 16px 'DM Sans'}.lg8 i{width:16px;height:16px;border-radius:50%}
""", "<div class=kk>WATCH REPAIR SHOP · JOB TRAY</div><h1>“Is my watch done?”<br><span>The hands show when.</span></h1>",
f'''<div class=vw><div class=ty>{"".join(f'<div class=jb>{watch(h,m,c)}<div class=jt><b>{j} · {t}</b><span>{r}</span></div><em style="background:{c}">{st}</em></div>' for j,t,r,h,m,c,st in jobs)}</div>
<div class=bt><div class=ms><small>MESSAGE SENT · SAMPLE</small><p>Your watch <b>W-31</b> (battery change) is ready. Please collect it before 8 PM.</p></div>
<div class=lg8>{"".join(f'<span><i style="background:{c}"></i>{a}</span>' for a,c in [("Ready","#3f8f5a"),("In work","#d9a441"),("Booked","#8b8f99"),("Waiting for part","#c2573b")])}</div></div></div>''',
"#173528", "Repair watches? DM us", "background:#2a6a4a;color:#fff")

# ───────── 297 INDIA · Papad and snacks home unit · CAROUSEL 5 · Anton + Inter · papad beige / chilli red / mustard
# New technique: sun-drying mats drawn as rows of papad discs (radial gradient with pepper specks), used as the counting unit.
PD = """
body{--f:'Inter';--h:'Anton';background:#f7efdc;color:#3a2016}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#c23b22;margin-top:22px;align-self:flex-start}
h1{font-family:'Anton';font-weight:400;font-size:68px;letter-spacing:.5px;line-height:1.3;margin-top:32px} h1 span{color:#c23b22}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(58,32,22,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#85735e}
.nb{display:flex;align-items:center;gap:14px;background:#3a2016;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Inter'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#c23b22}.nb b{color:#f6c94e}
.pp{border-radius:50%;flex:none;background:radial-gradient(circle at 30% 30%,#7a4a2a 0 1.5px,transparent 2px) 0 0/11px 11px,radial-gradient(circle,#f4d79a,#e7bd6a);box-shadow:0 0 0 2px #d9a74f}
.pp.m{background:radial-gradient(circle at 30% 30%,#b8321c 0 2px,transparent 2.5px) 0 0/10px 10px,radial-gradient(circle,#f2c27a,#e0a14f)}
.pp.g{background:radial-gradient(circle at 30% 30%,#5b7a2a 0 1.5px,transparent 2px) 0 0/9px 9px,radial-gradient(circle,#f1e2a4,#e2cc78)}
"""
def pd(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3a2016;color:#fff"):
    return page(PD + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3a2016", cta, ctacss, tagline=f"{n} / 5")
def mat(k, n, s=60):
    return "".join(f'<i class="pp {k}" style="width:{s}px;height:{s}px"></i>' for _ in range(n))
P["p297_papad_s1"] = pd(1, "PAPAD AND SNACKS · HOME UNIT", "Orders on voice notes?<br><span>Put them in one sheet.</span>",
f'''<div class=w1><div class="cd mt1"><small class=cap>TODAY'S DRYING MATS · SAMPLE</small>{"".join(f'<div class=mr><b>{a}</b><div class=ds>{mat(k,9,62)}</div></div>' for a,k in [("Plain","p"),("Masala","m"),("Moong","g")])}</div>
<div class=bb1><span class=vn>{ic("chat",24)} Voice note · 0:48</span><p>“Send 10 masala, 6 plain… no wait, 8 plain, and the moong one also…”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.mt1{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:10px;background:repeating-linear-gradient(90deg,#fff 0 40px,#fbf5e8 40px 80px)}
.mr{flex:1;display:flex;align-items:center;gap:16px;border-top:2px dashed #e6d6b6}.mr b{width:120px;font:400 30px/1.4 Anton;letter-spacing:.5px}.ds{flex:1;display:flex;justify-content:space-between}
.bb1{background:#3a2016;color:#fff;border-radius:22px 22px 22px 6px;padding:18px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px Inter;color:#f6c94e;margin-bottom:6px}.bb1 p{font:500 22px/1.45 Inter}""")

shops = [("Shop S-01", 8, 10, 4), ("Shop S-02", 12, 6, 0), ("Shop S-03", 6, 6, 6), ("Shop S-04", 10, 0, 8), ("Shop S-05", 4, 8, 2)]
tot = [sum(s[i] for s in shops) for i in (1, 2, 3)]
P["p297_papad_s2"] = pd(2, "STEP 1 · ONE ORDER SHEET FOR ALL SHOPS", "Shops fill a link.<br><span>You see the totals.</span>",
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>SHOP · SAMPLE</span><span><i class="pp p"></i>PLAIN</span><span><i class="pp m"></i>MASALA</span><span><i class="pp g"></i>MOONG</span></div>
{"".join(f'<div class=rw2><b>{a}</b>{"".join(f"<em>{v or chr(8212)}</em>" for v in (p,m,g))}</div>' for a,p,m,g in shops)}
<div class="rw2 tt2"><b>Packets</b>{"".join(f"<em>{v}</em>" for v in tot)}</div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>Orders close every Wednesday at 6 PM, <b>so Thursday's batch is planned.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:1.3fr 1fr 1fr 1fr;gap:12px;align-items:center;border-bottom:1px solid #f0e6d2}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #3a2016;font:700 14px/1.4 Inter;letter-spacing:1.5px;color:#85735e}.hd2 span{display:flex;align-items:center;gap:8px}.hd2 .pp{width:26px;height:26px}
.rw2 b{font:700 24px Inter}.rw2 em{font:400 34px/1.4 Anton;font-style:normal;letter-spacing:.5px}
.tt2{border:0;background:#fbeed0;border-radius:14px;padding:0 12px}.tt2 em{color:#c23b22}""")

# 1 kg dough = 40 papads (sample rule); 1 packet = 20 papads
plan = [("Plain", tot[0], "p"), ("Masala", tot[1], "m"), ("Moong", tot[2], "g")]
P["p297_papad_s3"] = pd(3, "STEP 2 · PACKETS TO DOUGH, BY A RULE", "40 packets of plain?<br><span>Know the dough first.</span>",
f'''<div class=w3>{"".join(f'<div class="cd pl3"><div class=ph3><i class="pp {k}" style="width:92px;height:92px"></i><b>{a}</b></div>{"".join(f"<div class=ln3><span>{x}</span><b>{y}</b></div>" for x,y in [("Packets",n),("Papads",f"{n*20:,}"),("Dough",f"{n*20//40} kg")])}</div>' for a,n,k in plan)}
<div class=nb><span class=ib>{ic("chart",26)}</span><span>Sample rule: 1 packet = 20 papads, 1 kg dough = 40 papads. <b>Change it to your own.</b></span></div></div>''',
css=""".w3{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr auto;gap:12px;min-height:0}.w3 .nb{grid-column:1 / 4}
.pl3{padding:18px;display:flex;flex-direction:column;gap:6px}.ph3{display:flex;flex-direction:column;align-items:center;gap:10px;padding-bottom:12px;border-bottom:2px dashed #e6d6b6}.ph3 b{font:400 34px/1.4 Anton;letter-spacing:.5px}
.ln3{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center}.ln3 span{font:600 17px/1.5 Inter;color:#85735e;margin-bottom:6px}.ln3 b{font:400 56px/1.5 Anton;letter-spacing:.5px;color:#c23b22}""")

route = [("Fri 27 Nov", "S-01, S-02", tot and 8+10+4+12+6), ("Sat 28 Nov", "S-03, S-04", 6+6+6+10+8), ("Sat 28 Nov", "S-05", 4+8+2)]
P["p297_papad_s4"] = pd(4, "STEP 3 · PACKED AND DISPATCHED BY SHOP", "Every packet<br><span>reaches the right shop.</span>",
f'''<div class=w4>{"".join(f'<div class="cd dp"><div class=dd4><small>{d}</small><b>{s}</b></div><div class=bx4>{"".join("<i class=pk></i>" for _ in range(n))}</div><em>{n} packets</em></div>' for d,s,n in route)}
<div class=nb><span class=ib>{ic("truck",26)}</span><span>The shop gets a message when its packets leave. <b>{sum(r[2] for r in route)} packets this week, sample.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.dp{flex:1;display:flex;align-items:center;gap:20px;padding:14px 22px}
.dd4{width:200px;flex:none}.dd4 small{display:block;margin-bottom:6px;font:700 15px/1.5 Inter;letter-spacing:1px;color:#85735e}.dd4 b{display:block;font:400 32px/1.5 Anton;letter-spacing:.5px}
.bx4{flex:1;display:flex;flex-wrap:wrap;gap:6px}.pk{width:26px;height:34px;border-radius:4px;background:linear-gradient(#c23b22 0 30%,#f6c94e 30% 100%);border:2px solid #7a2414}
.dp em{font:400 30px/1.4 Anton;font-style:normal;color:#c23b22;width:150px;text-align:right}""")

P["p297_papad_s5"] = pd(5, "YOUR TURN", "Make papad or snacks at home?<br><span>Let's build your order sheet.</span>",
f'''<div class=w5><div class="cd hp">{mat("p",6,110)}{mat("m",6,110)}{mat("g",6,110)}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Order link","Shops order by packet"),("chart","Batch plan","Packets to dough"),("box","Packing list","By shop"),("truck","Dispatch","Message when it leaves")])}</div>
<div class=q>How do shops send you orders today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#c23b22;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;flex-wrap:wrap;justify-content:center;align-content:center;gap:18px;padding:24px 50px}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(58,32,22,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#fbeed0;color:#c23b22}.ti b{display:block;font:400 28px/1.45 Anton;letter-spacing:.5px}.ti div span{font:500 19px/1.35 Inter;color:#6b5a48}
.q{background:#3a2016;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Inter}""")

# ───────── 298 USA · Hot tub service · SINGLE · Lora + DM Sans · lagoon aqua / cedar / navy · PHONE
# New technique: top-down hot tub (cedar frame, seats, jets) with each visit logged as a stamp-style row; phone shows the visit report.
tub = '''<svg viewBox="0 0 420 420" class=tb><rect x="10" y="10" width="400" height="400" rx="40" fill="#b07a4a"/>
''' + "".join(f'<rect x="{10+i*25}" y="10" width="3" height="400" fill="#8e5e34"/>' for i in range(1, 16)) + '''
<rect x="50" y="50" width="320" height="320" rx="60" fill="#e9f3f5" stroke="#1d3557" stroke-width="5"/>
<rect x="66" y="66" width="288" height="288" rx="50" fill="#5ec4cf"/>
<rect x="80" y="80" width="110" height="80" rx="20" fill="#7fd3dc"/><rect x="230" y="80" width="110" height="80" rx="20" fill="#7fd3dc"/>
<rect x="80" y="260" width="110" height="80" rx="20" fill="#7fd3dc"/><rect x="230" y="260" width="110" height="80" rx="20" fill="#7fd3dc"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="8" fill="#1d3557"/>' for x, y in [(100, 120), (170, 120), (250, 120), (320, 120), (100, 300), (170, 300), (250, 300), (320, 300)]) + '''
<circle cx="210" cy="210" r="34" fill="#ffffff" stroke="#1d3557" stroke-width="5"/><text x="210" y="218" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="20" fill="#1d3557">Filter</text></svg>'''
visits = [("Tue 3 Nov", "7.4", "3 ppm", "Rinsed"), ("Tue 10 Nov", "7.6", "2 ppm", "—"), ("Tue 17 Nov", "7.5", "3 ppm", "Rinsed")]
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE HOT TUB CARE</small><b>Visit report</b><span>Tue 17 Nov · your backyard</span></div>
<div class=pho><span>Photo · clear water</span></div>
{"".join(f'<div class=rr2><span>{a}</span><b>{b}</b></div>' for a,b in [("pH","7.5"),("Sanitizer","3 ppm"),("Filter","Rinsed"),("Cover","Clips OK")])}
<div class=nx><small>NEXT VISIT</small><b>Tue 24 Nov · AM</b></div><div class=nx><small>TECH NOTE</small><b style="font-size:15px;font-weight:600">One cover strap is loose. New strap next visit.</b></div>
<div class=bk2>Change my visit</div></div>''', 370, 820)
P["p298_hottub"] = page("""
body{--f:'DM Sans';--h:'Lora';background:#e8f4f5;color:#1d3557}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#a0663a;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#1f8f9c}
.vw{flex:1;display:flex;gap:20px;min-height:0;align-items:center}
.lc{flex:1;min-width:0;align-self:stretch;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(29,53,87,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#6b7a8a}
.tb{width:350px;height:350px;display:block;align-self:center;flex:none}
.lgh,.lgr{display:grid;grid-template-columns:1.4fr .7fr 1fr 1fr;gap:8px;align-items:center}
.lgh{font:700 13px/1.4 'DM Sans';letter-spacing:1.5px;color:#6b7a8a;border-bottom:2px solid #1d3557;padding-bottom:6px}
.lgr{flex:1;border-bottom:1px solid #e6eef2;font:700 22px 'DM Sans'}.lgr:last-child{border:0}.lgr b{font:700 21px Lora}
.ap{flex:1;display:flex;flex-direction:column;gap:10px;padding:8px 18px 20px}
.ah small{display:block;font:700 12px/1.4 'DM Sans';letter-spacing:2px;color:#1f8f9c}.ah b{display:block;font:700 26px/1.3 Lora}.ah span{font:500 14px 'DM Sans';color:#6b7a8a}
.pho{height:150px;border-radius:14px;background:linear-gradient(135deg,#7fd3dc,#3aa8b5);display:flex;align-items:flex-end;padding:10px}.pho span{font:700 13px 'DM Sans';color:#fff;background:rgba(29,53,87,.55);padding:4px 8px;border-radius:6px}
.rr2{display:flex;justify-content:space-between;border-bottom:1px solid #e6eef2;padding:7px 2px;font:500 16px 'DM Sans'}.rr2 b{font:700 16px 'DM Sans'}
.nx{background:#e8f4f5;border-radius:12px;padding:10px 12px}.nx small{display:block;font:700 11px/1.4 'DM Sans';letter-spacing:2px;color:#6b7a8a}.nx b{font:700 18px 'DM Sans'}
.bk2{margin-top:auto;background:#1d3557;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 18px 'DM Sans'}
""", "<div class=kk>HOT TUB SERVICE · WEEKLY VISITS</div><h1>Every visit logged,<br><span>every reading shared.</span></h1>",
f'''<div class=vw><div class=lc><small class=cap>SAMPLE CLIENT TUB · TOP VIEW</small>{tub}<div class=lgh><span>VISIT</span><span>PH</span><span>SANITIZER</span><span>FILTER</span></div>
{"".join(f'<div class=lgr><b>{a}</b><span>{b}</span><span>{c}</span><span>{d}</span></div>' for a,b,c,d in visits)}</div>{ph}</div>''',
"#1d3557", "Service hot tubs? DM us", "background:#1f8f9c;color:#fff")

# ───────── 299 INDIA · Typing and DTP centre · SINGLE · Gelasio + Fira Sans · print cyan / charcoal / lemon
# New technique: LED dot-matrix token board (CSS radial dots behind amber text) showing now-serving and ready times.
P["p299_dtp"] = page("""
body{--f:'Fira Sans';--h:'Gelasio';background:#eef6f8;color:#20262b}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#0f8fb3;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#0f8fb3}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.led{background:#121619;border-radius:24px;padding:20px 24px;border:8px solid #2a3036;display:flex;flex-direction:column;gap:12px;background-image:radial-gradient(circle,#1d2328 1.4px,transparent 1.8px);background-size:8px 8px}
.lr3{display:grid;grid-template-columns:200px 1fr 220px;gap:16px;align-items:center;font:700 34px/1.3 'Fira Sans';color:#ffd54a;text-shadow:0 0 10px rgba(255,213,74,.6);letter-spacing:2px}
.lr3 span{font-size:26px;color:#ffe9a3}.lr3 em{font-style:normal;text-align:right;color:#7fe0ff;text-shadow:0 0 10px rgba(127,224,255,.6);font-size:28px}
.lr3.nw{font-size:44px}.lr3.hd3{font:700 15px/1.4 'Fira Sans';letter-spacing:3px;color:#8a949c;text-shadow:none}.lr3.hd3 em{color:#8a949c;text-shadow:none;font-size:15px}
.bt{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.cd{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(32,38,43,.08)}
.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#707a82}
.fr{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #e9eef1}.fr i{width:34px;height:42px;border-radius:4px 12px 4px 4px;background:#dff2f8;border:2px solid #0f8fb3;flex:none}
.fr b{display:block;font:700 21px/1.3 'Fira Sans'}.fr span{font:500 17px 'Fira Sans';color:#5a646c}
.fr em{margin-left:auto;font:700 14px 'Fira Sans';font-style:normal;background:#fff4b8;color:#6b5a00;padding:4px 8px;border-radius:6px;flex:none}
.ms{background:#20262b;color:#fff}.ms .cap{color:#ffe066}.ms p{font:500 21px/1.45 'Fira Sans';background:#2e363d;border-radius:16px 16px 16px 4px;padding:14px 16px}.ms b{color:#7fe0ff}
.ms .st{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;gap:8px}.ms .st div{background:#2e363d;border-radius:12px;padding:10px 12px}.ms .st small{display:block;font:700 12px/1.4 'Fira Sans';letter-spacing:2px;color:#9aa5ad}.ms .st b{font:700 30px/1.3 Gelasio;color:#ffe066}
""", "<div class=kk>TYPING AND DTP CENTRE · JOB QUEUE</div><h1>A crowd at the counter?<br><span>Give them a token.</span></h1>",
f'''<div class=vw><div class=led><div class="lr3 hd3"><span>TOKEN</span><span>JOB · SAMPLE</span><em>READY</em></div>
{"".join(f'<div class="lr3{" nw" if i==0 else ""}"><b>{t}</b><span>{j}</span><em>{r}</em></div>' for i,(t,j,r) in enumerate([("T-14","Resume typing","NOW"),("T-15","Shop bill book design","11:40 AM"),("T-16","Form filling, 3 pages","12:10 PM"),("T-17","Wedding card proof","12:45 PM")]))}</div>
<div class=bt><div class=cd><small class=cap>FILES RECEIVED ON THE LINK</small>{"".join(f'<div class=fr><i></i><div><b>{a}</b><span>{b}</span></div><em>{c}</em></div>' for a,b,c in [("T-15 · logo + rates","2 files","Got it"),("T-16 · ID page photo","1 file","Got it"),("T-17 · card text","1 file","Proof sent")])}</div>
<div class="cd ms"><small class=cap>MESSAGE TO T-15 · SAMPLE</small><p>Your bill book design is ready at <b>11:40 AM</b>. You are next.</p><p>T-16: your forms will be ready at <b>12:10 PM</b>. Please bring the original ID.</p><div class=st><div><small>IN QUEUE</small><b>4</b></div><div><small>DONE TODAY</small><b>13</b></div></div></div></div></div>''',
"#20262b", "Run a DTP centre? DM us", "background:#0f8fb3;color:#fff")

# ───────── 300 INDIA · Steel utensils shop (bulk for caterers) · SINGLE · TeX Gyre Adventor + Source Sans 3 · steel silver / copper / indigo
# New technique: SVG stacks of steel plates, bowls and glasses with metallic gradients; stack height carries the count (1 layer = 25).
def stk(kind, layers):
    g = '<defs><linearGradient id="st" x1="0" x2="1"><stop offset="0" stop-color="#9aa3ad"/><stop offset=".5" stop-color="#eef1f4"/><stop offset="1" stop-color="#8b949e"/></linearGradient></defs>'
    if kind == "plate":
        body = "".join(f'<ellipse cx="90" cy="{200-i*12}" rx="80" ry="14" fill="url(#st)" stroke="#5d6670" stroke-width="2"/>' for i in range(layers))
    elif kind == "bowl":
        body = "".join(f'<path d="M30 {190-i*14} Q90 {230-i*14} 150 {190-i*14} Z" fill="url(#st)" stroke="#5d6670" stroke-width="2"/><ellipse cx="90" cy="{190-i*14}" rx="60" ry="9" fill="#dfe4e9" stroke="#5d6670" stroke-width="2"/>' for i in range(layers))
    else:
        body = "".join(f'<path d="M62 {206-i*14} L118 {206-i*14} L112 {150-i*14} L68 {150-i*14} Z" fill="url(#st)" stroke="#5d6670" stroke-width="2"/>' for i in range(layers))
    return f'<svg viewBox="0 0 180 230" class=sk>{g}{body}</svg>'
items = [("plate", "Full plates", 300, "12 layers"), ("bowl", "Katori bowls", 600, "24 layers"), ("glass", "Glasses", 300, "12 layers")]
P["p300_utensils"] = page("""
body{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:#eceef2;color:#232a4d}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#b8642f;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#3b4a9e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sh{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.it{background:#fff;border-radius:24px;padding:16px;display:flex;flex-direction:column;align-items:center;gap:6px;box-shadow:0 14px 30px rgba(35,42,77,.08)}
.sk{flex:1;min-height:0;width:100%;display:block}
.it b{font:700 46px/1.3 'TeX Gyre Adventor';color:#b8642f}.it span{font:700 21px 'Source Sans 3'}.it em{font:600 15px 'Source Sans 3';font-style:normal;color:#6c7186}
.bt{display:grid;grid-template-columns:1.3fr 1fr;gap:12px}
.oc{background:#232a4d;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.oc small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#f2b98f}
.orr{display:flex;justify-content:space-between;font:500 18px/1.45 'Source Sans 3';color:#cfd3e6}.orr b{color:#fff}
.rl{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px;box-shadow:0 14px 30px rgba(35,42,77,.08)}
.rl small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#6c7186}.rl b{font:700 26px/1.3 'TeX Gyre Adventor'}.rl span{font:500 17px/1.4 'Source Sans 3';color:#4f5670}
""", "<div class=kk>STEEL UTENSILS · BULK ORDERS FOR CATERERS</div><h1>300 guests on Saturday?<br><span>Count it in stacks.</span></h1>",
f'''<div class=vw><div class=sh>{"".join(f'<div class=it>{stk(k,{"plate":12,"bowl":12,"glass":12}[k])}<b>{n}</b><span>{a}</span><em>Sample · 1 layer = {n//12}</em></div>' for k,a,n,l in items)}</div>
<div class=bt><div class=oc><small>CATERER ORDER C-300 · SAMPLE</small>{"".join(f'<div class=orr><span>{a}</span><b>{b}</b></div>' for a,b in [("Event","Sat 28 Nov · 300 guests"),("Rule","1 plate, 2 bowls, 1 glass a guest"),("Ready","Fri 27 Nov · 6 PM"),("Delivery","Tempo, Sat 7 AM")])}</div>
<div class=rl><small>REPEAT ORDER</small><b>One tap next time</b><span>The same list comes back for the next event. Change the guest count and it updates.</span></div></div></div>''',
"#232a4d", "Sell utensils in bulk? DM us", "background:#b8642f;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
