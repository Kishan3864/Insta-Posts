import sys
from PIL import Image
fs=sys.argv[2:]; out=sys.argv[1]; w=540;h=675; n=len(fs); cols=min(n,4); rows=(n+cols-1)//cols
S=Image.new('RGB',(cols*w,rows*h),'white')
for i,f in enumerate(fs): S.paste(Image.open(f).convert('RGB').resize((w,h)),((i%cols)*w,(i//cols)*h))
S.save(out,quality=85)
