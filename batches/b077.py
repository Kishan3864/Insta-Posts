import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 402 INDIA · Bus body builder · SINGLE · Anton + Roboto · primer grey / coach blue / signal yellow
# New technique: SVG top-down bus seat plan generated from a layout spec (2+2 rows, aisle, door, driver, emergency exit)
# with seat numbers; the seat count on the spec card and the approval stamp come from the same layout.
ROWS2 = 10
def busplan2():
    s = 34; g = 6; x0 = 70; y0 = 26; W = 720; H = 230
    seats = []; n = 0
    for r in range(ROWS2):
        x = x0 + 60 + r * (s + 12)
        for k, yy in enumerate([y0 + 14, y0 + 14 + s + g, y0 + 14 + 2 * (s + g) + 34, y0 + 14 + 3 * (s + g) + 34]):
            if r == 0 and k >= 2: continue
            n += 1; seats.append((x, yy, n))
    last = x0 + 60 + ROWS2 * (s + 12)
    for k in range(5):
        n += 1; seats.append((last, y0 + 14 + k * (s + 2) + (6 if k > 1 else 0), n))
    body = f'<rect x="{x0}" y="{y0}" width="{last + s + 22 - x0}" height="{4 * (s + g) + 34 + 22}" rx="26" fill="#f4f6f9" stroke="#1f4e8c" stroke-width="5"/>'
    drv = f'<rect x="{x0 + 14}" y="{y0 + 14}" width="{s}" height="{s}" rx="8" fill="#1b1f27"/><text x="{x0 + 31}" y="{y0 + 14 + s + 20}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="12" fill="#1b1f27">Driver</text>'
    door = f'<rect x="{x0 + 10}" y="{y0 + 4 * (s + g) + 34 - 4}" width="{s + 18}" height="12" rx="4" fill="#f2c230"/><text x="{x0 + 36}" y="{y0 + 4 * (s + g) + 34 - 12}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="12" fill="#8a6a08">Door</text>'
    ex = f'<rect x="{x0 + 60 + 6 * (s + 12) - 4}" y="{y0 - 6}" width="{s + 8}" height="10" rx="3" fill="#d9442b"/><text x="{x0 + 60 + 6 * (s + 12) + s / 2}" y="{y0 - 10}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="12" fill="#d9442b">Exit</text>'
    st = "".join(f'<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="7" fill="#1f4e8c"/><text x="{x + s / 2}" y="{y + s / 2 + 5}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="14" fill="#fff">{k}</text>' for x, y, k in seats)
    aisle = f'<text x="{x0 + 60 + 3 * (s + 12)}" y="{y0 + 14 + 2 * (s + g) + 22}" font-family="Roboto" font-weight="600" font-size="13" fill="#7c8594">Aisle</text>'
    return f'<svg viewBox="0 0 {last + s + 40} {y0 + 4 * (s + g) + 34 + 40}" width="{last + s + 40}" style="display:block;width:100%;height:auto;max-height:250px">{body}{ex}{drv}{door}{st}{aisle}</svg>', n
PLAN2, SEATS2 = busplan2()
STG2 = ["Chassis in", "Frame", "Panels", "Paint", "Interior", "Delivery"]
YD2 = [("BB-31", f"Staff bus · {SEATS2} seats", 4, "Interior done Fri"), ("BB-32", "Tourist bus · 2+2", 2, "Panels till Thu"), ("BB-33", "Staff bus · 33 seats", 1, "Frame Mon"), ("BB-34", "Tourist bus · AC", 5, "Ready Wed 25 Nov")]
P["p402_busbody"] = page("""
body{--f:'Roboto';--h:'Anton';background:#eceff3;color:#1b1f27}
.kk{font:700 16px/1.5 Roboto;letter-spacing:3px;color:#1f4e8c;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.25;letter-spacing:.3px;margin-top:30px} h1 span{color:#1f4e8c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm2{font:700 13px/1.5 Roboto;letter-spacing:2px;color:#68707e}
.pc2{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(27,31,39,.08)}
.pc2 .h{display:flex;justify-content:space-between;align-items:center;gap:10px}
.ap2{font:700 15px/1.2 Roboto;background:#e2f1e6;color:#1f6b3a;border:2px solid #1f6b3a;border-radius:10px;padding:7px 12px;white-space:nowrap}
.md2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:14px}
.sp2{background:#1b1f27;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:4px}.sp2 .sm2{color:#aab3c2}
.sp2 .r{flex:1;min-height:34px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.12);gap:10px}.sp2 .r span{font:500 16px/1.3 Roboto;color:#c4ccd8}.sp2 .r b{font:700 18px/1.3 Roboto;text-align:right}
.ch2{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(27,31,39,.08)}
.cv2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:4px;border-top:1px solid #edf0f4}.cv2 b{font:700 18px/1.3 Roboto}.cv2 span{font:500 15px/1.35 Roboto;color:#5f6775}.cv2 s{color:#9aa1ad}
.yd2{flex:1;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(27,31,39,.08);min-height:0}
.yr2{flex:1;display:grid;grid-template-columns:1.25fr 2.2fr 1fr;gap:12px;align-items:center;border-top:1px solid #edf0f4}
.yr2 b{display:block;font:700 18px/1.3 Roboto}.yr2 span{font:500 14px/1.3 Roboto;color:#5f6775}
.sb2{display:grid;grid-template-columns:repeat(6,1fr);gap:4px}.sb2 i{height:26px;border-radius:6px;background:#e3e7ee;display:flex;align-items:center;justify-content:center;font:600 11px/1 Roboto;font-style:normal;color:#7c8594}
.sb2 i.on{background:#1f4e8c;color:#fff}.sb2 i.nw{background:#f2c230;color:#1b1f27}
.yr2 em{font:700 14px/1.3 Roboto;font-style:normal;background:#fff6d6;color:#7a5a00;border-radius:10px;padding:7px 9px;text-align:center}
""", "<div class=kk>BUS BODY BUILDER · LAYOUT AND STAGES</div><h1>Seat plan changed again?<br><span>Get the layout approved first.</span></h1>",
f'''<div class=vw><div class=pc2><div class=h><span class=sm2>BB-31 · SEAT PLAN v2 · TOP VIEW · SAMPLE</span><span class=ap2>✓ Approved by buyer · Mon 9 Nov</span></div>{PLAN2}</div>
<div class=md2><div class=sp2><span class=sm2>BB-31 · BODY SPEC</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Buyer", "Sample Transport Co."), ("Use", "Staff bus"), ("Seats", f"{SEATS2} + driver"), ("Windows", "Sliding glass"), ("Colour", "White, blue band")])}</div>
<div class=ch2><span class=sm2>CHANGES ON RECORD</span>{"".join(f'<div class=cv2><b>{a}</b><span>{b}</span></div>' for a, b in [("v1 · Tue 3 Nov", "37 seats, last row of 4"), ("v2 · Fri 6 Nov", "Last row of 5, exit moved to row 7"), ("Buyer approval", "Signed on the app, Mon 9 Nov")])}</div></div>
<div class=yd2><span class=sm2>BODIES IN THE YARD</span>{"".join(f'<div class=yr2><div><b>{j}</b><span>{d}</span></div><div class=sb2>{"".join(f"""<i class='{"on" if k < n else ("nw" if k == n else "")}'>{s}</i>""" for k, s in enumerate(STG2))}</div><em>{nx}</em></div>' for j, d, n, nx in YD2)}</div></div>''',
"#1b1f27", "Build bus bodies? DM us", "background:#1f4e8c;color:#fff")


# ───────── 403 USA · Pickleball facility · SINGLE · Montserrat + DM Sans · court blue / kitchen green / ball yellow
# New technique: four top-down SVG pickleball courts (kitchen zones, centre lines, net) each wearing its live status, over a
# courts x hours booking grid where every block is sized by its time span from one schedule list.
CT3 = ["Court 1", "Court 2", "Court 3", "Court 4"]
HR3 = list(range(16, 22))
SC3 = [(0, 16, 18, "Open play", "op"), (0, 18, 19.5, "Private · Sample Group", "pv"), (0, 20, 22, "League night", "lg"),
       (1, 16, 17, "Lesson", "ls"), (1, 17.5, 19, "Private · Sample Pair", "pv"), (1, 20, 22, "League night", "lg"),
       (2, 16, 18, "Open play", "op"), (2, 19, 20.5, "Private · Sample Group", "pv"),
       (3, 17, 18, "Lesson", "ls"), (3, 18, 20, "Private · Sample Club", "pv")]
NOW3 = 18.25
def stat3(c):
    for cc, a, b, t, k in SC3:
        if cc == c and a <= NOW3 < b: return (f"{t.split(' · ')[0]} until {fmt3(b)}", k)
    nxt = min([a for cc, a, b, t, k in SC3 if cc == c and a > NOW3], default=22)
    return (f"Open until {fmt3(nxt)}", "fr")
def fmt3(h): return f"{int(h) - 12}:{'30' if h % 1 else '00'} PM"
def court3(k):
    col = {"op": "#3a7dc2", "pv": "#1d4f8a", "lg": "#6a4fb3", "ls": "#2c8f6a", "fr": "#9aa6b2"}[k]
    return f'''<svg viewBox="0 0 120 220" width="120" style="display:block;width:100%;height:auto"><rect x="4" y="4" width="112" height="212" rx="6" fill="{col}"/><rect x="14" y="14" width="92" height="192" fill="#2f6fb0" stroke="#fff" stroke-width="3"/>
<rect x="14" y="88" width="92" height="44" fill="#4f9a5e" stroke="#fff" stroke-width="3"/><line x1="60" y1="14" x2="60" y2="88" stroke="#fff" stroke-width="3"/><line x1="60" y1="132" x2="60" y2="206" stroke="#fff" stroke-width="3"/>
<line x1="8" y1="110" x2="112" y2="110" stroke="#1b2530" stroke-width="5"/><circle cx="88" cy="56" r="6" fill="#f3e24a"/></svg>'''
P["p403_pickle"] = page("""
body{--f:'DM Sans';--h:'Montserrat';background:#eef3f8;color:#16202b}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#2c8f6a;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#1d4f8a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm3{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#66727f}
.ct3{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.cc3{background:#fff;border-radius:22px;padding:12px;display:flex;flex-direction:column;gap:8px;align-items:center;box-shadow:0 12px 26px rgba(22,32,43,.08)}
.cc3 .cw{width:118px}.cc3 b{font:800 19px/1.3 Montserrat}.cc3 span{font:700 14px/1.3 'DM Sans';border-radius:10px;padding:6px 9px;text-align:center}
.k-op{background:#e1edf9;color:#245e9c}.k-pv{background:#dfe7f3;color:#1d4f8a}.k-lg{background:#ebe5f7;color:#553c9a}.k-ls{background:#dff1e9;color:#1f6f50}.k-fr{background:#fbf6d2;color:#6f6300}
.gr3{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(22,32,43,.08);min-height:0}
.gh3{display:grid;grid-template-columns:100px 1fr;gap:8px}.gh3 .hs{display:flex}.gh3 .hs span{flex:1;font:600 13px/1.3 'DM Sans';color:#66727f}
.gl3{flex:1;display:grid;grid-template-columns:100px 1fr;gap:8px;align-items:center}.gl3 b{font:700 16px/1.3 Montserrat}
.tr3{position:relative;height:100%;min-height:44px;border-radius:10px;background:repeating-linear-gradient(90deg,#f3f6fa 0 calc(100%/12 - 2px),#e6ecf2 calc(100%/12 - 2px) calc(100%/12))}
.bk3{position:absolute;top:4px;bottom:4px;border-radius:8px;padding:0 8px;display:flex;align-items:center;font:700 13px/1.25 'DM Sans';color:#fff;overflow:hidden}
.bk3.op{background:#3a7dc2}.bk3.pv{background:#1d4f8a}.bk3.lg{background:#6a4fb3}.bk3.ls{background:#2c8f6a}
.nw3{position:absolute;top:0;bottom:0;width:3px;background:#e2463a;z-index:0}.bk3{z-index:1}
.fm3{background:#16202b;color:#fff;border-radius:22px;padding:14px 20px;display:grid;grid-template-columns:auto repeat(3,1fr) auto;gap:14px;align-items:center}.fm3 .sm3{color:#a9b6c4}
.fm3 small{display:block;font:500 13px/1.3 'DM Sans';color:#a9b6c4}.fm3 b{font:700 17px/1.3 'DM Sans'}.fm3 .bt{background:#f3e24a;color:#16202b;border-radius:12px;padding:12px 16px;font:800 16px/1.2 Montserrat;white-space:nowrap}
""", "<div class=kk>PICKLEBALL COURTS · BOOKINGS</div><h1>Court times by group text?<br><span>Let players book online.</span></h1>",
f'''<div class=vw><div class=ct3>{"".join(f'<div class=cc3><div class=cw>{court3(stat3(i)[1])}</div><b>{c}</b><span class="k-{stat3(i)[1]}">{stat3(i)[0]}</span></div>' for i, c in enumerate(CT3))}</div>
<div class=gr3><span class=sm3>TONIGHT · 4-10 PM · NOW 6:15 PM · SAMPLE</span><div class=gh3><span></span><div class=hs>{"".join(f"<span>{h - 12} PM</span>" for h in HR3)}</div></div>
{"".join(f'<div class=gl3><b>{c}</b><div class=tr3>' + "".join(f'<div class="bk3 {k}" style="left:calc({(a - 16) / 6 * 100:.2f}% + 2px);width:calc({(b - a) / 6 * 100:.2f}% - 4px)">{t}</div>' for cc, a, b, t, k in SC3 if cc == i) + f'<i class=nw3 style="left:{(NOW3 - 16) / 6 * 100:.2f}%"></i></div></div>' for i, c in enumerate(CT3))}</div>
<div class=fm3><span class=sm3>BOOK<br>A COURT</span>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a, b in [("Court", "Court 3"), ("Time", "8:30-10:00 PM"), ("Players", "4 · paddles: own")])}<span class=bt>Book now</span></div></div>''',
"#16202b", "Run courts or a club? DM us", "background:#1d4f8a;color:#fff")


# ───────── 405 INDIA · Parking lot (monthly passes) · SINGLE · TeX Gyre Adventor + DM Sans · asphalt / parking blue / line white
# New technique: top-down CSS parking lot (painted bays, drive lane arrows) where pass-holder cars, daily cars and empty bays
# are coloured from one bay list; the counts tile and the expiring-pass list come from the same data.
R5 = random.Random(405)
BAY5 = []
for i in range(30):
    r = R5.random(); BAY5.append("P" if r < .5 else ("D" if r < .78 else "E"))
for _b in (3, 10, 16, 21): BAY5[_b] = "P"
CNT5 = {k: BAY5.count(k) for k in "PDE"}
PS5 = [("XX 01 AB 1234", "Bay 4", "Sat 28 Nov", "Renew reminder sent"), ("XX 02 CD 5678", "Bay 11", "Mon 30 Nov", "Renew reminder sent"),
       ("XX 01 EF 9012", "Bay 17", "Tue 1 Dec", "Renewed by UPI"), ("XX 03 GH 3456", "Bay 22", "Fri 4 Dec", "Reminder on Wed")]
def car5(k, i):
    if k == "E": return f'<div class="by5 e"><span>{i + 1}</span></div>'
    col = R5.choice(["#e0e4ea", "#c7302b", "#2c2f36", "#3f6fb5", "#d9d2c3"])
    return f'<div class="by5 {k.lower()}"><div class=car style="background:{col}"><i></i><i></i></div><span>{i + 1}</span></div>'
P["p405_parking"] = page("""
body{--f:'DM Sans';--h:'TeX Gyre Adventor';background:#eef1f5;color:#1d232b}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#1f6fd1;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#1f6fd1}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm5{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#6b7480}
.lt5{background:#3a3f47;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}.lt5 .sm5{color:#c5ccd6}
.rw5{display:grid;grid-template-columns:repeat(15,1fr);gap:0}
.by5{height:112px;border-left:3px solid #f4f4f0;position:relative;display:flex;align-items:center;justify-content:center}.rw5 .by5:last-child{border-right:3px solid #f4f4f0}
.by5 span{position:absolute;font:700 12px/1 'DM Sans';color:#c5ccd6}.rw5.t .by5 span{bottom:4px}.rw5.b .by5 span{top:4px}
.by5 .car{width:38px;height:76px;border-radius:12px 12px 9px 9px;position:relative;box-shadow:0 4px 8px rgba(0,0,0,.35)}
.by5 .car i{position:absolute;left:5px;right:5px;height:14px;border-radius:4px;background:rgba(20,30,45,.55)}.by5 .car i:first-child{top:12px}.by5 .car i:last-child{bottom:10px}
.by5.p{background:rgba(31,111,209,.38)}.by5.d{background:rgba(242,184,48,.22)}.by5.e{background:transparent}
.ln5{height:46px;display:flex;align-items:center;justify-content:space-around;font:700 22px/1 'DM Sans';color:#f4f4f0;letter-spacing:6px}
.lg5{display:flex;gap:16px}.lg5 span{display:flex;gap:6px;align-items:center;font:600 14px/1.2 'DM Sans';color:#e3e7ec}.lg5 i{width:16px;height:16px;border-radius:4px}
.lt5 .h{display:flex;justify-content:space-between;align-items:center}
.bt5{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:14px;min-height:0}
.ct5{display:flex;flex-direction:column;gap:10px}.ct5>div{flex:1;background:#fff;border-radius:20px;padding:12px 18px;display:flex;align-items:center;gap:14px;box-shadow:0 12px 26px rgba(29,35,43,.08)}
.ct5 b{font:700 54px/1.2 'TeX Gyre Adventor'}.ct5 span{font:600 17px/1.3 'DM Sans';color:#4f5864}
.ps5{background:#fff;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 12px 26px rgba(29,35,43,.08)}
.pr5{flex:1;display:grid;grid-template-columns:1.5fr .8fr 1.5fr;gap:10px;align-items:center;border-top:1px solid #edf0f4}
.np5{font:700 17px/1.2 'DM Sans';background:#fff;border:2px solid #1d232b;border-radius:6px;padding:6px 8px;text-align:center;letter-spacing:1px;white-space:nowrap}
.pr5 span{font:500 16px/1.3 'DM Sans';color:#4f5864}.pr5 div b{display:block;font:700 16px/1.3 'DM Sans'}.pr5 div span{font-size:14px}
.ok5{color:#1f7a47}.wt5{color:#b06a00}
""", "<div class=kk>PARKING LOT · MONTHLY PASSES</div><h1>Monthly passes on paper slips?<br><span>See bays, passes and dues.</span></h1>",
f'''<div class=vw><div class=lt5><div class=h><span class=sm5>LOT A · 30 BAYS · NOW · SAMPLE</span><div class=lg5><span><i style="background:#1f6fd1"></i>Monthly pass</span><span><i style="background:#f2b830"></i>Daily</span><span><i style="border:2px solid #c5ccd6"></i>Empty</span></div></div>
<div class="rw5 t">{"".join(car5(k, i) for i, k in enumerate(BAY5[:15]))}</div><div class=ln5><span>→</span><span>→</span><span>→</span><span>→</span></div><div class="rw5 b">{"".join(car5(k, i + 15) for i, k in enumerate(BAY5[15:]))}</div></div>
<div class=bt5><div class=ct5>{"".join(f'<div><b style="color:{c}">{CNT5[k]}</b><span>{t}</span></div>' for k, t, c in [("P", "monthly pass cars in", "#1f6fd1"), ("D", "daily cars in", "#b07a00"), ("E", "bays free now", "#1d232b")])}</div>
<div class=ps5><span class=sm5>PASSES ENDING SOON</span>{"".join(f'<div class=pr5><span class=np5>{v}</span><span>{b}</span><div><b>Ends {d}</b><span class="{"ok5" if "Renewed" in s else "wt5"}">{s}</span></div></div>' for v, b, d, s in PS5)}</div></div></div>''',
"#1d232b", "Run a parking lot? DM us", "background:#1f6fd1;color:#fff")


# ───────── 401 INDIA · Jute bag maker · CAROUSEL 5 · Bitter + DM Sans · jute natural / screen-print green / ink black
# New technique: CSS jute bags (two-way weave from crossed repeating gradients, webbing handles as bordered half-loops,
# gusset side panel) and a stage funnel of horizontal bars where each stage can never exceed the one before it.
def bag1(w, h, txt="SAMPLE PRINT", col="#2f6b45", hd=True):
    weave = "repeating-linear-gradient(0deg,rgba(120,86,40,.20) 0 2px,transparent 2px 5px),repeating-linear-gradient(90deg,rgba(120,86,40,.18) 0 2px,transparent 2px 5px)"
    hnd = f'<i class="hd1 free" style="left:{w * .2:.0f}px;width:{w * .22:.0f}px;height:{h * .32:.0f}px;top:-{h * .32 - 4:.0f}px"></i><i class="hd1 free" style="right:{w * .2:.0f}px;width:{w * .22:.0f}px;height:{h * .32:.0f}px;top:-{h * .32 - 4:.0f}px"></i>' if hd else ""
    return f'<div class=bg1 style="width:{w}px;height:{h}px;background:{weave},linear-gradient(#d8b781,#c9a46a)">{hnd}<div class=pr1 style="border-color:{col};color:{col}">{txt}</div></div>'
B1 = """
body{--f:'DM Sans';--h:'Bitter';background:#f4eee2;color:#1f1d1a;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#2f6b45;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1px} h1 span{color:#2f6b45}
.cd1{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(31,29,26,.08)}
.sm1{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7a6f5c}
.bg1{position:relative;border-radius:4px 4px 10px 10px;box-shadow:inset 0 -8px 0 rgba(120,86,40,.18),0 14px 24px rgba(60,40,15,.18);display:flex;align-items:center;justify-content:center;flex:none}
.hd1{position:absolute;border:7px solid #e9dcc2;border-bottom:0;border-radius:60px 60px 0 0;display:block}
.pr1{border:3px dashed;border-radius:8px;padding:10px 12px;font:800 15px/1.3 'DM Sans';letter-spacing:1px;text-align:center;max-width:78%}
.bb1{background:#1f1d1a;color:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}.bb1 b{font:700 21px/1.3 'DM Sans'}.bb1 span{font:500 17px/1.35 'DM Sans';color:#d3cab8}
"""
def t1(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f1d1a;color:#e9d9b4"):
    return page(B1 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f1d1a", cta, ctacss, tagline=f"{n} / 5")
OD1 = dict(id="J-208", who="Sample Bookstore", size="14 × 16 in", gus="4 in gusset", hnd="Cotton webbing, 24 in", lam="Inside lamination", prn="2 colours, front only", qty=500, due="Fri 4 Dec")
P["p401_jute_s1"] = t1(1, "JUTE BAG MAKER · CUSTOM ORDERS", "Bag order lost in a long chat?<br><span>Size, print and qty in one place.</span>",
f'''<div class=w11><div class="cd1 sh11"><span class=sm1>THE SAME ORDER, SPREAD OVER A CHAT · SAMPLE</span><div class=bgs>{bag1(330, 390, "PRINT?<br>WHICH ONE?")}{bag1(260, 310, "SIZE?<br>14 OR 16 IN?", "#b2462e")}{bag1(210, 250, "QTY?<br>500 OR 600?", "#1f1d1a")}</div></div>
<div class=pn11>{"".join(f'<div class=bb1><b>{a}</b><span>{b}</span></div>' for a, b in [("“Which logo file was final?”", "Sent 3 times in chat"), ("“Handles 22 or 24 inches?”", "Said on a call"), ("“How many are ready?”", "Count the pile again")])}</div></div>''',
css=""".w11{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sh11{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:10px}
.sh11 .bgs{flex:1;display:flex;align-items:flex-end;justify-content:space-around;padding:20px 10px 20px}.sh11 .pr1{font-size:19px}.pn11{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}""")
def plan1():
    return f'''<svg viewBox="0 0 420 330" width="420" style="display:block;width:100%;height:auto"><rect x="70" y="70" width="210" height="240" rx="6" fill="#d3b07a" stroke="#8a6a3a" stroke-width="3"/>
<rect x="300" y="70" width="60" height="240" rx="4" fill="#c49d63" stroke="#8a6a3a" stroke-width="3"/><path d="M110 72 C110 10 150 10 150 72" fill="none" stroke="#e9dcc2" stroke-width="9"/><path d="M200 72 C200 10 240 10 240 72" fill="none" stroke="#e9dcc2" stroke-width="9"/>
<rect x="110" y="150" width="130" height="80" rx="6" fill="none" stroke="#2f6b45" stroke-width="3" stroke-dasharray="8 6"/><text x="175" y="196" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#2f6b45">Print area</text>
<line x1="70" y1="322" x2="280" y2="322" stroke="#1f1d1a" stroke-width="2"/><text x="175" y="318" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#1f1d1a">14 in</text>
<line x1="44" y1="70" x2="44" y2="310" stroke="#1f1d1a" stroke-width="2"/><text x="38" y="196" text-anchor="end" font-family="DM Sans" font-weight="700" font-size="15" fill="#1f1d1a">16 in</text>
<text x="330" y="196" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="14" fill="#1f1d1a">4 in</text><text x="330" y="60" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="13" fill="#6b5f4b">Side</text>
<text x="175" y="20" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="13" fill="#6b5f4b">Handles 24 in</text></svg>'''
P["p401_jute_s2"] = t1(2, "1 · ONE ORDER CARD", "Every detail, written once.<br><span>Seen by cutting and printing.</span>",
f'''<div class=w12><div class="cd1 dw12"><span class=sm1>{OD1["id"]} · FRONT AND SIDE</span><div class=pw>{plan1()}</div><span class=sm1>MATERIALS</span><div class=mt>{"".join(f'<div><i style="background:{bg}"></i><b>{a}</b><span>{b}</span></div>' for bg, a, b in [("repeating-linear-gradient(0deg,rgba(120,86,40,.25) 0 2px,transparent 2px 5px),repeating-linear-gradient(90deg,rgba(120,86,40,.22) 0 2px,transparent 2px 5px),#d3b07a", "Jute fabric", "Natural"), ("repeating-linear-gradient(90deg,#efe3c9 0 4px,#e2d2b0 4px 6px)", "Webbing", "Cotton, cream"), ("linear-gradient(135deg,#f4f4f2,#d9dde0)", "Lining", "Inside lamination")])}</div></div>
<div class=oc12><div class=hd><b>{OD1["id"]}</b><span>ORDER CARD · SAMPLE</span></div>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Buyer", OD1["who"]), ("Size", f'{OD1["size"]}, {OD1["gus"]}'), ("Handles", OD1["hnd"]), ("Inside", OD1["lam"]), ("Print", OD1["prn"]), ("Quantity", f'{OD1["qty"]} bags'), ("Delivery", OD1["due"])])}</div></div>''',
css=""".w12{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}.dw12{padding:18px 20px;display:flex;flex-direction:column;gap:10px}.dw12 .pw{flex:1;display:flex;align-items:center}.dw12 .mt{display:flex;flex-direction:column;gap:8px}.dw12 .mt>div{display:grid;grid-template-columns:56px 1fr;grid-template-rows:auto auto;column-gap:12px;align-items:center}.dw12 .mt i{grid-row:span 2;width:56px;height:44px;border-radius:8px;display:block;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}.dw12 .mt b{font:700 17px/1.3 "DM Sans"}.dw12 .mt span{font:500 15px/1.3 "DM Sans";color:#6b5f4b}
.oc12{background:#1f1d1a;color:#fff;border-radius:24px;padding:20px 22px;display:flex;flex-direction:column;gap:4px}.oc12 .hd{display:flex;justify-content:space-between;align-items:center;padding-bottom:6px}.oc12 .hd b{font:800 32px/1.3 Bitter;color:#e9d9b4}.oc12 .hd span{font:700 13px/1.3 'DM Sans';letter-spacing:2px;color:#a89f8c}
.oc12 .r{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1px solid rgba(255,255,255,.12)}.oc12 .r span{font:500 15px/1.3 'DM Sans';color:#b9b09d}.oc12 .r b{font:700 20px/1.3 'DM Sans'}""")
PN1 = [(46, 18, "1", "Move text up a little"), (80, 72, "2", "Use the darker green"), (30, 74, "3", "Add the website line")]
P["p401_jute_s3"] = t1(3, "2 · PRINT PROOF, APPROVED IN THE APP", "Proof, comments, approval.<br><span>No more “final_final” files.</span>",
f'''<div class=w13><div class="cd1 pf13"><span class=sm1>{OD1["id"]} · PROOF v2</span><div class=bw><div style="position:relative">{bag1(400, 480, "SAMPLE BOOKSTORE<br>READ MORE")}{"".join(f'<i class=pin style="left:{x}%;top:{y}%">{n}</i>' for x, y, n, _ in PN1)}</div></div></div>
<div class=rt13><div class="cd1 cm13"><span class=sm1>BUYER COMMENTS ON v1</span>{"".join(f'<div class=c><i>{n}</i><span>{t}</span><em>Done in v2</em></div>' for _, _, n, t in PN1)}</div>
<div class="cd1 hs13"><span class=sm1>PROOF HISTORY</span>{"".join(f'<div class=h><b>{a}</b><span>{b}</span></div>' for a, b in [("v1 · Mon 16 Nov", "3 comments"), ("v2 · Wed 18 Nov", "Sent to buyer"), ("Approved · Thu 19 Nov", "Printing can start")])}</div></div></div>''',
css=""".w13{flex:1;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:16px;min-height:0}.pf13{padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.pf13 .bw{flex:1;display:flex;align-items:flex-end;justify-content:center;padding:20px 0 20px}.pf13 .pr1{font-size:18px}
.pin{position:absolute;width:40px;height:40px;border-radius:50% 50% 50% 4px;background:#d9472b;color:#fff;font:800 18px/40px 'DM Sans';font-style:normal;text-align:center;box-shadow:0 6px 12px rgba(0,0,0,.2)}
.rt13{display:flex;flex-direction:column;gap:14px}.cm13{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:6px}.cm13 .c{flex:1;display:flex;gap:12px;align-items:center;}
.cm13 .c{border-top:1px solid #efe8da}.cm13 .c i{width:36px;height:36px;border-radius:50%;background:#d9472b;color:#fff;font:800 16px/36px 'DM Sans';font-style:normal;text-align:center;flex:none}.cm13 .c span{flex:1;font:600 19px/1.35 'DM Sans'}.cm13 .c em{font:700 14px/1.2 'DM Sans';font-style:normal;background:#e1efe5;color:#2f6b45;border-radius:10px;padding:7px 9px;white-space:nowrap}
.hs13{padding:18px 20px;display:flex;flex-direction:column;gap:8px}.hs13 .h{display:flex;justify-content:space-between;gap:10px;border-top:1px solid #efe8da;padding-top:8px}.hs13 b{font:700 18px/1.3 'DM Sans'}.hs13 span{font:500 17px/1.3 'DM Sans';color:#6b5f4b}""")
FN1 = [("Cut", 500), ("Printed", 500), ("Stitched", 320), ("Handles on", 260), ("Checked", 200), ("Packed", 150)]
P["p401_jute_s4"] = t1(4, "3 · COUNT EVERY STAGE", "“How many are ready?”<br><span>See it at every stage.</span>",
f'''<div class=w14><div class="cd1 fn14"><span class=sm1>{OD1["id"]} · {OD1["qty"]} BAGS · TODAY · SAMPLE</span>{"".join(f'<div class=r><b>{a}</b><div class=br><i style="width:{n / OD1["qty"] * 100:.0f}%"></i></div><em>{n}</em></div>' for a, n in FN1)}</div>
<div class=bt14><div class="cd1 ms14"><span class=sm1>UPDATE TO BUYER · 6 PM</span><p>{OD1["id"]}: {FN1[-1][1]} of {OD1["qty"]} bags packed today. All {OD1["qty"]} on track for {OD1["due"]}.</p></div>
<div class="cd1 nx14"><span class=sm1>TOMORROW</span><p>Stitching line: finish the last {OD1["qty"] - FN1[2][1]} bags first.</p></div></div></div>''',
css=""".w14{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.fn14{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:6px}
.fn14 .r{flex:1;display:grid;grid-template-columns:150px 1fr 70px;gap:14px;align-items:center}.fn14 b{font:700 21px/1.3 'DM Sans'}.fn14 em{font:800 28px/1.3 Bitter;font-style:normal;text-align:right}
.fn14 .br{height:46px;border-radius:12px;background:#efe8da;overflow:hidden}.fn14 .br i{display:block;height:100%;background:repeating-linear-gradient(90deg,#2f6b45 0 calc(10% - 3px),transparent calc(10% - 3px) 10%);background-size:100% 100%;border-radius:12px 0 0 12px}
.bt14{display:grid;grid-template-columns:1.4fr 1fr;gap:14px}.ms14{padding:16px 20px;display:flex;flex-direction:column;gap:8px;background:#e5f0e8}.ms14 p{font:500 20px/1.45 'DM Sans';text-wrap:pretty}
.nx14{padding:16px 20px;display:flex;flex-direction:column;gap:8px}.nx14 p{font:600 20px/1.45 'DM Sans'}""")
P["p401_jute_s5"] = t1(5, "JUTE BAG ORDER APP", "Make jute or cloth bags?<br><span>Let's build your order app.</span>",
f'''<div class=w15><div class=bgs>{bag1(210, 300, "ORDER<br>CARDS")}{bag1(210, 300, "PROOF<br>APPROVAL", "#b2462e")}{bag1(210, 300, "STAGE<br>COUNTS", "#1f1d1a")}{bag1(210, 300, "BUYER<br>UPDATES")}</div>
<div class=q15><span class=sm1>A QUESTION FOR BAG MAKERS</span><p>Where do your bag orders live today: chats, a diary or a sheet? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss="background:#2f6b45;color:#fff",
css=""".w15{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}.bgs{flex:1;display:flex;align-items:center;justify-content:space-around;padding-top:70px}.bgs .pr1{font-size:18px}
.q15{background:#1f1d1a;color:#fff;border-radius:24px;padding:28px 30px;display:flex;flex-direction:column;gap:12px}.q15 .sm1{color:#e9d9b4}.q15 p{font:700 32px/1.35 Bitter;text-wrap:pretty}""")


# ───────── 404 INDIA · Coworking space · CAROUSEL 5 · Cardo + Roboto · desk oak / ink navy / coral
# New technique: CSS floor plan of a coworking floor (desk clusters, cabins, meeting room) with each seat coloured by plan,
# plus a meeting-room hours meter per member; all slides read one member list.
F4 = "#24324a"; C4 = "#e8634a"; O4 = "#c79a62"
DESK4 = ["d", "d", "h", "h", "f", "d", "h", "f", "d", "h", "h", "f", "d", "d", "h", "f"]
def floor4():
    cols = {"d": F4, "h": "#7da0c9", "f": "#e8e2d6"}
    cl = "".join(f'<div class=cl4>{"".join(f"""<i style="background:{cols[DESK4[c * 4 + k]]}"></i>""" for k in range(4))}</div>' for c in range(4))
    cab = "".join(f'<div class="cb4 {"f" if i == 2 else ""}"><b>Cabin {i + 1}</b><span>{"Free from 1 Dec" if i == 2 else "4 seats · taken"}</span></div>' for i in range(3))
    return f'<div class=fl4><div class=dk4>{cl}</div><div class=cs4>{cab}</div><div class=mr4><b>Meeting room</b><span>In use till 12:00</span></div><div class=rc4><b>Front desk</b></div></div>'
B4 = f"""
body{{--f:'Roboto';--h:'Cardo';background:#f5f0e8;color:{F4};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{C4};margin-top:22px}}
h1{{font-family:'Cardo';font-weight:700;font-size:62px;line-height:1.2}} h1 span{{color:{C4}}}
.cd4{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(36,50,74,.08)}}
.sm4{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#6d7483}}
.fl4{{flex:1;display:grid;grid-template-columns:1.6fr 1fr;grid-template-rows:1fr auto;gap:14px;background:#efe7da;border-radius:18px;padding:16px;border:6px solid {O4}}}
.dk4{{display:grid;grid-template-columns:1fr 1fr;gap:16px;background:#fbf8f2;border-radius:12px;padding:16px}}
.cl4{{display:grid;grid-template-columns:1fr 1fr;gap:6px;padding:10px;border-radius:10px;background:{O4}}}.cl4 i{{border-radius:6px;min-height:52px;display:block}}
.cs4{{display:flex;flex-direction:column;gap:10px}}.cb4{{flex:1;background:{F4};color:#fff;border-radius:12px;padding:10px 14px;display:flex;flex-direction:column;justify-content:center;gap:2px}}.cb4.f{{background:#fff;color:{F4};border:3px dashed {C4}}}
.cb4 b{{font:700 19px/1.3 Roboto}}.cb4 span{{font:500 14px/1.3 Roboto;opacity:.8}}
.mr4{{background:{C4};color:#fff;border-radius:12px;padding:12px 16px;display:flex;justify-content:space-between;align-items:center}}.mr4 b{{font:700 19px/1.3 Roboto}}.mr4 span{{font:600 15px/1.3 Roboto}}
.rc4{{background:#fbf8f2;border-radius:12px;padding:12px 16px;display:flex;align-items:center}}.rc4 b{{font:700 17px/1.3 Roboto;color:#6d7483}}
.lg4{{display:flex;gap:16px;flex-wrap:wrap}}.lg4 span{{display:flex;gap:6px;align-items:center;font:600 15px/1.2 Roboto;color:#4b5363}}.lg4 i{{width:16px;height:16px;border-radius:4px}}
.bb4{{background:{F4};color:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}}.bb4 b{{font:700 20px/1.3 Roboto}}.bb4 span{{font:500 16px/1.35 Roboto;color:#c3cbd9}}
"""
def t4(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{F4};color:#fff"):
    return page(B4 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, F4, cta, ctacss, tagline=f"{n} / 5")
LEG4 = f'<div class=lg4><span><i style="background:{F4}"></i>Fixed desk</span><span><i style="background:#7da0c9"></i>Hot desk today</span><span><i style="background:#e8e2d6;border:1px solid #cfc6b6"></i>Free</span></div>'
NF4 = DESK4.count("f")
P["p404_cowork_s1"] = t4(1, "COWORKING SPACE · DESKS AND ROOMS", "“Is a desk free today?”<br><span>See the whole floor live.</span>",
f'''<div class=w41><div class="cd4 fc41"><div class=h><span class=sm4>FLOOR 2 · 16 DESKS · 3 CABINS · SAMPLE</span>{LEG4}</div>{floor4()}</div>
<div class=pn41>{"".join(f'<div class=bb4><b>{a}</b><span>{b}</span></div>' for a, b in [(f"{NF4} desks free today", "Owner knew only after a walk"), ("Room booked twice", "Two teams at 11 AM"), ("Who has paid?", "Checked in a notebook")])}</div></div>''',
css=""".w41{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.fc41{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:12px}.fc41 .h{display:flex;justify-content:space-between;align-items:center;gap:10px}
.pn41{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}""")
SL4 = [("9:00", "10:00", "Sample Studio", "b"), ("10:00", "10:30", "", "f"), ("10:30", "12:00", "Sample Startup", "b"), ("12:00", "13:00", "", "f"), ("13:00", "14:00", "Sample Agency", "b"), ("14:00", "16:00", "", "f"), ("16:00", "17:00", "Sample Freelancer", "b"), ("17:00", "18:00", "", "f")]
def mins4(t): h, m = map(int, t.split(":")); return h * 60 + m
HRS4 = [("Sample Startup", 10, 7), ("Sample Studio", 6, 2), ("Sample Agency", 6, 5), ("Sample Freelancer", 2, 1)]
P["p404_cowork_s2"] = t4(2, "1 · MEETING ROOM BY THE SLOT", "No more double bookings.<br><span>Members book free slots.</span>",
f'''<div class=w42><div class="cd4 dy42"><span class=sm4>MEETING ROOM · TUE 24 NOV · SAMPLE</span>{"".join(f'<div class="sl {k}" style="flex:{(mins4(b) - mins4(a)) / 30}"><span>{a}</span><b>{w if w else "Free · tap to book"}</b><em>{a}-{b}</em></div>' for a, b, w, k in SL4)}</div>
<div class=rt42><div class="cd4 hr42"><span class=sm4>ROOM HOURS THIS MONTH · BY PLAN</span>{"".join(f'<div class=r><div class=t><b>{m}</b><span>{u} of {t} hours used</span></div><div class=br><i style="width:{u / t * 100:.0f}%"></i></div></div>' for m, t, u in HRS4)}</div>
<div class="cd4 cf42"><span class=sm4>BOOKING CONFIRMED</span><p>Meeting room, Tue 24 Nov, 10:30 AM to 12:00 PM, Sample Startup. 1.5 hours added to this month.</p></div></div></div>''',
css=f""".w42{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:16px;min-height:0}}.dy42{{padding:16px 18px;display:flex;flex-direction:column;gap:6px}}
.dy42 .sl{{border-radius:12px;padding:6px 14px;display:grid;grid-template-columns:56px 1fr;grid-template-rows:auto auto;column-gap:10px;align-content:center;min-height:0}}.dy42 .sl span{{grid-row:span 2;font:700 15px/1.3 Roboto;color:#6d7483;align-self:center}}
.dy42 .sl b{{font:700 17px/1.3 Roboto}}.dy42 .sl em{{font:500 13px/1.3 Roboto;font-style:normal;color:#6d7483}}.dy42 .sl.b{{background:{F4}}}.dy42 .sl.b b{{color:#fff}}.dy42 .sl.b span,.dy42 .sl.b em{{color:#b9c3d4}}.dy42 .sl.f{{background:#fff;border:2px dashed #d5cdbf}}.dy42 .sl.f b{{color:{C4}}}
.rt42{{display:flex;flex-direction:column;gap:14px}}.hr42{{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:8px}}.hr42 .r{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:1px solid #efe9df}}
.hr42 .t{{display:flex;justify-content:space-between;gap:10px}}.hr42 b{{font:700 18px/1.3 Roboto}}.hr42 .t span{{font:500 16px/1.3 Roboto;color:#6d7483}}.hr42 .br{{height:14px;border-radius:7px;background:#efe9df;overflow:hidden}}.hr42 .br i{{display:block;height:100%;background:{C4}}}
.cf42{{padding:16px 20px;display:flex;flex-direction:column;gap:8px;background:#fdebe6}}.cf42 p{{font:500 19px/1.45 Roboto;text-wrap:pretty}}""")
def qr4():
    R = random.Random(404); out = []
    for i in range(81):
        r, c = divmod(i, 9)
        fz = any(r0 <= r < r0 + 3 and c0 <= c < c0 + 3 for r0, c0 in [(0, 0), (0, 6), (6, 0)])
        k = (fz and not (r % 6 == 1 and c % 6 == 1)) if fz else R.random() < .45
        out.append(f'<i class="{"k" if k else ""}"></i>')
    return "".join(out)
QR4 = qr4()
VS4 = [("Sample Visitor 1", "Sample Startup", "10:15 AM", "In"), ("Sample Visitor 2", "Sample Agency", "12:40 PM", "Expected"), ("Sample Courier", "Sample Studio", "2:00 PM", "Expected"), ("Sample Visitor 3", "Sample Freelancer", "4:30 PM", "Expected")]
P["p404_cowork_s3"] = t4(3, "2 · VISITORS WITH A PASS", "Guests at the front desk?<br><span>Members add them first.</span>",
f'''<div class=w43><div class=ps43><div class=hd><span>VISITOR PASS</span><b>V-0412</b></div><div class=qr>{QR4}</div>
{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Name", "Sample Visitor 1"), ("Meeting", "Sample Startup"), ("Date", "Tue 24 Nov"), ("Time", "10:15 AM"), ("Room", "Meeting room")])}</div>
<div class="cd4 lg43"><span class=sm4>TODAY AT THE FRONT DESK · SAMPLE</span>{"".join(f'<div class=r><div><b>{n}</b><span>for {m}</span></div><em>{t}</em><i class="{"in" if s == "In" else ""}">{s}</i></div>' for n, m, t, s in VS4)}<div class=nt>Members add a guest in the app. The guest gets a pass by message and shows it at the desk.</div></div></div>''',
css=f""".w43{{flex:1;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:16px;min-height:0}}
.ps43{{background:{F4};color:#fff;border-radius:24px;padding:22px;display:flex;flex-direction:column;gap:8px}}.ps43 .hd{{display:flex;justify-content:space-between;align-items:center}}.ps43 .hd span{{font:700 14px/1.3 Roboto;letter-spacing:2px;color:#b9c3d4}}.ps43 .hd b{{font:700 26px/1.3 Cardo;color:#ffb19f}}
.ps43 .qr{{align-self:center;width:210px;height:210px;background:#fff;border-radius:12px;padding:12px;display:grid;grid-template-columns:repeat(9,1fr);gap:2px;margin:6px 0}}.ps43 .qr i{{display:block;background:#fff}}.ps43 .qr i.k{{background:{F4}}}
.ps43 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.14);gap:10px}}.ps43 .r span{{font:500 16px/1.3 Roboto;color:#b9c3d4}}.ps43 .r b{{font:700 18px/1.3 Roboto}}
.lg43{{padding:16px 20px;display:flex;flex-direction:column;gap:6px}}.lg43 .r{{flex:1;display:grid;grid-template-columns:1fr auto auto;gap:12px;align-items:center;border-top:1px solid #efe9df}}
.lg43 b{{display:block;font:700 19px/1.3 Roboto}}.lg43 .r span{{font:500 15px/1.3 Roboto;color:#6d7483}}.lg43 em{{font:700 17px/1.3 Roboto;font-style:normal}}.lg43 .r i{{font:700 14px/1.2 Roboto;font-style:normal;background:#f1ece3;color:#6d7483;border-radius:10px;padding:7px 10px}}.lg43 .r i.in{{background:#e2f1e6;color:#1f6b3a}}
.lg43 .nt{{background:#fdebe6;border-radius:14px;padding:12px 14px;font:500 17px/1.45 Roboto}}""")
IV4 = [("Sample Startup", "Cabin 1 · 4 seats", "Paid by UPI · 2 Nov"), ("Sample Studio", "3 fixed desks", "Paid by bank · 4 Nov"), ("Sample Agency", "Cabin 2 · 4 seats", "Due · reminder sent"), ("Sample Freelancer", "Hot desk · 10 days", "Paid by UPI · 1 Nov"), ("Sample Designer", "1 fixed desk", "Due · reminder sent")]
P["p404_cowork_s4"] = t4(4, "3 · MONTHLY BILLS WITHOUT CHASING", "Bills made on the 1st.<br><span>Reminders go out on time.</span>",
f'''<div class=w44><div class="cd4 iv44"><span class=sm4>NOVEMBER BILLS · NO AMOUNTS SHOWN · SAMPLE</span>{"".join(f'<div class=r><div><b>{m}</b><span>{p}</span></div><em class="{"du" if s.startswith("Due") else ""}">{s}</em></div>' for m, p, s in IV4)}</div>
<div class=bt44><div class="cd4 rm44"><span class=sm4>AUTO REMINDER · SAMPLE AGENCY</span><p>Your November bill for Cabin 2 is due. Pay by UPI or bank transfer. The tax invoice is attached.</p></div>
<div class=cn44>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [(str(sum(1 for x in IV4 if not x[2].startswith("Due"))), "bills paid"), (str(sum(1 for x in IV4 if x[2].startswith("Due"))), "reminders sent")])}</div></div></div>''',
css=f""".w44{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.iv44{{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:4px}}
.iv44 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:12px;border-top:1px solid #efe9df}}.iv44 b{{display:block;font:700 22px/1.3 Roboto}}.iv44 span{{font:500 17px/1.3 Roboto;color:#6d7483}}
.iv44 em{{font:700 16px/1.2 Roboto;font-style:normal;background:#e2f1e6;color:#1f6b3a;border-radius:10px;padding:9px 12px}}.iv44 em.du{{background:#fdebe6;color:#b23a22}}
.bt44{{display:grid;grid-template-columns:1.5fr 1fr;gap:14px}}.rm44{{padding:16px 20px;display:flex;flex-direction:column;gap:8px;background:#fdebe6}}.rm44 p{{font:500 19px/1.45 Roboto;text-wrap:pretty}}
.cn44{{display:flex;flex-direction:column;gap:10px}}.cn44>div{{flex:1;background:{F4};color:#fff;border-radius:18px;padding:10px 18px;display:flex;align-items:center;gap:12px}}.cn44 b{{font:700 40px/1.2 Cardo;color:#ffb19f}}.cn44 span{{font:600 17px/1.3 Roboto}}""")
P["p404_cowork_s5"] = t4(5, "COWORKING SPACE APP", "Run a coworking space?<br><span>Let's build your desk app.</span>",
f'''<div class=w45><div class=tl45>{"".join(f'<div class=cd4><span class=ib>{ic(i, 36)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("grid", "Live floor plan", "Desks and cabins"), ("cal", "Room booking", "Hours per plan"), ("qr", "Visitor passes", "Sent by message"), ("doc", "Monthly bills", "With reminders")])}</div>
<div class=q45><span class=sm4>A QUESTION FOR SPACE OWNERS</span><p>How do members book the meeting room today: a chat group, a sheet or the front desk? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{C4};color:#fff",
css=f""".w45{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl45{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl45>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl45 .ib{{width:80px;height:80px;border-radius:22px;background:{F4};color:#ffb19f}}.tl45 b{{font:700 38px/1.3 Cardo}}.tl45 span{{font:500 22px/1.4 Roboto;color:#6d7483}}
.q45{{background:{F4};color:#fff;border-radius:26px;padding:26px 30px;display:flex;flex-direction:column;gap:12px}}.q45 .sm4{{color:#ffb19f}}.q45 p{{font:700 30px/1.4 Cardo;text-wrap:pretty}}""")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
