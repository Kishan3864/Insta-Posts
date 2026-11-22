import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 301 INDIA · E-rickshaw fleet owner · SINGLE · Montserrat + Roboto · asphalt / electric lime / white
# New technique: SVG battery packs with charge fill by %, colour by level and a bolt when charging, keyed to rickshaw numbers.
def batt(pct, chg, w=170):
    col = "#9be22d" if pct >= 80 else ("#f2c230" if pct >= 40 else "#ef5b45")
    fh = round(196 * pct / 100)
    bolt = '<path d="M92 92 L68 140 H86 L78 182 L110 124 H90 Z" fill="#1c2127" opacity=".85"/>' if chg else ""
    return f'''<svg viewBox="0 0 170 250" width="{w}" class=bt1><rect x="55" y="6" width="60" height="22" rx="6" fill="#59616b"/>
<rect x="10" y="26" width="150" height="218" rx="18" fill="#2b323a" stroke="#59616b" stroke-width="4"/>
<rect x="21" y="{37+196-fh}" width="128" height="{fh}" rx="10" fill="{col}"/>{bolt}</svg>'''
fleet = [("ER-01", 100, False, "Ready now"), ("ER-02", 85, True, "Full by 2:10 PM"), ("ER-03", 0, False, "Out on road"), ("ER-04", 55, True, "Full by 3:30 PM"),
         ("ER-05", 95, True, "Full by 1:40 PM"), ("ER-06", 30, True, "Full by 5 PM"), ("ER-07", 0, False, "Out on road"), ("ER-08", 100, False, "Ready now")]
def bcell(code, pct, chg, note):
    out = pct == 0
    return f'''<div class="bc{' ou' if out else ''}"><div class=bh><b>{code}</b><em>{'ON ROAD' if out else f'{pct}%'}</em></div>
<div class=bw>{batt(pct if not out else 0, chg, 118) if not out else '<div class=rd>' + ic('truck', 54) + '</div>'}</div><span>{note}</span></div>'''
shifts = [("ER-03", "Morning", "6 AM – 2 PM", "Paid"), ("ER-07", "Morning", "6 AM – 2 PM", "Due"), ("ER-05", "Evening", "2 PM – 10 PM", "Next")]
P["p301_erick"] = page("""
body{--f:'Roboto';--h:'Montserrat';background:#eef1ea;color:#1c2127}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#5a8a12;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:66px;letter-spacing:-1.8px;line-height:1.2} h1 span{color:#5a8a12}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sh1{flex:1;min-height:0;background:#1c2127;border-radius:28px;padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.sh1>small{font:700 14px/1.4 Roboto;letter-spacing:2px;color:#b6f05a}
.gr1{flex:1;min-height:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:1fr 1fr;gap:12px}
.bc{background:#252c34;border-radius:18px;padding:12px;display:flex;flex-direction:column;align-items:center;gap:6px}
.bh{width:100%;display:flex;justify-content:space-between;align-items:center}.bh b{font:800 22px/1.3 Montserrat;color:#fff}.bh em{font:700 17px/1.3 Roboto;font-style:normal;color:#b6f05a}
.bc.ou .bh em{color:#9aa3ad}
.bw{flex:1;min-height:0;display:flex;align-items:center;justify-content:center}.bt1{display:block;max-height:100%}
.rd{width:118px;height:150px;border-radius:18px;border:3px dashed #59616b;display:flex;align-items:center;justify-content:center;color:#9aa3ad}
.bc>span{font:500 16px/1.4 Roboto;color:#d4dae0}
.bt2{display:grid;grid-template-columns:1.25fr 1fr;gap:12px}
.dl{background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 12px 26px rgba(28,33,39,.07)}
.dl small,.ms1 small{display:block;font:700 13px/1.4 Roboto;letter-spacing:2px;color:#6b7480;margin-bottom:4px}
.dr{display:grid;grid-template-columns:80px 1fr 70px;gap:8px;align-items:center;padding:8px 0;border-top:1px solid #e8ebe4}
.dr b{font:800 19px Montserrat}.dr span{font:500 17px/1.35 Roboto;color:#444c55}.dr em{font:700 15px Roboto;font-style:normal;text-align:center;padding:4px 0;border-radius:8px}
.ms1{background:#5a8a12;color:#fff;border-radius:22px;padding:14px 20px;display:flex;flex-direction:column;justify-content:center}.ms1 small{color:#e3f7c4}
.ms1 p{font:500 20px/1.45 Roboto;background:rgba(255,255,255,.14);border-radius:14px 14px 14px 4px;padding:12px 14px}.ms1 b{color:#e9ffbf}
""", "<div class=kk>E-RICKSHAW FLEET · CHARGING SHED</div><h1>Which battery is full?<br><span>See all 8 at a glance.</span></h1>",
f'''<div class=vw><div class=sh1><small>CHARGING SHED · TODAY 1:15 PM · SAMPLE</small><div class=gr1>{"".join(bcell(*f) for f in fleet)}</div></div>
<div class=bt2><div class=dl><small>DRIVER SHIFTS · DAILY RENT · SAMPLE</small>{"".join(f'<div class=dr><b>{c}</b><span>{s} · {t}</span><em style="background:{dict(Paid="#e1f5c4",Due="#fde2dc",Next="#eceff3")[r]};color:{dict(Paid="#3f6a0a",Due="#b23a26",Next="#555")[r]}">{r}</em></div>' for c,s,t,r in shifts)}</div>
<div class=ms1><small>MESSAGE TO EVENING DRIVER</small><p><b>ER-05</b> will be full by 1:40 PM. Pick it up at the shed for your 2 PM shift.</p></div></div></div>''',
"#1c2127", "Run e-rickshaws? DM us", "background:#1c2127;color:#b6f05a")

# ───────── 302 INDIA · Handloom weaving cluster · CAROUSEL 5 · Lora + Open Sans · turmeric / kora cotton / peacock teal
# New technique: SVG handloom front view (warp threads, woven part with border motif, shuttle) reused as a progress meter per loom.
HL = """
body{--f:'Open Sans';--h:'Lora';background:#f6f0e1;color:#173f45}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#b5770c;margin-top:22px;align-self:flex-start}
h1{font-family:'Lora';font-weight:700;font-size:64px;line-height:1.25;letter-spacing:-.5px} h1 span{color:#0f7a7a}
.cd{background:#fffdf7;border-radius:24px;box-shadow:0 12px 28px rgba(23,63,69,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#7c7462}
.nb{display:flex;align-items:center;gap:14px;background:#173f45;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.45 'Open Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e3a21a;color:#173f45}.nb b{color:#f3c75a}
.sw{display:inline-block;width:30px;height:30px;border-radius:8px;flex:none;box-shadow:inset 0 0 0 2px rgba(0,0,0,.12)}
"""
def hl(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#173f45;color:#fff"):
    return page(HL + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#173f45", cta, ctacss, tagline=f"{n} / 5")
def loom(done, total=6.3, body="#e3a21a", border="#0f7a7a", w=420, h=520, label=True):
    # woven part grows from the bottom; warp threads above it
    top, bot = 70, 440
    wy = bot - (bot - top) * done / total
    warp = "".join(f'<line x1="{x}" y1="{top}" x2="{x}" y2="{wy:.0f}" stroke="#d9cfb8" stroke-width="2"/>' for x in range(78, 345, 9))
    motif = "".join(f'<path d="M{x} {wy+14:.0f} l9 -9 l9 9 l-9 9 z" fill="#f6f0e1"/>' for x in range(84, 330, 26))
    return f'''<svg viewBox="0 0 420 520" width="{w}" class=lm>
<rect x="30" y="30" width="360" height="30" rx="8" fill="#7a4e22"/><rect x="30" y="448" width="360" height="30" rx="8" fill="#7a4e22"/>
<rect x="30" y="30" width="22" height="470" rx="6" fill="#5e3a17"/><rect x="368" y="30" width="22" height="470" rx="6" fill="#5e3a17"/>
<rect x="70" y="{top}" width="280" height="{bot-top}" fill="#fbf7ec"/>{warp}
<rect x="70" y="{wy:.0f}" width="280" height="{bot-wy:.0f}" fill="{body}"/>
<rect x="70" y="{wy:.0f}" width="280" height="36" fill="{border}"/>{motif}
<rect x="70" y="{bot-28}" width="280" height="28" fill="{border}"/>
<rect x="58" y="{wy-26:.0f}" width="304" height="14" rx="7" fill="#8b5a2b"/>
<path d="M150 {wy-50:.0f} h120 l18 9 l-18 9 h-120 l-18 -9 z" fill="#c98a3a" stroke="#5e3a17" stroke-width="3"/></svg>'''

P["p302_loom_s1"] = hl(1, "HANDLOOM WEAVING · YOUR WEAVERS AT HOME", "Yarn with 6 weavers?<br><span>Know where each saree is.</span>",
f'''<div class=w1><div class="cd lc1">{loom(4.1, body="#b8322a", border="#0f7a7a", w=440)}<div class=lt1><small class=cap>LOOM L-03 · SAMPLE</small><b>4.1 m</b><span>of a 6.3 m saree woven</span>
<div class=pr1><i style="width:{4.1/6.3*100:.0f}%"></i></div><span class=dt1>Ready about Fri 27 Nov</span></div></div>
<div class=bb1><span class=vn>{ic("chat",24)} You, every week</span><p>“How much yarn did I give loom 4? Was it 2 kg or 3? And when is the teal one ready?”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.lc1{flex:1;min-height:0;display:flex;align-items:center;gap:26px;padding:20px 30px}
.lm{display:block;max-height:100%;flex:none}.lt1{flex:1;display:flex;flex-direction:column;gap:8px}.lt1 b{font:700 92px/1.3 Lora;color:#b5770c}.lt1>span{font:600 22px/1.4 'Open Sans'}
.pr1{height:22px;border-radius:11px;background:#ece3cc;overflow:hidden;margin:8px 0}.pr1 i{display:block;height:100%;background:#0f7a7a}.lt1 .dt1{font:600 19px 'Open Sans';color:#6c6656}
.bb1{background:#173f45;color:#fff;border-radius:22px 22px 22px 6px;padding:18px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px 'Open Sans';color:#f3c75a;margin-bottom:6px}.bb1 p{font:500 22px/1.45 'Open Sans'}""")

yarn = [("L-01", "#e3a21a", "Turmeric", 3.0, "Mon 9 Nov"), ("L-02", "#0f7a7a", "Peacock teal", 2.0, "Tue 10 Nov"), ("L-03", "#b8322a", "Madder red", 2.5, "Wed 11 Nov"),
        ("L-04", "#e3a21a", "Turmeric", 2.0, "Fri 13 Nov"), ("L-05", "#2f4a8a", "Indigo", 3.0, "Mon 16 Nov"), ("L-06", "#0f7a7a", "Peacock teal", 1.5, "Wed 18 Nov")]
ytot = sum(y[3] for y in yarn)
P["p302_loom_s2"] = hl(2, "STEP 1 · EVERY KG OF YARN, WRITTEN ONCE", "Yarn given?<br><span>One tap, with the date.</span>",
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>LOOM</span><span>YARN · SAMPLE</span><span>GIVEN</span><span>DATE</span></div>
{"".join(f'<div class=rw2><b>{l}</b><span class=yc><i class=sw style="background:{c}"></i>{n}</span><em>{k:g} kg</em><span class=dd>{d}</span></div>' for l,c,n,k,d in yarn)}
<div class="rw2 tt2"><b>Total</b><span></span><em>{ytot:g} kg</em><span class=dd>6 looms</span></div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>The weaver gets a message with the kg and colour, <b>so nobody has to remember.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:14px 26px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:.8fr 1.6fr .8fr 1fr;gap:12px;align-items:center;border-bottom:1px solid #eee5cf}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #173f45;font:700 14px/1.4 'Open Sans';letter-spacing:1.5px;color:#7c7462}
.rw2 b{font:700 26px/1.4 Lora}.yc{display:flex;align-items:center;gap:12px;font:600 21px 'Open Sans'}.rw2 em{font:700 30px/1.4 Lora;font-style:normal;color:#b5770c}.dd{font:500 18px 'Open Sans';color:#5b6366}
.tt2{border:0;background:#f7e7bf;border-radius:14px;padding:0 12px}""")

prog = [("L-01", 6.3, "#e3a21a", "Ready · collect"), ("L-02", 5.2, "#0f7a7a", "Wed 25 Nov"), ("L-03", 4.1, "#b8322a", "Fri 27 Nov"), ("L-04", 2.6, "#e3a21a", "Tue 1 Dec"),
        ("L-05", 1.4, "#2f4a8a", "Fri 4 Dec"), ("L-06", 0.5, "#0f7a7a", "Tue 8 Dec")]
P["p302_loom_s3"] = hl(3, "STEP 2 · WEAVERS SEND METRES, NOT EXCUSES", "6 looms.<br><span>Every saree in metres.</span>",
f'''<div class=w3><div class="cd lp3">{"".join(f'<div class=lr3><b>{l}</b><div class=fb3><i style="width:{m/6.3*100:.1f}%;background:repeating-linear-gradient(90deg,{c} 0 14px,rgba(255,255,255,.18) 14px 16px),{c};box-shadow:inset 0 -12px 0 #173f45"></i></div><div class=mm3><em>{m:g} m</em><span>{d}</span></div></div>' for l,m,c,d in prog)}
<div class=ax3><span style="left:0">0 m</span><span style="left:{3/6.3*100:.1f}%;transform:translateX(-50%)">3 m</span><span style="right:0">6.3 m · one saree</span></div></div>
<div class=nb><span class=ib>{ic("chat",26)}</span><span>Each evening the weaver taps the metres done. <b>Ready dates update by themselves.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.lp3{flex:1;padding:18px 26px;display:flex;flex-direction:column;gap:4px}
.lr3{flex:1;display:grid;grid-template-columns:80px 1fr 190px;gap:16px;align-items:center}.lr3 b{font:700 26px/1.4 Lora}
.fb3{height:60px;border-radius:10px;background:repeating-linear-gradient(90deg,#efe6cf 0 2px,#fbf7ec 2px 9px);overflow:hidden;box-shadow:inset 0 0 0 2px #e3d8bd}.fb3 i{display:block;height:100%}
.mm3 em{display:block;font:700 30px/1.35 Lora;font-style:normal;color:#173f45}.mm3 span{font:600 17px/1.4 'Open Sans';color:#6c6656}
.ax3{position:relative;height:24px;margin:6px 206px 0 96px;font:600 15px/1.4 'Open Sans';color:#7c7462}.ax3 span{position:absolute;top:0;white-space:nowrap}""")

# sample rule: 1 saree uses 0.5 kg yarn
recv = [("L-01", 3.0, 2, "#e3a21a"), ("L-02", 2.0, 1, "#0f7a7a"), ("L-04", 2.0, 1, "#e3a21a")]
P["p302_loom_s4"] = hl(4, "STEP 3 · SAREES IN, YARN BALANCE OUT", "Sarees back?<br><span>Yarn left is worked out.</span>",
f'''<div class=w4>{"".join(f'<div class="cd yb4"><div class=yh4><b>{l}</b><i class=sw style="background:{c}"></i></div><div class=sr4>{"".join(f"<span class=sa style=background:{c}></span>" for _ in range(s))}</div>{"".join(f"<div class=yl4><span>{a}</span><b>{v}</b></div>" for a,v in [("Yarn given",f"{g:g} kg"),("Sarees back so far",s),("Yarn used",f"{s*0.5:g} kg"),("Still with weaver",f"{g-s*0.5:g} kg")])}</div>' for l,g,s,c in recv)}
<div class=nb><span class=ib>{ic("chart",26)}</span><span>Sample rule: 1 saree uses 0.5 kg yarn. <b>Change it to your own design.</b></span></div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr auto;gap:12px;min-height:0}.w4 .nb{grid-column:1 / 4}
.yb4{padding:18px;display:flex;flex-direction:column;gap:6px}.yh4{display:flex;justify-content:space-between;align-items:center}.yh4 b{font:700 32px/1.4 Lora}
.sr4{display:flex;flex-wrap:wrap;gap:12px;padding:12px 0 16px;border-bottom:2px dashed #e3d8bd;justify-content:center}
.sa{width:70px;height:92px;border-radius:8px;box-shadow:inset 0 -9px 0 #173f45,inset 0 9px 0 rgba(255,255,255,.35)}
.yl4{flex:1;display:flex;flex-direction:column;justify-content:center}.yl4 span{font:600 16px/1.5 'Open Sans';color:#7c7462;margin-bottom:4px}.yl4 b{font:700 38px/1.4 Lora;color:#173f45}
.yl4:last-child b{color:#b8322a}""")

P["p302_loom_s5"] = hl(5, "YOUR TURN", "Give yarn to weavers?<br><span>Let's build your loom book.</span>",
f'''<div class=w5><div class="cd hp5">{"".join(f'<div class=lm5>{loom(d, body=b, border=r, w=270)}<b>{d:g} m</b></div>' for d,b,r in [(5.2,"#0f7a7a","#e3a21a"),(4.1,"#b8322a","#0f7a7a"),(2.6,"#e3a21a","#2f4a8a")])}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Yarn book","Kg and colour per loom"),("chart","Metres woven","Ready dates"),("box","Sarees back","Yarn balance"),("chat","Messages","To each weaver")])}</div>
<div class=q>How do you keep track of yarn today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b5770c;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;display:flex;justify-content:space-around;align-items:center;padding:10px 14px}.hp5 .lm{max-height:none}
.lm5{display:flex;flex-direction:column;align-items:center;gap:4px}.lm5 b{font:700 30px/1.4 Lora;color:#b5770c}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fffdf7;border-radius:22px;padding:18px 22px;box-shadow:0 10px 22px rgba(23,63,69,.07)}
.ti .ib{width:70px;height:70px;border-radius:20px;background:#f7e7bf;color:#b5770c}.ti b{display:block;font:700 26px/1.4 Lora}.ti div span{font:500 18px/1.35 'Open Sans';color:#5b6366}
.q{background:#173f45;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Open Sans'}""")

# ───────── 303 USA · Meal prep company · SINGLE · Archivo Black + DM Sans · basil / tomato / oat cream
# New technique: top-down CSS meal containers (3 compartments with drawn food blobs) as the cook count, derived from the order page.
foods = {"rice": "radial-gradient(circle at 30% 30%,#fff 0 3px,transparent 4px) 0 0/12px 12px,#f1ead6",
         "green": "radial-gradient(circle at 40% 40%,#5f9a3a 0 6px,transparent 7px) 0 0/18px 18px,#3f7a2a",
         "red": "radial-gradient(circle at 50% 50%,#e36b4a 0 7px,transparent 8px) 0 0/20px 20px,#c0452e",
         "brown": "radial-gradient(circle at 50% 50%,#b07a44 0 8px,transparent 9px) 0 0/22px 22px,#8a5a2e",
         "yellow": "radial-gradient(circle at 50% 50%,#f3c64a 0 6px,transparent 7px) 0 0/16px 16px,#e0a92a"}
def tray(a, b, c, w=200):
    return f'''<div class=try style="width:{w}px"><i class=c1 style="background:{foods[a]}"></i><i class=c2 style="background:{foods[b]}"></i><i class=c3 style="background:{foods[c]}"></i></div>'''
menu = [("Lemon chicken + rice", ("rice", "yellow", "green"), 46), ("Beef chili bowl", ("red", "brown", "rice"), 38), ("Veggie pasta", ("yellow", "green", "red"), 29), ("Turkey meatballs", ("brown", "green", "rice"), 33)]
mtot = sum(m[2] for m in menu)
P["p303_mealprep"] = page("""
body{--f:'DM Sans';--h:'Archivo Black';background:#f4eedf;color:#22301f}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#c0452e;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.25;margin-top:30px} h1 span{color:#3f7a2a}
.vw{flex:1;display:grid;grid-template-columns:430px 1fr;gap:14px;min-height:0}
.of{display:flex;flex-direction:column;padding:16px 20px;gap:8px;flex:1}
.of small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7a7462}.of h3{font:400 24px/1.35 'Archivo Black'}
.mi{display:flex;align-items:center;justify-content:space-between;padding:13px 0;border-top:1px solid #eee7d6;font:600 18px/1.35 'DM Sans'}
.qt{display:flex;align-items:center;gap:8px}.qt i{width:30px;height:30px;border-radius:9px;background:#efe8d6;display:flex;align-items:center;justify-content:center;font:700 18px 'DM Sans';font-style:normal}.qt b{font:700 19px 'DM Sans';width:20px;text-align:center}
.fd{display:flex;justify-content:space-between;background:#f6f2e7;border-radius:12px;padding:10px 12px;font:500 16px 'DM Sans'}.fd b{font-weight:700}
.ct{margin-top:auto;background:#c0452e;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 19px 'DM Sans'}
.rt{display:flex;flex-direction:column;gap:12px;min-height:0}
.ck{flex:1;min-height:0;background:#22301f;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.ck>small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#cfe4b8}
.kr{flex:1;display:flex;align-items:center;gap:16px;background:#2d3d29;border-radius:18px;padding:8px 16px}
.try{flex:none;aspect-ratio:1.45;border-radius:16px;background:#fff;padding:8px;display:grid;grid-template-columns:1.3fr 1fr;grid-template-rows:1fr 1fr;gap:6px;box-shadow:0 6px 0 #d9d2bf}
.try i{border-radius:9px}.try .c1{grid-row:1 / 3}
.kn{flex:1}.kn b{display:block;font:400 21px/1.35 'Archivo Black';color:#fff}.kn span{font:500 15px 'DM Sans';color:#b9c9ad}
.kr em{font:400 40px/1.3 'Archivo Black';font-style:normal;color:#f3c64a}
.zn{background:#fff;border-radius:22px;padding:14px 18px;box-shadow:0 12px 26px rgba(34,48,31,.07)}
.zn small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#7a7462;margin-bottom:6px}
.zr{display:flex;justify-content:space-between;align-items:center;padding:6px 0;border-top:1px solid #eee7d6;font:500 17px/1.35 'DM Sans'}.zr b{font:700 18px 'DM Sans';color:#3f7a2a}
""", "<div class=kk>MEAL PREP COMPANY · WEEKLY ORDERS</div><h1>Orders in 40 texts?<br><span>Close them on one page.</span></h1>",
f'''<div class=vw>{browser(f"""<div class=of><small>ORDER PAGE · SAMPLE</small><h3>Week of Mon 7 Dec</h3>
{"".join(f'<div class=mi><span>{n}</span><span class=qt><i>−</i><b>{q}</b><i>+</i></span></div>' for n,q in [("Lemon chicken + rice",2),("Beef chili bowl",1),("Veggie pasta",0),("Turkey meatballs",2)])}
<div class=fd><span>Delivery</span><b>Sun 6 Dec · 8 AM – 12 PM</b></div><div class=fd><span>ZIP code</span><b>12345</b></div><div class=fd><span>Orders close</span><b>Thu 3 Dec · 8 PM</b></div><div class=fd><span>Drop-off note</span><b>Leave at side door</b></div><div class=fd><span>Repeat next week</span><b>Yes, same meals</b></div><div class=fd><span>Name</span><b>Sample customer</b></div><div class=fd><span>Meals this week</span><b>5</b></div>
<div class=ct>Place my order · 5 meals</div></div>""", url="yourmealprep.com/order", style="display:flex;flex-direction:column")}
<div class=rt><div class=ck><small>KITCHEN COOK LIST · AFTER THE CUTOFF · SAMPLE</small>{"".join(f'<div class=kr>{tray(*t, w=118)}<div class=kn><b>{n}</b><span>From all orders</span></div><em>{q}</em></div>' for n,t,q in menu)}
<div class=kr style="background:#3f7a2a;flex:none;padding:10px 16px"><div class=kn><b>Total meals to cook</b></div><em>{mtot}</em></div></div>
<div class=zn><small>SUNDAY DELIVERY ROUTE · BY ZIP · SAMPLE</small>{"".join(f'<div class=zr><span>{a}</span><b>{b}</b></div>' for a,b in [("Zone A · 8 AM – 10 AM","14 bags"),("Zone B · 10 AM – 12 PM","11 bags")])}</div></div></div>''',
"#22301f", "Run a meal prep business? DM us", "background:#3f7a2a;color:#fff")

# ───────── 304 INDIA · Mess (meals for working people) · SINGLE · Crimson Text + Fira Sans · manila / brick red / ink blue
# New technique: a manila punch card drawn in CSS — punched holes show the dark board behind, struck holes = skip told in time.
taken = set(); skipped = set()
random.seed(304)
for d in range(1, 23):
    for m in ("L", "D"):
        (skipped if (d, m) in {(3, "D"), (7, "L"), (8, "L"), (14, "D"), (15, "D"), (19, "L")} else taken).add((d, m))
cells = []
for d in range(1, 31):
    hs = ""
    for m in ("L", "D"):
        k = "hp" if (d, m) in taken else ("hs" if (d, m) in skipped else "ho")
        hs += f'<i class="{k}"></i>'
    cells.append(f'<div class="dy{" td" if d == 22 else ""}"><span>{d}</span><div class=hh>{hs}</div></div>')
nt, ns = len(taken), len(skipped); left = 60 - nt - ns
lunch_members, lunch_skips = 42, 5
P["p304_mess"] = page("""
body{--f:'Fira Sans';--h:'Crimson Text';background:#2a3550;color:#fff}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#f0b8a2;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;line-height:1.2;margin-bottom:4px} h1 span{color:#f3d9a4}
.vw{flex:1;display:grid;grid-template-columns:1fr 330px;gap:14px;min-height:0}
.pc{background:#e9d3a0;color:#2a3550;border-radius:14px;padding:18px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 18px 40px rgba(0,0,0,.3);
 background-image:linear-gradient(90deg,transparent 0 96%,rgba(160,60,40,.25) 96% 100%)}
.ph{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2px solid #b0452f;padding-bottom:8px}
.ph div small{display:block;font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#8a6a3a;margin-bottom:2px}.ph div b{font:700 32px/1.3 'Crimson Text'}
.ph em{font:700 15px 'Fira Sans';font-style:normal;color:#b0452f;text-align:right}
.gd{flex:1;min-height:0;display:grid;grid-template-columns:repeat(6,1fr);grid-template-rows:repeat(5,1fr);gap:6px}
.dy{border:1.5px dashed #c4a46a;border-radius:10px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}
.dy span{font:600 14px/1.3 'Fira Sans';color:#7a5a2a}.dy.td{border:2.5px solid #b0452f;background:#f2e0b4}
.hh{display:flex;gap:8px}.hh i{width:26px;height:26px;border-radius:50%;display:block;position:relative}
.hp{background:#2a3550;box-shadow:inset 0 3px 4px rgba(0,0,0,.6)}
.hs{border:2.5px solid #b0452f;background:linear-gradient(45deg,transparent 44%,#b0452f 44% 56%,transparent 56%)}
.ho{border:2px solid #c4a46a}
.lgd4{display:flex;gap:18px;font:600 15px 'Fira Sans'}.lgd4 span{display:flex;align-items:center;gap:6px}.lgd4 i{width:18px;height:18px;border-radius:50%;display:block}
.sd{display:flex;flex-direction:column;gap:12px;min-height:0}
.ct4{background:#fff;color:#2a3550;border-radius:20px;padding:14px 18px;display:flex;flex-direction:column;gap:4px}
.ct4 small{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#7c7f8f}
.cr{display:flex;align-items:center;justify-content:space-between;padding:4px 0}.cr span{font:500 18px/1.35 'Fira Sans'}.cr b{font:700 38px/1.3 'Crimson Text'}
.cr.hl4{background:#f6e6c4;border-radius:12px;padding:6px 12px;margin-top:4px}.cr.hl4 b{color:#b0452f}
.sk4{flex:1;background:#b0452f;border-radius:20px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;gap:12px}.sk4 em{font:600 16px/1.4 'Fira Sans';font-style:normal;color:#ffd9cc}
.sk4 small{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#ffd9cc}.sk4 p{font:500 19px/1.45 'Fira Sans'}
.sk4 .bn{background:#fff;color:#b0452f;border-radius:12px;padding:12px;text-align:center;font:700 19px 'Fira Sans'}
""", "<div class=kk>MESS · MONTHLY MEAL CARDS</div><h1>Paper coupons lost again?<br><span>One card counts every meal.</span></h1>",
f'''<div class=vw><div class=pc><div class=ph><div><small>MEMBER M-12 · NOVEMBER · SAMPLE</small><b>Lunch + dinner plan</b></div><em>Each day: left hole lunch,<br>right hole dinner</em></div>
<div class=gd>{"".join(cells)}</div>
<div class=lgd4><span><i style="background:#2a3550"></i>Eaten {nt}</span><span><i style="border:2.5px solid #b0452f"></i>Skip told {ns}</span><span><i style="border:2px solid #a8884e"></i>Left {left}</span></div></div>
<div class=sd><div class=ct4><small>TODAY'S LUNCH · SUN 22 NOV</small><div class=cr><span>Members</span><b>{lunch_members}</b></div><div class=cr><span>Skips told by 10 AM</span><b>{lunch_skips}</b></div><div class="cr hl4"><span>Cook for</span><b>{lunch_members-lunch_skips}</b></div></div>
<div class=ct4><small>TONIGHT'S DINNER · SKIPS UNTIL 4 PM</small><div class=cr><span>Members</span><b>{lunch_members}</b></div><div class=cr><span>Skips told so far</span><b>3</b></div></div><div class=sk4><small>MEMBER APP · SAMPLE</small><p>Not coming for dinner? Tap before 4 PM. The meal stays on your card.</p><div class=bn>Skip tonight's dinner</div><em>Card M-12: {left} meals left, renew by Mon 30 Nov.</em></div></div></div>''',
"#fff", "Run a mess? DM us", "background:#f3d9a4;color:#2a3550", logo_color="#ffffff")

# ───────── 305 CANADA · Boat winter storage · SINGLE · Bitter + Inter · shrink-wrap white / marine navy / buoy orange · PHONE
# New technique: top-down storage yard of SVG hulls under shrink-wrap (highlight streaks), status by outline colour, numbered spots.
def hull(x, y, L, W, st, n):
    col = {"w": "#e9eef3", "p": "#ffffff", "s": "#ffffff"}[st]
    ol = {"w": "#16324f", "p": "#f26b21", "s": "#2c9a6a"}[st]
    dash = ' stroke-dasharray="10 7"' if st == "p" else ""
    path = f"M{x} {y+W/2} Q{x+L*0.18} {y} {x+L*0.55} {y} L{x+L} {y+W*0.18} L{x+L} {y+W*0.82} L{x+L*0.55} {y+W} Q{x+L*0.18} {y+W} {x} {y+W/2} Z"
    streak = f'<path d="M{x+L*0.2} {y+W*0.3} L{x+L*0.85} {y+W*0.3}" stroke="#ffffff" stroke-width="6" stroke-linecap="round" opacity=".9"/><path d="M{x+L*0.3} {y+W*0.62} L{x+L*0.8} {y+W*0.62}" stroke="#c9d4de" stroke-width="4" stroke-linecap="round"/>' if st != "p" else ""
    return f'<path d="{path}" fill="{col}" stroke="{ol}" stroke-width="5"{dash}/>{streak}<rect x="{x+L+10}" y="{y+W/2-17}" width="62" height="34" rx="8" fill="{ol}"/><text x="{x+L+41}" y="{y+W/2+7}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="19" fill="#fff">{n}</text>'
spots = [("w", "B-01"), ("w", "B-02"), ("s", "B-03"), ("w", "B-04"), ("p", "B-05"), ("w", "B-06"), ("s", "B-07"), ("w", "B-08"), ("p", "B-09"), ("w", "B-10")]
yard = '<svg viewBox="0 0 520 900" class=yd><rect width="520" height="900" rx="24" fill="#c9cfc6"/>' + \
       '<rect x="238" y="0" width="44" height="900" fill="#b4bbb1"/>' + "".join(f'<rect x="256" y="{y}" width="8" height="30" fill="#e8ece6"/>' for y in range(20, 900, 60))
for i, (st, n) in enumerate(spots):
    col, row = i % 2, i // 2
    x = 12 if col == 0 else 290
    yard += hull(x, 30 + row * 172, 152, 96, st, n)
yard += "</svg>"
nW = sum(1 for s in spots if s[0] == "w"); nS = sum(1 for s in spots if s[0] == "s"); nP = sum(1 for s in spots if s[0] == "p")
ph5 = phone(f'''<div class=ap><div class=ah><small>SAMPLE MARINA</small><b>Book spring launch</b><span>Boat B-07 · Spot 7, row 4</span></div>
<div class=fl5><small>PICK A LAUNCH WEEK</small><div class=ch5>{"".join(f'<span class="{"on" if a=="Sat 8 May" else ""}">{a}</span>' for a in ["Sat 24 Apr","Sat 1 May","Sat 8 May","Sat 15 May"])}</div></div>
<div class=fl5><small>BEFORE LAUNCH</small>{"".join(f'<div class=ck5><i class="{"y" if y else ""}">{ic("check",16) if y else ""}</i>{a}</div>' for a,y in [("Remove shrink-wrap",True),("Wash and wax",True),("Battery check",False)])}</div>
<div class=fl5><small>LAUNCH TIME</small><div class=ch5>{"".join(f'<span class="{"on" if a=="9 AM" else ""}">{a}</span>' for a in ["9 AM","11 AM","1 PM","3 PM"])}</div></div><div class=fl5><small>WE TEXT YOU</small><div class=tx5>The day before launch</div></div><div class=fl5><small>NOTE FOR THE YARD</small><div class=tx5>Trailer pickup right after launch</div></div>
<div class=bk5>Book Sat 8 May</div></div>''', 360, 830)
P["p305_boat"] = page("""
body{--f:'Inter';--h:'Bitter';background:#eaf0f5;color:#16324f}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#d85a14;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:64px;letter-spacing:-1px;line-height:1.22} h1 span{color:#d85a14}
.vw{flex:1;display:flex;gap:16px;min-height:0;align-items:stretch}
.yc{flex:1;min-width:0;background:#fff;border-radius:26px;padding:14px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(22,50,79,.08)}
.yc>small{font:700 13px/1.4 'Inter';letter-spacing:2px;color:#6a7a8a;padding:2px 6px 0}
.yd{flex:1;min-height:0;width:100%;display:block}
.lgd5{display:grid;grid-template-columns:1fr;gap:6px;padding:0 6px 4px}.lgd5 span{display:flex;align-items:center;gap:10px;font:600 16px/1.3 'Inter'}.lgd5 i{width:26px;height:16px;border-radius:8px;display:block}
.ap{display:flex;flex-direction:column;gap:12px;padding:8px 18px 18px;flex:1;min-height:0}
.ah small{display:block;font:700 11px/1.4 Inter;letter-spacing:2px;color:#6a7a8a}.ah b{display:block;font:800 24px/1.3 Bitter}.ah span{font:500 14px/1.4 Inter;color:#4a5a6a}
.fl5{background:#f1f5f9;border-radius:14px;padding:10px 12px}.fl5 small{display:block;font:700 11px/1.4 Inter;letter-spacing:1.5px;color:#6a7a8a;margin-bottom:6px}
.ch5{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ch5 span{background:#fff;border-radius:10px;padding:8px 4px;text-align:center;font:600 14px Inter;border:1.5px solid #d5dde5}.ch5 .on{background:#16324f;color:#fff;border-color:#16324f}
.ck5{display:flex;align-items:center;gap:10px;font:600 15px/1.3 Inter;padding:4px 0}.ck5 i{width:22px;height:22px;border-radius:6px;border:2px solid #9aa8b6;display:flex;align-items:center;justify-content:center;color:#fff}.ck5 i.y{background:#2c9a6a;border-color:#2c9a6a}
.tx5{font:600 15px Inter}
.bk5{margin-top:auto;background:#f26b21;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 17px Inter}
""", "<div class=kk>BOAT WINTER STORAGE · MARINA</div><h1>Boats wrapped for winter.<br><span>Spring launch, booked now.</span></h1>",
f'''<div class=vw><div class=yc><small>STORAGE YARD · ROW BY ROW · SAMPLE</small>{yard}
<div class=lgd5><span><i style="background:#16324f"></i>Wrapped, stored · {nW}</span><span><i style="background:#2c9a6a"></i>Launch booked · {nS}</span><span><i style="background:#f26b21"></i>Wrap this week · {nP}</span></div></div>
{ph5}</div>''',
"#16324f", "Run a marina? DM us", "background:#16324f;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
