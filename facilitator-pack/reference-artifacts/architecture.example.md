# Example Architecture

## Components

- **CloudFront** — serves the static frontend using its generated distribution URL and default CloudFront certificate; no custom domain is needed.
- **Private S3 bucket** — stores attendee/organizer HTML, CSS, and JavaScript.
- **CloudFront OAC** — permits CloudFront to read S3 without making the bucket public.
- **API Gateway HTTP API** — exposes feedback and health endpoints.
- **Python Lambda** — validates requests and accesses persistence.
- **DynamoDB PAY_PER_REQUEST table** — stores feedback items.
- **CloudWatch Logs** — Lambda operational logs.
- **Terraform** — owns all infrastructure.

## Data flow

### Submit feedback

```text
Browser → API Gateway → Lambda → DynamoDB
```

### Review feedback

```text
Organizer Browser → API Gateway → Lambda → DynamoDB
```

### Load frontend

```text
Browser → CloudFront → private S3
```

## Domain approach

No Route 53, ACM, or custom-domain setup is used. Terraform outputs the generated CloudFront distribution URL for the frontend.

## POC limitations

Organizer review is unauthenticated because authentication is explicitly out of scope. This is not an acceptable default for a production feedback system containing sensitive responses.

ARCH_STATUS: PASS
