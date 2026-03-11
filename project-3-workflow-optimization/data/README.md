# Data exports (templates)

## `jobs.csv`
- `job_id`
- `test_type`
- `priority`
- `received_at`
- `due_at`
- `status`

## `events.csv` (append-only)
- `event_id`
- `job_id`
- `step_name`
- `event_type` (STARTED/COMPLETED/QC_PASSED/QC_FAILED)
- `event_ts`
- `resource_id`
- `station_type`
- `metadata_json` (optional)

## `resources.csv`
- `resource_id`
- `resource_type` (INSTRUMENT/STAFF)
- `station_type`
- `capacity`
- `shift_calendar_id`

## `downtime_events.csv` (optional)
- `id`
- `resource_id`
- `event_ts`
- `event_type`
- `details_json`

