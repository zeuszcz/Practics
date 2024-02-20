from fastapi import APIRouter, Depends
from src.database import get_session, Session
from src.services.component_service import ComponentService

router = APIRouter(
    prefix="/productcomponent",
    tags=["productcomponent"]
)

@router.get("/ram")
def get_ram_component(new_db: Session = Depends(get_session)):
    return ComponentService.get_ram_component(db=new_db)


@router.get("/video")
def get_video_component(new_db: Session = Depends(get_session)):
    return ComponentService.get_video_component(db=new_db)


@router.get("/all")
def get_ordered_component(new_db: Session = Depends(get_session)):
    return ComponentService.get_ordered_component(db=new_db)


@router.post("/add")
def add_product_component(new_pti:int,newname:str,newcost:int, new_db: Session = Depends(get_session)):
    return ComponentService.add_product_component(pti=new_pti,new_name=newname,new_cost=newcost,db=new_db)


@router.put("/update")
def update_product_component(oldname: str, new_pti:int,newname:str,newcost:int, new_db: Session = Depends(get_session)):
    return ComponentService.update_product_component(old_name=oldname,pti=new_pti,new_name=newname,new_cost=newcost,db=new_db)


@router.delete("/delete")
def delete_product_component(oldname: str, new_db: Session = Depends(get_session)):
    return ComponentService.delete_product_component(old_name=oldname,db=new_db)
