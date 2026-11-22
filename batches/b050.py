import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 266 INDIA · Home chef (party orders) · CAROUSEL 5 · Crimson Text + Inter · tomato red / leaf green / cream
# New technique: top-down party table plan (plates as circles around long tables) whose plate count drives the quantity sheet.
def table(n, w=640, cls="tb6"):
    per = n // 2
    plates = "".join(f'<i class=pl6 style="left:{(i+0.5)*100/per:.2f}%"></i>' for i in range(per))
    return f'<div class={cls}><div class=row6>{plates}</div><div class=tt6></div><div class=row6>{plates}</div></div>'
HC = """
body{--f:'Inter';--h:'Crimson Text';background:#fbf5ea;color:#3a1d14}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#2f7a3d;margin-top:22px;align-self:flex-start}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#d2462e}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(58,29,20,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#86756b}
.tb6{display:flex;flex-direction:column;gap:6px;width:100%}.row6{position:relative;height:46px}
.pl6{position:absolute;top:4px;width:40px;height:40px;margin-left:-20px;border-radius:50%;background:#fff;border:3px solid #3a1d14;box-shadow:inset 0 0 0 7px #fde3d6}
.tt6{height:56px;border-radius:10px;background:repeating-linear-gradient(90deg,#d2462e 0 28px,#e86a52 28px 56px);border:3px solid #3a1d14}
.nb{display:flex;align-items:center;gap:14px;background:#3a1d14;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Inter'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#2f7a3d}.nb b{color:#ffc6b5}
"""
def hc(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3a1d14;color:#fff"):
    return page(HC + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3a1d14", cta, ctacss, tagline=f"{n} / 5")
P["p266_chef_s1"] = hc(1, "HOME CHEF · PARTY ORDERS", "“We are 30 now… or 36?”<br><span>Cook for the right number.</span>",
f'''<div class=w1><div class="cd tp"><small class=cap>SAT 5 DEC · SAMPLE HOUSE PARTY · TOP VIEW</small>{table(16)}{table(14)}{table(6)}<div class=ad><span>+ 6 guests added on Friday night</span></div></div>
<div class=q3>{"".join(f'<div class=qx><b>{a}</b><span>{b}</span></div>' for a,b in [("30 → 36","Guests changed twice"),("Paneer?","For 30 or for 36?"),("Rotis","Nobody re-counted")])}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tp{flex:1;padding:18px 26px;display:flex;flex-direction:column;justify-content:space-around;gap:10px}
.tp .tb6:last-of-type .pl6{border-color:#d2462e;border-style:dashed}
.ad{align-self:flex-start;font:700 19px Inter;background:#fde3d6;color:#b3361f;padding:8px 14px;border-radius:10px}
.q3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.qx{background:#fff;border-radius:20px;padding:16px 20px;border-top:6px solid #d2462e}.qx b{display:block;font:700 34px/1.3 'Crimson Text'}.qx span{font:500 18px Inter;color:#6d5a50}""")

menu = [("Starter", "Paneer tikka", True), ("Main", "Dal makhani", True), ("Main", "Veg pulao", True), ("Bread", "Butter roti", True), ("Sweet", "Gulab jamun", True), ("Starter", "Corn chaat", False)]
P["p266_chef_s2"] = hc(2, "STEP 1 · THE HOST PICKS THE MENU", "A menu link,<br><span>not a long call.</span>",
f'''<div class=w2><div class="cd mn"><small class=cap>YOUR PARTY MENU · SAMPLE</small>{"".join(f'<div class="mr{" on" if o else ""}"><em>{c}</em><b>{d}</b><i>{"✓" if o else "+"}</i></div>' for c,d,o in menu)}</div>
<div class=sd>{"".join(f'<div class="cd sx"><small class=cap>{a}</small><b>{b}</b></div>' for a,b in [("DATE","Sat 5 Dec"),("GUESTS","36"),("SERVE AT","8 PM"),("SPICE","Medium")])}</div></div>''',
css=""".w2{flex:1;display:flex;gap:14px;min-height:0}.mn{flex:1;padding:16px 22px;display:flex;flex-direction:column}
.mr{flex:1;display:grid;grid-template-columns:110px 1fr 48px;gap:12px;align-items:center;border-top:1px solid #f1e8dc}.mr em{font:700 15px Inter;font-style:normal;letter-spacing:1px;color:#86756b;text-transform:uppercase}.mr b{font:700 30px/1.3 'Crimson Text'}
.mr i{width:44px;height:44px;border-radius:12px;border:3px solid #e8dccd;font:800 22px/38px Inter;font-style:normal;text-align:center;color:#86756b}.mr.on i{background:#2f7a3d;border-color:#2f7a3d;color:#fff}
.sd{width:280px;flex:none;display:flex;flex-direction:column;gap:12px}.sx{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center}.sx b{font:700 40px/1.3 'Crimson Text';color:#d2462e}""")

qty = [("Paneer tikka", "100 g each", "3.6 kg"), ("Dal makhani", "150 ml each", "5.4 L"), ("Veg pulao", "120 g each", "4.3 kg"), ("Butter roti", "3 each", "108"), ("Gulab jamun", "2 each", "72")]
P["p266_chef_s3"] = hc(3, "STEP 2 · QUANTITIES FROM YOUR OWN RULES", "36 guests in,<br><span>shopping list out.</span>",
f'''<div class=w3><div class="cd qt"><div class=qh><span>DISH</span><span>YOUR RULE</span><span>FOR 36</span></div>{"".join(f'<div class=qr><b>{a}</b><span>{b}</span><em>{c}</em></div>' for a,b,c in qty)}</div>
<div class=nb><span class=ib>{ic("cart",26)}</span><span>Guests change to 40? <b>Every quantity updates at once.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.qt{flex:1;padding:18px 26px;display:flex;flex-direction:column}
.qh,.qr{display:grid;grid-template-columns:1.3fr 1fr 150px;gap:12px;align-items:center}.qh{font:700 14px/1.4 Inter;letter-spacing:2px;color:#86756b;padding-bottom:10px;border-bottom:2px solid #3a1d14}.qh span:last-child{text-align:right}
.qr{flex:1;border-bottom:1px solid #f1e8dc}.qr:last-child{border:0}.qr b{font:700 32px/1.3 'Crimson Text'}.qr span{font:500 21px Inter;color:#6d5a50}.qr em{font:800 30px Inter;font-style:normal;text-align:right;color:#2f7a3d}""")

cal = [("Mon 30", ""), ("Tue 1", ""), ("Wed 2", "Lunch · 20"), ("Thu 3", ""), ("Fri 4", "Dinner · 15"), ("Sat 5", "Dinner · 36"), ("Sun 6", "Lunch · 25")]
P["p266_chef_s4"] = hc(4, "STEP 3 · ONE PARTY PER SLOT", "Your week of parties,<br><span>never double booked.</span>",
f'''<div class=w4><div class=cl>{"".join(f'<div class="dy{" b" if t else ""}{" hl" if d=="Sat 5" else ""}"><em>{d}</em><b>{t.split(" · ")[0] if t else "Open"}</b><span>{(t.split(" · ")[1]+" guests") if t else "Take a booking"}</span></div>' for d,t in cal)}<div class="dy nx"><em>Next week</em><b>2 booked</b><span>Mon 7 – Sun 13 Dec</span></div></div>
<div class=nb><span class=ib>{ic("cal",26)}</span><span>Your rule: one big party a day. <b>Full days close on the booking page.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.cl{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:12px}
.dy{background:#fff;border-radius:22px;padding:18px;display:flex;flex-direction:column;border:3px dashed #e8dccd}.dy em{font:700 20px Inter;font-style:normal;color:#86756b}.dy b{margin-top:auto;font:700 36px/1.3 'Crimson Text'}.dy span{font:500 18px Inter;color:#6d5a50}
.dy.b{border:3px solid #2f7a3d;background:#eef7ef}.dy.b b{color:#2f7a3d}.dy.hl{border-color:#d2462e;background:#fde3d6}.dy.hl b{color:#d2462e}
.dy.nx{background:#3a1d14;border:3px solid #3a1d14}.dy.nx em{color:#ffc6b5}.dy.nx b{color:#fff}.dy.nx span{color:#e9d6cc}""")

P["p266_chef_s5"] = hc(5, "YOUR TURN", "Cook for parties from home?<br><span>Let's build your order page.</span>",
f'''<div class=w5><div class="cd hp"><div style="width:100%;display:flex;flex-direction:column;gap:40px">{table(12)}{table(12)}</div></div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Menu link","The host picks dishes"),("users","Guest count","Change it any time"),("cart","Shopping list","From your own rules"),("cal","Party calendar","One slot per party")])}</div>
<div class=q>How do you take party orders today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#d2462e;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;align-items:center;padding:24px 34px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(58,29,20,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#fde3d6;color:#d2462e}.ti b{display:block;font:700 32px/1.3 'Crimson Text'}.ti div span{font:500 19px/1.35 Inter;color:#6d5a50}
.q{background:#3a1d14;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Inter}""")

# ───────── 267 USA · In-home personal trainer · SINGLE · Archivo Black + Roboto · court blue / lime / white
# New technique: week planner where drive time between client homes is drawn as hatched blocks between session blocks.
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
blocks = {  # (start hour from 6, length hours, kind, label)
 "Mon": [(0.5, 1, "s", "Client A"), (1.5, .5, "d", ""), (2, 1, "s", "Client B"), (5, 1, "s", "Client C")],
 "Tue": [(1, 1, "s", "Client D"), (2, .5, "d", ""), (2.5, 1, "s", "Client E")],
 "Wed": [(0.5, 1, "s", "Client A"), (1.5, .5, "d", ""), (2, 1, "s", "Client B"), (6, 1, "o", "Open")],
 "Thu": [(1, 1, "s", "Client D"), (2, .5, "d", ""), (2.5, 1, "s", "Client E"), (5, 1, "o", "Open")],
 "Fri": [(0.5, 1, "s", "Client A"), (1.5, .5, "d", ""), (2, 1, "s", "Client F")],
}
H = 8
grid = "".join(f'<div class=dcol><b>{d}</b><div class=dtrack>{"".join(f"<i class={k} style=\"top:{s/H*100:.2f}%;height:{l/H*100:.2f}%\">{t}</i>" for s,l,k,t in blocks[d])}</div></div>' for d in days)
hours = "".join(f'<span style="top:{h/H*100:.2f}%">{["6 AM","8 AM","10 AM","12 PM","2 PM"][h//2]}</span>' for h in range(0, 9, 2))
P["p267_trainer"] = page("""
body{--f:'Roboto';--h:'Archivo Black';background:#eef3fb;color:#132a52}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#2a63d4;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.22;margin-top:16px} h1 span{color:#2a63d4}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.wk{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 20px 20px 84px;display:flex;flex-direction:column;gap:8px;position:relative;box-shadow:0 14px 30px rgba(19,42,82,.08)}
.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6b7a93;margin-left:-64px}
.gw{flex:1;display:flex;gap:8px;position:relative;min-height:0}
.hrs{position:absolute;left:-70px;top:38px;bottom:0;width:60px}.hrs span{position:absolute;font:600 15px Roboto;color:#6b7a93;transform:translateY(-50%)}
.dcol{flex:1;display:flex;flex-direction:column;gap:8px}.dcol>b{font:400 20px/1.4 'Archivo Black';text-align:center;height:30px}
.dtrack{flex:1;position:relative;border-radius:12px;background:repeating-linear-gradient(#f3f6fb 0 calc(12.5% - 1px),#e4eaf3 calc(12.5% - 1px) 12.5%)}
.dtrack i{position:absolute;left:4px;right:4px;border-radius:10px;font:700 16px/1.3 Roboto;font-style:normal;display:flex;align-items:center;justify-content:center;text-align:center}
.dtrack i.s{background:#2a63d4;color:#fff}.dtrack i.d{background:repeating-linear-gradient(45deg,#c9f27a 0 6px,#e6fbbf 6px 12px)}.dtrack i.o{border:3px dashed #2a63d4;color:#2a63d4;background:#fff}
.lg3{display:flex;gap:18px;font:600 16px Roboto;color:#4f5f7a;margin-left:-64px}.lg3 span{display:flex;align-items:center;gap:8px}.lg3 i{width:24px;height:16px;border-radius:4px;background:#2a63d4}.lg3 i.d{background:repeating-linear-gradient(45deg,#c9f27a 0 4px,#e6fbbf 4px 8px)}.lg3 i.o{background:#fff;border:2px dashed #2a63d4}
.rc{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.bk{flex:1;background:#132a52;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.bk small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#c9f27a}
.br{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:1px solid #2b4370}.br span{font:500 16px Roboto;color:#a9b8d3}.br b{font:700 22px/1.35 Roboto}
.bb{background:#c9f27a;color:#132a52;border-radius:12px;padding:13px;text-align:center;font:700 18px Roboto}
.nt{background:#fff;border-radius:22px;padding:14px 18px;font:500 18px/1.45 Roboto;box-shadow:0 14px 30px rgba(19,42,82,.08)}.nt b{color:#2a63d4}
""", "<div class=kk>IN-HOME PERSONAL TRAINER · BOOKINGS</div><h1>Sessions at their homes,<br><span>with drive time built in.</span></h1>",
f'''<div class=vw><div class=wk><small class=cap>YOUR WEEK · SAMPLE</small><div class=gw><div class=hrs>{hours}</div>{grid}</div>
<div class=lg3><span><i></i>Session</span><span><i class=d></i>Drive</span><span><i class=o></i>Open slot</span></div></div>
<div class=rc><div class=bk><small>NEW BOOKING · SAMPLE</small>{"".join(f'<div class=br><span>{a}</span><b>{b}</b></div>' for a,b in [("Client","New client G"),("Area","Same ZIP as Client C"),("Slot","Thu 11 AM · 1 hour"),("Notes","Your own session notes")])}<div class=bb>Confirm Thu 11 AM</div></div>
<div class=nt>Only slots with time to drive there <b>show up on the booking page</b>.</div></div></div>''',
"#132a52", "Train clients at home? DM us", "background:#2a63d4;color:#fff")

# ───────── 268 INDIA · Mushroom grower · SINGLE · DM Sans + Source Sans 3 · mushroom beige / forest / clay
# New technique: grow room racks drawn as shelves of bags, each bag coloured by its stage, with harvest dates under each rack.
racks = [("Rack 1", ["h"]*8, "Harvest today"), ("Rack 2", ["p"]*8, "Pins out · harvest Thu 26"), ("Rack 3", ["w"]*6 + ["r"]*2, "Spreading · harvest Wed 2 Dec"), ("Rack 4", ["n"]*8, "Filled Mon 23 · harvest Mon 7 Dec")]
stage = {"h": ("#c46a3c", "Ready"), "p": ("#e7a97a", "Pins"), "w": ("#f3efe6", "Spreading"), "r": ("#9b2d20", "Check"), "n": ("#d9cfbf", "New")}
def bag(k):
    c = stage[k][0]
    caps = '<i class=mc></i><i class=mc2></i>' if k in "hp" else ""
    return f'<div class="bg2 {k}" style="background:{c}">{caps}</div>'
P["p268_mushroom"] = page("""
body{--f:'Source Sans 3';--h:'DM Sans';background:#f2ede4;color:#26382b}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#b4552c;margin-top:22px}
h1{font-family:'DM Sans';font-weight:800;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#3f6b48}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.rm{flex:1;min-height:0;background:#26382b;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;gap:10px}
.rm>small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#b9d4bd}
.rk{flex:1;display:grid;grid-template-columns:110px 1fr 300px;gap:16px;align-items:center}
.rk>b{font:700 24px/1.3 'DM Sans';color:#fff}
.sh{display:flex;gap:8px;align-items:flex-end;border-bottom:8px solid #8a6b47;padding:0 8px;height:100%;max-height:130px}
.bg2{flex:1;height:110px;border-radius:12px 12px 6px 6px;position:relative;box-shadow:inset 0 -8px 0 rgba(0,0,0,.12)}
.mc,.mc2{position:absolute;width:22px;height:14px;border-radius:12px 12px 4px 4px;background:#f6e7d2;top:4px;left:8px;border:2px solid #7d4a2c}.mc2{left:auto;right:8px;top:6px;width:18px;height:12px}
.bg2.p .mc,.bg2.p .mc2{width:12px;height:9px}
.rk>span{font:600 19px/1.35 'Source Sans 3';color:#dfe9e0}
.rk.t>span{color:#ffd0b5;font-weight:700}
.bt{display:flex;gap:14px}
.lgd{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;gap:14px;align-items:center;flex-wrap:wrap;box-shadow:0 14px 30px rgba(38,56,43,.08)}
.lgd span{display:flex;align-items:center;gap:8px;font:600 18px 'Source Sans 3'}.lgd i{width:24px;height:24px;border-radius:6px}
.by{width:420px;flex:none;background:#b4552c;color:#fff;border-radius:22px;padding:14px 20px;font:500 19px/1.45 'Source Sans 3'}.by b{font-weight:700}
""", "<div class=kk>MUSHROOM GROWING UNIT · HARVEST PLAN</div><h1>Which rack is ready?<br><span>Buyers know before you call.</span></h1>",
f'''<div class=vw><div class=rm><small>GROW ROOM 1 · BAGS BY STAGE · SAMPLE</small>{"".join(f'<div class="rk{" t" if i==0 else ""}"><b>{r}</b><div class=sh>{"".join(bag(k) for k in bs)}</div><span>{t}</span></div>' for i,(r,bs,t) in enumerate(racks))}</div>
<div class=bt><div class=lgd>{"".join(f'<span><i style="background:{c}"></i>{n}</span>' for c,n in stage.values())}</div>
<div class=by><b>Rack 1 today:</b> orders from 3 buyers are already matched, sample.</div></div></div>''',
"#26382b", "Grow mushrooms? DM us", "background:#3f6b48;color:#fff")

# ───────── 269 CANADA · Maple syrup farm stand · CAROUSEL 5 · Lora + Roboto · maple red / syrup amber / birch white
# New technique: pickup slip with zigzag (torn) edges via clip-path, drawn syrup bottles by size, Saturday pickup slot board.
def bottle(h=150, c="#b8641a", lbl=""):
    return f'<div class=bt9 style="height:{h}px"><i class=nk></i><div class=bd9 style="background:linear-gradient(transparent 0 18%,{c} 18%)">{f"<span>{lbl}</span>" if lbl else ""}</div></div>'
MP = """
body{--f:'Roboto';--h:'Lora';background:#f7f2ea;color:#3b1a12}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#b3261e;margin-top:22px;align-self:flex-start}
h1{font-family:'Lora';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b3261e}
.bt9{display:flex;flex-direction:column;align-items:center;flex:none;width:130px}.nk{width:26%;height:16%;background:#f2e8d8;border:3px solid #3b1a12;border-bottom:0;border-radius:6px 6px 0 0}
.bd9{flex:1;width:100%;border:3px solid #3b1a12;border-radius:16px 16px 12px 12px;display:flex;align-items:center;justify-content:center;background-color:#fffaf2}
.bd9 span{background:#fff;border-radius:8px;padding:4px 8px;font:700 16px Roboto;color:#3b1a12}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(59,26,18,.08)}
.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#857166}
.nb{display:flex;align-items:center;gap:14px;background:#3b1a12;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Roboto'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#b3261e}.nb b{color:#f3c27a}
"""
def mp(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3b1a12;color:#fff"):
    return page(MP + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3b1a12", cta, ctacss, tagline=f"{n} / 5")
P["p269_maple_s1"] = mp(1, "MAPLE SYRUP FARM STAND · PRE-ORDERS", "Sold out by 10 AM?<br><span>Let people pre-order.</span>",
f'''<div class=w1><div class="cd sh1"><small class=cap>SATURDAY AT THE STAND · SAMPLE</small><div class=bl>{"".join(bottle(h,c,l) for h,c,l in [(300,"#c9831f","1 L"),(230,"#b8641a","500 ml"),(170,"#8f3f12","250 ml")])}</div><div class=so>SOLD OUT</div></div>
<div class=q3>{"".join(f'<div class=qx><b>{a}</b><span>{b}</span></div>' for a,b in [("Drove 30 min","and found the shelf empty"),("Regulars","asked you to hold a bottle"),("A paper list","at the stand, in pencil")])}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sh1{flex:1;padding:18px 24px;display:flex;flex-direction:column;position:relative}
.bl .bt9{width:160px}.bl{flex:1;display:flex;gap:60px;align-items:flex-end;justify-content:center;border-bottom:10px solid #8a5a34;padding-bottom:0;opacity:.35}
.so{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);font:800 64px/1.3 Lora;color:#b3261e;border:6px solid #b3261e;border-radius:16px;padding:6px 26px;background:rgba(255,255,255,.85)}
.q3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.qx{background:#fff;border-radius:20px;padding:16px 20px;border-top:6px solid #b3261e}.qx b{display:block;font:700 30px/1.3 Lora}.qx span{font:500 18px Roboto;color:#6d5a50}""")

sizes = [("1 L glass", 2), ("500 ml glass", 1), ("250 ml gift", 3)]
P["p269_maple_s2"] = mp(2, "STEP 1 · ORDER BY SIZE, ONLINE", "Pick the size,<br><span>pick the Saturday.</span>",
f'''<div class=w2>{"".join(f'<div class="cd sz"><div class=bw>{bottle(h,c)}</div><b>{n}</b><div class=st><em>−</em><strong>{q}</strong><em>+</em></div></div>' for (n,q),(h,c) in zip(sizes,[(430,"#c9831f"),(350,"#b8641a"),(270,"#8f3f12")]))}</div>
<div class=nb><span class=ib>{ic("cal",26)}</span><span>Pickup on <b>Sat 5 Dec</b> · stock is held for each order, sample.</span></div>''',
css=""".w2{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;min-height:0;margin-bottom:14px}
.sz{padding:18px;display:flex;flex-direction:column;align-items:center;gap:14px}.bw{flex:1;display:flex;align-items:flex-end;justify-content:center}.bw .bt9{width:180px}
.sz b{font:700 30px/1.3 Lora}.st{display:flex;align-items:center;gap:14px}.st em{width:52px;height:52px;border-radius:14px;background:#f7f2ea;font:700 28px/52px Roboto;font-style:normal;text-align:center}.st strong{font:800 34px Roboto;width:40px;text-align:center}
.vis{flex-direction:column}""")

slots = [("9:00", 4, 4), ("9:30", 4, 3), ("10:00", 4, 4), ("10:30", 4, 2), ("11:00", 4, 1), ("11:30", 4, 0)]
P["p269_maple_s3"] = mp(3, "STEP 2 · SATURDAY PICKUP SLOTS", "No line at the stand.<br><span>Everyone has a time.</span>",
f'''<div class=w3><div class="cd sb"><small class=cap>SAT 5 DEC · 4 PICKUPS PER HALF HOUR · SAMPLE</small>{"".join(f'<div class=sr><b>{t}</b><div class=dots>{"".join("<i class=f></i>" for _ in range(u))}{"".join("<i></i>" for _ in range(c-u))}</div><span>{"Full" if u==c else f"{c-u} open"}</span></div>' for t,c,u in slots)}</div>
<div class=nb><span class=ib>{ic("clock",26)}</span><span>Full slots close on the order page. <b>14 of 24 pickups booked.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sb{flex:1;padding:16px 26px;display:flex;flex-direction:column}
.sr{flex:1;display:grid;grid-template-columns:130px 1fr 130px;gap:16px;align-items:center;border-top:1px solid #f0e8dc}.sr b{font:700 34px/1.3 Lora}
.dots{display:flex;gap:14px}.dots i{width:56px;height:56px;border-radius:50%;border:4px dashed #d9c9b6}.dots i.f{background:#b8641a;border:4px solid #8f3f12}
.sr span{font:700 20px Roboto;text-align:right;color:#3f7a3a}""")

random.seed(269)
def _q(r,c):
    for (R0,C0) in [(0,0),(0,8),(8,0)]:
        if R0<=r<R0+3 and C0<=c<C0+3: return True
    if (r,c) in [(1,1),(1,9),(9,1)]: return False
    if any(R0<=r<R0+3 and C0<=c<C0+3 for R0,C0 in [(0,0),(0,8),(8,0)]): return True
    return random.random()<.45 and not (r<4 and c<4) and not (r<4 and c>6) and not (r>6 and c<4)
QR="".join(f'<i style="background:{"#3b1a12" if _q(r,c) else "transparent"}"></i>' for r in range(11) for c in range(11))
P["p269_maple_s4"] = mp(4, "STEP 3 · THE PICKUP SLIP", "Show the slip,<br><span>take your bottles.</span>",
f'''<div class=w4><div class=slip><div class=sl1><b>Sample Maple Farm</b><span>Pickup slip · order M-269</span></div>
<div class=sl2><span>Name</span><b>Sample customer</b></div><div class=sl2><span>Pickup</span><b>Sat 5 Dec · 10:30</b></div>
{"".join(f'<div class=sl3><span>{q} ×</span><b>{n}</b><em>Held</em></div>' for n,q in sizes)}
<div class=sl4><span>Paid</span><b>Online, before pickup</b></div><div class=qrb>{QR}</div></div>
<div class=sd>{"".join(f'<div class="cd sx"><span class=ib>{ic(i,28)}</span><b>{a}</b><span>{b}</span></div>' for i,a,b in [("send","Sent by text","The day before"),("qr","Scan at the stand","Marks it picked up"),("box","Bottles held","Packed before 9 AM")])}</div></div>''',
css=""".w4{flex:1;display:flex;gap:18px;min-height:0}
.slip{flex:1;min-width:0;background:#fffdf7;padding:34px 30px;display:flex;flex-direction:column;gap:6px;clip-path:polygon(0 12px,3% 0,6% 12px,9% 0,12% 12px,15% 0,18% 12px,21% 0,24% 12px,27% 0,30% 12px,33% 0,36% 12px,39% 0,42% 12px,45% 0,48% 12px,51% 0,54% 12px,57% 0,60% 12px,63% 0,66% 12px,69% 0,72% 12px,75% 0,78% 12px,81% 0,84% 12px,87% 0,90% 12px,93% 0,96% 12px,100% 0,100% calc(100% - 12px),96% 100%,93% calc(100% - 12px),90% 100%,87% calc(100% - 12px),84% 100%,81% calc(100% - 12px),78% 100%,75% calc(100% - 12px),72% 100%,69% calc(100% - 12px),66% 100%,63% calc(100% - 12px),60% 100%,57% calc(100% - 12px),54% 100%,51% calc(100% - 12px),48% 100%,45% calc(100% - 12px),42% 100%,39% calc(100% - 12px),36% 100%,33% calc(100% - 12px),30% 100%,27% calc(100% - 12px),24% 100%,21% calc(100% - 12px),18% 100%,15% calc(100% - 12px),12% 100%,9% calc(100% - 12px),6% 100%,3% calc(100% - 12px),0 100%);filter:drop-shadow(0 10px 20px rgba(59,26,18,.15))}
.sl1{text-align:center;border-bottom:2px dashed #3b1a12;padding-bottom:12px}.sl1 b{display:block;font:700 32px/1.3 Lora}.sl1 span{font:500 18px 'Roboto';color:#857166}
.sl2,.sl4{display:flex;justify-content:space-between;align-items:center;flex:1;font:500 20px Roboto;color:#6d5a50;border-bottom:1px dashed #e1d6c8}.sl2 b,.sl4 b{color:#3b1a12;font-weight:700}
.sl3{flex:1;display:grid;grid-template-columns:50px 1fr auto;gap:10px;align-items:center;font:500 20px Roboto;border-bottom:1px dashed #e1d6c8}.sl3 b{font:700 24px Lora}.sl3 em{font-style:normal;font-weight:700;font-size:16px;color:#3f7a3a;background:#e6f2e4;padding:5px 10px;border-radius:8px}
.qrb{align-self:center;margin-top:10px;width:130px;height:130px;display:grid;grid-template-columns:repeat(11,1fr);gap:1px;padding:8px;background:#fff;border:2px solid #e1d6c8;border-radius:8px}
.sd{width:300px;flex:none;display:flex;flex-direction:column;gap:12px}.sx{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.sx .ib{width:56px;height:56px;border-radius:16px;background:#fbe3d8;color:#b3261e}.sx b{font:700 30px/1.3 Lora}.sx>span:last-child{font:500 19px Roboto;color:#6d5a50}""")

P["p269_maple_s5"] = mp(5, "YOUR TURN", "Sell syrup at a farm stand?<br><span>Let's build your pre-orders.</span>",
f'''<div class=w5><div class="cd hp">{"".join(bottle(h,c,l) for h,c,l in [(290,"#c9831f","1 L"),(230,"#b8641a","500 ml"),(170,"#8f3f12","250 ml")])}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("cart","Pre-order page","By bottle size"),("clock","Pickup slots","No line on Saturday"),("doc","Pickup slip","Scan at the stand"),("box","Stock held","Never sold twice")])}</div>
<div class=q>Do your customers ever find the stand sold out? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b3261e;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;justify-content:center;align-items:flex-end;gap:60px;padding:24px;border-bottom:10px solid #8a5a34}.hp .bt9{width:130px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(59,26,18,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#fbe3d8;color:#b3261e}.ti b{display:block;font:700 30px/1.35 Lora}.ti div span{font:500 19px/1.35 Roboto;color:#6d5a50}
.q{background:#3b1a12;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Roboto}""")

# ───────── 270 INDIA · Sign board painter / maker · SINGLE · Poppins + Gelasio · board yellow / black / signal blue
# New technique: a big shop sign proof with red-ring spelling marks and measured size, next to a job sheet and approval state.
P["p270_signboard"] = page("""
body{--f:'Poppins';--h:'Gelasio';background:#eef1f6;color:#151515}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#1f5bd1;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#1f5bd1}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pf{background:#fff;border-radius:26px;padding:16px 22px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(21,21,21,.08)}
.cap{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#6d7380}
.sgw{position:relative;padding:34px 56px 40px 0}
.sg{background:#ffd21f;border:10px solid #151515;border-radius:8px;padding:22px 30px;text-align:center;position:relative}
.sg{padding:44px 30px!important}.sg b{display:block;font:800 56px/1.35 Poppins;letter-spacing:1px}.sg span{display:block;font:600 28px/1.4 Poppins;margin-top:22px}.rw{text-decoration:none;outline:5px solid #e0302b;outline-offset:6px;border-radius:30px;position:relative;padding:0 8px}.rw:after{content:attr(data-n);position:absolute;right:-26px;top:-26px;width:34px;height:34px;border-radius:50%;background:#e0302b;color:#fff;font:700 18px/34px Poppins;text-align:center}
.rg{position:absolute;border:5px solid #e0302b;border-radius:50%}
.tg{position:absolute;background:#e0302b;color:#fff;font:600 16px Poppins;padding:6px 10px;border-radius:10px;white-space:nowrap}
.dmw{position:absolute;left:0;right:56px;bottom:0;height:26px;border-left:3px solid #151515;border-right:3px solid #151515;display:flex;align-items:center;justify-content:center}
.dmw:before{content:"";position:absolute;left:0;right:0;top:50%;border-top:3px solid #151515}.dmw em{position:relative;background:#fff;padding:0 10px;font:700 18px Poppins;font-style:normal}
.dmh{position:absolute;right:0;top:34px;bottom:40px;width:30px;border-top:3px solid #151515;border-bottom:3px solid #151515;display:flex;align-items:center;justify-content:center}
.dmh:before{content:"";position:absolute;top:0;bottom:0;left:50%;border-left:3px solid #151515}.dmh em{position:relative;background:#fff;padding:6px 0;font:700 18px Poppins;font-style:normal;writing-mode:vertical-rl}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.js{flex:1;min-width:0;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(21,21,21,.08)}
.jr{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #edf0f4;font:500 19px Poppins;color:#5b616d}.jr b{color:#151515;font-weight:700}
.ap{width:340px;flex:none;display:flex;flex-direction:column;gap:12px}
.st{flex:1;border-radius:22px;padding:14px 18px;display:flex;gap:14px;align-items:center}
.st i{width:44px;height:44px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font:700 18px Poppins;font-style:normal}
.st b{display:block;font:700 22px/1.3 Gelasio}.st span{font:500 16px Poppins}
.st.d{background:#fff;box-shadow:0 14px 30px rgba(21,21,21,.08)}.st.d i{background:#2f9e5b;color:#fff}.st.d span{color:#5b616d}
.st.n{background:#151515;color:#fff}.st.n i{background:#ffd21f;color:#151515}.st.n span{color:#c9ccd2}
""", "<div class=kk>SIGN BOARD MAKER · PROOF APPROVAL</div><h1>Catch the spelling mistake<br><span>before the paint dries.</span></h1>",
f'''<div class=vw><div class=pf><small class=cap>PROOF 2 · JOB SB-270 · SAMPLE SHOP · 1 SPELLING FIXED · 2 LINE ADDED</small><div class=sgw><div class=sg><b>SAMPLE <u class=rw data-n="1">GENERAL</u> STORE</b><span><u class=rw data-n="2">Groceries · Daily needs · Home delivery</u></span></div>
<div class=dmw><em>8 ft</em></div><div class=dmh><em>3 ft</em></div></div></div>
<div class=bt><div class=js><small class=cap>JOB SHEET</small>{"".join(f'<div class=jr><span>{a}</span><b>{b}</b></div>' for a,b in [("Board","Flex on metal frame"),("Size","8 × 3 ft"),("Colours","Yellow, black"),("Fitting","Mon 30 Nov · 10 AM")])}</div>
<div class=ap><div class="st d"><i>✓</i><div><b>Proof 1 · changes</b><span>2 notes from the customer</span></div></div><div class="st n"><i>2</i><div><b>Proof 2 · approved</b><span>Sent to print with one tap</span></div></div></div></div></div>''',
"#151515", "Make sign boards? DM us", "background:#1f5bd1;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
