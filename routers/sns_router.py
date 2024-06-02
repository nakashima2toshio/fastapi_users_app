# routers/sns_router.py
from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.sns_schemas import PostCreate, Post
from cruds.sns_crud import get_posts, create_post
from app_databases.database import get_db
from auth.auth import jwt_authentication
from fastapi_users import FastAPIUsers
from auth.user_manager import get_user_manager

router = APIRouter()

fastapi_users = FastAPIUsers(get_user_manager, [jwt_authentication])


@router.get("/posts", response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_posts(db, skip=skip, limit=limit)


@router.post("/posts", response_model=Post)
def create_new_post(post: PostCreate, db: Session = Depends(get_db), user=Depends(fastapi_users.current_user())):
    return create_post(db, post, user.id)
