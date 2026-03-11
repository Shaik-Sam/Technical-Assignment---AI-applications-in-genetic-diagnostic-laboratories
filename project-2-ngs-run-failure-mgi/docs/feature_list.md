Feature list (pre-QC / run-start)

This is a practical checklist; implement what you can reliably capture.

Pool / library QC (from wet lab)
- mean/median molarity, standard deviation across libraries
- mean fragment size, IQR, %adapter dimers
- %libraries below minimum concentration
- number of libraries pooled, total mass loaded
- GC-content summary if available, low-diversity flags

Run plan / configuration
- chemistry version, kit type, read structure (PE/SE, read lengths)
- expected yield target (Gb), target cluster/DNB density
- sample sheet validity checks (unique index combinations, naming rules)

Loading / preparation
- loading concentration used
- denaturation/incubation times, temperatures (if recorded)
- storage time since pooling, freeze-thaw counts (if tracked)

Instrument health (leading indicators)
- time since last maintenance, last optics/fluidics calibration
- early warning counts from logs (last N runs / last 7 days)
- module health flags (fluidics, temperature, optics)
- number of recent aborted runs on same instrument

Reagents and consumables
- lot IDs for key reagents, expiration, time since opened
- storage excursions / chain-of-custody if available

Environment (optional)
- room temperature/humidity at setup time

Target leakage warning
Do not include metrics computed after run progression (e.g., final Q30).