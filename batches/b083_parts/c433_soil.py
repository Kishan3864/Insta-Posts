
# ───────── 433 INDIA · Soil testing lab (farm samples) · SINGLE · Gelasio + Inter · loam brown / sprout green / report cream
# New technique: CSS sample-pouch rack (clip-path pouches with tied necks and code tags) coloured by lab stage from one
# sample list, plus a phone report with low / medium / high band bars and a marker for each sample value.
LB3 = "#6b4a2f"; SG3 = "#3f8f4e"; RC3 = "#f6f1e6"; INK3 = "#24201b"; MU3 = "#6e665c"
STG3 = {"Received": "#b9a58a", "Drying": "#d99a2b", "Testing": "#4f7fb8", "Report sent": SG3}
SM3 = [("S-101", "Report sent"), ("S-102", "Report sent"), ("S-103", "Report sent"), ("S-104", "Testing"), ("S-105", "Testing"), ("S-106", "Testing"),
       ("S-107", "Report sent"), ("S-108", "Drying"), ("S-109", "Drying"), ("S-110", "Drying"), ("S-111", "Received"), ("S-112", "Received")]
CNT3 = {k: sum(1 for s in SM3 if s[1] == k) for k in STG3}
RES3 = [("pH", 7.8, 4, 10, (6.5, 7.5), ""), ("Nitrogen (N)", 210, 0, 600, (280, 560), " kg/ha"), ("Phosphorus (P)", 18, 0, 60, (10, 25), " kg/ha"),
        ("Potassium (K)", 320, 0, 500, (120, 280), " kg/ha"), ("Organic carbon", 0.42, 0, 1.2, (0.5, 0.75), "%")]
def lvl3(v, lo, hi): return "Low" if v < lo else "High" if v > hi else "Medium"
def bar3(nm, v, a, b, band, u):
    pc = lambda x: (x - a) / (b - a) * 100
    lv = lvl3(v, *band)
    col = {"Low": "#d99a2b", "Medium": SG3, "High": "#4f7fb8"}[lv]
    return f'''<div class=rs><div class=t><span>{nm}</span><b>{v:g}{u}</b><em style="background:{col}">{lv}</em></div><div class=bb><i class=lo style="width:{pc(band[0]):.1f}%"></i><i class=md style="left:{pc(band[0]):.1f}%;width:{pc(band[1]) - pc(band[0]):.1f}%"></i><u style="left:{pc(v):.1f}%"></u></div></div>'''
APP3 = f'''<div class=ap3><div class=hd><span>Soil report · sample</span><b>S-107 · Sample Farmer G</b><small>Field 2 · 3 acres · tested Sat 21 Nov</small></div>
{"".join(bar3(*r) for r in RES3)}<div class=lg><span><i style="background:#f1dfb8"></i>Low</span><span><i style="background:#d4ead6"></i>Medium</span><span><i style="background:#e3e9f2"></i>High</span><span>· your lab's bands</span></div>
<div class=hs><span>Taken by</span><b>Lab staff · 5 spots mixed</b></div><div class=hs><span>Past tests</span><b>Nov 2025 · Nov 2024</b></div><div class=bt>Send report to farmer</div></div>'''
def pouch3(code, st):
    return f'<div class=pc><div class=bg style="--c:{STG3[st]}"><i class=nk></i><b>{code}</b></div></div>'
P["p433_soil"] = page(f"""
body{{--f:'Inter';--h:'Gelasio';background:{RC3};color:{INK3};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{SG3};margin-top:22px}}
h1{{font-family:'Gelasio';font-weight:700;font-size:60px;line-height:1.2;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{LB3}}}
.w3{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 380px;gap:20px;min-height:0}}
.sm3{{font:700 13px/1.4 Inter;letter-spacing:2px;color:{MU3}}}
.lf3{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.cd3{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(60,40,20,.08);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.rk3{{flex:1;min-height:0}}.rk3 .g{{flex:1;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(3,1fr);gap:12px 14px;background:linear-gradient(transparent calc(100% - 10px),#8a6b4c calc(100% - 10px));padding:6px}}
.pc{{display:flex;align-items:flex-end;justify-content:center;border-bottom:8px solid #8a6b4c}}
.pc .bg{{width:84%;height:88%;background:var(--c);clip-path:polygon(30% 0,70% 0,64% 16%,92% 30%,100% 100%,0 100%,8% 30%,36% 16%);position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:12px}}
.pc .nk{{position:absolute;top:13%;left:34%;width:32%;height:5px;background:#fff;opacity:.85;border-radius:3px}}
.pc b{{font:800 17px/1.2 Inter;color:{INK3};background:#fff;border-radius:7px;padding:5px 8px}}
.lg3{{display:flex;flex-wrap:wrap;gap:8px 16px}}.lg3 div{{display:flex;align-items:center;gap:8px;font:600 16px/1.3 Inter}}.lg3 i{{width:18px;height:18px;border-radius:5px}}.lg3 b{{font-weight:800}}
.nt3{{background:{LB3};color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}}.nt3 .sm3{{color:#e3cfb8}}.nt3 p{{font:500 19px/1.45 Inter}}.nt3 s{{opacity:.75}}
.ph3{{display:flex;align-items:center}}
.ap3{{flex:1;padding:6px 18px 18px;display:flex;flex-direction:column;gap:15px}}.ap3 .hd span{{font:600 13px/1.3 Inter;color:{MU3}}}.ap3 .hd b{{display:block;font:700 20px/1.3 Gelasio;color:{INK3}}}.ap3 .hd small{{font:500 14px/1.3 Inter;color:{MU3}}}
.ap3 .rs{{display:flex;flex-direction:column;gap:6px}}.ap3 .t{{display:flex;align-items:center;gap:8px}}.ap3 .t span{{flex:1;font:600 16px/1.3 Inter;color:{INK3}}}.ap3 .t b{{font:700 15px/1.3 Inter;color:{INK3}}}.ap3 .t em{{font:700 12px/1.2 Inter;font-style:normal;color:#fff;border-radius:7px;padding:4px 7px}}
.ap3 .bb{{position:relative;height:14px;border-radius:7px;background:#e3e9f2;overflow:hidden}}.ap3 .bb i{{position:absolute;top:0;bottom:0}}.ap3 .bb .lo{{left:0;background:#f1dfb8}}.ap3 .bb .md{{background:#d4ead6}}.ap3 .bb u{{position:absolute;top:0;bottom:0;width:5px;margin-left:-2px;background:{INK3};border-radius:2px}}
.ap3 .lg{{display:flex;gap:12px}}.ap3 .lg span{{display:flex;align-items:center;gap:5px;font:600 13px/1.3 Inter;color:{MU3}}}.ap3 .lg i{{width:12px;height:12px;border-radius:3px}}
.ap3 .hs{{display:flex;justify-content:space-between;gap:8px;background:#f6f1e6;border-radius:12px;padding:10px 12px}}.ap3 .hs span{{font:500 14px/1.3 Inter;color:{MU3}}}.ap3 .hs b{{font:700 14px/1.3 Inter;color:{INK3}}}
.ap3 .bt{{margin-top:auto;background:{SG3};color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 16px/1.2 Inter}}
""", "<div class=kk>SOIL TESTING LAB · FARM SAMPLES</div><h1>Soil samples in loose bags?<br><span>Track each one to the report.</span></h1>",
f'''<div class=w3><div class=lf3><div class="cd3 rk3"><span class=sm3>SAMPLE RACK · MON 23 NOV · SAMPLE</span><div class=g>{"".join(pouch3(*s) for s in SM3)}</div>
<div class=lg3>{"".join(f'<div><i style="background:{c}"></i>{k} <b>{CNT3[k]}</b></div>' for k, c in STG3.items())}</div></div>
<div class=nt3><span class=sm3>BEFORE: MARKER ON THE BAG</span><p>“Field near the well, <s>wheat</s> mustard?” Now every bag gets a code, the farmer's phone number and the field, the day it comes in.</p></div></div>
<div class=ph3>{phone(APP3, w=380, h=730)}</div></div>''',
INK3, "Run a soil lab? DM us", f"background:{SG3};color:#fff")
