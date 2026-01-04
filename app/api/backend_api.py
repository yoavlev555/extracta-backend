import datetime
from importlib.metadata import version, PackageNotFoundError

from fastapi import FastAPI
from app.constants import PACKAGE_NAME

try:
    VERSION = version(PACKAGE_NAME)
except PackageNotFoundError:
    VERSION = "0.0.0-dev"
app = FastAPI(version=VERSION)

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service:": PACKAGE_NAME,
        "version": VERSION,
        "timestamp": datetime.datetime.now(datetime.UTC)
    }

@app.put("/documents/{document_id}")
async def upload_document(document_id: str):
    # 1. Upload document to docsDB
    # 2. Send Job Request to JobQueue
    pass
