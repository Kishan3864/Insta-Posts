import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 381 INDIA · Combine harvester operator · SINGLE · Anton + Source Sans 3 · paddy gold / harvester red / field green
# New technique: slice treemap of acres per village (column height ∝ village acres, cell height ∝ plot acres) coloured by
# harvest day; the day plan, the capacity bars and the village message are computed from the same plots.
CAP1 = 12
VL1 = [("Village A", [("K-01", 3), ("K-02", 2.5), ("K-03", 4), ("K-04", 1.5)]),
       ("Village B", [("K-05", 5), ("K-06", 2), ("K-07", 3), ("K-08", 2)]),
       ("Village C", [("K-09", 2), ("K-10", 3.5), ("K-11", 1.5), ("K-12", 3), ("K-13", 2)])]
DY1 = ["Mon", "Tue", "Wed"]
ST1 = ["done", "today", "next"]
STL1 = {"done": "Cut Mon", "today": "Today", "next": "Wed"}
def harv1(w=170):
    return f'''<svg viewBox="0 0 170 96" width="{w}" style="display:block"><rect x="40" y="30" width="96" height="40" rx="6" fill="#c8322a"/><rect x="88" y="6" width="38" height="30" rx="5" fill="#c8322a"/><rect x="94" y="11" width="26" height="16" rx="3" fill="#cfe7f2"/>
<rect x="128" y="18" width="30" height="8" rx="3" fill="#8f231d" transform="rotate(-14 128 22)"/><rect x="6" y="52" width="40" height="12" rx="3" fill="#f0b429"/><circle cx="20" cy="46" r="13" fill="none" stroke="#f0b429" stroke-width="4"/>
<line x1="20" y1="33" x2="20" y2="59" stroke="#f0b429" stroke-width="3"/><line x1="7" y1="46" x2="33" y2="46" stroke="#f0b429" stroke-width="3"/>
<circle cx="70" cy="74" r="18" fill="#2a2418"/><circle cx="70" cy="74" r="7" fill="#b8ae98"/><circle cx="124" cy="80" r="12" fill="#2a2418"/><circle cx="124" cy="80" r="5" fill="#b8ae98"/></svg>'''
TOT1 = [sum(a for _, a in p) for _, p in VL1]
P["p381_harvester"] = page("""
body{--f:'Source Sans 3';--h:'Anton';background:#f7f1df;color:#2a2418}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#c8322a;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:70px;line-height:1.25;letter-spacing:.5px;text-transform:uppercase;margin-top:30px} h1 span{color:#c8322a}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp1{flex:1;display:grid;grid-template-columns:1.55fr 1fr;gap:14px;min-height:0}
.tm1{background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(42,36,24,.08);min-height:0}
.sm1{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#7b705a}
.lg1{display:flex;gap:14px}.lg1 span{display:flex;gap:6px;align-items:center;font:600 15px/1.2 'Source Sans 3';color:#5b5240}.lg1 i{width:16px;height:16px;border-radius:4px}
.cl1{flex:1;display:grid;gap:8px;min-height:0}
.vc1{display:flex;flex-direction:column;gap:6px;min-height:0}.vc1 h3{font:400 24px/1.3 Anton;letter-spacing:.5px;text-transform:uppercase}.vc1 h3 span{font:600 15px/1.3 'Source Sans 3';color:#7b705a;text-transform:none;letter-spacing:0;margin-left:6px}
.pc1{flex:1;display:flex;flex-direction:column;gap:5px;min-height:0}
.pc1>div{border-radius:10px;padding:0 10px;display:flex;justify-content:space-between;align-items:center;min-height:0;overflow:hidden}
.pc1 b{font:700 19px/1.2 'Source Sans 3'}.pc1 em{font:600 15px/1.2 'Source Sans 3';font-style:normal}
.pc1 .done{background:repeating-linear-gradient(90deg,#e6dcc0 0 6px,#efe7d0 6px 12px);color:#7b705a}
.pc1 .today{background:#f0b429;color:#2a2418}.pc1 .next{background:#7a9a3a;color:#fff}
.fm1{background:#2a2418;color:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}.fm1 .sm1{color:#d9c79a}
.fd1{flex:1;display:flex;flex-direction:column;justify-content:center;gap:4px;border-top:1px solid rgba(255,255,255,.12)}
.fd1 small{font:600 14px/1.3 'Source Sans 3';color:#c9bd9e}.fd1 b{font:600 22px/1.3 'Source Sans 3'}
.ch1{display:flex;gap:6px;flex-wrap:wrap}.ch1 i{font:600 15px/1.2 'Source Sans 3';font-style:normal;border:1.5px solid #6b604a;border-radius:10px;padding:5px 10px;color:#e6dcc0}.ch1 i.on{background:#f0b429;border-color:#f0b429;color:#2a2418}
.bt1{display:grid;grid-template-columns:1.55fr 1fr;gap:14px}
.dp1{background:#fff;border-radius:26px;padding:14px 18px;display:flex;gap:14px;align-items:center;box-shadow:0 14px 30px rgba(42,36,24,.08)}
.dp1 .bs{flex:1;display:flex;flex-direction:column;gap:8px}.dp1 .r{display:grid;grid-template-columns:54px 1fr 92px;gap:10px;align-items:center}
.dp1 .r b{font:400 20px/1.3 Anton;letter-spacing:.5px}.dp1 .r span{font:600 15px/1.3 'Source Sans 3';color:#5b5240;text-align:right}
.dp1 .tr{height:22px;border-radius:6px;background:#efe7d0;position:relative;overflow:hidden}.dp1 .tr i{position:absolute;left:0;top:0;bottom:0;border-radius:6px}
.ms1{background:#e9f0d8;border-radius:22px 22px 22px 6px;padding:14px 18px;display:flex;flex-direction:column;gap:6px}.ms1 .sm1{color:#4f6a1f}.ms1 p{font:500 18px/1.45 'Source Sans 3';color:#2c3a12;text-wrap:pretty}
""", "<div class=kk>COMBINE HARVESTER OPERATOR · PADDY SEASON</div><h1>Farmers calling all night?<br><span>Book acres by village.</span></h1>",
f'''<div class=vw><div class=tp1><div class=tm1><div style="display:flex;justify-content:space-between;align-items:center"><span class=sm1>BOOKED ACRES · {sum(TOT1):g} ACRES · SAMPLE</span><div class=lg1>{"".join(f'<span><i class={s} style="background:{c}"></i>{t}</span>' for s, c, t in [("d", "#e6dcc0", "Cut"), ("t", "#f0b429", "Today"), ("n", "#7a9a3a", "Next")])}</div></div>
<div class=cl1 style="grid-template-columns:{" ".join(f"{t:g}fr" for t in TOT1)}">{"".join(f'<div class=vc1><h3>{v}<span>{t:g} ac</span></h3><div class=pc1>{"".join(f"<div class={ST1[i]} style={chr(34)}flex:{a:g}{chr(34)}><b>{k}</b><em>{a:g} ac</em></div>" for k, a in pl_)}</div></div>' for i, ((v, pl_), t) in enumerate(zip(VL1, TOT1)))}</div></div>
<div class=fm1><span class=sm1>BOOKING FORM · FARMER</span>
<div class=fd1><small>Village and plot</small><b>Village C · near canal</b></div>
<div class=fd1><small>Acres</small><div class=ch1><i>1</i><i>2</i><i class=on>3.5</i><i>5+</i></div></div>
<div class=fd1><small>Crop ready from</small><b>Wed, 25 Nov</b></div>
<div class=fd1><small>Path for the machine</small><div class=ch1><i class=on>Open</i><i>Narrow</i><i>Wet</i></div></div>
<div class=fd1><small>Field photo</small><b>1 photo added</b></div></div></div>
<div class=bt1><div class=dp1>{harv1(150)}<div class=bs><span class=sm1>DAY PLAN · {CAP1} ACRES A DAY</span>{"".join(f'<div class=r><b>{d}</b><div class=tr><i style="width:{t / CAP1 * 100:.0f}%;background:{c}"></i></div><span>{t:g} of {CAP1} ac</span></div>' for d, t, c in zip(DY1, TOT1, ["#c9bc98", "#f0b429", "#7a9a3a"]))}</div></div>
<div class=ms1><span class=sm1>MESSAGE TO VILLAGE C · 5 FARMERS</span><p>The harvester reaches Village C on Wednesday morning. Keep the path to your field open.</p></div></div></div>''',
"#2a2418", "Run harvesters? DM us", "background:#c8322a;color:#fff")


# ───────── 382 INDIA · Hand block printing unit · SINGLE · Lora + Inter · indigo / madder red / unbleached cotton
# New technique: CSS block-print repeats (layered radial/linear gradients) used for wooden block faces AND for long fabric
# runs on printing tables, printed part patterned vs plain cloth by metres done; stage counts come from the same orders.
PT2 = {"B-14": ("Leaf", "radial-gradient(ellipse 5px 9px at 50% 50%,#23395d 92%,transparent) 0 0/26px 26px,radial-gradient(ellipse 5px 9px at 50% 50%,#23395d 92%,transparent) 13px 13px/26px 26px"),
       "B-07": ("Dot jaal", "radial-gradient(circle,#b23a2b 3.5px,transparent 4px) 0 0/16px 16px,radial-gradient(circle,#b23a2b 2px,transparent 2.5px) 8px 8px/16px 16px"),
       "B-21": ("Flower", "radial-gradient(circle,#d99a2b 3px,transparent 3.5px) 0 0/30px 30px,radial-gradient(circle,#2f6b4f 9px,transparent 9.5px) 0 0/30px 30px,radial-gradient(circle,#b23a2b 2.5px,transparent 3px) 15px 15px/30px 30px"),
       "B-03": ("Stripe", "repeating-linear-gradient(90deg,#d99a2b 0 5px,transparent 5px 16px),repeating-linear-gradient(90deg,transparent 0 9px,#23395d 9px 11px,transparent 11px 16px)")}
OR2 = [("O-31", "Sample Boutique A", "B-14", 40, 40, "Drying", "Saturday"), ("O-32", "Sample Store B", "B-07", 60, 36, "Printing", "Monday"),
       ("O-33", "Sample Label C", "B-21", 25, 10, "Printing", "Tuesday"), ("O-34", "Sample Boutique D", "B-03", 30, 0, "Waiting", "Thursday")]
STG2 = ["Waiting", "Printing", "Drying", "Washing", "Ready"]
TB2 = [o for o in OR2 if o[4] > 0]
P["p382_blockprint"] = page("""
body{--f:'Inter';--h:'Lora';background:#f5efe2;color:#22283a;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#b23a2b;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:66px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#23395d;font-style:italic}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm2{font:700 13px/1.4 Inter;letter-spacing:2px;color:#7c7462}
.bk2{display:grid;grid-template-columns:repeat(4,1fr);gap:12px}
.bk2>div{background:#fff;border-radius:22px;padding:14px;display:flex;gap:12px;align-items:center;box-shadow:0 10px 22px rgba(34,40,58,.07)}
.fc2{width:70px;height:70px;border-radius:8px;flex:none;box-shadow:0 0 0 6px #a5713f,0 0 0 8px #7b5129;background-color:#f5efe2;margin:8px}
.bk2 b{display:block;font:700 22px/1.25 Lora}.bk2 span{font:500 15px/1.3 Inter;color:#6b6352}
.tb2{flex:1;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(34,40,58,.08);min-height:0}
.tr2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:1px solid #efe8d8}
.tr2 .t{display:flex;justify-content:space-between;align-items:baseline;gap:10px}.tr2 .t b{font:700 22px/1.3 Lora}.tr2 .t span{font:500 16px/1.3 Inter;color:#6b6352}
.cl2{height:72px;border-radius:6px;display:flex;overflow:hidden;box-shadow:inset 0 0 0 2px #e3dac6;background:#fbf8f1}
.cl2 .pr{height:100%;background-color:#fbf8f1;border-right:3px dashed #b23a2b}
.cl2 .rw{flex:1;display:flex;align-items:center;justify-content:flex-end;padding-right:14px;font:600 15px/1.2 Inter;color:#a89e88}
.tr2 .m{font:700 17px/1.3 Inter;color:#22283a}
.bt2{display:grid;grid-template-columns:1.25fr 1fr;gap:14px}
.pp2{background:#23395d;color:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}.pp2 .sm2{color:#b7c4dc}
.sg2{display:grid;grid-template-columns:repeat(5,1fr);gap:6px}.sg2>div{background:rgba(255,255,255,.08);border-radius:12px;padding:10px 4px;text-align:center;display:flex;flex-direction:column;gap:4px}
.sg2 b{font:700 30px/1.2 Lora}.sg2 span{font:600 13px/1.25 Inter;color:#cbd5e8}.sg2 .on{background:#b23a2b}.sg2 .z{opacity:.55}
.ms2{background:#fff;border-radius:22px 22px 22px 6px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 10px 22px rgba(34,40,58,.07)}.ms2 .sm2{color:#2f6b4f}.ms2 p{font:500 20px/1.45 Inter;text-wrap:pretty}
""", "<div class=kk>HAND BLOCK PRINTING UNIT · ORDERS BY METRE</div><h1>Whose fabric is on table 2?<br><span>Track each order by block.</span></h1>",
f'''<div class=vw><div class=bk2>{"".join(f'<div><i class=fc2 style="background:{p}"></i><div><b>{c}</b><span>{n}</span></div></div>' for c, (n, p) in PT2.items())}</div>
<div class=tb2><span class=sm2>PRINTING TABLES · TODAY · SAMPLE</span>{"".join(f'<div class=tr2><div class=t><b>Table {i} · {o} · {c}</b><span>{who}</span></div><div class=cl2><i class=pr style="width:{dn / m * 100:.0f}%;background:{PT2[c][1]}"></i>{"<span class=rw>" + f"{m - dn} m to print" + "</span>" if m > dn else ""}</div><span class=m>{dn} of {m} m printed · {st}</span></div>' for i, (o, who, c, m, dn, st, rd) in enumerate(TB2, 1))}</div>
<div class=bt2><div class=pp2><span class=sm2>ORDERS BY STAGE · {len(OR2)} ORDERS · {sum(o[3] for o in OR2)} M</span><div class=sg2>{"".join(f'<div class="{"on" if s == "Printing" else ("" if any(o[5] == s for o in OR2) else "z")}"><b>{sum(1 for o in OR2 if o[5] == s)}</b><span>{s}</span></div>' for s in STG2)}</div></div>
<div class=ms2><span class=sm2>MESSAGE TO {OR2[1][1].upper()}</span><p>{OR2[1][0].replace("-", "&#8209;")} in {PT2[OR2[1][2]][0].lower()}, block&nbsp;{OR2[1][2].replace("-", "&#8209;")}: {OR2[1][4]} of {OR2[1][3]}&nbsp;m printed. Ready on {OR2[1][6]}.</p></div></div></div>''',
"#22283a", "Run a print unit? DM us", "background:#b23a2b;color:#fff")


# ───────── 383 USA · Countertop fabricator (quartz / stone) · CAROUSEL 5 · TeX Gyre Adventor + Roboto · quartz white / graphite / brass
# New technique: SVG top-down L-shaped counter plan with sink/cooktop cutouts and inch dimensions, the same two pieces
# nested to scale on an SVG slab with a remnant, CSS stone swatches (layered vein gradients), install prep checklist.
PC3 = [("A", 96, 25.5), ("B", 72, 25.5)]
SLB3 = (126, 63)
SW3 = [("Sample White Vein", "linear-gradient(115deg,transparent 40%,rgba(120,120,130,.35) 41%,transparent 43%),linear-gradient(160deg,transparent 60%,rgba(140,140,150,.3) 61%,transparent 62.5%),linear-gradient(135deg,#fbfbf9,#ecebe7)"),
       ("Sample Grey Sand", "radial-gradient(circle at 20% 30%,rgba(255,255,255,.5) 1px,transparent 1.5px) 0 0/9px 9px,radial-gradient(circle at 60% 70%,rgba(60,60,60,.25) 1px,transparent 1.5px) 0 0/7px 7px,linear-gradient(135deg,#b9b6af,#a19d95)"),
       ("Sample Black Mist", "linear-gradient(120deg,transparent 45%,rgba(255,255,255,.18) 46%,transparent 47.5%),radial-gradient(circle,rgba(255,255,255,.15) 1px,transparent 1.5px) 0 0/8px 8px,linear-gradient(135deg,#2c2d30,#1b1c1e)")]
def plan3(w=520):
    s = 5
    A, B = PC3
    VW, VH = A[1] * s + 20, B[1] * s + 20
    t = lambda x, y, txt, fs=20, c="#26282c", an="middle", fw=700: f'<text x="{x + 10:g}" y="{y + 10:g}" text-anchor="{an}" font-family="Roboto" font-weight="{fw}" font-size="{fs}" fill="{c}">{txt}</text>'
    return f'''<svg viewBox="0 0 {VW} {VH}" width="{VW}" style="display:block;zoom:{w / VW:.3f}"><g transform="translate(10 10)">
<rect x="0" y="0" width="{A[1] * s}" height="{A[2] * s}" fill="#e9e6df" stroke="#26282c" stroke-width="3"/>
<rect x="{(A[1] - B[2]) * s}" y="{A[2] * s}" width="{B[2] * s}" height="{(B[1] - A[2]) * s}" fill="#e9e6df" stroke="#26282c" stroke-width="3"/>
<line x1="{(A[1] - B[2]) * s}" y1="{A[2] * s}" x2="{A[1] * s}" y2="{A[2] * s}" stroke="#b8873b" stroke-width="3" stroke-dasharray="8 6"/>
<rect x="{42 * s}" y="{6 * s}" width="{26 * s}" height="{16 * s}" rx="14" fill="#fff" stroke="#26282c" stroke-width="2.5"/>
<rect x="{(A[1] - B[2] + 3) * s}" y="{(A[2] + 8) * s}" width="{19 * s}" height="{24 * s}" rx="6" fill="#fff" stroke="#26282c" stroke-width="2.5"/></g>
{t(55 * s, 15 * s + 6, "Sink")}{t((A[1] - B[2] / 2) * s, (A[2] + 21) * s, "Cooktop")}
{t(3 * s, A[2] * s / 2 + 8, f'A · {A[1]}" × {A[2]:g}"', 20, "#8a6427", "start")}
{t((A[1] - B[2] / 2) * s, (B[1] - 6) * s, f'B · {B[1]}"', 21, "#8a6427")}
{t((A[1] - B[2]) * s - 12, (A[2] + 6) * s, "Seam", 19, "#6b6d72", "end", 600)}</svg>'''
def slab3(sw, w=860):
    s = 6.4
    A, B = PC3
    return f'''<div class=sl3 style="width:{SLB3[0] * s:.0f}px;height:{SLB3[1] * s:.0f}px;background:{sw}">
<div class=pz3 style="left:6px;top:6px;width:{A[1] * s - 6:.0f}px;height:{A[2] * s:.0f}px"><b>Piece A · {A[1]}" × {A[2]:g}"</b></div>
<div class=pz3 style="left:6px;top:{(A[2] + 2) * s + 6:.0f}px;width:{B[1] * s - 6:.0f}px;height:{A[2] * s:.0f}px"><b>Piece B · {B[1]}" × {B[2]:g}"</b></div>
<div class=rm3 style="left:{(B[1] + 2) * s + 6:.0f}px;top:{(A[2] + 2) * s + 6:.0f}px;right:6px;bottom:6px"><span>Remnant {SLB3[0] - B[1] - 2}" × {SLB3[1] - A[2] - 2:g}"</span></div></div>'''
B3 = """
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#f6f5f2;color:#26282c}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#8a6427;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;line-height:1.2;letter-spacing:-1px} h1 span{color:#b8873b}
.cd3{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(38,40,44,.08)}
.sm3{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#6b6d72}
.sl3{position:relative;border-radius:6px;box-shadow:inset 0 0 0 2px rgba(0,0,0,.12),0 14px 26px rgba(0,0,0,.12)}
.pz3{position:absolute;border:3px dashed #b8873b;border-radius:4px;display:flex;align-items:center;justify-content:center;background:rgba(255,255,255,.18)}
.pz3 b{font:700 20px/1.2 Roboto;background:#26282c;color:#fff;border-radius:8px;padding:6px 10px}
.rm3{position:absolute;border:2px dotted rgba(0,0,0,.35);border-radius:4px;display:flex;align-items:center;justify-content:center}.rm3 span{font:600 15px/1.3 Roboto;background:rgba(255,255,255,.85);border-radius:6px;padding:4px 8px;text-align:center}
"""
def c3(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#26282c;color:#f1d6a6"):
    return page(B3 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#26282c", cta, ctacss, tagline=f"{n} / 5")
STG3 = [("1", "Template", "Done"), ("2", "Slab picked", "Done"), ("3", "Cutting", "Now"), ("4", "Install", "Thu")]
P["p383_counter_s1"] = c3(1, "COUNTERTOP FABRICATOR · QUARTZ AND STONE", "Countertop jobs lost in texts?<br><span>One page from measure to install.</span>",
f'''<div class=w31><div class="cd3 pl31"><div class=h><span class=sm3>JOB C-208 · KITCHEN · SAMPLE</span><span class=sm3>2 PIECES · 1 SEAM</span></div><div class=pv>{plan3(560)}<div class=sp31>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a, b in [("Customer", "Sample Home"), ("Slab", "S-114 White Vein"), ("Edge", "Eased"), ("Sink", "Undermount"), ("Install", "Thu, 8 to 11 AM")])}</div></div>
<div class=sg31>{"".join(f'<div class="{"on" if st == "Now" else ("dn" if st == "Done" else "")}"><i>{n}</i><b>{a}</b><span>{st}</span></div>' for n, a, st in STG3)}</div></div>
<div class=tx31>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [("“Which slab did we pick?”", "Customer, 3 weeks later"), ("“When do you install?”", "Third text this week"), ("“Is the sink on site?”", "Crew at the door, no sink")])}</div></div>''',
css=""".w31{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.pl31{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px;min-height:0}.pl31 .h{display:flex;justify-content:space-between}.pl31 .pv{flex:1;display:flex;align-items:center;justify-content:space-between;gap:20px;min-height:0}.sp31{width:280px;display:flex;flex-direction:column;gap:12px}.sp31>div{background:#f6f5f2;border-radius:14px;padding:10px 14px}.sp31 small{display:block;font:600 13px/1.3 Roboto;color:#6b6d72}.sp31 b{font:700 20px/1.3 Roboto}
.sg31{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.sg31>div{display:flex;align-items:center;gap:10px;background:#f1efea;border-radius:16px;padding:12px 14px}
.sg31 i{width:34px;height:34px;border-radius:50%;background:#d9d6cf;font:700 17px/34px Roboto;font-style:normal;text-align:center;flex:none}.sg31 b{font:700 17px/1.25 Roboto;flex:1}.sg31 span{font:600 14px/1.2 Roboto;color:#6b6d72}
.sg31 .dn i{background:#26282c;color:#fff}.sg31 .on{background:#26282c;color:#fff}.sg31 .on i{background:#b8873b;color:#fff}.sg31 .on span{color:#f1d6a6}
.tx31{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.tx31>div{background:#e7ecf3;border-radius:20px 20px 20px 6px;padding:16px 18px;display:flex;flex-direction:column;gap:6px}
.tx31 b{font:700 20px/1.3 'TeX Gyre Adventor'}.tx31 span{font:500 16px/1.35 Roboto;color:#55585e}""")
SL3 = [("Mon", ["9 AM", "1 PM"], None), ("Tue", ["10 AM", "3 PM"], "10 AM"), ("Wed", ["9 AM", "11 AM", "2 PM"], None), ("Thu", ["1 PM"], None)]
P["p383_counter_s2"] = c3(2, "1 · TEMPLATE VISIT", "Book the measure online.<br><span>Get the drawing the same day.</span>",
f'''<div class=w32><div class="cd3 bk32"><span class=sm3>PICK A TEMPLATE TIME · SAMPLE</span><div class=dy32>{"".join(f'<div><b>{d}</b>{"".join(f"<i class={chr(34)}{'on' if t == pk else ''}{chr(34)}>{t}</i>" for t in ts)}</div>' for d, ts, pk in SL3)}</div>
<div class=cf32><small>BOOKED</small><b>Tue, 10 AM</b><span>About 45 minutes · we text when on the way</span></div><span class=sm3>BEFORE WE COME</span>{"".join(f'<div class=ck32><i>{ic("check", 18, "#fff", 3)}</i><span>{a}</span></div>' for a in ["Cabinets installed and level", "Sink and cooktop model numbers", "Old top removed, or tell us"])}</div>
<div class="cd3 dr32"><span class=sm3>TEMPLATE DRAWING · JOB C-208</span><div class=pv>{plan3(480)}</div>
<div class=ed32><span class=sm3>EDGE</span><div>{"".join(f'<i class="{"on" if e == "Eased" else ""}">{e}</i>' for e in ["Eased", "Bevel", "Bullnose"])}</div></div>
<div class=ed32><span class=sm3>BACKSPLASH</span><div>{"".join(f'<i class="{"on" if e == "4 in" else ""}">{e}</i>' for e in ["None", "4 in", "Full"])}</div></div></div></div>''',
css=""".w32{flex:1;display:grid;grid-template-columns:1fr 1.15fr;gap:14px;min-height:0}
.bk32{padding:18px 20px;display:flex;flex-direction:column;gap:12px}.dy32{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}
.dy32>div{display:flex;flex-direction:column;gap:8px;background:#f6f5f2;border-radius:14px;padding:10px 8px}.dy32 b{font:700 18px/1.3 'TeX Gyre Adventor';text-align:center}
.dy32 i{font:600 15px/1.2 Roboto;font-style:normal;text-align:center;background:#fff;border:1.5px solid #dedbd3;border-radius:10px;padding:9px 2px}.dy32 i.on{background:#b8873b;border-color:#b8873b;color:#fff}
.ck32{flex:1;display:flex;gap:10px;align-items:center;font:500 19px/1.35 Roboto;border-top:1px solid #eceae4}.cf32{background:#26282c;color:#fff;border-radius:18px;padding:14px 16px;display:flex;flex-direction:column;gap:4px}.cf32 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#c9cbd0}.cf32 b{font:700 30px/1.25 'TeX Gyre Adventor';color:#f1d6a6}.cf32 span{font:500 16px/1.35 Roboto;color:#d6d8dc}.ck32 i{width:28px;height:28px;border-radius:50%;background:#26282c;display:flex;align-items:center;justify-content:center;flex:none}
.dr32{padding:18px 20px;display:flex;flex-direction:column;gap:12px}.dr32 .pv{flex:1;display:flex;align-items:center;justify-content:center;background:#f6f5f2;border-radius:16px}
.ed32{display:flex;justify-content:space-between;align-items:center;gap:10px}.ed32 div{display:flex;gap:6px}.ed32 i{font:600 15px/1.2 Roboto;font-style:normal;border:1.5px solid #dedbd3;border-radius:10px;padding:8px 12px}.ed32 i.on{background:#26282c;border-color:#26282c;color:#fff}""")
P["p383_counter_s3"] = c3(3, "2 · PICK THE SLAB", "See the cuts on the slab.<br><span>Approve it from the couch.</span>",
f'''<div class=w33><div class="cd3 sb33"><div class=h><span class=sm3>SLAB S-114 · {SLB3[0]}" × {SLB3[1]}" · {SW3[0][0].upper()}</span><span class=sm3>TO SCALE · SAMPLE</span></div><div class=pv>{slab3(SW3[0][1])}</div></div>
<div class=bt33><div class="cd3 sw33"><span class=sm3>OTHER SLABS IN THE YARD</span><div>{"".join(f'<div><i style="background:{b}"></i><span>{a}</span></div>' for a, b in SW3)}</div></div>
<div class=ap33><span class=sm3>CUSTOMER APPROVAL</span><p>Layout on slab S-114 with the seam by the cooktop.</p><div class=bn33><i>Approve layout</i><i class=o>Ask a question</i></div></div></div></div>''',
css=""".w33{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sb33{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:12px;min-height:0}.sb33 .h{display:flex;justify-content:space-between}.sb33 .pv{flex:1;display:flex;align-items:center;justify-content:center}
.bt33{display:grid;grid-template-columns:1.25fr 1fr;gap:14px}.sw33{padding:16px 18px;display:flex;flex-direction:column;gap:10px}.sw33>div{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.sw33>div>div{display:flex;flex-direction:column;gap:6px;align-items:center}.sw33 i{width:100%;height:92px;border-radius:10px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}.sw33 span{font:600 14px/1.3 Roboto;text-align:center}
.ap33{background:#26282c;color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}.ap33 .sm3{color:#c9cbd0}.ap33 p{font:500 18px/1.45 Roboto;text-wrap:pretty}
.bn33{margin-top:auto;display:flex;flex-direction:column;gap:8px}.bn33 i{font:700 17px/1.2 Roboto;font-style:normal;text-align:center;background:#b8873b;border-radius:12px;padding:12px}.bn33 i.o{background:transparent;border:1.5px solid #6b6d72}""")
PR3 = [("Sink on site", True), ("Faucet holes marked", True), ("Cabinets cleared", True), ("Old top removed", False), ("Clear path from the driveway", True), ("Water off for 1 hour", True)]
P["p383_counter_s4"] = c3(4, "3 · INSTALL DAY", "No surprises on install day.<br><span>Prep list and a time window.</span>",
f'''<div class=w34><div class="cd3 pr34"><span class=sm3>PREP LIST · JOB C-208 · SAMPLE</span>{"".join(f'<div class="r34 {"no" if not ok else ""}"><i>{ic("check" if ok else "x", 18, "#fff", 3)}</i><span>{a}</span><em>{"Done" if ok else "Still to do"}</em></div>' for a, ok in PR3)}</div>
<div class=rt34><div class=wn34><span class=sm3>INSTALL WINDOW</span><b>Thu · 8 to 11 AM</b><span>Crew of 2 · about 3 hours</span></div>
<div class="cd3 tl34"><span class=sm3>TEXT UPDATES · SAMPLE</span>{"".join(f'<div><b>{t}</b><p>{m}</p></div>' for t, m in [("Mon 5 PM", "Your top is cut. Install is Thu, 8 to 11 AM."), ("Wed 4 PM", "1 item left on your prep list: old top removed."), ("Thu 7:40 AM", "Crew on the way. About 20 minutes.")])}</div></div></div>''',
css=""".w34{flex:1;display:grid;grid-template-columns:1.1fr 1fr;gap:14px;min-height:0}
.pr34{padding:18px 20px;display:flex;flex-direction:column;gap:8px}.r34{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #eceae4}
.r34 i{width:32px;height:32px;border-radius:50%;background:#3f8a5a;display:flex;align-items:center;justify-content:center;flex:none}.r34 span{flex:1;font:500 19px/1.3 Roboto}.r34 em{font:700 14px/1.2 Roboto;font-style:normal;color:#3f8a5a}
.r34.no i{background:#c0442c}.r34.no em{color:#c0442c}.r34.no span{font-weight:700}
.rt34{display:flex;flex-direction:column;gap:14px}.wn34{background:#26282c;color:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:6px}.wn34 .sm3{color:#c9cbd0}
.wn34 b{font:700 34px/1.25 'TeX Gyre Adventor';color:#f1d6a6}.wn34 span{font:500 17px/1.3 Roboto;color:#d6d8dc}
.tl34{flex:1;padding:16px 18px;display:flex;flex-direction:column;gap:10px}.tl34>div{flex:1;display:flex;flex-direction:column;gap:4px;justify-content:center;border-left:3px solid #b8873b;padding-left:12px}
.tl34 b{font:700 16px/1.3 Roboto;color:#8a6427}.tl34 p{font:500 20px/1.4 Roboto;text-wrap:pretty}""")
P["p383_counter_s5"] = c3(5, "YOUR TURN", "Fabricate countertops?<br><span>Let's build your job app.</span>",
f'''<div class=w35><div class="cd3 pv35"><div class=sw35>{"".join(f'<i style="background:{b}"></i>' for a, b in SW3)}</div>{plan3(380)}</div>
<div class=td35>{"".join(f'<div class=ti35><span class=ib>{ic(i, 30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("cal", "Template booking", "Customers pick a time"), ("doc", "Drawing", "Sizes, cutouts, edge"), ("grid", "Slab layout", "Approved before cutting"), ("check", "Install prep", "List, window, texts")])}</div>
<div class=q35>What do your customers text you about most before install day? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b8873b;color:#fff",
css=""".w35{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}
.pv35{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:20px}.sw35{display:flex;gap:10px}.sw35 i{width:110px;height:80px;border-radius:10px;box-shadow:inset 0 0 0 1px rgba(0,0,0,.1)}
.td35{display:flex;flex-direction:column;gap:12px}.ti35{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(38,40,44,.07)}
.ti35 .ib{width:58px;height:58px;border-radius:18px;background:#26282c;color:#f1d6a6}.ti35 b{display:block;font:700 23px/1.3 'TeX Gyre Adventor'}.ti35 div span{font:500 17px/1.4 Roboto;color:#55585e}
.q35{grid-column:1 / 3;background:#26282c;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 Roboto}""")


# ───────── 384 INDIA · Nameplate and acrylic sign maker · SINGLE · Gelasio + Poppins · black acrylic / gold leaf / brushed steel
# New technique: CSS black acrylic plate with gold engraved text, standoff screw caps and a glossy diagonal sheen;
# proof versions in a phone chat reuse the same plate builder at small size; cutting is "locked" until a proof is approved.
def plate4(l1, l2, sc=1.0, big=False, l2fs=19):
    return f'<div class="pl4 {"bg" if big else ""}" style="zoom:{sc}"><i class="sc a"></i><i class="sc b"></i><i class="sc c"></i><i class="sc d"></i><b>{l1}</b><span style="font-size:{l2fs}px">{l2}</span></div>'
JB4 = [("J-51", "Home nameplate", "12 × 6 in · black acrylic, gold", "Approved", "Cutting now"),
       ("J-52", "Office sign", "24 × 8 in · brushed steel", "Proof 1 sent", "Cut locked"),
       ("J-53", "House number", "8 × 8 in · white acrylic", "Changes asked", "Cut locked"),
       ("J-54", "Desk plate", "10 × 3 in · wood finish", "Approved", "Ready 6 PM")]
P["p384_nameplate"] = page("""
body{--f:'Poppins';--h:'Gelasio';background:#f4f2ee;color:#17181b;font-variant-numeric:lining-nums}
.kk{font:600 15px/1.4 Poppins;letter-spacing:3px;color:#9a7a2c;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#9a7a2c;font-style:italic}
.vw{flex:1;display:flex;gap:22px;align-items:stretch;min-height:0}
.lf4{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.hr4{background:linear-gradient(135deg,#e7e4de,#d6d2ca);border-radius:26px;padding:22px;display:flex;flex-direction:column;align-items:center;gap:14px;position:relative}
.hr4 small,.jb4 small{font:700 13px/1.4 Poppins;letter-spacing:2px;color:#6d6a63;align-self:flex-start}
.pl4{width:480px;height:230px;border-radius:12px;background:linear-gradient(120deg,rgba(255,255,255,0) 30%,rgba(255,255,255,.13) 38%,rgba(255,255,255,0) 46%),linear-gradient(#202227,#0e0f12);box-shadow:0 22px 36px rgba(0,0,0,.35),inset 0 0 0 2px #2c2e34;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.pl4 b{font:700 44px/1.2 Gelasio;color:#d8b25a;background:linear-gradient(#f1d68b,#b88a2e);-webkit-background-clip:text;color:transparent}
.pl4 span{font:500 19px/1.3 Poppins;letter-spacing:2px;color:#c9a14a}
.pl4 .sc{position:absolute;width:18px;height:18px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,#b9bcc2 45%,#7c8088);box-shadow:0 2px 3px rgba(0,0,0,.4)}
.pl4 .a{left:14px;top:14px}.pl4 .b{right:14px;top:14px}.pl4 .c{left:14px;bottom:14px}.pl4 .d{right:14px;bottom:14px}
.ok4{position:absolute;right:22px;top:18px;font:700 14px/1.2 Poppins;background:#2f8a57;color:#fff;border-radius:20px;padding:7px 12px}
.jb4{flex:1;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(23,24,27,.08);min-height:0}
.jr4{flex:1;display:grid;grid-template-columns:1fr auto;gap:4px 12px;align-items:center;border-top:1px solid #efece6;padding:6px 0}
.jr4 b{font:600 18px/1.3 Poppins}.jr4 span{font:400 15px/1.35 Poppins;color:#6d6a63}
.jr4 .st{display:flex;flex-direction:column;align-items:flex-end;gap:5px}.jr4 em{font:600 13px/1.2 Poppins;font-style:normal;border-radius:9px;padding:5px 9px;white-space:nowrap}
.jr4 .ap{background:#dff1e6;color:#22704a}.jr4 .wt{background:#f3eee2;color:#7a5f1c}.jr4 .ch{background:#fde4dc;color:#a8361b}
.jr4 .ct{background:#17181b;color:#f1d68b}.jr4 .lk{background:#ecebe8;color:#6d6a63}
.cht{flex:1;display:flex;flex-direction:column;gap:9px;padding:8px 12px 12px;background:#efe9df}
.chh{display:flex;gap:10px;align-items:center;margin:0 -12px;padding:10px 12px;background:#17181b;color:#fff}.chh i{width:34px;height:34px;border-radius:50%;background:#c9a14a;color:#17181b;font:700 15px/34px Poppins;font-style:normal;text-align:center}.chh b{font:600 15px/1.3 Poppins}.chh span{display:block;font:400 12px/1.3 Poppins;color:#bdbab3}
.bu{max-width:88%;border-radius:14px;padding:9px 11px;font:500 14px/1.4 Poppins;box-shadow:0 1px 2px rgba(0,0,0,.08)}
.bu.me{align-self:flex-end;background:#dcf3d0;border-radius:14px 14px 4px 14px}.bu.th{align-self:flex-start;background:#fff;border-radius:14px 14px 14px 4px}
.bu small{display:block;font:700 11px/1.3 Poppins;letter-spacing:1px;color:#6d6a63;margin-bottom:5px}.bu .pw{display:flex;justify-content:center;padding:4px 0 2px}
.tk4{margin-top:auto;display:grid;grid-template-columns:repeat(4,1fr);background:#fff;border-radius:14px;padding:10px 6px}.tk4>div{display:flex;flex-direction:column;align-items:center;gap:5px}.tk4 i{width:16px;height:16px;border-radius:50%;background:#d6d2ca}.tk4 .d i{background:#2f8a57}.tk4 .n i{background:#c9a14a;box-shadow:0 0 0 4px #f1e3bd}.tk4 span{font:600 12px/1.2 Poppins;color:#4a4842}
.bu em{display:block;text-align:right;font:500 10px/1.2 Poppins;font-style:normal;color:#8a877f;margin-top:3px}
""", "<div class=kk>NAMEPLATE AND ACRYLIC SIGN MAKER</div><h1>Spelling wrong after cutting?<br><span>Send a proof first.</span></h1>",
f'''<div class=vw><div class=lf4><div class=hr4><small>J-51 · PROOF 2 · SAMPLE</small><span class=ok4>Approved 4:12 PM</span>{plate4("Sample Family", "FLAT 302 · SAMPLE RESIDENCY", 1, True, 23)}</div>
<div class=jb4><small>TODAY'S JOBS · CUT ONLY AFTER APPROVAL</small>{"".join(f'<div class=jr4><div><b>{j} · {n}</b><br><span>{d}</span></div><div class=st><em class="{"ap" if p == "Approved" else ("ch" if "Changes" in p else "wt")}">{p}</em><em class="{"lk" if "locked" in c else "ct"}">{c}</em></div></div>' for j, n, d, p, c in JB4)}</div></div>
{phone(f"""<div class=cht><div class=chh><i>SS</i><div><b>Sample Signs</b><span>Proofs for J-51</span></div></div>
<div class="bu me"><small>PROOF 1</small><div class=pw>{plate4("Sample Family", "FLAT 302 · SAMPLE RESIDENCY", .5)}</div><em>3:40 PM</em></div>
<div class="bu th">Looks good. Please make the flat number bigger.<em>3:52 PM</em></div>
<div class="bu me"><small>PROOF 2 · FLAT NUMBER BIGGER</small><div class=pw>{plate4("Sample Family", "FLAT 302 · SAMPLE RESIDENCY", .5, False, 23)}</div><em>4:05 PM</em></div>
<div class="bu th">Perfect. Approved.<em>4:12 PM</em></div>
<div class="bu me">Thank you! Cutting now. Ready tomorrow at 11 AM.<em>4:13 PM</em></div><div class=tk4>{"".join(f'<div class="{c}"><i></i><span>{t}</span></div>' for t, c in [("Proof", "d"), ("Approved", "d"), ("Cutting", "n"), ("Ready", "")])}</div></div>""", w=330, h=860)}</div>''',
"#17181b", "Make nameplates? DM us", "background:#17181b;color:#f1d68b")


# ───────── 385 CANADA · Attic insulation contractor · SINGLE · Cardo + Inter · attic pine / insulation cream / frost blue
# New technique: SVG attic cross-sections (rafters, joists, fluffy wavy-top insulation layer drawn to depth) with an
# inch ruler; "now" vs "after" use the same drawing; the quote table's depths and cubic feet are computed from one list.
TGT5 = 14
Q5 = [("Q-61", "Bungalow", 1100, 4, "Tue"), ("Q-62", "2-storey", 900, 6, "Tue"), ("Q-63", "Split-level", 1250, 3, "Wed"), ("Q-64", "Bungalow", 1000, 9, "Thu")]
def attic5(dep, lab, col, cid):
    W, H, base, ppi, ap = 440, 240, 222, 7, 24
    top = base - dep * ppi
    wave = " ".join(f"q 10 -{5 + (i % 2) * 3} 20 0" for i in range(22))
    rx = 236
    ticks = "".join(f'<line x1="{rx}" x2="{rx + (14 if i % 2 == 0 else 8)}" y1="{base - i * ppi}" y2="{base - i * ppi}" stroke="#26313d" stroke-width="2"/>' + (f'<text x="{rx + 20}" y="{base - i * ppi + 5}" font-family="Inter" font-weight="700" font-size="13" fill="#26313d">{i}</text>' if i % 4 == 0 and 0 < i < 16 else "") for i in range(0, 17))
    return f'''<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;height:auto"><defs><clipPath id="{cid}"><polygon points="14,{base} 220,{ap} 426,{base}"/></clipPath></defs>
<polygon points="14,{base} 220,{ap} 426,{base}" fill="#f4ead8"/>
<g clip-path="url(#{cid})"><path d="M0 {base} L0 {top} {wave} L 440 {top} L440 {base} Z" fill="{col}" stroke="#d7c27a" stroke-width="2"/></g>
<polyline points="14,{base} 220,{ap} 426,{base}" fill="none" stroke="#a87a42" stroke-width="10" stroke-linejoin="round"/>
<rect x="10" y="{base}" width="420" height="12" fill="#a87a42"/>{"".join(f'<rect x="{x}" y="{base - 4}" width="8" height="16" fill="#8a6234"/>' for x in range(46, 420, 52))}
<rect x="{rx - 6}" y="{base - 16 * ppi}" width="44" height="{16 * ppi}" rx="3" fill="#ffd34d" stroke="#26313d" stroke-width="2"/>{ticks}
<line x1="{rx - 70}" x2="{rx - 6}" y1="{top}" y2="{top}" stroke="#c0442c" stroke-width="3" stroke-dasharray="6 4"/></svg>'''
P["p385_insulation"] = page("""
body{--f:'Inter';--h:'Cardo';background:#eef3f7;color:#26313d;font-variant-numeric:lining-nums}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#2f6c9a;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:68px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#a87a42}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.sm5{font:700 13px/1.4 Inter;letter-spacing:2px;color:#5e6b78}
.at5{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:14px}
.at5>div{background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(38,49,61,.08)}
.at5 .pv{display:flex;justify-content:center}.at5 svg{zoom:1}
.at5 .t{display:flex;justify-content:space-between;align-items:baseline}.at5 b{font:700 28px/1.2 Cardo}.at5 .t span{font:600 15px/1.3 Inter;color:#5e6b78}
.cp5{font:500 15px/1.35 Inter;color:#5e6b78}.at5 .nw b{color:#c0442c}.at5 .af b{color:#2f8a57}
.bt5{flex:1;display:grid;grid-template-columns:1fr 1.5fr;gap:14px;min-height:0}
.fm5{background:#26313d;color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}.fm5 .sm5{color:#a9bccc}
.fd5{flex:1;display:flex;flex-direction:column;justify-content:center;gap:4px;border-top:1px solid rgba(255,255,255,.12)}.fd5 small{font:600 14px/1.3 Inter;color:#a9bccc}.fd5 b{font:600 19px/1.3 Inter}
.qt5{background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:4px;box-shadow:0 14px 30px rgba(38,49,61,.08)}
.qt5 .r{flex:1;display:grid;grid-template-columns:1.45fr .5fr 1.7fr .55fr;gap:10px;align-items:center;border-top:1px solid #e6edf2}
.qt5 .r.hd{flex:none;border:0;padding-bottom:4px}.qt5 .r.hd span{font:700 12px/1.3 Inter;letter-spacing:1.5px;color:#5e6b78}
.qt5 b{display:block;font:700 17px/1.3 Inter;white-space:nowrap}.qt5 span{font:500 15px/1.35 Inter;color:#5e6b78}
.dp5{display:flex;flex-direction:column;gap:5px}.dp5 .br{height:12px;border-radius:6px;background:#e6edf2;position:relative;overflow:hidden}.dp5 .br i{position:absolute;left:0;top:0;bottom:0;background:#f3d97a}.dp5 .br em{position:absolute;top:0;bottom:0;background:repeating-linear-gradient(-45deg,#2f6c9a 0 4px,#7fb0d6 4px 8px)}
.qt5 .dy{justify-self:end;font:700 15px/1.2 Inter;background:#e3eef7;color:#2f6c9a;border-radius:10px;padding:7px 10px}
""", "<div class=kk>ATTIC INSULATION CONTRACTOR · WINTER QUOTES</div><h1>Cold rooms upstairs?<br><span>Check the attic depth first.</span></h1>",
f'''<div class=vw><div class=at5><div class=nw><div class=t><span class=sm5>CUSTOMER PHOTO · Q-61</span><b>{Q5[0][3]} in now</b></div><div class=cp5>Ruler pushed into the insulation, photo sent with the form</div><div class=pv>{attic5(Q5[0][3], "", "#f3e3a8", "c51")}</div></div>
<div class=af><div class=t><span class=sm5>AFTER THE JOB · SAMPLE</span><b>{TGT5} in</b></div><div class=cp5>Blown-in insulation added to the planned depth</div><div class=pv>{attic5(TGT5, "", "#f6eac0", "c52")}</div></div></div>
<div class=bt5><div class=fm5><span class=sm5>QUOTE REQUEST FORM</span>{"".join(f'<div class=fd5><small>{a}</small><b>{b}</b></div>' for a, b in [("Home and postal code", "Bungalow · A1A 1A1"), ("Attic size", "About 1,100 sq ft"), ("Depth on the ruler", "Photo added · 4 in"), ("Attic hatch", "Bedroom closet"), ("Best day", "Any weekday")])}</div>
<div class=qt5><span class=sm5>QUOTES THIS WEEK · FILL TO {TGT5} IN · SAMPLE</span><div class="r hd"><span>HOME</span><span>NOW</span><span>TO ADD</span><span style="justify-self:end">DAY</span></div>
{"".join(f'<div class=r><div><b>{q} · {h}</b><span>{a:,} sq ft</span></div><b>{d} in</b><div class=dp5><div class=br><i style="width:{d / TGT5 * 100:.0f}%"></i><em style="left:{d / TGT5 * 100:.0f}%;right:0"></em></div><span>Add {TGT5 - d}&nbsp;in · about {a * (TGT5 - d) / 12:,.0f}&nbsp;cu&nbsp;ft</span></div><span class=dy>{dy}</span></div>' for q, h, a, d, dy in Q5)}</div></div></div>''',
"#26313d", "Insulate attics? DM us", "background:#a87a42;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
