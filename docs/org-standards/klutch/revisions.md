---
title: Klutch Revision Numbering
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Revision Numbering

Klutch deliverables (PER, EDP, drawing sets and other engineering documents) use software-style revision numbers: **MAJOR.MINOR.BUILD**.

| Part | Increments when | Example |
|---|---|---|
| **MAJOR** | A major milestone: the design passes a major review, or the requirements are judged met and the set is packaged for others to use as a complete set based on current conditions | First submittal: `0.x.x` → `1.0.0` |
| **MINOR** | A function is worked out | "We figured out the damper setup": `1.1.x` → `1.2.0` |
| **BUILD** | Each distinct handoff between the agent and the owner | `1.2.0` → `1.2.1` |

## Rules

- **The owner decides how and when to uprev.** The agent proposes a MAJOR or MINOR uprev and does it only when the owner says so. The BUILD number goes up by one at each distinct agent / owner handoff unless the owner says otherwise.
- **Before the first submittal**, work is `0.x.x`. When the `0.x.x` work is accepted as the first submittal, everything is uprevved together to `1.0.0`.
- A MINOR uprev resets BUILD to 0; a MAJOR uprev resets MINOR and BUILD to 0. *(To confirm.)*
- An uprev records a revision number only. It is not human acceptance, a snapshot or a configuration baseline; those are recorded separately in the PER.
- Every uprev gets a change log entry naming what changed.

## Open questions (owner to confirm)

- How the drawing title block revision (for example "Rev 1 INITIAL SUBMITTAL") relates to `MAJOR.MINOR.BUILD`: does the title block show only MAJOR with a description, or the full number?
- File naming: for example `<PROJECT>_PER_v1.2.3.xlsx`.
- Whether the PER, EDP and drawings share one revision number or each keeps its own.
