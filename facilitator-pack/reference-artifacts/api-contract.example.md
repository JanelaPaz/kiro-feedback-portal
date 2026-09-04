# Example API Contract

## GET /health

Response 200:

```json
{"status":"ok"}
```

## POST /feedback

Request:

```json
{
  "rating": 5,
  "comment": "Clear and useful"
}
```

Rules:

- rating required integer 1–5,
- comment optional string up to 500 characters.

Response 201:

```json
{
  "id": "...",
  "rating": 5,
  "comment": "Clear and useful",
  "submittedAt": "2026-09-05T00:00:00Z"
}
```

Invalid request: 400.

## GET /feedback

Response 200:

```json
{
  "items": [
    {
      "id": "...",
      "rating": 5,
      "comment": "Clear and useful",
      "submittedAt": "2026-09-05T00:00:00Z"
    }
  ]
}
```
