import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 156 INDIA · Water tanker supplier · CAROUSEL 5 · Anton + DM Sans · steel blue / safety yellow / concrete
# New techniques: SVG side-view water tanker, trip lanes per tanker with status chips, statement cards by trip count (no amounts).
WT = """
body{--f:'DM Sans';--h:'Anton';background:#e7e9ea;color:#13314a}
h1{font-family:'Anton';font-weight:400;font-size:62px;letter-spacing:.3px;line-height:1.25;margin-top:22px} h1 span{color:#1f6fb2}
.sub{color:#4e6273;font-size:23px}
.kk{font:700 16px 'DM Sans';letter-spacing:3px;color:#b88a00;margin-top:22px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(19,49,74,.08)}
.dn{background:#1f6fb2;color:#fff}.ow{background:#ffc928;color:#13314a}.nx{background:#fff;color:#13314a;border:2px dashed #8aa0b2}
"""
def wt(n, head, vis, css="", cta="Swipe", ctacss="background:#13314a;color:#fff"):
    return page(WT + css, head, vis, "#13314a", cta, ctacss, tagline=f"{n} / 5")
tanker = '''<svg viewBox="0 0 760 300" width="100%" style="display:block">
<rect x="0" y="262" width="760" height="10" rx="5" fill="#c3c9cd"/>
<path d="M40 170 L40 110 Q40 96 54 96 L140 96 L175 150 L190 150 L190 240 L40 240 Z" fill="#1f6fb2"/>
<path d="M62 112 L130 112 L158 150 L62 150 Z" fill="#cfe6f7"/>
<rect x="200" y="78" width="520" height="150" rx="75" fill="#ffc928"/><rect x="200" y="78" width="520" height="150" rx="75" fill="none" stroke="#13314a" stroke-width="5"/>
<path d="M330 80 V226 M460 80 V226 M590 80 V226" stroke="#e0ac10" stroke-width="5"/>
<rect x="430" y="60" width="60" height="22" rx="6" fill="#13314a"/>
<rect x="190" y="226" width="540" height="18" rx="6" fill="#13314a"/><rect x="726" y="180" width="26" height="14" rx="4" fill="#13314a"/>
<text x="460" y="166" text-anchor="middle" font-family="Anton" font-size="40" fill="#13314a"><tspan>DRINKING WATER</tspan></text>
''' + "".join(f'<circle cx="{x}" cy="248" r="34" fill="#22262a"/><circle cx="{x}" cy="248" r="13" fill="#a9b2b8"/>' for x in [110, 520, 640]) + '</svg>'
P["p156_tank_s1"] = wt(1, "<div class=kk>WATER TANKER SUPPLIERS</div><h1>Tanker trips in a diary?<br><span>See every trip of the day.</span></h1>",
f'''<div class="cd hero">{tanker}<div class=lb>Sample tanker · 10,000 L</div><div class=sq2><small>TODAY'S 14 TRIPS</small><div>{"".join(f'<i class={k}></i>' for k in ["dn"]*9+["ow"]*2+["nx"]*3)}</div></div></div>
<div class=sr>{"".join(f'<div class="{k}"><b>{a}</b><span>{b}</span></div>' for a,b,k in [("14","trips today","t"),("9","delivered","dn"),("2","on the way","ow"),("3","to go","nx")])}</div>''',
css=""".vis{flex-direction:column;gap:18px}.hero{flex:1;display:flex;flex-direction:column;justify-content:center;gap:14px;padding:26px 30px}
.sq2 small{font:700 15px 'DM Sans';letter-spacing:2px;color:#8a9aa8}.sq2 div{display:flex;gap:8px;margin-top:10px}.sq2 i{flex:1;height:54px;border-radius:12px}.lb{align-self:flex-start;font:700 20px 'DM Sans';background:#e7e9ea;border-radius:12px;padding:8px 14px}
.sr{display:flex;gap:14px}.sr div{flex:1;border-radius:22px;padding:18px 20px}.sr .t{background:#13314a;color:#fff}
.sr b{display:block;font:400 52px/1.4 Anton;margin-bottom:6px}.sr span{font:600 19px 'DM Sans'}""")

ords = [("Sample Society A", "2 tankers daily", "6 AM – 8 AM", "Daily"), ("Sample Hotel", "1 tanker", "Every 2nd day", "Repeat"), ("Sample Site 4", "3 tankers", "Mon to Sat", "Repeat"),
        ("Sample House 12", "1 tanker", "Today, 4 PM", "One-time")]
P["p156_tank_s2"] = wt(2, "<div class=kk>PART 1 · ORDERS</div><h1>Repeat orders set once.<br><span>They show up every day.</span></h1>",
browser(f'''<div class=ol><div class=hd2><b>Orders</b><span class=nb2>+ New order</span></div>
{"".join(f'<div class=or><span class=ib>{ic("drop",26)}</span><div><b>{a}</b><span>{b} · {c}</span></div><em class="{"one" if d=="One-time" else ""}">{d}</em></div>' for a,b,c,d in ords)}
<div class=nf><b>New order · sample</b><div class=fr>{"".join(f'<div><small>{x}</small><span>{y}</span></div>' for x,y in [("Customer","Sample House 12"),("Quantity","10,000 L"),("Time","Today, 4 PM")])}</div></div></div>''', url="yourtankers.in/orders · sample", style="flex:1"),
css=""".vis{display:flex}.ol{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.hd2{display:flex;justify-content:space-between;align-items:center}.hd2 b{font:400 34px/1.35 Anton}.nb2{font:700 18px 'DM Sans';background:#13314a;color:#fff;border-radius:12px;padding:10px 16px}
.or{flex:1;display:flex;align-items:center;gap:16px;background:#f1f3f4;border-radius:18px;padding:0 18px}
.or .ib{width:54px;height:54px;border-radius:16px;background:#1f6fb2;color:#fff}.or div{flex:1}.or b{display:block;font:700 24px 'DM Sans'}.or span{font:500 19px 'DM Sans';color:#4e6273}
.or em{font-style:normal;font:700 17px 'DM Sans';background:#ffc928;border-radius:12px;padding:8px 14px}.or em.one{background:#dfe5ea}
.nf{background:#13314a;color:#fff;border-radius:18px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}.nf>b{font:700 20px 'DM Sans'}
.fr{display:flex;gap:10px}.fr div{flex:1;background:rgba(255,255,255,.1);border-radius:12px;padding:10px 12px}.fr small{display:block;font:700 13px 'DM Sans';letter-spacing:1.5px;color:#9fb6c8}.fr span{font:600 19px 'DM Sans'}""")

lanes = [("Tanker 1", "Driver 1", [("6 AM", "Society A", "dn"), ("8 AM", "Site 4", "dn"), ("10 AM", "Hotel", "dn"), ("1 PM", "Site 4", "ow"), ("4 PM", "House 12", "nx")]),
         ("Tanker 2", "Driver 2", [("6 AM", "Society A", "dn"), ("8 AM", "Site 4", "dn"), ("11 AM", "Site 4", "dn"), ("1 PM", "Sample Shop", "ow"), ("4 PM", "Society B", "nx")]),
         ("Tanker 3", "Driver 3", [("7 AM", "Society B", "dn"), ("9 AM", "Sample Mall", "dn"), ("12 PM", "Society C", "dn"), ("3 PM", "Sample Lab", "nx")])]
P["p156_tank_s3"] = wt(3, "<div class=kk>PART 2 · TRIP BOARD</div><h1>Which tanker is where?<br><span>One board for all trips.</span></h1>",
f'''<div class="cd tb">{"".join(f'<div class=ln><div class=th><b>{a}</b><span>{d}</span></div><div class=tc>' + "".join(f'<div class="tp {k}"><small>{t}</small><b>{p}</b></div>' for t,p,k in T) + '</div></div>' for a,d,T in lanes)}</div>
<div class=lg3>{"".join(f'<span><i class={k}></i>{t}</span>' for k,t in [("dn","Delivered · 9"),("ow","On the way · 2"),("nx","To go · 3")])}</div>''',
css=""".vis{flex-direction:column;gap:14px}.tb{flex:1;padding:12px 22px;display:flex;flex-direction:column}
.ln{flex:1;display:flex;flex-direction:column;justify-content:center;gap:10px;border-bottom:1.5px solid #e7e9ea}.ln:last-child{border-bottom:none}
.th{display:flex;align-items:baseline;gap:12px}.th b{font:400 30px/1.35 Anton}.th span{font:600 18px 'DM Sans';color:#4e6273}
.tc{display:flex;gap:10px}.tp{flex:0 0 172px;border-radius:16px;padding:18px 14px}.tp small{display:block;font:700 17px 'DM Sans';opacity:.85}.tp b{font:700 22px/1.3 'DM Sans'}
.lg3{display:flex;gap:26px;font:600 20px 'DM Sans'}.lg3 span{display:flex;gap:10px;align-items:center}.lg3 i{width:26px;height:26px;border-radius:8px}""")

st = [("Sample Society A", "60 trips", "Bill sent 1 Dec", "Paid", "pd"), ("Sample Site 4", "75 trips", "Bill sent 1 Dec", "Due", "du"), ("Sample Hotel", "15 trips", "Bill sent 1 Dec", "Paid", "pd"),
      ("Sample Society B", "30 trips", "Bill sent 1 Dec", "Reminder sent", "rm")]
P["p156_tank_s4"] = wt(4, "<div class=kk>PART 3 · MONTH-END</div><h1>Trips counted for you.<br><span>Bills go out on the 1st.</span></h1>",
f'''<div class=gd2>{"".join(f'<div class=sc2><small>NOVEMBER · SAMPLE</small><b>{a}</b><div class=tn>{t}</div><span>{s}</span><em class={k}>{p}</em></div>' for a,t,s,p,k in st)}</div>
<div class=nt2>{ic("check",24,w=3)}<span>Every trip is counted from the board, so no more arguing over the diary.</span></div>''',
css=""".vis{flex-direction:column;gap:16px}.gd2{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.sc2{background:#fff;border-radius:24px;padding:22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(19,49,74,.08)}
.sc2 small{font:700 15px 'DM Sans';letter-spacing:2px;color:#8a9aa8}.sc2>b{font:700 30px/1.3 'DM Sans'}
.tn{font:400 92px/1.35 Anton;color:#1f6fb2;margin-top:auto}.sc2>span{font:500 18px 'DM Sans';color:#4e6273}
.sc2 em{align-self:flex-start;font-style:normal;font:700 17px 'DM Sans';border-radius:12px;padding:8px 14px;margin-top:6px}.pd{background:#d8f1e1;color:#1d6b3c}.du{background:#ffe2dc;color:#a8321c}.rm{background:#fff0bf;color:#6b5200}
.nt2{background:#13314a;color:#fff;border-radius:20px;padding:18px 22px;display:flex;gap:14px;align-items:center;font:600 21px/1.4 'DM Sans'}""")

P["p156_tank_s5"] = wt(5, "<div class=kk>YOUR TURN</div><h1>Supply water by tanker?<br><span>Let's build your trip app.</span></h1>",
f'''<div class="cd hero2">{tanker}</div><div class=rw3>{"".join(f'<div><span class=ib>{ic(i,28)}</span><b>{a}</b></div>' for i,a in [("doc","Repeat orders"),("truck","Trip board"),("phone","Driver app"),("file","Month-end bills")])}</div>''',
css=""".vis{flex-direction:column;gap:18px}.hero2{flex:1;display:flex;align-items:center;padding:30px}
.rw3{display:grid;grid-template-columns:1fr 1fr;gap:14px}.rw3 div{background:#13314a;color:#fff;border-radius:22px;padding:28px 22px;display:flex;align-items:center;gap:16px}
.rw3 .ib{width:58px;height:58px;border-radius:16px;background:#ffc928;color:#13314a}.rw3 b{font:700 30px 'DM Sans'}""",
cta="DM us to start", ctacss="background:#ffc928;color:#13314a")


# ───────── 157 INDIA · Bridal wear rental · SINGLE · Gelasio + Poppins · wine / gold foil / ivory
# New technique: clothes rail with SVG gown silhouettes + hang tags, and a per-outfit month calendar with booked, fitting and cleaning days.
def gown(c, w=150):
    return (f'<svg viewBox="0 0 120 260" width="{w}" style="display:block"><path d="M60 4 Q70 4 70 14 Q70 20 60 22 L60 30" fill="none" stroke="#7a6a50" stroke-width="3"/>'
            f'<path d="M14 40 L60 28 L106 40" fill="none" stroke="#7a6a50" stroke-width="4"/>'
            f'<path d="M42 38 L78 38 L84 96 L118 250 L2 250 L36 96 Z" fill="{c}"/><path d="M36 96 L84 96" stroke="#e9c46a" stroke-width="6"/>'
            f'<path d="M14 236 L106 236" stroke="#e9c46a" stroke-width="5" stroke-dasharray="6 6"/></svg>')
outfits = [("L-07", "#2f6b5a", ""), ("L-12", "#8e1b3a", "on"), ("S-03", "#c9874a", "")]
book = {**{d: "b" for d in [4, 5, 6, 12, 13, 14, 26, 27, 28]}, **{d: "f" for d in [3, 11, 25]}, **{d: "c" for d in [7, 15, 29]}}
cells = [""] + [str(d) for d in range(1, 32)] + [""] * 3
P["p157_bridal"] = page("""
body{--f:'Poppins';--h:'Gelasio';background:#fbf6ec;color:#3b1424}
h1{font-family:'Gelasio';font-size:60px;font-weight:700;letter-spacing:-.3px;line-height:1.22} h1 span{color:#8e1b3a}
.vis{gap:20px}
.rl{width:400px;flex:none;background:#f1e6d2;border-radius:28px;padding:18px 14px;display:flex;flex-direction:column}
.rod{height:12px;border-radius:6px;background:linear-gradient(#b89b5e,#8a7140);margin:6px 10px 0}
.gs{flex:none;display:flex;justify-content:space-around;align-items:flex-start}
.gw{display:flex;flex-direction:column;align-items:center;gap:8px;padding:0 4px 10px;border-radius:18px}
.gw.on{background:#fff;box-shadow:0 0 0 3px #8e1b3a}
.gw em{font-style:normal;font:700 17px Poppins;background:#fffaf0;border:2px solid #b89b5e;border-radius:8px;padding:4px 10px}
.oc{flex:1;background:#fff;border-radius:20px;margin:12px 6px;padding:14px 16px;display:flex;flex-direction:column}.oc small{font:700 13px Poppins;letter-spacing:2px;color:#a08a7a}.orow{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid #f1e6d2;font:500 20px Poppins}.orow b{font:700 22px Poppins}.rl .cap{font:600 16px/1.4 Poppins;color:#6b4a3a;text-align:center;padding:0 10px}
.cl{flex:1;background:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(59,20,36,.08)}
.cl small{font:700 13px Poppins;letter-spacing:2.5px;color:#a08a7a}.cl h3{font:700 30px/1.3 Gelasio}
.gr{flex:1;display:grid;grid-template-columns:repeat(7,1fr);gap:6px}
.gr span{display:flex;align-items:center;justify-content:center;font:600 19px Poppins;border-radius:12px}
.gr .wd{font:700 13px Poppins;color:#a08a7a}.gr .b{background:#8e1b3a;color:#fff}.gr .f{background:#f6d77a}.gr .c{background:#e4ecf3;color:#4a6378}
.lg{display:flex;gap:14px;flex-wrap:wrap;font:600 15px Poppins}.lg span{display:flex;gap:6px;align-items:center}.lg i{width:18px;height:18px;border-radius:5px}
.fr2{background:#3b1424;color:#fff;border-radius:16px;padding:14px 16px;font:500 18px/1.4 Poppins}.fr2 b{color:#f6d77a}
""", "<h1>Same outfit, two brides,<br>one date?<br><span>Block dates per outfit.</span></h1>",
f'''<div class=rl><div class=rod></div><div class=gs>{"".join(f'<div class="gw {k}">{gown(c,112)}<em>{n}</em></div>' for n,c,k in outfits)}</div><div class=oc><small>L-12 · SAMPLE</small>{"".join(f'<div class=orow><span>{a}</span><b>{b}</b></div>' for a,b in [("Size","Fits 32 to 36"),("Bookings in Dec","3"),("Fittings in Dec","3"),("Photos","8 on the website")])}</div><div class=cap>Every outfit has a code, photos and its own calendar</div></div>
<div class=cl><small>OUTFIT L-12 · DECEMBER 2026</small><h3>Wine bridal lehenga</h3><div class=gr>{"".join(f'<span class=wd>{d}</span>' for d in "MTWTFSS")}{"".join(f'<span class="{book.get(int(c),"") if c else ""}">{c}</span>' for c in cells)}</div>
<div class=lg><span><i style="background:#8e1b3a"></i>Booked</span><span><i style="background:#f6d77a"></i>Fitting</span><span><i style="background:#e4ecf3"></i>Cleaning</span></div>
<div class=fr2>Customers see <b>only free dates</b> on your website. Fitting and cleaning days block on their own.</div></div>''',
"#3b1424", "Rent bridal wear? DM us", "background:#8e1b3a;color:#fff")


# ───────── 158 CANADA · Ski / snowboard rental · SINGLE · Montserrat + Roboto · glacier white / ski red / pine
# New technique: rack of skis drawn as tall rounded bars with length labels; reserved skis carry a name tag.
skis = [(150, ""), (155, "r"), (160, ""), (165, "me"), (165, "r"), (170, ""), (175, "r"), (180, "")]
P["p158_ski"] = page("""
body{--f:'Roboto';--h:'Montserrat';background:#eef4f7;color:#173a2e}
.mt{position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(170deg,#dbe8ee,#c9dbe3)}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#d7263d}
.sub{color:#4f6a60}
.vis{gap:20px}
.rk{flex:1;background:#173a2e;border-radius:28px;padding:22px 20px 18px;display:flex;flex-direction:column;gap:12px}
.rk .bar{height:14px;border-radius:7px;background:#6d8c7f}
.sk{flex:1;display:flex;justify-content:space-between;align-items:stretch;padding:0 6px}
.ski{width:46px;border-radius:23px 23px 10px 10px;background:linear-gradient(90deg,#f4f7f9,#d6e0e6);display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:14px 0 12px;position:relative}
.ski.r{background:linear-gradient(90deg,#9aa9b1,#7d8d96)}.ski.me{background:linear-gradient(90deg,#ff5a6e,#d7263d)}
.ski b{font:800 16px Montserrat;color:#173a2e;writing-mode:vertical-rl;transform:rotate(180deg)}.ski.me b{color:#fff}
.ski i{width:30px;height:46px;border-radius:8px;background:rgba(23,58,46,.25)}
.rk .lg{display:flex;gap:18px;font:600 17px Roboto;color:#dfeae5}.rk .lg span{display:flex;gap:8px;align-items:center}.rk .lg i{width:18px;height:18px;border-radius:5px}
.rv{width:420px;flex:none;background:#fff;border-radius:28px;padding:22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(23,58,46,.10)}
.rv small{font:700 13px Roboto;letter-spacing:2.5px;color:#8aa096}.rv h3{font:800 28px/1.25 Montserrat}
.rv .f{flex:1;background:#eef4f7;border-radius:14px;padding:0 16px;display:flex;flex-direction:column;justify-content:center}
.rv .f span{font:600 16px Roboto;color:#6c8479;letter-spacing:1px}.rv .f b{font:700 28px Roboto}
.rv .ok{background:#e4f3ea;color:#1d6b3c;border-radius:14px;padding:12px 14px;font:600 17px/1.4 Roboto}
.rv .bt{background:#d7263d;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 19px Montserrat}
""", "<h1>Long line at the rental desk?<br><span>Let skiers reserve<br>gear online.</span></h1><div class=sub>Sized from their height and boot size, ready at pickup.</div>",
f'''<div class=rk><div class=bar></div><div class=sk>{"".join(f'<div class="ski {k}"><b>{l} cm</b><i></i></div>' for l,k in skis)}</div>
<div class=lg><span><i style="background:#eef4f7"></i>Free</span><span><i style="background:#8a99a2"></i>Reserved</span><span><i style="background:#d7263d"></i>This booking</span></div></div>
<div class=rv><small>RESERVATION · SAMPLE</small><h3>Ski set for Sample Guest</h3>{"".join(f'<div class=f><span>{a}</span><b>{b}</b></div>' for a,b in [("HEIGHT","5 ft 8 in"),("BOOT SIZE","US 9"),("SKI LENGTH","165 cm"),("PICKUP","Sat, Dec 19 · 8:30 AM")])}
<div class=ok>Set is tagged and waiting at Counter 2.</div><div class=bt>Reserve gear</div></div>''',
"#173a2e", "Rent ski gear? DM us", "background:#d7263d;color:#fff", bg="<div class=mt></div>")


# ───────── 159 INDIA · Generator rental · SINGLE · Archivo Black + Inter · forest green / amber / charcoal
# New technique: SVG generator set with a digital hour meter readout + site table with service-due bars.
genset = '''<svg viewBox="0 0 420 300" width="100%" style="display:block">
<rect x="20" y="250" width="380" height="20" rx="6" fill="#2b2f2c"/><rect x="40" y="60" width="340" height="190" rx="18" fill="#2f6b4a"/>
''' + "".join(f'<rect x="{x}" y="90" width="12" height="130" rx="6" fill="#245a3d"/>' for x in range(70, 210, 26)) + '''
<rect x="230" y="84" width="128" height="140" rx="12" fill="#1f2421"/>
<rect x="244" y="100" width="100" height="40" rx="6" fill="#0d110f"/><text x="294" y="128" text-anchor="middle" font-family="Inter" font-weight="800" font-size="20" fill="#ffb52e"><tspan>1248.6 h</tspan></text>
<circle cx="266" cy="176" r="16" fill="#ffb52e"/><circle cx="322" cy="176" r="16" fill="#d64b3b"/><rect x="250" y="204" width="88" height="10" rx="5" fill="#3d4440"/>
<rect x="310" y="30" width="22" height="34" rx="4" fill="#3d4440"/></svg>'''
sites = [("Sample Site 1", "62.5 kVA", "Since 2 Nov", 64, 120, 210, 250), ("Sample Event Lawn", "125 kVA", "Since 20 Nov", 22, 60, 236, 250), ("Sample Factory", "82.5 kVA", "Since 12 Oct", 71, 140, 242, 250)]
P["p159_gen"] = page("""
body{--f:'Inter';--h:'Archivo Black';background:#f1efe8;color:#1f2421}
h1{font-family:'Archivo Black';font-weight:400;font-size:54px;letter-spacing:0;line-height:1.28} h1 span{color:#2f6b4a}
.vis{flex-direction:column;gap:16px}
.tp{display:flex;gap:16px}
.gs{width:470px;flex:none;background:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:8px}
.gs small{font:700 13px Inter;letter-spacing:2.5px;color:#8a8f88}.gs b{font:400 24px/1.35 'Archivo Black'}
.kp{flex:1;display:flex;flex-direction:column;gap:12px}
.k{flex:1;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;justify-content:center}
.k b{font:400 40px/1.35 'Archivo Black'}.k span{font:600 18px/1.35 Inter}
.k1{background:#2f6b4a;color:#fff}.k1 span{color:#d3e6da}.k2{background:#ffb52e;color:#1f2421}.k3{background:#1f2421;color:#fff}.k3 span{color:#c9cec8}
.tb{flex:1;background:#fff;border-radius:26px;padding:12px 22px;display:flex;flex-direction:column}
.tr{flex:1;display:grid;grid-template-columns:1.3fr .8fr .8fr 1.2fr;align-items:center;gap:10px;border-bottom:1.5px solid #ece9df}.tr:last-child{border-bottom:none}
.th{flex:none;height:44px;font:700 13px Inter;letter-spacing:1.5px;color:#8a8f88}
.tr b{display:block;font:700 21px Inter}.tr span{font:500 16px Inter;color:#6a7069}.tr .v{font:700 22px Inter}
.sv span{display:block;font:600 15px Inter;color:#6a7069;margin-bottom:6px}.sv .br{height:14px;border-radius:7px;background:#ece9df;overflow:hidden}.sv .br i{display:block;height:100%;border-radius:7px}
""", "<h1>How long did the genset<br>run at the site?<br><span>Log hours and diesel daily.</span></h1>",
f'''<div class=tp><div class=gs><small>GENSET G-04 · 62.5 KVA · SAMPLE</small>{genset}<b>Hour meter: 1248.6 h</b></div>
<div class=kp><div class="k k1"><b>64 h</b><span>run this week at Sample Site 1</span></div><div class="k k2"><b>120 L</b><span>diesel added this week</span></div><div class="k k3"><b>40 h</b><span>left before the next service</span></div></div></div>
<div class=tb><div class="tr th"><span>SITE · SAMPLE</span><span>HOURS / WK</span><span>DIESEL / WK</span><span>NEXT SERVICE</span></div>
{"".join(f'<div class=tr><div><b>{a}</b><span>{k} · {d}</span></div><span class=v>{h} h</span><span class=v>{l} L</span><div class=sv><span>{s} of {m} h</span><div class=br><i style="width:{s*100//m}%;background:{"#d64b3b" if m-s<15 else "#ffb52e" if m-s<45 else "#2f6b4a"}"></i></div></div></div>' for a,k,d,h,l,s,m in sites)}</div>''',
"#1f2421", "Rent out gensets? DM us", "background:#2f6b4a;color:#fff")


# ───────── 160 INDIA · Spoken English institute (adults) · CAROUSEL 5 · TeX Gyre Adventor + DM Sans · chalk navy / coral / paper
# New technique: level staircase (4 steps) with student counts + "ready to move up" flags.
SE = """
body{--f:'DM Sans';--h:'TeX Gyre Adventor';background:#fbf8f2;color:#1c2541}
h1{font-family:'TeX Gyre Adventor';font-size:58px;font-weight:700;letter-spacing:-.8px;line-height:1.22;margin-top:22px} h1 span{color:#e4572e}
.sub{color:#5b6179;font-size:23px}
.kk{font:700 16px 'DM Sans';letter-spacing:3px;color:#e4572e;margin-top:22px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(28,37,65,.07)}
"""
def se(n, head, vis, css="", cta="Swipe", ctacss="background:#1c2541;color:#fff"):
    return page(SE + css, head, vis, "#1c2541", cta, ctacss, tagline=f"{n} / 5")
lv = [("Level 1", "Basic words", 18, 4), ("Level 2", "Daily talk", 22, 6), ("Level 3", "Office talk", 14, 3), ("Level 4", "Interview ready", 8, 0)]
P["p160_eng_s1"] = se(1, "<div class=kk>SPOKEN ENGLISH CLASSES · ADULTS</div><h1>Who is ready for the next level?<br><span>See it on one screen.</span></h1>",
f'''<div class="cd stp">{"".join(f'<div class=sp style="height:{38+i*20}%"><div class=tx><small>{a}</small><b>{b}</b><span>{c} students</span></div>' + (f'<em>{r} ready to move up</em>' if r else '<em class=top>Top level</em>') + '</div>' for i,(a,b,c,r) in enumerate(lv))}</div>
<div class=sm3><div><b>62</b><span>adult students · sample</span></div><div class=hi><b>13</b><span>ready for a level test this month</span></div></div>''',
css=""".vis{flex-direction:column;gap:16px}.stp{flex:1;display:flex;align-items:flex-end;gap:14px;padding:22px 22px 0;min-height:0}
.sp{flex:1;background:#1c2541;border-radius:20px 20px 0 0;padding:18px 16px;display:flex;flex-direction:column;justify-content:space-between;color:#fff}
.sp small{font:700 14px 'DM Sans';letter-spacing:2px;color:#ffb39c}.sp b{display:block;font:700 27px/1.3 'TeX Gyre Adventor';margin:4px 0}.sp span{font:500 19px 'DM Sans';color:#c8cde0}
.sp em{font-style:normal;font:700 16px/1.35 'DM Sans';background:#e4572e;border-radius:12px;padding:8px 10px}.sp em.top{background:#3a4670}
.sm3{display:flex;gap:14px}.sm3 div{flex:1;background:#fff;border-radius:22px;padding:14px 22px;display:flex;align-items:center;gap:16px;box-shadow:0 14px 30px rgba(28,37,65,.07)}
.sm3 b{font:700 46px/1.3 'TeX Gyre Adventor'}.sm3 span{font:500 19px/1.4 'DM Sans';color:#5b6179}.sm3 .hi{background:#e4572e;color:#fff}.sm3 .hi span{color:#fff}""")

random.seed(160)
bt = [("Morning · 7 AM", "Level 1", 12), ("Afternoon · 2 PM", "Level 2", 11), ("Evening · 7 PM", "Level 2", 11), ("Weekend · Sat 10 AM", "Level 3", 9)]
pat = ["101111011111", "111111111101", "110101111001", "111111111111"]
P["p160_eng_s2"] = se(2, "<div class=kk>PART 1 · BATCHES + ATTENDANCE</div><h1>Spot who is skipping<br><span>before they drop out.</span></h1>",
f'''<div class="cd at">{"".join(f'<div class=br2><div class=bh><b>{a}</b><span>{l} · {n} students</span></div><div class=dts>' + "".join(f'<i class="{"on" if c=="1" else ""}"></i>' for c in p) + f'</div><em style="{"color:#e4572e" if "00" in p else ""}">{p.count("1")} of 12{"<br><small style=\'font:700 14px DM Sans\'>2 missed in a row</small>" if "00" in p else ""}</em></div>' for (a,l,n),p in zip(bt,pat))}
<div class=cap2>Last 12 classes for one sample student per batch · each dot is one class</div></div>
<div class=al>{ic("bell",26)}<span>Missed 2 classes in a row? The student gets a kind “We missed you” message and a recap of the class.</span></div>''',
css=""".vis{flex-direction:column;gap:16px}.at{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.br2{flex:1;display:flex;align-items:center;gap:18px;border-bottom:1.5px solid #efeadf}
.bh{width:260px;flex:none}.bh b{display:block;font:700 25px/1.3 'TeX Gyre Adventor'}.bh span{font:500 17px 'DM Sans';color:#5b6179}
.dts{flex:1;display:flex;gap:8px}.dts i{width:30px;height:30px;border-radius:8px;background:#f6d3c7}.dts i.on{background:#1c2541}
.br2 em{font-style:normal;font:700 21px/1.4 'DM Sans';width:150px;text-align:right}
.cap2{flex:none;padding-top:12px;font:600 16px 'DM Sans';color:#8b90a6}
.al{background:#1c2541;color:#fff;border-radius:20px;padding:18px 22px;display:flex;gap:14px;align-items:center;font:500 20px/1.45 'DM Sans'}""")

sc = [("Speaking", 78), ("Listening", 84), ("Reading", 72), ("Writing", 66)]
P["p160_eng_s3"] = se(3, "<div class=kk>PART 2 · LEVEL TEST</div><h1>A clear score card<br><span>after every level test.</span></h1>",
f'''<div class="cd rc2"><div class=rh2><div class=av2>S</div><div><small>SAMPLE STUDENT · LEVEL 2</small><b>Level test · Sat, 28 Nov</b></div></div>
{"".join(f'<div class=sk2><div class=lb2><b>{a}</b><span>{v} / 100</span></div><div class=bb><i style="width:{v}%"></i></div></div>' for a,v in sc)}
<div class=res><b>Moves up to Level 3 · Office talk</b><span>Next batch starts Mon, 7 Dec · Weekend batch also open</span></div></div>
<div class=sd2><div class=tip><small>WORK ON NEXT</small><b>Writing short emails</b><span>3 practice tasks added to the app</span></div><div class=tip><small>TEACHER NOTE · SAMPLE</small><b>“Speaks with more confidence now.”</b><span>Shared with the student</span></div></div>''',
css=""".vis{gap:18px}.rc2{flex:1;padding:24px;display:flex;flex-direction:column;gap:14px}
.rh2{display:flex;gap:16px;align-items:center}.av2{width:72px;height:72px;border-radius:50%;background:#e4572e;color:#fff;font:700 28px/72px 'TeX Gyre Adventor';text-align:center;flex:none}
.rh2 small{font:700 13px 'DM Sans';letter-spacing:2px;color:#8b90a6}.rh2 b{display:block;font:700 28px/1.3 'TeX Gyre Adventor'}
.sk2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px}.lb2{display:flex;justify-content:space-between}.lb2 b{font:700 22px 'DM Sans'}.lb2 span{font:700 22px 'DM Sans';color:#e4572e}
.bb{height:20px;border-radius:10px;background:#efeadf;overflow:hidden}.bb i{display:block;height:100%;background:#1c2541;border-radius:10px}
.res{background:#1c2541;color:#fff;border-radius:18px;padding:16px 18px}.res b{display:block;font:700 23px/1.3 'TeX Gyre Adventor'}.res span{font:500 17px 'DM Sans';color:#c8cde0}
.sd2{width:330px;flex:none;display:flex;flex-direction:column;gap:14px}
.tip{flex:1;background:#fff;border-radius:22px;padding:20px;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:8px solid #e4572e;box-shadow:0 14px 30px rgba(28,37,65,.07)}
.tip small{font:700 13px 'DM Sans';letter-spacing:2px;color:#8b90a6}.tip b{font:700 25px/1.3 'TeX Gyre Adventor'}.tip span{font:500 18px 'DM Sans';color:#5b6179}""")

P["p160_eng_s4"] = se(4, "<div class=kk>PART 3 · PRACTICE APP</div><h1>Five minutes of practice<br><span>on the phone every day.</span></h1>",
f'''<div class=lf3>{"".join(f'<div class=ft3><span class=ib>{ic(i,28)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("chat","Word of the day","With an example sentence."),("phone","Record and listen","Speak a line, hear it back."),("bell","Class reminder","An hour before every class."),("check","Practice streak","Days in a row, shown simply.")])}</div>
{phone('<div class=ap3><small>TODAY · SAMPLE</small><b class=t>Hi, Sample Student</b><div class=wd2><small>WORD OF THE DAY</small><b>Schedule</b><span>“Can we schedule the call for Monday?”</span></div><div class=rc3><span class=mic>' + ic("phone",22) + '</span><div><b>Say it out loud</b><span>Tap to record</span></div></div><div class=cr3><small>NEXT CLASS</small><b>Level 3 · Mon, 7 Dec · 7 PM</b></div><div class=stk><b>6 days</b><span>practice streak</span></div></div>', w=380, h=770)}''',
css=""".vis{gap:24px;align-items:center}.lf3{flex:1;display:flex;flex-direction:column;gap:14px;align-self:stretch}
.ft3{flex:1;background:#fff;border-radius:22px;padding:16px 20px;display:flex;gap:16px;align-items:center;box-shadow:0 10px 24px rgba(28,37,65,.06)}
.ft3 .ib{width:58px;height:58px;border-radius:16px;background:#1c2541;color:#fff}.ft3 b{display:block;font:700 26px/1.3 'TeX Gyre Adventor'}.ft3 span{font:500 20px/1.4 'DM Sans';color:#5b6179}
.ap3{flex:1;padding:8px 16px 16px;display:flex;flex-direction:column;gap:10px;background:#fbf8f2}
.ap3 small{font:700 12px 'DM Sans';letter-spacing:2px;color:#8b90a6}.ap3 .t{font:700 22px 'TeX Gyre Adventor'}
.wd2{flex:1;background:#1c2541;color:#fff;border-radius:18px;padding:16px;display:flex;flex-direction:column;justify-content:center;gap:6px}.wd2 small{color:#ffb39c}.wd2 b{font:700 32px 'TeX Gyre Adventor'}.wd2 span{font:500 16px/1.4 'DM Sans';color:#dfe3f0}
.rc3{background:#fff;border-radius:16px;padding:12px;display:flex;gap:12px;align-items:center}.mic{width:46px;height:46px;border-radius:50%;background:#e4572e;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.rc3 b{display:block;font:700 16px 'DM Sans'}.rc3 span{font:500 14px 'DM Sans';color:#5b6179}
.cr3{background:#fff;border-radius:16px;padding:12px}.cr3 b{display:block;font:700 16px 'DM Sans'}
.stk{background:#ffe3d9;border-radius:16px;padding:12px;display:flex;gap:10px;align-items:baseline}.stk b{font:700 24px 'TeX Gyre Adventor';color:#c2421d}.stk span{font:600 15px 'DM Sans';color:#7a2a12}""")

P["p160_eng_s5"] = se(5, "<div class=kk>YOUR TURN</div><h1>Teach spoken English?<br><span>Let's build your<br>institute app.</span></h1>",
f'''<div class=st5>{"".join(f'<div class=s5 style="height:{40+i*20}%"><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate([("Levels","Who moves up"),("Attendance","Who is skipping"),("Score cards","After every test"),("Practice app","Every day")]))}</div>''',
css=""".vis{flex-direction:column}.st5{flex:1;display:flex;align-items:flex-end;gap:14px;min-height:0}
.s5{flex:1;background:#1c2541;color:#fff;border-radius:22px 22px 0 0;padding:22px 18px;display:flex;flex-direction:column;gap:6px}
.s5:last-child{background:#e4572e}.s5 b{font:700 32px/1.3 'TeX Gyre Adventor'}.s5 span{font:500 22px/1.4 'DM Sans';color:#dfe3f0}.s5:last-child span{color:#fff}""",
cta="DM us to start", ctacss="background:#e4572e;color:#fff")

if __name__ == "__main__":
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
