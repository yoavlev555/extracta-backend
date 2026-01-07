from datetime import datetime

from fastapi import APIRouter, Path, Query, status
from fastapi_pagination import Page

from app.models.documents import Document, DocumentBulkDelete, DocumentBulkDeleteResponse, DocumentCreate, DocumentStatus, DocumentUpdate

router = APIRouter(tags=["Documents"])

RESPONSES = {404: {"description": "Document not found"}, 400: {"description": "Invalid document ID format"}}


@router.get("/documents", response_model=Page[Document])
async def get_all_documents(
    name: str | None = Query(default=None, max_length=512, description="Filter documents by name"),
    document_status: DocumentStatus | None = Query(default=None, description="Filter documents by status"),
    category: str | None = Query(default=None, description="Filter documents by category"),
    created_after: datetime | None = Query(default=None, description="Filter documents created after this date"),
    created_before: datetime | None = Query(default=None, description="Filter documents created before this date"),
    sort_by: str = Query(default="created_at", pattern="^(created_at|file_name|status)$"),
    sort_order: str = Query(default="desc", pattern="^(asc|desc)$"),
) -> Page[Document]:
    """
    Retrieve a paginated list of documents accessible to the user with optional filtering and sorting.

    Args:
        name: Filter documents containing this text in their file name (case-insensitive partial match)
        document_status: Filter by document processing status (PENDING, PROCESSING, OCR_PARSED, LLM_ANALYZED, etc.)
        category: Filter by document category (exact match)
        created_after: Return only documents created after this datetime (inclusive)
        created_before: Return only documents created before this datetime (inclusive)
        sort_by: Field to sort results by. Options: 'created_at', 'file_name', 'status' (default: 'created_at')
        sort_order: Sort direction. Options: 'asc' (ascending), 'desc' (descending) (default: 'desc')

    Query Parameters auto-injected by fastapi-pagination:
        page: Page number to retrieve (default: 1)
        size: Number of items per page (default: 50)

    Returns:
        Page[Document]: Paginated response containing:
            - items: List of Document objects matching the criteria
            - total: Total number of matching documents
            - page: Current page number
            - size: Number of items per page
            - pages: Total number of pages available

    Example:
        GET /api/v1/documents?document_status=PENDING&sort_by=created_at&sort_order=desc&page=1&size=20
    """


@router.get("/documents/{document_id}", response_model=Document, responses=RESPONSES)
async def get_document_by_id(document_id: str = Path(..., min_length=1, description="The document ID")) -> Document:
    """
    Retrieve a single document by its unique identifier for the user.

    Args:
        document_id: Unique identifier of the document to retrieve

    Returns:
        Document object with the specified document_id

    Raises:
        404: Document not found - The specified document ID does not exist for the user
        400: Invalid document ID format

    Example:
        GET /api/v1/documents/abc123
    """


@router.post("/documents", response_model=Document, status_code=status.HTTP_201_CREATED)
async def create_document(request: DocumentCreate) -> Document:
    """
    Create a new document in the system for a specific user.

    Args:
        request: Document creation data (DocumentCreate)

    Returns:
        Document: The newly created document object with:
            - Generated unique ID
            - Initial status set to PENDING
            - All provided metadata

    Example:
        POST /api/v1/documents
        {
            "username": "john_doe",
            "file_name": "invoice_2024.pdf",
            "storage_key": "s3://bucket/invoice_2024.pdf",
            "category": "invoices",
            "created_at": "2024-01-15T10:30:00Z"
        }
    """


@router.patch("/documents/{document_id}", response_model=Document, responses=RESPONSES)
async def update_document(request: DocumentUpdate, document_id: str = Path(..., min_length=1, description="The document ID")) -> Document:
    """
    Partially update an existing document's metadata.

    Args:
        request: Partial document data (DocumentUpdate) containing fields to update:
        document_id: Unique identifier of the document to update

    Returns:
        Document: The updated document object with all current values

    Raises:
        404: Document not found - The specified document ID does not exist
        400: Invalid document ID format or validation error on update fields

    Example:
        PATCH /api/v1/documents/abc123
        {
            "file_name": "updated_invoice_2024.pdf",
            "category": "processed_invoices"
        }
    """


@router.delete("/documents/bulk", response_model=DocumentBulkDeleteResponse, status_code=status.HTTP_200_OK)
async def delete_documents_bulk(request: DocumentBulkDelete) -> DocumentBulkDeleteResponse:
    """
    Delete multiple documents in a single batch operation.

    Args:
        request: Bulk delete request (DocumentBulkDelete) containing:
            - document_ids: List of document IDs to delete (typically limited to max 100)

    Returns:
        DocumentBulkDeleteResponse: Summary of the deletion operation containing:
            - deleted_count: Number of documents successfully deleted
            - failed_ids: List of document IDs that could not be deleted (optional)

    Example:
        DELETE /api/v1/documents/bulk
        {
            "document_ids": ["abc123", "def456", "ghi789"]
        }

        Response:
        {
            "deleted_count": 3,
            "failed_ids": [],
        }
    """


@router.delete("/documents/{document_id}", status_code=status.HTTP_204_NO_CONTENT, responses=RESPONSES)
async def delete_document_by_id(document_id: str = Path(..., min_length=1, description="The document ID")) -> None:
    """
    Delete a single document by its unique identifier.

    Args:
        document_id: Unique identifier of the document to delete

    Raises:
        404: Document not found - The specified document ID does not exist
        400: Invalid document ID format

    Example:
        DELETE /api/v1/documents/abc123
    """
