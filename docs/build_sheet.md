# Build Sheet

Text to paste while building the topics and flows in the trial. The logic is defined
in [the flow designs](flows.md). Items in `{braces}` are replaced with a variable in
Copilot Studio or Power Automate. Items in `[brackets]` stay as placeholders in a draft.

## Lists

| List | Values |
| --- | --- |
| Staff role | Advisor, Paraplanner, Client Service, Operations, Compliance, Management and Administration |
| Topic | address change, beneficiary change, account transfer, onboarding, complaint, document sharing, identity check, email retention, insurance review, tax documents, data protection, client communication, other |
| Escalation type | Complaint, Privacy incident, Failed identity check, Regulatory question, Process question, Technical question |
| Request category | Policy question, Client reply draft, Knowledge-base draft |

## Topic: Draft a client reply

**Description**

```text
Use when a staff member asks for help writing a reply, email or message to a client
about a firm process. Do not use for complaints or for requests for investment, tax or
legal advice.
```

**Example phrases:** "Draft a reply to a client", "Write an email to a client",
"Help me answer a client about a transfer"

| Order | The agent asks | Answer type | Saved as |
| --- | --- | --- | --- |
| 1 | What is your role? | Staff role list | `staff_role` |
| 2 | Which topic is this about? | Topic list | `topic` |
| 3 | In general terms, what does the client need? Do not include names or account details. | Text | `request_summary` |
| 4 | Are you the client service manager? | Yes or No | `is_manager` |

If `topic` is complaint, the agent says the following and starts "Talk to a person":

```text
Complaints are answered only by Compliance, so I won't draft a reply. I can pass this
to the Compliance officer now. It must be passed on the same business day (POL-08).
```

The agent then writes `draft_text` and `source_ids` from policy, shows the draft and
calls Flow 1. After the flow replies, it says:

```text
Sent for approval. Nothing has been sent to the client. Please acknowledge the
client's message within 1 business day (POL-07).
```

## Topic: Talk to a person

**Description**

```text
Use when a staff member asks for a person, when no policy answers the question, or for
a complaint, privacy incident or failed identity check.
```

**Example phrases:** "Talk to a person", "Escalate this", "I need to report a problem"

| Order | The agent asks | Answer type | Saved as |
| --- | --- | --- | --- |
| 1 | What is your role? | Staff role list | `staff_role` |
| 2 | What kind of issue is it? | Escalation type list | `escalation_type` |
| 3 | Which topic is this about? | Topic list | `topic` |
| 4 | Describe it in general terms. Do not include names or account details. | Text | `question_summary` |

The request category is Policy question unless the escalation started from a client
reply draft.

Replies after Flow 2:

```text
Sent to the {recipient_role}.
```

```text
I couldn't send this. Please contact the {recipient_role} directly today.
```

## Flow 1 messages

**Approval title**

```text
Client reply approval: {topic}
```

**Approval details**

`{approver_role}` is "Client service manager", or "Compliance officer" when the manager
made the request. In the backup approval it is "Compliance officer (backup)".

```text
Approver role: {approver_role}
Requested by role: {staff_role}
Request: {request_summary}
Source policies: {source_ids}
Recipient if approved: {recipient}

Draft:
{draft_text}

Approve only if the draft is accurate, follows policy and gives no advice. You cannot
approve your own request. The first response decides.
```

**Approved email** (sent to the builder's address in the demonstration)

```text
Subject: [DEMO] Reply from Juniper Ridge Financial

{draft_text}
```

**Notices to the requester**

| Result | Subject | Body |
| --- | --- | --- |
| Approved and sent | Approved and sent: {topic} | Your draft was approved and sent. |
| Rejected | Not sent: {topic} | Your draft was rejected. Nothing was sent. Comments: {comments} |
| Timed out | Not sent: {topic} | No one approved your draft in time. Nothing was sent. Submit it again or contact the Compliance officer. |
| Sending failed | Not sent: {topic} | Your draft was approved but could not be sent. Nothing was sent. |

## Flow 2 message

**Subject**

```text
[DEMO] Help desk escalation for {recipient_role}: {escalation_type}{same_day_label}
```

`{same_day_label}` is " (same business day)" for a complaint, privacy incident or
failed identity check, and empty otherwise.

**Body**

```text
From role: {staff_role}
Topic: {topic}

{question_summary}
```

## Flow 3 failure alert

```text
Subject: [DEMO] Help desk log row not saved

A row could not be added to the request log. Request ID: {request_id}. Add it by hand.
```

## Knowledge-base draft

The manager starts with:

```text
Draft a knowledge-base article for these repeated questions: {questions}
```

## Excel log

Upload `dashboard/request_log_template.xlsx` to OneDrive under a working name. It holds
one table, `RequestLog`, with the log columns. Delete its empty first row after the
first real row is added.
