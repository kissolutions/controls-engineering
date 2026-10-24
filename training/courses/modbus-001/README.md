# Modbus 001 — Communications Fundamentals & Network Engineering

**Status:** Course development seed; not a completed course or released competency standard.

**Curriculum authority:** [MODBUS-001 Canonical Syllabus v0.2.0 (draft)](SYLLABUS.md). This README is a condensed course-package overview, not a competing curriculum. The syllabus defines atomic blocks, labs, critical conceptual floor, assessment expectations, and generation profiles for a half-day lab, one-hour gateway session, or project-specific field brief. See the [Course Assembly Contract](../../COURSE-ASSEMBLY-CONTRACT.md) for reuse across KIS domains.

**Engine reference:** [frozen v0.2](../../engine/baselines/v0.2/index.html).  
**Technical sources:**
- [Modbus RTU reference](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-rtu.md)
- [Modbus TCP reference](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-tcp.md)
- [Network design playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-rtu-network-design.md)
- [Troubleshooting playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-communications-troubleshooting.md)
- [Modbus performance calculator method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-network-performance.md)
- [Timeout/retry method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-timeout-retry-impact.md)
- [RS-485 loading method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/rs485-electrical-loading.md)

## Target course structure

### 01 — Academic learning

- Overview, learning objectives, skill prerequisites.
- Modbus RTU architecture and serial-master behavior.
- RS-485 bus physics, termination, bias, grounding, topology, unit loads.
- Addressing, register types, FC03/FC04, offsets, data types and endian issues.
- Modbus TCP architecture, Unit IDs, gateways and routing.
- Poll scheduling, timeouts, retries and diagnostic failure domains.

### 02 — Playbooks

- **Modbus RTU Network Design:** all ten engineering steps from the canonical playbook.
- **Modbus Communications Troubleshooting:** complete guided diagnostic steps, measurement interpretation and safe isolate/reconnect methods.
- Every step has a unique lesson stub and stable anchor, selected from the horizontal navigator.

### 03 — Engineering calculators

- RTU network performance and minimum baud rate.
- Timeout and retry impact under degraded network conditions.
- RS-485 electrical unit loading.
- Explain input sources, assumptions, acceptable screening uses and limits.

### 04 — Knowledge checks

- Chapter-based checks for academic understanding.
- Domain-based checks for wiring, gateway routing, registers, communications performance and troubleshooting.
- A final applied exercise: 30-sensor vibration monitoring network through a TCP-to-RTU gateway, including intentional faults.
- Questions should have stable IDs and both chapter and domain tags; avoid duplicate copies of the same question.

## Definition of done

All course lessons are substantive, linked to authoritative source revisions, interactive exercises work, calculators are independently checked against source equations, navigation and question feedback are tested, and engineering content is reviewed by a knowledgeable engineer. The frozen v0.2 file is **not** the finished Modbus 001 course.
