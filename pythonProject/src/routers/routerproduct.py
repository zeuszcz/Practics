from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.product_service import ProductService

router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@router.get("/name")
def get_product_name(new_db: Session = Depends(get_session)):
    return ProductService.get_product_name(db=new_db)


@router.post("/add")
def add_product(newcost:int,newname:str, new_db: Session = Depends(get_session)):
    return ProductService.add_product(new_cost=newcost,new_name=newname,db=new_db)


@router.put("/update")
def update_product(oldname: str, newname: str, newcost: int, new_db: Session = Depends(get_session)):
    return ProductService.update_product(old_name=oldname,new_name=newname,new_cost=newcost,db=new_db)


@router.delete("/delete")
def delete_product(oldname: str, new_db: Session = Depends(get_session)):
    return ProductService.delete_product(old_name=oldname,db=new_db)
