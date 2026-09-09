#!/usr/bin/env python3
import argparse, json, csv
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('input'); ap.add_argument('output')
    a=ap.parse_args(); data=json.loads(Path(a.input).read_text(encoding='utf-8')); shots=data.get('shots',data if isinstance(data,list) else [])
    fields=['shot_id','scene','look','sequence','shot_role','shot_size','aspect_ratio','status']
    with Path(a.output).open('w',newline='',encoding='utf-8-sig') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader();
        for s in shots: w.writerow({k:s.get(k,'') for k in fields})
if __name__=='__main__': main()
