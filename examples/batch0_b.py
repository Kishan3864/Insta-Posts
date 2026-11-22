import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 11 INDIA · Family personal software · SINGLE · Poppins · mint/peach widgets
wid = lambda bg, fg, ico, title, body: f'<div class=w style="background:{bg}"><div class=wt><span class=ib style="background:{fg};color:#fff">{ic(ico,24)}</span>{title}</div>{body}</div>'
li = lambda a,b,c="#2d3a35": f'<div class=li><span>{a}</span><b style="color:{c}">{b}</b></div>'
P["p11_family"] = page("""
body{--f:'Poppins';background:linear-gradient(160deg,#eafaf3 0%,#fff0e6 100%);color:#22302b}
h1{font-size:60px;letter-spacing:-1.5px} h1 span{color:#e8713c}
.sub{color:#5d6b66}
.vis{flex-direction:column;gap:20px}
.grid{display:grid;grid-template-columns:1fr 1fr;gap:18px;flex:1}
.w{border-radius:28px;padding:22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 18px 40px rgba(34,48,43,.08)}
.wt{display:flex;gap:12px;align-items:center;font:700 22px Poppins;margin-bottom:4px}
.wt .ib{width:44px;height:44px;border-radius:14px}
.li{display:flex;justify-content:space-between;align-items:center;background:rgba(255,255,255,.75);border-radius:14px;padding:11px 14px;font:500 16px Poppins}
.li b{font-weight:700}
.bot{display:flex;align-items:flex-end;gap:18px}
.ask{flex:1;background:#22302b;color:#fff;border-radius:24px;padding:22px 24px;font:600 22px/1.4 Poppins;margin-bottom:16px}
.ask small{display:block;font:400 17px Poppins;color:#b9c9c2;margin-top:6px}
""", "<h1>One small app for your<br><span>whole family's paperwork.</span></h1><div class=sub>Personal software, made just for your home.</div>",
'<div class=grid>' +
 wid("#fff3e9","#e8713c","rupee","Bills due", li("Electricity","12th")+li("Rent","1st")+li("Internet","20th")+li("Insurance","Mar")) +
 wid("#e6f7ef","#1f9d6a","file","Documents", li("Car papers","Saved")+li("Warranty cards","6 saved")+li("Property papers","Saved")+li("Medical bills","Folder")) +
 wid("#eef0ff","#5b5bd6","cal","Family dates", li("Anniversary","Jun 14")+li("Car service","Every 6 mo")+li("Gas booking","Due soon","#e8713c")+li("Renewals","Auto alert")) +
 wid("#fff8dc","#c99a00","chart","This month", li("Groceries","Tracked")+li("Travel","Tracked")+li("Savings goal","On track","#1f9d6a")+li("Shared with","2 members")) +
 '</div><div class=bot>' + peep("Coffee","Smile","Medium",w=180,h=210) + peep("Device","Smile","ShortWavy","Chin",w=180,h=210) +
 '<div class=ask>Which one would you use first?<small>Tell us in the comments. Every family needs a different mix.</small></div></div>',
"#22302b", "Want one for your family? DM us", "background:#e8713c;color:#fff")

# ───────── 12 INDIA · Hardware / sanitary shop quotation · SINGLE · Roboto · steel blue/orange
items = [("CPVC pipe 1 in","20 m"),("Ball valve 1 in","6 pcs"),("Elbow 1 in","24 pcs"),("Wash basin set","2 sets"),("Wall mixer","2 pcs"),("Solvent cement","2 tins")]
it = "".join(f'<tr><td>{i+1}</td><td>{a}</td><td>{b}</td><td>Rate</td><td>Amount</td></tr>' for i,(a,b) in enumerate(items))
P["p12_hardware"] = page("""
body{--f:'Roboto';background:#e9eef4;color:#14273e}
.blue{position:absolute;left:0;top:420px;bottom:0;width:470px;background:#1d4e89;border-radius:0 40px 0 0}
h1{font-size:64px;font-weight:900;letter-spacing:-1.5px;color:#14273e} h1 span{color:#f26b1d}
.sub{color:#4a5d75}
.vis{gap:30px;align-items:center}
.doc{width:560px;flex:none;background:#fff;border-radius:6px;padding:30px 28px;box-shadow:0 40px 80px rgba(20,39,62,.25);transform:rotate(-2deg)}
.doc .h{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:3px solid #1d4e89;padding-bottom:14px;margin-bottom:14px}
.doc .h b{display:block;font:900 26px Roboto;color:#1d4e89}.doc .h small{font:400 13px Roboto;color:#7b8798;display:block}
.doc .q{font:700 20px Roboto;color:#f26b1d;text-align:right}
table{width:100%;border-collapse:collapse;font:400 15px Roboto}
th{background:#eef3f9;color:#1d4e89;text-align:left;padding:10px 8px;font-weight:700}
td{padding:15px 8px;border-bottom:1px solid #edf0f4;color:#2a3b52}
td:nth-child(4),td:nth-child(5){color:#a8b2c0}
.tot{display:flex;justify-content:space-between;margin-top:14px;background:#1d4e89;color:#fff;padding:14px 16px;border-radius:8px;font:700 18px Roboto}
.r{flex:1;display:flex;flex-direction:column;gap:16px}
.c{background:#fff;border-radius:20px;padding:24px 20px;display:flex;gap:14px;align-items:center;font:500 22px/1.35 Roboto;box-shadow:0 12px 26px rgba(20,39,62,.08)}
.c .ib{width:50px;height:50px;border-radius:14px;background:#ffe9dc;color:#f26b1d}
""", "<h1>A neat quotation<br><span>while the customer waits.</span></h1><div class=sub>For hardware, sanitary and building material shops.</div>",
f'''<div class=doc><div class=h><div><b>Your Hardware Store</b><small>Quotation · sample</small></div><div class=q>QUOTE<br><small>Valid 7 days</small></div></div>
<table><tr><th>#</th><th>Item</th><th>Qty</th><th>Rate</th><th>Amount</th></tr>{it}</table><div class=tot><span>Total</span><span>Auto-calculated</span></div></div>
<div class=r>''' + "".join(f'<div class=c><span class=ib>{ic(i,26)}</span>{t}</div>' for i,t in [("search","Pick items from your own price list"),("doc","Quotation PDF with your logo"),("send","Send it to the customer in one tap"),("cart","Turn it into a bill when they buy")]) + '</div>',
"#14273e", "Get your quotation app. DM us", "background:#f26b1d;color:#fff", bg="<div class=blue></div>", logo_color="#fff")

# ───────── 13 INDIA · Packers & movers · SINGLE · Bitter · cardboard/forest green
box = lambda w,h,lbl,x,y,z=1: f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;z-index:{z}"><div style="position:absolute;inset:0;background:linear-gradient(160deg,#d7a46a,#b97f43);border-radius:6px;box-shadow:0 24px 40px rgba(70,40,10,.3)"></div><div style="position:absolute;left:0;right:0;top:0;height:{h*0.16}px;background:#c48e52;border-radius:6px 6px 0 0"></div><i style="position:absolute;left:50%;top:0;bottom:0;width:{w*0.14}px;transform:translateX(-50%);background:rgba(240,220,170,.55)"></i><div style="position:absolute;left:12%;bottom:14%;right:12%;background:#fff;border-radius:6px;padding:8px 10px;display:flex;gap:8px;align-items:center;font:700 14px Bitter;color:#3a2a14"><span style="color:#1f5c3a">{ic("qr",28)}</span>{lbl}</div></div>'
P["p13_movers"] = page("""
body{--f:'Bitter';background:#f4ebdd;color:#2f2414}
h1{font-size:64px;font-weight:800;letter-spacing:-1px} h1 span{color:#1f5c3a}
.sub{color:#6e5c44;font-family:Poppins}
.vis{gap:26px}
.scene{position:relative;flex:1}
.ck{width:400px;flex:none;display:flex;flex-direction:column;gap:14px}
.lst{padding:6px 16px 16px;flex:1;display:flex;flex-direction:column;gap:9px}
.lst .t{font:700 20px Bitter;color:#2f2414;margin:6px 2px}
.lst .bar{height:12px;border-radius:6px;background:#e8e1d4;overflow:hidden}.lst .bar i{display:block;height:100%;width:94%;background:#1f5c3a}
.lst .row{display:flex;justify-content:space-between;align-items:center;padding:11px 12px;border-radius:12px;background:#f7f3ec;font:600 14px Poppins;color:#2f2414}
""", "<h1>Know every box,<br><span>from packing to delivery.</span></h1><div class=sub>A move-tracking app for packers and movers. Customers love the peace of mind.</div>",
'<div class=scene>' + box(290,250,"Box 12 · Kitchen",0,470,2) + box(250,220,"Box 07 · Books",260,500,3) + box(270,230,"Box 03 · Bedroom",40,250,1) + box(230,200,"Box 21 · Fragile",290,290,1) +
 '<div style="position:absolute;left:20px;top:0;background:#1f5c3a;color:#fff;border-radius:18px;padding:16px 20px;font:600 19px/1.4 Poppins;max-width:430px">Scan each box at packing, loading and delivery.</div></div>' +
 phone('<div class=lst><div class=t>Move · Sample family</div><span style="font:500 13px Poppins;color:#8a7a62">Surat → Pune · sample</span><div class=bar><i></i></div><span style="font:600 14px Poppins;color:#1f5c3a">32 of 34 boxes delivered</span>' + "".join(f'<div class=row><span>{a}</span><span style="color:{c}">{b}</span></div>' for a,b,c in [("Box 03 · Bedroom","Delivered","#1f5c3a"),("Box 07 · Books","Delivered","#1f5c3a"),("Box 12 · Kitchen","Delivered","#1f5c3a"),("Box 21 · Fragile","On the truck","#c07a1a"),("Box 22 · Fragile","On the truck","#c07a1a"),("Box 30 · TV","Delivered","#1f5c3a")]) + '</div>', w=380, h=760),
"#2f2414", "Want this for your moves? DM us", "background:#1f5c3a;color:#fff")

# ───────── 14 INDIA · Startup founder MVP · SINGLE · Archivo Black + Source Sans 3 · midnight/neon
ph_ = [("01","Talk","Your idea, your users, the one problem to solve."),("02","Plan","Only the screens that matter for version one."),("03","Build","A clean first version, ready for real users."),("04","Test","Real feedback from real people."),("05","Grow","Add features people actually ask for.")]
road = "".join(f'<div class=ph style="--y:{y}px"><span class=n>{n}</span><b>{a}</b><small>{b}</small></div>' for (n,a,b),y in zip(ph_,[260,170,90,170,40]))
P["p14_startup"] = page("""
body{--f:'Source Sans 3';--h:'Archivo Black';background:radial-gradient(900px 700px at 80% 20%,#3b1d78 0%,rgba(59,29,120,0) 60%),radial-gradient(700px 600px at 0% 100%,#0c4a5a 0%,rgba(12,74,90,0) 60%),#0b0920;color:#f2efff}
h1{font-size:54px;font-weight:400;letter-spacing:-.5px} h1 span{background:linear-gradient(90deg,#7cf0d0,#a98bff);-webkit-background-clip:text;color:transparent}
.sub{color:#bdb6e6;font-size:25px}
.vis{flex-direction:column;gap:18px}
.track{position:relative;flex:1}
.track svg{position:absolute;inset:0;width:100%;height:100%}
.ph{position:absolute;bottom:calc(var(--y) * 0 + 0px);width:176px;display:flex;flex-direction:column;gap:8px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.16);border-radius:20px;padding:18px 16px;backdrop-filter:blur(6px)}
.ph .n{font:400 30px 'Archivo Black';background:linear-gradient(90deg,#7cf0d0,#a98bff);-webkit-background-clip:text;color:transparent}
.ph b{font:700 24px 'Source Sans 3'}.ph small{font:400 17px/1.35 'Source Sans 3';color:#c9c2ef}
.note{display:flex;gap:16px;align-items:center;background:linear-gradient(90deg,rgba(124,240,208,.16),rgba(169,139,255,.16));border:1px solid rgba(255,255,255,.18);border-radius:20px;padding:18px 22px;font:600 21px/1.4 'Source Sans 3'}
.note .ib{width:50px;height:50px;border-radius:14px;background:#7cf0d0;color:#0b0920}
""", "<h1>Have a startup idea?<br><span>Start with a small first version.</span></h1><div class=sub>Build what matters, test it with real users, then grow.</div>",
f'''<div class=track><svg viewBox="0 0 952 520" preserveAspectRatio="none"><path d="M20 470 C 220 470, 220 330, 400 300 S 640 160, 930 60" fill="none" stroke="url(#g)" stroke-width="5" stroke-dasharray="2 14" stroke-linecap="round"/><defs><linearGradient id="g"><stop offset="0" stop-color="#7cf0d0"/><stop offset="1" stop-color="#a98bff"/></linearGradient></defs></svg>
''' + "".join(f'<div class=ph style="left:{x}px;top:{y}px"><span class=n>{n}</span><b>{a}</b><small>{b}</small></div>' for (n,a,b),(x,y) in zip(ph_,[(0,250),(190,180),(380,110),(570,170),(760,20)])) + f'''</div>
<div class=note><span class=ib>{ic("rocket",26)}</span>Web app, mobile app, or both. We help you choose what to build first.</div>''',
"#f2efff", "Share your idea with us", "background:linear-gradient(90deg,#7cf0d0,#a98bff);color:#0b0920", logo_color="#f2efff")

# ───────── 15 USA · Food truck · SINGLE · Archivo Black + Open Sans · teal/mustard retro
sched = [("MON","11 AM – 2 PM","Downtown Plaza"),("TUE","11 AM – 2 PM","Tech Park, Lot B"),("WED","5 PM – 9 PM","Riverside Market"),("THU","11 AM – 2 PM","City Hall Square"),("FRI","6 PM – 10 PM","Brewery Row")]
sr = "".join(f'<div class=sr{" on" if d=="WED" else ""}><b>{d}</b><span>{t}</span><em>{p}</em></div>' for d,t,p in sched)
P["p15_foodtruck"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#f6e7c4;color:#17433f}
.sun{position:absolute;left:50%;top:880px;width:900px;height:900px;transform:translateX(-50%);border-radius:50%;background:repeating-conic-gradient(#f3d48a 0 10deg,#f6e7c4 10deg 20deg);opacity:.7}
h1{font-size:60px;font-weight:400;letter-spacing:-.5px;line-height:1.2} h1 span{color:#d9472b}
.sub{color:#3f6a64}
.vis{gap:24px}
.l{flex:1;display:flex;flex-direction:column;gap:18px;min-width:0}
.map{flex:1;border-radius:24px;background:#d8ecd9;position:relative;overflow:hidden;box-shadow:0 20px 40px rgba(23,67,63,.15);border:4px solid #17433f}
.map i.rd{position:absolute;background:#fff}
.pin{position:absolute;width:44px;height:44px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);background:#d9472b;border:4px solid #fff;box-shadow:0 8px 14px rgba(0,0,0,.25)}
.pin.g{background:#17433f;width:34px;height:34px}
.tag{position:absolute;background:#17433f;color:#f6e7c4;border-radius:14px;padding:10px 14px;font:700 16px 'Open Sans'}
.truck{display:flex;align-items:flex-end;gap:0}
.sc{width:420px;flex:none;background:#17433f;border-radius:26px;padding:22px;color:#f6e7c4;display:flex;flex-direction:column;gap:10px}
.sc .t{font:400 26px 'Archivo Black';color:#f3c54a;margin-bottom:4px}
.sr{display:grid;grid-template-columns:62px 1fr;row-gap:2px;padding:20px 16px;border-radius:16px;background:rgba(255,255,255,.07)}
.sr b{grid-row:span 2;font:400 20px 'Archivo Black';color:#f3c54a;align-self:center}
.sr span{font:700 18px 'Open Sans'}.sr em{font:400 16px 'Open Sans';font-style:normal;color:#bcd6cf}
.sr.on{background:#d9472b}.sr.on b{color:#fff}.sr.on em{color:#ffe1d6}
.ft2{margin-top:auto;font:600 17px/1.4 'Open Sans';color:#bcd6cf}
""", "<h1>\"Where's the truck today?\"<br><span>Your website tells them.</span></h1><div class=sub>For food trucks across the US and Canada.</div>",
f'''<div class=l><div class=map><i class=rd style="left:0;right:0;top:40%;height:22px"></i><i class=rd style="left:30%;top:0;bottom:0;width:22px"></i><i class=rd style="left:68%;top:0;bottom:0;width:18px"></i><i class=rd style="left:0;right:0;top:78%;height:16px"></i>
<span class=pin style="left:44%;top:22%"></span><span class="pin g" style="left:12%;top:60%"></span><span class="pin g" style="left:78%;top:58%"></span><span class="pin g" style="left:80%;top:12%"></span>
<span class=tag style="left:52%;top:20%">Today · Riverside Market</span></div>
<div class="truck free"><div style="width:300px;height:150px;background:#d9472b;border-radius:18px 8px 8px 18px;position:relative"><i style="position:absolute;left:24px;top:22px;width:200px;height:56px;background:#f6e7c4;border-radius:8px"></i><i style="position:absolute;left:14px;right:60px;top:18px;height:10px;background:repeating-linear-gradient(90deg,#f3c54a 0 20px,#fff 20px 40px)"></i><span style="position:absolute;left:44px;top:34px;font:400 22px 'Archivo Black';color:#17433f">TACOS · SAMPLE</span><i style="position:absolute;left:40px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:#17433f;border:8px solid #9fb8b2"></i><i style="position:absolute;right:40px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:#17433f;border:8px solid #9fb8b2"></i></div><div style="width:110px;height:110px;background:#17433f;border-radius:6px 34px 8px 6px;position:relative"><i style="position:absolute;left:16px;top:16px;width:60px;height:40px;border-radius:6px;background:#9fd8e8"></i><i style="position:absolute;right:20px;bottom:-24px;width:48px;height:48px;border-radius:50%;background:#17433f;border:8px solid #9fb8b2"></i></div></div></div>
<div class=sc><div class=t>This week</div>{sr}<div class=ft2>Plus your menu, online orders and catering requests.</div></div>''',
"#17433f", "We build food truck sites. DM us", "background:#d9472b;color:#fff", bg="<div class=sun></div>")

# ───────── 16 USA · Dog groomer · SINGLE · Source Sans 3 + Crimson Text · lavender/coral
days = ["Mon","Tue","Wed","Thu","Fri"]
appts = {(0,0):("Buddy","Bath & trim","#ff8a7a"),(1,1):("Luna","Full groom","#9b8cff"),(2,0):("Max","Nail trim","#5ec8a8"),(3,2):("Daisy","Bath","#ffb84d"),(4,1):("Rocky","Full groom","#ff8a7a"),(0,2):("Coco","Puppy bath","#9b8cff"),(2,2):("Milo","Bath & trim","#ff8a7a"),(3,0):("Bella","De-shed","#5ec8a8")}
cal = '<div class=cal><div></div>' + "".join(f'<div class=dh>{d}</div>' for d in days)
for r,t in enumerate(["9 AM","11 AM","2 PM"]):
    cal += f'<div class=tm>{t}</div>' + "".join((lambda a: f'<div class=ap style="background:{a[2]}22;border-left:5px solid {a[2]}"><b>{a[0]}</b><small>{a[1]}</small></div>' if a else '<div class=fr>Open</div>')(appts.get((c,r))) for c in range(5))
cal += '</div>'
P["p16_doggroomer"] = page("""
body{--f:'Source Sans 3';--h:'Crimson Text';background:linear-gradient(160deg,#f3efff 0%,#ffe9e4 100%);color:#2b2340}
h1{font-size:68px;font-weight:700;letter-spacing:-.5px;line-height:1.18} h1 span{color:#e8604c;font-style:italic}
.sub{color:#5f5577}
.vis{flex-direction:column;gap:18px}
.cal{display:grid;grid-template-columns:80px repeat(5,1fr);gap:8px;background:#fff;border-radius:26px;padding:18px;box-shadow:0 22px 50px rgba(43,35,64,.12)}
.dh{font:700 17px 'Source Sans 3';text-align:center;color:#5f5577;padding:6px 0}
.tm{font:600 15px 'Source Sans 3';color:#8c84a3;display:flex;align-items:center}
.ap{border-radius:12px;padding:16px 12px;min-height:130px}.ap b{display:block;font:700 21px 'Source Sans 3'}.ap small{font:400 14px 'Source Sans 3';color:#5f5577}
.fr{border-radius:12px;border:2px dashed #e0daf0;min-height:130px;display:flex;align-items:center;justify-content:center;font:600 14px 'Source Sans 3';color:#b7aecd}
.bot{display:flex;gap:18px;align-items:flex-end;flex:1}
.pts{flex:1;display:flex;flex-direction:column;gap:12px;align-self:center}
.pt{display:flex;gap:14px;align-items:center;background:#fff;border-radius:18px;padding:18px 20px;font:600 23px 'Source Sans 3';box-shadow:0 10px 22px rgba(43,35,64,.07)}
.pt .ib{width:46px;height:46px;border-radius:14px;background:#ffe1dc;color:#e8604c}
""", "<h1>Pet parents book online.<br><span>You groom, not answer calls.</span></h1><div class=sub>Booking websites for dog groomers in the US and Canada.</div>",
cal + '<div class=bot>' + peep("Coffee","Smile","LongCurly",w=250,h=300) + '<div class=pts>' + "".join(f'<div class=pt><span class=ib>{ic(i,24)}</span>{t}</div>' for i,t in [("cal","Clients pick an open slot"),("paw","Each pet\'s notes and history saved"),("bell","Reminders cut no-shows")]) + '</div></div>',
"#2b2340", "Want online booking? DM us", "background:#2b2340;color:#fff")

# ───────── 17 USA · Cleaning company · CAROUSEL 6 · Open Sans · aqua/white sparkle
CL = """
body{--f:'Open Sans';background:linear-gradient(170deg,#e9fbfd 0%,#c9f1f6 100%);color:#073a4a}
h1{font-size:62px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#0ba5b8}
.sub{color:#3d6b78}
.k{font:700 16px 'Open Sans';letter-spacing:3px;color:#0ba5b8;margin-top:22px;text-transform:uppercase}
.sp{position:absolute;color:#7fe0ec}
.cd{background:#fff;border-radius:26px;box-shadow:0 22px 50px rgba(7,58,74,.12)}
"""
spk = lambda: "".join(f'<span class=sp style="left:{x}px;top:{y}px">{ic("spark",s,w=1.6)}</span>' for x,y,s in [(880,150,70),(960,260,40),(820,300,34)])
P["p17_cleaning_s1"] = page(CL+".vis{flex-direction:column;gap:18px}.vis{justify-content:space-between}.it{flex:1;display:flex;gap:22px;align-items:center;padding:24px 30px}.it .n{font:800 72px 'Open Sans';color:#0ba5b8;width:120px}.it b{display:block;font:700 32px 'Open Sans'}.it small{font:400 21px 'Open Sans';color:#3d6b78}",
 "<div class=k>Cleaning businesses · US &amp; Canada</div><h1 style='margin-top:10px'>Your website should do<br><span>these 4 things.</span></h1>",
 "".join(f'<div class="cd it"><span class=n>0{i+1}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,(a,b) in enumerate([("Instant quotes","By home size and service"),("Online booking","Pick a date and time"),("Before and after photos","Proof of your work"),("Your service areas","So locals know you cover them")])),
 "#073a4a", "Swipe", "background:#0ba5b8;color:#fff", bg=spk(), tagline="1 / 6")
def cslide(n, k, title, left, pts):
    return page(CL+".vis{gap:24px}.p{flex:1;display:flex;flex-direction:column;gap:14px;justify-content:center}.pt{display:flex;gap:16px;align-items:center;padding:20px 22px}.pt .ib{width:54px;height:54px;border-radius:16px;background:#dff7fa;color:#0ba5b8}.pt b{display:block;font:700 22px 'Open Sans'}.pt small{font:400 17px 'Open Sans';color:#3d6b78}",
      f"<div class=k>{k}</div><h1 style='margin-top:10px'>{title}</h1>", left + '<div class=p>' + "".join(f'<div class="cd pt"><span class=ib>{ic(i,26)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in pts) + '</div>',
      "#073a4a", "Swipe", "background:#fff;color:#073a4a", bg=spk(), tagline=f"{n} / 6")
opt = lambda lbl, ch: f'<div style="margin-bottom:12px"><div style="font:600 13px Open Sans;color:#888;margin-bottom:6px">{lbl}</div><div style="display:flex;gap:6px;flex-wrap:wrap">' + "".join(f'<span style="padding:9px 12px;border-radius:10px;font:600 14px Open Sans;background:{"#0ba5b8" if i==1 else "#eef6f8"};color:{"#fff" if i==1 else "#073a4a"}">{c}</span>' for i,c in enumerate(ch)) + '</div></div>'
P["p17_cleaning_s2"] = cslide(2, "Thing 01", "Give an instant quote<br><span>by home size.</span>",
 phone('<div style="padding:10px 18px 18px;flex:1;display:flex;flex-direction:column"><b style="font:700 20px Open Sans;color:#073a4a;margin-bottom:14px">Get your quote</b>' + opt("Bedrooms",["1","2","3","4+"]) + opt("Bathrooms",["1","2","3+"]) + opt("Service",["Standard","Deep clean","Move-out"]) + opt("How often",["Once","Weekly","Every 2 weeks"]) + '<div style="margin-top:auto;background:#073a4a;color:#fff;border-radius:16px;padding:16px;font:700 16px Open Sans;display:flex;justify-content:space-between"><span>Your price</span><span>Shown instantly</span></div></div>', w=370, h=740),
 [("dollar","Your own pricing rules","You set the rates, the site does the math."),("clock","No back-and-forth","Customers see a price right away."),("send","Quote saved as a lead","Even if they book later.")])
cg = "".join(f'<div style="aspect-ratio:1;border-radius:10px;display:flex;align-items:center;justify-content:center;font:700 15px Open Sans;{"background:#0ba5b8;color:#fff" if d==12 else ("background:#eef6f8;color:#073a4a" if d not in (3,8,14,17) else "color:#c3d3d8")}">{d}</div>' for d in range(1,22))
P["p17_cleaning_s3"] = cslide(3, "Thing 02", "Let clients book<br><span>a date and time online.</span>",
 '<div class=cd style="width:440px;flex:none;padding:24px;display:flex;flex-direction:column;gap:14px"><b style="font:700 22px Open Sans">Pick a date</b><div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px">' + "".join(f'<div style="text-align:center;font:700 12px Open Sans;color:#888">{d}</div>' for d in "SMTWTFS") + cg + '</div><b style="font:700 18px Open Sans;margin-top:6px">Available times</b><div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">' + "".join(f'<span style="padding:12px;border-radius:12px;text-align:center;font:600 15px Open Sans;{"background:#073a4a;color:#fff" if t=="10:00 AM" else "background:#eef6f8"}">{t}</span>' for t in ["8:00 AM","10:00 AM","1:00 PM","3:30 PM"]) + '</div><div style="margin-top:auto;background:#0ba5b8;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 16px Open Sans">Confirm booking</div></div>',
 [("cal","Only open slots show","No double bookings."),("bell","Automatic reminders","A text the day before."),("users","Teams get their list","Every morning, with addresses.")])
room = lambda clean: f'<div style="flex:1;border-radius:18px;overflow:hidden;position:relative;background:{"linear-gradient(#f4fbfc,#e3f2f5)" if clean else "linear-gradient(#e2ddd3,#cfc6b6)"}"><i style="position:absolute;left:0;right:0;bottom:0;height:34%;background:{"#cfe9ee" if clean else "#b9ae99"}"></i><i style="position:absolute;left:12%;bottom:22%;width:46%;height:28%;border-radius:10px;background:{"#7fd3df" if clean else "#9c8f78"}"></i><i style="position:absolute;right:12%;top:18%;width:22%;height:26%;border-radius:6px;background:{"#fff" if clean else "#d8d0c0"};box-shadow:inset 0 0 0 6px {"#bfe7ee" if clean else "#b3a892"}"></i>{"" if clean else "".join(f"<i style=&quot;position:absolute;left:{x}%;top:{y}%;width:{s}px;height:{s}px;border-radius:50%;background:rgba(90,70,40,.35)&quot;></i>" for x,y,s in [(20,70,16),(40,80,10),(65,75,20),(30,40,12),(75,60,14)])}{"".join(f"<span style=&quot;position:absolute;left:{x}%;top:{y}%;color:#0ba5b8&quot;>{ic('spark',s,w=1.8)}</span>" for x,y,s in [(60,30,40),(25,25,28),(80,70,30)]) if clean else ""}<span style="position:absolute;left:14px;top:14px;background:{"#0ba5b8" if clean else "#6b5f4a"};color:#fff;font:700 14px Open Sans;padding:7px 12px;border-radius:10px;letter-spacing:1px">{"AFTER" if clean else "BEFORE"}</span></div>'
P["p17_cleaning_s4"] = page(CL+".vis{flex-direction:column;gap:20px}.ba{flex:1;display:flex;gap:14px;background:#fff;border-radius:26px;padding:14px;box-shadow:0 22px 50px rgba(7,58,74,.12)}.row{display:flex;gap:14px}.row div{flex:1;display:flex;gap:12px;align-items:center;font:600 19px 'Open Sans'}.row .ib{width:46px;height:46px;border-radius:14px;background:#fff;color:#0ba5b8}",
 "<div class=k>Thing 03</div><h1 style='margin-top:10px'>Show your work with<br><span>before and after photos.</span></h1>",
 f'<div class=ba>{room(False)}{room(True)}</div><div class=row>' + "".join(f'<div><span class=ib>{ic(i,24)}</span>{t}</div>' for i,t in [("img","A gallery for each service"),("heart","Builds trust fast"),("upload","Your team adds photos from the job")]) + '</div>',
 "#073a4a", "Swipe", "background:#fff;color:#073a4a", bg=spk(), tagline="4 / 6")
zips = "".join(f'<span style="padding:18px 20px;border-radius:12px;font:700 19px Open Sans;background:{"#0ba5b8" if i%3!=2 else "#fff"};color:{"#fff" if i%3!=2 else "#9ab"};border:2px solid #0ba5b8">{z}</span>' for i,z in enumerate(["Area 01","Area 02","Area 03","Area 04","Area 05","Area 06","Area 07","Area 08","Area 09"]))
P["p17_cleaning_s5"] = cslide(5, "Thing 04", "Show the areas<br><span>you serve.</span>",
 '<div class=cd style="width:440px;flex:none;padding:24px;display:flex;flex-direction:column;gap:16px"><b style="font:700 22px Open Sans">Do we serve you?</b><div style="display:flex;gap:8px"><span style="flex:1;padding:14px;border-radius:12px;background:#eef6f8;font:600 16px Open Sans;color:#789">Enter your ZIP or postal code</span><span style="background:#073a4a;color:#fff;padding:14px 16px;border-radius:12px;font:700 15px Open Sans">Check</span></div><div style="display:flex;flex-wrap:wrap;gap:8px">' + zips + f'</div><div style="flex:1;border-radius:16px;background:#d9f1e3;position:relative;overflow:hidden;min-height:0"><i style="position:absolute;left:0;right:0;top:45%;height:14px;background:#fff"></i><i style="position:absolute;left:35%;top:0;bottom:0;width:14px;background:#fff"></i><i style="position:absolute;left:70%;top:0;bottom:0;width:10px;background:#fff"></i><i style="position:absolute;left:12%;top:10%;width:62%;height:76%;border-radius:40%;background:rgba(11,165,184,.18);border:3px dashed #0ba5b8"></i><span style="position:absolute;left:38%;top:34%;color:#0ba5b8">{ic("pin",44)}</span></div><div style="display:flex;gap:10px;align-items:center;background:#dff7fa;border-radius:14px;padding:14px;font:600 16px Open Sans;color:#073a4a"><span style="color:#0ba5b8">{ic("check",22,w=3)}</span>Yes! We clean in your area. Book now.</div></div>',
 [("pin","Locals find you in search","Area pages help you show up."),("x","Fewer wasted calls","Out-of-area visitors know right away."),("map","Grow area by area","Add new areas any time.")])
P["p17_cleaning_s6"] = page(CL+".vis{flex-direction:column;align-items:center;justify-content:center;gap:26px;text-align:center}.q{font:500 30px/1.45 'Open Sans';max-width:840px;color:#204f5c}.ch{display:flex;gap:12px;flex-wrap:wrap;justify-content:center}.ch span{background:#fff;border-radius:30px;padding:14px 22px;font:700 19px 'Open Sans';color:#0ba5b8;box-shadow:0 10px 22px rgba(7,58,74,.1)}",
 "<div class=k>Your turn</div><h1 style='margin-top:10px;text-align:center'>Want a website that books<br><span>cleaning jobs for you?</span></h1>",
 peep("ArmsCrossed","Smile","ShortCurly",w=360,h=380) + '<div class=q>Tell us your services and the areas you cover. We build websites for cleaning companies in the US and Canada.</div><div class=ch><span>Quotes</span><span>Booking</span><span>Photos</span><span>Service areas</span></div>',
 "#073a4a", "DM us to start", "background:#0ba5b8;color:#fff", bg=spk(), tagline="6 / 6")

# ───────── 18 USA · Auto repair shop · SINGLE · Anton + Inter · red/charcoal
insp = [("Brake pads","Replace soon","#ffb020"),("Tires","Good","#2ecc71"),("Battery","Replace now","#ff4d4d"),("Oil","Good","#2ecc71"),("Wipers","Replace soon","#ffb020")]
ir = "".join(f'<div class=ir><span class=th style="background:linear-gradient(135deg,#3a3f47,#23272d)">{ic("camera",22)}</span><div><b>{a}</b><small>{b}</small></div><span class=dot style="background:{c}"></span><span class=ok>{"Approve" if c!="#2ecc71" else "OK"}</span></div>' for a,b,c in insp)
P["p18_autorepair"] = page("""
body{--f:'Inter';--h:'Anton';background:#191b1f;color:#f3f3f1}
.stripe{position:absolute;right:-120px;top:-60px;width:520px;height:1500px;background:#e0292c;transform:rotate(14deg)}
h1{font-size:70px;font-weight:400;text-transform:uppercase;letter-spacing:.5px;line-height:1.2} h1 span{color:#ff5a4f}
.sub{color:#b5b8bf;width:640px}
.vis{gap:26px;align-items:center}
.tab{width:520px;flex:none;border-radius:34px;padding:16px;background:#0e0f12;box-shadow:0 0 0 2px #3a3d46,0 40px 80px rgba(0,0,0,.6)}
.tab .s{background:#f6f6f4;border-radius:22px;padding:22px;color:#191b1f;display:flex;flex-direction:column;gap:10px}
.tab .hd{display:flex;justify-content:space-between;align-items:center;font:700 20px Inter}
.tab .hd small{font:500 13px Inter;color:#888}
.ir{display:flex;align-items:center;gap:12px;background:#fff;border-radius:14px;padding:12px;box-shadow:0 3px 8px rgba(0,0,0,.05)}
.ir .th{width:54px;height:54px;border-radius:12px;color:#aaa;display:flex;align-items:center;justify-content:center;flex:none}
.ir div{flex:1}.ir b{display:block;font:700 17px Inter}.ir small{font:500 14px Inter;color:#777}
.ir .dot{width:14px;height:14px;border-radius:50%}
.ir .ok{font:700 13px Inter;padding:8px 12px;border-radius:10px;background:#191b1f;color:#fff}
.tot{background:#e0292c;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 17px Inter}
.r{flex:1;display:flex;flex-direction:column;gap:16px;z-index:2}
.c{background:#24272d;border-radius:20px;padding:20px;display:flex;gap:14px;align-items:center;font:600 20px/1.35 Inter}
.c .ib{width:48px;height:48px;border-radius:14px;background:#e0292c;color:#fff}
""", "<h1>Show what's wrong.<br><span>Get approvals by text.</span></h1><div class=sub>Digital inspections for auto repair shops in the US and Canada.</div>",
f'''<div class=tab><div class=s><div class=hd>Vehicle inspection<small>Sample · 2019 sedan</small></div>{ir}<div class=tot>Send to customer</div></div></div>
<div class=r>''' + "".join(f'<div class=c><span class=ib>{ic(i,24)}</span>{t}</div>' for i,t in [("camera","Photo of every issue"),("chat","Customer approves from their phone"),("bell","\"Your car is ready\" text"),("doc","History saved for next visit")]) + '</div>',
"#f3f3f1", "Want this for your shop? DM us", "background:#fff;color:#191b1f", bg="<div class=stripe></div>", logo_color="#f3f3f1")

# ───────── 19 CANADA/USA · Coffee shop loyalty · SINGLE · Cardo + Inter · espresso/latte/cream
cups = "".join(f'<div class=cp style="background:{"#6b3f24" if i<7 else "transparent"};border:2px {"solid #6b3f24" if i<7 else "dashed #c9b39a"};color:{"#f7ecdf" if i<7 else "#c9b39a"}">{ic("cup",22)}</div>' for i in range(10))
P["p19_coffee"] = page("""
body{--f:'Inter';--h:'Cardo';background:#f4ebe0;color:#2e1a10}
.circ{position:absolute;right:-220px;top:300px;width:760px;height:760px;border-radius:50%;background:#e7d5c0}
.ring{position:absolute;right:-120px;top:400px;width:560px;height:560px;border-radius:50%;border:2px solid #d6bfa5}
h1{font-size:72px;font-weight:700;letter-spacing:-1px;line-height:1.15} h1 span{color:#a0522d;font-style:italic}
.sub{color:#6e5443}
.vis{gap:34px;align-items:center}
.l{flex:1;display:flex;flex-direction:column;gap:18px;z-index:2}
.it{display:flex;gap:16px;align-items:flex-start}
.it .ib{width:62px;height:62px;border-radius:50%;background:#2e1a10;color:#f4ebe0}
.l{gap:30px!important}.it b{display:block;font:700 36px Cardo}.it small{display:block;font:400 22px/1.45 Inter;color:#6e5443;margin-top:2px}
.cp{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center}
""", "<h1>Turn first-time visitors<br><span>into regulars.</span></h1><div class=sub>A simple app for coffee shops and cafés in Canada and the US.</div>",
'<div class=l>' + "".join(f'<div class=it><span class=ib>{ic(i,24)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("grid","Digital stamp card","No paper cards to lose."),("cup","Order ahead","Skip the line, pick up and go."),("bell","Your news, their phone","New drinks, new hours, events.")]) + '</div>' +
 phone(f'<div style="padding:6px 18px 16px;flex:1;display:flex;flex-direction:column;gap:10px;background:#fbf6f0;min-height:0"><b style="font:700 26px Cardo;color:#2e1a10">Your Café</b><span style="font:500 13px Inter;color:#9a8572;margin-top:-10px">Rewards · sample</span><div style="background:#2e1a10;color:#f4ebe0;border-radius:20px;padding:18px"><div style="font:600 15px Inter;opacity:.8">Your card</div><div style="font:700 26px Cardo;margin:4px 0 14px">7 of 10 stamps</div><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;justify-items:center">{cups.replace("#6b3f24","#c98b5a").replace("dashed #c9b39a","dashed #8c6a52")}</div></div><div style="background:#fff;border-radius:16px;padding:14px;display:flex;justify-content:space-between;align-items:center;font:600 15px Inter"><span>Oat latte · Medium</span><span style="background:#a0522d;color:#fff;padding:8px 12px;border-radius:10px;font-size:13px">Order ahead</span></div><div style="background:#fff;border-radius:16px;padding:14px;font:500 14px/1.4 Inter;color:#6e5443"><b style="color:#2e1a10">New this week</b><br>Cinnamon cold brew is here.</div><div style="font:700 15px Inter;color:#2e1a10;margin-top:4px">Quick order</div><div style="background:#fff;border-radius:14px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center;font:600 14px Inter;color:#2e1a10"><span>Cappuccino</span><span style="width:28px;height:28px;border-radius:8px;background:#f1e3d3;color:#a0522d;text-align:center;line-height:28px;font-size:18px">+</span></div><div style="background:#fff;border-radius:14px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center;font:600 14px Inter;color:#2e1a10"><span>Cold brew</span><span style="width:28px;height:28px;border-radius:8px;background:#f1e3d3;color:#a0522d;text-align:center;line-height:28px;font-size:18px">+</span></div><div style="background:#fff;border-radius:14px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center;font:600 14px Inter;color:#2e1a10"><span>Butter croissant</span><span style="width:28px;height:28px;border-radius:8px;background:#f1e3d3;color:#a0522d;text-align:center;line-height:28px;font-size:18px">+</span></div><div style="margin-top:auto;background:#a0522d;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 15px Inter">Pick up in 10 min</div></div>', w=380, h=760, style="z-index:2"),
"#2e1a10", "Want one for your café? DM us", "background:#2e1a10;color:#f4ebe0", bg="<div class=circ></div><div class=ring></div>")

# ───────── 20 USA · Lawn care · SINGLE · Bitter? -> Montserrat? use Fira? -> 'Source Sans 3' bold + grass/sky · weekly route board
jobs = [("Mon","Route A","8 homes"),("Tue","Route B","7 homes"),("Wed","Route C","9 homes"),("Thu","Route A","8 homes"),("Fri","Route D","6 homes")]
jb = "".join(f'<div class=jb><b>{d}</b><span>{r}</span><em>{h}</em><i style="width:{int(h.split()[0])*10}%"></i></div>' for d,r,h in jobs)
P["p20_lawncare"] = page("""
body{--f:'Fira Sans';background:linear-gradient(180deg,#e4f4ff 0%,#f3fbff 55%,#e7f6e1 100%);color:#16331c}
.hill{position:absolute;left:-100px;right:-100px;bottom:-560px;height:900px;border-radius:50%;background:#7cc46a}
.hill2{position:absolute;left:300px;right:-300px;bottom:-640px;height:900px;border-radius:50%;background:#5aa84c}
h1{font-size:62px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#2f8a3b}
.sub{color:#456451}
.vis{gap:22px;align-items:stretch}
.bd{flex:1;background:#fff;border-radius:26px;padding:24px;box-shadow:0 22px 50px rgba(22,51,28,.14);display:flex;flex-direction:column;gap:12px}
.bd .t{display:flex;justify-content:space-between;font:700 22px 'Fira Sans'}.bd .t small{font:500 14px 'Fira Sans';color:#7a8f7f}
.jb{display:grid;grid-template-columns:60px 1fr auto;align-items:center;gap:10px 12px;background:#f3f8f1;border-radius:16px;padding:20px 18px}
.jb b{font:700 18px 'Fira Sans';color:#2f8a3b}.jb span{font:600 18px 'Fira Sans'}.jb em{font:500 15px 'Fira Sans';font-style:normal;color:#5d7563}
.jb i{grid-column:1/-1;height:8px;border-radius:4px;background:linear-gradient(90deg,#7cc46a,#2f8a3b)}
.r{width:380px;flex:none;display:flex;flex-direction:column;gap:14px}
.c{background:#16331c;color:#eaf6e4;border-radius:22px;padding:20px;display:flex;flex-direction:column;gap:8px}
.c .ib{width:46px;height:46px;border-radius:14px;background:#7cc46a;color:#16331c}
.c{flex:1;justify-content:center}.c b{font:700 23px 'Fira Sans'}.c small{font:400 18px/1.4 'Fira Sans';color:#b9d4b4}
""", "<h1>Recurring lawn jobs,<br><span>scheduled and billed on their own.</span></h1><div class=sub>Software for lawn care and landscaping companies in the US and Canada.</div>",
f'<div class=bd><div class=t>This week\'s routes<small>Sample</small></div>{jb}<div style="margin-top:auto;display:flex;gap:10px"><span style="flex:1;background:#2f8a3b;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 16px Fira Sans">Send crew lists</span><span style="flex:1;background:#eaf6e4;color:#2f8a3b;border-radius:14px;padding:14px;text-align:center;font:700 16px Fira Sans">Send invoices</span></div></div>' +
 '<div class=r>' + "".join(f'<div class=c><span class=ib>{ic(i,24)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("cal","Weekly or bi-weekly","Jobs repeat by themselves."),("map","Smart routes","Crews know where to go next."),("dollar","Auto invoices","Sent when a job is marked done.")]) + '</div>',
"#16331c", "Want this for your crew? DM us", "background:#16331c;color:#eaf6e4", bg="<div class=hill></div><div class=hill2></div>")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
