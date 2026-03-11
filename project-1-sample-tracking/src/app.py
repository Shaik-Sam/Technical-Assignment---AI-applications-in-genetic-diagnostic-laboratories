from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Project 1 — Sample Tracking (Stub)", version="0.1.0")


class RiskRequest(BaseModel):
    sample_id: str = Field(..., description="Internal sample identifier")
    as_of_ts: str = Field(..., description="ISO timestamp for prediction time")


class RiskResponse(BaseModel):
    sample_id: str
    risk_miss_tat: float = Field(..., ge=0.0, le=1.0)
    eta_p50_hours: float | None = None
    eta_p90_hours: float | None = None
    model_version: str
    notes: str


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/predict/tat-risk", response_model=RiskResponse)
def predict_tat_risk(req: RiskRequest):

    risk = (sum(ord(c) for c in req.sample_id) % 100) / 100.0
    return RiskResponse(
        sample_id=req.sample_id,
        risk_miss_tat=risk,
        eta_p50_hours=None,
        eta_p90_hours=None,
        model_version="stub-0.1.0",
        notes="Replace with trained model + explanation payload (e.g., top SHAP drivers).",
    )

