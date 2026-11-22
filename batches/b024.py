import sys, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 137 INDIA · CCTV installer · SINGLE · Poppins + Inter · graphite / lime / ice
# New technique: SVG floor plan with camera field-of-view wedges (computed arcs) + a quote card without prices.
def wedge(cx, cy, ang, spread, r):
    a1, a2 = math.radians(ang - spread / 2), math.radians(ang + spread / 2)
    x1, y1, x2, y2 = cx + r * math.cos(a1), cy + r * math.sin(a1), cx + r * math.cos(a2), cy + r * math.sin(a2)
    return f'<path d="M{cx} {cy} L{x1:.0f} {y1:.0f} A{r} {r} 0 0 1 {x2:.0f} {y2:.0f} Z" fill="#b8f34a" opacity=".28"/>'
cams = [(40, 40, 45, 80, 230, "C1"), (560, 40, 135, 80, 230, "C2"), (40, 380, -45, 70, 200, "C3"), (300, 400, -90, 70, 150, "C4"), (560, 600, 225, 60, 160, "C5"), (380, 600, -135, 60, 150, "C6")]
plan = f'''<svg viewBox="0 0 600 640" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
<rect x="20" y="20" width="560" height="600" fill="#232a33" stroke="#e9f0f6" stroke-width="8"/>
<path d="M20 400 L400 400 M400 400 L400 620 M480 400 L580 400" stroke="#e9f0f6" stroke-width="6"/>
<rect x="190" y="12" width="140" height="16" fill="#232a33"/><text x="260" y="58" text-anchor="middle" font-family="Inter" font-weight="700" font-size="16" fill="#8fa0b3">ENTRANCE</text>
<rect x="250" y="150" width="200" height="60" rx="8" fill="#384350"/><text x="350" y="186" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#c9d4df">COUNTER</text>
{"".join(f'<rect x="{x}" y="250" width="40" height="110" rx="6" fill="#384350"/>' for x in (80, 150))}
<text x="110" y="440" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#8fa0b3">STORE ROOM</text>
<text x="490" y="440" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#8fa0b3">BACK DOOR</text>
<rect x="572" y="470" width="16" height="90" fill="#232a33"/>
{"".join(wedge(x,y,a,s,r) for x,y,a,s,r,_ in cams)}
{"".join(f'<circle cx="{x}" cy="{y}" r="17" fill="#b8f34a"/><text x="{x}" y="{y+6}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="15" fill="#151a20">{n}</text>' for x,y,a,s,r,n in cams)}</svg>'''
items = [("Cameras", "6 · 4 dome + 2 bullet"), ("Recorder", "8-channel, room for 2 more"), ("Cable", "90 m, in conduit"), ("Phone view", "App set up on 2 phones"), ("Fitting", "1 day, shop stays open"), ("AMC", "1 year · 4 visits")]
P["p137_cctv"] = page("""
body{--f:'Inter';--h:'Poppins';background:#151a20;color:#e9f0f6}
h1{font-family:'Poppins';font-size:58px;font-weight:800;letter-spacing:-1.3px} h1 span{color:#b8f34a}
.sub{color:#9aa8b8}
.vis{gap:18px}
.pl{flex:1;background:#1c232b;border-radius:28px;padding:18px;display:flex;flex-direction:column;gap:10px;border:1.5px solid #2b3440}
.pl small,.qt small{font:700 13px Inter;letter-spacing:3px;color:#8fa0b3}
.pl .sv{flex:1;min-height:0}
.lg2{display:flex;gap:16px;font:600 16px Inter;color:#c9d4df}.lg2 span{display:flex;align-items:center;gap:8px}.lg2 i{width:18px;height:18px;border-radius:50%;background:#b8f34a;display:block}.lg2 i.w{border-radius:4px;opacity:.35}
.qt{width:360px;flex:none;background:#e9f0f6;color:#151a20;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:6px}
.qt h3{font:800 26px/1.25 Poppins}.qt h3 span{display:block;font:500 16px Inter;color:#5b6878}
.ql{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1.5px solid #d3dce5}
.ql span{font:600 14px Inter;color:#6b7888;letter-spacing:1px}.ql b{font:700 19px/1.3 Inter}
.ok{display:flex;align-items:center;gap:8px;background:#151a20;color:#b8f34a;border-radius:14px;padding:12px 14px;font:700 17px Inter}
""", "<h1>“Where will the<br>cameras go?”<br><span>Send a camera plan<br>with every quote.</span></h1>",
f'''<div class=pl><small>CAMERA PLAN · SAMPLE SHOP</small><div class=sv>{plan}</div><div class=lg2><span><i></i>Camera</span><span><i class=w></i>What it sees</span></div></div>
<div class=qt><small>QUOTE Q-118 · SAMPLE</small><h3>Sample Shop<span>Main market · site visit done</span></h3>
{"".join(f'<div class=ql><span>{a.upper()}</span><b>{b}</b></div>' for a,b in items)}
<div class=ok>{ic("check",20)} Approved on WhatsApp</div></div>''',
"#e9f0f6", "Install CCTV? DM us", "background:#b8f34a;color:#151a20")

# ───────── 139 CANADA · Pilates studio · SINGLE · Crimson Text + Poppins · eucalyptus / clay pink / bone
# New technique: top-down studio seat map — reformer machines drawn as rounded beds with carriage + straps, coloured by booked/free.
def reformer(st, n):
    return f'<div class="rf {st}"><i class=ca></i><i class=hb></i><b>{n}</b></div>'
row1 = [("bk", 1), ("bk", 2), ("fr", 3), ("bk", 4), ("me", 5)]
row2 = [("bk", 6), ("fr", 7), ("bk", 8), ("fr", 9), ("bk", 10)]
slots = [("7:00 AM", "Full", "fl"), ("12:00 PM", "4 spots", "op"), ("6:00 PM", "3 spots", "sel"), ("7:15 PM", "Waitlist", "wl")]
P["p139_pilates"] = page("""
body{--f:'Poppins';--h:'Crimson Text';background:#efe9df;color:#2d3a33}
h1{font-family:'Crimson Text';font-size:66px;font-weight:700;letter-spacing:-.4px;line-height:1.2} h1 span{color:#c46f5e}
.vis{flex-direction:column;gap:18px}
.hd{display:flex;gap:10px}
.hd div{flex:1;border-radius:16px;padding:12px 14px;background:#fff;display:flex;flex-direction:column;gap:2px;border:2px solid transparent}
.hd b{font:600 19px Poppins}.hd span{font:500 15px Poppins;color:#6e7a72}
.hd .fl{opacity:.55}.hd .sel{border-color:#5f8a75;background:#e3eee7}.hd .wl span{color:#c46f5e}
.st{flex:1;background:#dfe8e1;border-radius:30px;padding:22px 26px;display:flex;flex-direction:column;gap:14px;position:relative}
.st .tp{display:flex;justify-content:space-between;align-items:center}
.st .tp b{font:700 30px/1.25 'Crimson Text'}.st .tp span{font:600 16px Poppins;color:#46604f}
.mr{display:flex;align-items:center;justify-content:center;font:700 13px Poppins;letter-spacing:4px;color:#7d968a;background:repeating-linear-gradient(90deg,#cfdcd3 0 30px,#d7e2db 30px 60px);border-radius:12px;height:40px}
.rw{flex:1;display:flex;gap:16px}
.rf{flex:1;border-radius:22px;position:relative;background:#fff;border:3px solid #c9d6cd;display:flex;align-items:flex-end;justify-content:center;padding-bottom:12px}
.rf .ca{position:absolute;left:18%;right:18%;top:22%;height:36%;border-radius:12px;background:#e7ece8}
.rf .hb{position:absolute;left:30%;right:30%;top:7%;height:6%;border-radius:4px;background:#c9d6cd}
.rf b{font:600 18px Poppins;color:#6e7a72;position:relative}
.rf.bk{background:#cbd5ce;border-color:#cbd5ce}.rf.bk .ca{background:#b5c2b9}.rf.bk .hb{background:#a9b8ae}
.rf.fr{border-color:#5f8a75}.rf.fr .ca{background:#d7e8dd}
.rf.me{background:#c46f5e;border-color:#c46f5e}.rf.me .ca{background:#e2a497}.rf.me .hb{background:#f0c3b8}.rf.me b{color:#fff}
.lg3{display:flex;gap:18px;font:500 16px Poppins;color:#46604f}.lg3 span{display:flex;align-items:center;gap:8px}.lg3 i{width:18px;height:18px;border-radius:6px;display:block}
.bt{display:flex;gap:14px}
.bt div{border-radius:18px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:2px}
.bt .pk{flex:1;background:#fff}.bt .pk b{font:700 24px/1.25 'Crimson Text'}.bt .pk span{font:500 16px Poppins;color:#6e7a72}
.bt .go{width:330px;background:#2d3a33;color:#fff;font:600 19px Poppins;align-items:center;text-align:center}
""", "<h1>Clients texting “Any spot<br>at 6 tonight?”<br><span>Let them pick a reformer<br>and book it.</span></h1>",
f'''<div class=hd>{"".join(f'<div class={k}><b>{a}</b><span>{b}</span></div>' for a,b,k in slots)}</div>
<div class=st><div class=tp><b>Tuesday 6:00 PM · Reformer flow</b><span>Instructor 2 · SAMPLE</span></div><div class=mr>MIRROR WALL</div>
<div class=rw>{"".join(reformer(s,n) for s,n in row1)}</div><div class=rw>{"".join(reformer(s,n) for s,n in row2)}</div>
<div class=lg3><span><i style="background:#cbd5ce"></i>Booked</span><span><i style="background:#fff;border:3px solid #5f8a75"></i>Free</span><span><i style="background:#c46f5e"></i>Your pick: Reformer 5</span></div></div>
<div class=bt><div class=pk><b>10-class pack · 6 classes left</b><span>Sample client · cancel free up to 8 hours before</span></div><div class=go>Book Reformer 5</div></div>''',
"#2d3a33", "Run a Pilates studio? DM us", "background:#c46f5e;color:#fff")

# ───────── 140 INDIA · Freelancer portfolio + invoices · SINGLE · Bitter + Poppins · ink black / lemon / lilac
# New technique: bento-grid portfolio site with CSS-made project art (gradients, shapes, type specimens) + invoice status strip.
art = {
 "a1": '<div class=ar style="background:#ffe14d"><i style="position:absolute;left:24px;bottom:20px;width:120px;height:120px;border-radius:50%;background:#16151a"></i><i style="position:absolute;right:26px;top:24px;width:150px;height:70px;border-radius:40px;background:#c9b6ff"></i><em style="right:24px;bottom:24px;color:#16151a">Aa</em></div>',
 "a2": '<div class=ar style="background:#c9b6ff"><i style="position:absolute;left:20px;top:20px;right:20px;height:26px;border-radius:8px;background:#fff"></i><i style="position:absolute;left:20px;top:58px;width:45%;bottom:20px;border-radius:10px;background:#16151a"></i><i style="position:absolute;right:20px;top:58px;width:42%;bottom:20px;border-radius:10px;background:#fff;opacity:.8"></i></div>',
 "a3": '<div class=ar style="background:#16151a"><i style="position:absolute;left:50%;top:50%;width:90px;height:130px;transform:translate(-50%,-50%);border-radius:10px;background:#ffe14d"></i><i style="position:absolute;left:50%;top:50%;width:90px;height:30px;transform:translate(-50%,-50%);background:#c46f5e"></i></div>',
 "a4": '<div class=ar style="background:#f2efe8">' + "".join(f'<i style="position:absolute;left:{10+i*30}%;top:22%;width:24%;height:56%;border-radius:12px;background:{c}"></i>' for i,c in enumerate(["#ffe14d","#c9b6ff","#16151a"])) + '</div>',
 "a5": '<div class=ar style="background:linear-gradient(135deg,#ffe14d,#c9b6ff)"><em style="left:22px;top:18px;color:#16151a;font-size:44px">Hello.</em></div>'}
tiles = [("a1", "Brand kit", "Sample Café", "t1"), ("a2", "Website", "Sample Store", "t2"), ("a3", "Packaging", "Sample Tea", "t3"), ("a4", "Social posts", "Sample Salon", "t4"), ("a5", "Landing page", "Sample Studio", "t5")]
inv = [("INV-031", "Sample Café", "Paid", "pd"), ("INV-032", "Sample Store", "Sent · due 30 Nov", "sn"), ("INV-033", "Sample Tea", "Draft", "dr")]
P["p140_freelancer"] = page("""
body{--f:'Poppins';--h:'Bitter';background:#16151a;color:#f6f3ea}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:0;line-height:1.2} h1 span{color:#ffe14d}
.sub{color:#b9b4c6}
.vis{flex-direction:column;gap:16px}
.br{flex:1;min-height:0}
.pf{flex:1;background:#fff;color:#16151a;padding:16px 18px 18px;display:flex;flex-direction:column;gap:12px;min-height:0}
.pf .hd{display:flex;justify-content:space-between;align-items:center}
.pf .hd b{font:800 24px Bitter}.pf .hd span{display:block;font:500 15px Poppins;color:#6d6878}
.pf .hd em{font-style:normal;font:600 15px Poppins;background:#e6f7dc;color:#2f6b1e;padding:8px 12px;border-radius:20px}
.bn{flex:1;display:grid;grid-template-columns:1.3fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:12px;min-height:0}
.tl{border-radius:16px;overflow:hidden;display:flex;flex-direction:column;background:#f2efe8}
.t1{grid-row:span 2}
.ar{flex:1;position:relative;overflow:hidden;min-height:0}
.ar em{position:absolute;font:800 40px/1.2 Bitter;font-style:normal}
.tl .cp{flex:none;padding:8px 12px;display:flex;justify-content:space-between;align-items:center;gap:8px}
.tl .cp b{font:600 16px Poppins}.tl .cp span{font:500 14px Poppins;color:#6d6878}
.iv{flex:none;display:flex;gap:12px}
.iv div{flex:1;background:#24222b;border-radius:18px;padding:14px 16px;display:flex;flex-direction:column;gap:4px}
.iv small{font:700 13px Poppins;letter-spacing:2px;color:#8e889c}.iv b{font:600 19px Poppins}
.iv em{font-style:normal;align-self:flex-start;font:600 15px Poppins;padding:5px 10px;border-radius:8px;margin-top:2px}
.pd{background:#e6f7dc;color:#2f6b1e}.sn{background:#fff1a8;color:#6b5a00}.dr{background:#3a3744;color:#cfcade}
""", "<h1>Sending your work as<br>30 screenshots?<br><span>Get a portfolio site<br>and simple invoices.</span></h1>",
browser(f'''<div class=pf><div class=hd><div><b>Sample Designer</b><span>Design and websites for small brands</span></div><em>Open for new work</em></div>
<div class=bn>{"".join(f'<div class="tl {k}">{art[a]}<div class=cp><b>{t}</b><span>{c}</span></div></div>' for a,t,c,k in tiles)}</div></div>''', "yourname.design", "flex:1") +
f'''<div class=iv>{"".join(f'<div><small>{n} · SAMPLE</small><b>{c}</b><em class={k}>{s}</em></div>' for n,c,s,k in inv)}</div>''',
"#f6f3ea", "Freelancer? Let's build yours. DM us", "background:#ffe14d;color:#16151a")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
