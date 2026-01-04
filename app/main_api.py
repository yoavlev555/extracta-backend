import datetime
from fastapi import FastAPI
from app.api.v1 import documents, users

from app.core.config import config

app = FastAPI(title="Extracta backend API", version=config.version)

# Register routes
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(users.router, prefix="/users", tags=["users"])


@app.get("/health")
def health_check() -> dict[str, str]:
    """Health check endpoint"""
    return {
        "status": "ok",
        "service:": config.app_name,
        "version": app.version,
        "timestamp": datetime.datetime.now(datetime.UTC),
    }
