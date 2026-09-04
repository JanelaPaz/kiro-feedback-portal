# Challenge — Orchestrate a Greenfield SDLC

You have a short business request for a Workshop Feedback Portal.

Your goal is **not simply to build the application**. Your goal is to create an SDLC Orchestrator Agent that can take the request from requirements elicitation through architecture, implementation, independent QA/security validation, Terraform deployment preparation, human authorization, AWS deployment, and post-deployment verification.

The six specialist agents are already supplied. You must create the orchestrator and make it follow `SDLC_WORKFLOW.md`.

## Success means

- the initial business request starts with the Business Analyst;
- stakeholder ambiguity is surfaced rather than invented;
- architecture is produced only after requirements pass;
- implementation follows approved requirements/design;
- QA and Security independently validate the implementation;
- failed validation causes automated remediation routing;
- DevOps runs Terraform validation/plan before deployment;
- Terraform apply waits for explicit human approval;
- the deployed application passes smoke verification;
- a later change request re-enters the SDLC through requirements impact analysis rather than going directly to development.
