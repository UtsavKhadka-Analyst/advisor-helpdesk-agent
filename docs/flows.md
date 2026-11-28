# Flow Designs

> Juniper Ridge Financial is a fictional firm. Flows 1 and 3 have been built and tested
> by manual runs, except for the parts listed as not built or not tested. Flow 2 is an
> untested design.

## Shared rules

- **Fail closed:** if a step fails or no one approves, nothing is sent to a client.
- **No self-approval:** the person who made a request cannot approve it.
- **Minimum data:** the log holds fixed values only, never message text or personal
  details.
- **Demonstration:** one person plays every role. All messages go to the builder's own
  address, set inside the flow and never collected in chat.
- **Respond early:** a flow called by the agent replies to it before any long wait.
  Microsoft documents a limit of about 100 seconds for this reply.

## Flow 1: Client reply approval

**Trigger:** the agent calls the flow from the "Draft a client reply" topic.

**Inputs:** staff role, topic, general description of the request, draft with
placeholders, source policy IDs, and whether the requester is the client service
manager.

```text
Agent calls flow
  -> Set topic (unlisted values become "other")
  -> Choose first approver
  -> Reply to agent: "Sent for approval. Nothing has been sent to the client."
  -> Wait for approval
       Approved  -> send the approved draft -> tell requester
       Rejected  -> send comments to requester
       No answer -> backup approver, or end as timed out
  -> Log the request (Flow 3)
```

### Approver

| Case | First approver | If no answer in 1 day | If still no answer after another day |
| --- | --- | --- | --- |
| Normal request | Client service manager | Compliance officer | End: timed out |
| Manager made the request | Compliance officer | End: timed out | Not applicable |

The approval request shows the request description, the draft, the source policy IDs
and the recipient. The first response decides.

### Results

| Result | Email to client | Requester is told | `approval_result` | `minutes_saved` |
| --- | --- | --- | --- | --- |
| Approved | Sent, unchanged | It was sent | approved | 8 |
| Rejected | Not sent | Approver comments | rejected | 0 |
| Timed out | Not sent | No one approved it | timed out | 0 |
| Approved, sending fails | Not sent | Sending failed | send failed | 0 |

For a client reply draft, `outcome` is `answered`, or `failed` if sending fails.

The requester acknowledges the client within 1 business day under POL-07 while the
full reply waits for approval.

The demonstration sends drafts with their placeholders. A real deployment would fill
them from the client record before approval, so the approver sees the final text.

Complaints never enter this flow. They go to Flow 2.

### Build and test results

Built as a Power Automate cloud flow in the same solution as Flow 3, which it calls as
a child flow. It replies to its caller in the first step. A topic outside the list
becomes `other`. The backup approval runs only when the first approval has no answer
and the requester is not the manager.

Approval timeouts are set to 2 minutes for testing. The design value is 1 day.

Tested by manual runs on 2026-11-27 and 2026-11-28:

| Test | Result |
| --- | --- |
| First approver approves | Email sent after approval, requester told, row `approved`, 8 minutes |
| Approver rejects | Requester told with a comments field, row `rejected`, 0 minutes |
| One approval unanswered, before the backup was added | No client email, requester told, row `timed out`, 0 minutes |
| First approval unanswered, backup approves | Email sent, requester told, row `approved`, 8 minutes |
| Manager's own request unanswered | One approval, to the Compliance officer; no client email; row `timed out` |
| Neither approver answers | Row `timed out`, 0 minutes |

Not yet built: the notice and log row when an approved email fails to send. Not yet
tested: calls from the agent and the 1-day timeouts.

Known limitations:

- One person plays every role, so the demonstration does not enforce separate
  approvers.
- The row is logged after the requester notice, so a failed notice would leave no row.
- The flow's run history keeps the original inputs.

## Flow 2: Escalation

**Trigger:** the agent calls the flow from the "Talk to a person" topic.

**Inputs:** staff role, request category, topic, escalation type and the question in
general terms.

```text
Agent calls flow
  -> Choose recipient from escalation type
  -> Send message to recipient
       Success -> reply to agent: who received it
       Failure -> reply to agent: contact that person directly
  -> Log the request (Flow 3)
```

| Escalation type | Recipient | Marked same day |
| --- | --- | --- |
| Complaint | Compliance officer | Yes |
| Privacy incident | Compliance officer | Yes |
| Failed identity check | Compliance officer | Yes |
| Regulatory question | Compliance officer | No |
| Process question | Operations lead | No |
| Technical question | Operations lead | No |

An unrecognised type goes to the Compliance officer. The question text appears in the
message to the recipient but not in the log.

`outcome` is `escalated` and `minutes_saved` is 3. If sending fails, `outcome` is
`failed` and `minutes_saved` is 0.

## Flow 3: Request logging

**Trigger:** called by Flow 1 and Flow 2, and by the agent after a policy answer, a
declined request or a knowledge-base draft.

```text
Receive values
  -> Replace any value outside the allowed list
  -> Add request ID and date
  -> Add one row to the Excel table
       Failure -> retry, then email the owner
```

One request produces one row, written when its outcome is known. A policy question
that is escalated is logged once, by Flow 2.

A value outside the allowed list is replaced before the row is written, so the
original text never reaches the log. Matching is exact, including capitals.

| Value | Replacement |
| --- | --- |
| `topic` | other |
| `staff_role`, `category`, `outcome`, `approval_result` | unknown |
| `minutes_saved` other than 0, 3, 6, 8 or 45 | 0 |

### Build and test results

Built as a Power Automate cloud flow in a solution, so that other flows can call it
as a child flow. The `date` column uses local time. The failure alert runs when the
Excel step fails or times out, and relies on the step's default retry setting.

Tested by manual runs on 2026-11-27:

| Test | Result |
| --- | --- |
| Allowed values | One row with the values as entered and a new request ID |
| Values outside the lists | Replaced as in the table above |
| Workbook deleted, then run | Alert email received with the request ID |
| Successful run after adding the alert | Row added and alert skipped |

Calls from Flow 1 have since added rows successfully. Not yet tested: calls from the
agent, retry behaviour and the timeout path.

Known limitation: replaced values are kept out of the log, but the flow's run history
still shows the original inputs.

## Excel log layout

One table in a workbook in OneDrive.

| Column | Allowed values |
| --- | --- |
| `request_id` | Unique ID set by the flow |
| `date` | Date the row is written, YYYY-MM-DD |
| `staff_role` | Advisor, Paraplanner, Client Service, Operations, Compliance, Management and Administration |
| `category` | Policy question, Client reply draft, Knowledge-base draft |
| `topic` | address change, beneficiary change, account transfer, onboarding, complaint, document sharing, identity check, email retention, insurance review, tax documents, data protection, client communication, other |
| `outcome` | answered, escalated, declined, failed |
| `approval_result` | approved, rejected, timed out, send failed, not required |
| `minutes_saved` | Estimate from the table below |

| Request | `minutes_saved` |
| --- | --- |
| Policy question answered | 6 |
| Client reply draft approved | 8 |
| Escalation delivered | 3 |
| Knowledge-base draft | 45 |
| Declined, rejected, timed out or failed | 0 |

The values come from [the use-case intake](governance/use_case_intake.md) and are
estimates, not measurements.

## Test cases

| Test | Expected result | Risk |
| --- | --- | --- |
| Approve a draft | One email and one row | R6 |
| Reject a draft | No email; comments returned | R6 |
| Leave a request unanswered | No email; backup asked, then timed out | R9 |
| Inspect an approval request | Draft, source and recipient shown | R7, R8 |
| Escalate each type | Correct recipient and one row | R11, R12 |
| Enter synthetic personal details | None appear in the log | R16 |
| Compare requests made with rows added | Counts match | R11 |

## To confirm in trial week 1

1. Whether to build these as agent flows or Power Automate cloud flows, and what each
   costs under the trial.
2. How the flows reply early to the agent while an approval is waiting.
3. How Flow 1 and Flow 2 call Flow 3.
4. Whether the agent calls the logging flow reliably after every policy answer.
5. How approval timeouts are configured and handled.
6. What run history and chat transcripts store, and for how long.
