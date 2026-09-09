#!/usr/bin/env python3
import argparse, math, json

def parse_ratio(s):
    if ':' not in s: raise ValueError('ratio must be W:H')
    a,b=s.split(':',1); a=float(a); b=float(b)
    if a<=0 or b<=0: raise ValueError('invalid ratio')
    return a,b

def even(n): return max(2,int(round(n/2))*2)

def main():
    ap=argparse.ArgumentParser(description='按运行时实际长边和目标比例计算尺寸；不假设固定4K像素或8000x12000。')
    ap.add_argument('--ratio',required=True); ap.add_argument('--long-edge',type=int,required=True); ap.add_argument('--orientation',choices=['portrait','landscape','auto'],default='auto')
    a=ap.parse_args(); rw,rh=parse_ratio(a.ratio); L=a.long_edge
    if L<64: raise SystemExit('long-edge too small')
    landscape=rw>=rh
    if a.orientation=='portrait' and landscape: rw,rh=rh,rw
    if a.orientation=='landscape' and not landscape: rw,rh=rh,rw
    if rw>=rh: w=L; h=L*rh/rw
    else: h=L; w=L*rw/rh
    print(json.dumps({"ratio":a.ratio,"requested_long_edge":L,"width":even(w),"height":even(h),"note":"尺寸计算不等于模型原生能力；仍需记录 ACTUAL_NATIVE_SIZE。"},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
