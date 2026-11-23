
# ───────── 447 USA · Cabinet refacing · SINGLE · Gelasio + Roboto · olive shaker / white oak / cream
# New technique: to-scale kitchen elevation where every door and drawer front is drawn from its inches and labelled, and the
# door order list is grouped by size from the same pieces; style picker as three mini SVG doors.
OL7 = "#5b6b3a"; OK7 = "#d9bf8f"; CR7 = "#f6f1e6"; INK7 = "#2a2a22"; MU7 = "#6e6a5c"
SC7 = 6; X07 = 20
UP7 = [("U1", 15), ("U2", 15), ("U3", 18), ("U4", 18), ("U5", 15), ("U6", 15)]
BASE7 = [("B1", 15, [("D", 6), ("Door", 24)]), ("B2", 18, [("Door", 30)]), ("B3", 18, [("Door", 30)]), ("B4", 15, [("D", 6), ("Door", 24)]),
         ("B5", 18, [("D", 6), ("D", 9), ("D", 15)]), ("B6", 12, [("Door", 30)])]
assert sum(w for _, w in UP7) == sum(b[1] for b in BASE7)
PCS7 = []
def elev7():
    s = ""; x = X07; y0 = 20
    for c, w in UP7:
        PCS7.append(("Door", w, 30))
        s += f'<rect x="{x}" y="{y0}" width="{w * SC7}" height="{30 * SC7}" fill="{OL7}" stroke="{CR7}" stroke-width="3"/><rect x="{x + 14}" y="{y0 + 14}" width="{w * SC7 - 28}" height="{30 * SC7 - 28}" fill="none" stroke="#7d8d58" stroke-width="3"/>'
        s += f'<text x="{x + w * SC7 / 2}" y="{y0 + 82}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="17" fill="#fff"><tspan>{c}</tspan></text><text x="{x + w * SC7 / 2}" y="{y0 + 106}" text-anchor="middle" font-family="Roboto" font-weight="500" font-size="14" fill="#e8ecd9"><tspan>{w}×30</tspan></text>'
        x += w * SC7
    yb = y0 + 30 * SC7 + 70
    s += f'<rect x="{X07 - 6}" y="{yb - 14}" width="{96 * SC7 + 12}" height="14" fill="{OK7}"/>'
    x = X07
    for c, w, parts in BASE7:
        y = yb
        for i, (k, h) in enumerate(parts):
            PCS7.append(("Drawer" if k == "D" else "Door", w, h))
            s += f'<rect x="{x}" y="{y}" width="{w * SC7}" height="{h * SC7}" fill="{OL7}" stroke="{CR7}" stroke-width="3"/>'
            if h >= 15:
                s += f'<rect x="{x + 12}" y="{y + 12}" width="{w * SC7 - 24}" height="{h * SC7 - 24}" fill="none" stroke="#7d8d58" stroke-width="3"/>'
            lab = f"{c}" if i == len(parts) - 1 or len(parts) == 1 else ""
            if h >= 15:
                s += f'<text x="{x + w * SC7 / 2}" y="{y + h * SC7 / 2 - 4}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="17" fill="#fff"><tspan>{c}</tspan></text><text x="{x + w * SC7 / 2}" y="{y + h * SC7 / 2 + 18}" text-anchor="middle" font-family="Roboto" font-weight="500" font-size="14" fill="#e8ecd9"><tspan>{w}×{h}</tspan></text>'
            else:
                s += f'<rect x="{x + w * SC7 / 2 - 16}" y="{y + h * SC7 / 2 - 3}" width="32" height="6" rx="3" fill="{OK7}"/>'
            y += h * SC7
        x += w * SC7
    s += f'<rect x="{X07}" y="{yb + 30 * SC7}" width="{96 * SC7}" height="16" fill="#3d3a30"/>'
    W = 96 * SC7 + 2 * X07; H = yb + 30 * SC7 + 16 + 10
    return f'<svg viewBox="0 0 {W} {H}" style="position:absolute;inset:0;width:100%;height:100%"><rect x="{X07}" y="{y0 + 30 * SC7}" width="{96 * SC7}" height="56" fill="#ece5d6"/>{s}</svg>'
EL7 = elev7()
from collections import Counter
GR7 = sorted(Counter(PCS7).items(), key=lambda t: (t[0][0], -t[0][2], -t[0][1]))
NDOOR7 = sum(v for (k, _, _), v in GR7 if k == "Door"); NDRW7 = sum(v for (k, _, _), v in GR7 if k == "Drawer")
def door7(kind, on):
    inner = {"Shaker": f'<rect x="12" y="12" width="46" height="76" fill="none" stroke="#7d8d58" stroke-width="5"/>', "Slab": "",
             "Raised": f'<rect x="12" y="12" width="46" height="76" fill="none" stroke="#7d8d58" stroke-width="3"/><path d="M20 20 H50 V80 H20 Z" fill="#6c7d45"/>'}[kind]
    return f'<div class="st{" on" if on else ""}"><svg viewBox="0 0 70 100" style="width:76px;height:auto;display:block"><rect width="70" height="100" fill="{OL7}"/>{inner}</svg><b>{kind}</b></div>'
P["p447_cab"] = page(f"""
body{{--f:'Roboto';--h:'Gelasio';background:{CR7};color:{INK7};font-variant-numeric:lining-nums}}
.kk7{{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:{OL7};margin-top:22px}}
h1{{font-family:'Gelasio';font-weight:700;font-size:52px;line-height:1.22;letter-spacing:-.5px;margin-top:12px}} h1 span{{color:{OL7}}}
.w7{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm7{{font:700 13px/1.4 'Roboto';letter-spacing:2px;color:{MU7}}}
.cd7{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(42,42,34,.08)}}
.tp7{{flex:none;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr);gap:16px}}.el7{{min-height:0;padding:16px 18px;display:flex;flex-direction:column;gap:10px}}.el7 .im{{position:relative;aspect-ratio:616/476}}.el7 .hd{{display:flex;flex-direction:column;align-items:flex-start;gap:8px}}.el7 .hd b{{font:700 15px/1.3 'Roboto';background:#eef0e4;color:{OL7};border-radius:8px;padding:5px 10px}}
.bt7{{display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:16px;flex:1;min-height:0}}.or7 .r{{flex:1}}
.or7{{padding:16px 20px;display:flex;flex-direction:column;gap:4px}}.or7 .r{{display:grid;grid-template-columns:80px 1fr auto;gap:10px;align-items:center;border-top:1px solid #efeadf;padding:6px 0}}.or7 .r span{{font:600 15px/1.3 'Roboto';color:{MU7}}}.or7 .r b{{font:700 19px/1.3 'Roboto'}}.or7 .r strong{{font:700 22px/1.3 Gelasio;color:{OL7}}}
.or7 .tt{{margin-top:6px;background:{OL7};color:#fff;border-radius:12px;padding:9px 14px;font:700 17px/1.35 'Roboto'}}
.rc7{{display:flex;flex-direction:column;gap:16px}}.sy7{{padding:16px 20px;display:flex;flex-direction:column;gap:10px;justify-content:space-between}}.sy7 .g{{display:flex;gap:10px}}.sy7 .st{{flex:1;border:2px solid #e6e0d2;border-radius:12px;padding:10px;display:flex;flex-direction:column;align-items:center;gap:6px}}.sy7 .st.on{{border-color:{OL7};background:#f1f3e8}}.sy7 .st b{{font:700 18px/1.3 'Roboto'}}
.sy7 .sw{{display:flex;gap:8px}}.sy7 .sw span{{flex:1;display:flex;align-items:center;gap:6px;font:600 17px/1.3 'Roboto'}}.sy7 .sw i{{width:22px;height:22px;border-radius:6px;flex:none;border:1px solid #0002}}
.js7{{background:{INK7};color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;justify-content:space-between}}.js7 .sm7{{color:#bdb8a6}}.js7 .r{{display:flex;flex-direction:column;gap:2px;font:500 16px/1.4 'Roboto';color:#bdb8a6;border-top:1px solid #45443a;padding-top:8px}}.js7 .r b{{font:700 21px/1.35 'Roboto';color:#fff}}
""", "<div class=kk7>CABINET REFACING</div><h1>Doors ordered from a tape list?<br><span>Size every door on one drawing.</span></h1>",
f'''<div class=w7><div class=tp7><div class="cd7 el7"><div class=hd><span class=sm7>SAMPLE KITCHEN · 96 IN WALL · DRAWN TO SCALE</span><b>{NDOOR7} doors · {NDRW7} drawer fronts</b></div><div class=im>{EL7}</div></div>
<div class="cd7 or7"><span class=sm7>DOOR ORDER · GROUPED BY SIZE</span>{"".join(f'<div class=r><span>{k}</span><b>{w}" × {h}"</b><strong>× {v}</strong></div>' for (k, w, h), v in GR7)}<div class=tt>{NDOOR7 + NDRW7} pieces, every size checked on the drawing</div></div></div>
<div class=bt7><div class="cd7 sy7"><span class=sm7>STYLE AND FINISH · PICKED BY THE HOMEOWNER</span><div class=g>{door7("Shaker", True)}{door7("Slab", False)}{door7("Raised", False)}</div><div class=sw>{"".join(f'<span><i style="background:{c}"></i>{n}</span>' for c, n in [(OL7, "Olive"), ("#f4f1ea", "White"), (OK7, "Oak")])}</div></div>
<div class=js7><span class=sm7>JOB · SAMPLE HOMEOWNER</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Measured", "Mon 23 Nov"), ("Quote sent", "Tue 24 Nov"), ("Install", "When the doors arrive")])}</div></div></div>''',
INK7, "Do cabinet refacing? DM us", f"background:{OL7};color:#fff")
