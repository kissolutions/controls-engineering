# KIS Training — engine incubation and course demonstrations

**Status:** v0.2 frozen; v0.3 Modbus 001 academic vertical slice under development.

The training engine is a derived instructional layer. This `training/` directory is an incubation home in `kissolutions/controls-engineering`, **not** a permanent assertion that training for every KIS domain belongs to controls engineering.

## Versions and entry points

- **[v0.2 frozen reference](engine/baselines/v0.2/index.html)** — do not modify this accepted standalone prototype.
- **[v0.2 baseline contract](engine/baselines/v0.2/BASELINE.md)** — accepted interactions and known gaps.
- **[v0.3 Modbus 001 standalone course demo](engine/prototypes/v0.3/modbus-001.html)** — built from independent lesson stubs, scenario JSON and reusable widget code; opens in a browser without a server.
- **[Engine/course architecture](ARCHITECTURE.md)** — authority and package boundaries.
- **[Modbus 001 course map](courses/modbus-001/course.json)** — stable IDs and documented source revisions.
- **[Course authoring guide](courses/modbus-001/README.md)**.

## Course user experience

1. **01 Academic Learning** — six selectable lessons from separate HTML stubs.
2. **02 Engineering Playbooks** — legacy prototype's clickable, left-to-right troubleshooting steps. Network design is still an overview.
3. **03 Engineering Calculators** — existing demonstration calculators, sourced from canonical calculation methods.
4. **04 Knowledge Checks** — existing domain-question demonstration; full tagged bank planned.

## Build and test

From repository root, with standard Python 3:

```bash
python training/tools/build_modbus_001.py
python -m unittest discover -s training/tests -p 'test_*.py' -v
```

Node.js is used only for optional inline-JavaScript syntax checks. The browser demo has no runtime dependencies. CI verifies that the generated standalone HTML matches the committed version.

## Governance

- Never modify v0.2 to implement a new course.
- All technical facts and methods remain owned by KIS Knowledgebase and domain playbooks.
- Lesson stubs and diagrams are derived teaching content; their examples must not be presented as manufacturer specifications or engineering acceptance.
- Version source references in `course.json` and reconcile technical changes before accepting instruction.
