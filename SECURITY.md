# Security and Privacy Policy

AI Wedding Photography Pro works with workflows that may involve real-person reference images and sensitive project assets. Public collaboration must therefore follow strict data-minimization rules.

## Never commit

Do not commit or upload to this public repository:

- real client photos or private identity references;
- medical, disability, health, biometric, or other sensitive personal information;
- private authorization/consent records;
- API keys, tokens, passwords, cookies, credentials, or private endpoints;
- private project state, customer metadata, or unpublished deliverables;
- proprietary model weights or third-party assets you are not licensed to redistribute.

## Safe examples

Use one of the following for examples and regression fixtures:

- synthetic identities;
- assets created specifically for public testing;
- properly licensed public materials;
- content for which you hold explicit redistribution permission.

## Reporting a security issue

Please do not publish exploitable security or privacy issues with sensitive details in a public issue. Contact the repository maintainer through GitHub first and provide the minimum information needed to reproduce the problem safely.

## Platform adapters

Adapters must not silently upload user assets to unrelated services. Any cross-service transfer, storage boundary, or credential requirement should be explicit and documented.

## Runtime truth

The project distinguishes observed UI features, directly callable Agent tools, and executable local tooling. Never claim that a sensitive action, upload, storage operation, or external call occurred unless it actually succeeded in the current runtime.
