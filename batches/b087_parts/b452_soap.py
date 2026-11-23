# ───────── 452 INDIA · Handmade soap maker (curing rack) · CAROUSEL 5 · Lora + Inter · oat cream / lavender / olive
# New technique: oblique-projection curing rack drawn from real sizes (bays 60 x 40 cm, bars 8 x 5.5 x 3 cm), every bar
# a 3-face prism coloured by batch; one batch list drives rack, cure calendar (gantt with today line) and order allocation.
import datetime as _dt2
OAT2 = "#f3ecdf"; INK2 = "#2e2a3a"; LAV2 = "#7b62b0"; OLV2 = "#6f7d3a"; MU2 = "#6d6878"
TODAY2 = _dt2.date(2026, 11, 23)
BT2 = [  # code, soap, colour, made, bars, sold
    ("B-31", "Lavender", "#a991d4", _dt2.date(2026, 10, 19), 36, 22),
    ("B-32", "Coffee", "#7a5236", _dt2.date(2026, 10, 26), 36, 0),
    ("B-33", "Rose clay", "#e3a3a6", _dt2.date(2026, 11, 2), 36, 0),
    ("B-34", "Charcoal", "#3d3b40", _dt2.date(2026, 11, 9), 36, 0),
    ("B-35", "Orange peel", "#ef9a3c", _dt2.date(2026, 11, 16), 36, 0),
    ("B-36", "Oatmeal", "#dccaa2", _dt2.date(2026, 11, 20), 24, 0)]
CURE2 = 28
def rdy2(b): return b[3] + _dt2.timedelta(days=CURE2)
def left2(b): return (rdy2(b) - TODAY2).days
def stock2(b): return b[4] - b[5]
def dfmt2(d): return d.strftime("%a %d %b").replace(" 0", " ")
def dshort2(d): return d.strftime("%d %b").lstrip("0")
# rack: shelf index 0 bottom..2 top, bay 0 left / 1 right
POS2 = {"B-31": (0, 0), "B-32": (0, 1), "B-33": (1, 0), "B-34": (1, 1), "B-35": (2, 0), "B-36": (2, 1)}
SHN2 = {0: "Bottom", 1: "Middle", 2: "Top"}
def where2(code): s, b = POS2[code]; return f'{SHN2[s]} shelf, {"left" if b == 0 else "right"}'
def shade2(hx, f):
    h = hx.lstrip("#"); r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return "#%02x%02x%02x" % tuple(max(0, min(255, int(c * f))) for c in (r, g, b))
def rack2(show=None, sc=3.6):
    K = 0.5 * 0.7071
    def pt(x, y, z): return (x + y * K, -(z + y * K))
    polys = []
    def poly(ps, fill, st="none", sw=0):
        polys.append(f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in (pt(*p) for p in ps))}" fill="{fill}" stroke="{st}" stroke-width="{sw}" stroke-linejoin="round"/>')
    def box(x, y, z, w, d, h, c, st="none", sw=0):
        poly([(x, y, z + h), (x + w, y, z + h), (x + w, y + d, z + h), (x, y + d, z + h)], shade2(c, 1.12), st, sw)   # top
        poly([(x + w, y, z), (x + w, y + d, z), (x + w, y + d, z + h), (x + w, y, z + h)], shade2(c, .78), st, sw)   # right
        poly([(x, y, z), (x + w, y, z), (x + w, y, z + h), (x, y, z + h)], c, st, sw)   # front
    W, D, H, BAY = 126, 40, 152, 60
    POST = "#8a7d66"; BOARD = "#c9b48e"
    for px in (0, 63, 123):   # back posts
        box(px, D - 3, 0, 3, 3, H, POST)
    for s, z in enumerate((4, 54, 104)):
        box(0, 0, z - 3, W, D, 3, BOARD)
        for bay in (0, 1):
            code = [c for c, p in POS2.items() if p == (s, bay)][0]
            b = [t for t in BT2 if t[0] == code][0]
            n = stock2(b); col = b[2]
            dim = show is not None and code not in show
            x0 = 3 + bay * 63 + 1.5
            cells = [(cx, cy) for cy in range(5, -1, -1) for cx in range(6)]
            filled = set()
            k = 0
            for cy in range(6):
                for cx in range(6):
                    if k < n: filled.add((cx, cy)); k += 1
            for cx, cy in cells:
                if (cx, cy) in filled:
                    box(x0 + cx * 9.6, 2 + cy * 6.2, z, 8, 5.4, 3, "#e6dfd2" if dim else col, "#00000022", .3)
        for px in (0, 63, 123):
            pass
    for px in (0, 63, 123):   # front posts last
        box(px, 0, 0, 3, 3, H, shade2(POST, .9))
    box(0, 0, H - 3, W, D, 3, BOARD)
    xs = []; ys = []
    import re as _re
    for p_ in polys:
        for a, b in _re.findall(r"(-?[\d.]+),(-?[\d.]+)", p_):
            xs.append(float(a)); ys.append(float(b))
    x0, y0, x1, y1 = min(xs) - 2, min(ys) - 2, max(xs) + 2, max(ys) + 2
    return f'<svg viewBox="{x0:.1f} {y0:.1f} {x1 - x0:.1f} {y1 - y0:.1f}" style="width:100%;height:100%;display:block">{"".join(polys)}</svg>'
B2 = f"""
body{{--f:'Inter';--h:'Lora';background:{OAT2};color:{INK2}}}
.kk2{{font:700 16px/1.4 'Inter';letter-spacing:3px;color:{OLV2};margin-top:22px;display:flex;gap:10px;align-items:center}}.kk2 i{{width:26px;height:16px;border-radius:5px;background:{LAV2}}}
h1{{font-family:'Lora';font-weight:700;font-size:58px;line-height:1.2;letter-spacing:-1px;margin-top:14px}} h1 span{{color:{LAV2};font-style:italic}}
.sm2{{font:700 13px/1.4 'Inter';letter-spacing:2px;color:{MU2}}}
.cd2{{background:#fffdf8;border-radius:24px;box-shadow:0 14px 30px rgba(46,42,58,.08)}}
.dk2{{background:{INK2};color:#fff;border-radius:24px}}.dk2 .sm2{{color:#b8b1c7}}
.sw2{{width:18px;height:18px;border-radius:5px;flex:none;display:inline-block}}
.ch2{{font:700 14px/1.3 'Inter';padding:5px 10px;border-radius:8px;white-space:nowrap}}.ch2.ok{{background:#e6eccf;color:#4b5a16}}.ch2.wt{{background:#ece6f6;color:#5a4590}}
"""
def bars2(items, w=22, h=14, cols=8):
    return f'<div class=bx2 style="grid-template-columns:repeat({cols},{w}px)">' + "".join(f'<i style="width:{w}px;height:{h}px;background:{c}"></i>' for c, q in items for _ in range(q)) + '</div>'
def t2(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{INK2};color:#fff"):
    return page(B2 + css, f"<div class=kk2><i></i>{kick}</div><h1>{head}</h1>", vis, INK2, cta, ctacss, tagline=f"{n} / 5")
def chip2(b):
    d = left2(b)
    return '<span class="ch2 ok">Ready now</span>' if d <= 0 else f'<span class="ch2 wt">{d} {"day" if d == 1 else "days"} left</span>'
# ── slide 1
P["p452_soap_s1"] = t2(1, "HANDMADE SOAP · CURING RACK", "Which soap is ready to sell?<br><span>Every tray shows its day.</span>",
f'''<div class=w21><div class="cd2 rk"><span class=sm2>SAMPLE CURING RACK · {len(BT2)} BATCHES · {sum(stock2(b) for b in BT2)} BARS</span><div class=sv>{rack2()}</div><div class=rn><span class=sm2>READY TO SELL NOW</span><b>{sum(stock2(b) for b in BT2 if left2(b) <= 0)} bars</b><em>{" + ".join(f"{stock2(b)} {b[1].lower()}" for b in BT2 if left2(b) <= 0)}</em></div></div>
<div class=ls>{"".join(f'<div class="cd2 tr"><div class=a><i class=sw2 style="background:{b[2]}"></i><b>{b[0]} · {b[1]}</b></div><div class=c><span>{where2(b[0])} · {stock2(b)} bars</span>{chip2(b)}</div><div class=br><i style="width:{min(100, (CURE2 - max(0, left2(b))) / CURE2 * 100):.0f}%;background:{b[2]}"></i></div></div>' for b in sorted(BT2, key=lambda b: rdy2(b)))}</div></div>''',
css=f""".w21{{flex:1;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.9fr);gap:16px;min-height:0}}
.rk{{padding:18px 20px;display:flex;flex-direction:column;gap:12px;min-height:0}}.rk .sv{{flex:1;min-height:0;position:relative}}.rk .sv svg{{position:absolute;inset:0}}.rn{{display:flex;align-items:baseline;gap:12px;background:#e6eccf;border-radius:14px;padding:12px 16px;flex-wrap:wrap}}.rn .sm2{{color:#4b5a16;width:100%}}.rn b{{font:700 30px/1.2 Lora;color:#4b5a16}}.rn em{{font:600 17px/1.3 Inter;font-style:normal;color:#4b5a16}}.rk .nt{{font:500 16px/1.35 'Inter';color:{MU2};text-align:center}}
.ls{{display:flex;flex-direction:column;gap:12px;min-height:0}}.tr{{flex:1;padding:12px 18px;display:flex;flex-direction:column;justify-content:center;gap:7px}}.tr .a{{display:flex;gap:10px;align-items:center}}.tr .a b{{font:700 21px/1.3 'Inter'}}
.tr .c{{display:flex;justify-content:space-between;align-items:center;gap:8px}}.tr .c span:first-child{{font:500 15px/1.3 'Inter';color:{MU2}}}.tr .br{{height:8px;border-radius:5px;background:#eee7da;overflow:hidden}}.tr .br i{{display:block;height:100%;border-radius:5px}}""")
# ── slide 2: batch card with scaled recipe
BASE2 = [("Coconut oil", 300), ("Olive oil", 400), ("Shea butter", 250), ("Castor oil", 50)]
NB2 = BT2[5]; F2 = NB2[4] / 36
P["p452_soap_s2"] = t2(2, "1 · BATCH CARD", "Make a half batch?<br><span>The recipe scales itself.</span>",
f'''<div class=w22><div class="cd2 bc"><div class=hd><div><span class=sm2>NEW BATCH · SAMPLE</span><b>{NB2[0]} · {NB2[1]}</b></div><i class=sw2 style="background:{NB2[2]};width:56px;height:56px;border-radius:14px"></i></div>
<div class=sc><div><span>Base recipe</span><b>36 bars</b></div><em>×&nbsp;{F2:.2f}</em><div class=on><span>This batch</span><b>{NB2[4]} bars</b></div></div>
<div class="r h"><span>OILS</span><span>BASE</span><span>THIS BATCH</span></div>{"".join(f'<div class=r><span>{a}</span><span>{g} g</span><b>{g * F2:.0f} g</b></div>' for a, g in BASE2)}
<div class="r t"><span>Total oils</span><span>{sum(g for _, g in BASE2)} g</span><b>{sum(g for _, g in BASE2) * F2:.0f} g</b></div></div>
<div class=sd><div class="dk2 dt">{"".join(f'<div><span class=sm2>{a}</span><b>{b}</b></div>' for a, b in [("MADE", dfmt2(NB2[3])), ("CURE", f"{CURE2} days"), ("READY", dfmt2(rdy2(NB2))), ("PLACE", where2(NB2[0]))])}</div>
<div class="cd2 lb"><span class=sm2>BAR LABEL · PRINTS ITSELF</span><div class=lab><div class=bar3>{"".join(f'<i style="background:{NB2[2]}"></i>' for _ in range(3))}</div><b>{NB2[1]}</b><span>Handmade soap · Sample Soap Studio</span><p class=ing>Made with coconut oil, olive oil, shea butter, castor oil and oats.</p><div class=ln><span>Batch {NB2[0]}</span><span>Made {dshort2(NB2[3])}</span><span>Ready {dshort2(rdy2(NB2))}</span></div></div></div></div></div>''',
css=f""".w22{{flex:1;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:16px;min-height:0}}
.bc{{padding:22px 24px;display:flex;flex-direction:column;gap:6px}}.bc .hd{{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}}.bc .hd b{{display:block;font:700 34px/1.3 Lora;margin-top:4px}}
.sc{{display:flex;align-items:center;gap:10px;background:{OAT2};border-radius:16px;padding:12px 14px;margin-bottom:8px}}.sc div{{flex:1;display:flex;flex-direction:column}}.sc span{{font:500 14px/1.3 Inter;color:{MU2}}}.sc b{{font:700 24px/1.3 Inter}}.sc em{{font:700 22px/1.3 Lora;font-style:italic;color:{LAV2}}}.sc .on b{{color:{LAV2}}}
.bc .r{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 90px 120px;align-items:center;border-top:1px solid #eee7da;font:500 20px/1.3 Inter}}.bc .r b{{text-align:right;font:700 21px/1.3 Inter}}.bc .r span:nth-child(2){{color:{MU2};text-align:right}}
.bc .r.h{{flex:none;border:0;padding-bottom:6px}}.bc .r.h span{{font:700 12px/1.3 Inter;letter-spacing:1.5px;color:{MU2};text-align:right}}.bc .r.h span:first-child{{text-align:left}}.bc .r.t{{font-weight:700;color:{OLV2}}}.bc .r.t b{{color:{OLV2}}}
.sd{{display:flex;flex-direction:column;gap:16px;min-height:0}}.dt{{padding:20px 22px;display:grid;grid-template-columns:1fr 1fr;gap:16px 14px}}.dt div{{border-top:1px solid #4a4558;padding-top:10px}}.dt b{{display:block;font:700 23px/1.35 Inter;margin-top:2px}}
.lb{{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:12px}}.lab{{flex:1;justify-content:center;border:2px dashed {LAV2};border-radius:16px;padding:16px;background:#f7f3fc;display:flex;flex-direction:column;gap:6px;align-items:center;text-align:center}}.lab b{{font:700 44px/1.3 Lora;font-style:italic;color:{LAV2}}}.lab>span{{font:500 17px/1.3 Inter;color:{MU2}}}
.bar3{{display:flex;gap:12px;margin-bottom:10px}}.ing{{font:500 17px/1.45 Inter;color:{INK2};max-width:340px;margin:4px 0}}.bar3 i{{width:96px;height:58px;border-radius:9px;box-shadow:inset 0 -6px 0 rgba(0,0,0,.12)}}.lab .ln{{display:flex;gap:8px;flex-wrap:wrap;justify-content:center;margin-top:4px}}.lab .ln span{{font:700 16px/1.3 Inter;background:#fff;border-radius:6px;padding:4px 8px}}""")
# ── slide 3: cure calendar (gantt)
G0 = _dt2.date(2026, 10, 19); G1 = _dt2.date(2026, 12, 21); GD = (G1 - G0).days
def gx2(d): return (d - G0).days / GD * 100
WK2 = [G0 + _dt2.timedelta(days=7 * i) for i in range(GD // 7 + 1)]
P["p452_soap_s3"] = t2(3, "2 · CURE CALENDAR", "No more guessing dates.<br><span>Ready day for every batch.</span>",
f'''<div class=w23><div class="cd2 gt"><div class=ax>{"".join(f'<span class="{"td" if w == TODAY2 else ""}" style="left:{gx2(w):.2f}%">{"Today" if w == TODAY2 else dshort2(w)}</span>' for w in WK2[:-1])}</div>
<div class=rows><div class=ov><i class=now style="left:{gx2(TODAY2):.2f}%"></i></div>{"".join(f'<div class=gr><div class=lbl><b>{b[0]}</b><span>{b[1]}</span></div><div class=tk>{"".join(f"<s style=left:{gx2(w):.2f}%></s>" for w in WK2[1:-1])}<div class=bar style="left:{gx2(b[3]):.2f}%;width:{gx2(rdy2(b)) - gx2(b[3]):.2f}%;background:{b[2]}"></div><u class="{"in" if gx2(rdy2(b)) > 80 else ""}" style="left:{gx2(rdy2(b)):.2f}%">{dshort2(rdy2(b))}</u></div></div>' for b in BT2)}</div></div>
<div class=bt><div class="dk2 rw"><span class=sm2>READY THIS WEEK</span>{"".join(f'<div class=r><i class=sw2 style="background:{b[2]}"></i><b>{b[0]} {b[1]}</b><span>{"Ready since " + dfmt2(rdy2(b)) if left2(b) < 0 else "Ready today"}</span></div>' for b in BT2 if left2(b) <= 0)}</div>
<div class="cd2 nx"><span class=sm2>NEXT UP</span>{"".join(f'<div class=r><i class=sw2 style="background:{b[2]}"></i><b>{b[0]} {b[1]}</b><span>{dfmt2(rdy2(b))}</span></div>' for b in BT2 if 0 < left2(b) <= 14)}</div></div></div>''',
css=f""".w23{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.gt{{flex:1;padding:20px 24px 18px;display:flex;flex-direction:column;gap:10px;min-height:0}}.ax{{position:relative;height:22px;margin-left:150px}}.ax span{{position:absolute;top:0;font:600 14px/1.4 Inter;color:{MU2};white-space:nowrap}}
.rows{{flex:1;display:flex;flex-direction:column;position:relative}}.ov{{position:absolute;left:150px;right:0;top:0;bottom:0;z-index:0}}.now{{position:absolute;top:0;bottom:0;width:3px;margin-left:-1px;background:{OLV2}}}.ax span.td{{color:#fff;background:{OLV2};border-radius:6px;padding:0 6px;transform:translateX(-50%)}}.gr{{position:relative;z-index:1}}.tk u.in{{transform:translateX(calc(-100% - 6px))}}
.gr{{flex:1;display:flex;align-items:center;border-top:1px solid #eee7da}}.lbl{{width:150px;flex:none;display:flex;flex-direction:column}}.lbl b{{font:700 19px/1.3 Inter}}.lbl span{{font:500 15px/1.3 Inter;color:{MU2}}}
.tk{{flex:1;position:relative;height:100%}}.tk s{{position:absolute;top:0;bottom:0;width:1px;background:#f0eadf}}.bar{{position:absolute;top:calc(50% - 13px);height:26px;border-radius:13px}}.tk u{{position:absolute;top:calc(50% - 14px);transform:translateX(8px);text-decoration:none;font:700 14px/1.3 Inter;background:#fff;border:2px solid #e2d9c8;border-radius:8px;padding:3px 7px;white-space:nowrap}}
.bt{{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:none}}.rw,.nx{{padding:18px 20px;display:flex;flex-direction:column;gap:10px}}.bt .r{{display:grid;grid-template-columns:18px minmax(0,1fr) auto;gap:10px;align-items:center}}.bt .r b{{font:700 19px/1.3 Inter}}.bt .r span{{font:500 16px/1.3 Inter;color:inherit;opacity:.8}}""")
# ── slide 4: orders from ready bars
ORD2 = [("Sample Gift Shop", [("Lavender", 12), ("Coffee", 12)]), ("Sample Cafe", [("Coffee", 10)]), ("Online order #118", [("Lavender", 2), ("Rose clay", 1)])]
avail2 = {b[1]: (stock2(b) if left2(b) <= 0 else 0) for b in BT2}
ALLOC2 = []
for who, items in ORD2:
    res = []
    for soap, q in items:
        g = min(q, avail2[soap]); avail2[soap] -= g
        b = [t for t in BT2 if t[1] == soap][0]
        res.append((soap, q, g, b))
    ALLOC2.append((who, res))
WAIT2 = [(who, s, q - g, b) for who, res in ALLOC2 for s, q, g, b in res if g < q]
assert WAIT2 and WAIT2[0][1] == "Rose clay"
P["p452_soap_s4"] = t2(4, "3 · ORDERS", "Orders packed from<br><span>bars that are ready.</span>",
f'''<div class=w24><div class=os>{"".join(f'<div class="cd2 od"><div class=tx><div class=hd><b>{who}</b><span class=sm2>MON 23 NOV</span></div>' + "".join(f'<div class=r><i class=sw2 style="background:{b[2]}"></i><span>{s} × {q}</span>' + (f'<span class="ch2 ok">From {b[0]}</span>' if g == q else f'<span class="ch2 wt">Ships {dshort2(rdy2(b))}</span>') + '</div>' for s, q, g, b in res) + '</div><div class=kb><span class=sm2>BOX · ' + str(sum(g for _, _, g, _ in res)) + ' BARS</span>' + bars2([(b[2], g) for _, _, g, b in res], cols=6) + '</div></div>' for who, res in ALLOC2)}</div>
<div class=sd><div class="dk2 st"><span class=sm2>READY STOCK AFTER PACKING</span>{"".join(f'<div class=r><i class=sw2 style="background:{b[2]}"></i><b>{b[1]}</b><strong>{avail2[b[1]]}</strong></div>' + (bars2([(b[2], avail2[b[1]])], 26, 16, 7) if avail2[b[1]] else '<div class=none>None left · make a new batch this week</div>') for b in BT2 if left2(b) <= 0)}<p>Still curing: {sum(stock2(b) for b in BT2 if left2(b) > 0)} bars in {sum(1 for b in BT2 if left2(b) > 0)} batches. They join ready stock on their own on their ready day.</p></div>
<div class="cd2 ms"><span class=sm2>MESSAGE TO {WAIT2[0][0].upper()}</span><div class=bb>Your lavender soaps are packed. The rose clay soap is still curing and will ship on {dfmt2(rdy2(WAIT2[0][3]))}.</div><div class="bb me">Okay, thank you. Send both together if that is easier.</div><div class=bb>Sure. Both will go on {dfmt2(rdy2(WAIT2[0][3]))}.</div></div></div></div>''',
css=f""".w24{{flex:1;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:16px;min-height:0}}.os{{display:flex;flex-direction:column;gap:16px;min-height:0}}
.od{{flex:1;padding:18px 22px;display:grid;grid-template-columns:minmax(0,1fr) 168px;gap:18px;align-items:center}}.od .tx{{display:flex;flex-direction:column;gap:12px}}.kb{{background:#e9d9bb;border-radius:14px;padding:12px;display:flex;flex-direction:column;gap:8px;align-items:center;align-self:stretch;justify-content:center}}.kb .sm2{{color:#7a6542}}
.bx2{{display:grid;gap:4px}}.bx2 i{{border-radius:4px;box-shadow:inset 0 -3px 0 rgba(0,0,0,.14)}}.none{{border:2px dashed #6b6480;border-radius:10px;padding:10px 12px;font:600 16px/1.3 Inter;color:#d8d2e4}}.od .hd{{display:flex;justify-content:space-between;align-items:baseline;gap:8px}}.od .hd b{{font:700 24px/1.3 Lora}}.od .hd{{flex-direction:column;align-items:flex-start!important;gap:2px!important}}.od .r{{display:grid;grid-template-columns:18px minmax(0,1fr) auto;gap:12px;align-items:center;border-top:1px solid #eee7da;padding-top:12px}}.od .r>span:nth-child(2){{font:600 19px/1.3 Inter;white-space:nowrap}}
.sd{{display:flex;flex-direction:column;gap:16px;min-height:0}}.st{{padding:20px 22px;display:flex;flex-direction:column;gap:12px}}.st .r{{display:grid;grid-template-columns:18px minmax(0,1fr) auto;gap:12px;align-items:center}}.st .r b{{font:600 21px/1.3 Inter}}.st .r strong{{font:700 44px/1.3 Lora}}.st p{{font:500 17px/1.4 Inter;color:#d8d2e4;border-top:1px solid #4a4558;padding-top:12px}}
.ms{{padding:18px 20px;display:flex;flex-direction:column;gap:12px;flex:1;justify-content:center}}.bb.me{{background:{OAT2};border-radius:16px 16px 4px 16px;align-self:flex-end;max-width:80%}}.bb{{background:#ece6f6;border-radius:16px 16px 16px 4px;padding:14px 16px;font:500 19px/1.45 Inter}}""")
# ── slide 5 CTA
P["p452_soap_s5"] = t2(5, "HANDMADE SOAP · YOUR APP", "Make soap by hand?<br><span>Let the app keep the dates.</span>",
f'''<div class=w25><div class=tl>{"".join(f'<div class="cd2 t"><div class=il>{il}</div><b>{a}</b><p>{p}</p></div>' for a, p, il in [("Curing rack", "Every tray, its batch and its ready day.", f'<div class=rs>{rack2()}</div>'), ("Batch card", "Recipe scales to any number of bars.", f'<div class=sc5><span>36 bars</span><em>× {F2:.2f}</em><b>{NB2[4]} bars</b></div>'), ("Cure calendar", "See what is ready this week and next.", '<div class=gm>' + "".join(f'<i style="margin-left:{k * 14}%;width:{40 + k * 3}%;background:{b[2]}"></i>' for k, b in enumerate(BT2[:4])) + '</div>'), ("Orders", "Pack only from ready bars, tell the rest.", f'<div class=kb>{bars2([(BT2[0][2], 12), (BT2[1][2], 12)], 24, 15, 6)}</div>')])}</div>
<div class="dk2 q"><p>How do you track which soap batch is ready today? Tell us in the comments.</p></div></div>''',
css=f""".w25{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl{{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px;min-height:0}}
.t{{padding:24px 26px;display:flex;flex-direction:column;gap:12px}}.il{{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;background:{OAT2};border-radius:16px;padding:14px}}.rs{{height:100%;min-height:150px;width:200px;position:relative}}.t .kb{{background:#e9d9bb;border-radius:14px;padding:14px;display:flex}}.bx2{{display:grid;gap:4px}}.bx2 i{{border-radius:4px;box-shadow:inset 0 -3px 0 rgba(0,0,0,.14)}}.rs svg{{position:absolute;inset:0}}.sc5{{display:flex;align-items:center;gap:12px;font:700 24px/1.3 Inter}}.sc5 em{{font:700 24px/1.3 Lora;color:{LAV2}}}.sc5 b{{color:{LAV2}}}.gm{{width:100%;display:flex;flex-direction:column;gap:12px}}.gm i{{display:block;height:20px;border-radius:10px}}.t .kb{{background:#e9d9bb;align-self:center}}.t>b{{font:700 32px/1.25 Lora}}.t p{{font:500 21px/1.45 Inter;color:{MU2}}}.q{{padding:24px 28px}}.q p{{font:600 24px/1.45 Lora;font-style:italic}}""",
cta="Make soap? DM us", ctacss=f"background:{LAV2};color:#fff")
