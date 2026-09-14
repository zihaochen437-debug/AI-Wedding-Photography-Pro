# Changelog

All notable public repository changes are tracked here.

## Unreleased — v2.0.0-dev

> Development source only. v2.0.0 has **not** been compiled or released.

### Project identity

- Renamed the v2+ product to **Ai 婚纱影像 Pro**.
- Retained `Ai 婚纱摄影 Pro` / `AI Wedding Photography Pro` only as v1.x historical or repository compatibility identifiers.
- Made Xiaoyunque the current first-class v2 runtime; historical Doubao source remains for traceability/research.

### Identity and retouching

- Replaced the v1 physical-board interpretation with six logical AB01–AB06 responsibilities.
- Established the formal `4 + 4 + 1` identity-stage output contract: bride M/U/F/D, groom M/U/F/D, and one couple front full-body master.
- Board regions are no longer independent authority assets; temporary intermediates are `WORKING_ARTIFACT` only.
- Added `FRONT_MEDIUM_MASTER_PRIMARY_ANCHOR` and single-slot version replacement rules.
- Added `RETOUCH_PROFILE_RESOLVER`, `RETOUCH_UI_LABEL_IS_NOT_PROMPT`, `STANDARD_ASSET_ALREADY_RETOUCHED`, and a standard wardrobe gate.

### Phase B and Looks

- Added the Phase B work-mode gate: AI_AUTO / PRESET_AUTO / SEMI_AUTO / CUSTOM.
- Separated work mode from Story/Storyboard autonomy.
- Added product-specific asset dependency routing so VF02 does not have to create unused wedding Looks/Scenes.
- Added Look/Makeup resolvers, explicit bride-makeup compilation, Look preflight, makeup presence and identity-drift gates, and edit-first makeup revision.
- Reinforced `PRESET_IS_NOT_LIMIT` across story, wardrobe, makeup, props, scenes and visual design.

### Photography direction

- Integrated a four-layer director system: Story Direction, Performance Direction, Physical/Cinematography Direction, and Model Prompt Compiler.
- Added DIR01 photo director planning, Performance Beat concepts, Eye Life/Listening rules, Blocking Before Framing, Optical Outcome First, motivated camera movement, motion physics, and lighting priority locks.
- Converted shot diversity percentages from an implicit hard rule into an explainable soft warning with creative exceptions.

### Prompt and reference execution

- Added `REFERENCE_BINDING_TRUTH`: internal asset IDs are executable references only when the underlying asset is truly bound to the target model.
- Added resolver-first compilation, risk-aware local negatives, precision-over-verbosity guidance, and explicit retouch/Look/makeup compilation.
- Preserved minimum-sufficient generation references while separating QC/audit references.

### Wedding film production

- Established three product classes: VF01 Dynamic Wedding Imagery, VF02 Creative Narrative Wedding Film, and VF03 Hybrid Narrative Wedding Film.
- Added professional hierarchy `FILM → ACT/CHAPTER → SEQUENCE → SCENE → SHOT → TAKE`.
- Added VP01, VS01, VD01, VC01, VB01, VSL01, VA01 and EDL01 logical film assets.
- Added separate Story and Storyboard approval gates with explicit `STORY_AUTONOMY` / `STORYBOARD_AUTONOMY`.
- Added Script Breakdown, First Frame / End State contracts, continuity gates, limited Take policy and segment-scoped video revision.
- Set final wedding-film master duration to <= 5 minutes.
- Standardized production/EDL planning data at 0.1-second precision while explicitly adapting model timing commands to real model capability and snapping final edits to frame boundaries.
- Added `NO_BGM_BEFORE_PICTURE_LOCK`, `SYNC_SOUND_ONLY`, default post-only VO, formal editing/sound/color/VFX/QC/mastering stages, and reframe+QC rules for platform derivatives.

### Model governance

- Added complete model/service Catalog files for reasoning, image, edit, video, audio and 3D/previs candidates.
- Catalog now explicitly retains Seed2.x, Seedream/SeedEdit, Anycook, 旗舰生图 V2-Pro, Seedance families, Jimeng specialty services, OmniHuman, Seed Audio/voice/music and Seed3D/Xiaoyunque tools.
- Added task-role model routing, runtime-preflight rules, stage-level Model Plan, and controlled commercial A/B test protocol.
- Catalog inclusion is explicitly separated from current Xiaoyunque callability.

### QC and project state

- Expanded Project State Snapshot to nine identity assets, DIR01, film approval/autonomy state, VB01/EDL/Picture Lock and Model Plan.
- Added QC evidence scopes: PASS / FAIL / PARTIAL / NOT_VERIFIED / NOT_APPLICABLE.
- Added targeted repair, retry-budget and manual-takeover policies without inventing unvalidated fixed retry counts.
- Added production ledger and dependency-health semantics for Story, Look, Scene, Shot, Take and post-production changes.

### Research governance

- Added a Professional Skill Source Matrix covering user GitHub Skills, uploaded director/acting prompt references, licenses, adoption status and Canon-promotion rules.
- Added research acknowledgement / license separation to NOTICE, including CC BY 4.0 attribution for the visual-skills research source.

### Validation

- Upgraded repository CI to require v2 naming, nine-image identity architecture, resolver rules, director system, VF01/VF02/VF03 production, Story/Storyboard gates, audio boundaries and complete model-catalog coverage.
- Superseded v1 six-physical-board and separate-angle formal-asset semantics in Canon.
- CI still validates Xiaoyunque no-executable packaging policy and repository privacy/governance rules.

## v1.9.0 — 2026-09-09

### Added

- Bilingual English / Simplified Chinese repository entry documentation.
- Universal Core + Platform Adapter architecture.
- Xiaoyunque and Doubao as current first-class adapters.
- Contribution, security, code-of-conduct, issue, and pull-request guidance.
- Apache License 2.0 and project NOTICE.
- Platform-agnostic Universal Core v1.9.0 source: Active Canon, reference specifications, registries, schemas, and templates.
- Full Xiaoyunque v1.9.0 compact runtime source.
- Doubao v1.9.0 runtime source, including manifests, shared production specifications, registries, schemas, templates, and deterministic Python tooling.
- Cross-platform repository regression validator and GitHub Actions workflow.

### Project governance

- Platform adapters may change execution mechanics but must not silently weaken Universal Core semantics.
- Platform capability claims must distinguish `VERIFIED`, `OBSERVED`, `UNKNOWN`, `UNSUPPORTED`, and `SUPERSEDED`.
- Private client/reference data must never be committed to the public repository.
- Contributions intentionally submitted for inclusion are accepted under Apache-2.0 unless explicitly stated otherwise.
- Platform runtime source is separated from Universal Core so future adapters can be added without redefining the commercial production standard.

### Validation

The v1.9.0 repository validator checked required Universal Core rules, platform leakage, Xiaoyunque no-executable packaging, Doubao deterministic tooling, structured syntax, and public-repository privacy/governance gates.

### Adapter baselines

- Xiaoyunque runtime baseline: v1.9.0
- Doubao runtime baseline: v1.9.0
- Universal Core baseline: v1.9.0
