import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 122 INDIA · Videographer / reel maker · SINGLE · Poppins + Lora · editing-suite black / neon purple / clip colours
# New technique: video editor UI — preview monitor with SVG scene, timecode ruler, 4 tracks of coloured clips and a playhead.
scene = '''<svg viewBox="0 0 640 360" width="100%" height="100%" preserveAspectRatio="xMidYMid slice"><rect width="640" height="360" fill="#f2b36b"/>
<circle cx="470" cy="120" r="56" fill="#ffe3a3"/><path d="M0 250 L120 170 L230 240 L360 150 L520 250 L640 200 V360 H0 Z" fill="#7a4fbf"/><path d="M0 300 L160 240 L320 300 L480 250 L640 290 V360 H0 Z" fill="#3b2a6e"/>
<circle cx="320" cy="180" r="38" fill="rgba(0,0,0,.45)"/><path d="M308 160 L338 180 L308 200 Z" fill="#fff"/></svg>'''
tracks = [("T1", [(18, 22, "#c9a7ff", "Title")]), ("V1", [(0, 28, "#7b5cff", "Clip 1"), (28, 20, "#5aa0ff", "Clip 2"), (48, 30, "#7b5cff", "Clip 3"), (78, 22, "#5aa0ff", "Clip 4")]),
          ("A1", [(0, 100, "#2fbf8f", "Music")]), ("A2", [(10, 35, "#f0b23a", "Voice"), (55, 30, "#f0b23a", "Voice")])]
proj = [("Sample Café", "Reel · 30 sec", "Draft 2 sent", "dr"), ("Sample Shop", "Ad · 45 sec", "Client review", "rv"), ("Sample Event", "Highlights · 3 min", "Final link sent", "dn")]
P["p122_video"] = page("""
body{--f:'Lora';--h:'Poppins';background:#121118;color:#f2effa}
h1{font-family:'Poppins';font-size:60px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#a98bff}
.sub{color:#a9a4bd;font-family:'Lora'}
.vis{flex-direction:column;gap:16px}
.ed{flex:1;background:#1d1b26;border-radius:26px;padding:16px;display:flex;flex-direction:column;gap:12px;border:1.5px solid #2c2939;min-height:0}
.mn{flex:1;border-radius:14px;overflow:hidden;position:relative;min-height:0}
.mn svg{position:absolute;inset:0}
.mn em{position:absolute;left:14px;top:12px;font:700 15px Poppins;font-style:normal;background:rgba(0,0,0,.55);color:#fff;padding:5px 10px;border-radius:8px}
.mn i{position:absolute;right:14px;top:12px;font:700 15px Poppins;font-style:normal;background:#e2483d;color:#fff;padding:5px 10px;border-radius:8px}
.tl{flex:none;position:relative;display:flex;flex-direction:column;gap:6px}
.ru{display:flex;margin-left:56px;justify-content:space-between;font:600 13px Poppins;color:#7f7a92}
.tr{display:flex;align-items:center;gap:8px;height:42px}
.tr b{width:48px;flex:none;font:700 15px Poppins;color:#a9a4bd;text-align:center;background:#2a2737;border-radius:8px;padding:9px 0}
.ln{flex:1;position:relative;height:100%;background:#16141d;border-radius:8px}
.cl{position:absolute;top:3px;bottom:3px;border-radius:7px;padding:0 10px;display:flex;align-items:center;font:700 14px Poppins;color:#121118;overflow:hidden;white-space:nowrap}
.ph{position:absolute;top:18px;bottom:0;left:calc(56px + (100% - 56px) * .62);width:3px;background:#e2483d;border-radius:2px}
.ph:before{content:"";position:absolute;left:-7px;top:-6px;width:17px;height:14px;background:#e2483d;clip-path:polygon(0 0,100% 0,50% 100%)}
.ps{flex:none;display:flex;gap:14px}
.pc{flex:1;background:#f2effa;color:#121118;border-radius:20px;padding:16px 18px;display:flex;flex-direction:column;gap:4px}
.pc b{font:700 22px/1.25 Poppins}.pc span{font:500 17px Lora;color:#5b5670}
.pc em{margin-top:6px;align-self:flex-start;font-style:normal;font:700 15px Poppins;padding:6px 10px;border-radius:8px}
.dr{background:#e9e0ff;color:#4b2fb3}.rv{background:#ffeccc;color:#8a5a0c}.dn{background:#d6f3e7;color:#1a6b4c}
""", "<h1>“Is my video ready?”<br><span>Every project, every draft,<br>one client link.</span></h1><div class=sub>For videographers and reel makers: projects, client feedback and delivery in one place.</div>",
f'''<div class=ed><div class=mn>{scene}<em>Sample Café · Draft 2</em><i>00:18 / 00:30</i></div>
<div class=tl><div class=ru>{"".join(f'<span>00:{s:02d}</span>' for s in range(0,31,5))}</div>
{"".join(f'<div class=tr><b>{n}</b><div class=ln>' + "".join(f'<div class=cl style="left:{a}%;width:{w}%;background:{c}">{t}</div>' for a,w,c,t in cl) + '</div></div>' for n,cl in tracks)}<i class=ph></i></div></div>
<div class=ps>{"".join(f'<div class=pc><b>{a}</b><span>{b}</span><em class={k}>{s}</em></div>' for a,b,s,k in proj)}</div>''',
"#f2effa", "Make videos for clients? DM us", "background:#a98bff;color:#121118")

# ───────── 123 USA · Trucking company · SINGLE · Anton + Fira Sans · highway blue / chrome / amber
# New technique: front-view SVG semi truck (grille, headlights, visor, mirrors) + expiry countdown list per truck and driver.
semi = '''<svg viewBox="0 0 340 420" width="{w}" height="{h}">
<rect x="40" y="40" width="260" height="190" rx="22" fill="#2f5d9e"/><rect x="58" y="70" width="104" height="96" rx="10" fill="#bcd6f2"/><rect x="178" y="70" width="104" height="96" rx="10" fill="#bcd6f2"/>
<rect x="50" y="48" width="240" height="16" rx="8" fill="#ffb400"/>''' + "".join(f'<circle cx="{80+i*45}" cy="56" r="5" fill="#fff3c2"/>' for i in range(5)) + '''
<rect x="8" y="90" width="22" height="70" rx="6" fill="#55657a"/><rect x="310" y="90" width="22" height="70" rx="6" fill="#55657a"/>
<rect x="60" y="230" width="220" height="130" rx="14" fill="#c9d1db"/>''' + "".join(f'<rect x="78" y="{246+i*20}" width="184" height="10" rx="4" fill="#8e99a8"/>' for i in range(5)) + '''
<rect x="20" y="250" width="40" height="30" rx="8" fill="#ffe7a1"/><rect x="280" y="250" width="40" height="30" rx="8" fill="#ffe7a1"/>
<rect x="20" y="360" width="300" height="24" rx="8" fill="#55657a"/><rect x="36" y="384" width="56" height="30" rx="6" fill="#1c2430"/><rect x="248" y="384" width="56" height="30" rx="6" fill="#1c2430"/>
<rect x="130" y="364" width="80" height="16" rx="3" fill="#fff"/><text x="170" y="377" text-anchor="middle" font-family="Fira Sans" font-weight="700" font-size="13" fill="#1c2430">TRUCK 12</text>
</svg>'''
docs = [("Truck 12", "Annual inspection", "Due in 6 days", "hi", 90), ("Truck 12", "Registration", "Due in 18 days", "md", 70), ("Truck 7", "Insurance", "Due in 26 days", "md", 55),
        ("Driver 4", "License renewal", "Due in 45 days", "ok", 30), ("Truck 3", "Fuel tax permit", "Due in 80 days", "ok", 12)]
P["p123_trucking"] = page("""
body{--f:'Fira Sans';--h:'Anton';background:#16263d;color:#eef3f9}
h1{font-family:'Anton';font-weight:400;font-size:66px;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#ffb400}
.vis{gap:20px}
.tk{width:380px;flex:none;background:linear-gradient(#1f3556,#0f1b2c);border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;padding:20px;position:relative;overflow:hidden}
.tk:after{content:"";position:absolute;left:0;right:0;bottom:0;height:70px;background:repeating-linear-gradient(90deg,transparent 0 40px,#ffb400 40px 80px) center 34px/100% 6px no-repeat,#2a3547}
.tk svg{display:block;position:relative;z-index:1}
.tk b{font:400 28px/1.35 Anton;letter-spacing:.3px;position:relative;z-index:1;text-align:center}
.ls{flex:1;background:#eef3f9;color:#16263d;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:8px;min-width:0}
.ls small{font:700 13px 'Fira Sans';letter-spacing:3px;color:#7b8796}
.ls h3{font:400 32px/1.35 Anton;letter-spacing:.3px}
.it{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:1.5px solid #dbe3ec}
.it .t{display:flex;justify-content:space-between;align-items:center;gap:8px}
.it b{font:700 22px 'Fira Sans'}.it span{font:500 17px 'Fira Sans';color:#5d6b7c}
.it em{font-style:normal;font:700 16px 'Fira Sans';padding:6px 10px;border-radius:8px;white-space:nowrap}
.it u{display:block;height:9px;border-radius:5px;background:#dbe3ec;position:relative;overflow:hidden}.it u s{position:absolute;left:0;top:0;bottom:0;border-radius:5px}
.hi em{background:#e2483d;color:#fff}.hi u s{background:#e2483d}.md em{background:#ffe2a1;color:#7a5200}.md u s{background:#ffb400}.ok em{background:#d9efe2;color:#1f6b45}.ok u s{background:#3fae7e}
.tx{background:#16263d;color:#fff;border-radius:14px;padding:12px 16px;font:500 18px/1.4 'Fira Sans'}
""", "<h1>Truck papers expiring<br>without warning?<br><span>Get a heads-up 30 days<br>before each one.</span></h1>",
f'''<div class=tk>{semi.format(w=300,h=371)}<b>12 trucks · 15 drivers<br>one renewal list</b></div>
<div class=ls><small>RENEWALS · SAMPLE</small><h3>Coming up</h3>
{"".join(f'<div class="it {k}"><div class=t><b>{a} · {b}</b><em>{c}</em></div><u><s style="width:{p}%"></s></u></div>' for a,b,c,k,p in docs)}
<div class=tx>Text to office: Truck 12 inspection is due in 6 days. Book a slot?</div></div>''',
"#eef3f9", "Run a trucking company? DM us", "background:#ffb400;color:#16263d")

# ───────── 125 INDIA · College student study planner (personal app) · SINGLE · TeX Gyre Adventor + Open Sans · notebook mint / graphite / pencil yellow
# New technique: syllabus "chapter squares" (one square per chapter, filled when done) + exam countdown, next to a phone day plan.
subs = [("Accounts", 12, 9), ("Economics", 10, 6), ("Business law", 8, 3), ("Statistics", 9, 5), ("Marketing", 7, 7)]
plan = [("7:00", "Accounts · ch 10", "y"), ("9:00", "College", "g"), ("4:00", "Statistics · ch 6", "y"), ("6:00", "Break · walk", "g"), ("7:00", "Law · ch 4", "y"), ("9:30", "Quick test · 20 Qs", "p")]
P["p125_planner"] = page("""
body{--f:'Open Sans';--h:'TeX Gyre Adventor';background:#dff1e8;color:#262b30;background-image:linear-gradient(#c8e3d6 1.5px,transparent 1.5px);background-size:100% 46px}
h1{font-family:'TeX Gyre Adventor';font-size:60px;font-weight:700;letter-spacing:-1px} h1 span{color:#2a7a5c;background:#ffd84a;padding:0 10px;border-radius:8px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.vis{gap:22px;align-items:center}
.lf{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.cd{flex:none;background:#262b30;color:#fff;border-radius:24px;padding:18px 22px;display:flex;align-items:center;gap:18px}
.cd b{font:700 72px/1.2 'TeX Gyre Adventor';color:#ffd84a}.cd span{font:600 20px/1.35 'Open Sans';color:#cfd6dc}
.sy{flex:1;background:#fff;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:6px;box-shadow:0 14px 30px rgba(38,43,48,.08)}
.sy small,.ap small{font:700 13px 'Open Sans';letter-spacing:3px;color:#8a949c}
.sb{flex:1;display:flex;flex-direction:column;justify-content:center;gap:8px;border-top:1.5px solid #edf1ef}
.sb .t{display:flex;justify-content:space-between}.sb b{font:700 21px 'TeX Gyre Adventor'}.sb span{font:700 17px 'Open Sans';color:#2a7a5c}
.sq{display:flex;gap:6px}.sq i{width:26px;height:26px;border-radius:6px;background:#e7eeea;display:block}.sq i.on{background:#2a7a5c}
.ap{flex:1;padding:12px 16px 16px;display:flex;flex-direction:column;gap:8px;background:#f6faf8}
.ap .h{display:flex;flex-direction:column;gap:2px;padding:4px 2px}.ap .h b{font:700 21px 'TeX Gyre Adventor'}
.bl{flex:1;display:flex;align-items:center;gap:10px;border-radius:12px;padding:0 12px;background:#fff;border-left:6px solid #ffd84a}
.bl em{font-style:normal;width:44px;font:700 14px 'Open Sans';color:#8a949c}.bl b{font:600 16px 'Open Sans'}
.bl.g{border-left-color:#b8c4bd}.bl.p{border-left-color:#2a7a5c;background:#e6f4ec}
""", "<h1>Exams in 30 days<br>and no plan?<br><span>Turn the syllabus</span><br><span>into a daily plan.</span></h1>",
f'''<div class=lf><div class=cd><b>30</b><span>days to exams<br>Sample student · B.Com year 2</span></div>
<div class=sy><small>SYLLABUS · CHAPTERS DONE · SAMPLE</small>{"".join(f'<div class=sb><div class=t><b>{a}</b><span>{d} of {n}</span></div><div class=sq>' + "".join(f'<i class="{"on" if i<d else ""}"></i>' for i in range(n)) + '</div></div>' for a,n,d in subs)}</div></div>
{phone(f"""<div class=ap><div class=h><small>TODAY · MON 23 NOV</small><b>Your plan</b></div>{"".join(f'<div class="bl {k}"><em>{a}</em><b>{b}</b></div>' for a,b,k in plan)}</div>""", w=350, h=700)}''',
"#262b30", "Want your own app? DM us", "background:#2a7a5c;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
