
# ───────── 425 USA · Tile and grout cleaning · SINGLE · Crimson Text + Open Sans · tile white / grout grey / aqua
# New technique: to-scale SVG floor plan (24 px per ft) with tile-grid pattern fills per service, carpet hatched out,
# room square feet computed from the plan, plus a diagonal before/after tile close-up drawn as two clipped tile grids.
AQ5 = "#2a9d9b"; NV5 = "#1d3557"; INK5 = "#1d2b2f"; BG5 = "#edf3f3"
SV5 = {"clean": ("Clean only", "#e6ecec"), "seal": ("Clean + clear seal", "#bfe5e3"), "color": ("Color seal", "#c9d3e6")}
RM5 = [("Kitchen", 0, 0, 12, 14, "seal"), ("Entry", 12, 0, 6, 10, "color"), ("Hall bath", 12, 10, 6, 8, "seal"), ("Laundry", 0, 14, 7, 8, "clean")]
TOT5 = sum(w * h for _, _, _, w, h, _ in RM5)
F5 = 24
def plan5():
    W, H = 18 * F5 + 20, 22 * F5 + 20
    pats = "".join(f'<pattern id="tp5{k}" width="24" height="24" patternUnits="userSpaceOnUse"><rect width="24" height="24" fill="{c}"/><path d="M0 0H24M0 0V24" stroke="#ffffff" stroke-width="2"/></pattern>' for k, (_, c) in SV5.items())
    rooms = ""
    for n, x, y, w, h, s in RM5:
        X, Y = 10 + x * F5, 10 + y * F5
        rooms += f'<rect x="{X}" y="{Y}" width="{w * F5}" height="{h * F5}" fill="url(#tp5{s})" stroke="{INK5}" stroke-width="4"/>'
        cx, cy = X + w * F5 / 2, Y + h * F5 / 2
        rooms += f'<text x="{cx}" y="{cy - 10}" text-anchor="middle" font-family="Crimson Text" font-weight="700" font-size="26" fill="{INK5}"><tspan>{n}</tspan></text><text x="{cx}" y="{cy + 18}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="#44575c"><tspan>{w} × {h} ft · {w * h} sq ft</tspan></text>'
    carpet = f'<path d="M{10 + 7 * F5} {10 + 14 * F5} H{10 + 12 * F5} V{10 + 18 * F5} H{10 + 18 * F5} V{10 + 22 * F5} H{10 + 7 * F5} Z" fill="url(#cp5)" stroke="{INK5}" stroke-width="4"/><text x="{10 + 12.5 * F5}" y="{10 + 20.4 * F5}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="#6b7478"><tspan>Carpet · not included</tspan></text>'
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto"><defs>{pats}<pattern id="cp5" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="12" height="12" fill="#f3f1ec"/><rect width="4" height="12" fill="#ddd8cd"/></pattern></defs>{rooms}{carpet}</svg>'''
def tiles5():
    def grid(tile, grout, stain=False):
        rnd = random.Random(2)
        g = f'<rect width="420" height="260" fill="{grout}"/>' + "".join(f'<rect x="{6 + c * 104}" y="{6 + r * 64}" width="96" height="56" rx="3" fill="{tile}"/>' for r in range(4) for c in range(4))
        if stain: g += "".join(f'<circle cx="{rnd.uniform(0, 420):.0f}" cy="{rnd.uniform(0, 260):.0f}" r="{rnd.uniform(3, 9):.1f}" fill="#7d6f5c" opacity=".25"/>' for _ in range(30))
        return g
    return f'''<svg viewBox="0 0 420 260" width="420" style="display:block;width:100%;height:auto;border-radius:14px"><defs><clipPath id="bf5"><path d="M0 0 H250 L170 260 H0 Z"/></clipPath><clipPath id="af5"><path d="M262 0 H420 V260 H182 Z"/></clipPath></defs>
<rect width="420" height="260" fill="#fff"/><g clip-path="url(#bf5)">{grid("#e9dfc9", "#4f463d", True)}</g><g clip-path="url(#af5)">{grid("#fbfbf8", "#cfd5d3")}</g>
<rect x="14" y="14" width="86" height="32" rx="8" fill="{INK5}"/><text x="57" y="36" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="#fff"><tspan>Before</tspan></text>
<rect x="320" y="214" width="86" height="32" rx="8" fill="{AQ5}"/><text x="363" y="236" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="#fff"><tspan>After</tspan></text></svg>'''
P["p425_grout"] = page(f"""
body{{--f:'Open Sans';--h:'Crimson Text';background:{BG5};color:{INK5};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:{AQ5};margin-top:22px}}
h1{{font-family:'Crimson Text';font-weight:700;font-size:64px;line-height:1.22;letter-spacing:-.5px;margin-top:18px}} h1 span{{color:{AQ5}}}
.vw5{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.sm5{{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#5f6f73}}
.cd5{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(29,43,47,.08);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.pl5{{flex:1;min-height:0}}.pv5{{flex:1;min-height:0;display:flex;justify-content:center}}.pv5 svg{{width:auto!important;height:100%!important;max-width:100%}}.lg5{{display:flex;flex-wrap:wrap;gap:8px 16px}}.lg5 div{{display:flex;align-items:center;gap:10px;font:600 17px/1.3 'Open Sans'}}.lg5 i{{width:24px;height:24px;border-radius:6px;border:2px solid {INK5}}}
.rt5{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.ls5{{flex:1}}.ls5 .r{{flex:1;display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:center;border-top:1px solid #e3ebea;padding:4px 0}}.ls5 .r b{{font:700 19px/1.3 'Open Sans'}}.ls5 .r strong{{font:700 26px/1.35 'Crimson Text';text-align:right}}.ls5 .r span{{font:500 15px/1.3 'Open Sans';color:#5f6f73}}
.ls5 .tt{{display:flex;justify-content:space-between;align-items:center;background:#d8efee;border-radius:12px;padding:8px 14px}}.ls5 .tt span{{font:700 16px/1.3 'Open Sans'}}.ls5 .tt b{{font:700 30px/1.35 'Crimson Text';color:{AQ5}}}
.bk5{{background:{NV5};color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column}}.bk5 .sm5{{color:#a9bad3}}.bk5 .r{{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-top:1px solid rgba(255,255,255,.12)}}.bk5 .r span{{font:500 16px/1.3 'Open Sans';color:#cdd8e8}}.bk5 .r b{{font:700 17px/1.3 'Open Sans';text-align:right}}
.bk5 .bt{{margin-top:8px;background:{AQ5};border-radius:12px;padding:12px;text-align:center;font:700 17px/1.2 'Open Sans'}}
""", "<div class=kk>TILE AND GROUT CLEANING · HOME VISITS</div><h1>Grout quotes over the phone?<br><span>Plan every room first.</span></h1>",
f'''<div class=vw5><div class=rt5><div class="cd5 pl5"><span class=sm5>SAMPLE HOME · FLOOR PLAN TO SCALE</span><div class=pv5>{plan5()}</div><div class=lg5>{"".join(f'<div><i style="background:{c}"></i>{t}</div>' for t, c in SV5.values())}</div></div>
<div class=bk5><span class=sm5>BOOKING · SAMPLE HOME · ZIP 12345</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Day", "Tue 1 Dec"), ("Arrival", "8 to 10 AM window"), ("Furniture", "We move it")])}<div class=bt>Send quote</div></div></div>
<div class=rt5><div class=cd5><span class=sm5>WHAT CLEAN GROUT LOOKS LIKE</span>{tiles5()}</div>
<div class="cd5 ls5"><span class=sm5>ROOMS · MEASURED ON SITE</span>{"".join(f'<div class=r><b>{n}</b><strong>{w * h} sq ft</strong><span>{SV5[s][0]}</span></div>' for n, x, y, w, h, s in RM5)}<div class=tt><span>Tile to clean</span><b>{TOT5} sq ft</b></div></div>
</div></div>''',
INK5, "Clean tile and grout? DM us", f"background:{AQ5};color:#fff")
