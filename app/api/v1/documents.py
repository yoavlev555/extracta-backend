from typing import List

from fastapi import APIRouter

from models.documents import Document

router = APIRouter(tags=["Documents"])


@router.get("/documents")
def get_all_documents() -> List[Document]:
    """
    Get all documents for a specific user.
    """
    pass

@router.get("/documents/{document_id}")
def get_all_documents(document_id: str) -> List[Document]:
    """
    Get document with a specific id.
    """
    pass
