import datetime

from fastapi import FastAPI

from app.api.v1 import documents, users
from app.core.config import config
from app.core.logger import init_logger

logger = init_logger(__name__)
app = FastAPI(title="Extracta backend API", version=config.version)


# Register routes
app.include_router(documents.router)
app.include_router(users.router)


@app.get("/health", tags=["Health"])
def health_check() -> dict[str, str]:
    """Health check endpoint"""
    return {
        "status": "ok",
        "service": config.app_name,
        "version": app.version,
        "timestamp": datetime.datetime.now(datetime.UTC),
    }
