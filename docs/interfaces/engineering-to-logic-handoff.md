---
title: Engineering-to-Logic Handoff
page_type: governance
page_status: draft
---
# Engineering-to-Logic Interface — candidate v0.1

**Producer:** Controls Engineering team/package. **Consumer:** separate BAS Logic Generation team/package. A team may begin at risk with draft material, but must identify exactly which revision it consumed.

## Required handoff information

- Package and project ID, engineering model/register revision, relevant immutable source revisions, snapshot/baseline ID if set, issue status (`draft_at_risk`, `reviewed`, `issued`, or an explicit equivalent).
- Stable System, Equipment, Device and Point identities with source/name aliases; scope and work-action flags; control/monitoring interface semantics; known network/hardwired assignments, scaling/units/ranges and unresolved fields.
- Reviewed source SOO and engineering controls narrative, including named sequences/functions, operating modes, alarms/trips/safeties, permissives and interlocks, operator overrides and failure-state/first-out behavior where applicable.
- Engineering limits/constraints (physical devices, controller I/O, selected platform, external interfaces, applicable safety review requirements) and owned open items with their `resolve_by` gate.
- Specific requirements, design decisions and acceptance holds that software implementation must preserve, plus testable acceptance criteria and known exceptions.

## Returned results

Logic package returns code/build revision and selected platform, pattern/archetype bindings, mapping from functions/points to program artifacts, test results, unsupported or contradictory requirements and structured **engineering change requests**. A change request does not itself amend the engineering source or narrative.

## Resynchronization

If the engineering team revises device/signal semantics, I/O assignment, sequencing, alarms/safeties, scope or network interface after a handoff, compare changed stable IDs and revs; flag affected pattern bindings, code blocks, test plans and runtime configuration; issue a revised handoff with disposition. Preserve previous handoff artifacts for audit and rollback.

**Not in scope yet:** a finalized wire format, generated programming API, comprehensive safety case, code generator integration or automated cross-repo reconciliation. Establish schema only after a real controls pilot establishes stable field meanings.
