# ───────── 455 USA · On-site document shredding (route + certificate) · CAROUSEL 5 · Archivo Black + Open Sans · security navy / shred white / lock green
# New technique: HTML service-area map with heat halos sized by bins and coloured by fullness, route line drawn in an
# overlay SVG (non-scaling stroke) through the stops chosen by a rule; one client list drives map, scan screen, route, certificate.
import random as _r5
NV5 = "#14233d"; GR5 = "#2f9e6a"; SH5 = "#f1f3f6"; MU5 = "#5f6b7d"; AM5 = "#f0a630"; RD5 = "#d64b3c"
CL5 = [  # name, x%, y%, bin fills
    ("Sample Law Office", 30, 30, [100, 80, 60, 40]), ("Sample Dental Office", 62, 22, [90, 70]),
    ("Sample Accounting Firm", 76, 52, [95, 85, 50]), ("Sample Realty", 18, 66, [30]),
    ("Sample Insurance Agency", 48, 60, [75, 65]), ("Sample Property Manager", 80, 80, [100, 90]),
    ("Sample Auto Dealer", 34, 84, [20])]
RULE5 = 75
ON5 = [c for c in CL5 if max(c[3]) >= RULE5]; OFF5 = [c for c in CL5 if max(c[3]) < RULE5]
DEPOT5 = (8, 40)
ORDER5 = ["Sample Law Office", "Sample Dental Office", "Sample Accounting Firm", "Sample Property Manager", "Sample Insurance Agency"]
assert sorted(ORDER5) == sorted(c[0] for c in ON5)
RT5 = [next(c for c in CL5 if c[0] == n) for n in ORDER5]
BINS5 = sum(len(c[3]) for c in RT5); FULL5 = sum(1 for c in CL5 for f in c[3] if f >= RULE5); TRUCK5 = 40
TIMES5 = ["8:30 AM", "9:20 AM", "10:15 AM", "11:10 AM", "12:05 PM"]
def col5(f): return RD5 if f >= 90 else (AM5 if f >= RULE5 else GR5)
def map5(big=True):
    halos = "".join(f'<i class=hl style="left:{x}%;top:{y}%;width:{90 + 30 * len(b)}px;height:{90 + 30 * len(b)}px;background:radial-gradient(circle,{col5(max(b))}66,{col5(max(b))}00 70%)"></i>' for _, x, y, b in CL5)
    pts = [DEPOT5] + [(c[1], c[2]) for c in RT5] + [DEPOT5]
    route = f'<svg class=rt viewBox="0 0 100 100" preserveAspectRatio="none"><polyline points="{" ".join(f"{x},{y}" for x, y in pts)}" fill="none" stroke="{NV5}" stroke-width="3" stroke-dasharray="7 6" vector-effect="non-scaling-stroke" stroke-linejoin="round"/></svg>'
    pins = "".join(f'<div class="pn{" off" if max(b) < RULE5 else ""}{" lf" if x > 70 else ""}" style="left:{x}%;top:{y}%"><b style="background:{col5(max(b))}">{(ORDER5.index(n) + 1) if n in ORDER5 else "–"}</b><span>{n.replace("Sample ", "")} · {len(b)} {"bin" if len(b) == 1 else "bins"}</span></div>' for n, x, y, b in CL5)
    return f'<div class=mp><div class=rv></div><div class=hz>{halos}</div>{route}<div class=dp style="left:{DEPOT5[0]}%;top:{DEPOT5[1]}%"><span>Depot</span></div>{pins}</div>'
B5 = f"""
body{{--f:'Open Sans';--h:'Archivo Black';background:{SH5};color:{NV5}}}
.kk5{{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:{GR5};margin-top:22px;display:flex;gap:10px;align-items:center}}.kk5 i{{width:22px;height:22px;border-radius:6px;background:repeating-linear-gradient(90deg,{NV5} 0 3px,transparent 3px 6px)}}
h1{{font-family:'Archivo Black';font-weight:400;font-size:54px;line-height:1.25;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{GR5}}}
.sm5{{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:{MU5}}}
.cd5{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(20,35,61,.08)}}
.dk5{{background:{NV5};color:#fff;border-radius:22px}}.dk5 .sm5{{color:#9fb0c8}}
.mp{{position:relative;flex:1;min-height:0;border-radius:16px;overflow:hidden;background:#e9edf2;background-image:repeating-linear-gradient(0deg,transparent 0 58px,#fff 58px 64px),repeating-linear-gradient(90deg,transparent 0 92px,#fff 92px 98px)}}
.mp .rv{{position:absolute;left:0;right:0;top:44%;height:26px;background:#bcd7ea;transform:rotate(-8deg);transform-origin:left}}
.mp .hz{{position:absolute;inset:0;overflow:hidden}}.hl{{position:absolute;transform:translate(-50%,-50%);border-radius:50%}}
.mp .rt{{position:absolute;inset:0;width:100%;height:100%}}
.pn{{position:absolute;transform:translate(-14px,-14px);display:flex;align-items:center;gap:6px}}.pn b{{width:28px;height:28px;border-radius:50%;color:#fff;font:800 15px/28px 'Open Sans';text-align:center;box-shadow:0 0 0 3px #fff;flex:none}}
.pn.lf{{flex-direction:row-reverse;transform:translate(calc(-100% + 14px),-14px)}}.pn span{{font:700 15px/1.3 'Open Sans';background:#fff;border-radius:7px;padding:3px 8px;white-space:nowrap;box-shadow:0 4px 10px rgba(0,0,0,.08)}}.pn.off span{{color:{MU5}}}
.dp{{position:absolute;transform:translate(-12px,-12px)}}.dp span{{display:block;background:{NV5};color:#fff;font:700 14px/1.3 'Open Sans';padding:5px 9px;border-radius:7px}}
.lg5{{display:flex;gap:16px;flex-wrap:wrap}}.lg5 span{{display:flex;align-items:center;gap:7px;font:600 15px/1.3 'Open Sans'}}.lg5 i{{width:14px;height:14px;border-radius:50%}}
"""
LG5 = f'<div class=lg5><span><i style="background:{RD5}"></i>90% full or more</span><span><i style="background:{AM5}"></i>{RULE5}–89%</span><span><i style="background:{GR5}"></i>Under {RULE5}%</span><span><i style="background:transparent;border:2px dashed {NV5};border-radius:3px"></i>Tuesday route</span></div>'
def t5(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{NV5};color:#fff"):
    return page(B5 + css, f"<div class=kk5><i></i>{kick}</div><h1>{head}</h1>", vis, NV5, cta, ctacss, tagline=f"{n} / 5")
P["p455_shred_s1"] = t5(1, "ON-SITE SHREDDING · ROUTES", "Bins overflowing before pickup?<br><span>See every full bin on a map.</span>",
f'''<div class=w51><div class="cd5 mc"><div class=hd><span class=sm5>SAMPLE SERVICE AREA · {len(CL5)} CLIENTS · BIN LEVELS AT 6 PM MON 23 NOV</span></div>{map5()}{LG5}</div>
<div class=tl>{"".join(f'<div class="{c}"><b>{a}</b><span>{b}</span></div>' for a, b, c in [(FULL5, f"bins {RULE5}% full or more", "cd5"), (len(ON5), "stops on Tuesday's route", "dk5"), (len(OFF5), "clients wait till next week", "cd5")])}</div></div>''',
css=f""".w51{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.mc{{flex:1;padding:16px 18px;display:flex;flex-direction:column;gap:12px;min-height:0}}
.tl{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.tl div{{padding:14px 18px}}.tl b{{display:block;font:400 42px/1.25 'Archivo Black'}}.tl span{{font:600 17px/1.35 'Open Sans'}}.tl .dk5 b{{color:#7fe0b0}}""")
# slide 2: scan the bin
SC5 = RT5[0]
def qr5(n=21, seed=455):
    rr = _r5.Random(seed); cells = []
    for y in range(n):
        for x in range(n):
            fz = any(x0 <= x < x0 + 7 and y0 <= y < y0 + 7 for x0, y0 in ((0, 0), (n - 7, 0), (0, n - 7)))
            if fz:
                lx = min(x, abs(x - (n - 7)) if x >= n - 7 else x); ly = min(y, abs(y - (n - 7)) if y >= n - 7 else y)
                ox = x if x < 7 else x - (n - 7); oy = y if y < 7 else y - (n - 7)
                on = ox in (0, 6) or oy in (0, 6) or (2 <= ox <= 4 and 2 <= oy <= 4)
            else:
                on = rr.random() < .48
            if on: cells.append(f'<rect x="{x}" y="{y}" width="1" height="1"/>')
    return f'<svg viewBox="-1 -1 {n + 2} {n + 2}" style="width:100%;height:100%;display:block;background:#fff"><g fill="{NV5}">{"".join(cells)}</g></svg>'
SCR5 = f'''<div class=sc><span class=sm5>BIN SCAN · SAMPLE</span><b class=tt>{SC5[0]}</b><p class=ln>Bin 1 of {len(SC5[3])} · front desk</p>
<div class=lv><span>How full is it?</span><div class=st>{"".join(f'<i class="{"on" if v == 100 else ""}">{v}%</i>' for v in (25, 50, 75, 100))}</div></div>
<div class=ck><i>{ic("check", 18, "#fff", 3)}</i><span>Ask for an extra pickup</span></div><div class=rw><span>Bins at this office</span><b>{len(SC5[3])}</b></div><div class=rw><span>Note for the driver</span><b>Side door after 5 PM</b></div><div class=ph5>{ic("camera", 22, MU5)}<span>Add a photo (optional)</span></div><div class=nt>Next pickup: Tue 24 Nov,<br>about <b style="white-space:nowrap">{TIMES5[0]}</b></div><div class=bt>Send</div></div>'''
P["p455_shred_s2"] = t5(2, "1 · CLIENT SCANS THE BIN", "A sticker on the bin.<br><span>One tap says it is full.</span>",
f'''<div class=w52><div class="cd5 bn"><span class=sm5>LOCKED CONSOLE BIN · 1 OF {len(SC5[3])}</span><div class=cab><div class=tp><i class=slot></i></div><div class=dr><i class=lock></i><div class=qr>{qr5()}</div><p>Scan when full</p></div><div class=bs5></div></div>
<div class=hs><span class=sm5>THIS BIN SO FAR</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Last emptied", "Tue 10 Nov"), ("Marked 75% full", "Thu 19 Nov"), ("Marked 100% full", "Mon 23 Nov, 4:12 PM")])}</div></div>
<div class=ph>{phone(SCR5, 380, 700)}</div></div>''',
css=f""".w52{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 400px;gap:20px;min-height:0;align-items:center}}
.bn{{align-self:stretch;padding:20px 22px;display:flex;flex-direction:column;gap:14px;align-items:center}}.bn>.sm5{{align-self:flex-start}}
.cab{{width:300px;display:flex;flex-direction:column;margin:auto 0}}.cab .tp{{height:44px;background:#3a4a63;border-radius:12px 12px 0 0;display:flex;align-items:center;justify-content:center}}.cab .slot{{width:150px;height:10px;border-radius:5px;background:#0d1626}}
.cab .dr{{height:400px;background:linear-gradient(90deg,#2a3a55,#344766);border-left:8px solid #22314a;border-right:8px solid #22314a;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;position:relative}}.cab .lock{{position:absolute;top:18px;right:20px;width:18px;height:26px;border-radius:5px;background:#c9ced6}}
.cab .qr{{width:150px;height:150px;border-radius:8px;overflow:hidden;border:6px solid #fff}}.cab .dr p{{font:700 16px/1.3 'Open Sans';color:#fff;background:{GR5};border-radius:7px;padding:4px 10px}}.cab .bs5{{height:14px;background:#22314a;border-radius:0 0 8px 8px}}
.hs{{align-self:stretch;display:flex;flex-direction:column;gap:6px}}.hs .r{{display:flex;justify-content:space-between;gap:10px;border-top:1px solid #e6eaf0;padding-top:8px;font:500 18px/1.35 'Open Sans'}}.hs .r b{{font-weight:700}}
.ph{{display:flex;justify-content:center}}
.sc{{flex:1;padding:14px 22px 22px;display:flex;flex-direction:column;gap:14px;font-family:'Open Sans'}}.sc .tt{{font:400 26px/1.3 'Archivo Black'}}.sc .ln{{font:500 17px/1.35 'Open Sans';color:{MU5};margin-top:-8px}}
.lv{{background:{SH5};border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:10px}}.lv>span{{font:700 17px/1.3 'Open Sans'}}.lv .st{{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}}.lv i{{font:700 16px/40px 'Open Sans';font-style:normal;text-align:center;background:#fff;border-radius:10px;border:2px solid #dfe4eb}}.lv i.on{{background:{RD5};border-color:{RD5};color:#fff}}
.ck{{display:flex;gap:10px;align-items:center;font:600 17px/1.3 'Open Sans'}}.ck i{{width:28px;height:28px;border-radius:8px;background:{GR5};display:flex;align-items:center;justify-content:center;flex:none}}
.rw{{display:flex;justify-content:space-between;gap:8px;border-top:1px solid #e6eaf0;padding-top:10px;font:500 16px/1.35 'Open Sans'}}.rw b{{font-weight:700}}.ph5{{display:flex;gap:10px;align-items:center;justify-content:center;border:2px dashed #cfd6e0;border-radius:12px;padding:14px;font:600 16px/1.3 'Open Sans';color:{MU5}}}.nt{{background:#e5f4ec;color:#1f6b46;border-radius:12px;padding:12px 14px;font:600 16px/1.4 'Open Sans'}}.sc .bt{{margin-top:auto;background:{NV5};color:#fff;text-align:center;border-radius:14px;padding:15px;font:700 18px/1.3 'Open Sans'}}""")
# slide 3: route
P["p455_shred_s3"] = t5(3, "2 · TUESDAY ROUTE", f"Only bins at {RULE5}% or more.<br><span>The route builds itself.</span>",
f'''<div class=w53><div class="cd5 rl"><span class=sm5>TUE 24 NOV · TRUCK 1 · SAMPLE</span>{"".join(f'<div class=st><b class=n>{i + 1}</b><div class=tx><b>{c[0]}</b><div class=bs>{"".join(f'<i style="background:{col5(f)}">{f}%</i>' for f in c[3])}</div></div><span class=tm>{TIMES5[i]}</span></div>' for i, c in enumerate(RT5))}</div>
<div class=sd><div class="dk5 tk"><span class=sm5>TRUCK LOAD</span><b>{BINS5} <small>of {TRUCK5} bins</small></b><div class=br><i style="width:{BINS5 / TRUCK5 * 100:.0f}%"></i></div><p>Room for {TRUCK5 - BINS5} more bins if a client asks.</p></div>
<div class="cd5 sk"><span class=sm5>WAITING TILL NEXT WEEK</span>{"".join(f'<div class=r><span>{c[0]}</span><b>{max(c[3])}% full</b></div>' for c in OFF5)}</div>
<div class="cd5 dy"><span class=sm5>THE DAY · SAMPLE DRIVER 1</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Leave the depot", "8:00 AM"), ("First stop", TIMES5[0]), ("Last stop", TIMES5[-1]), ("Stops and bins", f"{len(RT5)} stops · {BINS5} bins")])}</div><div class="cd5 ru"><span class=sm5>THE RULE · YOU SET IT</span><p>Any bin at {RULE5}% or more puts the client on the next route. Every client still gets at least one visit a month.</p></div></div></div>''',
css=f""".w53{{flex:1;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:16px;min-height:0}}
.rl{{padding:18px 22px;display:flex;flex-direction:column;gap:4px}}.rl .st{{flex:1;display:grid;grid-template-columns:40px minmax(0,1fr) auto;gap:14px;align-items:center;border-top:1px solid #e6eaf0}}.rl .st:nth-child(2){{border:0}}
.rl .n{{width:40px;height:40px;border-radius:50%;background:{NV5};color:#fff;font:400 18px/40px 'Archivo Black';text-align:center}}.rl .tx>b{{display:block;font:700 20px/1.3 'Open Sans';margin-bottom:6px}}.bs{{display:flex;gap:6px;flex-wrap:wrap}}.bs i{{font:700 14px/1.3 'Open Sans';font-style:normal;color:#fff;border-radius:7px;padding:3px 8px}}.rl .tm{{font:700 18px/1.3 'Open Sans';color:{MU5};white-space:nowrap}}
.sd{{display:flex;flex-direction:column;gap:16px;min-height:0}}.tk{{padding:20px 22px;display:flex;flex-direction:column;gap:10px}}.tk b{{font:400 46px/1.25 'Archivo Black'}}.tk small{{font:600 18px/1.3 'Open Sans';color:#c9d3e2}}.tk .br{{height:14px;border-radius:8px;background:#2c3d5c;overflow:hidden}}.tk .br i{{display:block;height:100%;background:#7fe0b0;border-radius:8px}}.tk p{{font:500 17px/1.4 'Open Sans';color:#d8e0ec}}
.sk{{padding:18px 22px;display:flex;flex-direction:column;gap:8px}}.sk .r{{display:flex;justify-content:space-between;gap:10px;border-top:1px solid #e6eaf0;padding-top:8px;font:500 18px/1.35 'Open Sans'}}.sk .r b{{color:{GR5}}}
.dy{{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:4px}}.dy .r{{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid #e6eaf0;font:500 18px/1.35 'Open Sans'}}.dy .r b{{font-weight:700}}.ru{{padding:18px 22px;display:flex;flex-direction:column;gap:8px;background:#e5f4ec}}.ru p{{font:500 18px/1.45 'Open Sans'}}""")
# slide 4: certificate
CERT5 = RT5[0]
P["p455_shred_s4"] = t5(4, "3 · CERTIFICATE", "Shredded on site.<br><span>Certificate sent the same hour.</span>",
f'''<div class=w54><div class=doc><div class=dh><div><span class=sm5>SAMPLE SHREDDING CO.</span><b>Certificate of Destruction</b></div><span class=no>No. 2026-1184</span></div>
{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Client", CERT5[0]), ("Date", "Tue 24 Nov 2026"), ("Bins emptied", f"{len(CERT5[3])} locked console bins"), ("Method", "Shredded on site, in the truck"), ("Start and finish", f"{TIMES5[0]} to 8:52 AM"), ("Seen by", "Front desk, Sample Law Office")])}
<div class=sg><div><i></i><span>Driver signature</span></div><div><i></i><span>Client signature</span></div></div><p class=fn>Sample document. Paper is taken for recycling after shredding.</p></div>
<div class=sd><div class="dk5 em"><span class=sm5>EMAIL · 9:01 AM</span><b>Your certificate is ready</b><p>{len(CERT5[3])} bins shredded today. Download the certificate or see all past visits.</p><div class=bt>Open certificate</div></div>
<div class="cd5 hi"><span class=sm5>PAST VISITS · {CERT5[0].upper().replace("SAMPLE ", "SAMPLE ")}</span>{"".join(f'<div class=r><span>{a}</span><div class=ic>{"<i></i>" * n}</div><b>{n} bins</b></div>' for a, n in [("Tue 24 Nov", len(CERT5[3])), ("Tue 27 Oct", 3), ("Tue 29 Sep", 4), ("Tue 1 Sep", 2)])}</div></div></div>''',
css=f""".w54{{flex:1;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:18px;min-height:0}}
.doc{{background:#fffdf7;border-radius:10px;padding:28px 30px;display:flex;flex-direction:column;gap:4px;box-shadow:0 24px 50px rgba(20,35,61,.14);border-top:10px solid {GR5}}}
.dh{{display:flex;justify-content:space-between;align-items:flex-start;gap:10px;margin-bottom:12px}}.dh b{{display:block;font:400 30px/1.3 'Archivo Black';margin-top:6px}}.no{{font:700 15px/1.3 'Open Sans';color:{MU5};white-space:nowrap;border:2px solid #dfe4eb;border-radius:8px;padding:4px 8px}}
.doc .r{{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:1px solid #ebe8de}}.doc .r span{{font:600 14px/1.4 'Open Sans';color:{MU5};letter-spacing:.5px}}.doc .r b{{font:700 21px/1.35 'Open Sans'}}
.sg{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:14px}}.sg i{{display:block;height:44px;border-bottom:2px solid {NV5};background:linear-gradient(transparent 60%,transparent)}}.sg span{{font:600 14px/1.4 'Open Sans';color:{MU5}}}.fn{{font:500 14px/1.4 'Open Sans';color:{MU5};margin-top:10px}}
.sd{{display:flex;flex-direction:column;gap:16px;min-height:0}}.em{{padding:20px 22px;display:flex;flex-direction:column;gap:10px}}.em b{{font:700 24px/1.3 'Open Sans'}}.em p{{font:500 17px/1.45 'Open Sans';color:#d8e0ec}}.em .bt{{background:#7fe0b0;color:{NV5};border-radius:12px;padding:12px;text-align:center;font:700 17px/1.3 'Open Sans'}}
.hi{{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:4px}}.hi .r{{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #e6eaf0;font:500 19px/1.35 'Open Sans'}}.hi .r b{{font-weight:700;width:64px;text-align:right}}.hi .r>span{{width:110px}}.hi .ic{{flex:1;display:flex;gap:5px}}.hi .ic i{{width:20px;height:28px;border-radius:4px;background:{NV5};box-shadow:inset 0 5px 0 #3a4a63}}""")
P["p455_shred_s5"] = t5(5, "ON-SITE SHREDDING · YOUR APP", "Run a shredding service?<br><span>Let's build your app.</span>",
f'''<div class=w55><div class=mini>{map5()}</div><div class=tl>{"".join(f'<div class="cd5 t"><b>{a}</b><p>{p}</p></div>' for a, p in [("Bin scan", "Clients mark a bin full with one tap."), ("Fill map", "See which offices need you first."), ("Smart route", "Only stops that need a visit."), ("Certificates", "Sent by email the same hour.")])}</div>
<div class="dk5 q"><p>How do your clients tell you a bin is full today? Tell us in the comments.</p></div></div>''',
css=f""".w55{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.mini{{flex:1;display:flex;min-height:0;border-radius:22px;overflow:hidden;box-shadow:0 14px 30px rgba(20,35,61,.08)}}.mini .mp{{border-radius:22px}}
.tl{{display:grid;grid-template-columns:repeat(4,1fr);gap:14px}}.t{{padding:18px}}.t b{{display:block;font:400 21px/1.3 'Archivo Black';margin-bottom:8px}}.t p{{font:500 17px/1.4 'Open Sans';color:{MU5}}}.q{{padding:20px 26px}}.q p{{font:700 21px/1.45 'Open Sans'}}""",
cta="Shred for offices? DM us", ctacss=f"background:{GR5};color:#fff")
