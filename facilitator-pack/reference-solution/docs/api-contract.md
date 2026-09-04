# API Contract

Base URL: Terraform output `api_url`.

## GET /health
Response `200`:
```json
{"status":"ok"}
```

## POST /feedback
Request:
```json
{
  "workshopTopic": "Multi-Agent Orchestration with SDLC",
  "rating": 5,
  "comment": "Useful workshop"
}
```

Rules:
- `workshopTopic`: required string after trim, max 100 characters.
- `rating`: required integer 1–5.
- `comment`: optional string, max 500 characters after trim.

Success: `201` with persisted object including `id` and `submittedAt`.
Validation failure: `400` with `{ "error": "..." }`.

## GET /feedback
Success `200`:
```json
{
  "items": [
    {
      "id": "uuid",
      "workshopTopic": "Multi-Agent Orchestration with SDLC",
      "rating": 5,
      "comment": "Useful workshop",
      "submittedAt": "2026-09-05T00:00:00Z"
    }
  ]
}
```

Legacy records may omit `workshopTopic` and must still be returned.
