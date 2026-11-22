import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 48 INDIA · Event decorator · SINGLE · Bitter + DM Sans · lilac / deep navy / marigold
# New technique: split-screen "chat bubbles vs one shared event page" (browser mockup).
qs = ["Which colour flowers did we pick?", "What time will setup start?", "Is the backdrop size final?", "Who is coming from your team?", "Can you send that photo again?"]
items = [("Backdrop 10 x 8 ft", "Packed"), ("Entry arch with flowers", "Packed"), ("12 table centrepieces", "Making"), ("Fairy lights, 20 strings", "Packed"), ("Stage carpet", "Ordered")]
P["p48_decorator"] = page("""
body{--f:'DM Sans';--h:'Bitter';background:#e9e3f7;color:#1c2140}
h1{font-family:'Bitter';font-size:64px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#6b4fd8}
.sub{color:#545a7a}
.vis{gap:22px;align-items:stretch}
.ch{width:350px;flex:none;background:#d8cfef;border-radius:28px;padding:24px 20px;display:flex;flex-direction:column;gap:14px}
.ch .t{font:800 15px 'DM Sans';letter-spacing:3px;color:#6b4fd8}
.bb{flex:1;display:flex;align-items:center;background:#fff;border-radius:22px 22px 22px 6px;padding:0 18px;font:600 20px/1.35 'DM Sans';box-shadow:0 8px 18px rgba(28,33,64,.08);margin-right:34px}
.bb.r{border-radius:22px 22px 6px 22px;margin:0 0 0 34px;background:#fff8e6}
.tm{font:700 16px 'DM Sans';color:#7b6fa8;text-align:center}
.ev{flex:1;min-width:0}
.ebody{flex:1;padding:22px 24px;display:flex;flex-direction:column;gap:14px;background:#fff}
.eh{display:flex;justify-content:space-between;align-items:flex-start}.eh b{display:block;font:800 28px 'Bitter'}.eh small{font:600 17px 'DM Sans';color:#6b7090}
.eh i{font-style:normal;font:800 13px 'DM Sans';letter-spacing:2px;background:#ffe2a8;color:#8a5a00;padding:6px 10px;border-radius:8px}
.row2{display:flex;gap:12px}
.bx2{flex:1;background:#f4f1fb;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:8px}
.bx2 em{font:800 13px 'DM Sans';font-style:normal;letter-spacing:2px;color:#6b4fd8}
.sw{display:flex;gap:8px}.sw i{width:38px;height:38px;border-radius:50%;display:block}
.bx2 b{font:800 22px 'DM Sans'}
.its{flex:1;display:flex;flex-direction:column;gap:7px}
.it{flex:1;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid #ece8f6;font:600 19px 'DM Sans'}
.it span{font:700 14px 'DM Sans';padding:5px 10px;border-radius:9px;background:#e3f4e8;color:#2c7a43}.it span.mk{background:#fff0d1;color:#9a6500}.it span.od{background:#e8e4fb;color:#5a44c2}
.crw{display:flex;align-items:center;gap:8px;font:700 18px 'DM Sans'}.crw i{width:40px;height:40px;border-radius:50%;background:#1c2140;color:#ffc145;font:800 16px/40px 'DM Sans';font-style:normal;text-align:center}
.crw small{margin-left:6px;color:#6b7090;font-weight:600}
.lnk{background:#1c2140;color:#fff;border-radius:20px;padding:18px 22px;display:flex;align-items:center;gap:14px;font:700 22px/1.3 'DM Sans'}
.lnk .ib{width:48px;height:48px;border-radius:14px;background:#ffc145;color:#1c2140}
.rc{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
""", "<h1>Same 5 questions<br><span>from every client?</span></h1><div class=sub>For event decorators: one event page with theme, items, setup time and crew.</div>",
f'''<div class=ch><div class=t>BEFORE · IN CHATS</div>{"".join(f'<div class="bb {"r" if k%2 else ""}">{q}</div>' for k,q in enumerate(qs))}<div class=tm>…and again the next day</div></div>
<div class=rc>{browser(f"""<div class=ebody><div class=eh><div><b>Sample Event</b><small>Saturday · Hall B · 300 guests</small></div><i>SAMPLE</i></div>
<div class=row2><div class=bx2><em>THEME</em><div class=sw><i style="background:#f4c2c2"></i><i style="background:#ffd166"></i><i style="background:#ffffff;box-shadow:inset 0 0 0 2px #ddd"></i><i style="background:#7fb685"></i></div></div><div class=bx2><em>SETUP</em><b>2 pm to 6 pm</b></div></div>
<div class=its>{"".join(f'<div class=it>{a}<span class="{ {"Making":"mk","Ordered":"od"}.get(b,"")}">{b}</span></div>' for a,b in items)}</div>
<div class=crw>{"".join(f"<i>{c}</i>" for c in "ARSM")}<small>4 crew members · photos added</small></div></div>""", "yourdecor.in/event/sample", style="flex:1;width:100%")}
<div class=lnk><span class=ib>{ic("send",24)}</span>Share one link. Every answer is there.</div></div>''',
"#1c2140", "Want this for your events? DM us", "background:#6b4fd8;color:#fff")

# ───────── 49 USA · Electrician · CAROUSEL 5 · Anton + DM Sans · electric yellow / deep indigo / white
# New technique: hazard-tape stripe bands + big outlined sign numbers.
EL = """
body{--f:'DM Sans';--h:'Anton';background:#1b1f4b;color:#fff}
h1{font-family:'Anton';font-weight:400;font-size:74px;letter-spacing:.5px;line-height:1.2;margin-top:32px} h1 span{color:#ffd400}
.sub{color:#c3c6e6}
.tape{height:26px;border-radius:6px;background:repeating-linear-gradient(-45deg,#ffd400 0 22px,#1b1f4b 22px 44px);margin-top:20px}
.kick{font:800 17px 'DM Sans';letter-spacing:4px;color:#ffd400;margin-top:22px}
"""
def el(n, head, vis, css, cta="Swipe", ctacss="background:#ffd400;color:#1b1f4b"):
    return page(EL + css, head, vis, "#ffffff", cta, ctacss, tagline=f"{n} / 5")
SG = """.vis{flex-direction:column;gap:18px}
.sg{display:flex;gap:22px;align-items:center;margin-top:14px}
.sg .nm{font:400 150px/1 'Anton';color:transparent;-webkit-text-stroke:3px #ffd400;width:120px;flex:none;text-align:center;padding-top:16px}
.sg b{font:800 15px 'DM Sans';letter-spacing:3px;color:#ffd400;display:block}.sg p{font:700 36px/1.3 'DM Sans'}
.fx{flex:1;background:#fff;color:#1b1f4b;border-radius:26px;padding:26px;display:flex;gap:24px;min-height:0}
.fx .t{width:320px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:12px}
.fx em{font:800 15px 'DM Sans';font-style:normal;letter-spacing:3px;color:#2d6cdf}.fx .t b{font:400 54px/1.25 'Anton';letter-spacing:.5px}.fx .t small{font:500 22px/1.5 'DM Sans';color:#4a4f78}
.mo{flex:1;background:#f3f4fb;border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:10px;min-width:0}
.mo h5{font:800 19px 'DM Sans';display:flex;justify-content:space-between}.mo h5 span{font:800 12px 'DM Sans';letter-spacing:2px;color:#8a8fb5}
"""
def sign(n, num, bad, ft, fs, mo):
    return el(n, f"<div class=tape></div><h1>Signs you need<br><span>a booking website.</span></h1>",
              f'<div class=sg><div class=nm>{num}</div><div><b>SIGN {num} OF 3</b><p>{bad}</p></div></div><div class=fx><div class=t><em>THE FIX</em><b>{ft}</b><small>{fs}</small></div>{mo}</div>', SG)

P["p49_electrician_s1"] = el(1, """<div class=kick>FOR ELECTRICIANS</div><h1 style="margin-top:14px">3 signs your business<br>needs a <span>booking website.</span></h1>
<div class=sub>If even one sounds like your week, swipe.</div>""",
f'''<div class=tape style="margin:0"></div><div class=ov>{"".join(f'<div class=oc><span>{i}</span><p>{t}</p></div>' for i,t in [(1,"You miss calls while you are on a job."),(2,"You ask the same quote questions every time."),(3,"People keep asking, “Do you serve my area?”")])}</div><div class=tape style="margin:0"></div>''',
""".vis{flex-direction:column;gap:20px}
.ov{flex:1;display:flex;flex-direction:column;gap:16px}
.oc{flex:1;background:#262b63;border-radius:24px;display:flex;align-items:center;gap:26px;padding:0 30px}
.oc span{font:400 110px/1 'Anton';color:transparent;-webkit-text-stroke:3px #ffd400;width:90px;text-align:center;padding-top:10px}
.oc p{font:700 34px/1.3 'DM Sans'}
""")

calls = [("Missed call", "9:12 am"), ("Missed call", "10:40 am"), ("Missed call", "1:05 pm"), ("Voicemail", "3:30 pm")]
P["p49_electrician_s2"] = sign(2, 1, "You miss calls while you are on a job.", "Booking that works while you work.", "Customers pick a time slot and describe the job. You check it between jobs.",
 f'''<div class=mo><h5>Booking requests <span>SAMPLE</span></h5>{"".join(f'<div class=br><div><b>{a}</b><small>{b}</small></div><i>{c}</i></div>' for a,b,c in [("Outlet not working","Tue · 9 to 11 am","New"),("Ceiling fan install","Tue · 2 to 4 pm","New"),("Panel check","Wed · 8 to 10 am","Booked"),("Porch light wiring","Wed · 1 to 3 pm","Booked")])}<div class=nt>{ic("bell",20)} 4 requests came in while you were on site</div></div>''') \
 .replace("</style>", """.br{flex:1;display:flex;align-items:center;justify-content:space-between;background:#fff;border-radius:14px;padding:0 16px}
.br b{display:block;font:700 21px 'DM Sans'}.br small{font:500 17px 'DM Sans';color:#6a6f96}
.br i{font-style:normal;font:800 13px 'DM Sans';padding:6px 10px;border-radius:9px;background:#fff3b0;color:#6b5600}
.nt{display:flex;align-items:center;gap:8px;font:700 16px 'DM Sans';color:#2d6cdf}</style>""")

P["p49_electrician_s3"] = sign(3, 2, "You ask the same quote questions every time.", "A quote form that asks for you.", "Type of work, photos of the problem and the address, all before you call back.",
 f'''<div class=mo><h5>Get a quote <span>SAMPLE</span></h5>
<div class=fl><small>What do you need?</small><div class=chp><i class=on>Repair</i><i>New install</i><i>Inspection</i></div></div>
<div class=fl><small>Tell us about it</small><div class=inp>Two outlets in the kitchen stopped working.</div></div>
<div class=fl><small>Add photos</small><div class=ph><i>{ic("camera",24)}</i><i>{ic("camera",24)}</i><i class=ad>+</i></div></div>
<div class=fl><small>Best time to call back</small><div class=chp><i>Morning</i><i class=on>Afternoon</i><i>Evening</i></div></div><div class=fl><small>ZIP code</small><div class=inp>Your ZIP code</div></div><div class=sb>Send request</div></div>''') \
 .replace("</style>", """.fl{display:flex;flex-direction:column;gap:7px;margin-bottom:6px}.fl small{font:700 17px 'DM Sans';color:#4a4f78}
.chp{display:flex;gap:8px}.chp i{font-style:normal;font:700 17px 'DM Sans';padding:8px 12px;border-radius:12px;background:#fff;border:2px solid #dfe1f0}.chp i.on{background:#1b1f4b;color:#ffd400;border-color:#1b1f4b}
.inp{background:#fff;border:2px solid #dfe1f0;border-radius:12px;padding:12px 14px;font:500 18px/1.35 'DM Sans';color:#3a3f66}
.ph{display:flex;gap:8px}.ph i{width:58px;height:50px;border-radius:12px;background:#dde3f7;color:#2d6cdf;display:flex;align-items:center;justify-content:center;font:800 24px 'DM Sans';font-style:normal}.ph i.ad{background:#fff;border:2px dashed #b9bedb;color:#8a8fb5}
.sb{margin-top:auto;background:#ffd400;color:#1b1f4b;border-radius:12px;padding:12px;text-align:center;font:800 18px 'DM Sans'}</style>""")

zones = "".join(f'<i class="{c}"></i>' for c in "oooxxooooxooooooxoooooxxooooooox")
P["p49_electrician_s4"] = sign(4, 3, "People keep asking, “Do you serve my area?”", "A service area page.", "Customers type their ZIP code and get the answer at once.",
 f'''<div class=mo><h5>Service area <span>SAMPLE</span></h5><div class=map>{zones}<em class=pin>{ic("pin",34,w=2.4)}</em></div>
<div class=lgd><span><i></i>We serve</span><span><i class=x></i>Outside our area</span></div><div class=zp><span>Your ZIP code</span><b>Check</b></div><div class=ok>{ic("check",20,w=3)} Yes, we serve your area.</div></div>''') \
 .replace("</style>", """.map{flex:1;display:grid;grid-template-columns:repeat(8,1fr);gap:5px;background:#dfe6f7;border-radius:14px;padding:10px;position:relative;min-height:0}
.map i{border-radius:5px;background:#ffd400}.map i.x{background:#c4cbe3}
.pin{position:absolute;left:44%;top:30%;color:#1b1f4b}
.zp{display:flex;background:#fff;border:2px solid #dfe1f0;border-radius:12px;overflow:hidden;font:600 16px 'DM Sans'}.zp span{flex:1;padding:11px 12px;color:#6a6f96}.zp b{background:#1b1f4b;color:#ffd400;padding:11px 16px}
.lgd{display:flex;gap:18px;font:700 15px 'DM Sans';color:#4a4f78}.lgd span{display:flex;align-items:center;gap:6px}.lgd i{width:16px;height:16px;border-radius:4px;background:#ffd400;display:block}.lgd i.x{background:#c4cbe3}
.ok{display:flex;align-items:center;gap:8px;font:800 17px 'DM Sans';color:#1d8a4a}</style>""")

P["p49_electrician_s5"] = el(5, """<div class=kick>BUILT FOR ELECTRICIANS</div><h1 style="margin-top:14px">Want a website that<br><span>books jobs for you?</span></h1>
<div class=sub>We build booking sites for electricians in the US and Canada.</div>""",
f'''<div class=w>{peep("PointingUp","Smile","ShortVolumed","Chin",w=400,h=700)}<div class=ops>{"".join(f'<div class=op><span class=ib>{ic(i,30)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i,a,b in [("cal","Online booking","Day and time slots you choose"),("doc","Quote request form","Photos, details and address"),("map","Service area page","ZIP code check"),("bell","Instant alerts","New requests on your phone")])}</div></div>''',
""".vis{align-items:stretch}.w{display:flex;align-items:flex-end;gap:16px;width:100%}
.ops{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.op{flex:1;background:#fff;color:#1b1f4b;border-radius:22px;padding:0 24px;display:flex;align-items:center;gap:18px;border-left:12px solid #ffd400}
.op .ib{width:60px;height:60px;border-radius:16px;background:#1b1f4b;color:#ffd400}
.op b{display:block;font:400 38px/1.3 'Anton';letter-spacing:.5px;margin-bottom:6px}.op small{font:500 21px/1.3 'DM Sans';color:#4a4f78}
""", cta="Tell us about your work. DM us")

# ───────── 50 INDIA · Spa centre · SINGLE · Lora + Source Sans 3 · eucalyptus / linen / clay
# New technique: frosted-glass cards (backdrop-filter) over soft blurred colour blobs.
slots = [("Therapist A", ["b", "b", "f", "b", "f"]), ("Therapist B", ["f", "b", "b", "f", "b"]), ("Therapist C", ["b", "f", "b", "b", "f"])]
P["p50_spa"] = page("""
body{--f:'Source Sans 3';--h:'Lora';background:#eee6da;color:#24352e}
.blob{position:absolute;border-radius:50%;filter:blur(60px)}
h1{font-family:'Lora';font-size:66px;font-weight:700;letter-spacing:-1px} h1 span{color:#b5643c;font-style:italic}
.sub{color:#56665e}
.vis{flex-direction:column;gap:18px}
.gl{background:rgba(255,255,255,.45);backdrop-filter:blur(18px);-webkit-backdrop-filter:blur(18px);border:1.5px solid rgba(255,255,255,.8);border-radius:28px;box-shadow:0 20px 50px rgba(36,53,46,.10)}
.top{display:flex;gap:18px}
.mc{flex:1.25;padding:26px 28px;display:flex;flex-direction:column;gap:14px;background:linear-gradient(135deg,rgba(62,107,90,.92),rgba(36,53,46,.92));color:#f3efe6;border-color:rgba(255,255,255,.25)}
.mc small{font:700 14px 'Source Sans 3';letter-spacing:3px;color:#b9d3c6}.mc b{font:700 32px 'Lora'}
.ss{display:flex;gap:10px}.ss i{flex:1;height:54px;border-radius:14px;background:rgba(255,255,255,.12);border:2px dashed rgba(255,255,255,.35)}.ss i.u{background:#d9a07c;border:0}
.mc p{font:600 21px 'Source Sans 3';display:flex;justify-content:space-between}.mc p span{color:#ffd9bf}
.lf{flex:.75;padding:24px;display:flex;flex-direction:column;justify-content:center;align-items:center;gap:4px;text-align:center}
.lf b{font:700 110px/1.25 'Lora';color:#b5643c}.lf span{font:700 22px/1.3 'Source Sans 3'}.lf small{font:600 17px 'Source Sans 3';color:#56665e}
.grid{flex:1;padding:20px 24px;display:flex;flex-direction:column;gap:8px;min-height:0}
.grid h5{font:700 22px 'Lora';display:flex;justify-content:space-between;align-items:center}.grid h5 small{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#7d8c84}
.gr{flex:1;display:grid;grid-template-columns:150px repeat(5,1fr);gap:8px;align-items:stretch}
.gr>span{display:flex;align-items:center;font:700 18px 'Source Sans 3'}
.gr.hd{flex:.5}.gr.hd span{justify-content:center;font:700 15px 'Source Sans 3';color:#7d8c84}.gr.hd span:first-child{justify-content:flex-start}
.gr i{border-radius:12px;font-style:normal;display:flex;align-items:center;justify-content:center;font:700 15px 'Source Sans 3'}
.gr i.b{background:#3e6b5a;color:#eaf3ee}.gr i.f{background:rgba(255,255,255,.7);color:#3e6b5a;border:2px dashed #a9c2b6}
.rm{display:flex;gap:16px;align-items:center;padding:18px 22px;font:600 21px/1.35 'Source Sans 3'}
.rm .ib{width:52px;height:52px;border-radius:50%;background:#b5643c;color:#fff}
""", "<h1>6 sessions in the package.<br><span>How many are left?</span></h1><div class=sub>For spas: packages, sessions and therapist slots in one simple app.</div>",
f'''<div class=top><div class="gl mc"><small>PACKAGE · SAMPLE MEMBER</small><b>Relax package</b><div class=ss>{"".join('<i class=u></i>' for _ in range(4))}<i></i><i></i></div><p>4 used <span>Valid till 31 Dec</span></p></div>
<div class="gl lf"><b>2</b><span>sessions left</span><small>shown at the desk</small></div></div>
<div class="gl grid"><h5>Today's slots <small>SAMPLE</small></h5><div class="gr hd"><span></span>{"".join(f"<span>{t}</span>" for t in ["11 am","1 pm","3 pm","5 pm","7 pm"])}</div>
{"".join(f'<div class=gr><span>{n}</span>{"".join(f"<i class={c}>{"Booked" if c=="b" else "Free"}</i>" for c in cs)}</div>' for n,cs in slots)}</div>
<div class="gl rm"><span class=ib>{ic("bell",24)}</span>Package ends soon? The member gets a reminder to book the last 2 sessions.</div>''',
"#24352e", "Want this for your spa? DM us", "background:#3e6b5a;color:#fff",
bg='<div class=blob style="width:620px;height:620px;left:-160px;top:420px;background:#9cc3b0"></div><div class=blob style="width:560px;height:560px;right:-140px;top:700px;background:#e7b08f"></div><div class=blob style="width:420px;height:420px;right:120px;top:-120px;background:#c9dccf"></div>')

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
