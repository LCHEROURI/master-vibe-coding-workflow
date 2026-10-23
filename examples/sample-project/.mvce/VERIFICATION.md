# Verification strategy (before implementation)

## Scope and environment

Verify AC1–AC8 for local, sequential use. Python's unittest runner will launch
the CLI as separate processes using temporary SQLite files. No mocks or external
services. Python 3.12.14 is present in this cloud environment; 3.10+ is the
intended source compatibility range, not a claim of testing every version.

## Planned checks

1. Capture a red test run before tasks.py exists. Diagnose that failure as a
   missing implementation, and keep the failed output.
2. Run `python3 -m unittest discover -s tests -v` from the sample directory.
   Require real tests, zero failures, and exit 0.
3. Use a separate shell-driven smoke path to add/list/complete and back up,
   modify, and restore a disposable database; assert JSON and exit statuses.
4. Review all gates and local links; use `git diff --check` and a changed-path
   allowlist to verify scope. Review the diff for secrets and unrelated work.

The smoke path is separate from the unittest code, but both are authored/run by
the implementation agent. This is reproducible external behavior, not a claim
of independent human review or CI. No build or code generation is needed for
interpreted Python. No dedicated linter/type checker is configured.

## Checks performed

| Criterion | Actual check | Result / evidence |
|---|---|---|
| AC1 | `test_empty_then_add_persists_ac1`; separate smoke lifecycle | PASS — E2/E7, E3 |
| AC2 | `test_literal_titles_and_order_ac2` | PASS — E2/E7 |
| AC3 | `test_complete_one_idempotently_ac3`; smoke completes first task | PASS — E2/E7, E3 |
| AC4 | `test_blank_title_preserves_rows_ac4` | PASS — E2/E7 |
| AC5 | `test_invalid_and_unknown_ids_preserve_rows_ac5` (four input cases) | PASS — E2/E7 |
| AC6 | Missing parent and corrupt database tests | PASS — E2/E7 |
| AC7 | Stopped-database restoration test and independent shell path | PASS — E2/E7, E3 |
| AC8 | Artifact/phase review and scope/link checks | PASS for local docs — E4/E6 and workbook; PR #1 open per user; review fix awaits re-verification |

E2 ran eight tests, all passed, zero skipped, exit 0. The fresh review rerun
E7 likewise ran eight tests, all passed, zero skipped, exit 0; its actual output
is embedded directly in EVIDENCE-LEDGER.md and retained as a new raw log. E3 printed the actual JSON
and asserted both intermediate and restored data, exit 0. No build step is
required; the real interpreter executed the app on every subprocess call.

## Failed checks and limitations

E1 ran eight tests, all failed with the missing tasks.py executable. This is
the planned pre-implementation failure, preserved rather than erased. It does
not independently establish the sensitivity of each behavioral assertion.
The initial capture harness also failed before tests started because its
destination directory was created relative to the wrong working directory;
that setup mistake was corrected before E1, with no application change.

GitHub API access returned Forbidden when inspecting repository metadata;
publication is tracked separately in the workbook and PR report. The user now reports Muse opened PR #1 and independently verified eight passing
tests; that report is not presented as locally captured external output. No
human merge approval, CI result, production check, performance result, or
cross-version/platform test is asserted. Encryption, concurrent writers,
automatic backups and production operation are outside scope.

## Conclusion

PASS for the tested local application requirements AC1–AC7. AC8 depends on the
recorded document/scope review, not runtime tests. Production remains NO-GO;
Muse's re-verification and Larry's merge decision remain outstanding for PR #1.
