---
title: Rule catalog — structure and use
page_type: engineering-data-contract
page_status: draft
---

# Rule catalog — candidate v0.1

One catalog of executable checks. Each rule has **one authoritative home** here; explanatory pages reference rules by ID instead of restating them. The catalog is written for a fast model or a script to execute without interpretation (see the [agent execution profile](../../governance-and-doctrine/agent-execution-profile-proposal.md)).

## Files

| File | Layer | Content |
|---|---|---|
| [`framework-rules.yaml`](framework-rules.yaml) | Framework | Organization-neutral rules (identifiers, scope, release) and decision tables DT-SCOPE and DT-NAME |
| [`../../org-standards/klutch/rules.yaml`](../../org-standards/klutch/rules.yaml) | Klutch profile | Klutch rules and decision tables DT-DEVICE, DT-ACTUATOR, DT-ALLOC, DT-STAGE |

## Rule schema

| Field | Meaning |
|---|---|
| `id` | Stable rule ID, never reused. Prefix = layer and area (`FW-ID-01`, `KL-ACT-03`). |
| `title` | Short name. |
| `applies_to` | Which rows, objects or artifacts the rule evaluates, and any condition that makes it applicable. |
| `inputs` | Exact registers, tabs, columns, sheets or files read. |
| `evaluate` | The test, stated as a single condition. A rule that needs two conditions is two rules. |
| `finding` | What to report when the test fails, including which IDs to list. |
| `severity` | `blocker` (blocks the release gate), `major` (must be resolved or accepted before issue), `minor` (fix when convenient), `info`. |
| `evidence` | What a pass or an accepted exception must cite. |
| `closure` | The condition that closes the finding. |
| `stages` | Issue stages where the rule must run (see DT-STAGE). |
| `tier` | Lowest speed tier that runs it during working reviews: `quick`, `standard`, `deep`. The release gate runs every rule listed for that stage, regardless of tier. |
| `source` | Page that explains the rule. |

## Use

1. Determine the issue stage (DT-STAGE) and the speed tier for a working review.
2. Run every rule whose `stages` includes the stage (release gate) or whose `tier` is at or below the chosen tier (working review).
3. Report each finding with rule ID, severity, the IDs listed in `finding`, and the inputs read (with revisions).
4. Record rules not run and why.

## Status

Initial rules converted from the validation pages on 2026-11-26. Explanatory pages still restate some rules; they will be cut back to references once the catalog is accepted.
