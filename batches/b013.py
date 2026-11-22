import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 81 INDIA · Steel railing fabricator · SINGLE · Lora + Fira Sans · brushed steel / ink / electric teal
# New technique: inline SVG technical elevation drawing (stair railing with dimension lines) on a drafting card.
svg = '''<svg viewBox="0 0 560 400" width="600" height="429" style="display:block">
<g stroke="#16202a" stroke-width="4" fill="none">
<path d="M40 360 H120 V320 H200 V280 H280 V240 H360 V200 H440 V160 H520" stroke="#8a96a3" stroke-width="5"/>
<path d="M80 250 L480 90" stroke-width="9" stroke="#00a3a1"/>
<path d="M80 250 V340 M480 90 V180"/>
''' + "".join(f'<path d="M{x} {250-(x-80)*0.4:.0f} V{340-(x-80)*0.4:.0f}" stroke-width="3"/>' for x in range(120, 480, 40)) + '''
</g>
<g stroke="#e0533a" stroke-width="2" fill="#e0533a">
<path d="M70 40 L490 40" fill="none"/><path d="M70 32 V48 M490 32 V48" fill="none"/>
<path d="M530 90 V180" fill="none"/><path d="M522 90 H538 M522 180 H538" fill="none"/>
</g>
<g font-family="Fira Sans" font-weight="700" font-size="22" fill="#e0533a">
<rect x="225" y="26" width="110" height="30" fill="#f4f6f8"/><text x="280" y="48" text-anchor="middle">18 ft run</text>
<rect x="480" y="120" width="80" height="30" fill="#f4f6f8"/><text x="520" y="142" text-anchor="middle">3 ft</text>
</g>
<g font-family="Fira Sans" font-weight="600" font-size="18" fill="#5c6b78">
<text x="96" y="392">Staircase · ground to first floor</text></g>
</svg>'''
steps = [("Measured",1),("Quote sent",1),("Approved",1),("Fabrication",2),("Installed",0)]
P["p81_railing"] = page("""
body{--f:'Fira Sans';--h:'Lora';background:#dfe4e8;color:#16202a}
h1{font-family:'Lora';font-size:62px;font-weight:700;letter-spacing:-.5px} h1 span{color:#00807e}
.sub{color:#56636f}
.vis{flex-direction:column;gap:16px}
.dw{flex:1;background:#f4f6f8;border-radius:26px;padding:20px 24px;display:flex;gap:20px;align-items:center;background-image:linear-gradient(#e4e9ee 1px,transparent 1px),linear-gradient(90deg,#e4e9ee 1px,transparent 1px);background-size:24px 24px;box-shadow:0 18px 40px rgba(22,32,42,.08)}
.dl{display:flex;flex-direction:column;gap:12px;flex:1;min-width:0}
.dl small{font:700 13px 'Fira Sans';letter-spacing:3px;color:#7d8a96}
.sp{background:#fff;border:2px solid #d4dbe1;border-radius:14px;padding:12px 14px}
.sp span{display:block;font:600 15px 'Fira Sans';color:#7d8a96;letter-spacing:1px}
.sp b{font:700 22px 'Fira Sans'}
.stp{display:flex;gap:8px;flex:none}
.stp div{flex:1;border-radius:16px;padding:16px 10px;text-align:center;font:700 19px 'Fira Sans';background:#fff;color:#8a96a3;display:flex;flex-direction:column;align-items:center;gap:8px}
.stp div i{width:30px;height:30px;border-radius:50%;border:3px solid #c3ccd4;display:block;font:800 17px/24px 'Fira Sans';font-style:normal;color:#fff}
.stp .dn{color:#16202a}.stp .dn i{background:#00a3a1;border-color:#00a3a1}
.stp .nw{background:#16202a;color:#fff}.stp .nw i{border-color:#00a3a1;background:#16202a;box-shadow:inset 0 0 0 5px #00a3a1}
.nt{display:flex;gap:14px;flex:none}
.nt div{flex:1;background:#16202a;color:#e6ebef;border-radius:18px;padding:16px 18px;font:500 19px/1.4 'Fira Sans'}
.nt div b{color:#3fd0cd;font-weight:700}
""", "<h1>Site size on a scrap of paper?<br><span>Save it with the job.</span></h1><div class=sub>For steel railing fabricators: measurements, drawing, quote and job status in one place.</div>",
f'''<div class=dw>{svg}<div class=dl><small>JOB R-31 · SAMPLE</small>
<div class=sp><span>MATERIAL</span><b>SS 304, 2 in pipe</b></div><div class=sp><span>BALUSTERS</span><b>Every 4 in</b></div><div class=sp><span>FINISH</span><b>Matt</b></div><div class=sp><span>SITE PHOTOS</span><b>4 added</b></div></div></div>
<div class=stp>{"".join(f'<div class="{"dn" if v==1 else "nw" if v==2 else ""}"><i>{"✓" if v==1 else ""}</i>{t}</div>' for t,v in steps)}</div>
<div class=nt><div><b>Customer asks “when?”</b> Send the job link. They see the stage.</div><div><b>Back to the same site?</b> Old sizes and photos are already there.</div></div>''',
"#16202a", "Steel railing fabricator? DM us", "background:#00a3a1;color:#fff")

# ───────── 83 INDIA · Photo studio · SINGLE · Archivo Black + Roboto · darkroom red / black / paper white  (phone post)
# New technique: film strip with sprocket holes holding passport-style frames (generic CSS silhouettes).
def frame(bg):
    return f'<div class=fr style="background:{bg}"><i class=hd></i><i class=sh></i></div>'
P["p83_photostudio"] = page("""
body{--f:'Roboto';--h:'Archivo Black';background:#141414;color:#f5f1ea}
h1{font-family:'Archivo Black';font-weight:400;font-size:58px;letter-spacing:-1px;line-height:1.25;margin-top:30px} h1 span{color:#ff5a4e}
.sub{color:#b9b3aa}
.vis{gap:22px}
.lf{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.fs{flex:1;background:#2a2725;border-radius:10px;padding:34px 22px;position:relative;display:flex;gap:14px;align-items:center;overflow:hidden}
.fs:before,.fs:after{content:"";position:absolute;left:10px;right:10px;height:16px;background:repeating-linear-gradient(90deg,#141414 0 18px,transparent 18px 34px);border-radius:3px}
.fs:before{top:9px}.fs:after{bottom:9px}
.fr{flex:1;height:100%;border-radius:4px;position:relative;overflow:hidden}
.fr .hd{position:absolute;left:15%;top:27%;width:70%;aspect-ratio:.82;border-radius:50% 50% 46% 46%;background:#3b3633;display:block}
.fr .sh{position:absolute;left:0;right:0;bottom:0;height:44%;border-radius:50% 50% 0 0;background:#3b3633;display:block}
.od{background:#f5f1ea;color:#141414;border-radius:24px;padding:18px 20px;display:flex;flex-direction:column;gap:8px}
.od small{font:700 13px Roboto;letter-spacing:3px;color:#8a837a}
.od .rw{display:flex;justify-content:space-between;font:500 20px Roboto}.od .rw b{font:700 20px Roboto}
.ap{flex:1;padding:6px 18px 18px;display:flex;flex-direction:column;gap:10px;background:#fbf8f4;color:#141414}
.ap .bb{background:#fff;border-radius:16px 16px 16px 4px;padding:12px 14px;font:500 16px/1.45 Roboto;box-shadow:0 4px 12px rgba(0,0,0,.06)}
.ap .bb b{font-weight:700}
.ap .fl{display:flex;align-items:center;gap:10px;background:#fff;border-radius:14px;padding:10px;box-shadow:0 4px 12px rgba(0,0,0,.06)}
.ap .fl i{width:44px;height:54px;border-radius:6px;background:#dfe9f3;display:block;position:relative;overflow:hidden;flex:none}
.ap .fl i:after{content:"";position:absolute;left:12px;top:10px;width:20px;height:22px;border-radius:50%;background:#7a8796}
.ap .fl span{font:700 15px Roboto}.ap .fl small{display:block;font:500 13px Roboto;color:#8a837a}
.ap .st{align-self:flex-start;font:700 13px Roboto;background:#dff1e2;color:#22693a;padding:5px 10px;border-radius:8px}
.ap .bt{margin-top:auto;background:#ff5a4e;color:#fff;border-radius:12px;padding:12px;text-align:center;font:700 16px Roboto}
.ap h5{font:400 20px 'Archivo Black';margin-top:4px}
""", "<h1>Customers waiting at the counter?<br><span>Send a “ready” message.</span></h1><div class=sub>For photo studios: passport photo orders with a ready message and a digital copy.</div>",
f'''<div class=lf><div class=fs>{frame("#dfe9f3")}{frame("#f5f1ea")}{frame("#e9f3e4")}</div>
<div class=od><small>ORDER P-0412 · SAMPLE</small><div class=rw><span>Passport size</span><b>8 prints</b></div><div class=rw><span>Stamp size</span><b>4 prints</b></div><div class=rw><span>Digital copy</span><b>Yes</b></div><div class=rw><span>Ready at</span><b>5:30 pm</b></div></div></div>
<div style="display:flex;align-items:center">{phone("""<div class=ap><h5>Your Studio</h5><div class=bb>Hi! Your photos for order <b>P-0412</b> are ready. Collect them any time before 9 pm.</div><div class=fl><i></i><div><span>photo_P-0412.jpg</span><small>Digital copy · sample</small></div></div><span class=st>Ready for pickup</span><div class=bb><b>Order summary</b><br>8 passport size, 4 stamp size and 1 digital copy.</div><div class=bb>You can use the digital copy for online forms.</div><div class=bt>Get directions</div></div>""", 340, 690)}</div>''',
"#f5f1ea", "Run a photo studio? DM us", "background:#ff5a4e;color:#fff")

# ───────── 84 USA · Realtor · SINGLE · Lora + Open Sans · sage / charcoal / terracotta
# New technique: CSS house facade (roof triangle, windows, door, porch) + tablet sign-in form.
P["p84_realtor"] = page("""
body{--f:'Open Sans';--h:'Lora';background:#e8ede4;color:#26302b}
h1{font-family:'Lora';font-size:64px;font-weight:700;letter-spacing:-.5px} h1 span{color:#c0603e;font-style:italic}
.sub{color:#5a675f}
.vis{gap:20px}
.hs{width:380px;flex:none;background:#c9d6c0;border-radius:30px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding:30px 24px 0;position:relative;overflow:hidden}
.sg{position:absolute;left:24px;top:26px;background:#fff;border-radius:14px;padding:12px 16px;font:700 20px Lora;box-shadow:0 10px 24px rgba(0,0,0,.08)}
.sg small{display:block;font:700 13px 'Open Sans';letter-spacing:3px;color:#c0603e}
.rf{width:0;height:0;border-left:170px solid transparent;border-right:170px solid transparent;border-bottom:120px solid #3f4a44}
.hb{width:300px;height:250px;background:#f3eee4;position:relative}
.wn{position:absolute;width:74px;height:74px;background:#9cc3d8;border:6px solid #fff;box-shadow:0 0 0 2px #d9d2c4}
.dr{position:absolute;left:113px;bottom:0;width:74px;height:130px;background:#c0603e;border-radius:4px 4px 0 0}
.dr:after{content:"";position:absolute;right:12px;top:66px;width:9px;height:9px;border-radius:50%;background:#f3d27a}
.gr{width:100%;height:46px;background:#8fae7e;margin:0 -24px;flex:none}
.rc{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.tb{flex:1;background:#26302b;border-radius:30px;padding:16px}
.sc{background:#fff;border-radius:18px;height:100%;padding:22px;display:flex;flex-direction:column;gap:12px;justify-content:space-between}
.sc h4{font:700 28px Lora}.sc small{font:700 13px 'Open Sans';letter-spacing:3px;color:#8a958e}
.fi{border:2px solid #dde3da;border-radius:12px;padding:10px 14px}
.fi span{display:block;font:700 13px 'Open Sans';letter-spacing:2px;color:#8a958e}.fi b{font:600 22px 'Open Sans'}
.ch{display:flex;gap:8px;flex-wrap:wrap}.ch span{font:600 19px 'Open Sans';padding:9px 14px;border-radius:10px;background:#eef2eb}.ch span.on{background:#26302b;color:#fff}
.sb{background:#c0603e;color:#fff;border-radius:12px;padding:14px;text-align:center;font:700 19px 'Open Sans'}
.ld{background:#fff;border-radius:22px;padding:16px 20px;display:flex;align-items:center;gap:14px;font:500 19px/1.4 'Open Sans'}
.lic{width:46px;height:46px;border-radius:50%;background:#c0603e;color:#fff;font:700 24px/46px 'Open Sans';font-style:normal;text-align:center;flex:none}
""", "<h1>Open house sign-in on paper?<br><span>Use a tablet at the door.</span></h1><div class=sub>For realtors: visitors sign in, pick what they want, and land in your lead list.</div>",
f'''<div class=hs><div class=sg><small>OPEN HOUSE</small>Sat · 1 to 4 pm</div><div class=rf></div><div class=hb><i class=wn style="left:24px;top:30px"></i><i class=wn style="right:24px;top:30px"></i><i class=dr></i></div><div class=gr></div></div>
<div class=rc><div class=tb><div class=sc><small>SIGN IN · SAMPLE</small><h4>Welcome! Please sign in.</h4>
<div class=fi><span>NAME</span><b>Sample Visitor</b></div><div class=fi><span>PHONE OR EMAIL</span><b>name@email.com</b></div>
<small>I AM</small><div class=ch><span class=on>Buying soon</span><span>Just looking</span><span>Selling too</span></div>
<small>WORKING WITH AN AGENT?</small><div class=ch><span>Yes</span><span class=on>No</span></div><div class=fi><span>QUESTION FOR THE AGENT</span><b>Is the basement finished?</b></div>
<div class=sb>Sign in and get the listing</div></div></div>
<div class=ld><i class=lic>✓</i>Every visitor lands in your lead list, with what they want.</div></div>''',
"#26302b", "Realtor or broker? DM us", "background:#26302b;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
