import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 39 USA · Roofing contractor · CAROUSEL 6 · Poppins + Source Sans 3 · charcoal / sky / shingle brown
# New format: "questions to answer before you build" + CSS roof-shingle texture header band.
RF = """
body{--f:'Source Sans 3';--h:'Poppins';background:#22262e;color:#f4f1ea}
.shg{position:absolute;left:0;right:0;top:0;height:120px;background:radial-gradient(circle at 50% 0,transparent 0 22px,#3a2f2a 23px) 0 0/56px 30px,#3a2f2a;opacity:.55;-webkit-mask:linear-gradient(#000,transparent)}
h1{font-family:'Poppins';font-size:58px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#9ad1ff}
.sub{color:#b9bfcb}
.sn{font:700 17px 'Poppins';letter-spacing:3px;color:#e0a36b;margin-top:22px}
.qn{font:800 210px/1.1 'Poppins';color:#9ad1ff;letter-spacing:-6px}
.card{background:#f4f1ea;color:#22262e;border-radius:24px}
.why{background:rgba(154,209,255,.1);border:1px solid rgba(154,209,255,.3);border-radius:22px;padding:22px 24px}
.why em{font:700 15px Poppins;font-style:normal;letter-spacing:2px;color:#9ad1ff}.why p{font:400 24px/1.45 'Source Sans 3';margin-top:6px}
"""
def rslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#9ad1ff;color:#22262e"):
    return page(RF+css, f"<div class=sn>{kick}</div><h1 style='margin-top:10px'>{title}</h1><div class=sub>{sub}</div>", vis, "#f4f1ea", cta, ctacss, bg="<div class=shg></div>", tagline=f"{n} / 6")

P["p39_roofing_s1"] = rslide(1, "FOR ROOFING CONTRACTORS", "4 questions to answer<br><span>before you build</span><br>your roofing website.",
 "Answer these first and your website will bring the right jobs, not just visits.",
 f'''<div class=hs><svg viewBox="0 -170 940 530" width="100%" height="100%" preserveAspectRatio="xMidYMax meet"><g fill="#4a5160"><circle cx="640" cy="-90" r="55"/><circle cx="710" cy="-110" r="70"/><circle cx="790" cy="-85" r="50"/><rect x="600" y="-90" width="230" height="55" rx="27"/></g><g stroke="#9ad1ff" stroke-width="6" stroke-linecap="round"><line x1="630" y1="-15" x2="616" y2="25"/><line x1="662" y1="-15" x2="648" y2="25"/><line x1="694" y1="-15" x2="680" y2="25"/><line x1="726" y1="-15" x2="712" y2="25"/><line x1="758" y1="-15" x2="744" y2="25"/><line x1="790" y1="-15" x2="776" y2="25"/><line x1="822" y1="-15" x2="808" y2="25"/></g><circle cx="170" cy="-100" r="8" fill="#e0a36b"/><circle cx="230" cy="-60" r="5" fill="#e0a36b"/><path d="M60 200 L470 30 L880 200 Z" fill="#7a4b2a"/><path d="M60 200 L470 30 L880 200" fill="none" stroke="#e0a36b" stroke-width="10" stroke-linejoin="round"/>
 {"".join(f'<path d="M{150+i*0} {120+i*0}" />' for i in range(1))}<g stroke="#5e3920" stroke-width="3">{"".join(f'<line x1="{470-(170-30)*k/170*2.4-0}" y1="{30+k}" x2="{470+(170-30)*k/170*2.4}" y2="{30+k}"/>' for k in range(30,171,28))}</g>
 <rect x="130" y="200" width="680" height="150" fill="#f4f1ea"/><rect x="420" y="250" width="100" height="100" fill="#22262e"/><rect x="190" y="235" width="140" height="80" fill="#9ad1ff"/><rect x="610" y="235" width="140" height="80" fill="#9ad1ff"/></svg>
 <div class=qs>{"".join(f'<span><b>Q{i}</b>{t}</span>' for i,t in [(1,"Which jobs?"),(2,"Which area?"),(3,"First step?"),(4,"Follow-up?")])}</div></div>''',
 """.vis{display:flex}.hs{flex:1;display:flex;flex-direction:column;gap:18px}.hs svg{flex:1;min-height:0}
.qs{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.qs span{background:#f4f1ea;color:#22262e;border-radius:18px;padding:22px 18px;font:700 22px Poppins;display:flex;flex-direction:column;gap:2px}.qs b{font:800 28px Poppins;color:#7a4b2a}""")

def qslide(n, q, title, why, vis, css):
    return rslide(n, f"QUESTION {q} OF 4", title, "", f'<div class=lq><div class=qn>Q{q}</div><div class=why><em>WHY IT MATTERS</em><p>{why}</p></div></div><div class=rq>{vis}</div>',
                  ".vis{gap:22px;align-items:stretch}.lq{width:330px;flex:none;display:flex;flex-direction:column;justify-content:space-between}.rq{flex:1;display:flex;min-width:0}" + css)

P["p39_roofing_s2"] = qslide(2, 1, "Which jobs do you<br><span>want more of?</span>",
 "Repairs, full replacements and inspections need different pages. Lead with the job you want most.",
 f'''<div class="card pk"><b class=t>Pick your main job · sample</b>{"".join(f'<div class="o {"on" if i==1 else ""}"><span class=ib>{ic(ic_,26)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,(ic_,a,b) in enumerate([("wrench","Roof repair","Leaks, missing shingles"),("home","Full replacement","Biggest jobs, longer decisions"),("search","Roof inspection","A first step for new customers"),("drop","Gutters","Add-on work after a roof job")]))}</div>''',
 """.pk{flex:1;padding:24px;display:flex;flex-direction:column;gap:12px}.t{font:800 22px Poppins}
.o{flex:1;display:flex;gap:16px;align-items:center;background:#fff;border-radius:18px;padding:14px 18px;border:3px solid transparent}
.o .ib{width:52px;height:52px;border-radius:14px;background:#e9e4da;color:#7a4b2a}.o b{display:block;font:700 22px Poppins}.o small{display:block;font:400 18px 'Source Sans 3';color:#5d6470}
.o.on{border-color:#7a4b2a}.o.on .ib{background:#7a4b2a;color:#fff}""")

P["p39_roofing_s3"] = qslide(3, 2, "Which area do<br><span>you serve?</span>",
 "Calls from too far away waste your time. Show your towns and let people check by ZIP code.",
 f'''<div class="card ar"><div class=zp><span>{ic("search",24)}</span><b>Enter ZIP code</b><i>12345</i></div><div class=mp>{"".join(f'<span class="tw {c}" style="left:{x}%;top:{y}%">{t}</span>' for t,x,y,c in [("Town A",26,28,"in"),("Town B",58,22,"in"),("Town C",44,52,"in"),("Town D",72,60,"in"),("Town E",18,72,"out"),("Town F",84,84,"out")])}<div class=zone></div></div><div class=rs>{ic("check",22,w=3)} Yes, we cover your area</div></div>''',
 """.ar{flex:1;padding:22px;display:flex;flex-direction:column;gap:14px}
.zp{display:flex;gap:12px;align-items:center;background:#fff;border:2px solid #22262e;border-radius:16px;padding:14px 18px}.zp b{flex:1;font:700 20px Poppins}.zp i{font:700 22px Poppins;font-style:normal;letter-spacing:3px;color:#7a4b2a}
.mp{flex:1;position:relative;background:#e3ecdf;border-radius:18px;overflow:hidden}
.zone{position:absolute;left:12%;top:10%;width:76%;height:66%;border-radius:46% 54% 50% 50%;background:rgba(154,209,255,.45);border:3px dashed #3c7fb8}
.tw{position:absolute;z-index:2;transform:translate(-50%,-50%);font:700 16px Poppins;padding:7px 12px;border-radius:12px;white-space:nowrap}.tw.in{background:#22262e;color:#fff}.tw.out{background:#fff;color:#8a8f99}
.rs{display:flex;gap:10px;align-items:center;justify-content:center;background:#2f7d4f;color:#fff;border-radius:16px;padding:16px;font:700 20px Poppins}""")

P["p39_roofing_s4"] = qslide(4, 3, "What should a visitor<br><span>do first?</span>",
 "One clear first step beats five buttons. For most roofers, that is booking a free inspection.",
 browser(f'''<div class=lp><div class=hr><b>Storm damage or a leak?</b><small>Sample roofing company · your area</small><span class=b1>Book a free inspection</span><span class=b2>or call us</span></div>
 <div class=st>{"".join(f'<div class=s><i>{i}</i>{t}</div>' for i,t in [(1,"Pick a time"),(2,"Add photos (optional)"),(3,"We confirm by text")])}</div></div>''', "yourroofing.com", "flex:1"),
 """.lp{flex:1;padding:18px;display:flex;flex-direction:column;gap:14px;background:#f4f1ea;color:#22262e}
.hr{flex:1;background:#7a4b2a;color:#fff;border-radius:18px;padding:26px;display:flex;flex-direction:column;justify-content:center;gap:10px}.hr b{font:800 32px/1.2 Poppins}.hr small{font:400 17px 'Source Sans 3';color:#f0dccb}
.b1{align-self:flex-start;background:#9ad1ff;color:#22262e;border-radius:14px;padding:15px 20px;font:700 19px Poppins;margin-top:8px}.b2{font:600 16px 'Source Sans 3';color:#f0dccb}
.st{display:flex;flex-direction:column;gap:10px}.s{display:flex;gap:14px;align-items:center;background:#fff;border-radius:14px;padding:14px 16px;font:600 19px Poppins}
.s i{width:34px;height:34px;border-radius:50%;background:#22262e;color:#fff;font:700 16px/1 Poppins;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}""")

P["p39_roofing_s5"] = qslide(5, 4, "How will you<br><span>follow up on estimates?</span>",
 "Roof jobs take time to decide. A simple estimate tracker reminds you who to call and when.",
 f'''<div class="card et"><b class=t>Estimates · sample</b>{"".join(f'<div class=e><div style="flex:1"><b>{a}</b><small>{b}</small></div><span class="pl {c}">{d}</span></div>' for a,b,c,d in [("Customer 1 · full replacement","Sent 3 days ago","y","Follow up today"),("Customer 2 · leak repair","Approved","g","Schedule crew"),("Customer 3 · inspection","Photos added","b","Send estimate"),("Customer 4 · gutters","Sent 10 days ago","r","Last reminder"),("Customer 5 · full replacement","Viewed twice","y","Call back")])}</div>''',
 """.et{flex:1;padding:22px;display:flex;flex-direction:column;gap:10px}.t{font:800 22px Poppins}
.e{flex:1;display:flex;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:12px 16px}.e b{display:block;font:700 19px Poppins}.e small{display:block;font:400 16px 'Source Sans 3';color:#5d6470}
.pl{font:700 14px Poppins;padding:6px 11px;border-radius:10px;white-space:nowrap}.y{background:#fff1d6;color:#a86400}.g{background:#dcf3e4;color:#1d7a43}.b{background:#e0f0ff;color:#2463a3}.r{background:#fde3e1;color:#b42318}""")

P["p39_roofing_s6"] = rslide(6, "YOUR ANSWERS, OUR BUILD", "Got your 4 answers?<br><span>We'll build around them.</span>",
 "Send them to us and we will plan a roofing website that brings the jobs you want.",
 f'''<div class=w>{peep("ArmsCrossed","Smile","ShortScratch","Chin",w=400,h=660)}<div class=cl>{"".join(f'<div class=c><span class=ck>{ic("check",22,w=3)}</span><div><b>Q{i}</b>{t}</div></div>' for i,t in [(1,"The jobs I want more of"),(2,"The area I serve"),(3,"The first step for visitors"),(4,"How I follow up")])}</div></div>''',
 """.vis{align-items:flex-end}.w{display:flex;align-items:flex-end;gap:20px;width:100%}
.cl{flex:1;display:flex;flex-direction:column;gap:14px;padding-bottom:8px}
.c{display:flex;gap:16px;align-items:center;background:#f4f1ea;color:#22262e;border-radius:22px;padding:38px 26px;font:600 26px/1.3 'Source Sans 3'}
.c b{font:800 24px Poppins;color:#7a4b2a;margin-right:10px}.ck{width:46px;height:46px;border-radius:50%;background:#2f7d4f;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}""",
 cta="Send us your answers. DM us")

# ───────── 40 INDIA · Yoga studio · SINGLE · Crimson Text + DM Sans · sage / charcoal / peach
# New mockup: printed receipt-style slip with zigzag edges (renewals this week).
ren = [("Member 01", "Morning batch · 6 AM", "Ends Mon"), ("Member 02", "Evening batch · 7 PM", "Ends Tue"), ("Member 03", "Weekend batch", "Ends Wed"),
       ("Member 04", "Morning batch · 7 AM", "Ends Thu"), ("Member 05", "Evening batch · 6 PM", "Ends Fri"), ("Member 06", "Morning batch · 6 AM", "Ends Sat"), ("Member 07", "Evening batch · 7 PM", "Ends Sat"), ("Member 08", "Weekend batch", "Ends Sun")]
P["p40_yoga"] = page("""
body{--f:'DM Sans';--h:'Crimson Text';background:#dfe8dc;color:#2b2f2c}
.sun{position:absolute;left:-120px;bottom:-120px;width:520px;height:520px;border-radius:50%;background:#f6c8a8;opacity:.8}
h1{font-size:72px;font-weight:700;line-height:1.2;letter-spacing:-.5px} h1 span{font-style:italic;color:#4f7a55}
.sub{color:#5b665d}
.vis{gap:28px;align-items:stretch}
.rc{width:470px;flex:none;display:flex;flex-direction:column;background:#fffdf8;padding:30px 30px 34px;position:relative;font-family:'Courier 10 Pitch','DejaVu Sans Mono',monospace;color:#2b2f2c;box-shadow:0 26px 40px rgba(43,47,44,.18);
-webkit-mask:conic-gradient(from -45deg at bottom,#0000,#000 1deg 89deg,#0000 90deg) 50%/24px 100%,conic-gradient(from 135deg at top,#0000,#000 1deg 89deg,#0000 90deg) 50%/24px 100%;-webkit-mask-composite:source-in;mask-composite:intersect}
.rc h4{text-align:center;font:700 22px 'DM Sans';letter-spacing:2px}.rc .c{text-align:center;font-size:15px;color:#6b726c;margin:4px 0 14px}
.rc .ln{border-top:2px dashed #b8bfb6;margin:10px 0}
.rr{flex:1;display:flex;justify-content:space-between;align-items:center;padding:6px 0;font-size:19px}.rr small{display:block;font-size:15px;color:#6b726c}.rr b{white-space:nowrap}
.tot{display:flex;justify-content:space-between;font:700 19px 'DM Sans';padding-top:4px}
.R{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.c2{flex:1;background:#2b2f2c;color:#fff;border-radius:22px;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.c2 .ib{width:48px;height:48px;border-radius:14px;background:#f6c8a8;color:#2b2f2c;margin-bottom:6px}.c2 b{font:700 22px/1.3 'DM Sans'}.c2 small{font:400 18px/1.45 'DM Sans';color:#c8d2c6}
""", "<h1>Renewals this week,<br><span>printed for you.</span></h1><div class=sub>For yoga studios: batch timings, attendance and renewals, without the register.</div>",
f'''<div class=rc><h4>RENEWALS · THIS WEEK</h4><div class=c>Sample studio · 8 members</div><div class=ln></div>{"".join(f'<div class=rr><div>{a}<small>{b}</small></div><b>{c}</b></div>' for a,b,c in ren)}<div class=ln></div><div class=tot><span>Reminders</span><span>Sent ✓</span></div></div>
<div class=R>{"".join(f'<div class=c2><span class=ib>{ic(i,24)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("clock","Batch timings in one place","Morning, evening and weekend batches with seats left."),("check","Attendance in a tap","Members check in with a QR at the door."),("bell","Renewal reminders","A friendly message a few days before the end date.")])}</div>''',
"#2b2f2c", "Want this for your studio? DM us", "background:#4f7a55;color:#fff", bg="<div class=sun></div>")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
