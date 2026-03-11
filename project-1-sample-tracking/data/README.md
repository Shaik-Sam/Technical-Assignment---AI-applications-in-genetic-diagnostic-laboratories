Data collection guide (what to export from LIMS)

Minimum dataset to build the first model
You can start with two CSV extracts:

1) samples.csv (1 row per sample)
Suggested columns:
- sample_id
- test_type
- priority
- sample_type
- received_at
- due_at
- final_report_dispatched_at (or NULL if cancelled/incomplete)
- final_status (DISPATCHED / CANCELLED / INCOMPLETE)

2) sample_events.csv (many rows per sample; append-only)
Suggested columns:
- event_id
- sample_id
- event_type
- station
- event_ts
- actor_id (pseudonym)
- instrument_id
- qc_value_1, qc_value_2, ... (optional flattened)
- metadata_json (optional)

Privacy / compliance
- Prefer pseudonymous IDs in analytics.
- Keep PHI only inside the LIMS; copy only what’s needed for operations/AI.
- Ensure retention aligns with lab policy.

Label creation (example)
- Define “missed TAT”: final_report_dispatched_at > due_at
- For each sample, create snapshot times t after key events, and label:
  - will_miss_tat_within_horizon_H (e.g., by due date or within 48h)