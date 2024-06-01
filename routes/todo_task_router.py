# routers/todo_task_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.todo_task_schemas import TodoTaskCreate, TodoTask
from cruds.todo_task_crud import get_todo_tasks, create_todo_task
from databases.database import get_db
from auth.auth import jwt_authentication
from fastapi_users import FastAPIUsers
from auth.user_manager import get_user_manager

router = APIRouter()

fastapi_users = FastAPIUsers(get_user_manager, [jwt_authentication])


@router.get("/todos", response_model=List[TodoTask])
def read_todo_tasks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_todo_tasks(db, skip=skip, limit=limit)


@router.post("/todos", response_model=TodoTask)
def create_todo_item(todo: TodoTaskCreate, db: Session = Depends(get_db), user=Depends(fastapi_users.current_user())):
    return create_todo_task(db, todo, user.id)
