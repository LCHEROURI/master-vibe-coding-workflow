# MVCE Project Workbook

**Project:**  
**Repository:**  
**Owner:**  
**Current phase:**  
**Current gate:**  
**Status:** NOT STARTED

---

## 0. Intake

- [ ] Problem defined
- [ ] Target user defined
- [ ] Success condition defined
- [ ] Platform selected
- [ ] Constraints captured
- [ ] Explicit exclusions captured

**Gate 0:** [ ] PASS

---

## 1. Specification

- [ ] Functional requirements documented
- [ ] Non-functional requirements documented
- [ ] Roles and permissions documented
- [ ] Data requirements documented
- [ ] Integrations documented
- [ ] Edge cases documented
- [ ] Acceptance criteria created

**Gate 1:** [ ] PASS

---

## 2. Architecture

- [ ] Frontend decided
- [ ] Backend decided
- [ ] Database decided
- [ ] Authentication decided
- [ ] Deployment target decided
- [ ] Observability decided
- [ ] Backup/recovery approach decided

**Gate 2:** [ ] PASS

---

## 3. Build Plan

- [ ] Work broken into bounded tasks
- [ ] Dependencies identified
- [ ] Every task has acceptance criteria
- [ ] Validation method defined

**Gate 3:** [ ] PASS

---

## 4. Authority Lease

- [ ] Allowed actions documented
- [ ] Approval-required actions documented
- [ ] Forbidden actions documented
- [ ] Protected files/systems documented

**Gate 4:** [ ] PASS

---

## 5. Repository Inspection

- [ ] Current state inspected
- [ ] Existing errors identified
- [ ] Uncommitted work identified
- [ ] Test/build commands identified
- [ ] Deployment configuration understood

**Gate 5:** [ ] PASS

---

## 6. Implementation

| Task | Status | Verification | Evidence | Notes |
|---|---|---|---|---|
| | | | | |

**Gate 6:** [ ] PASS — every unit satisfied its acceptance criteria and produced supporting evidence

---

## 7. Verification

- [ ] Targeted tests complete
- [ ] Regression checks complete
- [ ] Acceptance criteria checked
- [ ] Independent verification performed where practical
- [ ] Unverified claims documented

**Gate 7:** [ ] PASS

---

## 8. Evidence

- [ ] Evidence ledger current
- [ ] Critical claims linked to evidence
- [ ] Failed checks preserved
- [ ] Known limitations documented

**Gate 8:** [ ] PASS

---

## 9. Commit

- [ ] Diff reviewed
- [ ] Intended files only
- [ ] No secrets detected
- [ ] Relevant checks passing
- [ ] Project artifacts updated

**Gate 9:** [ ] PASS

---

## 10. Pre-Deployment Gate

_If the project never deploys anywhere, mark every item below N/A and skip to §13._

- [ ] Build passes
- [ ] Tests pass
- [ ] Type checks pass (N/A if not applicable)
- [ ] Lint passes (N/A if not applicable)
- [ ] Migrations reviewed (N/A if not applicable)
- [ ] Environment variables present
- [ ] Secrets not exposed
- [ ] Authentication works
- [ ] Authorization works
- [ ] Payments tested (N/A if not applicable)
- [ ] Backups verified
- [ ] Observability active
- [ ] Rollback path documented

Required artifact: `.mvce/DEPLOYMENT-CHECKLIST.md`

**Gate 10:** [ ] PASS — explicit GO decision recorded

---

## 11. Deployment

_No gate on this phase — record the release. N/A for local-only projects._

- [ ] Deployment target recorded
- [ ] Version or commit recorded
- [ ] Migration state recorded
- [ ] Deployment identifier recorded
- [ ] Deployment outcome recorded

_If deployment fails, go to §13 Recovery._

---

## 12. Production Verification

_N/A for local-only projects. Rule: local success does not satisfy this gate._

- [ ] Application loads
- [ ] Critical user path works
- [ ] Authentication works (if present)
- [ ] Critical write operations work
- [ ] Errors are not spiking
- [ ] External integrations respond
- [ ] Expected version is running

**Gate 12:** [ ] PASS — release is complete only after production verification succeeds

---

## 13. Recovery

Required artifact: `.mvce/RECOVERY-PLAN.md`

- [ ] Further uncontrolled changes stopped
- [ ] Failure characterized
- [ ] Relevant evidence preserved
- [ ] Last known-good state identified
- [ ] Repair vs. rollback decided
- [ ] Bounded recovery executed
- [ ] Restored behavior verified
- [ ] Cause and resolution documented

---

## 14. Maintenance

_Maintenance work re-enters the same MVCE loop as feature work._

- [ ] Dependency health checked
- [ ] Security advisories reviewed
- [ ] Expired credentials rotated
- [ ] Failing jobs addressed
- [ ] Broken integrations fixed
- [ ] Test drift corrected
- [ ] Architecture drift corrected
- [ ] Data growth reviewed
- [ ] Backup validity confirmed
- [ ] Cost growth reviewed
- [ ] Observability gaps closed
- [ ] Documentation drift corrected

---

## 15. Project Closeout

- [ ] Current specification filed
- [ ] Final acceptance status recorded
- [ ] Known limitations listed
- [ ] Architecture summary filed
- [ ] Deployment state recorded
- [ ] Recovery instructions filed
- [ ] Unresolved risks listed
- [ ] Evidence summary filed
- [ ] Next recommended actions listed

_A project is closed because evidence supports completion, not because activity stopped._

---

## Current Decision

**Next action:**  
**Blocked by:**  
**Human approval required:** YES / NO  
**Last verified state:**  
