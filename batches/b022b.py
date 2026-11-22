import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 126 INDIA · AC repair and service · CAROUSEL 5 · Archivo Black + Roboto · ice blue / navy / signal orange
# New techniques: SVG split-AC indoor unit with a hanging AMC string tag, month bar strip of visits due, SVG street-grid route map.
AC = """
body{--f:'Roboto';--h:'Archivo Black';background:#dcebf5;color:#10264a}
h1{font-family:'Archivo Black';font-weight:400;font-size:60px;letter-spacing:-.5px;line-height:1.25;margin-top:30px} h1 span{color:#e8551c}
.sub{color:#4b5f7d}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Roboto';letter-spacing:3px;color:#10264a}
.kt b{width:44px;height:44px;border-radius:12px;background:#ff6a2b;color:#fff;font:400 22px/1 'Archivo Black';display:flex;align-items:center;justify-content:center}
.kt + h1{margin-top:20px}
.cd{background:#fff;border-radius:24px;box-shadow:0 16px 32px rgba(16,38,74,.08)}
.lb{font:700 13px 'Roboto';letter-spacing:3px;color:#8796ad}
"""
def ac(n, head, vis, css="", cta="Swipe", ctacss="background:#10264a;color:#fff"):
    return page(AC + css, head, vis, "#10264a", cta, ctacss, tagline=f"{n} / 5")
def unit(w):
    return f'''<svg viewBox="0 0 560 300" width="{w}" style="display:block">
<rect x="10" y="10" width="540" height="150" rx="26" fill="#fff"/><rect x="10" y="118" width="540" height="42" rx="0" fill="#eef3f8"/><rect x="10" y="134" width="540" height="26" rx="13" fill="#eef3f8"/>
<rect x="40" y="128" width="480" height="8" rx="4" fill="#c9d6e4"/><rect x="40" y="144" width="480" height="6" rx="3" fill="#d9e3ee"/>
<rect x="420" y="40" width="96" height="34" rx="8" fill="#10264a"/><text x="468" y="64" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="20" fill="#7fd0ff">24°</text>
<circle cx="390" cy="57" r="6" fill="#3ccf8e"/>
<path d="M150 160 C150 190 170 200 190 206" stroke="#7d8ea6" stroke-width="3" fill="none"/>
<rect x="160" y="196" width="270" height="94" rx="14" fill="#ffd9c6"/><circle cx="182" cy="218" r="8" fill="#dcebf5"/>
<text x="200" y="224" font-family="Roboto" font-weight="700" font-size="17" fill="#10264a">AMC · SAMPLE FLAT 302</text>
<text x="180" y="252" font-family="Roboto" font-weight="500" font-size="17" fill="#4b5f7d">Visit 2 of 3 done</text>
<text x="180" y="276" font-family="Roboto" font-weight="700" font-size="17" fill="#c8430f">Next visit: March</text></svg>'''
months = [("Jan",18),("Feb",26),("Mar",64),("Apr",92),("May",71),("Jun",30),("Jul",12),("Aug",10),("Sep",22),("Oct",35),("Nov",28),("Dec",14)]
P["p126_ac_s1"] = ac(1, "<h1>Whose AC service<br>is due this week?<br><span>Keep every AMC with<br>its next visit date.</span></h1>",
f'''<div class=c1><div class=hr1><span class=tg1>AC REPAIR · SERVICE · AMC</span>{unit(600)}</div>
<div class="cd ch1"><div class=t1><span class=lb>AMC VISITS DUE PER MONTH · SAMPLE</span><b>227 visits due Mar–May</b></div>
<div class=bs1>{"".join(f'<div class="b1{" hot" if m in ("Mar","Apr","May") else ""}{" now" if m=="Nov" else ""}"><em>{v}</em><i style="height:{v/92*100:.0f}%"></i><span>{m}</span></div>' for m,v in months)}</div>
<div class=nt1>Plan your technicians before the summer rush, not during it.</div></div></div>''',
""".c1{flex:1;display:flex;flex-direction:column;gap:18px}
.hr1{flex:1;background:linear-gradient(160deg,#173563,#0c1d3a);border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:22px}
.tg1{font:700 15px 'Roboto';letter-spacing:3px;color:#7fd0ff}
.ch1{flex:none;padding:20px 24px;display:flex;flex-direction:column;gap:12px}
.t1{display:flex;justify-content:space-between;align-items:center}.t1 b{font:400 22px/1.3 'Archivo Black';color:#e8551c}
.bs1{height:190px;display:flex;gap:10px;align-items:stretch}
.b1{flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:4px}
.b1 i{width:100%;background:#b9cde2;border-radius:8px 8px 3px 3px;display:block}
.b1 em{font:700 15px 'Roboto';font-style:normal;color:#4b5f7d}.b1 span{font:600 15px 'Roboto';color:#4b5f7d}
.b1.hot i{background:#ff6a2b}.b1.hot em{color:#c8430f}.b1.now i{background:#10264a}.b1.now span{color:#10264a;font-weight:800}
.nt1{font:500 19px 'Roboto';color:#4b5f7d}""")

rows = [("Sample Office, 4th floor", "6 split AC", 1, "Nov · today", "td"), ("Sample Restaurant", "2 cassette AC", 1, "Nov · today", "td"),
        ("Sample Flat 118", "2 split AC", 0, "Nov · today", "td"), ("Sample Shop, Main Road", "1 window AC", 3, "AMC ends Jan · renew", "rn"),
        ("Sample Bungalow", "3 split AC", 2, "February", "ok"), ("Sample Flat 302", "2 split AC", 2, "March", "ok")]
P["p126_ac_s2"] = ac(2, "<div class=kt><b>1</b>AMC LIST</div><h1>Every customer, every visit,<br><span>in one list.</span></h1>",
browser(f'''<div class=w2><div class=ch2>{"".join(f'<span class="{k}">{t}</span>' for k,t in [("on","Due in Nov · 28"),("","Renewals · 6"),("","All AMCs")])}<em class=lb>SAMPLE</em></div>
<div class=hd2><span>CUSTOMER</span><span>VISITS</span><span>NEXT VISIT</span></div>
{"".join(f'<div class=r2><div class=n2><b>{a}</b><span>{u}</span></div><div class=d2>' + "".join(f'<i class="{"f" if j<d else ""}"></i>' for j in range(3)) + f'<small>{d} of 3</small></div><em class="p2 {k}">{nx}</em></div>' for a,u,d,nx,k in rows)}
<div class=ft2>{ic("bell",22)}<span>Renewal reminder goes to the customer 30 days before the AMC ends.</span></div></div>''', "amc.yourservice.in", "flex:1"),
""".vis{flex-direction:column}
.w2{flex:1;padding:18px 22px 20px;display:flex;flex-direction:column;gap:8px}
.ch2{display:flex;gap:10px;align-items:center;margin-bottom:6px}.ch2 span{font:600 17px 'Roboto';padding:9px 16px;border-radius:22px;background:#eef3f8;color:#4b5f7d}
.ch2 span.on{background:#10264a;color:#fff}.ch2 em{margin-left:auto;font-style:normal}
.hd2,.r2{display:grid;grid-template-columns:1fr 170px 230px;align-items:center;gap:12px}
.hd2 span{font:700 13px 'Roboto';letter-spacing:2.5px;color:#8796ad}
.r2{flex:1;border-top:1.5px solid #e6edf4}
.n2 b{display:block;font:700 22px 'Roboto'}.n2 span{font:500 17px 'Roboto';color:#6b7c95}
.d2{display:flex;align-items:center;gap:7px}.d2 i{width:20px;height:20px;border-radius:50%;border:2.5px solid #b9cde2;display:block}.d2 i.f{background:#10264a;border-color:#10264a}
.d2 small{margin-left:6px;font:600 16px 'Roboto';color:#6b7c95}
.p2{font-style:normal;justify-self:start;font:700 17px 'Roboto';padding:8px 12px;border-radius:10px}
.td{background:#ffe1d3;color:#b33f0e}.rn{background:#fff1c4;color:#7a5a00}.ok{background:#e3eef8;color:#2d4f80}
.ft2{display:flex;align-items:center;gap:10px;background:#10264a;color:#fff;border-radius:14px;padding:13px 16px;font:500 18px 'Roboto'}""")

stops = [(1, "10:00", "Sample Office, 4th floor", "6 split AC"), (2, "12:30", "Sample Restaurant", "2 cassette AC"), (3, "2:30", "Sample Flat 118", "2 split AC"),
         (4, "4:00", "Sample Salon", "2 split AC"), (5, "5:30", "Sample Flat 45", "1 split AC")]
pins = [(140, 103), (243, 200), (140, 293), (330, 483), (413, 600)]
roads = "".join(f'<rect x="0" y="{y}" width="500" height="26" fill="#fff"/>' for y in (90, 280, 470, 650)) + "".join(f'<rect x="{x}" y="0" width="26" height="760" fill="#fff"/>' for x in (60, 230, 400))
blocks = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}"/>' for x,y,w,h,c in [(100,10,110,60,"#cfe0ee"),(270,130,110,120,"#d6ead8"),(100,330,110,120,"#cfe0ee"),(270,520,110,110,"#cfe0ee"),(440,140,50,110,"#cfe0ee"),(100,520,110,110,"#d6ead8"),(440,690,50,60,"#d6ead8"),(270,10,110,60,"#cfe0ee")])
route = "M140 103 L243 103 L243 293 L140 293 M243 293 L243 483 L413 483 L413 600"
P["p126_ac_s3"] = ac(3, "<div class=kt><b>2</b>TODAY'S ROUTE</div><h1>Visits sorted by area,<br><span>less time on the road.</span></h1>",
f'''<div class=w3><div class="cd mp3"><svg viewBox="0 0 500 760" width="100%" height="100%" preserveAspectRatio="xMidYMid slice"><rect width="500" height="760" fill="#e7f0f7"/>{roads}{blocks}
<path d="{route}" stroke="#ff6a2b" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 14"/>
{"".join(f'<circle cx="{x}" cy="{y}" r="26" fill="#10264a"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Archivo Black" font-size="22" fill="#fff">{i+1}</text>' for i,(x,y) in enumerate(pins))}</svg></div>
<div class="cd ls3"><span class=lb>TECHNICIAN 1 · SAMPLE</span><b class=h3>5 visits · 13 AC units</b>
{"".join(f'<div class=s3><i>{n}</i><div><em>{t}</em><b>{a}</b><span>{u}</span></div></div>' for n,t,a,u in stops)}</div></div>''',
""".w3{flex:1;display:flex;gap:18px}
.mp3{flex:1;overflow:hidden;padding:0}
.ls3{width:400px;flex:none;padding:20px 22px;display:flex;flex-direction:column;gap:6px}
.h3{font:400 26px/1.3 'Archivo Black';margin-bottom:4px}
.s3{flex:1;display:flex;align-items:center;gap:14px;border-top:1.5px solid #e6edf4}
.s3 i{width:40px;height:40px;flex:none;border-radius:50%;background:#10264a;color:#fff;font:400 18px/1 'Archivo Black';font-style:normal;display:flex;align-items:center;justify-content:center}
.s3 em{font-style:normal;font:700 15px 'Roboto';color:#e8551c}.s3 b{display:block;font:700 20px/1.25 'Roboto'}.s3 span{font:500 16px 'Roboto';color:#6b7c95}""")

checks = [("Filters washed", 1), ("Indoor coil cleaned", 1), ("Drain pipe cleared", 1), ("Gas pressure checked", 1), ("Outdoor unit cleaned", 1)]
P["p126_ac_s4"] = ac(4, "<div class=kt><b>3</b>SERVICE REPORT</div><h1>The report reaches the customer<br><span>before the tech leaves.</span></h1>",
f'''<div class=w4>{phone(f"""<div class=ap4><span class=lb>VISIT 2 OF 3 · SAMPLE</span><b class=t4>Sample Restaurant</b><span class=u4>2 cassette AC</span>
<div class=ph4><div class=bf4><i class=dt4></i><span>Before</span></div><div class=af4><i class=cl4></i><span>After</span></div></div>
{"".join(f'<div class=ck4><i>{ic("check",16,"#fff",3)}</i>{a}</div>' for a,_ in checks)}
<div class=sg4>Customer sign ✓</div><div class=bt4>Send report on WhatsApp</div></div>""", w=360, h=740)}
<div class=sd4>{"".join(f'<div class="cd c4"><i>{ic(i,30,"#e8551c")}</i><b>{a}</b><span>{b}</span></div>' for i,a,b in [("send","Report + photos sent","Customer sees what was done"),("cal","Next visit set: March","Added to the AMC list"),("users","Job closed on the spot","The office sees it live")])}</div></div>''',
""".w4{flex:1;display:flex;gap:26px;align-items:center}
.ap4{flex:1;padding:8px 18px 18px;display:flex;flex-direction:column;gap:8px;background:#f4f8fc}
.t4{font:400 22px/1.3 'Archivo Black'}.u4{font:500 16px Roboto;color:#6b7c95;margin-top:-6px}
.ph4{display:flex;gap:8px;height:120px;flex:none}
.ph4>div{flex:1;border-radius:12px;position:relative;overflow:hidden}
.ph4 span{position:absolute;left:8px;bottom:8px;font:700 13px 'Roboto';background:rgba(16,38,74,.8);color:#fff;padding:3px 8px;border-radius:6px}
.ph4 i{position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0 5px,rgba(0,0,0,.12) 5px 7px),repeating-linear-gradient(90deg,transparent 0 5px,rgba(0,0,0,.12) 5px 7px)}
.dt4{background-color:#a59a7e!important}.cl4{background-color:#e9f3fb!important}
.ck4{flex:1;display:flex;align-items:center;gap:10px;background:#fff;border-radius:12px;padding:0 12px;font:600 17px 'Roboto'}
.ck4 i{width:26px;height:26px;border-radius:7px;background:#2fae6e;display:flex;align-items:center;justify-content:center;flex:none}
.sg4{font:500 15px 'Roboto';color:#6b7c95;text-align:center}
.bt4{background:#ff6a2b;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 17px 'Roboto'}
.sd4{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:16px;justify-content:center}
.c4{flex:1;padding:22px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.c4 b{font:400 27px/1.3 'Archivo Black'}.c4 span{font:500 20px 'Roboto';color:#6b7c95}""")

P["p126_ac_s5"] = ac(5, "<h1>Run an AC repair and<br>service business?<br><span>Let's build your AMC<br>and service app.</span></h1>",
f'''<div class=w5><div class=hr5>{unit(520)}</div><div class=g5>{"".join(f'<div class="cd t5"><i>0{i+1}</i><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate([("AMC list","Next visit for every customer"),("Route for each tech","Visits sorted by area"),("Report on WhatsApp","Photos and checklist"),("Renewal reminders","30 days before the end")]))}</div></div>''',
""".w5{flex:1;display:flex;flex-direction:column;gap:18px}
.hr5{flex:none;height:330px;background:linear-gradient(160deg,#173563,#0c1d3a);border-radius:30px;display:flex;align-items:center;justify-content:center}
.g5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.t5{padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px;position:relative;overflow:hidden}
.t5 i{font:400 30px/1.3 'Archivo Black';font-style:normal;color:#ff6a2b}.t5 b{font:400 25px/1.3 'Archivo Black'}.t5 span{font:500 19px 'Roboto';color:#6b7c95}""",
cta="Service ACs? DM us", ctacss="background:#ff6a2b;color:#fff")

# ───────── 130 INDIA · Namkeen (snack) manufacturer · CAROUSEL 6 · Lora + Fira Sans · sev yellow / chilli red / kraft
# New techniques: SVG pillow-pouch snack packets with crimped seals and a see-through window, order matrix with totals/ready/to-make rows.
NK = """
body{--f:'Fira Sans';--h:'Lora';background:#f0e3cb;color:#3b2516}
h1{font-family:'Lora';font-weight:700;font-size:62px;letter-spacing:-.6px;line-height:1.2} h1 span{color:#c7361f}
.sub{color:#6e5640}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Fira Sans';letter-spacing:3px;color:#c7361f}
.kt b{width:44px;height:44px;border-radius:50%;background:#c7361f;color:#fff;font:700 22px/1 'Lora';display:flex;align-items:center;justify-content:center}
.kt + h1{margin-top:16px}
.cd{background:#fffaf0;border-radius:24px;box-shadow:0 14px 30px rgba(59,37,22,.08)}
.lb{font:700 13px 'Fira Sans';letter-spacing:3px;color:#9a8670}
"""
def nk(n, head, vis, css="", cta="Swipe", ctacss="background:#3b2516;color:#f6c84c"):
    return page(NK + css, head, vis, "#3b2516", cta, ctacss, tagline=f"{n} / 6")
import random
def pouch(name, size, col, fill, w=190, seed=1):
    r = random.Random(seed)
    zz = lambda y, d: "".join(f'L{10+i*10} {y+(d if i%2 else 0)}' for i in range(1, 17))
    dots = "".join(f'<circle cx="{r.uniform(52,128):.0f}" cy="{r.uniform(150,200):.0f}" r="{r.uniform(2.5,5):.1f}" fill="{fill}"/>' for _ in range(34))
    return f'''<svg viewBox="0 0 180 270" width="{w}" style="display:block"><defs><clipPath id="w{seed}"><rect x="44" y="140" width="92" height="70" rx="12"/></clipPath></defs>
<path d="M10 18 {zz(18,-8)} L170 252 {"".join(f'L{170-i*10} {252+(8 if i%2 else 0)}' for i in range(1,17))} Z" fill="{col}"/>
<path d="M10 18 {zz(18,-8)} L170 18 L170 34 L10 34 Z" fill="#000" opacity=".12"/><path d="M10 236 L170 236 L170 252 L10 252 Z" fill="#000" opacity=".12"/>
<rect x="24" y="52" width="132" height="70" rx="10" fill="#fffaf0"/><text x="90" y="84" text-anchor="middle" font-family="Lora" font-weight="700" font-size="19" fill="#3b2516">{name}</text>
<text x="90" y="108" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="15" fill="#c7361f">{size}</text>
<rect x="44" y="140" width="92" height="70" rx="12" fill="#fff3d6"/><g clip-path="url(#w{seed})">{dots}</g><rect x="44" y="140" width="92" height="70" rx="12" fill="none" stroke="#fff" stroke-width="3"/></svg>'''
prods = [("Aloo bhujia", "200 g", "#e9a91c", "#d98c12"), ("Moong dal", "150 g", "#3f8f4e", "#e6c35a"), ("Mixture", "200 g", "#c7361f", "#b8742a"), ("Masala peanuts", "150 g", "#7a4a2a", "#a0522d")]
P["p130_nk_s1"] = nk(1, "<h1>Distributor wants<br>200 boxes by Friday?<br><span>Plan production from<br>real orders.</span></h1>",
f'''<div class=c1><div class=sh1>{"".join(f'<div class=pk1>{pouch(a if a!="Masala peanuts" else "Peanuts",b,c,f,205,i+1)}</div>' for i,(a,b,c,f) in enumerate(prods))}</div>
<div class=st1>{"".join(f'<div class="cd s1 {k}"><b>{v}</b><span>{t}</span></div>' for v,t,k in [("460","boxes ordered this week",""),("105","boxes already packed",""),("355","boxes to make","hi")])}</div>
<div class=nt1>Sample · 3 distributors · 1 box = 30 packets</div></div>''',
""".c1{flex:1;display:flex;flex-direction:column;gap:16px}
.sh1{flex:1;background:linear-gradient(#c9a57a 0 84%,#a9825a 84%);border-radius:30px;display:flex;align-items:flex-end;justify-content:space-around;padding:24px 20px 34px;position:relative}.sh1:before{content:"THIS WEEK'S ORDERS · SAMPLE";position:absolute;left:24px;top:22px;font:700 14px 'Fira Sans';letter-spacing:3px;color:#5a3d28}
.st1{flex:none;display:flex;gap:16px}
.s1{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:2px}
.s1 b{font:700 52px/1.35 'Lora'}.s1 span{font:600 18px 'Fira Sans';color:#6e5640}
.s1.hi{background:#c7361f;color:#fff}.s1.hi span{color:#ffd9cf}
.nt1{font:600 16px 'Fira Sans';color:#6e5640;letter-spacing:.5px}""")

cols = ["Aloo bhujia", "Moong dal", "Mixture", "Peanuts", "Total"]
mat = [("Sample Distributor 1", [80, 40, 30, 50], ""), ("Sample Distributor 2", [60, 30, 40, 20], ""), ("Sample Distributor 3", [40, 20, 20, 30], ""),
       ("Total ordered", [180, 90, 90, 100], "tt"), ("Already packed", [30, 10, 25, 40], "rd"), ("To make", [150, 80, 65, 60], "mk")]
P["p130_nk_s2"] = nk(2, "<div class=kt><b>1</b>ORDERS IN</div><h1>All distributor orders<br><span>add up by themselves.</span></h1>",
f'''<div class=w2><div class="cd tb2"><div class="r2 hd2"><span class=lb>BOXES · SAMPLE</span>{"".join(f'<span>{c}</span>' for c in cols)}</div>
{"".join(f'<div class="r2 {k}"><b>{a}</b>' + "".join(f'<em>{v}</em>' for v in vs) + f'<em class=sm2>{sum(vs)}</em></div>' for a,vs,k in mat)}</div>
<div class=nt2>{ic("check",24,"#fff",3)}<span>Orders come from the distributor app, so nobody retypes a WhatsApp message.</span></div></div>''',
""".w2{flex:1;display:flex;flex-direction:column;gap:16px}
.tb2{flex:1;padding:16px 22px;display:flex;flex-direction:column}
.r2{flex:1;display:grid;grid-template-columns:1.6fr repeat(5,1fr);align-items:center;gap:8px;border-top:1.5px solid #eadcc4}
.r2 b{font:600 21px/1.25 'Fira Sans'}.r2 em{font-style:normal;font:500 25px 'Fira Sans';text-align:center}
.hd2{flex:none;padding:6px 0 12px;border-top:0}.hd2 span{font:700 16px/1.25 'Fira Sans';text-align:center;color:#6e5640}.hd2 span.lb{text-align:left;font-size:13px}
.sm2{font-weight:700!important}
.tt{border-top:3px solid #3b2516}.tt b,.tt em{font-weight:700}
.rd b,.rd em{color:#6e5640}
.mk{background:#c7361f;color:#fff;border-radius:16px;border-top:0;margin-top:6px;padding:0 0 0 14px}.mk em{font-weight:700}
.nt2{flex:none;display:flex;align-items:center;gap:12px;background:#3b2516;color:#fff;border-radius:16px;padding:16px 20px;font:500 19px 'Fira Sans'}""")

days = [("Mon", [("Line 1", "Aloo bhujia · 450 kg", "75 boxes", "y")]), ("Tue", [("Line 1", "Aloo bhujia · 450 kg", "75 boxes", "y")]),
        ("Wed", [("Line 1", "Moong dal · 360 kg", "80 boxes", "g")]), ("Thu", [("Line 1", "Mixture · 390 kg", "65 boxes", "r"), ("Line 2", "Peanuts · 270 kg", "60 boxes", "b")]),
        ("Fri", [("Dispatch", "Sample Distributor 1", "200 boxes", "d")]), ("Sat", [("Dispatch", "Distributors 2 + 3", "260 boxes", "d")])]
P["p130_nk_s3"] = nk(3, "<div class=kt><b>2</b>PRODUCTION PLAN</div><h1>A week plan made from<br><span>the “to make” row.</span></h1>",
f'''<div class="cd w3"><div class=t3><span class=lb>THIS WEEK · SAMPLE</span><span class=lb>355 BOXES TO MAKE</span></div>
{"".join(f'<div class=d3><b>{d}</b><div class=bb3>' + "".join(f'<div class="j3 {k}"><i>{l}</i><span>{t}</span><em>{x}</em></div>' for l,t,x,k in js) + '</div></div>' for d,js in days)}</div>''',
""".w3{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:8px}
.t3{display:flex;justify-content:space-between}
.d3{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px solid #eadcc4}
.d3>b{width:70px;flex:none;font:700 28px 'Lora'}
.bb3{flex:1;display:flex;gap:10px}
.j3{flex:1;display:flex;align-items:center;gap:12px;border-radius:14px;padding:14px 16px}
.j3 i{font-style:normal;font:700 14px 'Fira Sans';letter-spacing:1px;opacity:.75;white-space:nowrap}.j3 span{flex:1;font:600 20px/1.3 'Fira Sans'}.j3 em{font-style:normal;font:700 17px 'Fira Sans';white-space:nowrap}
.y{background:#f6d77a}.g{background:#cfe5c4}.r{background:#f4c3b6}.b{background:#e3cdb6}.d{background:#3b2516;color:#fff}""")

P["p130_nk_s4"] = nk(4, "<div class=kt><b>3</b>BATCH + PACKING</div><h1>Know how many packets are done,<br><span>and if film will run out.</span></h1>",
f'''<div class=w4><div class="cd bc4"><span class=lb>BATCH CARD · SAMPLE</span><b class=h4>B-1123 · Aloo bhujia 200 g</b>
<div class=kv4>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [("Made","Monday · Line 1"),("Quantity","450 kg"),("Packets","2,250 = 75 boxes"),("Checked by","Supervisor 1")])}</div>
<div class=pr4><div class=pt4><span>Packed</span><b>1,620 of 2,250 packets</b></div><u><s style="width:72%"></s></u><small>54 of 75 boxes · 72%</small></div></div>
<div class=sd4><div class="cd pc4">{pouch("Aloo bhujia","200 g","#e9a91c","#d98c12",220,9)}</div>
<div class="cd fm4"><span class=lb>POUCH FILM · 200 G</span><b>2,900 left</b><span class=tx4>Needed: 630 for this batch + 2,250 on Tuesday = 2,880</span><em>Order more before Wednesday</em></div></div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.bc4{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:14px}
.h4{font:700 32px/1.25 'Lora'}
.kv4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.kv4 div{background:#f5ead6;border-radius:16px;padding:14px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.kv4 span{font:600 17px 'Fira Sans';color:#9a8670;letter-spacing:1px}.kv4 b{font:700 30px/1.35 'Lora'}
.pr4{display:flex;flex-direction:column;gap:8px;background:#3b2516;color:#fff;border-radius:18px;padding:18px 20px}
.pt4{display:flex;justify-content:space-between;align-items:baseline}.pt4 span{font:600 17px 'Fira Sans';color:#e3cdb6}.pt4 b{font:700 22px 'Fira Sans'}
.pr4 u{display:block;height:16px;border-radius:8px;background:#5a3d28;position:relative;overflow:hidden}.pr4 u s{position:absolute;left:0;top:0;bottom:0;background:#f6c84c;border-radius:8px}
.pr4 small{font:600 16px 'Fira Sans';color:#f6c84c}
.sd4{width:330px;flex:none;display:flex;flex-direction:column;gap:18px}
.pc4{flex:1;display:flex;align-items:center;justify-content:center;background:#c9a57a}
.fm4{flex:none;padding:20px 22px;display:flex;flex-direction:column;gap:6px}
.fm4 b{font:700 40px/1.35 'Lora';color:#c7361f}.tx4{font:500 17px/1.4 'Fira Sans';color:#6e5640}
.fm4 em{font-style:normal;margin-top:6px;background:#ffe1a0;color:#7a4a00;border-radius:10px;padding:9px 12px;font:700 16px 'Fira Sans'}""")

load = [("Aloo bhujia 200 g", 80, 1), ("Moong dal 150 g", 40, 1), ("Mixture 200 g", 30, 1), ("Masala peanuts 150 g", 50, 0)]
P["p130_nk_s5"] = nk(5, "<div class=kt><b>4</b>DISPATCH</div><h1>Load the truck from a list,<br><span>not from memory.</span></h1>",
f'''<div class=w5><div class="cd ds5"><div class=t5><div><span class=lb>DISPATCH · FRIDAY · SAMPLE</span><b>Sample Distributor 1</b></div><em>200 boxes</em></div>
{"".join(f'<div class="l5{" on" if d else ""}"><i>{ic("check",20,"#fff",3) if d else ""}</i><b>{a}</b><span>{q} boxes</span><em>{"Loaded" if d else "Loading"}</em></div>' for a,q,d in load)}
<div class=bm5><div><span>Loaded</span><b>150 of 200</b></div><div><span>Invoice</span><b>Ready to send</b></div><div><span>Driver</span><b>Sample Driver</b></div></div></div></div>''',
""".w5{flex:1;display:flex}
.ds5{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:10px}
.t5{display:flex;justify-content:space-between;align-items:center;padding-bottom:8px}.t5 b{display:block;font:700 34px/1.3 'Lora'}
.t5 em{font-style:normal;font:700 22px 'Fira Sans';background:#c7361f;color:#fff;border-radius:14px;padding:10px 16px}
.l5{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px solid #eadcc4}
.l5 i{width:38px;height:38px;border-radius:10px;border:2.5px solid #c9a57a;display:flex;align-items:center;justify-content:center;flex:none}
.l5.on i{background:#3f8f4e;border-color:#3f8f4e}
.l5 b{flex:1;font:600 24px 'Fira Sans'}.l5 span{font:700 24px 'Fira Sans';width:130px;text-align:right}
.l5 em{font-style:normal;font:700 16px 'Fira Sans';width:110px;text-align:center;padding:7px 0;border-radius:10px;background:#ffe1a0;color:#7a4a00}
.l5.on em{background:#dcefd6;color:#2d6b39}
.bm5{display:flex;gap:12px}
.bm5 div{flex:1;background:#3b2516;color:#fff;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:2px}
.bm5 span{font:600 15px 'Fira Sans';color:#e3cdb6}.bm5 b{font:700 21px 'Fira Sans'}""")

P["p130_nk_s6"] = nk(6, "<h1>Make namkeen or snacks?<br><span>Let's build your order<br>and production app.</span></h1>",
f'''<div class=w6><div class=pk6>{"".join(pouch(a if a!="Masala peanuts" else "Peanuts",b,c,f,150,20+i) for i,(a,b,c,f) in enumerate(prods))}</div>
<div class=g6>{"".join(f'<div class="cd t6"><b>{a}</b><span>{b}</span></div>' for a,b in [("Distributor orders","Added up by product"),("Week plan","From the “to make” row"),("Batch + packing","Packets and film stock"),("Dispatch list","Box by box, per truck")])}</div></div>''',
""".w6{flex:1;display:flex;flex-direction:column;gap:18px}
.pk6{flex:none;height:300px;background:linear-gradient(#c9a57a 0 84%,#a9825a 84%);border-radius:30px;display:flex;align-items:flex-end;justify-content:space-around;padding:0 20px 26px}
.g6{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.t6{padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-left:8px solid #c7361f}
.t6 b{font:700 36px/1.3 'Lora'}.t6 span{font:500 22px 'Fira Sans';color:#6e5640}""",
cta="Make snacks? DM us", ctacss="background:#c7361f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
