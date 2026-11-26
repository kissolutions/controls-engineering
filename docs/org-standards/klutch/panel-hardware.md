---
title: Klutch Panel and Hardware Conventions
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Panel and Hardware Conventions

Standard DDC panel conventions that the pre-canned panel design implements. Project-specific deviations are recorded as precedence overrides or EDP notes.

## Panel power

- **One building branch circuit** feeds the panel. A separate building circuit for dampers is not expected.
- **Separate 120 VAC fuses inside the panel** (no additional breakers):
  1. **Controls:** a 120 VAC fuse for the 24 VDC power supply and everything it feeds.
  2. **24 VAC:** a separate 120 VAC fuse for the 24 VAC transformer that feeds the damper actuators (existing Klutch practice).
- **24 VAC distribution on fused terminal blocks.** The transformer secondary is broken out to a few fused terminal blocks (the existing Klutch motif). Damper actuators and the damper proving circuit get their own fused 24 VAC terminal.
- Pulling or replacing the 24 VDC power supply, or pulling its 120 VAC fuse, does not affect anything on 24 VAC. The controllers can be isolated or removed while the dampers stay live for HAND or bypass operation.
- **Caution:** the panel main breaker, or the 120 VAC fuse feeding the 24 VAC transformer, removes damper power. With only one branch circuit in the panel, label which 120 VAC fuse feeds the transformer, and label the 24 VAC damper terminals as live with the controls off.

## Damper actuator power: dedicated 24 VAC transformer

- **Damper actuators are 24 VAC.** Specify 24 VAC (or 24 VAC/DC) actuators and power them only from the damper transformer. This makes damper operation independent of the 24 VDC power supply.
- The transformer is a Class 2 control transformer in the panel's existing 24 VAC transformer provision, sized as the **smallest standard size that does the job**:
  - sum the running (sizing) VA of every actuator on it from the datasheets, plus the relay coils it feeds;
  - add margin *(Klutch margin to confirm, for example 25%)*;
  - select the next standard size up.
- Everything in the damper proving circuit runs from this transformer: actuator power switched by the KMC relay output, with the CR-DPR contact in parallel; the CR-DPR coil, switched by the drive or bypass "started" relay output; and the CR-ES coil, switched by the damper end switch.
- Only dry relay contacts cross between the damper circuit, the 24 VDC controls circuit and the drive or bypass inputs. Commons are not connected across those boundaries.

### Caution: modulating dampers

A modulating actuator commanded by a KMC analog output (2–10 VDC) shares its signal common with the controller. Its 24 VAC supply common is then tied to the controller's DC common. If a project has modulating dampers:

- tie the damper transformer secondary common to the controller common at one point only, deliberately and drawn;
- keep that transformer for half-wave devices that share the common (do not also feed full-wave devices or rectified loads from it);
- otherwise use a separate transformer for the modulating actuators.

Two-position dampers switched by relay contacts do not have this problem.

## Relay coils switched by drive or bypass outputs

- Fit suppression on every relay coil switched by a drive or bypass relay output: a flyback diode on DC coils, an R-C snubber or MOV on AC coils. *(ABB requires this for the E-Bypass; verify the ACH580 E-Clipse requirement.)*
- Check the drive or bypass relay contact rating against the coil before use.

## KMC controllers

- The KMC output that commands a damper is always a relay output.
- Land 4–20 mA inputs on the main controller, not on CAN expansion modules, and leave panel space for a relay to switch field loop power. *(Reason and affected models to be documented from the KMC source.)*

## Open questions

- Damper transformer sizing margin.
- Standard transformer sizes used in the pre-canned design.
- 120 VAC fuse ratings for the 24 VDC supply and the 24 VAC transformer; fuse ratings for the 24 VAC terminal blocks.
