import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"


# ───────── 376 INDIA · Ready-mix concrete (RMC) plant · SINGLE · Archivo Black + Roboto · concrete grey / safety orange / drum teal
# New technique: CSS side-view transit mixers (cab + striped drum + wheels) as an isotype per order, one truck per 7 m3,
# coloured by trip state; the "site ready" checks gate each order and the plant message is derived from the missing check.
CHK6 = ["Shuttering done", "Steel checked", "Pump on site", "Labour ready", "Water and power"]
TR6 = 7
O6 = [("RO-41", "Site A", "Roof slab", "M25", 21, [1, 1, 1, 1, 1], "go"),
      ("RO-42", "Site B", "Footing", "M20", 14, [1, 1, 0, 1, 1], "hold"),
      ("RO-43", "Site C", "Road PCC", "M15", 28, [1, 1, 1, 1, 1], "road"),
      ("RO-44", "Site D", "Columns", "M25", 7, [0, 1, 1, 1, 0], "hold")]
def mixer(state):
    return f'<div class="mx6 {state}"><i class=dr></i><i class=cb></i><i class=ch></i><i class="w w1"></i><i class="w w2"></i><i class="w w3"></i></div>'
def trucks(m3, st):
    n = math.ceil(m3 / TR6)
    if st == "road": sts = ["done"] + ["road"] + ["wait"] * (n - 2)
    elif st == "go": sts = ["load"] + ["wait"] * (n - 1)
    else: sts = ["hold"] * n
    return "".join(mixer(s) for s in sts)
STL6 = {"go": "Loading now", "road": "Trip 2 of 4 on road", "hold": "On hold"}
def miss(c): return [CHK6[i] for i, v in enumerate(c) if not v]
P["p376_rmc"] = page("""
body{--f:'Roboto';--h:'Archivo Black';background:#e9e7e3;color:#22262b;font-variant-numeric:tabular-nums}
.kk{font:700 16px/1.4 Roboto;letter-spacing:3px;color:#c2510f;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;line-height:1.22;letter-spacing:-.5px;margin-top:12px} h1 span{color:#f26b1d}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ck6{background:#22262b;color:#fff;border-radius:26px;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.ck6 .t{display:flex;justify-content:space-between;align-items:center}
.ck6 small,.bd6 small{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#b9c0c7}
.ck6 .t b{font:700 15px/1.2 Roboto;background:#1fa37a;color:#fff;border-radius:20px;padding:8px 14px}
.ph6{display:grid;grid-template-columns:repeat(5,1fr);gap:10px}
.ph6>div{background:rgba(255,255,255,.07);border-radius:16px;padding:12px 10px 12px;display:flex;flex-direction:column;align-items:center;gap:8px;position:relative}
.ph6 .im{width:100%;height:84px;border-radius:10px;background:linear-gradient(160deg,#5d6670,#3a4148);display:flex;align-items:center;justify-content:center;color:#d7dde2}
.ph6 span{font:600 15px/1.3 Roboto;text-align:center;color:#e9edf0}
.ph6 em{position:absolute;top:18px;right:16px;width:26px;height:26px;border-radius:50%;background:#1fa37a;display:flex;align-items:center;justify-content:center;color:#fff}
.bd6{flex:1;background:#fff;border-radius:26px;padding:16px 22px 10px;display:flex;flex-direction:column;box-shadow:0 14px 30px rgba(34,38,43,.08);min-height:0}
.bd6 small{color:#6f767d;margin-bottom:4px}
.bd6>.r{flex:1;display:grid;grid-template-columns:1.15fr 2.55fr 1fr;gap:14px;align-items:center;border-top:1px solid #ecebe8}
.bd6 .r b{display:block;font:700 20px/1.3 Roboto}.bd6 .r span{font:400 16px/1.35 Roboto;color:#5c636a}
.tk6{display:flex;gap:10px;flex-wrap:wrap;align-items:center}.tk6 .mx6{zoom:1.12}.tk6 em{font:600 15px/1.3 Roboto;font-style:normal;color:#b52a16;background:#fff4f2;border:1.5px dashed #e0442a;border-radius:10px;padding:6px 10px}
.lgd6{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}.lgd6 small{margin:0}.lgd6 div{display:flex;gap:14px;align-items:center}.lgd6 span{display:flex;align-items:center;gap:6px;font:500 14px/1.2 Roboto;color:#5c636a}.lgd6 i{width:14px;height:14px;border-radius:4px}
.dt6{display:flex;gap:5px;margin-top:6px}.dt6 i{width:14px;height:14px;border-radius:50%;background:#1fa37a}.dt6 i.n{background:#fff;border:2px solid #e0442a}
.st6{justify-self:end;font:700 15px/1.25 Roboto;border-radius:12px;padding:8px 12px;text-align:center}
.st6.go{background:#d8f3ea;color:#127a5a}.st6.road{background:#ffe6d4;color:#b4470b}.st6.hold{background:#fde3df;color:#b52a16}
.mx6{width:92px;height:48px;position:relative;flex:none}
.mx6 .dr{position:absolute;left:4px;top:4px;width:60px;height:30px;border-radius:16px 22px 22px 16px;background:repeating-linear-gradient(115deg,#138a8a 0 9px,#e9e7e3 9px 15px);transform:skewY(-6deg)}
.mx6 .cb{position:absolute;right:2px;top:8px;width:24px;height:26px;border-radius:6px 9px 3px 3px;background:#f26b1d}
.mx6 .cb::after{content:'';position:absolute;right:4px;top:4px;width:11px;height:9px;border-radius:2px 5px 2px 2px;background:#cfe7f2}
.mx6 .ch{position:absolute;left:2px;right:2px;top:33px;height:5px;border-radius:3px;background:#3a4148}
.mx6 .w{position:absolute;top:34px;width:14px;height:14px;border-radius:50%;background:#22262b;box-shadow:inset 0 0 0 4px #22262b,inset 0 0 0 7px #9aa3ab}
.mx6 .w1{left:10px}.mx6 .w2{left:28px}.mx6 .w3{right:6px}
.mx6.done .dr{background:repeating-linear-gradient(115deg,#aab2b9 0 9px,#e9e7e3 9px 15px)}.mx6.done .cb{background:#aab2b9}
.mx6.road .dr{background:repeating-linear-gradient(115deg,#f26b1d 0 9px,#fff2e8 9px 15px)}
.mx6.wait,.mx6.hold{opacity:.38}.mx6.hold .cb{background:#8a939b}
.ms6{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.ms6>div{border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:6px}
.ms6 small{font:700 13px/1.4 Roboto;letter-spacing:2px}
.ms6 p{font:500 18px/1.45 Roboto;text-wrap:pretty}
.ms6 .a{background:#fde3df;border-radius:22px 22px 22px 6px}.ms6 .a small{color:#b52a16}.ms6 .a p{color:#4a1a12}
.ms6 .b{background:#22262b;color:#fff}.ms6 .b small{color:#ffb07c}.ms6 .b p{color:#eef1f3}
""", "<div class=kk>READY-MIX CONCRETE PLANT · POUR DAY</div><h1>Mixer stuck at the site?<br><span>Send it only when ready.</span></h1>",
f'''<div class=vw><div class=ck6><div class=t><small>SITE READY CHECK · {O6[0][0]} · {O6[0][1].upper()} · 5 PHOTOS</small><b>All 5 OK · Load now</b></div>
<div class=ph6>{"".join(f'<div><div class=im>{ic(i, 38, "#d7dde2", 1.8)}</div><span>{c}</span><em>{ic("check", 16, "#fff", 3)}</em></div>' for c, i in zip(CHK6, ["grid", "wrench", "truck", "users", "drop"]))}</div></div>
<div class=bd6><div class=lgd6><small>TODAY'S POURS · 1 MIXER = {TR6} m³ · SAMPLE</small><div>{"".join(f'<span><i style="background:{c}"></i>{t}</span>' for c, t in [("#aab2b9", "Done"), ("#f26b1d", "On road"), ("#138a8a", "Loading"), ("#c9e3e3", "Waiting")])}</div></div>{"".join(f'<div class=r><div><b>{o} · {s}</b><span>{w} · {g} · {m}&nbsp;m³</span><div class=dt6>{"".join(f"<i class={chr(34)}{chr(110) if not v else chr(121)}{chr(34)}></i>" for v in c)}</div></div><div class=tk6>{trucks(m, st)}{f'<em>Needs: {", ".join(miss(c)).lower()}</em>' if miss(c) else ''}</div><div class="st6 {st}">{STL6[st]}</div></div>' for o, s, w, g, m, c, st in O6)}</div>
<div class=ms6><div class=a><small>AUTO MESSAGE TO {O6[1][1].upper()}</small><p>{O6[1][0]} is on hold: <b>{" and ".join(miss(O6[1][5])).lower()}</b> photo missing. Send it and the mixer leaves in 15 minutes.</p></div>
<div class=b><small>WHY IT HELPS</small><p>Mixers leave only for sites that are ready, so no truck stands waiting while the concrete sets.</p></div></div></div>''',
"#22262b", "Run an RMC plant? DM us", "background:#f26b1d;color:#fff")


# ───────── 377 INDIA · Cotton ginning factory · CAROUSEL 5 · Bitter + Open Sans · cotton white / boll green / jute brown
# New technique: SVG side-view tractor + trolley heaped with cotton (bump path) as a gate queue isotype with token flags,
# an LED "now weighing" board, a printed weigh slip with computed net, and CSS pressed bales with strap bands per lot.
TK7 = [("T-14", "Sample Village A", "Weighing now", "now"), ("T-15", "Sample Village B", "At the gate", "gate"), ("T-16", "Sample Village A", "At the gate", "gate"),
       ("T-17", "Sample Village C", "About 11:10 AM", "home"), ("T-18", "Sample Village D", "About 11:30 AM", "home"), ("T-19", "Sample Village B", "About 11:50 AM", "home"), ("T-20", "Sample Village E", "About 12:10 PM", "home")]
GR7, TA7 = 7840, 3260
NET7 = GR7 - TA7
LOT7 = [("L-07", 4580), ("L-08", 6200), ("L-09", 3900), ("L-10", 5100)]
OT7, BW7 = 0.34, 170
def tractor7(tok, col="#4f7a3a", load=True, w=230):
    heap = '<path d="M86 46 q10 -20 24 -8 q10 -18 26 -6 q12 -16 26 -2 q12 -14 24 2 q10 -6 14 12 z" fill="#fff" stroke="#d9d3c3" stroke-width="2"/>' if load else ''
    return f'''<svg viewBox="0 0 230 120" width="{w}" style="display:block">{heap}
<rect x="84" y="46" width="118" height="34" rx="4" fill="#8b5e34"/><rect x="84" y="46" width="118" height="6" fill="#6f4826"/>
<rect x="70" y="72" width="16" height="5" fill="#3b3a33"/><circle cx="118" cy="92" r="14" fill="#2b2a24"/><circle cx="118" cy="92" r="5" fill="#bdb6a4"/><circle cx="170" cy="92" r="14" fill="#2b2a24"/><circle cx="170" cy="92" r="5" fill="#bdb6a4"/>
<rect x="10" y="50" width="52" height="24" rx="5" fill="{col}"/><rect x="34" y="22" width="30" height="32" rx="4" fill="none" stroke="{col}" stroke-width="5"/><rect x="8" y="40" width="6" height="14" fill="#3b3a33"/>
<circle cx="52" cy="86" r="24" fill="#2b2a24"/><circle cx="52" cy="86" r="10" fill="#e6c34a"/><circle cx="16" cy="96" r="13" fill="#2b2a24"/><circle cx="16" cy="96" r="5" fill="#e6c34a"/>
{f'<rect x="10" y="2" width="56" height="22" rx="6" fill="#2b2a24"/><text x="38" y="18" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="15" fill="#fff">{tok}</text>' if tok else ''}</svg>'''
def bale7(): return '<i class=bl7><b></b><b></b><b></b></i>'
B7 = """
body{--f:'Open Sans';--h:'Bitter';background:#fbfaf5;color:#2b2a24;font-variant-numeric:lining-nums tabular-nums}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#8b5e34;margin-top:22px}
h1{font-family:'Bitter';font-weight:800;font-size:60px;line-height:1.2;letter-spacing:-.5px} h1 span{color:#4f7a3a}
.cd7{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(43,42,36,.08)}
.sm7{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#7a7465}
.led7{background:#1c1b17;border-radius:20px;padding:14px 20px;display:flex;justify-content:space-between;align-items:center;gap:14px}
.led7 small{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#a8a08c}.led7 b{font:700 44px/1.3 'Courier New',monospace;color:#ffb21e;letter-spacing:3px;text-shadow:0 0 12px rgba(255,178,30,.45)}
.bl7{display:block;width:62px;height:42px;border-radius:6px;background:linear-gradient(#fffdf6,#ece6d6);border:2px solid #d4ccb8;position:relative;flex:none}
.bl7 b{position:absolute;top:-2px;bottom:-2px;width:5px;background:#8b5e34}.bl7 b:nth-child(1){left:12px}.bl7 b:nth-child(2){left:27px}.bl7 b:nth-child(3){left:42px}
"""
def b7(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#4f7a3a;color:#fff"):
    return page(B7 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#2b2a24", cta, ctacss, tagline=f"{n} / 5")
P["p377_gin_s1"] = b7(1, "COTTON GINNING FACTORY · PEAK SEASON", "Tractor line outside the gin?<br><span>Give every farmer a token.</span>",
f'''<div class=w71><div class="cd7 q71"><div class=hd71><span class=sm7>GATE · 9:40 AM · SAMPLE</span><span class=sm7>7 TROLLEYS IN LINE</span></div>
<div class=gt71><span>SAMPLE GINNING FACTORY</span><b>GATE 1 · KANTA</b></div>
<div class=rd71>{"".join(f'<div>{tractor7(t[0], "#4f7a3a" if i == 0 else "#7d9a68", True, 205)}</div>' for i, t in enumerate(TK7[:4]))}</div><div class=road71></div>
<div class=rd71>{"".join(f'<div>{tractor7(t[0], "#7d9a68", True, 205)}</div>' for t in TK7[4:])}<div class=mr71>+ more<br>on the road</div></div><div class=road71></div>
<div class=led7><small>NOW WEIGHING</small><b>{TK7[0][0]}</b><small>NEXT {TK7[1][0]} · {TK7[2][0]}</small></div></div>
<div class=pn71>{"".join(f'<div class=bb71><b>{a}</b><span>{b}</span></div>' for a, b in [("“Since 6 AM in the line.”", "Farmers wait all day with no idea when"), ("“Whose trolley was weighed?”", "Paper slips get mixed up at the kanta"), ("“How many bales from my lot?”", "Owner asks the press floor every hour")])}</div>
<div class=st71>{"".join(f'<div><i>{n}</i><b>{a}</b></div>' for n, a in [(1, "Token on arrival"), (2, "Weigh slip in seconds"), (3, "Lots to bales")])}</div></div>''',
css=""".w71{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.q71{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:10px;background:linear-gradient(#eef3e6,#fff 70%)}.hd71{display:flex;justify-content:space-between}
.rd71{flex:1;display:flex;align-items:flex-end;justify-content:space-between;gap:8px}.mr71{width:205px;align-self:center;text-align:center;font:600 17px/1.35 'Open Sans';color:#7a7465;border:2px dashed #c9bfa6;border-radius:14px;padding:14px}
.gt71{align-self:center;background:#8b5e34;color:#fff;border-radius:14px;padding:10px 26px;text-align:center;box-shadow:0 8px 0 #6f4826}.gt71 span{display:block;font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#f1dfc6}.gt71 b{font:800 26px/1.3 Bitter;letter-spacing:1px}.road71{height:12px;border-radius:6px;background:repeating-linear-gradient(90deg,#c9bfa6 0 40px,#e7e0cf 40px 60px);margin-top:-6px}
.pn71{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.bb71{background:#fff;border-radius:20px 20px 20px 6px;padding:16px 18px;box-shadow:0 10px 22px rgba(43,42,36,.07);display:flex;flex-direction:column;gap:6px}
.bb71 b{font:700 21px/1.3 Bitter}.bb71 span{font:500 16px/1.4 'Open Sans';color:#5f5a4d;text-wrap:pretty}
.st71{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}.st71>div{display:flex;align-items:center;gap:12px;background:#2b2a24;color:#fff;border-radius:18px;padding:14px 16px}
.st71 i{width:36px;height:36px;border-radius:50%;background:#4f7a3a;font:700 18px/36px Bitter;font-style:normal;text-align:center;flex:none}.st71 b{font:600 18px/1.3 'Open Sans'}""")

P["p377_gin_s2"] = b7(2, "1 · TOKEN ON ARRIVAL", "Get a token by phone.<br><span>Wait at home, not at the gate.</span>",
f'''<div class=w72><div class="cd7 tb72"><span class=sm7>TODAY'S TOKENS · 20 MIN EACH · SAMPLE</span>
{"".join(f'<div class="r72 {s}"><b class=tk>{t}</b><span>{v}</span><em>{w}</em></div>' for t, v, w, s in TK7)}</div>
<div class=sd72><div class="cd7 sms72"><span class=sm7>MESSAGE TO TOKEN {TK7[4][0]}</span><p>Token {TK7[4][0]} for Sample Village D. Your turn is about 11:30 AM. Start from home after our next message.</p><p>Message 2 · 10:50 AM: Leave now. Two trolleys before you.</p></div>
<div class="cd7 ky72"><span class=sm7>WHAT THE FARMER SENDS</span>{"".join(f'<div><span class=ib>{ic(i, 24)}</span><b>{a}</b></div>' for i, a in [("users", "Name and village"), ("truck", "Trolley number"), ("phone", "Phone for the message"), ("img", "Photo of the cotton")])}</div></div></div>''',
css=""".w72{flex:1;display:grid;grid-template-columns:1.15fr 1fr;gap:14px;min-height:0}
.tb72{padding:18px 22px;display:flex;flex-direction:column;gap:6px}.r72{flex:1;display:grid;grid-template-columns:84px 1fr auto;gap:12px;align-items:center;border-top:1px solid #eee9dc}
.r72 .tk{font:700 24px/1.3 Bitter}.r72 span{font:500 18px/1.35 'Open Sans';color:#4a463b}.r72 em{font:700 15px/1.2 'Open Sans';font-style:normal;border-radius:10px;padding:7px 10px;background:#f1ede2;color:#6b5a3c;white-space:nowrap}
.r72.now em{background:#ffb21e;color:#2b2a24}.r72.gate em{background:#e3ecd8;color:#3d6128}
.sd72{display:flex;flex-direction:column;gap:14px}.sms72{padding:18px 20px;display:flex;flex-direction:column;gap:10px;background:#e8f1de}
.sms72 p{background:#fff;border-radius:16px 16px 16px 4px;padding:12px 14px;font:500 18px/1.45 'Open Sans';text-wrap:pretty}
.ky72{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:8px}.ky72>div{flex:1;display:flex;align-items:center;gap:12px;border-top:1px solid #eee9dc}
.ky72 .ib{width:42px;height:42px;border-radius:12px;background:#4f7a3a;color:#fff}.ky72 b{font:600 19px/1.3 'Open Sans'}""")

P["p377_gin_s3"] = b7(3, "2 · WEIGH SLIP IN SECONDS", "Full trolley, empty trolley.<br><span>Net weight, sent to the farmer.</span>",
f'''<div class=w73><div class=lf73><div class="cd7 tr73"><span class=sm7>{TK7[0][0]} ON THE KANTA</span><div class=pair73><div>{tractor7(TK7[0][0], "#4f7a3a", True, 250)}<b>Full · {GR7:,} kg</b></div><div>{tractor7(TK7[0][0], "#4f7a3a", False, 250)}<b>Empty · {TA7:,} kg</b></div></div></div>
<div class=led7><small>NET<br>COTTON</small><b>{NET7:,} KG</b><small>SENT<br>10:02 AM</small></div></div>
<div class="sl73"><div class=sh73><b>WEIGH SLIP</b><span>Sample Ginning Factory</span></div>
{"".join(f'<div class=ln73><span>{a}</span><b>{b}</b></div>' for a, b in [("Slip no.", "WS-0482"), ("Token", TK7[0][0]), ("Farmer", "Sample Farmer"), ("Village", TK7[0][1]), ("Full trolley", f"{GR7:,} kg"), ("Empty trolley", f"{TA7:,} kg")])}
<div class="ln73 nt"><span>Net cotton</span><b>{NET7:,} kg</b></div>
{"".join(f'<div class=ln73><span>{a}</span><b>{b}</b></div>' for a, b in [("Moisture (sample)", "8%"), ("Lot", LOT7[0][0])])}
<div class=sg73>Checked by: Kanta staff · Copy sent by message</div></div></div>''',
css=""".w73{flex:1;display:grid;grid-template-columns:1.1fr 1fr;gap:16px;min-height:0}.lf73{display:flex;flex-direction:column;gap:14px}
.tr73{flex:1;padding:18px 20px;display:flex;flex-direction:column;gap:10px}.pair73{flex:1;display:flex;flex-direction:column;justify-content:space-around;align-items:center}
.pair73>div{display:flex;flex-direction:column;align-items:center;gap:6px}.pair73 svg{zoom:1.3}.pair73 b{font:700 21px/1.3 'Open Sans'}
.led7 b{font-size:40px;white-space:nowrap}
.sl73{background:#fffef8;border:2px dashed #d4ccb8;border-radius:8px;padding:22px 24px;display:flex;flex-direction:column;gap:2px;font-family:'Courier New',monospace;box-shadow:0 18px 34px rgba(43,42,36,.10)}
.sh73{text-align:center;border-bottom:2px dashed #d4ccb8;padding-bottom:12px;margin-bottom:8px}.sh73 b{display:block;font:700 26px/1.3 'Courier New',monospace;letter-spacing:3px}.sh73 span{font:600 16px/1.3 'Open Sans';color:#6b6455}
.ln73{flex:1;display:flex;justify-content:space-between;align-items:center;gap:10px;font-size:19px;line-height:1.3}.ln73 b{font-weight:700}
.ln73.nt{background:#e3ecd8;border-radius:8px;padding:0 10px;margin:4px -10px;font-size:22px;color:#2f4f1d}
.sg73{border-top:2px dashed #d4ccb8;padding-top:12px;margin-top:8px;font:600 15px/1.4 'Open Sans';color:#6b6455;text-align:center}""")

P["p377_gin_s4"] = b7(4, "3 · LOTS TO BALES", "Cotton in, bales out.<br><span>Every lot on one board.</span>",
f'''<div class=w74><div class="cd7 bd74"><div class=hd74><span class=sm7>PRESS BOARD · LINT {OT7:.0%} OF COTTON · 1 BALE = {BW7} KG · SAMPLE</span></div>
{"".join(f'<div class=r74><div><b>{l}</b><span>{k:,} kg cotton</span></div><div class=bs74>{"".join(bale7() for _ in range(int(k * OT7 // BW7)))}</div><div class=n74><b>{int(k * OT7 // BW7)}</b><span>bales</span></div></div>' for l, k in LOT7)}</div>
<div class=bt74><div class="cd7 tt74">{"".join(f'<div><b>{a}</b><span>{b}</span></div>' for a, b in [(f"{sum(k for _, k in LOT7):,} kg", "cotton in 4 lots"), (f"{sum(int(k * OT7 // BW7) for _, k in LOT7)}", "bales pressed"), ("4", "lots closed today")])}</div>
<div class=ow74><small>OWNER'S PHONE · 6 PM</small><p>Today: 4 lots, {sum(int(k * OT7 // BW7) for _, k in LOT7)} bales. Biggest lot {max(LOT7, key=lambda x: x[1])[0]} gave {int(max(k for _, k in LOT7) * OT7 // BW7)} bales.</p></div></div></div>''',
css=""".w74{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.bd74{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:6px}.r74{flex:1;display:grid;grid-template-columns:190px 1fr 90px;gap:14px;align-items:center;border-top:1px solid #eee9dc}
.r74 b{display:block;font:700 24px/1.3 Bitter}.r74 span{font:500 16px/1.35 'Open Sans';color:#5f5a4d}
.bs74{display:flex;flex-wrap:wrap;gap:8px 8px;align-content:center}.n74{text-align:right}.n74 b{font-size:40px;color:#4f7a3a}
.bt74{display:grid;grid-template-columns:1.4fr 1fr;gap:14px}.tt74{display:grid;grid-template-columns:repeat(3,1fr);padding:16px 10px}
.tt74>div{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;border-left:1px solid #eee9dc}.tt74>div:first-child{border:0}
.tt74 b{font:800 32px/1.3 Bitter;color:#2b2a24}.tt74 span{font:500 15px/1.35 'Open Sans';color:#5f5a4d;text-align:center}
.ow74{background:#2b2a24;color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}.ow74 small{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#c9b48f}.ow74 p{font:500 18px/1.45 'Open Sans';text-wrap:pretty}""")

P["p377_gin_s5"] = b7(5, "YOUR TURN", "Run a ginning factory?<br><span>Let's build your gate app.</span>",
f'''<div class=w75><div class="cd7 pv75">{tractor7("", "#4f7a3a", True, 400)}<div class=bb75>{"".join(bale7() for _ in range(6))}</div></div>
<div class=td75>{"".join(f'<div class=ti75><span class=ib>{ic(i, 30)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i, a, b in [("clock", "Tokens", "Farmers wait at home"), ("doc", "Weigh slips", "Net weight sent by message"), ("grid", "Lot board", "Cotton in, bales out"), ("chart", "Day summary", "On the owner's phone")])}</div>
<div class=q75>How long is the tractor line at your gate in peak season? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#8b5e34;color:#fff",
css=""".w75{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr auto;gap:14px;min-height:0}
.pv75{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;padding:20px;background:linear-gradient(#eef3e6 66%,#e7e0cf 66%)}
.bb75{display:grid;grid-template-columns:repeat(3,auto);gap:10px}.bb75 .bl7{width:92px;height:60px}.bb75 .bl7 b:nth-child(1){left:20px}.bb75 .bl7 b:nth-child(2){left:42px}.bb75 .bl7 b:nth-child(3){left:64px}
.td75{display:flex;flex-direction:column;gap:12px}.ti75{flex:1;display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:14px 20px;box-shadow:0 10px 22px rgba(43,42,36,.07)}
.ti75 .ib{width:58px;height:58px;border-radius:18px;background:#4f7a3a;color:#fff}.ti75 b{display:block;font:700 25px/1.3 Bitter}.ti75 div span{font:500 17px/1.4 'Open Sans';color:#5f5a4d}
.q75{grid-column:1 / 3;background:#2b2a24;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'Open Sans'}""")


# ───────── 378 USA · Lawn aeration (spring sign-up list) · SINGLE · Poppins + Source Sans 3 · turf green / plug brown / flag pink
# New technique: top-down SVG street map with lots drawn as house + lawn; signed-up lawns get an SVG <pattern> of core
# plugs and a pink flag; a street opens a route day at 5 yards, and every count/label below is computed from the map.
ST8 = [("Maple St", 10, [0, 2, 3, 5, 6, 8]), ("Oak Ave", 10, [1, 4, 7, 8]), ("Cedar Ln", 10, [2, 5])]
MIN8 = 5
DAY8 = {"Maple St": "Sat, Apr 11"}
def map8():
    W, LW, LH, G = 900, 80, 78, 10
    out = ['<defs><pattern id="pl8" width="12" height="12" patternUnits="userSpaceOnUse"><rect width="12" height="12" fill="#3f9e5c"/><ellipse cx="4" cy="4" rx="2.2" ry="1.6" fill="#6b4226"/><ellipse cx="10" cy="10" rx="2.2" ry="1.6" fill="#6b4226"/></pattern></defs>']
    y = 0
    for name, n, sg in ST8:
        out.append(f'<rect x="0" y="{y}" width="{W}" height="34" rx="8" fill="#5b636b"/><line x1="14" x2="{W - 14}" y1="{y + 17}" y2="{y + 17}" stroke="#e8d36a" stroke-width="3" stroke-dasharray="18 14"/>')
        out.append(f'<rect x="12" y="{y + 5}" width="{len(name) * 13 + 24}" height="24" rx="6" fill="#fff"/><text x="24" y="{y + 23}" font-family="Poppins" font-weight="700" font-size="17" fill="#22302a">{name}</text>')
        ly = y + 42
        for i in range(n):
            x = i * (LW + G) + 2
            on = i in sg
            out.append(f'<rect x="{x}" y="{ly}" width="{LW}" height="{LH}" rx="8" fill="{"url(#pl8)" if on else "#cfe6c8"}" stroke="{"#2f8f4e" if on else "#b5d4ad"}" stroke-width="2"/>')
            out.append(f'<rect x="{x + 22}" y="{ly + 8}" width="50" height="30" rx="3" fill="{"#a5664a" if on else "#b9a89a"}"/><rect x="{x + 22}" y="{ly + 8}" width="50" height="15" rx="3" fill="{"#c07a58" if on else "#cdbfb2"}"/><rect x="{x + 4}" y="{ly + 2}" width="12" height="{LH - 4}" rx="2" fill="#d9d4c8"/>')
            if on: out.append(f'<line x1="{x + 64}" y1="{ly + 70}" x2="{x + 64}" y2="{ly + 40}" stroke="#22302a" stroke-width="2.5"/><path d="M{x + 64} {ly + 40} l14 6 l-14 6 z" fill="#e84a8a"/>')
        y += 42 + LH + 18
    return f'<svg viewBox="0 0 {W} {y - 12}" style="width:100%;display:block">{"".join(out)}</svg>'
P["p378_aeration"] = page("""
body{--f:'Source Sans 3';--h:'Poppins';background:#eef6ee;color:#22302a}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#2f8f4e;margin-top:22px}
h1{font-family:'Poppins';font-weight:800;font-size:64px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#2f8f4e}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.mp8{background:#fff;border-radius:26px;padding:16px 20px 14px;box-shadow:0 14px 30px rgba(34,48,42,.08);display:flex;flex-direction:column;gap:10px}
.mp8 .h{display:flex;justify-content:space-between;align-items:center;gap:10px}
.sm8{font:700 13px/1.4 'Source Sans 3';letter-spacing:2px;color:#617066}
.lg8{display:flex;gap:16px}.lg8 span{display:flex;gap:6px;align-items:center;font:600 15px/1.2 'Source Sans 3';color:#4a5a50}.lg8 i{width:16px;height:16px;border-radius:4px}
.bt8{flex:1;display:grid;grid-template-columns:1fr 1.15fr;gap:14px;min-height:0}
.fm8{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(34,48,42,.08)}
.fd8{flex:1;display:flex;flex-direction:column;justify-content:center;gap:4px;border-top:1px solid #e6eee4;padding:4px 0}
.fd8 small{font:600 14px/1.3 'Source Sans 3';color:#617066}.fd8 b{font:600 19px/1.3 'Source Sans 3'}
.ch8{display:flex;gap:6px;flex-wrap:wrap}.ch8 i{font:600 15px/1.2 'Source Sans 3';font-style:normal;border:1.5px solid #c8d9c4;border-radius:10px;padding:5px 10px;color:#4a5a50}.ch8 i.on{background:#2f8f4e;border-color:#2f8f4e;color:#fff}
.ls8{background:#22302a;color:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}.ls8 .sm8{color:#a9c4b0}
.rw8{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;background:rgba(255,255,255,.06);border-radius:16px;padding:12px 14px}
.rw8 .t{display:flex;justify-content:space-between;align-items:center;gap:8px}.rw8 b{font:700 21px/1.3 Poppins}.rw8 em{font:700 15px/1.2 'Source Sans 3';font-style:normal;border-radius:10px;padding:6px 10px;background:#3a4a41;color:#d6e6da;white-space:nowrap}.rw8 em.ok{background:#e84a8a;color:#fff}
.br8{display:grid;gap:4px}.br8 i{height:14px;border-radius:4px;background:#3a4a41}.br8 i.on{background:#5cc47d}
.rw8 span{font:500 16px/1.35 'Source Sans 3';color:#cfe0d4}
""", "<div class=kk>LAWN AERATION · SPRING SIGN-UP LIST</div><h1>One yard per street?<br><span>Fill the street first.</span></h1>",
f'''<div class=vw><div class=mp8><div class=h><span class=sm8>SAMPLE NEIGHBORHOOD · {sum(len(s) for _, _, s in ST8)} YARDS SIGNED UP</span><div class=lg8><span><i style="background:url(#)#3f9e5c;box-shadow:inset 0 0 0 3px #6b4226"></i>Signed up</span><span><i style="background:#cfe6c8"></i>Not yet</span><span><i style="background:#e84a8a"></i>Sprinklers flagged</span></div></div>{map8()}</div>
<div class=bt8><div class=fm8><span class=sm8>SIGN-UP FORM · 1 MINUTE</span>
<div class=fd8><small>Address</small><b>14 Oak Ave, ZIP 00000</b></div>
<div class=fd8><small>Lawn size</small><div class=ch8><i>Small</i><i class=on>Medium</i><i>Large</i></div></div>
<div class=fd8><small>Sprinkler heads</small><div class=ch8><i class=on>We'll flag them</i><i>No sprinklers</i></div></div>
<div class=fd8><small>Gate and pets</small><b>Side gate open · Dog inside</b></div></div>
<div class=ls8><span class=sm8>ROUTE DAYS · OPENS AT {MIN8} YARDS · SAMPLE</span>{"".join(f'<div class=rw8><div class=t><b>{nm}</b><em class="{"ok" if len(sg) >= MIN8 else ""}">{"Route day: " + DAY8[nm] if len(sg) >= MIN8 else pl(MIN8 - len(sg), "more yard") + " to open"}</em></div><div class=br8 style="grid-template-columns:repeat({n},1fr)">{"".join(f"<i class={chr(34)}{'on' if i in sg else ''}{chr(34)}></i>" for i in range(n))}</div><span>{len(sg)} of {n} yards signed up</span></div>' for nm, n, sg in ST8)}</div></div></div>''',
"#22302a", "Run a lawn crew? DM us", "background:#2f8f4e;color:#fff")


# ───────── 379 INDIA · Hosiery wholesaler (leggings, socks, vests) · SINGLE · Montserrat + Fira Sans · navy / heather grey / coral
# New technique: colour × size order matrix with CSS folded-fabric swatches and dozen counts, totals computed both ways,
# a stock-short cell flagged from a stock dict, and CSS taped cartons (10 dozen each) filled to the order size per shop.
SZ9 = ["M", "L", "XL", "XXL"]
OR9 = [("Black", "#1f1f24", [4, 6, 6, 3]), ("Navy", "#22325e", [2, 4, 4, 2]), ("Maroon", "#7a1f35", [2, 3, 3, 3]),
       ("Beige", "#d9c3a0", [1, 2, 2, 0]), ("Bottle green", "#1f5a43", [0, 2, 2, 1])]
STK9 = {("Maroon", "XXL"): 1}
T9 = sum(sum(q) for _, _, q in OR9)
SH9 = [("R-12 · Your Shop", T9), ("R-09 · Sample Store", 18), ("R-15 · Sample Mart", 25), ("R-21 · Sample Corner", 9)]
CT9 = 10
def short9(c, s, q): return (c, s) in STK9 and STK9[(c, s)] < q
SHORT9 = [(c, SZ9[j], q, STK9[(c, SZ9[j])]) for c, _, qs in OR9 for j, q in enumerate(qs) if short9(c, SZ9[j], q)]
def cartons9(dz):
    out = []
    while dz > 0:
        f = min(dz, CT9); out.append(f'<div class=cx9><i class=tp></i><i class=fl style="height:{f / CT9 * 100:.0f}%"></i><b>{f}</b></div>'); dz -= f
    return "".join(out)
P["p379_hosiery"] = page("""
body{--f:'Fira Sans';--h:'Montserrat';background:#f1f0ed;color:#1d2a4a}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#e2533f;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:62px;line-height:1.2;letter-spacing:-1.5px} h1 span{color:#e2533f}
.vw{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}
.ct9{display:grid;grid-template-columns:auto 1fr 1fr 1fr;gap:12px;align-items:stretch}
.ct9>small{writing-mode:vertical-rl;transform:rotate(180deg);font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#8a8f9c;text-align:center}
.ct9 p{background:#fff;border-radius:18px 18px 18px 4px;padding:12px 14px;font:500 17px/1.4 'Fira Sans';color:#3b4560;box-shadow:0 8px 18px rgba(29,42,74,.07);text-wrap:pretty}
.ct9 p em{display:block;font:600 13px/1.3 'Fira Sans';font-style:normal;color:#8a8f9c;margin-top:4px}
.mx9{flex:1;background:#fff;border-radius:26px;padding:16px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(29,42,74,.08);min-height:0}
.mx9 .h{display:flex;justify-content:space-between;align-items:center}
.sm9{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#6b7183}
.g9{flex:1;display:grid;grid-template-columns:1.6fr repeat(4,1fr) .9fr;gap:6px}
.g9>div{display:flex;align-items:center;justify-content:center;border-radius:10px;font:600 22px/1.2 'Fira Sans'}
.g9 .hd{font:700 15px/1.2 'Fira Sans';color:#6b7183;letter-spacing:1px}
.g9 .nm{justify-content:flex-start;gap:12px;font:600 19px/1.2 'Fira Sans'}
.g9 .q{background:#eef0f5}.g9 .z{background:#f7f7f5;color:#b9bcc6}.g9 .sh{background:#ffe3de;color:#b0301f;box-shadow:inset 0 0 0 2px #e2533f}
.g9 .tt{background:#1d2a4a;color:#fff;font-weight:700}.g9 .tl{font:700 15px/1.2 'Fira Sans';color:#6b7183;justify-content:flex-start}
.sw9{width:40px;height:30px;border-radius:4px;position:relative;flex:none;box-shadow:inset 0 -6px 0 rgba(0,0,0,.18)}
.sw9::after{content:'';position:absolute;right:0;top:0;width:12px;height:12px;background:linear-gradient(225deg,#fff 50%,rgba(0,0,0,.25) 50%)}
.bt9{display:grid;grid-template-columns:1.5fr 1fr;gap:14px}
.pk9{background:#1d2a4a;color:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:10px}.pk9 .sm9{color:#aeb7cf}
.sp9{display:grid;grid-template-columns:1.9fr 1fr 1.3fr .7fr;gap:10px}.sp9>div{display:flex;flex-direction:column;gap:8px;align-items:center}
.sp9 .cs{display:flex;gap:4px;align-items:flex-end;height:58px}
.sp9 span{font:600 14px/1.3 'Fira Sans';color:#d6dcea;text-align:center}
.cx9{width:30px;height:52px;border-radius:4px;background:#5a4632;position:relative;overflow:hidden;flex:none}
.cx9 .fl{position:absolute;left:0;right:0;bottom:0;background:#c79a62}.cx9 .tp{position:absolute;left:11px;width:8px;top:0;bottom:0;background:rgba(255,255,255,.35);z-index:2}
.cx9 b{position:absolute;left:0;right:0;bottom:4px;text-align:center;font:700 13px/1.2 "Fira Sans";color:#fff;text-shadow:0 1px 2px rgba(0,0,0,.8);z-index:3}
.al9{background:#fff;border-radius:26px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;box-shadow:0 14px 30px rgba(29,42,74,.08);border-left:8px solid #e2533f}
.al9 .sm9{color:#b0301f}.al9 b{font:700 22px/1.3 Montserrat}.al9 p{font:500 17px/1.45 'Fira Sans';color:#3b4560;text-wrap:pretty}
""", "<div class=kk>HOSIERY WHOLESALER · RETAILER ORDERS</div><h1>Orders lost in 40 chats?<br><span>One size sheet per shop.</span></h1>",
f'''<div class=vw><div class=ct9><small>BEFORE</small>{"".join(f'<p>{a}<em>{b}</em></p>' for a, b in [("Leggings black 3 dz, XL and L mix", "Shop 1 · voice note too"), ("Same as last time but less maroon", "Shop 2 · which time?"), ("Send navy XXL, how many left?", "Shop 3 · no reply yet")])}</div>
<div class=mx9><div class=h><span class=sm9>ORDER SHEET · {SH9[0][0].upper()} · LEGGINGS · IN DOZENS · SAMPLE</span><span class=sm9>{T9} DOZEN</span></div>
<div class=g9><div class="hd" style="justify-content:flex-start">COLOUR</div>{"".join(f'<div class=hd>{s}</div>' for s in SZ9)}<div class=hd>TOTAL</div>
{"".join(f'<div class=nm><i class=sw9 style="background:{hx}"></i>{c}</div>' + "".join(f'<div class="{"sh" if short9(c, SZ9[j], q) else ("q" if q else "z")}">{q if q else "–"}</div>' for j, q in enumerate(qs)) + f'<div class=tt>{sum(qs)}</div>' for c, hx, qs in OR9)}
<div class=tl>SIZE TOTAL</div>{"".join(f'<div class=tt>{sum(qs[j] for _, _, qs in OR9)}</div>' for j in range(4))}<div class=tt style="background:#e2533f">{T9}</div></div></div>
<div class=bt9><div class=pk9><span class=sm9>PACK TODAY · 1 CARTON = {CT9} DOZEN</span><div class=sp9>{"".join(f'<div><div class=cs>{cartons9(d)}</div><span><b style="color:#fff">{n.split(" · ")[0]}</b><br>{d}&nbsp;dz<br>{pl(-(-d // CT9), "carton").replace(" ", "&nbsp;")}</span></div>' for n, d in SH9)}</div></div>
<div class=al9><span class=sm9>STOCK CHECK</span>{"".join(f'<b>{c} {s}: {q} dz asked, {h} in stock</b>' for c, s, q, h in SHORT9)}<p>The shop gets a message before packing, not after delivery.</p></div></div></div>''',
"#1d2a4a", "Sell hosiery wholesale? DM us", "background:#e2533f;color:#fff")


# ───────── 380 INDIA · Button, zip and lace shop (garment trims) · SINGLE · Crimson Text + DM Sans · ivory / charcoal / thread teal
# New technique: CSS zipper teeth (two offset repeating gradients on a tape) and CSS 4-hole buttons as the catalogue swatches;
# the phone (1 of 3 this batch) shows the shade card; the pouch list on the right is built from the same item codes.
ZP10 = [("Z-101", "#1c1c1e"), ("Z-104", "#f4f1ea"), ("Z-108", "#7a1f35"), ("Z-111", "#22325e"), ("Z-114", "#0f6e6e"), ("Z-117", "#e3a521"),
        ("Z-120", "#c2417a"), ("Z-123", "#5b3a29"), ("Z-126", "#8fa3b8"), ("Z-129", "#3f7d3a"), ("Z-132", "#d8693a"), ("Z-135", "#b9a37e")]
SEL10 = "Z-114"
def zip10(c, w="100%"): return f'<i class=zp10 style="--c:{c};width:{w}"></i>'
def btn10(c, s=34): return f'<i class=bn10 style="--c:{c};width:{s}px;height:{s}px"></i>'
PO10 = [("Sample Tailors A", "Pickup 4 PM", "Ready", [("zip", "#0f6e6e", "Z-114 · 9 in", "12"), ("btn", "#0f6e6e", "B-27 · 15 mm", "48"), ("lace", "#f4f1ea", "L-08 · cotton lace", "5 m")]),
        ("Sample Boutique B", "Pickup 5 PM", "Packing", [("zip", "#7a1f35", "Z-108 · 7 in", "20"), ("btn", "#e3a521", "B-12 · 11 mm", "60"), ("lace", "#7a1f35", "L-21 · net lace", "3 m")]),
        ("Sample Tailors C", "Delivery tomorrow", "New", [("zip", "#22325e", "Z-111 · 12 in", "10"), ("btn", "#1c1c1e", "B-03 · 20 mm", "24"), ("lace", "#e3a521", "L-15 · gota lace", "8 m")])]
def item10(k, c):
    if k == "zip": return f'<div class=ii>{zip10(c, "58px")}</div>'
    if k == "btn": return f'<div class=ii>{btn10(c, 30)}{btn10(c, 30)}</div>'
    return f'<div class=ii><i class=lc10 style="--c:{c}"></i></div>'
P["p380_trims"] = page("""
body{--f:'DM Sans';--h:'Crimson Text';background:#fbf7ef;color:#2a2a2e}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#0f6e6e;margin-top:22px}
h1{font-family:'Crimson Text';font-weight:700;font-size:72px;line-height:1.15;letter-spacing:-.5px} h1 span{color:#0f6e6e;font-style:italic}
.vw{flex:1;display:flex;gap:24px;align-items:stretch;min-height:0}
.zp10{display:block;height:18px;border-radius:3px;background:linear-gradient(var(--c),var(--c)) center/100% 4px no-repeat,
 repeating-linear-gradient(90deg,var(--c) 0 5px,transparent 5px 10px) 0 3px/100% 6px no-repeat,
 repeating-linear-gradient(90deg,transparent 0 5px,var(--c) 5px 10px) 0 9px/100% 6px no-repeat,#e7e2d7;box-shadow:inset 0 0 0 1px rgba(0,0,0,.12)}
.bn10{display:block;border-radius:50%;flex:none;background:radial-gradient(circle at 38% 38%,#fff6 0 2.5px,transparent 3px),radial-gradient(circle at 62% 38%,#fff6 0 2.5px,transparent 3px),radial-gradient(circle at 38% 62%,#fff6 0 2.5px,transparent 3px),radial-gradient(circle at 62% 62%,#fff6 0 2.5px,transparent 3px),radial-gradient(circle,var(--c) 58%,rgba(0,0,0,.25) 60%,var(--c) 66%);box-shadow:0 2px 4px rgba(0,0,0,.2)}
.lc10{display:block;width:58px;height:18px;border-radius:2px;background:radial-gradient(circle at 50% 100%,transparent 4px,var(--c) 5px) 0 0/10px 10px repeat-x,var(--c);-webkit-mask:radial-gradient(circle at 5px 18px,transparent 4px,#000 5px) 0 0/10px 100%;box-shadow:inset 0 0 0 1px rgba(0,0,0,.15)}
.ap10{flex:1;display:flex;flex-direction:column;gap:10px;padding:6px 16px 16px;background:#fbf7ef}
.ah10{display:flex;justify-content:space-between;align-items:center;margin:0 -16px;padding:10px 16px;background:#2a2a2e;color:#fff;font:700 16px/1.3 'DM Sans'}.ah10 span{font:500 13px/1.3 'DM Sans';color:#c9c4b8}
.ap10 small{font:700 12px/1.3 'DM Sans';letter-spacing:1.5px;color:#7a7568}
.sc10{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.sc10>div{background:#fff;border-radius:10px;padding:8px 8px 6px;display:flex;flex-direction:column;gap:5px;align-items:center;border:2px solid transparent}
.sc10>div.on{border-color:#0f6e6e;background:#e3f1ef}.sc10 b{font:700 13px/1.2 'DM Sans'}
.ln10{display:flex;gap:6px}.ln10 i{flex:1;text-align:center;font:600 14px/1.2 'DM Sans';font-style:normal;border:1.5px solid #d8d2c4;border-radius:10px;padding:8px 0;background:#fff}.ln10 i.on{background:#0f6e6e;border-color:#0f6e6e;color:#fff}
.qt10{display:flex;justify-content:space-between;align-items:center;background:#fff;border-radius:12px;padding:8px 12px;font:600 15px/1.2 'DM Sans'}.qt10 b{font:700 18px/1.2 'DM Sans'}
.ad10{margin-top:auto;background:#0f6e6e;color:#fff;border-radius:14px;padding:12px;text-align:center;font:700 16px/1.2 'DM Sans'}
.rt10{flex:1;display:flex;flex-direction:column;gap:12px;min-width:0}
.po10{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(42,42,46,.08)}
.po10 .h{display:flex;justify-content:space-between;align-items:center;gap:8px}.po10 .h b{font:700 24px/1.25 'Crimson Text'}.po10 .h span{display:block;font:500 14px/1.3 'DM Sans';color:#7a7568}
.po10 em{font:700 13px/1.2 'DM Sans';font-style:normal;border-radius:10px;padding:6px 10px;background:#f1ede2;color:#6b5a3c}.po10 em.rd{background:#0f6e6e;color:#fff}.po10 em.pk{background:#fbe7b5;color:#7a5600}
.po10 .r{flex:1;display:grid;grid-template-columns:76px 1fr auto;gap:10px;align-items:center;border-top:1px solid #efeae0}
.po10 .ii{display:flex;gap:4px;align-items:center}.po10 .r span{font:500 16px/1.3 'DM Sans'}.po10 .r b{font:700 17px/1.2 'DM Sans'}
.nt10{background:#2a2a2e;color:#fff;border-radius:22px;padding:14px 18px;font:500 17px/1.45 'DM Sans';text-wrap:pretty}.nt10 b{color:#f0c35a}
""", "<div class=kk>BUTTON, ZIP AND LACE SHOP · TAILOR ORDERS</div><h1>Which zip matches?<br><span>Send the shade number.</span></h1>",
f'''<div class=vw>{phone(f"""<div class=ap10><div class=ah10>Sample Trims Store<span>Zips · shade card</span></div><small>TAP A SHADE · SAMPLE</small>
<div class=sc10>{"".join(f'<div class="{"on" if z == SEL10 else ""}">{zip10(c)}<b>{z}</b></div>' for z, c in ZP10)}</div>
<small>LENGTH</small><div class=ln10>{"".join(f'<i class="{"on" if l == "9 in" else ""}">{l}</i>' for l in ["7 in", "9 in", "12 in", "18 in"])}</div><div class=qt10><span>{SEL10} · 9 in zips</span><b>12</b></div>
<small>MATCHING BUTTONS</small><div class=qt10><span style="display:flex;gap:8px;align-items:center">{btn10("#0f6e6e", 28)}B-27 · 15 mm</span><b>48</b></div>
<small>MATCHING LACE</small><div class=qt10><span style="display:flex;gap:8px;align-items:center"><i class=lc10 style="--c:#f4f1ea;width:44px"></i>L-08 · cotton lace</span><b>5 m</b></div>
<small>PICKUP</small><div class=ln10><i class=on>Today 4 PM</i><i>Tomorrow</i></div>
<div class=ad10>Add to order</div></div>""", w=352, h=820)}
<div class=rt10>{"".join(f'<div class=po10><div class=h><div><b>{n}</b><span>{t}</span></div><em class="{"rd" if s == "Ready" else ("pk" if s == "Packing" else "")}">{s}</em></div>' + "".join(f'<div class=r>{item10(k, c)}<span>{lbl}</span><b>{q}</b></div>' for k, c, lbl, q in its) + '</div>' for n, t, s, its in PO10)}
<div class=nt10>Tailors pick from the <b>same shade numbers</b> printed on your card, so the right zip is packed the first time.</div></div></div>''',
"#2a2a2e", "Run a trims shop? DM us", "background:#0f6e6e;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = [k for k in P if len(sys.argv) < 2 or any(a in k for a in sys.argv[1:])]
    asyncio.run(render(P, "work/out", keys))
