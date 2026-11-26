---
title: Klutch Revision Numbering
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Revision Numbering

Klutch engineering registers (PER, EDP) and other engineering working documents use software-style revision numbers: **MAJOR.MINOR.BUILD**. Drawings follow their own revision system (see Drawings below).

| Part | Increments when | Example |
|---|---|---|
| **MAJOR** | A major milestone: the design passes a major review, or the requirements are judged met and the set is packaged for others to use as a complete set based on current conditions | First submittal: `0.x.x` → `1.0.0` |
| **MINOR** | A function is worked out | "We figured out the damper setup": `1.1.x` → `1.2.0` |
| **BUILD** | Each distinct handoff between the agent and the owner | `1.2.0` → `1.2.1` |

## Rules

- **The owner decides how and when to uprev.** The agent proposes a MAJOR or MINOR uprev and does it only when the owner says so. The BUILD number goes up by one at each distinct agent / owner handoff unless the owner says otherwise.
- **Before the first submittal**, work is `0.x.x`. When the `0.x.x` work is accepted as the first submittal, everything is uprevved together to `1.0.0`.
- **MAJOR and MINOR stay aligned** across the PER and EDP. BUILD may differ between them.
- BUILD resets to 0 after a MAJOR or MINOR uprev; a MAJOR uprev also resets MINOR to 0.
- An uprev records a revision number only. It is not human acceptance, a snapshot or a configuration baseline; those are recorded separately in the PER.
- Every uprev gets a change log entry naming what changed.
- **Release manifest:** every issue to others (a submittal, a logic handoff) records the exact compatible set: PER, EDP, drawing transmittal revision and logic handoff revision. Matching version numbers alone do not establish compatibility.

## Drawings

- The drawing set does **not** carry MAJOR.MINOR.BUILD. CAD follows its own revision system.
- **Every transmittal is a drawing revision** (Rev 1, Rev 2, ... with a description such as INITIAL SUBMITTAL). The transmittal is currently the only client-facing, revision-controlled document.
- The PER, EDP and programming logic hold enough information to rebuild the drawings almost from scratch; the registers' revision numbers carry the engineering history, the drawing revision carries the client-facing issue history.
- Record which register revision each drawing transmittal was built from (PER SOURCES entry for the drawing set, or the change log).

## Open questions (owner to confirm)

- File naming: for example `<PROJECT>_PER_v1.2.3.xlsx`.
