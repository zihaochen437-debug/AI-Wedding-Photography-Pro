#!/usr/bin/env python3
import argparse, json
from pathlib import Path
VALID_GRADES={'S','A','B','C','D'}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('manifest'); ap.add_argument('--id',required=True); ap.add_argument('--owner',required=True); ap.add_argument('--role',required=True); ap.add_argument('--grade',required=True); ap.add_argument('--allow-generation',action='store_true'); ap.add_argument('--control',action='append',default=[]); ap.add_argument('--no-transfer',action='append',default=[])
    a=ap.parse_args()
    if a.grade not in VALID_GRADES: raise SystemExit('grade must be S/A/B/C/D')
    p=Path(a.manifest); p.parent.mkdir(parents=True,exist_ok=True); data=json.loads(p.read_text(encoding='utf-8')) if p.exists() else {"references":[]}
    data['references']=[x for x in data['references'] if x.get('reference_id')!=a.id]
    data['references'].append({"reference_id":a.id,"owner":a.owner,"role":a.role,"grade":a.grade,"allowed_for_generation":a.allow_generation,"controls":a.control,"must_not_transfer":a.no_transfer})
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__': main()
