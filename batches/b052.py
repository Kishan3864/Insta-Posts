import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 276 INDIA · Hardware tool rental · SINGLE · Montserrat + Inter · safety orange / steel grey / chalk white
# New technique: tool "shadow board" — painted outlines on a dark board; a tool that is out shows only its dashed outline + a return tag.
TOOLS = {
 "drill": '<path d="M30 40 h110 a18 18 0 0 1 18 18 v14 a18 18 0 0 1 -18 18 h-40 l-10 60 h-40 l8 -60 h-28 a10 10 0 0 1 -10 -10 v-30 a10 10 0 0 1 10 -10z M158 56 h26 v20 h-26z M184 62 h22 v8 h-22z"/>',
 "ladder": '<path d="M70 10 h18 v170 h-18z M132 10 h18 v170 h-18z M88 30 h44 v12 h-44z M88 66 h44 v12 h-44z M88 102 h44 v12 h-44z M88 138 h44 v12 h-44z"/>',
 "toolbox": '<path d="M30 74 h160 a10 10 0 0 1 10 10 v80 a10 10 0 0 1 -10 10 h-160 a10 10 0 0 1 -10 -10 v-80 a10 10 0 0 1 10 -10z M80 36 h60 v14 h-60z M80 36 h12 v38 h-12z M128 36 h12 v38 h-12z M20 108 h180 v12 h-180z"/>',
 "trolley": '<path d="M20 56 h160 l-34 64 h-92z M96 126 a26 26 0 1 1 0.1 0z M172 62 l40 -18 v14 l-36 18z M58 120 h12 v46 h-12z"/>',
 "reel": '<path d="M110 20 a70 70 0 1 1 -0.1 0z M110 70 a20 20 0 1 0 0.1 0z M40 160 h140 v18 h-140z"/>',
 "hammer": '<path d="M20 50 h110 a24 24 0 0 1 24 24 v6 a24 24 0 0 1 -24 24 h-30 l-6 60 h-36 l4 -60 h-42 a10 10 0 0 1 -10 -10 v-34 a10 10 0 0 1 10 -10z M154 64 h50 v26 h-50z"/>',
}
slots = [("drill", "Drill machine", "in", ""), ("ladder", "Ladder 8 ft", "out", "Back 5 PM today"), ("toolbox", "Tool kit box", "in", ""),
         ("trolley", "Wheelbarrow", "out", "Back Tue 24 Nov"), ("reel", "Extension reel", "in", ""), ("hammer", "Hammer drill", "out", "Back 7 PM today")]
def tool(k, st):
    if st == "in":
        return f'<svg viewBox="0 0 220 190" class=tsv><g fill="#f26a1b" stroke="#fff" stroke-width="4" stroke-linejoin="round">{TOOLS[k]}</g></svg>'
    return f'<svg viewBox="0 0 220 190" class=tsv><g fill="none" stroke="#f3f2ee" stroke-width="5" stroke-dasharray="12 9" stroke-linejoin="round">{TOOLS[k]}</g></svg>'
P["p276_toolrent"] = page("""
body{--f:'Inter';--h:'Montserrat';background:#f3f2ee;color:#232a33}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#d9560c;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:64px;letter-spacing:-1.5px;line-height:1.2} h1 span{color:#f26a1b}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.bd{flex:1;min-width:0;background:#3a4048;border-radius:24px;padding:18px;display:flex;flex-direction:column;gap:12px;box-shadow:inset 0 0 0 8px #2d3239}
.bh{display:flex;justify-content:space-between;font:700 15px/1.4 'Inter';letter-spacing:2px;color:#c9ced6;padding:4px 8px 0}
.gr{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:12px;min-height:0}
.sl{background:#2d3239;border-radius:16px;padding:10px 14px 12px;display:flex;flex-direction:column;align-items:center;gap:6px;min-height:0}
.tsv{flex:1;min-height:0;width:100%;display:block}
.sl b{font:700 19px/1.3 'Montserrat';color:#fff}
.sl em{font:700 15px/1.3 'Inter';font-style:normal;padding:5px 12px;border-radius:8px;background:#4a8f5a;color:#fff}
.sl.out em{background:#ffd23f;color:#232a33}
.sd{width:340px;flex:none;display:flex;flex-direction:column;gap:12px}
.cd{background:#fff;border-radius:24px;padding:16px 20px;box-shadow:0 14px 30px rgba(35,42,51,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#7b8089}
.ol{flex:1;display:flex;flex-direction:column;gap:10px}
.or{flex:1;border-top:1px solid #ecebe6;display:flex;flex-direction:column;justify-content:center;gap:2px}
.or b{font:700 24px/1.3 'Montserrat'}.or span{font:500 18px/1.4 'Inter';color:#5b616b}.ok.rt{background:#fde7d8;color:#b4480b}
.ok{display:inline-block;font:700 14px 'Inter';color:#2f7a44;background:#e3f1e6;border-radius:6px;padding:3px 8px;margin-top:4px;align-self:flex-start}
.al{background:#f26a1b;color:#fff}.al small{display:block;font:700 14px/1.4 'Inter';letter-spacing:2px;color:#ffe2cf}.al b{display:block;font:800 26px/1.3 'Montserrat';margin:4px 0}.al span{font:500 17px/1.4 'Inter';color:#fff3ea}
""", "<div class=kk>HARDWARE TOOL RENTAL · ITEMS OUT AND BACK</div><h1>Who has the ladder?<br><span>The board knows.</span></h1>",
f'''<div class=vw><div class=bd><div class=bh><span>TOOL BOARD · SAMPLE SHOP</span><span>3 IN · 3 OUT</span></div><div class=gr>{"".join(f'<div class="sl {st}">{tool(k,st)}<b>{n}</b><em>{"In shop" if st=="in" else r}</em></div>' for k,n,st,r in slots)}</div></div>
<div class=sd><div class="cd ol"><small class=cap>TODAY'S RENTALS · SAMPLE</small>{"".join(f'<div class=or><b>{a}</b><span>{b}</span><i class=ok>Deposit noted</i></div>' for a,b in [("Ladder 8 ft","Customer C-104 · back 5 PM"),("Hammer drill","Customer C-117 · back 7 PM"),("Wheelbarrow","Customer C-098 · back Tue")])}<div class=or><b>Drill machine</b><span>Customer C-121 · back 11 AM</span><i class="ok rt">Returned</i></div></div>
<div class="cd al"><small>REMINDER SENT 4 PM</small><b>Ladder due at 5 PM</b><span>The customer gets a message one hour before.</span></div></div></div>''',
"#232a33", "Rent out tools? DM us", "background:#f26a1b;color:#fff")

# ───────── 277 USA · Closet installer · CAROUSEL 5 · Crimson Text + DM Sans · white oak / sage / ink
# New technique: closet elevations built from CSS sections (rods, shelves, drawers) drawn to the measured width, reused as layout options.
CB = """
body{--f:'DM Sans';--h:'Crimson Text';background:#f5f1ea;color:#1f2a2e}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#5f7d61;margin-top:22px;align-self:flex-start}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;letter-spacing:-.5px;line-height:1.2} h1 span{color:#5f7d61}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(31,42,46,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7c7a72}
.nb{display:flex;align-items:center;gap:14px;background:#1f2a2e;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.4 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#7d9a7e}.nb b{color:#e7d3b3}
.cl{display:flex;gap:6px;background:#c9a77c;border:6px solid #8a6b45;border-radius:8px;padding:6px}
.sec{flex:1;background:#f7efe2;border-radius:4px;position:relative;display:flex;flex-direction:column;justify-content:flex-start;gap:6px;padding:6px}
.rod{height:7px;border-radius:4px;background:#5d6b70;margin:10px 4px 0}
.hng{display:flex;gap:5px;padding:0 6px;flex:1;min-height:0}.hng i{flex:1;border-radius:3px 3px 8px 8px;background:#a9bfaa}
.hng i:nth-child(2n){background:#d4c3a6}.hng i:nth-child(3n){background:#8fa3b0}
.shf{height:7px;background:#8a6b45;border-radius:2px}
.drw{flex:none;height:30px;border:3px solid #8a6b45;border-radius:4px;background:#efe2cc;position:relative}.drw:after{content:"";position:absolute;left:50%;top:9px;width:26px;height:6px;margin-left:-13px;border-radius:3px;background:#5d6b70}
.box{flex:1;min-height:10px;max-height:46px;border-radius:3px;background:#d7c6aa}
"""
def cb(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f2a2e;color:#fff"):
    return page(CB + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f2a2e", cta, ctacss, tagline=f"{n} / 5")
def hang(n, f): return f'<div class=rod></div><div class=hng style="flex:{f};min-height:0">{"<i></i>"*n}</div>'
def shelves(n): return "".join('<div class=box></div><div class=shf></div>' for _ in range(n))
def drawers(n): return '<div style="flex:1"></div>' + "<div class=drw></div>" * n
LAYOUTS = {
 "A": [hang(5, 1) + '<div class=shf></div>' + hang(5, 1), shelves(5), hang(5, 1.4) + shelves(1)],
 "B": [hang(9, 3) + '<div style="flex:1"></div>', shelves(3) + drawers(3)],
 "C": [hang(5, 3) + '<div style="flex:1"></div>', shelves(6)],
}
def closet(k, h, style=""):
    return f'<div class=cl style="height:{h}px;{style}">{"".join(f"<div class=sec>{s}</div>" for s in LAYOUTS[k])}</div>'

P["p277_closet_s1"] = cb(1, "CLOSET INSTALLER · QUOTES AND DESIGN", "Quoting from a blurry photo?<br><span>Get the real sizes first.</span>",
f'''<div class=w1><div class="cd bf"><small class=cap>WHAT YOU GET TODAY</small><div class=blr><div class=bl1></div><div class=bl2></div><div class=bl3></div></div><div class=bub>“Is this big enough for a closet system?”</div></div>
<div class="cd af"><small class=cap>WHAT YOU NEED · SAMPLE</small><div class=el><div class=dimw><span>96 in wide</span></div><div class=rw1><div class=wall></div><div class=dimh><span>96 in high</span></div></div></div>
<div class=kv>{"".join(f"<div><small>{a}</small><b>{b}</b></div>" for a,b in [("DEPTH","24 in"),("DOOR","Sliding"),("PHOTOS","3 clear"),("OUTLET","Left wall")])}</div></div></div>''',
css=""".w1{flex:1;display:flex;gap:14px;min-height:0}.bf,.af{flex:1;min-width:0;padding:18px 20px;display:flex;flex-direction:column;gap:12px}
.blr{flex:1;border-radius:16px;background:#d8d2c6;position:relative;overflow:hidden}.blr div{position:absolute;filter:blur(14px);border-radius:20px}
.bl1{left:16%;top:12%;width:62%;height:72%;background:#9a8f7f}.bl2{left:28%;top:22%;width:20%;height:50%;background:#c9b89c}.bl3{left:56%;top:30%;width:16%;height:40%;background:#6f675c}
.bub{background:#f5f1ea;border-radius:16px 16px 16px 4px;padding:16px 18px;font:500 21px/1.45 'DM Sans'}
.el{flex:1;display:flex;flex-direction:column;gap:8px;min-height:0}
.dimw{border-left:3px solid #5f7d61;border-right:3px solid #5f7d61;height:30px;margin-right:84px;display:flex;align-items:center;justify-content:center;background:linear-gradient(#5f7d61,#5f7d61) center/100% 3px no-repeat}
.dimw span,.dimh span{font:700 17px 'DM Sans';background:#fff;padding:0 8px;color:#3f5c41}
.rw1{flex:1;display:flex;gap:12px;min-height:0}.wall{flex:1;border:5px solid #1f2a2e;border-radius:4px;background:repeating-linear-gradient(45deg,#f5f1ea 0 14px,#efe8dc 14px 16px)}
.dimh{width:72px;border-top:3px solid #5f7d61;border-bottom:3px solid #5f7d61;display:flex;align-items:center;justify-content:center;background:linear-gradient(#5f7d61,#5f7d61) center/3px 100% no-repeat}.dimh span{writing-mode:vertical-rl;padding:8px 0}
.kv{display:grid;grid-template-columns:1fr 1fr;gap:8px}.kv div{background:#eef3ee;border-radius:12px;padding:10px 14px}.kv small{display:block;font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#5f7d61}.kv b{font:700 24px/1.3 'DM Sans'}""")

fields = [("Wall width", "96 in"), ("Ceiling height", "96 in"), ("Depth", "24 in"), ("ZIP code", "12345")]
P["p277_closet_s2"] = cb(2, "STEP 1 · A MEASURING FORM ON YOUR WEBSITE", "Customers measure,<br><span>you quote with facts.</span>",
f'''<div class=w2>{browser(f"""<div class=fm><div class=fh><b>Plan your closet</b><span>Takes about 5 minutes · sample form</span></div>
<div class=g2>{"".join(f"<div class=fl><small>{a}</small><div class=in>{b}</div></div>" for a,b in fields)}</div>
<div class=fl><small>Door type</small><div class=chs>{"".join(f"<span class={chr(34)}{c}{chr(34)}>{t}</span>" for t,c in [("Sliding","on"),("Bifold",""),("Hinged",""),("No door","")])}</div></div>
<div class=fl><small>Anything on the walls?</small><div class=chs>{"".join(f"<span class={chr(34)}{c}{chr(34)}>{t}</span>" for t,c in [("Outlet","on"),("Light switch",""),("Vent","on"),("Nothing","")])}</div></div>
<div class=fl><small>Closet type</small><div class=chs>{"".join(f"<span class={chr(34)}{c}{chr(34)}>{t}</span>" for t,c in [("Reach-in","on"),("Walk-in",""),("Not sure","")])}</div></div>
<div class=fl><small>Photos of the space</small><div class=ph3><i></i><i></i><i></i><span>3 added</span></div></div>
<div class=btn>Send for a design</div></div>""", "yourclosets.com/plan", "flex:1")}</div>''',
css=""".w2{flex:1;display:flex;min-height:0}.fm{flex:1;padding:22px 28px 26px;display:flex;flex-direction:column;gap:16px}
.fh b{display:block;font:700 36px/1.3 'Crimson Text'}.fh span{font:500 17px 'DM Sans';color:#7c7a72}
.g2{display:grid;grid-template-columns:1fr 1fr;gap:12px}.fl{display:flex;flex-direction:column;gap:6px}.fl small{font:700 15px/1.4 'DM Sans';color:#55615f}
.in{border:2px solid #dcd6cb;border-radius:12px;padding:12px 16px;font:600 22px 'DM Sans'}
.chs{display:flex;gap:8px;flex-wrap:wrap}.chs span{font:700 18px 'DM Sans';padding:10px 16px;border-radius:12px;border:2px solid #dcd6cb}.chs span.on{border-color:#5f7d61;background:#eef3ee;color:#3f5c41}
.ph3{display:flex;gap:10px;align-items:center}.ph3 i{width:96px;height:72px;border-radius:10px;background:linear-gradient(135deg,#c9b89c,#8a7d6b)}.ph3 span{font:600 17px 'DM Sans';color:#5f7d61}
.btn{margin-top:auto;background:#5f7d61;color:#fff;border-radius:14px;padding:18px;text-align:center;font:700 22px 'DM Sans'}""")

P["p277_closet_s3"] = cb(3, "STEP 2 · LAYOUTS DRAWN TO THEIR WALL", "Three options.<br><span>One tap to approve.</span>",
f'''<div class=w3><div class=ops>{"".join(f'<div class="cd op{" on" if k=="B" else ""}"><div class=oh><b>Option {k}</b>{"<em>Approved</em>" if k=="B" else ""}</div>{closet(k, 470)}<span>{d}</span></div>' for k,d in [("A","Double hang + shelves"),("B","Long hang + drawers"),("C","Long hang + shoe shelves")])}</div>
<div class=nb><span class=ib>{ic("check",26)}</span><span>Customer picked Option B on Mon 23 Nov. <b>All three fit 96 inches.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ops{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.op{padding:16px;display:flex;flex-direction:column;gap:12px;border:3px solid transparent}.op.on{border-color:#5f7d61}
.oh{display:flex;justify-content:space-between;align-items:center}.oh b{font:700 30px/1.3 'Crimson Text'}.oh em{font:700 14px 'DM Sans';font-style:normal;background:#5f7d61;color:#fff;padding:5px 10px;border-radius:8px}
.op>span{font:600 18px/1.35 'DM Sans';color:#55615f}.op .cl{flex:1}""")

steps = [("Mon 23 Nov", "Design approved", "Option B, sample"), ("Wed 25 Nov", "Parts cut", "Shelves, rods, 3 drawers"), ("Sat 28 Nov · 9 AM", "Install day", "Crew of 2 · about 5 hours"), ("Sat 28 Nov · 2 PM", "Done photo sent", "Customer checks it in the app")]
P["p277_closet_s4"] = cb(4, "STEP 3 · INSTALL DAY WITH NO GUESSING", "They know who comes,<br><span>when, and for how long.</span>",
f'''<div class=w4><div class="cd tl">{"".join(f'<div class="st{" now" if i==2 else ""}"><i class=dt></i><div><small>{a}</small><b>{b}</b><span>{c}</span></div></div>' for i,(a,b,c) in enumerate(steps))}</div>
<div class="cd pv"><small class=cap>OPTION B · INSTALLED</small>{closet("B", 520)}</div></div>''',
css=""".w4{flex:1;display:flex;gap:14px;min-height:0}.tl{flex:1;min-width:0;padding:24px 26px;display:flex;flex-direction:column;position:relative}
.st{flex:1;display:flex;gap:18px;align-items:flex-start;position:relative}.st:not(:last-child):before{content:"";position:absolute;left:13px;top:30px;bottom:0;width:4px;background:#d6dfd6}
.dt{width:30px;height:30px;border-radius:50%;background:#7d9a7e;flex:none;margin-top:4px;border:5px solid #eef3ee}.st.now .dt{background:#c9a77c;border-color:#f3e7d4}
.st small{display:block;font:700 17px/1.4 'DM Sans';letter-spacing:1px;color:#5f7d61}.st b{display:block;font:700 38px/1.3 'Crimson Text'}.st span{font:500 20px/1.4 'DM Sans';color:#55615f}
.pv{width:360px;flex:none;padding:18px;display:flex;flex-direction:column;gap:12px}.pv .cl{flex:1}""")

P["p277_closet_s5"] = cb(5, "YOUR TURN", "Install closets?<br><span>Let's build your quote form.</span>",
f'''<div class=w5><div class="cd hp">{closet("A", 430, "width:360px")}{closet("C", 430, "width:270px")}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Measuring form","Real sizes and photos"),("grid","Layout options","Drawn to their wall"),("check","Online approval","One tap, saved"),("cal","Install booking","Day, crew and time")])}</div>
<div class=q>How do customers send you their closet sizes today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#5f7d61;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp{flex:1;display:flex;justify-content:center;align-items:center;gap:40px;padding:20px}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:20px 22px;box-shadow:0 10px 22px rgba(31,42,46,.07)}
.ti .ib{width:72px;height:72px;border-radius:20px;background:#eef3ee;color:#5f7d61}.ti b{display:block;font:700 30px/1.3 'Crimson Text'}.ti div span{font:500 19px/1.35 'DM Sans';color:#55615f}
.q{background:#1f2a2e;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'DM Sans'}""")

# ───────── 278 INDIA · E-waste collector · SINGLE · Anton + Source Sans 3 · circuit green / copper / charcoal · PHONE
# New technique: item picker with +/- counters inside the phone, and a weight slip with a drawn scale reading next to it.
items = [("Old laptops", 2), ("Mobile phones", 6), ("Cables and chargers", 1, "bag"), ("Keyboards and mice", 4), ("Printer", 1), ("Old TV", 1)]
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE E-WASTE PICKUP</small><b>What should we pick up?</b></div>
{"".join(f'<div class=itr><span>{t[0]}</span><div class=ctr><i>−</i><b>{t[1]}{" "+t[2] if len(t)>2 else ""}</b><i class=pl>+</i></div></div>' for t in items)}
<div class=sl2><small>PICKUP SLOT</small><div class=slc><span>Tue 10–12</span><span class=on>Tue 2–4</span><span>Wed 10–12</span></div></div>
<div class=adr>{ic("pin",20)}<span>Sample Office, 2nd floor</span></div><div class=adr>{ic("camera",20)}<span>3 photos of the items added</span></div>
<div class=bk>Book pickup</div></div>''', 400, 860)
P["p278_ewaste"] = page("""
body{--f:'Source Sans 3';--h:'Anton';background:#eaf1ec;color:#1d2321}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#1f8a5b;margin-top:22px}
h1{font-family:'Anton';font-weight:400;font-size:70px;letter-spacing:.5px;line-height:1.25;margin-top:34px} h1 span{color:#c8733a}
.vw{flex:1;display:flex;gap:22px;min-height:0;align-items:center}
.ap{flex:1;display:flex;flex-direction:column;gap:9px;padding:8px 18px 20px}
.ah small{display:block;font:700 12px/1.4 'Source Sans 3';letter-spacing:2px;color:#1f8a5b;margin-bottom:6px}.ah b{display:block;font:400 26px/1.5 'Anton';color:#1d2321}
.itr{display:flex;align-items:center;justify-content:space-between;gap:8px;border:2px solid #e3e9e5;border-radius:12px;padding:11px 10px;font:600 18px/1.25 'Source Sans 3'}
.itr>span{flex:1;min-width:0}
.ctr{display:flex;align-items:center;gap:6px;flex:none}.ctr i{width:28px;height:28px;border-radius:8px;background:#eef2ef;font:700 18px/28px 'Source Sans 3';font-style:normal;text-align:center}.ctr i.pl{background:#1f8a5b;color:#fff}
.ctr b{font:700 17px 'Source Sans 3';min-width:34px;text-align:center}
.sl2 small{display:block;font:700 12px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b746f;margin-bottom:5px}
.slc{display:flex;gap:5px}.slc span{flex:1;font:700 13px 'Source Sans 3';text-align:center;padding:8px 2px;border-radius:9px;border:2px solid #e3e9e5}.slc span.on{border-color:#1f8a5b;background:#e5f3eb;color:#16694a}
.adr{display:flex;align-items:center;gap:8px;font:600 15px 'Source Sans 3';color:#4a524e;background:#f4f6f4;border-radius:10px;padding:8px 10px}
.bk{margin-top:auto;background:#1f8a5b;color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 18px 'Source Sans 3'}
.rc2{flex:1;min-width:0;align-self:stretch;display:flex;flex-direction:column;gap:12px}
.ws{flex:1;background:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(29,35,33,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b746f}
.sc{display:flex;align-items:center;gap:16px;background:#1d2321;border-radius:16px;padding:14px 18px}
.lcd{flex:1;background:#b8e0c4;border-radius:10px;padding:6px 14px;font:400 46px/1.4 'Anton';color:#173a26;text-align:right;letter-spacing:2px}
.sc span{font:700 15px/1.3 'Source Sans 3';color:#c9d3cd;width:90px}
.wr{flex:1;display:flex;align-items:center;justify-content:space-between;border-bottom:2px dotted #d5ddd8;font:600 19px 'Source Sans 3'}.wr b{font:700 21px 'Source Sans 3'}
.wt{display:flex;justify-content:space-between;font:700 20px 'Source Sans 3';color:#1f8a5b;padding-top:4px}
.dn{background:#c8733a;color:#fff;border-radius:24px;padding:16px 22px}.dn small{display:block;font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#ffe3cf;margin-bottom:6px}.dn b{display:block;font:400 30px/1.5 'Anton';letter-spacing:.5px;margin-bottom:4px}.dn span{font:500 17px/1.4 'Source Sans 3'}
""", "<div class=kk>E-WASTE COLLECTOR · PICKUP BOOKINGS</div><h1>“Come and take old stuff”?<br><span>Let them book by item.</span></h1>",
f'''<div class=vw>{ph}<div class=rc2><div class=ws><small class=cap>WEIGHT SLIP · PICKUP P-276 · SAMPLE</small><div class=sc><span>Weighed at pickup</span><div class=lcd>25.6 kg</div></div>
{"".join(f'<div class=wr><span>{a}</span><b>{b}</b></div>' for a,b in [("Laptops × 2","4.6 kg"),("Phones × 6","1.2 kg"),("Cables, 1 bag","3.1 kg"),("Keyboards and mice × 4","3.5 kg"),("Printer × 1","6.0 kg"),("Old TV × 1","7.2 kg")])}
<div class=wt><span>6 item types</span><span>25.6 kg</span></div></div>
<div class=dn><small>AFTER PICKUP</small><b>Slip sent by message</b><span>Same items as the booking, so nothing is missed.</span></div></div></div>''',
"#1d2321", "Collect e-waste? DM us", "background:#1f8a5b;color:#fff")

# ───────── 279 INDIA · Wall putty and POP contractor · SINGLE · Cardo + Inter · putty grey / ultramarine / ivory
# New technique: wall cross-section strata (brick, POP, putty 1, putty 2, primer) as a legend, then room rows with one cell per layer.
LAY = [("POP", "#e9e4d8", "#8c8578"), ("Putty 1", "#f1eee7", "#a39d90"), ("Putty 2", "#f7f5f0", "#b8b2a6"), ("Primer", "#dfe6fb", "#2b45a8")]
rooms = [("Hall", 420, 4), ("Bedroom 1", 310, 3), ("Bedroom 2", 280, 2), ("Kitchen", 160, 1), ("Passage", 90, 0)]
days = [("Mon", "Bedroom 1 primer"), ("Tue", "Bedroom 2 putty 2"), ("Wed", "Kitchen putty 1"), ("Thu", "Passage POP"), ("Fri", "Kitchen putty 2"), ("Sat", "Check and handover")]
strata = "".join(f'<div class=sa style="background:{c};border-color:{e}"><b>{n}</b></div>' for n, c, e in LAY)
P["p279_putty"] = page("""
body{--f:'Inter';--h:'Cardo';background:#faf7f0;color:#1f2547}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#2b45a8;margin-top:22px}
h1{font-family:'Cardo';font-weight:700;font-size:68px;line-height:1.25} h1 span{color:#2b45a8}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.xs{display:flex;gap:16px;background:#fff;border-radius:24px;padding:16px 20px;align-items:stretch;box-shadow:0 14px 30px rgba(31,37,71,.07)}
.xl{width:250px;flex:none;display:flex;flex-direction:column;justify-content:center;gap:4px}.xl small{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#777264}.xl b{font:700 30px/1.3 Cardo}
.br{width:110px;flex:none;border-radius:8px;background:repeating-linear-gradient(0deg,#b4553a 0 26px,#e8d9c9 26px 30px);border:3px solid #8a3f2a}
.sx{flex:1;display:flex;gap:0}.sa{flex:1;border:3px solid;border-left-width:0;display:flex;align-items:flex-end;justify-content:center;padding:10px 4px;min-height:120px}.sa:first-child{border-left-width:3px}
.sa b{font:700 18px/1.3 'Inter'}
.tb{flex:1;background:#fff;border-radius:24px;padding:14px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(31,37,71,.07)}
.th,.tr{display:grid;grid-template-columns:200px 120px repeat(4,1fr);gap:10px;align-items:center}
.th{font:700 14px/1.4 'Inter';letter-spacing:1.5px;color:#777264;padding-bottom:8px;border-bottom:2px solid #1f2547}
.tr{flex:1;border-bottom:1px solid #eeeae0}.tr:last-child{border:0}
.tr b{font:700 26px/1.3 Cardo}.tr em{font:600 19px 'Inter';font-style:normal;color:#4a4f6a}
.cl{height:44px;border-radius:10px;border:3px dashed #d4cfc2;display:flex;align-items:center;justify-content:center;font:700 15px 'Inter';color:#a39d90}
.cl.d{border-style:solid;color:#1f2547}.cl.n{border:3px solid #2b45a8;background:#2b45a8;color:#fff}
.dy{display:grid;grid-template-columns:repeat(6,1fr);gap:8px}
.dd{background:#1f2547;color:#fff;border-radius:16px;padding:12px 12px}.dd small{display:block;font:700 14px/1.4 'Inter';letter-spacing:2px;color:#aab8f2}.dd span{font:600 17px/1.35 'Inter'}
.dd.t{background:#2b45a8}
""", "<div class=kk>WALL PUTTY AND POP CONTRACTOR · SITE SHEET</div><h1>Which room got 2 coats?<br><span>Every wall on one sheet.</span></h1>",
f'''<div class=vw><div class=xs><div class=xl><small>WALL LAYERS</small><b>Brick to primer</b></div><div class=br></div><div class=sx>{strata}</div></div>
<div class=tb><div class=th><span>ROOM · SAMPLE</span><span>AREA</span>{"".join(f"<span>{n.upper()}</span>" for n,_,_ in LAY)}</div>
{"".join(f'<div class=tr><b>{r}</b><em>{a} sq ft</em>{"".join(f"<div class={chr(34)}cl {chr(100) if i<k else (chr(110) if i==k else chr(32))}{chr(34)} style={chr(34)}{(f'background:{LAY[i][1]};border-color:{LAY[i][2]}') if i<k else ''}{chr(34)}>{'Done' if i<k else ('Next' if i==k else '—')}</div>" for i in range(4))}</div>' for r,a,k in rooms)}</div>
<div class=dy>{"".join(f'<div class="dd{" t" if i==0 else ""}"><small>{d}</small><span>{t}</span></div>' for i,(d,t) in enumerate(days))}</div></div>''',
"#1f2547", "POP or putty work? DM us", "background:#2b45a8;color:#fff")

# ───────── 280 INDIA · Aluminium sliding window maker · SINGLE · TeX Gyre Adventor + Inter · anodized bronze / sky glass / graphite
# New technique: building elevation where each flat's windows are coloured by job stage, next to one flat's window list.
ST = {"m": ("#c7cbd1", "Measured"), "c": ("#f0b53c", "Cutting"), "g": ("#7cc3ea", "Glass fitted"), "d": ("#3ea66b", "Dispatched")}
flats = [("401", "mmm"), ("402", "mmm"), ("301", "ccc"), ("302", "ggc"), ("201", "ggg"), ("202", "ggg"), ("101", "ddd"), ("102", "ddg")]
def flat(n, s, sel=False): return f'<div class="fl{" sel" if sel else ""}"><b>{n}</b><div class=wn>{"".join(f"<i style={chr(34)}background:{ST[c][0]}{chr(34)}></i>" for c in s)}</div></div>'
wl = [("W1", "Bedroom", "5 × 4 ft", "2-track · clear glass", "g"), ("W2", "Hall", "6 × 4 ft", "3-track · tinted", "g"), ("W3", "Kitchen", "3 × 3 ft", "2-track · frosted", "c")]
P["p280_alwindow"] = page("""
body{--f:'Inter';--h:'TeX Gyre Adventor';background:#f1efec;color:#23272c}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#8a5a2b;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:62px;letter-spacing:-1.5px;line-height:1.22} h1 span{color:#8a5a2b}
.vw{flex:1;display:flex;gap:14px;min-height:0}
.bl{width:420px;flex:none;background:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(35,39,44,.08)}
.cap{font:700 14px/1.4 'Inter';letter-spacing:2px;color:#77736d}
.bg{flex:1;background:#e6dfd4;border:6px solid #23272c;border-radius:10px 10px 0 0;padding:14px;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(4,1fr);gap:12px;position:relative}
.fl{background:#f8f5f0;border-radius:6px;padding:8px 10px;display:flex;flex-direction:column;gap:6px;border:2px solid #cfc6b8}
.fl b{font:700 18px/1.3 'TeX Gyre Adventor'}
.wn{flex:1;display:flex;gap:6px}.wn i{flex:1;border:4px solid #8a5a2b;border-radius:3px;position:relative}.wn i:after{content:"";position:absolute;top:0;bottom:0;left:50%;width:3px;background:#8a5a2b}
.fl.sel{border:3px solid #23272c;box-shadow:0 0 0 4px #f0b53c}
.gd{height:16px;background:#23272c;border-radius:0 0 6px 6px;margin-top:-10px}
.lgd3{display:grid;grid-template-columns:1fr 1fr;gap:6px 10px}.lgd3 span{display:flex;align-items:center;gap:8px;font:600 15px 'Inter'}.lgd3 i{width:16px;height:16px;border-radius:4px}
.rc{flex:1;min-width:0;display:flex;flex-direction:column;gap:12px}
.wl{flex:1;background:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(35,39,44,.08)}
.wh{display:flex;justify-content:space-between;align-items:baseline}.wh b{font:700 32px/1.3 'TeX Gyre Adventor'}
.wr{flex:1;display:flex;gap:14px;align-items:center;border:2px solid #ece7df;border-radius:16px;padding:10px 14px}
.wd{width:130px;height:104px;flex:none;border:5px solid #8a5a2b;border-radius:4px;background:#bfe0f2;position:relative}.wd:after{content:"";position:absolute;top:0;bottom:0;left:48%;width:4px;background:#8a5a2b}
.wd.f{background:repeating-linear-gradient(45deg,#e4eef4 0 6px,#d3e1ea 6px 9px)}.wd.t{background:#6f8796}
.wi{flex:1;min-width:0}.wi b{display:block;font:700 26px/1.3 'TeX Gyre Adventor'}.wi span{font:500 18px/1.4 'Inter';color:#5c5953}
.wr em{font:700 14px 'Inter';font-style:normal;padding:5px 10px;border-radius:8px;flex:none}
.dc{background:#23272c;color:#fff;border-radius:24px;padding:16px 20px}.dc small{display:block;font:700 14px/1.4 'Inter';letter-spacing:2px;color:#f0c98a}.dc b{display:block;font:700 26px/1.3 'TeX Gyre Adventor';margin:2px 0}.dc span{font:500 17px/1.4 'Inter';color:#cfd2d6}
""", "<div class=kk>ALUMINIUM SLIDING WINDOWS · SITE ORDERS</div><h1>Which flat is ready?<br><span>See the whole building.</span></h1>",
f'''<div class=vw><div class=bl><small class=cap>SAMPLE TOWER · 8 FLATS · 24 WINDOWS</small><div class=bg>{"".join(flat(n,s,n=="302") for n,s in flats)}</div><div class=gd></div>
<div class=lgd3>{"".join(f'<span><i style="background:{c}"></i>{l}</span>' for c,l in ST.values())}</div></div>
<div class=rc><div class=wl><div class=wh><b>Flat 302</b><small class=cap>3 WINDOWS · SAMPLE</small></div>
{"".join(f'<div class=wr><div class="wd {dict(g="",c="f").get(s,"")}{" t" if "tinted" in d else ""}"></div><div class=wi><b>{w} · {r}</b><span>{sz} · {d}</span></div><em style="background:{ST[s][0]};color:{"#23272c"}">{ST[s][1]}</em></div>' for w,r,sz,d,s in wl)}</div>
<div class=dc><small>DISPATCH · FLAT 302</small><b>Thu 26 Nov, after W3 glass</b><span>The site gets a message with the window list.</span></div></div></div>''',
"#23272c", "Make aluminium windows? DM us", "background:#8a5a2b;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
