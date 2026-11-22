# usage: python3 tools/drive_done.py 276 277 ...  (marks Drive files done, extends lock 50 min)
import json,sys,datetime
s=json.load(open('state.json'))
s['drive_files_done']=sorted(set(s['drive_files_done'])|{int(a) for a in sys.argv[1:]})
s['lock_until_utc']=(datetime.datetime.now(datetime.UTC)+datetime.timedelta(minutes=50)).strftime('%Y-%m-%dT%H:%M:%SZ')
json.dump(s,open('state.json','w'),indent=1)
print(len(s['drive_files_done']),s['lock_until_utc'])
