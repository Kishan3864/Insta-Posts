import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 91 INDIA · Plant nursery · SINGLE · Gelasio + Open Sans · olive moss / clay pink / linen
# New technique: inline SVG potted plants on a wooden plank with hanging care tags (string + punched hole).
def pot(inner, c1="#c8714f", c2="#a85a3c"):
    return f'''<svg viewBox="0 0 200 250" width="214" height="268">{inner}
<path d="M40 168 L160 168 L148 246 L52 246 Z" fill="{c1}"/><rect x="32" y="156" width="136" height="22" rx="5" fill="{c2}"/>
<path d="M60 190 L140 190" stroke="#e8a283" stroke-width="5" stroke-linecap="round" opacity=".55"/></svg>'''
snake = "".join(f'<path d="M{x} 160 Q{x-14+d} 90 {x+2+d} {t} Q{x+16+d} 90 {x+12} 160 Z" fill="#2f6b34" stroke="#cfc66a" stroke-width="3"/>' for x,d,t in [(60,-10,40),(78,0,12),(96,4,28),(114,10,6),(130,14,46)])
money = ('<path d="M100 160 C 96 120 70 100 52 70 M100 160 C 108 118 140 98 150 62 M100 160 C 100 120 100 90 98 50" stroke="#4f7a2c" stroke-width="4" fill="none"/>'
  + "".join(f'<ellipse cx="{x}" cy="{y}" rx="19" ry="14" fill="{c}" transform="rotate({r} {x} {y})"/>' for x,y,r,c in [(52,70,-30,"#6fa83c"),(70,100,20,"#8cc04f"),(150,62,30,"#6fa83c"),(128,98,-20,"#8cc04f"),(98,50,0,"#6fa83c"),(100,92,10,"#8cc04f"),(78,134,-25,"#6fa83c"),(124,134,25,"#6fa83c")]))
areca = "".join(f'<path d="M100 160 Q {100+a} {90} {100+b} {t}" stroke="#3d7d3a" stroke-width="5" fill="none" stroke-linecap="round"/>' + "".join(f'<ellipse cx="{100+b*k/4+a*(1-k/4)*.4:.0f}" cy="{160-(160-t)*k/4:.0f}" rx="16" ry="5" fill="#5c9e47" transform="rotate({-30 if b<0 else 30} {100+b*k/4+a*(1-k/4)*.4:.0f} {160-(160-t)*k/4:.0f})"/>' for k in (1,2,3)) for a,b,t in [(-30,-78,40),(-8,-30,10),(10,30,14),(30,80,44)])
jade = ('<path d="M100 160 L100 110 M100 120 L72 86 M100 112 L132 80 M100 130 L130 112" stroke="#7a5a3a" stroke-width="9" stroke-linecap="round" fill="none"/>'
  + "".join(f'<ellipse cx="{x}" cy="{y}" rx="15" ry="11" fill="#5f9c58" stroke="#3f7340" stroke-width="2"/>' for x,y in [(72,80),(58,94),(86,70),(132,74),(146,88),(118,64),(100,100),(138,110),(150,124),(84,108),(100,78)]))
plants = [("Snake plant","Low light is fine","Water every 2 weeks","In stock","ok",snake),
          ("Money plant","Indoor light","Water weekly","In stock","ok",money),
          ("Areca palm","Bright light","Water twice a week","3 left","lw",areca),
          ("Jade plant","Sunny window","Water every 10 days","Sold out","so",jade)]
P["p91_nursery"] = page("""
body{--f:'Open Sans';--h:'Gelasio';background:#f4efe6;color:#26341d}
h1{font-family:'Gelasio';font-size:64px;font-weight:700;letter-spacing:-.6px} h1 span{color:#c0604a}
.sub{color:#5f6857;font-size:23px}
.vis{flex-direction:column;gap:16px}
.sh{flex:1;background:#dfe6cf;border-radius:30px;padding:18px 22px 20px;display:flex;flex-direction:column;position:relative;overflow:hidden}
.sh .lb{font:700 13px 'Open Sans';letter-spacing:3px;color:#5f6e4c;margin-bottom:2px}
.pl{display:flex;justify-content:space-between;align-items:flex-end}
.pl svg{display:block}
.pk{height:26px;border-radius:6px;background:repeating-linear-gradient(90deg,#9a6b42 0 120px,#8d6039 120px 124px);box-shadow:0 8px 14px rgba(60,40,20,.25);flex:none}
.tgs{display:flex;justify-content:space-between;gap:14px;flex:1}
.tw{flex:1;display:flex;flex-direction:column;align-items:center}
.tw i{display:block;width:3px;height:22px;background:#7d6a52}
.tg{width:100%;flex:1;background:#fffdf7;border-radius:16px 16px 18px 18px;padding:26px 12px 12px;display:flex;flex-direction:column;align-items:center;gap:5px;position:relative;box-shadow:0 8px 16px rgba(40,50,30,.12);text-align:center}
.tg u{position:absolute;top:9px;left:50%;margin-left:-7px;width:14px;height:14px;border-radius:50%;background:#dfe6cf;box-shadow:inset 0 0 0 2px #b9a98e}
.tg b{font:700 25px/1.25 'Gelasio'}
.tg span{font:600 17px/1.4 'Open Sans';color:#5f6857}
.tg s{text-decoration:none;font:700 16px 'Open Sans';color:#26341d;background:#f1ece0;border-radius:8px;padding:4px 10px;margin-top:4px}
.tg em{margin-top:auto;font-style:normal;font:700 15px 'Open Sans';padding:5px 11px;border-radius:8px}
.ok{background:#e1efd2;color:#2f6b34}.lw{background:#fbe0d5;color:#a8442c}.so{background:#ebe7de;color:#8b8577}
.rw{display:flex;gap:16px;flex:none}
.cd{background:#fff;border-radius:24px;padding:20px 22px;box-shadow:0 12px 28px rgba(40,50,30,.07);display:flex;flex-direction:column;gap:10px}
.cd small{font:700 13px 'Open Sans';letter-spacing:3px;color:#8b8577}
.dl{flex:1.15}
.dr{display:flex;align-items:center;gap:12px;border-top:1.5px solid #efeae0;padding-top:10px}
.dr b{font:700 20px 'Open Sans';flex:1}.dr span{font:600 17px 'Open Sans';color:#c0604a;white-space:nowrap}
.ft2{flex:1;background:#26341d;color:#f4efe6}
.ft2 small{color:#b9c6a6}
.ch{display:flex;flex-wrap:wrap;gap:8px}
.ch em{font-style:normal;font:600 17px 'Open Sans';padding:7px 13px;border-radius:20px;background:#3a4a2e}
.ch em.on{background:#d9826b;color:#26341d}
.ft2 p{font:500 18px/1.4 'Open Sans';color:#dfe6cf;margin-top:auto}
""", "<h1>Plant orders from<br>40 WhatsApp photos?<br><span>Share one catalogue link.</span></h1><div class=sub>For plant nurseries: every plant with a care tag, and every delivery in one list.</div>",
f'''<div class=sh><span class=lb>YOUR CATALOGUE · SAMPLE</span><div class=pl>{"".join(pot(s) for *_,s in plants)}</div><div class=pk></div>
<div class=tgs>{"".join(f'<div class=tw><i></i><div class=tg><u></u><b>{n}</b><span>{a}<br>{w}</span><s>{z}</s><em class={k}>{st}</em></div></div>' for (n,a,w,st,k,_),z in zip(plants,["Pot size 8 inch","Pot size 6 inch","Height 3 ft","Pot size 6 inch"]))}</div></div>
<div class=rw><div class="cd dl"><small>TODAY'S DELIVERIES · SAMPLE</small>{"".join(f'<div class=dr><b>{a}</b><span>{b}</span></div>' for a,b in [("Order 1 · 3 plants + pots","10 am"),("Order 2 · Areca palm x 2 · office","1 pm"),("Order 3 · Jade plant · flat 4B","5 pm")])}</div>
<div class="cd ft2"><small>BUYERS FILTER THE LIST</small><div class=ch>{"".join(f'<em class="{"on" if i==0 else ""}">{t}</em>' for i,t in enumerate(["Low light","Balcony","Office desk","Big plants","Hanging"]))}</div><p>They find the right plant without asking you 10 questions.</p></div></div>''',
"#26341d", "Run a plant nursery? DM us", "background:#3f5a2e;color:#fff")

# ───────── 93 USA · Nail salon · SINGLE · Crimson Text + Inter · lilac / cherry / porcelain
# New technique: SVG polish bottle rack used as a shade picker, linked to the booking phone.
shades = [("#b3123a","Cherry"),("#e86f8c","Rose"),("#f2c4c9","Blush"),("#7b4bb0","Plum"),("#2f3a8f","Navy"),("#e9dcc9","Nude")]
def bottle(c, sel=False):
    return f'''<svg viewBox="0 0 80 150" width="96" height="180"><rect x="28" y="4" width="24" height="54" rx="5" fill="#2b2230"/><rect x="24" y="52" width="32" height="10" rx="3" fill="#43384a"/>
<path d="M14 66 Q14 60 22 60 L58 60 Q66 60 66 66 L66 136 Q66 146 56 146 L24 146 Q14 146 14 136 Z" fill="{c}" stroke="{'#b3123a' if sel else 'rgba(0,0,0,.12)'}" stroke-width="{5 if sel else 2}"/>
<rect x="22" y="72" width="8" height="52" rx="4" fill="#fff" opacity=".35"/></svg>'''
slots = [("10:00",""),("11:30","tk"),("1:00",""),("2:30","on"),("4:00",""),("5:30","tk")]
P["p93_nails"] = page("""
body{--f:'Inter';--h:'Crimson Text';background:#fbf8f6;color:#2b2230}
h1{font-family:'Crimson Text';font-size:70px;font-weight:700;letter-spacing:-.5px} h1 span{color:#b3123a}
.sub{color:#6d6272}
.vis{gap:26px;align-items:stretch}
.lc{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.rk{flex:none;height:330px;background:#e9e0f3;border-radius:30px;padding:22px 20px 18px;display:flex;flex-direction:column;gap:6px}
.rk small,.cd small{font:700 13px Inter;letter-spacing:3px;color:#7d6f8c}
.rk .row{display:flex;justify-content:space-around;align-items:flex-end;flex:1}
.rk .bd{height:16px;border-radius:5px;background:#c9b6e4;flex:none}
.rk .nm{display:flex;justify-content:space-around}.rk .nm span{width:96px;text-align:center;font:600 16px Inter;color:#5d4f6b}
.rk .nm span.on{color:#b3123a;font-weight:800}
.cd{background:#fff;border-radius:24px;padding:20px 22px;box-shadow:0 12px 28px rgba(43,34,48,.08);display:flex;flex-direction:column;gap:10px;flex:1}
.sm{flex:1;display:flex;flex-direction:column;justify-content:center;background:#f4eff8;border-radius:16px 16px 16px 4px;padding:16px 18px;font:500 24px/1.4 Inter}
.sm em{font-style:normal;display:block;font:600 15px Inter;color:#7d6f8c;margin-top:6px}
.stp{display:flex;gap:10px}
.stp{flex:1;align-items:center;justify-content:space-between}.stp i{flex:none;width:66px;height:66px;border-radius:50%;border:3px dashed #c9b6e4;display:flex;align-items:center;justify-content:center;font:700 18px Inter;font-style:normal;color:#c9b6e4;aspect-ratio:1}
.stp i.f{background:#b3123a;border:3px solid #b3123a;color:#fff}
.cd p{font:600 19px Inter;color:#6d6272}
.ap{flex:1;padding:14px 20px 16px;display:flex;flex-direction:column;gap:10px;background:#fff}
.ap h3{font:700 30px 'Crimson Text'}
.ap .lb{font:700 12px Inter;letter-spacing:2.5px;color:#9a8fa5}
.ap .chs{display:flex;gap:6px;flex-wrap:wrap}
.ap .chs em{font-style:normal;font:600 16px Inter;padding:8px 12px;border-radius:16px;background:#f2edf6;color:#5d4f6b}
.ap .chs em.on{background:#2b2230;color:#fff}
.dots{display:flex;gap:8px}.dots i{width:36px;height:36px;border-radius:50%;display:block}
.dots i.on{box-shadow:0 0 0 3px #fff,0 0 0 6px #b3123a}
.sl{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.sl span{font:700 18px Inter;text-align:center;padding:12px 0;border-radius:12px;border:2px solid #e6deef}
.sl .tk{color:#c4bccb;text-decoration:line-through;background:#f6f3f8}
.sl .on{background:#b3123a;border-color:#b3123a;color:#fff}
.nte{border:2px solid #e6deef;border-radius:12px;padding:11px 14px;font:500 17px Inter;color:#6d6272}
.sum{margin-top:auto;background:#f6f1f9;border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:3px}.sum b{font:700 18px Inter}.sum span{font:500 16px Inter;color:#6d6272}
.bt{;background:#2b2230;color:#fff;border-radius:16px;text-align:center;font:700 19px Inter;padding:14px}
""", "<h1>Bookings lost in DMs?<br><span>Let clients pick a time<br>and a shade.</span></h1><div class=sub>For nail salons: online booking, a reminder text and a stamp card.</div>",
f'''<div class=lc><div class=rk><small>CLIENT PICKS A SHADE · SAMPLE</small><div class=row>{"".join(bottle(c, i==0) for i,(c,_) in enumerate(shades[:5]))}</div><div class=bd></div>
<div class=nm>{"".join(f'<span class="{"on" if i==0 else ""}">{n}</span>' for i,(_,n) in enumerate(shades[:5]))}</div></div>
<div class=cd><small>REMINDER TEXT · DAY BEFORE</small><div class=sm>See you tomorrow at 2:30 pm for a gel manicure. Reply C to change.<em>Sent automatically</em></div></div>
<div class=cd><small>STAMP CARD · REWARD YOU CHOOSE</small><div class=stp>{"".join(f'<i class="{"f" if k<4 else ""}">{k+1}</i>' for k in range(6))}</div><p>4 of 6 visits · sample client</p></div></div>
{phone(f"""<div class=ap><span class=lb>YOUR SALON · SAMPLE</span><h3>Book a visit</h3>
<span class=lb>SERVICE</span><div class=chs><em class=on>Gel manicure</em><em>Pedicure</em><em>Nail art</em></div>
<span class=lb>SHADE</span><div class=dots>{"".join(f'<i class="{"on" if i==0 else ""}" style="background:{c}"></i>' for i,(c,_) in enumerate(shades))}</div>
<span class=lb>TECH</span><div class=chs><em>Any</em><em class=on>Tech 1</em><em>Tech 2</em></div>
<span class=lb>TUESDAY</span><div class=sl>{"".join(f'<span class="{k}">{t}</span>' for t,k in slots)}</div>
<span class=lb>NOTE (OPTIONAL)</span><div class=nte>Short nails, almond shape</div><div class=sum><b>Tue · 2:30 pm · Tech 1</b><span>Gel manicure · shade Cherry</span></div><div class=bt>Confirm 2:30 pm</div></div>""", w=380, h=760)}''',
"#2b2230", "Own a nail salon? DM us", "background:#b3123a;color:#fff")

# ───────── 94 INDIA · Badminton / box cricket court · SINGLE · Archivo Black + DM Sans · emerald court / white lines / neon lime
# New technique: top-down SVG court diagrams with live status, over a slot grid in a browser.
def court(st):
    return f'''<svg viewBox="0 0 220 120" width="250" height="136"><rect x="0" y="0" width="220" height="120" rx="10" fill="{'#0f6b4f' if st!='bk' else '#164036'}"/>
<g stroke="#fff" stroke-width="2.5" fill="none" opacity="{1 if st!='bk' else .45}"><rect x="12" y="10" width="196" height="100"/><line x1="110" y1="10" x2="110" y2="110" stroke-width="4"/>
<line x1="12" y1="20" x2="208" y2="20"/><line x1="12" y1="100" x2="208" y2="100"/><line x1="78" y1="10" x2="78" y2="110"/><line x1="142" y1="10" x2="142" y2="110"/>
<line x1="24" y1="10" x2="24" y2="110"/><line x1="196" y1="10" x2="196" y2="110"/><line x1="12" y1="60" x2="78" y2="60"/><line x1="142" y1="60" x2="208" y2="60"/></g></svg>'''
cts = [("Court 1","Playing till 7 pm","pl"),("Court 2","Free now","fr"),("Court 3","Booked","bk")]
grid = [("6 pm",["b","b","b"]),("7 pm",["f","b","b"]),("8 pm",["f","f","b"]),("9 pm",["b","f","f"]),("10 pm",["f","f","b"])]
P["p94_court"] = page("""
body{--f:'DM Sans';--h:'Archivo Black';background:#0b2a22;color:#eef6ee}
h1{font-family:'Archivo Black';font-weight:400;font-size:62px;letter-spacing:-1px;line-height:1.22} h1 span{color:#d7f542}
.sub{color:#a9c4b6}
.vis{flex-direction:column;gap:18px}
.cs{display:flex;gap:16px;flex:none}
.ct{flex:1;background:#123a2f;border-radius:22px;padding:14px;display:flex;flex-direction:column;align-items:center;gap:10px}
.ct svg{display:block}
.ct div{display:flex;justify-content:space-between;align-items:center;width:100%;padding:0 4px}
.ct b{font:700 22px 'DM Sans'}
.ct em{font-style:normal;font:700 16px 'DM Sans';padding:5px 10px;border-radius:8px}
.pl{background:#24584a;color:#d4efe2}.fr{background:#d7f542;color:#0b2a22}.bk{background:#3a2a2a;color:#ffb3a3}
.gw{flex:1;display:flex;flex-direction:column;padding:16px 22px 18px;gap:10px;background:#fff;color:#0b2a22}
.gh{display:flex;justify-content:space-between;align-items:center}
.gh b{font:400 28px 'Archivo Black'}.gh small{font:700 13px 'DM Sans';letter-spacing:3px;color:#6f8a7e}
.gr{flex:1;display:grid;grid-template-columns:110px 1fr 1fr 1fr;grid-auto-rows:1fr;gap:8px}
.gr .h{font:700 17px 'DM Sans';color:#6f8a7e;display:flex;align-items:center;justify-content:center}
.gr .t{font:700 22px 'DM Sans';display:flex;align-items:center}
.gr .b{background:#e8eeea;color:#9bb0a6;border-radius:12px;display:flex;align-items:center;justify-content:center;font:600 18px 'DM Sans'}
.gr .f{background:#0f6b4f;color:#fff;border-radius:12px;display:flex;align-items:center;justify-content:center;gap:8px;font:700 19px 'DM Sans'}
.gr .f u{text-decoration:none;background:#d7f542;color:#0b2a22;padding:4px 10px;border-radius:8px;font:700 15px 'DM Sans'}
.nt{display:flex;align-items:center;gap:10px;font:600 18px 'DM Sans';color:#3d5a4e;background:#f0f7d2;border-radius:12px;padding:11px 14px}
""", "<h1>“Is a court free at 8?”<br><span>Show live slots on a<br>booking page.</span></h1><div class=sub>For badminton and box cricket courts: players see free slots, book and pay the advance online.</div>",
f'''<div class=cs>{"".join(f'<div class=ct>{court(k)}<div><b>{n}</b><em class={k}>{s}</em></div></div>' for n,s,k in cts)}</div>
{browser(f"""<div class=gw><div class=gh><b>Tonight · Tuesday</b><small>SAMPLE SLOTS</small></div>
<div class=gr><span></span>{"".join(f'<span class=h>Court {i}</span>' for i in (1,2,3))}{"".join(f'<span class=t>{t}</span>' + "".join('<span class=b>Booked</span>' if c=="b" else '<span class=f>Free <u>Book</u></span>' for c in cs) for t,cs in grid)}</div>
<div class=nt>{ic("check",22)}Booked slots close on their own. No double booking.</div></div>""", "book.yourcourt.in · sample", "flex:1")}''',
"#eef6ee", "Run a court? DM us", "background:#d7f542;color:#0b2a22")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
