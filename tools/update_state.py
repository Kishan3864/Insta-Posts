# usage: python3 tools/update_state.py batches/bNNN_meta.json  → appends posts to state.json + index.csv
import json, sys, re, datetime
from pathlib import Path
R = Path(__file__).resolve().parent.parent
meta = json.load(open(sys.argv[1])); s = json.load(open(R / "state.json"))
for m in meta:
    d = next(p for p in (R / "posts").glob(f"{m['n']:04d}_*"))
    fmt, mk, cat = d.name.split("_", 3)[1:]
    slides = len(list(d.glob("*.jpg")))
    md = (d / "post.md").read_text()
    tags = re.search(r"\n(#[^\n]+)\n\n## Alt", md).group(1)
    s["posts_done"].append(dict(n=m["n"], dir=f"posts/{d.name}", format=fmt, slides=slides, market=mk, category=cat))
    s["market_counts"]["India" if mk == "India" else "Abroad"] += 1
    s["used_categories"].append(cat)
    for k, v in (("recent_palettes", m["palette"]), ("recent_fonts", m["fonts"]), ("recent_layouts", m["layout"]), ("used_hashtag_sets", tags)):
        s[k].append(v)
    s["log"].append(dict(n=m["n"], date=datetime.date.today().isoformat(), format=fmt, market=mk, category=cat, palette=m["palette"], fonts=m["fonts"], layout=m["layout"], dots=m["dots"], phone=m["phone"]))
    with open(R / "index.csv", "a") as f:
        f.write(f"{m['n']},{fmt},{slides},{mk},{cat},https://github.com/Kishan3864/Insta-Posts/tree/main/posts/{d.name}\n")
    s["next_post_no"] = m["n"] + 1
for k, lim in (("recent_palettes", 25), ("recent_fonts", 25), ("recent_layouts", 25), ("log", 30), ("used_hashtag_sets", 60)):
    s[k] = s[k][-lim:]
json.dump(s, open(R / "state.json", "w"), indent=1)
print("next", s["next_post_no"], s["market_counts"])
