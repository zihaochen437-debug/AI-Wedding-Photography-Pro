#!/usr/bin/env python3
import argparse, json, math

def plan(count):
    if count<=9: return {"directions":"1","note":"1个主要视觉方向为主"}
    if count<=18: return {"directions":"1-2","note":"1-2个方向/Look/Scene"}
    if count<=36: return {"directions":"2-3","note":"多Scene、多Sequence"}
    return {"directions":"multi","note":"完整多套系体系"}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--shots',type=int,required=True); ap.add_argument('--per-batch',type=int,default=1)
    a=ap.parse_args(); batches=math.ceil(a.shots/max(1,a.per_batch)); print(json.dumps({"shots":a.shots,"per_batch":a.per_batch,"batches":batches,"soft_planning":plan(a.shots)},ensure_ascii=False,indent=2))
if __name__=='__main__': main()
