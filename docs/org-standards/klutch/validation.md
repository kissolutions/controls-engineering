---
title: Klutch Validation — Devices, Points and Drawing Representation
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Validation — Devices, Points and Drawing Representation

Klutch review gates run before a submittal is issued. They add to the framework's checks; they do not replace them. The framework's M2 independent completeness pass checks the inventory against the **source documents**. These gates check the inventory against the **Klutch drawings**, and the drawings against each other.

A gate failure is a finding (PER ISSUES or EDP note) with an owner. A **deviation** from a typical rule below is acceptable only when it is either approved by the owner or confirmed against the device datasheet or specification, and that evidence is cited.

## 1. Every device is represented on the drawings

| Device | Must appear on | Not required on |
|---|---|---|
| Device with points Klutch uses (hardwired or network) | P&ID, with its device tag and the signal names of the points used | — |
| Network-connected device, including interface-only (for example an existing gas analyzer controller read over a network) | Network diagram, as a logical or physical network device | P&ID, if none of its points are used |
| Device Klutch wires (field device or panel component) | Wiring diagrams | — |
| Device wired by others and only connected to Klutch over a network | Network diagram | Wiring diagrams (not Klutch's internal wiring) |
| Panel component | General arrangement and its BOM | — |

Checks:

- Every EDP device appears on at least one sheet, and on every sheet the table above requires.
- Every device on a drawing exists in the EDP (no drawing-only devices).
- Every point in the EDP IO LIST appears on the P&ID (signal name) and, if hardwired by Klutch, on a wiring sheet at its terminal.

## 2. Device and point completeness

- Every device has a confirmed tag, model and location. Placeholders (`TBD`, `##`) are counted and listed as open items, never passed silently.
- Every device has its points, or a stated reason it has none (interface only, monitoring by others).
- Every point has a terminal (or network object), signal type, range and units.
- Sensor type matches the specification for the location type (for example a stainless wall plate in common areas). A controller input does not count as a sensor until the device is in the field device list.
- Every field device records its power source and conductor count (for example 2-wire loop powered; 4-wire 24 VDC plus relay output).
- Vendor-furnished devices carry the vendor submittal's full model number everywhere. Name fields never hold part numbers.

## 3. Valves

All control valves are tagged `CV` regardless of type. (ISA practice distinguishes on/off and modulating valves; Klutch keeps `CV` to avoid confusing BAS readers.)

Every controllable valve actuator has a full set of commands and feedbacks:

| Control | Commands | Feedback (typical) |
|---|---|---|
| Analog (modulating) | One 2–10 VDC command | One 2–10 VDC position feedback |
| Digital (open/close), spring return | One command | Two: open and closed end switches |
| Digital (open/close), non-spring return | Two commands (drive open, drive closed) *(to confirm)* | Two: open and closed end switches |

- A valve without the typical feedback set (for example only one end switch) is a deviation: approve it or confirm it against the actuator datasheet.
- Every valve states its fail position, and the fail position matches the actuator (spring return direction) and the specification.

## 4. Dampers

Typical damper actuator: one command, fail closed, one feedback.

- Base the command count, fail position and feedback on the datasheet or specification. If the device appears to need two commands, flag it for owner approval.
- The single feedback is an end switch, usually set at 50% or more toward the open side. Check the setting direction against the damper's normally open or normally closed configuration.
- Any departure from the typical set is a deviation: approve it or confirm it against the datasheet.

## 5. Names match across the drawings

- Each device has one device tag (hyphenated) on every sheet, in every register, and matching the source documents.
- Each point has one signal name (underscored) on every sheet and in the register, built from the owner's naming standard ([Naming](naming.md)).
- Panels and equipment use the same tag on every sheet.

## 6. Drawing-to-register sync, after every drawing revision

- BOM quantities equal the number of uses on the wiring sheets.
- BOM part numbers match their descriptions and the datasheets.
- Terminal assignments in the EDP match the wiring sheets.
- Removed scope is removed everywhere: search every register note, BOM row, wiring sheet and narrative for the removed tags.

## 7. Issue checks

- Every sheet shows the same revision, date and description for the issue.
- The issued PDF was exported after the last drawing edit.
- The controls narrative meets its own pre-issue checklist ([Narrative format](narrative-format.md)).

## Open questions (owner to confirm)

- Non-spring-return digital valves: two commands (open / close) as shown?
- Analog valves: is position feedback always required, or only where the specification or owner asks?
- Should these gates live in the EDP as columns or a check tab, so a script can run the mechanical ones (sections 1, 2, 5, 6)?
