# Edge Runtime

**Role:** execute plan locally; wrap outputs; ask backend to refine when needed.

## Edge main loop (concept)
```python
while not done:
    step = plan.next_step()
    result = run_locally(step)   # decode/detect/track/etc.
    wrap_and_emit(result)        # metrics + artifact pointers

    if triggers_refine(result):
        reply = POST /v1/agents/{id}/step {observation,state}
        plan.apply(reply.step or reply.patch)

    if heartbeat_due():
        update = PATCH /v1/streams/{id}/heartbeat {plan_version}
        if update.changed: plan.apply(update.patch)


Connectivity: edge initiates REST + optional WS/SSE control channel. Backend may “push” patches over the edge-opened channel.

