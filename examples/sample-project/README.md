# Pocket Tasks: a worked MVCE example

This is a real, deliberately small local task tracker and its engineering
record. The point is the chain from requirements to observed behavior, including
an initial failing run and a **NO-GO for production**. It uses Python's standard
library; there is nothing to install beyond Python 3.10+ with SQLite support.
The recorded run used Python 3.12.14 on Linux; other versions/platforms have not
been verified.

## Run it

From the repository root:

```bash
cd examples/sample-project
python3 tasks.py --db tasks.sqlite3 add "Read WORKFLOW.md"
python3 tasks.py --db tasks.sqlite3 add "Record evidence"
python3 tasks.py --db tasks.sqlite3 list
python3 tasks.py --db tasks.sqlite3 done 1
python3 tasks.py --db tasks.sqlite3 list
python3 -m unittest discover -s tests -v
bash smoke.sh
```

Use a fresh database for the numbered example; existing databases retain their
IDs. `--db` goes before the subcommand and defaults to `tasks.sqlite3` in your
current directory. `list` returns all tasks, including completed ones, in ID
order. Output is JSON; each new invocation reads the saved file. Completing a
task twice succeeds. Duplicate titles are allowed. Blank titles and invalid IDs
exit 2; unknown IDs or storage failures exit 1 with an error on stderr. `--help`
lists the commands. Tests and smoke checks create their own temporary data;
they do not modify your `tasks.sqlite3`.

The real smoke run's first successful add printed:

```json
{"id": 1, "title": "Read WORKFLOW.md", "done": false}
```

That is an excerpt from [the captured CLI run](.mvce/evidence/03-cli-and-recovery.txt),
not a substitute for rerunning it. No secrets or confidential tasks belong in
this educational database. Its contents are not encrypted or backed up
automatically. Only sequential, single-user local use is in scope.

## Follow the phases

The phase numbers below follow the canonical [WORKFLOW.md](../../WORKFLOW.md).
The root [agent rules](../../AGENTS.md) and [operating skill](../../SKILL.md)
apply here. Start with the [workbook](.mvce/WORKBOOK.md) to see actual gate state.

| Phase | What happened here | What to do on your own project |
|---|---|---|
| 0 — Intake | [Specification](PROJECT-SPEC.md) identifies a reader, a small local problem, scale, constraints, and exclusions | Define an observable outcome before picking features |
| 1 — Specification | F1–F4/N1–N3 map to prospective [AC1–AC8](.mvce/ACCEPTANCE-CRITERIA.md); [risks](.mvce/RISK-REGISTER.md) name what can go wrong | Write requirements and expected results before code; record unknowns |
| 2 — Architecture | One CLI module, SQLite, no services; tradeoffs and security limits are in the spec | Choose only infrastructure your requirements need |
| 3 — Planning | [T1–T5](.mvce/BUILD-PLAN.md) name dependencies, acceptance checks, and rollback | Break delivery into testable units |
| 4 — Authority | [Lease](.mvce/AUTHORITY-LEASE.md) derives permission from the user's build/branch/PR request and protects the method | Obtain real authority; do not manufacture approval in a template |
| 5 — Inspection | Clean baseline had a placeholder, no app or dependencies; spec/criteria/plan/lease/verification strategy were committed at `d8f7235` before app code | Inspect the actual repo and preserve unrelated changes |
| 6 — Implementation | CLI acceptance tests were written first; [red run](.mvce/evidence/01-red-tests.txt) failed eight times because tasks.py was absent, then the CLI was implemented | Reject failed units; diagnose them before advancing |
| 7 — Verification | [Green run](.mvce/evidence/02-green-tests.txt) passed eight subprocess tests; a separate shell path checked behavior and restoration | Use observable results; disclose who performed verification |
| 8 — Evidence | [Ledger](.mvce/EVIDENCE-LEDGER.md) links actual combined output, commands, exit status, and code hashes | Capture output as produced, retain failures, and link claims to evidence |
| 9 — Commit | Planning checkpoint preserves chronology; final scope/diff review precedes delivery commit | Review intended paths, tests, secrets, artifacts, and limitations before committing |
| 10 — Pre-deployment | [Checklist](.mvce/DEPLOYMENT-CHECKLIST.md) says NO-GO: no production target, operating model, or approval | A correct decision can be to stop; passing local tests is insufficient |
| 11 — Deployment | Not run; source delivery is not deployment | Record a real release ID only after an authorized deployment |
| 12 — Production verification | Not run; no deployed environment exists | Verify the actual production user path; don't relabel local smoke checks |
| 13 — Recovery | [Plan](.mvce/RECOVERY-PLAN.md) plus test and shell drill restore a stopped disposable database | Preserve damaged data, restore a known-good backup, and verify before resuming |
| 14 — Maintenance | Future changes must rerun checks and preserve new evidence; no recurring service is operating | Re-enter the same workflow for changes, incidents, and drift |
| 15 — Closeout | Workbook records local acceptance, limits, publishing state, and next action | Close only the scope your evidence supports |

The planning commit is an auditable checkpoint, not a claim that the human
approved every document separately. The user authorized this local example.
Gates 0–5 are document/inspection judgments. The red run proves the suite detects
a missing app; it does not prove each assertion was mutation-tested. The shell
path is separate from the test code, but the same agent authored and ran both.
No independent human review or CI run is claimed.

## Inspect or repeat the evidence

Read [VERIFICATION.md](.mvce/VERIFICATION.md) for acceptance coverage and exclusions
and [EVIDENCE-LEDGER.md](.mvce/EVIDENCE-LEDGER.md) for raw logs. Run the commands
above to produce new observations; do not overwrite the historical logs to make
them look current. Python unittest output includes elapsed time and temp paths
vary, so byte-for-byte reproduction of a whole transcript is not expected.
The database backup drill only copies files while every CLI process has exited.
Do not apply that recipe to a live database or restore real data without consent.

## Method gaps encountered

The method itself is unchanged. Two small documentation gaps matter here:

- The root workbook groups deployment at gate 10 and production verification at
  gate 11, while canonical WORKFLOW.md uses phase 10 pre-deployment, phase 11
  deployment, and phase 12 production verification. This sample spells out all
  canonical phases to avoid implying that deployment/production checks passed.
- The templates do not explicitly label non-applicable checks or distinguish
  local delivery from production release. This sample records NOT APPLICABLE,
  NOT RUN, and NO-GO explicitly rather than checking every box.

The next gate is human PR review for the local deliverable; production work
would require a new specification and lease.
