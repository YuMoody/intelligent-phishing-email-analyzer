from fastapi.testclient import TestClient

from app.main import app


def test_health_route():
    client = TestClient(app)

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_index_route_renders():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert "Phishing Email Analyzer" in response.text

