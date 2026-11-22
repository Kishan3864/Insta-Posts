import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 191 INDIA · Borewell drilling · SINGLE · Archivo Black + Open Sans · earth brown / water blue / off-white
# New technique: SVG ground cross-section with a depth ruler and drill line as a per-site drilling log.
def ground():
    layers = [(0, 40, "#b98b5e", "Soil"), (40, 120, "#a37a52", "Clay"), (120, 260, "#8d8476", "Soft rock"), (260, 440, "#6e6a64", "Hard rock")]
    out = '<svg viewBox="0 0 470 850" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block">'
    out += '<rect x="0" y="0" width="470" height="60" fill="#dfeef5"/>'
    out += '<rect x="196" y="6" width="60" height="54" rx="4" fill="#2f241b"/><rect x="214" y="-4" width="24" height="20" fill="#2f241b"/><text x="226" y="40" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="14" fill="#fff"><tspan>RIG</tspan></text>'
    sc = 1.75
    for a, b, c, n in layers:
        y1 = 60 + a * sc; h = (b - a) * sc
        out += f'<rect x="70" y="{y1}" width="400" height="{h}" fill="{c}"/><text x="84" y="{y1+h/2+6}" text-anchor="start" font-family="Open Sans" font-weight="700" font-size="18" fill="#fff"><tspan>{n}</tspan></text>'
    for d in range(0, 441, 80):
        y = 60 + d * sc
        out += f'<rect x="54" y="{y-1.5}" width="16" height="3" fill="#2f241b"/><text x="48" y="{y+6}" text-anchor="end" font-family="Open Sans" font-weight="700" font-size="16" fill="#2f241b"><tspan>{d}</tspan></text>'
    out += f'<rect x="219" y="60" width="14" height="{340*sc}" fill="#f4efe6" stroke="#2f241b" stroke-width="2"/>'
    out += f'<rect x="219" y="{60+300*sc}" width="14" height="{40*sc}" fill="#2a9fd6"/>'
    out += f'<rect x="250" y="{60+300*sc-22}" width="150" height="40" rx="20" fill="#2a9fd6"/><text x="325" y="{60+300*sc+5}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="17" fill="#fff"><tspan>Water at 300 ft</tspan></text>'
    out += f'<rect x="250" y="{60+340*sc-4}" width="150" height="40" rx="20" fill="#f4efe6"/><text x="325" y="{60+340*sc+23}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="17" fill="#2f241b"><tspan>Stopped 340 ft</tspan></text>'
    out += '<text x="10" y="36" font-family="Open Sans" font-weight="700" font-size="14" fill="#2f241b"><tspan>FEET</tspan></text>'
    return out + '</svg>'
logs = [("Drilled depth", "340 ft"), ("Casing pipe", "60 ft"), ("Water found at", "300 ft"), ("Rig hours", "7.5 h")]
sites = [("Site 1 · Sample farm", "Done today", "d"), ("Site 2 · Sample villa", "Tomorrow, 7 AM", "t"), ("Site 3 · Sample factory", "Thu · survey done", "t")]
P["p191_borewell"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#f4efe6;color:#2f241b}
h1{font-family:'Archivo Black';font-size:58px;font-weight:400;letter-spacing:-.8px;line-height:1.22} h1 span{color:#1f86b8}
.sub{color:#6b5a4a;font-size:23px}
.vis{gap:16px}
.gp{width:440px;flex:none;background:#fff;border-radius:28px;padding:16px 14px 10px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(47,36,27,.10)}
.gp small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#8f7d6a;margin-left:8px}.gp .gv{flex:1;min-height:0}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.lg2{flex:1;background:#2f241b;color:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:10px}
.lg2 small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#d8c2a5}.lg2 h3{font:400 28px/1.3 'Archivo Black'}
.lr{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.14)}.lr span{font:600 20px 'Open Sans';color:#e9dccb}.lr b{font:400 28px/1.3 'Archivo Black'}
.lr.w b{color:#5cc3f2}
.ph{display:flex;gap:8px}.ph i{flex:1;font-style:normal;background:#3d3026;border-radius:12px;padding:10px;text-align:center;font:600 16px 'Open Sans';color:#e9dccb}
.st{background:#fff;border-radius:24px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(47,36,27,.08)}
.st small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#8f7d6a}
.sr{display:flex;justify-content:space-between;align-items:center;font:700 19px 'Open Sans'}.sr em{font-style:normal;font:700 16px 'Open Sans';border-radius:10px;padding:5px 10px}
.sr.d em{background:#1f86b8;color:#fff}.sr.t em{background:#efe5d6;color:#6b5a4a}
""", "<h1>Borewell depth and pipes<br><span>written on a cement bag?</span></h1><div class=sub>Log every site's depth, casing and rig hours on the spot.</div>",
f'''<div class=gp><small>SITE 1 · DRILLING LOG · SAMPLE</small><div class=gv>{ground()}</div></div>
<div class=rc><div class=lg2><small>SITE 1 · SAMPLE FARM · TODAY</small><h3>Borewell report</h3>
{"".join(f'<div class="lr {"w" if "Water" in a else ""}"><span>{a}</span><b>{b}</b></div>' for a,b in logs)}
<div class=ph>{"".join(f'<i>{ic("camera",18)} {t}</i>' for t in ["Rig", "Pipe", "Water"])}</div></div>
<div class=st><small>RIG 1 · THIS WEEK</small>{"".join(f'<div class="sr {k}"><span>{a}</span><em>{b}</em></div>' for a,b,k in sites)}</div></div>''',
"#2f241b", "Run borewell rigs? DM us", "background:#1f86b8;color:#fff")


# ───────── 192 INDIA · Ice cream parlour party orders · SINGLE · Lora + DM Sans · strawberry pink / pistachio / cream
# New technique: diagonal before/after split (clip-path) — a vague phone-call note vs a clear order form, with a scoop divider badge.
def cup(c1, c2):
    return (f'<svg viewBox="0 0 80 90" width="64" height="72" style="display:block;flex:none"><circle cx="26" cy="30" r="20" fill="{c1}"/><circle cx="54" cy="30" r="20" fill="{c2}"/><circle cx="40" cy="18" r="18" fill="{c1}" opacity=".9"/>'
            '<path d="M8 40h64l-8 46H16z" fill="#fff" stroke="#3a1f2b" stroke-width="3" stroke-linejoin="round"/><path d="M14 54h52" stroke="#f06292" stroke-width="5"/></svg>')
items = [("Chocolate tub", "2 × 1 L", "#7b4a2f", "#9c6440"), ("Mango tub", "1 × 1 L", "#ffbf3c", "#ffd36e"), ("Pista cups", "20 cups", "#a8d28b", "#c4e3ad"), ("Strawberry cups", "10 cups", "#f48fb1", "#f8b5cb")]
P["p192_icecream"] = page("""
body{--f:'DM Sans';--h:'Lora';background:#fff3ea;color:#3a1f2b}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.6px;line-height:1.22} h1 span{color:#e2457a}
.sub{color:#7a5562;font-size:23px}
.vis{position:relative}
.bf,.af{position:absolute;inset:0;border-radius:30px;padding:30px}
.bf{background:#ffe0ea;clip-path:polygon(0 0,100% 0,100% 30%,0 56%)}
.af{background:#3a1f2b;color:#fff;clip-path:polygon(0 61%,100% 35%,100% 100%,0 100%)}
.nt{width:580px;background:#fffef6;padding:24px 28px;border-radius:8px;box-shadow:0 16px 30px rgba(58,31,43,.14);font:italic 600 30px/1.5 Lora;color:#5a3a44}
.nt small{display:block;font:700 14px 'DM Sans';font-style:normal;letter-spacing:2.5px;color:#b07a8b;margin-bottom:6px}
.nt s{color:#c2185b}
.qs{position:absolute;right:34px;top:40px;display:flex;flex-direction:column;gap:10px;align-items:flex-end}
.qs i{font-style:normal;background:#fff;border:2px dashed #e2457a;color:#e2457a;border-radius:16px;padding:10px 18px;font:700 23px 'DM Sans'}
.badge{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);background:#a8d28b;color:#24401b;border-radius:40px;padding:12px 26px;font:700 22px 'DM Sans';box-shadow:0 12px 24px rgba(0,0,0,.18);z-index:3;white-space:nowrap}
.fm{position:absolute;left:30px;right:30px;bottom:30px;display:flex;flex-direction:column;gap:10px}
.fm small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#f8b5cb}
.ig{display:grid;grid-template-columns:1fr 1fr;gap:10px}.ig div{background:#4b2c39;border-radius:18px;padding:10px 14px;display:flex;align-items:center;gap:12px}
.ig b{display:block;font:700 21px 'DM Sans'}.ig span{font:500 18px 'DM Sans';color:#f3d7e0}
.fr{display:flex;gap:10px}.fr div{flex:1;background:#4b2c39;border-radius:16px;padding:10px 14px}.fr span{display:block;font:700 13px 'DM Sans';letter-spacing:2px;color:#f8b5cb}.fr b{font:700 21px 'DM Sans'}
.fr .ok{background:#a8d28b;color:#24401b}.fr .ok span{color:#3d6b2e}
""", "<h1>Party orders on a call<br><span>get mixed up.</span></h1><div class=sub>Send one order link. The customer picks flavours, packs and pickup time.</div>",
f'''<div class=bf><div class=nt><small>BEFORE · NOTE FROM A CALL · SAMPLE</small>"Some chocolate, some mango…<br>for around 30 people,<br>evening time, <s>name?</s>"</div>
<div class=qs><i>How many litres?</i><i>Which evening?</i><i>Cups or tubs?</i></div></div>
<div class=badge>After: one order link</div>
<div class=af><div class=fm><small>PARTY ORDER P-58 · SAMPLE CUSTOMER</small>
<div class=ig>{"".join(f'<div>{cup(c1,c2)}<p><b>{a}</b><span>{q}</span></p></div>' for a,q,c1,c2 in items)}</div>
<div class=fr><div><span>PICKUP</span><b>Sat, 28 Nov · 6 PM</b></div><div><span>FOR</span><b>About 30 people</b></div><div class=ok><span>STATUS</span><b>Advance paid</b></div></div></div></div>''',
"#3a1f2b", "Run an ice cream parlour? DM us", "background:#e2457a;color:#fff")


# ───────── 193 USA · Appliance repair · CAROUSEL 5 · Montserrat + Open Sans · off-white / cobalt / amber
# New techniques: stacked notification cards hook, appliance picker with drawn icons, parts-on-order board, tech route day strip.
AP = """
body{--f:'Open Sans';--h:'Montserrat';background:#f6f6f2;color:#14213d}
h1{font-family:'Montserrat';font-weight:800;font-size:60px;letter-spacing:-1.3px;line-height:1.22} h1 span{color:#2251cc}
.kk{font:700 16px 'Open Sans';letter-spacing:3px;color:#d98a00;margin-top:22px}
.cd{background:#fff;border-radius:26px;box-shadow:0 14px 30px rgba(20,33,61,.08)}
"""
def ap(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#14213d;color:#fff"):
    return page(AP + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#14213d", cta, ctacss, tagline=f"{n} / 5")
def appl(k, s=70, col="#2251cc"):
    d = {"washer": '<rect x="10" y="6" width="60" height="68" rx="8" fill="none" stroke="C" stroke-width="4"/><circle cx="40" cy="44" r="18" fill="none" stroke="C" stroke-width="4"/><circle cx="22" cy="17" r="3" fill="C"/><circle cx="32" cy="17" r="3" fill="C"/>',
         "fridge": '<rect x="16" y="4" width="48" height="72" rx="8" fill="none" stroke="C" stroke-width="4"/><path d="M16 30h48" stroke="C" stroke-width="4"/><path d="M26 14v8M26 40v14" stroke="C" stroke-width="4" stroke-linecap="round"/>',
         "dryer": '<rect x="10" y="6" width="60" height="68" rx="8" fill="none" stroke="C" stroke-width="4"/><circle cx="40" cy="44" r="18" fill="none" stroke="C" stroke-width="4"/><path d="M30 44q5-6 10 0t10 0" fill="none" stroke="C" stroke-width="3"/><rect x="18" y="13" width="22" height="7" rx="3" fill="C"/>',
         "oven": '<rect x="8" y="10" width="64" height="62" rx="8" fill="none" stroke="C" stroke-width="4"/><rect x="18" y="30" width="44" height="32" rx="4" fill="none" stroke="C" stroke-width="4"/><circle cx="22" cy="20" r="3" fill="C"/><circle cx="34" cy="20" r="3" fill="C"/><circle cx="46" cy="20" r="3" fill="C"/>',
         "dish": '<rect x="12" y="6" width="56" height="68" rx="8" fill="none" stroke="C" stroke-width="4"/><path d="M12 20h56" stroke="C" stroke-width="4"/><path d="M28 13h24" stroke="C" stroke-width="4" stroke-linecap="round"/><path d="M26 44h28M26 56h28" stroke="C" stroke-width="3" stroke-dasharray="4 4"/>'}[k]
    return f'<svg viewBox="0 0 80 80" width="{s}" height="{s}" style="display:block;flex:none">{d.replace("C", col)}</svg>'
notes = [("washer", "Washer won't drain", "Sample caller · 7:42 AM", "Missed call"), ("fridge", "Fridge not cooling", "Sample caller · 8:15 AM", "Voicemail"), ("dryer", "Dryer making a loud noise", "Sample caller · 9:03 AM", "Missed call"), ("oven", "Oven not heating", "Sample caller · 9:30 AM", "Text: call me?")]
P["p193_appliance_s1"] = ap(1, "APPLIANCE REPAIR", "Four calls before 10 AM.<br><span>Which one, what model?</span>",
f'''<div class=stk>{"".join(f'<div class=nf style="margin-left:{i*34}px;margin-right:{(3-i)*34}px"><span class=ai>{appl(k,56)}</span><div><b>{a}</b><span>{b}</span></div><em>{t}</em></div>' for i,(k,a,b,t) in enumerate(notes))}
<div class=qn>No model number. No photo. No address yet.</div></div>''',
css=""".stk{flex:1;display:flex;flex-direction:column;gap:14px}
.nf{flex:1;background:#fff;border-radius:24px;display:flex;align-items:center;gap:18px;padding:0 22px;box-shadow:0 14px 30px rgba(20,33,61,.10);border-left:8px solid #d98a00}
.ai{width:84px;height:84px;border-radius:20px;background:#eef2fc;display:flex;align-items:center;justify-content:center;flex:none}
.nf div{flex:1}.nf b{display:block;font:700 27px/1.3 Montserrat}.nf span{font:600 19px 'Open Sans';color:#68708a}
.nf em{font-style:normal;font:700 17px 'Open Sans';background:#fff3dc;color:#9a6200;border-radius:12px;padding:7px 12px}
.qn{background:#14213d;color:#fff;border-radius:20px;padding:18px 22px;font:700 24px 'Montserrat';text-align:center}""")

P["p193_appliance_s2"] = ap(2, "PART 1 · BOOKING FORM", "The model, the photo<br><span>and the problem, up front.</span>",
browser(f'''<div class=bk><b class=t>Book a repair</b>
<div class=pk>{"".join(f'<div class="{"on" if k=="washer" else ""}">{appl(k,60,"#fff" if k=="washer" else "#2251cc")}<span>{n}</span></div>' for k,n in [("washer","Washer"),("dryer","Dryer"),("fridge","Fridge"),("oven","Oven"),("dish","Dishwasher")])}</div>
<div class=f2><div class=fl><small>WHAT'S WRONG?</small><span>Won't drain, water left in the drum</span></div></div>
<div class=f2><div class=fl><small>MODEL NUMBER</small><span>Sample WM-4500</span></div><div class="fl ph">{ic("camera",30)}<span>Label photo added</span></div></div>
<div class=f2><div class=fl><small>ZIP CODE</small><span>Sample 30301</span></div><div class=fl><small>BEST TIME</small><span>Tue, 8 AM-12 PM</span></div></div>
<div class=bt>Request a visit</div></div>''', url="yourrepair.com/book · sample", style="flex:1"),
css=""".vis{display:flex}.bk{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:12px}.bk .t{font:800 32px Montserrat}
.pk{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}.pk div{border:2px solid #dfe4f1;border-radius:18px;padding:12px 4px;display:flex;flex-direction:column;align-items:center;gap:6px}.pk span{font:700 17px 'Open Sans'}
.pk .on{background:#2251cc;border-color:#2251cc;color:#fff}
.f2{flex:1;display:flex;gap:12px}.fl{flex:1;background:#f3f5fa;border-radius:16px;padding:12px 18px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.fl small{font:700 13px 'Open Sans';letter-spacing:2px;color:#7c849a}.fl span{font:600 23px 'Open Sans'}
.fl.ph{flex-direction:row;align-items:center;gap:12px;background:#fff3dc;color:#9a6200}.fl.ph span{font-size:21px}
.bt{background:#d98a00;color:#fff;border-radius:16px;padding:17px;text-align:center;font:700 22px 'Open Sans'}""")

parts = [("Drain pump", "Job 118 · Washer", "Arrives Tue", "a"), ("Door gasket", "Job 121 · Washer", "Arrives Wed", "a"), ("Thermostat", "Job 119 · Fridge", "In the van", "v"), ("Bake element", "Job 123 · Oven", "Ordered today", "o"), ("Belt kit", "Job 120 · Dryer", "In the van", "v")]
P["p193_appliance_s3"] = ap(3, "PART 2 · PARTS ON ORDER", "Every part tied to a job.<br><span>Customers get the date.</span>",
f'''<div class="cd pb"><div class=ph2><small>PARTS BOARD · SAMPLE</small><div class=lgd><span><i class=v></i>In the van</span><span><i class=a></i>Arriving</span><span><i class=o></i>Ordered</span></div></div>
{"".join(f'<div class="prt {k}"><span class=bx>{ic("box",30)}</span><div><b>{a}</b><span>{j}</span></div><em>{s}</em></div>' for a,j,s,k in parts)}
<div class=tx>{ic("send",22)} When a part arrives, the customer gets a text to pick a visit time.</div></div>''',
css=""".vis{display:flex}.pb{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px}
.ph2{display:flex;justify-content:space-between;align-items:center}.ph2 small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#7c849a}
.lgd{display:flex;gap:16px;font:600 16px 'Open Sans'}.lgd span{display:flex;align-items:center;gap:6px}.lgd i{width:16px;height:16px;border-radius:5px}
.lgd .v,.prt.v .bx{background:#2251cc}.lgd .a,.prt.a .bx{background:#d98a00}.lgd .o,.prt.o .bx{background:#9aa3b8}
.prt{flex:1;display:flex;align-items:center;gap:16px;border-bottom:2px solid #f0f2f7}
.bx{width:58px;height:58px;border-radius:16px;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.prt div{flex:1}.prt b{display:block;font:700 25px/1.3 Montserrat}.prt span{font:600 18px 'Open Sans';color:#68708a}
.prt em{font-style:normal;font:700 18px 'Open Sans';border-radius:12px;padding:8px 14px;width:170px;text-align:center;background:#f3f5fa}
.tx{display:flex;gap:10px;align-items:center;background:#14213d;color:#fff;border-radius:16px;padding:14px 18px;font:600 19px 'Open Sans'}.tx svg{flex:none;color:#ffc24d}""")

route = [("8:00 AM", "Job 119 · Fridge", "Thermostat swap", "d"), ("9:45 AM", "Job 120 · Dryer", "Belt kit", "d"), ("11:30 AM", "Job 124 · Dishwasher", "First visit", "n"), ("1:30 PM", "Job 118 · Washer", "Waiting for drain pump", "w"), ("3:15 PM", "Job 125 · Oven", "First visit", "n")]
P["p193_appliance_s4"] = ap(4, "PART 3 · TECH'S DAY", "One day plan<br><span>for every tech.</span>",
f'''<div class="cd rt"><div class=rh><small>TECH 1 · TODAY · SAMPLE</small><b>5 stops</b></div>
{"".join(f'<div class="stp {k}"><time>{t}</time><i></i><div><b>{a}</b><span>{b}</span></div><em>{dict(d="Done",n="Next" if j==2 else "Later",w="Moved")[k]}</em></div>' for j,(t,a,b,k) in enumerate(route))}
<div class=rn>Job 118 moves to Tuesday when the pump arrives. The customer is told automatically.</div></div>''',
css=""".vis{display:flex}.rt{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:6px}
.rh{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}.rh small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#7c849a}.rh b{font:800 26px Montserrat;color:#2251cc}
.stp{flex:1;display:flex;align-items:center;gap:16px;position:relative}
.stp time{width:110px;flex:none;font:700 20px 'Open Sans';color:#68708a;text-align:right}
.stp i{width:22px;height:22px;border-radius:50%;flex:none;border:4px solid #2251cc;background:#fff;position:relative;z-index:2}
.stp.d i{background:#2251cc}.stp.w i{border-color:#d98a00}
.stp:before{content:"";position:absolute;left:135px;top:0;bottom:0;width:4px;background:#e1e6f3}
.stp div{flex:1;background:#f3f5fa;border-radius:16px;padding:10px 16px}.stp b{display:block;font:700 23px/1.3 Montserrat}.stp span{font:600 18px 'Open Sans';color:#68708a}
.stp em{font-style:normal;width:100px;text-align:center;font:700 17px 'Open Sans';border-radius:12px;padding:7px 0;background:#eef2fc;color:#2251cc}
.stp.d em{background:#2251cc;color:#fff}.stp.w em{background:#fff3dc;color:#9a6200}
.rn{background:#fff3dc;color:#7a4e00;border-radius:16px;padding:14px 18px;font:600 19px/1.4 'Open Sans';margin-top:6px}""")

P["p193_appliance_s5"] = ap(5, "YOUR TURN", "Fix washers, fridges<br>and ovens?<br><span>Let's build your repair app.</span>",
f'''<div class=c5><div class=row5>{"".join(f'<div>{appl(k,96)}</div>' for k in ["washer","fridge","dryer","oven","dish"])}</div>
<div class=g4>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("Booking form","Model, photo, ZIP"),("Parts board","Each part tied to a job"),("Day plan","Stops for every tech"),("Customer texts","Dates without phone tag")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#d98a00;color:#fff",
css=""".c5{flex:1;display:flex;flex-direction:column;gap:16px}
.row5{display:flex;gap:12px}.row5 div{flex:1;height:150px;background:#fff;border-radius:24px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 24px rgba(20,33,61,.07)}
.g4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}.g4 div{background:#14213d;color:#fff;border-radius:24px;padding:24px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}
.g4 div:nth-child(2),.g4 div:nth-child(3){background:#2251cc}.g4 b{font:800 34px/1.25 Montserrat}.g4 span{font:500 20px 'Open Sans';color:#d6def5}""")


# ───────── 194 INDIA · Waterproofing contractor · SINGLE · Bitter + Source Sans 3 · storm grey / teal / white
# New technique: top-down SVG terrace plan with numbered crack/leak points + stage photo strip per point.
def terrace():
    Y = 1.5
    pts = [(150, 140, 1, "d"), (390, 110, 2, "d"), (300, 300, 3, "w"), (130, 400, 4, "n"), (430, 420, 5, "n")]
    col = {"d": "#0e8f8a", "w": "#f2a73b", "n": "#e0e4e8"}
    out = ('<svg viewBox="0 0 560 800" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block">'
           '<rect x="20" y="20" width="520" height="760" rx="8" fill="#d9dee3" stroke="#3f4a54" stroke-width="10"/>'
           '<path d="M20 400 H540 M280 20 V780" stroke="#c6ccd2" stroke-width="3" stroke-dasharray="10 8"/>'
           '<rect x="440" y="30" width="90" height="80" fill="#bfc6cd" stroke="#3f4a54" stroke-width="3"/><text x="485" y="76" text-anchor="middle" font-family="Source Sans 3" font-weight="700" font-size="18" fill="#3f4a54"><tspan>Tank</tspan></text>'
           '<circle cx="54" cy="740" r="16" fill="#3f4a54"/><text x="80" y="747" font-family="Source Sans 3" font-weight="700" font-size="18" fill="#3f4a54"><tspan>Drain</tspan></text>'
           '<path d="M160 180 l20 45 l-14 27 l22 39" fill="none" stroke="#3f4a54" stroke-width="3"/><path d="M290 450 l30 21 l-10 36 l28 24" fill="none" stroke="#3f4a54" stroke-width="3"/>')
    for x, y, n, k in pts:
        y = y * Y
        out += (f'<circle cx="{x}" cy="{y}" r="34" fill="{col[k]}" stroke="#fff" stroke-width="5"/>'
                f'<text x="{x}" y="{y+10}" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="30" fill="{"#fff" if k!="n" else "#3f4a54"}"><tspan>{n}</tspan></text>')
    return out + '</svg>'
pl = [("1", "Crack near parapet", "Sealed + 2 coats", "d"), ("2", "Tank base joint", "Sealed + 2 coats", "d"), ("3", "Centre crack", "First coat today", "w"), ("4", "Drain corner", "Wed", "n"), ("5", "Slab joint", "Wed", "n")]
P["p194_waterproof"] = page("""
body{--f:'Source Sans 3';--h:'Bitter';background:#e9edf0;color:#24303a}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:0;line-height:1.22} h1 span{color:#0e8f8a}
.sub{color:#56626d;font-size:23px}
.vis{gap:16px}
.tp{flex:1;background:#fff;border-radius:28px;padding:16px 16px 12px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(36,48,58,.08)}
.tp small{font:700 14px 'Source Sans 3';letter-spacing:2.5px;color:#7d8893;margin-left:6px}.tp .tv{flex:1;min-height:0}
.lgd{display:flex;gap:16px;justify-content:center;font:600 17px 'Source Sans 3'}.lgd span{display:flex;align-items:center;gap:6px}.lgd i{width:16px;height:16px;border-radius:50%}
.rl{width:400px;flex:none;display:flex;flex-direction:column;gap:12px}
.pl{flex:1;background:#24303a;color:#fff;border-radius:28px;padding:18px 20px;display:flex;flex-direction:column;gap:8px}
.pl small{font:700 14px 'Source Sans 3';letter-spacing:2.5px;color:#a9b6c1}
.pr{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid rgba(255,255,255,.12)}
.pr i{width:38px;height:38px;border-radius:50%;font-style:normal;display:flex;align-items:center;justify-content:center;font:800 19px Bitter;flex:none}
.pr.d i{background:#0e8f8a}.pr.w i{background:#f2a73b;color:#24303a}.pr.n i{background:#e0e4e8;color:#24303a}
.pr div{flex:1}.pr b{display:block;font:700 23px/1.35 'Source Sans 3';margin-bottom:3px}.pr span{display:block;font:500 19px/1.35 'Source Sans 3';color:#c4ced6}
.ph3{display:flex;gap:6px}.ph3 em{font-style:normal;font:700 14px 'Source Sans 3';background:#34424e;border-radius:8px;padding:4px 8px;color:#c4ced6}
.cc{background:#0e8f8a;color:#fff;border-radius:22px;padding:16px 20px}.cc small{font:700 13px 'Source Sans 3';letter-spacing:2px;color:#bfeeea}.cc b{display:block;font:800 24px/1.3 Bitter}.cc span{font:500 17px/1.35 'Source Sans 3'}
""", "<h1>Leak fixed on which spot?<br><span>Keep a record per point.</span></h1><div class=sub>Mark every crack, add photos at each stage, share one report.</div>",
f'''<div class=tp><small>TERRACE PLAN · SAMPLE SITE</small><div class=tv>{terrace()}</div>
<div class=lgd><span><i style="background:#0e8f8a"></i>Done</span><span><i style="background:#f2a73b"></i>In progress</span><span><i style="background:#e0e4e8;border:2px solid #9aa5ae"></i>Planned</span></div></div>
<div class=rl><div class=pl><small>POINTS · PHOTOS PER STAGE</small>{"".join(f'<div class="pr {k}"><i>{n}</i><div><b>{a}</b><span>{s}</span></div></div>' for n,a,s,k in pl)}
<div class=ph3>{"".join(f'<em>{ic("camera",14)} {t}</em>' for t in ["Before", "After clean", "After coat"])}</div></div>
<div class=cc><small>SHARED WITH THE CLIENT</small><b>One report link</b><span>Points, photos and the next check date you set.</span></div></div>''',
"#24303a", "Do waterproofing work? DM us", "background:#0e8f8a;color:#fff")


# ───────── 195 INDIA · Self-drive car rental · SINGLE · Anton + Inter · black / racing red / silver
# New technique: pickup vs return dashboard gauges (odometer + fuel needle) side by side.
def gauge(fuel, km, lbl):
    import math
    a = math.radians(180 - fuel * 180)
    x, y = 150 + 104 * math.cos(a), 150 - 104 * math.sin(a)
    return (f'<svg viewBox="0 0 300 220" width="100%" style="display:block"><path d="M30 150 A120 120 0 0 1 270 150" fill="none" stroke="#3a3a3f" stroke-width="22" stroke-linecap="round"/>'
            f'<path d="M30 150 A120 120 0 0 1 270 150" fill="none" stroke="#e63946" stroke-width="22" stroke-linecap="round" stroke-dasharray="{fuel*377} 400"/>'
            f'<line x1="150" y1="150" x2="{x:.1f}" y2="{y:.1f}" stroke="#fff" stroke-width="6" stroke-linecap="round"/><circle cx="150" cy="150" r="12" fill="#fff"/>'
            f'<text x="34" y="190" font-family="Inter" font-weight="700" font-size="18" fill="#9a9aa3"><tspan>E</tspan></text><text x="256" y="190" font-family="Inter" font-weight="700" font-size="18" fill="#9a9aa3"><tspan>F</tspan></text>'
            f'<rect x="80" y="176" width="140" height="40" rx="8" fill="#000"/><text x="150" y="204" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="22" fill="#f1f1f1"><tspan>{km}</tspan></text></svg>')
P["p195_carrental"] = page("""
body{--f:'Inter';--h:'Anton';background:#121214;color:#f4f4f5}
h1{font-family:'Anton';font-size:70px;font-weight:400;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#e63946}
.sub{color:#b3b3bb;font-size:23px}
.vis{flex-direction:column;gap:16px}
.gg{display:flex;gap:16px}
.gc{flex:1;background:#1f1f23;border-radius:28px;padding:18px 20px;display:flex;flex-direction:column;gap:8px;border:2px solid #2d2d33}
.gc small{font:700 14px 'Inter';letter-spacing:2.5px;color:#9a9aa3}.gc h3{font:400 34px/1.35 Anton;margin-bottom:6px}
.gc .rw{display:flex;justify-content:space-between;font:600 19px 'Inter';color:#d4d4d8}.gc .rw b{color:#fff}
.gc.rt{border-color:#e63946}
.sm{flex:1;background:#f4f4f5;color:#121214;border-radius:28px;padding:20px 24px;display:flex;flex-direction:column;gap:10px}
.sm small{font:700 14px 'Inter';letter-spacing:2.5px;color:#71717a}
.sr{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #e4e4e7;font:600 21px 'Inter'}.sr b{font:400 30px/1.35 Anton}
.sr.r b{color:#e63946}
.dk{display:flex;gap:10px}.dk span{flex:1;background:#121214;color:#fff;border-radius:14px;padding:12px;text-align:center;font:700 17px 'Inter';display:flex;align-items:center;justify-content:center;gap:8px}
""", "<h1>Fuel and km disputes<br><span>at car return?</span></h1>",
f'''<div class=gg><div class=gc><small>PICKUP · FRI 9:00 AM</small><h3>Car 4 · sample</h3>{gauge(.75,"48,210 km","pickup")}<div class=rw><span>Fuel</span><b>3/4 tank</b></div><div class=rw><span>Photos</span><b>8 added</b></div></div>
<div class="gc rt"><small>RETURN · SUN 7:30 PM</small><h3>Car 4 · sample</h3>{gauge(.5,"48,846 km","return")}<div class=rw><span>Fuel</span><b>1/2 tank</b></div><div class=rw><span>Photos</span><b>8 added</b></div></div></div>
<div class=sm><small>TRIP SUMMARY · SENT TO THE CUSTOMER · SAMPLE</small>
<div class=sr><span>Distance driven</span><b>636 km</b></div><div class=sr><span>Trip length</span><b>2 days, 10.5 h</b></div><div class="sr r"><span>Fuel to top up</span><b>1/4 tank</b></div>
<div class=dk>{"".join(f'<span>{ic("check",18,w=3)} {t}</span>' for t in ["Licence checked", "ID checked", "Deposit noted"])}</div></div>''',
"#f4f4f5", "Rent out self-drive cars? DM us", "background:#e63946;color:#fff", logo_color="#ffffff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
