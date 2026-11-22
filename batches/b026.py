import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 146 INDIA · Tour operator (group trips) · CAROUSEL 5 · Archivo Black + DM Sans · sunset orange / deep teal / sand
# New techniques: top-down SVG tempo traveller seat map (booked / on hold / free), perforated ticket CTA.
TO = """
body{--f:'DM Sans';--h:'Archivo Black';background:#f6ecd9;color:#0f3c48}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:0;line-height:1.25;margin-top:22px} h1 span{color:#e8602c}
.sub{color:#4f6b72;font-size:23px}
.kk{font:700 16px 'DM Sans';letter-spacing:3px;color:#e8602c;margin-top:22px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(15,60,72,.08)}
.st-b{background:#0f4c5c;color:#fff}.st-h{background:#e8602c;color:#fff}.st-f{background:#fff;color:#0f4c5c;border:2px solid #0f4c5c}
.chip{font:700 15px 'DM Sans';padding:6px 12px;border-radius:10px;white-space:nowrap}
"""
def to(n, head, vis, css="", cta="Swipe", ctacss="background:#0f4c5c;color:#fff"):
    return page(TO + css, head, vis, "#0f3c48", cta, ctacss, tagline=f"{n} / 5")

# seat layout: seat 1 next to driver, rows 2-6 of 3 (2 + aisle + 1), back row 4 = 20 seats
SEAT = {}
st = {**{i: "b" for i in range(1, 21)}, 9: "h", 13: "h", 18: "h", 6: "f", 16: "f", 20: "f"}
def van(w=330):
    s = ['<svg viewBox="0 0 300 660" width="%d" style="display:block">' % w,
         '<rect x="10" y="10" width="280" height="640" rx="70" fill="#dfe7e4" stroke="#0f3c48" stroke-width="4"/>',
         '<path d="M40 90 Q150 30 260 90 L250 120 Q150 80 50 120 Z" fill="#9fc3cc"/>',
         '<rect x="190" y="140" width="70" height="66" rx="14" fill="#8aa1a6"/><circle cx="225" cy="173" r="20" fill="none" stroke="#0f3c48" stroke-width="5"/>',
         '<text x="225" y="228" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#0f3c48"><tspan>DRIVER</tspan></text>']
    pos = [(40, 140)]
    for r in range(5):
        y = 250 + r * 66
        pos += [(40, y), (104, y), (210, y)]
    pos += [(40, 580), (104, 580), (168, 580), (232, 580)]
    col = {"b": ("#0f4c5c", "#fff"), "h": ("#e8602c", "#fff"), "f": ("#ffffff", "#0f4c5c")}
    for i, (x, y) in enumerate(pos, 1):
        bg, fg = col[st[i]]
        s.append(f'<rect x="{x}" y="{y}" width="56" height="54" rx="12" fill="{bg}" stroke="#0f3c48" stroke-width="2.5"/>'
                 f'<text x="{x+28}" y="{y+35}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="21" fill="{fg}"><tspan>{i}</tspan></text>')
    s.append('</svg>')
    return "".join(s)

P["p146_tour_s1"] = to(1, "<div class=kk>GROUP TRIPS · TOUR OPERATORS</div><h1>Seats on a WhatsApp list?<br><span>Show a live seat map.</span></h1>",
f'''<div class="cd vn">{van(340)}</div>
<div class=rc>
<div class=tt><small>SAMPLE HILL TRIP · 20 SEATS</small><b>Fri 18 – Sun 20 Dec</b></div>
<div class=sc><i class="sq st-b"></i><div><b>14 booked</b><span>Seat confirmed</span></div></div>
<div class=sc><i class="sq st-h"></i><div><b>3 on hold</b><span>Seats 9, 13, 18 · pay by Tue 24 Nov</span></div></div>
<div class=sc><i class="sq st-f"></i><div><b>3 free</b><span>Seats 6, 16, 20 · open to book</span></div></div>
<div class=nt>Travellers pick their own seat. No more “Is the window seat free?” calls.</div></div>''',
css=""".vis{gap:22px}.vn{width:380px;flex:none;display:flex;align-items:center;justify-content:center;padding:18px;background:#fff}
.rc{flex:1;display:flex;flex-direction:column;gap:14px}
.tt{background:#0f4c5c;color:#fff;border-radius:22px;padding:20px 22px}.tt small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#ffc9a8}.tt b{display:block;font:400 30px/1.35 'Archivo Black';margin-top:6px}
.sc{flex:1;background:#fff;border-radius:22px;padding:16px 20px;display:flex;align-items:center;gap:16px;box-shadow:0 10px 24px rgba(15,60,72,.07)}
.sq{width:66px;height:66px;border-radius:14px;flex:none}.sc b{display:block;font:400 34px/1.35 'Archivo Black'}.sc span{font:500 20px/1.4 'DM Sans';color:#4f6b72}
.nt{background:#fde3d4;border-radius:20px;padding:18px 20px;font:600 20px/1.4 'DM Sans';color:#7a2e10}""")

days = [("DAY 1 · FRI 18 DEC", "Pickup 5:30 AM · reach the hills by 2 PM", "Check-in · sunset point · bonfire evening"),
        ("DAY 2 · SAT 19 DEC", "Breakfast · waterfall walk · local market", "Free evening · dinner at the stay"),
        ("DAY 3 · SUN 20 DEC", "Breakfast · view point · lunch on the way", "Drop back by 9 PM at the same points")]
P["p146_tour_s2"] = to(2, "<div class=kk>PART 1 · TRIP PAGE</div><h1>One link with the plan,<br><span>seats left and a book button.</span></h1>",
browser(f'''<div class=tp><div class=hr><svg viewBox="0 0 600 170" preserveAspectRatio="xMidYMid slice" width="100%" height="170" style="display:block"><rect width="600" height="170" fill="#ffd7b8"/><circle cx="470" cy="70" r="34" fill="#ffb07a"/><path d="M0 170 L120 70 L210 140 L320 40 L450 150 L520 100 L600 150 V170 Z" fill="#0f4c5c"/><path d="M0 170 L90 120 L200 165 L330 110 L460 170 Z" fill="#2f7f86"/></svg><div class=ht><b>Sample Hill Trip</b><span>3 days · 2 nights · Fri 18 – Sun 20 Dec</span></div></div>
<div class=bd><div class=it>{"".join(f'<div class=dy><small>{a}</small><b>{b}</b><span>{c}</span></div>' for a,b,c in days)}</div>
<div class=sd><small>INCLUDED</small>{"".join(f'<span class=in>{ic("check",18,w=3)}{t}</span>' for t in ["Van, both ways","2 nights stay","Breakfast + dinner","Sightseeing"])}
<div class=sl><b>3 seats left</b><span>Pick your seat on the map</span></div><div class=bt>Book a seat</div></div></div></div>''', url="yourtrips.in/hill-trip · sample", style="flex:1"),
css=""".vis{display:flex}.tp{flex:1;display:flex;flex-direction:column;min-height:0}
.hr{position:relative;flex:none}.ht{position:absolute;left:22px;bottom:16px;background:#fff;border-radius:16px;padding:10px 16px}.ht b{display:block;font:400 26px/1.35 'Archivo Black';color:#0f3c48}.ht span{font:600 16px 'DM Sans';color:#4f6b72}
.bd{flex:1;display:flex;gap:16px;padding:18px;min-height:0}
.it{flex:1;display:flex;flex-direction:column;gap:12px}
.dy{flex:1;background:#f6ecd9;border-radius:18px;padding:14px 18px;border-left:8px solid #e8602c;display:flex;flex-direction:column;justify-content:center;gap:4px}
.dy small{font:700 16px 'DM Sans';letter-spacing:2px;color:#e8602c}.dy b{font:700 25px/1.35 'DM Sans'}.dy span{font:500 21px/1.4 'DM Sans';color:#4f6b72}
.sd{width:290px;flex:none;display:flex;flex-direction:column;gap:10px}.sd small{font:700 14px 'DM Sans';letter-spacing:2px;color:#4f6b72}
.in{display:flex;align-items:center;gap:10px;font:600 21px 'DM Sans';background:#eef4f3;border-radius:12px;padding:11px 14px;color:#0f4c5c}
.sl{margin-top:auto;background:#fde3d4;border-radius:16px;padding:14px 16px}.sl b{display:block;font:400 24px/1.35 'Archivo Black';color:#c24a1c}.sl span{font:500 16px 'DM Sans';color:#7a2e10}
.bt{background:#e8602c;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 20px 'DM Sans'}""")

rows = [("1", "Traveller 1", "Pickup A", "Full paid", "st-b"), ("2", "Traveller 2", "Pickup A", "Full paid", "st-b"), ("5", "Traveller 5", "Pickup B", "Advance paid", "adv"),
        ("9", "Traveller 9", "Pickup B", "On hold · due Tue", "st-h"), ("11", "Traveller 11", "Pickup C", "Advance paid", "adv"), ("13", "Traveller 13", "Pickup C", "On hold · due Tue", "st-h"),
        ("17", "Traveller 17", "Pickup A", "Full paid", "st-b")]
P["p146_tour_s3"] = to(3, "<div class=kk>PART 2 · PAYMENTS</div><h1>Full paid, advance paid<br><span>or on hold, at a glance.</span></h1>",
f'''<div class=tb><div class="tr th"><span>SEAT</span><span>TRAVELLER · SAMPLE</span><span>PICKUP</span><span>STATUS</span></div>
{"".join(f'<div class=tr><span class=sn>{a}</span><span>{b}</span><span class=pk>{c}</span><span><em class="chip {k}">{d}</em></span></div>' for a,b,c,d,k in rows)}
<div class=mr>+ 10 more travellers</div></div>
<div class=bm><div class=sm><b>9</b><span>full paid</span></div><div class=sm><b>5</b><span>advance paid</span></div><div class="sm hh"><b>3</b><span>on hold</span></div>
<div class=rm>{ic("bell",26)}<span>Reminder sent to the 3 on hold: “Pay by Tue 24 Nov to keep your seat.”</span></div></div>''',
css=""".vis{flex-direction:column;gap:16px}
.tb{flex:1;background:#fff;border-radius:24px;padding:10px 22px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(15,60,72,.08)}
.tr{flex:1;display:grid;grid-template-columns:90px 1fr 170px 250px;align-items:center;border-bottom:1.5px solid #f1e8d8;font:600 21px 'DM Sans'}
.th{flex:none;height:46px;font:700 14px 'DM Sans';letter-spacing:2px;color:#8a9a9e}
.sn{width:46px;height:46px;border-radius:12px;background:#0f4c5c;color:#fff;display:flex;align-items:center;justify-content:center;font:700 19px 'DM Sans'}
.pk{color:#4f6b72;font-weight:500}.adv{background:#ffe9a8;color:#6b4a00}.chip{font-size:17px}
.mr{flex:none;height:50px;display:flex;align-items:center;font:600 18px 'DM Sans';color:#8a9a9e}
.bm{display:flex;gap:12px;flex:none}.sm{width:150px;background:#0f4c5c;color:#fff;border-radius:20px;padding:14px 16px}.sm b{display:block;font:400 36px/1.35 'Archivo Black'}.sm span{font:600 17px 'DM Sans';color:#cfe2e4}
.sm.hh{background:#e8602c}.sm.hh span{color:#fff}
.rm{flex:1;background:#fde3d4;border-radius:20px;padding:14px 18px;display:flex;align-items:center;gap:12px;font:600 18px/1.4 'DM Sans';color:#7a2e10}""")

pts = [("A", "5:30 AM", "Sample Point A", "6 of 6 boarded", "ok"), ("B", "6:00 AM", "Sample Point B", "5 of 6 boarded", "late"), ("C", "6:30 AM", "Sample Point C", "Next stop · 5", "nx")]
P["p146_tour_s4"] = to(4, "<div class=kk>PART 3 · DEPARTURE DAY</div><h1>Pickup list on your phone.<br><span>Know who boarded.</span></h1>",
f'''<div class=lf>{"".join(f'<div class=ft2><span class=ib>{ic(i,28)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("pin","Stops in order","Time and place for every pickup."),("check","Tick as they board","The count updates for the trip lead."),("phone","Call who is late","One tap from the list."),("send","Message everyone","“Van is 10 minutes away.”")])}</div>
{phone(f'<div class=ap><small>FRI 18 DEC · SAMPLE</small><b class=t>Pickup list</b>{"".join(f'<div class="pp {k}"><i>{a}</i><div><b>{c}</b><span>{b} · {d}</span></div></div>' for a,b,c,d,k in pts)}<div class=lt><b>Traveller 8 · Point B</b><span>Not boarded yet</span><em>{ic("phone",18)} Call</em></div><div class=ms>{ic("send",18)} Message all 17</div></div>', w=380, h=770)}''',
css=""".vis{gap:24px;align-items:center}.lf{flex:1;display:flex;flex-direction:column;gap:14px;align-self:stretch}
.ft2{flex:1;background:#fff;border-radius:22px;padding:16px 20px;display:flex;gap:16px;align-items:center;box-shadow:0 10px 24px rgba(15,60,72,.07)}
.ft2 .ib{width:58px;height:58px;border-radius:16px;background:#0f4c5c;color:#fff}.ft2 b{display:block;font:700 28px 'DM Sans'}.ft2 span{font:500 21px/1.4 'DM Sans';color:#4f6b72}
.ap{flex:1;padding:8px 16px 16px;display:flex;flex-direction:column;gap:10px;background:#f7f3ea}
.ap small{font:700 12px 'DM Sans';letter-spacing:2px;color:#8a9a9e}.ap .t{font:400 24px/1.35 'Archivo Black';color:#0f3c48}
.pp{flex:1;background:#fff;border-radius:16px;padding:10px 12px;display:flex;gap:12px;align-items:center}
.pp i{width:40px;height:40px;border-radius:50%;font:700 18px/40px 'DM Sans';font-style:normal;text-align:center;color:#fff;background:#0f4c5c;flex:none}
.pp.late i{background:#e8602c}.pp.nx i{background:#fff;color:#0f4c5c;border:2px solid #0f4c5c}
.pp b{display:block;font:700 19px 'DM Sans';color:#0f3c48}.pp span{font:500 15px 'DM Sans';color:#4f6b72}
.lt{background:#fde3d4;border-radius:16px;padding:12px;display:flex;flex-direction:column;gap:2px;position:relative}.lt b{font:700 16px 'DM Sans';color:#7a2e10}.lt span{font:500 14px 'DM Sans';color:#7a2e10}
.lt em{position:absolute;right:12px;top:14px;font:700 14px 'DM Sans';font-style:normal;background:#e8602c;color:#fff;border-radius:10px;padding:6px 10px;display:flex;gap:6px;align-items:center}
.ms{background:#0f4c5c;color:#fff;border-radius:14px;padding:13px;display:flex;gap:8px;justify-content:center;align-items:center;font:700 16px 'DM Sans'}""")

tk = [("SEAT MAP", "Live, pick your own"), ("TRIP PAGE", "Plan + book button"), ("PAYMENTS", "Paid or on hold"), ("PICKUP LIST", "Who boarded")]
P["p146_tour_s5"] = to(5, "<div class=kk>YOUR TURN</div><h1>Run group trips?<br><span>Let's build your<br>trip booking site.</span></h1>",
f'''<div class=sr2>{"".join(f'<i class="{ {"b":"st-b","h":"st-h","f":"st-f"}[st[i]]}">{i}</i>' for i in range(1,21))}</div><div class=tk><div class=tl><small>BOARDING PASS · YOUR TRIP APP</small><b>Your Tours</b><div class=fg>{"".join(f'<div><small>{a}</small><span>{b}</span></div>' for a,b in tk)}</div></div>
<div class=tr2><small>FOR</small><b>Tour operators</b><span>Weekend trips, group tours, college and office outings</span><div class=bc>{"".join(f'<i style="width:{w}px"></i>' for w in [4,2,6,2,3,5,2,4,6,2,3,2,5,4,2,6,3,2,4])}</div></div></div>
<div class=q>Tell us how you run trips today. We'll plan a booking site that fits your work.</div>''',
css=""".vis{flex-direction:column;justify-content:center;gap:26px}
.tk{display:flex;filter:drop-shadow(0 24px 40px rgba(15,60,72,.18))}
.tl{flex:1;background:#fff;border-radius:28px 0 0 28px;padding:28px 30px;border-right:4px dashed #f1d9c4;display:flex;flex-direction:column;gap:10px}
.tl>small,.tr2 small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#e8602c}.tl>b{font:400 54px/1.3 'Archivo Black';color:#0f3c48}
.fg{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:6px}.fg div{background:#f6ecd9;border-radius:16px;padding:22px 18px}.fg small{display:block;font:700 15px 'DM Sans';letter-spacing:2px;color:#8a9a9e}.fg span{font:700 25px/1.35 'DM Sans'}
.tr2{width:300px;flex:none;background:#0f4c5c;color:#fff;border-radius:0 28px 28px 0;padding:28px 26px;display:flex;flex-direction:column;gap:8px}
.tr2 small{color:#ffc9a8}.tr2 b{font:400 34px/1.3 'Archivo Black'}.tr2 span{font:500 22px/1.45 'DM Sans';color:#cfe2e4}
.bc{margin-top:auto;height:110px;background:#fff;border-radius:10px;display:flex;gap:4px;padding:10px 14px;align-items:stretch}.bc i{background:#0f3c48;display:block;flex:none}
.sr2{display:grid;grid-template-columns:repeat(10,1fr);gap:12px;background:#fff;border-radius:24px;padding:20px}.sr2 i{height:68px;border-radius:14px;font:700 24px/68px 'DM Sans';font-style:normal;text-align:center;border:2px solid #0f4c5c}.q{font:600 30px/1.45 'DM Sans';color:#4f6b72;text-align:center;padding:0 40px}.tl,.tr2{padding-top:40px;padding-bottom:40px}""",
cta="DM us to start", ctacss="background:#e8602c;color:#fff")


# ───────── 147 USA · SaaS founder (landing page + waitlist) · SINGLE · Montserrat + Inter · midnight violet / mint / white
# New technique: "anatomy" landing page with numbered pins inside the browser + matching numbered legend.
parts = [("1", "One clear promise", "Say who it is for and what it fixes, in one line."), ("2", "One email field", "Nothing else to fill in. Low effort, more signups."),
         ("3", "Three key features", "Short, with a simple icon each."), ("4", "A short survey", "Ask what problem they want solved first."), ("5", "FAQ", "Answer the 3 questions people always ask.")]
pin = lambda n: f'<i class=pn>{n}</i>'
P["p147_saas"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#1d1645;color:#f2f0ff}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#6ef2c0}
.sub{color:#b9b3e6}
.vis{gap:20px}
.pn{width:38px;height:38px;border-radius:50%;background:#6ef2c0;color:#1d1645;font:800 19px/38px Montserrat;font-style:normal;text-align:center;flex:none;box-shadow:0 0 0 5px rgba(110,242,192,.25)}
.lp{flex:1;padding:18px;display:flex;flex-direction:column;gap:12px;background:#fbfaff;color:#1d1645;min-height:0}
.nv{display:flex;justify-content:space-between;align-items:center;font:800 20px Montserrat}.nv span{font:500 14px Inter;color:#7a76a0}
.hero{background:#efeaff;border-radius:18px;padding:18px;display:flex;flex-direction:column;gap:10px;position:relative}
.hero b{font:800 30px/1.3 Montserrat;padding-right:46px}.hero p{font:500 19px/1.45 Inter;color:#5a567d}
.em{display:flex;gap:8px;position:relative}.em span{flex:1;background:#fff;border:1.5px solid #d8d1f5;border-radius:12px;padding:12px;font:500 17px Inter;color:#9a96b8}.em em{font-style:normal;background:#5b3df5;color:#fff;border-radius:12px;padding:12px 14px;font:700 17px Inter}
.ab{position:absolute;right:12px;top:12px}
.fs{display:flex;gap:10px;position:relative}.fs div{flex:1;background:#fff;border:1.5px solid #ece7fb;border-radius:14px;padding:12px;display:flex;flex-direction:column;gap:6px;font:700 18px/1.3 Inter}
.fs .ib{width:36px;height:36px;border-radius:10px;background:#e4fbf2;color:#0f8f66}
.sv{background:#fff;border:1.5px solid #ece7fb;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:8px;position:relative}.sv>b{font:700 18px Inter;padding-right:46px}
.sv label{display:flex;gap:8px;align-items:center;font:500 17px Inter;color:#5a567d}.sv label i{width:16px;height:16px;border-radius:50%;border:2px solid #b9b3e6;flex:none}.sv label i.on{border:5px solid #5b3df5}
.fq{flex:1;display:flex;flex-direction:column;gap:6px;position:relative}.fq div{flex:1;background:#fff;border:1.5px solid #ece7fb;border-radius:12px;padding:0 14px;display:flex;align-items:center;justify-content:space-between;font:600 18px Inter}
.rp{position:absolute;right:10px;top:8px}.fq div:first-of-type{padding-right:62px}
.lg2{width:380px;flex:none;display:flex;flex-direction:column;gap:10px}
.li{flex:1;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.12);border-radius:20px;padding:14px 18px;display:flex;gap:14px;align-items:center}
.li b{display:block;font:700 22px/1.3 Montserrat}.li span{font:500 17px/1.4 Inter;color:#b9b3e6}
""", "<h1>Testing a SaaS idea?<br><span>Start with a one-page<br>waitlist site.</span></h1><div class=sub>The 5 parts every landing page needs.</div>",
browser(f'''<div class=lp><div class=nv>YourApp<span>Sample landing page</span></div>
<div class=hero><span class=ab>{pin(1)}</span><b>Invoices that chase themselves.</b><p>For freelancers who hate asking for money twice.</p>
<div class=em><span>you@email.com</span><em>Join the waitlist</em></div></div>
<div class=fs><span class=rp>{pin(3)}</span>{"".join(f'<div><span class=ib>{ic(i,20)}</span>{t}</div>' for i,t in [("bell","Auto reminders"),("doc","Simple invoices"),("chart","Paid or not, at a glance")])}</div>
<div class=sv><span class=rp>{pin(4)}</span><b>What should we build first?</b><label><i class=on></i>Reminders</label><label><i></i>Invoice templates</label></div>
<div class=fq><span class=rp>{pin(5)}</span>{"".join(f'<div>{q}<span>+</span></div>' for q in ["When does it launch?","Will there be a free plan?","Is my data safe?"])}</div></div>''', url="yourapp.com · sample", style="flex:1") +
'<div class=lg2>' + "".join(f'<div class=li>{pin(n)}<div><b>{a}</b><span>{b}</span></div></div>' for n,a,b in parts) + '</div>',
"#f2f0ff", "Got an idea? DM us", "background:#6ef2c0;color:#1d1645", logo_color="#f2f0ff")
# pin 2 sits on the email row: add it inside .em
P["p147_saas"] = P["p147_saas"].replace('<div class=em><span>you@email.com</span>', f'<div class=em>{pin(2)}<span>you@email.com</span>')


# ───────── 148 INDIA · Swimming pool (memberships + batches) · SINGLE · Anton + Open Sans · pool blue / lane red / white tile
# New technique: top-down pool where each lane is a batch; swimmer dots = spots taken.
lanes = [("6 AM", "Adult beginners", 8, 10), ("7 AM", "Lap swim", 12, 12), ("8 AM", "Ladies batch", 6, 10), ("5 PM", "Adult beginners", 9, 10), ("6 PM", "Lap swim", 7, 12), ("7 PM", "Ladies batch", 10, 10)]
def lane(t, n, a, c):
    full = a == c
    dots = "".join(f'<i class="{"on" if k < a else ""}"></i>' for k in range(c))
    return f'<div class=ln><div class=lb><b>{t}</b><span>{n}</span></div><div class=dt>{dots}</div><em class="{"fu" if full else ""}">{"FULL" if full else f"{c-a} left"}</em></div>'
import random
_r=random.Random(148)
def _q(x,y):
    for fx,fy in [(0,0),(8,0),(0,8)]:
        if fx<=x<fx+5 and fy<=y<fy+5:
            return x in(fx,fx+4) or y in(fy,fy+4) or (fx+2<=x<=fx+2 and fy+2<=y<=fy+2) or (fx+1<x<fx+3 and fy+1<y<fy+3)
    return _r.random()<.45
QR="".join(f'<i class="{"" if _q(k%13,k//13) else "o"}"></i>' for k in range(169))
P["p148_pool"] = page("""
body{--f:'Open Sans';--h:'Anton';background:#eaf6fc;color:#0b3550}
.tile{position:absolute;inset:0;background-image:linear-gradient(#d6ebf5 2px,transparent 2px),linear-gradient(90deg,#d6ebf5 2px,transparent 2px);background-size:54px 54px}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.3px;line-height:1.25;margin-top:26px} h1 span{color:#e8433f}
.sub{color:#3f6a82}
.vis{gap:22px;align-items:center}
.pl{flex:1;align-self:stretch;background:#fff;border-radius:30px;padding:14px;display:flex;flex-direction:column;box-shadow:0 18px 40px rgba(11,53,80,.12)}
.wt{flex:1;border-radius:20px;background:linear-gradient(160deg,#39b5e6,#1689c4);display:flex;flex-direction:column;padding:6px 0;overflow:hidden}
.ln{flex:1;display:flex;align-items:center;gap:12px;padding:0 16px;position:relative;border-bottom:6px solid transparent;border-image:repeating-linear-gradient(90deg,#e8433f 0 14px,#fff 14px 28px) 6}
.ln:last-child{border-bottom:none}
.lb{width:178px;flex:none;background:#fff;border-radius:14px;padding:8px 12px}.lb b{display:block;font:400 26px/1.35 Anton;color:#0b3550}.lb span{font:600 15px 'Open Sans';color:#3f6a82}
.dt{flex:1;display:grid;grid-template-columns:repeat(6,22px);gap:6px 8px}.dt i{width:22px;height:22px;border-radius:50%;border:2px solid rgba(255,255,255,.75)}.dt i.on{background:#fff;border-color:#fff}
.ln em{font-style:normal;width:84px;text-align:center;background:#0b3550;color:#fff;border-radius:12px;padding:7px 0;font:700 15px 'Open Sans'}.ln em.fu{background:#e8433f}
.cap{display:flex;justify-content:space-between;font:600 15px 'Open Sans';color:#3f6a82;padding:10px 6px 0}
.ps{flex:1;padding:8px 16px 16px;display:flex;flex-direction:column;gap:10px;background:#f2f9fd}
.ps small{font:700 12px 'Open Sans';letter-spacing:2px;color:#7a98aa}.ps .t{font:400 26px/1.35 Anton}
.pc{background:linear-gradient(150deg,#1689c4,#0b3550);border-radius:18px;padding:14px;color:#fff;display:flex;flex-direction:column;gap:6px}
.pc b{font:700 18px 'Open Sans'}.pc span{font:500 14px 'Open Sans';color:#cfe8f5}
.qr{display:grid;grid-template-columns:repeat(13,1fr);gap:1px;width:150px;height:150px;background:#fff;border-radius:10px;padding:8px;align-self:center}
.qr i{background:#0b3550;border-radius:1px}.qr i.o{background:transparent}
.vb{background:#fff;border-radius:14px;padding:12px}.vb div{display:flex;justify-content:space-between;font:600 14px 'Open Sans'}.vb .br{height:10px;border-radius:6px;background:#dcecf5;margin-top:8px;overflow:hidden}.vb .br i{display:block;height:100%;width:75%;background:#1689c4}
.bk{margin-top:auto;background:#0b3550;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 15px 'Open Sans'}.rn{background:#ffe3e2;color:#9b1f1b;border-radius:14px;padding:12px;font:600 14px/1.4 'Open Sans'}
""", "<h1>Which batch has space?<br><span>Show it lane by lane.</span></h1><div class=sub>Members see free spots and book a batch on their phone.</div>",
f'''<div class=pl><div class=wt>{"".join(lane(*l) for l in lanes)}</div><div class=cap><span>Each dot = 1 member · sample</span><span>Today's batches</span></div></div>
{phone(f'<div class=ps><small>MEMBERSHIP · SAMPLE</small><b class=t>Your pool pass</b><div class=pc><b>Sample member</b><span>Batch: 6 AM · Adult beginners</span><span>Valid till 31 Jan 2027</span></div><div class=qr>' + QR + '</div><div class=vb><div><span>Visits used</span><span>18 of 24</span></div><div class=br><i></i></div></div><div class=rn>Renewal reminder goes out 7 days before.</div><div class=bk>Book a batch · 6 AM has 2 left</div></div>', w=350, h=740)}''',
"#0b3550", "Run a pool? DM us", "background:#e8433f;color:#fff", bg="<div class=tile></div>")


# ───────── 149 INDIA · GST practitioner (small office) · SINGLE · Gelasio + Inter · paper white / forest green / vermilion
# New technique: spiral tear-off wall calendar (December 2026) with circled due dates beside a client document tracker.
cl = [("Sample Traders", [1, 1, 1], "Ready to file"), ("Sample Textiles", [1, 0, 1], "Purchase bills pending"), ("Sample Hardware", [0, 0, 1], "Sales + purchase pending"),
      ("Sample Kirana", [1, 1, 0], "Bank statement pending"), ("Sample Motors", [1, 1, 1], "Ready to file")]
def cal():
    cells = [""] + [str(d) for d in range(1, 32)]
    cells += [""] * (35 - len(cells))
    mark = {"11": "GSTR-1", "20": "GSTR-3B"}
    h = "".join(f'<span class=wd>{d}</span>' for d in ["M", "T", "W", "T", "F", "S", "S"])
    h += "".join(f'<span class="dd{" mk" if c in mark else ""}">{c}</span>' for c in cells)
    return h
P["p149_gst"] = page("""
body{--f:'Inter';--h:'Gelasio';background:#fbfaf5;color:#1d2b24}
h1{font-family:'Gelasio';font-size:60px;font-weight:700;letter-spacing:-.4px;line-height:1.22} h1 span{color:#1f5b3f}
.sub{color:#5b6a62}
.vis{gap:22px}
.wc{width:400px;flex:none;display:flex;flex-direction:column;align-items:stretch}
.rg{height:40px;display:flex;justify-content:space-around;align-items:flex-end;padding:0 30px;background:#fff;border-radius:22px 22px 0 0;border:2px solid #e5e2d6;border-bottom:none}
.rg i{width:16px;height:30px;border-radius:8px;border:4px solid #7a7f7a;border-bottom:none;display:block;background:transparent}
.pgc{flex:1;background:#fff;border:2px solid #e5e2d6;border-top:2px dashed #cfcab8;border-radius:0 0 22px 22px;padding:18px 20px;display:flex;flex-direction:column;gap:12px;box-shadow:0 22px 40px rgba(29,43,36,.10)}
.mh{background:#1f5b3f;color:#fff;border-radius:14px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center}.mh b{font:700 28px/1.3 Gelasio}.mh span{font:600 16px Inter;color:#cde3d6}
.gr{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;flex:1}
.gr span{display:flex;align-items:center;justify-content:center;font:600 21px Inter;border-radius:50%}
.gr .wd{font:700 14px Inter;color:#8a958e}
.gr .mk{background:#e2553b;color:#fff}
.lgd{display:flex;flex-direction:column;gap:8px}.lgd div{display:flex;gap:10px;align-items:center;font:600 17px Inter}.lgd i{width:34px;height:34px;border-radius:50%;background:#e2553b;color:#fff;font:700 14px/34px Inter;font-style:normal;text-align:center;flex:none}
.lgd small{font:500 13px Inter;color:#8a958e}
.tr{flex:1;background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 16px 34px rgba(29,43,36,.08)}
.tr small{font:700 13px Inter;letter-spacing:2.5px;color:#8a958e}.tr h3{font:700 27px/1.3 Gelasio}
.hd{display:grid;grid-template-columns:1fr 84px 84px 84px;font:700 12px Inter;letter-spacing:1px;color:#8a958e;text-align:center;padding:0 2px}.hd span:first-child{text-align:left}
.cr{flex:1;display:flex;flex-direction:column;justify-content:center;gap:4px;border-top:1.5px solid #efede4}
.cr .tp{display:grid;grid-template-columns:1fr 84px 84px 84px;align-items:center}.cr b{font:700 21px Inter}
.cr .d{width:30px;height:30px;border-radius:50%;justify-self:center;display:flex;align-items:center;justify-content:center}
.cr .y{background:#dcefe3;color:#1f5b3f}.cr .n{background:#fde4de;color:#c23b22}
.cr .s{font:600 17px Inter;color:#5b6a62}.cr .s.ok{color:#1f5b3f}
.wa{background:#1f5b3f;color:#fff;border-radius:16px;padding:12px 14px;font:500 18px/1.45 Inter}.wa b{color:#ffd2c7}
""", "<h1>Chasing clients for bills<br>before every due date?<br><span>Let the app ask for them.</span></h1>",
f'''<div class=wc><div class=rg>{"<i></i>"*7}</div><div class=pgc><div class=mh><b>December 2026</b><span>Sample</span></div><div class=gr>{cal()}</div>
<div class=lgd><div><i>11</i><span>GSTR-1 due · Fri</span></div><div><i>20</i><span>GSTR-3B due · Sun</span></div><small>Monthly filers · always check the portal</small></div></div></div>
<div class=tr><small>CLIENT DOCUMENTS · NOV</small><h3>Who has sent what</h3>
<div class=hd><span>CLIENT · SAMPLE</span><span>SALES</span><span>PURCHASE</span><span>BANK</span></div>
{"".join(f'<div class=cr><div class=tp><b>{a}</b>' + "".join(f'<span class="d {"y" if v else "n"}">{ic("check" if v else "x",16,w=3)}</span>' for v in f) + f'</div><span class="s{" ok" if "Ready" in s else ""}">{s}</span></div>' for a,f,s in cl)}
<div class=wa><b>Auto reminder sent to 3 clients:</b> “Please share your pending bills for November by 5 Dec.”</div></div>''',
"#1d2b24", "Tax practice? DM us", "background:#1f5b3f;color:#fff")


# ───────── 150 CANADA · Martial arts school (adult classes) · CAROUSEL 5 · TeX Gyre Adventor + Roboto · mat blue / canvas cream / belt black
# New technique: belts drawn as horizontal SVG bands with a knot, used as bar rows (members + ready for test).
MA = """
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#f3ecdf;color:#161616}
h1{font-family:'TeX Gyre Adventor';font-size:58px;font-weight:700;letter-spacing:-.8px;line-height:1.22;margin-top:22px} h1 span{color:#2a4d8f}
.sub{color:#5a5650;font-size:23px}
.kk{font:700 16px Roboto;letter-spacing:3px;color:#2a4d8f;margin-top:22px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(22,22,22,.07)}
"""
def ma(n, head, vis, css="", cta="Swipe", ctacss="background:#2a4d8f;color:#fff"):
    return page(MA + css, head, vis, "#161616", cta, ctacss, tagline=f"{n} / 5")
belts = [("White", "#ffffff", 14, 5), ("Yellow", "#f5c518", 11, 4), ("Orange", "#f08a24", 9, 3), ("Green", "#3a9b4a", 8, 2), ("Blue", "#2a6fd1", 6, 1), ("Brown", "#7a4a2a", 3, 0)]
def belt(c, w=300):
    return (f'<svg viewBox="0 0 300 84" width="{w}" style="display:block"><rect x="4" y="14" width="292" height="34" rx="5" fill="{c}" stroke="#161616" stroke-width="2.5"/>'
            f'<path d="M134 40 L108 80 L128 80 L148 44 Z M166 40 L192 80 L172 80 L152 44 Z" fill="{c}" stroke="#161616" stroke-width="2.5"/>'
            f'<rect x="128" y="6" width="44" height="50" rx="7" fill="{c}" stroke="#161616" stroke-width="2.5"/></svg>')
P["p150_ma_s1"] = ma(1, "<div class=kk>MARTIAL ARTS SCHOOLS · ADULT CLASSES</div><h1>Who's ready for the next belt test?<br><span>Know without the binder.</span></h1>",
f'''<div class="cd bl">{"".join(f'<div class=br><div class=bn><b>{a}</b><span>{m} members</span></div>{belt(c,330)}<div class=rd><b>{r}</b><span>ready</span></div></div>' for a,c,m,r in belts)}</div>
<div class=sm2><div><b>51</b><span>adult members · sample</span></div><div class=hi><b>15</b><span>ready for the test on Sat, Dec 12</span></div></div>''',
css=""".vis{flex-direction:column;gap:16px}.bl{flex:1;padding:10px 24px;display:flex;flex-direction:column}
.br{flex:1;display:flex;align-items:center;gap:20px;border-bottom:1.5px solid #eee6d6}.br:last-child{border-bottom:none}
.bn{width:190px;flex:none}.bn b{display:block;font:700 26px/1.3 'TeX Gyre Adventor'}.bn span{font:500 17px Roboto;color:#5a5650}
.rd{margin-left:auto;width:120px;background:#e7eefb;border-radius:16px;padding:8px 0;text-align:center}.rd b{display:block;font:700 30px/1.3 'TeX Gyre Adventor';color:#2a4d8f}.rd span{font:600 14px Roboto;color:#2a4d8f}
.sm2{display:flex;gap:14px}.sm2 div{flex:1;background:#161616;color:#fff;border-radius:22px;padding:16px 22px;display:flex;align-items:center;gap:16px}
.sm2 b{font:700 44px/1.3 'TeX Gyre Adventor'}.sm2 span{font:500 19px/1.4 Roboto;color:#d9d3c6}.sm2 .hi{background:#2a4d8f}.sm2 .hi span{color:#dfe8fa}""")

wk = [("MON", [("6:00 PM", "Adult beginners", "4 spots"), ("7:30 PM", "Sparring", "Full")]), ("TUE", [("7:00 AM", "Early class", "6 spots")]),
      ("WED", [("6:00 PM", "Adult beginners", "2 spots"), ("7:30 PM", "Forms", "5 spots")]), ("THU", [("7:00 AM", "Early class", "8 spots")]),
      ("FRI", [("6:30 PM", "Sparring", "3 spots")]), ("SAT", [("10:00 AM", "Open mat", "10 spots")])]
P["p150_ma_s2"] = ma(2, "<div class=kk>PART 1 · CLASS BOOKING</div><h1>Members book a spot,<br><span>you see who is coming.</span></h1>",
browser(f'''<div class=wk>{"".join(f'<div class=dy><b>{d}</b><div class=cs>' + "".join(f'<div class="cl{" fu" if s=="Full" else ""}"><span class=tm>{t}</span><span class=nm>{n}</span><em>{s}</em></div>' for t,n,s in L) + '</div></div>' for d,L in wk)}</div>''', url="yourdojo.ca/classes · sample", style="flex:1"),
css=""".vis{display:flex}.wk{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.dy{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1.5px solid #eee6d6}.dy:last-child{border-bottom:none}
.dy>b{width:76px;font:700 26px 'TeX Gyre Adventor';color:#2a4d8f}
.cs{flex:1;display:flex;gap:12px}.cl{flex:1;background:#f3ecdf;border-radius:16px;padding:12px 16px;display:flex;align-items:center;gap:12px}
.tm{font:700 21px Roboto;width:104px;flex:none}.nm{font:500 22px Roboto;flex:1}
.cl em{font-style:normal;font:700 17px Roboto;background:#2a4d8f;color:#fff;border-radius:10px;padding:6px 10px;white-space:nowrap}.cl.fu em{background:#161616}""")

sk = [("Basic kicks set", 1), ("Blocks set 1 to 3", 1), ("Form 4", 1), ("Light sparring, 3 rounds", 1), ("Board break", 0)]
P["p150_ma_s3"] = ma(3, "<div class=kk>PART 2 · MEMBER PROGRESS</div><h1>Classes and skills<br><span>tracked for every member.</span></h1>",
f'''<div class="cd pc"><div class=ph><div class=av>M7</div><div><small>SAMPLE MEMBER 7</small><b>Green belt</b>{belt("#3a9b4a",230)}</div></div>
<div class=rg2><div class=ring><div><b>22</b><span>of 24 classes</span></div></div><div class=rt><b>2 more classes</b><span>to be ready for the blue belt test</span></div></div></div>
<div class="cd sk"><small>SKILLS FOR BLUE BELT</small>{"".join(f'<div class="si{" no" if not v else ""}"><i>{ic("check" if v else "clock",20,w=3)}</i><span>{t}</span><em>{"Done" if v else "Next class"}</em></div>' for t,v in sk)}
<div class=nt>The coach ticks skills on a tablet during class.</div></div>''',
css=""".vis{gap:20px}.pc{width:420px;flex:none;padding:24px;display:flex;flex-direction:column;gap:20px}
.ph{display:flex;gap:16px;align-items:center}.av{width:76px;height:76px;border-radius:50%;background:#2a4d8f;color:#fff;font:700 24px/76px 'TeX Gyre Adventor';text-align:center;flex:none}
.ph small{font:700 13px Roboto;letter-spacing:2px;color:#8a857c}.ph b{display:block;font:700 30px/1.3 'TeX Gyre Adventor';margin-bottom:6px}
.rg2{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px;background:#f3ecdf;border-radius:20px;padding:20px}
.ring{width:320px;height:320px;border-radius:50%;background:conic-gradient(#2a4d8f 0 330deg,#d9d0bf 330deg 360deg);display:flex;align-items:center;justify-content:center}
.ring div{width:246px;height:246px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ring b{font:700 84px/1.35 'TeX Gyre Adventor';color:#2a4d8f;margin-bottom:4px}.ring span{font:600 18px Roboto;color:#5a5650}
.rt{text-align:center}.rt b{display:block;font:700 30px/1.3 'TeX Gyre Adventor'}.rt span{font:500 21px Roboto;color:#5a5650}
.sk{flex:1;padding:22px;display:flex;flex-direction:column;gap:10px}.sk>small{font:700 13px Roboto;letter-spacing:2.5px;color:#8a857c}
.si{flex:1;display:flex;align-items:center;gap:14px;background:#eef6ef;border-radius:16px;padding:0 16px}
.si i{width:40px;height:40px;border-radius:50%;background:#3a9b4a;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.si span{flex:1;font:600 23px/1.3 Roboto}.si em{font-style:normal;font:700 17px Roboto;color:#2c7a3a}
.si.no{background:#f3ecdf}.si.no i{background:#8a857c}.si.no em{color:#5a5650}
.nt{background:#161616;color:#fff;border-radius:16px;padding:14px 16px;font:500 18px/1.4 Roboto}""")

tg = [("White → Yellow", "#ffffff", "#f5c518", 5), ("Yellow → Orange", "#f5c518", "#f08a24", 4), ("Orange → Green", "#f08a24", "#3a9b4a", 3), ("Green → Blue", "#3a9b4a", "#2a6fd1", 2), ("Blue → Brown", "#2a6fd1", "#7a4a2a", 1)]
msgs = [("Mon, Nov 30", "You're on the belt test list for Sat, Dec 12. Please confirm."), ("Thu, Dec 10", "Test day is Saturday, 10 AM. Arrive by 9:45 AM."), ("Sat, Dec 12", "Results and new belt photos are in the app.")]
P["p150_ma_s4"] = ma(4, "<div class=kk>PART 3 · TEST DAY</div><h1>Test list built for you.<br><span>Reminders go out on their own.</span></h1>",
f'''<div class="cd tl"><small>BELT TEST · SAT, DEC 12 · SAMPLE</small><b class=t>15 members ready</b>
{"".join(f'<div class=tg><span class=sw style="background:linear-gradient(90deg,{a} 0 50%,{b} 50% 100%)"></span><span class=nm>{n}</span><em>{q}</em></div>' for n,a,b,q in tg)}</div>
<div class=ms>{"".join(f'<div class=mg><small>{d}</small><span>{m}</span></div>' for d,m in msgs)}</div>''',
css=""".vis{gap:20px}.tl{flex:1;padding:22px;display:flex;flex-direction:column;gap:10px}
.tl>small{font:700 13px Roboto;letter-spacing:2px;color:#8a857c}.tl .t{font:700 32px/1.3 'TeX Gyre Adventor'}
.tg{flex:1;display:flex;align-items:center;gap:14px;border-top:1.5px solid #eee6d6}
.sw{width:100px;height:34px;border-radius:5px;border:2.5px solid #161616;flex:none}.tg .nm{flex:1;font:600 25px Roboto}
.tg em{font-style:normal;width:56px;height:46px;border-radius:12px;background:#2a4d8f;color:#fff;font:700 22px/46px 'TeX Gyre Adventor';text-align:center}
.ms{width:380px;flex:none;display:flex;flex-direction:column;gap:14px}
.mg{flex:1;background:#2a4d8f;color:#fff;border-radius:22px 22px 22px 6px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.mg small{font:700 16px Roboto;letter-spacing:1.5px;color:#c9d7f3}.mg span{font:500 23px/1.45 Roboto}""")

P["p150_ma_s5"] = ma(5, "<div class=kk>YOUR TURN</div><h1>Run a martial arts school?<br><span>Let's build your member app.</span></h1>",
f'''<div class=gd>{"".join(f'<div class=tl2>{belt(c,360)}<b>{a}</b><span>{b}</span></div>' for c,a,b in [("#f5c518","Belt tracker","Who is ready for which test"),("#f08a24","Class booking","Spots, full classes, check-in"),("#3a9b4a","Skill checklists","Ticked by the coach in class"),("#2a6fd1","Auto reminders","Test day, renewals, missed classes")])}</div>
<div class=q>Tell us how you run classes today. We'll plan an app that fits your school.</div>''',
css=""".vis{flex-direction:column;gap:22px}.gd{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.tl2{background:#fff;border-radius:24px;padding:24px;display:flex;flex-direction:column;justify-content:center;gap:10px;box-shadow:0 14px 30px rgba(22,22,22,.07)}
.tl2 b{font:700 34px/1.3 'TeX Gyre Adventor';margin-top:10px}.tl2 span{font:500 23px/1.4 Roboto;color:#5a5650}
.q{background:#161616;color:#fff;border-radius:22px;padding:24px 30px;font:500 26px/1.45 Roboto;text-align:center}""",
cta="DM us to start", ctacss="background:#2a4d8f;color:#fff")

if __name__ == "__main__":
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
