
# ───────── 432 INDIA · Wire harness job work unit · SINGLE · Montserrat + Source Sans 3 · harness black / copper / signal blue
# New technique: harness board drawing with wire branches drawn proportional to their length (mm) from one wire list,
# which also builds the cut list (metres for the whole order) and the stage counts.
HB2 = "#1d2126"; CU2 = "#c9773a"; SB2 = "#2f6fd1"; BG2b = "#f2f0ec"; MU2 = "#636a73"
WR2 = [("W1", "Red", "#d64541", 1.0, 450, "C"), ("W2", "Black", "#22262b", 1.0, 450, "C"), ("W3", "Blue", "#2f6fd1", 0.5, 620, "B"),
       ("W4", "Yellow", "#e8b923", 0.5, 620, "B"), ("W5", "Green", "#2e9e5b", 0.5, 380, "D"), ("W6", "White", "#f4f4f4", 0.5, 380, "D")]
QTY2 = 500
STG2 = [("Cut", 500), ("Crimp", 420), ("Assemble", 260), ("Test", 180)]
def board2():
    K = 1.1; ax = 110; out = '<rect x="0" y="0" width="900" height="300" rx="16" fill="#e7e1d6"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="2.5" fill="#cfc6b6"/>' for x in range(30, 900, 40) for y in range(24, 300, 40))
    ends = {"B": (ax + 620 * K, 70), "C": (ax + 450 * K, 150), "D": (ax + 380 * K, 236)}
    for i, (c, nm, col, mm2, L, to) in enumerate(WR2):
        y0 = 126 + i * 8; ex, ey = ends[to]; off = (i % 2) * 8 - 4
        bx = ax + 120
        out += f'<path d="M{ax} {y0} H{bx} L{bx + 60} {ey + off} H{ex}" stroke="{"#9aa0a6" if nm == "White" else col}" stroke-width="{7 if mm2 == 1.0 else 5}" fill="none" stroke-linejoin="round"/>'
        if nm == "White": out += f'<path d="M{ax} {y0} H{bx} L{bx + 60} {ey + off} H{ex}" stroke="#f4f4f4" stroke-width="3" fill="none" stroke-linejoin="round"/>'
    out += f'<rect x="{ax - 70}" y="104" width="74" height="92" rx="10" fill="{HB2}"/><text x="{ax - 33}" y="158" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="24" fill="#fff"><tspan>A</tspan></text>'
    for k, (x, y) in ends.items():
        out += f'<rect x="{x}" y="{y - 26}" width="60" height="52" rx="9" fill="{HB2}"/><text x="{x + 30}" y="{y + 8}" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="22" fill="#fff"><tspan>{k}</tspan></text>'
    for k, L in [("B", 620), ("C", 450), ("D", 380)]:
        x, y = ends[k]
        out += f'<rect x="{x - 110}" y="{y - 46 if k != "D" else y + 18}" width="96" height="26" rx="6" fill="#fff"/><text x="{x - 62}" y="{(y - 46 if k != "D" else y + 18) + 19}" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="16" fill="{HB2}"><tspan>{L} mm</tspan></text>'
    out += f'<rect x="{ax + 128}" y="112" width="40" height="76" rx="6" fill="{CU2}" opacity=".85"/>'
    return f'<svg viewBox="0 0 900 300" style="display:block;width:100%;height:auto">{out}</svg>'
P["p432_harness"] = page(f"""
body{{--f:'Source Sans 3';--h:'Montserrat';background:{BG2b};color:{HB2}}}
.kk{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{CU2};margin-top:22px}}
h1{{font-family:'Montserrat';font-weight:800;font-size:56px;line-height:1.2;letter-spacing:-1.5px;margin-top:14px}} h1 span{{color:{SB2}}}
.w2{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm2{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:{MU2}}}
.cd2{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(29,33,38,.08);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.bt2{{flex:1;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:16px;min-height:0}}
.cl2 .h,.cl2 .r{{display:grid;grid-template-columns:28px 1fr 70px 80px 90px;gap:10px;align-items:center}}.cl2 .h span{{font:700 13px/1.3 'Source Sans 3';color:{MU2};letter-spacing:1px}}.cl2 .h span:nth-child(n+3){{text-align:right}}
.cl2 .r{{flex:1;border-top:1px solid #ece8e1}}.cl2 .r i{{width:24px;height:24px;border-radius:50%;border:2px solid #c9c3b8}}.cl2 .r b{{font:700 19px/1.3 'Source Sans 3'}}.cl2 .r span{{font:600 18px/1.3 'Source Sans 3';text-align:right}}.cl2 .r strong{{font:800 19px/1.3 Montserrat;text-align:right;color:{SB2}}}
.cl2 .tt{{display:flex;justify-content:space-between;background:#f6f1ea;border-radius:12px;padding:10px 14px;font:700 18px/1.3 'Source Sans 3'}}.cl2 .tt b{{font:800 20px/1.3 Montserrat;color:{CU2}}}
.rt2{{display:flex;flex-direction:column;gap:16px;min-height:0}}
.sg2{{flex:1;background:{HB2};color:#fff}}.sg2 .sm2{{color:#aab1ba}}.sg2 .r{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px}}.sg2 .r div{{display:flex;justify-content:space-between;font:700 19px/1.3 'Source Sans 3'}}.sg2 .r div b{{font:800 20px/1.3 Montserrat;color:#f2b27c}}.sg2 .bar{{height:14px;border-radius:7px;background:#3a4048;overflow:hidden}}.sg2 .bar i{{display:block;height:100%;background:{CU2};border-radius:7px}}
.ts2 p{{display:flex;align-items:center;gap:10px;font:600 18px/1.35 'Source Sans 3'}}.ts2 p svg{{flex:none}}
""", "<div class=kk>WIRE HARNESS · JOB WORK</div><h1>Harness orders on paper?<br><span>Every wire cut, crimped, tested.</span></h1>",
f'''<div class=w2><div class=cd2><span class=sm2>HARNESS H-12 · BOARD DRAWING · WIRES TO SCALE · SAMPLE</span>{board2()}</div>
<div class=bt2><div class="cd2 cl2"><span class=sm2>CUT LIST · ORDER OF {QTY2} HARNESSES</span><div class=h><span></span><span>WIRE</span><span>SQ MM</span><span>MM</span><span>METRES</span></div>
{"".join(f'<div class=r><i style="background:{col}"></i><b>{c} · {nm}</b><span>{mm2:.1f}</span><span>{L}</span><strong>{L * QTY2 // 1000:,}</strong></div>' for c, nm, col, mm2, L, to in WR2)}
<div class=tt><span>Wire to cut for H-12</span><b>{sum(w[4] for w in WR2) * QTY2 // 1000:,} m</b></div></div>
<div class=rt2><div class="cd2 sg2"><span class=sm2>H-12 · DUE SAT 28 NOV · SAMPLE</span>{"".join(f'<div class=r><div><span>{a}</span><b>{n} / {QTY2}</b></div><div class=bar><i style="width:{n / QTY2 * 100:.0f}%"></i></div></div>' for a, n in STG2)}</div>
<div class="cd2 ts2"><span class=sm2>TEST BENCH · TODAY</span><p>{ic("check", 22, "#2e9e5b", 3)}Continuity checked on each harness</p><p>{ic("x", 22, "#d64541", 3)}3 failed: crimp on W4 redone</p></div></div></div></div>''',
HB2, "Make wire harnesses? DM us", f"background:{SB2};color:#fff")
