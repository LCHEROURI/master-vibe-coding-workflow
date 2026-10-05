# Master Vibe Coding Engineering Workflow

**Version:** 0.1.0  
**Status:** Open-source draft

Master Vibe Coding Engineering Workflow (MVCE Workflow) is an executable development workflow for vibe coders and AI coding agents.

It converts the principles of *Master Vibe Coding Engineering* into a governed software-development process with explicit gates, bounded agent authority, independent verification, evidence capture, deployment controls, and recovery discipline.

## Core idea

> Do not trust an AI coding agent because it says the work is done.  
> Define success before implementation, constrain authority, verify independently, and preserve evidence.

## Lifecycle

`INTAKE → SPECIFY → PLAN → AUTHORIZE → IMPLEMENT → TEST → VERIFY → EVIDENCE → COMMIT → DEPLOY → PRODUCTION VERIFY → MAINTAIN`

## Required project artifacts

A project using MVCE should contain:

```text
PROJECT-SPEC.md
AGENTS.md
.mvce/
  WORKBOOK.md
  AUTHORITY-LEASE.md
  BUILD-PLAN.md
  ACCEPTANCE-CRITERIA.md
  RISK-REGISTER.md
  VERIFICATION.md
  EVIDENCE-LEDGER.md
  DEPLOYMENT-CHECKLIST.md
  RECOVERY-PLAN.md
```

## Quick start

1. Copy this repository into, or alongside, your software project.
2. Give the coding agent `SKILL.md` as its operating workflow.
3. Keep project-specific agent rules in `AGENTS.md`.
4. Start with Phase 0 in `WORKFLOW.md`.
5. Copy the templates from `/templates` into your project.
6. Do not advance to the next gate until the current gate is satisfied.
7. Keep `.mvce/WORKBOOK.md` current throughout the project.

## Non-negotiable rule

No meaningful implementation begins until the project has:

- a written project specification;
- acceptance criteria;
- a build plan;
- an Authority Lease;
- a verification strategy.

## Design goals

MVCE is designed to be:

- platform-neutral;
- understandable by non-programmers;
- usable with coding agents and vibe-coding tools;
- evidence-driven;
- resistant to uncontrolled agent behavior;
- suitable for greenfield projects and existing repositories;
- lightweight enough for solo builders.

## License

MIT. See `LICENSE`.
