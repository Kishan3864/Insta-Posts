import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 44 CANADA · Painting contractor · CAROUSEL 5 · Gelasio + DM Sans · white / paint swatch strip
# New technique: paint-chip swatch strips as section markers + roller stroke band.
SW = ["#e76f51", "#f4a261", "#e9c46a", "#2a9d8f", "#264653"]
PC = """
body{--f:'DM Sans';--h:'Gelasio';background:#fbfaf7;color:#1f2b33}
.stroke{position:absolute;left:-40px;right:-40px;top:300px;height:150px;background:#2a9d8f;border-radius:80px 30px 90px 40px/60px 70px 50px 80px;opacity:.12;transform:rotate(-3deg)}
h1{font-family:'Gelasio';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#e76f51;font-style:italic}
.sub{color:#5c6870}
.sn{display:flex;gap:6px;align-items:center;margin-top:22px;font:700 17px 'DM Sans';letter-spacing:3px;color:#264653}
.sn i{width:22px;height:22px;border-radius:5px;display:block}
.card{background:#fff;border-radius:24px;box-shadow:0 20px 44px rgba(31,43,51,.1)}
"""
def pslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#264653;color:#fff"):
    chips = "".join(f'<i style="background:{c}"></i>' for c in SW[:n])
    return page(PC+css, f"<div class=sn>{chips}<span style='margin-left:8px'>{kick}</span></div><h1 style='margin-top:12px'>{title}</h1><div class=sub>{sub}</div>", vis, "#1f2b33", cta, ctacss, bg="<div class=stroke></div>", tagline=f"{n} / 5")

P["p44_painter_s1"] = pslide(1, "FOR PAINTING CONTRACTORS", "From walk-through<br>to final touch-up,<br><span>nothing lost.</span>",
 "How painting software keeps every job clear. Swipe through 3 steps.",
 f'''<div class=chipset>{"".join(f'<div class=pc style="--c:{c}"><div class=top></div><div class=bt><b>{a}</b><small>{b}</small></div></div>' for c,a,b in [(SW[0],"Step 1","Estimate by room"),(SW[2],"Step 2","Colours and photos"),(SW[3],"Step 3","Schedule and touch-ups"),(SW[4],"You","Fewer calls, cleaner jobs")])}</div>''',
 """.vis{display:flex}.chipset{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.pc{background:#fff;border-radius:16px;box-shadow:0 20px 44px rgba(31,43,51,.12);display:flex;flex-direction:column;overflow:hidden}
.pc .top{flex:1;background:var(--c)}.pc .bt{padding:18px 16px;display:flex;flex-direction:column;gap:4px}.pc b{font:700 26px 'Gelasio'}.pc small{font:500 18px/1.35 'DM Sans';color:#5c6870}""")

rooms = [("Living room", "Walls + ceiling", "2 coats"), ("Kitchen", "Walls + cabinets", "Primer + 2 coats"), ("Main bedroom", "Walls", "2 coats"),
         ("Hallway", "Walls + trim", "2 coats"), ("Bathroom", "Walls", "Moisture-safe paint"), ("Front door", "Exterior", "1 coat + touch-up")]
P["p44_painter_s2"] = pslide(2, "STEP 1 · ESTIMATE", "Estimate room by room,<br><span>during the walk-through.</span>",
 "Add each room on a tablet. The estimate is ready before you leave the house.",
 f'''<div class="card es"><div class=eh><b>Estimate · sample home</b><span>Walk-through · Tue 10 AM</span></div>{"".join(f'<div class=rm><span class=dt style="background:{SW[i%5]}"></span><div style="flex:1"><b>{a}</b><small>{b}</small></div><i>{c}</i></div>' for i,(a,b,c) in enumerate(rooms))}<div class=sd>Send estimate to the customer</div></div>''',
 """.vis{display:flex}.es{flex:1;padding:24px;display:flex;flex-direction:column;gap:10px}
.eh{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}.eh b{font:700 27px 'Gelasio'}.eh span{font:500 16px 'DM Sans';color:#5c6870}
.rm{flex:1;display:flex;align-items:center;gap:14px;background:#f5f3ee;border-radius:14px;padding:0 16px}.rm .dt{width:20px;height:44px;border-radius:5px;flex:none}
.rm b{display:block;font:700 20px 'DM Sans'}.rm small{display:block;font:400 16px 'DM Sans';color:#5c6870}.rm i{font-style:normal;font:600 16px 'DM Sans';color:#264653}
.sd{background:#e76f51;color:#fff;border-radius:14px;padding:16px;text-align:center;font:700 19px 'DM Sans'}""")

cols = [("Living room", "Warm white · sample code W-102", "#f3efe6"), ("Kitchen cabinets", "Deep teal · sample code T-415", "#2a9d8f"), ("Main bedroom", "Soft clay · sample code C-208", "#e9b9a0"), ("Front door", "Charcoal · sample code G-990", "#264653")]
P["p44_painter_s3"] = pslide(3, "STEP 2 · COLOURS + PHOTOS", "Colours approved,<br><span>in writing, per room.</span>",
 "No more \"I thought it was the lighter one.\" Every colour is signed off before you start.",
 f'''<div class=g2>{"".join(f'<div class="card cc"><div class=sw style="background:{c}"></div><div class=ct><b>{a}</b><small>{b}</small><span>{ic("check",16,w=3)} Approved by customer</span></div></div>' for a,b,c in cols)}</div>''',
 """.vis{display:flex}.g2{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.cc{display:flex;flex-direction:column;overflow:hidden}.cc .sw{flex:1;border-bottom:1px solid #eee}.ct{padding:18px 20px;display:flex;flex-direction:column;gap:4px}
.ct b{font:700 24px 'Gelasio'}.ct small{font:500 16px 'DM Sans';color:#5c6870}.ct span{display:flex;gap:6px;align-items:center;font:700 15px 'DM Sans';color:#2a7d50;margin-top:4px}""")

days = [("Mon", "Prep + patch", "Crew A", "d"), ("Tue", "Primer", "Crew A", "d"), ("Wed", "Coat 1", "Crew A + B", "n"), ("Thu", "Coat 2", "Crew A + B", ""), ("Fri", "Trim + doors", "Crew B", ""), ("Sat", "Walk-through + touch-ups", "Owner", "")]
P["p44_painter_s4"] = pslide(4, "STEP 3 · SCHEDULE + TOUCH-UPS", "Every day planned.<br><span>Touch-ups tracked.</span>",
 "The customer sees the plan. The final walk-through list gets ticked off.",
 f'''<div class="card sc">{"".join(f'<div class="dy {c}"><b>{a}</b><span>{t}</span><small>{w}</small></div>' for a,t,w,c in days)}</div>
 <div class="card tu"><b class=th>Touch-up list · sample</b>{"".join(f'<div class=ti><span class="bx {"on" if k else ""}">{"✓" if k else ""}</span>{t}</div>' for t,k in [("Hallway corner scuff",1),("Kitchen trim drip",1),("Bedroom outlet edge",0),("Front door handle tape",0)])}</div>''',
 """.vis{gap:16px;align-items:stretch}.sc{flex:1.2;padding:18px;display:flex;flex-direction:column;gap:8px;min-width:0}
.dy{flex:1;display:grid;grid-template-columns:70px 1fr auto;align-items:center;gap:12px;background:#f5f3ee;border-radius:12px;padding:0 16px}
.dy b{font:700 19px 'DM Sans'}.dy span{font:600 18px 'DM Sans'}.dy small{font:500 15px 'DM Sans';color:#5c6870}
.dy.d{background:#e3f1ec}.dy.d b{color:#2a7d50}.dy.n{background:#fde9e3;box-shadow:inset 0 0 0 2px #e76f51}
.tu{flex:1;padding:22px;display:flex;flex-direction:column;gap:12px;min-width:0}.th{font:700 23px 'Gelasio'}
.ti{flex:1;display:flex;gap:12px;align-items:center;font:600 19px/1.3 'DM Sans';border-bottom:1px dashed #ddd}
.bx{width:30px;height:30px;border-radius:8px;border:2px solid #264653;display:flex;align-items:center;justify-content:center;font:700 17px 'DM Sans';flex:none}.bx.on{background:#264653;color:#fff}""")

P["p44_painter_s5"] = pslide(5, "YOUR CREW, YOUR WAY", "Want this for your<br><span>painting business?</span>",
 "We build estimate, colour approval and scheduling tools for painting contractors in Canada and the US.",
 f'''<div class=w>{peep("Explaining","Smile","ShortCurly","GoateeCircle",w=400,h=640)}<div class=lst>{"".join(f'<div class=i style="border-left:14px solid {SW[k]}"><b>{a}</b><small>{b}</small></div>' for k,(a,b) in enumerate([("Room-by-room estimates","Ready before you leave"),("Colour sign-off","No repaint surprises"),("Crew schedule","Everyone knows the plan"),("Touch-up list","Close jobs cleanly")]))}</div></div>''',
 """.vis{align-items:stretch}.w{display:flex;align-items:flex-end;gap:20px;width:100%}
.lst{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px;padding-bottom:6px}
.i{flex:1;background:#fff;border-radius:16px;padding:0 24px;display:flex;flex-direction:column;justify-content:center;gap:4px;box-shadow:0 14px 30px rgba(31,43,51,.08)}
.i b{font:700 27px 'Gelasio'}.i small{font:500 19px 'DM Sans';color:#5c6870}""",
 cta="Tell us about your jobs. DM us", ctacss="background:#e76f51;color:#fff")

# ───────── 45 INDIA · Juice & shake bar · SINGLE · TeX Gyre Adventor + Open Sans · mango / leaf / cream
# New technique: "paper pile vs one card" — scattered stamp cards vs a single clean digital stamp card on a counter tablet.
def pcard(x, y, r, n):
    st = "".join(f'<i class="{"on" if k < n else ""}"></i>' for k in range(8))
    return f'<div class=pcard style="left:{x}px;top:{y}px;transform:rotate({r}deg)"><b>Juice card</b><div class=st>{st}</div></div>'
P["p45_juicebar"] = page("""
body{--f:'Open Sans';--h:'TeX Gyre Adventor';background:#fff6e6;color:#1f3d1f}
h1{font-family:'TeX Gyre Adventor';font-size:66px;font-weight:700;letter-spacing:-1.5px} h1 span{color:#ff8a00}
.sub{color:#5d6b55}
.vis{gap:20px;align-items:stretch}
.pile{flex:1;background:#f3e6cf;border-radius:26px;position:relative;overflow:hidden;min-width:0}
.pile .lb{position:absolute;left:22px;top:20px;font:800 16px 'Open Sans';letter-spacing:3px;color:#a0622a;z-index:9}
.pcard{position:absolute;width:250px;background:#fffdf6;border:2px solid #e2cfae;border-radius:14px;padding:14px;box-shadow:0 10px 20px rgba(80,50,10,.12)}
.pcard b{font:700 17px 'TeX Gyre Adventor';color:#8a5a12}.st{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-top:10px}
.st i{height:38px;border-radius:50%;border:2px dashed #d6bf96;display:block}.st i.on{background:#ffb347;border:0}
.lost{position:absolute;left:30px;bottom:24px;right:30px;z-index:9;background:#1f3d1f;color:#fff;border-radius:16px;padding:14px 16px;font:600 18px/1.35 'Open Sans'}
.tab{flex:1;background:#1f3d1f;border-radius:30px;padding:16px;min-width:0;display:flex}
.scr{flex:1;background:#fff;border-radius:18px;padding:22px;display:flex;flex-direction:column;gap:12px}
.scr .lb{font:800 16px 'Open Sans';letter-spacing:3px;color:#2e7d32}
.cu{display:flex;gap:12px;align-items:center}.cu .av{width:54px;height:54px;border-radius:50%;background:#ff8a00;color:#fff;font:700 22px/1 'TeX Gyre Adventor';display:flex;align-items:center;justify-content:center}
.cu b{display:block;font:700 21px 'Open Sans'}.cu small{font:500 15px 'Open Sans';color:#6b7a63}
.dg{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.dg i{aspect-ratio:1;border-radius:50%;background:#eef5e6;display:flex;align-items:center;justify-content:center;color:#b8c9a8}
.dg i.on{background:#ff8a00;color:#fff}.dg i.fr{background:#2e7d32;color:#fff;font:800 13px 'Open Sans';font-style:normal}
.nx{background:#fff3df;border-radius:14px;padding:14px;font:600 18px/1.35 'Open Sans'}
.cmb{flex:1;display:flex;flex-direction:column;gap:8px}.cb{flex:1;display:flex;justify-content:space-between;align-items:center;background:#f6f8f2;border-radius:12px;padding:0 16px;font:600 20px 'Open Sans'}
.cb span{font:700 16px 'Open Sans';color:#2e7d32}
""", "<h1>Stamp cards get lost.<br><span>Phone numbers don't.</span></h1><div class=sub>For juice and shake bars: loyalty that lives on your counter tablet, not in a wallet.</div>",
f'''<div class=pile><div class=lb>BEFORE</div>{pcard(30,70,-8,3)}{pcard(170,170,6,5)}{pcard(40,300,4,2)}{pcard(190,390,-5,6)}{pcard(60,520,9,1)}<div class=lost>"I forgot my card at home." Every day.</div></div>
<div class=tab><div class=scr><div class=lb>AFTER · SAMPLE</div><div class=cu><span class=av>R</span><div><b>Regular customer</b><small>Found by phone number</small></div></div>
<div class=dg>{"".join(f'<i class=on>{ic("cup",22)}</i>' for _ in range(6))}<i>{ic("cup",22)}</i><i class=fr>FREE</i></div>
<div class=nx>1 more visit for a free juice.</div><div class=cmb>{"".join(f'<div class=cb>{a}<span>{b}</span></div>' for a,b in [("Combo: juice + sandwich","Popular"),("Combo: shake + fries","New"),("Today's special","On the menu QR")])}</div></div></div>''',
"#1f3d1f", "Want loyalty for your juice bar? DM us", "background:#ff8a00;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
