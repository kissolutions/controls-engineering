---
title: "MODBUS-001 — Modbus Communications Fundamentals & Network Engineering"
document_type: canonical-course-syllabus
course_id: MODBUS-001
syllabus_version: "0.1.0"
status: draft
domain: communications/modbus
date: 2026-10-24
---

# MODBUS-001 — Canonical Course Syllabus

**Status:** Draft curriculum specification for owner/subject-matter review. This document defines the **intended learning scope and outcomes**; it does not certify a student, approve an engineering design, or replace a technical reference.

## 1. Purpose and authority

Teach an engineer or field technician to understand, design, commission, and systematically diagnose a Modbus RTU network—including one accessed through Modbus TCP gateways—using defensible engineering calculations and documented field evidence.

This syllabus is the **single course-level curriculum blueprint**. It describes *what must be learned and demonstrated*, not exactly how each lesson must appear on a screen. Audience-specific courses, scenario exercises, instructor guides, quizzes, and HTML presentations are **derived variants** of this syllabus.

| Layer | Responsibility | Change rule |
| --- | --- | --- |
| **Canonical engineering sources** | Protocol facts, calculation methods, domain playbooks, manufacturer-specific limitations | Changed only in their owning framework/document |
| **This syllabus** | Learning objectives, module coverage, competencies, required evidence | Version through curriculum review |
| **Course manifest** (`course.json`) | Selected module order, navigation IDs, source references, scenario selection | Generated or reconciled against an identified syllabus revision |
| **Lesson / scenario / quiz content** | Explanations, interactive demonstrations, cases, questions and feedback | Derived for the chosen audience and scenario; never silently changes the syllabus |

The engine is a **presentation mechanism**, not the curriculum authority. The syllabus must remain useful whether delivered as interactive HTML, instructor-led instruction, a field workshop, or an internal knowledge-check package.

## 2. Intended audiences and prerequisites

**Baseline audience:** Controls engineers, BAS/PLC integrators, commissioning personnel, and technically qualified field service personnel.

**Recommended prerequisites:** Basic electrical safety; low-voltage wiring and instruments; fundamental Ethernet/IP concepts; reading equipment schedules and manufacturer documentation. No prior Modbus expertise is assumed for the foundational track.

**Variable depth:** Time, required mathematics, field practice, and assessed outcomes depend on the audience profile (Section 8). Do **not** prescribe one universal course duration or declare a universal passing score here.

## 3. Course learning outcomes

On successful completion of an appropriately scoped and assessed variant, the learner should be able to:

| ID | Learning outcome |
| --- | --- |
| **LO-01** | Distinguish Modbus RTU, Modbus TCP, RS-485 electrical signaling, TCP/IP connectivity, and BACnet MS/TP bus access without conflating them. |
| **LO-02** | Explain RTU master/slave request-response behavior, device addresses, function codes, register conventions, and limits of automatic discovery. |
| **LO-03** | Review an RS-485 segment for supported topology, termination, biasing, polarity, reference, shielding, isolation, power, and unit loading. |
| **LO-04** | Trace TCP/RTU gateway requests through IP/port, Unit ID, serial-port routing, function, register offset, and response interpretation. |
| **LO-05** | Estimate RTU polling time, nominal utilization, and the impact of timeouts, retries, and offline devices; identify assumptions and limitations. |
| **LO-06** | Apply repeatable design and troubleshooting playbooks, distinguishing observed facts from hypotheses, and preserve field/change evidence. |
| **LO-07** | Explain an engineering recommendation or fault diagnosis using a topology, configuration schedule, measurement or transaction record, and appropriate calculations. |

Assessment of a subset of outcomes qualifies **only** that variant's stated competence—not the entire canonical course.

## 4. Canonical course structure

The default structure has **four sections**, matching the KIS Training Engine's navigation. Section identifiers and module IDs should remain stable across variants; a variant may hide or abbreviate presentation modules without renumbering them.

### 01 — Academic Learning: concepts before procedures

Each lesson has a learning objective, prerequisite concepts, a technical reference, and at least one explanation/example. Interactive diagrams are recommended, not the source of engineering truth.

| Module | Stable lesson key | Required concepts | Learner should be able to... |
| --- | --- | --- | --- |
| **01.0 Course overview** | `overview` | End-to-end architecture, course method, limits of training simulations | Identify the TCP client, gateway, RTU segment, and sensor in a given scenario. |
| **01.1 Modbus fundamentals** | `principles` | RTU vs TCP; request/response; one coordinated RTU master; addressing and broadcast; Modbus vs MS/TP; no generic RTU discovery | Explain who initiates a transaction and why RS-485 wiring alone does not determine a protocol. |
| **01.2 RS-485 physical networks** | `physical` | Differential bus, linear trunk and stubs, two-end termination, bias, A/B conventions, signal reference, shield, isolation, power, electrical unit loads | Identify electrical failure candidates from a wiring/topology diagram and state safe verification steps. |
| **01.3 Registers and addressing** | `registers` | Coils, discrete inputs, input/holding registers; FC03/FC04; 0-/1-based notation; 16-/32-bit values; signedness; scale; word order | Formulate and interpret a read request using a specific vendor register map. |
| **01.4 TCP-to-RTU gateways** | `gateway` | MBAP Unit ID, IP and TCP port, RTU CRC/framing differences, mapping to serial port, queueing, client limits and gateway exceptions | Trace a transaction and separate gateway reachability from downstream device communication. |
| **01.5 Polling and fault budgets** | `performance-basics` | Baud and bits per character, register grouping, scan intervals, transaction turnaround, queueing, timeouts, retries, nominal vs degraded cycles | Explain why a nominally healthy network may fail the desired update interval after device loss. |

**Optional extensions, not mandatory in every variant:** Packet-level frame decoding, waveform analysis, complex gateway routing modes, 32-bit/float endianness labs, data quality/alarming, network segmentation, and redundancy implications. Extensions need their own objectives and source references before publication.

### 02 — Engineering Playbooks: guided application

The presentation engine should expose each step through a **left-to-right clickable flowchart**, with stable step IDs and independently addressable lesson content. The source playbook defines the steps; a training animation does not supersede it.

**02.A — Modbus RTU Network Design** (canonical ten-step playbook):

| Step | Topic | Typical learner evidence |
| --- | --- | --- |
| D01 | Device inventory and exact documentation | Device/model/firmware/register schedule |
| D02 | Gateway, serial ports, and physical topology | As-designed network diagram |
| D03 | Capacity by independent constraints | Address, unit-load, gateway and performance checks |
| D04 | Compatible serial parameters | Baud, data bits, parity and stop-bit schedule |
| D05 | Slave IDs and address domains | Address schedule |
| D06 | RS-485 electrical design | Wiring, terminations, bias, reference and isolation notes |
| D07 | TCP-to-RTU gateway routing | Unit ID/port configuration |
| D08 | Poll schedule definition | Functions, offsets, quantities, scan targets |
| D09 | Nominal and degraded performance | Timing and failure-case calculation |
| D10 | Validation and handoff | Commissioning tests, saved configuration and as-left records |

**02.B — Modbus Communications Troubleshooting** (canonical source stages):

| Step | Topic | Typical learner evidence |
| --- | --- | --- |
| T00 | Preserve the as-found state and protect operations | Backup/configuration/evidence log |
| T01 | Reconcile the design baseline | Known settings, constraints and unresolved items |
| T02 | Separate Ethernet, TCP, gateway and serial layers | Layer-by-layer test record |
| T03 | Interpret data, exceptions and timeouts | Evidence-supported response classification |
| T04 | Use failure patterns to frame hypotheses | Affected-device map and ranked checks |
| T05 | Controlled isolation and retesting | Approved test sequence and restoration notes |
| T06 | Confirm exit criteria and as-left condition | Valid reads, measured cycle and documented correction |

Include safe-isolation prerequisites. Contiguous offline nodes **suggest** a cable or power boundary but are not proof: RS-485 nodes do not forward messages. A successful ping does not demonstrate RTU device health.

### 03 — Engineering Calculators: assumptions, equations, interpretation

Calculators teach engineering reasoning; a single output without assumptions is not sufficient.

| Module | Purpose | Minimum learner action |
| --- | --- | --- |
| **03.1 RTU network performance** | Estimate wire time, transaction/scan time, utilization and indicative minimum baud | Supply registers, baud, framing, turnaround and scan target; interpret limitations |
| **03.2 Timeout and retry impact** | Estimate degraded polling with offline devices and retry policies | Compare nominal and failed-device scenarios against scan target |
| **03.3 RS-485 electrical loading** | Sum receiver unit loads and compare with documented electrical capacity | Calculate loading while explicitly separating it from manufacturer device-count limits |

Use the canonical calculator pages for formulas, input definitions and caveats. A screening estimate is **not** a device manufacturer's capacity certification or commissioned performance measurement.

### 04 — Knowledge Checks: prove the correct competency

Assessment items are **tagged by both academic chapter and engineering domain**. One question may appear in different views without becoming a duplicate source record.

| Domain | Example competence demonstrated |
| --- | --- |
| **04.1 Protocol and data model** | Choose function/offset, identify client/master and decode a documented register |
| **04.2 RS-485 electrical** | Identify termination/topology or polarity hypotheses and safe tests |
| **04.3 Gateway and diagnostics** | Interpret ping, port 502, response, exception and timeout evidence |
| **04.4 Polling and performance** | Calculate utilization and degraded-cycle implications |

A variant may use formative self-checks, graded knowledge checks, practical troubleshooting demonstrations, or an engineering design review. It must declare the **assessment method, covered learning outcomes, and pass/acceptance criteria**. Do not infer competency from page visits or completed animations alone.

**CAP-01 — Applied scenario:** Baseline synthetic case: a TCP-to-RTU gateway communicating with **30 vibration sensors**, with documented polling requirements and selectable faults. Learners should produce a network/configuration sketch, an initial polling estimate, a diagnostic sequence, and an evidence-backed resolution or design recommendation. The sensor count is an instructional scenario, **not** a universal electrical, gateway or performance limit.

## 5. Required cross-section traceability

For each delivered course variant, maintain a matrix relating:

`learning_outcome → academic lesson(s) → playbook step(s) → calculator/exercise(s) → knowledge check or observed evidence`.

At minimum, every outcome claimed by a variant needs a teaching opportunity and at least one matching assessment. A chapter may be presented briefly, but omitting a required learning objective from assessment must be explicit.

## 6. Source documents and authority

### Authoritative technical references

- [KIS Modbus RTU field integration reference](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-rtu.md)
- [KIS Modbus TCP field integration reference](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-tcp.md)
- [KIS Modbus RTU Network Design playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-rtu-network-design.md)
- [KIS Modbus Communications Troubleshooting playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-communications-troubleshooting.md)
- [RTU Network Performance calculator method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-network-performance.md)
- [RTU Timeout and Retry Impact method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-timeout-retry-impact.md)
- [RS-485 Electrical Loading method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/rs485-electrical-loading.md)

These source pages are currently draft engineering references. Each course variant must **capture the actual revision** consulted (commit/blob SHA and vendor-document revision where applicable), rather than relying only on moving `main` URLs. For the first v0.3 build, `course.json` records these references.

### Explicit exclusions

This syllabus does **not** establish a universal maximum node count, a universally acceptable serial polling utilization, manufacturer-specific gateway behavior, a legal/code compliance standard, or authorization to modify live systems. Device-specific claims require the correct manufacturer documentation; project-specific limits and acceptance belong to project engineering records.

## 7. Reusable instructional pattern

For each module, author the following components as warranted by the chosen variant:

1. **Concept:** Plain-language explanation and vocabulary.
2. **Mental model:** Diagram, comparison, table or worked example.
3. **Interaction:** Adjustable topology, simulation, register translator or calculator.
4. **Application:** Relevant playbook step or scenario task.
5. **Check:** One or more questions / observed actions tied to explicit outcomes.
6. **References:** Canonical document links with revisions, assumptions and limitations.

Not every audience requires equal depth in all six components. **The course objectives are stable; instructional depth and presentation are variable.**

## 8. Audience- and scenario-driven course variants

A course generator or human author should start with **this** syllabus, then apply a named variant profile. The profile is a set of inputs, not a fork of the canonical syllabus.

| Profile input | Supported examples | Effect |
| --- | --- | --- |
| **Audience** | Field technician; BAS/PLC integrator; design/PE reviewer; PM/technical reviewer | Language, prerequisite assumptions, depth and role-specific evidence |
| **Starting competency** | New to Modbus; familiar with BACnet MS/TP; experienced PLC integrator | Condense familiar prerequisites, add comparative examples |
| **Goal** | Explain fundamentals; commission; troubleshoot an outage; design a new network; review a submittal | Select and emphasize outcomes and playbook steps |
| **Scenario** | Synthetic 30-sensor vibration network; brownfield intermittent bus; BAS gateway integration; PLC data acquisition | Equipment maps, injected faults, register schedules and design constraints |
| **Depth / time** | Orientation; field-practitioner; deep engineering workshop | Optional modules, mathematics, number of cases and review exercises |
| **Delivery** | Self-paced HTML; instructor-led; mobile field reference; facilitated lab | Layout, navigation, instructor prompts, practice and assessment |
| **Assessment** | Formative checks; practical diagnosis; documented design exercise | Required evidence, outcome coverage and stated acceptance criteria |

Illustrative profiles:

- **Field Troubleshooting Workshop:** Emphasize 01.2, 01.4, 02.B, 03.2 and diagnostic checks. Use a brownfield fault scenario; retain foundational concepts needed to troubleshoot safely.
- **Controls Network Design / PE Review:** Emphasize all of 01, 02.A, 03.1–03.3 and CAP-01. Require topology, configuration schedules, manufacturer capacity verification and nominal/degraded timing evidence.
- **Quick BAS-to-Modbus Orientation:** Emphasize 01.1, 01.3, 01.4 and gateway diagnostics, using an explicit comparison to BACnet MS/TP. Mark unassessed design competencies as **not covered**, not passed.

A variant may also substitute a specific manufacturer/model, provided its actual manuals and firmware are identified. Never automatically assign a real device undocumented sample capacities or register maps.

## 9. Variant generation contract (human or AI)

1. **Select the canonical syllabus revision.** Record course ID and syllabus version.
2. **Provide the profile.** Audience, prerequisites, goals, scenario, time/depth, delivery and assessments; flag unresolved inputs instead of inventing project constraints.
3. **Resolve and freeze source revisions.** Collect the canonical references and any manufacturer/project source documents allowed for the course.
4. **Build the coverage plan.** Select objectives/modules, set depth and required evidence, and document omissions explicitly.
5. **Generate course artifacts.** Derive manifest, academic lessons, horizontal playbook steps, interactive scenarios/calculator bindings, question set and answer feedback. The engine remains reusable.
6. **Validate.** Confirm stable IDs, source fidelity, scenario consistency, technical equations, safety notes, navigation/interactions, mobile readability and assessment coverage.
7. **Review and release a variant.** Record variant ID/version, syllabus/source revisions, reviewer, delivery type, assessment rules and unresolved limitations.

**Regeneration rule:** Do not modify `SYLLABUS.md` merely because a presentation is regenerated. Proposed changes to course outcomes or canonical scope must be separately reviewed and versioned. Previously accepted course variants remain reproducible against their recorded inputs and source revisions.

### Suggested variant identity

```yaml
course_id: MODBUS-001
syllabus_version: 0.1.0
variant_id: modbus-001-field-troubleshooting
variant_version: 0.1.0
audience: field-technician
goal: diagnose-rtu-network
scenario: brownfield-gateway-outage
depth: practitioner
delivery: interactive-html
source_snapshot: required-at-generation
included_outcomes: [LO-01, LO-02, LO-03, LO-04, LO-06, LO-07]
assessment: practical-diagnosis-plus-formative-checks
status: draft
```

This is an **illustrative profile schema**, not a validated machine-readable contract.

## 10. Course acceptance and change management

Before calling **MODBUS-001** a complete released course, confirm:

- Owner/SME acceptance of syllabus objectives and intended audience.
- Technical fidelity of lessons and scenarios to versioned canonical references.
- Both playbooks represented with navigable, distinct steps and safe operational preconditions.
- Each calculator independently checked against its canonical method, with assumptions visible.
- Explicit outcome-to-lesson-to-evidence mapping for each published variant.
- Knowledge checks and applied scenarios reviewed for accuracy and declared assessment scope.
- Interactive course tested on desktop and mobile; any offline build reproducible.
- Known course limitations and unresolved manufacturer-specific questions documented.

**Document maturity:** The frozen training engine v0.2 is an accepted interaction prototype, not acceptance of this draft syllabus or any newly generated technical course.

## Related training artifacts

- [Training architecture](../../ARCHITECTURE.md)
- [MODBUS-001 course package](README.md)
- [Frozen v0.2 training engine baseline](../../engine/baselines/v0.2/BASELINE.md)
- [v0.3 course manifest and source snapshot (development branch)](https://github.com/kissolutions/controls-engineering/blob/work/modbus-001-vertical-slice/training/courses/modbus-001/course.json) *(not yet merged into `main`)*
