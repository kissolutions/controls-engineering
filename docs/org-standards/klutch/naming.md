---
title: Klutch Naming — Device Tags and Signal Names
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Naming — Device Tags and Signal Names

Klutch uses **two naming schemes**, and they are not interchangeable.

| Scheme | Form | Comes from | Names | Example |
|---|---|---|---|---|
| **Device tag** | ISA / P&ID style, hyphenated | The source documents, usually the mechanical drawings | The physical device or equipment | `CV-HW`, `CS-SF1`, `WTR-DET`, `VSD-4-1` |
| **Signal name** | Underscored, no hyphens (controllers do not accept hyphens in object names) | The owner's point naming standard | The point / object as it appears in the controller and on the SCADA system | `_HW_VLV`, `_STAT_SF1`, `_WTR_DET`, `_VSD_SPD` |

The device tag ties the controls drawings to the engineered and architectural drawings. The signal name is what the operator sees. One device may carry several signals (a valve has a command and a position feedback), so the two are related, not the same.

## On the drawings

- **Wiring diagrams:** the device is labelled with its **hyphenated device tag**. On the wire, near the I/O terminal, the **underscored signal name** is shown: the SCADA name with the prefix common to the whole system left off, to save space. The leading underscore marks where that prefix attaches. For example, the SCADA name `<SITE>_<BLDG>_<SYSTEM>_HW_VLV` is shown on the wire as `_HW_VLV`; the prefix is stated once in the register, not on every wire.
- **P&ID and instrument BOM:** device tags. *(To confirm: whether signal names also appear on the P&ID, as `_WTR_DET` did on the AHU-4-1 P&ID.)*
- **Network and object tables:** signal / object names.

## Rules

- **SCADA and signal names follow the owner's point naming standard.** Many owners publish a point naming or acronym standard for their BAS (for example a hospital campus standard). It is a client standard in the [precedence order](../README.md#precedence): it outranks this profile. Register it as a project source at intake and cite it for every name built from it; a name that departs from it needs a precedence override.
- **No Klutch default naming form is defined.** When the owner has no standard, record that as an open item and agree the naming with the owner; do not invent a house form.
- Use the source document's tag when the source has one. Do not rename a device for convenience; if the source tag is missing or ambiguous, record that as an open item and assign a provisional tag.
- Signal names use underscores only. Never put a hyphen in a signal or object name.
- Device tags and signal names are different identifiers from the framework's internal IDs (`D-##`, `P-##`) and from vendor part numbers. A field that holds a name never holds a part number.

## Mapping to the framework registers

| Klutch name | EDP field |
|---|---|
| Device tag | DEVICE LIST `Source Document Tag` (and IO LIST `Source Document Tag`) |
| Signal name (as on the drawing) | IO LIST `Signal Name` |
| Full SCADA object name | IO LIST / DEVICE LIST `Operational / SCADA Name` |

## Open questions (owner to confirm)

- Panel and controller names: panel `DDC-<SYSTEM>` (for example `DDC-AHU4-1`), controllers `KMC1`, `KMC2`: are these the standard forms, and is the panel name hyphenated as a device tag?
- Standard signal suffixes: these come from each owner's standard, so the profile should not carry one master list. Capture a list only for Klutch's default form.
- Software points (mode, alarm words, setpoints): same underscored form?
