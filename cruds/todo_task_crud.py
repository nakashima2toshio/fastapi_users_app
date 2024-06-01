# cruds/todo_task.py
from sqlalchemy.orm import Session
from models.todo_task_models import TodoTask
from schemas.todo_task_schemas import TodoTaskCreate


def get_todo_tasks(db: Session, skip: int = 0, limit: int = 10):
    return db.query(TodoTask).offset(skip).limit(limit).all()


def create_todo_task(db: Session, todo: TodoTaskCreate, user_id: int):
    db_todo = TodoTask(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
