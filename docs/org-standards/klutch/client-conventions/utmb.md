---
title: Client Conventions — UTMB (unwritten expectations, as practiced by Klutch)
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Client Conventions — UTMB

UTMB expectations that are not written in a UTMB standard, and Klutch's standard way of meeting them. They rank as client standards in the [precedence order](../../README.md#precedence). Record the source as "owner expectation, as reported by the Klutch PE" until a written UTMB reference exists.

Facts marked *verify* must be checked against the ABB ACH580 / E-Clipse bypass documentation for the installed firmware before they are used on a drawing. Terminal assignments below come from a Klutch wiring diagram, not from ABB documentation.

## VFD interface (ABB ACH580 with E-Clipse bypass)

Read from a Klutch wiring diagram for a large outdoor air handler (2026). All drive inputs are **dry contacts from Klutch interposing relays**, wetted by the bypass unit's own +24 VDC, so the drive's inputs never depend on the DDC panel's power.

| Bypass X2 terminal | Bypass input | Function | Signal name | Klutch contact | Source of the contact |
|---|---|---|---|---|---|
| 1, 2 | +24 VDC | Wetting supply for the inputs below | — | — | Bypass unit |
| 3 | DI CMN | Digital input common | — | — | — |
| 4 | GND | — | — | — | — |
| 5 | DI1 | Start / stop | `_VSD_SS` | SS relay (11–14) | KMC start/stop output |
| 6 | DI2 | Start permissive | `_VSD_PERM` | ES contact (11–14) | Damper end switch, through the CR-ES relay |
| 7 | DI3 | Start interlock (hard interlock, also in bypass) | `_SAFETY` | FIRE contact **in series with** SAFETY relay (11–14) | Fire alarm panel (FACP) dry contact, then the DDC safety relay |

### Fire and safety (DI3, start interlock)

- `_FIRE`: dry contact from the fire alarm system, configured for this equipment.
- `_SAFETY`: from the DDC control system, normally an RIB MNLB-series safety relay with enough inputs for the system (usually high static, low static, freeze, door; more when found).
- Both are wired **in series** into DI3 (bypass X2 terminal 7), the start interlock that also holds the unit off in bypass. The wire into the drive carries the signal name `_SAFETY`.

### Dampers and fans in HAND or maintenance

**Expectation:** if dampers would prevent the fan from running in any HAND or maintenance mode, the drive must be able to run the fan safely without the controller, from the keypad or the bypass.

**Klutch solution:**

- **CR-DPR** (interposing relay in the Klutch panel): its coil is driven by the drive's "started" / damper-control relay output (RO1 on the reference drawing; RO1's HVAC default function in the ACH580 is "Damper control", *verify the bypass configuration*). Its N.O. contact is wired **in parallel with the KMC relay output** that powers the damper actuator. The drive therefore opens its own damper whenever it starts, with or without the controller. The KMC damper output is always a relay output.
- **Damper actuator power** must stay on when the controller is removed or isolated: it is on its own fused 24 V circuit, separate from the controller's fuse group (see Panel power below).
- **CR-ES** (interposing relay in the Klutch panel; `CR-ES1`, `CR-ES2`, ... for multiple dampers): energized by the damper end switch. Two poles: one reports the end switch to a KMC input for monitoring; the other goes to **DI2 start permissive** (bypass X2 terminal 6, `_VSD_PERM`). The drive holds speed until the damper proves open, without showing a fault.

Result: if the controller fails, the fans can still be run in HAND from the keypad or the bypass, with the damper opened and proven.

### Panel power and isolation for damper proving

- The ACH580 auxiliary +24 VDC output is limited to 6.0 W total (250 mA), minus any option modules, and is non-isolated. It cannot power damper actuators (typically 10–20 W). Use it only to wet the drive's own inputs, or a relay coil of a few hundred milliwatts.
- Every crossing between the drive and the Klutch panel is a dry relay contact. The drive's 24 V and the panel's 24 V commons are never connected.
- Damper actuator power is on its own fuse, so the controller and other loads can be switched off and isolated while the dampers can still be driven for HAND operation. Label it as a source that remains live with the controller off.

### To verify on the next drawing

- "DI7" and "DI6" in earlier notes were the **X2 terminal numbers** (7 and 6); the inputs are DI3 and DI2.
- On the reference drawing the relay coils are labelled SAFETY, PERM and SS, but the contact into DI2 is labelled ES. Use one name (CR-ES) for coil and contact.
- What drives the SAFETY relay coil (the MNLB master relay output, or a KMC output)?
- The remaining bypass terminals for the complete set: speed reference, run / fault / bypass status relay outputs, and the BACnet connection.

## Validation checks for UTMB projects

- Every VFD has `_FIRE` in series with the DDC safety relay into DI3 (start interlock), and `_VSD_SS` on DI1.
- Every damper that can block a fan has CR-DPR and CR-ES (one CR-ES per end switch), and DI2 (start permissive, `_VSD_PERM`) is wired from CR-ES.
- The safety relay has enough inputs for every safety on the system, plus any spares the project calls for.
