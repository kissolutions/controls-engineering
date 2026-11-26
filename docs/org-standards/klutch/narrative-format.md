---
title: Klutch Controls Narrative Format
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Controls Narrative Format

The controls narrative sits in the narrative position of each engineering block (see [Document model](document-model.md)). It always uses the same section order, so the narratives read alike from system to system.

## Section order

| # | Section | Fixed or variable |
|---|---|---|
| 1 | Overview | Fixed |
| 2 | Requirements | When the system has M/E references or design specifications to cite |
| 3 | Operating modes | Fixed |
| 4 | System sections | Variable: as many as the system needs |
| 5 | Setpoints | Fixed |
| 6 | Alarms | Fixed |

## 1. Overview

A short description of the system and its controls:

- what the equipment is and what it serves;
- what Klutch controls, what it only monitors, and what is controlled by others (packaged controls, drives with their own logic);
- the controller(s) and how they connect to the SCADA system;
- what is hardwired and independent of the controller (safety circuits, fire alarm shutdown).

No drafting or review language ("this draft", "proposed") on an issued sheet.

## 2. Requirements

References taken from the mechanical and electrical drawings and specifications go in their own section of the narrative, titled for what they are (for example "Requirements" or "Design Specifications"), not scattered through the system sections. Each reference gives the source and locator (document, sheet or section) and what it requires, so the narrative's control can be traced to it. Where the narrative departs from a reference, say so and cite the precedence override.

## 3. Operating modes

The basic state machine, as a table: one row per mode, with the condition that enters it, what the system does in it, and where it goes next.

| Column | Content |
|---|---|
| Mode | Mode name |
| Entered when | The condition, in point and word names (`TRIP_WORD > 0`, `OCC_UNOCC = 1`) |
| What the system does | Outputs in this mode: fan or pump, valves, dampers, loops held or released |
| Leaves to | Next mode(s) and the condition for each |

The standard mode set is SAFETY, FREEZE, DISABLED, ALARM, READY, STARTUP, RUN, STOPPING and ABORTING.

- **Engineering owns the required behavior:** the approved narrative states the modes, transitions, interlocks, stopped positions and alarm actions this system must have. It is the requirement the program is checked against.
- **The logic domain owns the implementation:** the implementation state machine and reusable programming patterns (`kissolutions/bas-logic-gen`, when installed and selected for the project).
- The logic handoff names the approved engineering revision, the logic revision and any unresolved decisions. A logic change that changes required behavior comes back through engineering review; a programming change never silently changes the requirement.

## 4. System sections

As many sections as the system needs, named by function. For example, an air handler: Start & Stop, Fan Speeds, Heating & Cooling, Safeties. Each section describes the control in steps or short rules, using signal names for points and the setpoint names from section 5.

Write rules that are required by code or standard as rules, not as options (for example: heating and cooling never run at the same time).

## 5. Setpoints

One table of everything an operator needs to operate the system: setpoints and tunables (deadbands, proof delays, ramp times, alarm limits), whether adjustable by the operator, set by TAB or fixed at commissioning.

| Column | Content |
|---|---|
| Name | Setpoint or tunable name. Follows the owner naming standard when it is adjustable by others, a TAB point, needed for external control or trended ([Naming](naming.md)) |
| Purpose | What it sets |
| Default | Value and units |
| Adjusted by | TAB, operator (SCADA), or fixed at commissioning |

## 6. Alarms

One table of every alarm.

| Column | Content |
|---|---|
| Alarm | Alarm name |
| Source | Point or condition |
| Limit / delay | Threshold and time delay |
| Type | Trip (shuts the system down) or Warning (monitoring only) |
| Action / notes | What the system does, and reset |

## Before issue

- Every mode states its outputs, including valve positions when stopped.
- Every alarm states its type, limit and delay.
- Every setpoint and tunable used in the text is in the setpoints table with a default.
- Every setpoint says what it controls (no ambiguous names such as a bare `STPT` used for both discharge air and room).
- No "proposed", "TBD" or drafting language remains unless it is an open item agreed with the owner.

## Trial status

The table column sets above are adopted for trial use (owner, 2026-11-26); there was no prior standard. Revise them from project use and record changes in the profile CHANGELOG.
