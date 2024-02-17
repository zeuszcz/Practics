from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session, Session
import sqlalchemy.orm

from src.models import cart

router = APIRouter(
    prefix="/cart",
    tags=["cart"]
)


@router.get("/")
def get_cartcount(db: Session = Depends(get_session)):
    stmt = text("""
                    select COUNT( name)
                    from cart
                """)
    result = db.execute(stmt).scalar_one_or_none()
    return result
# def get_specific_operations(session: get_session):
#     query = select(cart).where(cart.id == 1)
#     result = Session.execute(query)
#     return result.all()


