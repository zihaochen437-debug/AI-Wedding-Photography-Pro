# Changelog

All notable public repository changes are tracked here.

## Unreleased

### Added

- Bilingual English / Simplified Chinese repository entry documentation.
- Universal Core + Platform Adapter architecture.
- Xiaoyunque and Doubao as current first-class adapters.
- Contribution, security, code-of-conduct, issue, and pull-request guidance.
- Public source entrypoints for Xiaoyunque v1.9.0 and Doubao v1.9.0 runtimes.

### Project governance

- Platform adapters may change execution mechanics but must not silently weaken Universal Core semantics.
- Platform capability claims must distinguish `VERIFIED`, `OBSERVED`, `UNKNOWN`, `UNSUPPORTED`, and `SUPERSEDED`.
- Private client/reference data must never be committed to the public repository.

## Adapter baselines

- Xiaoyunque runtime baseline: v1.9.0
- Doubao runtime baseline: v1.9.0

The Universal Core will be versioned independently from adapter release cadence as the public repository matures.
