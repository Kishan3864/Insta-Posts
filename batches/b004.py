import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 36 INDIA · Banquet hall · SINGLE · Montserrat? no -> Poppins + Gelasio · ivory / emerald / champagne
# New technique: 3D-tilted availability board (perspective + rotateX) with a flat answer card in front.
halls = ["Main hall", "Lawn", "Mini hall"]
days = ["Fri 11", "Sat 12", "Sun 13", "Mon 14", "Tue 15", "Wed 16", "Thu 17"]
grid = {"Main hall": "BBHFBFF", "Lawn": "BHFFFBB", "Mini hall": "FBBFHFF"}
lab = {"B": "Booked", "H": "On hold", "F": "Free"}
cells = "".join(f'<div class=hn>{h}</div>' + "".join(f'<div class="cl {c}">{lab[c]}</div>' for c in grid[h]) for h in halls)
P["p36_banquet"] = page("""
body{--f:'Poppins';--h:'Gelasio';background:#f7f3ea;color:#123c33}
h1{font-size:64px;font-weight:700;letter-spacing:-.5px;font-family:'Gelasio'} h1 span{color:#b07d2b;font-style:italic}
.sub{color:#58706a}
.vis{flex-direction:column;align-items:center;justify-content:space-between;gap:0;position:relative}
.stage{width:100%;perspective:1400px;display:flex;justify-content:center;margin-top:6px}
.brd{width:950px;background:#123c33;border-radius:26px;padding:24px;transform:rotateX(24deg);transform-origin:50% 100%;box-shadow:0 60px 80px rgba(18,60,51,.28)}
.bh{display:flex;justify-content:space-between;align-items:center;color:#f7f3ea;margin-bottom:14px}.bh b{font:700 30px 'Gelasio'}.bh span{font:600 15px Poppins;color:#cfe0d9}
.tb{display:grid;grid-template-columns:150px repeat(7,1fr);gap:8px}
.dh{font:700 17px Poppins;color:#cfe0d9;text-align:center;padding:4px 0}
.hn{font:700 20px Poppins;color:#f7f3ea;display:flex;align-items:center}
.cl{height:120px;border-radius:14px;font:700 16px Poppins;display:flex;align-items:center;justify-content:center}
.B{background:#2b5a4f;color:#9fc0b6}.H{background:#e8c879;color:#5a4210}.F{background:#f7f3ea;color:#123c33;box-shadow:inset 0 0 0 3px #7fd1ae}
.ans{position:relative;margin-top:-40px;width:952px;background:#fff;border-radius:26px;padding:24px 28px;box-shadow:0 30px 60px rgba(18,60,51,.2);display:flex;gap:20px;align-items:center;z-index:3}
.q{flex:1}.q small{font:600 18px Poppins;color:#8a9a95}.q b{display:block;font:700 36px/1.3 'Gelasio'}
.ok{background:#e1f4ea;color:#1f7a4d;border-radius:18px;padding:18px 20px;font:700 21px/1.35 Poppins;width:290px;flex:none}
.pts{display:flex;gap:14px;width:100%}
.pt{flex:1;background:#123c33;color:#f7f3ea;border-radius:20px;padding:24px 18px;display:flex;gap:12px;align-items:center;font:600 20px/1.3 Poppins}
.pt .ib{width:44px;height:44px;border-radius:12px;background:#e8c879;color:#123c33}
""", "<h1>\"Is the 14th free?\"<br><span>Answer in 5 seconds.</span></h1><div class=sub>For banquet halls and lawns: every hall, every date, booked, on hold or free.</div>",
f'''<div class=stage><div class=brd><div class=bh><b>Availability · December</b><span>Sample</span></div><div class=tb><div></div>{"".join(f"<div class=dh>{d}</div>" for d in days)}{cells}</div></div></div>
<div class=ans><div class=q><small>Enquiry · Mon 14 Dec · 300 guests</small><b>Main hall and Lawn are free.</b></div><div class=ok>Put on hold for 48 hours and send details</div></div>
<div class=pts>{"".join(f'<div class=pt><span class=ib>{ic(i,22)}</span>{t}</div>' for i,t in [("cal","Holds expire on their own"),("rupee","Advance noted per booking"),("users","Every enquiry saved")])}</div>''',
"#123c33", "Want this for your hall? DM us", "background:#123c33;color:#f7f3ea")

# ───────── 37 INDIA · Mehendi artist · CAROUSEL 5 · Gelasio + Poppins · henna orange / olive / blush cream
# New technique: CSS petal/dot ornament pattern (radial + conic gradients), arch-shaped image frames.
MH = """
body{--f:'Poppins';--h:'Gelasio';background:#fbf1e8;color:#3f2a17}
.orn{position:absolute;width:420px;height:420px;border-radius:50%;background:repeating-conic-gradient(from 0deg,rgba(194,88,28,.14) 0 8deg,transparent 8deg 22.5deg);-webkit-mask:radial-gradient(circle,transparent 0 22%,#000 23% 70%,transparent 71%)}
.o1{right:-150px;top:-150px}.o2{left:-190px;bottom:-200px}
h1{font-size:62px;font-weight:700;font-family:'Gelasio';letter-spacing:-.5px} h1 span{color:#c2581c;font-style:italic}
.sub{color:#7a5f4a}
.sn{font:700 17px Poppins;letter-spacing:3px;color:#3f4a1f;margin-top:22px}
.arch{border-radius:200px 200px 22px 22px;overflow:hidden;position:relative}
.hand{position:absolute;inset:14px;border-radius:186px 186px 14px 14px;background:radial-gradient(circle,#8a3b12 0 2.5px,transparent 3px) 32px 32px/64px 64px,radial-gradient(circle,#8a3b12 0 5px,transparent 6px) 0 0/64px 64px,radial-gradient(circle,transparent 0 9px,#8a3b12 10px 11px,transparent 12px 17px,#8a3b12 18px 20px,var(--sk) 21px) 0 0/64px 64px,repeating-conic-gradient(#8a3b12 0 9deg,transparent 9deg 30deg) 0 0/64px 64px;background-position:32px 32px,0 0,0 0,0 0;opacity:.92}
"""
def mslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#3f4a1f;color:#fff"):
    return page(MH+css, f"<div class=sn>{kick}</div><h1 style='margin-top:10px'>{title}</h1><div class=sub>{sub}</div>", vis, "#3f2a17", cta, ctacss,
                bg="<div class='orn o1'></div><div class='orn o2'></div>", tagline=f"{n} / 5")
skin = ["#e8b48f", "#d9a07a", "#c98d66", "#e3ab86", "#d49b73", "#efc09c"]
P["p37_mehendi_s1"] = mslide(1, "FOR MEHENDI ARTISTS", "Your designs deserve<br><span>a proper website.</span>",
 "4 things it should do for you. Swipe through.",
 f'''<div class=row>{"".join(f'<div class="arch fr" style="background:{c};--sk:{c}"><div class=hand></div></div>' for c in skin[:3])}</div>
 <div class=chips>{"".join(f'<span><b>{i}</b>{t}</span>' for i,t in [("1","Design gallery"),("2","Packages"),("3","Booking dates"),("4","Enquiry form")])}</div>''',
 """.vis{flex-direction:column;gap:22px}.row{flex:1;display:flex;gap:18px}.fr{flex:1;box-shadow:0 24px 50px rgba(63,42,23,.16)}
.chips{display:grid;grid-template-columns:1fr 1fr;gap:12px}.chips span{display:flex;gap:14px;align-items:center;background:#fff;border-radius:18px;padding:16px 18px;font:700 21px Poppins}
.chips b{width:42px;height:42px;border-radius:50%;background:#c2581c;color:#fff;font:700 19px/1 Poppins;display:flex;align-items:center;justify-content:center;flex:none}""")

cats = ["Bridal", "Party", "Arabic style", "Simple", "Feet", "Kids"]  # 'Kids' removed below (minors rule)
cats = ["Bridal", "Party", "Arabic style", "Simple", "Feet", "Guests"]
P["p37_mehendi_s2"] = mslide(2, "1 · DESIGN GALLERY", "Customers see your style<br><span>before they call.</span>",
 "Sorted by type, so a bride finds bridal designs in one tap.",
 browser(f'''<div class=gl><div class=fl>{"".join(f'<span class="{"on" if i==0 else ""}">{c}</span>' for i,c in enumerate(cats))}</div><div class=gg>{"".join(f'<div class=it><div class="arch ph" style="background:{c};--sk:{c}"><div class=hand></div></div><small>Design {i+1} · sample</small></div>' for i,c in enumerate(skin))}</div></div>''', "yourmehendi.in/designs", "flex:1"),
 """.vis{display:flex}.gl{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:14px;background:#fffaf5}
.fl{display:flex;gap:8px;flex-wrap:wrap}.fl span{font:600 16px Poppins;padding:8px 14px;border-radius:20px;background:#f3e4d6}.fl .on{background:#3f4a1f;color:#fff}
.gg{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px;min-height:0}
.it{display:flex;flex-direction:column;gap:6px;min-height:0}.it .ph{flex:1}.it small{font:500 14px Poppins;color:#7a5f4a}""")

pk = [("Bridal", "Both hands up to elbow, both feet", "About 5 to 6 hours"), ("Party", "Both hands, front and back", "About 1 to 2 hours"), ("Guests", "Simple designs for a group", "Per person, at the venue")]
P["p37_mehendi_s3"] = mslide(3, "2 · PACKAGES", "Clear packages.<br><span>Fewer back-and-forth chats.</span>",
 "What is included and how long it takes. Price on request, your way.",
 '<div class=pk>' + "".join(f'<div class=p><div class="arch pi" style="background:{skin[i]};--sk:{skin[i]}"><div class=hand></div></div><div class=pt><b>{a}</b><span>{b}</span><small>{ic("clock",16)} {c}</small></div><div class=pr>Price on request</div></div>' for i, (a, b, c) in enumerate(pk)) + '</div>',
 """.vis{display:flex}.pk{flex:1;display:flex;flex-direction:column;gap:14px}
.p{flex:1;display:flex;gap:20px;align-items:center;background:#fff;border-radius:24px;padding:16px 22px 16px 16px;box-shadow:0 14px 30px rgba(63,42,23,.08)}
.pi{width:130px;height:100%;flex:none}.pt{flex:1;display:flex;flex-direction:column;gap:4px}.pt b{font:700 30px 'Gelasio'}.pt span{font:500 19px Poppins}.pt small{font:500 16px Poppins;color:#7a5f4a;display:flex;gap:6px;align-items:center}
.pr{font:700 16px Poppins;color:#c2581c;background:#fbe7da;border-radius:14px;padding:10px 14px;white-space:nowrap}""")

mdays = [("1", ""), ("2", ""), ("3", "b"), ("4", "b"), ("5", ""), ("6", "h"), ("7", "")] + [(str(d), s) for d, s in zip(range(8, 29), ["", "b", "", "", "b", "b", "b", "", "", "h", "", "b", "", "", "", "b", "b", "", "", "", ""])]
P["p37_mehendi_s4"] = mslide(4, "3 · BOOKING DATES", "Busy season?<br><span>Show your free dates.</span>",
 "Customers pick a free date and pay an advance to confirm.",
 f'''<div class=cal><div class=ch><b>February · sample</b><span><i class=b></i>Booked <i class=h></i>On hold <i class=f></i>Free</span></div><div class=cg>{"".join(f'<div class="d {s or "fr"}">{d}</div>' for d,s in mdays)}</div></div>
 <div class=bk><b>Saturday 21 is free</b><span>Bridal · venue in your city</span><div class=bt>Pay advance to confirm</div></div>''',
 """.vis{gap:18px;align-items:stretch}.cal{flex:1.4;background:#fff;border-radius:24px;padding:22px;display:flex;flex-direction:column;gap:14px;min-width:0}
.ch{display:flex;justify-content:space-between;align-items:center}.ch b{font:700 26px 'Gelasio'}.ch span{font:600 14px Poppins;display:flex;gap:6px;align-items:center}
.ch i{width:14px;height:14px;border-radius:4px;display:inline-block;margin-left:8px}.ch .b{background:#c2581c}.ch .h{background:#e8c879}.ch .f{background:#e6efd9}
.cg{flex:1;display:grid;grid-template-columns:repeat(7,1fr);grid-template-rows:repeat(4,1fr);gap:8px}
.d{border-radius:12px;font:700 20px Poppins;display:flex;align-items:center;justify-content:center}.fr{background:#e6efd9;color:#3f4a1f}.b{background:#c2581c;color:#fff}.h{background:#e8c879;color:#5a4210}
.bk{flex:1;background:#3f4a1f;color:#fff;border-radius:24px;padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center;min-width:0}
.bk b{font:700 34px/1.25 'Gelasio'}.bk span{font:500 19px Poppins;color:#d9dfc6}.bk .bt{margin-top:18px;background:#fff;color:#3f4a1f;border-radius:14px;padding:16px;text-align:center;font:700 18px Poppins}""")

P["p37_mehendi_s5"] = mslide(5, "4 · ENQUIRY FORM", "Every enquiry arrives<br><span>with the details you need.</span>",
 "Date, place, number of people and a reference photo. Then DM us to build yours.",
 f'''<div class=fm>{"".join(f'<div class=f><small>{a}</small><b>{b}</b></div>' for a,b in [("Event date","Sat, 21 Feb"),("Location","Your city · venue name"),("Who needs mehendi","Bride + 8 guests"),("Style","Bridal, Arabic style for guests")])}
 <div class=up><span class=ib>{ic("img",30)}</span>Reference photo added</div><div class=sd>Send enquiry</div></div>
 <div class=cta2>{peep("Device","Smile","LongCurly",w=300,h=400)}<div class=bb>Want a website like this for your mehendi work?</div></div>''',
 """.vis{gap:20px;align-items:stretch}.fm{flex:1.2;background:#fff;border-radius:24px;padding:24px;display:flex;flex-direction:column;gap:12px;min-width:0}
.f{flex:1;background:#fbf1e8;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;justify-content:center}.f small{font:600 14px Poppins;color:#7a5f4a}.f b{font:600 21px Poppins}
.up{display:flex;gap:12px;align-items:center;border:3px dashed #e0b999;border-radius:16px;padding:14px;font:600 18px Poppins;color:#c2581c}
.sd{background:#c2581c;color:#fff;border-radius:16px;padding:16px;text-align:center;font:700 19px Poppins}
.cta2{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:14px;min-width:0}
.bb{background:#3f4a1f;color:#fff;border-radius:22px;padding:22px;font:700 24px/1.35 'Gelasio';text-align:center}""",
 cta="DM us for your website", ctacss="background:#c2581c;color:#fff")

# ───────── 38 INDIA · Barber shop · SINGLE · TeX Gyre Heros Cn + Inter · cream / navy / barber red
# New mockup: wall TV queue display + phone token card (phone 1 of 5 in this batch).
P["p38_barber"] = page("""
body{--f:'Inter';--h:'TeX Gyre Heros Cn';background:#f6efe2;color:#1b2a4a}
.pole{position:absolute;right:64px;top:0;width:44px;height:250px;border-radius:0 0 22px 22px;background:repeating-linear-gradient(135deg,#d7263d 0 18px,#fff 18px 36px,#1b2a4a 36px 54px,#fff 54px 72px);box-shadow:0 10px 20px rgba(0,0,0,.15)}
h1{font-family:'TeX Gyre Heros Cn';font-size:84px;font-weight:700;letter-spacing:-1px;line-height:1.2;text-transform:uppercase;max-width:820px} h1 span{color:#d7263d}
.sub{color:#5a6478;max-width:780px}
.vis{flex-direction:column;gap:20px}
.tv{background:#111;border-radius:22px;padding:16px;box-shadow:0 30px 60px rgba(27,42,74,.3)}
.sc{background:#1b2a4a;border-radius:10px;display:flex;color:#fff;overflow:hidden}
.now{width:44%;background:#d7263d;padding:26px;display:flex;flex-direction:column;justify-content:center;gap:14px}
.now small{font:700 18px Inter;letter-spacing:3px}.now b{font:700 140px/1.2 'TeX Gyre Heros Cn'}.now span{font:600 20px Inter}
.nx{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:10px}
.nx em{font:700 16px Inter;font-style:normal;letter-spacing:3px;color:#9fb0d0}
.q{display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.08);border-radius:12px;padding:12px 16px}
.q b{font:700 34px/1.2 'TeX Gyre Heros Cn';width:70px}.q span{flex:1;font:600 19px Inter}.q i{font:600 16px Inter;font-style:normal;color:#9fb0d0}
.bot{flex:1;display:flex;gap:22px;align-items:stretch;min-height:0}
.L{flex:1;display:flex;flex-direction:column;gap:12px}
.pt{flex:1;background:#fff;border-radius:20px;padding:16px 20px;display:flex;gap:14px;align-items:center;box-shadow:0 12px 26px rgba(27,42,74,.08)}
.pt .ib{width:50px;height:50px;border-radius:14px;background:#1b2a4a;color:#fff}.pt b{display:block;font:700 21px Inter}.pt small{display:block;font:400 17px Inter;color:#5a6478}
.tk{padding:4px 18px 18px;display:flex;flex-direction:column;gap:10px;flex:1;color:#1b2a4a;text-align:center}
.tk small{font:600 13px Inter;color:#5a6478}.tk .n{font:700 92px/1.2 'TeX Gyre Heros Cn';color:#d7263d}
.tk .w{background:#f6efe2;border-radius:12px;padding:10px;font:600 15px Inter}.tk .al{margin-top:auto;background:#1b2a4a;color:#fff;border-radius:12px;padding:12px;font:600 14px Inter}
""", "<h1>No more waiting<br><span>on the bench.</span></h1><div class=sub>For barber shops and salons: customers take a token on their phone and come back on time.</div>",
f'''<div class=tv><div class=sc><div class=now><small>NOW SERVING</small><b>11</b><span>Chair 2 · haircut</span></div><div class=nx><em>NEXT · SAMPLE</em>{"".join(f'<div class=q><b>{a}</b><span>{b}</span><i>{c}</i></div>' for a,b,c in [("12","Haircut + beard","about 10 min"),("13","Beard trim","about 25 min"),("14","Hair colour","about 35 min")])}</div></div></div>
<div class=bot><div class=L>{"".join(f'<div class=pt><span class=ib>{ic(i,24)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("qr","Scan at the door","Or take a token from home"),("bell","Alert when it's close","Come back just in time"),("users","Regulars remembered","Last service and style saved")])}</div>
{phone('<div class=tk><small>Your token · sample</small><div class=n>14</div><div class=w>3 people before you</div><div class=w>About 35 min wait</div><div class=al>We will alert you 10 min before</div></div>', w=270, h=450)}</div>''',
"#1b2a4a", "Get a token system. DM us", "background:#d7263d;color:#fff", bg="<div class=pole></div>")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
