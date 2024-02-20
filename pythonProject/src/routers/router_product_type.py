from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update, delete
from src.database import get_session, Session
from src.schemas.schema_product_type import ProductTypeCreate
from src.models import product_type

router = APIRouter(
    prefix="/product_types",
    tags=["product type"]
)


@router.get("/name")
def get_product_type_name(db: Session = Depends(get_session)):
    stmt = select(product_type)
    result = db.execute(stmt).scalars().all()
    return result


@router.post("/add")
def add_product_type(new_service: ProductTypeCreate, db: Session = Depends(get_session)):
    stmt = insert(product_type).values(**new_service.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}


@router.put("/update")
def update_product_type(old_name: str, new_name: str, db: Session = Depends(get_session)):
    stmt = update(product_type).where(product_type.c.name == old_name).values(name=new_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}


@router.delete("/delete")
def delete_product_type(old_name: str, db: Session = Depends(get_session)):
    stmt = delete(product_type).where(product_type.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}