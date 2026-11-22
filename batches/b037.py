import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

def arc(cx, cy, r, h1, h2):
    a1 = math.radians(h1 / 12 * 360 - 90); a2 = math.radians(h2 / 12 * 360 - 90)
    x1, y1 = cx + r * math.cos(a1), cy + r * math.sin(a1); x2, y2 = cx + r * math.cos(a2), cy + r * math.sin(a2)
    return f"M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}"
def pt(cx, cy, r, h):
    a = math.radians(h / 12 * 360 - 90); return cx + r * math.cos(a), cy + r * math.sin(a)

# ───────── 201 INDIA · Ice factory · SINGLE · Anton + DM Sans · deep indigo / frost white / sunrise yellow
# New technique: radial 12-hour clock dial used as a delivery round (coloured arcs per slot, numbered pins, "now" hand).
slots = [(4.5, 5.25, "Sample Fish Market", "4:30 AM", 40, "Delivered", "d"), (5.5, 6.0, "Sample Hotel", "5:30 AM", 20, "On the way", "w"),
         (6.25, 6.75, "Juice stall row", "6:15 AM", 12, "Next", "n"), (7.0, 7.75, "Sample Caterer", "7:00 AM", 24, "Next", "n")]
col = {"d": "#7fd0c4", "w": "#ffc83d", "n": "#ffffff"}
dial = ""
for h in range(1, 13):
    x, y = pt(200, 200, 112, h); dial += f'<text x="{x:.1f}" y="{y+9:.1f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="26" fill="#9aa6e6"><tspan>{h}</tspan></text>'
for t in range(60):
    x1, y1 = pt(200, 200, 146, t / 5); x2, y2 = pt(200, 200, 140 if t % 5 else 132, t / 5)
    dial += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#4b56a8" stroke-width="{3 if t%5==0 else 1.5}"/>'
dial += '<circle cx="200" cy="200" r="170" stroke="#1d2670" stroke-width="30" fill="none"/>'
for i, (a, b, *_r, k) in enumerate(slots, 1):
    dial += f'<path d="{arc(200,200,170,a,b)}" stroke="{col[k]}" stroke-width="30" fill="none" stroke-linecap="butt"/>'
    x, y = pt(200, 200, 170, (a + b) / 2)
    dial += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="19" fill="#0f1650" stroke="{col[k]}" stroke-width="3"/><text x="{x:.1f}" y="{y+8:.1f}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="22" fill="#fff"><tspan>{i}</tspan></text>'
hx, hy = pt(200, 200, 92, 5.67); mx, my = pt(200, 200, 96, 8.0)
dial += f'<line x1="200" y1="200" x2="{hx:.1f}" y2="{hy:.1f}" stroke="#ffc83d" stroke-width="9" stroke-linecap="round"/><line x1="200" y1="200" x2="{mx:.1f}" y2="{my:.1f}" stroke="#ffc83d" stroke-width="5" stroke-linecap="round"/><circle cx="200" cy="200" r="11" fill="#ffc83d"/>'
P["p201_ice"] = page("""
body{--f:'DM Sans';--h:'Anton';background:#141b5c;color:#fff}
.bgk{position:absolute;inset:0;background:radial-gradient(circle at 85% 8%,#2a3593 0,transparent 45%),radial-gradient(circle at 0% 100%,#1f2a7a 0,transparent 50%)}
.kk{font:700 16px 'DM Sans';letter-spacing:3px;color:#ffc83d;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:76px;letter-spacing:.5px;line-height:1.2;text-transform:uppercase} h1 span{color:#ffc83d}
.vw{flex:1;display:flex;flex-direction:column;gap:16px}
.top{flex:1;display:flex;gap:18px;min-height:0}
.dl{width:440px;flex:none;background:#0f1650;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;position:relative}
.dl svg{width:410px;height:410px}
.dl p{font:700 15px/1.4 'DM Sans';letter-spacing:2.5px;color:#9aa6e6}
.lgd{display:flex;gap:16px;margin-top:14px;font:600 17px 'DM Sans';color:#dfe3ff}.lgd span{display:flex;align-items:center;gap:7px}.lgd i{width:16px;height:16px;border-radius:4px}
.ls{flex:1;display:flex;flex-direction:column;gap:10px}
.rw{flex:1;background:#f4f7ff;color:#141b5c;border-radius:22px;padding:0 20px;display:flex;align-items:center;gap:16px}
.rw i{font-style:normal;width:46px;height:46px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font:700 22px 'DM Sans';background:#141b5c;color:#fff}
.rw div{flex:1}.rw b{display:block;font:700 23px/1.3 'DM Sans'}.rw small{font:500 18px/1.4 'DM Sans';color:#5560a0}
.rw em{font-style:normal;font:700 15px 'DM Sans';border-radius:12px;padding:6px 11px;white-space:nowrap}
.rw.d em{background:#d6f1ec;color:#1d6e63}.rw.w{background:#ffc83d}.rw.w em{background:#141b5c;color:#ffc83d}.rw.w small{color:#4a3c08}.rw.n em{background:#e6e9f7;color:#3b4590}
.st{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.st div{background:#f4f7ff;color:#141b5c;border-radius:22px;padding:14px 20px;display:flex;align-items:center;gap:16px}.st b{font:400 64px/1.4 Anton;flex:none}.st span{font:600 20px/1.35 'DM Sans';color:#5560a0}
.st div:last-child{background:#ffc83d}.st div:last-child span{color:#4a3c08}
""", "<div class=kk>ICE FACTORY · MORNING ROUND</div><h1>Every shop wants ice<br>before 8 AM?<br><span>Plan it on one clock.</span></h1>",
f'''<div class=vw><div class=top><div class=dl><svg viewBox="0 0 400 400">{dial}</svg><p>TODAY · SAMPLE ROUND</p><div class=lgd><span><i style="background:#7fd0c4"></i>Delivered</span><span><i style="background:#ffc83d"></i>On the way</span><span><i style="background:#fff"></i>Next</span></div></div>
<div class=ls>{"".join(f'<div class="rw {k}"><i>{i}</i><div><b>{n}</b><small>{t} · {q} blocks</small></div><em>{s}</em></div>' for i,(a,b,n,t,q,s,k) in enumerate(slots,1))}</div></div>
<div class=st><div><b>96</b><span>blocks today</span></div><div><b>2</b><span>tempos on the road</span></div><div><b>1</b><span>bill due today: Sample Hotel</span></div></div></div>''',
"#fff", "Run an ice factory? DM us", "background:#ffc83d;color:#141b5c", bg="<div class=bgk></div>")

# ───────── 203 USA · Chimney sweep · SINGLE · Gelasio + Fira Sans · brick red / soot black / snow white
# New technique: house cut-away with chimney flue showing soot level + browser booking with ZIP check side by side.
house = '''<svg viewBox="0 0 360 560" class=hs>
<rect x="0" y="520" width="360" height="40" fill="#e9e1d6"/>
<rect x="200" y="40" width="74" height="250" fill="#a5432f"/>
<g stroke="#8a3424" stroke-width="2">''' + "".join(f'<line x1="200" y1="{y}" x2="274" y2="{y}"/>' for y in range(64, 290, 24)) + "".join(f'<line x1="{237 if (i%2) else 218}" y1="{64+24*i}" x2="{237 if (i%2) else 218}" y2="{88+24*i}"/><line x1="{256 if not (i%2) else 237}" y1="{64+24*i}" x2="{256 if not (i%2) else 237}" y2="{88+24*i}"/>' for i in range(9)) + '''</g>
<rect x="190" y="28" width="94" height="20" rx="3" fill="#2a2523"/>
<rect x="222" y="48" width="30" height="460" fill="#3b3330"/>
<rect x="226" y="60" width="22" height="440" fill="#6b5f59"/>
<rect x="226" y="120" width="22" height="380" fill="#1b1716"/>
<path d="M20 250 L180 120 L340 250 Z" fill="#2a2523"/>
<rect x="40" y="250" width="280" height="270" fill="#f7f2ea" stroke="#2a2523" stroke-width="4"/>
<rect x="190" y="420" width="90" height="100" fill="#2a2523"/><rect x="202" y="440" width="66" height="80" fill="#e2512f"/>
<path d="M214 520 Q222 488 235 500 Q240 470 252 492 Q262 480 258 520 Z" fill="#ffb347"/>
<rect x="70" y="300" width="80" height="80" fill="#cfe3ef" stroke="#2a2523" stroke-width="4"/><line x1="110" y1="300" x2="110" y2="380" stroke="#2a2523" stroke-width="4"/>
</svg>'''
P["p203_chimney"] = page("""
body{--f:'Fira Sans';--h:'Gelasio';background:#f7f2ea;color:#2a2523}
.kk{font:600 16px 'Fira Sans';letter-spacing:3px;color:#b5432f;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:66px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b5432f}
.vw{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}
.top{flex:1;display:flex;gap:18px;min-height:0}
.hc{width:350px;flex:none;background:#efe6da;border-radius:28px;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:150px 30px 0;overflow:hidden}
.hs{width:100%;height:auto;display:block}
.sootag{position:absolute;top:22px;left:18px;background:#2a2523;color:#fff;border-radius:16px;padding:10px 14px;font:500 17px/1.35 'Fira Sans';width:180px}
.sootag b{display:block;font:700 22px/1.3 Gelasio;color:#ffb347}
.bwr{flex:1;min-width:0;display:flex}
.bk{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:14px}
.bk h3{font:700 32px/1.25 Gelasio}
.zp{display:flex;align-items:center;gap:12px;border:2px solid #e2d6c6;border-radius:16px;padding:12px 16px;font:500 20px 'Fira Sans'}
.zp b{flex:1;font:600 22px 'Fira Sans'}.zp em{font-style:normal;background:#e3f1e6;color:#2b6a3a;border-radius:10px;padding:5px 10px;font:600 16px 'Fira Sans'}
.sv{display:flex;flex-direction:column;gap:10px}.sv div{border:2px solid #e2d6c6;border-radius:16px;padding:12px 16px;display:flex;gap:12px;align-items:center;font:600 20px/1.3 'Fira Sans'}
.sv i{width:24px;height:24px;border-radius:50%;border:3px solid #c9b9a5;flex:none}.sv .on{border-color:#b5432f;background:#fbeee9}.sv .on i{border:7px solid #b5432f}
.sv small{display:block;font:400 16px 'Fira Sans';color:#7a6d64}
.dl2{font:600 14px 'Fira Sans';letter-spacing:2px;color:#7a6d64}
.ds{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.ds span{border:2px solid #e2d6c6;border-radius:14px;padding:9px 0;text-align:center;font:600 17px/1.3 'Fira Sans'}.ds .x{color:#b9ada2;text-decoration:line-through}.ds .on{background:#b5432f;border-color:#b5432f;color:#fff}
.bt{margin-top:auto;background:#2a2523;color:#fff;border-radius:16px;padding:14px;text-align:center;font:600 21px 'Fira Sans'}
.rp{background:#2a2523;color:#fff;border-radius:24px;padding:18px 22px;display:flex;align-items:center;gap:18px}
.rp>b{font:700 26px/1.3 Gelasio;color:#ffb347;width:220px;flex:none}
.rp div{flex:1;display:flex;flex-wrap:wrap;gap:8px}.rp span{background:#3d3532;border-radius:12px;padding:8px 12px;font:500 17px 'Fira Sans';display:flex;gap:6px;align-items:center}
""", "<div class=kk>CHIMNEY SWEEPS · BOOKING SEASON</div><h1>Every fireplace wants<br>a sweep this month?<br><span>Let them book online.</span></h1>",
f'''<div class=vw><div class=top><div class=hc><div class=sootag><b>Soot in the flue</b>Book a sweep before the first fire.</div>{house}</div>
<div class=bwr>{browser(f"""<div class=bk><h3>Book a chimney sweep</h3>
<div class=zp>{ic("pin",24)}<b>ZIP 12345</b><em>We serve this area</em></div>
<div class=sv><div class=on><i></i><span>Sweep and inspection<small>Fireplace or wood stove</small></span></div><div><i></i><span>Inspection only<small>Photos of the flue in your report</small></span></div></div>
<div class=dl2>OPEN DAYS · SAMPLE</div>
<div class=ds><span class=x>Mon 23</span><span class=on>Tue 24</span><span>Wed 25</span><span class=x>Fri 27</span><span>Sat 28</span><span>Mon 30</span></div>
<div class=dl2>TIME</div><div class=ds><span class=on>9 AM</span><span>11 AM</span><span class=x>2 PM</span></div><div class=bt>Book Tue, Nov 24 · 9 AM</div></div>""", url="yoursweep.com/book", style="flex:1")}</div></div>
<div class=rp><b>After the visit, they get a report</b><div><span>{ic("camera",20)}Flue photos</span><span>{ic("check",20)}Cap checked</span><span>{ic("check",20)}Damper checked</span><span>{ic("cal",20)}Next sweep: Nov 2027</span></div></div></div>''',
"#2a2523", "Run a chimney service? DM us", "background:#b5432f;color:#fff")

# ───────── 204 INDIA · Lift AMC company · SINGLE · Montserrat + Roboto · graphite / LED amber / mist
# New technique: lift floor-indicator displays (LED digits + arrows) on top of drawn steel doors, one per building.
lifts = [("Sample Tower A", "7", "up", "Visit done 3 Nov", "ok", 0), ("Sample Plaza", "G", "", "Due today · Tech 1", "due", 0),
         ("Sample Heights B", "4", "", "Stuck call · Tech 2 on the way", "call", 1), ("Sample Residency", "12", "down", "Due 28 Nov", "ok2", 0),
         ("Sample Mall lift 2", "2", "up", "Due today · Tech 1", "due", 0), ("Sample Apartments", "G", "", "Visit done 9 Nov", "ok", 0)]
def lift(n, fl, ar, st, k, op):
    arr = {"up": "&#9650;", "down": "&#9660;", "": "&nbsp;"}[ar]
    return f'''<div class="lc {k}"><div class=ld><span class=ar>{arr}</span><b>{fl}</b></div>
<div class=dr><i style="{'flex:.8' if op else ''}"></i>{'<u></u>' if op else ''}<i style="{'flex:.8' if op else ''}"></i></div>
<div class=ln><b>{n}</b><em>{st}</em></div></div>'''
P["p204_lift"] = page("""
body{--f:'Roboto';--h:'Montserrat';background:#e9edf1;color:#1e2329}
.kk{font:700 16px 'Montserrat';letter-spacing:3px;color:#c77d00;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:62px;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#c77d00}
.vw{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}
.gd{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;min-height:0}
.lc{background:#fff;border-radius:22px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 10px 24px rgba(30,35,41,.08);min-height:0}
.ld{background:#111417;border-radius:12px;height:62px;display:flex;align-items:center;justify-content:center;gap:12px;flex:none}
.ld b{font:700 40px/1.3 'Roboto';color:#ffb020;text-shadow:0 0 12px rgba(255,176,32,.6);letter-spacing:2px}.ld .ar{font-size:20px;color:#ffb020;width:20px}
.dr{flex:1;min-height:70px;display:flex;gap:4px;background:#2b3138;border-radius:8px;padding:6px;overflow:hidden}
.dr u{flex:.4;background:#fff3d6;border-radius:4px}.dr i{flex:1;border-radius:4px;background:linear-gradient(90deg,#b9c2cb,#e3e8ec 45%,#a9b3bd)}
.ln b{display:block;font:700 19px/1.3 'Montserrat'}.ln em{display:inline-block;font-style:normal;margin-top:6px;font:500 15px/1.3 'Roboto';border-radius:10px;padding:5px 9px}
.ok em{background:#e2f3e7;color:#22663a}.ok2 em{background:#eef1f4;color:#4f5a66}.due em{background:#ffe9bf;color:#7a4a00}
.call{background:#1e2329;color:#fff}.call .dr{background:#ffb020}.call em{background:#e5483a;color:#fff}
.tb{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.tb div{background:#1e2329;color:#fff;border-radius:22px;padding:16px 20px;display:flex;align-items:center;gap:16px}
.tb .ib{width:56px;height:56px;border-radius:16px;background:#ffb020;color:#1e2329}
.tb b{display:block;font:700 22px/1.3 'Montserrat'}.tb span{font:400 18px/1.4 'Roboto';color:#c6ced6}
""", "<div class=kk>LIFT AMC COMPANIES · SAMPLE DAY</div><h1>Lift visits on a<br>wall chart? <span>See every<br>lift's status at once.</span></h1>",
f'''<div class=vw><div class=gd>{"".join(lift(*l) for l in lifts)}</div>
<div class=tb><div><span class=ib>{ic("wrench",30)}</span><p><b>Tech 1 · 2 visits</b><span>Sample Plaza, then Sample Mall</span></p></div><div><span class=ib>{ic("bell",30)}</span><p><b>Tech 2 · 1 stuck call</b><span>Sample Heights B, floor 4</span></p></div></div></div>''',
"#1e2329", "Run a lift service company? DM us", "background:#1e2329;color:#ffb020")

# ───────── 205 INDIA · Aquarium shop (tank care visits) · SINGLE · TeX Gyre Adventor + Inter · deep sea teal / coral / sand
# New technique: SVG aquarium with water gradient, plants, fish and gravel + 14-day visit cycle strip.
random.seed(205)
gravel = "".join(f'<ellipse cx="{random.uniform(30,830):.0f}" cy="{random.uniform(318,352):.0f}" rx="{random.uniform(5,10):.0f}" ry="{random.uniform(3,6):.0f}" fill="{random.choice(["#d9c39a","#c7ab7c","#e8d6b2","#b89a6a"])}"/>' for _ in range(190))
def fish(x, y, s, c, flip=False):
    t = f"translate({x},{y}) scale({-s if flip else s},{s})"
    return f'<g transform="{t}"><path d="M0 0 Q22 -16 44 0 Q22 16 0 0 Z" fill="{c}"/><path d="M0 0 L-14 -10 L-14 10 Z" fill="{c}"/><circle cx="34" cy="-3" r="3" fill="#0d2b33"/></g>'
plants = "".join(f'<path d="M{x} 340 Q{x-20} {260} {x+6} {200-h} Q{x+20} 260 {x+8} 340 Z" fill="{c}"/>' for x, h, c in [(90, 20, "#2f8a5f"), (120, -20, "#3ca371"), (640, 40, "#2f8a5f"), (720, 0, "#3ca371"), (770, -30, "#277a52")])
bubbles = "".join(f'<circle cx="{560+random.uniform(-8,8):.0f}" cy="{y}" r="{random.uniform(3,7):.0f}" fill="none" stroke="#e6fbff" stroke-width="2" opacity=".8"/>' for y in range(60, 300, 34))
tank = f'''<svg viewBox="0 0 860 400" class=tk><defs><linearGradient id="aqw" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fd3d8"/><stop offset="1" stop-color="#1f8a95"/></linearGradient></defs>
<rect x="10" y="20" width="840" height="340" rx="14" fill="url(#aqw)" stroke="#0d2b33" stroke-width="8"/>
<rect x="14" y="20" width="832" height="18" fill="#bfeef0" opacity=".6"/>
{gravel}{plants}{bubbles}
{fish(250,150,1.6,"#ff7a59")}{fish(420,230,1.3,"#ffd166",True)}{fish(330,95,1.1,"#ff7a59",True)}{fish(480,140,1.0,"#f4f1e8")}
<rect x="0" y="360" width="860" height="34" rx="6" fill="#0d2b33"/></svg>'''
P["p205_aquarium"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#f4ecdd;color:#0d2b33}
.kk{font:700 16px 'Inter';letter-spacing:3px;color:#e0603f;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#e0603f}
.vw{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}
.hero{background:#0d2b33;border-radius:28px;padding:20px 22px 16px;display:flex;flex-direction:column;gap:12px;position:relative}
.tk{width:100%;height:auto;display:block}
.tg{position:absolute;top:34px;right:40px;background:#f4ecdd;border-radius:14px;padding:10px 14px;font:500 16px/1.35 Inter;box-shadow:0 8px 18px rgba(0,0,0,.25)}
.tg b{display:block;font:700 20px/1.3 'TeX Gyre Adventor'}
.cy{display:flex;align-items:center;gap:6px}.cy span{flex:1;height:30px;border-radius:7px;background:#1d4a54;display:flex;align-items:center;justify-content:center;font:600 13px Inter;color:#9cc6cc}
.cy .v{background:#e0603f;color:#fff}.cy .t{background:#7fd3d8;color:#0d2b33}
.cyl{display:flex;justify-content:space-between;font:500 15px Inter;color:#9cc6cc}
.bt{flex:1;display:flex;gap:14px;min-height:0}
.lg2{flex:1.15;background:#fff;border-radius:24px;padding:16px 22px;display:flex;flex-direction:column;gap:2px;justify-content:center}
.lg2 small{font:700 14px/1.4 Inter;letter-spacing:2px;color:#6f8a8f}
.lg2 div{display:flex;align-items:center;gap:12px;padding:6px 0;border-bottom:1px solid #eee4d3;font:500 20px/1.35 Inter}.lg2 div:last-child{border:0}
.lg2 .ib{width:34px;height:34px;border-radius:50%;background:#dff3f1;color:#1f8a95}
.nx{flex:1;background:#e0603f;color:#fff;border-radius:24px;padding:20px 22px;display:flex;flex-direction:column;justify-content:space-between}
.nx small{font:700 14px/1.4 Inter;letter-spacing:2px;color:#ffe1d8}.nx b{font:700 50px/1.25 'TeX Gyre Adventor'}.nx p{font:500 19px/1.45 Inter}
""", "<div class=kk>AQUARIUM SHOPS · TANK CARE VISITS</div><h1>Tank cleaning every<br>2 weeks? <span>Never miss<br>a customer's visit.</span></h1>",
f'''<div class=vw><div class=hero>{tank}<div class=tg><b>Tank T-12 · 3 ft</b>Sample home, Sector 4</div>
<div class=cy>{"".join(f'<span class="{"v" if d in (10,24) else ("t" if d==22 else "")}">{d}</span>' for d in range(10,25))}</div>
<div class=cyl><span>Visit 10 Nov</span><span>Today 22 Nov</span><span>Next visit 24 Nov</span></div></div>
<div class=bt><div class=lg2><small>LAST VISIT · 10 NOV · SAMPLE</small>{"".join(f'<div><span class=ib>{ic("check",20)}</span>{t}</div>' for t in ["30% water change","Filter sponge cleaned","Glass cleaned inside","Fish food refilled"])}</div>
<div class=nx><small>REMINDER SENT TODAY</small><b>Visit on Tue, 24 Nov</b><p>11 AM at Sample home. Tech brings filter wool.</p></div></div></div>''',
"#0d2b33", "Run an aquarium shop? DM us", "background:#0d2b33;color:#fff")

# ───────── 202 INDIA · Curtains and blinds shop · CAROUSEL 5 · Crimson Text + Source Sans 3 · linen / terracotta / olive
# New techniques: drawn windows with dimension arrows (proportional to W x H), CSS fabric swatches, item x stage dot matrix.
CB = """
body{--f:'Source Sans 3';--h:'Crimson Text';background:#f3ece1;color:#2b2622}
h1{font-family:'Crimson Text';font-weight:700;font-size:68px;letter-spacing:-.3px;line-height:1.22} h1 span{color:#b5532f}
.kk{font:700 16px 'Source Sans 3';letter-spacing:3px;color:#5a6b3a;margin-top:22px;line-height:1.4}
.cd{background:#fffaf2;border-radius:24px;box-shadow:0 12px 28px rgba(43,38,34,.08)}
.lin{background:repeating-linear-gradient(90deg,#e9dcc6 0 2px,#efe4d2 2px 5px),repeating-linear-gradient(0deg,rgba(255,255,255,.35) 0 2px,transparent 2px 5px);background-blend-mode:multiply}
.str{background:repeating-linear-gradient(90deg,#f6efe2 0 18px,#b5532f 18px 26px,#f6efe2 26px 34px,#5a6b3a 34px 38px)}
.sag{background:#8c9c6a}
.blk{background:repeating-linear-gradient(45deg,#2f3a4a 0 6px,#334052 6px 12px)}
"""
def cb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2b2622;color:#fff"):
    return page(CB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2b2622", cta, ctacss, tagline=f"{n} / 5")

def win(w, h, kind, scale=26, fab="#b5532f"):
    W, H = w * scale, h * scale
    pad = 34
    vb = f"0 0 {W+pad*2} {H+pad*2}"
    g = f'<rect x="{pad}" y="{pad}" width="{W}" height="{H}" fill="#cfe3ef" stroke="#2b2622" stroke-width="5"/><line x1="{pad+W/2}" y1="{pad}" x2="{pad+W/2}" y2="{pad+H}" stroke="#2b2622" stroke-width="3"/>'
    if kind == "blind":
        g += f'<rect x="{pad}" y="{pad}" width="{W}" height="{H*0.55}" fill="#5a6b3a"/>' + "".join(f'<line x1="{pad}" y1="{pad+y}" x2="{pad+W}" y2="{pad+y}" stroke="#4a5a2e" stroke-width="2"/>' for y in range(12, int(H*0.55), 12))
    else:
        cw = W * 0.22
        for x0 in (pad - 6, pad + W - cw + 6):
            g += f'<rect x="{x0}" y="{pad-4}" width="{cw}" height="{H+8}" fill="{fab}"/>' + "".join(f'<line x1="{x0+i}" y1="{pad}" x2="{x0+i}" y2="{pad+H}" stroke="rgba(0,0,0,.18)" stroke-width="2"/>' for i in range(8, int(cw), 12))
        g += f'<rect x="{pad-16}" y="{pad-14}" width="{W+32}" height="8" rx="4" fill="#2b2622"/>'
    g += f'<g stroke="#b5532f" stroke-width="3"><line x1="{pad}" y1="{pad+H+20}" x2="{pad+W}" y2="{pad+H+20}"/><line x1="{pad+W+20}" y1="{pad}" x2="{pad+W+20}" y2="{pad+H}"/></g>'
    return f'<svg viewBox="{vb}" class=wn>{g}</svg>'

# slide 1 — hook: torn paper slip + question cards
slip = [("Hall", "6.5 × ?", True), ("Bedrm", "5 × 4½", False), ("Kitchen", "3 × 3 blind?", False), ("Balcony", "4 × 7 (door)", False), ("Fabric", "?? metres", True)]
P["p202_curtain_s1"] = cb(1, "CURTAIN AND BLINDS SHOPS", "Window sizes on a<br>torn paper slip?<br><span>Measure once, fit right.</span>",
f'''<div class=w1><div class=slip>{"".join(f'<div class=sr><b>{a}</b><span class="{"q" if q else ""}">{b}</span></div>' for a,b,q in slip)}<small>Sample slip from a site visit</small></div>
<div class=qs>{"".join(f'<div><span class=ib>{ic(i,30)}</span><p><b>{a}</b>{b}</p></div>' for i,a,b in [("search","Which room was 6.5 ft?","The slip says Hall, but the photo shows two windows."),("scissors","Eyelet or pleated?","The customer said it on the phone. Nobody wrote it."),("box","How many metres to cut?","Worked out again at the counter, by hand.")])}</div></div>''',
css=""".w1{flex:1;display:flex;gap:22px}
.slip{width:400px;flex:none;background:#fffdf7;border-radius:6px;padding:26px 26px 18px;transform:rotate(-2.5deg);box-shadow:0 18px 30px rgba(43,38,34,.16);display:flex;flex-direction:column;margin:10px 0;clip-path:polygon(0 0,100% 0,100% 96%,92% 100%,80% 96%,66% 100%,50% 96%,34% 100%,20% 96%,8% 100%,0 96%)}
.sr{flex:1;display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #d8e3ef;gap:10px}
.sr b{font:italic 600 32px/1.3 'Crimson Text'}.sr span{font:italic 400 32px/1.3 'Crimson Text';color:#33506e}.sr .q{color:#b5532f;text-decoration:underline wavy #b5532f}
.slip small{font:600 15px/1.4 'Source Sans 3';letter-spacing:1px;color:#8a7d70;margin:14px 0 18px}
.qs{flex:1;display:flex;flex-direction:column;gap:14px}.qs div{flex:1;background:#fffaf2;border-radius:22px;padding:18px 20px;display:flex;gap:16px;align-items:center;box-shadow:0 10px 24px rgba(43,38,34,.07);border-left:8px solid #b5532f}
.qs .ib{width:56px;height:56px;border-radius:50%;background:#f4dcd1;color:#b5532f}.qs p{font:400 20px/1.4 'Source Sans 3';color:#5b5149}.qs b{display:block;font:700 30px/1.25 'Crimson Text';color:#2b2622;margin-bottom:4px}""")

wins = [("Hall", 7, 5, "curtain", "Eyelet curtain"), ("Bedroom 1", 5, 4.5, "curtain", "Pleated curtain"), ("Kitchen", 3, 3, "blind", "Roller blind"), ("Balcony door", 4, 7, "curtain", "Eyelet curtain")]
P["p202_curtain_s2"] = cb(2, "PART 1 · MEASURE ON SITE", "Every window saved<br><span>with size and type.</span>",
f'''<div class=g2>{"".join(f'<div class="cd wc"><div class=wv>{win(w,h,k)}</div><div class=wt><b>{r}</b><span>{str(w).replace(".5","½")} × {str(h).replace(".5","½")} ft</span></div><em>{t}</em></div>' for r,w,h,k,t in wins)}</div>
<div class=nt>{ic("camera",26)}<span>Site photo saved with each window · Sample home, Sector 9</span></div>''',
css=""".vis{flex-direction:column;gap:14px}.g2{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;min-height:0}
.wc{padding:16px 20px;display:flex;flex-direction:column;gap:8px;min-height:0}.wv{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}.wn{height:100%;max-width:100%;display:block}
.wt{display:flex;justify-content:space-between;align-items:baseline}.wt b{font:700 30px/1.25 'Crimson Text'}.wt span{font:700 24px 'Source Sans 3';color:#b5532f}
.wc em{font-style:normal;align-self:flex-start;background:#e7ead9;color:#46552a;border-radius:10px;padding:5px 12px;font:600 17px 'Source Sans 3'}
.nt{display:flex;gap:12px;align-items:center;background:#2b2622;color:#fff;border-radius:18px;padding:14px 20px;font:500 20px 'Source Sans 3'}""")

fabs = [("lin", "Natural linen"), ("str", "Stripe"), ("sag", "Plain sage"), ("blk", "Blackout")]
rows = [("Hall", "7 ft wide · 7 ft drop", "4 panels × 2.4 m", "9.6 m"), ("Bedroom 1", "5 ft wide · 6½ ft drop", "3 panels × 2.2 m", "6.6 m"), ("Balcony door", "4 ft wide · 8 ft drop", "2 panels × 2.7 m", "5.4 m")]
P["p202_curtain_s3"] = cb(3, "PART 2 · FABRIC AND METRES", "Pick the fabric.<br><span>The app works out metres.</span>",
f'''<div class=w3><div class=sw>{"".join(f'<div class="{"on" if i==0 else ""}"><i class={c}></i><b>{n}</b></div>' for i,(c,n) in enumerate(fabs))}</div>
<div class="cd mt"><div class=mh><span>ROOM</span><span>PANELS</span><span>FABRIC</span></div>{"".join(f'<div class=mr><p><b>{r}</b><small>{d}</small></p><span>{p}</span><em>{m}</em></div>' for r,d,p,m in rows)}
<div class=tot><span>Natural linen for 3 rooms</span><b>21.6 m</b></div><div class=kb>{ic("check",22)}<span>Kitchen: 1 roller blind, 3 × 3 ft, olive</span></div></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px}
.sw{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.sw div{background:#fffaf2;border-radius:20px;padding:12px;display:flex;flex-direction:column;gap:10px;border:3px solid transparent}
.sw .on{border-color:#b5532f}.sw i{height:120px;border-radius:12px;display:block}.sw b{font:700 19px 'Source Sans 3';text-align:center}
.mt{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.mh{display:grid;grid-template-columns:1.5fr 1fr .7fr;font:700 14px 'Source Sans 3';letter-spacing:2px;color:#8a7d70;padding:6px 0 10px;border-bottom:2px solid #e9dcc6}
.mr{flex:1;display:grid;grid-template-columns:1.5fr 1fr .7fr;align-items:center;border-bottom:1px solid #eee3d2}
.mr b{display:block;font:700 28px/1.25 'Crimson Text'}.mr small{font:400 18px 'Source Sans 3';color:#6d6259}.mr span{font:600 20px 'Source Sans 3'}.mr em{font-style:normal;font:700 26px 'Source Sans 3';color:#b5532f}
.tot{display:flex;justify-content:space-between;align-items:center;background:#2b2622;color:#fff;border-radius:16px;padding:12px 18px;margin-top:14px}.tot span{font:600 21px 'Source Sans 3'}.tot b{font:700 36px/1.3 'Crimson Text';color:#f1b89f}
.kb{display:flex;gap:10px;align-items:center;margin-top:10px;font:600 19px 'Source Sans 3';color:#46552a}""")

stages = ["Fabric cut", "Stitching", "Ready", "Fitted"]
items = [("Hall · 4 panels", 1), ("Bedroom 1 · 3 panels", 2), ("Balcony · 2 panels", 2), ("Kitchen · roller blind", 2)]
P["p202_curtain_s4"] = cb(4, "PART 3 · STITCHING AND FITTING", "Know what is ready<br><span>before the fitting day.</span>",
f'''<div class=w4><div class="cd mx"><div class=xh><span></span>{"".join(f'<span>{s}</span>' for s in stages)}</div>
{"".join(f'<div class=xr><b>{n}</b>{"".join(f"<i class={chr(34)}{'dn' if j<d else ('nw' if j==d else '')}{chr(34)}></i>" for j in range(4))}</div>' for n,d in items)}
<div class=xl><span><i class=dn></i>Done</span><span><i class=nw></i>Now</span><span><i></i>Waiting</span></div></div>
<div class=fx><div class=fd><small>FITTING · SAMPLE HOME</small><b>Sat, 28 Nov · 11 AM</b><span>Hall stitching ends Thursday.</span></div>
<div class=fl><small>TEAM CARRIES</small>{"".join(f'<p>{ic("check",20)}{t}</p>' for t in ["3 curtain rods + brackets","9 stitched panels","1 roller blind, 3 × 3 ft","Drill and spirit level"])}</div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px}
.mx{flex:1;padding:16px 24px;display:flex;flex-direction:column}
.xh,.xr{display:grid;grid-template-columns:1.7fr repeat(4,1fr);align-items:center;gap:6px}
.xh span{font:700 15px/1.3 'Source Sans 3';letter-spacing:1px;color:#8a7d70;text-align:center;padding-bottom:8px}
.xr{flex:1;border-top:1px solid #eee3d2}.xr b{font:700 26px/1.25 'Crimson Text'}
.xr i,.xl i{justify-self:center;width:40px;height:40px;border-radius:50%;border:3px dashed #cdbfa9}
.xr i.dn,.xl i.dn{background:#5a6b3a;border:3px solid #5a6b3a}.xr i.nw,.xl i.nw{background:#f4dcd1;border:3px solid #b5532f;box-shadow:0 0 0 6px rgba(181,83,47,.15)}
.xl{display:flex;gap:22px;padding-top:12px;font:600 18px 'Source Sans 3'}.xl span{display:flex;gap:8px;align-items:center}.xl i{width:22px;height:22px}
.fx{display:flex;gap:14px}.fd{flex:1;background:#b5532f;color:#fff;border-radius:22px;padding:20px 22px;display:flex;flex-direction:column;gap:6px;justify-content:center}
.fd small,.fl small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;opacity:.8}.fd b{font:700 40px/1.25 'Crimson Text'}.fd span{font:500 20px 'Source Sans 3'}
.fl{flex:1;background:#2b2622;color:#fff;border-radius:22px;padding:18px 22px;display:flex;flex-direction:column;gap:6px}.fl p{display:flex;gap:10px;align-items:center;font:500 19px/1.35 'Source Sans 3'}.fl p svg{color:#a9bb7d;flex:none}""")

P["p202_curtain_s5"] = cb(5, "YOUR TURN", "Sell curtains and blinds?<br><span>Let's build your<br>measure-to-fit app.</span>",
f'''<div class=w5><div class="cd big">{win(7,5,"curtain",40)}</div>
<div class=t5>{"".join(f'<div><span class=ib>{ic(i,34)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("camera","Site measure","Size, type, photo"),("tag","Fabric picker","Metres worked out"),("check","Job tracker","Cut to fitted"),("cal","Fitting day","Team list ready")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#b5532f;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px}.big{flex:1;min-height:0;display:flex;align-items:center;justify-content:center;padding:16px}.big .wn{height:100%;max-width:100%}
.t5{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.t5 div{background:#2b2622;color:#fff;border-radius:22px;padding:18px;display:flex;flex-direction:column;gap:6px}
.t5 div:nth-child(2n){background:#5a6b3a}.t5 .ib{width:58px;height:58px;border-radius:16px;background:rgba(255,255,255,.12);margin-bottom:8px}.t5 b{font:700 26px/1.2 'Crimson Text'}.t5 small{font:500 17px/1.35 'Source Sans 3';opacity:.85}""")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
