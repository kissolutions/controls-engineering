---
title: Agent execution profile — proposed
page_type: governance
page_status: draft
---

# Agent execution profile — candidate v0.1

**Status:** Proposal for owner review (2026-11-26). Not yet applied to existing pages.

## Principle: build for RISC

The package is written so that a fast, general model can run it accurately. Depth comes from running more checks or more passes (a speed setting), not from needing a more capable model or more reasoning effort.

Writing rules that follow from this:

- One rule per line, numbered, with a single condition and a single result.
- Decision tables instead of prose where a choice depends on several inputs.
- Checklists with pass / fail outcomes. Each check names its inputs (which register, tab, sheet) and the form of its finding.
- Explanations and background are kept apart from the rules, so the rules can be read on their own.
- Speed tiers say which checks run at each depth during working reviews (for example: quick = presence and exact-match checks; standard = plus cross-document sync; deep = plus independent completeness pass and failure-mode review).
- **The release gate is fixed.** Speed tiers never change the acceptance criteria for an issued deliverable. Any check not performed is recorded as not performed.
- Every rule in the rule catalog declares: rule ID, applicability, required inputs, evaluation, finding (what to report), severity, evidence, and closure condition.

## Tasks that benefit from a deeper model

Some tasks are open-ended, spatial or judgement-heavy, and run better on a more capable model or a higher reasoning setting. Each such task is marked in its process or playbook page, and the agent tells the PE at the start of the task which model or setting is preferable, so the PE can choose.

| Task | Domain | Why it benefits |
|---|---|---|
| Auto-placement of control devices and wire bundle routing | LV lighting | Spatial optimization across many interacting constraints |
| Failure-mode analysis (for example a controlling 4–20 mA input on a CAN module, damper fail directions) | Controls | Open-ended consequence reasoning |
| Controls narrative and state machine design for a new system type | Controls / logic | Abstract design with many interacting modes |
| Independent completeness pass (M2) | Controls | Needs to find what is missing, not check what is present |
| Bird's-eye review and streamlining of the package itself | Framework | Whole-package synthesis |

Routine work stays on the RISC default: register edits, drawing-to-EDP sync, identifier validation, BOM checks, terminal tables from accepted rules, change log entries.

## Marking a page

A process or playbook step that benefits from a deeper model carries a line such as:

> **Model note:** deeper model or higher reasoning setting recommended for this step (spatial optimization). The agent tells the PE before starting.

The note recommends; the PE decides.
