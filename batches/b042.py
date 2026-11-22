import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 226 INDIA · Fire extinguisher refilling service · SINGLE · Montserrat + Roboto · extinguisher red / graphite / pale lemon
# New technique: row of drawn cylinders on a wall rail, each with a pressure-gauge needle and a hanging due-date tag (status by colour).
cyl = [("F1 · Reception", "ABC 6 kg", "Due Jun 2027", "ok"), ("F1 · Kitchen", "CO2 4.5 kg", "Due 4 Dec", "ds"), ("F2 · Store", "ABC 6 kg", "Due Mar 2027", "ok"),
       ("F2 · Office", "ABC 4 kg", "Overdue · Oct", "od"), ("F3 · Server room", "CO2 4.5 kg", "Due Aug 2027", "ok"), ("F3 · Corridor", "ABC 9 kg", "Due May 2027", "ok")]
def ext(kind, st):
    ang = {"ok": -35, "ds": 20, "od": 62}[st]
    nx, ny = 70 + 22 * math.sin(math.radians(ang)), 132 - 22 * math.cos(math.radians(ang))
    co2 = kind.startswith("CO2")
    s = '<svg viewBox="0 0 140 300" width="146" height="313">'
    s += '<path d="M44 58 C14 70 12 150 26 230" fill="none" stroke="#2b2b30" stroke-width="9" stroke-linecap="round"/>'
    if co2: s += '<path d="M20 222 l12 0 l6 34 l-24 0 z" fill="#2b2b30"/>'
    s += '<rect x="56" y="36" width="28" height="30" rx="4" fill="#3a3a40"/><path d="M60 30 L112 22 L114 32 L64 40 z" fill="#2b2b30"/><path d="M58 44 L98 54 L96 62 L58 54 z" fill="#55555c"/>'
    s += '<rect x="32" y="64" width="76" height="220" rx="30" fill="url(#rg)" stroke="#7a1010" stroke-width="3"/>'
    s += '<rect x="36" y="160" width="68" height="64" rx="6" fill="#fff8d6"/>'
    s += f'<text x="70" y="188" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="17" fill="#2b2b30"><tspan>{kind.split()[0]}</tspan></text><text x="70" y="212" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="14" fill="#55555c"><tspan>{kind.split()[1]} kg</tspan></text>'
    if not co2:
        s += '<circle cx="70" cy="132" r="25" fill="#fff" stroke="#2b2b30" stroke-width="4"/><path d="M52 124 A20 20 0 0 1 70 112" stroke="#2f9e44" stroke-width="7" fill="none"/><path d="M78 113 A20 20 0 0 1 89 126" stroke="#e03131" stroke-width="7" fill="none"/>'
        s += f'<line x1="70" y1="132" x2="{nx:.1f}" y2="{ny:.1f}" stroke="#2b2b30" stroke-width="4" stroke-linecap="round"/><circle cx="70" cy="132" r="4" fill="#2b2b30"/>'
    else:
        s += '<rect x="44" y="104" width="52" height="40" rx="6" fill="#2b2b30"/><text x="70" y="131" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="14" fill="#fff8d6"><tspan>WEIGH</tspan></text>'
    s += '<defs><linearGradient id="rg" x1="0" x2="1"><stop offset="0" stop-color="#a5161a"/><stop offset=".4" stop-color="#e5383b"/><stop offset="1" stop-color="#a5161a"/></linearGradient></defs></svg>'
    return s
P["p226_extinguisher"] = page("""
body{--f:'Roboto';--h:'Montserrat';background:#fbf7e4;color:#26262b}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#c71f24;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#c71f24}
.vw{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}
.wall{flex:1;min-height:0;background:#e9e6dc;border-radius:28px;padding:16px 20px 18px;display:flex;flex-direction:column;gap:6px;position:relative}
.wall>small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6d6a60}
.rail{height:14px;border-radius:7px;background:linear-gradient(#8e8b82,#5f5c55);margin:4px 0 0}
.cy{flex:1;display:flex;justify-content:space-between;align-items:center}
.cl{width:146px;display:flex;flex-direction:column;align-items:center}
.cl svg{display:block;margin-top:-2px}
.str{width:3px;height:16px;background:#6d6a60}
.tg{width:150px;background:#fff;border-radius:12px;padding:12px 8px;text-align:center;border-top:7px solid #2f9e44}
.tg b{display:block;font:700 16px/1.35 'Roboto';color:#26262b}.tg em{display:block;font:700 18px/1.35 'Montserrat';font-style:normal;color:#2f9e44;margin-top:3px}
.tg.ds{border-top-color:#f08c00}.tg.ds em{color:#d9480f}.tg.od{border-top-color:#c71f24;background:#ffe9e6}.tg.od em{color:#c71f24}
.br{display:flex;gap:16px}
.st{width:330px;flex:none;background:#26262b;color:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:6px}
.st small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#ffd43b}
.st h4{font:800 25px/1.3 'Montserrat'}
.sr{display:flex;align-items:center;gap:14px;border-top:1px solid #3d3d44;padding-top:8px;margin-top:4px}.sr b{font:800 44px/1.3 'Montserrat';width:50px}.sr span{font:500 19px/1.35 'Roboto';color:#d6d6dc}
.sr.y b{color:#ffa94d}.sr.r b{color:#ff6b6b}
.ms{flex:1;min-width:0;background:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:12px;box-shadow:0 14px 30px rgba(38,38,43,.08)}
.ms small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6d6a60}
.bub{background:#f3f1e7;border-radius:18px 18px 18px 6px;padding:16px 18px;font:500 22px/1.45 'Roboto'}.bub b{color:#c71f24}
.lv{margin-top:auto;display:flex;gap:10px;align-items:center;font:600 17px/1.35 Roboto;color:#2f9e44;border-top:1px solid #eee9da;padding-top:10px}.dy{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}.dy span{border:2px solid #e2ddcc;border-radius:12px;padding:13px 0;text-align:center;font:700 17px 'Roboto'}.dy .on{background:#c71f24;border-color:#c71f24;color:#fff}
""", "<div class=kk>FIRE EXTINGUISHER REFILLING · SITE VISITS</div><h1>Refill dates in a diary?<br><span>Let the app remind you.</span></h1>",
f'''<div class=vw><div class=wall><small>SAMPLE OFFICE · 6 CYLINDERS · 3 FLOORS</small><div class=rail></div><div class=cy>
{"".join(f'<div class=cl>{ext(k, s)}<div class=str></div><div class="tg {s}"><b>{a}</b><b style="font-weight:500;color:#6d6a60">{k}</b><em>{d}</em></div></div>' for a,k,d,s in cyl)}</div></div>
<div class=br><div class=st><small>SITE SUMMARY · SAMPLE</small><h4>Sample Office</h4><div class=sr><b>4</b><span>cylinders OK</span></div><div class="sr y"><b>1</b><span>due in December</span></div><div class="sr r"><b>1</b><span>overdue since October</span></div></div>
<div class=ms><small>REMINDER SENT TO THE SITE · SAMPLE</small><div class=bub>Hi, <b>2 cylinders</b> at Sample Office need a refill: F1 Kitchen and F2 Office. Pick a visit day:</div>
<div class=dy><span>Tue 1 Dec</span><span class=on>Thu 3 Dec</span><span>Sat 5 Dec</span></div><div class=lv>{ic("doc",20)}After each refill: new due date and photo saved per cylinder</div></div></div></div>''',
"#26262b", "Refill extinguishers? DM us", "background:#c71f24;color:#fff")

# ───────── 227 INDIA · Bangle wholesaler · CAROUSEL 5 · Cardo + Inter · magenta / emerald / ivory
# New technique: bangles drawn as stacked ellipses on display rods; colour x size order heatmap in dozens; boxes by town dispatch board.
COL = [("Red", "#d62839"), ("Maroon", "#7b1e3a"), ("Green", "#13856b"), ("Royal blue", "#2b4fc7"), ("Gold", "#d4a017"), ("Pink", "#f06ba8")]
ORD = {"Red": (4, 6, 2), "Maroon": (2, 4, 2), "Green": (3, 3, 0), "Royal blue": (2, 2, 2), "Gold": (6, 6, 4), "Pink": (2, 4, 0)}
SZ = ["2.4", "2.6", "2.8"]
def rod(colours, per=4, w=150, h=560, uid="a"):
    n = len(colours) * per
    gap = (h - 120) / n
    s = f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"><rect x="{w/2-6}" y="10" width="12" height="{h-40}" rx="6" fill="#b8a98e"/><ellipse cx="{w/2}" cy="{h-24}" rx="{w/2-8}" ry="16" fill="#8f7f63"/>'
    y = h - 52
    for c in colours:
        for k in range(per):
            s += f'<ellipse cx="{w/2}" cy="{y:.0f}" rx="{w/2-14}" ry="{w/7:.0f}" fill="none" stroke="{c}" stroke-width="{gap*0.8:.0f}"/><ellipse cx="{w/2}" cy="{y-gap*0.25:.0f}" rx="{w/2-14}" ry="{w/7:.0f}" fill="none" stroke="#fff" stroke-opacity=".35" stroke-width="2"/>'
            y -= gap
    return s + '</svg>'
def pair(c, s=1):
    return f'<svg viewBox="0 0 120 80" width="{120*s:.0f}" height="{80*s:.0f}"><ellipse cx="48" cy="44" rx="38" ry="28" fill="none" stroke="{c}" stroke-width="10"/><ellipse cx="72" cy="38" rx="38" ry="28" fill="none" stroke="{c}" stroke-width="10"/><ellipse cx="72" cy="34" rx="36" ry="25" fill="none" stroke="#fff" stroke-opacity=".4" stroke-width="2"/></svg>'
BB = """
body{--f:'Inter';--h:'Cardo';background:#fbf6ec;color:#2a1426}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#13856b;margin-top:22px;align-self:flex-start}
h1{font-family:'Cardo';font-weight:700;font-size:68px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#b0186a}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(42,20,38,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#86707e}
.nb{display:flex;align-items:center;gap:14px;background:#2a1426;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 Inter}.nb .ib{width:50px;height:50px;border-radius:14px;background:#b0186a}
.nb b{color:#ffb3d9}
"""
def bb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#2a1426;color:#fff"):
    return page(BB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2a1426", cta, ctacss, tagline=f"{n} / 5")
rods = "".join(rod([COL[i][1], COL[j][1], COL[k][1]], per=5, uid=str(i)) for i, j, k in [(0, 4, 1), (2, 5, 3), (4, 1, 0)])
P["p227_bangles_s1"] = bb(1, "BANGLE WHOLESALE · RETAILER ORDERS", "Bangle orders by<br>voice note?<br><span>Get them colour by colour.</span>",
f'''<div class=w1><div class="cd rs"><div class=rr>{rods}</div><small class=cap>YOUR STOCK · SAMPLE</small></div>
<div class=ch><small class=cap>WHAT A RETAILER SENDS · SAMPLE</small>
<div class=bu>“Send red ones, same as last time.”<i>Which red?</i></div>
<div class=bu>“Two dozen in 2.6... or was it 2.4?”<i>Which size?</i></div>
<div class=bu>“Green also, the dark one.”<i>How many?</i></div>
<div class=bu>“Send by tomorrow's transport.”<i>To which town?</i></div></div></div>''',
css=""".w1{flex:1;display:flex;gap:16px;min-height:0}.rs{width:400px;flex:none;padding:22px 16px 16px;display:flex;flex-direction:column;align-items:center;justify-content:space-between}
.rr{display:flex;gap:0;align-items:flex-end;justify-content:center}.rr svg{display:block;margin:0 -12px}
.ch{flex:1;min-width:0;display:flex;flex-direction:column;gap:14px;justify-content:center}
.bu{background:#fff;border-radius:22px 22px 22px 6px;padding:16px 20px;font:500 23px/1.4 Inter;box-shadow:0 10px 22px rgba(42,20,38,.07);display:flex;flex-direction:column;gap:8px}
.bu i{align-self:flex-start;font:700 17px Inter;font-style:normal;background:#ffe3f1;color:#b0186a;padding:6px 12px;border-radius:10px}""")

cards = "".join(f'''<div class=pc>{pair(c, 1.15)}<div class=pi><small class=cap>BG-0{i+1}</small><b>{nm}</b><div class=sz>{"".join(f'<span class="{"lo" if (i==1 and z=="2.8") else ""}"><i></i>{z}</span>' for z in SZ)}</div></div></div>''' for i, (nm, c) in enumerate(COL))
P["p227_bangles_s2"] = bb(2, "STEP 1 · YOUR COLOUR LIST", "Retailers pick from<br><span>a clear colour list.</span>",
f'''<div class=w2>{browser(f'<div class=bh><b>Sample Bangles · Wholesale</b><span>Order in dozens</span></div><div class=gr>{cards}</div><div class=lgx><span><i></i>In stock</span><span><i class=l></i>Low stock</span><span>Sizes 2.4, 2.6, 2.8 · sample</span></div>', url="yourbangles.in/order · sample", style="flex:1;min-height:0")}
<div class=nb><span class=ib>{ic("grid",26)}</span><span>Each colour has a code and a photo, so <b>“which red?”</b> never comes up again.</span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bh{display:flex;justify-content:space-between;align-items:center;padding:16px 22px 6px}.bh b{font:700 28px/1.3 Cardo}.bh span{font:700 16px Inter;background:#e5f4ef;color:#13856b;padding:8px 14px;border-radius:12px}
.gr{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-auto-rows:1fr;gap:12px;padding:10px 22px}
.pc{display:flex;align-items:center;gap:14px;border:2px solid #efe6ea;border-radius:18px;padding:10px 16px}
.pi{flex:1;min-width:0}.pi b{display:block;font:700 26px/1.3 Cardo;margin:2px 0 6px}
.sz{display:flex;gap:8px}.sz span{display:flex;align-items:center;gap:6px;font:700 16px Inter;background:#f7f2f4;border-radius:10px;padding:6px 10px}.sz i{width:10px;height:10px;border-radius:50%;background:#13856b}.sz .lo i{background:#f08c00}
.lgx{display:flex;gap:22px;padding:8px 22px 16px;font:600 16px Inter;color:#86707e}.lgx span{display:flex;align-items:center;gap:8px}.lgx i{width:12px;height:12px;border-radius:50%;background:#13856b}.lgx i.l{background:#f08c00}""")

mx = max(max(v) for v in ORD.values())
rows = "".join(f'''<div class=hr><span class=hn><i style="background:{c}"></i>{nm}</span>{"".join(f'<span class=hc style="background:rgba(176,24,106,{(q/mx)*0.85+0.06 if q else 0:.2f});color:{"#fff" if q/mx>0.5 else "#2a1426"}">{q if q else "—"}</span>' for q in ORD[nm])}<span class=ht>{sum(ORD[nm])}</span></div>''' for nm, c in COL)
ct = [sum(ORD[nm][k] for nm, _ in COL) for k in range(3)]
P["p227_bangles_s3"] = bb(3, "STEP 2 · ONE ORDER SHEET", "Colour × size,<br><span>in dozens. No guessing.</span>",
f'''<div class=w3><div class="cd hm"><div class=hh><div><small class=cap>SAMPLE BANGLE STORE · TOWN A</small><b>Order ORD-227</b></div><em>Mon 23 Nov</em></div>
<div class="hr hx"><span class=hn>COLOUR</span>{"".join(f'<span class=hc>{z}</span>' for z in SZ)}<span class=ht>DOZEN</span></div>{rows}
<div class="hr tt"><span class=hn>Total</span>{"".join(f'<span class=hc>{t}</span>' for t in ct)}<span class=ht>{sum(ct)}</span></div></div>
<div class=sx><div><b>{sum(ct)}</b><span>dozen in total</span></div><div><b>6</b><span>boxes, one per colour</span></div><div><b>1</b><span>town to send to</span></div></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hm{flex:1;padding:18px 24px;display:flex;flex-direction:column;gap:6px}
.hh{display:flex;justify-content:space-between;align-items:flex-end;padding-bottom:8px}.hh b{display:block;font:700 34px/1.3 Cardo}.hh em{font:700 18px Inter;font-style:normal;color:#13856b}
.hr{flex:1;display:grid;grid-template-columns:1fr 130px 130px 130px 120px;gap:8px;align-items:stretch}
.hn{display:flex;align-items:center;gap:12px;font:700 23px Inter}.hn i{width:30px;height:30px;border-radius:50%;flex:none;border:3px solid #fff;box-shadow:0 0 0 2px #e8dde2}
.hc{display:flex;align-items:center;justify-content:center;border-radius:12px;font:800 26px Inter}
.ht{display:flex;align-items:center;justify-content:center;font:800 26px Inter;color:#13856b}
.hx{flex:none}.hx .hn,.hx .hc,.hx .ht{font:700 15px/1.4 Inter;letter-spacing:2px;color:#86707e;padding:4px 0}
.tt{border-top:2px solid #2a1426;padding-top:6px}.tt .hc{background:#2a1426;color:#fff}.tt .ht{color:#b0186a}
.sx{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.sx div{background:#13856b;color:#fff;border-radius:20px;padding:14px 18px;display:flex;align-items:center;gap:14px}
.sx b{font:700 52px/1.3 Cardo}.sx span{font:600 19px/1.35 Inter}""")

boxes = [(nm, c, sum(ORD[nm]), sum(ORD[nm]) - (2 if nm == "Maroon" else 0)) for nm, c in COL]
bx = "".join(f'''<div class="bx{" sh" if p < q else ""}"><div class=bt style="background:{c}"></div><div class=bl><b>{nm}</b><span>{p} of {q} dozen</span></div><i>{ic("check",18,w=3) if p==q else "!"}</i></div>''' for nm, c, q, p in boxes)
towns = [("Town A", [("ORD-227", "Sample Bangle Store", "6 boxes", True), ("ORD-229", "Sample Gift Corner", "3 boxes", False)]), ("Town B", [("ORD-230", "Sample Fancy Store", "4 boxes", False)]), ("Town C", [("ORD-231", "Sample Bangle House", "2 boxes", False)])]
tw = "".join(f'''<div class=tn><small class=cap>{t.upper()}</small>{"".join(f'<div class="to{" me" if me else ""}"><b>{o}</b><span>{s}<small>LR-{o[-3:]}1 · sample</small></span><em>{b}</em></div>' for o,s,b,me in L)}</div>''' for t, L in towns)
P["p227_bangles_s4"] = bb(4, "STEP 3 · PACK AND DISPATCH", "Pack box by box,<br><span>send town by town.</span>",
f'''<div class=w4c><div class=w4><div class="cd pk"><small class=cap>ORD-227 · PACKING CHECK</small>{bx}</div>
<div class="cd db"><div class=dh><small class=cap>DISPATCH BOARD · TUE 24 NOV</small><b>Sample Transport</b></div>{tw}</div></div>
<div class=nb><span class=ib>{ic("box",26)}</span><span><b>Maroon 2.8 · 2 dozen short.</b> It moves to the store's next order by itself.</span></div></div>''',
css=""".w4c{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.w4{flex:1;display:flex;gap:14px;min-height:0}.pk{width:420px;flex:none;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.bx{flex:1;display:flex;align-items:center;gap:14px;background:#f3ead7;border-radius:14px;padding:0 14px 0 0;overflow:hidden;border:2px solid #d9c7a3}
.bt{width:26px;align-self:stretch;flex:none}.bl{flex:1}.bl b{display:block;font:700 22px/1.3 Inter}.bl span{font:500 17px/1.3 Inter;color:#6f5b4a}
.bx>i{width:34px;height:34px;border-radius:50%;background:#13856b;color:#fff;display:flex;align-items:center;justify-content:center;font:800 20px Inter;font-style:normal;flex:none}
.bx.sh{background:#ffe3f1;border-color:#f3a3cb}.bx.sh>i{background:#b0186a}.bx.sh span{color:#b0186a;font-weight:700}
.db{flex:1;min-width:0;padding:18px 20px;display:flex;flex-direction:column;gap:10px}.dh b{display:block;font:700 28px/1.3 Cardo}
.tn{flex:1;display:flex;flex-direction:column;gap:6px;border-top:2px dashed #e3d6dc;padding-top:8px}
.to{flex:1;display:grid;grid-template-columns:96px 1fr auto;align-items:center;gap:10px;background:#f7f2f4;border-radius:12px;padding:0 14px}
.to b{font:800 16px Inter;color:#86707e}.to span{font:600 20px/1.3 Inter}.to span small{display:block;font:500 15px/1.4 Inter;color:#86707e;margin-top:2px}.to.me span small{color:#e0c4d4}.to em{font:700 16px Inter;font-style:normal;color:#13856b}
.to.me{background:#2a1426}.to.me b{color:#ffb3d9}.to.me span,.to.me em{color:#fff}""")

P["p227_bangles_s5"] = bb(5, "YOUR TURN", "Sell bangles wholesale?<br><span>Let's build your order app.</span>",
f'''<div class=w5><div class="cd rs5"><div class=rr>{rod([COL[0][1], COL[4][1], COL[2][1], COL[5][1]], per=5, w=170, h=760)}{rod([COL[3][1], COL[1][1], COL[4][1], COL[0][1]], per=5, w=170, h=760)}</div></div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,40)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Colour list","Codes, photos, sizes"),("doc","Order sheet","Colour × size in dozens"),("check","Packing check","Short items move ahead"),("truck","Dispatch board","Boxes by town and transport")])}
<div class=q>How do retailers order from you today? Tell us in the comments.</div></div></div>''',
cta="DM us to start", ctacss="background:#b0186a;color:#fff",
css=""".w5{flex:1;display:flex;gap:16px;min-height:0}.rs5{width:380px;flex:none;display:flex;align-items:center;justify-content:center}.rr{display:flex}.rr svg{display:block;margin:0 -14px}
.tl{flex:1;display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:0 20px;box-shadow:0 10px 22px rgba(42,20,38,.07)}
.ti .ib{width:76px;height:76px;border-radius:20px;background:#ffe3f1;color:#b0186a}.ti b{display:block;font:700 32px/1.3 Cardo}.ti span{font:500 19px/1.35 Inter;color:#6f5b6a}
.q{background:#13856b;color:#fff;border-radius:22px;padding:20px 22px;font:700 24px/1.4 Inter}""")

# ───────── 228 CANADA · Gutter cleaning · SINGLE · Anton + Source Sans 3 · slate roof / autumn orange / sky white
# New technique: one street drawn as a row of house elevations with leaf-filled vs clean gutters and a numbered route along the road.
st228 = [("done", "Done", "Photos sent"), ("done", "Done", "Photos sent"), ("now", "Now", "11:00 AM"), ("next", "Next", "1:00 PM"), ("next", "Next", "2:30 PM")]
def street():
    s = '<svg viewBox="0 0 960 360" class=sv><rect width="960" height="360" fill="#dfe9f1"/><rect y="292" width="960" height="68" fill="#4a535e"/><line x1="20" y1="326" x2="940" y2="326" stroke="#f3f6f8" stroke-width="4" stroke-dasharray="26 18"/>'
    s += '<rect y="276" width="960" height="16" fill="#9bb07a"/>'
    random.seed(228)
    for i, (k, _, _) in enumerate(st228):
        x = 22 + i * 186; w = 170; roof = ["#3d4652", "#5a4637", "#3d4652", "#6b3f2f", "#4d5a48"][i]; wall = ["#f3e3c3", "#e7eef3", "#f6d7b8", "#efe7da", "#dde6ea"][i]
        s += f'<rect x="{x+14}" y="150" width="{w-28}" height="126" fill="{wall}" stroke="#2c333b" stroke-width="3"/>'
        s += f'<path d="M{x} 156 L{x+w/2} 70 L{x+w} 156 Z" fill="{roof}" stroke="#2c333b" stroke-width="3"/>'
        s += f'<rect x="{x+w/2-18}" y="214" width="36" height="62" fill="#8a5a3c" stroke="#2c333b" stroke-width="3"/><rect x="{x+28}" y="176" width="34" height="30" fill="#bcd6ea" stroke="#2c333b" stroke-width="3"/><rect x="{x+w-62}" y="176" width="34" height="30" fill="#bcd6ea" stroke="#2c333b" stroke-width="3"/>'
        s += f'<rect x="{x-4}" y="154" width="{w+8}" height="12" rx="3" fill="#c9d1d8" stroke="#2c333b" stroke-width="3"/><rect x="{x+w-2}" y="160" width="9" height="116" fill="#c9d1d8" stroke="#2c333b" stroke-width="2.5"/>'
        if k != "done":
            for j in range(9):
                lx = x + 6 + j * 19 + random.uniform(-3, 3)
                s += f'<ellipse cx="{lx:.0f}" cy="{152+random.uniform(-2,2):.0f}" rx="9" ry="5" fill="{random.choice(["#e8772e","#c94f1a","#d9a520"])}" transform="rotate({random.randint(-30,30)} {lx:.0f} 152)"/>'
        pc = {"done": "#2f9e44", "now": "#e8772e", "next": "#3d4652"}[k]
        s += f'<circle cx="{x+w/2}" cy="40" r="24" fill="{pc}" stroke="#fff" stroke-width="4"/><text x="{x+w/2}" y="49" text-anchor="middle" font-family="Anton" font-size="26" fill="#fff"><tspan>{i+1}</tspan></text>'
    s += '<path d="M60 310 L900 310" stroke="#e8772e" stroke-width="6" stroke-dasharray="2 14" stroke-linecap="round"/><path d="M890 300 l18 10 l-18 10 z" fill="#e8772e"/></svg>'
    return s
leaves = lambda n: "".join(f'<i class=free style="left:{8+j*11}%;transform:rotate({(j*37)%60-30}deg);background:{["#e8772e","#c94f1a","#d9a520"][j%3]}"></i>' for j in range(n))
P["p228_gutter"] = page("""
body{--f:'Source Sans 3';--h:'Anton';background:#f3f6f8;color:#2c333b}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#c9581a;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#e8772e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sp{background:#fff;border-radius:26px;padding:14px 16px 16px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(44,51,59,.08)}
.sp>small,.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b7580}
.sv{width:100%;display:block;border-radius:16px}
.chs{display:grid;grid-template-columns:repeat(5,1fr);gap:8px}
.chs div{border-radius:14px;padding:8px 10px;text-align:center;background:#eef2f5}.chs b{display:block;font:400 22px/1.4 'Anton';letter-spacing:.5px}.chs span{font:600 16px/1.3 'Source Sans 3';color:#55606b}
.chs .done{background:#e3f4e6}.chs .done b{color:#2f9e44}.chs .now{background:#e8772e}.chs .now b,.chs .now span{color:#fff}
.bt{flex:1;min-height:0;display:flex;gap:14px}
.jb{flex:1;min-width:0;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(44,51,59,.08)}
.jb h4{font:400 28px/1.4 'Anton';letter-spacing:.5px}
.ph{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.pf{border-radius:16px;background:linear-gradient(#bcd6ea 0 45%,#3d4652 45% 100%);position:relative;overflow:hidden}
.pf .gt{position:absolute;left:8%;right:8%;top:40%;height:44px;background:#c9d1d8;border:4px solid #2c333b;border-top:0;border-radius:0 0 14px 14px}
.pf .gt i{position:absolute;top:2px;width:30px;height:18px;border-radius:50%}
.pf em{position:absolute;left:12px;bottom:12px;font:700 16px 'Source Sans 3';font-style:normal;background:#fff;color:#2c333b;padding:5px 12px;border-radius:10px}
.pf.af em{background:#2f9e44;color:#fff}
.sn{width:330px;flex:none;background:#2c333b;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.sn small{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#ffb27a}
.sn .rw{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #444d57;font:600 20px/1.35 'Source Sans 3'}.sn .rw .ib{width:40px;height:40px;border-radius:12px;background:#e8772e}
""", "<div class=kk>GUTTER CLEANING · FALL ROUTE</div><h1>Gutter calls all fall?<br><span>Book them street by street.</span></h1>",
f'''<div class=vw><div class=sp><small>TODAY · SAMPLE STREET · 5 HOMES IN ONE ROUTE</small>{street()}
<div class=chs>{"".join(f'<div class={k}><b>{i+1} · {a}</b><span>{b}</span></div>' for i,(k,a,b) in enumerate(st228))}</div></div>
<div class=bt><div class=jb><small class=cap>JOB 2 · 14 SAMPLE STREET · PHOTOS SENT TO THE OWNER</small><div class=ph><div class=pf><div class=gt>{leaves(8)}</div><em>Before</em></div><div class="pf af"><div class=gt></div><em>After</em></div></div></div>
<div class=sn><small>EVERY BOOKING · SAMPLE</small>{"".join(f'<div class=rw><span class=ib>{ic(i,22)}</span>{t}</div>' for i,t in [("pin","Grouped by street"),("camera","Before and after photos"),("bell","Spring round reminder")])}</div></div></div>''',
"#2c333b", "Clean gutters? DM us", "background:#e8772e;color:#fff")

# ───────── 229 INDIA · Mobile tyre puncture van · SINGLE · DM Sans + Fira Sans · rubber black / safety orange / concrete · PHONE
# New technique: van stock drawn as tube rings per size with low-stock flag, paired with a phone booking page that has a drawn location map.
def tube(c="#1c1c1e", s=46):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 40 40"><circle cx="20" cy="20" r="15" fill="none" stroke="{c}" stroke-width="8"/><rect x="18" y="1" width="4" height="7" rx="1" fill="#8a8a8a"/></svg>'
stock = [("Bike tubes 2.75-18", 3, 6, False), ("Scooter tubes 3.00-10", 1, 6, True), ("Car tubeless plugs", 6, 6, False)]
jobs = [("9:10 AM", "Bike · Sample Road", "Tube changed", "d"), ("10:05 AM", "Car · Highway km 12", "Tubeless plug", "d"), ("11:30 AM", "Scooter · Market area", "Tube changed", "d"), ("12:20 PM", "Car · Sample Colony", "On the way", "n")]
mp = '<svg viewBox="0 0 300 190" class=mp><rect width="300" height="190" fill="#ece8e1"/><path d="M0 120 L300 70" stroke="#fff" stroke-width="22"/><path d="M110 0 L150 190" stroke="#fff" stroke-width="16"/><path d="M0 40 L300 160" stroke="#fff" stroke-width="10"/><path d="M60 104 C120 96 150 90 205 78" stroke="#ff7a1a" stroke-width="5" stroke-dasharray="8 7" fill="none"/>'
mp += '<g transform="translate(205 78)"><path d="M0 -40 C-16 -40 -22 -26 -22 -20 C-22 -8 0 10 0 10 C0 10 22 -8 22 -20 C22 -26 16 -40 0 -40 Z" fill="#e03131"/><circle cx="0" cy="-21" r="8" fill="#fff"/></g>'
mp += '<g transform="translate(46 96)"><rect x="-4" y="0" width="40" height="22" rx="5" fill="#1c1c1e"/><rect x="26" y="4" width="14" height="10" rx="2" fill="#ff7a1a"/><circle cx="6" cy="24" r="5" fill="#555"/><circle cx="28" cy="24" r="5" fill="#555"/></g></svg>'
P["p229_puncture"] = page("""
body{--f:'Fira Sans';--h:'DM Sans';background:#e9e6e1;color:#1c1c1e}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#d9480f;margin-top:22px}
h1{font-family:'DM Sans';font-weight:800;font-size:62px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#d9480f}
.vw{flex:1;display:flex;gap:18px;min-height:0}
.lf{flex:1;min-width:0;display:flex;flex-direction:column;gap:14px}
.vk{background:#1c1c1e;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.vk small,.jl small{font:700 14px/1.4 'Fira Sans';letter-spacing:2px;color:#ffa94d}
.sk{display:flex;flex-direction:column;gap:4px}.sk b{font:600 19px/1.35 'Fira Sans'}.sk .tb{display:flex;gap:4px;align-items:center}.sk .tb svg{display:block}
.sk.lo b{color:#ffa94d}.sk .tb em{font:700 15px 'Fira Sans';font-style:normal;background:#ff7a1a;color:#1c1c1e;padding:4px 10px;border-radius:8px;margin-left:8px}
.jl{flex:1;min-height:0;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.jl small{color:#86807a}
.jr{flex:1;display:grid;grid-template-columns:92px 1fr;gap:2px 10px;align-content:center;border-top:1px solid #eee9e2}
.jr b{font:700 17px/1.35 'Fira Sans';color:#86807a;grid-row:span 2;align-self:center}.jr span{font:700 19px/1.3 'DM Sans'}.jr em{font:500 16px/1.3 'Fira Sans';font-style:normal;color:#2f9e44}
.jr.n em{color:#d9480f;font-weight:700}
.ap{flex:1;padding:6px 16px 16px;display:flex;flex-direction:column;gap:9px}
.ap h4{font:800 21px/1.3 'DM Sans'}.ap small{font:700 12px/1.4 'Fira Sans';letter-spacing:1.5px;color:#86807a}
.mp{width:100%;display:block;border-radius:14px}
.lc{display:flex;align-items:center;gap:8px;font:700 15px 'Fira Sans';color:#2f9e44}
.cs{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.cs span{text-align:center;border:2px solid #e6e1d9;border-radius:10px;padding:7px 0;font:600 14px 'Fira Sans'}.cs .on{background:#1c1c1e;border-color:#1c1c1e;color:#fff}
.rw2{display:flex;justify-content:space-between;border:2px solid #e6e1d9;border-radius:10px;padding:8px 12px;font:500 15px 'Fira Sans'}.rw2 b{font-weight:700}.eta{background:#fff1e6;border-radius:12px;padding:10px 12px;font:600 15px/1.4 'Fira Sans'}.eta b{color:#d9480f}
.bt{margin-top:auto;background:#ff7a1a;color:#1c1c1e;border-radius:12px;padding:12px;text-align:center;font:800 16px 'DM Sans'}
""", "<div class=kk>MOBILE TYRE PUNCTURE VAN · CALL BOOKING</div><h1>Puncture calls start with<br>“Where are you?”<br><span>Get a location pin.</span></h1>",
f'''<div class=vw><div class=lf><div class=vk><small>VAN 2 · STOCK RIGHT NOW · SAMPLE</small>
{"".join(f'<div class="sk{" lo" if lo else ""}"><b>{a} · {n} left</b><div class=tb>{"".join(tube("#ff7a1a" if k<n else "#4a4a4e", 40) for k in range(m))}{"<em>Reorder</em>" if lo else ""}</div></div>' for a,n,m,lo in stock)}</div>
<div class=jl><small>TODAY'S JOBS · VAN 2 · SAMPLE</small>{"".join(f'<div class="jr {k}"><b>{t}</b><span>{a}</span><em>{b}</em></div>' for t,a,b,k in jobs)}</div></div>
{phone(f"""<div class=ap><h4>Book puncture help</h4><small>SAMPLE BOOKING PAGE</small>{mp}<div class=lc>{ic("pin",18)}Location shared</div>
<div class=cs><span>Bike</span><span>Scooter</span><span class=on>Car</span></div><div class=cs><span class=on>Tubeless</span><span>Tube</span><span>Not sure</span></div>
<div class=rw2><span>Which tyre</span><b>Front left</b></div><div class=rw2><span>Landmark</span><b>Near the bus stop</b></div><div class=eta><b>Van 2 is on the way.</b> You can see it move on the map.</div><div class=bt>Call the driver</div></div>""", w=330, h=700)}</div>''',
"#1c1c1e", "Run a puncture van? DM us", "background:#1c1c1e;color:#fff")

# ───────── 230 INDIA · Second-hand book seller · SINGLE · Lora + Open Sans · paper cream / library green / oxblood
# New technique: bookshelf of vertical spines (writing-mode vertical-rl) with one spine found and pinned, plus a browser search result list.
random.seed(230)
titles = ["Short Stories", "Old Atlas", "Cookbook", "Poems", "Sample Novel", "Travel Diary", "Art Book", "Dictionary", "History Notes", "Garden Guide", "Eng. Physics", "Puzzles", "Letters", "Sea Tales", "Big Maths", "Film Notes",
          "Sample Novel II", "Bird Guide", "Word Games", "Sketch Book", "City Walks", "Old Recipes", "Night Sky", "Folk Tales", "Chess Guide", "Essays", "Tea Notes", "Rail Maps", "Grammar", "Quiz Book", "Stamps", "Poems II"]
SPC = ["#1f4d3a", "#7a1f2b", "#c08a2c", "#2f4b7a", "#5b3a29", "#3b6b5a", "#a2462e", "#6a5a8a", "#2a2a2a", "#8a7a52"]
def shelf(ts, hit=None, lab=""):
    out = ""
    for i, t in enumerate(ts):
        w = random.choice([44, 48, 52]); h = random.choice([170, 182, 194, 206]); c = "#2f4b7a" if t == hit else SPC[(i * 7 + 3) % len(SPC)]
        hcls = " hit" if t == hit else ""
        out += f'<div class="sb{hcls}" style="width:{w}px;height:{h}px;background:{c}"><span>{t}</span></div>'
    return out
P["p230_books"] = page("""
body{--f:'Open Sans';--h:'Lora';background:#f5efe2;color:#22271f}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#7a1f2b;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:66px;letter-spacing:-.8px;line-height:1.22} h1 span{color:#1f4d3a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bk{background:#6b4a2f;border-radius:22px;padding:14px 18px 0;display:flex;flex-direction:column;box-shadow:inset 0 0 0 8px #5a3d26}
.bk>small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#f1d9b5;padding:0 6px 6px}
.row{display:flex;align-items:flex-end;gap:3px;padding:0 10px;height:214px;border-bottom:16px solid #4a321e;position:relative}
.rl{position:absolute;left:-8px;top:8px;font:700 15px/1.4 'Open Sans';color:#f1d9b5;writing-mode:vertical-rl;transform:rotate(180deg)}
.sb{flex:none;border-radius:4px 4px 0 0;display:flex;align-items:center;justify-content:center;box-shadow:inset -5px 0 0 rgba(0,0,0,.18),inset 3px 0 0 rgba(255,255,255,.12);position:relative}
.sb span{writing-mode:vertical-rl;transform:rotate(180deg);font:600 15px/1.2 'Open Sans';color:#f8f1e3;white-space:nowrap;letter-spacing:.5px}
.sb.hit{outline:5px solid #ffd166;outline-offset:2px;z-index:2}
.bhd{display:flex;justify-content:space-between;align-items:center;padding:0 6px 10px}.bhd small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#f1d9b5}.fd{background:#ffd166;color:#22271f;border-radius:14px;padding:8px 14px;font:700 17px/1.35 'Open Sans';display:flex;gap:8px;align-items:center}
.sr{flex:1;min-height:0;display:flex;flex-direction:column}
.sq{display:flex;align-items:center;gap:12px;margin:14px 20px 6px;border:2px solid #1f4d3a;border-radius:14px;padding:10px 14px;font:600 21px 'Open Sans'}.sq em{margin-left:auto;font:700 15px 'Open Sans';font-style:normal;color:#7a1f2b}
.rs{flex:1;display:flex;flex-direction:column;padding:4px 20px 14px}
.re{flex:1;display:grid;grid-template-columns:52px 1fr auto;gap:16px;align-items:center;border-bottom:1px solid #efe7d6}.re:last-child{border:0}
.re i{width:42px;height:58px;border-radius:3px;box-shadow:inset -5px 0 0 rgba(0,0,0,.2)}
.re b{display:block;font:700 23px/1.3 'Lora'}.re span{font:500 17px/1.35 'Open Sans';color:#5e6458}
.re em{font:700 16px 'Open Sans';font-style:normal;padding:8px 14px;border-radius:12px;background:#e4efe8;color:#1f4d3a;white-space:nowrap}
.re.sel em{background:#1f4d3a;color:#fff}
""", "<div class=kk>SECOND-HAND BOOK SHOP · ONLINE SHELF</div><h1>“Do you have this book?”<br><span>Let them search your shelf.</span></h1>",
f'''<div class=vw><div class=bk><div class=bhd><small>YOUR SHOP · SHELF A AND B · SAMPLE</small><div class=fd>{ic("pin",18)}Found: Shelf B, spot 7</div></div>
<div class=row>{shelf(titles[:16])}</div><div class=row>{shelf(titles[16:], hit="Night Sky")}</div></div>
{browser(f"""<div class=sr><div class=sq>{ic("search",22)}night sky<em>3 copies · sample</em></div><div class=rs>
<div class="re sel"><i style="background:#2f4b7a"></i><div><b>Night Sky · paperback</b><span>Like new · Shelf B, spot 7</span></div><em>Hold for 24 hours</em></div>
<div class=re><i style="background:#1f4d3a"></i><div><b>Night Sky · hardcover</b><span>Good · a few notes inside · Shelf A, spot 3</span></div><em>Ask on chat</em></div>
<div class=re><i style="background:#7a1f2b"></i><div><b>Night Sky · old edition</b><span>Fair · cover worn · Store room</span></div><em>Ask on chat</em></div></div></div>""", url="yourbookshop.in/search · sample", style="flex:1;min-height:0")}</div>''',
"#22271f", "Sell used books? DM us", "background:#1f4d3a;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
