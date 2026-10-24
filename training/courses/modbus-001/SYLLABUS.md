---
title: "MODBUS-001 — Modbus Communications Fundamentals & Network Engineering"
document_type: canonical-course-syllabus
course_id: MODBUS-001
syllabus_version: "0.2.0"
status: draft
last_updated: 2026-10-24
domain: communications/modbus
delivery_contract: ../../COURSE-ASSEMBLY-CONTRACT.md
---

# MODBUS-001 — Canonical Course Syllabus

**Status:** Draft for engineering/instructor review.  
**Authority:** Canonical **curriculum definition** for MODBUS-001, not a protocol specification, manufacturer manual, training application, or accepted field procedure.  
**Intended scale:** From a focused field briefing or one-hour lunch-and-learn to a hands-on **four-hour/half-day** workshop, with optional deeper engineering extensions.

> **Design principle:** Specify what a learner must understand, practice, and demonstrate in small, stable teaching units. The KIS Training Engine decides how to present those units; a variant profile decides which units to emphasize for an audience and scenario. Do not duplicate or invent engineering authority when regenerating course content.

## 0. How to use this syllabus

Three compatible views of the same curriculum:

1. **Five instructional strands** define the teaching content originally developed for this course: Understanding Modbus; RS-485 and Network Addressing; Modbus TCP and Gateways; Building a Modbus Request; Troubleshooting Modbus Networks. These are concepts, not fixed presentation chapters.
2. **Four engine sections** organize the delivered interface: `01 Academic Learning`, `02 Engineering Playbooks`, `03 Engineering Calculators`, and `04 Knowledge Checks`.
3. **Atomic learning blocks and labs** (`F01`, `E01`, `R01`, `G01`, `X01`, `LAB-01`, etc.) can be reordered, expanded, condensed, or selected without inventing a new course or changing their identity.

A four-hour bench training may teach a concept inside a lab; a 30-minute field briefing may show the same concept as a compact diagnostic card. Neither changes the canonical fact or learning outcome.

**Course package:** [README](README.md). **Engine contract:** [Course Assembly Contract](../../COURSE-ASSEMBLY-CONTRACT.md). **Current HTML prototype:** v0.2 is a frozen interaction reference; the v0.3 course manifest and individual lesson stubs are implementation work, not independent curriculum authority.

### Terminology and stable IDs

| Term | Meaning |
| --- | --- |
| **Learning outcome** (`LO-xx`) | Competency the learner is expected to demonstrate. |
| **Learning block** (`F/E/R/G/T-xx`) | Selectable concept, diagram, demonstration, or short practice. Its identity survives course regeneration. |
| **Academic chapter** (`01.x`) | Default sidebar grouping for related blocks; may be reordered or abridged. |
| **Playbook step** (`D01–D10`, `T00–T06`) | Training presentation of a separately governed engineering procedure. |
| **Calculator** (`CAL-01–03`) | Interactive teaching view of a canonical method, with assumptions and limits. |
| **Lab** (`LAB-00–07`) | Practical instruction plus required observations and evidence. |
| **Knowledge check** (`KC-xx`) | Question, diagnostic choice, oral explanation, or reviewed work product, tagged to a block/outcome. |
| **Variant** | A versioned presentation derived from this syllabus plus a profile, source snapshot, and selected activities. |

**Compatibility rule:** The established academic lesson keys `overview`, `principles`, `physical`, `registers`, `gateway`, and `performance-basics` remain valid. New micro-block IDs sit *inside* those lessons; do not repurpose existing keys.

## 1. Course intent, audience, and evidence

### Learning objective

The learner should be capable of tracing a Modbus request from the calling application to a physical sensor and back, interpreting the result, identifying likely failure layers without guessing, and supporting basic network design and performance decisions.

### Intended users

- **Field technician:** Connect safely, obtain a known-good read, isolate common failures, preserve as-found/as-left evidence.
- **BAS / PLC integrator:** Map registers and gateways, understand serial constraints, plan polling and client integration.
- **Controls designer / PE:** Verify electrical, configuration, gateway, and performance capacities independently; document engineering decisions and acceptance.
- **Project reviewer / instructor:** Recognize which evidence supports each claimed result and which limits still require product documentation.

**Prerequisites:** Basic low-voltage safety, wiring/terminal familiarity, a working understanding of IP networks, and the ability to read a manufacturer's sensor and gateway documentation. The foundational track does not assume prior Modbus experience. Lab configuration must be matched to the exact hardware and software versions in use.

### Learning outcomes

| ID | After the relevant training and assessment, the learner can... |
| --- | --- |
| **LO-01** | Distinguish protocol, physical layer, host interface, and gateway roles; compare Modbus RTU/TCP with BACnet MS/TP without assuming equivalence. |
| **LO-02** | Explain request-response transactions, serial master/slave behavior, local device IDs, function codes, register types, and data representation. |
| **LO-03** | Identify RS-485 topology, termination, biasing, polarity, reference, shielding, power, isolation and electrical-loading concerns; propose safe verification steps. |
| **LO-04** | Trace and test a TCP-to-RTU request using IP/TCP port, Unit ID, serial-port route, function, register address and quantity. |
| **LO-05** | Estimate normal and degraded serial polling time, interpret headroom, and distinguish protocol address range from electrical, gateway, and performance capacity. |
| **LO-06** | Apply KIS network design and communications troubleshooting playbooks in an evidence-first sequence, including preservation/restoration. |
| **LO-07** | Present an engineering recommendation or fault diagnosis using verified settings, transaction results, topology, calculations, and unresolved questions. |
| **LO-08** | Safely transition between a direct USB-to-RS-485 bench master and a gateway-managed RTU segment, without accidentally creating competing serial masters. |

**Claim rule:** A short variant is not automatically a complete course. Its completion or assessment may claim only the outcomes it actually teaches and tests.

## 2. Mandatory conceptual floor — never silently omit

Every variant contains a proportionate, compact treatment of **CF-01 through CF-08**, even if some appear as a preflight card rather than full lessons. When a topic becomes a focus, expand its linked blocks and verify its nuance.

| Floor ID | Non-negotiable understanding | Core blocks |
| --- | --- | --- |
| **CF-01** | RS-485 is an electrical interface, not Modbus; conventional RTU uses one coordinated serial master, unlike MS/TP token passing. | `F01`, `F02`, `F04` |
| **CF-02** | Addresses, data tables, function codes, starting offsets and quantities together define a request; zero/one-based notation can differ. | `F03`, `R01–R04` |
| **CF-03** | RS-485 topology, two-end termination, bias, reference, A/B conventions and power have independent failure modes. | `E01–E05` |
| **CF-04** | An RTU slave ID's usual 1–247 address range does **not** establish permissible node counts, gateway routes or polling bandwidth. | `F03`, `E06`, `G04` |
| **CF-05** | Gateway ping, TCP socket reachability and a valid Modbus read establish **different things**; a responding gateway may generate exceptions itself. | `G01–G03`, `X01`, `X02` |
| **CF-06** | Timeout is not a Modbus exception; codes 01/02/03 differ from gateway path/target reports 0A/0B. | `X02` |
| **CF-07** | Healthy polling estimates do not prove degraded/failure-case performance; retries, queueing and multiple clients matter. | `G05`, `X04` |
| **CF-08** | Preserve configuration and field evidence, use approved testing boundaries, avoid unsafe writes and do not add independent serial masters to an active RTU trunk. | `G06`, `X05`, `LAB-00` |

**Nuance rule:** A variant that introduces a concept must not teach its oversimplified form as a universal truth. For example, a measured ~60 Ω across an isolated bus can be consistent with two 120 Ω terminations but does not prove they are at the correct physical ends; A/B labeling varies by manufacturer; a contiguous outage suggests but does not prove a cable break.

## 3. Detailed academic instruction — Section 01

The five original instructional strands are represented by the following default six academic chapters. **Presentation order is flexible:** for a gateway-focused audience, `01.4` can precede `01.3`, provided prerequisite concept blocks are included.

A block includes **Teach / show**, **Try / discuss**, and **Proof**. Typical exposure for a single block is 4–10 minutes when taught separately; time is **not additive** when a block is embedded in a hands-on lab.

### 01.0 — Course overview and learning method (lesson key: `overview`)

**Purpose:** Establish a common system vocabulary, a concrete diagram and the difference between simulation, bench observation, field evidence and source documentation.

| Block | Teach / show | Try / discuss | Proof |
| --- | --- | --- | --- |
| **O01** | Trace BAS/PLC client → Ethernet → Moxa gateway → RS-485 trunk → sensors; show the direct USB master alternative. | Point to the active initiator and the responding device. | Label the transport and control boundary on one diagram. |
| **O02** | Source authority and evidence tiers: documented, observed, inferred, unknown. | Identify what is known versus assumed about a sample sensor map. | Record an open technical question instead of inventing a value. |
| **O03** | Lab and field safety boundaries; never write an unknown register or modify active production controls for an exercise. | Classify an acceptable bench test versus an unauthorized plant-network intervention. | Instructor-approved test boundary and as-found record. |

**Anchor illustration:** Two illustrative vibration sensors with unique RTU slave IDs **7 and 8**, sharing a documented register-map structure *only if the chosen devices actually support it*. A Moxa gateway IP such as **192.168.1.50** is a **synthetic isolated-lab example**, not a client setting.

### 01.1 — Understanding Modbus (lesson key: `principles`)

**Teaching question:** What exactly is Modbus, who initiates communications, and what distinguishes it from BACnet or Ethernet?

| Block | Teach / show | Try / discuss | Proof |
| --- | --- | --- | --- |
| **F01** | Protocol versus transport: Modbus RTU over a serial link; Modbus TCP over IP; RS-485 is electrical signaling. | Relabel a diagram with “protocol,” “transport,” “device” and “gateway.” | Correctly separate the four layers. |
| **F02** | Request-response; one coordinated serial master, addressed slaves, frame timing, CRC on RTU, no token passing. | Predict which node speaks next in an RTU transaction. | Explain why two uncoordinated serial masters are a problem. |
| **F03** | Slave IDs 1–247, broadcast address 0 with no reply, address scope per segment; no generic RTU discovery or BACnet-style system-wide Device Instance. | Compare sensors 7/8 on one trunk and the same IDs on two different ports. | Distinguish local address validity from gateway route and physical capacity. |
| **F04** | BACnet MS/TP contrast: MAC versus BACnet Device Instance; token passing versus a single serial poller; points/objects versus coils/registers. | Translate an MS/TP mental model into Modbus terminology. | State at least two things that cannot be assumed equivalent. |
| **F05** | Two-device transaction sequence and response interpretation. | Switch the request between hypothetical ID 7 and ID 8 using the same documented register block. | Explain why a different Unit ID changes the selected sensor, not the register-map meaning. |

**Minimum concepts:** Four data tables (coils, discrete inputs, input registers, holding registers); read versus write; no standardized point-name discovery; identify actual device documentation. Device address 247 is a protocol notation fact, **not** permission for 247 installed devices.

### 01.2 — RS-485 and Network Addressing (lesson key: `physical`)

**Teaching question:** What makes the physical serial network reliable, and what information must be distinguished from protocol identity?

| Block | Teach / show | Try / discuss | Proof |
| --- | --- | --- | --- |
| **E01** | Half-duplex differential communication, transceiver purpose, serial formats: baud, data bits, parity and stop bits. | Read the serial configuration schedule for the laptop, gateway and sensors. | Identify a common compatible setting from actual manuals. |
| **E02** | Supported trunk topology, physical cable order, stubs, cable type/length and repeaters; physical order differs from ascending slave IDs. | Put sensor 8 physically before sensor 7 on the drawing. | Locate first/last physical node without using address order. |
| **E03** | End termination (normally two electrical ends), bias/fail-safe behavior, consequences of missing/extra termination. | Compare ideal isolated readings for two, one or three 120 Ω resistors; discuss why readings are not conclusive. | State what an ohmmeter reading **does and does not** establish. |
| **E04** | A/B nomenclature varies across vendors; signal common/reference, common-mode limits, shield, grounding and isolation follow product rules. | Compare two incompatible A/B naming diagrams. | Request vendor pinouts rather than guessing polarity. |
| **E05** | Stable sensor supply; power distribution versus serial wiring; safe measurement boundaries. | Compare a loss-of-power group with a cable fault symptom. | Record evidence that separates the two hypotheses. |
| **E06** | Electrical unit loads, gateway limits, cable limits, repeaters/isolators versus TCP bridges and true protocol converters. | Calculate fractional-load totals separately from supported node count. | Name at least three independent capacity checks. |

**Worked physical pattern:** A contiguous group of sensors stops communicating. Hypotheses include a shared cable termination/junction, common power, polarity or a gateway-port issue; the pattern alone does not prove that a sensor has failed or that serial traffic passes “through” upstream sensors.

### 01.3 — Building and Interpreting a Modbus Request (lesson key: `registers`)

**Teaching question:** Can the learner build a known-good read without confusing the function, reference label, transmitted address and decoded value?

| Block | Teach / show | Try / discuss | Proof |
| --- | --- | --- | --- |
| **R01** | Four Modbus data tables: 0xxxx coils, 1xxxx discrete inputs, 3xxxx input registers, 4xxxx holding registers; typical functions 01/02/03/04. | Given vendor table, select FC03 vs FC04 for an actual documented register. | Correct function/data-table pair. |
| **R02** | The complete read tuple: client connection, serial slave/Unit ID, function, start offset, quantity, data decoding. | Build a one-line test request for sensor 7, then sensor 8. | Reproducible tuple with no missing fields. |
| **R03** | Displayed “40001” versus protocol offset 0; “40101” versus 100 under the traditional five-digit convention; vendor/driver one-based exceptions. | Translate several labels and explain how to verify the selected convention. | Correct offsets with cited device/map notation. |
| **R04** | Each register is 16 bits; combining registers may require signedness, scale, word order and byte order. | Decode a worked synthetic 32-bit value, then compare to the vendor map. | Raw value, conversion and engineering units documented separately. |
| **R05** | Modbus Poll as an RTU/TCP test client; connection settings, read definitions, traffic/response evidence, read-only exercise posture. | Obtain a supported FC03 or FC04 read through a direct USB-RS-485 connection. | Timestamped test tuple, result and observed reading. |
| **R06** | Exceptions 01/02/03 versus no response; invalid range/quantity is not always a wiring defect. | Intentionally select a *read-only* unsupported request in a controlled simulation or bench. | Distinguish exception, timeout and bad decoding. |

**Teaching artifact:** A reusable “transaction card”:
`transport / endpoint (COM or IP:port) / RTU slave or Unit ID / gateway serial port (if applicable) / serial format / function / starting offset / quantity / format & scale / expected result / actual result / source revision`.

### 01.4 — Modbus TCP and Gateways (lesson key: `gateway`)

**Teaching question:** How does one Ethernet endpoint serve multiple serial devices, and how do you prove which layer is failing?

| Block | Teach / show | Try / discuss | Proof |
| --- | --- | --- | --- |
| **G01** | IP + TCP port (often 502) identifies a network service; an MBAP header carries Unit ID. RTU framing has a CRC; the TCP application frame does not carry that RTU CRC. | Follow one request from a BAS workstation to gateway IP 192.168.1.50. | Identify connection endpoint and downstream Unit ID separately. |
| **G02** | Unit ID-to-serial-port routing, gateway firmware/mode and potentially ambiguous duplicate IDs across two ports. | Draw two sensors 7/8 under one gateway, then under two ports. | Explain when an explicit routing table is necessary. |
| **G03** | Direct serial master versus TCP client-to-RTU-slave bridge; transparent forwarding, register mapping and protocol conversion are different operating patterns. | Identify which exact gateway mode is required for the bench setup. | State mode and source manual before configuration. |
| **G04** | Gateway/model-specific serial-port count, route count, device support, concurrent client connections and queue management. | Show why “can connect 32 TCP clients” does not mean 32 simultaneous transactions on one serial bus. | Separate connection acceptance from downstream serial throughput. |
| **G05** | Progressive layer tests: ping → TCP service → known-good Modbus read → second slave → full polling. | Predict what each pass/fail proves and does not prove. | Correct layer-specific diagnostic decision tree. |
| **G06** | Safe cutover: only one coordinated RTU master controls the segment; save Moxa configuration and isolate test changes. | Transfer from USB master testing to gateway testing without leaving two independent masters connected. | Signed lab handoff/checklist and valid TCP-through-RTU read. |

**Illustrative transaction:** `192.168.1.50:502 / Unit ID 7 / FC03 / offset 100 / quantity 2`; repeat Unit ID 8. These values are illustrative only: a real register must be confirmed against the exact chosen sensor map.

**Gateway nuance:** On multiport devices, overlapping downstream IDs are allowed only when the actual gateway/firmware can disambiguate route selection. An open TCP socket or a successful ping does not prove that either RTU sensor responds.

### 01.5 — Troubleshooting and Network Performance (lesson key: `performance-basics`)

**Teaching question:** What should an engineer test first, and can the network meet its update requirement during failure conditions?

| Block | Teach / show | Try / discuss | Proof |
| --- | --- | --- | --- |
| **X01** | Ethernet/IP, TCP listener, gateway routes, serial wiring, power, slave/Unit ID and register layers. | Start with one known-good request; choose the next test by actual observation. | Layered test plan rather than an unranked list of guesses. |
| **X02** | Valid data; exception 01 illegal function, 02 illegal address, 03 illegal value; 0A gateway path and 0B gateway target; timeouts; who generated the exception may matter. | Sort sample traces by likely origin and next verification. | Explain why a timeout is not a Modbus exception. |
| **X03** | Pattern evidence: all slaves on one port, contiguous physical group, scattered slaves, intermittent updates, wrong-but-valid values. | Given “last working / first failed” positions, propose **multiple** candidate causes. | Evidence-supported ranked hypotheses, not a prematurely declared root cause. |
| **X04** | FC03/FC04 wire bytes, framing bits, turnaround, polling groups, timeout/retry budget, multi-client queueing. | Compare a normal 30-sensor estimate with three offline devices. | Calculate whether the target scan interval is plausible under assumptions. |
| **X05** | Preserve as-found state, choose safe approved isolation, restore settings and test full-cycle operation. | Fill in a short field-evidence record and as-left validation. | Configuration backup, test evidence and outstanding uncertainties. |

**Worked scenario:** Thirty hypothetical vibration sensors, 10 registers/read, 19,200 baud, 8E1 (11 bits/character), 20 ms sensor response allowance, 5 ms additional allowance, five-second target scan. The canonical screening calculation yields ~1.317 s normal cycle (~26.3% nominal loading). With 500 ms timeout and **two additional retries**, three nonresponding devices can increase a simplified cycle to ~5.685 s—beyond the target. This is a modeling exercise, not measured Moxa/sensor behavior.

## 4. Engineering playbooks — Section 02

Playbook steps are **independent selectable teaching units**, presented as a left-to-right flowchart in the HTML engine, each linking to a stable lesson anchor. Their exact procedure, evidence requirements and status remain governed by the source playbook; the syllabus supplies teaching cues and exercises.

### 02.A — Modbus RTU Network Design

| ID | Guided step | Student action / expected work product |
| --- | --- | --- |
| **D01** | Inventory models, firmware and registers. | Identify exact sensor/gateway manuals; create a source-backed device schedule. |
| **D02** | Draw topology: client(s), gateway, ports, physical trunk, power. | Produce a network diagram with physical cable order. |
| **D03** | Screen separate address, electrical, gateway, cable and performance limits. | List each bound and unresolved vendor limit; never collapse into one node count. |
| **D04** | Select common serial mode, baud, parity/data/stop bits. | Configuration schedule based on supported settings. |
| **D05** | Allocate unique addresses within each RTU domain. | Slave-ID and gateway-routing schedule. |
| **D06** | Detail end termination, biasing, reference, shielding, isolation and surge strategy. | Wiring/electrical assumptions and verification notes. |
| **D07** | Configure Unit ID/port route and gateway forwarding behavior. | Mode/routing configuration record and backup. |
| **D08** | Build a poll schedule with function, offset, quantity and interval. | Transaction schedule and expected scan window. |
| **D09** | Screen normal and offline/retry performance plus TCP queueing. | Calculator evidence and decision on segmentation/headroom. |
| **D10** | Plan first/middle/last reads, restart, offline-node and full-load tests. | Commissioning checklist and as-left evidence. |

### 02.B — Modbus Communications Troubleshooting

| ID | Guided step | Student action / expected evidence |
| --- | --- | --- |
| **T00** | Preserve as-found conditions and obtain authorization. | Equipment/configuration versions, observed symptoms, timestamps, backups. |
| **T01** | Check serial, addressing, routing, electrical, gateway and polling baseline. | Separate confirmed settings from unknowns and contradictions. |
| **T02** | Divide by communications layer. | Record ping, TCP listener and representative read; explain limits of each. |
| **T03** | Classify valid data, exceptions and timeouts. | Select next check based on code and likely response origin. |
| **T04** | Use physical/functional failure patterns. | Map working/failing nodes to physical order, ports and power domains. |
| **T05** | Execute approved isolate/test/reconnect plan. | Preserve safe test boundaries and restore termination/bias as appropriate. |
| **T06** | Verify exit criteria. | Normal/degraded cycle, plausible decoded data, backups, as-left configuration. |

**ID rule:** Academic diagnostic blocks use `X01–X05`; `T00–T06` are reserved for troubleshooting **playbook steps**. They are distinct stable identities, not a numbering collision. Generated manifests should also preserve typed unit categories (`academic`, `playbook`, `lab`, `calculator`, `assessment`).

## 5. Engineering calculators — Section 03

The curriculum specifies the skill demonstrated, not a competing copy of the canonical equations. Each generated calculator page shows input units, assumptions, method revision, results, reasonableness checks and limits.

| ID | Calculator lesson | Student inputs | Required interpretation |
| --- | --- | --- | --- |
| **CAL-01** | RTU network performance and indicative baud rate | Device count, requests/device, registers/read, baud, bits/character, turnaround/overhead, target scan interval | Estimate wire time and utilization. Distinguish calculated capacity from observed performance; identify infeasible timing budgets. |
| **CAL-02** | Timeout/retry degradation | Healthy transaction, failed devices, response timeout, additional retries, scan target | Compare nominal/degraded cycle and explain queueing risk. |
| **CAL-03** | RS-485 electrical loading | Receiver quantity, transceiver unit-load ratings, gateway contribution, documented driver/electrical limit | Sum electrical receiver loading while still checking cable and gateway specifications independently. |

**Calculation principle:** Use method links and revision IDs from the [KIS Knowledgebase](#13-technical-source-ownership-and-course-governance). Any default “target utilization” is internal engineering guidance, not a Modbus standard or manufacturer guarantee.

## 6. Knowledge checks and competency evidence — Section 04

Questions may be browsed **by academic chapter or by skill domain** without storing duplicate question truth. Each question has a stable ID, source/answer rationale, difficulty, associated block IDs, outcome IDs and at least one domain tag.

| ID family | Knowledge domain | Acceptable demonstration |
| --- | --- | --- |
| **KC-PROTOCOL** | Roles, Modbus RTU/TCP, MS/TP comparison, identifiers | Explain who sends what and why matching RS-485 wiring is insufficient. |
| **KC-ELECTRICAL** | Topology, power, polarity, termination, bias, reference, loading | Diagnose a diagram and choose defensible physical checks. |
| **KC-REQUEST** | Function, table, 40001/offset and multi-register format | Compose and decode a verified request. |
| **KC-GATEWAY** | IP, TCP port, Unit ID, routing, modes and queueing | Separate host/gateway/serial/slave failures from test evidence. |
| **KC-PERFORMANCE** | Scan budget, retry impacts and electrical capacity | Calculate and interpret both nominal and degraded cases. |
| **KC-PRACTICAL** | Design, commissioning, restoration and root-cause evidence | Present an as-left record or justified design recommendation. |

**Assessment principle:** Attendance and checkbox completion do not prove competency. A variant may use quick formative feedback, an instructor-observed lab, an oral walkthrough or a graded exercise. It must declare **which LO IDs were actually assessed** and any passing criterion; omit claims not substantiated by evidence.

### Required misconception checks

Use short questions or demonstrations that explicitly disprove these shortcuts:

- “If it pings, the sensor must be online.”
- “Every unit of a 247-address RTU network is supported electrically.”
- “A device with a valid 4xxxx label always uses the displayed number as its zero-based offset.”
- “Exception 02 proves an RS-485 cable is broken.”
- “Any two masters can independently poll the same RTU segment.”
- “A nominal 26% bus utilization guarantees a five-second scan when multiple devices fail.”
- “A contiguous offline group proves the last good node forwards communications.”

## 7. Reusable bench labs — instructional activity catalog

**Default bench:** A non-production, isolated RS-485 network of at least **two known-working Modbus RTU sensors** and a **Moxa Modbus TCP-to-RTU gateway** of a *confirmed model/mode*, plus a Windows laptop running **Modbus Poll** and a compatible **USB-to-RS-485 adapter**. Use actual manuals and the actual supported read-only register map; the IDs 7/8 and sample IP are illustrative, not predetermined settings.

### Instructor readiness (must be complete before class)

- Identify and record **sensor make/model/firmware** and **Moxa gateway model/firmware/serial port**; confirm the gateway supports **Modbus TCP client → RTU slaves** in the chosen mode. Different Moxa product families and operating modes are not interchangeable.
- Confirm each sensor's documented **power supply rating, serial format, supported unique slave ID, function code, starting address, register quantity and display scaling**.
- Provide an **appropriately rated and protected low-voltage power supply**, safe wiring, compatible USB/RS-485 driver, serial connector/pinout, required termination/bias arrangements and Ethernet cable or isolated lab switch.
- Install and test **Modbus Poll** (including any needed license/usable evaluation), verify serial COM-port enumeration, and back up the gateway's starting configuration.
- Establish one **known-good read** before students arrive; capture a screenshot/transaction card. Reserve a way to revert any injected settings.
- Separate the bench from clinical/industrial production networks and prohibit uncontrolled writes, arbitrary polarity/ground manipulation, and shorting power or signal conductors.

**Station roles:** For a team, pair students as **operator** (makes approved read-only test) and **recorder/reviewer** (documents request and evidence), swapping roles between labs. Each group needs enough actual devices/ports to carry out its assigned station or the instructor must provide an explicitly identified simulation.

### LAB-00 — Safe setup and baseline preservation

- **Objective:** Establish that the test equipment, wiring, power, gateway configuration and device manuals are suitable for the exercise.
- **Action:** Confirm power and wiring against specifications; record adapter COM port, serial parameters, device IDs and baseline gateway config. Instructor checks that only one serial master will operate at a time.
- **Required evidence:** Bench wiring sketch, source revision list, as-found settings and first known-good read reference.
- **Success:** Student can identify what is known, what remains unknown, and the approved test boundary.

### LAB-01 — First direct RTU read (USB-to-RS-485 + Modbus Poll)

- **Objective:** See a complete Modbus RTU transaction without a TCP gateway.
- **Action:** With the gateway not acting as an independent second master, connect Modbus Poll's **serial RTU mode** through the USB adapter to one documented sensor; set compatible COM/baud/data/parity/stop bits; request a *known readable register* using FC03 or FC04 as documented.
- **Observe:** A real response, transmitted/read function, ID, starting address, quantity, update rate and raw data.
- **Evidence:** Screenshot or log plus complete transaction card and physical/serial settings.
- **Failure branch:** If no response, verify wiring/power/configuration and retry only inside the approved lab, not by guessing register writes.

### LAB-02 — Two sensors, serial topology and identity

- **Objective:** Distinguish physical cable sequence from Modbus slave addresses.
- **Action:** Add a second sensor with verified compatible settings and a **different slave ID**. Read sensor 7, then sensor 8 *if those IDs are actually supported/configured*. Draw which physical device is first and last.
- **Observe:** Identical request fields can reach a different device when the addressed slave ID changes; a shared bus is not a chain of device-to-device message repeaters.
- **Evidence:** Topology sketch, two transaction cards and any supported safe termination/bias check.
- **Caution:** Do not assign duplicate IDs on a shared live bus; do not resistance-test energized wiring or move terminations without an approved test setup.

### LAB-03 — Build a request and interpret register data

- **Objective:** Translate documentation into a valid Modbus Poll read.
- **Action:** Locate a documented input/holding register, select the correct FC03/FC04, starting offset and quantity, and decode raw register values with the documented scale and 16-/32-bit ordering.
- **Observe:** Why using the wrong 40001 notation, function or address can create valid protocol errors or misleading decoded values.
- **Evidence:** Vendor map excerpt/revision, request tuple, raw registers, decoded result and units.
- **Safe fault option:** Test a deliberately unsupported **read-only** function/range against a simulator or a known permissive lab device; record the returned exception if one occurs.

### LAB-04 — Move the same network behind the Moxa gateway

- **Objective:** Follow the transition from direct serial master to Modbus TCP client.
- **Action:** Remove/disable the USB test master as a master **before** letting the Moxa poll the RTU segment; document the gateway's operating mode, IP/TCP port, unit/serial-port mapping and serial parameters. Switch Modbus Poll to **Modbus TCP/IP**, then attempt the same known-good read through the gateway.
- **Observe:** IP connectivity vs TCP service vs actual downstream RTU reply; determine how the Unit ID selects sensor 7 versus 8.
- **Evidence:** Before/after topology, saved gateway configuration, ping/socket observations where appropriate, and at least two verified TCP-to-RTU request cards.
- **Restore:** Record any configuration changes and make the network ready for the next student.

### LAB-05 — Fault identification by layer

- **Objective:** Diagnose without “fixing” unrelated parts of the system.
- **Action:** Instructor injects one bounded fault at a time: wrong Unit ID, wrong serial format, wrong *read-only* register/function, gateway route mismatch, or a controlled isolated bench-device outage. Provide both a working baseline and symptom record.
- **Observe:** Timeout vs exception vs valid-but-wrong value; distinguish individual-device, shared-port and layered symptoms.
- **Evidence:** Initial symptom, discriminating test, likely layer, correction, successful retest and as-left state.
- **Forbidden injections:** Power shorts, intentional destructive polarity/reversal tests, unknown register writes, unplugging production equipment, changing live grounding/shielding, or producing an unapproved multi-master bus.

### LAB-06 — Estimate polling under healthy and failed-device conditions

- **Objective:** Recognize that the bench's successful two-device demonstration does not itself prove a 30-device design.
- **Action:** Use the canonical performance and timeout calculators to model the hypothetical **30-sensor** case (or measured values from the actual lab if available). Compare nominal to one/three failed devices; note assumptions and vendor/client queueing.
- **Evidence:** Inputs, estimated scan/utilization, revised degradation, interpretation and the manufacturer limits that still need verification.
- **Success:** The student can distinguish *modeled* capacity from verified installed performance.

### LAB-07 — Integrated capstone and field handoff

- **Objective:** Turn disconnected lessons into a defensible engineering/field record.
- **Scenario:** A TCP client can reach a Moxa gateway, but a subset of vibration sensors fails intermittently; a five-second update requirement is under review.
- **Action:** Classify existing evidence; select test order with the troubleshooting playbook; document which devices share serial port, power and physical cable paths; review performance; recommend tests/corrections without overstating root cause.
- **Deliverable:** One-page network sketch, configuration/transaction schedule, at least two captured tests, nominal/degraded calculation, likely causes ranked by evidence, as-left notes and unresolved questions.
- **Assessment:** Instructor checks `LO-01–LO-08` only where observed; software completion alone is not a signoff.

### Reusable bench evidence template

Every lab report should be able to record:

| Item | What to capture |
| --- | --- |
| Source | Device/gateway model, firmware, manual revision, register-map page |
| Endpoint | COM/USB serial configuration **or** IP:TCP port + gateway serial port |
| Target | Slave/Unit ID, function, start offset, quantity, decoding and scale |
| Observation | Timestamp; valid response, exception, timeout or wrong value; raw and engineering data |
| Intervention | Who approved what change/test; before/after settings, mode and wiring |
| Conclusion | Supported inference, remaining alternate hypotheses, verified restoration |

## 8. Default four-hour / half-day team workshop

**Variant ID suggestion:** `modbus-001-bench-240`. **Total elapsed:** **240 minutes**, including a 10-minute break. This is a **real lab**; provide instructor prep and equipment access before starting. Activities overlap with short concept instruction, so the separate block durations in Section 3 are not summed.

| Elapsed | Time | Instruction / activity | Outcome and evidence |
| --- | ---: | --- | --- |
| 00:00–00:10 | 10 min | Introduction, system diagram, safety, station roles (`O01–O03`; `LAB-00`) | Safe lab boundary and as-found card |
| 00:10–00:35 | 25 min | Modbus roles and first serial connection (`F01–F05`; `LAB-01`) | Direct RTU read |
| 00:35–01:00 | 25 min | RS-485 trunk, identity, termination and second sensor (`E01–E06`; `LAB-02`) | Two sensor reads + topology |
| 01:00–01:25 | 25 min | Register/function/offset/decoding (`R01–R06`; `LAB-03`) | Complete decoded request |
| 01:25–01:35 | 10 min | **Break** | — |
| 01:35–02:15 | 40 min | TCP gateway transition, routing and two Unit IDs (`G01–G06`; `LAB-04`) | TCP-through-RTU reads and saved gateway config |
| 02:15–02:45 | 30 min | Fault-injection stations and layered troubleshooting (`X01–X03`; `LAB-05`) | Classified exception/timeout and justified test |
| 02:45–03:10 | 25 min | Nominal/degraded scan, loading and caveats (`X04`; `CAL-01–03`; `LAB-06`) | Calculator evidence |
| 03:10–03:45 | 35 min | Case exercise: 30-sensor system; design/troubleshooting flow (`D01–D10`, `T00–T06` as applicable; `LAB-07`) | Diagram, hypothesis/evidence trail, recommendation |
| 03:45–04:00 | 15 min | Knowledge checks, teach-back, restore bench, collect work products (`KC-xx`) | Declared outcome coverage and as-left record |

**Timing is a teaching allocation, not a promise that 10 engineering-design playbook steps can be fully performed in 35 minutes.** The capstone rehearses selection/application of relevant steps; an expanded design-review workshop would cover all steps individually. If students are new to serial electrical work or equipment is unverified, increase time, reduce lab scope explicitly, or use additional instructor stations rather than skipping safety and evidence requirements.

**Materials produced by this variant:** Student HTML course, instructor run sheet, lab station wiring/connection diagram, verified register examples, fault cards, lab worksheets, response capture files, calculator records and final knowledge check. Project-specific information remains in approved project storage.

## 9. Other canonical example variants

### 09.A — One-hour Modbus TCP Gateway lunch-and-learn

**Suggested variant ID:** `modbus-001-gateway-60`. **Audience:** BAS engineers and technicians, including a healthcare-facility BAS team. No assumption about their specific owner network, installed Moxa model, or production permissions.

| Elapsed | Minutes | Content |
| --- | ---: | --- |
| 00:00–00:07 | 7 | Why gateways exist; “one IP, many RTU devices”; safety and core floor |
| 00:07–00:18 | 11 | RTU versus TCP roles, MBAP Unit ID, address domain, register/map minimum |
| 00:18–00:30 | 12 | Moxa gateway diagram, mode and serial-port routing; illustrative two-sensor case |
| 00:30–00:42 | 12 | Modbus Poll live/simulated TCP read and layered connectivity tests |
| 00:42–00:50 | 8 | Queueing, offline retries, why client limits and RTU throughput differ |
| 00:50–00:58 | 8 | “Ping works but slave is offline”: guided diagnosis and exception/timeout exercise |
| 00:58–01:00 | 2 | Two-question knowledge check and takeaway |

**Declared scope:** Gateway integration/diagnostic orientation, not full RS-485 design competence, field authorization or 30-node capacity certification. Provide a separate engineer/field appendix link for deeper detail.

### 09.B — Field departure brief for a specific job

**Suggested variant ID:** `modbus-001-field-preflight-[project-alias]`. **Default length:** 20–45 minutes, adjusted to uncertainty and task criticality.

1. **Situation briefing:** What system is involved, why the engineer is going, affected devices, known past symptoms, current impact, access constraints and owner approvals. Separate **reported**, **observed**, and **unverified**.
2. **Targeted refresh:** The essential CF floor plus the highest-risk 2–5 learning blocks, selected according to Ethernet/TCP/gateway/RS-485/data/performance failure patterns.
3. **Scenario diagram:** Draw only documented endpoints and suspected boundaries. Unknown gateway port mapping, slave settings or cable order remain visibly **unknown**.
4. **Tools and safe actions:** Which tester/adapter/laptop/manual is needed; the approved sequence for read-only diagnostics; whether direct serial tests would require controlled isolation.
5. **Discriminating test plan:** First known-good request, comparison against adjacent slave where meaningful, expected result, what each outcome establishes and which action follows.
6. **Exit and deliverable:** As-found snapshot, evidence record, changes/backup, as-left validation, unresolved RFIs/issues and technical contacts.

**Example prompt to an AI agent:**

> Generate a 30-minute MODBUS-001 field brief for a technician visiting a site with a Moxa TCP/RTU gateway and intermittent loss of downstream vibration sensors. We know the gateway IP responds, but do not yet know the specific Moxa model, serial-port mapping, or physical order. Prioritize the first safe checks and provide a pocket-sized transaction/evidence card. Do not assume a cable break or propose unapproved plant changes.

### 09.C — Engineering-design/PE review track

Expand `E01–E06`, `G02–G05`, `X04`, `D01–D10`, and `CAL-01–03`. Require actual manufacturer capacities, cable details, the source-backed poll schedule, a nominal/degraded timing analysis, and a design/commissioning acceptance record. Do not infer device-specific limits from an illustrative lab.

## 10. Course variant generation — AI or instructor workflow

The course generator consumes **this versioned syllabus** and a **short conversational scenario description**. Users should not need to complete a long form. Missing critical facts may be requested once or represented as unknown/conditional steps; do not fill gaps with invented device models, register values or topology.

### Profile dimensions

| Field | Example / handling |
| --- | --- |
| **Audience and prior knowledge** | Field technician familiar with BACnet, PLC programmer, BAS engineer, PE reviewer; assume only stated experience |
| **Purpose** | Orientation, preflight, troubleshooting, new network design, commissioning, mentoring, competency evaluation |
| **Duration and delivery** | 30-minute field brief on phone; one-hour lunch-and-learn; four-hour bench workshop; extended design review |
| **System / hardware** | Exact Moxa model/firmware if known; actual sensors, serial adapter, software, port topology, network constraints |
| **Known facts and current problems** | As-found reports, dates, symptoms, what is confirmed/uncertain, lessons from previous site work |
| **Work permissions and safety** | Production versus isolated lab, authorized read-only requests, shutdown approvals, safety-critical interfaces |
| **Depth and assessment** | Core awareness, practitioner diagnosis, engineering substantiation; oral, quiz, lab or design review |
| **Source snapshot and output location** | Canonical document revisions and allowed project source documents; keep client data out of public GitHub |

### Selection and generation sequence

1. **Resolve the scenario.** Extract intent, duration, audience, equipment and known unknowns from the conversation/project evidence. No new user form is required by default.
2. **Declare the course variant.** Set `course_id`, `syllabus_version`, `variant_id` and version, scenario alias, output privacy/location, sources and assessment scope.
3. **Apply the mandatory floor.** Cover CF-01–CF-08 proportionately, and preserve the nuanced caveats for all selected topics.
4. **Select teaching blocks.** Choose by purpose, prerequisite edges, known symptoms and desired proficiency; retain stable block IDs and record omitted/unassessed outcomes. Reorder as necessary.
5. **Attach exercises and sources.** Pick playbook steps, calculators, bench labs or simulated field cases. Validate actual manufacturer specs and register maps; use unknown placeholders when unavailable.
6. **Generate a course package.** Produce a coverage matrix, expanded outline, lesson content, diagrams/scenarios, question bank/answer rationale, lab/instructor materials if needed, and a mobile-capable HTML build using the shared engine.
7. **Run checks and review.** Technical/source consistency, equations, correct IDs, safety, links, responsiveness, offline behavior, quiz keys, real bench readiness, and human review when claims warrant it.
8. **Release a variant, not a new syllabus.** Record inputs, source snapshot, test results, limitations and the actual competencies assessed. A changed source, scenario or emphasis results in a new variant version.

### Minimum output artifacts

| Output | Purpose |
| --- | --- |
| `variant-profile` | Reproducible audience, system, goal, time, risk, source and assessment inputs |
| `coverage-matrix` | Selected CF/learning block IDs, LO IDs, where taught, how checked; explicitly not-covered items |
| `course-manifest` | Engine navigation, presentation order, stable IDs and source pointers |
| `lesson-content` | Chosen lessons, exercises, diagrams and scenario-specific diagnostic branches |
| `knowledge-check` | Tagged questions, answer rationale and appropriate proficiency criteria |
| `training-html` | Standalone/mobile-capable presentation or another approved delivery format |
| `instructor/lab-pack` | Required when physical labs are selected: prep, verified hardware settings, fault cards, safety and evidence sheets |
| `generation-record` | Syllabus and source revisions, generated version, checks, responsible reviewer, known limits |

**Confidentiality:** Project-specific facts, client identity details, IP assignments, network inventories, credentials and field photographs belong in authorized project storage, **not** the public generic training repository. A public course may contain anonymous/synthetic fixtures only.

## 11. Acceptance criteria for course variants

A generated course is **ready for use**, not automatically an approved engineering standard, only when it has:

- A declared syllabus revision, audience, objective, duration, learning-outcome scope and source revisions.
- A traceable learning block → objective → assessment/evidence mapping, with CF floor covered.
- Correctly linked canonical engineering references; no new unsupported manufacturer or site facts.
- Distinct, anchor-addressable playbook steps when those are in scope, with the clickable horizontal navigation retained.
- Correct calculator assumptions/units and test cases when calculators are included.
- Working diagrams, quizzes and navigation on targeted desktop/mobile browsers, including offline mode when required.
- Physical lab readiness and safe fault-injection controls for any real-hardware course.
- Explicit uncertainty and unresolved issues; recorded review and acceptance as applicable.

**A passed HTML build is not proof of learning, field performance, engineering acceptance or instructor readiness.**

## 12. Model answers and evidence anchors

The following mini-examples are suitable for reuse, provided they are clearly marked as **illustrative**:

- **Two sensors:** Sensor IDs 7/8 may share a map, but a request to one address tells you nothing about whether the other responds; the actual register offset and scaling come from the vendor map.
- **TCP gateway:** Client targets `192.168.1.50:502`, uses a Unit ID, and depends on the gateway's route table/serial port; do not treat IP connectivity as a valid serial read.
- **Register labels:** Under the conventional holding-register reference scheme, `40001` corresponds to transmitted offset `0` and `40101` to `100`; device and client notation must be verified.
- **Exceptions:** 01/02/03 establish a protocol-level rejection, subject to identifying the responding endpoint; 0A/0B may be gateway-reported path/target faults; a timeout is the absence of a timely valid response.
- **Sequential failures:** Map physical order and power/port commonality; “last working/first failed” is a clue, not proof that serial messages are forwarded node to node.
- **Polling:** A calculated ~26.3% normal loading does not guarantee acceptable updates when multiple devices fail and retry.

Use these anchors to generate short explainers, questions, diagrams and comparative examples without recreating an entire course.

## 13. Technical source ownership and course governance

### Canonical KIS references

- [Modbus RTU — field integration reference](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-rtu.md)
- [Modbus TCP — field integration reference](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-tcp.md)
- [Modbus RTU Network Design — engineering playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-rtu-network-design.md)
- [Modbus Communications Troubleshooting — field playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-communications-troubleshooting.md)
- [RTU Network Performance calculator method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-network-performance.md)
- [RTU Timeout/Retry Impact method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-timeout-retry-impact.md)
- [RS-485 Electrical Loading method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/rs485-electrical-loading.md)

### Training-tool / hardware reference material

- [Witte Software — Modbus Poll User Manual](https://www.modbustools.com/mbpoll-user-manual.html): serial/USB and Modbus TCP/IP connection definitions, functions, traffic and data display.
- [Moxa MGate MB3170/MB3270 product reference](https://www.moxa.com/en/products/industrial-edge-connectivity/protocol-gateways/modbus-tcp-gateways/mgate-mb3170-mb3270-series): **example series only**; replace with the *actual* gateway model's user manual before bench or field instruction.

The KIS sources above remain **draft technical references** until separately approved. Any derived course variant must record the consulted Git commit/blob IDs and vendor model/firmware/manual revisions. Do not assume that the listed gateway represents the team's actual device.

### Change control and scope boundaries

- This syllabus owns **instructional intent and competency**, not protocol truth or engineering acceptance.
- Change a canonical calculation or engineering procedure **in its owning repository**, then reconcile derived lessons after review.
- Changing a venue, class length, equipment model, case, or visual treatment **does not modify** this syllabus; it produces a new profile/variant revision.
- Change this syllabus only for genuine changes to intended competencies, minimum floor, lab contract or curriculum coverage. Preserve stable IDs or explicitly migrate them.
- The existing frozen training engine v0.2 remains unchanged. The newer modular implementation is evaluated independently.
- No working client project data or sensitive files are committed to the generic public training framework.

**Next work:** Reconcile the v0.3 Modbus course manifest/HTML lessons against `syllabus_version: 0.2.0`, generate the `modbus-001-bench-240` lab variant, and verify its actual exercises and questions on the chosen hardware.

## Related documents

- [KIS Course Assembly Contract](../../COURSE-ASSEMBLY-CONTRACT.md)
- [Training architecture](../../ARCHITECTURE.md)
- [MODBUS-001 course implementation notes](README.md)
- [Frozen v0.2 HTML interaction baseline](../../engine/baselines/v0.2/BASELINE.md)
- [v0.3 course manifest (still under development)](https://github.com/kissolutions/controls-engineering/blob/work/modbus-001-vertical-slice/training/courses/modbus-001/course.json)
