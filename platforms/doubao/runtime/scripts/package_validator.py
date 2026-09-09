#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('root'); a=ap.parse_args(); root=Path(a.root); errors=[]; warnings=[]
    required=['SKILL.md','manifest/active-canon.yaml','references/INDEX.md','references/08-video-production.md','references/12-script-tool-policy.md']
    for r in required:
        if not (root/r).exists(): errors.append('missing '+r)
    for p in root.rglob('*'):
        try: str(p.relative_to(root)).encode('ascii')
        except UnicodeEncodeError: errors.append('non-ascii path '+str(p.relative_to(root)))
    secret_patterns=[r'AKIA[0-9A-Z]{16}',r'sk-[A-Za-z0-9_-]{20,}',r'(?i)(api[_-]?key|token|password)\s*[:=]\s*["\']?[A-Za-z0-9_\-]{16,}']
    for p in root.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.md','.yaml','.yml','.json','.py','.txt'}:
            txt=p.read_text(encoding='utf-8',errors='ignore')
            for pat in secret_patterns:
                if re.search(pat,txt): errors.append('possible secret '+str(p.relative_to(root)))
    for p in (root/'scripts').glob('*.py') if (root/'scripts').exists() else []:
        try: compile(p.read_text(encoding='utf-8'),str(p),'exec')
        except SyntaxError as e: errors.append(f'python syntax {p.name}: {e}')
    try:
        import yaml
        for p in list(root.rglob('*.yaml'))+list(root.rglob('*.yml')):
            try: yaml.safe_load(p.read_text(encoding='utf-8'))
            except Exception as e: errors.append(f'yaml {p}: {e}')
        ac=yaml.safe_load((root/'manifest/active-canon.yaml').read_text(encoding='utf-8'))
        for rule in ac.get('rules',[]):
            target=rule.get('implementation')
            if target and not (root/target).exists(): errors.append(f'orphan rule {rule.get("rule_id")}: {target}')
    except ImportError:
        warnings.append('PyYAML unavailable: YAML validation UNKNOWN')
    active_text='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in root.rglob('*.md') if 'deprecated' not in str(p))
    if '正式母版目标：8000 × 12000' in active_text: errors.append('fixed 8000x12000 active rule found')
    result={"valid":not errors,"errors":errors,"warnings":warnings}; print(json.dumps(result,ensure_ascii=False,indent=2)); raise SystemExit(1 if errors else 0)
if __name__=='__main__': main()
