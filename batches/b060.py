import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 316 INDIA · Trophy and medal shop · CAROUSEL 5 · Cardo + Poppins · trophy gold / velvet navy / ivory
# New technique: SVG gold trophies (cup, star, plaque) with gradient metal and engraving plates whose text is the proof.
TR = """
body{--f:'Poppins';--h:'Cardo';background:#f6f1e4;color:#1d2550}
.kk{font:600 16px/1.4 'Poppins';letter-spacing:3px;color:#a07a1c;margin-top:22px;align-self:flex-start}
h1{font-family:'Cardo';font-weight:700;font-size:68px;line-height:1.3} h1 span{color:#a07a1c}
.cd{background:#fffcf4;border-radius:22px;box-shadow:0 12px 28px rgba(29,37,80,.08)}
.cap{font:600 13px/1.4 'Poppins';letter-spacing:2px;color:#7f7a6a}
.nb{display:flex;align-items:center;gap:14px;background:#1d2550;color:#fff;border-radius:20px;padding:16px 20px;font:500 20px/1.45 'Poppins'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e6c25a;color:#1d2550}.nb b{color:#f0d47e}
"""
def tr(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1d2550;color:#f0d47e"):
    return page(TR + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1d2550", cta, ctacss, tagline=f"{n} / 5")
GOLD = '<defs><linearGradient id="gd" x1="0" x2="1"><stop offset="0" stop-color="#b8892a"/><stop offset=".45" stop-color="#f6dc86"/><stop offset=".6" stop-color="#e2b84a"/><stop offset="1" stop-color="#9c7222"/></linearGradient></defs>'
def cup(w=220, line1="Office Cup", line2="2026"):
    return f'''<svg viewBox="0 0 220 330" width="{w}" class=tp>{GOLD}<path d="M50 20 H170 Q170 120 110 140 Q50 120 50 20 Z" fill="url(#gd)"/>
<path d="M50 35 Q10 35 14 70 Q18 100 60 108" stroke="url(#gd)" stroke-width="12" fill="none"/><path d="M170 35 Q210 35 206 70 Q202 100 160 108" stroke="url(#gd)" stroke-width="12" fill="none"/>
<rect x="98" y="138" width="24" height="50" fill="url(#gd)"/><rect x="70" y="186" width="80" height="18" rx="4" fill="url(#gd)"/>
<rect x="40" y="204" width="140" height="110" rx="6" fill="#1d2550"/><rect x="56" y="224" width="108" height="70" rx="4" fill="url(#gd)"/>
<text x="110" y="254" text-anchor="middle" font-family="Cardo" font-weight="700" font-size="19" fill="#1d2550">{line1}</text><text x="110" y="280" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="15" fill="#1d2550">{line2}</text></svg>'''
def star(w=180, line1="Best Player"):
    pts = " ".join(f"{90+math.cos(math.radians(-90+i*36))*(70 if i%2==0 else 30):.0f},{80+math.sin(math.radians(-90+i*36))*(70 if i%2==0 else 30):.0f}" for i in range(10))
    return f'''<svg viewBox="0 0 180 300" width="{w}" class=tp>{GOLD}<polygon points="{pts}" fill="url(#gd)"/><rect x="80" y="148" width="20" height="40" fill="url(#gd)"/>
<rect x="30" y="186" width="120" height="100" rx="6" fill="#1d2550"/><rect x="44" y="206" width="92" height="56" rx="4" fill="url(#gd)"/>
<text x="90" y="240" text-anchor="middle" font-family="Cardo" font-weight="700" font-size="16" fill="#1d2550">{line1}</text></svg>'''
def plaque(w=200, line1="Blue Hawks", line2="Winners"):
    return f'''<svg viewBox="0 0 200 260" width="{w}" class=tp>{GOLD}<rect x="10" y="10" width="180" height="240" rx="12" fill="#6b3d22"/><rect x="22" y="22" width="156" height="216" rx="8" fill="#8a5330"/>
<circle cx="100" cy="80" r="40" fill="url(#gd)"/><rect x="34" y="150" width="132" height="70" rx="4" fill="url(#gd)"/>
<text x="100" y="180" text-anchor="middle" font-family="Cardo" font-weight="700" font-size="20" fill="#1d2550">{line1}</text><text x="100" y="205" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="14" fill="#1d2550">{line2}</text></svg>'''
P["p316_trophy_s1"] = tr(1, "TROPHY AND MEDAL SHOP · EVENT ORDERS", "Wrong name on a trophy?<br><span>Check it before engraving.</span>",
f'''<div class=w1><div class="cd po1"><div class=pd1><div class=st1>{star(190)}<span class=p2>2</span></div><div class=st1>{cup(250)}<span class=p1>1</span></div><div class=st1>{plaque(210)}<span class=p3>3</span></div></div></div>
<div class=bb1><span class=vn>{ic("chat",24)} Customer, one day before the event</span><p>“It is ‘Blue Hawks’, not ‘Blue Hawk’! Can you change it by tomorrow?”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.po1{flex:1;min-height:0;padding:20px 24px;display:flex;align-items:flex-end;background:radial-gradient(circle at 50% 30%,#fffaf0,#f3ead2)}
.pd1{width:100%;display:flex;justify-content:center;align-items:flex-end;gap:14px}.st1{display:flex;flex-direction:column;align-items:center}.tp{display:block}
.st1 span{width:100%;display:flex;align-items:center;justify-content:center;background:#1d2550;color:#f0d47e;font:700 40px/1.4 Cardo;border-radius:10px 10px 0 0}.p1{height:150px}.p2{height:100px}.p3{height:70px}
.bb1{background:#1d2550;color:#fff;border-radius:22px 22px 22px 6px;padding:18px 22px}.vn{display:flex;align-items:center;gap:10px;font:600 15px 'Poppins';color:#f0d47e;margin-bottom:6px}.bb1 p{font:500 23px/1.45 'Poppins'}""")

items = [("Big cup · 24 in", "Winners", 1), ("Big cup · 18 in", "Runners-up", 1), ("Star trophy", "Best player, best bowler", 2), ("Wooden plaque", "Team photo plaque", 3), ("Medals · gold colour", "Winning team", 12), ("Medals · silver colour", "Runners-up team", 12)]
tot_items = sum(i[2] for i in items)
P["p316_trophy_s2"] = tr(2, "STEP 1 · ONE ORDER FORM FOR THE EVENT", "Office cricket cup?<br><span>{} pieces, one list.</span>".format(tot_items),
f'''<div class=w2><div class="cd tb2"><div class="rw2 hd2"><span>ITEM · SAMPLE</span><span>FOR</span><span>QTY</span></div>
{"".join(f'<div class=rw2><b>{a}</b><span>{b}</span><em>{q}</em></div>' for a,b,q in items)}
<div class="rw2 tt2"><b>Total pieces</b><span>Event: Sun 6 Dec · pickup Sat 5 Dec</span><em>{tot_items}</em></div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>The customer fills the names on the same form, <b>so nothing is typed twice.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tb2{flex:1;padding:12px 26px;display:flex;flex-direction:column}
.rw2{flex:1;display:grid;grid-template-columns:1.2fr 1.3fr .4fr;gap:12px;align-items:center;border-bottom:1px solid #eee6d2}
.hd2{flex:none;padding:6px 0 12px;border-bottom:2px solid #1d2550;font:600 13px/1.4 'Poppins';letter-spacing:1.5px;color:#7f7a6a}
.rw2 b{font:700 26px/1.3 Cardo}.rw2>span{font:500 18px/1.4 'Poppins';color:#4b4f66}.rw2 em{font:700 34px/1.3 Cardo;font-style:normal;color:#a07a1c;text-align:right}
.tt2{border:0;background:#f6e9c3;border-radius:14px;padding:0 14px}""")

plates = [("Winners cup", "Office Cricket Cup 2026", "Winners · Blue Hawks", "ok", "Approved Tue 1 Dec"), ("Star trophy 1", "Best Player", "Office Cricket Cup 2026", "ok", "Approved Tue 1 Dec"),
          ("Team plaque", "Blue Hawk", "Winners 2026", "ch", "Change asked: Blue Hawks")]
P["p316_trophy_s3"] = tr(3, "STEP 2 · ENGRAVING PROOF ON THE PHONE", "See the plate first.<br><span>Engrave after the OK.</span>",
f'''<div class=w3>{"".join(f'<div class="cd pr3"><small class=cap>{a.upper()}</small><div class=pl3><b>{l1}</b><span>{l2}</span></div><div class="ss3 {k}"><i>{ic("check",16) if k=="ok" else ic("x",16)}</i>{s}</div></div>' for a,l1,l2,k,s in plates)}
<div class=nb><span class=ib>{ic("check",26)}</span><span>Every plate is checked by the customer, <b>with the date and time saved.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.pr3{flex:1;padding:14px 22px;display:grid;grid-template-columns:200px 1fr 290px;gap:18px;align-items:center}
.pl3{background:linear-gradient(90deg,#b8892a,#f6dc86 45%,#e2b84a 60%,#9c7222);border-radius:10px;padding:16px 20px;text-align:center;box-shadow:inset 0 0 0 4px rgba(29,37,80,.25)}
.pl3 b{display:block;font:700 32px/1.3 Cardo}.pl3 span{font:600 18px/1.4 'Poppins'}
.ss3{display:flex;align-items:center;gap:10px;font:600 18px/1.35 'Poppins'}.ss3 i{width:34px;height:34px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
.ss3.ok i{background:#2f7a4a}.ss3.ch{color:#b23a2a}.ss3.ch i{background:#b23a2a}""")

P["p316_trophy_s4"] = tr(4, "STEP 3 · READY ON TIME, PICKED UP ON TIME", "Event on Sunday?<br><span>Ready on Saturday.</span>",
f'''<div class=w4><div class="cd sp4">{"".join(f'<div class=sr4><i class={k}>{ic("check",16) if k=="d" else ""}</i><div><b>{a}</b><span>{t}</span></div></div>' for a,t,k in [("Order and names in","Mon 30 Nov","d"),("Proofs approved","Tue 1 Dec","d"),("Plaque name fixed","Wed 2 Dec","d"),("Engraving","Thu 3 Dec","n"),("Packed in boxes","Fri 4 Dec","w"),("Pickup","Sat 5 Dec · 5 PM","w")])}</div>
<div class=rt4><div class="cd hr4">{cup(220,"Office Cup","Winners")}</div><div class=ms4><small>MESSAGE · SAMPLE</small><p>Your {tot_items} pieces are packed. Pickup <b>Sat 5 Dec, 5 PM</b>.</p></div></div></div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:1.1fr 1fr;gap:14px;min-height:0}.sp4{padding:16px 24px;display:flex;flex-direction:column}
.sr4{flex:1;display:flex;align-items:center;gap:16px;border-top:1px solid #eee6d2}.sr4:first-child{border:0}.sr4 i{width:36px;height:36px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;color:#fff}
.sr4 i.d{background:#2f7a4a}.sr4 i.n{background:#a07a1c}.sr4 i.w{border:3px solid #cfc6ad}.sr4 b{display:block;font:700 26px/1.3 Cardo}.sr4 span{font:500 17px/1.4 'Poppins';color:#6a6658}
.rt4{display:flex;flex-direction:column;gap:12px;min-height:0}.hr4{flex:1;display:flex;align-items:center;justify-content:center;background:radial-gradient(circle,#fffaf0,#f3ead2)}
.ms4{background:#1d2550;color:#fff;border-radius:22px;padding:16px 20px}.ms4 small{font:600 13px/1.4 'Poppins';letter-spacing:2px;color:#f0d47e}.ms4 p{font:500 20px/1.45 'Poppins';margin-top:6px}.ms4 b{color:#f0d47e}""")

P["p316_trophy_s5"] = tr(5, "YOUR TURN", "Sell trophies and medals?<br><span>Let's build your order form.</span>",
f'''<div class=w5><div class="cd hp5">{star(170)}{cup(230)}{plaque(190)}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,34)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Event order form","Items and names"),("check","Engraving proof","OK before work"),("clock","Ready date","For every order"),("bell","Pickup message","When it is packed")])}</div>
<div class=q>How do customers send you names for engraving today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#a07a1c;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;display:flex;justify-content:center;align-items:flex-end;gap:30px;padding:20px;background:radial-gradient(circle at 50% 30%,#fffaf0,#f3ead2)}.tp{display:block}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fffcf4;border-radius:22px;padding:16px 22px;box-shadow:0 10px 22px rgba(29,37,80,.07)}
.ti .ib{width:64px;height:64px;border-radius:20px;background:#f6e9c3;color:#a07a1c}.ti b{display:block;font:700 26px/1.3 Cardo}.ti div span{font:500 17px/1.4 'Poppins';color:#5d5a4e}
.q{background:#1d2550;color:#fff;border-radius:22px;padding:20px 24px;font:500 22px/1.45 'Poppins'}""")

# ───────── 317 INDIA · Garment stitching job-work unit · SINGLE · Anton + Roboto · denim blue / thread orange / chalk
# New technique: hourly production board (lines x hours) with cells coloured against the hourly target + bundle stage tracker with thread spools.
lines_ = [("Line 1", [52, 55, 58, 60, 48, 57, 60, 0]), ("Line 2", [44, 50, 52, 49, 40, 51, 55, 0]), ("Line 3", [60, 62, 61, 63, 55, 60, 64, 0]), ("Line 4", [38, 45, 47, 50, 42, 48, 50, 0])]
TGT = 50
hours = ["9", "10", "11", "12", "2", "3", "4", "5"]
done_today = sum(sum(v) for _, v in lines_)
po_total = 4000; po_done = 1820 + done_today
P["p317_garment"] = page("""
body{--f:'Roboto';--h:'Anton';background:#e9eef5;color:#1b2d4f}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#e0701e;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:70px;letter-spacing:.5px;line-height:1.3;margin-top:32px} h1 span{color:#2f5fa7}
.vw{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}
.bd7{flex:1;min-height:0;background:#1b2d4f;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.bd7>small{font:700 13px/1.5 'Roboto';letter-spacing:2px;color:#a9c0e4}
.hr7,.ln7{display:grid;grid-template-columns:110px repeat(8,1fr) 90px;gap:6px;align-items:center}
.hr7 span{font:700 14px/1.5 'Roboto';color:#a9c0e4;text-align:center}
.ln7{flex:1}.ln7 b{font:400 26px/1.5 Anton;letter-spacing:.5px;color:#fff}
.ln7 i{height:100%;min-height:54px;border-radius:10px;display:flex;align-items:center;justify-content:center;font:700 21px 'Roboto';font-style:normal}
.ok{background:#3f9a63;color:#fff}.lo{background:#e0701e;color:#fff}.nx{background:#2a3f66;color:#7f95ba;border:2px dashed #4a618a}
.ln7 em{font:400 28px/1.5 Anton;font-style:normal;color:#ffc58a;text-align:right;letter-spacing:.5px}
.bt7{display:grid;grid-template-columns:1.2fr 1fr;gap:12px}
.bn7{background:#fff;border-radius:22px;padding:14px 18px;box-shadow:0 12px 26px rgba(27,45,79,.08)}.bn7 small,.po7 small{display:block;font:700 13px/1.5 'Roboto';letter-spacing:2px;color:#6b7891;margin-bottom:6px}
.sg{display:flex;align-items:center;gap:8px}.sg div{flex:1;text-align:center}.sg i{display:block;width:44px;height:44px;margin:0 auto 4px;border-radius:50%;}
.sg i.d{background:radial-gradient(circle,#fff 0 6px,#3f9a63 7px)}.sg i.n{background:radial-gradient(circle,#fff 0 6px,#e0701e 7px)}.sg i.w{background:radial-gradient(circle,#fff 0 6px,#cfd7e4 7px)}
.sg span{font:600 15px/1.4 'Roboto'}.sg em{flex:none;width:24px;height:3px;background:#cfd7e4}
.po7{background:#e0701e;color:#fff;border-radius:22px;padding:14px 18px}.po7 small{color:#ffe2c8}.po7 b{display:block;font:400 44px/1.4 Anton;letter-spacing:.5px}.po7 span{font:500 16px/1.4 'Roboto'}
.pb7{height:12px;border-radius:6px;background:rgba(255,255,255,.3);overflow:hidden;margin:6px 0}.pb7 i{display:block;height:100%;background:#fff}
""", "<div class=kk>GARMENT STITCHING UNIT · JOB WORK</div><h1>Order due on Saturday?<br><span>See every line, every hour.</span></h1>",
f'''<div class=vw><div class=bd7><small>PIECES STITCHED PER HOUR · TARGET {TGT} · TODAY · SAMPLE</small>
<div class=hr7><span></span>{"".join(f"<span>{h}</span>" for h in hours)}<span>TOTAL</span></div>
{"".join(f'<div class=ln7><b>{n}</b>{"".join(f"<i class={chr(110)+chr(120) if v==0 else (chr(111)+chr(107) if v>=TGT else chr(108)+chr(111))}>{v if v else chr(8212)}</i>" for v in vs)}<em>{sum(vs)}</em></div>' for n,vs in lines_)}</div>
<div class=bt7><div class=bn7><small>BUNDLE B-114 · 50 PIECES · SAMPLE</small><div class=sg>{"<em></em>".join(f'<div><i class={k}></i><span>{a}</span></div>' for a,k in [("Cutting","d"),("Stitching","d"),("Checking","n"),("Packing","w")])}</div></div>
<div class=po7><small>ORDER PO-7 · {po_total:,} T-SHIRTS · SAMPLE</small><b>{po_done:,} done</b><div class=pb7><i style="width:{po_done/po_total*100:.0f}%"></i></div><span>{done_today:,} today · due Sat 5 Dec</span></div></div></div>''',
"#1b2d4f", "Run a stitching unit? DM us", "background:#1b2d4f;color:#fff")

# ───────── 318 INDIA · Mock test centre (adult job exam aspirants) · SINGLE · TeX Gyre Adventor + Roboto · answer-sheet white / pencil yellow / graphite
# New technique: top-down exam hall seat map (desk + chair shapes) with booked / free / your seat, beside an OMR-style bubble strip.
random.seed(318)
rows, cols = 6, 8
booked = set(random.sample(range(rows * cols), 37))
mine = 21; booked.discard(mine)
nfree = rows * cols - len(booked) - 1
def desk(i):
    k = "me" if i == mine else ("bk" if i in booked else "fr")
    return f'<div class="dk {k}"><i class=tb8></i><i class=ch8></i><span>{chr(65 + i // cols)}{i % cols + 1}</span></div>'
P["p318_mocktest"] = page("""
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#f4f3ee;color:#2b2d31}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#b88a00;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#b88a00}
.vw{flex:1;display:grid;grid-template-columns:1fr 330px;gap:14px;min-height:0}
.hl8{background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(43,45,49,.08)}
.hl8>small,.sd8 small{font:700 13px/1.4 'Roboto';letter-spacing:2px;color:#777a80}
.bd8{height:40px;border-radius:10px;background:#2b2d31;color:#fff;display:flex;align-items:center;justify-content:center;font:700 16px 'Roboto';letter-spacing:2px}
.gd8{flex:1;min-height:0;display:grid;grid-template-columns:repeat(8,1fr);grid-template-rows:repeat(6,1fr);gap:8px 10px}
.dk{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;border-radius:10px;position:relative}
.tb8{width:80%;height:26px;border-radius:6px;display:block}.ch8{width:42%;height:14px;border-radius:7px 7px 3px 3px;display:block}
.dk span{font:700 13px/1.3 'Roboto'}
.fr .tb8{background:#fff;border:2.5px solid #b9bcc2}.fr .ch8{background:#d9dbe0}.fr span{color:#8a8d93}
.bk .tb8{background:#5b5f68}.bk .ch8{background:#5b5f68}.bk span{color:#5b5f68}
.me{background:#ffe48a}.me .tb8{background:#f2b705}.me .ch8{background:#2b2d31}.me span{color:#2b2d31}
.lg8{display:flex;gap:20px;font:600 16px 'Roboto'}.lg8 span{display:flex;align-items:center;gap:8px}.lg8 i{width:24px;height:16px;border-radius:4px;display:block}
.sd8{display:flex;flex-direction:column;gap:12px;min-height:0}
.ct8{background:#2b2d31;color:#fff;border-radius:22px;padding:16px 18px}.ct8 small{color:#f2d36b}.ct8 b{display:block;font:700 30px/1.3 'TeX Gyre Adventor';margin:4px 0}.ct8 span{font:500 16px/1.45 'Roboto';color:#d6d8dc}
.sl8{background:#fff;border-radius:22px;padding:14px 18px;box-shadow:0 14px 30px rgba(43,45,49,.08)}
.sr8{display:flex;justify-content:space-between;align-items:center;padding:8px 0;border-top:1px solid #eeede8;font:600 16px/1.4 'Roboto'}.sr8 em{font-style:normal;font-weight:700;font-size:14px;border-radius:8px;padding:4px 10px}
.om{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(43,45,49,.08)}
.oq{flex:1;display:flex;align-items:center;gap:10px;font:700 15px 'Roboto'}.oq b{width:26px}.oq i{width:26px;height:26px;border-radius:50%;border:2px solid #9a9da3;display:flex;align-items:center;justify-content:center;font:600 12px 'Roboto';font-style:normal;color:#777}
.oq i.f{background:#2b2d31;border-color:#2b2d31;color:#fff}
""", "<div class=kk>MOCK TEST CENTRE · ADULT EXAM ASPIRANTS</div><h1>Seats full on Sunday?<br><span>Let them book a seat.</span></h1>",
f'''<div class=vw><div class=hl8><small>HALL A · SUN 29 NOV · 10 AM TEST · SAMPLE</small><div class=bd8>FRONT · INVIGILATOR DESK</div><div class=gd8>{"".join(desk(i) for i in range(rows*cols))}</div>
<div class=lg8><span><i style="background:#5b5f68"></i>Booked {len(booked)}</span><span><i style="background:#fff;border:2.5px solid #b9bcc2"></i>Free {nfree}</span><span><i style="background:#f2b705"></i>Your seat C6</span></div></div>
<div class=sd8><div class=ct8><small>SEAT BOOKED · SAMPLE</small><b>Seat C6</b><span>Sun 29 Nov · 10 AM · Hall A. Reach by 9:40 AM with your ID card.</span></div>
<div class=sl8><small>NEXT TESTS</small>{"".join(f'<div class=sr8><span>{a}</span><em style="background:{c[0]};color:{c[1]}">{b}</em></div>' for a,b,c in [("Sun 29 Nov · 10 AM",f"{nfree} seats left",("#fff2c4","#8a6600")),("Sun 29 Nov · 2 PM","Full",("#eceef2","#555")),("Sun 6 Dec · 10 AM","Open",("#dff3e6","#25713f"))])}</div>
<div class=om><small>ANSWER SHEET PRACTICE · SAMPLE</small>{"".join(f'<div class=oq><b>{q}</b>{"".join(f"<i class={chr(102) if o==a else chr(110)}>{o}</i>" for o in "ABCD")}</div>' for q,a in [(1,"B"),(2,"D"),(3,"A"),(4,"C")])}</div></div></div>''',
"#2b2d31", "Run a mock test centre? DM us", "background:#2b2d31;color:#f2d36b")

# ───────── 319 USA · Furniture assembly service · SINGLE · Montserrat + Open Sans · kraft brown / allen-key silver / teal
# New technique: stacked CSS kraft flat-pack boxes (tape stripe, arrows, box labels) whose sizes follow the items, + browser booking that sums a time estimate.
fp = [("Bed frame", 3, 90, 300), ("Dresser", 2, 120, 260), ("Desk", 1, 60, 220), ("Bookcase", 1, 45, 180)]
mins = sum(q and m for _, q, m, w in fp)
def box(name, n, w):
    return "".join(f'<div class=bx9 style="width:{w-i*14}px"><i class=tp9></i><span>{name} · box {i+1} of {n}</span><em>↑ ↑</em></div>' for i in range(n))
P["p319_assembly"] = page("""
body{--f:'Open Sans';--h:'Montserrat';background:#eef3f2;color:#1f3b3b}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#1d8a83;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:62px;letter-spacing:-1.8px;line-height:1.2} h1 span{color:#1d8a83}
.vw{flex:1;display:grid;grid-template-columns:1fr 470px;gap:14px;min-height:0}
.st9{background:#fff;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;justify-content:flex-end;align-items:center;gap:4px;box-shadow:0 14px 30px rgba(31,59,59,.08)}
.tc9{align-self:stretch;margin-bottom:auto;background:#1f3b3b;color:#fff;border-radius:18px;padding:16px 18px}.tc9 b{display:block;font:800 28px/1.3 Montserrat;color:#7fe0d6;margin-bottom:4px}.tc9 span{font:500 17px/1.45 'Open Sans'}.st9>small{align-self:flex-start;margin-bottom:8px;font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#6d8080}
.bx9{height:84px;border-radius:6px;background:linear-gradient(#d2a874,#c39461);position:relative;display:flex;align-items:center;justify-content:space-between;padding:0 16px;box-shadow:inset 0 -5px 0 rgba(0,0,0,.12)}
.tp9{position:absolute;left:50%;top:0;bottom:0;width:34px;margin-left:-17px;background:rgba(240,228,200,.75)}
.bx9 span{position:relative;font:700 18px/1.3 'Open Sans';color:#3b2a16;background:rgba(255,248,235,.85);border-radius:6px;padding:3px 8px}.bx9 em{position:relative;font:700 16px 'Open Sans';font-style:normal;color:#5a3d1e}
.fl{width:100%;height:12px;border-radius:6px;background:#cfd9d8;margin-top:2px}
.of{display:flex;flex-direction:column;padding:16px 20px;gap:8px;flex:1}
.of small{font:700 12px/1.4 'Open Sans';letter-spacing:2px;color:#6d8080}.of h3{font:800 23px/1.3 Montserrat}
.ir{display:grid;grid-template-columns:1fr 90px 70px;gap:8px;align-items:center;padding:13px 0;border-top:1px solid #e6eceb;font:600 17px/1.35 'Open Sans'}
.ir b{font:700 16px 'Open Sans';text-align:center;background:#eef3f2;border-radius:8px;padding:4px 0}.ir em{font-style:normal;color:#6d8080;font-size:15px;text-align:right}
.es{display:flex;justify-content:space-between;align-items:center;background:#1f3b3b;color:#fff;border-radius:12px;padding:10px 14px;font:600 16px 'Open Sans'}.es b{font:800 24px Montserrat;color:#7fe0d6}
.fd9{display:flex;justify-content:space-between;background:#f3f6f6;border-radius:12px;padding:9px 12px;font:500 15px 'Open Sans'}.fd9 b{font-weight:700}
.sl9{display:grid;grid-template-columns:repeat(3,1fr);gap:6px}.sl9 span{text-align:center;border:1.5px solid #cfd9d8;border-radius:10px;padding:7px 0;font:600 14px 'Open Sans'}.sl9 .on{background:#1d8a83;border-color:#1d8a83;color:#fff}
.bk9{margin-top:auto;background:#1d8a83;color:#fff;border-radius:12px;padding:12px;text-align:center;font:700 17px 'Open Sans'}
""", "<div class=kk>FURNITURE ASSEMBLY SERVICE</div><h1>“How long will it take?”<br><span>The booking page knows.</span></h1>",
f'''<div class=vw><div class=st9><small>THE CUSTOMER'S BOXES · SAMPLE</small><div class=tc9><b>7 boxes, 4 items</b><span>The page turns them into one time slot, so you send the right number of people and plan the day.</span></div>{"".join(box(n,q,w+130) for n,q,m,w in fp)}<div class=fl></div></div>
{browser(f"""<div class=of><small>BOOKING PAGE · SAMPLE</small><h3>What do we assemble?</h3>
{"".join(f'<div class=ir><span>{n}</span><b>{q} box{"es" if q>1 else ""}</b><em>{m} min</em></div>' for n,q,m,w in fp)}
<div class=es><span>Time estimate</span><b>{mins//60} h {mins%60} min</b></div>
<div class=fd9><span>Sample rule</span><b>Set minutes per item</b></div>
<div class=fd9><span>ZIP code</span><b>12345</b></div>
<div class=fd9><span>Floor</span><b>2nd, no elevator</b></div>
<div class=sl9>{"".join(f'<span class="{"on" if a=="Sat 8 AM" else ""}">{a}</span>' for a in ["Fri 1 PM","Sat 8 AM","Sat 2 PM"])}</div>
<div class=fd9><span>Take boxes away</span><b>Yes</b></div><div class=fd9><span>Name</span><b>Sample customer</b></div>
<div class=bk9>Book Sat 8 AM · 5 h 15 min</div></div>""", url="yourassembly.com/book", style="display:flex;flex-direction:column")}</div>''',
"#1f3b3b", "Assemble furniture? DM us", "background:#1f3b3b;color:#7fe0d6")

# ───────── 320 INDIA · Local broadband / fibre internet provider · CAROUSEL 5 · Gelasio + Roboto · fibre cyan / router black / signal green
# New technique: building cross-section (floors x flats) with a fibre riser and per-flat status dots; reused across slides.
BB = """
body{--f:'Roboto';--h:'Gelasio';background:#e8f4f6;color:#14262c}
.kk{font:700 16px/1.4 'Roboto';letter-spacing:3px;color:#0f8fa3;margin-top:22px;align-self:flex-start}
h1{font-family:'Gelasio';font-weight:700;font-size:64px;line-height:1.25;letter-spacing:-.5px} h1 span{color:#0f8fa3}
.cd{background:#fff;border-radius:22px;box-shadow:0 12px 28px rgba(20,38,44,.08)}
.cap{font:700 14px/1.4 'Roboto';letter-spacing:2px;color:#68808a}
.nb{display:flex;align-items:center;gap:14px;background:#14262c;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.45 'Roboto'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#3fd17f;color:#14262c}.nb b{color:#7fe8ad}
"""
def bb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#14262c;color:#fff"):
    return page(BB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#14262c", cta, ctacss, tagline=f"{n} / 5")
# status per flat: on, down, new, none
flats = {}
for f in range(5, 0, -1):
    for u in range(1, 5):
        flats[f"{f}0{u}"] = "on"
for k in ["504", "303", "102"]: flats[k] = "none"
flats["402"] = "down"; flats["201"] = "new"
def bldg(name="Tower B"):
    FC = {"on": "#3fd17f", "down": "#e5484d", "new": "#f2b705", "none": "#c9d6da"}
    rows = "".join(f'<div class=fr>{"".join(f"<div class=fl><i style=background:{FC[flats[f]]}></i><span>{f}</span></div>" for f in [f"{fl}0{u}" for u in (1,2)])}<div class=rs></div>{"".join(f"<div class=fl><i style=background:{FC[flats[f]]}></i><span>{f}</span></div>" for f in [f"{fl}0{u}" for u in (3,4)])}</div>' for fl in range(5, 0, -1))
    return f'<div class=bg><div class=rf>{name} · sample</div>{rows}<div class=gr><span>Fibre box</span></div></div>'
BG = """.bg{flex:1;min-height:0;display:flex;flex-direction:column;gap:6px;background:#d6e4e8;border-radius:16px;padding:12px}
.rf{text-align:center;font:700 18px/1.4 Gelasio;padding:4px;color:#14262c}
.fr{flex:1;display:grid;grid-template-columns:1fr 1fr 26px 1fr 1fr;gap:6px}.fl{background:#fff;border-radius:8px;display:flex;align-items:center;justify-content:center;gap:8px;box-shadow:inset 0 -4px 0 #e5eef0}
.fl i{width:20px;height:20px;border-radius:50%}.fl span{font:700 16px 'Roboto'}.rs{background:repeating-linear-gradient(#0f8fa3 0 10px,#7fd3df 10px 14px);border-radius:6px}
.gr{background:#14262c;color:#7fe8ad;border-radius:10px;padding:8px;text-align:center;font:700 15px 'Roboto'}.gr span{font:700 15px/1.4 'Roboto'}"""
LG = '<div class=lgx>' + "".join(f'<span><i style="background:{c}"></i>{a}</span>' for a, c in [("Working", "#3fd17f"), ("Down", "#e5484d"), ("New request", "#f2b705"), ("No connection", "#c9d6da")]) + '</div>'
LGC = ".lgx{display:flex;flex-wrap:wrap;gap:16px;font:600 16px/1.4 'Roboto'}.lgx span{display:flex;align-items:center;gap:8px}.lgx i{width:18px;height:18px;border-radius:50%}"
P["p320_fibre_s1"] = bb(1, "LOCAL BROADBAND · FIBRE IN BUILDINGS", "Wi-Fi down at 10 PM?<br><span>A ticket, not ten calls.</span>",
f'''<div class=w1><div class="cd b1">{bldg()}{LG}</div><div class=sd1>
<div class=bb1><span class=vn>{ic("phone",22)} Flat 402 · 10:04 PM</span><p>“Net is not working. Again.”</p></div>
<div class=bb1><span class=vn>{ic("phone",22)} Flat 402 · 10:09 PM</span><p>“Hello?? Office work is pending.”</p></div>
<div class=bb1><span class=vn>{ic("phone",22)} Flat 402 · 10:15 PM</span><p>“Calling again. Please pick up.”</p></div>
<div class="bb1 dk1"><p>Your phone at night, with 300 homes connected. <b>There is a better way.</b></p></div></div></div>''',
css=BG + LGC + """.w1{flex:1;display:grid;grid-template-columns:1.15fr 1fr;gap:14px;min-height:0}.b1{padding:16px;display:flex;flex-direction:column;gap:10px;min-height:0}
.sd1{display:flex;flex-direction:column;gap:12px}.bb1{flex:1;background:#fff;border-radius:22px 22px 22px 6px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;box-shadow:0 12px 28px rgba(20,38,44,.08)}
.vn{display:flex;align-items:center;gap:10px;font:700 15px 'Roboto';color:#e5484d;margin-bottom:6px}.bb1 p{font:500 22px/1.4 'Roboto'}.dk1{background:#14262c;color:#fff;border-radius:22px}.dk1 b{color:#7fe8ad}""")

tickets = [("T-881", "Tower B · 402", "No internet", "Tech R-2 · 9 AM", "o"), ("T-882", "Tower A · 105", "Slow speed", "Tech R-2 · 10 AM", "o"), ("T-883", "Row house 14", "Router light red", "Tech R-2 · 11 AM", "o"),
           ("T-879", "Tower C · 301", "Wire cut", "Fixed · 7:40 PM", "d"), ("T-880", "Tower B · 201", "New connection", "Fixed · 6:10 PM", "d")]
P["p320_fibre_s2"] = bb(2, "STEP 1 · CUSTOMERS RAISE A TICKET", "Every complaint<br><span>gets a number and a time.</span>",
f'''<div class=w2><div class="cd tk2">{"".join(f'<div class="tr2 {k}"><b>{t}</b><div><em>{w}</em><span>{p}</span></div><i>{a}</i></div>' for t,w,p,a,k in tickets)}</div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>The customer gets the ticket number and the visit time <b>in a message, right away.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.tk2{flex:1;padding:14px 24px;display:flex;flex-direction:column}
.tr2{flex:1;display:grid;grid-template-columns:120px 1fr 230px;gap:16px;align-items:center;border-bottom:1px solid #e3edef}.tr2:last-child{border:0}
.tr2 b{font:700 26px/1.3 Gelasio}.tr2 em{display:block;font:700 22px/1.35 'Roboto';font-style:normal}.tr2 div span{font:500 18px/1.4 'Roboto';color:#56707a}
.tr2 i{font:700 17px/1.3 'Roboto';font-style:normal;text-align:center;border-radius:12px;padding:10px 8px}.tr2.o i{background:#fff1c9;color:#8a6600}.tr2.d i{background:#dcf5e6;color:#1f7a47}""")

stops = [("9:00 AM", "Tower B · 402", "T-881 · no internet"), ("10:00 AM", "Tower A · 105", "T-882 · slow speed"), ("11:00 AM", "Row house 14", "T-883 · router light red"), ("12:30 PM", "Tower B · 201", "Router fit for the new connection"), ("2:00 PM", "Tower D", "Check the fibre box")]
P["p320_fibre_s3"] = bb(3, "STEP 2 · ONE ROUTE FOR EACH TECHNICIAN", "Tech R-2's day,<br><span>stop by stop.</span>",
f'''<div class=w3><div class="cd rt3">{"".join(f'<div class=sp3><span class=tm3>{t}</span><i class=dt3></i><div><b>{w}</b><span>{j}</span></div><em>{"Done" if n==0 else ("Next" if n==1 else "")}</em></div>' for n,(t,w,j) in enumerate(stops))}</div>
<div class=nb><span class=ib>{ic("map",26)}</span><span>The tech closes the ticket with a photo, <b>and the customer gets a message.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rt3{flex:1;padding:16px 26px;display:flex;flex-direction:column;position:relative}
.sp3{flex:1;display:grid;grid-template-columns:120px 40px 1fr 90px;gap:14px;align-items:center;position:relative}
.sp3::before{content:"";position:absolute;left:153px;top:0;bottom:0;width:4px;background:#bfe3ea}
.dt3{width:28px;height:28px;border-radius:50%;background:#fff;border:5px solid #0f8fa3;position:relative;z-index:1;justify-self:center}
.tm3{font:700 20px/1.3 'Roboto';color:#0f8fa3}.sp3 b{display:block;font:700 26px/1.3 Gelasio}.sp3 div span{font:500 18px/1.4 'Roboto';color:#56707a}
.sp3 em{font:700 15px 'Roboto';font-style:normal;text-align:center;border-radius:10px;padding:6px 0}.sp3:first-child em{background:#dcf5e6;color:#1f7a47}.sp3:nth-child(2) em{background:#fff1c9;color:#8a6600}""")

ren = [("Tower A · 203", "Tue 24 Nov", "Reminder sent", "s"), ("Tower B · 501", "Wed 25 Nov", "Renewed", "r"), ("Tower C · 104", "Thu 26 Nov", "Reminder on Tue", "w"), ("Row house 9", "Fri 27 Nov", "Renewed", "r"), ("Tower D · 302", "Sat 28 Nov", "Reminder on Thu", "w"), ("Tower A · 401", "Sun 29 Nov", "Reminder on Fri", "w")]
nr = sum(1 for r in ren if r[3] == "r")
P["p320_fibre_s4"] = bb(4, "STEP 3 · RENEWALS DUE THIS WEEK", "Plan ends on Friday?<br><span>They hear on Wednesday.</span>",
f'''<div class=w4><div class="cd rn4"><div class=hd4><small class=cap>RENEWALS · THIS WEEK · SAMPLE</small><em>{nr} of {len(ren)} renewed</em></div>{"".join(f'<div class="rr4 {k}"><b>{a}</b><span>Ends {d}</span><i>{s}</i></div>' for a,d,s,k in ren)}</div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>A reminder goes 2 days before the plan ends, <b>with a link to renew.</b></span></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.rn4{flex:1;padding:16px 26px;display:flex;flex-direction:column}
.hd4{display:flex;justify-content:space-between;align-items:center;padding-bottom:10px;border-bottom:2px solid #14262c}.hd4 em{font:700 20px 'Roboto';font-style:normal;color:#1f7a47}
.rr4{flex:1;display:grid;grid-template-columns:1.2fr 1fr 220px;gap:14px;align-items:center;border-bottom:1px solid #e3edef}.rr4:last-child{border:0}
.rr4 b{font:700 25px/1.3 Gelasio}.rr4 span{font:500 19px 'Roboto';color:#56707a}.rr4 i{font:700 16px/1.3 'Roboto';font-style:normal;text-align:center;border-radius:12px;padding:9px 6px}
.rr4.r i{background:#dcf5e6;color:#1f7a47}.rr4.s i{background:#fff1c9;color:#8a6600}.rr4.w i{background:#eef3f5;color:#56707a}""")

P["p320_fibre_s5"] = bb(5, "YOUR TURN", "Run a local internet business?<br><span>Let's build your ticket app.</span>",
f'''<div class=w5><div class="cd b5">{bldg()}</div><div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,34)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("bell","Tickets","Number and visit time"),("map","Tech routes","Stop by stop"),("cal","Renewals","Reminders that go out"),("grid","Building view","Every flat at a glance")])}</div>
<div class=q>How do customers tell you the net is down today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#0f8fa3;color:#fff",
css=BG + """.w5{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.b5{padding:14px;display:flex;min-height:0}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(20,38,44,.07)}
.ti .ib{width:62px;height:62px;border-radius:18px;background:#d7f2f5;color:#0f8fa3}.ti b{display:block;font:700 26px/1.3 Gelasio}.ti div span{font:500 17px/1.4 'Roboto';color:#56707a}
.q{background:#14262c;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'Roboto'}""")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
