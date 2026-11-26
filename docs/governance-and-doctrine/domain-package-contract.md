---
title: Controls Engineering Domain Package Contract
page_type: governance
page_status: draft
---

# Domain Package Contract — proposed v0.1

A **Domain** is a coherent area of engineering knowledge. A **Domain Package** is its independently versioned combination of procedures, schema/data contracts, validation, work-product formats and agent instructions. A package may be a GitHub repository or a smaller collection of parent knowledge pages; domains do not inherently require their own repository.

## Identity and dependencies

- **Package ID:** `kis.controls-engineering`
- **Repository:** `kissolutions/controls-engineering`
- **Maturity:** bootstrap proposal
- **Parent:** `kissolutions/knowledgebase_wikijs`; KIS Systems Engineering Framework v1.0
- **Optional downstream consumer:** `kissolutions/bas-logic-gen`
- **Optional dependency (proposed):** a *logic domain*, to help write and validate controls narratives (operating modes / state machine, sequences, alarm and permissive logic). `kissolutions/bas-logic-gen` is the current logic domain.
- **Parallel example domain:** `kissolutions/lv-lighting-design`
- **Project data:** outside repository, governed by project manifest and source/revision matrix

## What packages declare

| Dimension | This package |
|---|---|
| Domain scope | Controls engineering, contract/scope intake through commissioning and closeout |
| Reusable processes | Source registration, scope extraction, inventory, independent reconciliation, owner review, baseline comparison and impact assessment |
| Canonical terminology | System, Equipment, Component, Device, Point, Interface, Source Evidence, Open Item, work action and scope responsibility |
| Input contracts | Registered source revisions, owner/contract evidence, prior engineering data, location and work boundaries |
| Output contracts | Source/scope matrix, equipment and I/O registers, applicable requirements, sequences, architecture selections, drawing packages, engineering-to-logic handoff |
| Validation | Stage-specific source and structural checks, independent completeness review, explicit unknown/deferral controls |
| Acceptance / baseline | Selected derived engineering decisions protected; full immutable snapshot/baseline explicitly designated |
| Agent entry points | This repo's `CLAUDE.md` and versioned processes; references to parent doctrine |

## Dependency rules

1. An agent reads parent framework terms and only the engineering package(s) needed for the project. Load `bas-logic-gen` when producing implementation code, **not** for ordinary scope/I/O extraction.
2. Domain-specific model IDs and semantic contracts can extend shared records but may not silently redefine parent terms.
3. A cross-package handoff includes producer/consumer version, authoritative project registry revision and source/baseline identifiers.
4. Never mark a package/process validated solely because a reference example passes or another agent once executed it.
5. Keep the WikiJS `Domains` index (when created) as a package *catalog* and navigation layer, not a second authoritative copy of every domain's executable rules.

6. *(Proposed.)* Optional dependencies are declared in each package's head files (`README.md`, `CLAUDE.md`). A package that can serve as a dependency (for example a logic domain) registers itself as a candidate when installed; the owner confirms it as a dependency at install time or first use. Until confirmed, the depending package works without it and says which steps lose support (for example, narrative mode tables are not checked against a canonical state machine).

This is documentation only; no plugin loader, automatic dependency resolution or release automation is implemented by this scaffold.
