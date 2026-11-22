import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 61 INDIA · Tyre shop · SINGLE · Inter Display + Source Sans 3 · rubber black / signal red / cool grey
# New technique: side-view tyre stack (rounded blocks with repeating tread stripes) with chalk size labels.
tyres = [("195/55 R16", 6), ("185/65 R15", 8), ("175/70 R14", 3), ("165/80 R14", 5)]
P["p61_tyre"] = page("""
body{--f:'Source Sans 3';--h:'Inter Display';background:#e9ecef;color:#141619}
h1{font-family:'Inter Display';font-size:66px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#e3262f}
.sub{color:#555c64}
.vis{gap:20px}
.st{flex:.9;background:#141619;border-radius:30px;padding:24px 26px;display:flex;flex-direction:column;gap:14px}
.st small{font:700 15px 'Source Sans 3';letter-spacing:3px;color:#9aa3ad}
.ty{flex:1;border-radius:34px;background:repeating-linear-gradient(90deg,#2a2d31 0 14px,#1d1f22 14px 22px);border:5px solid #34383d;display:flex;align-items:center;justify-content:space-between;padding:0 22px;position:relative}
.ty b{font:800 28px 'Inter Display';color:#f2f4f6;background:#141619;padding:6px 12px;border-radius:10px}
.ty em{font-style:normal;font:700 18px 'Source Sans 3';color:#141619;background:#ffd23f;padding:6px 12px;border-radius:10px}
.ty.hit{border-color:#e3262f;box-shadow:0 0 0 4px rgba(227,38,47,.35)}
.rt{flex:1.1;display:flex;flex-direction:column;gap:16px;min-width:0}
.sc{flex:1;background:#fff;border-radius:28px;padding:24px;display:flex;flex-direction:column;gap:12px}
.sb{display:flex;align-items:center;gap:12px;border:3px solid #141619;border-radius:16px;padding:12px 16px;font:800 28px 'Inter Display'}
.sb svg{color:#e3262f}
.sc small,.al small{font:700 14px 'Source Sans 3';letter-spacing:3px;color:#8a929b}
.rr{flex:1;display:flex;align-items:center;justify-content:space-between;background:#f3f5f7;border-radius:16px;padding:0 18px}
.rr b{display:block;font:700 22px 'Source Sans 3'}.rr span{font:500 18px 'Source Sans 3';color:#555c64}
.rr em{font-style:normal;font:700 17px 'Source Sans 3';padding:6px 12px;border-radius:10px;white-space:nowrap}
.g{background:#dcf3e3;color:#16803d}.o{background:#fff0c9;color:#8a6200}.r{background:#ffe0e1;color:#b4161e}
.al{background:#e3262f;color:#fff;border-radius:24px;padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.al small{color:#ffd0d2}
.sl{display:flex;gap:10px}.sl span{flex:1;text-align:center;background:rgba(255,255,255,.16);border-radius:12px;padding:10px 4px;font:700 19px 'Source Sans 3'}
.sl span.f{background:#fff;color:#e3262f}
""", "<h1>“Do you have 185/65 R15?”<br><span>Answer before the call ends.</span></h1><div class=sub>For tyre shops: stock by size across shop and godown, plus alignment bookings.</div>",
f'''<div class=st><small>STOCK BY SIZE · SAMPLE</small>{"".join(f'<div class="ty{" hit" if s=="185/65 R15" else ""}"><b>{s}</b><em>{q} in stock</em></div>' for s,q in tyres)}</div>
<div class=rt><div class=sc><div class=sb>{ic("search",30,w=3)}185/65 R15</div><small>4 RESULTS · SAMPLE</small>
{"".join(f'<div class=rr><div><b>{a}</b><span>{b}</span></div><em class={c}>{d}</em></div>' for a,b,c,d in [("Sample Tyre A","Tubeless · Shop rack 2","g","6 here"),("Sample Tyre A","Tubeless · Godown 1","g","2 there"),("Sample Tyre B","Tubeless · Shop","o","1 left"),("Sample Tyre C","Tube type","r","Order now")])}</div>
<div class=al><small>WHEEL ALIGNMENT · TODAY · WHITE = FREE</small><div class=sl>{"".join(f'<span class="{"f" if f else ""}">{t}</span>' for t,f in [("10:00",0),("11:30",1),("2:00",0),("4:30",1)])}</div></div></div>''',
"#141619", "Run a tyre shop? DM us", "background:#141619;color:#fff")

# ───────── 63 INDIA · Lawyer / advocate office · SINGLE · Crimson Text + Roboto · legal navy / parchment / oxblood
# New technique: tear-off desk calendar (binding rings + torn zigzag page underneath via clip-path).
P["p63_lawyer"] = page("""
body{--f:'Roboto';--h:'Crimson Text';background:#f4ecdc;color:#1b2340}
h1{font-family:'Crimson Text';font-size:74px;font-weight:700;letter-spacing:-.5px} h1 span{color:#7d1f2a}
.sub{color:#5b5f72}
.vis{gap:22px}
.cal{flex:1;background:#1b2340;border-radius:30px;padding:34px 30px 30px;display:flex;flex-direction:column;position:relative}
.rings{display:flex;justify-content:space-around;padding:0 40px;position:relative;z-index:2;height:34px}
.rings i{width:22px;height:34px;border-radius:11px;background:linear-gradient(90deg,#9ba3b8,#e6e9f0,#9ba3b8);display:block}
.pad{flex:1;position:relative;margin-top:-14px}
.torn{position:absolute;left:0;right:0;top:0;height:60px;background:#e8dcc4;clip-path:polygon(0 0,100% 0,100% 70%,95% 100%,90% 70%,85% 100%,80% 70%,75% 100%,70% 70%,65% 100%,60% 70%,55% 100%,50% 70%,45% 100%,40% 70%,35% 100%,30% 70%,25% 100%,20% 70%,15% 100%,10% 70%,5% 100%,0 70%)}
.pgc{position:absolute;left:0;right:0;top:50px;bottom:0;background:#fffaf0;border-radius:6px 6px 18px 18px;display:flex;flex-direction:column;align-items:center;padding:20px 24px;box-shadow:0 -6px 0 #e8dcc4}
.pgc .mo{font:700 26px Roboto;letter-spacing:6px;color:#7d1f2a}
.pgc .dt{font:700 190px/1.35 'Crimson Text';color:#1b2340;margin-top:6px}
.ckl{width:100%;display:flex;flex-direction:column;gap:10px;margin-top:22px}.ckl div{display:flex;align-items:center;gap:12px;font:500 21px Roboto;background:#fff;border:2px solid #ece4d3;border-radius:12px;padding:10px 14px}.ckl svg{color:#3f7d2c;flex:none}.ckl div.no svg{color:#b8a888}
.pgc .dy{font:500 26px Roboto;color:#5b5f72}
.cs{margin-top:auto;width:100%;background:#f4ecdc;border-left:8px solid #7d1f2a;border-radius:12px;padding:16px 18px}
.cs b{display:block;font:700 26px/1.25 'Crimson Text'}.cs span{font:500 19px/1.4 Roboto;color:#5b5f72}
.wk{flex:1.05;display:flex;flex-direction:column;gap:14px;min-width:0}
.lst{flex:1;background:#fff;border-radius:28px;padding:22px 24px;display:flex;flex-direction:column;gap:10px}
.lst small{font:700 14px Roboto;letter-spacing:3px;color:#8d8f9c}
.hr{flex:1;display:flex;align-items:center;gap:16px;border-bottom:1px solid #ece4d3}
.hr:last-child{border-bottom:none}
.hr .d{width:66px;text-align:center;flex:none}.hr .d b{display:block;font:700 32px/1.2 'Crimson Text'}.hr .d span{font:700 14px Roboto;letter-spacing:2px;color:#7d1f2a}
.hr div b{display:block;font:700 21px Roboto}.hr div span{font:400 18px Roboto;color:#5b5f72}
.rm{background:#7d1f2a;color:#fff;border-radius:24px;padding:20px 22px;display:flex;align-items:center;gap:14px;font:500 21px/1.4 Roboto}
.rm svg{flex:none}
""", "<h1>Hearing dates in a diary?<br><span>Get reminders instead.</span></h1><div class=sub>For advocates: case dates, client files and hearing reminders in one place.</div>",
f'''<div class=cal><div class=rings><i></i><i></i><i></i><i></i></div><div class=pad><div class=torn></div><div class=pgc><span class=mo>DECEMBER</span><span class=dt>14</span><span class=dy>Monday · next hearing</span><div class=ckl>{"".join(f'<div class="{c}">{ic("check" if c=="" else "clock",24,w=3)}{t}</div>' for t,c in [("Documents ready",""),("Client informed",""),("Notes from last date","no")])}</div>
<div class=cs><b>Sample vs Sample</b><span>Civil matter · Court room 4 · 11 am<br>File: 3 documents attached</span></div></div></div></div>
<div class=wk><div class=lst><small>THIS WEEK · SAMPLE</small>{"".join(f'<div class=hr><div class=d><b>{d}</b><span>{m}</span></div><div><b>{a}</b><span>{b}</span></div></div>' for d,m,a,b in [("14","MON","Sample vs Sample","Court room 4 · 11 am"),("15","TUE","Rent dispute, Mr. R","Arguments · 2 pm"),("16","WED","Property papers, Ms. K","Client meeting · office"),("17","THU","Cheque matter, Mr. S","Next date to be fixed"),("18","FRI","Partnership deed","Drafting due")])}</div>
<div class=rm>{ic("bell",34)}Client gets a reminder one day before each hearing.</div></div>''',
"#1b2340", "Advocate? Let's talk. DM us", "background:#7d1f2a;color:#fff")

# ───────── 64 INDIA · Tractor / farm equipment rental · SINGLE · Fira Sans + Gelasio · field green / mustard / soil brown
# New technique: Gantt-style week booking chart (bars spanning day columns).
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
rows = [("Tractor 1", "with rotavator", [(0, 2, "Ramesh · 2 days", "a"), (3, 1, "Sunil", "b"), (5, 2, "Mohan · 2 days", "a")]),
        ("Tractor 2", "with trolley", [(1, 1, "Anil", "b"), (4, 2, "Kiran · 2 days", "a")]),
        ("Tractor 3", "with cultivator", [(0, 1, "Vijay", "b"), (4, 3, "Prakash · 3 days", "a")]),
        ("Seed drill", "attachment", [(2, 1, "Ramesh", "b"), (5, 1, "Sunil", "b")])]
def gantt():
    out = '<div class=gh><span></span>' + "".join(f'<b class="{"th" if d=="Thu" else ""}">{d}</b>' for d in days) + '</div>'
    for n, s, bars in rows:
        out += f'<div class=gr><div class=gn><b>{n}</b><span>{s}</span></div><div class=gt>' + "".join(f'<i class={k} style="grid-column:{a+1}/span {l}">{t}</i>' for a, l, t, k in bars) + '</div></div>'
    return out
P["p64_tractor"] = page("""
body{--f:'Fira Sans';--h:'Gelasio';background:#f6efd9;color:#2f2416}
h1{font-family:'Gelasio';font-size:66px;font-weight:700;letter-spacing:-.5px} h1 span{color:#3f7d2c}
.sub{color:#6a5b44}
.vis{flex-direction:column;gap:18px}
.gc{flex:1;background:#fff;border-radius:28px;padding:22px 24px;display:flex;flex-direction:column;gap:10px}
.gc small{font:700 14px 'Fira Sans';letter-spacing:3px;color:#9a8a6c}
.gh,.gr{display:grid;grid-template-columns:190px 1fr;gap:12px}
.gh{grid-template-columns:190px repeat(7,1fr);gap:6px;font:700 18px 'Fira Sans';text-align:center;color:#6a5b44}
.gh b{padding:8px 0;border-radius:10px}.gh b.th{background:#3f7d2c;color:#fff}
.gr{flex:1;align-items:stretch}
.gn{display:flex;flex-direction:column;justify-content:center}.gn b{font:700 25px Gelasio}.gn span{font:500 17px 'Fira Sans';color:#6a5b44}
.gt{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;background:repeating-linear-gradient(90deg,#f6efd9 0 calc((100% - 36px)/7),transparent calc((100% - 36px)/7) calc((100% - 36px)/7 + 6px));border-radius:12px;padding:10px 0;align-items:center}
.gt i{font-style:normal;height:100%;min-height:56px;border-radius:12px;display:flex;align-items:center;padding:0 10px;font:700 17px 'Fira Sans';white-space:nowrap;overflow:hidden}
.gt i.a{background:#e1a92b;color:#2f2416}.gt i.b{background:#8a5a32;color:#fff}
.bt{display:flex;gap:16px;flex:none;height:240px}
.fr{flex:1.2;background:#3f7d2c;color:#fff;border-radius:26px;padding:22px 24px;display:flex;flex-direction:column;gap:10px}
.fr small{font:700 14px 'Fira Sans';letter-spacing:3px;color:#cfe8c4}.fr b{font:700 30px/1.25 Gelasio}
.fr div{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1px solid rgba(255,255,255,.2);font:500 20px 'Fira Sans'}
.fr div em{font-style:normal;font:700 17px 'Fira Sans';background:#fff;color:#3f7d2c;padding:5px 12px;border-radius:9px}
.fr div em.p{background:#e1a92b;color:#2f2416}
.qq{flex:1;background:#2f2416;color:#f6efd9;border-radius:26px;padding:22px 24px;display:flex;flex-direction:column;justify-content:center;gap:10px}
.qq b{font:700 34px/1.25 Gelasio;color:#e1a92b}.qq span{font:500 20px/1.4 'Fira Sans'}
""", "<h1>Which tractor is free<br>on Thursday?<br><span>See the whole week.</span></h1>",
f'''<div class=gc><small>BOOKINGS THIS WEEK · SAMPLE</small>{gantt()}</div>
<div class=bt><div class=fr><small>RAMESH · SAMPLE</small><b>Tractor 1, Mon to Tue</b><div>Hours used: 14<em>Logged</em></div><div>Advance<em>Received</em></div><div>Balance<em class=p>Pending</em></div></div>
<div class=qq><b>Thursday:</b><span>Tractors 2 and 3 and the seed drill are free. Book them for the next caller.</span></div></div>''',
"#2f2416", "Rent out farm machines? DM us", "background:#3f7d2c;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
