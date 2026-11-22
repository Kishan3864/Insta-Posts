import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 291 INDIA · Fruit commission agent (mandi) · SINGLE · Archivo Black + Fira Sans · mango yellow / crate green / slate
# New technique: CSS plastic crates (slotted sides) as a returnable-crate ledger per grower: solid = given, faded = back, dashed = still out.
def crate(st):
    return f'<i class="cr {st}"></i>'
growers = [("G-11", "Mango", 30, 30), ("G-14", "Banana", 40, 28), ("G-19", "Papaya", 20, 12), ("G-23", "Guava", 30, 30)]
P["p291_mandi"] = page("""
body{--f:'Fira Sans';--h:'Archivo Black';background:#f3eedc;color:#22303a}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#2f7d4a;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.25;margin-top:16px} h1 span{color:#d99a00}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.lg7{flex:1;min-height:0;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(34,48,58,.08)}
.hd7{display:grid;grid-template-columns:150px 1fr 150px;gap:14px;font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#77735f;padding-bottom:8px;border-bottom:2px solid #22303a}
.gr7{flex:1;display:grid;grid-template-columns:150px 1fr 150px;gap:14px;align-items:center;border-bottom:1px solid #eee8d6}.gr7:last-child{border:0}
.gn b{display:block;font:400 28px/1.4 'Archivo Black'}.gn span{font:600 17px 'Fira Sans';color:#5f6a6f}
.cs{display:flex;flex-wrap:wrap;gap:5px}
.cr{width:36px;height:28px;border-radius:4px;background:repeating-linear-gradient(90deg,#2f7d4a 0 6px,#3f9a5d 6px 8px);border:2px solid #1f5c35;position:relative}
.cr:after{content:"";position:absolute;left:8px;right:8px;top:3px;height:4px;border-radius:2px;background:#f3eedc}
.cr.bk{opacity:.28}.cr.out{background:#fff;border:2px dashed #c0573b}.cr.out:after{background:#f6d8cf}
.st7{text-align:right}.st7 b{display:block;font:400 30px/1.4 'Archivo Black'}.st7 span{font:600 16px 'Fira Sans';color:#5f6a6f}
.ok7 b{color:#2f7d4a}.due b{color:#c0573b}
.bt7{display:grid;grid-template-columns:1fr 1.3fr;gap:12px}
.lgd7{background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;gap:10px;box-shadow:0 14px 30px rgba(34,48,58,.08)}.lgd7 span{display:flex;align-items:center;gap:12px;font:600 20px 'Fira Sans'}
.msg7{background:#22303a;color:#fff;border-radius:22px;padding:16px 20px}.msg7 small{display:block;font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#ffd35c;margin-bottom:6px}.msg7 p{font:500 20px/1.45 'Fira Sans'}.msg7 b{color:#ffd35c}
""", "<div class=kk>FRUIT COMMISSION AGENT · MANDI CRATES</div><h1>120 crates went out.<br><span>Who still has them?</span></h1>",
f'''<div class=vw><div class=lg7><div class=hd7><span>GROWER · SAMPLE</span><span>ONE BOX = ONE CRATE · THIS WEEK</span><span style="text-align:right">STILL OUT</span></div>
{"".join(f'<div class=gr7><div class=gn><b>{g}</b><span>{f}</span></div><div class=cs>{"".join(crate("bk") for _ in range(back))}{"".join(crate("out") for _ in range(given-back))}</div><div class="st7 {"ok7" if given==back else "due"}"><b>{given-back}</b><span>of {given} given</span></div></div>' for g,f,given,back in growers)}</div>
<div class=bt7><div class=lgd7><span>{crate("bk")} Came back</span><span>{crate("out")} Still with the grower</span></div>
<div class=msg7><small>REMINDER TO G-14 · SAMPLE</small><p>You have <b>12 crates</b> with you. Please send them with your next load.</p></div></div></div>''',
"#22303a", "Commission agent? DM us", "background:#2f7d4a;color:#fff")

# ───────── 292 CANADA · Mobile bike repair · SINGLE · Montserrat + Source Sans 3 · pine / off-white / tangerine · PHONE
# New technique: van side cutaway with shelf bins whose counts come from today's bookings (parts to load).
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE MOBILE BIKE REPAIR</small><b>Book a home visit</b></div>
<div class=af><small>BIKE TYPE</small><div class=chs2><span>Road</span><span class=on>Hybrid</span><span>Kids</span><span>E-bike</span></div></div>
<div class=af><small>WHAT NEEDS FIXING?</small><div class=chs2 style="flex-wrap:wrap"><span class=on>Flat tire</span><span class=on>Brakes</span><span>Gears</span><span>Chain</span></div></div>
<div class=af><small>TIRE SIZE (ON THE SIDE)</small><div class=in2>700 × 35c</div></div>
<div class=af><small>WHERE</small><div class=in2>Driveway · postal code A1A 1A1</div></div>
<div class=af><small>PHOTO OF THE PROBLEM</small><div class=in2>2 photos added</div></div>
<div class=af><small>VISIT</small><div class=chs2><span>Sat AM</span><span class=on>Sat PM</span><span>Sun AM</span></div></div>
<div class=bk2>Book visit</div></div>''', 380, 830)
bins = [("Tubes 700c", 4), ("Tubes 26 in", 2), ("Brake pads", 6), ("Chains", 1), ("Cables", 3), ("Tire levers", 2)]
P["p292_bikerepair"] = page("""
body{--f:'Source Sans 3';--h:'Montserrat';background:#f4f1ea;color:#1f3b33}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#e3701f;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#2d6a57}
.vw{flex:1;display:flex;gap:20px;min-height:0;align-items:center}
.ap{flex:1;display:flex;flex-direction:column;gap:12px;padding:8px 18px 20px}
.ah small{display:block;font:700 12px/1.4 'Source Sans 3';letter-spacing:2px;color:#2d6a57}.ah b{display:block;font:800 24px/1.35 'Montserrat'}
.af small{display:block;font:700 12px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#76736a;margin-bottom:5px}
.in2{border:2px solid #e2ddd2;border-radius:10px;padding:9px 12px;font:700 16px 'Source Sans 3'}
.chs2{display:flex;gap:6px}.chs2 span{flex:1;text-align:center;font:700 14px 'Source Sans 3';padding:9px 6px;border-radius:9px;border:2px solid #e2ddd2;white-space:nowrap}.chs2 span.on{border-color:#2d6a57;background:#e3f0eb;color:#1f4d3f}
.bk2{margin-top:auto;background:#e3701f;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 18px 'Source Sans 3'}
.rc{flex:1;min-width:0;align-self:stretch;display:flex;flex-direction:column;gap:12px}
.van{flex:1;background:#2d6a57;border-radius:26px 60px 20px 20px;padding:18px 18px 34px;display:flex;flex-direction:column;gap:10px;position:relative;box-shadow:0 14px 30px rgba(31,59,51,.15)}
.van:after{content:"";position:absolute;bottom:-22px;left:60px;width:56px;height:56px;border-radius:50%;background:#1f2a28;border:10px solid #9aa5a1}
.van:before{content:"";position:absolute;bottom:-22px;right:60px;width:56px;height:56px;border-radius:50%;background:#1f2a28;border:10px solid #9aa5a1}
.vh{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#cfe5dc}
.shf{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:10px;background:#f4f1ea;border-radius:14px;padding:10px;border-bottom:8px solid #c9b48f}
.bn{background:#fff;border-radius:10px;border-top:6px solid #e3701f;padding:6px 12px;display:flex;align-items:center;gap:12px}.bn b{font:800 52px/1.25 'Montserrat';color:#e3701f}.bn span{font:600 19px/1.3 'Source Sans 3'}
.td{background:#fff;border-radius:22px;padding:14px 18px;box-shadow:0 14px 30px rgba(31,59,51,.08);display:flex;flex-direction:column;gap:6px;margin-top:20px}
.td small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#76736a}.tr2{display:flex;justify-content:space-between;font:600 17px 'Source Sans 3'}.tr2 b{color:#2d6a57}
""", "<div class=kk>MOBILE BIKE REPAIR · HOME VISITS</div><h1>Drove there, no tube?<br><span>Bookings fill the van.</span></h1>",
f'''<div class=vw>{ph}<div class=rc><div class=van><div class=vh>LOAD FOR SAT 28 NOV · FROM 6 BOOKINGS</div><div class=shf>{"".join(f"<div class=bn><b>{n}</b><span>{a}</span></div>" for a,n in bins)}</div></div>
<div class=td><small>TODAY · SAMPLE</small>{"".join(f"<div class=tr2><span>{a}</span><b>{b}</b></div>" for a,b in [("Flat tires","4 visits"),("Brakes","3 visits"),("Gears + chain","1 visit")])}</div></div></div>''',
"#1f3b33", "Fix bikes at home? DM us", "background:#e3701f;color:#fff")

# ───────── 293 INDIA · Vegetable seedling nursery · CAROUSEL 5 · Gelasio + Inter · sprout green / coir brown / tray black
# New technique: CSS plug trays (grid of cells with seedling dots, empty cells shown) reused as the counting unit through the carousel.
SN = """
body{--f:'Inter';--h:'Gelasio';background:#f2efe3;color:#22301f}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#8a5a2b;margin-top:22px;align-self:flex-start}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#3f8a2f}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(34,48,31,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#77735f}
.nb{display:flex;align-items:center;gap:14px;background:#22301f;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Inter'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#3f8a2f}.nb b{color:#c9e8a6}
.tray{display:grid;gap:4px;background:#1f2321;border-radius:10px;padding:8px}
.tray i{aspect-ratio:1;border-radius:4px;background:#7a5634;position:relative}
.tray i.g:after{content:"";position:absolute;inset:22%;border-radius:50% 50% 50% 0;background:#6fbf4a;transform:rotate(-45deg)}
.tray i.y:after{content:"";position:absolute;inset:34%;border-radius:50%;background:#b8d98f}
"""
def tray(cols, rows, kind="g", empty=0, w=None):
    cells = [kind] * (cols * rows - empty) + [""] * empty
    return f'<div class=tray style="grid-template-columns:repeat({cols},1fr);{f"width:{w}px;" if w else ""}">{"".join(f"<i class={chr(34)}{c}{chr(34)}></i>" for c in cells)}</div>'
def sn(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#22301f;color:#fff"):
    return page(SN + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#22301f", cta, ctacss, tagline=f"{n} / 5")
P["p293_seedling_s1"] = sn(1, "VEGETABLE SEEDLING NURSERY · TRAY ORDERS", "“2,000 chilli plants?”<br><span>Book trays, not calls.</span>",
f'''<div class=w1><div class="cd tc">{tray(14, 7, "g", 0)}<div class=tl><b>1 tray = 98 seedlings</b><span>Sample 98-cell plug tray</span></div></div>
<div class=sm1>{"".join(f'<div class="cd s1"><small class=cap>{a}</small><b>{b}</b><span>{c}</span></div>' for a,b,c in [("ORDER","2,000","Chilli seedlings"),("TRAYS","21","98 cells each"),("READY","Mon 7 Dec","Sample date")])}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tc{flex:1;padding:22px;display:flex;flex-direction:column;justify-content:center;gap:16px}
.tl{display:flex;justify-content:space-between;align-items:baseline}.tl b{font:700 32px/1.3 Gelasio}.tl span{font:600 18px Inter;color:#77735f}
.sm1{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.s1{padding:16px 20px}.s1 b{display:block;font:700 44px/1.3 Gelasio;color:#3f8a2f}.s1 span{font:600 17px Inter;color:#5f6a58}""")

crops = [("Chilli", "Ready in about 5 weeks", 34), ("Tomato", "Ready in about 4 weeks", 18), ("Brinjal", "Ready in about 5 weeks", 9), ("Cauliflower", "Ready in about 4 weeks", 0)]
P["p293_seedling_s2"] = sn(2, "STEP 1 · TRAYS AVAILABLE BY CROP", "Farmers see what is<br><span>growing, and when.</span>",
f'''<div class=w2>{"".join(f'<div class="cd cr2"><div class=mt>{tray(7, 4, "g" if n else "y", 0)}</div><div class=ci><b>{c}</b><span>{r}</span></div><div class=av><b>{n if n else "Sowing"}</b><span>{"trays free" if n else "Mon 23 Nov"}</span></div></div>' for c,r,n in crops)}</div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.cr2{flex:1;display:flex;align-items:center;gap:22px;padding:14px 22px}
.mt{width:190px;flex:none}.ci{flex:1}.ci b{display:block;font:700 34px/1.3 Gelasio}.ci span{font:500 19px Inter;color:#5f6a58}
.av{text-align:right}.av b{display:block;font:700 44px/1.3 Gelasio;color:#3f8a2f}.av span{font:600 16px Inter;color:#77735f}""")

wk = [("Sow", "Mon 2 Nov", "d"), ("Sprout", "Mon 9 Nov", "d"), ("Grow", "Mon 16 to 30 Nov", "n"), ("Harden", "Wed 2 Dec", ""), ("Ready", "Mon 7 Dec", "")]
P["p293_seedling_s3"] = sn(3, "STEP 2 · EVERY BATCH ON A TIMELINE", "Batch C-41 is growing.<br><span>The farmer can check.</span>",
f'''<div class=w3><div class="cd bt3"><div class=bh3><div><small class=cap>BATCH C-41 · CHILLI · SAMPLE</small><b>21 trays for order O-293</b></div>{tray(14, 3, "g", 0, 380)}</div>
<div class=tl3>{"".join(f'<div class="ts {k}"><i></i><b>{a}</b><span>{d}</span>{tray(3, 4, ["","y","g","g","g"][j], 0, 150)}</div>' for j,(a,d,k) in enumerate(wk))}</div></div>
<div class=nb><span class=ib>{ic("camera",26)}</span><span>A tray photo goes to the farmer every week, <b>so no one has to visit to check.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.bt3{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:20px}
.bh3{display:flex;justify-content:space-between;align-items:center;gap:20px}.bh3 b{display:block;font:700 34px/1.3 Gelasio}
.tl3{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:0;position:relative;align-items:center}
.ts{display:flex;flex-direction:column;align-items:center;gap:10px;text-align:center;position:relative;padding:0 4px}
.ts:before{content:"";position:absolute;top:28px;left:-50%;right:50%;height:8px;background:#ddd6bf}.ts:first-child:before{display:none}.ts.d:before,.ts.n:before{background:#3f8a2f}
.ts>i{width:64px;height:64px;border-radius:50%;background:#fff;border:6px solid #ddd6bf;position:relative;z-index:1}.ts.d>i{background:#3f8a2f;border-color:#3f8a2f}.ts.n>i{border-color:#3f8a2f;background:#dff0d2}
.ts b{font:700 30px/1.3 Gelasio;margin-top:6px}.ts .tray{margin-top:14px}.ts span{font:600 18px/1.35 Inter;color:#5f6a58}""")

P["p293_seedling_s4"] = sn(4, "STEP 3 · PICKUP SLOT AND TRAY RETURN", "Ready day is fixed.<br><span>So is the pickup.</span>",
f'''<div class=w4><div class="cd oc"><small class=cap>ORDER O-293 · SAMPLE</small>{"".join(f'<div class=or4><span>{a}</span><b>{b}</b></div>' for a,b in [("Farmer","F-118"),("Crop","Chilli, batch C-41"),("Seedlings","2,000 · 21 trays"),("Pickup","Mon 7 Dec · 7 AM"),("Vehicle","Pickup van, 2 trips")])}</div>
<div class=sd4><div class="cd rt"><small class=cap>TRAYS TO RETURN</small><b>21</b><span>Marked back when the van returns</span></div><div class="cd ms4"><small class=cap>MESSAGE · SUN 6 DEC</small><p>Your 21 trays are ready for <b>7 AM tomorrow</b>.</p></div></div></div>''',
css=""".w4{flex:1;display:flex;gap:14px;min-height:0}.oc{flex:1;min-width:0;padding:20px 24px;display:flex;flex-direction:column}
.or4{flex:1;display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid #eee8d6}.or4:last-child{border:0}.or4 span{font:600 17px Inter;color:#77735f}.or4 b{font:700 32px/1.3 Gelasio}
.sd4{width:360px;flex:none;display:flex;flex-direction:column;gap:12px}.rt{flex:1;padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:4px;background:#22301f;color:#fff}.rt .cap{color:#c9e8a6}.rt b{font:700 110px/1.2 Gelasio;color:#c9e8a6}.rt span{font:500 19px/1.4 Inter;color:#dfe7d6}
.ms4{padding:20px 24px}.ms4 p{margin-top:8px;font:500 24px/1.45 Inter;background:#eef6e6;border-radius:16px 16px 16px 4px;padding:16px}.ms4 b{color:#3f8a2f}""")

P["p293_seedling_s5"] = sn(5, "YOUR TURN", "Grow seedlings for farmers?<br><span>Let's build your tray booking.</span>",
f'''<div class=w5><div class="cd hp">{tray(7, 6, "g", 0, 270)}{tray(7, 6, "g", 3, 270)}{tray(7, 6, "y", 0, 270)}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Trays by crop","Free trays, live"),("cal","Batch timeline","Sow to ready"),("camera","Weekly photos","Sent to farmers"),("truck","Pickup slots","And tray returns")])}</div>
<div class=q>How do farmers book seedlings with you today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#3f8a2f;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;justify-content:center;align-items:center;gap:26px;padding:20px}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(34,48,31,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#e6f2dc;color:#3f8a2f}.ti b{display:block;font:700 28px/1.35 Gelasio}.ti div span{font:500 19px/1.35 Inter;color:#5f6a58}
.q{background:#22301f;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Inter}""")

# ───────── 294 INDIA · Key duplicate and lock shop · SINGLE · Bitter + Poppins · key brass / teal / ink
# New technique: drawn key ring with keys (SVG bow + blade with cut teeth) and coloured caps, each key matched to a job line.
def key(cap, tx):
    teeth = "".join(f"L{60+i*16} {50 + (10 if (i*7+len(tx))%3 else 18)} L{68+i*16} 42 " for i in range(9))
    return f'''<svg viewBox="0 0 250 70" class=ky><circle cx="34" cy="35" r="28" fill="{cap}" stroke="#1d2a33" stroke-width="4"/><circle cx="24" cy="35" r="8" fill="#f6f1e6" stroke="#1d2a33" stroke-width="3"/>
<path d="M60 26 H236 L244 34 L236 42 {teeth} L60 50 Z" fill="#d9b25a" stroke="#1d2a33" stroke-width="3.5" stroke-linejoin="round"/><line x1="70" y1="33" x2="226" y2="33" stroke="#a8842f" stroke-width="3"/></svg>'''
keys = [("#1b8a8a", "Main door", "× 2 copies", "Ready 12:30 PM"), ("#e0603a", "Bedroom", "× 1 copy", "Ready 12:30 PM"), ("#5a6acf", "Bike", "× 1 copy", "Ready 1 PM"), ("#d9b25a", "Cupboard", "× 2 copies", "Ready 1 PM")]
P["p294_keyshop"] = page("""
body{--f:'Poppins';--h:'Bitter';background:#f6f1e6;color:#1d2a33}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#1b8a8a;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#b8892c}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.rg{flex:1;min-width:0;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(29,42,51,.08)}
.cap{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#79736a}
.ring{display:flex;align-items:center;gap:14px}.ring i{width:70px;height:70px;border-radius:50%;border:9px solid #9aa3aa;flex:none}.ring b{font:800 30px/1.3 Bitter}.ring span{display:block;font:500 17px Poppins;color:#5f6a72}
.kr{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #efe9dc}
.ky{width:250px;height:70px;flex:none;display:block}
.kt{flex:1;min-width:0}.kt b{display:block;font:700 24px/1.3 Bitter}.kt span{font:500 17px Poppins;color:#5f6a72}
.kr em{font:600 15px 'Poppins';font-style:normal;background:#e3f2f2;color:#136b6b;padding:6px 10px;border-radius:8px;flex:none}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.cd{background:#fff;border-radius:24px;padding:16px 20px;box-shadow:0 14px 30px rgba(29,42,51,.08)}
.tk{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;background:#1d2a33;color:#fff}.tk small{font:600 14px/1.4 Poppins;letter-spacing:2px;color:#f2d38f}.tk b{font:800 130px/1.2 Bitter;color:#f2d38f}.tk span{font:500 18px/1.4 Poppins;color:#cfd6db}
.hv{display:flex;flex-direction:column;gap:6px}.hv b{font:800 26px/1.3 Bitter}.hv span{font:500 17px/1.4 Poppins;color:#5f6a72}
.hv i{font:600 15px Poppins;font-style:normal;background:#fbeed2;color:#8a6417;border-radius:8px;padding:5px 10px;align-self:flex-start}
""", "<div class=kk>KEY DUPLICATE AND LOCK SHOP</div><h1>“Come back in an hour”?<br><span>Send a ready message.</span></h1>",
f'''<div class=vw><div class=rg><div class=ring><i></i><div><b>Job K-294</b><span>Customer's key ring · sample</span></div></div>
{"".join(f'<div class=kr>{key(c,n)}<div class=kt><b>{n}</b><span>{q}</span></div><em>{r}</em></div>' for c,n,q,r in keys)}</div>
<div class=sd><div class="cd tk"><small>COPIES IN THIS JOB</small><b>6</b><span>Ready message goes out when the last key is cut.</span></div>
<div class="cd hv"><small class=cap>HOME VISIT · SAMPLE</small><b>Lock change</b><span>Flat 3B · Sat 28 Nov · 5 PM</span><i>Photo of the lock received</i></div></div></div>''',
"#1d2a33", "Run a key shop? DM us", "background:#1b8a8a;color:#fff")

# ───────── 295 USA · Sprinkler blowout (winterizing) · SINGLE · Crimson Text + Roboto · frost white / ice blue / lawn olive
# New technique: top-down yard with irrigation zones as tinted areas, heads as spray-arc dots, plus a same-street route list.
def yard():
    zones = [(30, 30, 250, 150, "#cfe6b0", "Z1"), (290, 30, 220, 150, "#bfe0c8", "Z2"), (30, 330, 160, 200, "#d9ecbf", "Z3"), (200, 330, 150, 200, "#c4e3b6", "Z4"), (360, 330, 150, 200, "#d2e9c4", "Z5")]
    z = ""
    for x, y, w, h, c, n in zones:
        heads = "".join(f'<path d="M{hx} {hy} L{hx+16} {hy-12} A20 20 0 0 1 {hx+16} {hy+12} Z" fill="#3d8fd1" opacity=".55"/><circle cx="{hx}" cy="{hy}" r="5" fill="#1f5f99"/>' for hx in (x + 30, x + w - 50) for hy in (y + 30, y + h - 30))
        z += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="12" fill="{c}" stroke="#7a9a5a" stroke-width="3"/>{heads}<text x="{x+w/2}" y="{y+h/2+12}" text-anchor="middle" font-family="Roboto" font-weight="800" font-size="34" fill="#3e5a2a">{n}</text>'
    return f'''<svg viewBox="0 0 540 830" class=yd><rect width="540" height="830" fill="#eef3ea"/>
<rect x="30" y="30" width="480" height="8" rx="4" fill="#9a8466"/><text x="270" y="70" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="18" fill="#7a6a52">Back fence</text>
<rect x="150" y="110" width="240" height="100" rx="10" fill="#e9e4da" stroke="#a89c88" stroke-width="3" stroke-dasharray="8 6"/><text x="270" y="168" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="20" fill="#7a6a52">Patio · no heads</text>
<circle cx="70" cy="150" r="34" fill="#9cc48a"/><circle cx="470" cy="150" r="34" fill="#9cc48a"/><g transform="translate(0,230)">{z}
<rect x="150" y="196" width="240" height="120" rx="8" fill="#e7ddcf" stroke="#5c5346" stroke-width="4"/><text x="270" y="264" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="24" fill="#5c5346">House</text>
<rect x="30" y="196" width="100" height="44" rx="8" fill="#ffffff" stroke="#1f5f99" stroke-width="3"/><text x="80" y="225" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="18" fill="#1f5f99">Valve box</text>
<rect x="404" y="196" width="106" height="44" rx="8" fill="#ffffff" stroke="#1f5f99" stroke-width="3"/><text x="457" y="225" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="18" fill="#1f5f99">Backflow</text>
<rect x="0" y="560" width="540" height="40" fill="#c9ccd1"/><text x="270" y="587" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="18" fill="#4a4f57">Sample Street</text></g></svg>'''
P["p295_sprinkler"] = page("""
body{--f:'Roboto';--h:'Crimson Text';background:#eef3f6;color:#1e3346}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#5d7a2e;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:68px;line-height:1.2} h1 span{color:#2c79b8}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.yc{width:520px;flex:none;background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(30,51,70,.08)}
.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6f7b85}
.yd{flex:1;min-height:0;width:100%;display:block;border-radius:12px}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.fm{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(30,51,70,.08)}
.fr{flex:1;display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid #e8eef2}.fr:last-child{border:0}.fr span{font:600 15px 'Roboto';color:#6f7b85}.fr b{font:700 28px/1.3 'Crimson Text'}
.rt{background:#1e3346;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.rt small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#a9d4f5}
.rr{display:flex;justify-content:space-between;font:500 17px/1.4 'Roboto';color:#cfdbe6}.rr b{color:#fff}.rr.on b{color:#a9d4f5}
""", "<div class=kk>SPRINKLER BLOWOUT · FALL BOOKINGS</div><h1>Blowout season is short.<br><span>Book by zones and street.</span></h1>",
f'''<div class=vw><div class=yc><small class=cap>SAMPLE YARD · 5 ZONES · 20 HEADS</small>{yard()}</div>
<div class=rc><div class=fm><small class=cap>BOOKING FORM · SAMPLE</small>{"".join(f'<div class=fr><span>{a}</span><b>{b}</b></div>' for a,b in [("Zones","5"),("Valve box","Left side of the house"),("Backflow","Right side, outside"),("Water shutoff","Found, in the basement"),("Day","Sat 5 Dec · morning")])}</div>
<div class=rt><small>SAT 5 DEC · SAME STREET ROUTE</small>{"".join(f'<div class="rr{" on" if n=="Your home" else ""}"><span>{t}</span><b>{n}</b></div>' for t,n in [("8:00 AM","House 12"),("8:40 AM","House 18"),("9:20 AM","Your home"),("10:00 AM","House 31")])}</div></div></div>''',
"#1e3346", "Do sprinkler blowouts? DM us", "background:#2c79b8;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
