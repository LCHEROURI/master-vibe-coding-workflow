# Pocket Tasks: project specification

## Intake (recorded before implementation)

Pocket Tasks gives a single local user a way to add a short task, list saved
tasks, and mark a task complete from a terminal. Its purpose is to make the MVCE
method observable in a tiny real project. Success means the acceptance criteria
pass against the actual CLI and a reader can trace those results to captured
commands, including failures and the decision not to deploy.

- Target user: a reader of *Master Vibe Coding Engineering* learning the workflow.
- Platform: a terminal with Python 3.10+ and its standard-library SQLite module.
- Scale: one user, sequential commands, tens of tasks; no shared service.
- Budget: no paid services or third-party dependencies.
- Deadline: this worked-example change; no external release deadline.
- External services: none at runtime. GitHub is used only to review the change.
- Delivery: source in a pull request, executable locally; no production target.
- Constraints: preserve the canonical method and templates; keep all sample
  code, tests, artifacts, and evidence in this directory.

## Requirements and acceptance mapping

| ID | Requirement | Acceptance |
|---|---|---|
| F1 | Add a nonblank title and return a stable positive ID | AC1, AC4 |
| F2 | List all tasks in ID order with completion state, across processes | AC1, AC2 |
| F3 | Complete an existing ID; repeating completion is harmless | AC3 |
| F4 | Reject blank titles, invalid/unknown IDs, and inaccessible storage without a traceback | AC4, AC5, AC6 |
| N1 | Run offline with the standard library and isolate data with an explicit path | AC1–AC7 |
| N2 | Demonstrate backup/restore using disposable data | AC7 |
| N3 | Preserve real evidence and explain every gate and excluded production work | AC8 |

## Interface and failure behavior

Run `python3 tasks.py --db PATH add TITLE`, `list`, or `done ID`. `--db`
defaults to `tasks.sqlite3` in the current directory. Output is one JSON object
for add/done, or a JSON array for list. Each task has `id` (integer), `title`
(trimmed, nonempty string), and `done` (boolean). Empty list prints `[]`.
Duplicate titles are allowed; IDs distinguish tasks. Unicode and quotes must
round-trip literally. Successful operations exit 0. Invalid arguments exit 2;
unknown IDs or SQLite errors exit 1 with an `error:` message on stderr.
Errors must not change existing task rows. Parent directories are not created.

## Architecture and data

The CLI parser is the frontend; one Python module performs parameterized SQLite
queries. SQLite is the database and storage, with a single `tasks` table:
`id INTEGER PRIMARY KEY`, `title TEXT NOT NULL`, `done INTEGER NOT NULL DEFAULT 0`.
Writes use transactions. No server, browser, background jobs, ORM, package
installation, or code generation is needed. SQLite is chosen over handwritten
JSON persistence for transactional writes without extra dependencies. An
in-memory-only app would be smaller but would not demonstrate persistence.

## Security, privacy, and operations

The only role is the local OS user. Filesystem permissions provide access
control; there is no authentication or application authorization boundary. No
secrets, payments, networking, telemetry, or API integrations are used. Titles
are user data and appear in terminal output: use synthetic tasks here, never
confidential data. The database is not encrypted. Back up only while CLI
processes are stopped; see the recovery plan. Observe commands through JSON,
stderr, exit status, and tests, rather than a monitoring service.

## Explicit non-goals and open questions

No delete/edit/search, multiuser service, concurrent-writer guarantees, schema
migrations, packaging, hosted deployment, or production suitability. These are
scope limits, not silently satisfied requirements. No blocking product questions
remain. Production work would require a new specification and lease.
