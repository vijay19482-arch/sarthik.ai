# ADR-0002: Media via Presigned URLs (Pointers, not Bytes)
Status: **Accepted**

Decision: All media uploads go to object storage via `/v1/storage/presign`. APIs carry pointers.

Consequences: Tiny control plane; cheaper bandwidth; uniform AV/retention; no raw bytes over API.

