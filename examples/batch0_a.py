import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 01 INDIA · Boutique / ladies tailor · SINGLE · Lora + Inter · blush/maroon
meas = [("Length","42 in"),("Shoulder","14.5 in"),("Sleeve","18 in"),("Waist","30 in"),("Neck style","Round, deep back")]
mrows = "".join(f'<div style="display:flex;justify-content:space-between;padding:13px 14px;border-radius:12px;background:#fbf3f1;margin-bottom:8px;font:500 15px Inter;color:#3b1420"><span>{a}</span><b style="font-weight:700">{b}</b></div>' for a,b in meas)
P["p01_boutique"] = page("""
body{--f:'Inter';--h:'Lora';background:radial-gradient(900px 700px at 100% 0%,#ffd9d2 0%,rgba(255,217,210,0) 60%),#fbefe9;color:#3b1420}
h1{font-size:66px;font-weight:700;letter-spacing:-1px} h1 i{color:#a2264f}
.sub{color:#7d4a57}
.vis{gap:30px;align-items:stretch}
.lft{flex:1;display:flex;flex-direction:column;justify-content:space-between;min-width:0}
.slip{background:#fffdf6 repeating-linear-gradient(transparent 0 37px,#eadfca 37px 38px);border-radius:8px;padding:26px 26px 20px;transform:rotate(-3deg);box-shadow:0 22px 40px rgba(90,30,40,.16);font-family:'Gelasio';font-style:italic;color:#6b4a2e;position:relative}
.slip b{display:block;font:700 22px 'Inter';font-style:normal;color:#3b1420;margin-bottom:10px;letter-spacing:.3px}
.slip p{font-size:26px;line-height:44px}.slip{background-size:100% 44px!important}
.slip s{color:#b33}
.slip .torn{position:absolute;right:16px;top:16px;background:#a2264f;color:#fff;font:700 14px Inter;font-style:normal;padding:7px 12px;border-radius:20px;transform:rotate(6deg)}
.note{display:flex;gap:16px;align-items:center}
.note .bub{background:#fff;border-radius:20px;padding:16px 18px;font:600 20px/1.35 Inter;box-shadow:0 14px 30px rgba(90,30,40,.12)}
.ap{padding:8px 18px 18px;flex:1;display:flex;flex-direction:column}
.ap .hd{display:flex;gap:12px;align-items:center;margin:8px 0 16px}
.ap .av{width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,#f6b7c6,#a2264f);color:#fff;font:700 20px/52px Inter;text-align:center}
.ap .hd b{font:700 19px Inter;color:#111;display:block}.ap .hd small{font:400 13px Inter;color:#888}
.ap .tg{display:flex;gap:8px;margin-bottom:14px}.ap .tg span{font:600 12px Inter;padding:6px 10px;border-radius:10px;background:#f6e3e7;color:#a2264f}
.ap .bt{margin-top:auto;background:#a2264f;color:#fff;border-radius:14px;padding:15px;text-align:center;font:600 16px Inter}
""", "<h1>Every customer's measurements,<br><i>saved forever.</i></h1><div class=sub>No more lost slips. Open any regular's details in seconds.</div>",
f'''<div class=lft><div class=slip><span class=torn>Slip lost?</span><b>Order slip</b><p>Mrs. ____ &nbsp;blouse<br>Length <s>40</s> 42 &nbsp;Sleeve 18?<br>Waist 30 ... check again<br>Delivery: Friday?</p></div>
<div class=note>{peep("Paper","Smile","Bun",w=260,h=300)}<div class=bub>"Same as last time, please."<br><span style="font-weight:400;color:#7d4a57;font-size:17px">Now you can say yes, instantly.</span></div></div></div>
{phone(f'<div class=ap><div class=hd><div class=av>R</div><div><b>Regular customer</b><small>Sample profile · 14 orders</small></div></div><div class=tg><span>Blouse</span><span>Kurti</span><span>Lehenga</span></div>{mrows}<div class=bt>New order with these details</div></div>', w=380, h=760)}''',
"#3b1420", "Get your boutique app. DM us", "background:#a2264f;color:#fff")

# ───────── 02 INDIA · Bakery & sweet shop · CAROUSEL 5 · Montserrat · indigo/saffron
BK = """
body{--f:'Montserrat';background:linear-gradient(170deg,#211c58 0%,#14113a 100%);color:#fff}
h1{font-size:62px;font-weight:800} h1 span{color:#ffb43a}
.sub{color:#c9c4f2}
.sn{font:700 17px Montserrat;letter-spacing:3px;color:#ffb43a;margin-top:22px}
.card{background:#fff;color:#1b1840;border-radius:26px;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.pill{display:inline-flex;gap:10px;align-items:center;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16);border-radius:40px;padding:12px 20px;font:600 20px Montserrat;color:#fff}
.pill .ib{width:34px;height:34px;border-radius:50%;background:#ffb43a;color:#211c58}
"""
cake = lambda c1,c2,s=1: f'<div style="width:{150*s}px;flex:none;display:flex;flex-direction:column;align-items:center"><div style="width:{14*s}px;height:{26*s}px;background:#fff3c4;border-radius:4px;margin-bottom:-2px;box-shadow:0 -8px 14px rgba(255,200,80,.6)"></div><div style="width:{110*s}px;height:{60*s}px;border-radius:{14*s}px {14*s}px 6px 6px;background:linear-gradient({c1},{c2});box-shadow:inset 0 -10px 0 rgba(0,0,0,.08)"></div><div style="width:{150*s}px;height:{70*s}px;border-radius:{14*s}px {14*s}px 8px 8px;background:linear-gradient({c2},{c1});margin-top:-4px;position:relative;box-shadow:inset 0 -12px 0 rgba(0,0,0,.08)"><i style="position:absolute;left:0;right:0;top:6px;height:{14*s}px;background:repeating-radial-gradient(circle at 10px 0,#fff 0 6px,transparent 7px 20px)"></i></div><div style="width:{190*s}px;height:{12*s}px;border-radius:50%;background:rgba(255,255,255,.25);margin-top:4px"></div></div>'
P["p02_bakery_s1"] = page(BK+".vis{flex-direction:column;align-items:center;justify-content:center;gap:34px}.row{display:flex;gap:30px;align-items:flex-end}.chips{display:flex;flex-wrap:wrap;gap:14px;justify-content:center}",
 "<div class=sn>BAKERY &amp; SWEET SHOP</div><h1 style='margin-top:10px'>Cake orders on paper slips?<br><span>Here's a calmer way.</span></h1>",
 f'<div class=row>{cake("#ffd1dc","#ff8fb1",1.3)}{cake("#ffe7b0","#ffb43a",1.8)}{cake("#cfe3ff","#7aa7ff",1.3)}</div><div class=chips>' + "".join(f'<span class=pill><span class=ib>{ic(i,18,w=2.4)}</span>{t}</span>' for i,t in [("cal","Pre-orders"),("doc","Daily bake list"),("box","Counter stock"),("bell","Ready alerts")]) + '</div>',
 "#fff", "Swipe", "background:#ffb43a;color:#211c58", tagline="1 / 5")
def bslide(n, title, sub, left, right):
    return page(BK+".vis{gap:26px;align-items:stretch}.l{flex:1;display:flex;flex-direction:column;gap:16px;justify-content:center;min-width:0}.pt{display:flex;gap:16px;align-items:center;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:22px;padding:20px 22px}.pt .ib{width:52px;height:52px;border-radius:16px;background:#ffb43a;color:#211c58}.pt b{display:block;font:700 22px/1.3 Montserrat}.pt small{display:block;font:500 17px/1.4 Montserrat;color:#c9c4f2;margin-top:3px}",
      f"<div class=sn>STEP {n-1} OF 3</div><h1 style='margin-top:10px;font-size:58px'>{title}</h1><div class=sub>{sub}</div>", left+right, "#fff", "Swipe", "background:rgba(255,255,255,.12);color:#fff", tagline=f"{n} / 5")
pts = lambda L: '<div class=l>' + "".join(f'<div class=pt><span class=ib>{ic(i,26)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in L) + '</div>'
P["p02_bakery_s2"] = bslide(2, "Take cake pre-orders<br><span>with photo and date.</span>", "Every order saved, nothing missed on a busy day.",
 phone('<div style="padding:8px 18px 18px;display:flex;flex-direction:column;gap:12px;flex:1"><b style="font:700 20px Montserrat;color:#1b1840">New cake order</b><div style="height:150px;border-radius:16px;background:linear-gradient(135deg,#ffd1dc,#ff8fb1);display:flex;align-items:center;justify-content:center;color:#fff;font:700 15px Montserrat">Design photo · sample</div>' + "".join(f'<div style="display:flex;justify-content:space-between;padding:12px 14px;border-radius:12px;background:#f4f2fb;font:600 15px Montserrat;color:#1b1840"><span style="color:#777;font-weight:500">{a}</span>{b}</div>' for a,b in [("Flavour","Chocolate"),("Weight","1 kg"),("Message","Happy Birthday"),("Pickup","Sat, 6 PM"),("Advance","Paid")]) + '<div style="margin-top:auto;background:#211c58;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 15px Montserrat">Save order</div></div>', w=360, h=740),
 pts([("img","Design photo attached","No confusion on the day."),("cal","Pickup date and time","Sorted by day automatically."),("rupee","Advance noted","Balance shown at pickup.")]))
P["p02_bakery_s3"] = bslide(3, "Know exactly what<br><span>to bake today.</span>", "The bake list builds itself from orders and counter sales.",
 '<div class="card" style="width:430px;flex:none;padding:26px;display:flex;flex-direction:column;gap:12px"><b style="font:800 24px Montserrat">Today\'s bake list</b><span style="font:500 14px Montserrat;color:#888;margin-top:-8px">Saturday · sample</span>' + "".join(f'<div style="display:flex;align-items:center;gap:14px;padding:13px;border-radius:14px;background:#f6f4fd"><span style="width:44px;height:44px;border-radius:12px;background:{c};flex:none"></span><div style="flex:1;font:700 17px Montserrat">{a}<div style="font:500 13px Montserrat;color:#888">{b}</div></div><b style="font:800 20px Montserrat;color:#211c58">{q}</b></div>' for a,b,q,c in [("Chocolate cake","4 orders + counter","6","#7a4a2e"),("Pineapple pastry","Counter","24","#ffd34d"),("Kaju katli","2 bulk orders","5 kg","#f1e2c6"),("Bread loaves","Daily","40","#e8b97a"),("Cookies","Counter","3 trays","#c98a4b")]) + '</div>',
 pts([("doc","One clear list","For the kitchen every morning."),("chart","Less waste","Bake what will actually sell."),("users","Staff stay in sync","Everyone sees the same list.")]))
P["p02_bakery_s4"] = bslide(4, "Tell customers<br><span>their order is ready.</span>", "A short message goes out the moment you mark it done.",
 phone('<div style="padding:10px 16px;display:flex;flex-direction:column;gap:12px;flex:1;background:#f2f1f8"><b style="font:700 18px Montserrat;color:#1b1840;margin:6px 4px">Messages</b>' + "".join(f'<div style="background:#fff;border-radius:16px;padding:14px;font:500 15px/1.4 Montserrat;color:#222;box-shadow:0 4px 10px rgba(0,0,0,.05)"><b style="display:block;font:700 14px Montserrat;color:#211c58;margin-bottom:4px">Your Bakery · {t}</b>{m}</div>' for t,m in [("Thu 10:02 AM","Order received. Chocolate cake, 1 kg, pickup Sat 6 PM."),("Sat 9:00 AM","Reminder: your cake will be ready by 6 PM today."),("Sat 5:20 PM","Your cake is ready! See you soon."),("Sat 6:15 PM","Thank you! Hope the party goes well."),("Next month","Your regular order? Tap to repeat.")]) + '</div>', w=360, h=740),
 pts([("bell","Ready alerts","No calls asking 'is it ready?'"),("heart","Feels personal","Customers love the care."),("users","Regulars come back","Their order history is saved.")]))
P["p02_bakery_s5"] = page(BK+".vis{flex-direction:column;align-items:center;justify-content:center;gap:28px;text-align:center}.q{font:600 30px/1.45 Montserrat;color:#e6e2ff;max-width:820px}",
 "<div class=sn>YOUR TURN</div><h1 style='margin-top:10px'>Want this for your<br><span>bakery or sweet shop?</span></h1>",
 cake("#ffe7b0","#ffb43a",2.2) + "<div class=q>Tell us what you sell and how you take orders today. We'll plan an app that fits your shop.</div>",
 "#fff", "DM us to start", "background:#ffb43a;color:#211c58", tagline="5 / 5")

# ───────── 03 INDIA · Gym · SINGLE · Archivo Black + Inter · black/neon lime · spot-the-problem
P["p03_gym"] = page("""
body{--f:'Inter';--h:'Archivo Black';background:#0c0d0c;color:#f1f5ea}
.lime{position:absolute;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,rgba(198,255,61,.22),rgba(198,255,61,0) 65%);left:-150px;bottom:120px}
h1{font-size:64px;font-weight:400;text-transform:uppercase;letter-spacing:0;line-height:1.18} h1 span{color:#c6ff3d}
.sub{color:#a6b09a}
.vis{gap:24px;align-items:stretch}
.reg{flex:1;background:#f4efe2;border-radius:14px;padding:22px;color:#3a3326;position:relative;transform:rotate(-1.5deg);box-shadow:0 30px 60px rgba(0,0,0,.5)}
.reg b{font:700 22px Inter;display:block;margin-bottom:12px}
.rw{display:flex;align-items:center;gap:12px;border-bottom:1px solid #d8cfb8;padding:15px 8px;font:500 19px 'Gelasio';font-style:italic;position:relative}.rw .n{font:500 15px Inter;font-style:normal;color:#8a7f66;width:28px}.rw .tx{flex:1}.rw.bad .tx{outline:3px solid #ff4b3e;outline-offset:4px;border-radius:30px}.rw .lbl{position:static!important}
.reg td{border-bottom:1px solid #d8cfb8;padding:12px 6px}
.reg td:first-child{font-style:normal;font-family:Inter;color:#8a7f66;width:40px}

.lbl{background:#ff4b3e;color:#fff;font:700 15px Inter;padding:7px 12px;border-radius:12px;white-space:nowrap}
.app{width:400px;flex:none;background:#171a15;border:1px solid #2b3125;border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:12px}
.app .t{font:700 22px Inter;display:flex;justify-content:space-between;align-items:center}
.app .t span{font:600 12px Inter;color:#0c0d0c;background:#c6ff3d;padding:5px 10px;border-radius:10px}
.m{display:flex;align-items:center;gap:12px;background:#20241d;border-radius:16px;padding:18px 14px}
.m .av{width:42px;height:42px;border-radius:50%;background:#2f3a24;color:#c6ff3d;font:700 16px/42px Inter;text-align:center;flex:none}
.m div{flex:1;font:600 16px Inter}.m small{display:block;font:400 13px Inter;color:#8e9a80}
.m em{font:700 12px Inter;font-style:normal;padding:5px 9px;border-radius:10px}
.ask{margin-top:auto;background:#c6ff3d;color:#0c0d0c;border-radius:18px;padding:16px 18px;font:700 19px/1.35 Inter}
""", "<h1>Spot the 3 problems<br>in this <span>gym register.</span></h1><div class=sub>Then see how a simple gym app fixes all three.</div>",
f'''<div class=reg><b>Members · Nov</b>{"".join(f'<div class="rw{" bad" if t else ""}"><span class=n>{n}</span><span class=tx>{a}</span>{f'<span class=lbl>{t}</span>' if t else ''}</div>' for n,a,t in [("01","Member A · paid till 30th",""),("02","Member B · fees ??? ask","1 · Fees unclear"),("03","Member C · 7 AM trainer","2 · Slot clash"),("04","Member D · 7 AM trainer","2 · Slot clash"),("05","Member E · not seen 3 weeks","3 · Who stopped?"),("06","Member F · paid till 15th",""),("07","Member G · paid ... cash?",""),("08","Member H · 6 PM batch","")])}</div>
<div class=app><div class=t>Gym app<span>SAMPLE</span></div>
<div class=m><div class=av>B</div><div>Member B<small>Fee due on 5th</small></div><em style="background:#3a2f12;color:#ffcf4a">REMINDER SENT</em></div>
<div class=m><div class=av>C</div><div>7 AM · Trainer 1<small>Member C booked</small></div><em style="background:#203a1c;color:#c6ff3d">BOOKED</em></div>
<div class=m><div class=av>D</div><div>8 AM · Trainer 1<small>Member D moved</small></div><em style="background:#203a1c;color:#c6ff3d">BOOKED</em></div>
<div class=m><div class=av>E</div><div>Member E<small>No visit in 21 days</small></div><em style="background:#3a1c1c;color:#ff8a80">CHECK IN</em></div>
<div class=ask>Which one happens at your gym? Tell us in the comments.</div></div>''',
"#f1f5ea", "Want a gym app? DM us", "background:#c6ff3d;color:#0c0d0c", bg="<div class=lime></div>", logo_color="#f1f5ea")

# ───────── 04 INDIA · Real estate broker · SINGLE · DM Sans · navy/gold/ivory
bld = lambda c1,c2: f'<div style="height:230px;border-radius:14px 14px 0 0;background:linear-gradient(180deg,#bfe0ff,#e9f4ff);position:relative;overflow:hidden"><i style="position:absolute;left:18%;bottom:0;width:30%;height:78%;background:linear-gradient({c1},{c2});border-radius:4px 4px 0 0;background-image:repeating-linear-gradient(0deg,transparent 0 14px,rgba(255,255,255,.55) 14px 20px),linear-gradient({c1},{c2})"></i><i style="position:absolute;left:52%;bottom:0;width:26%;height:58%;border-radius:4px 4px 0 0;background-image:repeating-linear-gradient(0deg,transparent 0 12px,rgba(255,255,255,.5) 12px 18px),linear-gradient({c2},{c1})"></i><i style="position:absolute;left:0;right:0;bottom:0;height:16px;background:#8fd18a"></i></div>'
props = [("2 BHK Flat","Sample Nagar · 1,050 sq ft","#0b1f3a","#2d4d7c","Ready to move"),("Shop · Ground floor","Main road · 320 sq ft","#7a5a1f","#d4a64a","Rent"),("Plot · 200 sq yd","Sample Ring Road","#2f6b4f","#6bbf8e","Sale")]
pc = "".join(f'<div style="flex:1;border-radius:14px;overflow:hidden;background:#fff;border:1px solid #e8e3d6">{bld(c1,c2)}<div style="padding:12px 14px"><span style="font:700 11px DM Sans;letter-spacing:1px;color:#d4a64a;text-transform:uppercase">{t}</span><b style="display:block;font:700 17px DM Sans;color:#0b1f3a;margin:4px 0 2px">{a}</b><small style="font:400 13px DM Sans;color:#7a7f8c">{b}</small></div></div>' for a,b,c1,c2,t in props)
P["p04_realestate"] = page("""
body{--f:'DM Sans';background:#f7f3ea;color:#0b1f3a}
.navy{position:absolute;left:0;right:0;bottom:0;height:420px;background:#0b1f3a}
h1{font-size:64px;letter-spacing:-2px} h1 span{color:#b8862e}
.sub{color:#56627a}
.vis{flex-direction:column;gap:22px}
.chips{display:flex;gap:10px;padding:16px 18px 6px}.chips span{font:600 14px DM Sans;padding:8px 14px;border-radius:20px;background:#f2eee4;color:#0b1f3a}.chips span:first-child{background:#0b1f3a;color:#fff}
.feat{display:flex;gap:16px}
.feat{flex:1;align-items:center}.f{flex:1;display:flex;flex-direction:column;gap:14px;align-items:flex-start;color:#f7f3ea;font:600 23px/1.35 'DM Sans'}
.f .ib{width:64px;height:64px;border-radius:20px;background:#d4a64a;color:#0b1f3a}
""", "<h1>Buyers want to see it<br><span>before they call you.</span></h1><div class=sub>A listing website shows every flat, shop and plot with photos and location.</div>",
 browser(f'<div class=chips><span>All</span><span>2 BHK</span><span>3 BHK</span><span>Shops</span><span>Plots</span></div><div style="display:flex;gap:14px;padding:12px 18px 18px">{pc}</div><div style="margin:0 18px 18px;display:flex;gap:12px;align-items:center;background:#0b1f3a;border-radius:14px;padding:14px 16px;color:#fff;font:600 15px DM Sans"><span style="color:#d4a64a">{ic("pin",22)}</span>See on map<span style="margin-left:auto;background:#d4a64a;color:#0b1f3a;padding:8px 14px;border-radius:10px">Book a site visit</span></div>', url="yourproperties.in · sample") +
 '<div class=feat>' + "".join(f'<div class=f><span class=ib>{ic(i,24)}</span>{t}</div>' for i,t in [("img","Photos and videos of every listing"),("pin","Exact location on the map"),("cal","Site visits booked online")]) + '</div>',
 "#0b1f3a", "Get your listing website. DM us", "background:#d4a64a;color:#0b1f3a", bg="<div class=navy></div>", logo_color="#f7f3ea")

# ───────── 05 INDIA · Restaurant direct ordering · SINGLE · Anton + Poppins · tomato/cream
menu = [("Paneer tikka","₹ 240"),("Dal makhani","₹ 190"),("Butter naan","₹ 45"),("Veg biryani","₹ 220"),("Masala chaas","₹ 60")]
mr = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-radius:14px;background:#fff6ea;margin-bottom:8px;font:600 15px Poppins;color:#2b1408"><span>{a}</span><span style="display:flex;gap:10px;align-items:center">{b}<i style="width:28px;height:28px;border-radius:8px;background:#e63b2e;color:#fff;font:700 18px/28px Poppins;text-align:center;font-style:normal">+</i></span></div>' for a,b in menu)
qr = '<div style="width:150px;height:150px;background:#fff;border-radius:12px;padding:12px;display:grid;grid-template-columns:repeat(9,1fr);gap:2px">' + "".join(f'<i style="background:{"#2b1408" if (i*7+i//9*3)%5<2 or i in (0,1,2,9,11,18,19,20,6,7,8,15,17,24,25,26,54,55,56,63,65,72,73,74) else "transparent"};border-radius:1px"></i>' for i in range(81)) + '</div>'
P["p05_restaurant"] = page("""
body{--f:'Poppins';--h:'Anton';background:#fff1dc;color:#2b1408}
.red{position:absolute;right:0;top:0;bottom:0;width:470px;background:#e63b2e}
h1{font-size:80px;font-weight:400;letter-spacing:.5px;line-height:1.24;text-transform:uppercase;width:560px} h1 span{color:#e63b2e}
.sub{color:#6e4a35;width:520px}
.vis{gap:40px;align-items:center}
.l{flex:1;display:flex;flex-direction:column;gap:18px}
.c{display:flex;gap:16px;align-items:center;background:#fff;border-radius:22px;padding:18px 20px;box-shadow:0 14px 30px rgba(120,40,10,.10);font:600 21px/1.35 Poppins}
.c .ib{width:50px;height:50px;border-radius:16px;background:#ffe1d6;color:#e63b2e}
.stand{display:flex;align-items:center;gap:18px;background:#2b1408;border-radius:22px;padding:18px;color:#fff1dc;font:600 19px/1.4 Poppins}
""", "<h1>Let your regulars<br><span>order direct.</span></h1><div class=sub>Your own ordering website. Your menu, your customers.</div>",
f'''<div class=l><div class=c><span class=ib>{ic("cart",26)}</span>Orders come straight to your kitchen</div><div class=c><span class=ib>{ic("tag",26)}</span>Your menu, your prices</div><div class=c><span class=ib>{ic("users",26)}</span>Your customer list stays with you</div>
<div class=stand>{qr}<span>A QR on every table and parcel. Scan, order, done.</span></div></div>
{phone(f'<div style="padding:6px 16px 16px;flex:1;display:flex;flex-direction:column"><div style="height:120px;border-radius:18px;background:linear-gradient(135deg,#ff8a5c,#e63b2e);color:#fff;padding:16px;font:700 22px/1.2 Poppins;margin-bottom:12px">Your Restaurant<br><span style="font:500 13px Poppins;opacity:.9">Order direct · sample menu</span></div>{mr}<div style="margin-top:auto;background:#2b1408;color:#fff;border-radius:14px;padding:14px;display:flex;justify-content:space-between;font:700 16px Poppins"><span>3 items</span><span>View cart →</span></div></div>', w=360, h=740, style="z-index:2")}''',
"#2b1408", "Want this? DM us", "background:#2b1408;color:#fff1dc", bg="<div class=red></div>")

# ───────── 06 INDIA · CA / tax consultant · CAROUSEL 5 · Swiss minimal · Inter · white/black/teal
CA = """
body{--f:'Inter';background:#f6f6f3;color:#111;background-image:linear-gradient(#e7e7e2 1px,transparent 1px),linear-gradient(90deg,#e7e7e2 1px,transparent 1px);background-size:90px 90px;background-position:-1px -1px}
h1{font-size:64px;font-weight:700;letter-spacing:-2.2px} h1 span{color:#0e7c86}
.sub{color:#555;font-weight:400}
.k{font:600 15px Inter;letter-spacing:3px;text-transform:uppercase;color:#0e7c86;margin-top:22px}
.box{background:#fff;border:1.5px solid #111;border-radius:0}
"""
P["p06_ca_s1"] = page(CA+".vis{align-items:stretch}.flow{flex:1;display:grid;grid-template-columns:repeat(3,1fr);border:1.5px solid #111;background:#fff;box-shadow:10px 10px 0 #0e7c86}.st{display:flex;flex-direction:column;gap:18px;padding:30px 26px;border-right:1.5px solid #111}.st:last-child{border-right:0}.st{padding:40px 30px!important}.st .no{font:800 96px Inter;letter-spacing:-3px;color:#0e7c86}.st .ic{color:#111;margin:auto 0;align-self:center}.st b{font:700 34px Inter}.st small{font:400 20px/1.4 Inter;color:#555}.side{width:420px;display:flex;flex-direction:column;gap:14px;margin-bottom:20px}.side div{border-top:1.5px solid #111;padding-top:12px;font:500 22px/1.4 Inter}",
 "<div class=k>For CAs and tax consultants</div><h1 style='margin-top:12px'>Collecting client documents<br><span>shouldn't take weeks.</span></h1>",
 "<div class=flow>" + "".join(f"<div class=st><span class=no>0{i+1}</span><span class=ic>{ic(c,150,w=1.2)}</span><b>{a}</b><small>{b}</small></div>" for i,(c,a,b) in enumerate([("upload","Upload","Clients send files to one link"),("grid","Sort","Every file lands in its folder"),("bell","Remind","Pending clients get a nudge")])) + "</div>",
 "#111", "Swipe", "background:#111;color:#fff", tagline="1 / 5")
scat = [("Chat",-10,20,20),("Email",7,290,0),("Photo",-6,70,200),("Paper",9,330,190),("Pen drive",-4,150,390),("PDF",6,0,560),("Scanned copy",-7,250,560)]
sc = "".join(f'<div class=box style="position:absolute;left:{x}px;top:{y}px;transform:rotate({r}deg);padding:24px 28px;display:flex;gap:14px;align-items:center;font:600 26px Inter;box-shadow:6px 6px 0 #111"><span style="color:#0e7c86">{ic("file",32)}</span>{t}</div>' for t,r,x,y in scat)
P["p06_ca_s2"] = page(CA+".vis{gap:30px}.mess{position:relative;flex:1}.txt{width:360px;display:flex;flex-direction:column;justify-content:center;gap:22px;font:500 27px/1.45 Inter}.txt b{font-weight:700}",
 "<div class=k>The problem</div><h1 style='margin-top:12px'>Files arrive from<br><span>everywhere.</span></h1>",
 f"<div class=mess>{sc}</div><div class=txt><div>Some on chat, some by email, some on paper.</div><div><b>You spend hours just finding them</b>, before the real work even starts.</div></div>",
 "#111", "Swipe", "background:#111;color:#fff", tagline="2 / 5")
fold = [("Client 01","8 of 8 files","#0e7c86","Complete"),("Client 02","5 of 8 files","#d99a00","Waiting"),("Client 03","8 of 8 files","#0e7c86","Complete"),("Client 04","2 of 8 files","#d33","Reminder sent"),("Client 05","7 of 8 files","#d99a00","Waiting"),("Client 06","8 of 8 files","#0e7c86","Complete"),("Client 07","0 of 8 files","#d33","Reminder sent")]
fr = "".join(f'<div style="display:flex;align-items:center;gap:16px;padding:27px 22px;border-top:1.5px solid #111"><span style="color:{c}">{ic("box",28)}</span><b style="flex:1;font:700 20px Inter">{a}<span style="display:block;font:400 15px Inter;color:#666">{b}</span></b><span style="font:700 13px Inter;letter-spacing:1px;text-transform:uppercase;color:{c}">{s}</span></div>' for a,b,c,s in fold)
P["p06_ca_s3"] = page(CA+".vis{gap:26px}.box.big{flex:1;box-shadow:10px 10px 0 #0e7c86}.up{width:330px;display:flex;flex-direction:column;gap:18px}.up{justify-content:space-between}.up .box{flex:1;padding:26px;font:500 23px/1.45 Inter;display:flex;flex-direction:column;justify-content:center}.up .box b{display:block;font:700 28px Inter;margin-bottom:10px}",
 "<div class=k>The fix</div><h1 style='margin-top:12px'>Each client uploads<br><span>to their own folder.</span></h1>",
 f'<div class="box big"><div style="padding:18px 20px;font:700 22px Inter;display:flex;justify-content:space-between">Client portal<span style="font:500 14px Inter;color:#888">sample</span></div>{fr}</div><div class=up><div class=box><b>For clients</b>Open a link, upload from phone. That\'s it.</div><div class=box><b>For you</b>See who is complete and who is pending, at a glance.</div></div>',
 "#111", "Swipe", "background:#111;color:#fff", tagline="3 / 5")
cal = "".join(f'<div style="height:150px;border:1.5px solid #111;margin:-0.75px;display:flex;flex-direction:column;justify-content:space-between;padding:8px;background:{"#0e7c86" if d in (7,15,24) else "#fff"};color:{"#fff" if d in (7,15,24) else "#111"};font:700 22px Inter">{d}{"<i style=&quot;font:700 14px Inter;font-style:normal;letter-spacing:1px&quot;>REMIND</i>" if d in (7,15,24) else ""}</div>' for d in range(1,29))
P["p06_ca_s4"] = page(CA+".vis{gap:24px;flex-direction:column}.cal{width:100%;display:grid;grid-template-columns:repeat(7,1fr);background:#fff}.txt{display:flex;gap:20px;align-items:center}.txt>div:last-child{flex:1}.m{width:560px;background:#fff;border:1.5px solid #111;padding:22px;font:500 21px/1.45 Inter;box-shadow:6px 6px 0 #111}.m b{display:block;font:700 14px Inter;color:#0e7c86;letter-spacing:1px;margin-bottom:6px}",
 "<div class=k>On autopilot</div><h1 style='margin-top:12px'>Reminders go out<br><span>before every due date.</span></h1>",
 f'<div class=cal>{cal}</div><div class=txt><div class=m><b>AUTO MESSAGE · SAMPLE</b>Hello! Please upload this month\'s bank statement and bills by Friday. Thank you.</div><div style="font:500 22px/1.45 Inter">No more calling every client one by one.</div></div>',
 "#111", "Swipe", "background:#111;color:#fff", tagline="4 / 5")
P["p06_ca_s5"] = page(CA+".vis{align-items:center;justify-content:space-between;gap:20px}.q{flex:1;font:500 34px/1.45 Inter}.q b{color:#0e7c86}",
 "<div class=k>Your turn</div><h1 style='margin-top:12px'>Want a client portal<br><span>for your practice?</span></h1>",
 "<div class=q>Tell us how many clients you handle and what you collect from them. <b>We'll build a portal that fits your office.</b></div>" + peep("Coffee","Smile","GrayShort","GrayFull","GlassRound",w=440,h=620),
 "#111", "DM us", "background:#0e7c86;color:#fff", tagline="5 / 5")

# ───────── 07 INDIA · Wedding photographer · SINGLE · Gelasio + DM Sans · warm black/sepia/rust
ph = lambda c1,c2,r,w,h: f'<div style="background:#fff;padding:10px 10px 34px;box-shadow:0 18px 34px rgba(0,0,0,.45);transform:rotate({r}deg);width:{w}px;flex:none"><div style="height:{h}px;background:linear-gradient(160deg,{c1},{c2})"></div></div>'
P["p07_photographer"] = page("""
body{--f:'DM Sans';--h:'Gelasio';background:#171412;color:#efe4d3}
h1{font-size:68px;font-weight:600;font-style:italic;letter-spacing:-1px} h1 span{color:#e08a5a;font-style:normal}
.sub{color:#b9ab97}
.vis{gap:28px;align-items:center}
.stack{position:relative;width:390px;height:700px;flex:none}
.stack>div{position:absolute}
.r{flex:1;display:flex;flex-direction:column;gap:16px}
.lap{background:#2a2420;border-radius:18px;padding:12px;box-shadow:0 30px 60px rgba(0,0,0,.5)}
.lap .s{background:#fbf7f0;border-radius:8px;padding:16px;color:#2a2420}
.lap .s b{font:600 22px Gelasio;font-style:italic;display:block}.lap .s small{font:500 12px 'DM Sans';color:#9a8d7a;letter-spacing:1px;text-transform:uppercase}
.g{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:14px 0}.g i{height:96px;border-radius:4px}
.dl{display:flex;gap:8px}.dl span{flex:1;text-align:center;padding:9px;border-radius:8px;font:700 12px 'DM Sans'}
.f{display:flex;gap:16px;align-items:center;font:500 23px/1.35 'DM Sans';color:#efe4d3}
.f .ib{width:46px;height:46px;border-radius:50%;border:1.5px solid #e08a5a;color:#e08a5a}
""", "<h1>Your photos deserve better<br><span>than a pen drive.</span></h1><div class=sub>For wedding and event photographers.</div>",
f'''<div class=stack><div style="left:10px;top:20px">{ph("#e7c9a3","#b4532a",-8,270,290)}</div><div style="left:110px;top:150px">{ph("#c9d6c2","#5e7a5a",7,260,280)}</div><div style="left:20px;top:290px">{ph("#f3d9c8","#8e4b3a",-3,280,250)}</div></div>
<div class=r><div class=lap><div class=s><small>Private gallery · sample</small><b>The Sample Wedding</b><div class=g>''' + "".join(f'<i style="background:linear-gradient(160deg,{a},{b})"></i>' for a,b in [("#e7c9a3","#b4532a"),("#c9d6c2","#5e7a5a"),("#f3d9c8","#8e4b3a"),("#d8c3e0","#6b4a7a"),("#f0e0b8","#a7802e"),("#cfe0e6","#3f6a7a")]) + '''</div><div class=dl><span style="background:#2a2420;color:#fbf7f0">Download all</span><span style="background:#efe4d3;color:#2a2420">Share with family</span></div></div></div>
''' + "".join(f'<div class=f><span class=ib>{ic(i,22)}</span>{t}</div>' for i,t in [("shield","A private link for every family"),("upload","Full-quality downloads, anytime"),("cal","Your portfolio with a booking form")]) + '</div>',
"#efe4d3", "Get your gallery website. DM us", "background:#e08a5a;color:#171412", logo_color="#efe4d3")

# ───────── 08 INDIA · Transport / fleet · SINGLE · Fira Sans · asphalt/safety yellow
trips = [("GJ 05 XX 1234","Surat → Pune","On the way","#ffd200","#2a2a14"),("GJ 05 XX 5678","Vapi → Surat","Loading","#7dd3fc","#0f2a36"),("GJ 05 XX 9012","Surat → Indore","Delivered","#86efac","#12301e"),("GJ 05 XX 3456","Bharuch → Surat","Driver rest","#fca5a5","#3a1616")]
tr = "".join(f'<div style="display:grid;grid-template-columns:190px 1fr 150px;align-items:center;gap:12px;padding:19px 18px;border-top:1px solid #3a3e46;font:500 20px Fira Sans"><b style="font-weight:700;letter-spacing:.5px">{a}</b><span style="color:#c4c8d0">{b}</span><span style="justify-self:end;font:700 13px Fira Sans;letter-spacing:.6px;text-transform:uppercase;padding:7px 12px;border-radius:8px;background:{d};color:{c}">{s}</span></div>' for a,b,s,c,d in trips)
P["p08_transport"] = page("""
body{--f:'Fira Sans';background:#1f2227;color:#f4f4f2}
.road{position:absolute;left:0;right:0;top:470px;height:120px;background:#2b2f36}
.road:before{content:'';position:absolute;left:0;right:0;top:56px;height:8px;background:repeating-linear-gradient(90deg,#ffd200 0 60px,transparent 60px 110px)}
h1{font-size:68px;font-weight:700;letter-spacing:-1.5px} h1 span{color:#ffd200}
.sub{color:#b0b5bf}
.vis{flex-direction:column;gap:22px}
.roadb{height:170px;flex:none;border-radius:22px;background:#2b2f36;position:relative;overflow:hidden}.roadb:before{content:'';position:absolute;left:0;right:0;bottom:34px;height:8px;background:repeating-linear-gradient(90deg,#ffd200 0 60px,transparent 60px 110px)}.trk{position:absolute;left:60px;bottom:58px;display:flex;align-items:flex-end;gap:2px}
.board{background:#2b2f36;border-radius:22px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.4)}
.bh{display:flex;justify-content:space-between;align-items:center;padding:18px;font:700 22px Fira Sans}
.bh span{font:600 13px Fira Sans;color:#1f2227;background:#ffd200;padding:6px 10px;border-radius:8px}
.cols{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.co{background:#2b2f36;border-radius:18px;padding:16px;display:flex;flex-direction:column;gap:8px}
.co .ib{width:44px;height:44px;border-radius:12px;background:#ffd200;color:#1f2227}
.co{flex:1}.cols{flex:1}.co b{font:700 22px Fira Sans}.co small{font:400 17px/1.35 Fira Sans;color:#b0b5bf}
""", "<h1>Where is each truck<br><span>right now?</span></h1><div class=sub>One trip board for loads, drivers, diesel and payments.</div>",
f'''<div class=roadb><div class="trk free">{''.join('')}<div style="width:220px;height:90px;background:#ffd200;border-radius:10px 4px 4px 10px;position:relative"><i style="position:absolute;left:24px;bottom:-14px;width:30px;height:30px;border-radius:50%;background:#111;border:5px solid #555"></i><i style="position:absolute;right:24px;bottom:-14px;width:30px;height:30px;border-radius:50%;background:#111;border:5px solid #555"></i><span style="position:absolute;left:16px;top:28px;font:800 20px Fira Sans;color:#1f2227;letter-spacing:1px">YOUR TRANSPORT</span></div><div style="width:90px;height:70px;background:#f4f4f2;border-radius:4px 22px 6px 4px;position:relative"><i style="position:absolute;left:14px;top:12px;width:46px;height:26px;border-radius:4px;background:#7dd3fc"></i><i style="position:absolute;right:18px;bottom:-14px;width:30px;height:30px;border-radius:50%;background:#111;border:5px solid #555"></i></div></div></div>
<div class=board><div class=bh>Trip board · today<span>SAMPLE</span></div>{tr}</div>
<div class=cols>''' + "".join(f'<div class=co><span class=ib>{ic(i,24)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("truck","Every trip","From loading to delivery"),("users","Drivers","Who is on which trip"),("drop","Diesel","Per trip, per truck"),("rupee","Payments","Freight due and received")]) + '</div>',
"#f4f4f2", "Get your trip app. DM us", "background:#ffd200;color:#1f2227", logo_color="#f4f4f2")

# ───────── 09 INDIA · Mobile repair shop · SINGLE · TeX Gyre Adventor + Inter · electric blue/ice
steps = [("Received","10:15 AM",1),("Checking","11:00 AM",1),("Repairing","2:30 PM",1),("Ready","5:45 PM",1)]
st = "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;position:relative;z-index:2"><span style="width:56px;height:56px;border-radius:50%;background:#2563eb;color:#fff;display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 8px #dbe7ff">{ic("check",26,w=3)}</span><b style="font:700 19px \'TeX Gyre Adventor\'">{a}</b><small style="font:500 14px Inter;color:#5b6b8c">{t}</small></div>' for a,t,d in steps)
P["p09_mobilerepair"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:linear-gradient(180deg,#f1f6ff 0%,#dfe9ff 100%);color:#0b1b3f}
h1{font-size:62px;font-weight:700;letter-spacing:-1px} h1 span{color:#2563eb}
.sub{color:#4b5d82}
.vis{flex-direction:column;gap:24px}
.track{background:#fff;border-radius:28px;padding:34px 20px 30px;position:relative;box-shadow:0 20px 50px rgba(37,99,235,.14)}
.track:before{content:'';position:absolute;left:12%;right:12%;top:56px;height:4px;background:#2563eb;border-radius:2px}
.row{display:flex;gap:24px;flex:1;align-items:flex-end;min-height:0}
.msg{flex:1;display:flex;flex-direction:column;gap:14px;align-self:center}
.bubble{background:#fff;border-radius:22px 22px 22px 6px;padding:22px 24px;font:500 23px/1.45 Inter;box-shadow:0 14px 30px rgba(11,27,63,.10)}
.bubble b{display:block;font:700 13px Inter;letter-spacing:1px;color:#2563eb;margin-bottom:6px}
.bubble.me{background:#2563eb;color:#fff;border-radius:22px 22px 6px 22px;align-self:flex-end}
""", "<h1>\"Is my phone ready?\"<br><span>Let an app answer that.</span></h1><div class=sub>A repair tracker for mobile and laptop repair shops.</div>",
f'''<div class=track><div style="display:flex">{st}</div></div>
<div class=row>{peep("Device","Smile","ShortVolumed",w=400,h=560)}<div class=msg><div class=bubble><b>YOUR REPAIR SHOP · SAMPLE</b>Hi! Your phone is repaired and ready for pickup. Shop open till 9 PM.</div><div class="bubble me">Great, coming in the evening!</div><div class=bubble style="font-size:18px;color:#4b5d82">Every update goes out by itself. Fewer calls, happier customers.</div></div></div>''',
"#0b1b3f", "Want a repair tracker? DM us", "background:#2563eb;color:#fff")

# ───────── 10 INDIA · Saree / textile seller · CAROUSEL 5 · Lora + Poppins · magenta/emerald/gold
SR = """
body{--f:'Poppins';--h:'Lora';background:#fff8f1;color:#3d0c26}
h1{font-size:64px;font-weight:700;letter-spacing:-1px} h1 span{color:#0f6b54;font-style:italic}
.sub{color:#7a4a5e}
.border{position:absolute;left:0;right:0;bottom:0;height:22px;background:repeating-linear-gradient(90deg,#c99a2e 0 18px,#8e1652 18px 36px)}
.k{font:600 15px Poppins;letter-spacing:3px;color:#8e1652;margin-top:22px;text-transform:uppercase}
"""
sar = lambda c1,c2,b,w=170,h=300,r=0: f'<div style="width:{w}px;height:{h}px;flex:none;border-radius:12px;background:linear-gradient(100deg,{c1} 0%,{c2} 45%,{c1} 70%,{c2} 100%);position:relative;overflow:hidden;transform:rotate({r}deg);box-shadow:0 26px 44px rgba(61,12,38,.25)"><i style="position:absolute;left:0;right:0;bottom:0;height:{h*0.22}px;background:repeating-linear-gradient(90deg,{b} 0 10px,transparent 10px 16px),linear-gradient({b}44,{b}88)"></i><i style="position:absolute;left:0;right:0;bottom:{h*0.22}px;height:8px;background:{b}"></i><i style="position:absolute;inset:0;background:repeating-linear-gradient(170deg,rgba(255,255,255,.10) 0 2px,transparent 2px 26px)"></i></div>'
P["p10_saree_s1"] = page(SR+".vis{align-items:flex-end;justify-content:center;gap:22px}",
 "<div class=k>Saree &amp; textile sellers</div><h1 style='margin-top:10px'>Stop sending 50 photos<br><span>one by one.</span></h1><div class=sub>Share one catalogue link instead. Swipe to see how.</div>",
 sar("#8e1652","#c2306f","#c99a2e",200,420,-6) + sar("#0f6b54","#1d9a7a","#e8c66a",230,500) + sar("#4a1d7a","#7b45b8","#c99a2e",200,420,6),
 "#3d0c26", "Swipe", "background:#8e1652;color:#fff", bg="<div class=border></div>", tagline="1 / 5")
cat = [("#8e1652","#c2306f","#c99a2e","Silk · Wedding"),("#0f6b54","#1d9a7a","#e8c66a","Cotton · Daily"),("#4a1d7a","#7b45b8","#c99a2e","Georgette · Party"),("#b5541c","#e58a3a","#5a2a0e","Linen · Office"),("#123b6b","#2f6fb8","#d9b44a","Chiffon · Festive"),("#6b1d1d","#a33a3a","#e8c66a","Banarasi · Bridal")]
cc = "".join(f'<div style="background:#fff;border-radius:16px;padding:10px;box-shadow:0 10px 24px rgba(61,12,38,.10)">{sar(a,b,c,0,0)}</div>'.replace('width:0px;height:0px','width:100%;height:170px') + '' for a,b,c,t in cat)
cc = "".join(f'<div style="background:#fff;border-radius:18px;padding:10px 10px 14px;box-shadow:0 10px 24px rgba(61,12,38,.10)"><div style="height:200px;border-radius:12px;background:linear-gradient(100deg,{a} 0%,{b} 45%,{a} 70%,{b} 100%);position:relative;overflow:hidden"><i style="position:absolute;left:0;right:0;bottom:0;height:44px;background:repeating-linear-gradient(90deg,{c} 0 8px,transparent 8px 13px),linear-gradient({c}44,{c}88)"></i></div><b style="display:block;font:600 16px Poppins;margin-top:10px">{t}</b><small style="font:500 13px Poppins;color:#8a6a78">Sample · see price</small></div>' for a,b,c,t in cat)
P["p10_saree_s2"] = page(SR+".vis{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}",
 "<div class=k>Step 1</div><h1 style='margin-top:10px'>Every design, neatly<br><span>in one catalogue.</span></h1><div class=sub>Photos, fabric, colours and price, sorted by type.</div>",
 cc, "#3d0c26", "Swipe", "background:#fff;color:#3d0c26;box-shadow:0 6px 16px rgba(0,0,0,.08)", bg="<div class=border></div>", tagline="2 / 5")
P["p10_saree_s3"] = page(SR+".vis{gap:30px;align-items:center}.share{flex:1;display:flex;flex-direction:column;gap:16px}.sh{display:flex;gap:16px;align-items:center;background:#fff;border-radius:22px;padding:18px 20px;box-shadow:0 12px 26px rgba(61,12,38,.08);font:500 20px/1.4 Poppins}.sh .ib{width:52px;height:52px;border-radius:16px;background:#fbe6ef;color:#8e1652}",
 "<div class=k>Step 2</div><h1 style='margin-top:10px'>Customers share it<br><span>in one tap.</span></h1>",
 phone('<div style="padding:8px 16px 16px;flex:1;display:flex;flex-direction:column;gap:12px"><b style="font:700 20px Lora;color:#3d0c26">Your Saree House</b><small style="font:500 12px Poppins;color:#999;margin-top:-8px">Catalogue · sample</small><div style="height:260px;border-radius:16px;background:linear-gradient(100deg,#0f6b54 0%,#1d9a7a 45%,#0f6b54 70%,#1d9a7a 100%);position:relative;overflow:hidden"><i style="position:absolute;left:0;right:0;bottom:0;height:56px;background:repeating-linear-gradient(90deg,#e8c66a 0 8px,transparent 8px 13px)"></i></div><b style="font:600 17px Poppins;color:#3d0c26">Cotton · Daily wear</b><div style="display:flex;gap:6px">' + "".join(f'<i style="width:30px;height:30px;border-radius:50%;background:{c};border:3px solid #fff;box-shadow:0 0 0 1px #ddd"></i>' for c in ["#0f6b54","#8e1652","#123b6b","#b5541c"]) + '</div><div style="margin-top:auto;display:flex;gap:8px"><span style="flex:1;background:#3d0c26;color:#fff;border-radius:12px;padding:13px;text-align:center;font:600 14px Poppins">Enquire</span><span style="flex:1;background:#fbe6ef;color:#8e1652;border-radius:12px;padding:13px;text-align:center;font:600 14px Poppins">Share link</span></div></div>', w=360, h=740) +
 '<div class=share>' + "".join(f'<div class=sh><span class=ib>{ic(i,26)}</span>{t}</div>' for i,t in [("send","One link instead of 50 photos"),("users","Customers forward it to family"),("chat","Enquiries come with the design name")]) + '</div>',
 "#3d0c26", "Swipe", "background:#fff;color:#3d0c26;box-shadow:0 6px 16px rgba(0,0,0,.08)", bg="<div class=border></div>", tagline="3 / 5")
P["p10_saree_s4"] = page(SR+".vis{gap:24px}.c2{flex:1;background:#fff;border-radius:26px;padding:26px;box-shadow:0 18px 40px rgba(61,12,38,.10);display:flex;flex-direction:column;gap:12px}.c2 .t{font:700 15px Poppins;letter-spacing:2px;text-transform:uppercase}.c2 .r{display:flex;justify-content:space-between;padding:14px 16px;border-radius:14px;font:600 18px Poppins}",
 "<div class=k>Step 3</div><h1 style='margin-top:10px'>Retail and wholesale,<br><span>each see their own rate.</span></h1><div class=sub>Wholesale buyers log in. Everyone else sees retail.</div>",
 '<div class=c2><span class=t style="color:#8e1652">Retail view</span>' + "".join(f'<div class=r style="background:#fdf1f5"><span>{a}</span><span>Retail price</span></div>' for a in ["Silk saree","Cotton saree","Georgette saree","Linen saree","Chiffon saree","Banarasi saree"]) + f'<span style="margin-top:auto;display:flex;gap:10px;align-items:center;font:500 18px Poppins;color:#7a4a5e">{ic("users",22)}Anyone with the link</span></div>' +
 '<div class=c2 style="background:#0f6b54;color:#fff"><span class=t style="color:#e8c66a">Wholesale login</span>' + "".join(f'<div class=r style="background:rgba(255,255,255,.12)"><span>{a}</span><span>Your rate</span></div>' for a in ["Silk saree","Cotton saree","Georgette saree","Linen saree","Chiffon saree","Banarasi saree"]) + f'<span style="margin-top:auto;display:flex;gap:10px;align-items:center;font:500 18px Poppins;color:#cfe9df">{ic("shield",22)}Only approved buyers</span></div>',
 "#3d0c26", "Swipe", "background:#fff;color:#3d0c26;box-shadow:0 6px 16px rgba(0,0,0,.08)", bg="<div class=border></div>", tagline="4 / 5")
P["p10_saree_s5"] = page(SR+".vis{flex-direction:column;align-items:center;justify-content:center;gap:26px;text-align:center}.q{font:500 28px/1.45 Poppins;color:#5a2a40;max-width:820px}.row{display:flex;gap:16px;align-items:flex-end}",
 "<div class=k>Your turn</div><h1 style='margin-top:10px;text-align:center'>Ready for your own<br><span>saree catalogue website?</span></h1>",
 '<div class=row>' + sar("#8e1652","#c2306f","#c99a2e",150,300,-5) + sar("#0f6b54","#1d9a7a","#e8c66a",170,350) + sar("#123b6b","#2f6fb8","#d9b44a",150,300,5) + '</div><div class=q>Tell us how many designs you sell and who you sell to. We will set up the right catalogue for you.</div>',
 "#3d0c26", "DM us to start", "background:#8e1652;color:#fff", bg="<div class=border></div>", tagline="5 / 5")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
