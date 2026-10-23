---
title: Chilled water plant primary-secondary with decoupler — engineering playbook
page_type: playbook
page_status: draft
---

# Primary/secondary chilled-water plant with decoupler (P11)

**Status:** Candidate design decision guide; no pre-approved sequence, mandatory point list or prescribed plant topology. Confirm actual hydraulic and equipment design.

## Establish operating architecture

Document chiller, primary and secondary pumping types; variable-speed vs constant-speed primary operation; pump/chiller isolation valves and end switches; decoupler placement and bidirectional flow; minimum chiller flows and anti-short-cycle; load/return temperature metering; bypass, expansion and redundant equipment. Trace all to drawings and OEM interface requirements.

## Decision sequence

1. Establish required primary flow and verified evaporator/condenser proof and valve interlocks **before** exposing chiller enable.
2. Select staged capacity variable: verified secondary tons/GPM, primary requirement, return temperature or another approved plant measurement. Record low-load and sensor-failure behavior.
3. Design secondary differential-pressure control and reset from selected representative valve positions, with limits, fallback DP and hydraulic bounds. Do not assume the most open valve is always a valid reset signal.
4. Coordinate CHW supply-temperature reset with hydraulic demand; a **DP-first, then CHWST** optimization is a candidate strategy, not universal plant law. Define authority limits, hunting prevention and proof of benefit.
5. Coordinate cooling-tower sequencing with verified number of cells/towers, ambient wet bulb and minimum leaving/condenser-water temperatures; define ramp, freeze/low-load/basin bypass operation through manufacturer requirements.
6. Explicitly document degraded/single-CPU, loss of network, bad temperature/DP/flow, and restart sequences.

## Candidate chiller interface checklist — never auto-add points

Start/stop command; CHWS setpoint command; %RLA; CHWS temperature; general alarm; CHW and CW isolation valve outputs/feedback; CW flow; enabling interlocks; and OEM-supported network data are **review candidates**. For each, identify hardwired vs network, owner, proof, protocol/register and commissioning source. Avoid duplicate hardwired controls when a chiller OEM provides the approved function.

## RFIs / owner decisions

Presence/type of VFD on primary and condenser pumps; chiller vs BAS valve control; wet bulb source; BTU meter/chargeable metering; future equipment provisions; what defines loss of capacity; and acceptable outage duration. Do not turn these questions into scope without authorization.
