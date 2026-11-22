import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 76 INDIA · Civil contractor · CAROUSEL 6 · Anton + Inter · asphalt / hi-vis orange / site sand
# New technique: CSS building under construction (slabs, columns, scaffold pipes) with stage tags per floor.
CV = """
body{--f:'Inter';--h:'Anton';background:#efe6d6;color:#1f2328}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#e8620c}
.sub{color:#5d5a52}
.kk{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:800 17px Inter;letter-spacing:3px;color:#1f2328}
.kk b{background:#ff7a1a;color:#1f2328;font:400 24px/46px Anton;width:46px;height:46px;text-align:center;border-radius:6px;letter-spacing:0}
.cd{background:#fff;border-radius:24px;box-shadow:0 16px 36px rgba(31,35,40,.08)}
.lbl{font:800 14px Inter;letter-spacing:3px;color:#8d877a}
.hz{height:16px;background:repeating-linear-gradient(-45deg,#ff7a1a 0 16px,#1f2328 16px 32px);border-radius:4px;flex:none}
"""
def cv(n, head, vis, css="", cta="Swipe", ctacss="background:#1f2328;color:#ff7a1a"):
    return page(CV + css, head, vis, "#1f2328", cta, ctacss, tagline=f"{n} / 6")

floors = [("Slab 3","Shuttering","nw"),("Floor 2","Brickwork","ip"),("Floor 1","Plaster","pl"),("Ground","Done","dn")]
P["p76_civil_s1"] = cv(1, """<h1>Running 3 sites<br>from one diary?<br><span>See every site in one app.</span></h1>""",
f'''<div class=sky><div class=bld>
<div class=top>{"".join('<i></i>' for _ in range(5))}</div>
{"".join(f'<div class="fl {k}"><span class=wl></span></div>' for _,_,k in floors[1:])}
<div class=scf></div></div>
<div class=tags>{"".join(f'<div class="tg {k}"><b>{a}</b><span>{b}</span></div>' for a,b,k in floors)}</div>
<div class=gd></div><div class=st1>SITE A · G+2 · SAMPLE</div></div>''',
""".sky{flex:1;background:linear-gradient(#cfe3ee,#e9f2f6);border-radius:30px;position:relative;display:flex;align-items:flex-end;padding:0 40px 60px;gap:40px;overflow:hidden}
.gd{position:absolute;left:0;right:0;bottom:0;height:60px;background:#c9a978}
.st1{position:absolute;left:30px;top:26px;font:800 15px Inter;letter-spacing:3px;color:#46606e}
.bld{width:500px;flex:none;position:relative;display:flex;flex-direction:column;z-index:2}
.top{height:150px;display:flex;justify-content:space-between;padding:0 14px;border-bottom:18px solid #9aa0a6;background:repeating-linear-gradient(90deg,transparent 0 40px,rgba(232,98,12,.18) 40px 44px)}
.top i{width:26px;background:#8a9096;display:block}
.fl{height:150px;border-bottom:18px solid #9aa0a6;display:flex;padding:0 14px;background:#b7bcc1;position:relative}
.fl.ip{background:repeating-linear-gradient(0deg,#c0583a 0 16px,#e6dccb 16px 18px),#c0583a;background-size:46px 18px}
.fl.dn{background:#eee6d6}.fl.pl{background:linear-gradient(90deg,#d9d2c4 0 55%,#c0583a 55%);background-size:100% 100%}
.pl span{background:#e6dccb;color:#1f2328}
.fl .wl{position:absolute;left:150px;top:40px;width:120px;height:70px;background:#5b7f93;border:6px solid #e6dccb}
.fl.ip .wl{background:#1f2328;border-color:#8a9096}
.scf{position:absolute;right:-30px;top:20px;bottom:0;width:40px;background:linear-gradient(90deg,#3a3f44 0 5px,transparent 5px 35px,#3a3f44 35px),repeating-linear-gradient(0deg,#3a3f44 0 5px,transparent 5px 60px)}
.tags{flex:1;display:flex;flex-direction:column;gap:0;z-index:2;align-self:stretch;justify-content:flex-end}
.tg{height:168px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-left:6px solid #1f2328;padding-left:20px}
.tg b{font:400 40px/1.3 Anton}.tg span{align-self:flex-start;font:800 21px Inter;padding:6px 12px;border-radius:8px}
.nw span{background:#ff7a1a;color:#1f2328}.ip span{background:#1f2328;color:#fff}.dn span{background:#2f7d4f;color:#fff}
""")

lab = [("Mason",6,4,3),("Helper",10,7,5),("Carpenter",3,0,2),("Bar bender",2,2,0)]
tot = [sum(r[i] for r in lab) for i in (1,2,3)]
P["p76_civil_s2"] = cv(2, """<div class=kk><b>1</b>LABOUR</div><h1 style="margin-top:14px">Who came to which site,<br><span>every single day.</span></h1>""",
f'''<div class="cd tb2"><div class=hd2><b>Today's attendance</b><span class=lbl>SAMPLE</span></div>
<div class="rw2 th"><span></span><span>Site A</span><span>Site B</span><span>Site C</span></div>
{"".join(f'<div class=rw2><span>{n}</span><b>{a}</b><b>{b}</b><b>{c}</b></div>' for n,a,b,c in lab)}
<div class="rw2 tt"><span>Total</span>{"".join(f'<b>{t}</b>' for t in tot)}</div>
<div class=nt2>{ic("camera",26)}Each supervisor marks attendance with a group photo from the site.</div></div>''',
""".vis{flex-direction:column}
.tb2{flex:1;padding:28px;display:flex;flex-direction:column}
.hd2{display:flex;justify-content:space-between;align-items:center;margin-bottom:10px}.hd2 b{font:400 34px/1.3 Anton}
.rw2{flex:1;display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;align-items:center;border-bottom:2px solid #eee6d6}
.rw2 span{font:700 26px Inter}.rw2 b{font:400 40px/1.3 Anton;text-align:center}
.rw2.th{flex:none;padding:8px 0}.rw2.th span{font:800 17px Inter;letter-spacing:2px;color:#8d877a;text-align:center}.rw2.th span:first-child{text-align:left}
.rw2.tt{background:#1f2328;color:#fff;border-radius:16px;padding:0 18px;margin:12px -10px 0;border:none}.rw2.tt b{color:#ff7a1a}
.nt2{display:flex;align-items:center;gap:12px;margin-top:16px;background:#fff3e8;border-radius:14px;padding:14px 16px;font:600 20px Inter;color:#7a3a06}
""")

mat = [("Cement","bags",200,80),("Steel","tonnes",5,2.6),("Sand","brass",6,3),("Bricks","pieces",20000,14000)]
def fm(x): return f"{x:,}" if isinstance(x,int) else f"{x:g}"
P["p76_civil_s3"] = cv(3, """<div class=kk><b>2</b>MATERIAL</div><h1 style="margin-top:14px">Material in and out,<br><span>site by site.</span></h1>""",
f'''<div class=mt3>{"".join(f'<div class="cd mr3"><div class=nm3><b>{n}</b><span>{u}</span></div><div class=nb3><div><small>IN</small><b>{fm(a)}</b></div><div><small>USED</small><b>{fm(b)}</b></div><div class=lf><small>LEFT</small><b>{fm(round(a-b,1) if isinstance(b,float) else a-b)}</b></div></div><i class=bar3><u style="width:{round((a-b)*100/a)}%"></u></i></div>' for n,u,a,b in mat)}
<div class=al3><b>Site A · cement</b> is close to your reorder level. Order before the slab day.</div></div>''',
""".vis{flex-direction:column}
.mt3{flex:1;display:flex;flex-direction:column;gap:12px}
.mr3{flex:1;padding:14px 24px;display:grid;grid-template-columns:200px 1fr;grid-template-rows:1fr auto;column-gap:20px;row-gap:8px;align-items:center}
.nm3 b{display:block;font:400 32px/1.35 Anton;margin-bottom:6px}.nm3 span{font:600 18px Inter;color:#8d877a}
.nb3{display:flex;gap:10px}.nb3 div{flex:1;text-align:center;background:#f6f1e8;border-radius:12px;padding:6px 0}
.nb3 small{display:block;font:800 13px Inter;letter-spacing:2px;color:#8d877a}.nb3 b{font:800 26px Inter}
.nb3 .lf{background:#1f2328;color:#fff}.nb3 .lf small{color:#ff9d55}
.bar3{grid-column:1/3;display:block;height:12px;border-radius:6px;background:#eee6d6;position:relative;overflow:hidden}
.bar3 u{position:absolute;left:0;top:0;bottom:0;background:#ff7a1a;border-radius:6px}
.al3{background:#ff7a1a;border-radius:18px;padding:16px 20px;font:600 21px/1.4 Inter;flex:none}
""")

bills = [("Shuttering team","Bill 3 · Site A","Approved","ap"),("Plumbing contractor","Bill 1 · Site B","Waiting for check","wt"),("Electrical team","Advance · Site C","Paid","pd"),("Brick supplier","Bill 2 · Site A","Due this week","du")]
P["p76_civil_s4"] = cv(4, """<div class=kk><b>3</b>PAYMENTS</div><h1 style="margin-top:14px">Every bill and advance,<br><span>with its status.</span></h1>""",
f'''<div class=bl4>{"".join(f'<div class="cd br4"><div class=ic4>{ic("doc",30)}</div><div class=tx4><b>{a}</b><span>{b}</span></div><em class={k}>{s}</em></div>' for a,b,s,k in bills)}
<div class=hz></div><div class=nt4>Bills, advances and approvals for every site in one list. No more hunting for slips.</div></div>''',
""".vis{flex-direction:column}
.bl4{flex:1;display:flex;flex-direction:column;gap:14px}
.br4{flex:1;display:flex;align-items:center;gap:18px;padding:0 24px}
.ic4{width:64px;height:64px;border-radius:16px;background:#f6f1e8;display:flex;align-items:center;justify-content:center;flex:none}
.tx4{flex:1}.tx4 b{display:block;font:400 30px/1.35 Anton;margin-bottom:6px}.tx4 span{font:600 20px Inter;color:#8d877a}
.br4 em{font-style:normal;font:800 18px Inter;padding:9px 14px;border-radius:10px;white-space:nowrap}
.ap{background:#e3f2e8;color:#2f7d4f}.wt{background:#fff3e8;color:#b5530a}.pd{background:#1f2328;color:#fff}.du{background:#ff7a1a;color:#1f2328}
.nt4{font:600 21px/1.4 Inter;color:#5d5a52}
""")

stages = [("Foundation",100),("Columns",100),("Slabs",66),("Brickwork",40),("Plaster",15)]
P["p76_civil_s5"] = cv(5, """<div class=kk><b>4</b>DAILY REPORT</div><h1 style="margin-top:14px">Photos and progress,<br><span>every evening.</span></h1>""",
f'''<div class="cd dr5"><div class=hd5><div><b>Site A · today</b><span>Sent by the site supervisor at 6:30 pm</span></div><em>SAMPLE</em></div>
<div class=ph5><i></i><i></i><i></i></div>
<div class=sg5>{"".join(f'<div><span>{n}</span><i><u style="width:{p}%"></u></i><b>{p}%</b></div>' for n,p in stages)}</div>
<div class=nt5><b>Work done:</b> slab 3 shuttering started, brickwork on floor 2, east side.</div></div>''',
""".vis{flex-direction:column}
.dr5{flex:1;padding:26px 28px;display:flex;flex-direction:column;gap:16px}
.hd5{display:flex;justify-content:space-between;align-items:flex-start}.hd5 b{display:block;font:400 34px/1.35 Anton;margin-bottom:6px}.hd5 span{font:600 19px Inter;color:#8d877a}
.hd5 em{font-style:normal;font:800 15px Inter;letter-spacing:3px;border:2px solid #1f2328;padding:6px 12px;border-radius:8px}
.ph5{display:flex;gap:12px}.ph5 i{flex:1;height:150px;border-radius:16px;display:block;background:linear-gradient(#cfe3ee 0 45%,#9aa0a6 45% 52%,#c0583a 52% 80%,#c9a978 80%)}
.sg5{flex:1;display:flex;flex-direction:column;gap:6px}
.sg5 div{flex:1;display:flex;align-items:center;gap:16px}
.sg5 span{width:170px;font:700 23px Inter}.sg5 b{width:70px;text-align:right;font:800 23px Inter}
.sg5 i{flex:1;height:22px;border-radius:11px;background:#eee6d6;display:block;position:relative;overflow:hidden}
.sg5 i u{position:absolute;left:0;top:0;bottom:0;background:#ff7a1a;border-radius:11px}
.nt5{background:#f6f1e8;border-radius:14px;padding:14px 16px;font:500 20px/1.4 Inter}
""")

P["p76_civil_s6"] = cv(6, """<h1>Want one app for<br><span>all your sites?</span></h1><div class=sub>We build site management apps for civil contractors and builders.</div>""",
f'''<div class=w6>{peep("Paper","Smile","ShortScratch","Chin",w=390,h=630)}<div class=o6>{"".join(f'<div class="cd q6"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Labour attendance"),(2,"Material in and out"),(3,"Bills and advances"),(4,"Daily photo report")])}</div></div>''',
""".w6{flex:1;display:flex;align-items:flex-end;gap:18px}
.o6{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q6{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q6 span{width:62px;height:62px;border-radius:10px;background:#ff7a1a;color:#1f2328;font:400 30px/62px Anton;text-align:center;flex:none}
.q6 b{font:400 32px/1.3 Anton}
""", cta="Civil contractor? DM us", ctacss="background:#ff7a1a;color:#1f2328")

# ───────── 80 USA · Commercial cleaning · CAROUSEL 5 · Fira Sans + Roboto · navy charcoal / mint / lemon
# New technique: office floor plan with zone fills (done = mint, missed = hatched lemon) + client report in a browser.
CC = """
body{--f:'Roboto';--h:'Fira Sans';background:#eef7f2;color:#1b2a3a}
h1{font-family:'Fira Sans';font-size:62px;font-weight:800;letter-spacing:-1.2px} h1 span{color:#178a5e}
.sub{color:#56677a}
.kp{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 17px Roboto;letter-spacing:3px;color:#1b2a3a}
.kp b{width:46px;height:46px;border-radius:50%;background:#ffe45c;font:800 22px/46px 'Fira Sans';text-align:center;letter-spacing:0}
.wc{background:#fff;border-radius:26px;box-shadow:0 16px 36px rgba(27,42,58,.08)}
.lb{font:700 14px Roboto;letter-spacing:3px;color:#8394a5}
"""
def cc(n, head, vis, css="", cta="Swipe", ctacss="background:#1b2a3a;color:#fff"):
    return page(CC + css, head, vis, "#1b2a3a", cta, ctacss, tagline=f"{n} / 5")

zones = [("Lobby",0,0,260,190,1),("Restrooms",260,0,200,190,1),("Kitchen",460,0,300,190,1),("Open office",0,190,460,330,1),("Conference",460,190,300,170,0),("Offices",460,360,300,160,1)]
P["p80_cleaning_s1"] = cc(1, """<h1 style="margin-top:34px">Did the night crew<br>clean every room?<br><span>Know before the client asks.</span></h1>""",
f'''<div class=fp1><div class=pl1>{"".join(f'<div class="zn {"ok" if d else "no"}" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><b>{n}</b><span>{"Done" if d else "Not done"}</span></div>' for n,x,y,w,h,d in zones)}</div>
<div class=tg1><small>SUITE 400 · LAST NIGHT · SAMPLE</small><b>5 of 6 areas done</b></div></div>''',
""".fp1{flex:1;background:#1b2a3a;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px;padding:24px}
.pl1{position:relative;width:768px;height:528px;border:4px solid #fff;background:#fff}
.zn{position:absolute;border:4px solid #fff;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px}
.zn b{font:800 26px 'Fira Sans'}.zn span{font:700 17px Roboto;padding:5px 12px;border-radius:8px}
.zn.ok{background:#bfe8d3}.zn.ok span{background:#178a5e;color:#fff}
.zn.no{background:repeating-linear-gradient(-45deg,#ffe45c 0 14px,#fff3a8 14px 28px)}.zn.no span{background:#1b2a3a;color:#ffe45c}
.tg1{display:flex;align-items:baseline;gap:20px;color:#fff}.tg1 small{font:700 15px Roboto;letter-spacing:3px;color:#9fb3c4}.tg1 b{font:800 30px 'Fira Sans';color:#ffe45c}
""")

tasks = [("Restrooms",[("Refill soap and paper",1),("Clean sinks and mirrors",1),("Mop floors",1),("Empty bins",1)],"Photo added"),
         ("Kitchen",[("Wipe counters and tables",1),("Clean microwave",1),("Empty fridge leftovers (Fri)",0),("Take out trash",1)],"Photo added")]
P["p80_cleaning_s2"] = cc(2, """<div class=kp><b>1</b>CHECKLIST</div><h1 style="margin-top:14px">A checklist for every area<br><span>of every site.</span></h1>""",
f'''<div class=ck2>{"".join(f'<div class="wc ca2"><div class=hd2><b>{z}</b><span class=lb>SUITE 400 · SAMPLE</span></div>' + "".join(f'<div class=ti2><i class="{"y" if d else ""}">{"✓" if d else ""}</i>{t}</div>' for t,d in ts) + f'<div class=pf2>{ic("camera",22)}{p}</div></div>' for z,ts,p in tasks)}</div>''',
""".vis{flex-direction:column}
.ck2{flex:1;display:flex;gap:16px}
.ca2{flex:1;padding:24px;display:flex;flex-direction:column;gap:10px}
.hd2{display:flex;flex-direction:column;gap:4px;margin-bottom:6px}.hd2 b{font:800 34px 'Fira Sans'}
.ti2{flex:1;display:flex;align-items:center;gap:14px;font:500 27px/1.3 Roboto;border-bottom:1.5px solid #e6eef0}
.ti2 i{width:42px;height:42px;border-radius:11px;border:3px solid #b8c6d1;font:800 26px/36px Roboto;font-style:normal;text-align:center;color:#fff;flex:none}
.ti2 i.y{background:#178a5e;border-color:#178a5e}
.pf2{display:flex;align-items:center;gap:10px;background:#eef7f2;border-radius:12px;padding:14px 16px;font:700 21px Roboto;color:#178a5e}
""")

crews = [("Crew A",["Suite 400","Suite 400","Suite 400","Suite 400","Suite 400"]),("Crew B",["Warehouse","Law office","Warehouse","Law office","Warehouse"]),("Crew C",["Bank branch","Gym","Bank branch","Gym","Off"])]
P["p80_cleaning_s3"] = cc(3, """<div class=kp><b>2</b>SCHEDULE</div><h1 style="margin-top:14px">Who cleans where,<br><span>every night of the week.</span></h1>""",
f'''<div class="wc sc3"><div class="rw3 th3"><span></span>{"".join(f'<em>{d}</em>' for d in ["Mon","Tue","Wed","Thu","Fri"])}</div>
{"".join(f'<div class=rw3><span>{c}</span>' + "".join(f'<i class="{"off" if s=="Off" else "c"+str(k)}">{s}</i>' for s in ss) + '</div>' for k,(c,ss) in enumerate(crews))}
<div class=nt3>Someone calls in sick? Move a site to another crew and they get the address and checklist.</div></div>''',
""".vis{flex-direction:column}
.sc3{flex:1;padding:24px;display:flex;flex-direction:column;gap:10px}
.rw3{flex:1;display:grid;grid-template-columns:130px repeat(5,1fr);gap:8px;align-items:stretch}
.th3{flex:none}.th3 em{font-style:normal;text-align:center;font:700 19px Roboto;color:#8394a5}
.rw3 span{font:800 26px 'Fira Sans';align-self:center}
.rw3 i{font-style:normal;border-radius:14px;display:flex;align-items:center;justify-content:center;text-align:center;font:700 21px/1.3 Roboto;padding:6px}
.c0{background:#bfe8d3}.c1{background:#fff3a8}.c2{background:#d7e3f0}.off{background:#f2f4f6;color:#9aa7b4}
.nt3{background:#1b2a3a;color:#fff;border-radius:16px;padding:16px 18px;font:500 20px/1.4 Roboto}
""")

P["p80_cleaning_s4"] = cc(4, """<div class=kp><b>3</b>CLIENT REPORT</div><h1 style="margin-top:14px">The client sees it done,<br><span>with photos.</span></h1>""",
browser(f'''<div class=rp4><div class=hd4><div><b>Suite 400 · Tuesday night</b><span>Cleaned by Crew A · sample report</span></div><em>5 of 6 areas</em></div>
<div class=gr4>{"".join(f'<div class=ar4><i></i><b>{n}</b><span>{t}</span></div>' for n,t in [("Lobby","10:05 pm"),("Restrooms","10:40 pm"),("Kitchen","11:10 pm"),("Open office","11:50 pm"),("Offices","12:20 am")])}
<div class="ar4 sk"><b>Conference</b><span>Skipped: room was locked</span></div></div></div>''', "clients.yourcleaningco.com · sample", "flex:1"),
""".vis{flex-direction:column}
.rp4{flex:1;display:flex;flex-direction:column;gap:14px;padding:22px;background:#f7faf9}
.hd4{display:flex;justify-content:space-between;align-items:flex-start}.hd4 b{display:block;font:800 30px 'Fira Sans'}.hd4 span{font:500 18px Roboto;color:#8394a5}
.hd4 em{font-style:normal;font:700 18px Roboto;background:#178a5e;color:#fff;padding:8px 14px;border-radius:10px}
.gr4{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.ar4{background:#fff;border:2px solid #e3ecea;border-radius:16px;padding:10px 10px 14px;display:flex;flex-direction:column;gap:4px}
.ar4 i{flex:1;display:block;border-radius:10px;background:linear-gradient(160deg,#cfe9dc 0 55%,#b5dcc8 55%);min-height:90px;margin-bottom:6px}
.ar4 b{font:800 22px 'Fira Sans'}.ar4 span{font:600 17px Roboto;color:#178a5e}
.ar4.sk{background:repeating-linear-gradient(-45deg,#fff8cc 0 14px,#fff 14px 28px);justify-content:center}.ar4.sk span{color:#1b2a3a;font-size:19px}
""")

P["p80_cleaning_s5"] = cc(5, """<h1 style="margin-top:34px">Want an app for<br><span>your cleaning crews?</span></h1><div class=sub>We build checklist, scheduling and client report apps for commercial cleaning companies.</div>""",
f'''<div class=w5>{peep("ArmsCrossed","Smile","ShortWavy","None",w=380,h=620)}<div class=o5>{"".join(f'<div class="wc q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Site checklists"),(2,"Crew schedule"),(3,"Photo proof"),(4,"Client reports")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:62px;height:62px;border-radius:50%;background:#ffe45c;font:800 27px/62px 'Fira Sans';text-align:center;flex:none}
.q5 b{font:800 30px/1.3 'Fira Sans'}
""", cta="Run a cleaning company? DM us", ctacss="background:#1b2a3a;color:#ffe45c")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
