Project 2 — AI System to Predict NGS Run Failure (MGI Platform)

Goal
Build an AI/ML approach that uses pre-QC parameters at the start of an NGS run (MGI) to:
- Predict probability of run failure early (before most cost is incurred)
- Recommend preventive actions (stop/reload/re-pool/re-calibrate)
- Reduce waste: flow cells, reagents, staff time, and downstream rework

Here “failure” should be defined operationally (e.g., run aborted, Q30 below threshold, yield below target, high duplication, index hopping, severe GC bias, contamination flags, or “investigation required”).

Scope and assumptions
Decision point
At run start (or earliest available checkpoint), only use:
- instrument status + maintenance history
- consumables/reagent lots
- environmental conditions (optional)
- library/pool QC summary (from lab QC)
- run plan/configuration (read length, chemistry, loading concentration, lane setup)

Outputs
- p_fail: probability of failure category
- reason codes: top drivers (interpretable features)
- actions: rule-based SOP suggestions based on predicted failure mode

Data needed

Table 1: runs (1 row per run)
- run_id
- platform (MGI model)
- start_ts, end_ts
- run_recipe / chemistry_version
- read_length (e.g., PE150)
- lane_count / flowcell_type
- operator_id (pseudonym)
- instrument_id
- was_success (bool) + failure_mode (enum)
- failure_reason_notes (free text; optional for later NLP)

Table 2: pre_qc_features (captured at run start)
Examples (replace with what MGI exports + lab QC produces):
- Pool / library QC: mean molarity, size distribution summary, %adapter dimers, concentration variance across libraries, #libraries, %low-input libraries
- Loading / setup: loading concentration, denaturation conditions, pooling ratios, index set info
- Instrument: error logs count (last 7 days), imaging module health flags, fluidics pressure warnings, last maintenance date, temperature calibration date
- Reagents / consumables: lot IDs, time since opening, storage excursions (if tracked)
- Environment: room temp/humidity (if available)

Table 3: post_qc_outcomes (ground truth)
Define success/failure using thresholds:
- yield (Gb), %>=Q30, %PF reads, error rate, duplication, insert size shifts, contamination, index cross-talk

Label definition (important)
You need crisp labels for supervised learning:
- Binary: PASS vs FAIL (based on a policy threshold)
- Multiclass: PASS / LOW_YIELD / LOW_Q30 / FLUIDICS_ERROR / IMAGING_ERROR / CONTAMINATION / OTHER

Start with binary, then evolve to multiclass once data volume supports it.

Modeling approach
Baseline (recommended)
- Gradient boosted trees on tabular pre-QC features.
  - Pros: strong performance, handles missingness, explainable.
  - Output: calibrated probability of failure.

Alternative / extensions
- Logistic regression as a transparent baseline.
- Anomaly detection when failures are rare:
  - Isolation Forest / One-Class SVM / autoencoder over “normal” runs
  - Use as a second signal: “this run setup is unusual”
- Text + logs:
  - Vectorize early instrument log messages to predict hardware-related failures.

Training strategy (data realities)
- Failures are typically rare → class imbalance.
- Use:
  - stratified splits by time
  - focal loss / class weights
  - precision-recall optimization
- Avoid leakage:
  - do not include metrics generated after sequencing has progressed
  - use only “at run start / pre-QC” fields

Evaluation (what matters to the lab)
- AUPRC (more meaningful with rare failures)
- Recall at fixed false-positive rate
  - e.g., “catch 70% of failures while stopping <2% good runs”
- Cost-weighted utility
  - model the cost of stopping a good run vs letting a bad run proceed
- Calibration
  - risk thresholds must be trustworthy

Action layer (SOP-driven)
Predictions must map to safe actions; start rule-based:
- If p_fail high AND driver indicates low loading conc → “re-quantify pool, adjust loading”
- If driver indicates instrument health warnings → “run instrument QC / check fluidics, consider postponing”
- If driver indicates reagent lot anomalies → “verify lot, check storage, swap reagents”

Store every alert with:
- model version, features, top drivers, recommended actions, operator decision.

System architecture (concept)
1. Data capture: parse MGI run setup + pre-QC report exports
2. Feature store: compute run-level features at “decision time”
3. Model service: returns p_fail, failure_mode_probs, top drivers
4. Run gating UI: a “go/no-go” screen before committing reagents
5. Feedback loop: outcomes appended automatically after run completion

See docs/architecture.md and docs/feature_list.md.

Deployment plan (assignment-ready)
- Phase 1 (shadow): predict on runs, no intervention; measure PR + utility
- Phase 2 (assistive): show risk + top drivers to supervisors; log decisions
- Phase 3 (gating): require supervisor acknowledgment above threshold

Folder guide
- docs/: feature list, failure modes, architecture, evaluation
- data/: export templates and privacy notes
- src/: starter inference API stub
- notebooks/: EDA + baseline model placeholders

Optional: run the stub API
From repo root:

python -m uvicorn project-2-ngs-run-failure-mgi.src.app:app --reload --port 8002