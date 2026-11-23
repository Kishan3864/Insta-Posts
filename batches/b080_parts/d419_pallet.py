
# ───────── 419 INDIA · Wooden pallet maker · SINGLE · Montserrat + Roboto · pine yellow / stamp black / factory blue
# New technique: isometric SVG pallet built from real part sizes (bottom boards, 9 blocks, stringers, 7 top boards) with
# an iso() projection and painter's order; the phone order form carries the same size, entry, wood and count.
PY9 = "#e7c27d"; K9 = "#1b1b1b"; BL9 = "#2457a6"; BG9 = "#f4efe4"
def iso9(x, y, z, s=.27, ox=290, oy=50):
    return (ox + (x - y) * .866 * s, oy + (x + y) * .5 * s - z * s)
def box9(x0, y0, z0, x1, y1, z1, tone=0):
    cs = [("#ecc98c", "#cfa565", "#b88d50"), ("#dcb274", "#bf9255", "#a87c43")][tone]
    def poly(pts, c): return '<polygon points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in (iso9(*p) for p in pts)) + f'" fill="{c}" stroke="#8a6534" stroke-width="1"/>'
    return (poly([(x0, y0, z1), (x1, y0, z1), (x1, y1, z1), (x0, y1, z1)], cs[0]) + poly([(x0, y1, z0), (x1, y1, z0), (x1, y1, z1), (x0, y1, z1)], cs[1]) + poly([(x1, y0, z0), (x1, y1, z0), (x1, y1, z1), (x1, y0, z1)], cs[2]))
def pallet9():
    L, Wd = 1200, 1000; parts = []
    for yb in (0, 450, 900): parts.append((0, 0, yb, 0, L, yb + 100, 22, 0))
    for xb in (0, 550, 1100):
        for yb in (0, 450, 900): parts.append((1, xb, yb, 22, xb + 100, yb + 100, 100, 1))
    for xb in (0, 550, 1100): parts.append((2, xb, 0, 100, xb + 100, Wd, 122, 0))
    for k in range(7): parts.append((3, 0, k * 150, 122, L, k * 150 + 100, 144, 0))
    parts.sort(key=lambda p: (p[0], p[1] + p[2]))
    body = "".join(box9(x0, y0, z0, x1, y1, z1, t) for _, x0, y0, z0, x1, y1, z1, t in parts)
    a = iso9(1200, 1000, 0); b = iso9(0, 1000, 0)
    return f'''<svg viewBox="0 0 600 400" width="600" style="display:block;width:100%;height:auto">{body}
<text x="110" y="318" font-family="Montserrat" font-weight="800" font-size="20" fill="{BL9}"><tspan>1000 mm</tspan></text>
<text x="{a[0] + 120:.0f}" y="{a[1] - 30:.0f}" font-family="Montserrat" font-weight="800" font-size="20" fill="{BL9}"><tspan>1200 mm</tspan></text></svg>'''
YD9 = [("PL-55", "Sample Auto Parts", 120, 120, "Ready"), ("PL-56", "Sample Foods", 48, 80, "Nailing"), ("PL-57", "Sample Textiles", 0, 50, "Wood cut"), ("PL-58", "Sample Engineering", 0, 100, "New")]
PH9 = f'''<div class=pp9><div class=h9>New pallet order</div><div class=cl9>Sample Engineering · PL-58</div>
{"".join(f'<div class=f9><span>{a}</span><div class=ch9>{"".join(f"<i class={chr(34)}on{chr(34)}>{o[1:]}</i>" if o.startswith("*") else f"<i>{o}</i>" for o in opts)}</div></div>' for a, opts in [("Size (mm)", ["*1200×1000", "1200×800", "Custom"]), ("Entry", ["2-way", "*4-way"]), ("Wood", ["*Pine", "Hardwood"]), ("Heat treated stamp", ["*Yes", "No"])])}
<div class=f9 style="flex-direction:row;justify-content:space-between;align-items:center"><span>Quantity</span><div class=st9><i>−</i><b>100</b><i>+</i></div></div>
<div class=g9><div><span>Load / pallet</span><b>1,000 kg</b></div><div><span>Deliver by</span><b>Thu 3 Dec</b></div></div>
<div class=g9><div style="grid-column:1/3"><span>Unload at</span><b>Gate 3 · loading dock</b></div></div><div class=g9><div style="grid-column:1/3"><span>Note to maker</span><b>Stack in 10s, strapped, label each stack</b></div></div><div class=bt9>Send order</div></div>'''
P["p419_pallet"] = page(f"""
body{{--f:'Roboto';--h:'Montserrat';background:{BG9};color:{K9}}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{BL9};margin-top:22px}}
h1{{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1.5px;margin-top:20px}} h1 span{{color:{BL9}}}
.vw9{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 330px;gap:20px;min-height:0}}
.lf9{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm9{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#776d5b}}
.cd9{{background:#fffdf7;border-radius:24px;box-shadow:0 14px 30px rgba(50,40,10,.09);padding:16px 20px;display:flex;flex-direction:column;gap:8px}}
.dr9 .tg9{{display:flex;gap:8px;flex-wrap:wrap}}.dr9 .tg9 span{{font:700 15px/1.2 Roboto;border-radius:10px;padding:8px 11px;background:#e2eaf6;color:{BL9}}}.dr9 .tg9 span.ht{{background:{K9};color:{PY9};letter-spacing:1px}}
.yd9{{flex:1;min-height:0}}.yd9 .r{{flex:1;display:grid;grid-template-columns:70px 1fr 104px;grid-template-rows:auto auto;gap:4px 12px;align-items:center;border-top:1px solid #eee5d2;padding:6px 0}}
.yd9 .r b{{font:800 18px/1.3 Montserrat}}.yd9 .r .nm{{font:600 17px/1.3 Roboto}}.yd9 .r em{{grid-row:1/3;grid-column:3;font:700 14px/1.2 Roboto;font-style:normal;text-align:center;border-radius:10px;padding:8px 6px;background:#efe6d2;color:#776d5b}}.yd9 .r em.rd{{background:#dde9d6;color:#2d6a2a}}.yd9 .r em.nw{{background:{BL9};color:#fff}}
.yd9 .bar{{grid-column:1/3;display:flex;align-items:center;gap:10px}}.yd9 .bar div{{flex:1;height:12px;border-radius:6px;background:#efe6d2;overflow:hidden}}.yd9 .bar i{{display:block;height:100%;background:{PY9}}}.yd9 .bar span{{font:600 15px/1.2 Roboto;color:#776d5b;width:70px;text-align:right}}
.ph9{{display:flex;align-items:center}}
.pp9{{flex:1;display:flex;flex-direction:column;gap:10px;padding:8px 16px 18px;background:#fffdf7}}.h9{{font:800 19px/1.3 Montserrat}}.cl9{{font:600 14px/1.3 Roboto;color:#776d5b;margin-top:-6px}}
.f9{{display:flex;flex-direction:column;gap:6px}}.f9>span,.g9 span{{font:700 12px/1.3 Roboto;letter-spacing:1px;color:#776d5b;text-transform:uppercase}}
.ch9{{display:flex;gap:6px}}.ch9 i{{flex:1;font:700 14px/1.2 Roboto;font-style:normal;text-align:center;border:1.5px solid #e3d9c4;border-radius:10px;padding:9px 4px;background:#fff}}.ch9 i.on{{background:{BL9};border-color:{BL9};color:#fff}}
.st9{{display:flex;align-items:center;gap:8px}}.st9 i{{width:30px;height:30px;border-radius:9px;background:{K9};color:#fff;font:800 18px/30px Montserrat;font-style:normal;text-align:center}}.st9 b{{font:800 20px/1.2 Montserrat;width:50px;text-align:center}}
.g9{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}.g9 div{{background:#fff;border:1.5px solid #e3d9c4;border-radius:12px;padding:8px 10px;display:flex;flex-direction:column;gap:3px}}.g9 b{{font:700 15px/1.3 Roboto}}
.bt9{{margin-top:auto;background:{K9};color:{PY9};border-radius:14px;padding:13px;text-align:center;font:800 16px/1.2 Montserrat}}
""", "<div class=kk>WOODEN PALLET MAKER · FACTORY ORDERS</div><h1>Pallet orders by phone call?<br><span>Buyers fill one order form.</span></h1>",
f'''<div class=vw9><div class=lf9><div class="cd9 dr9"><span class=sm9>PL-58 · DRAWN FROM THE ORDER · SAMPLE</span>{pallet9()}<div class=tg9><span>1200 × 1000 mm</span><span>4-way entry</span><span>Pine</span><span>Load 1,000 kg</span><span class=ht>HT STAMP</span></div></div>
<div class="cd9 yd9"><span class=sm9>IN THE YARD TODAY</span>{"".join(f'<div class=r><b>{o}</b><span class=nm>{n}</span><em class="{ {"Ready": "rd", "New": "nw"}.get(s, "") }">{s}</em><div class=bar><div><i style="width:{m / t * 100:.0f}%"></i></div><span>{m} / {t}</span></div></div>' for o, n, m, t, s in YD9)}</div></div>
<div class=ph9>{phone(PH9, w=330, h=760)}</div></div>''',
K9, "Make pallets? DM us", f"background:{BL9};color:#fff")
