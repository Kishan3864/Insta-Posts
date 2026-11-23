
# ───────── 441 INDIA · Rainwater harvesting installer · SINGLE · Montserrat + Inter · monsoon slate / terracotta / rain teal
# New technique: house-to-pit cross-section SVG (terrace, down pipe, filter chamber, layered recharge pit with seeded
# gravel and boulders) + an equation strip that turns the surveyed roof size into litres (1 mm on 1 m² = 1 L).
SL1 = "#243039"; TC1 = "#c0643f"; RT1 = "#1d7f8f"; BG1 = "#eaf0f1"; MU1 = "#5e6b73"
RF1 = dict(w=30, l=40); RFA1 = RF1["w"] * RF1["l"]; RFM1 = RFA1 * 0.092903; RAIN1 = 50; LIT1 = round(RFM1 * RAIN1, -1)
STG1 = [("Site survey", "Mon 23 Nov", "done"), ("Quote sent", "Mon 23 Nov", "done"), ("Pit digging", "Thu 26 Nov", "next"), ("Filter and pipes", "Fri 27 Nov", ""), ("Photos and handover", "Sat 28 Nov", "")]
def sect1():
    rnd = random.Random(441)
    rain = "".join(f'<path d="M{x:.0f} {y:.0f} l-7 18" stroke="{RT1}" stroke-width="2.4" stroke-linecap="round" opacity=".55"/>' for x, y in [(rnd.uniform(20, 880), rnd.uniform(-42, 92)) for _ in range(95)])
    grav = "".join(f'<circle cx="{rnd.uniform(664, 816):.0f}" cy="{rnd.uniform(352, 394):.0f}" r="{rnd.uniform(3, 5.5):.1f}" fill="#8f8a84"/>' for _ in range(90))
    bould = "".join(f'<ellipse cx="{x}" cy="{y}" rx="17" ry="13" fill="#6f665d" stroke="#544c45" stroke-width="2"/>' for x, y in [(674, 414), (708, 420), (742, 412), (776, 421), (806, 414), (690, 438), (724, 440), (758, 436), (792, 440)])
    soil = "".join(f'<circle cx="{rnd.uniform(0, 900):.0f}" cy="{rnd.uniform(312, 466):.0f}" r="2" fill="#7a5638" opacity=".5"/>' for _ in range(120))
    return f'''<svg viewBox="0 0 900 540" style="position:absolute;inset:0;width:100%;height:100%" preserveAspectRatio="xMidYMid slice">
<rect x="0" y="0" width="900" height="540" fill="#dfe9ec"/><g transform="translate(0,50)">{rain}<rect x="0" y="0" width="900" height="0"/>
<rect x="0" y="300" width="900" height="200" fill="#b98a5e"/>{soil}<rect x="0" y="296" width="900" height="8" fill="#6f9a4a"/>
<rect x="80" y="140" width="340" height="160" fill="#f3ece2" stroke="#c9bba7" stroke-width="3"/><rect x="70" y="126" width="360" height="16" fill="#8d8379"/><rect x="70" y="112" width="12" height="16" fill="#8d8379"/><rect x="418" y="112" width="12" height="16" fill="#8d8379"/>
<rect x="120" y="180" width="70" height="56" fill="#9ec3cc" stroke="#7d6e5f" stroke-width="3"/><rect x="230" y="200" width="60" height="100" fill="{TC1}"/><rect x="330" y="180" width="70" height="56" fill="#9ec3cc" stroke="#7d6e5f" stroke-width="3"/>
<path d="M100 120 H400" stroke="{RT1}" stroke-width="4" stroke-dasharray="10 8"/><path d="M386 113 l14 7 l-14 7" fill="none" stroke="{RT1}" stroke-width="4"/>
<path d="M430 130 H446 V318 H560" fill="none" stroke="#5d6a72" stroke-width="14" stroke-linejoin="round"/><path d="M430 130 H446 V318 H560" fill="none" stroke="{RT1}" stroke-width="4" stroke-dasharray="8 8"/>
<rect x="560" y="300" width="64" height="62" fill="#c7ced2" stroke="#5d6a72" stroke-width="3"/><path d="M566 332 H618" stroke="#5d6a72" stroke-width="3" stroke-dasharray="3 3"/><path d="M566 342 H618" stroke="#5d6a72" stroke-width="3" stroke-dasharray="3 3"/>
<path d="M624 318 H660" stroke="#5d6a72" stroke-width="10"/>
<rect x="660" y="304" width="160" height="152" fill="#e7cf9a" stroke="#5d6a72" stroke-width="3"/><rect x="662" y="346" width="156" height="52" fill="#b9b2a7"/>{grav}<rect x="662" y="398" width="156" height="56" fill="#9b9187"/>{bould}
<path d="M700 462 v18 M740 462 v26 M780 462 v18" stroke="{RT1}" stroke-width="4" stroke-dasharray="6 5"/>
<rect x="96" y="70" width="270" height="34" rx="17" fill="#fff"/><text x="231" y="93" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="{SL1}"><tspan>Terrace · {RFA1:,} sq ft</tspan></text>
<rect x="462" y="178" width="150" height="34" rx="17" fill="#fff"/><text x="537" y="201" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="{SL1}"><tspan>Down pipe</tspan></text>
<rect x="548" y="250" width="92" height="34" rx="17" fill="#fff"/><text x="594" y="273" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="{SL1}"><tspan>Filter</tspan></text>
<rect x="672" y="250" width="136" height="34" rx="17" fill="{RT1}"/><text x="740" y="273" text-anchor="middle" font-family="Inter" font-weight="700" font-size="18" fill="#fff"><tspan>Recharge pit</tspan></text>
<text x="740" y="332" text-anchor="middle" font-family="Inter" font-weight="700" font-size="16" fill="#5a4a2c"><tspan>Sand</tspan></text>
<rect x="702" y="360" width="76" height="26" rx="6" fill="#fff" opacity=".9"/><text x="740" y="379" text-anchor="middle" font-family="Inter" font-weight="700" font-size="16" fill="{SL1}"><tspan>Gravel</tspan></text>
<rect x="696" y="420" width="88" height="26" rx="6" fill="#fff" opacity=".9"/><text x="740" y="439" text-anchor="middle" font-family="Inter" font-weight="700" font-size="16" fill="{SL1}"><tspan>Boulders</tspan></text>
<rect x="96" y="382" width="250" height="34" rx="17" fill="#fff" opacity=".92"/><text x="221" y="405" text-anchor="middle" font-family="Inter" font-weight="700" font-size="17" fill="#6a4a2c"><tspan>Sandy soil · sample</tspan></text></g>
</svg>'''
P["p441_rain"] = page(f"""
body{{--f:'Inter';--h:'Montserrat';background:{BG1};color:{SL1}}}
.kk1{{font:700 16px/1.4 'Inter';letter-spacing:3px;color:{TC1};margin-top:22px}}
h1{{font-family:'Montserrat';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.2px;margin-top:12px}} h1 span{{color:{RT1}}}
.w1{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm1{{font:700 13px/1.4 'Inter';letter-spacing:2px;color:{MU1}}}
.cd1{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(36,48,57,.08)}}
.sx1{{flex:1;min-height:0;padding:16px 20px 18px;display:flex;flex-direction:column;gap:8px}}.sx1 .im{{flex:1;min-height:0;position:relative;border-radius:14px;overflow:hidden}}
.bt1{{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:16px;flex:none}}
.sv1{{padding:18px 22px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}}
.eq1{{display:flex;align-items:stretch;gap:8px}}.eq1 div{{flex:1;background:#eef4f5;border-radius:14px;padding:10px 12px;display:flex;flex-direction:column;gap:2px}}.eq1 div span{{font:600 13px/1.3 'Inter';color:{MU1}}}.eq1 div b{{font:800 24px/1.3 'Montserrat'}}
.eq1 em{{font:800 26px/1 'Montserrat';font-style:normal;align-self:center;color:{MU1}}}.eq1 div.r1{{background:{RT1};color:#fff}}.eq1 div.r1 span{{color:#d6eef1}}
.nt1{{font:600 15px/1.4 'Inter';color:{RT1}}}
.kv1{{display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}}.kv1 div{{display:flex;justify-content:space-between;border-top:1px solid #e6ecee;padding-top:8px;gap:8px}}.kv1 span{{font:500 16px/1.35 'Inter';color:{MU1}}}.kv1 b{{font:700 16px/1.35 'Inter';text-align:right}}
.jb1{{background:{SL1};color:#fff;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;gap:8px}}.jb1 .sm1{{color:#b7c4cc}}
.jb1 .r{{display:grid;grid-template-columns:22px 1fr auto;gap:10px;align-items:center;padding:4px 0}}.jb1 .r i{{width:18px;height:18px;border-radius:50%;border:3px solid #6d7c86}}.jb1 .r i.done{{background:{RT1};border-color:{RT1}}}.jb1 .r i.next{{border-color:{TC1};background:#fff}}
.jb1 .r b{{font:700 17px/1.3 'Inter'}}.jb1 .r span{{font:600 14px/1.3 'Inter';color:#b7c4cc;white-space:nowrap}}
.jb1 .rm{{margin-top:4px;background:{TC1};border-radius:12px;padding:9px 12px;font:700 15px/1.35 'Inter'}}
""", "<div class=kk1>RAINWATER HARVESTING · INSTALLER</div><h1>Rain pit by guesswork?<br><span>Plan it from the roof size.</span></h1>",
f'''<div class=w1><div class="cd1 sx1"><span class=sm1>SITE PLAN · SAMPLE HOUSE · TERRACE TO RECHARGE PIT</span><div class=im>{sect1()}</div></div>
<div class=bt1><div class="cd1 sv1"><span class=sm1>SITE SURVEY · MON 23 NOV · SAMPLE</span>
<div class=eq1><div><span>Roof {RF1["w"]} × {RF1["l"]} ft</span><b>{RFM1:.1f} m²</b></div><em>×</em><div><span>One heavy rain</span><b>{RAIN1} mm</b></div><em>=</em><div class=r1><span>Water off the roof</span><b>≈ {LIT1:,.0f} L</b></div></div>
<div class=nt1>1 mm of rain on 1 m² of roof = 1 litre</div>
<div class=kv1>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in [("Roof", "Flat terrace"), ("Down pipes", "2"), ("Pit place", "Front yard"), ("Soil", "Sandy"), ("Pit size", "1.5 × 2.5 m"), ("Pipe", "4 inch")])}</div></div>
<div class=jb1><span class=sm1>JOB J-118 · SAMPLE</span>{"".join(f'<div class=r><i class="{s}"></i><b>{a}</b><span>{d}</span></div>' for a, d, s in STG1)}<div class=rm>Pit cleaning reminder: May 2027</div></div></div></div>''',
SL1, "Install rain pits? DM us", f"background:{TC1};color:#fff")
