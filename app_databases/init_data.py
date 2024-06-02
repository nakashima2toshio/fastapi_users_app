# app_databases/init_data.py
import sys
import os

# プロジェクトのルートディレクトリをパスに追加
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import uuid
from sqlalchemy.orm import Session
from app_databases.database import SessionLocal  # 相対インポートを使用
from models.user_models import User
from models.todo_task_models import TodoTask
from models.sns_models import Post


def init_db():
    db: Session = SessionLocal()
    try:
        # ユーザーの作成
        user = User(
            id=str(uuid.uuid4()),  # UUIDを文字列に変換
            username="testuser",
            email="testuser@example.com",
            hashed_password="hashedpassword",
            is_active=True,
            is_superuser=False,
        )
        db.add(user)
        db.commit()
        db.refresh(user)

        # Todoタスクの作成
        todo_task = TodoTask(
            title="Sample Task",
            description="This is a sample task",
            owner_id=user.id  # owner_idは文字列
        )
        db.add(todo_task)
        db.commit()

        # SNS投稿の作成
        post = Post(
            title="Sample Post",
            content="This is a sample post",
            owner_id=user.id  # owner_idは文字列
        )
        db.add(post)
        db.commit()

    finally:
        db.close()


if __name__ == "__main__":
    init_db()
