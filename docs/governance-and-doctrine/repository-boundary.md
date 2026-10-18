---
title: Controls Engineering Repository Boundary
page_type: governance
page_status: draft
---

# Controls Engineering Repository Boundary

**Status:** proposed package interface; subject to pilot validation.

## Parent knowledgebase: authoritative upstream

`kissolutions/knowledgebase_wikijs` owns cross-domain terminology, KIS Systems Engineering Framework architecture, generic process contract and taxonomy, shared physical boundary process, applicable shared codes/application knowledge, and physical device hardware data. Refer to those pages by link, revision and evidence; do not copy whole catalogs or establish competing hardware capacities here.

## Controls engineering package: domain authority

`kissolutions/controls-engineering` owns controls project lifecycle orchestration, domain-specific processes and acceptance gates, System/Equipment/Device/Point engineering ontology, scope and responsibility review, project-register contracts, engineering verification, narrative and architecture design processes, drawing/schedule presentation contracts, and review/handoff conventions. It may use shared methods without owning them.

## Logic generation package: separate domain and team

`kissolutions/bas-logic-gen` owns reusable vendor-neutral logic patterns, platform-specific code archetypes, programming architecture, code assembly, and software/test validation. It consumes explicit engineering decisions and approved/draft sequence and point/interface data with version status, and feeds back findings or proposed change requests. It is **not** the authority to revise contractual scope, device requirements, or a released controls narrative.

Existing `bas-logic-gen` engineering playbook pages remain in their original repository until cross-repository migration, preservation of history and agent entry points are explicitly reviewed. References during migration do not constitute two concurrently authoritative processes.

## Domain boundaries

`kissolutions/lv-lighting-design` owns LV lighting's exact fixtures, zones, supply channels, grouping, routing and milestone/PDF conventions. Transfer generic lessons and interface design; never graft lighting-specific geometry or 100-W channel assumptions into BAS.

## Project storage

External contractual sources, approved submittals, field records and internal PM/PE registers exist in the project's authorized storage. This repository contains **templates and processes**, not real client source PDFs, working PM trackers or client deliverables. Project intake declares the specific authoritative editable register(s) and makes all XML/JSON/CSV reports derived unless deliberately established otherwise.

## Changes crossing a boundary

Record a proposed upstream edit when a generic KIS concept is insufficient. Record a handoff change request when code implementation cannot satisfy a versioned engineering decision. Changing a code archetype is not permission to change the engineered sequence; changing a project source requirement is not automatically a global BAS doctrine change.
