import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 82 INDIA · Gift shop · corporate gifting · CAROUSEL 5 · Gelasio + Poppins · forest navy / coral / blush cream
# New technique: CSS gift box stack (box + lid + ribbon cross + loop bow) as the hero.
GF = """
body{--f:'Poppins';--h:'Gelasio';background:#fbefe6;color:#172a46}
h1{font-family:'Gelasio';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#e5533f}
.sub{color:#5d6680}
.kq{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Poppins;letter-spacing:3px;color:#e5533f}
.kq b{width:46px;height:46px;border-radius:50%;background:#172a46;color:#fff;font:700 22px/46px Gelasio;text-align:center;letter-spacing:0}
.cd{background:#fff;border-radius:26px;box-shadow:0 16px 36px rgba(23,42,70,.07)}
.lb{font:700 13px Poppins;letter-spacing:3px;color:#9198ab}
.gb{position:relative;flex:none;display:flex;flex-direction:column;align-items:center}
.gb .ld{height:22%;width:108%;border-radius:8px;position:relative;z-index:2;box-shadow:0 6px 0 rgba(0,0,0,.12)}
.gb .bd{flex:1;width:100%;border-radius:0 0 8px 8px}
.gb .rv{position:absolute;left:44%;width:12%;top:0;bottom:0;z-index:3}
.gb .bw{position:absolute;top:2px;left:50%;width:0;height:0;z-index:4}
.gb .bw i{position:absolute;bottom:0;width:60px;height:44px;border:11px solid;border-radius:50% 50% 50% 50%;display:block}
.gb .bw i:first-child{right:-4px;transform:rotate(-20deg)}.gb .bw i:last-child{left:-4px;transform:rotate(20deg)}
"""
def gf(n, head, vis, css="", cta="Swipe", ctacss="background:#172a46;color:#fff"):
    return page(GF + css, head, vis, "#172a46", cta, ctacss, tagline=f"{n} / 5")
def gbox(w, h, box, lid, rib):
    return f'<div class="gb free" style="width:{w}px;height:{h}px"><div class=ld style="background:{lid}"></div><div class=bd style="background:{box}"></div><i class=rv style="background:{rib}"></i><div class=bw><i style="border-color:{rib}"></i><i style="border-color:{rib}"></i></div></div>'

P["p82_gifting_s1"] = gf(1, """<h1 style="margin-top:34px">Bulk gift orders<br>on calls and chats?<br><span>Give companies<br>one order page.</span></h1>""",
f'''<div class=sc1><div class=stk>{gbox(270,220,"#172a46","#22395e","#ff6f59")}{gbox(330,290,"#ff6f59","#ff8a77","#172a46")}{gbox(230,180,"#f3c969","#f7d88a","#e5533f")}</div>
<div class=tg1><span class=lb>SAMPLE ORDER</span><b>120 boxes · 3 offices · 1 card message</b></div></div>''',
""".sc1{flex:1;background:#f4dccd;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;padding:30px;gap:50px;overflow:hidden}
.stk{display:flex;align-items:flex-end;gap:20px}
.tg1{background:#fff;border-radius:20px;padding:16px 26px;display:flex;flex-direction:column;align-items:center;gap:4px}.tg1 b{font:700 26px Gelasio}
""")

sets = [("Desk set",["Notebook","Metal pen","Year planner","Card with your logo"],"#172a46"),("Snack box",["Dry fruit jar","Cookies","Tea sampler","Card with your logo"],"#ff6f59"),("Eco set",["Steel bottle","Cotton tote","Small plant","Card with your logo"],"#4f8a5b")]
P["p82_gifting_s2"] = gf(2, """<div class=kq><b>1</b>CATALOGUE</div><h1 style="margin-top:14px">Gift sets, with<br><span>what is inside each box.</span></h1>""",
f'''<div class=cg2>{"".join(f'<div class="cd hs2"><div class=pic2 style="background:{c}">{gbox(170,124,"#fff","#f1e3d8","#ff6f59" if c!="#ff6f59" else "#172a46")}</div><b>{n}</b>' + "".join(f'<span>{x}</span>' for x in it) + '<em>Min. 25 boxes · sample</em></div>' for n,it,c in sets)}</div>''',
""".vis{flex-direction:column}
.cg2{flex:1;display:flex;gap:16px}
.hs2{flex:1;padding:16px 16px 22px;display:flex;flex-direction:column;gap:10px}
.pic2{height:340px;border-radius:18px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:40px;margin-bottom:8px;overflow:hidden}
.hs2 b{font:700 34px Gelasio}
.hs2 span{flex:1;display:flex;align-items:center;font:500 24px Poppins;padding:8px 0;border-bottom:1.5px solid #f1e3d8}
.hs2 em{margin-top:auto;font-style:normal;font:600 18px Poppins;color:#9198ab}
""")

P["p82_gifting_s3"] = gf(3, """<div class=kq><b>2</b>BULK ORDER</div><h1 style="margin-top:14px">Quantity, message and logo<br><span>in one form.</span></h1>""",
f'''<div class="cd fm3"><div class=rw3><div class=fi3><span class=lb>COMPANY</span><b>Sample Pvt Ltd</b></div><div class=fi3><span class=lb>GIFT SET</span><b>Desk set</b></div></div>
<div class=rw3><div class=fi3><span class=lb>QUANTITY</span><b>120 boxes</b></div><div class=fi3><span class=lb>DELIVER BY</span><b>Fri, 18 Dec</b></div></div>
<div class=fi3 style="flex:1.4"><span class=lb>CARD MESSAGE</span><b class=msg>Thank you for a great year with us. Wishing you and your family the very best.</b></div>
<div class=rw3><div class="fi3 up3">{ic("upload",30)}<b>Add company logo</b><span>Printed on the card</span></div><div class="fi3 up3">{ic("file",30)}<b>Upload address list</b><span>Excel or CSV</span></div></div>
<div class=bt3>Send order for confirmation</div></div>''',
""".vis{flex-direction:column}
.fm3{flex:1;padding:24px;display:flex;flex-direction:column;gap:12px}
.rw3{flex:1;display:flex;gap:12px}
.fi3{flex:1;border:2px solid #f1e3d8;border-radius:16px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;gap:6px;background:#fffaf6}
.fi3 b{font:600 28px Poppins}.fi3 .msg{font:italic 600 28px/1.45 Gelasio}
.up3{border-style:dashed;border-color:#e5b8a6;align-items:center;text-align:center;gap:4px}.up3 svg{color:#e5533f}.up3 b{font-size:21px}.up3 span{font:500 16px Poppins;color:#9198ab}
.bt3{background:#e5533f;color:#fff;border-radius:16px;padding:17px;text-align:center;font:700 21px Poppins}
""")

dl = [("Mumbai office","50 boxes","Delivered","ok",100),("Pune office","40 boxes","Out for delivery","ow",70),("Staff at home","30 addresses","22 of 30 delivered","pt",73)]
P["p82_gifting_s4"] = gf(4, """<div class=kq><b>3</b>DELIVERY</div><h1 style="margin-top:14px">Every address,<br><span>with its delivery status.</span></h1>""",
f'''<div class=dl4>{"".join(f'<div class="cd dr4"><div class=t4><div><b>{a}</b><span>{b}</span></div><em class={k}>{s}</em></div><i class=br4><u style="width:{p}%"></u></i></div>' for a,b,s,k,p in dl)}
<div class=sm4><div><b>120</b><span>boxes</span></div><div><b>3</b><span>drop points</span></div><div><b>1</b><span>link for the client</span></div></div></div>''',
""".vis{flex-direction:column}
.dl4{flex:1;display:flex;flex-direction:column;gap:14px}
.dr4{flex:1;padding:20px 26px;display:flex;flex-direction:column;justify-content:center;gap:16px}
.t4{display:flex;justify-content:space-between;align-items:center}
.t4 b{display:block;font:700 32px Gelasio}.t4 span{font:500 21px Poppins;color:#5d6680}
.t4 em{font-style:normal;font:700 18px Poppins;padding:8px 14px;border-radius:10px}
.ok{background:#dff1e2;color:#22693a}.ow{background:#ffe5df;color:#c43c28}.pt{background:#fdf0cf;color:#8a5d00}
.br4{display:block;height:14px;border-radius:7px;background:#f1e3d8;position:relative;overflow:hidden}.br4 u{position:absolute;left:0;top:0;bottom:0;background:#172a46;border-radius:7px}
.sm4{display:flex;gap:14px;flex:none}.sm4 div{flex:1;background:#172a46;color:#fff;border-radius:20px;padding:14px 18px}
.sm4 b{display:block;font:700 36px/1.3 Gelasio;color:#ffb3a5}.sm4 span{font:500 18px Poppins}
""")

P["p82_gifting_s5"] = gf(5, """<h1 style="margin-top:34px">Want an order page<br><span>for company gifting?</span></h1><div class=sub>We build gifting catalogues and bulk order pages for gift and stationery shops.</div>""",
f'''<div class=w5>{peep("Coffee","Smile","Long","None",w=380,h=620)}<div class=o5>{"".join(f'<div class="cd q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Gift set catalogue"),(2,"Bulk order form"),(3,"Logo and card message"),(4,"Delivery status")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:62px;height:62px;border-radius:50%;background:#ff6f59;color:#fff;font:700 28px/62px Gelasio;text-align:center;flex:none}
.q5 b{font:700 30px/1.3 Gelasio}
""", cta="Gift shop owner? DM us", ctacss="background:#e5533f;color:#fff")

# ───────── 85 INDIA · Courier franchise · CAROUSEL 5 · Montserrat + DM Sans · royal purple / kraft / lime
# New technique: CSS parcel with a printed shipping label (barcode stripes, AWB, to/from blocks).
CR = """
body{--f:'DM Sans';--h:'Montserrat';background:#f1eefa;color:#1d1640}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.4px} h1 span{color:#5b3fd0}
.sub{color:#5d587a}
.kx{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 17px 'DM Sans';letter-spacing:3px;color:#3b2a8a}
.kx b{width:46px;height:46px;border-radius:12px;background:#c6f432;color:#1d1640;font:800 22px/46px Montserrat;text-align:center;letter-spacing:0}
.cd{background:#fff;border-radius:26px;box-shadow:0 16px 36px rgba(29,22,64,.07)}
.lb{font:700 13px 'DM Sans';letter-spacing:3px;color:#8d88a8}
"""
def cr(n, head, vis, css="", cta="Swipe", ctacss="background:#3b2a8a;color:#fff"):
    return page(CR + css, head, vis, "#1d1640", cta, ctacss, tagline=f"{n} / 5")

P["p85_courier_s1"] = cr(1, """<h1 style="margin-top:34px">Parcel bookings<br>in a register?<br><span>Print the label.<br>Track the parcel.</span></h1>""",
f'''<div class=bx1><div class=tp1></div><div class=lbl1>
<div class=hd1><b>EXPRESS</b><span>AWB 7104 2209 85 · sample</span></div>
<div class=bc1></div>
<div class=ad1><div><span class=lb>FROM</span><b>Your Courier Point</b><em>Shop 4, Station Road</em></div><div><span class=lb>TO</span><b>Sample Receiver</b><em>PIN 395007</em></div></div>
<div class=ft1><span>2.4 kg</span><span>Box</span><span class=cod>Prepaid</span></div></div></div>''',
""".bx1{flex:1;background:#d9b382;border-radius:20px;position:relative;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 -18px 0 #c79f6c,0 24px 50px rgba(29,22,64,.18)}
.tp1{position:absolute;left:0;right:0;top:46%;height:56px;background:rgba(255,255,255,.28)}
.lbl1{position:relative;zoom:1.22;width:620px;background:#fff;border-radius:10px;padding:24px 28px;display:flex;flex-direction:column;gap:16px;box-shadow:0 12px 28px rgba(0,0,0,.15)}
.hd1{display:flex;justify-content:space-between;align-items:center}.hd1 b{font:800 30px Montserrat;background:#1d1640;color:#c6f432;padding:6px 14px;border-radius:8px}.hd1 span{font:600 18px 'DM Sans';color:#5d587a}
.bc1{height:96px;background:repeating-linear-gradient(90deg,#1d1640 0 3px,#fff 3px 6px,#1d1640 6px 11px,#fff 11px 13px,#1d1640 13px 15px,#fff 15px 21px)}
.ad1{display:flex;gap:16px}.ad1 div{flex:1;border:2px solid #e4e0f2;border-radius:12px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}
.ad1 b{font:700 22px Montserrat}.ad1 em{font-style:normal;font:500 18px 'DM Sans';color:#5d587a}
.ft1{display:flex;gap:10px}.ft1 span{flex:1;text-align:center;font:700 20px 'DM Sans';background:#f1eefa;border-radius:10px;padding:10px}.ft1 .cod{background:#c6f432}
""")

P["p85_courier_s2"] = cr(2, """<div class=kx><b>1</b>BOOKING</div><h1 style="margin-top:14px">Book at the counter,<br><span>the label prints itself.</span></h1>""",
f'''<div class="cd fm2"><div class=fi2><span class=lb>SENDER PHONE</span><b>98XXX XXX21</b><em>Regular customer found · address filled</em></div>
<div class=rw2><div class=fi2><span class=lb>RECEIVER PIN CODE</span><b>395007</b></div><div class=fi2><span class=lb>WEIGHT</span><b>2.4 kg</b></div></div>
<div class=fi2><span class=lb>SERVICE</span><div class=ch2>{"".join(f'<span class="{"on" if o else ""}">{t}</span>' for t,o in [("Express",1),("Surface",0),("Document",0)])}</div></div>
<div class=fi2><span class=lb>PAYMENT</span><div class=ch2>{"".join(f'<span class="{"on" if o else ""}">{t}</span>' for t,o in [("Prepaid",1),("Cash on delivery",0)])}</div></div>
<div class=bt2>{ic("doc",24)}Book and print label</div></div>''',
""".vis{flex-direction:column}
.fm2{flex:1;padding:26px;display:flex;flex-direction:column;gap:14px}
.rw2{flex:1;display:flex;gap:14px}
.fi2{flex:1;border:2px solid #e4e0f2;border-radius:18px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;gap:8px}
.fi2 b{font:700 30px Montserrat}.fi2 em{align-self:flex-start;font-style:normal;font:700 17px 'DM Sans';background:#eafcc0;color:#3c5a00;padding:5px 10px;border-radius:8px}
.ch2{display:flex;gap:10px}.ch2 span{font:700 21px 'DM Sans';padding:11px 18px;border-radius:12px;background:#f1eefa}.ch2 span.on{background:#3b2a8a;color:#fff}
.bt2{display:flex;align-items:center;justify-content:center;gap:12px;background:#c6f432;border-radius:16px;padding:18px;font:800 22px Montserrat}
""")

stg = ["Booked","Picked","In transit","Out for delivery","Delivered"]
pcs = [("7104 2209 85","To 395007",1),("7104 2209 71","To 400001",2),("7104 2209 64","To 110092",3),("7104 2209 52","To 560034",4)]
P["p85_courier_s3"] = cr(3, """<div class=kx><b>2</b>TRACKING</div><h1 style="margin-top:14px">Customers check the status<br><span>without calling you.</span></h1>""",
f'''<div class=tk3>{"".join(f'<div class="cd pr3"><div class=t3><b>AWB {a}</b><span>{b} · sample</span></div><div class=sg3>' + "".join(f'<div class="{"dn" if i<=k else ""}"><i></i><span>{t}</span></div>' for i,t in enumerate(stg)) + '</div></div>' for a,b,k in pcs)}</div>''',
""".vis{flex-direction:column}
.tk3{flex:1;display:flex;flex-direction:column;gap:14px}
.pr3{flex:1;padding:16px 24px;display:flex;flex-direction:column;justify-content:center;gap:12px}
.t3{display:flex;justify-content:space-between;align-items:baseline}.t3 b{font:800 25px Montserrat}.t3 span{font:600 18px 'DM Sans';color:#8d88a8}
.sg3{display:flex}
.sg3 div{flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;position:relative}
.sg3 div:before{content:"";position:absolute;top:13px;left:-50%;right:50%;height:5px;background:#e4e0f2}
.sg3 div:first-child:before{display:none}
.sg3 div.dn:before{background:#5b3fd0}
.sg3 i{width:30px;height:30px;border-radius:50%;background:#fff;border:5px solid #e4e0f2;display:block;position:relative;z-index:2}
.sg3 div.dn i{background:#5b3fd0;border-color:#5b3fd0}
.sg3 span{font:600 18px 'DM Sans';color:#8d88a8;text-align:center}.sg3 div.dn span{color:#1d1640}
""")

P["p85_courier_s4"] = cr(4, """<div class=kx><b>3</b>DAY END</div><h1 style="margin-top:14px">COD parcels and day closing<br><span>on one screen.</span></h1>""",
f'''<div class=de4><div class=nm4>{"".join(f'<div class=cd><b>{n}</b><span>{t}</span></div>' for n,t in [("46","Booked today"),("31","Delivered"),("2","Returned")])}</div>
<div class="cd cl4"><div class=lb>CASH ON DELIVERY · SAMPLE</div>{"".join(f'<div class=r4><b>AWB {a}</b><span>{p}</span><em class={k}>{s}</em></div>' for a,p,s,k in [("7104 2208 12","Rider 1","Collected","ok"),("7104 2208 19","Rider 1","Handed over","hv"),("7104 2208 27","Rider 2","Collected","ok"),("7104 2208 33","Rider 2","Not delivered","no")])}</div>
<div class=nt4>Close the day in one tap. The summary is ready for your hub.</div></div>''',
""".vis{flex-direction:column}
.de4{flex:1;display:flex;flex-direction:column;gap:14px}
.nm4{display:flex;gap:14px}.nm4 div{flex:1;padding:18px 22px}
.nm4 b{display:block;font:800 52px/1.25 Montserrat;color:#5b3fd0}.nm4 span{font:600 19px 'DM Sans';color:#5d587a}
.cl4{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:6px}
.r4{flex:1;display:flex;align-items:center;gap:14px;border-bottom:1.5px solid #eeebf7}.r4:last-child{border:none}
.r4 b{font:800 26px Montserrat;width:300px}.r4 span{flex:1;font:500 23px 'DM Sans';color:#5d587a}
.r4 em{font-style:normal;font:700 20px 'DM Sans';padding:7px 12px;border-radius:9px;white-space:nowrap}
.ok{background:#eafcc0;color:#3c5a00}.hv{background:#3b2a8a;color:#fff}.no{background:#ffe1dc;color:#b3311d}
.nt4{background:#1d1640;color:#fff;border-radius:18px;padding:18px 22px;font:600 22px 'DM Sans'}
""")

P["p85_courier_s5"] = cr(5, """<h1 style="margin-top:34px">Want booking and tracking<br><span>for your courier point?</span></h1><div class=sub>We build booking, label and tracking software for courier franchise owners.</div>""",
f'''<div class=w5>{peep("Explaining","Smile","ShortCurly","GoateeCircle",w=390,h=630)}<div class=o5>{"".join(f'<div class="cd q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Counter booking"),(2,"Label printing"),(3,"Tracking page"),(4,"COD and day end")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:62px;height:62px;border-radius:14px;background:#c6f432;font:800 27px/62px Montserrat;text-align:center;flex:none}
.q5 b{font:800 28px/1.3 Montserrat}
""", cta="Run a courier point? DM us", ctacss="background:#3b2a8a;color:#c6f432")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
