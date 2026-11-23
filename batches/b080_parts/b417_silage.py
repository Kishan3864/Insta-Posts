
# ───────── 417 INDIA · Silage bale maker · SINGLE · Archivo Black + Roboto · straw cream / bale black / tractor blue
# New technique: wrapped-bale isotype (end view with film overlap lines and shine; 1 icon = 5 bales) where booked icons
# are tinted from the order list, a trolley-trip strip derived from orders (40 bales per trip), and a stock-check reply.
S7 = "#f5eed8"; K7 = "#17191c"; B7 = "#2f6fb5"; Y7 = "#e2b93b"
STOCK7 = 600; TRIP7 = 40
OR7 = [("Sample Dairy A", 120, "Wed 25 Nov"), ("Sample Dairy B", 80, "Thu 26 Nov"), ("Sample Dairy C", 100, "Fri 27 Nov"), ("Sample Dairy D", 50, "Sat 28 Nov"), ("Sample Dairy E", 30, "Sat 28 Nov")]
BOOK7 = sum(o[1] for o in OR7); FREE7 = STOCK7 - BOOK7
DAYS7 = {}
for n, q, d in OR7: DAYS7[d] = DAYS7.get(d, 0) + q
ASK7 = 250
def bale7(booked):
    body = B7 if booked else "#22262b"
    return f'''<svg viewBox="0 0 60 60" width="100%" style="display:block"><circle cx="30" cy="31" r="27" fill="#0c0d0f" opacity=".18"/><circle cx="30" cy="29" r="27" fill="{body}"/>
<path d="M8 20 Q30 8 52 20 M5 32 Q30 20 55 32 M9 44 Q30 33 51 44" stroke="#ffffff" stroke-opacity=".16" stroke-width="2.2" fill="none"/><ellipse cx="20" cy="17" rx="9" ry="4" fill="#fff" opacity=".28" transform="rotate(-25 20 17)"/></svg>'''
P["p417_silage"] = page(f"""
body{{--f:'Roboto';--h:'Archivo Black';background:{S7};color:{K7}}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{B7};margin-top:22px}}
h1{{font-family:'Archivo Black';font-weight:400;font-size:60px;line-height:1.22;letter-spacing:-1px;margin-top:20px}} h1 span{{color:{B7}}}
.vw7{{flex:1;display:grid;grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr);gap:16px;min-height:0}}
.sm7{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#7a7463}}
.cd7{{background:#fffbf0;border-radius:24px;box-shadow:0 14px 30px rgba(60,50,20,.09);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.lf7{{display:flex;flex-direction:column;gap:16px;min-height:0}}.yd7{{flex:1;min-height:0}}
.gr7{{flex:1;display:grid;grid-template-columns:repeat(10,1fr);gap:6px 8px;align-content:space-evenly;background:repeating-linear-gradient(90deg,#efe1b4 0 8px,#e8d8a4 8px 16px);border-radius:14px;padding:12px}}
.lgd7{{display:flex;gap:18px;align-items:center;font:600 16px/1.3 Roboto}}.lgd7 i{{display:inline-block;width:18px;height:18px;border-radius:50%;margin-right:6px;vertical-align:-3px}}
.ct7{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.ct7 div{{background:#f1e6c6;border-radius:14px;padding:10px 14px}}.ct7 b{{display:block;font:400 34px/1.35 'Archivo Black'}}.ct7 span{{font:600 15px/1.3 Roboto;color:#6b6553}}.ct7 .bk b{{color:{B7}}}
.tp7{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.tp7 div{{background:{K7};color:#fff;border-radius:16px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}}.tp7 span{{font:600 14px/1.3 Roboto;color:#c9c3b0}}.tp7 b{{font:400 24px/1.35 'Archivo Black';color:{Y7}}}.tp7 em{{font:600 15px/1.3 Roboto;font-style:normal}}
.rt7{{display:flex;flex-direction:column;gap:16px;min-height:0}}.ol7{{flex:1}}
.ol7 .r{{flex:1;display:grid;grid-template-columns:1fr 56px;gap:4px 10px;align-items:center;border-top:1px solid #ece1c2;padding:4px 0}}.ol7 .r b{{font:700 19px/1.3 Roboto}}.ol7 .r strong{{font:400 24px/1.35 'Archivo Black';text-align:right;color:{B7}}}.ol7 .r span{{font:500 15px/1.3 Roboto;color:#6b6553}}
.ol7 .tt{{display:flex;justify-content:space-between;align-items:center;background:#e3ecf7;border-radius:12px;padding:10px 14px}}.ol7 .tt span{{font:700 16px/1.3 Roboto}}.ol7 .tt b{{font:400 26px/1.35 'Archivo Black';color:{B7}}}
.nw7{{background:{K7};color:#fff;border-radius:24px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}}.nw7 .sm7{{color:#c9c3b0}}.nw7 p{{font:500 19px/1.45 Roboto;text-wrap:pretty}}.nw7 p b{{color:{Y7}}}
""", "<div class=kk>SILAGE BALE MAKER · DAIRY FARM ORDERS</div><h1>Silage bookings on calls?<br><span>Stock and orders, one board.</span></h1>",
f'''<div class=vw7><div class=lf7><div class="cd7 yd7"><div style="display:flex;justify-content:space-between;align-items:center"><span class=sm7>YARD · TUE 24 NOV · SAMPLE</span><span class=lgd7><span><i style="background:{B7}"></i>Booked</span><span><i style="background:#22262b"></i>Free</span></span></div>
<div class=gr7>{"".join(bale7(k < BOOK7 // 5) for k in range(STOCK7 // 5))}</div>
<div class=ct7><div><b>{STOCK7}</b><span>bales in the yard</span></div><div class=bk><b>{BOOK7}</b><span>booked</span></div><div><b>{FREE7}</b><span>free to sell</span></div></div><span class=sm7>1 BALE ICON = 5 BALES</span></div>
<div class=tp7>{"".join(f'<div><span>{d[:3]} {d[4:]}</span><b>{q}</b><em>{pl(math.ceil(q / TRIP7), "trolley trip")}</em></div>' for d, q in DAYS7.items())}</div></div>
<div class=rt7><div class="cd7 ol7"><span class=sm7>ORDERS THIS WEEK</span>{"".join(f'<div class=r><b>{n}</b><strong>{q}</strong><span>{d}</span></div>' for n, q, d in OR7)}<div class=tt><span>Booked</span><b>{BOOK7} bales</b></div></div>
<div class=nw7><span class=sm7>NEW CALL · SAMPLE DAIRY F</span><p>Wants <b>{ASK7}</b> bales on Saturday. Free stock is <b>{FREE7}</b>. Offer {FREE7} now and {ASK7 - FREE7} from the next batch.</p></div></div></div>''',
K7, "Make silage bales? DM us", f"background:{B7};color:#fff")
