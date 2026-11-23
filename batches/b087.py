import sys, random, math, glob, asyncio; sys.path.insert(0, "tools/postkit"); from lib import *
P = {}
def pl(n, w, ws=None): return f"{n:g} {w if n == 1 else (ws or w + 's')}"
for _f in sorted(glob.glob("batches/b087_parts/*.py")):
    exec(open(_f).read())
if __name__ == "__main__":
    pre = sys.argv[1:] or [""]
    keys = [k for k in P if any(k.startswith(p) for p in pre)]
    asyncio.run(render(P, "work/out", keys))
