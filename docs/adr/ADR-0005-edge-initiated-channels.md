# ADR-0005: Edge-Initiated Control Channels
Status: **Accepted**

Decision: Backend does not call into edge. Push commands over edge-opened WS/SSE or pub/sub.

Consequences: Firewall/NAT friendly; secure; auditable; consistent.

