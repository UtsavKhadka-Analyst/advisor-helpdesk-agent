"""Generate a synthetic request history for the help desk dashboard.

All rows are invented. The volumes, mix, approval rates and growth trend are
assumptions, so charts built from this file demonstrate the dashboard and are not
findings. Columns match the Excel log layout in docs/flows.md.
"""

import csv
import random
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

SEED = 2026
START = date(2026, 8, 31)  # a Monday
WEEKS = 13
HOLIDAYS = {date(2026, 9, 7), date(2026, 11, 26)}
OUTPUT = Path(__file__).resolve().parents[1] / "data" / "request_history.csv"

# Requests per week rise steadily and average 116, as in the use-case intake.
WEEKLY_REQUESTS = [92 + 4 * week for week in range(WEEKS)]

# From the intake: 70 policy questions (10 of them escalated) per 115 non-article
# requests, plus 1 knowledge-base draft each week.
POLICY_SHARE = 70 / 115
ESCALATED_SHARE = 10 / 70

APPROVAL_WEIGHTS = {"approved": 85, "rejected": 12, "timed out": 3}

COLUMNS = [
    "request_id",
    "date",
    "staff_role",
    "category",
    "topic",
    "outcome",
    "approval_result",
    "minutes_saved",
]

POLICY_ROLES = {
    "Client Service": 40,
    "Paraplanner": 22,
    "Advisor": 18,
    "Operations": 10,
    "Management and Administration": 6,
    "Compliance": 4,
}
DRAFT_ROLES = {"Client Service": 60, "Paraplanner": 22, "Advisor": 18}

POLICY_TOPICS = {
    "address change": 15,
    "account transfer": 14,
    "beneficiary change": 12,
    "document sharing": 12,
    "identity check": 11,
    "onboarding": 10,
    "email retention": 6,
    "client communication": 6,
    "insurance review": 5,
    "data protection": 4,
    "tax documents": 2,
    "other": 3,
}
# Complaints are never drafted, so the topic is left out.
DRAFT_TOPICS = {
    "address change": 20,
    "account transfer": 20,
    "onboarding": 16,
    "beneficiary change": 14,
    "document sharing": 12,
    "insurance review": 9,
    "client communication": 5,
    "tax documents": 2,
    "other": 2,
}
ESCALATION_TOPICS = {
    "other": 40,
    "complaint": 18,
    "account transfer": 14,
    "identity check": 10,
    "data protection": 8,
    "beneficiary change": 6,
    "document sharing": 4,
}


def pick(rng, weights):
    return rng.choices(list(weights), weights=list(weights.values()))[0]


def row(day, role, category, topic, outcome, approval, minutes):
    return {
        "date": day.isoformat(),
        "staff_role": role,
        "category": category,
        "topic": topic,
        "outcome": outcome,
        "approval_result": approval,
        "minutes_saved": minutes,
    }


def week_rows(rng, week):
    monday = START + timedelta(weeks=week)
    days = [monday + timedelta(days=d) for d in range(5)]
    days = [d for d in days if d not in HOLIDAYS]

    others = WEEKLY_REQUESTS[week] - 1
    policy = round(others * POLICY_SHARE)
    escalated = round(policy * ESCALATED_SHARE)
    drafts = others - policy

    rows = []
    for _ in range(policy - escalated):
        rows.append(row(rng.choice(days), pick(rng, POLICY_ROLES), "Policy question",
                        pick(rng, POLICY_TOPICS), "answered", "not required", 6))
    for _ in range(escalated):
        rows.append(row(rng.choice(days), pick(rng, POLICY_ROLES), "Policy question",
                        pick(rng, ESCALATION_TOPICS), "escalated", "not required", 3))
    for _ in range(drafts):
        approval = pick(rng, APPROVAL_WEIGHTS)
        rows.append(row(rng.choice(days), pick(rng, DRAFT_ROLES), "Client reply draft",
                        pick(rng, DRAFT_TOPICS), "answered", approval,
                        8 if approval == "approved" else 0))
    rows.append(row(rng.choice(days), "Management and Administration",
                    "Knowledge-base draft", pick(rng, POLICY_TOPICS), "answered",
                    "not required", 45))
    return rows


def main():
    rng = random.Random(SEED)
    rows = [r for week in range(WEEKS) for r in week_rows(rng, week)]
    rows.sort(key=lambda r: r["date"])
    for number, r in enumerate(rows, start=1):
        r["request_id"] = f"SYN-{number:05d}"

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} synthetic rows to {OUTPUT.name}")
    print("Outcomes:", dict(Counter(r["outcome"] for r in rows)))
    print("Categories:", dict(Counter(r["category"] for r in rows)))
    print("Approvals:", dict(Counter(r["approval_result"] for r in rows)))
    hours = sum(r["minutes_saved"] for r in rows) / 60
    print(f"Estimated hours saved: {hours:.0f} ({hours / WEEKS:.1f} per week)")


if __name__ == "__main__":
    main()
