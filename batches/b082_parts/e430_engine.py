
# ───────── 430 CANADA · Small engine repair shop (snowblowers, generators) · SINGLE · Poppins + Fira Sans · spruce green / frost / tag yellow
# New technique: CSS pegboard (radial-gradient holes) with hanging manila repair tags on pegs and strings, chamfered by
# clip-path, plus a side-view SVG snowblower with numbered pins that match the job steps and the text to the owner.
SP0 = "#2e5a4c"; FR0 = "#eef3f2"; TY0 = "#f4c542"; INK0 = "#1f2d29"; MU0 = "#5f6f6a"; MN0 = "#e9d9b4"
ST0 = {"Waiting for parts": "#c8553d", "On the bench": "#d99a2b", "Ready": "#3c8d6e", "Stored to spring": "#4f6d8f"}
TG0 = [("T-114", "2-stage snowblower", "Sample Owner A", "Ready", "Pick up Thu"), ("T-115", "Portable generator", "Sample Owner B", "On the bench", "Fri 27 Nov"),
       ("T-116", "Chainsaw", "Sample Owner C", "Waiting for parts", "Part due Wed"), ("T-117", "Lawn tractor", "Sample Owner D", "Stored to spring", "Out in April"),
       ("T-118", "2-stage snowblower", "Sample Owner E", "Ready", "Pick up Thu"), ("T-119", "1-stage snowblower", "Sample Owner F", "On the bench", "Sat 28 Nov")]
STEPS0 = [("New auger belt", True), ("Carburetor cleaned", True), ("Shear pins replaced", True)]
PROB0 = {"T-114": "Won't throw snow", "T-115": "Surges under load", "T-116": "Chain brake stuck", "T-117": "Winter storage", "T-118": "Belt slipping", "T-119": "Hard to start"}
def blower0():
    pins = [(1, 250, 205), (2, 360, 150), (3, 150, 236)]
    g = f'''<rect x="0" y="318" width="560" height="12" rx="6" fill="#d7e2df"/>
<path d="M230 170 V300 H110 A65 65 0 0 1 110 170 Z" fill="#c8553d"/><path d="M200 184 V286 H112 A51 51 0 0 1 112 184 Z" fill="#2c3a36"/>
<path d="M70 236 H200" stroke="#8a9893" stroke-width="6"/><path d="M84 198 L104 274 M114 192 L134 280 M144 192 L164 280 M174 192 L192 278" stroke="#d7dcda" stroke-width="7" stroke-linecap="round"/>
<path d="M130 170 V110 Q130 90 150 92 L190 98" stroke="#2c3a36" stroke-width="18" fill="none" stroke-linecap="round"/><path d="M186 92 l26 8 l-6 16 l-24 -6 Z" fill="#2c3a36"/>
<rect x="230" y="150" width="190" height="130" rx="18" fill="#3b4a46"/><rect x="250" y="130" width="120" height="30" rx="10" fill="#56645f"/><circle cx="300" cy="215" r="34" fill="#56645f"/><circle cx="300" cy="215" r="14" fill="#2c3a36"/>
<path d="M420 170 L520 40 M432 190 L534 58" stroke="#2c3a36" stroke-width="12" stroke-linecap="round"/><path d="M512 34 L548 62" stroke="#2c3a36" stroke-width="14" stroke-linecap="round"/>
<circle cx="380" cy="282" r="38" fill="#222c29"/><circle cx="380" cy="282" r="14" fill="#8a9893"/>'''
    g += "".join(f'<circle cx="{x}" cy="{y}" r="20" fill="{TY0}" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y + 8}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="21" fill="{INK0}"><tspan>{n}</tspan></text>' for n, x, y in pins)
    return f'<svg viewBox="0 20 560 316" style="display:block;width:100%;height:auto">{g}</svg>'
def tag0(t):
    c, m, o, s, d = t
    return f'''<div class=hg><i class=pg0></i><i class=str></i><div class=tg><i class=hl></i><b>{c}</b><strong>{m}</strong><span>{o}</span><p>“{PROB0[c]}”</p><em style="background:{ST0[s]}">{s}</em><small>{d}</small></div></div>'''
READY0 = [t for t in TG0 if t[3] == "Ready"]
P["p430_engine"] = page(f"""
body{{--f:'Fira Sans';--h:'Poppins';background:{FR0};color:{INK0}}}
.kk{{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:{SP0};margin-top:22px}}
h1{{font-family:'Poppins';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.5px;margin-top:14px}} h1 span{{color:{SP0}}}
.w0{{flex:1;display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,.95fr);gap:18px;min-height:0}}
.sm0{{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:{MU0}}}
.pb0{{background:radial-gradient(circle,#8f6f48 0 3.5px,transparent 4.5px) 0 0/30px 30px,#c9a77c;border-radius:22px;padding:16px 18px;display:flex;flex-direction:column;gap:6px;box-shadow:inset 0 0 0 6px #b48f62}}
.pb0 .sm0{{color:#4a3720;background:#e9d9b4;border-radius:8px;padding:4px 10px;align-self:flex-start}}
.pb0 .gd{{flex:1;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:repeat(3,1fr);gap:4px 16px}}
.hg{{display:flex;flex-direction:column;align-items:center}}.hg .pg0{{width:16px;height:16px;border-radius:50%;background:#5a6662;box-shadow:0 2px 0 #3c4542}}.hg .str{{width:2px;height:16px;background:#f2ece0}}
.tg{{flex:1;width:100%;background:{MN0};clip-path:polygon(18px 0,calc(100% - 18px) 0,100% 18px,100% 100%,0 100%,0 18px);padding:22px 14px 10px;display:flex;flex-direction:column;align-items:flex-start;gap:2px;position:relative}}
.tg .hl{{position:absolute;top:8px;left:50%;margin-left:-6px;width:12px;height:12px;border-radius:50%;background:#c9a77c;box-shadow:0 0 0 3px #d8c18c}}
.tg b{{font:800 25px/1.3 Poppins}}.tg strong{{font:700 18px/1.3 'Fira Sans'}}.tg span{{font:500 15px/1.3 'Fira Sans';color:#6b5a3c}}.tg p{{font:italic 600 18px/1.35 'Fira Sans';color:#4a3720;margin-top:6px;border-top:1px dashed #b9a274;padding-top:6px;align-self:stretch}}.tg em{{font:700 13px/1.2 'Fira Sans';font-style:normal;color:#fff;border-radius:8px;padding:5px 8px;margin-top:auto}}.tg small{{font:600 13px/1.3 'Fira Sans';color:#4a3720;margin-top:3px}}
.rt0{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.cd0{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(31,45,41,.08);padding:16px 20px;display:flex;flex-direction:column;gap:8px}}
.jb0{{flex:1;justify-content:space-between}}.jb0 .pt{{display:flex;justify-content:space-between;gap:10px;background:#f1f5f4;border-radius:12px;padding:10px 14px}}.jb0 .pt span{{font:500 16px/1.3 'Fira Sans';color:{MU0}}}.jb0 .pt b{{font:700 16px/1.3 'Fira Sans'}}.jb0 .s{{display:flex;align-items:center;gap:12px;padding:8px 0;border-top:1px solid #e6ecea;font:600 19px/1.3 'Fira Sans'}}.jb0 .s u{{text-decoration:none;width:30px;height:30px;border-radius:50%;background:{TY0};font:800 16px/30px Poppins;text-align:center;flex:none}}.jb0 .s svg{{margin-left:auto}}
.tx0{{background:{SP0};color:#fff;border-radius:22px;padding:18px 20px;display:flex;flex-direction:column;gap:8px}}.tx0 .sm0{{color:#bcd6cd}}.tx0 p{{font:500 19px/1.45 'Fira Sans'}}.tx0 em{{align-self:flex-start;font:700 15px/1.2 'Fira Sans';font-style:normal;background:{TY0};color:{INK0};border-radius:9px;padding:7px 12px}}
""", "<div class=kk>SMALL ENGINE REPAIR · SNOW SEASON</div><h1>Snowblowers piling up?<br><span>Tag it, fix it, text the owner.</span></h1>",
f'''<div class=w0><div class=pb0><span class=sm0>THE SHOP WALL · MON 23 NOV · SAMPLE</span><div class=gd>{"".join(tag0(t) for t in TG0)}</div></div>
<div class=rt0><div class="cd0 jb0"><span class=sm0>JOB CARD · T-118 · 2-STAGE SNOWBLOWER</span>{blower0()}{"".join(f'<div class=s><u>{i}</u>{a}{ic("check", 24, "#3c8d6e", 3)}</div>' for i, (a, ok) in enumerate(STEPS0, 1))}<div class=s><u>✓</u>Test run in the yard{ic("check", 24, "#3c8d6e", 3)}</div><div class=pt><span>Parts used</span><b>1 auger belt · 2 shear pins</b></div><div class=pt><span>Next service reminder</span><b>Oct 2027, by text</b></div></div>
<div class=tx0><span class=sm0>TEXT TO SAMPLE OWNER E</span><p>Your snowblower (T-118) is ready: new auger belt, carburetor cleaned, shear pins replaced. Pick up Thu 26 Nov, 8 AM to 6 PM.</p><em>{len(READY0)} machines ready · owners told</em></div></div></div>''',
INK0, "Fix small engines? DM us", f"background:{SP0};color:#fff")
