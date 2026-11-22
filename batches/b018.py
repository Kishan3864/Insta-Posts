import sys; sys.path.insert(0, "tools/postkit"); from lib import *
import random
P = {}

# ───────── 106 INDIA · Spices / masala manufacturer · SINGLE · Anton + DM Sans · paprika red / cardamom green / cream paper
# New technique: trace-flow diagram (batch → cartons → distributors → shops) with an SVG curve layer under HTML nodes,
# plus SVG spice heaps with grain speckle.
random.seed(106)
def heap(cx, col, dot, label, batch):
    sp = "".join(f'<circle cx="{cx-70+random.random()*140:.0f}" cy="{150-random.random()*60:.0f}" r="{1.5+random.random()*1.5:.1f}" fill="{dot}"/>' for _ in range(60))
    return (f'<ellipse cx="{cx}" cy="172" rx="104" ry="22" fill="#c9c3b6"/><ellipse cx="{cx}" cy="166" rx="96" ry="18" fill="#e4dfd4"/>'
            f'<path d="M{cx-86} 166 Q{cx-40} 70 {cx} 64 Q{cx+40} 70 {cx+86} 166 Z" fill="{col}"/>{sp}'
            f'<rect x="{cx-62}" y="194" width="124" height="54" rx="10" fill="#fffaf0"/>'
            f'<text x="{cx}" y="217" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#2b1d16">{label}</text>'
            f'<text x="{cx}" y="239" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="15" fill="#a33a24">{batch}</text>')
heaps = ('<svg viewBox="0 0 900 256" width="900" height="256">'
         + heap(115, "#b8321f", "#7d1d10", "Chilli", "B-2611") + heap(335, "#e2a72e", "#b07812", "Turmeric", "B-2612")
         + heap(555, "#8c7a3c", "#5e5122", "Coriander", "B-2608") + heap(775, "#6b3d26", "#3d2014", "Garam masala", "B-2605") + '</svg>')
dist = [("Sample Distributor 1", "Rajkot · 40 cartons", "18 shops", 16), ("Sample Distributor 2", "Ahmedabad · 50 cartons", "24 shops", 50), ("Sample Distributor 3", "Surat · 30 cartons", "11 shops", 84)]
curves = "".join(f'<path d="M49.4 50 C 53.5 50, 52.5 {y}, 56.7 {y}" fill="none" stroke="#a33a24" stroke-width="3" vector-effect="non-scaling-stroke"/>' for *_, y in dist)
P["p106_spice"] = page("""
body{--f:'DM Sans';--h:'Anton';background:#f4ecdc;color:#2b1d16}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#a33a24}
.vis{flex-direction:column;gap:16px}
.hp{flex:none;background:#3f5a3a;border-radius:28px;padding:18px 0 10px;display:flex;justify-content:center}
.hp svg{display:block}
.fl{flex:1;background:#fffaf0;border-radius:28px;position:relative;box-shadow:0 14px 30px rgba(43,29,22,.08)}
.fl>svg{position:absolute;left:0;top:0;width:100%;height:100%}
.fl small{position:absolute;left:24px;top:18px;font:700 13px 'DM Sans';letter-spacing:3px;color:#97897a}
.nd{position:absolute;transform:translateY(-50%);border-radius:18px;padding:14px 18px;display:flex;flex-direction:column;gap:4px}
.nd b{font:400 30px/1.35 Anton;letter-spacing:.3px}.nd span{font:500 17px/1.35 'DM Sans'}
.n1{left:24px;top:50%;width:270px;background:#a33a24;color:#fff}.n1 span{color:#f6d9cf}
.n2{left:330px;top:50%;width:140px;background:#3f5a3a;color:#fff;align-items:center;text-align:center}.n2 span{color:#d6e2cf}
.n3{left:540px;width:388px;background:#f4ecdc;flex-direction:row;align-items:center;gap:12px;padding:12px 16px}
.n3 div{flex:1;display:flex;flex-direction:column;gap:2px}.n3 b{font:700 21px/1.3 'DM Sans'}.n3 span{color:#6f6253}
.n3 em{font-style:normal;font:700 16px 'DM Sans';background:#2b1d16;color:#f4ecdc;padding:6px 10px;border-radius:8px;white-space:nowrap}
""", "<h1>A shop complains about<br>one packet?<br><span>Find the batch and every<br>shop it went to.</span></h1>",
f'''<div class=hp>{heaps}</div>
<div class=fl><svg viewBox="0 0 100 100" preserveAspectRatio="none"><path d="M30.9 50 H34.7" stroke="#a33a24" stroke-width="3" vector-effect="non-scaling-stroke"/>{curves}</svg><small>BATCH TRACE · SAMPLE</small>
<div class="nd n1"><span>Chilli powder · 200 g</span><b>Batch B-2611</b><span>Packed 18 Nov · Line 2<br>Best before May 2027</span></div>
<div class="nd n2"><b>120</b><span>cartons</span></div>
{"".join(f'<div class="nd n3" style="top:{y}%"><div><b>{a}</b><span>{b}</span></div><em>{c}</em></div>' for a,b,c,y in dist)}</div>''',
"#2b1d16", "Masala maker? DM us", "background:#a33a24;color:#fff")

# ───────── 108 INDIA · Mini-truck / tempo booking · SINGLE · Poppins + Roboto · jade / tangerine / asphalt
# New technique: SVG city map with river, road grid, dashed route and pins, floating booking card; SVG vehicle size picker.
mapsvg = '''<svg viewBox="0 0 952 470" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">
<rect width="952" height="470" fill="#dfe9e4"/>
<path d="M0 360 C 200 330, 330 420, 520 380 S 820 300, 952 330 V 470 H 0 Z" fill="#b9d8e6"/>
<g fill="#cfe0c8"><rect x="40" y="40" width="160" height="110" rx="10"/><rect x="700" y="60" width="200" height="120" rx="10"/><rect x="420" y="190" width="120" height="90" rx="10"/></g>
<g stroke="#fff" stroke-width="16" fill="none"><path d="M0 190 H952"/><path d="M0 300 H600"/><path d="M260 0 V340"/><path d="M620 0 V360"/><path d="M820 0 V320"/><path d="M90 190 V470"/></g>
<path d="M600 300 L 760 240 L952 240" stroke="#fff" stroke-width="16" fill="none"/>
<path d="M260 380 L 330 330" stroke="#fff" stroke-width="14"/>
<path d="M150 300 H260 V190 H620 V110 H820" stroke="#f08a24" stroke-width="7" fill="none" stroke-dasharray="4 14" stroke-linecap="round"/>
<g><circle cx="150" cy="300" r="20" fill="#1f6f5c"/><circle cx="150" cy="300" r="8" fill="#fff"/></g>
<g><path d="M820 110 m0 0 c-26 -30 -22 -62 0 -62 c22 0 26 32 0 62 z" fill="#f08a24"/><circle cx="820" cy="68" r="9" fill="#fff"/></g>
<g transform="translate(470 172)"><rect x="-26" y="-14" width="52" height="28" rx="6" fill="#1d2a2f"/><rect x="10" y="-10" width="14" height="12" rx="2" fill="#9fd3c4"/></g>
<text x="176" y="338" font-family="Poppins" font-weight="700" font-size="22" fill="#1f6f5c">Pickup</text>
<text x="700" y="44" font-family="Poppins" font-weight="700" font-size="22" fill="#b85d0d">Drop</text>
</svg>'''
def tempo(w, body, label, cap, on=False):
    return f'''<div class="vc {"on" if on else ""}"><svg viewBox="0 0 220 100" width="200" height="91">
<rect x="{150-body}" y="22" width="{body}" height="52" rx="5" fill="{"#f08a24" if on else "#c7d3cf"}"/>
<path d="M152 36 H186 L206 56 V74 H152 Z" fill="#1d2a2f"/><path d="M160 42 H182 L196 56 H160 Z" fill="#9fd3c4"/>
<circle cx="{150-body+26}" cy="78" r="13" fill="#1d2a2f"/><circle cx="182" cy="78" r="13" fill="#1d2a2f"/>
<circle cx="{150-body+26}" cy="78" r="5" fill="#c7d3cf"/><circle cx="182" cy="78" r="5" fill="#c7d3cf"/></svg><b>{label}</b><span>{cap}</span></div>'''
P["p108_tempo"] = page("""
body{--f:'Roboto';--h:'Poppins';background:#1d2a2f;color:#eef4f1}
h1{font-family:'Poppins';font-size:60px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#f08a24}
.sub{color:#a9bcb5}
.vis{flex-direction:column;gap:16px}
.mp{flex:1;border-radius:28px;overflow:hidden;position:relative;min-height:0}
.mp>svg{position:absolute;inset:0}
.bk{position:absolute;right:22px;bottom:22px;width:400px;background:#fff;color:#1d2a2f;border-radius:20px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 18px 40px rgba(0,0,0,.25)}
.bk small{font:700 13px Roboto;letter-spacing:3px;color:#7e908a}
.bk b{font:800 26px/1.3 Poppins}
.bk .r{display:flex;justify-content:space-between;font:500 18px Roboto;color:#5b6d67;border-top:1.5px solid #edf2f0;padding-top:6px}
.bk .r em{font-style:normal;font-weight:700;color:#1d2a2f}
.bk .st{background:#1f6f5c;color:#fff;border-radius:12px;padding:10px 14px;font:700 18px Roboto;margin-top:4px}
.vs{flex:none;display:flex;gap:14px}
.vc{flex:1;background:#26373d;border-radius:20px;padding:12px 16px 16px;display:flex;flex-direction:column;align-items:center;gap:4px;border:3px solid transparent}
.vc svg{display:block}
.vc b{font:700 22px Poppins}.vc span{font:500 17px Roboto;color:#a9bcb5}
.vc.on{border-color:#f08a24;background:#2f4148}
""", "<h1>Load bookings on calls<br>all day long?<br><span>Let customers book a<br>tempo online.</span></h1>",
f'''<div class=mp>{mapsvg}<div class=bk><small>BOOKING BK-552 · SAMPLE</small><b>Shop goods · 600 kg</b>
<div class=r><span>Vehicle</span><em>Tempo · up to 1 ton</em></div><div class=r><span>When</span><em>Mon 23 Nov, 10:30 am</em></div><div class=r><span>Helpers</span><em>1 loader</em></div>
<div class=st>Driver 3 allotted · reaching pickup</div></div></div>
<div class=vs>{tempo(1,70,"Tempo","Up to 1 ton",True)}{tempo(1,95,"Pickup","Up to 1.5 tons")}{tempo(1,128,"Truck, 14 ft","Up to 4 tons")}</div>''',
"#eef4f1", "Tempo or truck owner? DM us", "background:#f08a24;color:#1d2a2f")

# ───────── 110 CANADA · Hair salon · SINGLE · Crimson Text + Montserrat · espresso / peach / sage
# New technique: multi-column day calendar (one column per stylist) with blocks sized by duration and dashed open slots.
hours = ["10", "11", "12", "1", "2", "3", "4", "5"]
cols = [("Stylist 1", [(0, 1, "Cut", "c"), (1, 2.5, "Colour", "k"), (4, 1, "Open slot", "o"), (5, 1, "Cut", "c"), (6, 1.5, "Blowout", "b")]),
        ("Stylist 2", [(0, 1.5, "Blowout", "b"), (2, 1, "Open slot", "o"), (3, 3, "Colour + cut", "k"), (6.5, 1, "Open slot", "o")]),
        ("Stylist 3", [(0.5, 1, "Cut", "c"), (2, 1.5, "Open slot", "o"), (4, 1, "Cut", "c"), (5, 2, "Highlights", "k")])]
H = 74
P["p110_salon"] = page("""
body{--f:'Montserrat';--h:'Crimson Text';background:#2f231d;color:#f6e9df}
h1{font-family:'Crimson Text';font-size:70px;font-weight:700;letter-spacing:-.5px;line-height:1.2} h1 span{color:#f2a98a}
.sub{color:#c9b6a8}
.vis{gap:18px}
.cal{flex:1;display:flex;flex-direction:column;padding:14px 18px 16px;background:#fffaf6;color:#2f231d;gap:10px}
.cal .t{display:flex;justify-content:space-between;align-items:baseline}.cal h3{font:700 30px/1.25 'Crimson Text'}
.cal small{font:700 12px Montserrat;letter-spacing:3px;color:#a08c7e}
.gr{flex:1;display:flex;gap:8px}
.tm{width:40px;flex:none;display:flex;flex-direction:column;padding-top:34px}
.tm span{height:%dpx;font:600 14px Montserrat;color:#a08c7e}
.cl{flex:1;display:flex;flex-direction:column;gap:6px}
.cl b{font:700 15px Montserrat;text-align:center;background:#f3e6dc;border-radius:8px;padding:5px 0}
.tr{position:relative;height:%dpx;background:repeating-linear-gradient(#efe3d9 0 1.5px,transparent 1.5px %dpx)}
.ap{position:absolute;left:3px;right:3px;border-radius:10px;padding:6px 8px;font:700 15px/1.3 Montserrat;overflow:hidden}
.ap.c{background:#c9d8c0;color:#2f4a2a}.ap.k{background:#f2a98a;color:#5a2a14}.ap.b{background:#e9d6f0;color:#4c2a5a}
.ap.o{background:#fff;border:2.5px dashed #7a9c6e;color:#4e6e43;display:flex;align-items:center;justify-content:center}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.sc{flex:1;background:#3d2f27;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.sc i{width:46px;height:46px;border-radius:12px;background:#f2a98a;color:#2f231d;display:flex;align-items:center;justify-content:center}
.sc b{font:700 30px/1.2 'Crimson Text'}.sc span{font:500 17px/1.4 Montserrat;color:#c9b6a8}
.lgn{flex:none;display:flex;gap:6px;flex-wrap:wrap}.lgn em{font-style:normal;font:600 13px Montserrat;padding:4px 8px;border-radius:6px}
""" % (H, H*8, H), "<h1>Gaps in the book,<br>but the phone keeps ringing?<br><span>Show open slots online.</span></h1>",
browser(f'''<div class=cal><div class=t><h3>Tuesday · 3 stylists</h3><small>SAMPLE</small></div>
<div class=gr><div class=tm>{"".join(f'<span>{h}</span>' for h in hours)}</div>
{"".join(f'<div class=cl><b>{n}</b><div class=tr>' + "".join(f'<div class="ap {k}" style="top:{s*H+2}px;height:{d*H-4}px">{"+ " if k=="o" else ""}{t}</div>' for s,d,t,k in aps) + '</div></div>' for n,aps in cols)}</div>
<div class=lgn><em style="background:#c9d8c0">Cut</em><em style="background:#f2a98a">Colour</em><em style="background:#e9d6f0">Blowout</em><em style="border:2px dashed #7a9c6e">Open, book online</em></div></div>''', "book.yoursalon.ca · sample", "flex:1") +
f'''<div class=sd>{"".join(f'<div class=sc><i>{ic(a,26)}</i><b>{b}</b><span>{c}</span></div>' for a,b,c in [("cal","Clients pick an open slot","Any time, even after hours."),("bell","Reminder the day before","Fewer no-shows."),("users","Right stylist, right time","Colour gets a long slot, a cut a short one.")])}</div>''',
"#f6e9df", "Salon owner? DM us", "background:#f2a98a;color:#2f231d")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
