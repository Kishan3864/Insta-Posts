import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 68 INDIA · Kurti and dress material seller · CAROUSEL 6 · Gelasio + Montserrat · indigo / madder red / unbleached
# New technique: clip-path kurti silhouettes filled with CSS block-print motifs.
KU = """
body{--f:'Montserrat';--h:'Gelasio';background:#f5efe2;color:#1d2a52}
h1{font-family:'Gelasio';font-size:62px;font-weight:700} h1 span{color:#b8432f}
.sub{color:#5d6481}
.nm{display:inline-flex;align-self:flex-start;align-items:center;gap:10px;margin-top:22px;font:700 17px Montserrat;letter-spacing:3px;color:#b8432f}
.nm b{width:44px;height:44px;border-radius:50%;background:#b8432f;color:#fff;font:700 22px/44px Gelasio;text-align:center;letter-spacing:0}
.kt{clip-path:polygon(32% 0,40% 6%,60% 6%,68% 0,88% 8%,100% 34%,86% 40%,80% 28%,84% 100%,16% 100%,20% 28%,14% 40%,0 34%,12% 8%);flex:none}
.p1{background:radial-gradient(circle,#f5efe2 18%,transparent 20%) 0 0/26px 26px,radial-gradient(circle,#e7b04a 10%,transparent 12%) 13px 13px/26px 26px,#23356b}
.p2{background:repeating-linear-gradient(45deg,#b8432f 0 8px,transparent 8px 22px),repeating-linear-gradient(-45deg,#b8432f 0 8px,#f5efe2 8px 22px)}
.p3{background:radial-gradient(circle at 50% 50%,#23356b 22%,transparent 24%,transparent 40%,#23356b 42%,#23356b 46%,transparent 48%) 0 0/40px 40px,#e8d9bf}
.p4{background:repeating-linear-gradient(90deg,#2e6b54 0 12px,#f5efe2 12px 16px,#e7b04a 16px 20px,#f5efe2 20px 24px)}
.p5{background:radial-gradient(circle,#b8432f 30%,transparent 32%) 0 0/30px 30px,#f2c9b8}
.p6{background:linear-gradient(#23356b 0 30%,transparent 30%),radial-gradient(circle,#fff 14%,transparent 16%) 0 0/22px 22px,#4a63a8}
.cd{background:#fff;border-radius:26px;box-shadow:0 16px 36px rgba(29,42,82,.08)}
.pl{font-style:normal;font:700 16px Montserrat;padding:6px 12px;border-radius:10px}
.g{background:#dcf1e3;color:#1c7a43}.o{background:#fdeacc;color:#8f5a06}.b{background:#e3e8f7;color:#23356b}
"""
def ku(n, head, vis, css="", cta="Swipe", ctacss="background:#23356b;color:#fff"):
    return page(KU + css, head, vis, "#1d2a52", cta, ctacss, tagline=f"{n} / 6")
def kurti(p, w, h):
    return f'<div class="kt {p}" style="width:{w}px;height:{h}px"></div>'

P["p68_kurti_s1"] = ku(1, """<h1 style="margin-top:34px">Sending the same photos<br>to every reseller?<br><span>Share one catalogue link.</span></h1>""",
f'''<div class=hr1><div class=rk1>{kurti("p1",230,330)}{kurti("p2",230,330)}{kurti("p4",230,330)}</div>
<div class=lnk>{ic("globe",30)}<span>yourbrand.in/catalogue · sample</span><b>Copy link</b></div></div>''',
""".hr1{flex:1;background:#e3d6bd;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:34px;padding:26px}
.rk1{display:flex;gap:22px;align-items:flex-end}.rk1 .kt:nth-child(2){transform:translateY(-24px)}
.lnk{display:flex;align-items:center;gap:14px;background:#fff;border-radius:18px;padding:14px 16px 14px 20px;font:600 23px Montserrat;color:#1d2a52}
.lnk svg{color:#b8432f}.lnk b{background:#b8432f;color:#fff;font:700 19px Montserrat;padding:10px 16px;border-radius:12px}
""")

cat = [("p1", "K-101", "Cotton, indigo print"), ("p2", "K-102", "Rayon, red lattice"), ("p3", "K-103", "Cotton, dabu style"),
       ("p4", "K-104", "Rayon, stripes"), ("p5", "K-105", "Cotton, polka"), ("p6", "K-106", "Rayon, yoke print")]
P["p68_kurti_s2"] = ku(2, """<div class=nm><b>1</b>CATALOGUE</div><h1 style="margin-top:12px">Every design, sorted<br><span>with a code.</span></h1>""",
browser(f'''<div class=ct2><div class=fl2>{"".join(f'<span class="{"on" if i==0 else ""}">{t}</span>' for i,t in enumerate(["New","Cotton","Rayon","Sets","Plus sizes"]))}</div><div class=gr2>{"".join(f'<div class=it2>{kurti(p,120,168)}<b>{c}</b><small>{d}</small></div>' for p,c,d in cat)}</div></div>''', "yourbrand.in/catalogue · sample", "flex:1"),
""".vis{flex-direction:column}
.ct2{flex:1;display:flex;flex-direction:column;gap:14px;padding:20px;background:#fbf8f1}
.fl2{display:flex;gap:10px}.fl2 span{font:600 18px Montserrat;padding:9px 14px;border-radius:12px;background:#ece3d1}.fl2 span.on{background:#23356b;color:#fff}
.gr2{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
.it2{background:#fff;border-radius:18px;border:2px solid #ece3d1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px}
.it2 b{font:700 24px Gelasio;margin-top:8px}.it2 small{font:500 16px Montserrat;color:#5d6481}
""")

P["p68_kurti_s3"] = ku(3, """<div class=nm><b>2</b>DESIGN PAGE</div><h1 style="margin-top:12px">Sizes, colours and fabric<br><span>on one page.</span></h1>""",
f'''<div class="cd dp"><div class=pic>{kurti("p1",300,430)}</div><div class=inf><small>DESIGN K-101 · SAMPLE</small><b>Indigo print straight kurti</b>
<div class=lb>SIZE SET</div><div class=sz>{"".join(f'<span>{s}</span>' for s in ["S","M","L","XL","XXL"])}</div>
<div class=lb>COLOURS</div><div class=sw>{"".join(f'<i style="background:{c}"></i>' for c in ["#23356b","#b8432f","#2e6b54"])}</div>
<div class=lb>DETAILS</div>{"".join(f'<div class=dl><span>{a}</span><b>{v}</b></div>' for a,v in [("Fabric","Cotton"),("Length","44 inches"),("Set","5 pieces, one per size")])}</div></div>''',
""".vis{flex-direction:column}.dp{flex:1;display:flex;gap:24px;padding:24px}
.pic{flex:1;background:#ece3d1;border-radius:20px;display:flex;align-items:center;justify-content:center}
.inf{flex:1.1;display:flex;flex-direction:column;gap:10px}
.inf small{font:700 14px Montserrat;letter-spacing:3px;color:#8a8fa8}.inf>b{font:700 32px/1.25 Gelasio}
.lb{font:700 14px Montserrat;letter-spacing:3px;color:#8a8fa8;margin-top:8px}
.sz{display:flex;gap:8px}.sz span{flex:1;text-align:center;border:2px solid #23356b;border-radius:12px;padding:10px 0;font:700 19px Montserrat}
.sw{display:flex;gap:12px}.sw i{width:50px;height:50px;border-radius:50%;display:block;box-shadow:0 0 0 3px #fff,0 0 0 5px #d9d2c2}
.dl{flex:1;display:flex;justify-content:space-between;align-items:center;background:#f5efe2;border-radius:12px;padding:0 14px;font:500 19px Montserrat}
.dl b{font-weight:700}
""")

P["p68_kurti_s4"] = ku(4, """<div class=nm><b>3</b>RESELLER LOGIN</div><h1 style="margin-top:12px">Wholesale rates only for<br><span>resellers you approve.</span></h1>""",
f'''<div class=two4><div class="cd lk"><div class=lc>{ic("shield",56)}</div><b>Rates are for approved resellers</b><span>Log in with your phone number to see wholesale rates.</span><div class=ph4>Phone number</div><div class=bt4>Get OTP</div></div>
<div class="cd rq"><small>NEW RESELLER REQUESTS · SAMPLE</small>{"".join(f'<div class=rr4><div><b>{a}</b><span>{c}</span></div><em class="pl {k}">{s}</em></div>' for a,c,k,s in [("Sample Boutique","Jaipur","o","Approve?"),("Online seller","Pune","g","Approved"),("Sample Store","Indore","g","Approved"),("Home seller","Surat","o","Approve?")])}</div></div>''',
""".two4{flex:1;display:flex;gap:18px}
.lk{flex:1;padding:28px 24px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;text-align:center}
.lc{width:110px;height:110px;border-radius:50%;background:#e3e8f7;color:#23356b;display:flex;align-items:center;justify-content:center}
.lk b{font:700 30px/1.25 Gelasio}.lk span{font:500 20px/1.4 Montserrat;color:#5d6481}
.ph4{width:100%;border:2px solid #d9d2c2;border-radius:14px;padding:14px;font:500 20px Montserrat;color:#8a8fa8;text-align:left}
.bt4{width:100%;background:#b8432f;color:#fff;border-radius:14px;padding:15px;font:700 20px Montserrat}
.rq{flex:1.1;padding:24px;display:flex;flex-direction:column;gap:12px}
.rq small{font:700 14px Montserrat;letter-spacing:3px;color:#8a8fa8}
.rr4{flex:1;display:flex;align-items:center;justify-content:space-between;background:#f5efe2;border-radius:16px;padding:0 18px}
.rr4 b{display:block;font:700 22px Montserrat}.rr4 span{font:500 17px Montserrat;color:#5d6481}
""")

P["p68_kurti_s5"] = ku(5, """<div class=nm><b>4</b>ORDERS</div><h1 style="margin-top:12px">Orders and dispatch<br><span>in one list.</span></h1>""",
f'''<div class="cd ol5"><div class=oh5><span>ORDER</span><span>RESELLER</span><span>STATUS</span></div>{"".join(f'<div class=or5><div><b>{o}</b><small>{d}</small></div><span>{r}</span><em class="pl {k}">{s}</em></div>' for o,d,r,k,s in [("#2041","K-101 × 2 sets","Sample Boutique","b","Packed"),("#2042","K-104 × 1 set","Online seller","o","Dispatched"),("#2043","K-102 × 3 sets","Sample Store","g","Delivered"),("#2044","K-106 × 2 sets","Home seller","b","Packed")])}
<div class=nt5>{ic("truck",28)}Courier tracking number goes to the reseller when you mark it dispatched.</div></div>''',
""".vis{flex-direction:column}.ol5{flex:1;padding:24px 26px;display:flex;flex-direction:column;gap:12px}
.oh5,.or5{display:grid;grid-template-columns:1.2fr 1fr 150px;align-items:center;gap:12px}
.oh5{font:700 14px Montserrat;letter-spacing:3px;color:#8a8fa8;padding:0 18px}
.or5{flex:1;background:#f5efe2;border-radius:16px;padding:0 18px}
.or5 b{display:block;font:700 24px Gelasio}.or5 small{font:500 17px Montserrat;color:#5d6481}.or5>span{font:600 19px Montserrat}.or5 em{justify-self:end}
.nt5{display:flex;align-items:center;gap:12px;background:#23356b;color:#fff;border-radius:16px;padding:16px 18px;font:500 20px/1.4 Montserrat}.nt5 svg{flex:none;color:#e7b04a}
""")

P["p68_kurti_s6"] = ku(6, """<h1 style="margin-top:34px">Want a catalogue website<br><span>for your kurtis?</span></h1><div class=sub>We build catalogue websites and reseller ordering for kurti and dress material sellers.</div>""",
f'''<div class=w6>{peep("Device","Smile","LongBangs","None",w=380,h=620)}<div class=o6>{"".join(f'<div class="cd q6"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"One catalogue link"),(2,"Design pages"),(3,"Reseller login"),(4,"Orders + dispatch")])}</div></div>''',
""".w6{flex:1;display:flex;align-items:flex-end;gap:18px}
.o6{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q6{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q6 span{width:60px;height:60px;border-radius:50%;background:#b8432f;color:#fff;font:700 28px/60px Gelasio;text-align:center;flex:none}
.q6 b{font:700 30px/1.25 Gelasio}
""", cta="Sell kurtis wholesale? DM us", ctacss="background:#b8432f;color:#fff")

# ───────── 70 CANADA · Property manager · CAROUSEL 5 · Archivo Black + Inter · slate / brick red / snow
# New technique: CSS apartment building cross-section with flagged units.
PM = """
body{--f:'Inter';--h:'Archivo Black';background:#eef2f5;color:#1f2d3a}
h1{font-family:'Archivo Black';font-size:60px;font-weight:400;letter-spacing:-1px;line-height:1.22} h1 span{color:#c0392b}
.sub{color:#5a6b7a}
.stp{align-self:flex-start;margin-top:22px;font:700 17px Inter;letter-spacing:3px;background:#1f2d3a;color:#fff;padding:8px 14px;border-radius:8px}
.cd{background:#fff;border-radius:26px;box-shadow:0 16px 36px rgba(31,45,58,.08)}
.pl{font-style:normal;font:700 16px Inter;padding:6px 12px;border-radius:10px}
.nw{background:#fde3df;color:#a93226}.sc{background:#e1ecf7;color:#1f5d99}.dn{background:#dcf1e3;color:#1c7a43}
"""
def pm(n, head, vis, css="", cta="Swipe", ctacss="background:#c0392b;color:#fff"):
    return page(PM + css, head, vis, "#1f2d3a", cta, ctacss, tagline=f"{n} / 5")

units = [["301", "302", "303"], ["201", "202", "203"], ["101", "102", "103"]]
flags = {"203": "Leaky tap", "102": "No heat", "301": "Window latch"}
P["p70_property_s1"] = pm(1, """<h1 style="margin-top:34px">Repair requests by text<br>and voicemail?<br><span>Give tenants a portal.</span></h1>""",
f'''<div class=sky><div class=bld><div class=roof></div>{"".join('<div class=fl>' + "".join(f'<div class="un{" fg" if u in flags else ""}"><b>{u}</b><i class=wn></i><i class=wn></i>{f"<em>{flags[u]}</em>" if u in flags else ""}</div>' for u in row) + '</div>' for row in units)}<div class=gd><span class=dr></span></div></div><div class=snow></div></div>''',
""".sky{flex:1;background:linear-gradient(#cfdbe6,#eef2f5);border-radius:30px;position:relative;overflow:hidden;display:flex;align-items:flex-end;justify-content:center}
.snow{position:absolute;left:0;right:0;bottom:0;height:40px;background:#fff}
.bld{width:800px;background:#8f5b4a;padding:16px 16px 0;display:flex;flex-direction:column;gap:12px;position:relative;z-index:1;margin-bottom:40px;border-radius:8px 8px 0 0}
.roof{height:22px;background:#1f2d3a;margin:-16px -16px 0;border-radius:8px 8px 0 0}
.fl{display:flex;gap:12px}
.un{flex:1;height:200px;background:#f4ede4;border-radius:8px;position:relative;display:flex;align-items:center;justify-content:center;gap:12px;padding-top:10px}
.un b{position:absolute;left:12px;top:8px;font:700 18px Inter;color:#5a6b7a}
.wn{width:62px;height:84px;background:#a9c8e2;border:5px solid #fff;border-radius:4px;display:block;box-shadow:0 0 0 2px #c8b8a6}
.un.fg{box-shadow:inset 0 0 0 5px #c0392b}
.un em{position:absolute;left:50%;bottom:10px;transform:translateX(-50%);font-style:normal;font:700 18px Inter;background:#c0392b;color:#fff;padding:5px 10px;border-radius:8px;white-space:nowrap}
.gd{height:60px;display:flex;justify-content:center;align-items:flex-end}.dr{width:80px;height:56px;background:#1f2d3a;border-radius:6px 6px 0 0;display:block}
""")

def chips(items, on):
    return "".join(f'<span class="{"on" if t in on else ""}">{t}</span>' for t in items)
P["p70_property_s2"] = pm(2, """<div class=stp>TENANT SIDE</div><h1 style="margin-top:14px">They send a request<br><span>with photos.</span></h1>""",
f'''<div class="cd fm2"><div class=hd2><b>New repair request</b><span>Unit 203 · sample</span></div>
<div class=fg2><small>WHAT IS IT ABOUT?</small><div class=cp2>{chips(["Plumbing","Heating","Electrical","Appliance","Other"],["Plumbing"])}</div></div>
<div class=fg2><small>DESCRIBE IT</small><div class=tx2>Kitchen tap keeps dripping, even when fully closed.</div></div>
<div class=fg2><small>PHOTOS</small><div class=ph2><i></i><i></i><span>+ Add</span></div></div>
<div class=fg2><small>HOW URGENT?</small><div class=cp2>{chips(["Normal","Urgent"],["Normal"])}</div></div>
<div class=tg2><span class=sw2><i></i></span>OK to enter when I'm not home</div><div class=bt2>Send request</div></div>''',
""".vis{flex-direction:column}.fm2{flex:1;padding:24px 28px;display:flex;flex-direction:column;gap:12px}
.hd2{display:flex;justify-content:space-between;align-items:center}.hd2 b{font:400 28px 'Archivo Black'}.hd2 span{font:600 18px Inter;color:#5a6b7a}
.fg2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px}
.fg2 small{font:700 14px Inter;letter-spacing:3px;color:#8796a4}
.cp2{display:flex;gap:10px}.cp2 span{font:600 19px Inter;padding:10px 15px;border-radius:12px;background:#eef2f5}.cp2 span.on{background:#1f2d3a;color:#fff}
.tx2{border:2px solid #dde4ea;border-radius:14px;padding:14px;font:500 20px Inter}
.ph2{display:flex;gap:10px}.ph2 i{width:110px;height:72px;border-radius:12px;background:repeating-linear-gradient(45deg,#c9d6e2 0 8px,#dbe4ec 8px 16px);display:block}
.ph2 span{width:110px;height:72px;border-radius:12px;border:2px dashed #b5c3cf;display:flex;align-items:center;justify-content:center;font:600 18px Inter;color:#5a6b7a}
.tg2{display:flex;align-items:center;gap:12px;font:600 20px Inter}
.sw2{width:56px;height:32px;border-radius:16px;background:#2e8b57;display:flex;align-items:center;justify-content:flex-end;padding:3px}.sw2 i{width:26px;height:26px;border-radius:50%;background:#fff;display:block}
.bt2{background:#c0392b;color:#fff;text-align:center;border-radius:14px;padding:16px;font:700 21px Inter}
""")

cols = [("New", "nw", [("Unit 203", "Leaky kitchen tap", "Photos: 2"), ("Unit 102", "No heat in bedroom", "Marked urgent")]),
        ("Scheduled", "sc", [("Unit 301", "Window latch broken", "Thu, 10 am"), ("Unit 202", "Dryer not spinning", "Fri, 2 pm")]),
        ("Done", "dn", [("Unit 101", "Smoke alarm battery", "Closed Mon"), ("Unit 303", "Door handle loose", "Closed Tue")])]
P["p70_property_s3"] = pm(3, """<div class=stp>YOUR SIDE</div><h1 style="margin-top:14px">Every request<br><span>on one board.</span></h1>""",
f'''<div class=bd3>{"".join(f'<div class=cl3><div class=ch3><em class="pl {k}">{t}</em><span>{len(cs)}</span></div>' + "".join(f'<div class="cd cc3"><b>{u}</b><span>{d}</span><small>{x}</small></div>' for u,d,x in cs) + '</div>' for t,k,cs in cols)}</div>''',
""".bd3{flex:1;display:flex;gap:14px}
.cl3{flex:1;background:#dfe6ec;border-radius:24px;padding:16px;display:flex;flex-direction:column;gap:12px}
.ch3{display:flex;justify-content:space-between;align-items:center}.ch3 em{font-size:18px}.ch3 span{font:700 20px Inter;color:#5a6b7a}
.cc3{flex:1;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:6px;border-radius:18px}
.cc3 b{font:400 28px 'Archivo Black'}.cc3 span{font:600 24px/1.35 Inter}.cc3 small{font:600 19px Inter;color:#5a6b7a;margin-top:6px}
""")

P["p70_property_s4"] = pm(4, """<div class=stp>SAME PORTAL</div><h1 style="margin-top:14px">Rent reminders and notices<br><span>in the same place.</span></h1>""",
browser(f'''<div class=pt4><div class=hl4><b>Hi, Unit 203</b><span>Sample tenant portal</span></div><div class=gr4>
<div class=bx4><small>RENT</small><b>Due on the 1st</b><span>Reminder sent 3 days before</span><em class="pl dn">Last month: paid</em></div>
<div class=bx4><small>NOTICES</small>{"".join(f'<div class=nt4>{ic(i,24)}<span>{t}</span></div>' for i,t in [("bell","Snow clearing Tuesday. Please move cars."),("wrench","Water off Friday, 9 to 11 am")])}</div>
<div class=bx4><small>REQUESTS</small><div class=nt4>{ic("check",24)}<span>Leaky tap: scheduled Thu</span></div></div>
<div class=bx4><small>DOCUMENTS</small><div class=nt4>{ic("file",24)}<span>Lease (PDF)</span></div><div class=nt4>{ic("file",24)}<span>Building rules (PDF)</span></div></div></div></div>''', "portal.yourproperties.ca · sample", "flex:1"),
""".vis{flex-direction:column}
.pt4{flex:1;display:flex;flex-direction:column;padding:20px;gap:14px;background:#f6f8fa}
.hl4{display:flex;justify-content:space-between;align-items:baseline}.hl4 b{font:400 30px 'Archivo Black'}.hl4 span{font:600 17px Inter;color:#8796a4}
.gr4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}
.bx4{background:#fff;border-radius:18px;border:2px solid #e3e9ee;padding:18px;display:flex;flex-direction:column;gap:10px}
.bx4 small{font:700 15px Inter;letter-spacing:3px;color:#8796a4}.bx4>b{font:400 32px 'Archivo Black'}.bx4>span{font:500 21px Inter;color:#5a6b7a}.bx4{justify-content:center}.bx4 em{align-self:flex-start}
.nt4{display:flex;gap:10px;align-items:flex-start;font:600 22px/1.4 Inter}.nt4 svg{color:#c0392b;flex:none}
""")

P["p70_property_s5"] = pm(5, """<h1 style="margin-top:34px">Want a tenant portal<br><span>for your buildings?</span></h1><div class=sub>We build tenant portals and repair request boards for property managers.</div>""",
f'''<div class=w5>{peep("Explaining","Smile","MediumStraight","None",w=380,h=620)}<div class=o5>{"".join(f'<div class="cd q5"><span>{k}</span><b>{t}</b></div>' for k,t in [(1,"Repair requests"),(2,"One board for all units"),(3,"Rent reminders"),(4,"Notices + documents")])}</div></div>''',
""".w5{flex:1;display:flex;align-items:flex-end;gap:18px}
.o5{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.q5{flex:1;display:flex;align-items:center;gap:18px;padding:0 26px}
.q5 span{width:60px;height:60px;border-radius:12px;background:#c0392b;color:#fff;font:400 26px/60px 'Archivo Black';text-align:center;flex:none}
.q5 b{font:400 27px/1.3 'Archivo Black'}
""", cta="Manage rentals? DM us", ctacss="background:#1f2d3a;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
