import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 121 INDIA · Dyeing and printing mill · CAROUSEL 5 · Crimson Text + Fira Sans · dye vat teal / magenta / greige
# New techniques: lab-dip approval card with stapled swatches, process stepper per lot, dye recipe card with % bars, stage lanes with lot chips.
DY = """
body{--f:'Fira Sans';--h:'Crimson Text';background:#e9e4d8;color:#13363a}
h1{font-family:'Crimson Text';font-weight:700;font-size:66px;letter-spacing:-.3px;line-height:1.2} h1 span{color:#c2185b}
.sub{color:#5b6461}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Fira Sans';letter-spacing:3px;color:#0f5c63}
.kt b{width:44px;height:44px;border-radius:50%;background:#0f5c63;color:#e9e4d8;font:700 24px/1 'Crimson Text';display:flex;align-items:center;justify-content:center}
.cd{background:#fffdf7;border-radius:22px;box-shadow:0 14px 30px rgba(19,54,58,.08)}
.lb{font:700 13px 'Fira Sans';letter-spacing:3px;color:#8b918c}
"""
def dy(n, head, vis, css="", cta="Swipe", ctacss="background:#0f5c63;color:#e9e4d8"):
    return page(DY + css, head, vis, "#13363a", cta, ctacss, tagline=f"{n} / 5")
dips = [("A", "#b5265f", "Too dark", ""), ("B", "#d0457a", "Approved", "ok"), ("C", "#e06b98", "Too light", "")]
P["p121_dye_s1"] = dy(1, """<h1>Party says the shade<br>doesn't match?<br><span>Keep every lab dip<br>and recipe on record.</span></h1>""",
f'''<div class=w1><div class=pn1><div class=lc1><div class=hd1><span class=lb>LAB DIP CARD · SAMPLE</span><b>Lot L-562 · Shade “Rani pink”</b><i>Party: Sample Fabrics · 3,000 m cotton</i></div>
<div class=dp1>{"".join(f'<div class="dd1 {k}"><i class=st1></i><div class=sw1 style="background:{c}"></div><b>Dip {a}</b><span>{t}</span></div>' for a,c,t,k in dips)}</div>
<div class=sg1>Approved by party on Sat 21 Nov · photo saved</div></div></div>
<div class=sd1>{"".join(f'<div class="cd s1"><b>{a}</b><span>{b}</span></div>' for a,b in [("Lab dips","With photos and party's yes"),("Recipe saved","Same shade next time"),("Lot tracking","From greige to folding")])}</div></div>''',
""".w1{flex:1;display:flex;gap:18px}
.pn1{flex:1;background:#0f5c63;border-radius:30px;display:flex;align-items:center;justify-content:center;padding:24px}
.lc1{width:100%;height:100%;background:#fffdf7;border-radius:12px;padding:22px;display:flex;flex-direction:column;gap:16px;box-shadow:0 20px 40px rgba(0,0,0,.25)}
.hd1{display:flex;flex-direction:column;gap:4px}.hd1 b{font:700 32px/1.2 'Crimson Text'}.hd1 i{font:500 18px 'Fira Sans';font-style:normal;color:#5b6461}
.dp1{flex:1;display:flex;gap:14px}
.dd1{flex:1;display:flex;flex-direction:column;gap:6px;align-items:center;position:relative}
.st1{position:absolute;top:-6px;width:40px;height:10px;border-radius:2px;background:linear-gradient(#c9ced3,#8c949c);z-index:2}
.sw1{flex:1;width:100%;border-radius:4px;clip-path:polygon(0 0,100% 0,100% 92%,92% 100%,84% 92%,76% 100%,68% 92%,60% 100%,52% 92%,44% 100%,36% 92%,28% 100%,20% 92%,12% 100%,4% 92%,0 100%)}
.dd1 b{font:700 24px 'Crimson Text'}.dd1 span{font:700 16px 'Fira Sans';color:#8b918c;padding:4px 10px;border-radius:8px;background:#efe9dc}
.dd1.ok span{background:#0f5c63;color:#fff}
.sg1{background:#fbe1ea;color:#8e1043;border-radius:12px;padding:12px 16px;font:600 18px 'Fira Sans'}
.sd1{width:290px;flex:none;display:flex;flex-direction:column;gap:14px}
.s1{flex:1;padding:20px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-left:10px solid #c2185b}
.s1 b{font:700 30px/1.2 'Crimson Text'}.s1 span{font:500 19px/1.35 'Fira Sans';color:#5b6461}
""")

steps = [("Greige in", 1), ("Scouring", 1), ("Dyeing", 1), ("Washing", 2), ("Finishing", 0), ("Folding", 0)]
P["p121_dye_s2"] = dy(2, """<div class=kt><b>1</b>JOB CARD</div><h1 style="margin-top:18px">Every lot, and the stage<br><span>it is at right now.</span></h1>""",
f'''<div class="cd jc2"><div class=t2><div><span class=lb>JOB CARD · SAMPLE</span><b>Lot L-562</b></div><em>Washing now</em></div>
<div class=g2>{"".join(f'<div class=f2><span>{a}</span><b>{b}</b></div>' for a,b in [("Party","Sample Fabrics"),("Greige","3,000 m cotton"),("Shade","Rani pink · dip B"),("Machine","Jet 2"),("Promised","Thu 26 Nov"),("Pieces","30 × 100 m")])}</div>
<div class=sp2>{"".join(f'<div class="p2 {"dn" if d==1 else "nw" if d==2 else ""}"><i>{"✓" if d==1 else i+1}</i><span>{t}</span></div>' for i,(t,d) in enumerate(steps))}</div></div>''',
""".vis{flex-direction:column}
.jc2{flex:1;padding:24px 26px;display:flex;flex-direction:column;gap:16px;border-top:12px solid #c2185b}
.t2{display:flex;justify-content:space-between;align-items:center}.t2 div{display:flex;flex-direction:column;gap:4px}.t2 b{font:700 44px/1.2 'Crimson Text'}
.t2 em{font-style:normal;font:700 18px 'Fira Sans';background:#c2185b;color:#fff;padding:10px 16px;border-radius:12px}
.g2{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:12px}
.f2{background:#f4efe3;border-radius:14px;padding:0 18px;display:flex;flex-direction:column;justify-content:center;gap:4px}.f2 span{font:600 18px 'Fira Sans';color:#8b918c}.f2 b{font:700 31px 'Fira Sans'}
.sp2{flex:none;display:flex;gap:8px}
.p2{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;padding:14px 4px;border-radius:14px;background:#f4efe3}
.p2 i{width:44px;height:44px;border-radius:50%;background:#fff;border:3px solid #cfc8b8;font:700 20px/1 'Fira Sans';font-style:normal;display:flex;align-items:center;justify-content:center}
.p2 span{font:700 16px 'Fira Sans'}
.p2.dn i{background:#0f5c63;border-color:#0f5c63;color:#fff}.p2.nw{background:#c2185b;color:#fff}.p2.nw i{border-color:#fff;color:#c2185b}
""")

rec = [("Reactive red", "#c2185b", 2.4), ("Reactive blue", "#3949ab", 0.3), ("Reactive yellow", "#f2b705", 0.15), ("Salt", "#b0b7bb", 60), ("Soda ash", "#d7dbde", 20)]
P["p121_dye_s3"] = dy(3, """<div class=kt><b>2</b>RECIPE</div><h1 style="margin-top:18px">Repeat order?<br><span>Use the same recipe.</span></h1>""",
f'''<div class=w3><div class="cd rc3"><div class=t3><div><span class=lb>SHADE RECIPE · SAMPLE</span><b>Rani pink · dip B</b></div><i class=sw3></i></div>
{"".join(f'<div class=r3><i style="background:{c}"></i><b>{a}</b><em>{v}{" %" if v<10 else " g/L"}</em></div>' for a,c,v in rec)}</div>
<div class=sd3>{"".join(f'<div class="cd s3"><span class=lb>{a}</span><b>{b}</b></div>' for a,b in [("MACHINE","Jet 2"),("TEMPERATURE","60 °C"),("TIME","60 min"),("LAST USED","Lot L-498, Oct")])}</div></div>''',
""".w3{flex:1;display:flex;gap:18px}
.rc3{flex:1.4;padding:24px;display:flex;flex-direction:column;gap:6px}
.t3{display:flex;justify-content:space-between;align-items:center;padding-bottom:8px}.t3 div{display:flex;flex-direction:column;gap:4px}.t3 b{font:700 38px/1.2 'Crimson Text'}
.sw3{width:90px;height:90px;border-radius:50%;background:#d0457a;box-shadow:inset 0 0 0 8px rgba(255,255,255,.4);display:block}
.r3{flex:1;display:flex;align-items:center;gap:16px;border-top:1.5px solid #ece5d6}
.r3 i{width:40px;height:40px;border-radius:50%;flex:none;display:block}.r3 b{flex:1;font:600 25px 'Fira Sans'}.r3 em{font-style:normal;font:700 26px 'Fira Sans';color:#0f5c63}
.sd3{flex:1;display:flex;flex-direction:column;gap:12px}
.s3{flex:1;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px;background:#0f5c63;color:#fff}.s3 .lb{color:#9cc8cb}.s3 b{font:700 30px/1.2 'Crimson Text'}
""")

lanes = [("Greige in", [("L-571", "2,000 m")]), ("Dyeing", [("L-565", "1,800 m"), ("L-568", "2,400 m")]), ("Washing", [("L-562", "3,000 m")]),
         ("Finishing", [("L-559", "1,500 m"), ("L-560", "2,200 m")]), ("Ready", [("L-555", "2,600 m"), ("L-557", "900 m")])]
P["p121_dye_s4"] = dy(4, """<div class=kt><b>3</b>LOT BOARD</div><h1 style="margin-top:18px">“When will my lot<br>be ready?”<br><span>One board answers it.</span></h1>""",
f'''<div class=bd4>{"".join(f'<div class="cd ln4"><div class=hd4><b>{t}</b><em>{len(ls)}</em></div>' + "".join(f'<div class="lt4 {"me" if a=="L-562" else ""}"><b>{a}</b><span>{m}</span></div>' for a,m in ls) + '</div>' for t,ls in lanes)}</div>''',
""".vis{flex-direction:column}
.bd4{flex:1;display:flex;flex-direction:column;gap:10px}
.ln4{flex:1;display:flex;gap:12px;padding:10px 12px;align-items:stretch}
.hd4{width:200px;flex:none;display:flex;justify-content:space-between;align-items:center;padding:0 10px}.hd4 b{font:700 28px/1.2 'Crimson Text'}
.hd4 em{font-style:normal;font:700 15px 'Fira Sans';background:#efe9dc;border-radius:8px;padding:3px 9px}
.lt4{flex:1;max-width:330px;background:#f4efe3;border-radius:12px;padding:0 18px;display:flex;justify-content:space-between;align-items:center;border-left:6px solid #0f5c63}
.lt4 b{font:700 23px 'Fira Sans'}.lt4 span{font:500 19px 'Fira Sans';color:#5b6461}
.lt4.me{background:#c2185b;color:#fff;border-left-color:#8e1043}.lt4.me span{color:#fbd6e3}
""")

P["p121_dye_s5"] = dy(5, """<h1>Run a dyeing or<br>printing mill?<br><span>Let's build your<br>lot and shade app.</span></h1>""",
f'''<div class=c5><div class=dp5>{"".join(f'<i style="background:{c}"></i>' for c in ["#b5265f","#d0457a","#e06b98","#e9e4d8","#3949ab","#f2b705"])}</div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Lab dips with approval","Job card per lot","Shade recipes saved","Lot board for parties"],1))}</div></div>''',
""".c5{flex:1;background:#0f5c63;color:#fff;border-radius:30px;padding:26px;display:flex;gap:24px}
.dp5{width:220px;flex:none;display:grid;grid-template-columns:1fr 1fr;gap:10px}.dp5 i{border-radius:10px;display:block;box-shadow:inset 0 0 0 6px rgba(255,255,255,.2)}
.ls5{flex:1;display:flex;flex-direction:column}
.r5{flex:1;display:flex;align-items:center;gap:16px;border-top:2px solid rgba(255,255,255,.15)}.r5:first-child{border-top:none}
.r5 em{width:52px;height:52px;border-radius:50%;background:#c2185b;font:700 26px/1 'Crimson Text';font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:700 32px/1.2 'Crimson Text'}
""", cta="Dyeing mill? DM us", ctacss="background:#c2185b;color:#fff")

# ───────── 124 INDIA · Readymade garment shop · CAROUSEL 5 · Cardo + Fira Sans · denim / coral / khaki
# New techniques: style × size stock heatmap, billing screen that cuts stock, reorder list to supplier, catalogue with size chips.
RG = """
body{--f:'Fira Sans';--h:'Cardo';background:#e6dcc6;color:#1f3049}
h1{font-family:'Cardo';font-weight:700;font-size:64px;letter-spacing:-.3px;line-height:1.2} h1 span{color:#d9533f}
.sub{color:#5f5a4e}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Fira Sans';letter-spacing:3px;color:#2d4a6b}
.kt b{width:44px;height:44px;border-radius:12px;background:#2d4a6b;color:#e6dcc6;font:700 24px/1 Cardo;display:flex;align-items:center;justify-content:center}
.cd{background:#fffaf0;border-radius:22px;box-shadow:0 14px 30px rgba(31,48,73,.08)}
.lb{font:700 13px 'Fira Sans';letter-spacing:3px;color:#8c8676}
"""
def rg(n, head, vis, css="", cta="Swipe", ctacss="background:#2d4a6b;color:#e6dcc6"):
    return page(RG + css, head, vis, "#1f3049", cta, ctacss, tagline=f"{n} / 5")
sizes = ["S", "M", "L", "XL", "XXL"]
grid = [("Kurta set", [4, 0, 6, 3, 1]), ("Denim shirt", [2, 5, 7, 2, 0]), ("Polo tee", [8, 12, 9, 4, 2]), ("Chinos", [1, 3, 0, 2, 1]), ("Hoodie", [3, 6, 5, 0, 2]), ("Track pants", [5, 9, 7, 3, 1])]
def heat(v):
    return ("#d9533f", "#fff") if v == 0 else ("#f3c9a8", "#1f3049") if v <= 2 else ("#a9c0db", "#1f3049") if v <= 5 else ("#2d4a6b", "#fff")
def hm(css_cls="hm"):
    return (f'<div class={css_cls}><div class=hr><span></span>' + "".join(f'<b>{s}</b>' for s in sizes) + '</div>'
            + "".join(f'<div class=hr><span>{n}</span>' + "".join(f'<i style="background:{heat(v)[0]};color:{heat(v)[1]}">{v}</i>' for v in vs) + '</div>' for n, vs in grid) + '</div>')
HMCSS = """.hm{flex:1;display:flex;flex-direction:column;gap:8px;padding:18px 20px}
.hr{flex:1;display:grid;grid-template-columns:190px repeat(5,1fr);gap:8px;align-items:stretch}
.hr:first-child{flex:none}.hr b{font:700 20px 'Fira Sans';text-align:center;color:#5f5a4e}
.hr span{font:700 22px 'Fira Sans';display:flex;align-items:center}
.hr i{font-style:normal;border-radius:10px;font:700 26px 'Fira Sans';display:flex;align-items:center;justify-content:center}
"""
P["p124_garment_s1"] = rg(1, """<h1>“Size M in this one?”<br><span>See stock by style<br>and size at a glance.</span></h1>""",
f'''<div class=cd style="flex:1;display:flex;flex-direction:column">{hm()}</div>
<div class=lg1>{"".join(f'<span><i style="background:{c}"></i>{t}</span>' for c,t in [("#d9533f","Sold out"),("#f3c9a8","1 to 2 left"),("#a9c0db","3 to 5"),("#2d4a6b","6 or more")])}<span class=lb>SAMPLE STOCK</span></div>''',
HMCSS + """.vis{flex-direction:column;gap:14px}
.lg1{flex:none;display:flex;gap:18px;align-items:center;font:600 18px 'Fira Sans'}.lg1 span{display:flex;align-items:center;gap:8px}.lg1 .lb{margin-left:auto}
.lg1 i{width:20px;height:20px;border-radius:6px;display:block}
""")

bill = [("Polo tee", "Navy · M", "1"), ("Denim shirt", "Light wash · L", "1"), ("Track pants", "Black · M", "2")]
P["p124_garment_s2"] = rg(2, """<div class=kt><b>1</b>BILLING</div><h1 style="margin-top:18px">Every bill<br><span>cuts the stock for you.</span></h1>""",
f'''<div class=w2>{browser(f"""<div class=bl2><div class=t2><b>Bill 3108</b><span class=lb>COUNTER 1 · SAMPLE</span></div>
<div class=sc2>{ic("search",22)}<span>Scan tag or type style</span></div>
{"".join(f'<div class=r2><div><b>{a}</b><span>{b}</span></div><em>× {q}</em></div>' for a,b,q in bill)}
<div class=pay2><i>UPI</i><i class=on>Cash</i><i>Card</i></div><div class=bt2>Save bill · stock updated</div></div>""", "billing.yourshop.in · sample", "flex:1.3")}
<div class=sd2><span class=lb>STOCK AFTER THIS BILL</span>{"".join(f'<div class="cd s2"><b>{a}</b><div><s>{b}</s><em>{c}</em></div></div>' for a,b,c in [("Polo tee · M","12","11 left"),("Denim shirt · L","7","6 left"),("Track pants · M","9","7 left")])}</div></div>''',
""".w2{flex:1;display:flex;gap:18px}
.bl2{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:12px;background:#fffdf8}
.t2{display:flex;justify-content:space-between;align-items:center}.t2 b{font:700 34px/1.2 Cardo}
.sc2{display:flex;align-items:center;gap:10px;border:2px dashed #cfc5ad;border-radius:12px;padding:12px 16px;font:500 18px 'Fira Sans';color:#8c8676}
.r2{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid #efe7d6}
.r2 div{display:flex;flex-direction:column;gap:2px}.r2 b{font:700 26px 'Fira Sans'}.r2 span{font:500 20px 'Fira Sans';color:#7a7466}.r2 em{font-style:normal;font:700 24px 'Fira Sans'}
.pay2{display:flex;gap:8px}.pay2 i{flex:1;font-style:normal;text-align:center;font:700 18px 'Fira Sans';padding:11px 0;border-radius:12px;background:#f1ebde}.pay2 i.on{background:#2d4a6b;color:#fff}
.bt2{background:#d9533f;color:#fff;border-radius:14px;text-align:center;font:700 20px 'Fira Sans';padding:14px}
.sd2{flex:1;display:flex;flex-direction:column;gap:12px}
.s2{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:8px}.s2 b{font:700 27px/1.2 Cardo}
.s2 div{display:flex;align-items:center;gap:12px}.s2 s{font:600 22px 'Fira Sans';color:#a39c8b}.s2 em{font-style:normal;font:700 22px 'Fira Sans';background:#2d4a6b;color:#fff;padding:5px 12px;border-radius:8px}
""")

reo = [("Kurta set", "M", "Sold out", "6"), ("Chinos", "L", "Sold out", "4"), ("Hoodie", "XL", "Sold out", "4"), ("Denim shirt", "XXL", "Sold out", "2"), ("Kurta set", "XXL", "1 left", "3"), ("Chinos", "S", "1 left", "3")]
P["p124_garment_s3"] = rg(3, """<div class=kt><b>2</b>REORDER</div><h1 style="margin-top:18px">Know what to reorder<br><span>before the weekend rush.</span></h1>""",
f'''<div class="cd ro3"><div class=t3><div><span class=lb>REORDER LIST · SAMPLE</span><b>For Sample Supplier</b></div><em>6 lines</em></div>
<div class="r3 hd3"><span>Style</span><span>Size</span><span>Now</span><span>Order</span></div>
{"".join(f'<div class=r3><b>{a}</b><i>{s}</i><span class="{"so" if n=="Sold out" else "lw"}">{n}</span><em>{q} pcs</em></div>' for a,s,n,q in reo)}
<div class=bt3>Send list to supplier on WhatsApp</div></div>''',
""".vis{flex-direction:column}
.ro3{flex:1;padding:22px 26px;display:flex;flex-direction:column}
.t3{display:flex;justify-content:space-between;align-items:flex-start;padding-bottom:12px}.t3 div{display:flex;flex-direction:column;gap:4px}.t3 b{font:700 34px/1.2 Cardo}
.t3 em{font-style:normal;font:700 16px 'Fira Sans';background:#e6dcc6;padding:6px 12px;border-radius:8px}
.r3{flex:1;display:grid;grid-template-columns:1.6fr .7fr 1fr .9fr;align-items:center;border-top:1.5px solid #efe7d6}
.r3.hd3{flex:none;padding-bottom:8px;border-top:none;font:700 15px 'Fira Sans';color:#8c8676;letter-spacing:1px}
.r3 b{font:700 25px 'Fira Sans'}.r3 i{font-style:normal;font:700 22px 'Fira Sans';background:#e6dcc6;border-radius:8px;padding:6px 0;width:70px;text-align:center}
.r3 span.so{font:700 20px 'Fira Sans';color:#d9533f}.r3 span.lw{font:700 20px 'Fira Sans';color:#b8762b}.r3 em{font-style:normal;font:700 24px 'Fira Sans';color:#2d4a6b}
.bt3{background:#2d4a6b;color:#fff;border-radius:14px;text-align:center;font:700 21px 'Fira Sans';padding:16px;margin-top:10px}
""")

cat = [("Polo tee", "Navy", ["S", "M", "L", "XL", "XXL"], [8, 11, 9, 4, 2], "#2d4a6b"), ("Kurta set", "Mustard", ["S", "M", "L", "XL", "XXL"], [4, 0, 6, 3, 1], "#d9a13b"),
       ("Hoodie", "Grey", ["S", "M", "L", "XL", "XXL"], [3, 6, 5, 0, 2], "#8d96a3"), ("Chinos", "Khaki", ["S", "M", "L", "XL", "XXL"], [1, 3, 0, 2, 1], "#c8b38a")]
SH = {"Polo tee": '<path d="M35 20 L50 12 Q60 22 70 12 L85 20 L110 45 L95 60 L88 52 V140 H32 V52 L25 60 L10 45 Z" fill="{c}"/><path d="M50 12 L60 34 L70 12" fill="#fff" opacity=".5"/>',
 "Kurta set": '<path d="M38 14 L52 8 Q60 18 68 8 L82 14 L104 40 L92 52 L86 46 L90 150 H30 L34 46 L28 52 L16 40 Z" fill="{c}"/><path d="M60 16 V60" stroke="#fff" stroke-width="3" opacity=".6"/><circle cx="60" cy="30" r="2.5" fill="#fff"/><circle cx="60" cy="44" r="2.5" fill="#fff"/>',
 "Hoodie": '<path d="M40 30 Q40 6 60 6 Q80 6 80 30 L108 50 L96 66 L88 58 V140 H32 V58 L24 66 L12 50 Z" fill="{c}"/><path d="M46 30 Q60 46 74 30" stroke="#fff" stroke-width="3" fill="none" opacity=".6"/><rect x="42" y="96" width="36" height="20" rx="6" fill="#fff" opacity=".25"/>',
 "Chinos": '<path d="M30 10 H90 L98 150 H66 L60 60 L54 150 H22 Z" fill="{c}"/><path d="M30 22 H90" stroke="#fff" stroke-width="3" opacity=".5"/>'}
P["p124_garment_s4"] = rg(4, """<div class=kt><b>3</b>CATALOGUE</div><h1 style="margin-top:18px">Share one link.<br><span>Sizes shown live.</span></h1>""",
browser(f'''<div class=ct4><div class=t4><b>New this week</b><span class=lb>YOUR SHOP · SAMPLE</span></div><div class=g4>
{"".join(f'<div class=it4><div class=im4><svg viewBox="0 0 120 160" width="128" height="171">{SH[a].format(c=c)}</svg></div><div class=tx4><b>{a}</b><span>{col}</span><div class=sz4>' + "".join(f'<i class="{"no" if q==0 else ""}">{s}</i>' for s,q in zip(ss,qs)) + '</div><u>Ask on WhatsApp</u></div></div>' for a,col,ss,qs,c in cat)}
</div></div>''', "shop.yourgarments.in · sample", "flex:1", bar="#efe6d2"),
""".vis{flex-direction:column}
.ct4{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px;background:#fffdf8}
.t4{display:flex;justify-content:space-between;align-items:baseline}.t4 b{font:700 32px/1.2 Cardo}
.g4{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:14px}
.it4{background:#f4eee1;border-radius:16px;padding:12px;display:flex;gap:14px}
.im4{width:140px;flex:none;border-radius:12px;display:flex;align-items:center;justify-content:center;background:#fff}.im4 svg{display:block}
.tx4{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px}.tx4 b{font:700 30px/1.2 Cardo}.tx4 span{font:500 19px 'Fira Sans';color:#7a7466}
.sz4{display:flex;gap:5px;flex-wrap:wrap}.sz4 i{font-style:normal;font:700 17px 'Fira Sans';padding:6px 8px;border-radius:7px;background:#fff;border:1.5px solid #cfc5ad}
.sz4 i.no{color:#c4bba8;text-decoration:line-through;background:transparent}
.tx4 u{text-decoration:none;align-self:flex-start;font:700 17px 'Fira Sans';background:#2d4a6b;color:#fff;padding:7px 10px;border-radius:8px;margin-top:2px}
""")

P["p124_garment_s5"] = rg(5, """<h1>Own a readymade<br>garment shop?<br><span>Let's build your<br>stock and billing app.</span></h1>""",
f'''<div class=c5><div class="cd mh5">{hm("hm")}</div><div class=ls5>{"".join(f'<div class=r5><em>{i}</em><b>{t}</b></div>' for i,t in enumerate(["Stock by style and size","Billing that cuts stock","Reorder list","Catalogue link"],1))}</div></div>''',
HMCSS + """.c5{flex:1;display:flex;flex-direction:column;gap:14px}
.mh5{flex:none;height:330px;display:flex}.mh5 .hm{padding:12px 16px;gap:5px}.mh5 .hr{grid-template-columns:150px repeat(5,1fr);gap:5px}.mh5 .hr span{font-size:16px}.mh5 .hr i{font-size:16px;border-radius:6px}.mh5 .hr b{font-size:15px}
.ls5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.r5{background:#2d4a6b;color:#fff;border-radius:18px;display:flex;align-items:center;gap:14px;padding:0 20px}
.r5 em{width:50px;height:50px;border-radius:12px;background:#d9533f;font:700 26px/1 Cardo;font-style:normal;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:700 28px/1.2 Cardo}
""", cta="Garment shop? DM us", ctacss="background:#d9533f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
