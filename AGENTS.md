# AGENTS.md

This project follows the Master Vibe Coding Engineering Workflow.

## Primary rule

Follow `WORKFLOW.md` and `SKILL.md`.

## Agent conduct

- Inspect before editing.
- Keep changes narrowly scoped.
- Preserve unrelated user work.
- Never invent test results.
- Never invent deployment results.
- Never claim a requirement is satisfied without evidence.
- Respect `.mvce/AUTHORITY-LEASE.md`.
- Record meaningful verification in `.mvce/EVIDENCE-LEDGER.md`.
- Keep `.mvce/WORKBOOK.md` current.
- Stop at human-approval boundaries.

## Protected actions

Unless explicitly authorized, do not:

- deploy to production;
- delete production data;
- modify billing behavior;
- rotate credentials;
- expose secrets;
- change authentication providers;
- weaken authorization;
- perform destructive database migrations;
- rewrite Git history.

## Development preference

Prefer small reversible changes over large speculative rewrites.

## Verification preference

Prefer deterministic, externally observable evidence over self-reported reasoning.
