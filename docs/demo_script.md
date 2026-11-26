# Demo Script

A narrated screen recording of about 3 minutes. Items in `[brackets]` are filled in
from test results. Lines that do not match what was built are changed before recording.

## Before recording

- Use invented data only, and send email only to the builder's address.
- Hide account names, email addresses, tenant names, notifications and bookmarks.
- Open each screen in advance: agent, approval request, inbox, Excel log, dashboard.
- Do one full practice run.
- Waiting time may be cut. Say so when it is.

## Script

### 1. Problem (0:00 to 0:25)

**Screen:** README title and diagram, or a title slide.

> This is an AI help desk for Juniper Ridge Financial, a fictional financial planning
> firm. All data is synthetic. Staff at a firm like this spend time searching policies
> and writing routine client replies, and anything sent to a client needs review. I
> built it in Microsoft Copilot Studio and Power Automate.

### 2. Policy answer and limits (0:25 to 1:00)

**Screen:** the agent. Type:

1. `How long do I have to update an address after the signed form and identity check?`
2. `My client has extra cash. Should I tell them to buy an annuity?`

> The agent answers from the firm's policy documents and names its source: here, two
> business days, from POL-03. When someone asks for a recommendation, it declines and
> points them to the advisor.

### 3. Draft, approval and send (1:00 to 1:50)

**Screen:** "Draft a client reply", the approval request, the inbox. Type:

`Draft a reply telling a client how to change their address.`

> The agent drafts a reply with placeholders instead of client details. Nothing is sent
> yet. The approver sees the request, the draft, the source policy and the recipient.
> I approve it, and only now does the email go out. In this demo it goes to my own
> address, and I play both roles. A rejected or unanswered draft is never sent.

### 4. Escalation and log (1:50 to 2:15)

**Screen:** "Talk to a person", the escalation message, the Excel log. Type:

`Can staff accept a gift from a client?`

> No policy covers this, so the agent says so and sends it to a named person. Each
> request adds a row to Excel with a role, topic and outcome, and no message text.

### 5. Test results (2:15 to 2:35)

**Screen:** `eval/results.md`.

> I tested it with 40 questions. It answered [number] of 20 policy questions correctly
> and handled [number] of 20 refusal, escalation and safety cases as expected. The most
> common failure was [failure]. After one change to the instructions, the failed
> questions went from [before] to [after]. I drafted most of the questions with an AI
> assistant, so independent users might find more problems.

### 6. Value (2:35 to 2:48)

**Screen:** dashboard, with the synthetic label visible.

> This dashboard uses mostly synthetic history. My estimate is about 13 hours saved a
> week. That comes from assumed times and volumes, not measurement.

### 7. Governance and close (2:48 to 3:00)

**Screen:** risk assessment.

> Each risk has a planned control and a test. The main limit is [limitation]. The
> documents, tests and configuration are in the GitHub repository.
