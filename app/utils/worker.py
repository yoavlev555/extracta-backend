import threading
import time

from enums import DocumentStatus

from app.core.logger import init_logger
from app.models.documents import Document

logger = init_logger(__name__)


def start_processing_simulation(doc_id: str, db: list[Document]) -> None:
    thread = threading.Thread(target=_run_simulation, args=(doc_id, db))
    thread.daemon = True
    thread.start()


def _run_simulation(doc_id: str, db: list[Document]) -> None:
    """
    Worker logic that strictly follows: FETCH -> PROCESS -> UPDATE
    """

    logger.info(f"Job received for ID: {doc_id}")
    time.sleep(5)

    doc = next((document for document in db if document.id == doc_id), None)

    if not doc:
        logger.error(f"Error: Document {doc_id} doesn't exist")
        return

    doc.status = DocumentStatus.PROCESSING
    logger.info(f"Processing {doc_id}...")

    time.sleep(10)

    doc.status = DocumentStatus.SUCCESS
    logger.info(f"{doc_id} is ready!")
