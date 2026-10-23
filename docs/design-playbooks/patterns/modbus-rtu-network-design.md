---
title: Modbus RTU Network Design
page_type: playbook
page_status: draft
---

# Modbus RTU Network Design — engineering playbook

**Purpose:** design and document a reliable Modbus RTU network, including RTU segments accessed through TCP gateways. Use the Modbus RTU and Modbus TCP technical references in the KIS Knowledgebase for underlying constraints.

## Design and acceptance checklist

| Step | Verify / establish | Evidence of completion |
|---|---|---|
| 1. Inventory | Device make/model/revision, quantity, supported serial modes and registers | Device schedule and manufacturer references |
| 2. Topology | Gateway, serial ports, physical bus order, cable lengths/stubs, power distribution | As-designed network drawing |
| 3. Capacity | Slave address space, transceiver loading, cable limits, manufacturer node/route limits, gateway TCP client limit | Capacity check by constraint, not one blanket device count |
| 4. Serial parameters | Baud, data bits, parity, stop bits, supported common setting | Configuration schedule |
| 5. Addresses | Unique RTU slave ID on each address domain; broadcasts not used for reads | Address schedule |
| 6. Electrical | A/B mapping, termination at two ends, bias, reference, isolation, shielding, surge/grounding | Wiring/termination detail |
| 7. Gateway routing | Unit ID-to-serial-port mapping, overlapping ID policy, forwarding mode, TCP port | Saved configuration and routing table |
| 8. Polling | Function code, offset convention, quantity, grouped reads, scan interval, timeouts/retries | Poll schedule and timing estimate |
| 9. Performance | Worst-case poll cycle including offline-node retries, multiple TCP clients and gateway queueing | Performance basis and accepted update interval |
| 10. Validation | Representative first/middle/last node reads, gateway restart, one offline node, restored communications | Commissioning test plan/results |

**Design gates:** Do not equate 247 protocol addresses with 247 electrically or operationally supported nodes. Traditional RS-485 unit-load limits do not establish universal gateway node counts. Verify exact product and firmware. Do not assume two gateway serial ports permit duplicate Unit IDs through one IP without explicit routing support.

## Required outputs
1. **Topology view:** gateway/ports, physical cable order, termination, power and isolation boundaries.
2. **Configuration schedule:** device/slave ID, serial format, gateway IP/port, routing, firmware and source references.
3. **Communications performance basis:** requested points/blocks, scan rates, baud rate, estimated response/timeout/retry budget, concurrency and failure behavior.

Use project engineering registers as the authoritative data source where available; avoid duplicate independent schedules. Record unresolved manufacturer limits or undocumented installation assumptions as issues/RFIs.

## Handoff to commissioning
Preserve gateway configuration backup, device map revisions, tested request examples, expected response values, and as-built physical order. Link the Modbus Communications Troubleshooting playbook.

**Status:** Draft; requires field pilot and engineering acceptance.
