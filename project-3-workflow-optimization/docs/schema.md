# Suggested schema (workflow optimization)

This schema is compatible with event logs used in process mining and scheduling.

## `jobs`
- `job_id` (sample_id or case_id)
- `test_type`
- `priority`
- `received_at`
- `due_at`
- `status`

## `job_steps` (static routing by test type)
- `test_type`
- `step_name`
- `sequence_order`
- `station_type`
- `is_optional`
- `batchable` (bool)

## `events` (append-only)
- `event_id`
- `job_id`
- `step_name`
- `event_type` (STARTED/COMPLETED/QC_PASSED/QC_FAILED/ON_HOLD/RESUMED)
- `event_ts`
- `resource_id` (instrument or staff)
- `station_type`
- `metadata_json` (QC values, reasons, batch_id, etc.)

## `resources`
- `resource_id`
- `resource_type` (INSTRUMENT/STAFF)
- `station_type` (where it can work)
- `capacity` (e.g., samples/hour or 1 for single-machine)
- `shift_calendar` (reference id)

## `downtime_events`
- `id`
- `resource_id`
- `event_ts`
- `event_type` (DOWN/UP/MAINTENANCE)
- `details_json`

