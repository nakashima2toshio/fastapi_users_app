# auth/auth.py
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport

SECRET = "SECRET"

# Define the transport
bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


jwt_authentication = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
