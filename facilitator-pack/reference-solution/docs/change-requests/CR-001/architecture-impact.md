# CR-001 Architecture Impact

## Topology
**No topology change required.**

Unchanged:
- CloudFront
- private S3
- API Gateway
- Python Lambda service boundary
- DynamoDB table
- CloudWatch Logs
- IAM permission set

## Application/API impact
- `POST /feedback` request gains required `workshopTopic`.
- Lambda validates and persists the new attribute.
- attendee form sends the new attribute.
- organizer page displays the attribute and tolerates legacy records.

## Data impact
DynamoDB requires no schema migration because only the primary key is declared. Existing items may omit `workshopTopic`.

## Terraform impact
No new service. Lambda package and S3 frontend objects will change when Terraform hashes/uploads new code/assets.

ARCH_STATUS: PASS
