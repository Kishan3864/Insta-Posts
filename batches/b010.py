import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 66 INDIA · Flex and signage printer · SINGLE · Montserrat + Fira Sans · process cyan / magenta / ink black
# New technique: annotated print proof with crop marks and numbered comment pins.
P["p66_flex"] = page("""
body{--f:'Fira Sans';--h:'Montserrat';background:#f1f3f4;color:#111417}
h1{font-family:'Montserrat';font-size:64px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#e6007e}
.sub{color:#545b62}
.vis{flex-direction:column;gap:18px}
.tbl{flex:1;background:#111417;border-radius:30px;padding:26px;display:flex;gap:20px}
.pf{flex:1.35;position:relative;display:flex;align-items:center;justify-content:center;background:#1d2227;border-radius:18px;padding:34px}
.pf small{position:absolute;left:16px;top:12px;font:700 13px 'Fira Sans';letter-spacing:3px;color:#7f8a94}
.cm{position:absolute;width:26px;height:26px;border-color:#7f8a94;border-style:solid;display:block}
.c1{left:14px;top:30px;border-width:2px 0 0 2px}.c2{right:14px;top:30px;border-width:2px 2px 0 0}.c3{left:14px;bottom:14px;border-width:0 0 2px 2px}.c4{right:14px;bottom:14px;border-width:0 2px 2px 0}
.bn{width:100%;aspect-ratio:1.0;background:linear-gradient(120deg,#00a6d6 0 58%,#ffe14d 58% 100%);border-radius:6px;position:relative;padding:22px;display:flex;flex-direction:column;justify-content:space-between;overflow:hidden}
.bn h3{font:900 42px/1.25 Montserrat;color:#fff;letter-spacing:-1px}
.bn p{font:600 20px 'Fira Sans';color:#06384a;margin-top:auto;margin-bottom:14px}
.bn .ph{align-self:flex-start;background:#111417;color:#ffe14d;font:800 17px Montserrat;padding:8px 12px;border-radius:6px}
.bn .cir{position:absolute;right:-30px;bottom:-30px;width:150px;height:150px;border-radius:50%;background:#e6007e;opacity:.9}
.bw{position:relative;width:100%}
.pin{position:absolute;width:44px;height:44px;border-radius:50% 50% 50% 4px;background:#e6007e;color:#fff;font:800 21px/44px Montserrat;text-align:center;box-shadow:0 0 0 4px #111417}
.cl{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.cl small{font:700 13px 'Fira Sans';letter-spacing:3px;color:#7f8a94}
.co{flex:1;background:#1d2227;border-radius:16px;padding:14px 16px;display:flex;gap:12px;align-items:center}
.co span{width:36px;height:36px;border-radius:50%;background:#e6007e;color:#fff;font:800 17px/36px Montserrat;text-align:center;flex:none}
.co b{font:500 23px/1.35 'Fira Sans';color:#f1f3f4}.co b em{display:block;font-style:normal;font:500 16px 'Fira Sans';color:#7f8a94;margin-top:4px}
.vs{display:flex;gap:10px;flex:none}
.vs div{flex:1;background:#fff;border-radius:18px;padding:16px 18px;display:flex;align-items:center;gap:12px;font:700 20px Montserrat;color:#9aa1a8}
.vs div i{width:32px;height:32px;border-radius:50%;border:3px solid #cfd4d8;display:block;flex:none}
.vs div.dn{color:#111417}.vs div.dn i{background:#00a6d6;border-color:#00a6d6}
.vs div.nw{background:#e6007e;color:#fff}.vs div.nw i{border-color:#fff;background:#fff}
""", "<h1>Proof changes on chat?<br><span>Mark them on the design.</span></h1><div class=sub>For flex and signage printers: customers tap the proof, write the change and approve it.</div>",
f'''<div class=tbl><div class=pf><small>PROOF · VERSION 2 · SAMPLE</small><i class="cm c1"></i><i class="cm c2"></i><i class="cm c3"></i><i class="cm c4"></i>
<div class=bw><div class=bn><div class="cir free"></div><h3>YOUR SHOP NAME<br>Grand Opening</h3><p>Shop 12, Main Market Road</p><div class=ph>Call: 98XXX XXXXX</div></div>
<div class="pin free" style="left:215px;bottom:28px">1</div><div class="pin free" style="right:80px;top:220px">2</div><div class="pin free" style="left:265px;bottom:150px">3</div></div></div>
<div class=cl><small>CUSTOMER'S CHANGES</small>{"".join(f'<div class=co><span>{k}</span><b>{t}<em>Customer · on version 2</em></b></div>' for k,t in [(1,"Make the phone number bigger."),(2,"Change yellow to light green."),(3,"Add our second branch address.")])}</div></div>
<div class=vs>{"".join(f'<div class={c}><i></i>{t}</div>' for t,c in [("Draft","dn"),("Changes","dn"),("Approved","nw"),("Printing","")])}</div>''',
"#111417", "Run a flex printing shop? DM us", "background:#111417;color:#fff")

# ───────── 67 INDIA · Fish and meat shop · SINGLE · Lora + Poppins · deep sea blue / ice white / salmon
# New layout: two-column "without vs with" timeline sharing one time axis (owner's morning).
before = [("7:00", "Crowd at the counter, everyone in a hurry"), ("7:30", "“Was the pomfret curry cut or fry cut?”"), ("8:15", "Prawns run out. Two customers leave."), ("9:00", "Missed calls for home delivery")]
after = [("Sat 8 pm", "Pre-orders for Sunday close"), ("6:00", "Cut list ready, sorted by item"), ("7:00", "Every order packed with a name tag"), ("8:00", "Delivery boys leave, sorted by area")]
P["p67_fishmeat"] = page("""
body{--f:'Poppins';--h:'Lora';background:#eaf3f7;color:#0f2c45}
h1{font-family:'Lora';font-size:66px;font-weight:700} h1 span{color:#e86a5a}
.sub{color:#4b6378}
.vis{flex-direction:column;gap:18px}
.tw{flex:1;display:flex;gap:16px}
.col{flex:1;border-radius:28px;padding:22px 24px;display:flex;flex-direction:column;gap:12px}
.col h4{font:700 30px Lora}
.c0{background:#fff;border:3px dashed #e8b9b2}.c0 h4{color:#c0473a}
.c1{background:#0f2c45;color:#fff}.c1 h4{color:#ffb4a8}
.ev{flex:1;display:flex;gap:14px;align-items:center}
.ev b{font:700 18px Poppins;width:86px;flex:none;padding:8px 0;border-radius:10px;text-align:center}
.c0 .ev b{background:#fde8e5;color:#c0473a}.c1 .ev b{background:#1d4466;color:#bfe3f5}
.ev span{font:500 20px/1.35 Poppins}
.ctl{background:#fff;border-radius:26px;padding:20px 24px;display:flex;flex-direction:column;gap:10px;flex:none}
.ctl small{font:700 14px Poppins;letter-spacing:3px;color:#7b8fa2}
.cr{display:flex;gap:10px}
.cr div{flex:1;background:#eaf3f7;border-radius:16px;padding:14px 16px}
.cr b{display:block;font:700 22px Lora}.cr span{font:500 17px Poppins;color:#4b6378}
.cr em{display:inline-block;margin-top:6px;font-style:normal;font:700 15px Poppins;background:#e86a5a;color:#fff;padding:4px 10px;border-radius:8px}
""", "<h1>Sunday rush at your shop?<br><span>Take pre-orders on Saturday.</span></h1><div class=sub>For fish and meat shops: pre-orders with the cut, weight and delivery slot.</div>",
f'''<div class=tw><div class="col c0"><h4>Without pre-orders</h4>{"".join(f'<div class=ev><b>{t}</b><span>{d}</span></div>' for t,d in before)}</div>
<div class="col c1"><h4>With pre-orders</h4>{"".join(f'<div class=ev><b>{t}</b><span>{d}</span></div>' for t,d in after)}</div></div>
<div class=ctl><small>SUNDAY CUT LIST · SAMPLE</small><div class=cr>{"".join(f'<div><b>{a}</b><span>{b}</span><br><em>{c}</em></div>' for a,b,c in [("Pomfret","Curry cut, cleaned","6 orders"),("Chicken","Curry cut, skinless","9 orders"),("Prawns","Cleaned, deveined","4 orders")])}</div></div>''',
"#0f2c45", "Run a fish or meat shop? DM us", "background:#e86a5a;color:#fff")

# ───────── 69 USA · Tattoo studio · SINGLE · Cardo + Fira Sans · charcoal / bone / teal ink
# New technique: CSS line-art portfolio tiles (borders, arcs, conic shapes) in a dark studio palette.
P["p69_tattoo"] = page("""
body{--f:'Fira Sans';--h:'Cardo';background:#17181a;color:#efe8dc}
h1{font-family:'Cardo';font-size:64px;font-weight:700;letter-spacing:-.5px} h1 span{color:#3fc1b0;font-style:italic}
.sub{color:#b3ab9e}
.vis{gap:20px}
.fm{flex:1.15;background:#efe8dc;color:#17181a;border-radius:28px;padding:24px 26px;display:flex;flex-direction:column;gap:10px}
.fm small{font:700 14px 'Fira Sans';letter-spacing:3px;color:#8a8275}
.fm h4{font:700 32px Cardo}
.fg{flex:1;display:flex;flex-direction:column;gap:8px;justify-content:center}
.fg label{font:700 15px 'Fira Sans';letter-spacing:2px;color:#8a8275}
.cs{display:flex;gap:8px;flex-wrap:wrap}.cs span{font:600 19px 'Fira Sans';padding:9px 13px;border-radius:12px;background:#ddd4c4}.cs span.on{background:#17181a;color:#3fc1b0}
.fi{font:600 21px 'Fira Sans';background:#fff;border-radius:12px;padding:12px 14px}
.rf{display:flex;gap:8px}.rf i{flex:1;height:64px;border-radius:12px;background:repeating-linear-gradient(45deg,#ccc2b1 0 8px,#d9cfbf 8px 16px);display:block}
.sb{background:#17181a;color:#3fc1b0;border-radius:14px;padding:15px;text-align:center;font:800 20px 'Fira Sans'}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.pt{flex:1;background:#222427;border-radius:28px;padding:20px;display:flex;flex-direction:column;gap:12px}
.pt small{font:700 14px 'Fira Sans';letter-spacing:3px;color:#8a8275}
.pg2{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}
.pg2 div{background:#efe8dc;border-radius:16px;display:flex;align-items:center;justify-content:center;overflow:hidden}
.a1{width:90px;height:90px;border-radius:50%;border:4px solid #17181a;box-shadow:0 0 0 12px #efe8dc,0 0 0 15px #17181a}
.a2{width:110px;height:56px;border:4px solid #17181a;border-radius:110px 110px 0 0;border-bottom:none}
.a3{width:80px;height:80px;border:4px solid #17181a;transform:rotate(45deg)}
.a4{width:100px;height:100px;border-radius:50%;background:conic-gradient(#17181a 0 25%,transparent 0 50%,#3fc1b0 0 75%,transparent 0)}
.a5{width:120px;height:40px;background:repeating-linear-gradient(90deg,#17181a 0 4px,transparent 4px 16px)}
.a6{width:0;height:0;border-left:50px solid transparent;border-right:50px solid transparent;border-bottom:86px solid #3fc1b0}
.pol{background:#3fc1b0;color:#17181a;border-radius:22px;padding:18px 20px;font:600 19px/1.4 'Fira Sans'}
.pol b{display:block;font:700 23px Cardo}
""", "<h1>“How much for a small one?”<br><span>Ask for a consult form.</span></h1><div class=sub>For tattoo studios: a consult form with your portfolio and policy on one page.</div>",
f'''<div class=fm><small>CONSULT REQUEST · SAMPLE</small><h4>Tell us your idea</h4>
<div class=fg><label>STYLE</label><div class=cs>{"".join(f'<span class="{"on" if o else ""}">{t}</span>' for t,o in [("Fine line",1),("Blackwork",0),("Script",0),("Color",0)])}</div></div>
<div class=fg><label>SIZE AND PLACEMENT</label><div class=fi>About 3 inches · inner forearm</div></div>
<div class=fg><label>REFERENCE PHOTOS</label><div class=rf><i></i><i></i><i></i></div></div>
<div class=fg><label>BEST DAYS</label><div class=cs>{"".join(f'<span class="{"on" if o else ""}">{t}</span>' for t,o in [("Weekdays",0),("Evenings",1),("Saturday",1)])}</div></div>
<div class=sb>Send request</div></div>
<div class=rc><div class=pt><small>YOUR WORK HERE · SAMPLE</small><div class=pg2>{"".join(f'<div><i class={c} style="display:block"></i></div>' for c in ["a1","a2","a3","a4","a5","a6"])}</div></div>
<div class=pol><b>Your policy, up front</b>Deposit, ID check and reschedule rules shown before they book. You set them.</div></div>''',
"#efe8dc", "Own a tattoo studio? DM us", "background:#3fc1b0;color:#17181a")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
