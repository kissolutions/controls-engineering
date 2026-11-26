---
title: Client Conventions — UTMB (unwritten expectations, as practiced by Klutch)
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Client Conventions — UTMB

UTMB expectations that are not written in a UTMB standard, and Klutch's standard way of meeting them. They rank as client standards in the [precedence order](../../README.md#precedence). Record the source as "owner expectation, as reported by the Klutch PE" until a written UTMB reference exists.

Facts marked *verify* must be checked against the ABB ACH580 / E-Clipse bypass documentation for the installed firmware before they are used on a drawing.

## VFD fire and safety inputs

| Signal | Source | Wiring |
|---|---|---|
| `_FIRE` | Dry contact from the fire alarm system, configured specifically for this equipment | Wired in series with any other signals into the VFD digital input that hard-interlocks the E-Clipse bypass (DI7, *verify*) |
| `_SAFETY` | The DDC control system, from an RIB MNLB-series safety relay with enough inputs for the system | Usually carries high static, low static, freeze and door. Add further safeties when found. |

## Dampers and fans in HAND or maintenance

**Expectation:** if dampers would prevent the fan from running in any HAND or maintenance mode, the drive must be able to run the fan safely without the controller, from the keypad or the bypass.

**Klutch solution:**

- **CR-DPR** (interposing relay in the Klutch panel): energized by the KMC damper output **in parallel with** the VFD's "started" relay output (*verify the ACH580 parameter name*). The drive therefore opens its own damper whenever it starts, with or without the controller.
- **CR-ES** (interposing relay in the Klutch panel; `CR-ES1`, `CR-ES2`, ... for multiple dampers): energized by the damper end switch. Two poles: one reports the end switch to a KMC input for monitoring; the other goes to the VFD digital input used as the start interlock (DI6, *verify*). The drive holds speed until the damper proves open, without showing a fault.
- The drive's start interlock waits for the end switch before releasing speed (*verify the ACH580 function name and parameter*).

Result: if the controller fails, the fans can still be run in HAND from the keypad or the bypass, with the damper opened and proven.

## Validation checks for UTMB projects

- Every VFD has `_FIRE` and `_SAFETY` wired as above.
- Every damper that can block a fan has CR-DPR and CR-ES (one CR-ES per end switch), and the drive's start interlock input is assigned.
- The safety relay has enough inputs for every safety on the system, plus any spares the project calls for.
