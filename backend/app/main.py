from fastapi import FastAPI, HTTPException
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import check_database_connection

app = FastAPI(
    title="Student Performance Intelligence API",
    description="Academic performance analytics and student management.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {
        "status": "healthy",
        "application": "student-performance-intelligence",
    }


@app.get("/health/database", tags=["Health"])
def database_health_check() -> dict[str, str]:
    try:
        check_database_connection()
        return {"status": "healthy", "database": "connected"}
    except SQLAlchemyError as exc:
        raise HTTPException(
            status_code=503,
            detail={"status": "unhealthy", "database": "unavailable"},
        ) from exc


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    return {
        "message": "Welcome to Student Performance Intelligence API",
        "docs": "/docs",
    }
