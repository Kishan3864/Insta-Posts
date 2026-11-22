import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 286 INDIA · Ironing service (press wala) · SINGLE · Lora + Poppins · starch white / indigo / ember orange
# New technique: CSS folded-clothes stacks (each garment a folded block with a collar or waistband), one stack per flat with a count tag.
GC = {"shirt": ("#ffffff", "#6d7fc9"), "trouser": ("#2f3a6b", "#1d2650"), "saree": ("#e0603a", "#b8431f"), "sheet": ("#cfe3f4", "#9bbcd8")}
def stack(items):
    out = []
    for kind, n in items:
        c, e = GC[kind]
        for i in range(n):
            out.append(f'<div class="gm {kind}" style="background:{c};border-color:{e}"></div>')
    return "".join(reversed(out))
flats = [("Flat 101", [("sheet", 2), ("trouser", 3), ("shirt", 8)], "Ready", "r"), ("Flat 204", [("saree", 2), ("trouser", 2), ("shirt", 4)], "Ready 6 PM", "w"), ("Flat 305", [("trouser", 4), ("shirt", 7)], "Picked 9 AM", "p")]
P["p286_ironing"] = page("""
body{--f:'Poppins';--h:'Lora';background:#f6f3ec;color:#1e2550}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#d1572a;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:66px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#3b4a9e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sh{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.fc{background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(30,37,80,.08)}
.fh{display:flex;justify-content:space-between;align-items:center}.fh b{font:700 28px/1.3 Lora}.fh em{font:600 14px 'Poppins';font-style:normal;padding:5px 10px;border-radius:8px}
.r .fh em{background:#e1f1e4;color:#2c7a3f}.w .fh em{background:#fde6dc;color:#b8431f}.p .fh em{background:#e5e8f7;color:#3b4a9e}
.st{flex:1;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:3px;background:#f1eee6;border-radius:16px;padding:12px 12px 16px}
.gm{width:250px;height:36px;border-radius:6px;border:3px solid;position:relative;flex:none}
.gm.shirt:after{content:"";position:absolute;left:50%;top:-3px;width:44px;height:12px;margin-left:-22px;border-radius:0 0 22px 22px;border:3px solid #6d7fc9;border-top:0;background:#eef1fb}
.gm.trouser:after{content:"";position:absolute;left:12px;right:12px;top:4px;height:4px;background:#5a6aa8;border-radius:2px}
.gm.saree:after{content:"";position:absolute;left:0;right:0;bottom:3px;height:5px;background:#f2c14e}
.ct{display:grid;grid-template-columns:repeat(2,1fr);gap:6px}.ct span{display:flex;align-items:center;gap:8px;font:600 17px 'Poppins';background:#f6f3ec;border-radius:10px;padding:6px 10px}.ct i{width:16px;height:16px;border-radius:4px;border:2px solid}
.tt{font:700 18px 'Poppins';text-align:center;background:#1e2550;color:#fff;border-radius:12px;padding:8px}
.bt{display:grid;grid-template-columns:1.3fr 1fr;gap:12px}
.bx{background:#1e2550;color:#fff;border-radius:22px;padding:16px 20px}.bx small{display:block;font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#f6b79e}.bx b{display:block;font:700 26px/1.3 Lora;margin:2px 0}.bx span{font:500 17px/1.4 'Poppins';color:#cfd3ec}
.bx.o{background:#d1572a}.bx.o small{color:#ffe1d3}.bx.o span{color:#fff1ea}
""", "<div class=kk>IRONING SERVICE · SOCIETY PICKUPS</div><h1>“I gave 8 shirts, not 6!”<br><span>Count them at the door.</span></h1>",
f'''<div class=vw><div class=sh>{"".join(f'<div class="fc {k}"><div class=fh><b>{f}</b><em>{st}</em></div><div class=st>{stack(it)}</div><div class=ct>{"".join(f"<span><i style={chr(34)}background:{GC[g][0]};border-color:{GC[g][1]}{chr(34)}></i>{n} {g if n==1 else (g+'s')}</span>" for g,n in it)}</div><div class=tt>{sum(n for _,n in it)} pieces · sample</div></div>' for f,it,st,k in flats)}</div>
<div class=bt><div class=bx><small>AT PICKUP</small><b>Count + one photo</b><span>The flat gets the count on its phone right away.</span></div><div class="bx o"><small>MONTH END</small><b>Bill by count</b><span>Sent on the 1st, sample.</span></div></div></div>''',
"#1e2550", "Run an ironing service? DM us", "background:#d1572a;color:#fff")

# ───────── 287 INDIA · Cold storage · CAROUSEL 5 · Bitter + Roboto · ice blue / jute brown / charcoal
# New technique: top-down chamber map with rack bays tinted by lot; jute-bag isotype (1 bag icon = 50 bags) for in/out ledger.
CS = """
body{--f:'Roboto';--h:'Bitter';background:#e9f1f6;color:#1f2a30}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#8a5a2b;margin-top:22px;align-self:flex-start}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#2f7db0}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(31,42,48,.08)}
.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6f7a80}
.nb{display:flex;align-items:center;gap:14px;background:#1f2a30;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Roboto'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#2f7db0}.nb b{color:#f1cf9b}
.bag{width:34px;height:42px;border-radius:8px 8px 12px 12px;background:repeating-linear-gradient(0deg,#b98a55 0 5px,#a87843 5px 7px);border:2px solid #7a5329;position:relative;flex:none}
.bag:before{content:"";position:absolute;top:-2px;left:8px;right:8px;height:7px;border-radius:0 0 6px 6px;background:#7a5329}
"""
def cs(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f2a30;color:#fff"):
    return page(CS + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f2a30", cta, ctacss, tagline=f"{n} / 5")
LOT = {"L-12": "#f2c14e", "L-15": "#7cc3a0", "L-18": "#e98a6b", "L-21": "#9bb4e8", "": "#eef3f6"}
ch2 = [["L-12", "L-12", "L-15", "L-15"], ["L-12", "L-18", "L-18", ""], ["L-21", "L-21", "L-18", ""]]
def bays(grid, sel=None):
    return "".join(f'<div class=rk><b>Rack {"ABC"[r]}</b><div class=bys>{"".join(f"<i class={chr(34)}{chr(115) if l==sel else chr(32)}{chr(34)} style={chr(34)}background:{LOT[l]}{chr(34)}>{l or 'Empty'}</i>" for l in row)}</div></div>' for r, row in enumerate(grid))
P["p287_coldstore_s1"] = cs(1, "COLD STORAGE · LOTS AND CHAMBERS", "“Where are my 450 bags?”<br><span>Answer in one tap.</span>",
f'''<div class=w1><div class="cd mp"><div class=mh><b>Chamber 2</b><span>Sample cold store · top view</span></div>{bays(ch2, "L-18")}<div class=dr2>DOOR</div></div>
<div class=sd><div class="cd lt"><small class=cap>LOT L-18 · SAMPLE</small><b>450 bags</b><span>Farmer F-207 · potatoes</span><div class=wh>Chamber 2 · Rack B, C</div><div class=lr1><span>Entry</span><b>Mon 16 Nov</b></div><div class=lr1><span>Bag size</span><b>50 kg</b></div><div class=lr1><span>Bags left today</span><b>300</b></div></div>
<div class="cd lg5">{"".join(f'<span><i style="background:{c}"></i>{l or "Empty bay"}</span>' for l,c in LOT.items())}</div></div></div>''',
css=""".w1{flex:1;display:flex;gap:14px;min-height:0}.mp{flex:1;min-width:0;padding:18px;display:flex;flex-direction:column;gap:12px;background:#f7fbfd;box-shadow:inset 0 0 0 6px #b9d4e6,0 12px 28px rgba(31,42,48,.08)}
.mh b{font:800 30px/1.3 Bitter}.mh span{display:block;font:500 17px Roboto;color:#6f7a80}
.rk{flex:1;display:flex;flex-direction:column;gap:6px}.rk b{font:700 15px/1.4 Roboto;letter-spacing:2px;color:#6f7a80}
.bys{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.bys i{border-radius:10px;font:700 18px Roboto;font-style:normal;display:flex;align-items:center;justify-content:center;border:2px solid rgba(0,0,0,.08)}.bys i.s{border:4px solid #1f2a30}
.dr2{align-self:center;width:200px;text-align:center;font:700 15px/1.4 Roboto;letter-spacing:4px;background:#1f2a30;color:#fff;border-radius:10px;padding:8px}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}.lt{flex:1;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.lt b{font:800 64px/1.3 Bitter;color:#8a5a2b}.lt span{font:500 19px Roboto;color:#4d585e}.wh{margin-top:10px;background:#1f2a30;color:#fff;border-radius:12px;padding:12px 14px;font:700 19px Roboto}
.lr1{display:flex;justify-content:space-between;border-bottom:1px solid #e6edf1;padding:10px 0;font:500 17px Roboto;color:#4d585e}.lt .lr1 b{color:#1f2a30;font:700 19px Roboto}.lt .lr1 span{font:500 17px Roboto}.lg5{padding:16px 20px;display:flex;flex-direction:column;gap:8px}.lg5 span{display:flex;align-items:center;gap:10px;font:600 18px Roboto}.lg5 i{width:22px;height:22px;border-radius:6px;border:2px solid rgba(0,0,0,.1)}""")

P["p287_coldstore_s2"] = cs(2, "STEP 1 · A LOT CARD AT THE GATE", "Every load gets<br><span>its own lot number.</span>",
f'''<div class=w2><div class="cd lc"><div class=lh><div><small class=cap>LOT CARD · SAMPLE</small><b>L-18</b></div><div class=qr2>{"".join(f'<i style="background:{"#1f2a30" if (i*7+i//5)%3 else "#fff"}"></i>' for i in range(49))}</div></div>
<div class=kv2>{"".join(f"<div><small>{a}</small><b>{b}</b></div>" for a,b in [("FARMER","F-207"),("CROP","Potato"),("BAGS IN","450"),("BAG SIZE","50 kg"),("ENTRY","Mon 16 Nov"),("PLACE","Ch 2 · Rack B, C")])}</div></div>
<div class=nb><span class=ib>{ic("send",26)}</span><span>The farmer gets the lot card by message, <b>so the bag count is never in doubt.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.lc{flex:1;padding:24px 28px;display:flex;flex-direction:column;gap:18px;border-top:12px solid #8a5a2b}
.lh{display:flex;justify-content:space-between;align-items:center}.lh b{display:block;font:800 96px/1.2 Bitter;color:#8a5a2b}
.qr2{display:grid;grid-template-columns:repeat(7,26px);gap:3px;padding:10px;border:3px solid #1f2a30;border-radius:10px}.qr2 i{width:26px;height:26px;border-radius:3px}
.kv2{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}.kv2 div{background:#eef4f8;border-radius:16px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center}
.kv2 small{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#6f7a80}.kv2 b{font:800 34px/1.3 Bitter}""")

led = [("Mon 16 Nov", "In", 450), ("Fri 20 Nov", "Out", 100), ("Sat 21 Nov", "Out", 50)]
P["p287_coldstore_s3"] = cs(3, "STEP 2 · BAGS IN AND OUT, PER LOT", "One bag icon = 50 bags.<br><span>No register needed.</span>",
f'''<div class=w3><div class="cd lg6">{"".join(f'<div class="lr {t.lower()}"><div class=ld><small>{d}</small><b>{t}</b></div><div class=bg6>{"<div class=bag></div>"*(n//50)}</div><em>{"+" if t=="In" else "−"}{n}</em></div>' for d,t,n in led)}
<div class="lr bal"><div class=ld><small>TODAY</small><b>Left</b></div><div class=bg6>{"<div class=bag></div>"*6}</div><em>300</em></div></div>
<div class=nb><span class=ib>{ic("box",26)}</span><span>Lot L-18: 450 in, 150 out, <b>300 bags still in Chamber 2.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.lg6{flex:1;padding:16px 24px;display:flex;flex-direction:column}
.lr{flex:1;display:grid;grid-template-columns:170px 1fr 110px;gap:16px;align-items:center;border-bottom:1px solid #e6edf1}.lr:last-child{border:0}
.ld small{display:block;font:700 15px/1.4 Roboto;color:#6f7a80}.ld b{font:800 30px/1.3 Bitter}
.bg6{display:flex;flex-wrap:wrap;gap:12px}.bg6 .bag{width:46px;height:58px}.lr em{font:800 34px/1.3 Bitter;font-style:normal;text-align:right}
.in em{color:#2f7db0}.out em{color:#c0573b}.bal{background:#fff7e8;border-radius:16px;padding:0 12px}.bal em{color:#8a5a2b}""")

P["p287_coldstore_s4"] = cs(4, "STEP 3 · WITHDRAWAL SLIP AND LOADING SLOT", "Farmer asks for 100 bags.<br><span>The crew knows where.</span>",
f'''<div class=w4><div class="cd rq"><small class=cap>REQUEST FROM FARMER F-207 · SAMPLE</small><div class=bb4><span>Please send <b>100 bags</b> from lot L-18 on <b>Tue 24 Nov</b>. Truck comes at 8 AM.</span></div><div class="bb4 rp"><span>OK. Slip <b>W-311</b> is ready. Loading at Rack C, 8 to 9 AM.</span></div><div class=bb4><span>Thanks. Truck number sent.</span></div>
<div class=sl4>{"".join(f'<span class={"on" if t=="8–9 AM" else ""}>{t}</span>' for t in ["7–8 AM","8–9 AM","9–10 AM","10–11 AM"])}</div></div>
<div class="cd ws4"><small class=cap>WITHDRAWAL SLIP W-311</small>{"".join(f'<div class=wr4><span>{a}</span><b>{b}</b></div>' for a,b in [("Lot","L-18"),("Bags","100"),("From","Chamber 2 · Rack C"),("Loading","Tue 24 Nov · 8 AM"),("Left after","200 bags")])}</div></div>''',
css=""".w4{flex:1;display:flex;gap:14px;min-height:0}.rq{flex:1;min-width:0;padding:20px;display:flex;flex-direction:column;gap:16px}
.bb4{background:#eef4f8;border-radius:20px 20px 20px 6px;padding:24px;font:500 28px/1.5 Roboto}.bb4.rp{background:#1f2a30;color:#fff;border-radius:20px 20px 6px 20px;margin-left:40px}.bb4.rp b{color:#f1cf9b}.sl4{margin-top:auto}.bb4 b{color:#2f7db0}
.sl4{display:grid;grid-template-columns:1fr 1fr;gap:10px}.sl4 span{text-align:center;font:700 20px Roboto;padding:14px 4px;border-radius:14px;border:3px solid #dbe6ed}.sl4 span.on{border-color:#2f7db0;background:#e3f0f8;color:#1d5f8c}
.ws4{width:400px;flex:none;padding:20px 24px;display:flex;flex-direction:column;background:#1f2a30;color:#fff}.ws4 .cap{color:#f1cf9b}
.wr4{flex:1;display:flex;flex-direction:column;justify-content:center;border-bottom:1px dashed #4a575e}.wr4:last-child{border:0}.wr4 span{font:500 17px Roboto;color:#b9c3c8}.wr4 b{font:800 30px/1.3 Bitter}""")

P["p287_coldstore_s5"] = cs(5, "YOUR TURN", "Run a cold storage?<br><span>Let's map your chambers.</span>",
f'''<div class=w5><div class="cd hp5">{"".join('<div class=bag></div>' for _ in range(16))}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Chamber map","Every lot in its bay"),("doc","Lot cards","Sent to the farmer"),("chart","In and out","Bags left, live"),("truck","Withdrawal slips","With loading slots")])}</div>
<div class=q>How do farmers check their bag count with you today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#2f7db0;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;display:flex;flex-wrap:wrap;align-content:center;justify-content:center;gap:18px 22px;padding:24px 60px}.hp5 .bag{width:80px;height:100px;border-radius:14px 14px 22px 22px}.hp5 .bag:before{left:20px;right:20px;height:14px}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(31,42,48,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#e3f0f8;color:#2f7db0}.ti b{display:block;font:700 28px/1.35 Bitter}.ti div span{font:500 19px/1.35 Roboto;color:#4d585e}
.q{background:#1f2a30;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 Roboto}""")

# ───────── 288 USA · Dryer vent cleaning · SINGLE · Anton + Open Sans · lint gray / blueprint blue / amber · PHONE
# New technique: house wall cutaway with the duct route drawn from dryer to outside vent, segment lengths and turns counted.
cut = '''<svg viewBox="0 0 520 600" class=cut>
<rect x="0" y="0" width="520" height="600" fill="#e8edf3"/>
<rect x="0" y="420" width="380" height="180" fill="#f6f2ea"/><rect x="380" y="0" width="40" height="600" fill="#c7ced8"/>
<rect x="420" y="0" width="100" height="600" fill="#dfe8d8"/>
<rect x="60" y="300" width="150" height="160" rx="12" fill="#ffffff" stroke="#24313f" stroke-width="5"/>
<circle cx="135" cy="390" r="46" fill="#cfdbe8" stroke="#24313f" stroke-width="5"/><rect x="80" y="316" width="70" height="12" rx="6" fill="#24313f"/>
<path d="M210 340 H270 V110 H460" fill="none" stroke="#2f6fb5" stroke-width="22" stroke-linejoin="round"/>
<path d="M210 340 H270 V110 H460" fill="none" stroke="#9cc3ea" stroke-width="10" stroke-dasharray="4 10" stroke-linejoin="round"/>
<rect x="452" y="84" width="40" height="52" rx="6" fill="#f0a531" stroke="#24313f" stroke-width="4"/>
<g font-family="Open Sans" font-weight="700" font-size="22" fill="#24313f">
<text x="220" y="384">3 ft</text><text x="286" y="232">10 ft</text><text x="300" y="86">5 ft</text>
<circle cx="270" cy="340" r="17" fill="#f0a531"/><text x="263" y="348" fill="#24313f">1</text>
<circle cx="270" cy="110" r="17" fill="#f0a531"/><text x="263" y="118" fill="#24313f">2</text></g>
<text x="60" y="490" font-family="Open Sans" font-weight="700" font-size="22" fill="#24313f">Dryer · laundry room</text>
<text x="408" y="176" font-family="Open Sans" font-weight="700" font-size="22" fill="#24313f">Outside</text>
</svg>'''
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE VENT CLEANING CO.</small><b>Book a vent clean</b></div>
<div class=af><small>DUCT LENGTH (ABOUT)</small><div class=chs2><span>Under 10 ft</span><span class=on>10–25 ft</span><span>25 ft +</span></div></div>
<div class=af><small>TURNS IN THE DUCT</small><div class=chs2><span>0–1</span><span class=on>2</span><span>3 +</span></div></div>
<div class=af><small>VENT EXITS ON</small><div class=chs2><span class=on>Side wall</span><span>Roof</span></div></div>
<div class=af><small>DRYER IS</small><div class=chs2><span class=on>Electric</span><span>Gas</span></div></div>
<div class=af><small>ZIP CODE</small><div class=in2>12345</div></div>
<div class=af><small>ARRIVAL WINDOW</small><div class=in2>Wed 2 Dec · 1–3 PM</div></div>
<div class=bk2>Book my visit</div></div>''', 380, 830)
P["p288_dryervent"] = page("""
body{--f:'Open Sans';--h:'Anton';background:#eceef1;color:#24313f}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#2f6fb5;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.5px;line-height:1.3;margin-top:34px} h1 span{color:#d98a10}
.vw{flex:1;display:flex;gap:20px;min-height:0;align-items:center}
.lc{flex:1;min-width:0;align-self:stretch;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(36,49,63,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#707a85}
.cut{flex:1;min-height:0;width:100%;display:block;border-radius:14px}
.sm{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.sm div{background:#24313f;color:#fff;border-radius:14px;padding:10px 12px}.sm small{display:block;font:700 12px/1.4 'Open Sans';letter-spacing:2px;color:#f6c46e}.sm small{margin-bottom:4px}.sm b{display:block;font:400 28px/1.5 'Anton';letter-spacing:.5px}
.ap{flex:1;display:flex;flex-direction:column;gap:12px;padding:8px 18px 20px}
.ah small{display:block;font:700 12px/1.4 'Open Sans';letter-spacing:2px;color:#2f6fb5;margin-bottom:4px}.ah b{display:block;font:400 26px/1.5 'Anton';letter-spacing:.5px}
.af small{display:block;font:700 12px/1.4 'Open Sans';letter-spacing:1.5px;color:#707a85;margin-bottom:5px}
.in2{border:2px solid #dde2e8;border-radius:10px;padding:9px 12px;font:700 16px 'Open Sans'}
.chs2{display:flex;gap:6px}.chs2 span{flex:1;text-align:center;font:700 14px 'Open Sans';padding:9px 2px;border-radius:9px;border:2px solid #dde2e8}.chs2 span.on{border-color:#2f6fb5;background:#e4eef9;color:#1f4f86}
.bk2{margin-top:auto;background:#2f6fb5;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 18px 'Open Sans'}
""", "<div class=kk>DRYER VENT CLEANING · BOOKINGS</div><h1>Clothes take two cycles to dry?<br><span>Make the vent clean easy to book.</span></h1>",
f'''<div class=vw><div class=lc><small class=cap>SAMPLE HOME · DUCT ROUTE</small>{cut}<div class=sm>{"".join(f"<div><small>{a}</small><b>{b}</b></div>" for a,b in [("LENGTH","18 ft"),("TURNS","2"),("EXIT","Side wall")])}</div></div>{ph}</div>''',
"#24313f", "Clean dryer vents? DM us", "background:#2f6fb5;color:#fff")

# ───────── 289 INDIA · Drip irrigation installer · SINGLE · Cardo + Fira Sans · field green / soil brown / water cyan
# New technique: to-scale plot plan with laterals and dripper dots, where the parts list is derived from the drawing (rows x length).
ROWS, LEN, SP = 20, 50, 0.5
def plot():
    W, H = 560, 380  # 50 m x 30 m -> 10.4 px/m x 12.7 px/m
    y0, y1 = 40, 360
    rows = "".join(f'<line x1="70" y1="{y0 + i*(y1-y0)/(ROWS-1):.1f}" x2="540" y2="{y0 + i*(y1-y0)/(ROWS-1):.1f}" stroke="#1aa7c4" stroke-width="3"/>' + "".join(f'<circle cx="{80+j*23.5:.1f}" cy="{y0 + i*(y1-y0)/(ROWS-1):.1f}" r="3.2" fill="#0d6f86"/>' for j in range(20)) for i in range(ROWS))
    return f'''<svg viewBox="0 0 600 470" class=pl><rect x="50" y="20" width="510" height="360" rx="10" fill="#e6d8bf" stroke="#7a5a35" stroke-width="5"/>
{rows}<line x1="62" y1="30" x2="62" y2="372" stroke="#0d6f86" stroke-width="12" stroke-linecap="round"/>
<rect x="8" y="180" width="40" height="40" rx="8" fill="#2c7a3f"/><text x="28" y="207" text-anchor="middle" font-family="Fira Sans" font-weight="800" font-size="18" fill="#fff">F</text>
<g font-family="Fira Sans" font-weight="700" font-size="20" fill="#3d2e1b"><text x="305" y="412" text-anchor="middle">50 m long</text><text x="575" y="200" text-anchor="middle" transform="rotate(90 575 200)">30 m wide</text></g>
<g font-family="Fira Sans" font-weight="600" font-size="17" fill="#3d2e1b"><text x="54" y="442">F = filter + valve</text><text x="226" y="442">Thick line = main pipe</text><text x="430" y="442">Dot = dripper</text></g></svg>'''
P["p289_drip"] = page("""
body{--f:'Fira Sans';--h:'Cardo';background:#f1efe4;color:#1f3a24}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#7a5a35;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;line-height:1.25;margin-bottom:4px} h1 span{color:#2c7a3f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pc{flex:1;min-height:0;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(31,58,36,.08)}
.cap{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#77735f}
.pl{flex:1;min-height:0;width:100%;display:block}
.pt{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.px{background:#fff;border-radius:20px;padding:14px 16px;box-shadow:0 10px 22px rgba(31,58,36,.07)}.px small{display:block;font:700 13px/1.4 'Fira Sans';letter-spacing:1.5px;color:#77735f}.px b{display:block;font:700 34px/1.3 Cardo;color:#0d6f86}.px span{font:500 15px/1.4 'Fira Sans';color:#5a6552}
.dk{display:flex;gap:12px}.dk div{flex:1;background:#1f3a24;color:#fff;border-radius:20px;padding:14px 18px}.dk small{display:block;font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#a9dcb5}.dk b{font:700 24px/1.4 Cardo}
""", "<div class=kk>DRIP IRRIGATION INSTALLER · SITE PLANS</div><h1>Quoting from a rough sketch?<br><span>Draw the plot, list the parts.</span></h1>",
f'''<div class=vw><div class=pc><small class=cap>SAMPLE PLOT · 20 ROWS · DRIPPER EVERY 0.5 M (DRAWING SHOWS FEWER DOTS)</small>{plot()}</div>
<div class=pt>{"".join(f"<div class=px><small>{a}</small><b>{b}</b><span>{c}</span></div>" for a,b,c in [("LATERAL PIPE","1,000 m","20 rows × 50 m"),("DRIPPERS","2,000","100 per row"),("MAIN PIPE","30 m","Along one side"),("FILTER","1 set","With valve")])}</div>
<div class=dk><div><small>SITE VISIT</small><b>Wed 25 Nov · 8 AM</b></div><div><small>INSTALL</small><b>Mon 30 Nov</b></div><div><small>FOLLOW-UP</small><b>2 weeks later</b></div></div></div>''',
"#1f3a24", "Install drip systems? DM us", "background:#2c7a3f;color:#fff")

# ───────── 290 INDIA · Steel almirah maker · SINGLE · TeX Gyre Adventor + DM Sans · steel grey / maroon / cream
# New technique: almirah front elevations drawn to relative size (height x width) with a "fits your wall" width check bar.
def alm(w, h, doors, color, locker=False, mirror=False, sc=4.2):
    W, H = int(w * sc), int(h * sc)
    d = "".join(f'<div class=dr5>{"<i class=mr></i>" if mirror and k==0 else ""}<span class=hd></span>{"<em class=lk></em>" if locker and k==doors-1 else ""}</div>' for k in range(doors))
    return f'<div class=al style="width:{W}px;height:{H}px;background:{color}">{d}</div>'
models = [("A-2", "2 door", 36, 78, 2, False, False), ("A-2L", "2 door + locker", 36, 78, 2, True, False), ("A-3M", "3 door + mirror", 54, 78, 3, True, True)]
P["p290_almirah"] = page("""
body{--f:'DM Sans';--h:'TeX Gyre Adventor';background:#f4efe6;color:#2a2c33}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#8c2a3c;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#8c2a3c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ct{flex:1;min-height:0;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(42,44,51,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#787268}
.ms{flex:1;display:flex;justify-content:space-around;align-items:flex-end;background:linear-gradient(transparent 92%,#e2d9ca 92%);padding:0 10px 6px}
.mo{display:flex;flex-direction:column;align-items:center;gap:8px}.mo.on b{margin-top:10px}.mo b{font:700 22px/1.3 'TeX Gyre Adventor'}.mo span{font:600 16px 'DM Sans';color:#5f5a52}
.al{display:flex;gap:4px;padding:8px;border-radius:6px;border:4px solid #2a2c33;box-shadow:inset 0 -10px 0 rgba(0,0,0,.12)}
.dr5{flex:1;border-radius:4px;border:3px solid rgba(0,0,0,.25);position:relative;background:linear-gradient(90deg,rgba(255,255,255,.18),rgba(255,255,255,0) 40%)}
.hd{position:absolute;top:44%;right:8px;width:8px;height:44px;border-radius:4px;background:#d9d2c4;border:2px solid #2a2c33}
.mr{position:absolute;left:12%;right:24%;top:10%;bottom:30%;border-radius:4px;background:linear-gradient(135deg,#eef5f8,#bcd3dd);border:2px solid #2a2c33}
.lk{position:absolute;left:14%;right:14%;top:40%;height:56px;border-radius:4px;border:3px solid rgba(0,0,0,.35);background:rgba(0,0,0,.08)}
.on .al{outline:5px solid #8c2a3c;outline-offset:6px}
.bt{display:grid;grid-template-columns:1.25fr 1fr;gap:12px}
.fw{background:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(42,44,51,.08)}
.wb{height:56px;border-radius:12px;background:#ece5d8;position:relative;overflow:hidden}.wb i{position:absolute;left:0;top:0;bottom:0;width:{fit}%;background:#2a2c33;color:#fff;font:700 17px/56px 'DM Sans';font-style:normal;padding-left:14px}.wb em{position:absolute;right:14px;top:0;font:700 17px/56px 'DM Sans';font-style:normal;color:#5f5a52}
.fw b{font:700 22px/1.3 'DM Sans';color:#2e7a43}
.cl5{display:flex;gap:8px}.cl5 span{flex:1;height:44px;border-radius:10px;border:3px solid #e2d9ca}.cl5 span.on{border-color:#2a2c33;box-shadow:0 0 0 3px #fff inset}
.od{background:#8c2a3c;color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.od small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#f6cbd3}
.or5{display:flex;justify-content:space-between;font:500 18px/1.4 'DM Sans';color:#fbe3e7}.or5 b{color:#fff}
""".replace("{fit}", str(round(54 / 60 * 100))), "<div class=kk>STEEL ALMIRAH MAKER · ORDERS</div><h1>Will it fit? Which colour?<br><span>Let them choose on a link.</span></h1>",
f'''<div class=vw><div class=ct><small class=cap>MODELS · DRAWN TO SIZE · SAMPLE</small><div class=ms>{"".join(f'<div class="mo{" on" if c=="A-3M" else ""}">{alm(w,h,d,"#8a929c" if c!="A-3M" else "#8c2a3c",lk,mr)}<b>{c}</b><span>{n} · {w} × {h} in</span></div>' for c,n,w,h,d,lk,mr in models)}</div></div>
<div class=bt><div class=fw><small class=cap>FITS YOUR WALL? · WALL IS 60 IN</small><div class=wb><i>A-3M · 54 in</i></div><b>Fits, with 6 in to spare</b><small class=cap>COLOUR</small><div class=cl5>{"".join(f'<span class="{"on" if c=="#8c2a3c" else ""}" style="background:{c}"></span>' for c in ["#8a929c","#8c2a3c","#3a5a7a","#d9cfbd","#2f5d4a"])}</div></div>
<div class=od><small>ORDER · SAMPLE</small>{"".join(f'<div class=or5><span>{a}</span><b>{b}</b></div>' for a,b in [("Model","A-3M, maroon"),("Floor","3rd, no lift"),("Delivery","Sat 28 Nov"),("Team","3 people")])}</div></div></div>''',
"#2a2c33", "Make steel almirahs? DM us", "background:#8c2a3c;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
