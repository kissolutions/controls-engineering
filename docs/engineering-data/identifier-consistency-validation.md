---
title: Identifier consistency validation — proposed requirement
page_type: engineering-data-contract
page_status: draft
---

# Identifier consistency validation — candidate v0.1

**Status:** Draft proposal for pilot review. Builds on the identifier invariants in the [canonical model](../ontology/canonical-model/README.md).

## Requirement

Every name and tag for Equipment, Devices and Points is validated against **its authoritative register** wherever it appears, through the whole project life: engineering registers, submittal drawings, the logic handoff, controller programs, SCADA configuration and closeout records.

### Ownership

| Information | Authoritative location |
|---|---|
| Systems, scopes, sources, issues, RFIs and decisions | PER (canonical model ownership) |
| Equipment, devices, points and their approved engineering names | EDP |
| Original source spelling of a tag | EDP Source Document Tag, linked to its source; preserved as observed |
| Approved downstream spelling or abbreviation (for example a SCADA prefix omitted on drawings) | An explicit naming mapping recorded by the project |
| Actual installed or programmed condition | Verification evidence, reconciled with the approved design |

- **Stable IDs carry identity; tags are attributes.** A rename (VSD-1 to VFD-1) changes the tag on the same internal ID; it never creates a new device.
- **Conflicting source tags are preserved** as source observations, each with its source, and resolved by an open item; the register is not rewritten to look consistent.
- Every other artifact **references** EDP identifiers. A name in an artifact that is not in the EDP, or differs from it after the naming mapping is applied, is a finding.
- A naming change is made in the EDP first and logged; downstream artifacts are then updated and re-checked. An artifact is never corrected by editing it alone.
- **Removed scope** leaves the current deliverables but keeps its history: the EDP row stays with a retired / removed disposition and the change that removed it.

## Field applicability

Which identifier fields a row must have depends on what the row is. A field marked "required" that is blank or a placeholder (`TBD`, `##`) is a finding. A field marked "n/a" records the reason.

| Row class | Source Document Tag | Operational / SCADA Name | Notes |
|---|---|---|---|
| Field device or point with a source tag | Required | Required if it has a SCADA point | |
| New Klutch device with no source tag (for example a new panel or relay) | Provisional tag, with "no source tag" recorded | Required if it has a SCADA point | |
| Interface-only device with no point | Required if the source tags it | n/a: no point | |
| Internal software value not exposed | n/a | n/a, unless it meets the naming page's owner-standard rule | |
| Reserved input (device not yet confirmed) | Provisional | Required | Disposition required before issue |

### Missing names do not stop other checks

- Missing required names **block a clean identifier-validation result** for the affected rows, and are listed as open items.
- All other checks still run on every row: duplicate terminals, wrong device / point pairing, BOM quantity, removed-scope sweep.
- The validation record states which rows were incomplete and which checks were therefore not conclusive.

## Artifacts in scope

At minimum: the project register (PER) records, issues and RFIs that cite tags; submittal drawings; the engineering-to-logic handoff; controller programs and object lists; SCADA / front-end point configuration; commissioning and closeout records. Each organization profile names the specific places to look (for example, the [Klutch validation gates](../org-standards/klutch/validation.md)).

## Limits

A programmatic check confirms only that identifiers agree with the EDP. It does not confirm that the EDP itself is complete or correct against the source documents; that is the M2 independent completeness review.

## Open questions

- Whether the EDP template needs a dedicated "retired identifier" column or status to support the removed-scope check.
- How drawing text is extracted for checking (PDF text, DXF attributes) and how reliably.
