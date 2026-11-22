import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 53 INDIA · Travel agent · SINGLE · Crimson Text + Montserrat · deep ocean / postcard cream / sun yellow
# New technique: folded paper itinerary (two panels with a centre crease gradient) vs a scroll of chat snippets.
plan = [("Day 1", "Arrive, check in, evening beach walk"), ("Day 2", "Fort visit, spice garden, local lunch"), ("Day 3", "Boat ride, free evening for shopping"), ("Day 4", "Waterfall trip, packed lunch"), ("Day 5", "Breakfast, checkout, drop to station")]
P["p53_travel"] = page("""
body{--f:'Montserrat';--h:'Crimson Text';background:#0f3b4c;color:#fdf6e3}
h1{font-family:'Crimson Text';font-size:70px;font-weight:700;letter-spacing:-.5px} h1 span{color:#ffd23f;font-style:italic}
.sub{color:#b8d3dc}
.vis{gap:22px;align-items:stretch}
.chat{width:300px;flex:none;display:flex;flex-direction:column;gap:12px;background:#174b5e;border-radius:26px;padding:22px 18px}
.chat .t{font:800 14px Montserrat;letter-spacing:3px;color:#ffd23f}
.cm{flex:1;background:#fdf6e3;color:#0f3b4c;border-radius:18px 18px 18px 4px;padding:0 14px;display:flex;align-items:center;font:600 17px/1.35 Montserrat}
.cm.x{opacity:.55}
.fold{flex:1;display:flex;border-radius:10px;overflow:hidden;box-shadow:0 30px 60px rgba(0,0,0,.35)}
.pn{flex:1;background:#fdf6e3;color:#0f3b4c;padding:26px 22px;display:flex;flex-direction:column;gap:12px}
.pn.l{background:linear-gradient(90deg,#fdf6e3 85%,#e7dcc2)}.pn.r{background:linear-gradient(90deg,#efe5cc,#fdf6e3 15%)}
.pn small{font:800 13px Montserrat;letter-spacing:3px;color:#c0841a}
.pn b{font:700 34px/1.2 'Crimson Text'}
.kv{display:flex;flex-direction:column;gap:2px;border-bottom:1px dashed #d6c8a6;padding-bottom:10px}
.kv em{font:700 13px Montserrat;font-style:normal;letter-spacing:2px;color:#6f8a92}.kv span{font:600 19px Montserrat}
.sun{width:92px;height:92px;border-radius:50%;background:radial-gradient(circle,#ffd23f 0 45%,transparent 46%),repeating-conic-gradient(#ffd23f 0 8deg,transparent 8deg 22deg);margin-top:auto;align-self:center}
.dy{flex:1;display:flex;gap:12px;align-items:center;border-bottom:1px dashed #d6c8a6}
.dy i{font-style:normal;font:800 15px Montserrat;background:#0f3b4c;color:#ffd23f;border-radius:10px;padding:6px 8px;flex:none}
.dy span{font:600 17px/1.35 Montserrat}
.pdf{display:flex;align-items:center;gap:8px;font:700 16px Montserrat;color:#0f3b4c;background:#ffd23f;border-radius:12px;padding:10px 12px;align-self:flex-start}
""", "<h1>20 chat messages?<br><span>Send one clean itinerary.</span></h1><div class=sub>For travel agents: fill a simple form, get a neat PDF with your name on it.</div>",
f'''<div class=chat><div class=t>BEFORE</div>{"".join(f'<div class="cm {"x" if k in (1,3) else ""}">{m}</div>' for k,m in enumerate(["Hotel is near the beach", "Day 2 changed, see above", "Pickup at 9, not 10", "Wait, which day is the boat?", "Sending hotel photo again", "Final plan? Please send"]))}</div>
<div class=fold><div class="pn l"><small>ITINERARY · SAMPLE</small><b>Coastal trip,<br>5 days</b>
<div class=kv><em>TRAVELLERS</em><span>2 adults</span></div><div class=kv><em>STAY</em><span>Sea view hotel, 4 nights</span></div><div class=kv><em>PICKUP</em><span>Station, 9 am</span></div><div class=sun></div></div>
<div class="pn r"><small>DAY BY DAY</small>{"".join(f'<div class=dy><i>{d}</i><span>{t}</span></div>' for d,t in plan)}<div class=pdf>{ic("file",20)} Your Agency · PDF</div></div></div>''',
"#fdf6e3", "Want this for your agency? DM us", "background:#ffd23f;color:#0f3b4c")

# ───────── 54 USA · Pressure washing · SINGLE · Archivo Black + Open Sans · aqua / concrete / navy
# New technique: top-down CSS "satellite" yard with a dashed measured area and a size callout, in a laptop mockup.
P["p54_pressurewash"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#e9f6f8;color:#0b2540}
h1{font-family:'Archivo Black';font-size:60px;font-weight:400;letter-spacing:-1px;line-height:1.2} h1 span{color:#0aa5c2}
.sub{color:#4a6278}
.vis{flex-direction:column;align-items:center;gap:0}
.lap{width:100%;flex:1;display:flex;flex-direction:column;align-items:center;min-height:0}
.scr{width:100%;flex:1;background:#0b2540;border-radius:22px 22px 0 0;padding:16px;display:flex;min-height:0}
.app{flex:1;background:#fff;border-radius:10px;display:flex;overflow:hidden}
.side{width:300px;flex:none;padding:22px 20px;display:flex;flex-direction:column;gap:12px;border-right:1px solid #e3ecf1}
.side small{font:800 13px 'Open Sans';letter-spacing:3px;color:#7b93a6}
.side b{font:400 24px/1.25 'Archivo Black'}
.ch{display:flex;flex-wrap:wrap;gap:8px}.ch i{font-style:normal;font:700 15px 'Open Sans';padding:8px 12px;border-radius:12px;border:2px solid #d5e3ea;color:#33506a}.ch i.on{background:#0aa5c2;border-color:#0aa5c2;color:#fff}
.sz{background:#e9f6f8;border-radius:14px;padding:14px;display:flex;flex-direction:column;gap:2px}.sz em{font:700 14px 'Open Sans';font-style:normal;color:#4a6278}.sz strong{font:400 26px 'Archivo Black';color:#0b2540}
.dt{display:flex;gap:6px}.dt i{flex:1;font-style:normal;text-align:center;padding:8px 0;border-radius:10px;background:#f1f5f8;font:700 14px/1.3 'Open Sans';color:#33506a}.dt i.on{background:#0b2540;color:#fff}
.ad{display:flex;flex-direction:column;gap:4px}.ad em{font:700 14px 'Open Sans';font-style:normal;color:#4a6278}.ad span{border:2px solid #d5e3ea;border-radius:10px;padding:9px 12px;font:600 16px 'Open Sans';color:#33506a;display:flex;align-items:center;gap:8px}
.snd{margin-top:auto;background:#0aa5c2;color:#fff;border-radius:12px;padding:13px;text-align:center;font:800 17px 'Open Sans'}
.map{flex:1;position:relative;background:#7fae6a;overflow:hidden}
.map .road{position:absolute;left:0;right:0;bottom:0;height:90px;background:#5d6670}
.map .road:after{content:"";position:absolute;left:0;right:0;top:42px;height:6px;background:repeating-linear-gradient(90deg,#f2f2f2 0 40px,transparent 40px 80px)}
.map .house{position:absolute;left:70px;top:46px;width:240px;height:180px;background:#c9c2b8;border-radius:4px;box-shadow:inset 0 0 0 10px #b2aa9f}
.map .drive{position:absolute;left:330px;top:70px;width:120px;height:calc(100% - 160px);background:#cfd3d6}
.map .deck{position:absolute;left:70px;top:246px;width:200px;height:110px;background:#b07a4a;background-image:repeating-linear-gradient(90deg,#a06c3e 0 4px,transparent 4px 22px)}
.map .tree{position:absolute;width:70px;height:70px;border-radius:50%;background:#4f8a3e;box-shadow:inset -8px -8px 0 #3e7230}
.map .meas{position:absolute;left:322px;top:62px;width:136px;height:calc(100% - 144px);border:4px dashed #ffe14d;border-radius:4px}
.map .tag{position:absolute;left:70px;top:400px;background:#0b2540;color:#fff;border-radius:12px;padding:10px 14px;font:800 16px/1.35 'Open Sans'}
.map .tag em{display:block;font:700 13px 'Open Sans';font-style:normal;color:#ffe14d}
.base{width:calc(100% + 40px);height:26px;background:linear-gradient(#cfd8de,#aab6bf);border-radius:0 0 26px 26px;flex:none;margin:0 -20px}
""", "<h1>Quote requests with<br><span>the size already filled in.</span></h1><div class=sub>For pressure washing: customers pick surfaces and mark the area on a map.</div>",
f'''<div class=lap><div class=scr><div class=app><div class=side><small>GET A QUOTE · SAMPLE</small><b>What should we wash?</b>
<div class=ch><i class=on>Driveway</i><i>Deck</i><i>Siding</i><i>Fence</i><i>Patio</i></div>
<div class=sz><em>Area marked on the map</em><strong>About 600 sq ft</strong></div>
<div class=ad><em>Address</em><span>Your street address</span></div><div class=ad><em>Photos</em><span>{ic("camera",18)} 2 added</span></div><b>Pick a day</b><div class=dt><i>Mon</i><i class=on>Tue</i><i>Wed</i><i>Thu</i></div><b>Time</b><div class=dt><i class=on>Morning</i><i>Afternoon</i></div><div class=snd>Send for a quote</div></div>
<div class=map><div class=house></div><div class=deck></div><div class=drive></div><div class=meas></div><div class=tree style="left:500px;top:40px"></div><div class=tree style="left:520px;top:200px"></div><div class=road></div>
<div class=tag><em>DRIVEWAY · SAMPLE</em>Marked by the customer →</div></div></div></div><div class=base></div></div>''',
"#0b2540", "Want quotes like this? DM us", "background:#0b2540;color:#fff")

# ───────── 55 INDIA · Exam coaching test series · SINGLE · Inter + Crimson Text · OMR pink / ink blue / white
# New technique: CSS OMR bubble sheet (filled / empty bubbles) beside an instant result card.
import random
random.seed(55)
omr_rows = []
for q in range(1, 11):
    pick = random.randint(0, 3)
    omr_rows.append(f'<div class=q><span>{q}</span>' + "".join(f'<i class="{"on" if k == pick else ""}">{"ABCD"[k]}</i>' for k in range(4)) + '</div>')
P["p55_testseries"] = page("""
body{--f:'Inter';--h:'Crimson Text';background:#fbe9ee;color:#1d2a6b}
h1{font-family:'Crimson Text';font-size:70px;font-weight:700;letter-spacing:-.5px} h1 span{color:#d6336c}
.sub{color:#5a6390}
.vis{gap:22px;align-items:stretch}
.omr{width:400px;flex:none;background:#fff;border-radius:18px;border:3px solid #f2a7bd;padding:20px;display:flex;flex-direction:column;gap:8px;background-image:linear-gradient(#fde3ea 0 58px,transparent 58px)}
.omr .hd{font:800 15px Inter;letter-spacing:3px;color:#d6336c;height:40px;display:flex;align-items:center}
.q{flex:1;display:flex;align-items:center;gap:12px;border-bottom:1px solid #fadbe4}
.q span{width:34px;font:800 18px Inter;color:#d6336c}
.q i{width:46px;height:46px;border-radius:50%;border:2px solid #f2a7bd;display:flex;align-items:center;justify-content:center;font:700 15px Inter;font-style:normal;color:#e58aa6}
.q i.on{background:#1d2a6b;border-color:#1d2a6b;color:#1d2a6b}
.rc{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.res{flex:1;background:#1d2a6b;color:#fff;border-radius:26px;padding:26px;display:flex;flex-direction:column;gap:14px}
.res small{font:800 14px Inter;letter-spacing:3px;color:#ff9fbf}
.big{display:flex;align-items:baseline;gap:10px}.big b{font:700 92px/1.2 'Crimson Text'}.big span{font:600 26px Inter;color:#c5cbef}
.st{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.st div{background:#2a3884;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}
.st em{font:700 13px Inter;font-style:normal;letter-spacing:2px;color:#aab2e6}.st b{font:800 26px Inter}
.tp{flex:1;display:flex;flex-direction:column;gap:8px}
.tp div{flex:1;display:flex;align-items:center;gap:12px;font:600 17px Inter}
.tp div span{width:130px;flex:none;font-size:20px}.tp em{font:800 18px Inter;font-style:normal;width:52px;text-align:right}.tp i{flex:1;height:14px;border-radius:7px;background:#2a3884;overflow:hidden;display:block}.tp i b{display:block;height:100%;background:#ff9fbf;border-radius:7px}
.ak{background:#fff;border-radius:20px;padding:18px 22px;display:flex;align-items:center;gap:14px;font:700 20px/1.35 Inter}
.ak .ib{width:50px;height:50px;border-radius:14px;background:#d6336c;color:#fff}
""", "<h1>Still checking answer<br>sheets <span>by hand?</span></h1><div class=sub>For exam coaching: online test series with instant results, ranks and answer keys.</div>",
f'''<div class=omr><div class=hd>ANSWER SHEET · SAMPLE</div>{"".join(omr_rows)}</div>
<div class=rc><div class=res><small>RESULT · SAMPLE TEST 4</small><div class=big><b>72</b><span>out of 100</span></div>
<div class=st><div><em>RANK</em><b>14 of 120</b></div><div><em>TIME</em><b>52 min</b></div></div>
<div class=tp>{"".join(f'<div><span>{a}</span><i><b style="width:{w}%"></b></i><em>{w}%</em></div>' for a,w in [("Reasoning",85),("Maths",60),("English",78),("General", 64)])}</div></div>
<div class=ak><span class=ib>{ic("doc",24)}</span>Answer key with solutions opens right after the test.</div></div>''',
"#1d2a6b", "Run a coaching centre? DM us", "background:#d6336c;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
