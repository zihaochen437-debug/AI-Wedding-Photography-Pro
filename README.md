# AI Wedding Photography Pro

[English](README.md) | [简体中文](README.zh-CN.md)

**AI Wedding Photography Pro** is an open, platform-agnostic framework for identity-preserving, commercial-grade AI wedding photography and wedding cinematic production.

The project defines a shared production core for real-person identity assets, bride/groom styling, scene design, photography directing, storyboards, prompt compilation, controlled revision, quality control, and photo/video delivery. Platform adapters translate that core into the capabilities and constraints of individual AI platforms without weakening the core requirements.

## Current first-class platform adapters

- **Xiaoyunque** — compact declarative Skill runtime, no executable scripts in the package.
- **Doubao** — Agent-oriented runtime with optional deterministic scripts/tooling when the runtime actually supports them.

More platform adapters can be added over time. A platform adapter may change *how* a capability is executed, but must not silently remove identity, quality, approval, or user-control requirements from the universal core.

## Core philosophy

- **Identity first, creativity second.**
- Bride and groom are independent identities; no face merging, swapping, or drift.
- Approved assets are semantic authorities.
- Prompts describe what is new, unlocked, or changing instead of repeatedly reinterpreting frozen assets.
- Photo and video share the same approved identity, look, and scene assets.
- Natural, real, photorealistic commercial imaging is preferred over template-like AI beautification.
- Revisions are scoped: change only the requested target and preserve approved decisions.

## Architecture

```text
Source Archive / Research
        ↓
Active Canon
        ↓
Universal Core
        ↓
Platform Adapter
        ↓
Platform Runtime Package
```

Repository layout:

```text
core/                 Platform-agnostic production rules and contracts
platforms/            Platform-specific adapters and runtimes
  xiaoyunque/
  doubao/
docs/                 Architecture, workflows, prompt and production documentation
tools/                 Platform-independent deterministic tooling where appropriate
examples/              Public-safe examples only
tests/                 Core and adapter regression tests
.github/               Contribution, issue and PR workflows
```

See [Architecture Overview](docs/architecture/overview.md) for details.

## Production scope

The framework covers:

- reference intake, grading, and role assignment;
- R0–R4 user-controlled refinement strategy;
- AB01–AB06 identity/look/scene asset boards;
- couple proportion and identity continuity;
- styling, wardrobe, accessories, props, and scene systems;
- Scene → Look → Sequence → Shot planning;
- Hero / Support / Detail / Safety Shot coverage;
- blocking, pose, camera geometry, lighting, and photographic language;
- photo production and controlled post-production;
- VB01 video storyboard/timeline assets;
- person-driven wedding video and photo-to-video workflows;
- authoritative-asset + delta prompt compilation;
- scoped revision, regeneration, QC, and delivery.

## Contributing

Contributions are welcome across photography, wedding styling, prompt engineering, visual identity consistency, video directing, platform adapters, tooling, tests, and documentation.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.

Good first contribution areas include:

- platform capability verification;
- regression cases for identity drift and scoped revision;
- photography/lighting/pose knowledge;
- bilingual documentation;
- adapter-specific prompt improvements;
- safe public examples using synthetic or explicitly publishable subjects.

## Privacy and data safety

**Do not commit real client photos, private reference assets, medical/body information, authorization records, API keys, tokens, or private project state to this public repository.**

Use synthetic identities, properly licensed public material, or assets you have explicit permission to publish when creating examples and tests.

See [SECURITY.md](SECURITY.md).

## Project status

The project is in active public development. Xiaoyunque and Doubao are the current priority adapters; the universal core is intended to remain platform-agnostic.

## License

Licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) and [NOTICE](NOTICE).

Unless explicitly marked otherwise, contributions intentionally submitted to this repository are provided under the same Apache-2.0 terms.
