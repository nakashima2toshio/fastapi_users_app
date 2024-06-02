# schemas/sns_schemas.py
from pydantic import BaseModel
from typing import List, Optional


class PostBase(BaseModel):
    title: str
    content: Optional[str] = None


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True
