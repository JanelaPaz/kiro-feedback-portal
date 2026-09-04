import json
import os
import uuid
from datetime import datetime, timezone

import boto3

TABLE_NAME = os.environ.get("TABLE_NAME", "")
_table = None


def get_table():
    global _table
    if _table is None:
        if not TABLE_NAME:
            raise RuntimeError("TABLE_NAME is not configured")
        _table = boto3.resource("dynamodb").Table(TABLE_NAME)
    return _table


def response(status_code, body):
    return {
        "statusCode": status_code,
        "headers": {"content-type": "application/json"},
        "body": json.dumps(body),
    }


def parse_feedback(body):
    try:
        payload = json.loads(body or "{}")
    except json.JSONDecodeError:
        raise ValueError("Request body must be valid JSON")

    workshop_topic = payload.get("workshopTopic")
    if not isinstance(workshop_topic, str):
        raise ValueError("workshopTopic is required")
    workshop_topic = workshop_topic.strip()
    if not workshop_topic:
        raise ValueError("workshopTopic is required")
    if len(workshop_topic) > 100:
        raise ValueError("workshopTopic must be 100 characters or fewer")

    rating = payload.get("rating")
    if isinstance(rating, bool) or not isinstance(rating, int) or not 1 <= rating <= 5:
        raise ValueError("rating must be an integer from 1 to 5")

    comment = payload.get("comment", "")
    if comment is None:
        comment = ""
    if not isinstance(comment, str):
        raise ValueError("comment must be a string")
    comment = comment.strip()
    if len(comment) > 500:
        raise ValueError("comment must be 500 characters or fewer")

    return workshop_topic, rating, comment


def create_feedback(body, table=None):
    workshop_topic, rating, comment = parse_feedback(body)
    item = {
        "id": str(uuid.uuid4()),
        "workshopTopic": workshop_topic,
        "rating": rating,
        "submittedAt": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    if comment:
        item["comment"] = comment

    (table or get_table()).put_item(Item=item)
    return response(201, item)


def list_feedback(table=None):
    result = (table or get_table()).scan()
    items = result.get("Items", [])
    items.sort(key=lambda item: item.get("submittedAt", ""), reverse=True)
    return response(200, {"items": items})


def handler(event, context):
    request_context = event.get("requestContext", {}).get("http", {})
    method = request_context.get("method", "")
    path = event.get("rawPath", "")

    if method == "GET" and path == "/health":
        return response(200, {"status": "ok"})

    if method == "POST" and path == "/feedback":
        try:
            return create_feedback(event.get("body", ""))
        except ValueError as exc:
            return response(400, {"error": str(exc)})

    if method == "GET" and path == "/feedback":
        return list_feedback()

    return response(404, {"error": "Not found"})
