# KIS Training Engine Architecture — candidate

## Scope

Training is a **presentation and learning layer**, separate from systems engineering source authority and domain-specific execution frameworks.

| Component | Owns | Does not own |
|---|---|---|
| Shared KIS Knowledgebase (`knowledgebase_wikijs`) | Canonical communication concepts, manufacturer-backed hardware facts, calculator methods | Local training navigation and student progress |
| Controls Engineering (`controls-engineering`) | Network design and troubleshooting playbooks and engineering procedures | A duplicated source of shared theory or equations |
| Training engine | Layout, sidebar, playbook navigator, scenario rendering, quizzes, progress UX | Engineering truth or course-specific claims |
| Canonical course syllabus (`courses/<course-id>/SYLLABUS.md`) | Course learning outcomes, required curriculum, assessment coverage, and audience/scenario variation rules | Engine presentation, manufacturer-specific engineering truth |
| Course packages | Lesson sequence, objectives, exercise variants, source pointers, question selection | Changes to canonical source documents |
| Project engineering records | Project-specific network design inputs, dispositions and acceptance | Generic training question-bank truth |

## Current residence

The proof of concept lives at `training/engine/baselines/v0.2/index.html` while the engine is being proven against **Modbus 001**. A future reusable `kis-training` repository may be appropriate once more than one engineering domain consumes the engine. Do not move it during the freeze.

## Proposed future structure (not implemented by the baseline)

```text
training/
  engine/
    baselines/v0.2/index.html    # immutable approved UI prototype
    src/                         # reusable components, in later iteration
  courses/
    modbus-001/
      course.json                # planned course map/source pointers
      lessons/                   # planned independently loaded content stubs
      exercises/                 # planned scenarios and diagrams
      questions/                 # planned tagged question bank
```

## Core component contracts for next iteration

- `ChapterSidebar`: stable section and lesson IDs; collapsible groups; active state.
- `PlaybookFlow`: ordered step IDs, left-to-right diagram, each step opens its unique lesson and supports anchor-based navigation and focused/continuous views.
- `LessonPanel`: loads an individual HTML lesson stub; deep links remain stable.
- `ScenarioDiagram`: takes explicit stages/state and redraws a common topology; may use Mermaid or SVG as appropriate; clearly labels simulated behavior.
- `EngineeringCalculator`: binds fields and outputs to a versioned canonical method; supports explicit assumptions and unit validation.
- `KnowledgeCheck`: stable question IDs with tags for chapter *and* domain, answer feedback, and user progress separate from engineering acceptance.
- `TroubleshootingSimulator`: injects controlled test faults into an instructional topology and explains observations.

## Course build gate

A course cannot be marked fully built solely because the generic engine demo runs. All required chapters, playbook steps, calculator references, questions and canonical-source provenance must be complete and reviewed. For Modbus 001, the ten-step network design flow and troubleshooting flow need individual chapter content rather than placeholders.
