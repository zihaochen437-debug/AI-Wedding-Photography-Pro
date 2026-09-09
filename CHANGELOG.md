# Changelog

All notable public repository changes are tracked here.

## Unreleased

No unreleased public changes yet.

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

The repository validator checks:

- required Universal Core rule coverage;
- platform-only claims do not leak into Universal Core;
- Xiaoyunque runtime contains no executable/script files;
- Doubao runtime includes its expected deterministic tooling;
- Doubao Active Canon implementation targets exist;
- YAML / JSON parsing and Python syntax;
- basic public-repository privacy and governance gates.

### Adapter baselines

- Xiaoyunque runtime baseline: v1.9.0
- Doubao runtime baseline: v1.9.0
- Universal Core baseline: v1.9.0

The Universal Core will be versioned independently from adapter release cadence as the public repository matures.
