
# ───────── 427 INDIA · Paper bag maker (shops, bakeries, garment stores) · SINGLE · Bitter + Inter · kraft / print green / paper white
# New technique: four kraft bags drawn to scale from W × H × gusset (14 px per inch) with handle types, plus the flat
# sheet layout (front, gusset, back, gusset, glue flap) computed from the same sizes, feeding a sheets-to-cut table.
KR7 = "#c49a6c"; KD7 = "#8a6440"; GN7 = "#2f6f4f"; PW7 = "#fbf7ef"; INK7 = "#2a2118"; BG7 = "#efe6d8"
BG_SZ7 = [("S", 6, 9, 3, "none"), ("M", 8, 10, 4, "flat"), ("L", 10, 12, 4, "twist"), ("XL", 12, 15, 5, "twist")]
SZ7 = {k: (w, h, g, hd) for k, w, h, g, hd in BG_SZ7}
HN7 = {"none": "No handle", "flat": "Flat handle", "twist": "Twisted handle"}
OR7 = [("Sample Garment Store", "L", 1000, "Print"), ("Sample Garment Store", "XL", 500, "Print"),
       ("Sample Sweet Shop", "M", 800, "Plain"), ("Sample Sweet Shop", "S", 1200, "Plain"),
       ("Sample Bakery", "S", 2000, "Plain"), ("Sample Gift Shop", "M", 300, "Print"), ("Sample Gift Shop", "L", 200, "Print")]
TOT7 = {k: sum(o[2] for o in OR7 if o[1] == k) for k in SZ7}
def sheet7(k):
    w, h, g, _ = SZ7[k]; return (2 * w + 2 * g + 1, h + 0.75 * g + 1.5)
def fmt7(n): return f"{n:,}"
def bags7():
    S = 14; out = ""; x = 20; base = 330
    for k, w, h, g, hd in BG_SZ7:
        W, H, G = w * S, h * S, g * S * .5
        y = base - H
        out += f'<path d="M{x + W} {y} L{x + W + G} {y - G * .5} V{base - G * .5} L{x + W} {base} Z" fill="{KD7}"/>'
        out += f'<rect x="{x}" y="{y}" width="{W}" height="{H}" fill="{KR7}"/><rect x="{x}" y="{y}" width="{W}" height="16" fill="#b88b5c"/>'
        out += "".join(f'<path d="M{x + 6 + i * 9} {y + 22} v{H - 30}" stroke="#b98d60" stroke-width="1" opacity=".5"/>' for i in range(int(W / 9) - 1))
        if hd == "twist":
            out += f'<path d="M{x + W * .3} {y + 6} C{x + W * .3} {y - 60}, {x + W * .7} {y - 60}, {x + W * .7} {y + 6}" stroke="{KD7}" stroke-width="7" fill="none" stroke-dasharray="5 2"/>'
        elif hd == "flat":
            out += f'<path d="M{x + W * .28} {y + 4} V{y - 34} H{x + W * .72} V{y + 4}" stroke="{KD7}" stroke-width="10" fill="none"/>'
        if k in ("L", "XL"):
            out += f'<circle cx="{x + W / 2}" cy="{y + H * .52}" r="{W * .2:.0f}" fill="none" stroke="{GN7}" stroke-width="5"/><text x="{x + W / 2}" y="{y + H * .52 + 7}" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="20" fill="{GN7}"><tspan>logo</tspan></text>'
        out += f'<rect x="{x + W / 2 - 34}" y="{base - 52}" width="68" height="34" rx="8" fill="{PW7}"/><text x="{x + W / 2}" y="{base - 28}" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="20" fill="{INK7}"><tspan>{k}</tspan></text>'
        out += f'<text x="{x + W / 2 + G / 2}" y="{base + 34}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="{INK7}"><tspan>{w} × {h} × {g} in</tspan></text><text x="{x + W / 2 + G / 2}" y="{base + 56}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="15" fill="#6d5a44"><tspan>{HN7[hd]}</tspan></text>'
        x += W + G + 46
    return f'<svg viewBox="0 66 {x - 26} 330" style="display:block;height:290px;width:auto;margin:0 auto">{out}</svg>'
def flat7(k):
    w, h, g, _ = SZ7[k]; S = 11; sw, sh = sheet7(k)
    xs = [(1, "Glue"), (w, "Front"), (g, "Gusset"), (w, "Back"), (g, "Gusset")]
    out = ""; x = 10; cols = ["#d9b98f", KR7, "#b8895a", KR7, "#b8895a"]
    for (u, lab), c in zip(xs, cols):
        out += f'<rect x="{x}" y="10" width="{u * S}" height="{sh * S}" fill="{c}" stroke="{INK7}" stroke-width="1.5" stroke-dasharray="{"5 4" if lab != "Front" else "0"}"/>'
        if u >= 3: out += f'<text x="{x + u * S / 2}" y="{10 + h * S / 2}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="16" fill="{INK7}"><tspan>{lab if u > 5 else "G"}</tspan></text><text x="{x + u * S / 2}" y="{30 + h * S / 2}" text-anchor="middle" font-family="Inter" font-weight="500" font-size="14" fill="{INK7}"><tspan>{u} in</tspan></text>'
        x += u * S
    out += f'<path d="M10 {10 + (h + 1.5) * S} H{x}" stroke="{GN7}" stroke-width="2" stroke-dasharray="8 5"/><path d="M10 {10 + 1.5 * S} H{x}" stroke="{GN7}" stroke-width="2" stroke-dasharray="8 5"/>'
    return f'<svg viewBox="0 0 {x + 10} {sh * S + 20}" style="display:block;width:100%;height:auto">{out}</svg>', sw, sh
FL7, SW7, SH7 = flat7("L")
P["p427_paperbag"] = page(f"""
body{{--f:'Inter';--h:'Bitter';background:{BG7};color:{INK7}}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{GN7};margin-top:22px}}
h1{{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1px;margin-top:16px}} h1 span{{color:{GN7}}}
.w7{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm7{{font:700 13px/1.4 Inter;letter-spacing:2px;color:#7a6650}}
.cd7{{background:{PW7};border-radius:24px;box-shadow:0 14px 30px rgba(60,40,20,.10);padding:18px 22px;display:flex;flex-direction:column;gap:10px}}
.bt7{{flex:1;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:16px;min-height:0}}
.fl7 p{{font:600 18px/1.4 Inter}}.fl7 .eq{{margin-top:auto;background:#e4efe8;border-radius:14px;padding:12px 16px;display:flex;justify-content:space-between;align-items:baseline;gap:10px}}.fl7 .eq span{{font:600 16px/1.3 Inter;color:{GN7}}}.fl7 .eq b{{font:800 28px/1.3 Bitter;color:{GN7}}}
.fl7 .lg{{display:flex;align-items:center;gap:10px;font:600 15px/1.3 Inter;color:#6d5a44}}.fl7 .lg i{{width:30px;border-top:2px dashed {GN7}}}
.od7 .r{{flex:1;display:grid;grid-template-columns:1fr 46px 76px 64px;gap:8px;align-items:center;border-top:1px solid #e6dccb}}.od7 .r b{{font:700 17px/1.3 Inter}}.od7 .r u{{text-decoration:none;font:800 16px/1 Bitter;background:{KR7};color:#fff;border-radius:8px;padding:6px 0;text-align:center}}.od7 .r strong{{font:700 18px/1.3 Inter;text-align:right}}.od7 .r em{{font:700 13px/1.2 Inter;font-style:normal;text-align:center;border-radius:8px;padding:6px 4px;background:#efe6d8;color:#6d5a44}}.od7 .r em.pr{{background:#dcebe2;color:{GN7}}}
.dk7{{background:{GN7};color:#fff;border-radius:16px;padding:12px 16px;display:grid;grid-template-columns:repeat(4,1fr);gap:8px}}.dk7 div{{display:flex;flex-direction:column}}.dk7 span{{font:700 13px/1.3 Inter;letter-spacing:1px;color:#bfe0cd}}.dk7 b{{font:800 24px/1.3 Bitter}}
""", "<div class=kk>PAPER BAG MAKER · SHOP ORDERS</div><h1>Bag orders in chats?<br><span>Size, print and count, sorted.</span></h1>",
f'''<div class=w7><div class=cd7><span class=sm7>YOUR 4 SIZES · DRAWN TO SCALE · SAMPLE</span>{bags7()}</div>
<div class=bt7><div class="cd7 fl7"><span class=sm7>SIZE L · FLAT SHEET BEFORE FOLDING</span>{FL7}<div class=lg><i></i>Fold lines · G = gusset (side panel)</div><p>Width: 2 × front + 2 × gusset + 1 in glue.<br>Length: height + base fold + top fold.<br><span style="color:#7a6650;font-weight:500">Your own sample rule.</span></p><div class=eq><span>One L sheet</span><b>{SW7:g} × {SH7:g} in</b></div><div class=eq style="margin-top:0;background:#efe3cf"><span style="color:#6d4c2a">L sheets to cut this week</span><b style="color:#6d4c2a">{fmt7(TOT7["L"])}</b></div></div>
<div class="cd7 od7"><span class=sm7>ORDERS · 23 TO 28 NOV · PRINT = 1-COLOUR LOGO</span>{"".join(f'<div class=r><b>{s}</b><u>{k}</u><strong>{fmt7(n)}</strong><em class="{"pr" if "print" in p else ""}">{p}</em></div>' for s, k, n, p in OR7)}
<div class=dk7>{"".join(f'<div><span>{k} BAGS</span><b>{fmt7(TOT7[k])}</b></div>' for k in SZ7)}</div></div></div></div>''',
INK7, "Make paper bags? DM us", f"background:{GN7};color:#fff")
