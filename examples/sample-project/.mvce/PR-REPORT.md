# Replace the placeholder with a runnable MVCE worked example

The sample previously promised a future worked example but contained no app or
completed artifacts. It now contains Pocket Tasks, a small Python/SQLite CLI
with add/list/done commands, eight subprocess acceptance tests, and a separate
CLI/backup-restore smoke path. No third-party dependencies are needed.

The completed spec and nine MVCE artifacts trace prospective requirements to
real captured output, retain the initial failures, and explain all canonical
workflow phases. Planning/authority/verification documents were committed at
`d8f7235` before application implementation. The root README gets one pointer;
the method, agent rules, root workbook and templates remain unchanged.

## Actual validation

Commands ran from `examples/sample-project/`:

| Command | Actual result |
|---|---|
| `python3 -m unittest discover -s tests -v` before tasks.py | 8 tests, 8 expected failures (missing app), exit 1; retained in evidence/01-red-tests.txt |
| `python3 -m unittest discover -s tests -v` after implementation | 8 tests passed, 0 skipped, exit 0; evidence/02-green-tests.txt |
| `bash smoke.sh` | Add/list/done JSON and offline backup/modify/restore assertions passed, exit 0; evidence/03-cli-and-recovery.txt |
| `python3 .mvce/check_artifacts.py` | Artifact presence, local links, current app/test/smoke hashes, path scope and diff whitespace checks passed, exit 0; evidence/04-artifacts.txt |

The initial capture wrapper failed before tests started because its output
directory was absent. Its actual error is retained in evidence/00-capture-error.txt;
the path was corrected before the red run. No failed check is relabeled as a
passing test. The capture logs record full commands, combined output, statuses,
UTC timestamps and source hashes. The tests and smoke path use temporary data.
Only Python 3.12.14/Linux was tested; 3.10+ is the intended compatibility floor.

## Every MVCE phase / gate

| Phase | State and reason |
|---|---|
| 0 Intake | PASS — local reader workflow and measurable success defined |
| 1 Specification | PASS — F1–F4/N1–N3 mapped to prospective AC1–AC8 and risks |
| 2 Architecture | PASS — one standard-library CLI, SQLite, explicit security/scale limits |
| 3 Planning | PASS — T1–T5 with dependencies, tests and rollback considerations |
| 4 Authority | PASS — user's request authorizes bounded sample, branch and PR; lease protects other files |
| 5 Inspection | PASS — clean placeholder baseline and tools inspected |
| 6 Implementation | PASS — local contract implemented, eight green tests |
| 7 Verification | PASS locally — subprocess tests plus a separate asserted shell path; same agent ran both, no CI/human review claimed |
| 8 Evidence | PASS — actual logs including capture failure and red tests, with code hashes |
| 9 Commit | PASS — planning d8f7235 and implementation/evidence 2e7f622 committed and pushed; later delivery notes do not change application code |
| 10 Pre-deployment | NO-GO — no production target, operating model or approval |
| 11 Deployment | NOT RUN — blocked by deliberate NO-GO |
| 12 Production verification | NOT RUN — no deployment; local smoke is not production evidence |
| 13 Recovery | PASS locally — written plan and two stopped-database restore checks; no production incident claimed |
| 14 Maintenance | Plan complete; future execution remains a maintainer responsibility |
| 15 Closeout | Local evidence/docs complete; human PR review remains outstanding; publication status in workbook |

No build/code generation is required. Dedicated lint/type tooling is not
configured. No hosted service, credentials, payments, encryption, automatic
backups, migrations, or multiuser guarantees are claimed. This is a runnable
local teaching example, not a production release. Next action: human review of
the source change, without merging automatically.

## Method defects / gaps found (reported, not edited)

1. Root WORKBOOK.md numbers deployment as gate 10 and production verification
   as gate 11; canonical WORKFLOW.md distinguishes phase 10 pre-deployment,
   phase 11 deployment and phase 12 production verification. The sample uses
   canonical phase numbers and shows each disposition separately.
2. Checklist/workbook templates do not explicitly distinguish not-applicable
   checks and local-only delivery from production completion. The sample spells
   out NO-GO, NOT RUN, and excluded checks rather than producing a fake all-green
   workbook.

## Delivery status

The branch `feat/sample-mvce-task-tracker` is pushed to origin. Automated PR
creation is blocked: the actual `gh pr create` returned
`Post "https://api.github.com/graphql": Forbidden`, including when retried with
the permitted network escalation. No PR has been created by this task. Enable
`api.github.com` access, then run the command recorded as E5 using this report
as `--body-file`. Do not treat the GitHub compare/new-PR link as an existing PR.
