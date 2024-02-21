from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.product_type_service import ProductTypeService
from src.schemas.schema_product_type import ProductTypeCreate,ProductTypeUpdate


router = APIRouter(
    prefix="/product_types",
    tags=["product type"]
)


@router.get("/name")
def get_product_type_name(new_db: Session = Depends(get_session)):
    return ProductTypeService.get_product_type_name(db=new_db)


@router.post("/add")
def add_product_type(newproducttype: ProductTypeCreate, new_db: Session = Depends(get_session)):
    return ProductTypeService.add_product_type(new_product_type=newproducttype,db=new_db)


@router.put("/update")
def update_product_type(oldname: str, newproducttype: ProductTypeUpdate, new_db: Session = Depends(get_session)):
    return ProductTypeService.update_product_type(old_name=oldname,new_product_type=newproducttype,db=new_db)


@router.delete("/delete")
def delete_product_type(oldname: str, new_db: Session = Depends(get_session)):
    return ProductTypeService.delete_product_type(old_name=oldname, db=new_db)
