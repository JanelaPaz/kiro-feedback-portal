# Example Security Report

## Findings

### SEC-001 — Organizer view has no authentication

Severity: MEDIUM

Status: Accepted POC limitation.

Rationale: Authentication is explicitly out of scope. Do not carry this design unchanged into production.

### SEC-002 — CORS permits public browser access

Severity: LOW / INFO depending implementation.

Status: Accepted for the public POC API if no credentials are used and only in-scope operations are exposed.

## Positive controls

- Private S3 bucket with Block Public Access.
- CloudFront OAC.
- No embedded credentials.
- Table-scoped DynamoDB permissions.
- Server-side rating/comment validation.
- Safe DOM rendering of comments.

No unresolved HIGH or CRITICAL findings.

SECURITY_STATUS: PASS
