import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 186 INDIA · Mattress maker (custom size) · SINGLE · Montserrat + DM Sans · lavender / deep navy / cream
# New technique: top-down bed frame SVG with dimension arrows + order card with thickness layers cross-section.
def bed():
    return ('<svg viewBox="50 30 480 600" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block">'
            '<rect x="70" y="40" width="380" height="60" rx="18" fill="#3b2e6e"/>'
            '<rect x="70" y="100" width="380" height="470" rx="10" fill="#d9d2f0" stroke="#3b2e6e" stroke-width="6"/>'
            '<rect x="92" y="122" width="336" height="426" rx="20" fill="#fffaf0" stroke="#b8aee0" stroke-width="3"/>'
            '<g stroke="#e6def8" stroke-width="2">' + "".join(f'<line x1="92" y1="{150+i*40}" x2="428" y2="{150+i*40}"/>' for i in range(10)) + '</g>'
            '<rect x="120" y="140" width="130" height="64" rx="18" fill="#ece6fb" stroke="#b8aee0" stroke-width="2"/><rect x="270" y="140" width="130" height="64" rx="18" fill="#ece6fb" stroke="#b8aee0" stroke-width="2"/>'
            '<line x1="92" y1="600" x2="428" y2="600" stroke="#e2574c" stroke-width="3"/><path d="M92 600l14-8v16zM428 600l-14-8v16z" fill="#e2574c"/>'
            '<rect x="200" y="584" width="120" height="32" rx="16" fill="#e2574c"/><text x="260" y="606" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="18" fill="#fff"><tspan>W 70 in</tspan></text>'
            '<line x1="476" y1="122" x2="476" y2="548" stroke="#e2574c" stroke-width="3"/><path d="M476 122l-8 14h16zM476 548l-8-14h16z" fill="#e2574c"/>'
            '<rect x="436" y="318" width="80" height="34" rx="17" fill="#e2574c"/><text x="476" y="341" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="17" fill="#fff"><tspan>L 76 in</tspan></text>'
            '<text x="260" y="370" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="26" fill="#3b2e6e"><tspan>Customer\'s bed</tspan></text>'
            '<text x="260" y="402" text-anchor="middle" font-family="DM Sans" font-weight="500" font-size="19" fill="#6b6590"><tspan>measured inside the frame</tspan></text></svg>')
layers = [("Quilted top", "1 in", "#fffaf0", 1), ("Soft foam", "2 in", "#ece6fb", 2), ("Firm core", "3 in", "#b8aee0", 3)]
P["p186_mattress"] = page("""
body{--f:'DM Sans';--h:'Montserrat';background:#efeaf9;color:#231c4a}
h1{font-family:'Montserrat';font-size:58px;font-weight:800;letter-spacing:-1.2px;line-height:1.22} h1 span{color:#e2574c}
.sub{color:#5b5583;font-size:23px}
.vis{gap:16px}
.bdp{width:470px;flex:none;background:#fff;border-radius:28px;padding:16px 10px 10px;display:flex;flex-direction:column;box-shadow:0 16px 34px rgba(35,28,74,.10)}
.bt2{display:flex;gap:10px;margin:12px 8px 0}.bt2 div{flex:1;background:#f3effc;border-radius:14px;padding:10px 14px}.bt2 span{display:block;font:700 13px 'DM Sans';letter-spacing:2px;color:#8a84ad}.bt2 b{font:700 21px 'DM Sans'}.bdp small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#8a84ad;margin-left:14px}.bdp .bv{flex:1;min-height:0}
.oc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.od{flex:1;background:#231c4a;color:#fff;border-radius:28px;padding:22px 24px;display:flex;flex-direction:column;gap:10px}
.od small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#b8aee0}.od h3{font:800 30px/1.25 Montserrat}
.kv{display:grid;grid-template-columns:1fr 1fr;gap:10px}.kv div{background:#30285e;border-radius:14px;padding:10px 14px}.kv span{display:block;font:700 13px 'DM Sans';letter-spacing:2px;color:#b8aee0}.kv b{font:700 23px 'DM Sans'}
.ly{flex:1;display:flex;flex-direction:column;gap:0}
.lyl{margin-top:6px}.ly div{display:flex;align-items:center;justify-content:space-between;padding:0 18px;font:600 22px 'DM Sans';color:#231c4a;border:2px solid #231c4a;margin-top:-2px}
.ly div:first-child{border-radius:14px 14px 0 0}.ly div:last-child{border-radius:0 0 14px 14px}
.ok{background:#f3effc;border-radius:20px;padding:14px 18px;display:flex;gap:14px;align-items:center;margin:0 8px 6px}.cf{display:flex;gap:10px;align-items:center;background:#e2574c;border-radius:14px;padding:12px 16px;font:600 19px/1.35 'DM Sans'}.cf svg{flex:none}
.ok .ib{width:52px;height:52px;border-radius:50%;background:#e2574c;color:#fff}.ok b{display:block;font:700 22px/1.3 'DM Sans'}.ok span{font:500 18px/1.35 'DM Sans';color:#5b5583}
""", "<h1>Custom mattress made<br><span>to the wrong size?</span></h1><div class=sub>The customer's measurements go straight into the order, with a photo.</div>",
f'''<div class=bdp><small>MEASURE FORM · SAMPLE</small><div class=bt2>{"".join(f'<div><span>{x}</span><b>{y}</b></div>' for x,y in [("BED TYPE","Double"),("FRAME","Wooden, with sides")])}</div><div class=bv>{bed()}</div><div class=ok><span class=ib>{ic("camera",26)}</span><p><b>Frame photo attached</b><span>Sent by the customer with the size.</span></p></div></div>
<div class=oc><div class=od><small>ORDER M-63 · SAMPLE CUSTOMER</small><h3>Custom double, 70 × 76 in</h3>
<div class=kv>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [("THICKNESS","6 in"),("FEEL","Medium firm"),("COVER","Zip, washable"),("DELIVERY","Sat, 28 Nov")])}</div>
<small class=lyl>LAYERS · 6 INCHES IN TOTAL</small><div class=ly>{"".join(f'<div style="flex:{h};background:{c}"><span>{a}</span><b>{t}</b></div>' for a,t,c,h in layers)}</div>
<div class=cf>{ic("check",22,w=3)} Cutting starts after the customer confirms the size.</div></div></div>''',
"#231c4a", "Make mattresses? DM us", "background:#e2574c;color:#fff")


# ───────── 187 USA · Pottery studio · CAROUSEL 5 · Gelasio + Open Sans · oatmeal / glaze teal / clay brown
# New techniques: SVG studio shelf of pots with name tags, piece tracker with stage pips greenware→bisque→glaze→ready, kiln load card.
PT = """
body{--f:'Open Sans';--h:'Gelasio';background:#efe7da;color:#3d2a1e}
h1{font-family:'Gelasio';font-weight:700;font-size:60px;letter-spacing:-.5px;line-height:1.22} h1 span{color:#1d7a74}
.kk{font:700 16px 'Open Sans';letter-spacing:3px;color:#a0582f;margin-top:22px}
.cd{background:#fffaf2;border-radius:26px;box-shadow:0 14px 30px rgba(61,42,30,.09)}
"""
def pt(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#3d2a1e;color:#fff"):
    return page(PT + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#3d2a1e", cta, ctacss, tagline=f"{n} / 5")
def pot(kind, x, y, col, tag, tc="#fff", tf="#3d2a1e"):
    shapes = {"bowl": f'<path d="M{x-60} {y-50} h120 q-6 50 -60 50 q-54 0 -60 -50z" fill="{col}" stroke="#3d2a1e" stroke-width="3"/>',
              "mug": f'<rect x="{x-38}" y="{y-80}" width="76" height="80" rx="10" fill="{col}" stroke="#3d2a1e" stroke-width="3"/><path d="M{x+38} {y-62} q30 0 30 24 q0 24 -30 24" fill="none" stroke="#3d2a1e" stroke-width="8"/><path d="M{x+38} {y-62} q30 0 30 24 q0 24 -30 24" fill="none" stroke="{col}" stroke-width="4"/>',
              "vase": f'<path d="M{x-18} {y-120} h36 v14 q34 30 30 70 q-4 36 -48 36 q-44 0 -48 -36 q-4 -40 30 -70z" fill="{col}" stroke="#3d2a1e" stroke-width="3"/>',
              "plate": f'<ellipse cx="{x}" cy="{y-14}" rx="72" ry="14" fill="{col}" stroke="#3d2a1e" stroke-width="3"/>'}[kind]
    return shapes + f'<rect x="{x-58}" y="{y+8}" width="116" height="34" rx="6" fill="{tc}" stroke="#3d2a1e" stroke-width="2"/><text x="{x}" y="{y+31}" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="16" fill="{tf}"><tspan>{tag}</tspan></text>'
def shelf(rows):
    out = '<svg viewBox="0 0 900 600" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block">'
    for r, items in enumerate(rows):
        y = 230 + r * 290
        out += f'<rect x="10" y="{y}" width="880" height="20" rx="4" fill="#a0582f"/>'
        out += "".join(f'<g transform="translate({it[0]},{y}) scale(1.5)">' + pot(it[1], 0, 0, it[2], it[3]).replace('y="8"', 'y="16"').replace('y="31"', 'y="39"') + '</g>' for it in items)
    return out + '</svg>'
q = "#e6dccb"
P["p187_pottery_s1"] = pt(1, "POTTERY STUDIOS", "Whose bowl is this?<br><span>Is it fired yet?</span>",
f'''<div class="cd sh"><small>THE DRYING SHELF · TODAY</small><div class=sv>{shelf([[(110,"bowl",q,"No name"),(330,"mug",q,"Member?"),(560,"vase",q,"Glaze: ?"),(780,"plate",q,"Tag fell off")],
[(110,"mug","#cfc3ad","Since Oct"),(330,"bowl","#cfc3ad","Class 3?"),(560,"plate","#cfc3ad","Pick up?"),(780,"vase","#cfc3ad","Fired?")]])}</div>
<div class=qs>{"".join(f'<i>{t}</i>' for t in ["Paper tags fall off", "Glaze notes get lost", "Pickups are forgotten"])}</div></div>''',
css=""".vis{display:flex}.sh{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:12px}.sh small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#8f7b69}.sv{flex:1;min-height:0}
.qs{display:flex;gap:10px}.qs i{flex:1;font-style:normal;text-align:center;background:#3d2a1e;color:#fff;border-radius:14px;padding:14px 6px;font:600 19px 'Open Sans'}""")

wk = [("Tue", "6:30 PM", "Wheel basics", 8, 8), ("Wed", "6:30 PM", "Hand building", 6, 8), ("Thu", "7:00 PM", "Wheel basics", 7, 8), ("Sat", "10:00 AM", "Open studio", 9, 12), ("Sat", "2:00 PM", "Glaze night", 4, 10)]
P["p187_pottery_s2"] = pt(2, "PART 1 · CLASS BOOKING", "Seats fill online.<br><span>No more DM back-and-forth.</span>",
browser(f'''<div class=bk><b class=t>Book a class · this week</b>
{"".join(f'<div class="cl {"full" if a==c else ""}"><div class=dt><b>{d}</b><span>{t}</span></div><div class=nm><b>{n}</b><div class=st>{"".join(f"<i class={chr(34)}{chr(102) if i<a else chr(111)}{chr(34)}></i>" for i in range(c))}</div></div><em>{"Waitlist" if a==c else f"{c-a} left"}</em></div>' for d,t,n,a,c in wk)}
<div class=nt>{ic("clock",22)} Reminder text goes out the morning of each class.</div></div>''', url="yourstudio.com/classes · sample", style="flex:1"),
css=""".vis{display:flex}.bk{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:10px}.bk .t{font:700 32px Gelasio}
.cl{flex:1;display:flex;align-items:center;gap:16px;border-radius:18px;background:#f6efe4;padding:0 18px}
.dt{width:110px;flex:none}.dt b{display:block;font:700 26px/1.25 Gelasio}.dt span{font:600 17px 'Open Sans';color:#8f7b69}
.nm{flex:1}.nm b{display:block;font:700 22px/1.3 'Open Sans';margin-bottom:6px}.st{display:flex;gap:5px}.st i{width:20px;height:20px;border-radius:50%}.st .f{background:#1d7a74}.st .o{border:2px solid #b9a98f}
.cl em{font-style:normal;font:700 18px 'Open Sans';background:#1d7a74;color:#fff;border-radius:12px;padding:8px 14px;width:118px;text-align:center}
.cl.full em{background:#3d2a1e}
.nt{display:flex;gap:10px;align-items:center;font:600 19px 'Open Sans';color:#5e4a3b}""")

stg = ["Greenware", "Bisque", "Glazed", "Ready"]
pieces = [("Bowl", "Member 14", 3, "Glaze firing Thu"), ("Mug", "Member 22", 4, "Pickup by Sun"), ("Vase", "Member 14", 2, "Glaze: sea green"), ("Plate", "Class 3 · seat 5", 1, "Drying"), ("Mug", "Member 09", 3, "Glaze firing Thu")]
P["p187_pottery_s3"] = pt(3, "PART 2 · PIECE TRACKER", "Every piece has a tag<br><span>and a stage.</span>",
f'''<div class="cd tr"><div class=hdr><span>PIECE · OWNER</span><div class=sh2>{"".join(f'<b>{s}</b>' for s in stg)}</div></div>
{"".join(f'<div class=pr><div class=pn><b>{a}</b><span>{o}</span></div><div class=pips>{"".join(f"<i class={chr(34)}{chr(100) if i<st else chr(110)}{chr(34)}></i>" for i in range(4))}</div><em>{n}</em></div>' for a,o,st,n in pieces)}</div>''',
css=""".vis{display:flex}.tr{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.hdr{display:flex;align-items:center;gap:16px;padding-bottom:6px;border-bottom:2px solid #e6dccb}.hdr>span{width:200px;flex:none;font:700 14px 'Open Sans';letter-spacing:2px;color:#8f7b69}
.sh2{width:500px;flex:none;display:grid;grid-template-columns:repeat(4,1fr)}.sh2 b{font:700 18px 'Open Sans';text-align:center;color:#8f7b69}
.pr{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1px solid #efe6d6}
.pn{width:200px;flex:none}.pn b{display:block;font:700 32px/1.25 Gelasio}.pn span{font:600 18px 'Open Sans';color:#8f7b69}
.pips{width:500px;flex:none;display:grid;grid-template-columns:repeat(4,1fr);position:relative}
.pips:before{content:"";position:absolute;left:12.5%;right:12.5%;top:50%;height:6px;margin-top:-3px;background:#e6dccb}
.pips i{width:52px;height:52px;border-radius:50%;justify-self:center;position:relative}.pips .d{background:#1d7a74;box-shadow:0 0 0 5px #fffaf2}.pips .n{background:#fffaf2;border:3px solid #cdbfa8}
.pr em{flex:1;font-style:normal;font:700 21px/1.3 'Open Sans';color:#a0582f;text-align:right}""")

P["p187_pottery_s4"] = pt(4, "PART 3 · READY TEXT", "Fired and ready?<br><span>The owner gets a text.</span>",
f'''<div class=kl><div class="cd kc"><small>KILN LOAD · THU · GLAZE FIRING · SAMPLE</small><div class=kg>{"".join(f'<div><b>{a}</b><span>{o}</span></div>' for a,o in [("Bowl","Member 14"),("Mug","Member 09"),("Cup","Member 31"),("Bowl","Class 3"),("Plate","Member 22"),("Mug","Member 17")])}</div></div>
<div class=sms><div class=bub><b>Your bowl is ready!</b><span>Glaze: sea blue. Pick it up from the ready shelf this week, 10 AM to 8 PM.</span></div><em>Text · Fri, 9:05 AM · sample</em></div>
<div class=nt2>{ic("bell",24)}<span>Not picked up in 14 days? A friendly second reminder goes out.</span></div></div>''',
css=""".kl{flex:1;display:flex;flex-direction:column;gap:16px}
.kc{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:12px;background:#3d2a1e;color:#fff}.kc small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#d9b48f}
.kg{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.kg div{border-radius:50% 50% 18px 18px;background:radial-gradient(circle at 50% 30%,#e98d4f,#a0582f);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.kg b{font:700 36px/1.3 Gelasio}.kg span{font:600 20px 'Open Sans';color:#ffe9d6}
.sms{align-self:flex-end;width:760px;display:flex;flex-direction:column;align-items:flex-end;gap:6px}
.bub{background:#1d7a74;color:#fff;border-radius:26px 26px 6px 26px;padding:20px 24px;display:flex;flex-direction:column;gap:6px}.bub b{font:700 30px/1.25 Gelasio}.bub span{font:500 21px/1.4 'Open Sans';text-wrap:balance}
.sms em{font-style:normal;font:600 16px 'Open Sans';color:#8f7b69}
.nt2{display:flex;gap:12px;align-items:center;background:#fffaf2;border-radius:18px;padding:14px 18px;font:600 20px 'Open Sans';color:#5e4a3b}.nt2 svg{color:#a0582f;flex:none}""")

P["p187_pottery_s5"] = pt(5, "YOUR TURN", "Run a pottery or<br>ceramics studio?<br><span>Let's build your studio app.</span>",
f'''<div class=fin><div class=svf>{shelf([[(110,"bowl","#1d7a74","Ready"),(330,"mug","#e98d4f","Glazed"),(560,"vase","#5aa9a2","Bisque"),(780,"plate","#d9b48f","Booked")]]).replace('viewBox="0 0 900 600"','viewBox="0 30 900 290"')}</div>
<div class=tl4>{"".join(f'<div><span>{ic(i,44)}</span><b>{a}</b><small>{d}</small></div>' for i,a,d in [("cal","Class booking","Seats and waitlist online"),("tag","Piece tags","Owner and glaze on every piece"),("chart","Stage tracker","Greenware to ready"),("bell","Ready texts","Pickups on time")])}</div></div>''',
cta="DM us to build yours", ctacss="background:#1d7a74;color:#fff",
css=""".fin{flex:1;display:flex;flex-direction:column;gap:16px}.svf{background:#fffaf2;border-radius:26px;padding:16px 20px;height:330px}
.tl4{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}.tl4 div{background:#fffaf2;border-radius:22px;display:flex;flex-direction:column;justify-content:center;padding:0 26px;gap:6px;box-shadow:0 10px 24px rgba(61,42,30,.07)}
.tl4 span{color:#a0582f}.tl4 b{font:700 36px/1.25 Gelasio}.tl4 small{font:500 20px/1.35 'Open Sans';color:#7a6655}""")


# ───────── 188 INDIA · Cement dealer · SINGLE · Anton + Roboto · cement grey / emerald / white
# New technique: SVG pallet stacks of cement bags as stock per brand-less grade + truck challan strip for sites.
def bags(n_rows, per, x0, y0, col):
    out = ""
    for r in range(n_rows):
        for i in range(per - (r % 2)):
            x = x0 + i * 74 + (37 if r % 2 else 0); y = y0 - r * 34
            out += f'<rect x="{x}" y="{y}" width="70" height="32" rx="12" fill="{col}" stroke="#4a4f55" stroke-width="2.5"/><rect x="{x+22}" y="{y+10}" width="26" height="12" rx="3" fill="#fff" opacity=".7"/>'
    return out
def stock():
    return ('<svg viewBox="0 0 900 300" width="100%" style="display:block">'
            '<rect x="20" y="246" width="250" height="14" fill="#8a7a62"/><rect x="330" y="246" width="250" height="14" fill="#8a7a62"/><rect x="640" y="246" width="250" height="14" fill="#8a7a62"/>'
            + bags(6, 3, 34, 212, "#d6d9dc") + bags(3, 3, 344, 212, "#cfe6da") + bags(1, 3, 654, 212, "#f2c9c0") +
            '<text x="145" y="292" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="22" fill="#2d3238"><tspan>OPC 53 · 410 bags</tspan></text>'
            '<text x="455" y="292" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="22" fill="#2d3238"><tspan>PPC · 180 bags</tspan></text>'
            '<text x="765" y="292" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="22" fill="#c0392b"><tspan>White cement · 12</tspan></text></svg>')
trips = [("Site A · Sample contractor", "120 bags OPC 53", "Delivered 9:40 AM", "d"), ("Site B · Sample builder", "80 bags PPC", "On the way", "w"), ("Site C · Sample house", "45 bags OPC 53", "Loading", "l"), ("Site A · Sample contractor", "60 bags PPC", "Tomorrow 8 AM", "t")]
P["p188_cement"] = page("""
body{--f:'Roboto';--h:'Anton';background:#e4e6e8;color:#2d3238}
h1{font-family:'Anton';font-size:70px;font-weight:400;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#0f8a5f}
.sub{color:#5a6068;font-size:23px}
.vis{flex-direction:column;gap:16px}
.sk{background:#fff;border-radius:28px;padding:18px 22px 10px;box-shadow:0 14px 30px rgba(45,50,56,.08)}
.sk .hd{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}.sk small{font:700 14px 'Roboto';letter-spacing:2.5px;color:#7a8088}
.sk em{font-style:normal;font:700 17px 'Roboto';background:#fdecea;color:#c0392b;border-radius:12px;padding:6px 12px}
.tp{flex:1;background:#2d3238;color:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:10px}
.tp small{font:700 14px 'Roboto';letter-spacing:2.5px;color:#aab1b9}
.tr{flex:1;display:flex;align-items:center;gap:16px;background:#3a4047;border-radius:18px;padding:0 18px}
.tr .ib{width:54px;height:54px;border-radius:14px;background:#4a5159}.tr.d .ib{background:#0f8a5f}
.tr div{flex:1}.tr b{display:block;font:700 23px/1.3 'Roboto'}.tr span{font:500 18px 'Roboto';color:#c3c9cf}
.tr em{font-style:normal;font:700 18px 'Roboto';border-radius:12px;padding:8px 14px;width:200px;text-align:center}
.tr.d em{background:#0f8a5f}.tr.w em{background:#f0b429;color:#2d3238}.tr.l em{background:#5d656e}.tr.t em{border:2px dashed #8a929b;color:#d5dade}
.ac{display:flex;gap:12px}.ac div{flex:1;background:#3a4047;border-radius:16px;padding:12px 16px}.ac span{display:block;font:600 15px 'Roboto';color:#aab1b9}.ac b{font:700 24px/1.3 'Roboto'}
""", "<h1>Bags on the floor, trucks on<br><span>the road. Who got what?</span></h1>",
f'''<div class=sk><div class=hd><small>GODOWN STOCK · SAMPLE · UPDATED AT EVERY DISPATCH</small><em>White cement low</em></div>{stock()}</div>
<div class=tp><small>TODAY'S SITE DELIVERIES · SAMPLE</small>{"".join(f'<div class="tr {k}"><span class=ib>{ic("truck",28)}</span><div><b>{a}</b><span>{b}</span></div><em>{s}</em></div>' for a,b,s,k in trips)}
<div class=ac>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [("Bags out today","245"),("Sites served","3"),("Challans sent","3")])}</div></div>''',
"#2d3238", "Sell cement or building material? DM us", "background:#0f8a5f;color:#fff")


# ───────── 189 INDIA · Dance classes for adults · CAROUSEL 5 · Poppins + Inter · midnight / electric violet / lemon
# New techniques: dance floor tile grid as attendance (lit tile = present), week batch timetable bars, phone fee reminder, show registration seats.
DC = """
body{--f:'Inter';--h:'Poppins';background:#14122b;color:#fff}
h1{font-family:'Poppins';font-weight:800;font-size:60px;letter-spacing:-1.2px;line-height:1.22} h1 span{color:#e8ff59}
.kk{font:700 16px 'Inter';letter-spacing:3px;color:#a98bff;margin-top:22px}
.cd{background:#221f45;border-radius:26px}
"""
def dc(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#e8ff59;color:#14122b"):
    return page(DC + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#fff", cta, ctacss, tagline=f"{n} / 5", logo_color="#ffffff")
random.seed(189)
pres = [1]*17 + [0]*3; random.shuffle(pres)
P["p189_dance_s1"] = dc(1, "DANCE CLASSES FOR ADULTS", "Who came today?<br><span>Who paid this month?</span>",
f'''<div class="cd fl"><div class=fh><small>EVENING BATCH · ATTENDANCE · SAMPLE</small><b>17 of 20 here</b></div>
<div class=tiles>{"".join(f'<div class="t {"on" if p else "off"}"><span>{i+1:02d}</span><em>{"Here" if p else "Absent"}</em></div>' for i,p in enumerate(pres))}</div>
<div class=ff><span><i class=on></i>Here today</span><span><i class=off></i>Absent</span><span>Tap a tile to mark</span></div></div>''',
css=""".vis{display:flex}.fl{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:14px}
.fh{display:flex;justify-content:space-between;align-items:center}.fh small{font:700 14px 'Inter';letter-spacing:2.5px;color:#a9a4d6}.fh b{font:800 28px Poppins;color:#e8ff59}
.tiles{flex:1;display:grid;grid-template-columns:repeat(5,1fr);grid-template-rows:repeat(4,1fr);gap:10px}
.t{border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.t span{font:800 34px/1.25 Poppins}.t em{font-style:normal;font:600 16px 'Inter'}
.t.on{background:linear-gradient(145deg,#7c4dff,#a98bff);box-shadow:0 0 24px rgba(169,139,255,.45)}.t.off{background:#2c2858;color:#77729f;border:2px dashed #4a4580}
.ff{display:flex;gap:24px;font:600 18px 'Inter';color:#c9c5ee}.ff span{display:flex;align-items:center;gap:8px}.ff span:last-child{margin-left:auto;color:#e8ff59}
.ff i{width:20px;height:20px;border-radius:6px}.ff i.on{background:#a98bff}.ff i.off{border:2px dashed #77729f}""")

tt = [("Mon", [("7-8 AM", "Morning batch", 0), ("7-8 PM", "Evening batch", 1)]), ("Tue", [("7-8 PM", "Beginners", 2)]), ("Wed", [("7-8 AM", "Morning batch", 0), ("7-8 PM", "Evening batch", 1)]),
      ("Thu", [("7-8 PM", "Beginners", 2)]), ("Fri", [("7-8 AM", "Morning batch", 0), ("7-8 PM", "Evening batch", 1)]), ("Sat", [("5-7 PM", "Show practice", 3)])]
cols = ["#7c4dff", "#e8ff59", "#40d6c4", "#ff7aa8"]
P["p189_dance_s2"] = dc(2, "PART 1 · BATCH TIMETABLE", "One timetable.<br><span>Every batch, every week.</span>",
f'''<div class="cd tb">{"".join(f'<div class=dr><b>{d}</b><div class=bars>{"".join(f"<div class=br style={chr(34)}background:{cols[c]};color:{chr(35)+chr(49)+chr(52)+chr(49)+chr(50)+chr(50)+chr(98) if c else chr(35)+chr(102)*3}{chr(34)}><span>{n}</span><em>{t}</em></div>" for t,n,c in sl)}</div></div>' for d,sl in tt)}
<div class=lgd>{"".join(f'<span><i style="background:{cols[i]}"></i>{n}</span>' for i,n in enumerate(["Morning", "Evening", "Beginners", "Show practice"]))}</div></div>''',
css=""".vis{display:flex}.tb{flex:1;padding:20px 22px;display:flex;flex-direction:column;gap:10px}
.dr{flex:1;display:flex;align-items:center;gap:16px}.dr>b{width:70px;flex:none;font:800 26px Poppins}
.bars{flex:1;display:flex;gap:10px;height:100%}.br{flex:1;border-radius:16px;display:flex;align-items:center;justify-content:space-between;padding:0 20px}
.br span{font:700 23px Poppins}.br em{font-style:normal;font:700 19px 'Inter';opacity:.85}
.lgd{display:flex;gap:22px;font:600 18px 'Inter';color:#c9c5ee;padding-top:4px}.lgd span{display:flex;gap:8px;align-items:center}.lgd i{width:18px;height:18px;border-radius:5px}""")

fees = [("Member 04", "Evening batch", "Paid early", "p"), ("Member 08", "Morning batch", "Reminder sent", "r"), ("Member 11", "Morning batch", "Not yet", "d"), ("Member 13", "Beginners", "Paid early", "p"), ("Member 17", "Beginners", "Reminder sent", "r"), ("Member 20", "Evening batch", "Paid early", "p")]
P["p189_dance_s3"] = dc(3, "PART 2 · MONTHLY FEES", "Fee reminders go out<br><span>on their own.</span>",
f'''<div class=fw><div class="cd fs"><small>DECEMBER FEES · DUE 1 DEC · SAMPLE</small>{"".join(f'<div class="fr {k}"><div><b>{a}</b><span>{b}</span></div><em>{s}</em></div>' for a,b,s,k in fees)}</div>
{phone(f"""<div class=ph><small>MESSAGE · SAMPLE</small><div class=bb1><b>Hi! Your December fee is due on 1 Dec.</b><span>Evening batch: Mon, Wed and Fri, 7-8 PM</span><i>Pay by UPI link</i></div><div class=bb2>Paid ✓</div><div class=bb1><b>Thank you! Your receipt is ready.</b><span>See you on Monday at 7 PM.</span></div><div class=rc><small>RECEIPT · SAMPLE</small><b>December fee</b><span>Evening batch · paid</span></div></div>""", w=340, h=700)}</div>''',
css=""".fw{flex:1;display:flex;gap:20px;align-items:center}
.fs{flex:1;align-self:stretch;padding:20px 22px;display:flex;flex-direction:column;gap:10px}.fs small{font:700 14px 'Inter';letter-spacing:2.5px;color:#a9a4d6}
.fr{flex:1;display:flex;align-items:center;gap:12px;border-radius:18px;background:#2c2858;padding:0 18px}.fr div{flex:1}.fr b{display:block;font:700 25px/1.3 Poppins}.fr span{font:500 18px 'Inter';color:#a9a4d6}
.fr em{font-style:normal;font:700 17px 'Inter';border-radius:12px;padding:8px 12px;width:150px;text-align:center}.fr.p em{background:#40d6c4;color:#14122b}.fr.d em{background:#ff7aa8;color:#14122b}.fr.r em{border:2px solid #a98bff;color:#d9ccff}
.ph{flex:1;background:#f1eefc;padding:16px 16px;display:flex;flex-direction:column;gap:12px;color:#14122b}.ph small{font:700 12px 'Inter';letter-spacing:2px;color:#77729f;text-align:center}
.bb1{background:#fff;border-radius:18px 18px 18px 4px;padding:14px 16px;display:flex;flex-direction:column;gap:6px;box-shadow:0 4px 10px rgba(20,18,43,.06)}.bb1 b{font:700 19px/1.35 Poppins}.bb1 span{font:500 16px/1.4 'Inter';color:#4b4770}.rc{background:#14122b;color:#fff;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;gap:2px}.rc small{color:#a98bff;text-align:left}.rc b{font:700 19px Poppins}.rc span{font:500 15px 'Inter';color:#c9c5ee}
.bb1 i{font-style:normal;background:#7c4dff;color:#fff;border-radius:12px;padding:10px;text-align:center;font:700 15px 'Inter'}
.bb2{align-self:flex-end;background:#7c4dff;color:#fff;border-radius:18px 18px 4px 18px;padding:12px 18px;font:700 17px 'Inter'}""")

seats = 40; taken = 28
P["p189_dance_s4"] = dc(4, "PART 3 · SHOW SIGN-UPS", "Annual show? Members<br><span>sign up in one link.</span>",
f'''<div class="cd sw"><div class=sh3><div><small>YEAR-END SHOW · SAT, 19 DEC · SAMPLE</small><b>Performer sign-ups</b></div><em>{taken} of {seats}</em></div>
<div class=sg2>{"".join(f'<i class="{("g1" if i<12 else "g2" if i<21 else "g3") if i<taken else "fr"}">{i+1:02d}</i>' for i in range(seats))}</div>
<div class=gr>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("Group 1 · Evening","12 signed up"),("Group 2 · Morning","9 signed up"),("Group 3 · Beginners","7 signed up")])}</div>
<div class=nt3>{ic("cal",24)}<span>Signed-up members see the Saturday practice slots in their timetable.</span></div></div>''',
css=""".vis{display:flex}.sw{flex:1;padding:22px;display:flex;flex-direction:column;gap:16px}
.sh3{display:flex;justify-content:space-between;align-items:center}.sh3 small{display:block;font:700 14px/1.4 'Inter';letter-spacing:2.5px;color:#a9a4d6;margin-bottom:6px}.sh3 b{font:800 32px/1.3 Poppins}.sh3 em{font-style:normal;font:800 36px/1.3 Poppins;color:#e8ff59}
.sg2{flex:1;display:grid;grid-template-columns:repeat(10,1fr);grid-template-rows:repeat(4,1fr);gap:10px}.sg2 i{border-radius:12px;font-style:normal;font:700 20px 'Inter';display:flex;align-items:center;justify-content:center}.sg2 .g1{background:#7c4dff}.sg2 .g2{background:#e8ff59;color:#14122b}.sg2 .g3{background:#40d6c4;color:#14122b}.sg2 .fr{border:2px dashed #4a4580;color:#5d5890}
.gr{display:flex;gap:12px}.gr div{flex:1;background:#2c2858;border-radius:16px;padding:14px 16px;border-left:8px solid #7c4dff}.gr div:nth-child(2){border-color:#e8ff59}.gr div:nth-child(3){border-color:#40d6c4}.gr b{display:block;font:700 20px/1.3 Poppins}.gr span{font:500 17px 'Inter';color:#c9c5ee}
.nt3{display:flex;gap:12px;align-items:center;font:600 20px 'Inter';color:#e8ff59}.nt3 svg{flex:none}""")

P["p189_dance_s5"] = dc(5, "YOUR TURN", "Run dance classes<br>for adults?<br><span>Let's build your class app.</span>",
f'''<div class=c5>{"".join(f'<div class="cc {k}"><span>{ic(i,68,w=1.8)}</span><b>{a}</b><small>{b}</small></div>' for i,a,b,k in [("users","Attendance","Tap tiles, done","a"),("cal","Timetable","All batches, one view","b"),("rupee","Fee reminders","Sent on the due date","c"),("spark","Show sign-ups","Groups fill themselves","d")])}</div>''',
cta="DM us to build yours", ctacss="background:#e8ff59;color:#14122b",
css=""".c5{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px}.cc{border-radius:26px;padding:26px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px}
.cc span{margin-bottom:auto}.cc b{font:800 38px/1.25 Poppins}.cc small{font:500 21px 'Inter';opacity:.85}
.cc.a{background:#7c4dff}.cc.b{background:#e8ff59;color:#14122b}.cc.c{background:#40d6c4;color:#14122b}.cc.d{background:#ff7aa8;color:#14122b}""")


# ───────── 190 CANADA · Locksmith · SINGLE · Cardo + Roboto · brass / black / off-white
# New technique: SVG key ring where each key carries a job tag (job type, area, time, status).
def keyring():
    keys = [("Lockout", "M4K area", "Now · ETA 25 min", "#e0a526", -38), ("Rekey 3 doors", "M6G area", "11:30 AM", "#c9c3b4", -14), ("New deadbolt", "L5B area", "2:00 PM", "#c9c3b4", 12), ("Safe opening", "M2N area", "4:30 PM", "#9c8e73", 36)]
    out = '<svg viewBox="50 15 800 535" width="100%" height="100%" preserveAspectRatio="xMidYMid meet" style="display:block"><circle cx="450" cy="90" r="62" fill="none" stroke="#2b2620" stroke-width="12"/>'
    for i, (a, b, c, col, ang) in enumerate(keys):
        x = 150 + i * 200
        out += (f'<path d="M450 140 L{x} 230" stroke="#2b2620" stroke-width="5"/>'
                f'<circle cx="{x}" cy="262" r="34" fill="{col}" stroke="#2b2620" stroke-width="4"/><circle cx="{x}" cy="262" r="12" fill="#f4f0e6" stroke="#2b2620" stroke-width="3"/>'
                f'<path d="M{x-10} 294 h20 v120 l-10 12 h-6 v-12 h-8 v-14 h8 v-12 h-8 v-14 h8z" fill="{col}" stroke="#2b2620" stroke-width="3" stroke-linejoin="round"/>'
                f'<rect x="{x-88}" y="438" width="176" height="104" rx="12" fill="#fff" stroke="#2b2620" stroke-width="3"/>'
                f'<text x="{x}" y="470" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="20" fill="#2b2620"><tspan>{a}</tspan></text>'
                f'<text x="{x}" y="497" text-anchor="middle" font-family="Roboto" font-weight="500" font-size="17" fill="#6d6455"><tspan>{b}</tspan></text>'
                f'<text x="{x}" y="525" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="17" fill="{"#b23a1e" if i==0 else "#2b2620"}"><tspan>{c}</tspan></text>')
    return out + '</svg>'
P["p190_locksmith"] = page("""
body{--f:'Roboto';--h:'Cardo';background:#f4f0e6;color:#2b2620}
h1{font-family:'Cardo';font-size:66px;font-weight:700;letter-spacing:-.4px;line-height:1.22} h1 span{color:#b07d12}
.sub{color:#6d6455;font-size:23px}
.vis{flex-direction:column;gap:16px}
.kr{flex:1;min-height:0;background:#fff;border-radius:28px;padding:16px 18px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(43,38,32,.08)}
.kr small{font:700 14px 'Roboto';letter-spacing:2.5px;color:#8d8371}.kr .ks{flex:1;min-height:0}
.rq{background:#2b2620;color:#fff;border-radius:28px;padding:20px 24px;display:flex;gap:18px;align-items:center}
.rq .ib{width:64px;height:64px;border-radius:18px;background:#e0a526;color:#2b2620}
.rq div{flex:1}.rq small{display:block;font:700 14px 'Roboto';letter-spacing:2.5px;color:#d8c9a6}.rq b{display:block;font:700 30px/1.3 Cardo}.rq span{font:500 19px/1.4 'Roboto';color:#d9d2c3}
.rq em{font-style:normal;background:#e0a526;color:#2b2620;border-radius:16px;padding:14px 18px;font:700 20px 'Roboto';text-align:center}
""", "<h1>Lockout calls at all hours?<br><span>Let them request you online.</span></h1><div class=sub>Every job lands on one ring: what, where, when.</div>",
f'''<div class=kr><small>TODAY'S JOBS · SAMPLE · ONE KEY PER JOB</small><div class=ks>{keyring()}</div></div>
<div class=rq><span class=ib>{ic("pin",32)}</span><div><small>REQUEST FORM · SAMPLE</small><b>Postal code, job type, photo of the lock</b><span>You see the area before you call back.</span></div><em>Request<br>a locksmith</em></div>''',
"#2b2620", "Run a locksmith service? DM us", "background:#b07d12;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
