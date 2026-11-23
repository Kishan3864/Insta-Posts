
# ───────── 418 USA · Stump grinding · SINGLE · Bitter + Source Sans 3 · sawdust tan / bark brown / lawn green
# New technique: to-scale top-down yard where each stump is an SVG tree-ring cross-section (seeded wobbly rings, bark rim,
# check crack) sized by its measured diameter; the gate width decides the grinder, totals come from the stump list.
T8 = "#efe2c6"; BR8 = "#5a3b24"; GR8 = "#4f8a34"; K8 = "#2a1d12"
ST8 = [(1, 18, "By the side fence", 80, 110), (2, 26, "Surface roots", 400, 170), (3, 10, "In the flower bed", 140, 380), (4, 32, "Near the patio", 380, 430)]
PX8 = 3.4
TOT8 = sum(s[1] for s in ST8)
GATE8 = 36
def stump8(x, y, d, seed):
    rnd = random.Random(seed); R = d * PX8 / 2
    def ring(r, wob):
        pts = []
        for k in range(36):
            a = k / 36 * 2 * math.pi; rr = r * (1 + rnd.uniform(-wob, wob))
            pts.append(f"{x + rr * math.cos(a):.1f},{y + rr * math.sin(a):.1f}")
        return "M" + " L".join(pts) + " Z"
    rings = "".join(f'<path d="{ring(R * f, .03)}" fill="none" stroke="#b98f5c" stroke-width="1.4"/>' for f in [.25, .42, .58, .72, .84])
    return f'''<path d="{ring(R + 6, .05)}" fill="{BR8}"/><path d="{ring(R, .02)}" fill="#e6c99a"/>{rings}<circle cx="{x}" cy="{y}" r="{max(2.5, R * .06):.1f}" fill="#9b6b3c"/><path d="M{x} {y} L{x + R * .9:.1f} {y - R * .35:.1f}" stroke="#7a5230" stroke-width="2"/>'''
def yard8():
    W, H, OY = 540, 1080, 250
    lab = "".join(f'<circle cx="{x + d * PX8 / 2 + 8:.0f}" cy="{y - d * PX8 / 2 - 4:.0f}" r="17" fill="{K8}"/><text x="{x + d * PX8 / 2 + 8:.0f}" y="{y - d * PX8 / 2 + 3:.0f}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="20" fill="#fff"><tspan>{n}</tspan></text>' for n, d, _, x, y in ST8)
    route = f'<path d="M520 560 L470 560 L470 300 L270 300 L270 170" fill="none" stroke="#fff" stroke-width="4" stroke-dasharray="3 10" stroke-linecap="round"/>'
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:100%"><defs><pattern id="ln8" width="40" height="1080" patternUnits="userSpaceOnUse"><rect width="20" height="1080" fill="#6ea44c"/><rect x="20" width="20" height="1080" fill="#67993f"/></pattern></defs>
<rect width="{W}" height="{H}" rx="14" fill="url(#ln8)"/><rect x="10" y="10" width="{W - 20}" height="{H - 20}" fill="none" stroke="#8a6a45" stroke-width="8"/>
<rect x="20" y="20" width="{W - 40}" height="190" rx="6" fill="#b9a78f"/><rect x="20" y="20" width="{W - 40}" height="190" rx="6" fill="none" stroke="#8d7b63" stroke-width="3"/><text x="{W // 2}" y="125" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="30" fill="#4a3c2c"><tspan>House</tspan></text>
<rect x="190" y="210" width="160" height="40" fill="#c9a77d"/><text x="270" y="237" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="17" fill="#4a3c2c"><tspan>Back door</tspan></text>
<rect x="40" y="910" width="150" height="120" rx="6" fill="#9c7b55"/><text x="115" y="976" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="19" fill="#fff"><tspan>Shed</tspan></text>
<g transform="translate(0 {OY})"><rect x="470" y="536" width="70" height="54" fill="#6ea44c"/><text x="404" y="570" font-family="Source Sans 3" font-weight="700" font-size="17" fill="#fff"><tspan>Gate {GATE8} in</tspan></text>
<rect x="60" y="470" width="190" height="100" rx="6" fill="#cfc6b6"/><text x="155" y="526" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="20" fill="#5e5547"><tspan>Patio</tspan></text>
<rect x="70" y="330" width="150" height="100" rx="40" fill="#8a5a3a" opacity=".55"/>{route}
{"".join(stump8(x, y, d, n * 13) for n, d, _, x, y in ST8)}{lab}</g></svg>'''
P["p418_stump"] = page(f"""
body{{--f:'Source Sans 3';--h:'Bitter';background:{T8};color:{K8}}}
.kk{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{GR8};margin-top:22px}}
h1{{font-family:'Bitter';font-weight:800;font-size:62px;line-height:1.22;letter-spacing:0;margin-top:20px}} h1 span{{color:{BR8}}}
.vw8{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}
.sm8{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#7c6a52}}
.cd8{{background:#fffaf0;border-radius:24px;box-shadow:0 14px 30px rgba(60,40,10,.1);padding:16px 18px;display:flex;flex-direction:column;gap:10px}}
.yd8{{min-height:0}}.yd8 .sv{{flex:1;min-height:0}}
.rt8{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.ls8{{flex:1}}.ls8 .r{{flex:1;display:grid;grid-template-columns:40px 88px 1fr;gap:12px;align-items:center;border-top:1px solid #eee0c4}}
.ls8 .r i{{width:36px;height:36px;border-radius:50%;background:{K8};color:#fff;font:700 19px/36px 'Source Sans 3';font-style:normal;text-align:center}}.ls8 .r b{{font:800 28px/1.3 Bitter}}.ls8 .r span{{font:600 18px/1.3 'Source Sans 3';color:#5d4c38}}
.ls8 .tt{{display:flex;justify-content:space-between;align-items:center;background:#f1e3c4;border-radius:12px;padding:10px 14px}}.ls8 .tt span{{font:700 17px/1.3 'Source Sans 3'}}.ls8 .tt b{{font:800 26px/1.3 Bitter;color:{BR8}}}
.op8{{display:flex;flex-wrap:wrap;gap:8px}}.op8 span{{font:700 16px/1.2 'Source Sans 3';border-radius:10px;padding:9px 12px;background:#e4efdc;color:#2f5f1c}}
.jb8{{background:{K8};color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column}}.jb8 .sm8{{color:#cbb995}}
.jb8 .r{{display:flex;justify-content:space-between;gap:10px;padding:8px 0;border-top:1px solid rgba(255,255,255,.12)}}.jb8 .r span{{font:500 17px/1.3 'Source Sans 3';color:#d7c9ae}}.jb8 .r b{{font:700 18px/1.3 'Source Sans 3';text-align:right}}
.jb8 .bt{{margin-top:8px;background:{GR8};border-radius:12px;padding:12px;text-align:center;font:700 18px/1.2 'Source Sans 3'}}
""", "<div class=kk>STUMP GRINDING · SITE VISITS</div><h1>Stump quotes by guesswork?<br><span>Measure each stump once.</span></h1>",
f'''<div class=vw8><div class="cd8 yd8"><span class=sm8>SAMPLE BACKYARD · STUMPS TO SCALE</span><div class=sv>{yard8()}</div></div>
<div class=rt8><div class="cd8 ls8"><span class=sm8>STUMP LIST · MEASURED ACROSS</span>{"".join(f'<div class=r><i>{n}</i><b>{d} in</b><span>{t}</span></div>' for n, d, t, x, y in ST8)}<div class=tt><span>{len(ST8)} stumps · total</span><b>{TOT8} in</b></div></div>
<div class=op8><span>Grind 6 in below grade</span><span>Haul chips away</span><span>Lines marked</span></div>
<div class=jb8><span class=sm8>JOB CARD · SAMPLE HOME · ZIP 12345</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Visit", "Fri 27 Nov · 9 AM"), ("Machine", f"Small grinder (fits {GATE8} in gate)"), ("Photos", "6 added by the owner")])}<div class=bt>Send quote</div></div></div></div>''',
K8, "Grind stumps? DM us", f"background:{BR8};color:#fff")
