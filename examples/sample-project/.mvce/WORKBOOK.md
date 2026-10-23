# Pocket Tasks workbook

Current phase: 5 — repository inspection, before application implementation.
Current gate: gates 0–5 satisfied for this authorized local example; next T2.

| Phase / gate | Initial status | Basis |
|---|---|---|
| 0 Intake | PASS | PROJECT-SPEC.md defines reader, problem, constraints and observable success |
| 1 Specification | PASS | Requirements map to prospective AC1–AC8; risks recorded |
| 2 Architecture | PASS | Single standard-library SQLite CLI; operational/security exclusions explicit |
| 3 Planning | PASS | T1–T5 have dependencies, validation and rollback considerations |
| 4 Authority | PASS | User authorized sample, branch and PR; lease bounds actions |
| 5 Inspection | PASS | Clean baseline ea023e2; placeholder only; no existing app/tests/dependencies/CI; Python 3.12.14 available |
| 6 Implementation | PENDING | No app code written yet |
| 7 Verification | PENDING | Strategy written; commands not run yet |
| 8 Evidence | PENDING | Capture actual outputs next |
| 9 Commit | PENDING | Planning checkpoint first; final diff/tests later |
| 10 Pre-deployment | NO-GO | Local-only example; no production target or authorization |
| 11 Deployment | NOT RUN | Blocked by NO-GO |
| 12 Production verification | NOT RUN | No production deployment |
| 13 Recovery | PENDING | Write plan and exercise disposable stopped-file restore |
| 14 Maintenance | PLANNED | Rerun suite on changes; preserve evidence and scope limits |
| 15 Closeout | PENDING | Local deliverable and PR handoff outstanding |

This sample inherits the repository's AGENTS.md. The root workbook is a blank
reusable artifact and is deliberately untouched. Initial gate judgments 0–5
are document/inspection judgments, not automated test results. Later updates
must point to captured evidence rather than pretend these were runtime tests.
