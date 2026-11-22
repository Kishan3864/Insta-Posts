import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 26 INDIA · Two-wheeler service centre · SINGLE · Fira Sans · petrol teal / amber / off-white
# New technique: diagonal before/after split (clip-path) with a paper job card vs a digital job card.
chk = lambda t, on: f'<div class=ck><span class="bx {"on" if on else ""}">{"✓" if on else ""}</span>{t}</div>'
P["p26_bikeservice"] = page("""
body{--f:'Fira Sans';background:#0b4f5c;color:#fff}
.diag{position:absolute;inset:0;background:#f3efe6;clip-path:polygon(0 0,100% 0,100% 30%,0 66%)}
h1{font-size:64px;font-weight:800;letter-spacing:-1.5px;color:#0b4f5c} h1 span{color:#d9480f}
.sub{color:#4e5d60}
.wm{color:#0b4f5c}
.vis{position:relative}
.paper{position:absolute;left:0;top:10px;width:560px;background:#fffbea;border-radius:6px;padding:24px 26px;color:#3a3a3a;transform:rotate(-4deg);box-shadow:0 24px 40px rgba(0,0,0,.18);font-family:'Gelasio'}
.paper h4{font:700 22px 'Fira Sans';letter-spacing:2px;color:#0b4f5c;border-bottom:2px dashed #c9bfa4;padding-bottom:10px;margin-bottom:10px}
.ck{display:flex;align-items:center;gap:12px;font:italic 25px 'Gelasio';padding:7px 0}
.bx{width:24px;height:24px;border:2px solid #6d6d6d;border-radius:4px;display:flex;align-items:center;justify-content:center;font:700 16px 'Fira Sans';color:#d9480f;flex:none}
.oil{position:absolute;right:30px;bottom:26px;width:90px;height:60px;border-radius:50%;background:radial-gradient(circle,rgba(60,40,10,.35),rgba(60,40,10,0) 70%)}
.q{font:italic 22px 'Gelasio';color:#d9480f;margin-top:16px}
.tagB{position:absolute;left:620px;top:60px;font:800 18px 'Fira Sans';letter-spacing:3px;color:#d9480f}
.tagA{position:absolute;right:0;top:190px;font:800 18px 'Fira Sans';letter-spacing:3px;color:#ffb627}
.dig{position:absolute;right:0;bottom:0;width:640px;background:#fff;border-radius:26px;color:#10353c;padding:28px;box-shadow:0 34px 70px rgba(0,0,0,.35);display:flex;flex-direction:column;gap:12px}
.dh{display:flex;justify-content:space-between;align-items:flex-start}.dh b{font:800 29px 'Fira Sans'}.dh small{display:block;font:500 16px 'Fira Sans';color:#6b7d80}
.pl{font:800 18px 'Fira Sans';background:#ffb627;color:#10353c;padding:7px 12px;border-radius:10px;letter-spacing:1px}
.stp{display:flex;gap:8px}.stp span{flex:1;height:10px;border-radius:5px;background:#e3ecec}.stp .on{background:#0b4f5c}
.sl{display:flex;justify-content:space-between;font:600 16px 'Fira Sans';color:#6b7d80}
.wk{display:flex;align-items:center;gap:12px;padding:15px 16px;border-radius:14px;background:#f1f6f6;font:600 21px 'Fira Sans'}
.wk i{font-style:normal;margin-left:auto;font:700 15px 'Fira Sans';padding:5px 10px;border-radius:10px}
.ok{background:#dcf3e4;color:#1d7a43}.ask{background:#fff1d6;color:#a86400}
.msg{background:#0b4f5c;color:#fff;border-radius:16px;padding:16px 18px;font:500 20px/1.4 'Fira Sans';display:flex;gap:12px;align-items:center}
.msg .ib{width:42px;height:42px;border-radius:50%;background:#ffb627;color:#0b4f5c}
""", "<h1>Bike ready by 5?<br><span>Stop the 10 calls.</span></h1><div class=sub>For two-wheeler service centres: digital job cards that update the customer for you.</div>",
f'''<div class=paper><h4>JOB CARD · SAMPLE</h4>{chk("Engine oil",True)}{chk("Brake shoe",False)}{chk("Chain set ?",False)}{chk("Clutch wire",True)}{chk("Washing",False)}<div class=q>Customer number... on the other slip?</div><div class=oil></div></div>
<div class=tagB>BEFORE</div><div class=tagA>AFTER</div>
<div class=dig><div class=dh><div><b>Job card #1042</b><small>Sample · in at 9:30 AM</small></div><span class=pl>XX 00 AB 1234</span></div>
<div class=stp><span class=on></span><span class=on></span><span class=on></span><span></span></div><div class=sl><span>Received</span><span>Checked</span><span>Working</span><span>Ready</span></div>
<div class=wk>Engine oil change<i class=ok>Done</i></div><div class=wk>Brake shoe<i class=ask>Ask customer</i></div><div class=wk>Clutch wire<i class=ok>Done</i></div><div class=wk>Washing<i class=ask>In progress</i></div>
<div class=msg><span class=ib>{ic("send",22)}</span>"Brake shoe is worn. Replace it? Reply YES." Sent to the customer.</div></div>''',
"#fff", "Want digital job cards? DM us", "background:#ffb627;color:#0b4f5c", bg="<div class=diag></div>")

# ───────── 27 INDIA · Beauty parlour · SINGLE · Lora + DM Sans · peach / plum · COMIC STRIP (4 panels)
def panel(n, cap, art, bubble, bpos, bg="#fff"):
    return f'<div class=pn style="background:{bg}"><div class=nb>{n}</div><div class=cap>{cap}</div><div class=art>{art}</div><div class="bb {bpos}">{bubble}</div></div>'
P["p27_parlour"] = page("""
body{--f:'DM Sans';--h:'Lora';background:#ffe9dc;color:#4a1942}
h1{font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#c2410c;font-style:italic}
.sub{color:#7b4a6e}
.vis{display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;gap:16px}
.pn{border:4px solid #4a1942;border-radius:22px;position:relative;overflow:hidden;display:flex;flex-direction:column;padding:14px 16px 0}
.nb{position:absolute;left:14px;top:14px;width:36px;height:36px;border-radius:50%;background:#4a1942;color:#fff;font:700 18px/36px 'DM Sans';text-align:center}
.cap{font:700 19px/1.3 'DM Sans';padding-left:48px;min-height:52px}
.art{flex:1;display:flex;align-items:flex-end;justify-content:center;gap:6px;min-height:0}
.bb{position:absolute;background:#fff;border:3px solid #4a1942;border-radius:20px;padding:10px 14px;font:600 17px/1.35 'DM Sans';max-width:270px}
.r{right:14px;top:70px}.l{left:14px;top:76px}
.ph{width:64px;height:110px;border-radius:14px;background:#4a1942;margin-bottom:60px;display:flex;align-items:center;justify-content:center;color:#ffb37a;flex:none}
.cal{width:300px;background:#fff;border:3px solid #4a1942;border-radius:16px;padding:10px;margin-bottom:16px;display:flex;flex-direction:column;gap:6px;flex:none}
.cal div{display:flex;justify-content:space-between;font:600 17px 'DM Sans';padding:9px 10px;border-radius:8px;background:#fbeee6}
.cal .bk{background:#4a1942;color:#fff}.cal .rd{background:#fde2e2;color:#b42318}
""", "<h1>Saturday at the parlour,<br><span>with and without bookings.</span></h1><div class=sub>A 4-panel story every beauty parlour owner knows.</div>",
 panel(1, "11 AM. Hands busy, phone ringing.", peep("Explaining","Concerned","Bun",w=250,h=300)+f'<div class=ph>{ic("phone",34)}</div>', "Is 4 PM free? I'll come for a facial.", "r") +
 panel(2, "4 PM. Two customers, one slot.", peep("Paper","Concerned","Long",w=220,h=290)+peep("ArmsCrossed","Angry","MediumShort",w=220,h=290,flip=True), "But I booked on call!", "l", "#fff4ee") +
 panel(3, "Next week: customers book online.", f'<div class=cal><div>3:00 PM<span>Open</span></div><div class=bk>4:00 PM<span>Facial · booked</span></div><div class=rd>5:00 PM<span>Taken</span></div><div>6:00 PM<span>Open</span></div><div class=bk>7:00 PM<span>Hair spa · booked</span></div></div>', "Slot booked. Reminder sent.", "r", "#f6ecff") +
 panel(4, "Saturday, calm. Every slot is clear.", peep("Coffee","Smile","Bun",w=270,h=310), "Now I can focus on my work.", "r", "#fff"),
"#4a1942", "Want online booking? DM us", "background:#4a1942;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
