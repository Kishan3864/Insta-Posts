
# ───────── 435 USA · Mobile knife sharpening (market stalls, drop-off and pickup) · SINGLE · Crimson Text + Roboto · stone grey / market teal / cream
# New technique: two-part claim ticket with a perforated tear line (dashed border + punched half-circles via radial-gradient
# masks), and a knife roll where each SVG knife is drawn to its blade length with a ticket tag and status.
SN5 = "#3d4448"; TL5 = "#1f8a86"; CR5 = "#f5efe3"; INK5b = "#1d2326"; MU5b = "#69716f"; OR5 = "#d9822b"
KN5 = [("Chef's knife", 8, "Sharpened"), ("Bread knife", 9, "Serrated · hand file"), ("Paring knife", 3.5, "Sharpened"), ("Santoku", 7, "Chip fixed"), ("Kitchen shears", 0, "Sharpened")]
STOP5 = [("Tue 24 Nov", "Sample Farmers Market", "8 AM to 12 PM", 14, 9), ("Thu 26 Nov", "Sample Library lot", "3 PM to 6 PM", 6, 11), ("Sat 28 Nov", "Sample Town Square", "9 AM to 1 PM", 18, 14)]
def knife5(name, L):
    S = 30; blade = L * S
    if L == 0:
        return f'<svg viewBox="0 0 330 70" style="display:block;width:330px;height:70px"><path d="M10 30 L150 31 L150 39 Z" fill="#c9cfd2" stroke="#7c8589" stroke-width="2"/><path d="M14 42 L150 33 L150 41 Z" fill="#b5bcc0" stroke="#7c8589" stroke-width="2"/><circle cx="150" cy="36" r="5" fill="#7c8589"/><path d="M154 33 L176 18 M154 39 L176 54" stroke="{TL5}" stroke-width="8"/><ellipse cx="196" cy="16" rx="22" ry="11" fill="none" stroke="{TL5}" stroke-width="8"/><ellipse cx="196" cy="56" rx="22" ry="11" fill="none" stroke="{TL5}" stroke-width="8"/></svg>'
    serr = "".join(f'<circle cx="{14 + k * 12}" cy="48" r="3.4" fill="{CR5}"/>' for k in range(int(blade / 12) - 1)) if "Bread" in name else ""
    return f'''<svg viewBox="0 0 {blade + 120} 70" style="display:block;width:{blade + 120}px;height:70px"><path d="M6 42 Q{blade * .3} 16 {blade} 20 V48 H10 Z" fill="#d7dcde" stroke="#7c8589" stroke-width="2"/>{serr}<path d="M{blade * .2} 44 H{blade - 6}" stroke="#fff" stroke-width="2" opacity=".7"/>
<rect x="{blade}" y="18" width="10" height="34" rx="2" fill="#7c8589"/><rect x="{blade + 10}" y="22" width="104" height="26" rx="8" fill="#5a3b2a"/><circle cx="{blade + 40}" cy="35" r="3" fill="#c9b48a"/><circle cx="{blade + 80}" cy="35" r="3" fill="#c9b48a"/></svg>'''
P["p435_knife"] = page(f"""
body{{--f:'Roboto';--h:'Crimson Text';background:{CR5};color:{INK5b};font-variant-numeric:lining-nums}}
.kk{{font:700 16px/1.4 Roboto;letter-spacing:3px;color:{TL5};margin-top:22px}}
h1{{font-family:'Crimson Text';font-weight:700;font-size:64px;line-height:1.18;letter-spacing:-.5px;margin-top:14px}} h1 span{{color:{TL5}}}
.w5{{flex:1;display:flex;flex-direction:column;gap:16px;min-height:0}}
.sm5{{font:700 13px/1.4 Roboto;letter-spacing:2px;color:{MU5b}}}
.tk5{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,.7fr)}}
.tk5>div{{background:#fff;padding:18px 22px;display:flex;flex-direction:column;gap:6px}}
.tk5 .a{{border-radius:18px 0 0 18px;border-right:3px dashed #c9c2b4;-webkit-mask:radial-gradient(circle 14px at 100% 0,transparent 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 14px at 100% 100%,transparent 98%,#000) bottom/100% 51% no-repeat}}
.tk5 .b{{border-radius:0 18px 18px 0;background:{SN5};color:#fff;-webkit-mask:radial-gradient(circle 14px at 0 0,transparent 98%,#000) top/100% 51% no-repeat,radial-gradient(circle 14px at 0 100%,transparent 98%,#000) bottom/100% 51% no-repeat}}.tk5 .b .sm5{{color:#c2c9cc}}
.tk5 .n{{font:700 54px/1.15 'Crimson Text';color:{TL5}}}.tk5 .b .n{{color:#ffd9a8}}.tk5 .r{{display:flex;justify-content:space-between;gap:10px;font:500 18px/1.35 Roboto}}.tk5 .r b{{font-weight:700}}.tk5 .b p{{font:500 17px/1.4 Roboto;color:#dfe4e6}}
.rl5{{flex:1;background:#5a3b2a;border-radius:22px;padding:14px;display:flex;flex-direction:column;gap:10px;min-height:0}}.rl5 .sm5{{color:#e2cdb4;padding:4px 8px 0}}
.rl5 .in{{flex:1;background:#7a5440 repeating-linear-gradient(90deg,transparent 0 46px,rgba(0,0,0,.08) 46px 48px);border-radius:14px;padding:8px 18px;display:flex;flex-direction:column;justify-content:space-around}}
.rl5 .k{{display:flex;align-items:center;gap:16px}}.rl5 .kw{{width:400px;flex:none}}.rl5 .k .tg{{background:{CR5};border-radius:8px;padding:6px 10px;display:flex;flex-direction:column;min-width:200px}}.rl5 .k .tg b{{font:700 17px/1.3 Roboto}}.rl5 .k .tg span{{font:600 14px/1.3 Roboto;color:{TL5}}}.rl5 .k .ln{{font:700 15px/1.2 Roboto;color:#f5e6d0;margin-left:auto}}
.st5{{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}}.st5>div{{background:#fff;border-radius:18px;padding:14px 18px;display:flex;flex-direction:column;gap:4px;border-top:6px solid {TL5}}}.st5 b{{font:700 24px/1.25 'Crimson Text'}}.st5 span{{font:500 16px/1.35 Roboto;color:{MU5b}}}.st5 .ct{{display:flex;gap:14px;margin-top:4px}}.st5 .ct em{{font:700 15px/1.2 Roboto;font-style:normal;border-radius:8px;padding:6px 9px;background:#e1f1f0;color:#14605d}}.st5 .ct em.p{{background:#fbe8d2;color:#8a4d12}}
""", "<div class=kk>MOBILE KNIFE SHARPENING · MARKET STALLS</div><h1>Knife drop-offs on scraps?<br><span>Ticket every knife, every stop.</span></h1>",
f'''<div class=w5><div class=tk5><div class=a><span class=sm5>CLAIM TICKET · CUSTOMER PART · SAMPLE</span><span class=n>#K-0418</span>{"".join(f'<div class=r><span>{a}</span><b>{b}</b></div>' for a, b in [("Name", "Sample Customer"), ("Dropped off", "Tue 24 Nov · Sample Farmers Market"), ("Knives", f"{len(KN5)} in one roll"), ("Pick up", "Sat 28 Nov · Sample Town Square")])}</div>
<div class=b><span class=sm5>STAYS WITH THE KNIVES</span><span class=n>#K-0418</span><p>We text you when they are ready, and again the morning of pickup.</p></div></div>
<div class=rl5><span class=sm5>KNIFE ROLL #K-0418 · DRAWN TO BLADE LENGTH</span><div class=in>{"".join(f'<div class=k><div class=kw>{knife5(n, L)}</div><div class=tg><b>{n}</b><span>{st}</span></div><span class=ln>{f"{L:g} in blade" if L else "pair"}</span></div>' for n, L, st in KN5)}</div></div>
<div class=st5>{"".join(f'<div><span class=sm5>{d.upper()}</span><b>{w}</b><span>{t}</span><div class=ct><em>{dr} drop-offs</em><em class=p>{pu} pickups</em></div></div>' for d, w, t, dr, pu in STOP5)}</div></div>''',
INK5b, "Sharpen knives? DM us", f"background:{TL5};color:#fff")
