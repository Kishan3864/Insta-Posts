
# ───────── 423 INDIA · Biogas plant installer · SINGLE · Gelasio + DM Sans · slurry brown / flame blue / leaf green
# New technique: underground cross-section of a fixed-dome plant where every part is coloured by its install stage
# (done / working / pending dashed) with numbered pins matching a stage list; survey and service cards share the site code.
SB3 = "#6b4f32"; FB3 = "#2f7fd1"; LG3 = "#3f8a3a"; AM3 = "#e8a33a"; K3 = "#22261f"; BG3 = "#f1efe5"
STG3 = [(1, "Pit dug", "done"), (2, "Base and walls", "done"), (3, "Dome", "work"), (4, "Inlet tank", "todo"), (5, "Outlet tank", "todo"), (6, "Gas pipe to kitchen", "todo")]
SC3 = {k: s for k, _, s in STG3}
def part3(k, d, extra=""):
    st = SC3[k]
    if st == "done": return f'<path d="{d}" fill="#9fcf8f" stroke="{LG3}" stroke-width="4"{extra}/>'
    if st == "work": return f'<path d="{d}" fill="#f6d398" stroke="{AM3}" stroke-width="4"{extra}/>'
    return f'<path d="{d}" fill="#ece8dc" fill-opacity=".7" stroke="#8d8676" stroke-width="3" stroke-dasharray="9 6"{extra}/>'
def pin3(x, y, n):
    return f'<circle cx="{x}" cy="{y}" r="19" fill="{K3}" stroke="#fff" stroke-width="3"/><text x="{x}" y="{y + 7}" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="19" fill="#fff"><tspan>{n}</tspan></text>'
def plant3():
    rnd = random.Random(5)
    soil = "".join(f'<circle cx="{rnd.uniform(0, 640):.0f}" cy="{rnd.uniform(170, 560):.0f}" r="{rnd.uniform(2, 4):.1f}" fill="#9c7a52"/>' for _ in range(90))
    pit = part3(1, "M150 222 L150 548 L470 548 L470 222 Z", ' fill-opacity=".35"')
    walls = part3(2, "M176 330 L176 520 L444 520 L444 330 L420 330 L420 496 L200 496 L200 330 Z")
    dome = part3(3, "M176 330 Q176 214 310 206 Q444 214 444 330 L420 330 Q420 238 310 230 Q200 238 200 330 Z")
    inlet = part3(4, "M40 150 L120 150 L120 214 L40 214 Z") + part3(4, "M112 206 L200 456 L184 462 L98 212 Z")
    outlet = part3(5, "M480 150 L580 150 L580 250 L480 250 Z") + part3(5, "M436 420 L490 244 L506 250 L452 426 Z")
    pipe = part3(6, "M302 206 L302 100 L590 100 L590 88 L318 88 L318 100 L318 206 Z")
    slurry = '<path d="M200 330 L420 330 L420 496 L200 496 Z" fill="#8a6a45" opacity=".55"/>'
    stove = f'<rect x="560" y="104" width="70" height="20" rx="4" fill="#8d8676"/><path d="M582 104 Q586 86 595 80 Q600 92 608 104 Z" fill="{FB3}" opacity=".4"/>'
    pins = pin3(160, 540, 1) + pin3(430, 470, 2) + pin3(310, 250, 3) + pin3(80, 182, 4) + pin3(530, 200, 5) + pin3(450, 70, 6)
    return f'''<svg viewBox="0 0 640 570" width="640" style="display:block;width:100%;height:auto"><rect width="640" height="150" fill="#e3ecf2"/><rect y="150" width="640" height="420" fill="#c29c6e"/>{soil}
<rect y="146" width="640" height="8" fill="#6f9a4a"/>{pit}{slurry}{walls}{dome}{inlet}{outlet}{pipe}{stove}
<text x="555" y="146" font-family="DM Sans" font-weight="700" font-size="17" fill="{K3}"><tspan>Kitchen</tspan></text><text x="18" y="140" font-family="DM Sans" font-weight="700" font-size="17" fill="{K3}"><tspan>Dung in</tspan></text>{pins}</svg>'''
CHIP3 = {"done": ("Done", "#dcefd6", "#2c6a28"), "work": ("Working", "#fbe6c3", "#8a560c"), "todo": ("Next", "#ece8dc", "#6d6658")}
P["p423_biogas"] = page(f"""
body{{--f:'DM Sans';--h:'Gelasio';background:{BG3};color:{K3};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{LG3};margin-top:22px}}
h1{{font-family:'Gelasio';font-weight:700;font-size:60px;line-height:1.24;letter-spacing:-.8px;margin-top:20px}} h1 span{{color:{SB3}}}
.vw3{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}
.sm3{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:#736c5c}}
.cd3{{background:#fffdf6;border-radius:24px;box-shadow:0 14px 30px rgba(40,40,20,.09);padding:16px 20px;display:flex;flex-direction:column;gap:8px}}
.tp3{{flex:1;display:grid;grid-template-columns:minmax(0,1.25fr) minmax(0,.75fr);gap:14px;min-height:0}}.sv3{{flex:1;min-height:0;display:flex;align-items:center}}
.sl3 .r{{flex:1;display:grid;grid-template-columns:36px 1fr auto;gap:10px;align-items:center;border-top:1px solid #ece5d2}}.sl3 .r i{{width:32px;height:32px;border-radius:50%;background:{K3};color:#fff;font:700 16px/32px 'DM Sans';font-style:normal;text-align:center}}
.sl3 .r b{{font:700 18px/1.3 'DM Sans'}}.sl3 .r em{{font:700 14px/1.2 'DM Sans';font-style:normal;border-radius:9px;padding:7px 9px}}
.bt3{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}
.sv3c .r,.vs3 .r{{display:flex;justify-content:space-between;gap:10px;padding:7px 0;border-top:1px solid #ece5d2}}.sv3c .r span{{font:500 17px/1.3 'DM Sans';color:#736c5c}}.sv3c .r b{{font:700 18px/1.3 'DM Sans';text-align:right}}
.sz3{{display:flex;justify-content:space-between;align-items:center;background:#e3efdf;border-radius:12px;padding:8px 14px}}.sz3 span{{font:600 15px/1.3 'DM Sans'}}.sz3 b{{font:700 28px/1.35 Gelasio;color:{LG3}}}
.vs3{{background:{K3};color:#fff}}.vs3 .sm3{{color:#b9c2ad}}.vs3 .r{{border-color:rgba(255,255,255,.12);flex:1;align-items:center}}.vs3 .r b{{font:700 18px/1.3 'DM Sans'}}.vs3 .r span{{font:500 16px/1.3 'DM Sans';color:#cfd6c4;text-align:right}}
""", "<div class=kk>BIOGAS PLANT INSTALLER · FARM UNITS</div><h1>Biogas jobs on loose paper?<br><span>Survey to service, one app.</span></h1>",
f'''<div class=vw3><div class=tp3><div class=cd3><span class=sm3>SITE S-27 · FIXED DOME · COLOUR = STAGE · SAMPLE</span><div class=sv3>{plant3()}</div></div>
<div class="cd3 sl3"><span class=sm3>INSTALL STAGES · S-27</span>{"".join(f'<div class=r><i>{n}</i><b>{t}</b><em style="background:{CHIP3[s][1]};color:{CHIP3[s][2]}">{CHIP3[s][0]}</em></div>' for n, t, s in STG3)}<div class=r><i style="background:{FB3}">7</i><b>First gas check</b><em style="background:#e1ecf8;color:{FB3}">Sat 5 Dec</em></div></div></div>
<div class=bt3><div class="cd3 sv3c"><span class=sm3>SURVEY · S-27 · SAMPLE FARM</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Cattle", "6"), ("Space", "4 m × 4 m"), ("Kitchen", "15 m away")])}<div class=sz3><span>Size from your chart</span><b>3 m³</b></div></div>
<div class="cd3 vs3"><span class=sm3>SERVICE VISITS THIS WEEK</span>{"".join(f'<div class=r><b>{a}</b><span>{b}</span></div>' for a, b in [("S-11 · Sat 28 Nov", "Slurry check"), ("S-19 · Mon 30 Nov", "Pipe leak check"), ("S-22 · Wed 2 Dec", "Gas valve check")])}</div></div></div>''',
K3, "Install biogas plants? DM us", f"background:{LG3};color:#fff")
