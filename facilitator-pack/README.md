# Facilitator Pack v5 — Multi-Agent Orchestration with SDLC

This is the facilitator-only package for the Workshop Feedback Portal exercise.

## Key folders

- `reference-solution/` — **complete golden participant submission**, not just application code. It includes the participant-created orchestrator answer, all specialist agents/prompts, SDLC workflow, generated artifacts, application, Terraform, tests, and CR-001 history.
- `reference-artifacts/` — shorter examples useful while facilitating.
- `fallback-orchestrator/` — a ready-to-use orchestrator if a participant's orchestrator is blocked.
- `diagrams/` — PPT-ready PNG/SVG diagrams and talk track.

## Change-request reveal

Give participants `CR-001_CHANGE_REQUEST_HANDOUT.md` only after their first release has reached `SDLC_STATUS: COMPLETED`.

They should place it at:

```text
change-requests/CR-001.md
```

and ask their orchestrator to process it through the change-request workflow in `SDLC_WORKFLOW.md`.

## Reference verification

The golden Python reference tests are expected to pass locally. Terraform still requires a facilitator preflight in an AWS-capable environment:

```bash
terraform fmt -check
terraform init
terraform validate
terraform plan
```
