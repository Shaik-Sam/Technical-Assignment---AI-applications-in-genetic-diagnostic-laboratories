Failure modes (example taxonomy)

Tune these to your lab’s acceptance criteria and platform behavior.

- LOW_YIELD: total bases/reads below minimum for test menu
- LOW_Q30: quality below threshold, high error rate
- HIGH_DUPLICATION: indicates over-amplification, low diversity, or overloading
- INDEXING_ISSUE: index hopping/cross-talk, demultiplex failure, sample sheet errors
- CONTAMINATION: foreign DNA, human/microbial mix anomalies, internal controls fail
- HARDWARE_FLUIDICS: pressure/flow anomalies, bubbles, leaks
- HARDWARE_IMAGING: focus/drift, camera faults, optics errors
- REAGENT_ISSUE: lot failures, improper storage, expiration
- OPERATOR_SETUP_ERROR: incorrect loading conc, wrong recipe, incorrect pooling ratio
- OTHER/UNKNOWN

For multiclass ML, ensure each class has enough examples; otherwise group rare modes.
