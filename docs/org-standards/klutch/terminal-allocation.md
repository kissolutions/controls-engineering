---
title: Klutch Terminal Allocation Handoff
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Terminal Allocation Handoff

Terminal allocation is part of the craft of panel design. Klutch handles it as a handoff, like the LV lighting extension: the agent makes a rules-based first pass, the PE tweaks and validates, and only then does the result go into the drawings and the EDP.

## First directive (trial)

1. **First pass, in the chat only.** The agent builds one point table for the panel. It does not edit the EDP or the drawings yet.

   | Controller / device | Terminal or function | Device tag | SCADA / operator signal name |
   |---|---|---|---|
   | KMC1 | UI3 | TT-MA | `_MA_TMP` |
   | SR1 (safety relay) | R2 | DOOR-SW | `_DOOR` |
   | VFD bypass | DI2 | ZS-OAD | `_VSD_PERM` |

   - Controllers and devices come from the EDP DEVICE tab (KMC1, KMC2, SR1, the VFD bypass, and so on).
   - Terminals use the device's own names: KMC `UI7`, `BO6`; safety relay `R1`, `R2`; bypass `DI6`, `RO2`.
   - The rules applied in the first pass: the 4–20 mA packing priority ([Panel and hardware](panel-hardware.md)), spares, and grouping that keeps the wiring sheets readable.
2. **Tweak in text.** The PE edits the table in the chat until it is right.
3. **Apply all at once.** The accepted table goes into the EDP rows and the drawings in one step, and the change is logged.

## Validation

- Every point in the accepted table matches an EDP row (tag and SCADA name), and every EDP point has a terminal.
- The drawings show the same terminals as the EDP.
