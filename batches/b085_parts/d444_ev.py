
# ───────── 444 INDIA · EV charging station · SINGLE · TeX Gyre Adventor + Source Sans 3 · asphalt / electric lime / cyan
# New technique: dark-mode top-down charging bays (CSS stall lines + SVG cars with charge % rings) feeding a 2 PM-8 PM bay
# timeline with a live "now" line; the phone booking takes the free gap in the same timeline.
AS4 = "#1a1e22"; LM4 = "#c8f03c"; CY4 = "#3cc6df"; MU4 = "#9aa3ab"; CD4 = "#252a30"
NOW4 = 15 * 60 + 40
def tm4(m): h, mm = divmod(m, 60); return f"{(h - 1) % 12 + 1}:{mm:02d} {'AM' if h < 12 else 'PM'}"
BAYS4 = [("Bay 1", "DC 60 kW", "charging", 68, 16 * 60 + 15, "#e8e4da"), ("Bay 2", "DC 60 kW", "free", 0, 0, ""), ("Bay 3", "AC 7.4 kW", "charging", 35, 19 * 60 + 10, "#5b7fa6"), ("Bay 4", "DC 30 kW", "booked", 0, 16 * 60, "")]
SL4 = {"Bay 1": [(30, 75, "done"), (80, 135, "on")], "Bay 2": [(0, 50, "done"), (150, 195, "new"), (270, 315, "bk")],
       "Bay 3": [(70, 310, "on")], "Bay 4": [(15, 90, "done"), (120, 165, "bk"), (210, 255, "bk")]}
T0 = 14 * 60; SPAN4 = 360
for b, sl in SL4.items():
    for a, e, k in sl: assert not (k == "on" and not (T0 + a <= NOW4 <= T0 + e))
def car4(col, pc):
    return f'''<svg viewBox="0 0 100 180" style="display:block;width:86px;height:auto"><rect x="10" y="8" width="80" height="164" rx="26" fill="{col}"/><path d="M20 52 Q50 36 80 52 L76 74 H24 Z" fill="#2c3540"/><rect x="24" y="80" width="52" height="56" rx="10" fill="{col}" stroke="#00000022" stroke-width="2"/><path d="M24 142 H76 L80 158 Q50 166 20 158 Z" fill="#2c3540"/></svg>'''
def bay4(n, kind, st, pc, end, col):
    if st == "charging":
        inner = f'{car4(col, pc)}<div class=pc4 style="background:conic-gradient({LM4} 0 {pc}%,#3a424a {pc}% 100%)"><b>{pc}%</b></div>'
        info = f'<em class=on>Charging</em><span>till {tm4(end)}</span>'
    elif st == "free":
        inner = '<div class=fr4>FREE</div>'; info = '<em class=fr>Free now</em><span>next 4:30 PM</span>'
    else:
        inner = '<div class=bk4>Booked</div>'; info = f'<em class=bk>Arriving</em><span>at {tm4(end)}</span>'
    return f'<div class=by4><div class=pt><i></i>{n}</div><small>{kind}</small><div class=st>{inner}</div>{info}</div>'
def line4():
    hrs = "".join(f'<span style="left:{(h * 60 - T0) / SPAN4 * 100:.2f}%">{tm4(h * 60).replace(":00", "")}</span>' for h in range(14, 21, 2))
    rows = "".join(f'''<div class=lr><b>{b}</b><div class=tr>{"".join(f'<i class="{k}" style="left:{a / SPAN4 * 100:.2f}%;width:{(e - a) / SPAN4 * 100:.2f}%">{"" if k == "done" else tm4(T0 + a)[:-3]}</i>' for a, e, k in sl)}</div></div>''' for b, sl in SL4.items())
    nowp = (NOW4 - T0) / SPAN4 * 100
    return f'<div class=tl4><div class=ax><b></b><div class=hx>{hrs}</div></div>{rows}<div class=nw style="left:calc(96px + (100% - 96px) * {nowp / 100:.4f})"><span>Now 3:40</span></div></div>'
PH4 = f'''<div class=ap4><span class=t>BOOK A CHARGER</span><b class=h>Sample Charging Point</b>
<div class=f><span>Car</span><b>Sample EV · CCS2</b></div>
<div class=f><span>Battery now → you want</span><div class=bb><i style="width:22%"></i><u style="left:80%"></u></div><div class=bl><b>22%</b><b>80%</b></div></div>
<div class=f><span>Charger</span><div class=ch><em class=on>DC 60 kW</em><em>DC 30 kW</em><em>AC 7.4 kW</em></div></div>
<div class=f><span>Today · Mon 23 Nov</span><div class=ch><em class=on>4:30 PM</em><em>5:15 PM</em><em class=x>6:30 PM</em></div></div>
<div class=f><span>Time needed · sample</span><b>About 45 min · till 5:15 PM</b></div>
<div class=f><span>Bay</span><b>Bay 2 · DC 60 kW</b></div>
<div class=f><span>Pay</span><b>At the station, by UPI</b></div>
<div class=nt>Reminder 10 min before your slot</div><div class=bt>Book Bay 2 · 4:30 PM</div></div>'''
CNT4 = {k: sum(1 for sl in SL4.values() for x in sl if x[2] in ks) for k, ks in [("Done", ("done",)), ("Charging", ("on",)), ("Booked", ("bk", "new"))]}
ST4 = "".join(f'<div><b>{v}</b><span>{k}</span></div>' for k, v in CNT4.items())
P["p444_ev"] = page(f"""
body{{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:radial-gradient(800px 600px at 100% 0%,#23303a 0%,rgba(35,48,58,0) 70%),{AS4};color:#fff}}
.kk4{{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:{LM4};margin-top:22px}}
h1{{font-family:'TeX Gyre Adventor';font-weight:700;font-size:56px;line-height:1.22;letter-spacing:-1px;margin-top:12px}} h1 span{{color:{LM4}}}
.w4{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 362px;gap:18px;min-height:0}}
.rc4{{display:flex;flex-direction:column;gap:16px}}.sm4b{{flex:1;justify-content:center}}.sm4b .g{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}.sm4b .g div{{background:#1e2328;border-radius:12px;padding:8px 10px;display:flex;flex-direction:column}}.sm4b b{{font:700 34px/1.3 'TeX Gyre Adventor';color:{LM4}}}.sm4b .g span{{font:600 15px/1.3 'Source Sans 3';color:#d5dade}}
.lc4{{display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm4{{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:{MU4}}}
.cd4{{background:{CD4};border-radius:22px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}}
.bys{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;border-top:4px solid #e8e4da;background:repeating-linear-gradient(90deg,transparent 0 2px,transparent 2px)}}
.by4{{display:flex;flex-direction:column;align-items:center;gap:6px;padding:10px 4px 6px;border-left:3px dashed #59616a}}.by4:last-child{{border-right:3px dashed #59616a}}
.by4 .pt{{display:flex;align-items:center;gap:6px;font:700 17px/1.3 'Source Sans 3'}}.by4 .pt i{{width:14px;height:22px;border-radius:4px;background:{LM4}}}.by4 small{{font:600 14px/1.3 'Source Sans 3';color:{MU4}}}
.by4 .st{{height:200px;width:100%;position:relative;display:flex;align-items:center;justify-content:center}}
.pc4{{position:absolute;bottom:4px;right:6px;width:56px;height:56px;border-radius:50%;display:flex;align-items:center;justify-content:center}}.pc4 b{{width:42px;height:42px;border-radius:50%;background:{AS4};display:flex;align-items:center;justify-content:center;font:700 14px/1 'Source Sans 3'}}
.fr4{{width:86px;height:164px;border:3px dashed {LM4};border-radius:24px;display:flex;align-items:center;justify-content:center;font:700 18px/1 'TeX Gyre Adventor';color:{LM4};letter-spacing:2px}}
.bk4{{width:86px;height:164px;border:3px dashed {CY4};border-radius:24px;display:flex;align-items:center;justify-content:center;font:700 16px/1 'Source Sans 3';color:{CY4}}}
.by4 em{{font:700 16px/1.3 'Source Sans 3';font-style:normal;padding:3px 10px;border-radius:8px}}.by4 em.on{{background:{LM4};color:{AS4}}}.by4 em.fr{{border:2px solid {LM4};color:{LM4}}}.by4 em.bk{{background:{CY4};color:{AS4}}}.by4>span{{font:600 15px/1.3 'Source Sans 3';color:#d5dade}}
.tlc{{flex:1;min-height:0}}.tl4{{flex:1;display:flex;flex-direction:column;gap:8px;position:relative}}
.tl4 .ax{{display:flex}}.tl4 .ax>b{{width:96px;flex:none}}.tl4 .hx{{flex:1;position:relative;height:22px}}.tl4 .hx span{{position:absolute;top:0;transform:translateX(-50%);font:600 14px/1.4 'Source Sans 3';color:{MU4};white-space:nowrap}}.tl4 .hx span:first-child{{transform:none}}.tl4 .hx span:last-child{{transform:translateX(-100%)}}
.tl4 .lr{{flex:1;display:flex;align-items:center}}.tl4 .lr>b{{width:96px;flex:none;font:700 17px/1.3 'Source Sans 3'}}.tl4 .tr{{flex:1;height:100%;max-height:56px;position:relative;z-index:1;background:#1e2328;border-radius:8px}}
.tl4 .tr i{{position:absolute;top:5px;bottom:5px;border-radius:6px;display:flex;align-items:center;padding-left:9px;font:700 15px/1 'Source Sans 3';font-style:normal;color:{AS4}}}.tl4 i.done{{background:#3d454d}}.tl4 i.on{{background:{LM4}}}.tl4 i.bk{{background:{CY4}}}.tl4 i.new{{background:repeating-linear-gradient(45deg,{LM4} 0 6px,#9fc12c 6px 12px);outline:2px solid #fff}}
.tl4 .nw{{position:absolute;top:24px;bottom:0;width:0;border-left:2px dashed #ff8a5c;z-index:0}}.tl4 .nw span{{position:absolute;bottom:-26px;left:0;transform:translateX(-50%);font:700 13px/1.3 'Source Sans 3';color:#ff8a5c;white-space:nowrap}}
.lg4{{display:flex;gap:16px;flex-wrap:wrap;margin-top:18px}}.lg4 span{{display:flex;align-items:center;gap:6px;font:600 15px/1.3 'Source Sans 3';color:#d5dade}}.lg4 i{{width:16px;height:16px;border-radius:4px}}
.ap4{{flex:1;padding:6px 18px 16px;display:flex;flex-direction:column;gap:9px;color:#15181b}}.ap4 .t{{font:700 12px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b737a}}.ap4 .h{{font:700 21px/1.3 'TeX Gyre Adventor'}}
.ap4 .f{{display:flex;flex-direction:column;gap:4px;border-top:1px solid #eceff1;padding-top:7px}}.ap4 .f>span{{font:600 13px/1.3 'Source Sans 3';color:#6b737a}}.ap4 .f>b{{font:700 17px/1.3 'Source Sans 3'}}
.ap4 .bb{{height:14px;border-radius:7px;background:#e7ebee;position:relative}}.ap4 .bb i{{position:absolute;left:0;top:0;bottom:0;border-radius:7px;background:#e0533a}}.ap4 .bb u{{position:absolute;top:0;bottom:0;width:4px;border-radius:2px;background:#15181b}}
.ap4 .bl{{display:flex;justify-content:space-between;font:700 14px/1.3 'Source Sans 3'}}.ap4 .bl b:first-child{{color:#e0533a}}
.ap4 .ch{{display:flex;gap:6px}}.ap4 .ch em{{flex:1;text-align:center;font:700 14px/1.2 'Source Sans 3';font-style:normal;padding:8px 2px;border-radius:9px;background:#eef1f3}}.ap4 .ch em.on{{background:#15181b;color:{LM4}}}.ap4 .ch em.x{{color:#a5adb3;text-decoration:line-through}}
.ap4 .nt{{font:600 14px/1.3 'Source Sans 3';color:#4b7f12;background:#eef8d6;border-radius:9px;padding:7px 10px}}.ap4 .bt{{background:{LM4};color:#15181b;border-radius:14px;padding:13px;text-align:center;font:700 17px/1.2 'TeX Gyre Adventor'}}
""", "<div class=kk4>EV CHARGING STATION</div><h1>“Is a charger free?” calls?<br><span>Show live bays, take bookings.</span></h1>",
f'''<div class=w4><div class=lc4><div class=cd4><span class=sm4>LIVE BAYS · MON 23 NOV · 3:40 PM · SAMPLE</span><div class=bys>{"".join(bay4(*b) for b in BAYS4)}</div></div>
<div class="cd4 tlc"><span class=sm4>TODAY · 2 PM TO 8 PM</span>{line4()}<div class=lg4>{"".join(f'<span><i style="background:{c}"></i>{t}</span>' for c, t in [("#3d454d", "Done"), (LM4, "Charging"), (CY4, "Booked"), (f"repeating-linear-gradient(45deg,{LM4} 0 4px,#9fc12c 4px 8px)", "New booking")])}</div></div></div>
<div class=rc4>{phone(PH4, w=362, h=716)}<div class="cd4 sm4b"><span class=sm4>TODAY SO FAR</span><div class=g>{ST4}</div></div></div></div>''',
"#fff", "Run a charging point? DM us", f"background:{LM4};color:{AS4}")
