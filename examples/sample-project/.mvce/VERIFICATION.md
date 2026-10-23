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

## Results

Not run yet. Gates 6–9 remain pending. Production and cross-platform behavior
will remain unverified; local success cannot pass the production gate.
