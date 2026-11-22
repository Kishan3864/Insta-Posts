import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 236 INDIA · Water tank cleaning service · SINGLE · Poppins + Inter · aqua teal / concrete / sunflower
# New technique: building section with overhead tanks and an underground sump, each tank drawn with water level + sediment layer by status.
tanks = [("Tank A", "Wing A roof", "Cleaned 12 Sep", "ok", 0.05), ("Tank B", "Wing B roof", "Cleaned 14 Jun", "due", 0.22), ("Tank C", "Wing C roof", "Cleaned 2 Mar", "over", 0.4), ("Sump", "Underground", "Cleaned 12 Sep", "ok", 0.06)]
def bld():
    s = '<svg viewBox="0 0 900 470" class=bd><rect width="900" height="470" fill="#e6f4f4"/><rect y="360" width="900" height="110" fill="#b9a68a"/>'
    for i in range(3):
        x = 60 + i * 270
        s += f'<rect x="{x}" y="150" width="240" height="210" fill="#d9dcde" stroke="#21414a" stroke-width="4"/>'
        for r in range(3):
            for c in range(3):
                s += f'<rect x="{x+22+c*72}" y="{168+r*62}" width="50" height="40" rx="4" fill="#9fd3dc" stroke="#21414a" stroke-width="2"/>'
    def tank(x, y, w, h, sed, st, lab):
        col = {"ok": "#2fb3b3", "due": "#f2b705", "over": "#e0524a"}[st]
        t = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="#fff" stroke="#21414a" stroke-width="4"/>'
        t += f'<rect x="{x+4}" y="{y+h*0.25}" width="{w-8}" height="{h*0.75-4}" rx="8" fill="#7fd1d6"/>'
        t += f'<rect x="{x+4}" y="{y+h-4-h*sed}" width="{w-8}" height="{h*sed}" rx="6" fill="#8b6b3f"/>'
        t += f'<circle cx="{x+w-12}" cy="{y-12}" r="15" fill="{col}" stroke="#21414a" stroke-width="3"/>'
        t += f'<text x="{x+w/2}" y="{y+h*0.18+6}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="20" fill="#21414a"><tspan>{lab}</tspan></text>'
        return t
    for i, (n, _, _, st, sed) in enumerate(tanks[:3]):
        s += tank(110 + i * 270, 60, 140, 90, sed, st, n.split()[1])
    s += tank(600, 378, 230, 80, tanks[3][4], "ok", "Sump")
    s += '<path d="M380 410 L560 410" stroke="#21414a" stroke-width="4" stroke-dasharray="10 8"/><text x="470" y="398" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#21414a"><tspan>pump line</tspan></text></svg>'
    return s
P["p236_tank"] = page("""
body{--f:'Inter';--h:'Poppins';background:#eef1f0;color:#21414a}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#168a8a;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#168a8a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sc{background:#fff;border-radius:26px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(33,65,74,.08)}
.sc>small,.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#66808a}
.bd{width:100%;display:block;border-radius:16px}
.lgd{display:flex;gap:22px;font:600 17px Inter;color:#4b6670}.lgd span{display:flex;align-items:center;gap:8px}.lgd i{width:16px;height:16px;border-radius:50%}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.tl{flex:1;min-width:0;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(33,65,74,.08)}
.tr{flex:1;display:grid;grid-template-columns:20px 1fr auto;gap:14px;align-items:center;border-top:1px solid #e6eceb}
.tr i{width:20px;height:20px;border-radius:50%}.tr b{display:block;font:700 22px/1.3 Poppins}.tr span{font:500 17px/1.3 Inter;color:#66808a}
.tr em{font:700 17px Inter;font-style:normal;padding:7px 12px;border-radius:10px}
.ok i{background:#2fb3b3}.ok em{background:#ddf3f3;color:#168a8a}.due i{background:#f2b705}.due em{background:#fff4cc;color:#8a6a00}.over i{background:#e0524a}.over em{background:#fde3e1;color:#c0392b}
.bk{width:330px;flex:none;background:#21414a;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.bk small{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#f2d55a}.bk p{font:500 20px/1.45 Inter}.bk p b{color:#f2d55a}
.ds{margin-top:auto;display:grid;grid-template-columns:1fr 1fr;gap:8px}.ds span{background:#2e5560;border-radius:12px;padding:10px 0;text-align:center;font:700 17px Inter}.ds .on{background:#f2b705;color:#21414a}
""", "<div class=kk>WATER TANK CLEANING · SOCIETIES</div><h1>“When was our tank cleaned?”<br><span>Show it, tank by tank.</span></h1>",
f'''<div class=vw><div class=sc><small>SAMPLE SOCIETY · 3 WINGS · 4 TANKS</small>{bld()}<div class=lgd><span><i style="background:#2fb3b3"></i>Cleaned in the last 3 months</span><span><i style="background:#f2b705"></i>Due now</span><span><i style="background:#e0524a"></i>Overdue</span></div></div>
<div class=bt><div class=tl>{"".join(f'<div class="tr {st}"><i></i><div><b>{n} · {w}</b><span>{c}</span></div><em>{ {"ok":"Next in Dec","due":"Due now","over":"Overdue"}[st] }</em></div>' for n,w,c,st,_ in tanks)}</div>
<div class=bk><small>MESSAGE TO THE SECRETARY · SAMPLE</small><p><b>Tank B and Tank C</b> are due for cleaning. Pick a day and we will share before and after photos.</p><div class=ds><span>Sat 28 Nov</span><span class=on>Sun 29 Nov</span></div></div></div></div>''',
"#21414a", "Clean water tanks? DM us", "background:#168a8a;color:#fff")

# ───────── 237 USA · Fence installer · SINGLE · Montserrat + Source Sans 3 · cedar orange / charcoal / pale sage
# New technique: top-down lot plan where the customer draws fence runs (measured in feet) + gate pins, feeding a quote form.
P["p237_fence"] = page("""
body{--f:'Source Sans 3';--h:'Montserrat';background:#eef1e8;color:#2b2d2f}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#b8612a;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#b8612a}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.pl{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(43,45,47,.08)}
.pl>small,.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6f746b}
.lt{width:100%;flex:1;min-height:0;display:block}
.qf{width:340px;flex:none;display:flex;flex-direction:column;gap:12px}
.fm{flex:1;background:#2b2d2f;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.fm small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#f3a76b}
.fr{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #45484b;font:500 24px 'Source Sans 3'}.fr b{font:800 30px Montserrat;color:#f3a76b}
.st{display:grid;grid-template-columns:1fr 1fr;gap:6px}.st span{text-align:center;border-radius:10px;padding:12px 0;font:700 18px 'Source Sans 3';background:#45484b}.st .on{background:#b8612a}
.nt{background:#fff;border-radius:20px;padding:16px 18px;font:600 21px/1.4 'Source Sans 3'}.nt b{color:#b8612a}
""", "<div class=kk>FENCE INSTALLATION · QUOTE REQUESTS</div><h1>“How much for a fence?”<br><span>Let them draw it first.</span></h1>",
f'''<div class=vw><div class=pl><small>SAMPLE BACKYARD · DRAWN BY THE CUSTOMER</small>
<svg viewBox="0 0 560 760" class=lt><rect width="560" height="760" rx="18" fill="#cfe3b8"/>
<rect x="170" y="560" width="220" height="170" fill="#e8e1d4" stroke="#2b2d2f" stroke-width="4"/><text x="280" y="652" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="24" fill="#2b2d2f"><tspan>House</tspan></text>
<rect x="250" y="250" width="110" height="80" rx="40" fill="#9fd3e6" stroke="#2b2d2f" stroke-width="3"/><circle cx="120" cy="330" r="46" fill="#7fae5a"/><circle cx="440" cy="190" r="38" fill="#7fae5a"/>
<path d="M170 600 L60 600 L60 60 L500 60 L500 600 L390 600" fill="none" stroke="#b8612a" stroke-width="10" stroke-linejoin="round"/>
<g fill="#2b2d2f">{"".join(f'<rect x="{x-6}" y="{y-6}" width="12" height="12"/>' for x,y in [(60,600),(60,330),(60,60),(280,60),(500,60),(500,330),(500,600),(170,600),(390,600)])}</g>
<rect x="44" y="430" width="32" height="70" fill="#fff" stroke="#2b2d2f" stroke-width="4"/><rect x="484" y="430" width="32" height="70" fill="#fff" stroke="#2b2d2f" stroke-width="4"/>
<g font-family="Montserrat" font-weight="800" font-size="22"><rect x="230" y="24" width="100" height="34" rx="10" fill="#2b2d2f"/><text x="280" y="48" text-anchor="middle" fill="#fff"><tspan>110 ft</tspan></text>
<rect x="84" y="290" width="88" height="34" rx="10" fill="#2b2d2f"/><text x="128" y="314" text-anchor="middle" fill="#fff"><tspan>135 ft</tspan></text>
<rect x="390" y="290" width="88" height="34" rx="10" fill="#2b2d2f"/><text x="434" y="314" text-anchor="middle" fill="#fff"><tspan>135 ft</tspan></text>
<rect x="64" y="612" width="96" height="34" rx="10" fill="#2b2d2f"/><text x="112" y="636" text-anchor="middle" fill="#fff"><tspan>28 ft</tspan></text>
<rect x="400" y="612" width="96" height="34" rx="10" fill="#2b2d2f"/><text x="448" y="636" text-anchor="middle" fill="#fff"><tspan>28 ft</tspan></text></g>
<g font-family="Source Sans 3" font-weight="700" font-size="20" fill="#b8612a"><text x="88" y="470"><tspan>Gate 1</tspan></text><text x="410" y="470"><tspan>Gate 2</tspan></text></g></svg></div>
<div class=qf><div class=fm><small>QUOTE REQUEST · SAMPLE</small>{"".join(f'<div class=fr><span>{a}</span><b>{b}</b></div>' for a,b in [("Total length","436 ft"),("Walk gates","2"),("Height","6 ft"),("Old fence to remove","No")])}
<div class=cap style="color:#c9ccc4">STYLE</div><div class=st><span class=on>Wood privacy</span><span>Picket</span><span>Vinyl</span><span>Chain link</span></div></div>
<div class=nt>You set the price per foot. <b>The quote is ready from the drawing</b>, before any site visit.</div></div></div>''',
"#2b2d2f", "Install fences? DM us", "background:#b8612a;color:#fff")

# ───────── 238 INDIA · Home salon at doorstep (women) · CAROUSEL 5 · Cardo + Fira Sans · coral / teal / sand · PHONE on slide 2
# New techniques: open kit bag with compartments as a per-booking checklist, day route ribbon with travel gaps, slot grid by area.
HB = """
body{--f:'Fira Sans';--h:'Cardo';background:#f7efe3;color:#163c40}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#e0604a;margin-top:22px;align-self:flex-start}
h1{font-family:'Cardo';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#e0604a}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(22,60,64,.08)}
.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#6d8285}
.nb{display:flex;align-items:center;gap:14px;background:#163c40;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Fira Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e0604a}.nb b{color:#ffc2b5}
"""
def hb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#163c40;color:#fff"):
    return page(HB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#163c40", cta, ctacss, tagline=f"{n} / 5")
day = [("10:00", "Facial + threading", "Area A", 60), ("11:00", "travel", "35 min", 35), ("11:35", "free", "", 25), ("12:00", "Hair spa", "Area B", 75), ("13:15", "travel", "50 min", 50), ("14:05", "Manicure + pedicure", "Area D", 90)]
P["p238_salon_s1"] = hb(1, "HOME SALON SERVICE · STYLIST'S DAY", "Bookings across the city?<br><span>Plan the route, not just the time.</span>",
f'''<div class=w1><div class="cd rb"><small class=cap>STYLIST 1 · TUESDAY · BOOKED BY CALLS · SAMPLE</small>
<div class=rib>{"".join(f'<div class="sg {"tv" if k=="travel" else ("fr" if k=="free" else "bk")}" style="flex:{m}"><b>{t}</b><span>{k if k not in ("travel","free") else ("Travel " + a if k=="travel" else "Gap")}</span>{f"<em>{a}</em>" if k not in ("travel","free") else ""}</div>' for t,k,a,m in day)}</div>
<div class=ax><span style="left:0">10 AM</span><span style="left:35.8%;transform:translateX(-50%)">12 PM</span><span style="left:71.6%;transform:translateX(-50%)">2 PM</span><span style="right:0">3:35 PM</span></div></div>
<div class=pr>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("85 min","on the road in one day"),("3 areas","booked far apart"),("1 kit bag","packed for three services")])}</div>
<div class=nb><span class=ib>{ic("map",26)}</span><span>Every call books a time. <b>Nobody checks the distance.</b></span></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rb{padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.rib{height:470px;display:flex;gap:6px}.sg{border-radius:18px;padding:16px 12px;display:flex;flex-direction:column;gap:6px;min-width:0}
.sg b{font:700 23px/1.3 'Fira Sans'}.sg span{font:600 20px/1.3 'Fira Sans'}.sg em{font:500 18px/1.3 'Fira Sans';font-style:normal}
.bk{background:#163c40;color:#fff}.bk em{color:#a9d3d0}.tv{background:repeating-linear-gradient(-45deg,#ffe0d8 0 14px,#ffd0c5 14px 28px);color:#b23a26}.fr{background:#f2ece2;color:#8a8478;border:2px dashed #d8cfbf}
.ax{position:relative;height:24px;font:600 16px/1.4 'Fira Sans';color:#6d8285}.ax span{position:absolute;top:0}
.pr{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.pr div{background:#fff;border-radius:20px;padding:18px 20px;border-top:8px solid #e0604a;display:flex;flex-direction:column;justify-content:center}.pr b{display:block;font:700 40px/1.35 Cardo}.pr span{font:500 21px/1.35 'Fira Sans';color:#6d8285}""")

slots = [("Area A", ["10 AM", "11 AM", "12 PM"], [0, 1]), ("Area B", ["12 PM", "1 PM", "2 PM"], [0]), ("Area C", ["2 PM", "3 PM", "4 PM"], []), ("Area D", ["3 PM", "4 PM", "5 PM"], [1])]
P["p238_salon_s2"] = hb(2, "STEP 1 · SLOTS BY AREA", "Customers pick a slot<br><span>near the stylist's route.</span>",
f'''<div class=w2><div class=lt2>{"".join(f'<div class="cd ar"><b>{a}</b><div class=sl>{"".join(f'<span class="{"tk" if i in tk else ""}">{t}</span>' for i,t in enumerate(ts))}</div></div>' for a,ts,tk in slots)}
<div class=nb><span class=ib>{ic("pin",26)}</span><span>Morning in one area, afternoon in the next. <b>Less time on the road.</b></span></div></div>
{phone(f"""<div class=ap><h4>Book at home</h4><small>SAMPLE BOOKING PAGE</small>
<div class=rw><span>Service</span><b>Hair spa</b></div><div class=rw><span>Your area</span><b>Area B</b></div><div class=rw><span>Date</span><b>Tue 24 Nov</b></div>
<div class=gl>{"".join(f'<span class="{c}">{t}</span>' for t,c in [("12 PM","x"),("1 PM","on"),("2 PM","")])}</div>
<div class=rw><span>Stylist</span><b>Stylist 1</b></div><div class=rw><span>Room needed</span><b>Chair + plug point</b></div><div class=rw><span>Advance</span><b>Paid by UPI</b></div><div class=bt>Confirm 1 PM</div></div>""", w=340, h=720)}</div>''',
css=""".w2{flex:1;display:flex;gap:18px;min-height:0}.lt2{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.ar{flex:1;padding:14px 20px;display:flex;flex-direction:column;justify-content:center;gap:10px}.ar b{font:700 30px/1.3 Cardo}
.sl{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.sl span{text-align:center;border:2px solid #cfe3e1;border-radius:12px;padding:10px 0;font:700 19px 'Fira Sans';color:#163c40}.sl .tk{background:#eee6da;border-color:#eee6da;color:#a39b8e;text-decoration:line-through}
.ap{flex:1;padding:8px 18px 18px;display:flex flex-direction:column;gap:10px;display:flex;flex-direction:column}.ap h4{font:700 26px/1.3 Cardo}.ap small{font:700 12px/1.4 'Fira Sans';letter-spacing:1.5px;color:#6d8285}
.ap .rw{display:flex;justify-content:space-between;border:2px solid #ece6dc;border-radius:12px;padding:12px 12px;font:500 16px 'Fira Sans'}.ap .rw b{font-weight:700}
.gl{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.gl span{text-align:center;border:2px solid #ece6dc;border-radius:10px;padding:8px 0;font:700 15px 'Fira Sans'}.gl .on{background:#e0604a;border-color:#e0604a;color:#fff}.gl .x{color:#b9b2a6;text-decoration:line-through}
.ap .bt{margin-top:auto;background:#163c40;color:#fff;border-radius:12px;padding:13px;text-align:center;font:700 16px 'Fira Sans'}""")

route = [("10:00 AM", "Area A", "Facial + threading", "60 min"), ("11:20 AM", "Area A", "Waxing", "45 min"), ("1:00 PM", "Area B", "Hair spa", "75 min"), ("3:00 PM", "Area C", "Manicure", "45 min")]
K = 1.4
mp = f'<svg viewBox="0 0 420 {560*K:.0f}" class=mpp><rect width="420" height="{560*K:.0f}" rx="18" fill="#e7efe9"/>'
mp += f'<path d="M0 {180*K} L420 {120*K} M0 {420*K} L420 {380*K} M140 0 L180 {560*K} M320 0 L300 {560*K}" stroke="#fff" stroke-width="18"/>'
for i, (x, y, w, h, n) in enumerate([(20, 20, 180, 150, "Area A"), (220, 140, 180, 170, "Area B"), (40, 330, 180, 170, "Area C")]):
    mp += f'<rect x="{x}" y="{y*K}" width="{w}" height="{h*K}" rx="16" fill="#163c40" fill-opacity=".08" stroke="#163c40" stroke-width="2" stroke-dasharray="8 6"/><text x="{x+14}" y="{y*K+30}" font-family="Fira Sans" font-weight="700" font-size="20" fill="#163c40"><tspan>{n}</tspan></text>'
pts = [(80, 110*K), (150, 150*K), (300, 240*K), (130, 430*K)]
mp += '<path d="M' + " L".join(f"{x} {y}" for x, y in pts) + '" fill="none" stroke="#e0604a" stroke-width="6" stroke-dasharray="4 12" stroke-linecap="round"/>'
mp += "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="#e0604a" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Fira Sans" font-weight="800" font-size="22" fill="#fff"><tspan>{i+1}</tspan></text>' for i, (x, y) in enumerate(pts)) + '</svg>'
P["p238_salon_s3"] = hb(3, "STEP 2 · THE DAY'S ROUTE", "Four homes, three areas,<br><span>one clean route.</span>",
f'''<div class=w3><div class="cd mpc">{mp}</div><div class="cd rl"><small class=cap>STYLIST 1 · WED 25 NOV · SAMPLE</small>{"".join(f'<div class=rs><i>{i+1}</i><div><b>{t} · {a}</b><span>{s} · {d}</span></div></div>' for i,(t,a,s,d) in enumerate(route))}
<div class=tt><b>4</b> bookings · <b>about 40 min</b> on the road</div></div></div>''',
css=""".w3{flex:1;display:flex;gap:14px;min-height:0}.mpc{width:440px;flex:none;padding:12px;display:flex}.mpp{width:100%;height:100%;display:block}
.rl{flex:1;min-width:0;padding:18px 22px;display:flex;flex-direction:column;gap:8px}
.rs{flex:1;display:flex;align-items:center;gap:16px;border-top:1px solid #efe8dc}.rs i{width:46px;height:46px;border-radius:50%;background:#e0604a;color:#fff;font:800 22px 'Fira Sans';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.rs b{display:block;font:700 26px/1.3 Cardo}.rs span{font:500 19px/1.35 'Fira Sans';color:#6d8285}
.tt{background:#163c40;color:#fff;border-radius:16px;padding:14px 18px;font:500 20px/1.4 'Fira Sans'}.tt b{color:#ffc2b5}""")

kit = [("Facial kit", "Booking 1", True), ("Threading set", "Booking 1", True), ("Wax heater + strips", "Booking 2", True), ("Hair spa cream + steamer", "Booking 3", True), ("Nail kit", "Booking 4", True), ("Fresh towels × 4", "All bookings", False)]
P["p238_salon_s4"] = hb(4, "STEP 3 · KIT CHECKLIST FROM BOOKINGS", "The kit bag is packed<br><span>from the day's bookings.</span>",
f'''<div class=w4><div class=bag><div class=hdl></div><div class=bgb>{"".join(f'<div class="cp{" mi" if not ok else ""}"><b>{a}</b><span>{b}</span><i>{ic("check",16,w=3) if ok else "!"}</i></div>' for a,b,ok in kit)}</div></div>
<div class=nb><span class=ib>{ic("box",26)}</span><span>5 of 6 packed. <b>Towels are still missing.</b> The app reminds the stylist before leaving home.</span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.bag{flex:1;display:flex;flex-direction:column;align-items:center;min-height:0;padding-top:4px}
.hdl{width:260px;height:56px;border:14px solid #163c40;border-bottom:0;border-radius:40px 40px 0 0}
.bgb{flex:1;width:100%;background:#e0604a;border-radius:30px;padding:22px;display:grid;grid-template-columns:1fr 1fr 1fr;grid-auto-rows:1fr;gap:12px;box-shadow:inset 0 -14px 0 rgba(0,0,0,.12)}
.cp{background:#fff7f0;border-radius:18px;padding:14px 16px;display:flex;flex-direction:column;justify-content:center;gap:6px;position:relative;border:3px dashed #f3b5a6}
.cp b{font:700 25px/1.3 Cardo;padding-right:30px}.cp span{font:600 17px 'Fira Sans';color:#6d8285}
.cp i{position:absolute;top:12px;right:12px;width:30px;height:30px;border-radius:50%;background:#163c40;color:#fff;display:flex;align-items:center;justify-content:center;font:800 18px 'Fira Sans';font-style:normal}
.cp.mi{background:#163c40;border-color:#163c40}.cp.mi b{color:#fff}.cp.mi span{color:#ffc2b5}.cp.mi i{background:#e0604a}""")

P["p238_salon_s5"] = hb(5, "YOUR TURN", "Run a home salon service?<br><span>Let's build your booking app.</span>",
f'''<div class=w5><div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,44)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("cal","Slots by area","Customers book near the route"),("map","Day route","One clean path per stylist"),("box","Kit checklist","Packed from the bookings"),("rupee","Advance by UPI","Noted on every booking")])}</div>
<div class=q>How do you plan your stylists' day today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#e0604a;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tl{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.ti{display:flex;flex-direction:column;justify-content:center;gap:18px;background:#fff;border-radius:26px;padding:26px;box-shadow:0 10px 22px rgba(22,60,64,.07)}
.ti .ib{width:96px;height:96px;border-radius:26px;background:#ffe3dc;color:#e0604a}.ti b{display:block;font:700 40px/1.3 Cardo}.ti span{font:500 21px/1.4 'Fira Sans';color:#6d8285}
.q{background:#163c40;color:#fff;border-radius:22px;padding:22px 24px;font:600 25px/1.4 'Fira Sans'}""")

# ───────── 239 INDIA · Bike servicing at doorstep · SINGLE · Anton + Roboto · racing green / cream / brick
# New technique: paper service booklet with stamped entries (circular ink stamps) beside its digital twin card with next service by km.
stamps = [("12 Jan 2026", "8,150 km", "Oil + chain"), ("18 May 2026", "11,020 km", "Oil + brakes"), ("2 Sep 2026", "13,940 km", "Oil + air filter")]
def stamp(i):
    return f'<svg viewBox="0 0 120 120" width="96" height="96"><circle cx="60" cy="60" r="52" fill="none" stroke="#b33a2c" stroke-width="5" stroke-opacity=".8"/><circle cx="60" cy="60" r="40" fill="none" stroke="#b33a2c" stroke-width="2" stroke-opacity=".8"/><text x="60" y="56" text-anchor="middle" font-family="Anton" font-size="17" fill="#b33a2c" fill-opacity=".85"><tspan>SERVICED</tspan></text><text x="60" y="84" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="12" fill="#b33a2c" fill-opacity=".85"><tspan>SAMPLE</tspan></text></svg>'
P["p239_bike"] = page("""
body{--f:'Roboto';--h:'Anton';background:#f4ecda;color:#173a2e}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#b33a2c;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#1f6b4e}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.bk{flex:1;min-width:0;background:#fffaf0;border-radius:10px 22px 22px 10px;padding:18px 22px 18px 40px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(23,58,46,.14);position:relative;border-left:16px solid #1f6b4e}
.bk>small,.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#7a7462}
.bk h4{font:400 30px/1.4 'Anton';letter-spacing:.5px}
.en{flex:1;display:flex;align-items:center;gap:16px;border-top:2px dashed #e0d6bf}
.en .tx{flex:1}.en b{display:block;font:700 25px/1.3 Roboto}.en span{font:500 20px/1.35 Roboto;color:#5f5a4c}.en svg{display:block;flex:none}
.en.nx{border:3px dashed #1f6b4e;border-radius:16px;padding:0 16px;background:#eaf4ef}.en.nx b{color:#1f6b4e}
.dc{width:340px;flex:none;display:flex;flex-direction:column;gap:12px}
.cd1{flex:1;background:#173a2e;color:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.cd1 small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#f2c14e}
.km{font:400 56px/1.35 'Anton';letter-spacing:1px;color:#f2c14e}.km span{font:500 18px 'Roboto';color:#cfe3da;display:block;letter-spacing:0;line-height:1.3}
.br{height:20px;border-radius:10px;background:#2c5547;overflow:hidden}.br i{display:block;height:100%;width:62%;background:#f2c14e}
.ln{display:flex;justify-content:space-between;font:600 16px Roboto;color:#cfe3da}
.pt{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:1px solid #2c5547;font:500 22px/1.4 Roboto}.pt b{color:#fff}
.rm{background:#fff;border-radius:22px;padding:16px 18px;font:500 19px/1.45 Roboto}.rm b{display:block;font:700 15px/1.4 Roboto;letter-spacing:2px;color:#b33a2c;margin-bottom:4px}
""", "<div class=kk>BIKE SERVICE AT HOME · SERVICE BOOK</div><h1>Service book lost again?<br><span>Keep every visit online.</span></h1>",
f'''<div class=vw><div class=bk><small>SERVICE BOOK · SAMPLE BIKE · 125 CC</small><h4>Visits so far</h4>
{"".join(f'<div class=en><div class=tx><b>{d}</b><span>{k} · {w}</span></div>{stamp(i)}</div>' for i,(d,k,w) in enumerate(stamps))}
<div class="en nx"><div class=tx><b>Next: at 16,900 km</b><span>Oil change, chain clean, brake check</span></div></div></div>
<div class=dc><div class=cd1><small>ON THE OWNER'S PHONE · SAMPLE</small><div class=km>15,780 km<span>today's reading</span></div><div class=br><i></i></div><div class=ln><span>Last: 13,940</span><span>Next: 16,900</span></div>
<div class=cap style="color:#f2c14e;margin-top:8px">PARTS USED LAST VISIT</div><div class=pt><span><b>Engine oil</b> · 1 L</span></div><div class=pt><span><b>Air filter</b> · replaced</span></div><div class=pt><span><b>Chain</b> · cleaned and oiled</span></div></div>
<div class=rm><b>REMINDER</b>About 1,100 km to go. Book a home visit for this Sunday?</div></div></div>''',
"#173a2e", "Service bikes at home? DM us", "background:#1f6b4e;color:#fff")

# ───────── 240 CANADA · Wood stove installer · SINGLE · Crimson Text + Roboto · ember red / stone grey / birch white
# New technique: room cutaway with stove, flue pipe through the roof and numbered survey points that match a checklist.
P["p240_stove"] = page("""
body{--f:'Roboto';--h:'Crimson Text';background:#f2f0ec;color:#26292c}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#c2412d;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:68px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#c2412d}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.cv{width:470px;flex:none;background:#fff;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(38,41,44,.08)}
.cv>small,.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#72777c}
.rmv{width:100%;flex:1;min-height:0;display:block}
.cl{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.sv{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(38,41,44,.08)}
.sv h4{font:700 30px/1.3 'Crimson Text'}
.pt{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #ece9e3}.pt i{width:40px;height:40px;border-radius:50%;background:#c2412d;color:#fff;font:800 19px Roboto;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.pt b{display:block;font:700 23px/1.3 Roboto}.pt span{font:500 19px/1.35 Roboto;color:#5f6468}
.dy{background:#26292c;color:#fff;border-radius:22px;padding:16px 20px;display:flex;align-items:center;gap:14px}.dy .ib{width:54px;height:54px;border-radius:16px;background:#c2412d}
.dy b{display:block;font:700 24px/1.3 'Crimson Text'}.dy span{font:500 17px/1.35 Roboto;color:#cfd2d5}
""", "<div class=kk>WOOD STOVE INSTALLATION · SITE SURVEY</div><h1>Same 5 checks at every site?<br><span>Do them in one form.</span></h1>",
f'''<div class=vw><div class=cv><small>SURVEY · SAMPLE CABIN · LIVING ROOM</small>
<svg viewBox="0 0 440 660" class=rmv><rect width="440" height="660" fill="#eef3f7"/><path d="M0 170 L220 40 L440 170 Z" fill="#7a7f85" stroke="#26292c" stroke-width="4"/><rect x="0" y="170" width="440" height="400" fill="#f6efe2" stroke="#26292c" stroke-width="4"/>
<rect x="0" y="570" width="440" height="90" fill="#b58a5c"/><rect x="120" y="510" width="200" height="60" fill="#9aa0a6" stroke="#26292c" stroke-width="3"/>
<rect x="160" y="400" width="120" height="110" rx="10" fill="#33373b" stroke="#26292c" stroke-width="3"/><rect x="180" y="430" width="80" height="56" rx="6" fill="#ff8a3d"/><path d="M200 486 q20 -40 40 0" fill="#ffd166"/>
<rect x="206" y="60" width="28" height="340" fill="#55595e" stroke="#26292c" stroke-width="3"/><rect x="198" y="40" width="44" height="24" fill="#55595e" stroke="#26292c" stroke-width="3"/>
<path d="M300 300 L400 300" stroke="#c2412d" stroke-width="3" stroke-dasharray="8 6"/><path d="M60 455 L160 455" stroke="#c2412d" stroke-width="3" stroke-dasharray="8 6"/>
{"".join(f'<circle cx="{x}" cy="{y}" r="22" fill="#c2412d" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Roboto" font-weight="800" font-size="22" fill="#fff"><tspan>{n}</tspan></text>' for n,x,y in [(1,350,270),(2,110,425),(3,220,600),(4,262,112),(5,330,370)])}</svg></div>
<div class=cl><div class=sv><small class=cap>SURVEY FORM · 5 POINTS · SAMPLE</small><h4>Sample cabin, Lot 12</h4>
{"".join(f'<div class=pt><i>{n}</i><div><b>{a}</b><span>{b}</span></div></div>' for n,a,b in [(1,"Wall distance","Measured, photo added"),(2,"Side distance","Measured, photo added"),(3,"Floor pad","Stone, size noted"),(4,"Pipe through roof","Roof type and pitch noted"),(5,"Room size","For the stove size you suggest")])}</div>
<div class=dy><span class=ib>{ic("cal",26)}</span><div><b>Install day: Thu 10 Dec</b><span>The crew sees all 5 points before they arrive.</span></div></div></div></div>''',
"#26292c", "Install wood stoves? DM us", "background:#c2412d;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
