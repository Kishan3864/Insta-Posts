import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 71 INDIA · Interior designer · SINGLE · Gelasio + DM Sans · charcoal green / oat / brass
# New technique: CSS material swatch board (wood grain, terrazzo, linen weave, brushed brass, marble veins).
SW = {
 "oak": "background:repeating-linear-gradient(100deg,#c8955c 0 6px,#b98249 6px 9px,#d3a26a 9px 17px,#b07a42 17px 19px)",
 "sage": "background:#a7b59a",
 "terr": "background:radial-gradient(circle at 20% 30%,#d9774e 0 7px,transparent 8px),radial-gradient(circle at 70% 60%,#5f7a63 0 6px,transparent 7px),radial-gradient(circle at 40% 80%,#e9c46a 0 5px,transparent 6px),radial-gradient(circle at 85% 20%,#8d6a52 0 6px,transparent 7px),radial-gradient(circle at 15% 75%,#5f7a63 0 4px,transparent 5px) ,#f1ece2;background-size:70px 70px",
 "linen": "background:repeating-linear-gradient(0deg,rgba(0,0,0,.05) 0 2px,transparent 2px 5px),repeating-linear-gradient(90deg,rgba(0,0,0,.05) 0 2px,transparent 2px 5px),#e6dccb",
 "brass": "background:linear-gradient(90deg,#9c7330,#d9b46a 30%,#b8893b 55%,#e4c27f 75%,#a37a36)",
 "marb": "background:linear-gradient(125deg,transparent 0 30%,#b8b4ac 31%,transparent 33% 60%,#c9c5bd 61%,transparent 62%),linear-gradient(40deg,transparent 0 55%,#cfcac1 56%,transparent 57%),#f4f2ee",
}
items = [("oak","Wardrobe shutter","Light oak laminate","ok"),("sage","Living room wall","Sage green paint","ok"),
         ("terr","Kitchen floor","Terrazzo tile","ch"),("linen","Sofa fabric","Natural linen","ok"),
         ("brass","Handles","Brushed brass","wt"),("marb","Counter top","White marble look","ok")]
ST = {"ok":("Approved","#dfeadf","#2c5a36"),"ch":("Change asked","#f7e2d3","#a24e1c"),"wt":("Waiting","#ece6d8","#6f6656")}
tiles = "".join(f'<div class=mt><i style="{SW[s]}"></i><b>{a}</b><span>{b}</span><em style="background:{ST[k][1]};color:{ST[k][2]}">{ST[k][0]}</em></div>' for s,a,b,k in items)
P["p71_interior"] = page("""
body{--f:'DM Sans';--h:'Gelasio';background:#efe7da;color:#24342c}
h1{font-family:'Gelasio';font-size:60px;font-weight:700;letter-spacing:-.5px} h1 span{color:#9a6f28;font-style:italic}
.sub{color:#5c6a61}
.vis{gap:18px}
.bd{flex:1.55;background:#24342c;border-radius:30px;padding:22px;display:flex;flex-direction:column;gap:14px}
.bd .hd{display:flex;justify-content:space-between;align-items:center;color:#efe7da}
.bd .hd b{font:700 26px Gelasio}.bd .hd small{font:700 13px 'DM Sans';letter-spacing:3px;color:#a9b5ad}
.mg{flex:1;display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px}
.mt{background:#f8f4ec;border-radius:18px;padding:10px 10px 14px;display:flex;flex-direction:column;gap:4px}
.mt i{display:block;flex:1;min-height:90px;border-radius:12px;margin-bottom:8px}
.mt b{font:700 18px 'DM Sans'}.mt span{font:500 16px 'DM Sans';color:#5c6a61}
.mt em{align-self:flex-start;margin-top:6px;font-style:normal;font:700 14px 'DM Sans';padding:5px 10px;border-radius:8px}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.cmt{flex:1;background:#fff;border-radius:26px;padding:22px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}
.cmt small{font:700 13px 'DM Sans';letter-spacing:3px;color:#8a948d}
.bb{border-radius:18px;padding:14px 16px;font:500 21px/1.4 'DM Sans'}
.bb b{display:block;font:700 15px 'DM Sans';letter-spacing:1px;margin-bottom:4px}
.b1{background:#f7e2d3;color:#5b2c10;border-bottom-left-radius:4px}
.b2{background:#24342c;color:#efe7da;border-bottom-right-radius:4px;margin-left:24px}
.b2 b{color:#d9b46a}
.opt{display:flex;gap:10px}.opt div{flex:1;display:flex;align-items:center;gap:10px;border:2px solid #e4ddd0;border-radius:14px;padding:8px;font:700 17px 'DM Sans'}
.opt div.on{border-color:#b8893b;background:#fbf4e6}.opt i{width:44px;height:44px;border-radius:9px;display:block;flex:none;border:1px solid #e4ddd0}
.apv{background:#b8893b;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 18px 'DM Sans'}
.cnt{background:#e4d6bd;color:#24342c;border-radius:26px;padding:20px 22px;display:flex;justify-content:space-between}
.cnt div{text-align:center}.cnt b{display:block;font:700 42px/1.3 Gelasio}.cnt span{font:600 15px 'DM Sans'}
""", "<h1>Client approvals lost in chat?<br><span>Put every choice<br>on one board.</span></h1><div class=sub>For interior designers: clients approve each material on one link.</div>",
f'''<div class=bd><div class=hd><b>2BHK · Living + kitchen</b><small>SAMPLE PROJECT</small></div><div class=mg>{tiles}</div></div>
<div class=rc><div class=cmt><small>ON KITCHEN FLOOR</small>
<div class="bb b1"><b>CLIENT</b>Can we see a lighter tile? This looks busy.</div>
<div class="bb b2"><b>YOU</b>Added two lighter options. Pick one and tap Approve.</div>
<div class=opt><div><i style="background:radial-gradient(circle at 30% 40%,#c9b8a6 0 4px,transparent 5px),radial-gradient(circle at 70% 70%,#a7b59a 0 4px,transparent 5px),#f6f2ea;background-size:34px 34px"></i>Option 1</div><div class=on><i style="background:radial-gradient(circle at 30% 40%,#e3d3bd 0 4px,transparent 5px),#fbf8f2;background-size:30px 30px"></i>Option 2</div></div>
<div class="bb b1"><b>CLIENT</b>Option 2 looks good. Approving it now.</div><div class=apv>Approve option 2</div></div>
<div class=cnt><div><b>4</b><span>Approved</span></div><div><b>1</b><span>Change</span></div><div><b>1</b><span>Waiting</span></div></div></div>''',
"#24342c", "Interior designer? DM us", "background:#24342c;color:#efe7da")

# ───────── 73 INDIA · Gents tailor · SINGLE · Bitter + Inter · chalk white / charcoal / mustard  (phone post)
# New technique: CSS measuring tape band with tick marks and inch numbers across the slide.
nums = "".join(f'<span>{n}</span>' for n in range(10, 25))
meas = [("SHIRT", [("Neck","15.5 in"),("Chest","40 in"),("Shoulder","18 in"),("Sleeve","25 in"),("Length","30 in")]),
        ("TROUSER", [("Waist","34 in"),("Hip","40 in"),("Length","41 in")])]
mrows = "".join(f'<div class=sec>{t}</div>' + "".join(f'<div class=mr><span>{a}</span><b>{b}</b></div>' for a,b in r) for t,r in meas)
dl = [("Mon","2 shirts","Message sent","Ready","rd"),("Tue","Suit · trial","Trial at 5 pm","Trial today","tr"),("Thu","3 kurtas","Due by 7 pm","Stitching","st"),("Sat","Safari suit","Navy cotton","Cutting","st")]
P["p73_tailor"] = page("""
body{--f:'Inter';--h:'Bitter';background:#2b2d31;color:#f4f1ea}
h1{font-family:'Bitter';font-size:64px;font-weight:800;letter-spacing:-1px} h1 span{color:#f0b429}
.sub{color:#b9b6ae}
.vis{flex-direction:column;gap:22px}
.tp{flex:none;height:78px;border-radius:8px;background:#f0b429;position:relative;overflow:hidden;box-shadow:0 14px 30px rgba(0,0,0,.3)}
.tp:before{content:"";position:absolute;left:0;right:0;top:0;height:22px;background:repeating-linear-gradient(90deg,#2b2d31 0 2px,transparent 2px 15.5px)}
.tp:after{content:"";position:absolute;left:0;right:0;top:0;height:34px;background:repeating-linear-gradient(90deg,#2b2d31 0 3px,transparent 3px 62px)}
.tp .nn{position:absolute;left:0;right:0;bottom:8px;display:flex}
.tp .nn span{width:62px;flex:none;font:700 22px Inter;color:#2b2d31;padding-left:4px}
.rw{flex:1;display:flex;gap:26px;min-height:0}
.ph1{display:flex;align-items:center}
.ap{flex:1;padding:6px 20px 18px;display:flex;flex-direction:column;gap:6px;color:#2b2d31;background:#faf8f3}
.ap .nm{display:flex;align-items:center;gap:12px;margin:6px 0 8px}
.ap .nm i{width:48px;height:48px;border-radius:50%;background:#f0b429;display:flex;align-items:center;justify-content:center;font:800 20px Bitter;font-style:normal}
.ap .nm b{font:800 21px Bitter;display:block}.ap .nm small{font:500 14px Inter;color:#7a776f}
.sec{font:700 13px Inter;letter-spacing:3px;color:#9a8a5a;margin-top:8px}
.mr{display:flex;justify-content:space-between;background:#fff;border:1.5px solid #ebe5d6;border-radius:12px;padding:8px 14px;font:500 18px Inter}
.mr b{font:800 18px Inter}
.ap .bt{margin-top:auto;background:#2b2d31;color:#f0b429;border-radius:14px;padding:14px;text-align:center;font:700 17px Inter}
.dv{flex:1;background:#f4f1ea;color:#2b2d31;border-radius:30px;padding:24px;display:flex;flex-direction:column;gap:12px;min-width:0}
.dv small{font:700 13px Inter;letter-spacing:3px;color:#8a867c}
.dv h4{font:800 30px Bitter}
.dr{flex:1;display:flex;align-items:center;gap:14px;background:#fff;border-radius:18px;padding:0 16px}
.dr b{font:800 23px Bitter;width:52px;flex:none}
.dr span{flex:1;font:600 23px Inter}.dr span small{display:block;font:500 17px Inter;letter-spacing:0;color:#7a776f;margin-top:3px}
.dr em{font-style:normal;font:700 15px Inter;padding:6px 10px;border-radius:9px;white-space:nowrap}
.rd{background:#dff1e2;color:#22693a}.tr{background:#fdecc4;color:#8a5a00}.st{background:#e9e6df;color:#5b574f}
.nt{background:#2b2d31;color:#f4f1ea;border-radius:16px;padding:14px 16px;font:500 18px/1.4 Inter}
.nt b{color:#f0b429}
""", "<h1>Measurements in an old register?<br><span>Save them once. Use every time.</span></h1><div class=sub>For gents tailors: every customer's sizes and delivery dates in one app.</div>",
f'''<div class=tp><div class=nn>{nums}</div></div>
<div class=rw><div class=ph1>{phone(f"""<div class=ap><div class=nm><i>RK</i><div><b>Sample customer</b><small>Last order: 2 shirts</small></div></div>{mrows}<div class=bt>New order with these sizes</div></div>""", 350, 660)}</div>
<div class=dv><small>THIS WEEK · SAMPLE</small><h4>Delivery dates</h4>{"".join(f'<div class=dr><b>{d}</b><span>{w}<small>{x}</small></span><em class={c}>{s}</em></div>' for d,w,x,s,c in dl)}
<div class=nt><b>Ready?</b> The customer gets a message to come and collect.</div></div></div>''',
"#f4f1ea", "Run a tailoring shop? DM us", "background:#f0b429;color:#2b2d31")

# ───────── 75 INDIA · Plywood and laminate dealer · SINGLE · Archivo Black + Source Sans 3 · birch / walnut / signal green
# New technique: side-view sheet stacks (layered edge stripes) with a dashed low-stock level line.
stacks = [("6 mm","MR ply",170,"#e2c597",""),("12 mm","MR ply",70,"#d8b47c","lo"),("18 mm","BWP ply",370,"#cfa56a",""),("1 mm","Laminate",260,"#8a5a3b","")]
st_html = "".join(f'<div class=sk><div class="sh {lo}" style="height:{h}px;--c:{c}"></div><b>{a}</b><span>{b}</span></div>' for a,b,h,c,lo in stacks)
P["p75_plywood"] = page("""
body{--f:'Source Sans 3';--h:'Archivo Black';background:#f3ece0;color:#3a2618}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.25;margin-top:30px} h1 span{color:#1f8a4c}
.sub{color:#6e5a49;font-size:25px}
.vis{flex-direction:column;gap:18px}
.yd{flex:1;background:#fffaf2;border-radius:30px;padding:22px 30px 18px;display:flex;flex-direction:column;position:relative;box-shadow:0 18px 40px rgba(58,38,24,.08)}
.yd small{font:700 15px 'Source Sans 3';letter-spacing:3px;color:#9b8670}
.yr{flex:1;display:flex;align-items:flex-end;justify-content:space-around;position:relative;border-bottom:6px solid #3a2618;padding-bottom:0}
.lv{position:absolute;left:0;right:0;bottom:60px;height:40px;border-top:3px dashed #d0412f}
.yh{display:flex;justify-content:space-between;align-items:center}.yh em{font-style:normal;font:700 16px 'Source Sans 3';color:#d0412f;display:flex;align-items:center;gap:8px}.yh em i{width:36px;border-top:3px dashed #d0412f;display:block}
.xlv em{position:absolute;right:0;top:4px;font-style:normal;font:700 16px 'Source Sans 3';color:#d0412f;background:#fffaf2;padding:2px 6px}
.sk{display:flex;flex-direction:column;align-items:center;width:170px;position:relative}
.sh{width:170px;border-radius:4px 4px 0 0;background:repeating-linear-gradient(0deg,var(--c) 0 9px,#7a5636 9px 10px);box-shadow:inset -10px 0 0 rgba(0,0,0,.08)}
.sh.lo{outline:4px solid #d0412f;outline-offset:3px}
.sk b{position:absolute;bottom:-56px;font:400 22px 'Archivo Black';white-space:nowrap}
.sk span{position:absolute;bottom:-80px;font:600 17px 'Source Sans 3';color:#6e5a49;white-space:nowrap}
.yd .gap{height:84px;flex:none}
.cr{display:flex;gap:16px;flex:none}
.sc{flex:1.25;background:#3a2618;color:#f3ece0;border-radius:26px;padding:20px 22px;display:flex;flex-direction:column;gap:10px}
.sc .q{display:flex;align-items:center;gap:10px;background:#f3ece0;color:#3a2618;border-radius:14px;padding:11px 14px;font:700 20px 'Source Sans 3'}
.sc .r{display:flex;justify-content:space-between;font:600 20px 'Source Sans 3';padding:2px 4px}
.sc .r b{font:400 20px 'Archivo Black'}
.sc .tt{border-top:1.5px solid #6b4f3a;padding-top:10px}.sc .tt b{color:#5fd391}
.al{flex:1;background:#d0412f;color:#fff;border-radius:26px;padding:20px 22px;display:flex;flex-direction:column;gap:8px}
.al small{font:700 14px 'Source Sans 3';letter-spacing:3px;opacity:.85}
.al .ab{margin-top:auto;background:#fff;color:#d0412f;border-radius:12px;padding:11px;text-align:center;font:700 18px 'Source Sans 3'}
.al b{font:400 26px/1.3 'Archivo Black'}.al span{font:600 19px/1.4 'Source Sans 3'}
""", "<h1>“Is 18 mm BWP in stock?”<br><span>Answer without going<br>to the godown.</span></h1><div class=sub>For plywood and laminate dealers: sheet stock by size, grade and godown.</div>",
f'''<div class=yd><div class=yh><small>STOCK BY THICKNESS · SAMPLE</small><em><i></i>Reorder level</em></div><div class=yr><div class=lv></div>{st_html}</div><div class=gap></div></div>
<div class=cr><div class=sc><div class=q>{ic("search",22)}18 mm · BWP · 8 x 4 ft</div>
<div class=r><span>Godown 1</span><b>42 sheets</b></div><div class=r><span>Godown 2</span><b>15 sheets</b></div><div class=r><span>Kept for orders</span><b>10 sheets</b></div>
<div class="r tt"><span>Free to sell</span><b>47 sheets</b></div></div>
<div class=al><small>LOW STOCK</small><b>12 mm MR ply</b><span>Below your reorder level. Add it to the next supplier order.</span><div class=ab>+ Add to supplier order</div></div></div>''',
"#3a2618", "Plywood dealer? DM us", "background:#1f8a4c;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
