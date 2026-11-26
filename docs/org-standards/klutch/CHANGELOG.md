# Klutch Standards Profile — Changelog

## 0.1 (draft, 2026-11-25)
- Profile created. Document model drafted from the owner's description of the standard drawing set; precedence override record defined in the org-standards README.
- Naming page drafted (device tags vs signal names, owner naming standard, prefix conventions, software point rule, panel and controller tags).
- Narrative format drafted: Overview, Requirements, Operating modes, system sections, Setpoints, Alarms; table columns adopted for trial.
- Validation gates drafted (device representation, completeness, valves, dampers, names, drawing sync, issue checks). UTMB client conventions page added.
- Panel and hardware page drafted: separate 120 VAC fuses for the 24 VDC supply and the 24 VAC transformer, fused 24 VAC terminal distribution; dedicated 24 VAC transformer for damper actuators and the damper proving circuit; relay suppression; KMC rules.
- KMC CAN 4–20 mA problem documented; CR-FP rules (KMC1 relay output, starts open, released after EIO boot confirmation) and validation checks added.
- Critical rule: 4–20 mA packing priority on KMC1 (controlling inputs first, across all systems on the controller; monitoring-only overflow to CAN behind its own switched field power, optional CR-FP2).
- Added device selection (EQ Library, ranges, HPO cards), issues and RFIs, intake checklist (door switches), terminal allocation handoff; validation for ranges, fail states (DEVICE tab final answer) and intake items.
