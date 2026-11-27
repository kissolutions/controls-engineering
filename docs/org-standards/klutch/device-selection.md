---
title: Klutch Device Selection and Signal Ranges
page_type: governance
page_status: draft
profile_id: klutch
profile_version: 0.1
---

# Klutch Device Selection and Signal Ranges

How Klutch selects field devices and sets their ranges, from requirements to the drawing tables. The EDP is the record of the result; the drawings import from it.

## Sources, in order

1. **Requirements from the source documents.** Pull every value that drives a selection or a range: filter MERV ratings, fan inlet (shroud) pressures and K factors, coil face areas, coil and valve pressure drops, design flows and temperatures, and so on. Cite the source and locator for each.
2. **Typical values, labelled as assumptions.** Where the sources are silent, the agent may supply typical engineering values (for example the usual prefilter MERV for an outdoor air handler, or a dirty-filter pressure drop to set an alarm). Each is recorded as an assumption with its basis, never as a source fact, and is replaced when a source value arrives.
3. **The Klutch EQ Library.** Datasheets for Klutch's go-to and previously used devices are kept in the EQ Library folder at the head of the KIS AUTOMATION drive. Preselect from it first; a device not in the library needs its datasheet added before it is selected.

## Workflow

1. **Requirements.** Agent lists the requirements per device from the sources, plus labelled assumptions.
2. **Preselection.** Agent preselects a device from the EQ Library for each, with the datasheet range and signal type, and shows why it fits (for example: the expected signal at design flow sits inside the transmitter span with margin).
3. **Designer / engineer handoff.** The engineer reviews, adjusts and confirms. Iterate until each selection is accepted.
4. **EDP update.** Record the selection, range, signal type, units, power and conductor count, and the datasheet reference in the EDP.
5. **Drawings.** The P&ID instrument table and other CAD device tables are filled from the EDP. Each instrument description includes its sensor range.

## Validation

- **Requirements to selection:** every selected device's range and rating covers its requirement (design value inside the span, with margin) or the shortfall is an open item.
- **Datasheet to EDP:** model, range, signal type, units and power in the EDP match the datasheet.
- **EDP to CAD tables:** the P&ID instrument table and other device tables match the EDP, including the sensor range in the description.
- **Outputs to output cards:** KMC output interface cards (the HPO series, for example HPO-6702 / HPO-6703) match the signal type and range of the output they serve.
- **Assumptions are visible:** every value that came from a typical assumption is marked as such in the EDP until replaced by a source value.

## Example of the failure this prevents

On an air handler retrofit, the ordered fan airflow transmitter had a 0–5 in. w.c. span, while the fan inlet cone signal at design airflow was about 5.7 in. w.c. The selection could not read design flow. The requirement-to-selection check catches this before ordering.
