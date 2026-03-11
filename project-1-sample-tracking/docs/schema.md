Suggested schema (minimal, practical)

Below is a simplified schema you can map to a LIMS (or implement as a standalone tracker).

Tables (relational)

samples
- sample_id (PK, string/UUID)
- external_accession_id (string, from LIMS)
- test_type (enum: panel / WES / WGS / CMA / ...)
- priority (enum: routine / urgent / stat)
- sample_type (enum: blood / saliva / tissue / ...)
- received_at (datetime)
- due_at (datetime) — SLA/TAT deadline
- current_station (string)
- current_status (string)
- is_cancelled (bool)

sample_events (append-only; immutable)
- event_id (PK)
- sample_id (FK → samples)
- event_type (string; see event_types.md)
- station (string)
- event_ts (datetime)
- actor_id (string; pseudonymous user id)
- instrument_id (string; optional)
- metadata_json (json) — QC values, reason codes, exception details

stations
- station_id (PK)
- name
- capacity_per_shift (int; optional)
- sla_minutes_target (int; optional)

instruments
- instrument_id (PK)
- type (e.g., extractor, qPCR, sequencer)
- vendor_model
- is_active

instrument_uptime_events (optional)
- id (PK)
- instrument_id
- event_ts
- event_type (UP/DOWN/MAINTENANCE)
- details_json

Why event-sourcing?
- You can always reconstruct “what did we know at time t?”
- It supports audits (critical in diagnostics)
- It simplifies ML snapshot generation