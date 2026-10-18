---
title: Controls Engineering Canonical Model Vocabulary
page_type: model-element
page_status: draft
---
# Controls Engineering Canonical Vocabulary — proposed

This is a **semantic contract**, not yet a released XML/JSON schema or workbook migration. A project's named canonical editable registers are authoritative. Serialize/export XML/JSON only as the chosen project's exchange representation unless explicitly designated as the editable primary record.

| Object | Meaning | Essential relationships |
|---|---|---|
| Project | Bounded engineering contract/workspace | owns source registry, records, scope and configuration history |
| System | Functional System of Interest / associated functional assembly | comprises equipment, dependencies, subsystem/interface boundaries |
| Equipment | Physical assembly such as AHU, VAV box, packaged plant, DDC panel | identified independently; may contain equipment and devices via physical Parent ID |
| Component (optional) | Mechanical/functional constituent (fan, coil, valve) when needed | belongs to equipment/system; has attached devices |
| Device | Physical article (sensor, actuator, controller, module, switch, VFD) | physically contained/associated, may supply points, may cite WikiJS product facts |
| Point | One named monitored/controlled signal or semantic variable | related to device/system, implementation signal/channel and logic function; no required one-to-one hardware I/O assumption |
| Interface | Boundary-crossing exchange (signal, protocol, power, mechanical or responsibility handoff) | endpoints and direction, responsibilities and evidence |
| Dependency | Functional service/logic requirement between elements | source/target, nature and conditions; not physical parenthood |
| Scope / Work Action | In-scope status, trade responsibility and what changes | independent of object existence, with source/decision |
| Source Reference | Traceable original evidence with issue and revision | attaches to facts and consequential decisions |
| Open Item / Finding | Unresolved source, interpretation, selection, coordination or validation concern | affected IDs, owner, `resolve_by`, evidence and resolution |
| Decision / Assumption | Scoped reviewed conclusion vs provisional input | source/evidence, responsible authority and configuration impact |
| Engineering Acceptance | Protect a selected derived configuration from silent agent/optimizer change | target IDs and optionally attributes/geometry, human basis |
| Snapshot / Baseline | Immutable selected project state, optionally designated comparison reference | source and register revisions, affected work products |

**Identifier invariants:** internal record ID is not the same as printed equipment tag, source display label, point name, PDF annotation `/NM`, network address or panel terminal name. Alias mappings must preserve historical identity. Physical containment, functional service, control dependency, network connectivity and contractual responsibility are separately typed relationships.

**Existing and interface work:** an existing VAV box may be modeled as Equipment even when KIS only rewires its existing Device/controller or integrates its data. An external packaged unit may be represented as context/interface without inventing internals. Hardware capabilities remain with referenced physical device knowledge in WikiJS.

**Migration warning:** legacy `bas-logic-gen` represents one AHU/VAV unit as `system` and generally `system → component → device → point`; the new hierarchy **does not automatically relabel those historical objects**. Design a reversible ID/relationship map and test against real project takeoffs before changing executable schemas or legacy agent instructions.

**Validation roadmap:** source coverage; unique stable IDs; source evidence & revision; scope responsibility cross-references; no double-counted physical devices/I/O; physical Parent references without cycles; nonphysical relationships do not imply containment; conflicting fact provenance; accepted attribute holds; snapshot reproducibility; changed-source impact checks. No production validator is asserted here.
