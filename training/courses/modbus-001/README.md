# Modbus 001 — Communications Fundamentals & Network Engineering

**Status:** First academic vertical slice built (v0.3), complete course not yet accepted.

## Try the course

[Standalone v0.3 HTML demo](../../engine/prototypes/v0.3/modbus-001.html) — save/open locally in a browser. No server or external JS dependencies required.

[Course manifest](course.json) — stable IDs, learning order, domains, authoring status and canonical-source references.

## Course authoring files

```text
course.json                   # chapter map, status and source references
lessons/
  01-00-overview.html         # start / learning objectives
  01-01-modbus-fundamentals.html
  01-02-rs485-physical.html
  01-03-registers-addressing.html
  01-04-tcp-rtu-gateways.html
  01-05-polling-budget.html
scenarios/
  modbus-paths.json            # progressive RTU-to-TCP architectures
  rs485-termination.json       # correct / missing / extra termination
```

The HTML lesson stubs contain *only* markup; reusable interactions live in `training/engine/src/`. Each independent lesson uses `id="learn-<course.json id>"` and can be selected from the course sidebar.

To rebuild: `python training/tools/build_modbus_001.py`.

## Status by section

| Course section | v0.3 result | Remaining work |
|---|---|---|
| 01 Academic | Six dedicated lessons; interactive communication-path and termination stages; register address translator | Engineer review; deeper exercises and chapter quiz integration |
| 02 Playbooks | Original 8-step troubleshooting simulator retained from v0.2 | Convert to independent step stubs; implement complete 10-step network design |
| 03 Calculators | Existing inline performance, retry and RS-485 unit-load tools | Extract common calculator component and validate all method variants |
| 04 Knowledge checks | Original four domain checks | Tagged reusable question bank, chapter and domain filters, completion criteria |

## Technical authority

Canonical sources:
- [Modbus RTU](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-rtu.md)
- [Modbus TCP](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/communications/modbus-tcp.md)
- [Network Design Playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-rtu-network-design.md)
- [Troubleshooting Playbook](https://github.com/kissolutions/controls-engineering/blob/main/docs/design-playbooks/patterns/modbus-communications-troubleshooting.md)
- [Network Performance Method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-network-performance.md)
- [Timeout/Retry Method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/modbus-rtu-timeout-retry-impact.md)
- [RS-485 Electrical Loading Method](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/engineering/calculators/communications/rs485-electrical-loading.md)

**Do not** duplicate manufacturer node limits, create new acceptance standards, or treat simulated conditions as commissioning evidence. The full course will require a domain SME review.
