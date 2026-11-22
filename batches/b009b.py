import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 62 INDIA · Home baker · CAROUSEL 6 · Cardo + DM Sans · strawberry pink / chocolate / vanilla
# New techniques: top-view CSS cake (piped border via repeating radial dots) and "field + why" checklist cards.
HB = """
body{--f:'DM Sans';--h:'Cardo';background:#fff6e8;color:#3d2218}
h1{font-family:'Cardo';font-size:68px;font-weight:700;letter-spacing:-.5px} h1 span{color:#d9467a}
.sub{color:#7a5a4a}
.kk{font:700 17px 'DM Sans';letter-spacing:4px;color:#d9467a;margin-top:22px}
.fq{flex:1;background:#fff;border-radius:28px;padding:26px 28px;display:flex;flex-direction:column;gap:14px;box-shadow:0 16px 36px rgba(61,34,24,.08)}
.fh{display:flex;align-items:center;gap:16px}
.fh span{width:58px;height:58px;border-radius:50%;background:#3d2218;color:#fff6e8;font:700 28px/58px Cardo;text-align:center;flex:none}
.fh b{font:700 38px/1.2 Cardo}
.inp{border:2px solid #f0d9c8;border-radius:16px;padding:16px 18px;font:600 24px 'DM Sans';background:#fffaf3;display:flex;gap:10px;flex-wrap:wrap;align-items:center}
.inp em{font-style:normal;font:700 21px 'DM Sans';padding:8px 14px;border-radius:12px;background:#fbe3ec;color:#a8285a}
.inp em.n{background:#f3ebe3;color:#7a5a4a}
.why{display:flex;gap:12px;align-items:flex-start;font:500 22px/1.4 'DM Sans';color:#5d4234}
.fq{justify-content:space-between}
.bad{display:flex;align-items:center;justify-content:space-between;gap:12px;background:#f3ebe3;border-radius:18px 18px 18px 6px;padding:14px 18px;font:500 21px/1.35 'DM Sans';color:#7a5a4a}
.bad em{font-style:normal;font:700 18px 'DM Sans';color:#fff;background:#3d2218;padding:6px 12px;border-radius:10px;white-space:nowrap;flex:none}
.why svg{color:#d9467a;flex:none;margin-top:3px}
"""
def hb(n, head, vis, css="", cta="Swipe", ctacss="background:#3d2218;color:#fff6e8"):
    return page(HB + ".vis{flex-direction:column;gap:18px}" + css, head, vis, "#3d2218", cta, ctacss, tagline=f"{n} / 6")
BAD = {1:("“Need a chocolate cake for Saturday.”","How big?"),2:("“Same as last time.”","Was it eggless?"),3:("“Write happy bday and her name.”","Which spelling?"),4:("“Something nice, pink theme.”","What is nice?"),5:("“Evening is fine.”","5 pm or 9 pm?"),6:("“Near the main road.”","Which road?"),7:("“Will pay at pickup.”","And if they cancel?")}
def fq(k, title, inp, why):
    b, q = BAD[k]
    return f'<div class=fq><div class=fh><span>{k}</span><b>{title}</b></div><div class=bad><span>On chat: {b}</span><em>{q}</em></div><div class=inp>{inp}</div><div class=why>{ic("spark",26)}<span>{why}</span></div></div>'
def ch(*a):
    return "".join(f'<em class="{"" if on else "n"}">{t}</em>' for i,(t,on) in enumerate(a))

P["p62_homebaker_s1"] = hb(1, """<div class=kk>FOR HOME BAKERS</div><h1 style="margin-top:10px">7 things your cake<br>order form <span>must ask.</span></h1><div class=sub>Save this before your next order comes in on chat.</div>""",
f'''<div class=hro><div class=plate><div class=cake><div class=top><b>Happy Birthday<br>Riya</b></div></div></div>
<div class=hl>{"".join(f'<div><span>{i}</span>{t}</div>' for i,t in enumerate(["Flavour + weight","Egg or eggless","Message text","Design photo","Date + time","Address","Advance"],1))}</div></div>''',
""".hro{flex:1;display:flex;gap:22px}
.plate{flex:1.15;background:#3d2218;border-radius:30px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.cake{width:420px;height:420px;border-radius:50%;background:#f7c6d6;box-shadow:0 0 0 22px #fff6e8,0 0 0 26px #e7d3c0;display:flex;align-items:center;justify-content:center;position:relative}
.cake:before{content:"";position:absolute;inset:10px;border-radius:50%;background:radial-gradient(circle,#fff 9px,transparent 10px) 0 0/34px 34px;-webkit-mask:radial-gradient(circle,transparent 168px,#000 170px)}
.top{width:300px;height:300px;border-radius:50%;background:#fbe3ec;display:flex;align-items:center;justify-content:center;text-align:center}
.top b{font:700 34px/1.3 Cardo;color:#a8285a}
.hl{flex:1;display:flex;flex-direction:column;gap:10px}
.hl div{flex:1;background:#fff;border-radius:18px;display:flex;align-items:center;gap:14px;padding:0 18px;font:700 22px 'DM Sans'}
.hl span{width:40px;height:40px;border-radius:50%;background:#d9467a;color:#fff;font:700 20px/40px Cardo;text-align:center;flex:none}
""")

P["p62_homebaker_s2"] = hb(2, """<h1 style="margin-top:30px">Start with <span>what they want.</span></h1>""",
fq(1, "Flavour and weight", ch(("Chocolate truffle",1),("1 kg",1),("Half kg",0),("2 kg",0)), "Weight decides your ingredients, box size and price. Never guess it from chat.")
+ fq(2, "Egg or eggless?", ch(("Eggless",1),("With egg",0)), "Ask every single time, even for regular customers. One mix-up can lose a customer."))

P["p62_homebaker_s3"] = hb(3, """<h1 style="margin-top:30px">Get the design <span>in writing.</span></h1>""",
fq(3, "Message on the cake", '<span style="font:600 26px Cardo">“Happy Birthday Riya”</span><em>Exact spelling</em>', "Ask them to type it. Names are spelt in many ways, and icing can't be undone.")
+ fq(4, "Photo of the design they like", ch(("1 photo added",1),("Colours: pink + white",1)), "A photo removes the “I wanted it more pink” talk at pickup."))

P["p62_homebaker_s4"] = hb(4, """<h1 style="margin-top:30px">Then <span>when and where.</span></h1>""",
fq(5, "Date and time", ch(("Sat, 14 Dec",1),("Pickup",0),("Delivery",1),("6 to 7 pm",1)), "Plan your baking day backwards from this time.")
+ fq(6, "Address with a landmark", '<span style="font:500 22px/1.4 DM Sans">Flat 302, Sample Residency, near the park gate</span>', "Saves the “where exactly?” calls while the cake is in the car."))

orders = [("Sat 14", "Chocolate truffle · 1 kg", "Eggless", "Advance paid"), ("Sat 14", "Red velvet · half kg", "With egg", "Advance paid"), ("Sun 15", "Pineapple · 1 kg", "Eggless", "Advance due")]
P["p62_homebaker_s5"] = hb(5, """<h1 style="margin-top:30px">Last: the advance.<br><span>Then it's all in one list.</span></h1>""",
fq(7, "Advance paid by UPI", ch(("Advance received",1),("Balance at pickup",1)), "Start baking only after the advance shows up.")
+ f'''<div class=ol><small>YOUR ORDERS · SAMPLE</small>{"".join(f'<div class=orw><b>{d}</b><div><strong>{a}</strong><span>{e}</span></div><em class="{"ok" if "paid" in p else "du"}">{p}</em></div>' for d,a,e,p in orders)}</div>''',
""".ol{flex:1.1;background:#3d2218;color:#fff6e8;border-radius:28px;padding:22px 26px;display:flex;flex-direction:column;gap:10px}
.ol small{font:700 14px 'DM Sans';letter-spacing:3px;color:#f7c6d6}
.orw{flex:1;display:flex;align-items:center;gap:16px;border-top:1px solid rgba(255,246,232,.15)}
.orw b{font:700 22px Cardo;width:70px;flex:none}.orw div{flex:1}.orw strong{display:block;font:700 21px 'DM Sans'}.orw span{font:500 17px 'DM Sans';color:#e7d3c0}
.orw em{font-style:normal;font:700 16px 'DM Sans';padding:6px 12px;border-radius:10px}.ok{background:#d8f1df;color:#16803d}.du{background:#fbe3ec;color:#a8285a}
""")

P["p62_homebaker_s6"] = hb(6, """<div class=kk>FOR YOUR HOME BAKERY</div><h1 style="margin-top:10px">Want this as<br><span>your own order form?</span></h1><div class=sub>We build simple order websites for home bakers. Customers fill it in, you get the full order.</div>""",
f'''<div class=w6>{peep("Paper","Smile","Bun","None",w=360,h=600)}<div class=o6>{"".join(f'<div class=q6>{ic(i,30)}<b>{t}</b></div>' for i,t in [("doc","All 7 questions, every time"),("img","Design photo upload"),("cal","Orders sorted by date"),("rupee","Advance status")])}</div></div>''',
""".w6{flex:1;display:flex;align-items:flex-end;gap:18px}
.o6{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q6{flex:1;background:#fff;border-radius:24px;display:flex;align-items:center;gap:18px;padding:0 26px;box-shadow:0 14px 30px rgba(61,34,24,.08)}
.q6 svg{color:#d9467a;flex:none}.q6 b{font:700 30px/1.25 Cardo}
""", cta="Bake from home? DM us", ctacss="background:#d9467a;color:#fff")

# ───────── 65 USA · Moving company · CAROUSEL 5 · Bitter + Open Sans · kraft brown / tape blue / white
# New technique: stacked CSS cardboard boxes with tape strips and marker labels.
MV = """
body{--f:'Open Sans';--h:'Bitter';background:#f7f3ec;color:#1f2a44}
h1{font-family:'Bitter';font-size:64px;font-weight:800;letter-spacing:-1px} h1 span{color:#2f6fdf}
.sub{color:#5e6677}
.stp{align-self:flex-start;margin-top:22px;font:800 17px 'Open Sans';letter-spacing:3px;background:#c89b6a;color:#fff;padding:8px 14px;border-radius:8px}
.cd{background:#fff;border-radius:26px;box-shadow:0 16px 36px rgba(31,42,68,.08)}
"""
def mv(n, head, vis, css="", cta="Swipe", ctacss="background:#2f6fdf;color:#fff"):
    return page(MV + css, head, vis, "#1f2a44", cta, ctacss, tagline=f"{n} / 5")
def box(w, h, label, tape=True, extra=""):
    return f'<div class=bx style="width:{w}px;height:{h}px;{extra}">{"<i class=tp></i>" if tape else ""}<span>{label}</span></div>'

P["p65_moving_s1"] = mv(1, """<h1 style="margin-top:30px">Moving quotes by phone?<br><span>Let them list it first.</span></h1><div class=sub>A moving quote form where customers add rooms, big items and access details.</div>""",
f'''<div class=pile><div class=row>{box(300,220,"BEDROOM 1")}{box(260,220,"BOOKS")}</div><div class=row>{box(220,250,"FRAGILE · GLASS",extra="background:#d9b083")}{box(360,250,"KITCHEN")}</div><div class=row>{box(420,240,"LIVING ROOM")}{box(200,240,"LAMPS")}</div>
<div class=tg>{ic("check",26,w=3)}Full list before you quote</div></div>''',
""".pile{flex:1;background:#1f2a44;border-radius:30px;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;padding:24px 24px 0;overflow:hidden;position:relative}
.row{display:flex;gap:6px;margin-top:6px}
.bx{background:#c89b6a;border-radius:6px 6px 2px 2px;position:relative;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 -14px 0 rgba(0,0,0,.08);overflow:hidden}
.tp{position:absolute;left:0;right:0;top:46%;height:34px;background:rgba(47,111,223,.85);display:block}
.bx span{position:relative;font:800 24px 'Bitter';color:#1f2a44;background:#fff;padding:6px 12px;border-radius:4px;transform:rotate(-2deg)}
.tg{position:absolute;left:24px;top:24px;background:#fff;border-radius:14px;padding:12px 16px;font:700 21px 'Open Sans';display:flex;align-items:center;gap:10px}
.tg svg{color:#2f6fdf}
""")

rooms = [("home", "Living room", 1), ("users", "Bedrooms", 3), ("cup", "Kitchen", 1), ("box", "Garage", 1), ("doc", "Home office", 1), ("leaf", "Patio", 0)]
P["p65_moving_s2"] = mv(2, """<div class=stp>STEP 1</div><h1 style="margin-top:14px">They pick the rooms.</h1><div class=sub>A three-bedroom home looks different from a studio. Now you know which one it is.</div>""",
f'''<div class=rg>{"".join(f'<div class="cd rm"><span class=ri>{ic(i,34)}</span><b>{t}</b><div class=ct><i>−</i><strong>{c}</strong><i class=pl>+</i></div></div>' for i,t,c in rooms)}</div>''',
""".vis{flex-direction:column}.rg{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.rm{padding:22px 24px;display:flex;flex-direction:column;justify-content:space-between}
.ri{width:62px;height:62px;border-radius:16px;background:#e7effd;color:#2f6fdf;display:flex;align-items:center;justify-content:center}
.rm b{font:800 30px 'Bitter'}
.ct{display:flex;align-items:center;gap:16px}.ct i{width:48px;height:48px;border-radius:50%;border:2px solid #d4dae6;font:700 26px/44px 'Open Sans';font-style:normal;text-align:center;color:#5e6677}
.ct i.pl{background:#2f6fdf;border-color:#2f6fdf;color:#fff}.ct strong{font:800 32px 'Bitter';min-width:24px;text-align:center}
""")

items = [("Sofa", "2", ""), ("Queen bed", "3", ""), ("Dresser", "2", ""), ("Fridge", "1", ""), ("Washer and dryer", "1 set", ""), ("Piano", "1", "Needs special handling"), ("Boxes (about)", "40", "")]
P["p65_moving_s3"] = mv(3, """<div class=stp>STEP 2</div><h1 style="margin-top:14px">They add the <span>big items.</span></h1>""",
f'''<div class="cd il"><div class=ih><span>BIG ITEMS · SAMPLE</span><span>Count</span></div>{"".join(f'<div class="ir{" fl" if n else ""}"><div><b>{a}</b>{f"<small>{n}</small>" if n else ""}</div><strong>{c}</strong></div>' for a,c,n in items)}</div>''',
""".vis{flex-direction:column}.il{flex:1;padding:24px 28px;display:flex;flex-direction:column;gap:8px}
.ih{display:flex;justify-content:space-between;font:700 15px 'Open Sans';letter-spacing:3px;color:#8a92a3}
.ir{flex:1;display:flex;align-items:center;justify-content:space-between;border-bottom:2px dashed #e6e9f0;padding:0 6px}
.ir b{font:700 26px 'Open Sans'}.ir small{display:block;font:600 17px 'Open Sans';color:#b25e12}
.ir strong{font:800 30px 'Bitter';background:#f7f3ec;border-radius:12px;padding:6px 16px;min-width:90px;text-align:center}
.ir.fl{background:#fff4e6;border-radius:14px;border-bottom:none;padding:0 14px}
""")

def ac(t, rows):
    return f'<div class="cd ad"><h4>{t}</h4>{"".join(f"<div class=ar><span>{a}</span><b>{b}</b></div>" for a,b in rows)}</div>'
P["p65_moving_s4"] = mv(4, """<div class=stp>STEP 3</div><h1 style="margin-top:14px">They add the <span>access details.</span></h1><div class=sub>Stairs, elevators and parking change the job. Now you know before moving day.</div>""",
f'''<div class=two>{ac("Moving from", [("ZIP code","30309"),("Floor","3rd"),("Elevator","No"),("Truck parking","Street, close")])}<div class=arw>{ic("arrow",44,w=3)}</div>{ac("Moving to", [("ZIP code","30024"),("Floor","Ground"),("Elevator","Not needed"),("Truck parking","Driveway")])}</div>
<div class=dt>{ic("cal",30)}<span><b>Moving day:</b> Saturday, morning start · sample</span></div>''',
""".vis{flex-direction:column;gap:16px}
.two{flex:1;display:flex;align-items:stretch;gap:12px}
.ad{flex:1;padding:24px;display:flex;flex-direction:column;gap:10px}
.ad h4{font:800 28px 'Bitter';color:#2f6fdf}
.ar{flex:1;display:flex;flex-direction:column;justify-content:center;background:#f7f3ec;border-radius:14px;padding:0 16px}
.ar span{font:600 18px 'Open Sans';color:#8a92a3}.ar b{font:700 26px 'Open Sans'}
.arw{display:flex;align-items:center;color:#c89b6a}
.dt{display:flex;align-items:center;gap:14px;background:#1f2a44;color:#fff;border-radius:20px;padding:20px 24px;font:500 22px 'Open Sans'}
.dt svg{color:#c89b6a;flex:none}
""")

P["p65_moving_s5"] = mv(5, """<h1 style="margin-top:30px">Want a quote form<br><span>like this?</span></h1><div class=sub>We build quote forms and booking pages for moving companies.</div>""",
f'''<div class=w5>{peep("ArmsCrossed","Smile","ShortWavy","Chin",w=380,h=620)}<div class=o5>{"".join(f'<div class="cd q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Rooms"),(2,"Big items"),(3,"Access details"),(4,"Sent to your inbox")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:60px;height:60px;border-radius:12px;background:#c89b6a;color:#fff;font:800 28px/60px 'Bitter';text-align:center;flex:none}
.q5 b{font:800 30px/1.25 'Bitter'}
""", cta="Run a moving company? DM us", ctacss="background:#1f2a44;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
