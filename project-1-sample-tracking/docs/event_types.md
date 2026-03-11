# Event taxonomy (examples)

Keep event types **small and consistent**, with details in `metadata_json`.

## Reception / accessioning
- `SAMPLE_RECEIVED`
- `ACCESSION_CREATED`
- `PATIENT_INFO_VERIFIED`
- `PRE_ANALYTICAL_QC_STARTED`
- `PRE_ANALYTICAL_QC_PASSED` / `PRE_ANALYTICAL_QC_FAILED`

## Wet lab
- `EXTRACTION_STARTED` / `EXTRACTION_COMPLETED`
- `DNA_QC_MEASURED` (metadata: conc, 260_280, volume, pass/fail)
- `LIBRARY_PREP_STARTED` / `LIBRARY_PREP_COMPLETED`
- `LIBRARY_QC_MEASURED` (metadata: size, conc, molarity, pass/fail)

## Sequencing
- `POOLING_COMPLETED`
- `RUN_CREATED` (metadata: run_id, lane, platform)
- `RUN_STARTED`
- `RUN_COMPLETED`
- `PRIMARY_QC_PASSED` / `PRIMARY_QC_FAILED`

## Bioinformatics / reporting
- `BIOINFO_STARTED` / `BIOINFO_COMPLETED`
- `VARIANT_REVIEW_STARTED` / `VARIANT_REVIEW_COMPLETED`
- `MEDICAL_SIGNOUT_COMPLETED`
- `REPORT_GENERATED`
- `REPORT_DISPATCHED`

## Exceptions
- `REWORK_REQUESTED` (metadata: reason_code)
- `SAMPLE_ON_HOLD` / `SAMPLE_RESUMED`
- `SAMPLE_CANCELLED`

