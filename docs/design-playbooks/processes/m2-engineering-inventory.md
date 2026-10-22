---
title: M2 Engineering Inventory and Reconciliation
page_type: playbook
page_status: draft
---
# PROC-CTL-M2-INVENTORY — v0.1 (proposed)

**Purpose:** independently establish project System, Equipment, Device, Point and interface completeness from source documents while distinguishing existing/modified/new work.

**Prerequisites:** registered source set, M1 scope boundaries and review open items (M1 acceptance if required by project gate). A preliminary engineering inventory may be built at risk before the M1 gate.

**Method**

1. Identify each functional System and physical Equipment assembly with immutable internal ID, source tag, description, source/revision, existing-state evidence, relevant scope dispositions, named responsibilities and work actions.
2. Capture physically contained/associated Devices: sensors, controllers, actuators, VFDs, switches, module instances and panel articles as applicable. Record optional physical Parent ID; separate containment from attachment, controls, network, service and responsibility links.
3. Capture Point records as distinguishable physical/digital/logical signals where contract detail allows. Preserve source point names, signal direction/type and the fact/uncertainty of the physical I/O channel. Network-exposed points are not implicitly separate hardwired channels.
4. Model only needed external system context and interfaces. A point crossing scope requires source/destination/direction/function evidence and unresolved status where the other side is unknown.
5. Record candidate selections as **engineering proposals**, not source facts; do not silently invent expected sensors/points to match typical playbooks. Track named reserved I/O, generic spare headroom, and provision-only hardware distinctly for later design.
6. Reconcile *prior* PM/PE workbook rows, existing I/O lists, markups, RFIs and other partially-complete deliverables. Preserve stable IDs, source tags and PDF annotation identifiers; a mismatch becomes a finding, not an automatic overwrite.
7. Have a separate agent/pass enumerate systems/equipment/devices/points/interfaces from the source set, independently of the working register. Compare omissions, false positives, duplicate counts, aliases, signal inconsistencies, parent mappings, cross-document contradictions, missing source references, and M1 scope compatibility.
8. Run available structural/schema checks only against what they actually validate. Return a consolidated owner review package containing draft schedules/marked plans, discrepancies, unresolved owner decisions and provenance.

**Work products:** System and Equipment schedules, Device and Point records, source I/O inventory, field interface and dependency records, existing/new action matrix, independent completeness findings, review-ready views and accepted decisions.

**Gate:** source-observed scope is accounted for, independent comparison reviewed, blockers resolved or explicitly carried with defensible `resolve_by`, object identities stable, and human M2 approval scope recorded. Selection and architecture approvals are separate and can remain provisional.

**Don't assume:** a mandatory room register; every modeled article must be in construction scope; every physical device has one I/O point; source points are always an I/O card channel; a controls diagram exhausts the complete project; a marked-up PDF is inherently editable or reliably round-trippable.

**Process evidence:** immutable process/version, source revision, affected IDs, authoritative register revision, discrepancies, reviewer and explicit completion limitations.

## Standard workbook artifact

The owner-accepted blank template for Equipment / Device / Point registers is [`templates/equipment-device-points/Equipment_Device_Points_Template_v1.0.xlsx`](../../../templates/equipment-device-points/Equipment_Device_Points_Template_v1.0.xlsx). Instantiate it as a **separate project deliverable** from the [`PROJECT_PER_v1.1.xlsx`](../../../templates/project-engineering-register/PROJECT_PER_v1.1.xlsx). Preserve stable `E-##`, `D-##`, and `P-##` identities and explicit PER source/scope/WP/issue references. Scope or work-package association is not assumed from physical parentage. Source evidence, linked requirements, decisions and unresolved items remain authoritative in the project's designated registers; do not create competing project issues inside the blank inventory template. Project-specific versions require owner verification and acceptance distinct from template acceptance.
