Project 1 — AI-Based Sample Tracking System (Genetic Lab)

Goal
Design a system that tracks every sample end-to-end (reception → accessioning → extraction → library prep → sequencing → analysis → review → report dispatch) and uses AI/ML to:
- Predict risk of missing TAT (turnaround time)
- Detect bottlenecks and anomalous delays
- Recommend actions (routing, escalation, reprioritization)

This is primarily a workflow + data + prediction problem; the AI component augments a robust LIMS-style tracking backbone.

Laboratory workflow (reference)
Typical sample states (customize to your lab):
- Received → Accessioned → Pre-analytical QC
- Extraction → DNA QC → Library Prep
- Library QC → Sequencing → Primary QC
- Bioinformatics → Variant Review → Medical Sign-out
- Report Generated → Report Dispatched

For each state, record:
- start/end timestamps, operator/instrument, consumables lot (optional), queue position, and exceptions.

What “AI-based tracking” means here
1) Predictive TAT risk scoring (core ML)
- Target: probability a sample will miss its due date (e.g., “miss TAT within next 48h”).
- Granularity: per-sample, updated after each event; optionally per-step ETA.
- Outputs:
  - risk score (0–1)
  - predicted completion time distribution (P50/P90)
  - top contributing factors (SHAP/explanations)

2) Bottleneck detection (analytics + ML)
- Queue-time forecasting per station (extraction, library prep, sequencing, review).
- Change-point / anomaly detection on queue length, cycle time, instrument downtime.

3) Action recommendations (rules + optimization)
Start with rules (high safety / auditable), then add optimization:
- Escalate if risk>threshold and due date < X
- Re-route to alternative instrument / shift if capacity exists
- Re-prioritize based on clinical priority + risk + SLA

Data design (minimal viable, LIMS-friendly)
Use an event-sourced model: every change is an immutable event.

Entities
- Sample: sample_id, patient pseudonym, test type, priority, received_at, due_at, status
- Event: event_id, sample_id, event_type, station, timestamp, actor_id, instrument_id, metadata
- Station: name, capacity, shift calendar
- Instrument: type, maintenance windows, uptime logs

See docs/schema.md and docs/event_types.md for suggested fields.

Features (examples)
Static
- test type (WES/WGS/panel), priority (routine/urgent), sample type (blood/saliva), batching constraints

Dynamic / time-dependent
- time since received, time spent in current station
- number of reworks, QC failures, exception count
- station queue length at event time, average cycle time last 7 days
- instrument downtime features (last 24h)
- staffing/shift indicators (weekday/weekend, night shift)

Modeling approach
Baseline (strong, interpretable)
- Gradient boosted trees (XGBoost/LightGBM/CatBoost) on tabular features.
- Or Cox / survival models for time-to-completion with censoring.

Sequence-aware (optional upgrade)
- Temporal convolution / LSTM / Transformer over event sequences per sample.
Good if event logs are rich and consistent, but harder to validate/explain.

Labels and leakage control
- Labels must use only information available up to prediction time.
- Build “snapshots” after each event: (features_at_t, will_miss_tat) for horizon H.

Evaluation
TAT-risk classifier
- Primary: AUROC, AUPRC (misses are often rare)
- Operational: recall@fixed_alert_rate, alerts/day, lead-time gained
- Calibration: reliability plots / Brier score (important for risk thresholds)

ETA / time prediction
- MAE at station and overall, P90 coverage (prediction intervals)

Offline → online validation
- Backtesting by week/month to simulate deployment
- Shadow mode before triggering real escalations

System architecture (practical)
1. Ingestion: LIMS + instruments + manual stations → event bus (or DB)
2. Store: relational DB + immutable event log (append-only)
3. Feature pipeline: scheduled + streaming feature computation
4. Model service: risk + ETA API (FastAPI) + model registry
5. UI: operations dashboard (queues, risk heatmaps, drill-down)
6. Audit: every alert stores model version + explanations + inputs hash

See docs/architecture.md.

Dashboard (what to show)
- Queue overview: samples by station, age, due-in buckets
- Risk board: top 20 highest risk, sortable by due date / priority
- Bottlenecks: station cycle time trend, queue time distribution
- Exceptions: QC fails, rework loops, instrument downtime

Risks / compliance / safety
- PHI: store only pseudonyms in analytics layer; strict RBAC
- Auditability: event-sourcing + immutable logs
- Bias: urgent vs routine triage; ensure policy is explicit
- Human-in-the-loop: AI suggests; lab leads decide

Implementation plan (deliverable-ready)
- Week 1: define event taxonomy + DB schema + ingestion from LIMS exports
- Week 2: build dashboard + baseline analytics (cycle time, queues)
- Week 3: train baseline risk model + explainability + backtesting
- Week 4: deploy in shadow mode + set alert thresholds + SOP

Folder guide
- docs/: schemas, event types, architecture, KPIs
- data/: what to collect + example CSV headers
- src/: starter FastAPI service + feature builder skeleton
- notebooks/: EDA/model prototype placeholders

Optional: run the stub API
From repo root:

python -m uvicorn project-1-sample-tracking.src.app:app --reload --port 8001