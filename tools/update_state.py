# usage: python3 tools/update_state.py entries.json  (list of dicts: n,format,slides,market,category,palette,fonts,layout,dots,phone,tags)
import json,sys,datetime
s=json.load(open('state.json')); E=json.load(open(sys.argv[1]))
for e in E:
    d=f"posts/{e['n']:04d}_{e['format']}_{e['market']}_{e['category']}"
    if any(p['n']==e['n'] for p in s['posts_done']): continue
    s['posts_done'].append(dict(n=e['n'],dir=d,format=e['format'],slides=e['slides'],market=e['market'],category=e['category']))
    s['market_counts']['India' if e['market']=='India' else 'Abroad']+=1
    s['used_categories'].append(e['category'])
    for k,key in [('recent_palettes','palette'),('recent_fonts','fonts'),('recent_layouts','layout')]:
        s[k]=(s[k]+[e[key]])[-25:]
    s['used_hashtag_sets']=(s['used_hashtag_sets']+[' '.join(e['tags'])])[-60:]
    s['log']=(s['log']+[dict(n=e['n'],date=str(datetime.date.today()),format=e['format'],market=e['market'],category=e['category'],palette=e['palette'],fonts=e['fonts'],layout=e['layout'],dots=e['dots'],phone=e['phone'])])[-30:]
    open('index.csv','a').write(f"{e['n']},{e['format']},{e['slides']},{e['market']},{e['category']},https://github.com/Kishan3864/Insta-Posts/tree/main/{d}\n")
    s['next_post_no']=max(s['next_post_no'],e['n']+1)
json.dump(s,open('state.json','w'),indent=1)
print(s['next_post_no'],s['market_counts'])
