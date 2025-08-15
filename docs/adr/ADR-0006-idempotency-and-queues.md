# ADR-0006: Idempotency & Queues
Status: **Accepted**

Decision: Write endpoints require Idempotency-Key; backend returns 202 and enqueues. At-least-once with idempotent upserts; DLQ present.

Consequences: Burst tolerance; safe retries; predictable scaling.

