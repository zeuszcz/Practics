from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session, Session
from src.models import ProductCreate, product

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
    result = db.execute(stmt).scalars().all()
    return result

@router.post("/add")
def add_product(new_product: ProductCreate,db: Session = Depends(get_session)):
    stmt = insert(product).values(**new_product.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.post("/update")
def update_product(old_name:str,new_name:str,new_cost: int,new_product_component: ProductCreate,db: Session = Depends(get_session)):
    stmt = update(product).where(product.c.name == old_name).values(name = new_name, cost = new_cost)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}