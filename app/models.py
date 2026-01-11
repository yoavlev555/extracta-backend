from datetime import datetime

from pydantic import BaseModel, Field

from app.enums import DocumentStatus


class User(BaseModel):
    """
    Represents a user.
    """

    serial: int


class DocumentCreate(BaseModel):
    """
    Document creation object for front app.
    """

    url: str
    category: str
    user_id: int


class Document(DocumentCreate):
    """
    DB document object.
    """

    url: str
    category: str
    user_id: int
    id: str
    status: DocumentStatus = Field(default=DocumentStatus.PENDING)
    created_at: datetime = Field(default_factory=datetime.now)
    error_message: str | None = None
