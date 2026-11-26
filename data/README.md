# Data

All data here is synthetic.

| Path | Contents |
| --- | --- |
| `policies/` | 12 invented policy documents |
| `request_history.csv` | Invented request log covering August 31 to November 27, 2026 |

## Request history

Created by `scripts/generate_request_history.py` with a fixed random seed:

```bash
uv run python scripts/generate_request_history.py
```

Columns match the Excel log layout in [the flow designs](../docs/flows.md). Request IDs
begin with `SYN-` so these rows stay identifiable when combined with trial rows.

## Assumptions

| Setting | Value |
| --- | --- |
| Weekly requests | Rising from 92 to 140, averaging 116 |
| Days | Weekdays, excluding September 7 and November 26 |
| Policy questions | About 60% of requests, 1 in 7 of them escalated |
| Client reply drafts | About 39% of requests |
| Knowledge-base drafts | 1 per week |
| Approval results | Drawn with weights of 85 approved, 12 rejected and 3 timed out |

Declined and failed requests are not simulated. Roles and topics follow invented
weights set in the script.

The file has 1,508 rows and about 12.3 hours saved per week. This is below the intake's
13 hours because rejected and timed-out drafts count as zero.

The growth trend, approval rates and time saved come from these assumptions. They
demonstrate the dashboard and are not results.
