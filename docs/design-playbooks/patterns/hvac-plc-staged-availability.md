---
title: HVAC PLC staged availability and failure containment — draft playbook
page_type: playbook
page_status: draft
---

# HVAC plant PLC availability architecture (P12)

**First determine requirement**, not a controller model: allowed outage and restoration time, whether transition must be bumpless, acceptable lost sequencing state, status preservation, maintainability, common-mode failure and capital phasing. HVAC plants may tolerate a restoration interval, but **do not assume minutes are universally acceptable**.

| Candidate stage | What it provides | What it does not guarantee |
|---|---|---|
| 1. Single CPU with distributed I/O | Centralized controls; replaceable CPU and modular Ethernet I/O | Controller availability, communications resilience |
| 2. Offline/cold spare plus verified backup image | Spare hardware and documented restoration | Automatic failover, fresh retained data, bumpless transfer |
| 3. Application-managed Logix Hot Backup | Two controllers with logic-managed failover where supported and engineered | Hardware-redundancy-module timing or completely transparent process transfer |
| 4. Manufacturer-supported ControlLogix redundancy | Dedicated redundancy architecture subject to catalog/firmware/I/O compatibility | Universal reuse of stage-1 hardware; immunity to common power/net failures |

**Manufacturer source:** Rockwell *High Availability Systems*, HIGHAV-RM002G-EN-P (Sept 2025), §Hot Backup, says Logix Hot Backup uses application code without redundancy module; supports CompactLogix 5370/5380 and ControlLogix 5570/5580, with supported I/O bulletins 1756/1794/5069/5094/5032. Its switchover is slower than controller redundancy and needs engineered data management. [Rockwell manual](https://literature.rockwellautomation.com/idc/groups/literature/documents/rm/highav-rm002_-en-p.pdf). **Specific firmware revisions, switchover guarantees, licenses, 5069 remote-I/O configuration and code-generator availability must be checked against current Rockwell selection documentation before procurement.**

## Architecture-independent design requirements

- Distinguish **PLC failure**, **remote-I/O adapter failure**, **ring/path loss**, **switch failure**, **power-supply failure** and **gateway/BAS-head-end loss**; each needs its own detection, state response and recovery test.
- A DLR ring, managed/supervised switch and redundant Ethernet links are network availability measures **not** controller redundancy. Confirm every proposed adapter, switch/bridge, firmware and topology is DLR-capable.
- Define critical outputs' behavior on controller fault, communications loss and loss of power; design appropriate independently operable fallback for chiller minimum flow, pumps, VFD enable and local protective interlocks. A watchdog or request relay must not bypass equipment safety.
- Plan procedure for software image, retain-state consistency, start order, manual/auto handback and alarms after recovery. Test actual interruption behavior before stating transfer characteristics.
- Any proposed staged hardware reuse is a **procurement hypothesis** until catalog-specific compatibility is documented. Preserve future-stage feasibility requirements in the PER and procurement basis.

**Acceptance evidence:** fault scenarios, failure-mode matrix, measured recovery behavior, supported hardware/firmware matrix, network topology, gateway recovery, operator notification and approved plant-outage criteria.
