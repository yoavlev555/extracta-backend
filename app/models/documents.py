from pydantic import BaseModel, Field

from enums import DocumentStatus


# ======== REQUEST MODELS ======== #
class DocumentBase(BaseModel):
    file_name: str = Field(min_length=3, max_length=512, description="Document File Name")
    storage_key: str = Field(description="Storage Key of the Document in storage")
    category: str | None = Field(description="The category of the document")
    created_at: str = Field(description="The creation time of the document")


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    file_name: str | None = Field(min_length=3, max_length=512, description="Document File Name")
    category: str | None = Field(description="The category of the document")


class DocumentBulkDelete(BaseModel):
    document_ids: list[str] = Field(description="List of document IDs to delete", max_length=100)


# ======== RESPONSE MODELS ======== #
class Document(DocumentBase):
    id: str = Field(description="Unique identifier of the document")
    status: DocumentStatus = Field(description="Status of the document")
    error_message: str | None = Field(description="Error message if there is a problem")


class DocumentBulkDeleteResponse(BaseModel):
    deleted_count: int = Field(description="Number of deleted documents")
    failed_ids: list[str] | None = Field(description="List of failed document IDs", max_length=100)
