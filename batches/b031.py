import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 171 INDIA · Furniture rental · SINGLE · Gelasio + DM Sans · walnut / linen / cobalt
# New technique: split owner vs customer view of the same rental (owner item ledger card | customer phone page), joined by a cobalt "same data" seam.
items = [("sofa", "3-seater sofa", "Since 1 Aug"), ("bed", "Queen bed + mattress", "Since 1 Aug"), ("table", "Study table + chair", "Since 15 Sep"), ("fridge", "Fridge 190 L", "Since 15 Sep")]
def fic(k):
    d = {"sofa": '<rect x="6" y="18" width="52" height="22" rx="6" fill="#8a5a3b"/><rect x="2" y="24" width="10" height="20" rx="4" fill="#6e4429"/><rect x="52" y="24" width="10" height="20" rx="4" fill="#6e4429"/><rect x="10" y="10" width="44" height="14" rx="5" fill="#a87452"/>',
         "bed": '<rect x="4" y="26" width="56" height="16" rx="4" fill="#8a5a3b"/><rect x="4" y="12" width="10" height="30" rx="3" fill="#6e4429"/><rect x="16" y="20" width="16" height="8" rx="3" fill="#f4ede2"/>',
         "table": '<rect x="4" y="18" width="40" height="6" rx="2" fill="#8a5a3b"/><path d="M8 24 V46 M40 24 V46" stroke="#6e4429" stroke-width="4"/><rect x="46" y="26" width="14" height="4" rx="2" fill="#a87452"/><path d="M48 30 V46 M58 30 V46 M58 30 V12" stroke="#6e4429" stroke-width="3"/>',
         "fridge": '<rect x="18" y="4" width="28" height="44" rx="5" fill="#d9dde6" stroke="#6e4429" stroke-width="3"/><path d="M18 20 H46 M40 10 V16 M40 26 V34" stroke="#6e4429" stroke-width="3"/>'}[k]
    return f'<svg viewBox="0 0 64 50" width="64" style="display:block">{d}</svg>'
P["p171_furn"] = page("""
body{--f:'DM Sans';--h:'Gelasio';background:#f4ede2;color:#3b2a1e}
h1{font-family:'Gelasio';font-size:60px;font-weight:700;letter-spacing:-.4px;line-height:1.22} h1 span{color:#2f55d4}
.sub{color:#6b5a4b;font-size:23px}
.vis{gap:0;align-items:stretch}
.side{display:flex;flex-direction:column;gap:12px}
.lab{font:700 15px 'DM Sans';letter-spacing:3px;color:#8a7461}
.ow{flex:1;background:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(59,42,30,.08)}
.ow h3{font:700 28px/1.25 Gelasio}.ow .s{font:600 18px 'DM Sans';color:#8a7461}
.it{flex:1;display:flex;align-items:center;gap:14px;border-top:1.5px solid #efe6d8}.it .ic{width:76px;height:60px;border-radius:14px;background:#f4ede2;display:flex;align-items:center;justify-content:center;flex:none}
.it b{display:block;font:700 24px 'DM Sans'}.it span{font:500 19px 'DM Sans';color:#8a7461}
.dues{display:grid;grid-template-columns:1fr 1fr;gap:10px}.dues div{background:#3b2a1e;color:#fff;border-radius:16px;padding:12px 14px}.dues small{display:block;font:700 13px 'DM Sans';letter-spacing:2px;color:#d9c4ad}.dues b{font:700 22px 'DM Sans'}
.seam{width:64px;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px}
.seam i{flex:1;width:4px;background:repeating-linear-gradient(#2f55d4 0 10px,transparent 10px 18px)}
.seam span{width:52px;height:52px;border-radius:50%;background:#2f55d4;color:#fff;display:flex;align-items:center;justify-content:center}
.cu{display:flex;flex-direction:column;padding:6px 16px 16px;gap:9px;flex:1}
.cu small{font:700 12px 'DM Sans';letter-spacing:2px;color:#8a7461}.cu .h{font:700 24px/1.25 Gelasio}
.cu .nx{background:#2f55d4;color:#fff;border-radius:16px;padding:12px 14px}.cu .nx small{color:#c9d5ff}.cu .nx b{display:block;font:700 22px 'DM Sans'}
.cu .r{flex:1;display:flex;align-items:center;gap:10px;background:#f6f1e9;border-radius:14px;padding:0 10px;font:600 16px 'DM Sans'}.cu .r .ic{transform:scale(.8)}
.cu .bt{display:flex;gap:8px}.cu .bt i{flex:1;font-style:normal;text-align:center;font:700 15px 'DM Sans';border-radius:12px;padding:11px 4px;background:#3b2a1e;color:#fff}.cu .bt i:last-child{background:#efe6d8;color:#3b2a1e}
""", "<h1>Rented 4 items to Flat 304.<br><span>Who sees what's due?</span></h1><div class=sub>You and your customer see the same items, dates and requests.</div>",
f'''<div class=side style="flex:1"><div class=lab>YOUR VIEW</div><div class=ow><h3>Flat 304 · Sample Tower</h3><div class=s>Customer: Sample Tenant · 4 items</div>
{"".join(f'<div class=it><div class=ic>{fic(k)}</div><div><b>{a}</b><span>{d}</span></div></div>' for k,a,d in items)}
<div class=dues><div><small>RENT DUE</small><b>1 Dec · auto reminder</b></div><div><small>REQUEST</small><b>Sofa cleaning, Sat</b></div></div></div></div>
<div class=seam><i></i><span>{ic("arrow",26,w=3)}</span><i></i></div>
<div class=side><div class=lab>CUSTOMER'S VIEW</div>{phone(f"""<div class=cu><small>MY RENTALS · SAMPLE</small><div class=h>Hi, Sample Tenant</div><div class=nx><small>NEXT RENT DATE</small><b>1 December</b></div>{"".join(f'<div class=r><span class=ic>{fic(k)}</span>{a}</div>' for k,a,d in items)}<div class=bt><i>Request service</i><i>Plan pickup</i></div></div>""", w=350, h=735)}</div>''',
"#3b2a1e", "Rent out furniture? DM us", "background:#2f55d4;color:#fff")


# ───────── 172 INDIA · Solar water heater dealer · CAROUSEL 5 · Archivo Black + Roboto · midnight blue / sun gold / cloud white
# New techniques: SVG rooftop with solar water heater (tank + tube rows), annotated paper survey form with handwriting-style ticks, crew week strip, yearly service ring list.
SW = """
body{--f:'Roboto';--h:'Archivo Black';background:#13204a;color:#fff}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-.6px;line-height:1.22;margin-top:30px} h1 span{color:#ffc53d}
.kk{font:700 16px Roboto;letter-spacing:3px;color:#ffc53d;margin-top:22px}
.cd{background:#f6f8fc;color:#13204a;border-radius:26px}
"""
def sw(n, head, vis, css="", cta="Swipe", ctacss="background:#ffc53d;color:#13204a"):
    return page(SW + css, head, vis, "#ffffff", cta, ctacss, tagline=f"{n} / 5", logo_color="#ffffff")
def roof(w=760):
    tubes = "".join(f'<rect x="{250+i*24}" y="150" width="16" height="130" rx="8" fill="#2b3f7d" stroke="#8fa6e6" stroke-width="2"/>' for i in range(12))
    return (f'<svg viewBox="0 0 760 420" width="{w}" style="display:block"><circle cx="660" cy="70" r="46" fill="#ffc53d"/>'
            + "".join(f'<path d="M660 70 L{660+80*__import__("math").cos(a/57.3):.0f} {70+80*__import__("math").sin(a/57.3):.0f}" stroke="#ffc53d" stroke-width="5" stroke-linecap="round" opacity=".55"/>' for a in range(0, 360, 45))
            + '<path d="M0 330 L760 330 L760 420 L0 420 Z" fill="#c9d3ea"/><rect x="60" y="300" width="640" height="30" fill="#8a97b8"/>'
            + '<path d="M230 300 L270 150 M540 300 L520 150" stroke="#13204a" stroke-width="8"/>'
            + f'{tubes}<rect x="236" y="104" width="300" height="56" rx="28" fill="#e9edf6" stroke="#13204a" stroke-width="5"/><text x="386" y="142" text-anchor="middle" font-family="Archivo Black" font-size="24" fill="#13204a"><tspan>200 L TANK</tspan></text>'
            + '<path d="M536 132 Q600 132 600 220 L600 300" fill="none" stroke="#e0533d" stroke-width="7"/><path d="M236 140 Q170 140 170 220 L170 300" fill="none" stroke="#3d8be0" stroke-width="7"/></svg>')
P["p172_solar_s1"] = sw(1, "<div class=kk>SOLAR WATER HEATER DEALERS</div><h1>Installed 40 heaters.<br><span>Who reminds them next year?</span></h1>",
f'''<div class="cd hero">{roof()}</div><div class=pl>{"".join(f'<div class={k}><b>{a}</b><span>{b}</span></div>' for a,b,k in [("6","site surveys","a"),("4","installs this week","b"),("40","on service list","c")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.hero{flex:1;display:flex;align-items:center;justify-content:center;padding:20px;background:linear-gradient(#dfe8fb,#f6f8fc)}
.pl{display:flex;gap:14px}.pl div{flex:1;border-radius:22px;padding:18px 20px;background:#22336b}.pl .c{background:#ffc53d;color:#13204a}.pl b{display:block;font:400 52px/1.3 'Archivo Black'}.pl span{font:600 20px Roboto}""")

qs = [("Roof type", "RCC flat roof", 1), ("Floor", "Ground + 2 floors", 1), ("Water source", "Overhead tank, soft water", 1), ("People using hot water", "4", 1),
      ("Suggested size", "200 L, as per your size chart", 1), ("Space on roof", "Clear, south side", 1)]
P["p172_solar_s2"] = sw(2, "<div class=kk>PART 1 · SITE SURVEY</div><h1>No more survey notes<br><span>on loose paper.</span></h1>",
f'''<div class=fm><div class=fh><div><small>SITE SURVEY · SAMPLE</small><b>Sample House 21</b></div><em>Fri, 27 Nov · 11 AM</em></div>
{"".join(f'<div class=q><span>{a}</span><b>{b}</b><i>{ic("check",22,w=3)}</i></div>' for a,b,_ in qs)}
<div class=ph2>{"".join(f'<div>{ic("camera",30)}<span>{t}</span></div>' for t in ["Roof","Tank","Pipe route"])}</div></div>''',
css=""".vis{display:flex}.fm{flex:1;background:#fffdf6;color:#13204a;border-radius:8px;padding:22px 26px;display:flex;flex-direction:column;gap:6px;box-shadow:0 20px 40px rgba(0,0,0,.25);background-image:repeating-linear-gradient(#fffdf6 0 63px,#dfe6f5 63px 65px)}
.fh{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6px}.fh small{display:block;font:700 14px Roboto;letter-spacing:2.5px;color:#7a88ad}.fh b{font:400 30px/1.3 'Archivo Black'}
.fh em{font-style:normal;font:700 18px Roboto;background:#13204a;color:#ffc53d;border-radius:12px;padding:8px 14px}
.q{flex:1;display:flex;align-items:center;gap:14px}.q span{width:270px;font:600 20px Roboto;color:#5d6b90}.q b{flex:1;font:700 24px Roboto}
.q i{width:38px;height:38px;border-radius:50%;background:#ffc53d;color:#13204a;display:flex;align-items:center;justify-content:center;flex:none}
.ph2{display:flex;gap:12px;margin-top:8px}.ph2 div{flex:1;background:#e8edf8;border-radius:16px;padding:14px;display:flex;align-items:center;gap:12px;font:700 20px Roboto}""")

crew = [("Mon 30", "Crew 1", "Sample House 21", "200 L"), ("Tue 1", "Crew 2", "Sample Villa 6", "300 L"), ("Wed 2", "Crew 1", "Sample Hostel", "500 L"),
        ("Thu 3", "Crew 2", "Sample Flat 2", "100 L"), ("Fri 4", "Keep open", "Free day", "")]
P["p172_solar_s3"] = sw(3, "<div class=kk>PART 2 · INSTALL WEEK</div><h1>Which crew goes where,<br><span>with which tank?</span></h1>",
f'''<div class="cd wk">{"".join(f'<div class="dy {"fr" if not z else ""}"><div class=dd>{d}</div><div class=dt><b>{s}</b><span>{c}{(" · " + z) if z else ""}</span></div>{"<em>Material packed</em>" if z else "<em class=op>Open for urgent jobs</em>"}</div>' for d,c,s,z in crew)}</div>''',
css=""".vis{display:flex}.wk{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.dy{flex:1;display:flex;align-items:center;gap:18px;background:#fff;border-radius:20px;padding:0 20px;box-shadow:0 8px 20px rgba(19,32,74,.06)}
.dd{width:140px;white-space:nowrap;font:400 28px/1.3 'Archivo Black';color:#13204a}.dt{flex:1}.dt b{display:block;font:700 26px Roboto}.dt span{font:500 20px Roboto;color:#5d6b90}
.dy em{font-style:normal;font:700 17px Roboto;background:#ffe9a8;color:#5c4300;border-radius:12px;padding:8px 14px}.dy em.op{background:#e8edf8;color:#5d6b90}
.dy.fr{background:transparent;border:3px dashed #b8c4e0;box-shadow:none}""")

svc = [("Sample House 3", "Installed Dec 2025", "Due in Dec", 92, "due"), ("Sample Villa 9", "Installed Jan 2026", "Due in Jan", 84, "soon"), ("Sample Hotel", "Installed Mar 2026", "Due in Mar", 68, "ok"),
       ("Sample Flat 14", "Installed Jun 2026", "Due in Jun", 42, "ok")]
P["p172_solar_s4"] = sw(4, "<div class=kk>PART 3 · YEARLY SERVICE</div><h1>A reminder goes out<br><span>before the service is due.</span></h1>",
f'''<div class="cd sv">{"".join(f'<div class=sr><svg viewBox="0 0 80 80" width="84"><circle cx="40" cy="40" r="32" fill="none" stroke="#e3e8f4" stroke-width="10"/><circle cx="40" cy="40" r="32" fill="none" stroke="{dict(due="#e0533d",soon="#ffc53d",ok="#3d8be0")[k]}" stroke-width="10" stroke-linecap="round" stroke-dasharray="{p*2.01:.0f} 300" transform="rotate(-90 40 40)"/></svg><div><b>{a}</b><span>{i}</span></div><em class={k}>{d}</em></div>' for a,i,d,p,k in svc)}
<div class=nt>Customers get a message 2 weeks before, with a link to <b>pick a visit date</b>.</div></div>''',
css=""".vis{display:flex}.sv{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:12px}
.sr{flex:1;display:flex;align-items:center;gap:18px;background:#fff;border-radius:20px;padding:0 20px}.sr div{flex:1}.sr b{display:block;font:700 27px Roboto}.sr span{font:500 20px Roboto;color:#5d6b90}
.sr em{font-style:normal;font:700 18px Roboto;border-radius:12px;padding:8px 14px}.sr .due{background:#fde1dc;color:#a8321c}.sr .soon{background:#ffe9a8;color:#5c4300}.sr .ok{background:#e1ecfb;color:#24508f}
.nt{background:#13204a;color:#fff;border-radius:20px;padding:18px 22px;font:500 21px/1.45 Roboto}.nt b{color:#ffc53d}""")

P["p172_solar_s5"] = sw(5, "<div class=kk>YOUR TURN</div><h1>Sell solar water heaters?<br><span>Let's build your dealer app.</span></h1>",
f'''<div class="cd hero">{roof(700)}</div><div class=g4>{"".join(f'<div><span class=ib>{ic(i,28)}</span><b>{a}</b></div>' for i,a in [("doc","Site survey"),("cal","Install week"),("bell","Service reminders"),("users","Customer list")])}</div>''',
css=""".vis{flex-direction:column;gap:16px}.hero{flex:1;display:flex;align-items:center;justify-content:center;padding:20px;background:linear-gradient(#dfe8fb,#f6f8fc)}
.g4{display:grid;grid-template-columns:1fr 1fr;gap:14px}.g4 div{background:#22336b;border-radius:22px;padding:24px 22px;display:flex;align-items:center;gap:16px}
.g4 .ib{width:58px;height:58px;border-radius:16px;background:#ffc53d;color:#13204a}.g4 b{font:700 26px Roboto}""",
cta="DM us to start")


# ───────── 173 USA · Mobile car wash · SINGLE · Montserrat + Source Sans 3 · aqua / hot coral / white
# New technique: hexagon zone map (CSS clip-path hexes) where each zone has a wash day; the picked zone opens a slot picker.
zones = [("Zone 1", "Mon", 0, 0, ""), ("Zone 2", "Tue", 1, 0, ""), ("Zone 3", "Wed", 2, 0, ""), ("Zone 4", "Thu", 0.5, 1, "on"), ("Zone 5", "Fri", 1.5, 1, ""), ("Zone 6", "Sat", 1, 2, ""), ("Outside", "Not served", 2.5, 1, "off")]
P["p173_carwash"] = page("""
body{--f:'Source Sans 3';--h:'Montserrat';background:#d9f4f2;color:#0d2a3a}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.2px;line-height:1.2} h1 span{color:#f0565b}
.sub{color:#3e5a66;font-size:24px}
.vis{flex-direction:column;gap:16px}
.mp{flex:1;background:#fff;border-radius:28px;padding:16px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 16px 34px rgba(13,42,58,.08)}
.mp small{font:700 14px 'Source Sans 3';letter-spacing:2.5px;color:#7a959e}
.hx{flex:1;position:relative}
.h{position:absolute;width:250px;height:217px;clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%);background:#a9e4df;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.h b{font:800 30px Montserrat}.h span{font:700 23px 'Source Sans 3'}
.h.on{background:#f0565b;color:#fff}.h.off{background:#eef2f3;color:#9aa9ae}
.sl{background:#0d2a3a;color:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.sl .t{display:flex;justify-content:space-between;align-items:baseline}.sl .t b{font:800 26px Montserrat}.sl .t span{font:600 19px 'Source Sans 3';color:#9cc7cf}
.sl .s{display:flex;gap:10px}.sl .s i{flex:1;font-style:normal;text-align:center;font:700 20px 'Source Sans 3';border-radius:14px;padding:14px 0;background:rgba(255,255,255,.1)}
.sl .s i.on{background:#f0565b}.sl .s i.x{background:transparent;border:2px dashed rgba(255,255,255,.25);color:#7f9aa3;text-decoration:line-through}
""", "<h1>Driving across town<br>for one car wash?<br><span>Give each area its own day.</span></h1>",
f'''<div class=mp><small>SERVICE AREA BY DAY · SAMPLE CITY · TAP YOUR ZIP CODE</small><div class=hx>{"".join(f'<div class="h {k}" style="left:{60+x*198}px;top:{6+y*190}px"><b>{z}</b><span>{d}</span></div>' for z,d,x,y,k in zones)}</div></div>
<div class=sl><div class=t><b>ZIP 85250 · Zone 4 · Thursday</b><span>Pick a time</span></div><div class=s>{"".join(f'<i class="{k}">{t}</i>' for t,k in [("8 AM","x"),("10 AM","on"),("12 PM",""),("2 PM","x"),("4 PM","")])}</div></div>''',
"#0d2a3a", "Run a mobile car wash? DM us", "background:#0d2a3a;color:#fff")


# ───────── 174 INDIA · Plumbing & sanitaryware contractor · SINGLE · Bitter + Inter · porcelain / charcoal / leaf green
# New technique: bathroom wall elevation SVG with numbered fitting points (fitted / pending / material short) + per-site material list.
pts = [(1, 120, 180, "f"), (2, 255, 300, "f"), (3, 420, 150, "p"), (4, 470, 330, "s"), (5, 140, 400, "p")]
PC = {"f": ("#2e9e5b", "Fitted"), "p": ("#f2f2ee", "Pending"), "s": ("#e8833a", "Material short")}
lst = [(1, "Shower mixer", "Fitted", "f"), (2, "Wash basin + tap", "Fitted", "f"), (3, "Geyser point", "Pending · Sat", "p"), (4, "WC + flush tank", "Short: flush valve", "s"), (5, "Floor drain", "Pending · Sat", "p")]
def bath():
    s = ('<svg viewBox="0 0 560 760" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block">'
         + "".join(f'<rect x="{x}" y="{y}" width="68" height="68" fill="#f7f7f3" stroke="#d9dbd4" stroke-width="2"/>' for x in range(10, 550, 68) for y in range(10, 720, 68))
         + '<rect x="0" y="710" width="560" height="50" fill="#5b6066"/><g transform="translate(0,240)">'
         + '<path d="M120 60 V150 M100 60 H140" stroke="#3a3f45" stroke-width="8" stroke-linecap="round"/><circle cx="120" cy="56" r="26" fill="#c9cdd2"/>'
         + '<rect x="200" y="260" width="120" height="44" rx="20" fill="#fff" stroke="#3a3f45" stroke-width="5"/><path d="M260 260 V236 H284" stroke="#3a3f45" stroke-width="7" stroke-linecap="round"/>'
         + '<rect x="370" y="80" width="100" height="120" rx="16" fill="#fff" stroke="#3a3f45" stroke-width="5" stroke-dasharray="12 8"/>'
         + '<rect x="420" y="260" width="96" height="60" rx="10" fill="#fff" stroke="#3a3f45" stroke-width="5"/><path d="M430 320 Q430 420 468 420 Q506 420 506 320" fill="#fff" stroke="#3a3f45" stroke-width="5"/>'
         + '<rect x="110" y="440" width="60" height="16" rx="6" fill="#3a3f45"/>')
    for n, x, y, k in pts:
        s += f'<g><circle cx="{x}" cy="{y}" r="26" fill="{PC[k][0]}" stroke="#3a3f45" stroke-width="4"/><text x="{x}" y="{y+9}" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="{"#fff" if k!="p" else "#3a3f45"}"><tspan>{n}</tspan></text></g>'
    return s + '</g></svg>'
P["p174_plumb"] = page("""
body{--f:'Inter';--h:'Bitter';background:#eceee8;color:#2c3136}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:-.8px;line-height:1.2} h1 span{color:#2e9e5b}
.sub{color:#5b6066;font-size:23px}
.vis{gap:18px}
.el{flex:1;background:#fff;border-radius:28px;padding:16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 16px 34px rgba(44,49,54,.08)}
.el small{font:700 14px Inter;letter-spacing:2.5px;color:#8b9197;padding:4px 6px 0}.el .bx{flex:1;min-height:0;display:flex}.el .bx svg{flex:1}
.lg{display:flex;gap:14px;padding:0 6px 4px;font:600 16px Inter}.lg span{display:flex;gap:6px;align-items:center}.lg i{width:18px;height:18px;border-radius:50%;border:2px solid #3a3f45}
.ls{width:370px;flex:none;display:flex;flex-direction:column;gap:10px}
.ls .hd{background:#2c3136;color:#fff;border-radius:20px;padding:16px 18px}.ls .hd small{display:block;font:700 13px Inter;letter-spacing:2px;color:#a9b7ad}.ls .hd b{font:800 24px/1.3 Bitter}
.rw{flex:1;background:#fff;border-radius:18px;display:flex;align-items:center;gap:12px;padding:0 14px}
.rw i{width:40px;height:40px;border-radius:50%;flex:none;display:flex;align-items:center;justify-content:center;font:800 19px Inter;font-style:normal;border:3px solid #3a3f45}
.rw b{display:block;font:700 20px Inter}.rw span{font:600 16px Inter}.rw .f{color:#2e9e5b}.rw .p{color:#6b7178}.rw .s{color:#c2621c}
""", "<h1>Site has 5 fittings.<br><span>Which are still pending?</span></h1><div class=sub>Mark each point on the wall, and the shop list fills itself.</div>",
f'''<div class=el><small>SAMPLE FLAT 802 · BATHROOM 1</small><div class=bx>{bath()}</div><div class=lg>{"".join(f'<span><i style="background:{c}"></i>{t}</span>' for c,t in PC.values())}</div></div>
<div class=ls><div class=hd><small>SITE: SAMPLE FLAT 802</small><b>2 fitted · 2 pending · 1 short</b></div>{"".join(f'<div class=rw><i style="background:{PC[k][0]};color:{"#fff" if k!="p" else "#3a3f45"}">{n}</i><div><b>{a}</b><span class={k}>{s}</span></div></div>' for n,a,s,k in lst)}</div>''',
"#2c3136", "Plumbing contractor? DM us", "background:#2e9e5b;color:#fff")


# ───────── 175 INDIA · Event management company · CAROUSEL 5 · Cardo + Inter · aubergine / peach / white
# New techniques: minute-by-minute run sheet as a vertical clock rail, vendor board with confirm/pending stamps, team checklist columns.
EV = """
body{--f:'Inter';--h:'Cardo';background:#3a1f3d;color:#fff}
h1{font-family:'Cardo';font-weight:700;font-size:64px;letter-spacing:-.4px;line-height:1.2} h1 span{color:#ffb38a;font-style:italic}
.kk{font:700 16px Inter;letter-spacing:3px;color:#ffb38a;margin-top:22px}
.cd{background:#fff;color:#3a1f3d;border-radius:26px}
"""
def ev(n, head, vis, css="", cta="Swipe", ctacss="background:#ffb38a;color:#3a1f3d"):
    return page(EV + css, head, vis, "#ffffff", cta, ctacss, tagline=f"{n} / 5", logo_color="#ffffff")
run = [("4:00 PM", "Venue open, decor check", "Decor team", "dn"), ("5:30 PM", "Sound and light test", "Sound vendor", "dn"), ("6:30 PM", "Guest entry, welcome desk", "Team A", "now"),
       ("7:15 PM", "Stage program starts", "Anchor", "nx"), ("8:30 PM", "Dinner opens", "Caterer", "nx"), ("10:30 PM", "Pack-up, vendor sign-off", "All", "nx")]
P["p175_event_s1"] = ev(1, "<div class=kk>EVENT MANAGEMENT COMPANIES</div><h1>Event day, 12 vendors,<br><span>one run sheet.</span></h1>",
f'''<div class="cd rs"><div class=rh><b>Run sheet · Sample Annual Meet</b><em>Sat, 12 Dec · Sample Lawns</em></div>{"".join(f'<div class="rr {k}"><span class=tm>{t}</span><i></i><div><b>{a}</b><small>{w}</small></div>{"<em>Now</em>" if k=="now" else ""}</div>' for t,a,w,k in run)}</div>''',
css=""".vis{display:flex}.rs{flex:1;padding:22px 26px;display:flex;flex-direction:column}
.rh{display:flex;justify-content:space-between;align-items:baseline;margin-bottom:8px}.rh b{font:700 32px Cardo}.rh em{font-style:normal;font:600 18px Inter;color:#8a6f8c}
.rr{flex:1;display:flex;align-items:center;gap:18px;position:relative}.rr .tm{width:120px;font:700 23px Inter;text-align:right}
.rr i{width:26px;height:26px;border-radius:50%;flex:none;border:4px solid #3a1f3d;background:#fff;position:relative;z-index:1}
.rr:not(:last-child):after{content:'';position:absolute;left:150px;top:50%;height:100%;width:4px;background:#ead9e9}
.rr.dn i{background:#3a1f3d}.rr.now i{background:#ff8a5c;border-color:#ff8a5c;box-shadow:0 0 0 8px #ffe3d6}
.rr div{flex:1}.rr b{display:block;font:600 24px Inter}.rr small{font:500 18px Inter;color:#8a6f8c}.rr.dn b{color:#8a6f8c}
.rr em{font-style:normal;font:700 17px Inter;background:#ff8a5c;color:#fff;border-radius:12px;padding:7px 14px}""")

vend = [("Decor", "Sample Decor Co.", "Confirmed", "c"), ("Sound and light", "Sample Sound", "Confirmed", "c"), ("Caterer", "Sample Caterers", "Menu final on Mon", "p"),
        ("Photo and video", "Sample Studio", "Confirmed", "c"), ("Anchor", "Sample Anchor", "Script sent", "p"), ("Return gifts", "Sample Gifts", "Not booked", "x")]
P["p175_event_s2"] = ev(2, "<div class=kk>PART 1 · VENDORS</div><h1>Who is confirmed?<br><span>See every vendor at once.</span></h1>",
f'''<div class=vg>{"".join(f'<div class="vc {k}"><small>{a.upper()}</small><b>{v}</b><em>{s}</em></div>' for a,v,s,k in vend)}</div>''',
css=""".vis{display:flex}.vg{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:14px}
.vc{background:#fff;color:#3a1f3d;border-radius:24px;padding:22px;display:flex;flex-direction:column;justify-content:space-between}
.vc small{font:700 14px Inter;letter-spacing:2.5px;color:#8a6f8c}.vc b{font:700 32px/1.2 Cardo}
.vc em{align-self:flex-start;font-style:normal;font:700 18px Inter;border-radius:12px;padding:8px 14px;border:3px solid}
.vc.c em{color:#2e8a57;border-color:#2e8a57;transform:rotate(-3deg)}.vc.p em{color:#b86a00;border-color:#e9a23b}.vc.x{background:#4d2b51;color:#fff;border:3px dashed #ffb38a}.vc.x small{color:#e0c5e0}.vc.x em{color:#ffb38a;border-color:#ffb38a}""")

teams = [("Decor team", ["Stage backdrop", "Entry arch", "Table flowers"], [1, 1, 0]), ("Guest desk", ["Guest list printed", "Name badges", "Seating chart"], [1, 0, 0]),
         ("Food team", ["Menu final", "Counters plan", "Water and ice"], [0, 1, 0])]
P["p175_event_s3"] = ev(3, "<div class=kk>PART 2 · TEAM TASKS</div><h1>Every team knows<br><span>what is left to do.</span></h1>",
f'''<div class=tc>{"".join(f'<div class="cd tt"><b>{t}</b><span class=cnt>{sum(d)} of {len(d)} done</span>' + "".join(f'<div class="tk {"d" if x else ""}"><i>{ic("check",20,w=3) if x else ""}</i><span>{a}</span></div>' for a,x in zip(L,d)) + '</div>' for t,L,d in teams)}</div>''',
css=""".vis{display:flex}.tc{flex:1;display:flex;gap:14px}.tt{flex:1;padding:22px 18px;display:flex;flex-direction:column;gap:10px}
.tt>b{font:700 32px/1.2 Cardo}.cnt{align-self:flex-start;font:700 16px Inter;background:#ffe3d6;color:#a8461c;border-radius:10px;padding:5px 12px}
.tk{flex:1;display:flex;flex-direction:column;justify-content:center;gap:10px;border-top:2px solid #f1e6f0}
.tk i{width:38px;height:38px;border-radius:10px;border:3px solid #3a1f3d;display:flex;align-items:center;justify-content:center;color:#fff}.tk.d i{background:#3a1f3d}
.tk span{font:600 22px/1.3 Inter}.tk.d span{color:#8a6f8c;text-decoration:line-through}""")

P["p175_event_s4"] = ev(4, "<div class=kk>PART 3 · CLIENT VIEW</div><h1>Clients stop calling<br><span>to ask, “Is it all set?”</span></h1>",
browser(f'''<div class=cv><small>SAMPLE ANNUAL MEET · CLIENT PAGE</small><b class=t>Your event is 3 weeks away</b>
<div class=pr><div style="width:72%"></div></div><span class=pl>72% of tasks done</span>
<div class=cg>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a,b in [("VENDORS","4 of 6 confirmed"),("GUESTS","230 confirmed"),("YOUR APPROVAL","Stage design, by Wed"),("NEXT MEETING","Mon, 30 Nov · 5 PM")])}</div>
<div class=ap><span>Stage design v2 is ready</span><i>Approve</i></div></div>''', url="yourevents.in/client · sample", style="flex:1"),
css=""".vis{display:flex}.cv{flex:1;padding:24px 28px;display:flex;flex-direction:column;gap:12px;color:#3a1f3d}
.cv>small{font:700 14px Inter;letter-spacing:2.5px;color:#8a6f8c}.cv .t{font:700 40px/1.2 Cardo}
.pr{height:22px;border-radius:11px;background:#f1e6f0;overflow:hidden}.pr div{height:100%;background:#ff8a5c;border-radius:11px}.pl{font:600 19px Inter;color:#8a6f8c}
.cg{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}.cg div{background:#f8f2f7;border-radius:18px;padding:18px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.cg small{font:700 15px Inter;letter-spacing:2px;color:#8a6f8c}.cg b{font:700 31px/1.3 Inter}
.ap{display:flex;align-items:center;justify-content:space-between;background:#3a1f3d;color:#fff;border-radius:18px;padding:16px 20px;font:600 21px Inter}.ap i{font-style:normal;font:700 19px Inter;background:#ffb38a;color:#3a1f3d;border-radius:12px;padding:10px 18px}""")

P["p175_event_s5"] = ev(5, "<div class=kk>YOUR TURN</div><h1>Run events for clients?<br><span>Let's build your event app.</span></h1>",
f'''<div class=g5>{"".join(f'<div class="cd"><span class=ib>{ic(i,34)}</span><b>{a}</b><span class=s5>{b}</span></div>' for i,a,b in [("clock","Run sheet","minute by minute"),("users","Vendor board","who is confirmed"),("check","Team tasks","what is left"),("globe","Client page","progress and approvals")])}</div>''',
css=""".vis{display:flex}.g5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}.g5 .cd{padding:28px;display:flex;flex-direction:column;justify-content:center;gap:12px}
.g5 .ib{width:96px;height:96px;border-radius:26px;background:#3a1f3d;color:#ffb38a}.g5 b{font:700 50px/1.2 Cardo}.g5 .s5{font:500 24px Inter;color:#8a6f8c}""",
cta="DM us to start")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
