import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 102 INDIA · Textile wholesaler (Surat) · CAROUSEL 6 · Bitter + Open Sans · deep teal / rust orange / unbleached cotton
# New techniques: SVG stack of fabric rolls (than) with spiral ends, CSS fabric swatches (stripe/check/dot/leaf/ikat),
# credit-days aging columns with bill chips.
TX = """
body{--f:'Open Sans';--h:'Bitter';background:#f3ede0;color:#173b3d}
h1{font-family:'Bitter';font-weight:800;font-size:64px;letter-spacing:0;line-height:1.2} h1 span{color:#c4552d}
.sub{color:#5d6b66}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Open Sans';letter-spacing:3px;color:#c4552d}
.kt b{width:44px;height:44px;border-radius:50%;background:#173b3d;color:#f3ede0;font:800 22px/1 Bitter;display:flex;align-items:center;justify-content:center}
.cd{background:#fffdf8;border-radius:24px;box-shadow:0 14px 30px rgba(23,59,61,.08)}
.lb{font:700 13px 'Open Sans';letter-spacing:3px;color:#8b948f}
"""
def tx(n, head, vis, css="", cta="Swipe", ctacss="background:#173b3d;color:#f3ede0"):
    return page(TX + css, head, vis, "#173b3d", cta, ctacss, tagline=f"{n} / 6")
def roll(x, y, r, col, dark):
    return (f'<rect x="{x}" y="{y-r}" width="300" height="{2*r}" fill="{col}"/>'
            f'<rect x="{x}" y="{y-r}" width="300" height="{2*r}" fill="url(#sh)"/>'
            f'<ellipse cx="{x}" cy="{y}" rx="{r*0.42:.0f}" ry="{r}" fill="{dark}"/>'
            + "".join(f'<ellipse cx="{x}" cy="{y}" rx="{r*0.42*k:.0f}" ry="{r*k:.0f}" fill="none" stroke="{col}" stroke-width="2.5" opacity=".7"/>' for k in (0.8, 0.6, 0.4))
            + f'<ellipse cx="{x}" cy="{y}" rx="{r*0.1:.0f}" ry="{r*0.22:.0f}" fill="#3b2a1e"/>')
rolls_svg = ('<svg viewBox="50 66 535 364" width="{w}" height="{h}"><defs><linearGradient id="sh" x1="0" y1="0" x2="0" y2="1">'
             '<stop offset="0" stop-color="#fff" stop-opacity=".25"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".18"/></linearGradient></defs>'
             + roll(150, 360, 58, "#c4552d", "#9c3f1e") + roll(270, 360, 58, "#2f6f6a", "#1f4f4b")
             + roll(210, 248, 58, "#e0b54a", "#b48c2c") + roll(90, 248, 58, "#7d4f8a", "#5c3768")
             + roll(150, 136, 58, "#e8dfcb", "#c6bba2") + '</svg>')
P["p102_textile_s1"] = tx(1, """<h1>Brokers order on<br>photos and calls?<br><span>Catalogue, orders and<br>dispatch in one app.</span></h1>""",
f'''<div class=w1><div class=rl1>{rolls_svg.format(w=580,h=395)}</div>
<div class=sd1>{"".join(f'<div class="cd s1"><span class=lb>{a}</span><b>{b}</b><i>{c}</i></div>' for a,b,c in [("STEP 1","Catalogue","Every design with thans in stock"),("STEP 2","Broker orders","One list, no lost messages"),("STEP 3","Dispatch","Bale and LR details for each party"),("STEP 4","Credit days","Who is due, by days")])}</div></div>''',
""".w1{flex:1;display:flex;gap:18px}
.rl1{flex:1;background:#173b3d;border-radius:30px;display:flex;align-items:center;justify-content:center;padding:10px}
.rl1 svg{display:block}
.sd1{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.s1{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.s1 b{font:800 30px/1.25 Bitter}.s1 i{font:500 18px/1.35 'Open Sans';font-style:normal;color:#5d6b66}
""")

sw = {"stripe": "repeating-linear-gradient(90deg,#c4552d 0 14px,#f3ede0 14px 22px,#173b3d 22px 28px,#f3ede0 28px 36px)",
      "check": "repeating-linear-gradient(0deg,rgba(47,111,106,.75) 0 12px,transparent 12px 24px),repeating-linear-gradient(90deg,rgba(47,111,106,.75) 0 12px,#f6e9c8 12px 24px)",
      "dot": "radial-gradient(circle,#f3ede0 4px,transparent 5px) 0 0/22px 22px,#7d4f8a",
      "leaf": "radial-gradient(ellipse 9px 4px at 50% 50%,#2f6f6a 90%,transparent) 0 0/26px 18px,radial-gradient(circle,#c4552d 3px,transparent 4px) 13px 9px/26px 18px,#f6e9c8",
      "ikat": "repeating-linear-gradient(45deg,#173b3d 0 10px,#e0b54a 10px 14px,#173b3d 14px 24px,#c4552d 24px 28px)",
      "plain": "linear-gradient(135deg,#e0b54a,#c99a2e)"}
designs = [("D-401", "stripe", "Cotton stripe", "42 thans", ""), ("D-402", "check", "Yarn-dyed check", "18 thans", ""),
           ("D-405", "dot", "Rayon polka", "6 thans", "lo"), ("D-409", "leaf", "Printed leaf", "30 thans", ""),
           ("D-411", "ikat", "Ikat print", "0 · on order", "no"), ("D-415", "plain", "Plain dyed", "55 thans", "")]
P["p102_textile_s2"] = tx(2, """<div class=kt><b>1</b>CATALOGUE</div><h1 style="margin-top:18px">Every design with<br><span>live stock, one link.</span></h1>""",
f'''<div class=gd2>{"".join(f'<div class="cd t2 {k}"><div class=sw2 style="background:{sw[p]}"></div><div class=in2><div class=r2><b>{c}</b><em>{d}</em></div><span>{n}</span></div></div>' for c,p,n,d,k in designs)}</div>
<div class=nt2>Brokers open the link and see what is in stock today. No more “send photos again”.</div>''',
""".vis{flex-direction:column;gap:14px}
.gd2{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px}
.t2{display:flex;flex-direction:column;overflow:hidden}
.sw2{flex:1;min-height:0}
.in2{flex:none;padding:12px 16px 14px;display:flex;flex-direction:column;gap:4px}
.r2{display:flex;justify-content:space-between;align-items:center;gap:8px}.r2 b{font:800 26px/1.25 Bitter}
.r2 em{font-style:normal;font:700 15px 'Open Sans';background:#e3efe9;color:#1f5b4a;padding:4px 9px;border-radius:8px;white-space:nowrap}
.lo .r2 em{background:#fbe6c9;color:#8a5a12}.no .r2 em{background:#f6d9cf;color:#a53e1c}
.in2 span{font:500 18px 'Open Sans';color:#5d6b66}
.nt2{flex:none;background:#173b3d;color:#f3ede0;border-radius:18px;padding:16px 22px;font:600 21px/1.4 'Open Sans'}
""")

orders = [("Broker A · Sample", "Party: Sample Traders, Jaipur", "D-401 × 10 · D-409 × 6", "New", "nw"),
          ("Broker B · Sample", "Party: Sample Fabrics, Pune", "D-402 × 8", "Confirmed", "cf"),
          ("Broker A · Sample", "Party: Sample Store, Indore", "D-415 × 12 · D-401 × 4", "Packing", "pk"),
          ("Broker C · Sample", "Party: Sample Mart, Kolkata", "D-405 × 6", "Confirmed", "cf")]
P["p102_textile_s3"] = tx(3, """<div class=kt><b>2</b>BROKER ORDERS</div><h1 style="margin-top:18px">Every broker order<br><span>in one list.</span></h1>""",
f'''<div class="cd ls3"><div class=h3r><span class=lb>TODAY · SAMPLE</span><span class=lb>4 ORDERS</span></div>
{"".join(f'<div class=o3><div class=a3><b>{a}</b><span>{b}</span></div><div class=d3>{c}</div><em class={k}>{d}</em></div>' for a,b,c,d,k in orders)}</div>
<div class=bt3>{"".join(f'<div class="cd b3"><b>{a}</b><span>{b}</span></div>' for a,b in [("Stock is held","when an order is confirmed"),("Brokers see status","without calling you")])}</div>''',
""".vis{flex-direction:column;gap:14px}
.ls3{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.h3r{display:flex;justify-content:space-between;padding-bottom:8px}
.o3{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px solid #ece5d5}
.a3{flex:1;display:flex;flex-direction:column;gap:4px}.a3 b{font:800 28px/1.25 Bitter}.a3 span{font:500 20px 'Open Sans';color:#5d6b66}
.d3{width:290px;font:600 20px/1.35 'Open Sans';background:#f3ede0;border-radius:10px;padding:8px 12px}
.o3 em{width:130px;text-align:center;font-style:normal;font:700 16px 'Open Sans';padding:8px 0;border-radius:10px}
.nw{background:#c4552d;color:#fff}.cf{background:#e3efe9;color:#1f5b4a}.pk{background:#fbe6c9;color:#8a5a12}
.bt3{flex:none;display:flex;gap:14px}.b3{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:2px;background:#173b3d;color:#f3ede0}
.b3 b{font:800 26px/1.25 Bitter;color:#e0b54a}.b3 span{font:500 18px 'Open Sans';color:#c9d6d2}
""")

steps = [("Packed", "6 thans checked", 1), ("Bale made", "Bale 2 of 2", 1), ("Given to transport", "Sample Transport", 1), ("LR sent to party", "On WhatsApp", 0)]
P["p102_textile_s4"] = tx(4, """<div class=kt><b>3</b>DISPATCH</div><h1 style="margin-top:18px">“Has my parcel left?”<br><span>Send the LR in one tap.</span></h1>""",
f'''<div class=w4><div class="cd dc4"><div class=t4><b>Dispatch slip</b><span class=lb>SAMPLE</span></div>
{"".join(f'<div class=r4><span>{a}</span><b>{b}</b></div>' for a,b in [("Party","Sample Fabrics, Pune"),("Order","Broker B · D-402 × 8"),("Bales","2 bales · 8 thans"),("Transport","Sample Transport"),("LR no.","LR-00 0000 · sample"),("Sent","Mon 23 Nov")])}
<div class=bc4>{"".join(f'<i style="width:{3 if i%3 else 6}px"></i>' for i in range(34))}</div></div>
<div class=st4>{"".join(f'<div class="s4 {"dn" if d else ""}"><em>{"✓" if d else i+1}</em><div><b>{a}</b><span>{b}</span></div></div>' for i,(a,b,d) in enumerate(steps))}</div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.dc4{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:6px;border-top:12px solid #c4552d;background-image:radial-gradient(circle at 0 50%,#f3ede0 10px,transparent 11px),radial-gradient(circle at 100% 50%,#f3ede0 10px,transparent 11px)}
.t4{display:flex;justify-content:space-between;align-items:center;padding-bottom:6px}.t4 b{font:800 32px/1.25 Bitter}
.r4{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1.5px dashed #ddd3bf}
.r4 span{font:600 15px 'Open Sans';color:#8b948f;letter-spacing:1px}.r4 b{font:700 22px 'Open Sans'}
.bc4{flex:none;height:54px;display:flex;gap:4px;align-items:stretch;padding-top:8px}.bc4 i{display:block;background:#173b3d}
.st4{width:360px;flex:none;display:flex;flex-direction:column;gap:12px}
.s4{flex:1;background:#fffdf8;border-radius:20px;padding:14px 18px;display:flex;align-items:center;gap:14px;border:2px solid #e5dccb}
.s4 em{width:46px;height:46px;border-radius:50%;flex:none;background:#f3ede0;font:800 22px/1 Bitter;font-style:normal;display:flex;align-items:center;justify-content:center}
.s4.dn{background:#173b3d;color:#f3ede0;border-color:#173b3d}.s4.dn em{background:#e0b54a;color:#173b3d}
.s4 div{display:flex;flex-direction:column;gap:2px}.s4 b{font:800 24px/1.25 Bitter}.s4 span{font:500 17px 'Open Sans';opacity:.75}
""")

cols = [("0 to 30 days", "ok", [("Sample Fabrics", "Bill 1182"), ("Sample Mart", "Bill 1190"), ("Sample Store", "Bill 1201"), ("Sample Traders", "Bill 1205")]),
        ("31 to 60 days", "md", [("Sample Traders", "Bill 1120"), ("Sample Silk House", "Bill 1131")]),
        ("Over 60 days", "hi", [("Sample Textiles", "Bill 1044")])]
P["p102_textile_s5"] = tx(5, """<div class=kt><b>4</b>CREDIT DAYS</div><h1 style="margin-top:18px">Who is due, and<br><span>for how many days?</span></h1>""",
f'''<div class=ag5>{"".join(f'<div class="cd c5 {k}"><div class=h5><b>{t}</b><em>{len(bs)} bill{"s" if len(bs)>1 else ""}</em></div><div class=g5>' + "".join(f'<div class=bl5><b>{a}</b><span>{b} · broker A</span></div>' for a,b in bs) + ('<div class=rm5>Reminder sent Fri · reply pending</div>' if k=="hi" else '') + '</div></div>' for t,k,bs in cols)}</div>
<div class=nt5>Bills move to the next row on their own. Send a polite reminder from the same screen.</div>''',
""".vis{flex-direction:column;gap:14px}
.ag5{flex:1;display:flex;flex-direction:column;gap:14px}
.c5{padding:16px;display:flex;gap:16px;border-left:14px solid #2f6f6a}
.c5.ok{flex:2}.c5.md,.c5.hi{flex:1}
.c5.md{border-left-color:#e0b54a}.c5.hi{border-left-color:#c4552d}
.h5{width:200px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:8px;padding-left:4px}.h5 b{font:800 30px/1.25 Bitter}
.h5 em{align-self:flex-start;font-style:normal;font:700 16px 'Open Sans';background:#f3ede0;border-radius:8px;padding:4px 10px}
.g5{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:10px}
.bl5{background:#f3ede0;border-radius:14px;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:3px}
.hi .bl5{background:#f8e3da}
.bl5 b{font:700 23px 'Open Sans'}.bl5 span{font:500 18px 'Open Sans';color:#5d6b66}
.rm5{background:#c4552d;color:#fff;border-radius:14px;padding:12px 16px;font:700 20px/1.35 'Open Sans';display:flex;align-items:center}
.nt5{flex:none;background:#173b3d;color:#f3ede0;border-radius:18px;padding:16px 22px;font:600 21px/1.4 'Open Sans'}
""")

P["p102_textile_s6"] = tx(6, """<h1>Textile wholesaler?<br><span>Let's build your<br>order app.</span></h1><div class=sub>For Surat and every textile market: catalogue, broker orders, dispatch and credit days.</div>""",
f'''<div class=c6><div class=rl6>{rolls_svg.format(w=380,h=259)}</div><div class=ls6>{"".join(f'<div class=r6><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Catalogue with live stock","Broker orders in one list","Dispatch slip and LR","Credit days board"],1))}</div></div>''',
""".c6{flex:1;background:#173b3d;color:#f3ede0;border-radius:30px;padding:24px;display:flex;gap:22px;align-items:stretch}
.rl6{width:400px;flex:none;background:#21494b;border-radius:22px;display:flex;align-items:center;justify-content:center}.rl6 svg{display:block}
.ls6{flex:1;display:flex;flex-direction:column}
.r6{flex:1;display:flex;align-items:center;gap:16px;border-top:2px solid rgba(243,237,224,.15)}.r6:first-child{border-top:none}
.r6 em{width:50px;height:50px;border-radius:50%;background:#e0b54a;color:#173b3d;font:800 24px/1 Bitter;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r6 b{font:800 28px/1.25 Bitter}
""", cta="Textile trader? DM us", ctacss="background:#c4552d;color:#fff")

# ───────── 104 INDIA · Four-wheeler garage · CAROUSEL 5 · Archivo Black + Inter · workshop blue / signal yellow / concrete grey
# New technique: top-down SVG car inspection diagram with numbered damage/check points; fuel gauge + photo strip job card.
car = '''<svg viewBox="0 0 300 560" width="{w}" height="{h}">
<rect x="40" y="20" width="220" height="520" rx="90" fill="#e8ebef" stroke="#1f3b73" stroke-width="5"/>
<path d="M70 150 Q150 110 230 150 L215 215 Q150 195 85 215 Z" fill="#9fb8d9" stroke="#1f3b73" stroke-width="4"/>
<path d="M85 395 Q150 410 215 395 L228 450 Q150 480 72 450 Z" fill="#9fb8d9" stroke="#1f3b73" stroke-width="4"/>
<rect x="85" y="222" width="130" height="165" rx="20" fill="#d3d9e1" stroke="#1f3b73" stroke-width="4"/>
<g fill="#2a2f38"><rect x="22" y="110" width="26" height="70" rx="8"/><rect x="252" y="110" width="26" height="70" rx="8"/><rect x="22" y="390" width="26" height="70" rx="8"/><rect x="252" y="390" width="26" height="70" rx="8"/></g>
<rect x="80" y="28" width="40" height="14" rx="6" fill="#ffd23f"/><rect x="180" y="28" width="40" height="14" rx="6" fill="#ffd23f"/>
<rect x="78" y="520" width="40" height="12" rx="5" fill="#e2483d"/><rect x="182" y="520" width="40" height="12" rx="5" fill="#e2483d"/>
{pins}</svg>'''
pts = [(1, 230, 46), (2, 265, 140), (3, 150, 170), (4, 35, 425)]
pins = "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="#e2483d" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Archivo Black" font-size="22" fill="#fff">{n}</text>' for n, x, y in pts)
car = car.replace("{pins}", pins)
GR = """
body{--f:'Inter';--h:'Archivo Black';background:#d9dde2;color:#14213d}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.22} h1 span{color:#1f3b73;background:#ffd23f;padding:0 10px;border-radius:8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sub{color:#4d596b}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:800 16px Inter;letter-spacing:3px;color:#1f3b73}
.kt b{width:44px;height:44px;border-radius:10px;background:#1f3b73;color:#ffd23f;font:400 22px/1 'Archivo Black';display:flex;align-items:center;justify-content:center}
.cd{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(20,33,61,.08)}
.lb{font:700 13px Inter;letter-spacing:3px;color:#7d8899}
"""
def gr(n, head, vis, css="", cta="Swipe", ctacss="background:#1f3b73;color:#ffd23f"):
    return page(GR + css, head, vis, "#14213d", cta, ctacss, tagline=f"{n} / 5")
notes = [(1, "Front bumper", "Scratch, photo taken"), (2, "Front right tyre", "Worn on one side"), (3, "Windscreen", "Small chip"), (4, "Rear left door", "Dent from before")]
P["p104_garage_s1"] = gr(1, """<h1>“Why is the bill<br>so high?”<br><span>Show photos and get a</span><br><span>yes before the work.</span></h1>""",
f'''<div class=w1><div class=cr1>{car.format(w=290,h=541)}</div><div class=nl1><span class=lb>CHECK-IN NOTES · SAMPLE</span>
{"".join(f'<div class="cd n1"><em>{n}</em><div><b>{a}</b><span>{b}</span></div></div>' for n,a,b in notes)}</div></div>''',
""".w1{flex:1;display:flex;gap:20px}
.cr1{width:400px;flex:none;background:#1f3b73;border-radius:30px;display:flex;align-items:center;justify-content:center;background-image:repeating-linear-gradient(90deg,transparent 0 96px,rgba(255,210,63,.35) 96px 100px)}
.cr1 svg{display:block}
.nl1{flex:1;display:flex;flex-direction:column;gap:12px}
.n1{flex:1;display:flex;align-items:center;gap:16px;padding:16px 20px}
.n1 em{width:48px;height:48px;border-radius:50%;background:#e2483d;color:#fff;font:400 22px/1 'Archivo Black';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.n1 div{display:flex;flex-direction:column;gap:3px}.n1 b{font:800 25px Inter}.n1 span{font:500 19px Inter;color:#5a6677}
""")

P["p104_garage_s2"] = gr(2, """<div class=kt><b>1</b>JOB CARD</div><h1 style="margin-top:18px">Every car gets<br><span>a job card at the gate.</span></h1>""",
browser(f'''<div class=jc2><div class=t2><div><span class=lb>JOB CARD · SAMPLE</span><b>JC-2231 · Hatchback</b></div><em>In bay 3</em></div>
<div class=g2>{"".join(f'<div class=f2><span>{a}</span><b>{b}</b></div>' for a,b in [("Car no.","XX 00 AB 1234"),("Owner","Sample customer"),("Reading","48,210 km"),("Promised","Mon 23 Nov, 6 pm")])}</div>
<div class=fu2><span>Fuel at check-in</span><div class=gg2>{"".join(f'<i class="{"on" if i<3 else ""}"></i>' for i in range(8))}</div><b>3 / 8</b></div>
<div class=cw2><div class=cp2><span>What the customer said</span><ul>{"".join(f'<li>{c}</li>' for c in ["Noise when braking","AC not cooling well","General service"])}</ul></div>
<div class="cp2 fd2"><span>What we found</span><ul>{"".join(f'<li>{c}</li>' for c in ["Brake pads worn","AC gas low","Wiper blades worn","Bumper scratch"])}</ul></div></div>
<div class=ph2><span>Photos</span><div>{"".join(f'<i style="background:{c}">{ic("camera",30,"#fff")}{t}</i>' for c,t in zip( ["linear-gradient(135deg,#9fb8d9,#1f3b73)","linear-gradient(135deg,#d3d9e1,#7d8899)","linear-gradient(135deg,#ffd23f,#d79b10)","linear-gradient(135deg,#e8ebef,#9aa3b0)","linear-gradient(135deg,#2a2f38,#5a6677)"],["Front","Right","Dashboard","Rear","Left"]))}</div></div></div>''', "garage.yourgarage.in · sample", "flex:1"),
""".vis{flex-direction:column}
.jc2{flex:1;padding:20px 26px;display:flex;flex-direction:column;gap:14px}
.t2{display:flex;justify-content:space-between;align-items:center}.t2 div{display:flex;flex-direction:column;gap:4px}.t2 b{font:400 32px/1.25 'Archivo Black'}
.t2 em{font-style:normal;font:800 18px Inter;background:#ffd23f;padding:10px 16px;border-radius:12px}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.f2{border:2px solid #e3e7ec;border-radius:14px;padding:10px 16px;display:flex;flex-direction:column;gap:2px}.f2 span{font:600 15px Inter;color:#7d8899}.f2 b{font:700 23px Inter}
.fu2{display:flex;align-items:center;gap:14px;font:600 18px Inter;color:#5a6677}.fu2 b{color:#14213d;font:800 20px Inter}
.gg2{flex:1;display:flex;gap:6px}.gg2 i{flex:1;height:22px;border-radius:5px;background:#e3e7ec;display:block}.gg2 i.on{background:#1f3b73}
.cw2{flex:1;display:flex;gap:12px;min-height:0}.fd2{background:#fff8d6!important}.fd2 li:before{background:#1f3b73!important}
.cp2{flex:1;background:#f2f4f7;border-radius:14px;padding:14px 18px;display:flex;flex-direction:column;gap:8px}
.cp2 span,.ph2 span{font:600 16px Inter;color:#7d8899}
.cp2 ul{list-style:none;display:flex;flex-direction:column;flex:1;justify-content:space-evenly}.cp2 li{font-size:23px!important}.cp2 li{font:700 23px Inter;padding-left:24px;position:relative}
.cp2 li:before{content:"";position:absolute;left:0;top:9px;width:12px;height:12px;border-radius:3px;background:#e2483d}
.ph2{flex:none;display:flex;flex-direction:column;gap:8px}.ph2 div{display:flex;gap:10px}.ph2 i{flex:1;height:130px;border-radius:12px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;color:#fff;font:700 16px Inter;font-style:normal}
""")

items = [("Brake pads, front", "Needed now", "Worn out · photo attached", "need"), ("AC gas top-up", "Needed now", "Low cooling · checked", "need"),
         ("Wiper blades", "Can wait", "Change at next service", "wait")]
P["p104_garage_s3"] = gr(3, """<div class=kt><b>2</b>APPROVAL</div><h1 style="margin-top:18px">Send the list.<br><span>The customer taps yes.</span></h1>""",
f'''<div class=w3>{phone(f"""<div class=ch3><div class=hd3>Your Garage · sample</div>
<div class=bb3>Your car JC-2231 is checked. Please approve the work:</div>
{"".join(f'<div class="it3 {k}"><div><b>{a}</b><span>{c}</span></div><em>{b}</em></div>' for a,b,c,k in items)}
<div class=bn3><i class=y>Approve all</i><i>Call me</i></div></div>""", w=380, h=760)}
<div class=sd3>{"".join(f'<div class="cd s3"><b>{t}</b><span>{d}</span></div>' for t,d in [("Photo with each item","So the customer sees why."),("“Can wait” items saved","They come back as a reminder."),("Yes is on record","No arguments at the counter.")])}</div></div>''',
""".w3{flex:1;display:flex;gap:22px;align-items:center}
.ch3{flex:1;padding:12px 16px 16px;display:flex;flex-direction:column;gap:10px;background:#f2f4f7}
.hd3{font:700 15px Inter;color:#7d8899;text-align:center}
.bb3{background:#fff;border-radius:16px 16px 16px 4px;padding:12px 14px;font:500 18px/1.4 Inter}
.it3{flex:1;background:#fff;border-radius:14px;padding:10px 14px;display:flex;align-items:center;gap:10px;border-left:6px solid #e2483d}
.it3 div{flex:1;display:flex;flex-direction:column;gap:3px}.it3 b{font:700 18px Inter}.it3 span{font:500 14px Inter;color:#7d8899}
.it3 em{font-style:normal;font:700 13px Inter;background:#fde4e2;color:#b2281f;padding:5px 8px;border-radius:8px;white-space:nowrap}
.it3.wait{border-left-color:#9aa3b0}.it3.wait em{background:#eef0f3;color:#5a6677}
.bn3{display:flex;gap:8px}.bn3 i{flex:1;font-style:normal;text-align:center;font:700 17px Inter;padding:12px 0;border-radius:12px;background:#fff;border:2px solid #d3d9e1}.bn3 i.y{background:#1f3b73;color:#ffd23f;border-color:#1f3b73}
.sd3{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.s3{flex:1;padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:10px solid #ffd23f}
.s3 b{font:400 30px/1.3 'Archivo Black'}.s3 span{font:500 22px/1.4 Inter;color:#5a6677}
""")

rem = [("XX 00 AB 1234", "Wiper blades", "Saved as “can wait”", "Next visit"), ("XX 00 CD 5678", "General service", "Every 10,000 km", "Due this week"),
       ("XX 00 EF 9012", "Insurance renewal", "Renewal date saved", "Due in 12 days"), ("XX 00 GH 3456", "Wheel alignment", "Every 5,000 km", "Due next week")]
P["p104_garage_s4"] = gr(4, """<div class=kt><b>3</b>REMINDERS</div><h1 style="margin-top:18px">Bring them back<br><span>before the next problem.</span></h1>""",
f'''<div class="cd ls4"><span class=lb>REMINDERS · SAMPLE</span>
{"".join(f'<div class=r4><div class=np4>{a}</div><div class=d4><b>{b}</b><span>{c}</span></div><em>{d}</em></div>' for a,b,c,d in rem)}</div>
<div class=tx4><span class=lb style="color:#9fb0cc">TEXT GOES OUT ON ITS OWN · SAMPLE</span><p>Your car XX 00 CD 5678 is due for a general service this week. Reply 1 to book a slot.</p></div>''',
""".vis{flex-direction:column;gap:14px}
.ls4{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.r4{flex:1;display:flex;align-items:center;gap:18px;border-top:1.5px solid #e9edf2}.ls4 .lb{padding-bottom:8px}
.np4{width:210px;flex:none;border:3px solid #14213d;border-radius:8px;font:800 21px Inter;text-align:center;padding:8px 0;background:#fff;letter-spacing:1px}
.d4{flex:1;display:flex;flex-direction:column;gap:3px}.d4 b{font:800 24px Inter}.d4 span{font:500 18px Inter;color:#5a6677}
.r4 em{font-style:normal;font:700 17px Inter;background:#ffd23f;padding:8px 12px;border-radius:10px;white-space:nowrap}
.tx4{flex:none;background:#1f3b73;color:#fff;border-radius:20px;padding:16px 22px;display:flex;flex-direction:column;gap:6px}.tx4 p{font:500 21px/1.45 Inter}
""")

P["p104_garage_s5"] = gr(5, """<h1>Run a car garage?<br><span>Let's build your</span><br><span>garage app.</span></h1><div class=sub>Job cards, photo approvals and service reminders for four-wheeler garages.</div>""",
f'''<div class=c5><div class=cr5>{car.format(w=250,h=467)}</div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Job card at the gate","Photos and a yes before work","Reminders that bring cars back","Bills and history per car"],1))}</div></div>''',
""".c5{flex:1;background:#ffd23f;border-radius:30px;padding:24px;display:flex;gap:24px}
.cr5{width:300px;flex:none;background:#1f3b73;border-radius:22px;display:flex;align-items:center;justify-content:center}.cr5 svg{display:block}
.ls5{flex:1;display:flex;flex-direction:column}
.r5{flex:1;display:flex;align-items:center;gap:16px;border-top:2.5px solid rgba(20,33,61,.15)}.r5:first-child{border-top:none}
.r5 em{width:52px;height:52px;border-radius:12px;background:#1f3b73;color:#ffd23f;font:400 24px/1 'Archivo Black';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:800 28px/1.3 Inter}
""", cta="Garage owner? DM us", ctacss="background:#1f3b73;color:#ffd23f")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
