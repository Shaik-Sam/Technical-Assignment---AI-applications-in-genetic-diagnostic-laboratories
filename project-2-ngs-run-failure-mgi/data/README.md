# Data exports (templates)

## `runs.csv` (one row per run)
Suggested columns:
- `run_id`
- `instrument_id`
- `platform_model`
- `chemistry_version`
- `kit_type`
- `read_structure`
- `start_ts`
- `operator_id`
- `flowcell_type`
- `lane_count`
- `loading_concentration`
- `reagent_lot_1`, `reagent_lot_2`, ...

## `pre_qc_features.csv` (captured at run start)
Suggested columns:
- `run_id`
- `pool_molarity_mean`
- `pool_molarity_std`
- `fragment_size_mean`
- `adapter_dimer_pct`
- `libraries_count`
- `low_conc_libraries_pct`
- `instrument_warn_count_7d`
- `days_since_maintenance`
- `room_temp_c` (optional)
- `room_humidity_pct` (optional)

## `post_qc_outcomes.csv` (ground truth)
Suggested columns:
- `run_id`
- `was_success` (0/1)
- `failure_mode`
- `yield_gb`
- `q30_pct`
- `duplication_pct`
- `contamination_flag` (0/1)

