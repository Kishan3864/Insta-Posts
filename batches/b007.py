import sys; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 51 INDIA · Co-working space · SINGLE · Fira Sans + Inter Display · concrete grey / electric green / black
# New technique: isometric desk floor (rotateX + rotateZ) with a flat legend and booking card.
desks = "fftbfbtffbbfftfb"  # f free, b booked, t taken by you
P["p51_coworking"] = page("""
body{--f:'Inter';--h:'Fira Sans';background:#e4e4df;color:#121212}
h1{font-family:'Fira Sans';font-size:66px;font-weight:800;letter-spacing:-1.5px} h1 span{background:#c6f432;padding:0 10px;border-radius:10px;box-decoration-break:clone;-webkit-box-decoration-break:clone}
.sub{color:#55554f}
.vis{gap:22px;align-items:stretch}
.flr{flex:1.25;background:#121212;border-radius:30px;position:relative;overflow:hidden;display:flex;align-items:center;justify-content:center}
.iso{width:330px;height:330px;transform:rotateX(55deg) rotateZ(-45deg);display:grid;grid-template-columns:repeat(4,1fr);gap:18px;padding:24px;background:#2a2a28;border-radius:18px;box-shadow:-18px 18px 0 #050505}
.iso i{border-radius:12px;background:#4a4a46;box-shadow:-8px 8px 0 #1c1c1a;display:block}
.iso i.f{background:#c6f432;box-shadow:-8px 8px 0 #7d9c1c}.iso i.t{background:#ffffff;box-shadow:-8px 8px 0 #9a9a94}
.fl{position:absolute;left:24px;top:22px;font:800 15px Inter;letter-spacing:3px;color:#c6f432}
.lgd{position:absolute;left:24px;right:24px;bottom:22px;display:flex;gap:18px;font:600 17px Inter;color:#e4e4df}
.lgd span{display:flex;align-items:center;gap:8px}.lgd i{width:18px;height:18px;border-radius:5px;display:block}
.rc{flex:1;display:flex;flex-direction:column;gap:16px;min-width:0}
.bk{flex:1;background:#fff;border-radius:26px;padding:24px;display:flex;flex-direction:column;gap:12px}
.bk small{font:800 14px Inter;letter-spacing:3px;color:#7a7a72}.bk b{font:800 30px/1.2 'Fira Sans'}
.op{flex:1;display:flex;align-items:center;justify-content:space-between;background:#f2f2ee;border-radius:14px;padding:0 16px;font:700 23px Inter}
.op em{font-style:normal;font:700 16px Inter;padding:5px 10px;border-radius:9px;background:#c6f432}
.go{background:#121212;color:#c6f432;border-radius:14px;padding:16px;text-align:center;font:800 20px Inter}
.mb{background:#c6f432;border-radius:22px;padding:20px 22px;display:flex;flex-direction:column;gap:6px}
.mb b{font:800 24px/1.3 'Fira Sans'}.mb span{font:500 18px/1.4 Inter}
""", "<h1>Is a desk free today?<br><span>Members check first.</span></h1><div class=sub>For co-working spaces: desk booking, monthly plans and visitor passes in one app.</div>",
f'''<div class=flr><div class=fl>FLOOR 2 · SAMPLE</div><div class=iso>{"".join(f'<i class={c}></i>' for c in desks)}</div>
<div class=lgd><span><i style="background:#c6f432"></i>Free</span><span><i style="background:#4a4a46;outline:1px solid #777"></i>Booked</span><span><i style="background:#fff"></i>Your desk</span></div></div>
<div class=rc><div class=bk><small>BOOK A DESK · SAMPLE</small><b>Tuesday, full day</b>{"".join(f'<div class=op>{a}<em>{b}</em></div>' for a,b in [("Window desk 2B","Free"),("Quiet zone 3A","Free"),("Phone booth","2 to 3 pm"),("Meeting room, 4 seats","4 to 5 pm")])}<div class=go>Book desk</div></div>
<div class=mb><b>Visitor pass sent.</b><span>Your guest gets a pass on their phone for the front desk.</span></div></div>''',
"#121212", "Run a co-working space? DM us", "background:#121212;color:#c6f432")

# ───────── 52 INDIA · Computer training institute · CAROUSEL 6 · Poppins + Bitter · royal blue / tangerine / white
# New format: process journey carousel with a running progress rail (step dots across the top of each slide).
CT = """
body{--f:'Poppins';--h:'Bitter';background:#f5f7ff;color:#14215c}
h1{font-family:'Bitter';font-size:62px;font-weight:800;letter-spacing:-1px} h1 span{color:#ff7a1a}
.sub{color:#59628f}
.rail{display:flex;align-items:center;margin-top:22px}
.rail i{width:40px;height:40px;border-radius:50%;background:#dfe4fb;color:#7b86bd;font:700 17px/40px Poppins;font-style:normal;text-align:center;flex:none}
.rail i.on{background:#2342d6;color:#fff}.rail i.dn{background:#ff7a1a;color:#fff}
.rail b{flex:1;height:5px;background:#dfe4fb;margin:0 6px}.rail b.dn{background:#ff7a1a}
.card{background:#fff;border-radius:26px;box-shadow:0 18px 40px rgba(20,33,92,.08)}
"""
def rail(k):
    out = ""
    for i in range(1, 5):
        c = "dn" if i < k else ("on" if i == k else "")
        out += f'<i class="{c}">{i}</i>' + (f'<b class="{"dn" if i < k else ""}"></b>' if i < 4 else "")
    return f'<div class=rail>{out}</div>'
def ct(n, head, vis, css, cta="Swipe", ctacss="background:#2342d6;color:#fff"):
    return page(CT + css, head, vis, "#14215c", cta, ctacss, tagline=f"{n} / 6")

P["p52_institute_s1"] = ct(1, """<div style="font:700 17px Poppins;letter-spacing:4px;color:#ff7a1a;margin-top:22px">FOR COMPUTER INSTITUTES</div><h1 style="margin-top:10px">From first enquiry<br>to certificate,<br><span>in one app.</span></h1>""",
f'''<div class=path>{"".join(f'<div class=st style="margin-left:{m}px"><span>{k}</span><div><b>{a}</b><small>{b}</small></div></div>' for k,m,a,b in [(1,0,"Enquiry","Form on your website"),(2,90,"Batch","Seat in the right batch"),(3,180,"Attendance + fees","One screen for both"),(4,270,"Certificate","Made from the records")])}</div>''',
""".vis{flex-direction:column}
.path{flex:1;display:flex;flex-direction:column;gap:18px;position:relative;background:linear-gradient(#ffd9bd,#ffd9bd) 40px 30px/6px calc(100% - 60px) no-repeat}
.st{flex:1;display:flex;align-items:center;gap:22px;background:#fff;border-radius:24px;padding:0 28px;box-shadow:0 18px 40px rgba(20,33,92,.08);max-width:640px}
.st span{width:64px;height:64px;border-radius:50%;background:#2342d6;color:#fff;font:800 30px/64px 'Bitter';text-align:center;flex:none}
.st b{display:block;font:800 38px/1.25 'Bitter'}.st small{font:500 23px Poppins;color:#59628f}
""")

P["p52_institute_s2"] = ct(2, rail(1) + """<h1>Step 1: Enquiries land<br><span>in one list.</span></h1><div class=sub>Website form, walk-in or phone call. Nothing lost in a notebook.</div>""",
f'''<div class="card lst"><h5>New enquiries <span>SAMPLE</span></h5>{"".join(f'<div class=er><div><b>{a}</b><small>{b}</small></div><i class={c}>{d}</i></div>' for a,b,c,d in [("Ankit P.","Tally + GST course · website","n","Call today"),("Sneha R.","Web design · walk-in","v","Visit Sat"),("Imran K.","Basic computer · phone","j","Joined"),("Pooja M.","Python · website","n","Call today"),("Ravi T.","Advanced Excel · walk-in","v","Demo class")])}</div>''',
""".vis{flex-direction:column}
.lst{flex:1;padding:24px 26px;display:flex;flex-direction:column;gap:10px}
.lst h5{font:800 24px 'Bitter';display:flex;justify-content:space-between}.lst h5 span{font:700 13px Poppins;letter-spacing:3px;color:#9aa2c8}
.er{flex:1;display:flex;align-items:center;justify-content:space-between;background:#f5f7ff;border-radius:16px;padding:0 20px}
.er b{display:block;font:700 23px Poppins}.er small{font:500 18px Poppins;color:#59628f}
.er i{font-style:normal;font:700 16px Poppins;padding:8px 14px;border-radius:12px}.n{background:#ffe7d6;color:#c2560c}.v{background:#e4e8ff;color:#2342d6}.j{background:#dff5e7;color:#1f8a4c}
""")

seats = [("Tally + GST", "Mon to Fri · 9 am", 18, 20), ("Web design", "Mon to Fri · 11 am", 12, 15), ("Python", "Sat and Sun · 10 am", 9, 15), ("Advanced Excel", "Mon to Fri · 5 pm", 20, 20)]
P["p52_institute_s3"] = ct(3, rail(2) + """<h1>Step 2: Put every student<br><span>in the right batch.</span></h1><div class=sub>See seats left before you promise a timing.</div>""",
f'''<div class=bgrid>{"".join(f'<div class="card bt"><b>{a}</b><small>{t}</small><div class=bar><i style="width:{u/m*100:.0f}%"></i></div><p><span>{u} of {m} seats</span><em class="{"full" if u==m else ""}">{"Full" if u==m else f"{m-u} left"}</em></p></div>' for a,t,u,m in seats)}</div>''',
""".vis{flex-direction:column}
.bgrid{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:18px}
.bt{padding:26px;display:flex;flex-direction:column;justify-content:center;gap:12px}
.bt b{font:800 38px 'Bitter'}.bt small{font:500 22px Poppins;color:#59628f}
.bar{height:24px;border-radius:8px;background:#e7eafa;overflow:hidden}.bar i{display:block;height:100%;background:#2342d6;border-radius:8px}
.bt p{display:flex;justify-content:space-between;align-items:center;font:600 22px Poppins}
.bt em{font-style:normal;font:700 18px Poppins;padding:6px 12px;border-radius:10px;background:#ffe7d6;color:#c2560c}.bt em.full{background:#14215c;color:#fff}
""")

days = "PPPAPPPPAPPPPPP"
P["p52_institute_s4"] = ct(4, rail(3) + """<h1>Step 3: Attendance and fees<br><span>on one screen.</span></h1><div class=sub>Mark attendance in a tap. Fee dates show up on their own.</div>""",
f'''<div class="card stu"><div class=sh><span class=av>S</span><div><b>Sample student</b><small>Web design · Mon to Fri · 11 am</small></div></div>
<div class=sec>ATTENDANCE · THIS MONTH · 13 OF 15 DAYS</div><div class=dg>{"".join(f'<i class={c}>{c}</i>' for c in days)}</div>
<div class=sec>FEES · SAMPLE</div>{"".join(f'<div class=fr><span>{a}</span><em class={c}>{b}</em></div>' for a,b,c in [("Instalment 1","Paid","pd"),("Instalment 2","Paid","pd"),("Instalment 3","Due on 5th","du")])}
<div class=rm>{ic("bell",22)} Fee reminder goes out 3 days before the due date.</div></div>''',
""".vis{flex-direction:column}
.stu{flex:1;padding:26px 28px;display:flex;flex-direction:column;gap:12px}
.sh{display:flex;align-items:center;gap:16px}.av{width:60px;height:60px;border-radius:50%;background:#ff7a1a;color:#fff;font:800 26px/60px 'Bitter';text-align:center}
.sh b{display:block;font:800 26px 'Bitter'}.sh small{font:500 18px Poppins;color:#59628f}
.sec{font:700 14px Poppins;letter-spacing:3px;color:#9aa2c8;margin-top:6px}
.dg{display:grid;grid-template-columns:repeat(15,1fr);gap:7px}.dg i{aspect-ratio:1;border-radius:10px;font-style:normal;font:700 16px Poppins;display:flex;align-items:center;justify-content:center}
.dg i.P{background:#e4e8ff;color:#2342d6}.dg i.A{background:#ffe0e0;color:#c62828}
.fr{flex:1;display:flex;align-items:center;justify-content:space-between;background:#f5f7ff;border-radius:14px;padding:0 22px;font:700 26px Poppins}
.fr em{font-style:normal;font:700 18px Poppins;padding:6px 12px;border-radius:10px}.pd{background:#dff5e7;color:#1f8a4c}.du{background:#ffe7d6;color:#c2560c}
.rm{display:flex;align-items:center;gap:10px;font:600 19px Poppins;color:#2342d6;background:#eef1ff;border-radius:14px;padding:14px 16px}
""")

P["p52_institute_s5"] = ct(5, rail(4) + """<h1>Step 4: Certificates made<br><span>from the records.</span></h1><div class=sub>Name, course and dates filled in from the app. No typing mistakes.</div>""",
f'''<div class=cert><div class=cin><small>CERTIFICATE OF COMPLETION · SAMPLE</small><b>Sample Student</b><p>has completed the course</p><h4>Web Design</h4><p>at Your Institute, from June to November</p>
<div class=sig><span><i></i>Course trainer</span><span class=seal>{ic("shield",40)}</span><span><i></i>Director</span></div></div></div>
<div class=chk>{"".join(f'<div>{ic("check",22,w=3)}<span>{t}</span></div>' for t in ["Only for those who finished","Download as PDF","Same design every time"])}</div>''',
""".vis{flex-direction:column;gap:18px}
.cert{flex:1;background:#fff;border-radius:22px;padding:16px;box-shadow:0 18px 40px rgba(20,33,92,.10);display:flex}
.cin{flex:1;border:3px double #2342d6;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;text-align:center;background:radial-gradient(circle at 50% 0,#fff3e8,transparent 60%)}
.cin small{font:700 17px Poppins;letter-spacing:4px;color:#ff7a1a}.cin b{font:800 66px/1.25 'Bitter'}.cin p{font:500 25px Poppins;color:#59628f}.cin h4{font:800 48px/1.25 'Bitter';color:#2342d6}
.sig{display:flex;align-items:center;gap:50px;margin-top:26px}.sig span{display:flex;flex-direction:column;align-items:center;gap:8px;font:600 19px Poppins;color:#59628f}.sig i{width:150px;height:2px;background:#9aa2c8;display:block}
.seal{width:96px;height:96px;border-radius:50%;background:#ff7a1a;color:#fff;justify-content:center}
.chk{display:flex;gap:14px}.chk div{flex:1;background:#14215c;color:#fff;border-radius:18px;padding:18px;display:flex;align-items:center;gap:10px;font:600 20px/1.3 Poppins}.chk svg{color:#ff7a1a;flex:none}
""")

P["p52_institute_s6"] = ct(6, """<div style="font:700 17px Poppins;letter-spacing:4px;color:#ff7a1a;margin-top:22px">FOR YOUR INSTITUTE</div><h1 style="margin-top:10px">Want one app for<br><span>your whole institute?</span></h1>
<div class=sub>We build enquiry, batch, fee and certificate tools for training institutes.</div>""",
f'''<div class=w>{peep("Explaining","Smile","Short","None",w=400,h=660)}<div class=ops>{"".join(f'<div class=op><span>{k}</span><div><b>{a}</b><small>{b}</small></div></div>' for k,a,b in [(1,"Enquiry list","From website, calls and walk-ins"),(2,"Batch seats","Know what is full"),(3,"Attendance + fees","With reminders"),(4,"Certificates","From your records")])}</div></div>''',
""".vis{align-items:stretch}.w{display:flex;align-items:flex-end;gap:16px;width:100%}
.ops{flex:1;align-self:stretch;display:flex;flex-direction:column;gap:14px}
.op{flex:1;background:#fff;border-radius:22px;padding:0 24px;display:flex;align-items:center;gap:18px;box-shadow:0 14px 30px rgba(20,33,92,.08)}
.op span{width:58px;height:58px;border-radius:50%;background:#ff7a1a;color:#fff;font:800 26px/58px 'Bitter';text-align:center;flex:none}
.op b{display:block;font:800 27px/1.25 'Bitter'}.op small{font:500 18px Poppins;color:#59628f}
""", cta="Tell us about your institute. DM us", ctacss="background:#ff7a1a;color:#fff")

if __name__ == "__main__":
    import asyncio
    asyncio.run(render(P, "work/out", sys.argv[1:] or None))
