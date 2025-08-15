# Overview (Design Freeze v1)

**Core split:** Backend = **brain** (plan/decide/govern). Edge = **hands** (run/wrap/report).

**Stable APIs (frozen):**
- `/v1/streams` (+ `/slices`, `/heartbeat`) — stream lease & telemetry
- `/v1/agents/{id}/step` — refine/“think” on demand
- `/v1/tools/llm.invoke` — ticketed LLM proxy
- `/v1/jobs` (+ `/v1/jobs/{id}`) — one-shot jobs (e.g., single images)
- `/v1/storage/presign` — presigned upload; API carries **pointers**, not bytes
- `/v1/health` — health/ops

**Artifacts:** Use-case logic ships as **artifacts (digest-signed plugins/images)**; backend/edge run a **generic host** to execute them.

**Profiles:** Use cases are **declarative** under `packages/specs/usecases/<id>/` (profile + plan template + schema + tests).

**Never do:** provider keys on edge, raw media through control API at stream FPS, backend dialing into the edge.

