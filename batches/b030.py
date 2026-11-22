import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 166 INDIA · Bike / scooter rental (tourist town) · CAROUSEL 5 · Montserrat + Inter · deep teal / sunset orange / sand
# New techniques: top-down scooter SVG with numbered damage marks, receipt-roll return timeline, pickup checklist as a paper slip.
BR = """
body{--f:'Inter';--h:'Montserrat';background:#f4ead8;color:#0f3d3e}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.4px;line-height:1.2} h1 span{color:#e8692c}
.kk{font:700 16px Inter;letter-spacing:3px;color:#e8692c;margin-top:22px}
.cd{background:#fff;border-radius:26px;box-shadow:0 14px 30px rgba(15,61,62,.08)}
"""
def br(n, head, vis, css="", cta="Swipe", ctacss="background:#0f3d3e;color:#fff"):
    return page(BR + css, head, vis, "#0f3d3e", cta, ctacss, tagline=f"{n} / 5")
def scooter(w=300, marks=False, c="#e8692c"):
    m = ""
    if marks:
        for i, (x, y) in enumerate([(70, 70), (128, 270), (60, 420)], 1):
            m += f'<g><circle cx="{x}" cy="{y}" r="22" fill="#0f3d3e"/><text x="{x}" y="{y+8}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="22" fill="#fff"><tspan>{i}</tspan></text></g>'
    return (f'<svg viewBox="0 0 200 500" width="{w}" style="display:block">'
            '<rect x="80" y="10" width="40" height="70" rx="16" fill="#22292b"/><rect x="80" y="420" width="40" height="70" rx="16" fill="#22292b"/>'
            '<path d="M20 92 L180 92" stroke="#3b4547" stroke-width="12" stroke-linecap="round"/>'
            f'<path d="M64 70 Q100 50 136 70 L150 160 Q160 260 150 360 Q140 450 100 460 Q60 450 50 360 Q40 260 50 160 Z" fill="{c}"/>'
            '<rect x="70" y="190" width="60" height="150" rx="26" fill="#22292b"/><rect x="82" y="104" width="36" height="40" rx="8" fill="#cfe3e3"/>'
            f'{m}</svg>')
fleet = [("S-01", "free"), ("S-02", "out"), ("S-03", "out"), ("S-04", "late"), ("S-05", "free"), ("S-06", "out"), ("S-07", "out"), ("S-08", "svc")]
FL = {"free": ("#ffffff", "Free"), "out": ("#e8692c", "Out"), "late": ("#b3261e", "Late"), "svc": ("#9fb3b3", "Service")}
P["p166_bike_s1"] = br(1, "<div class=kk>BIKE AND SCOOTER RENTAL</div><h1>Scooters out all day.<br><span>Which come back by 6 PM?</span></h1>",
f'''<div class="cd yd"><div class=yh><b>Today's fleet · sample</b><span>Sat, 28 Nov</span></div><div class=rw>{"".join(f'<div class=sl><div class=sv style="background:{FL[k][0]}">{scooter(72, c=("#0f3d3e" if k=="free" else "#ffffff"))}</div><b>{n}</b><em class={k}>{FL[k][1]}</em></div>' for n,k in fleet)}</div></div>
<div class=st>{"".join(f'<div class={k}><b>{a}</b><span>{b}</span></div>' for a,b,k in [("5","out now","o"),("4","due by 6 PM","d"),("1","running late","l"),("2","free to rent","f")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.yd{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:14px}
.yh{display:flex;justify-content:space-between;align-items:baseline}.yh b{font:800 28px Montserrat}.yh span{font:600 19px Inter;color:#6a7f7f}
.rw{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.sl{background:#f6f1e7;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;padding:10px}
.sv{border-radius:16px;padding:6px 18px;border:2px solid #e2d6c1}.sl b{font:800 22px Montserrat}
.sl em{font-style:normal;font:700 16px Inter;border-radius:10px;padding:4px 12px}.sl .free{background:#dff0e8;color:#1c6b4a}.sl .out{background:#fde2d3;color:#a3441a}.sl .late{background:#b3261e;color:#fff}.sl .svc{background:#e3eaea;color:#4d6363}
.st{display:flex;gap:12px}.st div{flex:1;border-radius:20px;padding:16px 18px;background:#fff}.st b{display:block;font:800 46px/1.25 Montserrat}.st span{font:600 18px Inter}
.st .o{background:#0f3d3e;color:#fff}.st .l b{color:#b3261e}.st .d b{color:#e8692c}""")

chk = [("Driving licence checked", 1), ("ID copy saved", 1), ("Photo of scooter, 4 sides", 1), ("Fuel level: half tank", 1), ("Helmets given: 2", 1), ("Return time agreed: 6 PM", 1)]
P["p166_bike_s2"] = br(2, "<div class=kk>PART 1 · PICKUP</div><h1>Hand over the keys<br><span>after a 6-point check.</span></h1>",
f'''<div class=slp><div class=sh><small>PICKUP SLIP · SAMPLE</small><b>S-03 · Rider: Sample Guest</b><span>Sat, 28 Nov · 9:10 AM</span></div>
{"".join(f'<div class=ck><i>{ic("check",24,w=3)}</i><span>{a}</span></div>' for a,_ in chk)}
<div class=sg2><span>Rider sign-off</span><svg viewBox="0 0 300 60" width="240" style="display:block"><path d="M10 42 C40 12 70 52 100 30 S150 14 170 40 S230 46 290 18" fill="none" stroke="#0f3d3e" stroke-width="4" stroke-linecap="round"/></svg></div></div>
<div class=sd>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("No paper files","Everything saved with the booking"),("Same check","for every rider, every time"),("Proof on return","photos match at drop-off")])}</div>''',
css=""".vis{gap:18px}.slp{flex:1;background:#fffdf7;border-radius:10px;padding:24px 26px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 30px rgba(15,61,62,.10);border-top:10px dashed #e2d6c1}
.sh small{display:block;font:700 14px Inter;letter-spacing:2.5px;color:#8a9a9a}.sh b{display:block;font:800 28px/1.3 Montserrat}.sh span{font:600 19px Inter;color:#6a7f7f}
.ck{flex:1;display:flex;align-items:center;gap:16px;border-bottom:2px dotted #e2d6c1;font:600 24px Inter}.ck i{width:42px;height:42px;border-radius:12px;background:#0f3d3e;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.sg2{display:flex;justify-content:space-between;align-items:center;font:600 18px Inter;color:#6a7f7f}
.sd{width:300px;flex:none;display:flex;flex-direction:column;gap:14px}.sd div{flex:1;background:#0f3d3e;color:#fff;border-radius:22px;padding:20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.sd b{font:800 28px/1.25 Montserrat;color:#ffb48a}.sd span{font:500 19px/1.4 Inter}""")

rets = [("2:00 PM", "S-07", "Back · checked", "ok"), ("3:30 PM", "S-02", "Back · checked", "ok"), ("4:00 PM", "S-04", "Late · reminder sent", "late"),
        ("5:00 PM", "S-06", "Due · on the way", "due"), ("6:00 PM", "S-03", "Due", "due")]
P["p166_bike_s3"] = br(3, "<div class=kk>PART 2 · RETURNS</div><h1>Every return time<br><span>on one roll.</span></h1>",
f'''<div class=roll><div class=cap2></div><div class=rp><small>RETURNS TODAY · SAMPLE</small>{"".join(f'<div class="rr {k}"><b>{t}</b><span class=id>{s}</span><em>{x}</em></div>' for t,s,x,k in rets)}<div class=zz></div></div></div>
<div class=sd3><div class=bl><b>S-04 is late</b><span>The rider got a reminder at 4:15 PM. Late fee rules are shown at pickup.</span></div><div class=nx3><small>NEXT FREE</small><b>S-07 · S-02</b><span>ready to rent again</span></div></div>''',
css=""".vis{gap:18px}.roll{flex:1;display:flex;flex-direction:column;align-items:stretch}
.cap2{height:36px;border-radius:18px;background:linear-gradient(#0f3d3e,#1d5a5b);margin:0 -10px}
.rp{flex:1;background:#fffdf7;margin:0 12px;padding:16px 22px 26px;display:flex;flex-direction:column;gap:6px;box-shadow:0 16px 30px rgba(15,61,62,.10);position:relative}
.rp small{font:700 14px Inter;letter-spacing:2.5px;color:#8a9a9a;text-align:center;margin-bottom:4px}
.rr{flex:1;display:flex;align-items:center;gap:14px;border-bottom:2px dashed #e2d6c1;font-family:Inter}.rr b{font:800 24px Montserrat;width:130px}.rr .id{font:700 22px Inter;width:76px}
.rr em{font-style:normal;font:700 18px Inter;border-radius:10px;padding:6px 12px}.rr.ok em{background:#dff0e8;color:#1c6b4a}.rr.late em{background:#b3261e;color:#fff}.rr.due em{background:#fde2d3;color:#a3441a}
.zz{position:absolute;left:0;right:0;bottom:0;height:14px;background:linear-gradient(135deg,#f4ead8 50%,transparent 50%) 0 0/20px 14px,linear-gradient(225deg,#f4ead8 50%,transparent 50%) 0 0/20px 14px}
.sd3{width:320px;flex:none;display:flex;flex-direction:column;gap:14px}.sd3>div{flex:1;border-radius:24px;padding:22px;display:flex;flex-direction:column;justify-content:center;gap:8px}
.bl{background:#b3261e;color:#fff}.bl b{font:800 32px/1.25 Montserrat}.bl span{font:500 20px/1.45 Inter}
.nx3{background:#0f3d3e;color:#fff}.nx3 small{font:700 14px Inter;letter-spacing:2.5px;color:#9fc7c7}.nx3 b{font:800 36px/1.25 Montserrat;color:#ffb48a}.nx3 span{font:500 20px Inter}""")

marks = [("1", "Scratch on left mirror", "At pickup", "pk"), ("2", "Seat cover torn", "At pickup", "pk"), ("3", "New dent, rear mudguard", "At return", "nw")]
P["p166_bike_s4"] = br(4, "<div class=kk>PART 3 · DAMAGE CHECK</div><h1>Old scratch or new dent?<br><span>The photos settle it.</span></h1>",
f'''<div class="cd tv"><small>S-03 · TOP VIEW · SAMPLE</small>{scooter(250, True)}</div>
<div class=ml>{"".join(f'<div class="mk {k}"><i>{n}</i><div><b>{a}</b><span>{w}</span></div></div>' for n,a,w,k in marks)}
<div class=nt4>Marks from pickup are saved with photos, so only <b>new</b> damage is talked about at return.</div></div>''',
css=""".vis{gap:18px}.tv{width:360px;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:22px}
.tv small{font:700 14px Inter;letter-spacing:2.5px;color:#8a9a9a}
.ml{flex:1;display:flex;flex-direction:column;gap:14px}.mk{flex:1;background:#fff;border-radius:22px;display:flex;align-items:center;gap:18px;padding:0 22px;box-shadow:0 14px 30px rgba(15,61,62,.08)}
.mk i{width:58px;height:58px;border-radius:50%;background:#0f3d3e;color:#fff;font:800 26px Montserrat;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.mk b{display:block;font:700 30px/1.3 Inter}.mk span{display:inline-block;margin-top:6px;font:700 17px Inter;border-radius:10px;padding:5px 12px;background:#e3eaea;color:#4d6363}.mk.nw span{background:#b3261e;color:#fff}.mk.nw{box-shadow:0 0 0 3px #b3261e}
.nt4{background:#0f3d3e;color:#fff;border-radius:22px;padding:20px 22px;font:500 21px/1.45 Inter}.nt4 b{color:#ffb48a}""")

P["p166_bike_s5"] = br(5, "<div class=kk>YOUR TURN</div><h1>Rent bikes or scooters?<br><span>Let's build your rental app.</span></h1>",
f'''<div class="cd hr5">{"".join(f'<div class=sv5>{scooter(120, c=c)}</div>' for c in ["#e8692c","#0f3d3e","#e8692c","#0f3d3e"])}</div>
<div class=rw5>{"".join(f'<div><span class=ib>{ic(i,28)}</span><b>{a}</b></div>' for i,a in [("grid","Fleet board"),("doc","Pickup check"),("clock","Return times"),("camera","Damage photos")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.hr5{flex:1;display:flex;align-items:center;justify-content:space-around;padding:24px}
.sv5{background:#f6f1e7;border-radius:24px;padding:20px 28px}
.rw5{display:grid;grid-template-columns:1fr 1fr;gap:14px}.rw5 div{background:#0f3d3e;color:#fff;border-radius:22px;padding:26px 22px;display:flex;align-items:center;gap:16px}
.rw5 .ib{width:58px;height:58px;border-radius:16px;background:#e8692c;color:#fff}.rw5 b{font:800 27px Montserrat}""",
cta="DM us to start", ctacss="background:#e8692c;color:#fff")


# ───────── 167 USA · Window cleaning · SINGLE · Bitter + Roboto · cornflower / lemon / white
# New technique: a big window SVG whose panes are the five route days (clean panes = done, streaked panes = to do) + recurring-client cycle chips.
days = [("MON", "North side", "9 stops", "done"), ("TUE", "Downtown", "6 stops", "done"), ("WED", "Lakeview", "8 stops", "today"),
        ("THU", "West hills", "7 stops", "todo"), ("FRI", "Storefronts", "11 stops", "todo"), ("SAT", "Make-up day", "Open", "open")]
P["p167_window"] = page("""
body{--f:'Roboto';--h:'Bitter';background:#e4ecfb;color:#1d2b4f}
h1{font-family:'Bitter';font-size:62px;font-weight:800;letter-spacing:-.8px;line-height:1.2} h1 span{color:#3f63d6}
.sub{color:#4d5b7c;font-size:23px}
.vis{flex-direction:column;gap:16px}
.fr{flex:1;background:#fff;border-radius:22px;padding:18px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:14px;box-shadow:0 0 0 10px #c9d6f2,0 26px 50px rgba(29,43,79,.14)}
.pn{border-radius:10px;padding:16px 18px;display:flex;flex-direction:column;justify-content:space-between;position:relative;overflow:hidden}
.pn.done{background:linear-gradient(140deg,#d9ecff 0%,#f4faff 45%,#d9ecff 46%,#eef6ff 100%)}
.pn.today{background:#3f63d6;color:#fff}
.pn.todo{background:repeating-linear-gradient(115deg,#d8dbe3 0 14px,#cdd1db 14px 18px)}
.pn.open{background:#fff8c6;border:3px dashed #e0c84a}
.pn small{font:700 18px Roboto;letter-spacing:3px;opacity:.75}.pn b{font:800 38px/1.2 Bitter}.pn span{font:600 24px Roboto}
.pn em{align-self:flex-start;font-style:normal;font:700 16px Roboto;border-radius:10px;padding:5px 12px;background:rgba(29,43,79,.10)}.pn.today em{background:#ffe45c;color:#1d2b4f}
.cy{display:flex;gap:12px}
.cy div{flex:1;background:#1d2b4f;color:#fff;border-radius:20px;padding:16px 18px;display:flex;flex-direction:column;gap:4px}
.cy small{font:700 14px Roboto;letter-spacing:2px;color:#a9b8e3}.cy b{font:800 26px/1.25 Bitter;color:#ffe45c}.cy span{font:500 18px Roboto}
""", "<h1>Same homes every few weeks?<br><span>Let the route plan itself.</span></h1><div class=sub>Recurring clients fill the right day, by area, on their own.</div>",
f'''<div class=fr>{"".join(f'<div class="pn {k}"><small>{d}</small><div><b>{a}</b><br><span>{s}</span></div><em>{dict(done="Done",today="Today",todo="To do",open="Rain or extra jobs")[k]}</em></div>' for d,a,s,k in days)}</div>
<div class=cy>{"".join(f'<div><small>{a}</small><b>{b}</b><span>{c}</span></div>' for a,b,c in [("EVERY 4 WEEKS","18 storefronts","added to Fridays"),("EVERY 8 WEEKS","22 homes","spread by area"),("TWICE A YEAR","30 homes","reminder sent first")])}</div>''',
"#1d2b4f", "Clean windows? DM us", "background:#3f63d6;color:#fff")


# ───────── 168 INDIA · Electrical goods shop · SINGLE · Anton + Open Sans · electric yellow / charcoal / paper
# New technique: counter slips as a curling receipt roll that feeds into contractor account cards (by site), no amounts shown.
slips = [("10:05", "Contractor A", "Site: Sample Tower", "Wire 1.5 sq mm × 6 coils"), ("11:40", "Contractor B", "Site: Sample Villa 3", "MCB 32 A × 8"),
         ("1:15", "Contractor A", "Site: Sample Tower", "Modular switches × 40"), ("4:30", "Contractor C", "Site: Sample Shop 12", "LED panels × 12")]
accs = [("Contractor A", "Sample Tower", "14 slips this month", "Bill on 30 Nov", "bl"), ("Contractor B", "Sample Villa 3", "6 slips this month", "Bill on 30 Nov", "bl"),
        ("Contractor C", "Sample Shop 12", "9 slips this month", "Reminder sent", "rm")]
P["p168_elec"] = page("""
body{--f:'Open Sans';--h:'Anton';background:#f6f3ea;color:#24262b}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.3px;line-height:1.22;margin-top:30px} h1 span{background:#ffd60a;padding:0 10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sub{color:#5b5e66;font-size:23px}
.vis{gap:20px}
.rl{width:430px;flex:none;display:flex;flex-direction:column}
.rl .top{height:40px;border-radius:20px;background:linear-gradient(#3a3d44,#24262b)}
.rl .pp{flex:1;background:#fffef9;margin:0 14px;padding:14px 20px 24px;display:flex;flex-direction:column;gap:8px;box-shadow:0 16px 30px rgba(36,38,43,.10);position:relative}
.rl small.t{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#9a9890;text-align:center}
.sp{flex:1;border-bottom:2px dashed #ddd8c8;display:flex;flex-direction:column;justify-content:center;gap:2px}
.sp .h{display:flex;justify-content:space-between;font:700 17px 'Open Sans';color:#9a9890}.sp b{font:700 22px 'Open Sans'}.sp span{font:500 19px 'Open Sans'}
.sp .h em{font-style:normal;color:#24262b;background:#ffd60a;border-radius:8px;padding:0 8px}
.zz{position:absolute;left:0;right:0;bottom:0;height:14px;background:linear-gradient(135deg,#f6f3ea 50%,transparent 50%) 0 0/20px 14px,linear-gradient(225deg,#f6f3ea 50%,transparent 50%) 0 0/20px 14px}
.ac{flex:1;display:flex;flex-direction:column;gap:14px}
.ah{font:400 32px/1.35 Anton}
.cc{flex:1;background:#24262b;color:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.cc b{font:400 32px/1.35 Anton;color:#ffd60a}.cc span{font:600 20px 'Open Sans'}.cc .rw{display:flex;justify-content:space-between;align-items:center;margin-top:4px}
.cc small{font:500 18px 'Open Sans';color:#c5c7cc}.cc em{font-style:normal;font:700 16px 'Open Sans';border-radius:10px;padding:5px 12px}.cc .bl{background:#3a3d44}.cc .rm{background:#ffd60a;color:#24262b}
""", "<h1>Who took the wire,<br><span>for which site?</span></h1><div class=sub>Every counter slip goes into the right contractor's account.</div>",
f'''<div class=rl><div class=top></div><div class=pp><small class=t>TODAY'S COUNTER SLIPS · SAMPLE</small>{"".join(f'<div class=sp><div class=h><span>{t}</span><em>{c}</em></div><b>{i}</b><span>{s}</span></div>' for t,c,s,i in slips)}<div class=zz></div></div></div>
<div class=ac><div class=ah>CONTRACTOR ACCOUNTS</div>{"".join(f'<div class=cc><b>{a}</b><span>{s}</span><div class=rw><small>{n}</small><em class={k}>{x}</em></div></div>' for a,s,n,x,k in accs)}</div>''',
"#24262b", "Run an electrical shop? DM us", "background:#24262b;color:#ffd60a")


# ───────── 169 USA · Home organizer · CAROUSEL 5 · Crimson Text + Poppins · blush / olive / cream
# New techniques: SVG closet with labelled bins (zones), session plan as a vertical stepper, bin shopping list with size swatches.
OR = """
body{--f:'Poppins';--h:'Crimson Text';background:#f8efe9;color:#3a3a24}
h1{font-family:'Crimson Text';font-weight:700;font-size:66px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#6f7a35;font-style:italic}
.kk{font:600 16px Poppins;letter-spacing:3px;color:#c46d6d;margin-top:22px}
.cd{background:#fff;border-radius:26px;box-shadow:0 14px 30px rgba(58,58,36,.08)}
"""
def org(n, head, vis, css="", cta="Swipe", ctacss="background:#6f7a35;color:#fff"):
    return page(OR + css, head, vis, "#3a3a24", cta, ctacss, tagline=f"{n} / 5")
bins = [("Scarves", "#e9b8b0"), ("Belts", "#d4d9b0"), ("Bags", "#e9b8b0"), ("Winter", "#d4d9b0"), ("Gym wear", "#e9b8b0"), ("Spare sheets", "#d4d9b0")]
def closet(w=560):
    s = f'<svg viewBox="0 0 560 600" width="{w}" style="display:block"><rect x="10" y="10" width="540" height="580" rx="18" fill="#efe3d6" stroke="#3a3a24" stroke-width="5"/>'
    s += '<path d="M40 70 L520 70" stroke="#6f7a35" stroke-width="8" stroke-linecap="round"/>'
    for i, c in enumerate(["#c46d6d", "#6f7a35", "#e9b8b0", "#3a3a24", "#d4d9b0", "#c46d6d", "#6f7a35"]):
        x = 70 + i * 62
        s += f'<path d="M{x} 70 L{x} 84" stroke="#3a3a24" stroke-width="3"/><path d="M{x-24} 90 L{x+24} 90 L{x+28} 230 L{x-28} 230 Z" fill="{c}"/>'
    s += '<rect x="30" y="262" width="500" height="10" fill="#3a3a24"/><rect x="30" y="422" width="500" height="10" fill="#3a3a24"/>'
    for i, (n, c) in enumerate(bins):
        x = 44 + (i % 3) * 164; y = 286 if i < 3 else 446
        s += f'<rect x="{x}" y="{y}" width="146" height="120" rx="12" fill="{c}" stroke="#3a3a24" stroke-width="3"/><rect x="{x+18}" y="{y+40}" width="110" height="40" rx="6" fill="#fff"/><text x="{x+73}" y="{y+68}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="19" fill="#3a3a24"><tspan>{n}</tspan></text>'
    return s + '</svg>'
P["p169_org_s1"] = org(1, "<div class=kk>HOME ORGANIZERS</div><h1>Clients ask, “What will<br>you do in my closet?”<br><span>Show them the plan.</span></h1>",
f'''<div class="cd hc"><small class=cl1>CLOSET PLAN · SAMPLE CLIENT</small>{closet(520)}<div class=cl2>Hanging by colour on top, 6 labelled bins below</div></div><div class=sd1>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("3","sessions planned"),("6","labelled bins"),("24","before and after photos")])}</div>''',
css=""".vis{gap:18px}.hc{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:22px}.cl1{font:600 14px Poppins;letter-spacing:2.5px;color:#9a8f7e}.cl2{font:500 20px/1.4 Poppins;text-align:center;background:#f8efe9;border-radius:14px;padding:10px 16px}
.sd1{width:280px;flex:none;display:flex;flex-direction:column;gap:14px}.sd1 div{flex:1;background:#6f7a35;color:#fff;border-radius:24px;padding:20px;display:flex;flex-direction:column;justify-content:center}
.sd1 div:nth-child(2){background:#c46d6d}.sd1 div:nth-child(3){background:#3a3a24}.sd1 b{font:700 72px/1.35 'Crimson Text';margin-bottom:6px}.sd1 span{font:500 20px/1.35 Poppins}""")

P["p169_org_s2"] = org(2, "<div class=kk>PART 1 · BOOKING</div><h1>A booking form<br><span>that asks the right things.</span></h1>",
browser(f'''<div class=fm2><b class=t>Book a home organizing session</b>
<div class=fl2><small>WHICH SPACES?</small><div class=ch>{"".join(f'<i class="{"on" if o else ""}">{a}</i>' for a,o in [("Closet",1),("Kitchen",1),("Garage",0),("Laundry",0),("Home office",1),("Pantry",0)])}</div></div>
<div class=r3><div class=fl2><small>HOW BIG?</small><span>Walk-in closet</span></div><div class=fl2><small>PHOTOS</small><span>6 added</span></div></div>
<div class=fl2><small>WHAT BOTHERS YOU MOST?</small><span class=q>“I can't find anything in the morning.”</span></div>
<div class=fl2><small>FIRST SESSION</small><div class=ch>{"".join(f'<i class="{"on" if o else ""}">{a}</i>' for a,o in [("Sat, Dec 5 · 9 AM",1),("Sun, Dec 6 · 1 PM",0),("Tue, Dec 8 · 10 AM",0)])}</div></div>
<div class=bt2>Send my request</div></div>''', url="yourorganizing.com/book · sample", style="flex:1"),
css=""".vis{display:flex}.fm2{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:12px}
.fm2 .t{font:700 36px 'Crimson Text'}
.fl2{flex:1;background:#f8f3ee;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:6px}.fl2 small{font:600 13px Poppins;letter-spacing:2px;color:#9a8f7e}.fl2 span{font:600 23px Poppins}.fl2 .q{font:italic 600 26px 'Crimson Text'}
.ch{display:flex;flex-wrap:wrap;gap:8px}.ch i{font-style:normal;font:600 20px Poppins;background:#fff;border:2px solid #e6dccf;border-radius:30px;padding:7px 16px}.ch .on{background:#6f7a35;border-color:#6f7a35;color:#fff}
.r3{display:flex;gap:12px}.r3 .fl2{flex:1}
.bt2{background:#c46d6d;color:#fff;border-radius:16px;padding:16px;text-align:center;font:600 21px Poppins}""")

steps = [("Session 1 · Sat, Dec 5", "Closet: sort, donate pile, measure shelves", "done"), ("Session 2 · Sat, Dec 12", "Closet: bins in, labels on, hang by colour", "now"),
         ("Session 3 · Sat, Dec 19", "Kitchen and home office drawers", "next"), ("Follow-up · in 6 weeks", "Quick reset visit, 1 hour", "next")]
P["p169_org_s3"] = org(3, "<div class=kk>PART 2 · PROJECT PLAN</div><h1>Every session,<br><span>planned and ticked off.</span></h1>",
f'''<div class="cd sp3">{"".join(f'<div class="st3 {k}"><i>{ic("check",22,w=3) if k=="done" else ""}</i><div><b>{a}</b><span>{b}</span><em>{dict(done="Done · 8 photos",now="Next · this Saturday",next="Planned")[k]}</em></div></div>' for a,b,k in steps)}</div>''',
css=""".vis{display:flex}.sp3{flex:1;padding:26px 30px;display:flex;flex-direction:column}
.st3{flex:1;display:flex;gap:22px;position:relative}.st3:not(:last-child):before{content:'';position:absolute;left:23px;top:50px;bottom:0;width:4px;background:#e6dccf}
.st3 i{width:50px;height:50px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;border:4px solid #6f7a35;background:#fff;color:#fff}
.st3.done i{background:#6f7a35}.st3.now i{border-color:#c46d6d;background:#fbe3e3}
.st3 b{display:block;font:700 34px/1.2 'Crimson Text'}.st3 span{display:block;font:500 23px/1.4 Poppins;margin-top:2px}
.st3 em{display:inline-block;margin-top:8px;font-style:normal;font:600 16px Poppins;border-radius:10px;padding:4px 12px;background:#efe9df}.st3.done em{background:#e4e8cc;color:#4e5624}.st3.now em{background:#c46d6d;color:#fff}""")

shop = [("Clear shoe boxes", "Small · 13 × 8 in", 12, 60), ("Fabric bins", "Medium · 11 × 11 in", 6, 90), ("Drawer dividers", "Adjustable", 8, 46), ("Velvet hangers", "Slim", 60, 30)]
P["p169_org_s4"] = org(4, "<div class=kk>PART 3 · SHOPPING LIST</div><h1>Measured once.<br><span>The right bins, the first time.</span></h1>",
f'''<div class="cd sl4"><div class=hd4><b>Closet shopping list</b><span>From session 1 measurements · sample</span></div>{"".join(f'<div class=it4><div class=swb><div class=sw style="width:{w}px;height:{w}px"></div></div><div class=tx4><b>{a}</b><span>{s}</span></div><em>× {q}</em></div>' for a,s,q,w in shop)}
<div class=ft4>{ic("check",22,w=3)}<span>Client approves the list, then you shop or they do.</span></div></div>''',
css=""".vis{display:flex}.sl4{flex:1;padding:24px 28px;display:flex;flex-direction:column;gap:10px}
.hd4 b{display:block;font:700 38px/1.2 'Crimson Text'}.hd4 span{font:500 19px Poppins;color:#9a8f7e}
.it4{flex:1;display:flex;align-items:center;gap:20px;border-bottom:2px solid #f1e9de}
.sw{flex:none;border-radius:12px;background:#e9b8b0;border:3px solid #3a3a24}
.swb{width:96px;flex:none;display:flex;align-items:center;justify-content:center}.it4:nth-child(odd) .sw{background:#d4d9b0}.tx4{flex:1;padding-left:10px}.tx4 b{display:block;font:600 26px Poppins}.tx4 span{font:500 19px Poppins;color:#7a7360}
.it4 em{font-style:normal;font:700 40px 'Crimson Text';color:#6f7a35}
.ft4{background:#6f7a35;color:#fff;border-radius:18px;padding:16px 20px;display:flex;gap:12px;align-items:center;font:500 20px Poppins}""")

P["p169_org_s5"] = org(5, "<div class=kk>YOUR TURN</div><h1>Organize homes?<br><span>Let's build your booking site.</span></h1>",
f'''<div class="cd hc5">{closet(540)}</div><div class=g5>{"".join(f'<div><span class=ib>{ic(i,28)}</span><b>{a}</b></div>' for i,a in [("doc","Booking form"),("cal","Session plan"),("box","Shopping list"),("camera","Photo gallery")])}</div>''',
css=""".vis{gap:18px}.hc5{flex:1;display:flex;align-items:center;justify-content:center;padding:20px}
.g5{width:300px;flex:none;display:flex;flex-direction:column;gap:14px}.g5 div{flex:1;background:#3a3a24;color:#fff;border-radius:22px;padding:18px 22px;display:flex;align-items:center;gap:14px}
.g5 .ib{width:54px;height:54px;border-radius:16px;background:#e9b8b0;color:#3a3a24}.g5 b{font:600 23px/1.3 Poppins}""",
cta="DM us to start", ctacss="background:#c46d6d;color:#fff")


# ───────── 170 INDIA · Mobile accessories wholesaler · SINGLE · Fira Sans + Roboto · deep purple / mint / white
# New technique: tablet (landscape-ish frame) dealer catalogue with SVG product drawings and stock level dots + order cart strip.
def prod(kind):
    d = {"case": '<rect x="30" y="10" width="60" height="100" rx="14" fill="#4b2a8c"/><circle cx="48" cy="30" r="9" fill="#cfc2ec"/><circle cx="48" cy="52" r="9" fill="#cfc2ec"/>',
         "charger": '<rect x="34" y="30" width="52" height="64" rx="10" fill="#ffffff" stroke="#4b2a8c" stroke-width="5"/><path d="M50 30 V12 M70 30 V12" stroke="#4b2a8c" stroke-width="6" stroke-linecap="round"/><path d="M62 48 L54 64 H66 L58 80" fill="none" stroke="#2bbf8a" stroke-width="5" stroke-linejoin="round"/>',
         "cable": '<path d="M30 30 Q30 100 60 90 Q95 80 90 30" fill="none" stroke="#4b2a8c" stroke-width="7" stroke-linecap="round"/><rect x="22" y="12" width="16" height="24" rx="4" fill="#4b2a8c"/><rect x="82" y="12" width="16" height="24" rx="4" fill="#4b2a8c"/>',
         "guard": '<rect x="28" y="10" width="64" height="100" rx="12" fill="#e7fbf3" stroke="#4b2a8c" stroke-width="4"/><path d="M40 30 L80 70 M40 50 L70 80" stroke="#2bbf8a" stroke-width="4" stroke-linecap="round"/>',
         "buds": '<rect x="26" y="40" width="68" height="50" rx="24" fill="#ffffff" stroke="#4b2a8c" stroke-width="5"/><path d="M26 62 H94" stroke="#4b2a8c" stroke-width="3"/><circle cx="60" cy="74" r="4" fill="#2bbf8a"/>',
         "holder": '<path d="M60 100 V60" stroke="#4b2a8c" stroke-width="8" stroke-linecap="round"/><rect x="30" y="18" width="60" height="44" rx="10" fill="#4b2a8c"/><rect x="40" y="96" width="40" height="10" rx="5" fill="#4b2a8c"/>'}[kind]
    return f'<svg viewBox="0 0 120 120" width="124" style="display:block">{d}</svg>'
cat = [("case", "Back covers", "Mixed models", "In stock", "hi"), ("charger", "Fast chargers", "Pack of 10", "In stock", "hi"), ("cable", "Type-C cables", "1 m · pack of 20", "Low · 6 packs", "lo"),
       ("guard", "Tempered glass", "Box of 50", "In stock", "hi"), ("buds", "Wireless earbuds", "Box of 10", "Out · back Thu", "no"), ("holder", "Car holders", "Box of 12", "In stock", "hi")]
P["p170_mobacc"] = page("""
body{--f:'Roboto';--h:'Fira Sans';background:#2a1560;color:#fff}
h1{font-family:'Fira Sans';font-size:62px;font-weight:800;letter-spacing:-1px;line-height:1.2} h1 span{color:#6ef0c0}
.sub{color:#c9bdf0;font-size:23px}
.vis{flex-direction:column;gap:16px}
.tab{flex:1;background:#111018;border-radius:40px;padding:18px;display:flex;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.scr{flex:1;background:#f6f4fb;border-radius:24px;color:#22184a;padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.th{display:flex;justify-content:space-between;align-items:center}.th b{font:800 28px 'Fira Sans'}.th span{font:600 16px Roboto;background:#e3dcf7;color:#4b2a8c;border-radius:10px;padding:6px 12px}
.gr{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.pc{background:#fff;border-radius:18px;padding:12px 14px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:4px;box-shadow:0 6px 16px rgba(42,21,96,.06)}
.pc b{font:700 25px 'Fira Sans';text-align:center}.pc span{font:500 19px Roboto;color:#6b6290}
.pc em{font-style:normal;font:700 17px Roboto;border-radius:10px;padding:4px 10px;display:flex;align-items:center;gap:6px}.pc em i{width:10px;height:10px;border-radius:50%}
.hi{background:#dcf8ec;color:#167a55}.hi i{background:#2bbf8a}.lo{background:#fff1cc;color:#7a5a00}.lo i{background:#e0a800}.no{background:#fde0e0;color:#a32323}.no i{background:#d33}
.ct{display:flex;align-items:center;gap:14px;background:#6ef0c0;color:#22184a;border-radius:22px;padding:16px 22px}
.ct .ib{width:52px;height:52px;border-radius:14px;background:#22184a;color:#6ef0c0}.ct div{flex:1}.ct b{display:block;font:800 24px 'Fira Sans'}.ct span{font:500 18px Roboto}
.ct em{font-style:normal;font:700 19px Roboto;background:#22184a;color:#fff;border-radius:14px;padding:12px 18px}
""", "<h1>Dealers call to ask,<br><span>“Is it in stock?”</span></h1><div class=sub>A dealer catalogue that shows live stock and takes the order.</div>",
f'''<div class=tab><div class=scr><div class=th><b>Dealer catalogue</b><span>Login: Sample Mobile Shop</span></div>
<div class=gr>{"".join(f'<div class=pc>{prod(k)}<b>{a}</b><span>{s}</span><em class={c}><i></i>{t}</em></div>' for k,a,s,t,c in cat)}</div></div></div>
<div class=ct><span class=ib>{ic("cart",28)}</span><div><b>Order from Sample Mobile Shop</b><span>4 items · 22 packs · sent to your counter</span></div><em>Order placed</em></div>''',
"#ffffff", "Sell accessories to dealers? DM us", "background:#6ef0c0;color:#22184a", logo_color="#ffffff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
