#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('output'); ap.add_argument('inputs',nargs='+')
    a=ap.parse_args(); rows=[]
    for f in a.inputs:
        d=json.loads(Path(f).read_text(encoding='utf-8')); rows.append(d)
    report={"records":rows,"summary":{"count":len(rows),"semantic_identity_decision":"must_be_provided_by_agent_or_visual_model"}}
    Path(a.output).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__': main()
