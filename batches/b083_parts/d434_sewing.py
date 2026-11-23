
# ───────── 434 INDIA · Sewing and tailoring classes (adult batches) · SINGLE · TeX Gyre Adventor + Open Sans · denim / tape yellow / chalk white
# New technique: measuring-tape progress bars (CSS tick marks via repeating gradients, numbered every 5 lessons) for each
# learner, plus a seat-dot batch timetable; every count comes from one learner list.
DN4 = "#2b4a74"; TP4 = "#f2c94c"; CW4 = "#f7f5f0"; INK4 = "#1e2633"; MU4 = "#667085"; RS4 = "#d0607a"
LS4 = 30
BT4 = [("10 AM", "Basic", 12, 10), ("2 PM", "Blouse", 10, 10), ("5 PM", "Kurti and salwar", 12, 7)]
ST4 = [("Sample Learner A", "10 AM", "Basic", 8, "Fri 27 Nov"), ("Sample Learner B", "2 PM", "Blouse", 21, ""), ("Sample Learner C", "2 PM", "Blouse", 27, ""),
       ("Sample Learner D", "5 PM", "Kurti and salwar", 14, "Mon 30 Nov"), ("Sample Learner E", "10 AM", "Basic", 30, ""), ("Sample Learner F", "5 PM", "Kurti and salwar", 3, "")]
DUE4 = [s for s in ST4 if s[4]]; CERT4 = [s for s in ST4 if s[3] >= LS4]
def tape4(done):
    return f'''<div class=tp><div class=fl style="width:{done / LS4 * 100:.2f}%"></div><div class=tk></div>{"".join(f'<span style="left:{k / LS4 * 100:.2f}%">{k}</span>' for k in range(5, LS4, 5))}</div>'''
P["p434_sewing"] = page(f"""
body{{--f:'Open Sans';--h:'TeX Gyre Adventor';background:{CW4};color:{INK4}}}
.kk{{font:700 16px/1.4 'Open Sans';letter-spacing:3px;color:{RS4};margin-top:22px}}
h1{{font-family:'TeX Gyre Adventor';font-weight:700;font-size:58px;line-height:1.2;letter-spacing:-1.5px;margin-top:14px}} h1 span{{color:{DN4}}}
.w4{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm4{{font:700 13px/1.4 'Open Sans';letter-spacing:2px;color:{MU4}}}
.cd4{{background:#fff;border-radius:22px;box-shadow:0 14px 30px rgba(43,74,116,.08);padding:16px 20px;display:flex;flex-direction:column;gap:10px}}
.bt4{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.bt4 .b{{background:{DN4};color:#fff;border-radius:20px;padding:14px 18px;display:flex;flex-direction:column;gap:6px}}.bt4 .b b{{font:700 30px/1.25 'TeX Gyre Adventor';color:{TP4}}}.bt4 .b span{{font:600 17px/1.3 'Open Sans'}}
.bt4 .dt{{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px}}.bt4 .dt{{gap:5px!important;flex-wrap:nowrap!important}}.bt4 .dt i{{width:16px;height:16px;border-radius:50%;background:{TP4}}}.bt4 .dt i.e{{background:none;border:2px solid rgba(255,255,255,.45)}}.bt4 .b small{{font:600 14px/1.3 'Open Sans';color:#c6d3e6}}
.mn4{{flex:1;display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.6fr);gap:16px;min-height:0}}
.pr4 .r{{flex:1;display:flex;flex-direction:column;justify-content:center;gap:6px;border-top:1px solid #ece9e2}}.pr4 .r .t{{display:flex;align-items:baseline;gap:10px}}.pr4 .r b{{font:700 19px/1.3 'Open Sans'}}.pr4 .r span{{font:500 15px/1.3 'Open Sans';color:{MU4};flex:1}}.pr4 .r strong{{font:700 18px/1.3 'TeX Gyre Adventor';color:{DN4}}}
.tp{{position:relative;height:34px;border-radius:5px;background:#fbe8a6;overflow:hidden;box-shadow:inset 0 0 0 1px #d8b43b}}.tp .fl{{position:absolute;left:0;top:0;bottom:0;background:{TP4}}}
.tp .tk{{position:absolute;inset:0;background:repeating-linear-gradient(90deg,#5b4a12 0 2px,transparent 2px calc(100% / 30)) top/100% 10px no-repeat}}
.tp span{{position:absolute;bottom:2px;transform:translateX(-50%);font:700 12px/1.2 'Open Sans';color:#5b4a12}}
.rt4{{display:flex;flex-direction:column;gap:16px;min-height:0}}.rt4 .cd4{{flex:none}}.rt4 .wl{{flex:1;background:{DN4};color:#fff;border-radius:22px;padding:16px 20px;display:flex;flex-direction:column;gap:8px;justify-content:center}}.rt4 .wl .sm4{{color:#c6d3e6}}.rt4 .wl b{{font:700 44px/1.2 'TeX Gyre Adventor';color:{TP4}}}.rt4 .wl p{{font:500 17px/1.45 'Open Sans'}}.rt4 .it{{display:flex;flex-direction:column;gap:2px;padding:8px 0;border-top:1px solid #ece9e2}}.rt4 .it b{{font:700 17px/1.3 'Open Sans'}}.rt4 .it span{{font:500 15px/1.35 'Open Sans';color:{MU4}}}
.rt4 .ce{{background:#fbe6ea;box-shadow:none}}.rt4 .ce .it{{border-color:#f1c9d2}}
""", "<div class=kk>SEWING CLASSES · ADULT BATCHES</div><h1>Sewing class in a register?<br><span>Batches, lessons, reminders.</span></h1>",
f'''<div class=w4><div class=bt4>{"".join(f"""<div class=b><span class=sm4 style="color:#c6d3e6">{t} BATCH</span><b>{n}</b><span>{f} of {c} seats filled</span><div class=dt>{"".join('<i></i>' for _ in range(f))}{"".join('<i class=e></i>' for _ in range(c - f))}</div></div>""" for t, n, c, f in BT4)}</div>
<div class=mn4><div class="cd4 pr4"><span class=sm4>LESSONS DONE OUT OF {LS4} · SAMPLE</span>{"".join(f'<div class=r><div class=t><b>{a}</b><span>{t} · {n}</span><strong>{d} / {LS4}</strong></div>{tape4(d)}</div>' for a, t, n, d, due in ST4)}</div>
<div class=rt4><div class=cd4><span class=sm4>FEE REMINDERS</span>{"".join(f'<div class=it><b>{s[0]}</b><span>Due {s[4]} · reminder sent</span></div>' for s in DUE4)}</div>
<div class="cd4 ce"><span class=sm4>CERTIFICATE READY</span>{"".join(f'<div class=it><b>{s[0]}</b><span>{s[2]} course done · {LS4} of {LS4} lessons</span></div>' for s in CERT4)}</div><div class=wl><span class=sm4>WAITING LIST · 2 PM BATCH</span><b>3 learners</b><p>The Blouse batch is full. They get a message as soon as a seat opens.</p></div></div></div></div>''',
INK4, "Run sewing classes? DM us", f"background:{DN4};color:#fff")
