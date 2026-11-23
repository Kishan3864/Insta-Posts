
# ───────── 445 USA · Water damage restoration (dry-out log) · SINGLE · Crimson Text + DM Sans · drywall white / navy / moisture heat
# New technique: to-scale floor plan with moisture reading points drawn as heat halos (colour by reading band), equipment
# glyphs, and four small-multiple day maps whose wet counts are computed from the same reading table.
NV5 = "#1c2b4a"; BG5 = "#f4f2ed"; MU5 = "#636b78"; WET5 = "#d64545"; DAMP5 = "#e9a23b"; DRY5 = "#3a9bd5"; GOAL5 = 15
PTS5 = [("P1", 3, 1.0, [42, 35, 26, 19]), ("P2", 5, 5, [38, 30, 21, 15]), ("P3", 9, 8.6, [30, 22, 16, 12]), ("P4", 18, 10.9, [35, 27, 18, 14]),
        ("P5", 16.5, 9.8, [28, 20, 14, 11]), ("P6", 20.9, 3, [45, 38, 30, 22]), ("P7", 18, 4.5, [40, 33, 25, 17]), ("P8", 11, 1, [33, 25, 17, 13])]
DAYS5 = ["Fri 20 Nov", "Sat 21 Nov", "Sun 22 Nov", "Mon 23 Nov"]
def col5(v): return WET5 if v > 30 else (DAMP5 if v > GOAL5 else DRY5)
WETN5 = [sum(1 for p in PTS5 if p[3][d] > GOAL5) for d in range(4)]
EQ5 = [("AM", 6.5, 10), ("AM", 13, 5), ("AM", 19.5, 6.5), ("DH", 12, 10.6)]
def plan5(S=30, d=3, mini=False):
    P = 20; W = 22 * S; H = 12 * S
    g = lambda x: P + x * S
    rooms = (f'<rect x="{g(0)}" y="{g(0)}" width="{14 * S}" height="{12 * S}" fill="#fff"/><rect x="{g(14)}" y="{g(0)}" width="{8 * S}" height="{8 * S}" fill="#fff"/><rect x="{g(14)}" y="{g(8)}" width="{8 * S}" height="{4 * S}" fill="#fff"/>'
             f'<rect x="{g(0)}" y="{g(0)}" width="{14 * S}" height="{2 * S}" fill="#e6e1d8"/><rect x="{g(7)}" y="{g(5)}" width="{4 * S}" height="{3 * S}" rx="4" fill="#e6e1d8"/><rect x="{g(15)}" y="{g(0)}" width="{4 * S}" height="{2.5 * S}" fill="#e6e1d8"/>')
    walls = f'<rect x="{g(0)}" y="{g(0)}" width="{W}" height="{H}" fill="none" stroke="{NV5}" stroke-width="{6 if not mini else 4}"/><path d="M{g(14)} {g(0)} V{g(5.5)} M{g(14)} {g(7.5)} V{g(12)} M{g(14)} {g(8)} H{g(16)} M{g(19)} {g(8)} H{g(22)}" stroke="{NV5}" stroke-width="{4 if not mini else 3}"/>'
    halos = dots = ""
    for n, x, y, v in PTS5:
        c = col5(v[d])
        if not mini:
            halos += f'<circle cx="{g(x):.0f}" cy="{g(y):.0f}" r="{24 + v[d] * 1.6:.0f}" fill="url(#h5{c[1:]})" clip-path="url(#cp5)"/>'
            dots += f'<circle cx="{g(x):.0f}" cy="{g(y):.0f}" r="20" fill="{c}" stroke="#fff" stroke-width="3"/><text x="{g(x):.0f}" y="{g(y) + 6:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#fff"><tspan>{v[d]}</tspan></text><rect x="{g(x) + (24 if x < 20 else -54):.0f}" y="{g(y) - 10:.0f}" width="30" height="20" rx="5" fill="{NV5}"/><text x="{g(x) + (39 if x < 20 else -39):.0f}" y="{g(y) + 5:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="13" fill="#fff"><tspan>{n}</tspan></text>'
        else:
            dots += f'<circle cx="{g(x):.0f}" cy="{g(y):.0f}" r="{7 + v[d] * .12:.1f}" fill="{c}"/>'
    eq = ""
    if not mini:
        for k, x, y in EQ5:
            eq += (f'<rect x="{g(x) - 22:.0f}" y="{g(y) - 15:.0f}" width="44" height="30" rx="8" fill="{NV5}"/><text x="{g(x):.0f}" y="{g(y) + 6:.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="#fff"><tspan>{k}</tspan></text>')
        lbl = "".join(f'<text x="{g(x):.0f}" y="{g(y):.0f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="15" fill="{MU5}" letter-spacing="2"><tspan>{t}</tspan></text>' for t, x, y in [("KITCHEN · 14 × 12 FT", 4.4, 3.4), ("LAUNDRY", 18, 7.5), ("HALL", 20.6, 9.3)])
    else:
        lbl = ""
    defs = "".join(f'<radialGradient id="h5{c[1:]}"><stop offset="0" stop-color="{c}" stop-opacity=".55"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></radialGradient>' for c in (WET5, DAMP5, DRY5)) + f'<clipPath id="cp5"><rect x="{P}" y="{P}" width="{W}" height="{H}"/></clipPath>' if not mini else ""
    return f'<svg viewBox="0 0 {W + 2 * P} {H + 2 * P}" style="display:block;width:100%;height:auto"><defs>{defs}</defs>{rooms}{halos}{walls}{lbl}{eq}{dots}</svg>'
P["p445_water"] = page(f"""
body{{--f:'DM Sans';--h:'Crimson Text';background:{BG5};color:{NV5};font-variant-numeric:lining-nums}}
.kk5{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{WET5};margin-top:22px}}
h1{{font-family:'Crimson Text';font-weight:700;font-size:64px;line-height:1.22;letter-spacing:-.5px;margin-top:10px}} h1 span{{color:{DRY5}}}
.w5{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm5{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:{MU5}}}
.cd5{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(28,43,74,.08)}}
.pl5{{padding:16px 20px;display:grid;grid-template-columns:minmax(0,1fr) 206px;gap:16px;flex:none}}.pl5 .l{{display:flex;flex-direction:column;gap:8px}}
.pl5 .r{{display:flex;flex-direction:column;gap:10px;justify-content:space-between}}.lgx5 div{{display:flex;align-items:center;gap:10px;font:600 18px/1.35 'DM Sans';padding:4px 0}}.lgx5 i{{width:20px;height:20px;border-radius:50%;flex:none}}
.big5{{background:{NV5};color:#fff;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column}}.big5 b{{font:700 54px/1.25 'Crimson Text';display:block;margin-bottom:4px}}.big5 span{{font:500 15px/1.35 'DM Sans';color:#c9d3e6}}
.eq5{{font:600 15px/1.45 'DM Sans';color:{MU5}}}.eq5 b{{color:{NV5}}}
.mn5{{padding:14px 20px;display:flex;flex-direction:column;gap:8px;flex:none}}.mn5 .g{{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}}.mn5 .d{{display:flex;flex-direction:column;gap:4px}}.mn5 .d .hd{{display:flex;justify-content:space-between;align-items:baseline}}.mn5 .d b{{font:700 15px/1.3 'DM Sans'}}.mn5 .d em{{font:700 14px/1.3 'DM Sans';font-style:normal;color:{WET5}}}.mn5 .d em.ok{{color:{DRY5}}}
.bt5{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px;min-height:0}}
.lg5{{background:{NV5};color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;justify-content:space-between}}.lg5 .sm5{{color:#aab6cc}}.lg5 p{{font:500 18px/1.45 'DM Sans'}}.lg5 .ch{{display:flex;gap:8px;flex-wrap:wrap}}.lg5 .ch span{{background:#2c3f66;border-radius:8px;padding:5px 10px;font:600 15px/1.3 'DM Sans'}}
.nx5{{padding:16px 20px;display:flex;flex-direction:column;gap:6px;justify-content:space-between}}.nx5 .r{{display:flex;justify-content:space-between;gap:10px;border-top:1px solid #ece8e0;padding-top:6px;font:500 17px/1.35 'DM Sans'}}.nx5 .r b{{font-weight:700;text-align:right}}
""", "<div class=kk5>WATER DAMAGE RESTORATION · DRY-OUT LOG</div><h1>Moisture readings on a notepad?<br><span>Map every wet spot, every day.</span></h1>",
f'''<div class=w5><div class="cd5 pl5"><div class=l><span class=sm5>SAMPLE HOME · DAY 4 · {DAYS5[3].upper()} · SAMPLE READINGS</span>{plan5()}</div>
<div class=r><div class=lgx5><div><i style="background:{WET5}"></i>Wet · over 30</div><div><i style="background:{DAMP5}"></i>Drying · 16 to 30</div><div><i style="background:{DRY5}"></i>Dry · {GOAL5} or less</div></div>
<div class=big5><b>{WETN5[3]} of {len(PTS5)}</b><span>points still above your dry goal of {GOAL5}</span></div><div class=eq5><b>AM</b> air mover · <b>DH</b> dehumidifier</div></div></div>
<div class="cd5 mn5"><span class=sm5>SAME 8 POINTS · DAY BY DAY</span><div class=g>{"".join(f'<div class=d><div class=hd><b>Day {i + 1} · {DAYS5[i][:3]}</b><em class="{"ok" if WETN5[i] < 4 else ""}">{WETN5[i]} wet</em></div>{plan5(S=9, d=i, mini=True)}</div>' for i in range(4))}</div></div>
<div class=bt5><div class=lg5><span class=sm5>DAILY LOG · SENT AT 6 PM</span><p>Readings, photos and equipment for each day, shared with the homeowner and their insurance adjuster.</p><div class=ch><span>8 points</span><span>4 days</span><span>12 photos</span></div></div>
<div class="cd5 nx5"><span class=sm5>NEXT VISIT · TUE 24 NOV · 9 AM</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Re-check", "P1, P6, P7"), ("Keep running", "2 air movers, 1 DH"), ("Pick up", "Air mover by P3"), ("Loss date", DAYS5[0])])}</div></div></div>''',
NV5, "Do water damage jobs? DM us", f"background:{WET5};color:#fff")
