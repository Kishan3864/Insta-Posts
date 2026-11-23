import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
fmt = lambda n: f"{n:,}"

# ───────── 341 INDIA · Rice mill (paddy job milling) · SINGLE · Gelasio + DM Sans · paddy gold / jute brown / rice white
# New technique: isotype jute sacks (SVG with a cross-hatch pattern fill, 1 sack = 5 bags) per farmer lot, stage
# chips derived from one lot list, and a farmer message for the lot that is done.
LOTS = [("L-10", "Farmer A", 40, "Done", "Mon 16 Nov"), ("L-11", "Farmer B", 55, "Milling", "Wed 18 Nov"),
        ("L-12", "Farmer C", 30, "Drying", "Fri 20 Nov"), ("L-13", "Farmer D", 45, "Waiting", "Sun 22 Nov")]
STC = {"Done": "dn", "Milling": "ml", "Drying": "dr", "Waiting": "wt"}
def sack(dim=False):
    op = ".35" if dim else "1"
    return (f'<svg viewBox="0 0 44 56" class=sk1 style="opacity:{op}"><path d="M10 10 Q22 4 34 10 L40 48 Q22 56 4 48 Z" fill="url(#jt1)" stroke="#6b4a22" stroke-width="2.5"/>'
            f'<path d="M12 10 Q22 15 32 10" fill="none" stroke="#6b4a22" stroke-width="2.5"/><rect x="17" y="2" width="10" height="8" rx="2" fill="#8a6430"/></svg>')
DEFS1 = '<svg width="0" height="0" style="position:absolute"><defs><pattern id="jt1" width="6" height="6" patternUnits="userSpaceOnUse"><rect width="6" height="6" fill="#c99a52"/><path d="M0 3 H6 M3 0 V6" stroke="#b0823e" stroke-width="1.4"/></pattern></defs></svg>'
P["p341_rice"] = page("""
body{--f:'DM Sans';--h:'Gelasio';background:#f6efdc;color:#3a2a12}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#a0701d;margin-top:22px}
h1{font-family:'Gelasio';font-weight:700;font-size:62px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#a0701d}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.yd1{flex:1;min-height:0;background:#fffaf0;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(58,42,18,.08)}
.yd1>small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#8a7350;margin-bottom:6px}
.lt1{flex:1;display:grid;grid-template-columns:120px 1fr 150px;gap:14px;align-items:center;border-bottom:1px solid #efe4cc}.lt1:last-of-type{border:0}
.lt1>div:first-child b{display:block;font:700 28px/1.2 Gelasio}.lt1>div:first-child span{font:500 16px/1.4 'DM Sans';color:#6b5a3e}
.sr1{display:flex;flex-wrap:wrap;gap:6px}.sk1{width:46px;height:58px;display:block}
.lt1>div:last-child{text-align:right}.lt1 strong{display:block;font:700 22px/1.3 'DM Sans'}
.lt1 em{display:inline-block;font:700 15px/1.3 'DM Sans';font-style:normal;padding:5px 12px;border-radius:20px;margin-top:4px}
em.dn{background:#2f7d4a;color:#fff}em.ml{background:#e0a425;color:#3a2a12}em.dr{background:#f4e2b8;color:#7a5a1c}em.wt{background:#ece6da;color:#6b5a3e}
.lg1{display:flex;gap:16px;align-items:center;font:600 15px/1.4 'DM Sans';color:#6b5a3e;margin-top:6px}.lg1 .sk1{width:26px;height:32px}
.bt1{display:grid;grid-template-columns:1fr 1.25fr;gap:14px}
.tl1{background:#3a2a12;color:#f6efdc;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;justify-content:center;gap:4px}
.tl1 small{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#d9c08a}.tl1 b{font:700 46px/1.2 Gelasio;color:#ffd77a}.tl1 span{font:500 17px/1.4 'DM Sans'}
.ms1{background:#fff;border-radius:22px 22px 22px 6px;padding:16px 20px;display:flex;flex-direction:column;gap:6px;box-shadow:0 12px 26px rgba(58,42,18,.08)}
.ms1 small{display:flex;align-items:center;gap:8px;font:700 14px/1.4 'DM Sans';color:#2f7d4a}.ms1 p{font:500 20px/1.45 'DM Sans'}
""", "<div class=kk>RICE MILL · PADDY JOB MILLING</div><h1>Whose paddy is this?<br><span>Track every lot by farmer.</span></h1>",
f'''{DEFS1}<div class=vw><div class=yd1><small>MILL YARD · {len(LOTS)} LOTS · SAMPLE</small>
{"".join(f'<div class=lt1><div><b>{l}</b><span>{f}</span></div><div class=sr1>{"".join(sack(s=="Waiting") for _ in range(b//5))}</div><div><strong>{b} bags</strong><em class={STC[s]}>{s}</em></div></div>' for l,f,b,s,d in LOTS)}
<div class=lg1>{sack()}<span>One sack = 5 bags. Faded = still waiting.</span></div></div>
<div class=bt1><div class=tl1><small>IN THE YARD</small><b>{sum(l[2] for l in LOTS)} bags</b><span>{len(LOTS)} farmers, each lot with its own tag and date</span></div>
<div class=ms1><small>{ic("chat",18)} MESSAGE TO FARMER A · LOT L-10</small><p>Your lot L-10 ({LOTS[0][2]} bags, came Mon 16 Nov) is milled. Rice and bran are ready for pickup.</p></div></div></div>''',
"#3a2a12", "Run a rice mill? DM us", "background:#3a2a12;color:#ffd77a")

# ───────── 342 INDIA · Vegetable van on a society route · SINGLE · Archivo Black + Roboto · okra green / tomato red / cart wood · PHONE
# New technique: vertical stop route drawn as a road ribbon with dashed centre line and society stop pins, beside a phone
# order list whose bag number and stop time come from the same route list.
STOPS = [("7:30 AM", "Society A", 14, "done"), ("8:15 AM", "Tower C", 22, "now"), ("9:00 AM", "Lane 5 houses", 9, ""), ("9:45 AM", "Society B", 17, ""), ("10:30 AM", "Market corner", 6, "")]
ORD2 = [("Tomatoes", "1 kg"), ("Onions", "2 kg"), ("Potatoes", "2 kg"), ("Spinach", "1 bunch"), ("Lady finger", "500 g"), ("Coriander", "1 bunch"), ("Green chillies", "100 g")]
ph2 = phone(f'''<div class=ap2><div class=ah2><small>SAMPLE SABZI VAN</small><b>Order for Tower C</b><span>Flat 504 · stop at {STOPS[1][0]}</span></div>
<div class=ol2>{"".join(f'<div class=oi2><span>{a}</span><b>{q}</b></div>' for a,q in ORD2)}</div>
<div class=bg2><b>Packed in bag 23</b><span>Pick it up at the gate</span></div><div class=rp2>Same list every Tuesday? Tap to repeat.</div><div class=bk2>Pay by UPI at pickup</div></div>''', 360, 760)
P["p342_sabzi"] = page("""
body{--f:'Roboto';--h:'Archivo Black';background:#eef3e3;color:#1f2a14}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#d64532;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:56px;line-height:1.25;letter-spacing:-1px;margin-top:28px} h1 span{color:#4f7a1f}
.vw{flex:1;display:flex;gap:18px;min-height:0;align-items:center}.rt2{align-self:stretch}
.rt2{flex:1;min-width:0;background:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(31,42,20,.08)}
.rt2>small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#6d7760}
.rl2{flex:1;position:relative;display:flex;flex-direction:column}
.rd2{position:absolute;left:24px;top:10px;bottom:10px;width:26px;border-radius:13px;background:#4a4f45}
.rd2 i{position:absolute;left:12px;top:8px;bottom:8px;border-left:2px dashed #f1f1e8}
.st2{flex:1;display:flex;align-items:center;gap:20px;position:relative;z-index:1}
.st2 .pn{width:74px;flex:none;display:flex;justify-content:center}
.st2 .pn i{width:30px;height:30px;border-radius:50%;background:#fff;border:5px solid #9aa58d}
.st2.done .pn i{background:#4f7a1f;border-color:#4f7a1f}.st2.now .pn i{background:#d64532;border-color:#ffd9d2;width:38px;height:38px}
.st2 div{flex:1}.st2 b{display:block;font:400 26px/1.4 'Archivo Black'}.st2 span{font:500 20px/1.4 Roboto;color:#5c6650}
.st2 strong{font:700 20px/1.3 Roboto;background:#eef3e3;border-radius:10px;padding:6px 12px;white-space:nowrap}.st2.now strong{background:#d64532;color:#fff}
.nt2{background:#1f2a14;color:#fff;border-radius:16px;padding:12px 16px;font:500 18px/1.4 Roboto}.nt2 b{color:#b9e27a}
.ap2{display:flex;flex-direction:column;gap:10px;padding:8px 18px 18px;flex:1}
.ah2 small{display:block;font:700 11px/1.4 Roboto;letter-spacing:2px;color:#6d7760}.ah2 b{display:block;font:400 22px/1.35 'Archivo Black'}.ah2 span{font:500 14px/1.4 Roboto;color:#5c6650}
.ol2{display:flex;flex-direction:column;gap:6px}.oi2{display:flex;justify-content:space-between;background:#f4f7ee;border-radius:10px;padding:11px 12px;font:500 17px/1.35 Roboto}.oi2 b{font-weight:700}
.bg2{background:#ffe8e3;border-radius:14px;padding:10px 12px}.bg2 b{display:block;font:700 17px/1.35 Roboto;color:#b8321f}.bg2 span{font:500 14px/1.4 Roboto}
.rp2{font:600 15px/1.4 Roboto;color:#4f7a1f;background:#eef3e3;border-radius:12px;padding:10px 12px}.bk2{margin-top:auto;background:#4f7a1f;color:#fff;border-radius:14px;padding:13px;text-align:center;font:700 16px Roboto}
""", "<div class=kk>VEGETABLE VAN · SOCIETY ROUTE</div><h1>Shouting at the gate?<br><span>Take orders before you arrive.</span></h1>",
f'''<div class=vw><div class=rt2><small>TODAY'S ROUTE · PRE-ORDERS · SAMPLE</small><div class=rl2><div class=rd2><i></i></div>
{"".join(f'<div class="st2 {c}"><div class=pn><i></i></div><div><b>{n}</b><span>{t}</span></div><strong>{o} orders</strong></div>' for t,n,o,c in STOPS)}</div>
<div class=nt2><b>{sum(s[2] for s in STOPS)} orders</b> packed in numbered bags before the van leaves.</div></div>{ph2}</div>''',
"#1f2a14", "Sell vegetables on a route? DM us", "background:#d64532;color:#fff")

# ───────── 343 INDIA · Silver jewellery karigar job work · SINGLE · Cardo + Inter · polished silver / garnet / black velvet
# New technique: SVG two-pan balance (issued vs returned grams) on a velvet card + karigar ledger where returned,
# scrap and the gap are computed from the same rows; the open gap row is flagged in garnet.
KG = [("Karigar 1", "Anklets, 12 pairs", 600.0, 588.5, 7.5), ("Karigar 2", "Toe rings, 40", 240.0, 231.0, 6.2), ("Karigar 3", "Chains, 8", 400.0, 388.0, 8.0), ("Karigar 4", "Bracelets, 10", 350.0, 342.0, 5.0)]
def gap(r): return round(r[2] - r[3] - r[4], 1)
def scale3():
    return ('<svg viewBox="0 0 420 300" class=sc3><rect x="200" y="40" width="20" height="220" rx="6" fill="#b9bfc8"/><rect x="140" y="256" width="140" height="20" rx="8" fill="#8f97a3"/>'
            '<g transform="rotate(-6 210 50)"><rect x="40" y="44" width="340" height="12" rx="6" fill="#d7dbe1"/>'
            '<path d="M70 56 L40 150 M70 56 L100 150" stroke="#b9bfc8" stroke-width="3"/><path d="M350 56 L320 150 M350 56 L380 150" stroke="#b9bfc8" stroke-width="3"/>'
            '<path d="M24 150 Q70 186 116 150 Z" fill="#d7dbe1"/><path d="M304 150 Q350 186 396 150 Z" fill="#d7dbe1"/>'
            '<rect x="48" y="122" width="44" height="28" rx="4" fill="#eef0f3" stroke="#8f97a3" stroke-width="2"/><rect x="56" y="100" width="28" height="22" rx="4" fill="#eef0f3" stroke="#8f97a3" stroke-width="2"/>'
            '<circle cx="335" cy="140" r="12" fill="none" stroke="#eef0f3" stroke-width="5"/><circle cx="362" cy="140" r="12" fill="none" stroke="#eef0f3" stroke-width="5"/><circle cx="349" cy="122" r="10" fill="none" stroke="#eef0f3" stroke-width="5"/></g>'
            '<circle cx="210" cy="46" r="12" fill="#a51c3a"/></svg>')
P["p343_karigar"] = page("""
body{--f:'Inter';--h:'Cardo';background:#efeff1;color:#1c1b22}
.kk{font:700 16px/1.4 Inter;letter-spacing:3px;color:#a51c3a;margin-top:22px;margin-bottom:4px}
h1{font-family:'Cardo';font-weight:700;font-size:66px;line-height:1.3;letter-spacing:-.5px} h1 span{color:#a51c3a}
.vw{flex:1;display:grid;grid-template-columns:400px 1fr;gap:16px;min-height:0}
.vl3{background:radial-gradient(circle at 30% 20%,#3a2340,#1c1b22 70%);border-radius:26px;padding:22px;display:flex;flex-direction:column;justify-content:space-between;gap:12px;color:#fff}
.vl3>small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#c9b8d0}.sc3{width:100%;display:block}
.vr3{display:grid;grid-template-columns:1fr 1fr;gap:10px}.vr3 div{background:rgba(255,255,255,.08);border-radius:14px;padding:10px 14px}.vr3 small{display:block;font:600 13px/1.4 Inter;color:#c9b8d0}.vr3 b{font:700 28px/1.4 Cardo}
.op3{background:#a51c3a;border-radius:14px;padding:10px 14px;display:flex;flex-direction:column;gap:4px}.op3 small{font:700 12px/1.4 Inter;letter-spacing:2px;color:#ffd3dc}.op3 div{display:flex;justify-content:space-between;font:600 19px/1.4 Inter}.vl3 p{font:500 18px/1.45 Inter;color:#e8e1ec}.vl3 p b{color:#ff8fa6}
.lg3{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(28,27,34,.08)}
.lg3>small{font:700 13px/1.4 Inter;letter-spacing:2px;color:#6d6b78;margin-bottom:4px}
.kr3{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-bottom:1px solid #ececf0}.kr3:last-of-type{border:0}
.kh3{display:flex;justify-content:space-between;align-items:baseline;gap:10px}.kh3 b{font:700 30px/1.4 Cardo}.kh3 span{font:500 16px/1.4 Inter;color:#6d6b78}
.kn3{display:grid;grid-template-columns:repeat(4,1fr);gap:6px}.kn3 div{background:#f5f5f7;border-radius:12px;padding:8px 12px}.kn3 small{display:block;font:600 14px/1.4 Inter;color:#6d6b78}.kn3 strong{font:700 24px/1.4 Inter}
.kr3.bad{background:#fff1f3;margin:0 -10px;padding:0 10px;border-radius:14px}.kr3.bad .kn3 div:last-child{background:#a51c3a;color:#fff}.kr3.bad .kn3 div:last-child small{color:#ffd3dc}
""", "<div class=kk>SILVER JEWELLERY · KARIGAR JOB WORK</div><h1>Every gram issued,<br><span>every gram back.</span></h1>",
f'''<div class=vw><div class=vl3><small>THIS WEEK · ALL KARIGARS · SAMPLE</small>{scale3()}
<div class=vr3><div><small>Silver issued</small><b>{fmt(int(sum(r[2] for r in KG)))} g</b></div><div><small>Back as jewellery</small><b>{sum(r[3] for r in KG):,.1f} g</b></div><div><small>Scrap back</small><b>{sum(r[4] for r in KG):.1f} g</b></div><div><small>Not yet matched</small><b>{sum(gap(r) for r in KG):.1f} g</b></div></div>
<div class=op3><small>OPEN GAPS TODAY</small>{''.join(f'<div><span>{r[0]}</span><b>{gap(r):.1f} g</b></div>' for r in KG if gap(r)>3)}</div><p>Grams that are not matched show up the same day, <b>not at the month-end count.</b></p></div>
<div class=lg3><small>KARIGAR LEDGER · GRAMS · SAMPLE</small>{"".join(f'<div class="kr3 {"bad" if gap(r)>3 else ""}"><div class=kh3><b>{r[0]}</b><span>{r[1]}</span></div><div class=kn3><div><small>Issued</small><strong>{r[2]:.1f}</strong></div><div><small>Jewellery</small><strong>{r[3]:.1f}</strong></div><div><small>Scrap</small><strong>{r[4]:.1f}</strong></div><div><small>Gap</small><strong>{gap(r):.1f}</strong></div></div></div>' for r in KG)}</div></div>''',
"#1c1b22", "Give out job work? DM us", "background:#a51c3a;color:#fff")

# ───────── 345 CANADA · Mobile sauna trailer rental · SINGLE · Lora + Source Sans 3 · cedar orange / snow blue / charcoal
# New technique: SVG barrel sauna on a trailer (wood staves via repeating stripes, chimney smoke) + a two-trailer
# weekend booking strip where delivered / picked up dates come from one booking list.
BK5 = {("T1", "Fri 4"): "Cottage, Lake Rd", ("T1", "Sat 5"): "Cottage, Lake Rd", ("T2", "Sat 5"): "Backyard, Elm St", ("T2", "Sun 6"): "Backyard, Elm St",
       ("T1", "Fri 11"): "Cabin, Hill Rd", ("T2", "Sat 12"): "Backyard, Oak Ave", ("T1", "Sun 13"): "Cabin, Hill Rd"}
DAYS5 = ["Fri 4", "Sat 5", "Sun 6", "Fri 11", "Sat 12", "Sun 13"]
def sauna():
    s = '<svg viewBox="0 0 520 300" class=sn5><defs><pattern id="st5" width="20" height="200" patternUnits="userSpaceOnUse"><rect width="20" height="200" fill="#c9733a"/><rect x="17" width="3" height="200" fill="#9c5326"/></pattern></defs>'
    s += '<path d="M392 40 Q380 20 398 6 M410 44 Q400 24 418 10" fill="none" stroke="#c7d6e3" stroke-width="5" stroke-linecap="round"/><rect x="388" y="44" width="18" height="40" fill="#3b3f45"/>'
    s += '<rect x="70" y="70" width="380" height="160" rx="80" fill="url(#st5)" stroke="#6e3a18" stroke-width="5"/>'
    s += '<rect x="150" y="74" width="10" height="152" fill="#3b3f45"/><rect x="360" y="74" width="10" height="152" fill="#3b3f45"/>'
    s += '<circle cx="450" cy="150" r="50" fill="#9c5326" stroke="#6e3a18" stroke-width="5"/><rect x="430" y="118" width="40" height="64" rx="6" fill="#6e3a18"/><rect x="438" y="126" width="24" height="24" rx="3" fill="#ffd27a"/>'
    s += '<rect x="40" y="232" width="440" height="14" rx="5" fill="#3b3f45"/><path d="M40 239 L6 250" stroke="#3b3f45" stroke-width="8" stroke-linecap="round"/>'
    s += '<circle cx="230" cy="262" r="26" fill="#2b2e33"/><circle cx="230" cy="262" r="10" fill="#9aa3ad"/><circle cx="296" cy="262" r="26" fill="#2b2e33"/><circle cx="296" cy="262" r="10" fill="#9aa3ad"/>'
    s += '<rect x="0" y="286" width="520" height="14" rx="7" fill="#e3edf5"/></svg>'
    return s
def cell5(t, d):
    p = BK5.get((t, d))
    return f'<div class="c5 {"bk" if p else ""}"><b>{p.split(",")[0] if p else "Open"}</b>{f"<span>{p.split(", ")[1]}</span>" if p else ""}</div>'
P["p345_sauna"] = page("""
body{--f:'Source Sans 3';--h:'Lora';background:#e7eef4;color:#22262b}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#b8612c;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:62px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#b8612c}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.tp5{background:#fff;border-radius:26px;padding:16px 24px;display:grid;grid-template-columns:1.2fr 1fr;gap:18px;align-items:center;box-shadow:0 14px 30px rgba(34,38,43,.08)}
.sn5{width:100%;display:block}
.in5{display:flex;flex-direction:column;gap:10px}.in5>small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b7580}
.in5 div{display:flex;gap:12px;align-items:center;font:600 19px/1.35 'Source Sans 3'}.in5 .ib{width:44px;height:44px;border-radius:12px;background:#fbe6d6;color:#b8612c}
.cl5{flex:1;min-height:0;background:#22262b;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;gap:10px;color:#fff}
.cl5>small{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#b7c4d1}
.gd5{flex:1;display:grid;grid-template-columns:120px repeat(6,1fr);grid-template-rows:auto 1fr 1fr;gap:8px;min-height:0}
.gd5 .dh{font:700 17px/1.35 'Source Sans 3';text-align:center;color:#b7c4d1}.gd5 .dh b{display:block;font:700 15px/1.35 'Source Sans 3';color:#fff}
.gd5 .tr{display:flex;flex-direction:column;justify-content:center;font:700 22px/1.3 Lora}.gd5 .tr span{font:500 15px/1.35 'Source Sans 3';color:#b7c4d1}
.c5{border-radius:12px;background:rgba(255,255,255,.06);border:2px dashed rgba(255,255,255,.18);display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:6px}
.c5>*{flex:none}.c5 b{font:700 20px/1.45 'Source Sans 3';color:#9fb0c1}.c5.bk{background:#c9733a;border:0}.c5.bk b{color:#fff}.c5 span{display:block;font:500 16px/1.45 'Source Sans 3';color:#ffe3cc;margin-top:3px}
.nt5{background:#b8612c;color:#fff;border-radius:16px;padding:12px 18px;font:500 19px/1.4 'Source Sans 3'}.nt5 b{color:#ffe3cc}
""", "<div class=kk>MOBILE SAUNA RENTAL · WEEKENDS</div><h1>Two sauna trailers,<br><span>every weekend booked online.</span></h1>",
f'''<div class=vw><div class=tp5>{sauna()}<div class=in5><small>EACH BOOKING INCLUDES · SAMPLE</small>{"".join(f'<div><span class=ib>{ic(i,22)}</span>{t}</div>' for i,t in [("truck","Drop-off and pickup"),("pin","Address and level spot photo"),("leaf","Firewood bundle"),("check","Safety and use checklist")])}</div></div>
<div class=cl5><small>DECEMBER WEEKENDS · TRAILER T1 AND T2 · SAMPLE</small><div class=gd5><div></div>{"".join(f'<div class=dh>{d.split()[0]}<b>Dec {d.split()[1]}</b></div>' for d in DAYS5)}
{"".join(f'<div class=tr>{t}<span>Barrel sauna</span></div>' + "".join(cell5(t,d) for d in DAYS5) for t in ["T1","T2"])}</div>
<div class=nt5><b>{12 - len(BK5)} open days left.</b> Customers pick a free day, add a photo of the spot and pay the deposit online.</div></div></div>''',
"#22262b", "Rent out saunas? DM us", "background:#22262b;color:#ffcfa8")

# ───────── 344 USA · Plastic moving crate rental · CAROUSEL 5 · TeX Gyre Adventor + Fira Sans · safety lime / charcoal / label white
# New technique: CSS stacked moving crates (lime body, ribbed sides, handle slot, lid lip) reused as stacks per job;
# yard counts per day computed from one job list (drop and pickup dates) and shown as stacked numbers on a week grid.
CR = """
body{--f:'Fira Sans';--h:'TeX Gyre Adventor';background:#eef0ea;color:#24272a}
.kk{font:600 16px/1.4 'Fira Sans';letter-spacing:3px;color:#5d7a00;margin-top:22px}
h1{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;line-height:1.22;letter-spacing:-1.5px} h1 span{color:#5d7a00}
.cd{background:#fff;border-radius:24px;box-shadow:0 12px 28px rgba(36,39,42,.08)}
.cap{font:600 14px/1.4 'Fira Sans';letter-spacing:2px;color:#6c7177}
.nb{display:flex;align-items:center;gap:14px;background:#24272a;color:#fff;border-radius:20px;padding:16px 20px;font:400 21px/1.4 'Fira Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#b8e021;color:#24272a}.nb b{color:#d4f25a;font-weight:600}
.crt{width:96px;height:44px;border-radius:5px;background:repeating-linear-gradient(90deg,#b8e021 0 12px,#a6cc17 12px 14px);border-top:7px solid #8fb20c;position:relative;flex:none}
.crt::after{content:"";position:absolute;left:34px;top:10px;width:28px;height:10px;border-radius:5px;background:#3c4a07}
.crt.ms{background:none;border:3px dashed #e5484d}.crt.ms::after{display:none}
.stk{display:flex;flex-direction:column-reverse;align-items:center;gap:3px}
"""
def cr(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#24272a;color:#d4f25a"):
    return page(CR + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#24272a", cta, ctacss, tagline=f"{n} / 5")
def stack(k, miss=0):
    return '<div class=stk>' + "".join('<div class="crt ms"></div>' if i >= k - miss else '<div class=crt></div>' for i in range(k)) + '</div>'
JOBS = [("J-101", "Maple St", 40, 7, 11), ("J-102", "Cedar Ave", 30, 8, 12), ("J-103", "Lake Dr", 50, 9, 14), ("J-104", "Birch Ct", 40, 0, 7), ("J-105", "Pine Rd", 20, 3, 10)]
STOCK = 300
OUT = sum(j[2] for j in JOBS)
def yard(d): return STOCK - sum(j[2] for j in JOBS if j[3] <= d < j[4])
P["p344_crates_s1"] = cr(1, "MOVING CRATE RENTAL", f"{OUT} crates out on {len(JOBS)} jobs.<br><span>Which ones come back today?</span>",
f'''<div class=w1><div class="cd c1">{"".join(f'<div class=jb1>{stack(j[2]//5)}<b>{j[0]}</b><span>{j[1]}</span><strong>{j[2]} crates</strong></div>' for j in JOBS)}</div>
<div class=nb><span class=ib>{ic("x",24)}</span><span>Sticky notes on the office wall: <b>"J-104 pickup Mon? Or was it Tue?"</b></span></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.c1{flex:1;padding:24px 20px 20px;display:grid;grid-template-columns:repeat(5,1fr);gap:10px;align-items:end;background:linear-gradient(transparent 82%,#e2e5dc 82%),#fff}
.jb1{display:flex;flex-direction:column;align-items:center;gap:4px}.jb1 .stk{margin-bottom:10px}.jb1 b{font:700 24px/1.35 'TeX Gyre Adventor'}.jb1 span{font:400 17px/1.4 'Fira Sans';color:#555a60}.jb1 strong{font:600 18px/1.4 'Fira Sans';background:#24272a;color:#d4f25a;border-radius:8px;padding:2px 10px}
.c1 .crt{width:124px;height:60px}.c1 .crt::after{left:46px;top:16px}""")

ROOMS = [("home", "Bedrooms", 3, 10), ("cup", "Kitchen", 1, 15), ("users", "Living room", 1, 10), ("box", "Office", 1, 8)]
nC = sum(q * r for _, _, q, r in ROOMS)
form2 = f'''<div class=bf2><div class=lf2><b>How many crates do you need?</b>{"".join(f'<div class=rm2><span class=ib>{ic(i,22)}</span><div><b>{a}</b><span>about {r} crates each · sample</span></div><div class=qt2><i>−</i><strong>{q}</strong><i>+</i></div></div>' for i,a,q,r in ROOMS)}</div>
<div class=rt2><div class=tt2><small>YOU NEED</small><b>{nC}</b><span>crates</span></div><div class=ad2><span>Dollies</span><b>2</b></div><div class=ad2><span>Rental</span><b>2 weeks</b></div><div class=ad2><span>ZIP code</span><b>In our area</b></div><div class=ad2><span>Drop-off</span><b>Mon, Dec 14</b></div><div class=ad2><span>Pickup</span><b>Mon, Dec 28</b></div><div class=bk2>Pick drop-off date</div></div></div>'''
P["p344_crates_s2"] = cr(2, "STEP 1 · ORDER ONLINE BY ROOM", "Customers count rooms,<br><span>the site counts crates.</span>",
f'''<div class=w2>{browser(form2, url="yourcraterental.com/order · sample")}<div class=nb><span class=ib>{ic("check",24)}</span><span>No more guessing on the phone. <b>Every order has a room list, a crate count and dates.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.w2>.browser{flex:1}
.bf2{flex:1;display:grid;grid-template-columns:1.5fr 1fr;gap:18px;padding:20px 22px}
.lf2{display:flex;flex-direction:column;gap:10px}.lf2>b{font:700 25px/1.3 'TeX Gyre Adventor';margin-bottom:4px}
.rm2{flex:1;display:flex;align-items:center;gap:14px;background:#f4f6f0;border-radius:16px;padding:10px 14px}.rm2 .ib{width:46px;height:46px;border-radius:12px;background:#e4f5a8;color:#3c4a07}
.rm2>div:nth-child(2){flex:1}.rm2 b{display:block;font:700 22px/1.35 'TeX Gyre Adventor'}.rm2 span{font:400 17px/1.4 'Fira Sans';color:#555a60}
.qt2{display:flex;align-items:center;gap:10px}.qt2 i{width:34px;height:34px;border-radius:10px;background:#fff;border:2px solid #d5d9cf;font:600 20px/30px 'Fira Sans';font-style:normal;text-align:center}.qt2 strong{font:700 24px 'TeX Gyre Adventor';width:22px;text-align:center}
.rt2{display:flex;flex-direction:column;gap:10px}.tt2{background:#24272a;color:#fff;border-radius:18px;padding:16px;text-align:center}.tt2 small{font:600 13px/1.4 'Fira Sans';letter-spacing:2px;color:#b9bec4}.tt2 b{display:block;font:700 72px/1.2 'TeX Gyre Adventor';color:#d4f25a}.tt2 span{font:400 18px/1.4 'Fira Sans'}
.ad2{display:flex;justify-content:space-between;background:#f4f6f0;border-radius:12px;padding:12px 14px;font:400 19px/1.4 'Fira Sans'}.ad2 b{font-weight:600}
.bk2{margin-top:auto;background:#b8e021;color:#24272a;border-radius:14px;padding:14px;text-align:center;font:700 18px 'TeX Gyre Adventor'}""")

WK = [("Mon", 7), ("Tue", 8), ("Wed", 9), ("Thu", 10), ("Fri", 11), ("Sat", 12)]
def ev(d):
    e = [f'<i class=dp>Drop {j[0]} · {j[2]}</i>' for j in JOBS if j[3] == d] + [f'<i class=pk>Pickup {j[0]} · {j[2]}</i>' for j in JOBS if j[4] == d]
    return "".join(e) or '<i class=no>No moves</i>'
P["p344_crates_s3"] = cr(3, "STEP 2 · ONE CALENDAR FOR DROPS AND PICKUPS", "See the week,<br><span>and what is left in the yard.</span>",
f'''<div class=w3><div class="cd ca3">{"".join(f'<div class=dy3><div class=hd3><b>{w}</b><span>Dec {d}</span></div><div class=ev3>{ev(d)}</div><div class=gg3><i style="height:{yard(d)/STOCK*100:.0f}%"></i></div><div class=yd3><strong>{yard(d)}</strong><span>in the yard</span></div></div>' for w,d in WK)}</div>
<div class=nb><span class=ib>{ic("truck",24)}</span><span>Sample fleet of {STOCK} crates. <b>Yard counts update with every drop and pickup.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.ca3{flex:1;padding:16px;display:grid;grid-template-columns:repeat(6,1fr);gap:10px;min-height:0}
.dy3{display:flex;flex-direction:column;gap:8px;background:#f4f6f0;border-radius:16px;padding:12px 10px}
.hd3{text-align:center}.hd3 b{display:block;font:700 22px/1.3 'TeX Gyre Adventor'}.hd3 span{font:400 16px/1.4 'Fira Sans';color:#555a60}
.gg3{flex:1;min-height:60px;background:#e2e5dc;border-radius:10px;display:flex;align-items:flex-end;overflow:hidden}.gg3 i{width:100%;background:repeating-linear-gradient(0deg,#b8e021 0 16px,#a6cc17 16px 19px)}.ev3{flex:none;display:flex;flex-direction:column;gap:8px}.ev3 i{font:600 17px/1.35 'Fira Sans';font-style:normal;border-radius:10px;padding:10px 8px;text-align:center}
.ev3 .dp{background:#b8e021;color:#24272a}.ev3 .pk{background:#24272a;color:#d4f25a}.ev3 .no{background:none;border:2px dashed #cfd4c8;color:#8a9096}
.yd3{background:#fff;border-radius:12px;padding:10px 4px;text-align:center}.yd3 strong{display:block;font:700 34px/1.2 'TeX Gyre Adventor'}.yd3 span{font:400 14px/1.4 'Fira Sans';color:#555a60}""")

j4 = JOBS[3]; back = 38
P["p344_crates_s4"] = cr(4, "STEP 3 · COUNT THEM BACK IN", f"{j4[0]}: {j4[2]} out, {back} back.<br><span>Found at the door.</span>",
f'''<div class=w4><div class="cd st4"><small class="cap hd4">PICKUP · J-104 · MON DEC 7 · EACH ICON = ONE CRATE · SAMPLE</small><div class=sk4>{"".join(stack(5, 2 if c==7 else 0) for c in range(8))}</div>
<div class=ck4>{"".join(f'<div class="cr4 {"bad" if not ok else ""}"><span>{a}</span><b>{v}</b></div>' for a,v,ok in [("Crates out",str(j4[2]),1),("Crates back",str(back),0),("Dollies back","2 of 2",1),("Labels removed","Yes",1),("Checked by","Driver 2, Mon Dec 7",1)])}</div></div>
<div class="cd ms4"><small class=cap>TEXT TO THE CUSTOMER · {j4[0]} · {j4[1].upper()}</small><p>Thanks for moving with us! We picked up {back} of {j4[2]} crates. 2 are still at your place. Can we grab them tomorrow at 10 AM?</p></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.st4{flex:1;padding:22px;display:grid;grid-template-columns:1.2fr 1fr;grid-template-rows:auto 1fr;gap:16px 22px;align-items:center;min-height:0}.hd4{grid-column:1 / 3;align-self:start}
.sk4{display:grid;grid-template-columns:repeat(4,1fr);gap:18px 10px;justify-items:center}.sk4 .crt{width:104px;height:52px}.sk4 .crt::after{left:38px;top:14px}
.ck4{display:flex;flex-direction:column;gap:10px}.cr4{display:flex;justify-content:space-between;gap:10px;background:#f4f6f0;border-radius:14px;padding:14px 16px;font:400 21px/1.4 'Fira Sans'}.cr4 b{font-weight:600;text-align:right}
.cr4.bad{background:#fde8e8;color:#b42328}
.ms4{padding:18px 22px;display:flex;flex-direction:column;gap:8px}.ms4 p{font:400 23px/1.45 'Fira Sans'}""")

P["p344_crates_s5"] = cr(5, "YOUR TURN", "Rent moving crates?<br><span>Let's build your booking site.</span>",
f'''<div class=w5><div class="cd c5">{"".join(stack(k) for k in [6,8,10,8,6])}</div>
<div class=sd5>{"".join(f'<div class=ti><span class=ib>{ic(i,30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("home","Order by room","Crate count done for them"),("cal","Drop and pickup","One calendar, yard counts"),("check","Count back in","Missing crates found fast"),("send","Customer texts","Dates, reminders, thanks")])}</div>
<div class=q>How do you keep track of crates out on jobs today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b8e021;color:#24272a",
css=""".w5{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}.c5{display:flex;align-items:flex-end;justify-content:center;gap:6px;padding:24px 16px;background:linear-gradient(transparent 92%,#e2e5dc 92%),#fff}.c5 .crt{width:84px;height:54px}.c5 .crt::after{left:28px;top:14px}.w5 .q{grid-column:1 / 3}
.sd5{display:flex;flex-direction:column;gap:12px}.ti{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(36,39,42,.07)}
.ti .ib{width:58px;height:58px;border-radius:18px;background:#e4f5a8;color:#3c4a07}.ti b{display:block;font:700 22px/1.4 'TeX Gyre Adventor';margin-bottom:2px}.ti div span{font:400 17px/1.4 'Fira Sans';color:#555a60}
.q{background:#24272a;color:#fff;border-radius:22px;padding:20px 24px;font:500 23px/1.4 'Fira Sans'}""")

if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
