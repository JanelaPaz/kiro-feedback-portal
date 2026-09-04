# Build the SDLC Orchestrator Agent

In this module, **you create the orchestrator agent**. The six specialist agents are supplied.

Your orchestrator is responsible for executing the process defined in `SDLC_WORKFLOW.md`. It must not invent its own SDLC.

## Supplied specialist agents

- `business-analyst`
- `solution-architect`
- `developer`
- `qa-engineer`
- `security-reviewer`
- `devops-engineer`

Their behaviors are defined in `agent-prompts/` and registered in `.kiro/agents/`.

## Files your orchestrator must use

- `SDLC_WORKFLOW.md` — authoritative lifecycle and change-request workflow
- `WORKSHOP_CONSTRAINTS.md` — global engineering boundaries
- `BUSINESS_REQUEST.md` — initial business input

## Create these two files

```text
.kiro/agents/sdlc-orchestrator.json
agent-prompts/sdlc-orchestrator.md
```

## Minimum orchestrator capabilities

Your orchestrator must:

1. read `SDLC_WORKFLOW.md` before starting or resuming work;
2. read `WORKSHOP_CONSTRAINTS.md` and enforce it globally;
3. use the six supplied specialists via sub-agent delegation;
4. determine whether the work is initial delivery or a change request;
5. track the current lifecycle state;
6. validate required artifacts and PASS/FAIL/BLOCKED statuses;
7. prevent invalid transitions;
8. route specialist failures to the correct remediation owner;
9. support both initial delivery and change-request delivery;
10. ask the human only for stakeholder clarification or deployment approval;
11. stop before Terraform apply until the exact approval phrase is received;
12. never perform specialist work itself.

## Suggested Kiro configuration pattern

Adapt paths as needed for your workspace:

```json
{
  "name": "sdlc-orchestrator",
  "description": "Coordinates the supplied specialist agents through the workshop SDLC.",
  "tools": ["read", "write", "shell", "subagent"],
  "resources": [
    "file://../../SDLC_WORKFLOW.md",
    "file://../../WORKSHOP_CONSTRAINTS.md"
  ],
  "toolsSettings": {
    "subagent": {
      "availableAgents": [
        "business-analyst",
        "solution-architect",
        "developer",
        "qa-engineer",
        "security-reviewer",
        "devops-engineer"
      ]
    }
  },
  "prompt": "file://../../agent-prompts/sdlc-orchestrator.md"
}
```

The configuration above registers the tools/resources. **Your `sdlc-orchestrator.md` prompt must define the orchestration behavior.**

## Acceptance criteria for your orchestrator

A successful orchestrator should demonstrate all of these behaviors:

```text
Initial request → BA first
BA PASS → Architect
Architect PASS → Developer
Developer PASS → QA + Security
Any QA/Security FAIL → Developer remediation → validation rerun
QA PASS + Security PASS → DevOps plan
DevOps plan → human approval stop
APPROVE DEPLOY → deployment → verification

Change request → BA impact analysis first
               → Architect impact analysis
               → Developer
               → QA + Security regression
               → DevOps plan
               → human approval
               → redeploy + verify
```

If your orchestrator sends a change request directly to Developer, performs architecture/security/QA itself, or deploys without approval, it does not meet the workshop objective.
