# Platform Adapter Contract

A platform adapter translates the Universal Core into a specific platform runtime.

## Non-degradation rule

Adapters may change execution mechanics, packaging, model routing, UI controls, storage, and tool invocation, but they must not silently weaken or remove Universal Core requirements for identity fidelity, user approval, user autonomy, asset authority, scoped revision, QC, or truthful capability reporting.

## Capability truth

Platform capabilities must be recorded as VERIFIED, OBSERVED, UNKNOWN, UNSUPPORTED, or SUPERSEDED. UI presence does not imply Agent-callable support. A bundled executable does not imply runtime executability.

## Current first-class adapters

- Xiaoyunque
- Doubao

Additional adapters may be added without redefining the Universal Core.
