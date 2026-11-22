import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 141 INDIA · Auto parts dealer · SINGLE · Anton + Roboto · gunmetal / tomato / fog
# New technique: parts bin wall (drawers with label cards + part number), search result pointing to the exact godown, rack and bin.
bins = [("BP-210", "Brake pad"), ("OF-118", "Oil filter"), ("SP-44", "Spark plug"), ("CL-302", "Clutch plate"), ("AF-77", "Air filter"),
        ("HB-12", "Headlight bulb"), ("WB-90", "Wiper blade"), ("BS-08", "Brake shoe"), ("CH-520", "Chain set"), ("FB-15", "Fan belt"),
        ("MR-61", "Mirror"), ("HN-05", "Horn"), ("BT-33", "Battery clamp"), ("SH-40", "Shocker"), ("GK-19", "Gasket kit")]
res = [("Godown 1", "Rack C · Bin 4", "18 pcs", "me"), ("Godown 2", "Rack A · Bin 9", "6 pcs", ""), ("Shop counter", "Drawer 2", "2 pcs", "")]
P["p141_parts"] = page("""
body{--f:'Roboto';--h:'Anton';background:#e6e9ec;color:#1f262e}
h1{font-family:'Anton';font-weight:400;font-size:64px;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#e2453a}
.vis{gap:18px}
.wl{flex:1;background:#2c3540;border-radius:28px;padding:20px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(5,1fr);gap:12px}
.bn{background:linear-gradient(#56636f,#46525d);border-radius:10px;padding:10px 10px 8px;display:flex;flex-direction:column;justify-content:space-between;position:relative;box-shadow:inset 0 -6px 0 rgba(0,0,0,.18)}
.bn .lc{background:#f4f1e8;border-radius:5px;padding:5px 8px;display:flex;flex-direction:column}
.bn .lc b{font:700 19px Roboto;color:#1f262e}.bn .lc span{font:500 15px Roboto;color:#59636d}
.bn i{align-self:center;width:56px;height:10px;border-radius:5px;background:#26303a;display:block}
.bn.me{background:linear-gradient(#e2453a,#c5372e);box-shadow:0 0 0 4px #ffd5cf,inset 0 -6px 0 rgba(0,0,0,.18)}
.rt{width:400px;flex:none;display:flex;flex-direction:column;gap:14px}
.sr{background:#fff;border-radius:18px;padding:14px 16px;display:flex;align-items:center;gap:10px;font:600 22px Roboto;box-shadow:0 10px 24px rgba(31,38,46,.08)}
.sr em{font-style:normal;margin-left:auto;font:700 14px Roboto;letter-spacing:2px;color:#8a949e}
.pc{flex:1;background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:8px}
.pc small{font:700 13px Roboto;letter-spacing:3px;color:#8a949e}
.pc h3{font:400 32px/1.3 Anton;letter-spacing:.3px}
.pc .fit{font:500 17px/1.4 Roboto;color:#59636d}
.lo{flex:1;display:flex;align-items:center;gap:12px;border-top:1.5px solid #edf0f2}
.lo i{width:14px;height:14px;border-radius:50%;background:#b5bec7;flex:none}.lo.me i{background:#e2453a;box-shadow:0 0 0 5px #ffd5cf}
.lo div{flex:1}.lo b{display:block;font:700 20px Roboto}.lo span{font:500 16px Roboto;color:#59636d}
.lo em{font-style:normal;font:700 18px Roboto}
.tt{background:#1f262e;color:#fff;border-radius:16px;padding:14px 16px;font:500 17px/1.4 Roboto}.tt b{color:#ffb3aa}
""", "<h1>Mechanic needs part BP-210.<br><span>Find it in 5 seconds,<br>not 15 minutes.</span></h1>",
f'''<div class=wl>{"".join(f'<div class="bn{" me" if c=="BP-210" else ""}"><div class=lc><b>{c}</b><span>{n}</span></div><i></i></div>' for c,n in bins)}</div>
<div class=rt><div class=sr>{ic("search",24)}BP-210<em>SAMPLE</em></div>
<div class=pc><small>PART FOUND</small><h3>Brake pad set · front</h3><div class=fit>Fits: sample bike models A, B and C</div>
{"".join(f'<div class="lo {k}"><i></i><div><b>{a}</b><span>{b}</span></div><em>{q}</em></div>' for a,b,q,k in res)}</div>
<div class=tt><b>26 pcs in all.</b> Reorder alert is set at 10 pcs.</div></div>''',
"#1f262e", "Run an auto parts shop? DM us", "background:#e2453a;color:#fff")

# ───────── 143 USA · Cake shop (custom cake orders) · SINGLE · Crimson Text + Inter · buttercream / raspberry / cocoa
# New technique: SVG tiered cake that matches the order form choices (tiers, flavor colors, drip, topper) beside the form.
cake = '''<svg viewBox="0 0 360 420" width="330" style="display:block">
<ellipse cx="180" cy="392" rx="160" ry="18" fill="#e9d3c0"/><rect x="40" y="376" width="280" height="14" rx="7" fill="#d8bfa9"/>
<rect x="60" y="270" width="240" height="108" rx="14" fill="#fbe3e8"/><path d="M60 284 Q75 300 90 284 T120 284 T150 284 T180 284 T210 284 T240 284 T270 284 T300 284 V272 H60 Z" fill="#c2185b"/>
<rect x="95" y="180" width="170" height="92" rx="12" fill="#fff6ea"/><path d="M95 194 Q108 208 121 194 T147 194 T173 194 T199 194 T225 194 T251 194 T265 194 V182 H95 Z" fill="#c2185b"/>
<rect x="125" y="110" width="110" height="72" rx="10" fill="#fbe3e8"/><path d="M125 122 Q136 134 147 122 T169 122 T191 122 T213 122 T235 122 V112 H125 Z" fill="#c2185b"/>
''' + "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="#fff"/>' for x, y in [(90, 330), (130, 340), (170, 330), (210, 340), (250, 330), (130, 235), (180, 240), (230, 235)]) + '''
<rect x="176" y="40" width="8" height="72" fill="#6b3f2a"/><path d="M150 40 H210 L200 70 H160 Z" fill="#f2b705"/><text x="180" y="62" text-anchor="middle" font-family="Inter" font-weight="800" font-size="14" fill="#4a2c1d">30</text></svg>'''
opts = [("Size", ["2 tier", "3 tier", "Sheet"], 1), ("Flavor", ["Vanilla", "Chocolate", "Red velvet"], 0), ("Filling", ["Raspberry", "Lemon", "Cream"], 0), ("Finish", ["Smooth", "Drip", "Naked"], 1)]
P["p143_cake"] = page("""
body{--f:'Inter';--h:'Crimson Text';background:#fff4e6;color:#4a2c1d}
h1{font-family:'Crimson Text';font-size:66px;font-weight:700;letter-spacing:-.4px;line-height:1.2} h1 span{color:#c2185b}
.vis{gap:20px}
.ck{width:380px;flex:none;background:#fde9ee;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:18px}
.ck b{font:700 26px/1.3 'Crimson Text';text-align:center}.ck span{font:500 16px Inter;color:#8a5a45}
.fm{flex:1;background:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 16px 34px rgba(74,44,29,.08)}
.fm small{font:700 13px Inter;letter-spacing:3px;color:#a88a7a}
.fm h3{font:700 30px/1.25 'Crimson Text'}
.op{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:1.5px solid #f4e6da}
.op>b{font:700 14px Inter;letter-spacing:2px;color:#a88a7a}
.ch{display:flex;gap:8px}.ch span{flex:1;text-align:center;font:600 17px Inter;padding:10px 4px;border-radius:12px;border:1.5px solid #ead8c9}
.ch span.on{background:#4a2c1d;color:#fff;border-color:#4a2c1d}
.rw{display:flex;gap:10px}.rw div{flex:1;background:#fff4e6;border-radius:12px;padding:10px 12px;display:flex;flex-direction:column;gap:2px}
.rw span{font:600 13px Inter;color:#a88a7a;letter-spacing:1px}.rw b{font:600 17px Inter}
.bt{background:#c2185b;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 18px Inter}
""", "<h1>Cake orders over 40<br>DMs and voice notes?<br><span>Send one custom cake<br>order form.</span></h1>",
f'''<div class=ck>{cake}<b>3 tiers · vanilla<br>raspberry · drip</b><span>Preview updates as they pick</span></div>
<div class=fm><small>CUSTOM CAKE ORDER · SAMPLE</small><h3>Build your cake</h3>
{"".join(f'<div class=op><b>{a.upper()}</b><div class=ch>' + "".join(f'<span class="{"on" if i==k else ""}">{o}</span>' for i,o in enumerate(os)) + '</div></div>' for a,os,k in opts)}
<div class=rw><div><span>PICKUP</span><b>Sat, Dec 5 · 11 AM</b></div><div><span>TOPPER TEXT</span><b>“30”</b></div></div>
<div class=bt>Send order · we confirm in 1 day</div></div>''',
"#4a2c1d", "Own a cake shop? DM us", "background:#c2185b;color:#fff")

# ───────── 144 INDIA · Pet grooming at home · SINGLE · Montserrat + Lora · aqua / sunny yellow / charcoal
# New technique: pet "passport" profile cards with SVG pet faces + stamps of past visits, next to a groomer's day plan on a phone.
dog = '<svg viewBox="0 0 100 100" width="112"><ellipse cx="22" cy="40" rx="14" ry="26" fill="#9a6a3c"/><ellipse cx="78" cy="40" rx="14" ry="26" fill="#9a6a3c"/><circle cx="50" cy="52" r="32" fill="#e0b07a"/><ellipse cx="50" cy="66" rx="16" ry="12" fill="#f6dfc0"/><circle cx="38" cy="46" r="4" fill="#2b2b2b"/><circle cx="62" cy="46" r="4" fill="#2b2b2b"/><ellipse cx="50" cy="60" rx="6" ry="4" fill="#2b2b2b"/></svg>'
cat = '<svg viewBox="0 0 100 100" width="112"><path d="M22 20 L34 44 L18 46 Z M78 20 L66 44 L82 46 Z" fill="#7d7d86"/><circle cx="50" cy="56" r="32" fill="#9b9ba6"/><circle cx="38" cy="52" r="5" fill="#2f8f5b"/><circle cx="62" cy="52" r="5" fill="#2f8f5b"/><path d="M46 64 L54 64 L50 69 Z" fill="#e58a9a"/><path d="M30 66 H14 M30 70 H16 M70 66 H86 M70 70 H84" stroke="#55555e" stroke-width="2"/></svg>'
pets = [(dog, "Sample dog · Bruno", "Labrador · 4 yrs", ["Bath + dry", "Nail trim"], "Scared of dryer noise", "Sep", "Oct"), (cat, "Sample cat · Mishti", "Persian · 2 yrs", ["Brush + bath", "Ear clean"], "Calm if held on the lap", "Aug", "Nov")]
day = [("10:00", "Bruno · Sample Flat 12", "Bath + nails"), ("12:30", "Mishti · Sample Villa 4", "Brush + bath"), ("3:00", "Sample dog · Tiger", "Full groom"), ("5:30", "Sample dog · Coco", "Nail trim")]
P["p144_petgroom"] = page("""
body{--f:'Montserrat';--h:'Lora';background:#dff5f2;color:#22282b}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.4px;line-height:1.2} h1 span{color:#0d8a7e}
.vis{gap:22px;align-items:center}
.lf{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:16px}
.pp{flex:1;background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:10px;border-left:10px solid #ffcf3a;box-shadow:0 14px 30px rgba(34,40,43,.08);position:relative;overflow:hidden}
.pp .tp{display:flex;gap:14px;align-items:center}
.pp .fc{width:130px;height:130px;border-radius:22px;background:#fff6d4;display:flex;align-items:center;justify-content:center;flex:none}
.pp small{font:700 12px Montserrat;letter-spacing:2.5px;color:#8a9497}
.pp b{display:block;font:700 30px/1.25 Lora}.pp .tp span{font:500 18px Montserrat;color:#5d676b}
.pp .sv{display:flex;gap:8px}.pp .sv i{font-style:normal;font:600 17px Montserrat;background:#dff5f2;color:#0b6d64;border-radius:10px;padding:7px 10px}
.pp .nt{font:600 18px Montserrat;color:#a05a00;background:#fff3d1;border-radius:10px;padding:8px 10px}
.pp .nx{margin-top:auto;font:600 16px Montserrat;color:#0b6d64;border-top:1.5px dashed #cfe9e5;padding-top:10px}.pp .st{position:absolute;right:16px;top:16px;display:flex;gap:8px}
.pp .st em{width:58px;height:58px;border-radius:50%;border:2.5px dashed #0d8a7e;color:#0d8a7e;font:700 12px/1.35 Montserrat;font-style:normal;display:flex;align-items:center;justify-content:center;text-align:center}
.ap{flex:1;padding:8px 16px 16px;display:flex;flex-direction:column;gap:9px;background:#f4fbfa}
.ap small{font:700 12px Montserrat;letter-spacing:2.5px;color:#8a9497}.ap .t{font:700 22px Lora}
.vi{flex:1;background:#fff;border-radius:14px;padding:10px 12px;display:flex;flex-direction:column;justify-content:center;gap:2px;border-left:5px solid #0d8a7e}
.vi em{font-style:normal;font:700 14px Montserrat;color:#0d8a7e}.vi b{font:700 16px Montserrat}.vi span{font:500 14px Montserrat;color:#5d676b}
.ap .bt{background:#ffcf3a;border-radius:12px;padding:11px;text-align:center;font:700 15px Montserrat}
""", "<h1>Pet parents ask the same<br>questions every visit?<br><span>Keep a profile for<br>every pet.</span></h1>",
f'''<div class=lf>{"".join(f'<div class=pp><div class=st>{"".join(f"<em>{m}<br>✓</em>" for m in (m1,m2))}</div><div class=tp><div class=fc>{svg}</div><div><small>PET PROFILE · SAMPLE</small><b>{n}</b><span>{br}</span></div></div><div class=sv>{"".join(f"<i>{s}</i>" for s in sv)}</div><div class=nt>Note: {nt}</div><div class=nx>Next visit: {nx} · reminder sent 2 days before</div></div>' for (svg,n,br,sv,nt,m1,m2),nx in zip(pets,["Sat 5 Dec","Wed 9 Dec"]))}</div>
{phone(f"""<div class=ap><small>GROOMER 1 · SAMPLE</small><div class=t>Today · 4 home visits</div>{"".join(f'<div class=vi><em>{t}</em><b>{a}</b><span>{b}</span></div>' for t,a,b in day)}<div class=bt>Send “on my way” message</div></div>""", w=340, h=690)}''',
"#22282b", "Groom pets at home? DM us", "background:#0d8a7e;color:#fff")

# ───────── 145 INDIA · Oil mill · SINGLE · Gelasio + Source Sans 3 · golden oil / deep green / cream
# New technique: SVG storage tanks with liquid level fills, level lines and batch tags, plus a dealer order list.
def tank(x, name, pct, col, cap):
    h = 260; lv = h * pct
    return f'''<g transform="translate({x},0)"><rect x="0" y="40" width="150" height="{h}" rx="20" fill="#f6efdc" stroke="#2c4a33" stroke-width="5"/>
<clipPath id="t{x}"><rect x="2.5" y="42.5" width="145" height="{h-5}" rx="18"/></clipPath>
<rect x="0" y="{40+h-lv}" width="150" height="{lv}" fill="{col}" clip-path="url(#t{x})"/><path d="M0 {40+h-lv} Q37 {32+h-lv} 75 {40+h-lv} T150 {40+h-lv}" fill="{col}" clip-path="url(#t{x})"/>
<rect x="55" y="20" width="40" height="24" rx="4" fill="#2c4a33"/>
<text x="75" y="{40+h-lv-12 if pct<.85 else 40+h-lv+30}" text-anchor="middle" font-family="Gelasio" font-weight="700" font-size="28" fill="#2c4a33">{int(pct*100)}%</text>
<text x="75" y="336" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="19" fill="#2c4a33">{name}</text>
<text x="75" y="360" text-anchor="middle" font-family="Source Sans 3" font-weight="600" font-size="16" fill="#6b6a55">{cap}</text></g>'''
tanks = '<svg viewBox="0 0 560 370" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block;flex:1;min-height:0">' + tank(10, "Mustard", .72, "#d9a514", "Tank 1 · 8,000 L") + tank(205, "Groundnut", .38, "#e8c35a", "Tank 2 · 6,000 L") + tank(400, "Sesame", .15, "#b9811a", "Tank 3 · 4,000 L") + '</svg>'
orders = [("Sample Dealer 1", "Mustard · 120 tins of 15 L", "Packed", "ok"), ("Sample Dealer 2", "Groundnut · 80 tins of 15 L", "Filling today", "md"), ("Sample Dealer 3", "Sesame · 60 tins of 15 L", "Needs pressing", "hi")]
P["p145_oil"] = page("""
body{--f:'Source Sans 3';--h:'Gelasio';background:#f7f0dc;color:#1f3424}
h1{font-family:'Gelasio';font-size:58px;font-weight:700;letter-spacing:-.4px;line-height:1.2} h1 span{color:#b07a06}
.vis{flex-direction:column;gap:16px}
.tk{flex:1;min-height:0;background:#fffaf0;border-radius:30px;padding:20px 26px;display:flex;flex-direction:column;justify-content:center;gap:10px;box-shadow:0 14px 30px rgba(31,52,36,.07)}
.tk small,.od small{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#8f8a72}
.od{flex:none;background:#1f3424;color:#f7f0dc;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:6px}
.od small{color:#a9b7a6}
.or{display:flex;align-items:center;gap:14px;padding:9px 0;border-top:1.5px solid #34503b}
.or div{flex:1}.or b{display:block;font:700 21px 'Source Sans 3'}.or span{font:500 17px 'Source Sans 3';color:#c9d3c2}
.or em{font-style:normal;font:700 16px 'Source Sans 3';padding:7px 12px;border-radius:10px}
.ok em{background:#cfe8c9;color:#1f5a2c}.md em{background:#f6dc8c;color:#6b4a00}.hi em{background:#f4b9a6;color:#7a2a12}
.al{display:flex;align-items:center;gap:10px;background:#f6dc8c;color:#3d2c00;border-radius:12px;padding:10px 14px;font:600 17px 'Source Sans 3';margin-top:4px}
""", "<h1>How much oil is left in each tank?<br><span>Know before you take the order.</span></h1>",
f'''<div class=tk><small>TANK LEVELS · LIVE · SAMPLE</small>{tanks}</div>
<div class=od><small>DEALER ORDERS THIS WEEK · SAMPLE</small>{"".join(f'<div class="or {k}"><div><b>{a}</b><span>{b}</span></div><em>{s}</em></div>' for a,b,s,k in orders)}
<div class=al>{ic("bell",20)}<span>Sesame tank at 15%: 600 L left, the order needs 900 L. Plan a pressing batch.</span></div></div>''',
"#1f3424", "Run an oil mill? DM us", "background:#1f3424;color:#f6dc8c")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
