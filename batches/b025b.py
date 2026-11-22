import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 142 INDIA · Small real estate builder · CAROUSEL 5 · Cardo + Montserrat · concrete grey / terracotta / sky
# New techniques: building facade as a live availability grid (floor x flat), simple SVG flat plan, slab-stage tracker, monthly build thumbnails.
BL = """
body{--f:'Montserrat';--h:'Cardo';background:#e7e6e1;color:#232a30}
h1{font-family:'Cardo';font-weight:700;font-size:64px;letter-spacing:-.4px;line-height:1.2} h1 span{color:#c4572e}
.kt{display:inline-flex;align-self:flex-start;align-items:center;gap:12px;margin-top:24px;font:700 16px 'Montserrat';letter-spacing:3px;color:#232a30}
.kt b{width:44px;height:44px;border-radius:10px;background:#c4572e;color:#fff;font:700 22px/1 'Cardo';display:flex;align-items:center;justify-content:center}
.kt + h1{margin-top:16px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(35,42,48,.08)}
.lb{font:700 13px 'Montserrat';letter-spacing:3px;color:#8d9296}
.sd{background:#232a30;color:#fff}.bk{background:#c4572e;color:#fff}.av{background:#fff;color:#1f6b45;box-shadow:inset 0 0 0 3px #3a9a6a}
"""
def bl(n, head, vis, css="", cta="Swipe", ctacss="background:#232a30;color:#fff"):
    return page(BL + css, head, vis, "#232a30", cta, ctacss, tagline=f"{n} / 5")
AV = {"1C", "2A", "3D", "5B", "7B", "8A", "9D", "10B", "10C"}; BK = {"4A", "6C", "8C", "9A", "10D"}
def st(f): return "av" if f in AV else "bk" if f in BK else "sd"
def facade(cell=58, gap=8, me=None):
    rows = "".join(f'<div class=fl1><em>{fl}</em>' + "".join(f'<i class="{st(f"{fl}{c}")}{" me" if me==f"{fl}{c}" else ""}">{fl}{c}</i>' for c in "ABCD") + '</div>' for fl in range(10, 0, -1))
    return f'<div class=bd1><div class=rf1></div>{rows}<div class=gf1>PARKING · ENTRANCE</div></div>'
FAC = """.bd1{background:#cfd3d6;border-radius:14px 14px 4px 4px;padding:16px 18px 10px;display:flex;flex-direction:column;gap:7px;position:relative}
.rf1{height:14px;background:#9aa1a7;border-radius:8px;margin:-4px -6px 4px}
.fl1{display:flex;gap:8px;align-items:center}.fl1 em{width:30px;font:700 15px Montserrat;font-style:normal;color:#5b6268;text-align:right}
.fl1 i{flex:1;height:50px;border-radius:7px;font:700 16px/50px Montserrat;font-style:normal;text-align:center;display:block}
.fl1 i.me{outline:4px solid #f0b23a;outline-offset:2px}
.gf1{margin-top:4px;background:#8d959b;color:#fff;border-radius:6px;text-align:center;font:700 13px/34px Montserrat;letter-spacing:3px}"""
P["p142_bl_s1"] = bl(1, "<h1>Buyers keep asking<br>“Which flats are free?”<br><span>Show live availability<br>on your project site.</span></h1>",
f'''<div class=w1><div class=sk1>{facade()}</div><div class=cs1><div class="cd n1"><span class=lb>SAMPLE PROJECT</span><b>40 flats</b><small>10 floors · 4 flats each</small></div>
{"".join(f'<div class="cd n1 {k}"><b>{v}</b><small>{t}</small></div>' for v,t,k in [("26","Sold","sd"),("5","Booked","bk"),("9","Available","av")])}</div></div>''',
FAC + """.w1{flex:1;display:flex;gap:18px}
.sk1{flex:1;background:linear-gradient(#cfe4f2,#eef5fa);border-radius:28px;display:flex;align-items:flex-end;justify-content:center;padding:22px 40px 0}
.sk1 .bd1{width:100%}
.cs1{width:250px;flex:none;display:flex;flex-direction:column;gap:14px}
.n1{flex:1;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:2px}
.n1 b{font:700 52px/1.3 Cardo}.n1 small{font:600 18px Montserrat}
.n1.sd small,.n1.bk small{color:#fff;opacity:.85}.n1.av{box-shadow:inset 0 0 0 4px #3a9a6a}""")

plan = '''<svg viewBox="0 0 400 300" width="100%" height="100%" preserveAspectRatio="xMidYMid meet">
<rect x="10" y="10" width="380" height="280" fill="#fff" stroke="#232a30" stroke-width="6"/>
<path d="M170 10 V170 M10 170 H250 M250 10 V290 M250 140 H390 M120 170 V290" stroke="#232a30" stroke-width="4" fill="none"/>
<rect x="60" y="166" width="40" height="8" fill="#fff"/><rect x="246" y="60" width="8" height="40" fill="#fff"/><rect x="246" y="200" width="8" height="40" fill="#fff"/>
<rect x="390" y="40" width="8" height="70" fill="#9cc7e4"/><rect x="20" y="4" width="80" height="8" fill="#9cc7e4"/>
''' + "".join(f'<text x="{x}" y="{y}" text-anchor="middle" font-family="Montserrat" font-weight="700" font-size="14" fill="#232a30"><tspan>{t}</tspan></text><text x="{x}" y="{y+20}" text-anchor="middle" font-family="Montserrat" font-weight="500" font-size="13" fill="#6b7177">{d}</text>'
              for x, y, t, d in [(90, 85, "LIVING", "14 x 12 ft"), (210, 85, "KITCHEN", "8 x 10 ft"), (320, 70, "BEDROOM 1", "12 x 11 ft"), (320, 210, "BEDROOM 2", "11 x 10 ft"), (65, 246, "BALCONY", "10 x 5 ft"), (185, 230, "BATH", "7 x 5 ft")]) + '</svg>'
P["p142_bl_s2"] = bl(2, "<div class=kt><b>1</b>FLAT PAGE</div><h1>Every free flat with its plan,<br><span>floor and facing.</span></h1>",
f'''<div class=w2>{browser(f"""<div class=pg2><div class=hd2><span class=lb>AVAILABLE · SAMPLE</span><b class=h2>Flat 7B · 2 BHK</b></div><div class=pl2>{plan}</div><div class=in2>
{"".join(f'<div class=kv2><span>{a}</span><b>{b}</b></div>' for a,b in [("Floor","7th of 10"),("Carpet area","1,050 sq ft"),("Facing","East · garden side"),("Parking","1 covered")])}
<div class=bt2>Book a site visit</div></div></div>""", "yourproject.in/flats/7B", "flex:1;min-height:0")}</div>''',
FAC + """.w2{flex:1;display:flex;gap:16px}
.pg2{flex:1;min-height:0;display:flex;flex-direction:column;gap:16px;padding:18px;background:#fff}
.pl2{flex:1;min-height:0;background:#f3f2ee;border-radius:16px;padding:14px;display:flex}.pl2 svg{flex:1;min-width:0;min-height:0}
.in2{flex:none;display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.in2 .bt2{grid-column:1/-1}.hd2{display:flex;flex-direction:column;gap:2px}
.h2{font:700 38px/1.25 Cardo}
.kv2{flex:1;background:#f3f2ee;border-radius:14px;padding:10px 14px;display:flex;flex-direction:column;justify-content:center;gap:2px}
.kv2 span{font:600 14px Montserrat;color:#8d9296;letter-spacing:1px}.kv2 b{font:700 20px Montserrat}
.bt2{background:#c4572e;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 18px Montserrat}
.mf2{width:230px;flex:none;display:flex;align-items:flex-end}
.mf2 .bd1{padding:10px 10px 8px;gap:4px;width:100%}.mf2 .fl1{gap:4px}.mf2 .fl1 em{display:none}
.mf2 .fl1 i{height:30px;font:700 11px/30px Montserrat}.mf2 .gf1{font-size:9px;line-height:20px;letter-spacing:1px}""")

stages = [("Booking", "done"), ("Agreement", "done"), ("Plinth", "done"), ("Slab 1 to 5", "done"), ("Slab 6 to 10", "now"), ("Brickwork", ""), ("Plaster + tiles", ""), ("Possession", "")]
P["p142_bl_s3"] = bl(3, "<div class=kt><b>2</b>BUYER STAGES</div><h1>Each buyer sees which stage<br><span>is done and what is next.</span></h1>",
f'''<div class="cd w3"><div class=t3><div><span class=lb>BUYER PAGE · FLAT 5A · SAMPLE</span><b>Your flat's stages</b></div><em>Slab 9 of 10 cast</em></div>
<div class=rl3>{"".join(f'<div class="s3 {k}"><i>{ic("check",20,"#fff",3) if k=="done" else ""}</i><b>{a}</b><span>{"Done" if k=="done" else "In progress" if k=="now" else "Next" if a=="Brickwork" else "Later"}</span></div>' for a,k in stages)}</div>
<div class=nt3>{ic("doc",22)}<span>When a stage is done, the demand letter and site photos go to every buyer of that stage on WhatsApp.</span></div></div>''',
""".w3{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:16px}
.t3{display:flex;justify-content:space-between;align-items:center}.t3 b{display:block;font:700 34px/1.25 Cardo}
.t3 em{font-style:normal;font:700 17px Montserrat;background:#fbe3d8;color:#9a3d1b;border-radius:12px;padding:9px 14px}
.rl3{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr);gap:12px}
.s3{display:flex;align-items:center;gap:14px;background:#f3f2ee;border-radius:16px;padding:0 18px}
.s3 i{width:40px;height:40px;border-radius:50%;flex:none;border:3px solid #c3c6c9;display:flex;align-items:center;justify-content:center}
.s3.done i{background:#3a9a6a;border-color:#3a9a6a}.s3.now{background:#fbe3d8}.s3.now i{border-color:#c4572e;box-shadow:inset 0 0 0 7px #fff,inset 0 0 0 20px #c4572e}
.s3 b{flex:1;font:700 21px/1.25 Montserrat}.s3 span{font:600 16px Montserrat;color:#6b7177}.s3.now span{color:#9a3d1b}
.nt3{display:flex;align-items:center;gap:12px;background:#232a30;color:#fff;border-radius:14px;padding:14px 18px;font:500 18px/1.4 Montserrat}""")

def bld(fl):
    return f'''<svg viewBox="0 0 120 170" width="100%" height="100%" preserveAspectRatio="xMidYMax slice"><rect width="120" height="170" fill="#dcebf5"/>
<rect y="158" width="120" height="12" fill="#b9a98c"/>''' + "".join(f'<rect x="20" y="{148-i*13}" width="80" height="10" fill="{"#8d959b" if i<fl-1 else "#c4572e"}"/>' for i in range(fl)) + "".join(f'<rect x="{x}" y="{158-fl*13}" width="4" height="{fl*13}" fill="#5b6268"/>' for x in (20, 58, 96)) + '' + '</svg>'
months = [("August", 4), ("September", 6), ("October", 8), ("November", 9)]
P["p142_bl_s4"] = bl(4, "<div class=kt><b>3</b>MONTHLY UPDATE</div><h1>Buyers see the building grow<br><span>without visiting the site.</span></h1>",
f'''<div class=w4><div class=g4>{"".join(f'<div class="cd m4{" me" if m=="November" else ""}"><div class=im4>{bld(f)}</div><b>{m}</b><span>Slab {f} cast</span></div>' for m,f in months)}</div>
<div class="cd pr4"><div class=tp4><span class=lb>OVERALL PROGRESS · SAMPLE</span><b>Slab 9 of 10</b></div><u><s style="width:90%"></s></u><small>Next update: first week of December · photos and a 30-second video</small></div></div>''',
""".w4{flex:1;display:flex;flex-direction:column;gap:16px}
.g4{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:14px}
.m4{padding:12px;display:flex;flex-direction:column;gap:4px}.m4.me{box-shadow:0 0 0 4px #c4572e}
.im4{flex:1;border-radius:14px;overflow:hidden;min-height:0}
.m4 b{font:700 24px/1.3 Cardo;margin-top:6px}.m4 span{font:600 16px Montserrat;color:#6b7177}
.pr4{flex:none;padding:20px 24px;display:flex;flex-direction:column;gap:10px}
.tp4{display:flex;justify-content:space-between;align-items:center}.tp4 b{font:700 30px Cardo}
.pr4 u{display:block;height:16px;border-radius:8px;background:#ecebe6;position:relative;overflow:hidden}.pr4 u s{position:absolute;left:0;top:0;bottom:0;border-radius:8px;background:#c4572e}
.pr4 small{font:500 17px Montserrat;color:#6b7177}""")

P["p142_bl_s5"] = bl(5, "<h1>Building flats?<br><span>Let's build your project<br>website and buyer app.</span></h1>",
f'''<div class=w5><div class=fc5>{facade()}</div><div class=g5>{"".join(f'<div class="cd t5"><i>0{i+1}</i><b>{a}</b><span>{b}</span></div>' for i,(a,b) in enumerate([("Live availability","Sold, booked, free"),("Flat pages","Plan, floor, facing"),("Buyer stages","Done and next"),("Monthly updates","Photos for buyers")]))}</div></div>''',
FAC + """.w5{flex:1;display:flex;gap:18px}
.fc5{width:380px;flex:none;background:linear-gradient(#cfe4f2,#eef5fa);border-radius:28px;display:flex;align-items:flex-end;padding:20px 24px 0}.fc5 .bd1{width:100%}
.g5{flex:1;display:grid;grid-template-rows:repeat(4,1fr);gap:14px}
.t5{padding:14px 22px;display:flex;flex-direction:column;justify-content:center;gap:2px}
.t5 i{font:700 22px/1.35 Cardo;font-style:normal;color:#c4572e;margin-bottom:4px}.t5 b{font:700 36px/1.25 Cardo}.t5 span{font:500 20px Montserrat;color:#6b7177}""",
cta="Building flats? DM us", ctacss="background:#c4572e;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
