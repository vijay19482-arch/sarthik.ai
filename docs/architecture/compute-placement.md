# Compute Placement Policy

Default policy (profile-driven, not code):
- **STREAM** (CCTV): run heavy work on **edge**; backend provides plan/patches.
- **TASKLET/BATCH** (one-shot images/docs): run on **backend workers**.

Override per use case or per job: `compute_target: "edge" | "worker"`.

Chooser:

| Criterion | Edge | Backend workers |
|---|---|---|
| Latency | sub-100ms, on-prem | >500ms ok |
| Connectivity | flaky/offline | reliable |
| Privacy | media stays on site | upload ptr OK |
| Device | GPU/codec available | central GPU pool |
| Scale | continuous streams | bursty jobs |

**Invariant:** backend always orchestrates; keys/budget/safety live in backend.

