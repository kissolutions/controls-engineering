---
title: Controls Engineering Lifecycle
page_type: playbook
page_status: draft
ai_role: workflow_router
---
# Controls Engineering Lifecycle — proposed v0.1

**Proposal only.** Aligned to [KIS Systems Engineering Framework v1.0](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/governance-and-doctrine/systems-engineering-framework-v1.md). The parent defines Phases, Processes, Milestones and Work Products as distinct concepts. The M1–M6 names below await pilot approval; existing bas-logic-gen stages 1–19 remain operative in legacy workflows until explicitly migrated.

| Phase | Proposed milestone/review | Work products |
|---|---|---|
| Phase 1 Intake | **M1 Source & Scope** | Source register, revisions, contract scope/responsibility matrix, context/interfaces, open items, derived scope navigator/infographic |
| Phase 1 Intake | **M2 System / Equipment / Device / Point Inventory** | Independently reconciled physical/functional inventory, source points, existing-versus-new actions, draft I/O, findings |
| Phase 2 Design Basis & Requirements | **M3 Functional Design Basis** | Applicable requirements/constraints, source SOO, proposed/adopted controls narrative, decisions/RFIs |
| Phase 3 Design Development | **M4 Architecture & Detailed Design** | Field selections; controller/panel/I/O and network assignment; diagrams, schematics, layouts, physical locations; design verification |
| Phase 4 Coordination & Delivery | **M5 Submittal & Release** | Coordinated package, external review, issue revision, configuration comparison/change impact |
| Phase 5 Verification & Closeout | **M6 Commissioning & Closeout** | Programming handoff/return, test results, site deficiencies, as-built reconciliation, final records |

A review gate is **not** the process that creates its work. A source reconciliation or change impact process may run repeatedly. Intermediate checkpoints are allowed; M2 factual verification need not block provisional controller sizing, and drafting logic may start at risk when its dependencies and revision are clear.

## Concurrency and dependencies

Following source and scope intake, work may fork into narrative, networking, controller/I/O sizing, physical markup, controls diagrams, panel layout and wiring diagrams. Tracks converge for external submittal review. Distinguish internal review from external approval. Logic generation is a **different package/team** and may consume a provisional engineering handoff only if the at-risk state, source revisions and resync obligations are explicit.

## Gate invariants

1. Source facts have a specific locator and revision or explicit owner-provided evidence; unknown is not zero.
2. Scope responsibility and physical modeling are separate. A modeled external interface is not automatically our equipment.
3. Stable internal IDs survive label/markup revisions; physical Parent ID is not the same as control relationship or scope responsibility.
4. Review unresolved items by `resolve_by`; do not require an arbitrary early close or silently carry a blocker past its gate.
5. Independent completeness review must compare to actual contract/source documents rather than checking only entered register rows.
6. Engineering Acceptance, Snapshot and Configuration Baseline are separate actions. An accepted owner location must not be silently moved by regeneration.
7. Source change after a gate triggers a targeted diff/impact assessment: systems/equipment/devices/points, I/O, narrative, network, panel, drawings, tests and handoffs as applicable.
8. A passed automated check is not professional approval, construction acceptance, verification of source completeness or commissioning.

## Processes

- [M1 Source & Scope Intake](processes/m1-source-scope-intake.md)
- [M2 Engineering Inventory](processes/m2-engineering-inventory.md)

Later M3–M6 processes, process IDs and machine-readable schemas remain to be drafted and tested with real-project work.
