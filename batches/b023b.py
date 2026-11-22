import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 132 INDIA · Homestay owner · CAROUSEL 6 · Crimson Text + DM Sans · deodar green / sunrise peach / mist
# New techniques: SVG hill cottage scene at dusk, SVG room thumbnails, month calendar with "rooms left" numbers, folded guest-guide card.
HS = """
body{--f:'DM Sans';--h:'Crimson Text';background:#eef1ec;color:#1d3a2c}
h1{font-family:'Crimson Text';font-weight:700;font-size:66px;letter-spacing:-.4px;line-height:1.2} h1 span{color:#d9693a}
.sub{color:#56685d}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'DM Sans';letter-spacing:3px;color:#234d3a}
.kt b{width:44px;height:44px;border-radius:50%;background:#f4a77c;color:#1d3a2c;font:700 24px/1 'Crimson Text';display:flex;align-items:center;justify-content:center}
.kt + h1{margin-top:16px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(29,58,44,.08)}
.lb{font:700 13px 'DM Sans';letter-spacing:3px;color:#8a9a90}
"""
def hs(n, head, vis, css="", cta="Swipe", ctacss="background:#234d3a;color:#fff"):
    return page(HS + css, head, vis, "#1d3a2c", cta, ctacss, tagline=f"{n} / 6")
def pine(x, y, s, c="#234d3a"):
    return f'<path d="M{x} {y-60*s} L{x+22*s} {y-20*s} L{x+12*s} {y-20*s} L{x+30*s} {y+10*s} L{x-30*s} {y+10*s} L{x-12*s} {y-20*s} L{x-22*s} {y-20*s} Z" fill="{c}"/><rect x="{x-4*s}" y="{y+10*s}" width="{8*s}" height="{14*s}" fill="#5a3b28"/>'
scene = f'''<svg viewBox="0 0 900 520" width="100%" height="100%" preserveAspectRatio="xMidYMax slice">
<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7c9a6"/><stop offset="1" stop-color="#fbe8d6"/></linearGradient></defs>
<rect width="900" height="520" fill="url(#sk)"/><circle cx="700" cy="150" r="56" fill="#fff3e2"/>
<path d="M0 300 L160 150 L300 260 L460 110 L640 280 L780 180 L900 260 V520 H0 Z" fill="#9fb8ad"/>
<path d="M0 360 L200 250 L380 340 L560 240 L760 350 L900 300 V520 H0 Z" fill="#5e8a76"/>
<path d="M0 430 Q300 380 520 420 T900 410 V520 H0 Z" fill="#3c6b55"/>
{pine(90,410,1.6)}{pine(170,430,1.2)}{pine(760,405,1.7)}{pine(840,425,1.2)}{pine(650,430,1)}
<path d="M330 300 L450 220 L570 300 Z" fill="#a8442a"/><rect x="350" y="300" width="200" height="120" fill="#f3e2c7"/>
<rect x="372" y="324" width="44" height="40" rx="4" fill="#ffd27a"/><rect x="484" y="324" width="44" height="40" rx="4" fill="#ffd27a"/><rect x="428" y="352" width="44" height="68" rx="4" fill="#7a4a2e"/>
<rect x="340" y="418" width="220" height="10" fill="#7a4a2e"/></svg>'''
P["p132_hs_s1"] = hs(1, "<h1>Guests book your homestay<br>through agents?<br><span>Get your own<br>booking website.</span></h1>",
f'''<div class=c1><div class=sc1>{scene}<div class=bk1><span class=lb>SAMPLE HOMESTAY</span><b>4 rooms · hill view</b><em>{ic("check",18,"#fff",3)} Rooms free this weekend</em><u>Book direct</u></div></div>
<div class=ch1>{"".join(f'<div class="cd"><i>{ic(a,30,"#d9693a")}</i><b>{b}</b></div>' for a,b in [("img","Your own photos"),("cal","Live calendar"),("check","Advance online")])}</div></div>''',
""".c1{flex:1;display:flex;flex-direction:column;gap:16px}
.sc1{flex:1;border-radius:30px;overflow:hidden;position:relative}
.sc1>svg{position:absolute;inset:0}
.bk1{position:absolute;left:28px;top:28px;background:#fff;border-radius:22px;padding:22px 24px;display:flex;flex-direction:column;gap:6px;box-shadow:0 18px 36px rgba(29,58,44,.18)}
.bk1 b{font:700 36px/1.25 'Crimson Text'}
.bk1 em{font-style:normal;display:flex;align-items:center;gap:8px;font:600 19px 'DM Sans';color:#2b6b47}.bk1 em svg{background:#2b9a5a;border-radius:6px;padding:2px}
.bk1 u{text-decoration:none;margin-top:4px;background:#d9693a;color:#fff;border-radius:12px;padding:13px 16px;text-align:center;font:700 20px 'DM Sans'}
.ch1{flex:none;display:flex;gap:16px}
.ch1 .cd{flex:1;padding:16px 18px;display:flex;align-items:center;gap:12px}.ch1 b{font:700 22px/1.25 'DM Sans'}""")

def room(bed, wall, w=220):
    return f'''<svg viewBox="0 0 220 140" width="100%" height="100%" preserveAspectRatio="xMidYMid slice"><rect width="220" height="140" fill="{wall}"/>
<rect x="120" y="18" width="78" height="56" rx="4" fill="#cfe3ee"/><path d="M120 66 L146 44 L164 58 L184 40 L198 52 V74 H120 Z" fill="#7aa38e"/><rect x="157" y="18" width="4" height="56" fill="#fff"/>
<rect x="0" y="112" width="220" height="28" fill="#c79a6b"/><rect x="20" y="64" width="16" height="52" rx="3" fill="#7a4a2e"/>
<rect x="30" y="84" width="120" height="34" rx="6" fill="{bed}"/><rect x="34" y="74" width="34" height="16" rx="6" fill="#fff"/><rect x="72" y="74" width="34" height="16" rx="6" fill="#fff"/></svg>'''
rooms = [("Valley View Room", "2 guests · balcony", "#f4a77c", "#f3ead9"), ("Pine Room", "2 guests · garden", "#7aa38e", "#eef1ec"),
         ("Family Room", "4 guests · 2 beds", "#c9a5d6", "#f6efe6"), ("Attic Room", "2 guests · skylight", "#e7c76a", "#f2ece3")]
P["p132_hs_s2"] = hs(2, "<div class=kt><b>1</b>ROOMS PAGE</div><h1>Your own photos and rooms,<br><span>not a listing among hundreds.</span></h1>",
browser(f'''<div class=w2><div class=t2><div><span class=lb>SAMPLE HOMESTAY · 4 ROOMS</span><b>Pick your room</b></div><em>Dates: 18–20 Dec</em></div>
<div class=g2>{"".join(f'<div class=r2><div class=im2>{room(c,wl)}</div><div class=tx2><b>{a}</b><span>{b}</span><i>{"Free on your dates" if a!="Family Room" else "Booked on your dates"}</i></div></div>' for a,b,c,wl in rooms)}</div></div>''', "stay.yourhomestay.in", "flex:1"),
""".vis{flex-direction:column}
.w2{flex:1;padding:18px 22px 22px;display:flex;flex-direction:column;gap:14px}
.t2{display:flex;justify-content:space-between;align-items:flex-end}.t2 b{display:block;font:700 32px/1.25 'Crimson Text'}
.t2 em{font-style:normal;font:700 17px 'DM Sans';background:#eef1ec;padding:9px 14px;border-radius:12px}
.g2{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px}
.r2{border:1.5px solid #e3e8e3;border-radius:20px;overflow:hidden;display:flex;flex-direction:column}
.im2{flex:1;min-height:0;position:relative}.im2 svg{position:absolute;inset:0}
.tx2{flex:none;padding:12px 16px 14px;display:flex;flex-direction:column;gap:2px}
.tx2 b{font:700 24px/1.25 'Crimson Text'}.tx2 span{font:500 16px 'DM Sans';color:#56685d}
.tx2 i{font-style:normal;align-self:flex-start;margin-top:6px;font:700 14px 'DM Sans';padding:5px 9px;border-radius:8px;background:#ddf0e3;color:#2b6b47}""")

# December 2026: 1 Dec is a Tuesday. Rooms left out of 4 (sample).
left = {d: 4 for d in range(1, 32)}
for d, v in {5: 1, 6: 2, 12: 0, 13: 1, 18: 2, 19: 2, 20: 3, 24: 0, 25: 0, 26: 0, 27: 1, 28: 1, 29: 0, 30: 0, 31: 0, 11: 2, 4: 3}.items(): left[d] = v
def cell(d):
    if d is None: return '<div class="dy e3"></div>'
    v = left[d]; k = "f0" if v == 0 else "f1" if v <= 2 else "f4"
    sel = " sl3" if d in (18, 19) else ""
    return f'<div class="dy {k}{sel}"><b>{d}</b><span>{"Full" if v==0 else f"{v} left"}</span></div>'
cells = [None, None] + list(range(1, 32))
cells += [None] * (-len(cells) % 7)
P["p132_hs_s3"] = hs(3, "<div class=kt><b>2</b>LIVE CALENDAR</div><h1>Guests see free rooms<br><span>before they call you.</span></h1>",
f'''<div class="cd w3"><div class=t3><b>December 2026</b><span class=lb>ROOMS LEFT OUT OF 4 · SAMPLE</span></div>
<div class=wk3>{"".join(f'<span>{d}</span>' for d in ["Sun","Mon","Tue","Wed","Thu","Fri","Sat"])}</div>
<div class=gr3>{"".join(cell(d) for d in cells)}</div>
<div class=lg3><span><i class=f4></i>3–4 rooms free</span><span><i class=f1></i>1–2 left</span><span><i class=f0></i>Full</span><span><i class="sl3 f1"></i>Your dates: 18–20 Dec</span></div></div>''',
""".w3{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px}
.t3{display:flex;justify-content:space-between;align-items:center}.t3 b{font:700 34px/1.25 'Crimson Text'}
.wk3,.gr3{display:grid;grid-template-columns:repeat(7,1fr);gap:8px}
.wk3 span{font:700 15px 'DM Sans';color:#8a9a90;text-align:center}
.gr3{flex:1;grid-auto-rows:1fr}
.dy{border-radius:12px;padding:8px 10px;display:flex;flex-direction:column;justify-content:space-between}
.dy b{font:700 22px/1.2 'Crimson Text'}.dy span{font:600 13px 'DM Sans'}
.f4{background:#ddf0e3;color:#22573b}.f1{background:#ffe2c9;color:#8a4316}.f0{background:#e7e4df;color:#9a948b}.e3{background:transparent}
.sl3{box-shadow:inset 0 0 0 3px #d9693a}
.lg3{display:flex;gap:18px;flex-wrap:wrap}.lg3 span{display:flex;align-items:center;gap:8px;font:600 16px 'DM Sans';color:#56685d}
.lg3 i{width:20px;height:20px;border-radius:6px;display:block}""")

P["p132_hs_s4"] = hs(4, "<div class=kt><b>3</b>BOOK + ADVANCE</div><h1>Booking and advance done<br><span>while you sleep.</span></h1>",
f'''<div class=w4>{phone(f"""<div class=ap4><span class=lb>BOOKING · SAMPLE</span><b class=h4>Valley View Room</b>
{"".join(f'<div class=fd4><span>{a}</span><b>{b}</b></div>' for a,b in [("Check-in","Fri 18 Dec · 12 PM"),("Check-out","Sun 20 Dec · 11 AM"),("Guests","2"),("Name","Sample Guest"),("Phone","98XXX XXXXX")])}
<div class=pa4>Pay advance by UPI</div><div class=ok4>{ic("check",18,"#fff",3)} Advance paid · booking confirmed</div></div>""", w=360, h=740)}
<div class=sd4><div class="cd b4"><span class=lb>SENT TO GUEST ON WHATSAPP</span><p>Your booking at Sample Homestay is confirmed for 18–20 Dec, Valley View Room. We will share the route a day before.</p></div>
<div class="cd b4"><span class=lb>SENT TO YOU</span><p>New booking: Valley View Room, 18–20 Dec, advance paid. Calendar updated.</p></div>
<div class="cd b4 hl4"><b>No agent in the middle</b><span>The guest pays you directly and you keep the guest's contact.</span></div></div></div>''',
""".w4{flex:1;display:flex;gap:26px;align-items:center}
.ap4{flex:1;padding:8px 18px 18px;display:flex;flex-direction:column;gap:9px;background:#f6f8f5}
.h4{font:700 26px/1.25 'Crimson Text'}
.fd4{flex:1;background:#fff;border:1.5px solid #e3e8e3;border-radius:12px;padding:6px 12px;display:flex;flex-direction:column;justify-content:center}
.fd4 span{font:600 13px 'DM Sans';color:#8a9a90;letter-spacing:1px}.fd4 b{font:600 19px 'DM Sans'}
.pa4{background:#234d3a;color:#fff;border-radius:12px;padding:12px;text-align:center;font:700 16px 'DM Sans'}
.ok4{display:flex;align-items:center;justify-content:center;gap:8px;background:#ddf0e3;color:#22573b;border-radius:12px;padding:10px;font:700 15px 'DM Sans'}
.ok4 svg{background:#2b9a5a;border-radius:6px;padding:2px}
.sd4{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:16px;justify-content:center}
.b4{flex:1;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px}
.b4 p{font:500 20px/1.45 'DM Sans'}
.hl4{background:#234d3a;color:#fff}.hl4 b{font:700 28px/1.25 'Crimson Text';color:#f4a77c}.hl4 span{font:500 19px/1.4 'DM Sans';color:#d4e2d9}""")

guide = [("Check-in", "12 PM · Check-out 11 AM"), ("Getting here", "Last 2 km is a narrow road. Call us, we will pick you up from the main road."), ("Wi-Fi", "Name: SampleStay · password at the desk"),
         ("House rules", "Quiet after 10 PM · no smoking in rooms"), ("Nearby", "Sunrise point 1.5 km · waterfall walk 3 km · local market 4 km")]
P["p132_hs_s5"] = hs(5, "<div class=kt><b>4</b>GUEST GUIDE</div><h1>Send one guide link<br><span>instead of 20 messages.</span></h1>",
f'''<div class=w5><div class=gd5><div class=fo5></div><div class=in5><span class=lb>GUEST GUIDE · SAMPLE HOMESTAY</span><b class=h5>Welcome! Here is all you need.</b>
{"".join(f'<div class=it5><i>{ic(ico,24,"#d9693a")}</i><div><b>{a}</b><span>{b}</span></div></div>' for (a,b),ico in zip(guide,["clock","pin","globe","doc","map"]))}</div></div></div>''',
""".w5{flex:1;display:flex}
.gd5{flex:1;background:#fffaf2;border-radius:14px;position:relative;overflow:hidden;box-shadow:0 24px 48px rgba(29,58,44,.14)}
.fo5{position:absolute;top:0;bottom:0;left:50%;width:60px;transform:translateX(-50%);background:linear-gradient(90deg,transparent,rgba(29,58,44,.07),transparent)}
.in5{position:absolute;inset:0;padding:26px 30px;display:flex;flex-direction:column;gap:8px}
.h5{font:700 36px/1.25 'Crimson Text';margin-bottom:4px}
.it5{flex:1;display:flex;align-items:center;gap:18px;border-top:1.5px dashed #e3d9c8}
.it5 i{width:52px;height:52px;flex:none;border-radius:14px;background:#fde6d6;display:flex;align-items:center;justify-content:center}
.it5 b{display:block;font:700 29px/1.3 'Crimson Text'}.it5 span{font:500 21px/1.4 'DM Sans';color:#56685d}""")

P["p132_hs_s6"] = hs(6, "<h1>Run a homestay?<br><span>Let's build your own<br>booking website.</span></h1>",
f'''<div class=w6><div class=sc6>{scene}</div><div class=g6>{"".join(f'<div class="cd t6"><i>0{i+1}</i><div><b>{a}</b><span>{b}</span></div></div>' for i,(a,b) in enumerate([("Rooms page","Your photos, your words"),("Live calendar","Rooms left per day"),("Book + advance","Paid to you directly"),("Guest guide","One link before arrival")]))}</div></div>''',
""".w6{flex:1;display:flex;flex-direction:column;gap:18px}
.sc6{flex:none;height:300px;border-radius:30px;overflow:hidden;position:relative}.sc6>svg{position:absolute;inset:0}
.g6{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.t6{padding:18px 22px;display:flex;align-items:center;gap:16px}
.t6 i{font:700 44px/1.3 'Crimson Text';font-style:normal;color:#f4a77c}.t6 b{display:block;font:700 34px/1.25 'Crimson Text'}.t6 span{font:500 21px 'DM Sans';color:#56685d}""",
cta="Run a homestay? DM us", ctacss="background:#d9693a;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
