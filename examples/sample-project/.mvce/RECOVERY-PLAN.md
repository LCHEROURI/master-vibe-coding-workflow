# Recovery plan

## Baseline and failure signals

Before implementation, repository baseline is `ea023e27bdec1b08cad74b7660f9a94288cf52c0`;
it has no app and is not a data recovery image. The final verified code checkpoint
will be the commit containing the green evidence bundle. Keep a known-good copy
of your own database separately. Signals: nonzero exit, `error:` on stderr,
unexpected task rows, or failing tests. No production incident is claimed.

## Containment and recovery

1. Stop issuing mutating commands. Preserve error output and the affected file
   before attempting recovery; do not overwrite the only copy.
2. Stop all CLI processes. Copy a healthy database to a separate backup path
   before risky operations. Offline copying is the only supported drill here;
   do not copy a live SQLite database this way.
3. Inspect whether the failure is code, input, permissions, or storage. Preserve
   the damaged file under a new name before restoring a known-good backup to
   the selected `--db` path. Restore intentionally loses tasks added after the
   backup; user approval is required for restoring real user data.
4. For a code regression, make a reviewed Git revert on a new branch; do not
   rewrite history or erase evidence. There is no migration rollback command.
5. Run `list` against the restored path and compare with the backup inventory;
   rerun the test suite before resuming writes. Record the outcome and cause.

## Escalation and limits

No backup means no promised recovery. Escalate if corruption persists, data is
valuable, or schema changes/concurrent writers are involved. Do not initialize
over a corrupt file to make an error disappear. Tests and the smoke drill use
disposable data only; their restoration needs no approval for real data.

## Drill result

PASS for disposable local data: E2's backup/restore test saves one task, copies
the stopped database, adds another, restores, and checks that only the original
remains. E3 separately saves two tasks (one completed), copies, adds a third,
restores, and compares the complete task state with the pre-backup JSON. See
[the ledger](EVIDENCE-LEDGER.md). This demonstrates the mechanism, not recovery
of an actual production incident or a guarantee against disk failure.
