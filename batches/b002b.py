import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 28 CANADA · Snow removal company · CAROUSEL 5 · Inter Display + Inter · ice white / midnight / signal red
# New technique: CSS snowfall dots + big outlined numbers.
SN = """
body{--f:'Inter';--h:'Inter Display';background:linear-gradient(180deg,#0d1b2e 0%,#18304f 100%);color:#fff}
.snow{position:absolute;inset:0;background-image:radial-gradient(circle,rgba(255,255,255,.55) 2px,transparent 2.5px),radial-gradient(circle,rgba(255,255,255,.3) 1.5px,transparent 2px);background-size:90px 90px,53px 53px;background-position:0 0,20px 31px}
.ground{position:absolute;left:0;right:0;bottom:0;height:150px;background:#eef4fb;border-radius:60% 40% 0 0/40px 30px 0 0}
h1{font-size:66px;font-weight:800;letter-spacing:-2px} h1 span{color:#ff5a4e}
.sub{color:#b8c7dd}
.sn{font:700 17px 'Inter';letter-spacing:3px;color:#8fd3ff;margin-top:22px}
.card{background:#fff;color:#0d1b2e;border-radius:24px;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.big{font:900 140px/1.2 'Inter Display';color:transparent;-webkit-text-stroke:3px #8fd3ff;letter-spacing:-6px}
"""
def sslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#ff5a4e;color:#fff", ft="#0d1b2e"):
    return page(SN+css, f"<div class=sn>{kick}</div><h1 style='margin-top:10px'>{title}</h1><div class=sub>{sub}</div>", vis, "#fff", cta, ctacss,
                bg="<div class=snow></div><div class=ground></div>", tagline=f"{n} / 5", logo_color=ft)

P["p28_snow_s1"] = sslide(1, "SNOW REMOVAL BUSINESSES", "Storm at 3 AM.<br><span>Who goes where?</span>",
 "What good software does for a snow removal company after a big snowfall.",
 f'''<div class=st>{"".join(f'<div class=r><span class=big>{n}</span><div><b>{a}</b><small>{b}</small></div></div>' for n,a,b in [("1","Routes ready","Every crew knows its list."),("2","Customers told","A text when the driveway is done."),("3","Billing sorted","Seasonal or per visit, no spreadsheets.")])}</div>''',
 """.vis{margin-bottom:120px}.st{display:flex;flex-direction:column;gap:16px;width:100%}.st .r{flex:1}
.r{display:flex;align-items:center;gap:30px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:26px;padding:6px 30px}
.r b{display:block;font:800 40px/1.25 'Inter Display';letter-spacing:-.5px}.r small{display:block;font:400 23px 'Inter';color:#b8c7dd;margin-top:4px}""")

stops = [("1", "Sample St, house 12", "Driveway + walkway", "Done 4:10 AM", "d"), ("2", "Sample St, house 18", "Driveway", "Done 4:25 AM", "d"),
         ("3", "Maple Crescent, 4", "Driveway + salt", "Now", "n"), ("4", "Maple Crescent, 9", "Walkway only", "Next", ""),
         ("5", "Lakeview Rd, 22", "Commercial lot", "Next", ""), ("6", "Lakeview Rd, 31", "Driveway", "Next", "")]
srows = "".join(f'<div class="sr {c}"><span class=no>{a}</span><div style="flex:1"><b>{b}</b><small>{d}</small></div><i>{e}</i></div>' for a, b, d, e, c in stops)
P["p28_snow_s2"] = sslide(2, "1 · ROUTES", "Each crew gets<br><span>its own list.</span>",
 "Sorted in driving order. Done stops tick off in real time.",
 f'''<div class="card L"><div class=th><b>Crew B · tonight</b><span>SAMPLE</span></div>{srows}</div>
 <div class=R><div class=map><i class=rd style="top:22%;left:0;right:0"></i><i class=rd style="top:60%;left:0;right:0"></i><i class=rd2 style="left:35%;top:0;bottom:0"></i><i class=rd2 style="left:72%;top:0;bottom:0"></i>
 {"".join(f'<span class="pin {c}" style="left:{x}%;top:{y}%">{n}</span>' for n,x,y,c in [("1",14,12,"d"),("2",28,30,"d"),("3",44,52,"n"),("4",60,68,""),("5",78,40,""),("6",88,80,"")])}</div>
 <div class=pr><b>2 of 6</b><span>stops done · sample</span></div></div>''',
 """.vis{gap:20px;align-items:stretch;margin-bottom:100px}
.L{flex:1.25;padding:22px;display:flex;flex-direction:column;gap:9px;min-width:0}
.th{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}.th b{font:800 24px 'Inter Display'}.th span{font:700 13px Inter;letter-spacing:2px;color:#7a8aa3}
.sr{flex:1;display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:#f1f5fb}
.sr b{display:block;font:700 19px Inter}.sr small{display:block;font:500 15px Inter;color:#6a7a93}
.sr .no{width:36px;height:36px;border-radius:50%;background:#d7e2f1;font:800 15px/1 Inter;display:flex;align-items:center;justify-content:center;flex:none}
.sr i{font:700 14px Inter;font-style:normal;color:#6a7a93;white-space:nowrap}
.sr.d .no{background:#2e9d62;color:#fff}.sr.d i{color:#2e9d62}.sr.n{background:#fff0ee;box-shadow:inset 0 0 0 2px #ff5a4e}.sr.n .no{background:#ff5a4e;color:#fff}.sr.n i{color:#ff5a4e}
.R{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.map{flex:1;background:#eef4fb;border-radius:24px;position:relative;overflow:hidden}
.rd{position:absolute;height:14px;background:#fff}.rd2{position:absolute;width:14px;background:#fff}
.pin{position:absolute;width:44px;height:44px;margin:-22px 0 0 -22px;border-radius:50%;background:#7a8aa3;color:#fff;font:800 18px/1 Inter;display:flex;align-items:center;justify-content:center;border:3px solid #fff}
.pin.d{background:#2e9d62}.pin.n{background:#ff5a4e}
.pr{background:#ff5a4e;border-radius:22px;padding:18px 22px}.pr b{display:block;font:800 36px 'Inter Display'}.pr span{font:500 18px Inter}""")

P["p28_snow_s3"] = sslide(3, "2 · CUSTOMERS", "A text the moment<br><span>the driveway is clear.</span>",
 "No more \"Did you come yet?\" calls at 7 AM.",
 f'''<div class=th2><div class=msgs><div class=m1>Good morning! Your driveway at house 12 was cleared at 4:10 AM. Salt applied to the walkway.<small>Your Snow Company · sample</small></div>
 <div class=m2>Thank you! Car is out already.</div><div class=m1>Next visit: after the next 5 cm of snow, as per your plan.<small>Automatic message</small></div></div>
 <div class=side>{"".join(f'<div class=sd><span class=ib>{ic(i,26)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("camera","Photo proof","Crew snaps a photo when done."),("clock","Time stamp","Saved for every visit."),("chat","Fewer calls","Customers stop asking.")])}</div></div>''',
 """.vis{margin-bottom:110px}.th2{display:flex;gap:22px;width:100%}
.msgs{flex:1.3;background:#eef4fb;border-radius:28px;padding:26px;display:flex;flex-direction:column;gap:16px;justify-content:center;min-width:0}
.m1{background:#fff;color:#0d1b2e;border-radius:6px 22px 22px 22px;padding:22px;font:500 23px/1.45 Inter;max-width:92%}
.m1 small{display:block;font:600 14px Inter;color:#7a8aa3;margin-top:8px}
.m2{align-self:flex-end;background:#1f6feb;color:#fff;border-radius:22px 6px 22px 22px;padding:18px 22px;font:500 23px/1.4 Inter}
.side{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.sd{flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:22px;padding:20px;display:flex;flex-direction:column;justify-content:center;gap:12px}
.sd .ib{width:52px;height:52px;border-radius:16px;background:#8fd3ff;color:#0d1b2e}.sd b{display:block;font:800 23px 'Inter Display'}.sd small{display:block;font:400 18px/1.4 Inter;color:#b8c7dd;margin-top:4px}""")

plans = [("Seasonal contract", "One price for the season", "Paid in instalments", "#8fd3ff"),
         ("Per visit", "Charged after each clear", "Visits counted for you", "#ffd166"),
         ("Commercial lot", "Plowing + salting", "Monthly invoice with visit log", "#ff5a4e")]
P["p28_snow_s4"] = sslide(4, "3 · BILLING", "Seasonal or per visit,<br><span>billing sorts itself.</span>",
 "Every visit is logged, so every invoice is right.",
 f'''<div class=pl>{"".join(f'<div class=pc><i style="background:{c}"></i><b>{a}</b><span>{b}</span><small>{d}</small></div>' for a,b,d,c in plans)}</div>
 <div class="card inv"><div class=ih><b>Invoice · sample</b><span>Lakeview Rd, 22</span></div>{"".join(f'<div class=il><span>{a}</span><span>{b}</span></div>' for a,b in [("Plow visits this month","Logged: 7"),("Salt applications","Logged: 4"),("Rate","As per your contract")])}<div class=vlog><b>Visit log</b>{"".join(f'<div class=lr><span>{a}</span><span>{b}</span><span>{c}</span></div>' for a,b,c in [("Nov 3","5:10 AM","Plow + salt"),("Nov 9","4:40 AM","Plow"),("Nov 14","6:05 AM","Plow + salt"),("Nov 20","3:55 AM","Plow")])}</div><div class=it><span>Total</span><span>Calculated</span></div></div>''',
 """.vis{flex-direction:column;gap:18px;margin-bottom:110px}
.pl{display:flex;gap:14px}.pc{flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:22px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.pc i{width:40px;height:8px;border-radius:4px;margin-bottom:8px}.pc b{font:800 23px 'Inter Display'}.pc span{font:500 18px Inter;color:#dbe5f3}.pc small{font:400 16px Inter;color:#9fb0c8}
.inv{flex:1;padding:20px 26px;display:flex;flex-direction:column;gap:8px}
.ih{display:flex;justify-content:space-between;align-items:center;border-bottom:2px solid #e3eaf4;padding-bottom:12px}.ih b{font:800 25px 'Inter Display'}.ih span{font:600 17px Inter;color:#7a8aa3}
.il{display:flex;justify-content:space-between;font:500 20px Inter;padding:6px 0;border-bottom:1px dashed #e3eaf4}.il span:last-child{font-weight:700}
.vlog{flex:none;background:#f1f5fb;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}.vlog b{font:800 18px Inter;color:#7a8aa3}.lr{display:flex;font:500 21px/1.6 Inter}.lr span{flex:1}.lr span:last-child{text-align:right;font-weight:700}
.it{margin-top:auto;display:flex;justify-content:space-between;background:#0d1b2e;color:#fff;border-radius:14px;padding:16px 18px;font:800 21px Inter}""")

P["p28_snow_s5"] = sslide(5, "BUILT FOR WINTER", "Want software that<br><span>runs your snow nights?</span>",
 "Routes, customer texts and billing in one place. We build it for your crews and your area.",
 f'''<div class=w>{peep("ArmsCrossed","Smile","Beanie","GoateeCircle",w=360,h=520,fill="#ffffff")}<div class=q><b>What slows you down most after a storm?</b><div class=op>{"".join(f'<span><i>{ic(i,24)}</i>{t}</span>' for i,t in [("map","Planning routes"),("phone","Calls from customers"),("doc","Billing at month end")])}</div><span class=ct>Tell us in the comments. We read every one.</span></div></div>''',
 """.vis{align-items:flex-end;margin-bottom:6px}.w{display:flex;align-items:flex-end;gap:20px;width:100%;position:relative;z-index:3}
.op{display:flex;flex-direction:column;gap:10px;margin-top:18px}.op span{display:flex;gap:12px;align-items:center;background:#eef4fb;border-radius:16px;padding:22px 20px;font:700 24px Inter}.op i{color:#ff5a4e;display:flex}.ct{display:block;font:400 20px Inter;color:#4a5a73;margin-top:16px}
.q{flex:1;background:#fff;color:#0d1b2e;border-radius:28px;padding:32px;margin-bottom:170px;box-shadow:0 26px 50px rgba(0,0,0,.3)}
.q b{display:block;font:800 40px/1.25 'Inter Display'}""",
 cta="DM us to plan yours")

# ───────── 29 INDIA · Driving school · CAROUSEL 5 · Montserrat + Open Sans · cream / dark green / L-plate red
# New format: "Which one do you need?" guide (website vs student app vs instructor app).
DS = """
body{--f:'Open Sans';--h:'Montserrat';background:#f4f1e8;color:#1c3d2e}
h1{font-size:62px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#d62f3a}
.sub{color:#5b6b62}
.sn{display:inline-flex;align-items:center;gap:10px;font:800 17px 'Montserrat';letter-spacing:2px;color:#1c3d2e;margin-top:22px}
.lp{width:40px;height:40px;background:#fff;border:3px solid #d62f3a;border-radius:6px;display:flex;align-items:center;justify-content:center;font:900 26px 'Montserrat';color:#d62f3a}
.card{background:#fff;border-radius:24px;box-shadow:0 24px 50px rgba(28,61,46,.12)}
.who{display:flex;gap:10px;flex-wrap:wrap}.who span{font:700 17px 'Open Sans';background:#1c3d2e;color:#fff;border-radius:20px;padding:8px 16px}
.pt{display:flex;gap:16px;align-items:center;background:#fff;border-radius:20px;padding:22px 22px;font:700 22px/1.35 'Open Sans';box-shadow:0 10px 24px rgba(28,61,46,.08)}
.R .pt{flex:1;flex-direction:column;align-items:flex-start;justify-content:center}
.pt .ib{width:52px;height:52px;border-radius:14px;background:#e8f1ec;color:#1c3d2e}
"""
def dslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#1c3d2e;color:#fff"):
    return page(DS+css, f"<div class=sn><span class=lp>L</span>{kick}</div><h1 style='margin-top:12px'>{title}</h1><div class=sub>{sub}</div>", vis, "#1c3d2e", cta, ctacss, tagline=f"{n} / 5")
dpts = lambda L: "".join(f'<div class=pt><span class=ib>{ic(i,24)}</span>{t}</div>' for i, t in L)

P["p29_driving_s1"] = dslide(1, "DRIVING SCHOOLS", "Website, app or both?<br><span>Which one do you need?</span>",
 "A simple guide for driving school owners. Swipe to find yours.",
 f'''<div class=g>{"".join(f'<div class=o><span class=n>{n}</span><span class=ib>{ic(i,38)}</span><b>{a}</b><small>{b}</small><div class=gf><em>Good for</em>{"".join(f"<p>✓ {x}</p>" for x in g)}</div></div>' for n,i,a,b,g in [("A","globe","Website","For new students who search online",["Getting found","Course details","Enquiries","Photos of your cars","Map and timings"]),("B","phone","Student app","For booking lessons and seeing progress",["Lesson booking","Lessons left","Test dates","Lesson reminders","Fee status"]),("C","users","Instructor app","For your team's daily schedule",["Day plan","Pickup points","Lesson status","Car assigned","Owner overview"])])}</div>''',
 """.vis{align-items:stretch}.g{display:flex;gap:16px;width:100%}
.o{flex:1;background:#fff;border-radius:26px;padding:28px 22px;display:flex;flex-direction:column;gap:14px;box-shadow:0 24px 50px rgba(28,61,46,.12);position:relative}
.o .n{font:900 170px/1 'Montserrat';color:#e9e3d3;margin:-10px 0 -20px}.o .ib{width:72px;height:72px;border-radius:22px;background:#1c3d2e;color:#fff}
.o b{font:800 28px/1.2 'Montserrat';margin-top:6px}.gf{flex:1;margin-top:8px;background:#f6f3ea;border-radius:16px;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:12px}.gf em{font:700 14px 'Open Sans';font-style:normal;letter-spacing:2px;text-transform:uppercase;color:#d62f3a}.gf p{font:600 20px/1.35 'Open Sans'}.o small{font:500 19px/1.45 'Open Sans';color:#5b6b62}""")

P["p29_driving_s2"] = dslide(2, "A · WEBSITE", "You need a <span>website</span><br>if new students...",
 "...ask \"Where is the nearest driving school?\" and you are not on their screen.",
 browser(f'''<div class=ws><div class=hero><b>Learn to drive with confidence</b><small>Sample Driving School · your area</small><span class=bt>Book a free enquiry call</span></div>
 <div class=cs>{"".join(f'<div class=c><b>{a}</b><small>{b}</small><span class=tm>Timings and batches listed</span></div>' for a,b in [("Beginner course","Car · manual or automatic"),("Two-wheeler","Scooter and bike"),("Refresher","For licence holders")])}</div></div>''', "yourdrivingschool.in", "flex:1.3;min-width:0") +
 f'<div class=R>{dpts([("search","Shows up when people search"),("doc","Courses and timings clearly listed"),("chat","Enquiries come to you directly")])}</div>',
 """.vis{gap:20px;align-items:stretch}
.ws{flex:1;display:flex;flex-direction:column;gap:14px;padding:18px;background:#fdfcf8}
.hero{background:#1c3d2e;color:#fff;border-radius:18px;padding:26px 22px;display:flex;flex-direction:column;gap:8px}.hero b{font:800 28px/1.25 'Montserrat'}.hero small{font:500 16px 'Open Sans';color:#b6cfc2}
.hero .bt{align-self:flex-start;margin-top:10px;background:#d62f3a;color:#fff;border-radius:12px;padding:12px 16px;font:700 16px 'Open Sans'}
.cs{display:flex;flex-direction:column;gap:10px;flex:1}.c{flex:1;background:#fff;border:2px solid #ece6d6;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;justify-content:center}.c b{font:800 22px 'Montserrat'}.c .tm{margin-top:8px;align-self:flex-start;font:600 14px 'Open Sans';background:#e8f1ec;border-radius:10px;padding:5px 10px}.c small{font:500 16px 'Open Sans';color:#5b6b62}
.R{flex:1;display:flex;flex-direction:column;gap:14px;justify-content:center;min-width:0}""")

days = [("Mon", ["7 AM", "8 AM"], [1, 0]), ("Tue", ["7 AM", "6 PM"], [0, 0]), ("Wed", ["8 AM", "5 PM"], [0, 2]), ("Thu", ["7 AM", "7 PM"], [1, 1]), ("Fri", ["6 AM", "8 AM"], [0, 0])]
P["p29_driving_s3"] = dslide(3, "B · STUDENT APP", "You need a <span>student app</span><br>if students keep calling...",
 "...to fix a lesson time, ask how many classes are left, or check their test date.",
 phone(f'''<div class=sa><b class=h>Book a lesson</b><small class=s>Sample student · 9 of 20 lessons done</small><div class=bar><i></i></div>
 {"".join(f'<div class=dy><span>{d}</span>{"".join(f'<i class="{["","tk","sel"][k]}">{t}</i>' for t,k in zip(ts,ks))}</div>' for d,ts,ks in days)}
 <div class=tt><b>Licence test</b><span>Date added by your school</span></div><div class=bk>Confirm Wed, 5 PM</div></div>''', w=360, h=760) +
 f'<div class=R>{dpts([("cal","Students pick open slots"),("chart","Lessons left, always visible"),("bell","Reminder before each lesson"),("check","Test date in one place")])}</div>',
 """.vis{gap:28px;align-items:stretch;justify-content:center}
.sa{padding:8px 18px 18px;display:flex;flex-direction:column;gap:11px;flex:1;color:#1c3d2e}
.sa .h{font:800 21px 'Montserrat'}.sa .s{font:500 13px 'Open Sans';color:#5b6b62;margin-top:-6px}
.bar{height:10px;border-radius:5px;background:#ece6d6}.bar i{display:block;width:45%;height:100%;border-radius:5px;background:#1c3d2e}
.dy{display:flex;align-items:center;gap:8px;background:#f6f3ea;border-radius:14px;padding:10px}.dy span{font:700 14px 'Open Sans';width:38px}
.dy i{flex:1;font:600 13px 'Open Sans';font-style:normal;text-align:center;padding:8px 4px;border-radius:10px;background:#fff}
.dy i.tk{background:#e9e3d3;color:#a39b86;text-decoration:line-through}.dy i.sel{background:#d62f3a;color:#fff}
.tt{background:#e8f1ec;border-radius:14px;padding:12px}.tt b{display:block;font:700 15px 'Open Sans'}.tt span{font:500 13px 'Open Sans';color:#5b6b62}
.bk{margin-top:auto;background:#1c3d2e;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 15px 'Open Sans'}
.R{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}""")

sched = [("7:00 AM", "Student A", "Lesson 4 · city roads", "Done"), ("8:00 AM", "Student B", "Lesson 11 · reverse parking", "Done"),
         ("9:00 AM", "Student C", "Lesson 1 · basics", "Next"), ("5:00 PM", "Student D", "Mock test", ""), ("6:00 PM", "Student E", "Lesson 7 · highway", ""), ("7:00 PM", "Student F", "Lesson 2 · gears", "")]
P["p29_driving_s4"] = dslide(4, "C · INSTRUCTOR APP", "You need an <span>instructor app</span><br>if your team asks...",
 "...\"Who is my next student?\" Every morning, by phone.",
 f'''<div class="card L"><div class=th><b>Instructor 2 · today</b><span>SAMPLE</span></div>{"".join(f'<div class="sr {"d" if s=="Done" else ("n" if s=="Next" else "")}"><span class=tm>{t}</span><div style="flex:1"><b>{a}</b><small>{b}</small></div><i>{s}</i></div>' for t,a,b,s in sched)}
 <div class=car><span>{ic("pin",22)}</span>Pickup point and car number shown for each lesson</div></div>
 <div class=R>{dpts([("clock","Day plan on their phone"),("check","Mark lessons done"),("users","Owner sees every car's day")])}</div>''',
 """.vis{gap:20px;align-items:stretch}
.L{flex:1.35;padding:24px;display:flex;flex-direction:column;gap:10px;min-width:0}
.th{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}.th b{font:800 24px 'Montserrat'}.th span{font:700 13px 'Open Sans';letter-spacing:2px;color:#8a978f}
.sr{flex:1;display:flex;align-items:center;gap:14px;padding:13px 14px;border-radius:14px;background:#f6f3ea}
.sr .tm{font:800 16px 'Montserrat';width:84px;flex:none}.sr b{display:block;font:700 18px 'Open Sans'}.sr small{display:block;font:500 15px 'Open Sans';color:#5b6b62}
.sr i{font:700 14px 'Open Sans';font-style:normal;color:#8a978f}.sr.d i{color:#2e8a57}.sr.n{background:#fdecee;box-shadow:inset 0 0 0 2px #d62f3a}.sr.n i{color:#d62f3a}
.car{margin-top:auto;display:flex;gap:10px;align-items:center;background:#1c3d2e;color:#fff;border-radius:14px;padding:14px 16px;font:600 17px 'Open Sans'}
.R{flex:1;display:flex;flex-direction:column;gap:14px;justify-content:center;min-width:0}""")

P["p29_driving_s5"] = dslide(5, "STILL NOT SURE?", "Most driving schools<br>start with <span>one.</span>",
 "Tell us how your school runs today. We will suggest the simplest place to start, then grow from there.",
 f'''<div class=w>{peep("Explaining","Smile","MediumStraight",w=380,h=560)}<div class=st>
 {"".join(f'<div class=s><span class=k>{k}</span><div><b>{a}</b><small>{b}</small></div></div>' for k,a,b in [("A","Need more students?","Start with the website."),("B","Too many calls from students?","Start with the student app."),("C","Busy team, many cars?","Start with the instructor app."),("+","Want all three?","Start with one, add the rest later.")])}</div></div>''',
 """.vis{align-items:flex-end}.w{display:flex;align-items:flex-end;gap:20px;width:100%}
.st{flex:1;display:flex;flex-direction:column;gap:14px;padding-bottom:10px}
.s{display:flex;gap:16px;align-items:center;background:#fff;border-radius:22px;padding:34px 26px;box-shadow:0 14px 30px rgba(28,61,46,.1)}
.s .k{width:56px;height:56px;border-radius:16px;background:#d62f3a;color:#fff;font:900 28px/56px 'Montserrat';text-align:center;flex:none}
.s b{display:block;font:800 25px/1.3 'Montserrat'}.s small{display:block;font:500 21px 'Open Sans';color:#5b6b62;margin-top:3px}""",
 cta="Ask us which one. DM us", ctacss="background:#d62f3a;color:#fff")

# ───────── 30 USA · Dog walker / pet sitter · SINGLE · Crimson Text + Poppins · butter / ink / teal · phone (2 of 10)
# New technique: hand-drawn SVG walk route on a mini map inside the phone + sticker labels.
route = '<svg viewBox="0 0 280 170" width="100%" height="170" style="display:block"><rect width="280" height="170" rx="14" fill="#e8f3ea"/><path d="M0 60H280M0 128H280M90 0V170M200 0V170" stroke="#fff" stroke-width="12"/><path d="M40 140 C 70 140, 90 120, 90 92 S 120 60, 160 60 S 200 40, 205 24" fill="none" stroke="#1f9d8f" stroke-width="5" stroke-linecap="round" stroke-dasharray="1 10"/><circle cx="40" cy="140" r="9" fill="#1f2a44"/><circle cx="205" cy="24" r="9" fill="#ff7a59"/></svg>'
P["p30_dogwalker"] = page("""
body{--f:'Poppins';--h:'Crimson Text';background:#fff4cf;color:#1f2a44}
.blob{position:absolute;right:-160px;bottom:120px;width:640px;height:640px;border-radius:50%;background:#ffe08a}
h1{font-size:72px;font-weight:700;letter-spacing:-1px;line-height:1.2} h1 span{color:#1f9d8f;font-style:italic}
.sub{color:#5a6178;max-width:860px}
.vis{gap:34px;align-items:stretch}
.L{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}.L .stk{flex:1}
.stk{background:#fff;border-radius:22px;padding:38px 26px;display:flex;gap:16px;align-items:center;box-shadow:0 14px 30px rgba(31,42,68,.08)}
.stk:nth-child(even){margin-left:34px}.stk:nth-child(odd){margin-right:34px}
.stk .ib{width:54px;height:54px;border-radius:50%;background:#1f9d8f;color:#fff}
.stk b{display:block;font:700 25px Poppins}.stk small{display:block;font:400 19px/1.4 Poppins;color:#5a6178}
.ap{padding:4px 16px 16px;display:flex;flex-direction:column;gap:10px;flex:1;color:#1f2a44}
.ap .h{display:flex;justify-content:space-between;align-items:center}.ap .h b{font:700 19px Poppins}.ap .h span{font:600 12px Poppins;background:#e0f5f2;color:#1f9d8f;border-radius:10px;padding:4px 8px}
.ap .s{font:500 12px Poppins;color:#7a8199;margin-top:-6px}
.kv{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}.kv div{background:#f6f2e4;border-radius:12px;padding:9px 6px;text-align:center}.kv b{display:block;font:700 16px Poppins}.kv small{font:500 11px Poppins;color:#7a8199}
.ph2{height:110px;border-radius:14px;background:linear-gradient(135deg,#ffd27a,#ff9e7a);display:flex;align-items:center;justify-content:center;color:#fff;font:600 13px Poppins;gap:8px}
.nt{background:#f6f2e4;border-radius:12px;padding:10px 12px;font:400 13px/1.45 Poppins}
.nt b{font-weight:700}
""", "<h1>Every walk,<br><span>a report owners love.</span></h1><div class=sub>For dog walkers and pet sitters: route, time, photo and notes, sent the moment you finish.</div>",
'<div class=L>' + "".join(f'<div class=stk><span class=ib>{ic(i,26)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i, a, b in [("map", "Route on a map", "Owners see where you went."), ("clock", "Start and end time", "Logged on its own."), ("camera", "A photo from the walk", "The part owners wait for."), ("doc", "Short notes", "Water, mood, anything unusual.")]) + '</div>' +
phone(f'''<div class=ap><div class=h><b>Walk report</b><span>Sent</span></div><div class=s>Sample · Buddy · Tue 12:30 PM</div>{route}
<div class=kv><div><b>32 min</b><small>Time</small></div><div><b>1.4 mi</b><small>Distance</small></div><div><b>Yes</b><small>Water</small></div></div>
<div class=ph2>{ic("camera",22,"#fff")} Photo from the walk</div><div class=nt><b>Note:</b> Happy and calm today. Said hello to two dogs at the park.</div></div>''', w=350, h=720),
"#1f2a44", "Want this for your pet business? DM us", "background:#1f2a44;color:#fff", bg="<div class=blob></div>")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
