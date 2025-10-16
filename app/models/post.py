from datetime import datetime

from pydantic import BaseModel, Field


class Post(BaseModel):
    id: int
    authorId: int
    title: str
    content: str
    createdAt: datetime
    updatedAt: datetime


class PostCreate(BaseModel):
    title: str = Field(
        min_length=1,
        max_length=200,
        description="Title must not be empty and can not be longer than 200 characters",
    )
    content: str = Field(
        min_length=10, description="Content must be at least 10 characters"
    )


class PostUpdate(BaseModel):
    title: str | None = Field(
        None,
        min_length=1,
        max_length=200,
        description="Title must not be empty and can not be longer than 200 characters",
    )
    content: str | None = Field(
        None, min_length=10, description="Content must be at least 10 characters"
    )
