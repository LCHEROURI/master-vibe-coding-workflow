# Evidence ledger

These are observations from this coding task, not outputs copied from onboarding.
Raw logs preserve combined stdout/stderr and the underlying exit status. E1–E3
were captured by a temporary Python wrapper using subprocess.run, without a
pipeline masking a failure. Their headers record actual UTC time, working
directory, command, and SHA256 of the code/tests/smoke script when present.
Times are machine UTC; they are not release dates. Logs are historical records,
not commands to blindly overwrite on later runs.

| ID | Claim and actual command | Observed result | Raw evidence |
|---|---|---|---|
| E0 | Initial capture: `python3 /tmp/mvce-capture.py .mvce/evidence/01-red-tests.txt python3 -m unittest discover -s tests -v` | Capture failed before invoking tests: destination directory absent; exit 1. Corrected working-directory-relative mkdir, then ran E1 | [Actual error output](evidence/00-capture-error.txt) |
| E1 | From sample: `python3 -m unittest discover -s tests -v` before tasks.py existed | 8 executed, 8 FAIL, exit 1; missing app caused every failure. Gate 6 remained pending | [Red run](evidence/01-red-tests.txt) |
| E2 | From sample: `python3 -m unittest discover -s tests -v` after implementation | 8 executed, all passed, none skipped, exit 0; AC1–AC7 | [Green run](evidence/02-green-tests.txt) |
| E3 | From sample: `bash smoke.sh` | Real JSON for add/list/done; offline restore matches expected saved state; exit 0 | [CLI and recovery](evidence/03-cli-and-recovery.txt) |
| E4 | From sample: `python3 .mvce/check_artifacts.py` | Review validation is recorded in this log; this is not an application test or human approval | [Artifacts and scope](evidence/04-artifacts.txt) |
| E5 | From repository root: `gh pr create --repo LCHEROURI/master-vibe-coding-workflow --base main --head feat/sample-mvce-task-tracker --title "Add runnable Pocket Tasks MVCE worked example" --body-file examples/sample-project/.mvce/PR-REPORT.md` | Exit 1: GitHub GraphQL request Forbidden; PR not created | [Publication failure](evidence/05-pr-publication.txt) |
| E6 | From sample: `python3 .mvce/check_artifacts.py` after delivery-note updates | Final document links, artifact presence, app/test/smoke hashes, scope and diff checks | [Final artifact check](evidence/06-final-artifacts.txt) |

| E7 | From sample: `python3 -m unittest discover -s tests -v` for PR #1 review | 8 executed, 8 passed, zero skipped, exit 0; raw output embedded below | [Review acceptance rerun](evidence/07-review-acceptance.txt) |

## Review judgments and chronology

Gates 0–5 are grounded in the completed spec, prospective acceptance criteria,
bounded plan, lease, and verification strategy. Git commit `d8f7235` contains
those artifacts before any application/test code was committed. Inspection
showed clean baseline `ea023e27bdec1b08cad74b7660f9a94288cf52c0`, no app or test
runner, and Python 3.12.14. These are inspection facts, not eight extra tests.
The final diff review examines the implementation as well as scope checks.

E0 is a capture-tool error, not an app failure; its output was transcribed from
the actual tool result, not regenerated. E1 is the expected missing-executable
red run, not a historical defect in released software. E2 and E3 cover the
local contract; they do not establish production readiness or independent human
review. No deployment occurred. Publication results are recorded in the
workbook and delivery report, separately from acceptance of the local app.

E4 is the first successful artifact check at that point in the task; later
documentation-only delivery updates add links. The final check is preserved as
E6 rather than overwriting E4. Code/test/smoke hashes have not changed.

## E7 — acceptance rerun for PR #1 review

Fresh acceptance run on the unchanged application and tests, captured directly
from subprocess stdout/stderr. This output is embedded verbatim, not reconstructed
from a prose summary. The same transcript is retained in
[07-review-acceptance.txt](evidence/07-review-acceptance.txt).

```text
UTC: 2026-10-23T10:29:45.124254+00:00
Working directory: /workspace/master-vibe-coding-workflow/examples/sample-project
Command: /opt/codex/runtimes/codex-primary-runtime/dependencies/python/bin/python3 -m unittest discover -s tests -v
SHA256 tasks.py: b144c6d589d79401046dd49b2442b7c24794aecd71b13846dc851ddf9b0a96d8
SHA256 tests/test_tasks.py: 9913425b6cbd260d3989101f15634b42b50f8455eab49b84cd7c445147c44308
SHA256 smoke.sh: e0a65bf68b365d91f4b080b51555e7fd1486de54f9863fb7b4d634d9e859a045
--- combined stdout/stderr ---
test_blank_title_preserves_rows_ac4 (test_tasks.TasksCLI.test_blank_title_preserves_rows_ac4) ... ok
test_complete_one_idempotently_ac3 (test_tasks.TasksCLI.test_complete_one_idempotently_ac3) ... ok
test_corrupt_database_preserved_ac6 (test_tasks.TasksCLI.test_corrupt_database_preserved_ac6) ... ok
test_empty_then_add_persists_ac1 (test_tasks.TasksCLI.test_empty_then_add_persists_ac1) ... ok
test_invalid_and_unknown_ids_preserve_rows_ac5 (test_tasks.TasksCLI.test_invalid_and_unknown_ids_preserve_rows_ac5) ... ok
test_literal_titles_and_order_ac2 (test_tasks.TasksCLI.test_literal_titles_and_order_ac2) ... ok
test_missing_parent_reports_storage_error_ac6 (test_tasks.TasksCLI.test_missing_parent_reports_storage_error_ac6) ... ok
test_stopped_database_backup_restore_ac7 (test_tasks.TasksCLI.test_stopped_database_backup_restore_ac7) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.949s

OK
--- exit status: 0 ---
```

### Earlier diagnostic failures — preserved, not replaced by E7

E0 remains the capture-tool diagnostic failure (exit 1, no tests started).
E1 remains the pre-implementation diagnostic/red run (exit 1, eight failures
because tasks.py did not yet exist); its complete captured output is still in
[evidence/01-red-tests.txt](evidence/01-red-tests.txt). E2's original green output
is also unchanged. These historical files were not overwritten by the rerun.

Review feedback described a pre-fix corrupt-database diagnostic with seven
passes and one failure. That block is not present in the fetched branch at
c372388: E1 has eight missing-app failures and E2 has eight passes. No raw
seven-pass/one-fail output was available to preserve or quote, so none is
invented or substituted for E1. E7 above is the fresh observed result.

### PR handoff update (user-reported)

The user reports that Muse opened [PR #1](https://github.com/LCHEROURI/master-vibe-coding-workflow/pull/1)
on this branch and independently reran the suite with eight passing tests.
That external verification is reported context, not a locally captured command.
E5 remains the historical failure of this agent's PR creation attempt; it does
not mean a PR is still absent. This revision awaits Muse's re-verification;
Larry retains merge authority. No merge was performed.
