import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 31 INDIA · Hostel / PG owner · SINGLE · Cardo + Inter · slate / mint / coral
# New technique: building floor plan (room grid with bed dots) as the hero.
rooms = {
 "101": "ppd", "102": "pp", "103": "pdv", "104": "ppp", "105": "pv", "106": "dd",
 "201": "ppp", "202": "pd", "203": "pp", "204": "vvp", "205": "ppd", "206": "pp",
}
def room(no, beds):
    dots = "".join(f'<i class="b {c}"></i>' for c in beds)
    dues = beds.count("d")
    return f'<div class=rm><div class=rh><b>{no}</b>{f"<span class=du>{dues} due</span>" if dues else ""}</div><div class=bs>{dots}</div></div>'
floor = lambda f: "".join(room(k, v) for k, v in rooms.items() if k.startswith(f))
P["p31_pg"] = page("""
body{--f:'Inter';--h:'Cardo';background:#262a3f;color:#f3f1ea}
h1{font-size:68px;font-weight:700;letter-spacing:-.5px;line-height:1.2} h1 span{color:#8fe3c8;font-style:italic}
.sub{color:#b5b8cc}
.vis{flex-direction:column;gap:16px}
.bld{flex:1;background:#f3f1ea;border-radius:26px;padding:22px 24px;color:#262a3f;display:flex;flex-direction:column;gap:12px;min-height:0}
.bh{display:flex;justify-content:space-between;align-items:center}.bh b{font:700 30px 'Cardo'}.bh small{font:500 16px Inter;color:#6b6f85}
.lgd{display:flex;gap:18px;font:600 16px Inter;color:#4a4e66}.lgd span{display:flex;align-items:center;gap:7px}
.fl{flex:1;display:flex;flex-direction:column;gap:6px}.fl em{font:700 14px Inter;font-style:normal;letter-spacing:2px;color:#8a8ea3}
.gr{flex:1;display:grid;grid-template-columns:repeat(6,1fr);gap:0;border:3px solid #262a3f;border-radius:10px;overflow:hidden}
.rm{border-right:2px solid #262a3f;padding:12px 10px;display:flex;flex-direction:column;justify-content:space-between;background:#fff}
.rm:last-child{border-right:0}
.rh{display:flex;flex-direction:column;gap:4px}.rh b{font:800 24px Inter}.du{align-self:flex-start;font:700 14px Inter;background:#ffe1d6;color:#c2410c;border-radius:8px;padding:3px 7px}
.bs{display:flex;gap:6px;flex-wrap:wrap}
.b{width:40px;height:40px;border-radius:10px;display:block}.p{background:#2f9e78}.d{background:#ff7a59}.v{background:transparent;border:2px dashed #b9bccb}
.lgd .b{width:18px;height:18px;border-radius:5px}
.cor{height:26px;background:repeating-linear-gradient(90deg,#e4e1d6 0 18px,#f3f1ea 18px 36px);border-radius:6px;font:700 13px/26px Inter;color:#8a8ea3;text-align:center;letter-spacing:3px}
.row{display:flex;gap:14px}
.k{flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.15);border-radius:20px;padding:20px 18px;display:flex;gap:14px;align-items:center}
.k .ib{width:46px;height:46px;border-radius:14px;background:#8fe3c8;color:#262a3f}
.k b{display:block;font:700 21px/1.3 Inter}.k small{display:block;font:400 17px/1.35 Inter;color:#b5b8cc}
""", "<h1>Every bed, every rent,<br><span>on one screen.</span></h1><div class=sub>For PG and hostel owners: see who paid, who is due and which beds are free.</div>",
f'''<div class=bld><div class=bh><div><b>Sample PG · December</b><br><small>Each square is one bed</small></div><div class=lgd><span><i class="b p"></i>Paid</span><span><i class="b d"></i>Rent due</span><span><i class="b v"></i>Free bed</span></div></div>
<div class=fl><em>SECOND FLOOR</em><div class=gr>{floor("2")}</div></div><div class=cor>STAIRS · CORRIDOR</div><div class=fl><em>FIRST FLOOR</em><div class=gr>{floor("1")}</div></div></div>
<div class=row>{"".join(f'<div class=k><span class=ib>{ic(i,24)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("bell","Rent reminders","Sent on the date you set"),("file","Deposit records","Saved for every tenant"),("wrench","Complaints","Fan, water, Wi-Fi, tracked")])}</div>''',
"#f3f1ea", "Want this for your PG? DM us", "background:#8fe3c8;color:#262a3f")

# ───────── 32 USA · HVAC company · CAROUSEL 6 · Archivo Black + Roboto · cool cyan / warm red / off-white
# New format: myth vs fact, with a hot/cold split background.
HV = """
body{--f:'Roboto';--h:'Archivo Black';background:#f7f5f0;color:#14213d}
.hot{position:absolute;left:0;top:0;bottom:0;width:50%;background:linear-gradient(180deg,#fff1ee,#f7f5f0)}
.cold{position:absolute;right:0;top:0;bottom:0;width:50%;background:linear-gradient(180deg,#e6f7fb,#f7f5f0)}
h1{font-size:60px;font-weight:400;letter-spacing:-1px;line-height:1.2} h1 span{color:#e63946}
.sub{color:#56607a}
.sn{font:700 17px Roboto;letter-spacing:3px;color:#0096c7;margin-top:22px}
"""
def hslide(n, kick, title, sub, vis, css, cta="Swipe", ctacss="background:#14213d;color:#fff", bg="<div class=hot></div><div class=cold></div>"):
    return page(HV+css, f"<div class=sn>{kick}</div><h1 style='margin-top:14px'>{title}</h1><div class=sub>{sub}</div>", vis, "#14213d", cta, ctacss, bg=bg, tagline=f"{n} / 6")
MY = """.vis{flex-direction:column;gap:18px}
.my{background:#fff;border-radius:26px;padding:26px 28px;border:3px solid #f3c4c8;position:relative}
.my em{font:700 16px Roboto;font-style:normal;letter-spacing:3px;color:#e63946}
.my p{font:400 38px/1.3 'Archivo Black';color:#14213d;text-decoration:line-through;text-decoration-color:#e63946;text-decoration-thickness:4px;margin-top:8px}
.fc{flex:1;background:#14213d;color:#fff;border-radius:26px;padding:28px;display:flex;gap:26px;align-items:stretch;min-height:0}
.fc .tx{flex:1;display:flex;flex-direction:column;gap:12px;justify-content:center}
.fc em{font:700 16px Roboto;font-style:normal;letter-spacing:3px;color:#48cae4}
.fc b{font:400 46px/1.2 'Archivo Black'}
.fc small{font:400 24px/1.5 Roboto;color:#c4cadb}
.ill{width:350px;flex:none;background:#f7f5f0;border-radius:20px;color:#14213d;padding:20px;display:flex;flex-direction:column;justify-content:space-between;gap:10px}
.li{flex:1;display:flex;justify-content:space-between;align-items:center;background:#fff;border-radius:14px;padding:12px 16px;font:600 19px Roboto}
.li i{font-style:normal;font:700 14px Roboto;padding:4px 9px;border-radius:9px}
.ok{background:#d8f3dc;color:#1b7a3a}.wt{background:#fff1d6;color:#a86400}.rd{background:#ffe3e5;color:#c1121f}.bl{background:#dff4fa;color:#0077a3}
.ih{font:800 20px Roboto;margin-bottom:2px}
"""
def myth(n, num, m, f_title, f_text, ill, h="Myth or fact?"):
    return hslide(n, f"MYTH {num} OF 4", h, "Things HVAC owners often hear about software.",
        f'<div class=my><em>MYTH</em><p>{m}</p></div><div class=fc><div class=tx><em>FACT</em><b>{f_title}</b><small>{f_text}</small></div><div class=ill>{ill}</div></div>', MY)
lst = lambda title, rows: f'<div class=ih>{title}</div>' + "".join(f'<div class=li>{a}<i class={c}>{b}</i></div>' for a, b, c in rows)

P["p32_hvac_s1"] = hslide(1, "FOR HVAC COMPANIES", "4 software myths that<br>keep HVAC owners<br><span>on paper.</span>",
 "Swipe through each one. The last slide has a simple way to start.",
 f'''<div class=th><div class="half h"><span class=ib>{ic("spark",44)}</span><b>Heating</b><small>Furnace tune-ups, no-heat calls</small></div><div class="half c"><span class=ib>{ic("drop",44)}</span><b>Cooling</b><small>AC checks, summer rush</small></div>
 <div class=mid><b>4</b><span>myths</span></div></div>''',
 """.vis{display:flex}.th{flex:1;display:flex;gap:18px;position:relative}
.half{flex:1;border-radius:30px;padding:34px;display:flex;flex-direction:column;justify-content:flex-end;gap:10px}
.half .ib{width:86px;height:86px;border-radius:26px;margin-bottom:auto}
.h{background:#e63946;color:#fff}.h .ib{background:rgba(255,255,255,.2)}.c{background:#0096c7;color:#fff}.c .ib{background:rgba(255,255,255,.2)}
.half b{font:400 46px/1.2 'Archivo Black'}.half small{font:400 21px/1.4 Roboto;opacity:.9}
.mid{position:absolute;left:50%;top:40%;width:190px;height:190px;margin-left:-95px;border-radius:50%;background:#14213d;color:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center;border:10px solid #f7f5f0}
.mid b{font:400 70px/1.1 'Archivo Black'}.mid span{font:700 18px Roboto;letter-spacing:3px;text-transform:uppercase}""")

P["p32_hvac_s2"] = myth(2, 1, "Software is only for big companies.",
 "Small teams feel the gaps most.", "With two or three techs, one missed call or lost job sheet hurts. Simple software can start small and grow with you.",
 lst("Today · sample", [("Tech 1 · tune-up", "On site", "bl"), ("Tech 2 · no heat", "Urgent", "rd"), ("Tech 3 · AC check", "Done", "ok"), ("New call · 2 PM", "Booked", "ok"), ("Quote · duct work", "Sent", "wt")]), h="Too small for <span>software?</span>")
P["p32_hvac_s3"] = myth(3, 2, "My techs will never use an app.",
 "They will, if it is simple.", "Big buttons, today's jobs only, and photos instead of typing. Built around how your techs already work.",
 lst("Tech app · sample", [("Next job", "Open map", "bl"), ("Before photo", "Added", "ok"), ("Parts used", "2 items", "wt"), ("Customer sign", "Done", "ok"), ("Job status", "Complete", "ok")]), h="Will your techs <span>use it?</span>")
P["p32_hvac_s4"] = myth(4, 3, "I'd have to change how I run my business.",
 "Custom software fits your way.", "Your service names, your checklists, your steps. We build it around your process, not the other way around.",
 lst("Your checklist · sample", [("Filter check", "Yes", "ok"), ("Thermostat test", "Yes", "ok"), ("Coil cleaning", "Skip", "wt"), ("Refrigerant check", "Yes", "ok"), ("Safety check", "Yes", "ok")]), h="Will it change <span>how you work?</span>")
P["p32_hvac_s5"] = myth(5, 4, "A website is just an online brochure.",
 "It can book tune-ups for you.", "Seasonal reminders, online booking and maintenance plan sign-ups, working while you are on a roof.",
 lst("yourhvac.com · sample", [("Fall furnace tune-up", "Book", "rd"), ("Spring AC check", "Book", "bl"), ("Maintenance plan", "Join", "ok"), ("No heat? Urgent", "Request", "rd"), ("Service area", "ZIP check", "wt")]), h="Is a website <span>just a brochure?</span>")

P["p32_hvac_s6"] = hslide(6, "WHERE TO START", "Start with your<br><span>biggest headache.</span>",
 "Tell us the one thing that costs you the most time. We will suggest the simplest first step.",
 f'''<div class=w>{peep("PointingUp","Smile","ShortMessy","FullMedium",w=380,h=560)}<div class=opts>{"".join(f'<div class=o><span class=ib>{ic(i,28)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("phone","Missed calls","Online booking and requests"),("cal","Messy schedule","Dispatch board for your techs"),("file","Lost job sheets","Tech app with photos and checklists"),("rupee" if False else "dollar","Slow invoices","Invoice the moment a job is done")])}</div></div>''',
 """.vis{align-items:stretch}.w{display:flex;align-items:flex-end;gap:20px;width:100%}
.opts{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px;padding-bottom:8px}.opts .o{flex:1}
.o{display:flex;gap:16px;align-items:center;background:#fff;border-radius:22px;padding:30px 24px;box-shadow:0 14px 30px rgba(20,33,61,.08)}
.o .ib{width:56px;height:56px;border-radius:16px;background:#14213d;color:#48cae4}
.o b{display:block;font:400 28px/1.25 'Archivo Black'}.o small{display:block;font:400 21px Roboto;color:#56607a;margin-top:3px}""",
 cta="Tell us yours. DM us", ctacss="background:#e63946;color:#fff")

# ───────── 33 INDIA · Tiles & sanitary showroom · SINGLE · Open Sans + Cardo · terracotta / stone
# New mockup: laptop (CSS) with a catalogue website + tile pattern swatches.
def tile(c1, c2, kind):
    pats = {"chk": f"repeating-conic-gradient({c1} 0 25%,{c2} 0 50%) 0 0/40px 40px",
            "dia": f"repeating-linear-gradient(45deg,{c1} 0 12px,{c2} 12px 24px)",
            "plain": f"linear-gradient(135deg,{c1},{c2})",
            "hex": f"radial-gradient(circle at 50% 50%,{c2} 0 30%,{c1} 31%) 0 0/36px 36px",
            "mar": f"linear-gradient(115deg,{c1} 0 40%,{c2} 45%,{c1} 52%,{c2} 70%,{c1} 80%)",
            "brk": f"repeating-linear-gradient(0deg,{c2} 0 2px,transparent 2px 22px),repeating-linear-gradient(90deg,{c1} 0 44px,{c2} 44px 46px)"}
    return pats[kind]
tiles = [("Wall tile · glossy", "300 x 600 mm", tile("#e9e4da", "#cfc6b6", "mar")), ("Floor tile · matt", "600 x 600 mm", tile("#b7a99a", "#a39383", "plain")),
         ("Pattern tile", "200 x 200 mm", tile("#1f4e5a", "#f0e9dc", "chk")), ("Parking tile", "300 x 300 mm", tile("#8d8a86", "#6f6c69", "brk")),
         ("Bathroom wall", "250 x 375 mm", tile("#cfe3e6", "#a9c9cd", "dia")), ("Kitchen dado", "300 x 450 mm", tile("#f4efe6", "#d9b48f", "hex"))]
tcards = "".join(f'<div class=tc><div class=sw style="background:{b}"></div><b>{a}</b><small>{s} · sample</small></div>' for a, s, b in tiles)
P["p33_tiles"] = page("""
body{--f:'Open Sans';--h:'Cardo';background:#efe9e1;color:#3b2a20}
.wm,h1{color:#3b2a20}.sub{color:#6e5a4c!important}.scr .in{color:#3b2a20}
.band{position:absolute;left:0;right:0;bottom:0;height:520px;background:#b5562f}
h1{font-size:62px;font-weight:800;letter-spacing:-1.5px;font-family:'Open Sans'} h1 span{font-family:'Cardo';font-style:italic;font-weight:700;color:#b5562f;letter-spacing:0}
.sub{color:#6e5a4c}
.vis{flex-direction:column;align-items:center;justify-content:flex-start;gap:0}
.lap{width:100%;display:flex;flex-direction:column;align-items:center}
.scr{width:880px;background:#1c1c1e;border-radius:22px 22px 0 0;padding:16px 16px 0}
.scr .in{background:#fff;border-radius:8px 8px 0 0;height:650px;overflow:hidden;display:flex;flex-direction:column}
.base{width:100%;height:26px;background:linear-gradient(#d9d9dc,#b9b9bd);border-radius:0 0 26px 26px;position:relative}
.base:before{content:"";position:absolute;left:50%;top:0;width:160px;height:10px;margin-left:-80px;background:#a3a3a8;border-radius:0 0 10px 10px}
.nav{display:flex;align-items:center;justify-content:space-between;padding:14px 20px;border-bottom:1px solid #eee}.nav b{font:700 20px 'Cardo'}.nav span{font:600 14px 'Open Sans';color:#777;display:flex;gap:16px}
.flt{display:flex;gap:8px;padding:12px 20px}.flt span{font:600 14px 'Open Sans';padding:7px 13px;border-radius:20px;background:#f3eee8;color:#5a4636}.flt .on{background:#3b2a20;color:#fff}
.grd{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px;padding:4px 20px 14px;min-height:0}
.tc{background:#faf7f3;border-radius:12px;padding:10px;display:flex;flex-direction:column;gap:4px}
.sw{flex:1;border-radius:8px;min-height:0}.tc b{font:700 17px 'Open Sans'}.tc small{font:500 13px 'Open Sans';color:#8a7666}
.qbar{display:flex;align-items:center;justify-content:space-between;background:#3b2a20;color:#fff;padding:12px 20px;font:600 15px 'Open Sans'}.qbar span{background:#e4a07a;color:#3b2a20;border-radius:10px;padding:7px 12px;font-weight:700}
.chips{display:flex;gap:14px;margin-top:22px;width:100%}
.ch{flex:1;background:#fff;color:#3b2a20;border-radius:20px;padding:24px 18px;display:flex;gap:12px;align-items:center;font:700 20px/1.3 'Open Sans'}
.ch .ib{width:44px;height:44px;border-radius:12px;background:#f6e1d5;color:#b5562f}
""", "<h1>\"Send me photos of tiles\"<br><span>Send one link instead.</span></h1><div class=sub>A catalogue website for tiles and sanitary showrooms: sizes, finishes and a quote request.</div>",
f'''<div class=lap><div class=scr><div class=in><div class=nav><b>Your Tile Showroom</b><span><i>Tiles</i><i>Sanitary</i><i>Fittings</i></span></div>
<div class=flt><span class=on>All tiles</span><span>Wall</span><span>Floor</span><span>Bathroom</span><span>Kitchen</span><span>Outdoor</span></div><div class=grd>{tcards}</div>
<div class=qbar>3 tiles selected for your quote<span>Request quote</span></div></div></div><div class=base></div></div>
<div class=chips>{"".join(f'<div class=ch><span class=ib>{ic(i,22)}</span>{t}</div>' for i,t in [("grid","Filter by size and room"),("img","Clear photos of every design"),("send","Quote request in one tap")])}</div>''',
"#fff", "Want a catalogue website? DM us", "background:#fff;color:#b5562f", bg="<div class=band></div>", logo_color="#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
