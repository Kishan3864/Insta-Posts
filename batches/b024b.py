import sys, datetime, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 136 USA · Event venue · CAROUSEL 5 · Lora + Open Sans · champagne / ink navy / blush
# New technique: "Saturday matrix" — every Saturday of 2027 as a dot (booked / on hold / open), months as rows.
EV = """
body{--f:'Open Sans';--h:'Lora';background:#f3e7d3;color:#1c2541}
h1{font-family:'Lora';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#b4545a}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Open Sans';letter-spacing:3px;color:#1c2541}
.kt b{width:44px;height:44px;border-radius:50%;background:#1c2541;color:#f3e7d3;font:700 22px/1 'Lora';display:flex;align-items:center;justify-content:center}
.kt + h1{margin-top:16px}
.cd{background:#fffaf1;border-radius:24px;box-shadow:0 14px 30px rgba(28,37,65,.08)}
.lb{font:700 13px 'Open Sans';letter-spacing:3px;color:#9a8f7e}
"""
def ev(n, head, vis, css="", cta="Swipe", ctacss="background:#1c2541;color:#f3e7d3"):
    return page(EV + css, head, vis, "#1c2541", cta, ctacss, tagline=f"{n} / 5")
rnd = random.Random(7)
sat = {}
d = datetime.date(2027, 1, 2)
while d.year == 2027:
    m = d.month
    p = {5: .75, 6: .85, 9: .8, 10: .8, 7: .5, 8: .5, 4: .45, 11: .35, 12: .4}.get(m, .2)
    r = rnd.random()
    st = "bk" if r < p else "hd" if r < p + .12 else "op"
    sat.setdefault(m, []).append((d.day, st)); d += datetime.timedelta(days=7)
sat[6] = [(day, "op" if day == 12 else st) for day, st in sat[6]]
cnt = {k: sum(1 for m in sat.values() for _, s in m if s == k) for k in ("bk", "hd", "op")}
MN = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
P["p136_ev_s1"] = ev(1, "<h1>“Is Saturday, June 12<br>still open?”<br><span>Show your dates before<br>couples have to ask.</span></h1>",
f'''<div class="cd w1"><div class=t1><span class=lb>2027 SATURDAYS · SAMPLE VENUE</span><div class=lg1><span><i class=bk></i>Booked</span><span><i class=hd></i>On hold</span><span><i class=op></i>Open</span></div></div>
<div class=gr1>{"".join(f'<div class=mr1><b>{MN[m-1]}</b><div class=ds1>' + "".join(f'<i class="{s}{" me" if (m==6 and dd==12) else ""}">{dd}</i>' for dd,s in sat[m]) + '</div></div>' for m in range(1,13))}</div>
<div class=nt1>{ic("cal",22)}<span><b>June 12 is open.</b> The couple books a tour from the same page.</span></div></div>''',
""".w1{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px}
.t1{display:flex;justify-content:space-between;align-items:center}
.lg1{display:flex;gap:14px}.lg1 span{display:flex;align-items:center;gap:6px;font:600 15px 'Open Sans'}.lg1 i{width:16px;height:16px;border-radius:50%;display:block}
.gr1{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;column-gap:26px}
.mr1{display:flex;align-items:center;gap:12px;border-top:1.5px solid #efe3cf}
.mr1 b{width:48px;font:700 20px Lora}
.ds1{display:flex;gap:8px}
.ds1 i{width:46px;height:46px;border-radius:50%;font:700 16px/46px 'Open Sans';font-style:normal;text-align:center;display:block}
.bk{background:#1c2541;color:#f3e7d3}.hd{background:#e8a3a0;color:#1c2541}.op{background:#fff;color:#1c2541;box-shadow:inset 0 0 0 2px #c9bba3}
.ds1 i.me{box-shadow:0 0 0 4px #b4545a;background:#fff}
.nt1{display:flex;align-items:center;gap:10px;background:#1c2541;color:#f3e7d3;border-radius:14px;padding:13px 16px;font:500 18px 'Open Sans'}""")

spaces = [("Garden lawn", "Up to 200 guests · outdoor", "Open on June 12", "op"), ("Ballroom", "Up to 150 guests · indoor", "On hold until Friday", "hd"), ("Rooftop terrace", "Up to 80 guests · views", "Booked", "bk")]
P["p136_ev_s2"] = ev(2, "<div class=kt><b>1</b>SPACES</div><h1>Every space and its status<br><span>for the date they pick.</span></h1>",
browser(f'''<div class=w2><div class=t2><div><span class=lb>SAMPLE VENUE</span><b>Saturday, June 12, 2027</b></div><em>Change date</em></div>
{"".join(f'<div class="sp2 {k}"><div class=im2><svg viewBox="0 0 160 100" width="100%" height="100%" preserveAspectRatio="xMidYMid slice"><rect width="160" height="100" fill="{bg}"/>{deco}</svg></div><div class=tx2><b>{a}</b><span>{b}</span></div><em>{s}</em></div>' for (a,b,s,k),(bg,deco) in zip(spaces,[("#cfe3c4",'<circle cx="40" cy="40" r="22" fill="#7fae6c"/><circle cx="120" cy="34" r="26" fill="#7fae6c"/><rect y="70" width="160" height="30" fill="#9cc58a"/>'),("#f3d9c9",'<path d="M20 20 H140 V100 H20 Z" fill="#e8c2ae"/><circle cx="80" cy="30" r="12" fill="#ffe7a6"/>'),("#c9d6ea",'<rect y="60" width="160" height="40" fill="#8ea2c4"/><rect x="20" y="50" width="120" height="6" fill="#1c2541"/>')]))}
<div class=bt2>Book a tour for the garden lawn</div></div>''', "yourvenue.com/dates", "flex:1"),
""".vis{flex-direction:column}
.w2{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:14px;background:#fffaf1}
.t2{display:flex;justify-content:space-between;align-items:flex-end}.t2 b{display:block;font:700 32px/1.25 Lora}
.t2 em{font-style:normal;font:600 16px 'Open Sans';border:1.5px solid #c9bba3;border-radius:12px;padding:8px 14px}
.sp2{flex:1;display:flex;align-items:center;gap:18px;background:#fff;border-radius:18px;padding:12px;border:1.5px solid #efe3cf}
.im2{width:210px;align-self:stretch;flex:none;border-radius:12px;overflow:hidden;position:relative}.im2 svg{position:absolute;inset:0}
.tx2{flex:1}.tx2 b{display:block;font:700 28px/1.25 Lora}.tx2 span{font:500 18px 'Open Sans';color:#6e6a62}
.sp2>em{font-style:normal;font:700 17px 'Open Sans';padding:9px 14px;border-radius:12px;margin-right:8px}
.sp2.bk>em{background:#1c2541;color:#f3e7d3}.sp2.hd>em{background:#e8a3a0;color:#1c2541}.sp2.op>em{background:#dcefd6;color:#2d6b39}
.sp2.bk .im2,.sp2.bk .tx2{opacity:.5}
.bt2{background:#b4545a;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 19px 'Open Sans'}""")

tours = [("Tue", [("5:30 PM", "Sample couple A", "bk")]), ("Wed", [("12:00 PM", "Open", "op"), ("5:30 PM", "Sample couple B", "bk")]), ("Thu", [("5:30 PM", "Open", "op")]),
         ("Sat", [("10:00 AM", "Sample couple C", "bk"), ("11:30 AM", "Sample couple D · June 12", "me")]), ("Sun", [("1:00 PM", "Open", "op")])]
P["p136_ev_s3"] = ev(3, "<div class=kt><b>2</b>TOURS</div><h1>Couples book a tour slot<br><span>without a phone call.</span></h1>",
f'''<div class="cd w3"><div class=t3><span class=lb>TOUR SLOTS · THIS WEEK · SAMPLE</span><span class=lb>30 MIN EACH</span></div>
{"".join(f'<div class=d3><b>{d}</b><div class=bb3>' + "".join(f'<div class="j3 {k}"><i>{t}</i><span>{w}</span></div>' for t,w,k in js) + '</div></div>' for d,js in tours)}
<div class=nt3>{ic("bell",22)}<span>Reminder text the day before. Tour notes saved on the couple's file.</span></div></div>''',
""".w3{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.t3{display:flex;justify-content:space-between}
.d3{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px solid #efe3cf}
.d3>b{width:64px;flex:none;font:700 28px Lora}
.bb3{flex:1;display:flex;gap:12px}
.j3{flex:1;display:flex;flex-direction:column;gap:2px;border-radius:14px;padding:12px 16px}
.j3 i{font-style:normal;font:700 15px 'Open Sans';opacity:.8}.j3 span{font:600 20px/1.3 'Open Sans'}
.j3.bk{background:#1c2541;color:#f3e7d3}.j3.op{background:#fff;box-shadow:inset 0 0 0 2px #c9bba3;color:#6e6a62}.j3.me{background:#e8a3a0}
.nt3{display:flex;align-items:center;gap:10px;background:#1c2541;color:#f3e7d3;border-radius:14px;padding:13px 16px;font:500 18px 'Open Sans'}""")

run = [("12:00 PM", "Florist and decor team arrive", "Garden lawn"), ("2:00 PM", "Caterer setup · tables and linens", "Kitchen + lawn"), ("4:30 PM", "Ceremony", "Garden lawn"),
       ("5:30 PM", "Guests move to dinner", "Garden tent"), ("8:00 PM", "Music and first dance", "Dance floor"), ("10:30 PM", "Last song · vendors pack up", "All areas")]
P["p136_ev_s4"] = ev(4, "<div class=kt><b>3</b>EVENT DAY</div><h1>One run sheet for staff,<br><span>vendors and the couple.</span></h1>",
f'''<div class=w4><div class="cd rs4"><span class=lb>RUN SHEET · SAT JUNE 12 · SAMPLE</span>
{"".join(f'<div class=r4><em>{t}</em><i></i><div><b>{a}</b><span>{p}</span></div></div>' for t,a,p in run)}</div>
<div class=sd4>{"".join(f'<div class="cd v4"><span class=lb>{a}</span><b>{b}</b><small>{c}</small></div>' for a,b,c in [("VENDORS","6 confirmed","Arrival times sent"),("GUESTS","180 expected","Final count due May 29"),("FLOOR PLAN","Shared","Tables, stage, dance floor")])}</div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.rs4{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:4px}
.r4{flex:1;display:flex;align-items:center;gap:16px;position:relative}
.r4 em{font-style:normal;width:96px;flex:none;font:700 18px 'Open Sans';color:#b4545a}
.r4 i{width:16px;height:16px;border-radius:50%;background:#1c2541;flex:none;box-shadow:0 0 0 5px #f3e7d3}
.r4 b{display:block;font:700 22px/1.3 Lora}.r4 span{font:500 16px 'Open Sans';color:#6e6a62}
.sd4{width:300px;flex:none;display:flex;flex-direction:column;gap:16px}
.v4{flex:1;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.v4 b{font:700 32px/1.3 Lora}.v4 small{font:500 18px 'Open Sans';color:#6e6a62}""")

P["p136_ev_s5"] = ev(5, "<h1>Run an event venue?<br><span>Let's build your dates,<br>tours and run sheets.</span></h1>",
f'''<div class=w5><div class=dt5>{"".join(f'<i class="{s}"></i>' for m in (5,6,7,8,9,10) for _,s in sat[m])}</div>
<div class=g5>{"".join(f'<div class="cd t5"><b>{a}</b><span>{b}</span></div>' for a,b in [("Saturday calendar","Booked, on hold, open"),("Spaces by date","Status for each space"),("Tour booking","Slots and reminders"),("Run sheets","For staff and vendors")])}</div></div>''',
""".w5{flex:1;display:flex;flex-direction:column;gap:18px}
.dt5{flex:none;background:#1c2541;border-radius:30px;padding:28px;display:grid;grid-template-columns:repeat(9,1fr);gap:14px;justify-items:center}
.dt5 i{width:58px;height:58px;border-radius:50%;display:block}
.dt5 .op{box-shadow:none;background:#f3e7d3}.dt5 .bk{background:#3a4670}.dt5 .hd{background:#e8a3a0}
.g5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.t5{padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:8px solid #e8a3a0}
.t5 b{font:700 36px/1.25 Lora}.t5 span{font:500 22px 'Open Sans';color:#6e6a62}""",
cta="Run a venue? DM us", ctacss="background:#b4545a;color:#fff")

# ───────── 138 INDIA · Security guard staffing agency · CAROUSEL 5 · TeX Gyre Adventor + Source Sans 3 · olive / brass / off-white
# New techniques: site tile matrix with post dots (covered / missing), roster table, QR checkpoint patrol rail.
SG = """
body{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:#f4f1e6;color:#1e2414}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#5d6f2c}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Source Sans 3';letter-spacing:3px;color:#1e2414}
.kt b{width:44px;height:44px;border-radius:10px;background:#c9a24a;color:#1e2414;font:700 22px/1 'TeX Gyre Adventor';display:flex;align-items:center;justify-content:center}
.kt + h1{margin-top:16px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(30,36,20,.08)}
.lb{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#8d917f}
"""
def sg(n, head, vis, css="", cta="Swipe", ctacss="background:#1e2414;color:#c9a24a"):
    return page(SG + css, head, vis, "#1e2414", cta, ctacss, tagline=f"{n} / 5")
sites = [("Site 1", "Sample Society A", 6, []), ("Site 2", "Sample Office Park", 4, []), ("Site 3", "Sample Factory", 5, []), ("Site 4", "Sample Mall", 6, []),
         ("Site 5", "Sample Society B", 3, []), ("Site 6", "Sample Hospital gate", 4, []), ("Site 7", "Sample Warehouse", 4, [2]), ("Site 8", "Sample School gate", 2, []),
         ("Site 9", "Sample Bank", 2, []), ("Site 10", "Sample Hotel", 4, []), ("Site 11", "Sample Society C", 4, [1]), ("Site 12", "Sample Showroom", 4, [])]
sites[5] = ("Site 6", "Sample IT office", 4, []); sites[7] = ("Site 8", "Sample Godown", 2, [])
P["p138_sg_s1"] = sg(1, "<h1>12 sites, 48 guards.<br><span>Who is at post<br>right now?</span></h1>",
f'''<div class=w1><div class=gr1>{"".join(f'<div class="cd st1{" al" if miss else ""}"><span>{a}</span><b>{b}</b><small class=ps1>{n-len(miss)} of {n} posts covered</small><div class=dt1>' + "".join(f'<i class="{"x" if j+1 in miss else ""}"></i>' for j in range(n)) + '</div></div>' for a,b,n,miss in sites)}</div>
<div class=sm1><div><b>46 of 48</b><span>posts covered · day shift</span></div><div class=al1><b>2 alerts</b><span>Site 7 post 2 · Site 11 post 1</span></div></div></div>''',
""".w1{flex:1;display:flex;flex-direction:column;gap:16px}
.gr1{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:12px}
.st1{padding:14px 16px;display:flex;flex-direction:column;gap:4px}
.st1 span{font:700 15px 'Source Sans 3';letter-spacing:2px;color:#8d917f}.st1 b{font:700 22px/1.25 'Source Sans 3'}
.st1.al{box-shadow:inset 0 0 0 3px #b23a2b}.ps1{font:500 16px 'Source Sans 3';color:#5b6150}.st1.al .ps1{color:#b23a2b;font-weight:700}
.dt1{margin-top:auto;display:flex;gap:6px;flex-wrap:wrap}.dt1 i{width:25px;height:25px;border-radius:50%;background:#5d6f2c;display:block}.dt1 i.x{background:#b23a2b}
.sm1{flex:none;display:flex;gap:16px}
.sm1 div{flex:1;border-radius:20px;padding:16px 20px;background:#1e2414;color:#f4f1e6;display:flex;flex-direction:column;gap:2px}
.sm1 b{font:700 36px/1.3 'TeX Gyre Adventor';color:#c9a24a}.sm1 span{font:500 18px 'Source Sans 3';color:#cfd2c2}
.sm1 .al1{background:#b23a2b}.sm1 .al1 b{color:#fff}.sm1 .al1 span{color:#ffd9d2}""")

ros = [("Site 1 · Sample Society A", 6, 4, "Guard 3 on leave · Guard 14 covers"), ("Site 3 · Sample Factory", 5, 3, "—"), ("Site 4 · Sample Mall", 6, 4, "—"),
       ("Site 7 · Sample Warehouse", 4, 2, "Post 2 not checked in"), ("Site 11 · Sample Society C", 4, 2, "Post 1 late by 20 min")]
P["p138_sg_s2"] = sg(2, "<div class=kt><b>1</b>ROSTER</div><h1>Day and night shifts<br><span>for every site, in one table.</span></h1>",
f'''<div class="cd w2"><div class="r2 h2"><span class=lb>SITE · SAMPLE</span><span class=lb>DAY</span><span class=lb>NIGHT</span><span class=lb>NOTE TODAY</span></div>
{"".join(f'<div class="r2{" a2" if "not" in nt or "late" in nt else ""}"><b>{a}</b><em>{d}</em><em>{n}</em><span>{nt}</span></div>' for a,d,n,nt in ros)}
<div class=nt2>{ic("users",22)}<span>Leave marked in the app → the roster shows who covers, before the shift starts.</span></div></div>''',
""".w2{flex:1;padding:18px 24px 22px;display:flex;flex-direction:column}
.r2{flex:1;display:grid;grid-template-columns:1.5fr 90px 90px 1.3fr;align-items:center;gap:12px;border-top:1.5px solid #ebe7da}
.h2{flex:none;border-top:0;padding-bottom:10px}
.r2 b{font:700 21px/1.3 'Source Sans 3'}.r2 em{font-style:normal;font:700 30px 'TeX Gyre Adventor';text-align:left}.r2 span{font:500 18px/1.35 'Source Sans 3';color:#5b6150}
.a2 span{color:#b23a2b;font-weight:700}
.nt2{flex:none;display:flex;align-items:center;gap:10px;background:#1e2414;color:#f4f1e6;border-radius:14px;padding:13px 16px;font:500 18px 'Source Sans 3';margin-top:10px}""")

P["p138_sg_s3"] = sg(3, "<div class=kt><b>2</b>CHECK-IN AT POST</div><h1>Guards check in at the post,<br><span>not on a paper register.</span></h1>",
f'''<div class=w3>{phone(f"""<div class=ap3><span class=lb>SITE 4 · POST 3 · SAMPLE</span><b class=h3>Day shift check-in</b>
<div class=ph3><svg viewBox="0 0 100 100" width="120"><circle cx="50" cy="38" r="20" fill="#cfd2c2"/><path d="M14 96 Q14 62 50 62 Q86 62 86 96 Z" fill="#cfd2c2"/></svg><span>Photo taken at post</span></div>
{"".join(f'<div class=ck3><i>{ic("check",16,"#fff",3)}</i><span>{a}</span><b>{b}</b></div>' for a,b in [("Location","Inside site area"),("Time","7:56 AM"),("Uniform","Yes")])}
<div class=bt3>Checked in</div></div>""", w=350, h=720)}
<div class=sd3>{"".join(f'<div class="cd c3 {k}"><span class=lb>{a}</span><b>{b}</b><small>{c}</small></div>' for a,b,c,k in [("ON TIME","46 guards","checked in before 8:00 AM",""),("ALERT TO SUPERVISOR","Site 11 · post 1","late by 20 min","al3"),("ALERT TO SUPERVISOR","Site 7 · post 2","no check-in yet","al3")])}</div></div>''',
""".w3{flex:1;display:flex;gap:26px;align-items:center}
.ap3{flex:1;padding:8px 18px 18px;display:flex;flex-direction:column;gap:10px;background:#f7f6f0}
.h3{font:700 22px/1.3 'TeX Gyre Adventor'}
.ph3{flex:1;border-radius:16px;background:#e4e6da;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;font:600 15px 'Source Sans 3';color:#5b6150}
.ck3{display:flex;align-items:center;gap:10px;background:#fff;border-radius:12px;padding:10px 12px;font:500 16px 'Source Sans 3'}
.ck3 i{width:24px;height:24px;border-radius:7px;background:#5d6f2c;display:flex;align-items:center;justify-content:center;flex:none}.ck3 span{color:#5b6150}.ck3 b{margin-left:auto;font-weight:700}
.bt3{background:#1e2414;color:#c9a24a;border-radius:12px;padding:12px;text-align:center;font:700 17px 'Source Sans 3'}
.sd3{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:16px;justify-content:center}
.c3{flex:1;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.c3 b{font:700 32px/1.3 'TeX Gyre Adventor'}.c3 small{font:500 19px 'Source Sans 3';color:#5b6150}
.c3.al3{box-shadow:inset 0 0 0 3px #b23a2b}.c3.al3 b{color:#b23a2b}""")

def qr(seed):
    r = random.Random(seed); n = 13
    fz = lambda x, y: any(x0 <= x < x0 + 4 and y0 <= y < y0 + 4 for x0, y0 in ((0, 0), (9, 0), (0, 9)))
    cells = "".join(f'<rect x="{x}" y="{y}" width="1" height="1"/>' for x in range(n) for y in range(n) if not fz(x, y) and r.random() < .5)
    fnd = "".join(f'<rect x="{a}" y="{b}" width="4" height="4" fill="none" stroke="#1e2414" stroke-width=".8"/><rect x="{a+1.3}" y="{b+1.3}" width="1.4" height="1.4"/>' for a, b in ((0.4, 0.4), (8.6, 0.4), (0.4, 8.6)))
    return f'<svg viewBox="0 0 13 13" width="118" height="118" shape-rendering="crispEdges" fill="#1e2414">{cells}{fnd}</svg>'
pts = [("Main gate", "10:02 PM", "ok"), ("Parking", "10:09 PM", "ok"), ("Back gate", "10:15 PM", "ok"), ("Pump room", "—", "ms"), ("Terrace", "10:31 PM", "ok")]
P["p138_sg_s4"] = sg(4, "<div class=kt><b>3</b>NIGHT ROUNDS</div><h1>Every round scanned<br><span>at each checkpoint.</span></h1>",
f'''<div class="cd w4"><div class=t4><div><span class=lb>SITE 1 · SAMPLE SOCIETY A · NIGHT</span><b>Round 1 · Guard 7</b></div><em>4 of 5 scanned</em></div>
<div class=rl4>{"".join(f'<div class="p4 {k}"><div class=q4>' + qr(i) + f'</div><b>{a}</b><span>{t}</span></div>' for i,(a,t,k) in enumerate(pts))}</div>
<div class=ms4>{ic("bell",22)}<span>Pump room not scanned in round 1 → supervisor told at 10:40 PM.</span></div>
<div class=rr4>{"".join(f'<div><span class=lb>ROUND {r}</span><b>{s}</b></div>' for r,s in [(1,"4 of 5"),(2,"5 of 5"),(3,"5 of 5"),(4,"Due 4:00 AM")])}</div></div>''',
""".w4{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:16px}
.t4{display:flex;justify-content:space-between;align-items:center}.t4 b{display:block;font:700 30px/1.3 'TeX Gyre Adventor'}
.t4 em{font-style:normal;font:700 18px 'Source Sans 3';background:#fbe6c2;color:#7a5200;border-radius:12px;padding:9px 14px}
.rl4{flex:1;display:flex;gap:12px;position:relative}
.p4{flex:1;border-radius:20px;background:#f4f1e6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:14px 8px;border:3px solid #5d6f2c}
.p4.ms{border-color:#b23a2b;border-style:dashed;background:#fff4f1}.p4.ms .q4{opacity:.3}
.q4{background:#fff;padding:8px;border-radius:10px}
.p4 b{font:700 22px/1.25 'Source Sans 3';text-align:center}.p4 span{font:600 18px 'Source Sans 3';color:#5b6150}.p4.ms span{color:#b23a2b}
.ms4{display:flex;align-items:center;gap:10px;background:#b23a2b;color:#fff;border-radius:14px;padding:13px 16px;font:600 18px 'Source Sans 3'}
.rr4{display:flex;gap:12px}.rr4 div{flex:1;background:#f4f1e6;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}.rr4 b{font:700 20px 'Source Sans 3'}""")

P["p138_sg_s5"] = sg(5, "<h1>Run a security or<br>staffing agency?<br><span>Let's build your guard<br>and site app.</span></h1>",
f'''<div class=w5><div class=g5>{"".join(f'<div class="cd t5"><i>{ic(a,46,"#5d6f2c")}</i><b>{b}</b><span>{c}</span></div>' for a,b,c in [("grid","Site board","Posts covered right now"),("users","Roster","Day, night and leave cover"),("pin","Check-in at post","Photo, place and time"),("qr","Patrol rounds","Checkpoint scans + alerts")])}</div>
<div class=rp5><span class=lb>MONTHLY CLIENT REPORT · SAMPLE</span><b>Sample Society A · November</b><span class=tx5>Shifts covered, rounds done and alerts, sent as a PDF.</span></div></div>''',
""".w5{flex:1;display:flex;flex-direction:column;gap:16px}
.g5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.t5{padding:22px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.t5 b{font:700 34px/1.3 'TeX Gyre Adventor'}.t5 span{font:500 22px 'Source Sans 3';color:#5b6150}
.rp5{flex:none;background:#1e2414;color:#f4f1e6;border-radius:22px;padding:18px 22px;display:flex;flex-direction:column;gap:4px}
.rp5 b{font:700 26px/1.3 'TeX Gyre Adventor';color:#c9a24a}.tx5{font:500 18px 'Source Sans 3';color:#cfd2c2}""",
cta="Run a security agency? DM us", ctacss="background:#c9a24a;color:#1e2414")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
