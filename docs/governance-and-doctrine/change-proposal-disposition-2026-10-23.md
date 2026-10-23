# Controls-engineering proposal disposition — 2026-10-23

**Status:** Proposed lessons triaged and integrated where verified. New playbooks/hardware pages are **DRAFT**, not mandatory KIS standards or project-specific acceptance. This file contains no client data.

| Proposal | Disposition | Location / remaining decision |
|---|---|---|
| P1 Shark 250 | Draft hardware page created from EIG manual/brochure | [EIG Shark 250](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/hardware/power-monitoring/eig-shark-250.md); precise card input specs and Modbus registers not accepted |
| P2 UPS network cards | Investigation stub | [UPS cards](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/hardware/power-monitoring/ups-network-cards.md); compatibility NOT VERIFIED |
| P3 ATS contacts | Investigation stub | [ASCO ATS contacts](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/hardware/power-monitoring/asco-ats-controllers.md); catalog/terminal drawings still required |
| P4 ATS/generator via meter | Conditional design playbook | [Monitoring pattern](../design-playbooks/patterns/ats-generator-status-monitoring.md); no unsupported default contact/engine-run assumption |
| P5 As-found photo verification | Lightweight evidence pattern | [As-found verification](../design-playbooks/patterns/as-found-verification.md); integrate with M2 |
| P6 Public data rule | Added to AI guide | [Shared AI governance](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/AI/AGENT-FRAMEWORK-GUIDE.md) |
| P7 Competing Devices vs hardware directories | **Deferred** namespace consolidation | Preserve existing links; do not move physical device pages without migration redirects and index audit |
| P8 Previously contaminated v1.0 PER | Owner reports fixed with v1.1; new sanitization applied to v1.2 | [v1.2 master](../../templates/project-engineering-register/PROJECT_PER_v1.2.xlsx), [blank-master validation script](../../scripts/validate_blank_per.py) and workflow |
| P9 PLC hardware I/O sizing schema | **Candidate contract only**, no accepted EDP workbook change | [Allocation/counting proposal](../engineering-data/point-allocation-and-counting-proposal.md); pilot mapping and worksheet design needed before v1.1 EDP release |
| P10 AB PLC, ABB ACH580, Modbus-to-EIP gateway | Draft hardware pages created | [Rockwell](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/Devices/Controllers/Allen-Bradley/Logix-Plant-Controllers.md), [ABB](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/Devices/VFDs/ABB-ACH580.md), [Moxa](https://github.com/kissolutions/knowledgebase_wikijs/blob/main/hardware/gateways/moxa-mgate-5105-mb-eip.md). Moxa **does not convert BACnet** |
| P11 Constant-primary/variable-secondary CHW plant | Draft decision playbook | [CHW plant](../design-playbooks/patterns/chw-primary-secondary-plant.md); source-backed takeoff and sequence approval required |
| P12 Staged PLC availability | Draft decision playbook | [Staged availability](../design-playbooks/patterns/hvac-plc-staged-availability.md); hardware reuse, switchover timing and compatible remote I/O remain verification gates |

## Guardrails

- **Framework owns patterns and technical hardware knowledge; project PER owns approved scope, architecture decisions and engineering evidence.**
- No project identity, private source data or vendor/client contract records belong in public framework repositories.
- Do not make a hardware catalog claim from a draft architecture; verify exact model/revision and communication capability first.
- Review P9 (EDP workbook data contract) with owner after at least one complete PLC sizing pilot before modifying the accepted v1.0 EDP template.
