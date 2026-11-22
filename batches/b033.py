import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 181 INDIA · 20-litre water can supplier · SINGLE · Archivo Black + Fira Sans · pale sky / marine navy / sunflower
# New technique: per-customer "can strip" ledger of drawn 20 L jars (full = with customer, outline = returned, yellow = not back 7+ days).
def jar(k, s=1.0):
    w, h = int(46*s), int(64*s)
    body = {"o": ("#1f6fd1", "#0b2f5b", "#8fc2ff"), "b": ("#ffffff", "#9bb3cf", "#ffffff"), "l": ("#ffc62b", "#7a5600", "#ffe28a")}[k]
    f, st, hl = body
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 46 64" style="flex:none;display:block">'
            f'<rect x="17" y="1" width="12" height="7" rx="2" fill="{st}"/><path d="M15 8h16l3 7H12z" fill="{f}" stroke="{st}" stroke-width="2" stroke-linejoin="round"/>'
            f'<rect x="4" y="15" width="38" height="46" rx="9" fill="{f}" stroke="{st}" stroke-width="2.4"/>'
            f'<rect x="4" y="29" width="38" height="3" fill="{st}" opacity=".35"/><rect x="4" y="44" width="38" height="3" fill="{st}" opacity=".35"/>'
            f'<rect x="10" y="19" width="5" height="18" rx="2.5" fill="{hl}" opacity=".7"/></svg>')
cust = [("Flat A-102", "2 cans daily", "oobbb", ""),
        ("Shop 3, Main Road", "4 cans daily", "ooooll", "Remind"),
        ("Office, 2nd floor", "5 cans, Mon-Sat", "oooobb", ""),
        ("Flat C-404", "1 can, alternate days", "llo", "Remind"),
        ("Sample café", "3 cans daily", "ooobbb", "")]
def crow(n, plan, s, act):
    out = s.count("o") + s.count("l"); late = s.count("l")
    chip = f'<em class=rm>{ic("bell",18,w=2.4)} {act}</em>' if act else '<em class=okc>All fine</em>'
    return (f'<div class=cr><div class=cn><b>{n}</b><span>{plan}</span></div><div class=js>{"".join(jar(k,1.15) for k in s)}</div>'
            f'<div class=cc><b>{out} out</b>{f"<span>{late} late</span>" if late else "<span class=z>0 late</span>"}</div>{chip}</div>')
P["p181_watercan"] = page("""
body{--f:'Fira Sans';--h:'Archivo Black';background:#dff1fb;color:#0b2f5b}
h1{font-family:'Archivo Black';font-size:60px;font-weight:400;letter-spacing:-1px;line-height:1.22} h1 span{color:#1f6fd1}
.sub{color:#33557f;font-size:23px}
.vis{flex-direction:column;gap:16px}
.stt{display:flex;gap:14px}.stt div{flex:1;background:#fff;border-radius:22px;padding:16px 20px;display:flex;align-items:center;gap:14px;box-shadow:0 12px 26px rgba(11,47,91,.08)}
.stt b{display:block;font:400 40px/1.25 'Archivo Black'}.stt span{font:600 17px/1.3 'Fira Sans';color:#5a7699}
.stt .yl{background:#ffc62b}.stt .yl span{color:#5c4300}
.ldg{flex:1;background:#fff;border-radius:28px;padding:20px 24px;display:flex;flex-direction:column;gap:6px;box-shadow:0 18px 36px rgba(11,47,91,.10)}
.lh{display:flex;justify-content:space-between;align-items:center;padding-bottom:6px}
.lh small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#5a7699}
.key{display:flex;gap:16px;font:600 16px 'Fira Sans';color:#33557f}.key span{display:flex;align-items:center;gap:6px}
.cr{flex:1;display:flex;align-items:center;gap:16px;border-top:2px solid #e6f0fa}
.cn{width:236px;flex:none}.cn b{display:block;font:700 23px/1.3 'Fira Sans'}.cn span{font:500 17px 'Fira Sans';color:#5a7699}
.js{flex:1;display:flex;gap:7px;align-items:center}
.cc{width:92px;flex:none;text-align:right}.cc b{display:block;font:700 22px/1.3 'Fira Sans'}.cc span{font:700 16px 'Fira Sans';color:#b07c00}.cc .z{color:#8aa3bf}
.rm,.okc{width:128px;flex:none;font-style:normal;font:700 17px 'Fira Sans';border-radius:14px;padding:10px 0;display:flex;align-items:center;justify-content:center;gap:6px}
.rm{background:#0b2f5b;color:#ffc62b}.okc{background:#e6f0fa;color:#33557f}
.dn{background:#0b2f5b;color:#fff;border-radius:20px;padding:16px 22px;font:500 20px/1.4 'Fira Sans';display:flex;gap:14px;align-items:center}.dn b{color:#ffc62b}.dn span{text-wrap:balance}
""", "<h1>20-litre cans go out.<br><span>Do they come back?</span></h1><div class=sub>See how many empty cans each customer still has, every day.</div>",
f'''<div class=stt><div>{jar("o",.8)}<p><b>46</b><span>cans with customers</span></p></div><div>{jar("b",.8)}<p><b>18</b><span>empties back today</span></p></div><div class=yl>{jar("l",.8)}<p><b>6</b><span>not back for 7+ days</span></p></div></div>
<div class=ldg><div class=lh><small>CAN LEDGER · SAMPLE CUSTOMERS</small><div class=key><span>{jar("o",.4)}With customer</span><span>{jar("b",.4)}Back</span><span>{jar("l",.4)}7+ days</span></div></div>
{"".join(crow(*c) for c in cust)}</div>
<div class=dn>{ic("truck",30)}<span>The driver taps <b>out</b> and <b>back</b> at every drop. Each customer sees their own can count on one link.</span></div>''',
"#0b2f5b", "Supply water cans? DM us", "background:#1f6fd1;color:#fff")


# ───────── 182 INDIA · Xerox and print shop · CAROUSEL 5 · TeX Gyre Adventor + Fira Sans · paper white / process cyan / magenta
# New techniques: counter TV mockup with token columns, printer SVG feeding a page, chat-bubble file pile with magenta question tags.
XC = """
body{--f:'Fira Sans';--h:'TeX Gyre Adventor';background:#f6f5ef;color:#17181c}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:60px;letter-spacing:-1px;line-height:1.22} h1 span{color:#e0218a}
.kk{font:700 16px 'Fira Sans';letter-spacing:3px;color:#0092cc;margin-top:22px;display:flex;gap:10px;align-items:center}
.kk i{width:14px;height:14px;border-radius:50%;display:inline-block}
.cmyk{display:flex;gap:6px}.cmyk i:nth-child(1){background:#00a3e0}.cmyk i:nth-child(2){background:#e0218a}.cmyk i:nth-child(3){background:#ffd400}.cmyk i:nth-child(4){background:#17181c}
.cd{background:#fff;border-radius:26px;box-shadow:0 16px 34px rgba(23,24,28,.08)}
"""
def xc(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#17181c;color:#fff"):
    return page(XC + css, f"<div class=kk><span class=cmyk><i></i><i></i><i></i><i></i></span>{kick}</div><h1>{head}</h1>", vis, "#17181c", cta, ctacss, tagline=f"{n} / 5")

files = [("notes_unit3.pdf", "38 pages", "How many copies?", 0), ("resume_new.pdf", "2 pages", "Colour or B&W?", 1), ("project_final(2).pdf", "64 pages", "Spiral or staple?", 0),
         ("IMG_2041.jpg", "1 photo", "Whose file is this?", 1), ("form_scan.pdf", "4 pages", "Ready by when?", 0)]
P["p182_xerox_s1"] = xc(1, "PRINT AND PHOTOCOPY SHOPS", "Print files on chat<br>all day long?<br><span>Which one? How many?</span>",
f'''<div class=chs>{"".join(f'<div class="bw {"r" if r else ""}"><div class=bb><span class=fi>{ic("file",36)}</span><div><b>{a}</b><span>{p} · sample</span></div><time>{t}</time></div><em>{q}</em></div>' for (a,p,q,r),t in zip(files,["9:12 AM","9:40 AM","10:05 AM","10:31 AM","11:02 AM"]))}</div>''',
css=""".chs{flex:1;display:flex;flex-direction:column;gap:12px}
.bw{flex:1;display:flex;align-items:center;gap:16px}.bw.r{flex-direction:row-reverse}
.bb{width:560px;height:100%;background:#fff;border-radius:24px;display:flex;align-items:center;gap:16px;padding:0 22px;box-shadow:0 10px 24px rgba(23,24,28,.07)}
.bw.r .bb{background:#e3f5fc}
.fi{width:76px;height:76px;border-radius:18px;background:#17181c;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.bb div{flex:1}.bb b{display:block;font:700 30px/1.3 'Fira Sans'}.bb span{font:500 21px 'Fira Sans';color:#6c6d75}.bb time{align-self:flex-end;margin-bottom:18px;font:600 17px 'Fira Sans';color:#8b8c93}
.bw em{flex:1;font-style:normal;font:700 28px/1.3 'TeX Gyre Adventor';color:#e0218a;text-align:center;border:3px dashed #e0218a;border-radius:20px;padding:16px 10px;background:#fdeaf4}""")

def tog(lbl, opts, on):
    return f'<div class=tg><small>{lbl}</small><div>{"".join(f"<i class={chr(34)}{chr(111)+chr(110) if o==on else chr(120)}{chr(34)}>{o}</i>" for o in opts)}</div></div>'
P["p182_xerox_s2"] = xc(2, "PART 1 · ORDER LINK", "One link for the file<br><span>and every detail.</span>",
browser(f'''<div class=fo><b class=t>Send a print job</b>
<div class=up><span class=fi>{ic("file",30)}</span><div><b>project_report.pdf</b><span>24 pages · uploaded</span></div><em>{ic("check",22,w=3)}</em></div>
{tog("PRINT", ["B&W", "Colour"], "B&W")}{tog("SIDES", ["One side", "Both sides"], "Both sides")}
<div class=r2><div class=tg><small>COPIES</small><div class=stp><i class=x>−</i><b>2</b><i class=x>+</i></div></div>{tog("BINDING", ["None", "Staple", "Spiral"], "Spiral")}</div>
<div class=r3><div class=fl2><small>PAGES</small><b>All (1-24)</b></div><div class=fl2><small>NOTE TO SHOP</small><b>Clear sheet on the front, please</b></div></div>
{tog("PICKUP", ["Today, 5 PM", "Tomorrow"], "Today, 5 PM")}
<div class=bt>Send to shop · get token</div></div>''', url="yourprintshop.in/print · sample", style="flex:1"),
css=""".vis{display:flex}.fo{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:12px}.fo .t{font:700 34px 'TeX Gyre Adventor'}
.up{display:flex;align-items:center;gap:16px;background:#e3f5fc;border-radius:18px;padding:14px 18px}.up div{flex:1}.up b{display:block;font:700 24px 'Fira Sans'}.up span{font:500 18px 'Fira Sans';color:#4f6670}
.fi{width:56px;height:56px;border-radius:14px;background:#17181c;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}
.up em{width:42px;height:42px;border-radius:50%;background:#00a3e0;color:#fff;display:flex;align-items:center;justify-content:center}
.tg{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px}.tg small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#8b8c93}
.tg>div{display:flex;gap:8px}.tg i{font-style:normal;flex:1;text-align:center;font:600 23px 'Fira Sans';padding:15px 0;border-radius:14px;border:2px solid #e2e1da;background:#fff}
.tg i.on{background:#17181c;color:#fff;border-color:#17181c}
.r2{flex:1;display:flex;gap:14px}.r3{flex:1;display:flex;gap:14px}.fl2{background:#f6f5ef;border-radius:16px;padding:12px 18px;display:flex;flex-direction:column;justify-content:center;gap:4px}.fl2:first-child{width:200px;flex:none}.fl2:last-child{flex:1}.fl2 small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#8b8c93}.fl2 b{font:600 23px 'Fira Sans'}.r2 .tg:first-child{flex:none;width:200px}
.stp{align-items:center}.stp b{font:700 28px 'Fira Sans';width:50px;text-align:center}.stp i{flex:none;width:56px}
.bt{background:#e0218a;color:#fff;border-radius:16px;padding:17px;text-align:center;font:700 22px 'Fira Sans'}""")

def tok(t, k, d=""): return f'<div class="tk {k}"><b>{t}</b>{f"<small>{d}</small>" if d else ""}</div>'
P["p182_xerox_s3"] = xc(3, "PART 2 · COUNTER SCREEN", "Every token on one screen.<br><span>No crowd at the counter.</span>",
f'''<div class=tvw><div class=tv><div class=sc>
<div class=co><small>PRINTING NOW</small>{tok("T-41","pn")}<span class=ds>24 pages · both sides · spiral</span></div>
<div class=co><small>NEXT</small>{tok("T-42","nx","2 pages · colour")}{tok("T-43","nx","38 pages · B&W")}{tok("T-44","nx","4 pages · B&W")}</div>
<div class=co><small>READY TO COLLECT</small>{tok("T-37","rd","Paid")}{tok("T-38","rd","Paid")}{tok("T-40","rd","Pay at pickup")}</div></div></div>
<div class=sd></div><div class=bs></div>
<div class=nt><span>{ic("clock",26)}</span><p>Customers send the file from home and walk in only when their token says <b>ready</b>.</p></div></div>''',
css=""".tvw{flex:1;display:flex;flex-direction:column;align-items:center}
.tv{width:100%;flex:1;background:#17181c;border-radius:26px;padding:18px;box-shadow:0 26px 50px rgba(23,24,28,.22)}
.sc{height:100%;background:#22242b;border-radius:14px;display:flex;gap:14px;padding:18px}
.co{flex:1;display:flex;flex-direction:column;gap:12px}.co small{font:700 16px 'Fira Sans';letter-spacing:2.5px;color:#9ea0aa;text-align:center}
.tk{flex:1;border-radius:16px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}.tk b{font:700 46px/1.3 'TeX Gyre Adventor'}.co .tk small{font:600 20px 'Fira Sans';letter-spacing:0;color:inherit;opacity:.8;text-align:center}
.tk.pn{background:#00a3e0;color:#fff;flex:2.2}.tk.pn b{font-size:84px}.tk.nx{background:#33363f;color:#fff}.tk.rd{background:#ffd400;color:#17181c}
.ds{font:600 19px/1.4 'Fira Sans';color:#cfd1d8;text-align:center}
.sd{width:120px;height:44px;background:linear-gradient(#2c2e35,#17181c)}.bs{width:340px;height:16px;border-radius:8px;background:#17181c}
.nt{margin-top:18px;width:100%;background:#fff;border-radius:20px;padding:16px 22px;font:500 21px/1.4 'Fira Sans';display:flex;gap:14px;align-items:center;box-shadow:0 10px 24px rgba(23,24,28,.07)}
.nt span{color:#e0218a;flex:none}.nt b{color:#b48f00}""")

summ = [("B&W pages", "1,180", "file"), ("Colour pages", "96", "img"), ("Spiral bindings", "14", "grid"), ("Staple jobs", "21", "check")]
P["p182_xerox_s4"] = xc(4, "PART 3 · READY ALERT", "Job done? The customer<br><span>gets a message.</span>",
f'''<div class=msg><div class=mh><span class=av>{ic("chat",28)}</span><div><b>Your Print Shop</b><span>Message · sample</span></div><em>4:52 PM</em></div>
<div class=mb><b>Token T-41 is ready.</b><span>project_report.pdf · 24 pages · both sides · 2 copies · spiral</span><span>Collect at the counter till 9 PM.</span></div></div>
<div class="cd dy"><div class=dh><small>TODAY AT THE SHOP · SAMPLE</small><b>62 jobs came in by link</b></div>
<div class=sg>{"".join(f'<div><i>{ic(c,34)}</i><b>{b}</b><span>{a}</span></div>' for a,b,c in summ)}</div>
<div class=bar><i style="width:94%"></i></div><div class=bl><span>58 collected</span><span>4 waiting</span></div></div>''',
css=""".vis{flex-direction:column;gap:16px}
.msg{background:#17181c;color:#fff;border-radius:26px;padding:22px 26px;display:flex;flex-direction:column;gap:16px}
.mh{display:flex;align-items:center;gap:14px}.av{width:54px;height:54px;border-radius:50%;background:#00a3e0;display:flex;align-items:center;justify-content:center}
.mh div{flex:1}.mh b{display:block;font:700 23px 'Fira Sans'}.mh span{font:500 17px 'Fira Sans';color:#9ea0aa}.mh em{font-style:normal;font:600 17px 'Fira Sans';color:#9ea0aa}
.mb{background:#2a2c33;border-radius:20px;padding:18px 22px;display:flex;flex-direction:column;gap:8px}.mb b{font:700 32px/1.3 'TeX Gyre Adventor';color:#ffd400}.mb span{font:500 21px/1.4 'Fira Sans'}
.dy{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:14px}
.dh small{display:block;font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#8b8c93}.dh b{font:700 32px/1.3 'TeX Gyre Adventor'}
.sg{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px}.sg div{border-radius:18px;background:#f6f5ef;padding:14px 26px;display:flex;flex-direction:column;justify-content:center}
.sg div:nth-child(1){border-left:8px solid #17181c}.sg div:nth-child(2){border-left:8px solid #e0218a}.sg div:nth-child(3){border-left:8px solid #00a3e0}.sg div:nth-child(4){border-left:8px solid #ffd400}
.sg div{position:relative}.sg i{position:absolute;top:18px;right:20px;color:#8b8c93}.sg b{font:700 72px/1.3 'TeX Gyre Adventor'}.sg span{font:600 22px 'Fira Sans';color:#6c6d75}
.bar{height:16px;border-radius:8px;background:#ececE4;overflow:hidden}.bar i{display:block;height:100%;background:#00a3e0;border-radius:8px}
.bl{display:flex;justify-content:space-between;font:600 18px 'Fira Sans';color:#6c6d75}""")

def printer():
    return ('<svg viewBox="0 0 520 400" width="600" style="display:block;flex:none">'
            '<rect x="150" y="10" width="220" height="100" rx="6" fill="#fff" stroke="#d9d8d0" stroke-width="3"/>'
            '<rect x="40" y="90" width="440" height="160" rx="26" fill="#17181c"/><rect x="60" y="112" width="160" height="22" rx="11" fill="#33363f"/>'
            '<circle cx="404" cy="124" r="10" fill="#00a3e0"/><circle cx="436" cy="124" r="10" fill="#e0218a"/><circle cx="372" cy="124" r="10" fill="#ffd400"/>'
            '<rect x="70" y="210" width="380" height="16" rx="8" fill="#000"/>'
            '<path d="M120 218h280l24 170H96z" fill="#fff" stroke="#d9d8d0" stroke-width="3"/>'
            '<text x="260" y="276" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="30" fill="#17181c"><tspan>Your print shop</tspan></text>'
            '<text x="260" y="316" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="30" fill="#e0218a"><tspan>online</tspan></text>'
            '<rect x="170" y="340" width="56" height="10" rx="5" fill="#00a3e0"/><rect x="232" y="340" width="56" height="10" rx="5" fill="#e0218a"/><rect x="294" y="340" width="56" height="10" rx="5" fill="#ffd400"/></svg>')
tiles = [("upload", "Order link", "File + details in one go"), ("grid", "Token screen", "Who is next, who is ready"), ("bell", "Ready alerts", "Customers come on time"), ("chart", "Day summary", "Pages, bindings, jobs")]
P["p182_xerox_s5"] = xc(5, "YOUR TURN", "Run a print or photocopy shop?<br><span>Let's put it online.</span>",
f'''<div class=pr>{printer()}</div><div class=tl>{"".join(f'<div><em>0{n}</em><span>{ic(i,52)}</span><b>{a}</b><small>{b}</small></div>' for n,(i,a,b) in enumerate(tiles,1))}</div>''',
cta="DM us to build yours", ctacss="background:#e0218a;color:#fff",
css=""".vis{flex-direction:column;gap:18px}.pr{display:flex;justify-content:center}
.tl{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:14px}.tl div{background:#fff;border-radius:22px;padding:18px 22px;display:flex;flex-direction:column;justify-content:center;gap:4px;box-shadow:0 10px 24px rgba(23,24,28,.07)}
.tl span{color:#00a3e0}.tl div:nth-child(2) span{color:#e0218a}.tl div:nth-child(3) span{color:#b48f00}
.tl div{position:relative}.tl em{position:absolute;right:22px;top:6px;font:700 84px/1.3 'TeX Gyre Adventor';font-style:normal;color:#eeede6}.tl span,.tl b,.tl small{position:relative}.tl b{font:700 36px/1.3 'TeX Gyre Adventor'}.tl small{font:500 22px 'Fira Sans';color:#6c6d75}""")


# ───────── 183 USA · Bridal boutique · SINGLE · Lora + Poppins · dove grey / champagne / plum
# New technique: fitting suites drawn as arches with curtains (closed = booked, open = free, dashed = on hold) as a day of try-on slots.
def arch(k, t, who):
    cur = {"b": '<path d="M14 60 Q14 8 80 8 Q146 8 146 60 V250 H14Z" fill="url(#ct)"/>',
           "o": '<path d="M14 60 Q14 8 80 8 Q30 30 32 250 H14Z" fill="url(#ct)"/><path d="M146 60 Q146 8 80 8 Q130 30 128 250 H146Z" fill="url(#ct)"/><rect x="62" y="150" width="36" height="100" rx="4" fill="#efe6d8"/><ellipse cx="80" cy="120" rx="26" ry="40" fill="#fff" stroke="#d8c8a8" stroke-width="3"/>',
           "h": '<path d="M14 60 Q14 8 80 8 Q146 8 146 60 V250 H14Z" fill="url(#ct)" opacity=".45"/>'}[k]
    frame = '#5b2a4a' if k != "h" else '#b98ba8'
    dash = ' stroke-dasharray="10 8"' if k == "h" else ''
    return (f'<div class="ar a{k}"><svg viewBox="0 0 160 262" width="160" height="262"><defs><linearGradient id="ct" x1="0" x2="1"><stop offset="0" stop-color="#d7b98a"/><stop offset=".15" stop-color="#f1dfbd"/><stop offset=".3" stop-color="#d7b98a"/><stop offset=".45" stop-color="#f1dfbd"/><stop offset=".6" stop-color="#d7b98a"/><stop offset=".75" stop-color="#f1dfbd"/><stop offset=".9" stop-color="#d7b98a"/></linearGradient></defs>'
            f'<path d="M14 60 Q14 8 80 8 Q146 8 146 60 V250 H14Z" fill="#faf6ef"/>{cur}<path d="M14 60 Q14 8 80 8 Q146 8 146 60 V250 H14Z" fill="none" stroke="{frame}" stroke-width="6"{dash}/><rect x="4" y="248" width="152" height="10" rx="5" fill="{frame}"/></svg>'
            f'<b>{t}</b><span>{who}</span></div>')
slots = [("b", "10:00 AM", "Booked"), ("b", "11:30 AM", "Booked"), ("o", "1:00 PM", "Open"), ("h", "2:30 PM", "On hold"), ("o", "4:00 PM", "Open")]
P["p183_bridal"] = page("""
body{--f:'Poppins';--h:'Lora';background:#ebe8e6;color:#3a1d33}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.6px;line-height:1.22} h1 span{color:#7b3a66;font-style:italic}
.sub{color:#6b5867;font-size:23px}
.vis{flex-direction:column;gap:16px}
.st{background:#fff;border-radius:28px;padding:18px 18px 14px;box-shadow:0 16px 34px rgba(58,29,51,.08)}
.st small{display:block;font:600 14px 'Poppins';letter-spacing:2.5px;color:#8f7a8a;margin:0 0 6px 8px}
.ars{display:flex;justify-content:space-between}
.ar{width:172px;display:flex;flex-direction:column;align-items:center;gap:2px}.ar svg{display:block}
.ar b{font:600 21px/1.35 'Poppins'}.ar span{font:600 15px 'Poppins';letter-spacing:1px;text-transform:uppercase;color:#8f7a8a;border-radius:20px;padding:3px 12px}
.ab span{background:#3a1d33;color:#fff}.ao span{background:#e8f1e4;color:#3c6a35}.ah span{border:2px dashed #b98ba8;color:#7b3a66}
.bk{flex:1;display:flex;gap:16px}
.fm{flex:1;background:#3a1d33;color:#fff;border-radius:28px;padding:22px 26px;display:flex;flex-direction:column;gap:10px}
.fm small{font:600 14px 'Poppins';letter-spacing:2.5px;color:#d7b98a}.fm h3{font:700 32px/1.3 'Lora'}
.fr{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:1px solid rgba(255,255,255,.16)}
.fr span{font:500 15px 'Poppins';letter-spacing:1.5px;color:#cdb9c8}.fr b{font:600 22px 'Poppins'}
.ch{display:flex;gap:8px;flex-wrap:wrap}.ch i{font-style:normal;font:500 17px 'Poppins';border:1.5px solid rgba(255,255,255,.35);border-radius:20px;padding:4px 14px}.ch i.on{background:#d7b98a;color:#3a1d33;border-color:#d7b98a;font-weight:600}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:16px}
.sl{flex:1;background:#fff;border-radius:28px;padding:20px 24px;display:flex;flex-direction:column;justify-content:center;gap:6px;box-shadow:0 16px 34px rgba(58,29,51,.08)}
.sl small{font:600 14px 'Poppins';letter-spacing:2.5px;color:#8f7a8a}.sl b{font:700 42px/1.3 'Lora';color:#7b3a66}.sl span{font:500 21px/1.45 'Poppins';color:#6b5867}.mi{display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:10px}.mi svg{display:block}.mi em{font-style:normal;font:600 17px 'Poppins';background:#f3ece4;border-radius:20px;padding:6px 14px}
.bt{background:#d7b98a;color:#3a1d33;border-radius:20px;padding:18px;text-align:center;font:600 22px 'Poppins'}
""", "<h1>Brides book try-ons<br><span>while you sleep.</span></h1><div class=sub>Open suites take bookings online. Booked ones stay closed.</div>",
f'''<div class=st><small>SATURDAY, NOV 28 · FITTING SUITES · SAMPLE</small><div class=ars>{"".join(arch(*s) for s in slots)}</div></div>
<div class=bk><div class=fm><small>BOOK A TRY-ON · SAMPLE BRIDE</small><h3>Tell us before you come</h3>
<div class=fr><span>WEDDING DATE</span><b>June 12, 2027</b></div>
<div class=fr><span>STYLES TO TRY</span><div class=ch>{"".join(f'<i class="{"on" if o else ""}">{a}</i>' for a,o in [("A-line",1),("Mermaid",0),("Ball gown",1),("Boho",0)])}</div></div>
<div class=fr><span>GUESTS COMING</span><b>3 people</b></div><div class=fr><span>REMINDER</span><b>Text the day before</b></div></div>
<div class=sd><div class=sl><div class=mi><svg viewBox="0 0 60 80" width="60" height="80"><path d="M6 26 Q6 4 30 4 Q54 4 54 26 V76 H6Z" fill="#faf6ef" stroke="#7b3a66" stroke-width="4"/><ellipse cx="30" cy="38" rx="11" ry="17" fill="#fff" stroke="#d7b98a" stroke-width="3"/></svg><em>90 min</em></div><small>YOUR PICK</small><b>Sat, 1:00 PM</b><span>Suite set up with your A&#8209;line and ball gown picks before you arrive.</span></div><div class=bt>Book this suite</div></div></div>''',
"#3a1d33", "Own a bridal shop? DM us", "background:#7b3a66;color:#fff")


# ───────── 184 INDIA · Scrap dealer (kabadi) · SINGLE · Bitter + Open Sans · rust orange / gunmetal / bone
# New technique: SVG platform scale with a live digital readout feeding a printed weight slip with a torn edge.
def scale():
    return ('<svg viewBox="0 0 400 560" width="100%" height="100%" preserveAspectRatio="xMidYMax meet" style="display:block">'
            '<rect x="186" y="96" width="28" height="330" fill="#3b4148"/>'
            '<rect x="60" y="20" width="280" height="110" rx="18" fill="#2b3036"/><rect x="80" y="38" width="240" height="74" rx="10" fill="#0f1a12"/>'
            '<text x="200" y="94" text-anchor="middle" font-family="DejaVu Sans Mono" font-weight="700" font-size="50" fill="#7dff8a"><tspan>38.5 kg</tspan></text>'
            '<g transform="translate(0,0)">'
            '<rect x="80" y="300" width="240" height="30" rx="4" fill="#cfc6b4" stroke="#8c836f" stroke-width="3"/>'
            '<rect x="84" y="330" width="232" height="30" rx="4" fill="#ddd5c3" stroke="#8c836f" stroke-width="3"/>'
            '<rect x="78" y="360" width="244" height="30" rx="4" fill="#cfc6b4" stroke="#8c836f" stroke-width="3"/>'
            '<rect x="82" y="390" width="236" height="30" rx="4" fill="#ddd5c3" stroke="#8c836f" stroke-width="3"/>'
            '<line x1="200" y1="296" x2="200" y2="424" stroke="#b5481f" stroke-width="5"/><line x1="74" y1="345" x2="326" y2="345" stroke="#b5481f" stroke-width="5"/>'
            '<line x1="74" y1="405" x2="326" y2="405" stroke="#b5481f" stroke-width="5"/></g>'
            '<rect x="20" y="424" width="360" height="40" rx="8" fill="#5a626b"/><rect x="34" y="434" width="332" height="6" rx="3" fill="#7b848e"/>'
            '<rect x="40" y="464" width="40" height="18" rx="4" fill="#2b3036"/><rect x="320" y="464" width="40" height="18" rx="4" fill="#2b3036"/>'
            '<text x="200" y="530" text-anchor="middle" font-family="Bitter" font-weight="700" font-size="24" fill="#2b3036"><tspan>Newspaper bundle</tspan></text></svg>')
items = [("Newspaper", "38.5"), ("Cardboard", "22.0"), ("Iron", "14.2"), ("Plastic", "6.8"), ("Aluminium", "3.1")]
pick = [("Sample shop, Gali 4", "84.6 kg", "Paid", "p"), ("Sample office", "41.0 kg", "Paid", "p"), ("Flat B-12", "12.4 kg", "Pending", "n"), ("Sample godown", "160.3 kg", "Weighing", "w")]
P["p184_scrap"] = page("""
body{--f:'Open Sans';--h:'Bitter';background:#efe7d8;color:#2b3036}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:0;line-height:1.22} h1 span{color:#b5481f}
.sub{color:#5d5a52;font-size:23px}
.vis{flex-direction:column;gap:16px}
.tp{flex:1;display:flex;gap:16px;min-height:0}
.scl{width:400px;flex:none;background:#fffaf0;border-radius:28px;padding:18px 18px 8px;display:flex;flex-direction:column;box-shadow:0 16px 34px rgba(43,48,54,.10)}
.scl small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#8c836f}
.scl .sv{flex:1;min-height:0}.tap{margin-top:12px;display:flex;flex-direction:column;gap:8px}.tap span{font:600 18px 'Open Sans';color:#5d5a52}.tap div{display:grid;grid-template-columns:1fr 1fr;gap:8px}.tap i{font-style:normal;font:600 19px 'Open Sans';text-align:center;padding:10px 0;border-radius:12px;border:2px solid #d8cfbd;background:#fff}.tap i.on{background:#b5481f;border-color:#b5481f;color:#fff}
.slp{flex:1;background:#fff;padding:26px 26px 22px;display:flex;flex-direction:column;gap:4px;clip-path:polygon(0 12px,4% 0,8% 12px,12% 0,16% 12px,20% 0,24% 12px,28% 0,32% 12px,36% 0,40% 12px,44% 0,48% 12px,52% 0,56% 12px,60% 0,64% 12px,68% 0,72% 12px,76% 0,80% 12px,84% 0,88% 12px,92% 0,96% 12px,100% 0,100% 100%,0 100%);border-radius:0 0 22px 22px}
.slp small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#8c836f;margin-top:6px}.slp h3{font:800 30px/1.3 'Bitter'}
.slp .mt{font:600 17px 'Open Sans';color:#6d685d;padding-bottom:6px;border-bottom:2px dashed #d8cfbd}
.ir{flex:1;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #eee6d6;font:600 22px 'Open Sans'}.ir b{font:700 22px 'Bitter'}
.ir.hl{color:#b5481f}
.tt{display:flex;justify-content:space-between;align-items:center;background:#2b3036;color:#fff;border-radius:14px;padding:12px 16px;margin-top:8px}.tt span{font:600 19px 'Open Sans'}.tt b{font:800 30px/1.3 'Bitter';color:#ffb38f}
.rt{font:500 16px/1.4 'Open Sans';color:#6d685d;margin-top:6px}
.pk{background:#2b3036;color:#fff;border-radius:24px;padding:16px 18px;display:flex;flex-direction:column;gap:10px}
.pk small{font:700 14px 'Open Sans';letter-spacing:2.5px;color:#c9bfae;margin-left:6px}
.pg4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.pg4 div{background:#3b4148;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:2px}
.pg4 span{font:600 16px/1.3 'Open Sans';color:#d8d2c6}.pg4 b{font:800 26px/1.3 'Bitter'}.pg4 em{font-style:normal;font:700 15px 'Open Sans';border-radius:10px;padding:3px 10px;align-self:flex-start;margin-top:4px}
.pg4 .p em{background:#3c6a35}.pg4 .n em{background:#b5481f}.pg4 .w em{background:#6b7480}
""", "<h1>Scrap weights still on<br><span>a torn chit?</span></h1><div class=sub>Weigh, tap, and the seller gets a clear slip on the spot.</div>",
f'''<div class=tp><div class=scl><small>LIVE WEIGHT · SAMPLE</small><div class=tap><span>Tap the item, then save:</span><div>{"".join(f'<i class="{"on" if a=="Newspaper" else ""}">{a}</i>' for a,_ in items[:4])}</div></div><div class=sv>{scale()}</div></div>
<div class=slp><small>WEIGHT SLIP · P-118 · SAMPLE</small><h3>Sample shop, Gali 4</h3><div class=mt>Sun, 22 Nov · 11:40 AM</div>
{"".join(f'<div class="ir {"hl" if i==0 else ""}"><span>{a}</span><b>{k} kg</b></div>' for i,(a,k) in enumerate(items))}
<div class=tt><span>Total weight</span><b>84.6 kg</b></div><div class=rt>Amount as per your own rate list. Slip sent to the seller by link.</div></div></div>
<div class=pk><small>TODAY'S PICKUPS · SAMPLE</small><div class=pg4>{"".join(f'<div class={k}><span>{a}</span><b>{w}</b><em>{s}</em></div>' for a,w,s,k in pick)}</div></div>''',
"#2b3036", "Run a scrap business? DM us", "background:#b5481f;color:#fff")


# ───────── 185 INDIA · Wedding card printer · SINGLE · Crimson Text + DM Sans · ivory / vermilion / bottle green
# New technique: proof timeline strip — three mini card proofs v1 → v2 → v3 with red-pen rings and margin notes, last one stamped approved.
def proof(v, mark, note, ok=False):
    flor = ('<svg viewBox="0 0 220 40" width="100%" height="44" style="display:block"><path d="M10 20 Q60 0 110 20 Q160 40 210 20" fill="none" stroke="#1f5a43" stroke-width="2.5"/>'
            '<circle cx="110" cy="20" r="7" fill="#d9442b"/><circle cx="60" cy="11" r="4.5" fill="#d9a441"/><circle cx="160" cy="29" r="4.5" fill="#d9a441"/><circle cx="20" cy="18" r="3.5" fill="#1f5a43"/><circle cx="200" cy="22" r="3.5" fill="#1f5a43"/></svg>')
    lines = [("tg", "Together with their families"), ("t", "Sample Bride"), ("a", "&amp;"), ("t", "Sample Groom"), ("d", "Saturday, 12 December 2026"), ("tm", "7 PM onwards" if v == 1 else "7:30 PM onwards"), ("vn", "Sample Venue, Ring Road")]
    lines.insert(4, ("iv", "invite you to their wedding"))
    if v == 3: lines.append(("rs", "RSVP: your number"))
    body = '<div class=mid>' + "".join(f'<p class="{k}{" mk" if mark==k else ""}">{t}</p>' for k, t in lines) + '</div>'
    return (f'<div class="pf{" ap" if ok else ""}"><div class=vt>v{v}</div><div class=cardp>{flor}{body}{flor}</div>'
            + (f'<div class=nt>{note}</div>' if not ok else f'<div class=stmp>{ic("check",22,w=3)} APPROVED</div>') + '</div>')
log = [("v1", "Thu", "Change time to 7:30 PM"), ("v2", "Fri", "Add an RSVP number"), ("v3", "Today", "Approved by the client")]
P["p185_weddingcard"] = page("""
body{--f:'DM Sans';--h:'Crimson Text';background:#f7f1e3;color:#1c2b24}
h1{font-family:'Crimson Text';font-size:66px;font-weight:700;letter-spacing:-.4px;line-height:1.22} h1 span{color:#d9442b}
.sub{color:#5d6a62;font-size:23px}
.vis{flex-direction:column;gap:16px}
.strip{flex:1;display:flex;gap:14px;align-items:stretch;margin-top:10px}
.pf{flex:1;display:flex;flex-direction:column;gap:10px;position:relative}
.vt{position:absolute;top:-12px;left:14px;z-index:3;background:#1c2b24;color:#fff;font:700 16px 'DM Sans';padding:4px 14px;border-radius:12px}
.cardp{flex:1;background:#fffdf7;border:2px solid #e3d6b8;border-radius:14px;padding:26px 14px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;gap:2px;text-align:center;box-shadow:inset 0 0 0 9px #fffdf7,inset 0 0 0 11px #eadcbc,0 12px 26px rgba(28,43,36,.10)}.mid{display:flex;flex-direction:column;align-items:center;gap:2px}.cardp .tg{font:italic 600 19px/1.3 'Crimson Text';color:#5d6a62;margin-bottom:8px}.cardp .iv{font:italic 600 19px/1.3 'Crimson Text';color:#5d6a62;margin-top:6px}
.cardp p{font-family:'Crimson Text';color:#1c2b24;line-height:1.3;padding:0 8px}
.cardp .t{font-size:34px;font-weight:700;color:#1f5a43}.cardp .a{font-size:24px;color:#d9a441}
.cardp .d{font:600 17px/1.45 'DM Sans';margin-top:14px}.cardp .tm{font:600 17px/1.45 'DM Sans'}.cardp .vn{font:500 17px/1.45 'DM Sans';color:#5d6a62}.cardp .rs{font:700 17px/1.45 'DM Sans';color:#1f5a43}
.cardp .mk{border:3px solid #e0301e;border-radius:40px}
.nt{background:#fff;border-left:6px solid #e0301e;border-radius:10px;padding:10px 14px;font:italic 600 21px/1.3 'Crimson Text';color:#c4281a}
.stmp{background:#1f5a43;color:#fff;border-radius:10px;padding:10px 14px;font:700 18px 'DM Sans';letter-spacing:2px;display:flex;align-items:center;justify-content:center;gap:8px}
.pf.ap .cardp{border-color:#1f5a43;border-width:3px;box-shadow:inset 0 0 0 9px #fffdf7,inset 0 0 0 11px #9cc3ae,0 12px 26px rgba(28,43,36,.10)}
.bt2{flex:none;display:flex;gap:16px}
.lg2{flex:1;background:#fff;border-radius:26px;padding:20px 24px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(28,43,36,.07)}
.lg2 small,.od small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#8a8f7f}
.lr{flex:none;padding:12px 0;display:flex;align-items:center;gap:14px;border-top:1px solid #efe7d4}.lr em{font-style:normal;width:50px;height:36px;border-radius:10px;background:#f7f1e3;font:700 17px 'DM Sans';display:flex;align-items:center;justify-content:center;flex:none}
.lr span{width:64px;flex:none;font:600 17px 'DM Sans';color:#8a8f7f}.lr b{font:600 21px/1.3 'DM Sans'}.lr:last-child b{color:#1f5a43}
.od{width:360px;flex:none;background:#1f5a43;color:#fff;border-radius:26px;padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.od small{color:#a9d1bd}.od b{font:700 34px/1.25 'Crimson Text'}.od span{font:500 18px/1.4 'DM Sans';color:#dcebe2}
.od i{font-style:normal;margin-top:8px;background:#d9442b;border-radius:14px;padding:12px;text-align:center;font:700 19px 'DM Sans'}
""", "<h1>Card proof changed again?<br><span>Keep every version in one place.</span></h1>",
f'''<div class=strip>{proof(1,"tm","7 PM → 7:30 PM")}{proof(2,"vn","Add RSVP below this")}{proof(3,"","",True)}</div>
<div class=bt2><div class=lg2><small>PROOF HISTORY · SAMPLE ORDER W-27</small>{"".join(f'<div class=lr><em>{a}</em><span>{d}</span><b>{t}</b></div>' for a,d,t in log)}</div>
<div class=od><small>ORDER · SAMPLE</small><b>300 cards + 300 envelopes</b><span>Printing starts only after approval. Ready Fri, 4 Dec.</span><i>Client approves on a link</i></div></div>''',
"#1c2b24", "Print wedding cards? DM us", "background:#d9442b;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
