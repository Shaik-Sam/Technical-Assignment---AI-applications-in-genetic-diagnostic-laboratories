# Discrete-event simulation (DES) outline

## Why simulation?
Before changing lab operations, you want to test policies safely:
- new batching rules
- staffing changes
- instrument acquisition/retirement
- priority dispatching strategies

## Core simulation objects
- **Job**: a sample/test moving through steps
- **Step**: operation requiring a station/resource
- **Resource**: instrument or staff, with availability calendar
- **Queue**: waiting jobs per station

## Random variables (estimated via ML)
- step duration distribution (P50/P90 or parametric fit)
- probability of QC failure causing rework/branch
- arrival process (jobs/day by type)
- downtime events (optional)

## Policy inputs (what we can choose)
- dispatching rule per station (EDD/CR/priority)
- batching size and windows (e.g., pool formation cutoffs)
- overtime/extra shift toggles

## Outputs
- TAT distribution by test type and priority
- utilization and idle time by resource
- queue time distributions by station
- sensitivity analysis (“what if arrivals +20%?”)

