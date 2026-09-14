# Ai 婚纱影像 Pro

[English](README.md) | [简体中文](README.zh-CN.md)

> **v2.0.0-dev is under active development.** Starting with v2.0.0, the official project name is **Ai 婚纱影像 Pro**. `Ai 婚纱摄影 Pro` is retained only as the historical v1.x product name. The repository name `AI-Wedding-Photography-Pro` remains a technical/historical identifier.

**Ai 婚纱影像 Pro** is a commercial AI production system for identity-preserving wedding photography and wedding filmmaking. It is not a fixed prompt/template library and not a one-shot outfit/background replacement tool.

The system covers real-person identity assets, retouching, bride/groom looks, scenes, photography direction, planning, screenwriting, script breakdown, film direction, performance direction, cinematography, production design, wardrobe/makeup, props, storyboards, prompt compilation, scoped revision, editing, sound, color, QC, and commercial delivery.

## Current development scope

### First-class v2 runtime: Xiaoyunque

v2.0.0 development, runtime validation, and commercial workflow hardening currently focus on **Xiaoyunque**.

Historical Doubao adapters and v1.x releases remain in the repository for traceability and research, but they do not drive current Xiaoyunque runtime decisions.

The Universal Core remains platform-agnostic. Future adapters may change *how* a capability is executed, but must not silently weaken identity fidelity, approval gates, user autonomy, asset authority, scoped revision, audio boundaries, or QC.

## Major v2 changes

### 1. Identity standard: 4 + 4 + 1

Each lead has four formal identity outputs:

- M01 front medium identity master
- U01 upper-body standard board
- F01 full-body standard board
- D01 detail standard board

Bride (4) + groom (4) + one `AB03-C01` couple front full-body master = **9 formal identity-stage outputs**.

AB01/AB02 are logical asset packages. AB03 is the single couple proportion master. Regions inside U/F/D boards are not separate authority assets.

### 2. Retouching is resolved before the first formal identity asset

R0–R4 are user-facing choices, not raw generation prompts. `RETOUCH_PROFILE_RESOLVER` expands them into concrete skin, facial-boundary, hair/beard, teeth, neck/shoulder, hand, posture, body-contour, personal-signature and forbidden-change instructions.

The first formal identity output already reflects the approved retouch baseline; downstream assets must not repeatedly “beautify” the person and cause identity drift.

### 3. Phase B starts with an operating-mode gate

Before creative production, the user chooses:

- AI_AUTO
- PRESET_AUTO
- SEMI_AUTO
- CUSTOM

The work mode changes default decision ownership and interaction density. It does not automatically grant story autonomy, storyboard autonomy, or permission to bypass QC.

### 4. Looks and makeup must be compiled explicitly

Style names are not production prompts. Unless the bride explicitly chooses no-makeup / near-original makeup, the first AB04 must contain executable complexion, brow, eyeshadow, liner, lashes, blush, contour, highlight, lip, intensity, and texture-retention instructions while preserving identity.

### 5. Professional photography direction

Photo production uses `DIR01 → Shot List → Coverage Preflight → Shot`.

The directing system separates Story Direction, Performance Direction, Physical/Cinematography Direction, and the Model Prompt Compiler. Pose, gaze, expression, hands, props, blocking, camera, lighting, physics, and shot diversity are managed as production variables rather than decorative prompt words.

### 6. Three wedding-film product classes

- **VF01 Dynamic Wedding Imagery** — extends approved wedding photographs through time while preserving the approved photo as visual authority.
- **VF02 Creative Narrative Wedding Film** — rebuilds character states, wardrobe, props and scenes around the couple's story or an adapted story concept.
- **VF03 Hybrid Narrative Wedding Film** — weaves the couple-story line and wedding-image line into one motivated narrative.

The final master is **up to 5 minutes**. Story design and the formal storyboard are separate approval gates by default. They may be bypassed only through explicit `STORY_AUTONOMY` / `STORYBOARD_AUTONOMY` authorization.

Film planning, shot cards, audio events and EDL data use **0.1-second planning precision**, while actual model timing instructions are adapted to the real supported timing granularity of the selected runtime model. Final edit points snap to frame boundaries.

Before Picture Lock there is no non-diegetic background score in production material. Shot generation is limited to sync/diegetic sound; VO and background music are post-production layers by default.

## Core philosophy

- **Identity first, creativity second.**
- Bride and groom remain independent identity subjects.
- Approved + frozen assets are semantic authorities.
- Prompt compilation follows `Authoritative Assets + Current Task + Unlocked Variables + Delta + Necessary Constraints`.
- Internal asset IDs are executable references only when the underlying asset is actually bound to the model; otherwise the approved execution state must be expanded into usable prompt/reference input.
- Story, wardrobe, makeup, props, scenes, actions, camera language and sound presets are open-ended starting points, **not capability limits**.
- Revisions are scoped: change the target and preserve other approved decisions.
- Approved Shot / Video becomes the final visual baseline instead of being randomly regenerated for a “final” version.
- UI availability, user-interactive availability, and direct Agent callability are separate facts.

## Model governance

The project preserves a complete candidate catalog while discovering runtime availability dynamically.

The catalog includes Seed2.x reasoning models, Seedream/SeedEdit, Anycook, 旗舰生图 V2-Pro, Seedance 2.5/2.0/legacy variants, Jimeng specialty video services, motion imitation, OmniHuman, Seed Audio/Seed-Music/voice models, Seed3D, Xiaoyunque 3D director stage, and the multitrack editor.

**Catalog inclusion does not mean the current Xiaoyunque account can call the model.** Critical production stages require runtime preflight, and commercial defaults require controlled A/B validation rather than “highest version wins”.

## Architecture

```text
Source Archive / Research
        ↓
Evidence / Professional Skill Ingestion
        ↓
Active Canon
        ↓
Universal Core
        ↓
Xiaoyunque Adapter
        ↓
Compact Runtime
        ↓
Runtime Preflight + Project State
        ↓
Photo / Film Production
```

Repository layout:

```text
core/                 Current platform-agnostic production Canon and contracts
platforms/xiaoyunque/ Current first-class Xiaoyunque adapter/runtime
platforms/doubao/     Historical adapter retained for v1.x traceability/research
docs/                 Architecture, workflow, prompt, and research documentation
tools/                 Development/historical deterministic tools; not shipped in Xiaoyunque runtime
examples/              Public-safe examples only
tests/                 Canon/Core/runtime regression validation
.github/               Contribution, issue, PR, and CI workflows
```

See [Architecture Overview](docs/architecture/overview.md) for details.

## Production scope

Includes, but is not limited to:

- real-person reference intake, grading, role assignment, and minimum-sufficient reference packs;
- R0–R4 retouching with resolver-based compilation;
- nine formal identity-stage outputs, AB04/05 Looks, and AB06 Scenes;
- complete bride/groom styling, wardrobe, accessories, props, and pet identity;
- Scene → Look → Sequence → Shot photo organization;
- DIR01 and Hero / Support / Detail / Safety shot roles;
- performance, blocking, camera geometry, lighting, and motion physics;
- AI-native final-quality photo generation, scoped revision, and approved baselines;
- VF01/VF02/VF03 wedding filmmaking;
- VP01 / VS01 / VD01 / VC01 / VB01 / VSL01 / VA01 / EDL01;
- takes, continuity, segment-level video revision, editing, sound, music, color, VFX/cleanup, and mastering;
- complete model catalog, runtime preflight, Model Plan, and controlled model A/B tests.

## Contributing

Contributions are welcome from wedding photographers and stylists, planners, screenwriters, directors, cinematographers, lighting/performance/production-design specialists, editors, sound/color professionals, and AI/Agent engineers.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

Useful contribution areas include:

- Xiaoyunque capability verification;
- regression cases for identity drift, makeup execution, edit-scope violations, and video continuity;
- professional photography, filmmaking, lighting, performance, script-breakdown, editing, and sound knowledge;
- controlled production tests for current Seedance/Seedream-class models;
- safe public examples using synthetic or explicitly publishable subjects;
- source verification and bilingual documentation.

## Privacy and data safety

**Do not commit real client photos, private reference assets, sensitive medical/body data, authorization records, API keys/tokens, or private project state to this public repository.**

Examples and tests should use synthetic identities, properly licensed public material, or assets with explicit permission to publish.

See [SECURITY.md](SECURITY.md).

## Project status

- Latest stable public release: **v1.9.0** (historical baseline)
- `main`: **v2.0.0-dev / Ai 婚纱影像 Pro**
- Current first-class runtime: **Xiaoyunque**
- v2.0.0 has not been compiled or released yet.

## License

Licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Unless explicitly marked otherwise, contributions intentionally submitted and merged into this repository are provided under the same Apache-2.0 terms.
