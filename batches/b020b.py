import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 116 USA · Catering company · CAROUSEL 5 · Bitter + Inter · linen / navy / tomato
# New techniques: SVG buffet line (chafing dishes with lids and steam on a draped table), quote-builder form,
# tray calculator cards, event sheet with timeline + staff + packing list.
CT = """
body{--f:'Inter';--h:'Bitter';background:#f4efe6;color:#1d2b4a}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:0;line-height:1.2} h1 span{color:#e0533d}
.sub{color:#5d6478}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Inter;letter-spacing:3px;color:#e0533d}
.kt b{width:44px;height:44px;border-radius:50%;background:#1d2b4a;color:#f4efe6;font:800 22px/1 Bitter;display:flex;align-items:center;justify-content:center}
.cd{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(29,43,74,.08)}
.lb{font:700 13px Inter;letter-spacing:3px;color:#8a8f9c}
"""
def ct(n, head, vis, css="", cta="Swipe", ctacss="background:#1d2b4a;color:#f4efe6"):
    return page(CT + css, head, vis, "#1d2b4a", cta, ctacss, tagline=f"{n} / 5")
def dish(x, lid=True):
    s = f'<g transform="translate({x},0)"><rect x="0" y="150" width="170" height="20" rx="6" fill="#b9c0cc"/><path d="M8 150 Q85 196 162 150" fill="#d8dde5"/>'
    s += '<rect x="20" y="168" width="8" height="34" fill="#8a93a3"/><rect x="142" y="168" width="8" height="34" fill="#8a93a3"/>'
    if lid:
        s += '<path d="M10 150 Q85 70 160 150 Z" fill="#dfe4ea" stroke="#aab3c0" stroke-width="3"/><rect x="72" y="96" width="26" height="10" rx="5" fill="#8a93a3"/>'
    else:
        s += '<ellipse cx="85" cy="150" rx="78" ry="14" fill="#e0533d"/><ellipse cx="85" cy="147" rx="60" ry="8" fill="#f07a5e"/>'
        s += '<path d="M60 128 q-8 -12 0 -24 q8 -12 0 -24 M85 124 q-8 -12 0 -24 q8 -12 0 -24 M110 128 q-8 -12 0 -24 q8 -12 0 -24" stroke="#c8ccd4" stroke-width="4" fill="none" stroke-linecap="round"/>'
    return s + '</g>'
buffet = ('<svg viewBox="0 0 860 330" width="{w}" height="{h}">' + dish(30) + dish(240, False) + dish(450) + dish(660, False)
          + '<rect x="0" y="200" width="860" height="22" rx="6" fill="#1d2b4a"/><path d="M0 222 H860 V300 Q800 320 740 300 T620 300 T500 300 T380 300 T260 300 T140 300 T20 300 L0 300 Z" fill="#e8ddc8"/>'
          + '<path d="M0 240 H860" stroke="#d4c6ab" stroke-width="3"/></svg>')
P["p116_catering_s1"] = ct(1, """<h1>Event quotes take days<br>of back-and-forth?<br><span>Send a clear quote<br>the same day.</span></h1>""",
f'''<div class=w1><div class=bf1><div class=qt1><div><span class=lb>QUOTE Q-214 · SAMPLE</span><b>Office lunch · 120 guests</b></div><em>Sent the same day</em></div>{buffet.format(w=880,h=338)}</div>
<div class=rw1>{"".join(f'<div class="cd c1"><span class=lb>{a}</span><b>{b}</b></div>' for a,b in [("STEP 1","Quote builder"),("STEP 2","Tray counts"),("STEP 3","Event sheet")])}</div></div>''',
""".w1{flex:1;display:flex;flex-direction:column;gap:16px}
.bf1{flex:1;background:#1d2b4a;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:space-evenly;background-image:radial-gradient(circle at 50% 30%,#2d3e66,#1d2b4a 70%)}.bf1 svg{display:block}
.qt1{width:820px;background:#fff;border-radius:18px;padding:16px 22px;display:flex;justify-content:space-between;align-items:center}.qt1 div{display:flex;flex-direction:column;gap:4px}.qt1 b{font:800 28px/1.25 Bitter}
.qt1 em{font-style:normal;font:700 18px Inter;background:#e0533d;color:#fff;padding:9px 14px;border-radius:10px}
.rw1{flex:none;display:flex;gap:14px}.c1{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:6px;border-top:10px solid #e0533d}.c1 b{font:800 28px/1.25 Bitter}
""")

P["p116_catering_s2"] = ct(2, """<div class=kt><b>1</b>QUOTE BUILDER</div><h1 style="margin-top:18px">The client fills it in.<br><span>You review and send.</span></h1>""",
browser(f'''<div class=fm2><div class=hd2><b>Plan your event</b><span class=lb>SAMPLE</span></div>
<div class=g2>{"".join(f'<div class=f2><span>{a}</span><b>{b}</b></div>' for a,b in [("Event","Office lunch"),("Date","Fri, Dec 11"),("Guests","120"),("ZIP code","00000 · sample")])}</div>
<div class=o2><span>Service style</span><div>{"".join(f'<em class="{"on" if k else ""}">{t}</em>' for t,k in [("Buffet",1),("Plated",0),("Drop-off",0)])}</div></div>
<div class=o2><span>Menu</span><div>{"".join(f'<em class="{"on" if k else ""}">{t}</em>' for t,k in [("Roast chicken",1),("Veggie pasta",1),("Garden salad",1),("Rice pilaf",1),("Cookies",1),("Fish",0)])}</div></div>
<div class=o2><span>Add-ons</span><div>{"".join(f'<em class="{"on" if k else ""}">{t}</em>' for t,k in [("Servers",1),("Plates and cutlery",1),("Setup and cleanup",0)])}</div></div>
<div class=bt2>Send my request</div></div>''', "quote.yourcatering.com · sample", "flex:1", bar="#ebe4d6"),
""".vis{flex-direction:column}
.fm2{flex:1;padding:20px 26px;display:flex;flex-direction:column;gap:12px;background:#fffdf9}
.hd2{display:flex;justify-content:space-between;align-items:center}.hd2 b{font:800 32px/1.25 Bitter}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.f2{border:2px solid #e8e2d6;border-radius:14px;padding:10px 16px;display:flex;flex-direction:column;gap:2px}.f2 span{font:600 15px Inter;color:#8a8f9c}.f2 b{font:700 23px Inter}
.o2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:10px;border-top:1.5px solid #efe9de}
.o2>span{font:600 16px Inter;color:#8a8f9c}.o2 div{display:flex;flex-wrap:wrap;gap:8px}
.o2 em{font-style:normal;font:600 21px Inter;padding:11px 16px;border-radius:12px;background:#f4efe6}
.o2 em.on{background:#1d2b4a;color:#fff}
.bt2{background:#e0533d;color:#fff;border-radius:14px;text-align:center;font:700 21px Inter;padding:15px}
""")

trays = [("Roast chicken", "1 tray feeds 20", "6 trays"), ("Veggie pasta", "1 tray feeds 25", "5 trays"), ("Garden salad", "1 bowl feeds 30", "4 bowls"),
         ("Rice pilaf", "1 tray feeds 30", "4 trays"), ("Cookies", "2 per guest", "240 pcs")]
P["p116_catering_s3"] = ct(3, """<div class=kt><b>2</b>TRAY COUNTS</div><h1 style="margin-top:18px">120 guests?<br><span>The app counts the trays.</span></h1>""",
f'''<div class="cd ls3"><div class=h3r><span class=lb>OFFICE LUNCH · 120 GUESTS · SAMPLE</span><span class=lb>YOUR OWN RULES</span></div>
{"".join(f'<div class=r3><div><b>{a}</b><span>{b}</span></div><em>{c}</em></div>' for a,b,c in trays)}</div>
<div class=nt3>You set how many each tray feeds once. Every quote and kitchen list uses it.</div>''',
""".vis{flex-direction:column;gap:14px}
.ls3{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.h3r{display:flex;justify-content:space-between;padding-bottom:8px}
.r3{flex:1;display:flex;align-items:center;justify-content:space-between;border-top:1.5px solid #efe9de;gap:16px}
.r3 div{display:flex;flex-direction:column;gap:4px}.r3 b{font:800 30px/1.25 Bitter}.r3 span{font:500 20px Inter;color:#6b7184}
.r3 em{font-style:normal;font:800 28px Bitter;background:#fdebe6;color:#c23f2a;border-radius:14px;padding:10px 18px;white-space:nowrap}
.nt3{flex:none;background:#1d2b4a;color:#f4efe6;border-radius:18px;padding:16px 22px;font:600 21px/1.4 Inter}
""")

tl = [("9:30 am", "Load van · 21 trays"), ("10:45 am", "Arrive, set up buffet"), ("12:00 pm", "Lunch served"), ("1:30 pm", "Clear and pack up")]
P["p116_catering_s4"] = ct(4, """<div class=kt><b>3</b>EVENT SHEET</div><h1 style="margin-top:18px">One sheet for<br><span>the kitchen and the crew.</span></h1>""",
f'''<div class=w4><div class="cd ev4"><span class=lb>EVENT SHEET · SAMPLE</span><h3>Office lunch · Fri, Dec 11</h3><span class=ad>Sample Office, 5th floor · 120 guests · buffet</span>
{"".join(f'<div class=t4><em>{a}</em><b>{b}</b></div>' for a,b in tl)}</div>
<div class=sd4><div class="cd st4"><span class=lb>CREW</span>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("Lead","Crew 1"),("Servers","Crew 2, 3"),("Driver","Crew 4")])}</div>
<div class="cd pk4"><span class=lb>PACK LIST</span>{"".join(f'<i>{t}</i>' for t in ["4 chafing dishes","8 fuel cans","120 plates","Serving spoons","Table covers"])}</div></div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.ev4{flex:1.3;padding:22px 24px;display:flex;flex-direction:column;gap:8px;border-top:12px solid #e0533d}
.ev4 h3{font:800 30px/1.25 Bitter}.ev4 .ad{font:500 18px Inter;color:#6b7184;padding-bottom:6px}
.t4{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px dashed #e8e2d6}
.t4 em{width:120px;flex:none;font-style:normal;font:800 22px Bitter;color:#e0533d}.t4 b{font:600 22px/1.3 Inter}
.sd4{flex:1;display:flex;flex-direction:column;gap:14px}
.st4{flex:none;padding:18px 20px;display:flex;flex-direction:column;gap:8px}
.st4 div{display:flex;justify-content:space-between;border-top:1.5px solid #efe9de;padding-top:8px}.st4 b{font:700 20px Inter}.st4 span{font:500 19px Inter;color:#6b7184}
.pk4{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:8px;background:#1d2b4a;color:#fff}.pk4 .lb{color:#aab3c8}
.pk4 i{flex:1;font-style:normal;font:600 19px Inter;display:flex;align-items:center;gap:10px;border-top:1.5px solid rgba(255,255,255,.12)}
.pk4 i:before{content:"";width:18px;height:18px;border-radius:5px;border:2.5px solid #e0533d;flex:none}
""")

P["p116_catering_s5"] = ct(5, """<h1>Run a catering<br>company?<br><span>Let's build your<br>quote and event app.</span></h1>""",
f'''<div class=c5><div class=bf5>{buffet.format(w=600,h=230)}</div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Online quote form","Tray counts from guests","Event sheet for the crew","Deposits and invoices"],1))}</div></div>''',
""".c5{flex:1;background:#e0533d;color:#fff;border-radius:30px;padding:24px;display:flex;flex-direction:column;gap:16px}
.bf5{flex:none;background:#1d2b4a;border-radius:22px;display:flex;justify-content:center;padding:12px}.bf5 svg{display:block}
.ls5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.r5{background:#fff;color:#1d2b4a;border-radius:18px;display:flex;align-items:center;gap:14px;padding:0 20px}
.r5 em{width:50px;height:50px;border-radius:50%;background:#1d2b4a;color:#fff;font:800 24px/1 Bitter;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:800 26px/1.25 Bitter}
""", cta="Caterer? DM us", ctacss="background:#1d2b4a;color:#fff")

# ───────── 118 INDIA · Warehouse / godown rental · CAROUSEL 6 · Montserrat + Open Sans · pallet pine / charcoal / teal
# New techniques: top-down warehouse floor plan with client-coloured bays + dock doors and trucks, GRN document,
# picking list by bay, monthly stock statement table.
WH = """
body{--f:'Open Sans';--h:'Montserrat';background:#22272e;color:#f2efe8}
h1{font-family:'Montserrat';font-weight:800;font-size:58px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#e3b873}
.sub{color:#aab1bb}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Open Sans';letter-spacing:3px;color:#5cc8c2}
.kt b{width:44px;height:44px;border-radius:12px;background:#1d8a8a;color:#fff;font:800 22px/1 Montserrat;display:flex;align-items:center;justify-content:center}
.cd{background:#2d333c;border-radius:22px;border:1.5px solid #3a414b}
.lb{font:700 13px 'Open Sans';letter-spacing:3px;color:#8f98a4}
"""
def wh(n, head, vis, css="", cta="Swipe", ctacss="background:#e3b873;color:#22272e"):
    return page(WH + css, head, vis, "#f2efe8", cta, ctacss, tagline=f"{n} / 6")
CL = {"A": ("#1d8a8a", "Client A"), "B": ("#e3b873", "Client B"), "C": ("#b55d8a", "Client C"), "D": ("#6d8fd6", "Client D"), "": ("", "Free")}
layout = ["AAABB-", "AAABBC", "DD-BCC", "DDD-CC"]
def plan(cell=110, gap=10, hl=None):
    rows = []
    for r, row in enumerate(layout):
        cells = []
        for c, k in enumerate(row):
            k = "" if k == "-" else k
            code = f"{'ABCD'[r]}{c+1}"
            st = f"background:{CL[k][0]}" if k else ""
            h = " hl" if hl and code in hl else ""
            cells.append(f'<div class="by{"" if k else " fr"}{h}" style="{st}"><b>{code}</b><span>{"Free" if not k else CL[k][1]}</span></div>')
        rows.append("".join(cells))
    return "".join(rows)
P["p118_godown_s1"] = wh(1, """<h1>Which client's goods<br>are in which bay?<br><span>See every bay, live.</span></h1>""",
f'''<div class=fp1><div class=dk1>{"".join(f'<div class=dr1><i></i><span>Dock {i}</span></div>' for i in (1,2,3))}</div><div class=gd1>{plan()}</div></div>
<div class=lg1>{"".join(f'<span><i style="background:{CL[k][0]}"></i>{CL[k][1]}</span>' for k in "ABCD")}<span><i class=fr></i>Free</span><span class=lb>SAMPLE</span></div>''',
""".vis{flex-direction:column;gap:14px}
.fp1{flex:1;display:flex;gap:14px;background:#1a1e24;border-radius:28px;padding:18px;background-image:linear-gradient(#262b33 1px,transparent 1px),linear-gradient(90deg,#262b33 1px,transparent 1px);background-size:40px 40px}
.dk1{width:120px;flex:none;display:flex;flex-direction:column;gap:14px}
.dr1{flex:1;background:repeating-linear-gradient(-45deg,#e3b873 0 14px,#22272e 14px 28px);border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:8px}
.dr1 i{width:64px;height:40px;border-radius:8px;background:#f2efe8;display:block}
.dr1 span{font:700 16px Montserrat;background:#22272e;padding:4px 8px;border-radius:6px}
.gd1{flex:1;display:grid;grid-template-columns:repeat(6,1fr);grid-template-rows:repeat(4,1fr);gap:10px}
.by{border-radius:12px;padding:10px;display:flex;flex-direction:column;justify-content:space-between;color:#1a1e24}
.by b{font:800 22px Montserrat}.by span{font:700 13px 'Open Sans'}
.by.fr{border:3px dashed #5a636f;color:#aab1bb}
.lg1{flex:none;display:flex;gap:18px;align-items:center;font:600 18px 'Open Sans'}.lg1 span{display:flex;align-items:center;gap:8px}.lg1 .lb{margin-left:auto}
.lg1 i{width:20px;height:20px;border-radius:6px;display:block}.lg1 i.fr{border:2.5px dashed #5a636f}
""")

P["p118_godown_s2"] = wh(2, """<div class=kt><b>1</b>SPACE BOOKING</div><h1 style="margin-top:18px">A new client needs space?<br><span>See free bays first.</span></h1>""",
f'''<div class=w2><div class=gd2>{plan(hl={"A6","C3","D4"})}</div>
<div class="cd bk2"><span class=lb>BOOKING · SAMPLE</span><b>Client E</b>{"".join(f'<div class=r2><span>{a}</span><em>{c}</em></div>' for a,c in [("Space","3 bays"),("From","Tue 1 Dec"),("For","3 months"),("Goods","Cartons, dry")])}
<div class=bt2>Hold A6, C3, D4</div></div></div>''',
""".w2{flex:1;display:flex;gap:16px}
.gd2{flex:1;display:grid;grid-template-columns:repeat(6,1fr);grid-template-rows:repeat(4,1fr);gap:8px;background:#1a1e24;border-radius:24px;padding:14px}
.by{border-radius:10px;padding:8px;display:flex;flex-direction:column;justify-content:space-between;color:#1a1e24;opacity:.35}
.by b{font:800 19px Montserrat}.by span{font:700 11px 'Open Sans'}
.by.fr{border:3px dashed #5a636f;color:#aab1bb;opacity:1}.by.hl{background:#f2efe8;border:3px solid #5cc8c2;color:#22272e;opacity:1}
.bk2{width:330px;flex:none;padding:22px;display:flex;flex-direction:column;gap:10px}
.bk2>b{font:800 32px/1.25 Montserrat}
.r2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1.5px solid #3a414b}.r2 span{font:600 15px 'Open Sans';color:#8f98a4}.r2 em{font-style:normal;font:700 23px 'Open Sans'}
.bt2{background:#1d8a8a;color:#fff;border-radius:14px;text-align:center;font:700 20px 'Open Sans';padding:15px}
""")

grn = [("Client", "Client B · sample"), ("Vehicle", "XX 00 AB 1234"), ("Received", "Mon 23 Nov, 11:20 am"), ("Goods", "240 cartons · SKU B-12, B-14"), ("Bay", "B5 and C4"), ("Damage", "2 cartons, photo saved")]
P["p118_godown_s3"] = wh(3, """<div class=kt><b>2</b>INWARD</div><h1 style="margin-top:18px">Every truck in<br><span>gets a GRN with photos.</span></h1>""",
f'''<div class=w3><div class=dc3><div class=t3><div><span class=lb style="color:#7d8590">GOODS RECEIVED NOTE · SAMPLE</span><b>GRN-1187</b></div><em>Signed</em></div>
{"".join(f'<div class="r3 {"dm" if a=="Damage" else ""}"><span>{a}</span><b>{b}</b></div>' for a,b in grn)}
<div class=ph3>{"".join(f'<i style="background:{c}">{ic("camera",28,"#fff")}</i>' for c in ["#6d8fd6","#1d8a8a","#e3b873","#b55d8a"])}</div></div>
<div class=sd3>{"".join(f'<div class="cd s3"><b>{a}</b><span>{b}</span></div>' for a,b in [("Client gets a copy","On WhatsApp, the same minute."),("Damage on record","Before the goods are yours to answer for."),("Stock goes up","In the client's statement.")])}</div></div>''',
""".w3{flex:1;display:flex;gap:18px}
.dc3{flex:1.3;background:#f2efe8;color:#22272e;border-radius:22px;padding:22px 24px;display:flex;flex-direction:column;gap:4px;border-top:12px solid #1d8a8a}
.t3{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:8px}.t3 div{display:flex;flex-direction:column;gap:4px}.t3 b{font:800 32px/1.25 Montserrat}
.t3 em{font-style:normal;font:700 16px 'Open Sans';background:#1d8a8a;color:#fff;padding:6px 12px;border-radius:8px}
.r3{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1.5px dashed #d8d2c4}.r3 span{font:600 15px 'Open Sans';color:#7d8590}.r3 b{font:700 22px 'Open Sans'}
.r3.dm b{color:#b5452c}
.ph3{display:flex;gap:10px;padding-top:10px}.ph3 i{flex:1;height:80px;border-radius:12px;display:flex;align-items:center;justify-content:center}
.sd3{flex:1;display:flex;flex-direction:column;gap:14px}
.s3{flex:1;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px}.s3 b{font:800 25px/1.25 Montserrat;color:#e3b873}.s3 span{font:500 20px/1.4 'Open Sans';color:#cfd4da}
""")

pick = [("B4", "SKU B-09", "25 cartons"), ("B5", "SKU B-12", "40 cartons"), ("B5", "SKU B-14", "20 cartons"), ("C4", "SKU B-14", "15 cartons")]
P["p118_godown_s4"] = wh(4, """<div class=kt><b>3</b>OUTWARD</div><h1 style="margin-top:18px">The client asks online.<br><span>You get a picking list.</span></h1>""",
f'''<div class=w4><div class="cd rq4"><span class=lb>DISPATCH REQUEST · SAMPLE</span><b>Client B</b><span class=s>Deliver to Sample Retail, Pune<br>Pickup Tue 24 Nov, 10 am</span>
<div class=q4><em>100</em><span>cartons asked</span></div><div class=bt4>Request sent from client portal</div></div>
<div class=pl4><span class=lb style="color:#5c4a24">PICKING LIST · BY BAY</span>{"".join(f'<div class=p4><em>{a}</em><div><b>{b}</b><span>{c}</span></div><i></i></div>' for a,b,c in pick)}<div class=tt4>Total 100 cartons · bay order B4, B5, C4</div></div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.rq4{flex:1;padding:22px;display:flex;flex-direction:column;gap:10px}.rq4>b{font:800 34px/1.25 Montserrat}.rq4 .s{font:500 20px/1.45 'Open Sans';color:#cfd4da}
.q4{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;background:#22272e;border-radius:18px}
.q4 em{font-style:normal;font:800 96px/1.25 Montserrat;color:#5cc8c2}.q4 span{font:600 20px 'Open Sans';color:#aab1bb}
.bt4{background:#1d8a8a;color:#fff;border-radius:14px;text-align:center;font:700 18px 'Open Sans';padding:13px}
.pl4{flex:1.2;background:#e3b873;color:#22272e;border-radius:22px;padding:22px;display:flex;flex-direction:column;gap:10px}
.p4{flex:1;background:#f2efe8;border-radius:14px;display:flex;align-items:center;gap:16px;padding:0 16px}
.p4 em{font-style:normal;width:62px;height:52px;border-radius:10px;background:#22272e;color:#e3b873;font:800 22px/1 Montserrat;display:flex;align-items:center;justify-content:center;flex:none}
.p4 div{flex:1;display:flex;flex-direction:column;gap:2px}.p4 b{font:700 21px 'Open Sans'}.p4 span{font:500 18px 'Open Sans';color:#5d646e}
.p4 i{width:28px;height:28px;border-radius:7px;border:3px solid #22272e;flex:none}
.tt4{font:700 18px 'Open Sans';text-align:center;padding-top:4px}
""")

stmt = [("SKU B-09", "180", "0", "25", "155"), ("SKU B-12", "400", "120", "40", "480"), ("SKU B-14", "260", "120", "35", "345"), ("SKU B-20", "90", "0", "0", "90")]
P["p118_godown_s5"] = wh(5, """<div class=kt><b>4</b>STATEMENT</div><h1 style="margin-top:18px">Each client gets<br><span>a stock statement.</span></h1>""",
f'''<div class="cd tb5"><div class=t5><div><span class=lb>STOCK STATEMENT · SAMPLE</span><b>Client B · November</b></div><em>5 bays · A4 to C4</em></div>
<div class="r5 hd5"><span>Item</span><span>Opening</span><span>In</span><span>Out</span><span>Closing</span></div>
{"".join(f'<div class=r5><b>{a}</b><span>{b}</span><span class=in>{"+"+c if c!="0" else "—"}</span><span class=ot>{"−"+d if d!="0" else "—"}</span><em>{e}</em></div>' for a,b,c,d,e in stmt)}
<div class=ft5><span>Storage: 5 bays × 30 days</span><span>Sent on the 1st, on its own</span></div></div>''',
""".vis{flex-direction:column}
.tb5{flex:1;padding:22px 26px;display:flex;flex-direction:column}
.t5{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:12px}.t5 div{display:flex;flex-direction:column;gap:4px}.t5 b{font:800 32px/1.25 Montserrat}
.t5 em{font-style:normal;font:700 16px 'Open Sans';background:#22272e;padding:6px 12px;border-radius:8px}
.r5{flex:1;display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr 1fr;align-items:center;border-top:1.5px solid #3a414b;font:600 24px 'Open Sans'}
.r5.hd5{flex:none;padding-bottom:8px;border-top:none;font:700 15px 'Open Sans';color:#8f98a4;letter-spacing:1px}
.r5 b{font:700 23px 'Open Sans'}.r5 .in{color:#5cc8c2}.r5 .ot{color:#e39a7a}.r5 em{font-style:normal;font:800 26px Montserrat;color:#e3b873}
.ft5{display:flex;justify-content:space-between;background:#22272e;border-radius:14px;padding:14px 18px;font:600 18px 'Open Sans';color:#cfd4da;margin-top:8px}
""")

P["p118_godown_s6"] = wh(6, """<h1>Rent out a godown<br>or warehouse?<br><span>Let's build your<br>warehouse app.</span></h1>""",
f'''<div class=c6><div class=mn6>{plan()}</div><div class=ls6>{"".join(f'<div class=r6><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Live bay map","Space booking","Inward GRN with photos","Picking lists and statements"],1))}</div></div>''',
""".c6{flex:1;display:flex;flex-direction:column;gap:14px}
.mn6{flex:none;height:300px;display:grid;grid-template-columns:repeat(6,1fr);grid-template-rows:repeat(4,1fr);gap:8px;background:#1a1e24;border-radius:24px;padding:14px}
.by{border-radius:10px;padding:6px 8px;display:flex;flex-direction:column;justify-content:space-between;color:#1a1e24}.by b{font:800 17px Montserrat}.by span{display:none}
.by.fr{border:3px dashed #5a636f;color:#aab1bb}
.ls6{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.r6{background:#2d333c;border:1.5px solid #3a414b;border-radius:18px;display:flex;align-items:center;gap:14px;padding:0 20px}
.r6 em{width:50px;height:50px;border-radius:12px;background:#e3b873;color:#22272e;font:800 24px/1 Montserrat;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r6 b{font:800 25px/1.3 Montserrat}
""", cta="Warehouse owner? DM us", ctacss="background:#1d8a8a;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
