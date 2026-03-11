 Architecture (concept)

 Inputs
- MGI run setup export (run recipe, sample sheet summary, instrument id)
- Pre-QC report (pool/library QC summary)
- Instrument health / maintenance logs (at run start)

Pipeline
1. Extract: parse exports into normalized `runs` + `pre_qc_features`
2. Validate: schema checks, range checks, missingness checks
3. Predict: model returns `p_fail` and optional failure-mode probabilities
4. Explain: top drivers (e.g., SHAP) + SOP mapping to actions
5. Decide: supervisor accepts/overrides; decision recorded
6. Feedback: after completion, outcomes appended into `post_qc_outcomes`

Controls
- RBAC (only authorized roles can gate/stop a run)
- Audit log (who saw what, what was recommended, what was done)
- Model versioning and drift monitoring

