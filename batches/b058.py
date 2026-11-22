import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 306 INDIA · Stone crusher / aggregate supplier · CAROUSEL 5 · Anton + Source Sans 3 · quarry grey / safety yellow / rust
# New technique: SVG stockpile cones with seeded gravel texture, height by stock, used as the series motif.
CR = """
body{--f:'Source Sans 3';--h:'Anton';background:#e7e5e0;color:#26282b}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#a4471f;margin-top:22px;align-self:flex-start}
h1{font-family:'Anton';font-weight:400;font-size:70px;letter-spacing:.5px;line-height:1.3;margin-top:32px} h1 span{color:#a4471f}
.cd{background:#fff;border-radius:22px;box-shadow:0 12px 28px rgba(38,40,43,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6f7075}
.nb{display:flex;align-items:center;gap:14px;background:#26282b;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 'Source Sans 3'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#f5c518;color:#26282b}.nb b{color:#f5c518}
"""
def cr(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#26282b;color:#f5c518"):
    return page(CR + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#26282b", cta, ctacss, tagline=f"{n} / 5")
def pile(h, base="#8c8e93", dot="#5c5e63", w=220, seed=1, H=260):
    rnd = random.Random(seed); top = H - h
    dots = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{rnd.uniform(2,4.5):.1f}" fill="{rnd.choice([dot,"#d8d9db","#45474b"])}"/>'
                   for x, y in ((rnd.uniform(10, 210), rnd.uniform(top + 8, H - 4)) for _ in range(int(h * 1.6)))
                   if abs(x - 110) < (y - top) / h * 104)
    return f'''<svg viewBox="0 0 220 {H+10}" width="{w}" class=pl><path d="M4 {H} L110 {top} L216 {H} Z" fill="{base}"/>{dots}<rect x="0" y="{H}" width="220" height="10" rx="5" fill="#b9b6ad"/></svg>'''
stock = [("10 mm", 120, 1), ("20 mm", 210, 2), ("40 mm", 80, 3), ("Dust", 150, 4)]
P["p306_crush_s1"] = cr(1, "STONE CRUSHER · AGGREGATE SUPPLY", "Sites calling all day?<br><span>Know every load.</span>",
f'''<div class=w1><div class="cd pc1"><small class=cap>STOCK IN THE YARD · TONNES · SAMPLE</small><div class=pr1>{"".join(f'<div class=pi>{pile(h*1.8, seed=s, H=400)}<b>{a}</b><span>{h} t</span></div>' for a,h,s in stock)}</div></div>
<div class=bb1><span class=vn>{ic("phone",24)} Site engineer · 9:40 AM</span><p>“Send 2 loads of 20 mm by 11. Where is the truck from yesterday?”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pc1{flex:1;min-height:0;padding:20px 24px;display:flex;flex-direction:column}
.pr1{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:8px;align-items:end}.pi{display:flex;flex-direction:column;align-items:center}.pl{display:block;width:100%;height:auto}
.pi b{font:400 34px/1.5 Anton;letter-spacing:.5px;margin:8px 0 6px}.pi span{font:700 22px/1.5 'Source Sans 3';color:#a4471f}
.bb1{background:#26282b;color:#fff;border-radius:22px 22px 22px 6px;padding:18px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px 'Source Sans 3';color:#f5c518;margin-bottom:6px}.bb1 p{font:500 24px/1.4 'Source Sans 3'}""")

orders = [("Site A · Ring road", "20 mm", 2, "Before 11 AM"), ("Site B · Mall", "10 mm", 1, "11 AM – 1 PM"), ("Site C · Bungalow", "Dust", 1, "After 2 PM"),
          ("Site A · Ring road", "40 mm", 1, "After 2 PM"), ("Site D · Factory shed", "20 mm", 3, "Full day"), ("Site E · Road work", "Dust", 2, "Before 11 AM")]
mt = {}
for _, m, l, _t in orders: mt[m] = mt.get(m, 0) + l
P["p306_crush_s2"] = cr(2, "STEP 1 · EVERY SITE ORDER IN ONE LIST", "Orders by phone?<br><span>One list for the day.</span>",
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>SITE · SAMPLE</span><span>MATERIAL</span><span>LOADS</span><span>WHEN</span></div>
{"".join(f'<div class=rw2><b>{s}</b><span class=mc>{m}</span><em>{l}</em><span class=tm>{t}</span></div>' for s,m,l,t in orders)}</div>
<div class=tt2>{"".join(f'<div><span>{m}</span><b>{v} load{'s' if v>1 else ''}</b></div>' for m,v in mt.items())}</div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.tb2{flex:1;padding:12px 26px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:1.7fr .9fr .6fr 1fr;gap:12px;align-items:center;border-bottom:1px solid #ecebe7}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #26282b;font:700 14px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#6f7075}
.rw2 b{font:700 23px 'Source Sans 3'}.mc{justify-self:start;background:#f5c518;border-radius:8px;padding:4px 12px;font:700 19px 'Source Sans 3'}.rw2 em{font:400 36px/1.4 Anton;font-style:normal;color:#a4471f}.tm{font:600 19px 'Source Sans 3';color:#4c4e53}
.tt2{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.tt2 div{background:#26282b;border-radius:18px;padding:14px 16px;color:#fff}.tt2 span{display:block;font:700 16px/1.5 'Source Sans 3';color:#c9cacd;margin-bottom:4px}.tt2 b{font:400 32px/1.5 Anton;letter-spacing:.5px;color:#f5c518}""")

# trucks: rounds as (start_min_from_7AM, dur, site, material)
trucks = [("Truck T-1", [(30, 90, "A", "20 mm"), (150, 90, "D", "20 mm"), (300, 90, "D", "20 mm")]),
          ("Truck T-2", [(30, 80, "E", "Dust"), (140, 80, "E", "Dust"), (270, 100, "C", "Dust")]),
          ("Truck T-3", [(60, 90, "A", "20 mm"), (240, 100, "B", "10 mm")]),
          ("Truck T-4", [(120, 100, "D", "20 mm"), (300, 100, "A", "40 mm")])]
TOT = 420
rounds = sum(len(r) for _, r in trucks)
P["p306_crush_s3"] = cr(3, "STEP 2 · TRUCK ROUNDS ON ONE BOARD", "4 trucks, {} rounds.<br><span>No site is missed.</span>".format(rounds),
f'''<div class=w3><div class="cd rb3"><small class=cap>TODAY · 7 AM TO 2 PM · SAMPLE</small>{"".join(f'<div class=tr3><b>{t}</b><div class=rib>{"".join(f"<span class=rd3 style=left:{s/TOT*100:.1f}%;width:{d/TOT*100:.1f}%><em>Site {x}</em><i>{m}</i></span>" for s,d,x,m in r)}</div></div>' for t,r in trucks)}
<div class=ax3>{"".join(f'<span style="left:{m/TOT*100:.1f}%">{l}</span>' for m,l in [(0,"7 AM"),(120,"9 AM"),(240,"11 AM"),(360,"1 PM")])}</div></div>
<div class=nb><span class=ib>{ic("truck",26)}</span><span>The driver taps “left the yard”, <b>and the site gets a message with the truck number.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rb3{flex:1;padding:18px 24px;display:flex;flex-direction:column;gap:6px}
.tr3{flex:1;display:grid;grid-template-columns:130px 1fr;gap:14px;align-items:center}.tr3 b{font:400 26px/1.5 Anton;letter-spacing:.5px}
.rib{position:relative;height:110px;border-radius:14px;background:repeating-linear-gradient(90deg,#f1f0ec 0 calc(100%/7 - 2px),#e2e0da calc(100%/7 - 2px) calc(100%/7))}
.rd3{position:absolute;top:8px;bottom:8px;border-radius:10px;background:#f5c518;padding:6px 10px;display:flex;flex-direction:column;justify-content:center;box-shadow:inset 0 -5px 0 #d9a90c}
.rd3 em{font:400 22px/1.5 Anton;font-style:normal;letter-spacing:.5px;margin-bottom:4px}.rd3 i{font:700 15px/1.3 'Source Sans 3';font-style:normal}
.ax3{position:relative;height:26px;margin-left:144px;font:700 15px/1.5 'Source Sans 3';color:#6f7075}.ax3 span{position:absolute;top:0}""")

done = [("Site A · Ring road", 3, 2), ("Site B · Mall", 1, 0), ("Site C · Bungalow", 1, 0), ("Site D · Factory shed", 3, 2), ("Site E · Road work", 2, 2)]
P["p306_crush_s4"] = cr(4, "STEP 3 · DELIVERY SLIP WITH A PHOTO", "Ordered vs delivered.<br><span>Clear for every site.</span>",
f'''<div class=w4><div class="cd sl4"><small class=cap>DELIVERY SLIP · SAMPLE</small><div class=ph4><div class=img4>{pile(150, seed=9, w=300)}<span>Photo at site · 9:20 AM</span></div>
<div class=kv4>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [("Slip","DS-0418"),("Site","A · Ring road"),("Material","20 mm"),("Truck","T-3"),("Received by","Site engineer")])}</div></div></div>
<div class="cd dv4"><small class=cap>LOADS · ORDERED VS DELIVERED</small>{"".join(f'<div class=dr4><span>{s}</span><div class=lb4>{"".join("<i class=ok></i>" for _ in range(d))}{"".join("<i></i>" for _ in range(o-d))}<b>{d} / {o}</b></div></div>' for s,o,d in done)}</div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px;min-height:0}.sl4,.dv4{padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.ph4{flex:1;display:flex;flex-direction:column;gap:12px}.img4{flex:1;background:linear-gradient(#cfe0ea,#e9eef0 55%,#c9c3b5 55%);border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:10px;gap:4px}
.img4 span{font:700 15px 'Source Sans 3';color:#26282b;background:rgba(255,255,255,.85);border-radius:8px;padding:3px 10px}
.kv4{display:grid;grid-template-columns:1fr 1fr;gap:8px}.kv4 div{background:#f3f2ee;border-radius:12px;padding:8px 12px}.kv4 div:last-child{grid-column:1 / 3}.kv4 span{display:block;margin-bottom:3px;font:600 14px/1.5 'Source Sans 3';color:#6f7075}.kv4 b{font:700 21px/1.3 'Source Sans 3'}
.dr4{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:1px solid #ecebe7}.dr4 span{font:700 19px 'Source Sans 3'}
.lb4{display:flex;gap:8px}.lb4 i{width:58px;height:30px;border-radius:8px;border:2.5px dashed #9a9ba0}.lb4 i.ok{border:0;background:#f5c518;box-shadow:inset 0 -5px 0 #d9a90c}
.lb4{align-items:center}.lb4 b{margin-left:auto;font:400 30px/1.5 Anton;letter-spacing:.5px;color:#a4471f}""")

P["p306_crush_s5"] = cr(5, "YOUR TURN", "Run a crusher or supply yard?<br><span>Let's build your load book.</span>",
f'''<div class=w5><div class="cd hp5">{"".join(pile(h, seed=s+20, w=210, H=400) for h,s in [(230,1),(380,2),(170,3),(300,4)])}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Site orders","One list a day"),("truck","Truck rounds","Who goes where"),("camera","Delivery slips","Photo at site"),("chart","Stock","Tonnes in the yard")])}</div>
<div class=q>How do sites send you orders today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#a4471f;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;display:flex;justify-content:space-around;align-items:flex-end;padding:20px 24px}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:18px 22px;box-shadow:0 10px 22px rgba(38,40,43,.07)}
.ti .ib{width:70px;height:70px;border-radius:20px;background:#f5c518;color:#26282b}.ti b{display:block;font:400 28px/1.5 Anton;letter-spacing:.5px;margin-bottom:4px}.ti div span{font:500 19px/1.35 'Source Sans 3';color:#55575c}
.q{background:#26282b;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Source Sans 3'}""")

# ───────── 307 INDIA · Ice cream distributor (freezers at shops) · SINGLE · Poppins + Fira Sans · freezer white / berry pink / mint
# New technique: top-down chest freezer (glass lid sheen) with round tub lids by flavour and dashed empty slots.
FL = {"Vanilla": "#f6e7b8", "Mango": "#f7b23b", "Strawberry": "#f07ca0", "Choco": "#7a4a32", "Pista": "#a6d48a"}
slots = ["Vanilla", "Vanilla", "Mango", None, "Strawberry", None, "Choco", None, None, "Pista", None, "Mango"]
empty = slots.count(None)
shops = [("S-01 · Station road", 10, 12), ("S-02 · College gate", 3, 12), ("S-03 · Park corner", 8, 12), ("S-04 · Bus stand", 12 - empty, 12), ("S-05 · Market", 11, 12), ("S-06 · Lake view", 4, 12)]
low = [s for s in shops if s[1] <= 6]
P["p307_icecream"] = page("""
body{--f:'Fira Sans';--h:'Poppins';background:#fdf1f4;color:#3a1830}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#c2386a;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:62px;letter-spacing:-1.8px;line-height:1.22} h1 span{color:#c2386a}
.vw{flex:1;display:grid;grid-template-columns:1fr 360px;gap:14px;min-height:0}
.fz{background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(58,24,48,.08)}
.fz>small,.sl small,.rt7 small{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#86707f}
.ch{flex:1;min-height:0;border-radius:22px;background:#dfe7ec;padding:16px;box-shadow:inset 0 0 0 6px #c8d3da;position:relative}
.gl{position:absolute;inset:16px;border-radius:14px;background:linear-gradient(120deg,rgba(255,255,255,.55) 0 18%,transparent 18% 30%,rgba(255,255,255,.35) 30% 36%,transparent 36%);pointer-events:none;z-index:2}
.tg{height:100%;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:10px;background:#a9c5d3;border-radius:14px;padding:12px}
.tb{border-radius:50%;align-self:center;justify-self:center;width:92%;aspect-ratio:1;display:flex;align-items:center;justify-content:center;font:700 14px 'Fira Sans';box-shadow:0 0 0 5px rgba(255,255,255,.75),0 6px 10px rgba(0,0,0,.12)}
.tb.e{background:transparent;border:3px dashed #6d8796;box-shadow:none;color:#3d5563}
.fl7{display:flex;justify-content:space-between;align-items:center}.fl7 b{font:800 24px/1.3 Poppins}.fl7 em{font:700 16px 'Fira Sans';font-style:normal;background:#fde0ea;color:#a52b58;border-radius:10px;padding:6px 12px}
.sd7{display:flex;flex-direction:column;gap:12px;min-height:0}
.sl{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(58,24,48,.08)}
.sr{flex:1;display:flex;flex-direction:column;justify-content:center;gap:5px;border-top:1px solid #f4e6ec}
.sr div{display:flex;justify-content:space-between;font:600 16px 'Fira Sans'}.sr div b{font:700 16px 'Fira Sans'}
.br{height:12px;border-radius:6px;background:#f4e6ec;overflow:hidden}.br i{display:block;height:100%;border-radius:6px}
.rt7{background:#3a1830;color:#fff;border-radius:22px;padding:14px 18px}.rt7 small{color:#f4b6cb}.rt7 p{font:500 18px/1.45 'Fira Sans';margin-top:4px}.rt7 b{color:#9fe3c4}
""", "<div class=kk>ICE CREAM DISTRIBUTOR · FREEZERS AT SHOPS</div><h1>Which shop freezer is empty?<br><span>Know before they call.</span></h1>",
f'''<div class=vw><div class=fz><small>SHOP S-04 · BUS STAND · FREEZER VIEW · SAMPLE</small><div class=ch><div class=gl></div><div class=tg>{"".join(f'<div class=tb style="background:{FL[s]};color:{"#fff" if s=="Choco" else "#3a1830"}">{s}</div>' if s else '<div class="tb e">Empty</div>' for s in slots)}</div></div>
<div class=fl7><b>{12-empty} of 12 tubs left</b><em>Shop tapped “running low”</em></div></div>
<div class=sd7><div class=sl><small>ALL SHOPS · TUBS LEFT · SAMPLE</small>{"".join(f'<div class=sr><div><span>{n}</span><b style="color:{"#c2386a" if f<=6 else "#2f8a62"}">{f} / {c}</b></div><div class=br><i style="width:{f/c*100:.0f}%;background:{"#f07ca0" if f<=6 else "#7ccfa8"}"></i></div></div>' for n,f,c in shops)}</div>
<div class=rt7><small>TODAY'S REFILL ROUND</small><p>{", ".join(s[0].split(" · ")[0] for s in low)}: <b>{sum(s[2]-s[1] for s in low)} tubs</b> on the van, in this order.</p></div></div></div>''',
"#3a1830", "Supply ice cream to shops? DM us", "background:#c2386a;color:#fff")

# ───────── 308 INDIA · Offset printing press · SINGLE · Cardo + Inter · process cyan / magenta / paper white
# New technique: print sheet imposition (8-up cards) with crop marks, registration targets and a CMYK colour bar, stamped approved.
def card8(i):
    return f'''<div class=vc><div class=vl></div><b>Your Shop</b><span>Sample text line</span><span class=sh>Phone · address</span></div>'''
reg = '<svg viewBox="0 0 30 30" width="30" class=rg><circle cx="15" cy="15" r="9" fill="none" stroke="#111" stroke-width="2"/><path d="M15 0V30M0 15H30" stroke="#111" stroke-width="2"/></svg>'
stages = [("Proof sent", "Mon 23 Nov · 4 PM", "d"), ("Approved by customer", "Tue 24 Nov · 11:20 AM", "d"), ("Plate made", "Tue 24 Nov · 3 PM", "n"), ("Printing", "Wed 25 Nov · AM", "w"), ("Cutting and packing", "Wed 25 Nov · PM", "w"), ("Ready to collect", "Thu 26 Nov · 11 AM", "w")]
P["p308_offset"] = page("""
body{--f:'Inter';--h:'Cardo';background:#eef6f9;color:#14232b}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#c4166e;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;line-height:1.4;margin-bottom:4px} h1 span{color:#0a8fb8}
.vw{flex:1;display:grid;grid-template-columns:1fr 350px;gap:14px;min-height:0}
.sht{background:#fff;border-radius:6px;padding:46px 40px 30px;position:relative;display:flex;flex-direction:column;gap:14px;box-shadow:0 20px 40px rgba(20,35,43,.12)}
.cm{position:absolute;background:#111}
.im{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr);gap:0;outline:1px dashed #9ab}
.vc{border:1px dashed #b8c6cc;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:3px;background:linear-gradient(90deg,#0a8fb8 0 8px,transparent 8px)}
.vc b{font:700 22px/1.3 Cardo;padding-left:10px}.vc span{font:500 13px/1.4 Inter;color:#556;padding-left:10px}.vc .sh{color:#c4166e}
.vl{display:none}
.cb{display:flex;gap:0;height:26px}.cb i{flex:1}
.rgr{display:flex;justify-content:space-between;align-items:center}.rgr small{font:700 12px/1.4 Inter;letter-spacing:1.5px;color:#556}
.rg{display:block}
.bot8{display:flex;align-items:center;gap:16px}.bot8 .cb{flex:1}.stp{flex:none;border:4px solid #1f9d55;color:#1f9d55;border-radius:14px;padding:10px 16px;background:rgba(255,255,255,.92);text-align:center;z-index:3}
.stp b{display:block;font:800 26px/1.3 Inter;letter-spacing:2px}.stp span{font:700 14px/1.4 Inter}
.jc{background:#14232b;color:#fff;border-radius:22px;padding:16px 18px;display:flex;flex-direction:column}
.jc small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#8fd3e8}.jc h3{font:700 26px/1.4 Cardo;margin:2px 0 6px}
.st{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #2a3c46}
.st i{width:26px;height:26px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
.st i.d{background:#1f9d55}.st i.n{background:#c4166e}.st i.w{border:2.5px solid #5d7480}
.st b{display:block;font:600 17px/1.35 Inter}.st span{font:500 14px/1.4 Inter;color:#a9bcc5}
.pp8{background:#fff;color:#14232b;border-radius:14px;padding:10px 12px;margin-top:8px;font:500 15px/1.4 Inter}.pp8 b{color:#c4166e}
""", "<div class=kk>OFFSET PRINTING PRESS · JOB CARDS</div><h1>“I never said yes to this!”<br><span>Get the OK on the proof.</span></h1>",
f'''<div class=vw><div class=sht>
<i class=cm style="left:22px;top:30px;width:2px;height:18px"></i><i class=cm style="left:10px;top:44px;width:18px;height:2px"></i>
<i class=cm style="right:22px;top:30px;width:2px;height:18px"></i><i class=cm style="right:10px;top:44px;width:18px;height:2px"></i>
<div class=rgr>{reg}<small>JOB J-2207 · 1,000 CARDS · 8 ON A SHEET · SAMPLE</small>{reg}</div>
<div class=im>{"".join(card8(i) for i in range(8))}</div>
<div class=bot8><div class=cb>{"".join(f'<i style="background:{c}"></i>' for c in ["#00aeef","#ec008c","#fff200","#111","#7fd6f7","#f57fc5","#fff97f","#777"])}</div>
<div class=stp><b>APPROVED</b><span>Customer · Tue 24 Nov · 11:20 AM</span></div></div></div>
<div class=jc><small>JOB CARD J-2207 · SAMPLE</small><h3>Visiting cards, Your Shop</h3>{"".join(f'<div class=st><i class={k}>{ic("check",15) if k=="d" else ""}</i><div><b>{a}</b><span>{t}</span></div></div>' for a,t,k in stages)}
<div class=pp8>Paper: 300 gsm art card, <b>in stock</b> for this job.</div></div></div>''',
"#14232b", "Run a printing press? DM us", "background:#c4166e;color:#fff")

# ───────── 309 CANADA · Ice fishing hut rental · SINGLE · TeX Gyre Adventor + Inter · frozen lake blue / hut red / pine · PHONE
# New technique: top-down frozen lake with SVG crack lines, numbered huts with roof ridges, shore with pines and a path.
random.seed(309)
cracks = "".join(f'<path d="M{x} {y} l{random.randint(30,70)} {random.randint(-30,30)} l{random.randint(30,70)} {random.randint(-30,30)} l{random.randint(20,60)} {random.randint(-30,30)}" stroke="#ffffff" stroke-width="2.5" fill="none" opacity=".8"/>' for x, y in [(60, 330), (300, 420), (120, 640), (330, 720), (70, 860), (260, 560)])
huts = [(80, 360, "H-1", "b"), (250, 330, "H-2", "f"), (400, 390, "H-3", "b"), (110, 520, "H-4", "f"), (300, 500, "H-5", "b"), (150, 700, "H-6", "b"), (350, 680, "H-7", "f"), (230, 850, "H-8", "b")]
def hut(x, y, n, st):
    roof = "#c8342b" if st == "b" else "#ffffff"; ol = "#7a1d17" if st == "b" else "#c8342b"
    return f'''<rect x="{x}" y="{y}" width="92" height="70" rx="6" fill="{roof}" stroke="{ol}" stroke-width="4"{' stroke-dasharray="9 6"' if st=="f" else ""}/>
<path d="M{x+46} {y+4} V{y+66}" stroke="{ol}" stroke-width="3"/><circle cx="{x+18}" cy="{y+90}" r="7" fill="#1b3a4b"/><circle cx="{x+40}" cy="{y+92}" r="7" fill="#1b3a4b"/>
<rect x="{x+52}" y="{y+80}" width="48" height="26" rx="6" fill="#1b3a4b"/><text x="{x+76}" y="{y+99}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#fff">{n}</text>'''
pines = "".join(f'<path d="M{x} {y} l18 40 h-36 z M{x} {y+18} l22 44 h-44 z" fill="#1f5a3e"/>' for x, y in [(40, 40), (95, 20), (150, 50), (410, 30), (465, 55), (360, 60)])
lake = f'''<svg viewBox="0 0 520 980" class=lk><rect width="520" height="980" rx="22" fill="#cfe6f2"/>
<path d="M0 0 H520 V170 Q400 210 260 190 Q120 170 0 215 Z" fill="#e9efe7"/>{pines}
<rect x="210" y="70" width="100" height="64" rx="8" fill="#7a4a2a"/><text x="260" y="108" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#fff">Shore shack</text>
<path d="M260 134 C250 220 280 300 260 400 S240 600 270 980" stroke="#8fb3c7" stroke-width="10" stroke-dasharray="2 16" stroke-linecap="round" fill="none"/>
{cracks}{"".join(hut(*h) for h in huts)}</svg>'''
nb = sum(1 for h in huts if h[3] == "b"); nf = len(huts) - nb
ph9 = phone(f'''<div class=ap><div class=ah><small>SAMPLE LAKE HUTS</small><b>Book a hut</b><span>Hut H-4 · sleeps 4</span></div>
<div class=fl9><small>PICK A DAY</small><div class=ch9>{"".join(f'<span class="{"on" if a=="Sat 9 Jan" else ""}">{a}</span>' for a in ["Sat 2 Jan","Sat 9 Jan","Sat 16 Jan","Sat 23 Jan"])}</div></div>
<div class=fl9><small>HOW LONG</small><div class=ch9>{"".join(f'<span class="{"on" if a=="Full day" else ""}">{a}</span>' for a in ["Half day","Full day"])}</div></div>
<div class=fl9><small>PEOPLE</small><div class=ct9><i>−</i><b>3</b><i>+</i></div></div>
<div class=fl9><small>IN THE HUT</small>{"".join(f'<div class=ck9><i>{ic("check",15)}</i>{a}</div>' for a in ["Heater and bench","Holes drilled for you","Rod holders"])}</div>
<div class=fl9><small>MEET AT</small><div class=tx9>Shore shack · 7 AM</div></div>
<div class=bk9>Book Sat 9 Jan</div></div>''', 360, 850)
P["p309_icehut"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#e6f0f5;color:#1b3a4b}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#c8342b;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#c8342b}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.lc{flex:1;min-width:0;background:#fff;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(27,58,75,.08)}
.lc>small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#62798a;padding:2px 6px 0}
.lk{flex:1;min-height:0;width:100%;display:block}
.lgd9{display:flex;gap:18px;padding:0 6px 4px}.lgd9 span{display:flex;align-items:center;gap:8px;font:600 16px Inter}.lgd9 i{width:22px;height:18px;border-radius:4px;display:block}
.ap{display:flex;flex-direction:column;gap:9px;padding:8px 18px 18px;flex:1;min-height:0}
.ah small{display:block;font:700 11px/1.4 Inter;letter-spacing:2px;color:#62798a}.ah b{display:block;font:700 24px/1.3 'TeX Gyre Adventor'}.ah span{font:500 14px/1.4 Inter;color:#4a6070}
.fl9{background:#eef5f9;border-radius:14px;padding:9px 12px}.fl9 small{display:block;font:700 11px/1.4 Inter;letter-spacing:1.5px;color:#62798a;margin-bottom:6px}
.ch9{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ch9 span{background:#fff;border-radius:10px;padding:7px 4px;text-align:center;font:600 14px Inter;border:1.5px solid #d3e0e8}.ch9 .on{background:#c8342b;color:#fff;border-color:#c8342b}
.ct9{display:flex;align-items:center;gap:14px}.ct9 i{width:30px;height:30px;border-radius:9px;background:#fff;border:1.5px solid #d3e0e8;display:flex;align-items:center;justify-content:center;font:700 18px Inter;font-style:normal}.ct9 b{font:700 20px Inter}
.ck9{display:flex;align-items:center;gap:10px;font:600 15px/1.3 Inter;padding:3px 0}.ck9 i{width:22px;height:22px;border-radius:6px;background:#1f5a3e;display:flex;align-items:center;justify-content:center;color:#fff}
.tx9{font:600 15px Inter}
.bk9{margin-top:auto;background:#1b3a4b;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 17px Inter}
""", "<div class=kk>ICE FISHING HUT RENTALS</div><h1>“Is a hut free on Saturday?”<br><span>Let them book it.</span></h1>",
f'''<div class=vw><div class=lc><small>HUTS ON THE LAKE · SAMPLE</small>{lake}
<div class=lgd9><span><i style="background:#c8342b;border:3px solid #7a1d17"></i>Booked · {nb}</span><span><i style="background:#fff;border:3px dashed #c8342b"></i>Free · {nf}</span></div></div>
{ph9}</div>''',
"#1b3a4b", "Rent out huts? DM us", "background:#c8342b;color:#fff")

# ───────── 310 INDIA · Album printing lab (for photographers) · CAROUSEL 5 · Gelasio + DM Sans · linen beige / charcoal / gold foil
# New technique: open album spread made of CSS landscape "photo" blocks (no people) with numbered comment pins + page-status thumbnail strip.
AL = """
body{--f:'DM Sans';--h:'Gelasio';background:#efe8dc;color:#2b2a2e}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#a5822f;margin-top:22px;align-self:flex-start}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;line-height:1.25;letter-spacing:-.5px} h1 span{color:#a5822f}
.cd{background:#fffaf2;border-radius:22px;box-shadow:0 12px 28px rgba(43,42,46,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7d7566}
.nb{display:flex;align-items:center;gap:14px;background:#2b2a2e;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.45 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#d8b45a;color:#2b2a2e}.nb b{color:#e8cd84}
.ph{border-radius:6px;position:relative}
.pin{position:absolute;width:40px;height:40px;border-radius:50%;background:#c2412f;color:#fff;font:700 19px/40px 'DM Sans';text-align:center;box-shadow:0 0 0 4px #fff;z-index:2}
.pin.ok{background:#2f8a5b}
"""
def al(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2b2a2e;color:#e8cd84"):
    return page(AL + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2b2a2e", cta, ctacss, tagline=f"{n} / 5")
SC = ["linear-gradient(#f3c48b,#f7e2c4 45%,#7d9a6a 45%,#5c7a4c)", "linear-gradient(#9cc4dc,#d8e8ef 50%,#4f7f9b 50%,#2f5f7b)", "linear-gradient(#f0a37a,#f6d0a6 40%,#c98a5a 40% 60%,#8c5a3a 60%)",
      "linear-gradient(135deg,#d8cbb4,#efe5d2)", "linear-gradient(#b7c7d9,#e6ecf2 55%,#9aa57a 55%)", "linear-gradient(#e7b8a6,#f3dcd0 50%,#a36a5a 50%)"]
def spread(pins=(), w=None):
    p = "".join(f'<span class="pin{" ok" if ok else ""}" style="left:{x}%;top:{y}%">{ic("check",18) if ok else n}</span>' for n, x, y, ok in pins)
    return f'''<div class=sp><div class=pgL><div class=ph style="background:{SC[0]};grid-row:1 / 3"></div><div class=ph style="background:{SC[1]}"></div><div class=ph style="background:{SC[3]}"></div></div>
<div class=gut></div><div class=pgR><div class=ph style="background:{SC[2]}"></div><div class=ph style="background:{SC[4]}"></div><div class=ph style="background:{SC[5]};grid-column:1 / 3"></div></div>{p}</div>'''
SPC = """.sp{position:relative;flex:1;min-height:0;display:flex;background:#fff;border-radius:10px;padding:16px;box-shadow:0 18px 36px rgba(43,42,46,.16)}
.pgL,.pgR{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:10px}.gut{width:18px;background:linear-gradient(90deg,transparent,rgba(0,0,0,.12),transparent)}"""
P["p310_album_s1"] = al(1, "ALBUM PRINTING LAB · FOR PHOTOGRAPHERS", "Changes in 20 voice notes?<br><span>Pin them on the page.</span>",
f'''<div class=w1><div class="cd sc1"><small class=cap>ALBUM A-118 · SPREAD 6 · SAMPLE</small>{spread([(1,20,30,False),(2,72,22,False),(3,64,74,False)])}</div>
<div class=cm1>{"".join(f'<div><span class=nn>{n}</span><p>{t}</p></div>' for n,t in [(1,"Swap this photo with the sunset one."),(2,"Make this photo bigger."),(3,"Move this to spread 8.")])}</div></div>''',
css=SPC + """.w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sc1{flex:1;min-height:0;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.cm1{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.cm1 div{background:#2b2a2e;color:#fff;border-radius:18px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start}
.nn{width:34px;height:34px;border-radius:50%;background:#c2412f;font:700 17px/34px 'DM Sans';text-align:center;flex:none}.cm1 p{font:500 19px/1.4 'DM Sans'}""")

jobs = [("A-118", "Studio · Sample 1", "12 x 36 in", 30, 412, "Designing"), ("A-119", "Studio · Sample 2", "12 x 30 in", 24, 318, "Proof sent"), ("A-120", "Studio · Sample 1", "10 x 24 in", 20, 240, "Photos in"),
        ("A-121", "Studio · Sample 3", "12 x 36 in", 40, 506, "Approved"), ("A-122", "Studio · Sample 4", "12 x 30 in", 30, 0, "Waiting")]
P["p310_album_s2"] = al(2, "STEP 1 · EVERY ALBUM, ONE JOB CODE", "Photos by link.<br><span>Every album has a code.</span>",
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>ALBUM</span><span>PHOTOGRAPHER · SAMPLE</span><span>SIZE · PAGES</span><span>PHOTOS</span><span>STATUS</span></div>
{"".join(f'<div class=rw2><b>{a}</b><span>{p}</span><span>{s} · {g}</span><em>{f if f else "—"}</em><i class="s{st.split()[0][:3]}">{st}</i></div>' for a,p,s,g,f,st in jobs)}</div>
<div class=nb><span class=ib>{ic("upload",26)}</span><span>The photographer uploads the photos on one link, <b>no more pen drives and lost folders.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:12px 24px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:.75fr 1.3fr 1.15fr .65fr 1fr;gap:10px;align-items:center;border-bottom:1px solid #eee5d4}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #2b2a2e;font:700 13px/1.4 'DM Sans';letter-spacing:1.5px;color:#7d7566}
.rw2 b{font:700 25px/1.4 Gelasio}.rw2>span{font:500 18px/1.35 'DM Sans'}.rw2 em{font:700 26px/1.4 Gelasio;font-style:normal;color:#a5822f}
.rw2 i{font:700 15px 'DM Sans';font-style:normal;border-radius:10px;padding:6px 10px;text-align:center;background:#eee5d4}
.sDes{background:#f8e6b8!important}.sPro{background:#f6d6cf!important;color:#8a2a1c}.sApp{background:#d6eedd!important;color:#1f6a40}.sWai{background:#ececec!important;color:#666}""")

pages = ["a"] * 9 + ["c"] * 2 + ["a"] * 3 + ["p"] * 1 + ["c"] * 1 + ["p"] * 2 + ["a"] * 2 + ["p"] * 4 + ["a"] * 1
counts = {k: pages.count(k) for k in "acp"}
P["p310_album_s3"] = al(3, "STEP 2 · PROOF ONLINE, CHANGES PINNED", "{} spreads.<br><span>See which ones are done.</span>".format(len(pages)),
f'''<div class=w3><div class="cd th3"><small class=cap>ALBUM A-119 · PROOF · SAMPLE</small><div class=gr3>{"".join(f'<div class="tn {k}"><div class=mi3><i style="background:{SC[i%6]}"></i><i style="background:{SC[(i+2)%6]}"></i></div><span>{i+1}</span></div>' for i,k in enumerate(pages))}</div>
<div class=lgd3>{"".join(f'<span><i class="{k}"></i>{a} · {counts[k]}</span>' for k,a in [("a","Approved"),("c","Changes pinned"),("p","Not seen yet")])}</div></div>
<div class=nb><span class=ib>{ic("chat",26)}</span><span>The couple and the photographer pin changes on the spread, <b>not in voice notes.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.th3{flex:1;min-height:0;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.gr3{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:12px}.tn{border-radius:12px;padding:8px;display:flex;flex-direction:column;gap:4px;border:3px solid #d8d0c0;background:#fff}
.mi3{flex:1;display:flex;gap:4px}.mi3 i{flex:1;border-radius:3px}.tn span{font:700 15px/1.3 'DM Sans';text-align:center}
.tn.a{border-color:#2f8a5b}.tn.c{border-color:#c2412f}.tn.p{border-style:dashed;opacity:.7}
.lgd3{display:flex;gap:24px}.lgd3 span{display:flex;align-items:center;gap:8px;font:600 18px 'DM Sans'}.lgd3 i{width:22px;height:22px;border-radius:6px;border:3px solid #d8d0c0}.lgd3 i.a{border-color:#2f8a5b}.lgd3 i.c{border-color:#c2412f}.lgd3 i.p{border-style:dashed}""")

covers = [("Linen", "repeating-linear-gradient(0deg,#cdbf9f 0 2px,#d9ccae 2px 4px),#d4c6a6", False), ("Leather look", "radial-gradient(circle at 30% 30%,#6b4a35 0 1px,transparent 1.5px) 0 0/6px 6px,#5a3b28", True), ("Velvet", "linear-gradient(135deg,#3f2a4f,#5a3d6e)", False)]
P["p310_album_s4"] = al(4, "STEP 3 · COVER, PRINT, DISPATCH", "Cover picked.<br><span>Ready date sent.</span>",
f'''<div class=w4><div class="cd cv4"><small class=cap>ALBUM A-121 · COVER · SAMPLE</small><div class=cr4>{"".join(f'<div class="cc{" on" if on else ""}"><div class=bk4 style="background:{b}"><span>A-121</span></div><b>{a}</b>{"<em>Picked</em>" if on else ""}</div>' for a,b,on in covers)}</div></div>
<div class="cd dp4"><small class=cap>A-121 · STEPS</small>{"".join(f'<div class=sr4><i class={k}>{ic("check",15) if k=="d" else ""}</i><div><b>{a}</b><span>{t}</span></div></div>' for a,t,k in [("Proof approved","Fri 20 Nov","d"),("Cover picked","Sat 21 Nov","d"),("Printing","Tue 24 Nov","n"),("Binding","Thu 26 Nov","w"),("Courier to studio","Sat 28 Nov","w")])}</div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:14px;min-height:0}.cv4,.dp4{padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.cr4{flex:1;display:grid;grid-template-rows:repeat(3,1fr);gap:12px}.cc{display:flex;align-items:center;gap:18px;border-radius:16px;padding:10px 14px;border:2px solid #eee5d4}.cc.on{border:3px solid #a5822f;background:#fbf3e0}
.bk4{width:150px;height:100%;min-height:90px;border-radius:6px 12px 12px 6px;box-shadow:inset 10px 0 0 rgba(0,0,0,.18),0 8px 14px rgba(0,0,0,.15);display:flex;align-items:center;justify-content:center}
.bk4 span{font:700 18px Gelasio;color:#e8cd84;letter-spacing:2px}.cc b{flex:1;font:700 28px/1.4 Gelasio}.cc em{font:700 15px 'DM Sans';font-style:normal;background:#a5822f;color:#fff;border-radius:10px;padding:6px 12px}
.sr4{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #eee5d4}.sr4 i{width:30px;height:30px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
.sr4 i.d{background:#2f8a5b}.sr4 i.n{background:#a5822f}.sr4 i.w{border:3px solid #c9bfae}.sr4 b{display:block;font:700 22px/1.35 Gelasio}.sr4 span{font:500 17px 'DM Sans';color:#6d6658}""")

P["p310_album_s5"] = al(5, "YOUR TURN", "Print albums for photographers?<br><span>Let's build your proof portal.</span>",
f'''<div class=w5><div class="cd hp5">{spread([(1,24,30,True),(2,70,24,True),(3,62,72,True)])}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("upload","Photo upload","By job code"),("chat","Pinned changes","On the spread"),("check","Online approval","With date and time"),("truck","Dispatch","Message to studio")])}</div>
<div class=q>How do photographers send you changes today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#a5822f;color:#fff",
css=SPC + """.w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;padding:18px 22px;display:flex}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fffaf2;border-radius:22px;padding:16px 22px;box-shadow:0 10px 22px rgba(43,42,46,.07)}
.ti .ib{width:66px;height:66px;border-radius:20px;background:#f3e6c4;color:#a5822f}.ti b{display:block;font:700 25px/1.4 Gelasio}.ti div span{font:500 18px/1.35 'DM Sans';color:#5e584c}
.q{background:#2b2a2e;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'DM Sans'}""")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
