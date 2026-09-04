# Data Model

DynamoDB table key:

```text
PK: id (String UUID)
```

Current feedback item:

```json
{
  "id": "uuid",
  "workshopTopic": "Multi-Agent Orchestration with SDLC",
  "rating": 5,
  "comment": "Optional",
  "submittedAt": "2026-09-05T00:00:00Z"
}
```

`comment` may be omitted when blank.

Legacy pre-CR-001 items may not contain `workshopTopic`; readers must tolerate that condition.

No name, email, employee ID, IP address, or other participant identity is intentionally stored.
