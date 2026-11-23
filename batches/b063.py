import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 331 INDIA · Newspaper agency (home delivery) · SINGLE · Lora + Roboto · newsprint grey / ink black / masthead red
# New technique: receipt-style month bill with zigzag torn edges (clip-path), next to a delivery register whose
# 30-day dot strip per flat (delivered / paused) produces the copy counts on the bill.
FLATS = [("B-101", "English daily", set()), ("B-102", "English daily + weekly", set()), ("B-201", "Marathi daily", {20, 21}),
         ("B-202", "English daily", {1, 2, 3}), ("B-304", "English daily + weekly", {12, 13, 14, 15}), ("B-401", "Hindi daily", set())]
def strip(paused):
    return "".join(f'<i class="{"pz" if d in paused else ""}"></i>' for d in range(1, 31))
bf = FLATS[4]; days = 30 - len(bf[2]); weeklies = 4
zig = "polygon(" + ",".join(f"{x*5}% {0 if x%2==0 else 2.2}%" for x in range(21)) + "," + ",".join(f"{100-x*5}% {100 if x%2==0 else 97.8}%" for x in range(21)) + ")"
P["p331_paper"] = page("""
body{--f:'Roboto';--h:'Lora';background:#e9e7e1;color:#1d1d1f}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#c62d2d;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:64px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#c62d2d}
.vw{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:18px;min-height:0}
.rg1{background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(0,0,0,.07)}
.rg1>small,.rc1 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#77756f}
.fl1{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-bottom:1px solid #ecebe6}.fl1:last-of-type{border:0}
.fl1>div:first-child{display:flex;justify-content:space-between;align-items:baseline;gap:10px}.fl1 b{font:700 22px/1.3 Lora}.fl1 span{font:500 16px/1.35 Roboto;color:#55534e}
.ds1{display:grid;grid-template-columns:repeat(30,1fr);gap:3px}.ds1 i{height:20px;border-radius:3px;background:#1d1d1f}.ds1 i.pz{background:#f3c6c6;box-shadow:inset 0 0 0 2px #c62d2d}
.fl1.on{background:#fff5f2;margin:0 -10px;padding:0 10px;border-radius:12px}
.lgx1{display:flex;gap:18px;font:600 15px/1.4 Roboto;color:#55534e;margin-top:4px}.lgx1 span{display:flex;align-items:center;gap:8px}.lgx1 i{width:16px;height:16px;border-radius:3px;background:#1d1d1f}.lgx1 i.pz{background:#f3c6c6;box-shadow:inset 0 0 0 2px #c62d2d}
.rc1{background:#fffef8;clip-path:ZIG;padding:40px 26px 40px;display:flex;flex-direction:column;justify-content:space-between;gap:6px;filter:drop-shadow(0 10px 18px rgba(0,0,0,.12))}
.rc1>b{font:700 30px/1.3 Lora;text-align:center}.rc1 .c1{text-align:center;font:500 15px/1.4 Roboto;color:#55534e;border-bottom:2px dashed #cfcac0;padding-bottom:10px}
.ln1{display:flex;justify-content:space-between;gap:10px;font:500 22px/1.4 Roboto;padding:4px 0}.ln1 strong{font-weight:700}
.ln1.m{color:#c62d2d}.ln1.t{border-top:2px dashed #cfcac0;padding-top:12px;font:700 22px/1.4 Roboto}
.cl1{display:grid;grid-template-columns:repeat(10,1fr);gap:4px;margin-top:6px}.cl1 i{font:600 15px/34px Roboto;font-style:normal;text-align:center;border-radius:5px;background:#ecebe6}.cl1 i.pz{background:#f3c6c6;color:#c62d2d;box-shadow:inset 0 0 0 2px #c62d2d}
.rc1 .up{background:#1d1d1f;color:#fff;border-radius:12px;padding:12px;text-align:center;font:700 18px/1.3 Roboto}
.rc1 .nt{font:500 17px/1.45 Roboto;color:#55534e;text-align:center}
""".replace("ZIG", zig), "<div class=kk>NEWSPAPER AGENCY · HOME DELIVERY</div><h1>Month-end bills by memory?<br><span>Count every paper.</span></h1>",
f'''<div class=vw><div class=rg1><small>TOWER B · NOVEMBER · SAMPLE REGISTER</small>{"".join(f'<div class="fl1 {"on" if f==bf[0] else ""}"><div><b>{f}</b><span>{p}</span></div><div class=ds1>{strip(z)}</div></div>' for f,p,z in FLATS)}
<div class=lgx1><span><i></i>Delivered</span><span><i class=pz></i>Paused by the customer</span></div></div>
<div class=rc1><b>Flat {bf[0]}</b><div class=c1>Bill for November · Tower B · sample</div>
<div class=ln1><span>English daily</span><strong>30 days</strong></div><div class="ln1 m"><span>Paused 12 to 15 Nov</span><strong>− {len(bf[2])} days</strong></div>
<div class=ln1><span>Daily, delivered</span><strong>{days} copies</strong></div><div class=ln1><span>Weekly magazine, Sundays</span><strong>5 issues</strong></div><div class="ln1 m"><span>Paused Sunday 15 Nov</span><strong>− 1 issue</strong></div><div class=ln1><span>Weekly, delivered</span><strong>{weeklies} issues</strong></div>
<div class="ln1 t"><span>To pay for</span><span>{days + weeklies} papers</span></div>
<div class=cl1>{"".join(f'<i class="{"pz" if d in bf[2] else ""}">{d}</i>' for d in range(1,31))}</div><div class=nt>Sent by message on 1 December. Pause days come from the customer's own reply.</div><div class=up>Pay by UPI</div></div></div>''',
"#1d1d1f", "Run a paper agency? DM us", "background:#c62d2d;color:#fff")

# ───────── 332 INDIA · Hydroponic farm · SINGLE · Archivo Black + Inter · leaf lime / pipe white / water teal
# New technique: SVG NFT grow channels (white pipes with net cups), plant size drawn from the week number,
# with harvest dates and buyer orders read from the same channel list.
CH = [("C1", "Lettuce", 5, "Sat 28 Nov"), ("C2", "Lettuce", 3, "Sat 12 Dec"), ("C3", "Basil", 4, "Fri 4 Dec"), ("C4", "Spinach", 5, "Sat 28 Nov"), ("C5", "Pak choi", 2, "Fri 18 Dec"), ("C6", "Basil", 1, "Fri 25 Dec")]
CC = {"Lettuce": "#7cc242", "Basil": "#2f8f4e", "Spinach": "#3f7a35", "Pak choi": "#9ccc65"}
def channel(crop, wk, n=9):
    W, H = 640, 64; r = 6 + wk * 4.2
    cups = "".join(f'<circle cx="{40+i*70}" cy="32" r="9" fill="#26313a"/>' for i in range(n))
    leaves = "".join(f'<g>{"".join(f"<ellipse cx=\'{40+i*70+math.cos(a)*r*.55:.1f}\' cy=\'{32+math.sin(a)*r*.45:.1f}\' rx=\'{r*.6:.1f}\' ry=\'{r*.42:.1f}\' transform=\'rotate({math.degrees(a):.0f} {40+i*70+math.cos(a)*r*.55:.1f} {32+math.sin(a)*r*.45:.1f})\' fill=\'{CC[crop]}\' stroke=\'#1f4d2b\' stroke-width=\'1.5\'/>" for a in [k*math.pi/3 for k in range(6)])}</g>' for i in range(n))
    return f'<svg viewBox="0 0 {W} {H}" class=cs2 preserveAspectRatio="xMidYMid meet"><rect x="4" y="20" width="{W-8}" height="24" rx="12" fill="#f4f7f6" stroke="#b9c7c4" stroke-width="2"/><rect x="8" y="34" width="{W-16}" height="6" rx="3" fill="#56c1c9" fill-opacity=".6"/>{cups}{leaves}</svg>'
ORD2 = [("Café 1", "Lettuce", 6), ("Restaurant 2", "Basil", 2), ("Salad bar 3", "Spinach", 4), ("Hotel 4", "Lettuce", 5)]
P["p332_hydro"] = page("""
body{--f:'Inter';--h:'Archivo Black';background:#eef5ee;color:#15302a}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#1b8a92;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;line-height:1.25;letter-spacing:-1px;margin-top:30px} h1 span{color:#4e9a23}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.gh{flex:1;min-height:0;background:#15302a;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}
.gh>small{font:700 13px/1.5 Inter;letter-spacing:2px;color:#a9dcc6}
.rw2{flex:1;display:grid;grid-template-columns:56px 1fr 170px;gap:12px;align-items:center;min-height:0}
.rw2>b{font:400 22px/1.5 'Archivo Black';color:#fff}.cs2{width:100%;height:100%;max-height:78px;display:block}
.rw2 div span{display:block;font:700 17px/1.35 Inter;color:#fff}.rw2 div em{font:500 15px/1.4 Inter;font-style:normal;color:#a9dcc6}.rw2 div em.rd{color:#d7f56b;font-weight:700}
.bt2{display:grid;grid-template-columns:1.4fr 1fr;gap:14px}
.or2{background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 12px 26px rgba(21,48,42,.07)}.or2 small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#6b7f78}
.oo{display:grid;grid-template-columns:1.3fr 1fr 60px;gap:8px;padding:8px 0;border-bottom:1px solid #e6eee8;font:500 18px/1.35 Inter}.oo:last-child{border:0}.oo strong{text-align:right;font:400 20px/1.4 'Archivo Black'}
.ms2{background:#4e9a23;color:#fff;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:8px;font:500 19px/1.45 Inter}.ms2 b{font:400 40px/1.3 'Archivo Black';color:#e8ff9a}
""", "<div class=kk>HYDROPONIC FARM · GROW CHANNELS</div><h1>Which channel is ready?<br><span>Know before buyers call.</span></h1>",
f'''<div class=vw><div class=gh><small>GROW ROOM 1 · SIX CHANNELS · 9 PLANTS EACH · SAMPLE</small>{"".join(f'<div class=rw2><b>{c}</b>{channel(cr,w)}<div><span>{cr} · week {w}</span><em class="{"rd" if d=="Sat 28 Nov" else ""}">Harvest {d}</em></div></div>' for c,cr,w,d in CH)}</div>
<div class=bt2><div class=or2><small>BUYER ORDERS · SAT 28 NOV · KG</small>{"".join(f'<div class=oo><span>{a}</span><span>{b}</span><strong>{q}</strong></div>' for a,b,q in ORD2)}</div>
<div class=ms2><b>C1 + C4</b>ready on Saturday. Basil for Restaurant 2 comes from C3 next Friday, so they get a message today.</div></div></div>''',
"#15302a", "Grow hydroponic greens? DM us", "background:#15302a;color:#d7f56b")

# ───────── 333 INDIA · Laptop rental for offices and events · CAROUSEL 5 · TeX Gyre Adventor + Open Sans · matte graphite / asset-tag yellow / screen blue
# New technique: CSS laptops (screen gradient + clip-path base) with yellow asset-tag stickers, reused as a fleet
# grid, plus a daily "units out" bar strip derived from the rental list.
LT = """
body{--f:'Open Sans';--h:'TeX Gyre Adventor';background:#eceef2;color:#22252b}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#3b6fe0;margin-top:22px;align-self:flex-start}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#3b6fe0}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(34,37,43,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#6e7380}
.nb{display:flex;align-items:center;gap:14px;background:#22252b;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 'Open Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#ffcc33;color:#22252b}.nb b{color:#ffcc33}
.lp{display:flex;flex-direction:column;align-items:center;position:relative}
.lp .sc{width:100%;aspect-ratio:16/10;border-radius:8px 8px 2px 2px;background:linear-gradient(135deg,#4b7cf0,#1c3f9e);box-shadow:inset 0 0 0 5px #2b2f37}
.lp .bs{width:118%;height:12px;background:#9aa1ad;clip-path:polygon(6% 0,94% 0,100% 100%,0 100%);border-radius:0 0 6px 6px}
.lp .tg{position:absolute;top:22%;left:50%;transform:translateX(-50%);background:#ffcc33;color:#22252b;font:700 15px/1.4 'Open Sans';border-radius:6px;padding:2px 8px;white-space:nowrap}
.lp .tg.q{background:#e5484d;color:#fff}
"""
def lt(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#22252b;color:#ffcc33"):
    return page(LT + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#22252b", cta, ctacss, tagline=f"{n} / 5")
def lap(tag, q=False):
    return f'<div class=lp><div class=sc></div><div class=bs></div><span class="tg {"q" if q else ""}">{tag}</span></div>'
RENT = [("Company A", "Office project", 1, 15, "Mon 2 Nov", "Mon 30 Nov"), ("Event B", "3-day event", 16, 25, "Tue 24 Nov", "Fri 27 Nov"), ("Training C", "Staff class", 26, 40, "Mon 16 Nov", "Mon 30 Nov")]
unk = {29, 33, 37}
P["p333_laptops_s1"] = lt(1, "LAPTOP RENTAL · OFFICES AND EVENTS", "40 laptops out on rent.<br><span>Who has L-33?</span>",
f'''<div class=w1><div class="cd c1"><small class=cap>TRAINING C · L-26 TO L-40 · SAMPLE</small><div class=gl1>{"".join(lap(f"L-{i}" if i not in unk else "L-?", i in unk) for i in range(26,41))}</div></div>
<div class=bb1><span class=vn>{ic("chat",22)} Training C, 11:20 AM</span><p>“We returned all 15 laptops. Your sheet says 14.”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c1{flex:1;min-height:0;padding:18px 26px;display:flex;flex-direction:column;gap:14px}
.gl1{flex:1;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(3,1fr);gap:14px 34px;align-items:center;padding:0 14px}
.bb1{background:#22252b;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 'Open Sans';color:#ffcc33;margin-bottom:6px}.bb1 p{font:500 24px/1.4 'Open Sans'}""")

tot = sum(b - a + 1 for _, _, a, b, _, _ in RENT)
P["p333_laptops_s2"] = lt(2, "STEP 1 · EVERY TAG HAS A CLIENT", "Each rental lists<br><span>the exact tag numbers.</span>",
f'''<div class=w2>{"".join(f'<div class="cd rc2"><div class=hd2><b>{c}</b><span>{p} · sample</span><strong>{b-a+1} units</strong></div><div class=tg2>{"".join(f"<i>L-{i:02d}</i>" for i in range(a,b+1))}</div><div class=dt2><span>Out <b>{o}</b></span><span>Back <b>{r}</b></span></div></div>' for c,p,a,b,o,r in RENT)}
<div class=nb><span class=ib>{ic("tag",26)}</span><span><b>{tot} laptops out</b>, 3 clients. Search any tag and see who has it.</span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.rc2{flex:1;padding:14px 20px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.hd2{display:flex;align-items:baseline;gap:14px}.hd2 b{font:700 30px/1.3 'TeX Gyre Adventor'}.hd2 span{font:500 17px/1.4 'Open Sans';color:#6e7380;flex:1}.hd2 strong{font:700 22px/1.3 'TeX Gyre Adventor';color:#3b6fe0}
.tg2{display:flex;flex-wrap:wrap;gap:6px}.tg2 i{font:700 18px/1.4 'Open Sans';font-style:normal;background:#ffcc33;border-radius:7px;padding:4px 9px}
.dt2{display:flex;gap:24px;font:500 19px/1.4 'Open Sans';color:#4b505b}.dt2 b{color:#22252b}""")

days3 = [("Mon", 23), ("Tue", 24), ("Wed", 25), ("Thu", 26), ("Fri", 27), ("Sat", 28), ("Sun", 29), ("Mon", 30)]
def outc(d):
    n = 0
    for c, p, a, b, o, r in RENT:
        od = 2 if "2 Nov" in o else int(o.split()[1]); rd = int(r.split()[1])
        if od <= d <= rd: n += b - a + 1
    return n
rets = {27: "Event B returns 10", 30: "A and C return 30"}
P["p333_laptops_s3"] = lt(3, "STEP 2 · RETURNS ON A CALENDAR", "See what comes back<br><span>and when.</span>",
f'''<div class=w3><div class="cd ch3"><small class=cap>LAPTOPS OUT PER DAY · OF 40 · SAMPLE</small><div class=br3>{"".join(f'<div class="cl3 {"rt" if d in rets else ""}"><b>{outc(d)}</b><div class=bw3><i style="height:{outc(d)/40*100:.0f}%"></i></div><span>{w}<br>{d} Nov</span></div>' for w,d in days3)}</div></div>
<div class=rr3>{"".join(f'<div class="cd ri3"><span class=ib>{ic("cal",28)}</span><div><b>{"Fri 27 Nov" if d==27 else "Mon 30 Nov"}</b><span>{t}. Pickup van booked, check sheet ready.</span></div></div>' for d,t in rets.items())}</div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ch3{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px;min-height:0}
.br3{flex:1;display:grid;grid-template-columns:repeat(8,1fr);gap:12px;min-height:0}.cl3{display:flex;flex-direction:column;align-items:center;gap:8px;min-height:0}
.cl3 b{font:700 26px/1.3 'TeX Gyre Adventor'}.bw3{flex:1;width:100%;background:#eef0f4;border-radius:12px;display:flex;align-items:flex-end;overflow:hidden}.bw3 i{width:100%;background:#3b6fe0;border-radius:12px 12px 0 0}
.cl3 span{font:600 16px/1.35 'Open Sans';text-align:center;color:#4b505b}.cl3.rt b{color:#e0a400}.cl3.rt .bw3{box-shadow:inset 0 0 0 3px #ffcc33}
.rr3{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ri3{display:flex;gap:14px;align-items:center;padding:16px 18px}.ri3 .ib{width:54px;height:54px;border-radius:14px;background:#ffcc33;color:#22252b}
.ri3 b{display:block;font:700 22px/1.35 'TeX Gyre Adventor'}.ri3 div span{font:500 17px/1.4 'Open Sans';color:#4b505b}""")

chk = [("L-16", 1, 1, 1, 1), ("L-17", 1, 1, 1, 1), ("L-18", 1, 1, 1, 1), ("L-19", 1, 0, 1, 1), ("L-20", 1, 1, 1, 1), ("L-21", 1, 1, 0, 1), ("L-22", 1, 1, 1, 1)]
ok = lambda v: f'<i class="{"y" if v else "n"}">{ic("check",18,w=3) if v else ic("x",18,w=3)}</i>'
P["p333_laptops_s4"] = lt(4, "STEP 3 · CHECK EVERY UNIT ON RETURN", "Missing charger?<br><span>Found on day one.</span>",
f'''<div class=w4><div class="cd tb4"><div class="rw4 hd4"><span>TAG</span><span>SCREEN</span><span>CHARGER</span><span>BAG</span><span>KEYS</span></div>
{"".join(f'<div class="rw4 {"bad" if 0 in (a,b,c,d) else ""}"><b>{t}</b>{ok(a)}{ok(b)}{ok(c)}{ok(d)}</div>' for t,a,b,c,d in chk)}
<div class=ft4>Event B · Fri 27 Nov · sample · <b>{sum(1 for r in chk if 0 not in r[1:])} of {len(chk)} shown complete</b></div></div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>Event B gets a message with the list: <b>L-19 charger, L-21 bag.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb4{flex:1;padding:14px 26px;display:flex;flex-direction:column}
.rw4{flex:1;display:grid;grid-template-columns:1.2fr repeat(4,1fr);gap:10px;align-items:center;border-bottom:1px solid #eceef2;padding:0 10px}
.hd4{flex:none;padding:6px 10px 12px;border-bottom:2px solid #22252b;font:700 14px/1.4 'Open Sans';letter-spacing:1.5px;color:#6e7380}
.rw4 b{font:700 24px 'TeX Gyre Adventor'}.rw4 i{width:40px;height:40px;border-radius:10px;display:flex;align-items:center;justify-content:center;color:#fff}.rw4 i.y{background:#2f9e6b}.rw4 i.n{background:#e5484d}
.rw4.bad{background:#fff3f3;border-radius:12px}
.ft4{background:#eef0f4;border-radius:14px;padding:14px 18px;margin-top:12px;font:500 19px/1.4 'Open Sans'}.ft4 b{color:#3b6fe0}""")

P["p333_laptops_s5"] = lt(5, "YOUR TURN", "Rent laptops or IT gear?<br><span>Let's build your rental app.</span>",
f'''<div class=w5><div class="cd c5"><div class=gl5>{"".join(lap(f"L-{i:02d}") for i in range(1,10))}</div></div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,32)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("tag","Tag search","Who has any laptop"),("cal","Return calendar","What comes back, when"),("check","Return check","Charger, bag, keys"),("send","Client messages","Lists and reminders")])}</div>
<div class=q>How do you track laptops out on rent today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#3b6fe0;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1.1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{padding:22px 30px;display:flex;min-height:0}.w5 .q{grid-column:1 / 3}
.gl5{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:10px 30px;align-items:center}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(34,37,43,.07)}
.ti .ib{width:60px;height:60px;border-radius:18px;background:#fff1c2;color:#22252b}.ti b{display:block;font:700 22px/1.45 'TeX Gyre Adventor';margin-bottom:3px}.ti div span{font:500 17px/1.4 'Open Sans';color:#4b505b}
.q{background:#22252b;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'Open Sans'}""")

# ───────── 334 INDIA · Rooftop solar panel cleaning service · SINGLE · Gelasio + Inter · sun yellow / panel navy / dust beige · PHONE
# New technique: top-down SVG rooftop (parapet, water tank, stair room) with a panel array where cleaned panels
# shine (diagonal glare) and dusty ones are speckled, counts taken from the same array.
done4 = 10; tot4 = 16
def roof():
    W, H = 520, 560
    s = f'<svg viewBox="0 0 {W} {H}" class=rf4><rect width="{W}" height="{H}" rx="14" fill="#cfc5ae"/><rect x="14" y="14" width="{W-28}" height="{H-28}" rx="8" fill="#e6dcc5"/>'
    s += '<rect x="34" y="34" width="120" height="96" rx="6" fill="#bdb196"/><circle cx="420" cy="90" r="46" fill="#4b5d73"/><circle cx="420" cy="90" r="30" fill="#5d7189"/>'
    random.seed(334)
    for i in range(tot4):
        r, c = divmod(i, 4)
        x, y = 50 + c * 108, 170 + r * 92
        if i < done4:
            s += f'<rect x="{x}" y="{y}" width="98" height="82" rx="4" fill="#1d3557" stroke="#c9d3df" stroke-width="3"/><path d="M{x+3} {y+60} L{x+60} {y+3} L{x+78} {y+3} L{x+3} {y+78} Z" fill="#fff" fill-opacity=".18"/>'
            s += "".join(f'<line x1="{x+3+k*24}" y1="{y+3}" x2="{x+3+k*24}" y2="{y+79}" stroke="#c9d3df" stroke-opacity=".35"/>' for k in range(1, 4))
        else:
            s += f'<rect x="{x}" y="{y}" width="98" height="82" rx="4" fill="#8c8670" stroke="#c9d3df" stroke-width="3"/>'
            s += "".join(f'<circle cx="{x+random.uniform(8,90):.0f}" cy="{y+random.uniform(8,74):.0f}" r="{random.uniform(1.5,4):.1f}" fill="#d8cda9"/>' for _ in range(26))
    return s + "</svg>"
RF = [("R-10", "Sector 4", 12, "Done 7:50 AM", "dn"), ("R-12", "Sector 4", 16, f"Now · {done4} of {tot4}", "nw"), ("R-15", "Sector 6", 24, "Next · 11 AM", "")]
ph4 = phone(f'''<div class=ap4><div class=ah4><small>SAMPLE SOLAR CARE</small><b>Your rooftop R-12</b><span>16 panels · twice a month</span></div>
<div class=lv4><b>Cleaning now</b><span>{done4} of {tot4} panels done</span><i><em style="width:{done4/tot4*100:.0f}%"></em></i></div>
<div class=ph4x><div><i class=d4></i><span>Before</span></div><div><i class=c4></i><span>After</span></div></div>
<div class=rw4x><small>LAST VISIT</small><span>Mon 9 Nov · 7:30 AM</span></div><div class=rw4x><small>NEXT VISIT</small><span>Tue 8 Dec · 7 AM</span></div>
<div class=rw4x><small>TEAM</small><span>Team 2 · 2 cleaners</span></div><div class=rw4x><small>WATER</small><span>Your tank tap, on the roof</span></div>
<div class=bk4>Change visit time</div></div>''', 350, 830)
P["p334_solar"] = page("""
body{--f:'Inter';--h:'Gelasio';background:#f4eddc;color:#1d3557}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#c98a00;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:58px;line-height:1.24;letter-spacing:-.5px} h1 span{color:#d48f00}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.lf4{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.mp4{flex:1;min-height:0;background:#fff;border-radius:24px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(29,53,87,.08)}
.mp4>small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#7a7462}.rf4{flex:1;min-height:0;width:100%;display:block}
.lgx4{display:flex;gap:18px;font:600 15px/1.4 Inter}.lgx4 span{display:flex;align-items:center;gap:8px}.lgx4 i{width:18px;height:18px;border-radius:4px}
.rl4{display:flex;flex-direction:column;gap:8px}.rr4{display:grid;grid-template-columns:70px 1fr auto;gap:10px;align-items:center;background:#fff;border-radius:16px;padding:10px 14px;border-left:7px solid #d8cda9}
.rr4 b{font:700 20px/1.3 Gelasio}.rr4 span{font:500 16px/1.35 Inter;color:#4a5568}.rr4 em{font:700 14px/1.3 Inter;font-style:normal;border-radius:8px;padding:5px 9px;background:#efe7d3}
.rr4.dn{border-color:#2f9e6b}.rr4.dn em{background:#2f9e6b;color:#fff}.rr4.nw{border-color:#f4b41a}.rr4.nw em{background:#f4b41a;color:#1d3557}
.ap4{display:flex;flex-direction:column;gap:10px;padding:8px 18px 18px;flex:1;min-height:0}
.ah4 small{display:block;font:700 11px/1.4 Inter;letter-spacing:2px;color:#7a7462}.ah4 b{display:block;font:700 23px/1.3 Gelasio}.ah4 span{font:500 14px/1.4 Inter;color:#4a5568}
.lv4{background:#1d3557;color:#fff;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}.lv4 b{font:700 17px/1.3 Inter;color:#f4b41a}.lv4 span{font:500 14px/1.4 Inter}.lv4 i{height:10px;border-radius:5px;background:#3b5478;overflow:hidden;margin-top:4px}.lv4 i em{display:block;height:100%;background:#f4b41a}
.ph4x{display:grid;grid-template-columns:1fr 1fr;gap:10px}.ph4x div{display:flex;flex-direction:column;gap:4px;align-items:center}.ph4x i{width:100%;height:120px;border-radius:12px}.ph4x span{font:600 13px/1.4 Inter;color:#4a5568}
.d4{background:radial-gradient(circle at 30% 40%,#d8cda9 0 3px,transparent 4px) 0 0/22px 22px,radial-gradient(circle at 70% 70%,#cfc39d 0 2px,transparent 3px) 0 0/17px 17px,#8c8670}
.c4{background:linear-gradient(135deg,transparent 40%,rgba(255,255,255,.22) 40% 55%,transparent 55%),repeating-linear-gradient(90deg,#1d3557 0 30px,#9fb0c6 30px 32px)}
.rw4x{background:#f8f4ea;border-radius:12px;padding:8px 12px}.rw4x small{display:block;font:700 11px/1.4 Inter;letter-spacing:1.5px;color:#7a7462}.rw4x span{font:600 15px/1.4 Inter}
.bk4{margin-top:auto;background:#f4b41a;color:#1d3557;border-radius:14px;padding:13px;text-align:center;font:700 16px Inter}
""", "<div class=kk>ROOFTOP SOLAR PANEL CLEANING</div><h1>Dusty panels on 40 rooftops?<br><span>Plan every visit.</span></h1>",
f'''<div class=vw><div class=lf4><div class=mp4><small>ROOFTOP R-12 · TUE 24 NOV · SAMPLE</small>{roof()}<div class=lgx4><span><i style="background:#1d3557"></i>Cleaned {done4}</span><span><i style="background:#8c8670"></i>Still dusty {tot4-done4}</span></div></div>
<div class=rl4>{"".join(f'<div class="rr4 {k}"><b>{r}</b><span>{a} · {n} panels</span><em>{t}</em></div>' for r,a,n,t,k in RF)}</div></div>{ph4}</div>''',
"#1d3557", "Clean solar panels? DM us", "background:#1d3557;color:#f4b41a")

# ───────── 335 USA · Dumpster rental · SINGLE · Montserrat + Source Sans 3 · dumpster green / caution orange / asphalt
# New technique: side-view SVG roll-off dumpsters drawn to length by size (10/20/30 yard) with ribbed walls,
# yard vs out counts derived from the rental rows below.
FLEET = {"10": 4, "20": 5, "30": 3}
RNT = [("D-10-1", "10", "Oak St", "Mon 11/30", "Wed 12/2", "On site"), ("D-20-1", "20", "Pine Ave", "Mon 11/30", "Fri 12/4", "On site"),
       ("D-20-3", "20", "Lake Rd", "Tue 12/1", "Thu 12/3", "Drop today"), ("D-30-2", "30", "Mill St", "Tue 12/1", "Mon 12/7", "Drop today"),
       ("D-10-2", "10", "Elm Ct", "Fri 11/27", "Tue 12/1", "Pickup today"), ("D-20-4", "20", "Birch Ln", "Wed 11/25", "Tue 12/1", "Pickup today")]
outn = {z: sum(1 for r in RNT if r[1] == z) for z in FLEET}
def dump(z):
    L = {"10": 150, "20": 210, "30": 270}[z]; Hh = {"10": 70, "20": 86, "30": 104}[z]
    W, H = 300, 130; x0 = (W - L) / 2; y0 = H - 22
    body = f'<path d="M{x0} {y0} L{x0+L} {y0} L{x0+L+10} {y0-Hh} L{x0-10} {y0-Hh} Z" fill="#2f6b4f" stroke="#1d4634" stroke-width="3"/>'
    ribs = "".join(f'<line x1="{x0+k*L/6:.0f}" y1="{y0-4}" x2="{x0+k*L/6 + (k-3)*3:.0f}" y2="{y0-Hh+4}" stroke="#1d4634" stroke-width="4"/>' for k in range(1, 6))
    rail = f'<rect x="{x0-14}" y="{y0}" width="{L+28}" height="8" rx="3" fill="#2b2d2f"/><circle cx="{x0+14}" cy="{y0+13}" r="7" fill="#2b2d2f"/><circle cx="{x0+L-14}" cy="{y0+13}" r="7" fill="#2b2d2f"/>'
    stripe = f'<rect x="{x0+L-30}" y="{y0-Hh+10}" width="20" height="{Hh-20}" fill="#f28b30"/>'
    return f'<svg viewBox="0 0 {W} {H}" class=dm5>{body}{ribs}{stripe}{rail}</svg>'
stc = {"On site": "os5", "Drop today": "dp5", "Pickup today": "pk5"}
P["p335_dumpster"] = page("""
body{--f:'Source Sans 3';--h:'Montserrat';background:#ecefe8;color:#2b2d2f}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#d9701c;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#2f6b4f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.yd5{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.dc5{background:#fff;border-radius:22px;padding:12px 14px 14px;display:flex;flex-direction:column;align-items:center;gap:4px;box-shadow:0 12px 26px rgba(43,45,47,.07)}
.dm5{width:100%;height:120px;display:block}.dc5 b{font:800 24px/1.3 Montserrat}.dc5 span{font:600 17px/1.4 'Source Sans 3';color:#55595e}.dc5 span em{font-style:normal;font-weight:700;color:#d9701c}
.tb5{flex:1;min-height:0;background:#fff;border-radius:24px;padding:12px 20px;display:flex;flex-direction:column;box-shadow:0 12px 26px rgba(43,45,47,.07)}
.r5{flex:1;display:grid;grid-template-columns:100px 70px 1fr 110px 110px 140px;gap:10px;align-items:center;border-bottom:1px solid #e9ece5;font:600 19px/1.35 'Source Sans 3'}.r5:last-child{border:0}
.r5.hd{flex:none;padding:6px 0 10px;border-bottom:2px solid #2b2d2f;font:700 13px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#6b6f74}
.r5 b{font:800 18px Montserrat;color:#2f6b4f}.r5 i{font:700 15px/1.3 'Source Sans 3';font-style:normal;border-radius:8px;padding:5px 10px;justify-self:start}
.os5{background:#e1efe6;color:#2f6b4f}.dp5{background:#f28b30;color:#fff}.pk5{background:#2b2d2f;color:#fff}
.nt5{display:flex;align-items:center;gap:14px;background:#2f6b4f;color:#fff;border-radius:20px;padding:14px 20px;font:500 20px/1.4 'Source Sans 3'}.nt5 b{color:#ffd29e}.nt5 .ib{width:48px;height:48px;border-radius:14px;background:#f28b30;color:#fff}
""", "<div class=kk>DUMPSTER RENTAL · ROLL-OFF</div><h1>Which dumpster is where?<br><span>See every drop and pickup.</span></h1>",
f'''<div class=vw><div class=yd5>{"".join(f'<div class=dc5>{dump(z)}<b>{z} yard</b><span>{FLEET[z]-outn[z]} in yard · <em>{outn[z]} out</em></span></div>' for z in FLEET)}</div>
<div class=tb5><div class="r5 hd"><span>UNIT</span><span>SIZE</span><span>JOB · SAMPLE</span><span>DROP</span><span>PICKUP</span><span>TODAY · 12/1</span></div>
{"".join(f'<div class=r5><b>{u}</b><span>{z} yd</span><span>{a}</span><span>{d}</span><span>{p}</span><i class={stc[s_]}>{s_}</i></div>' for u,z,a,d,p,s_ in RNT)}</div>
<div class=nt5><span class=ib>{ic("img",26)}</span><span>Customers book online and add a driveway photo with a pin, <b>so the driver knows where to drop.</b></span></div></div>''',
"#2b2d2f", "Rent dumpsters? DM us", "background:#2b2d2f;color:#ffd29e")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
