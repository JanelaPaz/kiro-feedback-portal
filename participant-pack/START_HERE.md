# Start Here — Multi-Agent Orchestration with SDLC

In this module you will build **one orchestration agent** and use it to coordinate six supplied specialist agents through a complete SDLC.

You are **not** expected to create the BA, Architect, Developer, QA, Security, or DevOps agents. Those are provided.

## Your job

1. Read `CHALLENGE.md`.
2. Read `ORCHESTRATOR_INTEGRATION.md`.
3. Create:
   - `.kiro/agents/sdlc-orchestrator.json`
   - `agent-prompts/sdlc-orchestrator.md`
4. Make your orchestrator use:
   - `SDLC_WORKFLOW.md`
   - `WORKSHOP_CONSTRAINTS.md`
5. Select your orchestrator agent.
6. Use the prompt in `LAUNCH_PROMPT.md`.
7. Answer stakeholder questions only when the BA asks through the orchestrator.
8. Review and explicitly approve deployment only after DevOps prepares the Terraform plan.
9. Later, process the facilitator-provided change request through the same orchestrator.

## Do not

- manually invoke specialists during the SDLC run;
- give the Developer implementation instructions directly;
- bypass failed QA/Security gates;
- deploy before the explicit approval point;
- show yourself the facilitator reference architecture/solution.
