#!/usr/bin/env python3
import argparse, json, datetime
from pathlib import Path

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('workspace')
    ap.add_argument('--project-id', default=None)
    args=ap.parse_args()
    pid=args.project_id or ('PROJECT-'+datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))
    root=Path(args.workspace)/pid
    for d in ['00_state','01_original_references','02_atomic_assets','03_asset_boards','04_suites','05_photo_shots','06_video','07_revisions','08_final_delivery','99_quarantine']:
        (root/d).mkdir(parents=True, exist_ok=True)
    state={"project_id":pid,"current_phase":"PHASE_A","current_active_task":None,"reference_intake_status":"OPEN",
           "asset_statuses":{f"AB0{i}":"DRAFT" for i in range(1,7)},"current_suite":None,"current_look":None,"current_scene":None,
           "photo_target_count":None,"video_projects":[],"active_generation_refs":[],"last_approved_asset":None,"open_revision":None,
           "model_plan":{},"persistence_status":"PERSISTED"}
    (root/'00_state'/'project_state.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
    print(root)
if __name__=='__main__': main()
