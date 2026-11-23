import sys, random, math, datetime as _dt; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
fmt = lambda n: f"{n:,}"

# ───────── 346 INDIA · Dairy farm (herd records) · SINGLE · Poppins + Roboto · fodder green / milk white / barn red
# New technique: clip-path yellow ear tags as animal IDs, each with a CSS milk can whose fill is morning + evening
# litres; herd totals and the collection-centre note are computed from the same list.
HERD = [("C-01", 7.5, 6.5, "Milking", ""), ("C-02", 6.0, 5.5, "Milking", ""), ("C-03", 0, 0, "Dry", "Calving due Wed 2 Dec"),
        ("C-04", 8.0, 7.0, "Milking", ""), ("C-05", 5.5, 5.0, "Milking", "Vet visit Thu 26 Nov"), ("C-06", 7.0, 6.0, "Milking", ""),
        ("C-07", 0, 0, "Dry", "Calving due Fri 18 Dec"), ("C-08", 6.5, 6.0, "Milking", "")]
AM = sum(h[1] for h in HERD); PM = sum(h[2] for h in HERD); MX = 16
def can(am, pm):
    a = am / MX * 100; p = pm / MX * 100
    return f'<div class=cn6><i class=lid></i><div class=bd6><em class=pm style="height:{p:.0f}%"></em><em class=am style="height:{a:.0f}%"></em></div></div>'
P["p346_dairy"] = page("""
body{--f:'Roboto';--h:'Poppins';background:#eef4e6;color:#1e2b16}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#b5332a;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#3f7d20}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.hd6{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:12px}
.cw6{background:#fff;border-radius:22px;padding:14px;display:flex;flex-direction:column;align-items:center;gap:8px;box-shadow:0 10px 24px rgba(30,43,22,.08)}
.cw6.dry{background:#f6f1e6}
.tg6{width:104px;height:64px;background:#f6c629;clip-path:polygon(0 30%,30% 0,100% 0,100% 100%,30% 100%,0 70%);display:flex;align-items:center;justify-content:center;padding-left:18px;font:800 22px/1.3 Poppins;color:#1e2b16;position:relative}
.tg6::before{content:"";position:absolute;left:16px;top:26px;width:12px;height:12px;border-radius:50%;background:#fff}
.cn6{display:flex;flex-direction:column;align-items:center;flex:1;min-height:0;width:84px}
.cn6 .lid{width:46px;height:12px;border-radius:6px 6px 0 0;background:#9aa4ad}
.bd6{flex:1;width:84px;border-radius:14px 14px 10px 10px;background:linear-gradient(90deg,#7d8791,#b9c2ca 40%,#8c96a0);box-shadow:inset 0 0 0 3px #6b747d;display:flex;flex-direction:column;justify-content:flex-end;overflow:hidden}
.bd6 em{display:block;width:100%}.bd6 .am{background:#fff4c9;box-shadow:inset 0 -2px 0 #d6dde3}.bd6 .pm{background:#cfe8ff;box-shadow:inset 0 2px 0 #fff}
.bd6 em.am{order:2}.bd6 em.pm{order:1}
.cw6 b{font:700 20px/1.3 Poppins}.cw6 span{font:500 15px/1.35 Roboto;color:#56604e;text-align:center}
.cw6 strong{font:700 14px/1.3 Roboto;color:#b5332a;background:#fde6e3;border-radius:8px;padding:4px 8px;text-align:center}
.bt6{display:grid;grid-template-columns:1fr 1fr 1.4fr;gap:12px}
.tt6{background:#fff;border-radius:20px;padding:12px 18px}.tt6 small{display:block;font:700 13px/1.4 Roboto;letter-spacing:2px;color:#56604e}.tt6 b{font:800 40px/1.25 Poppins}.tt6 i{display:inline-block;width:16px;height:16px;border-radius:4px;margin-right:8px;vertical-align:-1px;box-shadow:inset 0 0 0 2px #b9c2ca}
.ms6{background:#3f7d20;color:#fff;border-radius:20px;padding:14px 18px;font:500 18px/1.4 Roboto;display:flex;align-items:center}.ms6 b{color:#e3f7c8}
""", "<div class=kk>DAIRY FARM · HERD RECORDS</div><h1>Which cow gave how much?<br><span>Know it every milking.</span></h1>",
f'''<div class=vw><div class=hd6>{"".join(f'<div class="cw6 {"dry" if s=="Dry" else ""}"><div class=tg6>{t}</div>{can(a,p)}<b>{(f"{a+p:g} L") if s!="Dry" else "Dry"}</b><span>{f"AM {a:g} · PM {p:g}" if s!="Dry" else "Resting"}</span>{f"<strong>{n}</strong>" if n else ""}</div>' for t,a,p,s,n in HERD)}</div>
<div class=bt6><div class=tt6><small><i style="background:#fff4c9"></i>MORNING</small><b>{AM:g} L</b></div><div class=tt6><small><i style="background:#cfe8ff"></i>EVENING</small><b>{PM:g} L</b></div>
<div class=ms6><span><b>{AM:g} L sent at 6:30 AM.</b> The collection slip matches the herd record. Sample, Mon 23 Nov.</span></div></div></div>''',
"#1e2b16", "Run a dairy farm? DM us", "background:#b5332a;color:#fff")

# ───────── 347 INDIA · Office tea supply (chai rounds) · CAROUSEL 5 · Bitter + DM Sans · masala chai brown / flask steel / cardamom green
# New technique: CSS steel flasks with cup tallies, and a cups-per-day heat calendar (office rows x working days) whose
# row sums become the monthly statement on slide 4.
OF = [("Office A", "3rd floor, IT team", ["10:30 AM", "4:00 PM"], 2), ("Office B", "Ground floor, accounts", ["10:30 AM", "1:00 PM", "4:00 PM"], 1),
      ("Office C", "Shop row, 6 shops", ["11:00 AM", "5:00 PM"], 1), ("Office D", "Clinic waiting room", ["10:00 AM", "12:30 PM", "3:30 PM"], 1)]
DAYS = [d for d in range(2, 24) if _dt.date(2026, 11, d).weekday() < 6]  # Mon-Sat, 2 to 23 Nov
random.seed(347)
HEAT = {o[0]: [0 if (o[0] == "Office C" and d in (8, 15)) else random.randint(12, 34) for d in DAYS] for o in OF}
HEAT["Office B"] = [0 if d in (3,) else random.randint(14, 28) for d in DAYS]; HEAT["Office B"][0] = 18
TC = {k: sum(v) for k, v in HEAT.items()}
CT = """
body{--f:'DM Sans';--h:'Bitter';background:#f3ebe0;color:#2e1e12}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#5f8a3a;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1px} h1 span{color:#9a5a24}
.cd{background:#fffaf3;border-radius:24px;box-shadow:0 12px 28px rgba(46,30,18,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7d6a58}
.nb{display:flex;align-items:center;gap:14px;background:#2e1e12;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#5f8a3a;color:#fff}.nb b{color:#f3c58f}
.fl{width:86px;display:flex;flex-direction:column;align-items:center;flex:none}
.fl .cp{width:46px;height:18px;border-radius:8px 8px 3px 3px;background:#2e1e12}
.fl .nk{width:36px;height:10px;background:#8c96a0}
.fl .bd{width:86px;height:170px;border-radius:22px 22px 16px 16px;background:linear-gradient(90deg,#8c96a0,#e9eef2 35%,#c3cbd2 60%,#7d8791);position:relative}
.fl .bd i{position:absolute;left:8px;right:8px;top:62px;height:40px;border-radius:6px;background:#9a5a24;color:#fff;font:700 15px/40px 'DM Sans';font-style:normal;text-align:center}
"""
def ct(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2e1e12;color:#f3c58f"):
    return page(CT + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2e1e12", cta, ctacss, tagline=f"{n} / 5")
def flask(lbl):
    return f'<div class=fl><i class=cp></i><i class=nk></i><div class=bd><i>{lbl}</i></div></div>'
P["p347_chai_s1"] = ct(1, "OFFICE TEA SUPPLY · CHAI ROUNDS", "Chai rounds for 4 offices.<br><span>Who counts the cups?</span>",
f'''<div class=w1><div class="cd c1">{"".join(f'<div class=of1>{flask(o[0].split()[1])}<b>{o[0]}</b><span class=tl1>{"".join("<i></i>" for _ in range(5))}<s>{"".join("<i></i>" for _ in range(3))}</s> ?</span></div>' for o in OF)}</div>
<div class=bb1><span class=vn>{ic("chat",22)} Office B, last month-end</span><p>“We only took 18 cups on Monday, not 24. Please check your notebook.”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c1{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:10px;align-items:center;padding:20px}
.of1{display:flex;flex-direction:column;align-items:center;gap:12px}.of1 .fl{transform:scale(1.7);margin:90px 0 80px}.of1 b{font:800 24px/1.3 Bitter}
.tl1{display:flex;gap:6px;align-items:center;font:700 30px/1.3 Bitter;color:#b5332a}.tl1 i{width:7px;height:40px;background:#2e1e12;border-radius:2px}.tl1 s{display:flex;gap:5px;text-decoration:none;opacity:.35}
.bb1{background:#2e1e12;color:#fff;border-radius:22px 22px 22px 6px;padding:16px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px/1.4 'DM Sans';color:#f3c58f;margin-bottom:6px}.bb1 p{font:500 24px/1.4 'DM Sans'}""")

P["p347_chai_s2"] = ct(2, "STEP 1 · EVERY OFFICE, ITS OWN ROUNDS", "Rounds and flasks<br><span>set once, per office.</span>",
f'''<div class=w2>{"".join(f'<div class="cd ro2"><div class=hd2><b>{o[0]}</b><span>{o[1]} · sample</span></div><div class=tm2>{"".join(f"<i>{t}</i>" for t in o[2])}</div><div class=fk2><b>{o[3]}</b><span>flask{"s" if o[3]>1 else ""}<br>a round</span></div></div>' for o in OF)}
<div class=nb><span class=ib>{ic("clock",26)}</span><span>The tea boy sees <b>today's rounds by time</b>, and taps the cups given at each office.</span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.ro2{flex:1;display:grid;grid-template-columns:1fr 1.2fr auto;gap:16px;align-items:center;padding:10px 22px;min-height:0}
.hd2 b{display:block;font:800 30px/1.3 Bitter}.hd2 span{font:500 19px/1.4 'DM Sans';color:#7d6a58}
.tm2{display:flex;flex-wrap:wrap;gap:8px}.tm2 i{font:700 20px/1.3 'DM Sans';font-style:normal;background:#efe2d0;border-radius:10px;padding:8px 12px}
.fk2{display:flex;align-items:center;gap:12px;background:#2e1e12;color:#fff;border-radius:16px;padding:10px 16px}.fk2 b{font:800 40px/1.2 Bitter;color:#f3c58f}.fk2 span{font:600 16px/1.35 'DM Sans'}""")

def hc(v):
    if v == 0: return 'class="h0"'
    return f'style="background:rgba(154,90,36,{0.18 + (v-12)/22*0.8:.2f});color:{"#fff" if v > 24 else "#2e1e12"}"'
P["p347_chai_s3"] = ct(3, "STEP 2 · CUPS COUNTED EVERY DAY", "A cup calendar<br><span>both sides can see.</span>",
f'''<div class=w3><div class="cd hm3"><div class="rw3 hd3"><span></span>{"".join(f"<b>{d}</b>" for d in DAYS)}<strong>Total</strong></div>
{"".join(f'<div class=rw3><span>{o[0]}</span>{"".join(f"<i {hc(v)}>{v if v else chr(8211)}</i>" for v in HEAT[o[0]])}<strong>{TC[o[0]]}</strong></div>' for o in OF)}
<div class=lg3><span><i style="background:rgba(154,90,36,.2)"></i>Fewer cups</span><span><i style="background:rgba(154,90,36,.98)"></i>More cups</span><span><i class=h0></i>Closed</span><em>Mon 2 to Mon 23 Nov · Sundays off · sample</em></div></div>
<div class=nb><span class=ib>{ic("check",26)}</span><span>Office B checks Monday 2 Nov: <b>{HEAT["Office B"][0]} cups, the same number they see.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hm3{flex:1;padding:18px 18px;display:flex;flex-direction:column;gap:6px;min-height:0}
.rw3{flex:1;display:grid;grid-template-columns:104px repeat(19,1fr) 64px;gap:4px;align-items:stretch}
.rw3>span{font:800 18px/1.3 Bitter;align-self:center}.rw3 i{border-radius:6px;display:flex;align-items:center;justify-content:center;font:600 14px/1.3 'DM Sans';font-style:normal}
.rw3 i.h0,.lg3 i.h0{background:repeating-linear-gradient(45deg,#e8ddd0 0 4px,#f6efe6 4px 8px);color:#a8957f}
.rw3 strong{font:800 22px/1.3 Bitter;align-self:center;text-align:right;color:#9a5a24}
.hd3{flex:none}.hd3 b{font:700 13px/1.3 'DM Sans';text-align:center;color:#7d6a58}.hd3 strong{font:700 13px/1.3 'DM Sans';color:#7d6a58}
.lg3{display:flex;gap:18px;align-items:center;font:600 15px/1.4 'DM Sans';color:#5d4b3a;margin-top:6px}.lg3 span{display:flex;align-items:center;gap:6px}.lg3 i{width:18px;height:18px;border-radius:4px}.lg3 em{margin-left:auto;font-style:normal;color:#7d6a58}""")

ob = OF[1]; offb = sum(1 for v in HEAT["Office B"] if v == 0)
P["p347_chai_s4"] = ct(4, "STEP 3 · THE STATEMENT MAKES ITSELF", "Month-end in one tap,<br><span>no arguments.</span>",
f'''<div class=w4><div class="cd sl4"><b class=t4>{ob[0]} · November</b><span class=s4>{ob[1]} · cup statement · sample</span>
<div class=ln4><span>Working days</span><strong>{len(DAYS)}</strong></div><div class=ln4><span>Closed days</span><strong>{offb} (Tue 3 Nov)</strong></div>
<div class=ln4><span>Rounds a day</span><strong>{len(ob[2])}</strong></div><div class="ln4 tt"><span>Cups in November</span><strong>{TC[ob[0]]}</strong></div>
<div class=bx4>{"".join(f"<i {hc(v)}></i>" for v in HEAT[ob[0]])}</div><div class=up4>Sent by message with your plan rate and a UPI link</div></div>
<div class=sd4>{"".join(f'<div class="cd t4b"><b>{o[0]}</b><span>{TC[o[0]]} cups</span></div>' for o in OF)}</div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:1.5fr 1fr;gap:14px;min-height:0}.sl4{padding:24px 26px;display:flex;flex-direction:column;gap:10px}
.t4{font:800 32px/1.3 Bitter}.s4{font:500 17px/1.4 'DM Sans';color:#7d6a58;border-bottom:2px dashed #d9c9b4;padding-bottom:12px}
.ln4{flex:1;display:flex;justify-content:space-between;align-items:center;font:500 26px/1.4 'DM Sans';border-bottom:1px solid #efe2d0}.ln4 strong{font-weight:700}
.ln4.tt{border:0;font:800 26px/1.4 Bitter;color:#9a5a24}
.bx4{display:grid;grid-template-columns:repeat(19,1fr);gap:4px}.bx4 i{height:56px;border-radius:5px}.bx4 i.h0{background:repeating-linear-gradient(45deg,#e8ddd0 0 4px,#f6efe6 4px 8px)}
.up4{background:#5f8a3a;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 19px/1.4 'DM Sans'}
.sd4{display:flex;flex-direction:column;gap:12px}.t4b{flex:1;display:flex;flex-direction:column;justify-content:center;padding:14px 22px}.t4b b{font:800 26px/1.3 Bitter}.t4b span{font:600 22px/1.4 'DM Sans';color:#9a5a24}
.sd4 .t4b:nth-child(2){box-shadow:0 0 0 4px #5f8a3a}""")

P["p347_chai_s5"] = ct(5, "YOUR TURN", "Supply tea to offices?<br><span>Let's build your round app.</span>",
f'''<div class=w5><div class="cd c5">{"".join(flask(l) for l in ["A","B","C","D"])}</div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("clock","Rounds by time","Every office, every flask"),("cup","Tap cups given","At the office door"),("grid","Cup calendar","Both sides see it"),("send","Month statement","Sent with a UPI link")])}</div>
<div class=q>How do you count cups for your offices today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#5f8a3a;color:#fff",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1.05fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{display:grid;grid-template-columns:1fr 1fr;align-items:center;justify-items:center;padding:20px}.c5 .fl{transform:scale(1.5)}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fffaf3;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(46,30,18,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#efe2d0;color:#9a5a24}.ti b{display:block;font:800 22px/1.4 Bitter;margin-bottom:2px}.ti div span{font:500 17px/1.4 'DM Sans';color:#5d4b3a}
.q{background:#2e1e12;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'DM Sans'}""")

# ───────── 348 INDIA · Glass and mirror shop · SINGLE · Montserrat + Inter · glass aqua / cutting orange / graphite
# New technique: to-scale SVG glass sheet (aqua gradient + diagonal sheen) with order pieces placed on it, dimension
# labels inside each piece and a hatched offcut that is saved to an offcut rack list.
SH = (96, 72)
PCS = [("T1", "Table top", 0, 0, 48, 30, "#ffb27a"), ("W1", "Window", 48, 0, 36, 24, "#8fd3e8"), ("W1", "Window", 48, 24, 36, 24, "#8fd3e8"),
       ("M1", "Mirror", 0, 30, 24, 36, "#c9d6f2"), ("S1", "Shelf", 24, 30, 24, 12, "#b9e6b0"), ("S1", "Shelf", 24, 42, 24, 12, "#b9e6b0"), ("S1", "Shelf", 24, 54, 24, 12, "#b9e6b0")]
OC = (48, 48, 48, 24)
def sheet():
    k = 8; W, H = SH[0]*k, SH[1]*k
    s = f'<svg viewBox="-6 -6 {W+12} {H+12}" class=gs8><defs><linearGradient id="gq8" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#e6f7f8"/><stop offset="1" stop-color="#a9dfe2"/></linearGradient>'
    s += '<pattern id="hz8" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="14" height="14" fill="#fff3e6"/><rect width="5" height="14" fill="#ffd2a8"/></pattern></defs>'
    s += f'<rect x="0" y="0" width="{W}" height="{H}" rx="4" fill="url(#gq8)" stroke="#2c3338" stroke-width="5"/>'
    for c, n, x, y, w, h, col in PCS:
        s += f'<rect x="{x*k+3}" y="{y*k+3}" width="{w*k-6}" height="{h*k-6}" rx="3" fill="{col}" fill-opacity=".85" stroke="#2c3338" stroke-width="2.5" stroke-dasharray="10 6"/>'
        if h >= 30 and w < 30:
            s += f'<text x="{x*k+16}" y="{y*k+52}" font-family="Montserrat" font-weight="800" font-size="38" fill="#1d2327">{c}</text><text x="{x*k+16}" y="{y*k+100}" font-family="Inter" font-weight="600" font-size="28" fill="#1d2327">{w} x {h} in</text>'
        else:
            s += f'<text x="{x*k+14}" y="{y*k+54}" font-family="Inter" font-weight="600" font-size="{24 if w<=24 else 28}" fill="#1d2327"><tspan font-family="Montserrat" font-weight="800" font-size="{30 if w<=24 else 36}">{c}</tspan> {w} x {h} in</text>'
    x, y, w, h = OC
    s += f'<rect x="{x*k+3}" y="{y*k+3}" width="{w*k-6}" height="{h*k-6}" rx="3" fill="url(#hz8)" stroke="#e46a1b" stroke-width="3"/>'
    s += f'<text x="{x*k+20}" y="{y*k+70}" font-family="Montserrat" font-weight="800" font-size="40" fill="#b84d0c">Offcut kept</text><text x="{x*k+20}" y="{y*k+130}" font-family="Inter" font-weight="600" font-size="32" fill="#b84d0c">{w} x {h} in</text>'
    s += '<path d="M60 40 L240 40 L60 220 Z" fill="#fff" fill-opacity=".25"/>'
    return s + "</svg>"
ORD8 = [("T1", "Table top, 5 mm", "48 x 30 in", 1, "Sample Cafe"), ("W1", "Window, 4 mm", "36 x 24 in", 2, "House 12"), ("M1", "Mirror, 4 mm", "24 x 36 in", 1, "Salon 3"), ("S1", "Shelf, 6 mm", "24 x 12 in", 3, "Shop 9")]
P["p348_glass"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#eaf3f3;color:#1d2327}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#e46a1b;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#1b8b93}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sc8{background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 28px rgba(29,35,39,.08)}
.sc8>small,.ol8>small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#5e6a70}.gs8{width:100%;max-height:440px;display:block}
.bt8{flex:1;display:grid;grid-template-columns:1.5fr 1fr;gap:14px;min-height:0}
.ol8{background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 12px 28px rgba(29,35,39,.08)}
.or8{flex:1;display:grid;grid-template-columns:56px 1fr auto;gap:12px;align-items:center;border-bottom:1px solid #e6eeee}.or8:last-child{border:0}
.or8>b{font:800 22px/1.3 Montserrat;background:#1d2327;color:#fff;border-radius:10px;text-align:center;padding:4px 0}
.or8 span{font:600 18px/1.35 Inter}.or8 span em{display:block;font-style:normal;font-weight:500;font-size:15px;color:#5e6a70}.or8 strong{font:800 20px/1.3 Montserrat;color:#1b8b93}
.rk8{background:#1d2327;color:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.rk8 small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#ffb27a}.rk8 b{font:800 30px/1.25 Montserrat}.rk8 p{font:500 18px/1.45 Inter;color:#d5dde0}.rk8 p b{font:700 18px Inter;color:#ffb27a}
.rk8 .r{margin-top:auto;display:flex;gap:8px;flex-wrap:wrap}.rk8 .r i{font:600 15px/1.3 Inter;font-style:normal;background:#2f383e;border-radius:8px;padding:6px 10px}
""", "<div class=kk>GLASS AND MIRROR SHOP · CUTTING</div><h1>Cutting glass by guesswork?<br><span>Plan every sheet first.</span></h1>",
f'''<div class=vw><div class=sc8><small>SHEET 8 x 6 FT (96 x 72 IN) · TODAY'S CUT PLAN · SAMPLE</small>{sheet()}</div>
<div class=bt8><div class=ol8><small>ORDERS ON THIS SHEET · SAMPLE</small>{"".join(f'<div class=or8><b>{c}</b><span>{n} · {z}<em>{w}</em></span><strong>x {q}</strong></div>' for c,n,z,q,w in ORD8)}</div>
<div class=rk8><small>OFFCUT RACK</small><b>48 x 24 in saved</b><p>Next small order that fits <b>gets cut from the rack first</b>, not from a new sheet.</p><div class=r><i>R-1 · 30 x 18</i><i>R-2 · 20 x 14</i><i>R-3 · 48 x 24</i></div></div></div></div>''',
"#1d2327", "Run a glass shop? DM us", "background:#e46a1b;color:#fff")

# ───────── 349 USA · Short-term rental turnover cleaning · SINGLE · Archivo Black + Source Sans 3 · linen white / turnover coral / slate
# New technique: "turnover window" bars (check-out to check-in) on an 8 AM to 6 PM axis with the cleaning block
# placed inside each window by % position; linen and crew counts summed from the same rows.
T0, T1 = 8, 18
def pc(h): return (h - T0) / (T1 - T0) * 100
TO = [("Lake Cabin", 10, 16, 10.5, 13, "Crew A", 3), ("Downtown Loft", 11, 15, 11.25, 13.25, "Crew B", 2), ("Beach Bungalow", 10, 16, 13.5, 15.5, "Crew A", 2),
      ("Garden Suite", 11, 17, 13.5, 15, "Crew B", 1), ("Hilltop House", 9, 15, 9.25, 13.25, "Crew C", 4)]
def hh(h): hr = int(h); m = int(round((h - hr) * 60)); ap = "AM" if hr < 12 else "PM"; hr12 = hr if hr <= 12 else hr - 12; return f"{hr12}:{m:02d} {ap}" if m else f"{hr12} {ap}"
P["p349_turnover"] = page("""
body{--f:'Source Sans 3';--h:'Archivo Black';background:#f5f1ea;color:#27313a}
.kk{font:700 16px/1.5 'Source Sans 3';letter-spacing:3px;color:#e0584a;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.25;letter-spacing:-1px} h1 span{color:#e0584a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bd9{flex:1;min-height:0;background:#fff;border-radius:26px;padding:16px 22px 14px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(39,49,58,.08)}
.bd9>small{font:700 13px/1.5 'Source Sans 3';letter-spacing:2px;color:#6a747d}
.ax9{display:grid;grid-template-columns:200px 1fr;margin-bottom:4px}.ax9 div{position:relative;height:22px}.ax9 span{position:absolute;transform:translateX(-50%);font:600 14px/1.5 'Source Sans 3';color:#6a747d;white-space:nowrap}
.rw9{flex:1;display:grid;grid-template-columns:200px 1fr;align-items:center;border-top:1px solid #efebe4}
.rw9>div:first-child b{display:block;font:400 19px/1.4 'Archivo Black'}.rw9>div:first-child span{font:500 16px/1.4 'Source Sans 3';color:#6a747d}
.tl9{position:relative;height:64px;background:repeating-linear-gradient(90deg,#f1ede6 0 1px,transparent 1px 10%);border-radius:10px}
.wd9{position:absolute;top:6px;bottom:6px;background:#fde3df;border:2px dashed #e0584a;border-radius:10px}
.cl9{position:absolute;top:14px;bottom:14px;background:#27313a;color:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;font:700 15px/1.3 'Source Sans 3';white-space:nowrap}
.lg9{display:flex;gap:20px;font:600 15px/1.5 'Source Sans 3';color:#55606a;margin-top:6px}.lg9 span{display:flex;align-items:center;gap:8px}.lg9 i{width:22px;height:14px;border-radius:4px}
.bt9{display:grid;grid-template-columns:1fr 1fr 1.3fr;gap:12px}
.tt9{background:#27313a;color:#fff;border-radius:20px;padding:14px 18px}.tt9 small{display:block;font:700 13px/1.5 'Source Sans 3';letter-spacing:2px;color:#b8c2cb}.tt9 b{font:400 38px/1.3 'Archivo Black';color:#ffb4a9}
.nt9{background:#e0584a;color:#fff;border-radius:20px;padding:14px 18px;font:500 18px/1.45 'Source Sans 3'}.nt9 b{color:#fff3e0}
""", "<div class=kk>SHORT-TERM RENTAL · TURNOVER CLEANING</div><h1>Checkout at 11, guests at 3?<br><span>See every clean window.</span></h1>",
f'''<div class=vw><div class=bd9><small>SATURDAY, DECEMBER 5 · 5 TURNOVERS · SAMPLE</small>
<div class=ax9><div></div><div>{"".join(f'<span style="left:{pc(h):.1f}%">{hh(h)}</span>' for h in range(T0+1, T1, 2))}</div></div>
{"".join(f'<div class=rw9><div><b>{n}</b><span>{c} · {l} linen set{"s" if l>1 else ""}</span></div><div class=tl9><div class=wd9 style="left:{pc(o):.1f}%;width:{pc(i)-pc(o):.1f}%"></div><div class=cl9 style="left:{pc(a):.1f}%;width:{pc(b)-pc(a):.1f}%">{hh(a)} to {hh(b)}</div></div></div>' for n,o,i,a,b,c,l in TO)}
<div class=lg9><span><i style="background:#fde3df;border:2px dashed #e0584a"></i>Checkout to next check-in</span><span><i style="background:#27313a"></i>Cleaning booked</span></div></div>
<div class=bt9><div class=tt9><small>LINEN SETS</small><b>{sum(t[6] for t in TO)}</b></div><div class=tt9><small>CREWS OUT</small><b>{len(set(t[5] for t in TO))}</b></div>
<div class=nt9>Each crew ends with a photo checklist, <b>so the host sees the place is ready.</b></div></div></div>''',
"#27313a", "Clean rentals? DM us", "background:#27313a;color:#ffb4a9")

# ───────── 350 INDIA · Broiler poultry farm · SINGLE · Gelasio + Open Sans · feed yellow / shed green / straw
# New technique: SVG side-view poultry sheds with curtain walls, a 42-dot batch-day strip per shed, and feed-days-left
# computed from bags in stock ÷ bags a day (shown as a CSS stack of feed bags).
SHD = [("Shed 1", 5000, 28, 13, 30, "Fri 4 Dec", "Trader A"), ("Shed 2", 4000, 12, 5, 70, "Sat 19 Dec", "Not booked")]
def shed(day):
    return ('<svg viewBox="0 0 420 150" class=sd0><path d="M10 60 L210 10 L410 60 Z" fill="#2f6b3a"/><rect x="24" y="60" width="372" height="80" fill="#f3e3b5"/>'
            + "".join(f'<rect x="{40+i*44}" y="72" width="34" height="44" rx="3" fill="#cfd9c4" stroke="#2f6b3a" stroke-width="2"/>' for i in range(8))
            + '<rect x="0" y="138" width="420" height="12" rx="4" fill="#c9a861"/></svg>')
P["p350_broiler"] = page("""
body{--f:'Open Sans';--h:'Gelasio';background:#faf3dc;color:#24301c}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#2f6b3a;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#b07d0a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sh0{flex:1;min-height:0;background:#fff;border-radius:24px;padding:16px 22px;display:grid;grid-template-columns:330px 1fr;gap:20px;align-items:center;box-shadow:0 12px 28px rgba(36,48,28,.08)}
.sd0{width:100%;display:block}.lf0{display:flex;flex-direction:column;gap:6px}.lf0 b{font:700 30px/1.3 Gelasio}.lf0 span{font:500 17px/1.4 'Open Sans';color:#5b6650}
.rt0{display:flex;flex-direction:column;gap:12px}
.dy0{display:grid;grid-template-columns:repeat(21,1fr);gap:4px}.dy0 i{aspect-ratio:1;border-radius:50%;background:#efe7cd}.dy0 i.on{background:#f2b705}.dy0 i.td{background:#2f6b3a;box-shadow:0 0 0 3px #b9dcb9}
.dl0{display:flex;justify-content:space-between;font:600 16px/1.4 'Open Sans';color:#5b6650}.dl0 b{color:#24301c}
.st0{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.st0 div{background:#faf3dc;border-radius:14px;padding:8px 12px}.st0 small{display:block;font:600 13px/1.4 'Open Sans';color:#6d6a4c}.st0 strong{font:700 22px/1.35 Gelasio}
.st0 div.wr{background:#fde6c4}.st0 div.wr strong{color:#b05a0a}
.bt0{display:grid;grid-template-columns:1.15fr 1.3fr;gap:14px}
.bg0{background:#2f6b3a;color:#fff;border-radius:22px;padding:14px 18px;display:flex;align-items:center;gap:16px}
.bs0{display:flex;flex-wrap:wrap;width:120px;gap:4px;flex:none}.bs0 i{width:36px;height:46px;border-radius:6px 6px 4px 4px;background:linear-gradient(#f6e7b8,#e5cc85);box-shadow:inset 0 -6px 0 #c9a861}
.bg0 b{display:block;font:700 26px/1.3 Gelasio;color:#ffe08a}.bg0 span{font:500 16px/1.4 'Open Sans'}
.ms0{background:#fff;border-radius:22px 22px 22px 6px;padding:14px 18px;font:500 18px/1.45 'Open Sans';box-shadow:0 12px 28px rgba(36,48,28,.08)}.ms0 small{display:block;font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#2f6b3a;margin-bottom:4px}
""", "<div class=kk>BROILER FARM · BATCH RECORDS</div><h1>Two sheds, two batches.<br><span>Feed and buyers in one place.</span></h1>",
f'''<div class=vw>{"".join(f"""<div class=sh0><div class=lf0>{shed(d)}<b>{n}</b><span>{b:,} birds placed · sample</span></div><div class=rt0>
<div class=dl0><span>Batch day <b>{d}</b> of about 42</span><span>Lifting <b>{lf}</b></span></div><div class=dy0>{"".join(f'<i class="{"td" if k==d else ("on" if k<d else "")}"></i>' for k in range(1,43))}</div>
<div class=st0><div><small>Feed bags a day</small><strong>{bd}</strong></div><div class="{"wr" if st//bd < 3 else ""}"><small>Bags in stock</small><strong>{st} · {st//bd} days</strong></div><div><small>Buyer</small><strong>{tr}</strong></div></div></div></div>""" for n,b,d,bd,st,lf,tr in SHD)}
<div class=bt0><div class=bg0><div class=bs0>{"".join("<i></i>" for _ in range(6))}</div><div><b>Order feed today</b><span>Shed 1 has {SHD[0][4]//SHD[0][3]} days of feed left.</span></div></div>
<div class=ms0><small>MESSAGE TO TRADER A</small>Shed 1 lifting is on Fri 4 Dec, 5:30 AM. Please confirm the truck by Wednesday.</div></div></div>''',
"#24301c", "Run a poultry farm? DM us", "background:#2f6b3a;color:#ffe08a")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
