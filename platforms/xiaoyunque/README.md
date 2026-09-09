# Xiaoyunque Adapter

This directory contains the Xiaoyunque-specific adapter and runtime for AI Wedding Photography Pro.

## Runtime principles

- Preserve Universal Core semantics.
- Prefer a compact declarative Skill runtime.
- Do not include executable scripts in the published Xiaoyunque package.
- Treat Xiaoyunque UI capabilities, user-interactive controls, and Agent-callable tools as separate evidence states.
- Do not claim a Free Canvas function is Agent-callable until it has been tested.
- Use only the platform tools actually available to the current runtime/account.

## Current adapter focus

- identity-preserving image generation;
- AB01–AB06 asset workflows;
- commercial photo production;
- VB01 video planning;
- person-driven video and photo-to-video when runtime tools are verified;
- natural high-density prompt compilation;
- scoped revision and QC.

Platform-specific packaging may differ from Doubao, but the underlying business semantics must not be weakened.
