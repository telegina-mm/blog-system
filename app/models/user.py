from datetime import datetime
from fastapi import FastAPI
from starlette.responses import JSONResponse
from typing import Optional
from flask import app
from pydantic import BaseModel, field_validator


class User(BaseModel):
  id: int
  email: str
  login: str
  password: str
  createdAt: datetime # Дата и время создания
  updatedAt: datetime # Дата и время последнего редактирования

class UserCreate(BaseModel):
    email: str
    login: str
    password: str

    @field_validator('password')
    @classmethod
    def password_length(cls, v: str) -> str:
        if len(v) < 6:
            raise ValueError('Password must be at least 6 characters')
        return v

    @field_validator('login')
    @classmethod
    def login_length(cls, v: str) -> str:
        if len(v) < 3:
            raise ValueError('Login must be at least 3 characters')
        return v

class UserUpdate(BaseModel):
    email: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None

class UserInDB(User):
    password: str