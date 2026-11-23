import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 411 INDIA · Tarpaulin maker · SINGLE · Anton + DM Sans · tarp blue / safety orange / rope beige
# New technique: before/after slider (diary half vs app half with matching rows and a round handle) over a to-scale SVG
# tarp whose eyelets are placed every 3 ft around the edge; the eyelet count on the card is counted from the drawing.
B1 = "#1f5fa8"; O1 = "#f07c1f"; K1 = "#17212e"
TW1, TH1, EV1 = 18, 24, 3
def eyelets1():
    pts = []
    for i in range(0, TW1 + 1, EV1): pts += [(i, 0), (i, TH1)]
    for j in range(EV1, TH1, EV1): pts += [(0, j), (TW1, j)]
    return sorted(set(pts))
EY1 = eyelets1()
def tarp1():
    s = 11; ox = 30; oy = 20
    ey = "".join(f'<circle cx="{ox + x * s + (6 if x == 0 else -6 if x == TW1 else 0)}" cy="{oy + y * s + (6 if y == 0 else -6 if y == TH1 else 0)}" r="5" fill="#e9eef5" stroke="#5e6b7a" stroke-width="2"/>' for x, y in EY1)
    return f'''<svg viewBox="0 0 {TW1 * s + 60} {TH1 * s + 40}" width="{TW1 * s + 60}" style="display:block;width:100%;height:auto"><rect x="{ox}" y="{oy}" width="{TW1 * s}" height="{TH1 * s}" rx="4" fill="{B1}"/>
<rect x="{ox + 4}" y="{oy + 4}" width="{TW1 * s - 8}" height="{TH1 * s - 8}" fill="none" stroke="#8fb5e6" stroke-width="2" stroke-dasharray="6 4"/>{"".join(f'<line x1="{ox}" y1="{oy + k * 22}" x2="{ox + TW1 * s}" y2="{oy + k * 22}" stroke="#2a6cb8" stroke-width="1.5"/>' for k in range(1, int(TH1 * s / 22)))}{ey}</svg>'''
ROW1 = [("Size", "18 x 24 or 20 x 24?", f"{TW1} × {TH1} ft"), ("Colour", "blue I think", "Blue · silver inside"), ("Eyelets", "?", f"Every {EV1} ft · {len(EY1)}"), ("Rope", "ask him", "Yes · 4 corners"), ("Ready", "Tuesday??", "Wed 25 Nov · 5 PM")]
TD1 = [("T-71", "18 × 24 ft", "Cutting"), ("T-72", "12 × 15 ft", "Welding"), ("T-73", "30 × 40 ft", "Eyelets"), ("T-74", "9 × 12 ft", "Ready")]
P["p411_tarp"] = page(f"""
body{{--f:'DM Sans';--h:'Anton';background:#edf1f5;color:{K1}}}
.kk{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{O1};margin-top:22px}}
h1{{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.25;letter-spacing:.3px;margin-top:30px}} h1 span{{color:{B1}}}
.vw{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm1{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#66717f}}
.sl1{{position:relative;display:grid;grid-template-columns:1fr 1fr;border-radius:24px;overflow:hidden;box-shadow:0 14px 30px rgba(23,33,46,.1)}}
.dy1{{background:#fffbea repeating-linear-gradient(180deg,transparent 0 47px,#c9d7ea 47px 48px);padding:14px 34px 14px 22px;display:flex;flex-direction:column}}
.ap1{{background:#fff;padding:14px 22px 14px 40px;display:flex;flex-direction:column}}
.dy1 .r,.ap1 .r{{height:48px;display:flex;justify-content:space-between;align-items:center;gap:10px}}
.dy1 .r span{{font:600 16px/1.3 'DM Sans';color:#8b8a80}}.dy1 .r b{{font:italic 600 22px/1.3 Gelasio;color:#3d4a8f}}.dy1 .r b.x{{text-decoration:line-through;text-decoration-color:#c0392b}}
.ap1 .r{{border-top:1px solid #e9edf2}}.ap1 .r span{{font:600 16px/1.3 'DM Sans';color:#66717f}}.ap1 .r b{{font:700 20px/1.3 'DM Sans'}}
.hd1{{height:30px;display:flex;align-items:center;justify-content:space-between}}.tg1{{font:700 14px/1 'DM Sans';border-radius:8px;padding:6px 10px}}
.dv1{{position:absolute;top:0;bottom:0;left:calc(50% - 3px);width:6px;background:{O1}}}
.hn1{{position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:58px;height:58px;border-radius:50%;background:{O1};border:5px solid #fff;color:#fff;display:flex;align-items:center;justify-content:center;font:800 22px/1 'DM Sans';box-shadow:0 6px 14px rgba(0,0,0,.2)}}
.bt1{{flex:1;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:14px;min-height:0}}
.tp1{{background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(23,33,46,.08);min-height:0}}.tp1 .sv{{flex:1;min-height:0;display:flex;justify-content:center}}.tp1 .sv svg{{height:100%!important;width:auto!important}}
.tp1 .lg{{display:flex;justify-content:space-between;font:600 15px/1.3 'DM Sans'}}.tp1 .lg b{{color:{O1}}}
.rt1{{display:flex;flex-direction:column;gap:14px}}
.sp1{{background:{K1};color:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column}}.sp1 .sm1{{color:#a7b3c3}}
.sp1 .r{{flex:1;min-height:38px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.12)}}.sp1 .r span{{font:500 16px/1.3 'DM Sans';color:#b9c4d3}}.sp1 .r b{{font:700 18px/1.3 'DM Sans'}}
.td1{{flex:1;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(23,33,46,.08)}}
.td1 .r{{flex:1;display:grid;grid-template-columns:70px 1fr auto;gap:10px;align-items:center;border-top:1px solid #e9edf2}}.td1 b{{font:700 18px/1.3 'DM Sans'}}.td1 .r span{{font:500 16px/1.3 'DM Sans';color:#66717f}}
.td1 em{{font:700 14px/1.2 'DM Sans';font-style:normal;border-radius:9px;padding:6px 10px;background:#e3edf9;color:{B1}}}.td1 em.rd{{background:#e1f2e5;color:#1f6b3a}}
""", "<div class=kk>TARPAULIN MAKER · CUSTOM SIZES</div><h1>Tarp orders on scrap paper?<br><span>Every size and eyelet, on record.</span></h1>",
f'''<div class=vw><div class=sl1><div class=dy1><div class=hd1><span class=sm1>BEFORE · DIARY</span><span class=tg1 style="background:#fde2cc;color:#a14a0b">Guesswork</span></div>{"".join(f'<div class=r><span>{a}</span><b class="{"x" if a == "Size" else ""}">{b}</b></div>' for a, b, c in ROW1)}</div>
<div class=ap1><div class=hd1><span class=sm1>AFTER · ORDER T-71 · SAMPLE</span><span class=tg1 style="background:#e1f2e5;color:#1f6b3a">Confirmed</span></div>{"".join(f'<div class=r><span>{a}</span><b>{c}</b></div>' for a, b, c in ROW1)}</div><i class=dv1></i><span class=hn1>⇆</span></div>
<div class=bt1><div class=tp1><span class=sm1>T-71 DRAWN TO SCALE</span><div class=sv>{tarp1()}</div><div class=lg><span>{TW1} × {TH1} ft</span><b>{len(EY1)} eyelets, every {EV1} ft</b></div></div>
<div class=rt1><div class=sp1><span class=sm1>T-71 · CUTTING SHEET</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Buyer", "Sample Transport"), ("Sheet", "Heavy · blue/silver"), ("Edges", "Welded hem + rope"), ("Eyelets", f"{len(EY1)} · brass colour")])}</div>
<div class=td1><span class=sm1>TODAY ON THE FLOOR</span>{"".join(f'<div class=r><b>{a}</b><span>{b}</span><em class="{"rd" if s == "Ready" else ""}">{s}</em></div>' for a, b, s in TD1)}</div></div></div></div>''',
K1, "Make tarpaulins? DM us", f"background:{B1};color:#fff")



# ───────── 413 INDIA · Bulk roti / chapati supplier · SINGLE · Poppins + Open Sans · wheat / tawa black / chilli red
# New technique: delivery round map where each stop is a bubble sized by its roti count (area-true), drawn from the same
# client list that gives the dough plan; the phone shows the client side with a 10 AM cut-off.
W3 = "#f4e7cf"; K3 = "#1f1b17"; R3 = "#c8372d"; Y3 = "#d9a441"
CL3 = [(n, c, o, ("Same" if c == o else f"Changed {'+' if c > o else '−'}{abs(c - o)}")) for n, c, o in [("Sample Office A", 240, 220), ("Sample Hostel B", 380, 400), ("Sample Canteen C", 150, 150), ("Sample PG D", 90, 90), ("Sample Factory E", 300, 300)]]
TOT3 = sum(c[1] for c in CL3)
PERKG3 = 30
KG3 = math.ceil(TOT3 / PERKG3)
STOPS3 = [(150, 300), (290, 170), (420, 280), (520, 140), (610, 250)]
def map3():
    W, H = 680, 360
    road = " ".join(f"{'M' if i == 0 else 'L'}{x} {y}" for i, (x, y) in enumerate([(40, 330)] + STOPS3))
    bub = ""
    for (x, y), (n, c, o, ch) in zip(STOPS3, CL3):
        r = 9 * math.sqrt(c / 10)
        bub += f'<circle cx="{x}" cy="{y}" r="{r:.1f}" fill="{R3}" fill-opacity=".85" stroke="#fff" stroke-width="3"/><text x="{x}" y="{y + 7}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="20" fill="#fff">{c}</text>'
    blocks = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="#eadbbd"/>' for x, y, w, h in [(60, 40, 140, 90), (230, 40, 120, 60), (380, 30, 90, 60), (560, 30, 90, 60), (60, 190, 50, 90), (320, 220, 70, 120), (470, 200, 80, 140), (630, 300, 40, 50)])
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto"><rect width="{W}" height="{H}" rx="18" fill="#f8efdc"/>{blocks}
<path d="{road}" fill="none" stroke="{K3}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="2 12"/>
<rect x="12" y="312" width="84" height="36" rx="8" fill="{K3}"/><text x="54" y="336" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="14" fill="{Y3}">Kitchen</text>{bub}</svg>'''
PH3 = f'''<div class=pp3><div class=h3>Tomorrow's roti order</div><div class=cl3>Sample Hostel B · Tue 24 Nov</div>
<div class=ml3>{"".join(f'<div class=r><span>{m}</span><div class=st><i>−</i><b>{q}</b><i>+</i></div></div>' for m, q in [("Lunch", 220), ("Dinner", 160)])}</div>
<div class=tt3><span>Total</span><b>380</b></div><div class=f3><span>Drop point</span><b>Gate 2 · kitchen</b></div><div class=f3><span>Delivery by</span><b>11:30 AM lunch · 7 PM dinner</b></div><div class=nt3>Was 400. You can change it till <b>10:00 AM</b> today.</div><div class=bt3>Save order</div></div>'''
P["p413_roti"] = page(f"""
body{{--f:'Open Sans';--h:'Poppins';background:{W3};color:{K3}}}
.kk{{font:800 16px/1.4 'Open Sans';letter-spacing:3px;color:{R3};margin-top:22px}}
h1{{font-family:'Poppins';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1.5px}} h1 span{{color:{R3}}}
.vw{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:20px;min-height:0}}
.lf3{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm3{{font:800 13px/1.4 'Open Sans';letter-spacing:2px;color:#7d6f58}}
.cd3{{background:#fffaf0;border-radius:24px;padding:14px 18px;box-shadow:0 12px 26px rgba(60,40,10,.08);display:flex;flex-direction:column;gap:8px}}
.ls3{{flex:1;min-height:0}}.ls3 .r{{flex:1;display:grid;grid-template-columns:1fr 64px 116px;gap:10px;align-items:center;border-top:1px solid #efe3cc}}.ls3 b{{font:700 17px/1.3 'Open Sans'}}.ls3 strong{{font:800 20px/1.3 Poppins;text-align:right}}
.ls3 em{{font:700 13px/1.2 'Open Sans';font-style:normal;border-radius:9px;padding:6px 8px;text-align:center;background:#efe6d4;color:#7d6f58}}.ls3 em.ch{{background:#fbe0dc;color:{R3}}}
.dg3{{background:{K3};color:#fff;border-radius:20px;padding:12px 18px;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}.dg3 b{{display:block;font:800 30px/1.2 Poppins;color:{Y3}}}.dg3 span{{font:600 14px/1.3 'Open Sans';color:#d8cdb8}}
.ph3{{display:flex;align-items:center}}
.pp3{{flex:1;display:flex;flex-direction:column;gap:12px;padding:10px 16px 18px;background:#fffaf0}}.h3{{font:800 19px/1.3 Poppins}}.cl3{{font:600 14px/1.3 'Open Sans';color:#7d6f58}}
.ml3{{display:flex;flex-direction:column;gap:10px}}.ml3 .r{{background:#fff;border:1.5px solid #ecdcc0;border-radius:14px;padding:12px;display:flex;justify-content:space-between;align-items:center}}.ml3 .r span{{font:700 16px/1.3 'Open Sans'}}
.st{{display:flex;align-items:center;gap:8px}}.st i{{width:30px;height:30px;border-radius:9px;background:{K3};color:#fff;font:800 18px/30px Poppins;font-style:normal;text-align:center}}.st b{{font:800 19px/1.2 Poppins;width:48px;text-align:center}}
.tt3{{display:flex;justify-content:space-between;align-items:center;background:#f4e7cf;border-radius:14px;padding:12px}}.tt3 span{{font:700 16px/1.3 'Open Sans'}}.tt3 b{{font:800 26px/1.2 Poppins;color:{R3}}}
.f3{{display:flex;flex-direction:column;gap:3px;background:#fff;border:1.5px solid #ecdcc0;border-radius:14px;padding:10px 12px}}.f3 span{{font:700 12px/1.3 'Open Sans';letter-spacing:1px;color:#7d6f58;text-transform:uppercase}}.f3 b{{font:700 15px/1.35 'Open Sans'}}.nt3{{font:500 15px/1.45 'Open Sans';color:#5d5244;text-wrap:pretty}}.bt3{{margin-top:auto;background:{R3};color:#fff;border-radius:14px;padding:13px;text-align:center;font:800 16px/1.2 Poppins}}
""", "<div class=kk>ROTI SUPPLIER · OFFICES, HOSTELS, CANTEENS</div><h1>Roti counts change daily?<br><span>Clients update by 10 AM.</span></h1>",
f'''<div class=vw><div class=lf3><div class=cd3><span class=sm3>TOMORROW'S ROUND · BUBBLE SIZE = ROTIS · SAMPLE</span>{map3()}</div>
<div class="cd3 ls3"><span class=sm3>ORDERS LOCKED AT 10 AM</span>{"".join(f'<div class=r><b>{n}</b><strong>{c}</strong><em class="{"ch" if ch.startswith("Changed") else ""}">{ch}</em></div>' for n, c, o, ch in CL3)}</div>
<div class=dg3>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [(str(TOT3), "rotis tomorrow"), (f"{KG3} kg", f"atta (1 kg ≈ {PERKG3} rotis)"), (str(len(CL3)), "stops on the round")])}</div></div>
<div class=ph3>{phone(PH3, w=330, h=700)}</div></div>''',
K3, "Supply rotis or meals? DM us", f"background:{K3};color:{Y3}")


# ───────── 414 USA · Concrete leveling (slab lifting) · SINGLE · TeX Gyre Adventor + Inter · concrete grey / foam yellow / navy
# New technique: top-down driveway panel grid coloured by measured drop (inches) feeding a site report, plus an SVG
# cross-section of a sunken panel with the void and injection holes; panels-to-lift count comes from the grid.
N4 = "#1b2a41"; Y4 = "#f2c230"
DROPS4 = [[0, 0, .5], [0, .5, 1], [.5, 1, 1.5], [1, 1.5, 1.5], [.5, 1, 1], [0, 0, .5]]
COL4 = {0: "#d9dcdf", .5: "#f7e7a6", 1: "#f2c230", 1.5: "#e07b2a"}
LIFT4 = sum(1 for r in DROPS4 for d in r if d >= 1)
WATCH4 = sum(1 for r in DROPS4 for d in r if d == .5)
def fr4(d): return {0: "0\"", .5: "½\"", 1: "1\"", 1.5: "1½\""}[d]
def xsec4():
    return f'''<svg viewBox="0 0 560 190" width="560" style="display:block;width:100%;height:auto"><rect x="0" y="120" width="560" height="70" fill="#b89a74"/>{"".join(f'<circle cx="{(k * 37) % 560}" cy="{140 + (k * 13) % 45}" r="3" fill="#9c7f5c"/>' for k in range(40))}
<rect x="20" y="70" width="170" height="50" fill="#c4c8cc" stroke="#7d848c" stroke-width="2"/><rect x="370" y="70" width="170" height="50" fill="#c4c8cc" stroke="#7d848c" stroke-width="2"/>
<path d="M194 70 L366 70 L366 120 L194 120 Z" fill="none" stroke="{N4}" stroke-width="2" stroke-dasharray="6 5"/>
<path d="M194 96 L366 96 L366 146 L194 146 Z" fill="#c4c8cc" stroke="#7d848c" stroke-width="2"/><path d="M194 120 L366 120 L366 96 L194 96 Z" fill="none"/>
<rect x="194" y="120" width="172" height="0" fill="none"/>
<path d="M200 146 Q280 160 360 146 L360 150 Q280 168 200 150 Z" fill="#6e5a43"/>
{"".join(f'<rect x="{x}" y="88" width="10" height="66" rx="3" fill="{Y4}" stroke="{N4}" stroke-width="1.5"/>' for x in (230, 275, 320))}
<rect x="380" y="20" width="160" height="34" rx="8" fill="{N4}"/><text x="460" y="43" text-anchor="middle" font-family="Inter" font-weight="700" font-size="15" fill="#fff">Dropped 1½ in</text>
<path d="M460 54 L460 64 L366 84" fill="none" stroke="{N4}" stroke-width="2"/></svg>'''
P["p414_slab"] = page(f"""
body{{--f:'Inter';--h:'TeX Gyre Adventor';background:#eceef0;color:{N4}}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:#b5841a;margin-top:22px}}
h1{{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;line-height:1.2;letter-spacing:-1.5px}} h1 span{{background:{Y4};padding:0 10px;border-radius:8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}}
.vw{{flex:1;display:grid;grid-template-columns:minmax(0,.82fr) minmax(0,1.18fr);gap:16px;min-height:0}}
.sm4{{font:700 13px/1.4 Inter;letter-spacing:2px;color:#68717c}}
.cd4{{background:#fff;border-radius:24px;padding:16px 18px;box-shadow:0 12px 26px rgba(27,42,65,.08);display:flex;flex-direction:column;gap:10px}}
.dw4{{min-height:0}}.gd4{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(6,1fr);gap:6px;background:#a9aeb4;padding:6px;border-radius:10px}}
.gd4 div{{border-radius:4px;display:flex;align-items:center;justify-content:center;font:800 20px/1 Inter}}
.st4{{display:flex;justify-content:space-between;align-items:center;font:600 14px/1.3 Inter;color:#68717c}}.st4 b{{font:700 15px/1 Inter;color:{N4};background:#dfe3e8;border-radius:8px;padding:6px 10px}}
.lg4{{display:grid;grid-template-columns:1fr 1fr;gap:6px}}.lg4 span{{display:flex;gap:8px;align-items:center;font:600 14px/1.3 Inter}}.lg4 i{{width:18px;height:18px;border-radius:4px}}
.rt4{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.rp4{{flex:1;background:{N4};color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column}}.rp4 .sm4{{color:#a9b6c8}}
.rp4 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.12);gap:10px}}.rp4 .r span{{font:500 16px/1.3 Inter;color:#c0cad7}}.rp4 .r b{{font:700 18px/1.3 Inter;text-align:right}}
.bk4{{display:flex;gap:10px;align-items:center;margin-top:8px}}.bk4 i{{width:72px;height:54px;border-radius:10px;background:linear-gradient(160deg,#c4c8cc,#8d949b 55%,#b89a74 55%)}}.bk4 b{{margin-left:auto;background:{Y4};color:{N4};border-radius:12px;padding:12px 16px;font:800 16px/1.2 Inter;white-space:nowrap}}
""", "<div class=kk>CONCRETE LEVELING · SITE REPORTS</div><h1>Sunken driveway quotes?<br><span>Measure every panel once.</span></h1>",
f'''<div class=vw><div class="cd4 dw4"><span class=sm4>DRIVEWAY · 18 PANELS · SAMPLE</span><div class=st4><span>Garage</span><b>Measured drop</b></div>
<div class=gd4>{"".join(f'<div style="background:{COL4[d]}">{fr4(d)}</div>' for r in DROPS4 for d in r)}</div><div class=st4><span>Street</span><span>Top view</span></div>
<div class=lg4>{"".join(f'<span><i style="background:{COL4[d]}"></i>{t}</span>' for d, t in [(0, "Level"), (.5, "½ in · watch"), (1, "1 in · lift"), (1.5, "1½ in · lift")])}</div></div>
<div class=rt4><div class=cd4><span class=sm4>A SUNKEN PANEL · SIDE VIEW · SAMPLE</span>{xsec4()}<div class=st4><span>Void under the slab</span><span>3 small holes · fill · lift</span></div></div>
<div class=rp4><span class=sm4>SITE REPORT · SAMPLE HOME · TUE 24 NOV</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Panels to lift", f"{LIFT4} of 18"), ("Panels to watch", str(WATCH4)), ("Biggest drop", "1½ in · middle panels"), ("Cracks to seal", "2 joints"), ("Photos", "6 added by the owner")])}
<div class=bk4><i></i><i></i><b>Send quote</b></div></div></div></div>''',
N4, "Do concrete leveling? DM us", f"background:{N4};color:{Y4}")


# ───────── 412 INDIA · Coir doormat maker · CAROUSEL 5 · Crimson Text + DM Sans · coir brown / backwater green / natural fibre
# New technique: CSS coir mats (layered repeating gradients for the fibre pile, inset-shadow borders, gradient motifs) at true
# aspect ratio, a loom board whose totals feed the order, and a carton grid derived from bundles x cartons.
C2 = "#8a5a2b"; G2 = "#1f5c4a"; F2 = "#efe2c8"; K2 = "#2a2118"
PILE2 = "repeating-linear-gradient(0deg,rgba(0,0,0,.07) 0 2px,transparent 2px 5px),repeating-linear-gradient(90deg,rgba(255,255,255,.08) 0 2px,transparent 2px 4px)"
MOT2 = {
 "border": f"{PILE2},linear-gradient(#b98545,#b98545)",
 "stripe": f"{PILE2},repeating-linear-gradient(90deg,#b98545 0 26px,#1f5c4a 26px 40px)",
 "diamond": f"{PILE2},linear-gradient(45deg,transparent 40%,#6b3f1c 40% 60%,transparent 60%) 0 0/44px 44px,linear-gradient(-45deg,transparent 40%,#6b3f1c 40% 60%,transparent 60%) 0 0/44px 44px,#b98545",
 "dots": f"{PILE2},radial-gradient(circle,#1f5c4a 7px,transparent 8px) 0 0/34px 34px,#c49157",
}
def mat2(kind, w, h, edge="#5b3a1c"):
    return f'<div class=mt2 style="width:{w}px;height:{h}px;background:{MOT2[kind]};box-shadow:inset 0 0 0 10px {edge},inset 0 0 0 13px #d8b27a,0 8px 18px rgba(0,0,0,.18)"></div>'
B2 = f"""
body{{--f:'DM Sans';--h:'Crimson Text';background:{F2};color:{K2};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{C2};margin-top:22px;align-self:flex-start}}
h1{{font-family:'Crimson Text';font-weight:700;font-size:66px;line-height:1.2;letter-spacing:-.6px;margin-top:20px}} h1 span{{color:{G2}}}
.sm2{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7d6a4f}}
.cd2{{background:#fffaf0;border-radius:24px;box-shadow:0 14px 30px rgba(60,40,10,.09)}}
.dk2{{background:{G2};color:#fff;border-radius:24px}}
.mt2{{border-radius:8px;flex:none}}
"""
def t2(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{K2};color:{F2}"):
    return page(B2 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, K2, cta, ctacss, tagline=f"{n} / 5")

Q2 = [("border", "Size? 40×60 or 45×75 cm"), ("stripe", "Backing? PVC or none"), ("diamond", "How many colours?"), ("dots", "Packed how many per bundle?")]
P["p412_coir_s1"] = t2(1, "COIR DOORMAT MAKER · BULK ORDERS", "Mat order from one photo?<br><span>Put size and design in writing.</span>",
f'''<div class=w21><div class=gd21>{"".join(f'<div class="cd2 mc21">{mat2(k, 300, 180)}<span>{q}</span></div>' for k, q in Q2)}</div>
<div class="dk2 bm21"><span class=sm2>BUYER'S MESSAGE</span><p>“Need 600 like this photo. Same as last time.”</p><em>4 questions before one mat is woven.</em></div></div>''',
css=f""".w21{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.gd21{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.mc21{{padding:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px}}.mc21 span{{font:700 19px/1.3 'DM Sans';background:#f6e3d2;color:#9a4b14;border-radius:12px;padding:8px 14px;text-align:center}}
.bm21{{padding:18px 24px;display:grid;grid-template-columns:auto 1fr;gap:6px 20px;align-items:center}}.bm21 .sm2{{color:#cfe3da;grid-row:1/3}}.bm21 p{{font:600 28px/1.35 'Crimson Text'}}.bm21 em{{font:500 18px/1.3 'DM Sans';font-style:normal;color:#cfe3da}}""")

SP2 = [("Order", "M-31 · Sample Home Store"), ("Size", "45 × 75 cm"), ("Design", "Border + stripe"), ("Colours", "Natural + green"), ("Backing", "PVC · non-slip"), ("Mats", "600 · due Thu 10 Dec")]
P["p412_coir_s2"] = t2(2, "1 · ONE ORDER CARD", "Size, design, backing.<br><span>Written once, woven right.</span>",
f'''<div class=w22><div class="cd2 dr22"><span class=sm2>M-31 · DRAWN TO SCALE · SAMPLE</span><div class=fr22><div class=dh22><i></i><b>75 cm</b><i></i></div><div class=mr22>{mat2("stripe", 450, 270)}<div class=dv22><i></i><b>45 cm</b><i></i></div></div></div></div>
<div class=bt22><div class="dk2 sp22"><span class=sm2>ORDER CARD · SAMPLE</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in SP2)}</div>
<div class=op22>{"".join(f'<div class="cd2 og22"><span class=sm2>{t}</span><div>{"".join(f"<i class={chr(39)}{'on' if o == s else ''}{chr(39)}>{o}</i>" for o in opts)}</div></div>' for t, opts, s in [("SIZE (CM)", ["40×60", "45×75", "60×90"], "45×75"), ("BACKING", ["None", "PVC"], "PVC"), ("PACKING", ["10 / bundle", "5 / bundle"], "10 / bundle")])}</div></div></div>''',
css=f""".w22{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.dr22{{padding:18px 22px;display:flex;flex-direction:column;gap:12px}}
.fr22{{display:flex;flex-direction:column;align-items:center;gap:8px}}.dh22{{width:450px;display:flex;align-items:center;gap:10px;margin-right:60px}}.dh22 i,.dv22 i{{flex:1;background:linear-gradient({C2},{C2}) center/100% 2px no-repeat;align-self:stretch}}.dh22 b,.dv22 b{{font:700 18px/1.2 'DM Sans';color:{C2}}}
.mr22{{display:flex;gap:12px;align-items:stretch}}.dv22{{width:48px;display:flex;flex-direction:column;align-items:center;gap:6px}}.dv22 i{{background:linear-gradient({C2},{C2}) center/2px 100% no-repeat}}
.bt22{{flex:1;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:16px;min-height:0}}
.sp22{{padding:16px 22px;display:flex;flex-direction:column}}.sp22 .sm2{{color:#cfe3da;margin-bottom:4px}}.sp22 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:12px;border-top:1px solid rgba(255,255,255,.14)}}.sp22 .r span{{font:500 17px/1.3 'DM Sans';color:#cfe3da}}.sp22 .r b{{font:700 19px/1.3 'DM Sans';text-align:right}}
.op22{{display:flex;flex-direction:column;gap:12px}}.og22{{flex:1;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:8px}}.og22>div{{display:flex;gap:8px}}
.og22 i{{flex:1;font:700 16px/1.2 'DM Sans';font-style:normal;text-align:center;padding:10px 4px;border-radius:10px;background:#f1e5cf;color:#7d6a4f;white-space:nowrap}}.og22 i.on{{background:{C2};color:#fff}}""")

LM2 = [("Loom 1", "M-31", 120, 150, "run"), ("Loom 2", "M-31", 150, 150, "done"), ("Loom 3", "M-31", 64, 150, "run"), ("Loom 4", "M-31", 40, 150, "yarn"), ("Loom 5", "M-29", 88, 100, "run"), ("Loom 6", "M-33", 0, 80, "wait")]
CH2 = {"run": ("Weaving", ""), "done": ("Done", "dn"), "yarn": ("Needs green yarn", "yn"), "wait": ("Starts Wed", "wt")}
M31 = [l for l in LM2 if l[1] == "M-31"]
DONE31 = sum(l[2] for l in M31)
P["p412_coir_s3"] = t2(3, "2 · LOOM BOARD", "Which loom is on which order?<br><span>See every loom live.</span>",
f'''<div class=w23><div class="cd2 lb23"><span class=sm2>LOOMS TODAY · TUE 24 NOV · SAMPLE</span>{"".join(f'<div class=r><b>{a}</b><span class=oc>{o}</span><div class=br><i style="width:{d / t * 100:.0f}%"></i></div><span class=ct>{d} / {t}</span><em class={CH2[s][1]}>{CH2[s][0]}</em></div>' for a, o, d, t, s in LM2)}</div>
<div class=bt23><div class="dk2 tt23"><span class=sm2>ORDER M-31 · 600 MATS</span><b>{DONE31}</b><span>mats woven on {len(M31)} looms</span><div class=pb><i style="width:{DONE31 / 600 * 100:.0f}%"></i></div></div>
<div class="cd2 al23"><span class=sm2>ALERT</span><p>Loom 4 needs green yarn. M-31 is {600 - DONE31} mats short, so order yarn today.</p></div></div></div>''',
css=f""".w23{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.lb23{{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:2px}}
.lb23 .r{{flex:1;display:grid;grid-template-columns:86px 62px 1fr 92px 150px;gap:12px;align-items:center;border-top:1px solid #efe2c8}}.lb23 b{{font:700 24px/1.2 'Crimson Text'}}.lb23 .oc{{font:700 15px/1.2 'DM Sans';color:#7d6a4f}}
.lb23 .br{{height:20px;border-radius:10px;background:#f1e5cf;overflow:hidden}}.lb23 .br i{{display:block;height:100%;background:{C2};border-radius:10px}}.lb23 .ct{{font:700 17px/1.2 'DM Sans';text-align:right}}
.lb23 em{{font:700 14px/1.2 'DM Sans';font-style:normal;text-align:center;border-radius:10px;padding:8px 6px;background:#e3efe9;color:{G2}}}.lb23 em.dn{{background:{G2};color:#fff}}.lb23 em.yn{{background:#fbe2d3;color:#a3461a}}.lb23 em.wt{{background:#f1e5cf;color:#7d6a4f}}
.bt23{{display:grid;grid-template-columns:1fr 1.2fr;gap:16px}}.tt23{{padding:18px 22px;display:flex;flex-direction:column;gap:6px}}.tt23 .sm2{{color:#cfe3da}}.tt23 b{{font:700 64px/1.1 'Crimson Text'}}.tt23 span{{font:500 17px/1.3 'DM Sans';color:#cfe3da}}
.tt23 .pb{{height:14px;border-radius:7px;background:rgba(255,255,255,.18);overflow:hidden;margin-top:6px}}.tt23 .pb i{{display:block;height:100%;background:#e9c27a}}
.al23{{padding:18px 22px;display:flex;flex-direction:column;gap:10px;background:#fbe2d3}}.al23 .sm2{{color:#a3461a}}.al23 p{{font:600 25px/1.4 'Crimson Text';text-wrap:pretty}}""")

PB2, PC2 = 10, 5
CART2 = 600 // (PB2 * PC2)
PACKED2 = 6
P["p412_coir_s4"] = t2(4, "3 · PACK AND SHIP", "Bundles, cartons, dispatch.<br><span>Counted, not guessed.</span>",
f'''<div class=w24><div class=fl24>{"".join(f'<div class="cd2 st24"><b>{a}</b><span>{b}</span></div>' for a, b in [(f"{PB2} mats", "= 1 bundle"), (f"{PC2} bundles", "= 1 carton"), (f"{CART2} cartons", "= order M-31")])}</div>
<div class="cd2 cg24"><div class=hd24><span class=sm2>M-31 · {CART2} CARTONS · SAMPLE</span><span class=lg24><i></i>Packed {PACKED2}<i class=o></i>To pack {CART2 - PACKED2}</span></div>
<div class=bx24>{"".join(f'<div class="cb{" pk" if k < PACKED2 else ""}"><b>C-{k + 1:02d}</b><span>{PB2 * PC2} mats</span></div>' for k in range(CART2))}</div></div>
<div class="dk2 ms24"><span class=sm2>MESSAGE TO BUYER</span><p>{PACKED2} of {CART2} cartons packed. The rest will be packed by Wed 9 Dec. Dispatch Thu 10 Dec.</p></div></div>''',
css=f""".w24{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.fl24{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}.st24{{padding:16px 20px;display:flex;flex-direction:column;gap:2px}}.st24 b{{font:700 34px/1.2 'Crimson Text';color:{C2}}}.st24 span{{font:600 17px/1.3 'DM Sans'}}
.cg24{{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:12px;min-height:0}}.hd24{{display:flex;justify-content:space-between;align-items:center}}.lg24{{display:flex;gap:8px;align-items:center;font:600 15px/1.2 'DM Sans'}}.lg24 i{{width:16px;height:16px;border-radius:4px;background:{G2};margin-left:8px}}.lg24 i.o{{background:#d9b57f}}
.bx24{{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:12px}}.cb{{background:#d9b57f;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;box-shadow:inset 0 14px 0 rgba(0,0,0,.06)}}
.cb b{{font:700 26px/1.2 'Crimson Text'}}.cb span{{font:600 15px/1.2 'DM Sans'}}.cb.pk{{background:{G2};color:#fff}}
.ms24{{padding:16px 22px;display:flex;flex-direction:column;gap:8px}}.ms24 .sm2{{color:#cfe3da}}.ms24 p{{font:600 24px/1.4 'Crimson Text';text-wrap:pretty}}""")

P["p412_coir_s5"] = t2(5, "COIR MAT ORDER APP", "Make coir mats?<br><span>Let's build your order app.</span>",
f'''<div class=w25><div class=tl25>{"".join(f'<div class=cd2><span class=ib>{ic(i, 36)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("doc", "Order cards", "Size, design, backing"), ("grid", "Loom board", "Every loom, live"), ("bell", "Yarn alerts", "Before looms stop"), ("box", "Carton counts", "Packed and pending")])}</div>
<div class="dk2 q25"><span class=sm2>A QUESTION FOR MAT MAKERS</span><p>How do you track which loom is on which order today: a register, a board or memory? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{C2};color:#fff",
css=f""".w25{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl25{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl25>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl25 .ib{{width:80px;height:80px;border-radius:22px;background:{C2};color:#fff}}.tl25 b{{font:700 40px/1.2 'Crimson Text'}}.tl25 span{{font:500 22px/1.4 'DM Sans';color:#7d6a4f}}
.q25{{padding:26px 30px;display:flex;flex-direction:column;gap:12px}}.q25 .sm2{{color:#cfe3da}}.q25 p{{font:600 32px/1.4 'Crimson Text';text-wrap:pretty}}""")


# ───────── 415 INDIA · Green tea leaf collection agent · CAROUSEL 5 · Gelasio + Fira Sans · tea green / leaf bud lime / clay
# New technique: SVG "two leaves and a bud" sprig, weigh slip with LED readout, per-grower week bars from one ledger, and a
# load reconciliation (points loaded vs factory received) that computes and flags the difference.
G5 = "#2e6b3a"; L5 = "#a6c94a"; C5 = "#b5653a"; K5 = "#1d261c"; BG5 = "#f1f4ea"
def sprig5(w=300):
    return f'''<svg viewBox="0 0 300 380" width="{w}" style="display:block;width:100%;height:auto"><path d="M150 370 C150 300 148 230 152 120" stroke="#6b4a2a" stroke-width="8" fill="none" stroke-linecap="round"/>
<path d="M152 120 C140 80 146 40 160 12 C176 44 172 86 152 120 Z" fill="{L5}" stroke="{G5}" stroke-width="3"/>
<path d="M151 200 C110 196 60 170 34 120 C88 116 132 150 151 200 Z" fill="#5d9a3c" stroke="{G5}" stroke-width="3"/><path d="M151 200 C110 175 70 150 40 122" stroke="{G5}" stroke-width="2" fill="none"/>
<path d="M151 260 C196 258 246 228 272 176 C214 176 170 214 151 260 Z" fill="#4d8a33" stroke="{G5}" stroke-width="3"/><path d="M151 260 C196 232 236 204 266 178" stroke="{G5}" stroke-width="2" fill="none"/></svg>'''
B5 = f"""
body{{--f:'Fira Sans';--h:'Gelasio';background:{BG5};color:{K5};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:{C5};margin-top:22px;align-self:flex-start}}
h1{{font-family:'Gelasio';font-weight:700;font-size:58px;line-height:1.24;letter-spacing:-.8px;margin-top:20px}} h1 span{{color:{G5}}}
.sm5{{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#6c7564}}
.cd5{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(30,50,20,.08)}}
.dk5{{background:{K5};color:#fff;border-radius:24px}}
.led5{{background:#0d1a10;border:3px solid #3a4a3c;border-radius:16px;padding:10px 18px;font:700 64px/1.2 'DejaVu Sans Mono';color:#9dff7a;text-align:right}}.led5 small{{font-size:26px;margin-left:8px}}
"""
def t5(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{K5};color:{L5}"):
    return page(B5 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, K5, cta, ctacss, tagline=f"{n} / 5")

NB5 = [("G-14", "42", True), ("G-07", "38 or 36?", False), ("G-21", "wet, 29", False), ("G-03", "51", True), ("G-14", "again?", False)]
P["p415_tea_s1"] = t5(1, "GREEN LEAF COLLECTION AGENT", "Leaf weights in a notebook?<br><span>Every grower's kg, on record.</span>",
f'''<div class=w51><div class="cd5 sp51"><span class=sm5>FINE LEAF</span><div class=sv>{sprig5()}</div><b>Two leaves and a bud</b></div>
<div class=rt51><div class=nb51><span class=sm5>TODAY'S NOTEBOOK · SAMPLE</span>{"".join(f'<div class=r><span>{g}</span><b class="{"" if ok else "bd"}">{v}</b></div>' for g, v, ok in NB5)}</div>
<div class="dk5 pr51">{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [("“How much this week?”", "Growers ask every day"), ("“38 or 36?”", "Smudged numbers"), ("“Was it wet leaf?”", "No notes on quality")])}</div></div></div>''',
css=f""".w51{{flex:1;display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:16px;min-height:0}}
.sp51{{padding:20px;display:flex;flex-direction:column;align-items:center;gap:12px}}.sp51 .sv{{flex:1;min-height:0;width:100%;display:flex;align-items:center;justify-content:center}}.sp51 .sv svg{{height:100%!important;width:auto!important;max-width:100%}}.sp51 b{{font:700 24px/1.3 Gelasio;color:{G5};text-align:center}}
.rt51{{display:flex;flex-direction:column;gap:16px}}.nb51{{flex:1;background:#fffdf3 repeating-linear-gradient(180deg,transparent 0 53px,#cfdcea 53px 54px);border-radius:16px;padding:16px 22px 10px 60px;position:relative;box-shadow:0 14px 30px rgba(30,50,20,.08);display:flex;flex-direction:column;border-left:3px solid #e8a2a2}}
.nb51 .r{{flex:1;display:flex;justify-content:space-between;align-items:center}}.nb51 .r span{{font:italic 600 24px/1.3 Gelasio;color:#3d4a8f}}.nb51 .r b{{font:italic 700 26px/1.3 Gelasio;color:#3d4a8f}}.nb51 .r b.bd{{color:#b3402e;text-decoration:underline wavy #b3402e}}
.pr51{{padding:16px 22px;display:flex;flex-direction:column;gap:10px}}.pr51>div{{display:flex;justify-content:space-between;align-items:center;gap:12px}}.pr51 b{{font:700 21px/1.3 Gelasio;color:{L5}}}.pr51 span{{font:500 16px/1.3 'Fira Sans';color:#c9d3c2}}""")

TD5 = [("G-14", "7:40 AM", 42.5, "Fine"), ("G-07", "7:52 AM", 36.0, "Fine"), ("G-21", "8:05 AM", 29.0, "Wet · noted"), ("G-03", "8:11 AM", 51.5, "Fine"), ("G-18", "8:20 AM", 33.5, "Coarse · noted")]
PT5 = sum(t[2] for t in TD5)
P["p415_tea_s2"] = t5(2, "1 · WEIGH AND SEND A SLIP", "Weighed at the point.<br><span>The grower gets a slip.</span>",
f'''<div class=w52><div class=tp52><div class="dk5 sc52"><span class=sm5 style="color:#c9d3c2">SCALE · POINT 2 · SAMPLE</span><div class=led5>42.5<small>kg</small></div><span class=nt>Grower G-14 · 2 bags · fine leaf</span></div>
<div class="cd5 sl52"><span class=sm5>SLIP SENT BY MESSAGE</span><p>G-14: 42.5 kg green leaf, fine, at Point 2 on Tue 24 Nov, 7:40 AM. This week so far: 82.5 kg.</p></div></div>
<div class="cd5 tb52"><div class=hd><span class=sm5>POINT 2 · TODAY · SAMPLE</span><b>{PT5:g} kg so far</b></div>{"".join(f'<div class=r><b>{g}</b><span>{t}</span><strong>{k:g} kg</strong><em class="{"" if q == "Fine" else "nq"}">{q}</em></div>' for g, t, k, q in TD5)}</div></div>''',
css=f""".w52{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tp52{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.sc52{{padding:18px 22px;display:flex;flex-direction:column;gap:12px}}.sc52 .nt{{font:600 17px/1.3 'Fira Sans'}}
.sl52{{padding:18px 22px;display:flex;flex-direction:column;gap:12px;background:#e9f2d9}}.sl52 p{{font:500 21px/1.5 'Fira Sans';text-wrap:pretty}}
.tb52{{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:2px}}.tb52 .hd{{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}}.tb52 .hd b{{font:700 18px/1.2 'Fira Sans';background:{G5};color:#fff;border-radius:10px;padding:8px 12px}}
.tb52 .r{{flex:1;display:grid;grid-template-columns:90px 1fr 120px 170px;gap:12px;align-items:center;border-top:1px solid #e6ebdf}}.tb52 .r b{{font:700 22px/1.3 Gelasio}}.tb52 .r span{{font:500 17px/1.3 'Fira Sans';color:#6c7564}}.tb52 strong{{font:700 21px/1.3 'Fira Sans';text-align:right}}
.tb52 em{{font:700 15px/1.2 'Fira Sans';font-style:normal;text-align:center;border-radius:10px;padding:8px;background:#e9f2d9;color:{G5}}}.tb52 em.nq{{background:#f7e1d5;color:#9a4a22}}""")

DAYS5 = ["Mon 16", "Tue 17", "Wed 18", "Thu 19", "Fri 20", "Sat 21"]
LG5 = {"G-14": [38, 41, 0, 44, 40, 36], "G-07": [30, 34, 33, 0, 36, 31], "G-03": [48, 50, 52, 47, 0, 49], "G-21": [26, 0, 28, 30, 27, 29]}
MX5 = max(max(v) for v in LG5.values())
P["p415_tea_s3"] = t5(3, "2 · A LEDGER FOR EVERY GROWER", "“How much this week?”<br><span>The answer is one tap away.</span>",
f'''<div class=w53><div class="cd5 gw53"><div class=hd><span class=sm5>G-14 · WEEK MON 16 – SAT 21 NOV · SAMPLE</span><b>{sum(LG5["G-14"])} kg</b></div>
<div class=bars>{"".join(f'<div class=bc><span class=v>{k if k else "—"}</span><div class=bw><i style="height:{k / MX5 * 100:.0f}%"></i></div><span class=d>{d}</span></div>' for d, k in zip(DAYS5, LG5["G-14"]))}</div></div>
<div class="cd5 tl53"><span class=sm5>ALL GROWERS · SAME WEEK · KG · SAMPLE</span><div class="r h"><span>Grower</span>{"".join(f"<span>{d.split()[0]}</span>" for d in DAYS5)}<span>Total</span></div>
{"".join(f'<div class=r><b>{g}</b>' + "".join(f"<span class={chr(39)}{'z' if k == 0 else ''}{chr(39)}>{k if k else '—'}</span>" for k in v) + f'<strong>{sum(v)}</strong></div>' for g, v in LG5.items())}</div></div>''',
css=f""".w53{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.gw53{{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:10px;min-height:0}}
.gw53 .hd{{display:flex;justify-content:space-between;align-items:center}}.gw53 .hd b{{font:700 24px/1.2 Gelasio;color:{G5}}}
.bars{{flex:1;display:grid;grid-template-columns:repeat(6,1fr);gap:16px;min-height:0}}.bc{{display:flex;flex-direction:column;align-items:center;gap:6px;min-height:0}}.bc .v{{font:700 19px/1.3 'Fira Sans'}}.bc .d{{font:600 15px/1.3 'Fira Sans';color:#6c7564}}
.bw{{flex:1;width:100%;background:#eef2e6;border-radius:12px;display:flex;align-items:flex-end;overflow:hidden;min-height:0}}.bw i{{display:block;width:100%;background:linear-gradient({L5},{G5});border-radius:12px}}
.tl53{{padding:16px 22px;display:flex;flex-direction:column;gap:2px}}.tl53 .r{{display:grid;grid-template-columns:100px repeat(6,1fr) 90px;gap:8px;align-items:center;height:48px;border-top:1px solid #e6ebdf}}
.tl53 .r.h{{border-top:0;height:34px}}.tl53 .r.h span{{font:700 14px/1.2 'Fira Sans';color:#6c7564;text-align:center}}.tl53 .r b{{font:700 21px/1.3 Gelasio}}.tl53 .r span{{font:600 18px/1.3 'Fira Sans';text-align:center}}.tl53 .r span.z{{color:#b9c0b1}}.tl53 strong{{font:700 20px/1.3 'Fira Sans';text-align:right;color:{G5}}}""")

LD5 = [("Point 1", 412, 14, 30), ("Point 2", 386, 12, 27), ("Point 3", 442, 15, 32)]
LDT5 = sum(x[1] for x in LD5)
FAC5 = 1226
DIF5 = LDT5 - FAC5
P["p415_tea_s4"] = t5(4, "3 · LOAD AND FACTORY RECEIPT", "Loaded vs received.<br><span>See any gap the same day.</span>",
f'''<div class=w54><div class=pts54>{"".join(f'<div class="cd5 pt54"><span class=sm5>{p.upper()} · SAMPLE</span><b>{k} kg</b><div class=rr><span>Growers</span><em>{g}</em></div><div class=rr><span>Bags</span><em>{bg}</em></div><div class=rr><span>Loaded</span><em>11:30 AM</em></div></div>' for p, k, g, bg in LD5)}</div>
<div class=eq54><div class="dk5 tt54"><span class=sm5 style="color:#c9d3c2">TRUCK LOADED · SAMPLE</span><b>{LDT5:,} kg</b></div><div class=vs54>vs</div><div class="cd5 tt54"><span class=sm5>FACTORY RECEIVED</span><b>{FAC5:,} kg</b></div></div>
<div class="cd5 df54"><div><span class=sm5>DIFFERENCE</span><b>{DIF5} kg</b></div><p>Flagged on Tue 24 Nov. Check the wet leaf from Point 2 and the factory scale slip before the week closes.</p></div></div>''',
css=f""".w54{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.pts54{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:16px}}
.pt54{{padding:18px 20px;display:flex;flex-direction:column;gap:6px}}.pt54 b{{font:700 56px/1.2 Gelasio;color:{G5}}}.pt54{{justify-content:space-between}}.pt54 .rr{{display:flex;justify-content:space-between;border-top:1px solid #e6ebdf;padding-top:8px}}.pt54 .rr span{{font:500 17px/1.3 'Fira Sans';color:#6c7564}}.pt54 .rr em{{font:700 18px/1.3 'Fira Sans';font-style:normal}}
.eq54{{display:grid;grid-template-columns:1fr auto 1fr;gap:16px;align-items:stretch}}.tt54{{padding:26px 24px;display:flex;flex-direction:column;justify-content:center;gap:10px}}.tt54 b{{font:700 64px/1.2 Gelasio}}.dk5.tt54 b{{color:{L5}}}
.vs54{{align-self:center;font:700 26px/1.2 Gelasio;color:#6c7564}}
.df54{{padding:20px 24px;display:grid;grid-template-columns:auto 1fr;gap:24px;align-items:center;background:#f7e1d5}}.df54 .sm5{{color:#9a4a22;display:block}}.df54 b{{font:700 54px/1.2 Gelasio;color:#9a4a22}}.df54 p{{font:500 21px/1.5 'Fira Sans';text-wrap:pretty}}""")

P["p415_tea_s5"] = t5(5, "LEAF COLLECTION APP", "Collect green leaf?<br><span>Let's build your weigh app.</span>",
f'''<div class=w55><div class=tl55>{"".join(f'<div class=cd5><span class=ib>{ic(i, 36)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("check", "Weigh slips", "Sent to each grower"), ("users", "Grower ledgers", "Kg by day and week"), ("leaf", "Leaf quality", "Wet or coarse, noted"), ("truck", "Load check", "Loaded vs received")])}</div>
<div class="dk5 q55"><span class=sm5 style="color:{L5}">A QUESTION FOR LEAF AGENTS</span><p>How do growers check their kg today: a notebook, a call or a slip? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{G5};color:#fff",
css=f""".w55{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl55{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl55>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.tl55 .ib{{width:80px;height:80px;border-radius:22px;background:{G5};color:{L5}}}.tl55 b{{font:700 34px/1.3 Gelasio}}.tl55 span{{font:500 22px/1.4 'Fira Sans';color:#6c7564}}
.q55{{padding:26px 30px;display:flex;flex-direction:column;gap:12px}}.q55 p{{font:700 30px/1.45 Gelasio;text-wrap:pretty}}""")



if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
