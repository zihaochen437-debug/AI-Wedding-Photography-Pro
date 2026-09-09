#!/usr/bin/env python3
import argparse, json, math
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('timeline'); ap.add_argument('--tolerance',type=float,default=1e-6)
    a=ap.parse_args(); d=json.loads(Path(a.timeline).read_text(encoding='utf-8')); segs=sorted(d.get('segments',[]),key=lambda x:x['start']); errs=[]
    prev=0.0
    for i,s in enumerate(segs):
        st=float(s['start']); en=float(s['end'])
        if en<=st: errs.append(f'segment {i}: end<=start')
        if abs(st-prev)>a.tolerance: errs.append(f'segment {i}: expected start {prev}, got {st}')
        prev=en
    dur=float(d.get('duration_seconds',prev))
    if abs(prev-dur)>a.tolerance: errs.append(f'final end {prev} != duration {dur}')
    print(json.dumps({"valid":not errs,"errors":errs},ensure_ascii=False,indent=2)); raise SystemExit(1 if errs else 0)
if __name__=='__main__': main()
