---
title: Identifier consistency validation — proposed requirement
page_type: engineering-data-contract
page_status: draft
---

# Identifier consistency validation — candidate v0.1

**Status:** Draft proposal for pilot review. Builds on the identifier invariants in the [canonical model](../ontology/canonical-model/README.md).

## Requirement

Every name and tag for a System, Equipment, Device and Point is validated against **one source of truth** wherever it appears, through the whole project life: engineering registers, submittal drawings, the logic handoff, controller programs, SCADA configuration and closeout records.

- The **project equipment/device/points register (EDP)** is the source of truth for tags and names. Each row carries the identifiers that apply to it: internal ID, source document tag, signal name, operational / SCADA name, network address or object name.
- Every other artifact **references** those identifiers. It does not define them. A name that appears in an artifact but not in the EDP, or differs from the EDP, is a finding.
- A naming change is made in the EDP first and logged; downstream artifacts are then updated and re-checked. An artifact is never corrected by editing it alone (consistent with "never edit a generated view as an alternate source of truth").
- The convention for building names (separators, prefixes, owner naming standards) is recorded once, by the project, against the EDP. Validation checks artifacts against the EDP values, not against the convention.

## Precondition

**Validation is not performed until the EDP has the Source Document Tag and the Operational / SCADA Name filled in** for every row in scope. A blank, placeholder (`TBD`, `##`) or unresolved value is not a valid reference.

- Before running the checks, list the EDP rows missing either value. Those rows are open items, not passes.
- Partial validation is allowed only for the rows that meet the precondition, and the record says which rows were excluded and why.
- A row whose source document has no tag records that fact (with the provisional tag assigned and its open item), rather than leaving the field blank.

## What each check confirms

| Check | Confirms |
|---|---|
| Presence | Every EDP identifier that an artifact is required to show appears there |
| No orphans | Every identifier in an artifact exists in the EDP |
| Exact match | Spelling, case and separators match the EDP value |
| Correct pairing | A device tag and its signal names appear together as the EDP pairs them (no point shown on the wrong device) |
| Removed scope | Identifiers retired in the EDP no longer appear in active artifacts |
| Revision trace | The check records the EDP revision and the artifact revision compared |

## Artifacts in scope

At minimum: the project register (PER) records, issues and RFIs that cite tags; submittal drawings; the engineering-to-logic handoff; controller programs and object lists; SCADA / front-end point configuration; commissioning and closeout records. Each organization profile names the specific places to look (for example, the [Klutch validation gates](../org-standards/klutch/validation.md)).

## Limits

A programmatic check confirms only that identifiers agree with the EDP. It does not confirm that the EDP itself is complete or correct against the source documents; that is the M2 independent completeness review.

## Open questions

- Whether the EDP template needs a dedicated "retired identifier" column or status to support the removed-scope check.
- How drawing text is extracted for checking (PDF text, DXF attributes) and how reliably.
