import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 77 INDIA · Footwear shop · SINGLE · Poppins + Fira Sans · cobalt / tomato / sneaker white
# New technique: CSS shoe-box wall (stacked boxes with lids and size labels, empty slots for sold-out sizes).
sizes = [6,7,8,9,10,11]
designs = [("SN-118","#2a52be",10),("SN-121","#e4572e",8),("SN-124","#f2c14e",7)]
boxes = "".join((f'<div class=bx style="--c:{c}"><i></i><b>{z}</b><span>{d}</span></div>' if z!=out else f'<div class="bx em"><b>{z}</b><span>Sold out</span></div>') for z in sizes for d,c,out in designs)
P["p77_footwear"] = page("""
body{--f:'Fira Sans';--h:'Poppins';background:#f6f4ef;color:#14213d}
h1{font-family:'Poppins';font-size:58px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#2a52be}
.sub{color:#5a6378}
.vis{gap:18px}
.sh{flex:1.2;background:#d9c7a7;border-radius:30px;padding:20px;display:flex;flex-direction:column;gap:12px;box-shadow:inset 0 -14px 0 #c4ae8a}
.sh small{font:700 14px 'Fira Sans';letter-spacing:3px;color:#6b5636}
.bw{flex:1;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(6,1fr);gap:12px 10px}
.bx{background:var(--c);border-radius:6px;position:relative;display:flex;align-items:center;gap:10px;padding:0 12px 0 14px;box-shadow:0 6px 0 rgba(0,0,0,.18)}
.bx i{position:absolute;left:0;top:0;bottom:0;width:8px;background:rgba(0,0,0,.16);border-radius:6px 6px 0 0;display:block}
.bx b{background:#fff;color:#14213d;font:800 22px Poppins;width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}
.bx span{font:700 15px 'Fira Sans';color:rgba(255,255,255,.92);letter-spacing:1px}
.bx.em{background:#efe4d0;box-shadow:inset 0 0 0 3px #e4572e;border:none}
.bx.em b{background:none;color:#e4572e;box-shadow:inset 0 0 0 3px #e4572e}
.bx.em span{font:700 16px 'Fira Sans';color:#e4572e}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.sc{flex:1;background:#fff;border-radius:28px;padding:22px;display:flex;flex-direction:column;gap:10px;box-shadow:0 16px 36px rgba(20,33,61,.08)}
.sc small{font:700 14px 'Fira Sans';letter-spacing:3px;color:#8b93a6}
.sc h4{font:800 26px/1.3 Poppins}
.sz{flex:1;display:flex;flex-direction:column;gap:7px}
.sz div{flex:1;display:flex;align-items:center;gap:12px;font:600 20px 'Fira Sans'}
.sz div b{width:40px;font:800 20px Poppins}
.sz div i{flex:1;height:14px;border-radius:7px;background:#eceef3;display:block;position:relative;overflow:hidden}
.sz div i em{position:absolute;left:0;top:0;bottom:0;background:#2a52be;border-radius:7px}
.sz div span{width:92px;text-align:right;white-space:nowrap}
.sz div.out span{color:#e4572e;font-weight:700}
.al{background:#14213d;color:#fff;border-radius:24px;padding:18px 20px;font:500 19px/1.4 'Fira Sans'}
.al b{color:#f2c14e;display:block;font:700 22px Poppins;margin-bottom:4px}
""", "<h1>“Do you have this in size 9?”<br><span>Know before you climb<br>the ladder.</span></h1><div class=sub>For footwear shops: stock for every design, size by size.</div>",
f'''<div class=sh><small>SHELF VIEW · SAMPLE</small><div class=bw>{boxes}</div></div>
<div class=rc><div class=sc><small>DESIGN SN-118 · SAMPLE</small><h4>Running shoe, navy</h4><div class=sz>{"".join(f'<div class="{"out" if q==0 else ""}"><b>{s}</b><i><em style="width:{q*12}%"></em></i><span>{"Sold out" if q==0 else str(q)+" pairs"}</span></div>' for s,q in [(6,3),(7,5),(8,6),(9,2),(10,0),(11,4)])}</div></div>
<div class=al><b>Size 10 sold out</b>Customers can ask to be told when it is back.</div></div>''',
"#14213d", "Run a footwear shop? DM us", "background:#2a52be;color:#fff")

# ───────── 78 USA · Handyman · SINGLE · Crimson Text + DM Sans · pegboard tan / deep green / tomato  (phone post)
# New technique: pegboard background (radial-gradient holes) with CSS tool silhouettes.
jobs = [("Hang TV or shelves",1),("Fix a door or lock",0),("Patch drywall",1),("Assemble furniture",0),("Replace a faucet",1)]
P["p78_handyman"] = page("""
body{--f:'DM Sans';--h:'Crimson Text';background:#efe4d2;color:#1d3b2f}
h1{font-family:'Crimson Text';font-size:66px;font-weight:700;letter-spacing:-.5px;line-height:1.2} h1 span{color:#d9472f}
.sub{color:#5b6a60}
.vis{gap:22px}
.pb{flex:1;background:#d4b183;background-image:radial-gradient(circle,#8a6a40 5px,transparent 6px);background-size:44px 44px;background-position:22px 22px;border-radius:30px;position:relative;display:flex;align-items:center;justify-content:center;padding:26px}
.tl{position:absolute;display:block}
.hm1{left:46px;top:40px;width:22px;height:200px;background:#6b4a2b;border-radius:6px}
.hm2{left:20px;top:40px;width:76px;height:34px;background:#3a3f44;border-radius:6px}
.wr1{left:130px;top:40px;width:24px;height:190px;background:#9aa3ab;border-radius:12px}
.wr2{left:116px;top:30px;width:52px;height:52px;border-radius:50%;background:#9aa3ab;box-shadow:inset 0 0 0 13px #9aa3ab}
.wr3{left:131px;top:30px;width:22px;height:26px;background:#d4b183}
.sd1{left:210px;top:40px;width:30px;height:90px;background:#d9472f;border-radius:10px}
.sd2{left:220px;top:130px;width:10px;height:110px;background:#9aa3ab;border-radius:0 0 4px 4px}
.ph2{position:relative;z-index:2;margin-left:240px}
.ap{flex:1;padding:8px 18px 18px;display:flex;flex-direction:column;gap:8px;background:#fbf7f0}
.ap h5{font:700 24px 'Crimson Text';color:#1d3b2f;margin:4px 0 2px}
.ap small{font:700 12px 'DM Sans';letter-spacing:2px;color:#8a8f86}
.jb{display:flex;align-items:center;gap:10px;background:#fff;border:2px solid #e6ddcc;border-radius:12px;padding:9px 12px;font:600 16px 'DM Sans';color:#1d3b2f}
.jb i{width:22px;height:22px;border-radius:6px;border:2px solid #b9b2a4;display:block;flex:none}
.jb.on{border-color:#1d3b2f}.jb.on i{background:#1d3b2f;border-color:#1d3b2f}
.pr{display:flex;gap:6px}.pr i{flex:1;height:52px;border-radius:10px;display:block;background:linear-gradient(150deg,#d8cdb8 0 55%,#c6b89e 55%)}
.tw{display:flex;gap:6px}.tw span{flex:1;text-align:center;font:600 14px 'DM Sans';padding:8px 0;border-radius:10px;background:#efe8db;color:#1d3b2f}.tw span.on{background:#1d3b2f;color:#fff}
.ap .bt{margin-top:auto;background:#d9472f;color:#fff;border-radius:12px;padding:12px;text-align:center;font:700 16px 'DM Sans'}
.sd{width:330px;flex:none;display:flex;flex-direction:column;gap:14px}
.sd div{flex:1;background:#1d3b2f;color:#efe4d2;border-radius:24px;padding:20px 22px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.sd div b{font:700 30px/1.2 'Crimson Text';color:#fff}
.sd div span{font:500 19px/1.4 'DM Sans'}
.sd div.hl{background:#d9472f}
""", "<h1>“Can you fix a few small things?”<br><span>Let them list every job first.</span></h1><div class=sub>For handyman businesses: a booking page where customers list jobs, add photos and pick a time.</div>",
f'''<div class=pb><i class="tl hm1"></i><i class="tl hm2"></i><i class="tl wr1"></i><i class="tl wr2"></i><i class="tl wr3"></i><i class="tl sd1"></i><i class="tl sd2"></i>
<div class=ph2>{phone(f"""<div class=ap><h5>What needs fixing?</h5><small>PICK ALL THAT APPLY · SAMPLE</small>{"".join(f'<div class="jb {"on" if o else ""}"><i></i>{j}</div>' for j,o in jobs)}<small>PHOTOS</small><div class=pr><i></i><i></i><i></i></div><small>TIME WINDOW</small><div class=tw><span>Morning</span><span class=on>Afternoon</span><span>Evening</span></div><div class=bt>Request a visit</div></div>""", 330, 680)}</div></div>
<div class=sd><div><b>3 jobs, 1 visit</b><span>You see the full list before you drive out.</span></div><div><b>Photos first</b><span>Bring the right part the first time.</span></div><div class=hl><b>Your service area</b><span>Requests come only from ZIP codes you serve.</span></div></div>''',
"#1d3b2f", "Own a handyman business? DM us", "background:#1d3b2f;color:#fff")

# ───────── 79 INDIA · Embroidery / zari job work unit · SINGLE · Cardo + Inter · deep maroon / zari gold / ivory
# New technique: CSS embroidery hoop (wood ring + dashed-stitch motif rings) as the hero object.
jobs79 = [("E-204","Sample Boutique","Zari border, 4 m",120,80,"Due Fri"),("E-207","Sample Fabrics","Mirror work yoke",60,60,"Ready"),("E-211","Sample Designer","Sequin buti",200,45,"Due Mon")]
P["p79_embroidery"] = page("""
body{--f:'Inter';--h:'Cardo';background:#5a1428;color:#f8f1e4}
h1{font-family:'Cardo';font-size:64px;font-weight:700;letter-spacing:-.5px} h1 span{color:#e3c27a;font-style:italic}
.sub{color:#e2c9cf}
.vis{gap:20px}
.hp{width:400px;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;background:#6c1d33;border-radius:30px}
.ho{width:340px;height:340px;border-radius:50%;background:#f8f1e4;border:16px solid #b98a54;box-shadow:0 0 0 4px #8f6233,0 24px 40px rgba(0,0,0,.3);position:relative;display:flex;align-items:center;justify-content:center}
.ho .r1{width:230px;height:230px;border-radius:50%;border:5px dashed #c9a24a;display:flex;align-items:center;justify-content:center}
.ho .r2{width:150px;height:150px;border-radius:50%;border:5px dotted #5a1428;display:flex;align-items:center;justify-content:center}
.ho .r3{width:72px;height:72px;border-radius:50%;background:repeating-conic-gradient(#c9a24a 0 15deg,#f8f1e4 15deg 30deg);border:4px solid #c9a24a}
.spl{display:flex;gap:26px}.spl div{display:flex;flex-direction:column;align-items:center;gap:8px}
.spl i{display:block;width:54px;height:70px;border-radius:6px;background:linear-gradient(#8f6233 0 10px,transparent 10px calc(100% - 10px),#8f6233 calc(100% - 10px)),repeating-linear-gradient(0deg,var(--t) 0 3px,rgba(0,0,0,.18) 3px 4px)}
.spl span{font:600 16px Inter;color:#e2c9cf}
.hp p{font:600 20px/1.4 Inter;text-align:center;color:#f3dfa8;padding:0 26px}
.jl{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.jl>small{font:700 14px Inter;letter-spacing:3px;color:#e2c9cf}
.jc{flex:1;background:#f8f1e4;color:#3b0e1b;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.jc .t{display:flex;justify-content:space-between;align-items:center}
.jc .t b{font:700 36px Cardo}
.jc .t em{font-style:normal;font:700 18px Inter;padding:5px 10px;border-radius:8px;background:#f1e2bd;color:#7a5a12}
.jc .t em.rd{background:#dcefe0;color:#22693a}
.jc span{font:500 21px Inter;color:#6d4b55}
.jc .br{display:flex;align-items:center;gap:12px;font:700 20px Inter;margin-top:4px}
.jc .br i{flex:1;height:16px;border-radius:8px;background:#ead9da;display:block;position:relative;overflow:hidden}
.jc .br i u{position:absolute;left:0;top:0;bottom:0;background:#c9a24a;border-radius:6px}
""", "<h1>Which design is at which stage?<br><span>Track every job, piece by piece.</span></h1><div class=sub>For embroidery and zari job work units: designs, pieces done and due dates in one place.</div>",
f'''<div class=hp><div class=ho><div class=r1><div class=r2><div class=r3></div></div></div></div><p>Each design gets its own job card.</p><div class=spl>{"".join(f'<div><i style="--t:{c}"></i><span>{n}</span></div>' for c,n in [("#c9a24a","Zari"),("#c0c4cc","Silver"),("#b8324f","Resham")])}</div></div>
<div class=jl><small>JOB WORK THIS WEEK · SAMPLE</small>{"".join(f'<div class=jc><div class=t><b>{c}</b><em class="{"rd" if d==t else ""}">{s}</em></div><span>{p} · {w}</span><div class=br><i><u style="width:{round(d*100/t)}%"></u></i>{d} of {t} pieces</div></div>' for c,p,w,t,d,s in jobs79)}</div>''',
"#f8f1e4", "Run an embroidery unit? DM us", "background:#e3c27a;color:#3b0e1b")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
