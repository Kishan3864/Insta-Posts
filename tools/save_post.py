# usage: from save_post import save; save(n, fmt, market, category, label, keys, caption, dots, tags, alts, scores)
from pathlib import Path
from PIL import Image
R = Path(__file__).resolve().parent.parent

def save(n, fmt, market, category, label, keys, caption, dots, tags, alts, scores, outdir="work/out"):
    d = R / "posts" / f"{n:04d}_{fmt}_{market}_{category}"
    d.mkdir(parents=True, exist_ok=True)
    for i, k in enumerate(keys, 1):
        Image.open(R / outdir / f"{k}.png").convert("RGB").save(d / f"{i}.jpg", quality=94, subsampling=0)
    N = len(keys)
    fl = "SINGLE post: upload 1 image" if fmt == "SINGLE" else f"CAROUSEL: upload all {N} images in order"
    alt = (f"ALT: {alts[0]}" if N == 1 else "\n".join(f"ALT {i}: {a}" for i, a in enumerate(alts, 1)))
    sc = " · ".join(f"{k} {v}" for k, v in scores.items())
    md = f"""# {n:04d} · {fmt} · {market} · {category}
{fl}
Business: {label}

## Caption
{caption.strip()}
{chr(10).join('.' for _ in range(dots))}
{' '.join(tags)}

## Alt text
{alt}

## QA
ISSUES none (check_text + check_gfx) · contact sheet and 1:1 crops checked
Scores: {sc}
"""
    (d / "post.md").write_text(md)
    return str(d.relative_to(R))
