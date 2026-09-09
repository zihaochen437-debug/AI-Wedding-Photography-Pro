# Doubao Adapter

This directory contains the Doubao-specific adapter and runtime for AI Wedding Photography Pro.

## Runtime principles

- Preserve Universal Core semantics.
- Separate reasoning models, image models, video models, and deterministic tools by responsibility.
- Runtime model availability must be detected or explicitly marked `UNKNOWN`; ByteDance/Volcengine model existence does not imply availability in every Doubao account.
- Deterministic scripts and media tooling may be used only when runtime execution is actually verified.
- A bundled script/tool is not automatically `SCRIPT_CALLABLE=VERIFIED`.
- Do not expose internal engineering details in user-facing `SKILL.md` sections when Doubao renders them as product details.

## Current adapter focus

- project initialization and asset registries;
- AB01–AB06 production and deterministic board layout;
- reference and prompt manifests;
- commercial photo production;
- VB01 and video workflows;
- timeline validation and media processing when tools are available;
- runtime capability truth, QC, scoped revision, and regeneration.

Platform-specific tooling may exceed Xiaoyunque capabilities, but the adapter must not turn Doubao-only implementation details into hard dependencies of the Universal Core.
