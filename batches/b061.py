import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 321 INDIA · Sleeper bus operator · CAROUSEL 5 · Poppins + Source Sans 3 · sleeper maroon / berth cream / route blue
# New technique: top-down sleeper bus decks (2+1 berths, lower and upper) as a live seat chart, reused across slides.
SB = """
body{--f:'Source Sans 3';--h:'Poppins';background:#f5eee6;color:#3a1420}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#2b5fa8;margin-top:22px;align-self:flex-start}
h1{font-family:'Poppins';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#8a1f37}
.cd{background:#fffaf4;border-radius:22px;box-shadow:0 12px 28px rgba(58,20,32,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7d6a6e}
.nb{display:flex;align-items:center;gap:14px;background:#3a1420;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 'Source Sans 3'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#f2c14e;color:#3a1420}.nb b{color:#f6d27a}
.dks{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.dk{background:#e6dbd0;border-radius:28px 28px 18px 18px;padding:14px 14px 16px;display:flex;flex-direction:column;gap:8px;box-shadow:inset 0 0 0 5px #d3c4b6}
.dk>b{font:700 17px/1.4 Poppins;text-align:center;color:#5a3a44}
.bs{flex:1;display:grid;grid-template-columns:1fr 1fr 20px 1fr;grid-template-rows:repeat(5,1fr);gap:8px}
.bt{border-radius:10px;display:flex;align-items:center;justify-content:center;font:700 17px 'Source Sans 3';border:2.5px solid transparent}
.bt.f{background:#fffaf4;border-color:#c9b6a6;color:#7d6a6e}.bt.b{background:#8a1f37;color:#fff}.bt.x{background:#e5484d;color:#fff;box-shadow:0 0 0 4px #ffd0d2}.bt.h{background:#f2c14e;color:#3a1420}
.ai{grid-column:3;grid-row:1 / 6;border-left:2px dashed #c9b6a6}
.lgx{display:flex;flex-wrap:wrap;gap:16px;font:600 16px/1.4 'Source Sans 3'}.lgx span{display:flex;align-items:center;gap:8px}.lgx i{width:20px;height:20px;border-radius:5px}
"""
def sb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3a1420;color:#f6d27a"):
    return page(SB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3a1420", cta, ctacss, tagline=f"{n} / 5")
def deck(name, pre, st):
    cells = ""
    for r in range(5):
        for c, col in enumerate((1, 2, 4)):
            k = f"{pre}{r*3+c+1}"
            cells += f'<div class="bt {st.get(k,"f")}" style="grid-column:{col};grid-row:{r+1}">{k}</div>'
    return f'<div class=dk><b>{name}</b><div class=bs><i class=ai></i>{cells}</div></div>'
S1 = {f"L{i}": "b" for i in [1, 2, 4, 5, 7, 9, 10, 13]} | {f"U{i}": "b" for i in [1, 3, 5, 6, 8, 11, 12, 15]} | {"U4": "x"}
LG = lambda items: '<div class=lgx>' + "".join(f'<span><i style="{s}"></i>{a}</span>' for a, s in items) + '</div>'
P["p321_bus_s1"] = sb(1, "SLEEPER BUS OPERATOR · NIGHT ROUTE", "Seat chart on paper?<br><span>One berth, two passengers.</span>",
f'''<div class=w1><div class="cd c1"><small class=cap>TONIGHT · CITY A TO CITY B · 9:30 PM · SAMPLE</small><div class=dks>{deck("LOWER DECK","L",S1)}{deck("UPPER DECK","U",S1)}</div>
{LG([("Booked","background:#8a1f37"),("Free","background:#fffaf4;border:2.5px solid #c9b6a6"),("Booked twice","background:#e5484d")])}</div>
<div class=bb1><span class=vn>{ic("phone",22)} Agent, 8:50 PM</span><p>“I also sold U4. My passenger is already at the bus stand.”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c1{flex:1;min-height:0;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.bb1{background:#3a1420;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px 'Source Sans 3';color:#f6d27a;margin-bottom:6px}.bb1 p{font:500 23px/1.4 'Source Sans 3'}""")

S2 = {f"L{i}": "b" for i in [1, 2, 3, 4, 5, 7, 9, 10, 12, 13, 14]} | {f"U{i}": "b" for i in [1, 2, 3, 5, 6, 8, 9, 11, 12, 15]} | {"U4": "h", "L8": "h"}
nb_ = sum(1 for v in S2.values() if v == "b"); nh = sum(1 for v in S2.values() if v == "h"); nf = 30 - nb_ - nh
P["p321_bus_s2"] = sb(2, "STEP 1 · ONE LIVE CHART FOR OFFICE AND AGENTS", "Agents book online.<br><span>A sold berth is gone.</span>",
f'''<div class=w2><div class="cd c2"><div class=dks>{deck("LOWER DECK","L",S2)}{deck("UPPER DECK","U",S2)}</div>
{LG([("Booked "+str(nb_),"background:#8a1f37"),("On hold 10 min "+str(nh),"background:#f2c14e"),("Free "+str(nf),"background:#fffaf4;border:2.5px solid #c9b6a6")])}</div>
<div class=nb><span class=ib>{ic("users",26)}</span><span>Every agent sees the same chart. <b>A berth on hold cannot be sold twice.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c2{flex:1;min-height:0;padding:16px 20px;display:flex;flex-direction:column;gap:10px}""")

points = [("8:45 PM", "Point 1 · Main bus stand", ["L1", "L2", "L3", "U1", "U2", "U3", "U5", "U6"]), ("9:05 PM", "Point 2 · Ring road", ["L4", "L5", "L7", "U8", "U9"]),
          ("9:20 PM", "Point 3 · Highway petrol pump", ["L9", "L10", "L12", "U11", "U12"]), ("9:30 PM", "Point 4 · Toll gate", ["L13", "L14", "U15"])]
P["p321_bus_s3"] = sb(3, "STEP 2 · BOARDING POINTS WITH NAMES", "Who boards where?<br><span>The conductor knows.</span>",
f'''<div class=w3><div class="cd rt3">{"".join(f'<div class=pt3><span class=tm3>{t}</span><i class=dt3></i><div class=pd3><b>{p}</b><div class=ch3>{"".join(f"<em>{b}</em>" for b in bs)}</div></div><strong>{len(bs)}</strong></div>' for t,p,bs in points)}</div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>Each passenger gets the bus number and boarding time <b>at 7 PM, by message.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rt3{flex:1;padding:16px 24px;display:flex;flex-direction:column}
.pt3{flex:1;display:grid;grid-template-columns:110px 36px 1fr 70px;gap:14px;align-items:center;position:relative}.pt3::before{content:"";position:absolute;left:141px;top:0;bottom:0;width:4px;background:#d9c6c9}
.tm3{font:800 20px/1.3 Poppins;color:#2b5fa8}.dt3{width:28px;height:28px;border-radius:50%;background:#fff;border:5px solid #8a1f37;position:relative;z-index:1;justify-self:center}
.pd3 b{display:block;font:700 23px/1.35 'Source Sans 3';margin-bottom:8px}.ch3{display:flex;flex-wrap:wrap;gap:6px}.ch3 em{font:700 16px 'Source Sans 3';font-style:normal;background:#8a1f37;color:#fff;border-radius:8px;padding:3px 10px}
.pt3 strong{font:800 40px/1.3 Poppins;color:#8a1f37;text-align:right}""")

rows = [("L1", "Passenger 1", "Point 1", "98xxxxxx21", "y"), ("L4", "Passenger 9", "Point 2", "97xxxxxx45", "y"), ("L9", "Passenger 14", "Point 3", "99xxxxxx08", "n"), ("U11", "Passenger 17", "Point 3", "90xxxxxx63", "n"), ("U15", "Passenger 21", "Point 4", "88xxxxxx12", "n")]
P["p321_bus_s4"] = sb(4, "STEP 3 · CONDUCTOR'S LIST ON THE PHONE", "Tick them in.<br><span>Leave on time.</span>",
f'''<div class=w4><div class="cd tb4"><div class="rw4 hd4"><span>BERTH</span><span>NAME · SAMPLE</span><span>BOARDS AT</span><span>MOBILE</span><span>IN</span></div>
{"".join(f'<div class=rw4><b>{a}</b><span>{n}</span><span>{p}</span><span class=mb4>{m}</span><i class={k}>{ic("check",18) if k=="y" else ""}</i></div>' for a,n,p,m,k in rows)}
<div class=ft4><span>On board <b>{sum(1 for r in rows if r[4]=="y")}</b> of {len(rows)} shown</span><span>Not boarded by 9:35 PM? <b>One tap calls them.</b></span></div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;min-height:0}.tb4{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.rw4{flex:1;display:grid;grid-template-columns:80px 1.3fr 1fr 1.1fr 50px;gap:12px;align-items:center;border-bottom:1px solid #eee2d8}
.hd4{flex:none;padding:6px 0 12px;border-bottom:2px solid #3a1420;font:700 14px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#7d6a6e}
.rw4 b{font:800 24px Poppins;color:#8a1f37}.rw4>span{font:600 20px 'Source Sans 3'}.mb4{color:#7d6a6e;font-weight:500!important}
.rw4 i{width:40px;height:40px;border-radius:10px;border:3px solid #c9b6a6;display:flex;align-items:center;justify-content:center;color:#fff}.rw4 i.y{background:#2f8a5b;border-color:#2f8a5b}
.ft4{display:flex;justify-content:space-between;background:#3a1420;color:#fff;border-radius:14px;padding:14px 18px;margin-top:10px;font:500 19px 'Source Sans 3'}.ft4 b{color:#f6d27a}""")

P["p321_bus_s5"] = sb(5, "YOUR TURN", "Run buses or a travel office?<br><span>Let's build your seat chart.</span>",
f'''<div class=w5><div class="cd c5"><div class=dks>{deck("LOWER DECK","L",S2)}{deck("UPPER DECK","U",S2)}</div></div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,34)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Live chart","For office and agents"),("pin","Boarding points","Names and times"),("check","Conductor list","Tick on board"),("bell","Messages","Bus number at 7 PM")])}</div>
<div class=q>How do your agents book berths today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#8a1f37;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1.15fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{padding:14px;display:flex;min-height:0}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fffaf4;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(58,20,32,.07)}
.ti .ib{width:60px;height:60px;border-radius:18px;background:#f7e3c4;color:#8a1f37}.ti b{display:block;font:700 22px/1.45 Poppins;margin-bottom:3px}.ti div span{font:500 17px/1.4 'Source Sans 3';color:#6b585c}
.q{background:#3a1420;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'Source Sans 3'}""")

# ───────── 322 INDIA · LED bulb assembly unit · SINGLE · Archivo Black + Fira Sans · bulb warm white / circuit green / charcoal
# New technique: SVG bulbs on a test rack, glowing (radial halo) when passed, grey with a cross when failed.
random.seed(322)
fails = {7, 26}
def bulb(ok):
    halo = '<circle cx="40" cy="38" r="36" fill="url(#hl)"/>' if ok else ""
    glass = "#fff6c8" if ok else "#c9ccd1"
    x = "" if ok else '<path d="M28 26 L52 50 M52 26 L28 50" stroke="#d1462f" stroke-width="5" stroke-linecap="round"/>'
    return f'''<svg viewBox="0 0 80 100" class=bl2>{halo}<circle cx="40" cy="38" r="24" fill="{glass}" stroke="{"#f2c14e" if ok else "#9aa0a8"}" stroke-width="3"/>{x}
<rect x="30" y="60" width="20" height="8" rx="2" fill="#8a9099"/><rect x="31" y="69" width="18" height="6" rx="2" fill="#6e747c"/><rect x="33" y="76" width="14" height="8" rx="3" fill="#3b4048"/></svg>'''
DEF = '<svg width="0" height="0" style="position:absolute"><defs><radialGradient id="hl"><stop offset=".5" stop-color="#ffe57a" stop-opacity=".9"/><stop offset="1" stop-color="#ffe57a" stop-opacity="0"/></radialGradient></defs></svg>'
trays, per = 30, 40
failed_day = 36
P["p322_led"] = page("""
body{--f:'Fira Sans';--h:'Archivo Black';background:#eef1ec;color:#22262b}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#2e7d4f;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:60px;letter-spacing:-1px;line-height:1.25;margin-top:30px} h1 span{color:#2e7d4f}
.vw{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}
.rk{flex:1;min-height:0;background:#22262b;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;position:relative}
.rk>small{font:700 13px/1.5 'Fira Sans';letter-spacing:2px;color:#b9e3c6}
.gd2{flex:1;min-height:0;display:grid;grid-template-columns:repeat(8,1fr);grid-template-rows:repeat(5,1fr);gap:4px;background:repeating-linear-gradient(0deg,#2a3036 0 2px,transparent 2px 100%);}
.bl2{width:100%;height:100%;display:block}
.tl{display:flex;justify-content:space-between;font:600 16px/1.4 'Fira Sans';color:#d6dadf}.tl b{color:#ffe57a}
.st{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.sc{background:#fff;border-radius:20px;padding:12px 18px;display:flex;align-items:center;gap:14px;box-shadow:0 12px 26px rgba(34,38,43,.07)}
.sc b{font:400 40px/1.3 'Archivo Black'}.sc span{font:600 16px/1.35 'Fira Sans';color:#555b63}
.ms{background:#2e7d4f;color:#fff;border-radius:20px;padding:14px 20px;font:500 19px/1.45 'Fira Sans'}.ms b{color:#ffe57a}
""", "<div class=kk>LED BULB ASSEMBLY UNIT · TESTING</div><h1>Which bulbs failed?<br><span>Count them as you test.</span></h1>",
f'''{DEF}<div class=vw><div class=rk><small>TEST RACK · TRAY T-17 · 9 W BULBS · SAMPLE</small><div class=gd2>{"".join(bulb(i not in fails) for i in range(per))}</div>
<div class=tl><span>Tray T-17: <b>{per-len(fails)} passed</b>, {len(fails)} failed</span><span>Failed bulbs go to the repair bench, not the box.</span></div></div>
<div class=st>{"".join(f'<div class=sc><b style="color:{c}">{v}</b><span>{a}</span></div>' for v,a,c in [(f"{trays*per:,}","bulbs tested today","#22262b"),(f"{trays*per-failed_day:,}","passed, packed","#2e7d4f"),(str(failed_day),"to the repair bench","#d1462f")])}</div>
<div class=ms>Shop order S-22 needs 600 bulbs by Friday. <b>{trays*per-failed_day:,} passed today, so it can go tomorrow.</b></div></div>''',
"#22262b", "Make LED lights? DM us", "background:#22262b;color:#ffe57a")

# ───────── 323 USA · Custom cookie decorator · SINGLE · Lora + DM Sans · icing pink / cocoa / mint · PHONE
# New technique: CSS decorated cookies (circle, heart, star via clip-path) with icing flood + piped dot borders, previewing the order.
def cookie(shape, ic_, txt="", s=120):
    clip = {"c": "circle(50%)", "h": "path('M60 108 C20 80 0 58 0 34 C0 14 16 0 34 0 C46 0 55 6 60 16 C65 6 74 0 86 0 C104 0 120 14 120 34 C120 58 100 80 60 108 Z')",
            "s": "polygon(50% 0,61% 35%,98% 35%,68% 57%,79% 91%,50% 70%,21% 91%,32% 57%,2% 35%,39% 35%)"}[shape]
    return f'''<div class=ck style="width:{s}px;height:{s}px"><div class=cb style="clip-path:{clip}"></div><div class=ci style="clip-path:{clip};background:{ic_}"></div><span>{txt}</span></div>'''
order = [("c", "#f7b6c8", "30"), ("h", "#f9d9e3", ""), ("s", "#bfe8d9", ""), ("c", "#bfe8d9", "30"), ("h", "#f7b6c8", ""), ("s", "#fff3c4", ""),
         ("c", "#fff3c4", "30"), ("h", "#bfe8d9", ""), ("s", "#f7b6c8", ""), ("c", "#f9d9e3", "30"), ("h", "#fff3c4", ""), ("s", "#bfe8d9", "")]
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE COOKIE STUDIO</small><b>Order custom cookies</b><span>Order #C-212</span></div>
<div class=fl3><small>SHAPES</small><div class=ch3>{"".join(f'<span class=on>{a}</span>' for a in ["Round","Heart","Star"])}</div></div>
<div class=fl3><small>COLORS</small><div class=sw3>{"".join(f'<i style="background:{c}"></i>' for c in ["#f7b6c8","#bfe8d9","#fff3c4","#f9d9e3"])}</div></div>
<div class=fl3><small>QUANTITY</small><div class=tx3>1 dozen · 12 cookies</div></div>
<div class=fl3><small>TEXT ON ROUND COOKIES</small><div class=tx3>“30”</div></div>
<div class=fl3><small>PICKUP</small><div class=tx3>Sat 5 Dec · 11 AM</div></div>
<div class=fl3><small>DESIGN PROOF</small><div class=tx3>Sent by Wed · you approve</div></div>
<div class=bk3>Place order</div></div>''', 360, 840)
P["p323_cookies"] = page("""
body{--f:'DM Sans';--h:'Lora';background:#fbeff2;color:#4a2a22}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#2f8a6d;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:64px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#c2506e}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.tr{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(74,42,34,.08)}
.tr>small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#8a736c}
.pan{flex:1;min-height:0;background:repeating-linear-gradient(45deg,#e8e2dc 0 2px,#f4f0ec 2px 14px);border-radius:18px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(4,1fr);place-items:center;padding:12px}
.ck{position:relative;filter:drop-shadow(0 6px 6px rgba(74,42,34,.25))}.cb{position:absolute;inset:0;background:#c98b52}.ci{position:absolute;inset:7px;box-shadow:inset 0 0 0 4px rgba(255,255,255,.65)}
.ck span{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:700 40px/1 Lora;color:#4a2a22}
.ap{display:flex;flex-direction:column;gap:9px;padding:8px 18px 18px;flex:1;min-height:0}
.ah small{display:block;font:700 11px/1.4 'DM Sans';letter-spacing:2px;color:#8a736c}.ah b{display:block;font:700 23px/1.3 Lora}.ah span{font:500 14px/1.4 'DM Sans';color:#6d5650}
.fl3{background:#fbf3f5;border-radius:14px;padding:9px 12px}.fl3 small{display:block;font:700 11px/1.4 'DM Sans';letter-spacing:1.5px;color:#8a736c;margin-bottom:5px}
.ch3{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.ch3 span{border-radius:10px;padding:6px 0;text-align:center;font:600 14px 'DM Sans'}.ch3 .on{background:#4a2a22;color:#fff}
.sw3{display:flex;gap:10px}.sw3 i{width:34px;height:34px;border-radius:50%;box-shadow:inset 0 0 0 2px rgba(0,0,0,.1)}
.tx3{font:600 15px/1.4 'DM Sans'}.bk3{margin-top:auto;background:#c2506e;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 17px 'DM Sans'}
.nt{background:#4a2a22;color:#fff;border-radius:16px;padding:12px 16px;font:500 17px/1.45 'DM Sans'}.nt b{color:#bfe8d9}
""", "<div class=kk>CUSTOM COOKIE DECORATOR</div><h1>Orders by DM at midnight?<br><span>Let them build it.</span></h1>",
f'''<div class=vw><div class=tr><small>ORDER #C-212 · PREVIEW · SAMPLE</small><div class=pan>{"".join(cookie(s,c,t,118) for s,c,t in order)}</div>
<div class=nt>The order page shows this preview, <b>so the customer sees what they asked for.</b></div></div>{ph}</div>''',
"#4a2a22", "Bake custom cookies? DM us", "background:#4a2a22;color:#fff")

# ───────── 324 CANADA · Snowmobile tours and rentals · SINGLE · Bitter + Open Sans · snow white / sled red / spruce
# New technique: winter trail map (SVG loop with km ticks, warming hut, lake) + machine schedule ribbons by hour.
trail = '''<svg viewBox="0 0 520 820" class=tm><rect width="520" height="820" rx="22" fill="#f4f8fb"/><path d="M50 20 l16 34 h-32 z M50 36 l20 40 h-40 z" fill="#2f5d46"/><path d="M120 30 l16 34 h-32 z M120 46 l20 40 h-40 z" fill="#2f5d46"/><path d="M200 15 l16 34 h-32 z M200 31 l20 40 h-40 z" fill="#2f5d46"/><path d="M290 25 l16 34 h-32 z M290 41 l20 40 h-40 z" fill="#2f5d46"/><path d="M380 20 l16 34 h-32 z M380 36 l20 40 h-40 z" fill="#2f5d46"/><path d="M460 35 l16 34 h-32 z M460 51 l20 40 h-40 z" fill="#2f5d46"/><path d="M60 740 l16 34 h-32 z M60 756 l20 40 h-40 z" fill="#2f5d46"/><path d="M150 750 l16 34 h-32 z M150 766 l20 40 h-40 z" fill="#2f5d46"/><path d="M260 735 l16 34 h-32 z M260 751 l20 40 h-40 z" fill="#2f5d46"/><path d="M360 745 l16 34 h-32 z M360 761 l20 40 h-40 z" fill="#2f5d46"/><path d="M450 730 l16 34 h-32 z M450 746 l20 40 h-40 z" fill="#2f5d46"/><g transform="translate(0,110)">
<ellipse cx="330" cy="230" rx="120" ry="70" fill="#cfe3ef"/><text x="330" y="236" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="18" fill="#4d7690">Frozen lake</text>''' + \
"".join(f'<path d="M{x} {y} l16 34 h-32 z M{x} {y+16} l20 40 h-40 z" fill="#2f5d46"/>' for x, y in [(60, 60), (110, 40), (160, 70), (60, 420), (110, 450), (460, 420), (420, 470), (470, 90), (90, 260)]) + '''
<path d="M120 520 C60 420 80 300 170 240 S260 110 360 120 S480 220 440 340 S330 520 220 520 Z" fill="none" stroke="#d1332e" stroke-width="10" stroke-linecap="round" stroke-dasharray="1 0"/>
<path d="M120 520 C60 420 80 300 170 240 S260 110 360 120 S480 220 440 340 S330 520 220 520 Z" fill="none" stroke="#ffffff" stroke-width="3" stroke-dasharray="12 14"/>
<rect x="90" y="500" width="120" height="50" rx="10" fill="#1f3a2e"/><text x="150" y="532" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="17" fill="#fff">Base · start</text>
<rect x="390" y="320" width="120" height="50" rx="10" fill="#d1332e"/><text x="450" y="352" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="#fff">Warming hut</text>
<rect x="250" y="70" width="110" height="40" rx="10" fill="#ffffff" stroke="#1f3a2e" stroke-width="2"/><text x="305" y="96" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="#1f3a2e">Lookout</text></g></svg>'''
mach = [("Sled 1", [(9, 11, "Tour A"), (13, 15, "Tour B")]), ("Sled 2", [(9, 11, "Tour A"), (13, 15, "Tour B")]), ("Sled 3", [(9, 11, "Tour A"), (15.5, 17, "Rental")]),
        ("Sled 4", [(11.5, 13, "Rental"), (13, 15, "Tour B")]), ("Sled 5", [(10, 12, "Rental")]), ("Sled 6", [])]
H0, H1 = 9, 17
P["p324_snowmobile"] = page("""
body{--f:'Open Sans';--h:'Bitter';background:#e9f1f6;color:#1f3a2e}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#d1332e;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#d1332e}
.vw{flex:1;display:grid;grid-template-columns:440px 1fr;gap:14px;min-height:0}
.mp{background:#fff;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(31,58,46,.08)}
.mp>small,.sc4 small{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#6a7d75}
.tm{flex:1;min-height:0;width:100%;display:block}.mp p{font:600 16px/1.4 'Open Sans'}.mp p b{color:#d1332e}
.rt{display:flex;flex-direction:column;gap:12px;min-height:0}
.sc4{flex:1;background:#1f3a2e;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}.sc4 small{color:#bfe0cf}
.mr{flex:1;display:grid;grid-template-columns:76px 1fr;gap:10px;align-items:center}.mr b{font:800 18px Bitter;color:#fff}
.rb{position:relative;height:100%;min-height:48px;border-radius:10px;background:repeating-linear-gradient(90deg,#284a3b 0 calc(100%/8 - 2px),#31574a calc(100%/8 - 2px) calc(100%/8))}
.bk{position:absolute;top:6px;bottom:6px;border-radius:8px;display:flex;align-items:center;padding:0 8px;font:700 14px/1.3 'Open Sans';white-space:nowrap;overflow:hidden}
.ta{background:#d1332e;color:#fff}.tb{background:#f2c14e;color:#1f3a2e}.re{background:#ffffff;color:#1f3a2e}
.ax{position:relative;height:22px;margin-left:86px;font:600 13px/1.5 'Open Sans';color:#bfe0cf}.ax span{position:absolute;top:0}
.bf{background:#fff;border-radius:22px;padding:14px 18px;box-shadow:0 14px 30px rgba(31,58,46,.08)}
.bf small{display:block;font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#6a7d75;margin-bottom:4px}
.br{display:flex;justify-content:space-between;padding:5px 0;border-top:1px solid #e6eeea;font:600 16px/1.4 'Open Sans'}.br b{font-weight:700}
""", "<div class=kk>SNOWMOBILE TOURS AND RENTALS</div><h1>Six sleds, one Saturday.<br><span>No double bookings.</span></h1>",
f'''<div class=vw><div class=mp><small>TRAIL LOOP · SAMPLE</small>{trail}<p>Tour A and B ride this loop, <b>with a stop at the warming hut.</b></p></div>
<div class=rt><div class=sc4><small>SLEDS · SAT 9 JAN · 9 AM TO 5 PM · SAMPLE</small>{"".join(f'<div class=mr><b>{m}</b><div class=rb>{"".join(f"<span class='bk {dict(Tour_A=chr(116)+chr(97),Tour_B=chr(116)+chr(98),Rental=chr(114)+chr(101))[t.replace(chr(32),chr(95))]}' style=left:{(a-H0)/(H1-H0)*100:.1f}%;width:{(b-a)/(H1-H0)*100:.1f}%>{t}</span>" for a,b,t in bk)}</div></div>' for m,bk in mach)}
<div class=ax>{"".join(f'<span style="left:{(h-H0)/(H1-H0)*100:.1f}%">{l}</span>' for h,l in [(9,"9 AM"),(11,"11"),(13,"1 PM"),(15,"3"),(16.5,"4:30")])}</div></div>
<div class=bf><small>BOOKING · TOUR B · SAMPLE</small>{"".join(f'<div class=br><span>{a}</span><b>{b}</b></div>' for a,b in [("Riders","4 adults"),("Sleds","3 (one shared)"),("Helmet sizes","M, L, L, XL"),("Meet at base","12:30 PM")])}</div></div></div>''',
"#1f3a2e", "Rent sleds or run tours? DM us", "background:#d1332e;color:#fff")

# ───────── 325 INDIA · Music instrument rental and repair · CAROUSEL 5 · TeX Gyre Adventor + DM Sans · rosewood / brass / sky
# New technique: SVG instrument wall (guitars, keyboard, cajon, violin) with hanging rental tags; tags carry the due date.
IR = """
body{--f:'DM Sans';--h:'TeX Gyre Adventor';background:#eef4f8;color:#3a2218}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b07d2b;margin-top:22px;align-self:flex-start}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#2d7fb8}
.cd{background:#fff;border-radius:22px;box-shadow:0 12px 28px rgba(58,34,24,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7a6e68}
.nb{display:flex;align-items:center;gap:14px;background:#3a2218;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.45 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e8b65a;color:#3a2218}.nb b{color:#f3cf8a}
"""
def ir(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3a2218;color:#fff"):
    return page(IR + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3a2218", cta, ctacss, tagline=f"{n} / 5")
def guitar(c="#a0522d", w=120):
    return f'''<svg viewBox="0 0 120 330" width="{w}" class=ins><rect x="52" y="10" width="16" height="40" rx="4" fill="#3a2218"/><rect x="55" y="40" width="10" height="130" fill="#5a3a26"/>
<path d="M60 150 C20 150 18 190 34 210 C10 230 12 300 60 310 C108 300 110 230 86 210 C102 190 100 150 60 150 Z" fill="{c}"/><circle cx="60" cy="215" r="16" fill="#3a2218"/><rect x="44" y="270" width="32" height="8" rx="3" fill="#3a2218"/>
<path d="M57 50 V270 M63 50 V270" stroke="#e8e0d0" stroke-width="1.5"/></svg>'''
def violin(w=90):
    return f'''<svg viewBox="0 0 90 300" width="{w}" class=ins><rect x="40" y="8" width="10" height="90" fill="#3a2218"/><path d="M45 90 C15 90 15 130 28 145 C12 160 12 230 45 240 C78 230 78 160 62 145 C75 130 75 90 45 90 Z" fill="#b5651d"/>
<rect x="30" y="160" width="3" height="26" rx="1.5" fill="#3a2218"/><rect x="57" y="160" width="3" height="26" rx="1.5" fill="#3a2218"/><path d="M42 20 V236 M48 20 V236" stroke="#e8e0d0" stroke-width="1.2"/><rect x="36" y="222" width="18" height="14" rx="3" fill="#3a2218"/></svg>'''
def keyboard(w=360):
    keys = "".join(f'<rect x="{12+i*24}" y="40" width="22" height="70" rx="2" fill="#fff"/>' for i in range(14))
    blk = "".join(f'<rect x="{28+i*24}" y="40" width="14" height="42" fill="#222"/>' for i in range(13) if i % 7 not in (2, 6))
    return f'<svg viewBox="0 0 360 130" width="{w}" class=ins><rect x="0" y="10" width="360" height="110" rx="12" fill="#2a2a2e"/><rect x="20" y="18" width="80" height="14" rx="3" fill="#4fb3e8"/>{keys}{blk}</svg>'
def tag(t, due, c):
    return f'<div class=tg style="border-color:{c}"><b>{t}</b><span>{due}</span></div>'
P["p325_music_s1"] = ir(1, "MUSIC INSTRUMENT RENTAL AND REPAIR", "Who has the blue guitar?<br><span>Tags that know.</span>",
f'''<div class=w1><div class="cd wl1"><div class=pg1>
<div class=it1>{guitar("#2d7fb8",130)}{tag("G-04","Due Sat 28 Nov","#2d7fb8")}</div><div class=it1>{guitar("#a0522d",130)}{tag("G-02","In shop","#2f8a5b")}</div>
<div class=it1>{violin(100)}{tag("V-01","Due Tue 1 Dec","#b07d2b")}</div><div class=it1>{guitar("#d94f3d",130)}{tag("G-07","Repair","#d94f3d")}</div></div>
<div class=kb1>{keyboard(470)}{tag("K-03","Due Mon 30 Nov","#2d7fb8")}</div></div>
<div class=bb1><span class=vn>{ic("chat",22)} Every week at the counter</span><p>“The blue guitar? I think someone took it last month…”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.wl1{flex:1;min-height:0;padding:20px;display:flex;flex-direction:column;gap:14px;background:repeating-linear-gradient(0deg,#fff 0 46px,#f3eee8 46px 48px)}
.pg1{flex:1;display:flex;justify-content:space-around;align-items:flex-start}.it1,.kb1{display:flex;flex-direction:column;align-items:center;gap:8px}.ins{display:block}.kb1{flex-direction:row;justify-content:center;gap:16px}
.tg{background:#fff8e8;border:3px solid;border-radius:10px;padding:6px 12px;text-align:center}.tg b{display:block;font:700 20px/1.3 'TeX Gyre Adventor'}.tg span{font:600 14px/1.4 'DM Sans';color:#5a4a42}
.bb1{background:#3a2218;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px 'DM Sans';color:#f3cf8a;margin-bottom:6px}.bb1 p{font:500 23px/1.4 'DM Sans'}""")

rent = [("G-04", "Blue acoustic guitar", "Renter R-11", "Sat 28 Nov", "o"), ("K-03", "61-key keyboard", "Renter R-08", "Mon 30 Nov", "o"), ("V-01", "Violin, full size", "Renter R-15", "Tue 1 Dec", "o"),
        ("G-09", "Electric guitar + amp", "Renter R-03", "Fri 20 Nov", "l"), ("C-02", "Cajon", "Renter R-12", "Sun 6 Dec", "o"), ("K-05", "Keyboard stand", "Renter R-08", "Mon 30 Nov", "o")]
late = sum(1 for r in rent if r[4] == "l")
P["p325_music_s2"] = ir(2, "STEP 1 · EVERY RENTAL WITH A DUE DATE", "Out on rent?<br><span>See who and till when.</span>",
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>TAG</span><span>INSTRUMENT · SAMPLE</span><span>WITH</span><span>DUE</span></div>
{"".join(f'<div class="rw2 {k}"><b>{t}</b><span>{n}</span><span>{w}</span><em>{d}{" · late" if k=="l" else ""}</em></div>' for t,n,w,d,k in rent)}</div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>{len(rent)} out, {late} late. <b>Late ones get a polite message first, then a call.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:12px 24px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:.6fr 1.6fr 1fr 1fr;gap:12px;align-items:center;border-bottom:1px solid #efe8e2}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #3a2218;font:700 14px/1.4 'DM Sans';letter-spacing:1.5px;color:#7a6e68}
.rw2 b{font:700 22px/1.3 'TeX Gyre Adventor';color:#2d7fb8}.rw2>span{font:600 19px/1.35 'DM Sans'}.rw2 em{font:700 18px 'DM Sans';font-style:normal}
.rw2.l{background:#fdeceb;border-radius:12px;padding:0 10px}.rw2.l em{color:#c23b2d}""")

msgs = [("Sun 22 Nov", "G-09 was due on Friday. Please return it today, or tap to extend.", "Sent"), ("Thu 26 Nov", "G-04 is due on Saturday. Reply KEEP to rent it one more week.", "Planned"), ("Sat 28 Nov", "K-03 and the stand are due on Monday.", "Planned")]
P["p325_music_s3"] = ir(3, "STEP 2 · REMINDERS GO OUT ON THEIR OWN", "Due on Saturday?<br><span>They hear on Thursday.</span>",
f'''<div class=w3>{"".join(f'<div class="cd ms3"><div class=dd3><small>{d}</small><em class="{"s" if st=="Sent" else "p"}">{st}</em></div><p>{t}</p></div>' for d,t,st in msgs)}
<div class=nb><span class=ib>{ic("chat",26)}</span><span>Renters can extend with one reply, <b>so you keep the rent and the instrument is tracked.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.ms3{flex:1;padding:18px 24px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.dd3{display:flex;justify-content:space-between;align-items:center}.dd3 small{font:700 18px 'DM Sans';color:#7a6e68}.dd3 em{font:700 15px 'DM Sans';font-style:normal;border-radius:10px;padding:5px 12px}.dd3 .s{background:#dcf2e5;color:#1f7a47}.dd3 .p{background:#e4effa;color:#1f5f8f}
.ms3 p{font:500 26px/1.4 'DM Sans';background:#eef4f8;border-radius:18px 18px 18px 4px;padding:16px 20px}""")

jobs = [("G-07", "Red guitar", "New strings + neck set", "Ready Wed 25 Nov", "n"), ("K-11", "Customer keyboard", "Two keys stuck", "Ready Fri 27 Nov", "w"), ("V-04", "Customer violin", "Bridge change", "Part ordered", "p"), ("G-02", "Brown guitar", "String change", "Done", "d")]
P["p325_music_s4"] = ir(4, "STEP 3 · REPAIRS ON THE SAME BOARD", "Repair jobs too.<br><span>Ready date for each.</span>",
f'''<div class=w4>{"".join(f'<div class="cd jb4"><div class=ic4>{guitar({"G-07":"#d94f3d","G-02":"#a0522d"}.get(t,"#888"),60) if t.startswith("G") else (violin(50) if t.startswith("V") else keyboard(150))}</div><div class=tx4><b>{t} · {n}</b><span>{w}</span></div><em class={k}>{r}</em></div>' for t,n,w,r,k in jobs)}
<div class=nb><span class=ib>{ic("wrench",26)}</span><span>The customer gets a message when it is ready, <b>with the job number.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.jb4{flex:1;display:grid;grid-template-columns:160px 1fr 230px;gap:18px;align-items:center;padding:8px 24px;min-height:0}
.ic4{display:flex;justify-content:center;align-items:center;height:100%;min-height:0;overflow:hidden}.ic4 .ins{max-height:130px;width:auto}
.tx4 b{display:block;font:700 26px/1.3 'TeX Gyre Adventor'}.tx4 span{font:500 19px/1.4 'DM Sans';color:#6a5e58}
.jb4 em{font:700 17px 'DM Sans';font-style:normal;text-align:center;border-radius:12px;padding:10px}.jb4 em.n{background:#fff1d6;color:#8a5a10}.jb4 em.w{background:#e4effa;color:#1f5f8f}.jb4 em.p{background:#fdeceb;color:#c23b2d}.jb4 em.d{background:#dcf2e5;color:#1f7a47}""")

P["p325_music_s5"] = ir(5, "YOUR TURN", "Rent or repair instruments?<br><span>Let's build your rental book.</span>",
f'''<div class=w5><div class="cd hp5">{guitar("#2d7fb8",140)}{violin(105)}{guitar("#a0522d",140)}{guitar("#d94f3d",140)}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,34)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("tag","Rental tags","Who has what"),("bell","Reminders","Before the due date"),("wrench","Repair jobs","With ready dates"),("chat","One-reply extend","Keep the rent going")])}</div>
<div class=q>How do you track instruments out on rent today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#2d7fb8;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;display:flex;justify-content:space-around;align-items:center;padding:20px;background:repeating-linear-gradient(0deg,#fff 0 46px,#f3eee8 46px 48px)}.ins{display:block}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:16px 22px;box-shadow:0 10px 22px rgba(58,34,24,.07)}
.ti .ib{width:62px;height:62px;border-radius:18px;background:#f6e6c4;color:#b07d2b}.ti b{display:block;font:700 22px/1.35 'TeX Gyre Adventor'}.ti div span{font:500 17px/1.4 'DM Sans';color:#6a5e58}
.q{background:#3a2218;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'DM Sans'}""")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
