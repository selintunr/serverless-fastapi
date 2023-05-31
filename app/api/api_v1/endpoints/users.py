
from fastapi import APIRouter

router = APIRouter()

#we added as prefix so that we can use it as /
@router.get("/")
async def get_users():
    return {"message": "Get Users"}

# /users

