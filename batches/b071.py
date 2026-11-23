import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 371 INDIA · JCB / earthmover rental · SINGLE · Anton + Inter · excavator yellow / soil brown / sky white
# New technique: CSS odometer hour meters (digit drums with a red tenths drum) for start and end photos; the hours,
# the machine table and the week bill are all computed from the same meter readings.
def odo(v, big=True):
    s = f"{v:07.1f}".replace(".", "")
    return '<div class="od1' + (' bg' if big else '') + '">' + "".join(f'<i class="{"t" if k == len(s) - 1 else ""}">{c}</i>' for k, c in enumerate(s)) + '<em>hrs</em></div>'
M1 = [("Backhoe 1", "Plot 14, Ring Road", "Op. Sample A", 4218.5, 4226.0),
      ("Backhoe 2", "Farm pond, Sample Village", "Op. Sample B", 3120.0, 3126.5),
      ("Excavator", "Society drain line", "Op. Sample C", 6841.0, 6849.5)]
WK1 = [("Mon", 6.0), ("Tue", 8.5), ("Wed", 7.0), ("Thu", 0), ("Fri", 7.5), ("Sat", 7.5)]
TOT1 = sum(h for _, h in WK1)
P["p371_jcb"] = page("""
body{--f:'Inter';--h:'Anton';background:#f6f3ea;color:#231c14}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#8a5a1c;margin-top:22px;margin-bottom:6px}
h1{font-family:'Anton';font-weight:400;font-size:68px;line-height:1.25;letter-spacing:.5px;text-transform:uppercase;margin-top:30px} h1 span{color:#d99a00}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.mt1{background:#231c14;color:#fff;border-radius:26px;padding:20px 24px;display:grid;grid-template-columns:1fr 1fr auto;gap:18px;align-items:center}
.mt1 small,.tb1 small,.wk1 small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#cdb68f}
.mt1 .ph{display:flex;flex-direction:column;gap:10px;background:rgba(255,255,255,.06);border-radius:18px;padding:14px 16px}
.mt1 .ph span{font:500 15px/1.3 Inter;color:#e6dccb}
.od1{display:flex;gap:4px;align-items:center}.od1 i{width:34px;height:50px;border-radius:6px;background:linear-gradient(#0d0d0d,#3a3a3a 50%,#0d0d0d);color:#fff;font:700 30px/50px Inter;font-style:normal;text-align:center}
.od1 i.t{background:linear-gradient(#7a0f0f,#c62828 50%,#7a0f0f)}.od1 em{font:600 15px/1 Inter;font-style:normal;color:#cdb68f;margin-left:6px}
.mt1 .rs{background:#ffc21a;color:#231c14;border-radius:20px;padding:14px 18px;text-align:center}.mt1 .rs b{display:block;font:400 52px/1.35 Anton;margin-bottom:4px}.mt1 .rs span{font:700 15px/1.3 Inter}
.tb1{flex:1;background:#fff;border-radius:24px;padding:16px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(35,28,20,.08);min-height:0}.tb1 small{color:#8a7a60}
.tb1>div{flex:1;display:grid;grid-template-columns:1.1fr 1.6fr 1.2fr .7fr;gap:12px;align-items:center;border-top:1px solid #efe9dc}
.tb1 b{font:700 19px/1.3 Inter}.tb1 span{font:500 16px/1.35 Inter;color:#5d5446}.tb1 .sm .od1 i{width:20px;height:30px;font-size:17px;line-height:30px;border-radius:4px}.tb1 .sm .od1 em{display:none}.tb1 .sm{display:flex;flex-direction:column;gap:4px}
.tb1 .hr{justify-self:end;font:400 30px/1.3 Anton;color:#8a5a1c}
.bt1{display:grid;grid-template-columns:1.3fr 1fr;gap:14px}
.wk1{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(35,28,20,.08)}.wk1 small{color:#8a7a60}
.br1{flex:1;display:grid;grid-template-columns:repeat(6,1fr);gap:10px;align-items:end;min-height:150px}.br1>div{display:flex;flex-direction:column;align-items:center;gap:4px;height:100%;justify-content:flex-end}
.br1 i{width:100%;border-radius:8px 8px 3px 3px;background:#ffc21a}.br1 i.z{background:repeating-linear-gradient(-45deg,#e9e2d3 0 5px,#f6f3ea 5px 10px);height:20px}
.br1 b{font:700 16px/1.3 Inter}.br1 span{font:500 14px/1.3 Inter;color:#5d5446}
.ms1{background:#e8f5e4;border:2px solid #c3e2bb;border-radius:22px 22px 22px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}
.ms1 small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#2f6b2a}.ms1 p{font:500 18px/1.45 Inter;color:#1f3a1c;text-wrap:pretty}.tg1{display:flex;gap:8px;flex-wrap:wrap}.tg1 span{font:600 15px/1.3 Inter;background:#fff;border-radius:10px;padding:6px 10px;color:#2f6b2a}.ms1 em{margin-top:auto;font:600 14px/1.4 Inter;font-style:normal;color:#2f6b2a}
""", "<div class=kk>JCB AND EARTHMOVER RENTAL · HOURLY BILLING</div><h1>Hours argued at billing?<br><span>Photo the hour meter. Twice.</span></h1>",
f'''<div class=vw><div class=mt1><div class=ph><small>START PHOTO · 8:05 AM</small>{odo(M1[0][3])}<span>{M1[0][0]} · {M1[0][1]}</span></div>
<div class=ph><small>END PHOTO · 6:10 PM</small>{odo(M1[0][4])}<span>Photos saved with time and site</span></div><div class=rs><b>{M1[0][4] - M1[0][3]:g}</b><span>hours to bill</span></div></div>
<div class=tb1><small>TODAY · 3 MACHINES · SAMPLE</small>{"".join(f'<div><div><b>{m}</b><br><span>{op}</span></div><span>{site}</span><div class=sm>{odo(a, False)}{odo(b, False)}</div><b class=hr>{b - a:g} h</b></div>' for m, site, op, a, b in M1)}</div>
<div class=bt1><div class=wk1><small>PLOT 14 · THIS WEEK · {pl(TOT1, "HOUR", "HOURS")}</small><div class=br1>{"".join(f'<div><b>{f"{h:g}" if h else "Off"}</b><i class="{"z" if not h else ""}" style="height:{h / 9 * 120 if h else 16:.0f}px"></i><span>{d}</span></div>' for d, h in WK1)}</div></div>
<div class=ms1><small>AUTO MESSAGE · 6:12 PM</small><p>Plot 14 today: {M1[0][4] - M1[0][3]:g} hours (meter {M1[0][3]:,} to {M1[0][4]:,}). Both photos attached.</p><div class=tg1><span>Start 8:05 AM</span><span>End 6:10 PM</span><span>Backhoe 1</span></div><em>Week bill ready with every day's photos.</em></div></div></div>''',
"#231c14", "Rent out machines? DM us", "background:#231c14;color:#ffc21a")

# ───────── 372 CANADA · Ice dam removal (roof steaming) · SINGLE · Crimson Text + Fira Sans · icicle blue / roof charcoal / alarm red
# New technique: SVG house cross-section (warm attic glow, snow layer, ice dam ridge, icicles, water arrow under the
# shingles) with numbered callouts; the request queue is sorted by "water inside" first and split into crew days.
REQ2 = [("R-31", "2-storey", True, "Maple Cres"), ("R-32", "Bungalow", False, "Birch St"), ("R-33", "Bungalow", True, "Cedar Ave"),
        ("R-34", "2-storey", False, "Pine Rd"), ("R-35", "Split-level", True, "Oak Dr"), ("R-36", "Bungalow", False, "Elm St"), ("R-37", "2-storey", False, "Spruce Ln"), ("R-38", "Bungalow", False, "Ash Ct"), ("R-39", "2-storey", True, "Willow Way")]
Q2 = sorted(REQ2, key=lambda r: (not r[2], r[0]))
CAP2 = 3
DAYS2 = [("Today", Q2[:CAP2]), ("Tomorrow", Q2[CAP2:2 * CAP2]), ("Thursday", Q2[2 * CAP2:])]
def house2():
    ic_ = "".join(f'<path d="M{x} 262 l6 0 l-3 {h} z" fill="#bfe3f7" stroke="#8cc3e3" stroke-width="1"/>' for x, h in [(88, 34), (104, 22), (120, 44), (138, 28), (154, 38), (172, 18), (188, 30)])
    return f'''<svg viewBox="30 -130 530 530" preserveAspectRatio="xMidYMax meet" style="width:100%;height:100%;display:block">
<rect x="0" y="-170" width="560" height="570" fill="#dfeaf3"/><circle cx="87" cy="-63" r="4" fill="#fff"/><circle cx="407" cy="29" r="5" fill="#fff"/><circle cx="241" cy="-32" r="5" fill="#fff"/><circle cx="417" cy="-77" r="5" fill="#fff"/><circle cx="405" cy="-23" r="3" fill="#fff"/><circle cx="244" cy="-74" r="5" fill="#fff"/><circle cx="63" cy="-54" r="4" fill="#fff"/><circle cx="464" cy="-107" r="4" fill="#fff"/><circle cx="85" cy="-35" r="3" fill="#fff"/><circle cx="308" cy="-29" r="5" fill="#fff"/><circle cx="59" cy="-4" r="4" fill="#fff"/><circle cx="187" cy="-22" r="4" fill="#fff"/><circle cx="162" cy="-15" r="4" fill="#fff"/><circle cx="375" cy="-47" r="4" fill="#fff"/><circle cx="353" cy="17" r="5" fill="#fff"/><circle cx="144" cy="-34" r="4" fill="#fff"/><circle cx="513" cy="36" r="4" fill="#fff"/><circle cx="128" cy="6" r="3" fill="#fff"/><circle cx="71" cy="-96" r="4" fill="#fff"/><circle cx="264" cy="-95" r="4" fill="#fff"/><circle cx="87" cy="-73" r="4" fill="#fff"/><circle cx="81" cy="3" r="4" fill="#fff"/><circle cx="71" cy="28" r="4" fill="#fff"/><circle cx="332" cy="-10" r="3" fill="#fff"/><circle cx="111" cy="17" r="5" fill="#fff"/><circle cx="536" cy="-90" r="4" fill="#fff"/><circle cx="283" cy="-25" r="4" fill="#fff"/><circle cx="78" cy="-90" r="4" fill="#fff"/><circle cx="382" cy="-31" r="5" fill="#fff"/><circle cx="235" cy="-50" r="3" fill="#fff"/><circle cx="450" cy="18" r="4" fill="#fff"/><circle cx="505" cy="-73" r="3" fill="#fff"/><circle cx="265" cy="-107" r="3" fill="#fff"/><circle cx="378" cy="17" r="3" fill="#fff"/><circle cx="346" cy="-106" r="4" fill="#fff"/><circle cx="152" cy="-56" r="3" fill="#fff"/><circle cx="215" cy="2" r="3" fill="#fff"/><circle cx="231" cy="-60" r="3" fill="#fff"/><circle cx="321" cy="17" r="3" fill="#fff"/><circle cx="245" cy="-84" r="5" fill="#fff"/>
<polygon points="300,60 560,200 560,400 300,400" fill="#f6efe2"/>
<polygon points="300,60 80,262 210,262 300,180 520,180 560,200" fill="none"/>
<polygon points="210,262 300,178 560,320 560,400 210,400" fill="#fff4d6"/>
<radialGradient id="wa2"><stop offset="0" stop-color="#ffcf6b" stop-opacity=".75"/><stop offset="1" stop-color="#ffcf6b" stop-opacity="0"/></radialGradient>
<ellipse cx="380" cy="270" rx="150" ry="90" fill="url(#wa2)"/>
<polygon points="300,52 64,262 82,272 300,74 560,210 560,190" fill="#2b2f36"/>
<path d="M300 40 C230 92 170 150 96 218 L110 228 C180 166 240 110 300 62 Z" fill="#fff" stroke="#d5e3ee" stroke-width="2"/>
<path d="M70 252 C82 226 104 214 122 226 L128 242 L90 266 Z" fill="#9fd2f0" stroke="#6eb2dc" stroke-width="2"/>
{ic_}
<rect x="60" y="262" width="150" height="10" fill="#7a818c"/>
<rect x="210" y="262" width="12" height="138" fill="#d9cdb8"/>
<path d="M170 196 Q140 222 128 240" fill="none" stroke="#d64032" stroke-width="5" stroke-linecap="round" marker-end="url(#ar2)"/>
<marker id="ar2" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#d64032"/></marker>
<path d="M140 250 C150 280 160 300 230 320" fill="none" stroke="#d64032" stroke-width="4" stroke-dasharray="8 7"/>
<circle cx="238" cy="324" r="9" fill="#d64032"/>
{"".join(f'<text x="{x}" y="{y}" text-anchor="{an}" font-family="Fira Sans" font-weight="700" font-size="{fs}" fill="{c}">{t}</text>' for t, x, y, an, c, fs in [("Warm attic melts the snow", 400, 250, "middle", "#8a5a00", 20), ("Snow", 150, 120, "middle", "#2f78ad", 20), ("Ice dam", 40, 206, "start", "#2f78ad", 20), ("Icicles", 70, 330, "start", "#2f78ad", 20), ("Water backs up and", 250, 356, "start", "#d64032", 19), ("leaks inside", 250, 380, "start", "#d64032", 19)])}
</svg>'''
P["p372_icedam"] = page("""
body{--f:'Fira Sans';--h:'Crimson Text';background:#f3f7fa;color:#1e242c}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#2f78ad;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#d64032}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp2{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:14px;min-height:0}
.hs2{background:#fff;border-radius:26px;padding:16px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(30,36,44,.08);min-height:0}
.hs2 small,.lg2 small,.qu2 small{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#5e6b78}
.sv2{flex:1;min-height:0;border-radius:16px;overflow:hidden}
.lg2{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(30,36,44,.08)}
.lg2>div{flex:1;display:flex;gap:12px;align-items:center;border-top:1px solid #e8eef3}
.lg2 i{width:32px;height:32px;flex:none;border-radius:50%;background:#2b2f36;color:#fff;font:700 16px/32px 'Fira Sans';font-style:normal;text-align:center}
.lg2 b{display:block;font:600 18px/1.3 'Fira Sans'}.lg2 span{font:400 15px/1.35 'Fira Sans';color:#5e6b78}
.qu2{background:#1e242c;color:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}.qu2 small{color:#9fb4c6}
.dy2{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.dy2>div{background:rgba(255,255,255,.07);border-radius:18px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.dy2 h3{font:700 24px/1.25 'Crimson Text'}
.rq2{display:flex;justify-content:space-between;align-items:center;gap:8px;background:rgba(255,255,255,.08);border-radius:12px;padding:8px 10px}
.rq2 b{font:600 16px/1.3 'Fira Sans'}.rq2 span{display:block;font:400 13px/1.3 'Fira Sans';color:#b7c6d3}.rq2 em{font:700 13px/1.2 'Fira Sans';font-style:normal;border-radius:8px;padding:5px 8px;background:#3a4450;color:#d6e3ee;white-space:nowrap}
.rq2.lk{box-shadow:inset 4px 0 0 #d64032}.rq2.lk em{background:#d64032;color:#fff}
""", "<div class=kk>ICE DAM REMOVAL · WINTER CALLS</div><h1>Water dripping inside?<br><span>Book the leaks first.</span></h1>",
f'''<div class=vw><div class=tp2><div class=hs2><small>WHY IT LEAKS · SAMPLE DRAWING</small><div class=sv2>{house2()}</div></div>
<div class=lg2><small>WHAT THE BOOKING FORM ASKS</small>{"".join(f'<div><i>{n}</i><div><b>{a}</b><span>{b}</span></div></div>' for n, a, b in [(1, "Water inside?", "Yes jumps to the top of the list"), (2, "Photo of the roof", "From the street is enough"), (3, "Ice at the roof edge", "Thick ridge or only icicles"), (4, "Gutter and downspout", "Frozen or clear"), (5, "Home type and address", "Bungalow, 2-storey, split-level")])}</div></div>
<div class=qu2><small>STEAM CREW · {CAP2} ROOFS A DAY · LEAKS FIRST · SAMPLE</small><div class=dy2>{"".join(f'<div><h3>{d}</h3>{"".join(f"<div class={chr(34)}rq2 {(chr(108) + chr(107)) if r[2] else ''}{chr(34)}><div><b>{r[0]} · {r[3]}</b><span>{r[1]}</span></div><em>{'Leak inside' if r[2] else 'Icicles'}</em></div>" for r in rs)}</div>' for d, rs in DAYS2)}</div></div></div>''',
"#1e242c", "Do winter roof work? DM us", "background:#d64032;color:#fff")


# ───────── 373 INDIA · Saree pre-pleating and box folding · SINGLE · Cardo + Poppins · rani pink / marigold / ivory
# New technique: CSS pre-pleated saree "boxes" (pleat bands from repeating-linear-gradient + pallu fold triangle) per
# order, grouped on an event-date board; phone (1 of 3 this batch) shows the WhatsApp-style order form.
OR3 = [("O-21", "Fri 28 Nov", "Silk", "#b0124f", "#e8a317", 1, "Ready"), ("O-22", "Fri 28 Nov", "Georgette", "#2f6f6a", "#f1d9a6", 2, "Ready"),
       ("O-23", "Sat 29 Nov", "Cotton", "#e2622e", "#fff3d6", 1, "Pleating"), ("O-24", "Sat 29 Nov", "Silk", "#5a2a82", "#e8a317", 3, "Pleating"),
       ("O-25", "Sun 30 Nov", "Chiffon", "#d9467a", "#ffe1ec", 1, "Received"), ("O-26", "Sun 30 Nov", "Silk", "#1f4f8f", "#e8c35a", 2, "Received")]
def sar3(c, b):
    return f'<div class=sa3><i class=pl style="background:repeating-linear-gradient(90deg,{c} 0 12px,rgba(0,0,0,.18) 12px 14px,{c} 14px 26px);box-shadow:inset 0 -8px 0 {b}"></i><i class=pa style="background:linear-gradient(135deg,{c} 50%,{b} 50%)"></i></div>'
DATES3 = list(dict.fromkeys(o[1] for o in OR3))
RB3 = {"Fri 28 Nov": "Thu 27", "Sat 29 Nov": "Fri 28", "Sun 30 Nov": "Sat 29"}
NS3 = sum(o[5] for o in OR3)
P["p373_saree"] = page("""
body{--f:'Poppins';--h:'Cardo';background:#fbf5ea;color:#2a1620}
.kk{font:600 15px/1.4 Poppins;letter-spacing:3px;color:#b0124f;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:64px;line-height:1.2} h1 span{color:#b0124f;font-style:italic}
.vw{flex:1;display:flex;gap:22px;align-items:stretch;min-height:0}
.ap3{flex:1;display:flex;flex-direction:column;gap:9px;padding:6px 14px 14px;background:#f3ece3}
.ah3{display:flex;gap:10px;align-items:center;background:#2a1620;color:#fff;margin:0 -14px;padding:10px 14px}.ah3 i{width:36px;height:36px;border-radius:50%;background:#e8a317;font:700 16px/36px Poppins;font-style:normal;text-align:center;color:#2a1620}
.ah3 b{display:block;font:600 15px/1.3 Poppins}.ah3 small{font:400 11px/1.3 Poppins;color:#d8c8cf}
.fq3{background:#fff;border-radius:14px;padding:9px 12px}.fq3 small{display:block;font:500 11.5px/1.3 Poppins;color:#8b7680}.fq3 b{font:600 15px/1.35 Poppins}
.ch3{display:flex;gap:6px;flex-wrap:wrap;margin-top:4px}.ch3 i{font:500 12.5px/1.2 Poppins;font-style:normal;border:1.5px solid #e3d5dc;border-radius:10px;padding:5px 8px}.ch3 i.on{background:#b0124f;border-color:#b0124f;color:#fff}
.bt3{margin-top:auto;background:#b0124f;color:#fff;border-radius:14px;padding:12px;text-align:center;font:600 15px/1.3 Poppins}
.rt3{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.bd3{flex:1;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(42,22,32,.08);min-height:0}
.bd3>small,.su3 small{font:600 12.5px/1.4 Poppins;letter-spacing:2px;color:#8b7680}
.dt3{flex:1;display:flex;flex-direction:column;gap:6px;border-top:1px solid #f0e6ea;padding-top:6px;min-height:0}.dt3>b{font:700 22px/1.3 Cardo}.dt3>b span{font:500 14px/1.3 Poppins;color:#8b7680;margin-left:8px}
.dt3>div{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.oc3{display:flex;gap:14px;align-items:center;background:#fbf5ea;border-radius:14px;padding:8px 10px}
.sa3{width:100px;height:96px;position:relative;flex:none}.sa3 .pl{position:absolute;left:0;bottom:0;width:100px;height:76px;border-radius:8px}
.sa3 .pa{position:absolute;right:0;top:0;width:46px;height:46px;border-radius:6px}
.oc3 b{display:block;font:600 16px/1.5 Poppins}.oc3 span{display:block;white-space:nowrap;font:400 14px/1.5 Poppins;color:#6f5b65}
.oc3 em{display:inline-block;margin-top:3px;font:600 13px/1.2 Poppins;font-style:normal;border-radius:7px;padding:3px 7px}.oc3 em.Ready{background:#e2f4e5;color:#226b30}.oc3 em.Pleating{background:#fff1cf;color:#8a5a00}.oc3 em.Received{background:#f1e6ec;color:#7a1e4a}
.su3{background:#2a1620;color:#fff;border-radius:22px;padding:14px 18px;display:grid;grid-template-columns:auto 1fr;gap:4px 16px;align-items:center}.su3 small{grid-column:1 / 3;color:#d8c8cf}
.su3 b{font:700 44px/1.2 Cardo;color:#f2b84b}.su3 p{font:400 16px/1.45 Poppins;color:#f1e6ea}
""", "<div class=kk>SAREE PRE-PLEATING · BOX FOLDING</div><h1>Sarees for the big day?<br><span>Book pleating by event date.</span></h1>",
f'''{phone(f"""<div class=ap3><div class=ah3><i>S</i><div><b>Sample Saree Studio</b><small>Order form · sample</small></div></div>
<div class=fq3><small>Event date</small><b>Saturday, 29 November</b></div>
<div class=fq3><small>Saree fabric</small><div class=ch3><i>Cotton</i><i class=on>Silk</i><i>Georgette</i><i>Chiffon</i></div></div>
<div class=fq3><small>How many sarees?</small><b>3</b></div>
<div class=fq3><small>Your height and pleat width</small><b>5 ft 3 in · 5 inch pleats</b></div>
<div class=fq3><small>Fall and pico done?</small><div class=ch3><i class=on>Yes</i><i>Please add</i></div></div>
<div class=fq3><small>Pickup</small><div class=ch3><i class=on>Home pickup</i><i>Drop at studio</i></div></div>
<div class=fq3><small>Delivery</small><b>Friday, 28 November, evening</b></div>
<div class=bt3>Book pleating</div></div>""", w=360, h=800, style="align-self:center")}
<div class=rt3><div class=bd3><small>ORDERS BY EVENT DATE · SAMPLE</small>{"".join(f'<div class=dt3><b>{d}<span>ready by {RB3[d]}</span></b><div>{"".join(f"<div class=oc3>{sar3(o[3], o[4])}<div><b>{o[0]}</b><span>{o[2]} · {pl(o[5], chr(115) + 'aree')}</span><em class={o[6]}>{o[6]}</em></div></div>" for o in OR3 if o[1] == d)}</div></div>' for d in DATES3)}</div>
<div class=su3><small>THIS WEEKEND</small><b>{NS3}</b><p>sarees to pleat for {len(OR3)} orders. Each one is ready one day before its event.</p></div></div>''',
"#2a1620", "Pleat sarees? DM us", "background:#b0124f;color:#fff")


# ───────── 374 INDIA · Printer cartridge refill and service for offices · CAROUSEL 5 · Lora + Open Sans · toner black / CMYK accents / paper white
# New techniques: CSS laser printer with a half-printed sheet and LCD "toner low", CMYK registration strip as a
# section divider, pages-since-refill bars vs cartridge yield (computed due list), SVG signature on a job sheet.
PR4 = [("Office A, 1st floor", "Laser, mono", "SAMPLE-12A", "2 Oct", 1600, 1490),
       ("Office A, 2nd floor", "Laser, mono", "SAMPLE-12A", "18 Oct", 1600, 820),
       ("Clinic front desk", "Ink tank, colour", "SAMPLE-INK4", "9 Sep", 4000, 3550),
       ("School office", "Laser, mono", "SAMPLE-88A", "25 Oct", 1500, 610),
       ("CA office", "Laser, mono", "SAMPLE-88A", "30 Sep", 1500, 1395),
       ("Shop billing desk", "Laser, mono", "SAMPLE-12A", "12 Nov", 1600, 240)]
DUE4 = [p for p in PR4 if p[5] / p[4] >= .85]
CMYK4 = '<div class=cm4><i style="background:#00a3e0"></i><i style="background:#e0007a"></i><i style="background:#ffd400"></i><i style="background:#111"></i></div>'
B4 = """
body{--f:'Open Sans';--h:'Lora';background:#f7f7f4;color:#161616}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#c4006c;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:60px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#0089bf}
.cm4{display:flex;gap:6px}.cm4 i{width:26px;height:8px;border-radius:4px}
.cd4{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(22,22,22,.07)}
.hd42{display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:8px;margin-bottom:6px}
.sm4{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#6d6d68}
"""
def b4(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#161616;color:#ffd400"):
    return page(B4 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#161616", cta, ctacss, tagline=f"{n} / 5")
PRN4 = '''<div class=pr41><div class=pp41><i></i><i></i><i style="width:60%"></i><i></i><i style="width:40%"></i><em>Half printed</em></div><div class=bd41><div class=lc41>TONER LOW</div><div class=bn41><i></i><i></i><i></i></div><div class=sl41></div></div><div class=tr41></div></div>'''
P["p374_toner_s1"] = b4(1, "PRINTER REFILL AND SERVICE · OFFICES", "Office printer stopped again?<br><span>Refill before it runs out.</span>",
f'''<div class=w41><div class="cd4 hr41">{PRN4}</div><div class=ms41>{"".join(f'<div class="bu41 {c}"><small>{w}</small>{t}</div>' for w, t, c in [("CA OFFICE · 9:40 AM", "Printer says toner low again. We have filings today.", "a"), ("CLINIC · 10:15 AM", "Colour prints are coming out faded.", "b"), ("SCHOOL OFFICE · 11:02 AM", "Can someone come before 2 PM?", "c")])}</div></div>
<div class=sw41>{"".join(f'<div><b>{i}</b><span>{t}</span></div>' for i, t in [(1, "Every printer listed"), (2, "Pages tell you when"), (3, "One route, one job sheet")])}</div>''',
css=""".w41{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px;min-height:0}.vis{flex-direction:column;gap:14px}
.hr41{display:flex;align-items:center;justify-content:center;padding:24px;background:linear-gradient(#fff 72%,#ecece6 72%)}
.pr41{width:380px;display:flex;flex-direction:column;align-items:center}
.pp41{width:240px;height:170px;background:#fff;border:2px solid #d9d9d2;border-bottom:0;border-radius:6px 6px 0 0;padding:18px 20px;display:flex;flex-direction:column;gap:12px;position:relative}
.pp41 i{display:block;height:10px;border-radius:5px;background:#c9c9c4}.pp41 i:nth-child(n+3){background:#ecece8}.pp41 em{position:absolute;right:12px;bottom:10px;font:700 14px/1.3 'Open Sans';font-style:normal;color:#c4006c}
.bd41{width:380px;height:200px;border-radius:24px 24px 14px 14px;background:linear-gradient(#3a3a3a,#1d1d1d);position:relative;padding:22px 26px}
.lc41{width:170px;background:#bfe0a8;color:#2c4a1a;border-radius:8px;font:700 20px/1.4 'Open Sans';letter-spacing:2px;padding:10px 14px;text-align:center;box-shadow:inset 0 0 0 3px #8fb878}
.bn41{display:flex;gap:10px;margin-top:16px}.bn41 i{width:30px;height:30px;border-radius:50%;background:#4a4a4a;box-shadow:inset 0 -3px 0 #222}.bn41 i:first-child{background:#e0007a}
.sl41{position:absolute;left:30px;right:30px;bottom:26px;height:12px;border-radius:6px;background:#0d0d0d}
.tr41{width:300px;height:22px;border-radius:0 0 12px 12px;background:#2a2a2a}
.ms41{display:flex;flex-direction:column;gap:14px;justify-content:center}.bu41{background:#fff;border-radius:22px 22px 22px 6px;padding:16px 20px;font:600 22px/1.4 'Open Sans';box-shadow:0 10px 22px rgba(22,22,22,.07);text-wrap:pretty}
.bu41 small{display:block;font:700 13px/1.4 'Open Sans';letter-spacing:2px;margin-bottom:4px}.bu41.a{border-left:6px solid #00a3e0}.bu41.b{border-left:6px solid #e0007a;margin-left:24px}.bu41.c{border-left:6px solid #ffd400}
.bu41.a small{color:#0089bf}.bu41.b small{color:#c4006c}.bu41.c small{color:#8a7300}
.sw41{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.sw41 div{background:#161616;color:#fff;border-radius:18px;padding:16px 18px;display:flex;align-items:center;gap:14px}
.sw41 b{font:700 34px/1.2 Lora;color:#ffd400}.sw41 span{font:600 18px/1.35 'Open Sans'}""")

P["p374_toner_s2"] = b4(2, "1 · EVERY PRINTER LISTED", "Which printer, which cartridge?<br><span>One list for all offices.</span>",
f'''<div class="cd4 tb42"><div class=hd42><span class=sm4>PRINTERS UNDER SERVICE · SAMPLE</span>{CMYK4}</div>
<div class="rw42 th"><span>Office</span><span>Printer</span><span>Cartridge</span><span>Last refill</span></div>
{"".join(f'<div class=rw42><b>{o}</b><span>{t}</span><span class=cc>{c}</span><span>{d}</span></div>' for o, t, c, d, y, pg in PR4)}
<div class=ft42><div><b>{len(PR4)}</b><span>printers</span></div><div><b>{len(set(p[0].split(",")[0] for p in PR4))}</b><span>customers</span></div><div><b>{len(set(p[2] for p in PR4))}</b><span>cartridge types to stock</span></div></div></div>''',
css=""".tb42{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:4px;min-height:0}
.rw42{flex:1;display:grid;grid-template-columns:1.5fr 1.2fr 1.1fr .8fr;gap:12px;align-items:center;border-top:1px solid #eeeee8;font:400 19px/1.35 'Open Sans'}
.rw42.th{flex:none;font:700 14px/1.4 'Open Sans';letter-spacing:1px;color:#6d6d68;padding-bottom:6px;border:0}.rw42 b{font:700 19px/1.35 'Open Sans'}
.rw42 .cc{justify-self:start;font:700 15px/1.3 'Open Sans';background:#f1f1ec;border-radius:8px;padding:5px 9px}
.ft42{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:8px}.ft42 div{background:#161616;color:#fff;border-radius:16px;padding:12px 16px;display:flex;align-items:baseline;gap:10px}
.ft42 b{font:700 34px/1.25 Lora;color:#ffd400}.ft42 span{font:600 16px/1.35 'Open Sans'}""")

P["p374_toner_s3"] = b4(3, "2 · PAGES TELL YOU WHEN", "Read the page counter.<br><span>See who needs a refill.</span>",
f'''<div class="cd4 pg43"><div class=hd42><span class=sm4>PAGES SINCE LAST REFILL · VS CARTRIDGE PAGES · SAMPLE</span>{CMYK4}</div>
{"".join(f'<div class=r43><div><b>{o}</b><span>{c} · {pg:,} of {y:,} pages</span></div><div class=bx43><i class="{"due" if pg / y >= .85 else ""}" style="width:{pg / y * 100:.0f}%"></i><em style="left:85%"></em></div><strong class="{"due" if pg / y >= .85 else ""}">{pg / y * 100:.0f}%</strong></div>' for o, t, c, d, y, pg in PR4)}
<div class=lg43><span><i class=due></i>85% or more: refill this week</span><span><i></i>Still fine</span></div></div>
<div class=du43><span class=sm4>REFILL DUE THIS WEEK</span><b>{len(DUE4)}</b><p>{", ".join(p[0] for p in DUE4)}</p></div>''',
css=""".vis{flex-direction:column;gap:14px}.pg43{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:6px;min-height:0}
.r43{flex:1;display:grid;grid-template-columns:1.25fr 1.4fr 64px;gap:16px;align-items:center;border-top:1px solid #eeeee8}
.r43 b{display:block;font:700 18px/1.35 'Open Sans'}.r43 span{font:400 15px/1.35 'Open Sans';color:#5d5d58}
.bx43{position:relative;height:26px;border-radius:13px;background:#efefea;overflow:hidden}.bx43 i{position:absolute;left:0;top:0;bottom:0;border-radius:13px;background:#00a3e0}.bx43 i.due{background:#e0007a}
.bx43 em{position:absolute;top:0;bottom:0;width:3px;background:#161616}
.r43 strong{font:700 22px/1.3 Lora;text-align:right}.r43 strong.due{color:#c4006c}
.lg43{display:flex;gap:22px;font:600 15px/1.4 'Open Sans';color:#4b4b47}.lg43 span{display:flex;align-items:center;gap:8px}.lg43 i{width:22px;height:12px;border-radius:6px;background:#00a3e0}.lg43 i.due{background:#e0007a}
.du43{background:#161616;color:#fff;border-radius:22px;padding:16px 22px;display:grid;grid-template-columns:auto auto 1fr;gap:18px;align-items:center}.du43 .sm4{color:#bdbdb6}
.du43 b{font:700 48px/1.2 Lora;color:#ff4fa8}.du43 p{font:600 18px/1.45 'Open Sans'}""")

TM4 = ["10:40 AM", "12:10 PM", "2:30 PM", "3:15 PM"]
SIG4 = '<svg viewBox="0 0 220 70" style="width:220px;height:70px;display:block"><path d="M8 50 C30 10 40 60 60 30 S90 20 96 44 C104 64 122 14 140 36 S170 52 190 24 L210 30" fill="none" stroke="#1d3fa0" stroke-width="3" stroke-linecap="round"/></svg>'
P["p374_toner_s4"] = b4(4, "3 · ONE ROUTE, ONE JOB SHEET", "Visit the due ones together.<br><span>Get a sign-off on the spot.</span>",
f'''<div class=w44><div class="cd4 rt44"><span class=sm4>TUESDAY ROUTE · SAMPLE</span>{"".join(f'<div class=st44><i>{k}</i><div><em>{TM4[k - 1]}</em><b>{p[0]}</b><span>{p[2]} refill · carry 1</span></div></div>' for k, p in enumerate(DUE4, 1))}
<div class=st44><i>4</i><div><em>{TM4[3]}</em><b>Office A, 2nd floor</b><span>Same building as stop 1, quick check</span></div></div><div class=nt44>Cartridges to carry: {", ".join(f"{sum(1 for p in DUE4 if p[2] == c)} × {c}" for c in dict.fromkeys(p[2] for p in DUE4))}</div></div>
<div class="cd4 js44"><div class=hd42><span class=sm4>JOB SHEET · J-118 · SAMPLE</span>{CMYK4}</div>
{"".join(f'<div class=fd44><span>{a}</span><b>{b}</b></div>' for a, b in [("Office", DUE4[0][0]), ("Visit", "Tue, 10:40 AM"), ("Engineer", "Sample Tech 1"), ("Printer", DUE4[0][1]), ("Cartridge", DUE4[0][2]), ("Page counter", "18,240"), ("Note", "Paper roller worn, quote sent")])}
<div class=wk44>{"".join(f"<i>{w}</i>" for w in ["Toner refilled", "Drum cleaned", "Test page OK"])}</div>
<div class=sg44><span>Signed by office staff</span>{SIG4}</div></div></div>''',
css=""".w44{flex:1;display:grid;grid-template-columns:1fr 1.05fr;gap:16px;min-height:0}.rt44{padding:20px 22px;display:flex;flex-direction:column;gap:10px}
.st44{flex:1;display:flex;gap:14px;align-items:center;border-top:1px solid #eeeee8}.st44 i{width:44px;height:44px;flex:none;border-radius:50%;background:#161616;color:#ffd400;font:700 20px/44px Lora;font-style:normal;text-align:center}
.st44 em{display:block;font:700 14px/1.4 'Open Sans';font-style:normal;color:#c4006c;letter-spacing:1px}.st44 b{display:block;font:700 19px/1.35 'Open Sans'}.st44 span{font:400 16px/1.35 'Open Sans';color:#5d5d58}
.nt44{background:#fff6c2;border-radius:16px;padding:14px 16px;font:600 17px/1.45 'Open Sans'}
.js44{padding:20px 22px;display:flex;flex-direction:column;gap:10px}.fd44{flex:1;align-items:center;display:flex;justify-content:space-between;border-top:1px dashed #deded8;padding-top:4px;font:400 18px/1.4 'Open Sans'}.fd44 span{color:#5d5d58}.fd44 b{font-weight:700}
.wk44{display:flex;flex-wrap:wrap;gap:8px;margin-top:4px}.wk44 i{font:600 15px/1.3 'Open Sans';font-style:normal;background:#e6f6fc;color:#005f86;border-radius:10px;padding:7px 11px}
.sg44{border:2px dashed #cfcfc8;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;gap:4px}.sg44 span{font:600 14px/1.4 'Open Sans';color:#6d6d68}""")

P["p374_toner_s5"] = b4(5, "YOUR TURN", "Refill or repair printers?<br><span>Let's build your service app.</span>",
f'''<div class=w45><div class="cd4 pv45">{PRN4}</div><div class=td45>{"".join(f'<div class=ti45><span class=ib>{ic(i, 30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("grid", "Printer list", "Every office, every cartridge"), ("chart", "Page counter", "Refill due before it runs out"), ("map", "Visit route", "Due ones on one trip"), ("doc", "Job sheet", "Work done and signed")])}</div>
<div class=q45>How do your office customers call you for refills today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#e0007a;color:#fff",
css=""".w45{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.pv45{display:flex;align-items:center;justify-content:center;padding:20px;background:linear-gradient(#fff 72%,#ecece6 72%)}.pv45 .pr41{transform:none}
.td45{display:flex;flex-direction:column;gap:12px}.ti45{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(22,22,22,.07)}
.ti45 .ib{width:58px;height:58px;border-radius:18px;background:#161616;color:#ffd400}.ti45 b{display:block;font:700 25px/1.3 Lora}.ti45 div span{font:500 17px/1.4 'Open Sans';color:#4b4b47}
.q45{grid-column:1 / 3;background:#161616;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'Open Sans'}
.pr41{width:380px;display:flex;flex-direction:column;align-items:center}
.pp41{width:240px;height:170px;background:#fff;border:2px solid #d9d9d2;border-bottom:0;border-radius:6px 6px 0 0;padding:18px 20px;display:flex;flex-direction:column;gap:12px;position:relative}
.pp41 i{display:block;height:10px;border-radius:5px;background:#c9c9c4}.pp41 i:nth-child(n+3){background:#ecece8}.pp41 em{position:absolute;right:12px;bottom:10px;font:700 14px/1.3 'Open Sans';font-style:normal;color:#c4006c}
.bd41{width:380px;height:200px;border-radius:24px 24px 14px 14px;background:linear-gradient(#3a3a3a,#1d1d1d);position:relative;padding:22px 26px}
.lc41{width:170px;background:#bfe0a8;color:#2c4a1a;border-radius:8px;font:700 20px/1.4 'Open Sans';letter-spacing:2px;padding:10px 14px;text-align:center;box-shadow:inset 0 0 0 3px #8fb878}
.bn41{display:flex;gap:10px;margin-top:16px}.bn41 i{width:30px;height:30px;border-radius:50%;background:#4a4a4a;box-shadow:inset 0 -3px 0 #222}.bn41 i:first-child{background:#e0007a}
.sl41{position:absolute;left:30px;right:30px;bottom:26px;height:12px;border-radius:6px;background:#0d0d0d}
.tr41{width:300px;height:22px;border-radius:0 0 12px 12px;background:#2a2a2a}""")


# ───────── 375 USA · Vending machine operator · SINGLE · Gelasio + Roboto · cobalt / snack yellow / chrome
# New technique: CSS vending machine fronts (glass grid of coils, filled vs empty slots from seeded stock), each machine's
# fill % and the truck load list are computed from the same slot grid; route order = emptiest first.
random.seed(375)
LOC5 = [("Gym lobby", 0.35), ("Office park B", 0.7), ("Car wash", 0.55), ("Library annex", 0.85), ("Hotel lobby", 0.25), ("Auto shop", 0.6)]
ITEMS5 = [("Chips", "#f2b705"), ("Water", "#4aa3df"), ("Granola", "#b8742a"), ("Crackers", "#e0573c")]
MCH5 = []
for nm, f in LOC5:
    slots = [(ITEMS5[c % 4], random.random() < f) for c in range(20)]
    MCH5.append((nm, slots))
def fill5(sl): return sum(1 for _, on in sl if on) / len(sl)
ROUTE5 = sorted([m for m in MCH5 if fill5(m[1]) < .6], key=lambda m: fill5(m[1]))
LOAD5 = {it[0]: sum(5 for m in ROUTE5 for (i, on) in m[1] if not on and i[0] == it[0]) for it in ITEMS5}
def vm5(sl):
    return '<div class=vm5><div class=gl5>' + "".join(f'<i style="background:{i[1] if on else "transparent"};{"" if on else "border:2px dashed #9aa6b4"}"></i>' for i, on in sl) + '</div><div class=pn5><i></i><i></i><i></i><b></b></div></div>'
P["p375_vending"] = page("""
body{--f:'Roboto';--h:'Gelasio';background:#eef1f5;color:#16233a;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#2147a8;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#2147a8}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.gr5{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;min-height:0}
.mc5{background:#fff;border-radius:22px;padding:12px 14px;display:flex;gap:12px;align-items:stretch;box-shadow:0 12px 26px rgba(22,35,58,.08)}
.mc5.lo{box-shadow:0 0 0 3px #e0573c,0 12px 26px rgba(22,35,58,.08)}
.vm5{width:118px;flex:none;border-radius:12px;background:linear-gradient(90deg,#1d3a8a,#2a52bd);padding:8px;display:flex;gap:6px}
.gl5{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(5,1fr);gap:4px;background:linear-gradient(135deg,#dfe8f3,#f6f9fc);border-radius:6px;padding:5px}
.gl5 i{border-radius:3px}
.pn5{width:20px;display:flex;flex-direction:column;gap:5px;padding-top:6px}.pn5 i{height:8px;border-radius:2px;background:#9fb3e6}.pn5 b{margin-top:auto;height:18px;border-radius:3px;background:#0f1f4d}
.in5{flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:4px;min-width:0}
.in5 b{font:700 20px/1.3 Gelasio}.in5 small{font:500 13px/1.3 Roboto;color:#5b6678}
.fl5{height:12px;border-radius:6px;background:#e4e9f0;overflow:hidden}.fl5 i{display:block;height:100%;background:#2147a8;border-radius:6px}.mc5.lo .fl5 i{background:#e0573c}
.in5 strong{display:block;font:700 40px/1.2 Gelasio}.es5{display:block}.mc5.lo .in5 strong{color:#c2412a}
.in5 em{font:700 13px/1.3 Roboto;font-style:normal;color:#2f7a45}.mc5.lo .in5 em{color:#c2412a}
.lg5{display:flex;gap:18px;font:500 15px/1.4 Roboto;color:#3c4758}.lg5 span{display:flex;align-items:center;gap:6px}.lg5 i{width:16px;height:16px;border-radius:4px}
.bt5{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.rt5{background:#16233a;color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}.rt5 small,.ld5 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#a9b8d6}
.rt5 div{display:flex;align-items:center;gap:12px;font:500 18px/1.35 Roboto}.rt5 div i{width:34px;height:34px;border-radius:50%;background:#f2b705;color:#16233a;font:700 16px/34px Roboto;font-style:normal;text-align:center}.rt5 div span{margin-left:auto;color:#ffb3a3;font-weight:700}
.rt5 p{margin-top:auto;font:400 15px/1.45 Roboto;color:#c9d3e6}
.ld5{background:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(22,35,58,.08)}.ld5 small{color:#5b6678}
.ld5 div{display:flex;align-items:center;gap:12px;border-top:1px solid #edf0f4;padding-top:6px;font:500 18px/1.35 Roboto}.ld5 div i{width:18px;height:18px;border-radius:4px}.ld5 div b{margin-left:auto;font:700 24px/1.25 Gelasio}
""", "<div class=kk>VENDING MACHINE OPERATOR · RESTOCK DAY</div><h1>Driving to full machines?<br><span>Restock only the empty ones.</span></h1>",
f'''<div class=vw><div class=gr5>{"".join(f'<div class="mc5 {"lo" if fill5(sl) < .6 else ""}">{vm5(sl)}<div class=in5><div><b>{nm}</b><br><small>20 slots · sample</small></div><div><strong>{fill5(sl) * 100:.0f}%</strong><small class=es5>full · {sum(1 for _, on in sl if not on)} empty slots</small></div><div class=fl5><i style="width:{fill5(sl) * 100:.0f}%"></i></div><em>{"Restock today" if fill5(sl) < .6 else "Skip this week"}</em></div></div>' for nm, sl in MCH5)}</div>
<div class=lg5>{"".join(f'<span><i style="background:{c}"></i>{n}</span>' for n, c in ITEMS5)}<span><i style="border:2px dashed #9aa6b4"></i>Empty slot</span></div>
<div class=bt5><div class=rt5><small>TODAY'S ROUTE · EMPTIEST FIRST</small>{"".join(f'<div><i>{k}</i>{m[0]}<span>{fill5(m[1]) * 100:.0f}% full</span></div>' for k, m in enumerate(ROUTE5, 1))}<p>Machines over 60% full wait for next week.</p></div>
<div class=ld5><small>LOAD THE VAN · 5 PER EMPTY SLOT</small>{"".join(f'<div><i style="background:{c}"></i>{n}<b>{LOAD5[n]}</b></div>' for n, c in ITEMS5)}</div></div></div>''',
"#16233a", "Run vending machines? DM us", "background:#2147a8;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
