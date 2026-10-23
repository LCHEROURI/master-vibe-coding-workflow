# Risk register

| ID | Risk | Likelihood / impact | Mitigation and trigger | Status |
|---|---|---|---|---|
| R1 | Accidental use of personal data | Low / disclosure or loss | Tests and demo use temporary paths and synthetic titles; stop if real data is implicated | Mitigated locally; users own their files |
| R2 | Invalid input or SQL-like title changes unintended rows | Medium / incorrect state | Parameterized queries, input checks, preservation assertions (AC2, AC4–AC6) | Mitigated for tested cases, E2; no general security audit claimed |
| R3 | Lost or corrupt database | Medium / task loss | SQLite transactions; surface errors; offline backup/restore drill (AC6–AC7) | Residual: no automatic backup or encryption |
| R4 | Local results misrepresented as production readiness | Medium / misleading example | Production NO-GO; distinguish tests, manual review, unrun platforms and deployment | Open scope limitation |
| R5 | Evidence becomes stale when code changes | Medium / false confidence | Commit logs with code; rerun checks on later changes; never silently overwrite failed records | Ongoing maintenance obligation |
| R6 | PR publishing credentials unavailable | Unknown / delivery blocked | Test actual Git/PR operations; do not expose tokens or claim an unopened PR exists | Pending publication |
