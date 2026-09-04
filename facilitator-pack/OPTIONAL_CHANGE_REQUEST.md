# Optional Change Request — CR-001

Use only if the core exercise finishes early or you want to demonstrate SDLC re-entry.

## Business change

Workshop organizers now want the feedback form to let an attendee optionally select one topic they found most valuable:

- Kiro Basics
- Agent Design
- Multi-Agent Orchestration
- AWS Deployment

Organizers should see the selected topic alongside the feedback response.

## Facilitation rule

Do not tell participants which agent to call first.

Expected orchestration:

```text
Change Request
  ↓
Business Analyst
  ↓
Requirements update
  ↓
Solution Architect impact assessment
  ↓
Developer
  ↓
QA + Security
  ↓
DevOps plan
  ↓
Human approval
  ↓
Deploy + verify
```

The teaching point is that a change does not bypass the SDLC simply because the code change appears small.
