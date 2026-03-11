from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Project 2 — NGS Run Failure Predictor (Stub)", version="0.1.0")


class RunStartFeatures(BaseModel):
    run_id: str
    instrument_id: str | None = None
    chemistry_version: str | None = None
    read_structure: str | None = None
    loading_concentration: float | None = Field(default=None, ge=0)
    pool_molarity_mean: float | None = Field(default=None, ge=0)
    adapter_dimer_pct: float | None = Field(default=None, ge=0, le=100)
    days_since_maintenance: int | None = Field(default=None, ge=0)
    instrument_warn_count_7d: int | None = Field(default=None, ge=0)


class RunFailurePrediction(BaseModel):
    run_id: str
    p_fail: float = Field(..., ge=0.0, le=1.0)
    top_drivers: list[str]
    recommended_actions: list[str]
    model_version: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/predict/run-failure", response_model=RunFailurePrediction)
def predict_run_failure(features: RunStartFeatures):
    
    p = 0.05
    drivers: list[str] = []
    if features.adapter_dimer_pct is not None and features.adapter_dimer_pct > 5:
        p += 0.25
        drivers.append("High adapter dimer % in pool QC")
    if features.days_since_maintenance is not None and features.days_since_maintenance > 30:
        p += 0.20
        drivers.append("Instrument maintenance overdue (days_since_maintenance > 30)")
    if features.instrument_warn_count_7d is not None and features.instrument_warn_count_7d > 0:
        p += 0.15
        drivers.append("Recent instrument warnings in last 7 days")
    p = min(max(p, 0.0), 0.99)

    actions = []
    if p >= 0.3:
        actions.append("Supervisor review before proceeding (gating).")
    if "High adapter dimer % in pool QC" in drivers:
        actions.append("Re-QC pool; consider bead cleanup / re-prep; verify quantification.")
    if any("maintenance" in d.lower() for d in drivers):
        actions.append("Run instrument QC / check fluidics and optics; consider postponing run.")

    return RunFailurePrediction(
        run_id=features.run_id,
        p_fail=p,
        top_drivers=drivers or ["No strong drivers (stub)"],
        recommended_actions=actions or ["Proceed; continue monitoring (stub)."],
        model_version="stub-0.1.0",
    )

