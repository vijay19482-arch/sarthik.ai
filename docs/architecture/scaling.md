# Scaling Guide

- **Queues**: Kafka/NATS; partition by tenant/stream for order & scale.
- **Idempotency**: Idempotency-Key on write endpoints; Redis or DB dedupe.
- **Backpressure**: policy signals to edge (drop newest/slow down).
- **Autoscale**: HPA on queue lag & GPU util; 20–30% headroom.
- **Batching**: dynamic GPU batching (8–32 images).
- **Sizing**: workers ≈ ceil(T / R) with headroom; T=jobs/sec, R=steady jobs/sec per worker/GPU.

