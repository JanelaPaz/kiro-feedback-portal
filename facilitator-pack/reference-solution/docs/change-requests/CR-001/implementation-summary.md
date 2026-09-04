# CR-001 Implementation Summary

Changed:
- attendee form: required workshop topic input, max 100;
- frontend submission payload: adds `workshopTopic`;
- Lambda validation/persistence: requires topic for new submissions;
- organizer rendering: displays topic, uses `Unknown workshop (legacy)` for old records;
- tests: topic validation, persistence, display-compatible legacy list behavior.

No AWS services or IAM permissions were added.

DEV_STATUS: PASS
