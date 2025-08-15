# Control Plane (Backend)

Thin HTTP API + queues. Returns plans/policies, enqueues work, enforces budgets.

## Request lifecycles

### Stream lease (CCTV)


Edge -> POST /v1/streams {adapter_type,usecase_id,capabilities,overrides}
Backend: load profile -> render plan -> create stream_id
Edge <- 200 {stream_id, plan_id, plan_version, plan, policy, agent_id?}


### Slice/heartbeat (metadata only)


Edge -> POST /v1/streams/{id}/slices {ts, metrics, events, artifacts:[ptrs]}
Edge -> PATCH /v1/streams/{id}/heartbeat {plan_version}
Backend <- 304 (no change) | 200 {patch|new_plan_version}


### Refine step


Edge -> POST /v1/agents/{id}/step {observation,state,constraints}
Edge <- 200 {decision: execute|stop|replan, step?, patch?, recursion, policy?}


### One-shot job (image, PDF, etc.)


Client -> POST /v1/storage/presign
Client -> PUT <presigned-url> (to storage)
Client -> POST /v1/jobs {usecase_id, artifact_ptr, compute_target:"worker"| "edge"}
Backend <- 202 {job_id}


**Controllers stay thin:** validate → call policy/engine → respond. Media is always **pointers**.

