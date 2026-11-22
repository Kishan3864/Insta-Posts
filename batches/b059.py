import sys, random, math; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 311 INDIA · Pond fish farm · CAROUSEL 5 · Bitter + Source Sans 3 · pond green / aerator white / feed orange
# New technique: top-down pond map (bunds, rippled water, paddle aerators) + SVG growth line chart from sampling.
FF = """
body{--f:'Source Sans 3';--h:'Bitter';background:#e9f0e4;color:#183b2c}
.kk{font:700 16px/1.4 'Source Sans 3';letter-spacing:3px;color:#d46a12;margin-top:22px;align-self:flex-start}
h1{font-family:'Bitter';font-weight:800;font-size:64px;line-height:1.22;letter-spacing:-1px} h1 span{color:#2e7d54}
.cd{background:#fff;border-radius:22px;box-shadow:0 12px 28px rgba(24,59,44,.08)}
.cap{font:700 14px/1.4 'Source Sans 3';letter-spacing:2px;color:#6b7a70}
.nb{display:flex;align-items:center;gap:14px;background:#183b2c;color:#fff;border-radius:20px;padding:16px 20px;font:500 22px/1.4 'Source Sans 3'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#f39a3c;color:#183b2c}.nb b{color:#ffc27a}
"""
def ff(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#183b2c;color:#fff"):
    return page(FF + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#183b2c", cta, ctacss, tagline=f"{n} / 5")
ponds = [("P-1", 6000, 650, 6, "#3f8f6b"), ("P-2", 5000, 420, 4, "#4c9aa0"), ("P-3", 7000, 250, 3, "#5fa06a"), ("P-4", 4000, 800, 5, "#3a7f8a")]
def aer(x, y):
    return f'<g><circle cx="{x}" cy="{y}" r="22" fill="#ffffff" opacity=".85"/>' + "".join(f'<rect x="{x-3}" y="{y-28}" width="6" height="56" rx="3" fill="#183b2c" transform="rotate({a} {x} {y})"/>' for a in (0, 45, 90, 135)) + f'<circle cx="{x}" cy="{y}" r="8" fill="#f39a3c"/></g>'
def pondmap(w=None):
    rects = [(20, 20, 330, 300), (370, 20, 330, 300), (20, 340, 330, 300), (370, 340, 330, 300)]
    s = '<svg viewBox="0 0 720 660" class=pm><rect width="720" height="660" rx="24" fill="#a8835a"/>'
    for (x, y, w_, h), (n, c, g, f, col) in zip(rects, ponds):
        s += f'<rect x="{x}" y="{y}" width="{w_}" height="{h}" rx="18" fill="{col}"/>'
        s += "".join(f'<path d="M{x+30+i*60} {y+70+j*70} q15 -8 30 0" stroke="#ffffff" stroke-width="3" fill="none" opacity=".35"/>' for i in range(5) for j in range(3))
        s += aer(x + w_ - 50, y + h - 50)
        s += f'<rect x="{x+18}" y="{y+18}" width="96" height="44" rx="10" fill="#183b2c"/><text x="{x+66}" y="{y+48}" text-anchor="middle" font-family="Bitter" font-weight="800" font-size="24" fill="#fff">{n}</text>'
    return s + "</svg>"
P["p311_fish_s1"] = ff(1, "POND FISH FARM · 4 PONDS", "Feed, size, harvest?<br><span>See every pond in one place.</span>",
f'''<div class=w1><div class="cd mp1"><small class=cap>FARM MAP · SAMPLE</small>{pondmap()}</div>
<div class=bb1><span class=vn>{ic("chat",24)} You, every evening</span><p>“Did pond 2 get feed today? How big are the fish in pond 3 now?”</p></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.mp1{flex:1;min-height:0;padding:16px 20px;display:flex;flex-direction:column;gap:10px}
.pm{flex:1;min-height:0;width:100%;display:block}
.bb1{background:#183b2c;color:#fff;border-radius:22px 22px 22px 6px;padding:18px 22px}.vn{display:flex;align-items:center;gap:10px;font:700 16px 'Source Sans 3';color:#ffc27a;margin-bottom:6px}.bb1 p{font:500 24px/1.4 'Source Sans 3'}""")

P["p311_fish_s2"] = ff(2, "STEP 1 · FEED LOG FOR EVERY POND", "Feed given today?<br><span>One tap per pond.</span>",
f'''<div class=w2>{"".join(f'<div class="cd fr2"><b>{n}</b><div class=bg2>{"".join("<i class=fb></i>" for _ in range(f))}{"".join("<i class=fe></i>" for _ in range(6-f))}</div><div class=nm2><em>{f} bags</em><span>{"Morning + evening" if f>3 else "Morning only"}</span></div></div>' for n,c,g,f,col in ponds)}
<div class=nb><span class=ib>{ic("bell",26)}</span><span>Sample: 1 bag = 25 kg. <b>Missed a pond by 7 PM? You get a reminder.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.fr2{flex:1;display:grid;grid-template-columns:90px 1fr 210px;gap:16px;align-items:center;padding:12px 24px}
.fr2 b{font:800 30px/1.3 Bitter}.bg2{display:flex;gap:10px}.bg2 i{width:66px;height:86px;border-radius:10px 10px 14px 14px;position:relative}
.fb{background:linear-gradient(#f39a3c 0 22%,#e8e0c8 22% 100%);box-shadow:inset 0 -6px 0 #cfc5a8}.fe{border:3px dashed #b9c4bb}
.nm2 em{display:block;font:800 34px/1.3 Bitter;font-style:normal;color:#d46a12}.nm2 span{font:600 18px/1.4 'Source Sans 3';color:#5d6c62}""")

days = ["1 Oct", "16 Oct", "31 Oct", "15 Nov"]
grow = {"P-1": [380, 470, 560, 650], "P-2": [210, 280, 350, 420], "P-3": [90, 140, 195, 250], "P-4": [560, 640, 720, 800]}
def chart():
    W, H, L, B = 760, 520, 80, 450
    sx = lambda i: L + i * (W - L - 120) / 3
    sy = lambda g: B - g / 900 * (B - 30)
    s = f'<svg viewBox="0 0 {W} {H}" class=gc>'
    for g in range(0, 901, 300):
        s += f'<line x1="{L}" y1="{sy(g):.0f}" x2="{W-110}" y2="{sy(g):.0f}" stroke="#e2e9e2" stroke-width="2"/><text x="{L-12}" y="{sy(g)+7:.0f}" text-anchor="end" font-family="Source Sans 3" font-weight="600" font-size="20" fill="#6b7a70">{g} g</text>'
    for i, d in enumerate(days):
        s += f'<text x="{sx(i):.0f}" y="{B+40}" text-anchor="middle" font-family="Source Sans 3" font-weight="600" font-size="20" fill="#6b7a70">{d}</text>'
    for n, c, g, f, col in ponds:
        pts = " ".join(f"{sx(i):.0f},{sy(v):.0f}" for i, v in enumerate(grow[n]))
        s += f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="7" stroke-linejoin="round"/>' + "".join(f'<circle cx="{sx(i):.0f}" cy="{sy(v):.0f}" r="9" fill="#fff" stroke="{col}" stroke-width="5"/>' for i, v in enumerate(grow[n]))
        s += f'<text x="{sx(3)+22:.0f}" y="{sy(grow[n][3])+8:.0f}" font-family="Bitter" font-weight="800" font-size="24" fill="{col}">{n}</text>'
    return s + "</svg>"
P["p311_fish_s3"] = ff(3, "STEP 2 · NET A FEW FISH, WEIGH, NOTE", "How big are they now?<br><span>Growth by pond.</span>",
f'''<div class=w3><div class="cd ch3"><small class=cap>AVERAGE WEIGHT PER FISH · EVERY 15 DAYS · SAMPLE</small>{chart()}</div>
<div class=st3>{"".join(f'<div><b style="color:{col}">{n}</b><span>{g} g now</span></div>' for n,c,g,f,col in ponds)}</div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.ch3{flex:1;min-height:0;padding:18px 22px;display:flex;flex-direction:column;gap:8px}.gc{flex:1;min-height:0;width:100%;display:block}
.st3{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}.st3 div{background:#183b2c;border-radius:18px;padding:14px 18px;display:flex;align-items:center;gap:12px}.st3 b{font:800 30px/1.3 Bitter}.st3 span{font:600 20px/1.3 'Source Sans 3';color:#fff}""")

est = {n: c * g // 1000 for n, c, g, f, col in ponds}
buyers = [("Buyer B-1 · sample", 1200, "Mon 30 Nov · 5 AM"), ("Buyer B-2 · sample", 1000, "Mon 30 Nov · 7 AM"), ("Buyer B-3 · sample", 1000, "Tue 1 Dec · 5 AM")]
P["p311_fish_s4"] = ff(4, "STEP 3 · HARVEST BOOKED BY KG", "Pond P-4 is ready.<br><span>{:,} kg, all booked.</span>".format(sum(b[1] for b in buyers)),
f'''<div class=w4><div class="cd es4"><small class=cap>ESTIMATE · SAMPLE RULE</small><div class=eq4><div><b>{ponds[3][1]:,}</b><span>fish</span></div><i>×</i><div><b>{ponds[3][2]} g</b><span>average</span></div><i>=</i><div class=rs4><b>{est["P-4"]:,} kg</b><span>to sell</span></div></div></div>
<div class="cd by4"><small class=cap>BUYERS FOR POND P-4</small>{"".join(f'<div class=br4><div><b>{a}</b><span>{t}</span></div><div class=bar4><i style="width:{k/est["P-4"]*100:.1f}%"></i></div><em>{k:,} kg</em></div>' for a,k,t in buyers)}
<div class="br4 tt4"><div><b>Total booked</b></div><em>{sum(b[1] for b in buyers):,} of {est["P-4"]:,} kg</em></div></div></div>''',
css=""".w4{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}.es4{padding:18px 24px}.eq4{display:flex;align-items:center;justify-content:space-between;margin-top:8px}
.eq4 div{text-align:center}.eq4 b{display:block;font:800 48px/1.3 Bitter}.eq4 span{font:600 18px/1.4 'Source Sans 3';color:#6b7a70}.eq4 i{font:800 40px Bitter;font-style:normal;color:#d46a12}.rs4{background:#fff3e4;border-radius:18px;padding:8px 18px}.rs4 b{color:#d46a12}
.by4{flex:1;padding:18px 24px;display:flex;flex-direction:column}.br4{flex:1;display:grid;grid-template-columns:260px 1fr 130px;gap:16px;align-items:center;border-top:1px solid #e6ece6}
.br4 b{display:block;font:700 25px/1.35 'Source Sans 3'}.br4 span{font:500 19px 'Source Sans 3';color:#5d6c62}.bar4{height:34px;border-radius:13px;background:#e9f0e4;overflow:hidden}.bar4 i{display:block;height:100%;background:#3a7f8a}
.br4 em{font:800 30px/1.3 Bitter;font-style:normal;text-align:right}.tt4{flex:none;grid-template-columns:1fr auto;background:#183b2c;color:#fff;border-radius:16px;padding:12px 18px;margin-top:6px}.tt4 em{color:#ffc27a}""")

P["p311_fish_s5"] = ff(5, "YOUR TURN", "Run fish ponds?<br><span>Let's build your pond book.</span>",
f'''<div class=w5><div class="cd hp5">{pondmap()}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("bell","Feed log","With reminders"),("chart","Growth","Weight by pond"),("users","Buyers","Booked by kg"),("truck","Harvest day","Who comes when")])}</div>
<div class=q>How do you keep pond records today? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#d46a12;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;padding:16px;display:flex}.pm{flex:1;min-height:0;width:100%;display:block}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fff;border-radius:22px;padding:16px 22px;box-shadow:0 10px 22px rgba(24,59,44,.07)}
.ti .ib{width:66px;height:66px;border-radius:20px;background:#fff0dc;color:#d46a12}.ti b{display:block;font:800 25px/1.4 Bitter}.ti div span{font:500 19px/1.35 'Source Sans 3';color:#55645a}
.q{background:#183b2c;color:#fff;border-radius:22px;padding:20px 24px;font:600 24px/1.4 'Source Sans 3'}""")

# ───────── 312 INDIA · Pav supplier to street stalls · SINGLE · Lora + Inter · pav golden / tray red / flour white
# New technique: CSS pav trays (joined golden buns via radial gradients); faded buns = unsold pav returned.
def tray(back, cols=6, rows=4, bun=34):
    n = cols * rows
    return f'<div class=ty2 style="grid-template-columns:repeat({cols},{bun}px)">' + "".join(f'<i class="{"bk" if i >= n-back else ""}"></i>' for i in range(n)) + '</div>'
stalls = [("Stall S-1 · Station", 3, 0), ("Stall S-2 · College road", 4, 6), ("Stall S-3 · Bus depot", 2, 0), ("Stall S-4 · Market", 3, 10), ("Stall S-5 · Office park", 5, 2), ("Stall S-6 · Bridge corner", 2, 0)]
tom = sum(s[1] for s in stalls)
P["p312_pav"] = page("""
body{--f:'Inter';--h:'Lora';background:#fbf4e6;color:#3b1f14}
.kk{font:700 16px/1.4 'Inter';letter-spacing:3px;color:#b8322a;margin-top:22px}
h1{font-family:'Lora';font-weight:700;font-size:66px;line-height:1.22;letter-spacing:-.5px} h1 span{color:#b8322a}
.vw{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}
.gd2{flex:1;min-height:0;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px}
.sc2{background:#fff;border-radius:22px;padding:14px 16px;display:flex;flex-direction:column;gap:8px;box-shadow:0 12px 26px rgba(59,31,20,.07)}
.sc2 b{font:700 20px/1.35 Lora}.tw{flex:1;display:flex;align-items:center;justify-content:center;background:#b8322a;border-radius:14px;padding:10px}
.ty2{display:grid;gap:3px}.ty2 i{width:34px;height:34px;border-radius:9px;background:radial-gradient(circle at 40% 35%,#f8cf7e,#e09a3a 70%,#c57a22);box-shadow:inset 0 -3px 0 rgba(0,0,0,.12)}
.ty2 i.bk{background:#f3e6cf;box-shadow:inset 0 0 0 2px #e4c9a0}
.sc2 .rw{display:flex;justify-content:space-between;font:600 16px/1.35 Inter}.sc2 .rw em{font-style:normal;font-weight:700}
.bt2{display:grid;grid-template-columns:1fr 1.2fr;gap:12px}
.pl2{background:#3b1f14;color:#fff;border-radius:22px;padding:16px 20px;display:flex;align-items:center;gap:18px}.pl2 div small{display:block;font:700 13px/1.4 Inter;letter-spacing:2px;color:#f3c27a;margin-bottom:8px}.pl2 b{display:block;font:700 64px/1.3 Lora;color:#f8cf7e}.pl2 span{font:500 17px/1.4 Inter;color:#e9d8c8}
.ms2{background:#fff;border-radius:22px;padding:14px 18px;box-shadow:0 12px 26px rgba(59,31,20,.07)}.ms2 small{display:block;font:700 13px/1.4 Inter;letter-spacing:2px;color:#8a7466;margin-bottom:6px}
.ms2 p{font:500 19px/1.45 Inter;background:#fbf0dc;border-radius:14px 14px 14px 4px;padding:12px 14px}.ms2 b{color:#b8322a}
""", "<div class=kk>PAV SUPPLY · STREET FOOD STALLS</div><h1>How many trays tomorrow?<br><span>Stalls order by 9 PM.</span></h1>",
f'''<div class=vw><div class=gd2>{"".join(f'<div class=sc2><b>{n}</b><div class=tw>{tray(bk)}</div><div class=rw><span>Today {t} trays</span><em style="color:{"#b8322a" if bk else "#2f7a4a"}">{f"{bk} pav back" if bk else "All sold"}</em></div></div>' for n,t,bk in stalls)}</div>
<div class=bt2><div class=pl2><div><small>TOMORROW'S BAKE · SAMPLE</small><b>{tom}</b></div><span>trays from 6 stall orders.<br>1 tray = 24 pav, sample.</span></div>
<div class=ms2><small>MESSAGE TO STALL S-4 · SAMPLE</small><p>10 pav came back today. <b>Order 2 trays for tomorrow instead of 3?</b> Tap to confirm by 9 PM.</p></div></div></div>''',
"#3b1f14", "Supply bread or pav? DM us", "background:#b8322a;color:#fff")

# ───────── 313 USA · Tax preparer office · CAROUSEL 5 · Crimson Text + DM Sans · cream paper / forest ink / stamp red
# New technique: SVG fanned paper stack (lines only, no fake text) vs a clean per-client document checklist; week-grid booking heat map.
TX = """
body{--f:'DM Sans';--h:'Crimson Text';background:#f5f1e8;color:#1f3a2e}
.kk{font:700 16px/1.4 'DM Sans';letter-spacing:3px;color:#b23a2a;margin-top:22px;align-self:flex-start}
h1{font-family:'Crimson Text';font-weight:700;font-size:70px;line-height:1.2} h1 span{color:#b23a2a}
.cd{background:#fffdf8;border-radius:22px;box-shadow:0 12px 28px rgba(31,58,46,.08)}
.cap{font:700 14px/1.4 'DM Sans';letter-spacing:2px;color:#7b7a6e}
.nb{display:flex;align-items:center;gap:14px;background:#1f3a2e;color:#fff;border-radius:20px;padding:16px 20px;font:500 21px/1.45 'DM Sans'}.nb .ib{width:50px;height:50px;border-radius:14px;background:#e9c46a;color:#1f3a2e}.nb b{color:#f1d58e}
"""
def tx(n, kick, head, vis, css="", cta="Swipe", ctacss="background:#1f3a2e;color:#fff"):
    return page(TX + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, "#1f3a2e", cta, ctacss, tagline=f"{n} / 5")
def papers():
    s = '<svg viewBox="0 0 440 470" class=pp1>'
    for i, (a, dx, dy) in enumerate([(-14, 40, 70), (9, 70, 50), (-5, 60, 40), (16, 100, 60), (-9, 80, 30)]):
        s += f'<g transform="translate({dx+120} {dy+170}) rotate({a})"><rect x="-120" y="-150" width="240" height="310" rx="6" fill="#ffffff" stroke="#d6d0c0" stroke-width="2"/>'
        s += "".join(f'<rect x="-95" y="{-120+k*26}" width="{150 if k%3 else 190}" height="8" rx="4" fill="#e4dfd1"/>' for k in range(10))
        s += "</g>"
    return s + '<circle cx="360" cy="90" r="38" fill="#b23a2a"/><text x="360" y="102" text-anchor="middle" font-family="DM Sans" font-weight="700" font-size="34" fill="#fff">?</text></svg>'
P["p313_tax_s1"] = tx(1, "TAX PREP OFFICE · CLIENT DOCUMENTS", "Tax papers in 9 emails?<br><span>One checklist per client.</span>",
f'''<div class=w1><div class="cd pc1">{papers()}<div class=em1>{"".join(f'<div class=ml><span>{ic("send",18)}</span><div><b>{a}</b><span>{b}</span></div></div>' for a,b in [("Fwd: my W-2","Photo, a bit blurry"),("One more form!!","Found it in the car"),("Re: Re: what else?","Do you need the bank one?"),("Here is the 1099","I think it is the right one"),("Sorry, last one","Promise")])}</div></div>
<div class=nb><span class=ib>{ic("doc",26)}</span><span>Every season starts the same way. <b>It does not have to.</b></span></div></div>''',
css=""".w1{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.pc1{flex:1;min-height:0;padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:center}
.pp1{width:100%;display:block}.em1{display:flex;flex-direction:column;gap:12px}.ml{display:flex;gap:14px;align-items:center;background:#f3efe4;border-radius:14px;padding:16px 16px}
.ml>span{width:36px;height:36px;border-radius:10px;background:#1f3a2e;color:#fff;display:flex;align-items:center;justify-content:center;flex:none}.ml b{display:block;font:700 22px/1.3 'DM Sans'}.ml div span{font:500 18px/1.4 'DM Sans';color:#6b6a5e}""")

docs = [("W-2 · job 1", "Uploaded Mon 4 Jan", "y"), ("W-2 · job 2", "Uploaded Mon 4 Jan", "y"), ("1099-INT · bank interest", "Waiting · reminder sent", "n"),
        ("Mortgage interest form", "Uploaded Wed 6 Jan", "y"), ("Last year's return", "Already on file", "y"), ("Donation receipts", "Waiting · reminder sent", "n")]
dy = sum(1 for d in docs if d[2] == "y")
P["p313_tax_s2"] = tx(2, "STEP 1 · A CHECKLIST MADE FOR EACH CLIENT", "Clients upload.<br><span>You see what is missing.</span>",
f'''<div class=w2><div class="cd cl2"><div class=hd2><div><small class=cap>SAMPLE CLIENT · 2027 SEASON</small><b>Document checklist</b></div><em>{dy} of {len(docs)} in</em></div>
<div class=pb2><i style="width:{dy/len(docs)*100:.0f}%"></i></div>
{"".join(f'<div class="dr2 {k}"><i>{ic("check",18) if k=="y" else ic("clock",18)}</i><b>{a}</b><span>{b}</span></div>' for a,b,k in docs)}</div>
<div class=nb><span class=ib>{ic("bell",26)}</span><span>Missing items get a friendly reminder, <b>so you do not have to chase.</b></span></div></div>''',
css=""".w2{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.cl2{flex:1;padding:18px 26px;display:flex;flex-direction:column;gap:8px}
.hd2{display:flex;justify-content:space-between;align-items:flex-end}.hd2 small{display:block;margin-bottom:2px}.hd2 b{display:block;font:700 36px/1.3 'Crimson Text'}.hd2 em{font:700 22px 'DM Sans';font-style:normal;color:#b23a2a}
.pb2{height:16px;border-radius:8px;background:#ece6d6;overflow:hidden;margin:6px 0}.pb2 i{display:block;height:100%;background:#2f6b4f}
.dr2{flex:1;display:grid;grid-template-columns:44px 1fr auto;gap:14px;align-items:center;border-top:1px solid #eee8da}.dr2 i{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff}
.dr2.y i{background:#2f6b4f}.dr2.n i{background:#e9c46a;color:#1f3a2e}.dr2 b{font:700 22px 'DM Sans'}.dr2 span{font:500 18px 'DM Sans';color:#6b6a5e}.dr2.n span{color:#b23a2a;font-weight:700}""")

weeks = ["4 Jan", "11 Jan", "18 Jan", "25 Jan", "1 Feb", "8 Feb", "15 Feb", "22 Feb", "1 Mar", "8 Mar", "15 Mar", "22 Mar", "29 Mar", "5 Apr"]
load = [2, 4, 6, 9, 12, 14, 15, 15, 14, 15, 15, 15, 12, 8]
P["p313_tax_s3"] = tx(3, "STEP 2 · CLIENTS BOOK THEIR OWN SLOT", "No phone tag in March.<br><span>They book online.</span>",
f'''<div class=w3><div class="cd hm3"><small class=cap>BOOKED MEETINGS PER WEEK · 15 SLOTS · SAMPLE</small><div class=gr3>{"".join(f'<div class=wk><div class=cl3>{"".join(f"<i class={chr(98) if j < l else chr(101)}></i>" for j in range(15))}</div><span>{w}</span></div>' for w,l in zip(weeks,load))}</div>
<div class=lg3><span><i class=b></i>Booked</span><span><i class=e></i>Open</span><span>Weeks with 15 of 15 show as full on the booking page.</span></div></div>
<div class=nb><span class=ib>{ic("cal",26)}</span><span>Office or video, 30 minutes. <b>Early birds get January.</b></span></div></div>''',
css=""".w3{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hm3{flex:1;min-height:0;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.gr3{flex:1;min-height:0;display:grid;grid-template-columns:repeat(14,1fr);gap:8px}.wk{display:flex;flex-direction:column;gap:6px;min-height:0}
.cl3{flex:1;display:flex;flex-direction:column-reverse;gap:4px}.cl3 i{flex:1;border-radius:4px}.cl3 i.b{background:#2f6b4f}.cl3 i.e{background:#efe9da}
.wk span{font:600 13px/1.3 'DM Sans';color:#6b6a5e;text-align:center}
.lg3{display:flex;gap:20px;align-items:center;font:600 17px/1.4 'DM Sans'}.lg3 span{display:flex;align-items:center;gap:8px}.lg3 i{width:20px;height:20px;border-radius:5px}.lg3 i.b{background:#2f6b4f}.lg3 i.e{background:#efe9da;border:1px solid #d9d2bf}.lg3 span:last-child{color:#6b6a5e;font-weight:500}""")

cols = [("Documents in", ["Client C-14", "Client C-21", "Client C-08", "Client C-19", "Client C-23"], "#e9c46a"), ("Preparing", ["Client C-03", "Client C-17", "Client C-09", "Client C-12"], "#8fb8a0"), ("Your review", ["Client C-11", "Client C-05", "Client C-16"], "#f0a58f"), ("Ready to sign", ["Client C-02", "Client C-07"], "#2f6b4f")]
P["p313_tax_s4"] = tx(4, "STEP 3 · EVERY RETURN ON ONE BOARD", "Where is my return?<br><span>They can see it.</span>",
f'''<div class=w4>{"".join(f'<div class=col4><div class=ch4 style="background:{c};color:{"#fff" if c=="#2f6b4f" else "#1f3a2e"}"><b>{h}</b><em>{len(cs)}</em></div>{"".join(f"<div class=cc4><b>{x}</b><span>Sample · 2026 return</span></div>" for x in cs)}<div class=op4>Open for new clients</div></div>' for h,cs,c in cols)}</div>''',
css=""".w4{flex:1;display:grid;grid-template-columns:repeat(4,1fr);gap:12px;min-height:0}.col4{background:#ece6d6;border-radius:20px;padding:10px;display:flex;flex-direction:column;gap:10px}
.ch4{border-radius:14px;padding:12px 14px;display:flex;justify-content:space-between;align-items:center}.ch4 b{font:700 18px/1.3 'DM Sans'}.ch4 em{font:700 24px/1.3 'Crimson Text';font-style:normal}
.cc4{background:#fffdf8;border-radius:14px;padding:14px;box-shadow:0 6px 14px rgba(31,58,46,.06)}.cc4 b{display:block;font:700 24px/1.3 'Crimson Text'}.cc4 span{font:500 15px/1.4 'DM Sans';color:#6b6a5e}
.op4{flex:1;border:2.5px dashed #c9c0a8;border-radius:14px;display:flex;align-items:center;justify-content:center;text-align:center;padding:10px;font:600 16px/1.4 'DM Sans';color:#8a8676}""")

P["p313_tax_s5"] = tx(5, "YOUR TURN", "Prepare taxes for clients?<br><span>Let's build your client portal.</span>",
f'''<div class=w5><div class="cd hp5"><div class=mini>{"".join(f'<div class="dr2 {k}"><i>{ic("check",16) if k=="y" else ic("clock",16)}</i><b>{a}</b></div>' for a,b,k in docs)}</div>{papers()}</div>
<div class=tl5>{"".join(f'<div class=ti><span class=ib>{ic(i,36)}</span><div><b>{a}</b><span>{b}</span></div></div>' for i,a,b in [("doc","Checklists","Made per client"),("upload","Secure upload","Photos and PDFs"),("cal","Online booking","Office or video"),("grid","Status board","For you and clients")])}</div>
<div class=q>When do most clients send their papers to you? Tell us in the comments.</div></div>''',
cta="DM us to start", ctacss="background:#b23a2a;color:#fff",
css=""".w5{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}.hp5{flex:1;min-height:0;padding:20px;display:grid;grid-template-columns:1fr 1fr;gap:16px;align-items:center}.pp1{width:100%;display:block}
.mini{display:flex;flex-direction:column;gap:8px}.dr2{display:flex;gap:12px;align-items:center;background:#f3efe4;border-radius:12px;padding:10px 12px}.dr2 i{width:30px;height:30px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;flex:none}
.dr2.y i{background:#2f6b4f}.dr2.n i{background:#e9c46a;color:#1f3a2e}.dr2 b{font:700 17px/1.3 'DM Sans'}
.tl5{display:grid;grid-template-columns:1fr 1fr;gap:12px}.ti{display:flex;align-items:center;gap:16px;background:#fffdf8;border-radius:22px;padding:16px 22px;box-shadow:0 10px 22px rgba(31,58,46,.07)}
.ti .ib{width:66px;height:66px;border-radius:20px;background:#f4e7c1;color:#1f3a2e}.ti b{display:block;font:700 27px/1.3 'Crimson Text'}.ti div span{font:500 18px/1.35 'DM Sans';color:#5e5d52}
.q{background:#1f3a2e;color:#fff;border-radius:22px;padding:20px 24px;font:600 23px/1.4 'DM Sans'}""")

# ───────── 314 CANADA · Skate sharpening shop · SINGLE · Archivo Black + Open Sans · rink blue / hockey black / blade steel
# New technique: SVG skate side profile with steel blade + drop-off tag, and blade cross-sections showing the hollow depth options.
skate = '''<svg viewBox="0 0 620 420" class=sk><defs><linearGradient id="st" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#f4f7fa"/><stop offset=".5" stop-color="#b9c4cf"/><stop offset="1" stop-color="#7d8a97"/></linearGradient></defs>
<path d="M120 40 L300 30 Q330 30 335 60 L345 170 Q450 180 520 205 Q560 220 555 260 L555 280 L110 280 Q90 280 92 250 L100 70 Q102 42 120 40 Z" fill="#1c1f24"/>
<path d="M300 34 L310 170" stroke="#3a4049" stroke-width="10"/>''' + "".join(f'<circle cx="{350+i*30}" cy="{190+i*6}" r="6" fill="#d7dde3"/>' for i in range(5)) + '''
<rect x="110" y="280" width="445" height="34" rx="8" fill="#2d6fb5"/>
<rect x="140" y="314" width="40" height="40" fill="#2d6fb5"/><rect x="470" y="314" width="40" height="40" fill="#2d6fb5"/>
<path d="M90 354 Q90 340 110 340 L540 340 Q585 345 590 372 Q560 388 520 388 L120 388 Q92 386 90 354 Z" fill="url(#st)" stroke="#5d6975" stroke-width="3"/>
<path d="M120 378 L540 378" stroke="#ffffff" stroke-width="3" opacity=".9"/></svg>'''
def xsec(d, on):
    # blade cross-section with a hollow of depth d px
    return f'''<div class="xs{" on" if on else ""}"><svg viewBox="0 0 120 150" width="96"><path d="M30 10 H90 V130 Q60 {130-d} 30 130 Z" fill="#b9c4cf" stroke="#5d6975" stroke-width="3"/><path d="M30 130 Q60 {130-d} 90 130" stroke="#d1462f" stroke-width="5" fill="none"/></svg>'''
hol = [("3/8 in", 22, "More bite"), ("1/2 in", 15, "Most common"), ("5/8 in", 9, "More glide")]
P["p314_skate"] = page("""
body{--f:'Open Sans';--h:'Archivo Black';background:#e4eef7;color:#1c1f24}
.kk{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:#2d6fb5;margin-top:22px}
h1{font-family:'Archivo Black';font-weight:400;font-size:60px;letter-spacing:-1px;line-height:1.25;margin-top:30px} h1 span{color:#2d6fb5}
.vw{flex:1;display:flex;flex-direction:column;gap:12px;min-height:0}
.hero{flex:1;min-height:0;background:#fff;border-radius:26px;padding:16px 22px;display:grid;grid-template-columns:1fr 250px;gap:16px;align-items:center;box-shadow:0 14px 30px rgba(28,31,36,.08)}
.sk{width:100%;display:block}
.tg4{background:#f7d64a;border-radius:16px;padding:16px 18px;position:relative;box-shadow:0 10px 20px rgba(0,0,0,.12)}
.tg4::before{content:"";position:absolute;left:50%;top:10px;width:18px;height:18px;margin-left:-9px;border-radius:50%;background:#fff;box-shadow:inset 0 0 0 3px #c9a922}
.tg4 small{display:block;font:700 13px/1.4 'Open Sans';letter-spacing:2px;margin-top:22px;color:#6a5a10}.tg4 b{display:block;font:400 40px/1.3 'Archivo Black'}
.tg4 div{display:flex;justify-content:space-between;font:600 16px/1.4 'Open Sans';border-top:1.5px dashed #c9a922;padding-top:6px;margin-top:6px}.tg4 div em{font-style:normal;font-weight:800}
.hl{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.xs{background:#fff;border-radius:20px;padding:10px 14px;display:flex;align-items:center;gap:10px;border:3px solid transparent;box-shadow:0 10px 22px rgba(28,31,36,.06)}.xs.on{border-color:#2d6fb5}
.xs svg{flex:none;display:block}.xs b{display:block;font:400 26px/1.3 'Archivo Black'}.xs span{font:600 15px/1.4 'Open Sans';color:#5a6570}.xs em{display:inline-block;margin-top:4px;font:700 13px 'Open Sans';font-style:normal;background:#2d6fb5;color:#fff;border-radius:8px;padding:3px 8px}
.bt4{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.rk{background:#1c1f24;color:#fff;border-radius:22px;padding:14px 18px}.rk small,.tx4 small{display:block;font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:#9fc3ea;margin-bottom:4px}
.rr{display:flex;justify-content:space-between;padding:6px 0;border-top:1px solid #343a43;font:600 16px/1.4 'Open Sans'}.rr em{font-style:normal;font-weight:700;color:#f7d64a}
.tx4{background:#2d6fb5;color:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;justify-content:center}.tx4 small{color:#d4e6fa}.tx4 p{font:500 18px/1.45 'Open Sans';background:rgba(255,255,255,.15);border-radius:14px 14px 14px 4px;padding:12px 14px}.tx4 b{color:#ffe98a}
""", "<div class=kk>SKATE SHARPENING · DROP-OFF</div><h1>Skates dropped off at 4?<br><span>Text them at 6.</span></h1>",
f'''<div class=vw><div class=hero>{skate}<div class=tg4><small>TAG S-14 · SAMPLE</small><b>S-14</b><div><span>Hollow</span><em>1/2 in</em></div><div><span>Pairs</span><em>1</em></div><div><span>Ready</span><em>Today 6 PM</em></div></div></div>
<div class=hl>{"".join(f'{xsec(d, a=="1/2 in")}<div><b>{a}</b><span>{t}</span>{"<br><em>Saved for S-14</em>" if a=="1/2 in" else ""}</div></div>' for a,d,t in hol)}</div>
<div class=bt4><div class=rk><small>TODAY'S RACK · SAMPLE</small>{"".join(f'<div class=rr><span>{a}</span><em>{b}</em></div>' for a,b in [("S-12 · 2 pairs","Ready"),("S-13 · 1 pair","Ready"),("S-14 · 1 pair","6 PM"),("S-15 · 3 pairs","7 PM")])}</div>
<div class=tx4><small>TEXT SENT · SAMPLE</small><p>Your skates (tag <b>S-14</b>, 1/2 in hollow) are ready. Pick up before 9 PM.</p></div></div></div>''',
"#1c1f24", "Sharpen skates? DM us", "background:#1c1f24;color:#f7d64a")

# ───────── 315 INDIA · Driver on call (for your own car) · SINGLE · Montserrat + Fira Sans · night navy / headlight yellow / white · PHONE
# New technique: driver duty ribbon board (hour blocks positioned by %) beside a phone booking screen.
drv = [("D-01", [(7, 11, "B-201"), (13, 18, "B-207")]), ("D-02", [(8, 20, "B-202 · outstation")]), ("D-03", [(9, 13, "B-203"), (16, 22, "B-209")]),
       ("D-04", [(6, 10, "B-204")]), ("D-05", [(10, 14, "B-205"), (18, 23, "B-210")]), ("D-06", [])]
T0, T1 = 6, 24
free = [d for d, b in drv if not b]
ph = phone(f'''<div class=ap><div class=ah><small>SAMPLE DRIVER SERVICE</small><b>Book a driver</b><span>For your own car</span></div>
<div class=fl6><small>YOUR CAR</small><div class=ch6>{"".join(f'<span class="{"on" if a in ("Sedan","Automatic") else ""}">{a}</span>' for a in ["Hatchback","Sedan","Manual","Automatic"])}</div></div>
<div class=fl6><small>WHEN</small><div class=tx6>Sat 28 Nov · 7 PM</div></div>
<div class=fl6><small>HOW LONG</small><div class=ch6 style="grid-template-columns:repeat(4,1fr)">{"".join(f'<span class="{"on" if a=="4 h" else ""}">{a}</span>' for a in ["2 h","4 h","8 h","12 h"])}</div></div>
<div class=fl6><small>TRIP</small><div class=tx6>In city · wedding hall and back</div></div>
<div class=dc6><span class=av>{ic("users",22)}</span><div><b>Driver D-06</b><span>Licence checked · sample</span></div></div>
<div class=bk6>Confirm booking</div></div>''', 360, 840)
P["p315_driver"] = page("""
body{--f:'Fira Sans';--h:'Montserrat';background:#152033;color:#fff}
.kk{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:#ffd23f;margin-top:22px}
h1{font-family:'Montserrat';font-weight:800;font-size:62px;letter-spacing:-1.8px;line-height:1.2} h1 span{color:#ffd23f}
.vw{flex:1;display:flex;gap:16px;min-height:0}
.bd{flex:1;min-width:0;background:#1e2d45;border-radius:26px;padding:16px 18px;display:flex;flex-direction:column;gap:8px}
.bd>small{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:#9fb3d1}
.dr{flex:1;display:grid;grid-template-columns:64px 1fr;gap:10px;align-items:center}.dr b{font:800 20px Montserrat}
.rb{position:relative;height:64px;border-radius:12px;background:repeating-linear-gradient(90deg,#26385a 0 calc(100%/6 - 2px),#2e4268 calc(100%/6 - 2px) calc(100%/6))}
.bl{position:absolute;top:7px;bottom:7px;border-radius:9px;background:#ffd23f;color:#152033;padding:4px 8px;display:flex;align-items:center;font:700 14px/1.3 'Fira Sans';overflow:hidden;white-space:nowrap}
.bl.nw{background:#fff;box-shadow:inset 0 0 0 3px #ffd23f}
.ax{position:relative;height:22px;margin-left:74px;font:600 13px/1.5 'Fira Sans';color:#9fb3d1}.ax span{position:absolute;top:0}
.nt{background:#ffd23f;color:#152033;border-radius:16px;padding:12px 14px;font:600 17px/1.4 'Fira Sans'}
.ap{display:flex;flex-direction:column;gap:9px;padding:8px 18px 18px;flex:1;min-height:0;color:#152033}
.ah small{display:block;font:700 11px/1.4 'Fira Sans';letter-spacing:2px;color:#6a7a90}.ah b{display:block;font:800 24px/1.3 Montserrat}.ah span{font:500 14px/1.4 'Fira Sans';color:#4a5a70}
.fl6{background:#eef2f8;border-radius:14px;padding:9px 12px}.fl6 small{display:block;font:700 11px/1.4 'Fira Sans';letter-spacing:1.5px;color:#6a7a90;margin-bottom:6px}
.ch6{display:grid;grid-template-columns:1fr 1fr;gap:6px}.ch6 span{background:#fff;border-radius:10px;padding:7px 2px;text-align:center;font:600 14px 'Fira Sans';border:1.5px solid #d3dbe8}.ch6 .on{background:#152033;color:#ffd23f;border-color:#152033}
.tx6{font:600 15px/1.4 'Fira Sans'}
.dc6{display:flex;align-items:center;gap:12px;background:#fff6d6;border-radius:14px;padding:10px 12px}.av{width:40px;height:40px;border-radius:50%;background:#152033;color:#ffd23f;display:flex;align-items:center;justify-content:center;flex:none}.dc6 b{display:block;font:800 16px/1.3 Montserrat}.dc6 span{font:500 13px 'Fira Sans';color:#5a6a80}
.bk6{margin-top:auto;background:#ffd23f;color:#152033;border-radius:14px;padding:13px;text-align:center;font:800 17px Montserrat}
""", "<div class=kk>DRIVER ON CALL · FOR YOUR OWN CAR</div><h1>“Need a driver tonight.”<br><span>Booked in one minute.</span></h1>",
f'''<div class=vw><div class=bd><small>DRIVER DUTY BOARD · SAT 28 NOV · SAMPLE</small>{"".join(f'<div class=dr><b>{d}</b><div class=rb>{"".join(f"<span class=bl style=left:{(a-T0)/(T1-T0)*100:.1f}%;width:{(b-a)/(T1-T0)*100:.1f}%>{t}</span>" for a,b,t in bk)}{"<span class=\"bl nw\" style=\"left:" + f"{(19-T0)/(T1-T0)*100:.1f}%;width:{4/(T1-T0)*100:.1f}%" + "\">New</span>" if d=="D-06" else ""}</div></div>' for d,bk in drv)}
<div class=ax>{"".join(f'<span style="left:{(h-T0)/(T1-T0)*100:.1f}%">{l}</span>' for h,l in [(6,"6 AM"),(12,"12 PM"),(18,"6 PM")])}</div>
<div class=nt>New booking 7 PM – 11 PM goes to D-06, the free driver.</div></div>
{ph}</div>''',
"#ffffff", "Run a driver service? DM us", "background:#ffd23f;color:#152033", logo_color="#ffffff")


if __name__ == "__main__":
    import asyncio
    keys_ = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys_))
