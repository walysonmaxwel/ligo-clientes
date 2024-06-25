from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import jwt
import datetime
import os

router = APIRouter()

SECRET_KEY = os.getenv("SECRET_KEY")
JWT_EXPIRATION_TIME_SECONDS = int(os.getenv("JWT_EXPIRATION_TIME_SECONDS", 3600))

class User(BaseModel):
    id: int
    name: str
    address: str
    email: str

@router.post("/generate_jwt")
async def generate_jwt(user: User):
    payload = {
        "id": user.id,
        "name": user.name,
        "address": user.address,
        "email": user.email,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=JWT_EXPIRATION_TIME_SECONDS)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return {"token": token}