import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 196 INDIA · Wedding band and dhol group · CAROUSEL 5 · Cardo + Poppins · teal green / brass / cream
# New techniques: month booking calendar with brass "booked" coins, team roster drum/brass/light icons per date, route card with reach time.
BD = """
body{--f:'Poppins';--h:'Cardo';background:#f6efe0;color:#123c38}
h1{font-family:'Cardo';font-weight:700;font-size:64px;letter-spacing:-.4px;line-height:1.22} h1 span{color:#b5852b}
.kk{font:600 16px 'Poppins';letter-spacing:3px;color:#0f6b62;margin-top:22px}
.cd{background:#fffaf0;border-radius:26px;box-shadow:0 14px 30px rgba(18,60,56,.09)}
"""
def bd(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#123c38;color:#fff"):
    return page(BD + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#123c38", cta, ctacss, tagline=f"{n} / 5")
calls = [("Sample caller", "Free on 12 Dec?", "10:05 AM"), ("Sample caller", "Is 5 Dec still open?", "11:20 AM"), ("Sample caller", "Any Saturday left in Dec?", "1:45 PM"), ("Sample caller", "Can you do 9 Dec?", "4:10 PM")]
P["p196_band_s1"] = bd(1, "WEDDING BAND AND DHOL GROUPS", "Same date asked<br>four times a day?<br><span>Show your calendar.</span>",
f'''<div class=cl>{"".join(f'<div class=cr><span class=ib>{ic("phone",30)}</span><div><b>{q}</b><span>{a} · {t}</span></div><em>Diary?</em></div>' for a,q,t in calls)}
<div class=dy><span class=ib>{ic("file",30)}</span><p>One diary at home, one in the owner's pocket, and the team asks on the phone.</p></div></div>''',
css=""".cl{flex:1;display:flex;flex-direction:column;gap:12px}
.cr{flex:1;display:flex;align-items:center;gap:18px;background:#fffaf0;border-radius:22px;padding:0 22px;box-shadow:0 10px 22px rgba(18,60,56,.07)}
.cr .ib{width:62px;height:62px;border-radius:50%;background:#e7f1ef;color:#0f6b62}.cr div{flex:1}.cr b{display:block;font:700 30px/1.3 Cardo}.cr span{font:500 19px 'Poppins';color:#5e7a76}
.cr em{font-style:normal;font:600 18px 'Poppins';border:2px dashed #b5852b;color:#8a6118;border-radius:14px;padding:6px 14px}
.dy{display:flex;gap:16px;align-items:center;background:#123c38;color:#fff;border-radius:22px;padding:18px 22px}.dy .ib{width:56px;height:56px;border-radius:14px;background:#b5852b}.dy p{font:500 21px/1.4 'Poppins'}""")

bk = {1: "b", 3: "b", 5: "b", 6: "b", 9: "h", 10: "b", 12: "b", 13: "b", 17: "h", 19: "b", 20: "b", 24: "b", 26: "b", 27: "b", 31: "b"}
def dec():
    cells = '<span class=dh>Mon</span><span class=dh>Tue</span><span class=dh>Wed</span><span class=dh>Thu</span><span class=dh>Fri</span><span class=dh>Sat</span><span class=dh>Sun</span><i></i>'
    for d in range(1, 32):
        k = bk.get(d, "o")
        cells += f'<div class="dc k{k}"><b>{d}</b>{"<em></em>" if k=="b" else ("<small>Hold</small>" if k=="h" else "<small>Open</small>")}</div>'
    return cells
P["p196_band_s2"] = bd(2, "PART 1 · DATE CALENDAR", "Clients see open dates<br><span>before they call.</span>",
f'''<div class="cd cal"><div class=ch><b>December 2026</b><span>SAMPLE</span></div><div class=gr>{dec()}</div>
<div class=lg><span><i class=b></i>Booked</span><span><i class=h></i>On hold (advance pending)</span><span><i class=o></i>Open</span></div></div>''',
css=""".vis{display:flex}.cal{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.ch{display:flex;justify-content:space-between;align-items:center}.ch b{font:700 34px Cardo}.ch span{font:600 15px 'Poppins';letter-spacing:2.5px;color:#7a8f8b}
.gr{flex:1;display:grid;grid-template-columns:repeat(7,1fr);grid-template-rows:30px repeat(5,1fr);gap:8px}
.dh{font:600 16px 'Poppins';text-align:center;color:#5e7a76}
.dc{border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;background:#fff;border:2px solid #e8dfcc}
.dc b{font:700 26px/1.2 Cardo}.dc small{font:600 13px 'Poppins';color:#7a8f8b}
.dc.kb{background:#123c38;color:#fff;border-color:#123c38}.dc.kb em{width:22px;height:22px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#f3d58a,#b5852b)}
.dc.kh{background:#f7e7c2;border:2px dashed #b5852b}.dc.kh small{color:#8a6118}
.lg{display:flex;gap:20px;font:600 17px 'Poppins'}.lg span{display:flex;gap:8px;align-items:center}.lg i{width:18px;height:18px;border-radius:5px}.lg .b{background:#123c38}.lg .h{background:#f7e7c2;border:2px dashed #b5852b}.lg .o{border:2px solid #e8dfcc;background:#fff}""")
# Dec 1 2026 is a Tuesday → the grid needs one blank cell before the 1st (handled by <i></i>).

team = [("Dhol players", "4", "drum"), ("Brass band", "6", "music"), ("Light carriers", "8", "spark"), ("Singer", "1", "users")]
P["p196_band_s3"] = bd(3, "PART 2 · BOOKING SHEET", "Every booking with<br><span>team, time and place.</span>",
f'''<div class="cd bs"><div class=bh><div><small>BOOKING B-41 · SAMPLE CLIENT</small><b>Sat, 12 Dec · 7:00 PM</b></div><em>Advance paid</em></div>
<div class=tm>{"".join(f'<div><i>{ic("users",40)}</i><b>{n}</b><span>{a}</span></div>' for a,n,i in team)}</div>
<div class=rt><div class=rp><span class=dot></span><div><small>START POINT</small><b>Sample Hall, Station Road</b></div></div><div class=rl></div><div class=rp><span class="dot e"></span><div><small>END POINT</small><b>Sample Lawn, 1.5 km away</b></div></div></div>
<div class=rq><span>Team reaches by</span><b>6:15 PM</b><span>Songs list</span><b>Sent by client</b></div></div>''',
css=""".vis{display:flex}.bs{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:14px}
.bh{display:flex;justify-content:space-between;align-items:center}.bh small{display:block;font:600 14px/1.4 'Poppins';letter-spacing:2.5px;color:#7a8f8b;margin-bottom:4px}.bh b{font:700 36px/1.25 Cardo}
.bh em{font-style:normal;background:#0f6b62;color:#fff;border-radius:14px;padding:8px 16px;font:600 18px 'Poppins'}
.tm{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.tm div{background:#123c38;color:#fff;border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}
.tm i{color:#9fd0c8}.tm b{font:700 96px/1.3 Cardo;color:#f3d58a}.tm span{font:600 20px 'Poppins';text-align:center}
.rt{display:flex;flex-direction:column;gap:0;background:#fff;border-radius:20px;padding:16px 20px}
.rp{display:flex;align-items:center;gap:16px}.rp small{display:block;font:600 13px 'Poppins';letter-spacing:2px;color:#7a8f8b}.rp b{font:600 24px 'Poppins'}
.dot{width:24px;height:24px;border-radius:50%;background:#0f6b62;flex:none}.dot.e{background:#b5852b}
.rl{width:4px;height:30px;margin-left:10px;background:repeating-linear-gradient(#cfc2a5 0 6px,transparent 6px 12px)}
.rq{display:grid;grid-template-columns:auto 1fr auto 1fr;gap:6px 14px;align-items:center;background:#f7e7c2;border-radius:20px;padding:16px 20px}.rq span{font:500 20px 'Poppins';color:#6b5320}.rq b{font:700 30px/1.3 Cardo}""")

pays = [("B-38 · Sat, 5 Dec", "Fully paid", "p"), ("B-39 · Sun, 6 Dec", "Balance on the day", "d"), ("B-40 · Wed, 9 Dec", "Hold · advance pending", "h"), ("B-41 · Sat, 12 Dec", "Advance paid", "p"), ("B-42 · Sun, 13 Dec", "Advance paid", "p")]
P["p196_band_s4"] = bd(4, "PART 3 · ADVANCE AND TEAM ALERTS", "Holds expire on time.<br><span>The team gets the plan.</span>",
f'''<div class=pw><div class="cd pl">{"".join(f'<div class="pr {k}"><b>{a}</b><em>{s}</em></div>' for a,s,k in pays)}</div>
<div class=al><div class=am><small>TO THE TEAM · FRI, 11 DEC · SAMPLE</small><b>Tomorrow: B-41</b><span>Report at Sample Hall by 6:15 PM. 4 dhol, 6 brass, 8 lights, 1 singer.</span></div>
<div class="am c"><small>TO THE CLIENT · HOLD ON 9 DEC</small><b>Your hold ends tomorrow</b><span>Pay the advance to keep Wed, 9 Dec.</span></div></div></div>''',
css=""".pw{flex:1;display:flex;flex-direction:column;gap:14px}
.pl{flex:none;padding:10px 20px;display:flex;flex-direction:column;gap:0}.pr{padding:16px 0;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #efe5cf}
.pr b{font:700 26px/1.3 Cardo}.pr em{font-style:normal;font:600 18px 'Poppins';border-radius:12px;padding:7px 14px}.pr.p em{background:#0f6b62;color:#fff}.pr.d em{background:#e7f1ef;color:#0f6b62}.pr.h em{background:#f7e7c2;color:#8a6118;border:2px dashed #b5852b}
.al{flex:1;display:flex;gap:14px}.am{flex:1;justify-content:center;background:#123c38;color:#fff;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;gap:6px}
.am small{font:600 13px/1.4 'Poppins';letter-spacing:2px;color:#9fd0c8}.am b{font:700 38px/1.3 Cardo;color:#f3d58a}.am span{font:500 22px/1.45 'Poppins'}
.am.c{background:#b5852b}.am.c small{color:#fbeacb}.am.c b{color:#fff}""")

P["p196_band_s5"] = bd(5, "YOUR TURN", "Run a wedding band<br>or dhol group?<br><span>Let's build your booking app.</span>",
f'''<div class=t5>{"".join(f'<div><i>{n}</i><b>{a}</b><span>{b}</span></div>' for n,a,b in [("01","Date calendar","Open, hold, booked"),("02","Booking sheet","Team, time, place"),("03","Advance tracker","Holds expire on time"),("04","Team alerts","Plan sent the day before")])}</div>''',
cta="DM us to build yours", ctacss="background:#b5852b;color:#fff",
css=""".t5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}.t5 div{background:#123c38;color:#fff;border-radius:26px;padding:26px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;position:relative}
.t5 div:nth-child(2),.t5 div:nth-child(3){background:#fffaf0;color:#123c38}
.t5 i{position:absolute;top:18px;left:26px;font-style:normal;font:700 80px/1.3 Cardo;color:#b5852b}.t5 b{font:700 40px/1.25 Cardo}.t5 span{font:500 20px 'Poppins';opacity:.85}""")


# ───────── 197 INDIA · Tyre retreading plant · SINGLE · Archivo Black + DM Sans · carbon / safety orange / fog
# New technique: SVG truck tyre with a progress arc around it (stages as arc segments) + casing intake list.
def tyre():
    stages = ["Inspect", "Buff", "Repair", "Build", "Cure", "Check"]
    done = 4
    out = '<svg viewBox="0 0 440 440" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block">'
    for i, s in enumerate(stages):
        a0 = math.radians(-90 + i * 60 + 3); a1 = math.radians(-90 + (i + 1) * 60 - 3)
        r = 200
        x0, y0, x1, y1 = 220 + r * math.cos(a0), 220 + r * math.sin(a0), 220 + r * math.cos(a1), 220 + r * math.sin(a1)
        col = "#ff6b1a" if i < done else ("#ffd2b8" if i == done else "#d5d8dc")
        out += f'<path d="M{x0:.1f} {y0:.1f} A{r} {r} 0 0 1 {x1:.1f} {y1:.1f}" fill="none" stroke="{col}" stroke-width="24"/>'
        am = math.radians(-90 + i * 60 + 30)
    out += '<circle cx="220" cy="220" r="170" fill="#22252a"/>'
    for i in range(36):
        a = math.radians(i * 10)
        out += f'<rect x="-9" y="-170" width="18" height="26" rx="3" fill="#3a3e45" transform="translate(220 220) rotate({i*10})"/>'
    out += ('<circle cx="220" cy="220" r="126" fill="#2d3137"/><circle cx="220" cy="220" r="86" fill="#c9ccd1"/><circle cx="220" cy="220" r="62" fill="#e6e8eb"/>'
            '<text x="220" y="212" text-anchor="middle" font-family="Archivo Black" font-size="30" fill="#22252a"><tspan>Cure</tspan></text>'
            '<text x="220" y="242" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#5b6068"><tspan>stage 5 of 6</tspan></text></svg>')
    return out
stg = [("Inspect", 1), ("Buff", 1), ("Repair", 1), ("Build", 1), ("Cure", 2), ("Check", 0)]
cas = [("T-207", "Sample transport · 4 tyres", "Cure", "w"), ("T-208", "Sample fleet · 6 tyres", "Build", "w"), ("T-205", "Sample truck owner · 2 tyres", "Ready", "d"), ("T-209", "Sample transport · 1 tyre", "Rejected at inspection", "x")]
P["p197_retread"] = page("""
body{--f:'DM Sans';--h:'Archivo Black';background:#e8eaed;color:#22252a}
h1{font-family:'Archivo Black';font-size:58px;font-weight:400;letter-spacing:-.8px;line-height:1.22} h1 span{color:#e8590c}
.sub{color:#5b6068;font-size:23px}
.vis{flex-direction:column;gap:16px}
.tp{flex:1;display:flex;gap:16px;min-height:0}
.ty{width:460px;flex:none;background:#fff;border-radius:28px;padding:16px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(34,37,42,.08)}
.ty small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#7b8088;margin-left:6px}.ty .tv{flex:1;min-height:0}
.sl{flex:1;background:#22252a;color:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:8px}
.sl small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#a6abb3}.sl h3{font:400 30px/1.3 'Archivo Black'}
.sr{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid rgba(255,255,255,.12)}
.sr i{width:30px;height:30px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center}
.sr.k1 i{background:#ff6b1a}.sr.k2 i{background:#ffd2b8;box-shadow:0 0 0 5px rgba(255,107,26,.35)}.sr.k0 i{border:3px solid #6b7079}
.sr b{font:700 22px 'DM Sans'}.sr em{margin-left:auto;font-style:normal;font:600 17px 'DM Sans';color:#a6abb3}.sr.k2 em{color:#ffb28a}
.cs{background:#fff;border-radius:26px;padding:16px 20px;display:grid;grid-template-columns:1fr 1fr;gap:10px;box-shadow:0 12px 26px rgba(34,37,42,.07)}
.cs>small{grid-column:1/-1;font:700 14px 'DM Sans';letter-spacing:2.5px;color:#7b8088}
.cs div{background:#f2f3f5;border-radius:16px;padding:10px 14px;display:flex;flex-direction:column;gap:2px}.cs b{font:400 22px/1.3 'Archivo Black'}.cs span{font:500 16px 'DM Sans';color:#5b6068}
.cs em{font-style:normal;align-self:flex-start;font:700 15px 'DM Sans';border-radius:10px;padding:4px 10px;margin-top:4px}
.cs .w em{background:#ffe3d3;color:#b94608}.cs .d em{background:#22252a;color:#fff}.cs .x em{background:#d5d8dc;color:#3b4047}
""", "<h1>\"Is my tyre ready?\"<br><span>Answer it with one link.</span></h1><div class=sub>Track every casing through each retreading stage.</div>",
f'''<div class=tp><div class=ty><small>CASING T-207 · 1 OF 4 · SAMPLE</small><div class=tv>{tyre()}</div></div>
<div class=sl><small>T-207 · SAMPLE TRANSPORT</small><h3>Stages</h3>{"".join(f'<div class="sr k{k}"><i>{ic("check",16,w=3) if k==1 else ""}</i><b>{a}</b><em>{"Done" if k==1 else ("Now, ready by 5 PM" if k==2 else "Next")}</em></div>' for a,k in stg)}</div></div>
<div class=cs><small>CASINGS IN THE PLANT · SAMPLE</small>{"".join(f'<div class={k}><b>{a}</b><span>{b}</span><em>{s}</em></div>' for a,b,s,k in cas)}</div>''',
"#22252a", "Run a retreading plant? DM us", "background:#e8590c;color:#fff")


# ───────── 198 USA · Bicycle repair shop · SINGLE · Bitter + Fira Sans · sage / ink / orange
# New technique: SVG bicycle with a hanging repair tag (claim number) + work-stand queue list.
def bike():
    return ('<svg viewBox="0 0 600 380" width="100%" style="display:block">'
            '<circle cx="140" cy="250" r="98" fill="none" stroke="#1f2a24" stroke-width="12"/><circle cx="460" cy="250" r="98" fill="none" stroke="#1f2a24" stroke-width="12"/>'
            '<circle cx="140" cy="250" r="10" fill="#1f2a24"/><circle cx="460" cy="250" r="10" fill="#1f2a24"/>'
            '<path d="M140 250 L250 250 L330 130 L200 130 Z" fill="none" stroke="#e86a1c" stroke-width="12" stroke-linejoin="round"/>'
            '<path d="M330 130 L460 250 M250 250 L190 92 M330 130 L318 80" fill="none" stroke="#e86a1c" stroke-width="12" stroke-linecap="round"/>'
            '<path d="M160 92 h64" stroke="#1f2a24" stroke-width="14" stroke-linecap="round"/><path d="M296 80 h50" stroke="#1f2a24" stroke-width="10" stroke-linecap="round"/>'
            '<circle cx="250" cy="250" r="22" fill="none" stroke="#1f2a24" stroke-width="8"/>'
            '<path d="M346 80 L370 120" stroke="#1f2a24" stroke-width="3"/>'
            '<rect x="348" y="118" width="150" height="104" rx="10" fill="#fffdf6" stroke="#1f2a24" stroke-width="3"/><circle cx="372" cy="138" r="7" fill="none" stroke="#1f2a24" stroke-width="3"/>'
            '<text x="430" y="150" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="16" fill="#6c7a70"><tspan>CLAIM</tspan></text>'
            '<text x="423" y="186" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="34" fill="#1f2a24"><tspan>#317</tspan></text>'
            '<text x="423" y="210" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="15" fill="#e86a1c"><tspan>Ready Wed</tspan></text></svg>')
q = [("#317", "Tune-up + new chain", "On the stand", "n"), ("#318", "Flat tire, rear", "Next", "x"), ("#319", "Brake pads, both", "Waiting for parts", "w"), ("#314", "Wheel true + tune-up", "Ready for pickup", "d")]
P["p198_bikeshop"] = page("""
body{--f:'Fira Sans';--h:'Bitter';background:#dfe8df;color:#1f2a24}
h1{font-family:'Bitter';font-size:62px;font-weight:800;letter-spacing:0;line-height:1.22} h1 span{color:#d15a12}
.sub{color:#4f5f54;font-size:23px}
.vis{flex-direction:column;gap:16px}
.bk{background:#fffdf6;border-radius:28px;padding:16px 24px 10px;box-shadow:0 14px 30px rgba(31,42,36,.08)}.bk svg{width:auto!important;height:330px;margin:0 auto}
.bk small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#6c7a70}
.ql{flex:1;background:#1f2a24;color:#fff;border-radius:28px;padding:18px 22px;display:flex;flex-direction:column;gap:8px}
.ql small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#a9bcae}
.qr{flex:1;display:flex;align-items:center;gap:16px;border-top:1px solid rgba(255,255,255,.12)}
.qr b{width:100px;font:800 32px/1.3 Bitter;color:#ffb07a}.qr span{flex:1;font:600 25px 'Fira Sans'}
.qr em{font-style:normal;font:700 19px 'Fira Sans';border-radius:12px;padding:10px 14px;width:220px;text-align:center}
.qr.n em{background:#e86a1c}.qr.x em{background:#33423a;color:#d6e2d9}.qr.w em{border:2px dashed #a9bcae;color:#d6e2d9}.qr.d em{background:#9fd3a8;color:#1f2a24}
.tx{display:flex;gap:10px;align-items:center;background:#33423a;border-radius:14px;padding:12px 16px;font:600 18px 'Fira Sans';color:#e6efe8}.tx svg{color:#ffb07a;flex:none}
""", "<h1>Bikes lined up. Which<br><span>one is ready today?</span></h1><div class=sub>Every bike gets a claim number, a job and a ready day.</div>",
f'''<div class=bk><small>DROP-OFF · SAMPLE CUSTOMER · CLAIM #317</small>{bike()}</div>
<div class=ql><small>REPAIR QUEUE · TODAY · SAMPLE</small>{"".join(f'<div class="qr {k}"><b>{a}</b><span>{b}</span><em>{s}</em></div>' for a,b,s,k in q)}
<div class=tx>{ic("send",22)} The owner of #314 just got a text: ready for pickup until 7 PM.</div></div>''',
"#1f2a24", "Run a bike shop? DM us", "background:#d15a12;color:#fff")


# ───────── 199 INDIA · Banana ripening chamber · SINGLE · Gelasio + Inter · banana yellow / leaf green / brown
# New technique: four chamber doors each showing a banana bunch tinted by ripening day + day dots + dispatch date.
def bunch(stage):
    col = ["#5f9e3a", "#9cbc3c", "#d8cf3e", "#f5cf3a", "#f2c12e"][stage]
    edge = "#4b6b26" if stage < 2 else "#8a6a1e"
    out = '<svg viewBox="0 0 170 150" width="160" height="140" style="display:block;flex:none">'
    out += '<rect x="6" y="40" width="22" height="60" rx="8" fill="#6b4f2a"/>'
    for i in range(5):
        y = 18 + i * 22
        out += (f'<path d="M24 {y+40} C 40 {y+80}, 110 {y+86}, 160 {y+46} C 112 {y+66}, 52 {y+58}, 28 {y+30} Z" fill="{col}" stroke="{edge}" stroke-width="3" stroke-linejoin="round"/>'
                f'<circle cx="159" cy="{y+46}" r="4" fill="#3b2c17"/>')
    return out + '</svg>'
ch = [("Chamber 1", 0, "Day 1 of 5", "Gas on today", "Thu, 26 Nov"), ("Chamber 2", 2, "Day 3 of 5", "Temp 18°C", "Tue, 24 Nov"), ("Chamber 3", 4, "Day 5 of 5", "Ready to load", "Today"), ("Chamber 4", 3, "Day 4 of 5", "Temp 17°C", "Mon, 23 Nov")]
P["p199_ripening"] = page("""
body{--f:'Inter';--h:'Gelasio';background:#fff6d6;color:#3b2c17}
h1{font-family:'Gelasio';font-size:62px;font-weight:700;letter-spacing:-.5px;line-height:1.22} h1 span{color:#2f7a2c}
.sub{color:#6b5a3a;font-size:23px}
.vis{flex-direction:column;gap:16px}
.chs{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.cb{background:#3b2c17;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:10px}
.cb .hd{display:flex;justify-content:space-between;align-items:center;color:#fff}.cb .hd b{font:700 26px/1.3 Gelasio}.cb .hd em{font-style:normal;font:700 15px 'Inter';background:#5a4626;border-radius:10px;padding:4px 10px;color:#f5e2b0}
.dr{flex:1;background:repeating-linear-gradient(90deg,#d7dbe0 0 22px,#c6cbd1 22px 24px);border-radius:16px;display:flex;align-items:center;gap:12px;padding:0 16px}
.dr .info{flex:1;background:#fffdf4;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}
.info b{font:700 22px/1.3 Inter}.info span{font:500 16px 'Inter';color:#6b5a3a}
.dots{display:flex;gap:6px;margin-top:4px}.dots i{width:22px;height:8px;border-radius:4px;background:#e3dccb}.dots i.on{background:#2f7a2c}
.ds{display:flex;justify-content:space-between;color:#f5e2b0;font:600 16px 'Inter'}.ds b{color:#fff;font:700 17px 'Inter'}
.cb.rd{background:#2f7a2c}.cb.rd .hd em{background:#f5cf3a;color:#3b2c17}
.ord{background:#fffdf4;border-radius:24px;padding:16px 20px;display:flex;align-items:center;gap:16px;box-shadow:0 12px 26px rgba(59,44,23,.08)}
.ord .ib{width:58px;height:58px;border-radius:16px;background:#f5cf3a;color:#3b2c17}.ord div{flex:1}.ord b{display:block;font:700 24px/1.3 Gelasio}.ord span{font:500 18px 'Inter';color:#6b5a3a}
""", "<h1>Which chamber is ready<br><span>for tomorrow's orders?</span></h1><div class=sub>Track the ripening day, temperature and dispatch for every chamber.</div>",
f'''<div class=chs>{"".join(f'<div class="cb {"rd" if st==4 else ""}"><div class=hd><b>{n}</b><em>{dy}</em></div><div class=dr>{bunch(st)}<div class=info><b>{nt}</b><span>Sample · 120 boxes</span><div class=dots>{"".join(f"<i class={chr(34)}{chr(111)+chr(110) if i<=st else chr(120)}{chr(34)}></i>" for i in range(5))}</div></div></div><div class=ds><span>Dispatch</span><b>{dd}</b></div></div>' for n,st,dy,nt,dd in ch)}</div>
<div class=ord><span class=ib>{ic("truck",30)}</span><div><b>Tomorrow: 3 shop orders, 210 boxes</b><span>Loaded from Chamber 3 first, then Chamber 4.</span></div></div>''',
"#3b2c17", "Run a ripening chamber? DM us", "background:#2f7a2c;color:#fff")


# ───────── 200 CANADA · Winter tire swap and storage · CAROUSEL 5 · Montserrat + Fira Sans · ice blue / tire black / signal red
# New techniques: tire storage rack map (bays with stacked tire sets + customer codes), swap-day slot board, spring reminder.
WT = """
body{--f:'Fira Sans';--h:'Montserrat';background:#e6f1f8;color:#101820}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.3px;line-height:1.22} h1 span{color:#d62839}
.kk{font:700 16px 'Fira Sans';letter-spacing:3px;color:#1d6fa3;margin-top:22px}
.cd{background:#fff;border-radius:26px;box-shadow:0 14px 30px rgba(16,24,32,.08)}
.ts{display:flex;flex-direction:column;align-items:center;gap:6px}.ts b{font:700 20px 'Fira Sans';color:#fff;background:#d62839;border-radius:10px;padding:3px 12px}
"""
def wt(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#101820;color:#fff"):
    return page(WT + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#101820", cta, ctacss, tagline=f"{n} / 5")
def tset(code, col="#101820", w=110):
    t = "".join(f'<ellipse cx="55" cy="{22+i*20}" rx="50" ry="13" fill="{col}" stroke="#4b5560" stroke-width="2"/><ellipse cx="55" cy="{22+i*20}" rx="22" ry="5" fill="#4b5560"/>' for i in range(4))
    return f'<div class=ts><svg viewBox="0 0 110 100" width="{w}" style="display:block">{t}</svg><b>{code}</b></div>'
P["p200_tires_s1"] = wt(1, "TIRE SHOPS · SWAP SEASON", "First snow, and the<br>phone won't stop?<br><span>Let them book a slot.</span>",
f'''<div class=snw><div class=cnt>{"".join(f'<div><i>{ic(c,34)}</i><b>{a}</b><span>{b}</span></div>' for c,a,b in [("phone","Calls asking for a slot","All day"),("search","Where are my tires stored?","On paper"),("bell","Torque check reminder","Forgotten")])}</div>
<div class=stack>{"".join(tset(c, "#2a3440", 150) for c in ["?", "A-12?", "?", "B-03?"])}</div></div>''',
css=""".snw{flex:1;display:flex;flex-direction:column;gap:16px}
.cnt{flex:1;display:flex;flex-direction:column;gap:12px}.cnt div{flex:1;background:#fff;border-radius:22px;display:flex;align-items:center;justify-content:space-between;padding:0 26px;box-shadow:0 10px 22px rgba(16,24,32,.07);border-left:10px solid #d62839}
.cnt i{width:70px;height:70px;border-radius:18px;background:#e6f1f8;color:#1d6fa3;display:flex;align-items:center;justify-content:center;flex:none;margin-right:20px}.cnt b{flex:1;font:800 32px/1.3 Montserrat}.cnt span{font:700 23px 'Fira Sans';color:#d62839}
.stack{display:flex;justify-content:space-around;background:#101820;border-radius:24px;padding:18px 10px}
""")

days = ["Mon 23", "Tue 24", "Wed 25", "Thu 26", "Fri 27", "Sat 28"]
times = ["8 AM", "10 AM", "12 PM", "2 PM", "4 PM"]
random.seed(200)
grid = {(d, t): random.random() < .62 for d in range(6) for t in range(5)}
grid[(2, 2)] = False
P["p200_tires_s2"] = wt(2, "PART 1 · SWAP BOOKING", "Customers pick an open<br><span>swap slot online.</span>",
f'''<div class="cd sb"><div class=g6><span></span>{"".join(f'<span class=dh>{d}</span>' for d in days)}
{"".join(f'<span class=th>{t}</span>' + "".join(f'<span class="sc {"bk" if grid[(d,ti)] else "op"}{" me" if (d,ti)==(2,2) else ""}">{"This one" if (d,ti)==(2,2) else ("Booked" if grid[(d,ti)] else "Open")}</span>' for d in range(6)) for ti,t in enumerate(times))}</div>
<div class=pk><div><small>YOUR PICK</small><b>Wed, Nov 25 · 12 PM</b></div><div><small>SERVICE</small><b>Swap to winter tires</b></div><div><small>STORED SET</small><b>Bay A-12</b></div></div></div>''',
css=""".vis{display:flex}.sb{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:14px}
.g6{flex:1;display:grid;grid-template-columns:76px repeat(6,1fr);grid-template-rows:34px repeat(5,1fr);gap:7px}
.dh{font:700 17px 'Fira Sans';text-align:center;align-self:center}.th{font:700 17px 'Fira Sans';color:#5d6b78;align-self:center}
.sc{border-radius:12px;display:flex;align-items:center;justify-content:center;font:600 16px 'Fira Sans'}
.sc.bk{background:#dce6ee;color:#7b8a97}.sc.op{background:#fff;border:2px dashed #1d6fa3;color:#1d6fa3}.sc.me{background:#d62839;color:#fff;border:none;font-weight:700}
.pk{display:flex;gap:12px}.pk div{flex:1;background:#101820;color:#fff;border-radius:16px;padding:12px 16px}.pk small{display:block;font:700 13px 'Fira Sans';letter-spacing:2px;color:#9cc3dd}.pk b{font:700 21px/1.3 Montserrat}""")

bays = [("A-10", 1), ("A-11", 1), ("A-12", 2), ("A-13", 0), ("B-01", 1), ("B-02", 0), ("B-03", 1), ("B-04", 1)]
P["p200_tires_s3"] = wt(3, "PART 2 · STORAGE RACKS", "Every stored set has<br><span>a bay and a code.</span>",
f'''<div class="cd rk"><div class=rows>{"".join(f'<div class="by k{k}"><span>{b}</span>{tset("", "#101820" if k else "#e6edf2", 165).replace("<b></b>","")}<em>{["Empty","Stored","Out Wed"][k]}</em></div>' for b,k in bays)}</div>
<div class=sd><div><small>BAY A-12 · SAMPLE CUSTOMER</small><b>4 winter tires on rims</b><span>Size 215/60 R16 · tread checked in spring</span></div><i>Out for the swap on Wed</i></div></div>''',
css=""".vis{display:flex}.rk{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:14px}
.rows{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:12px;background:repeating-linear-gradient(#e6f1f8 0 49%,#5d6b78 49% 51%,#e6f1f8 51% 100%);border-radius:18px;padding:12px}
.by{background:#fff;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;border:3px solid #dce6ee}
.by span{font:800 26px Montserrat}.by em{font-style:normal;font:700 19px 'Fira Sans';color:#5d6b78}
.by.k2{border-color:#d62839}.by.k2 em{color:#d62839}.by.k0 em{color:#9aa8b4}
.sd{display:flex;align-items:center;gap:16px;background:#101820;color:#fff;border-radius:20px;padding:16px 20px}.sd div{flex:1}.sd small{display:block;font:700 13px 'Fira Sans';letter-spacing:2px;color:#9cc3dd}.sd b{display:block;font:800 26px/1.3 Montserrat}.sd span{font:500 18px 'Fira Sans';color:#c9d6e0}
.sd i{font-style:normal;background:#d62839;border-radius:14px;padding:10px 14px;font:700 17px 'Fira Sans';text-align:center;width:170px}""")

P["p200_tires_s4"] = wt(4, "PART 3 · AUTOMATIC TEXTS", "The follow-ups<br><span>send themselves.</span>",
f'''<div class=tx>{"".join(f'<div class="mg {c}"><small>{w}</small><b>{a}</b><span>{b}</span></div>' for w,a,b,c in [("WED, NOV 25 · AFTER THE SWAP","Winter tires are on.","Summer set stored in Bay A-12. Come back after 100 km for a torque check.","a"),("MON, NOV 30","Torque check reminder","Drop by any weekday, no booking needed.","b"),("SPRING · SAMPLE","Time to swap back?","Book your summer tire slot online.","c")])}</div>''',
css=""".tx{flex:1;display:flex;flex-direction:column;gap:14px}
.mg{flex:1;border-radius:26px;padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px;max-width:86%}
.mg small{font:700 15px 'Fira Sans';letter-spacing:2.5px}.mg b{font:800 42px/1.25 Montserrat}.mg span{font:500 25px/1.4 'Fira Sans';text-wrap:balance}
.mg.a{background:#101820;color:#fff}.mg.a small{color:#9cc3dd}.mg.b{background:#fff;align-self:flex-end;box-shadow:0 10px 22px rgba(16,24,32,.07)}.mg.b small{color:#1d6fa3}.mg.c{background:#d62839;color:#fff}.mg.c small{color:#ffd0d4}""")

P["p200_tires_s5"] = wt(5, "YOUR TURN", "Run a tire or auto shop?<br><span>Let's build your swap app.</span>",
f'''<div class=c5><div class=rowt>{"".join(tset(c, "#101820", 150) for c in ["A-10","A-12","B-03","B-04"])}</div>
<div class=g4>{"".join(f'<div><i>{ic(c,64,w=1.8)}</i><b>{a}</b><span>{b}</span></div>' for c,a,b in [("cal","Slot booking","Open slots online"),("grid","Storage map","Bay for every set"),("send","Auto texts","Torque check, spring swap"),("users","Customer list","Sizes and history")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#d62839;color:#fff",
css=""".c5{flex:1;display:flex;flex-direction:column;gap:16px}.rowt{display:flex;justify-content:space-around;background:#fff;border-radius:24px;padding:20px 10px}
.g4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}.g4 div{background:#101820;color:#fff;border-radius:24px;padding:24px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}
.g4 div:nth-child(2),.g4 div:nth-child(3){background:#1d6fa3}.g4 i{margin-bottom:auto;color:#9cc3dd}.g4 b{font:800 38px/1.25 Montserrat}.g4 span{font:500 20px 'Fira Sans';color:#d5e6f1}""")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
