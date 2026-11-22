import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 86 INDIA · Mobile accessories and watch shop · SINGLE · Anton + Source Sans 3 · graphite / electric cyan / receipt white
# New technique: thermal receipt roll with zigzag tear edge (clip-path) and faded print.
rec = [("Wireless earbuds","1 year"),("Phone charger 20W","6 months"),("Analog wrist watch","1 year"),("Tempered glass","No warranty")]
P["p86_accessories"] = page("""
body{--f:'Source Sans 3';--h:'Anton';background:#1e2228;color:#eef2f5}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#2fd6f0}
.sub{color:#a9b3bd}
.vis{gap:22px}
.rl{width:380px;flex:none;display:flex;flex-direction:column;align-items:center}
.rr{width:300px;height:40px;border-radius:20px;background:linear-gradient(#f5f3ee,#d9d6cf);flex:none;box-shadow:0 8px 18px rgba(0,0,0,.35)}
.rp{width:270px;flex:1;margin-top:-20px;background:#fbfaf6;color:#3c3f44;padding:40px 22px 40px;display:flex;flex-direction:column;gap:10px;clip-path:polygon(0 0,100% 0,100% calc(100% - 14px),93% 100%,86% calc(100% - 14px),79% 100%,72% calc(100% - 14px),65% 100%,58% calc(100% - 14px),51% 100%,44% calc(100% - 14px),37% 100%,30% calc(100% - 14px),23% 100%,16% calc(100% - 14px),9% 100%,2% calc(100% - 14px),0 100%);font-family:'Source Sans 3'}
.rp b{font:700 22px 'Source Sans 3';text-align:center;letter-spacing:2px}
.rp .ln{border-top:2px dashed #c9c6be}
.rp .r{display:flex;justify-content:space-between;font:600 17px 'Source Sans 3';opacity:.55}
.rp .fd{opacity:.22}
.rp .x{font:700 18px 'Source Sans 3';color:#d0412f;text-align:center;border:3px solid #d0412f;border-radius:8px;padding:6px;margin-top:auto}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.sr{background:#eef2f5;color:#1e2228;border-radius:18px;padding:16px 18px;display:flex;align-items:center;gap:12px;font:700 23px 'Source Sans 3'}
.sr svg{color:#0b8fa6}
.ls{flex:1;background:#2a3038;border-radius:26px;padding:20px;display:flex;flex-direction:column;gap:10px}
.ls small{font:700 14px 'Source Sans 3';letter-spacing:3px;color:#8d98a3}
.it{flex:1;background:#343b45;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.it .t{display:flex;justify-content:space-between;align-items:center}
.it b{font:700 27px 'Source Sans 3'}
.it em{font-style:normal;font:700 18px 'Source Sans 3';padding:5px 10px;border-radius:8px;white-space:nowrap}
.ok{background:#173f47;color:#2fd6f0}.nw{background:#4a3a14;color:#ffd166}.nx{background:#3f444c;color:#a9b3bd}
.it span{font:500 20px 'Source Sans 3';color:#a9b3bd}
""", "<h1>“I lost the bill.”<br><span>Find the warranty<br>by phone number.</span></h1><div class=sub>For mobile accessories and watch shops: every sale and warranty saved with the customer.</div>",
f'''<div class=rl><div class=rr></div><div class=rp><b>YOUR SHOP</b><div class=ln></div>
{"".join(f'<div class="r {"fd" if i%2 else ""}"><span>{"Item " + str(i+1)}</span><span>Qty 1</span></div>' for i in range(9))}
<div class=ln></div><div class="r fd"><span>Date</span><span>faded</span></div><div class=x>Paper bills fade</div></div></div>
<div class=rc><div class=sr>{ic("search",28)}98XXX XXX47 · sample customer</div>
<div class=ls><small>PURCHASES AND WARRANTY · SAMPLE</small>{"".join(f'<div class=it><div class=t><b>{n}</b><em class={k}>{s}</em></div><span>Bought {d} · warranty {w}</span></div>' for n,w,d,s,k in [("Wireless earbuds","1 year","10 Mar 2026","Valid till Mar 2027","ok"),("Analog wrist watch","1 year","2 Dec 2025","Ends next month","nw"),("Phone charger 20W","6 months","15 Jan 2026","Ended in July","nx")])}</div></div>''',
"#eef2f5", "Accessories shop? DM us", "background:#2fd6f0;color:#1e2228")

# ───────── 88 USA · Insurance agency · SINGLE · Bitter + Source Sans 3 · deep navy / sky / sunflower
# New technique: horizontal month ruler with policy pins (renewal timeline) above a reminder queue.
pins = [(4,"Home · Sample client A",0),(12,"Auto · Sample client B",1),(19,"Business · Sample client C",0),(27,"Renters · Sample client D",1)]
P["p88_insurance"] = page("""
body{--f:'Source Sans 3';--h:'Bitter';background:#eaf2fb;color:#14284b}
h1{font-family:'Bitter';font-size:64px;font-weight:800;letter-spacing:-1px} h1 span{color:#2f6fd6}
.sub{color:#556681}
.vis{flex-direction:column;gap:18px}
.tl{flex:1;background:#14284b;border-radius:30px;padding:24px 30px;display:flex;flex-direction:column;color:#fff}
.tl .hd{display:flex;justify-content:space-between;align-items:center}
.tl .hd b{font:800 28px Bitter}.tl .hd small{font:700 14px 'Source Sans 3';letter-spacing:3px;color:#9db4d8}
.ax{flex:1;position:relative;margin-top:16px}
.ax .ln{position:absolute;left:0;right:0;bottom:56px;height:6px;background:#2d4673;border-radius:3px}
.ax .tk{position:absolute;bottom:20px;font:700 17px 'Source Sans 3';color:#9db4d8;transform:translateX(-50%)}
.ax .td{position:absolute;bottom:44px;width:4px;height:30px;background:#ffd23f;border-radius:2px}
.ax .tdl{position:absolute;bottom:80px;font:700 15px 'Source Sans 3';color:#ffd23f;letter-spacing:2px}
.pn{position:absolute;bottom:62px;display:flex;flex-direction:column;align-items:flex-start}
.pn .cd{background:#fff;color:#14284b;border-radius:14px;padding:12px 16px;font:700 22px 'Source Sans 3';white-space:nowrap;box-shadow:0 10px 20px rgba(0,0,0,.25)}
.pn .cd em{display:block;font-style:normal;font:600 18px 'Source Sans 3';color:#2f6fd6}
.pn .st{width:4px;background:#fff;margin-left:16px}
.pn.hi .cd{background:#ffd23f}.pn.rt{align-items:flex-end;transform:translateX(calc(-100% + 20px))}.pn.rt .st{margin:0 16px 0 0}
.qq{display:flex;gap:14px;flex:none}
.q{flex:1;background:#fff;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(20,40,75,.08)}
.q small{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#8796ad}
.q .bb{background:#eaf2fb;border-radius:14px 14px 14px 4px;padding:12px 14px;font:500 19px/1.4 'Source Sans 3'}
.q .ss{display:flex;justify-content:space-between;align-items:center;font:700 18px 'Source Sans 3'}
.q .ss em{font-style:normal;font:700 15px 'Source Sans 3';background:#dff3e4;color:#1e7a3e;padding:5px 10px;border-radius:8px}
.q.dk{background:#2f6fd6;color:#fff}.q.dk small{color:#cfe0fb}
.q.dk b{font:800 26px/1.3 Bitter}.q.dk span{font:500 19px/1.4 'Source Sans 3'}
""", "<h1>Renewal dates in a spreadsheet?<br><span>Get reminded before they lapse.</span></h1><div class=sub>For insurance agencies: every renewal on a timeline, with reminders to you and the client.</div>",
f'''<div class=tl><div class=hd><b>Next 30 days</b><small>RENEWALS · SAMPLE</small></div><div class=ax>
{"".join(f'<div class="pn {"hi" if h else ""} {"rt" if d>22 else ""}" style="left:{3+d*3.0:.0f}%"><div class=cd>Day {d}<em>{t}</em></div><div class=st style="height:{[60,290,60,200][i]}px"></div></div>' for i,(d,t,h) in enumerate(pins))}
<div class=ln></div><div class=td style="left:0"></div><div class=tdl style="left:12px">TODAY</div>
{"".join(f'<span class=tk style="left:{3+d*3.0:.0f}%">Day {d}</span>' for d in (7,14,21,28))}</div></div>
<div class=qq><div class=q><small>TO THE CLIENT · BEFORE RENEWAL</small><div class=bb>Hi, your auto policy renews in 12 days. Reply YES to review it with us.</div><div class=ss>Sample client B<em>Replied YES</em></div></div>
<div class="q dk"><small>TO YOU</small><b>4 renewals in 30 days</b><span>Each with the client's contact and a call reminder.</span></div></div>''',
"#14284b", "Insurance agency? DM us", "background:#14284b;color:#ffd23f")

# ───────── 89 INDIA · Imitation jewellery seller · SINGLE · Cardo + Montserrat · velvet teal / rose gold / blush
# New technique: velvet display tray with inline SVG jewellery (bead necklace arc, drop earrings, bangles).
neck = "".join(f'<circle cx="{150+130*__import__("math").cos(__import__("math").radians(a)):.1f}" cy="{30+120*__import__("math").sin(__import__("math").radians(a)):.1f}" r="{9 if a%20 else 12}" fill="{"#e8b4a0" if a%20 else "#f6e2b0"}" stroke="#a5644e" stroke-width="2"/>' for a in range(10, 171, 10))
svgj = f'''<svg viewBox="0 0 300 200" width="330" height="220" style="display:block">{neck}<path d="M150 150 l-18 26 h36z" fill="#f6e2b0" stroke="#a5644e" stroke-width="2"/></svg>'''
ear = '''<svg viewBox="0 0 60 120" width="66" height="132" style="display:block"><circle cx="30" cy="12" r="8" fill="#f6e2b0" stroke="#a5644e" stroke-width="2"/><path d="M30 20 V36" stroke="#a5644e" stroke-width="3"/><path d="M30 36 C8 60 8 96 30 112 C52 96 52 60 30 36z" fill="#e8b4a0" stroke="#a5644e" stroke-width="2"/><circle cx="30" cy="78" r="9" fill="#2f8f87"/></svg>'''
P["p89_jewellery"] = page("""
body{--f:'Montserrat';--h:'Cardo';background:#f8e9e4;color:#123c3a}
h1{font-family:'Cardo';font-size:64px;font-weight:700} h1 span{color:#b7654d;font-style:italic}
.sub{color:#5f6e6c}
.vis{gap:18px}
.ty{flex:1.2;background:#155450;background-image:radial-gradient(circle at 30% 20%,rgba(255,255,255,.08),transparent 60%);border-radius:30px;padding:24px;display:flex;flex-direction:column;gap:14px;box-shadow:inset 0 0 0 10px #0f403d}
.ty small{font:700 13px Montserrat;letter-spacing:3px;color:#a9d1cc;margin:6px 0 0 6px}
.slt{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1.3fr 1fr;gap:12px}
.sl{background:#0f403d;border-radius:18px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;box-shadow:inset 0 4px 10px rgba(0,0,0,.35)}
.sl.wd{grid-column:1/3}
.sl b{font:700 16px Montserrat;color:#f6e2b0;letter-spacing:1px}
.er{display:flex;gap:18px}
.bg{display:flex}.bg i{width:96px;height:96px;border-radius:50%;border:9px solid #e8b4a0;margin-left:-30px;display:block;box-shadow:inset 0 0 0 3px #a5644e,0 0 0 3px #a5644e}
.bg i:first-child{margin-left:0;border-color:#f6e2b0}
.rc{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.ord{flex:1;background:#fff;border-radius:26px;padding:20px;display:flex;flex-direction:column;gap:10px}
.ord small{font:700 13px Montserrat;letter-spacing:3px;color:#8b9a98}
.or{flex:1;border-bottom:1.5px solid #f1e2dc;display:flex;flex-direction:column;justify-content:center;gap:5px}
.or:last-child{border:none}
.or .t{display:flex;justify-content:space-between;align-items:center}
.or b{font:700 20px Montserrat}
.or em{font-style:normal;font:700 14px Montserrat;padding:5px 9px;border-radius:8px;white-space:nowrap}
.pk{background:#fde7c6;color:#8a5a00}.sh{background:#d9efec;color:#155450}.nw{background:#155450;color:#fff}
.or span{font:500 17px Montserrat;color:#5f6e6c}
.lk{background:#b7654d;color:#fff;border-radius:20px;padding:16px 18px;font:600 18px/1.4 Montserrat}
.lk b{display:block;font:700 23px Cardo}
""", "<h1>Reseller orders in 10 chats?<br><span>Give them one catalogue link.</span></h1><div class=sub>For imitation jewellery sellers: an online store for customers and a reseller order list for you.</div>",
f'''<div class=ty><small>NEW ARRIVALS · SAMPLE</small><div class=slt><div class="sl wd">{svgj}<b>N-210 · BEAD NECKLACE</b></div><div class=sl><div class=er>{ear}{ear}</div><b>E-118 · DROPS</b></div><div class=sl><div class=bg><i></i><i></i><i></i></div><b>B-305 · BANGLE SET</b></div></div></div>
<div class=rc><div class=ord><small>RESELLER ORDERS · SAMPLE</small>{"".join(f'<div class=or><div class=t><b>{r}</b><em class={k}>{s}</em></div><span>{d}</span></div>' for r,d,s,k in [("Reseller 1","N-210 x 6, E-118 x 10","New","nw"),("Reseller 2","B-305 x 4","Packing","pk"),("Reseller 3","E-118 x 12","Shipped","sh"),("Reseller 4","N-210 x 3, B-305 x 2","Shipped","sh")])}</div>
<div class=lk><b>One link for all designs</b>Resellers share your catalogue. Orders come to you in one list.</div></div>''',
"#123c3a", "Sell jewellery online? DM us", "background:#155450;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
