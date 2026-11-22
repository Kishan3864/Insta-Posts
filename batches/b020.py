import sys; sys.path.insert(0, "tools/postkit"); from lib import *
import random, math
P = {}

# ───────── 117 INDIA · Organic farm produce box · SINGLE · Lora + Poppins · soil brown / leaf lime / cream
# New technique: top-down SVG wooden crate packed with drawn vegetables (tomatoes, carrots, greens, brinjal, okra),
# phone subscription screen with skip/swap, farm packing chips.
random.seed(117)
def veg():
    o = []
    for x, y in [(60 + i * 46, 70 + j * 44) for i in range(4) for j in range(3)]:
        o.append(f'<circle cx="{x}" cy="{y}" r="20" fill="#d9412b"/><path d="M{x-6} {y-18} l6 5 l6 -5" stroke="#3f7d2a" stroke-width="4" fill="none"/>')
    for i in range(7):
        x = 250 + i * 22
        o.append(f'<path d="M{x} 50 L{x+10} 50 L{x+5} 200 Z" fill="#ee8a2a"/><path d="M{x+5} 50 l-8 -22 M{x+5} 50 l0 -24 M{x+5} 50 l8 -22" stroke="#4c9a2f" stroke-width="4"/>')
    for x, y in [(80, 240), (150, 250), (110, 300), (60, 310), (170, 320)]:
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="42" ry="30" fill="#4c9a2f"/><ellipse cx="{x}" cy="{y}" rx="26" ry="18" fill="#6fbf43"/><path d="M{x-30} {y} H{x+30}" stroke="#3a7a22" stroke-width="3"/>')
    for x, y, a in [(270, 260, -20), (330, 280, 15), (300, 320, -5)]:
        o.append(f'<ellipse cx="{x}" cy="{y}" rx="38" ry="20" transform="rotate({a} {x} {y})" fill="#5b2a6e"/><path d="M{x-40} {y-6} l-12 -6" stroke="#3f7d2a" stroke-width="7" stroke-linecap="round" transform="rotate({a} {x} {y})"/>')
    for i in range(6):
        x = 382 + (i % 2) * 22; y = 230 + (i // 2) * 40
        o.append(f'<path d="M{x} {y} q8 -4 8 30 q-8 6 -16 0 q0 -26 8 -30 z" fill="#7cb342" stroke="#558b2f" stroke-width="2"/>')
    return "".join(o)
crate = (f'<svg viewBox="0 0 460 380" width="{{w}}" height="{{h}}"><rect x="0" y="0" width="460" height="380" rx="14" fill="#a8743f"/>'
         f'<rect x="18" y="18" width="424" height="344" rx="8" fill="#6b4524"/>'
         + "".join(f'<rect x="0" y="{y}" width="460" height="10" fill="#8a5a2e" opacity=".5"/>' for y in (120, 250))
         + f'<g>{veg()}</g><rect x="0" y="0" width="460" height="18" fill="#c08850"/><rect x="0" y="362" width="460" height="18" fill="#c08850"/></svg>')
P["p117_organic"] = page("""
body{--f:'Poppins';--h:'Lora';background:#f3ecdc;color:#2f2216}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#4f8a2b}
.sub{color:#6b5a45}
.vis{flex-direction:column;gap:16px}
.tp{flex:1;display:flex;gap:20px;align-items:center;min-height:0}
.cr{flex:1;align-self:stretch;background:#d7e7bf;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:12px}
.cr svg{display:block}
.cr b{font:700 26px/1.25 Lora;color:#2f2216}.cr span{font:600 17px Poppins;color:#4f6b3a}
.ap{flex:1;padding:12px 16px 16px;display:flex;flex-direction:column;gap:9px;background:#faf6ec}
.ap .h{display:flex;flex-direction:column;gap:2px;padding:4px 2px}.ap .h b{font:700 22px Lora}.ap .h span{font:600 14px Poppins;color:#8a7a62}
.ap .it{flex:1;background:#fff;border-radius:14px;padding:0 14px;display:flex;justify-content:space-between;align-items:center;font:600 16px Poppins}
.ap .it em{font-style:normal;font:600 13px Poppins;color:#4f8a2b;background:#eaf3dc;padding:4px 8px;border-radius:8px}
.ap .wk{display:flex;gap:6px}.ap .wk i{flex:1;font-style:normal;text-align:center;font:600 13px Poppins;padding:8px 0;border-radius:10px;background:#fff;border:2px solid #e3dac6}
.ap .wk i.sk{background:#f6e3d8;border-color:#e6b9a1;color:#a04a22}
.ap .bt{display:flex;gap:8px}.ap .bt i{flex:1;font-style:normal;text-align:center;font:700 15px Poppins;padding:11px 0;border-radius:12px;background:#4f8a2b;color:#fff}.ap .bt i.l{background:#fff;color:#2f2216;border:2px solid #e3dac6}
.pk{flex:none;background:#2f2216;color:#f3ecdc;border-radius:22px;padding:14px 20px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.pk small{font:700 13px Poppins;letter-spacing:3px;color:#c9b99c;width:100%}
.pk em{font-style:normal;font:600 18px Poppins;background:#45341f;border-radius:10px;padding:7px 12px}
""", "<h1>Weekly veg box orders<br>on chat?<br><span>Let families subscribe<br>and skip online.</span></h1>",
f'''<div class=tp><div class=cr>{crate.format(w=440,h=363)}<b>Saturday box · sample</b><span>Packed fresh on Friday evening</span></div>
{phone(f"""<div class=ap><div class=h><b>Your Farm Box</b><span>Sample family · weekly</span></div>
{"".join(f'<div class=it><span>{a}</span><em>{b}</em></div>' for a,b in [("Tomatoes","1 kg"),("Carrots","500 g"),("Spinach","2 bunches"),("Brinjal","500 g"),("Okra","250 g · swapped in")])}
<div class=wk><i>Sat 28</i><i class=sk>Sat 5 · skip</i><i>Sat 12</i></div>
<div class=bt><i>Swap items</i><i class=l>Skip a week</i></div></div>""", w=360, h=720)}</div>
<div class=pk><small>FRIDAY PACKING LIST · SAMPLE</small>{"".join(f'<em>{t}</em>' for t in ["48 boxes","Tomatoes 48 kg","Carrots 24 kg","Spinach 96 bunches","3 skipped this week"])}</div>''',
"#2f2216", "Farm or organic seller? DM us", "background:#4f8a2b;color:#fff")

# ───────── 119 CANADA · Music teacher · SINGLE · Cardo + DM Sans · ebony / ivory / brass
# New technique: a piano keyboard turned into a week calendar (each white key = one day, black keys between),
# lesson chips sit on the keys; practice tracker card underneath.
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
lessons = {0: [("4:00", "Piano · S1"), ("5:00", "Piano · S2")], 1: [("6:00", "Guitar · S3")], 2: [("4:30", "Piano · S4"), ("5:30", "Open")],
           3: [("6:00", "Piano · S5")], 4: [("5:00", "Open")], 5: [("10:00", "Piano · S6"), ("11:00", "Guitar · S7"), ("1:00", "Open")], 6: []}
practice = [("Mon", 30), ("Tue", 20), ("Wed", 0), ("Thu", 25), ("Fri", 30), ("Sat", 15), ("Sun", 0)]
P["p119_music"] = page("""
body{--f:'DM Sans';--h:'Cardo';background:#1c1815;color:#f4eee2}
h1{font-family:'Cardo';font-size:66px;font-weight:700;letter-spacing:-.3px;line-height:1.2} h1 span{color:#d6a64a}
.sub{color:#b9ae9c}
.vis{flex-direction:column;gap:16px}
.kb{flex:1;position:relative;display:flex;gap:6px;background:#0f0d0b;border-radius:24px;padding:14px 14px 16px;min-height:0;border-top:14px solid #5a3b22}
.wk{flex:1;background:linear-gradient(#fffdf6,#efe8d8);border-radius:0 0 12px 12px;display:flex;flex-direction:column;justify-content:flex-end;gap:8px;padding:10px 8px 14px;position:relative}
.wk b{font:700 20px 'DM Sans';color:#1c1815;text-align:center;margin-top:6px}
.ls{background:#1c1815;color:#f4eee2;border-radius:10px;padding:7px 8px;display:flex;flex-direction:column;gap:1px}
.ls em{font-style:normal;font:700 15px 'DM Sans';color:#d6a64a}.ls span{font:600 14px/1.25 'DM Sans'}
.ls.op{background:#fff;border:2px dashed #b08a3e;color:#7a5a1c}.ls.op em{color:#7a5a1c}
.wk.hb:after{content:'';position:absolute;top:0;right:-25px;width:44px;height:26%;background:linear-gradient(#2a2420,#0b0a09);border-radius:0 0 8px 8px;z-index:2}
.pt{flex:none;background:#2a241f;border-radius:22px;padding:16px 22px;display:flex;align-items:center;gap:22px}
.pt .l{width:280px;flex:none;display:flex;flex-direction:column;gap:4px}
.pt small{font:700 13px 'DM Sans';letter-spacing:3px;color:#a89c88}.pt .l b{font:700 28px/1.25 Cardo}.pt .l span{font:500 17px 'DM Sans';color:#cfc4b2}
.br{flex:1;display:flex;gap:10px;align-items:flex-end;height:120px}
.br div{flex:1;display:flex;flex-direction:column;align-items:center;gap:6px;height:100%;justify-content:flex-end}
.br i{display:block;width:100%;background:#d6a64a;border-radius:6px 6px 2px 2px}.br i.z{background:#4a4038;height:6px}
.br span{font:600 14px 'DM Sans';color:#a89c88}
""", "<h1>Lesson times in a<br>paper diary?<br><span>Let students book online.</span></h1><div class=sub>For music teachers: weekly lesson slots, open times to book, and a practice log.</div>",
f'''<div class=kb>{"".join(f'<div class="wk {"hb" if i in (0,1,3,4,5) else ""}">' + "".join(f'<div class="ls {"op" if t=="Open" else ""}"><em>{a}</em><span>{"Open · book" if t=="Open" else t}</span></div>' for a,t in lessons[i]) + f'<b>{d}</b></div>' for i,d in enumerate(days))}
</div>
<div class=pt><div class=l><small>PRACTICE LOG · SAMPLE</small><b>Student S1</b><span>5 of 7 days · 2 hrs</span></div>
<div class=br>{"".join(f'<div><i class="{"z" if m==0 else ""}" style="height:{m*3 if m else 6}px"></i><span>{d}</span></div>' for d,m in practice)}</div></div>''',
"#f4eee2", "Music teacher? DM us", "background:#d6a64a;color:#1c1815")

# ───────── 120 INDIA · Paint dealer · SINGLE · Anton + Open Sans · gallery white / ink / shade swatches
# New technique: SVG shade fan deck (strips rotated around one pivot), shade-coded order card, contractor account strip.
strips = [("#e8d9c0", "7-101"), ("#c9dcd2", "7-118"), ("#9cc3c9", "7-204"), ("#f2c96b", "7-233"), ("#e59a6d", "7-310"), ("#b5543c", "7-402"), ("#6d4f7a", "7-455"), ("#2f4858", "7-520")]
fan = '<svg viewBox="-30 0 540 440" width="{w}" height="{h}">' + "".join(
    f'<g transform="rotate({-50 + i*100/7:.1f} 240 410)"><rect x="216" y="100" width="48" height="310" rx="10" fill="{c}" stroke="#fff" stroke-width="3"/>'
    f'<rect x="216" y="100" width="48" height="54" rx="10" fill="#fff" opacity=".85"/><text x="240" y="133" text-anchor="middle" font-family="Open Sans" font-weight="700" font-size="13" fill="#20232a">{t}</text></g>'
    for i, (c, t) in enumerate(strips)) + '<circle cx="240" cy="410" r="16" fill="#20232a"/><circle cx="240" cy="410" r="6" fill="#fff"/></svg>'
order = [("Wall emulsion", "20 L", "#c9dcd2", "7-118 · Sea mist"), ("Wall emulsion", "10 L", "#f2c96b", "7-233 · Sunbeam"), ("Primer", "20 L", "#ffffff", "White"), ("Enamel", "4 L", "#b5543c", "7-402 · Brick")]
P["p120_paint"] = page("""
body{--f:'Open Sans';--h:'Anton';background:#f7f5f0;color:#20232a}
h1{font-family:'Anton';font-weight:400;font-size:68px;letter-spacing:.3px;line-height:1.25;margin-top:30px} h1 span{color:#b5543c}
.vis{gap:20px}
.fn{width:420px;flex:none;background:#20232a;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;padding:16px}
.fn svg{display:block}
.fn>b{font:400 30px/1.35 Anton;color:#fff;letter-spacing:.3px}
.hs{align-self:stretch;margin-top:10px;display:flex;flex-direction:column;gap:8px}.hs small{font:700 12px 'Open Sans';letter-spacing:3px;color:#8d919b}
.hs div{display:flex;align-items:center;gap:12px;background:#2c3038;border-radius:12px;padding:10px 14px}.hs i{width:28px;height:28px;border-radius:8px;flex:none}
.hs b{flex:1;font:700 19px 'Open Sans';color:#fff}.hs em{font-style:normal;font:700 17px 'Open Sans';color:#e6e2d8}.fn>span{font:600 17px 'Open Sans';color:#b8bcc6;text-align:center}
.rc{flex:1;display:flex;flex-direction:column;gap:14px;min-width:0}
.od{flex:1;background:#fff;border-radius:26px;padding:20px 22px;display:flex;flex-direction:column;gap:8px;box-shadow:0 16px 34px rgba(32,35,42,.08)}
.od small{font:700 13px 'Open Sans';letter-spacing:3px;color:#8d919b}
.od h3{font:400 32px/1.35 Anton;letter-spacing:.3px;margin-bottom:6px}
.od .s{font:600 17px 'Open Sans';color:#5c616b;margin-top:-4px}
.ln{flex:1;display:flex;align-items:center;gap:14px;border-top:1.5px solid #efede7}
.ln i{width:46px;height:46px;border-radius:12px;flex:none;border:2px solid #e2dfd6}
.ln div{flex:1;display:flex;flex-direction:column;gap:2px}.ln b{font:700 21px 'Open Sans'}.ln span{font:600 16px 'Open Sans';color:#6d717b}
.ln em{font-style:normal;font:700 20px 'Open Sans'}
.od .bt{display:flex;gap:10px;margin-top:4px}.od .bt u{flex:1;text-decoration:none;text-align:center;font:700 17px 'Open Sans';padding:12px 0;border-radius:12px;background:#20232a;color:#fff}
.od .bt u.l{background:#f1efe9;color:#20232a}
.ac{flex:none;background:#b5543c;color:#fff;border-radius:22px;padding:16px 20px;display:flex;gap:12px}
.ac div{flex:1;display:flex;flex-direction:column;gap:2px}.ac small{font:700 12px 'Open Sans';letter-spacing:2px;color:#f6d2c6}.ac b{font:400 26px/1.35 Anton;letter-spacing:.3px}
""", "<h1>Wrong shade sent<br>to the site again?<br><span>Save every order with<br>its shade code.</span></h1>",
f'''<div class=fn>{fan.format(w=388,h=300)}<b>Shade 7-118</b><span>Saved to Sample Painter 3 · Flat 402</span>
<div class=hs><small>SHADES BY SITE · SAMPLE</small>{"".join(f'<div><i style="background:{c}"></i><b>{a}</b><em>{t}</em></div>' for a,t,c in [("Flat 402","7-118","#c9dcd2"),("Shop 9","7-233","#f2c96b"),("Villa 3","7-402","#b5543c")])}</div></div>
<div class=rc><div class=od><small>PAINTER ORDER · SAMPLE</small><h3>Sample Painter 3</h3><div class=s>Site: Flat 402, Sample Heights · deliver today 4 pm</div>
{"".join(f'<div class=ln><i style="background:{c}"></i><div><b>{a}</b><span>{s}</span></div><em>{q}</em></div>' for a,q,c,s in order)}
<div class=bt><u>Send to godown</u><u class=l>Same as last site</u></div></div>
<div class=ac>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a,b in [("THIS MONTH","6 orders"),("SITES","3 open"),("BILLS DUE","2")])}</div></div>''',
"#20232a", "Paint dealer? DM us", "background:#b5543c;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
