from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.product_service import ProductService
from src.schemas.schema_product import ProductCreate,ProductUpdate

router = APIRouter(
    prefix="/product",
    tags=["product"]
)


@router.get("/name")
def get_product_name(new_db: Session = Depends(get_session)):
    return ProductService.get_product_name(db=new_db)


@router.post("/add")
def add_product(newproduct:ProductCreate, new_db: Session = Depends(get_session)):
    return ProductService.add_product(new_product=newproduct,db=new_db)


@router.put("/update")
def update_product(oldname: str, newproduct:ProductUpdate, new_db: Session = Depends(get_session)):
    return ProductService.update_product(old_name=oldname,new_product=newproduct,db=new_db)


@router.delete("/delete")
def delete_product(oldname: str, new_db: Session = Depends(get_session)):
    return ProductService.delete_product(old_name=oldname,db=new_db)
