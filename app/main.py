from fastapi import FastAPI, HTTPException, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

from app.model_loader import load_model
from app.schemas import ReviewRequest, PredictionResponse
from app.monitoring import (
    REQUEST_COUNT,
    PREDICTION_ERRORS,
    PREDICTION_LATENCY,
    update_system_metrics,
)

app = FastAPI(title="Sentiment Analysis API")

try:
    model = load_model()
except Exception:
    model = None


@app.get("/health")
def health():
    if model is None:
        return {
            "status": "degraded",
            "api": "running",
            "model": "not loaded"
        }

    return {
        "status": "ok",
        "api": "running",
        "model": "loaded"
    }


@app.get("/metrics")
def metrics():
    update_system_metrics()
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.post("/predict", response_model=PredictionResponse)
def predict_sentiment(request: ReviewRequest):
    REQUEST_COUNT.inc()

    if model is None:
        PREDICTION_ERRORS.inc()
        raise HTTPException(
            status_code=503,
            detail="Model not available."
        )

    with PREDICTION_LATENCY.time():
        try:
            prediction = model.predict([request.review])
            return {"sentiment": str(prediction[0])}
        except Exception as e:
            PREDICTION_ERRORS.inc()
            raise HTTPException(
                status_code=500,
                detail="Prediction failed due to an internal server error."
            ) from e