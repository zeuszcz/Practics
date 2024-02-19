from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update, delete
from src.database import get_session, Session
from src.models import ServiceCreate, service

router = APIRouter(
    prefix="/services",
    tags=["service"]
)
@router.get("/name")
def get_service_name(db: Session = Depends(get_session)):
    stmt = text("""
                    select  name
                    from service  
                """)
    result = db.execute(stmt).scalars().all()
    return result

@router.post("/add")
def add_service(new_service: ServiceCreate,db: Session = Depends(get_session)):
    stmt = insert(service).values(**new_service.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.put("/update")
def update_service(old_name:str,new_name:str,new_cost: int,db: Session = Depends(get_session)):
    stmt = update(service).where(service.c.name == old_name).values(name = new_name, cost = new_cost)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.delete("/delete")
def delete_service(old_name:str,db: Session = Depends(get_session)):
    stmt = delete(service).where(service.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}