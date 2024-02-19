from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update,delete
from src.database import get_session, Session

from src.models import cart_item, CartItemCreate

router = APIRouter(
    prefix="/cart_items",
    tags=["cart_item"]
)


@router.get("/count")
def get_cart_item_count(db: Session = Depends(get_session)):
    stmt = db.query(cart_item).count()
    return {"result":stmt}


@router.get("/all")
def get_all_cart_item(db: Session = Depends(get_session)):
    stmt = select(cart_item)
    result = db.execute(stmt).all()
    result = [row._asdict() for row in result]
    return result

@router.post("/add")
def add_cart(new_cart_item: CartItemCreate,db: Session = Depends(get_session)):
    stmt = insert(cart_item).values(**new_cart_item.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.put("/update")
def update_cart(old_name:str,new_name:str,new_product_id: int,new_cart_id:int,new_service_id:int,db: Session = Depends(get_session)):
    stmt = update(cart_item).where(cart_item.c.name == old_name).values(name = new_name, product_id = new_product_id, cart_id = new_cart_id, service_id = new_service_id)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.delete("/delete")
def update_cart(old_name:str,db: Session = Depends(get_session)):
    stmt = delete(cart_item).where(cart_item.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}