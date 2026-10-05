# MVCE Workflow Skill

## Purpose

Apply the Master Vibe Coding Engineering workflow to software-development tasks.

The skill governs AI-assisted implementation. It does not replace project requirements.

## Default behavior

When activated:

1. Determine the current MVCE phase.
2. Read the project specification and `.mvce/WORKBOOK.md` if they exist.
3. Inspect current repository state.
4. Identify the next unsatisfied gate.
5. Perform only actions allowed by the current Authority Lease.
6. Make the smallest coherent change needed to advance the current gate.
7. Verify the result.
8. Record evidence.
9. Update the workbook.
10. Stop at approval boundaries.

## Hard rules

- Do not begin meaningful implementation without a specification, acceptance criteria, build plan, and Authority Lease.
- Do not claim tests passed unless they were actually run.
- Do not treat generated reasoning as verification.
- Do not fabricate evidence.
- Do not hide failed checks.
- Do not remove security controls simply to make the build pass.
- Do not expose or commit secrets.
- Do not deploy without satisfying the deployment gate.
- Do not expand task scope silently.
- Do not overwrite unrelated user work.
- Do not mark a phase complete if required evidence is missing.

## Existing projects

If the repository already exists:

1. inspect before editing;
2. identify existing conventions;
3. preserve compatible project structure;
4. create missing MVCE artifacts without unnecessarily rewriting the project;
5. document technical debt rather than silently repairing unrelated areas.

## New projects

For a new project:

1. complete Intake;
2. produce `PROJECT-SPEC.md`;
3. produce acceptance criteria;
4. establish architecture;
5. produce the build plan;
6. establish the Authority Lease;
7. begin implementation only after these gates pass.

## Per-task execution protocol

```text
READ TASK
→ INSPECT
→ STATE INTENT
→ CHECK AUTHORITY
→ IMPLEMENT
→ INSPECT DIFF
→ TEST
→ VERIFY
→ CAPTURE EVIDENCE
→ UPDATE WORKBOOK
→ COMMIT/WAIT
```

## Completion response

When reporting completion, include:

- what changed;
- what was verified;
- evidence generated;
- what remains unverified;
- risks or limitations;
- next MVCE gate.
