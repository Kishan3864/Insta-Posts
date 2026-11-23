
# ───────── 446 INDIA · Fuel station (shift closing) · SINGLE · Poppins + Open Sans · canopy navy / meter amber / concrete grey
# New technique: CSS fuel dispensers with LCD totalizer windows per nozzle (open → close), litres computed per nozzle and
# matched against underground tank dip gauges for the same shift.
NV6 = "#1d2b44"; AM6 = "#f2a71b"; CG6 = "#e9eaec"; MU6 = "#646d7a"; PT6 = "#2f80c1"; DS6 = "#3f9b6a"
NZ6 = [("N1", "Petrol", 482310.5, 483126.0, "Attendant 1"), ("N2", "Diesel", 610442.0, 611708.5, "Attendant 1"),
       ("N3", "Petrol", 377905.0, 378520.5, "Attendant 2"), ("N4", "Diesel", 291118.5, 292010.0, "Attendant 2")]
SOLD6 = {f: sum(c - o for _, ff, o, c, _ in NZ6 if ff == f) for f in ("Petrol", "Diesel")}
TK6 = [("T1", "Petrol", 15000, 9840, 8415), ("T2", "Diesel", 20000, 14200, 12046)]
def disp6(a, b, k):
    def lcd(n, f, o, c, who):
        return f'''<div class=lcd><div class=hd><b class="{f.lower()}">{n} · {f}</b><span>{who}</span></div><div class=rd><span>Open</span><code>{o:,.1f}</code></div><div class=rd><span>Close</span><code>{c:,.1f}</code></div><div class="rd sold"><span>Sold</span><strong>{c - o:,.1f} L</strong></div></div>'''
    return f'''<div class=dp6><div class=top>DISPENSER {k}</div><div class=body>{lcd(*a)}{lcd(*b)}</div><div class=hs><i class="{a[1].lower()}"></i><i class="{b[1].lower()}"></i></div><div class=base></div></div>'''
def tank6(t, f, cap, op, cl):
    out = op - cl; diff = out - SOLD6[f]
    return f'''<div class="cd6 tk"><div class=gx><div class=g><i style="height:{op / cap * 100:.1f}%" class=op></i><i style="height:{cl / cap * 100:.1f}%" class="cl {f.lower()}"></i></div></div>
<div class=tx><span class=sm6>{t} · {f.upper()} TANK · DIP</span><div class=r><span>Start of shift</span><b>{op:,} L</b></div><div class=r><span>End of shift</span><b>{cl:,} L</b></div><div class=r><span>Out of the tank</span><b>{out:,.0f} L</b></div><div class=r><span>Sold at nozzles</span><b>{SOLD6[f]:,.1f} L</b></div><div class=r><span>Water in tank</span><b>None found</b></div><div class=ok>Difference {abs(diff):.0f} L · within your limit</div></div></div>'''
P["p446_fuel"] = page(f"""
body{{--f:'Open Sans';--h:'Poppins';background:{CG6};color:{NV6}}}
.kk6{{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#b8770a;margin-top:22px}}
h1{{font-family:'Poppins';font-weight:800;font-size:54px;line-height:1.2;letter-spacing:-1.4px;margin-top:12px}} h1 span{{color:{PT6}}}
.w6{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm6{{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:{MU6}}}
.cd6{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(29,43,68,.08)}}
.ds6{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.dp6{{display:flex;flex-direction:column;align-items:stretch}}.dp6 .top{{background:{NV6};color:#fff;border-radius:18px 18px 0 0;padding:10px 16px;font:700 14px/1.4 'Open Sans';letter-spacing:3px;text-align:center}}
.dp6 .body{{background:#f7f8fa;border-left:6px solid {NV6};border-right:6px solid {NV6};padding:14px;display:grid;grid-template-columns:1fr 1fr;gap:12px}}
.dp6 .hs{{background:#f7f8fa;border-left:6px solid {NV6};border-right:6px solid {NV6};display:flex;justify-content:space-around;padding:2px 0 12px}}.dp6 .hs i{{width:46px;height:22px;border-radius:0 0 12px 12px}}.dp6 .base{{height:18px;background:#9aa1ab;border-radius:0 0 10px 10px}}
i.petrol,b.petrol{{background:{PT6}}}i.diesel,b.diesel{{background:{DS6}}}
.lcd{{background:#16202f;border-radius:12px;padding:10px 12px;display:flex;flex-direction:column;gap:5px;color:#fff}}.lcd .hd{{display:flex;flex-direction:column;gap:3px;margin-bottom:2px}}.lcd .hd b{{align-self:flex-start;font:700 14px/1.3 'Open Sans';padding:2px 8px;border-radius:6px}}.lcd .hd span{{font:500 12px/1.3 'Open Sans';color:#9fb0c6}}
.lcd .rd{{display:flex;justify-content:space-between;align-items:baseline;gap:6px}}.lcd .rd span{{font:500 13px/1.3 'Open Sans';color:#9fb0c6}}.lcd code{{font:600 16px/1.3 'DejaVu Sans Mono',monospace;color:{AM6}}}
.lcd .sold{{border-top:1px dashed #3a4a63;padding-top:5px}}.lcd .sold strong{{font:800 18px/1.3 Poppins;color:#fff}}
.bt6{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:16px;min-height:0}}
.tk{{padding:16px 18px;display:flex;gap:16px}}.tk .gx{{width:70px;flex:none;display:flex}}.tk .g{{flex:1;border:4px solid {NV6};border-radius:16px;position:relative;overflow:hidden;background:#f2f3f5}}.tk .g i{{position:absolute;left:0;right:0;bottom:0}}.tk .g i.op{{background:#d9dde3;border-top:3px dashed {MU6}}}.tk .g i.cl{{opacity:.9}}
.tk .tx{{flex:1;display:flex;flex-direction:column;justify-content:space-between;gap:6px}}.tk .r{{display:flex;justify-content:space-between;font:500 20px/1.35 'Open Sans';border-top:1px solid #eceef1;padding-top:8px}}.tk .r b{{font:700 21px/1.35 'Open Sans'}}
.tk .ok{{background:#e3f3ea;color:#22693f;border-radius:10px;padding:10px 12px;font:700 17px/1.35 'Open Sans'}}
.sx6{{background:{NV6};color:#fff;border-radius:22px;padding:14px 22px;display:flex;align-items:center;justify-content:space-between;gap:16px}}.sx6 .sm6{{color:#9fb0c6}}.sx6 b{{display:block;font:700 19px/1.35 'Open Sans'}}.sx6 .k{{display:flex;gap:10px}}.sx6 .k div{{background:#2b3c5a;border-radius:12px;padding:8px 14px;display:flex;flex-direction:column}}.sx6 .k span{{display:block;font:600 13px/1.4 'Open Sans';color:#c9d4e3;margin-bottom:6px}}.sx6 .k strong{{display:block;font:800 22px/1.4 Poppins;color:{AM6}}}
""", "<div class=kk6>FUEL STATION · SHIFT CLOSING</div><h1>Shift closing on a calculator?<br><span>Every nozzle matched to a tank.</span></h1>",
f'''<div class=w6><div class=ds6>{disp6(NZ6[0], NZ6[1], 1)}{disp6(NZ6[2], NZ6[3], 2)}</div>
<div class=sx6><div><span class=sm6>SHIFT A · MON 23 NOV · 6 AM TO 2 PM · SAMPLE</span><b>Closed at 2:05 PM, handed to Shift B</b></div><div class=k><div><span>Petrol sold</span><strong>{SOLD6["Petrol"]:,.1f} L</strong></div><div><span>Diesel sold</span><strong>{SOLD6["Diesel"]:,.1f} L</strong></div></div></div>
<div class=bt6>{"".join(tank6(*t) for t in TK6)}</div></div>''',
NV6, "Run a fuel station? DM us", f"background:{AM6};color:{NV6}")
