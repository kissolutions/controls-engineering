# KIS Controls Engineering

**Repository:** `kissolutions/controls-engineering`  
**Status:** Architecture scaffold / proposed domain lifecycle — not an approved production process

This repository defines **controls engineering**, from contractual source intake and scope identification through equipment/device/point inventory, design basis, functional narrative, controller and network architecture, submittals, field verification, and closeout.

It does **not** own program logic patterns or generation of controller code. Those are the responsibility of the sibling `kissolutions/bas-logic-gen` team and package.

## Package context

| Source / package | Authority |
|---|---|
| [knowledgebase_wikijs](https://github.com/kissolutions/knowledgebase_wikijs) | Shared KIS engineering framework, cross-domain vocabulary, knowledge taxonomy, generic processes and authoritative physical device facts |
| **controls-engineering** (this repository) | Domain-specific controls lifecycle, canonical engineering data contracts, work products, intake/verification processes, review gates and engineering-to-logic interface |
| [bas-logic-gen](https://github.com/kissolutions/bas-logic-gen) | Vendor-neutral behavior patterns, platform code archetypes, program construction, logic verification and tests |
| [lv-lighting-design](https://github.com/kissolutions/lv-lighting-design) | Independent LV lighting domain; a beta-tested example of source reconciliation, physical-first extraction, editable review, accepted configurations and milestone packages |

The parent [KIS Systems Engineering Framework v1.0](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/governance-and-doctrine/systems-engineering-framework-v1.md) supplies the five-phase lifecycle, process/work-product/milestone distinction, evidence and requirements terminology, and snapshot/acceptance/baseline contracts.

## Start here

1. [Agent entry point](CLAUDE.md)
2. [Repository boundaries](docs/governance-and-doctrine/repository-boundary.md)
3. [Domain package contract](docs/governance-and-doctrine/domain-package-contract.md)
4. [Controls engineering lifecycle — proposed](docs/design-playbooks/controls-engineering-lifecycle.md)
5. [Canonical engineering vocabulary — proposed](docs/ontology/canonical-model/README.md)
6. [M1 Source & Scope Intake](docs/design-playbooks/processes/m1-source-scope-intake.md)
7. [M2 Engineering Inventory](docs/design-playbooks/processes/m2-engineering-inventory.md)
8. [Engineering-to-logic handoff](docs/interfaces/engineering-to-logic-handoff.md)
9. [Migration plan](docs/governance-and-doctrine/legacy-bas-playbook-migration.md)

## Working principles

- **Facts before engineering proposals:** record exactly what the source establishes; keep unsupported values unresolved, not inferred.
- **One authoritative project record:** explicitly designate the editable project workbook/registers. JSON/XML, schedules, generated PDF markups and infographics are derived unless formally named the primary editable record.
- **Separate identity from display:** source tags and presentation labels may change; canonical IDs and reconciled annotation references persist.
- **Separate scope from physical existence:** record work actions, responsibility, scope disposition, interfaces and existing condition without pretending all observed equipment is in KIS's work scope.
- **Preserve reviewed work:** engineering acceptance protects selected attributes/configurations, while snapshots and configuration baselines preserve entire identified states; they are distinct acts.
- **Independent source verification:** passing validators doesn't establish that all contractual responsibilities or physical points were found.
- **Retain legitimate parallelism:** networking, narratives, drawing tracks and at-risk logic handoff may proceed from properly identified, versioned inputs with change-impact tracking.

## Maturity

This scaffold is a **proposal**, intended to be piloted and refined using a partially completed controls project before schemas, editable-register mappings or cross-package interfaces become binding. Current `bas-logic-gen` content remains where it is until migration is reviewed. No real-project source documents, credentials or confidential deliverables should be committed to this public repository.

## Official workbook templates

The following owner-accepted blank workbook structures are the official templates for new controls-engineering projects:

- [Project Engineering Register (PER) v1.2](templates/project-engineering-register/PROJECT_PER_v1.2.xlsx) — project-level scopes, work package definitions and progress, requirements/evidence, RFIs, engineering issues, operational actions and management views. See the [PER template changelog](templates/project-engineering-register/CHANGELOG.md).
- [Equipment / Device / Points v1.0](templates/equipment-device-points/Equipment_Device_Points_Template_v1.0.xlsx) — standalone physical equipment, device and point inventory deliverable, using stable IDs and cross-references to the PER.

**Initialization:** Copy each blank template into approved project storage; never populate the repository template with client/project data. Designate the project copies and revisions in the project source/baseline register. Preserve the provided identity, validation and relationship fields. Engineering contents require project-specific source reconciliation and review; accepting the blank template does not accept any project engineering.

## Controls design patterns (draft)

- [ATS/generator monitoring interfaces](docs/design-playbooks/patterns/ats-generator-status-monitoring.md)
- [CHW primary/secondary plant architecture](docs/design-playbooks/patterns/chw-primary-secondary-plant.md)
- [HVAC PLC staged availability](docs/design-playbooks/patterns/hvac-plc-staged-availability.md)
- [Field as-found evidence pattern](docs/design-playbooks/patterns/as-found-verification.md)
- [PLC point ownership and I/O sizing contract — candidate](docs/engineering-data/point-allocation-and-counting-proposal.md)

These design patterns are **draft decision aids**, not project requirements or validated controller selections. Document source, assumptions, alternatives and owner approval in each project PER.
