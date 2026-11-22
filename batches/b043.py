import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 231 INDIA · Scented candle maker · CAROUSEL 5 · Gelasio + Inter · wax beige / charcoal / lavender
# New techniques: drawn candle jars with wax fill + flame, 7-day cure strip, curing rack where shelf = pour day and badge = days left.
SC = {"Lavender": "#a58bd6", "Vanilla": "#f1dcae", "Coffee": "#8a5a3c", "Lemongrass": "#c9d66b", "Sandalwood": "#c99b6b"}
def jar(scent, w=120, lit=False, lab=True, fill=0.78):
    c = SC[scent]; h = w * 1.15
    s = f'<svg viewBox="0 0 100 130" width="{w}" height="{h:.0f}">'
    if lit: s += '<path d="M50 4 C58 16 58 24 50 30 C42 24 42 16 50 4 Z" fill="#ffb347"/><path d="M50 13 C54 19 54 24 50 27 C46 24 46 19 50 13 Z" fill="#fff3c4"/>'
    s += '<rect x="48.5" y="28" width="3" height="16" fill="#2b2b2b"/>'
    s += f'<rect x="12" y="{44+ (1-fill)*70:.0f}" width="76" height="{fill*70+12:.0f}" rx="6" fill="{c}"/>'
    s += '<rect x="10" y="36" width="80" height="92" rx="12" fill="#ffffff" fill-opacity=".28" stroke="#2f2a33" stroke-width="3"/><rect x="18" y="42" width="8" height="70" rx="4" fill="#fff" fill-opacity=".55"/>'
    if lab: s += f'<rect x="17" y="78" width="66" height="30" rx="4" fill="#fffaf0" stroke="#2f2a33" stroke-width="1.5"/><text x="50" y="97" text-anchor="middle" font-family="Gelasio" font-weight="700" font-size="10.5" fill="#2f2a33"><tspan>{scent[:9]}</tspan></text>'
    return s + '</svg>'
CB = """
body{--f:'Inter';--h:'Gelasio';background:#f3ece0;color:#2f2a33}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#7a5cc0;margin-top:22px;align-self:flex-start}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#7a5cc0}
.cd{background:#fffaf2;border-radius:24px;box-shadow:0 12px 28px rgba(47,42,51,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#8a7f73}
.nb{display:flex;align-items:center;gap:14px;background:#2f2a33;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Inter}.nb .ib{width:50px;height:50px;border-radius:14px;background:#a58bd6;color:#2f2a33}.nb b{color:#d6c6ff}
"""
def cb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2f2a33;color:#fff"):
    return page(CB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2f2a33", cta, ctacss, tagline=f"{n} / 5")
P["p231_candle_s1"] = cb(1, "SCENTED CANDLE MAKER · BATCHES", "A customer loved one candle.<br><span>Which batch was it?</span>",
f'''<div class=w1><div class="cd hj"><small class=cap>THE CANDLE THEY WANT AGAIN · SAMPLE</small>{jar("Lavender", 330, lit=True)}<div class=qq>“Same one as last month, please!”</div></div>
<div class=nbk><small class=cap>YOUR NOTEBOOK TODAY</small>
<p>Lavender — big jars, <s>6%</s> 8%?</p><p>Wick: the thick one... or medium?</p><p>Poured on Tuesday, I think</p><p>Ready by... next week?</p><p>Gift shop wants 12, cafe wants coffee</p></div></div>''',
css=""".w1{flex:1;display:flex;gap:16px;min-height:0}.hj{width:440px;flex:none;padding:20px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}.hj svg{display:block}
.qq{background:#2f2a33;color:#fff;border-radius:18px 18px 18px 6px;padding:14px 18px;font:600 22px/1.4 Inter;align-self:stretch}
.nbk{flex:1;min-width:0;background:#fffdf6;border-radius:12px;padding:20px 24px 10px 54px;box-shadow:0 14px 30px rgba(47,42,51,.12);position:relative;display:flex;flex-direction:column;background-image:linear-gradient(90deg,transparent 38px,#f0a3a3 38px 40px,transparent 40px)}
.nbk p{flex:1;display:flex;align-items:center;border-bottom:2px solid #d8e3ef;font:italic 400 27px/1.35 Gelasio;color:#4a4050}.nbk s{color:#c0392b}.nbk small{padding-bottom:6px}""")

P["p231_candle_s2"] = cb(2, "STEP 1 · A CARD FOR EVERY BATCH", "One batch card.<br><span>Every detail, saved.</span>",
f'''<div class=w2><div class="cd bc"><div class=bh><div><small class=cap>BATCH · SAMPLE</small><b>B-231 · Lavender</b></div>{jar("Lavender", 130)}</div>
<div class=kv>{"".join(f'<div><small class=cap>{a}</small><b>{b}</b></div>' for a,b in [("JAR SIZE","200 g"),("JARS","20"),("WAX","Soy, 4 kg"),("FRAGRANCE","8%"),("WICK","Cotton, M"),("POURED","23 Nov")])}</div>
<div class=cu><small class=cap>CURING · 7 DAYS · READY MON 30 NOV</small><div class=dd>{"".join(f'<span class="{"dn" if i<5 else ""}"><b>{d}</b>{n}</span>' for i,(d,n) in enumerate([("Mon","23"),("Tue","24"),("Wed","25"),("Thu","26"),("Fri","27"),("Sat","28"),("Sun","29")]))}<span class=rd><b>Mon</b>30</span></div></div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>Next time someone asks for <b>“the same one”</b>, open B-231 and pour it again.</span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.bc{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:14px}
.bh{display:flex;justify-content:space-between;align-items:center}.bh b{display:block;font:700 42px/1.3 Gelasio}.bh svg{display:block}
.kv{flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}.kv div{background:#f3ece0;border-radius:16px;padding:14px 22px;display:flex;flex-direction:column;justify-content:center}.kv small{font-size:16px}.kv b{font:700 42px/1.35 Gelasio}
.cu{display:flex;flex-direction:column;gap:8px}.dd{display:grid;grid-template-columns:repeat(8,1fr);gap:6px}
.dd span{border-radius:12px;background:#ece5f8;padding:8px 0;text-align:center;font:700 22px/1.3 Inter;color:#4a4050}.dd b{display:block;font:600 14px/1.4 Inter;color:#8a7f73}
.dd .dn{background:#a58bd6;color:#fff}.dd .dn b{color:#efe7ff}.dd .rd{background:#2f2a33;color:#fff}.dd .rd b{color:#d6c6ff}""")

rack = [("Poured Mon 23 Nov", "Lavender", "B-231 · 20 jars, 200 g", 2, "Ready Mon 30 Nov"), ("Poured Wed 25 Nov", "Vanilla", "B-232 · 30 jars, 100 g", 4, "Ready Wed 2 Dec"), ("Poured Fri 27 Nov", "Coffee", "B-233 · 12 jars, 200 g", 6, "Ready Fri 4 Dec")]
shelves = "".join(f'''<div class=sh><div class=shl><small class=cap>{p.upper()}</small><b>{b}</b><span>{r}</span></div><div class=jj>{"".join(jar(sc, 96 if "200" in b else 80, lab=False) for _ in range(5))}</div><div class=dl><b>{d}</b><span>days left</span></div></div>''' for p, sc, b, d, r in rack)
P["p231_candle_s3"] = cb(3, "STEP 2 · CURING RACK · TODAY SAT 28 NOV", "See what is curing<br><span>and when it is ready.</span>",
f'''<div class=w3><div class="cd rk">{shelves}</div>
<div class=nb><span class=ib>{ic("clock",26)}</span><span>No more opening every box to check. <b>Ready dates come from the pour date.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rk{flex:1;padding:14px 20px;display:flex;flex-direction:column;gap:10px}
.sh{flex:1;display:flex;align-items:flex-end;gap:16px;border-bottom:14px solid #b08a5f;border-radius:0 0 4px 4px;padding:0 4px 4px}
.shl{width:250px;flex:none;align-self:center}.shl b{display:block;font:700 21px/1.35 Gelasio;margin:2px 0}.shl span{font:600 17px Inter;color:#7a5cc0}
.jj{flex:1;display:flex;justify-content:space-between;align-items:flex-end}.jj svg{display:block}
.dl{width:104px;flex:none;align-self:center;background:#2f2a33;color:#fff;border-radius:18px;padding:10px 0;text-align:center}.dl b{display:block;font:700 44px/1.3 Gelasio;color:#d6c6ff}.dl span{font:600 14px Inter}""")

ords = [("Sample Gift Shop", "12 × Lavender 200 g", "B-231", "Ships Mon 30 Nov"), ("Sample customer", "4 × Lavender 200 g", "B-231", "Ships Mon 30 Nov"), ("Website order", "2 × Vanilla 100 g", "B-232", "Ships Wed 2 Dec"), ("Sample Cafe", "6 × Coffee 200 g", "B-233", "Ships Fri 4 Dec")]
P["p231_candle_s4"] = cb(4, "STEP 3 · ORDERS MATCHED TO BATCHES", "Every order knows<br><span>its batch and ship date.</span>",
f'''<div class=w4><div class="cd ol"><small class=cap>ORDERS THIS WEEK · SAMPLE</small>{"".join(f'<div class=or><div><b>{a}</b><span>{b}</span></div><em>{c}</em><i>{d}</i></div>' for a,b,c,d in ords)}</div>
<div class=sx><div><b>16 of 20</b><span>Lavender jars already booked</span></div><div><b>4</b><span>Lavender jars free to sell</span></div><div><b>28 of 30</b><span>Vanilla jars still free</span></div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ol{flex:1;padding:18px 24px;display:flex;flex-direction:column;gap:6px}
.or{flex:1;display:grid;grid-template-columns:1fr 110px 190px;gap:14px;align-items:center;border-top:1px solid #ece4d6}
.or b{display:block;font:700 32px/1.3 Gelasio}.or span{font:500 22px/1.35 Inter;color:#6a6070}
.or em{font:800 20px Inter;font-style:normal;background:#ece5f8;color:#7a5cc0;border-radius:12px;padding:8px 0;text-align:center}.or i{font:700 20px Inter;font-style:normal;text-align:right}
.sx{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.sx div{background:#2f2a33;color:#fff;border-radius:20px;padding:14px 18px}
.sx b{display:block;font:700 36px/1.35 Gelasio;color:#d6c6ff}.sx span{font:500 18px/1.35 Inter}""")

P["p231_candle_s5"] = cb(5, "YOUR TURN", "Make candles at home<br><span>or in a small studio?</span>",
f'''<div class=w5><div class="cd jr5">{jar("Coffee", 230)}{jar("Lavender", 320, lit=True)}{jar("Vanilla", 230)}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,40)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Batch cards","Wax, wick, scent, dates"),("clock","Curing rack","Ready dates by batch"),("cart","Orders by batch","Ship dates you can keep"),("tag","Batch labels","Number on every jar")])}</div>
<div class=q>We can build a simple app for your batches and orders. Tell us how you track them today.</div></div>''',
cta="DM us to start", ctacss="background:#7a5cc0;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.jr5{flex:1;display:flex;justify-content:center;align-items:flex-end;gap:30px;padding:22px}.jr5 svg{display:block}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fffaf2;border-radius:22px;padding:24px 22px;box-shadow:0 10px 22px rgba(47,42,51,.07)}
.ti .ib{width:76px;height:76px;border-radius:20px;background:#ece5f8;color:#7a5cc0}.ti b{display:block;font:700 34px/1.3 Gelasio}.ti span{font:500 20px/1.35 Inter;color:#6a6070}
.q{background:#7a5cc0;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Inter}""")

# ───────── 232 USA · Appliance installer · SINGLE · Archivo Black + Inter · appliance white / steel teal / tangerine
# New technique: measured laundry-nook elevation (dimension lines in SVG) beside an install job card with a haul-away list.
nook = '''<svg viewBox="0 0 440 560" class=nk><rect x="0" y="0" width="440" height="560" fill="#eef3f3"/><rect x="0" y="470" width="440" height="90" fill="#cfd8d8"/>
<rect x="70" y="40" width="300" height="70" rx="6" fill="#d9e2e2" stroke="#1f3b40" stroke-width="4"/><line x1="220" y1="40" x2="220" y2="110" stroke="#1f3b40" stroke-width="3"/>
<rect x="96" y="210" width="248" height="260" rx="14" fill="#ffffff" stroke="#1f3b40" stroke-width="5"/><rect x="96" y="210" width="248" height="46" rx="10" fill="#e5ecec" stroke="#1f3b40" stroke-width="4"/>
<circle cx="130" cy="233" r="9" fill="#ff8a3d"/><rect x="160" y="226" width="70" height="14" rx="5" fill="#1f3b40"/><circle cx="220" cy="356" r="76" fill="#d6e3e5" stroke="#1f3b40" stroke-width="6"/><circle cx="220" cy="356" r="50" fill="#9fc3c8" stroke="#1f3b40" stroke-width="4"/>
<path d="M380 130 L380 470" stroke="#1f3b40" stroke-width="3"/><path d="M372 140 L380 126 L388 140 M372 460 L380 474 L388 460" fill="none" stroke="#1f3b40" stroke-width="3"/>
<rect x="388" y="276" width="46" height="70" rx="8" fill="#ff8a3d"/><text x="411" y="318" text-anchor="middle" font-family="Inter" font-weight="800" font-size="18" fill="#fff"><tspan>44"</tspan></text>
<path d="M70 500 L370 500" stroke="#1f3b40" stroke-width="3"/><path d="M84 492 L70 500 L84 508 M356 492 L370 500 L356 508" fill="none" stroke="#1f3b40" stroke-width="3"/>
<rect x="180" y="482" width="80" height="36" rx="8" fill="#ff8a3d"/><text x="220" y="507" text-anchor="middle" font-family="Inter" font-weight="800" font-size="18" fill="#fff"><tspan>29"</tspan></text>
<rect x="30" y="150" width="28" height="40" rx="5" fill="#2f8f9d"/><rect x="34" y="160" width="20" height="8" fill="#fff"/><text x="44" y="210" text-anchor="middle" font-family="Inter" font-weight="700" font-size="13" fill="#1f3b40"><tspan>Water</tspan></text>
<circle cx="400" cy="70" r="22" fill="none" stroke="#1f3b40" stroke-width="5"/><text x="400" y="112" text-anchor="middle" font-family="Inter" font-weight="700" font-size="13" fill="#1f3b40"><tspan>Vent</tspan></text></svg>'''
chk = [("Opening measured", "29 in wide, 44 in tall", True), ("Water hookup", "Hot and cold valves OK", True), ("Stairs", "Basement, 12 steps", True), ("New hoses", "Bring 2", True)]
P["p232_installer"] = page("""
body{--f:'Inter';--h:'Archivo Black';background:#e9f1f1;color:#1f3b40}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#e0661c;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:60px;letter-spacing:-1px;line-height:1.22} h1 span{color:#2f8f9d}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.nc{width:430px;flex:none;background:#fff;border-radius:26px;padding:16px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(31,59,64,.08)}
.nc>small,.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#6b8286}
.nk{width:100%;flex:1;min-height:0;display:block;border-radius:16px}
.nf{background:#fff1e6;border-radius:14px;padding:10px 14px;font:600 18px/1.4 Inter;color:#b14b0f}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:14px}
.jc{flex:1;background:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(31,59,64,.08)}
.jc h4{font:400 28px/1.35 'Archivo Black'}
.ck{flex:1;display:flex;align-items:center;gap:14px;border-top:1px solid #e6eeee}.ck i{width:34px;height:34px;border-radius:50%;background:#2f8f9d;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.ck b{display:block;font:700 25px/1.3 Inter}.ck span{font:500 20px/1.35 Inter;color:#5d7377}
.ha{background:#1f3b40;color:#fff;border-radius:24px;padding:16px 22px;display:flex;flex-direction:column;gap:10px}
.ha small{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#ffb27a}
.hr{display:flex;align-items:center;gap:12px;font:600 20px/1.35 Inter}.hr .ib{width:42px;height:42px;border-radius:12px;background:#ff8a3d;color:#1f3b40}.hr em{margin-left:auto;font:700 15px Inter;font-style:normal;background:#2f5a61;padding:6px 12px;border-radius:10px}
.sl{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.sl span{background:#fff;border-radius:14px;padding:10px 0;text-align:center;font:700 18px Inter;color:#1f3b40}.sl .on{background:#ff8a3d;color:#fff}
""", "<div class=kk>APPLIANCE INSTALLATION · BOOKING</div><h1>“Will it fit?”<br><span>Ask before install day.</span></h1>",
f'''<div class=vw><div class=nc><small>JOB A-232 · LAUNDRY NOOK · SAMPLE PHOTO FORM</small>{nook}<div class=nf>Customer sent a photo and 2 numbers before booking.</div></div>
<div class=rc><div class=jc><small class=cap>INSTALL CHECKLIST · NEW WASHER</small><h4>Sample home, Unit 4</h4>{"".join(f'<div class=ck><i>{ic("check",18,w=3)}</i><div><b>{a}</b><span>{b}</span></div></div>' for a,b,_ in chk)}</div>
<div class=ha><small>HAUL-AWAY LIST · SAMPLE</small><div class=hr><span class=ib>{ic("truck",22)}</span>Old washer<em>Take away</em></div><div class=hr><span class=ib>{ic("box",22)}</span>Packing and pallet<em>Take away</em></div>
<div class=sl><span>Tue 8 AM</span><span class=on>Tue 11 AM</span><span>Wed 2 PM</span></div></div></div></div>''',
"#1f3b40", "Install appliances? DM us", "background:#2f8f9d;color:#fff")

# ───────── 233 INDIA · Office stationery supplier · SINGLE · Bitter + Roboto · notebook blue / highlighter yellow / white
# New technique: clipboard with a metal clip holding a repeat order list with drawn stationery items and last vs this month quantities.
def item(k):
    d = {"pen": '<rect x="8" y="20" width="44" height="22" rx="3" fill="#2f5fb3"/><rect x="12" y="14" width="6" height="26" rx="2" fill="#111"/><rect x="22" y="12" width="6" height="28" rx="2" fill="#c62828"/><rect x="32" y="14" width="6" height="26" rx="2" fill="#1565c0"/>',
         "ream": '<rect x="6" y="18" width="48" height="26" rx="2" fill="#fff" stroke="#2d3a55" stroke-width="2"/><rect x="6" y="18" width="48" height="10" fill="#f5d000"/><line x1="10" y1="36" x2="50" y2="36" stroke="#c9d1e0" stroke-width="2"/>',
         "file": '<path d="M10 16 h16 l4 5 h20 v26 h-40z" fill="#4c8ce0" stroke="#2d3a55" stroke-width="2"/>',
         "marker": '<rect x="10" y="24" width="38" height="12" rx="5" fill="#f5d000" stroke="#2d3a55" stroke-width="2"/><path d="M48 26 l8 4 l-8 4z" fill="#2d3a55"/>',
         "tape": '<circle cx="30" cy="30" r="16" fill="#e8d9b0" stroke="#2d3a55" stroke-width="2"/><circle cx="30" cy="30" r="7" fill="#fff" stroke="#2d3a55" stroke-width="2"/>',
         "pins": '<rect x="10" y="20" width="40" height="22" rx="3" fill="#90a4ae" stroke="#2d3a55" stroke-width="2"/><line x1="16" y1="26" x2="44" y2="26" stroke="#fff" stroke-width="2"/><line x1="16" y1="32" x2="44" y2="32" stroke="#fff" stroke-width="2"/>'}
    return f'<svg viewBox="0 0 60 60" width="58" height="58">{d[k]}</svg>'
lst = [("pen", "Ball pens, box of 10", "6", "6"), ("ream", "A4 paper, 500 sheets", "10", "12"), ("file", "Box files", "8", "8"), ("marker", "Highlighters", "12", "12"), ("tape", "Clear tape rolls", "6", "4"), ("pins", "Stapler pins, packs", "5", "5")]
P["p233_stationery"] = page("""
body{--f:'Roboto';--h:'Bitter';background:#dfe8f6;color:#1d2b4c}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#2f5fb3;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:0;line-height:1.22} h1 span{background:linear-gradient(transparent 58%,#f5e04a 58%)}
.vw{flex:1;display:flex;gap:18px;min-height:0}
.cb{flex:1;min-width:0;background:#b98b57;border-radius:22px;padding:44px 18px 18px;position:relative;display:flex}
.clip{position:absolute;top:-14px;left:50%;transform:translateX(-50%);width:170px;height:52px;border-radius:12px;background:linear-gradient(#e3e7ee,#9aa3b2);border:3px solid #6b7486}
.sht{flex:1;background:#fff;border-radius:6px;padding:16px 20px;display:flex;flex-direction:column;box-shadow:0 8px 18px rgba(0,0,0,.15)}
.sh{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:8px;border-bottom:3px solid #1d2b4c}.sh b{display:block;font:800 28px/1.3 Bitter}.sh small,.cap{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#6a7690}
.ch{display:grid;grid-template-columns:58px 1fr 64px 64px;gap:10px;padding:8px 0 2px;font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#6a7690}
.it{flex:1;display:grid;grid-template-columns:58px 1fr 64px 64px;gap:10px;align-items:center;border-bottom:1px solid #e4e9f2}.it svg{display:block}
.it b{font:600 23px/1.3 Roboto}.it span{font:600 22px Roboto;color:#6a7690;text-align:center}.it em{font:800 22px Roboto;font-style:normal;text-align:center;border-radius:10px;padding:6px 0;background:#eef3fb}
.it em.up{background:#f5e04a}.it em.dn{background:#ffe0d6;color:#c0392b}
.rc{width:330px;flex:none;display:flex;flex-direction:column;gap:14px}
.dv{flex:1;background:#1d2b4c;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.dv small{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#f5e04a}
.dr{flex:1;display:flex;flex-direction:column;justify-content:center;border-top:1px solid #33456e}.dr b{font:700 24px/1.35 Bitter;color:#f5e04a}.dr span{font:500 22px/1.35 Roboto}
.ok{background:#fff;border-radius:24px;padding:16px 20px;font:500 20px/1.4 Roboto}.ok b{display:block;font:800 24px/1.35 Bitter;margin-bottom:4px}
""", "<div class=kk>OFFICE STATIONERY SUPPLY · MONTHLY ORDERS</div><h1>Office orders on calls?<br><span>Send one repeat list.</span></h1>",
f'''<div class=vw><div class=cb><div class="clip free"></div><div class=sht><div class=sh><div><small>SAMPLE OFFICE · DECEMBER LIST</small><b>Repeat order</b></div><small>EDIT, THEN CONFIRM</small></div>
<div class=ch><span></span><span>ITEM</span><span style="text-align:center">NOV</span><span style="text-align:center">DEC</span></div>
{"".join(f'<div class=it>{item(k)}<b>{a}</b><span>{n}</span><em class="{"up" if int(d)>int(n) else ("dn" if int(d)<int(n) else "")}">{d}</em></div>' for k,a,n,d in lst)}</div></div>
<div class=rc><div class=dv><small>DELIVERY DAYS · SAMPLE</small>{"".join(f'<div class=dr><b>{a}</b><span>{b}</span></div>' for a,b in [("Tue 1 Dec","Sample Office, Sample Clinic Desk"),("Thu 3 Dec","Sample Firm, 2nd floor"),("Sat 5 Dec","Sample Studio")])}</div>
<div class=ok><b>2 changes this month</b>A4 paper up to 12, tape down to 4. The bill follows the list.</div></div></div>''',
"#1d2b4c", "Supply offices? DM us", "background:#2f5fb3;color:#fff")

# ───────── 234 USA · Estate sale company · CAROUSEL 5 · Lora + DM Sans · dusty rose / oak / navy
# New techniques: room scene with numbered lot tags, lot catalogue grid, top-down house map with lot ranges per room + checkout path.
EB = """
body{--f:'DM Sans';--h:'Lora';background:#f6ebe8;color:#1f2a44}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b5656b;margin-top:22px;align-self:flex-start}
h1{font-family:'Lora';font-weight:700;font-size:64px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b5656b}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(31,42,68,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7d7a86}
.nb{display:flex;align-items:center;gap:14px;background:#1f2a44;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e3a7a9;color:#1f2a44}.nb b{color:#f4c6c8}
.lt{font:800 15px 'DM Sans';background:#1f2a44;color:#fff;border-radius:8px;padding:4px 8px}
"""
def eb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f2a44;color:#fff"):
    return page(EB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f2a44", cta, ctacss, tagline=f"{n} / 5")
ICO = {"Armchair": '<path d="M14 30 q0-14 16-14 h20 q16 0 16 14 v10 h-52z" fill="#b5656b"/><rect x="8" y="34" width="12" height="22" rx="4" fill="#9a4f55"/><rect x="60" y="34" width="12" height="22" rx="4" fill="#9a4f55"/><rect x="18" y="40" width="44" height="14" rx="3" fill="#c97c82"/><rect x="14" y="56" width="4" height="10" fill="#6b4a2f"/><rect x="62" y="56" width="4" height="10" fill="#6b4a2f"/>',
       "Floor lamp": '<path d="M28 8 h24 l8 20 h-40z" fill="#e9c46a" stroke="#1f2a44" stroke-width="2"/><rect x="38" y="28" width="4" height="36" fill="#1f2a44"/><rect x="28" y="64" width="24" height="5" rx="2" fill="#1f2a44"/>',
       "Bookcase": '<rect x="20" y="6" width="40" height="62" fill="#a0764a" stroke="#1f2a44" stroke-width="2"/><line x1="20" y1="26" x2="60" y2="26" stroke="#1f2a44" stroke-width="2"/><line x1="20" y1="46" x2="60" y2="46" stroke="#1f2a44" stroke-width="2"/><rect x="24" y="12" width="5" height="14" fill="#2f4b7a"/><rect x="30" y="14" width="5" height="12" fill="#b5656b"/><rect x="26" y="32" width="5" height="14" fill="#3b6b5a"/><rect x="44" y="52" width="10" height="16" fill="#e9c46a"/>',
       "Wall mirror": '<ellipse cx="40" cy="38" rx="20" ry="28" fill="#cfe3ea" stroke="#a0764a" stroke-width="6"/><path d="M32 24 l8 -6" stroke="#fff" stroke-width="3"/>',
       "Dining set": '<rect x="10" y="30" width="60" height="8" rx="2" fill="#a0764a"/><rect x="16" y="38" width="4" height="26" fill="#6b4a2f"/><rect x="60" y="38" width="4" height="26" fill="#6b4a2f"/><rect x="2" y="20" width="4" height="44" fill="#6b4a2f"/><rect x="74" y="20" width="4" height="44" fill="#6b4a2f"/>',
       "Rug": '<rect x="8" y="22" width="64" height="34" rx="3" fill="#c97c82" stroke="#1f2a44" stroke-width="2"/><rect x="16" y="29" width="48" height="20" fill="none" stroke="#f6ebe8" stroke-width="3"/>'}
def ico(k, s=1):
    return f'<svg viewBox="0 0 80 72" width="{80*s:.0f}" height="{72*s:.0f}">{ICO[k]}</svg>'
lots = [("1", "Armchair", "Living room", "av"), ("2", "Floor lamp", "Living room", "av"), ("3", "Bookcase", "Den", "ho"), ("4", "Rug", "Living room", "ho"), ("5", "Wall mirror", "Hall", "av"), ("6", "Dining set", "Dining room", "av")]
room = f'''<div class=rm><div class=wl></div><div class=fl></div>
<div class=ob style="left:40px;bottom:120px">{ico("Bookcase",3.2)}<span class=lt>#3</span></div>
<div class=ob style="left:330px;top:40px">{ico("Wall mirror",2)}<span class=lt>#5</span></div>
<div class=ob style="left:400px;bottom:180px;z-index:3">{ico("Armchair",2.6)}<span class=lt>#1</span></div>
<div class=ob style="right:10px;bottom:130px">{ico("Floor lamp",3)}<span class=lt>#2</span></div>
<div class=ob style="left:240px;bottom:6px">{ico("Rug",3.0)}<span class=lt>#4</span></div></div>'''
P["p234_estate_s1"] = eb(1, "ESTATE SALE COMPANY · SALE WEEKEND", "A house full of items?<br><span>Show every lot online first.</span>",
f'''<div class=w1><div class="cd sc"><small class=cap>SAMPLE HOME · LIVING ROOM · 5 OF 214 LOTS TAGGED</small>{room}</div>
<div class=qs>{"".join(f'<span>{q}</span>' for q in ["“Is the armchair still there?”","“Can you hold the rug?”","“Which room is the bookcase in?”"])}</div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sc{flex:1;min-height:0;padding:16px;display:flex;flex-direction:column;gap:10px}
.rm{flex:1;position:relative;border-radius:16px;overflow:hidden}.wl{position:absolute;inset:0 0 34% 0;background:repeating-linear-gradient(90deg,#efd9d6 0 40px,#ead1ce 40px 80px)}.fl{position:absolute;inset:66% 0 0 0;background:repeating-linear-gradient(90deg,#c9a27a 0 90px,#bb946c 90px 94px)}
.ob{position:absolute;display:flex;flex-direction:column;align-items:center;gap:4px}.ob svg{display:block}
.qs{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.qs span{background:#1f2a44;color:#fff;border-radius:18px;padding:14px 16px;font:600 20px/1.4 'DM Sans'}""")

P["p234_estate_s2"] = eb(2, "STEP 1 · ONLINE LOT CATALOGUE", "Buyers browse lots<br><span>before the doors open.</span>",
f'''<div class=w2>{browser(f'<div class=bh><b>Sample Estate Sale · Sat 5 and Sun 6 Dec</b><span>214 lots · sample</span></div><div class=gr>{"".join(f"""<div class=lc><div class=lp>{ico(k,1.5)}</div><div class=li><span class=lt>#{n}</span><b>{k}</b><small>{r}</small><em class={s}>{"Available" if s=="av" else "On hold"}</em></div></div>""" for n,k,r,s in lots)}</div><div class=pz>Prices are set by you on each lot.</div>', url="yoursales.com/sale · sample", style="flex:1;min-height:0")}
<div class=nb><span class=ib>{ic("search",26)}</span><span>Every lot has a number, a photo and a room. <b>Fewer calls asking “is it still there?”</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bh{display:flex;justify-content:space-between;align-items:center;padding:14px 20px 6px}.bh b{font:700 24px/1.3 Lora}.bh span{font:700 15px 'DM Sans';background:#f6ebe8;color:#b5656b;padding:7px 12px;border-radius:10px}
.gr{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:12px;padding:10px 20px}
.lc{display:flex;gap:14px;align-items:center;border:2px solid #f0e4e2;border-radius:18px;padding:10px 14px}.lp{width:140px;height:120px;flex:none;border-radius:14px;background:#f6ebe8;display:flex;align-items:center;justify-content:center}.lp svg{display:block}
.li{flex:1;min-width:0;display:flex;flex-direction:column;align-items:flex-start;gap:4px}.li b{font:700 26px/1.3 Lora}.li small{font:500 17px 'DM Sans';color:#7d7a86}
.li em{font:700 15px 'DM Sans';font-style:normal;padding:5px 10px;border-radius:8px}.li em.av{background:#e3f1ea;color:#2e7d5b}.li em.ho{background:#fde2e3;color:#b5656b}
.pz{padding:4px 20px 14px;font:600 16px 'DM Sans';color:#7d7a86}""")

rooms = [("Living room", "Lots 1-40", 20, 20, 470, 300, "#f4c6c8"), ("Dining room", "Lots 41-75", 510, 20, 330, 300, "#e9d5b5"), ("Kitchen", "Lots 76-130", 510, 340, 330, 260, "#cfe0d8"), ("Den", "Lots 131-170", 20, 340, 280, 260, "#d6d9ea"), ("Hall", "Lots 171-180", 320, 340, 170, 260, "#efe6d0"), ("Garage", "Lots 181-214", 20, 620, 820, 170, "#dcdcdc")]
hm = '<svg viewBox="0 0 860 810" class=hm><rect x="6" y="6" width="848" height="798" rx="18" fill="#fff" stroke="#1f2a44" stroke-width="6"/>'
for nm, lt, x, y, w, h, c in rooms:
    hm += f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{c}" stroke="#1f2a44" stroke-width="3"/><text x="{x+w/2}" y="{y+h/2-6}" text-anchor="middle" font-family="Lora" font-weight="700" font-size="30" fill="#1f2a44"><tspan>{nm}</tspan></text><text x="{x+w/2}" y="{y+h/2+28}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="22" fill="#5b5f70"><tspan>{lt}</tspan></text>'
hm += '<path d="M260 760 L260 612 L310 612 L310 330 L560 330 L670 250" fill="none" stroke="#b5656b" stroke-width="7" stroke-dasharray="4 16" stroke-linecap="round"/>'
hm += '<rect x="200" y="760" width="120" height="40" rx="10" fill="#1f2a44"/><text x="260" y="787" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#fff"><tspan>Entry</tspan></text>'
hm += '<rect x="580" y="700" width="200" height="50" rx="12" fill="#b5656b"/><text x="680" y="733" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#fff"><tspan>Checkout table</tspan></text></svg>'
P["p234_estate_s3"] = eb(3, "STEP 2 · SALE DAY MAP", "Every room has<br><span>its own lot numbers.</span>",
f'''<div class=w3><div class="cd mp"><small class=cap>SAMPLE HOME · SALE MAP ON THE SALE PAGE</small>{hm}</div>
<div class=sd><div class=sx><b>6</b><span>rooms and the garage</span></div><div class=sx><b>214</b><span>lots, each with a number</span></div><div class=sx><b>1</b><span>checkout table</span></div>
<div class=sq>Buyers find lot #3 in the den without asking your team.</div></div></div>''',
css=""".w3{flex:1;display:flex;gap:14px;min-height:0}.mp{flex:1;min-width:0;padding:14px;display:flex;flex-direction:column;gap:8px}.hm{width:100%;flex:1;min-height:0;display:block}
.sd{width:250px;flex:none;display:flex;flex-direction:column;gap:12px}.sx{flex:1;background:#1f2a44;color:#fff;border-radius:20px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center}.sx b{font:700 50px/1.3 Lora;color:#f4c6c8}.sx span{font:500 18px/1.35 'DM Sans'}
.sq{background:#fff;border-radius:20px;padding:16px 18px;font:600 20px/1.4 'DM Sans'}""")
# 6 rooms? living, dining, kitchen, den, hall + garage = 5 rooms and the garage
P["p234_estate_s3"] = P["p234_estate_s3"].replace("<b>6</b><span>rooms and the garage</span>", "<b>5</b><span>rooms and the garage</span>")

holds = [("#4", "Rug", "Buyer 12", "Hold until Sat 2 PM", "ho"), ("#3", "Bookcase", "Buyer 7", "Hold until Sat 2 PM", "ho"), ("#6", "Dining set", "Buyer 21", "Paid · pickup Sun 4 PM", "pk"), ("#1", "Armchair", "Buyer 9", "Paid · taken Sat", "dn")]
P["p234_estate_s4"] = eb(4, "STEP 3 · HOLDS AND PICKUPS", "Holds and pickups,<br><span>in one list for the team.</span>",
f'''<div class=w4><div class="cd hl"><small class=cap>SAT 5 DEC · SAMPLE</small>{"".join(f'<div class=hr><div class=hi>{ico(k,1.2)}</div><div class=hn><span class=lt>{n}</span><b>{k}</b><small>{b}</small></div><em class={c}>{s}</em></div>' for n,k,b,s,c in holds)}</div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>When a hold ends, the lot goes back online as <b>available</b> by itself.</span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hl{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:8px}
.hr{flex:1;display:flex;align-items:center;gap:18px;border-top:1px solid #f0e4e2}.hi{width:130px;height:100px;flex:none;border-radius:14px;background:#f6ebe8;display:flex;align-items:center;justify-content:center}.hi svg{display:block}
.hn{flex:1;display:flex;flex-direction:column;align-items:flex-start;gap:2px}.hn b{font:700 30px/1.3 Lora}.hn small{font:500 18px 'DM Sans';color:#7d7a86}
.hr em{font:700 18px 'DM Sans';font-style:normal;padding:10px 16px;border-radius:12px}.hr em.ho{background:#fde2e3;color:#b5656b}.hr em.pk{background:#fff1d6;color:#9a6a00}.hr em.dn{background:#e3f1ea;color:#2e7d5b}""")

P["p234_estate_s5"] = eb(5, "YOUR TURN", "Run estate sales?<br><span>Let's build your sale page.</span>",
f'''<div class=w5><div class="cd ic5">{"".join(ico(k,2.1) for k in ["Armchair","Floor lamp","Bookcase","Wall mirror","Rug"])}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,40)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Lot catalogue","Number, photo, room"),("map","Sale day map","Lots by room"),("clock","Holds","End on time by themselves"),("truck","Pickups","One list for the team")])}</div>
<div class=q>How do buyers see your items before a sale today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b5656b;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ic5{flex:1;display:flex;justify-content:space-around;align-items:center;padding:22px}.ic5 svg{display:block}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:24px 22px;box-shadow:0 10px 22px rgba(31,42,68,.07)}
.ti .ib{width:76px;height:76px;border-radius:20px;background:#fde2e3;color:#b5656b}.ti b{display:block;font:700 36px/1.3 Lora}.ti span{font:500 21px/1.35 'DM Sans';color:#6a6f80}
.q{background:#1f2a44;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'DM Sans'}""")

# ───────── 235 INDIA · Street food carts (chaat) · SINGLE · TeX Gyre Adventor + Source Sans 3 · tamarind brown / mint green / turmeric
# New technique: row of drawn food carts, each with an out/back stock bar for puri packets; sold = out minus back in the table.
carts = [("Cart 1", "Station road", 40, 4), ("Cart 2", "College gate", 35, 9), ("Cart 3", "Market", 45, 2), ("Cart 4", "Park side", 30, 12), ("Cart 5", "Bus stand", 40, 5)]
def cart(i):
    c = ["#2f9e6e", "#e0a21a", "#c0532b", "#2f9e6e", "#e0a21a"][i]
    return f'''<svg viewBox="0 0 160 170" width="176" height="187"><rect x="22" y="14" width="116" height="22" rx="6" fill="{c}"/><path d="M22 36 q14.5 14 29 0 q14.5 14 29 0 q14.5 14 29 0 q14.5 14 29 0" fill="{c}"/>
<rect x="34" y="36" width="5" height="60" fill="#5a3b22"/><rect x="121" y="36" width="5" height="60" fill="#5a3b22"/><rect x="16" y="94" width="128" height="44" rx="6" fill="#7a4a26" stroke="#3a2412" stroke-width="3"/>
<ellipse cx="60" cy="90" rx="22" ry="8" fill="#f2d28a" stroke="#3a2412" stroke-width="2"/><ellipse cx="104" cy="90" rx="18" ry="7" fill="#e8b04a" stroke="#3a2412" stroke-width="2"/>
<rect x="48" y="106" width="64" height="22" rx="4" fill="#fff6e0"/><text x="80" y="122" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="14" fill="#3a2412"><tspan>{i+1}</tspan></text>
<circle cx="42" cy="150" r="14" fill="#2b2b2b"/><circle cx="42" cy="150" r="5" fill="#bbb"/><circle cx="118" cy="150" r="14" fill="#2b2b2b"/><circle cx="118" cy="150" r="5" fill="#bbb"/></svg>'''
mxo = 45
P["p235_chaat"] = page("""
body{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:#f6efd9;color:#3a2412}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#2f9e6e;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#c0532b}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.rw{background:#fff;border-radius:26px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(58,36,18,.08)}
.rw>small,.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#86735c}
.cs{display:flex;justify-content:space-between}.ct{width:172px;display:flex;flex-direction:column;align-items:center;gap:6px}.ct svg{display:block}
.ct b{font:700 19px/1.3 'TeX Gyre Adventor'}.ct span{font:600 16px/1.3 'Source Sans 3';color:#86735c}
.br{width:100%;height:22px;border-radius:11px;background:#f1e6c8;position:relative;overflow:hidden}.br i{position:absolute;left:0;top:0;bottom:0;background:#e0a21a}.br u{position:absolute;top:0;bottom:0;background:#c0532b}
.tb{flex:1;min-height:0;background:#fff;border-radius:26px;padding:14px 22px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(58,36,18,.08)}
.th,.tr{display:grid;grid-template-columns:1fr 1.3fr 110px 110px 110px;gap:10px;align-items:center}
.th{font:700 14px/1.4 'Source Sans 3';letter-spacing:1.5px;color:#86735c;padding:6px 0;border-bottom:2px solid #3a2412}
.tr{flex:1;border-bottom:1px solid #f1e6c8;font:600 21px 'Source Sans 3'}.tr b{font:700 21px 'TeX Gyre Adventor'}.tr span{text-align:center}.tr em{font-style:normal;text-align:center;font:800 22px 'Source Sans 3';color:#2f9e6e;background:#e3f4ea;border-radius:10px;padding:4px 0}
.tr.hi{background:#fff3e6}.tr.hi span:nth-child(4){color:#c0532b;font-weight:800}
.lgd{display:flex;gap:22px;font:600 16px 'Source Sans 3';color:#86735c;justify-content:flex-end}.lgd span{display:flex;align-items:center;gap:8px}.lgd i{width:14px;height:14px;border-radius:4px;background:#e0a21a}.lgd i.b{background:#c0532b}
""", "<div class=kk>CHAAT CARTS · ONE KITCHEN, FIVE CARTS</div><h1>5 carts went out today.<br><span>What came back?</span></h1>",
f'''<div class=vw><div class=rw><small>PURI PACKETS · OUT IN THE MORNING, BACK AT NIGHT · SAMPLE</small><div class=cs>{"".join(f'<div class=ct>{cart(i)}<b>{n}</b><span>{a}</span><div class=br><i style="width:{o/mxo*100:.0f}%"></i><u style="left:{(o-b)/mxo*100:.0f}%;width:{b/mxo*100:.0f}%"></u></div></div>' for i,(n,a,o,b) in enumerate(carts))}</div>
<div class=lgd><span><i></i>Sold</span><span><i class=b></i>Came back</span></div></div>
<div class=tb><div class=th><span>CART</span><span>AREA</span><span style="text-align:center">OUT</span><span style="text-align:center">BACK</span><span style="text-align:center">SOLD</span></div>
{"".join(f'<div class="tr{" hi" if b>=10 else ""}"><b>{n}</b><span style="text-align:left">{a}</span><span>{o}</span><span>{b}</span><em>{o-b}</em></div>' for n,a,o,b in carts)}
<div class=tr style="border:0"><b>Total</b><span style="text-align:left;color:#86735c">Mon 23 Nov · sample</span><span>{sum(c[2] for c in carts)}</span><span>{sum(c[3] for c in carts)}</span><em style="background:#2f9e6e;color:#fff">{sum(c[2]-c[3] for c in carts)}</em></div></div></div>''',
"#3a2412", "Run food carts? DM us", "background:#c0532b;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
