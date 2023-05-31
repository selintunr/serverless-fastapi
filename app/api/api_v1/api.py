

#İmport users as module

from fastapi import APIRouter
from .endpoints import users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])