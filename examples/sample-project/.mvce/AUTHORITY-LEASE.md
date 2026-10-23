# Authority lease

- Applies to: Pocket Tasks worked example, branch `feat/sample-mvce-task-tracker`.
- Grant: the user's explicit request to build the app/artifacts, run checks,
  work on a branch, and open a pull request without merging.
- Starts: before application implementation in this task.
- Expires: at PR handoff, or immediately if scope materially expands.

## Allowed

Read the repository; create and edit files below `examples/sample-project/`;
optionally add one pointer line to the root README; run Python tests and local
CLI commands with disposable synthetic data; create the local sample SQLite
schema; preserve logs; commit and push this branch and open its PR. No new
approval is required for these actions because the user requested them.

## Approval required

Any production operation, destructive action on user data, paid infrastructure,
new external dependency, schema migration of existing data, or change to
authentication, authorization, billing, or credentials requires separate scope
and explicit approval. Missing publishing access is a blocker, not permission
to extract credentials or bypass access controls.

## Protected and forbidden

Do not change root `WORKFLOW.md`, `SKILL.md`, `AGENTS.md`, `WORKBOOK.md`,
`templates/`, or other out-of-scope files. Do not merge, deploy, expose secrets,
rewrite history, disable security controls, invent results, or delete evidence.
The sample inherits root AGENTS.md; no competing agent rules are introduced.

## Stop conditions

Stop the affected action if authority is missing, scope expands materially, or
real user data would be destroyed. A planned red test is expected evidence:
reject the implementation unit until corrected; do not advance its gate.
Unexpected failures likewise block the affected gate until diagnosed.
