# ───────── 453 INDIA · Xerox and print shop (job tokens + weekly statement) · SINGLE · Anton + Fira Sans · toner black / copy white / highlighter yellow
# New technique: receipt-style weekly statement on perforated paper (radial-gradient punch holes on top, zigzag bottom),
# totals computed from the day rows; queue tokens with sheets computed from pages × copies and a live printing bar.
TB3 = "#17181b"; YL3 = "#f6e04b"; PW3 = "#fbfaf6"; MU3 = "#6a6d74"; CY3 = "#1aa3c7"; MG3 = "#d6337f"
Q3 = [("T-38", "Rent agreement.pdf", 6, 3, "B/W", "", "Collected", "11:05 AM"),
      ("T-39", "Menu card.pdf", 2, 50, "Colour", "laminated", "Ready", "1:40 PM"),
      ("T-40", "Project report.pdf", 48, 2, "B/W", "spiral binding", "Printing", "4:30 PM"),
      ("T-41", "Photos.zip", 12, 1, "Colour", "4 × 6 photo paper", "Next", "3:15 PM"),
      ("T-42", "Form.pdf", 4, 20, "B/W", "", "Received", "5:00 PM")]
NOW3 = [q for q in Q3 if q[6] == "Printing"][0]; DONE3 = 62; TOT3 = NOW3[2] * NOW3[3]
assert DONE3 < TOT3
ST3 = {"Collected": ("#e4e5e8", MU3), "Ready": ("#dff3df", "#256b2a"), "Printing": (YL3, TB3), "Next": ("#dff1f7", "#14708a"), "Received": ("#fbe3ee", "#9c2459")}
WK3 = [("Mon 16", 120, 8, 3), ("Tue 17", 86, 0, 2), ("Wed 18", 240, 24, 5), ("Thu 19", 64, 4, 2), ("Fri 20", 310, 40, 6), ("Sat 21", 45, 0, 1)]
MX3 = max(b + c for _, b, c, _ in WK3)
TW3 = (sum(r[1] for r in WK3), sum(r[2] for r in WK3), sum(r[3] for r in WK3))
IN3 = [("WhatsApp", 14), ("email", 3), ("pen drive", 5)]
P["p453_xerox"] = page(f"""
body{{--f:'Fira Sans';--h:'Anton';background:#e9e7e1;color:{TB3}}}
.kk3{{font:700 16px/1.4 'Fira Sans';letter-spacing:3px;color:{MU3};margin-top:22px;display:flex;gap:6px;align-items:center}}.kk3 i{{width:14px;height:14px;border-radius:50%}}
h1{{font-family:'Anton';font-weight:400;font-size:66px;line-height:1.2;letter-spacing:.2px;margin-top:12px;text-transform:uppercase}} h1 span{{background:linear-gradient(transparent 58%,{YL3} 58%,{YL3} 92%,transparent 92%)}}
.w3{{flex:1;display:grid;grid-template-columns:minmax(0,1.12fr) minmax(0,.88fr);gap:18px;min-height:0}}
.sm3{{font:700 13px/1.4 'Fira Sans';letter-spacing:2px;color:{MU3}}}
.lf{{display:flex;flex-direction:column;gap:14px;min-height:0}}
.np{{background:{TB3};color:#fff;border-radius:22px;padding:18px 22px;display:flex;flex-direction:column;gap:10px}}.np .sm3{{color:#a9acb3}}
.np .tp{{display:flex;justify-content:space-between;align-items:center;gap:12px}}.np .tk{{font:400 52px/1.2 Anton;color:{YL3}}}.np .tp p{{font:500 18px/1.4 'Fira Sans';text-align:right;color:#d9dbe0}}.np .tp p b{{display:block;font:700 22px/1.35 'Fira Sans';color:#fff}}
.np .bar{{height:16px;border-radius:9px;background:#33353b;overflow:hidden}}.np .bar i{{display:block;height:100%;background:{YL3};border-radius:9px}}.np .nm{{display:flex;justify-content:space-between;font:600 17px/1.3 'Fira Sans';color:#d9dbe0}}
.in{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}.in div{{background:#fff;border-radius:14px;padding:10px 14px}}.in b{{display:block;font:400 30px/1.3 Anton;margin-bottom:6px}}.in span{{font:600 15px/1.3 'Fira Sans';color:{MU3}}}
.qu{{flex:1;background:#fff;border-radius:22px;padding:14px 18px;display:flex;flex-direction:column;min-height:0;box-shadow:0 14px 30px rgba(0,0,0,.06)}}
.qu .r{{flex:1;display:grid;grid-template-columns:62px minmax(0,1fr) auto;gap:12px;align-items:center;border-top:1px solid #eeede9}}.qu .r:nth-child(2){{border:0}}
.qu .r>b{{font:400 22px/1.3 Anton;letter-spacing:.5px}}.qu .r div b{{display:block;font:700 18px/1.3 'Fira Sans'}}.qu .r div span{{font:500 15px/1.35 'Fira Sans';color:{MU3}}}
.qu .r em{{font:700 14px/1.3 'Fira Sans';font-style:normal;padding:5px 10px;border-radius:8px;white-space:nowrap;text-align:center}}
.rc{{position:relative;display:flex;flex-direction:column;min-height:0;filter:drop-shadow(0 14px 22px rgba(0,0,0,.12))}}
.pp{{flex:1;background:{PW3};padding:30px 26px 40px;display:flex;flex-direction:column;gap:6px;min-height:0;
-webkit-mask:radial-gradient(circle 7px at 50% 0,transparent 98%,#000) top/24px 100% repeat-x;
clip-path:polygon(0 0,100% 0,100% calc(100% - 14px),{",".join(f"{100 - i * 100 / 24:.2f}% {'100%' if i % 2 else 'calc(100% - 14px)'}" for i in range(1, 25))})}}
.pp .c{{text-align:center;font:700 14px/1.4 'DejaVu Sans Mono',monospace;color:{MU3};letter-spacing:1px}}.pp h3{{text-align:center;font:400 30px/1.25 Anton;letter-spacing:1px}}
.pp hr{{border:0;border-top:2px dashed #cfcdc6;margin:6px 0}}
.pp .r{{display:grid;grid-template-columns:minmax(0,1fr) 52px 46px 40px;gap:6px;font:500 17px/1.3 'DejaVu Sans Mono',monospace;padding:3px 0}}.pp .r span:not(:first-child){{text-align:right}}.pp .r.h span{{font:700 12px/1.3 'Fira Sans';letter-spacing:1px;color:{MU3}}}
.pp .r.t{{font-weight:700;font-size:19px}}.pp .gr{{flex:1;display:flex;flex-direction:column;justify-content:space-around}}
.dy{{display:flex;flex-direction:column;gap:5px}}.sb{{display:flex;height:9px;gap:2px}}.sb i{{display:block;height:100%;background:{TB3};border-radius:2px}}.sb i.co{{background:{MG3}}}.lg3{{display:flex;gap:14px;justify-content:center;font:600 14px/1.3 'Fira Sans';color:{MU3}}}.lg3 i{{display:inline-block;width:12px;height:12px;border-radius:2px;margin-right:6px;vertical-align:-1px}}.pp .ft3{{font:500 14px/1.45 'Fira Sans';color:{MU3};text-align:center}}.pp .ft3 b{{display:block;color:{TB3};font-size:15px}}
""", f"<div class=kk3>{''.join(f'<i style=background:{c}></i>' for c in (CY3, MG3, YL3, TB3))}&nbsp;XEROX · PRINT SHOP</div><h1>Print files lost in WhatsApp?<br><span>Every file gets a token.</span></h1>",
f'''<div class=w3><div class=lf><div class=np><span class=sm3>NOW PRINTING · SAMPLE · MON 23 NOV</span><div class=tp><div class=tk>{NOW3[0]}</div><p><b>{NOW3[1]}</b>{NOW3[2]} pages × {NOW3[3]} copies, {NOW3[5]}</p></div>
<div class=bar><i style="width:{DONE3 / TOT3 * 100:.1f}%"></i></div><div class=nm><span>{DONE3} of {TOT3} pages done</span><span>Ready by {NOW3[7]}</span></div></div>
<div class=in>{"".join(f'<div><b>{n}</b><span>files by {a} today</span></div>' for a, n in IN3)}</div>
<div class=qu><span class=sm3>TODAY'S TOKENS</span>{"".join(f'<div class=r><b>{t}</b><div><b>{f}</b><span>{p} {"photos" if "Photo" in f else ("page" if p == 1 else "pages")} × {c} · {k}{", " + x if x else ""} · {p * c} prints</span></div><em style="background:{ST3[s][0]};color:{ST3[s][1]}">{s}{" " + tm if s == "Collected" else ""}</em></div>' for t, f, p, c, k, x, s, tm in Q3)}</div></div>
<div class=rc><div class=pp><div class=c>SAMPLE PRINT SHOP</div><h3>WEEKLY STATEMENT</h3><div class=c>Sample Office · account A-07<br>Mon 16 Nov to Sat 21 Nov</div><hr>
<div class="r h"><span>DAY</span><span>B/W</span><span>COL</span><span>JOBS</span></div><div class=gr>{"".join(f'<div class=dy><div class=r><span>{d}</span><span>{b}</span><span>{c}</span><span>{j}</span></div><div class=sb><i style="width:{b / MX3 * 100:.1f}%"></i><i class=co style="width:{c / MX3 * 100:.1f}%"></i></div></div>' for d, b, c, j in WK3)}</div><hr>
<div class=lg3><span><i style="background:{TB3}"></i>B/W pages</span><span><i style="background:{MG3}"></i>Colour pages</span></div><hr><div class="r t"><span>Total</span><span>{TW3[0]}</span><span>{TW3[1]}</span><span>{TW3[2]}</span></div><hr>
<div class=ft3><b>Sent on WhatsApp · Sat 21 Nov, 7 PM</b>Every job from the token list.<br>Rates as per your account.</div></div></div></div>''',
TB3, "Run a print shop? DM us", f"background:{YL3};color:{TB3}")
