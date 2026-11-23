import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 391 INDIA · Cashew processing unit · SINGLE · Bitter + Inter · cashew cream / roast amber / deep olive
# New technique: SVG cashew kernels drawn to relative size per grade (W180 biggest .. splits as a half kernel) over a
# tin isotype per grade (1 tin = 10 kg); orders are allocated by delivery date in Python, so booked / free / short all agree.
GR1 = [("W180", "about 180 per lb", 40, 70), ("W240", "about 240 per lb", 90, 62), ("W320", "about 320 per lb", 120, 54), ("W450", "about 450 per lb", 60, 46), ("Splits", "split in two halves", 50, 54)]
OR1 = [("O-52", "Sample Sweet Maker", "Splits", 50, "Wed 25 Nov", 2), ("O-53", "Sample Wholesaler", "W320", 70, "Thu 26 Nov", 3), ("O-51", "Sample Dry Fruit Store", "W240", 60, "Fri 27 Nov", 4),
       ("O-54", "Sample Gift Box Maker", "W180", 20, "Sat 28 Nov", 5), ("O-55", "Sample Bakery", "W240", 40, "Mon 30 Nov", 7)]
def alloc1():
    left = {g: kg for g, _, kg, _ in GR1}; out = []
    for o in sorted(OR1, key=lambda x: x[5]):
        t = min(o[3], left[o[2]]); left[o[2]] -= t; out.append(o + (t,))
    return out, left
AL1, LEFT1 = alloc1()
BOOK1 = {g: sum(a[6] for a in AL1 if a[2] == g) for g, *_ in GR1}
SHORT1 = [a for a in AL1 if a[6] < a[3]]
KP1 = "M88 30 C88 12 70 4 52 6 C30 8 10 20 10 40 C10 56 24 66 38 64 C48 62 50 54 46 48 C42 42 44 34 54 32 C64 30 72 40 80 42 C86 43 88 38 88 30Z"
def kern1(g, s, i):
    half = g == "Splits"
    clip = f'<clipPath id="hk{i}"><rect x="0" y="0" width="100" height="36"/></clipPath>' if half else ""
    return f'''<svg viewBox="0 0 100 70" width="{s * 1.5:.0f}" height="{s * 1.05:.0f}" style="display:block"><defs>{clip}<linearGradient id="kg{i}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7e6c2"/><stop offset="1" stop-color="#e2bf86"/></linearGradient></defs>
<path d="{KP1}" fill="url(#kg{i})" stroke="#b9853f" stroke-width="2.5" {""}/>{'<path d="M16 46 C22 26 44 12 66 12 C76 12 84 18 86 28" stroke="#9a6a2c" stroke-width="2.5" fill="none" stroke-dasharray="5 4"/>' if half else ""}{'' if half else '<path d="M30 22 C40 16 56 14 68 16" stroke="#fff6e0" stroke-width="4" fill="none" stroke-linecap="round"/>'}</svg>'''
def tins1(g, kg):
    n = kg // 10; b = BOOK1[g] // 10
    return "".join(f'<i class="{"bk" if k < b else ""}"></i>' for k in range(n))
P["p391_cashew"] = page("""
body{--f:'Inter';--h:'Bitter';background:#f6efe0;color:#2c2a1f;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#8a5a1c;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;line-height:1.2;letter-spacing:-1px} h1 span{color:#c77a2a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm1{font:800 13px/1.4 Inter;letter-spacing:2px;color:#7d7259}
.gc1{background:#fff;border-radius:26px;padding:18px 20px;display:flex;flex-direction:column;gap:12px;box-shadow:0 14px 30px rgba(44,42,31,.08)}
.gc1 .h{display:flex;justify-content:space-between;align-items:center;gap:10px}
.lg1{display:flex;gap:14px}.lg1 span{display:flex;gap:6px;align-items:center;font:600 14px/1.2 Inter;color:#5f5743}.lg1 i{width:14px;height:16px;border-radius:3px;border:2px solid #b9853f;background:#fbf4e4}.lg1 i.bk{background:#c77a2a;border-color:#a35f17}
.gg1{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
.gd1{display:flex;flex-direction:column;gap:6px;align-items:center;text-align:center;background:#fbf6ea;border-radius:18px;padding:12px 8px}
.gd1 .kw{height:76px;display:flex;align-items:center;justify-content:center}
.gd1 b{font:800 28px/1.25 Bitter}.gd1 small{font:500 14px/1.3 Inter;color:#7d7259}
.tn1{display:grid;grid-template-columns:repeat(4,22px);gap:6px;justify-content:center;min-height:86px;align-content:end;margin-top:4px}
.tn1 i{height:22px;border-radius:4px 4px 3px 3px;border:2px solid #b9853f;background:#fbf4e4;box-shadow:inset 0 4px 0 #e9d3a6}.tn1 i.bk{background:#c77a2a;border-color:#a35f17;box-shadow:inset 0 4px 0 #e39a4b}
.gd1 .fr{font:700 16px/1.3 Inter;color:#3d4a2a}.gd1 .fr.sh{color:#b3261e}
.oc1{flex:1;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(44,42,31,.08);min-height:0}
.or1{flex:1;display:grid;grid-template-columns:1.9fr .8fr .8fr 1.25fr;gap:12px;align-items:center;border-top:1px solid #f0e7d4}
.or1 b{display:block;font:700 19px/1.3 Inter}.or1 span{font:500 15px/1.35 Inter;color:#6d6550}
.or1 .gt{font:800 18px/1.2 Bitter;background:#f6e6c8;color:#7a4a12;border-radius:10px;padding:8px 10px;text-align:center}
.or1 .kg b{font:800 22px/1.2 Bitter}
.st1{font:700 15px/1.3 Inter;border-radius:10px;padding:8px 10px;text-align:center;background:#e4ecd6;color:#3d4a2a}.st1.sh{background:#fbe1dc;color:#9b2219}
.ms1{background:#3d4a2a;color:#fff;border-radius:22px;padding:14px 20px;display:flex;gap:16px;align-items:center}.ms1 .sm1{color:#d9e3b8;white-space:nowrap}.ms1 p{font:500 18px/1.45 Inter;text-wrap:pretty}
""", "<div class=kk>CASHEW PROCESSING UNIT · STOCK AND ORDERS</div><h1>“Is W240 ready for Monday?”<br><span>See stock by grade, not by guess.</span></h1>",
f'''<div class=vw><div class=gc1><div class=h><span class=sm1>STOCK BY GRADE · 1 TIN = 10 KG · SAMPLE</span><div class=lg1><span><i class=bk></i>Booked</span><span><i></i>Free</span></div></div>
<div class=gg1>{"".join(f'<div class=gd1><div class=kw>{kern1(g, s, i)}</div><b>{g}</b><small>{d}</small><div class=tn1>{tins1(g, kg)}</div><span class="fr {"sh" if LEFT1[g] == 0 and any(a[2] == g for a in SHORT1) else ""}">{kg} kg · {LEFT1[g]} kg free</span></div>' for i, (g, d, kg, s) in enumerate(GR1))}</div></div>
<div class=oc1><span class=sm1>ORDERS · FILLED BY DELIVERY DATE</span>{"".join(f'<div class=or1><div><b>{o} · {who}</b><span>Deliver {dt}</span></div><span class=gt>{g}</span><div class=kg><b>{kg} kg</b></div><span class="st1 {"sh" if got < kg else ""}">{"Ready" if got == kg else f"{got} ready, {kg - got} short"}</span></div>' for o, who, g, kg, dt, _, got in AL1)}</div>
<div class=ms1><span class=sm1>ALERT TO OWNER</span><p>{SHORT1[0][2]} is {SHORT1[0][3] - SHORT1[0][6]} kg short for {SHORT1[0][0]} ({SHORT1[0][4]}). Grade the next batch before then.</p></div></div>''',
"#2c2a1f", "Process cashews? DM us", "background:#c77a2a;color:#fff")


# ───────── 393 INDIA · Rolling shutter and grill fabricator · SINGLE · Anton + Fira Sans · red oxide / zinc grey / chalk
# New technique: SVG front elevation of a rolling shutter (drum box, slat lines, guide channels, centre lock) with true
# dimension arrows; the site-measure form and the stage tracker (6 stage dots per job) come from one job list.
def shut3():
    W, H = 420, 330
    sl = "".join(f'<rect x="58" y="{70 + k * 12}" width="304" height="12" fill="{"#9aa3ab" if k % 2 else "#a9b1b8"}"/><line x1="58" y1="{70 + k * 12}" x2="362" y2="{70 + k * 12}" stroke="#7d868e" stroke-width="1.2"/>' for k in range(19))
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;zoom:1.13"><rect x="40" y="26" width="340" height="44" rx="6" fill="#a8432a"/><rect x="48" y="34" width="324" height="28" rx="4" fill="#bf5a3e"/>
<rect x="44" y="70" width="14" height="230" fill="#6f7880"/><rect x="362" y="70" width="14" height="230" fill="#6f7880"/>{sl}
<rect x="58" y="296" width="304" height="8" fill="#5e676f"/><rect x="194" y="272" width="32" height="20" rx="4" fill="#3a4046"/><circle cx="210" cy="282" r="4" fill="#d6dbe0"/>
<rect x="30" y="304" width="360" height="6" fill="#c9c4bb"/>
<line x1="58" y1="14" x2="362" y2="14" stroke="#22262a" stroke-width="2"/><path d="M58 14 l10 -6 v12z M362 14 l-10 -6 v12z" fill="#22262a"/>
<rect x="160" y="2" width="100" height="24" rx="6" fill="#fff"/><text x="210" y="20" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="16" fill="#22262a">10 ft 6 in</text>
<line x1="404" y1="70" x2="404" y2="304" stroke="#22262a" stroke-width="2"/><path d="M404 70 l-6 10 h12z M404 304 l-6 -10 h12z" fill="#22262a"/>
<rect x="386" y="170" width="34" height="40" rx="6" fill="#fff"/><text x="403" y="187" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="14" fill="#22262a">9 ft</text><text x="403" y="203" text-anchor="middle" font-family="Fira Sans" font-weight="500" font-size="11" fill="#5e676f">high</text></svg>'''
ST3 = ["Measured", "Cut", "Welded", "Primer", "Painted", "Fitted"]
JB3 = [("J-11", "Sample Medical Store", "Shutter 8 × 9 ft", 5, "Fitting today"), ("J-12", "Sample Godown", "Shutter 14 × 12 ft, motor", 3, "Paint Wed"),
       ("J-14", "Sample Shop, Main Road", "Shutter 10.5 × 9 ft", 3, "Fitting Thu 26 Nov"), ("J-15", "Sample House", "Window grill × 6", 2, "Primer Wed"), ("J-16", "Sample Office", "Safety door", 1, "Cutting Tue")]
P["p393_shutter"] = page("""
body{--f:'Fira Sans';--h:'Anton';background:#f2f0ec;color:#22262a}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#a8432a;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.25;letter-spacing:.3px;margin-top:30px} h1 span{color:#a8432a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm3{font:700 13px/1.5 'Fira Sans';letter-spacing:2px;color:#6b737a}
.tp3{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:14px}
.dw3{background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(34,38,42,.08)}
.fm3{background:#22262a;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.fm3 .sm3{color:#c3cad0}
.fm3 .fd{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid rgba(255,255,255,.12)}
.fm3 .fd span{font:500 16px/1.3 'Fira Sans';color:#c3cad0}.fm3 .fd b{font:600 19px/1.3 'Fira Sans';text-align:right}
.fm3 .ph{display:flex;gap:8px}.fm3 .ph i{width:56px;height:44px;border-radius:8px;background:#3a4046;display:flex;align-items:center;justify-content:center}
.jb3{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(34,38,42,.08);min-height:0}
.jh3{display:grid;grid-template-columns:1.7fr repeat(6,64px) 1.1fr;gap:8px;align-items:center}
.jh3 em{font:600 13px/1.3 'Fira Sans';font-style:normal;color:#6b737a;text-align:center}
.jr3{flex:1;display:grid;grid-template-columns:1.7fr repeat(6,64px) 1.1fr;gap:8px;align-items:center;border-top:1px solid #ece8e1}
.jr3 b{display:block;font:700 19px/1.3 'Fira Sans'}.jr3 span{font:500 15px/1.35 'Fira Sans';color:#5e676f}
.jr3 .d{justify-self:center;width:26px;height:26px;border-radius:50%;border:3px solid #d5d1c9}.jr3 .d.on{background:#a8432a;border-color:#a8432a}.jr3 .d.nw{border-color:#a8432a;box-shadow:inset 0 0 0 4px #fff,inset 0 0 0 10px #e7a593}
.jr3 .nx{font:700 15px/1.3 'Fira Sans';background:#f6e3dc;color:#8a3420;border-radius:10px;padding:8px 10px;text-align:center}
.ms3{background:#a8432a;color:#fff;border-radius:22px;padding:14px 20px;display:flex;gap:16px;align-items:center}.ms3 .sm3{color:#f6d3c7;white-space:nowrap}.ms3 p{font:500 18px/1.45 'Fira Sans';text-wrap:pretty}
""", "<div class=kk>ROLLING SHUTTER AND GRILL WORKS</div><h1>Shutter size on a scrap of paper?<br><span>Measure the site in the app.</span></h1>",
f'''<div class=vw><div class=tp3><div class=dw3><span class=sm3>J-14 · FRONT VIEW · CLEAR OPENING</span>{shut3()}</div>
<div class=fm3><span class=sm3>SITE MEASURE · J-14 · SAMPLE</span>{"".join(f'<div class=fd><span>{a}</span><b>{b}</b></div>' for a, b in [("Site", "Sample Shop, Main Road"), ("Width", "10 ft 6 in"), ("Height", "9 ft"), ("Slats", "Plain, 18 gauge"), ("Open by", "Hand, centre lock"), ("Colour", "Grey")])}<div class=fd><span>Photos</span><div class=ph>{"".join(f"<i>{ic('camera', 24, '#c3cad0', 1.8)}</i>" for _ in range(3))}</div></div></div></div>
<div class=jb3><div class=jh3><span class=sm3>JOBS THIS WEEK</span>{"".join(f"<em>{s}</em>" for s in ST3)}<em>Next</em></div>{"".join(f'<div class=jr3><div><b>{j} · {who}</b><span>{what}</span></div>' + "".join(f'<i class="d {"on" if k < n else ("nw" if k == n else "")}"></i>' for k in range(6)) + f'<span class=nx>{nx}</span></div>' for j, who, what, n, nx in JB3)}</div>
<div class=ms3><span class=sm3>AUTO MESSAGE</span><p>Your shutter J-14 is in primer now. Fitting on Thursday, 26 Nov, at 10 AM.</p></div></div>''',
"#22262a", "Make shutters or grills? DM us", "background:#22262a;color:#fff")


# ───────── 395 USA · Epoxy garage floor installer · SINGLE · Montserrat + Inter · slate / epoxy teal / flake tan
# New technique: top-down SVG garage plan filled with seeded multi-colour flake speckle, crack lines and a drain pin,
# with the quote form computing square feet from the drawn size; flake swatches reuse the same speckle generator.
def flakes5(x, y, w, h, n, cols, seed, r=(1.4, 3.2)):
    R = random.Random(seed)
    return "".join(f'<circle cx="{x + R.random() * w:.1f}" cy="{y + R.random() * h:.1f}" r="{R.uniform(*r):.1f}" fill="{R.choice(cols)}"/>' for _ in range(n))
FC5 = [("Sample Granite", "#5d636b", ["#2b2f35", "#c9cdd2", "#8a9097", "#f2f2f0"]), ("Sample Sand", "#cbb69a", ["#7d6a52", "#f4ead9", "#a68f71", "#3e352a"]), ("Sample Storm", "#37506a", ["#1d2b3a", "#9fb3c7", "#e9eef2", "#5f7a94"])]
GW5, GD5 = 22, 24
def garage5():
    s = 12; W, H = GW5 * s, GD5 * s; ox, oy = 40, 26
    return f'''<svg viewBox="0 0 {W + 100} {H + 70}" width="{W + 100}" style="display:block;zoom:1.24"><rect x="{ox - 8}" y="{oy - 8}" width="{W + 16}" height="{H + 8}" fill="#2e3440"/>
<rect x="{ox}" y="{oy}" width="{W}" height="{H}" fill="#5d636b"/>{flakes5(ox, oy, W, H, 900, FC5[0][2], 5)}
<path d="M{ox + 40} {oy + 60} l30 18 l14 -6 l26 30 l10 24" stroke="#ff6b4a" stroke-width="3" fill="none" stroke-linecap="round"/><path d="M{ox + 180} {oy + 190} l-20 26 l6 18 l-16 24" stroke="#ff6b4a" stroke-width="3" fill="none" stroke-linecap="round"/>
<circle cx="{ox + W / 2}" cy="{oy + H / 2}" r="9" fill="#2e3440" stroke="#d8c3a5" stroke-width="3"/>
<rect x="{ox + 20}" y="{oy + H}" width="{W - 40}" height="10" fill="#d8c3a5"/>
<text x="{ox + W / 2}" y="{oy + H + 34}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="15" fill="#2e3440">Garage door · {GW5} ft</text>
<text x="{ox + W + 12}" y="{oy + H / 2 + 5}" font-family="Inter" font-weight="700" font-size="15" fill="#2e3440">{GD5} ft</text>
<rect x="{ox + 54}" y="{oy + 34}" width="64" height="22" rx="6" fill="#fff"/><text x="{ox + 86}" y="{oy + 50}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="13" fill="#c2412a">Crack 1</text>
<rect x="{ox + 176}" y="{oy + 250}" width="64" height="22" rx="6" fill="#fff"/><text x="{ox + 208}" y="{oy + 266}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="13" fill="#c2412a">Crack 2</text>
<rect x="{ox + W / 2 + 14}" y="{oy + H / 2 - 11}" width="50" height="22" rx="6" fill="#fff"/><text x="{ox + W / 2 + 39}" y="{oy + H / 2 + 5}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="13" fill="#2e3440">Drain</text></svg>'''
def sw5(c, cols, i):
    return f'<svg viewBox="0 0 90 56" width="90" height="56" style="display:block;border-radius:10px"><rect width="90" height="56" fill="{c}"/>{flakes5(0, 0, 90, 56, 70, cols, 40 + i, (1, 2.4))}</svg>'
TL5 = [("Day 1 · AM", "Grind floor, fill cracks"), ("Day 1 · PM", "Base coat and flakes"), ("Day 2", "Scrape, top coat"), ("After", "We text you when to park")]
P["p395_epoxy"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#eef0f2;color:#2e3440}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#1f8a8a;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#1f8a8a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm5{font:800 13px/1.4 Inter;letter-spacing:2px;color:#6b7480}
.tp5{flex:1;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);gap:14px;min-height:0}
.pl5{background:#fff;border-radius:26px;padding:18px 20px;display:flex;flex-direction:column;gap:10px;align-items:center;box-shadow:0 14px 30px rgba(46,52,64,.08)}.pl5 .sm5{align-self:flex-start}
.fm5{background:#fff;border-radius:26px;padding:18px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(46,52,64,.08)}
.fm5 .fd{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1px solid #e7eaee}
.fm5 small{font:500 14px/1.3 Inter;color:#6b7480}.fm5 b{font:600 19px/1.3 Inter}.fm5 b em{font-style:normal;color:#1f8a8a}
.fc5{display:flex;gap:10px;margin-top:4px}.fc5>div{display:flex;flex-direction:column;gap:4px;align-items:center;padding:4px;border-radius:14px}.fc5>div.on{box-shadow:0 0 0 3px #1f8a8a}.fc5 span{font:600 13px/1.2 Inter;color:#4a525e}
.tl5{background:#2e3440;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}.tl5 .sm5{color:#b8c2cc}
.tl5 .rw{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.tl5 .st{background:rgba(255,255,255,.07);border-radius:16px;padding:12px 14px;border-top:5px solid #1f8a8a;display:flex;flex-direction:column;gap:4px}.tl5 .st:last-child{border-top-color:#d8c3a5}
.tl5 .st b{font:700 18px/1.3 Montserrat}.tl5 .st span{font:500 16px/1.35 Inter;color:#d3dae1}
""", "<div class=kk>EPOXY GARAGE FLOORS · QUOTE REQUESTS</div><h1>Quoting a garage floor blind?<br><span>Get size and photos first.</span></h1>",
f'''<div class=vw><div class=tp5><div class=pl5><span class=sm5>THEIR GARAGE · FROM THE FORM · SAMPLE</span>{garage5()}</div>
<div class=fm5><span class=sm5>QUOTE REQUEST · Q-208</span>{"".join(f'<div class=fd><small>{a}</small><b>{b}</b></div>' for a, b in [("ZIP code", "00012 · in service area"), ("Garage size", f"{GW5} × {GD5} ft · <em>{GW5 * GD5} sq ft</em>"), ("Floor now", "Old paint, peeling in spots"), ("Cracks", "2 marked on the drawing"), ("Photos", "3 added"), ("Best week", "Week of Dec 7")])}
<div class=fd><small>Flake color</small><div class=fc5>{"".join(f'<div class="{"on" if i == 0 else ""}">{sw5(c, cols, i)}<span>{n}</span></div>' for i, (n, c, cols) in enumerate(FC5))}</div></div></div></div>
<div class=tl5><span class=sm5>YOUR INSTALL PLAN · SENT WITH THE QUOTE · DRY TIMES DEPEND ON THE PRODUCT</span><div class=rw>{"".join(f'<div class=st><b>{a}</b><span>{b}</span></div>' for a, b in TL5)}</div></div></div>''',
"#2e3440", "Install epoxy floors? DM us", "background:#1f8a8a;color:#fff")


# ───────── 392 INDIA · Self-study library (paid reading room) · CAROUSEL 5 · Lora + DM Sans · study green / lamp amber / paper
# New technique: shift-split seat map (each seat's top half = morning, bottom half = evening) generated from one seat list;
# the join form, fee list and waitlist all pick seats from the same list so every number agrees across slides.
R2 = random.Random(392)
ids2 = list(range(1, 41)); R2.shuffle(ids2)
SEAT2 = {s: ("F" if k < 14 else ("M" if k < 21 else "ME")) for k, s in enumerate(ids2)}
FREE_E2 = sorted(s for s, t in SEAT2.items() if t == "M")
NEW2 = FREE_E2[0]
ME2 = sorted(s for s, t in SEAT2.items() if t == "ME")
LEAVE2 = ME2[2]
CNT2 = {"F": sum(1 for t in SEAT2.values() if t == "F"), "M": len(FREE_E2), "ME": len(ME2)}
MEM2 = CNT2["F"] + CNT2["M"] + 2 * CNT2["ME"]
def seatmap2(hi=None, sz=92):
    def one(s):
        t = SEAT2[s]; h = "hi" if hi and s in hi else ""
        top = "f" if t == "F" else "m"; bot = "f" if t == "F" else ("e" if t == "ME" else "o")
        return f'<div class="se2 {h}" style="width:{sz}px;height:{sz * .82:.0f}px"><i class="{top}"></i><i class="{bot}"></i><b><u>{s}</u></b></div>'
    rows = "".join(f'<div class=rw2>{"".join(one(r * 8 + c + 1) for c in range(4))}<span class=ai2></span>{"".join(one(r * 8 + c + 1) for c in range(4, 8))}</div>' for r in range(5))
    return f'<div class=mp2>{rows}</div>'
LEG2 = '<div class=lg2>' + "".join(f'<span><i class="{c}"></i>{t}</span>' for c, t in [("f", "Full day"), ("m", "Morning 6 AM-2 PM"), ("e", "Evening 2-10 PM"), ("o", "Free")]) + '</div>'
B2 = """
body{--f:'DM Sans';--h:'Lora';background:#f7f3ea;color:#1c2b26;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b7791f;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:58px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#1f4a3d;font-style:italic}
.cd2{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(28,43,38,.08)}
.sm2{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#6e7a73}
.mp2{display:flex;flex-direction:column;gap:10px;align-items:center}.rw2{display:flex;gap:8px}.ai2{width:30px}
.se2{border-radius:10px 10px 6px 6px;position:relative;display:flex;flex-direction:column;overflow:hidden;border:2px solid #cfd8d2;background:#fff}
.se2 i{flex:1;display:block}.se2 i.f{background:#1f4a3d}.se2 i.m{background:#f2b33d}.se2 i.e{background:#3d5a8a}.se2 i.o{background:repeating-linear-gradient(45deg,#fff 0 5px,#eef2ef 5px 10px)}
.se2 b{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:700 18px/1 'DM Sans';color:#fff}.se2 u{text-decoration:none;background:rgba(20,34,29,.78);border-radius:7px;padding:4px 6px}
.se2.hi{box-shadow:0 0 0 4px #e0532f;border-color:#e0532f}
.lg2{display:flex;gap:14px;flex-wrap:wrap}.lg2 span{display:flex;gap:6px;align-items:center;font:600 15px/1.2 'DM Sans';color:#44524c}.lg2 i{width:18px;height:18px;border-radius:4px;border:2px solid #cfd8d2}
.lg2 i.f{background:#1f4a3d}.lg2 i.m{background:#f2b33d}.lg2 i.e{background:#3d5a8a}.lg2 i.o{background:repeating-linear-gradient(45deg,#fff 0 4px,#eef2ef 4px 8px)}
.bb2{background:#1f4a3d;color:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}.bb2 b{font:700 19px/1.3 'DM Sans'}.bb2 span{font:500 16px/1.35 'DM Sans';color:#c9dbd3}
"""
def t2(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f4a3d;color:#fff"):
    return page(B2 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1c2b26", cta, ctacss, tagline=f"{n} / 5")
P["p392_library_s1"] = t2(1, "SELF-STUDY LIBRARY · SEATS AND SHIFTS", "Seats tracked in a register?<br><span>See every seat, every shift.</span>",
f'''<div class=w21><div class="cd2 sc21"><div class=h><span class=sm2>YOUR HALL TODAY · 40 SEATS · {MEM2} MEMBERS · SAMPLE</span></div>{seatmap2()}{LEG2}
<div class=ct21>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [(f"{CNT2['F']}", "full-day seats"), ("0", "morning seats free"), (f"{CNT2['M']}", "evening seats free")])}</div></div>
<div class=pn21>{"".join(f'<div class=bb2><b>{a}</b><span>{b}</span></div>' for a, b in [("“Is any evening seat free?”", "Owner checks 3 pages"), ("“Who has not paid?”", "Ticks in a notebook"), ("“Morning seat for my friend?”", "Name on a loose slip")])}</div></div>''',
css=""".w21{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sc21{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:14px;justify-content:space-between;align-items:center}.sc21 .h{align-self:flex-start}
.ct21{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;width:100%}.ct21>div{background:#f4efe3;border-radius:16px;padding:10px 14px;display:flex;gap:10px;align-items:center}.ct21 b{font:700 34px/1.3 Lora;color:#1f4a3d}.ct21 span{font:600 16px/1.3 'DM Sans';color:#44524c}
.pn21{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}""")
P["p392_library_s2"] = t2(2, "1 · NEW MEMBER IN TWO MINUTES", "Evening seat free?<br><span>Book it while they wait.</span>",
f'''<div class=w22><div class=lf22><div class="cd2 mc22"><div class=eq22><span class=sm2>WALK-IN · 6:40 PM</span><p>“Any seat free in the evening shift?”</p></div><div class=mw22><span class=sm2>FREE EVENING SEATS · {CNT2["M"]}</span>{seatmap2(hi=FREE_E2, sz=58)}<div class=fr22>{"".join(f'<i class="{"on" if s == NEW2 else ""}">Seat {s}</i>' for s in FREE_E2)}</div></div></div>
<div class="cd2 wm22"><span class=sm2>WELCOME MESSAGE · SENT ON SAVE</span><p>Welcome! Seat {NEW2}, evening shift 2-10 PM, locker L-12. Starts Tue 24 Nov, renews Thu 24 Dec. Please keep the hall quiet.</p></div></div>
{phone(f"""<div class=ph22><span class=sm2>JOIN FORM · SAMPLE</span>{"".join(f'<div class=fd><small>{a}</small><b>{b}</b></div>' for a, b in [("Name", "Sample Member"), ("Phone", "98XXX XXXXX"), ("Shift", "Evening, 2-10 PM"), ("Seat", f"Seat {NEW2}"), ("Locker", "L-12"), ("Starts", "Tue 24 Nov"), ("Renews", "Thu 24 Dec")])}<div class=ok>{ic("check", 20, "#1f4a3d", 3)} ID photo checked</div><div class=bt>Confirm seat</div></div>""", w=360, h=760)}</div>''',
css=""".w22{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 360px;gap:20px;align-items:center;min-height:0}.lf22{height:100%;display:flex;flex-direction:column;gap:14px}
.mc22{flex:1;padding:16px 18px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}.mc22{justify-content:space-between}.mw22{flex:1;display:flex;flex-direction:column;gap:14px;justify-content:center}.eq22{background:#f4efe3;border-radius:16px 16px 16px 4px;padding:14px 16px;display:flex;flex-direction:column;gap:4px}.eq22 p{font:600 21px/1.4 'DM Sans'}.mc22 .se2 b{font-size:15px}.mc22 .rw2{gap:6px}.mc22 .ai2{width:14px}
.fr22{display:flex;flex-wrap:wrap;gap:6px}.fr22 i{font:700 15px/1.2 'DM Sans';font-style:normal;border-radius:10px;padding:7px 10px;background:#e7edf5;color:#3d5a8a}.fr22 i.on{background:#e0532f;color:#fff}
.wm22{padding:16px 18px;display:flex;flex-direction:column;gap:8px;background:#e9f1ec}.wm22 p{font:500 18px/1.45 'DM Sans';text-wrap:pretty}
.ph22{flex:1;padding:8px 20px 20px;display:flex;flex-direction:column;gap:4px}.ph22 .fd{flex:1;display:flex;flex-direction:column;justify-content:center;border-bottom:1px solid #e6ebe8}
.ph22 small{font:500 13px/1.3 'DM Sans';color:#6e7a73}.ph22 b{font:700 18px/1.3 'DM Sans'}.ph22 .ok{display:flex;gap:8px;align-items:center;font:700 15px/1.3 'DM Sans';color:#1f4a3d;padding:10px 0}
.ph22 .bt{background:#1f4a3d;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 18px/1.2 'DM Sans'}""")
FE2 = [(ME2[0], "Morning", "Mon 23 Nov", "paid"), (ids2[1], "Full day", "Mon 23 Nov", "today"), (FREE_E2[2], "Morning", "Tue 24 Nov", "soon"), (ME2[4], "Evening", "Wed 25 Nov", "soon"), (ids2[3], "Full day", "Sat 21 Nov", "late"), (ME2[6], "Evening", "Fri 27 Nov", "soon")]
WK2 = [("Mon", 23), ("Tue", 24), ("Wed", 25), ("Thu", 26), ("Fri", 27), ("Sat", 28), ("Sun", 29)]
DUE2 = {23: 3, 24: 2, 25: 4, 26: 1, 27: 3, 28: 2, 29: 0}
def fst2(st, d):
    return {"paid": ("Paid by UPI today", "pd"), "today": ("Due today", "td"), "soon": (f"Due {d[:3]}", "sn"), "late": (f"2 days late", "lt")}[st]
P["p392_library_s3"] = t2(3, "2 · RENEWALS WITHOUT CHASING", "Who has not paid this month?<br><span>The app reminds them.</span>",
f'''<div class=w23><div class="cd2 wk23"><span class=sm2>RENEWALS DUE THIS WEEK · SAMPLE</span><div class=dd>{"".join(f'<div class="{"tdy" if n == 23 else ""}"><span>{d}</span><b>{n}</b><div class=br><i style="height:{DUE2[n] / 4 * 100:.0f}%"></i></div><em>{DUE2[n]}</em></div>' for d, n in WK2)}</div></div>
<div class=bt23><div class="cd2 ls23"><span class=sm2>MEMBERS · NO AMOUNTS SHOWN</span>{"".join(f'<div class=r><b>Seat {s}</b><span>{sh} · renews {d}</span><em class={fst2(st, d)[1]}>{fst2(st, d)[0]}</em></div>' for s, sh, d, st in FE2)}</div>
<div class=rc23><div class="cd2 rm23"><span class=sm2>AUTO REMINDER · 1 DAY BEFORE</span><p>Hi, your seat {FE2[2][0]} (morning) renews tomorrow, Tue 24 Nov. Pay at the desk or by UPI to keep your seat.</p></div>
<div class="cd2 lt23"><span class=sm2>LATE · SEAT {FE2[4][0]}</span><p>Second reminder sent. Owner sees it at the top of the list.</p></div></div></div></div>''',
css=""".w23{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.wk23{padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.dd{display:grid;grid-template-columns:repeat(7,1fr);gap:10px}.dd>div{display:flex;flex-direction:column;align-items:center;gap:4px;background:#f6f2e8;border-radius:16px;padding:10px 6px}.dd>div.tdy{background:#1f4a3d;color:#fff}
.dd span{font:600 14px/1.3 'DM Sans';color:#6e7a73}.dd .tdy span{color:#c9dbd3}.dd b{font:700 26px/1.3 Lora}.dd em{font:700 15px/1.2 'DM Sans';font-style:normal}
.dd .br{width:28px;height:70px;border-radius:8px;background:rgba(31,74,61,.12);display:flex;align-items:flex-end;overflow:hidden}.dd .br i{display:block;width:100%;background:#f2b33d}
.bt23{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ls23{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:4px}.ls23 .r{flex:1;display:grid;grid-template-columns:110px 1fr auto;gap:10px;align-items:center;border-top:1px solid #eef0ec}
.ls23 b{font:700 22px/1.3 'DM Sans'}.ls23 span{font:500 17px/1.35 'DM Sans';color:#5d6a64}.ls23 em{font:700 15px/1.2 'DM Sans';font-style:normal;border-radius:10px;padding:8px 10px}
em.pd{background:#e2efe7;color:#1f4a3d}em.td{background:#fdf0d3;color:#8a5a0b}em.sn{background:#edf0f6;color:#3d5a8a}em.lt{background:#fbe2da;color:#a8371b}
.rc23{display:grid;grid-template-columns:1.5fr 1fr;gap:14px}.rm23{padding:16px 18px;display:flex;flex-direction:column;gap:10px;justify-content:center;background:#e9f1ec}.rm23 p{font:500 19px/1.45 'DM Sans';text-wrap:pretty}
.lt23{padding:16px 18px;display:flex;flex-direction:column;gap:8px;background:#fbe9e2}.lt23 p{font:500 17px/1.45 'DM Sans'}""")
WL2 = [("W-1", "Sample Member A", "Morning", "since Wed 18 Nov"), ("W-2", "Sample Member B", "Morning", "since Fri 20 Nov"), ("W-3", "Sample Member C", "Full day", "since Sun 22 Nov")]
EN2 = [(ids2[5], "Full day", "Renewed"), (ME2[1], "Morning", "Renewed"), (LEAVE2, "Morning", "Not renewing"), (ME2[3], "Morning", "No reply yet")]
P["p392_library_s4"] = t2(4, "3 · WAITLIST FOR FULL SHIFTS", "Morning seats all taken?<br><span>Keep a waitlist, not slips.</span>",
f'''<div class=w24><div class=tp24><div class="cd2 wl24"><span class=sm2>WAITLIST · SAMPLE</span>{"".join(f'<div class=r><b>{a}</b><div><strong>{b}</strong><span>{c} · {d}</span></div></div>' for a, b, c, d in WL2)}</div>
<div class="cd2 en24"><span class=sm2>MORNING SEATS ENDING 30 NOV</span>{"".join(f'<div class=r><b>Seat {s}</b><span>{sh}</span><em class="{"lt" if st == "Not renewing" else ("td" if "reply" in st else "pd")}">{st}</em></div>' for s, sh, st in EN2)}</div></div>
<div class=fl24>{"".join(f'<div class=st><span>{a}</span><b>{b}</b></div>' + ('<i>' + ic("arrow", 30, "#b7791f", 2.5) + '</i>' if k < 2 else '') for k, (a, b) in enumerate([("Not renewing", f"Seat {LEAVE2} morning"), ("Free from", "Tue 1 Dec"), ("Offered to", "W-1 first")]))}</div>
<div class="cd2 of24"><span class=sm2>AUTO OFFER TO W-1</span><p>Good news! Seat {LEAVE2}, morning shift, is free from Tue 1 Dec. Reply YES by Wed 6 PM to book it. If not, it goes to the next person.</p></div></div>''',
css=""".w24{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tp24{flex:1;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px;min-height:0}
.wl24,.en24{padding:16px 20px;display:flex;flex-direction:column;gap:4px}.wl24 .r,.en24 .r{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #eef0ec}
.wl24 .r>b{width:58px;height:58px;border-radius:16px;background:#f2b33d;color:#1c2b26;font:700 19px/1 'DM Sans';display:flex;align-items:center;justify-content:center;flex:none}.wl24 strong{display:block;font:700 22px/1.3 'DM Sans'}.wl24 span{font:500 17px/1.35 'DM Sans';color:#5d6a64}
.en24 .r{display:grid;grid-template-columns:90px 1fr auto}.en24 b{font:700 22px/1.3 'DM Sans'}.en24 span{font:500 18px/1.3 'DM Sans';color:#5d6a64}.en24 em{font:700 15px/1.2 'DM Sans';font-style:normal;border-radius:10px;padding:8px 10px}
em.pd{background:#e2efe7;color:#1f4a3d}em.td{background:#fdf0d3;color:#8a5a0b}em.lt{background:#fbe2da;color:#a8371b}
.fl24{display:flex;align-items:center;gap:10px}.fl24 .st{flex:1;background:#1f4a3d;color:#fff;border-radius:18px;padding:14px 16px;display:flex;flex-direction:column;gap:4px}.fl24 .st span{font:600 14px/1.3 'DM Sans';color:#c9dbd3}.fl24 .st b{font:700 21px/1.3 'DM Sans'}.fl24 i{display:flex}
.of24{padding:16px 20px;display:flex;flex-direction:column;gap:8px;background:#fdf3dc}.of24 p{font:500 19px/1.45 'DM Sans';text-wrap:pretty}""")
P["p392_library_s5"] = t2(5, "SELF-STUDY LIBRARY APP", "Run a study library?<br><span>Let's build your seat app.</span>",
f'''<div class=w25><div class=tl25>{"".join(f'<div class=cd2><span class=ib>{ic(i, 40)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("grid", "Seat map", "Morning and evening, live"), ("doc", "Join form", "Seat, locker, ID check"), ("bell", "Renewal reminders", "Sent a day before"), ("users", "Waitlist", "Free seats offered in order")])}</div>
<div class=q25><span class=sm2>A QUESTION FOR LIBRARY OWNERS</span><p>How do you track seats today: a register, a sheet or chat groups? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss="background:#f2b33d;color:#1c2b26",
css=""".w25{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}.tl25{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}
.tl25>div{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}.tl25 .ib{width:84px;height:84px;border-radius:22px;background:#1f4a3d;color:#f2b33d}.tl25 b{font:700 40px/1.3 Lora}.tl25 span{font:500 24px/1.4 'DM Sans';color:#5d6a64}
.q25{background:#1f4a3d;color:#fff;border-radius:26px;padding:28px 30px;display:flex;flex-direction:column;gap:12px}.q25 .sm2{color:#f2b33d}.q25 p{font:500 32px/1.4 Lora;text-wrap:pretty}""")


# ───────── 394 INDIA · Corrugated box maker · CAROUSEL 5 · Archivo Black + Source Sans 3 · corrugated tan / flexo blue / die-line red
# New techniques: SVG RSC dieline (cut lines red, creases dashed blue, slots) drawn from the box L/W/H; flute cross-section
# waves (3 ply vs 5 ply); sheet size and reel deckle "ups" computed in Python; a conveyor line with order cartons at stations.
BL4, BW4, BH4, GF4 = 300, 200, 150, 35
SL4 = 2 * (BL4 + BW4) + GF4; SWD4 = BH4 + BW4
DK4 = 1100; UPS4 = DK4 // SWD4; TRIM4 = DK4 - UPS4 * SWD4
QTY4 = 2000; CUTS4 = -(-QTY4 // UPS4)
def die4(sc=0.78, lab=True):
    f = BW4 / 2; x0 = 20; y0 = 20; s = sc
    xs = [x0 + GF4 * s]
    for p in [BL4, BW4, BL4, BW4]: xs.append(xs[-1] + p * s)
    yT, yB = y0 + f * s, y0 + (f + BH4) * s; yE = y0 + (2 * f + BH4) * s
    W = xs[-1] + 20; H = yE + 20
    g = 4
    cut = f'M{x0} {yT + 8} L{xs[0]} {yT} '
    path = [f"M{xs[0]} {yT}"]
    for i in range(4):
        a, b = xs[i], xs[i + 1]
        path.append(f"L{a + (g if i else 0)} {yT} L{a + (g if i else 0)} {y0} L{b - (g if i < 3 else 0)} {y0} L{b - (g if i < 3 else 0)} {yT}")
    path.append(f"L{xs[4]} {yB}")
    for i in range(3, -1, -1):
        a, b = xs[i], xs[i + 1]
        path.append(f"L{b - (g if i < 3 else 0)} {yB} L{b - (g if i < 3 else 0)} {yE} L{a + (g if i else 0)} {yE} L{a + (g if i else 0)} {yB}")
    path.append(f"L{xs[0]} {yB} L{x0} {yB - 8} L{x0} {yT + 8} Z")
    crease = "".join(f'<line x1="{x}" y1="{yT}" x2="{x}" y2="{yB}" stroke="#1f5fa8" stroke-width="2" stroke-dasharray="7 5"/>' for x in xs[:-1]) + \
             "".join(f'<line x1="{xs[0]}" y1="{y}" x2="{xs[4]}" y2="{y}" stroke="#1f5fa8" stroke-width="2" stroke-dasharray="7 5"/>' for y in (yT, yB))
    labs = ""
    if lab:
        for i, (p, n) in enumerate([(BL4, "Length"), (BW4, "Width"), (BL4, "Length"), (BW4, "Width")]):
            cx = (xs[i] + xs[i + 1]) / 2
            labs += f'<text x="{cx:.0f}" y="{(yT + yB) / 2 - 4:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="20" fill="#1e1c19">{p}</text><text x="{cx:.0f}" y="{(yT + yB) / 2 + 18:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="600" font-size="14" fill="#6b5a40">{n}</text>'
            labs += f'<text x="{cx:.0f}" y="{(y0 + yT) / 2 + 5:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="600" font-size="14" fill="#6b5a40">flap {BW4 // 2}</text>'
        labs += f'<text x="{(x0 + xs[0]) / 2 + 2:.0f}" y="{(yT + yB) / 2 + 5:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="12" fill="#6b5a40">glue</text>'
    return f'''<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" style="display:block;max-width:100%;height:auto"><path d="{" ".join(path)}" fill="#d9b47e" stroke="#d6362f" stroke-width="3" stroke-linejoin="round"/>
<path d="{" ".join(path)}" fill="url(#fl4)" opacity=".35"/><defs><pattern id="fl4" width="10" height="10" patternUnits="userSpaceOnUse"><rect width="10" height="10" fill="none"/><line x1="0" y1="0" x2="0" y2="10" stroke="#b58c55" stroke-width="2"/></pattern></defs>{crease}{labs}</svg>'''
def flute4(ply):
    w, h = 300, 90 if ply == 5 else 60
    def wave(y, amp): return "M0 " + f"{y}" + "".join(f" Q{x + 7.5} {y - amp} {x + 15} {y} T{x + 30} {y}" for x in range(0, w, 30))
    if ply == 3:
        body = f'<rect x="0" y="6" width="{w}" height="6" fill="#8a6a3d"/><path d="{wave(30, 18)}" stroke="#b58c55" stroke-width="3" fill="none"/><rect x="0" y="48" width="{w}" height="6" fill="#8a6a3d"/>'
    else:
        body = f'<rect x="0" y="6" width="{w}" height="6" fill="#8a6a3d"/><path d="{wave(26, 14)}" stroke="#b58c55" stroke-width="3" fill="none"/><rect x="0" y="40" width="{w}" height="6" fill="#8a6a3d"/><path d="{wave(60, 14)}" stroke="#b58c55" stroke-width="3" fill="none"/><rect x="0" y="74" width="{w}" height="6" fill="#8a6a3d"/>'
    return f'<svg viewBox="0 -6 {w} {h + 4}" width="{w}" style="display:block;max-width:100%;height:auto">{body}</svg>'
B4 = """
body{--f:'Source Sans 3';--h:'Archivo Black';background:#f3ead9;color:#1e1c19}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#d6362f;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.24;letter-spacing:-.5px;margin-top:16px} h1 span{color:#1f5fa8}
.cd4{background:#fffaf1;border-radius:22px;box-shadow:0 14px 30px rgba(30,28,25,.09)}
.sm4{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7a6a50}
.lg4{display:flex;gap:18px;flex-wrap:wrap}.lg4 span{display:flex;gap:8px;align-items:center;font:600 16px/1.2 'Source Sans 3';color:#4a4033}.lg4 i{width:30px;height:0;border-top:3px solid #d6362f}.lg4 i.cr{border-top:3px dashed #1f5fa8}
.bb4{background:#1e1c19;color:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}.bb4 b{font:700 20px/1.3 'Source Sans 3'}.bb4 span{font:500 16px/1.35 'Source Sans 3';color:#cbbfa8}
"""
def t4(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1e1c19;color:#f3c98b"):
    return page(B4 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1e1c19", cta, ctacss, tagline=f"{n} / 5")
LEG4 = '<div class=lg4><span><i></i>Cut</span><span><i class=cr></i>Fold</span></div>'
P["p394_box_s1"] = t4(1, "CORRUGATED BOX MAKER · REPEAT ORDERS", "“Same box as last time.”<br><span>Which size was that?</span>",
f'''<div class=w41><div class="cd4 dl41"><div class=h><span class=sm4>B-104 · FLAT BOX LAYOUT · MM · SAMPLE</span>{LEG4}</div>{die4(0.84)}<div class=dy41><span>Old diary, last March:</span><em>B-104 → 30 × 20 × 15 cm? 3 ply or 5 ply?? print blue (ask)</em></div><div class=ch41>{''.join(f'<span>{a} <b>?</b></span>' for a in ['Ply', 'Print colour', 'Joint', 'Last qty'])}</div><div class=sz>Inside size <b>{BL4} × {BW4} × {BH4} mm</b> · sheet <b>{SL4:,} × {SWD4} mm</b></div></div>
<div class=pn41>{"".join(f'<div class=bb4><b>{a}</b><span>{b}</span></div>' for a, b in [("“Same as last time”", "Size is in an old diary"), ("“3 ply or 5 ply?”", "Nobody remembers"), ("“Print in blue, right?”", "Proof lost in chat")])}</div></div>''',
css=""".w41{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.dl41{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px;justify-content:space-between;align-items:center}
.dl41 .h{width:100%;display:flex;justify-content:space-between;align-items:center;gap:10px}.dl41 .sz{font:500 20px/1.4 'Source Sans 3';color:#4a4033}.dl41 .sz b{font-weight:700;color:#1e1c19}
.dy41{width:100%;background:#fffdf6;border-radius:6px;padding:14px 20px;background-image:repeating-linear-gradient(#fffdf6 0 33px,#c9d8ea 33px 34px);box-shadow:inset 4px 0 0 #e7a3a0;display:flex;flex-direction:column;gap:2px;line-height:34px}.dy41 span{font:600 15px/34px 'Source Sans 3';color:#7a6a50}.dy41 em{font:italic 600 24px/34px 'Crimson Text';color:#2b3f73}
.ch41{display:flex;gap:10px}.ch41 span{font:600 17px/1.2 'Source Sans 3';background:#f3ead9;border-radius:12px;padding:10px 14px;color:#4a4033}.ch41 b{color:#d6362f;font-weight:800}
.pn41{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.pn41 .bb4 b{font-size:22px}.pn41 .bb4 span{font-size:18px}""")
SP4 = [("Customer", "Sample Snacks Unit"), ("Inside size", f"{BL4} × {BW4} × {BH4} mm"), ("Style", "Regular slotted box"), ("Board", "5 ply"), ("Print", "1 colour, 2 sides"), ("Joint", "Stitched"), ("Usual qty", f"{QTY4:,} boxes"), ("Last order", "Tue 3 Nov")]
P["p394_box_s2"] = t4(2, "1 · ONE SPEC CARD PER BOX", "Save the size, ply and print<br><span>once. Repeat in one tap.</span>",
f'''<div class=w42><div class="cd4 sp42"><div class=hd><b>B-104</b><span>SPEC CARD</span></div>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in SP4)}<div class=bt>Repeat B-104 · enter qty</div></div>
<div class=rt42><div class="cd4 fl42"><span class=sm4>BOARD · SIDE VIEW</span><div class=fw>{"".join(f'<div class="fx {"on" if p == 5 else ""}"><div class=t><b>{p} ply</b><span>{d}</span></div>{flute4(p)}</div>' for p, d in [(3, "Light items"), (5, "Heavier items, B-104")])}</div></div>
<div class="cd4 pr42"><span class=sm4>PRINT PROOF · APPROVED</span><div class=pf><div class=bx><span>YOUR BRAND</span><small>Sample print area</small></div><div class=ok>{ic("check", 22, "#fff", 3)}<span>Approved by customer<br>Wed 28 Oct</span></div></div></div></div></div>''',
css=""".w42{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}
.sp42{padding:20px 22px;display:flex;flex-direction:column;gap:4px;border-top:10px solid #c9a06a}.sp42 .hd{display:flex;justify-content:space-between;align-items:center;padding-bottom:8px}.sp42 .hd b{font:400 34px/1.35 'Archivo Black'}.sp42 .hd span{font:700 15px/1.3 'Source Sans 3';letter-spacing:2px;color:#d6362f}
.sp42 .r{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px dashed #e2d3b8}.sp42 .r span{font:500 17px/1.3 'Source Sans 3';color:#7a6a50}.sp42 .r b{font:700 19px/1.3 'Source Sans 3';text-align:right}
.sp42 .bt{margin-top:8px;background:#1f5fa8;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 19px/1.2 'Source Sans 3'}
.rt42{display:flex;flex-direction:column;gap:16px}.fl42{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:12px}.fl42 .fw{flex:1;display:flex;flex-direction:column;gap:16px;justify-content:center}
.fx{border-radius:16px;padding:12px 14px;background:#f3ead9;display:flex;flex-direction:column;gap:8px}.fx.on{box-shadow:0 0 0 3px #1f5fa8}.fx .t{display:flex;justify-content:space-between;align-items:center}.fx b{font:400 22px/1.35 'Archivo Black'}.fx span{font:600 16px/1.3 'Source Sans 3';color:#6b5a40}
.pr42{padding:18px 20px;display:flex;flex-direction:column;gap:12px}.pf{display:flex;gap:14px;align-items:center}.pf .bx{flex:1;height:110px;border-radius:8px;background:#d9b47e;border:3px dashed #1f5fa8;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.pf .bx span{font:400 22px/1.35 'Archivo Black';color:#1f5fa8}.pf .bx small{font:600 14px/1.3 'Source Sans 3';color:#4a4033}.pf .ok{display:flex;gap:10px;align-items:center;background:#2f8a57;color:#fff;border-radius:14px;padding:12px 14px}.pf .ok span{font:700 16px/1.35 'Source Sans 3'}""")
def deckle4():
    s = 0.27; L = SL4 * s; Wd = SWD4 * s; x0, y0 = 20, 20
    sh = ""
    for c in range(2):
        for k in range(UPS4):
            x = x0 + c * L; y = y0 + k * Wd
            sh += f'<rect x="{x:.1f}" y="{y:.1f}" width="{L:.1f}" height="{Wd:.1f}" fill="#d9b47e" stroke="#d6362f" stroke-width="2"/><text x="{x + L / 2:.0f}" y="{y + Wd / 2 + 6:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="17" fill="#1e1c19">{SL4:,} × {SWD4}</text>'
    ty = y0 + UPS4 * Wd
    tr = f'<rect x="{x0}" y="{ty:.1f}" width="{2 * L:.1f}" height="{TRIM4 * s:.1f}" fill="#bfae92"/>'
    W = x0 + 2 * L + 150; H = y0 + DK4 * s + 40
    return f'''<svg viewBox="0 0 {W:.0f} {H:.0f}" width="{W:.0f}" style="display:block;width:100%;height:auto">{sh}{tr}
<text x="{x0 + 2 * L + 16:.0f}" y="{ty + 8:.0f}" font-family="Source Sans 3" font-weight="700" font-size="16" fill="#6b5a40">trim {TRIM4} mm</text>
<text x="{x0 + 2 * L + 16:.0f}" y="{y0 + 40:.0f}" font-family="Source Sans 3" font-weight="700" font-size="16" fill="#1f5fa8">Reel width</text><text x="{x0 + 2 * L + 16:.0f}" y="{y0 + 62:.0f}" font-family="Source Sans 3" font-weight="700" font-size="16" fill="#1f5fa8">{DK4:,} mm</text></svg>'''
P["p394_box_s3"] = t4(3, "2 · SHEET SIZE FROM THE BOX SIZE", "No more sums on paper.<br><span>Sheet and cuts worked out.</span>",
f'''<div class=w43><div class=fm43>{"".join(f'<div class=cd4><span class=sm4>{a}</span><div class=eq>{b}</div><b>{c}</b></div>' for a, b, c in [("SHEET LENGTH", f"2 × ({BL4} + {BW4}) + {GF4} glue flap", f"{SL4:,} mm"), ("SHEET WIDTH", f"{BH4} height + 2 flaps of {BW4 // 2}", f"{SWD4} mm")])}</div>
<div class="cd4 dk43"><span class=sm4>ON A {DK4:,} MM REEL · {UPS4} SHEETS ACROSS · SAMPLE</span>{deckle4()}<div class=rn43>Board runs this way, cut every {SL4:,} mm →</div></div>
<div class=nb43>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [(f"{QTY4:,}", "boxes ordered"), (f"{UPS4} ups", "sheets per cut"), (f"{CUTS4:,}", "cuts on the machine")])}</div><div class=nt43>Sizes before trim allowance. Your own allowances can be set in the app.</div></div>''',
css=""".w43{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.fm43{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.fm43>div{padding:16px 20px;display:flex;flex-direction:column;gap:6px}.fm43 .eq{font:500 18px/1.4 'Source Sans 3';color:#4a4033}.fm43 b{font:400 36px/1.35 'Archivo Black';color:#1f5fa8}
.dk43{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:10px;justify-content:center}
.nb43{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.nb43>div{background:#1e1c19;color:#fff;border-radius:18px;padding:14px 18px;display:flex;flex-direction:column;gap:2px}.nb43 b{font:400 30px/1.4 'Archivo Black';color:#f3c98b}.nb43 span{font:600 16px/1.3 'Source Sans 3';color:#cbbfa8}
.rn43{font:600 18px/1.4 'Source Sans 3';color:#6b5a40}.nt43{font:500 16px/1.4 'Source Sans 3';color:#6b5a40}""")
ST4 = ["Corrugation", "Printing", "Slotting", "Stitching", "Bundled", "Dispatch"]
OD4 = [("B-104", "Sample Snacks Unit", 5), ("B-117", "Sample Shoe Maker", 3), ("B-121", "Sample Spice Packer", 1), ("B-109", "Sample Hardware Shop", 4), ("B-130", "Sample Sweet Shop", 0), ("B-112", "Sample Toy Seller", 2),
       ("B-126", "Sample Tile Dealer", 0), ("B-119", "Sample Pickle Maker", 1), ("B-115", "Sample Bulb Trader", 2), ("B-108", "Sample Tea Packer", 3), ("B-111", "Sample Bakery", 4), ("B-102", "Sample Spare Parts", 5)]
P["p394_box_s4"] = t4(4, "3 · EVERY ORDER ON THE LINE", "“Is my order ready?”<br><span>See its station, then dispatch.</span>",
f'''<div class=w44><div class="cd4 ln44"><span class=sm4>FACTORY LINE TODAY · SAMPLE</span><div class=bl>{"".join(f'<div class=sta><div class=nm>{k + 1}. {s}</div><div class=sl>{"".join(f"<div class=ob><b>{o}</b><span>{w}</span></div>" for o, w, st in OD4 if st == k)}</div></div>' for k, s in enumerate(ST4))}</div><div class=belt></div></div>
<div class=bt44><div class="cd4 sl44"><div class=hd><b>DISPATCH SLIP</b><span>B-104</span></div>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("To", "Sample Snacks Unit"), ("Boxes", f"{QTY4:,}"), ("Bundles", f"{QTY4 // 50} of 50"), ("Bill", "Attached to message"), ("Vehicle", "Sample tempo"), ("Leaves", "Today, 4 PM")])}</div>
<div class=rc44><div class="cd4 ms44"><span class=sm4>AUTO MESSAGE · 3:45 PM</span><p>B-104: {QTY4:,} boxes in {QTY4 // 50} bundles leave our factory at 4 PM today. The bill is attached.</p></div>
<div class="cd4 dl44"><span class=sm4>DISPATCH PLAN</span>{"".join(f'<div class=r><b>{o}</b><span>{w}</span><em class="{"td" if st == 5 else ""}">{"Today" if st == 5 else "Tomorrow"}</em></div>' for o, w, st in OD4 if st >= 4)}</div></div></div></div>''',
css=""".w44{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ln44{flex:none;padding:16px 18px;display:flex;flex-direction:column;gap:10px;position:relative;min-height:0}
.ln44 .bl{flex:1;display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:8px;min-height:0}.sta{display:flex;flex-direction:column;gap:8px;background:#f3ead9;border-radius:14px;padding:10px 8px}
.sta .nm{font:700 15px/1.3 'Source Sans 3';color:#1f5fa8;text-align:center;min-height:40px;display:flex;align-items:center;justify-content:center}
.sta .sl{flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:8px}
.ob{background:#d9b47e;border-radius:6px;padding:12px 8px;display:flex;flex-direction:column;gap:2px;text-align:center;box-shadow:inset 0 0 0 2px #b58c55,inset 0 14px 0 -6px #c79f68;background-image:linear-gradient(90deg,transparent 46%,#c4a06a 46% 54%,transparent 54%)}
.ob b{font:400 17px/1.4 'Archivo Black'}.ob span{font:600 13px/1.3 'Source Sans 3';color:#3b3226}
.ln44 .belt{height:18px;border-radius:9px;background:repeating-linear-gradient(90deg,#3b3631 0 18px,#57514a 18px 36px);flex:none}
.bt44{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px;min-height:0}.sl44{padding:16px 20px;display:flex;flex-direction:column;gap:6px;border-left:8px solid #d6362f}
.sl44 .hd{display:flex;justify-content:space-between}.sl44 .hd b{font:400 24px/1.4 'Archivo Black'}.sl44 .hd span{font:700 18px/1.3 'Source Sans 3';color:#d6362f}
.sl44 .r{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px dashed #e2d3b8}.sl44 .r span{font:500 19px/1.3 'Source Sans 3';color:#7a6a50}.sl44 .r b{font:700 21px/1.3 'Source Sans 3'}
.rc44{display:flex;flex-direction:column;gap:14px}.dl44{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:4px}.dl44 .r{flex:1;display:grid;grid-template-columns:80px 1fr auto;gap:10px;align-items:center;border-top:1px dashed #e2d3b8}.dl44 b{font:700 19px/1.3 'Source Sans 3'}.dl44 span{font:500 17px/1.3 'Source Sans 3';color:#6b5a40}.dl44 em{font:700 15px/1.2 'Source Sans 3';font-style:normal;border-radius:10px;padding:7px 10px;background:#f3ead9;color:#6b5a40}.dl44 em.td{background:#1f5fa8;color:#fff}
.ms44{padding:20px 22px;display:flex;flex-direction:column;gap:12px;justify-content:center;background:#e6eef8}.ms44 p{font:500 23px/1.45 'Source Sans 3';text-wrap:pretty}""")
P["p394_box_s5"] = t4(5, "CORRUGATED BOX ORDER APP", "Make corrugated boxes?<br><span>Let's build your order app.</span>",
f'''<div class=w45><div class="cd4 mn45">{die4(0.6, False)}</div><div class=tl45>{"".join(f'<div class=cd4><span class=ib>{ic(i, 28)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("doc", "Spec cards", "Size, ply, print, proof"), ("grid", "Sheet sizes", "Worked out for you"), ("truck", "Order line", "Every station, live"), ("send", "Dispatch messages", "Slip and bill sent")])}</div>
<div class=q45><span class=sm4>A QUESTION FOR BOX MAKERS</span><p>How do your regular buyers reorder today: a call, a chat or a visit? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss="background:#d6362f;color:#fff",
css=""".w45{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.mn45{padding:18px;display:flex;justify-content:center}
.tl45{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.tl45>div{padding:20px 22px;display:flex;gap:16px;align-items:center}.tl45 .ib{width:72px;height:72px;border-radius:16px;background:#1f5fa8;color:#fff}
.tl45 b{display:block;font:400 28px/1.4 'Archivo Black'}.tl45 span{font:500 21px/1.4 'Source Sans 3';color:#6b5a40}
.q45{background:#1e1c19;color:#fff;border-radius:24px;padding:24px 28px;display:flex;flex-direction:column;gap:10px}.q45 .sm4{color:#f3c98b}.q45 p{font:600 28px/1.4 'Source Sans 3';text-wrap:pretty}""")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
