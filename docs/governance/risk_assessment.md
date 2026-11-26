# Risk Assessment

> Juniper Ridge Financial is a fictional firm. Ratings are judgements made for this
> project.

## Scope and method

This assessment covers the four use cases in
[the use-case intake](use_case_intake.md). Likelihood and impact are rated Low,
Medium or High before controls are applied.

Controls are of two kinds:

- **Process:** enforced by a flow step or a person.
- **Instruction:** written into the agent's instructions. These reduce a risk but do
  not guarantee behaviour, so each one is tested.

All controls are planned. They are confirmed only after testing.

## UC1: Policy questions

| ID | Risk | Likelihood | Impact | Control | Type | Test |
| --- | --- | --- | --- | --- | --- | --- |
| R1 | Wrong or invented answer | Medium | High | Answer only from policy documents and name the source; staff check it | Instruction, process | Compare answers and sources on the test set |
| R2 | Question is not covered by policy | High | Medium | Say it does not know and offer escalation | Instruction | Out-of-scope test questions |
| R3 | Policy documents are outdated or disagree | Low | High | Each document has an owner and review date; documents are checked against each other | Process | Manual consistency review |
| R4 | Request for investment, tax or legal advice | Medium | High | Decline and direct the person to an advisor or the client's own professional | Instruction | Advice-seeking test questions |
| R5 | A trick message tells the assistant to ignore its rules | Low | High | Instructions refuse rule changes; sending still requires approval | Instruction, process | Trick test questions |

## UC2: Client reply drafts

| ID | Risk | Likelihood | Impact | Control | Type | Test |
| --- | --- | --- | --- | --- | --- | --- |
| R6 | A reply is sent without review | Low | High | The flow sends email only after an approval is recorded | Process | Reject a draft and confirm nothing is sent |
| R7 | An approver accepts a draft containing an error | Medium | High | Approval request shows the draft, the original request and the source policy | Process | Inspect an approval request |
| R8 | Reply goes to the wrong recipient | Low | High | Approval request shows the recipient; during the project only the builder's address is used | Process | Inspect an approval request |
| R9 | No approver is available | Medium | Medium | Compliance officer is the backup; an unapproved draft is never sent | Process | Leave a request unanswered and confirm nothing is sent |
| R10 | A complaint is handled as a routine reply | Medium | High | Do not draft; escalate to the compliance officer | Instruction | Complaint test questions |

## UC3: Escalation

| ID | Risk | Likelihood | Impact | Control | Type | Test |
| --- | --- | --- | --- | --- | --- | --- |
| R11 | An escalated question is missed | Medium | Medium | Send to a named person and record the escalation in the log | Process | Confirm both the message and the log row |
| R12 | A question goes to the wrong person | Medium | Medium | Fixed routing: complaints and regulatory to compliance, process and technical to operations | Instruction, process | One test of each type |

## UC4: Knowledge-base drafts

| ID | Risk | Likelihood | Impact | Control | Type | Test |
| --- | --- | --- | --- | --- | --- | --- |
| R13 | Client details are copied into an article | Medium | High | Leave out personal details; manager reviews before publishing | Instruction, process | Draft from input containing synthetic personal details |
| R14 | An article contradicts policy | Medium | Medium | Draft from policy documents; manager reviews before publishing | Instruction, process | Compare the article with its sources |

## All use cases

| ID | Risk | Likelihood | Impact | Control | Type | Test |
| --- | --- | --- | --- | --- | --- | --- |
| R15 | Client personal details are typed into chat | High | High | Tell staff not to enter them; do not repeat them; use only synthetic data | Instruction, process | Test messages with synthetic personal details |
| R16 | The request log stores personal details | Medium | High | Log a short topic label, not the full message | Process | Inspect log rows after testing |
| R17 | Staff trust answers without checking | Medium | Medium | Show sources; the user guide states the limits | Process | Review the user guide |
| R18 | Exported files reveal account or tenant details | Medium | Medium | Check every export before committing | Process | Review before each commit |

## Remaining risk

Instructions can fail, approvers can miss errors, and a person may still type client
details into chat. A real deployment would also need data protection, retention and
compliance reviews, which are outside this project.
