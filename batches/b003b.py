import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 34 INDIA · Caterer · CAROUSEL 6 · Lora + Fira Sans · maroon / gold / cream
# New technique: ticket-stub cards (notched edges via radial-gradient masks) + process story across slides.
CT = """
body{--f:'Fira Sans';--h:'Lora';background:#5a1a2b;color:#fbf3e4}
body:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 500px at 100% 0%,rgba(233,180,76,.18),transparent 70%)}
h1{font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#e9b44c;font-style:italic}
.sub{color:#e6cfc4}
.sn{font:700 17px 'Fira Sans';letter-spacing:3px;color:#e9b44c;margin-top:22px}
.tk{background:#fbf3e4;color:#3a1220;border-radius:18px;-webkit-mask:radial-gradient(circle 16px at 0 50%,transparent 15px,#000 16px) left/51% 100% no-repeat,radial-gradient(circle 16px at 100% 50%,transparent 15px,#000 16px) right/51% 100% no-repeat}
.pill{font:700 14px 'Fira Sans';padding:5px 11px;border-radius:12px;white-space:nowrap}
.g{background:#e3f2e1;color:#2d6a2f}.y{background:#fdf0d2;color:#8a5a00}.r{background:#fbe0e3;color:#a1142f}.n{background:#ece4dc;color:#6b5a4e}
"""
def cslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#e9b44c;color:#3a1220"):
    return page(CT+css, f"<div class=sn>{kick}</div><h1 style='margin-top:10px'>{title}</h1><div class=sub>{sub}</div>", vis, "#fbf3e4", cta, ctacss, tagline=f"{n} / 6")

steps = [("chat", "Enquiry", "Date, place and guest count saved"), ("doc", "Menu", "Fixed and approved by the customer"),
         ("users", "Headcount", "Changes update the quantities"), ("clock", "Staff", "Who reports where, and when"), ("check", "Bill", "Advance and balance, clear")]
P["p34_caterer_s1"] = cslide(1, "FOR CATERERS", "500 guests. 3 menu changes.<br><span>One calm caterer.</span>",
 "How a catering app handles one event, start to finish.",
 '<div class=st>' + "".join(f'<div class="tk s"><span class=no>{i+1}</span><span class=ib>{ic(ic_,30)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i, (ic_, a, b) in enumerate(steps)) + '</div>',
 """.vis{display:flex}.st{flex:1;display:flex;flex-direction:column;gap:12px}
.s{flex:1;display:flex;align-items:center;gap:20px;padding:0 40px}
.s .no{font:700 44px 'Lora';color:#c9a46b;width:40px;font-style:italic}.s .ib{width:60px;height:60px;border-radius:18px;background:#5a1a2b;color:#e9b44c}
.s b{display:block;font:700 27px 'Lora'}.s small{display:block;font:400 20px 'Fira Sans';color:#6b4a52;margin-top:2px}""")

enq = [("14 Dec", "Wedding reception", "500 guests", "Confirmed", "g"), ("18 Dec", "Office lunch", "120 guests", "Quote sent", "y"),
       ("21 Dec", "Engagement", "250 guests", "Site visit", "y"), ("27 Dec", "Birthday party", "80 guests", "New", "r"),
       ("3 Jan", "Housewarming", "150 guests", "Confirmed", "g"), ("9 Jan", "Family get-together", "60 guests", "New", "r")]
P["p34_caterer_s2"] = cslide(2, "STEP 1 · ENQUIRY", "Every enquiry saved<br><span>with date and headcount.</span>",
 "No more \"Which date did they say?\" Follow up before someone else does.",
 f'''<div class="tk L"><div class=th><b>Enquiries · December</b><span>SAMPLE</span></div>{"".join(f'<div class=er><div class=dt>{d}</div><div style="flex:1"><b>{e}</b><small>{g}</small></div><span class="pill {c}">{s}</span></div>' for d,e,g,s,c in enq)}</div>''',
 """.vis{display:flex}.L{flex:1;padding:26px 44px;display:flex;flex-direction:column;gap:10px}
.th{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}.th b{font:700 28px 'Lora'}.th span{font:700 14px 'Fira Sans';letter-spacing:2px;color:#9a7f73}
.er{flex:1;display:flex;align-items:center;gap:18px;padding:10px 16px;border-radius:14px;background:#f3e7d3}
.dt{width:84px;flex:none;font:700 20px 'Fira Sans';color:#5a1a2b}.er b{display:block;font:600 21px 'Fira Sans'}.er small{display:block;font:400 17px 'Fira Sans';color:#6b4a52}""")

menu = [("Starters", ["Paneer tikka", "Veg spring roll", "Corn chaat", "Hara bhara kebab", "Soup counter"]), ("Main course", ["Dal makhani", "Paneer butter masala", "Mix veg", "Jeera rice", "Butter naan", "Raita"]), ("Desserts", ["Gulab jamun", "Rasmalai", "Fruit cream", "Ice cream counter"])]
P["p34_caterer_s3"] = cslide(3, "STEP 2 · MENU", "The menu, fixed<br><span>and approved in writing.</span>",
 "The customer approves it on their phone. Your kitchen sees the same list.",
 f'''<div class="tk M"><div class=mh><b>Wedding reception · 14 Dec</b><small>Sample menu · 500 guests · veg</small></div><div class=mc>{"".join(f'<div class=sec><em>{t}</em>{"".join(f"<p>{x}</p>" for x in items)}</div>' for t,items in menu)}</div>
 <div class=ap><span class=ib>{ic("check",24,w=3)}</span><div><b>Approved by the customer</b><small>12 Nov, 6:40 PM · version 3</small></div></div></div>''',
 """.vis{display:flex}.M{flex:1;padding:30px 46px;display:flex;flex-direction:column;gap:18px}
.mh{text-align:center;border-bottom:2px dashed #d9c3a5;padding-bottom:16px}.mh b{display:block;font:700 30px 'Lora'}.mh small{font:500 17px 'Fira Sans';color:#8a6f63}
.mc{flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:20px}
.sec{background:#f3e7d3;border-radius:16px;padding:18px;display:flex;flex-direction:column;gap:10px}
.sec em{font:italic 700 24px 'Lora';color:#5a1a2b;margin-bottom:4px}.sec p{flex:1;display:flex;align-items:center;font:500 20px/1.3 'Fira Sans';padding-bottom:4px;border-bottom:1px solid #e2d2b9}
.ap{display:flex;gap:14px;align-items:center;background:#2d6a2f;color:#fff;border-radius:16px;padding:16px 20px}
.ap .ib{width:46px;height:46px;border-radius:50%;background:#fff;color:#2d6a2f}.ap b{display:block;font:700 21px 'Fira Sans'}.ap small{font:400 16px 'Fira Sans';color:#d7efd6}""")

qty = [("Paneer", "40 kg", "45 kg"), ("Rice", "50 kg", "56 kg"), ("Dal", "35 kg", "40 kg"), ("Naan dough", "60 kg", "68 kg"), ("Plates and cutlery", "500 sets", "560 sets")]
P["p34_caterer_s4"] = cslide(4, "STEP 3 · HEADCOUNT", "450 became 500?<br><span>Quantities update too.</span>",
 "Change the guest count once. The shopping list follows.",
 f'''<div class=w><div class="tk ch"><em>CHANGE LOG · SAMPLE</em>{"".join(f'<div class=lg2><b>{a}</b><small>{b}</small></div>' for a,b in [("400 → 450 guests","Customer call · 2 Nov"),("450 → 500 guests","Customer call · 10 Nov"),("Menu version 3","Approved · 12 Nov")])}</div>
 <div class="tk qt"><div class=qh><b>Shopping list</b><span>Was</span><span>Now</span></div>{"".join(f'<div class=qr><b>{a}</b><span>{b}</span><span class=nw>{c}</span></div>' for a,b,c in qty)}<div class=qn>Quantities shown are sample numbers. Your own recipe ratios are used.</div></div></div>''',
 """.vis{display:flex}.w{flex:1;display:flex;gap:18px}
.ch{width:330px;flex:none;padding:28px 34px;display:flex;flex-direction:column;gap:12px}.ch em{font:700 15px 'Fira Sans';font-style:normal;letter-spacing:2px;color:#9a7f73}
.lg2{flex:1;background:#f3e7d3;border-radius:14px;padding:16px;display:flex;flex-direction:column;justify-content:center}.lg2 b{font:700 22px 'Lora'}.lg2 small{font:400 16px 'Fira Sans';color:#6b4a52}
.qt{flex:1;padding:28px 40px;display:flex;flex-direction:column;gap:8px}
.qh,.qr{display:flex;align-items:center}.qh b{flex:1;font:700 26px 'Lora'}.qh span{width:110px;text-align:right;font:700 15px 'Fira Sans';color:#9a7f73;letter-spacing:1px}
.qr{flex:1;border-bottom:1px dashed #d9c3a5}.qr b{flex:1;font:600 20px 'Fira Sans'}.qr span{width:110px;text-align:right;font:500 19px 'Fira Sans';color:#9a7f73;text-decoration:line-through}
.qr .nw{color:#5a1a2b;font-weight:700;text-decoration:none}.qn{font:italic 400 16px/1.4 'Lora';color:#8a6f63;margin-top:6px}""")

roster = [("Head cook", "1", "Kitchen · 9 AM"), ("Cooks", "6", "Kitchen · 10 AM"), ("Servers", "14", "Venue · 5 PM"), ("Counter staff", "4", "Venue · 5:30 PM"), ("Cleaning", "5", "Venue · 9 PM"), ("Driver", "2", "Load at 3 PM")]
P["p34_caterer_s5"] = cslide(5, "STEP 4 · STAFF", "Everyone knows<br><span>where to be, and when.</span>",
 "Staff get their reporting time and place. You see who confirmed.",
 f'''<div class=rg>{"".join(f'<div class="tk sc"><span class=cnt>{c}</span><b>{a}</b><small>{t}</small><span class="pill {"g" if i%3 else "y"}">{"Confirmed" if i%3 else "Waiting"}</span></div>' for i,(a,c,t) in enumerate(roster))}</div>''',
 """.vis{display:flex}.rg{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:14px}
.sc{padding:20px 34px;display:flex;flex-direction:column;justify-content:center;gap:4px;position:relative}
.sc .cnt{position:absolute;right:34px;top:18px;font:700 52px/1.2 'Lora';color:#e9b44c}
.sc b{font:700 26px 'Lora'}.sc small{font:500 18px 'Fira Sans';color:#6b4a52}.sc .pill{align-self:flex-start;margin-top:8px}""")

P["p34_caterer_s6"] = cslide(6, "STEP 5 · BILL, THEN YOU", "Want this for your<br><span>catering business?</span>",
 "Enquiries, menus, headcount, staff and billing in one simple app, built around how you work.",
 f'''<div class=w>{peep("Paper","Smile","ShortWavy","MoustacheThin",w=430,h=680)}<div class=rt><div class="tk bl"><em>BILL SUMMARY · SAMPLE</em>{"".join(f'<div class=br><span>{a}</span><b>{b}</b></div>' for a,b in [("Final guest count","500"),("Extra items","Added from log"),("Advance","Received 12 Nov"),("Balance","Due after the event")])}</div>
 <div class=q>Tell us how many events you handle in a month. We will suggest where to start.</div></div></div>''',
 """.vis{align-items:flex-end}.w{display:flex;align-items:flex-end;gap:18px;width:100%}
.rt{flex:1;display:flex;flex-direction:column;gap:14px;padding-bottom:8px}
.bl{padding:26px 40px;display:flex;flex-direction:column;gap:10px}.bl em{font:700 15px 'Fira Sans';font-style:normal;letter-spacing:2px;color:#9a7f73}
.br{display:flex;justify-content:space-between;font:500 24px 'Fira Sans';padding:16px 0;border-bottom:1px dashed #d9c3a5}.br b{font-weight:700}
.q{background:#e9b44c;color:#3a1220;border-radius:20px;padding:30px 28px;font:600 25px/1.4 'Fira Sans'}""",
 cta="DM us to plan yours")

# ───────── 35 USA · Pool service · SINGLE · Comic Relief + DM Sans · sand / coral / deep teal
# Format: spot-the-problem on a marker whiteboard.
wb = [("Mon", "Oak St pool ✓", "Cl ok", ""), ("Tue", "Pine Ave pool ✓", "Cl ___", "1"), ("Wed", "??? who went", "", "2"),
      ("Thu", "Elm Ct pool ✓", "pH 7.4", ""), ("Fri", "Lake Dr pool ✓", "paid?", "3")]
rows = "".join(f'<div class=wr><b>{d}</b><span>{a}</span><i>{c}</i>{f"<span class=ring>{n}</span>" if n else ""}</div>' for d, a, c, n in wb)
P["p35_pool"] = page("""
body{--f:'DM Sans';background:#fff3e0;color:#0f3d3e}
.sea{position:absolute;left:0;right:0;bottom:0;height:300px;background:repeating-linear-gradient(170deg,#0f766e 0 26px,#139488 26px 52px);opacity:.95}
h1{font-size:64px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#ef5b4b}
.sub{color:#5b6b67}
.vis{gap:22px;align-items:stretch}
.wbd{flex:1.35;background:#fff;border:14px solid #c9ced3;border-radius:18px;padding:22px 24px;display:flex;flex-direction:column;gap:8px;box-shadow:0 26px 50px rgba(15,61,62,.2);position:relative;min-width:0}
.wbd h4{font:700 30px 'Comic Relief';color:#1d4ed8;border-bottom:3px solid #1d4ed8;padding-bottom:6px;margin-bottom:4px}
.wr{flex:1;display:flex;align-items:center;gap:14px;font:400 25px 'Comic Relief';color:#1f2937;position:relative;border-bottom:1px dashed #e5e7eb}
.wr b{width:62px;flex:none;color:#1d4ed8}.wr i{font-style:normal;margin-left:auto;color:#15803d}
.ring{position:absolute;right:-8px;top:50%;width:46px;height:46px;margin-top:-23px;border-radius:50%;background:#ef5b4b;color:#fff;font:800 22px/1 'DM Sans';display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 5px rgba(239,91,75,.25)}
.wr:has(.ring){padding-right:56px}
.mk{display:flex;gap:10px;margin-top:4px}.mk i{width:70px;height:16px;border-radius:8px}
.R{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.f{flex:1;background:#0f3d3e;color:#fff;border-radius:22px;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.f .t{display:flex;gap:12px;align-items:center}.f .n{width:38px;height:38px;border-radius:50%;background:#ef5b4b;font:800 18px/1 'DM Sans';display:flex;align-items:center;justify-content:center;flex:none}
.f b{font:700 22px/1.3 'DM Sans'}.f small{font:400 18px/1.45 'DM Sans';color:#bfe3dd}
""", "<h1>Spot the 3 problems<br><span>on this pool board.</span></h1><div class=sub>A sample week for a pool service company. Then see how software fixes each one.</div>",
f'''<div class=wbd><h4>Pool route · this week</h4>{rows}<div class=mk><i style="background:#1d4ed8"></i><i style="background:#15803d"></i><i style="background:#ef5b4b"></i></div></div>
<div class=R>{"".join(f'<div class=f><div class=t><span class=n>{n}</span><b>{a}</b></div><small>{b}</small></div>' for n,a,b in [("1","Missing water readings","Techs log chlorine and pH on their phone at each pool."),("2","No one knows who went","Every visit has a tech name, time and photo."),("3","\"Paid?\" on a whiteboard","Invoices go out after each visit and payments are tracked.")])}</div>''',
"#0f3d3e", "Want this for your pool business? DM us", "background:#ef5b4b;color:#fff", bg="<div class=sea></div>", logo_color="#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
