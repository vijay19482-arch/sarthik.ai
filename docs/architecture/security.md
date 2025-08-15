# Security & Compliance (v1)

- **Secrets**: provider keys only in backend; edge uses **short-lived tickets**.
- **Media**: presigned uploads to storage; API carries **pointers** + checksums.
- **Signing**: artifacts signed; edge/worker run by **digest**, not tag.
- **Sandbox**: plugins execute in microVM/WASM container with resource limits.
- **Identity**: per-device credentials (mTLS/HMAC), per-tenant quotas.
- **Audit**: log every refine step, model choice, and artifact access.
- **PII**: redaction policy in profile; access via short-lived, logged URLs.

