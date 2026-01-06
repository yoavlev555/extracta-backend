from datetime import datetime
from enum import StrEnum, auto

from pydantic import BaseModel, Field

class DocumentStatus(StrEnum):
    """
    Enum representing all possible workflow statuses.
    """
    PENDING = auto()
    PROCESSING = auto()
    OCR_PARSED = auto()
    LLM_ANALYZED = auto()
    STORED_IN_STORAGE = auto()
    ERROR = auto()
    SUCCESS = auto()


class DocumentBase(BaseModel):
    document_file_name: str = Field(min_length=3, max_length=512, description="Document File Name")
    storage_key: str = Field(description="Storage Key of the Document in storage")
    created_at: datetime = Field(description="Date of creation of the document")
    document_category: str | None = Field(description="The category of the document")

class Document(DocumentBase):
    document_id: str = Field(min_length=3, max_length=512, description="Unique identifier of the document")
    status: DocumentStatus = Field(description="Status of the document")

class UpdateDocument(BaseModel):
    document_file_name: str | None = Field(min_length=3, max_length=512, description="Document File Name")
    storage_key: str | None = Field(description="Storage Key of the Document in storage")
    document_category: str | None = Field(description="The category of the document")






