
# ───────── 450 CANADA · Campground (site booking) · SINGLE · Lora + Source Sans 3 · birch white / forest teal / canoe red
# New technique: campground site map SVG (loop road, numbered pads by type and status, lake, washrooms, gate) where the
# free/booked counts and the booking form are computed from the same site list.
FT0 = "#24493d"; CR0 = "#c84b31"; LK0 = "#3d7ea6"; BG0 = "#f3efe6"; MU0 = "#66705f"
rnd0 = random.Random(450)
SITES0 = []
for i in range(24):
    typ = "Tent" if i in (0, 1, 2, 3, 20, 21, 22, 23) else ("RV 50A" if i in (8, 9, 10, 11) else "RV 30A")
    SITES0.append(dict(n=i + 1, t=typ, st="booked" if rnd0.random() < .55 else "free"))
SEL0 = 14; SITES0[SEL0 - 1]["st"] = "sel"
FREE0 = sum(1 for s in SITES0 if s["st"] == "free"); BOOK0 = sum(1 for s in SITES0 if s["st"] == "booked")
def map0():
    pos = []
    for k in range(4): pos.append((140 + k * 92, 150))       # 1-4 top
    for k in range(8): pos.append((500, 236 + k * 60))        # 5-12 right
    for xx in (470, 380, 164, 74): pos.append((xx, 728))       # 13-16 bottom
    for k in range(8): pos.append((44, 656 - k * 60))         # 17-24 left
    col = {"booked": "#c9c4b6", "free": "#fff", "sel": CR0}
    pads = ""
    for s, (x, y) in zip(SITES0, pos):
        tc = "#fff" if s["st"] == "sel" else FT0
        stroke = FT0 if s["st"] != "booked" else "#a9a392"
        dash = ' stroke-dasharray="5 4"' if s["t"] == "Tent" else ""
        pads += f'<rect x="{x}" y="{y}" width="56" height="44" rx="8" fill="{col[s["st"]]}" stroke="{stroke}" stroke-width="3"{dash}/><text x="{x + 28}" y="{y + 30}" text-anchor="middle" font-family="Source Sans 3" font-weight="800" font-size="23" fill="{tc}"><tspan>{s["n"]}</tspan></text>'
    trees = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#3f7a5e" opacity=".85"/>' for x, y, r in [(220, 310, 22), (250, 350, 16), (380, 300, 22), (360, 560, 20), (230, 600, 18), (390, 630, 16), (250, 480, 16), (575, 140, 18), (575, 770, 20), (25, 760, 18), (28, 140, 18)])
    return f'''<svg viewBox="0 0 600 980" style="position:absolute;inset:0;width:100%;height:100%"><rect width="600" height="980" fill="#e7ecd9"/>
<path d="M0 0 H600 V196 Q500 230 400 204 Q300 180 200 212 Q100 236 0 200 Z" fill="#a9cbe0"/><path d="M60 120 h60 M420 90 h70 M250 150 h50" stroke="#8ab6d0" stroke-width="3" stroke-linecap="round"/><path d="M300 900 V980" stroke="#b9ab8f" stroke-width="34"/><text x="330" y="960" font-family="Source Sans 3" font-weight="700" font-size="17" fill="{MU0}"><tspan>To the highway</tspan></text><g transform="translate(0,100)"><text x="300" y="62" text-anchor="middle" font-family="Lora" font-style="italic" font-weight="700" font-size="24" fill="{LK0}"><tspan>Lake</tspan></text>
<rect x="140" y="232" width="320" height="470" rx="60" fill="none" stroke="#b9ab8f" stroke-width="34"/><rect x="140" y="232" width="320" height="470" rx="60" fill="none" stroke="#e9dfc8" stroke-width="2" stroke-dasharray="10 10"/>
<path d="M300 719 V800" stroke="#b9ab8f" stroke-width="34"/>{trees}
<rect x="252" y="420" width="96" height="58" rx="8" fill="{FT0}"/><text x="300" y="455" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="15" fill="#fff"><tspan>Washrooms</tspan></text>
<rect x="265" y="752" width="70" height="32" rx="6" fill="{FT0}"/><text x="300" y="774" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="15" fill="#fff"><tspan>Gate</tspan></text>{pads}</g></svg>'''
FORM0 = [("Site", f"{SEL0} · {SITES0[SEL0 - 1]['t']} · fits up to 32 ft"), ("Dates", "Fri 16 Jul to Sun 18 Jul 2027"), ("Nights", "2"), ("Campers", "4"), ("RV length", "28 ft"), ("Pets", "1 dog, on a leash"), ("Arrive", "After 2 PM"), ("Vehicles", "1 RV and 1 car"), ("Fire pit", "Yes, at the site")]
P["p450_camp"] = page(f"""
body{{--f:'Source Sans 3';--h:'Lora';background:{BG0};color:{FT0};font-variant-numeric:lining-nums}}
.kk0{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{CR0};margin-top:22px}}
h1{{font-family:'Lora';font-weight:700;font-size:58px;line-height:1.22;letter-spacing:-.5px;margin-top:10px}} h1 span{{color:{CR0}}}
.w0{{flex:1;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:16px;min-height:0}}
.sm0{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:{MU0}}}
.cd0{{background:#fff;border-radius:20px;box-shadow:0 14px 30px rgba(36,73,61,.08)}}
.lc0{{display:flex;flex-direction:column;gap:16px;min-height:0}}.mp0{{flex:1;min-height:0;padding:14px 16px;display:flex;flex-direction:column;gap:8px}}.mp0 .im{{flex:1;min-height:0;position:relative;border-radius:12px;overflow:hidden}}
.lg0{{padding:14px 18px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.lg0 div{{display:flex;flex-direction:column;gap:6px}}.lg0 i{{width:34px;height:24px;border-radius:6px;border:3px solid {FT0}}}.lg0 b{{font:700 16px/1.3 'Source Sans 3'}}.lg0 strong{{font:700 26px/1.3 Lora}}
.fm0{{flex:1;padding:4px 18px 16px;display:flex;flex-direction:column;gap:8px}}.fm0 .t{{font:700 22px/1.3 Lora;margin:8px 0 2px}}.fm0 .f{{display:flex;flex-direction:column;gap:3px;border:1.5px solid #dcd8cc;border-radius:10px;padding:7px 12px}}.fm0 .f span{{font:600 13px/1.3 'Source Sans 3';color:{MU0}}}.fm0 .f b{{font:700 17px/1.3 'Source Sans 3';color:#1e2a26}}
.fm0 .nt{{font:600 15px/1.35 'Source Sans 3';color:#2f6b50;background:#e6f1ea;border-radius:9px;padding:8px 10px}}.fm0 .bt{{margin-top:auto;background:{CR0};color:#fff;border-radius:12px;padding:13px;text-align:center;font:700 18px/1.2 'Source Sans 3'}}
""", "<div class=kk0>CAMPGROUND · SITE BOOKING</div><h1>Site requests by email?<br><span>Campers pick a site on the map.</span></h1>",
f'''<div class=lc0><div class="cd0 mp0"><span class=sm0>SAMPLE CAMPGROUND · FRI 16 TO SUN 18 JUL 2027</span><div class=im>{map0()}</div></div>
<div class="cd0 lg0"><div><i style="background:#fff"></i><b>Free</b><strong>{FREE0}</strong></div><div><i style="background:#c9c4b6;border-color:#a9a392"></i><b>Booked</b><strong>{BOOK0}</strong></div><div><i style="background:{CR0};border-color:{CR0}"></i><b>Your pick</b><strong>Site {SEL0}</strong></div><div><i style="border-style:dashed"></i><b>Tent site</b><strong>{sum(1 for s in SITES0 if s["t"] == "Tent")}</strong></div></div></div>
{browser(f'<div class=fm0><div class=t>Book your site</div>{"".join(f"<div class=f><span>{a}</span><b>{b}</b></div>" for a, b in FORM0)}<div class=nt>Booked sites close on their own. No double booking.</div><div class=bt>Book site {SEL0}</div></div>', url="yourcampground.com/book", style="min-height:0")}''',
FT0, "Run a campground? DM us", f"background:{CR0};color:#fff")
