# Controls Engineering — Agent Entry Point

Applies to Claude, ChatGPT, Codex and other agents using this repository.

## Authority and purpose

Read the parent [KIS Systems Engineering Framework v1.0](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/governance-and-doctrine/systems-engineering-framework-v1.md) and [repository boundaries](docs/governance-and-doctrine/repository-boundary.md) before design work.

This package owns **controls engineering**. It does not generate controller code; `kissolutions/bas-logic-gen` owns implementation logic, patterns, archetypes and platform bindings. The engineering-to-logic boundary is a reviewed, versioned handoff; never silently update an issued engineering input in response to programming convenience.

The initial lifecycle documents are **proposals for pilot review**, not automatic authority to reclassify an existing project's records or rewrite approved designs. Preserve existing project decisions and source IDs during migration.

## First-pass workflow

1. Identify project storage and authoritative working registers. Register contract/client sources, versions and excluded materials; identify vendor documentation separately.
2. Extract and reconcile contractual scope, responsibilities and interfaces before asserting what KIS will build.
3. Independently enumerate systems, equipment assemblies, devices, points, dependencies and existing/new work actions from the source; preserve prior project markups/workbooks as prior-work evidence.
4. Verify completeness against sources through a separate review pass. Record unresolved source conflicts, omissions and unknowns with owner and `resolve_by`.
5. Present a consolidated M1/M2 owner-review package. Approved attributes/geometry are protected; do not infer universal acceptance from a milestone or snapshot.
6. Derive requirements and narrative, then develop design architecture and coordinated outputs. Distinguish source-prescribed behavior from proposed and externally approved changes.
7. Generate downstream schedules, diagrams, and programming handoff from authoritative project records, preserving version and traceability.

## Non-negotiable controls

- Do not fabricate devices, points, equipment, capacities, code applicability, sequences or scope obligations to make a gate pass.
- Do not call an unreviewed inference a source fact, or treat silence in one document as confirmed absence.
- An existing device within a modeled system can be interface-only or outside implementation scope. Scope is a separate dimension from modeled existence.
- Distinguish **System** (functional context), **Equipment** (physical assembly), **Device** (physical article), **Point** (signal), **Interface** (boundary crossing) and optional **Component** (mechanical/functional constituent).
- Physical containment / Parent ID, served-by dependencies, network connectivity and contract responsibility are separate relationships.
- Keep internal IDs stable. Source tags, displayed labels, annotations and vendor models are different identifiers.
- Null/unresolved does not mean zero, none, excluded, or accepted. Preserve both conflicting source values and revisions.
- Never edit a generated view as an alternate source of truth. Owner corrections must return into the explicitly designated canonical project records.
- Record human acceptance, snapshots and configuration baselines separately. An accepted location may be held while other equipment attributes remain provisional.
- Independent review checks source completeness; programmatic validators check only stated input data conditions.
- No client documents, sensitive project data, credentials or client markups in this repository; keep approved anonymized/synthetic precedents only.

## Relevant pages

- [Lifecycle](docs/design-playbooks/controls-engineering-lifecycle.md)
- [M1 Source & Scope](docs/design-playbooks/processes/m1-source-scope-intake.md)
- [M2 Inventory & Reconciliation](docs/design-playbooks/processes/m2-engineering-inventory.md)
- [Canonical model](docs/ontology/canonical-model/README.md)
- [Logic handoff](docs/interfaces/engineering-to-logic-handoff.md)
- [Legacy migration](docs/governance-and-doctrine/legacy-bas-playbook-migration.md)

Treat all M1–M6 labels in these initial files as **provisional mappings**, pending pilot/owner review. Do not overwrite the independently versioned legacy controls stages in bas-logic-gen.
