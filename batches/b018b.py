import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 107 USA · Wedding planner · CAROUSEL 5 · Gelasio + DM Sans · dusty rose / olive / ivory
# New techniques: conic countdown ring in a couple portal, month-band checklist, vendor status grid, day-of run sheet on a time rail.
WD = """
body{--f:'DM Sans';--h:'Gelasio';background:#fbf6ee;color:#2e2a22}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#b56a6a;font-style:italic}
.sub{color:#6e675b}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 15px 'DM Sans';letter-spacing:3px;color:#5b6236}
.kt b{width:44px;height:44px;border-radius:50%;border:2px solid #5b6236;font:700 22px/1 Gelasio;display:flex;align-items:center;justify-content:center}
.cd{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(46,42,34,.07)}
.lb{font:700 13px 'DM Sans';letter-spacing:3px;color:#9a9283}
"""
def wd(n, head, vis, css="", cta="Swipe", ctacss="background:#5b6236;color:#fbf6ee"):
    return page(WD + css, head, vis, "#2e2a22", cta, ctacss, tagline=f"{n} / 5")
tiles = [("Checklist", "18 of 30 done", 60), ("Vendors", "6 of 9 booked", 67), ("RSVPs", "84 of 120 back", 70), ("Payments", "2 due this month", 0)]
P["p107_wedding_s1"] = wd(1, """<h1>Wedding details in<br>40 text threads?<br><span>Give each couple one<br>planning portal.</span></h1>""",
browser(f'''<div class=po1><div class=hd1><div><span class=lb>COUPLE PORTAL · SAMPLE</span><b>Sample Couple</b><em>Saturday, June 12, 2027 · Sample Venue</em></div>
<div class=rg1><i></i><div><b>202</b><span>days to go</span></div></div></div>
<div class=tl1>{"".join(f'<div class=t1><span class=lb>{a.upper()}</span><b>{b}</b>' + (f'<u><s style="width:{p}%"></s></u>' if p else '<u class=n1>Next: florist on Dec 1</u>') + '</div>' for a,b,p in tiles)}</div>
<div class=ms1><b>New from your planner</b><span>Two cake tasting dates are open. Pick one in the portal.</span></div></div>''', "portal.yourplanning.com · sample", "flex:1", bar="#f1e9dc"),
""".vis{flex-direction:column}
.po1{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:16px;background:#fffdf9}
.hd1{display:flex;justify-content:space-between;align-items:center;gap:20px}.hd1>div:first-child{display:flex;flex-direction:column;gap:6px}
.hd1 b{font:700 40px/1.2 Gelasio}.hd1 em{font-style:normal;font:500 19px 'DM Sans';color:#6e675b}
.rg1{width:190px;height:190px;flex:none;border-radius:50%;background:conic-gradient(#b56a6a 0 45%,#f1e3dd 45% 100%);display:flex;align-items:center;justify-content:center;position:relative}
.rg1 i{position:absolute;inset:18px;border-radius:50%;background:#fffdf9}
.rg1 div{position:relative;display:flex;flex-direction:column;align-items:center}.rg1 b{font:700 54px/1.35 Gelasio;margin-bottom:4px}.rg1 span{font:600 16px 'DM Sans';color:#6e675b}
.tl1{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.t1{background:#f6efe4;border-radius:18px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.t1 b{font:700 30px/1.25 Gelasio}
.t1 u{display:block;height:12px;border-radius:6px;background:#e7dccb;position:relative;overflow:hidden;text-decoration:none}.t1 u s{position:absolute;left:0;top:0;bottom:0;background:#5b6236;border-radius:6px}
.t1 u.n1{height:auto;background:none;font:600 18px 'DM Sans';color:#b56a6a;overflow:visible}
.ms1{background:#5b6236;color:#fbf6ee;border-radius:16px;padding:14px 18px;display:flex;flex-direction:column;gap:4px}.ms1 b{font:700 20px 'DM Sans'}.ms1 span{font:500 19px 'DM Sans';color:#dfe2cc}
""")

bands = [("9 months out", [("Book venue", 1), ("Pick photographer", 1), ("Save-the-date list", 1)]),
         ("6 months out", [("Book caterer", 1), ("Book florist", 0), ("Send save-the-dates", 1)]),
         ("3 months out", [("Cake tasting", 0), ("Send invitations", 0), ("Plan seating", 0)])]
P["p107_wedding_s2"] = wd(2, """<div class=kt><b>1</b>CHECKLIST</div><h1 style="margin-top:18px">Every task, by month,<br><span>ticked off together.</span></h1>""",
f'''<div class=bd2>{"".join(f'<div class="cd b2"><div class=bh2><b>{t}</b><span class=lb>{sum(d for _,d in its)} OF {len(its)} DONE</span></div><div class=bl2>' + "".join(f'<div class="i2 {"dn" if d else ""}"><em>{"✓" if d else ""}</em>{x}</div>' for x,d in its) + '</div></div>' for t,its in bands)}</div>
<div class=nt2>The couple sees the same list. When they tick a task, you see it too. Sample tasks.</div>''',
""".vis{flex-direction:column;gap:14px}
.bd2{flex:1;display:flex;flex-direction:column;gap:14px}
.b2{flex:1;display:flex;gap:18px;padding:16px 20px;align-items:stretch;border-left:12px solid #c98b8b}
.bh2{width:210px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:8px}.bh2 b{font:700 30px/1.2 Gelasio}
.bl2{flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:8px}
.i2{flex:1;display:flex;align-items:center;gap:14px;background:#f6efe4;border-radius:12px;padding:0 16px;font:600 22px 'DM Sans'}
.i2 em{width:30px;height:30px;border-radius:8px;border:2.5px solid #b7ab97;font-style:normal;font:700 18px/1 'DM Sans';display:flex;align-items:center;justify-content:center;flex:none}
.i2.dn{color:#8b8474;text-decoration:line-through}.i2.dn em{background:#5b6236;border-color:#5b6236;color:#fff}
.nt2{flex:none;background:#c98b8b;color:#fff;border-radius:18px;padding:16px 22px;font:600 21px/1.4 'DM Sans'}
""")

vend = [("Venue", "Booked", "Final walk-through May 20", "ok"), ("Caterer", "Booked", "Menu tasting Feb 6", "ok"), ("Photographer", "Booked", "Shot list due May 1", "ok"),
        ("Florist", "Contract sent", "Waiting for signature", "md"), ("DJ", "Booked", "Song list due May 15", "ok"), ("Cake", "Pick one", "2 tasting dates open", "no"),
        ("Rentals", "Booked", "Chairs and tables", "ok"), ("Hair and makeup", "Contract sent", "Trial date to set", "md"), ("Transport", "Pick one", "3 quotes to compare", "no")]
P["p107_wedding_s3"] = wd(3, """<div class=kt><b>2</b>VENDORS</div><h1 style="margin-top:18px">Nine vendors,<br><span>one status board.</span></h1>""",
f'''<div class=vg3>{"".join(f'<div class="cd v3 {k}"><span class=lb>{a.upper()}</span><b>{b}</b><i>{c}</i></div>' for a,b,c,k in vend)}</div>
<div class=lg3><span><i class=ok></i>Booked</span><span><i class=md></i>Contract sent</span><span><i class=no></i>Still to pick</span><span class=lb>SAMPLE</span></div>''',
""".vis{flex-direction:column;gap:14px}
.vg3{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:14px}
.v3{padding:16px 18px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:10px solid #5b6236}
.v3.md{border-top-color:#d9a441}.v3.no{border-top-color:#c98b8b;background:#fbefec}
.v3 b{font:700 34px/1.25 Gelasio}.v3 i{font-style:normal;font:500 21px/1.35 'DM Sans';color:#6e675b}.v3 .lb{font-size:14px}
.lg3{flex:none;display:flex;gap:22px;align-items:center;font:600 18px 'DM Sans'}.lg3 span{display:flex;align-items:center;gap:8px}.lg3 .lb{margin-left:auto}
.lg3 i{width:18px;height:18px;border-radius:5px;display:block}.lg3 i.ok{background:#5b6236}.lg3 i.md{background:#d9a441}.lg3 i.no{background:#c98b8b}
""")

run = [("12:00 pm", "Hair and makeup start", "Hair and makeup team"), ("2:30 pm", "First-look photos", "Photographer"), ("3:30 pm", "Guests arrive", "Venue team"),
       ("4:00 pm", "Ceremony", "Planner · DJ"), ("5:00 pm", "Family photos", "Photographer"), ("6:00 pm", "Dinner served", "Caterer"), ("8:00 pm", "First dance", "DJ")]
P["p107_wedding_s4"] = wd(4, """<div class=kt><b>3</b>THE DAY</div><h1 style="margin-top:18px">One run sheet<br><span>every vendor can open.</span></h1>""",
f'''<div class="cd rs4"><div class=hd4><b>Saturday, June 12 · run sheet</b><span class=lb>SAMPLE</span></div>
{"".join(f'<div class=r4><span class=tm4>{a}</span><i></i><div><b>{b}</b><em>{c}</em></div></div>' for a,b,c in run)}</div>''',
""".vis{flex-direction:column}
.rs4{flex:1;padding:20px 26px;display:flex;flex-direction:column;position:relative}
.hd4{display:flex;justify-content:space-between;align-items:center;padding-bottom:10px}.hd4 b{font:700 30px/1.25 Gelasio}
.r4{flex:1;display:flex;align-items:center;gap:20px;position:relative}
.r4:before{content:"";position:absolute;left:162px;top:0;bottom:0;width:3px;background:#eadfcd}
.tm4{width:140px;flex:none;text-align:right;font:700 24px Gelasio;color:#b56a6a}
.r4 i{width:22px;height:22px;border-radius:50%;background:#fff;border:4px solid #5b6236;flex:none;position:relative;z-index:1}
.r4 div{flex:1;display:flex;justify-content:space-between;align-items:center;gap:12px;background:#f6efe4;border-radius:14px;padding:12px 18px}
.r4 b{font:700 23px 'DM Sans'}.r4 em{font-style:normal;font:600 17px 'DM Sans';background:#fff;border-radius:8px;padding:5px 10px;color:#5b6236;white-space:nowrap}
""")

P["p107_wedding_s5"] = wd(5, """<h1>Wedding planner?<br><span>Let's build your<br>couple portal.</span></h1><div class=sub>Checklists, vendor boards and run sheets your couples and vendors can open.</div>""",
f'''<div class=c5><div class=rg5><i></i><div><b>202</b><span>days to go · sample</span></div></div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Countdown and updates","Shared checklist by month","Vendor status board","Run sheet for the day"],1))}</div></div>''',
""".c5{flex:1;background:#5b6236;color:#fbf6ee;border-radius:30px;padding:28px;display:flex;gap:28px;align-items:center}
.rg5{width:340px;height:340px;flex:none;border-radius:50%;background:conic-gradient(#c98b8b 0 45%,#7a8150 45% 100%);display:flex;align-items:center;justify-content:center;position:relative}
.rg5 i{position:absolute;inset:26px;border-radius:50%;background:#5b6236}
.rg5 div{position:relative;display:flex;flex-direction:column;align-items:center}.rg5 b{font:700 88px/1.35 Gelasio;margin-bottom:6px}.rg5 span{font:600 18px 'DM Sans';color:#dfe2cc}
.ls5{flex:1;align-self:stretch;display:flex;flex-direction:column}
.r5{flex:1;display:flex;align-items:center;gap:16px;border-top:2px solid rgba(251,246,238,.18)}.r5:first-child{border-top:none}
.r5 em{width:50px;height:50px;border-radius:50%;border:2px solid #f1d3cb;font:700 24px/1 Gelasio;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:700 28px/1.25 Gelasio}
""", cta="Wedding planner? DM us", ctacss="background:#c98b8b;color:#fff")

# ───────── 109 INDIA · Housekeeping staffing agency · CAROUSEL 6 · Archivo Black + Source Sans 3 · mint / plum / white
# New techniques: site cards with staff dot matrix (present/absent seats), printed QR poster + phone check-in list,
# relief staff suggestions, staff × day roster grid with site codes, man-days bill document.
HK = """
body{--f:'Source Sans 3';--h:'Archivo Black';background:#d6f0e3;color:#3a1736}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;letter-spacing:-1px;line-height:1.22} h1 span{color:#8a2f6f}
.sub{color:#5b4a58}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Source Sans 3';letter-spacing:3px;color:#8a2f6f}
.kt b{width:44px;height:44px;border-radius:12px;background:#3a1736;color:#d6f0e3;font:400 22px/1 'Archivo Black';display:flex;align-items:center;justify-content:center}
.cd{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(58,23,54,.08)}
.lb{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#8f8090}
"""
def hk(n, head, vis, css="", cta="Swipe", ctacss="background:#3a1736;color:#d6f0e3"):
    return page(HK + css, head, vis, "#3a1736", cta, ctacss, tagline=f"{n} / 6")
sites = [("Site A", "Office tower · 2 floors", 8, 8), ("Site B", "Shopping mall", 12, 11), ("Site C", "IT park, block 3", 6, 6), ("Site D", "Housing society", 5, 3)]
P["p109_staff_s1"] = hk(1, """<h1>Staff absent at a site,<br>and the client tells you?<br><span>See every site's<br>attendance by 9 am.</span></h1>""",
f'''<div class=sg1>{"".join(f'<div class="cd s1 {"bad" if p<n else ""}"><div class=h1r><div><b>{a}</b><span>{b}</span></div><em>{p} of {n}</em></div><div class=dt1>' + "".join(f'<i class="{"" if i<p else "ab"}"></i>' for i in range(n)) + '</div>' + (f'<div class=al1>{n-p} absent · send relief</div>' if p<n else '<div class=ok1>All present</div>') + '</div>' for a,b,n,p in sites)}</div>''',
""".sg1{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px}
.s1{padding:18px 20px;display:flex;flex-direction:column;gap:12px;border-top:10px solid #3fae7e}
.s1.bad{border-top-color:#d9534f}
.h1r{display:flex;justify-content:space-between;align-items:flex-start;gap:8px}.h1r div{display:flex;flex-direction:column;gap:2px}
.h1r b{font:400 30px/1.3 'Archivo Black'}.h1r span{font:500 18px 'Source Sans 3';color:#6d5d6b}
.h1r em{font-style:normal;font:700 20px 'Source Sans 3';background:#e7f6ee;color:#1f6e4b;padding:6px 12px;border-radius:10px;white-space:nowrap}
.bad .h1r em{background:#fbe3e2;color:#b3261e}
.dt1{flex:1;display:flex;flex-wrap:wrap;gap:10px;align-content:center}
.dt1 i{width:44px;height:44px;border-radius:50%;background:#3fae7e;display:block}
.dt1 i.ab{background:#fff;border:3px dashed #d9534f}
.al1{background:#d9534f;color:#fff;border-radius:12px;padding:10px 14px;font:700 19px 'Source Sans 3'}
.ok1{background:#e7f6ee;color:#1f6e4b;border-radius:12px;padding:10px 14px;font:700 19px 'Source Sans 3'}
""")

qr = "".join(f'<i style="background:{"#3a1736" if (x*7+y*13+x*y)%3==0 or (x<3 and y<3) or (x>8 and y<3) or (x<3 and y>8) else "#fff"}"></i>' for y in range(12) for x in range(12))
checks = [("Staff 08", "7:52 am", "ok"), ("Staff 09", "7:55 am", "ok"), ("Staff 10", "8:04 am · late", "lt"), ("Staff 05", "Not yet", "no"), ("Staff 07", "Not yet", "no")]
P["p109_staff_s2"] = hk(2, """<div class=kt><b>1</b>CHECK-IN</div><h1 style="margin-top:18px">Staff scan the QR<br><span>at the site gate.</span></h1>""",
f'''<div class=w2><div class=pst2><span class=lb>SITE D · SAMPLE</span><b>Scan to mark<br>attendance</b><div class=qr2>{qr}</div><em>Works only at this site</em></div>
{phone(f"""<div class=ch2><div class=hd2><b>Site D · today</b><span>Shift 8 am</span></div>{"".join(f'<div class="c2 {k}"><b>{a}</b><span>{t}</span></div>' for a,t,k in checks)}<div class=ft2>3 of 5 in · sample</div></div>""", w=360, h=720)}</div>''',
""".w2{flex:1;display:flex;gap:26px;align-items:center;justify-content:center}
.pst2{width:400px;align-self:stretch;flex:none;background:#fff;border-radius:22px;border:10px solid #3a1736;padding:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;text-align:center}
.pst2 b{font:400 34px/1.3 'Archivo Black'}
.qr2{width:288px;height:288px;display:grid;grid-template-columns:repeat(12,1fr);gap:0;padding:12px;background:#fff;border:3px solid #3a1736;border-radius:8px}
.qr2 i{display:block}
.pst2 em{font-style:normal;font:600 18px 'Source Sans 3';color:#6d5d6b}
.ch2{flex:1;padding:12px 16px 16px;display:flex;flex-direction:column;gap:10px;background:#f6f2f6}
.hd2{display:flex;justify-content:space-between;align-items:center;padding:4px 2px}.hd2 b{font:700 20px 'Source Sans 3'}.hd2 span{font:600 15px 'Source Sans 3';color:#8f8090}
.c2{flex:1;background:#fff;border-radius:14px;padding:0 16px;display:flex;justify-content:space-between;align-items:center;border-left:6px solid #3fae7e}
.c2 b{font:700 19px 'Source Sans 3'}.c2 span{font:700 16px 'Source Sans 3';color:#1f6e4b}
.c2.lt{border-left-color:#e0a030}.c2.lt span{color:#a86d0c}.c2.no{border-left-color:#d9534f}.c2.no span{color:#b3261e}
.ft2{text-align:center;font:600 15px 'Source Sans 3';color:#8f8090}
""")

relief = [("Relief staff 1", "2 km from Site D", "Free today", "on"), ("Relief staff 2", "5 km from Site D", "Free today", ""), ("Relief staff 3", "On leave", "Not free", "off")]
P["p109_staff_s3"] = hk(3, """<div class=kt><b>2</b>RELIEF</div><h1 style="margin-top:18px">Someone is absent?<br><span>Send relief in minutes.</span></h1>""",
f'''<div class="cd al3"><div><span class=lb>ALERT · SAMPLE</span><b>Site D · 2 absent</b><i>Staff 05 and Staff 07 not checked in by 8:30 am</i></div><em>!</em></div>
<div class=rl3>{"".join(f'<div class="cd r3 {k}"><div class=av3>{ic("users",30)}</div><div class=tx3><b>{a}</b><span>{b}</span></div><em>{c}</em>' + ('<u>Send to Site D</u>' if k=="on" else '') + '</div>' for a,b,c,k in relief)}</div>
<div class=nt3>The client gets a text: relief staff on the way. You fix it before they notice.</div>''',
""".vis{flex-direction:column;gap:14px}
.al3{flex:none;background:#3a1736;color:#fff;padding:20px 24px;display:flex;align-items:center;justify-content:space-between;gap:16px}
.al3 div{display:flex;flex-direction:column;gap:4px}.al3 .lb{color:#d6b8d0}.al3 b{font:400 32px/1.3 'Archivo Black'}.al3 i{font-style:normal;font:500 20px 'Source Sans 3';color:#e6d6e3}
.al3 em{width:70px;height:70px;border-radius:50%;background:#d9534f;font:400 40px/1 'Archivo Black';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.rl3{flex:1;display:flex;flex-direction:column;gap:12px}
.r3{flex:1;display:flex;align-items:center;gap:18px;padding:0 22px}
.av3{width:64px;height:64px;border-radius:50%;background:#d6f0e3;color:#3a1736;display:flex;align-items:center;justify-content:center;flex:none}
.tx3{flex:1;display:flex;flex-direction:column;gap:3px}.tx3 b{font:700 32px 'Source Sans 3'}.tx3 span{font:500 22px 'Source Sans 3';color:#6d5d6b}
.r3 em{font-style:normal;font:700 20px 'Source Sans 3';background:#e7f6ee;color:#1f6e4b;padding:6px 12px;border-radius:8px}
.r3 u{text-decoration:none;font:700 21px 'Source Sans 3';background:#8a2f6f;color:#fff;padding:12px 16px;border-radius:12px}
.r3.on{border:3px solid #8a2f6f}.r3.off{opacity:.55}.r3.off em{background:#f1ecf1;color:#6d5d6b}
.nt3{flex:none;background:#8a2f6f;color:#fff;border-radius:18px;padding:16px 22px;font:600 21px/1.4 'Source Sans 3'}
""")

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
ros = [("Staff 01", "AAAAAA"), ("Staff 02", "AAAAA-"), ("Staff 03", "BBBB-B"), ("Staff 04", "BBBBBB"), ("Staff 05", "DD-DDD"), ("Staff 06", "CCCCC-"), ("Staff 07", "DDDD-D"), ("Relief 1", "--R-R-")]
cc = {"A": ("#3fae7e", "#fff"), "B": ("#8a2f6f", "#fff"), "C": ("#e0a030", "#3a1736"), "D": ("#5a8bd6", "#fff"), "-": ("#f1ecf1", "#8f8090"), "R": ("#d9534f", "#fff")}
def cell(c):
    bg, fg = cc[c]; t = {"-": "Off", "R": "D"}.get(c, c)
    return f'<i style="background:{bg};color:{fg}">{t}</i>'
P["p109_staff_s4"] = hk(4, """<div class=kt><b>3</b>ROSTER</div><h1 style="margin-top:18px">Who works where,<br><span>all week.</span></h1>""",
f'''<div class="cd ro4"><div class="rw4 hd4"><span class=lb>SAMPLE</span>{"".join(f'<b>{d}</b>' for d in days)}</div>
{"".join(f'<div class=rw4><span>{n}</span>{"".join(cell(c) for c in s)}</div>' for n,s in ros)}</div>
<div class=lg4>{"".join(f'<span><i style="background:{cc[k][0]}"></i>{t}</span>' for k,t in [("A","Site A"),("B","Site B"),("C","Site C"),("D","Site D"),("R","Relief cover")])}</div>''',
""".vis{flex-direction:column;gap:14px}
.ro4{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:8px}
.rw4{flex:1;display:grid;grid-template-columns:170px repeat(6,1fr);gap:8px;align-items:stretch}
.rw4.hd4{flex:none;align-items:center}.rw4.hd4 b{font:700 18px 'Source Sans 3';text-align:center;color:#6d5d6b}
.rw4>span{font:700 22px 'Source Sans 3';display:flex;align-items:center}
.rw4 i{border-radius:10px;font:400 20px/1 'Archivo Black';font-style:normal;display:flex;align-items:center;justify-content:center}
.lg4{flex:none;display:flex;gap:18px;justify-content:center;font:600 18px 'Source Sans 3'}.lg4 span{display:flex;align-items:center;gap:8px}.lg4 i{width:18px;height:18px;border-radius:5px;display:block}
""")

bill = [("Staff 05", "Housekeeping", "24 of 26"), ("Staff 07", "Housekeeping", "25 of 26"), ("Staff 08", "Housekeeping", "26 of 26"), ("Staff 09", "Pantry", "26 of 26"), ("Staff 10", "Garden", "26 of 26"), ("Relief cover", "For absent days", "3 days")]
P["p109_staff_s5"] = hk(5, """<div class=kt><b>4</b>MONTHLY BILL</div><h1 style="margin-top:18px">Bill each site from<br><span>real attendance.</span></h1>""",
f'''<div class=w5><div class="cd dc5"><div class=t5><div><span class=lb>ATTENDANCE SHEET · SAMPLE</span><b>Site D · November</b></div><em>26 working days</em></div>
<div class="r5 hd5"><span>Staff</span><span>Role</span><span>Days</span></div>
{"".join(f'<div class=r5><b>{a}</b><span>{b}</span><em>{c}</em></div>' for a,b,c in bill)}
<div class=tt5><span>Total man-days</span><b>130 of 130</b></div></div>
<div class=sd5>{"".join(f'<div class="cd s5"><b>{a}</b><span>{b}</span></div>' for a,b in [("No disputes","The client sees the same check-ins."),("Ready on the 1st","One sheet per site, made on its own."),("Payroll too","Days per staff for salary.")])}</div></div>''',
""".w5{flex:1;display:flex;gap:18px}
.dc5{flex:1;padding:22px 24px;display:flex;flex-direction:column;border-top:12px solid #8a2f6f}
.t5{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:10px}.t5 div{display:flex;flex-direction:column;gap:4px}.t5 b{font:400 28px/1.3 'Archivo Black'}
.t5 em{font-style:normal;font:700 15px 'Source Sans 3';background:#d6f0e3;padding:6px 10px;border-radius:8px;white-space:nowrap}
.r5{flex:1;display:grid;grid-template-columns:1.1fr 1.2fr .9fr;align-items:center;border-top:1.5px dashed #e3d9e2}
.r5.hd5{flex:none;padding-bottom:6px;border-top:none;font:700 15px 'Source Sans 3';color:#8f8090}
.r5 b{font:700 24px 'Source Sans 3'}.r5 span{font:500 21px 'Source Sans 3';color:#6d5d6b}.r5 em{font-style:normal;font:700 23px 'Source Sans 3';text-align:right}
.tt5{flex:none;display:flex;justify-content:space-between;align-items:center;background:#3a1736;color:#fff;border-radius:14px;padding:14px 18px;margin-top:8px}
.tt5 span{font:600 18px 'Source Sans 3'}.tt5 b{font:400 24px 'Archivo Black'}
.sd5{width:300px;flex:none;display:flex;flex-direction:column;gap:14px}
.s5{flex:1;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}.s5 b{font:400 25px/1.3 'Archivo Black';color:#8a2f6f}.s5 span{font:500 19px/1.4 'Source Sans 3';color:#5b4a58}
""")

P["p109_staff_s6"] = hk(6, """<h1>Run a housekeeping<br>or staffing agency?<br><span>Let's build your<br>site app.</span></h1>""",
f'''<div class=c6>{"".join(f'<div class=k6><em>{i}</em><b>{t}</b><span>{d}</span></div>' for i,t,d in [(1,"QR check-in","At every site gate"),(2,"Live site board","Who is in, who is not"),(3,"Relief in minutes","Nearest free staff"),(4,"Bills from attendance","Man-days per site")])}</div>''',
""".c6{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px}
.k6{background:#3a1736;color:#fff;border-radius:26px;padding:24px;display:flex;flex-direction:column;justify-content:flex-end;gap:8px;position:relative;overflow:hidden}
.k6 em{position:absolute;right:20px;top:4px;font:400 150px/1.25 'Archivo Black';font-style:normal;color:rgba(214,240,227,.14)}
.k6 b{font:400 30px/1.3 'Archivo Black';position:relative}.k6 span{font:500 21px 'Source Sans 3';color:#d6b8d0;position:relative}
.k6:nth-child(2),.k6:nth-child(3){background:#8a2f6f}
""", cta="Staffing agency? DM us", ctacss="background:#8a2f6f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
