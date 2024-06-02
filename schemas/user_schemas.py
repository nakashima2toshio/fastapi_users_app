# schemas/users_schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    username: str


class UserCreate(schemas.BaseUserCreate):
    username: str


class UserUpdate(schemas.BaseUserUpdate):
    username: Optional[str]

    class Config:
        from_attributes = True
