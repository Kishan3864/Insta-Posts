import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 41 INDIA · DJ & sound rental · SINGLE · Montserrat + Inter · ink black / hot orange / warm white
# New technique: before/after slider with a round drag handle down the middle.
paper = [("Speakers (big)", "4", "3 back?"), ("Mixer", "1", "ok"), ("Mic + stand", "2", "1 stand ??"), ("LED par lights", "8", "check"), ("Cables box", "1", "—"), ("Smoke machine", "1", "with helper?"), ("Laser light", "2", "?")]
app = [("Speakers (big)", "4 out", "3 back", "r"), ("Mixer", "1 out", "Back", "g"), ("Mic + stand", "2 out", "Back", "g"), ("LED par lights", "8 out", "Back", "g"), ("Cables box", "1 out", "Back", "g"), ("Smoke machine", "1 out", "Due today", "y"), ("Laser light", "2 out", "Back", "g")]
P["p41_djsound"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#121212;color:#f6f1e9}
h1{font-family:'Montserrat';font-size:64px;font-weight:900;letter-spacing:-2px} h1 span{color:#ff6a00}
.sub{color:#b9b3aa}
.vis{flex-direction:column;gap:16px}
.sl{flex:1;display:flex;border-radius:26px;overflow:hidden;position:relative;min-height:0}
.bf{flex:1;background:#f4ecd8;color:#3b3125;padding:26px 54px 22px 26px;display:flex;flex-direction:column;gap:6px;font-family:'Gelasio';position:relative}
.af{flex:1;background:#1f1f1f;padding:26px 26px 22px 54px;display:flex;flex-direction:column;gap:9px;border:2px solid #2c2c2c;border-left:0;border-radius:0 26px 26px 0}
.tg{font:800 15px Inter;letter-spacing:3px;margin-bottom:6px}.bf .tg{color:#b3541e;font-family:Inter}.af .tg{color:#ff6a00}
.pr{flex:1;display:flex;align-items:center;gap:10px;font:italic 21px 'Gelasio';border-bottom:1px solid #d9cba8}
.pr b{font-weight:700;width:34px;text-align:center}.pr i{margin-left:auto;color:#c0392b;font-size:18px}
.ar{flex:1;display:flex;align-items:center;gap:10px;background:#2a2a2a;border-radius:12px;padding:0 12px;font:600 17px Inter}
.ar span{color:#9a948b;font-size:15px;margin-left:auto}.ar i{font-style:normal;font:700 13px Inter;padding:5px 9px;border-radius:9px;white-space:nowrap}
.g{background:#1e3b26;color:#7ee29a}.y{background:#3d3214;color:#ffcf5a}.r{background:#45201c;color:#ff8a7a}
.mid{position:absolute;left:50%;top:0;bottom:0;width:6px;margin-left:-3px;background:#ff6a00;z-index:3}
.hd{position:absolute;left:50%;top:50%;width:78px;height:78px;margin:-39px 0 0 -39px;border-radius:50%;background:#ff6a00;color:#121212;z-index:4;display:flex;align-items:center;justify-content:center;font:900 26px Montserrat;box-shadow:0 0 0 8px rgba(255,106,0,.25)}
.al{background:#ff6a00;color:#121212;border-radius:20px;padding:18px 22px;display:flex;gap:14px;align-items:center;font:700 21px/1.35 Inter}
.al .ib{width:48px;height:48px;border-radius:50%;background:#121212;color:#ff6a00}
""", "<h1>Gig over. Gear back?<br><span>Know before you leave.</span></h1><div class=sub>For DJ and sound rental businesses: every item out and back, per event.</div>",
f'''<div class=sl><div class=bf><div class=tg>BEFORE · PAPER LIST</div>{"".join(f"<div class=pr><span>{a}</span><b>{b}</b><i>{c}</i></div>" for a,b,c in paper)}</div>
<div class=af><div class=tg>AFTER · APP · SAMPLE</div>{"".join(f'<div class=ar>{a}<span>{b}</span><i class={c}>{d}</i></div>' for a,b,d,c in app)}</div><div class=mid></div><div class=hd>‹ ›</div></div>
<div class=al><span class=ib>{ic("bell",24)}</span>1 big speaker not back from Saturday's event. Alert sent before the next booking.</div>''',
"#f6f1e9", "Want this for your rental? DM us", "background:#ff6a00;color:#121212")

# ───────── 42 INDIA · Makeup artist · CAROUSEL 6 · Cardo + Poppins · black / champagne / dusty pink
# New format: mistakes list carousel (mistake + fix per slide).
MU = """
body{--f:'Poppins';--h:'Cardo';background:#151313;color:#f3e9dc}
body:before{content:"";position:absolute;inset:0;background:radial-gradient(800px 600px at 110% -10%,rgba(216,161,168,.22),transparent 65%)}
h1{font-family:'Cardo';font-size:64px;font-weight:700;letter-spacing:-.5px} h1 span{color:#e8c79a;font-style:italic}
.sub{color:#b8aca0}
.sn{font:600 17px Poppins;letter-spacing:4px;color:#d8a1a8;margin-top:22px}
"""
def mk(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#e8c79a;color:#151313"):
    return page(MU+css, f"<div class=sn>{kick}</div><h1 style='margin-top:10px'>{title}</h1><div class=sub>{sub}</div>", vis, "#f3e9dc", cta, ctacss, tagline=f"{n} / 6")
MX = """.vis{flex-direction:column;gap:16px}
.ms{background:#2a2222;border:2px solid #4a3434;border-radius:24px;padding:22px 26px;display:flex;gap:18px;align-items:center}
.ms .x{width:56px;height:56px;border-radius:50%;background:#5a2a2e;color:#ff9aa5;display:flex;align-items:center;justify-content:center;flex:none}
.ms b{display:block;font:600 15px Poppins;letter-spacing:3px;color:#ff9aa5}.ms p{font:700 30px/1.3 'Cardo'}
.fx{flex:1;background:#f3e9dc;color:#151313;border-radius:24px;padding:26px;display:flex;gap:24px;min-height:0}
.fx .t{width:330px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:12px}
.fx em{font:600 15px Poppins;font-style:normal;letter-spacing:3px;color:#9b5a62}.fx .t b{font:700 38px/1.2 'Cardo'}.fx .t small{font:400 20px/1.5 Poppins;color:#5a4d44}
.mo{flex:1;background:#fff;border-radius:18px;padding:18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(0,0,0,.08);min-width:0}
.mo h5{font:700 19px Poppins}.r{flex:1;display:flex;justify-content:space-between;align-items:center;background:#f7f1ea;border-radius:12px;padding:0 14px;font:500 17px Poppins}
.r i{font-style:normal;font:600 14px Poppins;padding:5px 10px;border-radius:9px}.ok{background:#e4f3e6;color:#2d7a3c}.pk{background:#f8e1e4;color:#9b3a4a}.go{background:#f3e3c7;color:#8a5a12}
"""
def mis(n, num, m, ft, fs, title, rows):
    mo = f'<div class=mo><h5>{title}</h5>' + "".join(f'<div class=r>{a}<i class={c}>{b}</i></div>' for a, b, c in rows) + '</div>'
    return mk(n, f"MISTAKE {num} OF 4", "Booking mistakes that<br><span>cost makeup artists.</span>", "", f'<div class=ms><span class=x>{ic("x",28,w=3)}</span><div><b>THE MISTAKE</b><p>{m}</p></div></div><div class=fx><div class=t><em>THE FIX</em><b>{ft}</b><small>{fs}</small></div>{mo}</div>', MX)

P["p42_makeup_s1"] = mk(1, "FOR MAKEUP ARTISTS", "4 booking mistakes<br><span>that cost you clients.</span>",
 "And the simple fix for each one. Swipe through.",
 f'''<div class=g4>{"".join(f'<div class=c><span class=n>0{i}</span><b>{t}</b></div>' for i,t in [(1,"Dates only in chats"),(2,"Advance not tracked"),(3,"Trial date forgotten"),(4,"No reminder before the day")])}</div>''',
 """.vis{display:flex}.g4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}
.c{border-radius:26px;padding:30px;display:flex;flex-direction:column;justify-content:space-between;background:#2a2222;border:2px solid #4a3434}
.c:nth-child(2),.c:nth-child(3){background:#e8c79a;color:#151313;border-color:#e8c79a}
.c .n{font:700 100px/1.2 'Cardo';opacity:.5}.c b{font:700 34px/1.25 'Cardo'}""")
P["p42_makeup_s2"] = mis(2, 1, "Booking dates live only in chats.", "One calendar for every booking.", "Bridal, party and trial dates in one place, with the venue and time.",
 "December · sample", [("Sat 5 · Bridal", "Confirmed", "ok"), ("Sun 6 · Party", "Confirmed", "ok"), ("Tue 8 · Trial", "Trial", "pk"), ("Fri 11 · Engagement", "Hold", "go"), ("Sun 13 · Bridal", "Confirmed", "ok")])
P["p42_makeup_s3"] = mis(3, 2, "The advance is \"somewhere in UPI\".", "Advance and balance per booking.", "See who paid the advance and what is due on the day, without scrolling payment apps.",
 "Payments · sample", [("Booking 1 · Bridal", "Advance paid", "ok"), ("Booking 2 · Party", "Advance due", "pk"), ("Booking 3 · Bridal", "Advance paid", "ok"), ("Booking 4 · Engagement", "Balance on day", "go"), ("Booking 5 · Party", "Fully paid", "ok")])
P["p42_makeup_s4"] = mis(4, 3, "The trial date gets forgotten.", "Trial linked to the main booking.", "Book the trial with the wedding date, and both show up together with notes from the trial.",
 "Bride 1 · sample", [("Trial", "Tue 8 Dec", "pk"), ("Main day", "Sun 13 Dec", "ok"), ("Look", "Soft glam", "go"), ("Skin notes", "Added", "ok"), ("Hair", "Low bun", "go")])
P["p42_makeup_s5"] = mis(5, 4, "No reminder the day before.", "Automatic reminders.", "The client gets the time, place and what to keep ready. You get your kit list.",
 "Reminder · sample", [("To client", "Sat, 6 PM", "ok"), ("Reporting time", "5:30 AM", "go"), ("Venue", "Added", "ok"), ("Kit list", "Ready", "ok"), ("Assistant", "Informed", "ok")])
P["p42_makeup_s6"] = mk(6, "YOUR ART, OUR APP", "Want a booking page<br><span>made for your work?</span>",
 "Portfolio, calendar, advance tracking and reminders in one simple app. We build it around how you work.",
 f'''<div class=w>{peep("Device","Smile","LongBangs",w=400,h=620)}<div class=lst>{"".join(f'<div class=i><span class=ib>{ic(i,26)}</span>{t}</div>' for i,t in [("img","Portfolio by look"),("cal","Booking calendar"),("rupee","Advance tracking"),("bell","Day-before reminders")])}</div></div>''',
 """.vis{align-items:stretch}.w{display:flex;align-items:flex-end;gap:20px;width:100%}
.lst{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px;padding-bottom:6px}
.i{flex:1;display:flex;gap:16px;align-items:center;background:#2a2222;border:2px solid #4a3434;border-radius:22px;padding:0 24px;font:700 28px 'Cardo'}
.i .ib{width:58px;height:58px;border-radius:16px;background:#e8c79a;color:#151313}""",
 cta="DM us for yours", ctacss="background:#d8a1a8;color:#151313")

# ───────── 43 USA · Auto detailing · SINGLE · Fira Sans · graphite / cyan glow / white
# New technique: dark-mode dashboard with glowing KPI tiles and a bar sparkline (sample data).
bars = [3, 5, 4, 6, 8, 9, 7]
bh = "".join(f'<div class=bc><i style="height:{v*10}%"></i><span>{d}</span></div>' for v, d in zip(bars, ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]))
P["p43_detailing"] = page("""
body{--f:'Fira Sans';background:#0e1116;color:#e8edf5}
body:before{content:"";position:absolute;inset:0;background:radial-gradient(700px 500px at 85% 20%,rgba(0,209,255,.16),transparent 70%)}
h1{font-size:64px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#00d1ff}
.sub{color:#9aa4b5}
.vis{display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:auto 1.5fr .62fr;gap:14px}
.k{background:#171c24;border:1px solid #263041;border-radius:20px;padding:18px 20px;display:flex;flex-direction:column;gap:4px}
.k small{font:600 16px 'Fira Sans';color:#8a95a8;letter-spacing:1px}.k b{font:800 56px/1.2 'Fira Sans'}.k span{font:500 17px 'Fira Sans';color:#00d1ff}
.k.gl{box-shadow:0 0 0 1px #00d1ff,0 0 30px rgba(0,209,255,.25)}
.pn{background:#171c24;border:1px solid #263041;border-radius:20px;padding:18px 20px;display:flex;flex-direction:column;gap:10px;min-height:0}
.pn h5{font:700 19px 'Fira Sans';display:flex;justify-content:space-between}.pn h5 span{font:600 13px 'Fira Sans';color:#8a95a8;letter-spacing:2px}
.tl{grid-column:span 2}
.jb{flex:1;display:flex;align-items:center;gap:12px;background:#1e2530;border-radius:12px;padding:0 16px;font:600 20px 'Fira Sans'}
.jb em{font-style:normal;color:#00d1ff;width:70px;font-weight:700}.jb span{flex:1}.jb i{font-style:normal;font:700 15px 'Fira Sans';padding:5px 9px;border-radius:9px;background:#13323b;color:#5be3ff}
.jb i.w{background:#3b3013;color:#ffcf5a}.jb i.d{background:#173a24;color:#7ee29a}
.ch{flex:1;display:flex;align-items:flex-end;gap:10px;padding-top:6px}.bc{flex:1;height:100%;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:6px}
.bc i{width:100%;border-radius:8px 8px 4px 4px;background:linear-gradient(#00d1ff,#0077ff)}.bc span{font:600 13px 'Fira Sans';color:#8a95a8}
.ad{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #263041;font:600 17px 'Fira Sans'}.ad b{color:#00d1ff}
.rp{grid-column:span 3}.rr{display:flex;gap:10px;flex:1}.rr div{flex:1;background:#1e2530;border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;justify-content:center}
.rr b{font:700 19px 'Fira Sans'}.rr small{font:500 15px 'Fira Sans';color:#8a95a8}
""", "<h1>Your detailing shop,<br><span>on one screen.</span></h1><div class=sub>Bookings, packages, add-ons and repeat customers. Sample data for a mobile and shop detailer.</div>",
f'''<div class="k gl"><small>BOOKED TODAY</small><b>7</b><span>2 mobile · 5 in shop</span></div><div class=k><small>THIS WEEK</small><b>42</b><span>jobs · sample</span></div><div class=k><small>DUE FOR A REVISIT</small><b>11</b><span>last visit 6+ weeks ago</span></div>
<div class="pn tl"><h5>Today <span>SAMPLE</span></h5>{"".join(f'<div class=jb><em>{t}</em><span>{a}</span><i class={c}>{s}</i></div>' for t,a,s,c in [("8:00","Full detail · SUV","Done","d"),("10:30","Interior only · sedan","In bay","x"),("1:00","Ceramic coating · truck","Next","w"),("3:30","Mobile wash · at home","Booked","x")])}</div>
<div class=pn><h5>Jobs per day</h5><div class=ch>{bh}</div></div>
<div class="pn rp"><h5>Top add-ons this month <span>SAMPLE</span></h5><div class=rr>{"".join(f"<div><b>{a}</b><small>{b}</small></div>" for a,b in [("Pet hair removal","Most added"),("Headlight restore","Rising"),("Engine bay clean","Steady"),("Odor treatment","New this month")])}</div></div>''',
"#e8edf5", "Want your own dashboard? DM us", "background:#00d1ff;color:#0e1116")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
