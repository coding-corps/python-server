from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from passlib.context import CryptContext
from datetime import timedelta, datetime
from app.schemas.user_schema import UserCreateSchema, UserUpdatePasswordSchema, UserInDB 
from app.models import User
from fastapi import APIRouter

router = APIRouter()


@router.get("/user")
async def example_route():
    return {"message": "user"}