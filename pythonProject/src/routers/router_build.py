from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.build_service import BuildService
from src.schemas.schema_build import BuildCreate,BuildUpdate

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
def add_build(newbuild:BuildCreate, new_db: Session = Depends(get_session)):
    return BuildService.add_build(new_build=newbuild,db=new_db)


@router.put("/update")
def update_build(oldname: str, newbuild:BuildUpdate, new_db: Session = Depends(get_session)):
    return BuildService.update_build(old_name=oldname,new_build=newbuild,db=new_db)


@router.delete("/delete")
def delete_build(oldname: str, new_db:Session = Depends(get_session)):
    return BuildService.delete_build(old_name=oldname,db=new_db)