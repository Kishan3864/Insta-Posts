
# ───────── 424 INDIA · Tractor trolley maker · SINGLE · Anton + Source Sans 3 · primer grey / oxide red / hazard yellow
# New technique: side-view SVG tipping trolley whose parts are filled by build stage (done solid, working hatched yellow,
# pending dashed outline), plus a stage-dot board for all orders and the customer update derived from the same stages.
OX4 = "#b5432c"; HY4 = "#f2c12e"; K4 = "#1f2124"; BG4 = "#e9e7e3"; GD4 = "#2e7d4f"
PART4 = {"Chassis": "done", "Drawbar": "done", "Axle + tyres": "done", "Body": "work", "Hydraulic": "todo", "Paint": "todo"}
def fill4(p, d):
    s = PART4[p]
    if s == "done": return f'<path d="{d}" fill="#4a4d52" stroke="{GD4}" stroke-width="5"/>'
    if s == "work": return f'<path d="{d}" fill="url(#hz4)" stroke="#b58d10" stroke-width="4"/>'
    return f'<path d="{d}" fill="#f4f2ee" stroke="#8f8b84" stroke-width="3" stroke-dasharray="10 7"/>'
def trolley4():
    body = fill4("Body", "M150 70 L760 70 L760 224 L150 224 Z") + "".join(f'<path d="M150 {y} L760 {y}" stroke="#b58d10" stroke-width="2.5"/>' for y in (108, 146, 186)) + "".join(f'<path d="M{x} 70 L{x} 224" stroke="#b58d10" stroke-width="3"/>' for x in (300, 455, 610))
    hyd = fill4("Hydraulic", "M196 232 L250 232 L262 254 L208 254 Z") + '<path d="M228 232 L246 150" stroke="#8f8b84" stroke-width="12" stroke-dasharray="10 7" stroke-linecap="round"/>'
    chassis = fill4("Chassis", "M120 230 L800 230 L800 256 L120 256 Z")
    draw = fill4("Drawbar", "M20 236 L130 236 L130 250 L20 250 Z") + '<circle cx="22" cy="243" r="14" fill="none" stroke="#2e7d4f" stroke-width="6"/>'
    wheels = "".join(f'<circle cx="{x}" cy="300" r="56" fill="#2a2c30" stroke="{GD4}" stroke-width="5"/><circle cx="{x}" cy="300" r="24" fill="#8d9096"/>' for x in (560, 690))
    lab = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="8" fill="{K4}"/><text x="{x + w / 2}" y="{y + 24}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="19" fill="#fff"><tspan>{t}</tspan></text>' for x, y, w, t in [(380, 128, 120, "Body"), (130, 268, 120, "Hydraulic"), (300, 262, 110, "Chassis"), (40, 196, 104, "Drawbar"), (750, 262, 66, "Tyres")])
    return f'''<svg viewBox="0 0 820 365" width="820" style="display:block;width:100%;height:auto"><defs><pattern id="hz4" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="22" height="22" fill="{HY4}"/><rect width="10" height="22" fill="#f7d76b"/></pattern></defs>
<rect x="0" y="356" width="820" height="6" rx="3" fill="#bdb9b1"/>{body}{chassis}{hyd}{draw}{wheels}{lab}</svg>'''
STG4 = ["Cut", "Chassis", "Body", "Ram", "Paint", "Ready"]
BD4 = [("T-12", "Sample Farmer A", 6), ("T-13", "Sample Farmer B", 4), ("T-14", "Sample Farmer C", 2), ("T-15", "Sample Farmer D", 0)]
def dots4(n):
    return "".join(f'<i class="{"dn" if k < n else ("wk" if k == n else "")}"></i>' for k in range(len(STG4)))
P["p424_trolley"] = page(f"""
body{{--f:'Source Sans 3';--h:'Anton';background:{BG4};color:{K4}}}
.kk{{font:700 16px/1.5 'Source Sans 3';letter-spacing:3px;color:{OX4};margin-top:22px}}
h1{{font-family:'Anton';font-weight:400;font-size:64px;line-height:1.28;letter-spacing:.4px;margin-top:30px}} h1 span{{color:{OX4}}}
.vw4{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm4{{font:700 13px/1.5 'Source Sans 3';letter-spacing:2px;color:#6f6b64;margin-bottom:4px}}
.cd4{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(31,33,36,.08);padding:16px 20px;display:flex;flex-direction:column;gap:8px}}
.lgd4{{display:flex;gap:18px;font:600 16px/1.3 'Source Sans 3'}}.lgd4 i{{display:inline-block;width:20px;height:20px;border-radius:5px;margin-right:6px;vertical-align:-4px}}
.bt4{{flex:1;display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:14px;min-height:0}}
.oc4{{background:{K4};color:#fff}}.oc4 .sm4{{color:#b3afa7}}.oc4 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid rgba(255,255,255,.12)}}.oc4 .r span{{font:500 17px/1.3 'Source Sans 3';color:#cfcbc3}}.oc4 .r b{{font:700 19px/1.3 'Source Sans 3';text-align:right}}
.rt4{{display:flex;flex-direction:column;gap:14px;min-height:0}}.bd4{{flex:1}}
.bd4 .hd{{display:grid;grid-template-columns:74px 1fr repeat(6,48px);gap:6px;font:700 12px/1.5 'Source Sans 3';letter-spacing:.5px;color:#6f6b64}}.bd4 .hd span:nth-child(n+3){{text-align:center}}
.bd4 .r{{flex:1;display:grid;grid-template-columns:74px 1fr repeat(6,48px);gap:6px;align-items:center;border-top:1px solid #ecebe7}}.bd4 .r b{{font:400 24px/1.5 Anton}}.bd4 .r span{{font:600 17px/1.3 'Source Sans 3'}}
.bd4 .r i{{width:24px;height:24px;border-radius:50%;border:3px solid #cfcbc3;justify-self:center}}.bd4 .r i.dn{{background:{GD4};border-color:{GD4}}}.bd4 .r i.wk{{background:{HY4};border-color:#b58d10}}
.ms4{{background:#fbecc0;padding:14px 18px}}.ms4 p{{font:600 19px/1.45 'Source Sans 3';text-wrap:pretty}}.ms4 p b{{color:{OX4}}}
""", "<div class=kk>TRACTOR TROLLEY MAKER · BUILD STATUS</div><h1>Customers calling for updates?<br><span>Show the build, part by part.</span></h1>",
f'''<div class=vw4><div class=cd4><div style="display:flex;justify-content:space-between;align-items:center"><span class=sm4>T-14 · TIPPING TROLLEY · TUE 24 NOV · SAMPLE</span><span class=lgd4><span><i style="background:#4a4d52;border:3px solid {GD4}"></i>Done</span><span><i style="background:{HY4}"></i>Working</span><span><i style="border:2px dashed #8f8b84"></i>Next</span></span></div>{trolley4()}</div>
<div class=bt4><div class="cd4 oc4"><span class=sm4>ORDER T-14 · SAMPLE FARMER C</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Body", "10 × 6 ft, sides 2 ft"), ("Type", "Hydraulic tipping"), ("Axle", "Tandem · 4 tyres"), ("Colour", "Red, yellow strip"), ("Ready", "Sat 28 Nov")])}</div>
<div class=rt4><div class="cd4 bd4"><div class=hd><span>ORDER</span><span>CUSTOMER</span>{"".join(f"<span>{s}</span>" for s in STG4)}</div>{"".join(f'<div class=r><b>{o}</b><span>{c}</span>{dots4(n)}</div>' for o, c, n in BD4)}</div>
<div class="cd4 ms4"><span class=sm4>UPDATE SENT TO SAMPLE FARMER C</span><p><b>T-14:</b> body welding today, 3 photos attached. Ram and paint on Thu 26 Nov. Ready Sat 28 Nov.</p></div></div></div></div>''',
K4, "Build trolleys? DM us", f"background:{OX4};color:#fff")
