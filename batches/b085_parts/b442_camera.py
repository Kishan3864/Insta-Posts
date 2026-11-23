
# ───────── 442 INDIA · Camera and lens rental shop · CAROUSEL 5 · Anton + Roboto · matte black / gaffer yellow / studio grey
# New technique: knolling flat-lay (every kit item drawn top-down on a cutting mat with code tags, the missing item as a
# dashed red outline), item-by-day booking grid with the asked day highlighted, and same-spot pins on pickup vs return photos.
BK2 = "#17181b"; YL2 = "#f2c230"; RD2 = "#d8432f"; BG2 = "#e8e6e1"; MU2 = "#6b6b68"; GN2 = "#2e8b57"
KIT2 = [("C-01", "Camera body A", True), ("L-27", "Lens 24-70 mm", True), ("L-50", "Lens 50 mm", True), ("L-72", "Lens 70-200 mm", True),
        ("B-01", "Battery 1", True), ("B-02", "Battery 2", True), ("CH-1", "Charger", True), ("M-01", "Memory card 1", True), ("M-02", "Memory card 2", True),
        ("CP-77", "Front lens cap 77 mm", False), ("S-01", "Strap", True), ("BG-1", "Camera bag", True)]
OUT2 = len(KIT2); BACK2 = sum(k[2] for k in KIT2); MISS2 = [k for k in KIT2 if not k[2]]
def mat2():
    grid = "".join(f'<path d="M{x} 0 V600" stroke="#2b2d33" stroke-width="1"/>' for x in range(30, 900, 60)) + "".join(f'<path d="M0 {y} H900" stroke="#2b2d33" stroke-width="1"/>' for y in range(30, 600, 60))
    def tag(x, y, t, miss=False):
        w = len(t) * 11 + 22
        return f'<rect x="{x - w / 2:.0f}" y="{y}" width="{w}" height="26" rx="6" fill="{RD2 if miss else YL2}"/><text x="{x}" y="{y + 19}" text-anchor="middle" font-family="Roboto" font-weight="700" font-size="16" fill="{"#fff" if miss else BK2}"><tspan>{t}</tspan></text>'
    def lens(x, y, L, H=78, lbl=""):
        rings = "".join(f'<rect x="{x + 22 + i * (L - 50) / 5:.0f}" y="{y}" width="{(L - 50) / 10:.0f}" height="{H}" fill="#2a2b30"/>' for i in range(5))
        return (f'<rect x="{x}" y="{y + 12}" width="24" height="{H - 24}" rx="4" fill="#55575e"/><rect x="{x + 20}" y="{y}" width="{L - 20}" height="{H}" rx="10" fill="#3b3d44"/>{rings}'
                f'<rect x="{x + L - 16}" y="{y - 4}" width="16" height="{H + 8}" rx="6" fill="#4a4c53"/><rect x="{x + L * .45:.0f}" y="{y + H / 2 - 3:.0f}" width="{L * .2:.0f}" height="6" rx="3" fill="#8d8f96"/>')
    body = (f'<path d="M120 64 L140 40 H220 L240 64 Z" fill="#3b3d44"/><rect x="40" y="62" width="280" height="150" rx="20" fill="#3b3d44"/><rect x="40" y="62" width="58" height="150" rx="20" fill="#2a2b30"/>'
            f'<circle cx="186" cy="140" r="56" fill="#2a2b30"/><circle cx="186" cy="140" r="42" fill="#55575e"/><circle cx="186" cy="140" r="30" fill="#1f2024"/><circle cx="70" cy="54" r="12" fill="#55575e"/><circle cx="286" cy="84" r="8" fill="{RD2}"/>')
    bat = lambda x: f'<rect x="{x}" y="300" width="70" height="104" rx="8" fill="#3b3d44"/><rect x="{x + 14}" y="292" width="14" height="10" fill="#8d8f96"/><rect x="{x + 42}" y="292" width="14" height="10" fill="#8d8f96"/><rect x="{x + 12}" y="330" width="46" height="8" rx="4" fill="#55575e"/>'
    card = lambda x: f'<path d="M{x} 316 L{x + 14} 302 H{x + 64} V398 H{x} Z" fill="#4a4c53"/><rect x="{x + 10}" y="330" width="44" height="40" rx="4" fill="{YL2}" opacity=".85"/>'
    strap = f'<path d="M40 500 C120 460, 200 540, 280 500 S440 460, 500 500" stroke="#3b3d44" stroke-width="26" fill="none" stroke-linecap="round"/><path d="M40 500 C120 460, 200 540, 280 500 S440 460, 500 500" stroke="#55575e" stroke-width="2" stroke-dasharray="8 8" fill="none"/>'
    bag = f'<rect x="570" y="446" width="290" height="124" rx="18" fill="#3b3d44"/><path d="M570 476 Q570 446 600 446 H830 Q860 446 860 476 V506 H570 Z" fill="#2a2b30"/><rect x="694" y="494" width="42" height="24" rx="5" fill="#8d8f96"/>'
    charger = f'<rect x="230" y="306" width="118" height="92" rx="12" fill="#3b3d44"/><rect x="250" y="324" width="78" height="44" rx="6" fill="#2a2b30"/><circle cx="318" cy="384" r="5" fill="{GN2}"/>'
    cap = f'<circle cx="640" cy="352" r="52" fill="none" stroke="{RD2}" stroke-width="4" stroke-dasharray="10 8"/><text x="640" y="368" text-anchor="middle" font-family="Anton" font-size="46" fill="{RD2}"><tspan>?</tspan></text>'
    tags = (tag(180, 226, "C-01") + tag(822, 86, "L-72") + tag(490, 256, "L-27") + tag(730, 256, "L-50") + tag(110, 414, "B-01 · B-02") + tag(289, 414, "CH-1")
            + tag(475, 414, "M-01 · M-02") + tag(640, 414, "CP-77 missing", True) + tag(270, 540, "S-01") + tag(715, 532, "BG-1"))
    return (f'<svg viewBox="0 0 900 600" style="position:absolute;inset:0;width:100%;height:100%"><rect width="900" height="600" fill="#1f2025"/>{grid}{body}'
            f'{lens(370, 56, 390)}{lens(370, 172, 240)}{lens(660, 172, 140)}{bat(40)}{bat(130)}{charger}{card(400)}{card(480)}{cap}{strap}{bag}{tags}</svg>')

B2 = f"""
body{{--f:'Roboto';--h:'Anton';background:{BG2};color:{BK2}}}
.kk2{{font:700 16px/1.5 'Roboto';letter-spacing:3px;color:{MU2};margin-top:22px;display:flex;align-items:center;gap:10px}}.kk2 i{{width:28px;height:10px;background:{YL2};border-radius:2px}}
h1{{font-family:'Anton';font-weight:400;font-size:72px;line-height:1.25;letter-spacing:.3px;margin-top:22px}} h1 span{{background:linear-gradient(transparent 62%,{YL2} 62%,{YL2} 92%,transparent 92%)}}
.sm2{{font:700 13px/1.5 'Roboto';letter-spacing:2px;color:{MU2}}}
.cd2{{background:#fff;border-radius:20px;box-shadow:0 14px 30px rgba(23,24,27,.08)}}
.dk2{{background:{BK2};color:#fff;border-radius:20px}}.dk2 .sm2{{color:#a9aaa6}}
.ok2{{color:{GN2}!important}}.no2{{color:{RD2}!important}}
"""
def t2(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{BK2};color:{YL2}"):
    return page(B2 + css, f"<div class=kk2><i></i>{kick}</div><h1>{head}</h1>", vis, BK2, cta, ctacss, tagline=f"{n} / 5")

QS2 = [("“Which lens went to whom?”", "Ask around the shop"), ("“Was that mark there before?”", "No photo, just an argument"), ("“Is the kit free on Saturday?”", "Check the notebook")]
P["p442_cam_s1"] = t2(1, "CAMERA AND LENS RENTAL", "Kit back, one cap missing?<br><span>Check every piece out and in.</span>",
f'''<div class=w21><div class="dk2 mt"><span class=sm2>RENTAL R-207 · {OUT2} ITEMS OUT · {BACK2} BACK · SAMPLE</span><div class=im>{mat2()}</div></div>
<div class=qs>{"".join(f'<div class="cd2 q"><p>{a}</p><em>{b}</em></div>' for a, b in QS2)}</div></div>''',
css=f""".w21{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.mt{{flex:1;min-height:0;padding:16px 20px 20px;display:flex;flex-direction:column;gap:10px}}.mt .im{{flex:1;min-height:0;position:relative;border-radius:12px;overflow:hidden}}
.qs{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.qs .q{{padding:18px 20px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}.qs p{{font:700 22px/1.35 'Roboto'}}.qs em{{align-self:flex-start;font:700 15px/1.3 'Roboto';font-style:normal;background:{BG2};border-radius:8px;padding:7px 10px;color:{MU2}}}""")

P["p442_cam_s2"] = t2(2, "1 · KIT CHECKLIST", "Every item ticked at pickup,<br><span>every item ticked at return.</span>",
f'''<div class=w22><div class="cd2 tb"><div class="r h"><span>CODE</span><span>ITEM</span><span>OUT</span><span>BACK</span></div>{"".join(f'<div class="r{"" if b else " miss"}"><b>{c}</b><span>{n}</span><i class=ok2>✓</i><i class="{"ok2" if b else "no2"}">{"✓" if b else "✗"}</i></div>' for c, n, b in KIT2)}</div>
<div class=sd><div class="dk2 k"><span class=sm2>R-207 · SAMPLE CUSTOMER R</span><div class=tt><div><span>Out</span><b>Fri 20 Nov · 6 PM</b></div><div><span>Back</span><b>Mon 23 Nov · 11 AM</b></div></div>
<div class=ct><div><b>{OUT2}</b><span>out</span></div><div><b>{BACK2}</b><span>back</span></div><div class=m><b>{len(MISS2)}</b><span>missing</span></div></div></div>
<div class="cd2 sg"><span class=sm2>SIGNED ON THE PHONE</span><div class=sr><span class=ok2>✓</span>At pickup by the customer</div><div class=sr><span class=ok2>✓</span>At return by your staff</div></div>
<div class="cd2 ms"><span class=sm2>MESSAGES · MON 23 NOV</span><div class=bb>Your kit is back, thank you. One item is missing: {MISS2[0][1].lower()} ({MISS2[0][0]}). Please bring it on your next visit.<small>Sample message · 11:05 AM</small></div><div class="bb cu">Sorry, it is in my other bag. I will drop it on Tue&nbsp;24&nbsp;Nov.<small>Customer · 11:20 AM</small></div><div class=bb>Thank you. We have marked it for Tue&nbsp;24&nbsp;Nov.<small>Your shop · 11:22 AM</small></div></div></div></div>''',
css=f""".w22{{flex:1;display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,.85fr);gap:16px;min-height:0}}
.tb{{padding:14px 20px;display:flex;flex-direction:column}}.tb .r{{flex:1;display:grid;grid-template-columns:78px 1fr 52px 52px;gap:8px;align-items:center;border-top:1px solid #eceae5;padding:0 6px}}.tb .h{{flex:none;border:0;padding-bottom:8px}}.tb .h span{{font:700 13px/1.4 'Roboto';letter-spacing:1px;color:{MU2}}}
.tb .r b{{font:700 17px/1.3 'Roboto';color:{MU2}}}.tb .r>span{{font:500 19px/1.3 'Roboto'}}.tb .r i{{font:900 22px/1.3 'Roboto';font-style:normal;text-align:center}}.tb .r.miss{{background:#fbe6e2;border-radius:10px}}.tb .r.miss>span{{font-weight:700;color:{RD2}}}
.sd{{display:flex;flex-direction:column;gap:14px}}.sd .k{{padding:18px 20px;display:flex;flex-direction:column;gap:12px}}.tt{{display:flex;flex-direction:column;gap:6px}}.tt div{{display:flex;justify-content:space-between;font:500 17px/1.4 'Roboto'}}.tt span{{color:#a9aaa6}}
.ct{{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}}.ct div{{background:#2a2b30;border-radius:12px;padding:8px 10px;display:flex;align-items:baseline;gap:6px}}.ct b{{font:400 40px/1.5 Anton;color:{YL2}}}.ct span{{font:500 15px/1.3 'Roboto';color:#d6d6d2}}.ct .m b{{color:#ff7a66}}
.sg{{padding:16px 20px;display:flex;flex-direction:column;gap:8px}}.sr{{font:600 18px/1.35 'Roboto';display:flex;gap:10px}}.sr span{{font-weight:900}}
.ms{{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:10px;justify-content:space-between}}.bb.cu{{background:#eceae5;border-radius:16px 16px 4px 16px;margin-left:30px}}.bb{{background:#fff5d1;border-radius:16px 16px 16px 4px;padding:14px 16px;font:500 18px/1.45 'Roboto';display:flex;flex-direction:column;gap:6px}}.bb small{{font:500 13px/1.3 'Roboto';color:{MU2}}}""")

DAYS2 = ["Mon 23", "Tue 24", "Wed 25", "Thu 26", "Fri 27", "Sat 28", "Sun 29"]
ITEMS2 = ["Camera body A", "Camera body B", "Lens 24-70 mm", "Lens 50 mm", "Lens 70-200 mm", "Gimbal", "Light kit"]
BOOK2 = [("Camera body A", 1, 1, "R-207 back"), ("Camera body A", 3, 4, "R-209"), ("Camera body B", 1, 2, "R-208"), ("Camera body B", 6, 7, "R-213"),
         ("Lens 24-70 mm", 1, 1, "R-207 back"), ("Lens 24-70 mm", 3, 4, "R-209"), ("Lens 50 mm", 1, 1, "R-207 back"), ("Lens 70-200 mm", 1, 1, "R-207 back"), ("Lens 70-200 mm", 5, 7, "R-210"),
         ("Gimbal", 2, 3, "R-211"), ("Gimbal", 6, 6, "R-214"), ("Light kit", 5, 6, "R-212")]
ASK2 = 6; WANT2 = ["Camera body A", "Lens 24-70 mm", "Lens 50 mm", "Lens 70-200 mm"]
def busy2(it, d): return any(b[0] == it and b[1] <= d <= b[2] for b in BOOK2)
def calgrid2():
    cells = "".join(f'<div class="dh{" ask" if i + 1 == ASK2 else ""}">{d}</div>' for i, d in enumerate(DAYS2))
    hl = f'<div class=hl style="grid-column:{ASK2 + 1};grid-row:1 / span {len(ITEMS2) + 1}"></div>'
    rows = ""
    for r, it in enumerate(ITEMS2, 2):
        rows += f'<div class=il style="grid-row:{r}">{it}</div>'
        for it2, a, b, c in BOOK2:
            if it2 == it:
                rows += f'<div class="bk{" rt" if "back" in c else ""}" style="grid-row:{r};grid-column:{a + 1} / {b + 2}">{c}</div>'
    return f'<div class=cg><div class=c0></div>{cells}{hl}{rows}</div>'
FREE2 = [w for w in WANT2 if not busy2(w, ASK2)]; BUSY2 = [w for w in WANT2 if busy2(w, ASK2)]
P["p442_cam_s3"] = t2(3, "2 · BOOKING CALENDAR", "“Free on Saturday?”<br><span>Answer in one look.</span>",
f'''<div class=w23><div class="cd2 cl"><span class=sm2>EVERY ITEM · MON 23 TO SUN 29 NOV · SAMPLE</span>{calgrid2()}</div>
<div class=bt><div class="cd2 qq"><span class=sm2>CUSTOMER ASKS · FULL KIT FOR {DAYS2[ASK2 - 1].upper()} NOV</span><div class=ls>{"".join(f'<div><i class={"ok2" if w in FREE2 else "no2"}>{"✓" if w in FREE2 else "✗"}</i>{w}<em class={"ok2" if w in FREE2 else "no2"}>{"free" if w in FREE2 else "booked"}</em></div>' for w in WANT2)}</div></div>
<div class="dk2 an"><span class=sm2>YOUR REPLY</span><p>{len(FREE2)} of {len(WANT2)} items are free. The {BUSY2[0].lower().replace("lens ", "")} lens is booked, so we offer it for Mon 30 Nov or the rest of the kit for Saturday.</p></div></div></div>''',
css=f""".w23{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.cl{{flex:1;min-height:0;padding:18px 20px;display:flex;flex-direction:column;gap:10px}}
.cg{{flex:1;display:grid;grid-template-columns:190px repeat(7,1fr);grid-template-rows:auto repeat({len(ITEMS2)},1fr);gap:6px 6px;position:relative}}
.cg .dh{{grid-row:1;font:700 15px/1.4 'Roboto';text-align:center;padding:6px 0;color:{MU2};z-index:1}}.cg .dh.ask{{color:{BK2}}}.cg .hl{{background:#fff3c4;border-radius:12px;border:2px solid {YL2}}}
.cg .il{{grid-column:1;font:600 18px/1.3 'Roboto';align-self:center}}.cg .bk{{background:{BK2};color:#fff;border-radius:10px;font:700 15px/1.3 'Roboto';display:flex;align-items:center;padding:0 12px;z-index:1;margin:4px 0}}.cg .bk.rt{{background:#c9c7c1;color:{BK2}}}
.bt{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px}}.qq{{padding:16px 20px;display:flex;flex-direction:column;gap:8px}}.ls div{{display:flex;align-items:center;gap:10px;font:600 18px/1.3 'Roboto';padding:5px 0;border-top:1px solid #eceae5}}.ls i{{font:900 20px/1.3 'Roboto';font-style:normal;width:20px}}.ls em{{margin-left:auto;font:700 15px/1.3 'Roboto';font-style:normal}}
.an{{padding:18px 22px;display:flex;flex-direction:column;gap:10px}}.an p{{font:500 20px/1.5 'Roboto'}}""")

def back2(pins):
    p = "".join(f'<circle cx="{x}" cy="{y}" r="17" fill="{c}" stroke="#fff" stroke-width="3"/><text x="{x}" y="{y + 7}" text-anchor="middle" font-family="Roboto" font-weight="900" font-size="19" fill="#fff"><tspan>{n}</tspan></text>' for n, x, y, c in pins)
    return f'''<svg viewBox="22 26 356 238" style="display:block;width:100%;height:auto"><rect width="400" height="290" rx="14" fill="#efede8"/>
<rect x="40" y="70" width="320" height="180" rx="22" fill="#3b3d44"/><rect x="70" y="40" width="80" height="40" rx="8" fill="#2a2b30"/><rect x="66" y="96" width="196" height="132" rx="8" fill="#20232a"/><rect x="76" y="106" width="176" height="112" rx="4" fill="#2c3440"/>
<circle cx="310" cy="120" r="20" fill="#55575e"/><circle cx="310" cy="120" r="8" fill="#2a2b30"/><circle cx="290" cy="176" r="9" fill="#55575e"/><circle cx="324" cy="176" r="9" fill="#55575e"/><circle cx="290" cy="208" r="9" fill="#55575e"/><circle cx="324" cy="208" r="9" fill="#55575e"/>
<path d="M116 241 l26 -4" stroke="#c9c6be" stroke-width="3.5" stroke-linecap="round"/><ellipse cx="129" cy="239" rx="22" ry="10" fill="none" stroke="#d8432f" stroke-width="2.5"/>{p}</svg>'''
PINS2 = [("1", 66, 238, RD2), ("2", 164, 162, BK2), ("3", 310, 120, BK2)]
CHK2 = [("1", "Small mark, bottom left", "There at pickup too, so no charge", True), ("2", "Screen", "Clean at pickup, clean at return", True), ("3", "Main dial", "Turns well at both checks", True)]
TL2 = [("Wed 18 Nov", "Booked online"), ("Fri 20 Nov · 6 PM", "Photo ID checked, photos taken"), ("Mon 23 Nov · 11 AM", "Back, photos at the same spots"), ("Mon 23 Nov · 11:05 AM", "1 item missing, message sent")]
P["p442_cam_s4"] = t2(4, "3 · PICKUP AND RETURN PHOTOS", "Same spots, two photos.<br><span>No argument about marks.</span>",
f'''<div class=w24><div class=ph>{"".join(f'<div class="cd2 fr"><span class=sm2>{t}</span>{back2(PINS2)}</div>' for t in ["PICKUP · FRI 20 NOV · 6 PM", "RETURN · MON 23 NOV · 11 AM"])}</div>
<div class=bt><div class="cd2 ck">{"".join(f'<div class=r><u>{n}</u><div><b>{a}</b><span>{b}</span></div><i class=ok2>✓</i></div>' for n, a, b, ok in CHK2)}</div>
<div class="dk2 tl"><span class=sm2>R-207 · SAMPLE</span>{"".join(f'<div class=t><i></i><div><b>{a}</b><span>{b}</span></div></div>' for a, b in TL2)}</div></div></div>''',
css=f""".w24{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.ph{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}.fr{{padding:14px 16px 16px;display:flex;flex-direction:column;gap:8px}}
.bt{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:16px;min-height:0}}.ck{{padding:12px 20px;display:flex;flex-direction:column}}.ck .r{{flex:1;display:grid;grid-template-columns:40px 1fr 26px;gap:12px;align-items:center;border-top:1px solid #eceae5}}.ck .r:first-child{{border:0}}
.ck u{{text-decoration:none;width:36px;height:36px;border-radius:50%;background:{BK2};color:#fff;display:flex;align-items:center;justify-content:center;font:900 18px/1 'Roboto'}}.ck .r:first-child u{{background:{RD2}}}.ck b{{display:block;font:700 24px/1.35 'Roboto'}}.ck span{{font:500 19px/1.4 'Roboto';color:{MU2}}}.ck i{{font:900 24px/1 'Roboto';font-style:normal}}
.tl{{padding:16px 22px;display:flex;flex-direction:column;justify-content:space-between}}.tl .t{{display:flex;gap:14px;align-items:flex-start;position:relative}}.tl .t>i{{width:16px;height:16px;border-radius:50%;background:{YL2};margin-top:4px;flex:none}}.tl .t:last-child>i{{background:#ff7a66}}.tl b{{display:block;font:700 17px/1.35 'Roboto';color:{YL2}}}.tl .t:last-child b{{color:#ff9b8a}}.tl span{{font:500 18px/1.4 'Roboto'}}""")

P["p442_cam_s5"] = t2(5, "CAMERA RENTAL APP", "Rent out cameras?<br><span>Let's build your rental app.</span>",
f'''<div class=w25><div class=tl>{"".join(f'<div class=cd2><span class=ib>{ic(i, 40)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("check", "Kit checklist", "Ticked out and in"), ("cal", "Item calendar", "Free or booked, by day"), ("camera", "Pickup photos", "Same spots at return"), ("chat", "Return message", "Sent in one tap")])}</div>
<div class="dk2 q"><span class=sm2>A QUESTION FOR RENTAL SHOPS</span><p>Which small item goes missing most often from your kits? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{YL2};color:{BK2}",
css=f""".w25{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.w25 .tl{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.w25 .tl>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center}}.w25 .ib{{width:86px;height:86px;border-radius:22px;background:{YL2};color:{BK2}}}.w25 .tl b{{font:400 40px/1.5 Anton}}.w25 .tl>div>span:last-child{{font:500 23px/1.4 'Roboto';color:{MU2}}}
.q{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q p{{font:700 29px/1.4 'Roboto';text-wrap:pretty}}""")
