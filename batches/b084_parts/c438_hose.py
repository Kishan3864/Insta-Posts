
# ───────── 438 INDIA · Hydraulic hose shop (crimping for earthmovers and tractors) · SINGLE · Archivo Black + DM Sans · hose black / brass / hydraulic red
# New technique: hose assembly drawing with two different end fittings and a dimension line from the job data, and
# hose reels as conic-gradient rings showing metres left, with the job's cut taken off the right reel.
HK8 = "#202326"; BR8 = "#c9a246"; RD8b = "#c8392f"; BG8b = "#f1efe9"; MU8b = "#676b70"
JOB8 = dict(no="H-2231", mach="Backhoe loader, bucket line", size='1/2"', wire="2-wire", L=1250, a="Straight female", b="90° elbow female")
RL8 = [('1/4"', 2, 34, 50), ('3/8"', 2, 12, 50), ('1/2"', 2, 41, 50), ('3/4"', 4, 18, 40)]
HS8 = [("Sample Contractor A", "Backhoe loader", "Bucket line", "Mon 23 Nov", "1/2\", 1,250 mm"), ("Sample Contractor A", "Backhoe loader", "Boom line", "Sat 3 Oct", "1/2\", 1,600 mm"),
       ("Sample Farmer B", "Tractor", "Loader line", "Fri 20 Nov", "3/8\", 900 mm"), ("Sample Crane C", "Truck crane", "Outrigger", "Thu 12 Nov", "3/4\", 2,100 mm")]
def hose8():
    return f'''<svg viewBox="0 0 900 220" style="display:block;width:100%;height:auto">
<path d="M150 110 C320 40, 560 180, 720 110" stroke="{HK8}" stroke-width="30" fill="none" stroke-linecap="round"/><path d="M150 110 C320 40, 560 180, 720 110" stroke="#4a4f55" stroke-width="2" fill="none" stroke-dasharray="14 10"/>
<rect x="110" y="88" width="56" height="44" rx="6" fill="{BR8}"/><rect x="60" y="94" width="54" height="32" rx="4" fill="#d9b961"/><path d="M60 94 v32 M74 94 v32 M88 94 v32" stroke="#a7852f" stroke-width="2"/>
<rect x="706" y="88" width="56" height="44" rx="6" fill="{BR8}"/><path d="M762 98 H800 Q820 98 820 78 V40" stroke="#d9b961" stroke-width="30" fill="none"/><path d="M806 46 H834 M806 58 H834" stroke="#a7852f" stroke-width="2"/>
<path d="M88 190 H790" stroke="{RD8b}" stroke-width="2.5"/><path d="M88 178 V202 M790 178 V202" stroke="{RD8b}" stroke-width="2.5"/>
<rect x="370" y="174" width="160" height="34" rx="8" fill="{RD8b}"/><text x="450" y="198" text-anchor="middle" font-family="DM Sans" font-weight="800" font-size="20" fill="#fff"><tspan>{JOB8["L"]:,} mm</tspan></text>
<text x="88" y="66" font-family="DM Sans" font-weight="700" font-size="17" fill="{HK8}"><tspan>{JOB8["a"]}</tspan></text><text x="640" y="26" font-family="DM Sans" font-weight="700" font-size="17" fill="{HK8}"><tspan>{JOB8["b"]}</tspan></text></svg>'''
def reel8(sz, w, left, full):
    pc = left / full * 100; low = left < 15
    return f'''<div class=rl><div class=ring style="background:conic-gradient({RD8b if low else HK8} 0 {pc:.1f}%,#ddd8cc {pc:.1f}% 100%)"><div class=hb><b>{sz}</b><span>{w}-wire</span></div></div><strong>{left} m left</strong><em class="{'lo' if low else ''}">{'Order more' if low else f'of {full} m'}</em></div>'''
P["p438_hose"] = page(f"""
body{{--f:'DM Sans';--h:'Archivo Black';background:{BG8b};color:{HK8}}}
.kk{{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:{RD8b};margin-top:22px}}
h1{{font-family:'Archivo Black';font-weight:400;font-size:54px;line-height:1.22;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{RD8b}}}
.w8{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm8b{{font:700 13px/1.4 'DM Sans';letter-spacing:2px;color:{MU8b}}}
.cd8b{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(32,35,38,.08);padding:16px 22px;display:flex;flex-direction:column;gap:10px}}
.jb8 .sp{{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}}.jb8 .sp div{{background:#f4f1ea;border-radius:12px;padding:10px 12px;display:flex;flex-direction:column}}.jb8 .sp span{{font:600 13px/1.3 'DM Sans';color:{MU8b}}}.jb8 .sp b{{font:700 18px/1.3 'DM Sans'}}
.bt8{{flex:1;display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.8fr);gap:16px;min-height:0}}
.hs8 .r{{flex:1;display:grid;grid-template-columns:1fr auto;gap:2px 10px;align-items:center;border-top:1px solid #ece8df;padding:6px 0}}.hs8 .r b{{font:700 18px/1.3 'DM Sans'}}.hs8 .r span{{font:500 15px/1.3 'DM Sans';color:{MU8b}}}.hs8 .r strong{{font:700 16px/1.3 'DM Sans';text-align:right}}.hs8 .r em{{font:700 13px/1.2 'DM Sans';font-style:normal;color:{RD8b};text-align:right}}
.hs8 .bt{{background:{HK8};color:#fff;border-radius:12px;padding:12px;text-align:center;font:700 16px/1.2 'DM Sans'}}
.rs8 .g{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:10px}}.rl{{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px}}.rl .ring{{width:150px;height:150px;border-radius:50%;display:flex;align-items:center;justify-content:center}}.rl .hb{{width:98px;height:98px;border-radius:50%;background:#fff;display:flex;flex-direction:column;align-items:center;justify-content:center}}.rl .hb b{{font:700 19px/1.1 'DM Sans';margin-bottom:5px}}.rl .hb span{{font:600 12px/1.3 'DM Sans';color:{MU8b}}}
.rl strong{{font:800 17px/1.3 'DM Sans'}}.rl em{{font:700 13px/1.2 'DM Sans';font-style:normal;color:{MU8b}}}.rl em.lo{{color:#fff;background:{RD8b};border-radius:7px;padding:4px 8px}}
""", "<div class=kk>HYDRAULIC HOSE SHOP · CRIMPING</div><h1>Old hose in hand, no record?<br><span>Every hose saved by machine.</span></h1>",
f'''<div class=w8><div class="cd8b jb8"><span class=sm8b>JOB {JOB8["no"]} · {JOB8["mach"].upper()} · SAMPLE</span>{hose8()}<div class=sp>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in [("Hose", f'{JOB8["size"]} {JOB8["wire"]}'), ("Length", f'{JOB8["L"]:,} mm'), ("End A", JOB8["a"]), ("End B", JOB8["b"])])}</div></div>
<div class=bt8><div class="cd8b hs8"><span class=sm8b>HOSE HISTORY BY MACHINE</span>{"".join(f'<div class=r><b>{c}</b><strong>{d}</strong><span>{m} · {ln}</span><em>{sz}</em></div>' for c, m, ln, d, sz in HS8)}<div class=bt>Same as last time: make it again</div></div>
<div class="cd8b rs8"><span class=sm8b>HOSE REELS · METRES LEFT</span><div class=g>{"".join(reel8(*r) for r in RL8)}</div></div></div></div>''',
HK8, "Run a hose shop? DM us", f"background:{RD8b};color:#fff")
