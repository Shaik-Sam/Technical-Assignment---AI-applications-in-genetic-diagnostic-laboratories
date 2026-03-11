Architecture (concept)

Core components
- Event ingestion: LIMS exports / instrument APIs / manual scan stations
- Operational DB: stores samples current state
- Event log: append-only sample_events table (or Kafka topic)
- Feature builder: turns events into ML-ready snapshots
- Model service: risk + ETA prediction endpoint
- Ops dashboard: queues + risk + bottlenecks
- Audit + governance: model registry, versioning, traceability

Data flow (high-level)
1. Operators/instruments produce events (barcode scan, QC measured, step completed)
2. Ingestion validates and appends to event log; updates samples.current_*
3. Feature builder computes:
   - per-sample features (time in state, queue context)
   - per-station features (cycle time trends, queue length)
4. Model service returns:
   - miss-TAT risk (probability)
   - ETA distribution
   - explanations (top drivers)
5. Dashboard displays and triggers SOP-based alerts

Deployment notes
- Start batch (hourly) features; move to near-real-time once stable
- Keep human-in-the-loop for escalations (no automatic rerouting at first)
- Store all predictions with: model version, feature snapshot id, timestamp