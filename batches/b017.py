import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 101 INDIA · Poultry / egg supplier · SINGLE · Montserrat + Source Sans 3 · eggshell / barn red / straw / charcoal
# New technique: top-down SVG egg tray (6x5 cups, eggs with highlights, two empty cups) + side-view tray stack with count,
# and a route table that also tracks EMPTY TRAYS to collect back.
def eggtray(cols=6, rows=5, empty=((5, 4), (4, 4)), cell=66):
    W, H = cols * cell + 28, rows * cell + 28
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}"><rect x="0" y="0" width="{W}" height="{H}" rx="18" fill="#d9ccb3"/>'
         f'<rect x="6" y="6" width="{W-12}" height="{H-12}" rx="14" fill="none" stroke="#c4b598" stroke-width="3"/>']
    for r in range(rows):
        for c in range(cols):
            x, y = 14 + c * cell + cell / 2, 14 + r * cell + cell / 2
            s.append(f'<circle cx="{x}" cy="{y}" r="{cell*0.42:.1f}" fill="#c9b994"/><circle cx="{x}" cy="{y}" r="{cell*0.34:.1f}" fill="#bba981"/>')
            if (c, r) not in empty:
                s.append(f'<ellipse cx="{x}" cy="{y}" rx="{cell*0.3:.1f}" ry="{cell*0.36:.1f}" fill="#f7efe2"/>'
                         f'<ellipse cx="{x-cell*0.08:.1f}" cy="{y-cell*0.12:.1f}" rx="{cell*0.09:.1f}" ry="{cell*0.12:.1f}" fill="#ffffff" opacity=".85"/>')
    s.append('</svg>')
    return "".join(s)
stack = '<svg viewBox="0 0 150 300" width="150" height="300">' + "".join(
    f'<path d="M6 {y} q12 -14 23 0 t23 0 t23 0 t23 0 t23 0 t23 0 v12 H6 Z" fill="{"#d9ccb3" if i%2 else "#cdbfa4"}" stroke="#b3a27f" stroke-width="2"/>'
    for i, y in enumerate(range(40, 290, 21))) + '</svg>'
route = [("Sample Kirana 1", "Main Market", "12", "10", "2 days"),
         ("Sample Bakery", "Station Road", "8", "8", "Paid"),
         ("Sample Hotel", "Highway", "20", "14", "5 days"),
         ("Sample Shop 4", "Sector 9", "6", "6", "Paid"),
         ("Sample Shop 5", "Old Town", "10", "7", "1 day")]
P["p101_eggs"] = page("""
body{--f:'Source Sans 3';--h:'Montserrat';background:#f6efe1;color:#26221f}
h1{font-family:'Montserrat';font-size:62px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#b8402f}
.sub{color:#6d6257}
.vis{flex-direction:column;gap:16px}
.hero{flex:none;display:flex;gap:16px}
.tr{flex:1;background:#e8b64a;border-radius:28px;display:flex;align-items:center;justify-content:center;padding:18px;position:relative}
.tr svg{display:block}
.sk{width:250px;flex:none;background:#26221f;color:#f6efe1;border-radius:28px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;padding:16px}
.sk svg{display:block;width:120px;height:240px}
.sk b{font:800 44px/1.25 Montserrat;color:#e8b64a}.sk span{font:600 18px/1.3 'Source Sans 3';color:#cfc4b6;text-align:center}
.tb{flex:1;background:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(38,34,31,.07)}
.tb small{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#9a8e80;padding-bottom:6px}
.rw{flex:1;display:grid;grid-template-columns:1.7fr .8fr .9fr .9fr;align-items:center;gap:10px;border-top:1.5px solid #efe7d8}
.rw.hd{flex:none;border-top:none;padding-bottom:6px;font:700 15px 'Source Sans 3';color:#9a8e80;letter-spacing:.5px}
.rw b{font:700 22px 'Source Sans 3';display:block}.rw i{font:500 16px 'Source Sans 3';font-style:normal;color:#8a7f72}
.rw .n{font:800 26px Montserrat}
.rw .bk{font:700 20px 'Source Sans 3';color:#b8402f}
.rw .bk.ok{color:#3f7a4a}
.rw em{font-style:normal;font:700 16px 'Source Sans 3';padding:6px 10px;border-radius:8px;background:#f6efe1;justify-self:start;white-space:nowrap}
.rw em.due{background:#b8402f;color:#fff}
""", "<h1>Eggs to 40 shops<br>every morning?<br><span>Track trays, empties<br>and dues per shop.</span></h1>",
f'''<div class=hero><div class=tr>{eggtray()}</div><div class=sk>{stack}<b>12 trays</b><span>empty trays still<br>with shops · sample</span></div></div>
<div class=tb><small>TODAY'S ROUTE · SAMPLE</small>
<div class="rw hd"><span>Shop</span><span>Trays given</span><span>Empties back</span><span>Payment</span></div>
{"".join(f'<div class=rw><div><b>{a}</b><i>{b}</i></div><span class=n>{c}</span><span class="bk {"ok" if c==d else ""}">{d} of {c}</span><em class="{"" if e=="Paid" else "due"}">{"Paid" if e=="Paid" else "Unpaid " + e}</em></div>' for a,b,c,d,e in route)}</div>''',
"#26221f", "Egg supplier? DM us", "background:#b8402f;color:#fff")

# ───────── 103 USA · Thrift / resale shop · SINGLE · TeX Gyre Adventor + DM Sans · mustard / forest green / manila tag
# New technique: SVG hang tags on strings from a clothes rail (each tag = item code + size + online status),
# then a browser "new in" grid where the item sold in store shows "Sold in store" automatically.
def tag(code, item, size, st, x):
    on = st == "online"
    col = "#1f4d3a" if on else "#b23a2a"
    txt = "On your site" if on else "Sold in store"
    return f'''<g transform="translate({x},0)">
<path d="M90 0 C 90 30, 70 40, 90 70" stroke="#5c4a2e" stroke-width="3" fill="none"/>
<path d="M30 70 H150 L180 100 V330 H0 V100 Z" fill="#f1dfb5" stroke="#c9b07a" stroke-width="3"/>
<circle cx="90" cy="96" r="11" fill="#e3b341" stroke="#c9b07a" stroke-width="3"/>
<text x="90" y="150" text-anchor="middle" font-family="TeX Gyre Adventor" font-weight="700" font-size="30" fill="#2a241b">{code}</text>
<text x="90" y="188" text-anchor="middle" font-family="DM Sans" font-weight="600" font-size="21" fill="#5c4a2e">{item}</text>
<text x="90" y="220" text-anchor="middle" font-family="DM Sans" font-weight="500" font-size="19" fill="#7a6a4f">Size {size}</text>
<g fill="#2a241b">{"".join(f'<rect x="{30+i*8}" y="240" width="{3 if i%3 else 5}" height="34"/>' for i in range(15))}</g>
<rect x="18" y="288" width="144" height="30" rx="8" fill="{col}"/>
<text x="90" y="309" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="16" fill="#fff">{txt}</text>
</g>'''
rail = (f'<svg viewBox="0 0 900 350" width="900" height="350"><rect x="0" y="0" width="900" height="12" rx="6" fill="#5c4a2e"/>'
        + tag("A-214", "Denim jacket", "M", "online", 20) + tag("A-215", "Wool coat", "L", "online", 250)
        + tag("A-216", "Leather boots", "9", "sold", 480) + tag("A-217", "Table lamp", "—", "online", 710) + '</svg>')
def thumb(kind, c):
    shapes = {
        "jacket": f'<path d="M30 20 L50 10 H70 L90 20 L105 70 L90 74 V110 H30 V74 L15 70 Z" fill="{c}"/><path d="M60 14 V110" stroke="#fff" stroke-width="2" opacity=".5"/>',
        "coat": f'<path d="M35 14 L50 8 H70 L85 14 L100 112 H20 Z" fill="{c}"/><circle cx="60" cy="50" r="3" fill="#fff"/><circle cx="60" cy="70" r="3" fill="#fff"/>',
        "boots": f'<path d="M30 10 H58 V70 Q60 78 72 80 L92 84 Q104 87 104 98 V104 H30 Z" fill="{c}"/><rect x="30" y="104" width="74" height="8" rx="3" fill="#2a241b"/><rect x="30" y="104" width="16" height="12" fill="#2a241b"/><path d="M30 24 H58" stroke="#fff" stroke-width="2" opacity=".4"/>',
        "lamp": f'<path d="M36 18 H84 L96 58 H24 Z" fill="{c}"/><rect x="56" y="58" width="8" height="40" fill="#5c4a2e"/><rect x="38" y="98" width="44" height="10" rx="4" fill="#5c4a2e"/>',
        "bag": f'<path d="M40 40 Q40 14 60 14 Q80 14 80 40" fill="none" stroke="{c}" stroke-width="8"/><rect x="22" y="40" width="76" height="66" rx="10" fill="{c}"/>',
        "chair": f'<rect x="34" y="12" width="52" height="48" rx="8" fill="{c}"/><rect x="28" y="60" width="64" height="16" rx="6" fill="{c}"/><path d="M34 76 V110 M86 76 V110" stroke="#5c4a2e" stroke-width="6"/>'}
    return f'<svg viewBox="0 0 120 120" width="100%" height="100%">{shapes[kind]}</svg>'
grid = [("jacket", "#3d5a80", "Denim jacket", "A-214 · M", ""), ("coat", "#8a5a44", "Wool coat", "A-215 · L", ""),
        ("boots", "#4a3b2c", "Leather boots", "A-216 · 9", "sold"), ("lamp", "#e3b341", "Table lamp", "A-217", ""),
        ("bag", "#1f4d3a", "Canvas bag", "A-218", ""), ("chair", "#b23a2a", "Side chair", "A-219", "")]
P["p103_thrift"] = page("""
body{--f:'DM Sans';--h:'TeX Gyre Adventor';background:#e3b341;color:#1d2a22}
h1{font-family:'TeX Gyre Adventor';font-size:58px;font-weight:700;letter-spacing:-1px} h1 span{color:#1f4d3a;background:#f6ecd0;padding:0 12px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.vis{flex-direction:column;gap:16px}
.rl{flex:none;display:flex;justify-content:center;padding-top:4px}
.rl svg{display:block}
.nw{flex:1;min-height:0;display:flex;flex-direction:column;padding:14px 22px 16px;gap:10px;background:#fffaf0}
.nw .t{display:flex;justify-content:space-between;align-items:baseline}
.nw h3{font:700 28px/1.25 'TeX Gyre Adventor'}.nw small{font:700 13px 'DM Sans';letter-spacing:3px;color:#8d7f62}
.gd{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px;min-height:0}
.it{background:#f4ead2;border-radius:16px;padding:12px;display:grid;grid-template-columns:120px 1fr;grid-template-rows:1fr auto auto auto 1fr;column-gap:14px;row-gap:3px;position:relative;min-width:0}
.it .im{grid-row:1/6;background:#fff;border-radius:12px;padding:8px;display:flex;align-items:center}
.it b{grid-row:2;font:700 21px/1.25 'DM Sans'}.it span{grid-row:3;font:500 17px 'DM Sans';color:#7a6a4f}
.it i{grid-row:4;justify-self:start;margin-top:4px;font:700 15px 'DM Sans';font-style:normal;background:#1f4d3a;color:#fff;border-radius:8px;padding:5px 10px}.it i.off{background:#b23a2a}
.it.sold .im{opacity:.35}
.it.sold em{position:absolute;left:12px;top:12px;width:120px;background:#b23a2a;color:#fff;font:700 15px 'DM Sans';font-style:normal;text-align:center;border-radius:8px;padding:6px 0}
""", "<h1>Sold in the shop,<br>still on your website?<br><span>One list for both.</span></h1><div class=sub>For thrift and resale shops: tag it, snap it, and it's online. Sell it, and it comes off.</div>",
f'''<div class=rl>{rail}</div>
{browser(f"""<div class=nw><div class=t><h3>New in this week</h3><small>YOUR SHOP · SAMPLE</small></div><div class=gd>
{"".join(f'<div class="it {s}"><div class=im>{thumb(k,c)}</div>' + ('<em>Sold in store</em>' if s else '') + f'<b>{n}</b><span>{d}</span>' + ('<i class=off>Off the site</i>' if s else '<i>On the site</i>') + '</div>' for k,c,n,d,s in grid)}</div></div>""", "shop.yourthrift.com · sample", "flex:1", bar="#efe6cf")}''',
"#1d2a22", "Resale shop? DM us", "background:#1f4d3a;color:#fff")

# ───────── 105 INDIA · Dry fruits seller · SINGLE · Cardo + Poppins · walnut brown / pistachio green / almond cream
# New technique: top-down SVG gift box with 4 compartments of drawn nuts (almonds, cashews, raisins, pistachios)
# + a 4-step box builder card with selected options.
import random
random.seed(105)
def nuts(kind, x0, y0, w, h):
    out = []
    for i in range(70 if kind != "raisin" else 120):
        x, y = x0 + 16 + random.random() * (w - 32), y0 + 16 + random.random() * (h - 32)
        a = random.randint(0, 179)
        if kind == "almond":
            out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="17" ry="10" transform="rotate({a} {x:.0f} {y:.0f})" fill="#b7773f" stroke="#8f5a2c" stroke-width="2"/>')
        elif kind == "cashew":
            out.append(f'<path d="M{x-16:.0f} {y+5:.0f} C{x-16:.0f} {y-16:.0f} {x+16:.0f} {y-16:.0f} {x+16:.0f} {y+5:.0f} C{x+8:.0f} {y+2:.0f} {x-8:.0f} {y+2:.0f} {x-16:.0f} {y+5:.0f} Z" transform="rotate({a} {x:.0f} {y:.0f})" fill="#f0d9a8" stroke="#c9a66b" stroke-width="2"/>')
        elif kind == "raisin":
            out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="8" ry="6" transform="rotate({a} {x:.0f} {y:.0f})" fill="#6b2f3a" stroke="#4a1d27" stroke-width="1.5"/>')
        else:
            out.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="13" ry="9" transform="rotate({a} {x:.0f} {y:.0f})" fill="#d9c79a" stroke="#a8925f" stroke-width="2"/>'
                       f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="7" ry="5" transform="rotate({a} {x:.0f} {y:.0f})" fill="#7fa64a"/>')
    return "".join(out)
cw, chh = 200, 200
box = (f'<svg viewBox="0 0 460 460" width="460" height="460"><rect x="0" y="0" width="460" height="460" rx="26" fill="#5a3a22"/>'
       f'<rect x="14" y="14" width="432" height="432" rx="18" fill="#7a5233"/>'
       + "".join(f'<clipPath id="c{i}"><rect x="{x}" y="{y}" width="{cw}" height="{chh}" rx="14"/></clipPath><rect x="{x}" y="{y}" width="{cw}" height="{chh}" rx="14" fill="#efe2c4"/><g clip-path="url(#c{i})">{nuts(k,x,y,cw,chh)}</g>'
                 for i, (k, x, y) in enumerate([("almond", 22, 22), ("cashew", 238, 22), ("pista", 22, 238), ("raisin", 238, 238)]))
       + '</svg>')
P["p105_dryfruit"] = page("""
body{--f:'Poppins';--h:'Cardo';background:#f4ead6;color:#3b2716}
h1{font-family:'Cardo';font-size:66px;font-weight:700;letter-spacing:-.5px} h1 span{color:#5d7d2f}
.sub{color:#7a6550}
.vis{gap:20px}
.lf{width:500px;flex:none;display:flex;flex-direction:column;gap:14px}
.bx{flex:1;background:#5d7d2f;border-radius:30px;display:flex;align-items:center;justify-content:center;position:relative}
.bx svg{display:block}
.rb{position:absolute;left:50%;transform:translateX(-50%);bottom:18px;background:#f4ead6;color:#3b2716;border-radius:30px;padding:8px 18px;font:600 16px Poppins;white-space:nowrap}
.lgd{flex:none;display:grid;grid-template-columns:1fr 1fr;gap:8px}
.lgd span{background:#fff;border-radius:12px;padding:10px 14px;font:600 18px Poppins;display:flex;align-items:center;gap:10px}
.lgd i{width:16px;height:16px;border-radius:50%;display:block;flex:none}
.bd{flex:1;background:#fffaf0;border-radius:28px;padding:22px 24px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 34px rgba(59,39,22,.08);min-width:0}
.bd small{font:700 13px Poppins;letter-spacing:3px;color:#9b8670}
.bd h3{font:700 32px/1.25 Cardo}
.st{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:1.5px solid #efe4cf}
.st .q{display:flex;align-items:center;gap:10px;font:600 17px Poppins;color:#7a6550}
.st .q b{width:30px;height:30px;border-radius:50%;background:#3b2716;color:#f4ead6;font:700 15px/1 Poppins;display:flex;align-items:center;justify-content:center;flex:none}
.op{display:flex;gap:8px;flex-wrap:wrap}
.op em{font-style:normal;font:600 16px Poppins;padding:7px 12px;border-radius:10px;background:#f4ead6}
.op em.on{background:#5d7d2f;color:#fff}
.msg{font:italic 400 20px/1.35 Cardo;background:#f4ead6;border-radius:10px;padding:8px 12px}
.bt{flex:none;background:#3b2716;color:#fff;border-radius:14px;text-align:center;font:600 19px Poppins;padding:14px}
""", "<h1>Gift box orders<br>on 50 phone calls?<br><span>Let buyers build<br>the box online.</span></h1>",
f'''<div class=lf><div class=bx>{box}<div class=rb>4-section box · sample</div></div>
<div class=lgd>{"".join(f'<span><i style="background:{c}"></i>{n}</span>' for n,c in [("Almonds","#b7773f"),("Cashews","#e9cf9c"),("Pistachios","#7fa64a"),("Raisins","#6b2f3a")])}</div></div>
<div class=bd><small>BUILD YOUR BOX · SAMPLE</small><h3>Your Dry Fruits</h3>
<div class=st><div class=q><b>1</b>Box size</div><div class=op><em>2 sections</em><em class=on>4 sections</em><em>6 sections</em></div></div>
<div class=st><div class=q><b>2</b>Fill each section</div><div class=op><em class=on>Almonds</em><em class=on>Cashews</em><em class=on>Pistachios</em><em class=on>Raisins</em></div></div>
<div class=st><div class=q><b>3</b>Note card</div><div class=msg>“Thanks for a great year. Sample Co.”</div></div>
<div class=st><div class=q><b>4</b>How many and when</div><div class=op><em class=on>40 boxes</em><em class=on>Deliver 12 Dec</em></div></div>
<div class=bt>Send bulk order</div></div>''',
"#3b2716", "Sell dry fruits? DM us", "background:#5d7d2f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
