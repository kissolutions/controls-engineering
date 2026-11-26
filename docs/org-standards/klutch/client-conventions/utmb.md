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

All of these signals land on the **E-Clipse bypass control board (terminal block X2)**, not on the ACH580 drive control board. The bypass generates and handles them in both drive and bypass mode. Terminal functions below are from ABB's E-Clipse default wiring diagrams (ACH580 E-Clipse bypass and packaged drive user manual) and a Klutch wiring diagram for a large outdoor air handler (2026).

All bypass inputs are **dry contacts from Klutch interposing relays**, wetted by the bypass board's own +24 VDC, so the bypass inputs never depend on the DDC panel's power.

| Bypass X2 terminal | Bypass input | Function | Signal name | Klutch contact | Source of the contact |
|---|---|---|---|---|---|
| 1, 2 | +24 VDC | Wetting supply for the inputs below | — | — | Bypass unit |
| 3 | DI CMN | Digital input common | — | — | — |
| 4 | GND | — | — | — | — |
| 5 | DI1 | Start / stop | `_VSD_SS` | SS relay (11–14) | KMC start/stop output |
| 6 | DI2 | Run permissive (ABB's example wiring: damper end switch) | `_VSD_PERM` | ES contact (11–14) | Damper end switch, through the CR-ES relay |
| 7 | DI3 | Interlock 1 (hard interlock, also in bypass) | `_SAFETY` | FIRE contact **in series with** SAFETY relay (11–14) | Fire alarm panel (FACP) dry contact, then the DDC safety relay |
| 8, 9 | DI4, DI5 | Interlock 2 / interlock 3 (programmable) | — | — | Spare on the reference drawing |
| 10 | DI6 | Smoke control (Override 1), fixed function | — | — | Not used by Klutch unless specified |
| 11–13 | RO1 | Bypass not faulted (default) | *verify* | — | Wired back to the Klutch panel on the reference drawing |
| 14–16 | RO2 | System running (default) | — | — | — |
| 17–19 | RO3 | System started (default) | — | — | Drives CR-DPR |
| 20–22 | RO4 | Bypass selected (default) | — | — | — |
| 23–25 | RO5 | Bypass in auto (default) | — | — | — |

The bypass control board's +24 VDC capacity and relay contact ratings were not confirmed from ABB documentation; *verify* in the user manual's "E-Clipse Bypass Control Unit Connections (RBCU)" technical data before loading the supply with relay coils.

### Fire and safety (DI3, start interlock)

- `_FIRE`: dry contact from the fire alarm system, configured for this equipment.
- `_SAFETY`: from the DDC control system, normally an RIB MNLB-series safety relay with enough inputs for the system (usually high static, low static, freeze, door; more when found).
- Both are wired **in series** into DI3 (bypass X2 terminal 7), the start interlock that also holds the unit off in bypass. The wire into the drive carries the signal name `_SAFETY`.

### Dampers and fans in HAND or maintenance

**Expectation:** if dampers would prevent the fan from running in any HAND or maintenance mode, the drive must be able to run the fan safely without the controller, from the keypad or the bypass.

**Klutch solution:**

- **CR-DPR** (interposing relay in the Klutch panel): its coil is switched by the bypass's **System Started** relay output (RO3, X2:17–19, default function). Its N.O. contact is wired **in parallel with the KMC relay output** that powers the damper actuator. The drive therefore opens its own damper whenever it starts, with or without the controller. The KMC damper output is always a relay output.
- **Damper actuator power** must stay on when the controller is removed or isolated: it is on its own fused 24 V circuit, separate from the controller's fuse group (see Panel power below).
- **CR-ES** (interposing relay in the Klutch panel; `CR-ES1`, `CR-ES2`, ... for multiple dampers): energized by the damper end switch. Two poles: one reports the end switch to a KMC input for monitoring; the other goes to **DI2 start permissive** (bypass X2 terminal 6, `_VSD_PERM`). The drive holds speed until the damper proves open, without showing a fault.

Result: if the controller fails, the fans can still be run in HAND from the keypad or the bypass, with the damper opened and proven.

### Panel power and isolation for damper proving

- Neither the bypass board nor the drive supplies damper actuators (typically 10–20 W). For reference, the ACH580 drive's auxiliary +24 VDC is 6.0 W total (250 mA) and non-isolated; the bypass board's capacity is unverified.
- Damper power follows the Klutch [panel standard](../panel-hardware.md#damper-actuator-power-dedicated-24-vac-transformer): a dedicated 24 VAC transformer on its own supplemental breaker.
- Power the CR-DPR coil from the panel's damper circuit, switched through the bypass RO3 dry contact. The coil then lives on the same dedicated fuse as the actuators it serves, and only a dry contact crosses the boundary. Fit a flyback diode on a DC coil (ABB requires diodes on DC relay coils switched by bypass outputs, per the ACH550 E-Bypass supplement; *verify for ACH580*).
- Every crossing between the drive and the Klutch panel is a dry relay contact. The drive's 24 V and the panel's 24 V commons are never connected.
- Damper actuator power is on its own fuse, so the controller and other loads can be switched off and isolated while the dampers can still be driven for HAND operation. Label it as a source that remains live with the controller off.

### To verify on the next drawing

- "DI7" and "DI6" in earlier notes were the bypass **X2 terminal numbers** (7 and 6); the inputs are bypass DI3 and DI2.
- On the reference drawing the relay coils are labelled SAFETY, PERM and SS, but the contact into DI2 is labelled ES. Use one name (CR-ES) for coil and contact.
- The wire into X2:11 (RO1C) is RO1, bypass not faulted by default, not the damper output.
- What drives the SAFETY relay coil (the MNLB master relay output, or a KMC output)?
- The remaining bypass terminals for the complete set: speed reference, run / fault / bypass status relay outputs, and the BACnet connection.

## Validation checks for UTMB projects

- Every VFD has `_FIRE` in series with the DDC safety relay into DI3 (start interlock), and `_VSD_SS` on DI1.
- Every damper that can block a fan has CR-DPR and CR-ES (one CR-ES per end switch), and DI2 (start permissive, `_VSD_PERM`) is wired from CR-ES.
- The safety relay has enough inputs for every safety on the system, plus any spares the project calls for.
