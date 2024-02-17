from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import session
from models import cart


router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)


@router.get("/")
async def get_specific_operations():
    query = select(cart).where(cart.id == 1)
    result = await session.execute(query)
    return result.all()


