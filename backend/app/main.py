from fastapi import FastAPI

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


@app.get("/", tags=["Root"])
def root() -> dict[str, str]:
    return {
        "message": "Welcome to Student Performance Intelligence API",
        "docs": "/docs",
    }