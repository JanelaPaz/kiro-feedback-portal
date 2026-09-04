# Requirements — Workshop Feedback Portal

## Business objective
Provide a low-cost POC where workshop attendees can anonymously submit feedback and organizers can review submissions across multiple workshop topics.

## Actors
- Attendee — submits feedback.
- Organizer — views submitted feedback.

## Functional requirements
- **FR-001** Attendee can submit anonymous feedback.
- **FR-002** Each new submission must include a workshop topic, 1–100 characters.
- **FR-003** Rating is required and must be an integer from 1 to 5.
- **FR-004** Comment is optional and limited to 500 characters.
- **FR-005** System stores a server-generated submission timestamp.
- **FR-006** Multiple submissions are allowed.
- **FR-007** Organizer can view workshop topic, rating, optional comment, and submitted timestamp.
- **FR-008** Existing records without workshop topic remain viewable after CR-001.
- **FR-009** A health endpoint is available for deployment verification.

## Non-functional requirements
- AWS only; managed/serverless services only within `WORKSHOP_CONSTRAINTS.md`.
- Backend runtime is Python.
- Frontend is static HTML/CSS/JavaScript.
- Infrastructure is Terraform.
- Frontend object storage is private; public delivery may use the generated CloudFront URL.
- Prefer negligible idle cost and least-privilege IAM.
- No custom domain, Route 53, or ACM.

## Acceptance criteria
- **AC-001** Valid topic + rating 1–5 can be submitted and persisted.
- **AC-002** Missing/blank topic is rejected.
- **AC-003** Topic longer than 100 characters is rejected.
- **AC-004** Rating outside 1–5 or non-integer rating is rejected.
- **AC-005** Comment may be omitted.
- **AC-006** Comment over 500 characters is rejected.
- **AC-007** Organizer view returns/display topic, rating, comment when present, and timestamp.
- **AC-008** Legacy records without topic still appear in organizer results.
- **AC-009** No attendee name/email/employee identifier is collected or persisted.
- **AC-010** Deployed frontend and API smoke checks pass.

## Assumptions
- Organizer page authentication is out of scope for the POC.
- Workshop topic is free text; no workshop catalog is maintained.
- Multiple submissions by the same person are acceptable.

## Out of scope
Authentication, authorization by user identity, analytics, moderation, editing/deleting feedback, email, custom domain, production-grade WAF/rate limiting.

BA_STATUS: PASS
