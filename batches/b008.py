import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 56 INDIA · Laundry and dry cleaning · SINGLE · Lora + Montserrat · powder blue / lavender / ink navy
# New technique: clothes rail with SVG hangers, each garment carrying a live status tag.
def garment(kind, col):
    hook = '<path d="M100 8 q14 0 14 13 q0 10-14 15 v8" fill="none" stroke="#2b2f55" stroke-width="5" stroke-linecap="round"/><path d="M100 44 L22 78 h156 Z" fill="none" stroke="#2b2f55" stroke-width="5" stroke-linejoin="round"/>'
    if kind == "shirt":
        body = f'<path d="M58 66 L100 76 L142 66 L182 96 L166 128 L148 118 L148 236 L52 236 L52 118 L34 128 L18 96 Z" fill="{col}" stroke="#2b2f55" stroke-width="4" stroke-linejoin="round"/><path d="M100 76 v160" stroke="#2b2f55" stroke-width="3" opacity=".35"/><circle cx="100" cy="110" r="4" fill="#2b2f55"/><circle cx="100" cy="146" r="4" fill="#2b2f55"/><circle cx="100" cy="182" r="4" fill="#2b2f55"/>'
    elif kind == "dress":
        body = f'<path d="M70 70 L130 70 L138 120 L176 236 L24 236 L62 120 Z" fill="{col}" stroke="#2b2f55" stroke-width="4" stroke-linejoin="round"/><path d="M62 120 h76" stroke="#2b2f55" stroke-width="3" opacity=".4"/>'
    elif kind == "coat":
        body = f'<path d="M56 66 L100 82 L144 66 L176 100 L176 236 L24 236 L24 100 Z" fill="{col}" stroke="#2b2f55" stroke-width="4" stroke-linejoin="round"/><path d="M100 82 L86 150 L100 236 M100 82 L114 150" stroke="#2b2f55" stroke-width="3" fill="none" opacity=".45"/><rect x="40" y="170" width="34" height="8" rx="4" fill="#2b2f55" opacity=".4"/><rect x="126" y="170" width="34" height="8" rx="4" fill="#2b2f55" opacity=".4"/>'
    else:  # folded blanket on hanger
        body = f'<rect x="26" y="76" width="148" height="160" rx="10" fill="{col}" stroke="#2b2f55" stroke-width="4"/><path d="M26 116 h148 M26 156 h148 M26 196 h148" stroke="#2b2f55" stroke-width="3" opacity=".3"/>'
    return f'<svg viewBox="0 0 200 240" width="160" height="192">{hook}{body}</svg>'

rail = [("shirt", "#ffffff", "#A-211", "Picked up", "s1"), ("dress", "#c9b8f2", "#A-212", "Washing", "s2"),
        ("coat", "#7d8fc9", "#A-213", "Ironing", "s3"), ("shirt", "#bfe3f5", "#A-214", "Ready", "s4"), ("blanket", "#f3d9e4", "#A-215", "Out for delivery", "s5")]
P["p56_laundry"] = page("""
body{--f:'Montserrat';--h:'Lora';background:#dcecf7;color:#1d2148}
h1{font-family:'Lora';font-size:68px;font-weight:700;letter-spacing:-1px} h1 span{color:#6b4fd8;font-style:italic}
.sub{color:#4a5177}
.vis{flex-direction:column;gap:20px}
.rk{flex:none;background:#f7fbff;border-radius:30px;position:relative;display:flex;justify-content:space-around;align-items:flex-start;padding:22px 26px 62px}
.bar{position:absolute;left:30px;right:30px;top:28px;height:12px;border-radius:6px;background:#2b2f55}
.hg{display:flex;flex-direction:column;align-items:center;gap:6px;position:relative;z-index:1}
.tg{background:#fff;border:2px solid #2b2f55;border-radius:12px;padding:8px 10px;text-align:center;min-width:150px}
.tg b{display:block;font:700 17px Montserrat}.tg span{display:inline-block;margin-top:4px;font:700 16px Montserrat;padding:4px 10px;border-radius:8px}
.s1{background:#eef0f7;color:#4a5177}.s2{background:#e6defc;color:#5a3fc4}.s3{background:#dbe4ff;color:#2d49b8}.s4{background:#d6f5e3;color:#15803d}.s5{background:#ffe6d1;color:#b45309}
.rl{position:absolute;left:30px;bottom:22px;font:800 14px Montserrat;letter-spacing:3px;color:#8a90b5}
.bt{flex:1;display:flex;gap:18px}
.oc{flex:1.15;background:#1d2148;color:#fff;border-radius:26px;padding:22px 26px;display:flex;flex-direction:column;gap:10px}
.oc small{font:700 14px Montserrat;letter-spacing:3px;color:#b9b0ff}.oc h4{font:700 32px Lora}
.it{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,.15);font:600 23px Montserrat}
.it em{font-style:normal;font:600 17px Montserrat;color:#b9b0ff}
.msg{flex:1;background:#fff;border-radius:26px;padding:22px 24px;display:flex;flex-direction:column;gap:12px}
.msg small{font:700 14px Montserrat;letter-spacing:3px;color:#8a90b5}
.bub{background:#e6defc;border-radius:20px 20px 20px 6px;padding:18px 20px;font:600 23px/1.4 Montserrat}
.pk{flex:1;display:flex;align-items:center;gap:12px;background:#dcecf7;border-radius:16px;padding:0 16px;font:700 20px/1.3 Montserrat}
.pk svg{color:#6b4fd8;flex:none}
""", "<h1>“Are my clothes ready?”<br><span>Customers can just check.</span></h1><div class=sub>For laundry and dry cleaning shops: pickup booking and live order status.</div>",
f'''<div class=rk><div class=bar></div>{"".join(f'<div class=hg>{garment(k,c)}<div class=tg><b>{o}</b><span class={s}>{st}</span></div></div>' for k,c,o,st,s in rail)}<div class=rl>TODAY'S RAIL · SAMPLE</div></div>
<div class=bt><div class=oc><small>ORDER #A-214 · SAMPLE</small><h4>Pickup: Mon, 9 to 11 am</h4>{"".join(f'<div class=it>{a}<em>{b}</em></div>' for a,b in [("5 shirts","Wash + iron"),("1 suit","Dry clean"),("2 bedsheets","Wash"),("1 silk saree","Dry clean")])}</div>
<div class=msg><small>SENT ON ITS OWN</small><div class=bub>Your order #A-214 is ready. Delivery today, 6 to 8 pm.</div><div class=pk>{ic("truck",30)}Book a pickup from your website</div><div class=pk>{ic("bell",30)}Status update at every step</div><div class=pk>{ic("rupee",30)}Pay by UPI on delivery</div></div></div>''',
"#1d2148", "Run a laundry? DM us", "background:#6b4fd8;color:#fff")

# ───────── 58 USA · Junk removal · SINGLE · Anton + Roboto · forest green / safety orange / off-white
# New technique: side-view CSS truck with a load-level selector (how full the truck gets).
P["p58_junk"] = page("""
body{--f:'Roboto';--h:'Anton';background:#f4f1ea;color:#16301f}
h1{font-family:'Anton';font-weight:400;font-size:84px;letter-spacing:.5px;line-height:1.25;margin-top:30px;text-transform:uppercase} h1 span{color:#f26b1d}
.sub{color:#4c5d50}
.vis{flex-direction:column;gap:20px}
.tk{flex:1;background:#16301f;border-radius:30px;position:relative;overflow:hidden;padding:26px 30px;display:flex;flex-direction:column}
.tk small{font:700 15px Roboto;letter-spacing:3px;color:#9fd3ae}
.tk h4{font:400 34px/1.3 Anton;color:#fff;margin-top:8px;letter-spacing:.5px}
.scene{flex:1;position:relative;margin-top:10px}
.road{position:absolute;left:0;right:0;bottom:0;height:16px;border-radius:8px;background:#0d1f13}
.bed{position:absolute;left:30px;bottom:60px;width:470px;height:270px;border:8px solid #f4f1ea;border-top:none;border-radius:0 0 10px 10px;display:flex;flex-direction:column-reverse;padding:6px;gap:6px;overflow:hidden}
.ly{height:calc((100% - 18px)/4);display:flex;gap:6px}
.ly i{flex:1;border-radius:6px;display:block}
.ly.e i{background:transparent;border:3px dashed rgba(244,241,234,.3)}
.half{position:absolute;left:30px;width:470px;bottom:196px;height:42px;border-bottom:4px dashed #f26b1d;}
.half span{position:absolute;right:8px;top:2px;font:700 17px Roboto;color:#f26b1d;background:#16301f;padding:2px 8px;border-radius:8px}
.cab{position:absolute;left:510px;bottom:60px;width:150px;height:190px;background:#f26b1d;border-radius:12px 50px 10px 10px}
.win{position:absolute;right:16px;top:20px;width:66px;height:54px;background:#cfe9ff;border-radius:6px 30px 6px 6px}
.wh{position:absolute;bottom:12px;width:84px;height:84px;border-radius:50%;background:#0d1f13;border:14px solid #3c4a40}
.lv{position:absolute;right:0;top:0;bottom:30px;width:230px;display:flex;flex-direction:column;gap:10px}
.lv div{flex:1;border-radius:14px;background:#24402d;color:#cfe3d4;display:flex;align-items:center;justify-content:space-between;padding:0 16px;font:700 21px Roboto}
.lv div em{font-style:normal;font:500 16px Roboto}
.lv div.on{background:#f26b1d;color:#fff}
.fm{display:flex;gap:18px;flex:none;height:300px}
.ph{flex:1;background:#fff;border-radius:26px;padding:22px;display:flex;flex-direction:column;gap:12px}
.ph small,.ch small{font:700 14px Roboto;letter-spacing:3px;color:#7d8a80}
.th{flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
.th div{border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;font:600 16px Roboto;color:#fff}
.ch{flex:1.2;background:#fff;border-radius:26px;padding:22px;display:flex;flex-direction:column;gap:12px}
.cps{display:flex;flex-wrap:wrap;gap:10px}
.cps span{font:600 21px Roboto;padding:11px 15px;border-radius:12px;background:#eef1ec}
.cps span.y{background:#16301f;color:#fff}
.zp{display:flex;gap:10px;margin-top:auto}.zp div{flex:1;border:2px solid #d6dcd3;border-radius:12px;padding:12px;font:600 18px Roboto;color:#4c5d50}
.zp b{background:#f26b1d;color:#fff;border-radius:12px;padding:12px 18px;font:700 18px Roboto}
""", "<h1>Send photos.<br><span>Get a quote back.</span></h1><div class=sub>For junk removal companies: customers show the job before you drive out.</div>",
f'''<div class=tk><small>STEP 2 OF 3 · SAMPLE QUOTE FORM</small><h4>How full will the truck be?</h4>
<div class=scene><div class=bed>{"".join(f'<div class="ly{"" if r<2 else " e"}">{"".join(f"<i style=background:{c}></i>" if c else "<i></i>" for c in cs)}</div>' for r,cs in enumerate([["#c9a27a","#8fb7d9","#e8c46a","#b48ad6"],["#e8c46a","#c9a27a","#9fd3ae"],["",""],["",""]]))}</div>
<div class=half><span>HALF TRUCK</span></div><div class=cab><div class=win></div></div><div class=wh style="left:70px"></div><div class=wh style="left:370px"></div><div class=wh style="left:550px"></div><div class=road></div>
<div class=lv>{"".join(f'<div class="{"on" if a=="1/2" else ""}">{a}<em>{b}</em></div>' for a,b in [("1/4","a few items"),("1/2","a room"),("3/4","a garage"),("Full","a whole move-out")])}</div></div></div>
<div class=fm><div class=ph><small>3 PHOTOS ADDED</small><div class=th>{"".join(f'<div style="background:{c}">{ic("img",34)}{t}</div>' for c,t in [("#7a9c86","Garage"),("#c08457","Sofa"),("#5f7f9e","Boxes")])}</div></div>
<div class=ch><small>WHAT GOES</small><div class=cps>{"".join(f'<span class="{"y" if y else ""}">{t}</span>' for t,y in [("Sofa",1),("Mattress",0),("Boxes",1),("Old TV",0),("Yard waste",0),("Bike",1),("Fridge",0),("Desk",1),("Carpet",0)])}</div>
<div class=zp><div>ZIP code: 78701</div><b>Send</b></div></div></div>''',
"#16301f", "Haul junk? Let's build your form. DM us", "background:#f26b1d;color:#fff")

# ───────── 59 INDIA · Society / RWA management · SINGLE · Gelasio + Inter · cork brown / marker red / paper white
# New technique: cork notice board texture (layered radial gradients) with pinned paper notices vs one app card.
P["p59_society"] = page("""
body{--f:'Inter';--h:'Gelasio';background:#fbf6ee;color:#2a1d14}
h1{font-family:'Gelasio';font-size:66px;font-weight:700;letter-spacing:-1px} h1 span{color:#d6342b}
.sub{color:#6d5a4b}
.vis{gap:20px}
.cork{flex:1;border-radius:28px;border:14px solid #7a4e2d;background:radial-gradient(circle at 20% 30%,#c08a5a 1.5px,transparent 2.5px) 0 0/14px 14px,radial-gradient(circle at 70% 60%,#a8703f 1.5px,transparent 2.5px) 0 0/18px 18px,#c99561;position:relative;overflow:hidden;box-shadow:inset 0 0 30px rgba(0,0,0,.25)}
.nt{position:absolute;background:#fffdf6;padding:22px 18px 16px;box-shadow:0 8px 14px rgba(0,0,0,.22);font:500 18px/1.35 Inter;color:#2a1d14}
.nt b{display:block;font:700 22px/1.25 Gelasio;margin-bottom:6px}
.nt:before{content:"";position:absolute;top:-6px;left:50%;margin-left:-11px;width:22px;height:22px;border-radius:50%;background:#d6342b;box-shadow:0 3px 4px rgba(0,0,0,.3)}
.nt.y{background:#fff2a8}.nt.p{background:#ffd9d1}
.cl{position:absolute;left:16px;right:16px;bottom:14px;background:rgba(42,29,20,.82);color:#fff;border-radius:14px;padding:12px 14px;font:600 18px/1.35 Inter}
.ap{flex:1.05;background:#fff;border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:12px;box-shadow:0 20px 50px rgba(42,29,20,.12)}
.ap small{font:700 14px Inter;letter-spacing:3px;color:#a08b7a}
.nc{background:#2a1d14;color:#fff;border-radius:20px;padding:18px 20px}
.nc b{display:block;font:700 25px/1.3 Gelasio}.nc span{font:500 18px Inter;color:#e7d6c6}
.rd{margin-top:12px;height:14px;border-radius:7px;background:#4a3a2e;overflow:hidden}.rd i{display:block;height:100%;width:80%;background:#ff6a5c;border-radius:7px}
.nc p{margin-top:8px;font:600 17px Inter;color:#ffb3aa}
.rw{flex:1;display:flex;align-items:center;justify-content:space-between;background:#fbf6ee;border-radius:16px;padding:0 18px}
.rw div b{display:block;font:700 21px Inter}.rw div span{font:500 17px Inter;color:#6d5a4b}
.rw em{font-style:normal;font:700 16px Inter;padding:6px 12px;border-radius:10px}
.ok{background:#dcf3e3;color:#16803d}.du{background:#ffe1dc;color:#c2281f}.wip{background:#fff1c2;color:#8a6200}
""", "<h1>Pinned on the board.<br><span>Read by a few flats.</span></h1><div class=sub>For housing societies: notices, maintenance bills and complaints in one app.</div>",
f'''<div class=cork>
<div class="nt" style="left:18px;top:30px;width:236px"><b>Water off Sunday</b>10 am to 2 pm, tank cleaning.</div>
<div class="nt y" style="right:18px;top:200px;width:196px"><b>Maintenance</b>Please pay by the 10th.</div>
<div class="nt p" style="left:26px;top:350px;width:210px"><b>Lift B service</b>Wednesday morning.</div>
<div class="nt" style="right:22px;top:500px;width:186px"><b>Parking</b>New stickers at the office.</div>
<div class="nt y" style="left:20px;top:600px;width:250px"><b>Committee meeting</b>Sunday, 6 pm, clubhouse.</div>
<div class=cl>Some notices get covered, torn or missed.</div></div>
<div class=ap><small>YOUR SOCIETY APP · SAMPLE</small>
<div class=nc><b>Water off on Sunday, 10 am to 2 pm</b><span>Sent to all 140 flats</span><div class=rd><i></i></div><p>Seen by 112 of 140 flats</p></div>
{"".join(f'<div class=rw><div><b>{a}</b><span>{b}</span></div><em class={c}>{d}</em></div>' for a,b,c,d in [("B-204 maintenance","November bill","ok","Paid"),("C-110 maintenance","November bill","du","Due 10th"),("Complaint: Lift B noise","Assigned to the lift team","wip","In progress"),("Complaint: Gate light","Fixed on Friday","ok","Closed"),("Visitor for A-302","Gate pass sent to the guard","ok","Approved")])}</div>''',
"#2a1d14", "On a society committee? DM us", "background:#d6342b;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
