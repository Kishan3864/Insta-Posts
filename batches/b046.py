import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 246 USA · Window tint shop · SINGLE · Montserrat + Inter · smoke black / chrome / sky
# New technique: car side view where each window takes the picked shade (opacity), plus a shade ladder the customer taps per window.
shade = {"Front doors": 35, "Rear doors": 20, "Back glass": 20}
op = lambda p: (100 - p) / 100 * 0.85
car = f'''<svg viewBox="0 0 900 340" class=cr><ellipse cx="450" cy="318" rx="400" ry="16" fill="#cfd5dc"/>
<path d="M60 240 L80 180 Q100 160 150 155 L270 150 L350 80 Q370 64 410 64 L610 64 Q650 64 680 88 L760 150 Q830 158 845 190 L852 240 Q852 262 830 262 L80 262 Q58 260 60 240 Z" fill="#e9edf2" stroke="#15181c" stroke-width="5"/>
<path d="M365 86 L440 80 L440 150 L300 152 Z" fill="#9cc7e6"/><path d="M365 86 L440 80 L440 150 L300 152 Z" fill="#15181c" fill-opacity="{op(shade["Front doors"]):.2f}" stroke="#15181c" stroke-width="3"/>
<path d="M460 80 L600 80 L640 150 L460 150 Z" fill="#9cc7e6"/><path d="M460 80 L600 80 L640 150 L460 150 Z" fill="#15181c" fill-opacity="{op(shade["Rear doors"]):.2f}" stroke="#15181c" stroke-width="3"/>
<path d="M618 82 Q650 84 672 100 L730 150 L660 150 Z" fill="#9cc7e6"/><path d="M618 82 Q650 84 672 100 L730 150 L660 150 Z" fill="#15181c" fill-opacity="{op(shade["Back glass"]):.2f}" stroke="#15181c" stroke-width="3"/>
<circle cx="210" cy="262" r="50" fill="#15181c"/><circle cx="210" cy="262" r="22" fill="#b9c0c8"/><circle cx="700" cy="262" r="50" fill="#15181c"/><circle cx="700" cy="262" r="22" fill="#b9c0c8"/>
{"".join(f'<circle cx="{x}" cy="{y}" r="22" fill="#2b8fd6" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="21" fill="#fff"><tspan>{n}</tspan></text>' for n,x,y in [(1,380,40),(2,530,40),(3,700,90)])}</svg>'''
P["p246_tint"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#eef2f6;color:#15181c}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#2b8fd6;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#2b8fd6}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.cc{background:#fff;border-radius:26px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(21,24,28,.08)}
.cc>small,.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#68717c}
.cr{width:100%;display:block}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.pk{flex:1;min-width:0;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(21,24,28,.08)}
.wr{flex:1;display:grid;grid-template-columns:200px 1fr;gap:12px;align-items:center;border-top:1px solid #eceff3}
.wr b{font:700 21px/1.3 Inter;display:flex;align-items:center;gap:10px}.wr b i{width:30px;height:30px;border-radius:50%;background:#2b8fd6;color:#fff;font:800 15px Inter;font-style:normal;display:flex;align-items:center;justify-content:center}
.sl{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}.sl span{height:46px;border-radius:10px;display:flex;align-items:center;justify-content:center;font:700 16px Inter;color:#fff;border:3px solid transparent}
.sl span.on{border-color:#2b8fd6;box-shadow:0 0 0 3px #fff inset}
.bk{width:320px;flex:none;background:#15181c;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.bk small{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#8fc8f2}
.br{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #2c3138;font:500 19px Inter}.br b{font:700 20px Inter}
.bb{background:#2b8fd6;border-radius:12px;padding:12px;text-align:center;font:700 18px Inter}
""", "<div class=kk>WINDOW TINT SHOP · BOOKINGS</div><h1>“How dark will it look?”<br><span>Show it on their car type.</span></h1>",
f'''<div class=vw><div class=cc><small>SAMPLE SEDAN · SHADES PICKED BY THE CUSTOMER</small>{car}</div>
<div class=bt><div class=pk><small class=cap>PICK A SHADE PER WINDOW · % OF LIGHT LET IN</small>{"".join(f'<div class=wr><b><i>{i+1}</i>{w}</b><div class=sl>{"".join(f'<span class="{"on" if p==shade[w] else ""}" style="background:rgba(21,24,28,{op(p):.2f}),#9cc7e6;background:linear-gradient(rgba(21,24,28,{op(p):.2f}),rgba(21,24,28,{op(p):.2f})),#9cc7e6">{p}%</span>' for p in [50,35,20,5])}</div></div>' for i,w in enumerate(shade))}</div>
<div class=bk><small>BOOKING · SAMPLE</small>{"".join(f'<div class=br><span>{a}</span><b>{b}</b></div>' for a,b in [("Car","Sedan"),("Windows","Sides + back"),("Film","Ceramic"),("Drop-off","Thu 9 AM"),("Ready","Thu 3 PM")])}<div class=bb>Confirm Thu 9 AM</div></div></div></div>''',
"#15181c", "Run a tint shop? DM us", "background:#2b8fd6;color:#fff")

# ───────── 247 INDIA · Dosa / idli batter maker · CAROUSEL 5 · Lora + Inter · rice white / banana leaf green / chutney red
# New techniques: crate of batter packets with made-on dates, shop order sheet by packet size, morning van route, returns board by date.
BT = """
body{--f:'Inter';--h:'Lora';background:#f6f3ea;color:#1f3a22}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#c2412d;margin-top:22px;align-self:flex-start}
h1{font-family:'Lora';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#2f7a3a}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(31,58,34,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#76806f}
.nb{display:flex;align-items:center;gap:14px;background:#1f3a22;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Inter}.nb .ib{width:50px;height:50px;border-radius:14px;background:#c2412d}.nb b{color:#ffd0c5}
.pkt{width:118px;height:150px;border-radius:12px 12px 18px 18px;background:#fffdf7;border:3px solid #1f3a22;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;position:relative}
.pkt:before{content:"";position:absolute;top:10px;left:8px;right:8px;height:6px;border-top:3px dashed #1f3a22}
.pkt b{font:700 20px/1.3 Lora}.pkt span{font:700 14px Inter;padding:3px 8px;border-radius:8px;background:#e3efe0;color:#2f7a3a}.pkt span.old{background:#ffe0d8;color:#c2412d}
"""
def bt(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f3a22;color:#fff"):
    return page(BT + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f3a22", cta, ctacss, tagline=f"{n} / 5")
crate = "".join(f'<div class=pkt><b>{t}</b><span class="{"old" if o else ""}">{d}</span></div>' for t, d, o in [("Idli 1 kg", "Made Mon", False), ("Dosa 1 kg", "Made Mon", False), ("Idli 1 kg", "Made Sat", True), ("Dosa 500 g", "Made Mon", False), ("Dosa 1 kg", "Made Sat", True), ("Idli 500 g", "Made Mon", False)])
P["p247_batter_s1"] = bt(1, "IDLI AND DOSA BATTER · SHOP SUPPLY", "Which packets are old?<br><span>Know before the shop calls.</span>",
f'''<div class=w1><div class="cd cr1"><small class=cap>SHOP 4 · FRIDGE · MON 23 NOV · SAMPLE</small><div class=crt>{crate}</div></div>
<div class=qs>{"".join(f'<div class=q><b>{a}</b><span>{b}</span></div>' for a,b in [("2 packets","made on Saturday, still on the shelf"),("Shop 4 asks","“Take back the old ones?”"),("Your notebook","says 10 sent, not which day")])}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.cr1{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.crt{flex:1;background:#2f7a3a;border-radius:20px;padding:24px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;justify-items:center;align-items:center;box-shadow:inset 0 -12px 0 rgba(0,0,0,.15)}
.crt .pkt{width:200px;height:200px}.crt .pkt b{font-size:28px}.crt .pkt span{font-size:18px;padding:5px 12px}
.qs{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.q{background:#fff;border-radius:20px;padding:16px 18px;border-top:6px solid #c2412d}.q b{display:block;font:700 28px/1.3 Lora}.q span{font:500 18px/1.4 Inter;color:#55604f}""")

shops = [("Shop 1 · Main road", 12, 6, 4), ("Shop 2 · Bus stand", 8, 4, 0), ("Shop 3 · Market", 15, 10, 6), ("Shop 4 · Colony", 10, 6, 2), ("Shop 5 · Station", 6, 4, 2)]
P["p247_batter_s2"] = bt(2, "STEP 1 · TONIGHT'S ORDER SHEET", "Every shop's order,<br><span>by packet size.</span>",
f'''<div class=w2><div class="cd os"><div class=oh><span>SHOP</span><span>IDLI 1 KG</span><span>DOSA 1 KG</span><span>500 G</span></div>{"".join(f'<div class=orr><b>{s}</b><em>{a}</em><em>{b}</em><em>{c if c else "—"}</em></div>' for s,a,b,c in shops)}
<div class="orr tt"><b>To grind tonight</b><em>{sum(x[1] for x in shops)}</em><em>{sum(x[2] for x in shops)}</em><em>{sum(x[3] for x in shops)}</em></div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>Shops order by 8 PM. <b>The grinding list adds itself up.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.os{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.oh,.orr{display:grid;grid-template-columns:1fr 150px 150px 120px;gap:10px;align-items:center}.oh{font:700 14px/1.4 Inter;letter-spacing:2px;color:#76806f;padding-bottom:10px;border-bottom:2px solid #1f3a22}.oh span:not(:first-child){text-align:center}
.orr{flex:1;border-bottom:1px solid #ece8dc}.orr b{font:700 24px/1.3 Lora}.orr em{font:800 28px Inter;font-style:normal;text-align:center}
.tt{border:0;background:#e3efe0;border-radius:14px;padding:0 12px}.tt em{color:#2f7a3a}""")

route = [("5:30 AM", "Kitchen", "Load 95 packets"), ("6:00 AM", "Shop 1 · Main road", "22 packets"), ("6:20 AM", "Shop 2 · Bus stand", "12 packets"), ("6:45 AM", "Shop 3 · Market", "31 packets"), ("7:10 AM", "Shop 4 · Colony", "18 packets"), ("7:30 AM", "Shop 5 · Station", "12 packets")]
P["p247_batter_s3"] = bt(3, "STEP 2 · MORNING DELIVERY · TUE 24 NOV", "One van, five shops,<br><span>before 8 AM.</span>",
f'''<div class=w3><div class="cd rt">{"".join(f'<div class="rs{" k" if i==0 else ""}"><em>{t}</em><i></i><div><b>{a}</b><span>{b}</span></div></div>' for i,(t,a,b) in enumerate(route))}</div>
<div class=sd><div class=sx><b>95</b><span>packets for 5 shops, from tonight's sheet</span></div><div class=sx><b>2 hrs</b><span>kitchen to the last shop</span></div></div></div>''',
css=""".w3{flex:1;display:flex;gap:14px;min-height:0}.rt{flex:1;padding:18px 24px;display:flex;flex-direction:column;position:relative}
.rs{flex:1;display:grid;grid-template-columns:110px 34px 1fr;gap:14px;align-items:center;position:relative}
.rs em{font:700 19px Inter;font-style:normal;color:#76806f}.rs i{width:30px;height:30px;border-radius:50%;background:#fff;border:6px solid #2f7a3a;z-index:2}.rs.k i{background:#c2412d;border-color:#c2412d}
.rs:not(:last-child):after{content:"";position:absolute;left:138px;top:50%;height:100%;width:6px;background:#cfe3cb}
.rs b{display:block;font:700 26px/1.3 Lora}.rs span{font:500 19px Inter;color:#55604f}
.sd{width:280px;flex:none;display:flex;flex-direction:column;gap:12px}.sx{flex:1;background:#1f3a22;color:#fff;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center}.sx b{font:700 60px/1.3 Lora;color:#bfe3b8}.sx span{font:500 19px/1.4 Inter}""")

ret = [("Shop 1", 2, "Made Sat"), ("Shop 2", 0, ""), ("Shop 3", 1, "Made Sat"), ("Shop 4", 2, "Made Sat"), ("Shop 5", 0, "")]
P["p247_batter_s4"] = bt(4, "STEP 3 · RETURNS BY MADE-ON DATE", "Old packets come back.<br><span>Next order gets smaller.</span>",
f'''<div class=w4><div class="cd rb">{"".join(f'<div class=rr><b>{s}</b><div class=pp>{"".join("<i class=o></i>" for _ in range(n)) or "<i class=z></i>"}</div><span>{f"{n} back · {d}" if n else "Nothing old on the shelf"}</span></div>' for s,n,d in ret)}</div>
<div class=nb><span class=ib>{ic("chart",26)}</span><span>5 packets came back this week. <b>Shop 1 and Shop 4 now get 2 fewer on Saturdays.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rb{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.rr{flex:1;display:grid;grid-template-columns:150px 260px 1fr;gap:16px;align-items:center;border-bottom:1px solid #ece8dc}.rr:last-child{border:0}.rr b{font:700 28px/1.3 Lora}.rr span{font:500 21px/1.35 Inter;color:#55604f}
.pp{display:flex;gap:10px}.pp i{width:56px;height:72px;border-radius:8px 8px 12px 12px;border:3px solid #1f3a22}.pp i.o{background:#ffe0d8}.pp i.z{border-style:dashed;border-color:#b9c2b3}""")

P["p247_batter_s5"] = bt(5, "YOUR TURN", "Make batter for shops?<br><span>Let's build your order app.</span>",
f'''<div class=w5><div class="cd hp">{"".join(f'<div class=pkt><b>{t}</b><span>Made Tue</span></div>' for t in ["Idli 1 kg","Dosa 1 kg","Idli 500 g"])}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,40)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Order sheet","Shops order by 8 PM"),("truck","Morning route","Packets per stop"),("clock","Made-on dates","On every packet"),("chart","Returns","Orders adjust by shop")])}</div>
<div class=q>How do shops send you their batter order today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#c2412d;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;justify-content:center;align-items:center;gap:40px;padding:20px}.hp .pkt{width:200px;height:230px}.hp .pkt b{font-size:28px}.hp .pkt span{font-size:18px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:22px;box-shadow:0 10px 22px rgba(31,58,34,.07)}
.ti .ib{width:76px;height:76px;border-radius:20px;background:#e3efe0;color:#2f7a3a}.ti b{display:block;font:700 32px/1.3 Lora}.ti span{font:500 19px/1.35 Inter;color:#55604f}
.q{background:#1f3a22;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Inter}""")

# ───────── 248 INDIA · Same-day document courier · SINGLE · DM Sans + Roboto · envelope buff / royal blue / lime
# New technique: one big envelope as the hero with a tracking stamp column on its face (pickup → handover → delivered) and proof photo frames.
steps = [("10:05 AM", "Picked up", "Sample office, 2nd floor", True), ("10:40 AM", "On the way", "Rider 2 · bike", True), ("11:25 AM", "Delivered", "Signed by reception · photo saved", True)]
P["p248_courier"] = page("""
body{--f:'Roboto';--h:'DM Sans';background:#eef1fb;color:#1b2a6b}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#5a8f00;margin-top:22px}
h1{font-family:'DM Sans';font-weight:800;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#2f4fd8}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.env{flex:1;min-width:0;background:#f1e3c4;border-radius:12px;position:relative;padding:150px 28px 24px;display:flex;flex-direction:column;gap:12px;box-shadow:0 18px 36px rgba(27,42,107,.16)}
.env:before{content:"";position:absolute;left:0;right:0;top:0;height:140px;background:#e6d2a8;clip-path:polygon(0 0,100% 0,50% 100%)}
.to{position:absolute;top:18px;left:28px;font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#7a6440}
.stp{position:absolute;top:16px;right:22px;width:96px;height:110px;border:3px dashed #2f4fd8;border-radius:6px;display:flex;align-items:center;justify-content:center;font:800 18px/1.3 'DM Sans';color:#2f4fd8;text-align:center;background:#f7ecd5}
.ad{font:700 28px/1.3 'DM Sans'}.ad span{display:block;font:500 19px/1.4 Roboto;color:#5d5038}
.tk{flex:1;display:flex;flex-direction:column;gap:10px}
.st{flex:1;display:grid;grid-template-columns:110px 40px 1fr;gap:12px;align-items:center;background:#fbf4e4;border-radius:14px;padding:0 14px}
.st em{font:700 20px Roboto;font-style:normal;color:#5d5038}.st i{width:36px;height:36px;border-radius:50%;background:#2f4fd8;color:#fff;display:flex;align-items:center;justify-content:center}
.st b{display:block;font:700 28px/1.3 'DM Sans'}.st span{font:500 20px/1.35 Roboto;color:#5d5038}
.rc{width:320px;flex:none;display:flex;flex-direction:column;gap:12px}
.pf{flex:1;background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(27,42,107,.08)}
.pf small,.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6a7396}
.ph{flex:1;border-radius:14px;background:linear-gradient(160deg,#c9d3f5,#aebcf0);display:flex;align-items:flex-end;padding:10px;position:relative;overflow:hidden}
.ph em{font:700 15px Roboto;font-style:normal;background:#fff;color:#1b2a6b;padding:5px 10px;border-radius:8px}
.ph .doc{position:absolute;left:50%;top:50%;width:90px;height:110px;margin:-60px 0 0 -45px;background:#fff;border-radius:6px;box-shadow:0 6px 14px rgba(0,0,0,.15);background-image:repeating-linear-gradient(transparent 0 14px,#dfe4f5 14px 17px);background-position:0 18px}
.sl{background:#1b2a6b;color:#fff;border-radius:22px;padding:16px 18px;font:500 19px/1.45 Roboto}.sl b{color:#c8f25a}
""", "<div class=kk>SAME-DAY DOCUMENT COURIER</div><h1>“Did the papers reach?”<br><span>Send proof, not a call.</span></h1>",
f'''<div class=vw><div class=env><span class=to>DOC-248 · SAMPLE</span><div class=stp>SAME<br>DAY</div>
<div class=ad>To: Sample Firm, reception<span>From: Sample office · 1 sealed envelope · pickup slot 10–11 AM</span></div>
<div class=tk>{"".join(f'<div class=st><em>{t}</em><i>{ic("check",18,w=3)}</i><div><b>{a}</b><span>{b}</span></div></div>' for t,a,b,_ in steps)}</div></div>
<div class=rc><div class=pf><small>PROOF PHOTOS · SAMPLE</small><div class=ph><div class=doc></div><em>At pickup · 10:05</em></div><div class=ph><div class=doc></div><em>At delivery · 11:25</em></div></div>
<div class=sl>The sender gets both photos and the time, <b>in one message</b>.</div></div></div>''',
"#1b2a6b", "Run a local courier? DM us", "background:#2f4fd8;color:#fff")

# ───────── 249 INDIA · Paper cup and plate supplier · SINGLE · Gelasio + Open Sans · paper white / coffee brown / teal
# New technique: stacked cup columns (one drawn cup per 100 pieces) per shop vs. its usual weekly use, with reorder flags.
cups = [("Sample Tea Stall", "150 ml cups", 4, 10, True), ("Sample Juice Bar", "250 ml cups", 7, 6, False), ("Sample Snack Corner", "100 ml cups", 2, 6, True), ("Sample Canteen", "200 ml cups", 9, 8, False)]
def cup(c="#f6efe4"):
    return f'<svg viewBox="0 0 60 40" width="150" height="100"><path d="M6 6 L54 6 L48 36 L12 36 Z" fill="{c}" stroke="#4a2f1d" stroke-width="2.5"/><rect x="4" y="3" width="52" height="6" rx="2" fill="#2a8c87"/></svg>'
P["p249_cups"] = page("""
body{--f:'Open Sans';--h:'Gelasio';background:#f3f7f6;color:#4a2f1d}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#2a8c87;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#2a8c87}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.cs{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.cl{background:#fff;border-radius:24px;padding:14px 14px 16px;display:flex;flex-direction:column;align-items:center;gap:8px;box-shadow:0 14px 30px rgba(74,47,29,.08)}
.cl b{font:700 21px/1.3 Gelasio;text-align:center}.cl small{font:600 15px 'Open Sans';color:#7a6a5c}
.stk{flex:1;width:100%;display:flex;flex-direction:column-reverse;align-items:center;justify-content:flex-start;gap:0;position:relative;padding-top:6px}
.stk svg{display:block;margin-top:-70px}.stk svg:last-of-type{margin-top:0}
.lv{position:absolute;left:4px;right:4px;height:26px;border-top:3px dashed #c0581a;text-align:right;z-index:3}
.lv span{font:700 15px/1.4 'Open Sans';color:#c0581a;background:#fff;padding:0 6px;border-radius:6px}
.cn{font:700 18px 'Open Sans'}.fl{align-self:stretch;text-align:center;border-radius:12px;padding:9px 0;font:700 17px 'Open Sans';background:#e3f2f1;color:#2a8c87}.fl.r{background:#ffe8d6;color:#c0581a}
.ms{display:flex;gap:14px;align-items:center;background:#4a2f1d;color:#fff;border-radius:22px;padding:16px 20px}.ms .ib{width:54px;height:54px;border-radius:16px;background:#2a8c87}
.ms p{flex:1;font:500 21px/1.45 'Open Sans'}.ms p b{color:#ffcf9e}
""", "<div class=kk>PAPER CUP SUPPLY · SHOPS AND STALLS</div><h1>Shops call when cups run out?<br><span>See it coming.</span></h1>",
f'''<div class=vw><div class=cs>{"".join(f'<div class=cl><b>{s}</b><small>{t}</small><div class=stk>{"".join(cup() for _ in range(n))}<div class=lv style="bottom:{100+(u-1)*30-26}px"><span>Usual week</span></div></div><div class=cn>{n*100} left</div><div class="fl{" r" if r else ""}">{"Reorder now" if r else "OK this week"}</div></div>' for s,t,n,u,r in cups)}</div>
<div class=ms><span class=ib>{ic("bell",26)}</span><p>One drawn cup = 100 pieces. <b>Tea stall and snack corner</b> get a reorder message today, sample data.</p></div></div>''',
"#4a2f1d", "Supply paper cups? DM us", "background:#2a8c87;color:#fff")

# ───────── 250 CANADA · Seasonal lights installer · SINGLE · Anton + Fira Sans · night navy / warm bulb yellow / snow
# New technique: night house elevation with measured light runs (bulb dots along the roofline) and an install + takedown date pair.
random.seed(250)
def bulbs(x1, y1, x2, y2, n):
    return "".join(f'<circle cx="{x1+(x2-x1)*i/(n-1):.0f}" cy="{y1+(y2-y1)*i/(n-1)+ (4 if i%2 else 0):.0f}" r="6" fill="{random.choice(["#ffd166","#ffe9a8","#ffb84d"])}"/>' for i in range(n))
house = '<svg viewBox="0 0 900 420" class=hs><rect width="900" height="420" fill="#13204a"/>'
house += "".join(f'<circle cx="{random.randint(10,890)}" cy="{random.randint(10,160)}" r="{random.choice([1.5,2,2.5])}" fill="#fff" fill-opacity=".7"/>' for _ in range(40))
house += '<rect y="350" width="900" height="70" fill="#eef3f8"/><path d="M170 190 L450 60 L730 190 Z" fill="#2c3a63" stroke="#0b1430" stroke-width="4"/><rect x="200" y="190" width="500" height="160" fill="#3b4a75" stroke="#0b1430" stroke-width="4"/>'
house += '<rect x="420" y="260" width="60" height="90" fill="#6b4a2f"/><rect x="250" y="230" width="90" height="70" fill="#ffd98a"/><rect x="560" y="230" width="90" height="70" fill="#ffd98a"/>'
house += '<path d="M60 350 L60 300 L90 250 L120 300 L120 350" fill="#2f6b4f"/><path d="M780 350 L780 290 L815 230 L850 290 L850 350" fill="#2f6b4f"/>'
house += bulbs(172, 192, 448, 64, 22) + bulbs(452, 64, 728, 192, 22) + bulbs(200, 352, 700, 352, 28) + bulbs(66, 300, 114, 300, 4) + bulbs(786, 292, 844, 292, 5)
house += '<g font-family="Anton" font-size="24"><rect x="230" y="96" width="110" height="40" rx="10" fill="#ffd166"/><text x="285" y="125" text-anchor="middle" fill="#13204a"><tspan>34 FT</tspan></text><rect x="560" y="96" width="110" height="40" rx="10" fill="#ffd166"/><text x="615" y="125" text-anchor="middle" fill="#13204a"><tspan>34 FT</tspan></text>'
house += '<rect x="395" y="372" width="110" height="40" rx="10" fill="#ffd166"/><text x="450" y="401" text-anchor="middle" fill="#13204a"><tspan>50 FT</tspan></text></g></svg>'
P["p250_lights"] = page("""
body{--f:'Fira Sans';--h:'Anton';background:#0f1a3d;color:#eef3f8}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#ffd166;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#ffd166}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.hc{background:#13204a;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:8px;border:2px solid #263569}
.hc>small,.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#9fb0dd}
.hs{width:100%;display:block;border-radius:16px}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.ls{flex:1;min-width:0;background:#eef3f8;color:#13204a;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}
.lr{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #d6deea;font:500 20px 'Fira Sans'}.lr b{font:400 26px/1.4 'Anton';letter-spacing:.5px}
.lr.t{border-top:2px solid #13204a}.lr.t b{color:#c98a00}
.dt{width:340px;flex:none;display:flex;flex-direction:column;gap:12px}
.dd{flex:1;background:#ffd166;color:#13204a;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;justify-content:center}.dd small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px}.dd b{font:400 40px/1.5 'Anton';letter-spacing:.5px;margin-bottom:6px}.dd span{font:600 17px 'Fira Sans'}
.dd.o{background:#263569;color:#eef3f8}.dd.o small{color:#9fb0dd}
""", "<div class=kk>SEASONAL LIGHTS INSTALLATION · BOOKINGS</div><h1>Every house, measured once.<br><span>Install and take down, booked.</span></h1>",
f'''<div class=vw><div class=hc><small>SAMPLE HOME · LIGHT RUNS FROM THE CUSTOMER'S PHOTO</small>{house}</div>
<div class=bt><div class=ls><small class=cap>LIGHT RUNS · SAMPLE</small>{"".join(f'<div class=lr><span>{a}</span><b>{b}</b></div>' for a,b in [("Roofline, left","34 ft"),("Roofline, right","34 ft"),("Front edge","50 ft"),("2 shrubs","2 nets")])}<div class="lr t"><span>Total string</span><b>118 ft + 2 nets</b></div></div>
<div class=dt><div class=dd><small>INSTALL</small><b>Sat 28 Nov</b><span>Crew 1 · 10 AM</span></div><div class="dd o"><small>TAKE DOWN · ALREADY BOOKED</small><b>Sat 9 Jan</b><span>Reminder sent a week before</span></div></div></div></div>''',
"#eef3f8", "Install seasonal lights? DM us", "background:#ffd166;color:#13204a", logo_color="#eef3f8")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
