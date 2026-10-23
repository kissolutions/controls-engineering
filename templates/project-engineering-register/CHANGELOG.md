# PROJECT_PER template changelog

Blank workbook template for the Project Engineering Register (PER). Copy it into authorized project storage before use; never enter project data in this repository copy.

## v1.2 — 2026-10-23

Owner-requested blank template promoted from a revised working workbook. **Project-specific data was removed prior to commit.** The 20-sheet workbook preserves the submitted dashboard and strategic column changes, spreadsheet color/fill conventions, 15,795 formulas, 26,083 styled cells and 29 data-validation rules. The REGISTRY GUIDE was rewritten generically. Synthetic SB1/SB2 formula tests, preconfigured legacy threshold helpers and default Open status remain as test/schema mechanics, **not project records**. The v1.1 workbook is retained for version history. See `PROJECT_PER_v1.2_manifest.json`; run `scripts/validate_blank_per.py` before modifying or releasing another template. Acceptance here covers template structure only, not engineering data or field behavior.

## v1.1 — 2026-10-22

Structure revision, owner-accepted after a pilot on a live project (pilot data not included). Minor version: the register contract, ID schemes and record tabs are unchanged; the work package and progress views changed.

**Work package definition and progress are separate tabs**
- `WORK PACKAGES` now holds definition only and owns WP IDs: ID, package code, boundary, hidden legacy selector, priority, parent WP, primary/additional scope, responsible team or person, method, deliverable, dependencies, progress columns in use, tracking basis, references, review state, notes, and a derived check that each WP has exactly one progress row.
- New `WP PROGRESS` tab holds entered progress, one row per WP ID chosen from `WORK PACKAGES` (dropdown on named range `ValidWorkPackageIDs`): percentages, C&E, program changes, SAT, vendor checks, Blocked (X) and comments. Package code, scope, priority, completion, gate and open punch/RFI/issue counts are formulas.
- `DASHBOARD` and `BLOCKED ITEMS REPORT` read `WP PROGRESS`; blank progress now displays blank instead of 0.

**Progress value convention**
- Number 0–1 = progress; `--` = column not used for this WP; blank = not entered; any other text shows `CHECK`.
- "Completed?" columns keep `--` as `--` (v1.0 showed text as "Yes" because text compares greater than numbers).
- Internal gate is complete when every column the WP uses is complete; shows `No` (was `--`) when not complete, `--` when the WP uses no columns.

**Scope progress is derived**
- `SCOPE PROGRESS` tab removed. `SCOPE DASHBOARD` derives per-column scope progress as the equal-weight average over WPs whose Primary Scope is that scope (blank and `--` excluded), plus WPs gate complete and a blocked-WP count. The scope Blocked? (X) remains human-managed.

**Scope work actions**
- New `SCOPES` column R `Work Actions` carries the M1 action vocabulary (furnish, install, remove, replace, modify, rewire, reprogram, integrate, monitor, test, document, coordinate). Warning-style dropdown: pick one or type several separated by `; `. Blank = not yet established.
- Removed the action-list dropdown that v1.0 had on `SCOPES` column C (Functional / Drawing Boundary, a free-text field).

**Other**
- `RFI REGISTER` Primary WP dropdown uses `ValidWorkPackageIDs` (survives Excel round trips).
- `REGISTRY GUIDE` rewritten as generic guidance, including when to split work packages and the rule for verbatim names (file, folder, document title and drawing-label quotes are copied exactly).
- New check tabs: `WP CHECKS` (structure checks and a sample roll-up test) and `WP FORMULA TESTS` (sample cases for the completion and gate formulas). Sample data only.
- All example and legacy content removed from data rows, saved filters and document properties; v1.1 is blank.

## v1.0

First owner-accepted structure baseline.
