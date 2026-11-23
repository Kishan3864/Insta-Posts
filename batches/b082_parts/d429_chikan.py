
# ───────── 429 INDIA · Chikankari unit (hand embroidery given to home karigars) · SINGLE · Cardo + Source Sans 3 · muslin white / thread lilac / indigo
# New technique: lane map of karigar homes with heat halos sized by pieces at each home and coloured by due status
# (computed against today), plus a phone "give work" slip with an SVG buti motif swatch.
MS9 = "#f7f3ec"; LI9 = "#8e6bb8"; IN9 = "#283a6b"; INK9 = "#22213a"; MU9 = "#6f6a80"; RD9 = "#c8553d"; GD9 = "#d9a441"; GN9 = "#4c9a7a"
TODAY9 = 23
KG9 = [("K-01", 110, 90, 12, 26), ("K-02", 250, 70, 8, 24), ("K-03", 420, 110, 18, 20), ("K-04", 90, 240, 10, 30), ("K-05", 210, 300, 6, 25),
       ("K-06", 470, 260, 14, 30), ("K-07", 360, 360, 12, 28), ("K-08", 120, 400, 9, 21), ("K-09", 470, 420, 7, 27), ("K-10", 260, 180, 4, 23)]
def st9(d): return ("Late", RD9) if d < TODAY9 else ("Due this week", GD9) if d <= TODAY9 + 5 else ("On time", GN9)
WITH9 = sum(k[3] for k in KG9); LATE9 = [k for k in KG9 if k[4] < TODAY9]
BACK9 = 58
def map9():
    lanes = '<path d="M0 160 H580 M0 330 H580 M180 0 V520 M400 0 V520 M180 250 H400" stroke="#e6dccb" stroke-width="26" fill="none" stroke-linecap="round"/>'
    halos = defs = dots = ""
    for c, x, y, n, d in KG9:
        lab, col = st9(d); r = 10 + math.sqrt(n) * 6
        dots += f'<circle cx="{x}" cy="{y}" r="{r * 1.9:.0f}" fill="url(#h9{col[1:]})"/>'
    for c, x, y, n, d in KG9:
        lab, col = st9(d); r = 10 + math.sqrt(n) * 6
        dots += f'<circle cx="{x}" cy="{y}" r="{r:.0f}" fill="{col}" stroke="#fff" stroke-width="3"/><text x="{x}" y="{y + 6}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="17" fill="#fff"><tspan>{n}</tspan></text><text x="{x}" y="{y + r + 20:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="16" fill="{INK9}"><tspan>{c}</tspan></text>'
    for col in {RD9, GD9, GN9}:
        defs += f'<radialGradient id="h9{col[1:]}"><stop offset="0" stop-color="{col}" stop-opacity=".35"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient>'
    unit = f'<rect x="262" y="226" width="96" height="48" rx="10" fill="{IN9}"/><text x="310" y="256" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="16" fill="#fff"><tspan>Your unit</tspan></text>'
    return f'<svg viewBox="40 30 500 450" style="display:block;width:100%;height:100%"><defs>{defs}</defs>{lanes}{dots}{unit}</svg>'
def buti9(s=150):
    g = ""
    for cx, cy in [(30, 30), (90, 30), (60, 70), (30, 110), (90, 110)]:
        g += "".join(f'<ellipse cx="{cx}" cy="{cy - 9}" rx="5" ry="9" fill="none" stroke="{LI9}" stroke-width="2" transform="rotate({a} {cx} {cy})"/>' for a in range(0, 360, 60)) + f'<circle cx="{cx}" cy="{cy}" r="3" fill="{LI9}"/>'
    return f'<svg viewBox="0 0 120 140" style="display:block;width:100%;height:100%" preserveAspectRatio="xMidYMid slice"><rect width="120" height="140" fill="#fdfbf7"/>{g}</svg>'
K7 = next(k for k in KG9 if k[0] == "K-07")
APP9 = f'''<div class=ap9><div class=hd><span>Give work</span><b>{K7[0]} · Sample Karigar</b></div>
<div class=sw>{buti9()}<div><b>Design D-4</b><span>White kurta · lilac buti · sample</span></div></div>
{"".join(f'<div class=f><span>{a}</span><b>{b}</b></div>' for a, b in [("Pieces", f"{K7[3]} kurtas"), ("Thread", "6 skeins, lilac"), ("Given", "Mon 16 Nov"), ("Due back", f"Sat {K7[4]} Nov"), ("Sizes", "S 4 · M 4 · L 4"), ("First piece", "Photo checked ✓")])}
<div class=nt><span>Note for karigar</span><p>Keep the neck border thin, same as the photo.</p></div><div class=bt>Save and send slip</div></div>'''
P["p429_chikan"] = page(f"""
body{{--f:'Source Sans 3';--h:'Cardo';background:{MS9};color:{INK9}}}
.kk{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{LI9};margin-top:22px}}
h1{{font-family:'Cardo';font-weight:700;font-size:64px;line-height:1.18;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{LI9}}}
.w9{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:20px;min-height:0}}
.lf9{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm9{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:{MU9}}}
.cd9{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(40,58,107,.08);padding:16px 20px;display:flex;flex-direction:column;gap:8px}}
.mp9{{flex:1;min-height:0}}.mp9 .m{{flex:1;min-height:0}}.mp9 .lg{{display:flex;gap:16px;flex-wrap:wrap}}.mp9 .lg div{{display:flex;align-items:center;gap:8px;font:600 16px/1.3 'Source Sans 3'}}.mp9 .lg i{{width:16px;height:16px;border-radius:50%}}
.st9{{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}}.st9 div{{background:{IN9};color:#fff;border-radius:18px;padding:12px 16px;display:flex;flex-direction:column}}.st9 b{{font:700 40px/1.1 Cardo;margin-bottom:10px}}.st9 span{{font:600 16px/1.3 'Source Sans 3';color:#cdd5ec}}
.lt9{{flex-direction:row;align-items:center;gap:14px;background:#fbe9e4;box-shadow:none}}.lt9 b{{display:block;margin-bottom:6px;font:700 19px/1.35 'Source Sans 3';color:#8c3422}}.lt9 span{{font:500 17px/1.35 'Source Sans 3';color:#8c3422}}
.ph9{{display:flex;align-items:center}}
.ap9{{flex:1;padding:6px 18px 18px;display:flex;flex-direction:column;gap:8px;font-family:'Source Sans 3'}}.ap9 .hd span{{font:600 14px/1.3 'Source Sans 3';color:{MU9}}}.ap9 .hd b{{display:block;font:700 21px/1.3 'Source Sans 3';color:{INK9}}}
.ap9 .sw{{display:flex;gap:12px;align-items:center;background:#f3eef9;border-radius:16px;padding:10px}}.ap9 .sw svg{{width:84px!important;height:96px!important;border-radius:10px;flex:none}}.ap9 .sw b{{display:block;font:700 18px/1.3 'Source Sans 3';color:{INK9}}}.ap9 .sw span{{font:500 15px/1.35 'Source Sans 3';color:{MU9}}}
.ap9 .f{{display:flex;justify-content:space-between;gap:8px;padding:11px 12px;border-radius:12px;background:#f6f4f0}}.ap9 .f span{{font:500 16px/1.3 'Source Sans 3';color:{MU9}}}.ap9 .f b{{font:700 16px/1.3 'Source Sans 3';color:{INK9}}}
.ap9 .nt{{border:2px dashed #cbbde0;border-radius:12px;padding:10px 12px}}.ap9 .nt span{{font:600 14px/1.3 'Source Sans 3';color:{MU9}}}.ap9 .nt p{{font:600 16px/1.4 'Source Sans 3';color:{INK9}}}
.ap9 .bt{{margin-top:auto;background:{LI9};color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 17px/1.2 'Source Sans 3'}}
""", "<div class=kk>CHIKANKARI · WORK GIVEN TO HOME KARIGARS</div><h1>Who has which kurtas?<br><span>See every karigar's pieces.</span></h1>",
f'''<div class=w9><div class=lf9><div class="cd9 mp9"><span class=sm9>PIECES AT EACH KARIGAR'S HOME · TODAY MON {TODAY9} NOV · SAMPLE</span><div class=m>{map9()}</div><div class=lg>{"".join(f'<div><i style="background:{c}"></i>{t}</div>' for t, c in [("Late", RD9), ("Due this week", GD9), ("On time", GN9)])}</div></div>
<div class="cd9 lt9">{ic("bell", 30, RD9)}<div><b>{len(LATE9)} karigars late</b><span style="display:block">{" · ".join(f"{k[0]}: {k[3]} pieces, due {k[4]} Nov" for k in LATE9)}</span></div></div>
<div class=st9><div><b>{WITH9}</b><span>pieces with karigars</span></div><div><b>{BACK9}</b><span>came back this week</span></div><div><b>{len(KG9)}</b><span>karigars at work</span></div></div></div>
<div class=ph9>{phone(APP9, w=380, h=780)}</div></div>''',
INK9, "Run a chikankari unit? DM us", f"background:{IN9};color:#fff")
