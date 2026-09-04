# Expected Repository Shape

Exact implementation filenames may vary, but a successful submission should contain the orchestrator, supplied specialists, auditable SDLC artifacts, application code, tests, and Terraform.

After the **initial release**, the repository should resemble:

```text
feedback-portal/
├── BUSINESS_REQUEST.md
├── WORKSHOP_CONSTRAINTS.md
├── SDLC_WORKFLOW.md
├── .kiro/
│   └── agents/
│       ├── sdlc-orchestrator.json        # created by participant
│       ├── business-analyst.json
│       ├── solution-architect.json
│       ├── developer.json
│       ├── qa-engineer.json
│       ├── security-reviewer.json
│       └── devops-engineer.json
├── agent-prompts/
│   ├── sdlc-orchestrator.md              # created by participant
│   ├── business-analyst.md
│   ├── solution-architect.md
│   ├── developer.md
│   ├── qa-engineer.md
│   ├── security-reviewer.md
│   └── devops-engineer.md
├── docs/
│   ├── requirements.md
│   ├── architecture.md
│   ├── api-contract.md
│   ├── data-model.md
│   ├── implementation-summary.md
│   ├── qa-report.md
│   ├── security-report.md
│   ├── deployment-plan.md
│   └── release-report.md
├── frontend/
├── backend/
├── tests/
└── terraform/
```

After a change request such as `CR-001`, preserve the audit trail rather than overwriting all evidence:

```text
├── change-requests/
│   └── CR-001.md
└── docs/
    └── change-requests/
        └── CR-001/
            ├── requirements-impact.md
            ├── architecture-impact.md
            ├── implementation-summary.md
            ├── qa-report.md
            ├── security-report.md
            ├── deployment-plan.md
            └── release-report.md
```

The canonical files in `docs/` should represent the **current deployed system**, while `docs/change-requests/CR-001/` records how that change moved through the lifecycle.
