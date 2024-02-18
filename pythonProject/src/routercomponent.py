from fastapi import APIRouter, Depends
from sqlalchemy import select, insert, text
from sqlalchemy.ext.asyncio import AsyncSession
from src.database import get_session, Session




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
    result = db.execute(stmt).scalars().all()
    return result




