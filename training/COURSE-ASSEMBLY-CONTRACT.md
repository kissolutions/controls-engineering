---
title: "KIS Course Assembly Contract"
document_type: training-framework-contract
status: draft
version: "0.1.0"
date: 2026-10-24
---

# KIS Course Assembly Contract

**Purpose:** Convert a versioned canonical course syllabus into a scenario-specific training experience without making the HTML engine, an AI agent, or a one-off workshop an alternate source of engineering truth.

This contract is **cross-domain**. The first working application is [MODBUS-001](courses/modbus-001/SYLLABUS.md), but the same method should be usable for BAS control narratives, PLC networks, LV lighting, commissioning and other KIS engineering topics.

## 1. Framework ownership

| Artifact | Owns | Must not silently change |
| --- | --- | --- |
| **Canonical KIS technical references** | Engineering vocabulary, equations, hardware facts and product/vendor constraints | To satisfy a convenient lesson example |
| **Domain design/field playbooks** | Human steps, order constraints, required evidence and safe test/verification procedure | To simplify a training animation |
| **Canonical course syllabus (`SYLLABUS.md`)** | Learning outcomes, essential conceptual floor, module/block IDs, labs and assessment expectations | To accommodate one audience, duration or job |
| **Variant profile** | Audience, scenario, duration, chosen competencies, safe equipment/permissions and private/source context | The canonical syllabus |
| **Generated course package** | Selected lessons, explanations, diagrams, questions, practice, references and navigation | Source of truth or primary register |
| **Training engine** | UI, navigation, diagrams, calculators, progress display, offline/mobile packaging | Course-specific facts or technical acceptance |

**Authority flow:** Source knowledge → syllabus → profile & verified project/hardware context → coverage plan → generated presentation → technical/delivery review.

## 2. Input contract — normal conversation is enough

An engineer may request, for example:

> “I'm heading to a site to troubleshoot intermittent Modbus TCP-to-RTU communications. There's a Moxa gateway and some vibration sensors. I know ping works, but a group of sensors has been dropping out. Make me a 25-minute phone-friendly field brief and test checklist.”

Or:

> “Build a half-day Modbus bench course with two RS-485 sensors, a USB-RS485 dongle, Modbus Poll and a Moxa gateway.”

Or:

> “Create a one-hour gateway lunch-and-learn for a BAS team. Emphasize architecture, Unit IDs, live reads, and what ping does not prove.”

A human/AI agent should **extract the profile from those sentences**, any supplied source documents and the available project record. Do not demand completion of a multi-question form before starting. Unavailable critical inputs are explicitly labeled **unknown**, replaced with a clearly marked synthetic lab example where safe, or asked about only when essential to safe execution.

### Suggested profile fields

| Field | Minimum expectation |
| --- | --- |
| `course_id` / `syllabus_version` | Explicit immutable syllabus baseline |
| `variant_id` / `variant_version` | Stable identity for reproducible delivery |
| `audience` / `prior_knowledge` | Learner roles and actual prerequisites |
| `purpose` / `target_outcomes` | What the learner should be able to do afterward |
| `duration_minutes` / `delivery` | Available time, desktop/mobile/offline/instructor-led format |
| `scenario` / `known_issues` | System facts, historical observations, active symptoms, unknowns; each with provenance |
| `equipment` | Exact known models, firmware, manuals, software and tooling; unresolved items stay unresolved |
| `operational_permissions` | Bench or production, live-system restrictions, safe test authority and restoration needs |
| `assessment` | What competencies will be checked, by what method and to what criterion |
| `source_snapshot` / `privacy_class` | Reference revisions and approved location for private project-specific output |

**Privacy:** Real client identifiers, networks, drawings, credentials, recordings and project-specific source files remain within authorized project storage, not the public generic training repository.

## 3. Course assembly procedure

### Stage A — Resolve intent and sources

1. Read the approved/relevant canonical syllabus (`course_id` plus exact syllabus version).
2. Resolve the user request into a profile, marking facts `confirmed` / `reported` / `hypothesis` / `unknown`.
3. Locate applicable canonical engineering knowledge, design/field playbooks, calculator methods and manufacturer manuals; record source revision and status.
4. Identify any safety-critical system, operating restriction or unknown hardware compatibility that requires human review before live practice.

### Stage B — Build the coverage matrix

1. Include the syllabus's **mandatory conceptual floor** with appropriate depth for the allotted time.
2. Select atomic learning blocks according to prerequisites, audience, problem layer, proficiency, and time.
3. Add related playbook steps, calculators, scenarios, physical labs and knowledge checks.
4. Produce `learning outcome → blocks → activity → evidence → assessment` mappings.
5. Explicitly mark omitted/unassessed outcomes. Never mark them complete because the presentation exists.
6. Reorder lessons or abbreviate presentations without changing canonical block IDs.

**Time conflict policy:** If requested time cannot reasonably cover mandatory content plus the chosen labs, create a feasible scope, flag the omissions, and distinguish a shorter **orientation** from a hands-on **competency assessment**. Do not imply a full workshop was compressed without loss.

### Stage C — Generate delivery materials

For every selected module generate, as appropriate:

- **Teach:** Concepts, vocabulary and the necessary nuance from canonical sources.
- **Show:** A system diagram, comparative view, progressive architecture or worked example.
- **Do:** Live/simulated action, calculation, diagnostic choice, supported configuration step or lab.
- **Check:** Immediate answer feedback, observed evidence or reviewed work product.
- **Source:** Source URL/revision, model-specific assumptions, known limits and confidence.

Every physical lab must declare hardware readiness, safe operating boundary, starting/restore condition, expected observations and acceptable instructor interventions. Any simulated result must be clearly identified as simulated, **never** presented as a measured field or manufacturer value.

Deliver an appropriate subset of:
`variant-profile`, `coverage-matrix`, `course-manifest`, `lessons`, `scenario-config`, `question-bank`, `lab-pack`, `training-html` and `generation-record`.

### Stage D — Validate and release

- **Technical:** Canonical-source fidelity, exact manufacturer model capabilities, protocol modes, transaction formats, equations, units, and non-universal limitations.
- **Structural:** Every displayed topic references a stable syllabus ID; each claimed outcome maps to teaching and assessment; no duplicate question authority.
- **Presentation:** Navigation, clickable playbook anchors, diagrams, calculator controls and question feedback work in the selected format; check mobile and offline operation when requested.
- **Safety:** No unauthorized connection/write/setpoint change, unsafe fault injection, inferred approval or instructions that disturb operational controls.
- **Evidence:** The generated materials distinguish confirmed/observed/unknown content; field recommendations point to verification steps rather than assumed causes.
- **Records:** Note syllabus and sources used, variant inputs, reviewed changes, known limitations, and responsible reviewer when required.

Passing a software build is only a **presentation-validation gate**. It is not engineering acceptance or proof of learner competence.

## 4. Standard assembly output and file organization

Illustrative package; actual directories depend on the approved storage location:

~~~text
training/
  courses/
    modbus-001/
      SYLLABUS.md                    # curriculum authority
      course.json                    # active course/engine manifest (derived)
      variants/
        [variant-id]/
          profile.yaml               # profile used for this generation
          coverage.md                # outcomes, selected units, skipped units
          lessons/                   # selected/expanded instructional units
          scenarios/                 # diagrams, lab fault cards, sample data
          questions/                 # tagged checks + rationale
          instructor.md              # if instructor/lab variant
          index.html                 # self-contained or deployable HTML
          generation-record.md       # source and acceptance snapshot
~~~

A real project variant with confidential content lives in **approved private project storage**, not the framework repository. The repository may keep only a sanitized template or synthetic example.

### Traceability example

| Outcome | Syllabus block | Presentation | Assessment evidence |
| --- | --- | --- | --- |
| LO-04 | G01/G02/G05 | Gateway lesson + routing diagram | Correctly identify Unit ID/port mapping and meaning of ping/TCP/read results |
| LO-05 | X04 + CAL-01/02 | Polling worksheet | Nominal/degraded scan budget and written interpretation |
| LO-06 | Playbook T02–T06 | Fault-isolation scenario | Ranked hypotheses, approved test sequence and as-left record |

No row can claim “assessed” unless it points to a real check/observed work product.

## 5. Status and evolution

- **Generic contract status:** Candidate for pilot; not a production LMS policy.
- **MODBUS-001 syllabus:** Owns its detailed learning unit/lab catalog and must be versioned independently of the HTML engine.
- **Frozen v0.2 HTML baseline:** Leave unchanged.
- **Course-specific implementation:** Review derived manifests and question banks against the most recent accepted syllabus; reconcile with individual branch work deliberately.
- **Curriculum revision:** Changes to learning outcomes, mandatory floor, unit/lab intent or pass standards require a syllabus revision and dependent variant review. Cosmetic HTML changes do not.
