# Deployment Plan — Current Release

Terraform checks expected before apply:

```text
terraform fmt -check
terraform init
terraform validate
terraform plan
```

Expected resource topology:
- DynamoDB PAY_PER_REQUEST table
- Lambda + CloudWatch log group
- API Gateway HTTP API/routes/stage + Lambda permission
- private S3 bucket + public access block + OAC bucket policy
- CloudFront distribution using default CloudFront certificate/domain
- least-privilege IAM role/policy
- frontend S3 objects/config.js

Expected for CR-001: no new AWS service/topology; Lambda artifact and frontend objects change. Actual Terraform add/change/destroy counts depend on current state and must be taken from the live plan.

No Route 53, ACM, EC2, ECS/EKS, RDS, VPC, NAT Gateway, or load balancer expected.

DEVOPS_STATUS: READY_FOR_APPROVAL
