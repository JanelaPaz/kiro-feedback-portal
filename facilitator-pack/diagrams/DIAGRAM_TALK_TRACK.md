# PPT Diagram Talk Track

All diagrams are supplied as SVG (best for PowerPoint) and PNG.

## 01 — End-to-End SDLC

Use early in the module.

Message:

> The orchestrator owns the lifecycle, not every specialist decision. The only mandatory approval gate is the actual AWS deployment.

## 02 — Agent Responsibilities

Use when introducing the six supplied agents.

Message:

> Multi-agent does not mean six personalities doing the same job. Each agent answers a different question and owns different artifacts.

## 03 — Orchestrator State Machine

Use when explaining what the participant's existing orchestrator must do.

Message:

> The orchestrator is essentially enforcing valid SDLC state transitions. PASS/FAIL is control data.

## 04 — AWS Architecture

Reveal only after the Solution Architect phase.

Message:

> The app is intentionally tiny: static frontend, one API, one Lambda, one DynamoDB table. The frontend uses the generated CloudFront distribution URL; no custom domain is required. Infrastructure complexity stays low so the exercise remains focused on SDLC orchestration.

## 05 — Quality Feedback Loop

Use when QA and Security start.

Message:

> QA and Security can run in parallel because they inspect the same implementation from different domains. If either fails, the orchestrator returns actionable findings to Development and then re-runs validation.

## 06 — Human Deployment Gate

Use immediately before Terraform apply.

Message:

> Automation and governance are not opposites. The workflow can be autonomous while authority over a high-impact action remains human-controlled.
