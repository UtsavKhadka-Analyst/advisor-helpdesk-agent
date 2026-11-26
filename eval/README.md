# Evaluation Test Set

`test_questions.csv` holds 40 questions used to test the help desk. All names and
details in it are invented.

## Columns

| Column | Meaning |
| --- | --- |
| `question` | What a staff member types |
| `expected_answer` | What a correct reply says or does |
| `source_document` | Policy ID, or `none` |
| `category` | Type of test |

## Categories

| Category | Tests whether the help desk | Count |
| --- | --- | --- |
| `answerable` | Answers correctly and names the source | 20 |
| `out_of_scope` | Says it does not know | 6 |
| `advice` | Declines to give advice | 4 |
| `complaint` | Escalates instead of drafting | 3 |
| `trick` | Keeps its rules | 3 |
| `personal_data` | Avoids repeating personal details | 4 |

## Authorship and limits

The project author wrote the starting ideas for 3 questions. An AI assistant (Claude)
edited those and drafted the other 37. Five were later reworded into informal
everyday language, also by the assistant. The author reviews the set.

The same assistant helped draft the policies and agent instructions, so the questions
may be easier for the help desk than questions from independent users. Results should
be read with that in mind.
