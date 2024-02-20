from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.service_service import ServiceService

router = APIRouter(
    prefix="/services",
    tags=["service"]
)


@router.get("/name")
def get_service_name(new_db: Session = Depends(get_session)):
    return ServiceService.get_service_name(db=new_db)


@router.post("/add")
def add_service(newname:str,newcost:int, new_db: Session = Depends(get_session)):
    return ServiceService.add_service(new_name = newname,new_cost=newcost,db=new_db)


@router.put("/update")
def update_service(oldname: str, newname: str, newcost: int, new_db: Session = Depends(get_session)):
    return ServiceService.update_service(old_name=oldname,new_name=newname,new_cost=newcost,db=new_db)


@router.delete("/delete")
def delete_service(oldname: str, new_db: Session = Depends(get_session)):
    return ServiceService.delete_service(old_name=oldname,db=new_db)
