import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 21 INDIA · Kirana store · CAROUSEL 5 · Bitter + Source Sans 3 · kraft paper / ink blue / red pencil
# New technique: ruled notebook "before" vs clean ledger "after", red-pencil annotations.
KR = """
body{--f:'Source Sans 3';--h:'Bitter';background:#efe4cc;color:#1d2c5e}
body:before{content:"";position:absolute;inset:0;background:repeating-linear-gradient(90deg,rgba(120,90,40,.05) 0 2px,transparent 2px 9px)}
h1{font-size:64px;font-weight:800;letter-spacing:-1px} h1 em{font-style:normal;color:#c8372a}
.sub{color:#5a5440;font-size:25px}
.sn{font:700 17px 'Source Sans 3';letter-spacing:3px;color:#c8372a;margin-top:22px}
.card{background:#fffdf7;border-radius:22px;box-shadow:0 26px 50px rgba(70,50,10,.16)}
.row{display:flex;align-items:center;gap:14px;padding:14px 16px;border-radius:14px;background:#f5f1e6}
.row b{font:700 20px 'Source Sans 3';color:#1d2c5e}
.row small{display:block;font:500 16px 'Source Sans 3';color:#7a735e}
.av{width:46px;height:46px;border-radius:50%;background:#1d2c5e;color:#fff;font:700 18px/46px 'Bitter';text-align:center;flex:none}
.chip{font:700 15px 'Source Sans 3';padding:6px 12px;border-radius:20px;white-space:nowrap}
.tag{font:700 14px 'Source Sans 3';letter-spacing:2px;color:#7a735e}
"""
def kslide(n, kicker, title, sub, vis, viscss, cta="Swipe", ctacss="background:#1d2c5e;color:#fff"):
    return page(KR+viscss, f"<div class=sn>{kicker}</div><h1 style='margin-top:10px'>{title}</h1><div class=sub>{sub}</div>",
                vis, "#1d2c5e", cta, ctacss, tagline=f"{n} / 5")

hand = [("Flat 3B", "<s>340</s> 520", "paid half?"), ("Corner house", "1,180", "since 2nd"), ("Tea stall", "<s>600</s> <s>450</s> 760", ""),
        ("House 14", "210", "→ see back page"), ("Flat 7A", "<s>95</s> ??", "ask"), ("New family, lane 3", "430", "no number"), ("Flat 9C", "<s>150</s> 300", "+ 2 L milk"), ("Shop next door", "75", "change?"), ("Flat 2A", "640", "pay Sunday")]
lines = "".join(f'<div class=hl><span>{a}</span><span class=amt>{b}</span><i>{c}</i></div>' for a, b, c in hand)
P["p21_kirana_s1"] = kslide(1, "KIRANA &amp; GENERAL STORE", "Udhaar diary full of<br><em>cuts and arrows?</em>",
 "Here is what a simple kirana app does instead.",
 f'''<div class=nb><div class=pgL><div class=hd>Udhaar · Nov</div>{lines}</div><div class=pgR><div class=hd>Monthly lists</div>
 <div class=hl><span>Flat 3B</span><span class=amt>atta, dal, oil...</span></div><div class=hl><span>Flat 7A</span><span class=amt>same as Oct</span></div>
 <div class=hl><span>House 14</span><span class=amt>call and ask</span></div><div class=hl><span>Tea stall</span><span class=amt>milk 6 L daily?</span></div><div class=hl><span>Corner house</span><span class=amt><s>rice 5 kg</s> 10 kg</span></div><div class=hl><span>Flat 9C</span><span class=amt>soap? check</span></div><div class=hl><span>Flat 2A</span><span class=amt>old list lost</span></div>
 <div class=ring>Who paid?</div><div class=ring2>Which list?</div></div></div>''',
 """.vis{align-items:center;justify-content:center}
.nb{width:100%;height:100%;display:flex;background:#fffef8;border-radius:16px;box-shadow:0 34px 60px rgba(70,50,10,.22);position:relative;overflow:hidden}
.nb:after{content:"";position:absolute;left:50%;top:0;bottom:0;width:26px;margin-left:-13px;background:linear-gradient(90deg,rgba(0,0,0,.08),rgba(0,0,0,0) 45%,rgba(0,0,0,0) 55%,rgba(0,0,0,.08))}
.pgL,.pgR{flex:1;padding:34px 34px 24px 54px;background:repeating-linear-gradient(transparent 0 61px,#cfd9ee 61px 63px);background-position:0 26px;position:relative}
.pgL:before,.pgR:before{content:"";position:absolute;left:36px;top:0;bottom:0;width:2px;background:#f0a8a0}
.hd{font:700 26px 'Gelasio';font-style:italic;color:#1d2c5e;height:63px;line-height:63px}
.hl{height:63px;display:flex;align-items:center;gap:10px;font:italic 400 22px 'Gelasio';color:#2a3f84;white-space:nowrap;overflow:hidden}
.hl .amt{margin-left:auto;font-weight:700}.hl s{color:#c8372a}.hl i{font-size:16px;color:#c8372a}
.ring,.ring2{position:absolute;font:700 20px 'Source Sans 3';color:#fff;background:#c8372a;border-radius:30px;padding:10px 18px}
.ring{right:30px;bottom:86px;transform:rotate(-5deg)}.ring2{left:60px;bottom:30px;transform:rotate(4deg)}""")

cust = [("A", "Flat 3B", "Last paid 12 Nov", "₹520 due", "#fde7e3", "#c8372a"), ("C", "Corner house", "Last paid 2 Nov", "₹1,180 due", "#fde7e3", "#c8372a"),
        ("T", "Tea stall", "Paid today by UPI", "Clear", "#e2f3e6", "#1f7a3e"), ("H", "House 14", "Last paid 18 Nov", "₹210 due", "#fde7e3", "#c8372a"),
        ("S", "Flat 7A", "Paid 20 Nov", "Clear", "#e2f3e6", "#1f7a3e"), ("N", "Flat 9C", "Last paid 15 Nov", "₹300 due", "#fde7e3", "#c8372a"), ("K", "Flat 2A", "Paid 21 Nov", "Clear", "#e2f3e6", "#1f7a3e")]
crows = "".join(f'<div class=row><span class=av>{a}</span><div style="flex:1"><b>{n}</b><small>{d}</small></div><span class=chip style="background:{bg};color:{c}">{s}</span></div>' for a, n, d, s, bg, c in cust)
P["p21_kirana_s2"] = kslide(2, "STEP 1 · KHATA", "Every customer's khata,<br><em>in one clean list.</em>",
 "Who owes what, and since when. No flipping pages.",
 f'<div class="card L"><div class=th><b>Customer khata</b><span class=tag>SAMPLE</span></div>{crows}</div><div class=R>' +
 "".join(f'<div class=pt><span class=ib>{ic(i,28)}</span><div><b>{a}</b><small>{b}</small></div></div>' for i, a, b in
   [("search", "Find anyone fast", "Type a name or flat number."), ("rupee", "Add udhaar in 2 taps", "Amount and date, saved."), ("check", "Mark paid", "Balance updates itself.")]) + '</div>',
 """.vis{gap:24px;align-items:stretch}
.L{flex:1.25;padding:24px;display:flex;flex-direction:column;gap:11px;min-width:0}
.th{display:flex;justify-content:space-between;align-items:center;margin-bottom:6px}.th b{font:800 25px 'Bitter'}
.R{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.pt{flex:1;background:#1d2c5e;color:#fff;border-radius:22px;padding:24px 22px;display:flex;flex-direction:column;justify-content:center;gap:16px;align-items:flex-start}
.pt .ib{width:54px;height:54px;border-radius:16px;background:#f3c64b;color:#1d2c5e}
.pt b{display:block;font:700 23px/1.3 'Source Sans 3'}.pt small{display:block;font:400 18px/1.4 'Source Sans 3';color:#c4cbe6;margin-top:4px}""")

items = [("Atta", "10 kg"), ("Rice", "5 kg"), ("Toor dal", "2 kg"), ("Sugar", "2 kg"), ("Cooking oil", "2 L"), ("Tea leaves", "500 g"), ("Bath soap", "4 pcs"), ("Detergent", "1 kg"), ("Salt", "1 kg")]
irows = "".join(f'<div class=it><span class=bx>{ic("check",16,w=3)}</span><span style="flex:1">{a}</span><b>{b}</b></div>' for a, b in items)
P["p21_kirana_s3"] = kslide(3, "STEP 2 · MONTHLY LIST", "Same list every month?<br><em>Repeat it in one tap.</em>",
 "Customers send their list once. You pack it again next month.",
 f'''<div class="card L"><div class=th><div><b>Flat 3B · monthly list</b><small>Sample · last packed 1 Nov</small></div></div>{irows}<div class=btn>Repeat this list for December</div></div>
 <div class=R><div class=st><span class=tag>ORDER STATUS</span>
 {"".join(f'<div class=s><span class=dot style="background:{c}"></span><div><b>{a}</b><small>{b}</small></div></div>' for a,b,c in [("List received","Customer tapped repeat","#1f7a3e"),("Packed","Ready at the counter","#1f7a3e"),("Out for delivery","With the delivery boy","#f3a516"),("Delivered","Added to khata","#c9c2ad")])}
 </div></div>''',
 """.vis{gap:24px;align-items:stretch}
.L{flex:1.2;padding:24px;display:flex;flex-direction:column;gap:9px;min-width:0}
.th b{font:800 24px 'Bitter';display:block}.th small{font:500 16px 'Source Sans 3';color:#7a735e}.th{margin-bottom:6px}
.it{display:flex;align-items:center;gap:12px;padding:15px 16px;border-radius:12px;background:#f5f1e6;font:600 19px 'Source Sans 3'}
.it b{font-weight:700}.bx{width:26px;height:26px;border-radius:8px;background:#1f7a3e;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.btn{margin-top:auto;background:#c8372a;color:#fff;border-radius:14px;padding:15px;text-align:center;font:700 18px 'Source Sans 3'}
.R{flex:1;display:flex;min-width:0}.st{flex:1;background:#1d2c5e;border-radius:22px;padding:26px 24px;display:flex;flex-direction:column;justify-content:space-around}
.st .tag{color:#f3c64b}
.s{display:flex;gap:16px;align-items:flex-start;color:#fff}.s .dot{width:22px;height:22px;border-radius:50%;flex:none;margin-top:4px;border:4px solid rgba(255,255,255,.2)}
.s b{display:block;font:700 22px 'Source Sans 3'}.s small{display:block;font:400 17px 'Source Sans 3';color:#c4cbe6}""")

P["p21_kirana_s4"] = kslide(4, "STEP 3 · REMINDER", "A polite reminder<br><em>goes out on the 1st.</em>",
 "No awkward calls. The customer pays by UPI from the message.",
 f'''<div class=L><div class=msg><div class=mh><span class=av style="background:#c8372a">Y</span><div><b>Your Kirana Store</b><small>Sample message · 1 Dec, 9:00 AM</small></div></div>
 <div class=bub>Hello! Your balance at Your Kirana Store is <b>₹1,180</b> for November.<br><br>Tap below to see the full list and pay by UPI. Thank you!</div>
 <div class=pay><span>{ic("qr",26)}</span>View bill and pay</div></div><div class=done><span class=ib>{ic("check",24,w=3)}</span><div><b>Paid · ₹1,180</b><small>Khata updated on its own · sample</small></div></div></div>
 <div class=R>{"".join(f'<div class=d><b>{a}</b><span>{b}</span></div>' for a,b in [("1st","Friendly reminder"),("5th","Gentle follow-up"),("10th","You decide: call or wait")])}<div class=note>You choose the days and the words.</div></div>''',
 """.vis{gap:26px;align-items:center}
.L{flex:1.3;min-width:0}.msg{background:#e9efe6;border-radius:28px;padding:30px 28px;box-shadow:0 26px 50px rgba(70,50,10,.16)}
.mh{display:flex;gap:14px;align-items:center;margin-bottom:18px}.mh b{font:700 21px 'Source Sans 3';display:block}.mh small{font:500 15px 'Source Sans 3';color:#6a7466}
.bub{background:#fff;border-radius:6px 22px 22px 22px;padding:30px 28px;font:400 28px/1.5 'Source Sans 3';color:#24302a}
.pay{margin-top:16px;background:#1d2c5e;color:#fff;border-radius:16px;padding:16px;display:flex;gap:12px;align-items:center;justify-content:center;font:700 20px 'Source Sans 3'}
.L{display:flex;flex-direction:column;gap:16px}.done{display:flex;gap:14px;align-items:center;background:#1f7a3e;color:#fff;border-radius:22px;padding:18px 22px}.done .ib{width:46px;height:46px;border-radius:50%;background:#fff;color:#1f7a3e}.done b{font:700 22px 'Source Sans 3';display:block}.done small{font:400 17px 'Source Sans 3';color:#d4eedb}
.R{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.d{background:#fffdf7;border-radius:20px;padding:40px 22px;box-shadow:0 14px 30px rgba(70,50,10,.1);display:flex;gap:16px;align-items:center}
.d b{font:800 34px 'Bitter';color:#c8372a;width:84px;flex:none}.d span{font:600 20px/1.3 'Source Sans 3'}
.note{font:italic 400 21px/1.4 'Gelasio';color:#5a5440;padding:6px 8px}""")

P["p21_kirana_s5"] = kslide(5, "YOUR SHOP, YOUR WAY", "Want a khata and order<br>app for <em>your kirana?</em>",
 "We build it around how your shop already works. Simple enough for anyone at the counter.",
 f'''<div class=w>{peep("PointingUp","Smile","ShortWavy","MoustacheThin",w=380,h=470)}<div class=lst>
 {"".join(f'<div class=li><span class=ib>{ic(i,26)}</span>{t}</div>' for i,t in [("users","Customer khata"),("doc","Monthly lists"),("bell","Payment reminders"),("box","Packing and delivery"),("chart","Daily sales view")])}
 <div class=ask>Tell us how you keep udhaar today. We will suggest the simplest setup.</div></div></div>''',
 """.vis{align-items:flex-end;margin-top:40px}.w{display:flex;align-items:flex-end;gap:26px;width:100%}
.lst{flex:1;display:flex;flex-direction:column;gap:12px;padding-bottom:10px}
.li{display:flex;gap:14px;align-items:center;background:#fffdf7;border-radius:18px;padding:24px 22px;font:700 24px 'Source Sans 3';box-shadow:0 10px 24px rgba(70,50,10,.1)}
.li .ib{width:46px;height:46px;border-radius:14px;background:#1d2c5e;color:#f3c64b}
.ask{background:#c8372a;color:#fff;border-radius:20px;padding:20px 22px;font:600 20px/1.4 'Source Sans 3';margin-top:4px}""",
 cta="Get your kirana app. DM us", ctacss="background:#c8372a;color:#fff")

# ───────── 22 INDIA · Dairy / milk delivery · SINGLE · Archivo Black + DM Sans · milk white / cobalt / grass
# New technique: month calendar heat-grid as the hero.
import random
random.seed(22)
cells = ""
pat = {3: "skip", 11: "skip", 12: "skip", 17: "2 L", 24: "2 L", 25: "2 L"}
for i in range(42):
    d = i - 6 + 1  # Nov 2026 starts Sunday -> use Mon-first grid; sample anyway
    if d < 1 or d > 30:
        cells += '<div class="c e"></div>'; continue
    v = pat.get(d, "1 L")
    cls = "sk" if v == "skip" else ("ex" if v == "2 L" else "ok")
    cells += f'<div class="c {cls}"><span>{d}</span><b>{"Skip" if v=="skip" else v}</b></div>'
P["p22_dairy"] = page("""
body{--f:'DM Sans';--h:'Archivo Black';background:#f6f3ea;color:#0f2a66}
h1{font-size:68px;font-weight:400;letter-spacing:-1px;line-height:1.2} h1 span{color:#1f5bd8}
.sub{color:#4b5a7c;font-size:25px}
.vis{flex-direction:column;gap:18px}
.cal{flex:1;background:#fff;border-radius:28px;padding:26px 28px;box-shadow:0 30px 60px rgba(15,42,102,.12);display:flex;flex-direction:column;min-height:0}
.ch{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px}
.ch b{font:400 28px 'Archivo Black'}.ch small{font:500 17px 'DM Sans';color:#6b7894}
.lg2{display:flex;gap:16px;font:600 16px 'DM Sans';color:#4b5a7c}.lg2 i{display:inline-block;width:14px;height:14px;border-radius:4px;margin-right:6px;vertical-align:-2px}
.wd{display:grid;grid-template-columns:repeat(7,1fr);gap:8px;font:700 15px 'DM Sans';color:#8a94ab;text-align:center;margin-bottom:8px}
.g{display:grid;grid-template-columns:repeat(7,1fr);grid-template-rows:repeat(6,1fr);gap:8px;flex:1}
.c{border-radius:14px;padding:8px 10px;display:flex;flex-direction:column;justify-content:space-between}
.c span{font:600 15px 'DM Sans';opacity:.7}.c b{font:700 20px 'DM Sans'}
.ok{background:#e7eefc;color:#0f2a66}.ex{background:#1f5bd8;color:#fff}.sk{background:#fde8e4;color:#c23b22}.e{background:transparent}
.bot{display:flex;gap:16px}
.bill{flex:1.4;background:#0f2a66;color:#fff;border-radius:24px;padding:22px 24px;display:flex;align-items:center;gap:18px}
.bill .ib{width:58px;height:58px;border-radius:18px;background:#7ed957;color:#0f2a66}
.bill b{display:block;font:700 23px 'DM Sans'}.bill small{display:block;font:400 17px 'DM Sans';color:#b9c6e6;margin-top:2px}
.st{flex:1;background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px;box-shadow:0 14px 30px rgba(15,42,102,.08)}
.st b{font:400 34px 'Archivo Black';color:#1f5bd8}.st span{font:600 16px 'DM Sans';color:#4b5a7c}
""", "<h1>Month-end milk bill?<br><span>Ready in one tap.</span></h1><div class=sub>Every house, every day: litres, skips and extra milk, counted for you.</div>",
f'''<div class=cal><div class=ch><div><b>Flat 204 · November</b><br><small>Sample customer · morning delivery</small></div><div class=lg2><span><i style="background:#e7eefc"></i>1 L</span><span><i style="background:#1f5bd8"></i>Extra</span><span><i style="background:#fde8e4"></i>Skip</span></div></div>
<div class=wd>{"".join(f"<span>{d}</span>" for d in ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])}</div><div class=g>{cells}</div></div>
<div class=bot><div class=st><b>30 L</b><span>Total this month</span></div><div class=st><b>3</b><span>Days skipped</span></div>
<div class=bill><span class=ib>{ic("send",30)}</span><div><b>Send bill to every house</b><small>One message each, with the daily list.</small></div></div></div>''',
"#0f2a66", "Want this for your dairy? DM us", "background:#1f5bd8;color:#fff")

# ───────── 23 INDIA · Tiffin / dabba service · SINGLE · TeX Gyre Adventor + Inter · turmeric / deep green
# New technique: one-day vertical timeline with clock column + phone (1 of 5 posts with a phone).
tl = [("9:00 PM", "Skips close for tomorrow", "6 customers skipped lunch. Count updates on its own.", "x"),
      ("7:00 AM", "Kitchen gets the count", "48 full meals · 9 roti only · 5 no-onion", "doc"),
      ("11:00 AM", "Riders get their routes", "3 routes, 62 stops, in the right order", "map"),
      ("Month end", "Bills by meals eaten", "Skipped days are left out automatically.", "rupee")]
tlh = "".join(f'<div class=t><div class=tm>{a}</div><div class=dt><i>{ic(i,22,w=2.4)}</i></div><div class=tc><b>{b}</b><small>{c}</small></div></div>' for a, b, c, i in tl)
P["p23_tiffin"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#14352a;color:#fdf6e3}
.sun{position:absolute;right:-140px;top:-140px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,#f5b90a 0 55%,rgba(245,185,10,0) 56%);opacity:.95}
h1{font-size:64px;font-weight:700;letter-spacing:-1.5px;max-width:720px} h1 span{color:#f5b90a}
.sub{color:#b8d0c3;max-width:640px}
.vis{gap:26px;align-items:stretch}
.tl{flex:1;display:flex;flex-direction:column;justify-content:space-between;position:relative;min-width:0}
.tl:before{content:"";position:absolute;left:147px;top:26px;bottom:26px;width:3px;background:repeating-linear-gradient(#f5b90a 0 10px,transparent 10px 18px)}
.t{display:flex;align-items:center;gap:16px}
.tm{width:110px;flex:none;text-align:right;font:700 19px 'Inter';color:#f5b90a}
.dt{width:44px;height:44px;border-radius:50%;background:#f5b90a;color:#14352a;display:flex;align-items:center;justify-content:center;flex:none;position:relative;z-index:2}
.tc{flex:1;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);border-radius:20px;padding:26px 22px}
.tc b{display:block;font:700 25px/1.3 'Inter'}.tc small{display:block;font:400 19px/1.45 'Inter';color:#b8d0c3;margin-top:4px}
.ap{padding:6px 18px 18px;flex:1;display:flex;flex-direction:column;gap:12px;color:#14352a}
.ap h4{font:700 20px 'TeX Gyre Adventor'}.ap .day{font:500 14px Inter;color:#6a7a72;margin-top:-8px}
.meal{border-radius:16px;background:#fff6d8;padding:14px}
.meal b{font:700 16px Inter;display:block;margin-bottom:6px}.meal p{font:400 14px/1.45 Inter;color:#4c5a53}
.tg{display:flex;justify-content:space-between;align-items:center;padding:13px 14px;border-radius:14px;background:#eef4f0;font:600 15px Inter}
.sw{width:46px;height:26px;border-radius:13px;background:#14352a;position:relative;flex:none}.sw:after{content:"";position:absolute;right:3px;top:3px;width:20px;height:20px;border-radius:50%;background:#f5b90a}
.sw.off{background:#cfd8d3}.sw.off:after{left:3px;right:auto;background:#fff}
.ok{margin-top:auto;background:#14352a;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 15px Inter}
""", "<h1>Who eats tomorrow?<br><span>Know by 9 PM.</span></h1><div class=sub>A sample day in a tiffin service, when customers skip from their phone.</div>",
f'''<div class=tl>{tlh}</div>{phone('<div class=ap><h4>Tomorrow\'s tiffin</h4><div class=day>Sample · Tuesday lunch</div><div class=meal><b>Today\'s menu</b><p>Dal, mixed veg, 4 roti, rice, salad</p></div><div class=tg>Lunch<span class=sw></span></div><div class=tg>Dinner<span class="sw off"></span></div><div class=tg>Extra roti (2)<span class="sw off"></span></div><div class=tg>No onion, no garlic<span class=sw></span></div><div class=meal style="background:#eef4f0"><b>This month</b><p>Paid till 30 Nov · 2 skips so far</p></div><div class=ok>Save for tomorrow</div></div>', w=320, h=650)}''',
"#fdf6e3", "Get your tiffin app. DM us", "background:#f5b90a;color:#14352a", bg="<div class=sun></div>")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
