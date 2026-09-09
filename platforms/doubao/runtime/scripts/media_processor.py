#!/usr/bin/env python3
import argparse, shutil, subprocess, json
from pathlib import Path

def ffmpeg(): return shutil.which('ffmpeg')
def main():
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest='cmd',required=True)
    probe=sub.add_parser('probe'); probe.add_argument('input')
    trans=sub.add_parser('transcode'); trans.add_argument('input'); trans.add_argument('output'); trans.add_argument('--codec',default='libx264')
    a=ap.parse_args(); exe=ffmpeg()
    if not exe: raise SystemExit('ffmpeg not found: SCRIPT_CALLABLE=UNKNOWN')
    if a.cmd=='probe':
        r=subprocess.run([exe,'-hide_banner','-i',a.input],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        print(json.dumps({"ffmpeg":"VERIFIED","returncode":r.returncode,"stderr_tail":r.stderr[-4000:]},ensure_ascii=False,indent=2))
    else:
        subprocess.run([exe,'-y','-i',a.input,'-c:v',a.codec,'-c:a','aac',a.output],check=True)
        print(Path(a.output))
if __name__=='__main__': main()
