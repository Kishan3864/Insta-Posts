import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 336 INDIA · Gas cylinder agency (home refills) · SINGLE · Bitter + Inter · steel teal / flame orange / ivory
# New technique: diagonal before/after split (two clip-path layers in one card) with a "before" paper diary + missed
# calls on top and an "after" rider board below, where SVG cylinder icons (filled = delivered) carry the counts.
RID = [("Rider 1", "Lanes 1 to 4", 14, 9), ("Rider 2", "Market road", 12, 7), ("Rider 3", "Tower area", 10, 4)]
def cyl(full):
    f, s = ("#f26b1d", "#f26b1d") if full else ("none", "#7fb3b7")
    return (f'<svg viewBox="0 0 34 52" class=cy6><rect x="12" y="2" width="10" height="7" rx="2" fill="{s}"/>'
            f'<rect x="4" y="9" width="26" height="40" rx="11" fill="{f}" stroke="{s}" stroke-width="3"/>'
            f'<line x1="6" y1="22" x2="28" y2="22" stroke="{"#fff" if full else s}" stroke-opacity=".6" stroke-width="2"/></svg>')
TB = sum(r[2] for r in RID); TD = sum(r[3] for r in RID)
P["p336_gas"] = page("""
body{--f:'Inter';--h:'Bitter';background:#faf5ea;color:#123c40}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#d2560f;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;line-height:1.22;letter-spacing:-1px} h1 span{color:#0f5c63}
.sp6{flex:1;position:relative;border-radius:28px;overflow:hidden;box-shadow:0 18px 40px rgba(18,60,64,.14)}
.ly6{position:absolute;inset:0}
.bf6{background:#fff3d9 repeating-linear-gradient(transparent 0 47px,#ecdcb5 47px 49px);clip-path:polygon(0 0,100% 0,100% 36%,0 47%)}
.af6{background:#0f5c63;clip-path:polygon(0 49%,100% 38%,100% 100%,0 100%)}
.tp6{position:absolute;left:30px;right:30px;top:24px;height:290px;display:grid;grid-template-columns:1.35fr 1fr;gap:20px}
.dr6{display:flex;flex-direction:column;gap:3px}
.dr6 small,.bt6>small{font:700 14px/1.4 Inter;letter-spacing:2px;color:#9a6a12}
.dr6 p{font:italic 500 26px/49px Bitter;color:#5b4320}.dr6 s{color:#c2410c}
.mc6{display:flex;flex-direction:column;gap:10px;justify-content:flex-start;padding-top:4px}
.ml6{display:flex;align-items:center;gap:12px;background:#fff;border-radius:16px;padding:10px 14px;box-shadow:0 6px 14px rgba(91,67,32,.12);font:600 18px/1.35 Inter;color:#9b2c0c}
.ml6 .ib{width:38px;height:38px;border-radius:50%;background:#ffe1d1;color:#d2560f}.ml6>span:nth-child(2){flex:1}.ml6 em{font:500 15px/1.3 Inter;font-style:normal;color:#7a6a55}
.pl6{position:absolute;left:50%;top:42.5%;transform:translate(-50%,-50%) rotate(-5.5deg);display:flex;gap:14px;align-items:center;z-index:3}
.pl6 span{font:700 17px/1.3 Inter;letter-spacing:2px;padding:9px 18px;border-radius:30px}
.pl6 .a{background:#fff3d9;color:#9a6a12;box-shadow:0 0 0 2px #ecdcb5}.pl6 .b{background:#f26b1d;color:#fff}
.bt6{position:absolute;left:30px;right:30px;top:51%;bottom:24px;display:flex;flex-direction:column;gap:14px}
.bt6>small{color:#a8d4d6}
.rs6{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;min-height:0}
.rc6{background:#16737b;border-radius:20px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;color:#fff}
.rc6 b{font:700 24px/1.3 Bitter}.rc6>span{font:500 16px/1.35 Inter;color:#c6e6e7}
.gr6{flex:1;display:grid;grid-template-columns:repeat(5,1fr);gap:6px 6px;align-content:center}.cy6{width:100%;height:40px;display:block}
.rc6 strong{font:700 19px/1.35 Inter;color:#ffd2b8}.rc6 strong em{font-style:normal;color:#fff;font-weight:500}
.ms6{display:flex;gap:16px;align-items:center;background:#faf5ea;border-radius:20px 20px 20px 6px;padding:14px 20px;color:#123c40}
.ms6 .ib{width:50px;height:50px;border-radius:14px;background:#f26b1d;color:#fff}
.ms6 div{font:500 20px/1.4 Inter}.ms6 b{display:block;font:700 16px/1.4 Inter;color:#d2560f;letter-spacing:.5px}
""", "<div class=kk>GAS CYLINDER AGENCY · HOME REFILLS</div><h1>Refill calls all morning?<br><span>Put every booking on one list.</span></h1>",
f'''<div class=sp6><div class="ly6 bf6"></div><div class="ly6 af6"></div>
<div class=tp6><div class=dr6><small>BEFORE · DIARY, MONDAY</small><p>House 14, Lane 2 · called twice<br>Shop 6 · <s>empty not back</s> ask again<br>Who took the 9 AM list?<br>Rider 2 brought 3 full ones back?<br>Lane 3 · booked Friday? check</p></div>
<div class=mc6>{"".join(f'<div class=ml6><span class=ib>{ic("phone",20)}</span><span>Missed call</span><em>{t}</em></div>' for t in ["9:12 AM","9:14 AM","9:20 AM","9:31 AM"])}</div></div>
<div class=pl6><span class=a>BEFORE</span><span class=b>AFTER</span></div>
<div class=bt6><small>AFTER · TODAY'S REFILL LIST · {TB} BOOKINGS · SAMPLE</small>
<div class=rs6>{"".join(f'<div class=rc6><b>{n}</b><span>{a}</span><div class=gr6>{"".join(cyl(i<d) for i in range(t))}</div><strong>{d} of {t} delivered<br><em>Empties back: {d}</em></strong></div>' for n,a,t,d in RID)}</div>
<div class=ms6><span class=ib>{ic("chat",26)}</span><div><b>BOOKED BY MESSAGE · B-218</b>Your refill comes today, 2 to 4 PM. Please keep the empty cylinder ready.</div></div></div></div>''',
"#123c40", "Run a gas agency? DM us", "background:#f26b1d;color:#fff")

# ───────── 338 USA · Mobile windshield chip repair · SINGLE · Poppins + Open Sans · glass sky blue / resin amber / charcoal
# New technique: SVG windshield (trapezoid glass gradient, wiper arcs, mirror) with numbered damage marks drawn as
# star breaks + a crack, feeding a browser booking page whose slots are taken from one schedule list.
SL8 = [("8:00 AM", 1), ("9:30 AM", 0), ("11:00 AM", 1), ("12:30 PM", 0), ("2:00 PM", 0), ("3:30 PM", 1)]
def star(x, y, r):
    pts = "".join(f'<line x1="{x}" y1="{y}" x2="{x+math.cos(a)*r:.1f}" y2="{y+math.sin(a)*r:.1f}" stroke="#fff" stroke-width="2.4" stroke-linecap="round"/>' for a in [k*math.pi/4+0.3 for k in range(8)])
    return pts + f'<circle cx="{x}" cy="{y}" r="{r*.32:.1f}" fill="#fff" fill-opacity=".85"/>'
def shield():
    W, H = 900, 330
    s = f'<svg viewBox="0 0 {W} {H}" class=ws8><defs><linearGradient id="gl8" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9fd3f2"/><stop offset=".55" stop-color="#4b93c9"/><stop offset="1" stop-color="#2b5f8e"/></linearGradient></defs>'
    s += '<path d="M120 24 Q450 0 780 24 L870 300 Q450 330 30 300 Z" fill="#2a2e35"/><path d="M134 38 Q450 16 766 38 L848 288 Q450 314 52 288 Z" fill="url(#gl8)"/>'
    s += '<path d="M200 60 L330 60 L180 260 L110 260 Z" fill="#fff" fill-opacity=".14"/><rect x="420" y="30" width="60" height="34" rx="8" fill="#2a2e35"/>'
    s += '<path d="M150 292 Q300 150 450 292" fill="none" stroke="#1d2127" stroke-width="7" stroke-linecap="round"/><path d="M450 292 Q600 150 750 292" fill="none" stroke="#1d2127" stroke-width="7" stroke-linecap="round"/>'
    s += star(300, 130, 22) + star(610, 190, 16)
    s += '<path d="M680 70 L700 96 L692 120 L716 150 L708 176" fill="none" stroke="#fff" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    for n, x, y in [(1, 338, 92), (2, 646, 160), (3, 742, 70)]:
        s += f'<circle cx="{x}" cy="{y}" r="19" fill="#f5a524" stroke="#1d2127" stroke-width="3"/><text x="{x-6}" y="{y+7}" font-family="Poppins" font-weight="700" font-size="20" fill="#1d2127">{n}</text>'
    return s + "</svg>"
slots8 = "".join(f'<span class="{"tk" if t else ("on" if h=="12:30 PM" else "")}">{h}</span>' for h, t in SL8)
form8 = f"""<div class=bf8><div class=cl8><b>Book a glass repair</b><small>1 · WHAT HAPPENED</small><div class=ch8><span class=on>Chip</span><span class=on>Crack</span><span>Full windshield</span></div>
<div class=pf8><i></i><span>Photo added: 2 chips and 1 crack</span></div><div class=fd8><small>VEHICLE</small><span>Sample sedan, 2019</span></div><div class=fd8><small>ADDRESS</small><span>Sample St, home driveway</span></div><div class=fd8><small>ZIP CODE</small><span>Inside our service area</span></div></div>
<div class=cl8><small>2 · WHERE AND WHEN</small><div class=ch8><span class=on>Home driveway</span><span>Work parking lot</span></div><div class=fd8><small>DATE</small><span>Tuesday, December 1</span></div>
<div class=sl8>{slots8}</div><div class=tx8>We text you when the tech is on the way.</div><div class=bk8>Book 12:30 PM</div></div></div>"""
P["p338_glass"] = page("""
body{--f:'Open Sans';--h:'Poppins';background:#e7f1f8;color:#1d2127}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#2b6ea6;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#d98a00}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ph8{background:#fff;border-radius:24px;padding:16px 24px 18px;display:flex;flex-direction:column;gap:12px;box-shadow:0 12px 28px rgba(29,33,39,.08)}
.ws8{width:100%;display:block}
.dm8{display:grid;grid-template-columns:auto 1fr 1fr 1fr;gap:16px;align-items:center}.dm8>small{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#5b6573}
.dl8{display:flex;gap:10px;align-items:flex-start;font:500 17px/1.35 'Open Sans'}.dl8 i{flex:none;width:28px;height:28px;border-radius:50%;background:#f5a524;font:700 15px/28px Poppins;font-style:normal;text-align:center}
.dl8 b{display:block;font:700 17px/1.35 Poppins}
.bw8{flex:1;min-height:0;display:flex}.ws8{max-height:262px}.bw8>.browser{flex:1}
.bf8{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px;padding:18px 22px 20px;min-height:0}
.cl8{display:flex;flex-direction:column;gap:10px}
.cl8>b{font:700 24px/1.3 Poppins}.cl8>small{font:700 13px/1.4 'Open Sans';letter-spacing:1.5px;color:#5b6573;margin-top:4px}
.fd8{background:#f1f5f9;border-radius:12px;padding:9px 14px}.fd8 small{display:block;font:700 12px/1.4 'Open Sans';letter-spacing:1.5px;color:#5b6573}.fd8 span{font:600 18px/1.4 'Open Sans'}
.ch8{display:flex;gap:8px;flex-wrap:wrap}.ch8 span{font:600 16px/1.3 'Open Sans';padding:8px 13px;border-radius:10px;background:#f1f5f9}.ch8 span.on{background:#1d2127;color:#fff}
.pf8{display:flex;gap:12px;align-items:center;background:#fff6e5;border-radius:12px;padding:10px 12px;font:600 16px/1.35 'Open Sans'}.pf8 i{width:64px;height:46px;border-radius:8px;flex:none;background:linear-gradient(135deg,#9fd3f2,#2b5f8e)}
.sl8{display:grid;grid-template-columns:1fr 1fr;gap:8px}.sl8 span{font:600 16px/1.3 'Open Sans';text-align:center;padding:10px 4px;border-radius:10px;background:#e3f0fa;color:#1d4f7a}
.sl8 span.tk{background:#eceff2;color:#9aa3ad;text-decoration:line-through}.sl8 span.on{background:#f5a524;color:#1d2127}
.tx8{font:600 16px/1.4 'Open Sans';color:#1d4f7a;background:#e3f0fa;border-radius:12px;padding:10px 14px}.bk8{margin-top:auto;background:#1d2127;color:#fff;border-radius:12px;padding:13px;text-align:center;font:700 17px Poppins}
""", "<div class=kk>MOBILE WINDSHIELD REPAIR</div><h1>A chip on the windshield?<br><span>Let them book it online.</span></h1>",
f'''<div class=vw><div class=ph8>{shield()}<div class=dm8><small>CUSTOMER<br>PHOTO<br>SAMPLE</small>
<div class=dl8><i>1</i><div><b>Star chip</b>Passenger side</div></div><div class=dl8><i>2</i><div><b>Small chip</b>Low, center</div></div><div class=dl8><i>3</i><div><b>Crack</b>Upper right</div></div></div></div>
<div class=bw8>{browser(form8, url="yourglassrepair.com/book · sample")}</div></div>''',
"#1d2127", "Fix glass on the go? DM us", "background:#f5a524;color:#1d2127")

# ───────── 339 INDIA · Jaggery (gur) unit · SINGLE · Crimson Text + Fira Sans · jaggery brown / cane green / cream gold
# New technique: top-down SVG boiling pans (radial syrup gradient, seeded bubbles, progress ring as a stroke-dasharray arc)
# + CSS jaggery block stacks whose counts match the buyer order list.
PANS = [("Pan 1", "Juice heating", 0.25, "Ready 3:40 PM"), ("Pan 2", "Thickening", 0.6, "Ready 2:10 PM"), ("Pan 3", "Ready to set", 0.95, "Setting now")]
def pan(st, seed):
    random.seed(seed); r = 120; c = 2 * math.pi * 132
    col = ["#e9c46a", "#c9842b", "#8a4b17"][0 if st < .4 else (1 if st < .8 else 2)]
    s = f'<svg viewBox="0 0 300 300" class=pn9><defs><radialGradient id="sy{seed}"><stop offset="0" stop-color="{col}"/><stop offset="1" stop-color="#5a2e0e"/></radialGradient></defs>'
    s += '<circle cx="150" cy="150" r="146" fill="#3a3330"/><circle cx="150" cy="150" r="132" fill="none" stroke="#5b524d" stroke-width="10"/>'
    s += f'<circle cx="150" cy="150" r="132" fill="none" stroke="#9bcf53" stroke-width="10" stroke-linecap="round" stroke-dasharray="{c*st:.0f} {c:.0f}" transform="rotate(-90 150 150)"/>'
    s += f'<circle cx="150" cy="150" r="{r}" fill="url(#sy{seed})"/>'
    s += "".join(f'<circle cx="{150+math.cos(a)*d:.0f}" cy="{150+math.sin(a)*d:.0f}" r="{random.uniform(3,9):.1f}" fill="#fff" fill-opacity=".22"/>' for a, d in [(random.uniform(0, 6.28), random.uniform(0, 100)) for _ in range(26)])
    return s + "</svg>"
STK = [("1 kg blocks", 120, 3), ("5 kg buckets", 18, 2), ("Powder, 1 kg bags", 40, 1)]
ORD9 = [("Shop A, town market", "1 kg blocks", 60), ("Sweet maker B", "5 kg buckets", 10), ("Shop C, highway", "1 kg blocks", 40), ("Home buyer D", "Powder, 1 kg bags", 6)]
need9 = {k: sum(q for _, b, q in ORD9 if b == k) for k, _, _ in STK}
def stack9(k):
    hs = [46, 60, 40] if k == 3 else ([62, 62] if k == 2 else [24, 24, 24])
    return "".join(f'<i style="height:{h}px"></i>' for h in hs)
unit9 = {3: "blocks", 2: "buckets", 1: "bags"}
P["p339_gur"] = page("""
body{--f:'Fira Sans';--h:'Crimson Text';background:#f7ecd4;color:#3d220c}
.kk{font:600 16px/1.4 'Fira Sans';letter-spacing:3px;color:#6d8f2a;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:66px;line-height:1.18;letter-spacing:-.5px} h1 span{color:#a05a12}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pr9{background:#2b2420;border-radius:26px;padding:16px 22px 18px;display:flex;flex-direction:column;gap:10px;color:#f7ecd4}
.pr9>small,.st9>small,.od9>small{font:600 13px/1.4 'Fira Sans';letter-spacing:2px;color:#c8b48f}
.pp9{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.pc9{display:flex;flex-direction:column;align-items:center;gap:6px}.pn9{width:200px;height:200px;display:block}
.pc9 b{font:700 28px/1.2 'Crimson Text'}.pc9 span{font:500 17px/1.35 'Fira Sans';color:#e8d8b8}.pc9 em{font:600 16px/1.3 'Fira Sans';font-style:normal;background:#9bcf53;color:#2b2420;border-radius:8px;padding:4px 10px}
.bt9{flex:1;display:grid;grid-template-columns:1fr 1.15fr;gap:14px;min-height:0}
.st9,.od9{background:#fffaf0;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 12px 26px rgba(61,34,12,.08)}
.st9>small,.od9>small{color:#7a6248}
.sr9{flex:1;display:flex;align-items:center;gap:14px;border-bottom:1px solid #efe2c8}.sr9:last-child{border:0}
.bl9{display:flex;gap:4px;align-items:flex-end;width:110px;flex:none}.bl9 i{width:30px;border-radius:6px 6px 4px 4px;background:linear-gradient(160deg,#c9842b,#7a3f12);box-shadow:inset 0 -5px 0 rgba(0,0,0,.18)}
.sr9>div:nth-child(2){flex:1}.sr9 b{display:block;font:700 23px/1.2 'Crimson Text'}.sr9 span{font:500 16px/1.35 'Fira Sans';color:#6a5440}
.sr9 strong{font:700 32px/1.2 'Crimson Text';color:#a05a12}
.or9{display:grid;grid-template-columns:1fr auto;gap:2px 10px;padding:9px 0;border-bottom:1px solid #efe2c8}.or9 b{font:600 18px/1.35 'Fira Sans'}.or9 span{font:500 15px/1.35 'Fira Sans';color:#6a5440}.or9 strong{grid-row:1 / 3;grid-column:2;align-self:center;font:700 26px/1.2 'Crimson Text'}
.nt9{margin-top:auto;background:#6d8f2a;color:#fff;border-radius:14px;padding:12px 14px;font:500 17px/1.4 'Fira Sans'}.nt9 b{color:#f1ffd0}
""", "<div class=kk>JAGGERY (GUR) UNIT · CANE SEASON</div><h1>Pans boiling, buyers calling?<br><span>See every batch and order.</span></h1>",
f'''<div class=vw><div class=pr9><small>BOILING HOUSE · TODAY · GREEN RING = HOW FAR ALONG · SAMPLE</small><div class=pp9>{"".join(f'<div class=pc9>{pan(st,i)}<b>{n}</b><span>{t}</span><em>{r}</em></div>' for i,(n,t,st,r) in enumerate(PANS))}</div></div>
<div class=bt9><div class=st9><small>IN STOCK · SAMPLE</small>{"".join(f'<div class=sr9><div class=bl9>{stack9(k)}</div><div><b>{a}</b><span>Ready to send</span></div><strong>{q}</strong></div>' for a,q,k in STK)}</div>
<div class=od9><small>ORDERS FOR TOMORROW · SAMPLE</small>{"".join(f'<div class=or9><b>{a}</b><span>{b}</span><strong>{q}</strong></div>' for a,b,q in ORD9)}
<div class=nt9>All 4 orders fit today's stock: <b>{need9["1 kg blocks"]} of 120 blocks</b>, {need9["5 kg buckets"]} of 18 buckets, {need9["Powder, 1 kg bags"]} of 40 bags.</div></div></div></div>''',
"#3d220c", "Make jaggery? DM us", "background:#3d220c;color:#f7ecd4")

# ───────── 340 INDIA · Weighbridge (dharam kanta) · SINGLE · Anton + Source Sans 3 · highway yellow / LED red / asphalt
# New technique: stamp-style approval slip (double ink border, unrotated) next to an SVG truck on a weighbridge deck
# with a red LED readout; net weights in the register are computed from gross minus tare.
TRK = [("1041", "GJ 05 sample", "Sand", 32460, 12180, "9:05 AM"), ("1042", "GJ 06 sample", "Cotton bales", 18420, 9340, "9:40 AM"),
       ("1043", "GJ 01 sample", "Cement bags", 27900, 11260, "10:15 AM"), ("1044", "GJ 05 sample", "Scrap iron", 21350, 10870, "10:50 AM"),
       ("1045", "GJ 18 sample", "Wheat bags", 25120, 10990, "11:30 AM")]
fmt = lambda n: f"{n:,}"
cur = TRK[1]
def truck0():
    W, H = 560, 300
    s = f'<svg viewBox="0 0 {W} {H}" class=tk0>'
    s += '<rect x="0" y="250" width="560" height="50" fill="#3a3d42"/><rect x="40" y="236" width="480" height="18" rx="3" fill="#f2c230"/>'
    s += "".join(f'<rect x="{60+i*44}" y="240" width="22" height="10" fill="#2b2d31"/>' for i in range(11))
    s += '<rect x="64" y="70" width="300" height="150" rx="6" fill="#d9e1e8" stroke="#2b2d31" stroke-width="4"/>'
    s += "".join(f'<rect x="{78+i*70}" y="86" width="58" height="56" rx="6" fill="#efe4c9" stroke="#b9a77c" stroke-width="3"/><rect x="{78+i*70}" y="150" width="58" height="56" rx="6" fill="#efe4c9" stroke="#b9a77c" stroke-width="3"/>' for i in range(4))
    s += '<path d="M372 220 L372 120 Q372 104 388 104 L452 104 L494 160 L494 220 Z" fill="#e2463b" stroke="#2b2d31" stroke-width="4"/><path d="M388 118 L446 118 L478 158 L388 158 Z" fill="#a8d2ef"/>'
    s += '<rect x="56" y="214" width="446" height="16" rx="4" fill="#2b2d31"/>'
    for x in (120, 200, 430):
        s += f'<circle cx="{x}" cy="232" r="24" fill="#1f2125"/><circle cx="{x}" cy="232" r="10" fill="#9aa0a8"/>'
    return s + "</svg>"
P["p340_kanta"] = page("""
body{--f:'Source Sans 3';--h:'Anton';background:#f4efe2;color:#1f2125}
.kk{font:700 16px/1.5 'Source Sans 3';letter-spacing:3px;color:#c0392b;margin-top:22px;margin-bottom:4px}
h1{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.25;letter-spacing:.3px;text-transform:uppercase} h1 span{color:#c0392b}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp0{display:grid;grid-template-columns:1.25fr 1fr;gap:14px}
.sc0{background:#2b2d31;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.ld0{background:#120607;border-radius:14px;padding:8px 16px 10px;display:flex;justify-content:space-between;align-items:center;box-shadow:inset 0 0 0 3px #3e1714}
.ld0 small{font:700 13px/1.5 'Source Sans 3';letter-spacing:2px;color:#d98b84}.ld0 b{font:400 50px/1.3 Anton;letter-spacing:4px;color:#ff4136;text-shadow:0 0 12px rgba(255,65,54,.7)}
.tk0{width:100%;display:block}
.sp0{background:#fffdf5;border-radius:24px;padding:16px;box-shadow:0 12px 26px rgba(31,33,37,.1);display:flex}
.st0{flex:1;border:4px double #1f5fa8;border-radius:14px;padding:12px 16px;display:flex;flex-direction:column;gap:6px;color:#1f5fa8}
.st0>b{font:400 30px/1.5 Anton;letter-spacing:1px;margin-bottom:2px}.st0>small{font:700 13px/1.5 'Source Sans 3';letter-spacing:2px;color:#4a76b0}
.sl0{display:flex;justify-content:space-between;font:600 19px/1.4 'Source Sans 3';color:#1f2125;border-bottom:1px dashed #b8c8de;padding:4px 0}.sl0 strong{font-weight:700}
.sl0.nt{border:0;font:700 22px/1.4 'Source Sans 3';color:#1f5fa8}
.ok0{margin-top:auto;border:3px solid #1f8a4c;color:#1f8a4c;border-radius:10px;text-align:center;font:400 22px/1.5 Anton;letter-spacing:2px;padding:4px}
.rg0{flex:1;min-height:0;background:#fff;border-radius:24px;padding:12px 22px;display:flex;flex-direction:column;box-shadow:0 12px 26px rgba(31,33,37,.08)}
.rr0{flex:1;display:grid;grid-template-columns:80px 150px 1fr 110px 110px 120px;gap:10px;align-items:center;border-bottom:1px solid #ece6d6;font:500 18px/1.35 'Source Sans 3'}
.rr0:last-child{border:0}.rr0 strong{font:400 22px/1.5 Anton;letter-spacing:.5px;text-align:right}.rr0 span:nth-child(4),.rr0 span:nth-child(5){text-align:right}
.rh0{flex:none;padding-bottom:8px;border-bottom:2px solid #1f2125;font:700 13px/1.5 'Source Sans 3';letter-spacing:1.5px;color:#6b6559}.rh0 span{text-align:left}.rh0 span:nth-child(n+4){text-align:right}
.rr0.on{background:#fff6d6;margin:0 -12px;padding:0 12px;border-radius:10px}
.ms0{display:flex;gap:14px;align-items:center;background:#1f2125;color:#fff;border-radius:20px;padding:14px 20px;font:500 20px/1.4 'Source Sans 3'}.ms0 .ib{width:48px;height:48px;border-radius:14px;background:#f2c230;color:#1f2125}.ms0 b{color:#f2c230}
""", "<div class=kk>WEIGHBRIDGE · DHARAM KANTA</div><h1>Handwritten weight slips?<br><span>Print them. Send them.</span></h1>",
f'''<div class=vw><div class=tp0><div class=sc0><div class=ld0><small>ON THE BRIDGE NOW</small><b>{fmt(cur[3])} KG</b></div>{truck0()}</div>
<div class=sp0><div class=st0><b>WEIGHT SLIP {cur[0]}</b><small>MON 23 NOV · {cur[5]} · SAMPLE</small>
<div class=sl0><span>Truck</span><strong>{cur[1]}</strong></div><div class=sl0><span>Load</span><strong>{cur[2]}</strong></div>
<div class=sl0><span>Gross</span><strong>{fmt(cur[3])} kg</strong></div><div class=sl0><span>Empty (tare)</span><strong>{fmt(cur[4])} kg</strong></div>
<div class="sl0 nt"><span>Net</span><span>{fmt(cur[3]-cur[4])} kg</span></div><div class=ok0>CHECKED · PAID BY UPI</div></div></div></div>
<div class=rg0><div class="rr0 rh0"><span>SLIP</span><span>TRUCK</span><span>LOAD</span><span>GROSS KG</span><span>TARE KG</span><span>NET KG</span></div>
{"".join(f'<div class="rr0 {"on" if t[0]==cur[0] else ""}"><span>{t[0]}</span><span>{t[1]}</span><span>{t[2]}</span><span>{fmt(t[3])}</span><span>{fmt(t[4])}</span><strong>{fmt(t[3]-t[4])}</strong></div>' for t in TRK)}</div>
<div class=ms0><span class=ib>{ic("send",24)}</span><span>Slip {cur[0]} goes to the driver and buyer by message. <b>No more "the slip got wet".</b></span></div></div>''',
"#1f2125", "Run a weighbridge? DM us", "background:#c0392b;color:#fff")

# ───────── 337 INDIA · Paver block maker · CAROUSEL 5 · Montserrat + Roboto · concrete grey / terracotta / moss
# New technique: SVG basket-weave paver patch (seeded shades) reused across slides, conic-gradient curing rings
# on top-down pallets, and truck trips derived from the order sheet (blocks = sq ft x rate + 5% for cuts).
import math as _m
PV = """
body{--f:'Roboto';--h:'Montserrat';background:#ebe8e3;color:#26282b}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#b4532a;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:58px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#b4532a}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(38,40,43,.08)}
.cap{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#73767b}
.nb{display:flex;align-items:center;gap:14px;background:#26282b;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Roboto}.nb .ib{width:50px;height:50px;border-radius:14px;background:#6f8f3d;color:#fff}.nb b{color:#f0b48f}
"""
def pv(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#26282b;color:#f0b48f"):
    return page(PV + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#26282b", cta, ctacss, tagline=f"{n} / 5")
COLS = {"red": ["#b4532a", "#a64a24", "#c25f34", "#9c4421"], "grey": ["#8d9096", "#7f8288", "#989ba1", "#868990"], "moss": ["#6f8f3d", "#668536", "#7a9a46", "#5f7d31"]}
def patch(W, H, cell=60, col="red", seed=1, mix=None):
    random.seed(seed); g = 4
    s = f'<svg viewBox="0 0 {W} {H}" class=pt7 preserveAspectRatio="xMidYMid slice"><rect width="{W}" height="{H}" fill="#55585d"/>'
    for r in range(H // cell + 1):
        for c in range(W // cell + 1):
            x, y = c * cell, r * cell; cc = (mix(r, c) if mix else col)
            f = lambda: random.choice(COLS[cc])
            if (r + c) % 2 == 0:
                s += f'<rect x="{x+g/2}" y="{y+g/2}" width="{cell-g}" height="{cell/2-g}" rx="3" fill="{f()}"/><rect x="{x+g/2}" y="{y+cell/2+g/2}" width="{cell-g}" height="{cell/2-g}" rx="3" fill="{f()}"/>'
            else:
                s += f'<rect x="{x+g/2}" y="{y+g/2}" width="{cell/2-g}" height="{cell-g}" rx="3" fill="{f()}"/><rect x="{x+cell/2+g/2}" y="{y+g/2}" width="{cell/2-g}" height="{cell-g}" rx="3" fill="{f()}"/>'
    return s + "</svg>"
RATE = {"Rectangle": 4.5, "Zigzag": 4, "Square, 1 ft": 1}
ORD7 = [("Order 14", "House driveway", "Rectangle", "Red", 1200), ("Order 15", "Shop front", "Zigzag", "Grey", 800),
        ("Order 16", "Garden path", "Square, 1 ft", "Moss", 400), ("Order 17", "Society lane", "Rectangle", "Grey", 600)]
def blocks(o): base = o[4] * RATE[o[2]]; return int(base), int(_m.ceil(base * 1.05))
TRIP = 3000
o14 = ORD7[0]; b14 = blocks(o14)[1]
P["p337_paver_s1"] = pv(1, "PAVER BLOCK MAKER · ORDERS AND DISPATCH", "Orders come in sq ft.<br><span>How many blocks is that?</span>",
f'''<div class=w1><div class="cd c1">{patch(900, 560, 70, "red", 7)}<div class=tg1><b>{o14[0]} · {o14[1]}</b><span>{fmt(o14[4])} sq ft · {o14[2].lower()} · {o14[3].lower()} · sample</span></div></div>
<div class=gs1>{"".join(f'<div class=gq1><span>Counted on the phone</span><b>{g}</b></div>' for g in ["4,800?","5,200?","6,000?"])}<div class="gq1 ok"><span>Worked out by the app</span><b>{fmt(b14)}</b></div></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c1{flex:1;min-height:0;overflow:hidden;position:relative;padding:0}.pt7{width:100%;height:100%;display:block}
.tg1{position:absolute;left:22px;bottom:22px;background:#fff;border-radius:18px;padding:14px 20px;box-shadow:0 10px 24px rgba(0,0,0,.25)}.tg1 b{display:block;font:800 26px/1.3 Montserrat}.tg1 span{font:500 18px/1.4 Roboto;color:#55585d}
.gs1{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}.gq1{background:#fff;border-radius:18px;padding:14px 16px;display:flex;flex-direction:column;gap:4px;border:2px dashed #c9c5bd}
.gq1 span{font:500 15px/1.35 Roboto;color:#73767b}.gq1 b{font:800 34px/1.25 Montserrat;color:#9a9da2;text-decoration:line-through}.gq1.ok{background:#6f8f3d;border:0}.gq1.ok span{color:#e6f2d3}.gq1.ok b{color:#fff;text-decoration:none}""")

rows2 = "".join(f'<div class=or2><b>{o[0]}</b><span>{o[1]}<br><em>{o[2]} · {o[3]}</em></span><span>{fmt(o[4])}</span><span>× {RATE[o[2]]:g}</span><strong>{fmt(blocks(o)[1])}</strong></div>' for o in ORD7)
TOT = sum(blocks(o)[1] for o in ORD7)
P["p337_paver_s2"] = pv(2, "STEP 1 · SQ FT TO BLOCKS", "Every order counted<br><span>the same way.</span>",
f'''<div class=w2><div class="cd tb2"><div class="or2 hd2"><span>ORDER</span><span>SITE AND DESIGN</span><span>SQ FT</span><span>PER SQ FT</span><span>TO MAKE</span></div>{rows2}
<div class=tt2><span>Sample rates. 5% extra added for cuts at the edges.</span><b>{fmt(TOT)} blocks</b></div></div>
<div class=sw2>{"".join(f'<div class=sw><div class=sp2>{patch(240, 120, 60, c, i+3)}</div><b>{d}</b><span>{RATE[d]:g} per sq ft</span></div>' for i,(d,c) in enumerate([("Rectangle","red"),("Zigzag","grey"),("Square, 1 ft","moss")]))}</div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.or2{flex:1;display:grid;grid-template-columns:120px 1fr 90px 110px 110px;gap:10px;align-items:center;border-bottom:1px solid #ece9e3;font:500 21px/1.35 Roboto}
.or2 b{font:800 22px/1.3 Montserrat}.or2 em{font-style:normal;font-size:18px;color:#73767b}.or2 strong{font:800 30px/1.3 Montserrat;color:#b4532a;text-align:right}.or2>span:nth-child(3),.or2>span:nth-child(4){text-align:right}
.hd2{flex:none;padding-bottom:10px;border-bottom:2px solid #26282b;font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#73767b}.hd2 span:nth-child(n+3){text-align:right}
.tt2{display:flex;justify-content:space-between;align-items:center;gap:16px;background:#f3efe8;border-radius:14px;padding:12px 18px;margin-top:10px;font:500 17px/1.4 Roboto;color:#55585d}.tt2 b{font:800 28px/1.3 Montserrat;color:#26282b;white-space:nowrap}
.sw2{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.sw{background:#fff;border-radius:18px;padding:12px;display:flex;flex-direction:column;gap:4px}.sp2{height:90px;border-radius:10px;overflow:hidden}.sp2 .pt7{width:100%;height:100%;display:block}.sw b{font:800 19px/1.3 Montserrat;margin-top:4px}.sw span{font:500 16px/1.35 Roboto;color:#73767b}""")

PAL = [("P-01", "Rectangle red", 14, "Mon 9 Nov"), ("P-02", "Rectangle red", 13, "Tue 10 Nov"), ("P-03", "Zigzag grey", 11, "Thu 12 Nov"), ("P-04", "Zigzag grey", 10, "Fri 13 Nov"),
       ("P-05", "Square moss", 8, "Sun 15 Nov"), ("P-06", "Rectangle grey", 6, "Tue 17 Nov"), ("P-07", "Rectangle red", 3, "Fri 20 Nov"), ("P-08", "Rectangle red", 1, "Sun 22 Nov")]
P["p337_paver_s3"] = pv(3, "STEP 2 · CURING YARD", "Which pallets are ready<br><span>to load today?</span>",
f'''<div class=w3><div class="cd yd3">{"".join(f'<div class="pl3 {"rd" if d>=14 else ""}"><div class=rg3 style="--p:{min(d,14)/14*100:.0f}%"><div><b>{d}</b><span>of 14 days</span></div></div><strong>{p}</strong><span>{t}</span><em>Made {m}</em></div>' for p,t,d,m in PAL)}</div>
<div class=nb><span class=ib>{ic("check",26)}</span><span><b>P-01 is ready today</b>, Mon 23 Nov. P-02 is ready tomorrow. Sample: 14 days of curing before dispatch.</span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.yd3{flex:1;padding:18px;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:14px;background:#d9d5ce}
.pl3{background:repeating-linear-gradient(90deg,#c8a77a 0 22px,#b08e60 22px 26px);border-radius:16px;padding:14px 10px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;box-shadow:0 8px 16px rgba(0,0,0,.12)}
.rg3{width:132px;height:132px;border-radius:50%;background:conic-gradient(#6f8f3d var(--p),#eae6df 0);display:flex;align-items:center;justify-content:center;margin-bottom:4px}
.rg3>div{width:100px;height:100px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}.rg3 b{font:800 34px/1.2 Montserrat}.rg3 span{font:500 13px/1.3 Roboto;color:#73767b}
.pl3>strong{font:800 22px/1.3 Montserrat;color:#26282b;background:#fff;border-radius:8px;padding:0 10px}.pl3>span{font:700 18px/1.35 Roboto;color:#2d2416}.pl3>em{font:500 17px/1.35 Roboto;font-style:normal;color:#3e3322}
.pl3.rd .rg3 b{color:#6f8f3d}.pl3.rd{box-shadow:0 0 0 4px #6f8f3d,0 8px 16px rgba(0,0,0,.12)}""")

trips = []
left = b14; k = 1
while left > 0:
    q = min(TRIP, left); trips.append((f"Trip {k}", q)); left -= q; k += 1
def lorry(q):
    pct = q / TRIP
    s = '<svg viewBox="0 0 420 170" class=lr4><rect x="10" y="40" width="270" height="90" rx="6" fill="#eae6df" stroke="#26282b" stroke-width="4"/>'
    s += f'<rect x="14" y="{44+86*(1-pct):.0f}" width="262" height="{86*pct:.0f}" fill="#b4532a"/>'
    s += "".join(f'<line x1="{14+i*26}" y1="{44+86*(1-pct):.0f}" x2="{14+i*26}" y2="126" stroke="#9c4421" stroke-width="2"/>' for i in range(1, 11))
    s += '<path d="M290 130 L290 70 Q290 58 302 58 L350 58 L386 98 L386 130 Z" fill="#6f8f3d" stroke="#26282b" stroke-width="4"/><path d="M302 70 L344 70 L370 98 L302 98 Z" fill="#cfe6f5"/>'
    s += '<rect x="6" y="128" width="384" height="12" rx="4" fill="#26282b"/>'
    for x in (70, 130, 340): s += f'<circle cx="{x}" cy="146" r="20" fill="#26282b"/><circle cx="{x}" cy="146" r="8" fill="#9a9da2"/>'
    return s + "</svg>"
DT = ["Tue 24 Nov, 8 AM", "Tue 24 Nov, 2 PM"]
P["p337_paver_s4"] = pv(4, "STEP 3 · TRUCK TRIPS", f"{fmt(b14)} blocks,<br><span>{len(trips)} truck trips.</span>",
f'''<div class=w4>{"".join(f'<div class="cd tr4">{lorry(q)}<div class=ti4><b>{t}</b><span>{DT[i]}</span><strong>{fmt(q)} blocks</strong><em>{"Full load" if q==TRIP else f"{q/TRIP*100:.0f}% of a load"}</em></div></div>' for i,(t,q) in enumerate(trips))}
<div class="cd ms4"><small class=cap>MESSAGE TO THE CUSTOMER · {o14[0].upper()}</small><p>Your {fmt(b14)} red rectangle blocks come in {len(trips)} trips on Tuesday, 8 AM and 2 PM. Please keep the gate clear for unloading.</p></div>
<div class=nb><span class=ib>{ic("truck",26)}</span><span>Sample truck size: <b>{fmt(TRIP)} blocks a trip.</b> Trips are planned from the order, not guessed.</span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tr4{flex:1;display:flex;align-items:center;gap:24px;padding:14px 26px;min-height:0}.lr4{height:100%;max-height:250px;width:auto;flex:none}
.ti4{display:flex;flex-direction:column;gap:2px}.ti4 b{font:800 34px/1.3 Montserrat}.ti4 span{font:500 21px/1.4 Roboto;color:#55585d}.ti4 strong{font:800 32px/1.3 Montserrat;color:#b4532a}.ti4 em{font:600 19px/1.4 Roboto;font-style:normal;color:#6f8f3d}
.ms4{padding:16px 22px;display:flex;flex-direction:column;gap:6px}.ms4 p{font:500 22px/1.45 Roboto}""")

P["p337_paver_s5"] = pv(5, "YOUR TURN", "Make paver blocks?<br><span>Let's build your order app.</span>",
f'''<div class=w5><div class="cd c5">{patch(520, 620, 65, seed=11, mix=lambda r,c: ["red","grey","moss"][(r//3+c//3)%3])}</div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Sq ft to blocks","Same rate, every order"),("clock","Curing yard","Days done per pallet"),("truck","Truck trips","Planned from the order"),("send","Customer messages","Dates and gate notes")])}</div>
<div class=q>How do you count blocks for an order today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b4532a;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1.05fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{overflow:hidden;padding:0;min-height:0}.w5 .q{grid-column:1 / 3}.pt7{width:100%;height:100%;display:block}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(38,40,43,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#f6dfd2;color:#b4532a}.ti b{display:block;font:800 22px/1.4 Montserrat;margin-bottom:2px}.ti div span{font:500 17px/1.4 Roboto;color:#55585d}
.q{background:#26282b;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 Roboto}""")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
