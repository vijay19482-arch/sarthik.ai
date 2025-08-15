# ADR-0004: Agent Refine Loop
Status: **Accepted**

Decision: Edge requests refine with observation; backend returns next step or patch. Optional LLM via `/v1/tools/llm.invoke` with tickets.

Consequences: Edge never holds provider keys; budgets/safety enforced centrally.

