import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 96 INDIA · RO water purifier dealer · SINGLE · Poppins + Inter · aqua mist / ink blue / coral
# New technique: SVG cutaway RO unit with labelled filter cartridges + filter-life bars per customer.
ro = '''<svg viewBox="0 0 300 470" width="320" height="501">
<rect x="10" y="10" width="280" height="450" rx="26" fill="#ffffff" stroke="#c9dde6" stroke-width="4"/>
<rect x="10" y="10" width="280" height="70" rx="26" fill="#1c3a5e"/><rect x="10" y="50" width="280" height="30" fill="#1c3a5e"/>
<circle cx="250" cy="45" r="10" fill="#4fd1c5"/><rect x="40" y="36" width="120" height="16" rx="8" fill="#35557d"/>
<rect x="34" y="104" width="232" height="330" rx="16" fill="#eef7fa"/>
<g><rect x="54" y="140" width="46" height="250" rx="18" fill="#f2e6c9" stroke="#c9b47e" stroke-width="3"/><rect x="62" y="150" width="30" height="230" rx="12" fill="none" stroke="#c9b47e" stroke-width="2" stroke-dasharray="6 6"/></g>
<g><rect x="127" y="140" width="46" height="250" rx="18" fill="#3a3f47"/><rect x="137" y="150" width="26" height="230" rx="10" fill="#555b66"/></g>
<g><rect x="200" y="140" width="46" height="250" rx="18" fill="#bfe9f2" stroke="#6cc3d6" stroke-width="3"/><path d="M206 170 H240 M206 200 H240 M206 230 H240 M206 260 H240 M206 290 H240 M206 320 H240 M206 350 H240" stroke="#6cc3d6" stroke-width="3"/></g>
<path d="M77 140 V122 H150 V140 M150 122 H223 V140" fill="none" stroke="#7aa7c7" stroke-width="5" stroke-linejoin="round"/>
</svg>'''
due = [("Sample customer 1","Sector 14 · installed Nov 2025","Sediment","Due Tue",92,"hi"),
       ("Sample customer 2","Green Park · installed Jan 2026","Carbon","Due Thu",80,"hi"),
       ("Sample customer 3","Shop 6, Main Road · AMC","Service visit","Due Sat",70,""),
       ("Sample customer 4","Flat 2C · installed May 2025","Membrane","Next month",55,"")]
P["p96_ro"] = page("""
body{--f:'Inter';--h:'Poppins';background:#e3f3f5;color:#14263f}
h1{font-family:'Poppins';font-size:60px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#e5604d}
.sub{color:#4d6278}
.vis{gap:22px}
.uw{width:360px;flex:none;background:#c7e7ec;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;padding:20px}
.uw svg{display:block}
.lgd{display:flex;gap:8px;width:320px;justify-content:space-between}
.lgd span{flex:1;text-align:center;font:700 15px Inter;background:#fff;border-radius:8px;padding:6px 0}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.ls{flex:1;background:#fff;border-radius:26px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 14px 30px rgba(20,38,63,.07)}
.ls small,.tx small{font:700 13px Inter;letter-spacing:3px;color:#7d90a3}
.it{flex:1;border:2px solid #e6f0f3;border-radius:16px;padding:10px 14px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.it .t{display:flex;justify-content:space-between;align-items:center;gap:8px}
.it b{font:700 21px Inter}.it span{font:500 16px Inter;color:#6b7f93}
.it em{font-style:normal;font:700 15px Inter;padding:5px 10px;border-radius:8px;background:#e6f0f3;color:#14263f;white-space:nowrap}
.it.hi em{background:#e5604d;color:#fff}
.it .f{display:flex;align-items:center;gap:10px;font:600 16px Inter;color:#14263f}
.it .f i{flex:1;height:10px;border-radius:5px;background:#e6f0f3;position:relative;overflow:hidden;display:block}
.it .f u{position:absolute;left:0;top:0;bottom:0;background:#4fb3c6;border-radius:5px}
.it.hi .f u{background:#e5604d}
.tx{background:#14263f;color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;flex:none}
.tx small{color:#9fb6cc}
.tx p{font:500 19px/1.45 Inter}
""", "<h1>Customers call only when<br>the water tastes bad?<br><span>Remind them before<br>the filter is due.</span></h1><div class=sub>For RO water purifier dealers: every installation with its filter dates.</div>",
f'''<div class=uw>{ro}<div class=lgd><span>Sediment</span><span>Carbon</span><span>Membrane</span></div></div>
<div class=rc><div class=ls><small>COMING UP · SAMPLE</small>{"".join(f'<div class="it {k}"><div class=t><b>{n}</b><em>{d}</em></div><span>{a}</span><div class=f>{f}<i><u style="width:{p}%"></u></i></div></div>' for n,a,f,d,p,k in due)}</div>
<div class=tx><small>AUTO REMINDER · SAMPLE</small><p>Your RO sediment filter is due for a change on Tuesday. Reply 1 to book a visit.</p></div></div>''',
"#14263f", "RO dealer? DM us", "background:#14263f;color:#fff")

# ───────── 98 INDIA · Engineering workshop / lathe · SINGLE · Bitter + Fira Sans · hammertone green / brass yellow / drawing paper
# New technique: SVG engineering drawing of a stepped shaft with dimension lines, job card clipped on top, machine load board.
shaft = '''<svg viewBox="0 0 560 250" width="560" height="250">
<g fill="#fffdf4" stroke="#24434a" stroke-width="3"><rect x="40" y="95" width="90" height="60"/><rect x="130" y="70" width="200" height="110"/><rect x="330" y="85" width="120" height="80"/><rect x="450" y="105" width="70" height="40"/></g>
<line x1="20" y1="125" x2="540" y2="125" stroke="#24434a" stroke-width="1.5" stroke-dasharray="18 6 4 6"/>
<g stroke="#b3541e" stroke-width="2" fill="#b3541e"><line x1="40" y1="215" x2="520" y2="215"/><polygon points="40,215 52,209 52,221"/><polygon points="520,215 508,209 508,221"/>
<line x1="40" y1="160" x2="40" y2="228" stroke-width="1.5"/><line x1="520" y1="150" x2="520" y2="228" stroke-width="1.5"/>
<line x1="130" y1="40" x2="330" y2="40"/><polygon points="130,40 142,34 142,46"/><polygon points="330,40 318,34 318,46"/>
<line x1="130" y1="66" x2="130" y2="28" stroke-width="1.5"/><line x1="330" y1="66" x2="330" y2="28" stroke-width="1.5"/></g>
<g font-family="Fira Sans" font-weight="700" font-size="20" fill="#b3541e" text-anchor="middle"><text x="280" y="242">480</text><text x="230" y="30">200</text></g>
<g font-family="Fira Sans" font-weight="600" font-size="18" fill="#24434a"><text x="230" y="110" text-anchor="middle">Ø 110</text><text x="390" y="112" text-anchor="middle">Ø 80</text></g>
</svg>'''
mach = [("Lathe 1","J-314 · Pins x 200","Free at 4 pm","bz"),("Lathe 2","J-318 · Shaft x 40","Free tomorrow","bz"),("CNC 1","J-320 · Flange x 60","Free Wed","bz"),("Milling","No job","Free now","fr")]
P["p98_lathe"] = page("""
body{--f:'Fira Sans';--h:'Bitter';background:#203a35;color:#f3efe2}
h1{font-family:'Bitter';font-size:62px;font-weight:800;letter-spacing:0} h1 span{color:#e9b949}
.sub{color:#b5c7bf}
.vis{flex-direction:column;gap:16px}
.dw{flex:1;background:#f6f1df;background-image:linear-gradient(#e7dfc4 1.5px,transparent 1.5px),linear-gradient(90deg,#e7dfc4 1.5px,transparent 1.5px);background-size:32px 32px;border-radius:22px;position:relative;display:flex;align-items:center;padding:20px 24px;gap:18px;color:#24434a;overflow:hidden}
.dw svg{display:block;flex:none}
.jc{flex:1;background:#fff;border-radius:16px;padding:18px 18px 16px;box-shadow:0 14px 26px rgba(20,40,35,.18);display:flex;flex-direction:column;gap:7px;border-top:10px solid #e9b949;position:relative}
.jc small{font:700 13px 'Fira Sans';letter-spacing:3px;color:#7f8c88}
.jc b{font:800 34px/1.25 Bitter}
.jc .r{display:flex;justify-content:space-between;font:500 18px 'Fira Sans';color:#56655f;border-top:1.5px dashed #e3ddc8;padding-top:6px}
.jc .r em{font-style:normal;font-weight:700;color:#24434a}
.jc .r em.d{color:#b3541e}
.pg2{height:12px;border-radius:6px;background:#ece7d6;position:relative;overflow:hidden;margin-top:4px}.pg2 u{position:absolute;left:0;top:0;bottom:0;width:60%;background:#2f6b5d;border-radius:6px}
.mb{flex:none;background:#2b4a44;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}
.mb small{font:700 13px 'Fira Sans';letter-spacing:3px;color:#9fb5ac}
.mr{display:flex;align-items:center;gap:14px;background:#335750;border-radius:12px;padding:13px 16px}
.mr b{width:130px;font:700 26px Bitter}.mr span{flex:1;font:500 21px 'Fira Sans';color:#d9e3de}
.mr em{font-style:normal;font:700 18px 'Fira Sans';padding:6px 12px;border-radius:8px;white-space:nowrap}
.bz{background:#203a35;color:#e9b949}.fr{background:#e9b949;color:#203a35}
""", "<h1>“When will my job<br>be ready?”<br><span>Every job card, with<br>its delivery date.</span></h1><div class=sub>For lathe, CNC and engineering workshops: jobs, machines and dates in one place.</div>",
f'''<div class=dw>{shaft}<div class=jc><small>JOB CARD · SAMPLE</small><b>J-318 · Shaft</b>
{"".join(f'<div class=r><span>{a}</span><em class="{c}">{b}</em></div>' for a,b,c in [("Party","Sample party B",""),("Material","EN8 steel",""),("Machine","Lathe 2",""),("Delivery","28 Nov","d")])}
<div class=r><span>Done</span><em>24 of 40</em></div><div class=pg2><u></u></div></div></div>
<div class=mb><small>MACHINE LOAD · SAMPLE</small>{"".join(f'<div class=mr><b>{a}</b><span>{b}</span><em class={k}>{c}</em></div>' for a,b,c,k in mach)}</div>''',
"#f3efe2", "Run a workshop? DM us", "background:#e9b949;color:#203a35")

# ───────── 100 CANADA · Farmers market vendor · SINGLE · Cardo + Source Sans 3 · kraft brown / beet purple / leaf green
# New technique: SVG striped market awning over produce crates, next to a pre-order page with reserved-count bars.
crates = '''<svg viewBox="0 0 400 450" width="400" height="450">
<line x1="140" y1="0" x2="120" y2="30" stroke="#5a4630" stroke-width="3"/><line x1="260" y1="0" x2="280" y2="30" stroke="#5a4630" stroke-width="3"/>
<rect x="70" y="28" width="260" height="84" rx="10" fill="#33402f" stroke="#8a6a45" stroke-width="8"/>
<text x="200" y="64" text-anchor="middle" font-family="Cardo" font-weight="700" font-size="26" fill="#f4ead8">Pre-ordered?</text>
<text x="200" y="96" text-anchor="middle" font-family="Source Sans 3" font-weight="600" font-size="20" fill="#d8c7a5">Pick up here</text>
<g transform="translate(0,120)">
<path d="M10 20 H390 V80 H10 Z" fill="#7a2f5a"/>{stripes}
<path d="M10 80 {scal} V80 Z" fill="#7a2f5a"/>
<rect x="24" y="80" width="8" height="240" fill="#8a6a45"/><rect x="368" y="80" width="8" height="240" fill="#8a6a45"/>
<g>{fruit}</g>
<rect x="40" y="210" width="150" height="100" rx="6" fill="#c89b62" stroke="#9c7442" stroke-width="3"/><rect x="210" y="210" width="150" height="100" rx="6" fill="#c89b62" stroke="#9c7442" stroke-width="3"/>
<path d="M40 245 H190 M40 280 H190 M210 245 H360 M210 280 H360" stroke="#9c7442" stroke-width="3"/>
</g></svg>'''
stripes = "".join(f'<rect x="{10+i*76}" y="20" width="38" height="60" fill="#f4ead8"/>' for i in range(5))
scal = " ".join(f"Q{29+i*38} 110 {48+i*38} 80" for i in range(10))
fruit = ("".join(f'<circle cx="{x}" cy="{y}" r="17" fill="#c8323a"/><path d="M{x} {y-17} v-7" stroke="#4d3a20" stroke-width="3"/>' for x,y in [(66,196),(100,192),(134,196),(168,196),(84,172),(118,170),(152,172)])
  + "".join(f'<ellipse cx="{x}" cy="{y}" rx="30" ry="20" fill="#e39a3b"/><ellipse cx="{x-14}" cy="{y}" rx="12" ry="14" fill="#efb35a"/>' for x,y in [(246,190),(310,190),(278,166)]))
crates = crates.replace("{stripes}", stripes).replace("{scal}", scal).replace("{fruit}", fruit)
items = [("Apples, 3 lb bag",32,40),("Butternut squash",18,25),("Potatoes, 5 lb bag",21,30),("Farm eggs, dozen",36,36),("Honey jar",9,20)]
P["p100_market"] = page("""
body{--f:'Source Sans 3';--h:'Cardo';background:#efe4d0;color:#2e2219}
h1{font-family:'Cardo';font-size:66px;font-weight:700;letter-spacing:-.5px} h1 span{color:#7a2f5a}
.sub{color:#6c5a49}
.vis{gap:20px}
.stl{width:420px;flex:none;display:flex;flex-direction:column;gap:14px}
.aw{flex:1;background:#d8c7a5;border-radius:28px;display:flex;align-items:flex-end;justify-content:center;padding:16px 10px 20px}
.aw svg{display:block}
.nt{background:#2e2219;color:#efe4d0;border-radius:20px;padding:16px 20px;display:flex;flex-direction:column;gap:4px;flex:none}
.nt small{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#c7b396}
.nt b{font:700 28px/1.3 Cardo}
.po{flex:1;display:flex;flex-direction:column;padding:18px 22px;gap:8px;background:#fffdf8}
.po h3{font:700 32px/1.25 Cardo}
.po .lb{font:700 13px 'Source Sans 3';letter-spacing:3px;color:#8d7c69}
.po .pk{display:flex;gap:8px}
.po .pk em{font-style:normal;font:700 16px 'Source Sans 3';padding:7px 12px;border-radius:10px;background:#f1e9dc}
.po .pk em.on{background:#3f7a3a;color:#fff}
.ir{flex:1;display:flex;flex-direction:column;justify-content:center;gap:7px;border-top:1.5px solid #f0e8da}
.ir .t{display:flex;justify-content:space-between;align-items:center}
.ir b{font:700 22px 'Source Sans 3'}
.ir .st{display:flex;align-items:center;gap:8px}
.ir .st span{width:34px;height:34px;border-radius:10px;border:2px solid #d8c7a5;font:700 20px/30px 'Source Sans 3';text-align:center}
.ir .st i{font:700 20px 'Source Sans 3';font-style:normal;width:22px;text-align:center}
.ir .br{display:flex;align-items:center;gap:10px;font:600 16px 'Source Sans 3';color:#6c5a49}
.ir .br u{flex:1;height:9px;border-radius:5px;background:#f1e9dc;position:relative;overflow:hidden;display:block}
.ir .br u s{position:absolute;left:0;top:0;bottom:0;background:#7a2f5a;border-radius:5px}
.ir.so b{color:#a5978a}.ir.so .br{color:#7a2f5a;font-weight:700}
.bt{background:#7a2f5a;color:#fff;border-radius:14px;text-align:center;font:700 20px 'Source Sans 3';padding:13px}
""", "<h1>Sold out by 10 am,<br>or stuck with extra?<br><span>Take pre-orders before<br>market day.</span></h1><div class=sub>For farmers market vendors: a pre-order page with pickup at your stall.</div>",
f'''<div class=stl><div class=aw>{crates}</div><div class=nt><small>PRE-ORDERS · SAMPLE</small><b>Close Friday 6 pm.<br>You pack only what's ordered.</b></div></div>
{browser(f"""<div class=po><span class=lb>YOUR FARM · SAMPLE</span><h3>Saturday winter market</h3><div class=pk><em class=on>Pick up 8 to 10</em><em>10 to 12</em><em>Stall 14</em></div>
{"".join(f'<div class="ir {"so" if r==m else ""}"><div class=t><b>{n}</b><div class=st><span>–</span><i>{0 if r==m else 1}</i><span>+</span></div></div><div class=br><u><s style="width:{round(r*100/m)}%"></s></u>{"Sold out" if r==m else f"{r} of {m} reserved"}</div></div>' for n,r,m in items)}
<div class=bt>Reserve for pickup</div></div>""", "preorder.yourfarm.ca · sample", "flex:1")}''',
"#2e2219", "Sell at a market? DM us", "background:#3f7a3a;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
