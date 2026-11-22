# usage: python3 tools/sheet_img.py out.jpg key1 key2 ...  (contact sheet of work/out PNGs)
import sys
from PIL import Image
ks=sys.argv[2:]; W=540;H=675;c=min(4,len(ks)); r=(len(ks)+c-1)//c
S=Image.new('RGB',(W*c,H*r),'white')
for i,k in enumerate(ks): S.paste(Image.open(f'work/out/{k}.png').convert('RGB').resize((W,H)),((i%c)*W,(i//c)*H))
S.save(sys.argv[1],quality=85)
