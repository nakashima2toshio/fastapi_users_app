# auth/user_manager.py
import uuid
from fastapi import Depends, Request
from fastapi_users.manager import BaseUserManager, UserManagerDependency
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from models.user_models import User
from app_databases.database import get_db
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase

SECRET = "SECRET"


class UserManager(BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(self, user: User, request: Request = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Request = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Request = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


user_db = SQLAlchemyUserDatabase(User, get_db)


async def get_user_manager(user_db=Depends(get_db)) -> UserManager:
    yield UserManager(user_db)
