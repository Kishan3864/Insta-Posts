
# ───────── 420 CANADA · Mobile welder · CAROUSEL 5 · Poppins + Roboto · arc blue / steel grey / spark orange
# New technique: blurred SVG "phone photos" (feGaussianBlur) vs sharp form thumbnails, a day ribbon with hatched drive
# blocks placed by minutes, and a before/after weld pair (crack vs rippled bead) on the job card; times match across slides.
AB0 = "#2b6cf0"; SG0 = "#e7eaee"; OR0 = "#ff7a1a"; DK0 = "#151a22"
def photo0(kind, blur=0, uid="p", w=170, h=120):
    f = f'<filter id="bl{uid}"><feGaussianBlur stdDeviation="{blur}"/></filter>' if blur else ""
    g = f' filter="url(#bl{uid})"' if blur else ""
    if kind == "hitch":
        art = f'<rect width="170" height="120" fill="#8fa3b3"/><rect y="78" width="170" height="42" fill="#6e6a5d"/><path d="M0 70 L120 58 L150 58 L150 74 L0 86 Z" fill="#3b4048"/><circle cx="150" cy="66" r="16" fill="#2a2e34"/><path d="M70 62 L78 70 L72 76 L80 84" stroke="{OR0 if not blur else "#3b4048"}" stroke-width="3" fill="none"/>'
    elif kind == "gate":
        art = '<rect width="170" height="120" fill="#a9c2d6"/><rect y="88" width="170" height="32" fill="#7d9a5b"/>' + "".join(f'<rect x="{30 + k * 22}" y="30" width="6" height="64" fill="#4d545e"/>' for k in range(5)) + '<rect x="26" y="30" width="104" height="7" fill="#4d545e"/><rect x="26" y="86" width="104" height="7" fill="#4d545e"/><rect x="134" y="20" width="12" height="80" fill="#5b4a3a"/><rect x="126" y="40" width="10" height="8" fill="#c0392b"/>'
    elif kind == "bucket":
        art = '<rect width="170" height="120" fill="#c9b79a"/><path d="M20 30 L150 30 L140 90 L30 90 Z" fill="#e0a52a"/><path d="M30 90 L140 90 L136 100 L34 100 Z" fill="#5d5f63"/>' + "".join(f'<path d="M{40 + k * 22} 100 L{48 + k * 22} 112 L{56 + k * 22} 100 Z" fill="#5d5f63"/>' for k in range(5))
    elif kind == "trailer":
        art = '<rect width="170" height="120" fill="#bcd3e4"/><rect y="90" width="170" height="30" fill="#8a9a6a"/><rect x="40" y="40" width="120" height="40" fill="#d8dde3" stroke="#5d6670" stroke-width="2"/><circle cx="100" cy="86" r="12" fill="#2a2e34"/><path d="M40 74 L6 80" stroke="#3b4048" stroke-width="5"/><circle cx="10" cy="80" r="11" fill="none" stroke="#ff7a1a" stroke-width="3"/>'
    elif kind == "tape":
        art = '<rect width="170" height="120" fill="#6e6a5d"/><path d="M0 60 L170 48 L170 66 L0 78 Z" fill="#3b4048"/><rect x="20" y="30" width="130" height="18" fill="#f2c230" transform="rotate(-4 85 39)"/>' + "".join(f'<rect x="{26 + k * 12}" y="30" width="2" height="9" fill="#1b1b1b" transform="rotate(-4 85 39)"/>' for k in range(10)) + '<text x="60" y="104" font-family="Roboto" font-weight="700" font-size="16" fill="#fff"><tspan>¼ in wall</tspan></text>'
    elif kind == "weld":
        art = '<rect width="170" height="120" fill="#8fa3b3"/><rect y="78" width="170" height="42" fill="#6e6a5d"/><path d="M0 70 L120 58 L150 58 L150 74 L0 86 Z" fill="#3b4048"/><circle cx="150" cy="66" r="16" fill="#2a2e34"/><path d="M58 60 L100 68 L100 80 L58 72 Z" fill="#55606b" stroke="#8a96a3" stroke-width="1.5"/>' + "".join(f'<path d="M{62 + k * 6} {61 + k * 1.2:.1f} q3 4 0 9" stroke="#b9c3cc" stroke-width="2" fill="none"/>' for k in range(6))
    return f'<svg viewBox="0 0 170 120" width="{w}" height="{h}" style="display:block;flex:none;border-radius:12px"><defs>{f}<clipPath id="cp{uid}"><rect width="170" height="120" rx="12"/></clipPath></defs><g clip-path="url(#cp{uid})"><g{g}>{art}</g></g></svg>'

B0 = f"""
body{{--f:'Roboto';--h:'Poppins';background:{SG0};color:{DK0}}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{OR0};margin-top:22px;align-self:flex-start}}
h1{{font-family:'Poppins';font-weight:800;font-size:58px;line-height:1.2;letter-spacing:-1.5px;margin-top:18px}} h1 span{{color:{AB0}}}
.sm0{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:#68717c}}
.cd0{{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(21,26,34,.08)}}
.dk0{{background:{DK0};color:#fff;border-radius:24px}}.dk0 .sm0{{color:#9fb0c6}}
.ch0{{display:inline-block;font:700 18px/1.2 Roboto;border-radius:10px;padding:9px 13px;background:#e3ebfd;color:{AB0}}}.ch0.on{{background:{AB0};color:#fff}}.ch0.ms{{background:#fff0e5;color:#b4500b;border:1.5px dashed {OR0}}}
"""
def t0(n, kick, head, vis, css="", cta="Swipe", ctacss=f"background:{DK0};color:#fff"):
    return page(B0 + css, f"<div class=kk>{kick}</div><h1>{head}</h1>", vis, DK0, cta, ctacss, tagline=f"{n} / 5")

TX0 = [("hitch", "Trailer hitch cracked. Can you come today?", ["Where is the crack?", "Steel or aluminum?", "Can a truck reach it?"]),
       ("gate", "Gate hinge snapped off.", ["How wide is the gate?", "Power on site?"]),
       ("bucket", "Loader bucket edge is worn out.", ["Which machine?", "Inside a shop or outside?"])]
P["p420_weld_s1"] = t0(1, "MOBILE WELDING · FARM, TRAILER, GATE", "Weld jobs from blurry texts?<br><span>Ask the right things first.</span>",
f'''<div class=w01>{"".join(f'<div class="cd0 tx01">{photo0(k, 4.5, f"s1{i}")}<div class=bd01><span class=sm0>TEXT · SAMPLE CUSTOMER {i + 1}</span><p>“{m}”</p><div class=ms01>{"".join(f"<span class='ch0 ms'>{q}</span>" for q in qs)}</div></div></div>' for i, (k, m, qs) in enumerate(TX0))}
<div class="dk0 bt01"><span class=sm0>WHAT IT COSTS YOU</span><p>Every unclear text means calls back and forth, the wrong rods in the truck, or a second trip.</p></div></div>''',
css=f""".w01{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.tx01{{flex:1;display:flex;gap:20px;align-items:center;padding:16px 20px}}
.tx01 svg{{width:240px!important;height:170px!important}}.bd01{{flex:1;display:flex;flex-direction:column;gap:8px}}.bd01 p{{font:600 28px/1.35 Poppins;text-wrap:pretty}}.ms01{{display:flex;flex-wrap:wrap;gap:8px}}
.bt01{{padding:18px 24px;display:flex;flex-direction:column;gap:6px}}.bt01 p{{font:600 24px/1.4 Poppins;text-wrap:pretty}}""")

def fld0(lab, val, full=False):
    return f'<div class="fd02{" fl" if full else ""}"><span>{lab}</span><div>{val}</div></div>'
FORM0 = "".join([
    fld0("Job type", "".join(f"<span class='ch0{' on' if o == 'Trailer' else ''}'>{o}</span>" for o in ["Trailer", "Gate", "Farm equipment", "Railing"]), True),
    fld0("Photos (3)", "".join(photo0(k, 0, f"s2{k}", 150, 106) for k in ["hitch", "trailer", "tape"]), True),
    fld0("Where is the damage?", "<b>Hitch coupler, crack on the left weld</b>", True),
    fld0("Metal", "".join(f"<span class='ch0{' on' if o == 'Steel' else ''}'>{o}</span>" for o in ["Steel", "Aluminum", "Not sure"])),
    fld0("Thickness", "<b>About ¼ in</b>"),
    fld0("Power on site", "".join(f"<span class='ch0{' on' if o == 'No' else ''}'>{o}</span>" for o in ["Yes", "No"]) + "<em>We bring a generator</em>"),
    fld0("Truck access", "<b>Can park within 50 ft</b>"),
    fld0("Area", "<b>Sample Township · 22 km</b>"),
    fld0("Best day", "<b>Wed 25 Nov · morning</b>"),
])
P["p420_weld_s2"] = t0(2, "1 · REQUEST FORM", "One form, all the details.<br><span>Before you load the truck.</span>",
f'''<div class=w02>{browser(f'<div class=fm02><div class=hd02><b>Request a weld job</b><span class=sm0>SAMPLE REQUEST · J-31</span></div><div class=gd02>{FORM0}</div><div class=bt02>Send request</div></div>', "yourwelding.ca/request", "flex:1;display:flex")}</div>''',
css=f""".w02{{flex:1;display:flex;min-height:0}}.browser{{width:100%}}.fm02{{flex:1;display:flex;flex-direction:column;gap:12px;padding:18px 26px 22px}}.hd02{{display:flex;justify-content:space-between;align-items:center}}.hd02 b{{font:800 26px/1.3 Poppins}}
.gd02{{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:12px 16px;align-content:space-between}}.fd02{{display:flex;flex-direction:column;gap:8px;border:1.5px solid #dfe4ea;border-radius:14px;padding:12px 14px}}.fd02.fl{{grid-column:1/3}}
.fd02>span{{font:700 13px/1.3 Roboto;letter-spacing:1px;text-transform:uppercase;color:#68717c}}.fd02>div{{display:flex;flex-wrap:wrap;gap:8px;align-items:center}}.fd02 b{{font:600 22px/1.3 Roboto}}.fd02 em{{font:500 17px/1.3 Roboto;font-style:normal;color:#68717c}}
.fd02 svg{{width:190px!important;height:134px!important}}.bt02{{background:{OR0};color:#fff;border-radius:14px;padding:15px;text-align:center;font:800 18px/1.2 Poppins}}""")

def mn0(t):
    h, m = t; return (h - 7) * 60 + m
DAY0 = [("d", (7, 30), (8, 0), ""), ("j", (8, 0), (9, 30), "J-31"), ("d", (9, 30), (10, 15), ""), ("j", (10, 15), (11, 15), "J-32"), ("d", (11, 15), (12, 30), ""), ("j", (12, 30), (14, 30), "J-33"), ("d", (14, 30), (15, 15), "")]
SPAN0 = 600
def hm0(t):
    h, m = t; return f"{(h - 1) % 12 + 1}:{m:02d} {'AM' if h < 12 else 'PM'}"
JOBS0 = [("J-31", "Trailer hitch", "Sample Farm A", 22, DAY0[1]), ("J-32", "Gate hinge", "Sample Ranch B", 14, DAY0[3]), ("J-33", "Stair railing", "Sample Home C", 9, DAY0[5])]
PIN0 = [(140, 250, "Shop"), (720, 90, "1"), (560, 300, "2"), (330, 150, "3")]
def map0():
    W, H = 900, 360
    roads = "".join(f'<path d="{d}" stroke="#fff" stroke-width="14" fill="none" stroke-linecap="round"/>' for d in ["M0 250 L900 250", "M560 0 L560 360", "M140 0 L140 360", "M330 60 L900 60", "M330 60 L330 360"])
    route = "M140 250 L560 250 L560 60 L720 60 L720 90 M720 60 L560 60 L560 300 M560 250 L330 250 L330 150 M330 250 L140 250"
    pins = ""
    for x, y, t in PIN0:
        if t == "Shop":
            pins += f'<rect x="{x - 36}" y="{y - 22}" width="72" height="44" rx="10" fill="{DK0}"/><text x="{x}" y="{y + 7}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="18" fill="#fff"><tspan>Shop</tspan></text>'
        else:
            pins += f'<circle cx="{x}" cy="{y}" r="22" fill="{OR0}" stroke="#fff" stroke-width="4"/><text x="{x}" y="{y + 7}" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="20" fill="#fff"><tspan>{t}</tspan></text>'
    fields = "".join(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{c}"/>' for x, y, w, h, c in [(20, 20, 100, 210, "#d5dccb"), (160, 80, 150, 150, "#cfd9c2"), (350, 80, 190, 150, "#d5dccb"), (580, 80, 300, 150, "#cbd6bf"), (160, 270, 150, 80, "#cfd9c2"), (580, 270, 300, 80, "#d5dccb"), (20, 270, 100, 80, "#cbd6bf")])
    return f'''<svg viewBox="0 0 {W} {H}" width="{W}" style="display:block;width:100%;height:auto"><rect width="{W}" height="{H}" rx="16" fill="#c4cfb6"/>{fields}{roads}<path d="{route}" stroke="{AB0}" stroke-width="5" fill="none" stroke-dasharray="10 8" stroke-linejoin="round"/>{pins}</svg>'''
P["p420_weld_s3"] = t0(3, "2 · DAY ROUTE", "Plan the day by area.<br><span>Less driving, more welding.</span>",
f'''<div class=w03><div class="cd0 mp03"><span class=sm0>WED 25 NOV · SAMPLE AREA</span>{map0()}</div>
<div class="cd0 rb03"><span class=sm0>DAY RIBBON · DRIVE TIME HATCHED</span><div class=rbx>{"".join(f'<div class="bk {t}" style="left:{mn0(a) / SPAN0 * 100:.2f}%;width:{(mn0(b) - mn0(a)) / SPAN0 * 100:.2f}%">{f"<b>{l}</b>" if l else ""}</div>' for t, a, b, l in DAY0)}</div>
<div class=ax>{"".join(f'<span style="left:{(h - 7) * 60 / SPAN0 * 100:.2f}%">{(h - 1) % 12 + 1} {"AM" if h < 12 else "PM"}</span>' for h in [7, 9, 11, 13, 15, 17])}</div></div>
<div class=jb03>{"".join(f'<div class="cd0 jc"><div><b>{j}</b><i>{k} km</i></div><strong>{w}</strong><span>{c}</span><em>{hm0(d[1])} to {hm0(d[2])}</em></div>' for j, w, c, k, d in JOBS0)}</div></div>''',
css=f""".w03{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.mp03{{padding:14px 18px;display:flex;flex-direction:column;gap:8px}}
.rb03{{padding:14px 18px 10px;display:flex;flex-direction:column;gap:10px}}.rbx{{position:relative;height:64px;background:#f1f3f6;border-radius:12px;overflow:hidden}}
.rbx .bk{{position:absolute;top:0;bottom:0;display:flex;align-items:center;justify-content:center}}.rbx .bk.j{{background:{AB0};color:#fff;border-left:2px solid #fff;border-right:2px solid #fff}}.rbx .bk b{{font:800 18px/1.2 Poppins}}
.rbx .bk.d{{background:repeating-linear-gradient(-45deg,#ffd9bd 0 8px,#fff2e8 8px 16px)}}
.ax{{position:relative;height:22px}}.ax span{{position:absolute;top:0;transform:translateX(-50%);font:600 14px/1.4 Roboto;color:#68717c;white-space:nowrap}}.ax span:first-child{{transform:none}}.ax span:last-child{{transform:translateX(-100%)}}
.jb03{{flex:1;display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.jc{{padding:16px 18px;display:flex;flex-direction:column;justify-content:space-between;gap:4px}}.jc>div{{display:flex;justify-content:space-between;align-items:center}}
.jc b{{font:800 22px/1.3 Poppins;color:{AB0}}}.jc i{{font:700 14px/1.2 Roboto;font-style:normal;background:#fff0e5;color:#b4500b;border-radius:8px;padding:6px 9px}}.jc strong{{font:700 28px/1.3 Poppins}}.jc span{{font:500 19px/1.3 Roboto;color:#68717c}}.jc em{{font:700 19px/1.3 Roboto;font-style:normal}}""")

J31 = JOBS0[0][4]
P["p420_weld_s4"] = t0(4, "3 · JOB CARD", "Finish the job on site.<br><span>Photos, parts, sign-off.</span>",
f'''<div class=w04><div class=ph04>{"".join(f'<div class="cd0 pc"><span class=sm0>{t}</span>{photo0(k, 0, f"s4{k}", 420, 296)}</div>' for t, k in [("BEFORE · 8:05 AM", "hitch"), ("AFTER · 9:20 AM", "weld")])}</div>
<div class=rw04><div class="cd0 dt04"><span class=sm0>J-31 · SAMPLE FARM A · TRAILER HITCH</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Work done", "Ground out the crack, welded both sides, added a gusset"), ("Plate", "Steel ¼ in · 4 × 6 in"), ("Wire", "Flux-core · about ½ lb"), ("On site", f"{hm0(J31[1])} to {hm0(J31[2])} · 1 h 30 min")])}</div>
<div class="dk0 sg04"><span class=sm0>CUSTOMER SIGN-OFF</span><svg viewBox="0 0 240 80" width="240" height="80" style="display:block;width:100%;height:auto"><path d="M10 60 C30 20 40 70 60 40 S90 20 100 50 S130 70 150 30 S190 40 230 35" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round"/><line x1="10" y1="72" x2="230" y2="72" stroke="#5a6678" stroke-width="2"/></svg><span class=sn>Signed 9:28 AM</span><div class=bt>Send job card</div></div></div></div>''',
css=f""".w04{{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0}}.ph04{{display:grid;grid-template-columns:1fr 1fr;gap:14px}}.pc{{padding:14px 16px;display:flex;flex-direction:column;gap:8px}}.pc svg{{width:100%!important;height:auto!important}}
.rw04{{flex:1;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.9fr);gap:14px;min-height:0}}.dt04{{padding:16px 20px;display:flex;flex-direction:column}}
.dt04 .r{{flex:1;display:grid;grid-template-columns:110px 1fr;gap:12px;align-items:center;border-top:1px solid #e6e9ed}}.dt04 .r span{{font:600 17px/1.3 Roboto;color:#68717c}}.dt04 .r b{{font:600 22px/1.35 Roboto;text-wrap:pretty}}
.sg04{{padding:16px 20px;display:flex;flex-direction:column;justify-content:space-between;gap:10px}}.sg04 .sn{{font:600 16px/1.3 Roboto;color:#cfd8e4}}.sg04 .bt{{background:{OR0};border-radius:12px;padding:13px;text-align:center;font:800 17px/1.2 Poppins}}""")

P["p420_weld_s5"] = t0(5, "MOBILE WELDING APP", "Weld on the road?<br><span>Let's build your job app.</span>",
f'''<div class=w05><div class=tl05>{"".join(f'<div class=cd0><span class=ib>{ic(i, 40)}</span><b>{a}</b><span>{b}</span></div>' for i, a, b in [("doc", "Request form", "Photos, metal, access"), ("map", "Day route", "Jobs by area"), ("camera", "Job cards", "Before and after"), ("send", "Sign-off", "Signed on site, sent")])}</div>
<div class="dk0 q05"><span class=sm0>A QUESTION FOR WELDERS</span><p>When a weld job comes in by text, what is the first thing you ask? Tell us in the comments.</p></div></div>''',
cta="Want this? DM us", ctacss=f"background:{OR0};color:#fff",
css=f""".w05{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}.tl05{{flex:1;display:grid;grid-template-columns:repeat(2,1fr);gap:16px}}
.tl05>div{{padding:26px;display:flex;flex-direction:column;gap:10px;justify-content:center;border-top:8px solid {AB0}}}.tl05 .ib{{width:84px;height:84px;border-radius:50%;background:{AB0};color:#fff}}.tl05 b{{font:800 42px/1.3 Poppins}}.tl05>div>span:last-child{{font:500 24px/1.4 Roboto;color:#68717c}}
.q05{{padding:26px 30px;display:flex;flex-direction:column;gap:10px}}.q05 p{{font:700 32px/1.4 Poppins;text-wrap:pretty}}""")
