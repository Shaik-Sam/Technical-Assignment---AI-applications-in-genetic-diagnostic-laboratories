from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Project 3 — Workflow Optimization (Stub)", version="0.1.0")


class DurationRequest(BaseModel):
    job_id: str
    step_name: str
    test_type: str | None = None
    station_type: str | None = None
    queue_length: int | None = Field(default=None, ge=0)


class DurationResponse(BaseModel):
    job_id: str
    step_name: str
    p50_minutes: float = Field(..., ge=0)
    p90_minutes: float = Field(..., ge=0)
    model_version: str


class PlanRequest(BaseModel):
    horizon_hours: int = Field(default=24, ge=1, le=168)


class PlanResponse(BaseModel):
    horizon_hours: int
    notes: str
    model_version: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/predict/step-duration", response_model=DurationResponse)
def predict_step_duration(req: DurationRequest):
    
    base = 30.0
    if req.queue_length is not None:
        base += min(req.queue_length, 20) * 2.0
    return DurationResponse(
        job_id=req.job_id,
        step_name=req.step_name,
        p50_minutes=base,
        p90_minutes=base * 1.8,
        model_version="stub-0.1.0",
    )


@app.post("/plan", response_model=PlanResponse)
def plan(req: PlanRequest):
    
    return PlanResponse(
        horizon_hours=req.horizon_hours,
        notes="Stub planner. Replace with DES + scheduling (EDD/CR or CP-SAT).",
        model_version="stub-0.1.0",
    )

