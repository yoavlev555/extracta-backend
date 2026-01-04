import time
import threading
from typing import List
from models import Document
from enums import Status


def start_processing_simulation(doc_id: str, db: List[Document]):
    thread = threading.Thread(target=_run_simulation, args=(doc_id, db))
    thread.daemon = True
    thread.start()


def _run_simulation(doc_id: str, db: List[Document]):
    """
    Worker logic that strictly follows: FETCH -> PROCESS -> UPDATE
    """
 
    print(f"[Worker] Job received for ID: {doc_id}")
    time.sleep(5)

    doc = next((document for document in db if document.id == doc_id), None)

    if not doc:
        print(f"[Worker] Error: Document {doc_id} doesn't exist")
        return

    doc.status = Status.PROCESSING
    print(f"[Worker] Processing {doc_id}...")

    time.sleep(10)

    doc.status = Status.SUCCESS
    print(f"[Worker] {doc_id} is ready!")