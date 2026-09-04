# Architecture — Workshop Feedback Portal

## Decision
Use the smallest approved AWS serverless topology satisfying the requirements.

```text
Browser
  ├── HTTPS → CloudFront → private S3 static frontend
  └── HTTPS → API Gateway HTTP API → Python Lambda → DynamoDB
                                      └→ CloudWatch Logs
```

## Components
- **Amazon S3** — private static frontend assets.
- **Amazon CloudFront** — public HTTPS delivery using the generated distribution domain and Origin Access Control to S3.
- **Amazon API Gateway HTTP API** — HTTP ingress for health, create feedback, and list feedback.
- **AWS Lambda (Python)** — validation and feedback API logic.
- **Amazon DynamoDB PAY_PER_REQUEST** — feedback persistence keyed by `id`.
- **Amazon CloudWatch Logs** — Lambda logs with short retention for the POC.
- **AWS IAM** — Lambda assumes a least-privilege role for required DynamoDB and log actions.
- **Terraform** — provisions all AWS resources and uploads frontend assets.

## Security/POC decisions
- S3 Block Public Access remains enabled.
- CloudFront uses OAC; the S3 bucket is not directly public.
- No AWS credentials are shipped to the frontend.
- No Route 53/ACM/custom domain.
- Organizer endpoint/page is intentionally unauthenticated for the POC and documented as an accepted risk.

## CR-001 impact
No topology change. CR-001 changes the application payload/data model and frontend/backend code only; the existing DynamoDB table can store the additional attribute without a table schema migration.

ARCH_STATUS: PASS
