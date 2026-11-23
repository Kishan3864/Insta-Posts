import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 386 INDIA · Vermicompost unit · SINGLE · Montserrat + Open Sans · compost brown / leaf green / straw
# New technique: CSS top-down compost beds (brick border, crumbly dotted texture, straw cover band) with a week-of-cycle
# meter; orders are allocated first-in-first-out to the beds by ready week in Python, and the board shows each allocation.
CYC6 = 8
BD6 = [("Bed 1", 8, 40), ("Bed 2", 7, 38), ("Bed 3", 5, 36), ("Bed 4", 3, 40), ("Bed 5", 1, 38), ("Bed 6", 0, 0)]
OD6 = [("O-11", "Sample Nursery", 30, 0), ("O-12", "Sample Farmer Group", 45, 1), ("O-13", "Sample Garden Shop", 12, 3)]
def ready6(w): return max(0, CYC6 - w)
def alloc6():
    left = {b: n for b, w, n in BD6 if w}
    out = []
    for o, who, need, by in OD6:
        parts = []
        for b, w, n in sorted(BD6, key=lambda x: ready6(x[1])):
            if not w or ready6(w) > by or left[b] == 0 or need == 0: continue
            t = min(need, left[b]); left[b] -= t; need -= t; parts.append((b, t))
        out.append((o, who, sum(t for _, t in parts), by, parts, need))
    return out
AL6 = alloc6()
def wk6(r): return "this week" if r == 0 else ("next week" if r == 1 else f"in {r} weeks")
def bed6(b, w, n):
    if not w: return f'<div class="bd6 em"><div class=sf><span>Empty · refill</span></div><b>{b}</b><span class=st>Fill with dung and waste</span></div>'
    r = ready6(w)
    return f'''<div class="bd6 {"rd" if r == 0 else ""}"><div class=sf><i class=sw></i></div><b>{b}</b><div class=mt>{"".join(f'<i class="{"on" if k < w else ""}"></i>' for k in range(CYC6))}</div><span class=st>Week {w} of {CYC6} · {"Ready now" if r == 0 else ("Ready " + wk6(r))}</span><span class=bg>About {n} bags</span></div>'''
P["p386_vermi"] = page("""
body{--f:'Open Sans';--h:'Montserrat';background:#f3efe4;color:#2b2118}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#4f7d2c;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:62px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#7a4b25}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm6{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#7a6a55}
.bs6{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(43,33,24,.08)}
.gd6{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.bd6{display:flex;flex-direction:column;gap:6px}
.bd6 .sf{height:86px;border-radius:8px;border:7px solid #b0573a;border-image:repeating-linear-gradient(90deg,#b0573a 0 22px,#8c4029 22px 24px) 7;background:radial-gradient(circle,#3b2a1c 1.5px,transparent 2px) 0 0/9px 9px,radial-gradient(circle,#6e4a2e 2px,transparent 2.5px) 4px 5px/11px 11px,#5a3c25;position:relative;overflow:hidden}
.bd6 .sw{position:absolute;left:0;right:0;top:0;height:22px;background:repeating-linear-gradient(80deg,#e0c27a 0 3px,#cfae5f 3px 6px)}
.bd6.rd .sf{box-shadow:0 0 0 4px #4f7d2c}.bd6.rd .sw{display:none}
.bd6.em .sf{background:#efe9db;display:flex;align-items:center;justify-content:center}.bd6.em .sf span{font:600 15px/1.3 'Open Sans';color:#8a7a62}
.bd6 b{font:800 20px/1.2 Montserrat}.bd6 .bg{font:700 16px/1.3 'Open Sans';color:#7a4b25}.bd6 .st{font:500 15px/1.35 'Open Sans';color:#5f5242}
.mt{display:grid;grid-template-columns:repeat(8,1fr);gap:3px}.mt i{height:9px;border-radius:3px;background:#e7dfcd}.mt i.on{background:#7aa84a}.bd6.rd .mt i.on{background:#4f7d2c}
.od6{flex:1;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(43,33,24,.08);min-height:0}
.or6{flex:1;display:grid;grid-template-columns:1.5fr .8fr 1.6fr;gap:14px;align-items:center;border-top:1px solid #efe8d8}
.or6 b{display:block;font:700 19px/1.3 Montserrat}.or6 span{font:500 15px/1.35 'Open Sans';color:#6a5c49}
.or6 .q b{font-size:26px;color:#7a4b25}
.pt6{display:flex;flex-wrap:wrap;gap:6px}.pt6 i{font:700 17px/1.2 'Open Sans';font-style:normal;background:#e8f1dc;color:#3a6420;border-radius:12px;padding:10px 14px;display:flex;gap:8px;align-items:center}.pt6 i::before{content:'';width:22px;height:14px;border-radius:3px;background:#5a3c25;box-shadow:0 0 0 2px #b0573a}
.ms6{background:#2b2118;color:#fff;border-radius:22px;padding:14px 20px;display:flex;gap:16px;align-items:center}.ms6 .sm6{color:#d8c49a;white-space:nowrap}.ms6 p{font:500 18px/1.45 'Open Sans';text-wrap:pretty}
""", "<div class=kk>VERMICOMPOST UNIT · BEDS AND ORDERS</div><h1>Buyer asks “Is it ready?”<br><span>Track every bed by week.</span></h1>",
f'''<div class=vw><div class=bs6><span class=sm6>COMPOST BEDS · {CYC6}-WEEK CYCLE · 1 BAG = 25 KG · SAMPLE</span><div class=gd6>{"".join(bed6(*b) for b in BD6)}</div></div>
<div class=od6><span class=sm6>ORDERS · FILLED FROM THE BEDS THAT ARE READY FIRST</span>{"".join(f'<div class=or6><div><b>{o} · {who}</b><span>Wants it {wk6(by)}</span></div><div class=q><b>{got}</b><span>{pl(got, "bag")}{" ready" if not short else f", {short} short"}</span></div><div class=pt6>{"".join(f"<i>{b} · {t}</i>" for b, t in parts)}</div></div>' for o, who, got, by, parts, short in AL6)}</div>
<div class=ms6><span class=sm6>AUTO MESSAGE</span><p>{AL6[1][0]}: {AL6[1][2]} bags for {AL6[1][1]}, ready {wk6(AL6[1][3])} from {" and ".join(b for b, _ in AL6[1][4])}.</p></div></div>''',
"#2b2118", "Make vermicompost? DM us", "background:#4f7d2c;color:#fff")


# ───────── 387 INDIA · Tractor repair workshop · CAROUSEL 5 · Archivo Black + Inter · engine orange / grease black / denim blue
# New technique: SVG top-down workshop yard (bays drawn as floor stripes, top-view tractors with big rear tyres) where each
# tractor carries its job tag; the same job list feeds the paper job card, the 4-column status board and the history line.
JB7 = [("J-201", "Sample 45 HP", "Clutch slipping", "work"), ("J-202", "Sample 35 HP", "Hydraulic lift slow", "parts"), ("J-203", "Sample 50 HP", "Self start not working", "ready"),
       ("J-204", "Sample 45 HP", "Oil leak, lift slow", "check"), ("J-205", "Sample 30 HP", "Brake noise", "work"), ("J-206", "Sample 55 HP", "Radiator leak", "parts"),
       ("J-207", "Sample 40 HP", "Gear hard to change", "check"), ("J-208", "Sample 45 HP", "Battery and wiring", "ready")]
CL7 = {"check": ("Checking", "#5b7fa6"), "parts": ("Waiting for parts", "#d9822b"), "work": ("Working", "#2f2f33"), "ready": ("Ready", "#2f8a57")}
def ttop7(col, tag):
    return f'''<g><rect x="-26" y="-44" width="52" height="88" rx="10" fill="{col}"/><rect x="-44" y="10" width="20" height="36" rx="5" fill="#1b1b1e"/><rect x="24" y="10" width="20" height="36" rx="5" fill="#1b1b1e"/>
<rect x="-36" y="-40" width="12" height="20" rx="4" fill="#1b1b1e"/><rect x="24" y="-40" width="12" height="20" rx="4" fill="#1b1b1e"/><rect x="-16" y="4" width="32" height="26" rx="5" fill="#e9e4da"/>
<rect x="-30" y="-74" width="60" height="24" rx="6" fill="#fff" stroke="{col}" stroke-width="3"/></g>'''
def yard7(w=900):
    pos = [(90, 120), (230, 120), (370, 120), (510, 120), (90, 300), (230, 300), (370, 300), (510, 300)]
    bays = "".join(f'<rect x="{x - 62}" y="{y - 86}" width="124" height="160" rx="8" fill="none" stroke="#d6cfc2" stroke-width="3" stroke-dasharray="10 8"/>' for x, y in pos)
    tr = "".join(f'<g transform="translate({x} {y + 10})">{ttop7(CL7[j[3]][1], j[0])}</g><text x="{x}" y="{y - 46}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="16" fill="#1b1b1e">{j[0]}</text>' for (x, y), j in zip(pos, JB7))
    return f'<svg viewBox="0 0 600 400" width="600" style="display:block;zoom:{w / 600:.3f}"><rect x="0" y="0" width="600" height="400" rx="16" fill="#f1ece3"/>{bays}{tr}</svg>'
B7 = """
body{--f:'Inter';--h:'Archivo Black';background:#f4f0e8;color:#1b1b1e}
.kk{font:800 16px/1.4 Inter;letter-spacing:3px;color:#d9622b;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:54px;line-height:1.22;letter-spacing:-.5px;margin-top:14px} h1 span{color:#d9622b}
.cd7{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(27,27,30,.08)}
.sm7{font:800 13px/1.4 Inter;letter-spacing:2px;color:#6d675c}
.lg7{display:flex;gap:14px;flex-wrap:wrap}.lg7 span{display:flex;gap:6px;align-items:center;font:600 15px/1.2 Inter;color:#4a463e}.lg7 i{width:16px;height:16px;border-radius:4px}
"""
def t7(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1b1b1e;color:#ffb27a"):
    return page(B7 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1b1b1e", cta, ctacss, tagline=f"{n} / 5")
LEG7 = '<div class=lg7>' + "".join(f'<span><i style="background:{c}"></i>{t}</span>' for t, c in CL7.values()) + '</div>'
P["p387_tractor_s1"] = t7(1, "TRACTOR REPAIR WORKSHOP · HARVEST SEASON", "8 tractors in the yard?<br><span>Give each one a job card.</span>",
f'''<div class=w71><div class="cd7 yd71"><div class=h><span class=sm7>YOUR YARD TODAY · SAMPLE</span>{LEG7}</div>{yard7()}</div>
<div class=pn71>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [("“Is my tractor done?”", "10 calls before noon"), ("“Which part did we order?”", "Written on the wall"), ("“What did you fix last time?”", "No record of old repairs")])}</div></div>''',
css=""".w71{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.yd71{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:10px;justify-content:center}.yd71 .h{display:flex;justify-content:space-between;align-items:center;gap:10px}
.pn71{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.pn71>div{background:#1b1b1e;color:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.pn71 b{font:800 19px/1.3 Inter}.pn71 span{font:500 16px/1.35 Inter;color:#c9c3b8}""")
J7 = JB7[3]
P["p387_tractor_s2"] = t7(2, "1 · JOB CARD AT THE GATE", "Photo, problem, phone.<br><span>Written once, seen by all.</span>",
f'''<div class=w72><div class=jc72><div class=hd><b>JOB CARD</b><span>{J7[0]}</span></div>{"".join(f'<div class=ln><span>{a}</span><b>{b}</b></div>' for a, b in [("Farmer", "Sample Farmer, Sample Village"), ("Phone", "98XXX XXXXX"), ("Tractor", J7[1]), ("Hour meter", "3,420 hrs"), ("In at", "Mon 9:10 AM")])}
<div class=pb><span>Problem</span><div>{"".join(f'<i>{p}</i>' for p in ["Oil leak", "Lift slow", "Check brakes"])}</div></div>
<div class=ph>{"".join(f'<div>{ic("camera", 30, "#8a8276", 1.8)}<span>{t}</span></div>' for t in ["Leak", "Lift arm", "Meter"])}</div>
<div class=ln><span>Promised</span><b>Wed evening</b></div></div>
<div class=rt72><div class="cd7 ms72"><span class=sm7>MESSAGE TO THE FARMER · 9:12 AM</span><p>Job {J7[0]} opened for your {J7[1]}: oil leak and lift slow. We will call you after checking. Expected Wednesday evening.</p></div>
<div class="cd7 wh72"><span class=sm7>WHO SEES THE CARD</span>{"".join(f'<div><span class=ib>{ic(i, 24)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("users", "Mechanic", "Problem and photos"), ("box", "Parts counter", "What to order"), ("phone", "Owner", "All jobs, any time")])}</div></div></div>''',
css=""".w72{flex:1;display:grid;grid-template-columns:1.1fr 1fr;gap:16px;min-height:0}
.jc72{background:#fffaf0;border:2px solid #e3d7bf;border-radius:10px;padding:20px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 18px 34px rgba(27,27,30,.10);background-image:linear-gradient(#d9622b,#d9622b);background-size:100% 8px;background-repeat:no-repeat}
.jc72 .hd{display:flex;justify-content:space-between;align-items:center;margin-top:6px;padding-bottom:10px;border-bottom:2px solid #e3d7bf}.jc72 .hd b{font:400 26px/1.3 'Archivo Black';letter-spacing:1px}.jc72 .hd span{font:800 20px/1.2 Inter;color:#d9622b}
.jc72 .ln{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;border-bottom:1px dashed #e3d7bf}.jc72 .ln span,.jc72 .pb>span{font:600 16px/1.3 Inter;color:#6d675c}.jc72 .ln b{font:700 18px/1.3 Inter;text-align:right}
.jc72 .pb{display:flex;flex-direction:column;gap:8px;padding:6px 0}.jc72 .pb div{display:flex;gap:6px;flex-wrap:wrap}.jc72 .pb i{font:700 15px/1.2 Inter;font-style:normal;background:#ffe3d1;color:#a8471b;border-radius:10px;padding:7px 11px}
.jc72 .ph{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.jc72 .ph>div{height:84px;border-radius:10px;background:#ece5d6;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}.jc72 .ph span{font:600 13px/1.2 Inter;color:#6d675c}
.rt72{display:flex;flex-direction:column;gap:14px}.ms72{padding:18px 20px;display:flex;flex-direction:column;gap:10px;background:#e8f3e4}.ms72 p{font:500 19px/1.45 Inter;text-wrap:pretty}
.wh72{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:8px}.wh72>div{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #efe9de}
.wh72 .ib{width:48px;height:48px;border-radius:14px;background:#1b1b1e;color:#ffb27a}.wh72 b{display:block;font:800 19px/1.3 Inter}.wh72 div span{font:500 16px/1.35 Inter;color:#6d675c}""")
PT7 = [("J-202", "Hydraulic pump seal kit", "Arrives Thu"), ("J-206", "Radiator core", "Arrives Wed"), ("J-201", "Clutch plate", "In stock"), ("J-207", "Gear lever bush", "Check first")]
PR7 = {"J-201": "Tue", "J-202": "Fri", "J-203": "Today", "J-204": "Wed", "J-205": "Tue", "J-206": "Thu", "J-207": "Wed", "J-208": "Today"}
P["p387_tractor_s3"] = t7(3, "2 · SEE WHAT IS WAITING", "Which jobs wait for parts?<br><span>One board, four columns.</span>",
f'''<div class=w73><div class=bd73>{"".join(f'<div class=cl style="--c:{c}"><div class=hd><b>{t}</b><span>{sum(1 for j in JB7 if j[3] == k)}</span></div>' + "".join(f'<div class=cr><b>{j[0]}</b><span>{j[1]}</span><em>{j[2]}</em><small>Promised {PR7[j[0]]}</small></div>' for j in JB7 if j[3] == k) + '</div>' for k, (t, c) in CL7.items())}</div>
<div class="cd7 pt73"><span class=sm7>PARTS ORDERED · SAMPLE</span>{"".join(f'<div><b>{j}</b><span>{p}</span><em>{d}</em></div>' for j, p, d in PT7)}</div></div>''',
css=""".w73{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.bd73{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;min-height:0}
.bd73 .cl{background:#fff;border-radius:20px;padding:12px;display:flex;flex-direction:column;gap:10px;box-shadow:0 12px 24px rgba(27,27,30,.07);border-top:8px solid var(--c)}
.bd73 .hd{display:flex;justify-content:space-between;align-items:center;gap:6px}.bd73 .hd b{font:800 17px/1.25 Inter}.bd73 .hd span{min-width:32px;height:32px;border-radius:10px;background:var(--c);color:#fff;font:800 17px/32px Inter;text-align:center}
.bd73 .cr{background:#f6f2ea;border-radius:14px;padding:12px;display:flex;flex-direction:column;gap:4px;border-left:5px solid var(--c)}.bd73 .cr b{font:800 20px/1.25 Inter}.bd73 .cr span{font:600 15px/1.3 Inter;color:#6d675c}.bd73 .cr em{font:500 16px/1.35 Inter;font-style:normal}.bd73 .cr small{font:700 13px/1.3 Inter;color:var(--c);margin-top:4px}
.pt73{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:8px}.pt73>div{flex:1;display:grid;grid-template-columns:90px 1fr auto;gap:12px;align-items:center;border-top:1px solid #efe9de;padding-top:8px}
.pt73 b{font:800 20px/1.3 Inter}.pt73 span{font:500 19px/1.3 Inter}.pt73 em{font:700 15px/1.2 Inter;font-style:normal;background:#ffe9d6;color:#a8471b;border-radius:10px;padding:7px 10px}""")
HS7 = [("Mar 2025", "2,610 hrs", "Engine oil and filters"), ("Oct 2025", "2,980 hrs", "Clutch plate changed"), ("Apr 2026", "3,190 hrs", "Battery replaced"), ("Nov 2026", "3,420 hrs", "Oil seal, lift valve")]
P["p387_tractor_s4"] = t7(4, "3 · READY MESSAGE AND HISTORY", "Tell the farmer it's ready.<br><span>Keep every repair on record.</span>",
f'''<div class=w74><div class="cd7 rd74"><span class=sm7>READY MESSAGE · WED 5:40 PM</span><p>Your {J7[1]} ({J7[0]}) is ready. Work done: oil seal changed, lift valve set, brakes checked. Please collect before 7 PM.</p><div class=ch>{"".join(f'<i>{t}</i>' for t in ["Bill attached", "Old parts kept for you"])}</div></div>
<div class="cd7 hs74"><span class=sm7>{J7[1].upper()} · SAMPLE FARMER · REPAIR HISTORY</span><div class=tl>{"".join(f'<div class="{"nw" if k == len(HS7) - 1 else ""}"><i></i><b>{d}</b><span>{h}</span><em>{w}</em></div>' for k, (d, h, w) in enumerate(HS7))}</div>
<div class=nx><b>Next service due</b><span>at about 3,670 hrs · reminder by message</span></div></div></div>''',
css=""".w74{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rd74{padding:20px 22px;display:flex;flex-direction:column;gap:12px;background:#e8f3e4}.rd74 p{font:500 22px/1.45 Inter;text-wrap:pretty}
.rd74 .ch{display:flex;gap:8px}.rd74 .ch i{font:700 15px/1.2 Inter;font-style:normal;background:#fff;color:#2f8a57;border-radius:10px;padding:8px 12px}
.hs74{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:14px}.hs74 .tl{flex:1;display:flex;flex-direction:column;position:relative}
.hs74 .tl::before{content:'';position:absolute;left:12px;top:20px;bottom:20px;width:4px;background:#e3d7bf}
.hs74 .tl>div{flex:1;position:relative;display:grid;grid-template-columns:44px 150px 130px 1fr;align-items:center;border-bottom:1px solid #efe9de}.hs74 .tl>div:last-child{border:0}
.hs74 .tl i{width:28px;height:28px;border-radius:50%;background:#1b1b1e;border:5px solid #fff;box-sizing:border-box;position:relative}.hs74 .tl .nw i{background:#d9622b}
.hs74 .tl b{font:800 21px/1.3 Inter}.hs74 .tl span{font:700 17px/1.3 Inter;color:#d9622b}.hs74 .tl em{font:500 20px/1.4 Inter;font-style:normal;color:#3d3a34}
.hs74 .nx{background:#1b1b1e;color:#fff;border-radius:16px;padding:14px 18px;display:flex;justify-content:space-between;align-items:center;gap:10px}.hs74 .nx b{font:800 19px/1.3 Inter;color:#ffb27a}.hs74 .nx span{font:500 17px/1.3 Inter}""")
P["p387_tractor_s5"] = t7(5, "YOUR TURN", "Repair tractors?<br><span>Let's build your workshop app.</span>",
f'''<div class=w75><div class="cd7 pv75"><span class=sm7>TODAY · 8 TRACTORS · SAMPLE</span>{yard7(500)}<div class=ct75>{"".join(f'<div style="--c:{c}"><b>{sum(1 for j in JB7 if j[3] == k)}</b><span>{t}</span></div>' for k, (t, c) in CL7.items())}</div></div>
<div class=td75>{"".join(f'<div class=ti75><span class=ib>{ic(i, 30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("doc", "Job cards", "Photo, problem, phone"), ("grid", "Status board", "Checking to ready"), ("box", "Parts list", "Ordered and arriving"), ("clock", "History", "Every repair saved")])}</div>
<div class=q75>How do farmers ask about their tractor today, calls or visits? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#d9622b;color:#fff",
css=""".w75{flex:1;display:grid;grid-template-columns:1.1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.pv75{display:flex;flex-direction:column;justify-content:center;gap:16px;padding:18px}.ct75{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.ct75>div{border-top:6px solid var(--c);background:#f6f2ea;border-radius:12px;padding:10px 6px;text-align:center;display:flex;flex-direction:column;gap:2px}.ct75 b{font:400 30px/1.25 'Archivo Black'}.ct75 span{font:600 13px/1.25 Inter;color:#4a463e}
.td75{display:flex;flex-direction:column;gap:12px}.ti75{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(27,27,30,.07)}
.ti75 .ib{width:58px;height:58px;border-radius:18px;background:#1b1b1e;color:#ffb27a}.ti75 b{display:block;font:800 23px/1.3 Inter}.ti75 div span{font:500 17px/1.4 Inter;color:#6d675c}
.q75{grid-column:1 / 3;background:#1b1b1e;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 Inter}""")


# ───────── 388 USA · Mobile mechanic · SINGLE · Poppins + Roboto · navy / signal yellow / driveway grey
# New technique: CSS cargo-van cutaway (body, wheel arches, shelf rails) whose bins are coloured per job and labelled
# with the parts for that stop; booking form -> parts list -> bins -> route all come from one job list.
JB8 = [("M-41", "8:30 AM", "ZIP 00011", "2017 sample sedan", "Front brakes squeak", ["Front pads", "Front rotors x2", "Brake cleaner"], "#ffc83d"),
       ("M-42", "10:45 AM", "ZIP 00014", "2015 sample SUV", "Battery dead", ["Battery, group 48", "Terminal kit"], "#6cc3a0"),
       ("M-43", "1:15 PM", "ZIP 00014", "2019 sample pickup", "Oil change, 5k miles", ["Oil filter", "6 qt oil", "Drain plug gasket"], "#7aa7e0"),
       ("M-44", "3:30 PM", "ZIP 00018", "2012 sample hatchback", "Belt squeal", ["Serpentine belt", "Tensioner"], "#f08a6b")]
J8 = JB8[0]
P["p388_mobilemech"] = page("""
body{--f:'Roboto';--h:'Poppins';background:#eef0f3;color:#13294b}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#c98a00;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:64px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#2b5fa8}
.vw{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}
.sm8{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#5d6b80}
.tp8{display:grid;grid-template-columns:1fr auto 1fr;gap:12px;align-items:stretch}
.fm8{background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(19,41,75,.08)}
.fd8{display:flex;justify-content:space-between;align-items:center;gap:10px;border-top:1px solid #e8ebf0;padding:7px 0}.fd8 small{font:500 15px/1.3 Roboto;color:#5d6b80}.fd8 b{font:600 17px/1.3 Roboto;text-align:right}
.ar8{display:flex;align-items:center;color:#2b5fa8}
.pl8{background:#13294b;color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}.pl8 .sm8{color:#aebbd0}
.pl8 .it{flex:1;display:flex;gap:12px;align-items:center;border-top:1px solid rgba(255,255,255,.12)}.pl8 .it i{width:26px;height:26px;border-radius:7px;background:#ffc83d;display:flex;align-items:center;justify-content:center;flex:none}.pl8 .it span{font:500 18px/1.3 Roboto}
.pl8 em{font:500 15px/1.4 Roboto;font-style:normal;color:#cfd8e6}
.vn8{flex:1;justify-content:center;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(19,41,75,.08)}
.van{position:relative;height:330px;margin:0 6px 26px}
.van .bd{position:absolute;inset:0 0 0 0;border-radius:18px 70px 18px 18px;background:#dfe5ee;border:4px solid #13294b}
.van .cb{position:absolute;right:0;top:0;bottom:0;width:150px;border-radius:0 70px 18px 0;border-left:4px dashed #9fb0c8;background:#d3dbe7}.van .cb::after{content:'';position:absolute;left:22px;right:26px;top:26px;height:96px;border-radius:12px 56px 12px 12px;background:#bcd7ef;box-shadow:inset 0 0 0 4px #13294b}
.van .wh{position:absolute;bottom:-26px;width:62px;height:62px;border-radius:50%;background:#13294b;box-shadow:inset 0 0 0 14px #13294b,inset 0 0 0 24px #9aa6b6}
.van .w1{left:90px}.van .w2{right:70px}
.van .sh{position:absolute;left:20px;right:170px;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;height:118px}
.van .s1{top:16px}.van .s2{top:152px}
.van .sh>div{border-radius:10px;padding:8px 10px;display:flex;flex-direction:column;gap:2px;box-shadow:inset 0 -6px 0 rgba(0,0,0,.12)}
.van .sh>div{padding:12px 12px}.van .sh b{font:800 19px/1.2 Roboto;color:#13294b}.van .sh span{font:500 15px/1.35 Roboto;color:#13294b}
.van .rl{position:absolute;left:14px;right:164px;height:5px;background:#13294b;border-radius:3px}.van .r1{top:114px}.van .r2{top:226px}
.rt8{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.rt8>div{background:#fff;border-radius:18px;padding:12px 14px;display:flex;flex-direction:column;gap:4px;box-shadow:0 10px 22px rgba(19,41,75,.07);border-top:8px solid var(--c)}
.rt8>div{gap:6px;padding:14px 16px}.rt8 b{font:800 19px/1.25 Roboto}.rt8 span{font:500 15px/1.35 Roboto;color:#5d6b80}.rt8 em{font:600 17px/1.3 Roboto;font-style:normal}
""", "<div class=kk>MOBILE MECHANIC · DRIVEWAY REPAIRS</div><h1>Wrong part on the van?<br><span>Get the car details first.</span></h1>",
f'''<div class=vw><div class=tp8><div class=fm8><span class=sm8>BOOKING FORM · {J8[0]}</span>{"".join(f'<div class=fd8><small>{a}</small><b>{b}</b></div>' for a, b in [("Year and model", J8[3].capitalize()), ("Engine", "2.0 L, 4 cyl"), ("Problem", J8[4]), ("Photo of the VIN sticker", "Added"), ("Where", f"Driveway · {J8[2]}")])}</div>
<div class=ar8>{ic("arrow", 40, "#2b5fa8", 2.5)}</div>
<div class=pl8><span class=sm8>PARTS PICKED FOR {J8[0]}</span>{"".join(f'<div class=it><i>{ic("check", 16, "#13294b", 3)}</i><span>{p}</span></div>' for p in J8[5])}<em>Matched to year, model and engine · sample</em></div></div>
<div class=vn8><span class=sm8>VAN LOADED BY STOP · ONE BIN PER JOB · SAMPLE</span><div class=van><div class=bd></div><div class=cb></div><i class=rl style="top:138px"></i><i class=rl style="top:274px"></i>
<div class="sh s1">{"".join(f'<div style="background:{c}"><b>{j}</b><span>{p[0]}</span></div>' for j, t, z, car, pr, p, c in JB8)}</div>
<div class="sh s2">{"".join(f'<div style="background:{c}"><b>{j}</b><span>{" · ".join(p[1:])}</span></div>' for j, t, z, car, pr, p, c in JB8)}</div>
<i class="wh w1"></i><i class="wh w2"></i></div></div>
<span class=sm8>TODAY'S ROUTE · 4 STOPS · SAMPLE</span><div class=rt8>{"".join(f'<div style="--c:{c}"><b>{t} · {j}</b><span>{z}<br>{car}</span><em>{pr}</em></div>' for j, t, z, car, pr, p, c in JB8)}</div></div>''',
"#13294b", "Fix cars on site? DM us", "background:#ffc83d;color:#13294b")


# ───────── 389 INDIA · Pet food and supplies shop · SINGLE · Gelasio + DM Sans · paw orange / bowl blue / cream
# New technique: CSS pet food bags (clip-path bag with crimped top and a window showing kibble at the level left), days
# left computed from bag kg, grams per day and days since purchase; reminders and the stock list derive from the same data.
PF9 = [("C-11", "Dog", 10, 300, 28), ("C-12", "Cat", 3, 60, 20), ("C-13", "Dog", 3, 150, 17),
       ("C-14", "Dog", 4, 120, 10), ("C-15", "Cat", 1.5, 50, 27), ("C-16", "Dog", 15, 400, 30)]
def days9(kg, g): return int(kg * 1000 // g)
ROW9 = [(c, p, kg, g, b, days9(kg, g), days9(kg, g) - b) for c, p, kg, g, b in PF9]
DUE9 = [r for r in ROW9 if r[6] <= 7]
def bag9(kg, pct, cat):
    col = "#3d5a99" if cat == "Cat" else "#f07a3a"
    return f'<div class=bg9 style="--c:{col}"><i class=cr></i><div class=wn><i class=kb style="height:{pct:.0f}%"></i></div><b>{kg:g} kg</b></div>'
P["p389_petfood"] = page("""
body{--f:'DM Sans';--h:'Gelasio';background:#fbf4ea;color:#2a2230;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#d4612a;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#3d5a99;font-style:italic}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm9{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7b6f66}
.sh9{flex:1;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:12px;box-shadow:0 14px 30px rgba(42,34,48,.08);min-height:0}
.gd9{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px;min-height:0}
.cl9{display:grid;grid-template-columns:auto 1fr;gap:6px 16px;align-items:center;border-radius:18px;padding:14px 16px;background:#fbf6ef}.cl9 .bg9{grid-row:1 / 5}.cl9>*{justify-self:start}
.cl9.due{background:#fff1e6;box-shadow:inset 0 0 0 2px #f07a3a}
.bg9{width:104px;height:170px;position:relative;flex:none}
.bg9>.cr{position:absolute;left:4px;right:4px;top:0;height:14px;background:repeating-linear-gradient(90deg,var(--c) 0 6px,rgba(0,0,0,.25) 6px 8px);border-radius:3px}
.bg9::before{content:'';position:absolute;left:0;right:0;top:10px;bottom:0;background:var(--c);clip-path:polygon(6% 0,94% 0,100% 100%,0 100%);border-radius:4px}
.bg9 .wn{position:absolute;left:22px;right:22px;top:40px;height:74px;border-radius:10px;background:#fff8ee;overflow:hidden;box-shadow:inset 0 0 0 3px rgba(0,0,0,.15)}
.bg9 .kb{position:absolute;left:0;right:0;bottom:0;background:radial-gradient(circle,#8a5a2b 3.5px,transparent 4px) 0 0/10px 9px,radial-gradient(circle,#b07a3f 3px,transparent 3.5px) 5px 4px/10px 9px,#d9a466}
.bg9 b{position:absolute;left:0;right:0;bottom:10px;text-align:center;font:700 16px/1.2 'DM Sans';color:#fff}
.cl9 strong{font:700 22px/1.2 'DM Sans'}.cl9 span{font:500 15px/1.4 "DM Sans";color:#6b6058}.cl9 .ub{width:100%;height:10px;border-radius:5px;background:#eadfd2;overflow:hidden}.cl9 .ub i{display:block;height:100%;background:#3d5a99}.cl9.due .ub i{background:#f07a3a}
.cl9 em{font:700 15px/1.2 'DM Sans';font-style:normal;border-radius:10px;padding:6px 10px;background:#e8eef9;color:#3d5a99;white-space:nowrap}.cl9.due em{background:#f07a3a;color:#fff}
.bt9{display:grid;grid-template-columns:1.2fr 1fr;gap:14px}
.ms9{background:#e9f3e3;border-radius:24px 24px 24px 6px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}.ms9 .sm9{color:#3e6b2b}.ms9 p{font:500 19px/1.45 'DM Sans';text-wrap:pretty}
.ms9 .bn{display:flex;gap:8px}.ms9 .bn i{font:700 15px/1.2 'DM Sans';font-style:normal;border-radius:12px;padding:9px 14px;background:#3e6b2b;color:#fff}.ms9 .bn i.o{background:#fff;color:#3e6b2b}
.st9{background:#2a2230;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}.st9 .sm9{color:#cbbfd2}
.st9 div{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.12)}.st9 b{font:700 19px/1.3 'DM Sans'}.st9 span{font:500 16px/1.3 'DM Sans';color:#ddd3e3}
""", "<div class=kk>PET FOOD AND SUPPLIES SHOP · REPEAT ORDERS</div><h1>Pet food bag ran out?<br><span>Remind owners first.</span></h1>",
f'''<div class=vw><div class=sh9><span class=sm9>REGULAR CUSTOMERS · DAYS LEFT FROM BAG SIZE AND DAILY GRAMS · SAMPLE</span><div class=gd9>{"".join(f'<div class="cl9 {"due" if l <= 7 else ""}">{bag9(kg, l / d * 100, p)}<strong>{c} · {p}</strong><span>{g} g a day<br>Bought {b}&nbsp;days&nbsp;ago</span><div class=ub><i style="width:{l / d * 100:.0f}%"></i></div><em>{pl(l, "day")} left</em></div>' for c, p, kg, g, b, d, l in ROW9)}</div></div>
<div class=bt9><div class=ms9><span class=sm9>AUTO REMINDER · {DUE9[0][0]}</span><p>Hello! Your {DUE9[0][1].lower()}'s {DUE9[0][2]:g} kg food bag will finish in about {DUE9[0][6]} days. Same bag again?</p><div class=bn><i>Yes, deliver</i><i class=o>Pick up at shop</i></div></div>
<div class=st9><span class=sm9>DUE THIS WEEK · {len(DUE9)} CUSTOMERS</span>{"".join(f'<div><b>{c} · {kg:g} kg {p.lower()} food</b><span>{pl(l, "day")} left</span></div>' for c, p, kg, g, b, d, l in sorted(DUE9, key=lambda r: r[6]))}</div></div></div>''',
"#2a2230", "Run a pet shop? DM us", "background:#f07a3a;color:#fff")


# ───────── 390 USA · Donut shop office pre-orders · SINGLE · TeX Gyre Adventor + Fira Sans · strawberry pink / chocolate / cream
# New technique: CSS donuts (radial-gradient ring: hole, icing, dough edge, sprinkle layer) packed 4×3 in open boxes per
# order; the bake list per flavor is summed from the boxes, so the 5 AM bake sheet matches every pickup.
FL0 = {"Glazed": ("#f6e3b8", None), "Chocolate": ("#5a3626", None), "Strawberry": ("#f28aa6", "#fff"), "Maple": ("#c98a3d", None), "Sprinkle": ("#fff3f6", "#e8557a")}
OR0 = [("D-31", "7:30 AM", "Sample Office A", {"Glazed": 4, "Chocolate": 4, "Strawberry": 4}),
       ("D-32", "8:00 AM", "Sample Clinic Front Desk", {"Glazed": 6, "Maple": 3, "Chocolate": 3}),
       ("D-33", "8:15 AM", "Sample Law Office", {"Strawberry": 4, "Sprinkle": 4, "Maple": 4})]
def dn0(f, s=58):
    ic_, sp = FL0[f]
    spr = f"radial-gradient(circle at 30% 30%,{sp} 2px,transparent 2.5px),radial-gradient(circle at 68% 40%,{sp} 2px,transparent 2.5px),radial-gradient(circle at 45% 72%,{sp} 2px,transparent 2.5px),radial-gradient(circle at 75% 70%,{sp} 2px,transparent 2.5px)," if sp else ""
    return f'<i class=dn0 style="width:{s}px;height:{s}px;background:{spr}radial-gradient(circle,#fff6ec 0 17%,{ic_} 19% 60%,#d9a066 63% 70%,transparent 71%)"></i>'
def box0(o):
    fl = [f for f, n in o[3].items() for _ in range(n)]
    return f'<div class=bx0><div class=lid><b>{o[0]}</b><span>{o[1]}</span></div><div class=gr>{"".join(dn0(f) for f in fl)}</div><div class=ft><b>{o[2]}</b><span>{" · ".join(f"{n}&nbsp;{f.lower()}" for f, n in o[3].items())}</span></div></div>'
BK0 = {f: sum(o[3].get(f, 0) for o in OR0) for f in FL0}
P["p390_donut"] = page("""
body{--f:'Fira Sans';--h:'TeX Gyre Adventor';background:#fff6ec;color:#3a2219}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#d23f66;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;line-height:1.2;letter-spacing:-1px} h1 span{color:#d23f66}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm0{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#86685a}
.bxs{flex:none;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.bx0{background:#fff;border-radius:18px;box-shadow:0 14px 30px rgba(58,34,25,.10);overflow:hidden;display:flex;flex-direction:column}
.bx0 .lid{background:#e8557a;color:#fff;padding:12px 16px;display:flex;justify-content:space-between;align-items:center;background-image:repeating-linear-gradient(90deg,rgba(255,255,255,.14) 0 14px,transparent 14px 28px)}
.bx0 .lid b{font:700 22px/1.2 'TeX Gyre Adventor'}.bx0 .lid span{font:700 16px/1.2 'Fira Sans';background:#fff;color:#d23f66;border-radius:10px;padding:5px 9px}
.bx0 .gr{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:14px;background:#f7efe3;justify-items:center;margin:12px;border-radius:10px;box-shadow:inset 0 0 0 2px #eadcc6}
.dn0{display:block;border-radius:50%;box-shadow:0 3px 5px rgba(58,34,25,.18)}
.bx0 .ft{padding:0 16px 14px;display:flex;flex-direction:column;gap:4px;text-align:center}.bx0 .ft b{font:600 18px/1.3 'Fira Sans'}.bx0 .ft span{font:400 15px/1.4 'Fira Sans';color:#6f5649}
.bt0{flex:1;display:grid;grid-template-columns:1.35fr 1fr;gap:14px;min-height:0}
.bk0{background:#3a2219;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}.bk0 .sm0{color:#e4c8b6}
.bk0 .r{flex:1;display:grid;grid-template-columns:62px 1fr 80px;gap:12px;align-items:center;border-top:1px solid rgba(255,255,255,.12)}
.bk0 .r span{font:500 19px/1.3 'Fira Sans'}.bk0 .r b{font:700 28px/1.2 'TeX Gyre Adventor';text-align:right;color:#ffc2d2}
.bk0 .r .br{height:12px;border-radius:6px;background:rgba(255,255,255,.12);overflow:hidden;margin-top:6px}.bk0 .r .br i{display:block;height:100%;background:#e8557a}
.fm0{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(58,34,25,.08)}
.fm0 .fd{flex:1;display:flex;flex-direction:column;justify-content:center;gap:3px;border-top:1px solid #f1e6d8}.fm0 small{font:500 14px/1.3 'Fira Sans';color:#86685a}.fm0 b{font:600 19px/1.3 'Fira Sans'}
.fm0 .ct{background:#fde4ec;color:#a8264c;border-radius:12px;padding:10px 12px;font:700 16px/1.3 'Fira Sans'}
""", "<div class=kk>DONUT SHOP · OFFICE PRE-ORDERS</div><h1>Office orders by text at 6 AM?<br><span>Pre-order by the dozen.</span></h1>",
f'''<div class=vw><div class=bxs>{"".join(box0(o) for o in OR0)}</div>
<div class=bt0><div class=bk0><span class=sm0>5 AM BAKE LIST · {sum(BK0.values())} DONUTS · 3 DOZEN · SAMPLE</span>{"".join(f'<div class=r>{dn0(f, 50)}<div><span>{f}</span><div class=br><i style="width:{n / max(BK0.values()) * 100:.0f}%"></i></div></div><b>{n}</b></div>' for f, n in BK0.items())}</div>
<div class=fm0><span class=sm0>PRE-ORDER FORM</span>{"".join(f'<div class=fd><small>{a}</small><b>{b}</b></div>' for a, b in [("Name on the box", "Sample Office A"), ("How many", "1 dozen"), ("Mix", "Pick 12, or shop's choice"), ("Pickup", "Tomorrow, 7:30 AM")])}<div class=ct>Orders close at 6 PM the day before</div></div></div></div>''',
"#3a2219", "Run a donut shop? DM us", "background:#e8557a;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
