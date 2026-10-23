# Build plan

Recorded before application implementation; execute in table order. No app
dependencies need installation. Each unit is rejected if its checks fail.

| ID | Purpose / affected area / implementation intent | Depends on | Acceptance / validation | Risk / rollback | Initial status |
|---|---|---|---|---|---|
| T1 | Establish spec, criteria, lease, risks, verification strategy and workbook | User request and repository inspection | Review gates 0–5 before app code; commit planning checkpoint | Scope creep; revise artifacts before code | In progress |
| T2 | Write CLI subprocess tests against disposable databases; observe missing-app failure | T1 | AC1–AC7; capture full failing unittest run | Misleading failure; inspect cause and preserve output | Not started |
| T3 | Implement a single standard-library CLI with SQLite transactions and JSON output | T2 | AC1–AC6; run complete test suite and inspect diff | Data/error handling; fix locally or revert code, preserve logs | Not started |
| T4 | Verify separately through shell-driven CLI lifecycle and stopped-file backup/restore | T3 | AC1, AC3, AC7; assert output/status, record commands | Accidental data changes; only use temp directory | Not started |
| T5 | Complete walkthrough and real evidence; review scope/links; commit and open PR | T4 | AC8; all gates honestly stated, production NO-GO | Unsupported claims/access failure; correct docs or report blocker | Not started |

## Deferred work

No deployment, production verification, multiuser support, packaging, CI setup,
or persistent services. No framework or third-party tools. Backup/restore uses
stopped CLI processes, not live-database file copying.

## Execution updates

Final task results and evidence IDs are recorded in WORKBOOK.md. The initial
plan above is retained so readers can distinguish intent from observed outcome.
