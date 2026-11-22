import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 111 INDIA · Dhaba / highway restaurant · SINGLE · Montserrat + Roboto · mustard road / tar black / milestone red
# New techniques: SVG highway milestone with road, kitchen ticket rail with hanging order tickets and clips.
milestone = '''<svg viewBox="0 30 300 390" width="300" height="390">
<rect x="0" y="330" width="300" height="90" fill="#2b2a28"/><path d="M0 372 H300" stroke="#f2c230" stroke-width="6" stroke-dasharray="30 22"/>
<path d="M40 330 V160 A110 110 0 0 1 260 160 V330 Z" fill="#f7f4ec" stroke="#cfc8b8" stroke-width="4"/>
<path d="M40 160 A110 110 0 0 1 260 160 V176 H40 Z" fill="#c8402f"/>
<rect x="30" y="322" width="240" height="16" rx="4" fill="#bdb5a3"/>
<text x="150" y="128" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="22" fill="#fff">NH · SAMPLE</text>
<text x="150" y="214" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="27" fill="#2b2a28">Your Dhaba</text>
<text x="150" y="282" text-anchor="middle" font-family="Montserrat" font-weight="800" font-size="56" fill="#c8402f">2 km</text>
</svg>'''
items = [("Dal tadka", "40"), ("Tandoori roti", "160"), ("Paneer curry", "20"), ("Jeera rice", "40"), ("Tea", "40")]
tickets = [("Table 4", "2 thali<br>1 lassi<br>1 raita", "Cooking", "#fff7d6"), ("Truck group", "6 thali<br>6 tea<br>Pack 2 parathas", "Ready", "#e3f1e0"), ("Bus BS-12", "40 guests<br>Pre-ordered<br>5 dishes", "Starts 1:00 pm", "#fde3dc"), ("Table 9", "1 paratha<br>1 tea", "New", "#fff")]
P["p111_dhaba"] = page("""
body{--f:'Roboto';--h:'Montserrat';background:#f2c230;color:#1f1e1c}
h1{font-family:'Montserrat';font-size:60px;font-weight:800;letter-spacing:-1.5px} h1 span{color:#c8402f}
.sub{color:#5a4a12}
.vis{flex-direction:column;gap:16px}
.tp{flex:1;display:flex;gap:16px;min-height:0}
.ms{width:340px;flex:none;background:#1f1e1c;border-radius:28px;display:flex;flex-direction:column;align-items:center;justify-content:space-between;overflow:hidden;padding-top:22px}
.lk{background:#f2c230;color:#1f1e1c;border-radius:14px;padding:12px 16px;font:800 21px/1.3 Montserrat;text-align:center}
.ms svg{display:block}
.po{flex:1;background:#fff;border-radius:28px;padding:20px 24px;display:flex;flex-direction:column;gap:8px}
.po small{font:700 13px Roboto;letter-spacing:3px;color:#8d8670}
.po h3{font:800 28px/1.25 Montserrat}
.po .mt{display:flex;gap:8px;flex-wrap:wrap}.po .mt em{font-style:normal;font:700 16px Roboto;background:#fbf0c4;border-radius:8px;padding:6px 10px}
.po .it{flex:1;display:flex;justify-content:space-between;align-items:center;border-top:1.5px dashed #e6dfc8;font:500 21px Roboto}
.po .it b{font:800 24px Montserrat}
.rl{flex:none;height:250px;background:#1f1e1c;border-radius:28px;padding:0 20px 18px;display:flex;flex-direction:column}
.rl .bar{height:16px;background:#8d8a83;border-radius:0 0 8px 8px;margin:0 -4px}
.rl small{font:700 13px Roboto;letter-spacing:3px;color:#b8b2a2;padding:10px 4px 6px}
.tk{flex:1;display:flex;gap:14px}
.tc{flex:1;border-radius:4px 4px 12px 12px;padding:24px 14px 12px;display:flex;flex-direction:column;gap:4px;position:relative;margin-top:-8px}
.tc:before{content:"";position:absolute;left:50%;top:0px;width:44px;height:22px;margin-left:-22px;border-radius:6px;background:#c8c3b6;border:3px solid #6f6c66}
.tc b{font:800 23px/1.25 Montserrat}.tc span{font:500 19px/1.45 Roboto;color:#4f4a40;border-top:1.5px dashed rgba(0,0,0,.15);padding-top:4px}
.tc em{margin-top:auto;font-style:normal;font:700 15px Roboto;background:#1f1e1c;color:#fff;border-radius:8px;padding:6px 8px;align-self:flex-start}
""", "<h1>A bus of 40 stops<br>at your dhaba at once?<br><span>Take their order before<br>they arrive.</span></h1>",
f'''<div class=tp><div class=ms><div class=lk>Bus operators order<br>with your link</div>{milestone}</div>
<div class=po><small>BUS PRE-ORDER · SAMPLE</small><h3>Bus BS-12 · 40 guests</h3><div class=mt><em>Arriving 1:30 pm</em><em>Sent by bus operator</em></div>
{"".join(f'<div class=it><span>{a}</span><b>{b}</b></div>' for a,b in items)}</div></div>
<div class=rl><div class=bar></div><div class=tk>{"".join(f'<div class=tc style="background:{c}"><b>{a}</b><span>{b}</span><em>{s}</em></div>' for a,b,s,c in tickets)}</div></div>''',
"#1f1e1c", "Run a dhaba? DM us", "background:#c8402f;color:#fff")

# ───────── 113 USA · Real estate photographer · SINGLE · Lora + Inter · slate / warm white / sunset orange
# New technique: camera viewfinder overlay (corner brackets, rule-of-thirds grid, focus box, exposure strip) over an SVG room.
room = '''<svg viewBox="0 0 900 470" width="100%" height="100%" preserveAspectRatio="xMidYMid slice">
<rect width="900" height="470" fill="#efe7da"/><rect y="360" width="900" height="110" fill="#c9a77f"/>
<path d="M0 360 H900" stroke="#b08d64" stroke-width="4"/>
<g stroke="#c49b70" stroke-width="2" opacity=".6">''' + "".join(f'<path d="M{x} 360 L{x-60} 470"/>' for x in range(60, 960, 90)) + '''</g>
<rect x="520" y="60" width="300" height="230" rx="6" fill="#bfe0f2" stroke="#fff" stroke-width="12"/>
<path d="M670 60 V290 M520 175 H820" stroke="#fff" stroke-width="8"/>
<path d="M540 290 L600 210 L640 250 L700 170 L800 290 Z" fill="#9fcf9a" opacity=".8"/>
<rect x="120" y="250" width="340" height="110" rx="20" fill="#5d6b7a"/><rect x="100" y="220" width="380" height="60" rx="24" fill="#6f7f8f"/>
<rect x="140" y="230" width="90" height="46" rx="12" fill="#e98a4e"/><rect x="350" y="230" width="90" height="46" rx="12" fill="#f3c56b"/>
<rect x="120" y="360" width="16" height="22" fill="#3c4650"/><rect x="444" y="360" width="16" height="22" fill="#3c4650"/>
<ellipse cx="290" cy="420" rx="200" ry="26" fill="#e9dcc6"/>
<rect x="40" y="120" width="8" height="240" fill="#3c4650"/><path d="M14 120 H74 L60 70 H28 Z" fill="#f3c56b"/>
<rect x="840" y="280" width="44" height="80" rx="8" fill="#d77a45"/><path d="M862 280 C 820 220, 850 200, 862 240 C 874 200, 904 220, 862 280" fill="#5d8f55"/>
</svg>'''
P["p113_rephoto"] = page("""
body{--f:'Inter';--h:'Lora';background:#2c3440;color:#f6f1ea}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.8px} h1 span{color:#f2945a}
.sub{color:#b8c0cb}
.vis{flex-direction:column;gap:16px}
.vf{flex:1;position:relative;border-radius:24px;overflow:hidden;min-height:0}
.vf>svg{position:absolute;inset:0}
.th{position:absolute;inset:0;background:linear-gradient(90deg,transparent calc(33.3% - 1px),rgba(255,255,255,.55) calc(33.3% - 1px) calc(33.3% + 1px),transparent calc(33.3% + 1px) calc(66.6% - 1px),rgba(255,255,255,.55) calc(66.6% - 1px) calc(66.6% + 1px),transparent calc(66.6% + 1px)),linear-gradient(0deg,transparent calc(33.3% - 1px),rgba(255,255,255,.55) calc(33.3% - 1px) calc(33.3% + 1px),transparent calc(33.3% + 1px) calc(66.6% - 1px),rgba(255,255,255,.55) calc(66.6% - 1px) calc(66.6% + 1px),transparent calc(66.6% + 1px))}
.cn{position:absolute;width:56px;height:56px;border:5px solid #fff}
.c1{left:22px;top:22px;border-right:none;border-bottom:none}.c2{right:22px;top:22px;border-left:none;border-bottom:none}
.c3{left:22px;bottom:22px;border-right:none;border-top:none}.c4{right:22px;bottom:22px;border-left:none;border-top:none}
.fc{position:absolute;left:46%;top:42%;width:90px;height:70px;border:3px solid #f2945a}
.ex{position:absolute;left:50%;bottom:26px;transform:translateX(-50%);background:rgba(20,24,30,.72);border-radius:10px;padding:8px 16px;font:600 17px Inter;color:#fff;white-space:nowrap;letter-spacing:1px}
.tg{position:absolute;left:96px;top:30px;background:#f2945a;color:#2c3440;border-radius:8px;padding:6px 12px;font:700 16px Inter}
.bt{flex:none;display:flex;gap:16px}
.cdx{flex:1;background:#f6f1ea;color:#2c3440;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:6px}
.cdx small{font:700 13px Inter;letter-spacing:3px;color:#8a8f97}
.cdx h3{font:700 26px/1.25 Lora}
.cdx .r{display:flex;justify-content:space-between;gap:10px;font:500 18px Inter;color:#5f6670;border-top:1.5px solid #e6ddd0;padding-top:6px}
.cdx .r em{font-style:normal;font-weight:700;color:#2c3440}
.cdx .bn{display:flex;gap:8px;margin-top:4px}.cdx .bn i{flex:1;font-style:normal;text-align:center;font:700 17px Inter;padding:10px 0;border-radius:10px;background:#2c3440;color:#fff}
.cdx .bn i.l{background:#fff;color:#2c3440;border:2px solid #d9cfc0}
""", "<h1>“Are the photos ready?”<br><span>Book shoots and deliver<br>in one link.</span></h1><div class=sub>For real estate photographers: agents book online and download from one page.</div>",
f'''<div class=vf>{room}<div class=th></div><div class="cn c1"></div><div class="cn c2"></div><div class="cn c3"></div><div class="cn c4"></div><div class=fc></div>
<div class=tg>Living room · 12 of 32</div><div class=ex>ISO 200 · f/8 · 1/60 · HDR</div></div>
<div class=bt><div class=cdx><small>SHOOT BOOKING · SAMPLE</small><h3>14 Sample Pine St</h3>
<div class=r><span>Agent</span><em>Sample Realty Team</em></div><div class=r><span>Package</span><em>Photos + floor plan</em></div><div class=r><span>When</span><em>Thu, Nov 26 · 10 am</em></div></div>
<div class=cdx><small>DELIVERY · SAMPLE</small><h3>32 photos ready</h3>
<div class=r><span>Sizes</span><em>Listing size + print size</em></div><div class=r><span>Floor plan</span><em>PDF ready</em></div>
<div class=bn><i>Download all</i><i class=l>Share link</i></div></div></div>''',
"#f6f1ea", "Shoot real estate? DM us", "background:#f2945a;color:#2c3440")

# ───────── 115 INDIA · Content creator / influencer · SINGLE · Gelasio + Inter · lavender / ink / tangerine
# New technique: ring-bound planner page (spiral holes + wire loops) with a week of deliverables, next to a deal tracker.
week = [("Mon 7", "Reel draft · Brand 1", "d"), ("Tue 8", "Story x 3 · Brand 2", "l"), ("Wed 9", "", ""), ("Thu 10", "Reel live · Brand 1", "l"),
        ("Fri 11", "Send report · Brand 2", "r"), ("Sat 12", "Shoot · Brand 3", "d"), ("Sun 13", "Rest day", "o")]
deals = [("Brand 1 · sample", "1 reel + 2 stories", "Draft sent", "dr"), ("Brand 2 · sample", "3 stories", "Live", "lv"),
         ("Brand 3 · sample", "1 reel", "Brief received", "br"), ("Brand 4 · sample", "2 posts", "Payment pending", "pp"), ("Brand 5 · sample", "1 reel", "Paid", "pd")]
P["p115_creator"] = page("""
body{--f:'Inter';--h:'Gelasio';background:#e4dcf5;color:#1e1a33}
h1{font-family:'Gelasio';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#e2631f}
.sub{color:#5a5371}
.vis{gap:20px}
.pl{width:470px;flex:none;background:#fffdf7;border-radius:10px 24px 24px 10px;position:relative;padding:20px 22px 20px 74px;display:flex;flex-direction:column;gap:8px;box-shadow:0 18px 36px rgba(30,26,51,.14)}
.sp{position:absolute;left:14px;top:22px;bottom:22px;width:44px;display:flex;flex-direction:column;justify-content:space-between}
.sp i{display:block;height:16px;border-radius:8px;background:linear-gradient(90deg,#9a96a8,#e7e4ee 50%,#8a8698);position:relative}
.sp i:after{content:"";position:absolute;right:-6px;top:2px;width:12px;height:12px;border-radius:50%;background:#e4dcf5}
.pl small{font:700 13px Inter;letter-spacing:3px;color:#9690a8}
.pl h3{font:700 32px/1.25 Gelasio}
.dy{flex:1;display:flex;align-items:center;gap:12px;border-top:1.5px solid #ece7f5}
.dy b{width:70px;flex:none;font:700 18px Inter;color:#6a6386}
.dy span{flex:1;font:600 19px Inter;border-radius:10px;padding:9px 12px}
.dy span.d{background:#fde4d3;color:#8d3a0f}.dy span.l{background:#e0d6f7;color:#3d2f80}.dy span.r{background:#d9f0e4;color:#1f6b45}.dy span.o{color:#9690a8;font-style:italic}
.tr{flex:1;background:#1e1a33;color:#fff;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:10px;min-width:0}
.tr small{font:700 13px Inter;letter-spacing:3px;color:#a59fc0}
.tr h3{font:700 30px/1.25 Gelasio}
.dl{flex:1;background:#2b2647;border-radius:16px;padding:10px 16px;display:flex;flex-direction:column;justify-content:center;gap:6px}
.dl .t{display:flex;justify-content:space-between;align-items:center;gap:8px}
.dl b{font:700 20px Inter}.dl span{font:500 17px Inter;color:#c4bedb}
.dl em{font-style:normal;font:700 14px Inter;padding:5px 9px;border-radius:8px;white-space:nowrap}
.dr{background:#fde4d3;color:#8d3a0f}.lv{background:#e0d6f7;color:#3d2f80}.br{background:#fff;color:#1e1a33}.pp{background:#e2631f;color:#fff}.pd{background:#bfe8d1;color:#1f6b45}
""", "<h1>Brand deals lost in<br>DMs and notes?<br><span>Track every post, date<br>and payment.</span></h1>",
f'''<div class=pl><div class=sp>{"<i></i>"*12}</div><small>DECEMBER · WEEK 2 · SAMPLE</small><h3>This week</h3>
{"".join(f'<div class=dy><b>{a}</b><span class={k}>{b if b else "No posts due"}</span></div>' for a,b,k in week)}</div>
<div class=tr><small>DEAL TRACKER · SAMPLE</small><h3>5 brand deals</h3>
{"".join(f'<div class=dl><div class=t><b>{a}</b><em class={k}>{s}</em></div><span>{b}</span></div>' for a,b,s,k in deals)}</div>''',
"#1e1a33", "Creator? DM us", "background:#e2631f;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
