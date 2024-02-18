from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session, Session





router = APIRouter(
    prefix="/product",
    tags=["product"]
)
@router.get("/name")
def get_product_name(db: Session = Depends(get_session)):
    stmt = text("""
                    select  name
                    from product  
                """)
    result = db.execute(stmt).scalar_one_or_none()
    return result