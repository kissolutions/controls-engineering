# Templates — blank masters and examples (proposed policy)

**Status:** proposal for owner review. Nothing has been moved yet.

Every template ships in two forms:

| Form | Purpose | Content |
|---|---|---|
| **Blank master** (`<NAME>_vX.Y.xlsx`) | Copied into project storage to start a project | Headers, formulas, guides and validation only. No project rows. The blank-template check must pass. |
| **Example** (`examples/<NAME>_vX.Y_EXAMPLE.xlsx`) | Shows a person how the system is used and cross-referenced | A small, sanitized data set (a few systems, devices, points, issues, RFIs and change log rows) with the IDs linked across tabs. No client names, addresses, IPs, pricing or private links. |

Rules:

- The blank master is never seeded with example rows "to be deleted"; the example file carries that guidance instead.
- The example is built from a real project's structure but sanitized or synthetic, since this repository is public.
- Example and blank master share a version number; a template change updates both.

Examples (built 2026-11-26 from a sanitized single air handler retrofit):

- `examples/PROJECT_PER_v1.2_EXAMPLE.xlsx`: 2 systems (one in scope, one interface-only), 2 scopes, 3 work packages, 5 sources, 4 records, 2 issues, 3 RFIs (one answered, one open, one notification), 6 links, 3 change log entries using MAJOR.MINOR.BUILD, 1 baseline. Every record, issue and RFI cites the scopes, systems and work packages it affects.
- `examples/Equipment_Device_Points_Template_v1.0_EXAMPLE.xlsx`: 2 equipment items (the AHU and its DDC panel), 13 devices (including engineered panel components: enclosure, power supply, transformer, relays), 9 points. Shows source tags vs signal names vs SCADA names, fail state in the DEVICE notes, a reserved safety input, an interface-only device with no point, and points cross-referenced to PER scopes, work packages, records and RFIs.
- All values are illustrative; names, owner and site are fictional.

Current state:

- `project-engineering-register/PROJECT_PER_v1.2.xlsx` is blank apart from punch list formula scaffolding and the registry guide.
- `project-engineering-register/PROJECT_PER_v1.0.xlsx` still carries a prior project's records (framework proposal P8). Proposed: remove it from the master folder and, if useful, rebuild its cross-reference value as a sanitized `examples/PROJECT_PER_v1.2_EXAMPLE.xlsx`.
- `equipment-device-points/Equipment_Device_Points_Template_v1.0.xlsx` is blank apart from its template guide. An example EDP would follow the same pattern.
