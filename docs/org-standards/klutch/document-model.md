---
title: Klutch Document Model — Drawing Set
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Document Model — Drawing Set

A Klutch controls drawing set is organized in **sheet number groups**. Each group holds one kind of information, in a fixed order. Groups start at fixed numbers, so a sheet number tells the reader what kind of sheet it is.

## Numbering rule

- Sheet numbers are reserved by group, and **gaps are intentional**. A sheet added after a prior submittal goes into an open number in its group, so existing sheets keep their numbers and cross-references do not have to be reworked.
- Group ranges below are the usual allocation. A project with many floor plans (or many wiring sheets) may widen a group; decide that at the start of the set, not by renumbering after a submittal.
- Unused numbers are simply absent from the set. The table of contents lists only issued sheets.
- Once a sheet number has been issued on a submittal, it is not reused for different content. *(To confirm.)*

## Sheet groups

| Sheets (usual) | Group | Content |
|---|---|---|
| 1 | Table of contents | Always the first sheet. Lists the issued sheets. |
| 2–5 | Spatial | Floor plans locating equipment; demolition; wiring routes and wiring types; any other spatial information. |
| 6–10 | Logical / network | Network diagrams and risers; device and object tables with addresses and instance IDs; typical object lists (standard points and connections for VFDs, gas analyzer networks and similar). |
| 11–20 | Engineering (the core of the set) | In order: process diagrams, controls narrative and references, general arrangement, system wiring. See below. |

### Engineering group order (11–20)

1. **Process diagrams.** Process and instrumentation diagram(s) for the system.
2. **Narratives and references.** Controls narrative; references taken from the mechanical and electrical drawings that mark important requirements; design intent and specification extracts.
3. **General arrangement.** Usually the DDC panel general arrangement and back panel. Drawn to scale. Carries the bill of materials for all internal components (power supplies, DIN rail, controllers, relays and so on).
4. **System wiring.** As many sheets as needed:
   - The first one or two sheets: power, and complex field devices such as VFDs and actuators.
   - Then the controller sheets: KMC controller terminals and their field device wiring are condensed together on their own sheets. This follows from the paper-space needs of the KMC controllers and how the wiring diagrams were originally set up.

## Example (sanitized): single AHU DDC upgrade

| Sheet | Title | Group |
|---|---|---|
| 1 | Title page (table of contents) | Table of contents |
| 2 | Floor plan | Spatial |
| 6 | Devices and networks | Logical / network |
| 11 | Process and instrumentation diagram, with instrument BOM | Engineering: process |
| 12 | Controls narrative | Engineering: narrative |
| 13 | DDC panel layout, with panel BOM | Engineering: general arrangement |
| 14 | System wiring (1 of 2): power and VFD | Engineering: wiring (power / complex devices) |
| 15 | System wiring (2 of 2): controllers and field devices | Engineering: wiring (controllers) |

Sheets 3–5, 7–10 and 16–20 are open for later insertion.

## Open questions (owner to confirm)

- Groups above 20: is 21+ reserved (for example details, schedules, as-built or commissioning records), or does the engineering group simply extend?
- Where do the symbol legend, abbreviations and general notes live: sheet 1, or a reserved sheet in a group?
- Does the instrument BOM always sit on the process diagram sheet, as in the example?
- Title block fields, revision scheme (for example Rev 1 Initial Submittal) and file naming: capture here or in a separate page?
- Multi-system projects: one set per system with the same numbering, or one set with groups subdivided by system?
