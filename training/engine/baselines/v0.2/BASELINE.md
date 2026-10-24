# KIS Training Engine — Frozen v0.2 Baseline

**Status:** Frozen UI/interaction reference (not production release).  
**Artifact:** [index.html](index.html)  
**Version:** `0.2`  
**Freeze date:** 2026-10-23 (America/Chicago)  
**Freeze policy:** Do not change the contents of `index.html` in this directory. Future modifications belong in a new versioned directory or the separately developed engine.

## What is accepted

- Four top-level training sections: **01 Academic Learning**, **02 Engineering Playbooks**, **03 Engineering Calculators**, **04 Knowledge Checks**.
- Nested sidebar navigation with chapter/domain selections.
- Clickable left-to-right playbook flow, with focused/continuous lesson presentation.
- Interactive RS-485 network states and field troubleshooting examples.
- Modbus network performance and RS-485 loading calculators.
- Domain-targeted knowledge checks and local progress display.

## Baseline constraints / known gaps

- This artifact is a **single self-contained HTML prototype**. It intentionally mixes layout, course content and JavaScript as a demonstration. It is **not** the permanent reusable engine architecture.
- The Modbus Network Design flow remains a placeholder; it is not a fully interactive ten-step lesson.
- Academic chapters are concise prototypes rather than complete validated instruction.
- Calculator results are screening estimates with assumptions, not certified network measurements.
- No backend LMS, user accounts, durable course records, or automated canonical-document import.
- Browser-saved progress is local to this prototype and is not an accepted competency record.

## Integrity and reproducibility

The locally archived source artifact `kis_training_engine_v0_2.html` had SHA-256:

```text
a590c7c2348e2e96f3093e1826aab13b00f2a7778004767cb18a991c45f916b8
```

The connector may normalize line endings during file retrieval. Treat the committed Git blob as the durable frozen baseline; do not silently overwrite it to match a local export.

## Next iteration contract

- Keep **engine**, **course definitions**, **individual lesson stubs**, **calculator adapters**, and **question banks** separate.
- Technical source-of-truth remains in `kissolutions/knowledgebase_wikijs` (reference facts and calculation methods) and `kissolutions/controls-engineering` (design/troubleshooting playbooks).
- A course may add instructional framing, exercises, tests and diagrams; it must not create new unsupported technical facts.
- Maintain explicit source links and document revision information.
- New engine versions must preserve v0.2's demonstrated interactions or document deliberate changes.
