import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 87 INDIA · Florist · CAROUSEL 5 · Crimson Text + Poppins · marigold / deep leaf / off-white
# New technique: CSS bouquet (clip-path paper cone, layered radial-gradient flower heads, leaf ellipses).
FL = """
body{--f:'Poppins';--h:'Crimson Text';background:#fbf7ee;color:#1f3a2b}
h1{font-family:'Crimson Text';font-size:66px;font-weight:700;letter-spacing:-.5px;line-height:1.2} h1 span{color:#d9820b}
.sub{color:#5e6b62}
.kf{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Poppins;letter-spacing:3px;color:#1f5136}
.kf b{width:46px;height:46px;border-radius:50%;background:#f2a516;color:#1f3a2b;font:700 24px/46px 'Crimson Text';text-align:center;letter-spacing:0}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 32px rgba(31,58,43,.07)}
.lb{font:700 13px Poppins;letter-spacing:3px;color:#8c978f}
"""
def fl(n, head, vis, css="", cta="Swipe", ctacss="background:#1f5136;color:#fff"):
    return page(FL + css, head, vis, "#1f3a2b", cta, ctacss, tagline=f"{n} / 5")
def flower(x, y, r, c1, c2):
    return f'<i class=fw style="left:{x}px;top:{y}px;width:{2*r}px;height:{2*r}px;background:radial-gradient(circle,{c2} 0 22%,{c1} 24% 58%,{c2} 60% 64%,{c1} 66%)"></i>'
def leaf(x, y, w, h, deg):
    return f'<i class=lf style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;transform:rotate({deg}deg)"></i>'
flowers = (leaf(60,150,70,150,-35)+leaf(250,140,70,150,35)+leaf(150,90,60,140,0)
  + flower(70,60,58,"#e5484d","#9c1f2a")+flower(170,20,62,"#f2a516","#b86a00")+flower(260,70,56,"#f4a3b5","#c2527a")
  + flower(120,130,52,"#fff4e0","#e0a43a")+flower(220,140,50,"#e5484d","#9c1f2a"))
P["p87_florist_s1"] = fl(1, """<h1 style="margin-top:34px">Flower orders<br>on three phones?<br><span>Put them all on one board.</span></h1>""",
f'''<div class=st1><div class=bq><div class=fls>{flowers}</div><div class=cn></div><div class=tie></div></div>
<div class=sd1><div class="cd tg"><span class=lb>TODAY · SAMPLE</span><b>18 orders</b><em>6 morning · 7 afternoon · 5 evening</em></div><div class="cd tg"><span class=lb>THIS WEEK</span><b>3 decorations</b><em>Car, stage and a shop opening</em></div></div></div>''',
""".st1{flex:1;background:#f6e7c8;border-radius:30px;display:flex;align-items:center;justify-content:center;gap:34px;padding:24px;overflow:hidden}
.bq{width:380px;height:560px;position:relative;flex:none;zoom:1.12}
.fls{position:absolute;left:0;top:0;width:380px;height:280px}
.fw{position:absolute;border-radius:50%;display:block;box-shadow:0 6px 14px rgba(0,0,0,.12)}
.lf{position:absolute;border-radius:50%/50%;background:#2f7a4f;display:block}
.cn{position:absolute;left:40px;top:220px;width:300px;height:330px;background:linear-gradient(90deg,#f4efe4 0 48%,#e6dcc6 48%);clip-path:polygon(0 0,100% 0,56% 100%,44% 100%)}
.tie{position:absolute;left:160px;top:350px;width:60px;height:22px;background:#d9820b;border-radius:6px}
.sd1{display:flex;flex-direction:column;gap:16px;width:360px}
.tg{padding:20px 22px;display:flex;flex-direction:column;gap:4px}.tg b{font:700 44px/1.25 'Crimson Text'}.tg em{font-style:normal;font:500 18px Poppins;color:#5e6b62}
""")

slots = [("Morning","9 to 12",[("Bouquet, 12 red roses","Andheri · card message"),("Gerbera basket","Bandra · call at gate"),("Thank-you flowers","Kurla · leave at desk")]),
         ("Afternoon","12 to 5",[("Lily bunch","Powai · office"),("Rose and orchid box","Juhu · card message"),("Desk flowers x 3","Vikhroli · office")]),
         ("Evening","5 to 9",[("Anniversary bouquet","Malad · 7 pm sharp"),("Table flowers x 4","Goregaon · restaurant"),("Birthday bouquet","Borivali · card message")])]
P["p87_florist_s2"] = fl(2, """<div class=kf><b>1</b>ORDERS</div><h1 style="margin-top:14px">Every order, sorted<br><span>by delivery time.</span></h1>""",
f'''<div class=bd2>{"".join(f'<div class=cl2><div class=hd2><b>{t}</b><span>{h}</span></div>' + "".join(f'<div class="cd oc2"><b>{a}</b><span>{b}</span></div>' for a,b in os) + '</div>' for t,h,os in slots)}</div>''',
""".vis{flex-direction:column}
.bd2{flex:1;display:flex;gap:14px}
.cl2{flex:1;background:#f1e8d4;border-radius:24px;padding:14px;display:flex;flex-direction:column;gap:12px}
.hd2{padding:4px 6px}.hd2 b{display:block;font:700 30px 'Crimson Text'}.hd2 span{font:600 17px Poppins;color:#8c978f}
.oc2{flex:1;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:8px;border-left:8px solid #f2a516}
.oc2 b{font:600 24px/1.3 Poppins}.oc2 span{font:500 19px/1.4 Poppins;color:#5e6b62}
""")

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
bk = {3:("Shop opening","9 am · door arch","sh"),5:("Car decoration","10 am · roses + ribbon","cr"),6:("Stage backdrop","6 pm · hall booking","sg")}
P["p87_florist_s3"] = fl(3, """<div class=kf><b>2</b>DECORATION</div><h1 style="margin-top:14px">Decoration bookings<br><span>on one calendar.</span></h1>""",
f'''<div class="cd cl3"><div class=wk3>{"".join(f'<div class=dy3><b>{d}</b>' + (f'<div class="ev3 {bk[i][2]}"><b>{bk[i][0]}</b><span>{bk[i][1]}</span></div>' if i in bk else '<i class=fr3>Free</i>') + '</div>' for i,d in enumerate(days))}</div>
<div class=dt3><div><span class=lb>SAT · CAR DECORATION · SAMPLE</span><b>Roses on the bonnet, ribbon on the doors</b></div><div class=ch3>{"".join(f'<em>{t}</em>' for t in ["Advance paid","Photo of car added","Team: 2 people"])}</div></div></div>''',
""".vis{flex-direction:column}
.cl3{flex:1;padding:22px;display:flex;flex-direction:column;gap:18px}
.wk3{flex:1;display:flex;flex-direction:column;gap:8px}
.dy3{flex:1;display:flex;gap:14px;align-items:stretch}
.dy3>b{width:80px;font:700 28px 'Crimson Text';display:flex;align-items:center}
.ev3{flex:1;border-radius:12px;padding:0 18px;display:flex;align-items:center;justify-content:space-between;gap:10px}
.ev3 b{font:700 22px Poppins}.ev3 span{font:500 19px Poppins}
.sh{background:#ffe2a8}.cr{background:#1f5136;color:#fff}.sg{background:#f4c4cf}
.fr3{flex:1;border:2px dashed #e3d8c0;border-radius:12px;display:flex;align-items:center;padding-left:18px;font:600 18px Poppins;font-style:normal;color:#b3ab98}
.dt3{background:#1f5136;color:#fff;border-radius:18px;padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.dt3 .lb{color:#a9cdb7}.dt3 b{display:block;font:700 28px/1.3 'Crimson Text'}
.ch3{display:flex;gap:8px}.ch3 em{font-style:normal;font:600 16px Poppins;background:#2f7a4f;padding:7px 12px;border-radius:10px}
""")

buy = [("Red roses","120 stems","#e5484d"),("Gerbera","40 stems","#f2a516"),("Carnations","60 stems","#f4a3b5"),("Lilies","24 stems","#fff4e0"),("Orchids","2 bunches","#b46fc9"),("Fillers and leaves","6 bunches","#2f7a4f")]
P["p87_florist_s4"] = fl(4, """<div class=kf><b>3</b>BUYING LIST</div><h1 style="margin-top:14px">Tomorrow's flower list,<br><span>made from the orders.</span></h1>""",
f'''<div class="cd by4"><div class=hd4><b>Mandi list for tomorrow</b><span class=lb>FROM 18 ORDERS + 1 DECORATION · SAMPLE</span></div>
{"".join(f'<div class=rw4><i style="background:{c}"></i><span>{n}</span><b>{q}</b></div>' for n,q,c in buy)}
<div class=nt4>Change an order and the list updates. No counting stems on paper at night.</div></div>''',
""".vis{flex-direction:column}
.by4{flex:1;padding:26px 28px;display:flex;flex-direction:column;gap:6px}
.hd4{display:flex;flex-direction:column;gap:4px;margin-bottom:10px}.hd4 b{font:700 36px 'Crimson Text'}
.rw4{flex:1;display:flex;align-items:center;gap:18px;border-bottom:1.5px dashed #e6dcc6}
.rw4 i{width:40px;height:40px;border-radius:50%;display:block;flex:none;box-shadow:inset 0 0 0 3px rgba(0,0,0,.12)}
.rw4 span{flex:1;font:500 26px Poppins}.rw4 b{font:700 30px 'Crimson Text'}
.nt4{margin-top:14px;background:#f6e7c8;border-radius:14px;padding:14px 16px;font:500 20px/1.4 Poppins}
""")

P["p87_florist_s5"] = fl(5, """<h1 style="margin-top:34px">Want an order board<br><span>for your flower shop?</span></h1><div class=sub>We build order, booking and buying-list apps for florists.</div>""",
f'''<div class=w5>{peep("Coffee","Smile","Bun","None",w=380,h=620)}<div class=o5>{"".join(f'<div class="cd q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Orders by delivery time"),(2,"Decoration calendar"),(3,"Buying list"),(4,"Card messages")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:62px;height:62px;border-radius:50%;background:#f2a516;font:700 30px/62px 'Crimson Text';text-align:center;flex:none}
.q5 b{font:700 32px/1.25 'Crimson Text'}
""", cta="Run a flower shop? DM us", ctacss="background:#d9820b;color:#fff")

# ───────── 90 USA · Bookkeeper / accountant · CAROUSEL 5 · Lora + DM Sans · ledger green / ivory / ink / amber
# New technique: stacked manila folders with tabs (CSS) + document checklist.
BK = """
body{--f:'DM Sans';--h:'Lora';background:#f7f3e8;color:#1c2430}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#1f5e45}
.sub{color:#5b6470}
.kb{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'DM Sans';letter-spacing:3px;color:#1f5e45}
.kb b{width:46px;height:46px;border-radius:50%;background:#1f5e45;color:#f7f3e8;font:700 22px/46px Lora;text-align:center;letter-spacing:0}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 32px rgba(28,36,48,.07)}
.lb{font:700 13px 'DM Sans';letter-spacing:3px;color:#8a919b}
"""
def bk(n, head, vis, css="", cta="Swipe", ctacss="background:#1f5e45;color:#fff"):
    return page(BK + css, head, vis, "#1c2430", cta, ctacss, tagline=f"{n} / 5")

fold = [("Income forms",0,"#e8c98a"),("Receipts",120,"#e2bd77"),("Bank statements",240,"#d9b066")]
P["p90_bookkeeper_s1"] = bk(1, """<h1 style="margin-top:34px">Tax papers by email,<br>text and mail?<br><span>Give each client one portal.</span></h1>""",
f'''<div class=dk1><div class=fs1>{"".join(f'<div class=fd1 style="top:{i*96}px"><div class=tb1 style="margin-left:{x}px;background:{c}">{t}</div><div class=fb1 style="background:{c}"></div></div>' for i,(t,x,c) in enumerate(fold))}</div>
<div class="cd pr1"><span class=lb>SAMPLE CLIENT</span><b>5 of 8 documents in</b><i class=br1><u style="width:62%"></u></i><em>3 missing · reminder set for Monday</em></div></div>''',
""".dk1{flex:1;background:#1f5e45;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:30px;padding:30px}
.fs1{position:relative;width:640px;height:460px}
.fd1{position:absolute;left:0;right:0;height:260px;display:flex;flex-direction:column}.fb1{flex:1;border-radius:0 14px 14px 14px;box-shadow:0 -6px 18px rgba(0,0,0,.18)}
.tb1{align-self:flex-start;height:46px;margin-bottom:-2px;position:relative;z-index:2;padding:0 22px;border-radius:12px 12px 0 0;font:700 20px/46px 'DM Sans';color:#4a3510;white-space:nowrap}
.pr1{width:640px;padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.pr1 b{font:700 32px Lora}.pr1 em{font-style:normal;font:600 18px 'DM Sans';color:#b5731a}
.br1{display:block;height:14px;border-radius:7px;background:#ece6d6;position:relative;overflow:hidden}.br1 u{position:absolute;left:0;top:0;bottom:0;background:#1f5e45;border-radius:7px}
""")

docs = [("Wage forms (W-2)","In",1),("Contractor income (1099)","In",1),("Last year's return","In",1),("Bank statements","In",1),("Mortgage interest statement","In",1),("Childcare receipts","Not needed",2),("Business receipts","Missing",0),("Car mileage log","Missing",0),("Photo ID","Missing",0)]
P["p90_bookkeeper_s2"] = bk(2, """<div class=kb><b>1</b>CHECKLIST</div><h1 style="margin-top:14px">Each client sees<br><span>what you still need.</span></h1>""",
f'''<div class="cd ck2"><div class=hd2><b>Sample client · tax checklist</b><span class=lb>2026 TAX YEAR · SAMPLE</span></div>{"".join(f'<div class=r2><i class="s{s}">{"✓" if s==1 else "–" if s==2 else "!"}</i><span>{t}</span><em class="e{s}">{st}</em></div>' for t,st,s in docs)}</div>''',
""".vis{flex-direction:column}
.ck2{flex:1;padding:24px 28px;display:flex;flex-direction:column}
.hd2{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}.hd2 b{font:700 30px Lora}
.r2{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1.5px solid #f0ebdd}.r2:last-child{border:none}
.r2 i{width:36px;height:36px;border-radius:50%;font:800 20px/36px 'DM Sans';font-style:normal;text-align:center;flex:none}
.s1{background:#1f5e45;color:#fff}.s0{background:#fbe3c0;color:#b5731a}.s2{background:#eef0f2;color:#8a919b}
.r2 span{flex:1;font:500 24px 'DM Sans'}
.r2 em{font-style:normal;font:700 17px 'DM Sans';padding:6px 12px;border-radius:9px}
.e1{background:#e3f1ea;color:#1f5e45}.e0{background:#e0a030;color:#1c2430}.e2{background:#eef0f2;color:#8a919b}
""")

ups = [("business_receipts_jan_mar.pdf","Business receipts","Just now"),("mileage_log.xlsx","Car mileage log","2 min ago"),("photo_id.jpg","Photo ID","5 min ago")]
P["p90_bookkeeper_s3"] = bk(3, """<div class=kb><b>2</b>UPLOAD</div><h1 style="margin-top:14px">They upload from home,<br><span>sorted by type.</span></h1>""",
browser(f'''<div class=up3><div class=dz3>{ic("upload",48)}<b>Drop files here or take a photo</b><span>PDF, photo, Excel · goes into the right folder</span></div>
<div class=lb>JUST UPLOADED · SAMPLE</div>{"".join(f'<div class=fl3>{ic("file",30)}<div><b>{f}</b><span>Filed under: {t}</span></div><em>{w}</em></div>' for f,t,w in ups)}
<div class=dn3>{ic("check",26)}All 8 documents are in. Your bookkeeper has been told.</div></div>''', "portal.yourbookkeeping.com · sample", "flex:1"),
""".vis{flex-direction:column}
.up3{flex:1;padding:22px;display:flex;flex-direction:column;gap:12px;background:#fbf9f3}
.dz3{flex:1.2;border:3px dashed #b9cbbf;border-radius:20px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;background:#f2f7f3}
.dz3 svg{color:#1f5e45}.dz3 b{font:700 28px Lora}.dz3 span{font:500 18px 'DM Sans';color:#5b6470}
.fl3{flex:1;display:flex;align-items:center;gap:14px;background:#fff;border:2px solid #ece6d6;border-radius:16px;padding:0 18px}
.fl3 svg{color:#1f5e45;flex:none}.fl3 div{flex:1}.fl3 b{display:block;font:700 24px 'DM Sans'}.fl3 span{font:500 19px 'DM Sans';color:#5b6470}
.fl3 em{font-style:normal;font:600 17px 'DM Sans';color:#8a919b}
.dn3{display:flex;align-items:center;gap:12px;background:#1f5e45;color:#fff;border-radius:14px;padding:14px 18px;font:600 19px 'DM Sans'}
""")

cl = [("Sample client A","Ready to file","rf",8),("Sample client B","Waiting on 2 documents","wt",6),("Sample client C","Waiting on 3 documents","wt",5),("Sample client D","Not started","ns",0),("Sample client E","Ready to file","rf",8)]
P["p90_bookkeeper_s4"] = bk(4, """<div class=kb><b>3</b>YOUR BOARD</div><h1 style="margin-top:14px">See who is missing what,<br><span>in one list.</span></h1>""",
f'''<div class="cd bd4">{"".join(f'<div class=r4><div class=n4><b>{n}</b><i class=br4><u style="width:{round(k*100/8)}%"></u></i></div><em class={c}>{s}</em><span class=bt4>{"File" if c=="rf" else "Remind"}</span></div>' for n,s,c,k in cl)}</div>
<div class=nt4>Tap Remind and the client gets a text with the link and the list of what is missing.</div>''',
""".vis{flex-direction:column;gap:14px}
.bd4{flex:1;padding:14px 26px;display:flex;flex-direction:column}
.r4{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1.5px solid #f0ebdd}.r4:last-child{border:none}
.n4{flex:1;display:flex;flex-direction:column;gap:10px}.n4 b{font:700 25px Lora}
.br4{display:block;height:12px;border-radius:6px;background:#ece6d6;position:relative;overflow:hidden}.br4 u{position:absolute;left:0;top:0;bottom:0;background:#1f5e45;border-radius:6px}
.r4 em{font-style:normal;font:700 18px 'DM Sans';padding:7px 12px;border-radius:9px;white-space:nowrap}
.rf{background:#e3f1ea;color:#1f5e45}.wt{background:#fbe3c0;color:#8a5208}.ns{background:#eef0f2;color:#5b6470}
.bt4{font:700 17px 'DM Sans';border:2px solid #1f5e45;color:#1f5e45;padding:8px 14px;border-radius:10px;width:96px;text-align:center}
.nt4{background:#1c2430;color:#fff;border-radius:18px;padding:16px 20px;font:500 20px/1.4 'DM Sans';flex:none}
""")

P["p90_bookkeeper_s5"] = bk(5, """<h1 style="margin-top:34px">Want a document portal<br><span>for your clients?</span></h1><div class=sub>We build client portals and checklists for bookkeepers and accountants.</div>""",
f'''<div class=w5>{peep("Device","Smile","LongBangs","None",w=380,h=620)}<div class=o5>{"".join(f'<div class="cd q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Checklist per client"),(2,"Upload from home"),(3,"Files sorted by type"),(4,"Who is missing what")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:62px;height:62px;border-radius:50%;background:#1f5e45;color:#fff;font:700 28px/62px Lora;text-align:center;flex:none}
.q5 b{font:700 29px/1.3 Lora}
""", cta="Bookkeeper or CPA? DM us", ctacss="background:#e0a030;color:#1c2430")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
