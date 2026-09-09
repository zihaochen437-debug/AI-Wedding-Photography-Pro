# Contributing to AI Wedding Photography Pro

[English](CONTRIBUTING.md) | [简体中文](CONTRIBUTING.zh-CN.md)

Thanks for helping improve AI Wedding Photography Pro.

This project combines photography knowledge, identity-preserving AI generation, wedding styling, prompt engineering, video directing, quality control, and platform adapters. Contributions do not have to be code.

## Contribution areas

You can contribute to:

- Universal Core rules and specifications;
- Xiaoyunque and Doubao adapters;
- identity consistency and reference-routing logic;
- wedding styling, wardrobe, props, lighting, pose, blocking, and camera direction;
- photo and video prompt compilation;
- QC and regression test cases;
- deterministic tooling;
- bilingual documentation;
- safe examples using synthetic or explicitly publishable subjects.

## Core governance rule

Platform adapters may change **how** a capability is executed, but must not silently weaken the Universal Core.

Changes affecting identity, approval gates, user autonomy, asset authority, revision scope, or QC require explicit justification and regression coverage.

## Pull request checklist

Please include:

1. **What changed?**
2. **Why is it needed?**
3. **Which area is affected?** Core / Xiaoyunque / Doubao / tooling / docs / tests.
4. **Does it change Active Canon behavior?** If yes, explain the old and new behavior.
5. **Does it affect identity fidelity, user approval, or personal-feature handling?**
6. **What regression tests or evidence support the change?**
7. **Does it change platform capability assumptions?** Distinguish verified behavior from inference.
8. **Does it introduce new private data, binaries, external services, or credentials?**

## Platform capability evidence

Use explicit evidence states when documenting platform capabilities:

- `VERIFIED` — directly tested and confirmed;
- `OBSERVED` — visible in UI or documentation but not fully executed by the adapter;
- `UNKNOWN` — not yet verified;
- `UNSUPPORTED` — confirmed unavailable;
- `SUPERSEDED` — obsolete behavior retained only for history.

Do not claim that a UI button is Agent-callable without testing it.

## Privacy

Never commit real client photos, private reference images, health/body-sensitive information, private authorization records, API keys, tokens, or confidential project state.

Use synthetic identities or materials you are explicitly allowed to publish.

## Issues

A useful bug report should contain:

- platform and runtime;
- current workflow stage;
- relevant asset IDs or synthetic test inputs;
- expected behavior;
- actual behavior;
- whether the issue is reproducible;
- screenshots or logs with private data removed;
- proposed severity: P0–P4 if known.

We prefer the lifecycle:

`Issue → Root Cause → Rule/Fix → Regression Test`.

## Language

English and Simplified Chinese are both first-class documentation languages. When changing important project documentation, please update both versions when practical.

## Licensing note

The repository has not yet selected its final public license. Until that decision is made, please avoid submitting substantial third-party code or content with incompatible or unclear licensing.
