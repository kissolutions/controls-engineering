---
title: Organization Standards Profiles
page_type: governance
page_status: draft
---

# Organization Standards Profiles — proposed v0.1

The framework defines **what** controls engineering produces and **how it is verified**. An **organization standards profile** defines **how one organization's deliverables look and are named**: drawing set structure, sheet content, naming, narrative format, panel and hardware conventions, and house review gates.

Profiles are versioned and owned independently of the framework. A framework change does not rewrite a profile; a profile update does not change KIS doctrine.

| Profile | Path | Owner | Status |
|---|---|---|---|
| Klutch Controls | [`klutch/`](klutch/README.md) | Klutch PE | draft |

## Loading rule

1. At project intake, the project declares its profile and version (for example `klutch v0.1`) in the PER SOURCES or project manifest.
2. Agents read the parent framework, then this package, then the declared profile.
3. A profile may add conventions and stricter checks. It may not redefine framework terms, IDs or acceptance/baseline rules.

**Framework invariants** cannot be overridden by a profile, a client convention or a precedence override: canonical terms and object types, stable internal IDs, register ownership, and the acceptance / snapshot / baseline rules. Everything else is a convention and can be overridden as below.

## Precedence

Default order, highest first:

1. Contract documents and the project specification
2. Client / owner standards (for example a campus BAS standard)
3. Organization standards profile
4. Framework defaults

The order is a default, not a law. Any convention (not a framework invariant) can be overruled for a project, system, equipment item or device by a **precedence override** record. Specifications are sometimes knowingly set aside when everyone agrees they are wrong but nobody will run the update process; the override records that agreement instead of leaving it implicit.

### Precedence override record

Recorded as a PER RECORDS row (Record Type `Decision`, statement beginning `Override:`) until the template carries a dedicated field set.

| Field | Content |
|---|---|
| Override ID | Stable ID (record ID) |
| Rule overridden | The specific clause, standard section or default, with source ID and locator |
| Prevailing rule | What applies instead, with its source ID |
| Scope | Project, system, equipment, device or point IDs it applies to; never implied wider |
| Reason | Why the higher-ranked rule is set aside |
| Approval authority | Who has the authority to approve this departure (for a client requirement, the client or its delegate; Klutch alone cannot waive a client requirement) |
| Agreed by | Who participated in the agreement (name, role, organization) and how (meeting, email, RFI answer) |
| Evidence | Source ID of the agreement |
| Date | When agreed |
| Review / expiry | When or on what event it is re-checked (next spec revision, closeout) |
| Status | proposed / agreed / withdrawn |

Rules:

- An override without evidence of agreement **by the approval authority** is `proposed`, and the higher-ranked rule still governs.
- The record documents a departure and its authorization; the record's existence does not itself authorize the departure.
- Silence is not an override. A deliverable that departs from a higher-ranked rule without an agreed override is a finding.
- Overrides are scoped; one override never generalizes to other projects or into the profile. Repeated overrides of the same profile rule are a signal to change the profile.
