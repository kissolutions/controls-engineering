---
title: PLC point allocation and I/O counting — proposed schema
page_type: engineering-data-contract
page_status: draft
---

# Point allocation and hardware sizing (P9) — candidate v0.1

**Status:** Draft only; **Equipment_Device_Points_Template_v1.0.xlsx remains the official workbook** until a separately accepted workbook version is released. This document records a proposed relationship model for pilot testing.

A Point's `Endpoint Device Internal ID` is **not** necessarily the controller, panel, I/O card or source device. Keep these distinct:

| Proposed field / relationship | Meaning | Example categories |
|---|---|---|
| Producing/source Device ID | Physical equipment/device from which the signal originates | flow meter, breaker contact, drive |
| Physical termination Panel ID | Physical cabinet or marshalling point where field wiring terminates | PLC-01, remote rack cabinet |
| I/O module/rack ID and channel | Actual selected physical I/O resource, may be unassigned at takeoff | 5069-IB16 module channel 3 |
| Logic owner/controller ID | Processor/system that owns tag interpretation or control | main PLC, dedicated controller |
| Count disposition | **Base / Excluded / Conditional** from current physical I/O quantity | control-scope confirmation pending |
| Allocation review | Candidate / Verified / Accepted, with source/issue links | review boundary |

**Counting algorithm:** Count `Base` points that require a **real physical I/O channel**, grouped by owning panel/rack and signal module class (DI/DO/AI/AO, specialty, safety). Network data points are inventory records **but not physical channels**. Excluded points are not counted; Conditional points appear in a **separate contingency subtotal**, never silently in or out of base. Distinguish dual/backup sensors, dry vs powered contacts, isolated circuits, pulse/frequency and special signal requirements before selecting module families. Count future/reserved channels separately from spare-percentage allowances to avoid double counting.

**Optional derived I/O summary** (next workbook release): panel, controller, rack and module class; Base physical channels, Conditional channels, installed slots/channels, named reserves, spare percentage (editable design assumption), available spare; capacity margin and review state. The summary is a **view**, not an additional point inventory or equipment register.

**Open design questions:** how to represent shared marshalling/panel crossings; owner of read-only network values; whether the point is logically referenced by multiple controllers; and per-module terminal-side electrical compatibility. Validate on a real project before normalizing the published schema.
