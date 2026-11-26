# Use-Case Intake

> Juniper Ridge Financial is a fictional firm. All volumes and time savings below are
> estimates made for this project, not measurements.

## Summary

| ID | Use case | Requests per week | Minutes saved each | Minutes saved per week | Data sensitivity | Human review |
| --- | --- | --- | --- | --- | --- | --- |
| UC1 | Policy questions | 60 answered | 6 | 360 | Low to medium | Staff check the cited source |
| UC2 | Client reply drafts | 45 | 8 | 360 | High | Required before sending |
| UC3 | Escalation of unanswered questions | 10 | 3 | 30 | Medium | A person answers each one |
| UC4 | Knowledge-base drafts | 1 | 45 | 45 | Low to medium | Required before publishing |
| | **Total** | **116** | | **795 (about 13 hours)** | | |

Staff ask about 70 policy questions a week: 60 are answered and 10 are escalated
under UC3. The total of 116 requests a week is about 1,500 over three months.
The saving averages about 20 minutes per employee per week.

## UC1: Policy questions

- **Problem:** Staff search several policy documents to answer routine questions.
- **Users:** All staff, mainly Client Service and Paraplanners.
- **What the help desk does:** Answers from the firm's policy documents, names the
  source, and says when it does not know.
- **Data involved:** Internal policies. Staff might type client details into a question.
- **Human review:** Staff check the cited document before relying on an answer.
- **Success measure:** Correct answer and correct source on the test set.

## UC2: Client reply drafts

- **Problem:** Routine client replies take time to write and must be reviewed.
- **Users:** Client Service, Paraplanners and Advisors.
- **What the help desk does:** Drafts a reply from policy and sends it for approval.
- **Data involved:** Client correspondence.
- **Human review:** Required. The client service manager approves, with the compliance
  officer as backup. No one approves their own request.
- **Success measure:** Share of drafts approved, and no reply sent without approval.
- **Not covered:** Complaints, and investment, tax or legal advice. Complaints and
  regulatory questions go to the compliance officer.

## UC3: Escalation of unanswered questions

- **Problem:** Unanswered questions are passed around informally and can be lost.
- **Users:** All staff.
- **What the help desk does:** Logs the question and sends it to a named person.
- **Data involved:** The question text, which might include client details.
- **Human review:** The operations lead handles process and technical questions. The
  compliance officer handles complaints and regulatory questions.
- **Success measure:** Every unanswered test question reaches the right person.

## UC4: Knowledge-base drafts

- **Problem:** Repeated questions are answered again each time.
- **Users:** Client service manager.
- **What the help desk does:** Drafts an article from repeated questions in the log.
- **Data involved:** Logged questions and internal policies.
- **Human review:** Required before an article is published.
- **Success measure:** Drafts match the source policies and need only light editing.

## Assumptions

- Minutes saved are net of the time the user spends checking the output.
- Client replies are already reviewed today, so approval adds no new review time.
- Demonstration data is synthetic. Real client data would need a data protection
  review before use.

## Checking the estimates

During testing, a few sample tasks will be timed with and without the help desk.
The results will be reported beside these estimates, noting the small sample and
that one person performed the tasks.

## Priority

1. UC1 and UC2 carry most of the estimated value.
2. UC3 is needed so that UC1 fails safely.
3. UC4 depends on the request log and is built last.
