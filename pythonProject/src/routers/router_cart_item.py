from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.cart_item_service import CartItemService
from src.schemas.schema_cart_item import CartItemCreate,CartItemUpdate


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
def add_cart_item(newcartitem:CartItemCreate, new_db: Session = Depends(get_session)):
    return CartItemService.add_cart_item(new_cart_item=newcartitem,db=new_db)


@router.put("/update")
def update_cart_item(oldCI: int,newcartitem:CartItemUpdate,
                new_db: Session = Depends(get_session)):
    return CartItemService.update_cart_item(CI=oldCI,new_cart_item=newcartitem,db=new_db)


@router.delete("/delete")
def delete_cart_item(cart_id: int, new_db: Session = Depends(get_session)):
    return CartItemService.delete_cart_item(CI=cart_id,db=new_db)


