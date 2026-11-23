# ───────── 451 INDIA · Invisible grill installer (balcony quote) · SINGLE · Montserrat + Roboto · sky blue / cable silver / brick coral
# New technique: to-scale facade built from HTML boxes (110 px per metre) with real cable spacing drawn as a repeating gradient
# (50 mm = 5.5 px), so the grill on the drawing has exactly the cable count in the measure sheet; spacing options recomputed live.
SK1 = "#dcecf6"; NV1 = "#18324a"; CO1 = "#e0674a"; MU1 = "#5d6f80"; WL1 = "#f3eee6"
OP1 = [("A", "Living balcony", 3.60, 1.80, 0), ("B", "Bedroom balcony", 2.40, 1.80, 0), ("W1", "Kitchen window", 1.50, 1.20, 0.30)]
PXM1 = 110
def cables1(w, gap): return round(w / gap) - 1
ROWS1 = [(k, nm, w, h, cables1(w, .05), cables1(w, .05) * h, 2 * w) for k, nm, w, h, _ in OP1]
TOT1 = (sum(r[4] for r in ROWS1), sum(r[5] for r in ROWS1), sum(r[6] for r in ROWS1))
GAPS1 = [("2 in", 50), ("3 in", 75), ("4 in", 100)]
def op1(k, nm, w, h, drop):
    n = cables1(w, .05)
    return f'''<div class=oc style="width:{w * PXM1:.0f}px"><div class=op style="height:{h * PXM1:.0f}px;margin-top:{drop * PXM1:.0f}px"><b class=pin>{k} · {n} cables</b></div><div class=pw style="height:{(0.6 if drop == 0 else 1.2) * PXM1 - drop * PXM1:.0f}px"><span>{"Parapet wall" if drop == 0 else "Wall"}</span></div><div class=dm><i></i><span>{w:.2f} m</span><i></i></div></div>'''
P["p451_grill"] = page(f"""
body{{--f:'Roboto';--h:'Montserrat';background:{SK1};color:{NV1}}}
.kk1{{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:{CO1};margin-top:22px}}
h1{{font-family:'Montserrat';font-weight:800;font-size:54px;line-height:1.2;letter-spacing:-1.4px;margin-top:12px}} h1 span{{color:{CO1}}}
.w1{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm1{{font:700 13px/1.4 'Roboto';letter-spacing:2px;color:{MU1}}}
.cd1{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(24,50,74,.08)}}
.fa{{background:{WL1};border-radius:22px;padding:18px 24px 14px;display:flex;flex-direction:column;gap:12px;flex:none;box-shadow:0 14px 30px rgba(24,50,74,.08)}}
.fa .hd{{display:flex;justify-content:space-between;align-items:baseline}}.fa .hd b{{font:700 18px/1.3 'Roboto'}}
.fr{{display:flex;justify-content:center;gap:36px;align-items:flex-start;border-top:10px solid #c9bfae;padding-top:0}}
.oc{{display:flex;flex-direction:column;gap:8px;flex:none}}
.op{{position:relative;background:repeating-linear-gradient(90deg,transparent 0 4.4px,#8c99a6 4.4px 5.5px),linear-gradient(#bfe0f3,#e9f5fb);border-left:6px solid #9aa6b2;border-right:6px solid #9aa6b2;border-bottom:8px solid #9aa6b2;display:flex;align-items:flex-start;justify-content:center;padding-top:12px}}
.pin{{background:{NV1};color:#fff;font:700 15px/1.3 'Roboto';padding:5px 10px;border-radius:8px;white-space:nowrap}}
.pw{{background:repeating-linear-gradient(0deg,transparent 0 17px,rgba(255,255,255,.55) 17px 19px),#e6a58f;border-radius:0 0 4px 4px;display:flex;align-items:center;justify-content:center}}.pw span{{font:600 14px/1.3 'Roboto';color:#7a3a28;background:rgba(255,255,255,.7);padding:3px 8px;border-radius:6px}}
.dm{{display:flex;align-items:center;gap:6px}}.dm i{{flex:1;height:2px;background:{MU1}}}.dm span{{font:700 15px/1.3 'Roboto';color:{MU1}}}
.bt1{{flex:1;display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:16px;min-height:0}}
.tb{{padding:16px 20px;display:flex;flex-direction:column}}.tb .r{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 104px 62px 74px;gap:8px;align-items:center;border-top:1px solid #e7ecf0}}
.tb .r.h{{flex:none;border:0;padding:8px 0 8px}}.tb .r.h span{{font:700 12px/1.3 'Roboto';letter-spacing:1px;color:{MU1}}}
.tb .r b{{font:700 19px/1.3 'Roboto';display:block}}.tb .r small{{font:500 14px/1.3 'Roboto';color:{MU1}}}.tb .r span{{font:500 18px/1.3 'Roboto'}}.tb .r strong{{font:700 19px/1.3 'Roboto';text-align:right}}
.tb .r.t{{background:#fdf0ec;border-radius:12px;border:0;padding:0 10px;margin:4px -10px 0}}.tb .r.t b,.tb .r.t strong{{color:{CO1}}}
.sd1{{display:flex;flex-direction:column;gap:16px;min-height:0}}
.gp{{padding:14px 18px;display:flex;flex-direction:column;gap:8px}}.gp .o{{display:flex;justify-content:space-between;align-items:center;border:2px solid #e3e9ee;border-radius:12px;padding:6px 14px}}.gp .o b{{font:700 18px/1.3 'Roboto'}}.gp .o span{{font:500 17px/1.3 'Roboto';color:{MU1}}}.gp .o.on{{border-color:{CO1};background:#fdf0ec}}.gp .o.on span{{color:{CO1};font-weight:700}}
.dk1{{flex:1;background:{NV1};color:#fff;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;justify-content:space-between;gap:6px;min-height:0}}.dk1 .sm1{{color:#9fb4c8}}
.mt{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}.mt div{{background:#26445f;border-radius:12px;padding:8px 10px}}.mt strong{{display:block;font:800 22px/1.3 Montserrat;color:#fff}}.mt span{{font:500 14px/1.3 'Roboto';color:#b9cad9}}
.dk1 .s{{display:flex;gap:12px;align-items:flex-start}}.dk1 .s i{{width:14px;height:14px;border-radius:50%;background:#5fd08a;margin-top:5px;flex:none}}.dk1 .s.nx i{{background:transparent;border:3px solid {CO1}}}.dk1 .s p{{font:500 16px/1.3 'Roboto'}}.dk1 .s p b{{display:block;font:700 17px/1.3 'Roboto'}}
""", "<div class=kk1>INVISIBLE GRILL · BALCONY QUOTE</div><h1>Balcony size on scrap paper?<br><span>Cables counted from the drawing.</span></h1>",
f'''<div class=w1><div class=fa><div class=hd><span class=sm1>SAMPLE FLAT 704 · FRONT VIEW TO SCALE · CABLE EVERY 50 MM</span><b>{len(OP1)} openings</b></div>
<div class=fr>{"".join(op1(*o) for o in OP1)}</div></div>
<div class=bt1><div class="cd1 tb"><div class="r h"><span>OPENING</span><span>W × H (M)</span><span>CABLES</span><span>CABLE M</span></div>
{"".join(f'<div class=r><div><b>{k} · {nm}</b><small>Track {tr:.1f} m, top and bottom</small></div><span>{w:.2f} × {h:.2f}</span><strong>{n}</strong><strong>{cm:.1f}</strong></div>' for k, nm, w, h, n, cm, tr in ROWS1)}
<div class="r t"><div><b>Total for the flat</b><small>Track {TOT1[2]:.1f} m in all</small></div><span></span><strong>{TOT1[0]}</strong><strong>{TOT1[1]:.1f}</strong></div></div>
<div class=sd1><div class="cd1 gp"><span class=sm1>CABLE GAP · TAP TO CHANGE</span>{"".join(f'<div class="o{" on" if mm == 50 else ""}"><b>{a} · {mm} mm</b><span>{sum(cables1(w, mm / 1000) for _, _, w, _, _ in OP1)} cables</span></div>' for a, mm in GAPS1)}</div>
<div class=dk1><span class=sm1>MATERIAL FOR THIS JOB</span><div class=mt>{"".join(f'<div><strong>{a}</strong><span>{b}</span></div>' for a, b in [(f"{TOT1[1]:.1f} m", "cable"), (f"{TOT1[2]:.1f} m", "track"), (f"{TOT1[0] * 2}", "end caps")])}</div><span class=sm1>SITE VISIT · SAMPLE</span><div class=s><i></i><p><b>Measured</b>Mon 23 Nov, 11 AM</p></div><div class=s><i></i><p><b>Quote + drawing on WhatsApp</b>Mon 23 Nov, 6:40 PM</p></div><div class="s nx"><i></i><p><b>Install booked</b>Thu 26 Nov, 10 AM</p></div></div></div></div></div>''',
NV1, "Fit invisible grills? DM us", f"background:{CO1};color:#fff")
