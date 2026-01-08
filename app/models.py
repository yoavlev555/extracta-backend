from pydantic import BaseModel, Field
from datetime import datetime
from app.enums import Status, Category
from typing import Optional


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
    error_message: Optional[str] = None