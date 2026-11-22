import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 72 INDIA · Modular kitchen maker · CAROUSEL 6 · Montserrat + Roboto · blueprint navy / graph white / marker yellow
# New technique: blueprint floor plan with dimension lines, drawn with absolute divs on a grid.
KC = """
body{--f:'Roboto';--h:'Montserrat';background:#f3f6fb;background-image:linear-gradient(#dde6f2 1px,transparent 1px),linear-gradient(90deg,#dde6f2 1px,transparent 1px);background-size:36px 36px;color:#0f2a4d}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.4px} h1 span{color:#1b5fb0}
.sub{color:#4c6380}
.st{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 17px Montserrat;letter-spacing:3px;color:#1b5fb0}
.st b{width:46px;height:46px;border-radius:12px;background:#ffd23f;color:#0f2a4d;font:800 22px/46px Montserrat;text-align:center;letter-spacing:0}
.bp{background:#123a6b;background-image:linear-gradient(rgba(255,255,255,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.07) 1px,transparent 1px);background-size:30px 30px;border-radius:30px;color:#fff}
.wc{background:#fff;border-radius:28px;box-shadow:0 18px 40px rgba(15,42,77,.08)}
.lbl{font:700 14px Roboto;letter-spacing:3px;color:#7d90a8}
"""
def kc(n, head, vis, css="", cta="Swipe", ctacss="background:#123a6b;color:#fff"):
    return page(KC + css, head, vis, "#0f2a4d", cta, ctacss, tagline=f"{n} / 6")

def ab(l, t, w, h, extra="", inner="", cls="ab"):
    return f'<div class="{cls}" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;{extra}">{inner}</div>'

plan = (
  ab(90, 2, 640, 36, "background:linear-gradient(#ffd23f,#ffd23f) 0 50%/100% 2px no-repeat", f'<span class=dm style="left:110px;top:0">10 ft</span>')
  + ab(2, 70, 70, 450, "background:linear-gradient(#ffd23f,#ffd23f) 50% 0/2px 100% no-repeat", f'<span class=dm style="left:0;width:70px;padding:0;text-align:center;top:200px">8 ft</span>')
  + ab(80, 56, 660, 14, "background:#fff")
  + ab(80, 56, 14, 464, "background:#fff")
  + ab(330, 56, 230, 14, "background:#123a6b;border-top:2px solid #fff;border-bottom:2px solid #fff")
  + ab(94, 70, 546, 120, "border:2px solid #9cc0ee;background:repeating-linear-gradient(90deg,transparent 0 89px,#9cc0ee 89px 91px)")
  + ab(94, 190, 120, 330, "border:2px solid #9cc0ee;border-top:none;background:repeating-linear-gradient(0deg,transparent 0 80px,#9cc0ee 80px 82px)")
  + ab(360, 84, 170, 88, "border:3px solid #fff;border-radius:14px;background:#123a6b", '<i class=sk1></i>')
  + ab(112, 300, 84, 140, "border:3px solid #fff;border-radius:10px;background:#123a6b", '<i class=hb></i><i class=hb></i><i class=hb></i><i class=hb></i>')
  + ab(652, 70, 88, 120, "border:3px dashed #ffd23f;border-radius:6px", '<span class=fz>Fridge</span>')
)
P["p72_kitchen_s1"] = kc(1, """<h1 style="margin-top:34px">Measure today,<br>quote next week?<br><span>Quote on the same visit.</span></h1>""",
f'''<div class=bp style="flex:1;display:flex;align-items:center;justify-content:center;position:relative;padding:24px">
<div class=pl>{plan}<span class="tg" style="left:400px;top:180px">Sink</span><span class="tg" style="left:220px;top:358px">Hob</span><span class="tg" style="left:400px;top:33px">Window</span></div>
<div class=nt1><small>SAMPLE SITE · FLAT 304</small><b>L-shape kitchen</b><span>Measured, planned and quoted before you leave.</span></div></div>''',
""".pl{position:relative;width:760px;height:540px;zoom:1.18;margin:-30px 0 0 -40px}
.ab{position:absolute;display:block}
.dm{position:absolute;font:700 22px/36px Montserrat;color:#ffd23f;background:#123a6b;padding:0 10px;white-space:nowrap}
.sk1{position:absolute;left:58px;top:20px;width:42px;height:42px;border-radius:50%;border:3px solid #fff}
.hb{display:block;width:26px;height:26px;border-radius:50%;border:3px solid #fff;margin:10px 0 0 10px;float:left}
.hb:nth-child(2n){margin-left:12px}
.fz{position:absolute;left:0;right:0;top:44px;text-align:center;font:700 16px Roboto;color:#ffd23f}
.tg{position:absolute;font:700 18px Roboto;color:#ffd23f;white-space:nowrap}
.nt1{position:absolute;right:30px;bottom:30px;width:330px;background:#ffd23f;color:#0f2a4d;border-radius:20px;padding:20px 22px;display:flex;flex-direction:column;gap:6px}
.nt1 small{font:700 13px Roboto;letter-spacing:3px}.nt1 b{font:800 28px Montserrat}.nt1 span{font:500 19px/1.4 Roboto}
""")

fields = [("WALL A","10 ft"),("WALL B","8 ft"),("CEILING HEIGHT","9 ft 6 in"),("WINDOW","Wall A, 3 ft from left"),("SINK POINT","Wall A, centre"),("GAS POINT","Wall B, 4 ft from corner")]
P["p72_kitchen_s2"] = kc(2, """<div class=st><b>1</b>MEASURE</div><h1 style="margin-top:14px">Wall sizes go straight<br><span>into the app.</span></h1>""",
f'''<div class="wc fm2"><div class=hd2><b>Site measurement</b><span class=lbl>FLAT 304 · SAMPLE</span></div>
<div class=gd2>{"".join(f'<div class=fd2><span class=lbl>{a}</span><b>{v}</b></div>' for a,v in fields)}</div>
<div class=lbl>SITE PHOTOS</div><div class=ph2><i></i><i></i><i></i><i class=ad>+</i></div>
<div class=bt2>Save and pick a layout</div></div>''',
""".vis{flex-direction:column}
.fm2{flex:1;padding:28px;display:flex;flex-direction:column;gap:16px}
.hd2{display:flex;justify-content:space-between;align-items:center}.hd2 b{font:800 32px Montserrat}
.gd2{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.fd2{border:2px solid #d5e0ee;border-radius:18px;padding:16px 18px;display:flex;flex-direction:column;justify-content:center;gap:8px;background:#f8fafd}
.fd2 b{font:700 34px/1.3 Roboto}.fd2 .lbl{font-size:16px}
.ph2{display:flex;gap:12px}.ph2 i{flex:1;height:110px;border-radius:14px;display:block;background:linear-gradient(160deg,#cfdcec 0 55%,#b9cbe2 55% 100%)}
.ph2 i.ad{background:#fff;border:2px dashed #9cb3d1;font:700 40px/106px Montserrat;font-style:normal;color:#7d90a8;text-align:center}
.bt2{background:#123a6b;color:#ffd23f;border-radius:16px;padding:17px;text-align:center;font:700 22px Montserrat}
""")

def mini(kind):
    bars = {"str": [(24,24,300,44)], "L": [(24,24,300,44),(24,68,44,120)], "U": [(24,24,300,44),(24,68,44,120),(280,68,44,120)], "par": [(24,24,300,44),(24,144,300,44)]}[kind]
    return '<div class=mp>' + "".join(f'<i style="left:{a}px;top:{b}px;width:{c}px;height:{d}px"></i>' for a,b,c,d in bars) + '</div>'
lays = [("str","Straight","Fits, but less storage","",""),("L","L-shape","Best fit for 10 x 8 ft walls","on","Fits"),("U","U-shape","Needs a third wall","",""),("par","Parallel","Needs two facing walls","","")]
P["p72_kitchen_s3"] = kc(3, """<div class=st><b>2</b>LAYOUT</div><h1 style="margin-top:14px">Show the client<br><span>the shape that fits.</span></h1>""",
f'''<div class=lg3>{"".join(f'<div class="wc ly {o}">{mini(k)}<b>{t}</b><span>{d}</span>{f"<em>{e}</em>" if e else ""}</div>' for k,t,d,o,e in lays)}</div>''',
""".vis{flex-direction:column}
.lg3{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.ly{padding:24px;display:flex;flex-direction:column;justify-content:center;gap:8px;position:relative;border:3px solid transparent}
.ly.on{border-color:#1b5fb0;background:#eef4fd}
.mp{position:relative;width:348px;height:212px;background:#123a6b;border-radius:16px;margin-bottom:10px}
.mp i{position:absolute;display:block;background:#9cc0ee;border-radius:4px}
.ly.on .mp i{background:#ffd23f}
.ly b{font:800 36px Montserrat}.ly span{font:500 24px/1.35 Roboto;color:#4c6380}
.ly em{position:absolute;right:22px;top:22px;font-style:normal;font:700 17px Roboto;background:#1b5fb0;color:#fff;padding:7px 14px;border-radius:10px}
""")

fin = [("SHUTTERS", [("Matte laminate","#c9cfd6",0),("Acrylic gloss","linear-gradient(135deg,#1b5fb0,#5d97dc 60%,#1b5fb0)",1),("PU finish","#e8e2d6",0)]),
       ("COUNTER TOP", [("Black granite","radial-gradient(circle at 30% 40%,#777 0 2px,transparent 3px) 0 0/14px 14px,#222",1),("Quartz","radial-gradient(circle at 60% 60%,#ddd 0 2px,transparent 3px) 0 0/12px 12px,#f4f4f2",0),("Solid surface","#efeae0",0)]),
       ("HANDLES", [("Profile","linear-gradient(#bfc6cf 0 20%,#fff 20%)",1),("Knob","radial-gradient(circle,#9aa3ad 0 30%,#fff 32%)",0),("Handle-less","linear-gradient(#fff 0 80%,#c9cfd6 80%)",0)])]
P["p72_kitchen_s4"] = kc(4, """<div class=st><b>3</b>FINISH</div><h1 style="margin-top:14px">Shutters, counter top, handles:<br><span>picked on the spot.</span></h1>""",
f'''<div class=fs4>{"".join(f'<div class="wc rw4"><div class=lbl>{t}</div><div class=op4>' + "".join(f'<div class="o4 {"on" if s else ""}"><i style="background:{bg}"></i><b>{n}</b></div>' for n,bg,s in ops) + '</div></div>' for t,ops in fin)}</div>''',
""".vis{flex-direction:column}
.fs4{flex:1;display:flex;flex-direction:column;gap:16px}
.rw4{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:12px}
.op4{flex:1;display:flex;gap:14px}
.o4{flex:1;border:3px solid #dbe4f0;border-radius:18px;padding:12px;display:flex;flex-direction:column;gap:10px;align-items:stretch}
.o4 i{flex:1;display:block;border-radius:12px;border:1px solid #d5dde8;min-height:70px}
.o4 b{font:700 23px Roboto;text-align:center}
.o4.on{border-color:#1b5fb0;background:#eef4fd}.o4.on b{color:#1b5fb0}
""")

qrows = [("Base units","14 running ft"),("Wall units","10 running ft"),("Tall unit","1 (2 ft wide)"),("Shutters","Acrylic gloss"),("Counter top","Black granite, 14 ft"),("Hardware","Soft-close hinges and channels")]
P["p72_kitchen_s5"] = kc(5, """<div class=st><b>4</b>QUOTE</div><h1 style="margin-top:14px">A clear quote<br><span>before you leave the site.</span></h1>""",
f'''<div class=dc5><div class=hd5><div><b>Quotation</b><span>Flat 304 · L-shape kitchen</span></div><em>SAMPLE</em></div>
<div class=th5><span>ITEM</span><span>SIZE / DETAIL</span></div>
{"".join(f'<div class=tr5><b>{a}</b><span>{v}</span></div>' for a,v in qrows)}
<div class=ft5><div class=rt5>Totals worked out from your own rate list</div><div class=bn5><span>Send to client</span><span class=ap5>Client approves on the link</span></div></div></div>''',
""".vis{flex-direction:column}
.dc5{flex:1;background:#fff;border-radius:8px;padding:30px 34px;display:flex;flex-direction:column;box-shadow:0 22px 50px rgba(15,42,77,.14);border-top:10px solid #123a6b}
.hd5{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:14px}
.hd5 b{display:block;font:800 36px Montserrat}.hd5 span{font:500 20px Roboto;color:#4c6380}
.hd5 em{font-style:normal;font:700 15px Roboto;letter-spacing:3px;border:2px solid #1b5fb0;color:#1b5fb0;padding:6px 12px;border-radius:8px}
.th5{display:flex;justify-content:space-between;font:700 14px Roboto;letter-spacing:3px;color:#7d90a8;border-bottom:2px solid #123a6b;padding:8px 0}
.tr5{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1.5px dashed #cfdbea}
.tr5 b{font:700 26px Roboto}.tr5 span{font:500 25px Roboto;color:#33496a}
.ft5{display:flex;flex-direction:column;gap:12px;margin-top:16px}
.rt5{background:#fff7d6;border-radius:12px;padding:12px 16px;font:600 19px Roboto;color:#6b5600}
.bn5{display:flex;gap:12px}.bn5 span{flex:1;text-align:center;border-radius:14px;padding:15px;font:700 20px Montserrat;background:#e6eef9;color:#123a6b}
.bn5 .ap5{background:#123a6b;color:#ffd23f}
""")

P["p72_kitchen_s6"] = kc(6, """<h1 style="margin-top:34px">Want a measure-to-quote app<br><span>for your kitchen business?</span></h1><div class=sub>We build site apps for modular kitchen and wardrobe makers.</div>""",
f'''<div class=w6>{peep("Device","Smile","ShortCurly","None",w=380,h=620)}<div class=o6>{"".join(f'<div class="wc q6"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Site measurement form"),(2,"Layout that fits"),(3,"Finish picker"),(4,"Quote the client approves")])}</div></div>''',
""".w6{flex:1;display:flex;align-items:flex-end;gap:18px}
.o6{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q6{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q6 span{width:62px;height:62px;border-radius:14px;background:#ffd23f;color:#0f2a4d;font:800 27px/62px Montserrat;text-align:center;flex:none}
.q6 b{font:800 27px/1.3 Montserrat}
""", cta="Make kitchens? DM us", ctacss="background:#123a6b;color:#ffd23f")

# ───────── 74 USA · Pest control · CAROUSEL 5 · TeX Gyre Adventor + Source Sans 3 · deep teal / goldenrod / cloud white
# New technique: top-down house plan with numbered perimeter stations + year-long visit dot board.
PC = """
body{--f:'Source Sans 3';--h:'TeX Gyre Adventor';background:#f4f6f2;color:#0e3a3d}
h1{font-family:'TeX Gyre Adventor';font-size:58px;font-weight:700;letter-spacing:-1px} h1 span{color:#c4860c}
.sub{color:#4f6a6b}
.sp{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 18px 'Source Sans 3';letter-spacing:3px;color:#0e4b4f}
.sp b{width:46px;height:46px;border-radius:50%;background:#0e4b4f;color:#e0a526;font:700 22px/46px 'TeX Gyre Adventor';text-align:center;letter-spacing:0}
.cw{background:#fff;border-radius:28px;box-shadow:0 16px 36px rgba(14,58,61,.08)}
.lb{font:700 14px 'Source Sans 3';letter-spacing:3px;color:#7b9091}
"""
def pc(n, head, vis, css="", cta="Swipe", ctacss="background:#0e4b4f;color:#fff"):
    return page(PC + css, head, vis, "#0e3a3d", cta, ctacss, tagline=f"{n} / 5")

stations = [(70,40),(330,40),(590,40),(660,200),(660,380),(420,440),(160,440),(10,250)]
P["p74_pest_s1"] = pc(1, """<h1 style="margin-top:34px">Quarterly visits<br>on a paper list?<br><span>Let the app plan them.</span></h1>""",
f'''<div class=yd1><div class=hs>
<div class=hm><div class=rm style="left:0;top:0;width:250px;height:170px">Garage</div><div class=rm style="left:250px;top:0;width:284px;height:170px">Kitchen</div><div class=rm style="left:0;top:170px;width:534px;height:154px">Living room</div></div>
{"".join(f'<span class=sn style="left:{x}px;top:{y}px">{i}</span>' for i,(x,y) in enumerate(stations,1))}</div>
<div class=nx1><small>12 MAPLE ST · SAMPLE</small><b>Next visit: Thu, Mar 11</b><span>8 stations · quarterly plan</span></div></div>''',
""".yd1{flex:1;background:#7fb069;background-image:radial-gradient(circle,#8dbb77 2px,transparent 3px);background-size:26px 26px;border-radius:30px;position:relative;display:flex;align-items:flex-start;justify-content:center;padding-top:24px}
.hs{position:relative;width:720px;height:500px;zoom:1.22}
.hm{position:absolute;left:80px;top:80px;width:550px;height:340px;background:#f4f6f2;border:8px solid #0e3a3d;border-radius:6px}
.rm{position:absolute;border:3px solid #9bb0b0;display:flex;align-items:center;justify-content:center;font:700 24px 'TeX Gyre Adventor';color:#4f6a6b}
.sn{position:absolute;width:52px;height:52px;border-radius:10px;background:#e0a526;border:4px solid #0e3a3d;color:#0e3a3d;font:700 22px/44px 'TeX Gyre Adventor';text-align:center}
.nx1{position:absolute;left:30px;right:30px;bottom:26px;background:#0e4b4f;color:#fff;border-radius:22px;padding:18px 24px;display:grid;grid-template-columns:1fr auto;align-items:center;column-gap:16px}
.nx1 small{grid-column:1/3;font:700 14px 'Source Sans 3';letter-spacing:3px;color:#9cc7c6}
.nx1 b{font:700 30px/1.3 'TeX Gyre Adventor'}.nx1 span{font:600 20px 'Source Sans 3';color:#e0a526}
""")

months = "JFMAMJJASOND"
cust = [("12 Maple St",[2,5,8,11],1),("48 Oak Ave",[1,4,7,10],2),("7 Pine Ct",[2,5,8,11],2),("90 Cedar Rd",[0,3,6,9],1),("33 Birch Ln",[1,4,7,10],2)]
def dot(m, ms, done_upto):
    if m not in ms: return '<i></i>'
    return '<i class=dn></i>' if m <= done_upto else '<i class=up></i>'
P["p74_pest_s2"] = pc(2, """<div class=sp><b>1</b>SCHEDULE</div><h1 style="margin-top:14px">Every visit booked<br><span>for the whole year.</span></h1>""",
f'''<div class="cw yb"><div class=yh><b>Quarterly customers</b><span class=lb>SAMPLE YEAR</span></div>
<div class=yrw><span></span>{"".join(f'<em>{m}</em>' for m in months)}</div>
{"".join(f'<div class=yrw><span>{n}</span>' + "".join(dot(m,ms,1) for m in range(12)) + '</div>' for n,ms,_ in cust)}
<div class=lgd><span><i class=dn></i>Done</span><span><i class=up></i>Booked</span><span class=nt2>New customer? Pick a plan and all 4 visits are booked.</span></div></div>''',
""".vis{flex-direction:column}
.yb{flex:1;padding:26px 28px;display:flex;flex-direction:column;gap:6px}
.yh{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}.yh b{font:700 30px 'TeX Gyre Adventor'}
.yrw{flex:1;display:grid;grid-template-columns:190px repeat(12,1fr);align-items:center;border-bottom:1.5px solid #e6ecea}
.yrw:nth-child(2){flex:none;border:none;padding-bottom:6px}
.yrw span{font:700 25px 'Source Sans 3'}
.yrw em{font-style:normal;text-align:center;font:700 21px 'Source Sans 3';color:#7b9091}
.yrw i{justify-self:center;width:38px;height:38px;border-radius:50%;display:block}
i.dn{background:#0e4b4f}i.up{background:#fff;border:4px solid #e0a526}
.lgd{display:flex;gap:22px;align-items:center;margin-top:12px;font:600 19px 'Source Sans 3'}
.lgd span{display:flex;align-items:center;gap:8px}.lgd i{width:22px;height:22px;border-radius:50%;display:block}
.lgd .nt2{flex:1;justify-content:flex-end;text-align:right;color:#4f6a6b}
""")

P["p74_pest_s3"] = pc(3, """<div class=sp><b>2</b>REMINDERS</div><h1 style="margin-top:14px">Customers get a text<br><span>before you show up.</span></h1>""",
f'''<div class=rm3><div class=bl3><div class=lb>AUTOMATIC TEXT · SAMPLE</div>
<div class=bu3>Hi, this is Your Pest Co. Your quarterly service is on <b>Thu, Mar&nbsp;11, 9 to 11&nbsp;am.</b> Reply 1 to confirm or 2 to pick another day.</div>
<div class="bu3 me">1</div><div class=bu3>Thanks! See you on Thursday.</div><div class=dy3>THE DAY BEFORE</div><div class=bu3>Reminder: we come tomorrow, 9 to 11 am. Please keep pets inside.</div></div>
<div class="cw cf3"><div class=lb>THIS WEEK'S REPLIES</div>{"".join(f'<div class=rr3><b>{a}</b><em class={c}>{s}</em></div>' for a,s,c in [("12 Maple St","Confirmed","ok"),("61 Elm Dr","Confirmed","ok"),("7 Pine Ct","Moved to Fri","mv"),("15 Ash Way","No reply yet","wt")])}</div></div>''',
""".vis{gap:18px}
.rm3{flex:1;display:flex;gap:18px}
.bl3{flex:1.25;background:#0e4b4f;border-radius:28px;padding:26px;display:flex;flex-direction:column;gap:16px;justify-content:center}
.dy3{align-self:center;font:700 15px 'Source Sans 3';letter-spacing:3px;color:#9cc7c6}
.bl3 .lb{color:#9cc7c6}
.bu3{background:#f4f6f2;color:#0e3a3d;border-radius:22px 22px 22px 6px;padding:18px 20px;font:500 27px/1.42 'Source Sans 3';max-width:94%}
.bu3 b{font-weight:700}
.bu3.me{align-self:flex-end;background:#e0a526;border-radius:22px 22px 6px 22px;font:700 28px 'TeX Gyre Adventor';padding:12px 28px}
.cf3{flex:1;padding:24px;display:flex;flex-direction:column;gap:12px}
.rr3{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-bottom:1.5px solid #e6ecea}
.rr3:last-child{border:none}
.rr3 b{font:700 28px 'Source Sans 3'}
.rr3 em{align-self:flex-start;font-style:normal;font:700 20px 'Source Sans 3';padding:6px 12px;border-radius:9px}
.ok{background:#dcefe2;color:#1d6b3b}.mv{background:#fbeecb;color:#8a5d00}.wt{background:#eceff0;color:#5b6b6c}
""")

areas = [("Outside perimeter",1),("Garage",1),("Kitchen",1),("Attic",0)]
P["p74_pest_s4"] = pc(4, """<div class=sp><b>3</b>REPORT</div><h1 style="margin-top:14px">The tech fills the report<br><span>right at the house.</span></h1>""",
f'''<div class=rp4><div class=rh4><div><b>Service report</b><span>12 Maple St · Thu, Mar 11</span></div><em>SAMPLE</em></div>
<div class=cl4><div class=bx4><div class=lb>AREAS SERVICED</div>{"".join(f'<div class=ck4><i class="{"y" if v else ""}">{"✓" if v else ""}</i>{a}</div>' for a,v in areas)}</div>
<div class=bx4><div class=lb>STATIONS CHECKED</div><div class=big4>8 of 8</div><div class=lb>ACTIVITY SEEN</div><div class=tg4><span>Station 3</span><span>Station 5</span></div><div class=lb style="margin-top:auto">NEXT VISIT</div><div class=nv4>Thu, Jun 10</div></div></div>
<div class=bx4 style="flex:none"><div class=lb>NOTES</div><div class=nt4>Sealed a gap under the garage door. Customer asked us to check the attic next time.</div></div>
<div class=pr4><div class=ph4><i></i><i></i><i></i></div><div class=sg4>Report emailed to the customer</div></div></div>''',
""".vis{flex-direction:column}
.rp4{flex:1;background:#fff;border-radius:10px;padding:28px 30px;display:flex;flex-direction:column;gap:16px;box-shadow:0 22px 50px rgba(14,58,61,.14);border-left:12px solid #e0a526}
.rh4{display:flex;justify-content:space-between;align-items:flex-start}.rh4 b{display:block;font:700 34px 'TeX Gyre Adventor'}.rh4 span{font:600 20px 'Source Sans 3';color:#4f6a6b}
.rh4 em{font-style:normal;font:700 15px 'Source Sans 3';letter-spacing:3px;color:#0e4b4f;border:2px solid #0e4b4f;padding:6px 12px;border-radius:8px}
.cl4{flex:1;display:flex;gap:16px}
.bx4{flex:1;background:#f4f6f2;border-radius:18px;padding:18px 20px;display:flex;flex-direction:column;gap:10px}
.ck4{flex:1;display:flex;align-items:center;gap:14px;font:600 27px 'Source Sans 3'}
.ck4 i{width:38px;height:38px;border-radius:9px;border:3px solid #9bb0b0;font:800 24px/32px 'Source Sans 3';font-style:normal;text-align:center;color:#fff;flex:none}
.ck4 i.y{background:#0e4b4f;border-color:#0e4b4f}
.big4{font:700 64px/1.3 'TeX Gyre Adventor';color:#0e4b4f;margin-bottom:6px}
.tg4{display:flex;gap:10px}.tg4 span{font:700 22px 'Source Sans 3';background:#fbeecb;color:#8a5d00;padding:7px 12px;border-radius:10px}
.nv4{font:700 30px 'TeX Gyre Adventor';color:#c4860c}
.nt4{font:500 25px/1.45 'Source Sans 3'}
.pr4{display:flex;gap:16px;align-items:stretch}
.ph4{display:flex;gap:10px}.ph4 i{width:120px;height:100px;border-radius:12px;display:block;background:linear-gradient(160deg,#c9d6d2 0 50%,#aebfba 50%)}
.sg4{flex:1;background:#0e4b4f;color:#fff;border-radius:16px;display:flex;align-items:center;justify-content:center;font:700 23px 'TeX Gyre Adventor'}
""")

P["p74_pest_s5"] = pc(5, """<h1 style="margin-top:34px">Want an app that runs<br><span>your recurring visits?</span></h1><div class=sub>We build scheduling and service report apps for pest control companies.</div>""",
f'''<div class=w5>{peep("PointingUp","Smile","ShortVolumed","Chin",w=380,h=620)}<div class=o5>{"".join(f'<div class="cw q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Visits booked for the year"),(2,"Reminder texts"),(3,"Service reports on site"),(4,"Your route for the day")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:62px;height:62px;border-radius:50%;background:#e0a526;color:#0e3a3d;font:700 27px/62px 'TeX Gyre Adventor';text-align:center;flex:none}
.q5 b{font:700 27px/1.3 'TeX Gyre Adventor'}
""", cta="Run a pest control company? DM us", ctacss="background:#0e4b4f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
