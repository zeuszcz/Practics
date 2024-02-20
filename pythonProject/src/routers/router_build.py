from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.build_service import BuildService

router = APIRouter(
    prefix="/builds",
    tags=["build"]
)


@router.get("/count")
def get_build_count(new_db: Session = Depends(get_session)):
    return BuildService.get_build_count(db=new_db)


@router.get("/all")
def get_all_build(new_db: Session = Depends(get_session)):
    return BuildService.get_all_build(db=new_db)


@router.post("/add")
def add_build(oldname: str, newname: str, newproduct_id: int, newproduct_component_id: int, new_db: Session = Depends(get_session)):
    return BuildService.add_build(old_name=oldname,new_name=newname,new_product_id=newproduct_id,new_product_component_id=newproduct_component_id,db=new_db)


@router.put("/update")
def update_build(oldname: str, newname: str, newproduct_id: int, newproduct_component_id: int, new_db: Session = Depends(get_session)):
    return BuildService.update_build(old_name=oldname,new_name=newname,new_product_id=newproduct_id,new_product_component_id=newproduct_component_id,db=new_db)


@router.delete("/delete")
def delete_build(oldname: str, new_db:Session = Depends(get_session)):
    return BuildService.delete_build(old_name=oldname,db=new_db)