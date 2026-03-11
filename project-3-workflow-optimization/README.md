#Project 3 — AI-Based Laboratory Workflow Optimization (Genetic Tests)

Goal
Develop an AI-driven concept that optimizes lab workflow by predicting:
- Processing time per step (cycle time)
- Machine utilization / capacity (instruments + staff)
- End-to-end TAT per sample/test

And then uses those predictions to:
- Plan and schedule work (batching, routing, prioritization)
- Prevent bottlenecks (proactive staffing/instrument allocation)
- Meet SLAs with minimal cost and rework

This is a classic operations research + ML hybrid: ML forecasts inputs; optimization decides actions.

 System view (what we optimize)
 Resources
- instruments (extractors, qPCR/Qubit, library prep robots, sequencers, etc.)
- staff by skill (techs, scientists, reviewers)
- consumables constraints (kits/flowcells), shift calendars

 Jobs
Samples/tests, each with:
- ordered sequence of steps (some optional/conditional based on QC)
- due date (TAT), priority, batching rules, compatibility constraints

 Objective (examples)
Minimize:
- missed TAT penalties (weighted by priority)
- total lead time / WIP
- overtime / idle time
- changeovers (setup time) and rework

 Data required
Minimum: historical event logs with timestamps (similar to Project 1), plus resource assignments.

 Key tables
- `jobs` (sample_id/test)
- `job_steps` (step_name, required, station_type)
- `events` (step started/completed with resource identifiers)
- `resources` (instrument/staff, capacity, shift calendar)
- `downtime` (maintenance/unplanned outages)

See `docs/schema.md`.

ML components
 1) Step duration prediction
Predict duration for each step given context.
- Models: gradient boosting or quantile regression (P50/P90).
- Features: test type, batch size, operator, instrument, day/time, prior QC outcomes, queue length.

 2) Arrival forecasting
Predict incoming workload by test type (daily/weekly).
- Models: SARIMAX/Prophet-like, or tree-based with calendar features.

 3) Rework probability
Predict chance of QC fail / rework loops at each stage.
- Helps planners allocate buffer time and contingency capacity.

 Optimization layer
Approach A: Simulation + heuristic scheduling (recommended first)
1. Use ML to estimate step durations and branching (QC pass/fail).
2. Run a discrete-event simulation (DES) to forecast queues and utilization.
3. Apply heuristics:
   - earliest due date (EDD)
   - critical ratio (CR)
   - minimize setup/changeover
4. Compare policies in simulation and choose best.

 Approach B: Mathematical optimization (MILP / CP-SAT)
Formulate scheduling with constraints:
- resource capacities
- precedence constraints (step order)
- batching (e.g., sequencing pools)
- shift calendars
Solve daily/shift-level plans with OR-Tools CP-SAT.

 Approach C: RL (advanced)
Only after stable simulation and strong baselines:
- RL agent selects dispatching rules
- Reward trades off SLA, WIP, overtime
Harder to validate in regulated environments; keep human oversight.

 KPIs and evaluation
 Forecast accuracy
- MAE for step durations
- coverage for prediction intervals (P90 should cover ~90%)

 Operational performance (simulation / pilot)
- % samples within TAT (by priority)
- mean/median lead time
- resource utilization (by station)
- overtime hours
- WIP levels and queue time distributions

 Deployment concept
1. Data ingestion from LIMS/instruments → event log
2. Predictor services for duration/rework/arrivals
3. Planner produces a recommended schedule (shift plan)
4. Dashboard shows:
   - predicted bottlenecks next 24–72h
   - “what-if” (add staff, extend shift, reroute)
   - recommended dispatch list per station
5. Feedback loop: compare predicted vs actual; retrain monthly

 Safety and governance
- Start as “decision support” (recommendations only)
- Keep SOP-based guardrails for priority handling (clinical safety)
- Audit every schedule recommendation and overrides

 Folder guide
- `docs/`: schema, simulation outline, optimization options
- `data/`: export templates
- `src/`: stub API endpoints (predict + plan)
- `notebooks/`: EDA + forecasting placeholders

 Optional: run the stub API
From repo root:

```bash
python -m uvicorn project-3-workflow-optimization.src.app:app --reload --port 8003
```

