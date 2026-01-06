import datetime
import logging

from fastapi import FastAPI

from app.api.v1 import documents, users
from app.core.config import config
from app.core.logger import setup_logging

setup_logging(log_level=logging.INFO)
app = FastAPI(title="Extracta backend API", version=config.version)

_LOGGER = logging.getLogger()

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
