import json
from backend import handler as app


class FakeTable:
    def __init__(self):
        self.items = []

    def put_item(self, Item):
        self.items.append(Item)
        return {"ResponseMetadata": {"HTTPStatusCode": 200}}

    def scan(self):
        return {"Items": list(self.items)}


def body(result):
    return json.loads(result["body"])


def valid_payload(**overrides):
    payload = {
        "workshopTopic": "Multi-Agent Orchestration with SDLC",
        "rating": 5,
        "comment": "Useful",
    }
    payload.update(overrides)
    return payload


def test_valid_feedback_is_created():
    table = FakeTable()
    result = app.create_feedback(json.dumps(valid_payload()), table)
    assert result["statusCode"] == 201
    saved = body(result)
    assert saved["workshopTopic"] == "Multi-Agent Orchestration with SDLC"
    assert saved["rating"] == 5
    assert saved["comment"] == "Useful"
    assert "submittedAt" in saved
    assert set(saved).isdisjoint({"name", "email", "employeeId"})
    assert len(table.items) == 1


def test_workshop_topic_is_required():
    table = FakeTable()
    for value in [None, "", "   "]:
        payload = valid_payload(workshopTopic=value)
        try:
            app.create_feedback(json.dumps(payload), table)
            assert False, f"expected ValueError for {value!r}"
        except ValueError as exc:
            assert "workshopTopic" in str(exc)


def test_workshop_topic_length_is_limited():
    table = FakeTable()
    try:
        app.create_feedback(json.dumps(valid_payload(workshopTopic="x" * 101)), table)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "100" in str(exc)


def test_comment_is_optional():
    table = FakeTable()
    payload = valid_payload()
    payload.pop("comment")
    result = app.create_feedback(json.dumps(payload), table)
    assert result["statusCode"] == 201
    assert "comment" not in body(result)


def test_rating_below_range_is_rejected():
    table = FakeTable()
    try:
        app.create_feedback(json.dumps(valid_payload(rating=0)), table)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "1 to 5" in str(exc)


def test_rating_above_range_is_rejected():
    table = FakeTable()
    try:
        app.create_feedback(json.dumps(valid_payload(rating=6)), table)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "1 to 5" in str(exc)


def test_non_integer_rating_is_rejected():
    table = FakeTable()
    for value in ["5", 4.5, True, None]:
        try:
            app.create_feedback(json.dumps(valid_payload(rating=value)), table)
            assert False, f"expected ValueError for {value!r}"
        except ValueError:
            pass


def test_long_comment_is_rejected():
    table = FakeTable()
    try:
        app.create_feedback(json.dumps(valid_payload(comment="x" * 501)), table)
        assert False, "expected ValueError"
    except ValueError as exc:
        assert "500" in str(exc)


def test_feedback_list_is_newest_first_and_tolerates_legacy_records():
    table = FakeTable()
    table.items = [
        {"id": "1", "rating": 3, "submittedAt": "2026-09-01T00:00:00Z"},
        {
            "id": "2",
            "workshopTopic": "Multi-Agent Orchestration with SDLC",
            "rating": 5,
            "submittedAt": "2026-09-05T00:00:00Z",
        },
    ]
    result = app.list_feedback(table)
    assert result["statusCode"] == 200
    items = body(result)["items"]
    assert [item["id"] for item in items] == ["2", "1"]
    assert "workshopTopic" not in items[1]
