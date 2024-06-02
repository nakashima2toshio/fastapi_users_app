# schemas/todo_task_schemas.py
from pydantic import BaseModel
from typing import List, Optional


class TodoTaskBase(BaseModel):
    title: str
    description: Optional[str] = None


class TodoTaskCreate(TodoTaskBase):
    pass


class TodoTask(TodoTaskBase):
    id: int
    owner_id: int

    # class Config:
    #     orm_mode = True
    class Config:
        from_attributes = True
