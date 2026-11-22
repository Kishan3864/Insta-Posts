import sys, random; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}

# ───────── 176 INDIA · Packaging pouch & label supplier · SINGLE · Poppins + Fira Sans · kraft / ink black / tomato
# New techniques: SVG label roll unrolling into a strip of printed labels + ticket-stub job card with perforation and stage punches.
def roll():
    labs = "".join(f'<g><rect x="{250+i*130}" y="128" width="112" height="84" rx="10" fill="#fff" stroke="#e23e2b" stroke-width="3"/><text x="{306+i*130}" y="166" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="18" fill="#1d1b19"><tspan>YOUR</tspan></text><text x="{306+i*130}" y="192" text-anchor="middle" font-family="Poppins" font-weight="800" font-size="18" fill="#e23e2b"><tspan>BRAND</tspan></text></g>' for i in range(4))
    return ('<svg viewBox="0 0 800 300" width="100%" style="display:block"><rect x="200" y="110" width="580" height="120" fill="#f3e3c8"/>' + labs +
            '<circle cx="140" cy="170" r="120" fill="#f3e3c8" stroke="#c9a77a" stroke-width="4"/><circle cx="140" cy="170" r="96" fill="none" stroke="#e0c9a6" stroke-width="3"/><circle cx="140" cy="170" r="72" fill="none" stroke="#e0c9a6" stroke-width="3"/>'
            '<circle cx="140" cy="170" r="44" fill="#8a6a45"/><circle cx="140" cy="170" r="22" fill="#d9c09a"/></svg>')
stages = [("Proof sent", "Mon", 1), ("Approved", "Tue", 1), ("Printing", "Wed", 1), ("Slitting", "Thu", 0), ("Dispatch", "Fri", 0)]
P["p176_labels"] = page("""
body{--f:'Fira Sans';--h:'Poppins';background:#d9c09a;color:#1d1b19}
h1{font-family:'Poppins';font-size:60px;font-weight:800;letter-spacing:-1.4px;line-height:1.2} h1 span{color:#e23e2b}
.sub{color:#4b3f31;font-size:23px}
.vis{flex-direction:column;gap:18px}
.rl{background:#fff8ec;border-radius:28px;padding:22px 24px 16px;display:flex;flex-direction:column;gap:6px;box-shadow:0 16px 34px rgba(29,27,25,.12)}
.rl small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#8a6a45}
.tk{flex:1;display:flex;filter:drop-shadow(0 16px 30px rgba(29,27,25,.14))}
.tk .m{flex:1;background:#fff8ec;border-radius:28px 0 0 28px;padding:22px 26px;display:flex;flex-direction:column;gap:12px}
.tk .s{width:250px;flex:none;background:#1d1b19;color:#fff;border-radius:0 28px 28px 0;padding:22px;display:flex;flex-direction:column;justify-content:center;gap:8px;border-left:4px dashed #d9c09a}
.tk .m small{font:700 14px 'Fira Sans';letter-spacing:2.5px;color:#8a6a45}.tk .m h3{font:800 32px/1.2 Poppins}
.sp{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}.sp div{background:#f3e3c8;border-radius:14px;padding:10px 14px}.sp span{display:block;font:700 13px 'Fira Sans';letter-spacing:2px;color:#8a6a45}.sp b{font:700 22px 'Fira Sans'}
.st{flex:1;display:flex;gap:8px;align-items:stretch}.st div{flex:1;border-radius:16px;border:3px solid #1d1b19;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:4px;text-align:center;padding:6px}
.st div.d{background:#1d1b19;color:#fff}.st div.n{border-style:dashed;color:#6b5a45}.st b{font:700 19px/1.2 'Fira Sans'}.st span{font:600 16px 'Fira Sans';opacity:.75}
.tk .s small{font:700 13px 'Fira Sans';letter-spacing:2px;color:#e8b9a0}.tk .s b{font:800 54px/1.15 Poppins;color:#ff6a52}.tk .s span{font:500 19px/1.4 'Fira Sans'}
""", "<h1>Label order stuck between<br><span>proof, print and dispatch?</span></h1><div class=sub>One job ticket shows the stage, rolls and date for every order.</div>",
f'''<div class=rl><small>JOB J-342 · PRINTED LABELS · SAMPLE</small>{roll()}</div>
<div class=tk><div class=m><small>JOB TICKET · SAMPLE CLIENT</small><h3>Paper labels for spice jars</h3>
<div class=sp>{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a,b in [("SIZE","50 × 38 mm"),("ROLLS","20 × 1,000"),("CORE","3 inch")])}</div>
<div class=st>{"".join(f'<div class="{"d" if d else "n"}">{ic("check",22,w=3) if d else ""}<b>{a}</b><span>{w}</span></div>' for a,w,d in stages)}</div></div>
<div class=s><small>DISPATCH</small><b>Fri</b><span>4 Dec, by courier. The client gets the tracking link.</span></div></div>''',
"#1d1b19", "Supply labels or pouches? DM us", "background:#1d1b19;color:#fff")


# ───────── 177 USA · Law office · CAROUSEL 5 · Lora + Source Sans 3 · oxford navy / cream / burgundy
# New techniques: intake form with practice-area chips, consultation calendar with booked blocks, client document checklist with upload rows, legal-pad CTA.
LW = """
body{--f:'Source Sans 3';--h:'Lora';background:#f5efe3;color:#1b2a47}
h1{font-family:'Lora';font-weight:700;font-size:62px;letter-spacing:-.6px;line-height:1.2} h1 span{color:#8c2338}
.kk{font:700 16px 'Source Sans 3';letter-spacing:3px;color:#8c2338;margin-top:22px}
.cd{background:#fff;border-radius:24px;box-shadow:0 14px 30px rgba(27,42,71,.08)}
"""
def lw(n, head, vis, css="", cta="Swipe", ctacss="background:#1b2a47;color:#fff"):
    return page(LW + css, head, vis, "#1b2a47", cta, ctacss, tagline=f"{n} / 5")
P["p177_law_s1"] = lw(1, "<div class=kk>LAW OFFICES</div><h1>New clients call<br>while you're in court?<br><span>Let them book online.</span></h1>",
f'''<div class="cd ms">{"".join(f'<div class="mr {k}"><span class=ib>{ic(i,28)}</span><div><b>{a}</b><span>{b}</span></div><em>{t}</em></div>' for i,a,b,t,k in [("phone","Missed call","Sample caller · no message left","10:12 AM","x"),("phone","Missed call","Sample caller · voicemail","11:40 AM","x"),("check","Consultation booked","Sample client · online intake done","12:05 PM","ok"),("check","Consultation booked","Sample client · 3 documents added","2:30 PM","ok")])}</div>''',
css=""".vis{display:flex}.ms{flex:1;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.mr{flex:1;display:flex;align-items:center;gap:18px;border-radius:18px;padding:0 20px;background:#f8f4ec}
.mr .ib{width:58px;height:58px;border-radius:16px;background:#e8dfd0;color:#6b6457}.mr.ok .ib{background:#1b2a47;color:#fff}
.mr div{flex:1}.mr b{display:block;font:700 27px Lora}.mr span{font:500 20px 'Source Sans 3';color:#6b6457}.mr em{font-style:normal;font:700 19px 'Source Sans 3';color:#6b6457}
.mr.x b{color:#8c2338}.mr.ok{background:#eef1f7}""")

P["p177_law_s2"] = lw(2, "<div class=kk>PART 1 · INTAKE FORM</div><h1>Know the matter<br><span>before the first call.</span></h1>",
browser(f'''<div class=fm><b class=t>Request a consultation</b>
<div class=fl><small>WHAT IS IT ABOUT?</small><div class=ch>{"".join(f'<i class="{"on" if o else ""}">{a}</i>' for a,o in [("Business contract",1),("Lease",0),("Estate planning",0),("Small claims",0),("Other",0)])}</div></div>
<div class=r2><div class=fl><small>NAME</small><span>Sample Client</span></div><div class=fl><small>BEST TIME TO REACH YOU</small><span>Afternoons</span></div></div>
<div class=fl><small>SHORT SUMMARY</small><span class=q>Supplier contract renewal, want it reviewed before signing.</span></div>
<div class=fl><small>DOCUMENTS</small><span>contract_draft.pdf · 2 more</span></div>
<div class=bt>Continue to booking</div></div>''', url="yourlawoffice.com/intake · sample", style="flex:1"),
css=""".vis{display:flex}.fm{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:12px}.fm .t{font:700 34px Lora}
.fl{flex:1;background:#f8f4ec;border-radius:16px;padding:12px 16px;display:flex;flex-direction:column;justify-content:center;gap:6px}.fl small{font:700 13px 'Source Sans 3';letter-spacing:2px;color:#8a8170}.fl span{font:600 23px 'Source Sans 3'}.fl .q{font:italic 500 23px/1.4 Lora}
.ch{display:flex;flex-wrap:wrap;gap:8px}.ch i{font-style:normal;font:600 19px 'Source Sans 3';border:2px solid #ddd3c2;border-radius:30px;padding:6px 16px;background:#fff}.ch .on{background:#1b2a47;color:#fff;border-color:#1b2a47}
.r2{display:flex;gap:12px}.r2 .fl{flex:1}.bt{background:#8c2338;color:#fff;border-radius:16px;padding:16px;text-align:center;font:700 21px 'Source Sans 3'}""")

cal = {("Mon", 0): "b", ("Mon", 2): "c", ("Tue", 1): "c", ("Tue", 3): "b", ("Wed", 0): "c", ("Wed", 1): "c", ("Thu", 2): "b", ("Fri", 0): "c", ("Fri", 3): "s"}
times = ["9:00 AM", "11:00 AM", "2:00 PM", "4:00 PM"]
dd = ["Mon", "Tue", "Wed", "Thu", "Fri"]
P["p177_law_s3"] = lw(3, "<div class=kk>PART 2 · CONSULTATIONS</div><h1>Clients pick a slot<br><span>you have left open.</span></h1>",
f'''<div class="cd cl"><div class=g><span></span>{"".join(f'<span class=dh>{d}</span>' for d in dd)}
{"".join(f'<span class=th>{t}</span>' + "".join(f'<span class="c k{cal.get((d,i),"o")}">{dict(b="Court",c="Consult",s="Selected")[cal[(d,i)]] if (d,i) in cal else "Open"}</span>' for d in dd) for i,t in enumerate(times))}</div>
<div class=lg>{"".join(f'<span><i class={k}></i>{t}</span>' for k,t in [("o","Open"),("cc","Consult booked"),("bb","Court or blocked"),("ss","This booking")])}</div></div>''',
css=""".vis{display:flex}.cl{flex:1;padding:22px;display:flex;flex-direction:column;gap:14px}
.g{flex:1;display:grid;grid-template-columns:120px repeat(5,1fr);grid-template-rows:40px repeat(4,1fr);gap:8px}
.dh{font:700 20px 'Source Sans 3';text-align:center;align-self:center}.th{font:700 18px 'Source Sans 3';color:#6b6457;align-self:center}
.c{border-radius:14px;display:flex;align-items:center;justify-content:center;font:600 18px 'Source Sans 3';background:#f8f4ec;color:#a49a88;border:2px dashed #ddd3c2}
.c.kc{background:#dfe5f1;color:#1b2a47;border:none}.c.kb{background:#1b2a47;color:#fff;border:none}.c.ks{background:#8c2338;color:#fff;border:none}
.lg{display:flex;gap:20px;flex-wrap:wrap;font:600 18px 'Source Sans 3'}.lg span{display:flex;gap:8px;align-items:center}.lg i{width:20px;height:20px;border-radius:6px}
.lg .o{border:2px dashed #ddd3c2}.lg .cc{background:#dfe5f1}.lg .bb{background:#1b2a47}.lg .ss{background:#8c2338}""")

docs = [("Contract draft", "Uploaded Tue", 1), ("Old contract (2024)", "Uploaded Tue", 1), ("Emails with supplier", "Uploaded Wed", 1), ("Company registration", "Still needed", 0), ("ID for the signer", "Still needed", 0)]
P["p177_law_s4"] = lw(4, "<div class=kk>PART 3 · DOCUMENTS</div><h1>No more chasing papers<br><span>by email.</span></h1>",
f'''<div class="cd dl"><div class=hd><div><small>SAMPLE CLIENT · CONTRACT REVIEW</small><b>Documents for Friday's consult</b></div><em>3 of 5</em></div>
<div class=bar><div style="width:60%"></div></div>
{"".join(f'<div class="dr {"y" if o else "n"}"><span class=ib>{ic("file" if o else "upload",26)}</span><div><b>{a}</b><span>{s}</span></div>{"<i>" + ic("check",22,w=3) + "</i>" if o else "<em>Upload</em>"}</div>' for a,s,o in docs)}
<div class=nt>A reminder goes to the client 2 days before the meeting if anything is missing.</div></div>''',
css=""".vis{display:flex}.dl{flex:1;padding:22px 26px;display:flex;flex-direction:column;gap:10px}
.hd{display:flex;justify-content:space-between;align-items:center}.hd small{display:block;font:700 14px 'Source Sans 3';letter-spacing:2px;color:#8a8170}.hd b{font:700 30px/1.3 Lora}.hd em{font-style:normal;font:700 28px Lora;color:#8c2338}
.bar{height:14px;border-radius:7px;background:#efe8db}.bar div{height:100%;background:#8c2338;border-radius:7px}
.dr{flex:1;display:flex;align-items:center;gap:16px;border-bottom:2px solid #f1ebdf}.dr .ib{width:52px;height:52px;border-radius:14px;background:#eef1f7;color:#1b2a47}.dr.n .ib{background:#f6e3e6;color:#8c2338}
.dr div{flex:1}.dr b{display:block;font:600 24px 'Source Sans 3'}.dr span{font:500 18px 'Source Sans 3';color:#8a8170}.dr.n span{color:#8c2338}
.dr i{width:40px;height:40px;border-radius:50%;background:#1b2a47;color:#fff;display:flex;align-items:center;justify-content:center}.dr em{font-style:normal;font:700 18px 'Source Sans 3';border:2px solid #8c2338;color:#8c2338;border-radius:12px;padding:7px 14px}
.nt{background:#1b2a47;color:#fff;border-radius:16px;padding:14px 18px;font:500 20px/1.4 'Source Sans 3'}""")

P["p177_law_s5"] = lw(5, "<div class=kk>YOUR TURN</div><h1>Run a small law office?<br><span>Let's build your client portal.</span></h1>",
f'''<div class=pad><div class=clip></div>{"".join(f'<div class=ln><span class=ib>{ic(i,28)}</span><b>{a}</b><span class=s>{b}</span></div>' for i,a,b in [("doc","Online intake","know the matter first"),("cal","Consult booking","only your open slots"),("upload","Document portal","no chasing by email"),("bell","Reminders","before every meeting")])}</div>''',
css=""".vis{display:flex}.pad{flex:1;background:#fdf3b8;border-radius:10px 10px 26px 26px;padding:70px 34px 26px;display:flex;flex-direction:column;position:relative;box-shadow:0 16px 34px rgba(27,42,71,.14);}
.clip{position:absolute;left:0;right:0;top:0;height:44px;background:#1b2a47;border-radius:10px 10px 0 0}
.pad:before{content:'';position:absolute;left:84px;top:44px;bottom:0;width:3px;background:#e8a0a8}
.ln{flex:1;display:flex;align-items:center;gap:22px;padding-left:80px;border-bottom:2px solid #a9c4e8}.ln .ib{width:58px;height:58px;border-radius:16px;background:#1b2a47;color:#fff}
.ln b{font:700 36px Lora}.ln .s{font:500 21px 'Source Sans 3';color:#5d5540;margin-left:auto}""",
cta="DM us to start", ctacss="background:#8c2338;color:#fff")


# ───────── 178 INDIA · Inverter & battery installer · SINGLE · TeX Gyre Adventor + Roboto · deep blue / electric cyan / white
# New technique: appliance toggle grid (on/off switches with counts) feeding a load meter bar; result says "as per your sizing chart" (no invented specs).
apps = [("Ceiling fans", "3", "on"), ("LED lights", "8", "on"), ("Wi-Fi router", "1", "on"), ("TV", "1", "on"), ("Fridge", "1", "on"), ("Laptop", "2", "on"), ("Water pump", "1", "off"), ("Mixer", "1", "off")]
P["p178_inverter"] = page("""
body{--f:'Roboto';--h:'TeX Gyre Adventor';background:#0e2a5c;color:#fff}
h1{font-family:'TeX Gyre Adventor';font-size:60px;font-weight:700;letter-spacing:-1px;line-height:1.22} h1 span{color:#3ee0f0}
.sub{color:#b9c9e8;font-size:23px}
.vis{flex-direction:column;gap:16px}
.fm{flex:1;background:#fff;color:#0e2a5c;border-radius:28px;padding:20px 22px;display:flex;flex-direction:column;gap:12px}
.fm .h{display:flex;justify-content:space-between;align-items:baseline}.fm .h b{font:700 28px 'TeX Gyre Adventor'}.fm .h small{font:700 14px Roboto;letter-spacing:2px;color:#7d8bab}
.gr{flex:1;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.ap{border-radius:16px;background:#f2f5fb;display:flex;align-items:center;gap:14px;padding:0 16px}
.ap .n{width:44px;height:44px;border-radius:12px;background:#0e2a5c;color:#3ee0f0;display:flex;align-items:center;justify-content:center;font:700 21px 'TeX Gyre Adventor';flex:none}
.ap b{flex:1;font:600 22px Roboto}
.sw{width:66px;height:36px;border-radius:18px;background:#c9d2e3;position:relative;flex:none}.sw:after{content:'';position:absolute;top:4px;left:4px;width:28px;height:28px;border-radius:50%;background:#fff}
.ap.on .sw{background:#11b5c7}.ap.on .sw:after{left:34px}.ap.off{opacity:.6}
.ld{background:#16397a;border-radius:24px;padding:18px 22px;display:flex;flex-direction:column;gap:12px}
.ld .t{display:flex;justify-content:space-between;font:700 20px Roboto}.ld .t span{color:#3ee0f0}
.mt{height:30px;border-radius:15px;background:#0e2a5c;display:flex;overflow:hidden;gap:3px}.mt i{height:100%}
.rs{display:flex;gap:12px}.rs div{flex:1;background:#0e2a5c;border-radius:16px;padding:12px 16px}.rs small{display:block;font:700 13px Roboto;letter-spacing:2px;color:#8fa6d6}.rs b{font:700 23px/1.3 Roboto}
""", "<h1>“Which inverter do I need?”<br><span>Let them pick what runs.</span></h1><div class=sub>A load form on your website, so every enquiry comes with the details.</div>",
f'''<div class=fm><div class=h><b>What should run in a power cut?</b><small>SAMPLE HOME</small></div><div class=gr>{"".join(f'<div class="ap {k}"><span class=n>{q}</span><b>{a}</b><span class=sw></span></div>' for a,q,k in apps)}</div></div>
<div class=ld><div class=t><b>Load picked: 6 types, 16 items</b><span>Pump and mixer off</span></div><div class=mt>{"".join(f'<i style="flex:{f};background:{c}"></i>' for f,c in [(3,"#3ee0f0"),(2,"#5fc8ff"),(1,"#8fe6c8"),(2,"#3ee0f0"),(3,"#5fc8ff"),(1,"#8fe6c8"),(4,"#16397a")])}</div>
<div class=rs>{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a,b in [("BACKUP WANTED","4 hours"),("SUGGESTED SIZE","As per your chart"),("SITE VISIT","Sat, 5 Dec · 11 AM")])}</div></div>''',
"#ffffff", "Install inverters? DM us", "background:#3ee0f0;color:#0e2a5c", logo_color="#ffffff")


# ───────── 179 INDIA · Loan agent (DSA) · SINGLE · Bitter + DM Sans · slate green / peach / white
# New technique: filing-cabinet drawer of lead folders with coloured tabs + the open folder's document checklist (no rates, no approvals promised).
leads = [("Lead 1", "Home loan", "6 of 8 docs", "#f4a37a"), ("Lead 2", "Business loan", "8 of 8 docs", "#7fc4a0"), ("Lead 3", "Car loan", "3 of 6 docs", "#f4a37a"), ("Lead 4", "Home loan", "1 of 8 docs", "#e6e9e7")]
chk = [("ID proof", 1), ("Address proof", 1), ("Salary slips, last 3 months", 1), ("Bank statement, 6 months", 1), ("Property papers", 1), ("Photo", 1), ("Form 16", 0), ("Co-applicant ID", 0)]
P["p179_dsa"] = page("""
body{--f:'DM Sans';--h:'Bitter';background:#e7eeea;color:#22362e}
h1{font-family:'Bitter';font-size:60px;font-weight:800;letter-spacing:-.8px;line-height:1.2} h1 span{color:#d7663a}
.sub{color:#51645c;font-size:23px}
.vis{gap:18px}
.cab{width:380px;flex:none;background:#3d5a4e;border-radius:26px;padding:18px;display:flex;flex-direction:column;gap:12px}
.cab small{font:700 14px 'DM Sans';letter-spacing:2.5px;color:#c4d6cd}
.fd{flex:1;border-radius:6px 16px 16px 16px;background:#fff;padding:14px 18px;display:flex;flex-direction:column;justify-content:center;position:relative;margin-top:16px}
.fd:before{content:'';position:absolute;left:0;top:-16px;width:120px;height:18px;border-radius:8px 8px 0 0;background:var(--c)}
.fd b{font:800 24px Bitter}.fd span{font:500 18px 'DM Sans';color:#51645c}.fd em{position:absolute;right:16px;top:50%;transform:translateY(-50%);font-style:normal;font:700 16px 'DM Sans';background:var(--c);border-radius:10px;padding:5px 10px}
.fd.on{box-shadow:0 0 0 4px #d7663a}
.op{flex:1;background:#fff;border-radius:26px;padding:20px 24px;display:flex;flex-direction:column;gap:8px;box-shadow:0 16px 34px rgba(34,54,46,.10)}
.op .hd small{display:block;font:700 14px 'DM Sans';letter-spacing:2.5px;color:#7b8d85}.op .hd b{font:800 30px/1.3 Bitter}
.ck{flex:1;display:flex;align-items:center;gap:14px;border-bottom:1.5px solid #edf1ee;font:600 21px 'DM Sans'}
.ck i{width:34px;height:34px;border-radius:10px;display:flex;align-items:center;justify-content:center;flex:none;border:3px solid #3d5a4e}.ck.y i{background:#3d5a4e;color:#fff}.ck.n{color:#d7663a}.ck.n i{border-color:#d7663a}
.op .bt{background:#d7663a;color:#fff;border-radius:16px;padding:14px;text-align:center;font:700 19px 'DM Sans'}
""", "<h1>Files stuck for one<br><span>missing document?</span></h1><div class=sub>Every lead has its own checklist, and the customer gets one upload link.</div>",
f'''<div class=cab><small>LEADS THIS WEEK · SAMPLE</small>{"".join(f'<div class="fd {"on" if i==0 else ""}" style="--c:{c}"><b>{a}</b><span>{t}</span><em>{d}</em></div>' for i,(a,t,d,c) in enumerate(leads))}</div>
<div class=op><div class=hd><small>LEAD 1 · HOME LOAN · SAMPLE</small><b>Documents: 6 of 8</b></div>{"".join(f'<div class="ck {"y" if o else "n"}"><i>{ic("check",20,w=3) if o else ""}</i>{a}</div>' for a,o in chk)}<div class=bt>Send upload link for 2 missing</div></div>''',
"#22362e", "Work as a loan agent? DM us", "background:#3d5a4e;color:#fff")


# ───────── 180 CANADA · Restaurant direct online ordering · SINGLE · Montserrat + Lora · tomato / cream / espresso
# New technique: pickup shelf of cubbies with paper order bags (name + order number + ready state) fed by a direct-order counter screen.
bags = [("#204", "Sample A.", "Ready", "r"), ("#205", "Sample K.", "Ready", "r"), ("#206", "Sample J.", "Packing", "p"), ("#207", "Sample M.", "Ready", "r"), ("#208", "Sample T.", "6:15 PM", "w"), ("#209", "Sample L.", "6:20 PM", "w")]
def bag(c="#c99a63"):
    return f'<svg viewBox="0 0 120 130" width="150" style="display:block"><path d="M14 36 L106 36 L100 126 L20 126 Z" fill="{c}"/><path d="M14 36 L30 14 L90 14 L106 36" fill="{c}" opacity=".75"/><path d="M44 36 Q44 6 60 6 Q76 6 76 36" fill="none" stroke="#6b4b2e" stroke-width="5"/></svg>'
P["p180_resto"] = page("""
body{--f:'Lora';--h:'Montserrat';background:#f8efe1;color:#3a2418}
h1{font-family:'Montserrat';font-size:58px;font-weight:800;letter-spacing:-1.4px;line-height:1.2} h1 span{color:#e1412e}
.sub{color:#6b5244;font-size:23px}
.vis{flex-direction:column;gap:16px}
.sh{flex:1;background:#5a3a26;border-radius:26px;padding:16px;display:grid;grid-template-columns:repeat(3,1fr);grid-template-rows:1fr 1fr;gap:12px}
.cb{background:#3a2418;border-radius:14px;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;gap:6px;padding:10px 10px 12px;box-shadow:inset 0 10px 18px rgba(0,0,0,.35)}
.cb .tg{background:#fff;border-radius:10px;padding:6px 12px;text-align:center}.cb .tg b{display:block;font:800 26px Montserrat}.cb .tg span{font:600 19px Lora}
.cb em{font-style:normal;font:700 18px Montserrat;border-radius:10px;padding:4px 12px}.cb .r{background:#3fae6b;color:#fff}.cb .p{background:#f2b33d;color:#3a2418}.cb .w{background:#7a5a46;color:#f8efe1}
.cn{background:#fff;border-radius:24px;padding:16px 20px;display:flex;align-items:center;gap:18px;box-shadow:0 14px 30px rgba(58,36,24,.10)}
.cn .ib{width:60px;height:60px;border-radius:18px;background:#e1412e;color:#fff}.cn div{flex:1}.cn b{display:block;font:800 25px Montserrat}.cn span{font:500 19px Lora;color:#6b5244}
.cn .st{display:flex;gap:10px}.cn .st i{font-style:normal;text-align:center;background:#f8efe1;border-radius:14px;padding:8px 14px}.cn .st i b{font:800 26px Montserrat;color:#e1412e}.cn .st i small{display:block;font:600 14px Lora}
""", "<h1>Orders through your own site,<br><span>picked up from one shelf.</span></h1><div class=sub>Customers order direct, get a text when the bag is ready, and grab it.</div>",
f'''<div class=sh>{"".join(f'<div class=cb>{bag("#c99a63" if k!="w" else "#8a6a52")}<div class=tg><b>{n}</b><span>{a}</span></div><em class={k}>{s}</em></div>' for n,a,s,k in bags)}</div>
<div class=cn><span class=ib>{ic("cart",30)}</span><div><b>Direct orders tonight · sample</b><span>Ordered on your website, paid online, picked up here</span></div><div class=st>{"".join(f'<i><b>{a}</b><small>{b}</small></i>' for a,b in [("3","ready"),("1","packing"),("2","later")])}</div></div>''',
"#3a2418", "Run a restaurant? DM us", "background:#e1412e;color:#fff")


if __name__ == "__main__":
    import asyncio
    keys = sys.argv[1:] or None
    asyncio.run(render(P, "work/out", keys))
