# Regression validation

`validate_repo.py` protects the public source architecture and the two current first-class adapters.

It checks:

- required Universal Core rule IDs;
- platform-only claims do not leak into Universal Core;
- Xiaoyunque runtime contains no executable/script files;
- Doubao runtime contains its expected deterministic scripts;
- Doubao Active Canon implementation targets exist;
- YAML, JSON and Python syntax;
- basic public-repository privacy/governance gates.

Run locally:

```bash
python -m pip install pyyaml
python tests/validate_repo.py
```
