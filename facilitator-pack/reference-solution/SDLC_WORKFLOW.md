# SDLC Workflow Contract

This file is the authoritative process definition that the participant-created `sdlc-orchestrator` agent must read and enforce.

The orchestrator controls workflow state, delegates to specialist agents, validates gates, routes failures, preserves artifacts, and stops for human approval before deployment. It must not perform specialist work itself.

## Authoritative inputs

- `BUSINESS_REQUEST.md` — stakeholder intent for the initial delivery
- `WORKSHOP_CONSTRAINTS.md` — engineering/platform boundaries
- `SDLC_WORKFLOW.md` — lifecycle and change-management rules
- `change-requests/CR-XXX.md` — future approved change requests, when provided

## Available specialist agents

- `business-analyst`
- `solution-architect`
- `developer`
- `qa-engineer`
- `security-reviewer`
- `devops-engineer`

---

# Entry routing

The orchestrator must first determine the type of work.

## Initial delivery

If there is no completed release and the task is based on `BUSINESS_REQUEST.md`, start at `INTAKE`.

## Change request

If a completed release already exists and the user supplies `change-requests/CR-XXX.md`, start at `CHANGE_REQUEST_INTAKE`.

A change request must **never** be sent directly to the Developer. It must begin with business impact analysis.

---

# Workflow A — Initial delivery

```text
INTAKE
  ↓
REQUIREMENTS
  ↓
DESIGN
  ↓
IMPLEMENTATION
  ↓
VALIDATION
  ↓
DEPLOYMENT_PREPARATION
  ↓
AWAITING_HUMAN_APPROVAL
  ↓
DEPLOYMENT
  ↓
VERIFICATION
  ↓
COMPLETED
```

## INTAKE

Actions:

- confirm `BUSINESS_REQUEST.md`, `WORKSHOP_CONSTRAINTS.md`, and this workflow exist;
- initialize lifecycle state;
- invoke `business-analyst`.

## REQUIREMENTS

Owner: `business-analyst`

Inputs:

- `BUSINESS_REQUEST.md`
- `WORKSHOP_CONSTRAINTS.md`

Expected artifact:

- `docs/requirements.md`

Required terminal status:

```text
BA_STATUS: PASS
```

If the BA returns `BA_STATUS: BLOCKED`:

1. surface only unresolved stakeholder questions to the human;
2. collect stakeholder answers;
3. re-invoke the Business Analyst with those answers;
4. remain in `REQUIREMENTS` until PASS.

Gate checks:

- actors identified;
- functional requirements present;
- applicable non-functional requirements present;
- acceptance criteria are testable;
- assumptions and out-of-scope items documented;
- no unresolved business blocker remains.

## DESIGN

Owner: `solution-architect`

Inputs:

- `WORKSHOP_CONSTRAINTS.md`
- `docs/requirements.md`

Expected artifacts:

- `docs/architecture.md`
- `docs/api-contract.md`
- `docs/data-model.md`

Required terminal status:

```text
ARCH_STATUS: PASS
```

Gate checks:

- all functional requirements are covered;
- only approved AWS services are used;
- solution remains serverless/managed and POC-sized;
- frontend storage is not directly public;
- no Route 53, ACM, or custom domain is introduced;
- backend runtime is Python;
- infrastructure is Terraform;
- no new business requirement is invented.

If a requirements conflict is found, route it to the Business Analyst and rerun design after requirements are corrected.

## IMPLEMENTATION

Owner: `developer`

Inputs:

- `WORKSHOP_CONSTRAINTS.md`
- `docs/requirements.md`
- `docs/architecture.md`
- `docs/api-contract.md`
- `docs/data-model.md`

Expected implementation areas:

```text
frontend/
backend/
tests/
terraform/
```

Expected artifact:

- `docs/implementation-summary.md`

Required terminal status:

```text
DEV_STATUS: PASS
```

Developer may implement and run local checks but must not deploy to AWS.

## VALIDATION

Owners, run independently and preferably in parallel:

- `qa-engineer`
- `security-reviewer`

Expected artifacts:

- `docs/qa-report.md`
- `docs/security-report.md`

Required terminal statuses:

```text
QA_STATUS: PASS
SECURITY_STATUS: PASS
```

### Failure loop

If either validator returns FAIL:

1. aggregate actionable findings;
2. invoke Developer with those findings plus approved artifacts;
3. Developer fixes only what is necessary;
4. after any code or Terraform change, rerun both QA and Security;
5. repeat until both PASS.

The orchestrator may not waive a specialist finding.

## DEPLOYMENT_PREPARATION

Owner: `devops-engineer`

Minimum commands:

```bash
terraform fmt -check
terraform init
terraform validate
terraform plan
```

Expected artifact:

- `docs/deployment-plan.md`

Required terminal status:

```text
DEVOPS_STATUS: READY_FOR_APPROVAL
```

The plan summary must include add/change/destroy counts, important IAM/security changes, region/account when detectable, validation result, and deployment risks.

DevOps must not run `terraform apply` yet.

## AWAITING_HUMAN_APPROVAL

This is the only mandatory human control gate after requirements clarification.

The orchestrator must present the deployment-plan summary and stop.

Exact approval phrase:

```text
APPROVE DEPLOY
```

Without that explicit approval, deployment is forbidden.

## DEPLOYMENT

Owner: `devops-engineer`

After approval only:

- run/apply the approved Terraform plan;
- capture resulting CloudFront and API outputs;
- continue to verification.

## VERIFICATION

Owner: `devops-engineer`

Perform live smoke tests against the deployed environment, including at minimum:

- CloudFront frontend loads;
- health/API endpoint works;
- valid feedback can be submitted;
- invalid rating is rejected;
- organizer feedback retrieval works.

Expected artifact:

- `docs/release-report.md`

Required terminal status:

```text
DEVOPS_STATUS: PASS
```

The orchestrator may mark the workflow `COMPLETED` only after live verification passes.

---

# Workflow B — Change request

A completed system may receive a new business change request.

```text
CHANGE_REQUEST_INTAKE
  ↓
REQUIREMENTS_IMPACT
  ↓
DESIGN_IMPACT
  ↓
IMPLEMENTATION
  ↓
VALIDATION
  ↓
DEPLOYMENT_PREPARATION
  ↓
AWAITING_HUMAN_APPROVAL
  ↓
DEPLOYMENT
  ↓
VERIFICATION
  ↓
COMPLETED
```

For a change request identified as `CR-XXX`, preserve the audit trail under:

```text
docs/change-requests/CR-XXX/
```

Canonical documentation in `docs/` must also be updated to describe the current system after the change.

## CHANGE_REQUEST_INTAKE

Actions:

- verify a completed prior release exists;
- read `change-requests/CR-XXX.md`;
- create/preserve a dedicated change-request artifact directory;
- invoke the Business Analyst.

## REQUIREMENTS_IMPACT

Owner: `business-analyst`

Inputs:

- current `docs/requirements.md`
- `change-requests/CR-XXX.md`
- `WORKSHOP_CONSTRAINTS.md`

Expected outputs:

- `docs/change-requests/CR-XXX/requirements-impact.md`
- updated canonical `docs/requirements.md`

Required status:

```text
BA_STATUS: PASS
```

The BA must identify changed/new acceptance criteria and explicitly state unaffected requirements.

If business clarification is needed, return BLOCKED and ask the human only those questions.

## DESIGN_IMPACT

Owner: `solution-architect`

Inputs:

- updated `docs/requirements.md`
- current `docs/architecture.md`
- current `docs/api-contract.md`
- current `docs/data-model.md`
- `docs/change-requests/CR-XXX/requirements-impact.md`
- `WORKSHOP_CONSTRAINTS.md`

Expected outputs:

- `docs/change-requests/CR-XXX/architecture-impact.md`
- update canonical architecture/API/data-model only where required

Required status:

```text
ARCH_STATUS: PASS
```

The architect must distinguish between:

- topology changes;
- application/API/data changes;
- unchanged components.

## IMPLEMENTATION for a change

Owner: `developer`

Inputs include all approved canonical documents plus the CR impact artifacts.

Expected output:

- implementation changes;
- updated tests;
- `docs/change-requests/CR-XXX/implementation-summary.md`.

Do not bypass the CR scope or silently redesign unrelated components.

## VALIDATION for a change

Run QA and Security independently.

Expected outputs:

- `docs/change-requests/CR-XXX/qa-report.md`
- `docs/change-requests/CR-XXX/security-report.md`

QA must verify:

- the new/changed acceptance criteria;
- regression of previously approved core requirements.

Security must review the changed attack surface plus any affected infrastructure/IAM configuration.

Both must PASS before deployment preparation.

## DEPLOYMENT_PREPARATION for a change

DevOps runs Terraform formatting/validation/plan again and writes:

- `docs/change-requests/CR-XXX/deployment-plan.md`

Status must be `READY_FOR_APPROVAL`.

A change may legitimately produce no new AWS topology. The orchestrator must not require new resources merely because a change request exists.

## HUMAN APPROVAL, DEPLOYMENT, AND VERIFICATION

The same explicit human gate applies:

```text
APPROVE DEPLOY
```

After approval, DevOps deploys the changed release and performs smoke/regression verification.

Expected final CR artifact:

- `docs/change-requests/CR-XXX/release-report.md`

Canonical `docs/release-report.md` should describe the latest deployed release.

---

# Orchestrator control principles

The orchestrator must:

- read this file before starting or resuming work;
- track the current workflow and state;
- invoke only the specialist(s) assigned to the current state;
- verify required artifacts and terminal statuses;
- never perform specialist work itself;
- never skip directly from a change request to implementation;
- never deploy without explicit human approval;
- preserve a traceable artifact history.
