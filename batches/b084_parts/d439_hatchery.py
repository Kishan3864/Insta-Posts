
# ───────── 439 INDIA · Fish seed hatchery (carp fry and fingerlings for pond farmers) · SINGLE · Poppins + Inter · pond teal / fry silver / hatchery orange
# New technique: top-down round hatchery tanks with seeded fish glyphs (density from the tank count), ready-date rings,
# and a phone booking whose bag count is computed from quantity and a sample fish-per-bag rule.
PT9 = "#13616b"; OR9 = "#e8833a"; BG9 = "#eef5f4"; INK9b = "#17282b"; MU9b = "#5d6f72"
TK9 = [("T1", "Rohu", "Fingerling", 18000, "Ready"), ("T2", "Catla", "Fingerling", 12000, "Ready"), ("T3", "Mrigal", "Fingerling", 15000, "Ready"),
       ("T4", "Rohu", "Fry", 40000, "Fri 4 Dec"), ("T5", "Catla", "Fry", 30000, "Fri 4 Dec"), ("T6", "Mrigal", "Spawn", 90000, "Mon 14 Dec")]
BK9 = [("Rohu", 4000), ("Catla", 3000), ("Mrigal", 3000)]; PB9 = 500
QTY9 = sum(q for _, q in BK9); BAGS9 = math.ceil(QTY9 / PB9)
def tank9(seed, n, st):
    rnd = random.Random(seed); k = min(70, max(14, n // 1500)); fish = ""
    for _ in range(k):
        a = rnd.uniform(0, 6.28); r = math.sqrt(rnd.uniform(0, 1)) * 70; x, y = 100 + r * math.cos(a), 100 + r * math.sin(a); rot = rnd.randint(0, 359)
        fish += f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot})"><ellipse rx="7" ry="2.8" fill="#dfe9ea"/><path d="M-7 0 l-5 -3 v6 Z" fill="#dfe9ea"/></g>'
    ring = "#3fae6a" if st == "Ready" else OR9
    return f'''<svg viewBox="0 0 200 200" style="display:block;width:100%;height:auto"><circle cx="100" cy="100" r="96" fill="{ring}"/><circle cx="100" cy="100" r="86" fill="#c9d3d5"/><circle cx="100" cy="100" r="80" fill="{PT9}"/>{fish}<circle cx="100" cy="100" r="6" fill="#9fc7cb"/></svg>'''
APP9b = f'''<div class=ap9b><div class=hd><span>Book fish seed</span><b>Sample Farmer K</b><small>Pond 1 acre · Sample Village</small></div>
<div class=sz><span>Size</span><b>Fingerling, 2 to 3 inch</b></div>
{"".join(f'<div class=mx><span>{sp}</span><div class=st><i>−</i><b>{q:,}</b><i>+</i></div></div>' for sp, q in BK9)}
<div class=tt><span>Total</span><b>{QTY9:,} fish</b></div>
<div class=sz><span>Oxygen bags</span><b>{BAGS9} bags · {PB9} a bag</b></div><div class=sz><span>From tanks</span><b>T1 · T2 · T3</b></div><div class=sz><span>Pickup</span><b>Thu 26 Nov · 6 AM</b></div>
<div class=bt>Book and send to hatchery</div></div>'''
P["p439_hatchery"] = page(f"""
body{{--f:'Inter';--h:'Poppins';background:{BG9};color:{INK9b}}}
.kk{{font:700 16px/1.4 Inter;letter-spacing:3px;color:{OR9};margin-top:22px}}
h1{{font-family:'Poppins';font-weight:800;font-size:56px;line-height:1.2;letter-spacing:-1.5px;margin-top:14px}} h1 span{{color:{PT9}}}
.w9b{{flex:1;display:grid;grid-template-columns:minmax(0,1fr) 370px;gap:20px;min-height:0}}
.sm9b{{font:700 13px/1.4 Inter;letter-spacing:2px;color:{MU9b}}}
.cd9b{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(19,97,107,.08);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.lf9b{{display:flex;flex-direction:column;gap:14px;min-height:0}}.tk9{{flex:1}}.tk9 .g{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:8px 14px;align-content:space-evenly}}
.tk9 .t{{display:flex;flex-direction:column;align-items:center;gap:2px}}.tk9 .t svg{{width:160px!important}}.tk9 .t b{{font:700 18px/1.3 Poppins}}.tk9 .t span{{font:500 14px/1.3 Inter;color:{MU9b}}}.tk9 .t em{{font:700 13px/1.2 Inter;font-style:normal;border-radius:7px;padding:4px 8px;color:#fff;margin-top:2px}}
.lg9{{display:flex;gap:16px;font:600 15px/1.3 Inter}}.lg9 span{{display:flex;align-items:center;gap:8px}}.lg9 i{{width:16px;height:16px;border-radius:50%}}
.sm9c{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}.sm9c div{{background:{PT9};color:#fff;border-radius:18px;padding:12px 16px}}.sm9c b{{display:block;font:800 30px/1.2 Poppins;margin-bottom:4px}}.sm9c span{{font:500 15px/1.3 Inter;color:#cfe5e7}}
.ph9b{{display:flex;align-items:center}}
.ap9b{{flex:1;padding:6px 18px 18px;display:flex;flex-direction:column;gap:9px}}.ap9b .hd span{{font:600 13px/1.3 Inter;color:{MU9b}}}.ap9b .hd b{{display:block;font:700 20px/1.3 Poppins;color:{INK9b}}}.ap9b .hd small{{font:500 14px/1.3 Inter;color:{MU9b}}}
.ap9b .sz,.ap9b .mx,.ap9b .tt{{display:flex;justify-content:space-between;align-items:center;gap:8px;background:#f1f6f6;border-radius:12px;padding:10px 12px}}.ap9b span{{font:500 15px/1.3 Inter;color:{MU9b}}}.ap9b .sz b{{font:700 15px/1.3 Inter;color:{INK9b}}}
.ap9b .st{{display:flex;align-items:center;gap:10px}}.ap9b .st i{{width:28px;height:28px;border-radius:8px;background:#fff;border:1.5px solid #c6d6d7;font:700 18px/25px Inter;font-style:normal;text-align:center;color:{PT9}}}.ap9b .st b{{font:700 16px/1.3 Inter;color:{INK9b};min-width:52px;text-align:center}}
.ap9b .tt{{background:#fdeedf}}.ap9b .tt b{{font:800 18px/1.3 Poppins;color:#a65216}}
.ap9b .bt{{margin-top:auto;background:{PT9};color:#fff;border-radius:14px;padding:14px;text-align:center;font:700 16px/1.2 Inter}}
""", "<div class=kk>FISH SEED HATCHERY · POND FARMERS</div><h1>Seed bookings by phone call?<br><span>Every tank, every booking.</span></h1>",
f'''<div class=w9b><div class=lf9b><div class="cd9b tk9"><span class=sm9b>HATCHERY TANKS · MON 23 NOV · SAMPLE</span><div class=g>{"".join(f'<div class=t>{tank9(i + 3, n, st)}<b>{t} · {sp}</b><span>{sz} · {n:,}</span><em style="background:{"#3fae6a" if st == "Ready" else OR9}">{"Ready now" if st == "Ready" else "Ready " + st}</em></div>' for i, (t, sp, sz, n, st) in enumerate(TK9))}</div>
<div class=lg9><span><i style="background:#3fae6a"></i>Ready now</span><span><i style="background:{OR9}"></i>Growing</span></div></div>
<div class=sm9c><div><b>{sum(t[3] for t in TK9 if t[4] == "Ready"):,}</b><span>fingerlings ready now</span></div><div><b>{BAGS9} bags</b><span>to pack for Thu 26 Nov</span></div></div></div>
<div class=ph9b>{phone(APP9b, w=370, h=740)}</div></div>''',
INK9b, "Run a hatchery? DM us", f"background:{OR9};color:#fff")
