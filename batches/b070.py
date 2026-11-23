import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n} {w if n == 1 else (ws or w + 's')}"
def hm(m): h, mm = divmod(int(round(m)), 60); return f"{(h - 1) % 12 + 1}:{mm:02d}"


# ───────── 366 INDIA · CNC laser cutting job shop · SINGLE · Bitter + Source Sans 3 · spark orange / sheet steel / graphite
# New technique: Gantt-style machine queue — one lane per machine, job blocks sized by qty / machine rate, a hatched
# sheet-change block when the material changes, a red "now" line; job slip + ready message computed from the schedule.
T0, T1 = 10 * 60, 13 * 60  # 10:00 to 1:00
LANES6 = [("Laser 1", "MS sheet, 2 to 6 mm", 6, "sheet", [(41, "MS 3 mm", 3), (42, "MS 3 mm", 2), (44, "MS 5 mm", 4), (47, "MS 5 mm", 3), (50, "MS 3 mm", 3)]),
          ("Laser 2", "SS sheet, 1 to 2 mm", 8, "sheet", [(43, "SS 1.5 mm", 3), (45, "SS 1.5 mm", 4), (48, "SS 1 mm", 3), (51, "SS 2 mm", 4), (54, "SS 2 mm", 3)]),
          ("Bending", "Press brake", 60, "part", [(46, "Brackets", 25), (49, "Brackets", 20), (52, "Panels", 30), (55, "Panels", 20), (56, "Clips", 25)])]
NOW6 = 11 * 60 + 45
SCH6 = []
for ln, kind, rate, unit, toks in LANES6:
    t, prev, row = T0, None, []
    for no, g, q in toks:
        if prev and prev != g:
            row.append(("clean", None, None, t, t + 10)); t += 10
        d = q / rate * 60
        row.append(("job", no, (g, q, unit), t, t + d)); t += d; prev = g
    SCH6.append((ln, kind, rate, unit, row))
JOBS6 = {b[1]: (ln, b[2][0], b[2][1], b[3], b[4], b[2][2]) for ln, k, r, u, row in SCH6 for b in row if b[0] == "job"}
def st6(a, b): return "done" if b <= NOW6 else ("now" if a < NOW6 else "wait")
READY6 = sorted([n for n, v in JOBS6.items() if v[4] <= NOW6])
SHEETS6 = sum(v[2] for v in JOBS6.values() if v[5] == "sheet")
SLIP6 = 50; SJ6 = JOBS6[SLIP6]
MSG6 = max([n for n in READY6 if JOBS6[n][5] == "sheet"], key=lambda n: JOBS6[n][4])
PX6 = 756 / (T1 - T0)
def blk6(b):
    typ, no, gk, a, e = b
    L, W = (a - T0) * PX6, (e - a) * PX6 - 4
    if typ == "clean":
        return f'<div class="b6 cl6" style="left:{L:.0f}px;width:{W:.0f}px"></div>'
    s = st6(a, e)
    return f'<div class="b6 {s}6" style="left:{L:.0f}px;width:{W:.0f}px"><b>J-{no}</b><span>{pl(gk[1], gk[2])}</span></div>'
P["p366_laser"] = page("""
body{--f:'Source Sans 3';--h:'Bitter';background:#eceff2;color:#23272e}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#d2551a;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-1px} h1 span{color:#e8631c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.gt6{flex:1;background:#fff;border-radius:26px;padding:18px 22px 16px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(40,48,58,.08);min-height:0}
.gh6{display:flex;justify-content:space-between;align-items:baseline}.gh6 small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7b7f86}.gh6 b{font:700 18px/1.4 'Source Sans 3';color:#c22a1d}
.ax6{display:grid;grid-template-columns:150px 756px;font:600 15px/1.3 'Source Sans 3';color:#7b7f86}.ax6>div{position:relative;height:20px}.ax6 span{position:absolute;top:0;transform:translateX(-50%)}.ax6 span:first-child{transform:none}.ax6 span:last-child{transform:translateX(-100%)}
.ln6{flex:1;display:grid;grid-template-columns:150px 756px;align-items:center;min-height:0;border-top:1px dashed #e3dccb}
.ln6>div:first-child b{display:block;font:800 22px/1.3 Bitter}.ln6>div:first-child span{font:500 15px/1.35 'Source Sans 3';color:#6c727a}.ln6>div:first-child em{display:block;font:600 14px/1.35 'Source Sans 3';font-style:normal;color:#d2551a}
.tr6{position:relative;height:128px;background:repeating-linear-gradient(90deg,#eef0f3 0 1px,transparent 1px 126px);border-radius:12px}
.b6{position:absolute;top:6px;bottom:6px;border-radius:10px;display:flex;flex-direction:column;justify-content:center;padding:0 5px;overflow:hidden;white-space:nowrap}
.b6 b{font:800 19px/1.25 Bitter}.b6 span{font:600 15px/1.3 'Source Sans 3'}
.done6{background:#d9dde3;color:#59606b}.now6{z-index:3;background:#f07a32;color:#2a1405;box-shadow:0 0 0 3px #fbd2b5}.wait6{background:#fff;border:2px solid #f07a32;color:#6b3410}
.cl6{background:repeating-linear-gradient(-45deg,#c8ccd3 0 4px,#eef0f3 4px 9px)}
.nw6{position:absolute;top:0;bottom:0;width:3px;z-index:2;background:#c22a1d;border-radius:2px}
.lgd6{display:flex;gap:22px;font:600 15px/1.4 'Source Sans 3';color:#4f5660}.lgd6 span{display:flex;align-items:center;gap:7px}.lgd6 i{width:22px;height:14px;border-radius:4px}
.bt6{display:grid;grid-template-columns:1fr 1.05fr 1.2fr;gap:14px}
.sl6{background:#fffdf6;border-radius:18px;padding:16px 20px 14px;border:2px dashed #b9c0c9;display:flex;flex-direction:column;gap:4px;position:relative}
.sl6 small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#d2551a}.sl6>b{font:800 40px/1.25 Bitter}
.sl6 div{display:flex;justify-content:space-between;font:600 17px/1.4 'Source Sans 3';border-top:1px solid #e3e7ec;padding-top:4px}.sl6 div span{color:#6c727a}
.ct6{background:#2c3440;color:#fff;border-radius:18px;padding:14px 18px;display:flex;flex-direction:column;justify-content:space-between;gap:6px}
.ct6 div{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(255,255,255,.12);padding-bottom:6px}.ct6 div:last-child{border:0;padding:0}
.ct6 span{font:500 17px/1.4 'Source Sans 3';color:#cfd5de}.ct6 b{font:800 30px/1.25 Bitter;color:#ff9a5c}
.ms6{background:#e7f6e9;border-radius:18px 18px 18px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;border:2px solid #bfe3c5}
.ms6{justify-content:space-between}.ms6 em{font:600 15px/1.4 'Source Sans 3';font-style:normal;color:#2f7a45}.ms6 small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#2f7a45}.ms6 p{font:500 19px/1.45 'Source Sans 3';color:#1f3a28;text-wrap:pretty}
""", "<div class=kk>CNC LASER CUTTING · JOB WORK QUEUE</div><h1>“When will my job be cut?”<br><span>Show every machine’s queue.</span></h1>",
f'''<div class=vw><div class=gt6><div class=gh6><small>TODAY · 3 MACHINES · SAMPLE</small><b>Now {hm(NOW6)}</b></div>
<div class=ax6><div></div><div>{"".join(f'<span style="left:{(t - T0) * PX6:.0f}px">{hm(t)}</span>' for t in range(T0, T1 + 1, 30))}</div></div>
{"".join(f'<div class=ln6><div><b>{ln}</b><span>{kind}</span><em>{rate} {unit}s an hour</em></div><div class=tr6>{"".join(blk6(b) for b in row)}<i class=nw6 style="left:{(NOW6 - T0) * PX6 - 1:.0f}px"></i></div></div>' for ln, kind, rate, unit, row in SCH6)}
<div class=lgd6><span><i class=done6></i>Done, ready</span><span><i class=now6></i>On the machine</span><span><i class=wait6 style="border-width:2px"></i>Waiting</span><span><i class=cl6></i>Sheet or tool change</span></div></div>
<div class=bt6><div class=sl6><small>JOB SLIP · SAMPLE</small><b>J-{SLIP6}</b><div><span>Material</span>{SJ6[1]} · {pl(SJ6[2], SJ6[5])}</div><div><span>{SJ6[0]}</span>Ready {hm(SJ6[4] + 5)}</div></div>
<div class=ct6><div><span>Jobs today</span><b>{len(JOBS6)}</b></div><div><span>Sheets today</span><b>{SHEETS6}</b></div><div><span>Ready to pick up</span><b>{len(READY6)}</b></div></div>
<div class=ms6><small>AUTO MESSAGE · {hm(JOBS6[MSG6][4] + 1)} AM</small><p>Job J-{MSG6}: your {pl(JOBS6[MSG6][2], "sheet")} of {JOBS6[MSG6][1]} are cut. Please pick them up today.</p><em>Sent by itself when a job is done.</em></div></div></div>''',
"#23272e", "Do laser cutting? DM us", "background:#e8631c;color:#fff")


# ───────── 367 INDIA · Battery dealer (car, bike, inverter) · CAROUSEL 6 · Archivo Black + DM Sans · graphite / acid lime / charge blue
# New techniques: CSS battery objects (terminals, label strip, charge cells), warranty timeline bar computed from sale
# date + months vs today, isotype of exchanged old batteries per type, one phone (slide 5 only).
import datetime as _dt
TODAY7 = _dt.date(2026, 11, 23)
def addm(d, m):
    y, mo = divmod(d.month - 1 + m, 12); y += d.year; mo += 1
    import calendar; return _dt.date(y, mo, min(d.day, calendar.monthrange(y, mo)[1]))
def fd(d): return f"{d.day} {d.strftime('%b')} {d.year}"
def mleft(a, b): return (b.year - a.year) * 12 + b.month - a.month - (1 if b.day < a.day else 0)
SALES7 = [("SN-24A-0187", "Car", "35 Ah", "98XXX XX123", _dt.date(2026, 1, 14), 24),
          ("SN-31C-0442", "Inverter", "150 Ah tubular", "97XXX XX408", _dt.date(2025, 6, 3), 36),
          ("SN-12B-0915", "Bike", "5 Ah", "99XXX XX761", _dt.date(2026, 8, 21), 18),
          ("SN-24A-0203", "Car", "45 Ah", "90XXX XX332", _dt.date(2024, 3, 9), 24),
          ("SN-31C-0518", "Inverter", "200 Ah tubular", "88XXX XX905", _dt.date(2026, 10, 2), 48),
          ("SN-12B-0977", "Bike", "9 Ah", "70XXX XX214", _dt.date(2025, 11, 30), 18)]
def bat(w=200, h=140, c="#2a3038", lab="#c6f432", sn="", cells=4, fill=4, cls=""):
    tw = max(14, w // 7)
    return (f'<div class="bt7 {cls}" style="width:{w}px"><div class=tm7><i style="width:{tw}px;height:{max(10, h // 9)}px;background:#d6dbe1"></i><i style="width:{tw}px;height:{max(10, h // 9)}px;background:#e9573f"></i></div>'
            f'<div class=bb7 style="height:{h}px;background:{c}"><div class=ls7 style="background:{lab}">{sn}</div>'
            f'<div class=ce7>{"".join(f"<i class={chr(34)}{"on" if k < fill else ""}{chr(34)}></i>" for k in range(cells))}</div></div></div>')
B7 = """
body{--f:'DM Sans';--h:'Archivo Black';background:#eef1f4;color:#1e2329}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#2f7cf6;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;line-height:1.22;letter-spacing:-1px} h1 span{color:#2f7cf6}
.bt7{display:flex;flex-direction:column;align-items:stretch;flex:none}.tm7{display:flex;justify-content:space-between;padding:0 16%}.tm7 i{display:block;border-radius:4px 4px 0 0}
.bb7{border-radius:14px;padding:12px;display:flex;flex-direction:column;justify-content:space-between;box-shadow:inset 0 -8px 0 rgba(0,0,0,.18)}
.ls7{border-radius:8px;font:700 15px/1.3 'DM Sans';color:#1e2329;padding:6px 10px;text-align:center;letter-spacing:.5px}
.ce7{display:flex;gap:6px}.ce7 i{flex:1;height:14px;border-radius:4px;background:rgba(255,255,255,.14)}.ce7 i.on{background:#c6f432}
.cd7{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(30,35,41,.08)}
.sm7{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#6c7480}
"""
def b7(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1e2329;color:#c6f432"):
    return page(B7 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1e2329", cta, ctacss, tagline=f"{n} / 6")

P["p367_battery_s1"] = b7(1, "BATTERY DEALER · CAR, BIKE, INVERTER", "“Battery died, bill is lost.”<br><span>Find it by serial number.</span>",
f'''<div class=w71><div class="cd7 st71"><div class=hb71><span class=sm7>LABEL ON THE BATTERY</span>{bat(340, 320, sn="SN-24A-0187", fill=1, cells=5)}<small>The serial is on every battery. Save it at the sale.</small></div>
<div class=ch71><div class="bu71 cu">Bought it here last year. The bill is lost somewhere.</div><div class="bu71 me">Which month? Which model? Let me check the bill books…</div>
<div class=bk71>{"".join(f'<div style="margin-left:{m}px;background:{c}"><b>Bill book {y}</b><span>{pg} pages</span></div>' for y, c, m, pg in [("2024", "#56606c", 0, 100), ("2025", "#3d4651", 22, 100), ("2026", "#2a3038", 8, 100)])}</div></div></div>
<div class=sw71>{"".join(f'<div><b>{i}</b><span>{t}</span></div>' for i, t in [(1, "Every sale saved"), (2, "Warranty in one search"), (3, "Old batteries counted"), (4, "Check-up reminders")])}</div></div>''',
css=""".w71{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.st71{flex:1;display:grid;grid-template-columns:400px 1fr;gap:20px;padding:26px;min-height:0}
.hb71{display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:22px;background:#e4e9ee;border-radius:20px;padding:20px}.hb71 small{font:600 18px/1.4 'DM Sans';color:#4a525d;text-align:center;text-wrap:balance}
.hb71 .ls7{font-size:26px;padding:14px}.hb71 .ce7 i{height:28px}.hb71 small{font-size:20px}
.ch71{display:flex;flex-direction:column;gap:20px;justify-content:center}.bu71{font:500 25px/1.45 'DM Sans';padding:18px 22px;border-radius:22px;text-wrap:pretty}
.bu71.cu{background:#1e2329;color:#fff;border-bottom-left-radius:6px}.bu71.me{background:#dfe9fd;color:#173c7a;border-bottom-right-radius:6px;margin-left:30px}
.bk71{display:flex;flex-direction:column;gap:6px;margin-top:6px}.bk71 div{color:#fff;border-radius:8px 14px 14px 8px;padding:16px 20px;display:flex;justify-content:space-between;width:330px;box-shadow:inset 8px 0 0 rgba(0,0,0,.25)}
.bk71 b{font:700 19px/1.3 'DM Sans'}.bk71 span{font:500 16px/1.3 'DM Sans';color:#cfd5dc}
.sw71{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.sw71 div{background:#1e2329;color:#fff;border-radius:18px;padding:14px 16px;display:flex;align-items:center;gap:12px}
.sw71 b{font:400 30px/1.3 'Archivo Black';color:#c6f432}.sw71 span{font:600 17px/1.35 'DM Sans'}""")

P["p367_battery_s2"] = b7(2, "1 · EVERY SALE SAVED", "Scan the serial at the sale.<br><span>Customer, model, warranty.</span>",
browser(f'''<div class=sh72><div class=nw72><span class=sm7>NEW SALE · SAMPLE</span><div class=fl72>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a, b in [("Serial", "SN-31C-0518 · scanned"), ("Model", "Inverter 200 Ah tubular"), ("Customer mobile", "88XXX XX905"), ("Warranty", "48 months")])}</div></div>
<div class=tb72><div class=hd72><span>Serial</span><span>Type</span><span>Model</span><span>Mobile</span><span>Sold</span><span>Warranty</span></div>
{"".join(f'<div class="rw72 {"nw" if i == 4 else ""}"><b>{sn}</b><span class="ty72 {t[0]}">{t}</span><span>{m}</span><span>{mob}</span><span>{fd(d)}</span><span>{w} mo</span></div>' for i, (sn, t, m, mob, d, w) in enumerate(SALES7))}</div></div>''', url="yourbatteryshop.in/sales", style="flex:1;min-height:0"),
css=""".sh72{flex:1;display:flex;flex-direction:column;gap:14px;padding:20px 22px;min-height:0}.nw72{background:#1e2329;border-radius:18px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}.nw72 .sm7{color:#c6f432}
.fl72{display:grid;grid-template-columns:1fr 1fr;gap:10px}.fl72 div{background:rgba(255,255,255,.08);border-radius:12px;padding:10px 14px}.fl72 small{display:block;font:500 14px/1.35 'DM Sans';color:#aeb6c0}.fl72 b{font:700 19px/1.35 'DM Sans';color:#fff}
.tb72{flex:1;display:flex;flex-direction:column;min-height:0}.hd72,.rw72{display:grid;grid-template-columns:1.3fr .9fr 1.45fr 1.25fr 1.15fr .8fr;gap:8px;align-items:center;padding:0 10px}
.hd72{font:700 14px/1.4 'DM Sans';letter-spacing:1px;color:#6c7480;padding-bottom:8px;border-bottom:2px solid #e4e8ed}
.rw72{flex:1;border-bottom:1px solid #eef1f4;font:500 17px/1.35 'DM Sans'}.rw72 b{font:700 17px/1.35 'DM Sans'}.rw72.nw{background:#f3fbd9;border-radius:10px}
.ty72{justify-self:start;border-radius:8px;padding:4px 10px;font-weight:700}.ty72.C{background:#dfe9fd;color:#1d4fb0}.ty72.I{background:#efe3fb;color:#6a2fb0}.ty72.B{background:#fde7d9;color:#a14812}""")

Q7 = SALES7[0]; Q7E = addm(Q7[4], Q7[5]); Q7L = mleft(TODAY7, Q7E)
O7 = SALES7[3]; O7E = addm(O7[4], O7[5])
def tl7(sale, end, ok):
    a, b = sale.toordinal(), end.toordinal(); t = min(max((TODAY7.toordinal() - a) / (b - a), 0), 1)
    tod = f'<i class=td73 style="left:{t * 100:.1f}%"></i>' if ok else ""
    lab = f'<div class=tq73><em style="left:{t * 100:.1f}%">Today</em></div>' if ok else ""
    return f'<div class=tl73>{lab}<div class="br73 {"ok" if ok else "ex"}"><i style="width:{t * 100:.1f}%"></i>{tod}</div><div class=dt73><span>Sold {fd(sale)}</span><span>Ends {fd(end)}</span></div></div>'
P["p367_battery_s3"] = b7(3, "2 · WARRANTY IN ONE SEARCH", "Type the serial.<br><span>Get the answer in seconds.</span>",
f'''<div class=w73><div class=sr73>{ic("search", 30)}<b>SN-24A-0187</b><span>Search</span></div>
<div class="cd7 rs73"><div class=hd73><div><span class=sm7>FOUND · SAMPLE</span><b>Car battery {Q7[2]}</b><small>Customer {Q7[3]} · {Q7[5]} months warranty</small></div><div class="ok73">IN WARRANTY<b>{pl(Q7L, "month")} left</b></div></div><div class=fx73>{"".join(f"<div><small>{x}</small><b>{y}</b></div>" for x, y in [("Bill no.", "B-0114"), ("Sold by", "Counter 1"), ("Next step", "Test and claim")])}</div>{tl7(Q7[4], Q7E, True)}</div>
<div class="cd7 rs73"><div class=hd73><div><span class=sm7>FOUND · SAMPLE</span><b>Car battery {O7[2]} · {O7[0]}</b><small>Customer {O7[3]} · {O7[5]} months warranty</small></div><div class="ex73">WARRANTY ENDED<b>on {fd(O7E)}</b></div></div><div class=fx73>{"".join(f"<div><small>{x}</small><b>{y}</b></div>" for x, y in [("Bill no.", "B-0309"), ("Sold by", "Counter 2"), ("Next step", "Show new models")])}</div>{tl7(O7[4], O7E, False)}</div>
<div class=nt73>No bill book search. The customer gets a clear answer at the counter.</div></div>''',
css=""".w73{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}.sr73{display:flex;align-items:center;gap:16px;background:#fff;border:3px solid #2f7cf6;border-radius:22px;padding:16px 16px 16px 22px;color:#2f7cf6}
.sr73 b{flex:1;font:700 30px/1.3 'DM Sans';color:#1e2329;letter-spacing:1px}.sr73 span{background:#2f7cf6;color:#fff;font:700 20px/1.2 'DM Sans';border-radius:14px;padding:14px 22px}
.rs73{flex:1;padding:22px 26px;display:flex;flex-direction:column;justify-content:space-between;gap:16px}.hd73{display:flex;justify-content:space-between;gap:16px}
.hd73 b{display:block;font:400 28px/1.3 'Archivo Black';margin-top:4px}.hd73 small{font:500 18px/1.4 'DM Sans';color:#5b636e}
.ok73,.ex73{flex:none;border-radius:18px;padding:12px 18px;font:700 14px/1.4 'DM Sans';letter-spacing:1.5px;text-align:right}.ok73{background:#eefbc9;color:#3f5a00}.ex73{background:#fde4df;color:#a3301b}
.ok73 b,.ex73 b{display:block;font:400 24px/1.3 'Archivo Black';letter-spacing:0;margin-top:2px}
.tl73{display:flex;flex-direction:column;gap:10px;padding-top:26px}.br73{position:relative;height:22px;border-radius:11px;background:#e4e8ed}.br73>i{position:absolute;left:0;top:0;bottom:0;border-radius:11px}
.br73.ok>i{background:linear-gradient(90deg,#9fcf1c,#c6f432)}.br73.ex>i{background:#e9573f}
.td73{position:absolute;top:0;bottom:0;width:4px;background:#1e2329;border-radius:2px}.tq73{position:relative;height:22px;margin-top:-26px}.tq73 em{position:absolute;top:0;transform:translateX(-50%);font:700 15px/1.3 'DM Sans';font-style:normal;white-space:nowrap}
.dt73{display:flex;justify-content:space-between;font:600 17px/1.4 'DM Sans';color:#5b636e}
.fx73{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.fx73 div{background:#f3f5f8;border-radius:14px;padding:10px 14px}.fx73 small{display:block;font:500 14px/1.35 'DM Sans';color:#6c7480}.fx73 b{font:700 19px/1.35 'DM Sans'}
.nt73{background:#1e2329;color:#fff;border-radius:20px;padding:18px 24px;font:600 22px/1.4 'DM Sans'}""")

OLD7 = [("Car", 14, "#2f7cf6"), ("Inverter", 9, "#8d4fe0"), ("Bike", 22, "#e98a2f")]
TOT7 = sum(q for _, q, _ in OLD7)
P["p367_battery_s4"] = b7(4, "3 · OLD BATTERIES COUNTED", "Old battery in, new one out.<br><span>Every exchange logged.</span>",
f'''<div class=w74><div class="cd7 is74"><div class=h74><span class=sm7>OLD BATTERIES TAKEN IN · NOVEMBER · SAMPLE</span><b>1 block = 1 battery</b></div>
{"".join(f'<div class=r74><div class=l74><b>{t}</b><span>{q}</span></div><div class=g74>{"".join(f"<i style={chr(34)}background:{c}{chr(34)}></i>" for _ in range(q))}</div></div>' for t, q, c in OLD7)}</div>
<div class=bt74><div class="cd7 sl74"><span class=sm7>EXCHANGE SLIP · SAMPLE</span>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in [("New battery", "SN-31C-0518"), ("Old battery in", "Inverter 150 Ah"), ("Date", "2 Oct 2026"), ("Customer", "88XXX XX905")])}</div>
<div class=pk74><span class=sm7>FOR THE RECYCLER PICKUP</span><b>{TOT7}</b><p>old batteries in the store room, counted by type. No guesswork at pickup.</p></div></div></div>''',
css=""".w74{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.is74{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:10px;min-height:0}.h74{display:flex;justify-content:space-between;align-items:baseline}.h74 b{font:700 16px/1.4 'DM Sans';color:#2f7cf6}
.r74{flex:1;display:grid;grid-template-columns:150px 1fr;gap:16px;align-items:center;border-top:1px solid #eef1f4}.l74 b{display:block;font:700 22px/1.3 'DM Sans'}.l74 span{font:400 40px/1.3 'Archivo Black'}
.g74{display:flex;flex-wrap:wrap;gap:8px}.g74 i{width:60px;height:42px;border-radius:7px;position:relative;box-shadow:inset 0 -5px 0 rgba(0,0,0,.2)}
.g74 i::before,.g74 i::after{content:"";position:absolute;top:-6px;width:10px;height:6px;background:#9aa3ae;border-radius:2px 2px 0 0}.g74 i::before{left:8px}.g74 i::after{right:8px;background:#e9573f}
.bt74{display:grid;grid-template-columns:1.15fr 1fr;gap:14px}.sl74{padding:18px 22px;display:flex;flex-direction:column;gap:6px}.sl74 div{display:flex;justify-content:space-between;border-top:1px dashed #d8dde3;padding-top:6px;font:500 18px/1.4 'DM Sans'}.sl74 div span{color:#5b636e}
.pk74{background:#1e2329;color:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:2px}.pk74 .sm7{color:#c6f432}.pk74 b{font:400 60px/1.3 'Archivo Black';color:#c6f432}.pk74 p{font:500 19px/1.45 'DM Sans';color:#dfe4ea}""")

DUE7 = [("Mon", "Inverter 150 Ah", "Sector 4"), ("Tue", "Inverter 200 Ah", "Old town"), ("Wed", "Inverter 150 Ah", "Sector 9"), ("Thu", "Inverter 100 Ah", "Station road"), ("Sat", "Inverter 150 Ah", "Sector 4")]
P["p367_battery_s5"] = b7(5, "4 · CHECK-UP REMINDERS", "Water level check due?<br><span>The app sends the reminder.</span>",
f'''<div class=w75>{phone(f"""<div class=ap75><div class=ah75><i>Y</i><div><b>Your Battery Shop</b><small>Business account · sample</small></div></div>
<div class=ms75><div class=in75>Hello! Your inverter battery (SN-31C-0442) was last checked 6 months ago. It is time for a water level check.<em>10:00 AM</em></div>
<div class=in75>Reply 1 to book a home visit this week.<em>10:00 AM</em></div><div class=ou75>1<em>10:12 AM</em></div>
<div class=in75>Booked for Tuesday, 11 AM to 1 PM. Our technician will call before coming.<em>10:12 AM</em></div></div></div>""", w=380, h=740)}
<div class=sd75><div class="cd7 vl75"><span class=sm7>CHECK-UP VISITS · THIS WEEK · SAMPLE</span>{"".join(f'<div><b>{d}</b><div><strong>{m}</strong><span>{a}</span></div></div>' for d, m, a in DUE7)}</div>
<div class=nt75>Every sale sets its next check-up date. Nobody has to remember.</div></div></div>''',
css=""".w75{flex:1;display:flex;gap:26px;align-items:center;min-height:0}.ap75{flex:1;display:flex;flex-direction:column;background:#e9e4dc}
.ah75{display:flex;gap:10px;align-items:center;background:#1e2329;color:#fff;padding:10px 14px}.ah75 i{width:38px;height:38px;border-radius:50%;background:#c6f432;color:#1e2329;font:700 18px/38px 'DM Sans';font-style:normal;text-align:center}
.ah75 b{display:block;font:700 16px/1.3 'DM Sans'}.ah75 small{font:500 12px/1.3 'DM Sans';color:#b9c1cb}
.ms75{flex:1;display:flex;flex-direction:column;gap:10px;padding:14px 12px}.in75,.ou75{font:500 17px/1.42 'DM Sans';padding:10px 12px 8px;border-radius:14px;max-width:88%;text-wrap:pretty}
.in75{background:#fff;align-self:flex-start;border-top-left-radius:4px}.ou75{background:#d9f7be;align-self:flex-end;border-top-right-radius:4px}
.in75 em,.ou75 em{display:block;text-align:right;font:500 11px/1.3 'DM Sans';font-style:normal;color:#7a8290;margin-top:4px}
.sd75{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}.vl75{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:6px}
.vl75>div{flex:1;display:flex;gap:14px;align-items:center;border-top:1px solid #eef1f4}.vl75>div>b{width:58px;height:58px;flex:none;border-radius:16px;background:#dfe9fd;color:#1d4fb0;font:700 18px/58px 'DM Sans';text-align:center}
.vl75 strong{display:block;font:700 19px/1.35 'DM Sans'}.vl75 span{font:500 16px/1.35 'DM Sans';color:#5b636e}
.nt75{background:#1e2329;color:#fff;border-radius:20px;padding:18px 22px;font:600 20px/1.45 'DM Sans'}""")

P["p367_battery_s6"] = b7(6, "YOUR TURN", "Sell batteries?<br><span>Let's build your shop app.</span>",
f'''<div class=w76><div class="cd7 bs76"><div class=tx76><span class=sm7>ONE APP FOR</span><b>Car, inverter and bike batteries</b></div><div class=qa76>{"".join(f"<i>{q}</i>" for q in ["Is my battery still in warranty?", "When is my next check-up?", "Do you take old batteries?"])}</div><div class=rw76>{bat(140, 150, sn="CAR", fill=3)}{bat(170, 210, lab="#ffd48a", sn="INVERTER", fill=4)}{bat(96, 96, lab="#bcd3ff", sn="BIKE", fill=2, cells=3)}</div></div>
<div class=td76>{"".join(f'<div class=ti76><span class=ib>{ic(i, 30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("qr", "Sale by serial", "Scan, save, done"), ("shield", "Warranty search", "Answer at the counter"), ("box", "Exchange log", "Old batteries counted"), ("bell", "Check-up reminders", "Sent by the app")])}</div>
<div class=q76>How do you check warranty at your shop today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#2f7cf6;color:#fff",
css=""".w76{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.bs76{display:flex;flex-direction:column;justify-content:space-between;padding:28px 22px 30px;background:linear-gradient(#fff 82%,#e4e9ee 82%)}.rw76{display:flex;align-items:flex-end;justify-content:center;gap:14px}.qa76{display:flex;flex-direction:column;gap:10px}.qa76 i{font:600 19px/1.4 'DM Sans';font-style:normal;background:#dfe9fd;color:#173c7a;border-radius:16px 16px 16px 4px;padding:12px 16px;align-self:flex-start}.qa76 i:nth-child(2){align-self:flex-end;border-radius:16px 16px 4px 16px}.tx76 b{display:block;font:400 36px/1.3 'Archivo Black';margin-top:8px}
.td76{display:flex;flex-direction:column;gap:12px}.ti76{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(30,35,41,.07)}
.ti76 .ib{width:58px;height:58px;border-radius:18px;background:#1e2329;color:#c6f432}.ti76 b{display:block;font:700 25px/1.3 'DM Sans'}.ti76 div span{font:500 18px/1.4 'DM Sans';color:#4f5761}
.q76{grid-column:1 / 3;background:#1e2329;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'DM Sans'}""")


# ───────── 368 USA · Fall leaf cleanup · SINGLE · Cardo + Montserrat · maple orange / pine green / kraft
# New technique: top-down SVG street of lots, each with a house, tree crowns and seeded leaf scatter (density from
# tree count); booked lots get a day-coloured outline + day chip; the route list and counts come from the same lots.
random.seed(368)
LOTS8 = [(12, "N", 3, "Tue", "M"), (14, "N", 1, None, "S"), (18, "N", 4, "Tue", "L"), (22, "N", 2, "Thu", "M"),
         (13, "S", 2, None, "S"), (17, "S", 5, "Thu", "L"), (21, "S", 3, "Tue", "M"), (27, "S", 2, "Thu", "M")]
DC8 = {"Tue": "#2f5d46", "Thu": "#d9622b"}
def lots8():
    W, out = 880, []
    lw, gap = 200, 20
    for i, (no, side, trees, day, ys) in enumerate([l for l in LOTS8 if l[1] == "N"] + [l for l in LOTS8 if l[1] == "S"]):
        col = i % 4; x = 10 + col * (lw + gap); y = 10 if side == "N" else 250
        g = [f'<rect x="{x}" y="{y}" width="{lw}" height="170" rx="10" fill="#b9cf8f"/>']
        hx, hy = x + 66, (y + 104 if side == "N" else y + 12)
        for _ in range(trees * 16):
            lx, ly = x + 8 + random.random() * (lw - 16), y + 8 + random.random() * 154
            g.append(f'<ellipse cx="{lx:.0f}" cy="{ly:.0f}" rx="5" ry="3" transform="rotate({random.randint(0, 180)} {lx:.0f} {ly:.0f})" fill="{random.choice(["#d9622b", "#e8a03a", "#b8461e"])}"/>')
        g.append(f'<rect x="{hx}" y="{hy}" width="68" height="54" rx="4" fill="#efe3cc" stroke="#6b5a45" stroke-width="2"/><line x1="{hx}" y1="{hy + 27}" x2="{hx + 68}" y2="{hy + 27}" stroke="#6b5a45" stroke-width="2"/>')
        spots = [(x + 30, y + 38), (x + 170, y + 38), (x + 100, y + 34), (x + 30, y + 86), (x + 170, y + 86)] if side == "N" else [(x + 30, y + 132), (x + 170, y + 132), (x + 100, y + 136), (x + 30, y + 84), (x + 170, y + 84)]
        for tx, ty in spots[:min(trees, 5)]:
            g.append(f'<circle cx="{tx}" cy="{ty}" r="22" fill="#2f5d46" opacity=".92"/><circle cx="{tx - 6}" cy="{ty - 6}" r="9" fill="#4d7f5f"/>')
        if day:
            g.append(f'<rect x="{x + 3}" y="{y + 3}" width="{lw - 6}" height="164" rx="9" fill="none" stroke="{DC8[day]}" stroke-width="6"/>')
            g.append(f'<rect x="{x + lw - 70}" y="{y + (12 if side == "S" else 120)}" width="58" height="34" rx="17" fill="{DC8[day]}"/><text x="{x + lw - 41}" y="{y + (35 if side == "S" else 143)}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="17" fill="#fff">{day}</text>')
        g.append(f'<text x="{x + 12}" y="{y + (160 if side == "N" else 30)}" font-family="Montserrat" font-weight="800" font-size="20" fill="#1f2a22" paint-order="stroke" stroke="#f3ecd9" stroke-width="5">{no}</text>')
        out.append("".join(g))
    road = '<rect x="0" y="186" width="880" height="58" fill="#5d6168"/><line x1="0" y1="215" x2="880" y2="215" stroke="#f3d27a" stroke-width="4" stroke-dasharray="26 18"/><rect x="300" y="200" width="280" height="30" rx="8" fill="#5d6168"/><text x="440" y="222" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="18" fill="#fff" letter-spacing="3">SAMPLE MAPLE AVE</text>'
    return f'<svg viewBox="0 0 880 430" style="width:100%;height:auto;display:block">{road}{"".join(out)}</svg>'
BK8 = {d: sorted([l for l in LOTS8 if l[3] == d], key=lambda l: l[0]) for d in DC8}
NB8 = sum(len(v) for v in BK8.values())
YS8 = {"S": "Small", "M": "Medium", "L": "Large"}
P["p368_leaves"] = page("""
body{--f:'Montserrat';--h:'Cardo';background:#efe3cc;color:#1f2a22}
.kk{font:700 15px/1.4 Montserrat;letter-spacing:3px;color:#b8461e;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#d9622b;font-style:italic}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.mp8{background:#fffaf0;border-radius:26px;padding:16px 18px 14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(31,42,34,.1)}
.mh8{display:flex;justify-content:space-between;align-items:center}.mh8 small{font:700 13px/1.4 Montserrat;letter-spacing:2px;color:#6b5a45}
.mh8 div{display:flex;gap:14px;font:600 14px/1.4 Montserrat}.mh8 span{display:flex;align-items:center;gap:6px}.mh8 i{width:16px;height:16px;border-radius:5px}
.bt8{flex:1;display:grid;grid-template-columns:1.08fr 1fr;gap:14px;min-height:0}
.fm8{flex:1;padding:18px 18px;display:flex;flex-direction:column;justify-content:space-between;gap:10px}.fm8 label{font:700 13px/1.3 Montserrat;letter-spacing:1.5px;color:#6b5a45;display:block;margin-bottom:5px}
.ch8{display:flex;gap:8px}.ch8 i{flex:1;text-align:center;font:600 16px/1.3 Montserrat;font-style:normal;border:2px solid #d9cdb5;border-radius:12px;padding:9px 4px;color:#4a4538}.ch8 i.on{background:#2f5d46;border-color:#2f5d46;color:#fff}
.in8{border:2px solid #d9cdb5;border-radius:12px;padding:9px 12px;font:600 16px/1.3 Montserrat}
.sb8{background:#d9622b;color:#fff;border-radius:14px;padding:12px;text-align:center;font:700 17px/1.3 Montserrat}
.rt8{display:flex;flex-direction:column;gap:12px}.dy8{flex:1;border-radius:22px;padding:14px 18px;color:#fff;display:flex;flex-direction:column;gap:8px}
.dy8 small{font:700 13px/1.4 Montserrat;letter-spacing:2px;opacity:.85}.dy8 b{font:700 30px/1.25 Cardo}.dy8 div{display:flex;flex-wrap:wrap;gap:6px}
.dy8 div i{font:600 15px/1.3 Montserrat;font-style:normal;background:rgba(255,255,255,.18);border-radius:10px;padding:6px 10px}
.nt8{background:#fffaf0;border-radius:18px;padding:12px 16px;font:600 16px/1.45 Montserrat;color:#3c3a30}
""", "<div class=kk>FALL LEAF CLEANUP · SERVICE AREA</div><h1>Leaf cleanup calls piling up?<br><span>Book by yard, route by street.</span></h1>",
f'''<div class=vw><div class=mp8><div class=mh8><small>BOOKINGS ON ONE STREET · SAMPLE</small><div>{"".join(f'<span><i style="background:{c}"></i>{d}</span>' for d, c in DC8.items())}<span><i style="background:#b9cf8f"></i>Not booked</span></div></div>{lots8()}</div>
<div class=bt8>{browser(f"""<div class=fm8><div><label>YARD SIZE</label><div class=ch8><i>Small</i><i class=on>Medium</i><i>Large</i></div></div>
<div><label>TREES ON THE LOT</label><div class=ch8><i>1–2</i><i class=on>3–4</i><i>5+</i></div></div>
<div><label>LEAVES</label><div class=ch8><i class=on>Bag and haul</i><i>Mulch in</i></div></div>
<div class=sb8>Send my yard details</div></div>""", url="yourleafcrew.com/quote", style="display:flex;flex-direction:column")}
<div class=rt8>{"".join(f'<div class=dy8 style="background:{DC8[d]}"><small>{"TUESDAY" if d == "Tue" else "THURSDAY"} ROUTE</small><b>{pl(len(v), "yard")}, one street</b><div>{"".join(f"<i>{l[0]} · {YS8[l[4]]}</i>" for l in v)}</div></div>' for d, v in BK8.items())}
<div class=nt8>We text each customer a quote and their day. {NB8} of {len(LOTS8)} yards on Maple Ave are booked.</div></div></div></div>''',
"#1f2a22", "Run a yard crew? DM us", "background:#2f5d46;color:#fff")


# ───────── 369 INDIA · Fridge and washing machine repair · SINGLE · Montserrat + Roboto · ice blue / compressor copper / deep navy
# New technique: CSS double-door fridge drawn with numbered callout pins that match the numbered fields in the
# booking card; the technician's day list and "parts to carry" are counted from the same job list.
JOBS9 = [("J-2611", "10–12", "Sector 7", "Fridge, double door", "Not cooling", "Thermostat"),
         ("J-2612", "12–2", "Old market", "Washing machine, top load", "Drum not spinning", "Belt"),
         ("J-2613", "2–4", "Sector 3", "Fridge, single door", "Door not closing", "Door gasket"),
         ("J-2614", "4–5", "Station road", "Fridge, double door", "Ice on back wall", "Thermostat"),
         ("J-2615", "5–6", "Sector 7", "Washing machine, front load", "Water not draining", "Drain pump")]
from collections import Counter as _C
PARTS9 = _C(j[5] for j in JOBS9)
P["p369_fridge"] = page("""
body{--f:'Roboto';--h:'Montserrat';background:#e3f1f8;color:#12324a}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#c4682c;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#c4682c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp9{flex:1;display:grid;grid-template-columns:330px 1fr;gap:16px;min-height:0}
.fz9{background:#fff;border-radius:26px;padding:20px 24px 16px;display:flex;flex-direction:column;align-items:center;gap:12px;box-shadow:0 14px 30px rgba(18,50,74,.08)}
.fz9 small,.jc9 small,.rt9 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#5f7686}
.fb9{flex:1;width:230px;position:relative;border-radius:22px;background:linear-gradient(90deg,#c9d6df,#eef3f6 40%,#d4dee5);box-shadow:inset 0 0 0 3px #a9bac6;display:flex;flex-direction:column;padding:10px;gap:8px}
.fb9 .dr{border-radius:14px;background:linear-gradient(90deg,#dbe4ea,#f6f9fb 45%,#e0e8ee);box-shadow:inset 0 0 0 2px #b4c3ce;position:relative}
.fb9 .d1{flex:1}.fb9 .d2{flex:1.9}
.fb9 .hd{position:absolute;left:14px;top:22px;width:10px;height:70px;border-radius:5px;background:#8ea2b1}
.fb9 .st{position:absolute;right:12px;bottom:14px;white-space:nowrap;font-size:12px!important;border-radius:6px;background:#fff;border:2px dashed #c4682c;font:700 11px/1.25 Roboto;color:#7a4a22;padding:5px;text-align:center}
.fb9 .ft{height:16px;border-radius:0 0 10px 10px;background:#8ea2b1;margin:0 10px}
.pn9{position:absolute;width:44px;height:44px;border-radius:50%;background:#c4682c;color:#fff;font:800 20px/44px Montserrat;text-align:center;box-shadow:0 0 0 5px rgba(196,104,44,.25)}
.jc9{background:#12324a;color:#fff;border-radius:26px;padding:20px 22px;display:flex;flex-direction:column;gap:10px}.jc9 small{color:#9fc1d6}
.jh9{display:flex;justify-content:space-between;align-items:baseline}.jh9 b{display:block;font:800 30px/1.25 Montserrat;margin-top:2px}.jh9 span{font:700 15px/1.3 Roboto;background:#c4682c;border-radius:10px;padding:6px 10px}
.jf9{flex:1;display:flex;gap:12px;align-items:center;background:rgba(255,255,255,.07);border-radius:16px;padding:8px 12px}
.jf9>i{width:36px;height:36px;flex:none;border-radius:50%;background:#c4682c;font:800 17px/36px Montserrat;font-style:normal;text-align:center}
.jf9 em{display:block;font:500 14px/1.3 Roboto;font-style:normal;color:#9fc1d6}.jf9 b{font:600 19px/1.35 Roboto}
.ph9{display:flex;gap:8px;margin-left:auto}.ph9 u{width:64px;height:52px;border-radius:10px;display:flex!important;align-items:center;justify-content:center;color:#fff;background:linear-gradient(135deg,#5d7a8f,#2d4b60);display:block}.ph9 u:nth-child(2){background:linear-gradient(135deg,#dfe7ec,#9fb3c1)}
.bt9{display:grid;grid-template-columns:1.6fr 1fr;gap:14px}
.rt9{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(18,50,74,.08)}
.rt9>div{display:grid;grid-template-columns:62px 1fr auto;gap:12px;align-items:center;border-top:1px solid #e6eef3;padding-top:5px}
.rt9 .tm{font:700 15px/1.3 Roboto;color:#c4682c}.rt9 b{display:block;font:700 17px/1.3 Roboto}.rt9 span{font:500 15px/1.3 Roboto;color:#5f7686}.rt9 .pt{font:600 14px/1.3 Roboto;background:#e3f1f8;border-radius:8px;padding:5px 8px;color:#12324a}
.pc9{background:#c4682c;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.pc9 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#ffe2cd}
.pc9 div{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(255,255,255,.25);padding-bottom:5px}.pc9 div span{font:500 18px/1.35 Roboto}.pc9 div b{font:800 26px/1.25 Montserrat}
.pc9 p{margin-top:auto;font:500 16px/1.45 Roboto;color:#fff3ea}
""", "<div class=kk>FRIDGE AND WASHING MACHINE REPAIR</div><h1>“Fridge not cooling” calls?<br><span>Get the model and photos first.</span></h1>",
f'''<div class=vw><div class=tp9><div class=fz9><small>CUSTOMER SENDS · SAMPLE</small><div class=fb9><div class="dr d1"><i class=hd></i></div><div class="dr d2"><i class=hd></i><div class=st>MODEL STICKER<br>SAMPLE-DD-340</div></div><div class=ft></div>
<i class=pn9 style="right:30px;bottom:110px">1</i><i class=pn9 style="left:46px;top:60px">2</i><i class=pn9 style="left:46px;top:270px">3</i></div></div>
<div class=jc9><div class=jh9><div><small>BOOKING FORM → JOB CARD</small><b>{JOBS9[0][0]}</b></div><span>Today {JOBS9[0][1]}</span></div>
<div class=jf9><i>1</i><div><em>Appliance and model</em><b>{JOBS9[0][3]} · SAMPLE-DD-340</b></div></div>
<div class=jf9><i>2</i><div><em>Problem</em><b>{JOBS9[0][4]}, for 2 days</b></div></div>
<div class=jf9><i>3</i><div><em>Photos</em><b>Model sticker, back panel</b></div><div class=ph9><u>{ic("camera", 24)}</u><u>{ic("camera", 24)}</u></div></div>
<div class=jf9><i>4</i><div><em>Area and mobile</em><b>{JOBS9[0][2]} · 98XXX XX617</b></div></div></div></div>
<div class=bt9><div class=rt9><small>TECHNICIAN · TODAY · {pl(len(JOBS9), "JOB", "JOBS")} · SAMPLE</small>{"".join(f'<div><span class=tm>{t}</span><div><b>{ap}</b><span>{a} · {pr}</span></div><span class=pt>{pt}</span></div>' for jid, t, a, ap, pr, pt in JOBS9)}</div>
<div class=pc9><small>PARTS TO CARRY TODAY</small>{"".join(f'<div><span>{k}</span><b>{v}</b></div>' for k, v in PARTS9.most_common())}<p>Counted from the job cards. One trip, the right parts.</p></div></div></div>''',
"#12324a", "Run a repair service? DM us", "background:#12324a;color:#fff")


# ───────── 370 INDIA · Carpenter / interior woodwork contractor · SINGLE · TeX Gyre Adventor + Source Sans 3 · teak brown / ply beige / blueprint blue
# New technique: SVG isometric 2BHK floor plan computed from feet (iso projection in Python), furniture as extruded
# boxes painted back to front, colour = work status, upright numbered pins that match the room-wise list.
C30, S30 = math.cos(math.radians(30)), 0.5
SC0, OX0, OY0 = 13, 340, 62
def iso(x, y, z=0): return ((x - y) * C30 * SC0 + OX0, (x + y) * S30 * SC0 - z * SC0 + OY0)
def poly(pts, fill, stroke="none", sw=0, extra=""):
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round" {extra}/>'
ROOMS0 = [("Living", 0, 0, 16, 12, "#efe4d2"), ("Kitchen", 16, 0, 14, 10, "#e6ecef"), ("Bedroom 1", 0, 12, 14, 12, "#f1e8da"), ("Bedroom 2", 14, 10, 16, 14, "#ebe2d2")]
ST0 = {"done": ("#9a5b2e", "#7a4522", "#b8794a", "Done"), "work": ("#e9c48f", "#d6a768", "#f3dbb4", "In progress"), "todo": ("#d9dde2", "#c3c9d0", "#eceff2", "Not started")}
ITEMS0 = [(1, "TV unit", "Living", 1, 3, 1.6, 7, 2.2, "done", "Day 6"), (2, "Shoe rack", "Living", 12, 0.3, 3.5, 1.4, 3.5, "done", "Day 8"),
          (3, "Kitchen cabinets", "Kitchen", 18, 0.3, 11, 2, 3, "work", "Day 14"), (4, "Wardrobe", "Bedroom 1", 0.3, 14, 2, 7, 7, "work", "Day 15"),
          (5, "Bed with storage", "Bedroom 1", 6, 13, 6, 6.5, 1.6, "todo", "Day 18"), (6, "Bed with storage", "Bedroom 2", 22.5, 15, 6, 6, 1.6, "work", "Day 16"),
          (7, "Study table", "Bedroom 2", 14.5, 10.3, 4, 2, 2.6, "todo", "Day 20")]
def box0(x, y, w, d, h, st):
    t, l, r, _ = ST0[st]
    dash = 'stroke-dasharray="6 5"' if st == "todo" else ""
    sk = "#8f98a3" if st == "todo" else "#5b3418"
    return (poly([iso(x + w, y, 0), iso(x + w, y + d, 0), iso(x + w, y + d, h), iso(x + w, y, h)], l, sk, 1.5, dash)
            + poly([iso(x, y + d, 0), iso(x + w, y + d, 0), iso(x + w, y + d, h), iso(x, y + d, h)], r, sk, 1.5, dash)
            + poly([iso(x, y, h), iso(x + w, y, h), iso(x + w, y + d, h), iso(x, y + d, h)], t, sk, 1.5, dash))
def plan0():
    g = []
    g.append(poly([iso(0, 0, 0), iso(0, 0, 3), iso(30, 0, 3), iso(30, 0, 0)], "#d7c7ad", "#8c7556", 1.5))
    g.append(poly([iso(0, 0, 0), iso(0, 0, 3), iso(0, 24, 3), iso(0, 24, 0)], "#cbb995", "#8c7556", 1.5))
    for n, x, y, w, d, c in ROOMS0:
        g.append(poly([iso(x, y), iso(x + w, y), iso(x + w, y + d), iso(x, y + d)], c, "#8c7556", 2.5))
    for _, x, y, w, d, c in ROOMS0:
        pass
    for it in sorted(ITEMS0, key=lambda i: (i[3] + i[5] / 2) + (i[4] + i[6] / 2)):
        g.append(box0(it[3], it[4], it[5], it[6], it[7], it[8]))
    for n, x, y, w, d, c in ROOMS0:
        lx, ly = iso(*LP0[n])
        g.append(f'<rect x="{lx - len(n) * 7.5 - 12:.0f}" y="{ly - 21:.0f}" width="{len(n) * 15 + 24:.0f}" height="30" rx="15" fill="#fff" opacity=".85"/><text x="{lx:.0f}" y="{ly:.0f}" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="19" fill="#5b4a33" letter-spacing="1">{n.upper()}</text>')
    for it in ITEMS0:
        px, py = iso(it[3] + it[5] / 2, it[4] + it[6] / 2, it[7])
        c = "#1f4e8c"
        g.append(f'<line x1="{px:.0f}" y1="{py:.0f}" x2="{px:.0f}" y2="{py - 26:.0f}" stroke="{c}" stroke-width="2.5"/><circle cx="{px:.0f}" cy="{py - 42:.0f}" r="17" fill="{c}" stroke="#fff" stroke-width="3"/><text x="{px:.0f}" y="{py - 35:.0f}" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="19" fill="#fff">{it[0]}</text>')
    return f'<svg viewBox="0 0 740 420" style="width:100%;height:100%;display:block">{"".join(g)}</svg>'
LP0 = {"Living": (6, 6), "Kitchen": (23, 6.8), "Bedroom 1": (5, 23.3), "Bedroom 2": (16.5, 23)}
CNT0 = {k: sum(1 for i in ITEMS0 if i[8] == k) for k in ST0}
P["p370_carpenter"] = page("""
body{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:#f4efe6;color:#2a2118}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#1f4e8c;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:56px;line-height:1.22;letter-spacing:-1px} h1 span{color:#9a5b2e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pl0{flex:1;background:#fff;border-radius:26px;padding:16px 22px 14px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(42,33,24,.08);min-height:0;background-image:linear-gradient(#eef3fa 1px,transparent 1px),linear-gradient(90deg,#eef3fa 1px,transparent 1px);background-size:28px 28px}
.ph0{display:flex;justify-content:space-between;align-items:center}.ph0 small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#6d6354}
.ph0 div{display:flex;gap:16px;font:600 15px/1.4 'Source Sans 3'}.ph0 span{display:flex;align-items:center;gap:6px}.ph0 i{width:18px;height:18px;border-radius:5px}
.sv0{flex:1;display:flex;align-items:center;min-height:0;overflow:hidden}
.bt0{display:grid;grid-template-columns:1.35fr 1fr;gap:14px}
.ls0{background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;gap:2px;box-shadow:0 14px 30px rgba(42,33,24,.08)}
.ls0>div{display:grid;grid-template-columns:34px 1fr auto;gap:12px;align-items:center;border-top:1px solid #efe8dc;padding:5px 0}.ls0>div:first-child{border:0}
.ls0 .nm{width:30px;height:30px;border-radius:50%;background:#1f4e8c;color:#fff;font:700 15px/30px 'TeX Gyre Adventor';text-align:center}
.ls0 b{font:700 18px/1.3 'Source Sans 3'}.ls0 b span{font-weight:500;color:#6d6354}
.ls0 em{font:700 14px/1.3 'Source Sans 3';font-style:normal;border-radius:8px;padding:4px 9px}.ls0 em.done{background:#9a5b2e;color:#fff}.ls0 em.work{background:#f3dbb4;color:#6b4318}.ls0 em.todo{background:#eceff2;color:#5f6873}
.up0{background:#1f4e8c;color:#fff;border-radius:24px 24px 24px 6px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.up0 small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#c9dbf5}.up0 p{font:500 18px/1.45 'Source Sans 3';text-wrap:pretty}
.pt0{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.pt0 u{text-decoration:none;display:flex;flex-direction:column;gap:4px}.pt0 u i{height:74px;border-radius:12px;background:linear-gradient(160deg,#c48a5a,#7a4522 70%,#5b3418)}.pt0 u:nth-child(3) i{background:linear-gradient(160deg,#f3dbb4,#d6a768)}.pt0 u span{font:500 14px/1.3 'Source Sans 3';color:#dbe7f8}
.up0>div:last-child{margin-top:auto;display:flex;gap:8px}.up0>div:last-child span{flex:1;background:rgba(255,255,255,.12);border-radius:12px;padding:8px 10px;font:500 14px/1.3 'Source Sans 3';color:#dbe7f8}.up0>div:last-child b{display:block;font:700 24px/1.25 'TeX Gyre Adventor';color:#fff}
""", "<div class=kk>CARPENTER · 2BHK INTERIOR WOODWORK</div><h1>Owner asks “how much is left?”<br><span>Show the flat, room by room.</span></h1>",
f'''<div class=vw><div class=pl0><div class=ph0><small>SITE: FLAT 302 · DAY 12 · SAMPLE</small><div>{"".join(f'<span><i style="background:{v[0]};border:1px solid {v[1]}"></i>{v[3]}</span>' for v in ST0.values())}</div></div><div class=sv0>{plan0()}</div></div>
<div class=bt0><div class=ls0>{"".join(f'<div><span class=nm>{i[0]}</span><b>{i[1]} <span>· {i[2]}</span></b><em class={i[8]}>{ST0[i[8]][3] if i[8] != "todo" else "Starts " + i[9]}</em></div>' for i in ITEMS0)}</div>
<div class=up0><small>SITE UPDATE · SENT TO OWNER</small><p>Day 12: TV unit and shoe rack are done. Kitchen, wardrobe and one bed are in progress.</p><div class=pt0>{"".join(f"<u><i></i><span>{t}</span></u>" for t in ["TV unit", "Shoe rack", "Kitchen"])}</div>
<div>{"".join(f'<span><b>{CNT0[k]}</b>{ST0[k][3].lower() if k != "done" else "done"}</span>' for k in ST0)}</div></div></div></div>''',
"#2a2118", "Run interior work? DM us", "background:#9a5b2e;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
