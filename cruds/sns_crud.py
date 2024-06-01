# cruds/sns_crud.py
from sqlalchemy.orm import Session
from models.sns_models import Post
from schemas.sns_schemas import PostCreate


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: PostCreate, user_id: int):
    db_post = Post(**post.dict(), owner_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post
