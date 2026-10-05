# Master Vibe Coding Engineering Workflow

**MVCE Workflow** is an open-source, platform-neutral workflow for vibe coders and AI coding agents.

It turns the principles of *Master Vibe Coding Engineering* into a governed software-development process with explicit gates, bounded agent authority, independent verification, evidence capture, deployment controls, and recovery discipline.

## Why this exists

AI coding agents can write code quickly. Speed is useful, but speed without control creates a different problem: unverified changes, hidden regressions, over-broad edits, weak evidence, and deployment risk.

MVCE adds an engineering control layer around AI-assisted development.

> Do not trust an AI coding agent because it says the work is done.  
> Define success before implementation, constrain authority, verify independently, and preserve evidence.

## Who this is for

MVCE is designed for:

- vibe coders;
- solo app builders;
- AI-assisted developers;
- no-code and low-code builders who also use coding agents;
- teams experimenting with autonomous or semi-autonomous coding agents;
- anyone who wants a repeatable workflow for safer AI-assisted software delivery.

## Lifecycle

```text
INTAKE
  ↓
SPECIFY
  ↓
PLAN
  ↓
AUTHORIZE
  ↓
INSPECT
  ↓
IMPLEMENT
  ↓
TEST
  ↓
VERIFY
  ↓
CAPTURE EVIDENCE
  ↓
ACCEPT / REJECT
  ↓
COMMIT
  ↓
DEPLOY
  ↓
VERIFY PRODUCTION
  ↓
MAINTAIN / RECOVER
```

## Core concepts

### Authority Lease

The agent receives explicit boundaries defining what it may change, what requires approval, and what is forbidden.

### Acceptance before implementation

Important requirements are converted into observable acceptance criteria before coding begins.

### Independent verification

The implementation agent's confidence is not treated as proof. Verification should use tests, runtime checks, CI, separate verification paths, or other independent evidence where practical.

### Evidence bundle

Important claims about correctness should point to durable evidence such as test output, CI results, screenshots, build logs, deployment IDs, or production checks.

### Recovery discipline

A production change is not considered ready if there is no credible recovery or rollback path.

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

1. Clone or download this repository.
2. Read `WORKFLOW.md`.
3. Give `SKILL.md` to the AI coding agent as its operating workflow.
4. Keep project-specific agent rules in `AGENTS.md`.
5. Copy the templates from `/templates` into the software project.
6. Complete project intake and specification.
7. Create the acceptance criteria, build plan, Authority Lease, and verification strategy.
8. Begin implementation only after those gates are satisfied.
9. Keep `.mvce/WORKBOOK.md` current as the project advances.
10. Do not advance a gate when required evidence is missing.

## Non-negotiable rule

No meaningful implementation begins until the project has:

- a written project specification;
- acceptance criteria;
- a build plan;
- an Authority Lease;
- a verification strategy.

## Works with

The workflow is intentionally vendor-neutral. It can be adapted to coding agents and AI development environments such as:

- OpenAI Codex;
- Claude Code;
- GitHub Copilot;
- Gemini-based coding agents;
- Cursor;
- Lovable-style builders;
- Replit-style coding agents;
- future agentic development tools.

Platform-specific adapters may be added later. The core workflow should remain independent of any one vendor.

## Repository guide

- `WORKFLOW.md` — canonical MVCE lifecycle and gates
- `SKILL.md` — operating instructions for an AI coding agent
- `AGENTS.md` — project-level agent behavior and protected actions
- `WORKBOOK.md` — persistent project state and gate tracker
- `templates/` — reusable project-control artifacts
- `examples/` — worked examples as they are added

## Design goals

MVCE is designed to be:

- platform-neutral;
- understandable by non-programmers;
- usable with coding agents and vibe-coding tools;
- evidence-driven;
- resistant to uncontrolled agent behavior;
- suitable for greenfield projects and existing repositories;
- lightweight enough for solo builders.

## Status

**Current release: v0.1**

This is the stable baseline of the workflow. Future releases will deepen the methodology without changing the core goal: reliable, verifiable, controlled AI-assisted software development.

## Contributing

Contributions are welcome. See `CONTRIBUTING.md`.

Useful contributions include:

- worked project examples;
- clearer verification patterns;
- stronger evidence-capture techniques;
- platform adapters;
- deployment and recovery patterns;
- improvements that make the workflow easier for non-programmers to follow.

## Search terms

AI coding workflow, vibe coding, vibe coder, coding agents, AI-assisted software development, agentic coding, software verification, bounded autonomy, acceptance criteria, evidence-driven development, deployment safety, AI software engineering.

## License

MIT. See `LICENSE`.
