
# ───────── 416 INDIA · Silk reeling unit · CAROUSEL 5 · Cardo + Inter · mulberry green / cocoon ivory / raw silk gold
# New technique: seeded cocoon heaps in woven trays (SVG, depth-sorted), top-down reeling basins with floating cocoons,
# and a figure-eight silk hank isotype (1 hank = 1 kg raw silk, partial hank clipped) computed from the lot ledger.
G6 = "#2f5d3a"; IV6 = "#f6f0df"; GD6 = "#c3922a"; K6 = "#1f2a22"; MU6 = "#8e3b5a"
LC6 = {"L-21": "#5e7fa3", "L-22": GD6, "L-23": MU6, "L-18": "#6f8a4a", "L-19": "#b0674a", "L-20": "#5c6f8f"}
TRAY6 = [("L-21", "F-03", 60), ("L-22", "F-08", 62), ("L-23", "F-11", 55)]

def heap6(seed, n=44, w=300, h=190, uid="a"):
    rnd = random.Random(seed)
    cx, cy, rx, ry = 150, 118, 128, 58
    pts = []
    while len(pts) < n:
        x = rnd.uniform(cx - rx + 18, cx + rx - 18); y = rnd.uniform(cy - ry - 34, cy + ry - 22)
        dx = (x - cx) / (rx - 14); dy = (y - (cy - 14)) / (ry - 4)
        if dx * dx + dy * dy <= 1: pts.append((x, y, rnd.uniform(-60, 60), rnd.choice(["#fbf6e8", "#f4ecd5", "#efe4c6"])))
    pts.sort(key=lambda p: p[1])
    co = "".join(f'<g transform="translate({x:.1f} {y:.1f}) rotate({a:.0f})"><path d="M-16 0 C-16 -11 -4 -11 0 -6 C4 -11 16 -11 16 0 C16 11 4 11 0 6 C-4 11 -16 11 -16 0 Z" fill="{c}" stroke="#b9a77a" stroke-width="1.6"/><path d="M-9 -3 Q-3 0 -9 3 M9 -3 Q3 0 9 3" stroke="#d6c79c" stroke-width="1.2" fill="none"/></g>' for x, y, a, c in pts)
    return f'''<svg viewBox="0 0 {w} {h}" width="{w}" style="display:block;width:100%;height:auto"><defs><pattern id="wv{uid}" width="12" height="12" patternUnits="userSpaceOnUse"><rect width="12" height="12" fill="#b78a4f"/><path d="M0 3h12M0 9h12" stroke="#9c7440" stroke-width="3"/><path d="M3 0v12M9 0v12" stroke="#cfa56a" stroke-width="2" stroke-dasharray="3 3"/></pattern></defs>
<ellipse cx="{cx}" cy="{cy + 8}" rx="{rx + 14}" ry="{ry + 12}" fill="#8a6435"/><ellipse cx="{cx}" cy="{cy}" rx="{rx + 8}" ry="{ry + 6}" fill="url(#wv{uid})"/>{co}</svg>'''

def hank6(frac=1.0, col=GD6, uid="h", dashed=False):
    clip = f'<clipPath id="hc{uid}"><rect x="0" y="{80 - 80 * frac:.1f}" width="34" height="{80 * frac:.1f}"/></clipPath>' if frac < 1 else ""
    d = "M17 4 C30 4 30 36 17 40 C4 44 4 76 17 76 C30 76 30 44 17 40 C4 36 4 4 17 4 Z"
    base = f'<path d="{d}" fill="none" stroke="#c9b48a" stroke-width="2" stroke-dasharray="4 3"/>' if (frac < 1 or dashed) else ""
    body = "" if dashed else f'<g {"clip-path=" + chr(34) + "url(#hc" + uid + ")" + chr(34) if frac < 1 else ""}><path d="{d}" fill="{col}" stroke="#7d5a14" stroke-width="2"/><path d="M11 10 C14 22 14 30 17 38 M23 10 C20 22 20 30 17 38 M11 70 C14 58 14 50 17 42 M23 70 C20 58 20 50 17 42" stroke="#f3dc9c" stroke-width="1.4" fill="none"/><rect x="9" y="37" width="16" height="6" rx="2" fill="#7d5a14"/></g>'
    return f'<svg viewBox="0 0 34 80" width="30" height="70" style="display:block;flex:none"><defs>{clip}</defs>{base}{body}</svg>'

def basin6(lot, seed):
    rnd = random.Random(seed)
    cs = "".join(f'<ellipse cx="{rnd.uniform(18, 52):.1f}" cy="{rnd.uniform(18, 52):.1f}" rx="6" ry="4" transform="rotate({rnd.randint(-50, 50)} 35 35)" fill="#fbf6e8" stroke="#b9a77a" stroke-width="1"/>' for _ in range(7)) if lot else ""
    return f'<svg viewBox="0 0 70 70" width="58" height="58" style="display:block;flex:none"><circle cx="35" cy="35" r="32" fill="#8d9aa3"/><circle cx="35" cy="35" r="26" fill="{"#cfe0e6" if lot else "#e7ecee"}"/>{cs}</svg>'

def chip6(l): return f'<span class=lc6 style="background:{LC6[l]}">{l}</span>'

B6 = f"""
body{{--f:'Inter';--h:'Cardo';background:{IV6};color:{K6}}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{MU6};margin-top:22px;align-self:flex-start}}
h1{{font-family:'Cardo';font-weight:700;font-size:62px;line-height:1.24;letter-spacing:-.6px;margin-top:18px}} h1 span{{color:{G6}}}
.sm6{{font:700 13px/1.4 Inter;letter-spacing:2px;color:#6f7464}}
.cd6{{background:#fffdf6;border-radius:24px;box-shadow:0 14px 30px rgba(40,50,20,.09)}}
.dk6{{background:{K6};color:#fff;border-radius:24px}}.dk6 .sm6{{color:#c9d3bf}}
.lc6.lc6.lc6{{display:inline-block;color:#fff!important;font:800 15px/1 Inter!important;border-radius:8px;padding:7px 10px;letter-spacing:.5px}}
"""
def t6(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{G6};color:#fff"):
    return page(B6 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, K6, cta, ctacss, tagline=f"{n} / 5")

P["p416_silk_s1"] = t6(1, "SILK REELING UNIT · COCOON LOTS", "Cocoon lots mixed up?<br><span>Track every lot to the skein.</span>",
f'''<div class=w61><div class=tr61>{"".join(f'<div class="cd6 ty61"><div class=hd61>{chip6(l)}<span>Farmer {f}</span></div>{heap6(i * 7 + 3, uid=f"s1{i}")}<b>{kg} kg cocoons</b><div class=in61><span>Bought</span><em>Mon 23 Nov</em></div><div class=in61><span>Stored</span><em>Rack {i + 1}</em></div><div class=q61><em>Basin ?</em><em>Silk ?</em></div></div>' for i, (l, f, kg) in enumerate(TRAY6))}</div>
<div class=nb61><span class=sm6>REGISTER · TUE · SAMPLE</span><p>L-21 + L-22 in basins 1 to 4 … <s>or 1 to 3?</s> silk weighed together</p></div>
<div class="dk6 qs61">{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [("Which lot?", "is in which basin today"), ("How much silk?", "did each lot give"), ("Which farmer?", "to buy from again")])}</div></div>''',
css=f""".w61{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tr61{{flex:1;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px;min-height:0}}
.ty61{{padding:16px 16px 18px;display:flex;flex-direction:column;justify-content:space-between;gap:8px}}.hd61{{display:flex;justify-content:space-between;align-items:center}}.hd61 span{{font:600 15px/1.3 Inter;color:#6f7464}}
.ty61 b{{font:700 30px/1.35 Cardo;text-align:center}}.in61{{display:flex;justify-content:space-between;border-top:1px solid #ece3c9;padding-top:10px}}.in61 span{{font:500 17px/1.3 Inter;color:#6f7464}}.in61 em{{font:700 18px/1.3 Inter;font-style:normal}}.q61{{display:flex;gap:8px}}.q61 em{{flex:1;text-align:center;font:700 16px/1.2 Inter;font-style:normal;border:2px dashed #c9b48a;border-radius:10px;padding:9px 4px;color:{MU6}}}
.nb61{{background:#fffbea repeating-linear-gradient(180deg,transparent 0 41px,#d8d2b8 41px 42px);border-radius:18px;padding:12px 24px 14px;display:flex;flex-direction:column;gap:4px;border-left:6px solid #d98b8b}}
.nb61 p{{font:italic 700 28px/1.5 Cardo;color:#3d4a8f}}.nb61 s{{text-decoration-color:#c0392b}}
.qs61{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:20px 24px}}.qs61 b{{display:block;font:700 30px/1.35 Cardo;color:#f1d58f;margin-bottom:4px}}.qs61 span{{font:500 17px/1.4 Inter;color:#d9e0d3}}""")

SORT6 = [("Good", 58, G6), ("Double", 3, GD6), ("Flimsy", 1, "#b0674a")]
LOT22 = sum(k for _, k, _ in SORT6)
P["p416_silk_s2"] = t6(2, "1 · LOT CARD", "Weigh and sort each lot.<br><span>One card per farmer lot.</span>",
f'''<div class=w62><div class="cd6 lt62"><div class=hd62><span class=sm6>LOT CARD · SAMPLE</span>{chip6("L-22")}</div>{heap6(11, n=58, uid="s2")}
{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Farmer", "F-08 · Sample Village"), ("Bought", "Mon 23 Nov · 9:10 AM"), ("Cocoons", f"{LOT22} kg"), ("Type", "White · bivoltine"), ("Stored", "Rack 2 · shelf B")])}</div>
<div class=rt62><div class="cd6 so62"><span class=sm6>SORTED · {LOT22} KG</span><div class=sb62>{"".join(f'<i style="flex:{k};background:{c}"></i>' for _, k, c in SORT6)}</div>
{"".join(f'<div class=r><i style="background:{c}"></i><span>{a}</span><b>{k} kg</b></div>' for a, k, c in SORT6)}</div>
<div class="dk6 rd62"><span class=sm6>READY FOR REELING</span><b>{SORT6[0][1]} kg</b><span>good cocoons from L-22, from Tue 24 Nov</span></div></div></div>''',
css=f""".w62{{flex:1;display:grid;grid-template-columns:minmax(0,1.1fr) minmax(0,.9fr);gap:16px;min-height:0}}
.lt62{{padding:18px 22px;display:flex;flex-direction:column;gap:6px;border:3px solid {GD6}}}.hd62{{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}}
.lt62 .r{{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid #ece3c9;gap:10px}}.lt62 .r span{{font:500 18px/1.3 Inter;color:#6f7464}}.lt62 .r b{{font:700 21px/1.3 Inter;text-align:right}}
.rt62{{display:flex;flex-direction:column;gap:16px;min-height:0}}.so62{{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px}}
.sb62{{display:flex;height:34px;border-radius:10px;overflow:hidden;gap:3px}}.sb62 i{{display:block}}
.so62 .r{{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #ece3c9}}.so62 .r i{{width:20px;height:20px;border-radius:6px;flex:none}}.so62 .r span{{font:600 22px/1.3 Inter}}.so62 .r b{{margin-left:auto;font:700 36px/1.4 Cardo}}
.rd62{{padding:20px 22px;display:flex;flex-direction:column;gap:4px}}.rd62 b{{font:700 72px/1.35 Cardo;color:#f1d58f}}.rd62>span:last-child{{font:500 18px/1.4 Inter;color:#d9e0d3}}""")

BS6 = [("B1", "L-22", 10, 1.3, "Reeling"), ("B2", "L-22", 10, 1.4, "Reeling"), ("B3", "L-22", 9.5, 1.2, "Reeling"), ("B4", "L-21", 10, 1.1, "Reeling"), ("B5", "L-23", 8, 0.9, "Reeling"), ("B6", None, 0, 0, "Free at 2 PM")]
IN22 = sum(b[2] for b in BS6 if b[1] == "L-22"); SILK22 = round(sum(b[3] for b in BS6 if b[1] == "L-22"), 1)
LEFT23 = 55 - sum(b[2] for b in BS6 if b[1] == "L-23")
P["p416_silk_s3"] = t6(3, "2 · BASIN BOARD", "Which lot is in which basin?<br><span>See it on one board.</span>",
f'''<div class=w63><div class="cd6 bb63"><div class="r hd"><span>BASIN</span><span>LOT</span><span>COCOONS IN</span><span>SILK SO FAR</span><span>STATUS</span></div>
{"".join(f'<div class=r><div class=bn>{basin6(l, k)}<b>{b}</b></div><div>{chip6(l) if l else "<em class=nl>—</em>"}</div><strong>{f"{c:g} kg" if c else "—"}</strong><strong>{f"{s:g} kg" if s else "—"}</strong><em class="{"fr" if not l else ""}">{st}</em></div>' for k, (b, l, c, s, st) in enumerate(BS6))}</div>
<div class=bt63><div class="dk6 pg63"><span class=sm6>L-22 · TUE 24 NOV · SAMPLE</span><b>{IN22:g} of {SORT6[0][1]} kg</b><span>in basins, {SILK22:g} kg silk so far</span><div class=pb><i style="width:{IN22 / SORT6[0][1] * 100:.0f}%"></i></div></div>
<div class="cd6 nx63"><span class=sm6>NEXT</span><p>B6 is free at 2 PM. Give it L-23: {LEFT23} kg left.</p></div></div></div>''',
css=f""".w63{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.bb63{{flex:1;padding:14px 22px;display:flex;flex-direction:column;min-height:0}}
.bb63 .r{{flex:1;display:grid;grid-template-columns:150px 110px 1fr 1fr 170px;gap:12px;align-items:center;border-top:1px solid #ece3c9}}.bb63 .r.hd{{flex:none;border:0;padding-bottom:8px;font:700 13px/1.4 Inter;letter-spacing:2px;color:#6f7464}}
.bn{{display:flex;align-items:center;gap:12px}}.bn b{{font:700 30px/1.35 Cardo}}.bb63 strong{{font:700 22px/1.3 Inter}}
.bb63 em{{font:700 15px/1.2 Inter;font-style:normal;text-align:center;border-radius:10px;padding:9px 6px;background:#e3eddd;color:{G6}}}.bb63 em.fr{{background:#f6e3c2;color:#8a5a10}}.bb63 em.nl{{background:none;font-size:22px;color:#9aa08f}}
.bt63{{display:grid;grid-template-columns:1.1fr .9fr;gap:16px}}.pg63{{padding:18px 22px;display:flex;flex-direction:column;gap:4px}}.pg63 b{{font:700 52px/1.35 Cardo;color:#f1d58f}}.pg63>span:nth-child(3){{font:500 17px/1.4 Inter;color:#d9e0d3}}
.pg63 .pb{{height:14px;border-radius:7px;background:rgba(255,255,255,.18);overflow:hidden;margin-top:8px}}.pg63 .pb i{{display:block;height:100%;background:{GD6}}}
.nx63{{padding:18px 22px;display:flex;flex-direction:column;gap:8px;background:#f6e3c2}}.nx63 .sm6{{color:#8a5a10}}.nx63 p{{font:700 30px/1.4 Cardo;text-wrap:pretty}}""")

DONE6 = [("L-18", "F-08", 60, 8.6), ("L-19", "F-03", 55, 6.5), ("L-20", "F-11", 48, 6.0)]
RT6 = {l: round(c / s, 1) for l, f, c, s in DONE6}
BEST6 = min(DONE6, key=lambda d: RT6[d[0]]); WORST6 = max(DONE6, key=lambda d: RT6[d[0]])
def hanks6(s, uid, dashed=False):
    full = int(s); part = round(s - full, 2)
    return "".join(hank6(col=GD6, uid=f"{uid}{k}", dashed=dashed) for k in range(full)) + (hank6(part, uid=f"{uid}p") if part > 0 else "")
P["p416_silk_s4"] = t6(4, "3 · SILK PER LOT", "How much silk from each lot?<br><span>Know it, then buy better.</span>",
f'''<div class=w64><div class="cd6 yl64"><div class=hd64><span class=sm6>LOTS FINISHED THIS WEEK · SAMPLE</span><span class=lgd64>{hank6(uid="lg")} = 1 kg raw silk</span></div>
{"".join(f'<div class=r><div class=lb>{chip6(l)}<span>Farmer {f}<br>{c} kg cocoons</span></div><div class=hk>{hanks6(s, l)}</div><div class=nm><b>{s:g} kg</b><span>{RT6[l]:g} kg cocoons<br>per kg silk</span></div></div>' for l, f, c, s in DONE6)}
<div class="r ip"><div class=lb>{chip6("L-22")}<span>Farmer F-08<br>{IN22:g} kg so far</span></div><div class=hk>{hanks6(SILK22, "ip")}</div><div class=nm><b>{SILK22:g} kg</b><span>reeling now<br>(basins 1 to 3)</span></div></div></div>
<div class="dk6 in64"><span class=sm6>WHAT THE NUMBERS SAY</span><p>Lot {BEST6[0]} from farmer {BEST6[1]} gave the most silk: {RT6[BEST6[0]]:g} kg of cocoons for 1 kg. {WORST6[0]} needed {RT6[WORST6[0]]:g} kg. Buy from {BEST6[1]} again.</p></div></div>''',
css=f""".w64{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.yl64{{flex:1;padding:16px 22px;display:flex;flex-direction:column;min-height:0}}
.hd64{{display:flex;justify-content:space-between;align-items:center;padding-bottom:6px}}.lgd64{{display:flex;align-items:center;gap:8px;font:600 15px/1.3 Inter}}.lgd64 svg{{width:16px!important;height:38px!important}}
.yl64 .r{{flex:1;display:grid;grid-template-columns:200px 1fr 190px;gap:14px;align-items:center;border-top:1px solid #ece3c9}}.lb{{display:flex;flex-direction:column;gap:6px;align-items:flex-start}}.lb span{{font:500 16px/1.4 Inter;color:#6f7464}}
.hk{{display:flex;gap:4px;align-items:center}}.nm b{{display:block;font:700 34px/1.35 Cardo}}.nm span{{font:500 15px/1.4 Inter;color:#6f7464}}
.yl64 .r.ip{{background:#fbf3dc;border-radius:16px;border-top:0;padding:0 10px;margin-top:6px}}
.in64{{padding:20px 26px;display:flex;flex-direction:column;gap:8px}}.in64 p{{font:700 28px/1.45 Cardo;text-wrap:pretty}}""")

P["p416_silk_s5"] = t6(5, "SILK REELING APP", "Run a reeling unit?<br><span>Let's build your lot tracker.</span>",
f'''<div class=w65><div class=tl65>{"".join(f'<div class=cd6><i>{n}</i><b>{a}</b><span>{b}</span></div>' for n, a, b in [("01", "Lot cards", "Weight, farmer, sorting"), ("02", "Basin board", "Which lot, which basin"), ("03", "Silk per lot", "Cocoons per kg of silk"), ("04", "Farmer ledger", "Every lot, every week")])}</div>
<div class=hr65>{hanks6(9, "c5")}</div>
<div class="dk6 q65"><span class=sm6>A QUESTION FOR REELERS</span><p>How do you know which basin has which lot today: chalk on the wall, a register, or you just remember? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{GD6};color:{K6}",
css=f""".w65{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl65{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl65>div{{padding:20px 26px 24px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}}.tl65 i{{margin-bottom:auto;align-self:flex-end;font:700 96px/1.3 Cardo;font-style:normal;color:#e9dcb6}}
.tl65 b{{position:relative;font:700 40px/1.35 Cardo}}.tl65 span{{position:relative;font:500 21px/1.4 Inter;color:#6f7464}}
.hr65{{display:flex;justify-content:center;gap:22px}}
.q65{{padding:24px 30px;display:flex;flex-direction:column;gap:10px}}.q65 p{{font:700 31px/1.45 Cardo;text-wrap:pretty}}""")
