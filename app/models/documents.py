from enums import DocumentStatus
from pydantic import BaseModel, Field

MAX_DELETE_COUNT = 20
MAX_NAME_LENGTH = 512
MIN_NAME_LENGTH = 3


# ======== REQUEST MODELS ======== #
class DocumentBase(BaseModel):
    file_name: str = Field(min_length=MIN_NAME_LENGTH, max_length=MAX_NAME_LENGTH, description="Document File Name")
    storage_key: str = Field(description="Storage Key of the Document in storage")
    category: str | None = Field(description="The category of the document")
    created_at: str = Field(description="The creation time of the document")


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    file_name: str | None = Field(min_length=MIN_NAME_LENGTH, max_length=MAX_NAME_LENGTH, description="Document File Name")
    category: str | None = Field(description="The category of the document")


class DocumentBulkDelete(BaseModel):
    document_ids: list[str] = Field(description="List of document IDs to delete", max_length=MAX_DELETE_COUNT)


# ======== RESPONSE MODELS ======== #
class Document(DocumentBase):
    id: str = Field(description="Unique identifier of the document")
    status: DocumentStatus = Field(description="Status of the document")
    error_message: str | None = Field(description="Error message if there is a problem")


class DocumentBulkDeleteResponse(BaseModel):
    deleted_count: int = Field(description="Number of deleted documents", max_length=MAX_DELETE_COUNT)
    failed_ids: list[str] | None = Field(description="List of failed document IDs", max_length=MAX_DELETE_COUNT)
