from pydantic import BaseModel, Field
from datetime import datetime
from app.enums import Status, Category
from typing import Optional
from enum import Enum


class User(BaseModel):
    """
    Represents a user.
    """
    serial: int


class Document(BaseModel):
    """
    Represents a document.
    """
    id: str
    url: str
    user: int
    category: Category
    status: Status = Status.PENDING
    created_at: datetime = Field(default_factory=datetime.now)
    error_message: Optional[str] = None



