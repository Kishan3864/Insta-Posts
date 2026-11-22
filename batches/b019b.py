import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 112 INDIA · Grocery wholesaler · CAROUSEL 5 · Poppins + Source Sans 3 · jute / forest / brick
# New techniques: SVG jute sack stack with stencil labels and weave texture; credit-limit bars with hold state; van loading totals.
GW = """
body{--f:'Source Sans 3';--h:'Poppins';background:#efe3cc;color:#1d2b22}
h1{font-family:'Poppins';font-weight:800;font-size:60px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#b5452c}
.sub{color:#5d5544}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Source Sans 3';letter-spacing:3px;color:#1f4d38}
.kt b{width:44px;height:44px;border-radius:12px;background:#1f4d38;color:#efe3cc;font:800 22px/1 Poppins;display:flex;align-items:center;justify-content:center}
.cd{background:#fffaf0;border-radius:22px;box-shadow:0 14px 30px rgba(29,43,34,.08)}
.lb{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#8f866f}
"""
def gw(n, head, vis, css="", cta="Swipe", ctacss="background:#1f4d38;color:#efe3cc"):
    return page(GW + css, head, vis, "#1d2b22", cta, ctacss, tagline=f"{n} / 5")
def sack(x, y, w, h, l1, l2, col="#d2b07a"):
    return (f'<g transform="translate({x},{y})"><path d="M10 18 Q{w/2} 0 {w-10} 18 L{w} {h-16} Q{w/2} {h+8} 0 {h-16} Z" fill="{col}" stroke="#9c7a45" stroke-width="3"/>'
            f'<path d="M10 18 Q{w/2} 0 {w-10} 18 L{w} {h-16} Q{w/2} {h+8} 0 {h-16} Z" fill="url(#wv)"/>'
            f'<path d="M{w/2-24} 6 Q{w/2} -10 {w/2+24} 6" stroke="#9c7a45" stroke-width="5" fill="none"/>'
            f'<text x="{w/2}" y="{h/2}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="{w*0.14:.0f}" fill="#1f4d38" opacity=".85">{l1}</text>'
            f'<text x="{w/2}" y="{h/2+w*0.15:.0f}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="{w*0.1:.0f}" fill="#b5452c" opacity=".9">{l2}</text></g>')
sacks = ('<svg viewBox="0 0 640 440" width="{w}" height="{h}"><defs><pattern id="wv" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 4 H8 M4 0 V8" stroke="#8a6a3a" stroke-width="1" opacity=".25"/></pattern></defs>'
         + sack(20, 230, 200, 200, "SUGAR", "50 kg") + sack(220, 230, 200, 200, "ATTA", "50 kg", "#dcc08f") + sack(420, 230, 200, 200, "RICE", "25 kg")
         + sack(120, 60, 200, 200, "DAL", "30 kg", "#dcc08f") + sack(320, 60, 200, 200, "SALT", "25 kg") + '</svg>')
P["p112_grocery_s1"] = gw(1, """<h1>Shop orders on 30 calls<br>every morning?<br><span>Let shops order from<br>their own phone.</span></h1>""",
f'''<div class=w1><div class=sk1>{sacks.format(w=760,h=522)}</div>
<div class=sd1>{"".join(f'<div class="cd s1"><b>{a}</b><span>{b}</span></div>' for a,b in [("Order app","Shops pick items and packs"),("Credit check","Before you load the van"),("Loading list","Per route, ready by 7 am")])}</div></div>''',
""".w1{flex:1;display:flex;flex-direction:column;gap:16px}
.sk1{flex:1;background:#1f4d38;border-radius:30px;display:flex;align-items:center;justify-content:center}.sk1 svg{display:block}
.sd1{flex:none;display:flex;gap:14px}
.s1{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px;border-top:10px solid #b5452c}
.s1 b{font:800 27px/1.25 Poppins}.s1 span{font:500 20px/1.35 'Source Sans 3';color:#5d5544}
""")

cat = [("Sugar", "50 kg bag", 4), ("Atta", "10 kg bag", 10), ("Toor dal", "30 kg bag", 1), ("Salt", "1 kg x 25", 2), ("Rice", "25 kg bag", 3)]
P["p112_grocery_s2"] = gw(2, """<div class=kt><b>1</b>ORDER APP</div><h1 style="margin-top:18px">The shop orders.<br><span>You get a clear list.</span></h1>""",
f'''<div class=w2>{phone(f"""<div class=ap2><div class=hd2><b>Your Wholesale</b><span>Sample Store 3 · sample</span></div>
{"".join(f'<div class=it2><div><b>{a}</b><span>{b}</span></div><div class=st2><i>–</i><em>{q}</em><i>+</i></div></div>' for a,b,q in cat)}
<div class=bt2>Send order · deliver tomorrow</div></div>""", w=370, h=740)}
<div class=sd2>{"".join(f'<div class="cd s2"><b>{a}</b><span>{b}</span></div>' for a,b in [("Last order, one tap","Most shops order the same list."),("Packs and bag sizes","No “which size?” calls."),("Cut-off time","Orders after 9 pm go the next day.")])}</div></div>''',
""".w2{flex:1;display:flex;gap:24px;align-items:center}
.ap2{flex:1;padding:12px 16px 16px;display:flex;flex-direction:column;gap:9px;background:#f7f2e6}
.hd2{display:flex;flex-direction:column;gap:2px;padding:4px 2px}.hd2 b{font:800 21px Poppins}.hd2 span{font:600 15px 'Source Sans 3';color:#8f866f}
.it2{flex:1;background:#fff;border-radius:14px;padding:0 14px;display:flex;justify-content:space-between;align-items:center}
.it2 div:first-child{display:flex;flex-direction:column}.it2 b{font:700 19px 'Source Sans 3'}.it2 span{font:500 15px 'Source Sans 3';color:#8f866f}
.st2{display:flex;align-items:center;gap:8px}.st2 i{width:30px;height:30px;border-radius:8px;border:2px solid #d8ccb3;font:700 18px/26px 'Source Sans 3';font-style:normal;text-align:center}
.st2 em{font-style:normal;font:800 18px Poppins;width:24px;text-align:center}
.bt2{background:#1f4d38;color:#fff;border-radius:14px;text-align:center;font:700 17px 'Source Sans 3';padding:13px}
.sd2{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.s2{flex:1;padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:10px solid #1f4d38}
.s2 b{font:800 28px/1.25 Poppins}.s2 span{font:500 21px/1.4 'Source Sans 3';color:#5d5544}
""")

cr = [("Sample Kirana 1", 35, "ok", "Load"), ("Sample Kirana 2", 62, "ok", "Load"), ("Sample Store 3", 88, "md", "Load · remind"), ("Sample Mart 4", 100, "hi", "Hold · limit reached"), ("Sample Kirana 5", 20, "ok", "Load")]
P["p112_grocery_s3"] = gw(3, """<div class=kt><b>2</b>CREDIT CHECK</div><h1 style="margin-top:18px">Know who is at<br><span>their credit limit.</span></h1>""",
f'''<div class="cd cr3"><div class=h3r><span class=lb>CREDIT USED · SAMPLE</span><span class=lb>BEFORE LOADING</span></div>
{"".join(f'<div class="r3 {k}"><b>{a}</b><div class=br3><u><s style="width:{p}%"></s></u><span>{p}% of limit</span></div><em>{t}</em></div>' for a,p,k,t in cr)}</div>
<div class=nt3>Set a limit per shop. The app tells you before the goods leave, not after.</div>''',
""".vis{flex-direction:column;gap:14px}
.cr3{flex:1;padding:18px 24px;display:flex;flex-direction:column}
.h3r{display:flex;justify-content:space-between;padding-bottom:8px}
.r3{flex:1;display:flex;align-items:center;gap:18px;border-top:1.5px solid #ece3cf}
.r3 b{width:230px;flex:none;font:700 25px 'Source Sans 3'}
.br3{flex:1;display:flex;flex-direction:column;gap:6px}.br3 u{display:block;height:16px;border-radius:8px;background:#ece3cf;position:relative;overflow:hidden}
.br3 s{position:absolute;left:0;top:0;bottom:0;background:#1f4d38;border-radius:8px}
.br3 span{font:600 17px 'Source Sans 3';color:#5d5544}
.md .br3 s{background:#d99a2b}.hi .br3 s{background:#b5452c}
.r3 em{width:230px;flex:none;text-align:center;font-style:normal;font:700 19px 'Source Sans 3';padding:9px 0;border-radius:10px;background:#e3efe6;color:#1f4d38}
.md em{background:#fbecd0;color:#8a5a0c}.hi em{background:#b5452c;color:#fff}
.nt3{flex:none;background:#1f4d38;color:#efe3cc;border-radius:18px;padding:16px 22px;font:600 21px/1.4 'Source Sans 3'}
""")

load = [("Sugar 50 kg", "12 bags"), ("Atta 10 kg", "40 bags"), ("Toor dal 30 kg", "5 bags"), ("Rice 25 kg", "14 bags"), ("Salt 1 kg x 25", "9 bundles")]
drops = ["Sample Kirana 5", "Sample Kirana 1", "Sample Store 3", "Sample Kirana 2"]
P["p112_grocery_s4"] = gw(4, """<div class=kt><b>3</b>LOADING LIST</div><h1 style="margin-top:18px">One list to load the van,<br><span>in drop order.</span></h1>""",
f'''<div class=w4><div class="cd ld4"><span class=lb>VAN 2 · ROUTE EAST · SAMPLE</span><h3>Load the van</h3>
{"".join(f'<div class=l4><span>{a}</span><b>{b}</b></div>' for a,b in load)}</div>
<div class=dp4><span class=lb>DROP ORDER</span>{"".join(f'<div class=d4><em>{i}</em><b>{d}</b></div>' for i,d in enumerate(drops,1))}<div class="d4 hd4"><em>!</em><b>Sample Mart 4 · on hold</b></div></div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.ld4{flex:1.2;padding:20px 24px;display:flex;flex-direction:column;gap:4px}.ld4 h3{font:800 32px/1.25 Poppins;padding-bottom:6px}
.l4{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1.5px dashed #e0d5bd;font:500 23px 'Source Sans 3'}.l4 b{font:800 24px Poppins;color:#1f4d38}
.dp4{flex:1;background:#1f4d38;color:#fff;border-radius:22px;padding:20px;display:flex;flex-direction:column;gap:10px}.dp4 .lb{color:#b9cfc2}
.d4{flex:1;background:#2a5e46;border-radius:14px;display:flex;align-items:center;gap:14px;padding:0 16px}
.d4 em{width:40px;height:40px;border-radius:50%;background:#efe3cc;color:#1f4d38;font:800 20px/1 Poppins;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.d4 b{font:700 21px 'Source Sans 3'}.d4.hd4{background:#b5452c}.d4.hd4 em{background:#fff;color:#b5452c}
""")

P["p112_grocery_s5"] = gw(5, """<h1>Grocery wholesaler?<br><span>Let's build your<br>order app.</span></h1><div class=sub>For FMCG and grocery wholesalers who supply kirana shops every day.</div>""",
f'''<div class=c5><div class=sk5>{sacks.format(w=520,h=357)}</div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Shops order from their phone","Credit limit per shop","Loading list per route","Bills and payments in one place"],1))}</div></div>''',
""".c5{flex:1;background:#fffaf0;border-radius:30px;padding:24px;display:flex;flex-direction:column;gap:16px;box-shadow:0 14px 30px rgba(29,43,34,.08)}
.sk5{flex:none;background:#1f4d38;border-radius:22px;display:flex;align-items:center;justify-content:center;padding:6px}.sk5 svg{display:block}
.ls5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.r5{display:flex;align-items:center;gap:16px;background:#efe3cc;border-radius:16px;padding:0 18px}
.r5 em{width:50px;height:50px;border-radius:12px;background:#b5452c;color:#fff;font:800 24px/1 Poppins;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:800 25px/1.3 Poppins}
""", cta="Wholesaler? DM us", ctacss="background:#b5452c;color:#fff")

# ───────── 114 INDIA · Plastic moulding unit · CAROUSEL 5 · TeX Gyre Adventor + Roboto · graphite / hot pink / aqua
# New techniques: SVG injection moulding machine (hopper, barrel, clamp, tie bars), machine tiles with shot counters,
# mould service ring gauges, job card with reject log.
PM = """
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#23262b;color:#f1f3f4}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;letter-spacing:-1px;line-height:1.22} h1 span{color:#ff5c93}
.sub{color:#a7adb5}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Roboto;letter-spacing:3px;color:#8fd6d4}
.kt b{width:44px;height:44px;border-radius:50%;background:#8fd6d4;color:#23262b;font:700 22px/1 'TeX Gyre Adventor';display:flex;align-items:center;justify-content:center}
.cd{background:#2e3238;border-radius:22px;border:1.5px solid #3b4048}
.lb{font:700 13px Roboto;letter-spacing:3px;color:#8d949d}
"""
def pm(n, head, vis, css="", cta="Swipe", ctacss="background:#ff5c93;color:#23262b"):
    return page(PM + css, head, vis, "#f1f3f4", cta, ctacss, tagline=f"{n} / 5")
imm = '''<svg viewBox="0 0 860 330" width="{w}" height="{h}">
<rect x="20" y="250" width="820" height="40" rx="8" fill="#3b4048"/><rect x="40" y="290" width="40" height="30" fill="#2e3238"/><rect x="780" y="290" width="40" height="30" fill="#2e3238"/>
<rect x="60" y="150" width="300" height="100" rx="12" fill="#8fd6d4"/><rect x="80" y="170" width="120" height="16" rx="6" fill="#23262b" opacity=".4"/>
<rect x="360" y="182" width="170" height="36" rx="8" fill="#a7adb5"/><g fill="#ff5c93">''' + "".join(f'<rect x="{370+i*30}" y="178" width="18" height="44" rx="4"/>' for i in range(5)) + '''</g>
<path d="M300 150 L280 40 H400 L380 150 Z" fill="#c9ced4"/><rect x="270" y="30" width="140" height="18" rx="6" fill="#a7adb5"/>
<g fill="#ff5c93">''' + "".join(f'<circle cx="{300+(i%5)*18}" cy="{60+(i//5)*16}" r="6"/>' for i in range(15)) + '''</g>
<rect x="530" y="120" width="40" height="130" rx="6" fill="#e8e9eb"/><rect x="570" y="140" width="30" height="90" rx="4" fill="#ff5c93"/>
<rect x="600" y="140" width="30" height="90" rx="4" fill="#d14778"/><rect x="630" y="120" width="40" height="130" rx="6" fill="#e8e9eb"/>
<rect x="530" y="128" width="290" height="10" rx="5" fill="#8d949d"/><rect x="530" y="232" width="290" height="10" rx="5" fill="#8d949d"/>
<rect x="770" y="110" width="50" height="140" rx="8" fill="#8fd6d4"/><rect x="670" y="170" width="100" height="20" rx="6" fill="#a7adb5"/>
<g transform="translate(110 205)"><rect width="140" height="34" rx="6" fill="#23262b"/><text x="70" y="24" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="18" fill="#8fd6d4">SHOTS 18,240</text></g>
<text x="340" y="22" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="16" fill="#a7adb5">granules</text>
<text x="600" y="110" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="16" fill="#ff5c93">mould</text>
</svg>'''
P["p114_mould_s1"] = pm(1, """<h1>Which mould is on<br>which machine?<br><span>Every job, mould and<br>shot count on one screen.</span></h1>""",
f'''<div class=st1><div class=mc1>{imm.format(w=880,h=338)}</div>
<div class=rw1>{"".join(f'<div class="cd c1"><span class=lb>{a}</span><b>{b}</b></div>' for a,b in [("MACHINE","M-3 · 150 ton"),("MOULD · 8 CAVITY","Cap 28 mm"),("JOB","J-77 · 50,000 pcs")])}</div>
<div class=rw1>{"".join(f'<div class="cd c1 c1b"><span class=lb>{a}</span><b>{b}</b></div>' for a,b in [("SHOTS ON THIS MOULD","18,240 today"),("CYCLE","12 sec"),("NEXT SERVICE","In 18,000 shots")])}</div></div>''',
""".st1{flex:1;display:flex;flex-direction:column;gap:16px}
.mc1{flex:1;background:radial-gradient(circle at 70% 30%,#33373e,#1b1d21 70%);border-radius:28px;display:flex;align-items:center;justify-content:center}.mc1 svg{display:block}
.rw1{flex:none;display:flex;gap:14px}.c1{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.c1 b{font:700 26px/1.3 'TeX Gyre Adventor'}.c1b{background:#ff5c93;border-color:#ff5c93;color:#23262b}.c1b .lb{color:#5b1530}
""")

mach = [("M-1", "Bucket 10 L", "Running", 72, "ru"), ("M-2", "Crate lid", "Running", 45, "ru"), ("M-3", "Cap 28 mm", "Running", 64, "ru"),
        ("M-4", "Mould change", "Back by 2 pm", 0, "ch"), ("M-5", "Container 500 ml", "Running", 18, "ru"), ("M-6", "No job", "Idle", 0, "id")]
P["p114_mould_s2"] = pm(2, """<div class=kt><b>1</b>MACHINES</div><h1 style="margin-top:18px">Six machines.<br><span>One live board.</span></h1>""",
f'''<div class=gd2>{"".join(f'<div class="cd m2 {k}"><div class=t2><b>{a}</b><em>{s}</em></div><span>{b}</span>' + (f'<div class=pr2><u><s style="width:{p}%"></s></u><i>{p}% of job</i></div>' if p else '<div class=pr2><i>&nbsp;</i></div>') + '</div>' for a,b,s,p,k in mach)}</div>
<div class=lg2><span class=lb>SAMPLE</span><span>Shots come from the machine counter. No paper log.</span></div>''',
""".vis{flex-direction:column;gap:14px}
.gd2{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:14px}
.m2{padding:18px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px;border-left:10px solid #8fd6d4}
.m2.ch{border-left-color:#ffb547}.m2.id{border-left-color:#5a616b;opacity:.8}
.t2{display:flex;justify-content:space-between;align-items:center}.t2 b{font:700 38px/1.25 'TeX Gyre Adventor'}
.t2 em{font-style:normal;font:700 16px Roboto;padding:6px 10px;border-radius:8px;background:#1f4e4c;color:#8fd6d4}
.ch .t2 em{background:#4d3a17;color:#ffb547}.id .t2 em{background:#3b4048;color:#a7adb5}
.m2>span{font:500 25px Roboto;color:#d4d8dc}
.pr2{display:flex;align-items:center;gap:10px}.pr2 u{flex:1;display:block;height:12px;border-radius:6px;background:#3b4048;position:relative;overflow:hidden}
.pr2 s{position:absolute;left:0;top:0;bottom:0;background:#ff5c93;border-radius:6px}.pr2 i{font-style:normal;font:600 16px Roboto;color:#a7adb5}
.lg2{flex:none;display:flex;gap:16px;align-items:center;font:500 20px Roboto;color:#d4d8dc;background:#2e3238;border-radius:16px;padding:14px 20px}
""")

moulds = [("Cap 28 mm", "8 cavity", 82, "Service in 18,000 shots", "md"), ("Bucket 10 L", "1 cavity", 40, "Service in 60,000 shots", "ok"),
          ("Crate lid", "2 cavity", 96, "Service due this week", "hi"), ("Container 500 ml", "4 cavity", 25, "Service in 75,000 shots", "ok")]
P["p114_mould_s3"] = pm(3, """<div class=kt><b>2</b>MOULD CARE</div><h1 style="margin-top:18px">Service the mould<br><span>before it breaks.</span></h1>""",
f'''<div class=gd3>{"".join(f'<div class="cd m3 {k}"><div class=rg3 style="background:conic-gradient({"#ff5c93" if k=="hi" else "#ffb547" if k=="md" else "#8fd6d4"} 0 {p}%,#3b4048 {p}% 100%)"><i></i><b>{p}%</b></div><div class=tx3><b>{a}</b><span>{c} · shots used</span><em>{t}</em></div></div>' for a,c,p,t,k in moulds)}</div>
<div class=nt3>Every shot is counted per mould, even when it moves to another machine. Sample numbers.</div>''',
""".vis{flex-direction:column;gap:14px}
.gd3{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px}
.m3{padding:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;text-align:center}
.rg3{width:170px;height:170px;border-radius:50%;position:relative;display:flex;align-items:center;justify-content:center;flex:none}
.rg3 i{position:absolute;inset:18px;border-radius:50%;background:#2e3238}.rg3 b{position:relative;font:700 38px/1.3 'TeX Gyre Adventor'}
.tx3{display:flex;flex-direction:column;align-items:center;gap:4px}.tx3 b{font:700 26px/1.3 'TeX Gyre Adventor'}.tx3 span{font:500 18px Roboto;color:#a7adb5}
.tx3 em{font-style:normal;font:700 17px Roboto;padding:6px 12px;border-radius:8px;background:#1f4e4c;color:#8fd6d4;margin-top:4px}
.md .tx3 em{background:#4d3a17;color:#ffb547}.hi .tx3 em{background:#ff5c93;color:#23262b}
.nt3{flex:none;background:#8fd6d4;color:#23262b;border-radius:18px;padding:16px 22px;font:600 21px/1.4 Roboto}
""")

P["p114_mould_s4"] = pm(4, """<div class=kt><b>3</b>JOB AND DISPATCH</div><h1 style="margin-top:18px">“How many are ready?”<br><span>Answer in one look.</span></h1>""",
f'''<div class=w4><div class="cd jc4"><div class=t4><div><span class=lb>JOB CARD · SAMPLE</span><b>J-77 · Cap 28 mm</b></div><em>On M-3</em></div>
{"".join(f'<div class=r4><span>{a}</span><b>{b}</b></div>' for a,b in [("Party","Sample Packaging Co."),("Order","50,000 pcs · white"),("Made so far","32,000 pcs"),("Rejects logged","420 pcs · short shot"),("Delivery","Sat 28 Nov")])}
<div class=pg4><u><s></s></u><i>64% done</i></div></div>
<div class=bx4><span class=lb>PACKED · SAMPLE</span><div class=bg4>{"".join(f'<i class="{"d" if j<6 else "p" if j<8 else ""}">{"Box " + str(j+1)}</i>' for j in range(10))}</div><b>6 boxes sent · 2 packed · 2 to go</b></div></div>''',
""".w4{flex:1;display:flex;gap:18px}
.jc4{flex:1.2;padding:22px 24px;display:flex;flex-direction:column;gap:4px;border-top:10px solid #ff5c93}
.t4{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:8px}.t4 div{display:flex;flex-direction:column;gap:4px}.t4 b{font:700 30px/1.3 'TeX Gyre Adventor'}
.t4 em{font-style:normal;font:700 16px Roboto;background:#1f4e4c;color:#8fd6d4;padding:6px 10px;border-radius:8px}
.r4{flex:1;display:flex;flex-direction:column;justify-content:center;gap:2px;border-top:1.5px solid #3b4048}.r4 span{font:600 15px Roboto;color:#8d949d}.r4 b{font:700 23px Roboto}
.pg4{display:flex;align-items:center;gap:12px;padding-top:10px}.pg4 u{flex:1;display:block;height:14px;border-radius:7px;background:#3b4048;position:relative;overflow:hidden}
.pg4 s{position:absolute;left:0;top:0;bottom:0;width:64%;background:#ff5c93}.pg4 i{font-style:normal;font:700 18px Roboto}
.bx4{flex:1;background:#8fd6d4;color:#23262b;border-radius:22px;padding:20px;display:flex;flex-direction:column;gap:12px}.bx4 .lb{color:#2f5654}
.bg4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.bg4 i{font-style:normal;border-radius:10px;border:2.5px dashed #2f5654;display:flex;align-items:center;justify-content:center;font:700 17px Roboto;color:#2f5654}
.bg4 i.d{background:#23262b;border:none;color:#8fd6d4}.bg4 i.p{background:#c4eceb;border:2.5px solid #23262b;color:#23262b}
.bx4 b{font:700 20px/1.3 Roboto}
""")

P["p114_mould_s5"] = pm(5, """<h1>Run a plastic<br>moulding unit?<br><span>Let's build your<br>shop-floor app.</span></h1>""",
f'''<div class=c5><div class=mc5>{imm.format(w=560,h=215)}</div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Live machine board","Shot count per mould","Service reminders","Job cards and dispatch"],1))}</div></div>''',
""".c5{flex:1;background:#2e3238;border:1.5px solid #3b4048;border-radius:30px;padding:24px;display:flex;flex-direction:column;gap:16px}
.mc5{flex:none;background:#1b1d21;border-radius:22px;display:flex;justify-content:center;padding:14px}.mc5 svg{display:block}
.ls5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.r5{background:#23262b;border-radius:16px;display:flex;align-items:center;gap:14px;padding:0 18px}
.r5 em{width:48px;height:48px;border-radius:50%;background:#ff5c93;color:#23262b;font:700 22px/1 'TeX Gyre Adventor';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:700 29px/1.3 'TeX Gyre Adventor'}
""", cta="Moulding unit? DM us", ctacss="background:#8fd6d4;color:#23262b")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
