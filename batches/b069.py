import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}



# ───────── 361 INDIA · Cable TV / local operator collections · SINGLE · Poppins + Fira Sans · signal purple / paid green / cream
# New technique: street strips with CSS clip-path houses (roof + body + door) per lane, coloured by bill status, on a
# grey road with dashed centre line; the collector's list and counts are computed from the same lanes.
LANES = [("Lane 1", "PPPDPPPPDP"), ("Lane 2", "PPDPPNPPPP"), ("Lane 3", "DPPPDDPPPP"), ("Lane 4", "PPPPPPDPPN")]
HS = [(ln, f"{i+1}{j+1:02d}", c) for i, (ln, st) in enumerate(LANES) for j, c in enumerate(st)]
DUE = [h for h in HS if h[2] == "D"]; NEW = [h for h in HS if h[2] == "N"]; PAID = [h for h in HS if h[2] == "P"]
def house(no, c):
    return f'<div class="hs1 {c}"><i class=rf></i><i class=bd><s></s></i><em>{no}</em></div>'
P["p361_cable"] = page("""
body{--f:'Fira Sans';--h:'Poppins';background:#f6f1e7;color:#251d3a}
.kk{font:600 16px/1.4 'Fira Sans';letter-spacing:3px;color:#6a3fb5;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#6a3fb5}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.mp1{flex:1;background:#fff;border-radius:26px;padding:14px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 28px rgba(37,29,58,.08);min-height:0}
.mp1>small,.cl1>small{font:600 13px/1.4 'Fira Sans';letter-spacing:2px;color:#7a7389}
.ln1{flex:1;display:grid;grid-template-columns:90px 1fr;gap:12px;align-items:center}
.ln1>b{font:800 20px/1.3 Poppins}
.st1{position:relative;display:flex;justify-content:space-between;padding:0 8px 14px}
.st1::after{content:"";position:absolute;left:0;right:0;bottom:0;height:12px;border-radius:6px;background:#d9d5de;background-image:repeating-linear-gradient(90deg,transparent 0 18px,#fff 18px 32px);background-size:100% 2px;background-repeat:repeat-x;background-position:0 5px}
.hs1{display:flex;flex-direction:column;align-items:center;width:70px}
.hs1 .rf{width:70px;height:30px;clip-path:polygon(50% 0,100% 100%,0 100%);background:#4b3a7a}
.hs1 .bd{width:56px;height:46px;position:relative;background:#3aa76d;border-radius:0 0 4px 4px}.hs1 .bd s{position:absolute;left:21px;bottom:0;width:14px;height:24px;background:rgba(0,0,0,.22);border-radius:3px 3px 0 0}
.hs1.D .bd{background:#f2a93b}.hs1.N .rf{background:#b9b1cc}.hs1.N .bd{background:#fff;border:3px dashed #8f86a6;border-top:0}
.hs1 em{font:600 16px/1.3 'Fira Sans';font-style:normal;color:#7a7389;margin-top:4px}
.lg1{display:flex;gap:20px;font:600 15px/1.4 'Fira Sans';color:#4c445e}.lg1 span{display:flex;align-items:center;gap:6px}.lg1 i{width:16px;height:16px;border-radius:4px}
.bt1{display:grid;grid-template-columns:1fr 1.15fr 1fr;gap:14px}
.ct1{background:#251d3a;color:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px}
.ct1 div{display:flex;justify-content:space-between;align-items:baseline;border-bottom:1px solid rgba(255,255,255,.12);padding-bottom:6px}.ct1 div:last-child{border:0}
.ct1 span{font:500 16px/1.4 'Fira Sans';color:#d6d0e6}.ct1 b{font:800 30px/1.2 Poppins}.ct1 .g{color:#7fe0a8}.ct1 .a{color:#ffc56b}.ct1 .n{color:#c9bdf0}
.cl1{background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 28px rgba(37,29,58,.08)}
.cl1 div{display:flex;flex-wrap:wrap;gap:6px}.cl1 i{font:700 16px/1.3 'Fira Sans';font-style:normal;background:#fdecd0;color:#8a5200;border-radius:8px;padding:6px 9px}.cl1 i.n{background:#eee9f8;color:#4b3a7a}
.cl1 p{margin-top:auto;font:700 18px/1.4 'Fira Sans';color:#251d3a}
.ms1{background:#6a3fb5;color:#fff;border-radius:22px 22px 22px 6px;padding:14px 18px;display:flex;flex-direction:column;gap:6px}.ms1 small{font:600 13px/1.4 'Fira Sans';letter-spacing:2px;color:#e0d4fb}.ms1 p{font:500 17px/1.45 'Fira Sans';text-wrap:pretty}
""", "<div class=kk>CABLE AND BROADBAND OPERATOR · MONTHLY BILLS</div><h1>Bill collection door to door?<br><span>Go only where it is due.</span></h1>",
f'''<div class=vw><div class=mp1><small>SAMPLE NAGAR · DECEMBER BILLS · {len(HS)} HOMES · SAMPLE</small>
{"".join(f'<div class=ln1><b>{ln}</b><div class=st1>{"".join(house(no, c) for l, no, c in HS if l == ln)}</div></div>' for ln, st in LANES)}
<div class=lg1><span><i style="background:#3aa76d"></i>Paid by UPI link</span><span><i style="background:#f2a93b"></i>Due</span><span><i style="border:2px dashed #8f86a6"></i>New connection request</span></div></div>
<div class=bt1><div class=ct1><div><span>Paid online</span><b class=g>{len(PAID)}</b></div><div><span>Due</span><b class=a>{len(DUE)}</b></div><div><span>New requests</span><b class=n>{len(NEW)}</b></div></div>
<div class=cl1><small>COLLECTOR · SATURDAY VISITS</small><div>{"".join(f"<i>{no}</i>" for l, no, c in DUE)}{"".join(f"<i class=n>{no} new</i>" for l, no, c in NEW)}</div><p>{len(DUE) + len(NEW)} doors instead of {len(HS)}.</p></div>
<div class=ms1><small>AUTO MESSAGE · 1 DEC</small><p>Your December bill is ready. Pay with this UPI link, or our collector comes on Saturday.</p></div></div></div>''',
"#251d3a", "Run a cable or net service? DM us", "background:#6a3fb5;color:#fff")


# ───────── 362 INDIA · Marble and granite dealer · CAROUSEL 5 · Cardo + Source Sans 3 · marble white / granite black / brass
# New techniques: CSS stone textures (vein gradients for marble, layered radial speckle for granite) on leaning slabs
# in an A-frame rack, a conic hold-timer ring, and a top-down rack slot map whose colours come from the slab list.
TX = {"W": "linear-gradient(115deg,transparent 38%,rgba(110,110,125,.55) 39%,transparent 41%),linear-gradient(62deg,transparent 58%,rgba(110,110,125,.4) 59%,transparent 61%),linear-gradient(160deg,transparent 20%,rgba(150,150,160,.35) 21%,transparent 22.5%),radial-gradient(circle at 30% 70%,#e6e3dd 0 20%,transparent 40%),#f7f5f0",
      "B": "radial-gradient(circle,#6b6b70 0 1.2px,transparent 1.6px) 0 0/9px 9px,radial-gradient(circle,#9a8f7a 0 1px,transparent 1.4px) 4px 5px/13px 11px,radial-gradient(circle,#3a3a3e 0 2px,transparent 2.4px) 2px 1px/17px 15px,#1f1f22",
      "G": "radial-gradient(circle,#c9a24a 0 1.2px,transparent 1.6px) 0 0/10px 10px,radial-gradient(circle,#0f2a22 0 2px,transparent 2.4px) 3px 4px/14px 12px,#1d4a3c",
      "C": "linear-gradient(120deg,transparent 45%,rgba(160,120,70,.5) 46%,transparent 48%),linear-gradient(70deg,transparent 30%,rgba(160,120,70,.35) 31%,transparent 33%),#e8d6b8",
      "R": "radial-gradient(circle,#2b1d1a 0 1.4px,transparent 1.8px) 0 0/9px 9px,radial-gradient(circle,#d9b9a6 0 1px,transparent 1.4px) 5px 3px/12px 12px,#8e4a3a",
      "S": "radial-gradient(circle,#555 0 1.2px,transparent 1.6px) 0 0/8px 8px,radial-gradient(circle,#f2f2f2 0 1.4px,transparent 1.8px) 4px 4px/11px 11px,#a9abae"}
SL = [("M-101", "White marble, grey veins", "W", "9 × 5.5 ft", "18 mm", "R1", "stock"),
      ("G-204", "Black granite", "B", "10 × 6 ft", "20 mm", "R2", "hold"),
      ("G-207", "Green granite, gold flecks", "G", "9 × 5 ft", "20 mm", "R2", "stock"),
      ("M-112", "Cream marble", "C", "8 × 5 ft", "18 mm", "R1", "sold"),
      ("G-215", "Red granite", "R", "10 × 5.5 ft", "20 mm", "R3", "stock"),
      ("G-221", "Grey granite, white dots", "S", "9 × 6 ft", "20 mm", "R3", "hold")]
STL = {"stock": "In stock", "hold": "On hold", "sold": "Sold today"}
MB = """
body{--f:'Source Sans 3';--h:'Cardo';background:#f1eee8;color:#1d1d1f}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#9a7630;margin-top:22px;margin-bottom:4px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#9a7630}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(29,29,31,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#77736b}
.nb{display:flex;align-items:center;gap:14px;background:#1d1d1f;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 'Source Sans 3'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#d9b866;color:#1d1d1f}.nb b{color:#e6c97a}
.chip{font:700 16px/1.3 'Source Sans 3';border-radius:8px;padding:5px 10px;display:inline-block}.stock{background:#e3efe6;color:#2d6a43}.hold{background:#f6ead0;color:#8a6410}.sold{background:#1d1d1f;color:#fff}
"""
def mb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1d1d1f;color:#e6c97a"):
    return page(MB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1d1d1f", cta, ctacss, tagline=f"{n} / 5")
P["p362_marble_s1"] = mb(1, "MARBLE AND GRANITE DEALER", "Which slab was it?<br><span>Show every slab with a photo.</span>",
f'''<div class=w1><div class="cd rk1"><div class=af1>{"".join(f'<div class=sb1 style="background:{TX[s[2]]};transform:skewX({-6+i*0.4}deg)"></div>' for i, s in enumerate(SL))}</div><div class=bs1></div></div>
<div class=bb1><span class=vn>{ic("chat",22)} A customer on the phone</span><p>“The one we saw last week. Light, with some lines. Is it still there?”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rk1{flex:1;padding:30px 40px 24px;display:flex;flex-direction:column;justify-content:flex-end}
.af1{flex:1;display:flex;gap:18px;align-items:flex-end;justify-content:center;padding:0 20px}.sb1{width:120px;height:92%;border-radius:6px;box-shadow:inset 0 0 0 3px rgba(0,0,0,.12),8px 10px 18px rgba(0,0,0,.18)}
.bs1{height:26px;border-radius:6px;background:linear-gradient(#8b8f96,#5b5f66)}
.bb1{background:#1d1d1f;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 'Source Sans 3';color:#e6c97a;margin-bottom:6px}.bb1 p{font:500 25px/1.4 'Source Sans 3'}""")

P["p362_marble_s2"] = mb(2, "STEP 1 · EVERY SLAB, ONE CARD", "Code, size and rack<br><span>under each photo.</span>",
f'''<div class=w2>{"".join(f'<div class="cd sc2"><div class=ph2 style="background:{TX[t]}"></div><div class=tx2><div class=hd2><b>{c}</b><span class="chip {st}">{STL[st]}</span></div><p>{n}</p><em>{sz} · {th} · Rack {r}</em></div></div>' for c,n,t,sz,th,r,st in SL)}</div>''',
css=""".w2{flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr;gap:14px;min-height:0}
.sc2{display:flex;flex-direction:column;overflow:hidden}.ph2{flex:1;min-height:0}.tx2{padding:12px 16px 14px}
.hd2{display:flex;justify-content:space-between;align-items:center}.hd2 b{font:700 26px/1.3 Cardo}.tx2 p{font:600 18px/1.35 'Source Sans 3';margin:4px 0 2px}.tx2 em{font:500 16px/1.4 'Source Sans 3';font-style:normal;color:#77736b}""")

H = SL[1]
P["p362_marble_s3"] = mb(3, "STEP 2 · SEND IT, HOLD IT", "Customer likes a photo?<br><span>Hold the slab for 3 days.</span>",
f'''<div class=w3><div class="cd ch3"><small class=cap>WHATSAPP · SAMPLE CUSTOMER</small>
<div class="bu3 me"><div class=pi3 style="background:{TX[H[2]]}"></div><b>{H[0]} · {H[1]}</b><span>{H[3]} · {H[4]} · real photo of this slab</span></div>
<div class=bu3>This one is perfect for our kitchen. Please keep it for us. We will come on Thursday.</div>
<div class="bu3 me">Done. {H[0]} is on hold for you till Thursday, 6 PM.</div></div>
<div class=sd3><div class="cd tm3"><div class=rg3><div><b>2 days</b><span>left on hold</span></div></div><small class=cap>{H[0]} · HOLD ENDS THU 6 PM</small></div>
<div class="cd hl3"><small class=cap>ON HOLD NOW</small>{"".join(f'<div class=hr3><i style="background:{TX[s[2]]}"></i><b>{s[0]}</b><span>Rack {s[5]}</span></div>' for s in SL if s[6]=="hold")}<small class=cap style="margin-top:6px">HOLD ENDED · BACK IN STOCK</small><div class=hr3><i style="background:{TX['W']}"></i><b>M-105</b><span>Rack R1</span></div><p>If no one comes, the slab goes back to the catalogue by itself.</p></div></div></div>''',
css=""".w3{flex:1;display:grid;grid-template-columns:1.25fr 1fr;gap:14px;min-height:0}.ch3{padding:16px 20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between;background:#ece5da}
.bu3{background:#fff;border-radius:18px 18px 18px 6px;padding:12px 16px;font:500 22px/1.45 'Source Sans 3';max-width:90%;text-wrap:pretty}.bu3.me{align-self:flex-end;background:#dcf3d2;border-radius:18px 18px 6px 18px}
.ch3 .bu3:nth-child(2){width:90%}.pi3{height:300px;border-radius:12px;margin-bottom:8px}.bu3 b{display:block;font:700 22px/1.3 Cardo}.bu3 span{font:500 16px/1.4 'Source Sans 3';color:#5d5a53}
.sd3{display:flex;flex-direction:column;gap:14px;min-height:0}.tm3{padding:24px 18px;display:flex;flex-direction:column;align-items:center;gap:12px}
.rg3{width:250px;height:250px;border-radius:50%;background:conic-gradient(#b08a3e 0 66%,#efe8da 66% 100%);display:flex;align-items:center;justify-content:center}
.rg3 div{width:190px;height:190px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}.rg3 b{display:block;font:700 40px/1.3 Cardo}.rg3 span{display:block;font:600 16px/1.4 'Source Sans 3';color:#77736b}
.hl3{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:10px}.hr3{display:flex;align-items:center;gap:12px;background:#f6f3ee;border-radius:14px;padding:14px 14px}.hr3 i{width:76px;height:56px;border-radius:6px;flex:none}.hr3 b{font:700 26px/1.3 Cardo}.hr3 span{margin-left:auto;font:600 16px/1.3 'Source Sans 3';color:#77736b}
.hl3 p{margin-top:auto;font:500 18px/1.45 'Source Sans 3';color:#4a4740}""")

RACKS = ["R1", "R2", "R3"]
EXTRA = {"R1": [("M-105", "W", "stock"), ("M-118", "C", "stock")], "R2": [("G-210", "B", "stock"), ("G-212", "G", "sold")], "R3": [("G-219", "R", "stock"), ("G-225", "S", "stock")]}
ALL = {r: [(s[0], s[2], s[6]) for s in SL if s[5] == r] + EXTRA[r] for r in RACKS}
CNT = {k: sum(1 for r in RACKS for x in ALL[r] if x[2] == k) for k in STL}
P["p362_marble_s4"] = mb(4, "STEP 3 · THE YARD MAP STAYS TRUE", "Sold slabs leave the list.<br><span>The yard map stays right.</span>",
f'''<div class=w4><div class="cd ym4"><small class=cap>YARD · TOP VIEW · 3 RACKS · SAMPLE</small><div class=rs4>{"".join(f'<div class=rk4><b>Rack {r}</b><div class=sl4>{"".join(f"<div class={chr(34)}st4 k-{k}{chr(34)}><i style={chr(34)}background:{TX[t]}{chr(34)}></i><span>{c}<em>{STL[k]}</em></span></div>" for c,t,k in ALL[r])}</div></div>' for r in RACKS)}</div></div>
<div class=ct4>{"".join(f'<div class="cd"><span class="chip {k}">{v}</span><b>{CNT[k]}</b><em>slabs</em></div>' for k,v in STL.items())}</div>
<div class=nb><span class=ib>{ic("truck",26)}</span><span>Sold today: {", ".join(c for r in RACKS for c,t,k in ALL[r] if k=="sold")}. <b>Loading list goes to the yard staff.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ym4{flex:1;padding:16px 22px;display:flex;flex-direction:column;gap:10px;min-height:0}
.rs4{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:16px;min-height:0}.rk4{background:#e7e2d8;border-radius:18px;padding:12px;display:flex;flex-direction:column;gap:8px}.rk4>b{font:700 24px/1.3 Cardo;text-align:center}
.sl4{flex:1;display:flex;flex-direction:column;gap:8px}.st4{flex:1;display:flex;align-items:center;gap:10px;background:#fff;border-radius:10px;padding:6px 10px;border-left:8px solid #2d6a43}.st4.k-hold{border-color:#d9a21b}.st4.k-sold{border-color:#1d1d1f;background:#f0ede7}
.st4 i{width:70px;height:100%;min-height:30px;border-radius:5px;flex:none}.st4 span{font:700 20px/1.3 'Source Sans 3'}.st4 em{display:block;font:600 14px/1.3 'Source Sans 3';font-style:normal;color:#77736b}
.ct4{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}.ct4 .cd{padding:12px 16px;display:flex;align-items:center;gap:12px}.ct4 b{font:700 38px/1.2 Cardo}.ct4 em{font:500 17px/1.3 'Source Sans 3';font-style:normal;color:#77736b}""")

P["p362_marble_s5"] = mb(5, "YOUR TURN", "Sell marble or granite?<br><span>Let's build your app.</span>",
f'''<div class=w5><div class="cd c5">{"".join(f'<i style="background:{TX[k]}"></i>' for k in "WBGCRS")}</div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("img","Slab catalogue","Photo, size, rack"),("send","WhatsApp sharing","Send the real slab"),("clock","Holds with a timer","Back to stock by itself"),("map","Yard map","In stock, on hold, sold")])}</div>
<div class=q>How do customers choose slabs at your yard today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#9a7630;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1.05fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:18px}.c5 i{border-radius:10px;box-shadow:inset 0 0 0 2px rgba(0,0,0,.08)}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(29,29,31,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#f3ead6;color:#1d1d1f}.ti b{display:block;font:700 27px/1.3 Cardo;margin-bottom:2px}.ti div span{font:500 18px/1.4 'Source Sans 3';color:#4a4740}
.q{background:#1d1d1f;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Source Sans 3'}""")


# ───────── 363 INDIA · Chappal / footwear wholesaler · SINGLE · Anton + Roboto · rubber teal / sole coral / sand
# New technique: size-run columns per article — a bar per size with a top-down SVG sole on top; the smallest size
# (bottleneck) is coral and sets how many full sets can be sold. The retailer order check is computed from it.
ARTS = [("A-12", "Flip-flop, navy", "#2a4d8f", {6: 40, 7: 52, 8: 18, 9: 22, 10: 30}),
        ("A-27", "Sandal, brown", "#8a5a3a", {6: 24, 7: 30, 8: 34, 9: 28, 10: 12}),
        ("A-31", "Slide, black", "#2b2b2b", {6: 20, 7: 26, 8: 24, 9: 30, 10: 22})]
def sole(c, w=34):
    return f'<svg viewBox="0 0 40 90" style="width:{w}px;display:block"><path d="M20 3 C33 3,37 22,34 40 C32 52,34 66,31 78 C29 86,11 86,9 78 C6 66,8 52,6 40 C3 22,7 3,20 3 Z" fill="{c}"/><path d="M12 30 Q20 22 28 30" fill="none" stroke="#fff" stroke-width="3" opacity=".7"/></svg>'
SETS = {a: min(sz.values()) for a, n, c, sz in ARTS}
ORDER = ("R-14", "A-27", 25)
OA = [a for a in ARTS if a[0] == ORDER[1]][0]; OK3 = SETS[ORDER[1]]; SHORT = {s: ORDER[2] - v for s, v in OA[3].items() if v < ORDER[2]}
P["p363_chappal"] = page("""
body{--f:'Roboto';--h:'Anton';background:#f3ecdf;color:#1f2a2a}
.kk{font:700 16px/1.5 Roboto;letter-spacing:3px;color:#127a74;margin-top:22px;margin-bottom:4px}
h1{font-family:'Anton';font-weight:400;font-size:68px;line-height:1.25;letter-spacing:.5px;text-transform:uppercase} h1 span{color:#e0604a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ar3{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px;min-height:0}
.ac3{background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(31,42,42,.08)}
.ac3>b{font:400 30px/1.5 Anton;letter-spacing:.5px}.ac3>span{font:500 17px/1.4 Roboto;color:#667272;margin-top:-6px}
.sz3{flex:1;display:flex;gap:8px;align-items:flex-end;border-bottom:2px solid #e6dccb;min-height:0}
.sz3>div{flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;justify-content:flex-end;height:100%}
.sz3 i{width:100%;border-radius:6px 6px 0 0;background:#bfe0dc}.sz3 .lo i{background:#e0604a}.sz3 em{font:700 16px/1.3 Roboto;font-style:normal}.sz3 .lo em{color:#c2432e}
.sx3{display:flex;gap:8px}.sx3 span{flex:1;text-align:center;font:600 15px/1.3 Roboto;color:#667272}
.fs3{background:#1f2a2a;color:#fff;border-radius:14px;padding:8px 12px;display:flex;justify-content:space-between;align-items:center}.fs3 small{font:600 14px/1.4 Roboto;color:#bfe0dc}.fs3 b{font:400 30px/1.4 Anton;color:#ffb3a5}
.bt3{display:grid;grid-template-columns:1.2fr 1fr;gap:14px}
.od3{background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(31,42,42,.08)}
.od3 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#667272}.od3 p{font:500 19px/1.45 Roboto}.od3 b{color:#127a74}.od3 .r{color:#c2432e}
.nt3{background:#127a74;color:#fff;border-radius:22px;padding:14px 18px;font:500 18px/1.45 Roboto;display:flex;flex-direction:column;gap:6px}.nt3 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#c9efe9}
""", "<div class=kk>CHAPPAL AND SANDAL WHOLESALE · SIZE SETS</div><h1>Size 8 sold out again?<br><span>See full sets, not pairs.</span></h1>",
f'''<div class=vw><div class=ar3>{"".join(f"""<div class=ac3><b>{a}</b><span>{n} · sample</span><small style="font:700 13px/1.4 Roboto;letter-spacing:1.5px;color:#667272">PAIRS IN STOCK BY SIZE</small>
<div class=sz3>{"".join(f'<div class="{"lo" if v == SETS[a] else ""}"><em>{v}</em>{sole(c)}<i style="height:{v/52*62:.0f}%"></i></div>' for s, v in sz.items())}</div>
<div class=sx3>{"".join(f"<span>{s}</span>" for s in sz)}</div><div class=fs3><small>FULL SETS<br>sizes 6 to 10</small><b>{SETS[a]}</b></div></div>""" for a, n, c, sz in ARTS)}</div>
<div class=bt3><div class=od3><small>RETAILER ORDER · {ORDER[0]}</small><p>{ORDER[2]} sets of {ORDER[1]}. <b>{OK3} full sets can go today.</b> <span class=r>Short for the rest: {", ".join(f"size {s}: {v} pair" + ("" if v == 1 else "s") for s, v in SHORT.items())}.</span></p></div>
<div class=nt3><small>FACTORY NOTE · SENT</small>{ORDER[1]} size 10 runs out first. Make more size 10 before the next order.</div></div></div>''',
"#1f2a2a", "Sell footwear wholesale? DM us", "background:#127a74;color:#fff")

# ───────── 364 USA · Consignment boutique · SINGLE · Lora + DM Sans · sage / dusty rose / linen
# New technique: a clothes rail drawn in CSS/SVG (hanger hooks, garment silhouettes in clip-path, string tags with
# day counters); each tag's markdown stage is computed from its days on the floor, and the consignor list matches.
STG = [(30, "Full price", "#e3ecdf", "#3f6b45"), (45, "20% off", "#f6e3e3", "#9a4a5a"), (60, "40% off", "#f0d0d6", "#7d2e42")]
def stage(d):
    for lim, nm, bg, fg in STG:
        if d <= lim: return nm, bg, fg
    return "Pickup or donate", "#2e2a27", "#fff"
ITEMS = [("T-201", "Wool coat", "#7a8b74", 12, "C-08"), ("T-188", "Silk blouse", "#d9a7b0", 34, "C-03"), ("T-176", "Denim jacket", "#4d6a8f", 52, "C-08"),
         ("T-205", "Knit sweater", "#c9b18f", 6, "C-11"), ("T-163", "Midi dress", "#9c5a6b", 61, "C-08"), ("T-194", "Blazer", "#3e3e44", 27, "C-03")]
GSH = {"Wool coat": "polygon(30% 0,70% 0,95% 18%,92% 100%,8% 100%,5% 18%)", "Silk blouse": "polygon(30% 0,70% 0,100% 22%,88% 34%,86% 70%,14% 70%,12% 34%,0 22%)",
       "Denim jacket": "polygon(30% 0,70% 0,100% 20%,94% 78%,6% 78%,0 20%)", "Knit sweater": "polygon(30% 0,70% 0,100% 24%,90% 34%,88% 76%,12% 76%,10% 34%,0 24%)",
       "Midi dress": "polygon(32% 0,68% 0,78% 30%,98% 100%,2% 100%,22% 30%)", "Blazer": "polygon(30% 0,70% 0,96% 18%,92% 86%,8% 86%,4% 18%)"}
C8 = [i for i in ITEMS if i[4] == "C-08"]
P["p364_consign"] = page("""
body{--f:'DM Sans';--h:'Lora';background:#f5efe6;color:#2e2a27}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#9a4a5a;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:60px;line-height:1.2;letter-spacing:-1px} h1 span{color:#5d7d5f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.rl4{flex:1.25;background:#fff;border-radius:26px;padding:14px 24px 16px;display:flex;flex-direction:column;box-shadow:0 12px 28px rgba(46,42,39,.08);min-height:0}
.rl4>small,.cs4>small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7c746b}
.bar4{height:10px;border-radius:5px;background:linear-gradient(#b9b2a8,#8f877d);margin:12px 0 0}
.hg4{flex:1;display:grid;grid-template-columns:repeat(6,1fr);gap:12px;min-height:0}
.it4{display:flex;flex-direction:column;align-items:center}
.it4 .hk{width:22px;height:20px;border:4px solid #8f877d;border-bottom:0;border-radius:12px 12px 0 0}
.it4 .gm{width:118px;height:220px;flex:none}
.tg4{margin-top:10px;align-self:stretch;background:#fffaf2;border:2px solid #d6cbbb;border-radius:8px;padding:6px 8px;box-shadow:0 6px 12px rgba(0,0,0,.1)}
.tg4 b{display:block;font:700 19px/1.3 Lora}.tg4 span{display:block;font:600 14px/1.35 'DM Sans';color:#7c746b}
.tg4 i{display:block;font:700 13px/1.3 'DM Sans';font-style:normal;border-radius:6px;padding:3px 5px;margin-top:4px;text-align:center}
.lg4{display:flex;gap:10px;margin-top:12px;flex-wrap:wrap}.lg4 span{font:700 14px/1.3 'DM Sans';border-radius:8px;padding:6px 10px}
.bt4{flex:1;display:grid;grid-template-columns:1.3fr 1fr;gap:14px;min-height:0}
.cs4{background:#fff;border-radius:26px;padding:14px 20px;display:flex;flex-direction:column;gap:4px;box-shadow:0 12px 28px rgba(46,42,39,.08)}
.cr4{flex:1;display:grid;grid-template-columns:70px 1fr 140px;gap:10px;align-items:center;border-bottom:1px solid #efe8dd}.cr4:last-child{border:0}
.cr4 b{font:700 18px/1.3 Lora}.cr4 span{font:500 17px/1.35 'DM Sans'}.cr4 i{font:700 14px/1.3 'DM Sans';font-style:normal;border-radius:8px;padding:6px 8px;text-align:center}
.ms4{background:#5d7d5f;color:#fff;border-radius:26px 26px 26px 6px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}.sd4{margin-top:auto;background:rgba(255,255,255,.14);border-radius:14px;padding:10px 14px}.sd4+.sd4{margin-top:0}.sd4 b{display:block;font:700 16px/1.4 Lora}.sd4 span{font:500 15px/1.4 'DM Sans'}
.ms4 small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#dfeadf}.ms4 p{font:500 19px/1.45 'DM Sans';text-wrap:pretty}
""", "<div class=kk>CONSIGNMENT BOUTIQUE · CONSIGNOR PORTAL</div><h1>“Did my coat sell yet?”<br><span>Give consignors a live list.</span></h1>",
f'''<div class=vw><div class=rl4><small>THE RAIL TODAY · DAYS ON THE FLOOR · SAMPLE</small><div class=bar4></div>
<div class=hg4>{"".join(f'<div class=it4><i class=hk></i><i class=gm style="background:{c};clip-path:{GSH[n]}"></i><div class=tg4><b>{t}</b><span>{n}</span><span>Day {d} · {cs.replace("-","&#8209;")}</span><i style="background:{stage(d)[1]};color:{stage(d)[2]}">{stage(d)[0]}</i></div></div>' for t,n,c,d,cs in ITEMS)}</div>
<div class=lg4>{"".join(f'<span style="background:{bg};color:{fg}">Up to day {lim}: {nm}</span>' for lim,nm,bg,fg in STG)}<span style="background:#2e2a27;color:#fff">Day 61: pickup or donate</span></div></div>
<div class=bt4><div class=cs4><small>CONSIGNOR C-08 · WHAT SHE SEES</small>{"".join(f'<div class=cr4><b>{t}</b><span>{n} · day {d}</span><i style="background:{stage(d)[1]};color:{stage(d)[2]}">{stage(d)[0]}</i></div>' for t,n,c,d,cs in C8)}</div>
<div class=ms4><small>AUTO TEXT · TO C-08</small><p>Your midi dress (T-163) reached day 61. Pick it up by Saturday, or we donate it as you chose.</p><div class=sd4><b>Sold for you this month</b><span>T-150 Leather bag · T-171 Wool scarf</span></div><div class=sd4><b>Next markdown</b><span>T-201 moves to 20% off on day 31</span></div></div></div></div>''',
"#2e2a27", "Run a consignment shop? DM us", "background:#9a4a5a;color:#fff")

# ───────── 365 INDIA · Kulhad (clay cup) maker for chai cafes · SINGLE · Gelasio + Inter · terracotta / clay cream / smoke charcoal
# New technique: CSS kulhads (clip-path tapered cups with a rim band) as an isotype (1 = 100) per cafe order, and a
# kiln week strip where each firing is filled to capacity from the order list in code (5% extra kept for breakage).
CAFES = [("Cafe 1", 600), ("Cafe 2", 400), ("Cafe 3", 900), ("Cafe 4", 300), ("Cafe 5", 500), ("Cafe 6", 800)]
TOTK = sum(c[1] for c in CAFES); NEED = round(TOTK * 1.05); CAP = 1500
FIR = []; left = NEED
for d in ["Mon", "Wed", "Fri"]:
    q = min(CAP, left); FIR.append((d, q)); left -= q
P["p365_kulhad"] = page("""
body{--f:'Inter';--h:'Gelasio';background:#f6ebdd;color:#2c2522}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#b5542c;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;line-height:1.2;letter-spacing:-1px} h1 span{color:#b5542c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.oc5{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px;min-height:0}
.cf5{background:#fff;border-radius:22px;padding:12px 16px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(44,37,34,.07)}
.cf5 .hd{display:flex;justify-content:space-between;align-items:baseline}.cf5 .hd b{font:700 24px/1.3 Gelasio}.cf5 .hd span{font:700 20px/1.3 Inter;color:#b5542c}
.ku5{flex:1;display:flex;flex-wrap:wrap;gap:10px 12px;align-content:center}
.kl{width:54px;height:62px;position:relative;flex:none}.kl::before{content:"";position:absolute;inset:6px 0 0;clip-path:polygon(0 0,100% 0,82% 100%,18% 100%);background:linear-gradient(90deg,#a9472a,#c9683f 45%,#a9472a)}
.kl::after{content:"";position:absolute;left:0;right:0;top:0;height:12px;border-radius:50%;background:#7e321c}
.cf5 small{font:600 14px/1.4 Inter;color:#7d6f66}
.kn5{background:#2c2522;color:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;gap:10px}
.kn5>div:first-child{display:flex;justify-content:space-between;align-items:baseline}.kn5 small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#f0b48f}.kn5>div:first-child b{font:700 18px/1.4 Inter}
.wk5{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}.wk5>div{background:rgba(255,255,255,.08);border-radius:14px;padding:8px 10px;display:flex;flex-direction:column;gap:6px}
.wk5 span{font:700 15px/1.3 Inter;color:#d8cbc2}.wk5 .bx{width:100%;height:30px;border-radius:6px;background:rgba(255,255,255,.12);overflow:hidden}.wk5 .bx i{display:block;height:100%;background:linear-gradient(90deg,#e0773f,#f2a66a)}
.wk5 b{font:700 22px/1.3 Gelasio}.wk5 em{font:500 13px/1.3 Inter;font-style:normal;color:#d8cbc2}
.kn5 p{font:500 16px/1.45 Inter;color:#eadfd7}.kn5 p b{color:#f2a66a}
""", "<div class=kk>KULHAD MAKER · WEEKLY CAFE ORDERS</div><h1>Kulhad orders from 6 cafes?<br><span>Plan each kiln firing.</span></h1>",
f'''<div class=vw><div class=oc5>{"".join(f'<div class=cf5><div class=hd><b>{n}</b><span>{q:,}</span></div><div class=ku5>{"".join("<i class=kl></i>" for _ in range(q//100))}</div><small>kulhads this week · sample</small></div>' for n,q in CAFES)}</div>
<div class=kn5><div><small>KILN WEEK · {CAP:,} KULHADS A FIRING</small><b>1 cup drawn = 100 kulhads</b></div>
<div class=wk5>{"".join(f'<div><span>{d}</span>' + (f'<div class=bx><i style="width:{q/CAP*100:.0f}%"></i></div><b>{q:,}</b><em>firing</em>' if q else '<div class=bx></div><b>–</b><em>' + ("drying" if d in ("Tue","Thu") else "deliveries") + '</em>') + '</div>' for d,q in [(d, dict(FIR).get(d, 0)) for d in ["Mon","Tue","Wed","Thu","Fri","Sat"]])}</div>
<p>Orders: {TOTK:,} kulhads. With 5% extra for breakage: <b>{NEED:,} to fire.</b> Each cafe gets its delivery day by message.</p></div></div>''',
"#2c2522", "Make clay products? DM us", "background:#b5542c;color:#fff")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
