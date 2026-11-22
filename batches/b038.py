import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 206 CANADA · Firewood delivery · SINGLE · Lora + Fira Sans · forest green / birch cream / rust
# New technique: woodpile of log ends (growth rings) where each coloured section is one order + delivery-day strip by area.
random.seed(206)
def logend(x, y, r, c, sc="#5b3a1f"):
    rings = "".join(f'<circle cx="{x}" cy="{y}" r="{r*k:.1f}" fill="none" stroke="#8a5a32" stroke-width="1.6" opacity=".55"/>' for k in (0.25, 0.5, 0.75))
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{c}" stroke="{sc}" stroke-width="6"/>{rings}'
pile = ""
cols = {0: "#e8c48d", 1: "#d9a86a", 2: "#f1d9ac"}
for row in range(5):
    for i in range(10 - (row % 2)):
        x = 50 + i * 76 + (38 if row % 2 else 0); y = 330 - row * 66
        grp = 0 if i < 4 else (1 if i < 7 else 2)
        pile += logend(x, y, 34 + random.uniform(-3, 3), cols[grp], ["#2f5d3a","#b0532a","#7a8a5a"][grp])
orders = [("Full cord", "Sample home, North side", "Tue", "#2f5d3a"), ("Face cord ×2", "Sample cabin, Lakeview", "Wed", "#b0532a"), ("Half cord + stacking", "Sample home, East end", "Wed", "#7a8a5a")]
P["p206_firewood"] = page("""
body{--f:'Fira Sans';--h:'Lora';background:#f4eee2;color:#1f3324}
.kk{font:600 16px 'Fira Sans';letter-spacing:3px;color:#b0532a;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#2f5d3a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pl{background:#1f3324;border-radius:28px;padding:20px 22px 16px;display:flex;flex-direction:column;gap:12px}
.pl svg{width:100%;height:auto;display:block}
.og{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.og div{border-radius:16px;padding:12px 14px;color:#fff;display:flex;flex-direction:column;gap:2px}
.og b{font:700 22px/1.3 Lora}.og span{font:400 16px/1.35 'Fira Sans';opacity:.9}.og em{font-style:normal;font:600 15px 'Fira Sans';margin-top:4px;opacity:.95}
.dd{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:10px;min-height:0}
.dd div{background:#fffaf0;border-radius:20px;padding:16px 14px;display:flex;flex-direction:column;gap:6px;box-shadow:0 10px 22px rgba(31,51,36,.07)}
.dd small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#8a7a62}.dd b{font:700 26px/1.25 Lora}.dd span{font:500 17px/1.35 'Fira Sans';color:#4f5d52}
.dd .on{background:#2f5d3a;color:#fff}.dd .on small,.dd .on span{color:#cfe0d2}
.fm{display:flex;align-items:center;gap:14px;background:#b0532a;color:#fff;border-radius:20px;padding:16px 20px;font:500 20px/1.4 'Fira Sans'}.fm .ib{width:50px;height:50px;border-radius:14px;background:rgba(255,255,255,.18)}
""", "<div class=kk>FIREWOOD DELIVERY · WINTER ORDERS</div><h1>Firewood orders by<br>voicemail and text?<br><span>Take them online.</span></h1>",
f'''<div class=vw><div class=pl><svg viewBox="0 0 800 370">{pile}</svg>
<div class=og>{"".join(f'<div style="background:{c}"><b>{a}</b><span>{b}</span><em>Delivery {d}</em></div>' for a,b,d,c in orders)}</div></div>
<div class=dd>{"".join(f'<div class="{"on" if d in ("Tue","Wed") else ""}"><small>{d.upper()}</small><b>{a}</b><span>{n}</span></div>' for d,a,n in [("Mon","West end","2 orders"),("Tue","North side","1 order"),("Wed","Lakeview, East end","2 orders"),("Thu","South hill","Open"),("Fri","Downtown","Open")])}</div>
<div class=fm><span class=ib>{ic("globe",28)}</span><span>Customers pick cord size, wood and stacking, and see the next delivery day.</span></div></div>''',
"#1f3324", "Sell firewood? DM us", "background:#2f5d3a;color:#fff")

# ───────── 207 INDIA · Corporate uniform maker · CAROUSEL 5 · Poppins + Roboto · steel blue / khaki / charcoal
# New techniques: shirt SVG with size tag, stacked size bars per department with derived totals, carton cards with packed progress.
UB = """
body{--f:'Roboto';--h:'Poppins';background:#eef1f3;color:#23272b}
h1{font-family:'Poppins';font-weight:800;font-size:64px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#2d4f6b}
.kk{font:600 16px 'Poppins';letter-spacing:3px;color:#9a7f45;margin-top:22px;line-height:1.4}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(35,39,43,.07)}
.uS{background:#c8b48a}.uM{background:#8fa9bf}.uL{background:#2d4f6b}.uXL{background:#23272b}.uXXL{background:#9a7f45}
"""
def ub(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#23272b;color:#fff"):
    return page(UB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#23272b", cta, ctacss, tagline=f"{n} / 5")
shirt = '''<svg viewBox="0 0 400 420" class=sh><path d="M130 40 L80 60 L20 130 L70 175 L100 150 L100 400 L300 400 L300 150 L330 175 L380 130 L320 60 L270 40 Q200 90 130 40 Z" fill="#8fa9bf" stroke="#23272b" stroke-width="6" stroke-linejoin="round"/>
<path d="M130 40 Q200 90 270 40 L250 30 Q200 64 150 30 Z" fill="#2d4f6b"/><line x1="200" y1="78" x2="200" y2="400" stroke="#23272b" stroke-width="4"/>
''' + "".join(f'<circle cx="214" cy="{y}" r="6" fill="#23272b"/>' for y in (120, 180, 240, 300, 360)) + '''<rect x="232" y="180" width="50" height="42" rx="4" fill="none" stroke="#23272b" stroke-width="4"/></svg>'''
P["p207_uniform_s1"] = ub(1, "UNIFORM MAKERS · BULK ORDERS", "120 staff sizes<br>collected on calls?<br><span>Send one size link.</span>",
f'''<div class=w1><div class="cd sp">{shirt}<div class=tg>Size?</div><small>SAMPLE COMPANY · 120 STAFF</small></div>
<div class=ns>{"".join(f'<div><small>{a}</small><b>{b}</b><em>{c}</em></div>' for a,b,c in [("STAFF 14 · ON CALL","“L, I think.”","Not sure"),("STAFF 32 · VOICE NOTE","“Same as last year.”","Which size?"),("STAFF 57 · KITCHEN","No reply yet","Missing"),("HR · SAMPLE COMPANY","“Can you start stitching?”","Sizes not ready")])}</div></div>''',
css=""".w1{flex:1;display:flex;gap:18px}.sp{width:380px;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px;position:relative}
.sh{width:300px;height:auto}.tg{position:absolute;top:150px;right:40px;background:#9a7f45;color:#fff;font:800 28px/1.3 Poppins;border-radius:14px;padding:8px 16px;transform:rotate(8deg)}
.sp small{font:600 15px/1.4 Roboto;letter-spacing:2px;color:#6b7680}
.ns{flex:1;display:flex;flex-direction:column;gap:12px}.ns div{flex:1;background:#fff;border-radius:20px;padding:14px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px;border-left:8px solid #2d4f6b;box-shadow:0 10px 22px rgba(35,39,43,.06)}
.ns small{font:600 14px/1.4 Roboto;letter-spacing:2px;color:#6b7680}.ns b{font:700 27px/1.3 Poppins}.ns em{font-style:normal;align-self:flex-start;font:600 16px Roboto;background:#f3ecdc;color:#7a6230;border-radius:10px;padding:4px 10px}""")

P["p207_uniform_s2"] = ub(2, "PART 1 · SIZE LINK", "Each staff member<br><span>fills their own size.</span>",
f'''<div class=w2>{browser(f"""<div class=fm><div class=fh><b>Uniform sizes · Sample Company</b><span>SAMPLE</span></div>
<div class=fr><label>Name</label><div class=in>Staff 14</div></div><div class=fr><label>Department</label><div class=in>Front office</div></div>
<div class=fr><label>Shirt size</label><div class=ch>{"".join(f'<span class="{"on" if s=="L" else ""}">{s}</span>' for s in ["S","M","L","XL","XXL"])}</div></div>
<div class=fr><label>Trouser waist</label><div class=ch>{"".join(f'<span class="{"on" if s=="32" else ""}">{s}</span>' for s in ["28","30","32","34","36","38"])}</div></div>
<div class=fr><label>Fit</label><div class=ch><span class=on>Regular</span><span>Slim</span></div></div>
<div class=fr><label>Mobile</label><div class=in>98XXX XXX14</div></div><div class=fr><label>Note to tailor</label><div class="in nt">Sleeves a little longer, please.</div></div>
<div class=bt>Submit my size</div></div>""", url="yourshop.com/sizes/sample-company", style="flex:1")}
<div class=pr><div><b>96 of 120</b><span>sizes filled</span></div><div class=bar><i style="width:80%"></i></div><em>{ic("bell",22)}Reminder sent to 24 staff</em></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px}.fm{flex:1;padding:22px 28px;display:flex;flex-direction:column;gap:16px}
.fh{display:flex;justify-content:space-between;align-items:center}.fh b{font:700 30px/1.3 Poppins}.fh span{font:600 14px Roboto;letter-spacing:2px;color:#6b7680}
.fr{display:flex;align-items:center;gap:18px}.fr label{width:190px;flex:none;font:500 21px Roboto;color:#4b5660}
.in{flex:1;border:2px solid #dde3e8;border-radius:14px;padding:12px 16px;font:500 22px Roboto}.in.nt{color:#4b5660;font-style:italic}
.ch{flex:1;display:flex;gap:8px}.ch span{flex:1;text-align:center;border:2px solid #dde3e8;border-radius:12px;padding:11px 0;font:600 20px Roboto}.ch .on{background:#2d4f6b;border-color:#2d4f6b;color:#fff}
.bt{margin-top:auto;background:#23272b;color:#fff;border-radius:14px;padding:16px;text-align:center;font:600 22px Poppins}
.pr{display:flex;align-items:center;gap:18px;background:#23272b;color:#fff;border-radius:20px;padding:16px 22px}.pr b{display:block;font:800 32px/1.4 Poppins;color:#c8b48a;margin-bottom:2px}.pr span{font:400 17px Roboto;color:#c3cbd2}
.bar{flex:1;height:14px;border-radius:7px;background:#3c434a;overflow:hidden}.bar i{display:block;height:100%;background:#c8b48a}
.pr em{font-style:normal;display:flex;gap:8px;align-items:center;font:500 18px Roboto}""")

depts = [("Front office", [4, 10, 10, 4, 2]), ("Kitchen", [5, 12, 14, 6, 3]), ("Housekeeping", [4, 12, 11, 5, 2]), ("Security", [1, 4, 5, 5, 1])]
sz = ["S", "M", "L", "XL", "XXL"]
tot = [sum(d[1][i] for d in depts) for i in range(5)]
def sbar(v):
    return "".join(f'<i class=u{s} style="flex:{n}">{n if n>=3 else ""}</i>' for s, n in zip(sz, v))
P["p207_uniform_s3"] = ub(3, "PART 2 · SIZE TOTALS", "All 120 sizes in.<br><span>Cut list ready by size.</span>",
f'''<div class=w3><div class="cd sb"><div class=lgd>{"".join(f'<span><i class=u{s}></i>{s}</span>' for s in sz)}</div>
{"".join(f'<div class=br><p><b>{n}</b><span>{sum(v)} staff</span></p><div class=bb style="width:{sum(v)/40*100:.1f}%">{sbar(v)}</div></div>' for n,v in depts)}</div>
<div class=tt>{"".join(f'<div class=u{s}><small>{s}</small><b>{t}</b><span>shirts</span></div>' for s,t in zip(sz,tot))}</div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px}.sb{flex:1;padding:18px 24px;display:flex;flex-direction:column;gap:6px}
.lgd{display:flex;gap:18px;font:600 17px Roboto;padding-bottom:6px}.lgd span{display:flex;gap:7px;align-items:center}.lgd i{width:18px;height:18px;border-radius:5px}
.br{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:1px solid #eef1f3}.br p{display:flex;justify-content:space-between;align-items:baseline}.br b{font:700 24px/1.3 Poppins}.br span{font:500 18px Roboto;color:#6b7680}
.bb{display:flex;height:46px;border-radius:12px;overflow:hidden;gap:3px}.bb i{display:flex;align-items:center;justify-content:center;font:700 18px Roboto;font-style:normal;color:#fff}.bb .uS{color:#23272b}
.tt{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.tt div{border-radius:20px;padding:14px 16px;color:#fff;display:flex;flex-direction:column}.tt .uS{color:#23272b}
.tt small{font:700 15px/1.4 Roboto;letter-spacing:2px;opacity:.85}.tt b{font:800 44px/1.4 Poppins;margin-bottom:2px}.tt span{font:500 16px Roboto;opacity:.85}""")

boxes = [("Box 1 · Front office", 30, 30, "Dispatched Mon", "d"), ("Box 2 · Kitchen", 40, 26, "Packing now", "p"), ("Box 3 · Housekeeping", 34, 0, "Stitching", "s"), ("Box 4 · Security", 16, 16, "Ready to dispatch", "r")]
P["p207_uniform_s4"] = ub(4, "PART 3 · PACK AND DISPATCH", "One named pack<br><span>for every staff member.</span>",
f'''<div class=w4><div class=bx>{"".join(f'<div class="cd ct {k}"><small>{a}</small><b>{p} of {n}</b><span>packs ready</span><div class=bar><i style="width:{p/n*100:.0f}%"></i></div><em>{st}</em></div>' for a,n,p,st,k in boxes)}</div>
<div class=pk><div class=lb><small>PACK LABEL · SAMPLE</small><b>Staff 14 · Front office</b><p><span>Shirt L × 3</span><span>Trouser 32 × 2</span><span>Regular fit</span></p></div>
<div class=dl><small>HR GETS A LIST</small><b>Who got which pack</b><span>No mix-ups at the office.</span></div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px}.bx{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px;min-height:0}
.ct{padding:20px 22px;display:flex;flex-direction:column;gap:4px;justify-content:center}.ct small{font:600 15px/1.4 Roboto;letter-spacing:1.5px;color:#6b7680}.ct b{font:800 46px/1.3 Poppins}.ct span{font:500 18px Roboto;color:#6b7680}
.ct .bar{height:12px;border-radius:6px;background:#e3e8ec;overflow:hidden;margin:10px 0}.ct .bar i{display:block;height:100%;background:#2d4f6b}
.ct em{font-style:normal;align-self:flex-start;font:600 17px Roboto;border-radius:10px;padding:5px 12px;background:#e3e8ec}
.ct.d em{background:#23272b;color:#fff}.ct.r em{background:#2d4f6b;color:#fff}.ct.p em{background:#c8b48a}.ct.s em{background:#f3ecdc;color:#7a6230}
.pk{display:flex;gap:14px}.lb{flex:1.3;background:#fff;border:3px dashed #9a7f45;border-radius:20px;padding:16px 20px}
.lb small,.dl small{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#9a7f45}.lb b{display:block;font:700 28px/1.3 Poppins}.lb p{display:flex;gap:8px;margin-top:8px;flex-wrap:wrap}.lb span{background:#eef1f3;border-radius:10px;padding:5px 10px;font:600 17px Roboto}
.dl{flex:1;background:#2d4f6b;color:#fff;border-radius:20px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center}.dl small{color:#c8b48a}.dl b{font:700 26px/1.3 Poppins}.dl span{font:400 18px Roboto;color:#d3dde6}""")

P["p207_uniform_s5"] = ub(5, "YOUR TURN", "Make uniforms<br>for companies?<br><span>Let's build your order app.</span>",
f'''<div class=w5><div class="cd sp5">{shirt}</div><div class=t5>{"".join(f'<div><span class=ib>{ic(i,32)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("send","Size link","Staff fill in their size"),("chart","Size totals","Cut list by size"),("box","Named packs","One per staff"),("users","HR list","Who got what")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#2d4f6b;color:#fff",
css=""".w5{flex:1;display:flex;gap:16px}.sp5{width:380px;flex:none;display:flex;align-items:center;justify-content:center;padding:24px}.sp5 .sh{width:330px}
.t5{flex:1;display:grid;grid-template-rows:repeat(4,1fr);gap:12px}.t5 div{background:#23272b;color:#fff;border-radius:22px;padding:14px 20px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:16px;align-content:center}
.t5 div:nth-child(2n){background:#2d4f6b}.t5 .ib{grid-row:span 2;width:76px;height:76px;border-radius:16px;background:rgba(255,255,255,.12)}.t5 b{font:700 34px/1.3 Poppins}.t5 small{font:400 21px/1.35 Roboto;color:#d3dde6}""")

# ───────── 208 INDIA · Hotel linen laundry (B2B) · SINGLE · Montserrat + Inter · powder blue / white / plum
# New technique: folded linen stacks drawn per item with heights from counts, out vs back side by side, short pieces flagged.
lin = [("Bed sheets", 80, 80), ("Pillow covers", 90, 87), ("Bath towels", 40, 37), ("Hand towels", 10, 10)]
def stack(n, c):
    k = max(1, round(n / 10))
    return '<div class=stk>' + "".join(f'<i style="background:{c}"></i>' for _ in range(k)) + '</div>'
P["p208_linen"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#dfeaf3;color:#1b2440}
.kk{font:700 16px 'Montserrat';letter-spacing:3px;color:#6d2f6f;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:64px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#6d2f6f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tb{flex:1;background:#fff;border-radius:28px;padding:18px 24px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(27,36,64,.08);min-height:0}
.th,.tr{display:grid;grid-template-columns:1.25fr 1fr 1fr .8fr;align-items:center;gap:12px}
.th{padding-bottom:10px;border-bottom:2px solid #e6edf4}.th span{font:700 14px/1.4 Inter;letter-spacing:2px;color:#6b7590}
.tr{flex:1;border-bottom:1px solid #eef2f7}.tr:last-child{border:0}
.tr b{font:700 24px/1.3 Montserrat}
.cl{display:flex;align-items:flex-end;gap:12px}.cl em{font-style:normal;font:700 28px/1.3 Inter}
.stk{display:flex;flex-direction:column-reverse;gap:3px;width:70px}.stk i{display:block;height:9px;border-radius:3px}
.df{justify-self:start;font:700 20px Inter;border-radius:12px;padding:7px 12px;background:#e6f4ea;color:#21653a}.df.sh{background:#6d2f6f;color:#fff}
.sm{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.sm div{border-radius:22px;padding:16px 20px;background:#fff}.sm small{display:block;font:700 14px/1.4 Inter;letter-spacing:2px;color:#6b7590}.sm b{font:800 42px/1.4 Montserrat}
.sm .al{background:#6d2f6f;color:#fff}.sm .al small{color:#e9cdea}
.nt{display:flex;gap:14px;align-items:center;background:#1b2440;color:#fff;border-radius:20px;padding:16px 20px;font:500 20px/1.4 Inter}.nt .ib{width:50px;height:50px;border-radius:14px;background:#6d2f6f}
""", "<div class=kk>HOTEL LINEN LAUNDRY · LOT L-58</div><h1>Sent 220 pieces,<br>got 214 back?<br><span>Count both ways.</span></h1>",
f'''<div class=vw><div class=tb><div class=th><span>ITEM · SAMPLE HOTEL</span><span>OUT · FRI 20 NOV</span><span>BACK · SAT 21 NOV</span><span>DIFF</span></div>
{"".join(f'<div class=tr><b>{n}</b><div class=cl>{stack(o,"#b9cde0")}<em>{o}</em></div><div class=cl>{stack(b,"#6d2f6f" if b<o else "#8fb3d1")}<em>{b}</em></div><span class="df {"sh" if b<o else ""}">{"−"+str(o-b) if b<o else "OK"}</span></div>' for n,o,b in lin)}</div>
<div class=sm><div><small>OUT</small><b>220</b></div><div><small>BACK</small><b>214</b></div><div class=al><small>SHORT</small><b>6</b></div></div>
<div class=nt><span class=ib>{ic("bell",26)}</span><span>3 pillow covers and 3 bath towels marked to come with the next lot.</span></div></div>''',
"#1b2440", "Run a hotel laundry? DM us", "background:#6d2f6f;color:#fff")

# ───────── 209 INDIA · Laptop repair shop · SINGLE · Archivo Black + Inter · graphite / mint / coral
# New technique: CSS laptop (screen + hinge + base) showing a live job status page, plus a paper repair tag with string.
steps = [("Received", "Mon 23 Nov", "d"), ("Checked", "Keyboard fault found", "d"), ("Waiting for part", "Keyboard arrives Wed", "n"), ("Repair", "", ""), ("Ready", "", "")]
P["p209_laptop"] = page("""
body{--f:'Inter';--h:'Archivo Black';background:#1f2328;color:#fff}
.kk{font:700 16px 'Inter';letter-spacing:3px;color:#6ee2b8;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:60px;letter-spacing:-1px;line-height:1.22} h1 span{color:#6ee2b8}
.vw{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}
.top{flex:1;display:flex;gap:16px;align-items:center;min-height:0}
.lp{flex:1;display:flex;flex-direction:column;align-items:center}
.scr{width:100%;background:#0c0e11;border-radius:22px 22px 0 0;padding:16px;border:3px solid #3a4049}
.sc{background:#f6f8f7;color:#1f2328;border-radius:8px;padding:24px 24px;display:flex;flex-direction:column;gap:16px}
.sc small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#6b737d}.sc h3{font:400 32px/1.3 'Archivo Black'}
.st{display:flex;align-items:center;gap:14px}.st i{width:34px;height:34px;border-radius:50%;flex:none;border:3px solid #c9d0d6;display:flex;align-items:center;justify-content:center;color:#fff}
.st.d i{background:#1f9e73;border-color:#1f9e73}.st.n i{background:#ff7a6b;border-color:#ff7a6b;box-shadow:0 0 0 6px rgba(255,122,107,.2)}
.st b{font:600 23px/1.3 Inter}.st span{font:400 18px Inter;color:#6b737d;margin-left:auto}.st.n span{color:#c4473a;font-weight:600}
.base{width:104%;height:24px;background:linear-gradient(#c9ced4,#8e959d);border-radius:0 0 26px 26px;position:relative}.base:after{content:"";position:absolute;left:42%;width:16%;height:8px;top:0;background:#6d747c;border-radius:0 0 8px 8px}
.tg{width:230px;flex:none;background:#f3e6c9;color:#1f2328;border-radius:10px 10px 18px 18px;padding:40px 20px 22px;position:relative;transform:rotate(4deg);clip-path:polygon(18% 0,82% 0,100% 12%,100% 100%,0 100%,0 12%)}
.tg:before{content:"";position:absolute;top:14px;left:50%;margin-left:-9px;width:18px;height:18px;border-radius:50%;background:#1f2328}
.tg b{display:block;font:400 34px/1.3 'Archivo Black'}.tg p{font:500 18px/1.45 Inter;margin-top:8px;border-top:2px dashed #c9b48a;padding-top:8px}
.ms{background:#2b3037;border-radius:22px;padding:18px 22px;border-left:8px solid #6ee2b8}.ms small{font:700 14px/1.4 Inter;letter-spacing:2px;color:#6ee2b8}.ms p{font:500 22px/1.45 Inter;margin-top:4px}.ms b{color:#6ee2b8}
.qq{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.qq div{background:#2b3037;border-radius:18px;padding:14px 16px}
.qq b{display:block;font:400 28px/1.3 'Archivo Black'}.qq span{font:500 18px/1.35 Inter;color:#b9c1ca}.qq .r{background:#6ee2b8;color:#1f2328}.qq .r span{color:#1f4d3d}.qq .w{background:#ff7a6b;color:#1f2328}.qq .w span{color:#5a1f19}
""", "<div class=kk>LAPTOP REPAIR SHOPS · JOB J-512</div><h1>“Is my laptop ready?”<br><span>Send a live status link.</span></h1>",
f'''<div class=vw><div class=ms><small>TEXT TO SAMPLE CUSTOMER · MON 23 NOV</small><p>Your laptop J-512 is checked. The keyboard part arrives Wed. Track it here: <b>yourshop.com/J-512</b></p></div><div class=top><div class=lp><div class=scr><div class=sc><small>YOURSHOP.COM/J-512 · SAMPLE</small><h3>Your laptop repair</h3>
{"".join(f'<div class="st {k}"><i>{ic("check",16,w=3) if k=="d" else ""}</i><b>{a}</b><span>{b}</span></div>' for a,b,k in steps)}</div></div><div class=base></div></div>
<div class=tg><b>J-512</b><p>Sample customer<br>Some keys not working<br>Charger kept: No<br>Data backup: Asked</p></div></div>
<div class=qq><div class=r><b>J-509</b><span>Ready for pickup</span></div><div><b>J-510</b><span>In repair</span></div><div><b>J-511</b><span>Checked</span></div><div class=w><b>J-512</b><span>Waiting for part</span></div></div></div>''',
"#fff", "Run a laptop repair shop? DM us", "background:#6ee2b8;color:#1f2328")

# ───────── 210 USA · Tree service · SINGLE · TeX Gyre Adventor + Source Sans 3 · moss green / sky / bark brown
# New technique: customer photo drawn as a scene with numbered dashed cut marks + estimate list + crew day chip.
scene = '''<svg viewBox="0 -170 520 810" class=sc2 preserveAspectRatio="xMidYMax meet"><rect y="-170" width="520" height="810" fill="#dceef7"/><g fill="#fff"><ellipse cx="130" cy="-90" rx="70" ry="24"/><ellipse cx="170" cy="-106" rx="44" ry="26"/><ellipse cx="380" cy="40" rx="60" ry="20"/><ellipse cx="410" cy="26" rx="36" ry="22"/></g><circle cx="440" cy="-110" r="34" fill="#ffd36b"/>
<rect y="540" width="520" height="100" fill="#9cc27e"/>
<path d="M240 420 L380 330 L520 420 Z" fill="#7a4a35"/><rect x="262" y="420" width="240" height="140" fill="#f4efe6" stroke="#5a3d2b" stroke-width="4"/><rect x="300" y="460" width="60" height="50" fill="#bfdbe9" stroke="#5a3d2b" stroke-width="4"/><rect x="410" y="470" width="50" height="90" fill="#5a3d2b"/>
<path d="M150 560 L162 330 L176 330 L190 560 Z" fill="#5a3d2b"/>
<path d="M168 360 L300 300" stroke="#5a3d2b" stroke-width="12" stroke-linecap="round"/><path d="M165 300 L70 230" stroke="#8a7a6a" stroke-width="10" stroke-linecap="round"/>
<circle cx="170" cy="230" r="110" fill="#3f6b3a"/><circle cx="100" cy="280" r="70" fill="#4f7d45"/><circle cx="240" cy="270" r="80" fill="#4f7d45"/><circle cx="300" cy="300" r="46" fill="#3f6b3a"/>
<path d="M60 220 L40 200 M60 220 L80 196 M70 230 L50 246" stroke="#8a7a6a" stroke-width="6" stroke-linecap="round"/>
<ellipse cx="420" cy="590" rx="44" ry="16" fill="#7a5a40"/><ellipse cx="420" cy="584" rx="36" ry="10" fill="#b08a64"/>
<g fill="none" stroke="#e2512f" stroke-width="5" stroke-dasharray="12 9"><circle cx="58" cy="222" r="44"/><path d="M270 250 L330 350"/><circle cx="420" cy="586" r="58"/></g>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="#e2512f"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="24" fill="#fff"><tspan>{n}</tspan></text>' for n,x,y in [(1,104,170),(2,352,250),(3,480,520)]) + '</svg>'
jobs = [("Remove dead limb", "Over the driveway"), ("Trim branches over roof", "Keep 10 ft clear"), ("Grind old stump", "Front yard, rake and clean")]
P["p210_tree"] = page("""
body{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:#eef4ea;color:#26331f}
.kk{font:700 16px 'Source Sans 3';letter-spacing:3px;color:#7a4a35;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#3f6b3a}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.ph{width:440px;flex:none;border-radius:26px;overflow:hidden;position:relative;background:#dceef7;box-shadow:0 16px 30px rgba(38,51,31,.15)}
.sc2{width:100%;height:100%;display:block}
.pt{position:absolute;left:16px;bottom:16px;background:rgba(38,51,31,.88);color:#fff;border-radius:14px;padding:8px 14px;font:600 17px 'Source Sans 3';display:flex;gap:8px;align-items:center}
.rt{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.es{flex:1;min-height:0;background:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:6px}
.es small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6d7a66}
.jb{flex:1;min-height:0;display:flex;gap:14px;align-items:center;border-top:1px solid #e4ece0}
.jb i{font-style:normal;width:40px;height:40px;border-radius:50%;background:#e2512f;color:#fff;display:flex;align-items:center;justify-content:center;font:700 21px 'Source Sans 3';flex:none}
.jb b{display:block;font:700 23px/1.25 'TeX Gyre Adventor'}.jb span{font:400 18px 'Source Sans 3';color:#5d6a57}
.ok{background:#3f6b3a;color:#fff;border-radius:22px;padding:16px 20px}.ok small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#cfe3c8}.ok b{display:block;font:700 28px/1.3 'TeX Gyre Adventor'}
.cr{background:#5a3d2b;color:#fff;border-radius:22px;padding:16px 20px;display:flex;gap:14px;align-items:center}.cr .ib{width:50px;height:50px;border-radius:14px;background:rgba(255,255,255,.15)}.cr b{display:block;font:700 24px/1.3 'TeX Gyre Adventor'}.cr span{font:400 18px 'Source Sans 3';color:#e6d6c8}
""", "<div class=kk>TREE SERVICES · PHOTO ESTIMATES</div><h1>Driving out just<br>to see the tree?<br><span>Get the photo first.</span></h1>",
f'''<div class=vw><div class=ph>{scene}<div class=pt>{ic("camera",20)}Photo sent by a sample customer</div></div>
<div class=rt><div class=es><small>ESTIMATE E-88 · 3 JOBS</small>{"".join(f'<div class=jb><i>{i}</i><div><b>{a}</b><span>{b}</span></div></div>' for i,(a,b) in enumerate(jobs,1))}</div>
<div class=ok><small>SENT THE SAME DAY</small><b>Customer approved online</b></div>
<div class=cr><span class=ib>{ic("truck",28)}</span><div><b>Crew A · Thu, Dec 3</b><span>8 AM · chipper truck</span></div></div></div></div>''',
"#26331f", "Run a tree service? DM us", "background:#3f6b3a;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
