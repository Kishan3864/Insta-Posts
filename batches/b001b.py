import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 24 USA · Plumber · CAROUSEL 6 · Anton + Roboto · blueprint navy / copper / cream
# New technique: blueprint grid background + CSS copper pipe illustration.
PL = """
body{--f:'Roboto';--h:'Anton';background:#0e2340;color:#fbf4ea}
body:before{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(140,180,230,.10) 1px,transparent 1px),linear-gradient(90deg,rgba(140,180,230,.10) 1px,transparent 1px),linear-gradient(rgba(140,180,230,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(140,180,230,.05) 1px,transparent 1px);background-size:120px 120px,120px 120px,24px 24px,24px 24px}
h1{font-size:72px;font-weight:400;letter-spacing:.5px;line-height:1.2;text-transform:uppercase} h1 span{color:#ee9a5f}
.sub{color:#b9c7dd;font-size:25px}
.sn{font:700 18px 'Roboto';letter-spacing:3px;color:#ee9a5f;margin-top:22px}
.card{background:#fbf4ea;color:#0e2340;border-radius:24px;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.pt{display:flex;gap:16px;align-items:center;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.14);border-radius:20px;padding:20px 22px}
.pt .ib{width:52px;height:52px;border-radius:14px;background:#ee9a5f;color:#0e2340}
.pt b{display:block;font:700 22px/1.3 'Roboto'}.pt small{display:block;font:400 18px/1.4 'Roboto';color:#b9c7dd;margin-top:3px}
"""
def pslide(n, kicker, title, sub, vis, css, cta="Swipe", ctacss="background:#ee9a5f;color:#0e2340"):
    return page(PL+css, f"<div class=sn>{kicker}</div><h1 style='margin-top:30px'>{title}</h1><div class=sub>{sub}</div>", vis, "#fbf4ea", cta, ctacss, tagline=f"{n} / 6")
pts = lambda L: "".join(f'<div class=pt><span class=ib>{ic(i,26)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i, a, b in L)

P["p24_plumber_s1"] = pslide(1, "FOR PLUMBING BUSINESSES", "Missed a burst-pipe<br>call at <span>11 PM?</span>",
 "4 things your plumbing website should do while you sleep.",
 f'''<div class=art><div class="p h1p"></div><div class="p v1"></div><div class="p h2p"></div><div class="p v2"></div>
 <div class="j" style="left:400px;top:52px"></div><div class="j" style="left:400px;top:262px"></div><div class="j" style="left:640px;top:262px"></div>
 <div class=valve style="left:178px;top:36px"></div><div class=drop></div><div class="drop d2"></div><div class=pud></div>
 <div class=sign><small>Office hours · sample</small><b>Closed now</b><span>Open 8 AM to 6 PM</span></div><div class=calls><b>Missed calls · sample</b>{"".join(f'<div class=mc><span class=ib>{ic("phone",18)}</span><div>Unknown number<small>{t}</small></div></div>' for t in ["11:04 PM","11:31 PM","6:12 AM"])}</div></div>
 <div class=nums>{"".join(f'<span><i>{i}</i>{t}</span>' for i,t in [(1,"Book a time"),(2,"Flag urgent"),(3,"Send a photo"),(4,"Check ZIP")])}</div>''',
 """.vis{flex-direction:column;gap:22px}
.art{flex:1;position:relative;border:2px dashed rgba(238,154,95,.35);border-radius:28px;overflow:hidden}
.p{position:absolute;background:linear-gradient(180deg,#f6b98a,#c96a33 60%,#9c4b20);border-radius:12px}
.h1p{left:0;top:62px;width:440px;height:44px}.v1{left:410px;top:62px;width:44px;height:250px;background:linear-gradient(90deg,#f6b98a,#c96a33 60%,#9c4b20)}
.h2p{left:410px;top:272px;width:270px;height:44px}.v2{left:650px;top:272px;width:44px;height:120px;background:linear-gradient(90deg,#f6b98a,#c96a33 60%,#9c4b20)}
.j{position:absolute;width:64px;height:64px;margin:-0px 0 0 0;border-radius:14px;background:#b85d2a;box-shadow:inset 0 -6px 0 rgba(0,0,0,.2)}
.valve{position:absolute;width:76px;height:76px;border-radius:50%;background:#d84a3a;box-shadow:inset 0 -8px 0 rgba(0,0,0,.2);border:6px solid #fbf4ea}
.drop{position:absolute;left:660px;top:408px;width:26px;height:36px;background:#7cc3ff;border-radius:50% 50% 50% 50%/60% 60% 40% 40%}
.drop.d2{top:458px;left:666px;width:16px;height:22px;opacity:.7}
.pud{position:absolute;left:600px;top:498px;width:150px;height:22px;border-radius:50%;background:rgba(124,195,255,.45)}
.calls{position:absolute;left:40px;bottom:40px;width:330px;background:#fbf4ea;color:#0e2340;border-radius:22px;padding:20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 24px 50px rgba(0,0,0,.35)}
.calls b{font:700 18px Roboto;color:#d84a3a}
.mc{display:flex;gap:12px;align-items:center;background:#fff;border-radius:14px;padding:11px 12px;font:600 18px Roboto}
.mc small{display:block;font:400 15px Roboto;color:#6b7891}.mc .ib{width:38px;height:38px;border-radius:50%;background:#fde3df;color:#d84a3a}
.sign{position:absolute;right:40px;top:40px;width:300px;background:#fbf4ea;color:#0e2340;border-radius:22px;padding:24px;text-align:center;box-shadow:0 24px 50px rgba(0,0,0,.35);border-top:10px solid #d84a3a}.sign small{display:block;font:600 15px Roboto;color:#8a7a68;letter-spacing:1px}.sign b{display:block;white-space:nowrap;font:400 46px/1.25 Anton;letter-spacing:1px;color:#d84a3a;margin:16px 0 8px}.sign span{font:600 19px Roboto}
.nums{display:flex;gap:12px}.nums span{flex:1;display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);border-radius:18px;padding:14px;font:700 18px Roboto}
.nums i{font:400 30px 'Anton';font-style:normal;color:#ee9a5f}""")

slots = [("8 - 10 AM", "Taken"), ("10 - 12", "Open"), ("12 - 2 PM", "Open"), ("2 - 4 PM", "Taken"), ("4 - 6 PM", "Open"), ("Emergency", "Call back")]
sl = "".join(f'<div class="sl {"tk" if b=="Taken" else ("em" if a=="Emergency" else ("on" if a=="12 - 2 PM" else ""))}"><b>{a}</b><small>{b}</small></div>' for a, b in slots)
P["p24_plumber_s2"] = pslide(2, "THING 1 OF 4", "Let them <span>book a<br>time window</span>",
 "Customers pick a slot at night. You wake up to a full schedule.",
 browser(f'''<div class=bk><div class=bh><b>Book a plumber</b><span>Sample site</span></div>
 <div class=lbl>What do you need?</div><div class=chips>{"".join(f'<span class="ch {"on" if i==1 else ""}">{t}</span>' for i,t in enumerate(["Leak","Clogged drain","Water heater","Toilet","Something else"]))}</div>
 <div class=lbl>Pick a day</div><div class=days>{"".join(f'<span class="dy {"on" if d=="Wed" else ""}"><small>{d}</small><b>{n}</b></span>' for d,n in [("Mon","16"),("Tue","17"),("Wed","18"),("Thu","19"),("Fri","20"),("Sat","21")])}</div>
 <div class=lbl>Pick a time window</div><div class=slots>{sl}</div><div class=lbl>Your details</div><div class=fm><span>Name</span><span>Phone</span><span class=wd>Street address</span></div><div class=go>Confirm booking · we text you a reminder</div></div>''', "yourplumbing.com/book", "flex:1;color:#0e2340"),
 """.vis{display:flex}
.bk{padding:24px 28px;display:flex;flex-direction:column;gap:12px;flex:1;background:#fbf4ea}
.bh{display:flex;justify-content:space-between;align-items:center}.bh b{font:400 34px 'Anton';letter-spacing:.5px}.bh span{font:700 14px Roboto;letter-spacing:2px;color:#8a7a68;text-transform:uppercase}
.lbl{font:700 17px Roboto;color:#6b5d4f;margin-top:6px}
.chips{display:flex;flex-wrap:wrap;gap:10px}.ch{font:600 18px Roboto;padding:11px 18px;border-radius:30px;background:#fff;border:2px solid #e6dccd}.ch.on{background:#0e2340;color:#fff;border-color:#0e2340}
.days{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}.dy{background:#fff;border:2px solid #e6dccd;border-radius:16px;padding:10px;text-align:center}.dy small{display:block;font:500 15px Roboto;color:#8a7a68}.dy b{font:700 24px Roboto}
.dy.on{background:#ee9a5f;border-color:#ee9a5f}.dy.on small{color:#0e2340}
.slots{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.sl{background:#fff;border:2px solid #e6dccd;border-radius:16px;padding:14px}.sl b{display:block;font:700 20px Roboto}.sl small{font:500 15px Roboto;color:#2e8a57}
.sl.tk{background:#efe8dd;color:#a89a89}.sl.tk small{color:#a89a89}.sl.on{border-color:#0e2340;box-shadow:inset 0 0 0 2px #0e2340}.sl.em{background:#fde3df;border-color:#f3b9b0}.sl.em small{color:#d84a3a}
.fm{display:grid;grid-template-columns:1fr 1fr;gap:10px}.fm span{background:#fff;border:2px solid #e6dccd;border-radius:14px;padding:14px 16px;font:500 17px Roboto;color:#9a8b7a}.fm .wd{grid-column:span 2}
.go{margin-top:auto;background:#0e2340;color:#fff;border-radius:16px;padding:18px;text-align:center;font:700 19px Roboto}""")

P["p24_plumber_s3"] = pslide(3, "THING 2 OF 4", "Let them <span>flag it<br>as urgent</span>",
 "Two quick questions tell you what can wait and what cannot.",
 f'''<div class="card L"><b class=t>Is water leaking right now?</b><div class=yn><span class=on>Yes</span><span>No</span></div>
 <b class=t>Where is the problem?</b><div class=yn><span class=on>Kitchen</span><span>Bathroom</span><span>Outside</span></div>
 <b class=t>Did you close the main valve?</b><div class=yn><span>Yes</span><span class=on>Not sure</span></div>
 <div class=al><span class=ib>{ic("bell",24)}</span><div><b>Urgent request sent</b><small>The on-call plumber gets an alert and calls back.</small></div></div></div>
 <div class=R><div class=tip><span class=tg>WHILE YOU WAIT</span><b>Find the main shut-off valve and turn it off.</b><small>Your website can show this tip the moment someone taps "Yes".</small></div>
 {pts([("clock","Urgent jobs first","Sorted above normal bookings."),("phone","Right person alerted","Only whoever is on call.")])}</div>''',
 """.vis{gap:24px;align-items:stretch}
.L{flex:1.1;padding:28px;display:flex;flex-direction:column;gap:14px;min-width:0}
.t{font:700 24px/1.3 Roboto}.yn{display:flex;gap:10px;margin-bottom:10px}.yn span{flex:1;text-align:center;padding:20px 10px;border-radius:16px;background:#fff;border:2px solid #e6dccd;font:700 20px Roboto}
.yn .on{background:#d84a3a;border-color:#d84a3a;color:#fff}
.al{margin-top:auto;display:flex;gap:14px;align-items:center;background:#0e2340;color:#fff;border-radius:18px;padding:20px}
.al .ib{width:50px;height:50px;border-radius:50%;background:#ee9a5f;color:#0e2340}.al b{display:block;font:700 21px Roboto}.al small{display:block;font:400 17px/1.4 Roboto;color:#b9c7dd}
.R{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.tip{flex:1;background:#ee9a5f;color:#0e2340;border-radius:24px;padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}
.tip .tg{font:700 15px Roboto;letter-spacing:2px}.tip b{font:400 34px/1.25 'Anton';letter-spacing:.3px}.tip small{font:500 18px/1.4 Roboto}""")

sink = '<div class=ph><div class=sk><i class=bw></i><i class=tp></i><i class=pp></i><i class=dr></i></div><span>Under the sink</span></div>'
heater = '<div class=ph><div class=wh><i class=lb></i></div><span>Water heater label</span></div>'
drain = '<div class=ph><div class=dn><i></i></div><span>Floor drain</span></div>'
P["p24_plumber_s4"] = pslide(4, "THING 3 OF 4", "Get a <span>photo</span> before<br>you drive out",
 "See the problem first. Bring the right parts on the first trip.",
 f'''<div class="card L"><div class=up><b>Add photos of the problem</b><small>Sample upload form</small></div><div class=grid>{sink}{heater}{drain}<div class="ph add"><span class=ib>{ic("upload",34)}</span><span>Add more</span></div></div>
 <div class=nt><b>Note from customer</b><p>Water under the sink since last night. Dripping from the pipe joint.</p></div></div>''',
 """.vis{display:flex}
.L{flex:1;padding:28px;display:flex;flex-direction:column;gap:18px}
.up b{display:block;font:400 32px 'Anton';letter-spacing:.4px}.up small{font:500 16px Roboto;color:#8a7a68}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1}
.ph{background:#e9eef6;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:14px;gap:10px;position:relative;overflow:hidden}
.ph>span{font:700 17px Roboto;background:#fff;border-radius:20px;padding:7px 14px}
.sk{width:200px;height:150px;position:relative}.sk .bw{position:absolute;left:10px;right:10px;top:0;height:40px;border-radius:6px 6px 40px 40px;background:#cfd8e6}
.sk .tp{position:absolute;left:40px;top:40px;width:22px;height:80px;background:#9aa8bd}.sk .pp{position:absolute;left:40px;top:110px;width:120px;height:22px;border-radius:10px;background:#c96a33}
.sk .dr{position:absolute;left:150px;top:132px;width:14px;height:18px;border-radius:50%;background:#4ea3ff}
.wh{width:110px;height:160px;border-radius:30px 30px 14px 14px;background:linear-gradient(90deg,#dfe5ee,#b9c3d3);position:relative}.wh .lb{position:absolute;left:25px;top:40px;width:60px;height:40px;border-radius:6px;background:#fff;box-shadow:inset 0 -14px 0 #ee9a5f}
.dn{width:150px;height:150px;border-radius:50%;background:#cfd8e6;display:flex;align-items:center;justify-content:center}.dn i{width:90px;height:90px;border-radius:50%;background:repeating-linear-gradient(90deg,#6b7891 0 8px,#cfd8e6 8px 16px)}
.ph.add{background:#fff;border:3px dashed #e0cbb3;justify-content:center;color:#c96a33}.ph.add>span:last-child{background:none}
.nt{background:#0e2340;color:#fff;border-radius:18px;padding:20px 22px}.nt b{font:700 17px Roboto;color:#ee9a5f}.nt p{font:400 21px/1.45 Roboto;margin-top:6px}""")

P["p24_plumber_s5"] = pslide(5, "THING 4 OF 4", "Show your <span>service<br>area</span> by ZIP code",
 "People outside your area find out before they call.",
 f'''<div class="card L"><div class=zip><span>{ic("search",26)}</span><b>Enter your ZIP code</b><i>12345</i></div>
 <div class=map><div class="z z3 free"></div><div class="z z2 free"></div><div class="z z1 free"></div><div class=pin>{ic("pin",44,"#fff",2.2)}</div>
 <div class=road style="top:40%;left:0;right:0;height:16px"></div><div class=road style="left:56%;top:0;bottom:0;width:16px"></div><div class=road style="top:75%;left:10%;right:30%;height:12px"></div></div>
 <div class=ok><span class=ib>{ic("check",24,w=3)}</span><div><b>Yes, we serve your area.</b><small>Pick a time window to book.</small></div></div></div>''',
 """.vis{display:flex}
.L{flex:1;padding:26px;display:flex;flex-direction:column;gap:16px}
.zip{display:flex;align-items:center;gap:14px;background:#fff;border:2px solid #0e2340;border-radius:18px;padding:16px 20px}.zip b{font:700 21px Roboto;flex:1}.zip i{font:700 24px Roboto;font-style:normal;letter-spacing:3px;color:#c96a33}
.map{flex:1;border-radius:20px;background:#e6ecd9;position:relative;overflow:hidden}
.road{position:absolute;background:#fff}
.z{position:absolute;left:56%;top:40%;border-radius:50%;transform:translate(-50%,-50%)}
.z1{width:220px;height:220px;background:rgba(46,138,87,.45)}.z2{width:420px;height:420px;background:rgba(46,138,87,.25)}.z3{width:640px;height:640px;background:rgba(46,138,87,.12)}
.pin{position:absolute;left:56%;top:40%;width:76px;height:76px;margin:-38px 0 0 -38px;border-radius:50%;background:#d84a3a;display:flex;align-items:center;justify-content:center;z-index:3;border:5px solid #fff}
.ok{display:flex;gap:14px;align-items:center;background:#2e8a57;color:#fff;border-radius:18px;padding:18px 20px}
.ok .ib{width:48px;height:48px;border-radius:50%;background:#fff;color:#2e8a57}.ok b{display:block;font:700 22px Roboto}.ok small{font:400 17px Roboto;color:#d5f0df}""")

P["p24_plumber_s6"] = pslide(6, "BUILT FOR YOUR TRUCKS AND TEAM", "Want a website that<br><span>books jobs</span> after hours?",
 "We build plumbing websites with booking, urgent requests, photo upload and service area checks.",
 f'''<div class=w>{peep("Explaining","Smile","ShortCurly","Full",w=400,h=560)}<div class=lst>
 {pts([("cal","Time window booking","Fills your schedule overnight."),("bell","Urgent requests","Straight to whoever is on call."),("camera","Photo upload","Right parts, first trip."),("map","ZIP code check","Only calls from your area.")])}</div></div>''',
 """.vis{align-items:flex-end}.w{display:flex;align-items:flex-end;gap:24px;width:100%}
.lst{flex:1;display:flex;flex-direction:column;gap:14px;padding-bottom:6px}.lst .pt{padding:30px 24px}.lst .pt b{font-size:25px}.lst .pt small{font-size:19px}""",
 cta="Let's talk. DM us", ctacss="background:#ee9a5f;color:#0e2340")

# ───────── 25 INDIA · Sweet shop bulk box orders · SINGLE · Gelasio + Poppins · pistachio / chocolate / orange
# New technique: kanban order board (columns) as the hero visual.
def kc(qty, size, item, when, tag, tc):
    return f'<div class=kc><div class=kt><b>{qty} boxes</b><span style="background:{tc[0]};color:{tc[1]}">{tag}</span></div><p>{item}</p><div class=km><span>{size}</span><span>{when}</span></div></div>'
cols = [("New", "#3d2314", [kc(40, "500 g box", "Kaju katli + barfi mix", "Pickup Sat, 11 AM", "Advance paid", ("#dff0cf", "#2f6b12")),
                             kc(50, "500 g box", "Dry fruit box", "Pickup Mon, 10 AM", "Call to confirm", ("#ffe6cf", "#a2510f")),
                             kc(120, "250 g box", "Assorted sweets", "Pickup Sun, 9 AM", "Office order", ("#ffe6cf", "#a2510f"))]),
        ("Packing", "#e07a1f", [kc(60, "1 kg box", "Soan papdi + dry fruit", "Pickup today, 6 PM", "Name sticker", ("#ffe6cf", "#a2510f")),
                                 kc(25, "500 g box", "Peda", "Pickup today, 7 PM", "Advance paid", ("#dff0cf", "#2f6b12")),
                                 kc(45, "250 g box", "Milk cake", "Pickup Fri, 5 PM", "Name sticker", ("#ffe6cf", "#a2510f"))]),
        ("Ready", "#2f6b12", [kc(80, "250 g box", "Motichoor laddoo", "Waiting at counter", "Customer told", ("#dff0cf", "#2f6b12")),
                               kc(20, "1 kg box", "Besan laddoo", "Waiting at counter", "Customer told", ("#dff0cf", "#2f6b12")),
                               kc(30, "1 kg box", "Kaju katli", "Picked up", "Balance paid", ("#e9e3dc", "#6b5a4c"))])]
board = "".join(f'<div class=col><div class=chd><i style="background:{c}"></i>{n}<span>{len(cards)}</span></div>{"".join(cards)}</div>' for n, c, cards in cols)
P["p25_sweetshop"] = page("""
body{--f:'Poppins';--h:'Gelasio';background:#e4eed3;color:#3d2314}
body:after{content:"";position:absolute;left:-120px;bottom:-160px;width:560px;height:560px;border-radius:50%;background:#d3e3b8;z-index:0}
h1{font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#d0661a;font-style:italic}
.sub{color:#5e4a3c}
.vis{flex-direction:column;gap:18px}
.bd{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;background:#fffaf1;border-radius:28px;padding:20px;box-shadow:0 30px 60px rgba(61,35,20,.14);min-height:0}
.col{background:#f4ede2;border-radius:20px;padding:14px;display:flex;flex-direction:column;gap:12px}
.chd{display:flex;align-items:center;gap:10px;font:700 21px Poppins}.chd i{width:14px;height:14px;border-radius:50%}.chd span{margin-left:auto;font:700 15px Poppins;background:#fff;border-radius:20px;padding:3px 11px}
.kc{background:#fff;border-radius:16px;padding:16px;box-shadow:0 6px 14px rgba(61,35,20,.07);flex:1;display:flex;flex-direction:column;gap:8px}
.kt{display:flex;justify-content:space-between;align-items:center;gap:6px}.kt b{font:700 26px 'Gelasio'}.kt span{font:600 12px Poppins;padding:4px 9px;border-radius:12px;white-space:nowrap}
.kc p{font:600 20px/1.35 Poppins}
.km{margin-top:auto;display:flex;flex-direction:column;gap:4px;font:500 16px Poppins;color:#7a6656}
.strip{display:flex;gap:14px}
.sp{flex:1;display:flex;gap:12px;align-items:center;background:#3d2314;color:#fff;border-radius:20px;padding:16px 18px;font:600 18px/1.3 Poppins}
.sp .ib{width:44px;height:44px;border-radius:14px;background:#e07a1f;color:#fff}
""", "<h1>Bulk box orders,<br><span>from order to pickup.</span></h1><div class=sub>For sweet shops: box sizes, quantities and pickup times on one board. Sample orders.</div>",
f'''<div class=bd>{board}</div><div class=strip>{"".join(f'<div class=sp><span class=ib>{ic(i,24)}</span>{t}</div>' for i,t in [("box","Boxes needed per size, totalled"),("bell","Ready message to the customer"),("rupee","Advance and balance noted")])}</div>''',
"#3d2314", "Want this board for your shop? DM us", "background:#e07a1f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
