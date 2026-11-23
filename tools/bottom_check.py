# usage: python3 tools/bottom_check.py key...  → prints bottom of the lowest .vis descendant vs top of .ft (must be < ft top)
import sys, asyncio
from playwright.async_api import async_playwright
async def main(keys):
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg = await b.new_page(viewport={"width":1080,"height":1350})
        for k in keys:
            await pg.goto(f"file:///home/claude/Insta-Posts/work/out_html/{k}.html"); await pg.wait_for_timeout(300)
            r = await pg.evaluate("""()=>{const ft=document.querySelector('.ft').getBoundingClientRect().top;let m=0;document.querySelectorAll('.vis *').forEach(e=>{if(e.closest('.free'))return;const r=e.getBoundingClientRect();if(r.height>0)m=Math.max(m,r.bottom)});return [Math.round(m),Math.round(ft)]}""")
            print(k, "vis bottom", r[0], "footer top", r[1], "OK" if r[0] <= r[1] - 8 else "OVERFLOWS FOOTER")
        await b.close()
asyncio.run(main(sys.argv[1:]))
