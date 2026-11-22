import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 161 INDIA · Event chair & table rental · SINGLE · Archivo Black + Source Sans 3 · terracotta / sand / ink navy
# New technique: SVG stack of nested plastic chairs as the stock hero + per-event "out / back" challan cards with a godown total.
def chair_stack(n=6):
    g = ""
    for i in range(n):
        g += (f'<g transform="translate({i*8},{-i*30})" stroke="#8f3519" stroke-width="3" stroke-linejoin="round">'
              f'<path d="M66 156 L88 34 Q91 22 104 22 L170 22 Q182 22 180 34 L176 60 Q174 70 162 70 L110 70 L96 156 Z" fill="#d9663e"/>'
              f'<rect x="56" y="148" width="156" height="20" rx="8" fill="#e2774f"/>'
              f'<path d="M70 168 L54 300 L66 300 L84 168 Z M186 168 L202 300 L214 300 L198 168 Z" fill="#b04724"/></g>')
    return f'<svg viewBox="40 -150 230 470" width="250" style="display:block">{g}<rect x="40" y="300" width="230" height="10" rx="5" fill="#1d2a44"/></svg>'
ev = [("Sample Lawn Party", "Sat, 21 Nov", "200 chairs · 20 tables", "196 chairs · 20 tables", "4 chairs short", "sh"),
      ("Sample Office Event", "Sat, 21 Nov", "150 chairs · 15 tables", "150 chairs · 15 tables", "All back", "ok"),
      ("Sample Family Function", "Sun, 22 Nov", "120 chairs · 12 tables", "Pickup today, 6 PM", "Still out", "out")]
P["p161_chairs"] = page("""
body{--f:'Source Sans 3';--h:'Archivo Black';background:#f3e9da;color:#1d2a44}
h1{font-family:'Archivo Black';font-weight:400;font-size:62px;letter-spacing:-.5px;line-height:1.22;margin-top:30px} h1 span{color:#c4532d}
.sub{color:#5a5f6e;font-size:24px}
.vis{gap:20px}
.gd{width:330px;flex:none;background:#1d2a44;color:#fff;border-radius:28px;padding:24px 22px;display:flex;flex-direction:column;align-items:center;gap:14px}
.gd small{font:700 15px 'Source Sans 3';letter-spacing:2.5px;color:#e9b48f;align-self:flex-start}
.gd .art{flex:1;display:flex;align-items:flex-end;justify-content:center;background:#f3e9da;border-radius:20px;align-self:stretch;padding:16px 0 18px}
.gd .tot{align-self:stretch;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.gd .tot div{background:rgba(255,255,255,.08);border-radius:16px;padding:12px 14px}.gd .tot b{display:block;font:400 34px/1.3 'Archivo Black'}.gd .tot span{font:600 17px 'Source Sans 3';color:#cfd6e4}
.evs{flex:1;display:flex;flex-direction:column;gap:14px}
.ev{flex:1;background:#fff;border-radius:24px;padding:14px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px;box-shadow:0 14px 30px rgba(29,42,68,.08)}
.ev .tp{display:flex;justify-content:space-between;align-items:baseline}.ev .tp b{font:700 28px 'Source Sans 3'}.ev .tp span{font:600 19px 'Source Sans 3';color:#8a8f9c}
.ev .rw{display:flex;gap:10px}.ev .rw div{flex:1;background:#f6f1e9;border-radius:14px;padding:8px 14px;display:flex;flex-direction:column;gap:2px}
.ev .rw small{display:block;font:700 13px 'Source Sans 3';letter-spacing:2px;color:#a0846c}.ev .rw p{font:600 21px/1.3 'Source Sans 3'}
.ev em{align-self:flex-start;font-style:normal;font:700 18px 'Source Sans 3';border-radius:12px;padding:7px 14px}
.sh{background:#fbdcd0;color:#a33a17}.ok{background:#dcefe2;color:#1f6a3d}.out{background:#fff0c2;color:#6e5300}
.nw{background:#c4532d;color:#fff;border-radius:20px;padding:16px 20px;font:600 20px/1.4 'Source Sans 3'}.nw b{font-weight:800}
""", "<h1>Chairs went to 3 events.<br><span>How many came back?</span></h1><div class=sub>Count out and back per event, and see the godown stock live.</div>",
f'''<div class=gd><small>GODOWN · SAMPLE</small><div class=art>{chair_stack()}</div>
<div class=tot><div><b>500</b><span>chairs owned</span></div><div><b>60</b><span>tables owned</span></div><div><b>376</b><span>chairs in now</span></div><div><b>48</b><span>tables in now</span></div></div></div>
<div class=evs>{"".join(f'<div class=ev><div class=tp><b>{a}</b><span>{d}</span></div><div class=rw><div><small>OUT</small><p>{o}</p></div><div><small>BACK</small><p>{bk}</p></div></div><em class={k}>{s}</em></div>' for a,d,o,bk,s,k in ev)}
<div class=nw><b>4 chairs short</b> at the lawn party are marked on the bill, so you never lose count.</div></div>''',
"#1d2a44", "Rent chairs and tables? DM us", "background:#1d2a44;color:#fff")


# ───────── 162 USA · Garage door repair · CAROUSEL 6 · Poppins + Fira Sans · graphite / lime / white
# New techniques: SVG garage door with sectional panels (one panel crooked), problem-tile picker form, SVG street dispatch map with numbered pins.
GD = """
body{--f:'Fira Sans';--h:'Poppins';background:#24272c;color:#fff}
h1{font-family:'Poppins';font-weight:800;font-size:60px;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#b7e34a}
.sub{color:#b5bac3;font-size:23px}
.kk{font:700 16px 'Fira Sans';letter-spacing:3px;color:#b7e34a;margin-top:22px}
.cd{background:#fff;color:#24272c;border-radius:24px}
.lm{background:#b7e34a;color:#1b1e22}
"""
def gd(n, head, vis, css="", cta="Swipe", ctacss="background:#b7e34a;color:#1b1e22"):
    return page(GD + css, head, vis, "#ffffff", cta, ctacss, tagline=f"{n} / 6", logo_color="#ffffff")
def door(w=620, broken=True, uid="a"):
    panels = ""
    for i in range(4):
        y = 70 + i * 52
        rot = ' transform="rotate(-4 300 %d)"' % (y + 26) if (broken and i == 2) else ""
        panels += f'<g{rot}><rect x="110" y="{y}" width="380" height="48" rx="4" fill="#e8ebef" stroke="#9aa1ab" stroke-width="2"/>' + "".join(f'<rect x="{126+j*92}" y="{y+10}" width="76" height="28" rx="3" fill="#d3d8de"/>' for j in range(4)) + '</g>'
    return (f'<svg viewBox="0 0 600 330" width="{w}" style="display:block"><path d="M40 70 L300 0 L560 70 Z" fill="#3a3f47"/>'
            f'<rect x="70" y="60" width="460" height="250" fill="#f2efe8"/><rect x="100" y="64" width="400" height="246" fill="#2b2f35"/>{panels}'
            f'<rect x="0" y="308" width="600" height="14" rx="7" fill="#596069"/>'
            + (f'<g><circle cx="470" cy="190" r="30" fill="#b7e34a"/><path d="M470 174 V194 M470 204 V206" stroke="#1b1e22" stroke-width="7" stroke-linecap="round"/></g>' if broken else '<g><circle cx="470" cy="120" r="30" fill="#b7e34a"/><path d="M456 120 L466 130 L485 110" fill="none" stroke="#1b1e22" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></g>')
            + '</svg>')
P["p162_gdoor_s1"] = gd(1, "<div class=kk>GARAGE DOOR REPAIR</div><h1>Door stuck at 6:50 AM?<br><span>Let them book before you open.</span></h1>",
f'''<div class="cd hero">{door(800)}<div class=al><div class=ai>{ic("bell",30)}</div><div><small>NEW REQUEST · 6:52 AM · SAMPLE</small><b>Door won't open, one panel bent</b><span>ZIP 75201 · in your service area · 2 photos</span></div></div></div>''',
css=""".vis{flex-direction:column}.hero{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:26px 28px;background:#f4f5f6}
.al{align-self:stretch;display:flex;gap:18px;align-items:center;background:#fff;border-radius:20px;padding:18px 20px;box-shadow:0 14px 30px rgba(0,0,0,.10)}
.ai{width:64px;height:64px;border-radius:18px;background:#24272c;color:#b7e34a;display:flex;align-items:center;justify-content:center;flex:none}
.al small{display:block;font:700 14px 'Fira Sans';letter-spacing:2px;color:#7b828c}.al b{display:block;font:700 27px/1.3 Poppins}.al span{font:500 19px 'Fira Sans';color:#5b626c}""")

probs = [("Won't open", 1), ("Won't close", 0), ("Broken spring", 0), ("Off track", 0), ("Loud noise", 0), ("Remote not working", 0)]
P["p162_gdoor_s2"] = gd(2, "<div class=kk>PART 1 · AFTER-HOURS FORM</div><h1>Calls missed at night?<br><span>A form that books the job.</span></h1>",
browser(f'''<div class=fm><b class=t>What's wrong with your door?</b>
<div class=pt>{"".join(f'<div class="{"on" if o else ""}">{ic("check",22,w=3) if o else ""}<span>{a}</span></div>' for a,o in probs)}</div>
<div class=r2><div class=fl><small>ZIP CODE</small><span>75201</span><em>In service area</em></div><div class=fl><small>PHOTOS</small><span>2 added</span></div></div>
<div class=fl><small>PICK A TIME</small><div class=tw>{"".join(f'<i class="{"on" if k else ""}">{t}</i>' for t,k in [("7–9 AM",1),("9–11 AM",0),("11–1 PM",0),("2–4 PM",0)])}</div></div>
<div class=bt>Book my repair</div></div>''', url="yourgaragedoors.com/book · sample", style="flex:1"),
css=""".vis{display:flex}.fm{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:14px;color:#24272c}
.fm .t{font:700 30px Poppins}
.pt{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px;flex:1}.pt div{border:2px solid #dfe2e6;border-radius:16px;display:flex;align-items:center;justify-content:center;gap:8px;font:600 25px 'Fira Sans';text-align:center;padding:0 8px}
.pt .on{background:#b7e34a;border-color:#b7e34a}
.r2{display:flex;gap:12px}.r2 .fl{flex:1}
.fl{background:#f1f2f4;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;gap:4px}.fl small{font:700 13px 'Fira Sans';letter-spacing:2px;color:#7b828c}.fl span{font:700 24px 'Fira Sans'}
.fl em{align-self:flex-start;font-style:normal;font:700 15px 'Fira Sans';background:#dcefcf;color:#2f5b0f;border-radius:10px;padding:5px 10px}
.tw{display:flex;gap:10px;margin-top:4px}.tw i{flex:1;font-style:normal;text-align:center;font:600 19px 'Fira Sans';background:#fff;border-radius:12px;padding:12px 0}.tw .on{background:#24272c;color:#b7e34a}
.bt{background:#24272c;color:#fff;border-radius:16px;padding:18px;text-align:center;font:700 22px Poppins}""")

pins = [(1, 160, 170, "d"), (2, 380, 150, "d"), (3, 530, 400, "o"), (4, 230, 560, "n"), (5, 480, 740, "n")]
streets = "".join(f'<rect x="0" y="{y}" width="640" height="26" fill="#ffffff"/>' for y in [90, 300, 480, 660, 820]) + "".join(f'<rect x="{x}" y="0" width="26" height="880" fill="#ffffff"/>' for x in [90, 300, 450])
jobs = [(1, "7:00 AM", "Broken spring", "Tech 1", "d", "Done"), (2, "8:00 AM", "Off track", "Tech 2", "d", "Done"), (3, "9:30 AM", "Won't open", "Tech 1", "o", "On the way"),
        (4, "11:00 AM", "Loud noise", "Tech 2", "n", "Next"), (5, "1:00 PM", "Remote issue", "Tech 1", "n", "Next")]
P["p162_gdoor_s3"] = gd(3, "<div class=kk>PART 2 · DISPATCH MAP</div><h1>Who goes where?<br><span>Jobs on a map, by time.</span></h1>",
f'''<div class="cd mp"><svg viewBox="0 0 640 880" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block"><rect width="640" height="880" rx="20" fill="#e6e9dd"/>{streets}
<path d="M160 170 L530 400 L480 740" fill="none" stroke="#24272c" stroke-width="6" stroke-dasharray="12 10"/>
{"".join(f'<g><circle cx="{x}" cy="{y}" r="30" fill="{dict(d="#24272c",o="#b7e34a",n="#ffffff")[k]}" stroke="#24272c" stroke-width="4"/><text x="{x}" y="{y+10}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="28" fill="{dict(d="#b7e34a",o="#1b1e22",n="#24272c")[k]}"><tspan>{n}</tspan></text></g>' for n,x,y,k in pins)}</svg></div>
<div class=jl>{"".join(f'<div class=jb><i class={k}>{n}</i><div><b>{t}</b><span>{p}</span><small>{te} · {s}</small></div></div>' for n,t,p,te,k,s in jobs)}</div>''',
css=""".vis{gap:16px}.mp{flex:1;padding:14px;display:flex}.mp svg{flex:1}
.jl{width:330px;flex:none;display:flex;flex-direction:column;gap:10px}
.jb{flex:1;background:#fff;color:#24272c;border-radius:20px;display:flex;align-items:center;gap:14px;padding:0 16px}
.jb i{width:50px;height:50px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font:800 22px Poppins;font-style:normal;border:3px solid #24272c}
.jb i.d{background:#24272c;color:#b7e34a}.jb i.o{background:#b7e34a}.jb i.n{background:#fff}
.jb b{display:block;font:700 25px Poppins}.jb span{display:block;font:600 22px 'Fira Sans'}.jb small{font:500 18px 'Fira Sans';color:#6b727c}""")

parts = [("Torsion spring", "2"), ("Rollers", "10"), ("Lift cable", "2"), ("Bent panel", "Ordered")]
P["p162_gdoor_s4"] = gd(4, "<div class=kk>PART 3 · JOB CARD</div><h1>Parts, photos, sign-off.<br><span>All on one job card.</span></h1>",
f'''<div class="cd jc"><div class=jh><div><small>JOB #1042 · SAMPLE</small><b>Double door · 16 × 7 ft</b></div><em>Tech 1 · 9:30 AM</em></div>
<div class=bd><div class=pl><small>PARTS USED</small>{"".join(f'<div class=pr><span>{a}</span><b>{q}</b></div>' for a,q in parts)}</div>
<div class=ph><small>PHOTOS</small><div class=pp><div><span class=tg>Before</span>{door(330, True)}</div><div><span class="tg lm">After</span>{door(330, False)}</div></div></div></div>
<div class=sg><div><small>CUSTOMER SIGN-OFF</small><svg viewBox="0 0 300 60" width="260" style="display:block"><path d="M10 40 C40 10 60 50 90 30 S140 10 160 38 S220 50 290 20" fill="none" stroke="#24272c" stroke-width="4" stroke-linecap="round"/></svg></div><div class=nx2><small>NEXT TUNE-UP</small><b>In 12 months</b></div></div></div>''',
css=""".vis{display:flex}.jc{flex:1;padding:24px 26px;display:flex;flex-direction:column;gap:16px}
.jc small{display:block;font:700 13px 'Fira Sans';letter-spacing:2px;color:#7b828c;margin-bottom:6px}
.jh{display:flex;justify-content:space-between;align-items:center}.jh b{font:800 30px Poppins}.jh em{font-style:normal;font:700 18px 'Fira Sans';background:#24272c;color:#b7e34a;border-radius:12px;padding:9px 14px}
.bd{flex:1;display:flex;gap:16px;min-height:0}.pl{width:340px;flex:none;background:#f1f2f4;border-radius:18px;padding:16px 18px;display:flex;flex-direction:column}
.pr{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid #dfe2e6;font:600 26px 'Fira Sans'}.pr b{font:800 26px Poppins}
.ph{flex:1;display:flex;flex-direction:column}.pp{flex:1;display:flex;flex-direction:column;gap:12px}.pp div{flex:1;background:#f1f2f4;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:10px}
.tg{font:700 16px 'Fira Sans';background:#24272c;color:#fff;border-radius:10px;padding:4px 12px}.tg.lm{background:#b7e34a;color:#1b1e22}
.sg{display:flex;gap:16px}.sg>div{flex:1;background:#f1f2f4;border-radius:18px;padding:14px 18px}.nx2{display:flex;flex-direction:column;justify-content:center}.nx2 b{font:800 28px Poppins}""")

msgs = [("in", "Hi! Your repair is booked for today, 7 to 9 AM. Tech 1 will text when on the way.", "6:53 AM"),
        ("in", "Tech 1 is on the way. Arriving in about 15 minutes.", "9:12 AM"),
        ("out", "Great, the gate code is on the form.", "9:13 AM"),
        ("in", "All done! Your job card and photos are in your email.", "10:20 AM")]
P["p162_gdoor_s5"] = gd(5, "<div class=kk>PART 4 · CUSTOMER TEXTS</div><h1>“When will the tech come?”<br><span>Answered by text, on time.</span></h1>",
f'''<div class="cd tx"><div class=th3><span class=av>{ic("wrench",26)}</span><div><b>Your Garage Doors</b><small>TEXT UPDATES · SAMPLE</small></div></div>
<div class=ms>{"".join(f'<div class="m {d}"><p>{t}</p><small>{tm}</small></div>' for d,t,tm in msgs)}</div></div>
<div class=sd>{"".join(f'<div><span class=ib>{ic(i,28)}</span><b>{a}</b><span class=s2>{b}</span></div>' for i,a,b in [("check","Booked","sent on its own"),("truck","On the way","with arrival time"),("doc","Job done","card and photos"),("bell","Tune-up","reminder in 12 months")])}</div>''',
css=""".vis{gap:16px}.tx{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:14px;background:#f4f5f6}
.th3{display:flex;gap:14px;align-items:center}.av{width:56px;height:56px;border-radius:50%;background:#24272c;color:#b7e34a;display:flex;align-items:center;justify-content:center}.th3 b{display:block;font:700 23px Poppins}.th3 small{font:700 13px 'Fira Sans';letter-spacing:2px;color:#7b828c}
.ms{flex:1;display:flex;flex-direction:column;justify-content:space-around;gap:10px}
.m{max-width:86%;border-radius:20px;padding:14px 18px}.m p{font:500 24px/1.4 'Fira Sans'}.m small{display:block;font:600 14px 'Fira Sans';opacity:.6;margin-top:4px}
.m.in{background:#fff;align-self:flex-start;border-bottom-left-radius:6px}.m.out{background:#b7e34a;align-self:flex-end;border-bottom-right-radius:6px}
.sd{width:290px;flex:none;display:flex;flex-direction:column;gap:12px}.sd div{flex:1;background:#33373e;border-radius:20px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.sd .ib{width:48px;height:48px;border-radius:14px;background:#b7e34a;color:#1b1e22;margin-bottom:4px}.sd b{font:700 27px Poppins}.sd .s2{font:500 20px 'Fira Sans';color:#b5bac3}""")

P["p162_gdoor_s6"] = gd(6, "<div class=kk>YOUR TURN</div><h1>Fix garage doors?<br><span>Let's build your booking and dispatch app.</span></h1>",
f'''<div class="cd hero2">{door(780, False)}</div><div class=rw3>{"".join(f'<div><span class=ib>{ic(i,28)}</span><b>{a}</b></div>' for i,a in [("doc","After-hours form"),("map","Dispatch map"),("file","Job cards"),("chat","Customer texts")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.hero2{flex:1;display:flex;align-items:center;justify-content:center;padding:24px;background:#f4f5f6}
.rw3{display:grid;grid-template-columns:1fr 1fr;gap:14px}.rw3 div{background:#33373e;border-radius:22px;padding:24px 22px;display:flex;align-items:center;gap:16px}
.rw3 .ib{width:58px;height:58px;border-radius:16px;background:#b7e34a;color:#1b1e22}.rw3 b{font:700 27px Poppins}""",
cta="DM us to start")


# ───────── 163 INDIA · Gas stove repair service · SINGLE · Lora + Open Sans · flame blue / copper / cream
# New technique: top-down open technician toolbox with compartments (spare part counts, low stock in copper) linked to a phone visit list that names the part each visit needs.
box = [("Burner caps", "6", ""), ("Knobs", "12", ""), ("Brass nozzles", "20", ""), ("Igniters", "4", ""), ("Gas hose pipes", "1", "lo"), ("Pan supports", "3", "")]
vis163 = [("10:00", "Sample Flat 2B", "Burner not lighting", "Igniter", "ok"), ("11:30", "Sample House 14", "Yellow flame", "Nozzle", "ok"),
          ("1:00", "Sample Flat 7A", "Knob loose", "Knob", "ok"), ("3:00", "Sample Shop 3", "Old gas hose", "Hose pipe", "ok"), ("5:00", "Sample Flat 9C", "Hose pipe change", "Hose pipe", "no")]
P["p163_stove"] = page("""
body{--f:'Open Sans';--h:'Lora';background:#f7efe2;color:#1c2b4a}
h1{font-family:'Lora';font-size:60px;font-weight:700;letter-spacing:-.6px;line-height:1.22} h1 span{color:#2b63d9}
.sub{color:#5c6170;font-size:23px}
.vis{gap:22px;align-items:stretch}
.tb{flex:1;display:flex;flex-direction:column;gap:14px}
.lid{height:54px;border-radius:20px 20px 8px 8px;background:linear-gradient(#c7773f,#a85f2c);display:flex;align-items:center;justify-content:center;gap:12px;color:#fff;font:700 19px 'Open Sans';letter-spacing:2px}
.lid i{width:90px;height:14px;border-radius:7px;background:#7d4520}
.bx{flex:1;background:#a85f2c;border-radius:12px 12px 26px 26px;padding:14px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:12px}
.cp{background:#fdf6ea;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:inset 0 4px 0 rgba(0,0,0,.08)}
.cp span{font:700 23px/1.3 'Open Sans'}.cp b{font:700 72px/1.2 Lora;color:#1c2b4a}.cp.lo{background:#ffe1cc}.cp.lo b{color:#b4531b}
.cp em{font-style:normal;font:700 14px 'Open Sans';color:#b4531b;letter-spacing:1px}
.al2{background:#1c2b4a;color:#fff;border-radius:18px;padding:14px 18px;font:600 19px/1.4 'Open Sans'}.al2 b{color:#ffb27a}
.pv{display:flex;flex-direction:column;padding:4px 16px 16px;gap:8px;flex:1}
.pv .h{font:700 27px Lora;margin-top:4px}.pv small.t{font:700 12px 'Open Sans';letter-spacing:2px;color:#8a8f9c}
.vr{flex:1;background:#f2f5fb;border-radius:14px;padding:6px 12px;display:flex;flex-direction:column;justify-content:center;gap:1px}
.vr .tm{display:flex;justify-content:space-between;font:700 16px 'Open Sans';color:#2b63d9}.vr b{font:700 19px 'Open Sans';color:#1c2b4a}.vr span{font:500 16px 'Open Sans';color:#5c6170}
.vr em{font-style:normal;font:700 14px 'Open Sans';border-radius:8px;padding:2px 8px}.vr .ok{background:#dcefe2;color:#1f6a3d}.vr .no{background:#ffe1cc;color:#b4531b}
""", "<h1>Reached the house, but<br><span>the spare part isn't in the bag?</span></h1><div class=sub>Today's visits and the parts they need, checked before you leave.</div>",
f'''<div class=tb><div class=lid><i></i>TECH 1'S TOOLBOX · SAMPLE<i></i></div><div class=bx>{"".join(f'<div class="cp {k}"><span>{a}</span><div>{"<em>LOW · 2 NEEDED TODAY</em>" if k else ""}<b>{q}</b></div></div>' for a,q,k in box)}</div>
<div class=al2>Visits need <b>2 hose pipes</b>, the box has 1. Pick one up from the shop first.</div></div>
{phone(f"""<div class=pv><small class=t>TODAY · 5 VISITS · SAMPLE</small><div class=h>Tech 1's visits</div>{"".join(f'<div class=vr><div class=tm><span>{t}</span><em class={k}>{"In box" if k=="ok" else "Not in box"}</em></div><b>{a}</b><span>{p} · {s}</span></div>' for t,a,p,s,k in vis163)}</div>""", w=370, h=760)}''',
"#1c2b4a", "Run a stove repair service? DM us", "background:#2b63d9;color:#fff")


# ───────── 164 USA · Carpet cleaning · SINGLE · Cardo + DM Sans · soft mint / charcoal / tangerine
# New technique: top-down SVG floor plan where tapped rooms fill with a carpet stripe pattern; quote card built from the rooms (no prices).
rooms = [("Living room", 20, 20, 300, 230, 1), ("Kitchen", 330, 20, 210, 150, 0), ("Hallway", 330, 180, 210, 70, 1),
         ("Bedroom 1", 20, 260, 250, 230, 1), ("Bath", 280, 260, 110, 110, 0), ("Bedroom 2", 280, 380, 260, 110, 1), ("Closet", 400, 260, 140, 110, 0)]
def fplan():
    s = '<svg viewBox="0 0 560 730" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block"><defs><pattern id="cpA" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="16" height="16" fill="#f7a35c"/><rect width="7" height="16" fill="#f4914a"/></pattern></defs>'
    for n, x, y, w, h, on in rooms:
        y, h = y*1.32, h*1.32
        s += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{"url(#cpA)" if on else "#f3f5f4"}" stroke="#2f3437" stroke-width="6"/>'
        fs = 26 if w > 200 else 22
        s += f'<text x="{x+w/2}" y="{y+h/2+8}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="{fs}" fill="{"#2f3437"}"><tspan>{n}</tspan></text>'
        if on:
            s += f'<circle cx="{x+w-24}" cy="{y+24}" r="15" fill="#2f3437"/><path d="M{x+w-31} {y+24} l5 5 l9 -10" fill="none" stroke="#fff" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>'
    s += '<g>' + "".join(f'<rect x="{20+i*22}" y="676" width="22" height="30" fill="{"url(#cpA)"}" stroke="#2f3437" stroke-width="3"/>' for i in range(13)) + '</g>'
    s += '<text x="320" y="698" font-family="DM Sans" font-weight="700" font-size="22" fill="#2f3437"><tspan>Stairs · 13 steps</tspan></text></svg>'
    return s
P["p164_carpet"] = page("""
body{--f:'DM Sans';--h:'Cardo';background:#dcefe6;color:#2f3437}
h1{font-family:'Cardo';font-size:64px;font-weight:700;letter-spacing:-.5px;line-height:1.2} h1 span{color:#d9651c}
.sub{color:#4f5a57;font-size:23px}
.vis{gap:20px}
.fp{flex:1;background:#fff;border-radius:28px;padding:18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(47,52,55,.10)}
.fp small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#7d8a86}.fp .pl{flex:1;min-height:0;display:flex}.fp .pl svg{flex:1}
.qc{width:360px;flex:none;background:#2f3437;color:#fff;border-radius:28px;padding:22px;display:flex;flex-direction:column;gap:10px}
.qc small{font:700 13px 'DM Sans';letter-spacing:2.5px;color:#a9c9bb}.qc h3{font:700 32px/1.2 Cardo}
.qc .r{flex:1;background:rgba(255,255,255,.07);border-radius:14px;padding:0 14px;display:flex;flex-direction:column;justify-content:center}
.qc .r span{font:600 15px 'DM Sans';color:#a9c9bb;letter-spacing:1px}.qc .r b{font:700 23px/1.3 'DM Sans'}
.qc .bt{background:#f7a35c;color:#2f3437;border-radius:14px;padding:15px;text-align:center;font:700 20px 'DM Sans'}
""", "<h1>Every caller asks, “How much?”<br><span>Let them tap their rooms.</span></h1><div class=sub>A floor plan on your website builds the job before you call back.</div>",
f'''<div class=fp><small>TAP THE ROOMS TO CLEAN · SAMPLE HOME</small><div class=pl>{fplan()}</div></div>
<div class=qc><small>YOUR JOB · SAMPLE</small><h3>3 rooms, hallway and stairs</h3>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a,b in [("ROOMS","Living room, Bedroom 1 and 2"),("ADD-ONS","Pet stain spot, deodorize"),("TIME ON SITE","About 2 h 30 min"),("PICK A TIME","Tue, Dec 8 · 9–11 AM")])}<div class=bt>Send my quote request</div></div>''',
"#2f3437", "Clean carpets? DM us", "background:#2f3437;color:#fff")


# ───────── 165 INDIA · T-shirt & merch printing · SINGLE · TeX Gyre Adventor + Inter · raspberry / off-white / ink
# New technique: SVG tee with a dashed print-area box + colour × size quantity matrix with row/column totals, and a proof version strip (v1 changes, v2 approved).
cols = [("White", "#ffffff"), ("Black", "#22222a"), ("Navy", "#22346b")]
sizes = ["S", "M", "L", "XL", "XXL"]
qty = {"White": [10, 25, 30, 15, 5], "Black": [5, 20, 25, 10, 5], "Navy": [0, 10, 15, 10, 5]}
def tee(c="#ffffff"):
    return (f'<svg viewBox="0 0 300 300" width="270" style="display:block"><path d="M95 30 L60 40 L10 90 L45 130 L70 110 L70 280 L230 280 L230 110 L255 130 L290 90 L240 40 L205 30 Q150 70 95 30 Z" fill="{c}" stroke="#2a1830" stroke-width="5" stroke-linejoin="round"/>'
            '<rect x="105" y="105" width="90" height="100" rx="6" fill="none" stroke="#c2185b" stroke-width="4" stroke-dasharray="10 7"/>'
            '<text x="150" y="160" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="22" fill="#c2185b"><tspan>YOUR</tspan></text><text x="150" y="186" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="22" fill="#c2185b"><tspan>LOGO</tspan></text></svg>')
tot = sum(sum(v) for v in qty.values())
P["p165_tees"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#fbf5f0;color:#2a1830}
h1{font-family:'TeX Gyre Adventor';font-size:60px;font-weight:700;letter-spacing:-1px;line-height:1.22} h1 span{color:#c2185b}
.sub{color:#6b5a66;font-size:23px}
.vis{flex-direction:column;gap:18px}
.top{flex:1;display:flex;gap:18px;min-height:0}
.tc{width:330px;flex:none;background:#c2185b;border-radius:28px;padding:20px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;color:#fff}
.tc small{font:700 14px Inter;letter-spacing:2.5px;color:#ffd1e1;align-self:flex-start}
.tc .pa{align-self:stretch;background:rgba(255,255,255,.14);border-radius:16px;padding:10px 14px;font:600 18px/1.4 Inter}
.mx{flex:1;background:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(42,24,48,.08)}
.mx small{font:700 14px Inter;letter-spacing:2.5px;color:#9a8794}
.gr{flex:1;display:grid;grid-template-columns:120px repeat(5,1fr) 76px;grid-template-rows:auto repeat(3,1fr) auto;gap:6px}
.gr span{display:flex;align-items:center;justify-content:center;font:600 22px Inter;border-radius:12px}
.gr .hd{font:700 17px Inter;color:#9a8794}.gr .q{background:#fbeef3}.gr .z{background:#f4f1f2;color:#b9aab4}
.gr .cl{justify-content:flex-start;gap:8px;font:700 19px Inter}.gr .cl i{width:22px;height:22px;border-radius:50%;border:2px solid #2a1830;flex:none}
.gr .tt{font:700 22px 'TeX Gyre Adventor';color:#c2185b}.gr .gt{background:#2a1830;color:#fff;font:700 24px 'TeX Gyre Adventor';padding:10px 0}.gr .tt{padding:10px 0}
.pf{display:flex;gap:14px}
.pv{flex:1;border-radius:20px;padding:16px 18px;display:flex;align-items:center;gap:14px}
.pv b{display:block;font:700 22px 'TeX Gyre Adventor'}.pv span{font:500 17px/1.35 Inter}
.pv.v1{background:#fff;border:2px dashed #d8c7d1}.pv.v2{background:#2a1830;color:#fff}.pv .ib{width:50px;height:50px;border-radius:14px}
.pv.v1 .ib{background:#f4f1f2;color:#9a8794}.pv.v2 .ib{background:#c2185b;color:#fff}
""", "<h1>Bulk T-shirt order,<br><span>sizes lost in 40 messages?</span></h1><div class=sub>One order sheet for colours and sizes, one proof link to approve.</div>",
f'''<div class=top><div class=tc><small>ORDER #T-118 · SAMPLE</small>{tee()}<div class=pa>Front print · 10 × 12 in<br>Screen print · 2 colours</div></div>
<div class=mx><small>QUANTITY BY COLOUR AND SIZE</small><div class=gr><span class=hd></span>{"".join(f'<span class=hd>{s}</span>' for s in sizes)}<span class=hd>Total</span>
{"".join(f'<span class=cl><i style="background:{c}"></i>{n}</span>' + "".join(f'<span class="{"q" if v else "z"}">{v if v else "—"}</span>' for v in qty[n]) + f'<span class=tt>{sum(qty[n])}</span>' for n,c in cols)}
<span class=hd>Total</span>{"".join(f'<span class=tt>{sum(qty[n][i] for n,_ in cols)}</span>' for i in range(5))}<span class=gt>{tot}</span></div></div></div>
<div class=pf><div class="pv v1"><span class=ib>{ic("doc",26)}</span><div><b>Proof v1</b><span>Client asked: logo a bit bigger</span></div></div>
<div class="pv v2"><span class=ib>{ic("check",26,w=3)}</span><div><b>Proof v2 · Approved</b><span>Mon, 23 Nov · printing starts</span></div></div></div>''',
"#2a1830", "Print T-shirts in bulk? DM us", "background:#c2185b;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
