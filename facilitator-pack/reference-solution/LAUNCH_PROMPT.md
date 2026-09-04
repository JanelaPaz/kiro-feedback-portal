# Launch Prompt

After you have created and selected your `sdlc-orchestrator` agent, start the initial delivery with:

```text
Take BUSINESS_REQUEST.md through the complete SDLC.

Use SDLC_WORKFLOW.md as the authoritative lifecycle and WORKSHOP_CONSTRAINTS.md as the engineering boundary.

Coordinate the supplied specialist agents. Do not perform their work yourself.

Ask me only when the Business Analyst needs stakeholder clarification or when DevOps has completed terraform plan and requires deployment approval.

Do not deploy until I explicitly say APPROVE DEPLOY.

Begin.
```

During the run, you should not manually invoke the specialist agents. Interact with the orchestrator only.

Later, when the facilitator provides a change request, the launch pattern is:

```text
A new approved change request is available at change-requests/CR-001.md.
Process it through the change-request workflow defined in SDLC_WORKFLOW.md.
Do not deploy until I explicitly say APPROVE DEPLOY.
```
