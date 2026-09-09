# Architecture Overview

[English](overview.md) | [简体中文](overview.zh-CN.md)

AI Wedding Photography Pro separates **platform-independent production semantics** from **platform-specific execution**.

## 1. Source Archive

Historical research, experiments, superseded rules, testing notes, and previous runtimes are preserved as design history. Historical material is not automatically active behavior.

## 2. Active Canon

Active Canon is the current authoritative rule set. It resolves conflicts between historical versions and marks obsolete behavior as superseded instead of silently mixing old and new rules.

## 3. Universal Core

The Universal Core defines the business semantics that every first-class adapter must preserve:

- reference intake and role assignment;
- identity authority and couple calibration;
- R0–R4 user-controlled refinement;
- AB01–AB06 asset system;
- styling, wardrobe, props, and scene semantics;
- Scene → Look → Sequence → Shot planning;
- pose, blocking, camera geometry, lighting, and shot intent;
- photo production and approved-shot baseline rules;
- VB01 video planning and photo/video shared identities;
- authoritative-assets + delta prompt compilation;
- scoped revision, regeneration, QC, and delivery;
- asset states, dependencies, invalidation, and audit semantics;
- user autonomy, privacy, and runtime-truth requirements.

## 4. Platform Adapters

Adapters translate Universal Core into a platform's actual capabilities.

An adapter may change:

- file/runtime structure;
- available tools;
- model routing;
- prompt syntax;
- reference attachment mechanics;
- persistence implementation;
- editing/upscale/video execution path.

An adapter must **not** silently change:

- identity fidelity requirements;
- approval gates;
- personal-feature autonomy;
- rejected/quarantined asset rules;
- scoped revision boundaries;
- QC acceptance criteria.

This is the **Platform Adapter Non-Degradation Policy**.

## 5. Current priority adapters

### Xiaoyunque

- Compact declarative Skill runtime.
- No executable scripts in the published Skill package.
- Uses platform-native Agent/image/video tooling when verified.
- Runtime must distinguish UI availability from Agent-callable capability.

### Doubao

- Agent-oriented runtime.
- May use deterministic scripts and media tooling when runtime execution is verified.
- Packaged tooling is not automatically considered executable.
- Runtime capability state must be explicit.

## 6. Capability evidence states

Use:

- `VERIFIED`
- `OBSERVED`
- `UNKNOWN`
- `UNSUPPORTED`
- `SUPERSEDED`

Also distinguish:

- `UI_AVAILABLE`
- `USER_INTERACTIVE`
- `AGENT_DIRECT_CALLABLE`
- `SCRIPT_CALLABLE`

These states must not be inferred from each other.

## 7. Versioning principle

Universal Core evolves independently from individual adapter release cadence. An adapter may lag behind the newest Core while work is in progress, but a release must disclose its Core compatibility level and known gaps.
