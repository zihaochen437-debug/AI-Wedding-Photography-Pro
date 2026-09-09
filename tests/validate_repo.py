#!/usr/bin/env python3
from __future__ import annotations

import json
import py_compile
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
ERRORS: list[str] = []


def error(message: str) -> None:
    ERRORS.append(message)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(f"YAML parse failed: {path.relative_to(ROOT)}: {exc}")
        return None


def validate_structured_files() -> None:
    for path in ROOT.rglob("*.yaml"):
        load_yaml(path)
    for path in ROOT.rglob("*.yml"):
        load_yaml(path)
    for path in ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except Exception as exc:
            error(f"JSON parse failed: {path.relative_to(ROOT)}: {exc}")


def validate_core() -> None:
    canon_path = ROOT / "core/canon/active-canon.yaml"
    if not canon_path.exists():
        error("Missing core/canon/active-canon.yaml")
        return
    canon = load_yaml(canon_path) or {}
    ids = {rule.get("rule_id") for rule in canon.get("rules", [])}
    required = {
        "PLATFORM_AGNOSTIC_CORE",
        "PLATFORM_ADAPTER_NON_DEGRADATION",
        "IDENTITY_PRIORITY",
        "SIX_CORE_BOARDS",
        "APPROVED_ASSET_AUTHORITY_DELTA",
        "SCOPED_REVISION_POLICY",
        "VIDEO_CORE_PRODUCT",
        "RUNTIME_CAPABILITY_TRUTH_POLICY",
    }
    missing = sorted(required - ids)
    if missing:
        error(f"Universal Core missing required rule IDs: {missing}")

    platform_only_phrases = [
        "豆包为当前唯一发行目标",
        "当前版本只针对小云雀",
        "当前版本只发行豆包",
    ]
    for path in (ROOT / "core").rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".yml", ".json"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            for phrase in platform_only_phrases:
                if phrase in text:
                    error(f"Platform-only claim leaked into Universal Core: {path.relative_to(ROOT)}: {phrase}")

    for path in (ROOT / "core/references").glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        if "正式母版目标：8000 × 12000" in text or "正式母版目标: 8000 × 12000" in text:
            error(f"Superseded fixed 8000x12000 master found in active core reference: {path.relative_to(ROOT)}")


def validate_xiaoyunque() -> None:
    root = ROOT / "platforms/xiaoyunque/runtime"
    required = [
        "SKILL.md",
        "references/INDEX.md",
        "references/phase-a-identity.md",
        "references/asset-board-spec.md",
        "references/phase-b-creative.md",
        "references/director-camera.md",
        "references/prompt-qc.md",
        "references/photo-production.md",
        "references/video-production.md",
        "references/xiaoyunque-runtime.md",
    ]
    for rel in required:
        if not (root / rel).exists():
            error(f"Xiaoyunque runtime missing: {rel}")

    banned_suffixes = {".py", ".pyc", ".sh", ".bat", ".cmd", ".ps1", ".exe"}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in banned_suffixes:
            error(f"Executable/script file is not allowed in Xiaoyunque runtime: {path.relative_to(ROOT)}")


def validate_doubao() -> None:
    root = ROOT / "platforms/doubao/runtime"
    required = [
        "SKILL.md",
        "manifest/active-canon.yaml",
        "manifest/build-gates.yaml",
        "references/INDEX.md",
        "references/09-doubao-runtime.md",
        "references/12-script-tool-policy.md",
        "references/08-video-production.md",
    ]
    for rel in required:
        if not (root / rel).exists():
            error(f"Doubao runtime missing: {rel}")

    expected_scripts = {
        "asset_board_layout.py",
        "asset_registry.py",
        "batch_planner.py",
        "media_processor.py",
        "output_size_calculator.py",
        "package_validator.py",
        "project_init.py",
        "prompt_manifest.py",
        "qc_report_generator.py",
        "reference_manifest.py",
        "runtime_probe.py",
        "shot_list_export.py",
        "timeline_validator.py",
    }
    actual_scripts = {p.name for p in (root / "scripts").glob("*.py")} if (root / "scripts").exists() else set()
    missing_scripts = sorted(expected_scripts - actual_scripts)
    if missing_scripts:
        error(f"Doubao runtime missing scripts: {missing_scripts}")

    for path in (root / "scripts").glob("*.py") if (root / "scripts").exists() else []:
        try:
            py_compile.compile(str(path), doraise=True)
        except Exception as exc:
            error(f"Python syntax failed: {path.relative_to(ROOT)}: {exc}")

    canon_path = root / "manifest/active-canon.yaml"
    if canon_path.exists():
        canon = load_yaml(canon_path) or {}
        for rule in canon.get("rules", []):
            implementation = rule.get("implementation")
            if implementation and not (root / implementation).exists():
                error(f"Doubao active rule target missing: {rule.get('rule_id')} -> {implementation}")


def validate_privacy_and_paths() -> None:
    forbidden_names = {".env", "customer-data", "user-assets", "private", "projects"}
    for path in ROOT.rglob("*"):
        rel = path.relative_to(ROOT)
        if any(part in forbidden_names for part in rel.parts):
            error(f"Private/customer path tracked: {rel}")

    required_docs = ["LICENSE", "NOTICE", "README.md", "README.zh-CN.md", "CONTRIBUTING.md", "CONTRIBUTING.zh-CN.md"]
    for rel in required_docs:
        if not (ROOT / rel).exists():
            error(f"Missing repository governance file: {rel}")


def main() -> int:
    validate_structured_files()
    validate_core()
    validate_xiaoyunque()
    validate_doubao()
    validate_privacy_and_paths()

    if ERRORS:
        print("Repository validation FAILED")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print("Repository validation PASS")
    print("- Universal Core required rules: PASS")
    print("- Xiaoyunque no-executable policy: PASS")
    print("- Doubao runtime/script coverage: PASS")
    print("- YAML/JSON/Python syntax: PASS")
    print("- privacy/governance gates: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
