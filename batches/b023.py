import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 131 INDIA · Cab / taxi operator · SINGLE · Montserrat + Fira Sans · matte black / cab yellow / steel
# New technique: split-flap departure board — every character in its own flap cell with a centre split line.
def flap(t, n, cls=""):
    t = t.ljust(n)
    return f'<span class="fw {cls}">' + "".join(f'<i>{c if c!=" " else "&nbsp;"}</i>' for c in t) + '</span>'
duty = [("06:30", "CAR 4", "DRV 2", "AIRPORT", "DONE", "dn"), ("08:00", "CAR 1", "DRV 5", "CITY 8H", "ON TRIP", "on"), ("09:15", "CAR 7", "DRV 3", "OUTSTATION", "ON TRIP", "on"),
        ("11:00", "CAR 2", "DRV 1", "STATION", "NEXT", "nx"), ("14:30", "CAR 4", "DRV 6", "HOTEL", "NEXT", "nx"), ("18:00", "CAR 1", "DRV 4", "AIRPORT", "NEXT", "nx")]
P["p131_cab"] = page("""
body{--f:'Fira Sans';--h:'Montserrat';background:#f3f1ea;color:#16171a}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.4px} h1 span{background:#ffc928;padding:0 12px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.vis{flex-direction:column;gap:18px}
.bd{flex:1;background:#16171a;border-radius:30px;padding:24px 26px;display:flex;flex-direction:column;gap:6px;box-shadow:0 24px 50px rgba(0,0,0,.25)}
.bh{display:flex;justify-content:space-between;align-items:center;padding-bottom:10px}
.bh b{font:800 26px 'Montserrat';color:#ffc928;letter-spacing:1px}.bh span{font:700 14px 'Fira Sans';letter-spacing:3px;color:#8d9097}
.rr,.hr{display:grid;grid-template-columns:repeat(5,auto);justify-content:space-between;align-items:center}
.hr span{font:700 13px 'Fira Sans';letter-spacing:3px;color:#8d9097}
.rr{flex:1;border-top:1.5px solid #2a2c31}
.fw{display:flex;gap:2px}
.fw i{width:23px;height:38px;border-radius:4px;background:linear-gradient(#2c2e34 0 49%,#0e0f11 49% 51%,#25272c 51%);color:#f3f1ea;font:700 22px/38px 'Fira Sans';font-style:normal;text-align:center;display:block}
.dn i{color:#7ee08a}.on i{color:#ffc928}.nx i{color:#9fc3ff}
.cs{flex:none;display:flex;gap:16px}
.cs div{flex:1;background:#fff;border-radius:22px;padding:16px 18px;display:flex;flex-direction:column;gap:4px;border-top:6px solid #ffc928}
.cs b{font:800 21px/1.3 'Montserrat'}.cs span{font:500 17px/1.35 'Fira Sans';color:#5d6068}
""", "<h1>“Who took Car 4 today?”<br><span>See every duty</span><br><span>on one board.</span></h1><div class=sub>For cab and taxi operators: driver duties, trip logs and fuel in one app.</div>",
f'''<div class=bd><div class=bh><b>TODAY'S DUTIES</b><span>7 CARS · 6 DRIVERS · SAMPLE</span></div>
<div class=hr><span>TIME</span><span>CAR</span><span>DRIVER</span><span>TRIP</span><span>STATUS</span></div>
{"".join(f'<div class=rr>{flap(a,5)}{flap(b,5)}{flap(c,5)}{flap(d,10)}{flap(e,7,k)}</div>' for a,b,c,d,e,k in duty)}</div>
<div class=cs>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("Trip log per car","Km at start and end of every trip"),("Fuel entries","With a photo of the bill"),("Duty hours","Per driver, per week")])}</div>''',
"#16171a", "Run a cab or taxi service? DM us", "background:#16171a;color:#ffc928")

# ───────── 133 USA · Courier / delivery startup · SINGLE · TeX Gyre Adventor + Inter · kraft brown / cobalt / off-white
# New technique: isometric SVG parcel stack (three shaded faces + tape) next to a live tracking timeline.
def box(x, y, s, h, c):
    top, left, right = c
    return (f'<path d="M{x} {y} L{x+s} {y-s/2} L{x+2*s} {y} L{x+s} {y+s/2} Z" fill="{top}"/>'
            f'<path d="M{x} {y} L{x+s} {y+s/2} L{x+s} {y+s/2+h} L{x} {y+h} Z" fill="{left}"/>'
            f'<path d="M{x+s} {y+s/2} L{x+2*s} {y} L{x+2*s} {y+h} L{x+s} {y+s/2+h} Z" fill="{right}"/>'
            f'<path d="M{x+s*.5} {y-s/4} L{x+s*1.5} {y+s/4}" stroke="#e9d3a8" stroke-width="{s*.16:.0f}"/>'
            f'<path d="M{x+s*1.5} {y+s/4} L{x+s*1.5} {y+s/4+h*.45}" stroke="#e9d3a8" stroke-width="{s*.16:.0f}"/>')
K = ("#d9a873", "#b98450", "#9c6b3c")
stack = '<svg viewBox="20 120 300 290" width="320" style="display:block">' + box(40, 300, 70, 70, K) + box(180, 300, 70, 70, K)[0:0] + box(110, 335, 70, 60, K) + box(40, 230, 70, 70, K) + box(150, 270, 60, 60, ("#e4b886", "#c28e59", "#a37444")) + box(80, 150, 60, 80, K) + box(170, 210, 50, 50, ("#cfe0ff", "#2f5bd3", "#1f43a8")) + '</svg>'
steps = [("Picked up", "9:12 AM · Sample Store", "dn"), ("At our hub", "11:40 AM · sorted", "dn"), ("Out for delivery", "1:05 PM · Driver 3", "now"), ("Delivered", "Expected 2:30–3:00 PM", "")]
P["p133_courier"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#f5efe4;color:#14213d}
h1{font-family:'TeX Gyre Adventor';font-size:62px;font-weight:700;letter-spacing:-1.4px} h1 span{color:#2f5bd3}
.sub{color:#5a6477}
.vis{gap:20px}
.lf{width:360px;flex:none;display:flex;flex-direction:column;gap:16px}
.st{flex:1;background:linear-gradient(#ead9bd 0 78%,#d8c09a 78%);border-radius:30px;display:flex;align-items:center;justify-content:center}
.sc{flex:none;background:#14213d;color:#fff;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;gap:6px}
.sc b{font:700 40px/1.3 'TeX Gyre Adventor';color:#9fb8ff}.sc span{font:500 17px/1.4 Inter;color:#c8d0e0}
.br{flex:1;min-width:0}
.tk{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:12px;background:#fff}
.tk small{font:700 13px Inter;letter-spacing:3px;color:#8b93a3}
.tk h3{font:700 28px/1.3 'TeX Gyre Adventor'}
.eta{background:#e8eeff;border-radius:16px;padding:14px 16px;display:flex;flex-direction:column;gap:2px}
.eta span{font:600 15px Inter;color:#2f5bd3;letter-spacing:1px}.eta b{font:700 30px/1.3 'TeX Gyre Adventor'}
.tl{flex:1;display:flex;flex-direction:column;position:relative;padding-left:6px}
.sp{flex:1;display:flex;gap:16px;align-items:flex-start;position:relative}
.sp:not(:last-child):after{content:"";position:absolute;left:15px;top:34px;bottom:0;width:3px;background:#d7deeb}
.sp.dn:after{background:#2f5bd3!important}
.sp i{width:33px;height:33px;border-radius:50%;flex:none;border:3px solid #c7d0e0;background:#fff;display:flex;align-items:center;justify-content:center}
.sp.dn i{background:#2f5bd3;border-color:#2f5bd3}.sp.now i{border-color:#2f5bd3;box-shadow:0 0 0 6px #dbe5ff}
.sp.now i:after{content:"";width:13px;height:13px;border-radius:50%;background:#2f5bd3}
.sp b{display:block;font:700 22px 'Inter'}.sp span{font:500 17px Inter;color:#6b7385}
.al{display:flex;align-items:center;gap:10px;background:#14213d;color:#fff;border-radius:14px;padding:13px 16px;font:500 17px Inter}
""", "<h1>“Where's my package?”<br><span>Give every customer<br>a tracking page.</span></h1><div class=sub>For delivery startups: live steps, a time window and a text at each step.</div>",
f'''<div class=lf><div class=st>{stack}</div><div class=sc><b>1 link</b><span>per package, sent by text the moment you pick it up</span></div></div>
{browser(f"""<div class=tk><small>TRACKING · SAMPLE ORDER SA-20417</small><h3>Your package is on its way</h3>
<div class=eta><span>EXPECTED TODAY</span><b>2:30 – 3:00 PM</b></div>
<div class=tl>{"".join(f'<div class="sp {k}"><i>{ic("check",16,"#fff",3) if k=="dn" else ""}</i><div><b>{a}</b><span>{b}</span></div></div>' for a,b,k in steps)}</div>
<div class=al>{ic("chat",22)}<span>Text sent: “Out for delivery, 2:30–3:00 PM.”</span></div></div>""", "track.yourdelivery.com", "flex:1;min-width:0")}''',
"#14213d", "Run a delivery business? DM us", "background:#2f5bd3;color:#fff")

# ───────── 134 INDIA · Flour mill (atta chakki) · SINGLE · Bitter + DM Sans · wheat / flour white / indigo
# New technique: SVG flour mill (hopper, motor, belt, outlet into a sack) + perforated token ticket + ready-message bubble.
mill = '''<svg viewBox="0 0 300 360" width="270" style="display:block">
<path d="M90 20 L210 20 L180 90 L120 90 Z" fill="#c9a55a"/><path d="M100 20 L200 20 L190 40 L110 40 Z" fill="#e5c983"/>
<rect x="110" y="90" width="80" height="20" fill="#6b7280"/><rect x="80" y="110" width="140" height="120" rx="14" fill="#3b4a8c"/>
<circle cx="150" cy="170" r="36" fill="#2c3870"/><circle cx="150" cy="170" r="12" fill="#c9cfe6"/>
<rect x="230" y="150" width="56" height="70" rx="10" fill="#6b7280"/><path d="M186 160 L236 160 M186 200 L236 200" stroke="#1f2937" stroke-width="5"/>
<rect x="128" y="230" width="44" height="40" fill="#6b7280"/>
<path d="M98 270 L202 270 L214 350 L86 350 Z" fill="#f3ead6"/><path d="M98 270 L202 270 L198 290 L102 290 Z" fill="#e2d6bb"/>
<text x="150" y="325" text-anchor="middle" font-family="Bitter" font-weight="700" font-size="20" fill="#3b4a8c">T-42</text>
<rect x="60" y="230" width="180" height="10" rx="5" fill="#2c3870"/></svg>'''
toks = [("41", "Wheat · 10 kg · fine", "Ready · message sent", "rd", "Dropped 10:20 AM"), ("42", "Bajra · 5 kg · coarse", "Grinding now", "gr", "Ready by 6:00 PM"),
        ("43", "Jowar · 8 kg · fine", "Next in line", "q", "Dropped 1:45 PM"), ("44", "Rice · 4 kg · fine", "In queue", "q", "Dropped 2:30 PM"), ("45", "Wheat · 12 kg · medium", "In queue", "q", "Home pickup · 3:10 PM")]
P["p134_mill"] = page("""
body{--f:'DM Sans';--h:'Bitter';background:#f4e6c4;color:#1f2a55}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:0;line-height:1.2} h1 span{color:#3b4a8c;background:#fffaf0;padding:0 10px;border-radius:8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.vis{gap:18px}
.lf{width:350px;flex:none;display:flex;flex-direction:column;gap:16px}
.ml{flex:1;background:#e8d3a2;border-radius:30px;display:flex;align-items:center;justify-content:center}
.tt{flex:none;background:#fffaf0;border-radius:10px;padding:18px 20px;position:relative;display:flex;flex-direction:column;gap:4px;
-webkit-mask:radial-gradient(circle 10px at 0 50%,transparent 98%,#000) left/51% 100% no-repeat,radial-gradient(circle 10px at 100% 50%,transparent 98%,#000) right/51% 100% no-repeat}
.tt small{font:700 13px 'DM Sans';letter-spacing:3px;color:#9a8a66}.tt b{font:800 46px/1.3 'Bitter';color:#3b4a8c}.tt span{font:600 18px/1.4 'DM Sans'}
.tt em{font-style:normal;border-top:2px dashed #d9c79c;margin-top:6px;padding-top:8px;font:600 16px 'DM Sans';color:#6b6046}
.rt{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.ls{flex:1;background:#fffaf0;border-radius:28px;padding:18px 22px;display:flex;flex-direction:column;gap:4px}
.ls small{font:700 13px 'DM Sans';letter-spacing:3px;color:#9a8a66;padding-bottom:6px}
.tr{flex:1;display:flex;align-items:center;gap:14px;border-top:1.5px solid #efe3c6}
.tr i{width:58px;height:46px;flex:none;border-radius:12px;background:#1f2a55;color:#fff;font:800 22px/1 'Bitter';font-style:normal;display:flex;align-items:center;justify-content:center}
.tr div{flex:1;min-width:0}.tr b{display:block;font:700 22px 'DM Sans'}.tr div span{font:500 16px 'DM Sans';color:#7a7058}
.tr em{font-style:normal;font:700 15px 'DM Sans';padding:6px 10px;border-radius:8px;white-space:nowrap}
.rd em{background:#dcefdc;color:#2c6b34}.gr em{background:#ffe2a6;color:#7a5200}.q em{background:#e7eaf5;color:#3b4a8c}
.mg{flex:none;align-self:flex-end;max-width:520px;background:#dcf5d0;border-radius:20px 20px 4px 20px;padding:14px 18px;font:500 18px/1.45 'DM Sans';box-shadow:0 10px 24px rgba(31,42,85,.08)}
.mg small{display:block;font:700 13px 'DM Sans';letter-spacing:2px;color:#4f7a45;margin-bottom:2px}
""", "<h1>Grain bags piling up<br>with paper slips?<br><span>Give a token, send a</span><br><span>“ready” message.</span></h1>",
f'''<div class=lf><div class=ml>{mill}</div><div class=tt><small>TOKEN · SAMPLE</small><b>T-42</b><span>Bajra · 5 kg · coarse<br>Ready by 6:00 PM</span><em>Show this or your number at pickup</em></div></div>
<div class=rt><div class=ls><small>TODAY'S QUEUE · SAMPLE</small>{"".join(f'<div class="tr {k}"><i>{n}</i><div><b>{a}</b><span>{d}</span></div><em>{s}</em></div>' for n,a,s,k,d in toks)}</div>
<div class=mg><small>SENT ON WHATSAPP</small>Your wheat flour (token 41) is ready. Please pick it up before 8 PM.</div></div>''',
"#1f2a55", "Run a flour mill? DM us", "background:#3b4a8c;color:#fff")

# ───────── 135 INDIA · Personal expense tracker (individual) · SINGLE · Cardo + Roboto · manila / terracotta / ink
# New technique: CSS envelope budgets (flap via clip-path, fill level shown as a coloured insert peeking out).
env = [("Groceries", 8200, 10000), ("Travel", 2100, 3000), ("Eating out", 3900, 3000), ("Bills", 4600, 5000), ("Shopping", 1200, 4000)]
fmt = lambda v: f"₹{v:,}"
today = [("Chai", 20, "Eating out"), ("Auto", 60, "Travel"), ("Vegetables", 180, "Groceries"), ("Phone recharge", 299, "Bills")]
P["p135_expense"] = page("""
body{--f:'Roboto';--h:'Cardo';background:#f1e5cc;color:#1e2233}
h1{font-family:'Cardo';font-size:64px;font-weight:700;letter-spacing:-.5px;line-height:1.2} h1 span{color:#b4532a}
.vis{gap:22px;align-items:center}
.lf{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:12px}
.lf>small{font:700 13px 'Roboto';letter-spacing:3px;color:#8a7a5c}
.ev{flex:1;display:flex;align-items:center;gap:16px;background:#fff8ea;border-radius:20px;padding:10px 18px 10px 12px}
.en{width:104px;height:72px;flex:none;position:relative;border-radius:6px;background:#d9b878;overflow:hidden}
.en:before{content:"";position:absolute;left:0;right:0;top:0;height:44px;background:#c9a462;clip-path:polygon(0 0,100% 0,50% 100%)}
.en u{position:absolute;left:10px;right:10px;bottom:6px;border-radius:3px;display:block}
.et{flex:1;display:flex;flex-direction:column;gap:6px;min-width:0}
.et .t{display:flex;justify-content:space-between;align-items:baseline}.et b{font:700 26px 'Cardo'}.et span{font:600 17px 'Roboto';color:#6b6455}
.et s{display:block;height:10px;border-radius:5px;background:#efe2c6;position:relative;overflow:hidden;text-decoration:none}
.et s i{position:absolute;left:0;top:0;bottom:0;border-radius:5px}
.ov .et span{color:#c2321f;font-weight:700}
.ap{flex:1;padding:10px 18px 18px;display:flex;flex-direction:column;gap:9px;background:#fbf6ec}
.ap small{font:700 12px 'Roboto';letter-spacing:2.5px;color:#9a8f7a}
.ap .tt{font:700 26px 'Cardo'}
.it{display:flex;justify-content:space-between;align-items:center;background:#fff;border-radius:12px;padding:10px 12px}
.it b{font:600 17px 'Roboto'}.it span{display:block;font:500 14px 'Roboto';color:#8a8172}.it em{font-style:normal;font:700 17px 'Roboto'}
.ad{margin-top:auto;background:#1e2233;color:#fff;border-radius:16px;padding:14px;display:flex;flex-direction:column;gap:10px}
.ad .am{font:700 30px 'Roboto'}.ad .cp{display:flex;gap:6px;flex-wrap:wrap}.ad .cp span{font:600 13px 'Roboto';padding:6px 9px;border-radius:8px;background:#2f3450}
.ad .cp span.on{background:#e7a07f;color:#1e2233}
.ad .sv{background:#b4532a;border-radius:10px;padding:10px;text-align:center;font:700 16px 'Roboto'}
""", "<h1>Where did this month's<br>money go?<br><span>Get an app made just<br>for your spending.</span></h1>",
f'''<div class=lf><small>THIS MONTH · SPENT OF LIMIT · SAMPLE</small>{"".join(f'<div class="ev{" ov" if a>b else ""}"><div class=en><u style="height:{min(a/b,1)*40+8:.0f}px;background:{"#c2321f" if a>b else "#e7a07f" if a/b>.8 else "#7aa37a"}"></u></div><div class=et><div class=t><b>{n}</b><span>{fmt(a)} of {fmt(b)}{" · over" if a>b else ""}</span></div><s><i style="width:{min(a/b,1)*100:.0f}%;background:{"#c2321f" if a>b else "#e7a07f" if a/b>.8 else "#7aa37a"}"></i></s></div></div>' for n,a,b in env)}</div>
{phone(f"""<div class=ap><small>TODAY · SAMPLE</small><div class=tt>{fmt(559)} spent</div>{"".join(f'<div class=it><div><b>{a}</b><span>{c}</span></div><em>{fmt(v)}</em></div>' for a,v,c in today)}
<div class=ad><div class=am>₹ 450</div><div class=cp>{"".join(f'<span class="{"on" if c=="Eating out" else ""}">{c}</span>' for c in ["Groceries","Eating out","Travel","Bills"])}</div><div class=sv>Add expense</div></div></div>""", w=340, h=700)}''',
"#1e2233", "Want your own app? DM us", "background:#b4532a;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
