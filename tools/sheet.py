# usage: python3 tools/sheet.py out.png key... → contact sheet (each 540x675)
import sys
from PIL import Image
out, keys = sys.argv[1], sys.argv[2:]
cols = min(3, len(keys)); rows = (len(keys) + cols - 1) // cols
S = Image.new("RGB", (cols * 720, rows * 900), "white")
for i, k in enumerate(keys):
    im = Image.open(f"work/out/{k}.png").resize((720, 900), Image.LANCZOS)
    S.paste(im, ((i % cols) * 720, (i // cols) * 900))
S.save(out)
