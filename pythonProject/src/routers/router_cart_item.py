from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.cart_item_service import CartItemService


router = APIRouter(
    prefix="/cart_items",
    tags=["cart_item"]
)


@router.get("/count")
def get_cart_item_count(new_db: Session = Depends(get_session)):
    return CartItemService.get_cart_item_count(db=new_db)


@router.get("/all")
def get_all_cart_item(new_db: Session = Depends(get_session)):
    return CartItemService.get_all_cart_item(db=new_db)


@router.post("/add")
def add_cart_item(newSI:int,newPI:int,newCI:int, new_db: Session = Depends(get_session)):
    return CartItemService.add_cart_item(new_SI=newSI,new_PI=newPI,new_CI=newCI,db=new_db)


@router.put("/update")
def update_cart_item(oldCI: int, product_id: int, cart_id: int, service_id: int,
                new_db: Session = Depends(get_session)):
    return CartItemService.update_cart_item(CI=oldCI,new_product_id=product_id,new_cart_id=cart_id,new_service_id=service_id,db=new_db)


@router.delete("/delete")
def delete_cart_item(cart_id: int, new_db: Session = Depends(get_session)):
    return CartItemService.delete_cart_item(CI=cart_id,db=new_db)
