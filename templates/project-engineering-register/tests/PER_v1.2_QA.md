# PER v1.2 tests removed from project workbook

The original 20-sheet draft contained three auxiliary sheets which were removed from the **17-sheet distributed v1.2 master** after owner review:

- **RFI LEGACY (hidden):** duplicate older punch/RFI-style register. Its 1,571 formulas consisted primarily of prefilled row numbering, Work Package lookup and elapsed-days calculations. No operational sheet referred to it; it is retired, **not** a source of record.
- **SB1 FORMULA TESTS:** synthetic cases for the six WP progress-completion fields and the internal gate. Testing intent preserved below; not required in live project workbooks.
- **SB2 CHECKS:** synthetic scope-average examples plus project Work Package/Progress data-health diagnostics. Replaced, in part, by optional \`scripts/check_project_per.py\`. **This script checks identities and progress input values; it does not recalculate Excel formulas.**

## Progress result contract from SB1

For a populated WP ID, each \`WP PROGRESS\` stage (E–J) maps to completed indicators (M–R):

| Input | Result |
|---|---|
| Number 1 (or greater) | Yes |
| Number 0 | No |
| Number strictly between 0 and 1 | PARTIAL |
| \`--\` (spaces trimmed) | \`--\` (not used) |
| Blank | Blank (not entered) |
| Other text (\`n/a\`) | CHECK |

\`Internal Progress Gates Complete?\` is \`--\` if all six indicators are \`--\`; **Yes** if each is Yes or \`--\` and at least one Yes; otherwise **No**. A blank WP ID keeps its derived indicators blank. The original SB1 cases included all complete, engineering-only complete/partial, no columns used, a mixed valve-work example, blank engineering, nothing started, stray text and padded \`--\`.

## Structural diagnostics from SB2

1. Exactly one progress row for each defined WP ID (if work has reached the tracking stage).
2. No duplicate WP ID on either sheet.
3. No \`WP PROGRESS\` ID outside \`WORK PACKAGES\`.
4. No invalid progress values (\`CHECK\` indicates a typing/data error).
5. Scope roll-up sample: 1 and 0.5 average to 0.75, ignoring blanks and \`--\`, but **including zero**.

## Where to run checks

\`\`\`bash
python scripts/validate_blank_per.py templates/project-engineering-register/PROJECT_PER_v1.2.xlsx
python scripts/check_project_per.py /path/to/project/PER.xlsx
\`\`\`

The first checks blank template shape, data leakage and formula preservation; the second checks actual project Work Package identities and progress-value semantics. They are not an Excel recalculation test, formal source reconciliation or project acceptance gate.
