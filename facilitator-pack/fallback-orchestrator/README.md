# Facilitator Fallback Orchestrator

Use this only if you need a workshop fallback/demo orchestrator.

To use it in a participant-style project root:

1. Copy `sdlc-orchestrator.json` to `.kiro/agents/sdlc-orchestrator.json`.
2. Copy `sdlc-orchestrator.md` to `agent-prompts/sdlc-orchestrator.md`.
3. Ensure the six supplied specialist agent registrations are also under `.kiro/agents/`.
4. Ensure `BUSINESS_REQUEST.md`, `WORKSHOP_CONSTRAINTS.md`, and `SDLC_WORKFLOW.md` are at the project root.
5. Select/use the `sdlc-orchestrator` custom agent and run `LAUNCH_PROMPT.md`.

This fallback is facilitator-only because participants are expected to reuse the orchestrator from the prior module.
