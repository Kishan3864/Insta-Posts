import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 127 CANADA · Wholesaler / distributor · SINGLE · Bitter + Source Sans 3 · carton kraft / cherry red / slate
# New technique: layered carbon-copy order pad (yellow over pink sheet, pen notes, scribbles) on a clipboard next to a B2B portal.
pad_lines = [("Store 14 · Tuesday", "h"), ("6 cs dish soap", ""), ("4 cs paper towel ??", "x"), ("3 cs paper towel", ""), ("2 cs coffee filters", ""), ("trash bags? same as last", ""), ("hand soap? ask Monday", ""), ("Called back twice!", "n")]
last = [("Dish soap · 12 x 750 ml", 6), ("Paper towel · 6-roll pack", 3), ("Coffee filters · 200 ct", 2), ("Trash bags · 40 ct", 4), ("Hand soap · refill 2 L", 2)]
P["p127_wholesale"] = page("""
body{--f:'Source Sans 3';--h:'Bitter';background:#e8dcc6;color:#2c3440}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:0;line-height:1.2} h1 span{color:#b3242f}
.sub{color:#5c6470}
.vis{flex-direction:column;gap:18px}
.rw{flex:1;display:flex;gap:20px;min-height:0}
.cb{width:330px;flex:none;background:#8a5a34;border-radius:22px;padding:58px 20px 20px;position:relative;display:flex;box-shadow:0 20px 40px rgba(60,40,20,.25)}
.cb:before{content:"";position:absolute;top:16px;left:50%;transform:translateX(-50%);width:130px;height:38px;border-radius:10px;background:linear-gradient(#d9dde2,#9aa2ab);box-shadow:0 3px 0 #6f7780}
.sh{flex:1;position:relative}
.sh .pk{position:absolute;inset:10px -6px -6px 10px;background:#f6c9cf;border-radius:4px}
.sh .yl{position:absolute;inset:0;background:#fff4b8;border-radius:4px;padding:18px 18px;display:flex;flex-direction:column;background-image:linear-gradient(#e9d98a 1.5px,transparent 1.5px);background-size:100% 52px;background-position:0 40px}
.yl small{font:700 13px 'Source Sans 3';letter-spacing:2.5px;color:#8a7a30;height:40px}
.yl p{font:italic 600 26px/52px 'Crimson Text';color:#23357a;white-space:nowrap}
.yl p.h{font-weight:700;color:#b3242f}.yl p.x{text-decoration:line-through;text-decoration-thickness:3px;color:#6a73a8}.yl p.n{color:#b3242f;font-size:23px}
.yl .no{margin-top:auto;font:700 15px 'Source Sans 3';color:#8a7a30;letter-spacing:1px}
.br{flex:1;min-width:0}
.po{flex:1;padding:18px 22px 20px;display:flex;flex-direction:column;gap:10px;background:#fff}
.po .hd{display:flex;justify-content:space-between;align-items:flex-start;gap:10px}
.po .hd b{font:800 25px/1.25 'Bitter'}.po .hd span{display:block;font:500 17px 'Source Sans 3';color:#6a7380;margin-top:2px}
.po .hd em{font-style:normal;font:700 13px 'Source Sans 3';letter-spacing:2px;color:#6a7380;background:#f1ece2;padding:6px 10px;border-radius:8px;white-space:nowrap}
.po small{font:700 13px 'Source Sans 3';letter-spacing:2.5px;color:#9aa1ab;margin-top:4px}
.ln{flex:1;display:flex;align-items:center;justify-content:space-between;gap:10px;border-top:1.5px solid #eee8dd}
.ln b{font:600 19px 'Source Sans 3'}
.st{display:flex;align-items:center;flex:none;border:1.5px solid #d9d2c4;border-radius:10px;overflow:hidden}
.st i{width:34px;height:34px;display:flex;align-items:center;justify-content:center;font:700 20px/1 'Source Sans 3';font-style:normal;color:#6a7380;background:#f7f3ec}
.st u{text-decoration:none;width:62px;text-align:center;font:700 18px 'Source Sans 3'}
.bt{display:flex;gap:10px}
.bt div{flex:1;border-radius:12px;padding:13px 14px;font:700 19px 'Source Sans 3';text-align:center}
.bt .r1{background:#b3242f;color:#fff}.bt .r2{background:#f1ece2;color:#2c3440}
.dl{font:600 17px 'Source Sans 3';color:#2c6b47;background:#e3f1e8;border-radius:10px;padding:10px 14px}
.cs{flex:none;display:flex;gap:16px}
.cs div{flex:1;background:#2c3440;color:#f4efe5;border-radius:20px;padding:16px 18px;display:flex;flex-direction:column;gap:4px}
.cs b{font:800 21px/1.3 'Bitter'}.cs span{font:500 17px/1.35 'Source Sans 3';color:#c4c9d1}
""", "<h1>Store orders still come<br>by phone and paper pad?<br><span>Let them reorder online<br>in two taps.</span></h1>",
f'''<div class=rw><div class=cb><div class=sh><div class=pk></div><div class=yl><small>ORDER PAD · COPY 1 OF 2</small>
{"".join(f'<p class="{k}">{t}</p>' for t,k in pad_lines)}<div class=no>Copy 2: lost in a drawer</div></div></div></div>
{browser(f"""<div class=po><div class=hd><div><b>Sample Grocer · Store 14</b><span>Your account · own price list</span></div><em>SAMPLE</em></div>
<small>YOUR LAST ORDER · CASES</small>{"".join(f'<div class=ln><b>{a}</b><div class=st><i>−</i><u>{q}</u><i>+</i></div></div>' for a,q in last)}
<div class=dl>Next truck to your postal code: Tuesday</div>
<div class=bt><div class=r1>Reorder all</div><div class=r2>Edit order</div></div></div>""", "orders.yourwholesale.ca", "flex:1;min-width:0")}</div>
<div class=cs>{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a,b in [("Order 24/7","No more missed calls"),("Their own prices","Set per store by you"),("Clean pick lists","For the warehouse team")])}</div>''',
"#2c3440", "Run a wholesale business? DM us", "background:#b3242f;color:#fff")

# ───────── 128 INDIA · Upholstery shop · SINGLE · Gelasio + Montserrat · velvet teal / mustard / oatmeal
# New technique: SVG <pattern> fabric fills — the same sofa drawing filled with the chosen fabric, plus a swatch catalogue.
def fabs(p):
    return f'''<defs>
<pattern id="{p}vt" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#1f6f6b"/><circle cx="2" cy="2" r="1" fill="#2b8a84"/></pattern>
<pattern id="{p}ln" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="#bdb7ab"/><rect width="5" height="1" fill="#a9a396"/><rect width="1" height="5" fill="#cbc6bb"/></pattern>
<pattern id="{p}ck" width="28" height="28" patternUnits="userSpaceOnUse"><rect width="28" height="28" fill="#e2a72a"/><rect width="10" height="28" fill="#c58714" opacity=".55"/><rect width="28" height="10" fill="#c58714" opacity=".55"/></pattern>
<pattern id="{p}jt" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#c79d6c"/><rect width="4" height="4" fill="#b3895a"/><rect x="4" y="4" width="4" height="4" fill="#b3895a"/></pattern>
<pattern id="{p}fl" width="22" height="22" patternUnits="userSpaceOnUse"><rect width="22" height="22" fill="#f1e4d4"/><circle cx="6" cy="6" r="3.4" fill="#c2556b"/><circle cx="17" cy="17" r="2.4" fill="#5d8f62"/></pattern>
<pattern id="{p}lt" width="40" height="40" patternUnits="userSpaceOnUse"><rect width="40" height="40" fill="#6b3b2c"/><rect width="40" height="2" y="19" fill="#7a4635"/></pattern></defs>'''
def sofa(p, f, w):
    u = f"url(#{p}{f})"; sh = 'fill="#000" opacity=".14"'
    return f'''<svg viewBox="0 0 400 214" width="{w}" style="display:block">{fabs(p)}
<rect x="40" y="18" width="320" height="104" rx="28" fill="{u}"/><rect x="40" y="18" width="320" height="104" rx="28" {sh}/>
{"".join(f'<rect x="{58+i*96}" y="32" width="92" height="84" rx="20" fill="{u}"/>' for i in range(3))}
<rect x="48" y="118" width="304" height="60" rx="14" fill="{u}"/><rect x="48" y="146" width="304" height="32" rx="12" {sh}/>
{"".join(f'<rect x="{58+i*96}" y="108" width="92" height="40" rx="14" fill="{u}"/><rect x="{58+i*96}" y="138" width="92" height="10" rx="5" {sh}/>' for i in range(3))}
<rect x="8" y="72" width="62" height="110" rx="26" fill="{u}"/><rect x="330" y="72" width="62" height="110" rx="26" fill="{u}"/>
<rect x="8" y="150" width="62" height="32" rx="14" {sh}/><rect x="330" y="150" width="62" height="32" rx="14" {sh}/>
<rect x="34" y="182" width="16" height="26" rx="4" fill="#3b2a20"/><rect x="350" y="182" width="16" height="26" rx="4" fill="#3b2a20"/></svg>'''
sw = [("vt", "F-104", "Velvet teal", "42 m", 1), ("ln", "F-211", "Linen grey", "30 m", 0), ("ck", "F-318", "Mustard check", "18 m", 0),
      ("jt", "F-402", "Jute weave", "25 m", 0), ("fl", "F-509", "Floral cotton", "12 m", 0), ("lt", "F-610", "Faux leather", "36 m", 0)]
steps = [("Tue", "Pickup"), ("Wed", "Old fabric off"), ("Thu", "Foam check"), ("Fri", "Stitch + fit"), ("Sat", "Delivery")]
P["p128_upholstery"] = page("""
body{--f:'Montserrat';--h:'Gelasio';background:#efe6d6;color:#1d3a39}
h1{font-family:'Gelasio';font-size:60px;font-weight:700;letter-spacing:-.4px;line-height:1.2} h1 span{color:#1f6f6b}
.vis{flex-direction:column;gap:18px}
.rw{flex:1;display:flex;gap:18px;min-height:0}
.hero{flex:1;background:linear-gradient(#f8f2e7 0 74%,#d9c9ad 74%);border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:18px;padding:22px;position:relative;overflow:hidden}
.hero .tg{align-self:flex-start;background:#1d3a39;color:#f7efe1;border-radius:14px;padding:10px 14px;display:flex;flex-direction:column;gap:2px}
.hero .tg b{font:700 18px 'Montserrat'}.hero .tg span{font:500 15px 'Montserrat';color:#bcd0cc}
.hero .nt{display:flex;gap:10px;align-self:stretch}
.hero .nt div{flex:1;background:#fff;border-radius:14px;padding:10px 12px;font:600 15px/1.35 'Montserrat';color:#1d3a39;box-shadow:0 8px 18px rgba(29,58,57,.08)}
.cat{width:330px;flex:none;background:#fff;border-radius:28px;padding:18px;display:flex;flex-direction:column;gap:10px}
.cat small{font:700 13px 'Montserrat';letter-spacing:2.5px;color:#8f9a98}
.grd{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:10px}
.fs{border-radius:16px;border:2px solid #ece4d6;padding:8px;display:flex;flex-direction:column;gap:6px}
.fs.on{border-color:#1f6f6b;box-shadow:0 0 0 3px #bfe0dc}
.fs svg{display:block;width:100%;flex:1;border-radius:10px;min-height:0}
.fs b{font:700 14px/1.3 'Montserrat'}.fs span{font:500 13px 'Montserrat';color:#6e7a78}
.jb{flex:none;background:#1d3a39;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:12px;color:#f7efe1}
.jb .t{display:flex;justify-content:space-between;align-items:center}.jb .t b{font:700 22px 'Gelasio'}.jb .t span{font:600 15px 'Montserrat';color:#e2a72a;letter-spacing:1.5px}
.sp{display:flex;gap:8px}
.sp div{flex:1;border-radius:14px;padding:10px 10px;background:#2b4f4d;display:flex;flex-direction:column;gap:2px}
.sp div.dn{background:#e2a72a;color:#1d3a39}
.sp i{font:700 14px 'Montserrat';font-style:normal;opacity:.8}.sp b{font:700 16px/1.3 'Montserrat'}
""", "<h1>“How will my sofa look<br>in this fabric?”<br><span>Show it before you stitch.</span></h1><div class=sub>For upholstery shops: a fabric catalogue, sofa previews and pickup to delivery in one app.</div>",
f'''<div class=rw><div class=hero><div class=tg><b>Sample customer · 3+1+1 sofa set</b><span>Chosen: F-104 Velvet teal</span></div>{sofa("h", "vt", 500)}
<div class=nt><div>Customer picks on the phone, no shop visit</div><div>Metres kept aside for this job</div></div></div>
<div class=cat><small>FABRIC CATALOGUE · SAMPLE</small><div class=grd>{"".join(f'<div class="fs{" on" if o else ""}"><svg viewBox="0 0 100 60" preserveAspectRatio="none">{fabs("c"+k)}<rect width="100" height="60" fill="url(#c{k}{k})"/></svg><b>{n}</b><span>{c}<br>{s} in stock</span></div>' for k,c,n,s,o in sw)}</div></div></div>
<div class=jb><div class=t><b>Job J-087 · this week</b><span>SAMPLE</span></div><div class=sp>{"".join(f'<div class="{"dn" if i<2 else ""}"><i>{d}</i><b>{s}</b></div>' for i,(d,s) in enumerate(steps))}</div></div>''',
"#1d3a39", "Run an upholstery shop? DM us", "background:#1f6f6b;color:#fff")

# ───────── 129 USA · Used car dealer · SINGLE · Poppins + DM Sans · charcoal / candy red / silver
# New technique: parametric SVG car side profiles (sedan / SUV / pickup) as inventory photos, with live lot status.
SHAPES = {
 "sedan": ("M10 80 Q10 64 30 62 L72 57 Q92 36 120 34 L160 34 Q182 36 198 57 L222 63 Q232 67 232 80 L232 87 Q232 91 228 91 L14 91 Q10 91 10 87 Z",
           ["M84 57 Q100 42 120 42 L126 42 L126 57 Z", "M134 42 L158 42 Q176 44 188 57 L134 57 Z"]),
 "suv": ("M10 86 L10 62 Q12 54 24 52 L54 50 L72 28 Q76 24 84 24 L184 24 Q194 24 200 32 L216 52 Q230 54 232 66 L232 87 Q232 91 228 91 L14 91 Q10 91 10 86 Z",
         ["M80 50 L92 32 L132 32 L132 50 Z", "M140 32 L188 32 L202 50 L140 50 Z"]),
 "pickup": ("M10 87 L10 62 Q12 56 22 55 L72 52 L86 28 Q88 24 96 24 L142 24 Q148 24 150 30 L152 52 L230 52 L232 87 Q232 91 228 91 L14 91 Q10 91 10 87 Z",
            ["M92 48 L100 32 L144 32 L146 48 Z"])}
def car(kind, col, w=190):
    b, wins = SHAPES[kind]
    return f'''<svg viewBox="0 0 242 112" width="{w}" style="display:block"><ellipse cx="121" cy="104" rx="112" ry="6" fill="#000" opacity=".12"/>
<path d="{b}" fill="{col}"/>{"".join(f'<path d="{x}" fill="#cfe3f2"/>' for x in wins)}<rect x="12" y="70" width="220" height="4" fill="#fff" opacity=".25"/>
<rect x="214" y="66" width="14" height="8" rx="3" fill="#ffe3a0"/><rect x="12" y="68" width="10" height="8" rx="3" fill="#e05a4f"/>
{"".join(f'<circle cx="{x}" cy="91" r="17" fill="#22252b"/><circle cx="{x}" cy="91" r="8" fill="#c9cdd3"/>' for x in (62, 186))}</svg>'''
cars = [("sedan", "#c8202f", "2019 Sample Sedan", "48,200 mi · Automatic", "On the lot", "ok"),
        ("suv", "#3d5a80", "2021 Sample SUV", "31,900 mi · AWD", "On the lot", "ok"),
        ("pickup", "#8a8f98", "2018 Sample Pickup", "72,400 mi · 4x4", "On hold · test drive Sat", "hd"),
        ("sedan", "#f2f3f5", "2020 Sample Sedan", "39,700 mi · Automatic", "On the lot", "ok"),
        ("suv", "#2b2e35", "2017 Sample SUV", "88,100 mi · FWD", "Sold · hides tonight", "sd"),
        ("pickup", "#d9a441", "2022 Sample Pickup", "22,600 mi · 4x4", "Coming soon · photos Mon", "cs")]
P["p129_usedcar"] = page("""
body{--f:'DM Sans';--h:'Poppins';background:#1f2228;color:#f2f3f5}
body:before{content:"";position:absolute;left:0;right:0;top:0;height:520px;background:radial-gradient(ellipse at 80% 0,#3a2226,transparent 60%)}
h1{font-family:'Poppins';font-size:60px;font-weight:800;letter-spacing:-1.4px} h1 span{color:#ff4b57}
.sub{color:#aab0ba;font-family:'DM Sans'}
.vis{flex-direction:column}
.br{flex:1;min-height:0}
.inv{flex:1;background:#f4f5f7;padding:16px 18px 18px;display:flex;flex-direction:column;gap:12px;color:#1f2228;min-height:0}
.fl{display:flex;gap:8px;align-items:center}
.fl span{font:600 16px 'DM Sans';padding:8px 14px;border-radius:20px;background:#fff;border:1.5px solid #dfe2e7}
.fl span.on{background:#1f2228;color:#fff;border-color:#1f2228}
.fl em{margin-left:auto;font-style:normal;font:700 13px 'DM Sans';letter-spacing:2px;color:#8b919b}
.cg{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:12px;min-height:0}
.cc{background:#fff;border-radius:18px;padding:12px 14px;display:flex;align-items:center;gap:12px;box-shadow:0 6px 14px rgba(0,0,0,.05)}
.cc .im{width:196px;height:150px;flex:none;border-radius:12px;background:linear-gradient(#e9edf2 0 70%,#d7dce3 70%);display:flex;align-items:center;justify-content:center}
.cc .tx{flex:1;min-width:0;display:flex;flex-direction:column;gap:4px}
.cc b{font:700 21px/1.25 'Poppins'}.cc span{font:500 17px 'DM Sans';color:#6b717b}
.cc em{font-style:normal;align-self:flex-start;font:700 15px/1.3 'DM Sans';padding:5px 9px;border-radius:8px;margin-top:4px}
.ok em{background:#e0f3e8;color:#1d7046}.hd em{background:#fff0cf;color:#8a5a00}.sd em{background:#e7e9ed;color:#5b616b}.cs em{background:#e3ecff;color:#2a4fa8}
.cc.sd .im,.cc.sd b{opacity:.45}
.rq{display:flex;align-items:center;gap:12px;background:#1f2228;color:#fff;border-radius:14px;padding:12px 16px;font:500 17px 'DM Sans'}
.rq b{color:#ff4b57;font-weight:700}
""", "<h1>“Is that car still there?”<br><span>Show live stock on<br>your own website.</span></h1><div class=sub>Sold cars hide by themselves. Buyers book a test drive in one tap.</div>",
browser(f'''<div class=inv><div class=fl>{"".join(f'<span class="{"on" if i==0 else ""}">{t}</span>' for i,t in enumerate(["All","SUV","Sedan","Pickup","Under 50k mi"]))}<em>SAMPLE STOCK</em></div>
<div class=cg>{"".join(f'<div class="cc {k}"><div class=im>{car(s,c,184)}</div><div class=tx><b>{n}</b><span>{d}</span><em>{st}</em></div></div>' for s,c,n,d,st,k in cars)}</div>
<div class=rq>{ic("cal",22)}<span><b>New test drive request:</b> Saturday 10:00 · 2018 Sample Pickup</span></div></div>''', "yourcarlot.com/inventory", "flex:1"),
"#f2f3f5", "Sell used cars? DM us", "background:#ff4b57;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
