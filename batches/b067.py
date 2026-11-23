import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
fmt = lambda n: f"{n:,}"

# ───────── 351 INDIA · Momo outlets (3 counters) · SINGLE · Anton + Inter · steamer bamboo / chilli red / dough white
# New technique: CSS bamboo steamer stacks (woven bands + lid knob) sized from the plan, beside mini bars of the
# last 4 same weekdays; the kitchen sheet totals are computed from the plans.
OUT = [("Outlet A", "College road", [110, 124, 118, 120], "Veg"), ("Outlet B", "Bus stand", [86, 92, 80, 90], "Paneer"), ("Outlet C", "Mall food court", [140, 150, 146, 152], "Chicken")]
PC = 6
plan = lambda o: round(sum(o[2]) / 4 / 5) * 5
def steamer(n):
    return '<div class=stm>' + '<i class=kn></i><i class=ld></i>' + "".join('<i class=ly></i>' for _ in range(n)) + '</div>'
P["p351_momo"] = page("""
body{--f:'Inter';--h:'Anton';background:#fbf3e4;color:#2b1d14}
.kk{font:700 16px/1.5 Inter;letter-spacing:3px;color:#d3361f;margin-top:22px;margin-bottom:4px}
h1{font-family:'Anton';font-weight:400;font-size:70px;line-height:1.25;letter-spacing:.5px;text-transform:uppercase} h1 span{color:#d3361f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.oc1{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.cd1{background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(43,29,20,.08)}
.cd1>b{font:400 30px/1.5 Anton;letter-spacing:.5px}.cd1>span{font:500 16px/1.4 Inter;color:#6f5c4c;margin-top:-6px}
.mb1{display:flex;gap:8px;align-items:flex-end;height:150px;border-bottom:2px solid #eadbc6;padding-bottom:4px}.mb1 div{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;justify-content:flex-end;height:100%}
.mb1 i{width:100%;background:#e9c98f;border-radius:6px 6px 0 0}.mb1 em{font:600 15px/1.3 Inter;font-style:normal;color:#6f5c4c}
.cap1{font:600 13px/1.4 Inter;letter-spacing:1.5px;color:#8a7461}
.stw{flex:1;display:flex;align-items:flex-end;justify-content:center;min-height:0}
.stm{display:flex;flex-direction:column;align-items:center}
.stm .kn{width:30px;height:12px;border-radius:6px 6px 0 0;background:#8a5a2b}
.stm .ld{width:160px;height:22px;border-radius:50% 50% 6px 6px / 100% 100% 6px 6px;background:#c98c46}
.stm .ly{width:170px;height:36px;margin-top:3px;border-radius:6px;background:repeating-linear-gradient(90deg,#d9a35f 0 8px,#c98c46 8px 10px);box-shadow:inset 0 4px 0 #b77937,inset 0 -4px 0 #b77937}
.pl1{background:#2b1d14;color:#fff;border-radius:16px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center}
.pl1 small{font:600 13px/1.4 Inter;color:#e7d2b8}.pl1 b{font:400 30px/1.4 Anton;color:#ffb199}
.ks1{background:#d3361f;color:#fff;border-radius:22px;padding:14px 20px;display:grid;grid-template-columns:1.2fr repeat(3,1fr);gap:14px;align-items:center}
.ks1>span{font:600 17px/1.4 Inter}.ks1 div{background:rgba(255,255,255,.14);border-radius:14px;padding:8px 12px}.ks1 small{display:block;font:600 13px/1.4 Inter;color:#ffd9d0}.ks1 b{font:400 28px/1.4 Anton}
""", "<div class=kk>MOMO OUTLETS · DAILY PREP</div><h1>Momos left over at night?<br><span>Steam what each outlet sells.</span></h1>",
f'''<div class=vw><div class=oc1>{"".join(f"""<div class=cd1><b>{o[0]}</b><span>{o[1]} · sample</span><small class=cap1>LAST 4 MONDAYS · PLATES</small>
<div class=mb1>{"".join(f'<div><i style="height:{v/160*100:.0f}%"></i><em>{v}</em></div>' for v in o[2])}</div>
<div class=stw>{steamer(min(7, plan(o)//20))}</div><div class=pl1><small>PLAN TODAY<br>{plan(o)*PC:,} pieces</small><b>{plan(o)} plates</b></div></div>""" for o in OUT)}</div>
<div class=ks1><span>Kitchen sheet for Monday, sent at 9 AM. {PC} pieces a plate.</span>{"".join(f'<div><small>{o[3]} momos</small><b>{plan(o)*PC:,}</b></div>' for o in OUT)}</div></div>''',
"#2b1d14", "Run momo outlets? DM us", "background:#d3361f;color:#fff")

# ───────── 353 USA · Cat sitting (home visits) · SINGLE · Poppins + DM Sans · whisker grey / yarn pink / mint · PHONE
# New technique: house-key tags on a ring (SVG) as the client list, with visit chips per day, beside a phone visit
# report whose times and tasks match the key tag for that client.
CL = [("K-1", "Maple St", "2 cats", ["Sat", "Sun", "Mon"], "#f49ac1"), ("K-2", "Oak Ave", "1 cat", ["Sat", "Sun"], "#8fd9c1"), ("K-3", "Pine Ct", "3 cats", ["Sun", "Mon", "Tue"], "#ffd27a"), ("K-4", "Elm Rd", "1 cat", ["Mon", "Tue", "Wed"], "#b7c4ff")]
def keyring():
    s = '<svg viewBox="0 0 320 300" class=kr3><circle cx="160" cy="46" r="34" fill="none" stroke="#8d939b" stroke-width="8"/>'
    for i, (k, st, n, d, c) in enumerate(CL):
        x = 40 + i * 80; r = -14 + i * 9
        s += f'<g transform="rotate({r} {x+20} 80)"><path d="M{x+20} 80 L{x+20} 120" stroke="#8d939b" stroke-width="5"/><rect x="{x}" y="118" width="40" height="120" rx="10" fill="{c}" stroke="#3b3f45" stroke-width="3"/><circle cx="{x+20}" cy="134" r="6" fill="#fff" stroke="#3b3f45" stroke-width="3"/>'
        s += f'<text x="{x+7}" y="200" font-family="Poppins" font-weight="800" font-size="16" fill="#2b2f35">{k}</text></g>'
    return s + "</svg>"
ph3 = phone('''<div class=ap3><div class=ah3><small>SAMPLE CAT CARE</small><b>Visit report · K-1</b><span>Maple St · Sat, Dec 5 · 8:10 AM</span></div>
<div class=pt3><i></i><i></i></div>
<div class=tk3>''' + "".join(f'<div><span class=ib>{ic("check",16,w=3)}</span>{t}</div>' for t in ["Food and fresh water", "Litter box cleaned", "Play time, 15 minutes", "Plants watered", "Door locked, key back on ring", "2 photos sent to the owner"]) + '''</div>
<div class=nx3><small>NEXT VISIT</small><b>Sat, Dec 5 · 6 PM</b></div><div class=bk3>Message the sitter</div></div>''', 350, 800)
P["p353_cats"] = page("""
body{--f:'DM Sans';--h:'Poppins';background:#f1f1f3;color:#2b2f35}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#d4558f;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:58px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#d4558f}
.vw{flex:1;display:flex;gap:18px;min-height:0;align-items:center}
.lf3{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:12px;min-width:0}
.rg3{background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;align-items:center;box-shadow:0 12px 26px rgba(43,47,53,.07)}
.rg3>small,.wk3>small{align-self:flex-start;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#6d727a}.kr3{width:420px;display:block}
.wk3{flex:1;background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(43,47,53,.07)}
.wr3{flex:1;display:grid;grid-template-columns:64px 1fr;gap:10px;align-items:center;border-bottom:1px solid #eeeef1}.wr3:last-child{border:0}
.wr3>b{font:800 20px/1.3 Poppins;border-radius:8px;padding:4px 0;text-align:center}
.wr3 div span{display:block;font:600 19px/1.35 'DM Sans'}.wr3 div em{display:flex;gap:6px;margin-top:4px}.wr3 div em i{font:700 15px/1.3 'DM Sans';font-style:normal;background:#2b2f35;color:#fff;border-radius:6px;padding:3px 8px}
.ap3{display:flex;flex-direction:column;gap:10px;padding:8px 18px 18px;flex:1}
.ah3 small{display:block;font:700 11px/1.4 'DM Sans';letter-spacing:2px;color:#6d727a}.ah3 b{display:block;font:800 21px/1.35 Poppins}.ah3 span{font:500 14px/1.4 'DM Sans';color:#6d727a}
.pt3{display:grid;grid-template-columns:1fr 1fr;gap:8px}.pt3 i{height:110px;border-radius:12px;background:radial-gradient(circle at 50% 60%,#9aa0a8 0 26px,transparent 27px),radial-gradient(circle at 38% 38%,#9aa0a8 0 10px,transparent 11px),radial-gradient(circle at 62% 38%,#9aa0a8 0 10px,transparent 11px),#f9dbe8}
.pt3 i:last-child{background:radial-gradient(circle at 50% 60%,#e3a35b 0 26px,transparent 27px),radial-gradient(circle at 38% 38%,#e3a35b 0 10px,transparent 11px),radial-gradient(circle at 62% 38%,#e3a35b 0 10px,transparent 11px),#d8f3ea}
.tk3{display:flex;flex-direction:column;gap:6px}.tk3 div{display:flex;align-items:center;gap:10px;font:500 16px/1.35 'DM Sans';background:#f6f6f8;border-radius:10px;padding:10px 10px}.tk3 .ib{width:24px;height:24px;border-radius:50%;background:#3fbf8f;color:#fff}
.nx3{background:#fde9f2;border-radius:12px;padding:8px 12px}.nx3 small{display:block;font:700 11px/1.4 'DM Sans';letter-spacing:1.5px;color:#a63d6d}.nx3 b{font:700 16px/1.4 'DM Sans'}
.bk3{margin-top:auto;background:#2b2f35;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 16px Poppins}
""", "<div class=kk>CAT SITTING · HOME VISITS</div><h1>Keys, visits, photos?<br><span>Give owners peace of mind.</span></h1>",
f'''<div class=vw><div class=lf3><div class=rg3><small>KEY RING · 4 CLIENTS · SAMPLE</small>{keyring()}</div>
<div class=wk3><small>VISITS THIS WEEKEND · 2 A DAY</small>{"".join(f'<div class=wr3><b style="background:{c}">{k}</b><div><span>{st} · {n}</span><em>{"".join(f"<i>{x}</i>" for x in d)}</em></div></div>' for k,st,n,d,c in CL)}</div></div>{ph3}</div>''',
"#2b2f35", "Run a pet sitting business? DM us", "background:#d4558f;color:#fff")

# ───────── 354 CANADA · Winter car storage · SINGLE · Bitter + Fira Sans · garage concrete / battery green / frost blue
# New technique: top-down SVG garage bay map with car silhouettes (roof + windshield shapes) and a battery tender
# charge badge per spot, plus a monthly check timeline computed from each car's last check date.
SP = [("A1", "Sedan", "Nov 2", 92), ("A2", "Coupe", "Nov 2", 88), ("A3", "SUV", "Nov 9", 64), ("A4", None, "", 0),
      ("B1", "Convertible", "Nov 9", 90), ("B2", "Classic", "Nov 16", 95), ("B3", None, "", 0), ("B4", "Sports car", "Nov 16", 58)]
def garage():
    W, H = 840, 420
    s = f'<svg viewBox="0 0 {W} {H}" class=gr4><rect width="{W}" height="{H}" rx="14" fill="#cfd3d6"/><rect x="0" y="190" width="{W}" height="40" fill="#b7bcc0"/>'
    s += "".join(f'<line x1="{20+i*200}" y1="14" x2="{20+i*200}" y2="180" stroke="#fff" stroke-width="4"/><line x1="{20+i*200}" y1="240" x2="{20+i*200}" y2="406" stroke="#fff" stroke-width="4"/>' for i in range(5))
    for i, (sp, car, d, b) in enumerate(SP):
        col, row = i % 4, i // 4
        x = 40 + col * 200; y = 26 if row == 0 else 252
        s += f'<text x="{x}" y="{y+20}" font-family="Bitter" font-weight="800" font-size="20" fill="#5b6268">{sp}</text>'
        if car:
            cx = x + 26; cy = y + 34
            s += f'<rect x="{cx}" y="{cy}" width="108" height="120" rx="26" fill="#3d6e9e"/><rect x="{cx+12}" y="{cy+26}" width="84" height="24" rx="8" fill="#cfe3f5"/><rect x="{cx+14}" y="{cy+58}" width="80" height="40" rx="10" fill="#2f5880"/>'
            col_b = "#3fa45b" if b >= 80 else "#e0a020"
            s += f'<rect x="{cx+68}" y="{cy+92}" width="62" height="30" rx="8" fill="{col_b}" stroke="#fff" stroke-width="3"/><text x="{cx+76}" y="{cy+114}" font-family="Fira Sans" font-weight="700" font-size="17" fill="#fff">{b}%</text>'
        else:
            s += f'<rect x="{x+26}" y="{y+34}" width="108" height="120" rx="20" fill="none" stroke="#8d949a" stroke-width="3" stroke-dasharray="10 8"/><text x="{x+50}" y="{y+100}" font-family="Fira Sans" font-weight="700" font-size="20" fill="#6d747a">Open</text>'
    return s + "</svg>"
cars4 = [c for c in SP if c[1]]
low4 = [c for c in cars4 if c[3] < 80]
P["p354_storage"] = page("""
body{--f:'Fira Sans';--h:'Bitter';background:#e6edf2;color:#22282d}
.kk{font:600 16px/1.4 'Fira Sans';letter-spacing:3px;color:#2f7f45;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1px} h1 span{color:#3d6e9e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.mp4{background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(34,40,45,.08)}
.mp4>small,.ck4>small{font:600 13px/1.4 'Fira Sans';letter-spacing:2px;color:#6a7278}.gr4{width:100%;display:block}
.bt4{flex:1;display:grid;grid-template-columns:1.35fr 1fr;gap:14px;min-height:0}
.ck4{background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 12px 26px rgba(34,40,45,.08)}
.cr4{flex:1;display:grid;grid-template-columns:50px 1fr auto;gap:12px;align-items:center;border-bottom:1px solid #eef1f3;font:500 17px/1.35 'Fira Sans'}.cr4:last-child{border:0}
.cr4 b{font:800 19px/1.3 Bitter}.cr4 strong{font:600 15px/1.3 'Fira Sans';border-radius:8px;padding:4px 10px;background:#e3f3e7;color:#2f7f45}.cr4 strong.lo{background:#fdf0d5;color:#9a6a00}
.nt4{background:#22282d;color:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.nt4 small{font:600 13px/1.4 'Fira Sans';letter-spacing:2px;color:#9fd3ff}.nt4 b{font:800 30px/1.25 Bitter;color:#9fe0ae}.nt4 p{font:400 18px/1.45 'Fira Sans';color:#d6dde2}
.nt4 .bx{margin-top:auto;background:#3d6e9e;border-radius:12px;padding:10px 14px;font:500 16px/1.4 'Fira Sans'}
""", "<div class=kk>WINTER CAR STORAGE · NOV TO APR</div><h1>Cars stored all winter?<br><span>Check each one, every month.</span></h1>",
f'''<div class=vw><div class=mp4><small>INDOOR BAYS A AND B · BATTERY TENDER CHARGE · SAMPLE</small>{garage()}</div>
<div class=bt4><div class=ck4><small>MONTHLY CHECKS · DECEMBER</small>{"".join(f'<div class=cr4><b>{sp}</b><span>{car} · last check {d}</span><strong class="{"lo" if b<80 else ""}">{"Check now" if b<80 else "Due Dec " + d.split()[1]}</strong></div>' for sp,car,d,b in cars4)}</div>
<div class=nt4><small>THIS WEEK</small><b>{len(low4)} batteries low</b><p>{" and ".join(c[0] for c in low4)} get a charge check. Owners get a photo of the dash and tire pressure.</p><div class=bx>{len(SP)-len(cars4)} open spots. New customers book a spot online.</div></div></div></div>''',
"#22282d", "Store cars for winter? DM us", "background:#3d6e9e;color:#fff")

# ───────── 355 INDIA · Electric scooter dealer · SINGLE · Archivo Black + DM Sans · EV teal / charge yellow / road grey
# New technique: SVG side-view scooters (floorboard, seat, round lamp) in showroom colours, each with a test-ride slot
# strip; the day's booked rides and follow-up list come from one slot table.
SC = [("Model 1", "#16a39a", ["10 AM", "11 AM", "12 PM", "4 PM", "5 PM", "6 PM"], {"10 AM", "12 PM", "5 PM"}),
      ("Model 2", "#f3c623", ["10 AM", "11 AM", "12 PM", "4 PM", "5 PM", "6 PM"], {"11 AM", "4 PM"}),
      ("Model 3", "#b9c4cb", ["10 AM", "11 AM", "12 PM", "4 PM", "5 PM", "6 PM"], {"10 AM", "5 PM", "6 PM"})]
def scooter(c):
    return (f'<svg viewBox="0 0 300 180" class=sc5><circle cx="62" cy="140" r="30" fill="#2a3135"/><circle cx="62" cy="140" r="12" fill="#9aa4aa"/><circle cx="238" cy="140" r="30" fill="#2a3135"/><circle cx="238" cy="140" r="12" fill="#9aa4aa"/>'
            f'<path d="M40 116 Q60 92 110 100 L200 100 Q215 70 236 66 L246 66 L262 120 L216 128 L100 128 Q70 130 40 116 Z" fill="{c}" stroke="#2a3135" stroke-width="4"/>'
            f'<rect x="86" y="74" width="84" height="20" rx="10" fill="#2a3135"/><path d="M246 66 L232 18 L210 16" fill="none" stroke="#2a3135" stroke-width="6" stroke-linecap="round"/><circle cx="252" cy="50" r="10" fill="#fff7c2" stroke="#2a3135" stroke-width="3"/></svg>')
BOOKED = sum(len(s[3]) for s in SC)
P["p355_ev"] = page("""
body{--f:'DM Sans';--h:'Archivo Black';background:#eaf3f2;color:#1d2a2d}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#0f8c84;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.25;letter-spacing:-1px} h1 span{color:#0f8c84}
.vw{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}
.rw5{flex:1;min-height:0;background:#fff;border-radius:24px;padding:12px 20px;display:grid;grid-template-columns:260px 1fr;gap:18px;align-items:center;box-shadow:0 12px 26px rgba(29,42,45,.07)}
.sc5{width:100%;display:block}.md5 b{display:block;font:400 26px/1.4 'Archivo Black'}
.sl5{display:flex;flex-direction:column;gap:8px}.sl5>div{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}
.sl5 i{font:700 19px/1.3 'DM Sans';font-style:normal;text-align:center;padding:16px 0;border-radius:10px;background:#eaf3f2;color:#0f6c66}.sl5 i.bk{background:#1d2a2d;color:#f3c623}
.sl5 small{font:600 16px/1.4 'DM Sans';color:#5d6b6f}
.bt5{display:grid;grid-template-columns:1fr 1.5fr;gap:12px}
.tt5{background:#1d2a2d;color:#fff;border-radius:20px;padding:14px 18px}.tt5 small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#9fd8d3}.tt5 b{font:400 40px/1.3 'Archivo Black';color:#f3c623}.tt5 span{display:block;font:500 16px/1.4 'DM Sans'}
.fu5{background:#0f8c84;color:#fff;border-radius:20px;padding:14px 18px;font:500 18px/1.45 'DM Sans'}.fu5 b{color:#fff3b0}
""", "<div class=kk>ELECTRIC SCOOTER DEALER · TEST RIDES</div><h1>Test ride calls all day?<br><span>Let buyers book a slot.</span></h1>",
f'''<div class=vw>{"".join(f'<div class=rw5><div class=md5>{scooter(c)}<b>{m}</b></div><div class=sl5><small>TEST RIDE SLOTS · SAT 28 NOV · SAMPLE</small><div>{"".join(f"<i class={chr(34)}{"bk" if t in b else ""}{chr(34)}>{t}</i>" for t in ts)}</div><small>{len(b)} booked · {len(ts)-len(b)} open</small></div></div>' for m,c,ts,b in SC)}
<div class=bt5><div class=tt5><small>SATURDAY</small><b>{BOOKED} rides</b><span>booked online, with phone number and licence check</span></div>
<div class=fu5>After each ride, the buyer gets the price sheet and a follow-up call is added for Monday. <b>No lead is lost in a notebook.</b></div></div></div>''',
"#1d2a2d", "Sell electric scooters? DM us", "background:#0f8c84;color:#fff")

# ───────── 352 INDIA · Construction labour contractor · CAROUSEL 5 · Cardo + Roboto · brick red / helmet yellow / blueprint navy
# New technique: CSS hard hats (dome + brim, filled = present, outline = absent) as an isotype per site, then a weekly
# attendance sheet (P / half / absent cells) whose day counts feed the pay list on slide 4.
LB = """
body{--f:'Roboto';--h:'Cardo';background:#eef1f5;color:#1c2738}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#b8432b;margin-top:22px;margin-bottom:4px}
h1{font-family:'Cardo';font-weight:700;font-size:64px;line-height:1.3;letter-spacing:-.5px} h1 span{color:#b8432b}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(28,39,56,.08)}
.cap{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#667185}
.nb{display:flex;align-items:center;gap:14px;background:#1c2738;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Roboto}.nb .ib{width:50px;height:50px;border-radius:14px;background:#f5c518;color:#1c2738}.nb b{color:#f5c518}
.ht{width:58px;height:40px;position:relative;flex:none}
.ht::before{content:"";position:absolute;left:8px;right:8px;top:0;bottom:10px;border-radius:30px 30px 4px 4px;background:#f5c518;box-shadow:inset -6px 0 0 #d9a90c}
.ht::after{content:"";position:absolute;left:0;right:0;bottom:2px;height:10px;border-radius:5px;background:#e0b10f}
.ht.ab::before{background:none;border:3px dashed #9aa3b2;box-shadow:none}.ht.ab::after{background:#d5dae2}
"""
def lb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1c2738;color:#f5c518"):
    return page(LB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1c2738", cta, ctacss, tagline=f"{n} / 5")
SITES = [("Site 1", "Tower, 7th floor slab", 16, 14), ("Site 2", "Bungalow, plaster work", 12, 10), ("Site 3", "Shop row, tiling", 12, 11)]
TW = sum(s[2] for s in SITES); TP = sum(s[3] for s in SITES)
P["p352_labour_s1"] = lb(1, "LABOUR CONTRACTOR · SITE ATTENDANCE", f"{TW} workers, 3 sites.<br><span>Who came today?</span>",
f'''<div class=w1>{"".join(f'<div class="cd st1"><div class=hd1><b>{a}</b><span>{b} · sample</span></div><div class=hs1>{"".join(f"<i class={chr(34)}ht {"" if i<p else "ab"}{chr(34)}></i>" for i in range(t))}</div><strong>{p} of {t}</strong></div>' for a,b,t,p in SITES)}
<div class=bb1><span class=vn>{ic("phone",22)} Site 2 supervisor, 9:40 AM</span><p>“Two more are coming at 10. Or maybe after lunch. I will call you back.”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.st1{flex:1;display:grid;grid-template-columns:240px 1fr 130px;gap:16px;align-items:center;padding:12px 22px}
.hd1 b{display:block;font:700 32px/1.35 Cardo}.hd1 span{font:500 17px/1.4 Roboto;color:#667185}
.hs1{display:flex;flex-wrap:wrap;gap:12px 10px}.hs1 .ht{width:66px;height:46px}.st1 strong{font:700 30px/1.35 Cardo;text-align:right;color:#b8432b}
.bb1{background:#1c2738;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 Roboto;color:#f5c518;margin-bottom:6px}.bb1 p{font:500 23px/1.4 Roboto}""")

GATE = [("W-01", "Mason", "Site 1", "8:02 AM"), ("W-02", "Helper", "Site 1", "8:05 AM"), ("W-07", "Carpenter", "Site 1", "8:11 AM"), ("W-12", "Mason", "Site 2", "8:20 AM"), ("W-15", "Helper", "Site 2", "8:24 AM"), ("W-21", "Tiler", "Site 3", "8:31 AM"), ("W-22", "Helper", "Site 3", "8:33 AM")]
P["p352_labour_s2"] = lb(2, "STEP 1 · MARK AT THE SITE GATE", "Each worker marked in,<br><span>with time and site.</span>",
f'''<div class=w2><div class="cd gl2"><div class=gh2><small class=cap>GATE LIST · MON 23 NOV · SAMPLE</small><span>{TP} of {TW} in</span></div>{"".join(f'<div class=gr2><i class=av>{w[2:]}</i><div><b>{w}</b><span>{r}</span></div><em>{s}</em><strong>{t}</strong><span class=ib>{ic("check",18,w=3)}</span></div>' for w,r,s,t in GATE)}
<div class=mr2>+ {TP-len(GATE)} more marked in today</div></div>
<div class=nb><span class=ib>{ic("users",26)}</span><span>The supervisor taps each name at the gate. <b>The office sees all 3 sites live.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.gl2{flex:1;padding:16px 24px;display:flex;flex-direction:column;gap:6px}
.gh2{display:flex;justify-content:space-between;align-items:center}.gh2 span{font:700 18px/1.4 Roboto;color:#2f8a4c}
.gr2{flex:1;display:grid;grid-template-columns:52px 1fr 110px 110px 34px;gap:14px;align-items:center;border-bottom:1px solid #eef1f5}
.gr2 .av{width:48px;height:48px;border-radius:50%;background:#1c2738;color:#f5c518;font:700 17px/48px Roboto;font-style:normal;text-align:center}
.gr2 b{display:block;font:700 22px/1.35 Cardo}.gr2 div span{font:500 16px/1.4 Roboto;color:#667185}.gr2 em{font:600 16px/1.3 Roboto;font-style:normal;background:#eef1f5;border-radius:8px;padding:6px 10px;text-align:center}
.gr2 strong{font:600 18px/1.3 Roboto;text-align:right}.gr2 .ib{width:32px;height:32px;border-radius:50%;background:#2f8a4c;color:#fff}
.mr2{font:600 17px/1.4 Roboto;color:#667185;text-align:center;padding-top:6px}""")

WK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
ATT = [("W-01", "Mason", "PPPPPH"), ("W-02", "Helper", "PPAPPP"), ("W-07", "Carpenter", "PPPHPP"), ("W-12", "Mason", "PPPPPP"), ("W-15", "Helper", "APPPPH"), ("W-21", "Tiler", "PPPPAP")]
dw = lambda a: sum(1 if c == "P" else (0.5 if c == "H" else 0) for c in a)
fd = lambda v: f"{v:g}"
P["p352_labour_s3"] = lb(3, "STEP 2 · THE WEEK SHEET BUILDS ITSELF", "Full day, half day, absent,<br><span>counted for you.</span>",
f'''<div class=w3><div class="cd sh3"><div class="r3 h3"><span>WORKER</span>{"".join(f"<span>{d.upper()}</span>" for d in WK)}<span>DAYS</span></div>
{"".join(f'<div class=r3><div><b>{w}</b><em>{r}</em></div>{"".join(f"<i class={c}>{ {chr(80):chr(80),chr(72):chr(189),chr(65):chr(8211)}[c]}</i>" for c in a)}<strong>{fd(dw(a))}</strong></div>' for w,r,a in ATT)}
<div class=lg3><span><i class=P>P</i>Present</span><span><i class=H>½</i>Half day</span><span><i class=A>–</i>Absent</span><em>Week of Mon 16 Nov · sample</em></div></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;min-height:0}.sh3{flex:1;padding:18px 24px;display:flex;flex-direction:column;gap:6px}
.r3{flex:1;display:grid;grid-template-columns:170px repeat(6,1fr) 80px;gap:8px;align-items:center}
.h3{flex:none;font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#667185;padding-bottom:6px;border-bottom:2px solid #1c2738}.h3 span{text-align:center}.h3 span:first-child{text-align:left}
.r3 b{display:block;font:700 24px/1.35 Cardo}.r3 em{font:500 15px/1.4 Roboto;font-style:normal;color:#667185}
.r3 i{height:56px;border-radius:12px;display:flex;align-items:center;justify-content:center;font:700 22px/1.3 Roboto;font-style:normal}
i.P{background:#2f8a4c;color:#fff}i.H{background:#f5c518;color:#1c2738}i.A{background:#f1f3f7;color:#9aa3b2;border:2px dashed #c9cfd9}
.r3 strong{font:700 30px/1.35 Cardo;text-align:right;color:#b8432b}
.lg3{display:flex;gap:18px;align-items:center;font:600 16px/1.4 Roboto;color:#4d5868;margin-top:6px}.lg3 span{display:flex;align-items:center;gap:8px}.lg3 i{width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font:700 16px Roboto;font-style:normal}.lg3 em{margin-left:auto;font-style:normal;color:#667185}""")

ADV = {"W-02": "Yes", "W-15": "Yes"}
P["p352_labour_s4"] = lb(4, "STEP 3 · SATURDAY PAY LIST", "Every worker sees<br><span>the same days you see.</span>",
f'''<div class=w4><div class="cd pl4">{"".join(f'<div class=p4><b>{w}</b><span>{r}</span><strong>{fd(dw(a))} days</strong><em class="{"y" if w in ADV else ""}">{"Advance taken" if w in ADV else "No advance"}</em><i>{ic("check",18,w=3)} UPI</i></div>' for w,r,a in ATT)}</div>
<div class="cd ms4"><small class=cap>MESSAGE TO W-07 · SATURDAY 21 NOV</small><p>This week: {fd(dw(ATT[2][2]))} days (half day on Thursday). Your pay is sent by UPI today. Next week: Site 1, 8 AM.</p></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pl4{flex:1;padding:12px 24px;display:flex;flex-direction:column}
.p4{flex:1;display:grid;grid-template-columns:110px 1fr 140px 190px 100px;gap:12px;align-items:center;border-bottom:1px solid #eef1f5}.p4:last-child{border:0}
.p4 b{font:700 26px/1.35 Cardo}.p4 span{font:500 20px/1.4 Roboto;color:#667185}.p4 strong{font:700 24px/1.35 Cardo;color:#b8432b}
.p4 em{font:600 17px/1.3 Roboto;font-style:normal;border-radius:8px;padding:6px 10px;background:#eef1f5;text-align:center}.p4 em.y{background:#fff4cc;color:#8a6a00}
.p4 i{display:flex;align-items:center;gap:6px;font:700 17px/1.3 Roboto;font-style:normal;background:#2f8a4c;color:#fff;border-radius:8px;padding:6px 10px}
.ms4{padding:16px 22px;display:flex;flex-direction:column;gap:6px}.ms4 p{font:500 22px/1.45 Roboto}""")

P["p352_labour_s5"] = lb(5, "YOUR TURN", "Supply workers to sites?<br><span>Let's build your app.</span>",
f'''<div class=w5><div class="cd c5">{"".join(f"<i class={chr(34)}ht {"" if i%7 else "ab"}{chr(34)}></i>" for i in range(30))}</div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("check","Gate attendance","Name, time and site"),("grid","Week sheet","Full, half, absent"),("rupee","Pay list","Days and advances"),("send","Worker messages","Days, pay, next site")])}</div>
<div class=q>How do you keep worker attendance today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b8432b;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1.05fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{display:grid;grid-template-columns:repeat(5,1fr);align-content:center;justify-items:center;gap:40px 8px;padding:20px}.c5 .ht{width:80px;height:56px}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(28,39,56,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#fff4cc;color:#1c2738}.ti b{display:block;font:700 24px/1.4 Cardo;margin-bottom:2px}.ti div span{font:500 17px/1.4 Roboto;color:#4d5868}
.q{background:#1c2738;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 Roboto}""")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
