from unittest.mock import patch

from fastapi.testclient import TestClient
from sqlalchemy.exc import SQLAlchemyError

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


@patch("app.main.check_database_connection")
def test_database_health_endpoint_returns_connected_status(mock_check) -> None:
    mock_check.return_value = True

    response = client.get("/health/database")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "database": "connected",
    }


@patch("app.main.check_database_connection")
def test_database_health_endpoint_returns_503_when_database_fails(
    mock_check,
) -> None:
    mock_check.side_effect = SQLAlchemyError("Simulated database failure")

    response = client.get("/health/database")

    assert response.status_code == 503
    assert response.json() == {
        "detail": {
            "status": "unhealthy",
            "database": "unavailable",
        }
    }
