# PROJECT_PER template changelog

Blank workbook template for the Project Engineering Register (PER). Copy it into authorized project storage before use; never enter project data in this repository copy.

## v1.2 — 2026-10-23

Owner-requested blank template promoted from a revised working workbook. **Project-specific data was removed prior to commit.** The **17-sheet distributed master** preserves all 17 operational worksheet formulas, dashboard/column changes, cell formatting conventions, and 29 data-validation rules from the sanitized submitted workbook: **14,127 formulas and 19,147 styled cells**. The REGISTRY GUIDE was rewritten generically. The hidden duplicate `RFI LEGACY` (1,571 formulas) and auxiliary `SB1 FORMULA TESTS` (81 formulas) / `SB2 CHECKS` (16 formulas) were removed following owner review. None of the 17 operational sheets depended on them. Their testing intent is documented in [v1.2 QA](tests/PER_v1.2_QA.md) with optional standalone checks. A first 20-sheet v1.2 draft was briefly committed before this same-day correction; the published v1.2 binary and SHA-256 manifest now reflect the 17-sheet file. The v1.1 workbook remains historical. Run `scripts/validate_blank_per.py` on any release. Template acceptance does not establish project engineering acceptance or live Excel recalculation.

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
