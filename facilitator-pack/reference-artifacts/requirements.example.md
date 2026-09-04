# Example Requirements Baseline

## Business objective

Provide a small browser-based proof of concept that lets internal workshop attendees submit anonymous feedback and lets organizers review responses.

## Actors

- Attendee
- Organizer

## Functional requirements

- **FR-001** Attendee can submit feedback from a browser.
- **FR-002** A feedback submission requires a rating that is an integer from 1 through 5.
- **FR-003** Attendee may provide an optional comment up to 500 characters.
- **FR-004** The system generates and stores a UTC submission timestamp.
- **FR-005** Organizer can view stored feedback responses.
- **FR-006** The application does not request or persist attendee PII.

## Non-functional requirements

- **NFR-001** Use AWS serverless services and avoid always-on compute.
- **NFR-002** Backend must use Python.
- **NFR-003** Infrastructure must use Terraform.
- **NFR-004** Static frontend must be served from private S3 through CloudFront.
- **NFR-005** The POC should use least-privilege IAM appropriate to its scope.

## Acceptance criteria

- **AC-001 / FR-001** Given a rating 1–5, submission persists and returns success.
- **AC-002 / FR-002** Rating 0, 6, non-integer, or missing is rejected with a client error.
- **AC-003 / FR-003** Submission succeeds without a comment.
- **AC-004 / FR-003** A comment over 500 characters is rejected.
- **AC-005 / FR-004** Persisted feedback contains a server-generated UTC timestamp.
- **AC-006 / FR-005** Organizer can retrieve submitted feedback.
- **AC-007 / FR-006** Persisted records contain no participant identity field.

## Assumptions

- Single workshop POC.
- Multiple submissions are allowed.
- Organizer view is unauthenticated for the POC.

## Out of scope

Authentication, authorization, multi-workshop management, delete/edit, analytics, notifications, export, file upload, duplicate prevention.

BA_STATUS: PASS
