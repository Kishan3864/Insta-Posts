import sys, json, subprocess, asyncio, re
from pathlib import Path
K = Path(__file__).resolve().parent
I = json.load(open(K/"icons.json"))
NOISE = (K/"noise.txt").read_text()
CHECK_JS = (K/"check_text.js").read_text()
GFX_JS = (K/"check_gfx.js").read_text()
LOGO = re.sub(r'^<svg ', '<svg class="lg" ', (K/"logo.svg").read_text())
def ic(n, s=40, c="currentColor", w=2):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round">{I[n]}</svg>'


BASE = """
*{margin:0;padding:0;box-sizing:border-box}
html,body{width:1080px;height:1350px;overflow:hidden}
body{-webkit-font-smoothing:antialiased;position:relative;font-family:var(--f,'Poppins')}
.grain{position:absolute;inset:0;background-image:%s;opacity:.06;pointer-events:none;z-index:50;mix-blend-mode:multiply}
.pg{position:absolute;inset:0;display:flex;flex-direction:column;padding:52px 64px 50px;z-index:2}
.wm{font:500 14px 'Poppins';letter-spacing:1.5px;opacity:.45;line-height:1.4;display:flex;justify-content:space-between}
h1{font-family:var(--h,var(--f,'Poppins'));font-weight:800;letter-spacing:-1.2px;line-height:1.2;margin-top:24px}
.sub{font-size:24px;line-height:1.45;margin-top:12px;font-weight:500}
.vis{flex:1;min-height:0;display:flex;margin:28px 0 24px;position:relative}
.ft{display:flex;align-items:center;justify-content:space-between;height:60px}
.lg{height:44px;width:auto;display:block}
.cta{font:600 20px/1.2 'Poppins';padding:15px 26px;border-radius:40px;display:flex;align-items:center;gap:10px}
.ib{display:flex;align-items:center;justify-content:center;flex:none}
h1,.sub,p,small,b,.bal{text-wrap:balance}
.peep svg{display:block}
""" % NOISE

PEEP_JS = """<script>document.querySelectorAll('.peep svg').forEach(s=>{const g=s.querySelector('g');const b=g.getBBox();
s.setAttribute('viewBox',(b.x-8)+' '+(b.y-8)+' '+(b.width+16)+' '+(b.height+16));s.setAttribute('preserveAspectRatio',s.parentElement.dataset.al||'xMidYMax meet')})</script>"""

_pc = {}
def peep(body, face="Smile", hair="ShortWavy", fh="None", acc="None", w=300, h=400, flip=False, style="", al="xMidYMax meet", fill="#ffffff", stroke="#16162a"):
    props = {"body": body, "face": face, "hair": hair, "facialHair": fh, "accessory": acc, "strokeColor": stroke,
             "backgroundColor": fill, "viewBox": {"x": "-400", "y": "-400", "width": "3000", "height": "3400"}}
    k = json.dumps(props, sort_keys=True)
    if k not in _pc:
        _pc[k] = subprocess.check_output(["node", str(K/"peep.js"), k], cwd=str(K)).decode().replace('style="width:100%;height:100%"', 'style="width:100%;height:100%"')
    return f'<div class=peep data-al="{al}" style="width:{w}px;height:{h}px;flex:none;{"transform:scaleX(-1);" if flip else ""}{style}">{_pc[k]}</div>'

def page(css, head, vis, fg, cta, ctacss, bg="", tagline="", arrow=True, logo_color=None):
    lg = LOGO if not logo_color else LOGO.replace('<svg class="lg" ', f'<svg class="lg" style="color:{logo_color}" ')
    return f"""<!doctype html><html><head><meta charset=utf-8><style>{BASE}{css}</style></head><body>{bg}
<div class=grain></div><div class=pg style="color:{fg}"><div class=wm><span>brightonsolution.com</span><span>{tagline}</span></div>{head}
<div class=vis>{vis}</div><div class=ft>{lg}<div class=cta style="{ctacss}">{cta}{(' '+ic('arrow',20)) if arrow else ''}</div></div></div>{PEEP_JS}</body></html>"""

def phone(inner, w=360, h=720, dark="#111218", radius=54, style=""):
    return f'''<div class=phone style="width:{w}px;height:{h}px;border-radius:{radius}px;padding:12px;background:linear-gradient(145deg,#33353f,{dark});box-shadow:0 0 0 2px #45485a,0 50px 90px rgba(0,0,0,.30),0 16px 28px rgba(0,0,0,.16);flex:none;position:relative;{style}">
<div style="width:100%;height:100%;border-radius:{radius-11}px;overflow:hidden;background:#fff;position:relative;display:flex;flex-direction:column">
<div style="position:absolute;top:12px;left:50%;transform:translateX(-50%);width:92px;height:26px;border-radius:16px;background:#0c0d12;z-index:5"></div>
<div style="display:flex;justify-content:space-between;padding:15px 24px 0;font:600 13px Inter;color:#111;height:42px;flex:none"><span>9:41</span><span>●●● ▮</span></div>{inner}</div></div>'''

def browser(inner, url="yourbusiness.com", style="", bar="#eef1f6"):
    return f'''<div class=browser style="border-radius:20px;overflow:hidden;background:#fff;box-shadow:0 30px 70px rgba(0,0,0,.18);display:flex;flex-direction:column;{style}">
<div style="height:40px;background:{bar};display:flex;align-items:center;gap:7px;padding:0 16px;flex:none"><i style="width:11px;height:11px;border-radius:50%;background:#ff6b5b"></i><i style="width:11px;height:11px;border-radius:50%;background:#ffc542"></i><i style="width:11px;height:11px;border-radius:50%;background:#2fbf71"></i>
<span style="margin-left:12px;flex:1;height:24px;border-radius:12px;background:#fff;font:500 13px/24px Inter;color:#7c8496;padding-left:12px">{url}</span></div>{inner}</div>'''

async def render(P, outdir, keys=None):
    from playwright.async_api import async_playwright
    D = Path(outdir).resolve().parent
    outdir = Path(outdir).name
    keys = keys or list(P)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = await b.new_page(viewport={"width":1080,"height":1350}, device_scale_factor=2)
        (D/outdir).mkdir(exist_ok=True); (D/(outdir+"_html")).mkdir(exist_ok=True)
        bad = {}
        for k in keys:
            f = D/(outdir+"_html")/f"{k}.html"; f.write_text(P[k])
            await pg.goto(f.as_uri()); await pg.wait_for_timeout(350)
            r = await pg.evaluate(CHECK_JS) + await pg.evaluate(GFX_JS)
            if r: bad[k] = r
            await pg.screenshot(path=str(D/outdir/f"{k}.png"))
        await b.close()
    print("ISSUES:", json.dumps(bad, indent=1) if bad else "none")
