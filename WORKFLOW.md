# Master Vibe Coding Engineering Workflow

**Version:** 0.1.0

This document defines the canonical MVCE development lifecycle.

The workflow is stateful. Every phase has an entry condition, required actions, required evidence, and an exit gate.

An agent must not skip a gate merely because implementation appears simple.

---

# Operating Principles

## 1. Specification precedes implementation

The system must know what it is trying to build before code changes begin.

## 2. Authority must be bounded

The agent may only perform actions explicitly allowed by the current Authority Lease.

## 3. Small changes beat giant changes

Prefer bounded, reviewable implementation units.

## 4. Verification is separate from implementation

The agent that writes a change must not treat its own confidence as proof.

## 5. Evidence must survive the session

Important verification results belong in persistent artifacts, not transient chat.

## 6. Production is a separate environment

Passing locally is not equivalent to passing in production.

## 7. Recovery is part of delivery

A change is not production-ready if failure cannot be reversed or mitigated.

---

# Phase 0 — Intake

## Goal

Convert an idea into a sufficiently precise project definition.

## Required actions

Capture:

- target user;
- problem being solved;
- primary workflow;
- success condition;
- platform;
- expected scale;
- constraints;
- external services;
- budget constraints;
- deadline constraints;
- deployment target;
- explicit exclusions.

## Required artifact

`PROJECT-SPEC.md`

## Gate 0

Do not continue until the project goal can be stated in one paragraph and success can be evaluated objectively.

---

# Phase 1 — Specification

## Goal

Transform the project idea into verifiable requirements.

## Required actions

Document:

- functional requirements;
- non-functional requirements;
- user roles;
- data entities;
- integrations;
- permissions;
- edge cases;
- failure behavior;
- security expectations;
- privacy expectations;
- observability requirements;
- acceptance criteria.

## Required artifacts

- `PROJECT-SPEC.md`
- `.mvce/ACCEPTANCE-CRITERIA.md`
- `.mvce/RISK-REGISTER.md`

## Gate 1

Every high-priority requirement must have at least one acceptance criterion.

---

# Phase 2 — Architecture

## Goal

Choose the simplest architecture capable of satisfying the specification.

## Required actions

Define:

- frontend;
- backend;
- database;
- authentication;
- authorization;
- storage;
- external APIs;
- background jobs;
- deployment platform;
- secrets management;
- observability;
- backup strategy.

Record significant tradeoffs.

## Rule

Do not introduce infrastructure because it is fashionable. Introduce it because a requirement demands it.

## Gate 2

Architecture must support the documented requirements without unnecessary complexity.

---

# Phase 3 — Planning

## Goal

Break implementation into small, independently verifiable units.

## Required actions

Create implementation tasks.

Each task must contain:

- purpose;
- affected area;
- dependencies;
- implementation intent;
- acceptance criteria;
- validation method;
- rollback consideration.

## Required artifact

`.mvce/BUILD-PLAN.md`

## Gate 3

No task may enter implementation unless its expected outcome can be tested.

---

# Phase 4 — Authority Lease

## Goal

Explicitly define what the coding agent may and may not do.

## Required artifact

`.mvce/AUTHORITY-LEASE.md`

## Lease categories

### Allowed without additional approval

Examples:

- inspect repository files;
- modify files within the current task scope;
- run local tests;
- run formatters;
- create non-secret documentation.

### Approval required

Examples:

- modify database schema;
- add paid infrastructure;
- rotate secrets;
- alter authentication;
- change production configuration;
- delete data;
- introduce major dependencies;
- change billing logic;
- change permissions;
- deploy to production.

### Forbidden

Examples:

- expose secrets;
- disable security controls to make tests pass;
- falsify tests;
- delete evidence;
- rewrite project history to conceal failures;
- claim verification that did not occur.

## Gate 4

Implementation may begin only after the current Authority Lease exists.

---

# Phase 5 — Repository Inspection

## Goal

Understand the real state of the project before editing it.

## Required actions

Inspect, when applicable:

- repository structure;
- current branch;
- uncommitted changes;
- package manifests;
- runtime versions;
- build scripts;
- test configuration;
- environment-variable references;
- database schema;
- authentication;
- deployment configuration;
- CI/CD;
- existing errors;
- documentation.

## Rule

Do not overwrite unknown work.

## Gate 5

The agent must be able to state what it intends to change and what it intends not to change.

---

# Phase 6 — Implementation Loop

For every implementation unit, perform the following sequence.

## 6.1 Restate the task

State the specific desired outcome.

## 6.2 Inspect the affected system

Read relevant code and configuration before editing.

## 6.3 Predict impact

Identify files, modules, data, integrations, tests, and user flows likely to be affected.

## 6.4 Implement the smallest coherent change

Avoid unrelated refactoring.

## 6.5 Inspect the diff

Check for:

- accidental changes;
- unrelated formatting;
- deleted behavior;
- leaked secrets;
- scope expansion.

## 6.6 Run targeted tests

Test the modified behavior first.

## 6.7 Run broader validation

Run relevant regression checks.

## 6.8 Record evidence

Update `.mvce/EVIDENCE-LEDGER.md`.

## 6.9 Accept or reject

A failed unit returns to diagnosis. It does not advance by explanation alone.

## Gate 6

The unit must satisfy its acceptance criteria and produce supporting evidence.

---

# Phase 7 — Verification

## Goal

Determine whether the implementation actually satisfies the specification.

## Verification hierarchy

Use the strongest practical evidence available:

1. deterministic automated tests;
2. integration tests;
3. end-to-end tests;
4. direct inspection of runtime behavior;
5. structured manual verification;
6. agent reasoning.

Agent reasoning is the weakest form of evidence.

## Independent verification

Whenever practical, verification should be separated from implementation by using:

- a different test path;
- a clean environment;
- a separate verifier;
- CI;
- an external service;
- reproducible commands;
- production smoke tests.

## Required artifact

`.mvce/VERIFICATION.md`

## Gate 7

A feature is not complete merely because the implementation agent reports success.

---

# Phase 8 — Evidence Bundle

## Goal

Create a durable record of why the project is believed to work.

## Evidence may include

- test commands;
- test outputs;
- screenshots;
- build logs;
- CI results;
- lint results;
- type checks;
- security scan results;
- migration output;
- deployment IDs;
- production checks;
- known limitations.

## Required artifact

`.mvce/EVIDENCE-LEDGER.md`

## Evidence integrity rule

Evidence should be captured from the system that produced it whenever practical rather than rewritten from memory by the implementation agent.

## Gate 8

All critical acceptance claims must point to evidence.

---

# Phase 9 — Commit Gate

## Goal

Create a meaningful, reviewable project checkpoint.

## Required actions

Before commit:

- verify intended files only;
- review diff;
- ensure tests relevant to the change pass;
- ensure no secrets were introduced;
- update project artifacts;
- document known limitations.

## Rule

Do not commit a knowingly broken state unless the commit is explicitly marked as such and the workflow requires it.

---

# Phase 10 — Pre-Deployment Gate

## Goal

Determine whether the project is safe to release.

## Required checks

When applicable:

- build passes;
- tests pass;
- type checks pass;
- lint passes;
- migrations reviewed;
- environment variables present;
- secrets not exposed;
- authentication works;
- authorization works;
- payments tested;
- backups verified;
- observability active;
- rollback path documented.

## Required artifact

`.mvce/DEPLOYMENT-CHECKLIST.md`

## Gate 10

Deployment requires an explicit GO decision.

---

# Phase 11 — Deployment

## Goal

Release the verified version without bypassing safety controls.

## Required actions

Record:

- deployment target;
- version or commit;
- migration state;
- deployment identifier;
- deployment outcome.

If deployment fails, transition to Recovery.

---

# Phase 12 — Production Verification

## Goal

Verify actual production behavior.

## Required checks

At minimum:

- application loads;
- critical user path works;
- authentication works if present;
- critical write operations work;
- errors are not spiking;
- external integrations respond;
- expected version is running.

## Rule

Local success does not satisfy this gate.

## Gate 12

Release is complete only after production verification succeeds.

---

# Phase 13 — Recovery

## Goal

Restore a safe state when implementation or deployment fails.

## Required artifact

`.mvce/RECOVERY-PLAN.md`

## Recovery sequence

1. stop further uncontrolled changes;
2. characterize the failure;
3. preserve relevant evidence;
4. identify last known-good state;
5. decide repair versus rollback;
6. execute bounded recovery;
7. verify restored behavior;
8. document cause and resolution.

---

# Phase 14 — Maintenance

## Goal

Prevent silent decay.

## Periodic checks

- dependency health;
- security advisories;
- expired credentials;
- failing jobs;
- broken integrations;
- test drift;
- architecture drift;
- data growth;
- backup validity;
- cost growth;
- observability gaps;
- documentation drift.

## Rule

Maintenance work enters the same MVCE loop as feature work.

---

# Phase 15 — Project Closeout

## Goal

Create a durable final state.

## Required outputs

- current specification;
- final acceptance status;
- known limitations;
- architecture summary;
- deployment state;
- recovery instructions;
- unresolved risks;
- evidence summary;
- next recommended actions.

A project is closed because evidence supports completion, not because activity stopped.

---

# Canonical MVCE Loop

```text
UNDERSTAND
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

# Stop Conditions

The agent must stop and request human approval when:

- required authority is absent;
- destructive data changes are proposed;
- production secrets are involved;
- billing behavior changes;
- authentication or authorization boundaries materially change;
- acceptance criteria conflict;
- evidence contradicts the claimed result;
- rollback is impossible for a high-risk change;
- implementation scope materially expands.

# Definition of Done

A task is done only when:

1. its acceptance criteria are satisfied;
2. verification has been performed;
3. evidence has been recorded;
4. known limitations are documented;
5. the project workbook reflects the current state.
