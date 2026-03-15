import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    data = response.json()

    assert "status" in data
    assert "api" in data
    assert "model" in data


def test_predict_valid_review():
    payload = {"review": "This product is amazing!"}

    response = client.post("/predict", json=payload)

    assert response.status_code == 200
    assert "sentiment" in response.json()


def test_predict_invalid_payload():
    payload = {"text": "This product is amazing!"}

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_empty_review():
    payload = {"review": ""}

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_whitespace_review():
    payload = {"review": "   "}

    response = client.post("/predict", json=payload)

    assert response.status_code == 422


def test_predict_too_long_review():
    payload = {"review": "a" * 1001}

    response = client.post("/predict", json=payload)

    assert response.status_code == 422