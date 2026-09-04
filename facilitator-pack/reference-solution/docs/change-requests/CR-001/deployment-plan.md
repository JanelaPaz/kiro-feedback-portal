# CR-001 Deployment Plan

Terraform format/init/validate/plan must be executed against the participant environment.

Expected semantic delta:
- Lambda code package changes;
- attendee/organizer frontend objects change;
- no DynamoDB schema/topology change;
- no IAM permission expansion;
- no new AWS service;
- no Route 53/ACM/custom domain.

Actual plan counts must come from the live Terraform plan and must be reviewed before approval.

DEVOPS_STATUS: READY_FOR_APPROVAL
