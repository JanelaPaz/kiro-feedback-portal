# CR-001 Requirements Impact

## Change summary
Organizers need each new feedback submission to identify the workshop topic.

## New/changed requirements
- Add required `workshopTopic` free-text field for new submissions.
- Trim whitespace and limit to 100 characters.
- Organizer review displays workshop topic.
- Existing records without the new field remain viewable.

## Unaffected requirements
- feedback remains anonymous;
- rating remains required integer 1–5;
- comment remains optional, max 500 characters;
- multiple submissions remain allowed;
- timestamp remains server-generated;
- authentication remains out of scope.

## Acceptance criteria added
- missing/blank topic rejected;
- >100-character topic rejected;
- valid topic is persisted and displayed;
- legacy items without topic still render.

BA_STATUS: PASS
