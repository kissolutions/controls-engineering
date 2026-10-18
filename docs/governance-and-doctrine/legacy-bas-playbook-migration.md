---
title: Legacy BAS Lifecycle Migration
page_type: governance
page_status: draft
---
# Migration from bas-logic-gen — proposed plan

The current `kissolutions/bas-logic-gen` [Controls Engineering Playbook](https://github.com/kissolutions/bas-logic-gen/blob/main/docs/design-playbooks/controls-engineering-playbook.md) currently covers 19 stages, parallel submittal tracks and logic generation. Its `CLAUDE.md` entry point retains a simplified older stage summary. Do not delete, silently overwrite or immediately redirect it.

## Preserve

- Source intake, system identification, takeoff and field device selection experience.
- Independent model checkpoint and source/RFI evidence.
- At-risk controller rough-in, reserve/spare/provision-only hardware distinctions and final I/O allocation.
- Parallel controls narrative, networking, floor plans, controls diagrams, panel layouts, schematics and external submittal review.
- `resolve_by` issue tracking and engineering change G6 branches.
- Parallel pattern selection, archetype binding, program architecture, assembly, impact assessment and logic validation on the **logic** side.

## Resolve before an operative migration

1. Map legacy **System-as-equipment** IDs and `Component → Device → Point` semantics to new System/Equipment/Component/Device/Point without inventing physical objects or losing references.
2. Distinguish a contract scope fact from an approved vendor product capability and from an existing field observation. Refine precedence rules by subject; preserve both conflicting claims.
3. Introduce M1 scope/work-action/boundary and M2 independent inventory verification before trying to formalize architecture.
4. Resolve default engineering authority: project workbook/register as editable master, XML exchange unless explicitly authoritative. Avoid two masters.
5. Preserve accepted per-attribute geometry/device/I/O decisions and full baseline states distinctly.
6. Specify actual M1/M2 templates and verify returned PDF annotation stability before advertising production round trips.
7. Separate controller/network architecture and engineering narratives from behavior/code implementation in the logic package, with explicit versioned handoff and feedback mechanism.
8. Test against a partially completed real controls project (M95 Life Safety proposed) using its known source/contract folder and trimmed PM TRACKER. Do not upload private project documents to GitHub.

## Controlled migration

- Keep this new repository's initial rules as **draft proposals**.
- Capture a baseline of the legacy engineering content and a reversible mapping table.
- Execute M1/M2 pilot and revise vocabulary based on source evidence and owner decisions.
- Introduce versioned schemas/checks with synthetic failure and regression fixtures.
- Only after acceptance, update legacy `bas-logic-gen` agent entry points and annotate relocated pages with link/redirect. Preserve its logic-specific guidance and upstream engineering contracts.
- Document package compatibility/release versions rather than creating a second source of truth.

**No migration or schema conversion is asserted complete by repository initialization.**
