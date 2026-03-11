# Optimization options (practical)

## Option 1: Heuristic dispatching (fastest to deploy)
- Earliest Due Date (EDD)
- Critical Ratio (CR = time_to_due / remaining_processing_time)
- Weighted shortest processing time (WSPT)

Pros: simple, transparent, easy to justify.
Cons: may miss global optimum.

## Option 2: CP-SAT scheduling (recommended for daily planning)
Use [OR-Tools CP-SAT](https://developers.google.com/optimization) to plan:
- assign jobs to resources and time slots
- enforce precedence constraints and shift calendars
- minimize tardiness and overtime

Pros: handles constraints well; produces concrete schedules.
Cons: needs careful modeling and runtime tuning.

## Option 3: MILP for capacity planning (strategic)
Monthly/quarterly:
- estimate required headcount and instrument capacity
- choose overtime/extra shift policies

## Option 4: RL for policy learning (advanced)
Only after simulation is trusted and baselines are stable.

