import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 281 INDIA · Pump and motor dealer · SINGLE · Bitter + Fira Sans · water blue / rust red / concrete
# New technique: site cross-section (house, roof tank, borewell, water level, pump depth) drawn to scale with depth ticks.
def section():
    s = 2.6  # px per ft in the bore
    g = 150  # ground y
    ticks = "".join(f'<line x1="250" y1="{g+d*s}" x2="266" y2="{g+d*s}" stroke="#55606a" stroke-width="3"/><text x="274" y="{g+d*s+7}" font-family="Fira Sans" font-weight="600" font-size="22" fill="#55606a">{d} ft</text>' for d in (50, 100, 150, 200))
    return f'''<svg viewBox="0 -110 520 990" class=sec>
<rect x="0" y="-110" width="520" height="{g+110}" fill="#e6f0f6"/>
<rect x="0" y="{g}" width="520" height="730" fill="#d9cdb8"/>
<rect x="0" y="{g+120*s}" width="520" height="{880-g-120*s}" fill="#b8d3e6"/>
<text x="290" y="{g+120*s+36}" font-family="Fira Sans" font-weight="700" font-size="24" fill="#1d5f8c">Water level 120 ft</text>
<rect x="0" y="{g-8}" width="520" height="10" fill="#7a8a5a"/>
<rect x="40" y="40" width="150" height="{g-40}" fill="#f4efe6" stroke="#2e3740" stroke-width="5"/>
<path d="M25 46 L115 0 L205 46" fill="#c0492f" stroke="#2e3740" stroke-width="5" stroke-linejoin="round"/>
<rect x="125" y="6" width="60" height="34" rx="6" fill="#2f7fb8" stroke="#2e3740" stroke-width="4" transform="translate(0,-2)"/>
<rect x="216" y="{g}" width="28" height="{220*s}" fill="#efe7da" stroke="#2e3740" stroke-width="4"/>
<line x1="230" y1="24" x2="230" y2="{g+200*s}" stroke="#2f7fb8" stroke-width="7"/>
<path d="M185 24 H230" stroke="#2f7fb8" stroke-width="7" fill="none"/>
<rect x="219" y="{g+200*s-8}" width="22" height="64" rx="6" fill="#c0492f" stroke="#2e3740" stroke-width="3"/>
{ticks}
<text x="30" y="{g+200*s+34}" font-family="Fira Sans" font-weight="700" font-size="25" fill="#c0492f">Pump at 200 ft</text>
<text x="286" y="{g+220*s-4}" font-family="Fira Sans" font-weight="700" font-size="23" fill="#2e3740">Bore ends 220 ft</text>
<text x="292" y="36" font-family="Fira Sans" font-weight="700" font-size="24" fill="#2e3740">Roof tank, 30 ft up</text>
<text x="292" y="{g-26}" font-family="Fira Sans" font-weight="600" font-size="20" fill="#55606a">Ground</text>
</svg>'''
P["p281_pump"] = page("""
body{--f:'Fira Sans';--h:'Bitter';background:#eceae6;color:#1f2a33}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#c0492f;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#2f7fb8}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.sc{width:470px;flex:none;background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(31,42,51,.08)}
.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#77736d}
.sec{flex:1;min-height:0;width:100%;display:block;border-radius:14px}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.fm{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(31,42,51,.08)}
.fr{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #ece8e1;font:500 19px 'Fira Sans';color:#4d5862}.fr b{font:700 22px 'Fira Sans';color:#1f2a33}
.pk{background:#2f7fb8;color:#fff;border-radius:16px;padding:12px 16px}.pk small{display:block;font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#cfe6f7}.pk b{font:700 24px/1.35 'Bitter'}
.dk{background:#1f2a33;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}
.dk small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#f3b6a6}
.dr{display:flex;justify-content:space-between;font:500 18px/1.4 'Fira Sans';color:#cfd5da}.dr b{color:#fff;font-weight:700}
""", "<div class=kk>PUMP AND MOTOR DEALER · SITE DETAILS</div><h1>Pump sent for the wrong bore?<br><span>Take site details first.</span></h1>",
f'''<div class=vw><div class=sc><small class=cap>SITE S-281 · CROSS SECTION · SAMPLE</small>{section()}</div>
<div class=rc><div class=fm><small class=cap>SITE FORM · FILLED BY THE CUSTOMER</small>{"".join(f'<div class=fr><span>{a}</span><b>{b}</b></div>' for a,b in [("Bore depth","220 ft"),("Water level","120 ft"),("Bore size","6 in"),("Tank height","30 ft"),("Power","Single phase"),("Photos","Bore + panel")])}
<div class=pk><small>PUMP PICKED · SAMPLE</small><b>1 HP submersible</b></div></div>
<div class=dk><small>INSTALL AND SERVICE</small>{"".join(f'<div class=dr><span>{a}</span><b>{b}</b></div>' for a,b in [("Install","Wed 25 Nov · 10 AM"),("Technician","Team 2"),("Service call","Logged on the same site")])}</div></div></div>''',
"#1f2a33", "Sell pumps? DM us", "background:#c0492f;color:#fff")

# ───────── 282 INDIA · Wedding tent lighting contractor · CAROUSEL 6 · Gelasio + Montserrat · midnight indigo / bulb amber / rose
# New technique: glowing string-light catenaries (SVG paths + radial-glow bulbs) as the series motif; split in/out bars per light type.
TL = """
body{--f:'Montserrat';--h:'Gelasio';background:#171a33;color:#f6efe2}
.kk{font:700 16px/1.4 'Montserrat';letter-spacing:3px;color:#f5b942;margin-top:22px;align-self:flex-start}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.25} h1 span{color:#f5b942}
.cd{background:#232750;border-radius:24px;box-shadow:inset 0 0 0 2px #2f3463}
.cap{font:700 14px/1.4 'Montserrat';letter-spacing:2px;color:#a9acd0}
.nb{display:flex;align-items:center;gap:14px;background:#f5b942;color:#171a33;border-radius:20px;padding:16px 20px;font:600 21px/1.4 'Montserrat'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#171a33;color:#f5b942}
"""
def tl(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#f5b942;color:#171a33"):
    return page(TL + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#f6efe2", cta, ctacss, tagline=f"{n} / 6", logo_color="#f6efe2")
def lights(w, h, rows=3, n=11, seed=1):
    out = []
    for r in range(rows):
        y0 = 30 + r * (h - 60) / max(rows - 1, 1) * 0.55
        sag = 40 + r * 14
        pts = []
        for i in range(n):
            t = i / (n - 1); x = 20 + t * (w - 40); y = y0 + sag * 4 * t * (1 - t)
            pts.append((x, y))
        d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts)
        out.append(f'<path d="{d}" fill="none" stroke="#5a5f93" stroke-width="2"/>')
        out += [f'<circle cx="{x:.0f}" cy="{y+10:.0f}" r="18" fill="url(#gl)"/><circle cx="{x:.0f}" cy="{y+10:.0f}" r="6" fill="#ffe3a1"/>' for x, y in pts]
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="display:block"><defs><radialGradient id="gl"><stop offset="0" stop-color="#ffd36b" stop-opacity=".9"/><stop offset="1" stop-color="#ffd36b" stop-opacity="0"/></radialGradient></defs>{"".join(out)}</svg>'
ev = [("Lawn A", "7 PM", [("Fairy strings", 30), ("Bulb strings", 20), ("Par lights", 8)], "Crew 1", "2 PM"),
      ("Hall B", "8 PM", [("Fairy strings", 30), ("Chandeliers", 4), ("Focus lights", 8)], "Crew 2", "3 PM"),
      ("Terrace C", "9 PM", [("Fairy strings", 20), ("Bulb strings", 20), ("Par lights", 4)], "Crew 3", "4 PM")]
P["p282_tentlight_s1"] = tl(1, "WEDDING TENT LIGHTING · CONTRACTOR", "Three events tonight.<br><span>Which lights go where?</span>",
f'''<div class=w1><div class="cd sk"><div class=lt>{lights(880, 330, 3, 13)}</div><div class=tent><div class=tr></div><div class=tb><span>Sample venue · tonight</span></div></div></div>
<div class=chs>{"".join(f'<div class=ch><b>{a}</b><span>Event at {t}</span></div>' for a,t,*_ in ev)}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sk{flex:1;display:flex;flex-direction:column;align-items:center;padding:20px 20px 0;overflow:hidden;background:linear-gradient(#1c1f40,#2a2e5e)}
.lt{flex:none}.tent{flex:1;width:640px;display:flex;flex-direction:column;margin-top:-30px}.tr{height:110px;background:#f6efe2;clip-path:polygon(50% 0,100% 100%,0 100%);opacity:.92}
.tb{flex:1;background:repeating-linear-gradient(90deg,#f6efe2 0 60px,#e9dcc6 60px 120px);display:flex;align-items:center;justify-content:center}.tb span{font:700 20px 'Montserrat';color:#171a33;background:#f5b942;padding:8px 16px;border-radius:10px}
.chs{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.ch{background:#232750;border-radius:20px;padding:16px 20px;box-shadow:inset 0 0 0 2px #2f3463}.ch b{display:block;font:700 30px/1.3 Gelasio;color:#f5b942}.ch span{font:600 18px 'Montserrat';color:#d6d3e8}""")

inv = [("Fairy strings", 120, 80), ("Bulb strings", 60, 40), ("Par lights", 24, 12), ("Focus lights", 16, 8), ("Chandeliers", 6, 4)]
P["p282_tentlight_s2"] = tl(2, "STEP 1 · EVERY LIGHT SET COUNTED", "Know what is out<br><span>before you promise more.</span>",
f'''<div class=w2><div class="cd iv"><div class=ih><span>LIGHT TYPE · SAMPLE</span><span>OUT TONIGHT / IN GODOWN</span></div>{"".join(f'<div class=ir><b>{a}</b><div class=br><i style="width:{o/t*100:.0f}%">{o} out</i><em>{t-o} in</em></div><span>{t} total</span></div>' for a,t,o in inv)}</div>
<div class=nb><span class=ib>{ic("box",26)}</span><span>40 fairy strings are free. A new enquiry for tonight gets a real answer.</span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.iv{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.ih{display:flex;justify-content:space-between;font:700 14px/1.4 'Montserrat';letter-spacing:2px;color:#a9acd0;padding-bottom:10px;border-bottom:2px solid #3a3f73}
.ir{flex:1;display:grid;grid-template-columns:220px 1fr 120px;gap:16px;align-items:center;border-bottom:1px solid #2f3463}.ir:last-child{border:0}
.ir b{font:700 26px/1.3 Gelasio}.ir>span{font:600 18px 'Montserrat';color:#a9acd0;text-align:right}
.br{height:56px;border-radius:14px;background:#2f3463;display:flex;overflow:hidden}.br i{background:#f5b942;color:#171a33;font:800 18px/56px 'Montserrat';font-style:normal;padding-left:14px;white-space:nowrap}.br em{flex:1;font:700 18px/56px 'Montserrat';font-style:normal;color:#d6d3e8;text-align:right;padding-right:14px}""")

P["p282_tentlight_s3"] = tl(3, "STEP 2 · ONE CARD PER EVENT", "Each crew loads<br><span>from its own list.</span>",
f'''<div class=w3>{"".join(f'<div class="cd ec"><div class=eh><b>{a}</b><span>Event {t}</span></div>{"".join(f"<div class=ei><span>{x}</span><b>{q}</b></div>" for x,q in items)}<div class=ef><small>CREW</small><b>{c}</b><small>SETUP STARTS</small><b>{s}</b></div></div>' for a,t,items,c,s in ev)}</div>''',
css=""".w3{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;min-height:0}.ec{padding:18px;display:flex;flex-direction:column;gap:10px}
.eh{border-bottom:2px solid #3a3f73;padding-bottom:10px}.eh b{display:block;font:700 34px/1.3 Gelasio;color:#f5b942}.eh span{font:600 18px 'Montserrat';color:#d6d3e8}
.ei{flex:1;display:flex;flex-direction:column;justify-content:center;background:#2c3060;border-radius:14px;padding:10px 14px}.ei span{font:600 19px/1.3 'Montserrat';color:#d6d3e8}.ei b{font:700 56px/1.3 Gelasio}
.ef{background:#f5b942;color:#171a33;border-radius:14px;padding:12px 14px;display:grid;grid-template-columns:1fr;gap:0}.ef small{font:700 12px/1.4 'Montserrat';letter-spacing:2px;color:#5c4510}.ef b{font:700 24px/1.3 'Montserrat';margin-bottom:4px}""")

# time ribbon 1 PM to 11 PM = 600 min
def pct(h): return (h - 13) / 10 * 100
blocks = [("Crew 1 · Lawn A", [(13.5, 14, "Load", "l"), (14, 17, "Setup", "s"), (17, 18.5, "Test", "t"), (19, 23, "Event on", "e")]),
          ("Crew 2 · Hall B", [(14.5, 15, "Load", "l"), (15, 18, "Setup", "s"), (18, 19.5, "Test", "t"), (20, 23, "Event on", "e")]),
          ("Crew 3 · Terrace C", [(15.5, 16, "Load", "l"), (16, 19, "Setup", "s"), (19, 20.5, "Test", "t"), (21, 23, "Event on", "e")])]
P["p282_tentlight_s4"] = tl(4, "STEP 3 · SETUP TIMES THE CREW CAN SEE", "Lights tested<br><span>before guests arrive.</span>",
f'''<div class=w4><div class="cd rb"><div class=ax>{"".join(f'<span style="left:{pct(h)}%">{(h-12) if h>12 else h} PM</span>' for h in (13,15,17,19,21,23))}</div>
{"".join(f'<div class=rr><b>{c}</b><div class=tk>{"".join(f"<i class={k} style={chr(34)}left:{pct(a)}%;width:{pct(b)-pct(a)}%{chr(34)}>{lab if b-a>=1 else ''}</i>" for a,b,lab,k in bl)}</div></div>' for c,bl in blocks)}
<div class=lgd4>{"".join(f'<span><i class={k}></i>{t}</span>' for k,t in [("l","Load van"),("s","Setup"),("t","Light test"),("e","Event on")])}</div></div>
<div class=nb><span class=ib>{ic("clock",26)}</span><span>Every crew sees its own times on the phone. Take-down starts at 11 PM.</span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rb{flex:1;padding:20px 26px 20px;display:flex;flex-direction:column;gap:12px}
.ax{position:relative;height:28px;margin-left:0}.ax span{position:absolute;transform:translateX(-50%);font:700 16px/1.6 'Montserrat';color:#a9acd0;white-space:nowrap}.ax span:first-child{transform:none}.ax span:last-child{transform:translateX(-100%)}
.rr{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px}.rr b{font:700 26px/1.3 Gelasio}
.tk{position:relative;height:74px;border-radius:14px;background:repeating-linear-gradient(90deg,#2c3060 0 calc(20% - 2px),#3a3f73 calc(20% - 2px) 20%)}
.tk i{position:absolute;top:8px;bottom:8px;border-radius:10px;font:700 17px/58px 'Montserrat';font-style:normal;text-align:center;color:#171a33;overflow:hidden;white-space:nowrap}
.l{background:#a9acd0}.s{background:#f5b942}.t{background:#ef7fa3}.e{background:#7fd1b0}
.lgd4{display:flex;gap:22px;justify-content:center}.lgd4 span{display:flex;align-items:center;gap:8px;font:600 17px 'Montserrat'}.lgd4 i{width:18px;height:18px;border-radius:5px}""")

back = [("Fairy strings", 30, 30, ""), ("Bulb strings", 20, 19, "1 damaged, photo saved"), ("Par lights", 8, 8, "")]
P["p282_tentlight_s5"] = tl(5, "STEP 4 · COUNT BACK NEXT MORNING", "Sent 58, back 57.<br><span>You know which one.</span>",
f'''<div class=w5><div class="cd cb"><div class=chd><b>Lawn A · return check</b><span>Sun 29 Nov · 9 AM · sample</span></div>{"".join(f'<div class="cr{" bad" if s!=r else ""}"><div class=cn><b>{a}</b><span>{n if n else "All back, no damage"}</span></div><div class=nums><div><small>SENT</small><b>{s}</b></div><div><small>BACK</small><b>{r}</b></div></div><i class=tick>{ic("check" if s==r else "x",30)}</i></div>' for a,s,r,n in back)}</div>
<div class=nb><span class=ib>{ic("camera",26)}</span><span>The damaged string is added to the event card, with a photo.</span></div></div>''',
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.cb{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:12px}
.chd b{display:block;font:700 34px/1.3 Gelasio;color:#f5b942}.chd span{font:600 18px 'Montserrat';color:#d6d3e8}
.cr{flex:1;display:flex;align-items:center;gap:20px;background:#2c3060;border-radius:18px;padding:12px 20px}.cr.bad{box-shadow:inset 0 0 0 3px #ef7fa3}
.cn{flex:1}.cn b{display:block;font:700 28px/1.3 Gelasio}.cn span{font:600 18px 'Montserrat';color:#a9acd0}.cr.bad .cn span{color:#ef7fa3}
.nums{display:flex;gap:12px}.nums div{background:#171a33;border-radius:12px;padding:8px 16px;text-align:center;min-width:90px}.nums small{display:block;font:700 12px/1.4 'Montserrat';letter-spacing:2px;color:#a9acd0}.nums b{font:700 34px/1.3 'Montserrat'}
.tick{width:58px;height:58px;border-radius:50%;background:#7fd1b0;color:#171a33;display:flex;align-items:center;justify-content:center;flex:none}.cr.bad .tick{background:#ef7fa3}""")

P["p282_tentlight_s6"] = tl(6, "YOUR TURN", "Light up weddings?<br><span>Let's build your event board.</span>",
f'''<div class=w6><div class="cd sk6">{lights(880, 330, 3, 13)}</div>
<div class=tl6>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("box","Light stock","Out and in, live"),("doc","Event cards","Sets for each crew"),("clock","Setup times","Load, setup, test"),("check","Count back","Damage with photos")])}</div>
<div class=q>How do your crews know which lights to load today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#ef7fa3;color:#171a33",
css=""".w6{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sk6{flex:1;display:flex;align-items:center;justify-content:center;background:linear-gradient(#1c1f40,#2a2e5e)}
.tl6{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#232750;border-radius:22px;padding:20px 22px;box-shadow:inset 0 0 0 2px #2f3463}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#f5b942;color:#171a33}.ti b{display:block;font:700 28px/1.35 Gelasio}.ti div span{font:500 19px/1.35 'Montserrat';color:#d6d3e8}
.q{background:#f6efe2;color:#171a33;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Montserrat'}""")

# ───────── 283 USA · Mobile tire service · SINGLE · Archivo Black + Inter · tire black / teal green / sand · PHONE
# New technique: drawn tire with the size printed along the sidewall (SVG textPath) and a decoder list for each part of the code.
tire = '''<svg viewBox="0 0 440 440" class=tire><defs><path id="arc" d="M80 220 A140 140 0 0 1 360 220"/></defs>
<circle cx="220" cy="220" r="205" fill="#22272b"/>
''' + "".join(f'<rect x="214" y="12" width="12" height="30" rx="3" fill="#3a4147" transform="rotate({a} 220 220)"/>' for a in range(0, 360, 12)) + '''
<circle cx="220" cy="220" r="170" fill="#2c3237"/>
<text font-family="Archivo Black" font-size="34" fill="#f2e7d0" letter-spacing="3"><textPath href="#arc" startOffset="50%" text-anchor="middle">225/65 R17 102H</textPath></text>
<circle cx="220" cy="220" r="112" fill="#c9cfd3" stroke="#8d969c" stroke-width="6"/>
''' + "".join(f'<path d="M220 220 L{220+95*math.cos(math.radians(a)):.0f} {220+95*math.sin(math.radians(a)):.0f}" stroke="#8d969c" stroke-width="18" stroke-linecap="round"/>' for a in range(18, 360, 72)) + '''
<circle cx="220" cy="220" r="30" fill="#6c757b"/></svg>'''
dec = [("225", "Width in mm"), ("65", "Sidewall height, % of width"), ("R", "Radial build"), ("17", "Wheel size in inches"), ("102H", "Load index + speed rating")]
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE MOBILE TIRE CO.</small><b>Book a tire swap</b></div>
<div class=af><small>TIRE SIZE</small><div class=in2>225/65 R17 102H</div></div>
<div class=af><small>SERVICE</small><div class=chs2><span class=on>Swap 4</span><span>Swap 2</span><span>Flat repair</span></div></div>
<div class=af><small>WHERE IS THE CAR?</small><div class=in2>Office lot · ZIP 12345</div></div>
<div class=af><small>TIME WINDOW</small><div class=chs2><span>Tue AM</span><span class=on>Tue PM</span><span>Wed AM</span></div></div>
<div class=af><small>NOTE FOR THE TECH</small><div class=in2>Car is a gray SUV, row C</div></div>
<div class=af><small>SIDEWALL PHOTO</small><div class=up>{ic("camera",22)}<span>1 photo added</span></div></div>
<div class=bk2>Book my swap</div></div>''', 380, 820)
P["p283_tire"] = page("""
body{--f:'Inter';--h:'Archivo Black';background:#efe8da;color:#1c2124}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#1b8a7a;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;letter-spacing:-1px;line-height:1.25;margin-top:16px} h1 span{color:#1b8a7a}
.vw{flex:1;display:flex;gap:20px;min-height:0;align-items:center}
.lc{flex:1;min-width:0;align-self:stretch;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(28,33,36,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#7a7466}
.tire{width:330px;height:330px;display:block;align-self:center;flex:none}
.dl{flex:1;display:flex;flex-direction:column;gap:6px}
.dr{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #eee8dc}
.dr b{font:400 26px/1.4 'Archivo Black';color:#1b8a7a;width:92px;flex:none}.dr span{font:600 19px/1.35 'Inter'}
.ap{flex:1;display:flex;flex-direction:column;gap:12px;padding:8px 18px 20px}
.ah small{display:block;font:700 12px/1.4 'Inter';letter-spacing:2px;color:#1b8a7a}.ah b{display:block;font:400 25px/1.4 'Archivo Black'}
.af small{display:block;font:700 12px/1.4 'Inter';letter-spacing:1.5px;color:#7a7466;margin-bottom:5px}
.in2{border:2px solid #e2ddd2;border-radius:10px;padding:9px 12px;font:700 17px 'Inter'}
.chs2{display:flex;gap:6px}.chs2 span{flex:1;text-align:center;font:700 14px 'Inter';padding:9px 2px;border-radius:9px;border:2px solid #e2ddd2}.chs2 span.on{border-color:#1b8a7a;background:#e1f2ef;color:#126a5d}
.up{display:flex;align-items:center;gap:8px;background:#f4f1ea;border-radius:10px;padding:9px 12px;font:600 15px 'Inter';color:#126a5d}
.bk2{margin-top:auto;background:#1b8a7a;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 18px 'Inter'}
""", "<div class=kk>MOBILE TIRE SERVICE · BOOKING</div><h1>“What size are my tires?”<br><span>Show them where to look.</span></h1>",
f'''<div class=vw><div class=lc><small class=cap>READ THE SIDEWALL · SAMPLE SIZE</small>{tire}<div class=dl>{"".join(f"<div class=dr><b>{a}</b><span>{b}</span></div>" for a,b in dec)}</div></div>{ph}</div>''',
"#1c2124", "Run a mobile tire service? DM us", "background:#1b8a7a;color:#fff")

# ───────── 284 INDIA · Office blazer tailoring · SINGLE · Lora + Inter · navy suiting / chalk stripe / camel
# New technique: drawn blazer with dashed measuring lines (chest, length, sleeve) whose letters match the size sheet columns.
blz = '''<svg viewBox="0 0 400 470" class=blz>
<defs><pattern id="pin" width="18" height="18" patternUnits="userSpaceOnUse"><rect width="18" height="18" fill="#243659"/><rect x="8" width="1.6" height="18" fill="#3a4e78"/></pattern></defs>
<path d="M140 30 L200 70 L260 30 L330 60 L370 400 L325 405 L300 200 L300 440 L100 440 L100 200 L75 405 L30 400 L70 60 Z" fill="url(#pin)" stroke="#0f1830" stroke-width="5" stroke-linejoin="round"/>
<path d="M140 30 L200 70 L172 210 L150 120 Z M260 30 L200 70 L228 210 L250 120 Z" fill="#1a2846" stroke="#0f1830" stroke-width="4" stroke-linejoin="round"/>
<path d="M200 70 L200 440" stroke="#0f1830" stroke-width="3"/>
<circle cx="214" cy="270" r="7" fill="#c89b62"/><circle cx="214" cy="330" r="7" fill="#c89b62"/>
<rect x="240" y="320" width="44" height="8" rx="3" fill="#0f1830"/>
<line x1="104" y1="185" x2="296" y2="185" stroke="#f2c14e" stroke-width="4" stroke-dasharray="10 7"/>
<line x1="112" y1="80" x2="112" y2="436" stroke="#f2c14e" stroke-width="4" stroke-dasharray="10 7" transform="translate(-50,0)"/>
<line x1="332" y1="66" x2="366" y2="392" stroke="#f2c14e" stroke-width="4" stroke-dasharray="10 7"/>
<g font-family="Inter" font-weight="800" font-size="22"><circle cx="200" cy="185" r="19" fill="#f2c14e"/><text x="200" y="193" text-anchor="middle" fill="#0f1830">A</text>
<circle cx="62" cy="260" r="19" fill="#f2c14e"/><text x="62" y="268" text-anchor="middle" fill="#0f1830">B</text>
<circle cx="349" cy="230" r="19" fill="#f2c14e"/><text x="349" y="238" text-anchor="middle" fill="#0f1830">C</text></g></svg>'''
staff = [("E-01", 38, 28, 24, "Mon 11 AM"), ("E-02", 40, 29, 25, "Mon 11 AM"), ("E-03", 36, 27, 23, "Mon 12 PM"), ("E-04", 42, 30, 25, "Mon 12 PM"), ("E-05", 40, 29, 24, "Tue 11 AM"), ("E-06", 44, 30, 26, "Tue 11 AM"), ("E-07", 38, 28, 24, "Tue 12 PM")]
P["p284_blazer"] = page("""
body{--f:'Inter';--h:'Lora';background:#f3efe7;color:#16213b}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#a5763d;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#a5763d}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.bc{width:380px;flex:none;background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(22,33,59,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#7a7364}
.blz{flex:1;min-height:0;width:100%;display:block}
.ky{display:flex;flex-direction:column;gap:6px}.ky span{display:flex;align-items:center;gap:10px;font:600 18px 'Inter'}.ky i{width:30px;height:30px;border-radius:50%;background:#f2c14e;font:800 16px/30px 'Inter';font-style:normal;text-align:center;flex:none}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.ss{flex:1;background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(22,33,59,.08)}
.th,.tr{display:grid;grid-template-columns:76px repeat(3,1fr) 130px;gap:8px;align-items:center}
.th{font:700 14px/1.4 'Inter';letter-spacing:1px;color:#7a7364;padding-bottom:8px;border-bottom:2px solid #16213b}.th i{display:inline-block;width:22px;height:22px;border-radius:50%;background:#f2c14e;color:#16213b;font:800 13px/22px 'Inter';font-style:normal;text-align:center;margin-right:4px}
.tr{flex:1;border-bottom:1px solid #ece7dc}.tr:last-child{border:0}.tr b{font:700 20px 'Lora'}.tr span{font:700 22px 'Inter'}.tr em{font:600 15px 'Inter';font-style:normal;background:#f1e6d6;color:#7d5426;border-radius:8px;padding:5px 8px;text-align:center}
.dk{background:#16213b;color:#fff;border-radius:24px;padding:16px 20px;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.dk div small{display:block;font:700 13px/1.4 'Inter';letter-spacing:2px;color:#e3c08e}.dk div b{font:700 26px/1.3 'Lora'}
""", "<div class=kk>BLAZER TAILORING FOR OFFICES · SIZE SHEETS</div><h1>Blazers for the whole office?<br><span>One size sheet, no mix-ups.</span></h1>",
f'''<div class=vw><div class=bc><small class=cap>HOW WE MEASURE · INCHES</small>{blz}<div class=ky>{"".join(f"<span><i>{k}</i>{t}</span>" for k,t in [("A","Chest, all round"),("B","Blazer length"),("C","Sleeve length")])}</div></div>
<div class=rc><div class=ss><div class=th><span>STAFF</span><span><i>A</i>CHEST</span><span><i>B</i>LENGTH</span><span><i>C</i>SLEEVE</span><span>TRIAL</span></div>
{"".join(f'<div class=tr><b>{c}</b><span>{a}</span><span>{b}</span><span>{s}</span><em>{t}</em></div>' for c,a,b,s,t in staff)}</div>
<div class=dk>{"".join(f"<div><small>{a}</small><b>{b}</b></div>" for a,b in [("STAFF","7 of 7"),("TRIALS","Mon + Tue"),("DELIVERY","Sat 5 Dec")])}</div></div></div>''',
"#16213b", "Stitch office blazers? DM us", "background:#a5763d;color:#fff")

# ───────── 285 USA · Adult tutoring center · SINGLE · Crimson Text + Source Sans 3 · oxblood / paper / navy
# New technique: stacked index cards (offset backs peeking above) as a session history, with a ruled front card.
P["p285_tutor"] = page("""
body{--f:'Source Sans 3';--h:'Crimson Text';background:#f4eee4;color:#1d2846}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#8c2f39;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:68px;line-height:1.2} h1 span{color:#8c2f39}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.stk{flex:1;min-width:0;display:flex;flex-direction:column;position:relative}
.bk{height:38px;margin:0 36px;border-radius:14px 14px 0 0;background:#e3d6c3;border:2px solid #cdbda5;border-bottom:0;padding:6px 18px;font:700 15px/1.6 'Source Sans 3';color:#6b5b45}
.bk.b2{margin:0 18px;background:#ece1cf}
.fc{flex:1;background:#fffdf8;border-radius:16px;border:2px solid #d8cbb6;padding:20px 26px 18px;display:flex;flex-direction:column;background-image:repeating-linear-gradient(180deg,transparent 0 47px,#d6e2f0 47px 49px);background-position:0 112px;box-shadow:0 16px 30px rgba(29,40,70,.10);border-top:6px solid #8c2f39}
.fh{display:flex;justify-content:space-between;align-items:baseline;background:#fffdf8;padding-bottom:10px}.fh b{font:700 34px/1.3 'Crimson Text'}.fh span{font:700 16px 'Source Sans 3';color:#8c2f39}
.fl2{flex:1;display:flex;flex-direction:column;justify-content:space-around}
.ln{display:flex;gap:12px;align-items:baseline;font:500 22px/1.35 'Source Sans 3'}.ln small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#8c2f39;width:110px;flex:none}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.cd{background:#fff;border-radius:24px;padding:16px 20px;box-shadow:0 14px 30px rgba(29,40,70,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7a7364}
.pg2{flex:1;display:flex;flex-direction:column;gap:8px}
.tp{flex:1;display:flex;align-items:center;gap:12px;font:600 19px/1.3 'Source Sans 3';border-top:1px solid #efe8dc}
.tp i{width:30px;height:30px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;border:3px solid #cdbda5}
.tp.d i{background:#1d2846;border-color:#1d2846;color:#fff}.tp.n i{border-color:#8c2f39;background:#f6dfe1}
.wk{background:#1d2846;color:#fff}.wk small{display:block;font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#e8b4ba;margin-bottom:8px}
.dy{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}.dy span{text-align:center;border-radius:10px;padding:8px 0;font:700 15px/1.3 'Source Sans 3';background:#2b3961;color:#aeb8d6}.dy span.on{background:#e8b4ba;color:#1d2846}
.wk b{display:block;font:700 24px/1.3 'Crimson Text';margin-top:10px}
""", "<div class=kk>TUTORING CENTER FOR ADULT LEARNERS</div><h1>Busy adults miss sessions.<br><span>Their progress shouldn't slip.</span></h1>",
f'''<div class=vw><div class=stk><div class="bk">Session 4 · Tue 10 Nov</div><div class="bk b2">Session 5 · Tue 17 Nov</div>
<div class=fc><div class=fh><b>Session 6 · Thu 19 Nov</b><span>SAMPLE LEARNER</span></div><div class=fl2>
{"".join(f'<div class=ln><small>{a}</small><span>{b}</span></div>' for a,b in [("SUBJECT","Math refresher"),("TODAY","Fractions and percents"),("WENT WELL","Word problems with money"),("PRACTICE","Worksheet 6, about 20 minutes"),("NEXT TIME","Ratios, then a short quiz")])}</div></div></div>
<div class=sd><div class="cd pg2"><small class=cap>MATH REFRESHER PLAN</small>{"".join(f'<div class="tp {k}"><i>{ic("check",16) if k=="d" else ""}</i><span>{t}</span></div>' for t,k in [("Whole numbers","d"),("Decimals","d"),("Fractions","d"),("Percents","n"),("Ratios",""),("Short quiz","")])}</div>
<div class="cd wk"><small>BOOK NEXT SESSION</small><div class=dy>{"".join(f'<span class={"on" if d=="Tue" else ""}>{d}</span>' for d in ["Mon","Tue","Wed","Thu","Fri"])}</div><b>Tue 24 Nov · 6:30 PM</b></div></div></div>''',
"#1d2846", "Run a tutoring center? DM us", "background:#8c2f39;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
