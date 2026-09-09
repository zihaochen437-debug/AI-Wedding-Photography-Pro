#!/usr/bin/env python3
import argparse, json, datetime
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('output'); ap.add_argument('--task-id',required=True); ap.add_argument('--prompt-file',required=True); ap.add_argument('--model-role',required=True); ap.add_argument('--model-name'); ap.add_argument('--reference',action='append',default=[])
    a=ap.parse_args(); data={"task_id":a.task_id,"prompt":Path(a.prompt_file).read_text(encoding='utf-8'),"references":a.reference,"model_role":a.model_role,"model_name":a.model_name,"parameters":{},"output":{},"created_at":datetime.datetime.now().isoformat()}
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
if __name__=='__main__': main()
