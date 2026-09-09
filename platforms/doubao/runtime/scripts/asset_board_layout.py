#!/usr/bin/env python3
import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(description='非生成式资产板排版：只拼接已批准原子资产，不重画人物。')
    ap.add_argument('manifest',help='JSON: title,width,height,items[{path,label}]')
    ap.add_argument('output')
    a=ap.parse_args()
    try:
        from PIL import Image, ImageDraw, ImageFont, ImageOps
    except Exception as e:
        raise SystemExit('Pillow unavailable: SCRIPT_CALLABLE=UNSUPPORTED')
    m=json.loads(Path(a.manifest).read_text(encoding='utf-8')); W=int(m['width']); H=int(m['height']); items=m.get('items',[])
    if W<256 or H<256 or not items: raise SystemExit('manifest requires width/height/items')
    canvas=Image.new('RGB',(W,H),'white'); draw=ImageDraw.Draw(canvas)
    margin=max(20,int(W*0.03)); title_h=max(80,int(H*0.06)); gap=max(10,int(W*0.01)); label_h=max(42,int(H*0.022))
    draw.text((margin,margin),m.get('title','Ai婚纱摄影资产板'),fill='black')
    n=len(items); cols=2 if n<=6 else 3; rows=(n+cols-1)//cols
    cell_w=(W-2*margin-gap*(cols-1))//cols; avail_h=H-margin-title_h-margin; cell_h=(avail_h-gap*(rows-1))//rows
    for i,it in enumerate(items):
        r=i//cols; c=i%cols; x=margin+c*(cell_w+gap); y=margin+title_h+r*(cell_h+gap)
        img=Image.open(it['path']).convert('RGB'); target=(cell_w, max(20,cell_h-label_h)); fitted=ImageOps.contain(img,target)
        px=x+(cell_w-fitted.width)//2; py=y+(target[1]-fitted.height)//2; canvas.paste(fitted,(px,py))
        label=it.get('label',''); draw.text((x+cell_w//2-len(label)*6,y+cell_h-label_h+8),label,fill='black')
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True); canvas.save(out)
    print(out)
if __name__=='__main__': main()
