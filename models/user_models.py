# models/users_models.py
import uuid

from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, String, Boolean
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from app_databases.database import Base


class User(SQLAlchemyBaseUserTable, Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))  # UUIDを文字列として保存
    username = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    is_verified = Column(Boolean, default=False)


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False
    username: str