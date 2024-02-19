from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session, Session
from src.models import ProductComponentCreate, product_component

router = APIRouter(
    prefix="/productcomponent",
    tags=["productcomponent"]
)
@router.get("/type")
def get_productcomponent_type(db: Session = Depends(get_session)):
    stmt = text("""
                    select  product_component.name, product_type.name
                    from product_component 
                    inner join product_type
                    on product_type_id = product_type.id
                """)
    result = db.execute(stmt).scalars().all()
    return result

@router.get("/ram")
def get_ram_component(db: Session = Depends(get_session)):
    stmt = text("""
                    select  product_component.name
                    from product_component 
                    where product_type_id = 3
                """)
    result = db.execute(stmt).scalars().all()
    return result


@router.get("/video/count")
def get_count_video_component(db: Session = Depends(get_session)):
    stmt = text("""
                    select  count(product_component.name)
                    from product_component 
                    where product_type_id = 2
                """)
    result = db.execute(stmt).scalars().all()
    return result

@router.get("/all")
def get_ordered_component(db: Session = Depends(get_session)):
    stmt = text("""
                    select * from product_component order by cost
                """)
    result = db.execute(stmt).scalars().all()
    return result

@router.get("/count")
def get_component_count(db: Session = Depends(get_session)):
    stmt = text("""
                    select  count( product_type.name ), product_type.name  
                    from product_component 
                    inner join product_type
                    on product_type_id = product_type.id
                    group by product_type.name
                """)
    result = db.execute(stmt).all()
    result = [row._asdict() for row in result]
    return result

@router.post("/add")
def add_product_component(new_product_component: ProductComponentCreate,db: Session = Depends(get_session)):
    stmt = insert(product_component).values(**new_product_component.dict())
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.post("/update")
def update_product_component(old_name:str,pti: int,new_name:str,new_cost: int,db: Session = Depends(get_session)):
    stmt = update(product_component).where(product_component.c.name == old_name).values(product_type_id = pti,name = new_name, cost = new_cost)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}

@router.post("/delete")
def delete_product_component(old_name:str,db: Session = Depends(get_session)):
    stmt = delete(product_component).where(product_component.c.name == old_name)
    result = db.execute(stmt)
    db.commit()
    return {"status": "complete"}