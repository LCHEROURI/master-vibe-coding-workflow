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
E6 below rather than overwriting E4. Code/test/smoke hashes have not changed.
