# Example Data Model

## Table

Partition key:

```text
id (String UUID)
```

Attributes:

| Field | Type | Required | Ownership |
|---|---|---:|---|
| id | String | Yes | Backend-generated |
| rating | Number | Yes | Validated request |
| comment | String | No | Validated request |
| submittedAt | String ISO-8601 UTC | Yes | Backend-generated |

## Access patterns

1. Insert a feedback response.
2. List feedback responses for organizer review.

For this small POC, a table scan is acceptable because the expected dataset is tiny. A production version should revisit access patterns and indexing.
