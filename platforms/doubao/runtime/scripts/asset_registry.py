#!/usr/bin/env python3
import argparse, json, datetime
from pathlib import Path
VALID_STATES={'DRAFT','UNDER_USER_REVIEW','REVISION_REQUIRED','APPROVED','FROZEN','SUPERSEDED','REJECTED','QUARANTINE'}

def load(p):
    if p.exists(): return json.loads(p.read_text(encoding='utf-8'))
    return {"assets":[]}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('registry'); sub=ap.add_subparsers(dest='cmd',required=True)
    add=sub.add_parser('add'); add.add_argument('--id',required=True); add.add_argument('--type',required=True); add.add_argument('--version',default='1.0'); add.add_argument('--status',default='DRAFT'); add.add_argument('--path'); add.add_argument('--parent',action='append',default=[])
    upd=sub.add_parser('status'); upd.add_argument('--id',required=True); upd.add_argument('--status',required=True)
    args=ap.parse_args(); p=Path(args.registry); p.parent.mkdir(parents=True,exist_ok=True); data=load(p)
    if args.cmd=='add':
        if args.status not in VALID_STATES: raise SystemExit('invalid status')
        if any(x['asset_id']==args.id for x in data['assets']): raise SystemExit('asset exists')
        data['assets'].append({"asset_id":args.id,"asset_type":args.type,"version":args.version,"status":args.status,"validity":"VALID","file_path":args.path,"parent_asset_ids":args.parent,"created_at":datetime.datetime.now().isoformat()})
    else:
        if args.status not in VALID_STATES: raise SystemExit('invalid status')
        item=next((x for x in data['assets'] if x['asset_id']==args.id),None)
        if not item: raise SystemExit('asset not found')
        item['status']=args.status; item['updated_at']=datetime.datetime.now().isoformat()
    p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__': main()
