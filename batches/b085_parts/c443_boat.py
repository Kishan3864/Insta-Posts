
# ───────── 443 INDIA · Fishing boat owner (trip accounts) · SINGLE · Bitter + Fira Sans · sea navy / ice white / buoy orange
# New technique: top-down boat SVG whose fish hold is split into compartments sized and filled from the trip's catch list
# (seeded fish in each hold), tied to a buyer list derived from the same catch.
NV3 = "#12324d"; OR3 = "#ee7a2b"; TL3 = "#2a9d8f"; BG3 = "#eaf2f6"; MU3 = "#5b6d7a"
CATCH3 = [("Sardine", 610, "#7fb3d5"), ("Mackerel", 420, "#5f9ea0"), ("Mixed fish", 230, "#9fb8c8"), ("Squid", 140, "#d9a6b3"), ("Prawns", 85, "#f0a77a"), ("Seer fish", 60, "#8aa5c2")]
TOT3 = sum(c[1] for c in CATCH3)
KG3 = {c[0]: c[1] for c in CATCH3}
SALE3 = [("Sample Agent A", ["Sardine"], "Paid"), ("Sample Agent B", ["Mackerel"], "To collect Wed 25 Nov"), ("Sample Exporter C", ["Squid", "Prawns"], "Paid"),
         ("Sample Hotel Buyer D", ["Seer fish"], "Paid"), ("Local market", ["Mixed fish"], "Paid")]
assert sorted(sum((s[1] for s in SALE3), [])) == sorted(KG3)
def boat3():
    rnd = random.Random(443)
    holds = ""; x0 = 250; W = 520; cols = 3; cw = W / cols
    for i, (n, kg, col) in enumerate(CATCH3):
        cx = x0 + (i % cols) * cw; cy = 64 if i < 3 else 172; h = 100
        fish = ""
        k = max(3, round(kg / 40))
        for _ in range(k):
            fx = rnd.uniform(cx + 22, cx + cw - 30); fy = rnd.uniform(cy + 50, cy + h - 14)
            fish += f'<g transform="translate({fx:.0f},{fy:.0f})"><ellipse cx="0" cy="0" rx="13" ry="5" fill="{col}" stroke="#355" stroke-width="1"/><path d="M12 0 l8 -5 v10 z" fill="{col}" stroke="#355" stroke-width="1"/></g>'
        holds += (f'<rect x="{cx + 4:.0f}" y="{cy}" width="{cw - 8:.0f}" height="{h}" rx="8" fill="#e6f1f6" stroke="#9db6c4" stroke-width="2"/>{fish}'
                  f'<rect x="{cx + 12:.0f}" y="{cy + 8}" width="{cw - 24:.0f}" height="30" rx="6" fill="#fff"/><text x="{cx + cw / 2:.0f}" y="{cy + 29}" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="17" fill="{NV3}"><tspan>{n} · {kg} kg</tspan></text>')
    return f'''<svg viewBox="0 0 900 340" preserveAspectRatio="xMidYMid slice" style="position:absolute;inset:0;width:100%;height:100%"><rect width="900" height="340" fill="#cfe3ec"/>
{"".join(f'<path d="M{x} {y} q12 -6 24 0 t24 0" stroke="#a9cbd9" stroke-width="2" fill="none"/>' for x, y in [(20, 20), (420, 14), (760, 24), (60, 316), (500, 322), (820, 310), (30, 170)])}
<path d="M60 40 H700 Q820 40 880 170 Q820 300 700 300 H60 Q44 300 44 284 V56 Q44 40 60 40 Z" fill="#fbfaf6" stroke="{NV3}" stroke-width="5"/>
<path d="M70 56 H696 Q800 56 852 170 Q800 284 696 284 H70 Z" fill="none" stroke="#c9d6dd" stroke-width="2"/>
<rect x="84" y="96" width="140" height="148" rx="12" fill="{NV3}"/><rect x="100" y="112" width="108" height="34" rx="6" fill="#7fa9c4"/><text x="154" y="200" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="16" fill="#fff"><tspan>Wheelhouse</tspan></text>
{holds}<circle cx="810" cy="170" r="16" fill="{OR3}"/><path d="M780 170 H840" stroke="#fff" stroke-width="3"/></svg>'''
P["p443_boat"] = page(f"""
body{{--f:'Fira Sans';--h:'Bitter';background:{BG3};color:{NV3};font-variant-numeric:lining-nums}}
.kk3{{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:{OR3};margin-top:22px}}
h1{{font-family:'Bitter';font-weight:800;font-size:56px;line-height:1.22;letter-spacing:0;margin-top:12px}} h1 span{{color:{TL3}}}
.w3{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm3{{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:{MU3}}}
.cd3{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(18,50,77,.08)}}
.bt3{{flex:none;padding:16px 20px 18px;display:flex;flex-direction:column;gap:8px}}.bt3 .hd{{display:flex;justify-content:space-between;align-items:center}}.bt3 .hd b{{font:800 24px/1.3 Bitter;color:{OR3}}}.bt3 .im{{height:318px;position:relative;border-radius:14px;overflow:hidden}}
.lo3{{flex:1;display:grid;grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr);gap:16px;min-height:0}}
.sl3{{padding:16px 20px;display:flex;flex-direction:column}}.sl3 .r{{flex:1;display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:center;border-top:1px solid #e3ecf1;padding:6px 0}}.sl3 .sm3{{margin-bottom:6px}}
.sl3 .r b{{font:700 22px/1.3 'Fira Sans'}}.sl3 .r span{{font:500 18px/1.3 'Fira Sans';color:{MU3}}}.sl3 .r strong{{font:800 23px/1.3 Bitter;text-align:right}}
.sl3 .r em{{font:700 16px/1.2 'Fira Sans';font-style:normal;text-align:right;color:{TL3}}}.sl3 .r em.due{{color:#fff;background:{OR3};border-radius:7px;padding:4px 8px}}
.rc3{{display:flex;flex-direction:column;gap:16px}}.tp3{{background:{NV3};color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px}}.tp3 .sm3{{color:#a9c1d1}}
.tp3 .g{{display:grid;grid-template-columns:1fr 1fr;gap:8px}}.tp3 .g div{{background:#1d4566;border-radius:12px;padding:8px 12px;display:flex;flex-direction:column}}.tp3 .g span{{font:500 14px/1.3 'Fira Sans';color:#a9c1d1}}.tp3 .g b{{font:700 19px/1.3 'Fira Sans'}}
.nx3{{flex:1;padding:16px 20px;display:flex;flex-direction:column;gap:6px;justify-content:space-between}}.nx3 .c{{display:flex;gap:10px;align-items:center;font:600 18px/1.3 'Fira Sans'}}.nx3 .c i{{width:22px;height:22px;border-radius:6px;flex:none;display:flex;align-items:center;justify-content:center;color:#fff;font:900 14px/1 'Fira Sans';font-style:normal;background:{TL3}}}.nx3 .c i.o{{background:#fff;border:2px solid {OR3}}}
.nx3 .lv{{background:#fdeee3;color:#8a3f10;border-radius:10px;padding:8px 12px;font:700 16px/1.35 'Fira Sans'}}
""", "<div class=kk3>FISHING BOAT OWNER · TRIP ACCOUNTS</div><h1>Trip accounts on loose slips?<br><span>Every trip, every buyer, saved.</span></h1>",
f'''<div class=w3><div class="cd3 bt3"><div class=hd><span class=sm3>TRIP T-46 · CATCH IN THE HOLD · SAMPLE BOAT</span><b>{TOT3:,} kg</b></div><div class=im>{boat3()}</div></div>
<div class=lo3><div class="cd3 sl3"><span class=sm3>WHO BOUGHT WHAT · MON 23 NOV</span>{"".join(f'<div class=r><b>{b}</b><strong>{sum(KG3[x] for x in sp)} kg</strong><span>{" + ".join(sp)}</span><em class="{"" if st == "Paid" else "due"}">{st}</em></div>' for b, sp, st in SALE3)}</div>
<div class=rc3><div class=tp3><span class=sm3>TRIP T-46 · SAMPLE</span><div class=g>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in [("Out", "Fri 20 Nov, 4 AM"), ("Back", "Mon 23 Nov, 6 AM"), ("Crew", "9 people"), ("Diesel", "640 L"), ("Ice", "120 blocks"), ("Catch", f"{TOT3:,} kg")])}</div></div>
<div class="cd3 nx3"><span class=sm3>NEXT TRIP · T-47</span>{"".join(f'<div class=c><i class="{"" if d else "o"}">{"✓" if d else ""}</i>{t}</div>' for t, d in [("Diesel ordered", True), ("Two nets repaired", True), ("Ice: Wed 25 Nov", False)])}<div class=lv>Leaves Thu 26 Nov, 4 AM</div></div></div></div></div>''',
NV3, "Own fishing boats? DM us", f"background:{OR3};color:#fff")
