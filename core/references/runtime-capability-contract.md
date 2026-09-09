# Runtime Capability Truth Contract

Universal Core must not assume that a capability is available merely because a platform UI, vendor model catalog, package file, or documentation mentions it.

## Evidence states

- `VERIFIED`: directly executed and confirmed in the target runtime.
- `OBSERVED`: visible in UI or documentation, but not fully executed by the adapter.
- `UNKNOWN`: insufficient evidence.
- `UNSUPPORTED`: confirmed unavailable.
- `SUPERSEDED`: historical behavior that is no longer active.

## Call surfaces

Adapters should distinguish `UI_AVAILABLE`, `USER_INTERACTIVE`, `AGENT_DIRECT_CALLABLE`, and `SCRIPT_CALLABLE` where relevant. These states do not imply one another.

A platform adapter must degrade honestly: preserve the business requirement, mark execution capability truthfully, and request user interaction or another supported path instead of pretending an action completed.
