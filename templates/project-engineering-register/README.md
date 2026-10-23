# Project Engineering Register (PER) — official blank master

**Latest owner-released structural template:** [PROJECT_PER_v1.2.xlsx](PROJECT_PER_v1.2.xlsx) (2026-10-23). Previous [v1.1](PROJECT_PER_v1.1.xlsx) remains an historical release, **not** the default initializer.

Before beginning a project, copy the master file to project-controlled storage and create a project revision. Never record project scope, client names, network/serial data, customer documents, personal links, prices or source extracts in this public framework. Engineering acceptance, progress and baselines are not granted by using a template.

v1.2 contains **17 operational sheets**, retaining revised dashboards, separate WORK PACKAGES / WP PROGRESS, the independent PUNCH LIST / ISSUES / RFI REGISTER and traceability registers. The retired hidden `RFI LEGACY` worksheet and two synthetic test tabs are **not** included. Their [QA cases](tests/PER_v1.2_QA.md) and [optional project consistency script](../../scripts/check_project_per.py) remain in this framework, rather than project copies. The `REGISTRY GUIDE` documents the generic data contract.

**Validate:** `python scripts/validate_blank_per.py templates/project-engineering-register/PROJECT_PER_v1.2.xlsx` (requires `openpyxl`). See [changelog](CHANGELOG.md) and [manifest](PROJECT_PER_v1.2_manifest.json).
