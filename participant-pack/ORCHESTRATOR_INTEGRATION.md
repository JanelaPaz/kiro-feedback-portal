# Orchestrator Integration Assignment

In this module, **you create the orchestrator agent**. Seven specialist agents are supplied:

- Business Analyst
- Solution Architect
- Frontend Developer
- Backend Developer
- QA Engineer
- Security Reviewer
- DevOps Engineer

Your orchestrator is the eighth agent in the multi-agent system.

## What you must create

```text
.kiro/agents/sdlc-orchestrator.json
agent-prompts/sdlc-orchestrator.md
```

The orchestrator must read and enforce:

- `SDLC_WORKFLOW.md`
- `WORKSHOP_CONSTRAINTS.md`

It must use sub-agent delegation to the supplied specialist registrations.

## Required orchestrator capabilities

Your orchestrator must:

1. distinguish initial delivery from a change request;
2. track and report current SDLC state;
3. invoke only agents allowed by the current state;
4. pass the correct approved artifacts to each agent;
5. support parallel Frontend + Backend implementation, plus DevOps infrastructure implementation;
6. support parallel QA + Security validation;
7. validate terminal status signals before transitioning;
8. route validation findings to the named remediation owner;
9. rerun both validators after code/Terraform remediation;
10. preserve CR-specific audit artifacts;
11. ask the human only for BA stakeholder blockers or deployment approval;
12. never allow Terraform apply until the participant explicitly says `APPROVE DEPLOY`;
13. require live smoke verification before `SDLC_STATUS: COMPLETED`.

## Specialist registrations that must be available

Configure your orchestrator's sub-agent allowlist with:

```text
business-analyst
solution-architect
frontend-developer
backend-developer
qa-engineer
security-reviewer
devops-engineer
```

## Minimum expected routing

```text
BA PASS
→ Architect

Architect PASS
→ Frontend Developer + Backend Developer + DevOps (Terraform implementation)

Frontend PASS + Backend PASS + Infra PASS
→ QA + Security

QA/Security FAIL
→ route each finding to its REMEDIATION_OWNER
→ rerun QA + Security

QA PASS + Security PASS
→ DevOps terraform plan
→ Human approval
→ DevOps terraform apply + smoke tests
```

## Change request routing

```text
CR-XXX
→ Business Analyst impact analysis
→ Solution Architect impact analysis
→ affected implementation workstreams
→ QA + Security regression validation
→ DevOps plan
→ Human approval
→ redeploy + verify
```

If your orchestrator sends a change request directly to an implementation developer, performs specialist work itself, bypasses failed validation, or deploys without approval, it does not meet the workshop objective.
