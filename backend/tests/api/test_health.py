from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint_returns_healthy_status() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "application": "student-performance-intelligence",
    }


def test_root_endpoint_returns_api_information() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["docs"] == "/docs"