import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 46 INDIA · Cloud kitchen · CAROUSEL 6 · Inter Display + Lora · aubergine / paprika / cream
# New technique: CSS kraft delivery bag with a die-cut sticker (dashed inner edge) as the hero object.
CK = """
body{--f:'Inter';--h:'Inter Display';background:#fbf1e3;color:#2d1630}
h1{font-family:'Inter Display';font-size:66px;font-weight:900;letter-spacing:-2px} h1 span{font-family:'Lora';font-style:italic;font-weight:700;color:#d9481c;letter-spacing:-1px}
.sub{color:#6d5468}
.kk{font:700 16px Inter;letter-spacing:4px;color:#d9481c;margin-top:22px}
.pt{display:inline-flex;align-items:center;gap:10px;background:#2d1630;color:#fbf1e3;border-radius:30px;padding:9px 18px 9px 9px;font:700 16px Inter;letter-spacing:2px;margin-top:22px;align-self:flex-start}
.pt i{width:34px;height:34px;border-radius:50%;background:#d9481c;font:800 17px/1 Inter;font-style:normal;display:flex;align-items:center;justify-content:center;letter-spacing:0}
"""
def ck(n, head, vis, css, cta="Swipe", ctacss="background:#d9481c;color:#fff"):
    return page(CK + css, head, vis, "#2d1630", cta, ctacss, tagline=f"{n} / 6")
def part(k, label):
    return f'<div class=pt><i>{k}</i>PART {k} OF 4 · {label}</div>'

P["p46_cloudkitchen_s1"] = ck(1, """<div class=kk>FOR CLOUD KITCHENS</div><h1 style="margin-top:10px">Your regulars order every week.<br><span>Through someone else's app.</span></h1>
<div class=sub>4 simple parts to bring them back to your own order page.</div>""",
f'''<div class=bagw><div class=bag><div class=fold></div><div class=stk><div class=sin><small>NEXT TIME</small><b>Order direct</b><div class=qrw>{ic("qr",64,w=1.6)}<span>yourkitchen.in<br><em>sample</em></span></div></div></div><div class=hnd></div></div></div>
<div class=lst>{"".join(f'<div class=li><b>{a}</b><span>{t}<small>{s}</small></span></div>' for a,t,s in [("1","A card in every bag","Turn one order into a direct one"),("2","Your own menu page","Fast, clear, on any phone"),("3","Repeat in one tap","“Your usual” ready to go"),("4","Know your regulars","Who orders, what, and when")])}</div>''',
""".vis{gap:28px;align-items:stretch}
.bagw{width:420px;flex:none;background:#2d1630;border-radius:30px;display:flex;align-items:center;justify-content:center;overflow:hidden;position:relative}
.bag{width:330px;height:600px;background:linear-gradient(90deg,#c99a62 0 8%,#d8ac72 8% 92%,#c4935a 92%);border-radius:6px 6px 14px 14px;position:relative;display:flex;align-items:center;justify-content:center;box-shadow:0 30px 50px rgba(0,0,0,.35)}
.fold{position:absolute;left:0;right:0;top:0;height:64px;background:repeating-linear-gradient(90deg,#b8844d 0 22px,#c99a62 22px 44px);border-radius:6px 6px 0 0}
.hnd{position:absolute;left:50%;top:22px;width:90px;height:20px;margin-left:-45px;border-radius:10px;background:#2d1630}
.stk{width:260px;background:#fff;border-radius:22px;padding:10px;transform:none;box-shadow:0 10px 24px rgba(0,0,0,.18);margin-top:40px}
.sin{border:3px dashed #d9481c;border-radius:15px;padding:20px 16px;display:flex;flex-direction:column;align-items:center;gap:6px;text-align:center}
.sin small{font:800 14px Inter;letter-spacing:4px;color:#d9481c}.sin b{font:900 38px/1.2 'Inter Display';color:#2d1630}
.qrw{display:flex;align-items:center;gap:10px;margin-top:8px;color:#2d1630}.qrw span{font:700 16px/1.35 Inter;text-align:left}.qrw em{font:600 13px Inter;color:#9a7f94}
.lst{flex:1;display:flex;flex-direction:column;gap:14px}
.li{flex:1;background:#fff;border-radius:22px;display:flex;align-items:center;gap:20px;padding:0 24px;box-shadow:0 12px 26px rgba(45,22,48,.07)}
.li b{width:62px;height:62px;border-radius:50%;background:#fbe2d6;color:#d9481c;font:900 30px/1 'Inter Display';display:flex;align-items:center;justify-content:center;flex:none}
.li span{font:800 26px/1.25 'Inter Display';display:flex;flex-direction:column;gap:4px}.li small{font:500 18px/1.35 Inter;color:#6d5468}
""")

P["p46_cloudkitchen_s2"] = ck(2, part(1, "THE BAG CARD") + """<h1>Put an order-direct card<br><span>in every bag.</span></h1>
<div class=sub>The customer already loves your food. Tell them where to find you next time.</div>""",
f'''<div class=cards><div class=crd><small>FRONT · SAMPLE</small><b>Hungry again?</b><p>Order direct from<br><strong>yourkitchen.in</strong></p><div class=dish><i></i><i></i><i></i></div><div class=hr>Open 11 am to 11 pm · sample</div><div class=spc><small>THIS WEEK ON OUR PAGE</small><b>Chole kulche, weekend only</b></div><div class=q>{ic("qr",120,w=1.4)}<span>Scan to see<br>today's menu</span></div></div>
<div class="crd bk"><small>BACK · SAMPLE</small><b>Why order direct?</b>{"".join(f'<div class=rw>{ic("check",24,w=3)}<span>{t}</span></div>' for t in ["Your usual saved for next time","Talk to the kitchen, not a bot","Special dishes only on our page","Updates on your phone"])}</div></div>
<div class=tip>{ic("spark",26)}<span>Keep the card small and simple: one line, one QR, one web address.</span></div>''',
""".vis{flex-direction:column;gap:20px}
.cards{flex:1;display:flex;gap:24px;min-height:0}
.crd{flex:1;background:#fff;border-radius:26px;padding:30px;display:flex;flex-direction:column;gap:14px;box-shadow:0 20px 40px rgba(45,22,48,.10);border-top:14px solid #d9481c}
.crd small{font:800 14px Inter;letter-spacing:3px;color:#9a7f94}.crd>b{font:900 40px/1.2 'Inter Display'}
.dish{display:flex;gap:18px;margin-top:18px}.dish i{width:112px;height:112px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#f2a516 0 20%,#d9481c 21% 46%,#f6dcc4 47% 62%,#efe4da 63%)}.dish i:nth-child(2){background:radial-gradient(circle at 55% 45%,#8fb339 0 18%,#e8b04a 19% 46%,#f6dcc4 47% 62%,#efe4da 63%)}.dish i:nth-child(3){background:radial-gradient(circle at 45% 55%,#7a2e12 0 24%,#c26a2b 25% 46%,#f6dcc4 47% 62%,#efe4da 63%)}
.hr{font:700 17px Inter;color:#2e8b57}.spc{border:2px dashed #e7c9b9;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:4px}.spc small{font:800 13px Inter;letter-spacing:2px;color:#d9481c}.spc b{font:800 21px Inter}
.crd p{font:500 23px/1.45 Inter;color:#6d5468}.crd p strong{color:#2d1630;font-weight:800}
.q{margin-top:auto;display:flex;align-items:center;gap:18px;background:#fbf1e3;border-radius:18px;padding:16px}.q span{font:700 20px/1.35 Inter}
.bk{background:#2d1630;color:#fbf1e3;border-top-color:#f2a516}.bk small{color:#c7a9c1}
.rw{flex:1;display:flex;align-items:center;gap:14px;border-bottom:1px solid #4a2c4e;font:600 21px/1.35 Inter}.rw:last-child{border:0}.rw svg{color:#f2a516;flex:none}
.tip{background:#f2a516;border-radius:20px;padding:20px 24px;display:flex;align-items:center;gap:16px;font:700 22px/1.35 Inter;color:#2d1630}.tip svg{flex:none}
""")

menu = [("Paneer tikka roll", "Bestseller", "Mint chutney inside"), ("Veg biryani bowl", "Spicy", "With raita"), ("Dal makhani combo", "Comfort", "Rice + 2 rotis"), ("Chole kulche", "New", "Weekend only"), ("Masala chaas", "Cool", "Chilled glass")]
P["p46_cloudkitchen_s3"] = ck(3, part(2, "YOUR MENU PAGE") + """<h1>A menu page that feels<br><span>like an app.</span></h1>
<div class=sub>Opens fast on any phone. No download needed.</div>""",
'<div class=pw>' + phone(f'''<div class=mh><b>Your Kitchen</b><small>Open now · sample menu</small></div>
<div class=tabs><i class=on>All</i><i>Rolls</i><i>Bowls</i><i>Combos</i></div>
{"".join(f'<div class=it><div class=im></div><div class=tx><b>{a}</b><small>{c}</small><em>{b}</em></div><span>Add</span></div>' for a,b,c in menu)}
<div class=cart>2 items · View cart</div>''', w=380, h=730) + '</div>' +
f'''<div class=pts>{"".join(f'<div class=pp><b>{a}</b><span>{b}</span></div>' for a,b in [("Photos first","People order with their eyes"),("Short menu","Your best dishes on top"),("Tags","Bestseller, spicy, new"),("One-page cart","Order in under a minute")])}</div>''',
""".vis{gap:26px;align-items:center}
.pw{flex:none;display:flex}
.mh{padding:10px 20px 8px}.mh b{display:block;font:900 26px 'Inter Display';color:#2d1630}.mh small{font:600 14px Inter;color:#2e8b57}
.tabs{display:flex;gap:8px;padding:4px 20px 10px}.tabs i{font:700 14px Inter;font-style:normal;padding:7px 14px;border-radius:16px;background:#f4ece6;color:#6d5468}.tabs i.on{background:#2d1630;color:#fff}
.it{display:flex;gap:12px;align-items:center;margin:0 16px 10px;padding:10px;border-radius:16px;background:#fbf6f1}
.im{width:70px;height:70px;border-radius:14px;flex:none;background:radial-gradient(circle at 35% 35%,#f2a516 0 22%,#d9481c 23% 45%,#7a2e12 46% 60%,#f6dcc4 61%)}
.tx{flex:1;min-width:0;display:flex;flex-direction:column;gap:2px}.tx b{font:800 16px Inter;color:#2d1630}.tx small{font:500 13px Inter;color:#7d6a78}
.tx em{font:700 12px Inter;font-style:normal;color:#d9481c}
.it span{font:800 14px Inter;color:#fff;background:#d9481c;border-radius:12px;padding:8px 12px}
.cart{margin:auto 16px 18px;background:#2d1630;color:#fff;border-radius:16px;padding:14px;text-align:center;font:800 16px Inter}
.pts{flex:1;display:flex;flex-direction:column;gap:16px;align-self:stretch}
.pp{flex:1;background:#fff;border-radius:22px;padding:0 26px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-left:10px solid #d9481c}
.pp b{font:900 30px 'Inter Display'}.pp span{font:500 20px/1.35 Inter;color:#6d5468}
""")

P["p46_cloudkitchen_s4"] = ck(4, part(3, "REPEAT ORDERS") + """<h1>"Your usual" ready.<br><span>Order again in one tap.</span></h1>
<div class=sub>Regulars don't want to search the menu every Friday.</div>""",
f'''<div class=ord><div class=oh><small>WELCOME BACK · SAMPLE</small><b>Your usual from last Friday</b></div>
{"".join(f'<div class=ol><i>{q}</i><span>{a}</span><em>{b}</em></div>' for q,a,b in [("1x","Veg biryani bowl","Extra raita"),("2x","Paneer tikka roll","Less spicy"),("1x","Gulab jamun (2 pcs)","")])}
<div class=ag>{ic("send",26)} Order again</div><div class=nt>Same address · same notes · change anything before you pay</div></div>
<div class=sd><div class=sb><b>Saved</b><span>Address and notes</span></div><div class=sb><b>Easy</b><span>Change one item</span></div><div class=sb><b>Fast</b><span>Checkout in seconds</span></div></div>''',
""".vis{gap:24px;align-items:stretch}
.ord{flex:1;background:#fff;border-radius:28px;padding:30px;display:flex;flex-direction:column;gap:14px;box-shadow:0 20px 40px rgba(45,22,48,.10)}
.oh small{font:800 14px Inter;letter-spacing:3px;color:#2e8b57}.oh b{display:block;font:900 32px/1.25 'Inter Display';margin-top:6px}
.ol{flex:1;display:flex;align-items:center;gap:16px;background:#fbf1e3;border-radius:18px;padding:0 20px;font:700 23px Inter}
.ol i{font-style:normal;font:900 22px 'Inter Display';color:#d9481c;width:40px}.ol em{margin-left:auto;font:600 17px Inter;font-style:normal;color:#7d6a78}
.ag{background:#d9481c;color:#fff;border-radius:20px;padding:22px;display:flex;align-items:center;justify-content:center;gap:14px;font:800 28px Inter}
.nt{font:500 17px Inter;color:#7d6a78;text-align:center}
.sd{width:250px;flex:none;display:flex;flex-direction:column;gap:16px}
.sb{flex:1;background:#2d1630;color:#fbf1e3;border-radius:22px;padding:0 22px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.sb b{font:900 32px 'Inter Display';color:#f2a516}.sb span{font:500 19px/1.35 Inter;color:#e2cfe0}
""")

rows = [("R. Shah", "6", "Yesterday", "Biryani bowl", ""), ("A. Mehta", "4", "3 days ago", "Paneer roll", ""), ("K. Iyer", "5", "16 days ago", "Dal combo", "hot"), ("S. Khan", "3", "Today", "Chole kulche", ""), ("P. Rao", "2", "19 days ago", "Biryani bowl", "hot"), ("N. Das", "7", "2 days ago", "Paneer roll", "")]
P["p46_cloudkitchen_s5"] = ck(5, part(4, "YOUR REGULARS") + """<h1>Know who orders,<br><span>what, and when.</span></h1>
<div class=sub>Your customer list is yours. Not hidden inside another app.</div>""",
f'''<div class=tb><div class="tr th"><span>Customer</span><span>Orders</span><span>Last order</span><span>Favourite</span></div>
{"".join(f'<div class="tr {c}"><span><b>{a}</b></span><span>{b}</span><span>{d}</span><span>{e}</span></div>' for a,b,d,e,c in rows)}
<div class=tf>SAMPLE DATA · this month</div></div>
<div class=msg><span class=ib>{ic("bell",26)}</span><div><b>2 regulars have not ordered in 2 weeks.</b><small>Send them a friendly message about this week's special.</small></div></div>''',
""".vis{flex-direction:column;gap:18px}
.tb{flex:1;background:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 20px 40px rgba(45,22,48,.08)}
.tr{flex:1;display:grid;grid-template-columns:1.1fr .7fr 1fr 1.1fr;align-items:center;padding:0 14px;border-radius:14px;font:500 21px Inter;color:#4b3349}
.tr b{font-weight:800;color:#2d1630}.th{flex:.7;font:800 15px Inter;letter-spacing:2px;text-transform:uppercase;color:#9a7f94}
.tr.hot{background:#fde4d8}.tr.hot span:nth-child(3){color:#d9481c;font-weight:800}
.tf{font:700 13px Inter;letter-spacing:3px;color:#9a7f94;text-align:right}
.msg{background:#2d1630;color:#fbf1e3;border-radius:22px;padding:22px 24px;display:flex;align-items:center;gap:18px}
.msg .ib{width:56px;height:56px;border-radius:50%;background:#d9481c;color:#fff}
.msg b{display:block;font:800 24px/1.3 Inter}.msg small{font:500 19px/1.4 Inter;color:#d8c2d4}
""")

P["p46_cloudkitchen_s6"] = ck(6, """<div class=kk>YOUR FOOD, YOUR CUSTOMERS</div><h1 style="margin-top:10px">Want your own<br><span>order page?</span></h1>
<div class=sub>We build order pages, repeat-order buttons and customer lists for cloud kitchens.</div>""",
f'''<div class=w>{peep("Device","Smile","Long","None",w=380,h=640)}<div class=ops>{"".join(f'<div class=op><span class=ib>{ic(i,30)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("qr","Bag cards with your QR","Designed for your kitchen"),("globe","Menu page on your web address","Fast on any phone"),("send","Order again button","For your regulars"),("users","Customer list","Know who to message")])}</div></div>''',
""".vis{align-items:stretch}.w{display:flex;align-items:flex-end;gap:16px;width:100%}
.ops{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.op{flex:1;background:#fff;border-radius:22px;padding:0 24px;display:flex;align-items:center;gap:18px;box-shadow:0 12px 26px rgba(45,22,48,.07)}
.op .ib{width:62px;height:62px;border-radius:18px;background:#2d1630;color:#f2a516}
.op b{display:block;font:800 25px/1.25 'Inter Display'}.op small{font:500 18px Inter;color:#6d5468}
""", cta="Tell us about your kitchen. DM us")

# ───────── 47 INDIA · Tea stall chain · SINGLE · Montserrat + Source Sans 3 · deep cocoa / saffron / cardamom green
# New technique: conic-gradient ring gauges per outlet (stock levels at a glance).
def ring(lbl, pct, col, txt):
    return f'<div class=rg><div class=ring style="background:conic-gradient({col} {pct*3.6}deg,#3d2a20 0)"><div class=hole><b>{txt}</b></div></div><span>{lbl}</span></div>'
outlets = [("Outlet 1 · Station Road", [("Milk", 70, "#8fb339", "70%"), ("Sugar", 55, "#8fb339", "55%"), ("Cups", 80, "#8fb339", "80%")], "All good till night"),
           ("Outlet 2 · Bus Stand", [("Milk", 18, "#ff5a3c", "18%"), ("Sugar", 60, "#8fb339", "60%"), ("Cups", 35, "#f2a516", "35%")], "Milk low · send 10 L by 4 pm"),
           ("Outlet 3 · College Gate", [("Milk", 50, "#f2a516", "50%"), ("Sugar", 25, "#ff5a3c", "25%"), ("Cups", 65, "#8fb339", "65%")], "Sugar low · send 2 kg")]
P["p47_teastall"] = page("""
body{--f:'Source Sans 3';--h:'Montserrat';background:#22150f;color:#fbf3e4}
body:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 500px at 100% 0,rgba(242,165,22,.16),transparent 70%)}
h1{font-family:'Montserrat';font-size:64px;font-weight:800;letter-spacing:-2px} h1 span{color:#f2a516}
.sub{color:#cdb9a6}
.vis{flex-direction:column;gap:16px}
.ol{flex:1;display:flex;align-items:center;gap:20px;background:#2f1f17;border:2px solid #44302400;border-radius:24px;padding:0 24px;min-height:0}
.ol.al{border-color:#ff5a3c;background:#3a1f17}
.on{width:250px;flex:none;display:flex;flex-direction:column;gap:8px}
.on small{font:700 16px 'Source Sans 3';letter-spacing:3px;text-transform:uppercase;color:#9c8573}.on b{font:800 27px/1.2 'Montserrat'}.on i{font:700 17px/1.35 'Source Sans 3';font-style:normal;padding:6px 12px;border-radius:10px;align-self:flex-start;background:#2c3a17;color:#c3e07a}
.ol.al .on i{background:#ff5a3c;color:#22150f}
.rgs{flex:1;display:flex;justify-content:space-around}
.rg{display:flex;flex-direction:column;align-items:center;gap:8px;font:700 20px 'Source Sans 3';color:#cdb9a6}
.ring{width:132px;height:132px;border-radius:50%;display:flex;align-items:center;justify-content:center}
.hole{width:96px;height:96px;border-radius:50%;background:#22150f;display:flex;align-items:center;justify-content:center}.hole b{font:800 26px 'Montserrat';color:#fbf3e4}
.bt{display:flex;gap:16px}
.bx{flex:1;background:#fbf3e4;color:#22150f;border-radius:20px;padding:18px 22px;display:flex;align-items:center;gap:14px;font:700 20px/1.35 'Source Sans 3'}
.bx .ib{width:50px;height:50px;border-radius:14px;background:#f2a516;color:#22150f}
.smp{font:700 14px 'Source Sans 3';letter-spacing:3px;color:#9c8573;text-align:right;margin-top:-6px}
""", "<h1>3 chai outlets.<br><span>Who runs out of milk first?</span></h1><div class=sub>For tea stall chains: milk, sugar and cups at every outlet, on one screen.</div>",
"".join(f'<div class="ol {"al" if k else ""}"><div class=on><small>{n.split(' · ')[0]}</small><b>{n.split(' · ')[1]}</b><i>{s}</i></div><div class=rgs>{"".join(ring(*r) for r in rs)}</div></div>' for n, rs, s, k in [(o[0], o[1], o[2], i > 0) for i, o in enumerate(outlets)]) +
f'''<div class=smp>SAMPLE LEVELS · updated by outlet staff at 2 pm</div><div class=bt><div class=bx><span class=ib>{ic("truck",26)}</span>Stock list ready for every delivery run.</div><div class=bx><span class=ib>{ic("chart",26)}</span>See which outlet uses the most milk.</div></div>''',
"#fbf3e4", "Run more than one outlet? DM us", "background:#f2a516;color:#22150f")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
