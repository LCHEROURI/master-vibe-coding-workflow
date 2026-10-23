# Acceptance criteria

Written before application implementation. These are prospective obligations;
results belong in VERIFICATION.md and EVIDENCE-LEDGER.md, not retroactive edits
to the expected behavior. All criteria are required for the local sample.

| ID | Given / when | Required observable result | Planned verification |
|---|---|---|---|
| AC1 | An absent database; list, then add a title and list in new processes | Empty array first; positive stable ID; saved title and `done: false` | CLI subprocess tests and smoke transcript |
| AC2 | Add two tasks, including Unicode and SQL-like punctuation | Distinct IDs; insertion/ID order; exact trimmed titles survive storage | CLI subprocess test |
| AC3 | Complete the first of two tasks twice, then list | Both calls succeed; only the selected task is done | CLI subprocess test and smoke transcript |
| AC4 | Add a whitespace-only title after a valid task | Exit 2; stderr `error:`; original rows unchanged | CLI subprocess test |
| AC5 | Complete an unknown, zero, negative, or noninteger ID | Nonzero exit with `error:`; original rows unchanged | CLI subprocess test |
| AC6 | Use an absent parent directory or a corrupt database | Exit 1; stderr `error:`; no traceback; corrupt file preserved | CLI subprocess tests |
| AC7 | Back up a stopped local database, modify it, then restore the copy | Listing matches the original snapshot after restore | CLI subprocess recovery test and smoke transcript |
| AC8 | Read the example as a workflow demonstration | Completed artifacts; phase-by-phase walkthrough; real command outputs; explicit production NO-GO | Document review and scope/link checks |
