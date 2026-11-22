import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 211 INDIA · Tender coconut supplier · SINGLE · Anton + Source Sans 3 · coconut green / husk tan / cream
# New technique: isotype (pictogram) chart — one drawn coconut = 10 coconuts, a row per stall, numbers derived from icons.
def nut(c="#5f9a3a", top="#e9f2c9"):
    return f'<svg width="34" height="38" viewBox="0 0 34 38"><path d="M17 3 C30 3 32 18 31 26 C30 34 24 36 17 36 C10 36 4 34 3 26 C2 18 4 3 17 3 Z" fill="{c}" stroke="#2f4d1e" stroke-width="2"/><ellipse cx="17" cy="8" rx="8" ry="4" fill="{top}" stroke="#2f4d1e" stroke-width="1.6"/><path d="M9 20 Q11 30 17 32" stroke="#ffffff" stroke-opacity=".35" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>'
stalls = [("Stall 1", "Beach road", 120, "ok", "OTP confirmed"), ("Stall 2", "Bus stand", 80, "ok", "OTP confirmed"),
          ("Stall 3", "College road", 140, "ok", "OTP confirmed"), ("Stall 4", "Market gate", 60, "wait", "Not confirmed"),
          ("Stall 5", "Park corner", 100, "ok", "OTP confirmed")]
tot211 = sum(s[2] for s in stalls)
P["p211_coconut"] = page("""
body{--f:'Source Sans 3';--h:'Anton';background:#f6f0df;color:#20361a}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#9a6b3c;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:74px;letter-spacing:0;line-height:1.2} h1 span{color:#4f8a2e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ch{flex:1;min-height:0;background:#fffdf5;border-radius:28px;padding:16px 26px 14px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(32,54,26,.08)}
.chh{display:flex;justify-content:space-between;align-items:center;padding-bottom:10px;border-bottom:2px solid #efe6cf}
.sm small{line-height:1.5!important}.chh small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#7b7560}
.key{display:flex;align-items:center;gap:8px;font:600 17px 'Source Sans 3';color:#4a5a40}.key svg{width:24px;height:27px}
.rw{flex:1;display:grid;grid-template-columns:170px 1fr 150px;align-items:center;gap:12px;border-bottom:1px solid #f1ead8}.rw:last-child{border:0}
.rw b{display:block;font:400 28px/1.4 Anton;letter-spacing:.5px;margin-bottom:2px}.rw span{font:500 17px 'Source Sans 3';color:#6c6a58}
.ic{display:flex;flex-wrap:wrap;gap:3px;align-items:center}
.ic svg{display:block}
.st{display:flex;flex-direction:column;align-items:flex-end;gap:2px}.st em{font-style:normal;font:400 30px/1.3 Anton}
.st i{font-style:normal;font:700 14px 'Source Sans 3';border-radius:9px;padding:4px 9px;background:#e4f0d6;color:#2f5a1c}.st i.w{background:#9a6b3c;color:#fff}
.sm{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.sm div{background:#20361a;color:#fff;border-radius:22px;padding:14px 20px}.sm small{display:block;font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#c7dcb2}.sm b{display:block;font:400 40px/1.5 Anton;margin:2px 0 4px}.sm span{font:500 17px 'Source Sans 3';color:#d9e6cc}
.sm .hk{background:#9a6b3c}.sm .hk small{color:#f3dfc6}.sm .hk span{color:#f6e8d6}
""", "<div class=kk>TENDER COCONUT SUPPLIERS · DAILY DROPS</div><h1>Coconut drops on a paper chit?<br><span>Count every stall in the app.</span></h1>",
f'''<div class=vw><div class=ch><div class=chh><small>TODAY · TUE 24 NOV · SAMPLE ROUTE</small><span class=key>{nut()}= 10 coconuts</span></div>
{"".join(f'<div class=rw><div><b>{a}</b><span>{b}</span></div><div class=ic>{nut() * (n//10)}</div><div class=st><em>{n}</em><i class="{"w" if k=="wait" else ""}">{t}</i></div></div>' for a,b,n,k,t in stalls)}</div>
<div class=sm><div><small>DROPPED TODAY</small><b>{tot211}</b><span>coconuts, 5 stalls</span></div><div><small>CONFIRMED</small><b>4 of 5</b><span>stalls by OTP</span></div><div class=hk><small>WEEKLY BILL</small><b>Sunday</b><span>made by the app</span></div></div></div>''',
"#20361a", "Supply coconuts? DM us", "background:#4f8a2e;color:#fff")

# ───────── 212 INDIA · Photo frame shop · CAROUSEL 5 · Cardo + Inter · walnut brown / gallery white / gold leaf
# New techniques: proportional frame wall (sizes drawn to scale), moulding swatches as SVG wood patterns, frame preview with dimension arrows.
FB = """
body{--f:'Inter';--h:'Cardo';background:#f7f4ee;color:#2b1d14}
.kk{font:600 16px/1.4 'Inter';letter-spacing:3px;color:#a8822e;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#7a4a2a}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(43,29,20,.07)}
.fr{border-style:solid;border-color:#7a4a2a;background:#efe7da;position:relative;box-shadow:0 10px 20px rgba(43,29,20,.18), inset 0 0 0 2px rgba(0,0,0,.15)}
.fr .mt{position:absolute;background:#fff;box-shadow:inset 0 0 0 1px #d9cfbe}
.fr .ph{position:absolute;overflow:hidden}
.fr .ph svg{width:100%;height:100%;display:block}
.tag{background:#fffaf0;border:2px solid #d9c39a;border-radius:8px;padding:6px 10px;font:600 16px/1.35 Inter;color:#5a3d22}
.stF{border-radius:10px;padding:5px 11px;font:600 16px Inter;display:inline-block}
.sR{background:#2b1d14;color:#fff}.sG{background:#a8822e;color:#fff}.sC{background:#efe4cf;color:#5a3d22}.sW{background:#fff;color:#7a4a2a;border:2px dashed #a8822e}
"""
def fb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2b1d14;color:#fff"):
    return page(FB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2b1d14", cta, ctacss, tagline=f"{n} / 5")
def land(pid, w=300, h=200):
    return f'''<svg viewBox="0 0 300 200" preserveAspectRatio="xMidYMid slice"><rect width="300" height="200" fill="#cfe3ea"/><circle cx="230" cy="52" r="22" fill="#f3d27a"/>
<path d="M0 140 L70 80 L120 120 L180 60 L260 130 L300 110 L300 200 L0 200 Z" fill="#8fb09a"/><path d="M0 170 Q80 140 160 165 T300 160 L300 200 L0 200 Z" fill="#5e8a6b"/></svg>'''
def frame(W, H, bw=14, mat=16, col="#7a4a2a"):
    return f'<div class=fr style="width:{W}px;height:{H}px;border-width:{bw}px;border-color:{col}"><div class=mt style="inset:0"></div><div class=ph style="inset:{mat}px">{land("a")}</div></div>'
# scale: 22 px per inch
wall = [(5, 7, "“5x7 or 6x8?”"), (8, 10, "Which moulding?"), (12, 18, "Glass or acrylic?"), (8, 12, "Mount colour?"), (6, 8, "Pickup when?")]
P["p212_frame_s1"] = fb(1, "PHOTO FRAME SHOPS · CUSTOM ORDERS", "Frame orders on<br>scraps of paper?<br><span>Sizes get mixed up.</span>",
f'''<div class=w1><div class=wl>
<div class=c1>{frame(12*22, 18*22, 16, 18)}<div class=tag style="transform:rotate(-3deg)">Glass or acrylic?</div></div>
<div class=c2>{frame(8*22, 10*22, 12, 14, "#a8822e")}<div class=tag style="transform:rotate(2deg)">Which moulding?</div>{frame(5*22, 7*22, 10, 10, "#2b1d14")}<div class=tag style="transform:rotate(-2deg)">“5x7 or 6x8?”</div></div>
<div class=c3>{frame(8*22, 12*22, 12, 14, "#5a3d22")}<div class=tag style="transform:rotate(3deg)">Mount colour?</div>{frame(6*22, 8*22, 10, 12, "#a8822e")}<div class=tag style="transform:rotate(-3deg)">Pickup when?</div></div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>5 orders today, 5 paper slips. One slip says only “big, brown, Friday”.</span></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.wl{flex:1;min-height:0;background:#e9e1d3;border-radius:28px;display:flex;justify-content:space-around;align-items:center;padding:16px 18px}
.c1,.c2,.c3{display:flex;flex-direction:column;align-items:center;gap:12px}
.nb{display:flex;align-items:center;gap:14px;background:#2b1d14;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Inter}.nb .ib{width:50px;height:50px;border-radius:14px;background:#a8822e}""")

mould = [("Walnut 1 in", "wn", "#6b4126", "#7e5233"), ("Gold leaf 1.5 in", "gd", "#b8913a", "#d4b25a"), ("Black flat 0.75 in", "bk", "#1f1a17", "#2f2925"), ("Natural oak 1 in", "ok", "#c9a272", "#d8b88a")]
def swatch(pid, a, b):
    return f'''<svg viewBox="0 0 120 60" preserveAspectRatio="none"><defs><pattern id="m{pid}" width="120" height="10" patternUnits="userSpaceOnUse"><rect width="120" height="10" fill="{a}"/><path d="M0 5 Q30 2 60 6 T120 4" stroke="{b}" stroke-width="2" fill="none"/></pattern></defs>
<rect width="120" height="60" fill="url(#m{pid})"/><rect x="0" y="0" width="120" height="8" fill="#000" opacity=".12"/></svg>'''
P["p212_frame_s2"] = fb(2, "PART 1 · ORDER ON A TABLET", "Size, moulding, glass.<br><span>Picked, not guessed.</span>",
f'''<div class=w2><div class=tb><div class=sc>
<div class=hd2><div><small>NEW ORDER F-301 · SAMPLE CUSTOMER</small><b>Custom frame</b></div><span class="stF sC">Pickup Sat 28 Nov</span></div>
<div class=row2><label>Photo size</label><div class=chs>{"".join(f'<span class="{"on" if s=="12 x 18 in" else ""}">{s}</span>' for s in ["8 x 10 in","8 x 12 in","12 x 18 in","16 x 20 in"])}</div></div>
<div class=row2 style="align-items:flex-start"><label>Moulding</label><div class=mg>{"".join(f'<div class="{"on" if k=="wn" else ""}">{swatch(k,a,b)}<span>{n}</span></div>' for n,k,a,b in mould)}</div></div>
<div class=row2><label>Mount</label><div class=chs>{"".join(f'<span class="{"on" if s=="White 2 in" else ""}">{s}</span>' for s in ["None","White 2 in","Cream 2 in"])}</div></div>
<div class=row2><label>Glass</label><div class=chs>{"".join(f'<span class="{"on" if s=="Clear glass" else ""}">{s}</span>' for s in ["Clear glass","Non-glare","Acrylic"])}</div></div>
<div class=row2><label>Photo</label><div class=up>{ic("img",24)}<span>Customer photo added · sample</span></div></div>
<div class=row2><label>Back</label><div class=chs>{"".join(f'<span class="{"on" if s=="Wall hook" else ""}">{s}</span>' for s in ["Wall hook","Table stand"])}</div></div>
<div class=row2><label>Pickup</label><div class=up>{ic("cal",24)}<span>Sat 28 Nov, after 4 PM</span></div></div>
<div class=bt2>Save order and send preview</div></div></div></div>''',
css=""".w2{flex:1;display:flex;min-height:0}
.tb{flex:1;background:#1d1714;border-radius:40px;padding:22px;box-shadow:0 30px 60px rgba(43,29,20,.25);display:flex}
.sc{flex:1;background:#fff;border-radius:22px;padding:24px 28px;display:flex;flex-direction:column;gap:16px}
.hd2{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}.hd2 small{display:block;font:600 14px/1.4 Inter;letter-spacing:1.5px;color:#8a7a68}.hd2 b{font:700 36px/1.3 Cardo}
.row2{display:flex;align-items:center;gap:16px}.row2 label{width:130px;flex:none;font:600 20px Inter;color:#5a4a3c}
.chs{flex:1;display:flex;gap:8px}.chs span{flex:1;text-align:center;border:2px solid #e6ddd0;border-radius:12px;padding:11px 4px;font:600 18px Inter}.chs .on{background:#7a4a2a;border-color:#7a4a2a;color:#fff}
.mg{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:10px}.mg div{border:2px solid #e6ddd0;border-radius:14px;padding:8px;display:flex;flex-direction:column;gap:6px}
.mg svg{width:100%;height:46px;display:block;border-radius:6px}.mg span{font:600 16px/1.3 Inter}.mg .on{border-color:#a8822e;box-shadow:0 0 0 3px #a8822e}
.up{flex:1;display:flex;gap:10px;align-items:center;border:2px dashed #d9c39a;border-radius:12px;padding:11px 14px;font:500 18px Inter;color:#5a4a3c}
.bt2{margin-top:auto;background:#2b1d14;color:#fff;border-radius:14px;padding:16px;text-align:center;font:600 21px Inter}""")

# preview: 12x18 photo + 2 in mount each side => 16 x 22 outer of mount; draw at 20 px/in
P["p212_frame_s3"] = fb(3, "PART 2 · PREVIEW LINK", "Customer sees the frame<br><span>before you cut it.</span>",
f'''<div class=w3><div class=pv><div class=dimv><i></i><span>22 in</span><i></i></div><div class=pvc>
<div class=fr style="width:{16*20+40}px;height:{22*20+40}px;border-width:20px;border-color:#6b4126"><div class=mt style="inset:0"></div><div class=ph style="inset:40px">{land("b")}</div></div>
<div class=dimh><i></i><span>16 in</span><i></i></div></div></div>
<div class=sd><div class="cd it"><small>ORDER F-301 · SAMPLE</small>{"".join(f'<p><span>{a}</span><b>{b}</b></p>' for a,b in [("Photo","12 x 18 in"),("Mount","White, 2 in"),("Outer size","16 x 22 in"),("Moulding","Walnut 1 in"),("Glass","Clear")])}</div>
<div class=ap3><small>CUSTOMER REPLY · THU 26 NOV</small><b>“Looks perfect. Go ahead.”</b><span class="stF sG">Approved</span></div></div></div>''',
css=""".w3{flex:1;display:flex;gap:18px;min-height:0}
.pv{flex:1;background:#e9e1d3;border-radius:28px;display:flex;align-items:center;justify-content:center;gap:14px;padding:16px}
.pvc{display:flex;flex-direction:column;align-items:center;gap:12px}
.dimv{display:flex;flex-direction:column;align-items:center;height:{22*20+40}px;gap:8px}.dimv i{flex:1;width:3px;background:#a8822e}.dimv span,.dimh span{font:700 18px Inter;color:#7a4a2a;white-space:nowrap}
.dimh{display:flex;align-items:center;width:{16*20+40}px;gap:8px}.dimh i{flex:1;height:3px;background:#a8822e}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:14px}
.it{flex:1;padding:18px 22px;display:flex;flex-direction:column;justify-content:space-between}.it small{margin-bottom:6px}.it small,.ap3 small{font:600 14px/1.4 Inter;letter-spacing:1.5px;color:#8a7a68}
.it p{display:flex;justify-content:space-between;border-top:1px solid #efe7da;padding-top:14px;font:500 22px Inter;color:#5a4a3c}.it b{color:#2b1d14;font-weight:700}
.ap3{background:#2b1d14;color:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:8px}.ap3 small{color:#d9c39a}.ap3 b{font:700 27px/1.3 Cardo}.ap3 .stF{align-self:flex-start}""".replace("{22*20+40}", str(22*20+40)).replace("{16*20+40}", str(16*20+40)))

jobs212 = [("F-298", "8 x 10 in · Black flat", "Ready", "sR"), ("F-299", "5 x 7 in · Gold leaf", "Glass cutting", "sC"), ("F-300", "8 x 12 in · Natural oak", "Mounting", "sC"), ("F-301", "12 x 18 in · Walnut", "Approved, cutting", "sG")]
P["p212_frame_s4"] = fb(4, "PART 3 · READY ALERT", "Frame ready?<br><span>The customer knows first.</span>",
f'''<div class=w4><div class="cd jl"><div class=jh><small>TODAY'S BENCH · SAT 28 NOV · SAMPLE</small></div>
{"".join(f'<div class=jr><b>{a}</b><span>{b}</span><em class="stF {k}">{c}</em></div>' for a,b,c,k in jobs212)}</div>
<div class=bt4><div class=ms4><small>TEXT TO SAMPLE CUSTOMER · 4:10 PM</small><p>Your frame F-298 is ready. Pickup till 8 PM today. Your shop.</p></div>
<div class=mini>{frame(8*16, 10*16, 9, 10, "#1f1a17")}<span class="stF sR">F-298 ready</span></div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.jl{flex:1;padding:16px 24px;display:flex;flex-direction:column}.jh{padding-bottom:10px;border-bottom:2px solid #efe7da}.jh small{font:600 14px/1.4 Inter;letter-spacing:1.5px;color:#8a7a68}
.jr{flex:1;display:grid;grid-template-columns:130px 1fr auto;align-items:center;gap:14px;border-bottom:1px solid #f2ece2}.jr:last-child{border:0}
.jr b{font:700 32px/1.3 Cardo}.jr span{font:500 20px Inter;color:#5a4a3c}.jr .stF{font-size:18px;padding:7px 14px}
.bt4{display:flex;gap:14px;align-items:stretch}
.ms4{flex:1;background:#2b1d14;color:#fff;border-radius:24px;padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px}.ms4 small{font:600 14px/1.4 Inter;letter-spacing:1.5px;color:#d9c39a}.ms4 p{font:500 23px/1.45 Inter}
.mini{width:230px;flex:none;background:#e9e1d3;border-radius:24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px;padding:16px}""")

P["p212_frame_s5"] = fb(5, "YOUR TURN", "Run a photo frame shop?<br><span>Let's build your order app.</span>",
f'''<div class=w5><div class=wl5>{frame(10*22, 14*22, 16, 18, "#6b4126")}</div><div class=t5>{"".join(f'<div><span class=ib>{ic(i,32)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b in [("grid","Order form","Size, moulding, glass"),("img","Preview link","Approve before cutting"),("doc","Bench list","Every job's stage"),("bell","Ready alert","Customer told at once")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#7a4a2a;color:#fff",
css=""".w5{flex:1;display:flex;gap:16px;min-height:0}.wl5{width:380px;flex:none;background:#e9e1d3;border-radius:28px;display:flex;align-items:center;justify-content:center}
.t5{flex:1;display:grid;grid-template-rows:repeat(4,1fr);gap:12px}.t5 div{background:#2b1d14;color:#fff;border-radius:22px;padding:14px 20px;display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:16px;align-content:center}
.t5 div:nth-child(2n){background:#7a4a2a}.t5 .ib{grid-row:span 2;width:76px;height:76px;border-radius:16px;background:rgba(255,255,255,.12)}.t5 b{font:700 36px/1.3 Cardo}.t5 small{font:400 20px/1.35 Inter;color:#eadccb}""")

# ───────── 213 USA · Mobile notary · SINGLE · Crimson Text + DM Sans · navy ink / parchment / seal red · PHONE
# New technique: travel-area rings map (concentric zones around the base) next to a booking phone; seal stamp badge.
rings = '''<svg viewBox="0 0 440 520" class=mp><rect width="440" height="520" fill="#efe6d2"/>
<g stroke="#d9ccb0" stroke-width="10" fill="none"><path d="M0 120 L440 150"/><path d="M0 380 Q220 330 440 400"/><path d="M130 0 L170 520"/><path d="M330 0 Q300 260 350 520"/></g>
<circle cx="220" cy="260" r="200" fill="#1e2b4a" fill-opacity=".06" stroke="#1e2b4a" stroke-width="3" stroke-dasharray="10 8"/>
<circle cx="220" cy="260" r="110" fill="#1e2b4a" fill-opacity=".10" stroke="#1e2b4a" stroke-width="3"/>
<circle cx="220" cy="260" r="16" fill="#1e2b4a"/><circle cx="220" cy="260" r="6" fill="#fff"/>'''
for n, (x, y) in enumerate([(150, 210), (300, 330), (360, 140)], 1):
    rings += f'<circle cx="{x}" cy="{y}" r="20" fill="#b3362c" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y+7}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="20" fill="#fff"><tspan>{n}</tspan></text>'
rings += '</svg>'
P["p213_notary"] = page("""
body{--f:'DM Sans';--h:'Crimson Text';background:#f5efe2;color:#1e2b4a}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b3362c;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b3362c}
.vw{flex:1;display:flex;gap:18px;min-height:0;align-items:stretch}
.lf{flex:none;display:flex;align-items:center}
.ap{flex:1;padding:6px 18px 18px;display:flex;flex-direction:column;gap:11px;background:#fbf8f1}
.ap h4{font:700 22px/1.3 'DM Sans';color:#1e2b4a}.ap small{font:700 12px/1.4 'DM Sans';letter-spacing:1.5px;color:#7a7f8c}
.op{display:flex;flex-direction:column;gap:6px}.op span{border:2px solid #e3dccb;border-radius:12px;padding:9px 12px;font:600 15px 'DM Sans';background:#fff}.op .on{border-color:#1e2b4a;background:#1e2b4a;color:#fff}
.zp{border:2px solid #e3dccb;border-radius:12px;padding:9px 12px;font:600 15px 'DM Sans';background:#fff;display:flex;justify-content:space-between}.zp em{font-style:normal;color:#2e7d4f}
.sl{display:grid;grid-template-columns:1fr 1fr;gap:6px}.sl span{text-align:center;border:2px solid #e3dccb;border-radius:10px;padding:8px 0;font:600 15px 'DM Sans';background:#fff}.sl .on{background:#b3362c;border-color:#b3362c;color:#fff}.sl .x{color:#b9b2a3;text-decoration:line-through}
.idn{display:flex;gap:8px;align-items:center;background:#fdf1d8;border-radius:10px;padding:8px 10px;font:600 14px/1.35 'DM Sans';color:#7a5a1a}
.bt{margin-top:auto;background:#1e2b4a;color:#fff;border-radius:12px;padding:13px;text-align:center;font:700 16px 'DM Sans'}
.rt{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.mpw{flex:1;min-height:0;background:#fff;border-radius:24px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 12px 26px rgba(30,43,74,.08)}
.mpw small{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7a7f8c}
.mp{width:100%;flex:1;min-height:0;display:block;border-radius:16px}
.lgd{display:flex;gap:14px;font:600 15px 'DM Sans';color:#4a5470}.lgd span{display:flex;align-items:center;gap:6px}.lgd i{width:16px;height:16px;border-radius:50%;border:3px solid #1e2b4a}.lgd .d{border-style:dashed}
.dy{background:#1e2b4a;color:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px}
.dy small{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#c9cfe0}
.dy p{display:flex;gap:10px;align-items:center;font:500 18px/1.3 'DM Sans'}.dy p i{font-style:normal;width:28px;height:28px;border-radius:50%;background:#b3362c;display:flex;align-items:center;justify-content:center;font:700 15px 'DM Sans';flex:none}.dy p b{margin-left:auto;font-weight:700}
""", "<div class=kk>MOBILE NOTARIES · BOOKINGS</div><h1>Booking calls while<br>you drive? <span>Let clients<br>book the visit.</span></h1>",
f'''<div class=vw><div class=lf>{phone(f"""<div class=ap><h4>Book a notary visit</h4><small>SAMPLE BOOKING PAGE</small>
<div class=op><span>Affidavit</span><span class=on>Power of attorney</span><span>Real estate signing</span></div>
<div class=zp><span>ZIP 12345</span><em>In service area</em></div><div class=zp><span>Signers</span><b>2</b></div><div class=zp><span>Meet at</span><b>Home</b></div>
<div class=sl><span class=x>9:00 AM</span><span>11:00 AM</span><span class=on>2:00 PM</span><span>4:30 PM</span></div>
<div class=idn>{ic("card",18)}Bring a valid photo ID. Do not sign before the visit.</div>
<div class=bt>Book Wed, Dec 2 · 2 PM</div></div>""", w=340, h=730)}</div>
<div class=rt><div class=mpw><small>TRAVEL AREA · SAMPLE</small>{rings}<div class=lgd><span><i></i>Zone 1</span><span><i class=d></i>Zone 2</span><span style="margin-left:auto">Wed, Dec 2</span></div></div>
<div class=dy><small>YOUR WEDNESDAY · 3 VISITS</small><p><i>1</i>Affidavit · Zone 1<b>10 AM</b></p><p><i>2</i>Power of attorney · Zone 2<b>2 PM</b></p><p><i>3</i>Real estate signing · Zone 2<b>5 PM</b></p></div></div></div>''',
"#1e2b4a", "Mobile notary? DM us", "background:#b3362c;color:#fff")

# ───────── 214 INDIA · Rubber stamp maker · SINGLE · Bitter + DM Sans · stamp violet / kraft / black
# New technique: circular stamp impressions with SVG textPath + feTurbulence ink texture; proof 1 vs proof 2 with a correction pin.
def stamp(pid, outer, inner, mid, ink="#4b3a8f", miss=False):
    return f'''<svg viewBox="0 0 300 300" class=stp><defs><filter id="ink{pid}"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="{len(pid)}"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.9 1.45"/><feComposite in="SourceGraphic" operator="in"/></filter>
<path id="tp{pid}" d="M150 150 m-104 0 a104 104 0 1 1 208 0 a104 104 0 1 1 -208 0"/><path id="bp{pid}" d="M150 150 m-112 0 a112 112 0 0 0 224 0"/></defs>
<g filter="url(#ink{pid})" fill="{ink}" stroke="{ink}"><circle cx="150" cy="150" r="138" fill="none" stroke-width="8"/><circle cx="150" cy="150" r="80" fill="none" stroke-width="4"/>
<text font-family="Bitter" font-weight="800" font-size="24" letter-spacing="2" stroke="none"><textPath href="#tp{pid}" startOffset="25%" text-anchor="middle">{outer}</textPath></text>
<text font-family="Bitter" font-weight="700" font-size="22" letter-spacing="2" stroke="none"><textPath href="#bp{pid}" startOffset="50%" text-anchor="middle">{inner}</textPath></text>
<text x="150" y="150" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="23" stroke="none"><tspan>{mid[0]}</tspan></text><text x="150" y="182" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" stroke="none"><tspan>{mid[1]}</tspan></text></g></svg>'''
P["p214_stamp"] = page("""
body{--f:'DM Sans';--h:'Bitter';background:#e8d9bd;color:#1c1a22}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#4b3a8f;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:66px;letter-spacing:-1px;line-height:1.2} h1 span{color:#4b3a8f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pr{flex:1;min-height:0;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.pf{background:#fffdf8;border-radius:26px;padding:18px 20px;display:flex;flex-direction:column;align-items:center;gap:10px;position:relative;box-shadow:0 12px 26px rgba(28,26,34,.1)}
.pf header{align-self:stretch;display:flex;justify-content:space-between;align-items:center}
.pf small{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7c7466}
.pf .ch{font:700 16px 'DM Sans';border-radius:10px;padding:5px 11px}
.c1{background:#f6dcd6;color:#9b2f22}.c2{background:#4b3a8f;color:#fff}
.stp{width:370px;height:370px;display:block;margin:auto 0}
.cm{align-self:stretch;border-radius:16px;padding:14px 16px;font:500 21px/1.4 'DM Sans'}
.cm b{display:block;font:700 14px/1.4 'DM Sans';letter-spacing:1.5px;margin-bottom:2px}
.cm1{background:#fbeeea;color:#6b2a20}.cm2{background:#eeebf8;color:#2f2560}
.pin{position:absolute;top:215px;right:30px;width:46px;height:46px;border-radius:50%;background:#c0392b;color:#fff;font:800 24px/46px Bitter;text-align:center;box-shadow:0 0 0 6px rgba(192,57,43,.2)}
.tl{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.tl div{background:#1c1a22;color:#fff;border-radius:18px;padding:12px 16px}
.tl small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:1.5px;color:#b9b1d9}.tl b{display:block;font:700 24px/1.3 Bitter}.tl span{font:500 16px 'DM Sans';color:#d6d2e4}
.tl .on{background:#4b3a8f}
""", "<div class=kk>RUBBER STAMP MAKERS · ORDER S-77</div><h1>A mistake on the stamp?<br><span>Get the proof approved first.</span></h1>",
f'''<div class=vw><div class=pr>
<div class=pf><header><small>PROOF 1 · 10:05 AM</small><span class="ch c1">Change asked</span></header>{stamp("a","SAMPLE TRADERS","YOUR CITY",("PROPRIETOR",""),"#4b3a8f")}<span class=pin>!</span>
<div class="cm cm1"><b>CUSTOMER NOTE</b>Please add “Shop 4” in the middle.</div></div>
<div class=pf><header><small>PROOF 2 · 11:20 AM</small><span class="ch c2">Approved</span></header>{stamp("bb","SAMPLE TRADERS","YOUR CITY",("PROPRIETOR","SHOP 4"),"#4b3a8f")}
<div class="cm cm2"><b>CUSTOMER REPLY</b>“Yes, this is correct. Please make it.”</div></div></div>
<div class=tl><div><small>ORDER</small><b>10:00 AM</b><span>Text and size</span></div><div><small>PROOF 1</small><b>10:05 AM</b><span>Change asked</span></div><div><small>PROOF 2</small><b>11:20 AM</b><span>Approved</span></div><div class=on><small>READY</small><b>4:00 PM</b><span>Pickup alert sent</span></div></div></div>''',
"#1c1a22", "Make stamps? DM us", "background:#4b3a8f;color:#fff")

# ───────── 215 INDIA · Tempo traveller rental · SINGLE · Archivo Black + Roboto · asphalt / lane yellow / sky
# New technique: horizontal road ribbon timeline (asphalt band with dashed lane line) with day pins and odometer readouts; log totals derived.
days = [("Day 1 · Fri 4 Dec", "Start 6:00 AM", "45,210 km", "Pickup at sample address"), ("Day 2 · Sat 5 Dec", "Local sightseeing", "45,560 km", "Night stay: driver"), ("Day 3 · Sun 6 Dec", "Return 9:30 PM", "46,080 km", "Drop at sample address")]
P["p215_tempo"] = page("""
body{--f:'Roboto';--h:'Archivo Black';background:#dcebf5;color:#1e2226}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#c58a00;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:60px;letter-spacing:-1px;line-height:1.22} h1 span{color:#2c6e9b}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.rd{background:#fff;border-radius:28px;padding:18px 24px 18px;box-shadow:0 12px 28px rgba(30,34,38,.08)}
.rd>small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6b7680}
.rbw{position:relative;padding-top:52px;margin:8px 0 16px}.rb{position:relative;height:74px;background:#33383d;border-radius:12px}
.rb:after{content:"";position:absolute;left:14px;right:14px;top:35px;height:5px;background:repeating-linear-gradient(90deg,#ffc928 0 34px,transparent 34px 58px)}
.pn{position:absolute;top:0;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;z-index:2}
.pn b{background:#ffc928;color:#1e2226;font:400 18px/1.3 'Archivo Black';border-radius:12px;padding:6px 12px;white-space:nowrap}
.pn i{width:4px;height:44px;background:#ffc928}
.cols{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.cols div{border-radius:18px;background:#f2f6f9;padding:12px 16px;display:flex;flex-direction:column;gap:3px}
.cols small{font:700 14px/1.4 'Roboto';letter-spacing:1.5px;color:#2c6e9b}.cols b{font:400 26px/1.35 'Archivo Black'}.cols span{font:500 17px/1.35 'Roboto';color:#56606a}
.cols .od{flex-direction:row;background:none;padding:0;border-radius:0;gap:4px;align-self:flex-start;margin:4px 0}.od em{font-style:normal;background:#1e2226;color:#ffc928;font:700 26px/1.3 'Roboto';width:32px;text-align:center;border-radius:4px;padding:3px 0}
.lg2{flex:1;min-height:0;display:grid;grid-template-columns:1.1fr 1fr;gap:14px}
.tt{background:#1e2226;color:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;justify-content:space-between}
.tt small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#ffc928}
.tt p{display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid #3a4046;padding-top:10px;font:500 22px 'Roboto';color:#c9d1d8}.tt p b{font:400 34px/1.3 'Archivo Black';color:#fff}
.dr{display:flex;flex-direction:column;gap:12px}
.dc{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;gap:14px;align-items:center}
.dc .ib{width:54px;height:54px;border-radius:14px;background:#dcebf5;color:#2c6e9b}
.dc small{display:block;font:700 14px/1.4 'Roboto';letter-spacing:1.5px;color:#6b7680}.dc b{display:block;font:400 26px/1.3 'Archivo Black'}.dc span{font:500 18px 'Roboto';color:#56606a}
""", "<div class=kk>TEMPO TRAVELLER RENTAL · TRIP T-42</div><h1>Trip km and tolls<br>in a diary?<br><span>Log every trip day.</span></h1>",
f'''<div class=vw><div class=rd><small>3-DAY SAMPLE TRIP · 12-SEATER · SAMPLE VEHICLE</small>
<div class=rbw>{"".join(f'<div class=pn style="left:{x}%"><b>{t}</b><i></i></div>' for x,t in [(10,"Start"),(50,"Day 2"),(90,"Return")])}<div class=rb></div></div>
<div class=cols>{"".join(f'<div><small>{a.upper()}</small><b>{b}</b><div class=od>{"".join(f"<em>{c}</em>" for c in o.replace(",","").replace(" km",""))}</div><span>{d}</span></div>' for a,b,o,d in days)}</div></div>
<div class=lg2><div class=tt><small>TRIP LOG · AUTO TOTALS</small><p>Distance<b>870 km</b></p><p>Trip time<b>3 days</b></p><p>Toll slips<b>6 photos</b></p><p>Driver nights<b>2</b></p></div>
<div class=dr><div class=dc><span class=ib>{ic("users",28)}</span><div><small>DRIVER</small><b>Sample driver</b><span>Duty sheet signed daily</span></div></div>
<div class=dc><span class=ib>{ic("doc",28)}</span><div><small>BILL</small><b>Made from the log</b><span>Sent to the customer</span></div></div>
<div class=dc><span class=ib>{ic("cal",28)}</span><div><small>NEXT TRIP</small><b>Wed 9 Dec</b><span>Same vehicle, booked</span></div></div></div></div></div>''',
"#1e2226", "Rent out tempos? DM us", "background:#2c6e9b;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
