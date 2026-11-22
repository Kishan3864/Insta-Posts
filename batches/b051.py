import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 271 INDIA · Car seat cover maker · SINGLE · TeX Gyre Adventor + Open Sans · leather tan / charcoal / stitch orange
# New technique: top-down car interior with each seat zone filled by the picked fabric pattern, linked to a fitting slot.
FAB = {"Tan leatherette": "repeating-linear-gradient(0deg,#b07842 0 18px,#9c6634 18px 20px)", "Black + orange stitch": "repeating-linear-gradient(0deg,#2b2b2e 0 16px,#e8792b 16px 18px,#2b2b2e 18px 22px)", "Grey fabric": "radial-gradient(circle,#9a9ea6 0 1.5px,transparent 2px) 0 0/7px 7px,#7f848c"}
pick = {"front": "Black + orange stitch", "rear": "Tan leatherette"}
seat = lambda f, w, h: f'<div class=st style="width:{w}px;height:{h}px;background:{FAB[f]}"><i class=hr></i></div>'
car = f'''<div class=cb><div class=bdy><div class=ws></div>
<div class=rw>{seat(pick["front"],150,170)}<div class=cn></div>{seat(pick["front"],150,170)}</div>
<div class=rw>{seat(pick["rear"],420,150)}</div>
<div class=bt2></div></div>
<span class="lb l1">Front seats</span><span class="lb l2">Rear bench</span></div>'''
P["p271_seatcover"] = page("""
body{--f:'Open Sans';--h:'TeX Gyre Adventor';background:#f2ede6;color:#232326}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#d4661c;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#a8672f}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.cc{width:500px;flex:none;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(35,35,38,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#7a746c}
.cb{flex:1;position:relative;display:flex;justify-content:center;align-items:center}
.bdy{width:440px;height:100%;max-height:720px;background:#dfe3e8;border:8px solid #232326;border-radius:150px 150px 90px 90px;padding:120px 20px 50px;display:flex;flex-direction:column;gap:34px;align-items:center;position:relative}
.ws{position:absolute;top:40px;left:50px;right:50px;height:60px;border-radius:60px 60px 10px 10px;background:#a9c6dc;border:5px solid #232326}
.bt2{position:absolute;bottom:18px;left:80px;right:80px;height:20px;border-radius:0 0 30px 30px;background:#a9c6dc;border:4px solid #232326}
.rw{display:flex;gap:20px;align-items:center}
.st{border-radius:30px 30px 18px 18px;border:5px solid #232326;position:relative;box-shadow:inset 0 -14px 0 rgba(0,0,0,.18)}
.hr{position:absolute;top:12px;left:50%;width:64px;height:28px;margin-left:-32px;border-radius:10px;background:rgba(255,255,255,.18);border:4px solid #232326}
.cn{width:50px;height:150px;border-radius:12px;background:#4a4a50}
.lb{position:absolute;font:700 16px 'Open Sans';background:#232326;color:#fff;padding:6px 12px;border-radius:10px}.l1{left:0;top:38%}.l2{right:0;top:66%}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.fp{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(35,35,38,.08)}
.fr{flex:1;display:flex;align-items:center;gap:14px;border-radius:16px;padding:0 14px;border:3px solid #ece6dd}
.fr i{width:64px;height:64px;border-radius:14px;flex:none;border:2px solid #232326}
.fr b{flex:1;font:700 21px/1.3 'Open Sans'}.fr em{font:700 15px 'Open Sans';font-style:normal;padding:6px 10px;border-radius:8px;background:#fbe6d6;color:#b3520f}
.fr.on{border-color:#d4661c}
.fs{background:#232326;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.fs small{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#f2b07e}
.fx{display:flex;justify-content:space-between;font:500 19px 'Open Sans';color:#cfcac3}.fx b{color:#fff;font-weight:700}
""", "<div class=kk>CAR SEAT COVER MAKER · FITTING BOOKINGS</div><h1>Let them see the seats<br><span>before you stitch.</span></h1>",
f'''<div class=vw><div class=cc><small class=cap>SAMPLE HATCHBACK · TOP VIEW</small>{car}</div>
<div class=rc><div class=fp><small class=cap>FABRIC PICKED · TAP TO CHANGE</small>{"".join(f'<div class="fr{" on" if f in pick.values() else ""}"><i style="background:{bg}"></i><b>{f}</b>{"<em>Front</em>" if pick["front"]==f else ("<em>Rear</em>" if pick["rear"]==f else "")}</div>' for f,bg in FAB.items())}</div>
<div class=fs><small>FITTING SLOT · SAMPLE</small>{"".join(f'<div class=fx><span>{a}</span><b>{b}</b></div>' for a,b in [("Car","Sample hatchback"),("Seats","5 seats + headrests"),("Fitting","Sat 28 Nov · 11 AM"),("Time","About 3 hours")])}</div></div></div>''',
"#232326", "Make seat covers? DM us", "background:#d4661c;color:#fff")

# ───────── 272 USA · Screen printing shop · SINGLE · Archivo Black + DM Sans · ink magenta / black / off-white
# New technique: flat t-shirt with print area box + size-run as stacked folded shirts, linked to a proof approval.
tee = '''<svg viewBox="0 0 420 440" class=te><path d="M120 30 L170 10 Q210 40 250 10 L300 30 L400 100 L355 165 L320 140 L320 420 L100 420 L100 140 L65 165 L20 100 Z" fill="#f4f1ec" stroke="#1b1b1d" stroke-width="7" stroke-linejoin="round"/>
<path d="M170 10 Q210 50 250 10" fill="none" stroke="#1b1b1d" stroke-width="6"/>
<rect x="140" y="110" width="140" height="140" fill="#d6247e" fill-opacity=".12" stroke="#d6247e" stroke-width="4" stroke-dasharray="10 7"/>
<circle cx="210" cy="165" r="34" fill="#d6247e"/><rect x="160" y="210" width="100" height="14" rx="7" fill="#1b1b1d"/><rect x="175" y="230" width="70" height="10" rx="5" fill="#1b1b1d" fill-opacity=".5"/>
<text x="210" y="290" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="20" fill="#d6247e">Print area 12 × 12 in</text></svg>'''
sizes = [("S", 10), ("M", 25), ("L", 30), ("XL", 15), ("2XL", 5)]
P["p272_screenprint"] = page("""
body{--f:'DM Sans';--h:'Archivo Black';background:#f6f3ee;color:#1b1b1d}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#d6247e;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.22;margin-top:16px} h1 span{color:#d6247e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp{flex:1;min-height:0;display:flex;gap:14px}
.pc{width:430px;flex:none;background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(27,27,29,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#77726a}
.te{width:100%;flex:1;min-height:0;display:block}
.ink{display:flex;gap:8px}.ink span{flex:1;display:flex;align-items:center;gap:8px;font:700 16px 'DM Sans';background:#f6f3ee;border-radius:10px;padding:8px 10px}.ink i{width:22px;height:22px;border-radius:50%}
.sr{flex:1;min-width:0;background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(27,27,29,.08)}
.sz{flex:1;display:grid;grid-template-columns:70px 1fr 60px;gap:12px;align-items:center;border-top:1px solid #efebe4}
.sz b{font:400 26px/1.4 'Archivo Black'}
.stk{display:flex;flex-wrap:wrap;gap:4px}.stk i{width:22px;height:16px;border-radius:4px 4px 2px 2px;background:#f4f1ec;border:2px solid #1b1b1d;position:relative}.stk i:after{content:"";position:absolute;left:5px;top:3px;width:8px;height:6px;background:#d6247e;border-radius:2px}
.sz em{font:800 24px 'DM Sans';font-style:normal;text-align:right}
.tt{border-top:2px solid #1b1b1d}.tt em{color:#d6247e}
.bt{display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.bx{background:#1b1b1d;color:#fff;border-radius:22px;padding:14px 18px}.bx small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#f59ac6}.bx b{font:700 24px/1.4 'DM Sans'}
.bx.p{background:#d6247e}.bx.p small{color:#ffe0ef}
""", "<div class=kk>SCREEN PRINTING SHOP · BULK ORDERS</div><h1>Sizes, colors and proof,<br><span>in one order page.</span></h1>",
f'''<div class=vw><div class=tp><div class=pc><small class=cap>PROOF 1 · FRONT · SAMPLE DESIGN</small>{tee}<div class=ink><span><i style="background:#d6247e"></i>Magenta</span><span><i style="background:#1b1b1d"></i>Black</span><span><i style="background:#f4f1ec;border:2px solid #1b1b1d"></i>White tee</span></div></div>
<div class=sr><small class=cap>SIZE RUN · 1 SHIRT ICON = 1 SHIRT</small>{"".join(f'<div class=sz><b>{s}</b><div class=stk>{"".join("<i></i>" for _ in range(n))}</div><em>{n}</em></div>' for s,n in sizes)}<div class="sz tt"><b>ALL</b><div style="font:600 18px DM Sans;color:#77726a">2 ink colors · front only</div><em>{sum(n for _,n in sizes)}</em></div></div></div>
<div class=bt><div class="bx p"><small>PROOF</small><b>Approved Tue</b></div><div class=bx><small>PRINT DAY</small><b>Thu 26 Nov</b></div><div class=bx><small>PICKUP</small><b>Fri 27 · 3 PM</b></div></div></div>''',
"#1b1b1d", "Run a print shop? DM us", "background:#d6247e;color:#fff")

# ───────── 273 INDIA · Saree fall and pico service · SINGLE · Cardo + Poppins · peacock teal / rose / ivory
# New technique: pigeonhole rack (grid of cubbies) where each folded saree carries its ticket number and ready time.
holes = [("T-41", "Fall + pico", "Ready", "r", "#1b7a7a"), ("T-42", "Pico only", "Ready", "r", "#c2416b"), ("T-43", "Fall + pico", "4 PM today", "w", "#e2a72e"),
 ("T-44", "Fall only", "4 PM today", "w", "#5a3e8c"), ("T-45", "Fall + pico", "Tomorrow 11 AM", "t", "#2f8f5b"), ("T-46", "Pico only", "Tomorrow 11 AM", "t", "#d2573a"),
 ("T-47", "Fall + pico", "Tomorrow 5 PM", "t", "#3567b0"), ("", "", "Empty", "e", ""), ("T-48", "Fall only", "Collected", "c", "#9a8f80")]
def fold(c):
    return f'<div class=fd style="background:linear-gradient(180deg,{c} 0 58%,#f6e7b8 58% 66%,{c} 66%)"></div>'
P["p273_saree"] = page("""
body{--f:'Poppins';--h:'Cardo';background:#f8f3ea;color:#173e3e}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#c2416b;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#1b7a7a}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.rk{flex:1;min-width:0;background:#8a5d3b;border-radius:20px;padding:16px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);gap:12px;box-shadow:inset 0 0 0 6px #6e4a2f}
.ch{background:#5c3c25;border-radius:10px;padding:12px 10px 10px;display:flex;flex-direction:column;gap:6px;box-shadow:inset 0 10px 18px rgba(0,0,0,.35)}
.fd{flex:1;border-radius:8px;box-shadow:0 -4px 0 rgba(255,255,255,.18) inset}
.tk{background:#fffaf0;border-radius:8px;padding:8px 12px;display:grid;grid-template-columns:auto 1fr;column-gap:8px;align-items:baseline}.tk em{grid-column:1 / 3}
.tk b{font:700 24px/1.3 Cardo}.tk span{font:600 15px Poppins;color:#6b6355;text-align:right}
.tk em{display:block;font:700 16px Poppins;font-style:normal}
.r .tk em{color:#2f8f5b}.w .tk em{color:#c98a00}.t .tk em{color:#3567b0}.c .tk em{color:#9a8f80}
.ch.e{align-items:center;justify-content:center;font:600 16px Poppins;color:#c9a888;border:3px dashed #a37a57;background:#6b4830}
.ch.c .fd{opacity:.35}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.mg{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:16px;box-shadow:0 14px 30px rgba(23,62,62,.08)}
.cap{font:600 14px/1.4 'Poppins';letter-spacing:2px;color:#7a7367}
.bb{background:#e7f3f1;border-radius:16px 16px 16px 4px;padding:20px 18px;font:500 21px/1.5 Poppins}.bb b{color:#1b7a7a}
.cnt{margin-top:auto;display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.cnt div{background:#f8f3ea;border-radius:14px;padding:10px;text-align:center}.cnt div{padding:18px 8px!important}.cnt b{display:block;font:700 52px/1.3 Cardo;color:#1b7a7a}.cnt span{font:600 14px Poppins;color:#6b6355}.lgd2{flex:none;display:grid;grid-template-columns:1fr 1fr;gap:12px;background:#173e3e;color:#fff;border-radius:24px;padding:16px 20px}
.lgd2 span{display:flex;align-items:center;gap:10px;font:500 18px Poppins}.lgd2 i{width:16px;height:16px;border-radius:50%}
""", "<div class=kk>SAREE FALL AND PICO SERVICE</div><h1>“Is my saree ready?”<br><span>Check the ticket, not the pile.</span></h1>",
f'''<div class=vw><div class=rk>{"".join(f'<div class="ch {k}">Empty slot</div>' if k=="e" else f'<div class="ch {k}">{fold(c)}<div class=tk><b>{t}</b><span>{j}</span><em>{st}</em></div></div>' for t,j,st,k,c in holes)}</div>
<div class=sd><div class=mg><small class=cap>MESSAGE SENT · SAMPLE</small><div class=bb>Your saree <b>T-43</b> (fall + pico) will be ready at <b>4 PM today</b>.</div><div class=bb>Ticket <b>T-41</b> is ready. Please collect it from the counter.</div><div class=bb>Tickets <b>T-45</b> and <b>T-46</b> will be ready <b>tomorrow at 11 AM</b>.</div><div class=cnt>{"".join(f"<div><b>{n}</b><span>{l}</span></div>" for n,l in [(2,"Ready"),(2,"Today"),(3,"Tomorrow")])}</div></div>
<div class=lgd2>{"".join(f'<span><i style="background:{c}"></i>{a}</span>' for a,c in [("Ready","#2f8f5b"),("Today","#c98a00"),("Tomorrow","#3567b0"),("Collected","#9a8f80")])}</div></div></div>''',
"#173e3e", "Do fall and pico work? DM us", "background:#1b7a7a;color:#fff")

# ───────── 274 INDIA · Bamboo and cane furniture maker · CAROUSEL 5 · Bitter + Open Sans · cane gold / bamboo green / clay
# New technique: CSS cane weave (octagon holes from conic + radial gradients) used as a material swatch through the carousel.
CANE = "radial-gradient(circle at 50% 50%,#f7efdc 0 22%,transparent 24%) 0 0/34px 34px,repeating-linear-gradient(45deg,#c9a25c 0 4px,transparent 4px 17px),repeating-linear-gradient(-45deg,#c9a25c 0 4px,transparent 4px 17px),repeating-linear-gradient(0deg,#b88d45 0 4px,transparent 4px 17px),repeating-linear-gradient(90deg,#b88d45 0 4px,transparent 4px 17px),#e8d3a6"
BB = """
body{--f:'Open Sans';--h:'Bitter';background:#f4efe3;color:#24361f}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#b5562e;margin-top:22px;align-self:flex-start}
h1{font-family:'Bitter';font-weight:800;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#4f7a2f}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(36,54,31,.08)}
.cap{font:700 14px/1.4 'Open Sans';letter-spacing:2px;color:#7a7462}
.cn{background:""" + CANE + """;border:6px solid #8a6a2f;border-radius:14px}
.bam{background:repeating-linear-gradient(90deg,#7ea64a 0 22px,#5f8a35 22px 26px);border-radius:12px}
.nb{display:flex;align-items:center;gap:14px;background:#24361f;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'Open Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#b5562e}.nb b{color:#f2d59a}
"""
def bb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#24361f;color:#fff"):
    return page(BB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#24361f", cta, ctacss, tagline=f"{n} / 5")
def chair(s=1.0):
    return f'<div class=chr style="width:{int(200*s)}px;height:{int(260*s)}px"><div class="cn bk3"></div><div class="cn st3"></div><div class="bam lg1"></div><div class="bam lg2"></div></div>'
CH = ".chr{position:relative;flex:none}.bk3{position:absolute;left:10%;right:10%;top:0;height:46%}.st3{position:absolute;left:0;right:0;top:46%;height:18%;border-radius:10px}.lg1,.lg2{position:absolute;top:64%;bottom:0;width:12%;border-radius:6px}.lg1{left:6%}.lg2{right:6%}"
P["p274_cane_s1"] = bb(1, "BAMBOO AND CANE FURNITURE · MADE TO ORDER", "“Send photos of all designs”?<br><span>Send one catalogue link.</span>",
f'''<div class=w1><div class="cd gl">{"".join(f'<div class=it><div class=ph>{chair(0.62)}</div><b>{a}</b><span>{b}</span></div>' for a,b in [("Lounge chair","C-01 · 2 sizes"),("Dining chair","C-02 · set of 4"),("Cafe chair","C-03 · stackable"),("Easy chair","C-04 · wide seat"),("Balcony chair","C-05 · sold as a pair"),("Study chair","C-06 · with arms")])}</div>
<div class=nb><span class=ib>{ic("send",26)}</span><span>Customers browse codes, sizes and finish. <b>No more photo after photo on chat.</b></span></div></div>''',
css=CH + """.w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.gl{flex:1;padding:16px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px}
.it{background:#f7f2e6;border-radius:18px;padding:12px;display:flex;flex-direction:column;gap:2px}.ph{flex:1;display:flex;align-items:center;justify-content:center}.it b{font:700 22px/1.3 Bitter}.it span{font:600 16px 'Open Sans';color:#7a7462}""")

P["p274_cane_s2"] = bb(2, "STEP 1 · PICK DESIGN, SIZE AND FINISH", "Every order starts<br><span>with clear choices.</span>",
f'''<div class=w2><div class="cd hero"><div class=hc>{chair(1.6)}</div><div class=tagc><b>C-01 Lounge chair</b><span>Sample order O-274</span></div></div>
<div class=opts>{"".join(f'<div class="cd op"><small class=cap>{a}</small><div class=ch3>{"".join(f"<span class={chr(34)}{c}{chr(34)}>{t}</span>" for t,c in b)}</div></div>' for a,b in [("SIZE",[("Regular","on"),("Large","")]),("FINISH",[("Natural","on"),("Walnut",""),("Black","")]),("CUSHION",[("Mustard","on"),("Grey",""),("None","")]),("QUANTITY",[("2 chairs","on")])])}</div></div>''',
css=CH + """.w2{flex:1;display:flex;gap:14px;min-height:0}.hero{flex:1;min-width:0;display:flex;flex-direction:column;padding:20px}.hc{flex:1;display:flex;align-items:center;justify-content:center}
.tagc{background:#24361f;color:#fff;border-radius:16px;padding:14px 18px}.tagc b{display:block;font:700 28px/1.3 Bitter}.tagc span{font:500 17px 'Open Sans';color:#cfd8c8}
.opts{width:380px;flex:none;display:flex;flex-direction:column;gap:12px}.op{flex:1;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.ch3{display:flex;gap:8px;flex-wrap:wrap}.ch3 span{font:700 18px 'Open Sans';padding:10px 14px;border-radius:12px;border:3px solid #e8e1cf}.ch3 span.on{border-color:#4f7a2f;background:#eef5e6;color:#3b6122}""")

stages = [("Frame", "Bamboo cut and bent", 100), ("Weave", "Cane seat and back", 60), ("Finish", "Natural polish", 0), ("Cushion", "Mustard, stitched", 100)]
P["p274_cane_s3"] = bb(3, "STEP 2 · MAKING STAGES THE CUSTOMER CAN SEE", "Handmade takes time.<br><span>Show where it is.</span>",
f'''<div class=w3><div class="cd sg">{"".join(f'<div class=sr><div class=nm><b>{a}</b><span>{b}</span></div><div class=bar><i class="{"cn" if a=="Weave" else ""}" style="width:{p}%"></i></div><em>{"Done" if p==100 else (f"{p}%" if p else "Next")}</em></div>' for a,b,p in stages)}</div>
<div class=nb><span class=ib>{ic("camera",26)}</span><span>A weaving photo goes out today. <b>Ready date: Sat 5 Dec, sample.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.sg{flex:1;padding:18px 26px;display:flex;flex-direction:column}
.sr{flex:1;display:grid;grid-template-columns:260px 1fr 90px;gap:18px;align-items:center;border-bottom:1px solid #efe9da}.sr:last-child{border:0}
.nm b{display:block;font:700 32px/1.3 Bitter}.nm span{font:500 19px 'Open Sans';color:#6b6553}
.bar{height:54px;border-radius:14px;background:#f1ecdf;overflow:hidden}.bar i{display:block;height:100%;border-radius:14px;background:#4f7a2f}.bar i.cn{border:0;border-radius:14px}
.sr em{font:800 22px 'Open Sans';font-style:normal;text-align:right;color:#4f7a2f}""")

P["p274_cane_s4"] = bb(4, "STEP 3 · DISPATCH WITHOUT SURPRISES", "Packed, photographed,<br><span>on its way.</span>",
f'''<div class=w4><div class="cd pk"><div class=bx4><div class=tp4>FRAGILE · CANE</div>{chair(1.1)}</div></div>
<div class=dl>{"".join(f'<div class="cd dr"><small class=cap>{a}</small><b>{b}</b></div>' for a,b in [("PACKING PHOTO","Sent Sat 5 Dec"),("TRANSPORT","Sample transport, LR 4471"),("REACHES","About Tue 8 Dec"),("CUSTOMER","Gets every update by message")])}</div></div>''',
css=CH + """.w4{flex:1;display:flex;gap:14px;min-height:0}.pk{flex:1;min-width:0;display:flex;align-items:center;justify-content:center;padding:24px}
.bx4{width:100%;height:100%;border:6px dashed #8a6a2f;border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;background:repeating-linear-gradient(0deg,#f4e7c9 0 30px,#efdfbb 30px 32px)}
.tp4{font:800 24px 'Open Sans';letter-spacing:3px;color:#b5562e;background:#fff;padding:8px 18px;border-radius:10px;border:3px solid #b5562e}
.dl{width:380px;flex:none;display:flex;flex-direction:column;gap:12px}.dr{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center}.dr b{font:700 26px/1.35 Bitter}""")

P["p274_cane_s5"] = bb(5, "YOUR TURN", "Make cane or bamboo furniture?<br><span>Let's build your catalogue.</span>",
f'''<div class=w5><div class="cd hp">{chair(0.95)}{chair(1.25)}{chair(0.95)}</div>
<div class=tl>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("grid","Catalogue link","Codes, sizes, finish"),("doc","Clear orders","Every choice saved"),("chart","Making stages","With photos"),("truck","Dispatch","Updates by message")])}</div>
<div class=q>How do customers choose a design from you today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b5562e;color:#fff",
css=CH + """.w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;justify-content:center;align-items:flex-end;gap:50px;padding:24px 24px 34px}
.tl{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(36,54,31,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#eef5e6;color:#4f7a2f}.ti b{display:block;font:700 28px/1.35 Bitter}.ti div span{font:500 19px/1.35 'Open Sans';color:#6b6553}
.q{background:#24361f;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Open Sans'}""")

# ───────── 275 INDIA · Housekeeping supplies dealer · SINGLE · Gelasio + Roboto · mop blue / lemon / white
# New technique: a long receipt-style monthly supply list (zigzag bottom, dotted leaders) per office, with quantities only.
items = [("Floor cleaner, 5 L", 4), ("Toilet cleaner, 1 L", 12), ("Hand wash refill, 5 L", 3), ("Garbage bags, large", 10), ("Tissue rolls", 48), ("Mop refills", 6), ("Glass cleaner, 500 ml", 4)]
P["p275_supplies"] = page("""
body{--f:'Roboto';--h:'Gelasio';background:#e8f0f8;color:#10305a}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#2a7bd1;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#2a7bd1}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.rc{flex:1;min-width:0;background:#fffef9;padding:24px 28px 40px;display:flex;flex-direction:column;filter:drop-shadow(0 14px 22px rgba(16,48,90,.15));clip-path:polygon(0 0,100% 0,100% calc(100% - 14px),97% 100%,94% calc(100% - 14px),91% 100%,88% calc(100% - 14px),85% 100%,82% calc(100% - 14px),79% 100%,76% calc(100% - 14px),73% 100%,70% calc(100% - 14px),67% 100%,64% calc(100% - 14px),61% 100%,58% calc(100% - 14px),55% 100%,52% calc(100% - 14px),49% 100%,46% calc(100% - 14px),43% 100%,40% calc(100% - 14px),37% 100%,34% calc(100% - 14px),31% 100%,28% calc(100% - 14px),25% 100%,22% calc(100% - 14px),19% 100%,16% calc(100% - 14px),13% 100%,10% calc(100% - 14px),7% 100%,4% calc(100% - 14px),0 100%)}
.rh{text-align:center;border-bottom:2px dashed #10305a;padding-bottom:12px}.rh b{display:block;font:700 30px/1.3 Gelasio}.rh span{font:500 17px Roboto;color:#5a6b85}
.ri{flex:1;display:flex;align-items:baseline;gap:10px;font:500 21px Roboto;padding-top:12px}.ri i{flex:1;border-bottom:3px dotted #b9c6d8}.ri b{font:700 24px Roboto}
.rt{display:flex;justify-content:space-between;border-top:2px dashed #10305a;padding-top:12px;margin-top:10px;font:700 20px Roboto}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:12px}
.cd{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 14px 30px rgba(16,48,90,.08)}
.cd small{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#6b7b93}.cd b{font:700 30px/1.3 Gelasio}.cd span{font:500 18px/1.4 Roboto;color:#4a5b75}
.cd.y{background:#ffe45c}.cd.y span{color:#3d3a10}.cd.d{background:#10305a;color:#fff}.cd.d small{color:#a9cdf5}.cd.d span{color:#cfdbec}
""", "<div class=kk>HOUSEKEEPING SUPPLIES · OFFICE ORDERS</div><h1>Same list every month?<br><span>Send it before they ask.</span></h1>",
f'''<div class=vw><div class=rc><div class=rh><b>Monthly supply list</b><span>Sample Office, 3rd floor · December · sample</span></div>
{"".join(f'<div class=ri><span>{a}</span><i></i><b>× {q}</b></div>' for a,q in items)}
<div class=rt><span>{len(items)} items</span><span>Deliver Tue 1 Dec</span></div></div>
<div class=sd><div class="cd y"><small>CHANGE THIS MONTH</small><b>+ 2 hand wash</b><span>Office manager added on the link</span></div>
<div class=cd><small>SENT FOR OK</small><b>Thu 26 Nov</b><span>List goes out 5 days before delivery</span></div>
<div class="cd d"><small>YOUR OFFICES</small><b>14 lists</b><span>Same day each month, sample</span></div></div></div>''',
"#10305a", "Supply offices? DM us", "background:#2a7bd1;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
