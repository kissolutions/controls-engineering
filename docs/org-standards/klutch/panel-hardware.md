---
title: Klutch Panel and Hardware Conventions
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Panel and Hardware Conventions

Standard DDC panel conventions that the pre-canned panel design implements. Project-specific deviations are recorded as precedence overrides or EDP notes.

## Terminal designations

Panel distribution uses **double-deck terminal blocks**. A terminal reference is the block position plus the deck: `3T` is terminal 3, top deck; `3B` is terminal 3, bottom deck. On power distribution strips the supply (+ or line) is on the top deck and its return (− or common) on the bottom deck of the same block, so each load's feed and return share one position.

## Panel power

Reference: Klutch pre-canned DDC panel power sheet (2026), drawn once for several air handlers with per-unit variants of the 24 VAC and 24 VDC groups.

### 120 VAC distribution

- One incoming branch circuit: 120 VAC line, neutral and equipment grounding conductor (E.G.C.).
- Line passes through one supplemental circuit breaker in the panel (CB2, 10 A on the reference sheet), then to the **TS-120VAC** fused terminal blocks (14 AWG):

| Fused terminal | Fuse (reference) | Feeds |
|---|---|---|
| 1 | 1 A | PS1, the 24 VDC power supply |
| 2 | 5 A | Panel receptacle |
| 3 | 1 A | XFMR1, the 24 VAC transformer |
| 4 | — | Spare |

- Neutrals return on the TS-120VAC neutral terminals. The receptacle and transformer are grounded (#14 green).

### 24 VAC distribution (XFMR1)

- **TB-24AC**: one fused terminal block per actuator (each valve, each damper), fed from the transformer secondary, with its own return terminal. No unfused distribution terminals between the fuse and the device.
- Loads on the reference sheet: the control valve actuators (CV-CW, CV-HW), the outdoor air damper (OAD ON/OFF), and spares. A unit variant adds a 24 VAC field supply pair.

### Grounding and common reference

- The 24 VAC transformer's negative (common) terminal is connected to ground **before any fusing**.
- PS1(−) is bonded to that same point **directly from the power supply**, not through terminal blocks.
- The 24 VAC and 24 VDC circuits therefore share one deliberate reference. Analog signals between the KMC (DC side) and 24 VAC actuators, such as 2–10 VDC valve commands, work against that common reference.

### 24 VDC distribution (PS1)

- Each group of equipment is on its own fused terminal (1 A on the reference sheet), supply on the top deck and return on the bottom deck:

| Fused terminal | Feeds |
|---|---|
| 1T | Router (ROU1) |
| 2T | KMC1 and KMC2 |
| 3T | KMC3 and KMC4 |
| 4T | Field power, FP(+) / FP(−) |
| 5T | General terminal strip, TS-GEN |
| 6T–8T | Spares (a unit variant uses one for a second field power group) |

### Field 24 VDC power (FP)

- Field device loop power (FP) is switched through a contact of relay **CR-FP**, then distributed on terminal strips **TS-FP1** (+) and **TS-FP2** (−). CR-FP cycles the 4–20 mA field power (see KMC controllers below).

### Standard relays

The pre-canned sheet carries **CR-FP**, **CR-INTLK** and **CR-DPR** (coil plus one 11–14 contact each).

### Isolation

- Pulling PS1's 1 A fuse removes 24 VDC (controllers, router, field power) without affecting anything on 24 VAC: valves and dampers keep their power for HAND or bypass operation.
- Pulling XFMR1's 1 A fuse, or opening CB2, removes 24 VAC. Label which fuse feeds the transformer, and label the 24 VAC terminals as live with the 24 VDC off.

## Actuator power: 24 VAC transformer (XFMR1)

- **Valve and damper actuators are 24 VAC.** Specify 24 VAC (or 24 VAC/DC) actuators and power them from XFMR1, each on its own fused TB-24AC terminal block. This makes actuator operation independent of the 24 VDC power supply.
- The transformer is XFMR1, a Class 2 control transformer in the panel's existing 24 VAC provision, sized as the **smallest standard size that does the job**:
  - sum the running (sizing) VA of every valve and damper actuator on it from the datasheets, plus the relay coils it feeds;
  - add margin *(Klutch margin to confirm, for example 25%)*;
  - select the next standard size up.
- Everything in the damper proving circuit runs from this transformer: actuator power switched by the KMC relay output, with the CR-DPR contact in parallel; the CR-DPR coil, switched by the drive or bypass "started" relay output; and the CR-ES coil, switched by the damper end switch.
- Only dry relay contacts cross between the damper circuit, the 24 VDC controls circuit and the drive or bypass inputs. Commons are not connected across those boundaries.

### Modulating actuators

The 24 VAC and 24 VDC commons are bonded at one point (see Grounding and common reference), so a modulating actuator on 24 VAC can take a 2–10 VDC command from the KMC. Keep that single bond point; do not add further common-to-ground connections at terminals or field devices, and do not feed full-wave rectified loads from XFMR1.

## Relay coils switched by drive or bypass outputs

- Fit suppression on every relay coil switched by a drive or bypass relay output: a flyback diode on DC coils, an R-C snubber or MOV on AC coils. *(ABB requires this for the E-Bypass; verify the ACH580 E-Clipse requirement.)*
- Check the drive or bypass relay contact rating against the coil before use.

## KMC controllers

- The KMC output that commands a damper is always a relay output.
- **4–20 mA inputs are packed into KMC1 by priority (critical rule):**
  1. **Controlling inputs first:** every 4–20 mA sensor that any control loop or sequence acts on goes on KMC1. This applies to every system the controller serves, including secondary systems that share it (for example an exhaust fan that does not warrant its own controller).
  2. **Monitoring-only inputs next**, in the KMC1 UIs left over.
  3. **Overflow:** only monitoring-only 4–20 mA inputs may go to KMC2 (a CAN module), and only behind their own switched field power (see below). A controlling 4–20 mA input never goes on a CAN module.
- Classify every 4–20 mA input as controlling or monitoring-only in the EDP before allocating terminals.
- KMC1 normally offers 8 UIs on its terminal blocks (UI3–UI10). UI1 and UI2 sit on the RJ45 room sensor port. When more than 8 4–20 mA inputs are needed, use the KMC RJ45 breakout board on that port to use UI1 and UI2 as standard UIs. The room sensor port has nothing special about it beyond making KMC thermostats easy to connect. *(Record the breakout board part number.)*

### KMC CAN modules and 4–20 mA inputs

**Known hardware problem (Klutch field experience, 2026):** on all KMC CAN expansion modules, the universal inputs start up in a state where a 4–20 mA input is a direct short until the module has booted. It is not fixed in firmware, and even a firmware fix would not cure it: the board itself needs a redesign. A 4–20 mA loop powered while a CAN module is booting is shorted through the input.

**Rule:** every 4–20 mA loop powered by Klutch is dead until the CAN modules have booted.

- Klutch-sourced 4–20 mA field power (FP) is switched by **CR-FP** and distributed on TS-FP1 / TS-FP2 downstream of its contact.
- The directive allows separate field power groups so controlling and monitoring loops can be isolated from each other: for example CR-FP for the KMC1 controlling loops and a second relay (`CR-FP2`) for monitoring-only loops on a CAN module. Each group gets its own relay, fused 24 VDC terminal and TS-FP strips. Most panels will need only one group; the provision is there when a project calls for it.
- **CR-FP is driven by a KMC1 relay output**, never by a CAN module output. Its placement on KMC1 is critical.
- **CR-FP starts open (field power off).** KMC1 firmware retains the output position through a power cycle, so the program sets the output's relinquish default to 0, and resets it to 0 whenever it finds it at 1. The relay is then all but guaranteed to start open.
- **CR-FP closes only after KMC1 has confirmed, by polling the EIO network, that the CAN modules are booted.**
- **Under discovery:** what happens if a CAN module drops off the EIO network or reboots while running, and whether CR-FP should open again. Current belief is that the short occurs only after a power-off. Revise this section as field findings come in.
- This programming is part of the engineering-to-logic handoff for every panel with CR-FP, and is checked at programming review.

**Open item (under discovery):** behavior of the CAN module inputs with externally powered (4-wire, self-powered) 4–20 mA transmitters is not known. CR-FP protects the 2-wire loops Klutch sources; it does not remove power from an externally powered transmitter. Treat an externally powered 4–20 mA device on a CAN module as an unresolved risk and record it.

## Open questions

- Damper transformer sizing margin.
- Standard transformer sizes used in the pre-canned design.
- Fuse ratings on TB-24AC (1T, 2T).
