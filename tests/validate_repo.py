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
    version_path = ROOT / "core/VERSION"
    if not version_path.exists():
        error("Missing core/VERSION")
    else:
        version_text = version_path.read_text(encoding="utf-8").strip()
        if not version_text.startswith("2.0.0"):
            error(f"v2 development branch expected core version 2.0.0*, got {version_text}")

    canon_path = ROOT / "core/canon/active-canon.yaml"
    if not canon_path.exists():
        error("Missing core/canon/active-canon.yaml")
        return

    canon = load_yaml(canon_path) or {}
    rules = canon.get("rules", [])
    active_ids = {rule.get("rule_id") for rule in rules if rule.get("status") == "ACTIVE"}

    required = {
        "PROJECT_NAME_V2_LOCK",
        "PLATFORM_AGNOSTIC_CORE",
        "PLATFORM_ADAPTER_NON_DEGRADATION",
        "IDENTITY_PRIORITY",
        "RETOUCH_PROFILE_RESOLVER",
        "STANDARD_WARDROBE_SELECTION_GATE",
        "SIX_LOGICAL_CORE_ASSETS",
        "STANDARD_IDENTITY_4_PLUS_1_POLICY",
        "AB03_SINGLE_COUPLE_MASTER",
        "PHASE_B_WORK_MODE_GATE",
        "WORK_MODE_DOES_NOT_BYPASS_QC",
        "EXPLICIT_MAKEUP_COMPILATION",
        "LOOK_IDENTITY_DRIFT_PROTECTION",
        "APPROVED_ASSET_AUTHORITY_DELTA",
        "REFERENCE_BINDING_TRUTH",
        "SCOPED_REVISION_POLICY",
        "VIDEO_CORE_PRODUCT",
        "RUNTIME_CAPABILITY_TRUTH_POLICY",
    }
    missing = sorted(required - active_ids)
    if missing:
        error(f"Universal Core missing required v2 ACTIVE rule IDs: {missing}")

    forbidden_active = {
        "SIX_CORE_BOARDS",
    }
    stale = sorted(forbidden_active & active_ids)
    if stale:
        error(f"Superseded v1 rule IDs are still ACTIVE: {stale}")

    highest_rules = ROOT / "core/references/00-highest-rules.md"
    if highest_rules.exists():
        text = highest_rules.read_text(encoding="utf-8", errors="ignore")
        if "Ai 婚纱影像 Pro" not in text:
            error("v2 project name missing from core/references/00-highest-rules.md")
    else:
        error("Missing core/references/00-highest-rules.md")

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

    superseded_phrases = [
        "正式母版目标：8000 × 12000",
        "正式母版目标: 8000 × 12000",
        "六张核心图片资产板",
        "正面上半身锚、六个全身方向",
        "正面上半身锚 + 六个标准全身方向",
    ]
    for path in (ROOT / "core/references").glob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for phrase in superseded_phrases:
            if phrase in text:
                error(f"Superseded v1 phrase found in active core reference: {path.relative_to(ROOT)}: {phrase}")


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

    skill_path = root / "SKILL.md"
    if skill_path.exists():
        skill = skill_path.read_text(encoding="utf-8", errors="ignore")
        required_skill_markers = [
            "display_name: Ai 婚纱影像 Pro",
            "9/9",
            "PHASE_B_WORK_MODE_GATE",
            "Resolver First",
            "Reference Binding Truth",
        ]
        for marker in required_skill_markers:
            if marker not in skill:
                error(f"Xiaoyunque SKILL.md missing v2 marker: {marker}")

    required_reference_markers = {
        "references/phase-a-identity.md": [
            "RETOUCH_PROFILE_RESOLVER",
            "STANDARD_IDENTITY_4_PLUS_1_POLICY",
            "9/9 APPROVED + FROZEN",
        ],
        "references/asset-board-spec.md": [
            "AB01-M01",
            "AB03-C01",
            "WORKING_ARTIFACT",
        ],
        "references/phase-b-creative.md": [
            "PHASE_B_WORK_MODE_GATE",
            "EXPLICIT_MAKEUP_COMPILATION",
            "LOOK_IDENTITY_GATE",
        ],
        "references/prompt-qc.md": [
            "REFERENCE_BINDING_TRUTH",
            "RISK_AWARE_NEGATIVE_COMPILER",
        ],
    }
    for rel, markers in required_reference_markers.items():
        path = root / rel
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="ignore")
            for marker in markers:
                if marker not in text:
                    error(f"Xiaoyunque {rel} missing v2 marker: {marker}")

    banned_v1_phrases = [
        "六张核心图片资产板",
        "正面上半身锚 + 六个标准全身方向",
    ]
    for path in root.rglob("*.md"):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for phrase in banned_v1_phrases:
            if phrase in text:
                error(f"Superseded v1 phrase found in Xiaoyunque runtime: {path.relative_to(ROOT)}: {phrase}")

    banned_suffixes = {".py", ".pyc", ".sh", ".bat", ".cmd", ".ps1", ".exe"}
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in banned_suffixes:
            error(f"Executable/script file is not allowed in Xiaoyunque runtime: {path.relative_to(ROOT)}")


def validate_doubao_history() -> None:
    """v2 does not treat Doubao as a first-class runtime, but keep historical files healthy."""
    root = ROOT / "platforms/doubao/runtime"
    if not root.exists():
        return

    for path in (root / "scripts").glob("*.py") if (root / "scripts").exists() else []:
        try:
            py_compile.compile(str(path), doraise=True)
        except Exception as exc:
            error(f"Historical Doubao Python syntax failed: {path.relative_to(ROOT)}: {exc}")


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
    validate_doubao_history()
    validate_privacy_and_paths()

    if ERRORS:
        print("Repository validation FAILED")
        for item in ERRORS:
            print(f"- {item}")
        return 1

    print("Repository validation PASS")
    print("- v2 project naming and core rule IDs: PASS")
    print("- 4+4+1 identity architecture: PASS")
    print("- retouch/work-mode/look/prompt resolvers: PASS")
    print("- Xiaoyunque no-executable policy: PASS")
    print("- structured syntax and privacy/governance gates: PASS")
    print("- historical Doubao Python syntax (if present): PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
