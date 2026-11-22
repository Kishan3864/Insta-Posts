import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 57 INDIA · Optical shop · CAROUSEL 6 · TeX Gyre Adventor + Inter · tortoise brown / cream / teal
# New technique: big CSS spectacles hero (thick bordered lenses + bridge) and CSS frame-shape catalogue.
OP = """
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#fbf3e4;color:#3b2414}
h1{font-family:'TeX Gyre Adventor';font-size:62px;font-weight:700;letter-spacing:-1.5px} h1 span{color:#0f7c7a}
.sub{color:#7a5a43}
.kk{font:700 17px Inter;letter-spacing:4px;color:#0f7c7a;margin-top:22px}
.num{display:inline-flex;align-items:center;justify-content:center;width:64px;height:64px;border-radius:18px;background:#6b3f1f;color:#fbf3e4;font:700 34px/1 'TeX Gyre Adventor';margin-top:22px}
.cd{background:#fff;border-radius:26px;box-shadow:0 18px 40px rgba(59,36,20,.08)}
.pl{font-style:normal;font:700 16px Inter;padding:6px 12px;border-radius:10px}
.t1{background:#d9f0ee;color:#0b6664}.t2{background:#fde6c8;color:#9a5b12}.t3{background:#e9e2f8;color:#5a3fa8}.t4{background:#dcf3e1;color:#167a3a}
"""
def op(n, head, vis, css, cta="Swipe", ctacss="background:#6b3f1f;color:#fbf3e4"):
    return page(OP + css, head, vis, "#3b2414", cta, ctacss, tagline=f"{n} / 6")

P["p57_optical_s1"] = op(1, """<div class=kk>FOR OPTICAL SHOPS</div><h1 style="margin-top:10px">4 things your own app<br><span>can do for your shop.</span></h1>""",
f'''<div class=gl><div class=frm><div class=ln><b>Records</b></div><div class=br></div><div class=ln><b>Orders</b></div></div></div>
<div class=g4>{"".join(f'<div class="cd it"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Every customer's power, saved"),(2,"A frame catalogue online"),(3,"Lab orders, tracked"),(4,"“Ready” messages, sent on their own")])}</div>''',
""".vis{flex-direction:column;gap:22px}
.gl{flex:1;background:#0f7c7a;border-radius:30px;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden}
.frm{display:flex;align-items:center}
.ln{width:300px;height:250px;border:26px solid #6b3f1f;border-radius:46% 46% 50% 50%;background:radial-gradient(circle at 30% 25%,rgba(255,255,255,.55),rgba(255,255,255,.12) 45%,rgba(255,255,255,.05));display:flex;align-items:center;justify-content:center;box-shadow:0 18px 0 rgba(0,0,0,.12)}
.ln b{font:700 36px 'TeX Gyre Adventor';color:#fff}
.br{width:70px;height:40px;border-top:22px solid #6b3f1f;border-radius:50% 50% 0 0}
.g4{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:none}
.it{padding:22px 24px;display:flex;align-items:center;gap:16px}
.it span{width:52px;height:52px;border-radius:14px;background:#0f7c7a;color:#fff;font:700 26px/52px 'TeX Gyre Adventor';text-align:center;flex:none}
.it b{font:700 24px/1.3 Inter}
""")

P["p57_optical_s2"] = op(2, """<div class=num>1</div><h1 style="margin-top:16px">Every customer's power,<br><span>saved and found fast.</span></h1>""",
f'''<div class="cd rc"><div class=sr>{ic("search",26)}<span>Search by name or phone number</span></div>
<div class=hd><div class=av>SC</div><div><b>Sample Customer</b><small>Customer since 2022 · 3 visits</small></div></div>
<table><tr><th>Eye</th><th>SPH</th><th>CYL</th><th>AXIS</th></tr><tr><td>Right</td><td>-1.25</td><td>-0.50</td><td>180</td></tr><tr><td>Left</td><td>-1.00</td><td>-0.25</td><td>170</td></tr></table>
<div class=lb>PAST VISITS · SAMPLE</div>{"".join(f'<div class=vr><span>{a}</span><b>{b}</b><em class="pl {c}">{d}</em></div>' for a,b,c,d in [("Nov 2026","Round metal frame","t1","Latest"),("Mar 2025","Anti-glare lenses","t2","Lens change"),("Jan 2024","Square acetate frame","t3","First visit")])}</div>''',
""".vis{flex-direction:column}
.rc{flex:1;padding:26px 28px;display:flex;flex-direction:column;gap:14px}
.sr{display:flex;align-items:center;gap:12px;border:2px solid #eadbc6;border-radius:16px;padding:14px 18px;font:500 21px Inter;color:#9a7b62}
.hd{display:flex;align-items:center;gap:16px}.av{width:64px;height:64px;border-radius:50%;background:#6b3f1f;color:#fff;font:700 24px/64px 'TeX Gyre Adventor';text-align:center}
.hd b{display:block;font:700 30px 'TeX Gyre Adventor'}.hd small{font:500 19px Inter;color:#7a5a43}
table{width:100%;border-collapse:separate;border-spacing:0 8px;font:600 26px Inter}
th{font:700 16px Inter;letter-spacing:2px;color:#9a7b62;text-align:left;padding:0 18px}
td{background:#f4fbfa;padding:16px 18px}td:first-child{border-radius:14px 0 0 14px;font-weight:700;color:#0f7c7a}td:last-child{border-radius:0 14px 14px 0}
.lb{font:700 15px Inter;letter-spacing:3px;color:#9a7b62;margin-top:4px}
.vr{flex:1;display:flex;align-items:center;gap:18px;background:#fbf3e4;border-radius:16px;padding:0 20px}
.vr span{font:600 19px Inter;color:#7a5a43;width:96px}.vr b{flex:1;font:700 22px Inter}
""")

frames = [("Round", "metal", "rnd", "In stock"), ("Square", "acetate", "sq", "3 colours"), ("Cat-eye", "acetate", "ce", "In stock"),
          ("Rimless", "light", "rl", "In stock"), ("Wayfarer-style", "bold", "wf", "2 colours"), ("Half-rim", "office", "hr", "New")]
P["p57_optical_s3"] = op(3, """<div class=num>2</div><h1 style="margin-top:16px">A frame catalogue<br><span>customers can browse.</span></h1>""",
browser(f'''<div class=cat><div class=fl>{"".join(f'<span class="{"on" if i==0 else ""}">{t}</span>' for i,t in enumerate(["All frames","Men","Women","Metal","Acetate"]))}</div><div class=fg>{"".join(f'<div class=fc><div class="fs {k}"><i></i><u></u><i></i></div><b>{a}</b><small>{b}</small><em class="pl {"t4" if s=="In stock" else "t2" if s!="New" else "t3"}">{s}</em></div>' for a,b,k,s in frames)}</div></div>''', "youropticals.com/frames · sample", "flex:1"),
""".vis{flex-direction:column}
.cat{flex:1;display:flex;flex-direction:column;padding:20px;gap:16px;background:#fffaf2}
.fl{display:flex;gap:10px}.fl span{font:600 18px Inter;padding:9px 14px;border-radius:12px;background:#f1e6d5}.fl span.on{background:#6b3f1f;color:#fff}
.fg{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.fc{background:#fff;border-radius:18px;border:2px solid #f1e6d5;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.fc b{font:700 27px 'TeX Gyre Adventor';margin-top:14px}.fc small{font:500 20px Inter;color:#7a5a43}.fc em{margin-top:6px}
.fs{display:flex;align-items:center}
.fs i{width:112px;height:84px;border:11px solid #3b2414;display:block}
.fs u{width:28px;height:14px;border-top:7px solid #3b2414;display:block;border-radius:40% 40% 0 0}
.rnd i{border-radius:50%;border-width:7px;width:100px;height:100px;border-color:#a8792b}
.sq i{border-radius:12px}
.ce i{border-radius:60% 60% 40% 40% / 70% 70% 30% 30%;border-color:#6b3f1f}
.rl i{border:3px solid #9aa7a6;border-radius:30%}
.wf i{border-radius:8px 8px 30px 30px;border-width:11px}
.hr i{border-width:9px 3px 3px;border-radius:6px 6px 40% 40%;border-color:#0f7c7a #9aa7a6 #9aa7a6}
""")

orders = [("#L-118", "Ravi S.", "Single vision, anti-glare", "t3", "At the lab"), ("#L-119", "Meena P.", "Progressive lenses", "t2", "Fitting"),
          ("#L-120", "Arjun K.", "Single vision", "t4", "Ready"), ("#L-121", "Farah N.", "Sunglass lenses", "t1", "Delivered")]
P["p57_optical_s4"] = op(4, """<div class=num>3</div><h1 style="margin-top:16px">Know where every<br><span>lab order is.</span></h1>""",
f'''<div class="cd tl">{"".join(f'<div class="sp{" dn" if i<3 else ""}"><span>{i+1}</span><b>{t}</b></div>' for i,t in enumerate(["Ordered","At the lab","Fitting","Ready"]))}</div>
<div class="cd ol"><div class=oh><span>LAB ORDERS · SAMPLE</span><span>4 open</span></div>{"".join(f'<div class=orw><div><b>{a} · {c}</b><small>{l}</small></div><em class="pl {k}">{s}</em></div>' for a,c,l,k,s in orders)}</div>''',
""".vis{flex-direction:column;gap:18px}
.tl{display:flex;padding:24px 26px;gap:10px;flex:none}
.sp{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;position:relative}
.sp span{width:56px;height:56px;border-radius:50%;background:#f1e6d5;color:#9a7b62;font:700 24px/56px 'TeX Gyre Adventor';text-align:center}
.sp.dn span{background:#0f7c7a;color:#fff}.sp b{font:700 20px Inter}
.ol{flex:1;padding:24px 26px;display:flex;flex-direction:column;gap:12px}
.oh{display:flex;justify-content:space-between;font:700 15px Inter;letter-spacing:3px;color:#9a7b62}
.orw{flex:1;display:flex;align-items:center;justify-content:space-between;background:#fbf3e4;border-radius:18px;padding:0 22px}
.orw b{display:block;font:700 25px Inter}.orw small{font:500 19px Inter;color:#7a5a43}.orw em{font-size:18px;padding:8px 14px}
""")

P["p57_optical_s5"] = op(5, """<div class=num>4</div><h1 style="margin-top:16px">“Your glasses are ready”<br><span>goes out on its own.</span></h1>""",
f'''<div class=w5>{phone(f"""<div class=ms><div class=mh><span>YO</span><div><b>Your Opticals</b><small>Sample message</small></div></div>
<div class=bb>Hello Arjun, your glasses (order #L-120) are ready. Pick them up any time from 10 am to 9 pm.</div>
<div class=bb>Bring this message for a quick pickup.</div><div class=me>Thank you! Coming at 6 pm.</div></div>""", 380, 700)}
<div class=sd>{"".join(f'<div class="cd sx"><span>{ic(i,30)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("bell","Ready alert","When the order is marked ready"),("clock","Pickup reminder","If they don't come in 3 days"),("spark","New collection","To past buyers, when you choose")])}</div></div>''',
""".w5{flex:1;display:flex;gap:26px;align-items:center}
.ms{flex:1;background:#f4fbfa;padding:16px;display:flex;flex-direction:column;gap:14px}
.mh{display:flex;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:12px}
.mh span{width:46px;height:46px;border-radius:50%;background:#0f7c7a;color:#fff;font:700 18px/46px Inter;text-align:center;flex:none}
.mh b{display:block;font:700 19px Inter}.mh small{font:500 14px Inter;color:#7a5a43}
.bb{background:#fff;border-radius:18px 18px 18px 6px;padding:14px 16px;font:500 19px/1.45 Inter;color:#3b2414}
.me{align-self:flex-end;background:#0f7c7a;color:#fff;border-radius:18px 18px 6px 18px;padding:14px 16px;font:500 19px/1.45 Inter}
.sd{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:16px;padding:10px 0}
.sx{flex:1;display:flex;align-items:center;gap:16px;padding:0 22px}
.sx span{width:62px;height:62px;border-radius:18px;background:#d9f0ee;color:#0f7c7a;display:flex;align-items:center;justify-content:center;flex:none}
.sx b{display:block;font:700 25px/1.3 'TeX Gyre Adventor'}.sx small{font:500 19px/1.35 Inter;color:#7a5a43}
""")

P["p57_optical_s6"] = op(6, """<div class=kk>FOR YOUR OPTICAL SHOP</div><h1 style="margin-top:10px">Want this app<br><span>for your shop?</span></h1><div class=sub>We build simple apps and websites for optical shops. Tell us how you work today.</div>""",
f'''<div class=w6>{peep("PointingUp","Smile","ShortCurly","None","GlassRound",w=380,h=640)}<div class=o6>{"".join(f'<div class="cd q"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Customer records"),(2,"Frame catalogue"),(3,"Lab order tracking"),(4,"Ready messages")])}</div></div>''',
""".w6{flex:1;display:flex;align-items:flex-end;gap:18px}
.o6{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q span{width:60px;height:60px;border-radius:18px;background:#0f7c7a;color:#fff;font:700 28px/60px 'TeX Gyre Adventor';text-align:center;flex:none}
.q b{font:700 30px/1.25 'TeX Gyre Adventor'}
""", cta="Run an optical shop? DM us", ctacss="background:#0f7c7a;color:#fff")

# ───────── 60 USA · Bubble tea shop · CAROUSEL 5 · Archivo Black + DM Sans · taro purple / milk tea beige / tapioca black
# New techniques: CSS illustrated drink cup with pearls, and a tablet mockup (first tablet in the log).
BT = """
body{--f:'DM Sans';--h:'Archivo Black';background:#f3e6d3;color:#231a17}
h1{font-family:'Archivo Black';font-size:64px;font-weight:400;letter-spacing:-1px;line-height:1.22} h1 span{color:#7b52b8}
.sub{color:#6b5a4c}
.stp{display:inline-block;align-self:flex-start;margin-top:22px;font:700 18px 'DM Sans';letter-spacing:3px;background:#231a17;color:#f3e6d3;padding:8px 14px;border-radius:10px}
.tab{background:#231a17;border-radius:40px;padding:20px;box-shadow:0 30px 60px rgba(35,26,23,.25);display:flex}
.scr{flex:1;background:#fffaf3;border-radius:24px;overflow:hidden;display:flex;flex-direction:column}
"""
def bt(n, head, vis, css, cta="Swipe", ctacss="background:#7b52b8;color:#fff"):
    return page(BT + css, head, vis, "#231a17", cta, ctacss, tagline=f"{n} / 5")

def cup(w=300):
    return f'''<div class=cupw style="width:{w}px"><div class=straw></div><div class=lid></div><div class=cup><div class=tea></div><div class=prl></div><div class=lbl>TARO · L</div></div></div>'''
CUPCSS = """
.cupw{position:relative;height:520px;flex:none}
.straw{position:absolute;left:58%;top:0;width:34px;height:200px;background:#231a17;border-radius:10px;transform:rotate(8deg)}
.lid{position:absolute;left:4%;right:4%;top:110px;height:60px;border-radius:120px 120px 12px 12px;background:rgba(255,255,255,.75);border:4px solid #231a17}
.cup{position:absolute;left:4%;right:4%;top:166px;bottom:0;clip-path:polygon(0 0,100% 0,88% 100%,12% 100%);background:#231a17}
.tea{position:absolute;inset:6px 6px 6px;clip-path:polygon(0 0,100% 0,88% 100%,12% 100%);background:linear-gradient(#c7a6ec,#a27fd6)}
.prl{position:absolute;left:16%;right:16%;bottom:12px;height:110px;background:radial-gradient(circle,#231a17 13px,transparent 14px) 0 0/36px 34px}
.lbl{position:absolute;left:50%;top:40%;transform:translateX(-50%);background:#fffaf3;border-radius:12px;padding:8px 14px;font:800 20px 'DM Sans';letter-spacing:2px;color:#231a17;white-space:nowrap}
"""

P["p60_bubbletea_s1"] = bt(1, """<h1 style="margin-top:34px">Long line at 3 pm?<br><span>Let regulars order ahead.</span></h1><div class=sub>An order-ahead page for bubble tea shops, with a stamp card built in.</div>""",
f'''<div class=hero><div class=sun>{cup(300)}</div><div class=s1r>{"".join(f'<div class=s1c><span>{k}</span><b>{t}</b><small>{d}</small></div>' for k,t,d in [(1,"Build the drink","Sweetness, ice, toppings"),(2,"Pick a time","Ready when they walk in"),(3,"Earn stamps","No paper card to lose")])}</div></div>''',
CUPCSS + """.hero{flex:1;display:flex;gap:24px}
.sun{flex:1;background:#e3d3f5;border-radius:30px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:30px;overflow:hidden}
.s1r{flex:1;display:flex;flex-direction:column;gap:16px}
.s1c{flex:1;background:#fffaf3;border-radius:26px;padding:0 26px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.s1c span{width:52px;height:52px;border-radius:50%;background:#7b52b8;color:#fff;font:400 24px/52px 'Archivo Black';text-align:center;margin-bottom:6px}
.s1c b{font:400 30px/1.25 'Archivo Black'}.s1c small{font:500 21px 'DM Sans';color:#6b5a4c}
""")

def chips(lbl, items, on):
    return f'<div class=og><small>{lbl}</small><div class=cr>{"".join(f"""<span class='{"on" if t in on else ""}'>{t}</span>""" for t in items)}</div></div>'
P["p60_bubbletea_s2"] = bt(2, """<div class=stp>STEP 1</div><h1 style="margin-top:14px">They build the drink<br><span>the way they like it.</span></h1>""",
f'''<div class=tab><div class=scr><div class=th2><b>Taro milk tea</b><span>Sample menu</span></div><div class=bd>
{chips("SIZE",["Medium","Large"],["Large"])}{chips("SWEETNESS",["0%","25%","50%","75%","100%"],["50%"])}{chips("ICE",["No ice","Less ice","Normal"],["Less ice"])}{chips("TOPPINGS",["Pearls","Pudding","Jelly","Cheese foam"],["Pearls","Jelly"])}
<div class=sm><div><small>YOUR DRINK</small><b>Taro, large, 50% sweet, less ice, pearls + jelly</b></div><em>Add to order</em></div></div></div></div>''',
""".vis{flex-direction:column}.tab{flex:1}
.th2{display:flex;justify-content:space-between;align-items:center;padding:20px 26px;background:#e3d3f5}
.th2 b{font:400 30px 'Archivo Black'}.th2 span{font:700 16px 'DM Sans';letter-spacing:2px;color:#5b3d8f}
.bd{flex:1;display:flex;flex-direction:column;gap:12px;padding:20px 26px}
.og{flex:1;display:flex;flex-direction:column;justify-content:center;gap:10px}
.og small{font:700 15px 'DM Sans';letter-spacing:3px;color:#8a7867}
.cr{display:flex;gap:10px}.cr span{flex:1;text-align:center;font:700 21px 'DM Sans';padding:14px 6px;border-radius:14px;background:#f3e6d3}
.cr span.on{background:#7b52b8;color:#fff}
.sm{display:flex;align-items:center;gap:16px;background:#231a17;color:#fff;border-radius:18px;padding:16px 20px}
.sm div{flex:1}.sm small{font:700 14px 'DM Sans';letter-spacing:3px;color:#c7a6ec}.sm b{display:block;font:700 21px/1.35 'DM Sans'}
.sm em{font-style:normal;background:#c7a6ec;color:#231a17;font:800 18px 'DM Sans';padding:12px 16px;border-radius:12px;flex:none}
""")

slots = [("3:00", "full"), ("3:10", "full"), ("3:20", "pick"), ("3:30", ""), ("3:40", ""), ("3:50", "full"), ("4:00", ""), ("4:10", ""), ("4:20", "")]
P["p60_bubbletea_s3"] = bt(3, """<div class=stp>STEP 2</div><h1 style="margin-top:14px">They pick a time.<br><span>Ready when they walk in.</span></h1>""",
f'''<div class=w3><div class=sl><small>PICKUP TIME · TODAY · SAMPLE</small><div class=sg>{"".join(f'<div class="{c}">{t}<em>{"Full" if c=="full" else "Picked" if c=="pick" else "Open"}</em></div>' for t,c in slots)}</div></div>
<div class=sh><small>PICKUP SHELF</small>{"".join(f'<div class=bx><span>{n}</span><b>{d}</b></div>' for n,d in [("Sam · 3:20","Taro, large"),("Lee · 3:20","Mango green tea"),("Ana · 3:30","Brown sugar milk")])}</div></div>''',
""".w3{flex:1;display:flex;gap:20px}
.sl{flex:1.3;background:#fffaf3;border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:14px}
.sl small,.sh small{font:700 15px 'DM Sans';letter-spacing:3px;color:#8a7867}
.sg{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.sg div{border-radius:18px;background:#f3e6d3;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;font:400 30px 'Archivo Black'}
.sg em{font-style:normal;font:700 16px 'DM Sans';color:#6b5a4c}
.sg div.full{background:#ebe3d8;color:#b3a594}.sg div.full em{color:#b3a594}
.sg div.pick{background:#7b52b8;color:#fff}.sg div.pick em{color:#e3d3f5}
.sh{flex:1;background:#231a17;border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:14px}
.sh small{color:#c7a6ec}
.bx{flex:1;background:#3a2d28;border-radius:18px;padding:0 18px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-bottom:8px solid #7b52b8}
.bx span{font:800 22px 'DM Sans';color:#fff}.bx b{font:500 19px 'DM Sans';color:#e3d3f5}
""")

P["p60_bubbletea_s4"] = bt(4, """<div class=stp>STEP 3</div><h1 style="margin-top:14px">The stamp card<br><span>fills itself.</span></h1>""",
f'''<div class=sc><div class=st><small>SAMPLE STAMP CARD</small><b>7 of 10 drinks</b><div class=pg4>{"".join(f'<i class="{"on" if i<7 else ""}">{i+1}</i>' for i in range(10))}</div><p>3 more drinks to the reward.</p></div>
<div class=nb>{"".join(f'<div><span>{ic(i,30)}</span><b>{t}</b></div>' for i,t in [("check","A stamp is added with every order"),("x","No paper card to lose"),("spark","You choose the reward")])}</div></div>''',
""".sc{flex:1;display:flex;flex-direction:column;gap:18px}
.st{flex:1;background:#7b52b8;color:#fff;border-radius:30px;padding:28px 30px;display:flex;flex-direction:column;gap:10px}
.st small{font:700 15px 'DM Sans';letter-spacing:3px;color:#e3d3f5}.st b{font:400 42px/1.25 'Archivo Black'}
.pg4{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:16px;align-content:center}
.pg4 i{aspect-ratio:1;border-radius:50%;border:4px dashed #c7a6ec;display:flex;align-items:center;justify-content:center;font:800 24px 'DM Sans';font-style:normal;color:#e3d3f5}
.pg4 i.on{background:radial-gradient(circle at 35% 30%,#6b5450,#231a17 60%);border:4px solid #231a17;color:#fff}
.st p{font:600 23px 'DM Sans';color:#f3e6d3}
.nb{display:flex;gap:14px;flex:none}
.nb div{flex:1;background:#fffaf3;border-radius:22px;padding:20px;display:flex;flex-direction:column;gap:10px}
.nb span{width:52px;height:52px;border-radius:14px;background:#e3d3f5;color:#5b3d8f;display:flex;align-items:center;justify-content:center}
.nb b{font:700 21px/1.35 'DM Sans'}
""")

P["p60_bubbletea_s5"] = bt(5, """<h1 style="margin-top:34px">Want order-ahead<br><span>for your tea shop?</span></h1><div class=sub>We build order pages, pickup times and stamp cards for drink shops.</div>""",
f'''<div class=w5>{peep("Coffee","Smile","Long","None",w=380,h=620)}<div class=o5>{"".join(f'<div class=q5><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Drink builder"),(2,"Pickup times"),(3,"Stamp card"),(4,"Your menu, your rules")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;background:#fffaf3;border-radius:24px;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:60px;height:60px;border-radius:50%;background:#7b52b8;color:#fff;font:400 26px/60px 'Archivo Black';text-align:center;flex:none}
.q5 b{font:400 29px/1.25 'Archivo Black'}
""", cta="Own a bubble tea shop? DM us", ctacss="background:#231a17;color:#f3e6d3")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
