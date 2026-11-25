---
title: Klutch Document Model — Drawing Set
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Document Model — Drawing Set

A Klutch controls drawing set is organized in **sheet number groups**. Each group holds one kind of information, and the groups always come in the same order. The group ranges are sized to the project at the start of the set, so a sheet number tells the reader what kind of sheet it is.

## Numbering rule

- Sheet numbers are reserved by group, and **gaps are intentional**. A sheet added after a prior submittal goes into an open number in its group, so existing sheets keep their numbers and cross-references do not have to be reworked.
- **Group order is fixed; group size is not.** Each project sizes its groups at the start of the set (for example a building with six floors reserves more spatial sheets). Decide this before the first submittal, not by renumbering afterward.
- **Multi-system sets give each system its own block of ten**, starting on a multiple of ten plus one (21, 31, 41, ...). Each block repeats the engineering pattern for that system.
- A sheet number may carry more than one page (for example "Network diagrams, 1 of 2"). *(To confirm how pages within one sheet number are labelled.)*
- Unused numbers are simply absent from the set. The table of contents lists only issued sheets.
- Once a sheet number has been issued on a submittal, it is not reused for different content. *(To confirm.)*

## Sheet groups

| Group | Usual sheets, single system | Content |
|---|---|---|
| Table of contents | 1 | Always the first sheet. Lists the issued sheets. |
| Spatial | 2–5 | Floor plans locating equipment; demolition; wiring routes and wiring types; any other spatial information. |
| Logical / network | 6–10 | Network diagrams and risers; device and object tables with addresses and instance IDs; typical object lists (standard points and connections for VFDs, gas analyzer networks and similar). |
| Engineering (the core of the set) | 11–20 | In order: process diagrams, controls narrative and references, general arrangement, system wiring. See below. |

### Engineering block order

Each engineering block, single-system (11–20) or per system (21–30, 31–40, ...), runs in this order:

1. **Process diagrams.** Process and instrumentation diagram(s) for the system.
2. **Narratives and references.** Controls narrative; references taken from the mechanical and electrical drawings that mark important requirements; design intent and specification extracts.
3. **General arrangement.** Usually the DDC panel general arrangement and back panel. Drawn to scale. Carries the bill of materials for all internal components (power supplies, DIN rail, controllers, relays and so on).
4. **System wiring.** As many sheets as needed:
   - The first one or two sheets: power, and complex field devices such as VFDs and actuators.
   - Then the controller sheets: KMC controller terminals and their field device wiring are condensed together on their own sheets. This follows from the paper-space needs of the KMC controllers and how the wiring diagrams were originally set up.

## Example A (sanitized): single AHU DDC upgrade

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

## Example B (sanitized): multi-floor, multi-system building

Seven systems (four air handlers, three other systems, including two exhaust systems) across six floors.

| Sheets | Content | Group |
|---|---|---|
| 1 | Table of contents | Table of contents |
| 2–10 | Floor plans for six floors (spatial group widened) | Spatial |
| 11 | Network diagrams and network device tables (two pages) | Logical / network (narrowed to one sheet number) |
| 21–30 | System 1: P&ID through wiring | Engineering block |
| 31–40 | System 2 | Engineering block |
| 41–50 | System 3 | Engineering block |
| 51–60 | System 4 | Engineering block |
| ... | One block per remaining system | Engineering block |

Sheets 12–20 are open.

## Open questions (owner to confirm)

- How are pages within one sheet number labelled (11.1 / 11.2, "1 of 2", or sheet 11 and 12)?
- In a multi-system set, is 12–20 reserved for anything (for example plant-wide or common narrative, typical details), or simply open?
- Shared hardware across systems (one panel serving two systems, a common network): which block carries it?
- Groups after the last system block: reserved for anything (details, schedules, as-built or commissioning records)?
- Where do the symbol legend, abbreviations and general notes live: sheet 1, or a reserved sheet?
- Does the instrument BOM always sit on the process diagram sheet?
- Title block fields, revision scheme (for example Rev 1 Initial Submittal) and file naming: on this page or a separate one?
