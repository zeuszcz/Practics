from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update, delete
from src.database import get_session, Session

from src.schemas.schema_build import BuildCreate
from src.models import build

router = APIRouter(
    prefix="/builds",
    tags=["build"]
)


@router.get("/count")
def get_build_count(db: Session = Depends(get_session)):
    stmt = db.query(build).count()
    return {"result": stmt}


@router.get("/all")
def get_all_build(db: Session = Depends(get_session)):
    stmt = select(build)
    result = db.execute(stmt).all()
    result = [row._asdict() for row in result]
    return result


@router.post("/add")
def add_build(new_build: BuildCreate, db: Session = Depends(get_session)):
    stmt = insert(build).values(**new_build.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}


@router.put("/update")
def update_build(old_name: str, new_name: str, new_product_id: int, new_product_component_id: int, new_service_id: int,
                db: Session = Depends(get_session)):
    stmt = update(build).where(build.c.name == old_name).values(name=new_name, product_id=new_product_id,
                                                                        product_component_id=new_product_component_id)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}


@router.delete("/delete")
def update_build(old_name: str, db: Session = Depends(get_session)):
    stmt = delete(build).where(build.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}