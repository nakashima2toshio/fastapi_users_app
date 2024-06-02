# routers/user_router.py
from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from auth.user_manager import get_user_manager
from auth.auth import jwt_authentication
from schemas.user_schemas import UserCreate, UserRead, UserUpdate

router = APIRouter()

fastapi_users = FastAPIUsers(
    get_user_manager,
    [jwt_authentication]
)

router.include_router(fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"])
router.include_router(fastapi_users.get_register_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
router.include_router(fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"])
router.include_router(fastapi_users.get_verify_router(UserRead), prefix="/auth", tags=["auth"])
router.include_router(fastapi_users.get_users_router(UserRead, UserUpdate), prefix="/users", tags=["users"])
