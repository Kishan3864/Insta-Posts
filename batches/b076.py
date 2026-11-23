import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 396 INDIA · Crane hire · SINGLE · TeX Gyre Adventor + Open Sans · crane amber / night navy / sky cyan
# New technique: SVG truck cranes drawn with boom length scaled to capacity; a job request is matched in Python to cranes
# that are big enough AND free on the date, and each crane card shows both checks.
CR6 = [("C-1", 14, {"Tue": "Sample Factory Shed"}), ("C-2", 20, {}), ("C-3", 25, {"Tue": "Sample Bridge Site", "Wed": "Sample Bridge Site"}), ("C-4", 40, {})]
REQ6 = dict(load=12, day="Tue", date="Tue 24 Nov", site="Sample Warehouse, Ring Road")
def fit6(c): return c[1] >= REQ6["load"] + 4
def crane6(cap, col):
    L = 90 + cap * 3.2; a = math.radians(38); x0, y0 = 70, 92
    x1, y1 = x0 + L * math.cos(a), y0 - L * math.sin(a)
    W = 330
    return f'''<svg viewBox="0 0 {W} 150" width="420" style="display:block"><rect x="20" y="92" width="190" height="26" rx="6" fill="{col}"/><rect x="150" y="70" width="48" height="26" rx="5" fill="{col}"/><rect x="158" y="76" width="30" height="14" rx="3" fill="#bfe6f2"/>
<rect x="40" y="80" width="56" height="16" rx="4" fill="#24324d"/><line x1="{x0}" y1="{y0}" x2="{x1:.1f}" y2="{max(y1, 8):.1f}" stroke="{col}" stroke-width="10" stroke-linecap="round"/><line x1="{x0}" y1="{y0}" x2="{x0 + (x1 - x0) * .55:.1f}" y2="{y0 - (y0 - max(y1, 8)) * .55:.1f}" stroke="#24324d" stroke-width="4"/>
<line x1="{x1:.1f}" y1="{max(y1, 8):.1f}" x2="{x1:.1f}" y2="{max(y1, 8) + 40:.1f}" stroke="#24324d" stroke-width="2"/><path d="M{x1 - 5:.1f} {max(y1, 8) + 40:.1f} h10 v6 a5 5 0 1 1 -10 0z" fill="#24324d"/>
{"".join(f'<circle cx="{x}" cy="124" r="13" fill="#24324d"/><circle cx="{x}" cy="124" r="5" fill="#9aa6bd"/>' for x in (44, 78, 160, 190))}</svg>'''
P["p396_crane"] = page("""
body{--f:'Open Sans';--h:'TeX Gyre Adventor';background:#eef4f7;color:#1b2740}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#b7700b;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:56px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#d98a0e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm6{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#62708a}
.rq6{background:#1b2740;color:#fff;border-radius:24px;padding:16px 22px;display:grid;grid-template-columns:auto repeat(4,1fr);gap:16px;align-items:center}.rq6 .sm6{color:#9fb3d1;writing-mode:horizontal-tb}
.rq6 div small{display:block;font:500 14px/1.3 'Open Sans';color:#9fb3d1}.rq6 div b{font:700 19px/1.3 'Open Sans'}.rq6 div b.big{font:700 26px/1.25 'TeX Gyre Adventor';color:#ffc24d}
.gd6{flex:1;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;min-height:0}
.cc6{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(27,39,64,.08);border:3px solid transparent}.cc6.best{border-color:#2aa3c7}
.cc6 .h{display:flex;justify-content:space-between;align-items:center}.cc6 .h b{font:700 26px/1.25 'TeX Gyre Adventor'}.cc6 .h span{font:700 15px/1.2 'Open Sans';background:#eef4f7;border-radius:10px;padding:7px 10px}
.cc6 .dr{flex:1;display:flex;align-items:center;justify-content:center;min-height:0}
.ck6{display:grid;grid-template-columns:1fr 1fr;gap:8px}.ck6 i{font:700 15px/1.3 'Open Sans';font-style:normal;border-radius:10px;padding:9px 10px;display:flex;gap:6px;align-items:center}
.ck6 i.y{background:#dff2f8;color:#0f6a86}.ck6 i.n{background:#fde5dc;color:#a2391a}
.ms6{background:#fff4dc;border-radius:22px;padding:14px 20px;display:flex;gap:16px;align-items:center}.ms6 p{font:500 18px/1.45 'Open Sans';text-wrap:pretty}.ms6 .sm6{white-space:nowrap;color:#a26407}
""", "<div class=kk>CRANE HIRE · BOOKINGS</div><h1>One crane, two jobs on Tuesday?<br><span>Check size and date first.</span></h1>",
f'''<div class=vw><div class=rq6><span class=sm6>NEW JOB<br>· SAMPLE</span>{"".join(f'<div><small>{a}</small><b class="{c}">{b}</b></div>' for a, b, c in [("Heaviest lift", f"{REQ6['load']} t", "big"), ("Crane needed", f"{REQ6['load'] + 4} t or more", ""), ("Date", REQ6["date"], ""), ("Site", REQ6["site"], "")])}</div>
<div class=gd6>{"".join(f'<div class="cc6 {"best" if fit6(c) and REQ6["day"] not in c[2] and not any(fit6(d) and REQ6["day"] not in d[2] for d in CR6[:k]) else ""}"><div class=h><b>{c[0]} · {c[1]} t</b><span>{"Fits and free" if fit6(c) and REQ6["day"] not in c[2] else ("Too small" if not fit6(c) else "Busy that day")}</span></div><div class=dr>{crane6(c[1], "#f0a72a" if fit6(c) and REQ6["day"] not in c[2] else "#c9d2de")}</div>'
 f'<div class=ck6><i class="{"y" if fit6(c) else "n"}">{"Big enough" if fit6(c) else "Under 16 t"}</i><i class="{"n" if REQ6["day"] in c[2] else "y"}">{"Booked on Tue" if REQ6["day"] in c[2] else "Free on Tue"}</i></div></div>' for k, c in enumerate(CR6))}</div>
<div class=ms6><span class=sm6>BOOKING SENT</span><p>C-2 (20 t) booked for {REQ6["date"]} at {REQ6["site"]}. Operator and crane reach by 8:30 AM. Hours are noted on the log sheet.</p></div></div>''',
"#1b2740", "Hire out cranes? DM us", "background:#1b2740;color:#ffc24d")


# ───────── 398 INDIA · Areca leaf plate maker · SINGLE · Cardo + Fira Sans · sheath beige / palm green / charcoal
# New technique: CSS areca plates seen from above (leaf grain via layered repeating gradients, pressed rim ring), one per
# size with packs in stock as a stacked-pack isotype; orders booked against stock in Python with a pressing plan line.
PL8 = [("Round 10 in", "r", 150, 18), ("Round 8 in", "r", 124, 26), ("Square 6 in", "s", 108, 9), ("Bowl 4 in", "b", 92, 14)]
OD8 = [("A-21", "Sample Caterer", "Round 10 in", 16, "Thu 26 Nov"), ("A-22", "Sample Eco Store", "Round 8 in", 10, "Fri 27 Nov"), ("A-23", "Sample Event Planner", "Square 6 in", 12, "Sat 28 Nov"), ("A-24", "Sample Café", "Bowl 4 in", 6, "Mon 30 Nov")]
LEFT8 = {p[0]: p[3] for p in PL8}
AL8 = []
for o in OD8:
    t = min(o[3], LEFT8[o[2]]); LEFT8[o[2]] -= t; AL8.append(o + (t,))
def plate8(kind, s):
    br = "50%" if kind != "s" else "18px"
    grain = "repeating-linear-gradient(100deg,rgba(120,84,40,.10) 0 3px,transparent 3px 9px),repeating-linear-gradient(96deg,rgba(255,255,255,.18) 0 2px,transparent 2px 13px)"
    deep = "inset 0 0 0 10px #d8b98a,inset 0 0 0 12px #c49c63,inset 0 10px 24px rgba(90,60,25,.35)" if kind == "b" else "inset 0 0 0 12px #e2c697,inset 0 0 0 14px #c49c63,inset 0 6px 14px rgba(90,60,25,.18)"
    return f'<div class=pt8 style="width:{s}px;height:{s}px;border-radius:{br};background:{grain},radial-gradient(circle at 40% 35%,#ecd3a6,#cfa86c);box-shadow:{deep},0 8px 14px rgba(40,30,20,.18)"></div>'
P["p398_areca"] = page("""
body{--f:'Fira Sans';--h:'Cardo';background:#f4ecdc;color:#2a2925;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#4e6b2f;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:64px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#4e6b2f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm8{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#7a6c55}
.st8{background:#fffaf0;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(42,41,37,.08)}
.gp8{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.pc8{display:flex;flex-direction:column;align-items:center;gap:8px;text-align:center}
.pc8 .ar{height:160px;display:flex;align-items:center;justify-content:center}
.pc8 b{font:700 22px/1.3 Cardo}
.pk8{display:flex;flex-wrap:wrap;gap:4px;justify-content:center;width:150px;min-height:58px;align-content:flex-end}.pk8 i{width:22px;height:12px;border-radius:3px;background:#c49c63;box-shadow:inset 0 -3px 0 #a37c45}.pk8 i.bk{background:#4e6b2f;box-shadow:inset 0 -3px 0 #364d1f}
.pc8 span{font:600 16px/1.3 'Fira Sans'}.pc8 span.sh{color:#a2391a}
.lg8{display:flex;gap:16px}.lg8 span{display:flex;gap:6px;align-items:center;font:600 14px/1.2 'Fira Sans';color:#5f5747}.lg8 i{width:22px;height:12px;border-radius:3px;background:#c49c63}.lg8 i.bk{background:#4e6b2f}
.st8 .h{display:flex;justify-content:space-between;align-items:center}
.od8{flex:1;background:#fffaf0;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(42,41,37,.08);min-height:0}
.or8{flex:1;display:grid;grid-template-columns:1.8fr 1.1fr .9fr 1.2fr;gap:12px;align-items:center;border-top:1px solid #efe4cf}
.or8 b{display:block;font:700 19px/1.3 'Fira Sans'}.or8 span{font:500 15px/1.35 'Fira Sans';color:#6d6450}.or8 .q b{font:700 24px/1.25 Cardo}
.or8 em{font:700 15px/1.3 'Fira Sans';font-style:normal;border-radius:10px;padding:8px 10px;text-align:center;background:#e3ecd6;color:#3a5420}.or8 em.sh{background:#fbe1d6;color:#9b3216}
.pp8{background:#2a2925;color:#fff;border-radius:22px;padding:14px 20px;display:flex;gap:16px;align-items:center}.pp8 .sm8{color:#d8c49a;white-space:nowrap}.pp8 p{font:500 18px/1.45 'Fira Sans';text-wrap:pretty}
""", "<div class=kk>ARECA LEAF PLATE UNIT · STOCK AND ORDERS</div><h1>Plate stock counted by hand?<br><span>See packs ready by size.</span></h1>",
f'''<div class=vw><div class=st8><div class=h><span class=sm8>PACKS IN STOCK · 1 PACK = 25 PLATES · SAMPLE</span><div class=lg8><span><i class=bk></i>Booked</span><span><i></i>Free</span></div></div>
<div class=gp8>{"".join(f'<div class=pc8><div class=ar>{plate8(k, s)}</div><b>{n}</b><div class=pk8>{"".join(f"""<i class='{"bk" if j < p - LEFT8[n] else ""}'></i>""" for j in range(p))}</div><span class="{"sh" if LEFT8[n] == 0 else ""}">{p} packs · {LEFT8[n]} free</span></div>' for n, k, s, p in PL8)}</div></div>
<div class=od8><span class=sm8>ORDERS THIS WEEK</span>{"".join(f'<div class=or8><div><b>{o} · {w}</b><span>Pickup {d}</span></div><div><b>{sz}</b><span>{q * 25:,} plates</span></div><div class=q><b>{q}</b><span>{"pack" if q == 1 else "packs"}</span></div><em class="{"sh" if g < q else ""}">{"Ready" if g == q else f"{g} ready, {q - g} to press"}</em></div>' for o, w, sz, q, d, g in AL8)}</div>
<div class=pp8><span class=sm8>PRESSING PLAN</span><p>{"; ".join(f"Press {pl(q - g, 'pack')} of {sz} before {d[:3]}" for o, w, sz, q, d, g in AL8 if g < q)}.</p></div></div>''',
"#2a2925", "Make areca plates? DM us", "background:#4e6b2f;color:#fff")


# ───────── 399 CANADA · Horse boarding barn · SINGLE · Gelasio + Source Sans 3 · saddle brown / hay gold / frost white
# New technique: top-down SVG barn aisle with stalls coloured by turnout group, each stall carrying its feed (hay flakes as
# small bars, grain scoops as dots) and blanket chip, built from one boarder list; a whiteboard-vs-app contrast strip below.
BD9 = [("1", "A", 3, 1, "Medium"), ("2", "A", 2, 2, "None"), ("3", "B", 4, 1, "Heavy"), ("4", "B", 3, 0, "Medium"), ("5", "A", 3, 2, "Medium"),
       ("6", "Stall rest", 2, 1, "Light"), ("7", "B", 4, 2, "Heavy"), ("8", "A", 3, 1, "None"), ("9", "B", 2, 1, "Light"), ("10", "A", 3, 1, "Medium")]
GC9 = {"A": "#5c8a4a", "B": "#3f74a8", "Stall rest": "#b8862f"}
def barn9():
    W, H = 720, 380; sw = 136; sh = 150; out = []
    for i, (n, g, hay, sc, bl) in enumerate(BD9):
        r, c = divmod(i, 5); x = 12 + c * (sw + 6); y = 12 if r == 0 else 218
        col = GC9[g]
        out.append(f'<rect x="{x}" y="{y}" width="{sw}" height="{sh}" rx="10" fill="#fffaf2" stroke="{col}" stroke-width="5"/><rect x="{x}" y="{y}" width="{sw}" height="34" rx="10" fill="{col}"/>'
                   f'<text x="{x + 12}" y="{y + 24}" font-family="Source Sans 3" font-weight="700" font-size="18" fill="#fff">Stall {n}</text>'
                   f'<text x="{x + 12}" y="{y + 62}" font-family="Source Sans 3" font-weight="600" font-size="15" fill="#6b5a45">Hay {hay} flakes</text>'
                   + "".join(f'<rect x="{x + 12 + k * 22}" y="{y + 72}" width="18" height="12" rx="3" fill="#d9b44a"/>' for k in range(hay))
                   + f'<text x="{x + 12}" y="{y + 108}" font-family="Source Sans 3" font-weight="600" font-size="15" fill="#6b5a45">Grain {sc} {"scoop" if sc == 1 else "scoops"}</text>'
                   + "".join(f'<circle cx="{x + 20 + k * 20}" cy="{y + 122}" r="7" fill="#7a4e2d"/>' for k in range(sc))
                   + f'<text x="{x + sw - 10}" y="{y + 140}" text-anchor="end" font-family="Source Sans 3" font-weight="700" font-size="13" fill="{col}">Blanket: {bl}</text>')
    aisle = f'<rect x="12" y="172" width="{W - 24}" height="36" rx="8" fill="#e7dccb"/><text x="{W / 2}" y="196" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="15" fill="#6b5a45">Center aisle</text>'
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto">{aisle}{"".join(out)}</svg>'
P["p399_barn"] = page("""
body{--f:'Source Sans 3';--h:'Gelasio';background:#f6f1e8;color:#2f2219;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#8a5a2b;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:60px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#8a5a2b}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm9{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#7c6a55}
.bn9{flex:1;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;justify-content:center;box-shadow:0 14px 30px rgba(47,34,25,.08)}
.bn9 .h{display:flex;justify-content:space-between;align-items:center}
.lg9{display:flex;gap:14px}.lg9 span{display:flex;gap:6px;align-items:center;font:600 15px/1.2 'Source Sans 3';color:#5a4a3a}.lg9 i{width:16px;height:16px;border-radius:4px}
.bt9{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:14px}
.wb9{background:#fdfdfb;border:10px solid #c9c2b6;border-radius:14px;padding:12px 16px;display:flex;flex-direction:column;gap:4px}.wb9 .sm9{color:#a2391a}
.wb9 p{font:italic 600 21px/1.4 'Gelasio';color:#2b4a8a}.wb9 p s{color:#9a8f80}
.up9{background:#2f2219;color:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px}.up9 .sm9{color:#e0c48a}
.up9 .r{display:flex;justify-content:space-between;gap:10px;border-top:1px solid rgba(255,255,255,.12);padding-top:7px}.up9 .r span{font:500 17px/1.35 'Source Sans 3';color:#e8dccb}.up9 .r b{font:700 17px/1.35 'Source Sans 3';color:#ffd77a;white-space:nowrap}
""", "<div class=kk>HORSE BOARDING BARN · DAILY CARE</div><h1>Feed notes on a whiteboard?<br><span>Every stall's care in one app.</span></h1>",
f'''<div class=vw><div class=bn9><div class=h><span class=sm9>BARN TODAY · TURNOUT GROUPS · SAMPLE</span><div class=lg9>{"".join(f'<span><i style="background:{c}"></i>{"Paddock " + g if len(g) == 1 else g}</span>' for g, c in GC9.items())}</div></div>{barn9()}</div>
<div class=bt9><div class=wb9><span class=sm9>THE OLD WHITEBOARD</span><p><s>Stall 4: 2 scoops</s> 0 scoops?<br>Stall 6 stays in… till when?<br>Blankets if it gets cold</p></div>
<div class=up9><span class=sm9>OWNER UPDATES · THIS WEEK</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Stall 4 grain changed by owner", "Mon"), ("Stall 6 stays in, owner's note", "Till Fri"), ("Farrier visit booked, stalls 1-5", "Thu 10 AM"), ("Blankets on below -5 °C", "Owner rule")])}</div></div></div>''',
"#2f2219", "Run a boarding barn? DM us", "background:#8a5a2b;color:#fff")


# ───────── 400 INDIA · Goat farm · SINGLE · Poppins + Inter · pasture olive / goat tan / clay
# New technique: per-goat cards with a CSS clip-path ear tag and an SVG monthly weight line that turns green when it
# crosses the target weight; buyer bookings are matched to goats that are at target, in Python.
GT0 = [("G-07", [14, 18, 22, 26, 29, 32]), ("G-11", [12, 15, 19, 22, 25, 27]), ("G-14", [15, 19, 23, 27, 31, 34]), ("G-18", [11, 13, 16, 19, 21, 23]),
       ("G-21", [13, 17, 21, 24, 28, 31]), ("G-25", [10, 12, 15, 17, 20, 22])]
TGT0 = 30
MON0 = ["Jun", "Jul", "Aug", "Sep", "Oct", "Nov"]
READY0 = [g for g, w in GT0 if w[-1] >= TGT0]
BK0 = [("B-31", "Sample Buyer A", 1, "Sat 28 Nov"), ("B-32", "Sample Livestock Trader", 2, "Tue 1 Dec")]
asg0 = []; pool = list(READY0)
for b, who, n, d in BK0:
    asg0.append((b, who, n, d, pool[:n])); pool = pool[n:]
def line0(w):
    W, H = 220, 90; mn, mx = 8, 36
    pts = [(10 + i * (W - 20) / 5, H - 10 - (v - mn) / (mx - mn) * (H - 20)) for i, v in enumerate(w)]
    ty = H - 10 - (TGT0 - mn) / (mx - mn) * (H - 20)
    col = "#4f7a2a" if w[-1] >= TGT0 else "#b0703c"
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto"><line x1="6" y1="{ty:.1f}" x2="{W - 6}" y2="{ty:.1f}" stroke="#c94f3a" stroke-width="2" stroke-dasharray="5 4"/>
<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}" fill="none" stroke="{col}" stroke-width="4" stroke-linejoin="round"/>{"".join(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="4.5" fill="{col}"/>' for x, y in pts)}</svg>'''
P["p400_goat"] = page("""
body{--f:'Inter';--h:'Poppins';background:#f3efe2;color:#2c2a1e}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#a35a2e;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#4f7a2a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm0{font:800 13px/1.4 Inter;letter-spacing:2px;color:#7c7559}
.hd0{display:flex;justify-content:space-between;align-items:center}
.lg0{display:flex;gap:14px}.lg0 span{display:flex;gap:6px;align-items:center;font:600 14px/1.2 Inter;color:#5a5540}.lg0 i{width:22px;height:0;border-top:3px dashed #c94f3a}
.gg0{flex:1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;min-height:0}
.gc0{background:#fff;border-radius:22px;padding:14px 16px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(44,42,30,.08)}.gc0.rd{box-shadow:0 0 0 3px #4f7a2a,0 12px 26px rgba(44,42,30,.08)}
.gc0 .t{display:flex;justify-content:space-between;align-items:center}
.tag0{width:74px;height:56px;background:#f2c230;clip-path:polygon(50% 0,100% 22%,100% 100%,0 100%,0 22%);display:flex;align-items:flex-end;justify-content:center;padding-bottom:9px;font:800 15px/1 Inter;position:relative}
.tag0::before{content:'';position:absolute;top:10px;left:50%;width:10px;height:10px;margin-left:-5px;border-radius:50%;background:#fff}
.gc0 .w{text-align:right}.gc0 .w b{display:block;font:800 30px/1.2 Poppins}.gc0 .w span{font:600 14px/1.3 Inter;color:#7c7559}
.gc0 .ln{flex:1;display:flex;align-items:center}
.gc0 .mo{display:flex;justify-content:space-between;font:500 12px/1.2 Inter;color:#8c8668;padding:0 4px}
.gc0 em{font:700 15px/1.3 Inter;font-style:normal;border-radius:10px;padding:7px 10px;text-align:center;background:#f6ead9;color:#8a4a20}.gc0.rd em{background:#e3eed6;color:#3a5a1c}
.bk0{background:#2c2a1e;color:#fff;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;gap:8px}.bk0 .sm0{color:#d8cf9e}
.bk0 .r{display:grid;grid-template-columns:1.6fr 1.1fr 1.3fr;gap:12px;align-items:center;border-top:1px solid rgba(255,255,255,.12);padding-top:8px}
.bk0 b{font:700 18px/1.3 Inter}.bk0 span{font:500 16px/1.3 Inter;color:#d6d0b8}.bk0 i{font:700 15px/1.2 Inter;font-style:normal;background:#4f7a2a;border-radius:10px;padding:7px 10px}.bk0 .gs{display:flex;gap:6px}
""", "<div class=kk>GOAT FARM · WEIGHT AND SALES</div><h1>Selling goats by guesswork?<br><span>Weigh monthly, sell on time.</span></h1>",
f'''<div class=vw><div class=hd0><span class=sm0>MONTHLY WEIGHT · KG · TARGET {TGT0} KG · SAMPLE</span><div class=lg0><span><i></i>Target weight</span></div></div>
<div class=gg0>{"".join(f'<div class="gc0 {"rd" if w[-1] >= TGT0 else ""}"><div class=t><div class=tag0>{g}</div><div class=w><b>{w[-1]} kg</b><span>+{w[-1] - w[-2]} kg this month</span></div></div><div class=ln>{line0(w)}</div><div class=mo>{"".join(f"<span>{m}</span>" for m in MON0)}</div><em>{"At target · ready to sell" if w[-1] >= TGT0 else f"{TGT0 - w[-1]} kg to target"}</em></div>' for g, w in GT0)}</div>
<div class=bk0><span class=sm0>BUYER BOOKINGS · GOATS AT TARGET ARE OFFERED FIRST</span>{"".join(f'<div class=r><div><b>{b} · {who}</b></div><span>{pl(n, "goat")} · {d}</span><div class=gs>{"".join(f"<i>{x}</i>" for x in gs)}</div></div>' for b, who, n, d, gs in asg0)}</div></div>''',
"#2c2a1e", "Run a goat farm? DM us", "background:#4f7a2a;color:#fff")


# ───────── 397 USA · Rug cleaning (pickup and delivery) · CAROUSEL 5 · Crimson Text + Inter · rug terracotta / wool cream / sage
# New technique: CSS rugs (border bands, medallion or stripe field, fringe ends via repeating gradients) drawn to scale in
# feet from one order list; the hanging drying rack, size form, ticket and delivery route all read that same list.
RP7 = {"med": ("#b5532f", "#f2e3c9", "#2f4a5c"), "str": ("#6f8f72", "#f6efe4", "#b5532f"), "grd": ("#2f4a5c", "#e9dcc4", "#c9873a")}
def rug7(w, h, kind, vert=False, tag=None):
    a, b, c = RP7[kind]
    if kind == "med": field = f"radial-gradient(ellipse at center,{c} 0 18%,{b} 19% 26%,{a} 27% 100%)"
    elif kind == "str": field = f"repeating-linear-gradient({0 if vert else 90}deg,{a} 0 14px,{b} 14px 22px,{c} 22px 28px,{b} 28px 36px)"
    else: field = f"repeating-linear-gradient(0deg,transparent 0 22px,{c} 22px 25px),repeating-linear-gradient(90deg,transparent 0 22px,{c} 22px 25px),{a}"
    fr = "repeating-linear-gradient(90deg,#efe5d2 0 3px,transparent 3px 6px)" if vert else "repeating-linear-gradient(0deg,#efe5d2 0 3px,transparent 3px 6px)"
    fp = (f"left:6px;right:6px;bottom:-14px;height:14px" if vert else f"top:6px;bottom:6px;right:-14px;width:14px")
    fp2 = (f"left:6px;right:6px;top:-14px;height:14px" if vert and not tag else ("top:6px;bottom:6px;left:-14px;width:14px" if not vert else "display:none"))
    t = f'<span class=tg7>{tag}</span>' if tag else ""
    return f'<div class=rg7 style="width:{w}px;height:{h}px;background:{field};box-shadow:inset 0 0 0 7px {b},inset 0 0 0 12px {c},0 10px 20px rgba(42,35,32,.18)"><i class=free style="position:absolute;{fp};background:{fr}"></i><i class=free style="position:absolute;{fp2};background:{fr}"></i>{t}</div>'
OR7 = [("A", "8 × 10 ft", 8, 10, "med", "Wool"), ("B", "5 × 8 ft", 5, 8, "grd", "Wool"), ("C", "2.5 × 8 ft runner", 2.5, 8, "str", "Synthetic")]
SQ7 = sum(w * h for _, _, w, h, _, _ in OR7)
B7 = """
body{--f:'Inter';--h:'Crimson Text';background:#f6efe4;color:#2a2320;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#b5532f;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:64px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#b5532f}
.cd7{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(42,35,32,.08)}
.sm7{font:700 13px/1.4 Inter;letter-spacing:2px;color:#7d6f62}
.rg7{position:relative;flex:none}
.tg7{position:absolute;top:18px;left:50%;transform:translateX(-50%);background:#fff;border:2px solid #2a2320;border-radius:8px;padding:5px 9px;font:800 15px/1.2 Inter;white-space:nowrap}
.bb7{background:#2a2320;color:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}.bb7 b{font:700 20px/1.3 Inter}.bb7 span{font:500 16px/1.35 Inter;color:#d8ccbf}
"""
def t7(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2a2320;color:#f6c9a8"):
    return page(B7 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2a2320", cta, ctacss, tagline=f"{n} / 5")
RK7 = [(190, 600, "med", "?"), (156, 500, "grd", "Name?"), (112, 560, "str", "?"), (166, 450, "grd", "Order 4?"), (140, 580, "med", "?")]
P["p397_rug_s1"] = t7(1, "RUG CLEANING · PICKUP AND DELIVERY", "Whose rug is this one?<br><span>Tag every rug at pickup.</span>",
f'''<div class=w71><div class="cd7 rk71"><span class=sm7>DRYING RACK TODAY · NO TAGS · SAMPLE</span><div class=pole></div><div class=hg>{"".join(rug7(w, h, k, True, t) for w, h, k, t in RK7)}</div></div>
<div class=pn71>{"".join(f'<div class=bb7><b>{a}</b><span>{b}</span></div>' for a, b in [("“Is my rug done?”", "Owner checks the rack"), ("“How big was it?”", "Quote was a guess"), ("“When do you deliver?”", "Calls all afternoon")])}</div></div>''',
css=""".w71{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rk71{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:6px;min-height:0}
.rk71 .pole{height:14px;border-radius:7px;background:linear-gradient(#9aa0a6,#6d7378);margin:18px 10px 0}
.rk71 .hg{flex:1;display:flex;justify-content:space-around;align-items:flex-start;padding-top:22px}
.rk71 .tg7{border-color:#c0392b;color:#c0392b;background:#fff4f0}
.pn71{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.pn71 .bb7 b{font-size:22px}.pn71 .bb7 span{font-size:18px}""")
S7 = 28
P["p397_rug_s2"] = t7(2, "1 · BOOK PICKUP WITH SIZES", "Get the rug sizes first.<br><span>Quote by the square foot.</span>",
f'''<div class=w72><div class="cd7 fm72"><span class=sm7>PICKUP REQUEST · RC-118 · SAMPLE</span>{"".join(f'<div class=fd><small>{a}</small><b>{b}</b></div>' for a, b in [("ZIP code", "00041 · in our area"), ("How many rugs", "3")])}
{"".join(f'<div class=fd><small>Rug {r}</small><b>{d} · {m} · <em>{w * h:g} sq ft</em></b></div>' for r, d, w, h, _, m in OR7)}
<div class=tot><span>Total to clean</span><b>{SQ7:g} sq ft</b></div>{"".join(f'<div class=fd><small>{a}</small><b>{b}</b></div>' for a, b in [("Pickup window", "Tue 17 Nov, 1-3 PM"), ("Photos", "3 added, one stain marked")])}</div>
<div class="cd7 sc72"><span class=sm7>DRAWN TO SCALE · 1 SQUARE = 1 FT</span><div class=fl>{"".join(f'<div class=it>{rug7(w * S7, h * S7, k)}<b>Rug {r}</b><span>{d}</span></div>' for r, d, w, h, k, _ in OR7)}</div></div></div>''',
css=""".w72{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr);gap:16px;min-height:0}
.fm72{padding:18px 20px;display:flex;flex-direction:column;gap:4px}.fm72 .fd{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1px solid #f0e8dc}
.fm72 small{font:500 14px/1.3 Inter;color:#7d6f62}.fm72 b{font:600 18px/1.3 Inter}.fm72 b em{font-style:normal;color:#b5532f}
.fm72 .tot{display:flex;justify-content:space-between;align-items:center;background:#2a2320;color:#fff;border-radius:14px;padding:12px 16px;margin:4px 0}.fm72 .tot span{font:600 16px/1.3 Inter}.fm72 .tot b{font:700 26px/1.2 'Crimson Text';color:#f6c9a8}
.sc72{padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.sc72 .fl{flex:1;border-radius:16px;background:#efe6d6;background-image:linear-gradient(#e2d6c2 1px,transparent 1px),linear-gradient(90deg,#e2d6c2 1px,transparent 1px);background-size:26px 26px;display:flex;align-items:center;justify-content:space-evenly;padding:30px 10px}
.sc72 .it{display:flex;flex-direction:column;align-items:center;gap:6px}.sc72 .it b{font:700 18px/1.3 Inter;margin-top:12px}.sc72 .it span{font:500 15px/1.3 Inter;color:#5f5247}""")
TL7 = [("Picked up", "Tue 17 Nov", 1), ("Checked and photos", "Wed 18 Nov", 1), ("Washed", "Thu 19 Nov", 1), ("Drying", "Fri 20 - Sun 22 Nov", 1), ("Ready, final check", "Today, Mon 23 Nov", 2), ("Delivery", "Wed 25 Nov, 1-3 PM", 0)]
P["p397_rug_s3"] = t7(3, "2 · TAG, PHOTO, TRACK", "One ticket for every rug.<br><span>Every step on record.</span>",
f'''<div class=w73><div class=tk73><div class=hd><b>RUG TICKET</b><span>RC-118-A</span></div><div class=bc>{"".join(f'<i style="width:{w}px"></i>' for w in [3, 6, 2, 4, 2, 7, 3, 2, 5, 3, 2, 6, 4, 2, 3, 7, 2, 4, 3, 5, 2, 6, 3, 2])}</div>
{"".join(f'<div class=ln><span>{a}</span><b>{b}</b></div>' for a, b in [("Order", "RC-118 · 3 rugs"), ("Rug", "A · 8 × 10 ft · wool"), ("Area", "80 sq ft"), ("Cleaning", "Full wash, fringe fix"), ("Ready by", "Mon 23 Nov")])}
<div class=ph>{"".join(f'<div>{ic("camera", 26, "#8a7b6c", 1.8)}<span>{t}</span></div>' for t in ["Front", "Back", "Stain"])}</div>
<div class=nt><span>Notes at pickup</span>{"".join(f'<i>{t}</i>' for t in ["Fringe loose on one end", "Stain marked near corner"])}</div></div>
<div class="cd7 tl73"><span class=sm7>RC-118 · STATUS · SAMPLE</span>{"".join(f'<div class="st s{d}"><i></i><div><b>{a}</b><span>{b}</span></div></div>' for a, b, d in TL7)}</div></div>''',
css=""".w73{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}
.tk73{background:#fffdf8;border-radius:12px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 18px 34px rgba(42,35,32,.12);border-top:10px solid #b5532f;-webkit-mask:radial-gradient(circle 12px at 0 50%,transparent 98%,#000) left/51% 100% no-repeat,radial-gradient(circle 12px at 100% 50%,transparent 98%,#000) right/51% 100% no-repeat}
.tk73 .hd{display:flex;justify-content:space-between;align-items:center}.tk73 .hd b{font:700 26px/1.3 'Crimson Text';letter-spacing:1px}.tk73 .hd span{font:800 20px/1.2 Inter;color:#b5532f}
.tk73 .bc{height:54px;display:flex;gap:3px}.tk73 .bc i{display:block;background:#2a2320}
.tk73 .ln{flex:1;align-items:center;display:flex;justify-content:space-between;border-top:1px dashed #e2d6c2;padding-top:8px}.tk73 .ln span{font:500 16px/1.3 Inter;color:#7d6f62}.tk73 .ln b{font:700 18px/1.3 Inter}
.tk73 .ph{height:120px;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.tk73 .ph>div{border-radius:10px;background:#efe6d6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}.tk73 .ph span{font:600 14px/1.2 Inter;color:#6d6055}
.tk73 .nt{display:flex;flex-direction:column;gap:6px}.tk73 .nt span{font:600 15px/1.3 Inter;color:#7d6f62}.tk73 .nt i{font:600 17px/1.3 Inter;font-style:normal;background:#fbe6dc;color:#8e3b1d;border-radius:10px;padding:8px 12px}
.tl73{padding:18px 22px;display:flex;flex-direction:column;gap:0}
.tl73 .st{flex:1;display:flex;gap:16px;align-items:center;position:relative}.tl73 .st i{width:26px;height:26px;border-radius:50%;flex:none;border:4px solid #d9cdbd;background:#fff;z-index:1}
.tl73 .st::before{content:'';position:absolute;left:11px;top:0;bottom:0;width:4px;background:#e9dfd1}.tl73 .st:first-of-type::before{top:50%}.tl73 .st:last-child::before{bottom:50%}
.tl73 .s1 i{background:#6f8f72;border-color:#6f8f72}.tl73 .s2 i{background:#fff;border-color:#b5532f;box-shadow:0 0 0 5px #f7d9cb}
.tl73 b{display:block;font:700 20px/1.3 Inter}.tl73 .st span{font:500 16px/1.35 Inter;color:#6d6055}.tl73 .s2 b{color:#b5532f}""")
ST7 = [("Shop", 70, 300, None), ("1", 210, 120, ("RC-115", "00039", 1, "10-12")), ("2", 430, 90, ("RC-118", "00041", 3, "1-3")), ("3", 560, 250, ("RC-120", "00041", 2, "1-3")), ("4", 330, 330, ("RC-121", "00044", 1, "3-5"))]
def map7():
    W, H = 640, 400
    st = "".join(f'<line x1="{x}" y1="0" x2="{x}" y2="{H}" stroke="#e3d8c6" stroke-width="10"/>' for x in range(40, W, 120)) + "".join(f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="#e3d8c6" stroke-width="10"/>' for y in range(50, H, 110))
    route = " ".join(f"{x},{y}" for _, x, y, _ in ST7)
    pins = ""
    for n, x, y, d in ST7:
        col = "#2a2320" if d is None else ("#b5532f" if n == "2" else "#6f8f72")
        pins += f'<circle cx="{x}" cy="{y}" r="22" fill="{col}" stroke="#fff" stroke-width="4"/>'
        pins += f'<text x="{x}" y="{y + 6}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="{13 if d is None else 18}" fill="#fff">{n}</text>'
    return f'<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto;border-radius:14px"><rect width="{W}" height="{H}" fill="#f4ecdf"/>{st}<polyline points="{route}" fill="none" stroke="#2a2320" stroke-width="4" stroke-dasharray="10 8"/>{pins}</svg>'
P["p397_rug_s4"] = t7(4, "3 · DELIVERY BY AREA", "Clean rugs, clear windows.<br><span>One route, texts sent ahead.</span>",
f'''<div class=w74><div class="cd7 mp74"><span class=sm7>WED 25 NOV · DELIVERY ROUTE · SAMPLE</span>{map7()}</div>
<div class=bt74><div class="cd7 ls74">{"".join(f'<div class="r {"on" if n == "2" else ""}"><b>{n}</b><div><strong>{d[0]} · ZIP {d[1]}</strong><span>{pl(d[2], "rug")} · {d[3]} PM</span></div></div>'.replace("10-12 PM", "10-12 AM") for n, x, y, d in ST7 if d)}</div>
<div class="cd7 ms74"><span class=sm7>TEXT TO RC-118 · MON 23 NOV</span><p>Your 3 rugs are clean and ready. We will deliver on Wed 25 Nov between 1 and 3 PM. Reply 1 to confirm, 2 to change the day.</p></div></div></div>''',
css=""".w74{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.mp74{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:10px;justify-content:center;min-height:0}.mp74 svg{max-height:370px;width:auto!important;align-self:center}
.bt74{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:14px}.ls74{padding:12px 18px;display:flex;flex-direction:column}
.ls74 .r{flex:1;display:flex;gap:14px;align-items:center;border-top:1px solid #f0e8dc;padding:7px 0}.ls74 .r:first-child{border-top:0}.ls74 .r>b{width:40px;height:40px;border-radius:50%;background:#6f8f72;color:#fff;display:flex;align-items:center;justify-content:center;font:800 17px/1 Inter;flex:none}
.ls74 .r.on>b{background:#b5532f}.ls74 strong{display:block;font:700 18px/1.3 Inter}.ls74 span{font:500 15px/1.3 Inter;color:#6d6055}
.ms74{padding:18px 20px;display:flex;flex-direction:column;gap:10px;justify-content:center;background:#fbeadf}.ms74 p{font:500 20px/1.45 Inter;text-wrap:pretty}""")
P["p397_rug_s5"] = t7(5, "RUG CLEANING APP", "Clean rugs for a living?<br><span>Let's build your rug app.</span>",
f'''<div class=w75><div class=rw75>{"".join(rug7(w * 20, h * 20, k) for _, _, w, h, k, _ in OR7)}</div><div class=tl75>{"".join(f'<div class=cd7><span class=ib>{ic(i, 30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("doc", "Pickup form", "Sizes and square feet"), ("tag", "Rug tickets", "Photos and notes"), ("clock", "Status steps", "Picked up to ready"), ("map", "Delivery route", "Windows and texts")])}</div>
<div class=q75><span class=sm7>A QUESTION FOR RUG CLEANERS</span><p>How do you keep track of each rug today: paper tags, tape or memory? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss="background:#b5532f;color:#fff",
css=""".w75{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}.rw75{display:flex;gap:36px;justify-content:center;align-items:center;padding:6px 0 4px}
.tl75{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.tl75>div{padding:20px 22px;display:flex;gap:16px;align-items:center}.tl75 .ib{width:80px;height:80px;border-radius:18px;background:#6f8f72;color:#fff}
.tl75 b{display:block;font:700 38px/1.3 'Crimson Text'}.tl75 span{font:500 22px/1.4 Inter;color:#6d6055}
.q75{background:#2a2320;color:#fff;border-radius:24px;padding:24px 28px;display:flex;flex-direction:column;gap:10px}.q75 .sm7{color:#f6c9a8}.q75 p{font:600 32px/1.35 'Crimson Text';text-wrap:pretty}""")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
