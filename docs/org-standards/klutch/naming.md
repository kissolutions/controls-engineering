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
| **Signal name** | Underscored, no hyphens | Klutch (controllers do not accept hyphens in object names) | The point / object as it appears in the controller and on the SCADA system | `_HW_VLV`, `_STAT_SF1`, `_WTR_DET`, `_VSD_SPD` |

The device tag ties the controls drawings to the engineered and architectural drawings. The signal name is what the operator sees. One device may carry several signals (a valve has a command and a position feedback), so the two are related, not the same.

## On the drawings

- **Wiring diagrams:** the device is labelled with its **hyphenated device tag**. On the wire, near the I/O terminal, the **underscored signal name** is shown as it will appear on the SCADA system.
- **P&ID and instrument BOM:** device tags. *(To confirm: whether signal names also appear on the P&ID, as `_WTR_DET` did on the AHU-4-1 P&ID.)*
- **Network and object tables:** signal / object names.

## Rules

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

- How the full SCADA name is built: is it a site / building / system prefix plus the signal name (for example `<SITE>_<BLDG>_<SYSTEM>` + `_HW_VLV`), and the leading underscore on the drawing marks the suffix?
- Panel and controller names: panel `DDC-<SYSTEM>` (for example `DDC-AHU4-1`), controllers `KMC1`, `KMC2`: are these the standard forms, and is the panel name hyphenated as a device tag?
- Standard signal suffixes (`_SS`, `_STAT`, `_VSD_SPD`, `_VSD_AUTO`, `_VSD_FAL`, `_CHW_VLV`, `_HW_VLV`, `_VPOS`, `_STPT`, ...): is there a standard list to capture here?
- Software points (mode, alarm words, setpoints): same underscored form?
