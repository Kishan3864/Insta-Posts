
# ───────── 440 USA · Senior move manager (downsizing and moving older adults) · SINGLE · Gelasio + Open Sans · sage / warm sand / plum
# New technique: room-by-room 100% stacked decision bars (keep, family, donate, sell) from one item tally, and a
# to-scale new-apartment plan where the "keep" furniture is placed and an item that does not fit is drawn dashed in red.
SG0 = "#5f7d63"; SD0 = "#efe6d6"; PL0 = "#6d3b5e"; INK0b = "#262326"; MU0b = "#6e6a66"
DC0 = [("Keep", SG0), ("To family", "#d39a3a"), ("Donate", "#7d8fb3"), ("Sell", PL0)]
RM0 = [("Living room", (6, 3, 9, 4)), ("Kitchen", (8, 4, 22, 6)), ("Main bedroom", (5, 2, 7, 2)), ("Guest room", (1, 3, 8, 5)), ("Garage", (2, 4, 18, 12))]
TOT0 = [sum(r[1][i] for r in RM0) for i in range(4)]
FU0 = [("Sofa", 1, 1, 7, 3, True), ("Armchair", 9, 1, 3, 3, True), ("Bed (queen)", 1, 11, 5, 7, True), ("Dresser", 8, 15, 5, 2, True), ("Table", 7, 6, 4, 3, True), ("China cabinet", 11, 6, 5, 2, False)]
def plan0():
    S = 22; o = 12; W, H = 15, 19
    out = f'<rect x="{o}" y="{o}" width="{W * S}" height="{H * S}" fill="#fbf8f2" stroke="{INK0b}" stroke-width="5"/><path d="M{o} {o + 10 * S} H{o + 7 * S} M{o + 10 * S} {o + 10 * S} H{o + W * S}" stroke="{INK0b}" stroke-width="4"/>'
    out += f'<text x="{o + 0.5 * S}" y="{o + 9.5 * S}" text-anchor="start" font-family="Open Sans" font-weight="700" font-size="14" fill="{MU0b}"><tspan>Living · 15 × 10 ft</tspan></text><text x="{o + 14.5 * S}" y="{o + 18.4 * S}" text-anchor="end" font-family="Open Sans" font-weight="700" font-size="14" fill="{MU0b}"><tspan>Bedroom · 15 × 9 ft</tspan></text>'
    for n, x, y, w, d, ok in FU0:
        if ok:
            out += f'<rect x="{o + x * S}" y="{o + y * S}" width="{w * S}" height="{d * S}" rx="6" fill="#cfdcd0" stroke="{SG0}" stroke-width="2.5"/><text x="{o + (x + w / 2) * S}" y="{o + (y + d / 2) * S + 5}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="14" fill="{INK0b}"><tspan>{n}</tspan></text>'
    n, x, y, w, d, ok = FU0[-1]
    out += f'<rect x="{o + 11 * S}" y="{o + 6 * S}" width="{w * S}" height="{d * S}" rx="6" fill="#f6dede" stroke="#c0392b" stroke-width="2.5" stroke-dasharray="7 5"/><text x="{o + 13.5 * S}" y="{o + 7 * S + 5}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="13" fill="#c0392b"><tspan>China cabinet?</tspan></text>'
    return f'<svg viewBox="0 0 {W * S + 50} {H * S + 24}" style="position:absolute;inset:0;width:100%;height:100%">{out}</svg>'
TL0 = [("Mon 30 Nov", "Sort and pack", "Two of us, room by room"), ("Thu 3 Dec", "Move day", "Movers 8 AM, new place by 1 PM"), ("Fri 4 Dec", "Unpack and set up", "Bed made, kitchen ready, photos up")]
P["p440_senior"] = page(f"""
body{{--f:'Open Sans';--h:'Gelasio';background:{SD0};color:{INK0b};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:{PL0};margin-top:22px}}
h1{{font-family:'Gelasio';font-weight:700;font-size:60px;line-height:1.2;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{SG0}}}
.w0b{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm0b{{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:{MU0b}}}
.cd0b{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(60,40,30,.08);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.tp0{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.dc0 .r{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:1px solid #efe8dc}}.dc0 .r .t{{display:flex;justify-content:space-between}}.dc0 .r b{{font:700 18px/1.3 'Open Sans'}}.dc0 .r span{{font:600 15px/1.3 'Open Sans';color:{MU0b}}}
.dc0 .bar{{display:flex;height:30px;border-radius:8px;overflow:hidden}}.dc0 .bar i{{display:flex;align-items:center;justify-content:center;font:700 13px/1 'Open Sans';font-style:normal;color:#fff}}
.dc0 .lg{{display:flex;flex-wrap:wrap;gap:8px 14px}}.dc0 .lg span{{display:flex;align-items:center;gap:7px;font:600 15px/1.3 'Open Sans'}}.dc0 .lg i{{width:16px;height:16px;border-radius:4px}}.dc0 .lg b{{font-weight:800}}
.pl0 .im{{flex:1;min-height:0;position:relative}}.pl0 .ok{{display:flex;align-items:center;gap:8px;font:700 16px/1.3 'Open Sans';color:{SG0}}}.pl0 p{{font:600 15px/1.4 'Open Sans';color:#c0392b}}
.tl0{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.tl0>div{{background:{PL0};color:#fff;border-radius:18px;padding:14px 18px;display:flex;flex-direction:column;gap:4px}}.tl0 span{{font:700 13px/1.3 'Open Sans';letter-spacing:1px;color:#e7cfe0}}.tl0 b{{font:700 23px/1.25 Gelasio}}.tl0 p{{font:500 15px/1.4 'Open Sans';color:#f1e3ec}}
""", "<div class=kk>SENIOR MOVE MANAGERS · DOWNSIZING</div><h1>Downsizing a whole house?<br><span>Every item has a plan.</span></h1>",
f'''<div class=w0b><div class=tp0><div class="cd0b dc0"><span class=sm0b>SAMPLE HOME · ITEMS SORTED BY ROOM</span>{"".join(f"""<div class=r><div class=t><b>{n}</b><span>{sum(c)} items</span></div><div class=bar>{"".join(f'<i style="flex:{v};background:{DC0[i][1]}">{v}</i>' for i, v in enumerate(c))}</div></div>""" for n, c in RM0)}
<div class=lg>{"".join(f'<span><i style="background:{c}"></i>{d} <b>{TOT0[i]}</b></span>' for i, (d, c) in enumerate(DC0))}</div></div>
<div class="cd0b pl0"><span class=sm0b>NEW APARTMENT · TO SCALE · KEEP ITEMS</span><div class=im>{plan0()}</div><div class=ok>{ic("check", 20, SG0, 3)}5 of 6 big keep items fit</div><p>China cabinet is 1 ft too wide for the dining wall. Ask the family first.</p></div></div>
<div class=tl0>{"".join(f'<div><span>{d.upper()}</span><b>{a}</b><p>{b}</p></div>' for d, a, b in TL0)}</div></div>''',
INK0b, "Help seniors move? DM us", f"background:{SG0};color:#fff")
