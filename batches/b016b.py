import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 97 USA · Towing company · CAROUSEL 5 · Anton + Roboto · night black / amber light / steel blue
# New techniques: SVG flatbed tow truck with light bar, 5-lane dispatch board, phone tracking card.
TW = """
body{--f:'Roboto';--h:'Anton';background:#121417;color:#f1f3f5}
h1{font-family:'Anton';font-weight:400;font-size:70px;letter-spacing:.5px;line-height:1.25;margin-top:30px} h1 span{color:#ffb020}
.sub{color:#a3acb7}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Roboto;letter-spacing:3px;color:#ffb020}
.kt b{width:46px;height:46px;border-radius:10px;background:#ffb020;color:#121417;font:400 26px/1 Anton;display:flex;align-items:center;justify-content:center}
.cd{background:#1d2127;border-radius:22px;border:1.5px solid #2c323b}
.lb{font:700 13px Roboto;letter-spacing:3px;color:#8792a0}
"""
def tw(n, head, vis, css="", cta="Swipe", ctacss="background:#ffb020;color:#121417"):
    return page(TW + css, head, vis, "#f1f3f5", cta, ctacss, tagline=f"{n} / 5")
truck = '''<svg viewBox="0 0 760 300" width="{w}" height="{h}">
<rect x="0" y="262" width="760" height="8" rx="4" fill="#2c323b"/>
<path d="M210 150 L610 150 L640 205 L210 205 Z" fill="#3a4b63"/><rect x="210" y="200" width="430" height="20" fill="#2c3a4f"/>
<path d="M300 150 L330 110 Q340 100 360 100 L470 100 Q490 100 500 112 L530 150 Z" fill="#7d8b9c"/><path d="M345 145 L362 115 L420 115 L420 145 Z M432 145 L432 115 L488 115 L508 145 Z" fill="#c9d6e3"/>
<rect x="290" y="140" width="250" height="18" rx="8" fill="#8e9bac"/>
<circle cx="350" cy="168" r="10" fill="#2c323b"/><circle cx="480" cy="168" r="10" fill="#2c323b"/>
<path d="M40 205 L40 110 Q40 90 60 90 L150 90 Q165 90 172 104 L200 160 L210 160 L210 220 L40 220 Z" fill="#e8edf2"/>
<path d="M120 102 L160 102 L186 156 L120 156 Z" fill="#9fc3e0"/>
<rect x="64" y="70" width="90" height="16" rx="6" fill="#ffb020"/><rect x="72" y="74" width="20" height="8" rx="3" fill="#fff3d0"/><rect x="122" y="74" width="20" height="8" rx="3" fill="#fff3d0"/>
<rect x="40" y="175" width="170" height="14" fill="#ffb020"/><rect x="0" y="190" width="40" height="20" rx="6" fill="#c3ccd6"/>
<line x1="610" y1="150" x2="700" y2="245" stroke="#7d8b9c" stroke-width="10" stroke-linecap="round"/>
<g fill="#16191d" stroke="#5a6470" stroke-width="8">{wh}</g><g fill="#a3acb7">{hub}</g>
<path d="M160 20 Q200 40 160 60 M180 10 Q240 40 180 70" stroke="#ffb020" stroke-width="5" fill="none" opacity=".7" stroke-linecap="round"/>
</svg>'''
wh = "".join(f'<circle cx="{x}" cy="232" r="30"/>' for x in (110,460,560))
hub = "".join(f'<circle cx="{x}" cy="232" r="10"/>' for x in (110,460,560))
truck = truck.replace("{wh}", wh).replace("{hub}", hub)
P["p97_towing_s1"] = tw(1, """<h1>Tow calls on sticky notes?<br><span>Turn every call into<br>a job on one board.</span></h1>""",
f'''<div class=st1><div class=tk1>{truck.format(w=900,h=355)}</div>
<div class="cd cl1"><div class=nw1><i></i>NEW CALL · SAMPLE</div><div class=rw1>{"".join(f'<div><span class=lb>{a}</span><b>{b}</b></div>' for a,b in [("VEHICLE","Sedan, won't start"),("PICKUP","Hwy 80, exit 12"),("DROP-OFF","Sample Auto Shop")])}</div></div></div>''',
""".st1{flex:1;display:flex;flex-direction:column;gap:18px}
.tk1{flex:1;background:radial-gradient(circle at 20% 20%,#2a2412,#1a1d22 60%);border-radius:28px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.tk1 svg{display:block}
.cl1{padding:20px 24px;display:flex;flex-direction:column;gap:14px;flex:none}
.nw1{display:flex;align-items:center;gap:10px;font:700 15px Roboto;letter-spacing:3px;color:#ffb020}
.nw1 i{width:14px;height:14px;border-radius:50%;background:#ffb020;box-shadow:0 0 0 6px rgba(255,176,32,.2);display:block}
.rw1{display:flex;gap:14px}.rw1 div{flex:1;display:flex;flex-direction:column;gap:6px;border-left:3px solid #2c323b;padding-left:14px}
.rw1 b{font:700 25px/1.3 Roboto}
""")

fields = [("Caller phone","(555) 010-0147"),("Pickup location","Hwy 80, exit 12 · shoulder"),("Vehicle","Gray sedan · 4-door"),("Problem","Won't start"),("Drop-off","Sample Auto Shop, Main St")]
P["p97_towing_s2"] = tw(2, """<div class=kt><b>1</b>CALL FORM</div><h1 style="margin-top:20px">One short form<br><span>while they talk.</span></h1>""",
browser(f'''<div class=fm2><div class=hd2><b>New tow job</b><span class=lb>SAMPLE · 5 FIELDS</span></div>
{"".join(f'<div class=f2><span>{a}</span><b>{b}</b></div>' for a,b in fields)}
<div class=ty2><span>Tow type</span><em class=on>Flatbed</em><em>Wheel-lift</em><em>Jump start</em></div>
<div class=bt2>Create job and send a truck</div></div>''', "dispatch.yourtowing.com · sample", "flex:1", bar="#e6e9ed"),
""".vis{flex-direction:column}
.fm2{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:10px;background:#fff;color:#121417}
.hd2{display:flex;justify-content:space-between;align-items:center}.hd2 b{font:400 34px/1.3 Anton;letter-spacing:.5px}
.f2{flex:1;display:flex;flex-direction:column;justify-content:center;gap:4px;border:2px solid #e3e7ec;border-radius:14px;padding:0 18px}
.f2 span{font:600 16px Roboto;color:#7a8592}.f2 b{font:600 25px Roboto}
.ty2{display:flex;align-items:center;gap:10px;padding:4px 0}.ty2 span{font:600 18px Roboto;color:#7a8592;margin-right:6px}
.ty2 em{font-style:normal;font:700 18px Roboto;padding:10px 16px;border-radius:12px;background:#eef1f4}.ty2 em.on{background:#121417;color:#ffb020}
.bt2{background:#ffb020;border-radius:14px;text-align:center;font:700 22px Roboto;padding:16px}
""")

lanes = [("Waiting",[("Job 41","Hwy 80, exit 12","Flatbed")]),("En route",[("Job 40","Truck 3 · 12 min away","Lockout"),("Job 39","Truck 1 · 20 min","Flatbed")]),
         ("On scene",[("Job 38","Truck 2","Jump start")]),("Towing",[("Job 37","Truck 4 to shop","Wheel-lift")]),("Done",[("Job 36","Paid · photos saved",""),("Job 35","Paid · photos saved","")])]
P["p97_towing_s3"] = tw(3, """<div class=kt><b>2</b>DISPATCH BOARD</div><h1 style="margin-top:20px">Every truck and every job,<br><span>on one screen.</span></h1>""",
f'''<div class=bd3>{"".join(f'<div class=ln3><div class=hd3><b>{t}</b><em>{len(js)}</em></div>' + "".join(f'<div class="jb3 {"dn" if t=="Done" else "wt" if t=="Waiting" else ""}"><b>{a}</b><span>{b}</span>' + (f'<i>{c}</i>' if c else '') + '</div>' for a,b,c in js) + '</div>' for t,js in lanes)}</div>
<div class=nt3>Drag a job to the next lane. The customer gets a text at each step.</div>''',
""".vis{flex-direction:column;gap:14px}
.bd3{flex:1;display:flex;flex-direction:column;gap:10px}
.ln3{flex:1;background:#1d2127;border:1.5px solid #2c323b;border-radius:18px;padding:10px 12px;display:flex;gap:10px;min-width:0}
.hd3{width:190px;flex:none;display:flex;justify-content:space-between;align-items:center;padding:0 10px 0 6px}.hd3 b{font:400 30px/1.3 Anton;letter-spacing:.5px}
.hd3 em{font-style:normal;font:700 15px Roboto;background:#2c323b;border-radius:8px;padding:3px 9px}
.jb3{flex:1;max-width:340px;background:#2a3038;border-radius:12px;padding:10px 16px;display:flex;flex-direction:column;justify-content:center;gap:5px;border-left:6px solid #6fa3d6;position:relative}
.jb3 b{font:700 24px Roboto}.jb3 span{font:500 19px/1.35 Roboto;color:#b9c2cc}
.jb3 i{position:absolute;right:12px;top:12px;font-style:normal;font:700 15px Roboto;background:#121417;color:#ffb020;padding:4px 8px;border-radius:6px}
.jb3.wt{border-left-color:#ffb020}.jb3.dn{border-left-color:#4fb37a;opacity:.75}
.nt3{flex:none;background:#ffb020;color:#121417;border-radius:16px;padding:16px 20px;font:600 21px Roboto}
""")

P["p97_towing_s4"] = tw(4, """<div class=kt><b>3</b>CUSTOMER TEXT</div><h1 style="margin-top:20px">No more “where is<br>the truck?” calls.<br><span>Send a live link.</span></h1>""",
f'''<div class=w4>{phone(f"""<div class=ch4><div class=hd4>Your Towing · sample</div>
<div class=bb4>Truck 3 is on the way to Pine Rd and 5th St. Track it here:<u>track.yourtowing.com/40</u></div>
<div class=mp4><svg viewBox="0 0 300 200" width="100%" height="100%" preserveAspectRatio="xMidYMid slice"><rect width="300" height="200" fill="#e9eef3"/>
<path d="M0 140 H300 M90 0 V200 M210 0 V200" stroke="#fff" stroke-width="14"/><path d="M40 170 Q100 150 120 100 T 230 40" stroke="#ffb020" stroke-width="6" fill="none" stroke-dasharray="2 10" stroke-linecap="round"/>
<circle cx="230" cy="40" r="12" fill="#121417"/><circle cx="230" cy="40" r="5" fill="#ffb020"/><circle cx="40" cy="170" r="12" fill="#e2483d"/></svg></div>
<div class=et4><b>About 12 min away</b><span>Truck 3 · lockout service</span></div>
<div class=bb4 style="background:#eef1f4">Reply 1 if you moved to a safer spot.</div></div>""", w=360, h=720)}
<div class=sd4>{"".join(f'<div class="cd s4">{ic(i,34)}<b>{t}</b><span>{d}</span></div>' for i,t,d in [("send","Sent on its own","When you assign the truck."),("pin","Live location","Updates while the driver drives."),("chat","Replies come to you","Not to the driver's phone.")])}</div></div>''',
""".w4{flex:1;display:flex;gap:22px;align-items:center}
.ch4{flex:1;padding:12px 16px 16px;display:flex;flex-direction:column;gap:10px;background:#f7f8fa;color:#121417}
.hd4{font:700 15px Roboto;color:#7a8592;text-align:center}
.bb4{background:#fff;border-radius:16px 16px 16px 4px;padding:12px 14px;font:500 17px/1.4 Roboto;box-shadow:0 2px 6px rgba(0,0,0,.06)}
.bb4 u{display:block;color:#1f6fc2;font-weight:700}
.mp4{flex:1;border-radius:16px;overflow:hidden;min-height:0}
.et4{background:#121417;color:#fff;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}.et4 b{font:700 20px Roboto;color:#ffb020}.et4 span{font:500 15px Roboto;color:#b9c2cc}
.sd4{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.s4{flex:1;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:8px}
.s4 svg{color:#ffb020}.s4 b{font:400 30px/1.3 Anton;letter-spacing:.5px}.s4 span{font:500 20px/1.4 Roboto;color:#a3acb7}
""")

P["p97_towing_s5"] = tw(5, """<h1>Want a dispatch board<br><span>for your towing company?</span></h1><div class=sub>We build call forms, dispatch boards and customer texts for towing and roadside companies.</div>""",
f'''<div class=c5><div class=tk5>{truck.format(w=560,h=221)}</div><div class=ls5>{"".join(f'<div class=r5><em>{k}</em><b>{t}</b></div>' for k,t in [(1,"Call form in 5 fields"),(2,"Dispatch board"),(3,"Live link for the customer"),(4,"Photos and payment per job")])}</div></div>''',
""".c5{flex:1;background:#ffb020;color:#121417;border-radius:30px;padding:26px 30px;display:flex;flex-direction:column;gap:12px}
.tk5{background:#121417;border-radius:22px;display:flex;justify-content:center;padding:14px;flex:none}.tk5 svg{display:block}
.ls5{flex:1;display:flex;flex-direction:column}
.r5{flex:1;display:flex;align-items:center;gap:18px;border-top:2.5px solid rgba(18,20,23,.18)}
.r5 em{font-style:normal;width:52px;height:52px;border-radius:12px;background:#121417;color:#ffb020;font:400 28px/1 Anton;display:flex;align-items:center;justify-content:center;flex:none}
.r5 b{font:700 30px Roboto}
""", cta="Towing company? DM us", ctacss="background:#f1f3f5;color:#121417")

# ───────── 99 INDIA · Powerloom / weaving unit · CAROUSEL 5 · Lora + Roboto · cotton white / madder red / charcoal / indigo thread
# New techniques: SVG warp beam roll with thread lines, loom floor status grid, paired shift bars, beam progress cards.
PL = """
body{--f:'Roboto';--h:'Lora';background:#faf7f2;color:#2a2a2e}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#b23a2e}
.sub{color:#66615a}
.kp{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px Roboto;letter-spacing:3px;color:#b23a2e}
.kp b{width:46px;height:46px;border-radius:50%;border:3px solid #b23a2e;color:#b23a2e;font:700 22px/1 Lora;display:flex;align-items:center;justify-content:center}
.cd{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(42,42,46,.07)}
.lb{font:700 13px Roboto;letter-spacing:3px;color:#97918a}
"""
def pl(n, head, vis, css="", cta="Swipe", ctacss="background:#2a2a2e;color:#fff"):
    return page(PL + css, head, vis, "#2a2a2e", cta, ctacss, tagline=f"{n} / 5")
beam = '''<svg viewBox="0 0 700 330" width="880" height="415">
<rect x="20" y="60" width="40" height="210" rx="12" fill="#6b4a2f"/><rect x="640" y="60" width="40" height="210" rx="12" fill="#6b4a2f"/>
<rect x="60" y="80" width="580" height="170" rx="20" fill="#e9e3d6"/>
{th}
<rect x="60" y="80" width="580" height="170" rx="20" fill="url(#sh)"/>
<defs><linearGradient id="sh" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/><stop offset=".45" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#000" stop-opacity=".22"/></linearGradient></defs>
<rect x="340" y="150" width="0" height="0"/>
</svg>'''
th = "".join(f'<line x1="{66+i*6}" y1="84" x2="{66+i*6}" y2="246" stroke="{["#2d4f8a","#e9e3d6","#b23a2e","#e9e3d6"][i%4]}" stroke-width="3"/>' for i in range(96))
beam = beam.replace("{th}", th)
P["p99_loom_s1"] = pl(1, """<h1 style="margin-top:34px">Which loom made<br>how many metres?<br><span>Know every loom, every shift.</span></h1>""",
f'''<div class=st1>{beam}<div class=tg1><span class=lb>BEAM B-12 · SAMPLE</span><b>860 of 1,200 m woven</b><i><u style="width:72%"></u></i></div></div>
<div class=rw1>{"".join(f'<div class="cd k1"><b>{a}</b><span>{b}</span></div>' for a,b in [("24","looms on one screen"),("2","shifts compared"),("Live","thread break alerts")])}</div>''',
""".vis{flex-direction:column;gap:16px}
.st1{flex:1;background:#2a2a2e;border-radius:28px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:20px}
.st1 svg{display:block}
.tg1{width:700px;background:#faf7f2;border-radius:16px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.tg1 b{font:700 30px/1.3 Lora}.tg1 i{display:block;height:12px;border-radius:6px;background:#e9e3d6;position:relative;overflow:hidden}.tg1 u{position:absolute;left:0;top:0;bottom:0;background:#b23a2e;border-radius:6px}
.rw1{display:flex;gap:14px;flex:none}
.k1{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:2px}.k1 b{font:700 40px/1.25 Lora;color:#b23a2e}.k1 span{font:500 19px Roboto;color:#66615a}
""")

st = "rrrrsrrbrrrrrrirrrsrrrrr"
lbl = {"r":("Running","rn"),"s":("Thread break","sp"),"b":("Beam change","bc"),"i":("Idle","id")}
P["p99_loom_s2"] = pl(2, """<div class=kp><b>1</b>LOOM FLOOR</div><h1 style="margin-top:14px">All 24 looms<br><span>on one screen.</span></h1>""",
f'''<div class="cd fl2"><div class=gd2>{"".join(f'<div class="lm2 {lbl[c][1]}"><b>L-{i+1:02d}</b><span>{lbl[c][0]}</span></div>' for i,c in enumerate(st))}</div>
<div class=lg2>{"".join(f'<span><i class={k}></i>{t} · {st.count(c)}</span>' for c,(t,k) in lbl.items())}</div></div>''',
""".vis{flex-direction:column}
.fl2{flex:1;padding:22px;display:flex;flex-direction:column;gap:16px}
.gd2{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:1fr;gap:10px}
.lm2{border-radius:14px;padding:10px 14px;display:flex;flex-direction:column;justify-content:center;gap:2px}
.lm2 b{font:700 30px/1.3 Lora}.lm2 span{font:600 19px Roboto}
.rn{background:#e3efe3;color:#2d5b33}.sp{background:#b23a2e;color:#fff}.bc{background:#2d4f8a;color:#fff}.id{background:#ece8e1;color:#7d776f}
.lg2{display:flex;gap:22px;flex-wrap:wrap}
.lg2 span{display:flex;align-items:center;gap:8px;font:600 18px Roboto}.lg2 i{width:18px;height:18px;border-radius:5px;display:block}
""")

sh = [("L-01",420,395),("L-02",410,300),("L-03",435,420),("L-04",390,405),("L-05",425,180),("L-06",415,400)]
P["p99_loom_s3"] = pl(3, """<div class=kp><b>2</b>SHIFTS</div><h1 style="margin-top:14px">Day shift vs night shift,<br><span>metres per loom.</span></h1>""",
f'''<div class="cd sh3"><div class=hd3><b>Yesterday · metres woven</b><div class=lg3><span><i class=d3></i>Day</span><span><i class=n3></i>Night</span></div></div>
{"".join(f'<div class=r3><b>{l}</b><div class=bs3><div><i class=d3 style="width:{d*100//450}%"></i><em>{d}</em></div><div><i class=n3 style="width:{n*100//450}%"></i><em>{n}</em></div></div></div>' for l,d,n in sh)}
<div class=nt3><span class=lb>SPOT IT FAST · SAMPLE</span><b>L-05 night shift: 180 m. Stopped 4 hours for a thread break.</b></div></div>''',
""".vis{flex-direction:column}
.sh3{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:6px}
.hd3{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}.hd3 b{font:700 30px Lora}
.lg3{display:flex;gap:16px}.lg3 span{display:flex;align-items:center;gap:8px;font:600 18px Roboto}.lg3 i{width:18px;height:18px;border-radius:5px;display:block}
.d3{background:#e0a33a}.n3{background:#2d4f8a}
.r3{flex:1;display:flex;align-items:center;gap:18px;border-bottom:1.5px solid #f0ebe2}
.r3>b{width:80px;font:700 25px Lora}
.bs3{flex:1;display:flex;flex-direction:column;gap:6px}.bs3 div{display:flex;align-items:center;gap:10px}
.bs3 i{display:block;height:18px;border-radius:9px}.bs3 em{font-style:normal;font:700 18px Roboto}
.nt3{margin-top:10px;background:#fbeae7;border-left:6px solid #b23a2e;border-radius:12px;padding:14px 18px;display:flex;flex-direction:column;gap:4px}
.nt3 b{font:600 22px/1.35 Roboto}
""")

bm = [("B-12","L-07",1200,860,"About 2 days left","Next beam ready","ok"),("B-15","L-11",1000,940,"Finishes tonight","Next beam not ready","no"),("B-09","L-02",1200,310,"About 6 days left","Next beam ready","ok")]
P["p99_loom_s4"] = pl(4, """<div class=kp><b>3</b>BEAMS</div><h1 style="margin-top:14px">Know when each beam<br><span>will run out.</span></h1>""",
f'''<div class=bl4>{"".join(f'<div class="cd b4"><div class=t4><div><span class=lb>BEAM · SAMPLE</span><b>{b} on {l}</b></div><em class={k}>{nx}</em></div><div class=p4><i><u style="width:{d*100//t}%"></u></i><span>{d:,} of {t:,} m</span></div><div class=f4>{ic("clock",24)}{e}</div></div>' for b,l,t,d,e,nx,k in bm)}</div>
<div class=nt4>Beam B-15 finishes tonight and the next beam is not ready. You see it today, not when the loom stops.</div>''',
""".vis{flex-direction:column;gap:14px}
.bl4{flex:1;display:flex;flex-direction:column;gap:12px}
.b4{flex:1;padding:16px 22px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.t4{display:flex;justify-content:space-between;align-items:center}.t4 b{display:block;font:700 30px/1.3 Lora}
.t4 em{font-style:normal;font:700 17px Roboto;padding:7px 12px;border-radius:9px}.ok{background:#e3efe3;color:#2d5b33}.no{background:#b23a2e;color:#fff}
.p4{display:flex;align-items:center;gap:14px}.p4 i{flex:1;height:16px;border-radius:8px;background:#ece8e1;position:relative;overflow:hidden;display:block}.p4 u{position:absolute;left:0;top:0;bottom:0;background:#2d4f8a;border-radius:8px}
.p4 span{font:700 20px Roboto;white-space:nowrap}
.f4{display:flex;align-items:center;gap:10px;font:500 19px Roboto;color:#66615a}
.nt4{flex:none;background:#2a2a2e;color:#fff;border-radius:18px;padding:16px 20px;font:500 21px/1.4 Roboto}
""")

swatch = "".join(f'<i style="background:{c}"></i>' for c in ["#2d4f8a","#faf7f2","#b23a2e","#e0a33a","#2a2a2e","#faf7f2","#2d4f8a","#b23a2e"])
P["p99_loom_s5"] = pl(5, """<h1 style="margin-top:34px">Run a powerloom<br>or weaving unit?<br><span>Let's build your loom app.</span></h1>""",
f'''<div class=c5><div class=sw5>{swatch}</div><div class=ls5>{"".join(f'<div class=r5>{ic("check",30)}<b>{t}</b></div>' for t in ["Loom status, live","Metres per loom, per shift","Beam finish dates","Thread break log"])}</div></div>''',
""".c5{flex:1;display:flex;gap:0;border-radius:28px;overflow:hidden;box-shadow:0 14px 30px rgba(42,42,46,.1)}
.sw5{width:220px;display:flex;flex:none}.sw5 i{flex:1;display:block}
.ls5{flex:1;background:#fff;padding:24px 30px;display:flex;flex-direction:column}
.r5{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1.5px dashed #e2dbcf}.r5:last-child{border:none}
.r5 svg{color:#b23a2e;flex:none}.r5 b{font:700 40px/1.25 Lora}
""", cta="Weaving unit? DM us", ctacss="background:#b23a2e;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
