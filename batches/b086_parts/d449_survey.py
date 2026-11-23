
# ───────── 449 INDIA · Land surveyor (plot survey) · SINGLE · Cardo + DM Sans · blueprint ink / graph cream / stake red
# New technique: plot boundary drawn from surveyed coordinates on graph paper, side lengths and area computed in code
# (shoelace formula) and the same numbers reused in the table, the area card and the client message.
BL9 = "#1f4e79"; GC9 = "#f7f4ea"; SR9 = "#c8372d"; MU9 = "#6a6656"; INK9 = "#1d2733"
PT9 = [("P1", 0.0, 0.0), ("P2", 38.2, 2.1), ("P3", 41.5, 27.8), ("P4", 24.0, 36.4), ("P5", 3.6, 31.2), ("P6", -1.8, 14.5)]
N9 = len(PT9)
AREA9 = abs(sum(PT9[i][1] * PT9[(i + 1) % N9][2] - PT9[(i + 1) % N9][1] * PT9[i][2] for i in range(N9))) / 2
SIDES9 = [(PT9[i][0], PT9[(i + 1) % N9][0], math.dist(PT9[i][1:], PT9[(i + 1) % N9][1:])) for i in range(N9)]
PER9 = sum(s[2] for s in SIDES9)
def plot9():
    S = 14; ox = 90; oy = 600  # metres to px, y up
    X = lambda e: ox + e * S; Y = lambda n: oy - n * S
    grid = "".join(f'<path d="M{x} 0 V840" stroke="#d9d2bd" stroke-width="{1.6 if (x - 25) % 65 == 0 else .7}"/>' for x in range(25, 740, 13)) + "".join(f'<path d="M0 {y} H740" stroke="#d9d2bd" stroke-width="{1.6 if (y - 24) % 65 == 0 else .7}"/>' for y in range(24, 840, 13))
    poly = " ".join(f"{X(e):.1f},{Y(n):.1f}" for _, e, n in PT9)
    cx = sum(p[1] for p in PT9) / N9; cy = sum(p[2] for p in PT9) / N9
    lab = ""
    for a, b, d in SIDES9:
        pa = [p for p in PT9 if p[0] == a][0]; pb = [p for p in PT9 if p[0] == b][0]
        mx = (pa[1] + pb[1]) / 2; my = (pa[2] + pb[2]) / 2; vx = mx - cx; vy = my - cy; L = math.hypot(vx, vy)
        lx = X(mx - vx / L * 4.2); ly = Y(my - vy / L * 4.2)
        lab += f'<rect x="{lx - 56:.0f}" y="{ly - 19:.0f}" width="112" height="36" rx="8" fill="#fff" stroke="{BL9}" stroke-width="2"/><text x="{lx:.0f}" y="{ly + 7:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="21" fill="{BL9}"><tspan>{d:.1f} m</tspan></text>'
    pts = ""
    for n, e, nn in PT9:
        dx = 1 if e >= cx else -1; dy = -1 if nn >= cy else 1
        tx = X(e) + dx * 20 - (0 if dx > 0 else 32); ty = Y(nn) + dy * 26 + 8
        pts += f'<rect x="{X(e) - 9:.0f}" y="{Y(nn) - 9:.0f}" width="18" height="18" transform="rotate(45 {X(e):.0f} {Y(nn):.0f})" fill="{SR9}" stroke="#fff" stroke-width="2"/><text x="{tx:.0f}" y="{ty:.0f}" font-family="DM Sans" font-weight="800" font-size="24" fill="{SR9}"><tspan>{n}</tspan></text>'
    return f'''<svg viewBox="0 0 740 840" style="position:absolute;inset:0;width:100%;height:100%"><rect width="740" height="840" fill="{GC9}"/>{grid}<g transform="translate(0,110)">
<polygon points="{poly}" fill="{BL9}" fill-opacity=".10" stroke="{BL9}" stroke-width="4"/>{lab}{pts}
<text x="{X(cx):.0f}" y="{Y(cy) - 6:.0f}" text-anchor="middle" font-family="Cardo" font-weight="700" font-size="40" fill="{BL9}"><tspan>{AREA9:,.0f} m²</tspan></text><text x="{X(cx):.0f}" y="{Y(cy) + 30:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="20" fill="{MU9}"><tspan>Sample plot 112</tspan></text>
<rect x="470" y="690" width="70" height="10" fill="{INK9}"/><rect x="540" y="690" width="70" height="10" fill="#fff" stroke="{INK9}" stroke-width="1.5"/><text x="470" y="680" font-family="DM Sans" font-weight="700" font-size="18" fill="{INK9}"><tspan>0</tspan></text><text x="588" y="680" font-family="DM Sans" font-weight="700" font-size="18" fill="{INK9}"><tspan>10 m</tspan></text>
<path d="M650 70 V30 M640 46 L650 30 L660 46" stroke="{INK9}" stroke-width="3" fill="none"/><text x="643" y="92" font-family="DM Sans" font-weight="800" font-size="18" fill="{INK9}"><tspan>N</tspan></text></g></svg>'''
STG9 = [("Field visit, 6 points taken", "Mon 23 Nov", True), ("Drawing and area worked out", "Mon 23 Nov", True), ("PDF sent to the client's phone", "Tue 24 Nov", False), ("Boundary stones fixed", "Fri 27 Nov", False)]
P["p449_survey"] = page(f"""
body{{--f:'DM Sans';--h:'Cardo';background:#efeadc;color:{INK9};font-variant-numeric:lining-nums}}
.kk9{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{SR9};margin-top:22px}}
h1{{font-family:'Cardo';font-weight:700;font-size:62px;line-height:1.22;letter-spacing:-.3px;margin-top:10px}} h1 span{{color:{BL9}}}
.w9{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm9{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:{MU9}}}
.cd9{{background:#fff;border-radius:20px;box-shadow:0 14px 30px rgba(29,39,51,.08)}}
.tp9{{flex:1;min-height:0;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:16px}}
.pl9{{padding:14px 16px;display:flex;flex-direction:column;gap:8px}}.pl9 .im{{flex:1;min-height:0;position:relative;border-radius:12px;overflow:hidden}}
.rc9{{display:flex;flex-direction:column;gap:16px}}.co9{{flex:1;padding:14px 18px;display:flex;flex-direction:column}}.co9 .r{{flex:1;display:grid;grid-template-columns:44px 1fr 1fr;gap:6px;align-items:center;border-top:1px solid #efeadf}}.co9 .h{{flex:none;border:0;padding:4px 0 6px}}.co9 .h span{{font:700 12px/1.4 'DM Sans';letter-spacing:1px;color:{MU9};text-align:right}}
.co9 .r b{{font:800 18px/1.3 'DM Sans';color:{SR9}}}.co9 .r>span{{font:600 18px/1.3 'DM Sans';text-align:right}}
.ar9{{background:{BL9};color:#fff;border-radius:20px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}}.ar9 .sm9{{color:#b9cde0}}.ar9 b{{display:block;font:700 44px/1.35 Cardo;margin-bottom:4px}}.ar9 .r{{display:flex;justify-content:space-between;font:600 17px/1.4 'DM Sans';border-top:1px solid #3a6a96;padding-top:6px}}
.bt9{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;flex:none}}.bt9 .s{{padding:14px 16px;display:flex;flex-direction:column;gap:8px}}.bt9 .s i{{width:24px;height:24px;border-radius:50%;border:3px solid #c9c2ad;display:flex;align-items:center;justify-content:center;font:900 13px/1 'DM Sans';font-style:normal;color:#fff}}.bt9 .s i.d{{background:{BL9};border-color:{BL9}}}
.bt9 .s b{{font:700 18px/1.35 'DM Sans'}}.bt9 .s span{{font:600 15px/1.3 'DM Sans';color:{MU9}}}
""", "<div class=kk9>LAND SURVEYOR · PLOT SURVEY</div><h1>Field book to drawing in days?<br><span>Points in, plot area out.</span></h1>",
f'''<div class=w9><div class=tp9><div class="cd9 pl9"><span class=sm9>SAMPLE PLOT 112 · 6 BOUNDARY POINTS · ONE SQUARE = 5 M</span><div class=im>{plot9()}</div></div>
<div class=rc9><div class="cd9 co9"><div class="r h"><span style="text-align:left">PT</span><span>EAST (M)</span><span>NORTH (M)</span></div>{"".join(f'<div class=r><b>{n}</b><span>{e:.1f}</span><span>{nn:.1f}</span></div>' for n, e, nn in PT9)}</div>
<div class=ar9><span class=sm9>AREA · WORKED OUT</span><b>{AREA9:,.0f} m²</b><div class=r><span>Square feet</span><span>{AREA9 * 10.7639:,.0f}</span></div><div class=r><span>Acres</span><span>{AREA9 / 4046.86:.2f}</span></div><div class=r><span>Boundary</span><span>{PER9:.1f} m</span></div></div></div></div>
<div class=bt9>{"".join(f'<div class="cd9 s"><i class="{"d" if d else ""}">{"✓" if d else ""}</i><b>{a}</b><span>{dt}</span></div>' for a, dt, d in STG9)}</div></div>''',
INK9, "Do land surveys? DM us", f"background:{SR9};color:#fff")
