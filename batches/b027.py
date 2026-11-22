import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 151 INDIA · NGO / trust (volunteers + donors) · CAROUSEL 5 · Bitter + Inter · sage / sunflower / cream
# New technique: volunteer shift board with slot circles per shift (filled / open) as a sign-up sheet.
NG = """
body{--f:'Inter';--h:'Bitter';background:#f7f3e6;color:#21352b}
h1{font-family:'Bitter';font-size:58px;font-weight:700;letter-spacing:0;line-height:1.22;margin-top:22px} h1 span{color:#3f7a5a}
.sub{color:#5a6b61;font-size:23px}
.kk{font:700 16px Inter;letter-spacing:3px;color:#b8860b;margin-top:22px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(33,53,43,.07)}
"""
def ng(n, head, vis, css="", cta="Swipe", ctacss="background:#3f7a5a;color:#fff"):
    return page(NG + css, head, vis, "#21352b", cta, ctacss, tagline=f"{n} / 5")
drives = [("Tree planting", "Sat, 5 Dec", [("7 AM – 10 AM", 8, 8), ("10 AM – 1 PM", 8, 6)]),
          ("Food packing", "Sun, 6 Dec", [("9 AM – 12 PM", 6, 6), ("2 PM – 5 PM", 6, 6)]),
          ("Clothes sorting", "Sat, 12 Dec", [("10 AM – 1 PM", 7, 5), ("2 PM – 5 PM", 7, 4)])]
def slots(c, f): return "".join(f'<i class="{"on" if k < f else ""}"></i>' for k in range(c))
P["p151_ngo_s1"] = ng(1, "<div class=kk>NGOS · TRUSTS · VOLUNTEER GROUPS</div><h1>Volunteers in 5 chat groups?<br><span>One sign-up board for every drive.</span></h1>",
f'''<div class="cd bd">{"".join(f'<div class=dr><div class=dh><b>{a}</b><span>{d}</span></div>' + "".join(f'<div class=sh><span class=tm>{t}</span><div class=sl>{slots(c,f)}</div><em class="{"fu" if c==f else ""}">{"Full" if c==f else f"{c-f} open"}</em></div>' for t,c,f in S) + '</div>' for a,d,S in drives)}</div>
<div class=st>{"".join(f'<div class="{k}"><b>{a}</b><span>{b}</span></div>' for a,b,k in [("3","drives",""),("42","volunteer slots",""),("35","filled",""),("7","open","op")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.bd{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.dr{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-bottom:1.5px solid #eee8d6}.dr:last-child{border-bottom:none}
.dh{display:flex;align-items:baseline;gap:14px}.dh b{font:700 32px/1.3 Bitter}.dh span{font:600 20px Inter;color:#b8860b}
.sh{display:flex;align-items:center;gap:16px}.tm{width:200px;font:600 21px Inter;color:#5a6b61}
.sl{flex:1;display:flex;gap:8px}.sl i{width:38px;height:38px;border-radius:50%;border:2.5px solid #9fbfac}.sl i.on{background:#3f7a5a;border-color:#3f7a5a}
.sh em{font-style:normal;width:110px;text-align:center;font:700 19px Inter;padding:7px 0;border-radius:12px;background:#ffe9a6;color:#6b4e00}.sh em.fu{background:#21352b;color:#fff}
.st{display:flex;gap:12px}.st div{flex:1;background:#3f7a5a;color:#fff;border-radius:20px;padding:12px 18px}.st b{display:block;font:700 38px/1.3 Bitter}.st span{font:600 17px Inter;color:#d6e8dd}
.st .op{background:#f2c230;color:#21352b}.st .op span{color:#21352b}""")

P["p151_ngo_s2"] = ng(2, "<div class=kk>PART 1 · VOLUNTEER SIGN-UP</div><h1>Pick a drive, pick a shift.<br><span>A reminder comes the day before.</span></h1>",
browser(f'''<div class=fm><div class=lf2><small>CHOOSE A DRIVE</small>{"".join(f'<div class="op2{" on" if i==2 else ""}"><b>{a}</b><span>{d}</span><em>{(lambda o: f"{o} open" if o else "Full")(sum(c-f for _,c,f in S))}</em></div>' for i,(a,d,S) in enumerate(drives))}
<small>CHOOSE A SHIFT · CLOTHES SORTING</small><div class=sf><div class="op2 on"><b>10 AM – 1 PM</b><em>2 open</em></div><div class=op2><b>2 PM – 5 PM</b><em>3 open</em></div></div></div>
<div class=rt2><small>YOUR DETAILS</small><div class=in2><span>Name</span><b>Sample Volunteer</b></div><div class=in2><span>Phone</span><b>98XXX XXXXX</b></div><div class=in2><span>Can bring</span><b>A friend (+1)</b></div>
<div class=rm2>{ic("bell",22)}<span>Reminder on Fri, 11 Dec with the address and what to bring.</span></div><div class=bt>Sign me up</div></div></div>''', url="yourngo.org/volunteer · sample", style="flex:1"),
css=""".vis{display:flex}.fm{flex:1;display:flex;gap:18px;padding:20px}
.lf2{flex:1;display:flex;flex-direction:column;gap:10px}.fm small{font:700 14px Inter;letter-spacing:2px;color:#8a978f;margin-top:6px}
.op2{flex:1;border:2px solid #e4dfcf;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;position:relative}
.op2 b{font:700 28px/1.3 Bitter}.op2 span{font:500 20px Inter;color:#5a6b61}.op2 em{position:absolute;right:14px;top:14px;font-style:normal;font:700 15px Inter;background:#ffe9a6;color:#6b4e00;border-radius:10px;padding:5px 9px}
.op2.on{border-color:#3f7a5a;background:#eef6f0}
.sf{display:flex;gap:10px;flex:1}.sf .op2{flex:1}.sf .op2 em{position:static;align-self:flex-start;margin-top:6px}
.rt2{width:360px;flex:none;display:flex;flex-direction:column;gap:10px;background:#f7f3e6;border-radius:20px;padding:16px}
.in2{background:#fff;border-radius:14px;padding:12px 14px}.in2 span{display:block;font:600 14px Inter;color:#8a978f}.in2 b{font:600 22px Inter}
.rm2{flex:1;display:flex;gap:10px;align-items:center;font:600 21px/1.4 Inter;color:#3f7a5a}
.bt{background:#3f7a5a;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 20px Inter}""")

donors = [("Sample Donor 1", "Monthly", "Nov", "Receipt sent"), ("Sample Donor 2", "One-time", "Oct", "Receipt sent"), ("Sample Donor 3", "Monthly", "Nov", "Receipt sent"),
          ("Sample Donor 4", "Monthly", "Oct", "Reminder sent"), ("Sample Donor 5", "In kind · clothes", "Nov", "Thank-you sent"), ("Sample Donor 6", "Monthly", "Oct", "Reminder sent")]
P["p151_ngo_s3"] = ng(3, "<div class=kk>PART 2 · DONOR RECORDS</div><h1>Every donor, every receipt,<br><span>in one list.</span></h1>",
f'''<div class="cd dt2"><div class="tr th"><span>DONOR · SAMPLE</span><span>TYPE</span><span>LAST</span><span>STATUS</span></div>
{"".join(f'<div class=tr><span><i class=av>{a[-1]}</i>{a}</span><span>{b}</span><span>{c}</span><span><em class="{"rm" if "Reminder" in d else ""}">{d}</em></span></div>' for a,b,c,d in donors)}</div>
<div class=bm>{"".join(f'<div class=bx><span class=ib>{ic(i,26)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Receipts in one tap","Made and sent from the record."),("bell","Monthly reminders","Donor 4 and 6 got a soft nudge."),("heart","Thank-you notes","Sent after every gift, even in kind.")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.dt2{flex:1;padding:8px 22px;display:flex;flex-direction:column}
.tr{flex:1;display:grid;grid-template-columns:1.5fr 1.1fr .5fr 1fr;align-items:center;border-bottom:1.5px solid #eee8d6;font:600 22px Inter}.tr:last-child{border-bottom:none}
.th{flex:none;height:48px;font:700 14px Inter;letter-spacing:2px;color:#8a978f}
.tr span:first-child{display:flex;align-items:center;gap:12px}.av{width:42px;height:42px;border-radius:50%;background:#dcebe2;color:#3f7a5a;font:700 18px/42px Bitter;font-style:normal;text-align:center;flex:none}
.tr em{font-style:normal;font:700 16px Inter;padding:7px 12px;border-radius:10px;background:#dcebe2;color:#2c5c42;white-space:nowrap}.tr em.rm{background:#ffe9a6;color:#6b4e00}
.bm{display:flex;gap:12px}.bx{flex:1;background:#21352b;color:#fff;border-radius:20px;padding:16px;display:flex;flex-direction:column;gap:10px}
.bx .ib{width:50px;height:50px;border-radius:14px;background:#f2c230;color:#21352b}.bx b{display:block;font:700 22px/1.3 Bitter}.bx span{font:500 17px/1.4 Inter;color:#cfdcd4}""")

tree = '<svg viewBox="0 0 100 100" width="100%" height="100%" preserveAspectRatio="xMidYMid meet"><rect width="100" height="100" fill="#dcebe2"/><rect x="0" y="78" width="100" height="22" fill="#a7c58f"/><rect x="46" y="48" width="8" height="34" fill="#7a5a3a"/><circle cx="50" cy="40" r="22" fill="#3f7a5a"/><circle cx="36" cy="48" r="12" fill="#4f8f69"/><circle cx="64" cy="48" r="12" fill="#4f8f69"/></svg>'
box = '<svg viewBox="0 0 100 100" width="100%" height="100%"><rect width="100" height="100" fill="#fbecc0"/><path d="M20 45 L50 32 L80 45 L80 78 L50 90 L20 78 Z" fill="#d9a55b"/><path d="M20 45 L50 58 L80 45 L50 32 Z" fill="#e8bd78"/><path d="M50 58 V90" stroke="#b9853f" stroke-width="2"/></svg>'
shirt = '<svg viewBox="0 0 100 100" width="100%" height="100%"><rect width="100" height="100" fill="#e6e1f2"/><path d="M30 26 L42 20 Q50 28 58 20 L70 26 L82 40 L72 48 L68 42 V82 H32 V42 L28 48 L18 40 Z" fill="#7d6bb3"/></svg>'
P["p151_ngo_s4"] = ng(4, "<div class=kk>PART 3 · DRIVE DAY REPORT</div><h1>Attendance and photos<br><span>shared with donors the same day.</span></h1>",
f'''<div class="cd rp"><div class=rh><div><small>REPORT · SAMPLE</small><b>Tree planting · Sat, 5 Dec</b></div><em>Shared</em></div>
<div class=ph>{"".join(f'<div class=pi>{x}</div>' for x in [tree,tree,tree,tree,box,tree])}</div>
<div class=nb>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("13 of 14","volunteers came, 7 AM shift"),("24","photos uploaded"),("1 tap","report sent to donors")])}</div></div>''',
css=""".vis{display:flex}.rp{flex:1;padding:22px;display:flex;flex-direction:column;gap:16px}
.rh{display:flex;justify-content:space-between;align-items:center}.rh small{font:700 14px Inter;letter-spacing:2px;color:#8a978f}.rh b{display:block;font:700 32px/1.3 Bitter}
.rh em{font-style:normal;font:700 17px Inter;background:#3f7a5a;color:#fff;border-radius:12px;padding:9px 16px}
.ph{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px;min-height:0}.pi{border-radius:18px;overflow:hidden}.pi svg{display:block}
.nb{display:flex;gap:12px}.nb div{flex:1;background:#f7f3e6;border-radius:18px;padding:14px 18px}.nb b{display:block;font:700 32px/1.3 Bitter;color:#3f7a5a}.nb span{font:600 17px/1.4 Inter;color:#5a6b61}""")
# note: the 7 AM shift had 8 slots filled; 13 of 14 counts both tree planting shifts (8 + 6 = 14)
P["p151_ngo_s4"] = P["p151_ngo_s4"].replace("volunteers came, 7 AM shift", "volunteers came, both shifts")

P["p151_ngo_s5"] = ng(5, "<div class=kk>YOUR TURN</div><h1>Run an NGO or a trust?<br><span>Let's build your volunteer<br>and donor app.</span></h1>",
f'''<div class=gd>{"".join(f'<div class=tl3><span class=nm>{n}</span><b>{a}</b><span class=ds>{b}</span></div>' for n,a,b in [("01","Shift board","Slots, open and full, per drive"),("02","Sign-up page","Pick a drive and shift in a minute"),("03","Donor records","Receipts, reminders, thank-you notes"),("04","Drive reports","Attendance and photos, same day")])}</div>
<div class=q>Tell us how your team works today. We'll plan an app that fits it.</div>''',
css=""".vis{flex-direction:column;gap:18px}.gd{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.tl3{background:#fff;border-radius:24px;padding:24px;display:flex;flex-direction:column;justify-content:flex-end;gap:8px;position:relative;overflow:hidden;box-shadow:0 14px 30px rgba(33,53,43,.07)}
.tl3 .nm{position:absolute;right:18px;top:8px;font:700 110px/1.2 Bitter;color:#f2ead0}
.tl3 b{font:700 36px/1.3 Bitter;position:relative}.tl3 .ds{font:500 22px/1.4 Inter;color:#5a6b61;position:relative}
.q{background:#3f7a5a;color:#fff;border-radius:22px;padding:22px 26px;font:500 24px/1.45 Inter;text-align:center}""",
cta="DM us to start", ctacss="background:#f2c230;color:#21352b")


# ───────── 152 INDIA · Used bike dealer · SINGLE · Archivo Black + Open Sans · asphalt / fluoro orange / white
# New technique: SVG motorcycle side profile + 12-point inspection grid on one listing card.
bike = '''<svg viewBox="0 0 520 300" width="500" style="display:block">
<circle cx="120" cy="210" r="70" fill="none" stroke="#1e2226" stroke-width="16"/><circle cx="120" cy="210" r="22" fill="#9aa3ab"/>
<circle cx="410" cy="210" r="70" fill="none" stroke="#1e2226" stroke-width="16"/><circle cx="410" cy="210" r="22" fill="#9aa3ab"/>
<path d="M120 210 L200 150 L300 150 L330 210 Z" fill="none" stroke="#5b636b" stroke-width="10" stroke-linejoin="round"/>
<path d="M190 150 Q200 105 260 100 L330 100 Q350 102 352 128 L300 150 Z" fill="#ff6a1a"/>
<path d="M120 140 L220 138 L230 120 L140 118 Z" fill="#1e2226"/>
<rect x="215" y="160" width="90" height="56" rx="10" fill="#3a4148"/><rect x="230" y="172" width="60" height="10" rx="4" fill="#9aa3ab"/>
<path d="M410 210 L360 90" stroke="#5b636b" stroke-width="10" stroke-linecap="round"/><path d="M345 70 L390 70" stroke="#1e2226" stroke-width="10" stroke-linecap="round"/>
<circle cx="392" cy="112" r="16" fill="#ffd9b8" stroke="#1e2226" stroke-width="4"/>
<path d="M300 205 L80 230" stroke="#9aa3ab" stroke-width="8" stroke-linecap="round"/></svg>'''
chk = [("Engine start", 1), ("Brakes", 1), ("Clutch", 1), ("Chain set", 1), ("Front tyre", 1), ("Rear tyre · 40% left", 2), ("Lights + horn", 1), ("Battery", 1), ("Suspension", 1), ("Body + paint", 2), ("Papers (RC)", 1), ("Service history", 1)]
P["p152_bike"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#24282c;color:#f4f4f2}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;letter-spacing:0;line-height:1.27} h1 span{color:#ff6a1a}
.sub{color:#b9bfc4}
.vis{flex-direction:column;gap:16px}
.ls{background:#fff;color:#1e2226;border-radius:28px;padding:20px 24px;display:flex;gap:18px;align-items:center}
.ls .im{width:520px;flex:none;background:#f1f1ee;border-radius:20px;padding:10px;display:flex;justify-content:center}
.ls .if{flex:1;display:flex;flex-direction:column;gap:10px}.ls small{font:700 13px 'Open Sans';letter-spacing:2px;color:#8b9298}
.ls b{font:400 28px/1.3 'Archivo Black'}.ch2{display:flex;flex-wrap:wrap;gap:8px}.ch2 span{font:700 16px 'Open Sans';background:#f1f1ee;border-radius:10px;padding:7px 11px}
.ls .bt{background:#ff6a1a;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 18px 'Open Sans'}
.ck{flex:1;background:#30353a;border-radius:28px;padding:20px 24px;display:flex;flex-direction:column;gap:12px}
.ck .hh{display:flex;justify-content:space-between;align-items:center}.ck .hh b{font:400 26px/1.3 'Archivo Black'}.ck .hh span{font:600 17px 'Open Sans';color:#b9bfc4}
.gr{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(4,1fr);gap:10px}
.it{background:#3a4046;border-radius:14px;display:flex;align-items:center;gap:12px;padding:0 14px;font:600 19px/1.3 'Open Sans'}
.it i{width:34px;height:34px;border-radius:50%;background:#3fbf6e;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.it.am i{background:#ffb020;color:#24282c}.it.am{background:#4a3f2c}
""", "<h1>“Is it in good condition?”<br><span>Show a 12-point check<br>on every listing.</span></h1>",
f'''<div class=ls><div class=im>{bike}</div><div class=if><small>LISTING · SAMPLE</small><b>150cc bike · 2021</b><div class=ch2><span>18,400 km</span><span>1st owner</span><span>Petrol</span></div><div class=bt>Book a test ride</div></div></div>
<div class=ck><div class=hh><b>12-point check</b><span>Done by your mechanic · sample</span></div><div class=gr>{"".join(f'<div class="it{" am" if v==2 else ""}"><i>{ic("check" if v==1 else "x",18,w=3) if v==1 else "!"}</i>{t}</div>' for t,v in chk)}</div></div>''',
"#f4f4f2", "Sell used bikes? DM us", "background:#ff6a1a;color:#fff", logo_color="#f4f4f2")
P["p152_bike"] = P["p152_bike"].replace("<i>!</i>", "<i style='font:800 18px Open Sans'>!</i>")


# ───────── 153 INDIA · Car accessories shop (fitting bookings) · SINGLE · Poppins + Roboto · jet black / electric blue / silver
# New technique: top-down SVG car with numbered hotspots + one combined bay slot bar.
car = '''<svg viewBox="0 0 300 600" style="display:block;height:100%;width:auto">
<rect x="40" y="20" width="220" height="560" rx="100" fill="#cfd5dc" stroke="#11151a" stroke-width="5"/>
<path d="M70 170 Q150 120 230 170 L220 220 Q150 195 80 220 Z" fill="#5b6b7c"/><path d="M80 430 Q150 450 220 430 L230 480 Q150 510 70 480 Z" fill="#5b6b7c"/>
<rect x="80" y="230" width="140" height="190" rx="18" fill="#e9edf1"/>
<rect x="95" y="250" width="50" height="60" rx="10" fill="#2f6bff"/><rect x="155" y="250" width="50" height="60" rx="10" fill="#2f6bff"/>
<rect x="95" y="340" width="110" height="60" rx="10" fill="#2f6bff"/>
<rect x="26" y="150" width="20" height="40" rx="6" fill="#11151a"/><rect x="254" y="150" width="20" height="40" rx="6" fill="#11151a"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="24" fill="#11151a" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+9}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="24" fill="#fff"><tspan>{n}</tspan></text>' for n, x, y in [(1, 150, 285), (2, 150, 370), (3, 150, 160), (4, 150, 548)]) + '</svg>'
fits = [("1", "Seat covers", "Sample fabric · black", "90 min"), ("2", "3D floor mats", "Full set", "20 min"), ("3", "Dashcam", "Front · hidden wiring", "45 min"), ("4", "Parking sensors", "4 sensors · rear", "60 min")]
P["p153_caracc"] = page("""
body{--f:'Roboto';--h:'Poppins';background:#0f1318;color:#eef2f6}
h1{font-family:'Poppins';font-size:60px;font-weight:800;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#4f8bff}
.sub{color:#a9b4c0}
.vis{flex-direction:column;gap:16px}
.tp{flex:1;display:flex;gap:18px;min-height:0}
.cr{width:330px;flex:none;background:#1a2028;border-radius:28px;display:flex;align-items:center;justify-content:center;padding:22px;min-height:0}
.ls{flex:1;display:flex;flex-direction:column;gap:12px}
.fx{flex:1;background:#fff;color:#11151a;border-radius:22px;padding:0 18px;display:flex;align-items:center;gap:16px}
.fx i{width:50px;height:50px;border-radius:50%;background:#11151a;color:#fff;font:700 22px/50px Poppins;font-style:normal;text-align:center;flex:none}
.fx div{flex:1}.fx b{display:block;font:700 23px/1.3 Poppins}.fx span{font:500 17px Roboto;color:#5d6875}
.fx em{font-style:normal;font:700 18px Roboto;background:#e6eeff;color:#1f55d6;border-radius:12px;padding:8px 12px}
.by{background:#1a2028;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.by .hh{display:flex;justify-content:space-between;font:600 18px Roboto;color:#a9b4c0}.by .hh b{color:#fff;font:700 20px Poppins}
.bar{display:flex;height:64px;border-radius:14px;overflow:hidden;gap:3px}
.bar div{display:flex;align-items:center;justify-content:center;font:700 17px Roboto;color:#fff}
.tk{display:flex;justify-content:space-between;font:600 15px Roboto;color:#7d8996}
""", "<h1>Customer wants 4 fittings?<br><span>Book one bay slot for all.</span></h1><div class=sub>They pick the accessories, the app adds up the fitting time.</div>",
f'''<div class=tp><div class=cr>{car}</div><div class=ls>{"".join(f'<div class=fx><i>{n}</i><div><b>{a}</b><span>{b}</span></div><em>{t}</em></div>' for n,a,b,t in fits)}</div></div>
<div class=by><div class=hh><span>BAY 2 · SAT, 28 NOV · SAMPLE</span><b>10:00 AM – 1:35 PM · 3 h 35 min</b></div>
<div class=bar><div style="flex:90;background:#2f6bff">1 · 90 min</div><div style="flex:20;background:#5b8cff">2</div><div style="flex:45;background:#2f6bff">3 · 45</div><div style="flex:60;background:#5b8cff">4 · 60 min</div></div>
<div class=tk><span>Start 10:00 AM</span><span>Car ready 1:35 PM · customer gets a message</span></div></div>''',
"#eef2f6", "Car accessories shop? DM us", "background:#2f6bff;color:#fff", logo_color="#eef2f6")


# ───────── 154 INDIA · Small team manager (tasks + attendance) · SINGLE · Lora + DM Sans · whiteboard white / sticky yellow / marker blue
# New technique: glass whiteboard with tilted sticky notes (two fallen to the floor strip) beside the same tasks in an app.
notes = [("Call supplier re: late order", "#ffe066", -3, ""), ("Update price list", "#ffd0e0", 2, ""), ("Send 3 quotes", "#c9f0d8", -2, ""), ("Fix shop banner", "#ffe066", 3, ""),
         ("Pay electricity bill", "#cfe3ff", -4, "fl"), ("Stock count, rack B", "#ffd0e0", 5, "fl")]
tasks = [("Call supplier re: late order", "A", "11 AM", "Done", "dn"), ("Send 3 quotes", "B", "1 PM", "Doing", "dg"), ("Update price list", "C", "3 PM", "To do", ""),
         ("Fix shop banner", "D", "4 PM", "To do", ""), ("Pay electricity bill", "A", "5 PM", "To do", ""), ("Stock count, rack B", "E", "6 PM", "To do", "")]
P["p154_team"] = page("""
body{--f:'DM Sans';--h:'Lora';background:#eef2f7;color:#1b2a4a}
h1{font-family:'Lora';font-size:60px;font-weight:700;letter-spacing:-.3px;line-height:1.22} h1 span{color:#2457c5}
.sub{color:#56637d}
.vis{gap:22px;align-items:center}
.wb{flex:1;align-self:stretch;background:#fff;border:10px solid #c9d1dc;border-radius:20px;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 20px 40px rgba(27,42,74,.10)}
.wb .tt{font:700 30px 'Lora';color:#2457c5;padding:18px 22px 0;font-style:italic}
.ns{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:26px;padding:22px 30px}
.nt{padding:16px;font:600 26px/1.35 'DM Sans';color:#2b2b2b;box-shadow:0 8px 14px rgba(0,0,0,.12);display:flex;align-items:center;text-align:center;justify-content:center}
.fl2{height:110px;background:repeating-linear-gradient(90deg,#d9dfe7 0 40px,#cfd6df 40px 80px);display:flex;gap:16px;align-items:center;padding:0 20px;position:relative}
.fl2 .nt{height:76px;width:200px;font-size:17px;padding:8px}
.fl2 em{position:absolute;right:16px;top:12px;font-style:normal;font:700 15px 'DM Sans';background:#e5484d;color:#fff;border-radius:10px;padding:6px 10px}
.ap{flex:1;padding:8px 16px 16px;display:flex;flex-direction:column;gap:9px;background:#f6f8fb}
.ap small{font:700 12px 'DM Sans';letter-spacing:2px;color:#8792a8}.ap .t{font:700 24px 'Lora'}
.at{display:flex;gap:6px;align-items:center;background:#fff;border-radius:14px;padding:10px 12px;font:600 14px 'DM Sans'}.at i{width:26px;height:26px;border-radius:50%;background:#2457c5;color:#fff;font:700 12px/26px 'DM Sans';font-style:normal;text-align:center}.at i.no{background:#d6dbe4;color:#56637d}.at span{margin-left:auto;color:#2457c5}
.tk{flex:1;background:#fff;border-radius:14px;padding:0 12px;display:flex;align-items:center;gap:10px}
.tk .av{width:32px;height:32px;border-radius:50%;background:#e3ebfb;color:#2457c5;font:700 14px/32px 'DM Sans';text-align:center;flex:none}
.tk div{flex:1}.tk b{display:block;font:600 15px/1.3 'DM Sans'}.tk span{font:500 13px 'DM Sans';color:#8792a8}
.tk em{font-style:normal;font:700 12px 'DM Sans';padding:5px 8px;border-radius:8px;background:#eef1f6;color:#56637d}.tk em.dn{background:#d9f5e3;color:#1c7a43}.tk em.dg{background:#fff1c2;color:#7a5a00}
""", "<h1>Sticky notes fall off.<br><span>Put your team's day<br>in one app.</span></h1>",
f'''<div class=wb><div class=tt>Today's work</div><div class=ns>{"".join(f'<div class=nt style="background:{c};transform:rotate({r}deg)">{t}</div>' for t,c,r,k in notes if not k)}</div>
<div class=fl2>{"".join(f'<div class=nt style="background:{c};transform:rotate({r}deg)">{t}</div>' for t,c,r,k in notes if k)}<em>Fell off</em></div></div>
{phone(f'<div class=ap><small>TEAM OF 6 · SAMPLE</small><b class=t>Today</b><div class=at>' + "".join(f'<i class="{"no" if x=="F" else ""}">{x}</i>' for x in "ABCDEF") + '<span>5 of 6 in</span></div>' + "".join(f'<div class=tk><span class=av>{o}</span><div><b>{a}</b><span>Due {d}</span></div><em class={k}>{s}</em></div>' for a,o,d,s,k in tasks) + '</div>', w=380, h=770)}''',
"#1b2a4a", "Want a team app? DM us", "background:#2457c5;color:#fff")


# ───────── 155 USA · Pet boarding (stays) · SINGLE · Cardo + Inter · lavender / teal / cream
# New technique: Gantt-style suite x day grid with stay bars + a daily "report card" for one guest.
days = ["Mon 23", "Tue 24", "Wed 25", "Thu 26", "Fri 27", "Sat 28", "Sun 29"]
stays = [(1, "Max", 1, 4, "#1f8a8a"), (1, "Luna", 5, 7, "#7a5cc7"), (2, "Bella", 2, 6, "#e08a3c"), (3, "Rocky", 1, 2, "#7a5cc7"), (3, "Daisy", 4, 7, "#1f8a8a"),
         (4, "Cooper", 3, 7, "#e08a3c"), (5, "Milo", 1, 3, "#1f8a8a"), (6, "Coco", 2, 3, "#7a5cc7"), (6, "Bear", 5, 6, "#e08a3c")]
P["p155_petboard"] = page("""
body{--f:'Inter';--h:'Cardo';background:#f3effa;color:#2a2440}
h1{font-family:'Cardo';font-size:64px;font-weight:700;letter-spacing:-.4px;line-height:1.2} h1 span{color:#1f8a8a}
.sub{color:#5f587a}
.vis{flex-direction:column;gap:16px}
.gt{flex:1;background:#fff;border-radius:26px;padding:18px 20px;display:grid;grid-template-columns:110px repeat(7,1fr);grid-template-rows:40px repeat(6,1fr);gap:8px 6px;box-shadow:0 16px 34px rgba(42,36,64,.08)}
.gt .dh{font:700 15px Inter;color:#8a84a3;text-align:center;align-self:center}
.gt .sr{font:700 18px Inter;align-self:center;color:#2a2440}
.gt .bg{background:#f6f4fb;border-radius:10px}
.gt .bar{border-radius:14px;color:#fff;font:700 18px Inter;display:flex;align-items:center;padding:0 14px;z-index:1}
.gt .bar span{font:500 14px Inter;opacity:.9;margin-left:8px}
.rc{display:flex;gap:16px}
.rc .cd{flex:1;background:#2a2440;color:#fff;border-radius:24px;padding:18px 22px;display:flex;gap:16px;align-items:center}
.rc .cd .fc{width:96px;height:96px;border-radius:20px;background:#3c3460;display:flex;align-items:center;justify-content:center;flex:none}
.rc .cd small{font:700 13px Inter;letter-spacing:2px;color:#b9b1d9}.rc .cd b{display:block;font:700 28px/1.3 Cardo}
.ck2{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}.ck2 span{font:600 15px Inter;background:#1f8a8a;border-radius:10px;padding:6px 10px}
.rc .sm{width:300px;flex:none;background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.rc .sm b{font:700 40px/1.3 Cardo;color:#1f8a8a}.rc .sm span{font:600 17px/1.4 Inter;color:#5f587a}
""", "<h1>Who's staying this week?<br><span>See every suite at a glance.</span></h1><div class=sub>Check-ins, check-outs and free suites, without a whiteboard.</div>",
f'''<div class=gt><span class=dh style="text-align:left">SAMPLE</span>{"".join(f'<span class=dh>{d}</span>' for d in days)}
{"".join(f'<span class=sr style="grid-row:{r+1};grid-column:1">Suite {r}</span>' + "".join(f'<span class=bg style="grid-row:{r+1};grid-column:{c+2}"></span>' for c in range(7)) for r in range(1,7))}
{"".join(f'<div class=bar style="grid-row:{r+1};grid-column:{a+1}/{b+2};background:{c}">{n}{"<span>sample</span>" if b-a>=3 else ""}</div>' for r,n,a,b,c in stays)}</div>
<div class=rc><div class=cd><div class=fc><svg viewBox="0 0 100 100" width="80"><ellipse cx="24" cy="42" rx="13" ry="24" fill="#8a5a32"/><ellipse cx="76" cy="42" rx="13" ry="24" fill="#8a5a32"/><circle cx="50" cy="54" r="30" fill="#d9a56a"/><ellipse cx="50" cy="68" rx="15" ry="11" fill="#f3dcc0"/><circle cx="39" cy="48" r="4" fill="#2a2440"/><circle cx="61" cy="48" r="4" fill="#2a2440"/><ellipse cx="50" cy="62" rx="6" ry="4" fill="#2a2440"/></svg></div>
<div><small>TODAY'S REPORT CARD · MAX · SAMPLE</small><b>Sent to Max's owner at 6 PM</b><div class=ck2><span>2 walks</span><span>Meals 2 of 2</span><span>Play group</span><span>3 photos</span></div></div></div>
<div class=sm><b>Suite 6</b><span>free Mon, Thu and Sun</span></div></div>''',
"#2a2440", "Run a pet boarding place? DM us", "background:#1f8a8a;color:#fff")

if __name__ == "__main__":
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
