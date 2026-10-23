---
title: Generator and ATS status monitoring via power meter — conditional design playbook
page_type: playbook
page_status: draft
---

# ATS / generator monitoring via power meter (P4)

**Purpose:** evaluate whether generator, ATS position and tank-status indications can be collected using an existing power meter with suitable optional status-input hardware. This is an **engineering option**, not a universal default or a proven product configuration.

## Required verification before selection

1. Read ATS and generator submittals: exact make/model, controller and **documented** position/ready/fault auxiliary contacts. Controller display does not prove available terminals or isolated contacts.
2. Obtain the as-found electrical interface: dry/wet, DC/AC, voltage/current, isolation, contact state and fail-state. Match to meter option-card limits; **never** use an AC powered contact on a DC-only status input.
3. Confirm installed meter model, option-card quantity and **two-slot budget**, available status inputs, communication path and required Modbus register/point mapping. If full, expansion requires a redesign or replacement card.
4. Confirm physical voltage measurement location. Generator-source voltage indication is not necessarily proof that the **generator engine is running** or available under load. Use a dedicated verified engine-run/status contact if the owner's definition requires it.
5. Verify CT class/ratio/shorting facilities, voltage-input protection, supply source and actual option-card count. Unknowns become Issues/RFIs, not assumed channels.

## Candidate point allocation

A suitable isolated ATS position auxiliary contact may use one verified meter input per required position or state. Low-fuel may use one appropriately isolated field contact when the owner provides compatible tank/level equipment. Derive a generator-voltage-present status **only** if the meter reads the correct generator source, its voltage threshold and loss behavior are approved, and that state satisfies the owner's intent.

**Required deliverables:** contact and signal matrix; source-backed point schedule; option-slot budget; interlock/indication distinction; communications map; commissioning tests for open/closed/failed/unpowered states.

**Invalidation:** contact absent or wrong electrical type; meter measures load/utility rather than generator source; option card/inputs unavailable; communications mapping unverified; or engine-run semantics require a discrete engine contact.
