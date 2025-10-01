from datetime import datetime
from typing import Optional
from pydantic import BaseModel, field_validator, validator

class Post(BaseModel):
    id: int
    authorId: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime

class PostCreate(BaseModel):
    title: str
    content: str
    @field_validator('title')
    @classmethod
    def title_length(cls, v: str) -> str:
        if len(v) < 1:
            raise ValueError('Title cannot be empty')
        if len(v) > 200:
            raise ValueError('Title too long')
        return v

    @field_validator('content')
    @classmethod
    def content_length(cls, v: str) -> str:
        if len(v) < 10:
            raise ValueError('Content must be at least 10 characters')
        return v

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None