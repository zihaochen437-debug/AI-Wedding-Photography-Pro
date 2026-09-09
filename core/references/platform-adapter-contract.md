# Platform Adapter Contract

A platform adapter translates Universal Core intent into a platform-specific runtime.

## Non-degradation policy

Adapters may change packaging, model selection, UI interaction, storage, tooling, prompt syntax, or execution mechanics, but must not silently weaken:

- identity fidelity and bride/groom separation;
- user approval gates and user autonomy;
- AB01–AB06 authority boundaries;
- Authoritative Assets + Delta prompt semantics;
- Scoped Revision;
- QC hard-failure rules;
- truthful capability reporting;
- photo/video continuity requirements.

If the target platform cannot directly execute a Core capability, the adapter must keep the requirement visible and mark the execution state `UNKNOWN` or `UNSUPPORTED`, or map it to an explicit user-interactive workflow.
