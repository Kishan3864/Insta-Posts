import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 92 INDIA · Diamond polishing unit · CAROUSEL 6 · TeX Gyre Adventor + Inter · midnight indigo / ice blue / silver
# New techniques: SVG folded parcel-paper packet + faceted gem, CSS QR lot card, stage pipeline with lot chips.
DM = """
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#141a3a;color:#eef2fb}
h1{font-family:'TeX Gyre Adventor';font-size:62px;font-weight:700;letter-spacing:-1px;line-height:1.22} h1 span{color:#8fd3f4}
.sub{color:#aab3d1}
.kb{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Inter;letter-spacing:3px;color:#8fd3f4}
.kb b{width:54px;height:54px;clip-path:polygon(50% 0,100% 50%,50% 100%,0 50%);background:#8fd3f4;color:#141a3a;font:700 22px/1 'TeX Gyre Adventor';display:flex;align-items:center;justify-content:center;letter-spacing:0}
.kb b i{font-style:normal}
.cd{background:#1e2650;border-radius:24px;border:1.5px solid #2c376b}
.lb{font:700 13px Inter;letter-spacing:3px;color:#8a94bd}
"""
def dm(n, head, vis, css="", cta="Swipe", ctacss="background:#8fd3f4;color:#141a3a"):
    return page(DM + css, head, vis, "#eef2fb", cta, ctacss, tagline=f"{n} / 6")
GEM = '''<svg viewBox="0 0 200 170" width="{w}" height="{h}"><g stroke="#141a3a" stroke-width="2.5" stroke-linejoin="round">
<polygon points="40,10 160,10 196,60 100,166 4,60" fill="#bfe3f5"/><polygon points="40,10 70,60 4,60" fill="#e6f5fc"/><polygon points="160,10 196,60 130,60" fill="#8fd3f4"/>
<polygon points="40,10 160,10 130,60 70,60" fill="#d6effa"/><polygon points="70,60 130,60 100,166" fill="#a8daf2"/><polygon points="4,60 70,60 100,166" fill="#d0ecf9"/><polygon points="130,60 196,60 100,166" fill="#79c3e8"/>
<polygon points="100,10 130,60 70,60" fill="#f2fafe"/></g></svg>'''
P["p92_diamond_s1"] = dm(1, """<h1 style="margin-top:34px">Which lot is at<br>which desk right now?<br><span>Track every lot, packet<br>to polish.</span></h1>""",
f'''<div class=st1><div class=pk1><svg viewBox="0 0 520 380" width="520" height="380">
<polygon points="20,60 500,60 500,340 20,340" fill="#f4f6fa"/><polygon points="20,60 260,200 500,60" fill="#e3e8f2" stroke="#c7cfe0" stroke-width="3"/>
<polygon points="20,340 200,190 20,60" fill="#ebeff6"/><polygon points="500,340 320,190 500,60" fill="#ebeff6"/>
<line x1="20" y1="340" x2="200" y2="190" stroke="#c7cfe0" stroke-width="3"/><line x1="500" y1="340" x2="320" y2="190" stroke="#c7cfe0" stroke-width="3"/>
<text x="260" y="290" text-anchor="middle" font-family="Inter" font-weight="700" font-size="34" fill="#141a3a">LOT L-2417</text>
<text x="260" y="326" text-anchor="middle" font-family="Inter" font-weight="600" font-size="22" fill="#6b7598">48 stones · sample</text></svg>
<div class=gm1>{GEM.format(w=200,h=170)}</div></div>
<div class="cd tg1"><span class=lb>WHERE IS IT NOW · SAMPLE</span><b>Polishing · Desk 6</b><em>Scanned 11:42 am · stage 4 of 6</em><i class=br1>{"".join(f'<u class="{"d" if k<3 else "n" if k==3 else ""}"></u>' for k in range(6))}</i></div></div>''',
""".st1{flex:1;display:flex;flex-direction:column;gap:18px;align-items:center;justify-content:center;background:#1a2147;border-radius:30px;padding:24px}
.pk1{position:relative;width:520px;height:380px}.pk1 svg{display:block}
.gm1{position:absolute;right:-40px;top:-30px;filter:drop-shadow(0 14px 20px rgba(0,0,0,.35))}
.tg1{width:620px;padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.tg1 b{font:700 38px/1.25 'TeX Gyre Adventor'}.tg1 em{font-style:normal;font:500 19px Inter;color:#aab3d1}
.br1{display:flex;gap:8px;margin-top:4px}.br1 u{flex:1;height:12px;border-radius:6px;background:#2c376b}.br1 u.d{background:#8fd3f4}.br1 u.n{background:#d7dbe3}
""")

qr = "".join(f'<i class="{"on" if (x*7+y*13+x*y)%3==0 or (x<3 and y<3) or (x>6 and y<3) or (x<3 and y>6) else ""}"></i>' for y in range(10) for x in range(10))
info = [("Lot no.","L-2417"),("Stones","48"),("Weight in","12.40 ct"),("Party","Sample party A"),("Received","18 Nov 2026"),("Due back","5 Dec 2026")]
P["p92_diamond_s2"] = dm(2, """<div class=kb><b><i>1</i></b>LOT CARD</div><h1 style="margin-top:14px">Every lot gets a card<br><span>and a QR code.</span></h1>""",
f'''<div class=w2><div class=lc2><div class=hd2><div><span class=lb>LOT CARD · SAMPLE</span><b>L-2417</b></div><div class=qr2>{qr}</div></div>
{"".join(f'<div class=r2><span>{a}</span><b>{b}</b></div>' for a,b in info)}</div>
<div class=sd2>{"".join(f'<div class="cd f2">{ic(i,34)}<b>{t}</b><span>{d}</span></div>' for i,t,d in [("qr","Print and stick","The card goes with the packet."),("search","Scan to see all","Stage, desk and weight, on any phone."),("clock","Due date alert","Lots running late show in red.")])}</div></div>''',
""".vis{flex-direction:column}
.w2{flex:1;display:flex;gap:18px}
.lc2{flex:1.25;background:#f4f6fa;color:#141a3a;border-radius:24px;padding:24px 26px;display:flex;flex-direction:column}
.hd2{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px}
.hd2 b{display:block;font:700 54px/1.3 'TeX Gyre Adventor';margin-top:4px}
.qr2{width:130px;height:130px;display:grid;grid-template-columns:repeat(10,1fr);gap:1px;padding:8px;background:#fff;border-radius:10px;border:2px solid #d7dbe3;flex:none}
.qr2 i{display:block;background:#fff}.qr2 i.on{background:#141a3a}
.r2{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1.5px dashed #c7cfe0}
.r2 span{font:500 22px Inter;color:#6b7598}.r2 b{font:700 25px Inter}
.sd2{flex:1;display:flex;flex-direction:column;gap:14px}
.f2{flex:1;padding:20px;display:flex;flex-direction:column;justify-content:center;gap:8px}
.f2 svg{color:#8fd3f4}.f2 b{font:700 26px 'TeX Gyre Adventor'}.f2 span{font:500 19px/1.4 Inter;color:#aab3d1}
""")

stages = [("Planning",["L-2421","L-2422"]),("Sawing",["L-2419"]),("Bruting",["L-2418","L-2420"]),("Polishing",["L-2417","L-2415","L-2416"]),("Assortment",["L-2414"]),("Ready",["L-2412","L-2413"])]
P["p92_diamond_s3"] = dm(3, """<div class=kb><b><i>2</i></b>STAGES</div><h1 style="margin-top:14px">Scan at every desk.<br><span>See where each lot is.</span></h1>""",
f'''<div class="cd pp3">{"".join(f'<div class=sg3><div class=nm3><i>{k+1}</i><b>{s}</b><em>{len(l)} lot{"s" if len(l)>1 else ""}</em></div><div class=ch3>' + "".join(f'<span class="{"hi" if x=="L-2417" else "lt" if x=="L-2415" else ""}">{x}</span>' for x in l) + '</div></div>' for k,(s,l) in enumerate(stages))}
<div class=nt3><i class=lt></i>Red = past its due date · sample board</div></div>''',
""".vis{flex-direction:column}
.pp3{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px}
.sg3{flex:1;display:flex;align-items:center;gap:18px;background:#252e5c;border-radius:16px;padding:0 18px}
.nm3{width:330px;display:flex;align-items:center;gap:14px;flex:none}
.nm3 i{width:40px;height:40px;border-radius:50%;background:#2f3b75;color:#8fd3f4;font:700 19px/40px Inter;font-style:normal;text-align:center;flex:none}
.nm3 b{font:700 27px 'TeX Gyre Adventor';flex:1}.nm3 em{font-style:normal;font:600 17px Inter;color:#8a94bd}
.ch3{flex:1;display:flex;gap:10px;flex-wrap:wrap}
.ch3 span{font:700 19px Inter;padding:9px 14px;border-radius:10px;background:#d7dbe3;color:#141a3a}
.ch3 span.hi{background:#8fd3f4}.ch3 span.lt{background:#ff8a7a}
.nt3{display:flex;align-items:center;gap:10px;font:500 18px Inter;color:#aab3d1;padding:4px 4px 0}
.nt3 i{width:18px;height:18px;border-radius:5px;display:block;background:#ff8a7a}
""")

wk = [("Worker 1","Polishing",14),("Worker 2","Polishing",11),("Worker 3","Bruting",17),("Worker 4","Sawing",9),("Worker 5","Assortment",22)]
P["p92_diamond_s4"] = dm(4, """<div class=kb><b><i>3</i></b>WORK DONE</div><h1 style="margin-top:14px">Each worker's pieces,<br><span>counted by the scan.</span></h1>""",
f'''<div class="cd ot4"><div class=hd4><b>Today · pieces done</b><span class=lb>SAMPLE · NO COUNTING BY HAND</span></div>
{"".join(f'<div class=r4><div class=n4><b>{n}</b><span>{s}</span></div><i class=b4><u style="width:{round(c*100/24)}%"></u></i><em>{c}</em></div>' for n,s,c in wk)}
<div class=ft4>{ic("cal",24)}Month total per worker, ready on the 1st, for piece-rate pay.</div></div>''',
""".vis{flex-direction:column}
.ot4{flex:1;padding:24px 26px;display:flex;flex-direction:column;gap:6px}
.hd4{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}.hd4 b{font:700 32px 'TeX Gyre Adventor'}
.r4{flex:1;display:flex;align-items:center;gap:20px;border-bottom:1.5px solid #2c376b}
.n4{width:230px;flex:none}.n4 b{display:block;font:700 26px Inter}.n4 span{font:500 18px Inter;color:#8a94bd}
.b4{flex:1;height:26px;border-radius:13px;background:#2c376b;position:relative;overflow:hidden;display:block}.b4 u{position:absolute;left:0;top:0;bottom:0;border-radius:13px;background:linear-gradient(90deg,#8fd3f4,#d7dbe3)}
.r4 em{font-style:normal;width:60px;text-align:right;font:700 34px 'TeX Gyre Adventor'}
.ft4{margin-top:12px;display:flex;align-items:center;gap:12px;background:#8fd3f4;color:#141a3a;border-radius:14px;padding:14px 18px;font:600 19px Inter}
""")

wt = [("L-2410","12.10","11.98","ok"),("L-2411","9.85","9.71","ok"),("L-2412","14.30","13.62","ck"),("L-2413","8.40","8.31","ok"),("L-2414","11.05","10.96","ok")]
P["p92_diamond_s5"] = dm(5, """<div class=kb><b><i>4</i></b>WEIGHT CHECK</div><h1 style="margin-top:14px">Weight in vs weight out,<br><span>for every lot.</span></h1>""",
f'''<div class=tb5><div class="th5"><span>Lot</span><span>In (ct)</span><span>Out (ct)</span><span>Status</span></div>
{"".join(f'<div class="tr5 {k}"><b>{l}</b><span>{a}</span><span>{b}</span><em>{"Within limit" if k=="ok" else "Check this lot"}</em></div>' for l,a,b,k in wt)}</div>
<div class=nt5><div><span class=lb>YOU SET THE LIMIT</span><b>Lots outside your limit are flagged the moment they are weighed.</b></div>{GEM.format(w=110,h=94)}</div>''',
""".vis{flex-direction:column;gap:16px}
.tb5{flex:1;background:#f4f6fa;color:#141a3a;border-radius:24px;padding:14px 22px;display:flex;flex-direction:column}
.th5,.tr5{display:grid;grid-template-columns:1.1fr 1fr 1fr 1.5fr;align-items:center;gap:10px}
.th5{padding:10px 0;font:700 15px Inter;letter-spacing:2px;color:#6b7598;text-transform:uppercase}
.tr5{flex:1;border-top:1.5px solid #dfe3ec}
.tr5 b{font:700 26px 'TeX Gyre Adventor'}.tr5 span{font:600 25px Inter}
.tr5 em{font-style:normal;font:700 18px Inter;padding:8px 12px;border-radius:10px;justify-self:start}
.tr5.ok em{background:#dff1fa;color:#1d6f96}.tr5.ck{background:#ffe9e5;margin:0 -22px;padding:0 22px}.tr5.ck em{background:#e0533f;color:#fff}
.nt5{flex:none;display:flex;align-items:center;gap:20px;padding:18px 24px;background:#1e2650;border:1.5px solid #2c376b;border-radius:20px}
.nt5 div{flex:1;display:flex;flex-direction:column;gap:6px}.nt5 b{font:600 23px/1.4 Inter}
""")

P["p92_diamond_s6"] = dm(6, """<h1 style="margin-top:34px">Want lot tracking<br><span>for your unit?</span></h1><div class=sub>We build lot, stage and worker apps for diamond units.</div>""",
f'''<div class=w6><div class=pk6><span class=lb>YOUR UNIT · ONE APP</span>{"".join(f'<div class=r6>{ic("check",30)}<b>{t}</b></div>' for t in ["Lot card with QR","Scan at every desk","Pieces per worker","Weight in vs out","Late lots in red"])}</div>
<div class=pp6>{peep("PointingUp","Smile","ShortCurly","None",w=330,h=600)}</div></div>''',
""".w6{flex:1;display:flex;align-items:stretch;gap:10px}
.pk6{flex:1;background:#f4f6fa;color:#141a3a;border-radius:28px;padding:26px 30px;display:flex;flex-direction:column;gap:10px;clip-path:polygon(0 0,calc(100% - 70px) 0,100% 70px,100% 100%,0 100%)}
.pk6 .lb{color:#6b7598;margin-bottom:6px}
.r6{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px dashed #c7cfe0}
.r6 svg{color:#1d6f96;flex:none}.r6 b{font:700 31px/1.25 'TeX Gyre Adventor'}
.pp6{display:flex;align-items:flex-end}
""", cta="Run a diamond unit? DM us")

# ───────── 95 INDIA · Canteen contractor · CAROUSEL 5 · Montserrat + Fira Sans · turmeric / charcoal brown / steel / rice white
# New techniques: top-down SVG steel thali, perforated tear-off coupon strip, tablet scan counter, bill doc with day sparkline.
CN = """
body{--f:'Fira Sans';--h:'Montserrat';background:#fbf8f1;color:#2b211c}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.2px} h1 span{color:#c98200}
.sub{color:#6e625a}
.kc{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Fira Sans';letter-spacing:3px;color:#8a5a00}
.kc b{width:46px;height:46px;border-radius:50%;background:#e8a317;color:#2b211c;font:800 22px/46px Montserrat;text-align:center;letter-spacing:0}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(43,33,28,.07)}
.lb{font:700 13px 'Fira Sans';letter-spacing:3px;color:#9a8f86}
"""
def cn(n, head, vis, css="", cta="Swipe", ctacss="background:#2b211c;color:#fff"):
    return page(CN + css, head, vis, "#2b211c", cta, ctacss, tagline=f"{n} / 5")
thali = '''<svg viewBox="0 0 400 400" width="400" height="400"><circle cx="200" cy="200" r="194" fill="#cfd6dc"/><circle cx="200" cy="200" r="180" fill="#e6eaee"/><circle cx="200" cy="200" r="172" fill="none" stroke="#b9c2ca" stroke-width="3"/>
<circle cx="130" cy="115" r="52" fill="#b9c2ca"/><circle cx="130" cy="115" r="44" fill="#e8a317"/>
<circle cx="250" cy="100" r="46" fill="#b9c2ca"/><circle cx="250" cy="100" r="38" fill="#7a9a3a"/>
<circle cx="300" cy="190" r="40" fill="#b9c2ca"/><circle cx="300" cy="190" r="32" fill="#fbf3dc"/>
<ellipse cx="165" cy="250" rx="95" ry="62" fill="#fffdf6"/><ellipse cx="150" cy="240" rx="40" ry="22" fill="#fff"/>
<circle cx="285" cy="290" r="48" fill="#d9a35b"/><circle cx="285" cy="290" r="38" fill="none" stroke="#b9823e" stroke-width="3"/><circle cx="270" cy="275" r="8" fill="#b9823e"/><circle cx="300" cy="300" r="6" fill="#b9823e"/></svg>'''
P["p95_canteen_s1"] = cn(1, """<h1 style="margin-top:34px">Paper coupons and a<br>fight over the bill?<br><span>Count every meal by scan.</span></h1>""",
f'''<div class=st1><div class=th1>{thali}</div><div class=cp1>{"".join(f'<div class=c1><span class=lb>MEAL COUPON</span><b>{m}</b><em>Torn, lost, counted by hand</em></div>' for m in ["Lunch","Tea","Lunch"])}</div></div>
<div class="cd td1"><span class=lb>TODAY · SAMPLE FACTORY</span>{"".join(f'<div><b>{n}</b><span>{m}</span></div>' for m,n in [("Breakfast",188),("Lunch",412),("Tea",630),("Dinner",96)])}</div>''',
""".vis{flex-direction:column;gap:16px}
.st1{flex:1;background:#2b211c;border-radius:30px;display:flex;align-items:center;justify-content:center;gap:34px;padding:24px;overflow:hidden}
.th1 svg{display:block}
.cp1{display:flex;flex-direction:column;gap:0;width:300px}
.c1{background:#fbf3dc;padding:18px 20px;display:flex;flex-direction:column;gap:4px;border-bottom:3px dashed #c9b98f;position:relative}
.c1:first-child{border-radius:14px 14px 0 0}.c1:last-child{border-radius:0 0 14px 14px;border-bottom:none;opacity:.55}
.c1 b{font:800 34px/1.25 Montserrat}.c1 em{font-style:normal;font:500 17px 'Fira Sans';color:#8a7a5a}
.td1{flex:none;display:flex;align-items:center;gap:10px;padding:18px 24px}
.td1 .lb{width:150px;line-height:1.5}
.td1 div{flex:1;display:flex;flex-direction:column;align-items:center;border-left:2px solid #f0e9da}
.td1 b{font:800 40px/1.25 Montserrat}.td1 span{font:600 18px 'Fira Sans';color:#6e625a}
""")

dep = [("Production · Shift A","Breakfast + lunch",210,240),("Production · Shift B","Lunch + dinner",150,240),("Stores","Lunch",28,40),("Office","Lunch + tea",64,80),("Security","All meals",18,20)]
P["p95_canteen_s2"] = cn(2, """<div class=kc><b>1</b>HEADCOUNT</div><h1 style="margin-top:14px">Tomorrow's headcount,<br><span>before you start cooking.</span></h1>""",
f'''<div class="cd hc2"><div class=hd2><b>Monday · expected meals</b><span class=lb>SAMPLE · FROM SHIFT ROSTER</span></div>
{"".join(f'<div class=r2><div class=n2><b>{a}</b><span>{b}</span></div><i class=b2><u style="width:{round(c*100/t)}%"></u></i><em>{c}<small> / {t}</small></em></div>' for a,b,c,t in dep)}
<div class=tt2><span>Cook for</span><b>470 people</b><span>Shift supervisors update by 6 pm.</span></div></div>''',
""".vis{flex-direction:column}
.hc2{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:6px}
.hd2{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}.hd2 b{font:800 28px Montserrat}
.r2{flex:1;display:flex;align-items:center;gap:18px;border-bottom:1.5px solid #f0e9da}
.n2{width:300px;flex:none}.n2 b{display:block;font:600 24px 'Fira Sans'}.n2 span{font:500 18px 'Fira Sans';color:#9a8f86}
.b2{flex:1;height:22px;border-radius:11px;background:#f3ecdc;position:relative;overflow:hidden;display:block}.b2 u{position:absolute;left:0;top:0;bottom:0;background:#e8a317;border-radius:11px}
.r2 em{font-style:normal;width:120px;text-align:right;font:800 28px Montserrat}.r2 small{font:600 17px 'Fira Sans';color:#9a8f86}
.tt2{margin-top:10px;display:flex;align-items:center;gap:16px;background:#2b211c;color:#fff;border-radius:16px;padding:14px 20px}
.tt2 b{font:800 32px Montserrat;color:#e8a317}.tt2 span{font:500 18px 'Fira Sans';color:#d8cfc6}.tt2 span:last-child{margin-left:auto}
""")

scans = [("Emp 1042","Lunch","12:41"),("Emp 0877","Lunch","12:41"),("Emp 1310","Lunch","12:40"),("Emp 0219","Lunch · second time","12:40")]
P["p95_canteen_s3"] = cn(3, """<div class=kc><b>2</b>SCAN</div><h1 style="margin-top:14px">Workers scan their ID card.<br><span>No paper coupons.</span></h1>""",
f'''<div class=tb3><div class=sc3><div class=lf3><div class=ok3>{ic("check",64)}</div><b>Lunch counted</b><span>Emp 1042 · Shift A</span><div class=ct3><div><em>Lunch now</em><b>287</b></div><div><em>Expected</em><b>470</b></div></div></div>
<div class=rt3><span class=lb>LAST SCANS · SAMPLE</span>{"".join(f'<div class="s3 {"dp" if "second" in m else ""}"><b>{e}</b><span>{m}</span><em>{t}</em></div>' for e,m,t in scans)}</div></div></div>
<div class=nt3>{ic("bell",26)}A second lunch on the same card is flagged at the counter.</div>''',
""".vis{flex-direction:column;gap:16px}
.tb3{flex:1;background:#3a302a;border-radius:40px;padding:22px;box-shadow:0 30px 60px rgba(43,33,28,.25);display:flex}
.sc3{flex:1;background:#fff;border-radius:22px;display:flex;gap:16px;padding:20px;overflow:hidden}
.lf3{flex:1;background:#fbf3dc;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:16px}
.ok3{width:120px;height:120px;border-radius:50%;background:#4f8a2e;color:#fff;display:flex;align-items:center;justify-content:center;margin-bottom:6px}
.lf3>b{font:800 38px/1.25 Montserrat}.lf3>span{font:500 23px 'Fira Sans';color:#6e625a}
.ct3{display:flex;gap:10px;margin-top:14px;width:100%}.ct3 div{flex:1;background:#fff;border-radius:14px;padding:12px;text-align:center}
.ct3 em{display:block;font-style:normal;font:600 18px 'Fira Sans';color:#9a8f86}.ct3 b{font:800 34px/1.3 Montserrat}
.rt3{flex:1;display:flex;flex-direction:column;gap:10px}
.s3{flex:1;border:2px solid #f0e9da;border-radius:14px;padding:0 16px;display:flex;flex-direction:column;justify-content:center;position:relative}
.s3 b{font:700 28px/1.3 'Fira Sans'}.s3 span{font:500 22px 'Fira Sans';color:#6e625a}.s3 em{position:absolute;right:16px;top:16px;font-style:normal;font:600 19px 'Fira Sans';color:#9a8f86}
.s3.dp{background:#fde3da;border-color:#e3714f}.s3.dp span{color:#b4401f;font-weight:700}
.nt3{flex:none;display:flex;align-items:center;gap:12px;background:#e8a317;border-radius:16px;padding:16px 20px;font:600 21px 'Fira Sans'}
""")

days = [380,402,395,410,388,170,0,398,405,412,400,392,180,0,401,399,407,415,396,175,0,404,409,398,411,393,168,0,402,406,397]
pts = " ".join(f"{i*20+10},{120-v/4.2:.0f}" for i,v in enumerate(days))
bill = [("Breakfast","5,120"),("Lunch","9,913"),("Tea","15,410"),("Dinner","2,340")]
P["p95_canteen_s4"] = cn(4, """<div class=kc><b>3</b>MONTHLY BILL</div><h1 style="margin-top:14px">The month-end bill,<br><span>made from the scans.</span></h1>""",
f'''<div class=dc4><div class=hd4><div><span class=lb>MEAL BILL · SAMPLE</span><b>Sample Factory Pvt Ltd</b><em>October 2026 · 31 days</em></div><div class=st4>Matches scans</div></div>
<div class=th4><span>Meal</span><span>Meals served</span></div>{"".join(f'<div class=r4><b>{m}</b><span>{q}</span></div>' for m,q in bill)}
<div class=ch4><span class=lb>LUNCHES PER DAY · OCTOBER</span><svg viewBox="0 0 620 130" width="100%" height="130" preserveAspectRatio="none"><polyline points="{pts}" fill="none" stroke="#e8a317" stroke-width="4" stroke-linejoin="round"/></svg></div>
<div class=ft4>Rates as per your contract · day-wise list attached</div></div>''',
""".vis{flex-direction:column}
.dc4{flex:1;background:#fff;border-radius:10px;box-shadow:0 24px 50px rgba(43,33,28,.12);padding:28px 32px;display:flex;flex-direction:column;border-top:12px solid #e8a317}
.hd4{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:14px;border-bottom:2px solid #2b211c}
.hd4 b{display:block;font:800 32px/1.3 Montserrat;margin-top:4px}.hd4 em{font-style:normal;font:500 19px 'Fira Sans';color:#6e625a}
.st4{font:800 18px Montserrat;color:#4f8a2e;border:3px solid #4f8a2e;border-radius:10px;padding:8px 14px}
.th4{display:flex;justify-content:space-between;padding:12px 0 4px;font:700 15px 'Fira Sans';letter-spacing:2px;color:#9a8f86;text-transform:uppercase}
.r4{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px dashed #e6dccb}
.r4 b{font:600 26px 'Fira Sans'}.r4 span{font:800 30px Montserrat}
.ch4{margin-top:14px;background:#fbf8f1;border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.ch4 svg{display:block}
.ft4{margin-top:12px;font:600 18px 'Fira Sans';color:#6e625a}
""")

P["p95_canteen_s5"] = cn(5, """<h1 style="margin-top:34px">Run a factory or<br>office canteen?<br><span>Let's build your app.</span></h1>""",
f'''<div class=g5>{"".join(f'<div class="cd t5 {c}"><div class=tp5>{ic(i,56)}<i>0{n}</i></div><b>{t}</b><span>{d}</span></div>' for n,(i,t,d,c) in enumerate([("users","Headcount","By shift, the day before",""),("check","ID card scan","Every meal counted","dk"),("bell","Second-meal flag","Right at the counter","dk"),("file","Monthly bill","Made from the scans","")],1))}
</div>''',
""".g5{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;position:relative}
.t5{padding:26px;display:flex;flex-direction:column;justify-content:flex-end;gap:8px}
.tp5{margin-bottom:auto;display:flex;justify-content:space-between;align-items:flex-start}.tp5 i{font:800 110px/1.2 Montserrat;font-style:normal;color:#f3ecdc}.t5.dk .tp5 i{color:#45382f}
.t5 svg{color:#c98200}.t5 b{font:800 32px/1.25 Montserrat}.t5 span{font:500 20px 'Fira Sans';color:#6e625a}
.t5.dk{background:#2b211c;color:#fff}.t5.dk svg{color:#e8a317}.t5.dk span{color:#d8cfc6}
.pp5{display:none}
""", cta="Canteen contractor? DM us", ctacss="background:#e8a317;color:#2b211c")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
