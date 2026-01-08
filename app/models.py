from datetime import datetime

from pydantic import BaseModel, Field

from app.enums import Category, Status


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
    category: Category
    user_id: int


class DocumentDB(DocumentCreate):
    """
    DB document object.
    """

    url: str
    category: Category
    user_id: int
    id: str
    status: Status = Field(default=Status.PENDING)
    created_at: datetime = Field(default_factory=datetime.now)
    error_message: str | None = None
