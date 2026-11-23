# ───────── 454 INDIA · Terracotta pot maker (kiln load + firing) · SINGLE · Bitter + Source Sans 3 · clay orange / kiln charcoal / ash cream
# New technique: kiln cross-section SVG (brick pattern walls, firebox flames, three shelves of drawn pot profiles in front
# and back rows) driven by the layer plan; firing curve polyline with the "now" temperature interpolated from the same points.
CL4 = "#c8643b"; CH4 = "#2b2523"; AS4 = "#f4ece2"; MU4 = "#76675e"; FL4 = "#f2a33a"
LY4 = [("Top shelf", "Kulhad cups", 160, [("Sample Tea Stall", 120)], "cup"),
       ("Middle shelf", "Planters, 6 in", 60, [("Sample Home Store", 30), ("Sample Garden Shop", 20)], "mid"),
       ("Bottom shelf", "Planters, 10 in", 44, [("Sample Nursery A", 40)], "big")]
CV4 = [(0, 30), (2, 150), (4, 300), (6, 600), (8, 850), (9, 900), (10, 900), (11, 700), (14, 300)]
NOWH4 = 6.5
def tempat4(h):
    for (a, ta), (b, tb) in zip(CV4, CV4[1:]):
        if a <= h <= b: return ta + (tb - ta) * (h - a) / (b - a)
NOWT4 = tempat4(NOWH4)
def potpath4(x, y, w, h, kind, fill, op=1):
    if kind == "cup":
        return f'<path d="M{x - w / 2:.1f} {y - h:.1f} L{x + w / 2:.1f} {y - h:.1f} L{x + w * .32:.1f} {y:.1f} L{x - w * .32:.1f} {y:.1f} Z" fill="{fill}" opacity="{op}"/>'
    r = h * .14
    return (f'<path d="M{x - w * .36:.1f} {y:.1f} L{x - w * .46:.1f} {y - h + r:.1f} L{x + w * .46:.1f} {y - h + r:.1f} L{x + w * .36:.1f} {y:.1f} Z" fill="{fill}" opacity="{op}"/>'
            f'<rect x="{x - w / 2:.1f}" y="{y - h:.1f}" width="{w:.1f}" height="{r:.1f}" rx="2" fill="{fill}" opacity="{op}"/>'
            f'<rect x="{x - w / 2:.1f}" y="{y - h + r:.1f}" width="{w:.1f}" height="2.5" fill="#00000030" opacity="{op}"/>')
def kiln4():
    o = ['<defs><pattern id="br4" width="28" height="14" patternUnits="userSpaceOnUse"><rect width="28" height="14" fill="#a5523a"/><path d="M0 0.5H28M0 7.5H28M14 0V7M0 7V14M28 7V14" stroke="#e9d3c4" stroke-width="1.4"/></pattern></defs>']
    o.append('<rect x="44" y="80" width="312" height="22" rx="6" fill="url(#br4)"/><rect x="186" y="18" width="28" height="64" fill="url(#br4)"/>')
    o.append('<path d="M20 102 H380 V500 H20 Z" fill="url(#br4)"/><rect x="48" y="112" width="304" height="322" fill="#3a302c"/>')
    # shelves bottom up
    ys = {"big": (426, 84, 5, 1), "mid": (326, 68, 7, 1), "cup": (236, 42, 10, 2)}
    for _, _, _, _, k in LY4:
        yb, h, n, stack = ys[k]
        o.append(f'<rect x="48" y="{yb:.0f}" width="304" height="7" fill="#8b7b6f"/>')
        step = 296 / n
        for sk in range(stack):
            y0 = yb - sk * (h + 4)
            for i in range(n - 1):   # back row, offset half a step
                o.append(potpath4(52 + step * (i + 1), y0 - 7, step * .74, h * .9, k, "#9c5a40"))
            for i in range(n):
                o.append(potpath4(52 + step * (i + .5), y0, step * .8, h, k, CL4))
    o.append('<rect x="48" y="434" width="304" height="50" fill="#1f1917"/>')
    for i in range(7):
        x = 72 + i * 42
        o.append(f'<path d="M{x - 15} 484 Q{x - 6} 452 {x} 440 Q{x + 6} 452 {x + 15} 484 Z" fill="{FL4}"/><path d="M{x - 7} 484 Q{x - 2} 466 {x} 458 Q{x + 3} 466 {x + 7} 484 Z" fill="#ffe08a"/>')
    return f'<svg viewBox="10 10 380 500" preserveAspectRatio="xMidYMid meet">{"".join(o)}</svg>'
def curve4(W=860, H=150):
    sx = lambda h: h / 14 * W; sy = lambda t: H - t / 1000 * H
    pts = " ".join(f"{sx(h):.1f},{sy(t):.1f}" for h, t in CV4)
    done = " ".join(f"{sx(h):.1f},{sy(t):.1f}" for h, t in CV4 if h <= NOWH4) + f" {sx(NOWH4):.1f},{sy(NOWT4):.1f}"
    area = f"0,{H} " + done + f" {sx(NOWH4):.1f},{H}"
    grid = "".join(f'<line x1="0" x2="{W}" y1="{sy(t):.1f}" y2="{sy(t):.1f}" stroke="#ead9c9" stroke-width="1"/>' for t in (250, 500, 750))
    return f'''<svg viewBox="0 0 {W} {H}" preserveAspectRatio="none">{grid}<polygon points="{area}" fill="{FL4}" opacity=".25"/><polyline points="{pts}" fill="none" stroke="#c9b7a6" stroke-width="3" stroke-dasharray="8 6"/><polyline points="{done}" fill="none" stroke="{CL4}" stroke-width="4" stroke-linejoin="round"/><line x1="{sx(NOWH4):.1f}" x2="{sx(NOWH4):.1f}" y1="0" y2="{H}" stroke="{CH4}" stroke-width="2"/><circle cx="{sx(NOWH4):.1f}" cy="{sy(NOWT4):.1f}" r="7" fill="{CH4}"/></svg>'''
def lay4(nm, what, cap, ords, k):
    n = sum(q for _, q in ords)
    return f'''<div class="cd4 ly"><div class=hd><div><span class=sm4>{nm.upper()}</span><b>{what}</b></div><strong>{n}<small> / {cap}</small></strong></div><div class=br><i style="width:{n / cap * 100:.0f}%"></i></div>
{"".join(f'<div class=o><span>{w}</span><b>{q}</b></div>' for w, q in ords)}<div class=fr>Room for {cap - n} more</div></div>'''
P["p454_clay"] = page(f"""
body{{--f:'Source Sans 3';--h:'Bitter';background:{AS4};color:{CH4}}}
.kk4{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{CL4};margin-top:22px}}
h1{{font-family:'Bitter';font-weight:800;font-size:56px;line-height:1.2;letter-spacing:-1px;margin-top:12px}} h1 span{{color:{CL4}}}
.w4{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm4{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:{MU4}}}
.cd4{{background:#fffaf4;border-radius:22px;box-shadow:0 14px 30px rgba(43,37,35,.08)}}
.tp4{{flex:1;display:grid;grid-template-columns:minmax(0,.95fr) minmax(0,1.05fr);gap:16px;min-height:0}}
.kc{{background:{CH4};border-radius:22px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;min-height:0}}.kc .sm4{{color:#bba99c}}.kc .sv{{flex:1;position:relative;min-height:0}}.kc .sv svg{{position:absolute;inset:0;width:100%;height:100%}}
.kc .ft4{{display:flex;justify-content:space-between;font:600 16px/1.3 'Source Sans 3';color:#e8d9cc}}
.ls4{{display:flex;flex-direction:column;gap:12px;min-height:0}}
.ly{{flex:1;padding:12px 18px;display:flex;flex-direction:column;gap:6px;justify-content:center}}.ly .hd{{display:flex;justify-content:space-between;align-items:center;gap:8px}}.ly .hd b{{display:block;font:700 21px/1.3 Bitter}}.ly .hd strong{{font:800 30px/1.3 Bitter;color:{CL4}}}.ly .hd small{{font:600 17px/1.3 'Source Sans 3';color:{MU4}}}
.ly .br{{height:10px;border-radius:6px;background:#efe2d4;overflow:hidden}}.ly .br i{{display:block;height:100%;background:{CL4};border-radius:6px}}
.ly .o{{display:flex;justify-content:space-between;font:500 18px/1.3 'Source Sans 3'}}.ly .o b{{font-weight:700}}.ly .fr{{font:700 15px/1.3 'Source Sans 3';color:#4f7a39}}
.fc{{flex:none;padding:16px 22px 14px;display:flex;flex-direction:column;gap:8px}}.fc .hd{{display:flex;justify-content:space-between;align-items:baseline;gap:10px}}.fc .hd b{{display:block;font:700 20px/1.3 Bitter;margin-top:2px}}.fc .now{{background:{CH4};color:#fff;border-radius:10px;padding:6px 12px;font:700 17px/1.3 'Source Sans 3';white-space:nowrap}}
.ch{{display:grid;grid-template-columns:54px minmax(0,1fr);gap:8px}}.yx{{display:flex;flex-direction:column;justify-content:space-between;font:600 13px/1.3 'Source Sans 3';color:{MU4};text-align:right;height:150px}}.cv{{height:150px;position:relative}}.cv svg{{position:absolute;inset:0;width:100%;height:100%}}
.xx{{display:flex;justify-content:space-between;margin-left:62px;font:600 13px/1.3 'Source Sans 3';color:{MU4}}}
""", "<div class=kk4>TERRACOTTA POTS · KILN PLAN</div><h1>Kiln loaded by guesswork?<br><span>Plan every pot before firing.</span></h1>",
f'''<div class=w4><div class=tp4><div class=kc><span class=sm4>KILN 1 · FIRING #27 · SAMPLE</span><div class=sv>{kiln4()}</div><div class=ft4><span>{sum(q for l in LY4 for _, q in l[3])} pots loaded</span><span>{sum(l[2] for l in LY4)} fit in all</span></div></div>
<div class=ls4>{"".join(lay4(*l) for l in LY4)}</div></div>
<div class="cd4 fc"><div class=hd><div><span class=sm4>FIRING · LIT MON 23 NOV, 6 AM · UNLOAD TUE 24 NOV, 8 AM</span><b>Slow warm-up, full fire, then cool down</b></div><span class=now>Now {NOWT4:.0f} °C · 12:30 PM</span></div>
<div class=ch><div class=yx><span>1000 °C</span><span>500 °C</span><span>0 °C</span></div><div class=cv>{curve4()}</div></div><div class=xx>{"".join(f"<span>{h} h</span>" for h in (0, 2, 4, 6, 8, 10, 12, 14))}</div></div></div>''',
CH4, "Make terracotta pots? DM us", f"background:{CL4};color:#fff")
