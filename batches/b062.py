import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 326 INDIA · Agri drone spraying service · CAROUSEL 5 · Poppins + Inter · paddy green / drone orange / khaki cream
# New technique: SVG patchwork village field map (plots tinted by crop, canal, road, numbered booking pins) reused
# across the carousel, plus a lawnmower flight path over one field with the sprayed part solid and the rest dashed.
DR = """
body{--f:'Inter';--h:'Poppins';background:#f2efdf;color:#1f3320}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#d9661f;margin-top:22px;align-self:flex-start}
h1{font-family:'Poppins';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#3f7a2e}
.cd{background:#fffdf4;border-radius:24px;box-shadow:0 12px 28px rgba(31,51,32,.08)}
.cap{font:700 14px/1.4 Inter;letter-spacing:2px;color:#7b7a63}
.nb{display:flex;align-items:center;gap:14px;background:#1f3320;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 Inter}
.nb .ib{width:50px;height:50px;border-radius:14px;background:#f08a3c;color:#1f3320}.nb b{color:#ffc58f}
.mapw{flex:1;min-height:0;display:flex}.mapw svg{width:100%;height:100%;display:block}
.lgx{display:flex;flex-wrap:wrap;gap:18px;font:600 16px/1.4 Inter;color:#3b4a35}.lgx span{display:flex;align-items:center;gap:8px}.lgx i{width:20px;height:20px;border-radius:5px}
"""
CROP = {"Wheat": "#b9d36c", "Mustard": "#f0cf3a", "Chana": "#6fa64a", "Cotton": "#efe9d8"}
FIELDS = [  # id, farmer, village, crop, acres, day
    ("F1", "Farmer 1", "Village A", "Wheat", 2.5, "Tue 24 Nov"), ("F2", "Farmer 2", "Village A", "Mustard", 1.5, "Tue 24 Nov"),
    ("F3", "Farmer 3", "Village A", "Wheat", 3.0, "Tue 24 Nov"), ("F4", "Farmer 4", "Village B", "Chana", 2.0, "Tue 24 Nov"),
    ("F5", "Farmer 5", "Village B", "Cotton", 4.0, "Wed 25 Nov"), ("F6", "Farmer 6", "Village B", "Mustard", 1.0, "Wed 25 Nov"),
    ("F7", "Farmer 7", "Village C", "Wheat", 2.0, "Wed 25 Nov")]
FC = {f[0]: CROP[f[3]] for f in FIELDS}
def fieldmap(W, H, pins="num", done=()):
    random.seed(326)
    cols = [0.2, 0.16, 0.22, 0.18, 0.24]
    plots, x = [], 0
    for ci, cw in enumerate(cols):
        w = cw * W; n = random.choice([3, 4]); cuts = sorted(random.uniform(.15, .85) for _ in range(n - 1))
        ys = [0] + cuts + [1]
        for a, b in zip(ys, ys[1:]):
            plots.append((x, a * H, w, (b - a) * H))
        x += w
    L = len(plots); pick = {3: "F1", 5: "F2", 8: "F3", 10: "F4", 12: "F5", L - 3: "F6", L - 1: "F7"}
    fall = ["#d9d0ae", "#cfd8a6", "#e3dcc0", "#c9c19c"]
    s = f'<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid meet"><rect width="{W}" height="{H}" rx="18" fill="#cfc6a0"/>'
    lab = ""
    for i, (px, py, pw, ph) in enumerate(plots):
        fid = pick.get(i)
        fill = FC[fid] if fid else fall[i % 4]
        s += f'<rect x="{px+4:.0f}" y="{py+4:.0f}" width="{pw-8:.0f}" height="{ph-8:.0f}" rx="6" fill="{fill}"/>'
        # furrow lines
        for k in range(int(pw // 18)):
            s += f'<line x1="{px+14+k*18:.0f}" y1="{py+10:.0f}" x2="{px+14+k*18:.0f}" y2="{py+ph-10:.0f}" stroke="#000" stroke-opacity=".05" stroke-width="3"/>'
        if fid:
            cx, cy = px + pw / 2, min(max(py + ph / 2, 62), H - 20)
            for vx, vy in [(W * .04, H * .04), (W * .62, H * .06), (min(W * .70, W - 162), H * .84)]:
                if vx - 30 < cx < vx + 180 and vy - 40 < cy - 22 < vy + 80: cy = vy + 120 if vy < H / 2 else vy - 50
            if pins == "q":
                col, t = "#d9661f", "?"
            elif pins == "done":
                col, t = ("#2f7a3a" if fid in done else "#d9661f"), fid
            else:
                col, t = "#1f3320", fid
            lab += f'<g transform="translate({cx:.0f},{cy-22:.0f})"><path d="M0 34 C-6 22 -24 12 -24 -2 A24 24 0 1 1 24 -2 C24 12 6 22 0 34 Z" fill="{col}" stroke="#fff" stroke-width="3"/></g><text x="{cx:.0f}" y="{cy-16:.0f}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="{20 if t!="?" else 26}" fill="#fff">{t}</text>'
    # canal + road
    s += f'<path d="M{-10} {H*.62:.0f} C{W*.25:.0f} {H*.5:.0f} {W*.45:.0f} {H*.78:.0f} {W*.7:.0f} {H*.6:.0f} S{W*.95:.0f} {H*.4:.0f} {W+10} {H*.45:.0f}" fill="none" stroke="#5aa7d6" stroke-width="16" stroke-linecap="round"/>'
    s += f'<path d="M{W*.36:.0f} -10 L{W*.38:.0f} {H+10}" stroke="#8d8a7a" stroke-width="14"/><path d="M{W*.36:.0f} -10 L{W*.38:.0f} {H+10}" stroke="#fff" stroke-width="2" stroke-dasharray="14 12"/>'
    for vx, vy, vn in [(W * .04, H * .04, "Village A"), (W * .62, H * .06, "Village B"), (W * .70, H * .84, "Village C")]:
        vx = min(vx, W - 162)
        s += f'<rect x="{vx:.0f}" y="{vy:.0f}" width="150" height="40" rx="10" fill="#fffdf4" stroke="#1f3320" stroke-width="2"/><text x="{vx+75:.0f}" y="{vy+27:.0f}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="#1f3320">{vn}</text>'
    s += f'<text x="{W*.80:.0f}" y="{H*.47:.0f}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#2d6f99">Canal</text>'
    return s + lab + "</svg>"
LG = lambda items: '<div class=lgx>' + "".join(f'<span><i style="{s}"></i>{a}</span>' for a, s in items) + '</div>'
CROPLG = LG([(k, f"background:{v};border:1.5px solid rgba(0,0,0,.15)") for k, v in CROP.items()])
def dr(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f3320;color:#ffc58f"):
    return page(DR + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f3320", cta, ctacss, tagline=f"{n} / 5")

P["p326_drone_s1"] = dr(1, "AGRI DRONE SPRAYING SERVICE", "Spray bookings on calls?<br><span>Which field? Which village?</span>",
f'''<div class=w1><div class="cd c1"><small class=cap>THIS WEEK · 7 BOOKINGS · SAMPLE MAP</small><div class=mapw>{fieldmap(900, 700, "q")}</div></div>
<div class=bb1><span class=vn>{ic("phone",22)} Farmer, 7:10 PM call</span><p>“My field is near the canal, after the second tree. You will find it.”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c1{flex:1;min-height:0;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.bb1{background:#1f3320;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 Inter;color:#ffc58f;margin-bottom:6px}.bb1 p{font:500 24px/1.4 Inter}""")

tot = sum(f[4] for f in FIELDS); tue = sum(f[4] for f in FIELDS if f[5].startswith("Tue"))
P["p326_drone_s2"] = dr(2, "STEP 1 · FARMERS BOOK BY FIELD", "Each booking has<br><span>a pin on the map.</span>",
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>FIELD</span><span>FARMER · SAMPLE</span><span>VILLAGE</span><span>CROP</span><span>ACRES</span><span>DAY</span></div>
{"".join(f'<div class=rw2><b>{a}</b><span>{b}</span><span>{c}</span><span class=cr2><i style="background:{CROP[d]}"></i>{d}</span><strong>{e:g}</strong><span>{g}</span></div>' for a,b,c,d,e,g in FIELDS)}
<div class=tt2><span>7 fields · <b>{tot:g} acres</b></span><span>Tuesday {tue:g} acres · Wednesday {tot-tue:g} acres</span></div></div>
<div class=nb><span class=ib>{ic("pin",26)}</span><span>The farmer drops a location pin once. <b>The pilot opens it in maps.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:14px 24px 18px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:62px 1.2fr 1.1fr 1.1fr 70px 1fr;gap:10px;align-items:center;border-bottom:1px solid #ebe5cf}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #1f3320;font:700 14px/1.4 Inter;letter-spacing:1.5px;color:#7b7a63}
.rw2 b{font:800 22px Poppins;color:#d9661f}.rw2>span{font:600 19px Inter}.rw2 strong{font:800 24px Poppins;text-align:right;padding-right:10px}
.cr2{display:flex;align-items:center;gap:8px}.cr2 i{width:18px;height:18px;border-radius:5px;border:1.5px solid rgba(0,0,0,.15);flex:none}
.tt2{display:flex;justify-content:space-between;background:#e9f1dc;border-radius:14px;padding:14px 18px;margin-top:12px;font:600 19px/1.4 Inter}.tt2 b{color:#3f7a2e}""")

# lawnmower path over F3 (3 acres): 10 passes, 6 done
def flight(W, H, passes=10, donep=6):
    m = 40; gap = (W - 2 * m) / (passes - 1)
    pts = []
    for i in range(passes):
        x = m + i * gap
        pts += [(x, m), (x, H - m)] if i % 2 == 0 else [(x, H - m), (x, m)]
    cut = donep * 2
    dpath = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts[:cut])
    rpath = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in pts[cut - 1:])
    sw = "".join(f'<rect x="{m+i*gap-gap/2:.0f}" y="{m-10}" width="{gap:.0f}" height="{H-2*m+20:.0f}" fill="#3f7a2e" fill-opacity=".22"/>' for i in range(donep))
    furrows = "".join(f'<line x1="{14+k*16}" y1="10" x2="{14+k*16}" y2="{H-10}" stroke="#000" stroke-opacity=".05" stroke-width="3"/>' for k in range(int(W // 16)))
    dx, dy = pts[cut - 1]
    drone = f'''<g transform="translate({dx:.0f},{dy+60:.0f})"><line x1="-34" y1="-34" x2="34" y2="34" stroke="#1f3320" stroke-width="7"/><line x1="34" y1="-34" x2="-34" y2="34" stroke="#1f3320" stroke-width="7"/>
{"".join(f'<circle cx="{a}" cy="{b}" r="17" fill="#fff" fill-opacity=".85" stroke="#1f3320" stroke-width="4"/>' for a,b in [(-34,-34),(34,-34),(-34,34),(34,34)])}<rect x="-16" y="-16" width="32" height="32" rx="8" fill="#f08a3c" stroke="#1f3320" stroke-width="4"/></g>'''
    return f'''<svg viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid meet"><rect width="{W}" height="{H}" rx="16" fill="{CROP["Wheat"]}"/>{furrows}{sw}
<path d="{dpath}" fill="none" stroke="#2f7a3a" stroke-width="8" stroke-linejoin="round"/><path d="{rpath}" fill="none" stroke="#1f3320" stroke-width="4" stroke-dasharray="10 12"/>{drone}</svg>'''
route = [("7:00 AM", "F1", "Village A", 2.5, "done"), ("8:10 AM", "F2", "Village A", 1.5, "done"), ("9:00 AM", "F3", "Village A", 3.0, "now"), ("11:30 AM", "F4", "Village B", 2.0, "next")]
P["p326_drone_s3"] = dr(3, "STEP 2 · DAY PLAN AND LIVE PROGRESS", "Village by village.<br><span>Field by field.</span>",
f'''<div class=w3><div class="cd fl3"><small class=cap>FIELD F3 · FARMER 3 · WHEAT · 3 ACRES</small><div class=mapw>{flight(420, 700)}</div>
<div class=pr3><span><b>6</b> of 10 rows sprayed</span><span class=bar3><i style="width:60%"></i></span></div></div>
<div class=rt3><small class=cap>TUESDAY 24 NOV · PILOT 1</small>{"".join(f'<div class="st3 {k}"><span class=tm3>{t}</span><div><b>{f} · {v}</b><span>{a:g} acres</span></div><em>{ {"done":"Done","now":"Spraying","next":"Next"}[k] }</em></div>' for t,f,v,a,k in route)}
<div class=sm3>Done today <b>{sum(r[3] for r in route if r[4]=="done"):g} acres</b> · left <b>{sum(r[3] for r in route if r[4]!="done"):g} acres</b></div></div></div>''',
css=""".w3{flex:1;display:grid;grid-template-columns:450px 1fr;gap:14px;min-height:0}.fl3{padding:16px 16px 18px;display:flex;flex-direction:column;gap:10px;min-height:0}
.pr3{display:flex;align-items:center;gap:12px;font:600 18px/1.4 Inter}.pr3 b{font:800 24px Poppins;color:#2f7a3a}.bar3{flex:1;height:14px;border-radius:7px;background:#e6e0c8;overflow:hidden}.bar3 i{display:block;height:100%;background:#2f7a3a}
.rt3{display:flex;flex-direction:column;gap:10px;min-height:0}.rt3>.cap{margin:4px 0 0 4px}
.st3{flex:1;display:grid;grid-template-columns:1fr;gap:4px;align-content:center;background:#fffdf4;border-radius:20px;padding:12px 18px;box-shadow:0 10px 22px rgba(31,51,32,.07);border-left:8px solid #c9c19c}
.st3 .tm3{font:800 18px/1.3 Poppins;color:#7b7a63}.st3 b{display:block;font:700 22px/1.35 Inter}.st3 div span{font:500 17px/1.4 Inter;color:#5d6656}
.st3 em{font:700 15px/1.3 Inter;font-style:normal;justify-self:start;border-radius:8px;padding:4px 10px;background:#ece6cf;color:#5d6656}
.st3.done{border-left-color:#2f7a3a}.st3.done em{background:#2f7a3a;color:#fff}.st3.now{border-left-color:#f08a3c;background:#fff4e8}.st3.now em{background:#f08a3c;color:#1f3320}
.sm3{background:#1f3320;color:#fff;border-radius:18px;padding:14px 18px;font:500 19px/1.4 Inter}.sm3 b{color:#ffc58f}""")

msgs = [("Mon 23 Nov · 6 PM · sent", "Tomorrow 9 AM, field F3, 3 acres. Please keep water ready at the field. Reply 1 to confirm.", "1", "Farmer 3"),
        ("Tue 24 Nov · 10:40 AM · after spray", "Field F3 done at 10:35 AM. 3 acres. Your bill and UPI payment link are below.", "", "")]
pays = [("F1", "Farmer 1", "2.5 acres", "Paid"), ("F2", "Farmer 2", "1.5 acres", "Paid"), ("F3", "Farmer 3", "3 acres", "Link sent"), ("F4", "Farmer 4", "2 acres", "After spray")]
P["p326_drone_s4"] = dr(4, "STEP 3 · MESSAGES AND PAYMENTS", "Farmers get a message.<br><span>You get paid on time.</span>",
f'''<div class=w4><div class="cd ms4"><small class=cap>MESSAGES TO FARMER 3 · SAMPLE</small>
<div class=b4><small>{msgs[0][0]}</small><p>{msgs[0][1]}</p></div><div class="b4 r4"><small>Farmer 3 · 6:12 PM</small><p>1</p></div>
<div class=b4><small>{msgs[1][0]}</small><p>{msgs[1][1]}</p><span class=up4>{ic("rupee",20)} Pay by UPI</span></div><div class="b4 r4"><small>Farmer 3 · 10:52 AM</small><p>Paid. Thank you, see you next season.</p></div></div>
<div class="cd py4"><small class=cap>TODAY'S PAYMENTS</small>{"".join(f'<div class=pr4><b>{a}</b><span>{b}<br><em>{c}</em></span><i class="{ {"Paid":"g","Link sent":"o"}.get(d,"n") }">{d}</i></div>' for a,b,c,d in pays)}</div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:14px;min-height:0}.ms4{padding:18px 20px;display:flex;flex-direction:column;gap:14px;background:#e8ecd9}
.b4{background:#fff;border-radius:6px 22px 22px 22px;padding:14px 18px;max-width:92%;box-shadow:0 6px 14px rgba(31,51,32,.06)}.b4 small{display:block;font:700 14px/1.4 Inter;color:#7b7a63;margin-bottom:6px}.b4 p{font:500 22px/1.42 Inter}
.r4{align-self:flex-end;background:#d4ecc3;border-radius:22px 6px 22px 22px}.up4{display:inline-flex;align-items:center;gap:8px;margin-top:12px;background:#3f7a2e;color:#fff;border-radius:12px;padding:8px 14px;font:700 17px/1.3 Inter}
.py4{padding:18px 20px;display:flex;flex-direction:column;gap:8px}.pr4{flex:1;display:grid;grid-template-columns:50px 1fr auto;gap:10px;align-items:center;border-bottom:1px solid #ebe5cf}.pr4:last-child{border:0}
.pr4 b{font:800 20px Poppins;color:#d9661f}.pr4 span{font:600 22px/1.4 Inter}.pr4 em{font-style:normal;font-weight:500;color:#5d6656;font-size:18px}
.pr4 i{font:700 15px/1.3 Inter;font-style:normal;border-radius:8px;padding:5px 10px;background:#ece6cf;color:#5d6656}.pr4 i.g{background:#2f7a3a;color:#fff}.pr4 i.o{background:#f08a3c;color:#1f3320}""")

P["p326_drone_s5"] = dr(5, "YOUR TURN", "Run drone spraying?<br><span>Let's build your booking app.</span>",
f'''<div class=w5><div class="cd c5"><div class=mapw>{fieldmap(480, 700, "done", done={"F1","F2","F3"})}</div></div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,32)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("pin","Field pins","Booked with location"),("map","Day plan","Village by village"),("chart","Live progress","Rows and acres done"),("rupee","UPI payments","Link after each field")])}</div>
<div class=q>How do farmers book your drone today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#d9661f;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1.1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{padding:14px;display:flex;min-height:0}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fffdf4;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(31,51,32,.07)}
.ti .ib{width:60px;height:60px;border-radius:18px;background:#fde3cc;color:#d9661f}.ti b{display:block;font:700 22px/1.45 Poppins;margin-bottom:3px}.ti div span{font:500 17px/1.4 Inter;color:#5d6656}
.q{background:#1f3320;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 Inter}""")

# appended into b062.py (posts 327-330)

# ───────── 327 INDIA · Saw mill and timber depot · SINGLE · Bitter + Roboto · sawdust tan / teak brown / blade blue
# New technique: isometric SVG plank stacks (front face = plank ends with end-grain rings, top + side faces),
# stack height drawn from the piece count, with the order table reading stock from the same data.
def iso_stack(count, tone, cols=4):
    rows = max(2, round(count / 16)); rows = min(rows, 13)
    cw, rh, dx, dy = 36, 22, 46, 26
    w, h = cols * cw, rows * rh
    W, H = 230, 330
    x0, y0 = 16, H - 12
    fr = "".join(f'<rect x="{x0+c*cw+2}" y="{y0-(r+1)*rh+2}" width="{cw-4}" height="{rh-4}" rx="3" fill="{tone}"/><ellipse cx="{x0+c*cw+cw/2:.0f}" cy="{y0-(r+1)*rh+rh/2:.0f}" rx="9" ry="5" fill="none" stroke="#6b3d1f" stroke-opacity=".45" stroke-width="1.6"/><ellipse cx="{x0+c*cw+cw/2:.0f}" cy="{y0-(r+1)*rh+rh/2:.0f}" rx="3.5" ry="2" fill="#6b3d1f" fill-opacity=".5"/>' for r in range(rows) for c in range(cols))
    top = f'<polygon points="{x0},{y0-h} {x0+w},{y0-h} {x0+w+dx},{y0-h-dy} {x0+dx},{y0-h-dy}" fill="#f3d9a8" stroke="#8a5a32" stroke-width="2"/>'
    top += "".join(f'<line x1="{x0+c*cw}" y1="{y0-h}" x2="{x0+c*cw+dx}" y2="{y0-h-dy}" stroke="#8a5a32" stroke-opacity=".5" stroke-width="1.5"/>' for c in range(1, cols))
    side = f'<polygon points="{x0+w},{y0} {x0+w+dx},{y0-dy} {x0+w+dx},{y0-h-dy} {x0+w},{y0-h}" fill="#a86a3a" stroke="#6b3d1f" stroke-width="2"/>'
    side += "".join(f'<line x1="{x0+w}" y1="{y0-r*rh}" x2="{x0+w+dx}" y2="{y0-r*rh-dy}" stroke="#6b3d1f" stroke-opacity=".5" stroke-width="1.5"/>' for r in range(1, rows))
    back = f'<rect x="{x0-4}" y="{y0-h-4}" width="{w+8}" height="{h+8}" rx="4" fill="#8a5a32"/>'
    shadow = f'<ellipse cx="{x0+w/2+dx/2:.0f}" cy="{y0+2}" rx="{w/2+dx/2+8:.0f}" ry="9" fill="#000" fill-opacity=".10"/>'
    return f'<svg viewBox="0 0 {W} {H}" class=st7>{shadow}{side}{back}{fr}{top}</svg>'
STK = [("A", "2 x 4 in", "10 ft", 120, "#e7c08a"), ("B", "3 x 3 in", "8 ft", 64, "#e2b67c"), ("C", "1 x 6 in", "12 ft", 210, "#ecc893"), ("D", "4 x 4 in", "10 ft", 18, "#d9a86e")]
SK = {f"{a} {b}": n for _, a, b, n, _ in STK}
ORD = [("O-41", "Carpenter 1", "2 x 4 in", "10 ft", 40), ("O-42", "Carpenter 2", "4 x 4 in", "10 ft", 30), ("O-43", "Furniture shop", "1 x 6 in", "12 ft", 80), ("O-44", "Carpenter 3", "3 x 3 in", "8 ft", 24)]
def ost(sz, ln, q):
    have = SK[f"{sz} {ln}"]
    return ("ok7", "Ready to load") if have >= q else ("sh7", f"Short by {q-have}")
short = [o for o in ORD if SK[f"{o[2]} {o[3]}"] < o[4]][0]
P["p327_timber"] = page("""
body{--f:'Roboto';--h:'Bitter';background:#f4ead8;color:#3b2414}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#2b6cb0;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;line-height:1.22;letter-spacing:-1px} h1 span{color:#a0522d}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.dp{flex:1.15;min-height:0;background:#fffaf0;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(59,36,20,.08)}
.cp7{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#8a7360}
.sr7{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;background:linear-gradient(#fffaf0 82%,#efe2c8 82%);border-radius:14px}
.cl7{display:flex;flex-direction:column;align-items:center;min-height:0}.st7{flex:1;min-height:0;width:100%;display:block}
.cl7 b{font:800 22px/1.35 Bitter}.cl7 span{font:500 16px/1.4 Roboto;color:#6d5a4a}.cl7 em{font:800 30px/1.3 Bitter;font-style:normal;color:#2b6cb0}.cl7 em.lw{color:#c0392b}
.od{background:#fffaf0;border-radius:26px;padding:14px 22px;box-shadow:0 14px 30px rgba(59,36,20,.08)}
.or7{display:grid;grid-template-columns:70px 1.3fr 1.5fr 70px 1.2fr;gap:10px;align-items:center;padding:11px 0;border-bottom:1px solid #eee0c8;font:500 19px/1.35 Roboto}.or7:last-child{border:0}
.or7.hd{font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#8a7360;border-bottom:2px solid #3b2414;padding-top:4px}
.or7 b{font:800 19px Bitter;color:#a0522d}.or7 strong{font:800 22px Bitter;text-align:right;padding-right:8px}
.or7 i{font:700 15px/1.3 Roboto;font-style:normal;border-radius:8px;padding:6px 10px;justify-self:start}.ok7{background:#dcebdc;color:#2c6b3a}.sh7{background:#c0392b;color:#fff}
.nt7{display:flex;align-items:center;gap:14px;background:#2b6cb0;color:#fff;border-radius:20px;padding:14px 20px;font:500 20px/1.4 Roboto}.nt7 b{color:#ffe3a3}.nt7 .ib{width:48px;height:48px;border-radius:14px;background:#fffaf0;color:#2b6cb0}
""", "<div class=kk>SAW MILL AND TIMBER DEPOT</div><h1>Which plank sizes are left?<br><span>See every stack.</span></h1>",
f'''<div class=vw><div class=dp><small class=cp7>DEPOT STOCK · STACKS A TO D · SAMPLE</small><div class=sr7>{"".join(f'<div class=cl7>{iso_stack(n,t)}<b>{a}</b><span>{b} · stack {k}</span><em class="{"lw" if n<30 else ""}">{n} pcs</em></div>' for k,a,b,n,t in STK)}</div></div>
<div class=od><div class="or7 hd"><span>ORDER</span><span>FOR · SAMPLE</span><span>SIZE</span><span>PCS</span><span>STATUS</span></div>
{"".join(f'<div class=or7><b>{o}</b><span>{w}</span><span>{sz} · {ln}</span><strong>{q}</strong><i class="{ost(sz,ln,q)[0]}">{ost(sz,ln,q)[1]}</i></div>' for o,w,sz,ln,q in ORD)}</div>
<div class=nt7><span class=ib>{ic("bell",26)}</span><span>{short[2]} is short for {short[0]}. <b>Log L-07 is set for cutting tomorrow at 7 AM.</b></span></div></div>''',
"#3b2414", "Run a timber depot? DM us", "background:#3b2414;color:#ffe3a3")

# ───────── 328 USA · Self storage facility · SINGLE · Anton + Open Sans · storage orange / concrete / ink navy
# New technique: CSS roll-up doors (corrugated slats via repeating gradients, handle, unit plate) in a building
# elevation, with the online size picker counting free units from the same door list.
DOORS = [[("101", "5x5", "free"), ("102", "5x5", "rent"), ("103", "5x10", "rent"), ("104", "5x10", "free"), ("105", "10x10", "rent"), ("106", "10x10", "free")],
         [("201", "10x10", "rent"), ("202", "10x10", "res"), ("203", "10x20", "free"), ("204", "10x20", "rent"), ("205", "5x10", "rent"), ("206", "5x5", "free")]]
GROW = {"5x5": 1, "5x10": 1, "10x10": 1.35, "10x20": 1.35}
STL = {"free": ("Free", "fr8"), "rent": ("Rented", "rn8"), "res": ("Reserved", "rs8")}
free = {z: sum(1 for row in DOORS for _, s_, st in row if s_ == z and st == "free") for z in GROW}
def door(u, z, st):
    lab, cl = STL[st]
    return f'<div class=dr8 style="flex:{GROW[z]}"><span class=pl8>{u}</span><div class="sl8 {cl}"><i></i></div><em class={cl}>{lab} · {z.replace("x"," x ")}</em></div>'
P["p328_storage"] = page("""
body{--f:'Open Sans';--h:'Anton';background:#e6e6e1;color:#1c2541}
.kk{font:700 16px/1.5 'Open Sans';letter-spacing:3px;color:#d9731a;margin-top:22px;margin-bottom:4px}
h1{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.2;letter-spacing:0;margin-top:8px} h1 span{color:#e0791c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bd8{background:#c9cac4;border-radius:22px;padding:14px 18px 16px;display:flex;flex-direction:column;gap:12px;box-shadow:inset 0 -10px 0 #b3b4ae}
.bd8>small{font:700 13px/1.5 'Open Sans';letter-spacing:2px;color:#4d5468}
.rw8{display:flex;gap:10px}
.dr8{display:flex;flex-direction:column;align-items:stretch;gap:6px;min-width:0}
.pl8{align-self:center;background:#1c2541;color:#fff;font:700 15px/1.4 'Open Sans';border-radius:6px;padding:2px 10px}
.sl8{height:128px;border-radius:6px 6px 2px 2px;position:relative;background:repeating-linear-gradient(180deg,#f28c28 0 10px,#d9731a 10px 12px,#f7a24a 12px 14px);box-shadow:inset 0 0 0 3px rgba(0,0,0,.12)}
.sl8 i{position:absolute;left:50%;bottom:12px;width:40px;height:8px;margin-left:-20px;border-radius:4px;background:#1c2541}
.sl8.rn8{filter:saturate(.35) brightness(.92)}.sl8.rs8{filter:saturate(.7)}
.dr8 em{font:700 13px/1.35 'Open Sans';font-style:normal;text-align:center;border-radius:6px;padding:4px 2px;white-space:nowrap}
em.fr8{background:#2f9e6b;color:#fff}em.rn8{background:#1c2541;color:#fff}em.rs8{background:#ffe08a;color:#1c2541}
.bw8{flex:1;min-height:0}
.pgx{flex:1;padding:16px 22px 18px;display:flex;flex-direction:column;gap:12px;min-height:0}
.pgx>b{font:400 30px/1.5 Anton;letter-spacing:.3px}.pgx>p{font:500 18px/1.4 'Open Sans';color:#4d5468;margin-top:-8px}
.sz8{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.sz8 div{border:2px solid #d4d6de;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}.sz8 div.on{border-color:#e0791c;background:#fff4e9}
.sz8 b{font:400 30px/1.5 Anton}.sz8 span{font:500 15px/1.4 'Open Sans';color:#4d5468}.sz8 em{font:700 16px/1.4 'Open Sans';font-style:normal;color:#2f9e6b}
.fx8{display:grid;grid-template-columns:1fr 1fr;gap:10px}.fx8 div{background:#f3f4f7;border-radius:12px;padding:10px 14px}.fx8 small{display:block;font:700 12px/1.4 'Open Sans';letter-spacing:1.5px;color:#6b7285}.fx8 span{font:600 18px/1.4 'Open Sans'}
.bt8{margin-top:auto;display:flex;justify-content:space-between;align-items:center;gap:14px}.bt8 span{font:500 16px/1.4 'Open Sans';color:#4d5468}.bt8 b{background:#e0791c;color:#fff;border-radius:12px;padding:12px 22px;font:700 18px/1.3 'Open Sans';white-space:nowrap}
""", "<div class=kk>SELF STORAGE FACILITY</div><h1>Units on a whiteboard?<br><span>Let renters see every free door.</span></h1>",
f'''<div class=vw><div class=bd8><small>BUILDING A · 12 UNITS · SAMPLE</small>{"".join('<div class=rw8>' + "".join(door(*d) for d in row) + '</div>' for row in DOORS)}</div>
<div class=bw8 style="display:flex">{browser(f"""<div class=pgx><b>Reserve a unit online</b><p>Free units right now, from the same door list.</p>
<div class=sz8>{"".join(f'<div class="{"on" if z=="10x10" else ""}"><b>{z.replace("x"," x ")}</b><span>{d}</span><em>{free[z]} free</em></div>' for z,d in [("5x5","Boxes, a bike"),("5x10","A small room"),("10x10","A 1-bed home"),("10x20","A 3-bed home")])}</div>
<div class=fx8><div><small>UNIT</small><span>106 · 10 x 10 · ground floor</span></div><div><small>MOVE-IN DATE</small><span>Tue, Dec 1</span></div></div>
<div class=bt8><span>Your gate code comes by text after you sign online.</span><b>Reserve unit 106</b></div></div>""", "yourstorage.com/units", "flex:1")}</div></div>''',
"#1c2541", "Own a storage facility? DM us", "background:#1c2541;color:#f7a24a")

# ───────── 329 INDIA · Shoe cleaning and care service · SINGLE · Montserrat + DM Sans · chalk white / foam blue / gum brown · PHONE
# New technique: SVG side-profile sneakers on a drying rack, each with a hanging string tag that carries the pair
# number and stage, matched to the customer's phone tracker.
def shoe(up, acc, x=0):
    return f'''<svg viewBox="0 0 220 110" class=sh9><path d="M14 74 C14 52 30 40 52 36 L84 20 C96 14 108 16 116 26 L132 44 C150 50 180 54 196 62 C206 67 208 76 206 82 L14 82 Z" fill="{up}" stroke="#2c3440" stroke-width="3" stroke-linejoin="round"/>
<path d="M88 26 L100 50 M100 22 L112 46 M110 24 L122 44" stroke="{acc}" stroke-width="4" stroke-linecap="round"/><path d="M30 60 C60 56 90 64 120 62 S170 66 196 70" fill="none" stroke="{acc}" stroke-width="5" stroke-linecap="round"/>
<rect x="10" y="80" width="200" height="16" rx="8" fill="#c58a52" stroke="#2c3440" stroke-width="3"/></svg>'''
PAIRS = [("P-118", "#ffffff", "#3d7bd9", "Washing", "wa9"), ("P-119", "#f3f1ea", "#b0703a", "Drying", "dr9"), ("P-120", "#2c3440", "#f7f7f2", "Ready", "rd9"),
         ("P-121", "#e9f1ff", "#3d7bd9", "Drying", "dr9"), ("P-122", "#ffffff", "#e0584f", "Ready", "rd9"), ("P-123", "#fff6e0", "#2c3440", "Washing", "wa9")]
steps = [("Picked up", "Wed 25 Nov, 10:40 AM", "dn"), ("Washing", "Wed 25 Nov", "dn"), ("Drying", "Now · 1 day", "nw"), ("Ready", "Fri 27 Nov", ""), ("Delivered", "Sat 28 Nov, 10 AM to 12 PM", "")]
ph9 = phone(f'''<div class=ap9><div class=ah9><small>SAMPLE SHOE CARE</small><b>Your pair P-119</b><span>Deep clean · 1 pair</span></div>
<div class=sv9>{shoe("#f3f1ea", "#b0703a")}</div>
<div class=tk9>{"".join(f'<div class="s9 {k}"><i>{ic("check",14,w=3) if k=="dn" else ""}</i><div><b>{a}</b><span>{b}</span></div></div>' for a,b,k in steps)}</div>
<div class=bk9>Change delivery time</div></div>''', 350, 830)
P["p329_shoes"] = page("""
body{--f:'DM Sans';--h:'Montserrat';background:#f2f3ee;color:#2c3440}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b0703a;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#3d7bd9}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.rk9{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(44,52,64,.08)}
.rk9>small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7a828e}
.gr9{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:0 12px}
.cl9{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;border-bottom:8px solid #c9ccd2;padding:4px 4px 8px;position:relative}
.tg9{display:flex;flex-direction:column;align-items:center;margin-bottom:6px}.tg9 i{width:2px;height:16px;background:#7a828e}
.tg9 span{border-radius:8px 8px 8px 8px;padding:6px 12px;font:700 18px/1.35 'DM Sans';background:#f7f3e8;border:2px dashed #b0703a;white-space:nowrap}
.tg9 span em{font-style:normal;font-weight:700;margin-left:6px}.wa9{color:#3d7bd9}.dr9{color:#b0703a}.rd9{color:#2f8a5b}
.sh9{width:236px;height:118px;display:block}
.nt9{background:#2c3440;color:#fff;border-radius:16px;padding:12px 16px;font:500 18px/1.45 'DM Sans'}.nt9 b{color:#9cc2ff}
.ap9{display:flex;flex-direction:column;gap:10px;padding:8px 18px 18px;flex:1;min-height:0}
.ah9 small{display:block;font:700 11px/1.4 'DM Sans';letter-spacing:2px;color:#7a828e}.ah9 b{display:block;font:800 22px/1.3 Montserrat}.ah9 span{font:500 14px/1.4 'DM Sans';color:#5b6470}
.sv9{background:#eef3fb;border-radius:16px;padding:10px;display:flex;justify-content:center}.sv9 .sh9{width:220px;height:110px}
.tk9{display:flex;flex-direction:column;flex:1;justify-content:space-between;padding:4px 2px}
.s9{display:flex;gap:12px;align-items:flex-start;position:relative}.s9 i{width:26px;height:26px;border-radius:50%;border:3px solid #c9ccd2;background:#fff;flex:none;display:flex;align-items:center;justify-content:center;color:#fff;margin-top:2px}
.s9.dn i{background:#2f8a5b;border-color:#2f8a5b}.s9.nw i{border-color:#3d7bd9;box-shadow:0 0 0 5px #dbe7fb}
.s9 b{display:block;font:700 16px/1.35 'DM Sans'}.s9 span{font:500 13px/1.4 'DM Sans';color:#6b7380}.s9.nw b{color:#3d7bd9}
.bk9{background:#3d7bd9;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 16px 'DM Sans'}
""", "<div class=kk>SHOE CLEANING AND CARE</div><h1>Whose pair is this?<br><span>Tag it. Track it.</span></h1>",
f'''<div class=vw><div class=rk9><small>DRYING RACK · WEDNESDAY · SAMPLE</small><div class=gr9>{"".join(f'<div class=cl9><div class=tg9><i></i><span>{n}<em class={c}>{st}</em></span></div>{shoe(u,a)}</div>' for n,u,a,st,c in PAIRS)}</div>
<div class=nt9>Every pair gets a tag at pickup. <b>The customer sees the same stage on the phone.</b></div></div>{ph9}</div>''',
"#2c3440", "Clean shoes for a living? DM us", "background:#2c3440;color:#9cc2ff")

# ───────── 330 CANADA · Escape room · CAROUSEL 5 · Crimson Text + Roboto · dark plum / clue amber / lock teal
# New technique: room schedule where every 60-minute game is followed by a hatched 15-minute reset block,
# computed from the same booking list, plus a lined paper booking diary with a double booking circled.
ES = """
body{--f:'Roboto';--h:'Crimson Text';background:#24122b;color:#f6ecdf}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#2bb3a3;margin-top:22px;align-self:flex-start}
h1{font-family:'Crimson Text';font-weight:700;font-size:68px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#f2b134}
.cd{background:#341c3d;border-radius:24px;box-shadow:0 16px 34px rgba(0,0,0,.25)}
.cap{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#bfa9c6}
.nb{display:flex;align-items:center;gap:14px;background:#f2b134;color:#24122b;border-radius:20px;padding:16px 20px;font:500 22px/1.4 Roboto}.nb .ib{width:50px;height:50px;border-radius:14px;background:#24122b;color:#f2b134}
"""
def es(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#f2b134;color:#24122b"):
    return page(ES + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#f6ecdf", cta, ctacss, tagline=f"{n} / 5", logo_color="#f6ecdf")
diary = [("2:00 PM", "Old Library · team of 5", ""), ("3:30 PM", "Night Train · team of 4", ""), ("5:00 PM", "The Lab · team of 3", ""),
         ("7:00 PM", "The Lab · team of 6 (phone)", "x"), ("7:00 PM", "The Lab · team of 4 (walk-in)", "x"), ("8:30 PM", "Old Library · team of 6", "")]
P["p330_escape_s1"] = es(1, "ESCAPE ROOM · BOOKINGS", "Bookings in a diary?<br><span>Two teams, one room.</span>",
f'''<div class=w1><div class=dy1><b>Saturday, December 5</b><small>SAMPLE BOOKING DIARY</small>{"".join(f'<div class="ln1"><span>{t}</span><p>{e}</p></div>' for t,e,k in diary[:3])}<div class=xg1>{"".join(f'<div class="ln1 x"><span>{t}</span><p>{e}</p></div>' for t,e,k in diary[3:5])}<em class=xb1>Same room, same time</em></div>{"".join(f'<div class="ln1"><span>{t}</span><p>{e}</p></div>' for t,e,k in diary[5:])}</div>
<div class=bb1><span class=vn>{ic("users",22)} Front desk, 6:52 PM</span><p>“Both teams are here for The Lab at 7. Who wrote the second one?”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}
.dy1{flex:1;min-height:0;position:relative;background:#fbf5e6;border-radius:10px;padding:22px 36px 20px 120px;color:#2b1d14;box-shadow:0 20px 40px rgba(0,0,0,.35);transform:rotate(-1.2deg);display:flex;flex-direction:column}
.dy1::before{content:"";position:absolute;left:92px;top:0;bottom:0;width:3px;background:#e07a7a}
.dy1>b{font:700 36px/1.35 'Crimson Text';margin-bottom:6px}.dy1>small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#8a7a66;margin-bottom:10px}
.ln1{flex:1;display:flex;align-items:center;gap:18px;position:relative;border-bottom:2px solid #ddd2ba}.ln1 span{position:absolute;left:-104px;width:90px;font:700 17px/1.3 Roboto;color:#6b5a4a}
.ln1 p{font:italic 600 31px/1.3 'Crimson Text';color:#24304f}
.ln1.x p{color:#a02c2c}
.xg1{flex:2.3;display:flex;flex-direction:column;border:4px solid #d23b3b;border-radius:18px;margin:6px -14px 6px -112px;padding:0 14px 0 112px;background:#fde9e4}.xg1 .ln1{border-color:#efc4bb}.xg1 .ln1:last-of-type{border:0}.xb1{align-self:flex-end;font:700 16px/1.4 Roboto;font-style:normal;color:#fff;background:#d23b3b;border-radius:8px;padding:3px 10px;margin:0 0 8px}
.bb1{background:#341c3d;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 Roboto;color:#2bb3a3;margin-bottom:6px}.bb1 p{font:500 24px/1.4 Roboto}""")

ROOMS = ["The Lab", "Old Library", "Night Train"]
slots = ["2:00", "3:30", "5:00", "6:30", "8:00", "9:30"]
taken = {"The Lab": {"2:00", "3:30", "5:00", "6:30"}, "Old Library": {"2:00", "8:00"}, "Night Train": {"3:30"}}
P["p330_escape_s2"] = es(2, "STEP 1 · BOOK ONLINE, ROOM BY ROOM", "A taken time<br><span>cannot be booked again.</span>",
f'''<div class=w2>{browser(f"""<div class=bp2><b>Book a room · Saturday, December 5</b><div class=rm2>{"".join(f'<div class="{"on" if r=="The Lab" else ""}"><i>{ic("shield",26)}</i><span>{r}</span><em>60 min · 2 to 8 players</em></div>' for r in ROOMS)}</div>
<small>TIMES FOR THE LAB · SAMPLE</small><div class=sl2>{"".join(f'<span class="{"tk" if t in taken["The Lab"] else ("pk" if t=="8:00" else "")}">{t} PM{"<br><em>Taken</em>" if t in taken["The Lab"] else ""}</span>' for t in slots)}</div>
<div class=pl2><small>PLAYERS</small><div>{"".join(f'<span class="{"on" if p==6 else ""}">{p}</span>' for p in range(2,9))}</div></div>
<div class=fd2><div><small>TEAM NAME</small><span>Sample Team</span></div><div><small>MOBILE</small><span>(xxx) xxx-xx12</span></div></div>
<div class=ft2><span>The Lab · 8:00 PM · 6 players</span><b>Book now</b></div></div>""", "yourescaperoom.ca/book", "flex:1;color:#24122b")}
<div class=nb><span class=ib>{ic("cal",26)}</span><span>Phone and walk-in bookings go in the same calendar.</span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bp2{flex:1;padding:22px 26px 24px;display:flex;flex-direction:column;gap:22px}.bp2>b{font:700 40px/1.3 'Crimson Text'}.bp2 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#7a6a80}
.rm2{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.rm2 div{border:2px solid #e2d8e6;border-radius:16px;padding:18px 14px;display:flex;flex-direction:column;gap:4px}.rm2 div.on{border-color:#2bb3a3;background:#e8f7f5}
.rm2 i{width:44px;height:44px;border-radius:12px;background:#24122b;color:#f2b134;display:flex;align-items:center;justify-content:center;margin-bottom:4px}.rm2 span{font:700 24px/1.35 Roboto}.rm2 em{font:500 15px/1.4 Roboto;font-style:normal;color:#6b5a70}
.sl2{display:grid;grid-template-columns:repeat(6,1fr);gap:10px}.sl2 span{border:2px solid #e2d8e6;border-radius:12px;padding:20px 0;text-align:center;font:700 20px/1.35 Roboto}
.sl2 span.tk{background:#f1edf2;color:#a99bb0;text-decoration:line-through}.sl2 span.tk em{font:500 13px/1.3 Roboto;font-style:normal;text-decoration:none;display:inline-block}.sl2 span.pk{background:#24122b;color:#f2b134;border-color:#24122b}
.pl2{display:flex;flex-direction:column;gap:8px}.pl2 div{display:flex;gap:10px}.pl2 span{width:62px;height:62px;border-radius:50%;border:2px solid #e2d8e6;display:flex;align-items:center;justify-content:center;font:700 20px Roboto}.pl2 span.on{background:#2bb3a3;border-color:#2bb3a3;color:#fff}
.fd2{display:grid;grid-template-columns:1fr 1fr;gap:12px}.fd2 div{background:#f6f1f7;border-radius:12px;padding:10px 14px}.fd2 span{display:block;font:600 21px/1.4 Roboto}.fd2 div{padding:14px 16px!important}.ft2{margin-top:auto;display:flex;justify-content:space-between;align-items:center;background:#f6f1f7;border-radius:14px;padding:12px 12px 12px 18px;font:600 19px/1.4 Roboto}.ft2 b{background:#f2b134;color:#24122b;border-radius:12px;padding:12px 24px;font:700 18px/1.3 Roboto}""")

# day schedule 1 PM to 11 PM, game 60 min + reset 15 min
H0, H1 = 13, 23
games = {"The Lab": [(14, 5), (15.5, 3), (17, 3), (18.5, 6), (20, 6)], "Old Library": [(14, 5), (15.5, 4), (20, 6), (21.5, 2)], "Night Train": [(15.5, 4), (17, 2), (18.5, 5), (20, 4)]}
pct = lambda t: (t - H0) / (H1 - H0) * 100
def blocks(r):
    out = ""
    for t, n in games[r]:
        out += f'<div class=gm3 style="left:{pct(t):.2f}%;width:{pct(t+1)-pct(t):.2f}%"><b>{n}</b></div><div class=rs3 style="left:{pct(t+1):.2f}%;width:{pct(t+1.25)-pct(t+1):.2f}%"></div>'
    return out
ng = sum(len(v) for v in games.values()); npl = sum(n for v in games.values() for _, n in v)
hl = lambda h: f"{h-12 if h>12 else h} PM" if h >= 12 else f"{h} AM"
P["p330_escape_s3"] = es(3, "STEP 2 · ONE SCHEDULE FOR ALL ROOMS", "Every game gets<br><span>15 minutes to reset.</span>",
f'''<div class=w3><div class="cd sc3"><small class=cap>SATURDAY, DECEMBER 5 · SAMPLE</small><div class=hh3><span></span><div>{"".join(f'<em style="left:{pct(h):.2f}%">{hl(h)}</em>' for h in range(14, 23, 2))}</div></div>
{"".join(f'<div class=rr3><b>{r}</b><div class=tr3>{blocks(r)}</div></div>' for r in ROOMS)}
<div class=lg3><span><i class=g3></i>Game, 60 min · number = players</span><span><i class=r3></i>Reset, 15 min</span></div></div>
<div class=tl3>{"".join(f'<div><b>{v}</b><span>{a}</span></div>' for v,a in [(ng,"games today"),(npl,"players"),(ng,"resets, never skipped")])}</div>
<div class=nb><span class=ib>{ic("clock",26)}</span><span>Staff see which room to reset next, and when.</span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sc3{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:10px;min-height:0}
.hh3{display:grid;grid-template-columns:150px 1fr;gap:12px;height:26px}.hh3 div{position:relative}.hh3 em{position:absolute;transform:translateX(-50%);font:700 15px/1.4 Roboto;font-style:normal;color:#bfa9c6;white-space:nowrap}
.rr3{flex:1;display:grid;grid-template-columns:150px 1fr;gap:12px;align-items:center}.rr3>b{font:700 26px/1.3 'Crimson Text'}
.tr3{position:relative;height:100%;min-height:80px;border-radius:12px;background:repeating-linear-gradient(90deg,#3f2549 0 calc(10% - 2px),#4a2d55 calc(10% - 2px) 10%)}
.gm3{position:absolute;top:10px;bottom:10px;background:#2bb3a3;border-radius:8px;display:flex;align-items:center;justify-content:center}.gm3 b{font:800 22px Roboto;color:#14262a}
.rs3{position:absolute;top:10px;bottom:10px;border-radius:4px;background:repeating-linear-gradient(45deg,#f2b134 0 4px,transparent 4px 9px);box-shadow:inset 0 0 0 2px #f2b134}
.lg3{display:flex;gap:26px;font:600 17px/1.4 Roboto;color:#e6d8ea}.lg3 span{display:flex;align-items:center;gap:10px}.lg3 i{width:30px;height:20px;border-radius:5px}.g3{background:#2bb3a3}.r3{background:repeating-linear-gradient(45deg,#f2b134 0 4px,transparent 4px 9px);box-shadow:inset 0 0 0 2px #f2b134}
.tl3{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.tl3 div{background:#341c3d;border-radius:18px;padding:14px 18px;display:flex;align-items:center;gap:14px}.tl3 b{font:700 46px/1.2 'Crimson Text';color:#f2b134}.tl3 span{font:500 17px/1.35 Roboto;color:#e6d8ea}""")

ms4 = [("Booked · Mon, Nov 23", "You're booked: The Lab, Saturday, December 5 at 8:00 PM, 6 players. Reply C to change the time.", ""),
       ("Day before · Fri, Dec 4, 10 AM", "See you tomorrow at 8:00 PM! Please arrive 15 minutes early. Free parking is behind the building.", ""),
       ("Team · Fri, Dec 4, 10:14 AM", "Thanks! Can we make it 7 players?", "r"),
       ("Front desk · Fri, Dec 4, 10:20 AM", "Yes, The Lab takes up to 8 players. Your booking now says 7.", ""),
       ("After the game · Sat, Dec 5, 9:15 PM", "Thanks for playing The Lab! Want to try Night Train next time? Tap to book.", "")]
P["p330_escape_s4"] = es(4, "STEP 3 · MESSAGES DO THE FOLLOW-UP", "Fewer calls.<br><span>Teams arrive on time.</span>",
f'''<div class=w4><div class="cd ch4"><small class=cap>MESSAGES WITH TEAM · SAMPLE</small>{"".join(f'<div class="b4 {k}"><small>{a}</small><p>{b}</p></div>' for a,b,k in ms4)}</div>
<div class=sd4>{"".join(f'<div class=tc4><span class=ib>{ic(i,28)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("send","Booking text","Sent the moment they book"),("bell","Day before","Arrive 15 minutes early"),("users","Player count","Changed by reply, up to 8")])}</div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:1.35fr 1fr;gap:14px;min-height:0}.ch4{padding:18px 20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}.ch4 .b4 p{font-size:21px!important}
.b4{background:#4a2d55;border-radius:6px 22px 22px 22px;padding:14px 18px;max-width:94%}.b4 small{display:block;font:700 14px/1.4 Roboto;color:#2bb3a3;margin-bottom:6px}.b4 p{font:500 21px/1.42 Roboto}
.ch4 .b4 p{font-size:24px}.b4.r{align-self:flex-end;background:#f2b134;color:#24122b;border-radius:22px 6px 22px 22px}.b4.r small{color:#5a3a10}
.sd4{display:flex;flex-direction:column;gap:12px}.tc4{flex:1;background:#341c3d;border-radius:22px;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:12px}
.tc4 .ib{width:56px;height:56px;border-radius:16px;background:#2bb3a3;color:#14262a}.tc4 b{display:block;font:700 30px/1.3 'Crimson Text';color:#f2b134}.tc4 div span{font:500 18px/1.4 Roboto;color:#e6d8ea}""")

def edoor(name, col):
    return f'''<div class=dd5><div class=fr5 style="background:{col}"><i class=kn5></i><span class=pk5>{ic("shield",30)}</span></div><b>{name}</b></div>'''
P["p330_escape_s5"] = es(5, "YOUR TURN", "Run an escape room?<br><span>Let's build your booking site.</span>",
f'''<div class=w5><div class="cd dr5">{edoor("The Lab","#2bb3a3")}{edoor("Old Library","#b86b3c")}{edoor("Night Train","#5a6fc0")}</div>
<div class=gd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("cal","Online booking","Room, time and players"),("clock","Reset blocks","15 minutes after every game"),("send","Auto messages","Booked, day before, changes"),("users","Front desk view","Phone and walk-ins in one place")])}</div>
<div class=q>How do teams book your rooms today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#2bb3a3;color:#14262a",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.dr5{flex:1;min-height:0;display:flex;justify-content:space-around;align-items:flex-end;padding:24px 30px 20px;background:#341c3d linear-gradient(#341c3d 84%,#2a1631 84%)}
.dd5{display:flex;flex-direction:column;align-items:center;gap:12px;height:100%}.dd5 b{font:700 28px/1.3 'Crimson Text';color:#f6ecdf}
.fr5{flex:1;width:190px;border-radius:95px 95px 6px 6px;position:relative;box-shadow:inset 0 0 0 10px rgba(0,0,0,.18),0 0 0 6px #1c0e22}
.kn5{position:absolute;right:22px;top:55%;width:16px;height:16px;border-radius:50%;background:#f2b134}
.pk5{position:absolute;left:50%;top:40%;transform:translate(-50%,-50%);width:66px;height:66px;border-radius:18px;background:#24122b;color:#f2b134;display:flex;align-items:center;justify-content:center}
.gd5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#341c3d;border-radius:20px;padding:16px 18px}
.ti .ib{width:56px;height:56px;border-radius:16px;background:#f2b134;color:#24122b}.ti b{display:block;font:700 26px/1.3 'Crimson Text'}.ti div span{font:500 16px/1.4 Roboto;color:#e6d8ea}
.q{background:#f2b134;color:#24122b;border-radius:22px;padding:20px 24px;font:600 23px/1.4 Roboto}""")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
