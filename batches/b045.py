import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 241 INDIA · Wedding car decorator · SINGLE · Gelasio + Fira Sans · jasmine white / marigold / ink teal
# New technique: side-view car with numbered decoration zones (bonnet, doors, roof, boot) that match a flower list; date strip of booked cars.
car = '''<svg viewBox="0 0 900 360" class=car><ellipse cx="450" cy="330" rx="400" ry="18" fill="#d9d2c0"/>
<path d="M70 250 L90 190 Q110 170 160 165 L300 160 L370 95 Q390 80 430 80 L600 80 Q640 80 665 100 L740 165 Q820 170 840 200 L850 250 Q850 270 830 272 L90 272 Q68 270 70 250 Z" fill="#f7f5ef" stroke="#163c45" stroke-width="5"/>
<path d="M390 100 L440 98 L440 160 L330 162 Z" fill="#cfe3e8" stroke="#163c45" stroke-width="3"/><path d="M460 98 L590 98 Q620 98 640 115 L690 160 L460 160 Z" fill="#cfe3e8" stroke="#163c45" stroke-width="3"/>
<line x1="450" y1="100" x2="450" y2="270" stroke="#163c45" stroke-width="3"/><line x1="300" y1="168" x2="300" y2="270" stroke="#163c45" stroke-width="3"/><line x1="700" y1="168" x2="700" y2="270" stroke="#163c45" stroke-width="3"/>
<circle cx="220" cy="275" r="52" fill="#163c45"/><circle cx="220" cy="275" r="22" fill="#c9c4b8"/><circle cx="690" cy="275" r="52" fill="#163c45"/><circle cx="690" cy="275" r="22" fill="#c9c4b8"/>'''
random.seed(241)
def flowers(cx, cy, n, r, c):
    return "".join(f'<circle cx="{cx+random.uniform(-r,r):.0f}" cy="{cy+random.uniform(-r*0.35,r*0.35):.0f}" r="{random.choice([9,11,13])}" fill="{c}" stroke="#b8650a" stroke-width="1.5"/>' for _ in range(n))
car += flowers(160, 182, 16, 70, "#f4a300") + flowers(515, 92, 12, 70, "#ffffff") + flowers(375, 215, 10, 45, "#f4a300") + flowers(575, 215, 10, 45, "#f4a300") + flowers(790, 185, 8, 35, "#ffffff")
car += '<path d="M440 160 Q520 230 600 160" fill="none" stroke="#e0567a" stroke-width="6"/>'
car += "".join(f'<circle cx="{x}" cy="{y}" r="24" fill="#163c45" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Fira Sans" font-weight="800" font-size="22" fill="#fff"><tspan>{n}</tspan></text>' for n, x, y in [(1, 130, 130), (2, 515, 32), (3, 375, 250), (4, 790, 130)]) + '</svg>'
fl = [("1", "Bonnet", "Marigold heart, 3 kg", "#f4a300"), ("2", "Roof", "White flower line", "#ffffff"), ("3", "Doors", "Marigold strings + ribbon", "#f4a300"), ("4", "Boot", "White bunch, small", "#ffffff")]
P["p241_weddingcar"] = page("""
body{--f:'Fira Sans';--h:'Gelasio';background:#fbf8f0;color:#163c45}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#c27a00;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#c27a00}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.cc{background:#fff;border-radius:26px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(22,60,69,.08)}
.cc>small,.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#6e8187}
.car{width:100%;display:block}
.fl{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.fl div{border-radius:16px;background:#f6f1e4;padding:12px 14px;display:flex;flex-direction:column;gap:4px}
.fl b{font:700 25px/1.3 Gelasio;display:flex;align-items:center;gap:8px}.fl b i{width:30px;height:30px;border-radius:50%;background:#163c45;color:#fff;font:800 16px 'Fira Sans';font-style:normal;display:flex;align-items:center;justify-content:center}
.fl span{font:500 19px/1.35 'Fira Sans';color:#4d6268}.fl em{width:22px;height:22px;border-radius:50%;border:2px solid #b8650a}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.ds{flex:1;min-width:0;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(22,60,69,.08)}
.dr{flex:1;display:grid;grid-template-columns:120px 1fr auto;gap:12px;align-items:center;border-top:1px solid #efe9da}
.dr b{font:700 20px/1.3 'Fira Sans'}.dr span{font:500 19px/1.35 'Fira Sans'}.dr em{font:700 16px 'Fira Sans';font-style:normal;padding:7px 12px;border-radius:10px;background:#e3f0f2;color:#163c45}
.dr.me{background:#fff4dc;border-radius:12px;padding:0 10px}.dr.me em{background:#f4a300;color:#163c45}
.ms{width:320px;flex:none;background:#163c45;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.ms small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#f4c35a}.ms p{font:500 20px/1.45 'Fira Sans'}.ms p b{color:#f4c35a}
.ms .ph{margin-top:auto;display:flex;gap:8px}.ms .ph i{flex:1;height:70px;border-radius:12px;background:linear-gradient(135deg,#2c5c66,#1d4851);display:flex;align-items:center;justify-content:center;color:#cfe3e8}
""", "<div class=kk>WEDDING CAR DECORATION · BOOKINGS</div><h1>“Same as the photo, please.”<br><span>Book it zone by zone.</span></h1>",
f'''<div class=vw><div class=cc><small>BOOKING WC-241 · SAMPLE CAR · SUN 6 DEC · 9 AM</small>{car}
<div class=fl>{"".join(f'<div><b><i>{n}</i>{z}</b><span>{t}</span></div>' for n,z,t,c in fl)}</div></div>
<div class=bt><div class=ds><small class=cap>CARS BOOKED · SUN 6 DEC · SAMPLE</small>{"".join(f'<div class="dr{" me" if m else ""}"><b>{t}</b><span>{a}</span><em>{s}</em></div>' for t,a,s,m in [("7:00 AM","Car WC-239 · full marigold","Team 1",False),("9:00 AM","Car WC-241 · 4 zones","Team 1",True),("11:30 AM","Car WC-240 · roses, light","Team 2",False)])}</div>
<div class=ms><small>SENT TO THE FLOWER SHOP</small><p>Sun 6 Dec: <b>marigold 3 kg</b>, white flowers 2 bunches, ribbon 5 m.</p><div class=ph><i>{ic("img",26)}</i><i>{ic("img",26)}</i><i>{ic("img",26)}</i></div></div></div></div>''',
"#163c45", "Decorate wedding cars? DM us", "background:#163c45;color:#fff")

# ───────── 242 INDIA · Modular wardrobe installer · CAROUSEL 5 · TeX Gyre Adventor + Inter · laminate grey / oak / olive
# New techniques: wall elevation with a beam and switchboard as obstacles, three shutter layouts as options, panel cut list with a sheet-usage bar.
WB = """
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#eceae4;color:#2a2f26}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#6b7d2a;margin-top:22px;align-self:flex-start}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#6b7d2a}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(42,47,38,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#7c7f75}
.nb{display:flex;align-items:center;gap:14px;background:#2a2f26;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Inter}.nb .ib{width:50px;height:50px;border-radius:14px;background:#c8a06a;color:#2a2f26}.nb b{color:#d9e59a}
"""
def wb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2a2f26;color:#fff"):
    return page(WB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2a2f26", cta, ctacss, tagline=f"{n} / 5")
def wall(marks=True, ward=None):
    # wall 9 ft wide x 10 ft tall, scale 70 px/ft -> 630 x 700, beam at top 1 ft deep, switchboard on right
    s = '<svg viewBox="-70 -60 780 820" class=wl><rect x="0" y="0" width="630" height="700" fill="#f4f1ea" stroke="#2a2f26" stroke-width="5"/>'
    s += '<rect x="0" y="0" width="630" height="70" fill="#c9c4b6" stroke="#2a2f26" stroke-width="3"/><text x="315" y="44" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="#2a2f26"><tspan>Beam · 1 ft deep</tspan></text>'
    s += '<rect x="560" y="330" width="44" height="62" rx="4" fill="#fff" stroke="#2a2f26" stroke-width="3"/><circle cx="582" cy="352" r="6" fill="#2a2f26"/><circle cx="582" cy="372" r="6" fill="#2a2f26"/>'
    s += '<rect x="0" y="690" width="630" height="10" fill="#8a7a62"/>'
    if ward:
        s += ward
    if marks:
        s += '<g font-family="Inter" font-weight="800" font-size="34" fill="#6b7d2a"><path d="M0 -30 L630 -30" stroke="#6b7d2a" stroke-width="3"/><rect x="250" y="-58" width="130" height="54" rx="12" fill="#fff" stroke="#6b7d2a" stroke-width="3"/><text x="315" y="-19" text-anchor="middle"><tspan>9 ft</tspan></text>'
        s += '<path d="M-36 0 L-36 700" stroke="#6b7d2a" stroke-width="3"/><rect x="-68" y="310" width="64" height="80" rx="12" fill="#fff" stroke="#6b7d2a" stroke-width="3"/><text x="-36" y="360" text-anchor="middle" font-size="24"><tspan>10 ft</tspan></text></g>'
    return s + '</svg>'
def wardrobe(cols, x0=10, w=540, top=80, bot=690, col="#c8a06a"):
    s = ""; x = x0
    for kind, cw in cols:
        s += f'<rect x="{x}" y="{top}" width="{cw}" height="{bot-top}" fill="{col}" stroke="#2a2f26" stroke-width="3"/>'
        if kind == "door":
            s += f'<rect x="{x+cw-18}" y="{(top+bot)/2-40}" width="6" height="80" rx="3" fill="#2a2f26"/>'
        elif kind == "drawers":
            for k in range(4):
                yy = top + (bot - top) * (0.45 + k * 0.137)
                s += f'<line x1="{x}" y1="{yy:.0f}" x2="{x+cw}" y2="{yy:.0f}" stroke="#2a2f26" stroke-width="3"/><rect x="{x+cw/2-24}" y="{yy+18:.0f}" width="48" height="6" rx="3" fill="#2a2f26"/>'
            s += f'<rect x="{x+cw-18}" y="{top+80}" width="6" height="80" rx="3" fill="#2a2f26"/>'
        elif kind == "slide":
            s += f'<line x1="{x+cw/2}" y1="{top}" x2="{x+cw/2}" y2="{bot}" stroke="#2a2f26" stroke-width="3"/><rect x="{x+cw/2-30}" y="{(top+bot)/2-50}" width="8" height="100" rx="3" fill="#2a2f26"/><rect x="{x+cw/2+22}" y="{(top+bot)/2-50}" width="8" height="100" rx="3" fill="#2a2f26"/>'
        x += cw
    s += f'<rect x="{x0}" y="{top-0}" width="{w}" height="40" fill="none"/>'
    return s
P["p242_wardrobe_s1"] = wb(1, "MODULAR WARDROBE · SITE VISIT", "“Will it fit under the beam?”<br><span>Measure it once, properly.</span>",
f'''<div class=w1><div class="cd wc"><small class=cap>SAMPLE BEDROOM · WALL B</small>{wall()}</div>
<div class=qs><small class=cap>WHAT USUALLY GOES WRONG</small>{"".join(f'<div class=q><i>{i+1}</i><span>{t}</span></div>' for i,t in enumerate(["Height taken to the ceiling, not the beam","Switchboard hidden behind a panel","Door swing hits the bed","Old photo of the wall, no numbers"]))}</div></div>''',
css=""".w1{flex:1;display:flex;gap:16px;min-height:0}.wc{width:560px;flex:none;padding:16px;display:flex;flex-direction:column;gap:6px}.wl{width:100%;flex:1;min-height:0;display:block}
.qs{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}.q{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:20px;padding:0 18px;font:600 22px/1.35 Inter}
.q i{width:46px;height:46px;border-radius:50%;background:#c0392b;color:#fff;font:800 20px Inter;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}""")

P["p242_wardrobe_s2"] = wb(2, "STEP 1 · MEASURE ON A TABLET", "Every number, with<br><span>the beam and the switch.</span>",
f'''<div class=w2><div class="cd wc2"><small class=cap>WALL B · SAMPLE</small>{wall()}</div><div class="cd fm">{"".join(f'<div class=fr><span>{a}</span><b>{b}</b></div>' for a,b in [("Wall width","9 ft"),("Floor to ceiling","10 ft"),("Floor to beam","9 ft"),("Switchboard","From right 0.5 ft, keep open"),("Bed to wall","3.5 ft · sliding doors?"),("Wall photos","4 added")])}
<div class=nt>The wardrobe height is taken to the beam: <b>9 ft</b>.</div></div></div>''',
css=""".w2{flex:1;display:flex;gap:16px;min-height:0}.wc2{width:520px;flex:none;padding:16px;display:flex;flex-direction:column;gap:6px}.wl{width:100%;flex:1;min-height:0;display:block}
.fm{flex:1;min-width:0;padding:18px 22px;display:flex;flex-direction:column;gap:8px}.fr{flex:1;display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid #ece9e1}.fr span{font:600 17px Inter;color:#7c7f75}.fr b{font:700 25px/1.35 'TeX Gyre Adventor'}
.nt{background:#eef2d6;border-radius:14px;padding:14px 16px;font:600 20px/1.4 Inter}.nt b{color:#6b7d2a}""")

opts = [("A", "Hinged doors", [("door", 135), ("door", 135), ("drawers", 135), ("door", 135)], "Door swing needs 2 ft", False),
        ("B", "Sliding doors", [("slide", 270), ("slide", 270)], "Fits the 3.5 ft gap by the bed", True),
        ("C", "Hinged + loft", [("door", 180), ("door", 180), ("drawers", 180)], "Loft space lost to the beam", False)]
oc = "".join(f'''<div class="cd op{" pk" if pk else ""}"><div class=oh><b>Option {k}</b>{"<em>Customer picked</em>" if pk else ""}</div><svg viewBox="-10 60 560 650" class=ow><rect x="-10" y="60" width="560" height="650" fill="#f4f1ea"/>{wardrobe(c, x0=0, w=540)}</svg><b class=ot>{t}</b><span>{n}</span></div>''' for k, t, c, n, pk in opts)
P["p242_wardrobe_s3"] = wb(3, "STEP 2 · DESIGN APPROVAL", "Show three layouts.<br><span>Get one approved.</span>",
f'''<div class=w3><div class=ops>{oc}</div><div class=nb><span class=ib>{ic("check",26)}</span><span>Approved on the phone with a tap. <b>Option B · oak laminate · Tue 24 Nov.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ops{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;min-height:0}
.op{padding:14px;display:flex;flex-direction:column;gap:8px;border:4px solid transparent}.op.pk{border-color:#6b7d2a}
.oh{display:flex;justify-content:space-between;align-items:center}.oh b{font:700 25px/1.3 'TeX Gyre Adventor'}.oh em{font:700 13px Inter;font-style:normal;background:#6b7d2a;color:#fff;padding:5px 8px;border-radius:8px}
.ow{width:100%;flex:1;min-height:0;display:block}.ot{font:700 24px/1.3 Inter}.op span{font:500 19px/1.35 Inter;color:#7c7f75}""")

cut = [("Side panel", "8.9 × 2 ft", 2), ("Top and bottom", "8.9 × 2 ft", 2), ("Middle divider", "8.6 × 2 ft", 1), ("Shelves", "4.4 × 1.9 ft", 6), ("Sliding shutters", "8.8 × 4.5 ft", 2), ("Back panel", "8.9 × 4.5 ft", 2)]
P["p242_wardrobe_s4"] = wb(4, "STEP 3 · PANEL LIST AND INSTALL DAY", "The panel list comes<br><span>from the approved design.</span>",
f'''<div class=w4><div class="cd cl"><div class=ch><span>PANEL</span><span>SIZE</span><span>QTY</span></div>{"".join(f'<div class=cr><b>{a}</b><span>{b}</span><em>{q}</em></div>' for a,b,q in cut)}</div>
<div class=sd><div class=dy><small class=cap style="color:#d9e59a">INSTALL DAY · SAMPLE</small><b>Sat 5 Dec</b><span>2 fitters · 10 AM</span></div><div class="cd chk"><small class=cap>BEFORE THE TEAM LEAVES</small>{"".join(f'<p>{ic("check",18,w=3)}{t}</p>' for t in ["Panels cut and labelled","Hinges and tracks packed","Switchboard cut-out marked"])}</div></div></div>''',
css=""".w4{flex:1;display:flex;gap:14px;min-height:0}.cl{flex:1;min-width:0;padding:16px 22px;display:flex;flex-direction:column}
.ch,.cr{display:grid;grid-template-columns:1fr 160px 60px;gap:10px;align-items:center}.ch{font:700 14px/1.4 Inter;letter-spacing:2px;color:#7c7f75;padding-bottom:8px;border-bottom:2px solid #2a2f26}
.cr{flex:1;border-bottom:1px solid #ece9e1}.cr b{font:700 22px/1.3 Inter}.cr span{font:500 20px Inter;color:#4f5348}.cr em{font:800 24px 'TeX Gyre Adventor';font-style:normal;color:#6b7d2a;text-align:center}
.sd{width:300px;flex:none;display:flex;flex-direction:column;gap:14px}.dy{background:#2a2f26;color:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:4px}.dy b{font:700 40px/1.3 'TeX Gyre Adventor'}.dy span{font:500 19px Inter;color:#d6d8cf}
.chk{flex:1;padding:16px 18px;display:flex;flex-direction:column;gap:8px}.chk p{flex:1;display:flex;align-items:center;gap:10px;font:600 22px/1.35 Inter;border-top:1px solid #ece9e1}.chk svg{color:#6b7d2a;flex:none}""")

P["p242_wardrobe_s5"] = wb(5, "YOUR TURN", "Make modular wardrobes?<br><span>Let's build your site app.</span>",
f'''<div class=w5><div class="cd hw"><svg viewBox="-10 60 560 650" class=hww><rect x="-10" y="60" width="560" height="650" fill="#f4f1ea"/>{wardrobe([("slide",270),("slide",270)], x0=0, w=540)}</svg></div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,40)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Site measure","Beam and switch included"),("grid","Design options","Approved with a tap"),("box","Panel list","Straight from the design"),("cal","Install day","Team and checklist")])}
<div class=q>How do you take site measurements today? Tell us in the comments.</div></div></div>''',
cta="DM us to start", ctacss="background:#6b7d2a;color:#fff",
css=""".w5{flex:1;display:flex;gap:16px;min-height:0}.hw{width:380px;flex:none;padding:20px;display:flex}.hww{width:100%;height:100%;display:block}
.tl{flex:1;display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:0 20px;box-shadow:0 10px 22px rgba(42,47,38,.07)}
.ti .ib{width:76px;height:76px;border-radius:20px;background:#eef2d6;color:#6b7d2a}.ti b{display:block;font:700 30px/1.3 'TeX Gyre Adventor'}.ti span{font:500 19px/1.35 Inter;color:#6a6e63}
.q{background:#6b7d2a;color:#fff;border-radius:22px;padding:20px 22px;font:700 23px/1.4 Inter}""")

# ───────── 243 INDIA · Pet food home delivery · SINGLE · Poppins + DM Sans · kibble brown / mint / sky blue
# New technique: drawn food bags whose fill level drops by daily grams; the run-out date is computed and becomes the refill reminder.
pets = [("Sample Dog 1", "Labrador · 3 yrs", "10 kg bag", 300, 4.2, "Sun 6 Dec", "#d98b3a", "3 Nov"), ("Sample Cat 1", "Indoor cat · 2 yrs", "3 kg bag", 60, 0.54, "Tue 1 Dec", "#4aa3c7", "12 Oct"), ("Sample Dog 2", "Beagle · 5 yrs", "4 kg bag", 180, 2.9, "Tue 8 Dec", "#7a9e3a", "16 Nov")]
def bag(pct, c):
    y = 60 + (1 - pct) * 210
    return f'''<svg viewBox="0 0 200 300" width="220" height="330"><path d="M30 40 L170 40 L180 290 L20 290 Z" fill="#f3ece0" stroke="#3b2a1d" stroke-width="5"/>
<clipPath id="cb{int(pct*100)}"><path d="M30 40 L170 40 L180 290 L20 290 Z"/></clipPath><g clip-path="url(#cb{int(pct*100)})"><rect x="0" y="{y:.0f}" width="200" height="300" fill="{c}" fill-opacity=".85"/>{"".join(f'<circle cx="{20+(i*37)%170}" cy="{y+20+(i*53)%(290-y if 290-y>30 else 30):.0f}" r="6" fill="#3b2a1d" fill-opacity=".35"/>' for i in range(14))}</g>
<path d="M30 40 L170 40 L160 14 L40 14 Z" fill="#3b2a1d"/><rect x="60" y="150" width="80" height="60" rx="8" fill="#fff" stroke="#3b2a1d" stroke-width="3"/><text x="100" y="188" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="24" fill="#3b2a1d"><tspan>{int(pct*100)}%</tspan></text></svg>'''
P["p243_petfood"] = page("""
body{--f:'DM Sans';--h:'Poppins';background:#eaf6f1;color:#3b2a1d}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#2e8a6b;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#2e8a6b}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bs{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.pc{background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;align-items:center;gap:8px;box-shadow:0 14px 30px rgba(59,42,29,.08)}
.pc .hd{align-self:stretch;display:flex;align-items:center;gap:10px}.pc .hd .ib{width:46px;height:46px;border-radius:50%;color:#fff}
.pc .hd b{display:block;font:700 21px/1.3 Poppins}.pc .hd small{font:500 16px 'DM Sans';color:#7a6a5c}
.pc svg{display:block}
.rw{align-self:stretch;flex:1;display:flex;justify-content:space-between;align-items:center;font:500 20px 'DM Sans';border-top:1px solid #efe7dc}.rw b{font-weight:700}
.ro{align-self:stretch;margin-top:auto;border-radius:14px;padding:10px 12px;text-align:center;font:700 18px/1.35 'DM Sans';background:#eaf6f1;color:#2e8a6b}.ro.soon{background:#ffe8d6;color:#c0581a}
.ms{display:flex;gap:14px;align-items:center;background:#3b2a1d;color:#fff;border-radius:22px;padding:16px 20px}.ms .ib{width:54px;height:54px;border-radius:16px;background:#2e8a6b}
.ms p{flex:1;font:500 21px/1.45 'DM Sans'}.ms p b{color:#ffcf9e}.ms em{font:700 17px 'DM Sans';font-style:normal;background:#ffcf9e;color:#3b2a1d;padding:10px 14px;border-radius:12px;white-space:nowrap}
""", "<div class=kk>PET FOOD HOME DELIVERY · REFILLS</div><h1>The bag runs out,<br>then they call?<br><span>Remind them before.</span></h1>",
f'''<div class=vw><div class=bs>{"".join(f'<div class=pc><div class=hd><span class=ib style="background:{c}">{ic("paw",24)}</span><div><b>{n}</b><small>{d}</small></div></div>{bag(left/ (int(sz.split()[0])), c)}<div class=rw><span>{sz}</span><b>{g} g a day</b></div><div class=rw><span>Left now</span><b>{left} kg</b></div><div class=rw><span>Last delivered</span><b>{ld}</b></div><div class="ro{" soon" if r=="Tue 1 Dec" else ""}">Runs out {r}</div></div>' for n,d,sz,g,left,r,c,ld in pets)}</div>
<div class=ms><span class=ib>{ic("bell",26)}</span><p><b>Sample Cat 1</b> runs out on Tue 1 Dec. Reminder sent today with a one-tap reorder.</p><em>Deliver Mon 30 Nov</em></div></div>''',
"#3b2a1d", "Deliver pet food? DM us", "background:#2e8a6b;color:#fff")

# ───────── 244 USA · Garage floor coating · SINGLE · Anton + Inter · epoxy grey / flake blue / safety yellow
# New technique: top-down garage plan with sq ft grid and a flake colour chip picker that recolours the floor sample.
P["p244_garage"] = page("""
body{--f:'Inter';--h:'Anton';background:#e9ebee;color:#1e2430}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#b08a00;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#2f63c8}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.gp{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(30,36,48,.08)}
.gp>small,.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#6b7280}
.gsv{width:100%;flex:1;min-height:0;display:block}
.rc{width:350px;flex:none;display:flex;flex-direction:column;gap:12px}
.ch{background:#1e2430;color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.ch small{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#ffd23f}
.cg{display:grid;grid-template-columns:1fr 1fr;gap:10px}.cg div{border-radius:14px;padding:8px;background:#2a3140;display:flex;flex-direction:column;gap:6px;border:3px solid transparent}.cg div.on{border-color:#ffd23f}
.cg i{height:62px;border-radius:10px}.cg b{font:600 16px Inter}
.qt{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(30,36,48,.08)}
.qr{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #eceef1;font:500 19px Inter}.qr b{font:700 21px Inter}
.qn{font:600 16px/1.4 Inter;color:#6b7280}
""", "<div class=kk>GARAGE FLOOR COATING · QUOTES</div><h1>“How much for my garage?”<br><span>Size and colour, online.</span></h1>",
f'''<div class=vw><div class=gp><small>SAMPLE 2-CAR GARAGE · TOP VIEW · 22 × 22 FT</small>
<svg viewBox="0 0 560 700" class=gsv><defs><pattern id="fk" width="22" height="22" patternUnits="userSpaceOnUse"><rect width="22" height="22" fill="#7d8594"/><circle cx="4" cy="6" r="2.4" fill="#2f63c8"/><circle cx="15" cy="3" r="1.8" fill="#e6e8ec"/><circle cx="11" cy="14" r="2.2" fill="#1e2430"/><circle cx="19" cy="17" r="2" fill="#2f63c8"/><circle cx="6" cy="19" r="1.6" fill="#e6e8ec"/></pattern></defs>
<rect x="20" y="60" width="520" height="560" fill="url(#fk)" stroke="#1e2430" stroke-width="8"/>
{"".join(f'<line x1="{20+i*520/22:.1f}" y1="60" x2="{20+i*520/22:.1f}" y2="620" stroke="#fff" stroke-opacity=".18" stroke-width="1.5"/>' for i in range(1,22))}{"".join(f'<line x1="20" y1="{60+i*560/22:.1f}" x2="540" y2="{60+i*560/22:.1f}" stroke="#fff" stroke-opacity=".18" stroke-width="1.5"/>' for i in range(1,22))}
<rect x="60" y="610" width="200" height="20" fill="#e9ebee"/><rect x="300" y="610" width="200" height="20" fill="#e9ebee"/>
<g fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="12 10"><rect x="70" y="140" width="180" height="400" rx="40"/><rect x="310" y="140" width="180" height="400" rx="40"/></g>
<rect x="420" y="70" width="110" height="50" fill="#c9cdd4" stroke="#1e2430" stroke-width="3"/><text x="475" y="102" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="#1e2430"><tspan>Shelf</tspan></text>
<g font-family="Anton" font-size="26"><rect x="225" y="8" width="110" height="44" rx="10" fill="#ffd23f"/><text x="280" y="41" text-anchor="middle" fill="#1e2430"><tspan>22 FT</tspan></text>
<rect x="225" y="644" width="110" height="44" rx="10" fill="#1e2430"/><text x="280" y="677" text-anchor="middle" fill="#fff"><tspan>DOORS</tspan></text></g></svg></div>
<div class=rc><div class=ch><small>FLAKE COLOUR · PICK ONE</small><div class=cg>{"".join(f'<div class="{"on" if on else ""}"><i style="background:{bg}"></i><b>{n}</b></div>' for n,bg,on in [("Storm blue","radial-gradient(circle at 20% 30%,#2f63c8 0 3px,transparent 4px) 0 0/16px 16px,radial-gradient(circle at 70% 60%,#e6e8ec 0 2px,transparent 3px) 0 0/14px 14px,#7d8594",True),("Granite","radial-gradient(circle at 20% 30%,#1e2430 0 3px,transparent 4px) 0 0/16px 16px,radial-gradient(circle at 70% 60%,#e6e8ec 0 2px,transparent 3px) 0 0/14px 14px,#a3a8b0",False),("Desert tan","radial-gradient(circle at 20% 30%,#7a5a2e 0 3px,transparent 4px) 0 0/16px 16px,radial-gradient(circle at 70% 60%,#f3ead8 0 2px,transparent 3px) 0 0/14px 14px,#c8b08a",False),("Solid grey","#8f96a3",False)])}</div></div>
<div class=qt><small class=cap>QUOTE REQUEST · SAMPLE</small>{"".join(f'<div class=qr><span>{a}</span><b>{b}</b></div>' for a,b in [("Floor area","484 sq ft"),("Cracks to fill","2 small"),("Flake colour","Storm blue"),("Preferred week","Dec 7")])}<div class=qn>You set the price per sq ft. The quote is ready from these numbers.</div></div></div></div>''',
"#1e2430", "Coat garage floors? DM us", "background:#2f63c8;color:#fff")

# ───────── 245 INDIA · Event photo booth rental · SINGLE · Bitter + Fira Sans · film black / electric blue / cream
# New technique: a 4-frame photo-booth strip used as the booking timeline (one frame = one event), beside a props and prints card.
ev = [("Fri 4 Dec", "Sample office party", "6 PM – 10 PM", "Props: office theme", "#3b6cff"), ("Sat 5 Dec", "Sample wedding reception", "7 PM – 11 PM", "Props: floral frames", "#ff6b4a"), ("Sun 6 Dec", "Sample college fest", "2 PM – 6 PM", "Props: neon signs", "#2ec4b6"), ("Sun 13 Dec", "Open", "Book this date", "", "#3a3a40")]
P["p245_photobooth"] = page("""
body{--f:'Fira Sans';--h:'Bitter';background:#f5f0e6;color:#16161a}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#3b6cff;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:0;line-height:1.22} h1 span{color:#3b6cff}
.vw{flex:1;display:flex;gap:18px;min-height:0}
.strip{width:380px;flex:none;background:#16161a;border-radius:14px;padding:18px 18px 14px;display:flex;flex-direction:column;gap:12px;box-shadow:0 20px 40px rgba(22,22,26,.25)}
.fr{flex:1;border-radius:6px;padding:14px 16px;display:flex;flex-direction:column;justify-content:space-between;color:#fff;position:relative;overflow:hidden}
.fr small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;opacity:.85}.fr b{font:700 24px/1.3 Bitter}.fr span{font:500 17px/1.35 'Fira Sans'}
.fr.op{border:3px dashed #5a5a62;background:transparent!important;color:#b9b9c2}
.sf{font:700 14px/1.4 'Fira Sans';letter-spacing:3px;color:#9a9aa5;text-align:center}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:14px}
.bk{flex:1;background:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(22,22,26,.08)}
.bk small,.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#6f6f78}.bk h4{font:800 30px/1.3 Bitter}
.br{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #efe9dd;font:500 23px 'Fira Sans'}.br b{font:700 24px 'Fira Sans'}
.pp{display:flex;gap:8px;flex-wrap:wrap}.pp span{font:600 18px 'Fira Sans';background:#eef2ff;color:#2a4fd0;padding:7px 12px;border-radius:10px}
.pr{background:#16161a;color:#fff;border-radius:24px;padding:16px 22px;display:flex;align-items:center;gap:16px}
.pr b{font:800 48px/1.3 Bitter;color:#8fa9ff}.pr span{font:500 19px/1.4 'Fira Sans'}
""", "<div class=kk>PHOTO BOOTH RENTAL · EVENT BOOKINGS</div><h1>Booth bookings on chat?<br><span>One strip of dates, clear.</span></h1>",
f'''<div class=vw><div class=strip>{"".join(f'<div class="fr{" op" if n=="Open" else ""}" style="background:linear-gradient(135deg,{c},{c}cc)"><small>{d.upper()}</small><div><b>{n}</b><span style="display:block">{t}</span></div>{f"<span>{p}</span>" if p else ""}</div>' for d,n,t,p,c in ev)}<div class=sf>SAMPLE BOOKINGS · DECEMBER</div></div>
<div class=rc><div class=bk><small>BOOKING PB-245 · SAT 5 DEC</small><h4>Sample wedding reception</h4>{"".join(f'<div class=br><span>{a}</span><b>{b}</b></div>' for a,b in [("Time","7 PM – 11 PM"),("Booth set-up by","6 PM"),("Backdrop","Cream floral"),("Prints","2 per photo"),("Advance","Paid")])}
<small class=cap style="margin-top:6px">PROPS TO PACK</small><div class=pp><span>Floral frames</span><span>Hand boards</span><span>Glasses</span><span>Name sign</span></div></div>
<div class=pr><b>4</b><span>December dates shown here: 3 booked, 1 open for new enquiries.</span></div></div></div>''',
"#16161a", "Rent a photo booth? DM us", "background:#3b6cff;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
