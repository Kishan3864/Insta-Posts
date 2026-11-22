# postkit
Setup: `npm i` here; Python needs playwright + Pillow; Chrome at /usr/bin/google-chrome.
In a batch file: `import sys; sys.path.insert(0, "tools/postkit"); from lib import *`, build `P = {key: page(...)}`,
then `asyncio.run(render(P, "work/out"))`. render() writes PNGs and prints ISSUES from check_text.js + check_gfx.js.
Helpers: page(css, head_html, vis_html, fg, cta, ctacss, bg="", tagline="", logo_color=None), phone(inner,w,h),
browser(inner,url), peep(body, face, hair, facialHair, accessory, w, h, flip), ic(name, size).
Icons: icons.json. Add class "free" only for deliberate decoration crossing a box edge.
