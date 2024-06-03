# auth/user_manager.py
import uuid
from fastapi import Depends, Request
from fastapi_users.manager import BaseUserManager
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from models.user_models import User, UserCreate
from app_databases.database import get_db
from sqlalchemy.ext.asyncio import AsyncSession

SECRET = "SECRET"


class UserManager(BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    def __init__(self, user_db: SQLAlchemyUserDatabase):
        super().__init__(user_db)
        self.user_db = user_db

    async def get_by_email(self, user_email: str) -> User:
        query = "SELECT * FROM users WHERE email = :email"
        user = await self.user_db.fetch_one(query=query, values={"email": user_email})
        if user is None:
            raise UserNotExists()
        return User(**user)

    async def on_after_register(self, user: User, request: Request = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(self, user: User, token: str, request: Request = None):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(self, user: User, token: str, request: Request = None):
        print(f"Verification requested for user {user.id}. Verification token: {token}")


async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_user_manager(user_db=Depends(get_user_db)) -> UserManager:
    yield UserManager(user_db)
