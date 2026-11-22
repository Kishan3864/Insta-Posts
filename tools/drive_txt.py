import sys,json,re
from pathlib import Path
def build(d):
    d=Path(d); n,fmt,mkt,cat=d.name.split('_',3)
    imgs=sorted(d.glob('*.jpg'),key=lambda p:int(p.stem))
    title=f"{n} · {fmt} · {mkt} · {cat}.txt"
    fl="SINGLE post: upload 1 image" if fmt=="SINGLE" else f"CAROUSEL: upload all {len(imgs)} images in order"
    links="\n".join(f"Image {i.stem}: https://github.com/Kishan3864/Insta-Posts/blob/main/{d}/{i.name}" for i in imgs)
    body=(d/'post.md').read_text()
    return title, f"{fl}\n\nImages (open link, then Download):\n{links}\n\n{body}"
if __name__=="__main__":
    out={}
    for a in sys.argv[1:]:
        t,c=build(a); out[t]=c
    json.dump(out,open('work/drive.json','w'),ensure_ascii=False,indent=0)
    for t,c in out.items(): print(t,len(c))
