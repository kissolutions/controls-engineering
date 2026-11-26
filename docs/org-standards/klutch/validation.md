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
| Digital (open/close), non-spring return | Two commands (drive open, drive closed) | Two: open and closed end switches |

- Every analog valve with a modulating actuator (2–10 VDC command) has a 2–10 VDC position feedback by default. Exceptions (for example an actuator model without feedback, or a valve class the owner excludes) are approved deviations.
- A valve without the typical feedback set (for example only one end switch) is a deviation: approve it or confirm it against the actuator datasheet.
- Every valve states its fail position, and the fail position matches the actuator (spring return direction) and the specification.

## 4. Dampers

Typical damper actuator: one command, fail closed, one feedback.

- Base the command count, fail position and feedback on the datasheet or specification. If the device appears to need two commands, flag it for owner approval.
- The single feedback is an end switch. **Default:** set at 50% or more toward the open side; confirm per application. Check the setting direction against the damper's normally open or normally closed configuration.
- Any departure from the typical set is a deviation: approve it or confirm it against the datasheet.

## 5. Names match the EDP everywhere

The EDP is the source of truth for every device tag, signal name and SCADA name; the framework requirement is [Identifier consistency validation](../../engineering-data/identifier-consistency-validation.md). Rows missing a required Source Document Tag or Operational / SCADA Name (per the framework's field applicability table) cannot pass this check and are listed as open items; the other checks still run. Klutch checks these places against the EDP:

| Where | What to check |
|---|---|
| PER | Records, issues and RFIs that cite tags |
| Network diagram and device tables (sheets 6–10) | Device tags, controller names, network addresses and instance IDs |
| P&ID and instrument BOM | Device tags and signal names, paired as in the EDP |
| Controls narrative | Signal names, setpoint names and device tags in the text and tables |
| DDC panel layout and BOM | Panel, controller and component tags |
| Wiring diagrams | Device tag on each device; signal name on each wire; terminal matches the EDP |
| Floor plans | Device and equipment tags |
| KMC programs and object lists | Object names match the signal / SCADA names |
| SCADA (Iconics) | Point names match the SCADA names |
| RFIs and transmittals to the owner | Tags used in questions match the EDP |

## 6. Drawing-to-register sync, after every drawing revision

- BOM quantities equal the number of uses on the wiring sheets.
- BOM part numbers match their descriptions and the datasheets.
- Terminal assignments in the EDP match the wiring sheets.
- Removed scope is removed from every current deliverable (register notes, BOM rows, wiring sheets, narrative) and keeps its history: the EDP row stays with a removed disposition and the change log entry.

## 6a. Device selection, ranges and output cards

The checks in [Device selection and signal ranges](device-selection.md): requirements to selection, datasheet to EDP, EDP to CAD tables (sensor range in each instrument description), outputs to HPO cards, and visible assumptions.

## 6b. Fail behavior

The EDP DEVICE tab holds the **final answer** for each controllable device's behavior, in structured columns (not notes), which every downstream item (narrative, drawings, schedules, programming) is validated against. The conditions can give different answers: a heating valve can be commanded closed on a normal stop and spring open on loss of power.

| Column | Content |
|---|---|
| Normal stop position | Position commanded on a normal stop |
| Loss of actuator power | Physical fail position (spring return direction) |
| Loss of command signal | Configured actuator response |
| Controller failure | Result of the actual output and wiring arrangement |
| Expansion comms loss | Module behavior and system response (for devices on expansion modules) |
| HAND / manual operation | Available control and remaining interlocks |
| Determination status | **Finalized**, **Open** or **Undetermined** |
| Evidence | Closing Issue / RFI / record for Finalized; the open item for Open; the reason and what is known for Undetermined |

Checks:

- Every controllable output device has every applicable column, or "n/a" with the reason.
- The narrative, drawings and schedules match the DEVICE row for each condition.
- "Finalized" means the answer is established. Commissioning evidence separately establishes that the installation performs accordingly.

*(Framework template proposal: add these as DEVICE LIST columns in the EDP template.)*

## 6c. Intake items

- Every air handler has a DOOR-SW input reserved during preliminary design, and a **disposition before issue**: device confirmed, or confirmed absent ([Intake checklist](intake-checklist.md)).
- Every jumper on a safety input states its purpose and its removal condition, and says whether it is an unused provision or stands in for a required safety device that is missing.

## 7. Field loop power and KMC CAN modules

See [Panel and hardware: KMC CAN modules and 4–20 mA inputs](panel-hardware.md#kmc-can-modules-and-4-20-ma-inputs).

- Every Klutch-sourced 4–20 mA loop draws its power from TS-FP, downstream of the CR-FP contact (wiring diagrams and EDP power source field).
- Every KMC panel with Klutch-powered 4–20 mA loops has CR-FP.
- CR-FP's coil is on a **KMC1 relay output** (EDP IO LIST and wiring diagram). A CR-FP on a CAN module output is a failure.
- The panel layout and the wiring sheet showing CR-FP carry the large boxed "disable CR-FP before first power-up" note next to CR-FP.
- The logic handoff and the program include: relinquish default 0 on the CR-FP output, the reset-to-0 logic, and the EIO-network "CAN modules booted" permissive before CR-FP closes. Checked at programming review.
- Every 4–20 mA input is classified in the EDP as **controlling** or **monitoring-only**. A value is **controlling** if it drives any loop, sequence, alarm action, interlock or permissive; it is monitoring-only only if it is displayed, trended or alarmed with no automatic action.
- **Every controlling 4–20 mA input is on KMC1**, for every system the controller serves. A controlling input on a CAN module needs a recorded failure-mode analysis and PE-approved deviation; without them it is a failure.
- KMC1 UIs are filled with controlling inputs before any monitoring-only input. A monitoring-only input on KMC1 while a controlling input sits elsewhere is a failure.
- A monitoring-only 4–20 mA input on a CAN module is allowed only as overflow (KMC1 full), with its field power on a switched group that is released after the CAN modules boot. An externally powered one is also recorded as an open risk.
- If KMC1 needs more than its 8 terminal UIs for 4–20 mA inputs, UI1 and UI2 are used through the KMC RJ45 breakout board before any other option.

## 8. Issue checks

- Every sheet shows the same revision, date and description for the issue.
- The issued PDF was exported after the last drawing edit.
- The controls narrative meets its own pre-issue checklist ([Narrative format](narrative-format.md)).

## Open questions (owner to confirm)

- Should these gates live in the EDP as columns or a check tab, so a script can run the mechanical ones (sections 1, 2, 5, 6)?
